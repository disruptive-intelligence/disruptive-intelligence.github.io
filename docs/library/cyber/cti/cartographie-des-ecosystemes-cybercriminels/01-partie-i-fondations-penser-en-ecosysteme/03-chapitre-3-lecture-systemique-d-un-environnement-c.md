---
title: Chapitre 3 — Lecture systémique d'un environnement clandestin
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - 'Partie I — Fondations : penser en écosystème'
  - index.md
---

## 3.1 Penser en graphe, pas en silos

L'erreur la plus courante de l'analyste débutant est de traiter chaque indice isolément. Un domaine C2, pris seul, est un indicateur de compromission (IoC) — utile pour la détection, mais pauvre en renseignement. Un pseudo vu sur un forum, pris seul, est un identifiant — utile pour le suivi, mais pauvre en contexte. Un wallet Bitcoin, pris seul, est une adresse — utile pour le traçage, mais pauvre en attribution.

La valeur analytique apparaît quand on relie ces éléments. Quand le domaine C2 pointe vers une IP hébergée chez un fournisseur connu pour son bulletproof hosting, que cette même IP héberge un blog anonyme qui relaie des revendications de ransomware, que le certificat SSL du domaine est un wildcard partagé avec trois autres domaines associés à des campagnes précédentes, que l'enregistrement WHOIS historique du domaine révèle un email ProtonMail, que cet email a été compromis dans un breach et est associé à un pseudo actif sur un forum underground, que ce pseudo a recommandé un service de mixing sur un canal Telegram — alors un écosystème commence à apparaître.

Penser en graphe signifie que chaque nouvel indice n'est pas évalué pour ce qu'il « est » mais pour ce qu'il « relie ». L'analyste ne collecte pas des données — il construit des connexions. Chaque entité est un nœud dans un graphe, et chaque connexion identifiée est une arête qui enrichit la compréhension de l'ensemble.

## 3.2 Nœuds, liens, flux et dépendances

Le vocabulaire de base de l'analyse de réseau, emprunté à la théorie des graphes et à l'analyse de réseau social (Social Network Analysis, SNA), doit être maîtrisé par l'analyste.

Un **nœud** (ou sommet) est une entité dans le graphe. Les nœuds peuvent être des personnes (identifiées ou pseudonymisées), des organisations (groupes, sociétés écrans, forums), des objets techniques (domaines, IP, serveurs, malware, certificats), des objets financiers (wallets, comptes bancaires, sociétés), ou des espaces (forums, canaux Telegram, leak sites). Chaque nœud a des attributs : type, nom, date de découverte, source, niveau de confiance.

Un **lien** (ou arête) est une relation entre deux nœuds. Les liens sont typés (technique, financier, identitaire, social, temporel — détail au Ch.11) et qualifiés (force, direction, confiance). Un lien peut être directionnel (A paie B) ou bidirectionnel (A et B communiquent). La qualification des liens est le cœur de la rigueur analytique — voir Ch.11 et Ch.12.

Un **flux** est un mouvement entre nœuds. Les flux peuvent être financiers (transfert de crypto), informationnels (transmission de données volées, communication d'instructions), ou matériels (livraison d'accès, déploiement de malware). L'analyse des flux révèle la dynamique de l'écosystème : qui fournit quoi à qui, dans quel ordre, à quel volume.

Une **dépendance** est un lien critique dont la rupture affecterait le fonctionnement de l'écosystème. Si un affilié dépend d'un seul IAB pour ses accès initiaux, la relation affilié-IAB est une dépendance. Si un opérateur RaaS dépend d'un seul hébergeur bulletproof pour son infrastructure, cette relation est une dépendance critique. L'identification des dépendances est l'objectif ultime de la cartographie, car elles révèlent les points de fragilité exploitables pour la disruption (Ch.22).

## 3.3 Intermédiaires critiques et points de concentration

Tous les nœuds d'un graphe n'ont pas la même importance structurelle. La théorie des réseaux distingue deux types de nœuds particulièrement significatifs.

Les **hubs** sont des nœuds très connectés — ils ont un grand nombre de liens directs avec d'autres nœuds. Un hébergeur bulletproof qui sert 50 groupes différents est un hub. Un forum avec 10 000 membres actifs est un hub. Les hubs sont importants parce que leur suppression déconnecte beaucoup de nœuds simultanément. Mais ils ne sont pas nécessairement les plus intéressants analytiquement, car leur rôle est souvent passif (ils fournissent un service sans contrôler les opérations).

Les **brokers** (ou intermédiaires de ponts) sont des nœuds qui connectent des communautés qui seraient sinon séparées. Un acteur qui est à la fois actif sur un forum anglophone de carding et sur un forum russophone de ransomware est un broker : il relie deux communautés. Un IAB qui vend des accès à des affiliés de trois plateformes RaaS différentes est un broker : il relie trois écosystèmes. La métrique formelle est la betweenness centrality — le nombre de chemins les plus courts entre paires de nœuds qui passent par un nœud donné.

