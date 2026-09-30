---
title: 'Chapitre 56 — Cas 2 : Fraude au changement d’IBAN / BEC'
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IX — Cas pratiques déroulés
  - index.md
---

## Contexte

Une PME française du secteur agroalimentaire, **ALPHA INDUSTRIE SARL**, 28 employés, 6 M€ de CA annuel, est victime d’une fraude au virement le mardi 14 mars. Montant : **215 000 €**. La fraude est découverte le mercredi matin lors d’un appel du vrai fournisseur réclamant son paiement.

ALPHA dépose plainte le mercredi 15 mars matin et saisit son cabinet d’avocats. Le cabinet sollicite une expertise FININT pour le volet traçage et reconstitution.

**Demande** : reconstituer la séquence, identifier les acteurs, évaluer les chances de récupération, préparer les éléments pour la procédure judiciaire et la coopération internationale.

## Indices initiaux fournis

- Le directeur financier d’ALPHA a reçu, le lundi 13 mars à 17h30, un email apparemment du dirigeant d’un fournisseur habituel (entreprise espagnole **TAIDA SL**), signalant un changement d’IBAN pour la prochaine facture.
- Le mardi 14 mars à 14h32, paiement effectif via SCT Inst de 215 K€ vers l’IBAN ES indiqué (compte au nom d’**IBERICA TRADING SL**, société espagnole).
- Le mercredi 15 mars vers 9h, le vrai TAIDA SL appelle ALPHA pour réclamer le paiement.
- L’examen de l’email frauduleux montre un domaine très proche du vrai TAIDA (typosquatting : `taida-sl.es` vs vrai `taidasl.es`).
- La banque d’ALPHA a tenté un rappel SCT Inst : refusé (compte récepteur a accepté l’opération ; SCT Inst irréversible sans accord).

## Cadrage initial

**Questions de renseignement** :

- QR1 — Reconstituer la séquence en aval (où sont allés les 215 K€ ?).
- QR2 — Identifier l’attaquant (groupe organisé, isolé, niveau d’expérience).
- QR3 — Quels leviers pour récupération partielle ?
- QR4 — Quelles coopérations engager ?

**Budget temps** : 1 semaine pour le cœur du travail, plus suivi.

**Limites prévisibles** : sans réquisitions des banques étrangères, traçage des comptes étrangers limité. Volet crypto à confier à Athéna Group / OSINT Crypto.

## Collecte

**OSINT sur IBERICA TRADING SL** :

- Registre espagnol (RMC) : société créée 4 mois avant les faits. Capital 3 000 €. Activité déclarée : « commerce de gros divers ». Dirigeant unique : un national espagnol d’environ 35 ans, sans expérience commerciale antérieure visible.
- Adresse : domiciliation à Madrid.
- Pas de site web. Pas de présence en ligne.
- Lecture : *probable* société de mule / shell créée pour l’opération.

**Compliance bancaire (via avocats)** :

- La banque d’IBERICA en Espagne, sollicitée, indique des transferts sortants rapides après le crédit de 215 K€.
- Détail (partiel, sous le cadre coopération européenne) :
  - 14h35-14h41 : 5 SCT Inst sortants depuis IBERICA vers 5 IBAN distincts (3 au Portugal, 2 en Lituanie).
  - Chaque sortie : 40 000 € à 45 000 €.
  - Bénéficiaires : 5 comptes ouverts récemment dans 3 banques différentes (Revolut LT, Wise via BE, et 3 banques portugaises moyennes).

**OSINT sur les 5 destinataires** : tous sont des personnes physiques (apparemment), avec profils minimaux. Aucun lien apparent entre elles. *Probable* réseau de mules.

**Volet crypto (confié à Sarah Marin / Athéna Group)** :

- Sur les 5 comptes en aval (LT, PT), 4 sur 5 ont rapidement (16h12-16h18) effectué des dépôts USDT sur un exchange A (basé hors UE, profil KYC ambigu).
- Les USDT sont sortis dans l’heure vers un wallet auto-géré, puis fragmentés via plusieurs adresses.
- Le rapport on-chain Athéna identifie une convergence : plusieurs des adresses finales correspondent à un cluster connu de cashout opérant sur des exchanges asiatiques non-KYC.
- *Quasi-certaine* attribution du cashout à un réseau organisé, mais identification individuelle des attaquants reste *indéterminable* au niveau on-chain seul.

