---
title: Chapitre 32 — Extorsion, rançon et arbitrages stratégiques
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VI — Éradication, reconstruction ET reprise
  - index.md
---

## 32.1 Le paysage de l'extorsion en 2025-2026

L'extorsion cyber a considérablement évolué. La **simple extorsion** (chiffrement seul) est devenue rare — la plupart des victimes qui ont de bonnes sauvegardes refusent de payer. La **double extorsion** (chiffrement + menace de publication des données exfiltrées) est le standard depuis 2020 — même si la victime peut restaurer ses systèmes, la menace de publication de données sensibles crée une pression supplémentaire. La **triple extorsion** (chiffrement + publication + pression directe sur les clients, employés, ou partenaires de la victime) se développe — certains groupes contactent directement les clients de la victime pour les informer de la fuite, ou menacent les employés individuellement. Certains groupes abandonnent le chiffrement et ne pratiquent que l'exfiltration avec menace de publication (**pure data extortion**) — ce modèle nécessite moins de compétences techniques et génère des revenus significatifs.

## 32.2 Payer ou ne pas payer : les arguments

**Arguments pour ne pas payer :** position de principe (ne pas financer le crime), pas de garantie que le déchiffreur fonctionnera, pas de garantie que les données ne seront pas publiées (les attaquants mentent), signal envoyé que l'organisation est une « bonne payeuse » (risque de reciblage), risque de sanctions OFAC/UE (si l'opérateur est sanctionné), et positionnement éthique (l'ANSSI et les autorités françaises recommandent de ne pas payer).

**Arguments pour payer :** quand les sauvegardes sont détruites et que l'activité ne peut pas reprendre autrement (survie de l'entreprise en jeu), quand des vies sont en danger (hôpital sans accès aux dossiers patients), quand le coût de la non-reprise dépasse significativement le montant de la rançon. Payer n'est pas illégal en France (ce n'est pas une interdiction légale mais une recommandation de l'ANSSI), mais c'est une décision stratégique avec des implications juridiques, éthiques et réputationnelles.

## 32.3 Si la décision est de payer

Engagement d'un négociateur spécialisé (certains PRIS ou courtiers spécialisés offrent ce service — la négociation est un métier, pas une improvisation). Vérification de la liste des sanctions OFAC et de l'UE (payer une entité sanctionnée expose à des sanctions pénales). Négociation du montant (les rançons sont systématiquement négociables — des réductions de 40 à 60 % sont courantes). Test du déchiffreur sur un échantillon avant paiement complet. Documentation exhaustive pour l'assureur (si la police couvre la rançon — ce qui est de moins en moins fréquent en France depuis la loi LOPMI de 2023 qui conditionne le remboursement au dépôt de plainte dans les 72h).

## 32.4 Gestion de la publication des données

Si la décision est de ne pas payer (ou si l'attaquant publie malgré le paiement), la publication des données sur le leak site est quasi certaine. L'organisation doit anticiper : monitoring du leak site pour détecter la publication dès qu'elle survient, communication proactive vers les personnes concernées (RGPD — notification aux personnes dont les données sont publiées), communication publique préparée (communiqué de presse factuel, validé juridiquement), et analyse des données publiées (quelles données exactement ? le volume correspond-il à l'exfiltration estimée ? y a-t-il des données de tiers ?).

## 32.5 Fil rouge — BLACKTIDE : la rançon

> **🔍 BLACKTIDE — Épisode 32**
>
> PhantomCrypt demande 4,2 M€ en Bitcoin, avec un compte à rebours de 10 jours sur le portail de négociation. Le portail est professionnel : chat en direct, FAQ, démo de déchiffrement sur 3 fichiers gratuits.
>
> L'analyse de la direction : les sauvegardes offline (bandes) sont intactes — la production peut reprendre avec 6 jours de perte. Les données R&D exfiltrées (310 Go) seront publiées que la rançon soit payée ou non (pas de garantie de suppression). Les données RH (70 Go) seront publiées aussi. Le coût de la non-reprise est limité (les sauvegardes fonctionnent). Le coût réputationnel de la publication est réel mais gérable.
>
> **Décision : ne pas payer.** Documentée, signée par le CEO. Motifs : sauvegardes exploitables, pas de garantie sur les données, refus éthique de financer le crime. La rançon n'est pas couverte par l'assurance (exclusion contractuelle).
>
> J+10 : PhantomCrypt publie les données sur son leak site. Le DPO notifie les 8 000 employés dont les données RH sont concernées. L'image de marque est impactée — 3 articles dans la presse spécialisée, 1 article dans un quotidien national. Le cours de bourse d'Arvantis baisse de 2,3 % avant de se stabiliser.

---
