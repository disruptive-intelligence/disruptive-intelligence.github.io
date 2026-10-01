---
title: Chapitre 4 — Cadre juridique, éthique et posture de travail
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - 'Partie I — Fondations : penser en écosystème'
  - index.md
---

## 4.1 Ce que l'analyste a le droit de faire — et ce qu'il n'a pas le droit de faire

Le cadre juridique de l'investigation CTI en France (et plus largement en Europe) est souvent mal compris par les praticiens, ce qui conduit soit à une paralysie excessive (« on ne peut rien faire sans mandat ») soit à des prises de risque inconsidérées (« c'est de l'OSINT, donc c'est légal »).

Les **activités légales sans restriction** pour un analyste CTI d'entreprise incluent la consultation de sources ouvertes indexées par les moteurs de recherche, la consultation de registres publics (WHOIS historique, registres d'entreprises, cadastre, brevets), l'analyse de données techniques partagées par la communauté CTI (rapports, IoC, samples soumis à des sandboxes publiques), l'analyse de la blockchain publique (Bitcoin, Ethereum — les transactions sont par design publiques et pseudonymisées), la consultation de bases de données de breaches accessibles via des services légaux (DeHashed, Have I Been Pwned, IntelX — la légalité de la consultation est établie, l'exploitation opérationnelle des données personnelles est encadrée par le RGPD), et l'observation passive du dark web (consulter un forum sans interaction).

Les **activités encadrées nécessitant une attention particulière** incluent l'exploitation de données à caractère personnel issues de breaches (autorisée dans le cadre de la réponse à incident de l'entreprise, mais les données doivent être traitées conformément au RGPD : finalité légitime, proportionnalité, durée de conservation limitée, information du DPO), la collecte de données depuis des canaux Telegram ou Discord (la consultation est légale, mais la collecte automatisée massive peut poser des questions sous l'angle du RGPD et de la loi Informatique et Libertés), et la communication d'IoC ou de résultats d'investigation aux forces de l'ordre ou à l'ANSSI (non seulement légale mais encouragée — l'article L.2321-1 du Code de la défense donne à l'ANSSI un rôle de coordination).

Les **activités illégales** incluent toute interaction active avec des acteurs criminels (même sous une fausse identité, sans cadre judiciaire, cela constitue potentiellement une provocation ou une complicité), toute intrusion dans un système informatique tiers, même celui d'un attaquant (le « hack back » est illégal en France — article 323-1 du Code pénal), l'achat de services criminels (même « pour tester » — acheter un accès sur un forum pour vérifier sa validité est une infraction), et l'utilisation de logiciels d'interception de communications (hors cadre judiciaire ou autorisation légale spécifique).

> **Alerte :** La frontière entre observation passive et interaction active est parfois floue. Créer un compte sur un forum pour lire des messages est généralement considéré comme de l'observation passive. Poster un message, même anodin, pour établir une couverture est une interaction active qui sort du cadre légal de l'analyste privé.

## 4.2 Responsabilité analytique

Une cartographie d'écosystème qui nomme des personnes ou des organisations crée un risque juridique et éthique que l'analyste doit anticiper.

Nommer un acteur comme « membre d'un écosystème criminel » dans un rapport interne ou partagé avec des partenaires, sans un niveau de preuve suffisant, est potentiellement diffamatoire (article 29 de la loi du 29 juillet 1881). Même dans un contexte de réponse à incident, l'analyste doit distinguer rigoureusement entre ce qui est établi (le pseudo kr0n0s_ops est actif sur le forum X et revendique Y), ce qui est probable (les indices convergents suggèrent que kr0n0s_ops et le compte GitHub Z sont contrôlés par la même personne), et ce qui est hypothétique (il est possible que cette personne opère depuis la Russie sur la base du fuseau horaire d'activité).

Le rapport d'analyse doit toujours expliciter ses niveaux de confiance (voir Ch.13) et ne jamais présenter une hypothèse comme un fait. Cette discipline n'est pas seulement une précaution juridique — c'est une exigence de qualité analytique. Un rapport qui mélange faits et hypothèses sans les distinguer est un mauvais rapport, indépendamment des conséquences juridiques.

## 4.3 Neutralité et rigueur

L'analyste CTI n'est pas un enquêteur judiciaire (il ne prouve pas la culpabilité), il n'est pas un journaliste (il ne publie pas), et il n'est pas un militant (il ne dénonce pas). Il produit du renseignement analytique destiné à informer une décision.

Sa valeur repose sur sa rigueur et sa prudence, pas sur le caractère spectaculaire de ses conclusions. Un rapport qui dit « nous avons identifié un écosystème de 12 acteurs avec un niveau de confiance modéré, et nous recommandons 3 investigations complémentaires pour renforcer l'attribution » est plus utile qu'un rapport qui dit « le groupe X, probablement sponsorisé par l'État Y, nous a ciblé dans le cadre de la stratégie Z » — si le second ne repose pas sur un faisceau d'indices suffisant.

La neutralité implique aussi de ne pas surinterpréter dans le sens qui plairait au commanditaire. Si la direction espère que l'attaque est « étatique » (parce que cela renforce le discours politique), l'analyste ne doit pas forcer les conclusions dans cette direction. Si les données pointent vers un affilié opportuniste, c'est cette conclusion qu'il faut présenter, avec les nuances nécessaires.

## 4.4 Conservation des sources et traçabilité du raisonnement

Chaque connexion dans la cartographie doit être traçable : quelle source, quelle date de consultation, quel outil utilisé, quel niveau de confiance attribué, et quel raisonnement a conduit à l'établissement du lien.

Un graphe non sourcé est un graphe inexploitable. Si un collègue reprend l'analyse six mois plus tard, ou si le rapport est transmis aux forces de l'ordre, ou si une décision stratégique est prise sur la base de la cartographie, il faut pouvoir remonter à l'origine de chaque assertion.

En pratique, cela signifie maintenir un journal de collecte (un document chronologique qui enregistre chaque recherche, chaque requête, chaque résultat, chaque décision analytique) et annoter chaque nœud et chaque lien du graphe avec ses métadonnées de source. Les outils comme Obsidian (notes liées) et Maltego (métadonnées sur les entités) permettent cette traçabilité. Le workflow opérationnel est détaillé au Ch.25.

## 4.5 Fil rouge — NEXUS : cadrage de l'investigation

> **🔍 NEXUS — Épisode 4**
>
> Samira cadre formellement l'investigation avant de plonger plus loin.
>
> **Cadre juridique :** L'investigation s'inscrit dans la réponse à incident de l'entreprise. Énergis est victime d'une tentative d'attaque par ransomware. L'analyste CTI est légitime à mener des recherches en source ouverte pour comprendre la menace, informer la direction, et préparer le dépôt de plainte.
>
> **Limites :** Samira peut consulter les forums (sans interagir), analyser la blockchain publique, interroger les bases de données CTI et OSINT. Elle ne peut pas créer de faux profils, interagir avec les acteurs, ni tenter d'accéder aux systèmes des attaquants. Pour les données nécessitant des réquisitions (identité derrière un compte Telegram, titulaire d'un compte crypto sur un exchange KYC, logs de connexion de l'hébergeur), il faudra articuler avec les forces de l'ordre après le dépôt de plainte.
>
> **DPO :** Samira informe le DPO d'Énergis que l'investigation CTI impliquera le traitement de données personnelles (pseudos, emails, éventuellement identités réelles si identifiées). Le traitement est légitime au titre de l'intérêt vital de l'entreprise (article 6.1.f du RGPD), avec conservation limitée à la durée de l'investigation et de la procédure judiciaire.

---
