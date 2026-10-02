---
title: Chapitre 22 — Investigation des environnements hybrides, OT et dépendances tierces
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation et analyse
  - index.md
---

*Ce chapitre est un panorama qui traite trois environnements d'investigation spécifiques, chacun avec ses propres contraintes. Il assume explicitement un traitement moins approfondi que les chapitres précédents sur chaque volet, en renvoyant vers les cours spécialisés de la bibliothèque.*

## 22.1 Investigation cloud (Microsoft 365 / Entra ID)

Les compromissions cloud suivent des logiques différentes de l'on-premise. L'attaquant ne « compromet » pas un serveur — il vole un token, il abuse d'un consentement OAuth, il modifie une conditional access policy. L'investigation repose sur les **Sign-in Logs** d'Entra ID (connexions, y compris les échecs, avec géolocalisation et device info), les **Unified Audit Logs** (toutes les actions administratives et utilisateur dans M365 — création de règles de forwarding, accès aux mailboxes, modifications de configuration, ajout d'app registrations), et les **Azure Activity Logs** (si Azure IaaS/PaaS est utilisé).

Les pièges spécifiques au cloud : la rétention des logs dépend de la licence (180 jours en E3, jusqu'à 365 jours en E5 pour certains types de logs), les tokens volés permettent un accès persistant même après reset du mot de passe (il faut révoquer explicitement les refresh tokens), et les app registrations malveillantes peuvent fournir un accès API permanent sans interaction utilisateur.

## 22.2 Investigation OT/ICS

L'investigation en environnement OT (Operational Technology) est contrainte par des réalités physiques que l'IT ne connaît pas. Les systèmes ne sont pas patchables (un automate en production ne peut pas être redémarré pour appliquer un correctif), les protocoles sont propriétaires (Modbus, S7, OPC-UA — les outils d'investigation réseau classiques ne les comprennent pas), les logs centralisés sont rares (les automates n'envoient pas de syslog au SIEM), les agents EDR ne peuvent pas être déployés sur les PLC (Programmable Logic Controllers), et les contraintes de disponibilité sont extrêmes (arrêter un automate dans une usine chimique peut causer un accident physique).

La plupart des incidents OT commencent par une compromission IT qui pivote vers le réseau OT via les passerelles de supervision (SCADA), les jump servers, ou les postes d'ingénierie à double connexion (un poste connecté à la fois au réseau IT et au réseau OT — c'est exactement le cas de BLACKTIDE). L'investigation OT est donc souvent une extension de l'investigation IT, menée conjointement avec les ingénieurs de production.

L'évaluation critique : l'attaquant a-t-il atteint les systèmes de contrôle ? A-t-il modifié des configurations d'automates ? A-t-il la capacité de causer un dommage physique ? Ces questions déterminent le niveau d'urgence et la mobilisation de compétences spécialisées (CERT-FR dispose d'équipes OT déployables sur les OIV).

## 22.3 Investigation supply chain et dépendances tierces

Quand l'incident provient d'un tiers de confiance (mise à jour logicielle piégée, accès VPN prestataire compromis, dépendance SaaS compromise), l'investigation dépasse le périmètre de l'organisation. Le scoping doit considérer tous les systèmes ayant interagi avec le tiers compromis, la coordination avec le fournisseur est indispensable (mais souvent lente, juridiquement complexe, et politiquement sensible), et l'évaluation de l'impact doit considérer le cas où le tiers a été un vecteur vers d'autres clients.

Dans le cas de BLACKTIDE, le point d'entrée est la compromission du sous-traitant RH GestPaie — un cas classique de supply chain via prestataire. L'infostealer sur le poste du DRH de GestPaie a fourni les credentials VPN d'Arvantis. La question de la responsabilité contractuelle (GestPaie avait-elle une obligation de MFA sur ses postes ?) est un enjeu juridique post-incident.

## 22.4 Fil rouge — BLACKTIDE : les volets spécifiques

> **🔍 BLACKTIDE — Épisode 22**
>
> **Cloud :** l'attaquant a utilisé un token volé d'un admin M365 (obtenu via le DCSync — le hash NTLM du compte a permis un pass-the-hash vers Entra ID via Azure AD Connect sync). Il a créé une règle de forwarding sur la boîte mail du CFO (toutes les PJ PDF redirigées vers une adresse ProtonMail externe). La règle est active depuis J-10. Les UAL E3 (180 jours) permettent de confirmer qu'aucune autre manipulation M365 n'a eu lieu.
>
> **OT :** le site OIV de Fos-sur-Mer utilise un SCADA Schneider Electric pour le contrôle des réacteurs. L'investigation révèle que l'attaquant a atteint le poste d'ingénierie OT (Windows 10, connecté au réseau IT via un second adaptateur réseau — la segmentation IT/OT reposait uniquement sur un VLAN, pas sur un pare-feu physique). Le ransomware a chiffré le poste d'ingénierie mais PAS les PLC Schneider (pas de système de fichiers Windows sur les automates). L'ANSSI déploie une équipe CERT-FR spécialisée OT le lundi pour vérifier l'intégrité des configurations SCADA.
>
> **Supply chain :** GestPaie est notifié de la compromission de son poste DRH le samedi matin. Réponse : « On va regarder. » Arvantis désactive immédiatement l'accès VPN de GestPaie et demande un audit de sécurité contractuel (la clause existe dans le contrat de prestation).

---
