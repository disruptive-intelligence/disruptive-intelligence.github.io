---
title: 'Chapitre 27 — Sécurité physique avancée : au-delà du badge'
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie VI — Dimensions avancées
  - index.md
---

## 27.1 Les systèmes de contrôle d'accès en profondeur

**RFID basse fréquence (125 kHz).** Technologies HID ProxCard, EM4100 — largement déployées, facilement clonables. L'investissement minimal (Proxmark3 — environ 300 €, Flipper Zero — environ 200 €) permet le clonage en quelques secondes à une distance de quelques centimètres. Ces technologies ne devraient plus être utilisées pour le contrôle d'accès de zones sensibles, mais restent massivement déployées par inertie dans de nombreuses organisations.

**RFID haute fréquence (13.56 MHz).** MIFARE Classic (vulnérable — attaques connues sur le chiffrement Crypto-1), MIFARE DESFire EV2/EV3 (robuste — chiffrement AES 128 bits, authentification mutuelle), iCLASS Standard (vulnérable), iCLASS SE/SEOS (robuste). La migration vers DESFire EV2+ ou SEOS est la recommandation de référence pour les organisations à risque élevé.

**Badges mobiles (NFC/BLE).** Apple Wallet, Google Wallet, applications dédiées (HID Mobile Access, SALTO JustIN) — protégés par la cryptographie du smartphone (enclave sécurisée), résistants au clonage à distance. L'avantage opérationnel est considérable : révocation à distance (en cas de perte ou de départ), provisioning sans contact physique, audit détaillé des accès. Les inconvénients : dépendance au smartphone (batterie, panne), compatibilité variable entre les fabricants de téléphones et les systèmes de contrôle d'accès, et le fait que certains sites sensibles interdisent les smartphones.

**Biométrie.** Empreintes digitales, reconnaissance faciale, reconnaissance de l'iris — offrent un facteur d'authentification non transférable (en théorie). En pratique, les systèmes biométriques ont des taux de faux rejet (l'employé légitime est refusé — frustration et contournement) et de faux acceptation (un attaquant est accepté — plus rare mais possible avec des attaques de présentation). Les considérations RGPD sont significatives : les données biométriques sont des données sensibles qui nécessitent une base légale spécifique et une analyse d'impact.

## 27.2 Le crochetage et le bypass physique

Dans le cadre d'un red team autorisé, les techniques de bypass physique complètent le social engineering quand l'accès par manipulation humaine échoue ou n'est pas applicable.

**Lock picking.** Le crochetage de serrures à goupilles standard est une compétence de base du red teamer physique. Les serrures à goupilles standard (cylindres européens de base) peuvent être crochetées en quelques minutes avec un jeu de crochets (tension wrench + pick). Les serrures haute sécurité (Abloy, Mul-T-Lock, Medeco) sont significativement plus résistantes et nécessitent des compétences et du matériel spécialisés.

**Bypass de serrures électriques.** Les serrures électriques à ventouse (maglocks) peuvent souvent être contournées en passant un objet fin (shim card) entre la porte et le cadre pour actionner le capteur de demande de sortie (REX — Request to Exit). Les serrures à gâche électrique sont vulnérables à des techniques similaires si elles sont en mode « fail-safe » (déverrouillées en cas de coupure de courant).

**Les faiblesses architecturales.** Faux plafonds (passage entre deux pièces par le plénum), gaines techniques (passage par les conduits de câblage ou de ventilation), fenêtres non verrouillées aux étages supérieurs, cloisons légères (certaines cloisons de bureau sont en plaque de plâtre et peuvent être traversées). Un audit de sécurité physique sérieux inclut l'évaluation de ces vecteurs.

## 27.3 Les implants physiques

Les implants physiques sont des dispositifs matériels déployés par le red teamer pour maintenir un accès persistant après l'intrusion physique.

**Clé USB drop.** Rubber Ducky (émule un clavier et exécute des commandes en quelques secondes), Bash Bunny (multi-payload, émulation de périphériques multiples), O.MG Cable (câble USB avec implant intégré — visuellement indistinguable d'un câble normal). En contexte offensif, la clé USB est déposée dans un lieu où elle sera trouvée et branchée (parking, accueil, salle de réunion) — le baiting exploite la curiosité.

**Implant réseau.** LAN Turtle (implant réseau passif se branchant sur un port Ethernet — fournit un accès distant au réseau interne), rogue access point WiFi (Raspberry Pi ou device dédié émettant un réseau WiFi qui capture les connections ou fournit un accès au réseau filaire), keylogger hardware (se place entre le clavier et le port USB — capture toutes les frappes).

La documentation de chaque implant déployé (localisation, horodatage, durée de présence, données collectées) est une obligation du rapport de red team. Tous les implants doivent être retirés à la fin du test — un implant oublié constitue une vulnérabilité réelle.

## 27.4 Conception d'un site résistant au social engineering physique

La sécurité physique contre le social engineering se conçoit dès l'architecture du site, pas comme un ajout après coup.

**Flux de circulation.** Les visiteurs et les prestataires doivent emprunter des circuits distincts des employés, avec accompagnement systématique. Les zones sensibles (R&D, salle serveur, direction) doivent être physiquement séparées des zones communes (accueil, réfectoire, salles de réunion visiteurs) avec un contrôle d'accès intermédiaire.

**Zone d'accueil comme sas de sécurité.** L'accueil ne doit pas être une simple réception — c'est un sas de sécurité qui vérifie l'identité, contacte l'hôte, émet le badge visiteur et assure l'accompagnement. Le gardien/réceptionniste doit être formé au contre-social engineering (détection des pretextes, refus poli, procédure d'escalade).

**Surveillance intégrée.** Caméras aux points d'accès et de circulation, avec monitoring en direct (pas seulement enregistrement). Détection d'anomalies (accès en horaires inhabituels, badge utilisé simultanément à deux endroits, tentatives d'accès répétées échouées).

---
