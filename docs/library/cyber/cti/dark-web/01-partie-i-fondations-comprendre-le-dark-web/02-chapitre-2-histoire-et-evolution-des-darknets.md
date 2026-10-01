---
title: Chapitre 2 — Histoire et évolution des darknets
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie I — Fondations : COMPRENDRE le DARK WEB'
  - index.md
---

Comprendre le dark web contemporain nécessite de connaître son histoire. Les darknets ont une trajectoire de 25 ans, marquée par des ruptures technologiques, des figures emblématiques, et des grandes opérations de police qui ont reconfiguré l'écosystème à plusieurs reprises.

## 2.1 Les origines : anonymat et recherche militaire (1990s)

L'histoire du dark web commence dans les années 1990 au **Naval Research Laboratory** (NRL) américain, où des chercheurs (notamment **Paul Syverson**, **Michael Reed**, **David Goldschlag**) développent le concept d'**onion routing** : un protocole où les communications sont chiffrées en couches successives, chaque nœud intermédiaire ne pouvant déchiffrer que la couche qui lui est destinée, révélant le saut suivant sans connaître ni l'origine ni la destination finale. L'objectif initial est la **protection des communications de renseignement** — permettre à des agents de communiquer sans que leur trafic puisse être identifié par un adversaire observant le réseau.

Paradoxe fondamental vite identifié : un réseau d'anonymat **ne fonctionne que si beaucoup de gens l'utilisent**. Si seuls les agents de renseignement américains utilisent l'onion routing, tout le trafic observé devient attribuable (« cette communication vient d'un agent américain »). L'anonymat requiert une **foule** — et la foule requiert des usages multiples, y compris civils.