## Analyse

**Reconstitution de la séquence** :

```
T-48h (lundi 17h30) : email frauduleux reçu par DF ALPHA, taida-sl.es (typosquat).
T-0   (mardi 14h32) : SCT Inst ALPHA → IBERICA, 215 K€.
T+3min                : Fractionnement IBERICA → 5 IBAN (PT, LT), 40-45 K€ chacun.
T+1h40                : Dépôts USDT sur exchange A par 4 des 5 comptes.
T+2h45                : Sorties USDT vers wallet auto-géré.
T+4h15                : Fragmentation crypto, convergence vers cluster cashout asiatique.
T+18h (mercredi 9h)   : ALPHA découvre la fraude.
```


**Acteurs et rôles** :

- Attaquant initial : auteur de l’email, *probable* groupe organisé (la sophistication du typosquatting + la connaissance du nom du fournisseur réel + le timing avec date de facturation suggèrent un repérage préalable).
- IBERICA TRADING SL : société écran de réception (mule de premier niveau).
- 5 comptes en aval : mules de deuxième niveau.
- Cluster cashout asiatique : infrastructure de monétisation.

**Typologie** : BEC avec layering rapide multi-PSP et cashout crypto. Schéma classique 2023-2025.

## Hypothèses calibrées

- BEC : quasi-certain.
- Réseau de mules organisé : quasi-certain.
- Attribution à un groupe spécifique : indéterminable au niveau du cabinet ; CTI / coopérations internationales nécessaires.
- Récupération totale : peu probable. Récupération partielle (50 000 € à 80 000 € si action très rapide sur comptes ES et PT non encore vidés) : possible.

## Limites

- Identification précise des attaquants : *indéterminable* au niveau de l’enquête privée. Reste à l’enquête judiciaire et aux coopérations internationales (Europol EC3, INTERPOL).
- Récupération crypto : la portion convertie en USDT est *peu probable* à récupérer (cashout déjà effectué dans des juridictions à faible coopération).
- La portion encore en comptes ES/PT (si non vidés) : *possible* à geler par requête judiciaire urgente, avec saisine du parquet européen via le PNF si applicable.

## Livrable

Rapport au client (ALPHA, via le cabinet d’avocats) :

- Reconstitution de la séquence.
- Cartographie des comptes et des juridictions.
- Pour la procédure : éléments à transmettre au parquet (déjà saisi par la plainte).
- Pour la récupération : actions immédiates (saisine du parquet européen pour gel des comptes ES et PT non vidés ; coopération via FIU.NET pour les comptes LT).
- Pour les leçons : audit des procédures internes (process de validation des changements d’IBAN, double signature, vérification téléphonique).

## Bilan honnête

La fraude est constatée. La portion fiat (encore en comptes ES/PT) peut être partiellement gelée si action très rapide (24-48h après dépôt de plainte) — en pratique, les délais administratifs et judiciaires ramènent souvent ces espoirs à 10-25 % de récupération réelle. La portion crypto (~75 % du montant) est *quasi-certainement* perdue. L’identification des attaquants est *indéterminable* au niveau du cabinet ; elle dépend des coopérations internationales et des renseignements policiers (cluster connu = identification *possible* avec temps et coopération).

Le travail FININT et OSINT Crypto a un double rôle : (1) tenter de sauver la partie fiat encore mobilisable, (2) alimenter la procédure judiciaire et les coopérations pour démantèlement à terme du réseau.

## Leçons FININT

- **La vitesse est centrale.** Au-delà de 24h, la majorité des fonds est partie.
- **FININT et OSINT Crypto se complètent.** Le partage du dossier est efficace.
- **Les mules ne sont pas l’objectif final** : elles sont des indicateurs vers les organisateurs.
- **Récupération vs identification** : deux objectifs différents, qui exigent des actions différentes.
- **Prévention vaut récupération** : un audit des procédures préviendrait l’écrasante majorité des BEC.

-----
