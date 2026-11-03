---
title: Chapitre 11 — Sécuriser WSUS et la chaîne de mise à jour
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie IV — WSUS
  - index.md
---

> 🧱 **Les bases**
>
> - **HTTP** transmet en clair ; **HTTPS** chiffre la communication et authentifie le serveur grâce à un **certificat**.
> - Une attaque de l'**homme du milieu** (*man-in-the-middle*) consiste à s'interposer entre un client et un serveur pour lire ou modifier ce qu'ils échangent.
> - La **chaîne d'approvisionnement** (*supply chain*) désigne tout ce par quoi un logiciel passe avant d'arriver chez vous : éditeur, serveurs de distribution, outils de déploiement.

## 11.1 Pourquoi c'est une cible

Le système de mises à jour **installe du code avec les droits SYSTEM sur toutes les machines**. Qui le contrôle contrôle le parc. C'est vrai pour WSUS, pour ConfigMgr, pour Intune, et pour les outils de mise à jour des éditeurs tiers. L'attaque contre la chaîne de mise à jour de SolarWinds Orion (2020), où une mise à jour légitime et signée contenait une porte dérobée, en est l'exemple le plus connu.

## 11.2 WSUS en HTTP : le risque réseau

En HTTP (port 8530), un attaquant présent sur le réseau peut s'interposer et proposer de faux « correctifs ». Le client n'accepte que des fichiers signés par Microsoft, mais des **outils légitimes signés par Microsoft** (comme PsExec) peuvent être détournés avec des paramètres malveillants. Ces attaques sont publiques depuis 2015 (**WSUSpect**), puis 2020 (**WSuspicious**, élévation de privilèges locale via le proxy de l'utilisateur, que Microsoft a corrigée en faisant utiliser par défaut le proxy système). Des travaux offensifs plus récents continuent de montrer que WSUS en HTTP reste un vecteur (relais d'authentification notamment).

✅ **La seule réponse durable : WSUS en HTTPS (port 8531)** avec un certificat d'une autorité de confiance interne.

