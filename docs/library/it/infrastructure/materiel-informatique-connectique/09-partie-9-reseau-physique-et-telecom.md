---
title: Partie 9 — Réseau physique et télécom
source: IT/06 Infrastructure & architecture/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

Partie fortement densifiée : c'est le socle du support, de l'admin sys et de la cyber.

---

## 34. RJ45, Ethernet et catégories de câbles

**RJ45 = connecteur** (prise carrée à clip) ; **Ethernet = protocole** qui y circule.

Le câble est fait de **paires torsadées** (les torsades réduisent la diaphonie et les interférences). Sa catégorie fixe le débit maximal :

| Catégorie | Débit max | Distance | Remarque |
|---|---|---|---|
| **Cat5e** | 1 Gb/s | 100 m | Le minimum aujourd'hui |
| **Cat6** | 1 Gb/s (10 Gb/s ≤ 55 m) | 100 m | Excellent choix domestique |
| **Cat6a** | 10 Gb/s | 100 m | 10 Gb/s sur pleine longueur |
| **Cat7** | 10 Gb/s (blindé) | 100 m | Connecteur parfois non standard |
| **Cat8** | 25–40 Gb/s | 30 m | Datacenter uniquement |

### Blindage

- **UTP** : non blindé (le plus courant, suffit chez soi).
- **FTP / STP** : blindé, pour les environnements à fortes interférences (industriel, proximité de câbles électriques). Un câble blindé exige une mise à la terre correcte pour être efficace.

### Vitesses négociées et auto-négociation

Deux équipements Ethernet **négocient** automatiquement la vitesse commune la plus élevée (100 Mb/s, 1 Gb/s, 2,5 Gb/s, 10 Gb/s). Si la négociation échoue (câble abîmé, paire coupée), la liaison retombe souvent à une vitesse basse.

> **🎯 À retenir**
> Pour une installation domestique, du **Cat6 UTP** est l'optimum : 1 Gb/s partout, prêt pour le 2,5/10 Gb/s sur longueurs raisonnables. Inutile de surpayer du Cat8 (datacenter). Le débit réel = le plus lent de la chaîne : carte réseau, câble, switch, port.

> **🔧 Cas concret**
> Liaison « fibre 2 Gb/s » qui plafonne à 1 Gb/s en filaire : vieux câble Cat5 (non e), ou carte réseau/port limité à 1 Gb/s. Le traitement complet « Ethernet bloqué à 100 Mb/s ou 1 Gb/s » est au chapitre 47.

---

## 35. PoE en détail

Le **PoE (Power over Ethernet)** fait transiter **l'alimentation électrique en plus des données** sur le câble réseau. Un seul câble alimente *et* connecte un appareil : caméra IP, point d'accès Wi-Fi au plafond, téléphone IP, serrure connectée.

### Les standards et leur puissance

| Standard | Nom | Puissance à l'appareil (~) |
|---|---|---|
| 802.3af | PoE | ~12,95 W |
| 802.3at | PoE+ | ~25,5 W |
| 802.3bt Type 3 | PoE++ / 4PPoE | ~51 W |
| 802.3bt Type 4 | PoE++ | ~71 W |

(La puissance *injectée* par le switch est un peu plus élevée que celle reçue, à cause des pertes dans le câble — encore le principe : ce qui arrive est inférieur à ce qui part.)

### Qui fournit le courant

- **Switch PoE** : alimente directement les appareils branchés.
- **Injecteur PoE** : ajoute le PoE sur une liaison quand le switch n'est pas PoE.
- **Splitter PoE** : sépare data et courant pour un appareil non-PoE.

> **🎯 À retenir**
> Le PoE simplifie énormément les installations : pas de prise électrique nécessaire là où l'on pose une caméra ou une borne Wi-Fi. Vérifier que le **budget PoE total** du switch (somme des watts pour tous les ports) couvre l'ensemble des appareils — un switch peut supporter le PoE sur 24 ports mais pas à pleine puissance sur tous en même temps.

