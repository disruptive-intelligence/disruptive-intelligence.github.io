---
title: Chapitre 2 — Cycle de vie d'une intrusion APT
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - ../index.md
- - 'Partie I — Fondations : comprendre les APT'
  - index.md
---

## 2.1 Le modèle d'intrusion moderne en 7 phases

En pratique, les équipes SOC/IR/CTI utilisent un modèle plus granulaire que la Kill Chain classique de Lockheed Martin.

**Phase 1 — Reconnaissance (J-60 à J-1) :** l'attaquant collecte des informations sur la cible. OSINT (LinkedIn — identifier les employés, les technologies utilisées via les offres d'emploi, les sous-traitants), scanning (Shodan, Censys — identifier les services exposés : VPN, portails web, appliances), et social engineering préliminaire (création de faux profils, préparation de lures de phishing personnalisés). Les APT les plus sophistiqués (APT29, Volt Typhoon) peuvent passer des semaines en reconnaissance avant l'accès initial.

**Phase 2 — Accès initial (J0) :** la première compromission. Le vecteur varie selon l'acteur : phishing ciblé (APT28, APT35), exploitation de vulnérabilité sur un service exposé (Volt Typhoon — Ivanti/Fortinet, APT40 — appliances réseau), supply chain (APT29 — SolarWinds, Lazarus — 3CX), credentials volés (APT29 — password spraying Azure AD), ou social engineering avancé (Lazarus — faux recruteurs LinkedIn).

**Phase 3 — Foothold (J0-J2) :** installation d'une persistence initiale. Dépôt d'un web shell, création d'une tâche planifiée, modification du registre, ou DLL sideloading. L'objectif est de survivre à un reboot et de disposer d'un point de retour si l'accès initial est fermé.

**Phase 4 — Escalade de privilèges (J3-J5) :** obtenir des droits admin/SYSTEM/root. Credential dumping (Mimikatz ou équivalent custom), Kerberoasting, exploitation de vulnérabilités locales, ou abus de configurations AD (ACL permissives, comptes de service surprivilégiés). L'obtention d'un compte Domain Admin est le tournant de l'intrusion.

**Phase 5 — Mouvement latéral (J5-J20+) :** l'attaquant se déplace vers les systèmes de valeur — Domain Controllers, serveurs de fichiers, boîtes mail des dirigeants, systèmes OT. Les techniques dépendent de l'acteur : PsExec (Sandworm), WMI (APT41), RDP (divers), ou uniquement des LOLBins (Volt Typhoon).

**Phase 6 — Collection et staging (J20-J45+) :** identification et rassemblement des données de valeur. Les fichiers sont copiés vers un serveur de staging, compressés et chiffrés. L'attaquant sélectionne — il ne copie pas tout, il cible ce qui correspond à son mandat.

**Phase 7 — Exfiltration / Impact (J45+) :** sortir les données (via HTTPS, DNS, services cloud) ou réaliser l'action finale (déployer un wiper, manipuler un automate OT, publier des données volées). Certaines APT ne réalisent jamais cette phase — elles se pré-positionnent et attendent (Volt Typhoon).

## 2.2 Dwell time

Le dwell time médian global était de 10 jours en 2023 selon Mandiant M-Trends (vs 16 jours en 2022). Mais cette moyenne masque une dispersion massive : les incidents détectés par un tiers (notification externe) ont un dwell time beaucoup plus long que ceux détectés en interne. Et pour les APT étatiques ciblant des organisations peu matures, le dwell time peut dépasser 200 jours.

Les gaps de détection typiques par phase : pas de logs DNS (C2 invisible), pas d'EDR sur les serveurs (mouvement latéral invisible), pas de monitoring cloud/identity (token theft invisible), pas de DLP (exfiltration invisible).

## 2.3 Fil rouge — BLACKOUT : la timeline

> **⚡ BLACKOUT — Épisode 2**
>
> Le CERT reconstitue la timeline : exploitation Ivanti à J0, web shell déposé à J+1, DLL sideloading pour la persistence à J+3, Kerberoasting ciblant les comptes de service à J+5, mouvement latéral via PsExec à J+8, pivot vers le poste d'ingénierie OT à J+15, tentative de reconnaissance du réseau SCADA à J+20-30, et inactivité de J+30 à la détection J+42. L'attaquant s'est pré-positionné et a cessé toute activité visible — comme s'il attendait un signal.

---
