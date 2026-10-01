---
title: Chapitre 90 — Rapport judiciaire et précontentieux
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 90.1 Spécificités du rapport judiciaire

Un rapport OSINT destiné à un **usage judiciaire** (transmission à un magistrat, dépôt dans un dossier pénal, soutien à une procédure civile) impose des exigences renforcées :

- **Chain of custody** stricte sur chaque pièce.
- **Horodatage qualifié** (eIDAS).
- **Signature électronique** AdES.
- **Vocabulaire calibré** sans qualification pénale.
- **Documentation méthodologique** exhaustive.
- **Préservation** des originaux numériques.

## 90.2 L'analyste OSINT n'est pas un juge

**Principe.** L'analyste **identifie des éléments**, **les cote**, **propose des hypothèses**. Il **ne qualifie pas pénalement**.

**Mauvaise pratique.** « Delaunay a commis un détournement de fonds. »

**Bonne pratique.** « Les éléments collectés sont compatibles avec un montage de détournement de fonds, qualification dont l'établissement relève de l'autorité judiciaire après expertise complémentaire. »

L'analyste apporte le **substrat factuel** ; le magistrat **qualifie**.

## 90.3 Chain of custody

Pour chaque pièce :

- **Capture** datée, horodatée, signée.
- **Hash** SHA-256 sur le fichier collecté.
- **Source** documentée (URL, date d'accès).
- **Outil** utilisé pour la collecte (Hunchly version X, ExifTool version Y).
- **Préservation** : stockage chiffré, intégrité périodiquement vérifiée.
- **Historique** : toute manipulation tracée.

Si la pièce est transmise au magistrat, **bordereau** mentionnant ces éléments.

## 90.4 Horodatage qualifié eIDAS

Le règlement **eIDAS** (UE 910/2014) reconnaît les horodatages qualifiés émis par prestataires de services de confiance.

**Pour OSINT.**

- **OpenTimestamps** (open source, blockchain Bitcoin) : preuve d'antériorité non qualifiée mais robuste.
- **Prestataires qualifiés eIDAS** (LuxTrust, Certigna, etc.) : valeur juridique renforcée.
- **Cachet électronique qualifié** : pour personne morale (cabinet, organisation).

**Pratique.** Pour pièces centrales, double horodatage : OpenTimestamps + cachet électronique qualifié.

## 90.5 Signature électronique AdES

**AdES** (Advanced Electronic Signatures) : signature électronique reconnue eIDAS.

**Pour rapport.**

- **PAdES** (PDF Advanced Electronic Signatures) : standard pour PDF.
- **CAdES** : pour ensemble de fichiers.
- **XAdES** : pour XML.

**Niveaux.**

- **AdES-B** : niveau de base.
- **AdES-T** : avec horodatage.
- **AdES-LT** : long terme (preuves intégrées).
- **AdES-LTA** : avec horodatage périodique de la chaîne entière.

**Pour OSINT judiciaire.** PAdES-LT au minimum.

## 90.6 Vocabulaire judiciaire calibré

**À utiliser.**

- « Les éléments collectés documentent... »
- « Plusieurs sources convergentes attestent... »
- « Un faisceau d'indices suggère... »
- « Il est probable que... »
- « Les éléments ne permettent pas de conclure définitivement sur... »
- « Une expertise complémentaire serait nécessaire pour établir... »

**À éviter.**

- « Coupable », « auteur du délit », « fraude avérée » (qualifications pénales).
- « Sans aucun doute » (sur-affirmation).
- Adjectifs jugeants.

## 90.7 Préservation des originaux numériques

**Discipline.**

- **Captures HTML originales** préservées (Hunchly).
- **Captures PDF horodatées** complémentaires.
- **Hashes** consignés.
- **Sauvegarde 3-2-1** : 3 copies, 2 supports différents, 1 hors site, **toutes chiffrées**.

Le commanditaire (cabinet, magistrat) doit pouvoir, à tout moment, demander la pièce originale et vérifier son intégrité par hash.

## 90.8 Structure type d'un rapport judiciaire

Similaire au rapport complet (Ch.88), avec **renforcements** :

- **Page de garde** mentionne le statut judiciaire.
- **Préambule** explicite la finalité judiciaire et le cadre déontologique.
- **Méthodologie** exhaustive et reproductible.
- **Chaque fait** porte sa pièce annexe avec hash.
- **Conclusions** strictement calibrées WEP.
- **Annexe « catalogue de pièces »** liste chaque capture, hash, source, date d'accès.
- **Signature et horodatage** qualifiés.

## 90.9 Témoin et auditionné

L'analyste OSINT peut être convoqué comme **témoin** dans la procédure. Sa préparation :

- Connaissance approfondie de son rapport.
- Capacité à expliquer la méthodologie en termes simples.
- Maîtrise des limites identifiées.
- Posture honnête : ne pas affirmer plus que le rapport.
- Adhésion à la cotation : ne pas céder à pression d'avocat pour sur-affirmer.

## 90.10 Cas particulier — la procédure prud'homale

En cas MIRAGE, le volet désinformation contre Berthier impacte sa **procédure prud'homale** contre TechnoVert. Le rapport OSINT peut servir à :

- **Démontrer** que les pièces TechnoVert contre Berthier sont compatibles avec une fabrication.
- **Préciser** le contexte (campagne coordonnée).
- **Documenter** l'authenticité douteuse de pièces présentées comme « preuves » contre Berthier.

## 90.11 Différence avec l'expertise judiciaire

**Expertise judiciaire.** Mandatée par le magistrat, conduite par un expert inscrit, soumise à serment, contradictoire avec parties.

**Rapport OSINT.** Mandaté par une partie privée (cabinet d'avocats, entreprise), conduite par un cabinet OSINT, sans serment.

**Statut.** Le rapport OSINT est **pièce contributive**, pas expertise. Le magistrat peut le verser au dossier ; il a la valeur d'un avis privé technique.

**Pratique.** L'analyste OSINT peut être ultérieurement nommé expert (s'il est inscrit). Distinction préservée.

## 90.12 Synthèse — exigences renforcées

| Aspect | Rapport complet | Rapport judiciaire |
|---|---|---|
| Chain of custody | Recommandée | **Obligatoire** |
| Horodatage | OpenTimestamps | **eIDAS qualifié** |
| Signature électronique | DocuSign / similaire | **AdES PAdES** |
| Vocabulaire | Calibré WEP | **Renforcé sans qualification pénale** |
| Préservation pièces | 3-2-1 | **3-2-1 chiffré, intégrité vérifiée** |
| Annexes | Variables | **Catalogue exhaustif des pièces** |
| Tonalité | Sobre | **Strictement neutre** |

-----
