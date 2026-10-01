---
title: Chapitre 12 — Cadrer une mission OSINT
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 12.1 La phase la plus négligée et la plus déterminante

Le cadrage est la phase d'orientation du cycle du renseignement (Ch.5) appliquée à une mission concrète. C'est la phase **la plus négligée** par les analystes pressés ou peu structurés, et **la plus déterminante** pour la qualité du livrable final. Une mission mal cadrée produit un rapport vague qui ne sert ni le commanditaire ni l'analyste. Une mission bien cadrée se déroule sans dérive et produit un livrable utile.

Le cadrage répond à sept questions structurantes.

## 12.2 Qui demande ?

Identifier précisément le **commanditaire réel**. Ce n'est pas toujours évident.

**Cas typiques.**

- Un cabinet d'avocats mandate au nom d'un client final. Qui est le client final ? A-t-on accès à lui ? Y a-t-il des restrictions de communication ?
- Une direction interne d'entreprise mandate. Quelle direction (juridique, sécurité, RH, conformité, audit) ? Avec quelle légitimité interne ?
- Un journaliste sollicite pour une enquête. Quel média ? Quelle rédaction valide la publication ?
- Un particulier sollicite (cas à examiner avec prudence).

Connaître le commanditaire réel permet d'évaluer la légitimité, d'anticiper les enjeux, de calibrer le livrable.

## 12.3 Pourquoi ?

La **motivation** du commanditaire détermine la finalité de l'enquête.

**Motivations légitimes typiques.**

- Préparation d'un contentieux.
- Due diligence pré-transaction.
- Vérification de partenaire commercial.
- Investigation de fraude interne.
- Protection contre une menace identifiée.
- Vérification de réputation pré-recrutement (cadre encadré).
- Enquête journalistique d'intérêt public.

**Motivations problématiques (signaux d'alerte).**

- « Je veux savoir ce qu'il fait » (vague, possible stalking).
- « Mon ex-conjoint(e) » (très haute probabilité de stalking).
- « Pour faire pression sur lui » (instrumentalisation possible).
- « Pour le faire renoncer » (chantage potentiel).
- « Pour le punir » (vengeance).
- Refus de répondre clairement.

Une motivation problématique = refus du mandat. Pas de « zone grise », pas de « si j'aide cette fois ». Le métier en dépend.

## 12.4 Sur qui ? (la cible)

La **cible** est définie précisément : personne physique, personne morale, événement, contenu, réseau ?

**Personne physique.** Nom, date de naissance (au moins année), juridiction de résidence, contexte professionnel. Plus la cible est précise, moins on risque l'homonymie (Ch.26).

**Personne morale.** Raison sociale, juridiction, numéro d'enregistrement (SIREN, registration number), forme juridique, activité.

**Événement.** Date, lieu, nature. Une vidéo, une publication, un incident.

**Contenu.** URL, hash, source, contexte de découverte.

**Réseau.** Groupe d'entités liées (réseau d'influence, cluster crypto, écosystème criminel). Plus complexe à cadrer, demande explicitation des limites.

## 12.5 Pour quoi ? (la décision attendue)

Quelle **décision** le commanditaire prendra-t-il sur la base du livrable ?

- Décider de déposer plainte / saisir une autorité.
- Décider d'entrer en transaction / la suspendre.
- Décider de licencier / d'engager.
- Décider de publier un article / le retenir.
- Décider d'engager une action de protection.
- Décider d'investir / s'abstenir.

Connaître la décision conditionne la **forme** du livrable, son **niveau de preuve requis**, et son **délai**.

## 12.6 Quel périmètre ?

Le **périmètre** définit ce qui entre et ce qui sort de l'enquête.

**Dimensions du périmètre.**

- **Temporel** : sur quelle période ? Faits depuis 2020 ? Depuis la création de la société ? Depuis un événement déclencheur ?
- **Géographique** : quelle juridiction ? France uniquement ? UE ? International ?
- **Thématique** : volet financier seulement ? Volet personnel ? Volet désinformation ?
- **Profondeur** : analyse de surface ou enquête approfondie ?
- **Exclusions** : qu'est-ce qu'on ne touche **pas** explicitement (vie privée familiale, mineurs, certaines juridictions sensibles) ?

