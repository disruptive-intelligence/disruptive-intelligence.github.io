---
title: Chapitre 12 — Corrélation, faisceau d'indices et prudence analytique
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie III — Liens, corrélations et rigueur analytique
  - index.md
---

## 12.1 Différence entre coïncidence et corrélation

Deux événements peuvent se produire simultanément ou en séquence sans être liés. Deux acteurs peuvent utiliser le même outil sans se connaître. Deux wallets peuvent recevoir des fonds du même exchange sans que leurs propriétaires aient un quelconque lien. Cette évidence est souvent oubliée quand le graphe est complexe et que l'analyste cherche à « raconter une histoire » cohérente.

Le cerveau humain est câblé pour détecter des patterns — y compris dans le bruit aléatoire. C'est le biais d'appariement (pattern matching bias) : confronté à des données complexes, l'analyste « voit » des liens qui n'existent pas, parce que son cerveau cherche activement de la cohérence. Dans un graphe de 100 nœuds, le nombre de paires possibles est 4 950 — il est statistiquement inévitable que certaines paires présentent des ressemblances fortuites.

La discipline analytique consiste à tester chaque corrélation apparente : « Ce lien pourrait-il être une coïncidence ? Quelle est l'explication alternative la plus probable ? Si ce lien est réel, quelles autres traces devrait-on trouver ? »

## 12.2 Convergence d'indices et indépendance des sources

La convergence est le standard de preuve en analyse de renseignement. Un indice isolé ne prouve rien. Deux indices concordants suggèrent. Trois indices indépendants convergents commencent à démontrer.

Le mot clé est « indépendants ». Trois articles de presse qui citent tous la même source ne sont pas trois indices indépendants — c'est un seul indice (la source originale) amplifié par la reprise médiatique. Trois transforms Maltego qui retournent le même résultat ne sont pas trois indices indépendants si elles interrogent la même base de données — c'est un seul résultat vu trois fois.

L'indépendance s'évalue en remontant à la source primaire. Un lien établi par le WHOIS historique (source : registrar) et corroboré par une breach de forum (source : base de données fuitée) et confirmé par une analyse de la blockchain (source : données on-chain) repose sur trois sources indépendantes. La convergence est forte.

## 12.3 Les faux liens — catalogue raisonné

Les faux liens sont des connexions apparentes qui ne reflètent pas une relation opérationnelle réelle. Voici les cas les plus fréquents.

**Mutualisation de services.** Le même hébergeur, le même crypter, le même registrar, le même VPN sont utilisés par des acteurs sans lien. C'est la source de faux liens la plus fréquente.

**Réemploi opportuniste.** Un acteur reprend un domaine expiré, un pseudo abandonné, ou un serveur revendu par un autre acteur. Le lien historique entre l'ancien et le nouveau propriétaire est un artefact, pas un lien opérationnel.

**Copie de TTP.** Un acteur imite délibérément les techniques, tactiques et procédures d'un autre groupe pour brouiller l'attribution. C'est documenté dans les opérations de false flag étatiques (voir Ch.34) mais aussi dans la cybercriminalité courante (un nouveau groupe utilise le code source fuité d'un ancien groupe sans avoir de lien avec lui).

**Pseudo vendu ou partagé.** Un compte de forum avec une bonne réputation a une valeur marchande. Il peut changer de main par vente, héritage au sein d'un groupe, ou vol. Les activités du nouveau propriétaire n'ont aucun lien avec celles de l'ancien.

**Wallet de transit.** Un wallet intermédiaire utilisé par un service (mixer, exchange, plateforme de paiement) est traversé par les fonds de dizaines d'acteurs différents. Relier deux acteurs parce que leurs fonds ont transité par le même wallet est une erreur si ce wallet est un nœud de service.

**Infra louée.** Un serveur peut être loué par un acteur, restitué, puis loué par un autre. L'historique d'hébergement crée un lien temporel entre les deux qui ne reflète pas une relation réelle.

## 12.4 Contamination analytique

La contamination analytique survient quand une erreur d'attribution initiale se propage dans toute l'analyse et se renforce par le biais de confirmation.

Scénario typique : l'analyste identifie à tort que le pseudo X = la personne Y (par exemple en se basant sur un seul indice faible — même pseudo courant sur deux plateformes). Une fois cette « identification » acceptée, l'analyste interprète toutes les activités de X comme celles de Y. Chaque nouvelle donnée est interprétée à travers le prisme de cette attribution initiale, les données contradictoires sont minimisées, et l'analyste développe une conviction croissante qui n'est pas justifiée par les preuves.

Le remède est la discipline de l'hypothèse alternative. Pour chaque identification, l'analyste doit formuler au moins une hypothèse alternative crédible (« et si kr0n0s_ops sur XSS n'était PAS le même que kr0n0s_ops sur GitHub ? ») et rechercher activement les données qui permettraient de la confirmer ou de l'infirmer. C'est le principe de l'Analysis of Competing Hypotheses (ACH) détaillé au Ch.13.

## 12.5 Fil rouge — NEXUS : test de robustesse

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
