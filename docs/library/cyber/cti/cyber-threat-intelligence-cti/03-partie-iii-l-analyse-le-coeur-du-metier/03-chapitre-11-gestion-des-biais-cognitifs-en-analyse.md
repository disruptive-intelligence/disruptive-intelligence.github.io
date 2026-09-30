---
title: Chapitre 11 — Gestion des biais cognitifs en analyse CTI
source: Cyber/01_CTI/CTI.md
note: Cyber Threat Intelligence (CTI)
up:
- - Cyber Threat Intelligence (CTI)
  - ../index.md
- - 'Partie III — L''analyse : le cœur du métier'
  - index.md
---

## 11.1 Le biais de confirmation

Le piège le plus dangereux et le plus universel. L'analyste qui suspecte APT28 cherche les IoC d'APT28, trouve des similitudes (forcément — les techniques ATT&CK sont partagées), et conclut « c'est APT28 » sans avoir testé les alternatives. Contremesure : l'ACH (qui force à tester toutes les hypothèses), le devil's advocate (un collègue est désigné pour argumenter contre la conclusion principale), et la question systématique « qu'est-ce qui pourrait contredire cette conclusion ? ».

## 11.2 Le biais de disponibilité

L'analyste surévalue les événements récents ou médiatisés. Le dernier rapport Mandiant parle de Volt Typhoon — donc tout comportement LotL est attribué à Volt Typhoon, même si 50 autres acteurs utilisent les mêmes techniques. Contremesure : rechercher systématiquement les acteurs alternatifs qui utilisent les mêmes TTP (la matrice ATT&CK Navigator montre tous les acteurs associés à une technique).

## 11.3 L'anchoring

L'analyste s'accroche à la première information reçue. Le premier rapport d'IR disait « ransomware » (parce qu'un fichier chiffré a été trouvé) — toute l'investigation CTI est cadrée comme un incident ransomware, même quand les indices pointent vers de l'espionnage avec un wiper déguisé en ransomware (exactement le modus operandi de NotPetya). Contremesure : réévaluer périodiquement les hypothèses à la lumière des données nouvelles, et accepter que la première impression soit fausse.

## 11.4 Le mirror imaging

L'analyste prête à l'adversaire sa propre logique. « Aucun acteur rationnel ne ciblerait cette PME de 50 personnes » — faux : la PME est sous-traitante d'un OIV, et c'est le vecteur d'accès supply chain. L'analyste occidental qui pense « aucun État ne risquerait une escalade en sabotant une infrastructure civile » projette sa propre rationalité sur un adversaire qui peut avoir une grille de calcul radicalement différente. Contremesure : le Red Hat Analysis (se mettre dans la peau de l'adversaire avec sa logique, ses contraintes, et ses objectifs — pas les nôtres).

## 11.5 Le groupthink

L'équipe converge vers un consensus sans examen critique. Le premier analyste dit « c'est Sandworm », les autres acquiescent parce que c'est plausible et que personne ne veut être le contradicteur. Contremesure : le devil's advocate institutionnalisé (dans chaque analyse d'attribution, un analyste est formellement désigné pour argumenter contre la conclusion du groupe), et le pré-mortem (« imaginons que notre conclusion est fausse — pourquoi aurait-elle échoué ? »).

## 11.6 Le biais d'attribution

L'analyste attribue trop vite et avec trop de confiance. La pression est forte : le RSSI veut savoir « qui », les médias veulent un nom, et l'analyste veut montrer sa valeur. Résultat : une attribution hâtive basée sur un indice fragile (un IoC partagé, une technique commune) présentée avec une confiance excessive. Contremesure : la discipline du niveau de confiance (Ch.13 — jamais de conclusion sans qualification), et le rappel que « insuffisamment déterminé » est une conclusion valide et souvent la plus honnête.

---
