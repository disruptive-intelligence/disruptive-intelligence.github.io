---
title: Chapitre 13 — Niveaux de confiance et formulation analytique
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie III — Liens, corrélations ET rigueur analytique
  - index.md
---

## 13.1 Hypothèses concurrentes et ACH

L'Analysis of Competing Hypotheses (ACH) est une méthode structurée développée par Richards Heuer pour la CIA, conçue pour contrer le biais de confirmation. Le principe est de formuler plusieurs hypothèses mutuellement exclusives, puis de tester systématiquement chaque donnée disponible contre toutes les hypothèses — pas seulement contre l'hypothèse préférée.

Dans le contexte de la cartographie d'écosystèmes, les hypothèses concurrentes portent typiquement sur l'attribution (qui est derrière l'attaque ?), la motivation (pourquoi cette cible ?), et la structure (quel est le lien entre les acteurs ?).

L'ACH fonctionne en 5 étapes. Premièrement, lister toutes les hypothèses raisonnables (pas seulement les deux ou trois les plus évidentes). Deuxièmement, lister toutes les données disponibles (les « évidences »). Troisièmement, pour chaque évidence, évaluer sa compatibilité avec chaque hypothèse (compatible, incompatible, ou non discriminante). Quatrièmement, identifier l'hypothèse la plus consistante (celle qui n'a pas d'évidences incompatibles). Cinquièmement, évaluer la sensibilité (le résultat changerait-il si une donnée clé s'avérait erronée ?).

## 13.2 Grille de cotation

fiabilité de la source × fiabilité de l'information

Le système standard de cotation du renseignement (utilisé par les services de renseignement, l'OTAN, et adopté par la communauté CTI) évalue chaque information sur deux axes indépendants.

**Fiabilité de la source (A à F) :**

- **A** — Source dont la fiabilité ne fait pas de doute (registre officiel, blockchain publique, document judiciaire)
- **B** — Source généralement fiable (rapport CTI d'un éditeur reconnu, base de données commerciale de référence)
- **C** — Source assez fiable (rapport d'un chercheur indépendant, information recoupée partiellement)
- **D** — Source pas toujours fiable (message sur un forum underground, témoignage d'un acteur anonyme)
- **E** — Source peu fiable (rumeur, information non sourcée, source à motivation douteuse)
- **F** — Fiabilité non évaluable (source inconnue ou première utilisation)

**Fiabilité de l'information (1 à 6) :**

- **1** — Confirmée par d'autres sources indépendantes
- **2** — Probablement vraie (cohérente avec d'autres informations, logique)
- **3** — Peut-être vraie (pas de contradiction mais pas de confirmation)
- **4** — Douteuse (informations contradictoires)
- **5** — Improbable (contredit par la majorité des autres sources)
- **6** — Véracité non évaluable

Chaque fait dans l'analyse est coté. Un enregistrement WHOIS = A1. Un message sur un forum underground = D3. Un rapport CTI d'un éditeur reconnu = B2. Un article de blog anonyme = E4.

## 13.3 Formulation prudente

Le vocabulaire de l'analyste reflète sa rigueur. Les formulations appropriées incluent « les données suggèrent que... » (confiance modérée), « il est probable que... » (confiance élevée mais pas certitude), « selon notre hypothèse principale... » (hypothèse explicitement identifiée), et « nous n'avons pas pu établir si... » (angle mort explicite).

Les formulations à proscrire incluent « kr0n0s_ops est le cybercriminel X » (affirmation d'identité sans nuance), « le groupe Y a attaqué Z » (attribution catégorique), « les preuves montrent que... » (l'analyste CTI ne produit pas des preuves au sens judiciaire), et « il est certain que... » (la certitude n'existe pas en analyse de renseignement).

La bonne formulation est : « Les indices convergents (pseudo commun, clé PGP partagée, profil linguistique cohérent, fuseau horaire compatible) suggèrent avec un niveau de confiance élevé (B2) que les comptes kr0n0s_ops sur XSS, GitHub, et Telegram sont contrôlés par la même entité. L'identité réelle de cette entité n'a pas pu être établie dans le cadre de cette investigation. »

## 13.4 Ce que l'on sait, ce que l'on estime, ce que l'on suppose, ce que l'on ne sait pas

Le rapport d'analyse doit distinguer explicitement quatre catégories de connaissances.

**Ce que l'on sait** (faits établis, cotés A1-B2) : les domaines, les IP, les hash de malware, les transactions blockchain, les messages observés sur les forums. Ce sont des données vérifiables.

**Ce que l'on estime** (conclusions analytiques, basées sur la convergence d'indices, cotées B2-C3) : l'attribution des comptes à un même acteur, l'identification des rôles dans l'écosystème, la reconstitution de la chaîne d'attaque. Ce sont des interprétations documentées.

**Ce que l'on suppose** (hypothèses non confirmées, cotées C3-D4) : la motivation de l'attaque (purement financière vs para-étatique), la localisation géographique de l'acteur, les liens avec des entités étatiques. Ce sont des pistes exploratoires.

**Ce que l'on ne sait pas** (angles morts explicites) : l'identité réelle de l'acteur, le périmètre exact de l'exfiltration, l'existence d'autres affiliés ciblant la même entreprise, la structure interne de l'opérateur RaaS. Documenter les angles morts est aussi important que documenter les résultats.

## 13.5 Fil rouge — NEXUS : conclusions intermédiaires formalisées

> **🔍 NEXUS — Épisode 13**
>
> Samira formalise les conclusions intermédiaires de l'investigation selon le cadre ACH.
>
> **Hypothèses concurrentes :**
> - **H1** — kr0n0s_ops est un affilié RaaS purement criminel qui a ciblé Énergis par opportunisme (l'accès était disponible, le prix attractif, le secteur énergie paie souvent).
> - **H2** — kr0n0s_ops est un affilié instrumentalisé par un acteur para-étatique (il a été orienté vers cette cible spécifique, consciemment ou non, pour servir des intérêts géopolitiques).
> - **H3** — kr0n0s_ops est un proxy direct d'un service de renseignement utilisant le modèle RaaS comme couverture.
>
> **Évidences discriminantes :**
> - Le ciblage OT/énergie : compatible avec H1 (certains affiliés se spécialisent dans l'industrie), H2, et H3. Non discriminant.
> - Le timing géopolitique : compatible avec H2 et H3, faiblement compatible avec H1 (coïncidence possible). Faiblement discriminant.
> - La coordination médiatique (blog de façade) : peu compatible avec H1 (inhabituel pour un affilié opportuniste), compatible avec H2 et H3. Modérément discriminant.
> - Le flux financier vers le wallet para-étatique : compatible avec H2 et H3, peu compatible avec H1. Mais le lien est indirect (via mixer) et à confiance faible (D3). Faiblement discriminant en l'état.
>
> **Conclusion intermédiaire :** H1 reste l'hypothèse la plus parcimonieuse (elle nécessite le moins d'hypothèses supplémentaires). H2 est plausible mais manque de données discriminantes. H3 est peu soutenue en l'état (aucune preuve de commandement étatique direct). Recommandation : poursuivre l'investigation, notamment sur le flux financier et sur le profil de ghost_access (l'IAB qui a vendu l'accès — a-t-il ciblé spécifiquement Énergis, ou vendait-il tous les accès énergie à qui voulait bien les acheter ?).

---
