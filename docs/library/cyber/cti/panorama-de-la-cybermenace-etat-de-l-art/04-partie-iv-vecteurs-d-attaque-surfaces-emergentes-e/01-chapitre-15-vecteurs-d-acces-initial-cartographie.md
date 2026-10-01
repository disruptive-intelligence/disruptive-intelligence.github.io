---
title: 'Chapitre 15 — Vecteurs d''accès initial : cartographie et évolution'
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
  - index.md
---

## 15.1 — Phishing : vecteur dominant en mutation

Le phishing reste le vecteur d'accès initial le plus répandu. L'ENISA ETL 2025 le confirme comme « primary initial intrusion vector ». L'ANSSI observe que les campagnes de phishing reposent de plus en plus sur des comptes légitimes compromis, des services de création d'adresses de messagerie temporaires, ou de l'usurpation d'adresses légitimes — rendant la détection par les filtres anti-spam traditionnels plus difficile.

L'évolution principale est le passage vers le **phishing multi-canal** : combinaison d'emails, de SMS (smishing), de QR codes (quishing), et d'appels téléphoniques (vishing) dans des attaques coordonnées. Le CERT-EU anticipe pour 2026 une intensification de l'ingénierie sociale multi-canal, où les attaquants utiliseront l'IA pour orchestrer des campagnes cohérentes à travers plusieurs canaux simultanément.

Les kits **Adversary-in-the-Middle (AitM)** représentent l'innovation technique la plus significative : ils capturent les tokens de session en interceptant la communication entre la victime et le service légitime, permettant de contourner l'authentification multi-facteurs. Des kits comme **Sneaky 2FA** ciblent spécifiquement les environnements Microsoft 365 — l'environnement cloud le plus déployé dans les organisations européennes.

## 15.2 — Exploitation de vulnérabilités : le pivot vers l'infrastructure

L'exploitation de vulnérabilités logicielles est devenue le deuxième vecteur d'accès initial principal. Microsoft note que « l'exploitation de vulnérabilités reste l'une des méthodes d'accès initial les plus fiables, scalables et silencieuses pour les acteurs de la menace ».

Le fait structurant est le **pivot vers la compromission d'infrastructure**. Les attaquants ciblent de moins en moins les postes utilisateurs (via le phishing) et de plus en plus les équipements d'infrastructure : VPN (Ivanti Connect Secure, Fortinet FortiOS), firewalls (Palo Alto PAN-OS), passerelles (Citrix), serveurs de gestion (BeyondTrust, SimpleHelp). Ce pivot est stratégique parce qu'il ne dépend pas de l'interaction utilisateur, offre un accès direct au réseau interne, et cible des équipements souvent moins supervisés que les endpoints.

L'ANSSI confirme que, en 2024, « plus de la moitié des opérations de cyberdéfense de l'ANSSI, ont eu pour origine l'exploitation de vulnérabilités sur ces équipements », en 2025, les équipements de bordure restent des cibles privilégiées.

## 15.3 — La gestion des CVE : un défi croissant

Le nombre de CVE (Common Vulnerabilities and Exposures) publiées continue de croître. Le CSE canadien documente cette tendance avec des données montrant une augmentation continue des CVE par sévérité. Le délai d'exploitation diminue parallèlement : les attaques commencent « dans les jours suivant la divulgation » des vulnérabilités.

La priorisation devient un enjeu critique. Le catalogue KEV (Known Exploited Vulnerabilities) de la CISA, l'EUVD européen (Ch. 3.6), et le score EPSS (Exploit Prediction Scoring System) sont les outils de priorisation disponibles. La recommandation convergente de toutes les agences est claire : **patcher les vulnérabilités activement exploitées en priorité**, indépendamment de leur score CVSS théorique.

## 15.4 — Zero-day : marché et utilisation

Les vulnérabilités zero-day (inconnues au moment de l'exploitation) sont le vecteur le plus dangereux parce qu'il n'existe aucun patch disponible. L'ANSSI note que des acteurs chinois ont exploité des zero-day (notamment la CVE-2023-23397 par APT28 côté russe). Le marché des zero-day est un secteur où acteurs étatiques, cyber-mercenaires et cybercriminels coexistent — les États étant les principaux acheteurs via des programmes de renseignement ou des intermédiaires.

## 15.5 — Living-off-the-Land (LotL)

La technique Living-off-the-Land consiste à utiliser les outils natifs du système ciblé (PowerShell, WMI, certutil, bitsadmin sous Windows ; bash, curl, python sous Linux) plutôt que de déployer des malwares personnalisés. Cette technique rend la détection beaucoup plus difficile parce que les outils utilisés sont légitimes et leur exécution est « normale » dans l'environnement.

Volt Typhoon est l'exemple emblématique d'utilisation systématique du LotL à des fins de prépositionnement. La détection des techniques LotL nécessite une analyse comportementale — identifier les séquences d'actions anormales plutôt que la présence de fichiers malveillants — ce qui requiert des capacités de monitoring avancées (EDR, SIEM avec règles comportementales, hunting proactif).

## 15.6 — Nouveaux vecteurs émergents

Le CERT-EU anticipe pour 2026 plusieurs vecteurs émergents. **ClickFix** : fenêtres pop-up imitant des erreurs système qui guident l'utilisateur vers l'exécution d'un script malveillant copié dans le presse-papier. **QR phishing** (quishing) : QR codes malveillants dans des emails professionnels, sur des supports physiques ou dans des documents partagés. **Vishing-to-OAuth** : appels téléphoniques qui guident la victime vers une page d'authentification OAuth légitime mais avec un grant malveillant, accordant à l'attaquant un accès persistant au compte sans mot de passe ni token MFA.

---
