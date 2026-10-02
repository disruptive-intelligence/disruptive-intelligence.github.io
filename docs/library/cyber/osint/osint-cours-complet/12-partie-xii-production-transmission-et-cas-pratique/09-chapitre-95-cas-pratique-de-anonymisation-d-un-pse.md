---
title: 'Chapitre 95 — Cas pratique : dé-anonymisation d''un pseudonyme'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 95.1 Présentation du cas

Un compte X pseudonyme `@whistleblower_fr` publie depuis 6 mois des allégations détaillées de fraude contre une grande entreprise française, en revendiquant être un ancien employé. Le cabinet d'avocats de l'entreprise mandate l'analyste pour identifier qui se cache derrière, dans le but d'une procédure en diffamation potentielle.

**Cadrage éthique préalable.** L'identification d'un lanceur d'alerte présumé soulève des enjeux. Le mandat est documenté. L'analyste s'engage à :

- Vérifier d'abord si les allégations sont publiquement étayées.
- Documenter prudemment.
- Ne pas exploiter pour intimidation.
- Limiter la diffusion au mandat (avocats de l'entreprise, pas publication, pas réseau social).
- Refuser si glissements vers harcèlement.

## 95.2 Étape 1 — Analyse du compte

**Profil.**

- @whistleblower_fr, créé en juillet 2025.
- Photo profil : avatar génériquement « business-like » (à tester pour origine IA).
- Bio : « Ancien employé. Je dis ce que vous taisez. »
- 1842 followers, 12 followings.
- 287 posts.

**Analyse photo profil.** Hive Moderation : 78 % « AI-generated ». Optic AI or Not : « AI ». **Conclusion : photo IA, pas un visage réel.**

**Cohérence linguistique.** Style soigné, vocabulaire de cadre supérieur, références à des processus internes (RH, comité de direction, audit) avec terminologie professionnelle.

## 95.3 Étape 2 — Analyse des posts

**Patterns.**

- 287 posts en 6 mois ≈ 1.6 / jour.
- Horaires : majoritaire 19h-23h français.
- Jours : très peu le weekend, suggérant pratique professionnelle structurée.
- Allégations factuelles spécifiques (noms de dirigeants, processus internes, chiffres).
- Pas de réponse aux mentions techniques pointues (suggère prudence opérationnelle).

**Conclusion préliminaire.** Probablement un humain, vraisemblablement avec expérience effective dans l'entreprise (cohérence des détails internes). Pseudo prudent (avatar IA).

## 95.4 Étape 3 — Stylométrie légère

**Échantillonnage de 30 posts longs.**

**Indicateurs récurrents.**

- Tournures spécifiques (« j'ajoute », « il faut savoir que », « rappelons que »).
- Ponctuation : usage généreux du point-virgule.
- Émojis : aucune utilisation.
- Capitalisations : sobre.
- Vocabulaire : « gouvernance », « processus », « conformité », « éthique ».

**Hypothèse.** Profil cadre supérieur, formation universitaire ou ingénieur, sensibilité gouvernance / conformité (possiblement audit ou contrôle).

## 95.5 Étape 4 — Recherche cross-plateformes

**Sherlock sur `whistleblower_fr`.** Pas d'autres comptes ce username.

**Recherche dans documents internes (sites entreprise publics).** Recherche de tournures stylométriques spécifiques détectées sur les sites publics de l'entreprise (communiqués, blog interne consulté).

**Hit faible.** Aucune correspondance directe.

**Approche alternative.** Recherche par sujets abordés. Les allégations concernent un processus spécifique : « audit interne 2022 » d'une filiale.

## 95.6 Étape 5 — Recherches LinkedIn

**Compte d'investigation LinkedIn (compte invest mature).**

**Recherche.** Anciens employés de l'entreprise sur la période (audit interne, finance, conformité, RH supérieures).

**Filtres.** Postes « audit », « contrôle », « risque », « gouvernance », « conformité », chez l'entreprise cible entre 2020 et 2024 (a quitté entre 2024 et 2025).

**Résultats.** 23 profils correspondants.

## 95.7 Étape 6 — Triangulation

**Croisement.**

- Profil 1 : a quitté l'entreprise en juillet 2024 (timing aligné avec création @whistleblower_fr en juillet 2025).
- Profil 1 : poste senior en audit interne 2020-2024, exposition au processus mentionné dans les posts.
- Profil 1 : signatures de mémos publics avec mêmes tournures stylométriques (« il faut savoir », « rappelons »).
- Profil 1 : photo correspondant à description vague que le compte donne accidentellement de lui-même.

**Hypothèse forte.** Profil 1 est probablement @whistleblower_fr. Cotation B2.

## 95.8 Étape 7 — Vérifications complémentaires

**Avant conclusion, vérifications.**

**Aliase numérique.** GitHub / autres comptes de Profil 1 ? Recherche Holehe / Sherlock sur email LinkedIn présumé : aucun lien direct.

**Cohérence temporelle.** Profil 1 a-t-il signalé en interne d'abord, est-il en procès, a-t-il témoigné ailleurs ? Recherche presse : oui, mentionné dans une enquête presse 2024 comme « source anonyme proche du dossier ».

**Cohérence motivationnelle.** Profil 1 aurait pu créer @whistleblower_fr pour continuer à dénoncer publiquement après son départ. Cohérent.

## 95.9 Étape 8 — Cotation finale et formulation

**Cotation.** B2 forte (faisceau d'indices convergents : timing, expertise, stylométrie, photo, presse anonyme). Pas A1 (pas d'aveu direct, pas de lien email/IP démontré).

**Formulation pour rapport.**

> Plusieurs éléments convergents suggèrent fortement que le compte @whistleblower_fr est probablement opéré par [Nom], ancien auditeur interne ayant quitté l'entreprise en juillet 2024. Ces éléments sont : (a) cohérence temporelle entre départ et création du compte, (b) cohérence des sujets abordés avec son périmètre d'intervention en interne, (c) cohérence stylométrique avec mémos publics signés, (d) source anonyme mentionnée dans la presse 2024 dans des termes compatibles. Niveau de confiance : probable. **Démonstration directe par lien email / IP / aveu nécessiterait approche complémentaire (réquisition judiciaire si procédure engagée).**

## 95.10 Étape 9 — Discussion éthique

**Pour le rapport.**

- L'analyste rappelle au cabinet que [Nom] a probablement le statut de **lanceur d'alerte** au sens des dispositifs européens (directive 2019/1937) et français (loi Sapin 2 modifiée).
- Procédure abusive en diffamation peut constituer une **infraction nouvelle** (procédure-bâillon, art. 712-1 et suivants du CPP modifié).
- Recommandation : avant action en justice, audit des allégations factuelles ; si certaines sont fondées, gestion par dialogue ou enquête interne, pas action judiciaire.

L'analyste a fait son travail technique ; il assume aussi sa responsabilité morale en alertant.

## 95.11 Pédagogie

Ce cas illustre :

- Maturité OPSEC d'une cible (avatar IA, pseudonyme).
- Triangulation par stylométrie + cohérence temporelle + cohérence thématique.
- Cotation prudente (B2 plutôt que A1 sans aveu direct).
- Responsabilité éthique de l'analyste qui peut alerter sur les conséquences possibles.
- Limite OSINT : démonstration directe demande réquisition judiciaire.

-----
