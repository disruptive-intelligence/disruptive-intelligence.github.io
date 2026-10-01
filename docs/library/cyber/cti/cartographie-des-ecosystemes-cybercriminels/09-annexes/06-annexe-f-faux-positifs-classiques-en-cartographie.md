---
title: Annexe F — Faux positifs classiques en cartographie d'écosystèmes
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Annexes
  - index.md
---

| Faux positif | Mécanisme | Comment le détecter | Gravité |
|-------------|-----------|-------------------|---------|
| **Co-localisation d'infrastructure** | Deux domaines sur la même IP chez un hébergeur bulletproof partagé | Vérifier les indicateurs de co-gestion (même certificat, même GA ID, même code custom). Si absents, le lien est non significatif. | Élevée (très fréquent) |
| **Pseudo recyclé** | Un acteur reprend le pseudo abandonné d'un autre | Vérifier la continuité (même clé PGP ? même style d'écriture ? changement brutal de comportement ?) | Élevée |
| **Wallet de transit** | Les fonds transitent par un wallet d'un service (mixer, exchange) utilisé par de nombreux acteurs | Identifier si le wallet est un nœud de service (volume élevé, flux multidirectionnels) ou un wallet personnel | Élevée |
| **Copie de TTP** | Un acteur imite délibérément les techniques d'un autre groupe | Chercher des incohérences (TTP trop parfaitement reproduites, éléments anachroniques, mix de techniques incompatibles) | Élevée (dans le contexte étatique) |
| **Même registrar** | Deux domaines enregistrés chez le même registrar | Non significatif sauf si le registrar est très marginal (un registrar gérant des millions de domaines ne crée pas de lien) | Faible |
| **Même crypter** | Deux malwares obfusqués avec le même service | Non significatif — les crypters sont des services commerciaux utilisés par des centaines de clients | Modérée |
| **Même loader** | Deux payloads distribués par le même loader | Faiblement significatif — les loaders distribuent de multiples payloads de clients différents | Modérée |
| **Contamination analytique** | L'analyste relie deux comptes sur la base d'un indice faible, puis interprète toutes les données suivantes à travers ce lien | Appliquer l'ACH, formuler systématiquement l'hypothèse alternative, réexaminer le lien initial | Critique (erreur méthodologique) |
| **Corrélation temporelle fortuite** | Deux événements proches dans le temps mais sans lien causal | Vérifier si la séquence temporelle est corroborée par d'autres types de liens (technique, financier, social) | Modérée |
| **Amplification médiatique** | Trois sources citent le même fait → interprété comme trois confirmations indépendantes | Remonter à la source primaire. Si les trois sources citent la même origine, c'est un seul indice | Modérée (fréquent en CTI) |
| **Infra louée successivement** | Un serveur loué par A puis restitué et reloué par B crée un faux lien temporel | Vérifier les dates de location, les changements de configuration, les discontinuités | Faible à Modérée |

---

> **Note de clôture**
>
> Ce cours a été conçu pour fournir à l'analyste CTI les cadres conceptuels, les méthodes, les outils et les réflexes nécessaires pour cartographier et comprendre les écosystèmes cybercriminels et para-étatiques dans leur complexité. L'objectif n'était pas d'enseigner des recettes, mais de construire une posture analytique : rigoureuse dans la méthode, humble dans les conclusions, et opérationnelle dans les recommandations.
>
> La cybercriminalité est un phénomène dynamique. Les acteurs, les outils, les plateformes et les modèles économiques décrits ici évolueront. Ce qui ne changera pas, c'est la nécessité de penser en écosystème, de qualifier les liens avant de les affirmer, de distinguer ce que l'on sait de ce que l'on suppose, et de produire du renseignement analytique qui informe des décisions concrètes.
>
> *Comprendre • Relier • Analyser • Produire — avec rigueur et humilité.*
