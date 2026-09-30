---
title: MITRE
source: Cyber/05_Cyberdefense/Frameworks Cyber Defense (Kill chain, Pyramid of pain, UKC, Diamant).md
note: Frameworks de cyberdéfense (Kill chain, Pyramid of pain, UKC, Diamant)
up:
- - Frameworks de cyberdéfense (Kill chain, Pyramid of pain, UKC, Diamant)
  - index.md
---

Organisation à but non lucratif qui créée des projets liés à la cybersécurité :

- Terminology :

|Terme|Signification|
|---|---|
|**APT** (_Advanced Persistent Threat_)|Groupe organisé (souvent étatique) menant des attaques prolongées et ciblées.|
|**TTPs**|Décrit comportement global d’un attaquant, pas juste un indicateur technique.  <br>- _T_**actic** → objectif de l’adversaire  <br>- **Technique** → méthode pour atteindre l’objectif  <br>- **Procedure** → manière concrète d’exécuter la technique|

### ATT&CK Framework & NAVIGATOR : Décrit les attaques

Base de connaissance sur les tactiques et techniques des cyberattaquants, décrit TTP.

- For Enterprise contient 14 catégories (de reconnaissance à impact), chaque catégories contient la technique pour parvenir à sa tactique

![image 10 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-10-1.png)

- Sous chaque tactique → Plusieurs techniques, parfois déclinées en sous-techniques.

![image 11 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-11-1.png)

![image 12 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-12-1.png)

- Chaque fiche technique détaille : Description, Procedure Examples, détection, mitigation, liens avec des groupes et logiciels

![image 13 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-13-1.png)

![image 14 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-14-1.png)

#### Navigator

Permet de visualiser et d’annoter les matrices, utiles pour individualiser en fonction de soihttps://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fgroups%2FG0008%2FG0008-enterprise-layer.json

![image 15 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-15-1.png)

![image 16 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-16-1.png)

  

### CAR (Cyber Analytics Repository) : Explique comment les détecter

Un référentiel d’**analyses de détection** basé sur le modèle ATT&CK. CAR complète ATT&CK qui décrit les attaques, CAR explique comment les détecter. https://car.mitre.org/

- Fournit des éléments divers :
	- Pseudocodes décrivant requêtes de détection (Splunk, EQL…)
	- Références vers TTPs
	- Implémentations selon OS et outils.

![image 17 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-17-1.png)

![image 18 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-18-1.png)

![image 19 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-19-1.png)

  

### ENGAGE : Planifier et mener opérations d’engagement adversaire

- Cyber Denial : Empêcher l’adversaire d’agir
- Cyber Deception : Le tromper volontairement
- Catégories principales (Engage Matrix) :

|Catégorie|Description|
|---|---|
|**Prepare**|Actions préliminaires menant à l’objectif|
|**Expose**|Identifier l’adversaire via la tromperie|
|**Affect**|Actions qui perturbent ses opérations|
|**Elicit**|Recueillir des infos sur son mode opératoire|
|**Understand**|Analyser les résultats obtenus|

![image 20 1.png](../../../assets/frameworks-cyber-defense-kill-chain-pyramid-of-pain-ukc-diamant-image-20-1.png)

- **Engage Matrix Explorer** → permet d’explorer ces interactions.

### D3FEND : Base de connaissance des contre-mesures cyber

- Chaque artefact contient

|   |   |
|---|---|
|**Catégorie**|**Description**|
|Definition|Information sur ce qu’est la technique|
|How it works|Comment cette technique fonctionne|
|Consideration|Chose à penser lors de l’implémentation|
|Example|Comment utiliser la technique|

### ATT&CK Emulation Plans : Simuler attaques réelles

### ATT&CK & Threat Intelligence : Faire lien TTP et posture défensive


## TLP

- **TLP:RED** : Réservé aux participants directs (yeux/oreilles uniquement). Pas de partage.
- **TLP:AMBER** : Partage limité au sein de l'organisation et avec les clients.
- **TLP:AMBER+STRICT** : Partage limité à l'organisation uniquement.
- **TLP:GREEN** : Partage avec la communauté (partenaires, secteur).
- **TLP:CLEAR** : Public (pas de restriction).


## L'évaluation de la confiance (Admiralty Code / NATO System)

En CTI, une info n'est jamais fiable à 100%. Tu dois ajouter comment noter tes sources.

- **Fiabilité de la source (A à F)** : De "A - Complètement fiable" à "F - Impossible à évaluer".
- **Crédibilité de l'information (1 à 6)** : De "1 - Confirmée par d'autres sources" à "6 - Impossible à évaluer".
- _Exemple :_ Une info classée **A1** est un fait avéré venant d'une source sûre. Une info **E5** est une rumeur improbable.


## Biais cognitif

|   |   |   |   |
|---|---|---|---|
|**Biais**|**Définition**|**Exemple**|**Contre-mesure**|
|**Biais de confirmation**|Chercher uniquement les preuves qui valident notre hypothèse de départ.|"Je suis sûr que c'est APT28, donc je cherche seulement des IP russes."|**ACH (Analysis of Competing Hypotheses) :** Essayer activement de prouver que son hypothèse est fausse.|
|**Biais de récence**|Donner plus d'importance aux informations reçues récemment.|"On a vu 3 attaques de ransomware hier, donc cette alerte est forcément un ransomware."|Regarder les statistiques historiques sur 12 mois.|
|**Effet de groupe**|S'aligner sur l'opinion de la majorité ou du chef sans critique.|"Si le Senior Analyst dit que c'est bénin, je ne vérifie pas."|Encourager l'avocat du diable ("Red Teaming" des idées).|
