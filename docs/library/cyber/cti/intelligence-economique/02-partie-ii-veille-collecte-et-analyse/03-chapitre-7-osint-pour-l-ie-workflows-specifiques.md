---
title: 'Chapitre 7 — OSINT pour l''IE : workflows spécifiques'
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Intelligence économique.md
note: Intelligence économique
up:
- - Intelligence économique
  - ../index.md
- - Partie II — Veille, collecte et analyse
  - index.md
---

*Ce chapitre ne redouble pas le cours OSINT Mastery — il enseigne les workflows OSINT spécifiques à l'IE que le cours OSINT général ne couvre pas. Pour les techniques OSINT générales (Google Dorking, SOCMINT, GEOINT, investigation technique), voir le cours OSINT de la bibliothèque.*

## 7.1 La veille brevets comme outil de renseignement concurrentiel

Les brevets sont la source OSINT la plus sous-estimée en IE — et pourtant la plus riche. Un brevet publié révèle l'orientation R&D du déposant (dans quelle direction innove-t-il ?), ses marchés cibles (dans quels pays dépose-t-il ?), ses partenariats (co-déposants ?), sa capacité d'innovation (fréquence de dépôt, domaines couverts), et ses vulnérabilités (ce qui n'est PAS breveté est protégé par le secret ou n'existe pas).

Les bases de brevets : **Espacenet** (OEB — européen, gratuit, couverture mondiale), **USPTO** (américain, gratuit), **WIPO** (international, gratuit — recherche PCT), **Google Patents** (interface simplifiée, traduction automatique). L'analyse : surveiller les dépôts d'un concurrent sur une période (tendance — accélération des dépôts dans un domaine = programme en cours), analyser les revendications (claims) pour détecter un chevauchement avec ses propres brevets, identifier les co-déposants (partenaires cachés), et cartographier les citations (qui cite qui — réseau de relations technologiques).

## 7.2 L'analyse des recrutements comme signal stratégique

Les offres d'emploi révèlent les projets futurs d'une organisation. Un concurrent qui recrute 15 ingénieurs en composites haute température prépare un programme dans ce domaine — le signal est public et gratuit (LinkedIn, sites d'emploi, Glassdoor). L'analyse des recrutements couvre le volume (combien de postes dans un domaine spécifique — un pic de recrutement = un lancement de projet), les profils (quelles compétences spécifiques — indiquent la direction technique du projet), les localisations (un nouveau site = une expansion géographique), et les départs (les démissions et les mouvements vers les concurrents — LinkedIn est une mine d'or).

Le piège : LinkedIn est aussi un terrain d'approche pour l'adversaire. Les « connexions spontanées » de profils étrangers travaillant dans des secteurs sensibles peuvent être des démarches de renseignement (le MSS chinois utilise LinkedIn de manière documentée pour approcher des cibles). L'HUMINT défensif (Ch.8) traite ce risque.

## 7.3 La cartographie capitalistique

L'investigation des structures de propriété est une compétence IE fondamentale — elle répond à la question « qui possède réellement quoi ? ». Les bases : **Orbis** (Bureau van Dijk/Moody's — la base la plus complète pour les liens capitalistiques internationaux, payante), **Diane/Ellisphere** (France), **Infogreffe/BODACC** (France — comptes, statuts, décisions, gratuit en partie), **Companies House** (UK — gratuit), **SEC/EDGAR** (US — filings, gratuit), et les registres nationaux des pays cibles.

La méthode : remonter la chaîne de participation (qui détient la société X ? → la société Y → le fonds Z → les UBO — Ultimate Beneficial Owners). Détecter les structures écrans (sociétés interposées dans des juridictions opaques — BVI, Caïmans, Guernesey, Luxembourg). Croiser avec les listes de sanctions (OFAC SDN, listes UE, gel des avoirs français). Et cartographier les liens entre les dirigeants (les mêmes personnes apparaissent-elles dans plusieurs structures liées ?).

## 7.4 Fil rouge — SENTINELLE : l'investigation OSINT

> **📋 SENTINELLE — Épisode 4**
>
> Camille lance 3 investigations OSINT en parallèle.
>
> **Brevets :** analyse des dépôts récents de GlobalComposites sur Espacenet et USPTO. Résultat : GlobalComposites a déposé 8 brevets en 18 mois dans le domaine des composites haute température — un pic par rapport à sa moyenne historique (2-3/an). Le brevet litigieux (US Patent Application 2026/0xxxxx) a des revendications qui chevauchent partiellement le brevet NovaTech FR3xxxxxx. Le timing (6 mois après le salon) et la spécificité technique sont suspects. Camille mandate un conseil en PI pour une analyse d'antériorité formelle.
>
> **Recrutements :** analyse LinkedIn de GlobalComposites. Résultat : recrutement de 12 ingénieurs spécialisés en résines haute température et en procédés de fabrication composites dans les 12 derniers mois — dont 3 issus de concurrents européens. Un programme de développement est clairement en cours.
>
> **Capitalistique :** investigation sur Meridian Capital Partners via Orbis et les registres singapouriens. Résultat : Meridian est une société créée il y a 3 ans, avec un capital modeste (10 M SGD) et un unique dirigeant (un financier singapourien). La chaîne de participation remonte via une holding à Hong Kong (Dragon Gate Investments Ltd) vers un conglomérat dont l'actionnaire de référence est... un fonds lié à AVIC (Aviation Industry Corporation of China). Le même AVIC dont une filiale mandate les chasseurs de tête qui approchent les ingénieurs NovaTech. **La connexion est établie.**

---
