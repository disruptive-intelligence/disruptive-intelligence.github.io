---
title: PARTIE III — LIENS, CORRÉLATIONS ET RIGUEUR ANALYTIQUE
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
chapter: 3
chapters: 8
---

*La partie la plus importante du cours sur le plan méthodologique. Savoir relier des entités est inutile si on ne sait pas qualifier la nature et la force des liens, et si on ne maîtrise pas les pièges de la surcorrélation.*

---

## Chapitre 11 — Les types de liens

### 11.1 Lien technique

Le lien technique est établi quand deux entités partagent un élément d'infrastructure : même adresse IP, même certificat SSL/TLS, même infrastructure C2, même malware ou builder, même serveur DNS, même registrar, ou même pattern de configuration technique.

Les liens techniques sont les plus faciles à établir automatiquement (les transforms Maltego, les requêtes Shodan, les bases de données CTI les révèlent) et les plus trompeurs. Le piège fondamental est la mutualisation : deux domaines hébergés sur la même IP partagent un lien technique, mais ce lien peut refléter une co-gestion intentionnelle (les deux domaines appartiennent au même acteur) ou une simple coïncidence d'hébergement (les deux domaines sont chez le même hébergeur bulletproof sans aucun lien entre les locataires).

Pour évaluer la significativité d'un lien technique, l'analyste doit estimer la spécificité de l'élément partagé. Un certificat wildcard partagé est très spécifique (il implique un contrôle administratif commun). Un même Google Analytics ID est très spécifique (il implique un accès au même compte Google). Un même ASN est peu spécifique (des milliers de clients partagent un ASN). Un même registrar est peu spécifique (un registrar populaire sert des millions de domaines).

### 11.2 Lien financier

Le lien financier est établi quand un flux de valeur (typiquement un transfert de cryptomonnaie) connecte deux entités. Les liens financiers sont généralement plus significatifs que les liens techniques, car un transfert d'argent implique une relation intentionnelle — on ne transfère pas des fonds à un inconnu par accident.

Les types de liens financiers incluent le paiement direct (A paie B pour un service — achat d'accès, commission RaaS, paiement de crypter), le transfert via intermédiaire (A envoie des fonds à B via un wallet de transit — le lien est indirect mais traçable), le partage de revenus (les fonds d'une rançon sont automatiquement répartis entre l'affilié et l'opérateur — la répartition révèle le modèle économique), et le blanchiment commun (deux acteurs utilisent le même service de mixing ou le même circuit de cash-out).

Les limites sont réelles : un transfert via un mixer ou un exchange centralisé rompt le lien traçable entre l'émetteur et le récepteur. Le mixer reçoit des fonds de centaines d'utilisateurs et redistribue des fonds mélangés — le fait que les fonds « ressortent » du mixer vers un wallet ne prouve pas qu'ils « proviennent » d'un wallet d'entrée spécifique (c'est un lien probabiliste, pas déterministe).

### 11.3 Lien identitaire

Le lien identitaire relie des comptes ou des profils à une même personne (ou à une entité prétendant être la même). Les indices identitaires incluent le même pseudo utilisé sur plusieurs plateformes, le même email, la même clé PGP (un identifiant fort — la possession de la clé privée prouve le contrôle), le même avatar ou photo de profil, et le même numéro de téléphone (pour les comptes Telegram notamment).

La force d'un lien identitaire dépend de la spécificité de l'identifiant. Une clé PGP est un identifiant fort (unique et non devinable). Un pseudo courant est un identifiant faible (des milliers de personnes peuvent utiliser le même pseudo). Un email ProtonMail unique est un identifiant modéré (il est probable, mais pas certain, qu'un seul acteur l'utilise).

### 11.4 Lien linguistique et comportemental

Le lien linguistique et comportemental est établi quand deux comptes ou profils partagent des caractéristiques stylistiques ou comportementales distinctives : même vocabulaire spécifique, mêmes tics de langage, mêmes erreurs grammaticales, mêmes heures d'activité, mêmes patterns de réponse.

Ces liens sont individuellement faibles — deux personnes du même pays et de la même génération auront des styles similaires. Mais en faisceau avec d'autres indicateurs, ils deviennent significatifs. Un même fuseau horaire d'activité + un même argot régional + les mêmes abréviations inhabituelles = un faisceau convergent.

### 11.5 Lien social

Le lien social est établi quand deux acteurs interagissent directement : conversation observée sur un forum ou un canal Telegram, recommandation mutuelle (vouching), co-administration d'un canal, mention directe dans un message. Les liens sociaux révèlent les relations de confiance — un vouching sur un forum est l'équivalent d'une recommandation professionnelle.

### 11.6 Lien narratif et informationnel

