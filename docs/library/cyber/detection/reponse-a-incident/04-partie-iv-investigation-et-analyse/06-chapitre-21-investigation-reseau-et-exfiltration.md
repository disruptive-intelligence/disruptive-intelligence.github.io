---
title: Chapitre 21 — Investigation réseau et exfiltration
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation et analyse
  - index.md
---

## 21.1 Identification des communications C2

Les communications C2 (Command and Control) sont le lien entre le malware et l'attaquant. Leur identification est un objectif prioritaire de l'investigation réseau car elles révèlent les machines compromises et les destinations de l'attaquant.

Le **beaconing** est le pattern le plus courant : le malware contacte le C2 à intervalles réguliers (toutes les 30 secondes, toutes les 5 minutes) pour recevoir des instructions. Les attaquants sophistiqués ajoutent du jitter (variation aléatoire de l'intervalle) pour simuler du trafic humain, mais le pattern reste détectable par analyse statistique. Le **DNS tunneling** utilise les requêtes DNS pour encapsuler des données — un volume anormal de requêtes DNS vers un même domaine, ou des requêtes avec des sous-domaines longs et encodés, sont des indicateurs. Le **fingerprinting TLS** (JA3/JA4) permet d'identifier des clients TLS suspects même sur du trafic chiffré — le hash JA3 du client TLS d'un malware est souvent distinct de celui d'un navigateur légitime.

## 21.2 Identification de l'exfiltration

L'exfiltration est souvent la composante la plus difficile à détecter et à quantifier. Les indicateurs incluent un volume anormal de trafic sortant par rapport à la baseline, des flux vers des services cloud non autorisés (Mega, file.io, transfer.sh, ou des instances AWS/Azure/GCP louées à la demande), des connexions longue durée vers des IP inconnues, et l'utilisation d'outils de transfert identifiables (rclone a un user-agent caractéristique dans les logs proxy, WinSCP et FTP ont des empreintes réseau spécifiques).

L'estimation du volume exfiltré est cruciale pour la CNIL (la notification doit indiquer le nombre de personnes et le type de données concernées), pour la communication de crise (« avons-nous perdu nos secrets industriels ? »), et pour la décision sur la rançon (si les données sont déjà exfiltrées, payer ne les « dé-exfiltrera » pas).

Le cas du **living off trusted services** : les attaquants utilisent de plus en plus des services légitimes pour l'exfiltration (AWS S3, Azure Blob, Google Drive, OneDrive). Ces flux passent les contrôles de sécurité (les domaines sont réputés légitimes) et sont invisibles aux filtres URL. La détection repose sur l'identification des outils (rclone, aws-cli) via les user-agents proxy, l'analyse volumétrique, et la corrélation avec les autres IoC.

## 21.3 Fil rouge — BLACKTIDE : l'exfiltration

> **🔍 BLACKTIDE — Épisode 21**
>
> Karim analyse les logs proxy (Squid) pour reconstituer l'exfiltration. Il identifie des connexions HTTPS vers `s3.eu-west-1.amazonaws.com` depuis 3 machines internes (10.42.15.87, 10.42.15.92, 10.42.10.45), totalisant 380 Go sur 7 jours (J-7 à J-0). Le user-agent est `rclone/v1.65.0` — confirmant l'utilisation de rclone, un outil de synchronisation cloud légitime détourné par l'attaquant.
>
> Les données exfiltrées sont identifiées par corrélation avec les logs d'accès aux partages de fichiers (Event ID 5140/5145) : accès massif aux partages `\\FS01-Lyon\R&D`, `\\FS01-Fos\Projets`, et `\\FS01-Lyon\RH` dans les 7 jours précédant l'exfiltration. Le volume se répartit en environ 310 Go de données R&D (formules chimiques, procédés de fabrication, brevets en cours) et 70 Go de données RH (fiches de paie, contrats, données de sécurité sociale de 8 000 employés).
>
> Le serveur de staging est une instance EC2 AWS en région `eu-west-1` (Irlande). L'identification du locataire nécessitera une réquisition judiciaire auprès d'AWS.

---
