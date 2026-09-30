---
title: Chapitre 9 — Ciblage sectoriel par les acteurs étatiques
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE II — Les acteurs étatiques
  - index.md
---

analyse comparée

## 9.1 — Administrations publiques et diplomatie

L'ENISA ETL 2025 identifie l'administration publique comme le secteur le plus ciblé de l'UE avec 38,2% des incidents documentés — une augmentation substantielle par rapport à la période précédente, principalement due aux attaques DDoS hacktivistes. Le ciblage hacktiviste (96,2% du total pour ce secteur) est contextualisé par les événements géopolitiques : soutien à l'Ukraine, arrestations de cybercriminels, élections, sommets OTAN.

Au-delà du DDoS, le secteur public est la cible première de l'espionnage étatique. Le CERT-EU documente que le cyberespionnage et le prépositionnement représentent 38% des MAI totales dans son dataset, avec la défense comme secteur le plus ciblé et la diplomatie en deuxième position. Les campagnes d'APT29 imitant des invitations diplomatiques et le ciblage de ministères des affaires étrangères illustrent la persistance de cette menace.

## 9.2 — Défense et recherche

Le secteur de la défense est une cible permanente de l'espionnage étatique. L'ANSSI note que « le secteur de la défense a fait l'objet en 2025 d'actions de reconnaissance, de tentatives de compromissions et de compromissions par des modes opératoires réputés étatiques à des fins d'espionnage stratégique et de renseignement ». Le ciblage est conduit par les principaux acteurs étatiques (Chine, Russie, RPDC) et porte sur la propriété intellectuelle militaire, les données contractuelles, les capacités technologiques et les informations stratégiques.

Les universités et centres de recherche constituent une extension du ciblage défense — les résultats de la recherche fondamentale alimentant les programmes militaires. L'ANSSI et Microsoft documentent un ciblage persistant de ce secteur, notamment par des acteurs iraniens (APT42) et chinois.

## 9.3 — Infrastructures numériques et télécommunications

L'ENISA classe les infrastructures numériques et services comme le troisième secteur le plus ciblé (4,8% des incidents). Ce secteur a un **effet multiplicateur** : compromettre un fournisseur de services numériques permet d'accéder aux données de tous ses clients.

Le ciblage des télécommunications est traité en détail au Ch.6.5. L'ASD et les partenaires Five Eyes ont publié un advisory conjoint sur la compromission des réseaux d'opérateurs télécom par des acteurs PRC, accompagné de recommandations de durcissement pour les ingénieurs réseau et les défenseurs.

## 9.4 — Transport et logistique

Le transport est le deuxième secteur le plus ciblé dans l'UE (7,5% des incidents ETL 2025). Le ciblage russe de la logistique de livraison d'aide à l'Ukraine (documenté par l'ASD en mai 2025) illustre comment les intérêts militaires drives le ciblage sectoriel. Le ciblage chinois du transport maritime est lié aux intérêts stratégiques Belt and Road.

## 9.5 — Secteur spatial

Le Space Threat Landscape 2025 de l'ENISA est la première évaluation systématique des menaces cyber pesant sur les systèmes satellitaires. Le secteur spatial est désormais inclus dans NIS2 comme secteur de haute criticité, imposant des obligations de cybersécurité aux opérateurs de satellites et d'infrastructures sol.

Les menaces identifiées couvrent l'ensemble du cycle de vie des satellites : compromission des centres de contrôle au sol, injection de code malveillant dans les logiciels embarqués (OBC/OBSW), exploitation de vulnérabilités dans les protocoles de communication satellite, interception des liaisons TM/TC (télémétrie/télécommande), et compromission de la supply chain des composants COTS. Le détail est traité au Chapitre 19.

## 9.6 — Finance

Le secteur financier (4,5% des incidents ETL 2025) est ciblé à la fois par l'espionnage étatique (ciblage des systèmes de paiement, surveillance des flux financiers) et par la cybercriminalité (ransomware, fraude). Le CERT-EU note que le secteur financier a vu une augmentation des MAI en 2025, avec le cybercrime comme menace principale suivie du cyberespionnage. Le règlement DORA impose au secteur financier des exigences spécifiques de résilience opérationnelle numérique.

## 9.7 — Santé, énergie, industrie manufacturière

Le secteur de la **santé** est la cible la plus documentée du ransomware dans les données FBI IC3, avec 460 incidents ransomware et 355 incidents data breach signalés pour les infrastructures critiques healthcare/public health en 2025. Le ciblage de la santé est particulièrement problématique parce qu'il peut avoir des conséquences directes sur la vie des patients.

Le secteur de l'**énergie** est ciblé pour le prépositionnement (Volt Typhoon), le sabotage (cas polonais 2025) et le hacktivisme OT (Z-PENTEST-ALLIANCE). L'**industrie manufacturière** est le secteur le plus touché par les revendications ransomware en UE (14,9% des claims selon l'ENISA).

## 9.8 — Analyse croisée multi-sources

Le croisement des données de sources différentes révèle des convergences et des divergences instructives. Tous les rapports s'accordent sur la prééminence du ransomware comme menace cybercriminelle, sur l'intensification de l'espionnage étatique chinois, et sur la persistance de la menace russe amplifiée par le conflit ukrainien. Les divergences portent principalement sur les proportions (le poids relatif de chaque secteur varie selon la perspective géographique) et sur les menaces émergentes (la menace quantique, par exemple, est traitée très différemment selon les sources).

## 9.9 — 🔴 Fil rouge : matrice de risque sectorielle

> **📌 FIL ROUGE — Épisode 9**
>
> Sophie produit la matrice de risque sectorielle d'EuroDefense en croisant les PIR avec les données du corpus. Le résultat identifie quatre zones rouges : espionnage étatique (Chine/Russie) sur la branche défense et les contrats OTAN, ransomware sur la supply chain IT, menace RPDC sur la branche spatial/UAV, et prépositionnement potentiel sur les réseaux OT industriels. Elle identifie aussi une zone orange négligée : le risque de campagne d'influence ciblée visant les contrats OTAN/ESA — un scénario hybride qui n'est pas couvert par le CERT mais par la communication du groupe.

> **🎯 CAPSTONE Partie II** : Rédiger un briefing exécutif (2 pages) attribuant un intrusion set observé sur un réseau industriel européen à un nexus étatique. Le briefing doit expliciter : les éléments techniques, comportementaux et contextuels soutenant l'attribution ; le niveau de confiance (Admiralty + LCA) ; les hypothèses alternatives ; les limites de l'attribution ; et les recommandations immédiates.

---