Le lien narratif est établi quand deux entités relaient le même récit, utilisent les mêmes éléments de langage, ou participent à la même campagne de communication. Ce type de lien est caractéristique des écosystèmes d'influence (Ch.32) mais apparaît aussi dans les opérations ransomware quand le leak site, le canal Telegram, et un média de façade diffusent le même message.

### 11.7 Lien temporel

Le lien temporel est établi quand deux événements se produisent en séquence rapide, suggérant une relation causale. Un accès est mis en vente sur un forum le 3 mars ; un ransomware est déployé chez la même victime le 15 mars. La séquence temporelle (12 jours entre la vente d'accès et le déploiement) est un indicateur fort de lien opérationnel entre l'IAB et l'affilié.

Les liens temporels sont particulièrement utiles quand les autres types de liens sont absents (pas de lien technique direct, pas de lien financier traçable). La temporalité est un indice de causalité potentielle — pas une preuve de causalité, mais un signal qui justifie une investigation plus approfondie.

### 11.8 Qualifier un lien : direct/indirect, fort/faible, contextuel/structurel

Chaque lien identifié doit être qualifié selon trois axes.

**Direct vs indirect.** Un lien direct implique une relation sans intermédiaire (A paie B, A utilise le serveur de B, A et B communiquent directement). Un lien indirect passe par un intermédiaire (A et B utilisent le même mixer, A et B sont membres du même forum). Les liens directs sont plus significatifs.

**Fort vs faible.** Un lien fort est basé sur un indice hautement spécifique (même clé PGP, même certificat wildcard, transfert financier direct). Un lien faible est basé sur un indice peu spécifique (même hébergeur, même fuseau horaire, même forum). Un lien fort peut suffire à établir une connexion ; un lien faible nécessite une corroboration par d'autres liens.

**Contextuel vs structurel.** Un lien contextuel est ponctuel (A et B ont interagi une fois sur un forum). Un lien structurel est durable et récurrent (A achète régulièrement des accès à B depuis 6 mois). Les liens structurels révèlent la véritable architecture de l'écosystème.

### 11.9 Fil rouge — NEXUS : tableau de synthèse des liens

> **🔍 NEXUS — Épisode 11**
>
> Samira compile un tableau de synthèse des liens identifiés à ce stade de l'investigation.
>
> | Entité A | Entité B | Type de lien | Qualification | Confiance |
> |----------|----------|-------------|---------------|-----------|
> | Domaine C2 | Blog phantom-news | Technique (même IP + même certificat + même GA ID) | Direct, Fort, Structurel | Élevée (B1) |
> | Email proton.me | Pseudo kr0n0s_ops (XSS) | Identitaire (breach) | Direct, Fort | Élevée (B2) |
> | kr0n0s_ops (XSS) | kr0n0s_ops (GitHub) | Identitaire (même pseudo) + Comportemental (même style) | Direct, Modéré | Modérée (C2) |
> | kr0n0s_ops (Telegram) | ghost_access (Telegram) | Social (interaction directe, achat d'accès) | Direct, Fort, Structurel | Élevée (B1) |
> | ghost_access | Cible Énergis | Temporel (vente d'accès 12 jours avant le déploiement) | Indirect, Fort | Modérée (C2) |
> | Wallets PhantomCrypt | Exchange Dubaï | Financier (flux via mixer) | Indirect, Modéré | Modérée (C3) |
> | Wallets PhantomCrypt | Wallet para-étatique | Financier (flux via mixer) | Indirect, Faible | Faible (D3) |
>
> Chaque lien est qualifié, ce qui permet de distinguer les connexions solides des pistes exploratoires.

---

## Chapitre 12 — Corrélation, faisceau d'indices et prudence analytique

### 12.1 Différence entre coïncidence et corrélation

Deux événements peuvent se produire simultanément ou en séquence sans être liés. Deux acteurs peuvent utiliser le même outil sans se connaître. Deux wallets peuvent recevoir des fonds du même exchange sans que leurs propriétaires aient un quelconque lien. Cette évidence est souvent oubliée quand le graphe est complexe et que l'analyste cherche à « raconter une histoire » cohérente.

Le cerveau humain est câblé pour détecter des patterns — y compris dans le bruit aléatoire. C'est le biais d'appariement (pattern matching bias) : confronté à des données complexes, l'analyste « voit » des liens qui n'existent pas, parce que son cerveau cherche activement de la cohérence. Dans un graphe de 100 nœuds, le nombre de paires possibles est 4 950 — il est statistiquement inévitable que certaines paires présentent des ressemblances fortuites.

La discipline analytique consiste à tester chaque corrélation apparente : « Ce lien pourrait-il être une coïncidence ? Quelle est l'explication alternative la plus probable ? Si ce lien est réel, quelles autres traces devrait-on trouver ? »

### 12.2 Convergence d'indices et indépendance des sources

La convergence est le standard de preuve en analyse de renseignement. Un indice isolé ne prouve rien. Deux indices concordants suggèrent. Trois indices indépendants convergents commencent à démontrer.

Le mot clé est « indépendants ». Trois articles de presse qui citent tous la même source ne sont pas trois indices indépendants — c'est un seul indice (la source originale) amplifié par la reprise médiatique. Trois transforms Maltego qui retournent le même résultat ne sont pas trois indices indépendants si elles interrogent la même base de données — c'est un seul résultat vu trois fois.

L'indépendance s'évalue en remontant à la source primaire. Un lien établi par le WHOIS historique (source : registrar) et corroboré par une breach de forum (source : base de données fuitée) et confirmé par une analyse de la blockchain (source : données on-chain) repose sur trois sources indépendantes. La convergence est forte.

### 12.3 Les faux liens — catalogue raisonné

Les faux liens sont des connexions apparentes qui ne reflètent pas une relation opérationnelle réelle. Voici les cas les plus fréquents.

**Mutualisation de services.** Le même hébergeur, le même crypter, le même registrar, le même VPN sont utilisés par des acteurs sans lien. C'est la source de faux liens la plus fréquente.

**Réemploi opportuniste.** Un acteur reprend un domaine expiré, un pseudo abandonné, ou un serveur revendu par un autre acteur. Le lien historique entre l'ancien et le nouveau propriétaire est un artefact, pas un lien opérationnel.

**Copie de TTP.** Un acteur imite délibérément les techniques, tactiques et procédures d'un autre groupe pour brouiller l'attribution. C'est documenté dans les opérations de false flag étatiques (voir Ch.34) mais aussi dans la cybercriminalité courante (un nouveau groupe utilise le code source fuité d'un ancien groupe sans avoir de lien avec lui).

**Pseudo vendu ou partagé.** Un compte de forum avec une bonne réputation a une valeur marchande. Il peut changer de main par vente, héritage au sein d'un groupe, ou vol. Les activités du nouveau propriétaire n'ont aucun lien avec celles de l'ancien.

**Wallet de transit.** Un wallet intermédiaire utilisé par un service (mixer, exchange, plateforme de paiement) est traversé par les fonds de dizaines d'acteurs différents. Relier deux acteurs parce que leurs fonds ont transité par le même wallet est une erreur si ce wallet est un nœud de service.

**Infra louée.** Un serveur peut être loué par un acteur, restitué, puis loué par un autre. L'historique d'hébergement crée un lien temporel entre les deux qui ne reflète pas une relation réelle.

### 12.4 Contamination analytique

La contamination analytique survient quand une erreur d'attribution initiale se propage dans toute l'analyse et se renforce par le biais de confirmation.

Scénario typique : l'analyste identifie à tort que le pseudo X = la personne Y (par exemple en se basant sur un seul indice faible — même pseudo courant sur deux plateformes). Une fois cette « identification » acceptée, l'analyste interprète toutes les activités de X comme celles de Y. Chaque nouvelle donnée est interprétée à travers le prisme de cette attribution initiale, les données contradictoires sont minimisées, et l'analyste développe une conviction croissante qui n'est pas justifiée par les preuves.

Le remède est la discipline de l'hypothèse alternative. Pour chaque identification, l'analyste doit formuler au moins une hypothèse alternative crédible (« et si kr0n0s_ops sur XSS n'était PAS le même que kr0n0s_ops sur GitHub ? ») et rechercher activement les données qui permettraient de la confirmer ou de l'infirmer. C'est le principe de l'Analysis of Competing Hypotheses (ACH) détaillé au Ch.13.

### 12.5 Fil rouge — NEXUS : test de robustesse

> **🔍 NEXUS — Épisode 12**
>
> Samira effectue un test de robustesse systématique sur chaque lien du graphe.
>
> **Test du lien technique C2-Blog :** Pourrait-il s'agir d'une simple co-localisation ? Vérification : les deux sites partagent non seulement l'IP mais aussi le même Google Analytics ID (`UA-XXXXXXXX-1`) et le même certificat wildcard. La probabilité d'une co-gestion est très élevée. **Verdict : lien validé, confiance élevée.**
>
> **Test du lien identitaire kr0n0s_ops (XSS) – kr0n0s_ops (GitHub) :** Pourrait-il s'agir d'un homonyme ? Le pseudo n'est pas générique — « kr0n0s_ops » est suffisamment distinctif pour réduire le risque d'homonymie. Les repos GitHub contiennent des scripts d'exploitation qui correspondent aux compétences revendiquées sur le forum. L'analyse linguistique montre un profil russophone cohérent. Le fuseau horaire GitHub (commits) et le fuseau horaire XSS (posts) sont compatibles. **Verdict : convergence forte, confiance modérée à élevée.**
>
> **Test du lien financier via mixer :** Le lien entre les wallets PhantomCrypt et le wallet « para-étatique » passe par un service de mixing. Le mixer mélange les fonds de centaines d'utilisateurs. Le fait que des fonds sortent du mixer vers ce wallet spécifique est un indice mais pas une preuve de relation directe — les fonds pourraient provenir de n'importe quel autre utilisateur du mixer. **Verdict : lien indicatif, confiance faible. Nécessite des données complémentaires (pattern temporel, volume, récurrence).**

---

## Chapitre 13 — Niveaux de confiance et formulation analytique

### 13.1 Hypothèses concurrentes et ACH

L'Analysis of Competing Hypotheses (ACH) est une méthode structurée développée par Richards Heuer pour la CIA, conçue pour contrer le biais de confirmation. Le principe est de formuler plusieurs hypothèses mutuellement exclusives, puis de tester systématiquement chaque donnée disponible contre toutes les hypothèses — pas seulement contre l'hypothèse préférée.

Dans le contexte de la cartographie d'écosystèmes, les hypothèses concurrentes portent typiquement sur l'attribution (qui est derrière l'attaque ?), la motivation (pourquoi cette cible ?), et la structure (quel est le lien entre les acteurs ?).

L'ACH fonctionne en 5 étapes. Premièrement, lister toutes les hypothèses raisonnables (pas seulement les deux ou trois les plus évidentes). Deuxièmement, lister toutes les données disponibles (les « évidences »). Troisièmement, pour chaque évidence, évaluer sa compatibilité avec chaque hypothèse (compatible, incompatible, ou non discriminante). Quatrièmement, identifier l'hypothèse la plus consistante (celle qui n'a pas d'évidences incompatibles). Cinquièmement, évaluer la sensibilité (le résultat changerait-il si une donnée clé s'avérait erronée ?).

### 13.2 Grille de cotation : fiabilité de la source × fiabilité de l'information

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

### 13.3 Formulation prudente

Le vocabulaire de l'analyste reflète sa rigueur. Les formulations appropriées incluent « les données suggèrent que... » (confiance modérée), « il est probable que... » (confiance élevée mais pas certitude), « selon notre hypothèse principale... » (hypothèse explicitement identifiée), et « nous n'avons pas pu établir si... » (angle mort explicite).

Les formulations à proscrire incluent « kr0n0s_ops est le cybercriminel X » (affirmation d'identité sans nuance), « le groupe Y a attaqué Z » (attribution catégorique), « les preuves montrent que... » (l'analyste CTI ne produit pas des preuves au sens judiciaire), et « il est certain que... » (la certitude n'existe pas en analyse de renseignement).

La bonne formulation est : « Les indices convergents (pseudo commun, clé PGP partagée, profil linguistique cohérent, fuseau horaire compatible) suggèrent avec un niveau de confiance élevé (B2) que les comptes kr0n0s_ops sur XSS, GitHub, et Telegram sont contrôlés par la même entité. L'identité réelle de cette entité n'a pas pu être établie dans le cadre de cette investigation. »

### 13.4 Ce que l'on sait, ce que l'on estime, ce que l'on suppose, ce que l'on ne sait pas

Le rapport d'analyse doit distinguer explicitement quatre catégories de connaissances.

**Ce que l'on sait** (faits établis, cotés A1-B2) : les domaines, les IP, les hash de malware, les transactions blockchain, les messages observés sur les forums. Ce sont des données vérifiables.

**Ce que l'on estime** (conclusions analytiques, basées sur la convergence d'indices, cotées B2-C3) : l'attribution des comptes à un même acteur, l'identification des rôles dans l'écosystème, la reconstitution de la chaîne d'attaque. Ce sont des interprétations documentées.

**Ce que l'on suppose** (hypothèses non confirmées, cotées C3-D4) : la motivation de l'attaque (purement financière vs para-étatique), la localisation géographique de l'acteur, les liens avec des entités étatiques. Ce sont des pistes exploratoires.

**Ce que l'on ne sait pas** (angles morts explicites) : l'identité réelle de l'acteur, le périmètre exact de l'exfiltration, l'existence d'autres affiliés ciblant la même entreprise, la structure interne de l'opérateur RaaS. Documenter les angles morts est aussi important que documenter les résultats.

### 13.5 Fil rouge — NEXUS : conclusions intermédiaires formalisées

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
