---
title: 'Chapitre 29 — Dé-anonymisation : méthodes et limites'
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VI — ANALYSE, renseignement et production
  - index.md
---

La **dé-anonymisation** — associer un pseudonyme dark web à une identité réelle — est l'un des Graal de l'investigation. Elle est possible, mais rarement facile. Ce chapitre cartographie les méthodes, leurs limites, et les principes de calibration.

## 29.1 Les grandes catégories d'attaque

**Attaques cryptographiques contre Tor**. En pratique, très rares en investigation. Les attaques théoriques contre le réseau Tor (analyse de trafic globale, compromission massive de relais) nécessitent des capacités d'État et restent pour l'essentiel classifiées. Pour l'analyste CTI privé, cette voie est fermée.

**Erreurs d'OPSEC**. Voie principale d'attribution historique. Un acteur qui réutilise un pseudo entre monde réel et dark web, qui révèle des détails personnels, qui laisse des métadonnées dans ses fichiers — s'auto-dé-anonymise. C'est ainsi qu'Ulbricht et Cazes ont été identifiés. Majoritaire parmi les cas de dé-anonymisation documentés publiquement.

**Corrélation OSINT**. Reconstruction progressive d'une identité par agrégation. Un pseudo sur forum → un email jetable → un profil réutilisé → un repo GitHub → un profil LinkedIn. Chaque étape réduit l'espace des candidats jusqu'à identification.

**Attaques applicatives**. Exploitation de failles d'un service .onion ou de comportements du navigateur de la cible pour faire leaker l'IP réelle. Les **NIT** (Network Investigative Techniques) policières — Ch.30 — en sont l'incarnation.

**Attaques financières**. Traçage blockchain qui remonte jusqu'à un off-ramp KYC. Ch.31.

**Attaques humaines**. Infiltration, informateurs, coopération sous pression de pairs arrêtés. Réservé aux forces de l'ordre mais structurant dans les grandes opérations (Operation Bayonet, Cronos).

## 29.2 Les signaux d'auto-dé-anonymisation

Les acteurs se trahissent souvent par patterns observables. Les plus fréquents :

**Réutilisation de pseudonymes**. Un acteur utilise le même pseudo ou une variation proche entre dark web et clearnet. Le pseudo apparaît sur GitHub, forums publics, réseaux sociaux, jeux en ligne. Chaque occurrence ajoute des données.

**Métadonnées dans fichiers publiés**. Documents PDF/DOCX avec champ « auteur » renseigné du nom réel. Photos avec données EXIF (GPS, appareil photo, horodatage). Captures d'écran contenant éléments identifiants (notifications, onglets, thème OS personnel).

**Fuseau horaire révélé**. Patterns d'activité cohérents avec un fuseau unique. Un acteur prétendument « américain » actif exclusivement entre 10h et 22h MSK est probablement russophone.

**Langue maternelle révélée**. Tournures, fautes, idiomes trahissent la langue native. Analyse stylométrique automatisée peut corréler multiples pseudos.

**Détails personnels involontaires**. Mentions de villes, d'événements locaux, de traditions culturelles, de sports préférés — chaque détail contraint l'espace d'identification.

**Infrastructure partagée**. Même adresse email jetable pour multiple comptes. Même serveur XMPP. Même registrar/hébergeur pour projets publics et projets clandestins.

**PGP keys stables**. Une clé PGP peut persister sur des années et traverser plusieurs pseudos. Elle est un identifiant cryptographique fort.

**Photos personnelles leaked**. Par vanité, opportunisme, ou sexting, certains acteurs partagent des photos d'eux-mêmes. Reverse image search peut identifier.

**Comptes bancaires / crypto liés au vrai nom**. Les échanges KYC ou les cartes bancaires utilisées pour payer infrastructure exposent l'identité.

## 29.3 La stylométrie

L'**analyse stylométrique** est l'étude des patterns stylistiques d'un auteur. Appliquée au dark web, elle permet :

- De corréler plusieurs pseudos comme appartenant au même auteur.
- Parfois d'orienter vers une région linguistique (locuteur natif russe ? arabophone ?).
- Exceptionnellement d'associer un texte dark web à un auteur connu (publications académiques, articles, posts publics).

**Techniques** :

- **Analyse de fréquence lexicale** : mots caractéristiques, vocabulaire.
- **Patterns syntaxiques** : structures de phrase, ponctuation, usage majuscules.
- **Fautes récurrentes** : erreurs grammaticales systématiques révélant langue maternelle.
- **Idiomes et expressions** : tournures idiomatiques spécifiques.
- **Métriques informatiques** : n-grams de caractères, distribution de longueur de phrase, type-token ratio.

**Outils** :