En 2002, **Roger Dingledine** et **Nick Mathewson**, rejoints par Paul Syverson, lancent le **Tor Project** comme implémentation **open source** de l'onion routing. Le projet devient indépendant en 2006 sous la forme d'une organisation à but non lucratif, avec un financement mixte — initialement beaucoup du gouvernement américain (Naval Research Laboratory, Broadcasting Board of Governors, State Department DRL), puis progressivement diversifié (donations individuelles, Mozilla, DARPA, fondations). Cette structure de financement mixte est emblématique du paradoxe : le gouvernement américain finance un outil qui protège aussi les criminels (cible d'investigation FBI), parce qu'il protège surtout les usages légitimes qui justifient stratégiquement l'existence du réseau.

## 2.2 L'ère Silk Road (2011-2013)

**Silk Road**, créé par **Ross Ulbricht** (alias « Dread Pirate Roberts ») en février 2011, est le premier darknet market généraliste significatif. L'idée : un e-commerce clandestin inspiré d'eBay, utilisant Tor pour l'anonymat et Bitcoin pour les paiements. Ulbricht articule une vision libertarienne — vendre n'importe quel produit entre adultes consentants sans intervention étatique.

Silk Road grandit rapidement. Au moment de sa saisie par le FBI en octobre 2013, la plateforme totalise plus de **1,2 million de transactions** avec plus de **150 000 acheteurs** et **4 000 vendeurs**. Dominé par les drogues (~70% des ventes), le catalogue inclut aussi documents contrefaits, services de hacking, armes (controversé, règles internes restrictives sur ce point), mais exclut explicitement CSAM et contrats de tueurs à gages (règles internes interdisant l'« harm against others »).

Ulbricht est arrêté le 1er octobre 2013 dans une bibliothèque publique de San Francisco, ordinateur portable ouvert sur son interface administrateur. Identifié via plusieurs **erreurs OPSEC** cumulatives : un post sur StackOverflow avec son vrai email rthomeumm sous le pseudonyme « frosty », un post sur un forum Bitcoin en avril 2011 sous le pseudonyme « altoid » promouvant Silk Road (alors tout nouveau), un serveur CAPTCHA qui a leaké l'IP du serveur Silk Road lors d'une requête mal configurée (point débattu — les défenseurs d'Ulbricht ont soutenu que cette découverte était une reconstruction *a posteriori* par le FBI, possiblement couvrant une méthode de collecte classifiée).

Ulbricht est condamné en mai 2015 à **double perpétuité sans possibilité de libération conditionnelle plus 40 ans**, peine considérée comme disproportionnée par de nombreux observateurs (aucun meurtre n'ayant été commis — les accusations de tentative de contrat sur des témoins ont été utilisées pendant le sentencing sans inculpation formelle). Grâce présidentielle obtenue en janvier 2025 sous l'administration Trump.

L'héritage Silk Road est ambivalent : démonstration que l'e-commerce clandestin à grande échelle est possible (inspiration pour des dizaines de successeurs), mais aussi démonstration des limites de l'OPSEC individuelle face à une enquête FBI déterminée.

## 2.3 La professionnalisation (2014-2019)

Après Silk Road, les successeurs se professionnalisent. **Silk Road 2.0** est lancé en novembre 2013, saisi un an plus tard (novembre 2014, operation Onymous — opération coordonnée qui saisit aussi plusieurs dizaines d'autres marchés). **Evolution Market** devient leader en 2014-2015 avant un exit scam retentissant (mars 2015, ~12 millions de dollars envolés). **Agora**, **Abraxas**, **Dream Market** se succèdent.

**AlphaBay**, lancé en décembre 2014 par **Alexandre Cazes** (canadien basé en Thaïlande, alias « alpha02 »), devient le **plus grand darknet market de l'histoire**. Au moment de sa saisie, le Département de la Justice américain documente **plus de 250 000 listings de drogues et produits chimiques**, auxquels s'ajoutent **plus de 100 000 listings** pour faux documents, accès frauduleux, malwares, armes et services divers. AlphaBay mature significativement le modèle : multiple cryptomonnaies acceptées (Bitcoin, Monero, Ethereum), 2FA obligatoire, PGP, système d'escrow robuste, ratings élaborés.

**Operation Bayonet** (juillet 2017) est une double frappe coordonnée entre le FBI américain et la police néerlandaise. AlphaBay est saisi suite à une erreur OPSEC de Cazes (inclusion de son email personnel `pimp_alex_91@hotmail.com` dans l'en-tête d'un email de bienvenue automatique généré en 2014). Cazes est arrêté en Thaïlande le 5 juillet 2017. Il est retrouvé mort en cellule le 12 juillet 2017 — officiellement suicide, version contestée par sa famille.

Le coup génial de l'opération : la police néerlandaise avait pris le contrôle de **Hansa Market** quelques semaines avant la saisie d'AlphaBay. Quand AlphaBay tombe, les utilisateurs et vendeurs migrent en masse vers Hansa — qui est maintenant opéré par la police. Pendant **30 jours**, les autorités néerlandaises collectent les données (vraies adresses de livraison, IPs, communications, patterns de transactions) avant de saisir Hansa à son tour. Cette opération devient la référence moderne de l'**infiltration active** par les forces de l'ordre.

## 2.4 Hydra et la domination russophone (2015-2022)

**Hydra Market** (ru-center : hydraruzxpnew4af.onion et successeurs) est un cas à part. Lancé en 2015 et exclusivement opéré en russe, Hydra devient le **leader absolu** de l'écosystème russophone. Le DOJ américain et les autorités allemandes indiquent, lors de la saisie d'avril 2022, qu'Hydra a reçu environ **5,2 milliards de dollars en cryptomonnaies depuis 2015** et représentait environ **80% des transactions crypto liées aux darknet markets en 2021**.

Deux particularités structurantes. **Exclusivement russophone** : barrière d'entrée linguistique qui l'a partiellement protégé des actions law enforcement occidentales et de l'infiltration par analystes étrangers. **Système de dead drops physiques** unique : contrairement aux marchés occidentaux qui utilisent la poste (avec les risques que cela implique), Hydra fonctionnait avec des *kladmen* — courriers qui cachaient physiquement les produits dans des endroits spécifiques (sous une pierre dans un parc, dans un interstice de mur), dont les coordonnées GPS étaient ensuite communiquées à l'acheteur. Modèle qui supprime l'interception postale mais crée un écosystème de travailleurs à bas salaire (les kladmen) avec une rotation élevée.

La saisie d'Hydra en avril 2022 par les autorités allemandes (Zentrale Kriminalinspektion, Bundeskriminalamt, avec soutien du FBI) a créé une **fragmentation** massive de l'écosystème russophone : plusieurs marchés successeurs (OMG!OMG!, Mega, BlackSprut, Kraken) se sont partagé le marché sans qu'un leader clair ne s'impose comme Hydra l'était. La fragmentation complique le monitoring (plus de plateformes à suivre) et augmente la méfiance (exit scams plus fréquents sur les nouveaux marchés).

## 2.5 L'ère post-Hydra et les tendances 2024-2026

L'écosystème 2024-2026 présente plusieurs caractéristiques structurantes.

**Fragmentation des marchés généralistes**. Les marchés « tout-en-un » type AlphaBay cèdent la place à des marchés **spécialisés** : marchés de logs (Russian Market), marchés de fraude (BriansClub, WWH Club, anciens 2easy.gg), marchés de ransomware-as-a-service, marchés de services (CaaS). Cette spécialisation reflète la professionnalisation de la cybercriminalité organisée.

**Montée de Telegram comme concurrent**. Telegram est devenu, dans la période 2020-2024, un canal majeur de communication cybercriminelle. Plus accessible que Tor (pas besoin d'outils spéciaux), plus réactif (chats en temps réel), avec des canaux publics et privés. Les canaux Telegram cybercriminels comptent des centaines de milliers de membres cumulés. **Arrestation de Pavel Durov en France le 24 août 2024** — inculpation incluant complicité dans la diffusion de contenus illicites. Impact : Telegram a considérablement durci sa modération (suppression massive de canaux criminels, coopération accrue avec les autorités), conduisant à une migration **partielle** des acteurs vers d'autres plateformes (Session, Matrix sur Tor, retour partiel vers les forums .onion).

**Glissement du vecteur d'accès initial**. L'évolution majeure 2025-2026 documentée par SOCRadar, Flare, Recorded Future : les attaquants **achètent** des credentials valides sur le dark web via des **stealer logs** à prix dérisoire (dès 15 USD) plutôt que de développer des exploits sophistiqués. Le dark web est devenu le **supermarché de l'accès initial**. L'attaquant moderne n'exploite plus la sophistication technique mais la **commoditisation** : pour 15 USD il achète un log d'infostealer, pour 500-50 000 USD il achète un accès VPN corporate préqualifié auprès d'un IAB, et il n'a plus qu'à monétiser.

**Intégration massive de l'IA**. Deepfakes, génération de phishing, chatbots criminels, analyse assistée — l'IA a basculé d'outil émergent à commodité dans la cybercriminalité. Parallèlement, les défenseurs adoptent l'IA pour le monitoring, l'analyse linguistique, et la détection d'anomalies (Ch.39).

**Pression croissante des forces de l'ordre**. Opérations de démantèlement plus fréquentes et plus sophistiquées (LockBit/Cronos février 2024, Kidflix mars 2025, BreachForums multiple, Qakbot, Hive, ALPHV/BlackCat, Genesis Market). Les grands opérateurs RaaS perdent en moyenne **18 mois** d'existence opérationnelle avant démantèlement. La pression a des effets : le niveau de paranoia opérationnelle augmente, les infrastructures se fragmentent pour résilience, et certains opérateurs se « retirent » après un gain significatif.

## 2.6 Chronologie synthétique des grandes dates

| Période | Événement | Impact structurant |
|---------|-----------|--------------------|
| 1995-2002 | Développement onion routing (NRL) | Foundation technique |
| 2002 | Lancement Tor | Accessibilité publique |
| 2009 | Lancement Bitcoin | Couche financière du dark web |
| 2011 | Lancement Silk Road | Premier grand market généraliste |
| 2013 | Saisie Silk Road, arrestation Ulbricht | Premier shock LE majeur |
| 2014 | Lancement AlphaBay, saisie Silk Road 2.0 | Professionnalisation |
| 2015 | Lancement Hydra (ru) | Émergence bloc russophone |
| 2017 | Operation Bayonet (AlphaBay + Hansa) | Référence infiltration LE |
| 2018-2019 | Dream Market, Wall Street Market | Succession post-AlphaBay |
| 2020-2022 | Ascension Telegram / CaaS | Convergence dark web / clearnet |
| 2022 (avril) | Saisie Hydra | Fragmentation russophone |
| 2023 | Operation Cookie Monster (Genesis) | Saisie marché de logs |
| 2024 (février) | Operation Cronos (LockBit) | Disruption grand RaaS |
| 2024 (août) | Arrestation Pavel Durov | Durcissement Telegram |
| 2025-2026 | Commoditisation accès, montée IA | Paradigme contemporain |

## 2.7 Fil rouge — DARKSTREAM : le forum ciblé

> **🌐 DARKSTREAM — Épisode 2 : IndustrialLeaks dans son contexte**
>
> Avant d'y accéder, Lucas documente le forum signalé. **IndustrialLeaks** est un forum .onion russophone créé fin 2022, dans le contexte post-Hydra. Il s'est positionné sur une niche : les **données industrielles** (pas le ransomware classique, pas les credentials bancaires) — documents techniques, spécifications, bases clients, données de supply chain industrielle.
>
> Environ 3 000 membres enregistrés selon les rares rapports publics disponibles. Accès sur **vouching** (parrainage par un membre établi) ou paiement d'un droit d'entrée (0,005 BTC, ~250 USD au cours actuel). Le forum a changé d'adresse .onion **trois fois** en 18 mois — comportement classique face à la pression (soit d'attaques DDoS concurrentes, soit de tentatives d'infiltration). Un miroir I2P est maintenu, indice de maturité technique des opérateurs. La langue principale est le russe ; l'anglais est toléré mais réservé aux ventes grand format.
>
> L'activité principale documentée : ventes de données d'entreprises industrielles (énergie, défense, aérospatial, chimie), occasionnellement services associés (accès persistant, exfiltration ciblée sur commande). Quelques posts de « dumps » publics pour établir la réputation de vendeurs cherchant à monter en crédibilité.
>
> Pour Lucas, ce contexte suggère qu'**IndustrialLeaks est un forum sérieux plus qu'un bazar à scams** — ce qui augmente la probabilité que la mention Vectris soit réelle. Mais il reste prudent : même dans un forum sérieux, l'opportunisme scam est fréquent. La vérification d'authenticité (Ch.14, Ch.25) reste incontournable.

---