1. Émettre un certificat serveur (PKI d'entreprise) au **nom DNS complet** utilisé par les clients.
2. Dans IIS, lier le site WSUS en **HTTPS sur 8531** avec ce certificat.
3. Exiger SSL sur les répertoires virtuels sensibles : `ApiRemoting30`, `ClientWebService`, `DSSAuthWebService`, `ServerSyncWebService`, `SimpleAuthWebService` (pas sur `Content` ni `selfupdate`).
4. Lancer `wsusutil configuressl <nom-dns-complet>`.
5. Modifier la GPO : `https://<nom-dns-complet>:8531` ; vérifier que les clients font confiance à l'autorité.
6. Faire de même entre serveurs amont et aval.

## 11.3 Le serveur WSUS lui-même : CVE-2025-59287

**CVE-2025-59287** (CVSS 9.8) : une faille de **désérialisation de données non fiables** dans le service WSUS permettait à un attaquant **non authentifié**, capable de joindre les ports 8530/8531, d'**exécuter du code avec les droits SYSTEM** sur le serveur. Chronologie :

- **14 octobre 2025** : correctif au Patch Tuesday, **incomplet** ;
- code d'exploitation public dans les jours qui suivent ;
- **23 octobre 2025** : correctif hors calendrier pour toutes les versions de Windows Server supportées (redémarrage requis) ; exploitations observées dans les heures suivantes ;
- inscription au catalogue **KEV** de la CISA.

Seuls les serveurs avec le **rôle WSUS activé** étaient concernés. La mesure temporaire recommandée : désactiver le rôle ou bloquer les ports entrants 8530/8531 jusqu'au correctif.

**Leçons** :

- **Patcher le serveur WSUS en priorité**, dans le groupe des serveurs critiques, pas « avec le reste ».
- **Ne jamais exposer 8530/8531 sur Internet**, et **filtrer** qui peut joindre le serveur (réseaux des clients et des serveurs aval, postes d'administration).
- **Détecter** : un processus `cmd.exe` ou `powershell.exe` lancé par `wsusservice.exe` ou par le `w3wp.exe` du pool WsusPool est un **signal fort** de compromission. Le transmettre au SOC comme règle de détection.

## 11.4 Les comptes et l'administration

- L'administration WSUS = **pouvoir d'installer du code sur tout le parc**. Le groupe local *WSUS Administrators* doit être restreint et revu.
- La console s'utilise depuis un **poste d'administration** dédié, pas depuis un poste bureautique.
- Dans un modèle de **tiering** Active Directory (niveaux d'administration), un serveur qui pilote des contrôleurs de domaine relève du niveau le plus sensible ; beaucoup d'organisations séparent un WSUS (ou un groupe) pour le tier 0 (renvoi : cours *Active Directory*).
- **Surveiller les approbations** : une approbation inattendue, surtout hors des créneaux habituels, doit être vérifiée.

## 11.5 La signature et la publication tierce

Les clients n'installent que des mises à jour **signées par Microsoft**, ou par un certificat **explicitement approuvé** pour la publication locale d'applications tierces (fonction utilisée par ConfigMgr et des outils comme Patch My PC). Ce certificat de publication est un **secret critique** : quiconque le possède peut publier un « correctif » accepté par tout le parc.

## 11.6 Au-delà de WSUS : les autres attaques par les mises à jour

| Attaque | Principe | Défense |
|---|---|---|
| **Fausses mises à jour de navigateur** (familles *FakeUpdates*/SocGholish, ClearFake…) | un site compromis affiche « Votre navigateur doit être mis à jour » et fait télécharger un malware | les mises à jour légitimes ne se téléchargent **jamais** depuis une page web ; sensibilisation ; filtrage |
| **Rétrogradation** (*Windows Downdate*, 2024, CVE-2024-21302 et CVE-2024-38202) | réinstaller d'anciennes versions vulnérables de composants système en détournant le processus de mise à jour | correctifs et mesures de révocation publiés par Microsoft ; VBS |
| **Pilotes vulnérables signés** (BYOVD) | charger un ancien pilote signé mais vulnérable pour désactiver les protections | liste de blocage des pilotes vulnérables, HVCI |
| **Outils de mise à jour tiers compromis** | l'infrastructure de mise à jour d'un éditeur est détournée | inventaire des agents de mise à jour, filtrage réseau, surveillance EDR |

## 11.7 Ce qui compte en MCS : la preuve

En MCS, la question n'est pas « WSUS tourne-t-il ? » mais :

- quel est le **délai** entre la publication d'un correctif et son installation **active** (après redémarrage) ?
- quelle est la **liste** des machines et des correctifs qui manquent, et **pourquoi** ?

C'est ce que demandent un auditeur, une RSSI, un régulateur (Ch.12).

> 🧵 **Fil rouge — Mai 2026**
>
> Inès présente au CAB un plan de durcissement : passage en HTTPS du WSUS amont et des trois réplicas (en commençant par Lille, encore en HTTP), filtrage des ports 8530/8531 aux seuls réseaux clients, règle de détection SOC sur les processus enfants de `wsusservice.exe` et `w3wp.exe`, revue du groupe *WSUS Administrators* (on y trouve encore deux comptes de prestataires partis en 2024). Thomas, côté serveurs, intègre les WSUS dans le premier anneau serveurs. Claire valide et demande une revue trimestrielle.

> 📌 **À retenir**
>
> - Le système de mises à jour est une **cible prioritaire** : il installe du code SYSTEM partout.
> - Production = **HTTPS (8531)**, ports jamais exposés sur Internet, accès filtré.
> - Le serveur WSUS se patche **en premier** (CVE-2025-59287).
> - Comptes d'administration restreints, approbations surveillées, détection des processus enfants suspects.

---
