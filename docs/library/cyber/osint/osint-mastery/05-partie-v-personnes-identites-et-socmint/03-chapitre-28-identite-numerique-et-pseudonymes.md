---
title: Chapitre 28 — Identité numérique et pseudonymes
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 28.1 L'identité numérique : multi-couches

Une **identité numérique** est rarement monolithique. Une personne a typiquement :

- Une identité civile (vraie identité, parfois affichée).
- Une ou plusieurs identités professionnelles (LinkedIn, signature email).
- Une ou plusieurs identités semi-privées (Facebook, Instagram avec pseudo).
- Une ou plusieurs identités pseudonymes (X, Reddit, Discord, gaming).
- Éventuellement des identités cachées (forums spécialisés, dark web).

L'investigation OSINT cherche souvent à **relier ces couches** : qui est X sur Reddit ? Qui opère ce compte Twitter pseudonyme ? Cette dé-anonymisation prudente est l'un des défis méthodologiques majeurs.

## 28.2 Pourquoi les couches existent

**Compartimentation légitime.** Un professionnel veut séparer pro / perso. Un militant peut craindre des représailles. Un journaliste protège ses sources.

**Évolution de l'usage.** Un compte pseudo créé pour un usage spécifique en 2015 a accumulé une histoire qui rend le rebranding coûteux.

**Compartimentation problématique.** Fraude, harcèlement, désinformation peuvent exploiter le pseudonymat.

L'analyste OSINT respecte le pseudonymat **sauf** quand l'investigation justifie sa percée — typiquement pour fraude, atteinte aux personnes, criminalité.

## 28.3 Méthodologie de dé-anonymisation prudente

La dé-anonymisation se conduit avec rigueur méthodologique et éthique.

**Étape 1 — Justification.** Pourquoi dé-anonymiser ? Quelle est la base légitime et proportionnée ? La justification est documentée dans le SOR.

**Étape 2 — Sélecteurs cross-plateformes.** Username, photo de profil, style d'écriture, fuseau horaire, sujets, cercles sociaux.

**Étape 3 — Faisceau d'indices.** Aucun sélecteur isolé ne suffit. Le faisceau converge.

**Étape 4 — Vérification.** Avant de conclure, vérifier par sources indépendantes.

**Étape 5 — Cotation prudente.** « Hypothèse forte » ≠ « identification certaine ».

**Étape 6 — Diffusion contrôlée.** Une dé-anonymisation reste dans le périmètre du mandat, jamais publique.

## 28.4 Username reuse comme signal

Un username identique cross-plateformes est un signal fort.

**Vérifications.**

- Photo de profil identique ?
- Bio cohérente ?
- Date de création comparable ?
- Activité corrélée (mêmes sujets, mêmes heures) ?
- Liens entre comptes (cross-promotion) ?

Plus de signaux convergents = hypothèse plus forte.

## 28.5 Photo de profil comme signal

**Méthode.**

- Capturer la photo originale.
- Recherche inversée (Yandex, Google Lens) pour autres apparitions.
- Comparaison croisée avec autres comptes.

**Limites.**

- Photo générique (paysage, célébrité) = signal faible.
- Photo générée IA = potentiellement réutilisable mais détectable.
- Vol d'image (photo de tiers utilisée) = faux positif possible.

## 28.6 Style d'écriture (stylométrie légère)

Le **style d'écriture** est un signal sous-utilisé en OSINT.

**Indicateurs stylométriques.**

- Vocabulaire récurrent (mots-fétiches).
- Fautes typiques (frappes, orthographe, ponctuation).
- Tournures de phrase.
- Émojis utilisés.
- Longueur moyenne des messages.
- Capitalisation, espaces.

**Outils.**

- **JStylo** (open source, académique).
- Analyses manuelles fines pour corpus limité.
- LLMs assistants (avec validation) pour comparaison de styles.

**Cas d'usage.** Comparer le style d'un compte pseudonyme suspect avec le style identifié de la cible (emails, posts publics).

**Limites en 2026.** Les LLMs permettent de masquer ou imiter un style. La stylométrie reste utile mais affaiblie.

## 28.7 Fuseau horaire et cadence

**Signaux temporels.**

- Heures d'activité (post matinaux vs nocturnes).
- Jours de la semaine actifs vs inactifs.
- Vacances corrélées (silence à des dates précises).
- Décalage horaire perceptible.