Un périmètre flou = dérive d'enquête garantie. Un périmètre trop large = épuisement budget sans livrable.

## 12.7 Quelles limites ?

Au-delà du périmètre, des **limites** explicites sont définies.

**Limites typiques.**

- **Légales** : pas d'accès non autorisé, pas d'interaction avec mineurs, pas de juridictions interdites.
- **Éthiques** : pas de doxxing, pas de surveillance famille.
- **Méthodologiques** : pas de bases payantes au-delà d'un seuil, pas d'outils non auditables.
- **Opérationnelles** : aucune interaction avec la cible (cas MIRAGE).
- **Confidentialité** : aucune communication externe avant livraison.

Les limites sont **écrites** dans le mandat. Elles protègent l'analyste autant que le commanditaire.

## 12.8 Quel livrable, quel délai, quel budget ?

**Livrable.** Note flash 2 pages ? Rapport complet 30 pages ? Rapport judiciaire versable au dossier ? Présentation orale ? Fiches entité ? Graphe ?

**Délai.** Calé sur la décision attendue. Un cadrage précoce permet d'évaluer si le délai est réaliste.

**Budget.** Définit l'envergure : nombre de jours-homme, accès à des outils payants, déplacement éventuel, partenariats nécessaires.

Si le triangle « livrable / délai / budget » est incohérent (livrable ambitieux, délai court, budget faible), c'est dit dès le cadrage. Mieux vaut renégocier que livrer un travail bâclé.

## 12.9 Document de cadrage : le SOR

Le **SOR** (Statement of Requirements, ou cahier des charges OSINT) formalise le cadrage. C'est un document court (2-3 pages) qui sert de contrat opérationnel entre l'analyste et le commanditaire.

**Sections du SOR.**

1. Contexte de la demande (court).
2. Commanditaire et destinataires.
3. Objectifs de l'enquête (questions de renseignement principales).
4. Cible(s).
5. Périmètre temporel, géographique, thématique.
6. Limites légales, éthiques, opérationnelles.
7. Livrables attendus (type, niveau de preuve).
8. Délai et jalons.
9. Budget et ressources.
10. Confidentialité, classification, diffusion.
11. Validation (signature du commanditaire).

Un SOR signé est la pierre angulaire d'une mission propre.

> **MIRAGE — Épisode 0 : Cadrage du mandat**
>
> Vendredi 16 mai 2026, 14h. Réunion dans les bureaux du cabinet Legrand & Associés, 6e arrondissement de Paris. Me Patricia Legrand expose le mandat : son client, actionnaire minoritaire (12 %) de TechnoVert SAS, soupçonne Marc Delaunay, DAF, de cinq agissements (détournement, blanchiment crypto, désinformation contre lanceur d'alerte, faux comptes coordonnés, deepfakes). Le client envisage un dépôt de plainte au PNF.
>
> L'analyste pose les questions de cadrage : qui est le commanditaire réel (Me Legrand, mandatée par l'actionnaire qui ne sera pas directement en contact) ; quelle décision (dépôt de plainte) ; quel périmètre (Delaunay, ses sociétés, ses flux visibles, son écosystème ; pas la famille, pas les mineurs ; France et juridictions où il opère manifestement, soit Malte, Chypre, BVI, Luxembourg, Maroc selon premières indications) ; quel livrable (rapport complet versable au dossier judiciaire, 30-50 pages) ; quel délai (6 semaines) ; quel budget (raisonnable, sans bases premium).
>
> Trois limites explicites sont posées : aucune interaction avec Delaunay (techniquement compétent), aucun accès non autorisé, aucune méthode susceptible de compromettre la procédure pénale ultérieure. Le SOR est signé en début de semaine suivante. L'enquête peut démarrer.

## 12.10 Réflexes du cadrage

- Toujours reformuler la demande du commanditaire.
- Toujours écrire le SOR.
- Toujours signer le SOR avant collecte.
- Toujours évaluer la triangulation livrable/délai/budget.
- Toujours détecter les signaux d'alerte sur la motivation.
- Toujours documenter les exclusions.
- Toujours prévoir un point de revue à mi-parcours.

-----