> **🔧 Cas concret (admin sys)**
> Une caméra PoE qui redémarre en boucle : souvent le budget PoE du switch est dépassé (trop d'appareils gourmands), ou le câble est trop long/abîmé et la tension chute. On vérifie le budget PoE, la longueur et la catégorie du câble.

---

## 36. Fibre optique, SFP/SFP+ et téléphonie

### Fibre optique

La donnée voyage en **lumière** dans un fil de verre : immunité aux interférences, hauts débits, longues distances.

- **FTTH** (Fiber To The Home) : la fibre jusqu'au logement.
- **Monomode** : cœur très fin, longues distances (opérateurs, inter-bâtiments).
- **Multimode** : cœur plus large, courtes distances (intérieur datacenter), moins cher.
- **Connecteurs SC / LC** : SC (carré, à pousser), LC (petit, à clip).
- **ONT** (Optical Network Terminal) : convertit la lumière en signal réseau pour la box.

### SFP / SFP+ : les modules enfichables

Un **SFP** (Small Form-factor Pluggable) est un petit module qu'on enfiche dans un switch ou un serveur pour y connecter une liaison — fibre ou cuivre selon le module.

- **SFP** : jusqu'à 1 Gb/s.
- **SFP+** : 10 Gb/s.
- **SFP28** : 25 Gb/s ; **QSFP+/QSFP28** : 40/100 Gb/s.
- **DAC** (Direct Attach Copper) : un câble cuivre à modules SFP intégrés aux deux bouts, économique pour relier deux équipements proches (entre baies).

> **🎯 À retenir**
> Le SFP rend un switch **modulaire** : un même port accepte de la fibre monomode, multimode ou du cuivre selon le module inséré. Attention à la compatibilité : certains fabricants verrouillent leurs ports sur des modules de leur marque.

### Téléphonie : RJ11

- **RJ11** : connecteur **plus petit** que le RJ45 (2-4 contacts), pour la ligne téléphonique et l'ADSL/VDSL.
- Le **cuivre téléphonique** (et donc le RJ11) disparaît progressivement avec la fibre ; en France, le réseau cuivre historique est en fermeture programmée.

> **⚠️ Erreur fréquente**
> Plier ou écraser un câble fibre comme un câble Ethernet : la fibre est **fragile**, un rayon de courbure trop serré casse le verre ou bloque la lumière. Une jarretière fibre pincée derrière un meuble = perte de connexion ; on remplace le cordon et on respecte le rayon de courbure.

---

## 37. Wi-Fi (jusqu'à Wi-Fi 7) et protocoles sans fil

### Les générations

| Norme | Nom | Bandes |
|---|---|---|
| 802.11n | Wi-Fi 4 | 2,4 / 5 GHz |
| 802.11ac | Wi-Fi 5 | 5 GHz |
| 802.11ax | Wi-Fi 6 | 2,4 / 5 GHz |
| 802.11ax | Wi-Fi 6E | + 6 GHz |
| **802.11be** | **Wi-Fi 7** | 2,4 / 5 / 6 GHz |

### Les bandes — un compromis portée/débit

- **2,4 GHz** : longue portée, traverse bien les murs, mais lent et encombré.
- **5 GHz** : plus rapide, moins encombré, portée plus courte.
- **6 GHz** (6E/7) : très rapide, très peu encombré, portée encore plus courte.

### Ce qu'apporte le Wi-Fi 7

Le Wi-Fi 7 (IEEE 802.11be, « Extremely High Throughput ») introduit trois nouveautés majeures, pour un débit théorique pouvant atteindre ~46 Gb/s :

- **Canaux 320 MHz** (dans la bande 6 GHz) : largeur de canal doublée par rapport au 160 MHz du Wi-Fi 6, donc deux fois plus de données en parallèle.
- **Modulation 4096-QAM (4K-QAM)** : chaque symbole transmet plus de bits qu'avec le 1024-QAM du Wi-Fi 6, augmentant le débit de pointe quand le signal est propre.
- **MLO (Multi-Link Operation)** : un appareil peut utiliser **plusieurs bandes/liens simultanément** (ex. 5 GHz + 6 GHz) pour agréger le débit et réduire fortement la latence et la gigue.

- **Débit réel vs théorique** : les chiffres annoncés sont des maximums de laboratoire. Distance, murs et interférences réduisent fortement le débit réel ; un seul appareil atteint rarement les pics théoriques.
- **Mesh** : plusieurs bornes formant un réseau unique pour couvrir une grande surface.

> **🎯 À retenir**
> Wi-Fi lent *loin* de la box → se rapprocher ou passer en 2,4 GHz (portée). Lent *près* de la box avec beaucoup de voisins → 5/6 GHz (moins encombré). Le **MLO** du Wi-Fi 7 atténue ce dilemme en combinant les bandes, mais exige client *et* borne compatibles.

> **🔒 Sécurité**
> Toujours **WPA3** quand c'est disponible, et un mot de passe long. Le Wi-Fi 7 et son MLO ajoutent de la logique de coordination entre liens qui demande une configuration soignée. Le 6 GHz est surtout un avantage de **performance et de réduction de la congestion** (spectre propre, peu d'appareils) ; ce n'est pas un argument de sécurité en soi. La sécurité dépend davantage de WPA3, de la segmentation réseau (isoler l'IoT et les invités) et de la qualité de la configuration.

