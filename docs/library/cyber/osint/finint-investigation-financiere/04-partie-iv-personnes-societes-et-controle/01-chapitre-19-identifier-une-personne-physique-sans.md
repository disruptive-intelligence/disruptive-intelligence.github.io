---
title: Chapitre 19 — Identifier une personne physique sans se tromper d’homonyme
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Maîtriser la **discipline d’identification** d’une personne physique. C’est l’erreur la plus courante et la plus dommageable en FININT : attribuer à une cible des éléments qui concernent en réalité un homonyme. Cette erreur peut détruire la crédibilité d’un livrable et causer un préjudice réel à un tiers innocent.

## Le concept

L’**homonymie** est une réalité statistique. Pour des prénoms et noms courants, on compte des centaines, voire des milliers d’homonymes dans un pays. Pour des noms moins courants, ce risque baisse mais n’est jamais nul. L’identification rigoureuse repose sur la **convergence** de plusieurs attributs.

## Les attributs d’identification

L’analyste cherche à stabiliser autant d’attributs que possible parmi :

- **Nom et prénoms** complets, dans l’ordre, avec orthographe précise.
- **Date de naissance** (jour, mois, année).
- **Lieu de naissance** (commune, pays).
- **Nationalité(s)** — peut être multiple.
- **Adresse(s) connue(s)** — actuelle, antérieures.
- **Numéro d’identification fiscale** (numéro fiscal de référence en France, NIF, NIN, etc.) — rarement accessible en OSINT, mais central en sources fermées.
- **Numéro de sécurité sociale** — non accessible en OSINT.
- **Numéro de passeport** — non accessible en OSINT sauf cas particuliers (leaks).
- **Photographie** — recoupement visuel.
- **Profil professionnel public** (LinkedIn, presse) — cohérence biographique.
- **Réseau familial** : conjoint, parents, frères et sœurs, enfants — souvent identifiable via presse ou réseaux sociaux.
- **Réseau professionnel** : associés, employeurs, mandats parallèles.

Plus le nombre d’attributs convergents, plus l’identification est solide. La règle pratique :

- 2 attributs forts (nom complet + date de naissance, ou nom + photo) = identification *possible*.
- 3-4 attributs convergents = identification *probable*.
- 5+ attributs convergents, dont des recoupements indépendants = identification *quasi-certaine*.

## Les pièges classiques

**Translittération** : un même nom peut s’écrire de plusieurs façons selon la langue source. « Mohamed » vs « Mohammad » vs « Muhammad ». « Иванов » → « Ivanov », « Ivanoff », « Iwanow » selon les conventions. L’analyste teste systématiquement les variantes.

**Articles et particules** : « Van der Berg », « De la Cruz », « Al-Hadi » — selon les sources, certaines parties peuvent être omises ou attachées. « Karim Haddad » peut apparaître comme « Haddad, Karim », « Karim El-Haddad », « K. Haddad », etc.

**Initiales** : les comptes annuels et certains documents officiels n’utilisent parfois que l’initiale du prénom. Source d’ambiguïté.

**Diminutifs** : « William » ↔ « Bill », « James » ↔ « Jim », « Catherine » ↔ « Cathy » ou « Kate » — fréquents dans le monde anglophone.

**Changement de nom** : mariage, divorce, naturalisation, raisons personnelles. Une personne née sous un nom peut apparaître sous un autre dans certains documents.

**Confusion père/fils** : Karim Haddad Senior vs Karim Haddad Junior — même nom, attributs différents. Toujours vérifier la date de naissance.

## Méthode — protocole d’identification en 6 étapes

1. **Collecter les attributs disponibles** : nom complet, date de naissance, lieu, nationalité, profession.
1. **Tester les variantes** : translittérations, articles, initiales, ordre.
1. **Croiser avec les sources** : registres (mandats déclarés), presse, leaks, réseaux sociaux.
1. **Identifier les homonymes potentiels** : combien de personnes avec ces attributs ?
1. **Valider par convergence** : la personne identifiée a-t-elle bien tous les attributs attendus ?
1. **Calibrer la confiance** : sur la base du nombre et de la qualité des recoupements.

## Mini-walkthrough

Cible : « Karim Haddad », mentionné dans une DS comme dirigeant suspect.

- Recherche initiale : « Karim Haddad » → des centaines de résultats Google, plusieurs profils LinkedIn, plusieurs entrées registre dans plusieurs pays.
- Attributs initiaux fournis par la DS : âge approximatif (« la cinquantaine »), nationalité (franco-libanais), domaine d’activité (négoce et import-export).
- Recherche affinée : « Karim Haddad » + « négoce » + « Liban » ou « France ».
- 3 candidats émergent :
  - Karim Haddad A, né 1965, ingénieur télécoms à Beyrouth → exclu (profession différente).
  - Karim Haddad B, né 1968, négociant franco-libanais, dirigeant déclaré de plusieurs sociétés en France et au Liban → match probable.
  - Karim Haddad C, né 1981, journaliste basé à Paris → exclu (profession différente).
- Recoupement complémentaire : RBE des SAS françaises identifie un UBO Karim Haddad, né 1968 à Beyrouth, nationalité française. Convergence : nom + date + lieu + nationalité + profession + mandats → identification *quasi-certaine*.

## Erreurs fréquentes

- **Conclure sur 2 attributs faibles** (nom + secteur) — risque homonyme élevé.
- **Ne pas tester les variantes orthographiques** — manque la cible si elle apparaît sous variante.
- **Ignorer les changements de nom** — femme mariée, naturalisation, etc.
- **Confondre père / fils** — toujours vérifier l’année de naissance précise.
- **Attribuer une photo sans recoupement** — un nom commun peut avoir plusieurs photos sur Internet, certaines non attribuables.

## Limites

L’identification peut rester **indéterminable** dans certains cas : très peu d’attributs accessibles (personne discrète, juridiction opaque), risque homonyme élevé (nom très courant), absence de photo ou de date de naissance. L’analyste documente explicitement la limite : *« Identification de M. K. Haddad établie à un niveau de confiance probable. Une confirmation quasi-certaine nécessiterait l’accès au numéro fiscal ou à un document d’identité, hors périmètre des sources ouvertes mobilisées. »*

## Lien avec le fil rouge

> **CLEARFLOW — Stabiliser Karim Haddad**
> 
> Avant toute autre analyse, Nassim consacre 2 heures à stabiliser l’identification : nom complet (Karim Élie Haddad), date de naissance (1968), lieux (Beyrouth puis Paris), nationalités (libanaise et française), parcours professionnel (négoce et import-export depuis 1995). Photo officielle récupérée via LinkedIn et site d’une chambre de commerce franco-libanaise. Cette stabilisation initiale conditionne tout le reste : sans elle, les attributions ultérieures seraient suspectes.

## Points clés à retenir

- L’identification rigoureuse repose sur la **convergence** de plusieurs attributs.
- Pièges : translittération, particules, initiales, diminutifs, changements de nom, père/fils.
- 5+ attributs convergents = quasi-certain ; 2 attributs faibles = à approfondir.
- Documenter explicitement les limites quand l’identification reste incomplète.

-----