Les brokers sont souvent les cibles les plus intéressantes pour la disruption, car leur suppression fragmente le réseau en communautés isolées qui ne peuvent plus coopérer.

> **Bonne pratique :** Lors de la construction d'un graphe dans Maltego ou Gephi (voir Ch.5), calculer systématiquement les métriques de centralité (degree, betweenness, closeness) pour identifier les hubs et les brokers. Ne pas se fier à l'impression visuelle seule — un nœud visuellement central dans le layout n'est pas forcément structurellement central.

## 3.4 Fonctions visibles et fonctions cachées

Chaque entité dans un écosystème remplit des fonctions manifestes (visibles, déclarées) et des fonctions latentes (cachées, implicites).

Un forum underground est manifestement une place de marché — les utilisateurs y achètent et vendent des services et des données. Mais un forum remplit aussi des fonctions latentes essentielles. C'est un espace de recrutement (les acteurs compétents se font remarquer par leurs contributions et sont approchés pour des opérations). C'est un filtre de sélection (le système de vouching, les fees d'entrée, et les règles de la communauté filtrent les « amateurs » et les agents infiltrés). C'est un mécanisme de réputation (l'historique des transactions et les ratings sont le « CV » d'un acteur). C'est un espace de gouvernance (les modérateurs arbitrent les litiges, les admins fixent les règles, les sanctions collectives punissent les tricheurs).

L'analyste qui ne voit que la fonction marchande d'un forum sous-estime dramatiquement son importance dans l'écosystème. Supprimer un forum ne supprime pas seulement une place de marché — cela détruit un capital social, un système de réputation, et un mécanisme de confiance qui avaient mis des années à se construire. C'est pourquoi les takedowns de forums ont un impact si profond, même quand les acteurs migrent rapidement vers des alternatives (le capital social ne migre pas automatiquement).

## 3.5 Résilience et adaptation

Un écosystème bien structuré survit à la perte de certains de ses nœuds. Si un forum ferme, l'activité migre vers un autre. Si un affilié est arrêté, un autre prend sa place. Si un service de mixing est saisi, un concurrent émerge. Cette propriété — la capacité du système à maintenir sa fonction malgré la perte de composants — est la résilience.

La résilience d'un écosystème dépend de plusieurs facteurs. La **redondance** : y a-t-il plusieurs nœuds capables de remplir la même fonction ? Si l'écosystème dispose de plusieurs hébergeurs bulletproof alternatifs, il survit à la perte de l'un d'eux. La **substituabilité des acteurs** : les rôles sont-ils suffisamment standardisés pour qu'un acteur puisse être remplacé par un autre ? Dans un modèle RaaS, les affiliés sont hautement substituables. La **décentralisation** : le contrôle et la prise de décision sont-ils distribués ? Un écosystème modulaire sans noyau central est plus résilient qu'un écosystème centralisé. La **rapidité de reconstitution** : combien de temps faut-il pour reconstruire un composant perdu ? L'opération Cronos contre LockBit en février 2024 a saisi l'infrastructure, identifié l'administrateur, et banni la marque des forums majeurs — pourtant, l'opérateur a tenté de reconstruire sous LockBit 4.0 puis LockBit 5.0, cette dernière version ayant été détectée en attaque active dès septembre 2025 par Check Point Research.

Évaluer la résilience est essentiel pour estimer l'impact d'une action de disruption (Ch.22) : une action qui supprime un nœud substituable a un impact temporaire ; une action qui supprime un nœud critique non redondant a un impact structurel.

## 3.6 Fil rouge — NEXUS : le domaine C2 comme point d'entrée

> **🔍 NEXUS — Épisode 3**
>
> Samira commence par le point d'entrée le plus concret : le domaine C2 `update-srv-infra[.]xyz`. Elle interroge les bases de données de renseignement.
>
> Le **WHOIS actuel** est masqué par un service de privacy (résultat attendu — les acteurs ne laissent plus de données WHOIS exploitables depuis des années). Le **WHOIS historique** (via DomainTools) révèle que le domaine a été enregistré 6 mois plus tôt, et qu'un enregistrement intermédiaire — probablement une erreur OPSEC du registrant — mentionne l'email `kr0n0s-ops@proton.me`.
>
> Le **reverse DNS** montre que l'IP associée au domaine (185.234.xx.xx) est hébergée par un fournisseur VPS basé en Moldavie, connu dans les rapports CTI pour sa tolérance envers les contenus malveillants — un hébergeur bulletproof. Le **reverse IP** (via SecurityTrails) révèle que cette même adresse héberge 4 autres domaines. L'un d'eux, `phantom-news[.]press`, ressemble à un blog.
>
> Ce n'est pas un nœud isolé — c'est un point d'entrée dans un graphe. Samira commence à dessiner : le domaine C2, l'IP, l'hébergeur, l'email ProtonMail, et les domaines co-localisés. Cinq nœuds, quatre liens. Le graphe est encore embryonnaire. Mais la méthode est en place.

---