### Autres protocoles sans fil de courte portée

| Techno | Portée | Usage |
|---|---|---|
| **Bluetooth** | ~10 m | Audio, claviers, accessoires |
| **NFC** | ~4 cm | Paiement, appairage, badges |
| **Zigbee** | maillé | Domotique (capteurs, ampoules) |
| **Thread** | maillé | Domotique moderne (base de Matter) |

Zigbee et Thread forment des **réseaux maillés** : chaque appareil relaie les autres, étendant la portée. Ils consomment très peu (des années sur pile), là où le Wi-Fi serait trop énergivore pour un capteur de porte. **Matter** unifie la domotique au-dessus de Thread/Wi-Fi pour faire dialoguer des marques différentes.

---

## 38. Câblage domestique et baie de brassage

Comment relier proprement un logement ou un petit bureau — souvent absent des cours, très utile en pratique.

### Le principe : du fixe et du mobile

- **Câblage fixe** : les câbles dans les murs/goulottes, posés une fois, qui ne bougent plus. Ils relient chaque prise murale (RJ45) à un point central.
- **Point central** : un **coffret de communication** (résidentiel) ou une **baie de brassage** (bureau).
- **Patch panel (panneau de brassage)** : tous les câbles fixes y aboutissent, étiquetés. On relie ensuite chaque port du panel au switch par un **cordon de brassage** (court, mobile).

### Pourquoi cette séparation

On ne touche jamais aux câbles muraux : tout le « routage » se fait en façade avec des cordons courts faciles à remplacer. Ajouter un équipement, changer un port défaillant, réorganiser le réseau : tout se fait au niveau du brassage, sans ouvrir un mur.

> **🎯 À retenir**
> Une installation propre repose sur trois éléments : **prises murales RJ45** → **câblage fixe** → **patch panel + switch** en baie. L'**étiquetage** des deux extrémités de chaque câble est ce qui sépare une infrastructure maintenable d'un cauchemar de dépannage. C'est aussi vrai chez soi (coffret de communication) qu'en entreprise.

> **🔧 Cas concret**
> Une prise murale ne donne plus de réseau. Grâce à l'étiquetage du patch panel, on identifie le port correspondant, on teste le cordon de brassage (souvent le coupable), puis on teste la liaison fixe avec un testeur de câble. Sans étiquetage, on perd des heures à deviner quelle prise correspond à quel port.

---
