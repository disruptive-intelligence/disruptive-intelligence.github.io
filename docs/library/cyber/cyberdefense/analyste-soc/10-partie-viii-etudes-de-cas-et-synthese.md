---
title: Partie VIII — Études de cas ET synthèse
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

*4 cas complets qui appliquent l'intégralité du cours. Chaque cas est une investigation de bout en bout — pas un mini-exemple.*

---


## Chapitre 37 — Cas complet

intrusion par phishing avec mouvement latéral et pré-ransomware (synthèse FALCONWATCH)

Synthèse du fil rouge sous forme de cas autonome. 48 heures d'intrusion reconstituées de bout en bout.

**Samedi 08h12 — Accès initial :** Marc Dubois (ingénieur de production) reçoit un email de spearphishing envoyé depuis le compte compromis d'un sous-traitant de maintenance (les credentials VPN du sous-traitant avaient été vendues sur Russian Market 3 semaines plus tôt). Le document Word contient une macro VBA qui exécute certutil pour télécharger lib.dll depuis `update-norexia[.]xyz` et l'exécute via rundll32. Le RAT s'installe et commence le beaconing HTTPS vers `185.xx.xx.xx` toutes les 45 secondes.

**Samedi 22h30 — Reconnaissance et mouvement latéral :** l'attaquant exécute des commandes de reconnaissance (`whoami /all`, `net group "Domain Admins"`, `nltest /domain_trusts`). Il utilise PsExec pour se déplacer vers WKS-IT-045 (poste d'un admin IT — cible de valeur pour les credentials et les accès).

**Dimanche 06h15 — Kerberoasting et staging :** depuis WKS-PROD-112, l'attaquant lance un Kerberoasting ciblant 8 comptes de service (détectable : 8 requêtes 4769 RC4 en 2 minutes depuis une seule machine). Il lance rclone sur WKS-IT-045 pour exfiltrer 12 Go de données R&D (formulations chimiques propriétaires) vers un bucket S3 externe.

