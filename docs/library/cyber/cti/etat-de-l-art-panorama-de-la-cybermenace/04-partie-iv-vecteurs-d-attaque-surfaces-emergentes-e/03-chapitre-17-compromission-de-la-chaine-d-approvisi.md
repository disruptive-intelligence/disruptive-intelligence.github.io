---
title: Chapitre 17 — Compromission de la chaîne d'approvisionnement
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
  - index.md
---

## 17.1 — Anatomie d'une supply chain attack

Les attaques supply chain exploitent les relations de confiance entre une organisation et ses fournisseurs, sous-traitants ou partenaires. Le principe est simple : plutôt que d'attaquer directement une cible bien défendue, compromettre un fournisseur moins protégé qui dispose d'un accès au réseau de la cible. L'ANSSI note que « ces attaques, qui sont en constante expansion depuis la fin des années 2010, illustrent combien la maîtrise du SI, de ses interconnexions et de ses dépendances est un enjeu majeur pour les organisations ».

Les vecteurs de supply chain attack se déclinent en trois catégories principales. La **supply chain logicielle** cible les composants logiciels (bibliothèques, packages, mises à jour). La **supply chain des services** cible les prestataires de services IT (MSP, hébergeurs, éditeurs SaaS). La **supply chain matérielle/physique** cible les composants physiques (COTS embarqués, équipements réseau). Le CSE canadien note l'émergence de **double supply chain attacks** — « une attaque supply chain qui en permet une autre ».

## 17.2 — Supply chain logicielle : empoisonnement de packages

L'empoisonnement de packages dans les registres publics (npm, PyPI, RubyGems) est un vecteur en croissance. Les attaquants publient des packages malveillants portant des noms similaires à des packages légitimes populaires (typosquatting) ou créent des packages dont les noms correspondent aux hallucinations de LLMs (slopsquatting).

Le cas **Shai-Hulud** (2025) illustre la sophistication croissante : un package malveillant distribué via npm avec des mécanismes d'évasion avancés. Les **Rules File Backdoors** ciblent les assistants de code IA en injectant des instructions cachées dans les fichiers de configuration des projets.

## 17.3 — Supply chain des services : le cas des prestataires IT

L'ANSSI documente de manière détaillée les cas de compromission en cascade via les prestataires en 2025. « L'ANSSI a été témoin de nombreuses compromissions d'entités par des attaquants en mesure de se latéraliser depuis les systèmes d'information de prestataires vers des clients. À titre d'exemple, un attaquant a compromis et exfiltré des ressources clientes chez un prestataire de nombreuses entités françaises. En tirant parti des interconnexions existantes avec les systèmes d'information des clients et grâce à des authentifiants volés, l'attaquant est parvenu à se latéraliser sur le système d'information de plusieurs clients. »

L'ANSSI a également été témoin de « plusieurs compromissions par rançongiciel de prestataires causant des impacts forts sur les clients ». Le schéma est récurrent : compromission du prestataire → latéralisation via les interconnexions réseau ou les credentials partagées → compromission des clients.

Les **services SaaS** ajoutent une dimension : les API, extensions de marketplace et grants OAuth cross-platform créent des vecteurs de supply chain spécifiques au cloud. Un grant OAuth malveillant peut donner à un attaquant un accès persistant aux données d'une organisation sans jamais compromettre ses credentials.

## 17.4 — Concentration des fournisseurs comme risque systémique

Le CSE canadien identifie la « concentration des fournisseurs » comme l'une des cinq tendances structurantes. La dépendance d'un grand nombre d'organisations aux mêmes fournisseurs de services cloud, de sécurité ou d'infrastructure crée des **points de défaillance uniques** (single points of failure). L'incident CrowdStrike de juillet 2024 — une mise à jour défectueuse ayant paralysé des millions de systèmes Windows dans le monde — illustre ce risque systémique, même en l'absence de cyberattaque.

## 17.5 — SBOM et hygiène des dépendances

Les Software Bills of Materials (SBOM) — inventaires exhaustifs des composants logiciels d'un produit — sont promus par le CRA européen et les régulateurs américains comme outil de transparence et de gestion des risques supply chain. Les SBOM permettent de savoir, lorsqu'une vulnérabilité est découverte dans un composant, quels produits sont affectés. Leur adoption reste cependant inégale, et la gestion opérationnelle des SBOM (mise à jour, corrélation avec les bases de vulnérabilités, intégration dans les processus de patching) est un défi non trivial.

## 17.6 — 🔴 Fil rouge : la surprise — convergence étatique-criminel

> **📌 FIL ROUGE — Épisode 17**
>
> L'investigation sur l'incident du prestataire (Ch. 11) réserve la surprise annoncée. L'analyse forensique approfondie du SI d'EuroDefense révèle, en plus des traces de l'affilié Qilin (ransomware), la présence d'un implant **ShadowPad** sur un serveur de gestion de contrats OTAN — un outil historiquement associé à l'espionnage chinois. L'implant est différent du ransomware : il est discret, persistent, et configuré pour l'exfiltration de données, pas pour le chiffrement.
>
> Deux hypothèses se forment :
> — Hypothèse A : un acteur étatique chinois a exploité le même accès initial que l'affilié Qilin (les credentials du prestataire), indépendamment de l'attaque ransomware. C'est le scénario de « victimes multiples du même IAB ».
> — Hypothèse B : l'affilié Qilin est lui-même un opérateur hybride mêlant ransomware (gain financier) et espionnage (pour un commanditaire étatique). C'est le scénario NailoLocker/ShadowPad documenté par l'ANSSI et Orange CyberDefense.
>
> Sophie ne peut pas trancher entre les deux hypothèses avec les données disponibles. Elle rédige un assessment à confiance basse distinguant explicitement les deux scénarios et recommande une escalade vers l'ANSSI (qui a l'expertise et les données comparatives nécessaires). Le RSSI Marc Vidal réalise la gravité : « Si c'est le scénario B, on n'est pas face à un simple ransomware — on est face à une opération d'espionnage étatique qui utilise le ransomware comme couverture. »

---