**Méthode.** Compiler les timestamps de posts publics sur 4-8 semaines. Visualiser en heatmap. Comparer avec timezone supposé de la cible.

**Outil simple.** Pandas + matplotlib en notebook Jupyter.

## 28.8 Sujets et cercles sociaux

**Sujets.** Les centres d'intérêt récurrents (industrie de niche, géographie spécifique, événements précis) sont discriminants.

**Cercles sociaux.** Les comptes suivis, suivants, mentionnés régulièrement forment un graphe social. Deux comptes pseudonymes avec un cercle social très similaire suggèrent un même opérateur ou un même milieu.

**Méthode.**

- Extraire les top 50 mentions/interactions du compte pseudonyme.
- Comparer avec le cercle connu de la cible.
- Recoupements significatifs = signal fort.

## 28.9 Erreurs OPSEC de la cible

La dé-anonymisation réussit souvent grâce à des **erreurs OPSEC** de la cible elle-même.

**Erreurs classiques.**

- Tweet posté depuis le mauvais compte (compte pseudo vs compte officiel).
- Réutilisation d'un username dérivable du vrai nom.
- Photo de profil identique sur compte pseudo et compte civil.
- Email pseudo lié au téléphone civil.
- Géolocalisation activée dans EXIF d'une photo.
- Cross-promotion involontaire (mention d'un compte pseudo dans un post officiel).
- Confirmation par un proche (un parent qui tagge le compte pseudo).

Une investigation patiente expose souvent ces erreurs accumulées.

## 28.10 Corrélations faibles vs fortes

| Type de corrélation | Force |
|---|---|
| Username identique | Forte |
| Photo profil identique | Très forte |
| Erreur OPSEC explicite (tweet depuis mauvais compte) | Quasi-certitude |
| Style d'écriture cohérent | Moyenne |
| Fuseau horaire cohérent | Faible (large population) |
| Sujets cohérents | Faible à moyenne |
| Cercle social recouvrant | Moyenne à forte |
| Mention par un tiers connu | Forte |

Une dé-anonymisation crédible repose sur **plusieurs corrélations** convergentes, idéalement de force variable mais incluant au moins une forte.

> **MIRAGE — Épisode 5 : Identité numérique et pseudonymes**
>
> L'analyste cherche à confirmer si l'username `mdelaunay76` détecté sur Twitter/Instagram/GitHub correspond bien à Marc Delaunay personne civile.
>
> Vérifications cross-comptes :
> - **Twitter @mdelaunay76** : compte verrouillé, créé en 2010. Photo profil : silhouette en costume sombre devant un fond uni. Description : « Finance & Tech enthusiast | Paris ». 87 followers, 312 following.
> - **Instagram mdelaunay76** : compte privé, photo de profil identique (silhouette costume). Bio : « 🌍 Voyages 🏠 Provence ».
> - **GitHub mdelaunay** : compte inactif depuis 2019, deux dépôts personnels (configurations Linux, scripts), email visible dans les commits : `marc.delaunay76@gmail.com`.
>
> Le **GitHub est l'élément déterminant** : les commits sont signés `marc.delaunay76@gmail.com`. Cross-vérification : cet email est-il bien personnel de Delaunay ?
>
> Holehe sur `marc.delaunay76@gmail.com` : présence détectée sur Twitter, Instagram, Pinterest, Spotify, Adobe, Apple. Cohérent avec un email personnel actif. GHunt sur cet email : compte Google actif, photo profil Google identique à celle des autres comptes (silhouette).
>
> Cross-recherche : `marc.delaunay76@gmail.com` apparaît également dans le WHOIS historique (DomainTools) du domaine `delaunay-patrimoine.fr` enregistré en 2017 (depuis abandonné). Ce domaine était une vitrine de conseil patrimonial personnel — cohérent avec un DAF qui aurait, en parallèle de son emploi, une activité personnelle accessoire.
>
> **Conclusion partielle (avec cotation prudente).** L'email `marc.delaunay76@gmail.com` est très probablement l'email personnel de Marc Delaunay (cotation B2 : faisceau d'indices convergents : GitHub + Holehe + WHOIS + cohérence des photos profil et bios).
>
> Implications : ce sélecteur ouvre de nouveaux pivots. Recherche HIBP / DeHashed sur cet email pour identifier exposition dans des stealer logs. Recherche WHOIS et certificats TLS sur tous les domaines potentiellement enregistrés. Ces pistes seront explorées dans MIRAGE 9 et MIRAGE 10.

-----