**Lundi 04h-07h — Préparation ransomware :** suppression des shadow copies sur 3 machines (`vssadmin delete shadows /all`). Un binaire BlackBasta est déposé dans `C:\Windows\Temp\` sur 3 machines — mais pas encore exécuté. L'attaquant prépare le déploiement massif.

**Lundi 07h42 — Détection :** l'EDR CrowdStrike détecte le certutil + rundll32 sur WKS-PROD-112 (l'alerte remonte avec un délai car le processus était dormant depuis samedi et a été re-flaggé lors d'un re-scan comportemental). Karim prend l'alerte.

**Lundi 07h42-08h30 — Triage et investigation L2 :** Karim reconstitue le process tree, confirme le VP, pivote vers le réseau (beaconing C2), pivote vers les autres machines (découverte de WKS-IT-045 compromis), pivote vers l'AD (Kerberoasting détecté).

**Lundi 08h30 — Escalade :** Karim émet le SITREP et escalade vers l'IR lead et le RSSI Norexia. Sévérité : critique (accès OT potentiel, pré-ransomware confirmé, exfiltration de données R&D).

**Lundi 08h30-09h15 — Confinement :** isolation des 2 postes via EDR, blocage du C2 au proxy et au firewall, reset des credentials de marc.dubois et svc-scada (le mot de passe svc-scada n'avait pas encore été cracké — confirmé par l'absence de 4624 avec ce compte depuis une machine non autorisée), suppression du binaire BlackBasta des 3 machines.

**Post-incident :** REX complet. 3 nouvelles règles Sigma (certutil download cradle, Kerberoasting > 5 comptes en 5 min, vssadmin delete shadows). Sysmon déployé sur les postes d'ingénierie OT (n'y était pas). Playbook ransomware mis à jour. IoC partagés avec la CTI → profil d'acteur enrichi. Le MTTD de 23h est analysé : la détection initiale samedi était manquée car le certutil a été exécuté une seule fois (sous le seuil) — la re-détection lundi est due au re-scan comportemental de l'EDR qui a corrélé le certutil avec le rundll32 en persistance.

---


## Chapitre 38 — Cas complet : compromission de compte M365 avec BEC

Un utilisateur du département finance d'un client CyberShield signale des emails suspects envoyés depuis son propre compte. L'investigation cloud pure : sign-in logs Azure AD (connexion depuis un VPS néerlandais, token replay après phishing AitM — le MFA a été « passé » par interception du token de session), M365 UAL (création de règle de forwarding vers une adresse ProtonMail, accès SharePoint Finance avec téléchargement de 45 fichiers, envoi de 3 emails BEC — demande de virement de 180 000 € au prestataire comptable avec un nouveau RIB), corrélation proxy (le phishing AitM initial identifié — kit EvilGinx2 hébergé sur un domaine de typosquatting), et scope assessment (recherche des IoC du kit AitM dans les logs proxy → 2 autres utilisateurs ont cliqué mais sans soumission de credentials → le scope est limité à 1 compte compromis). Confinement : reset mot de passe + révocation de toutes les sessions + suppression de la règle de forwarding + blocage du domaine AitM + notification du prestataire comptable (le virement a été bloqué à temps). Le cas illustre l'investigation cloud pure sans composante endpoint.

---


## Chapitre 39 — Cas complet : threat hunt sur les LOLBins

3 mois après FALCONWATCH, le SOC CyberShield mène un hunt proactif sur les LOLBins dans l'environnement Norexia. Hypothèse : « si un attaquant est encore présent ou si un nouvel attaquant a pénétré, il utilise probablement des LOLBins pour éviter la détection ». Le hunt utilise le stacking (quelles sont les utilisations les plus rares de certutil, mshta, bitsadmin, regsvr32, rundll32 dans le parc sur les 30 derniers jours ?), l'analyse de contexte (les 5 occurrences de certutil -urlcache sur des postes non-IT sont-elles légitimes ?), et l'investigation d'une anomalie (un poste d'ingénierie utilise mshta pour charger un HTA depuis un partage réseau — investigation → c'est un script de maintenance légitime mais non documenté et non sécurisé — BTP). Résultat : pas de compromission trouvée, mais le script non sécurisé est corrigé, la baseline est enrichie (5 nouvelles exclusions documentées), et la confiance dans la posture post-incident est renforcée. Le cas illustre un hunt complet qui ne trouve PAS de compromission — et qui a quand même de la valeur.

---


## Chapitre 40 — Cas complet

8 heures d'un analyste SOC — la réalité du shift

Ce cas est un format unique : une journée de travail complète, pas une investigation unique. 8 heures de shift avec les alertes réelles, les FP, les BTP, les doutes, et le VP qui change tout.

**07h15 — Alerte « Impossible Travel » (VPN) :** un utilisateur se connecte au VPN depuis Paris à 07h00 et depuis le Brésil à 07h12. Investigation : l'utilisateur utilise un VPN personnel qui sort par un nœud brésilien. L1 vérifie le user-agent et le device → identiques. Conclusion : **FP**. Temps : 8 minutes.

**08h02 — Alerte « PowerShell -EncodedCommand » (serveur) :** PowerShell avec -enc exécuté sur un serveur de production. Investigation : le processus parent est SCCM (System Center Configuration Manager). La commande décodée est un script de déploiement de patch légitime. Conclusion : **BTP** (la détection est correcte — PowerShell -enc a bien été exécuté — mais l'action est légitime). L'analyste documente le BTP et vérifie que SCCM est dans la liste d'exclusion de la règle — il n'y est pas. Recommandation : ajouter l'exclusion SCCM (documentée). Temps : 12 minutes.

**09h30 — Alerte « Internal Port Scan » (IDS) :** scan de ports depuis 10.0.2.15 vers 10.0.2.0/24. Investigation : l'IP source est le scanner Nessus. Conclusion : **FP** (l'IP de Nessus aurait dû être exclue de la règle IDS). L'analyste crée un ticket de tuning pour ajouter l'exclusion. Temps : 5 minutes.

**10h45 — Alerte « Data Exfiltration — Large Upload » (proxy) :** 2.1 Go uploadés vers Google Drive depuis un poste du département RH. Investigation : l'utilisatrice RH partage un dossier de candidatures avec un cabinet de recrutement externe — validé par son manager via email. Conclusion : **FP** (activité métier légitime). L'analyste note que la catégorisation proxy de Google Drive comme « exfiltration » génère trop de FP → recommandation de tuning (exclure Google Drive des alertes de volume OU ajouter une condition sur le département source). Temps : 15 minutes.

**11h30 — Alerte « Mimikatz Detected » (EDR) :** CrowdStrike détecte la signature de Mimikatz sur DC01 (le contrôleur de domaine du client). **Le monde change.** L'analyste L1 escalade immédiatement au L2. L'investigation révèle : un processus `lsass_dump.exe` (renommé, mais le hash matche Mimikatz) exécuté par le compte `admin-it-03` à 11h28. Le process tree montre `cmd.exe → lsass_dump.exe` avec le parent `explorer.exe` — l'attaquant a une session interactive sur le DC. L'analyste L2 pivote : 4624 type 10 (RDP) sur DC01 depuis 10.0.1.87 (WKS-ADMIN-03, poste de l'admin IT n°3) à 11h25. L'admin IT n°3 est contacté : « Non, ce n'est pas moi, je suis en réunion depuis 10h. » → **Compromission confirmée du DC.** Escalade IR immédiate. Confinement : isolation de WKS-ADMIN-03 et de DC01 (après coordination avec l'IT — isoler un DC impacte tout le domaine). Le shift bascule en mode incident — le reste des alertes est transféré à un collègue.

Le cas illustre la réalité du métier : 4 FP/BTP pour 1 VP, la gestion du temps et de l'énergie, la priorisation (les alertes de 07h-11h sont traitées calmement ; l'alerte de 11h30 déclenche l'adrénaline), et le moment où une journée « normale » bascule en incident majeur.

---