- **Signature** (logiciel académique).
- **JGAAP** (Java Graphical Authorship Attribution Program).
- **Stylo** (R package).
- Solutions commerciales dédiées pour grandes entreprises.

**Limites** :

- **Besoin d'un corpus suffisant** : quelques centaines de mots minimum par pseudo, idéalement plusieurs milliers.
- **Fragilité face à modification intentionnelle** : un acteur conscient peut altérer son style.
- **Biais des outils** : beaucoup entraînés sur littérature anglophone, moins fiables sur langues peu documentées.
- **Conclusions probabilistes** : stylométrie fournit un scoring de similarité, jamais une identification certaine.

## 29.4 L'attribution technique versus attribution personnelle

Distinction fondamentale :

**Attribution technique** : associer un ensemble d'activités à un même acteur (ou cluster d'acteurs coordonnés), sans identifier son identité civile. On sait que « aero_source », « aerosrc », « aero_src » sont probablement un même individu, sans savoir qui il est dans la vie réelle. Utile pour le suivi, la priorisation, la threat intelligence.

**Attribution personnelle** : identifier l'identité civile de l'acteur (nom, localisation, état civil). Beaucoup plus difficile, réservé aux cas aboutis. Nécessaire pour action coercitive (arrestation, poursuite).

Pour l'analyste CTI privé, **l'attribution technique est presque toujours l'objectif réaliste**. L'attribution personnelle relève des forces de l'ordre et des services de renseignement. Le rôle du privé est de fournir la matière à l'attribution personnelle, pas de la produire directement.

## 29.5 Niveaux de confiance en dé-anonymisation

Comme pour l'attribution APT, utiliser vocabulaire calibré.

**Certain** : preuve directe. Acte ou fichier signé du nom réel de l'acteur, photo claire identifiable, données KYC extraites d'exchange. Rare en investigation privée.

**Très probable** (80-95%) : convergence forte de multiples indicateurs indépendants. Exemple : PGP key + wallet crypto + analyse linguistique + localisation d'activité + photo partielle + pattern temporel — tous cohérents avec un individu spécifique.

**Probable** (55-80%) : convergence d'indicateurs, mais incomplète ou faiblement contraignante. Ex : stylométrie + fuseau horaire + pseudonyme similaire. Plusieurs candidats plausibles.

**Possible** (20-55%) : indicateurs suggestifs mais pas probants. Poursuite d'investigation nécessaire.

**Spéculatif** : hypothèse sans support fort. Utile pour orienter la recherche mais pas pour conclure.

**Indéterminable** : données insuffisantes pour même formuler une hypothèse crédible.

## 29.6 Fil rouge — DARKSTREAM

attribution technique confirmée, personnelle partielle

> **🌐 DARKSTREAM — Épisode 17 : état de l'attribution**
>
> Synthèse attribution DARKSTREAM au moment du rapport final :
>
> **Attribution technique** — Très probable (confidence ~90%) :
> - aero_source (IndustrialLeaks), aerosrc (XSS), aero_src (Exploit.in) = même individu, fondé sur identité PGP, analyse linguistique, chevauchement crypto.
> - Cet acteur est actif depuis ~2 ans sur l'écosystème russophone, profil courtier/IAB intermédiaire.
> - Pas de lien structurel avec APT étatique identifié. Profil purement cybercriminel à motivation financière.
>
> **Attribution personnelle** — Possible (~30%), partielle :
> - Russophone quasi-certain (linguistique + fuseau horaire + infrastructure + wallet).
> - Localisation probable : Russie européenne ou Bélarus (fuseau + inactivité lors de jours fériés russes).
> - Âge estimé : 25-40 ans (maturité de discours + durée sur l'écosystème).
> - Genre non déterminé (pas de signaux sûrs).
> - **Pas de nom civil identifiable** par l'investigation privée. Les indicateurs convergents pointent vers un profil, pas un individu.
>
> **Communication à la DGSI** : la DGSI reçoit le dossier technique complet. Elle dispose de capacités additionnelles (coopération SIGINT, échanges avec services partenaires russes dans le cadre Europol/Interpol, requêtes légales sur exchanges crypto concernant les wallets identifiés). Ces capacités peuvent permettre de pousser plus loin l'attribution personnelle, mais Athéna n'en sera pas informée.
>
> **Pour Vectris** : l'attribution technique suffit pour l'action défensive (monitoring, durcissement, communication). L'attribution personnelle, même si elle advenait, ne changerait pas immédiatement les actions. Elle pourrait servir ultérieurement pour d'éventuelles poursuites civiles internationales (procédure longue et coûteuse, rarement aboutissable contre un acteur russe dans le contexte géopolitique 2025-2026).

---
