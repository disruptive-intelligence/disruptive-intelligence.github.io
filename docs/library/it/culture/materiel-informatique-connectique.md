---
title: Matériel informatique & connectique
source: IT/Culture/Materiel_informatique-connectique-andco.md
---

#### Édition 2.1 — Référence de culture matérielle IT & cyber

> Cours autonome, de débutant vers intermédiaire. Objectif : maîtriser le matériel, les connectiques et les standards au point de pouvoir diagnostiquer une panne, lire une fiche technique sans se faire piéger, et tenir une conversation crédible en support, admin système, homelab ou cybersécurité.

---

### Comment lire ce cours

Le cours suit un **fil rouge en trois niveaux**, présent dans la plupart des chapitres :

1. **Comprendre** — comment ça fonctionne réellement, pas seulement le nom.
2. **Choisir** — lire une fiche technique et acheter sans se tromper.
3. **Diagnostiquer** — pourquoi ça ne marche pas, et comment le prouver méthodiquement.

Encadrés récurrents :

- **🎯 À retenir** — l'essentiel.
- **⚠️ Erreur fréquente** — le piège classique.
- **🔧 Cas concret** — situation réelle (souvent orientée support / admin sys / cyber).
- **🔒 Sécurité** — l'angle sécurité matérielle, transversal à tout le cours.

Deux idées structurent l'ensemble. Si tu ne retiens que cela :

> **(1) Connecteur, câble et protocole sont trois choses distinctes.**
> **(2) La performance réelle d'une chaîne est toujours celle de son maillon le plus faible.**

Ces deux principes expliquent à eux seuls la majorité des incompréhensions matérielles, de l'écran 144 Hz bloqué à 60 jusqu'au chargeur 240 W qui ne charge « qu'à 60 W ».

---

### Table des matières

**Partie 1 — Fondations physiques**
1. Électricité, signal et énergie
2. Connecteur, câble, protocole : la distinction fondatrice

**Partie 2 — Composants internes d'un PC**
3. Vue d'ensemble et chaîne de démarrage
4. Le processeur (CPU) : socket, cœurs, architecture
5. Carte mère : chipset, VRM, lignes PCIe
6. PCIe en profondeur : lignes, versions, partage
7. La mémoire vive (RAM)
8. Le stockage (HDD, SSD SATA, NVMe, M.2)
9. La carte graphique (GPU)
10. Alimentation, refroidissement et boîtier
11. Firmware, BIOS/UEFI, TPM et Secure Boot

**Partie 3 — Portables, mini-PC et stations de travail**
12. PC portables et mini-PC
13. Stations de travail

**Partie 4 — Serveurs et infrastructure professionnelle**
14. Qu'est-ce qu'un serveur ? Formats et redondance
15. Composants serveur et gestion hors-bande (iDRAC/iLO/IPMI)
16. RAID matériel vs logiciel, HBA, backplane
17. Stockage en réseau : DAS, NAS, SAN
18. La baie : switch, routeur, firewall, PDU, brassage

**Partie 5 — Écrans et affichage**
19. Comprendre un écran : résolution, densité, dalle
20. Fréquence, fluidité, VRR et latence
21. HDR, couleurs et calibration
22. TV vs écran PC

**Partie 6 — Connectiques vidéo**
23. VGA et DVI (l'héritage analogique)
24. HDMI (jusqu'à 2.2 / Ultra96)
25. DisplayPort
26. Vidéo sur USB-C et choix d'une connectique vidéo

**Partie 7 — USB, Thunderbolt et périphériques**
27. Comprendre l'USB : connecteurs et standards
28. USB-C, USB4 et USB Power Delivery
29. Thunderbolt (jusqu'à Thunderbolt 5)
30. Périphériques, hubs et docks

**Partie 8 — Audio**
31. Jack, audio numérique et DAC
32. XLR, alimentation fantôme et audio pro
33. Bluetooth et audio du salon (RCA, optique, ARC/eARC)

**Partie 9 — Réseau physique et télécom**
34. RJ45, Ethernet et catégories de câbles
35. PoE en détail
36. Fibre optique, SFP/SFP+ et téléphonie
37. Wi-Fi (jusqu'à Wi-Fi 7) et protocoles sans fil
38. Câblage domestique et baie de brassage

**Partie 10 — Énergie : chargeurs, batteries, protection**
39. Chargeurs, charge rapide et charge sans fil
40. Batteries lithium-ion
41. Charge des véhicules électriques
42. Onduleurs et protection électrique

**Partie 11 — Matériel domestique, multimédia et sécurité matérielle**
43. Box, TV connectée, consoles, NAS, impression
44. Sécurité matérielle : USB malveillant, firmware, DMA, équipements exposés

**Partie 12 — Choisir et diagnostiquer**
45. Lire une fiche technique (PC, écran, câble)
46. Choisir selon l'usage
47. Manuel de diagnostic matériel (11 pannes traitées)

**Annexes**
- A. Sources et standards à surveiller
- B. Fiches réflexes (7 aide-mémoires)
- C. Cinq mini-labs de diagnostic

---
## Partie 1 — Fondations physiques

Avant tout équipement, deux fondations. Sans elles, on confond énergie et données, et on croit qu'un connecteur identique garantit une fonction identique.

---

### 1. Électricité, signal et énergie

#### Les trois grandeurs, par l'analogie de l'eau

- **Tension** (volts, V) = la *pression* dans le tuyau.
- **Courant** (ampères, A) = le *débit*, la quantité qui passe.
- **Puissance** (watts, W) = le *travail réellement fourni*.

Relation fondamentale, à connaître par cœur :

```
Puissance (W) = Tension (V) × Courant (A)
```

Un chargeur délivrant 20 V sous 5 A fournit `20 × 5 = 100 W`. Cette formule explique pourquoi l'USB Power Delivery monte la tension (jusqu'à 48 V) pour atteindre 240 W sans faire passer un courant énorme dans le câble : à puissance donnée, plus on monte la tension, moins il faut de courant, donc moins le câble chauffe.

#### AC vs DC

- **Courant alternatif (AC)** : la prise murale (230 V en Europe, 50 Hz). Le sens du courant s'inverse 50 fois par seconde.
- **Courant continu (DC)** : ce dont l'électronique a besoin. Le courant va dans un seul sens.

Un **chargeur** ou une **alimentation** convertit l'AC en DC et abaisse la tension. C'est cette conversion qui produit de la chaleur — d'où le bloc qui chauffe.

#### Pourquoi une puissance annoncée est un plafond, jamais une dose imposée

C'est le malentendu le plus répandu de tout le domaine. Un chargeur annonce une puissance **maximale**. L'appareil **demande** ce dont il a besoin via une négociation ; le chargeur fournit jusqu'à sa limite. Un téléphone qui n'accepte que 18 W ne tirera que 18 W sur un chargeur 100 W, sans danger.

> **⚠️ Erreur fréquente**
> « Mon chargeur est trop puissant, il va griller mon appareil. » Faux. Le danger vient des chargeurs *contrefaits* mal régulés, pas de la puissance élevée d'un chargeur de qualité. On retrouvera ce principe du plafond pour l'USB-PD (chapitre 28) et même la charge des voitures électriques (chapitre 41).

#### Signal : analogique vs numérique

Un câble transporte trois choses possibles : **énergie**, **signal analogique**, **signal numérique** — parfois plusieurs à la fois.

- **Analogique** : variation continue, comme une vague. Se dégrade *progressivement* avec la distance et le bruit. Exemples : VGA, jack 3,5 mm.
- **Numérique** : suite de 0 et 1. Effet *tout ou rien* : soit l'information passe correctement, soit elle ne passe pas (scintillements, coupures). Exemples : HDMI, DisplayPort, USB, Ethernet.

> **🎯 À retenir**
> Un câble **analogique** trop long donne une image *floue*. Un câble **numérique** trop long donne une image *parfaite ou absente* (ou des décrochages). Ce comportement différencié est un outil de diagnostic : un signal qui « papillote » est numérique en limite de tenue ; un signal « baveux » est analogique dégradé.

#### Le vocabulaire qui revient partout

- **Débit / bande passante** : volume de données par seconde (Mb/s, Gb/s). **8 bits = 1 octet** : une ligne « 1 Gb/s » fait au mieux ~125 Mo/s. Le facteur 8 piège tout le monde.
- **Latence** : délai avant que la donnée arrive. Une liaison peut avoir un gros débit *et* une mauvaise latence (cruciale en jeu, visio, audio live).
- **Blindage** : protection métallique contre les perturbations extérieures (UTP/FTP/STP en Ethernet, voir chapitre 34).
- **Interférences** : perturbations électromagnétiques qui dégradent un signal mal protégé.

---

### 2. Connecteur, câble, protocole : la distinction fondatrice

**Le** chapitre clé. Trois choses sont constamment confondues :

| Notion | Définition | Question |
|---|---|---|
| **Connecteur** | La forme physique de la prise | « Est-ce que ça rentre ? » |
| **Câble** | Le fil et ce qu'il sait *réellement* transporter | « Est-ce que ça transporte ce dont j'ai besoin ? » |
| **Protocole / standard** | Les règles de communication | « Est-ce qu'ils se comprennent ? » |

Exemples qui clarifient :

- **USB-C** = un **connecteur** (la forme ovale réversible). Ne dit *rien* des capacités.
- **USB 3.2 / USB4** = des **standards** de transmission.
- **Thunderbolt** = un **protocole** complet qui *emprunte* le connecteur USB-C.
- **HDMI** = à la fois **connecteur** et **protocole** vidéo/audio.
- **RJ45** = **connecteur** ; **Ethernet** = **protocole** qui y circule.

> **🎯 À retenir**
> Deux câbles USB-C physiquement identiques peuvent être radicalement différents : l'un fait charge 240 W + vidéo 8K + 80 Gb/s, l'autre *seulement* de la charge lente. Le connecteur est une promesse de *forme*, jamais de *fonction*. C'est la cause n°1 des « pourquoi ça ne marche pas alors que ça rentre ».

> **🔧 Cas concret**
> « J'ai branché mon écran sur le port USB-C du PC avec un câble USB-C, pas d'image. » Trois causes, toutes dans ce chapitre : (1) le **câble** ne porte pas la vidéo, (2) le **port** ne sait pas sortir de la vidéo (pas de DisplayPort Alt Mode), (3) le **protocole** attendu n'est pas supporté des deux côtés. La forme identique masque trois incompatibilités.

Tout le reste du cours — vidéo, USB, réseau, audio, énergie — est une déclinaison de ce tableau. Garde-le en tête.

---
## Partie 2 — Composants internes d'un PC

---

### 3. Vue d'ensemble et chaîne de démarrage

Un PC est un orchestre de composants spécialisés reliés par la **carte mère**. Qui fait quoi :

- **CPU** : le cerveau, calcule et coordonne.
- **RAM** : mémoire de travail rapide *mais volatile* (vidée à l'extinction).
- **Stockage (SSD/HDD)** : mémoire durable, plus lente.
- **GPU** : spécialiste du calcul massivement parallèle (affichage, IA).
- **Alimentation (PSU)** : convertit le 230 V AC en tensions DC.
- **Refroidissement** : évacue la chaleur pour éviter le bridage thermique.
- **Boîtier** : contient et organise, conditionne le flux d'air.
- **Firmware (UEFI)** : démarre la machine avant l'arrivée de l'OS.

#### La chaîne de démarrage (essentielle pour diagnostiquer)

Comprendre l'ordre d'allumage permet de localiser une panne « PC qui ne démarre pas » :

1. **Alimentation** : reçoit l'ordre, fournit les tensions, envoie un signal « Power Good ».
2. **Firmware UEFI** : s'exécute depuis une puce de la carte mère.
3. **POST** (Power-On Self-Test) : l'UEFI teste CPU, RAM, GPU. Une erreur ici se manifeste par des **bips** ou des **LED de diagnostic** (souvent 4 LED : CPU / DRAM / VGA / BOOT).
4. **Détection du périphérique de démarrage** (SSD/clé/réseau).
5. **Chargement du bootloader**, puis de l'OS.

> **🎯 À retenir**
> Si un PC s'allume (ventilateurs tournent) mais n'affiche rien, le problème est presque toujours *avant* l'OS : RAM mal enfichée, GPU mal détecté, ou écran/câble. Les LED de diagnostic de la carte mère disent à quelle étape ça bloque — c'est l'outil n°1 du dépannage matériel.

---

### 4. Le processeur (CPU) : socket, cœurs, architecture

#### Les notions de performance

- **Cœurs (cores)** : unités de calcul indépendantes. Plus de cœurs = plus de tâches en parallèle.
- **Threads** : fils d'exécution. Avec l'*hyper-threading* (Intel) / *SMT* (AMD), un cœur gère 2 threads.
- **Fréquence (GHz)** : cycles par seconde. Ne se compare *qu'à architecture égale*.
- **Cache** (L1/L2/L3) : mémoire ultra-rapide intégrée, évite d'aller en RAM.
- **Architecture** : x86 (Intel/AMD, PC et serveurs) vs ARM (Apple Silicon, Snapdragon, mobile, de plus en plus de serveurs) — très efficace énergétiquement.
- **TDP** : enveloppe thermique en watts ; indique grossièrement chaleur et besoin de refroidissement.

#### Socket : le point de compatibilité n°1

Le **socket** est l'emplacement physique du CPU sur la carte mère. Il doit correspondre **exactement** : un CPU AMD AM5 n'entre pas dans une carte mère AM4 ; un Intel LGA 1700 ne va pas sur du LGA 1851. Le socket conditionne aussi indirectement la génération de RAM supportée (un socket AM5 implique de la DDR5).

> **⚠️ Erreur fréquente**
> Comparer deux CPU sur la seule fréquence (« 3 GHz > 2,8 GHz »). Entre générations ou marques, faux : un cœur récent à 2,8 GHz écrase souvent un ancien à 3,5 GHz grâce à l'**IPC** (instructions par cycle). On compare via des tests réels, jamais le seul nombre de GHz.

#### Bridage thermique (throttling)

Quand le CPU chauffe trop, il **réduit volontairement** sa fréquence pour survivre. Un PC qui rame après quelques minutes d'effort souffre presque toujours d'un refroidissement insuffisant, pas d'un CPU « trop faible ».

> **🔧 Cas concret**
> Portable rapide au démarrage puis lent après 10 min de visio : pâte thermique sèche + ventilateur encrassé → throttling. Nettoyage et nouvelle pâte = machine relancée, sans rien remplacer d'autre.

---

### 5. Carte mère : chipset, VRM, lignes PCIe

La carte mère ne « rend pas le PC plus rapide » : elle décide **ce qu'on peut y brancher** et **avec quelle stabilité**.

- **Socket** : voir chapitre 4 ; doit matcher le CPU.
- **Chipset** : le « gestionnaire de trafic » de la carte. Il détermine les fonctionnalités : nombre de ports, possibilité d'overclocking, nombre de lignes PCIe disponibles, ports USB rapides. Sur une même plateforme, un chipset haut de gamme (ex. X870 chez AMD, Z890 chez Intel) offre plus de connectique et l'overclocking ; un chipset d'entrée de gamme (A620, H810) est bridé mais moins cher.
- **VRM** (Voltage Regulator Module) : le circuit qui **alimente proprement le CPU** en transformant le 12 V de l'alim en la tension précise et stable dont le processeur a besoin. Des VRM de qualité (plus de « phases », meilleurs dissipateurs) = stabilité sous charge et durée de vie. **Un VRM faible bride un CPU puissant** ou provoque des instabilités sous charge prolongée — point souvent ignoré à l'achat.
- **Slots RAM** : nombre et génération (DDR4/DDR5).
- **Slots PCIe et ports M.2** : voir chapitre 6.
- **Connecteurs internes** : ATX 24 broches, EPS/CPU, ventilateurs, façade, USB internes.

> **🎯 À retenir — la règle de compatibilité de la plateforme**
> Une configuration cohérente se vérifie sur quatre points :
> 1. **CPU ↔ socket** (correspondance exacte) ;
> 2. **CPU ↔ chipset** (et version de firmware UEFI suffisamment récente pour reconnaître un CPU sorti après la carte) ;
> 3. **RAM ↔ génération** (DDR4 *ou* DDR5, jamais mélangées, le slot est physiquement différent) ;
> 4. **GPU ↔ slot PCIe + alimentation + place dans le boîtier**.
> Vérifier ces quatre points évite l'essentiel des montages qui ne démarrent pas.

> **⚠️ Erreur fréquente**
> Acheter un CPU récent et une carte mère du même socket… dont le firmware d'usine est trop ancien pour le reconnaître. La carte ne POST pas. Solution : une fonction **BIOS Flashback** (mise à jour du firmware sans CPU), si la carte la possède. À vérifier *avant* l'achat sur une plateforme récente.

---

### 6. PCIe en profondeur : lignes, versions, partage

Le **PCI Express (PCIe)** est l'autoroute qui relie le CPU/chipset aux composants rapides : carte graphique, SSD NVMe, cartes réseau, contrôleurs. C'est une notion centrale et souvent mal comprise.

#### Lignes (lanes) et largeur de slot

Une **ligne PCIe** est une voie de communication bidirectionnelle. Les slots se notent par leur nombre de lignes :

- **x1** : une ligne (carte réseau, carte son).
- **x4** : typiquement un SSD NVMe.
- **x8 / x16** : cartes graphiques, cartes haute performance.

⚠️ Attention : **la taille physique d'un slot ne dit pas le nombre de lignes réellement câblées**. Un slot mécaniquement « x16 » peut n'être branché qu'en « x4 » électriquement. D'où la notation « x16 (x4) ».

#### Versions et débit (le débit double à chaque génération)

| Version PCIe | Débit par ligne (~) | x16 (~) |
|---|---|---|
| PCIe 3.0 | ~1 Go/s | ~16 Go/s |
| PCIe 4.0 | ~2 Go/s | ~32 Go/s |
| PCIe 5.0 | ~4 Go/s | ~64 Go/s |

Les versions sont **rétrocompatibles** : une carte PCIe 4.0 fonctionne dans un slot 3.0, mais au débit du plus lent des deux (encore le maillon faible).

#### Le partage des lignes : le piège qui ralentit un SSD

Le CPU n'offre qu'un **nombre limité de lignes** (souvent ~20-28 côté CPU sur grand public). Le reste passe par le **chipset**, relié au CPU par un lien lui-même limité. Conséquence pratique majeure :

> **⚠️ Erreur fréquente — la plus subtile de ce chapitre**
> Installer un SSD NVMe dans le « 2e port M.2 » et constater que la carte graphique passe de x16 à x8, ou que le SSD tombe à x2. Beaucoup de cartes mères **partagent** les lignes : remplir un port M.2 secondaire ou un slot PCIe désactive ou bride un autre. Le manuel de la carte mère contient toujours un tableau de partage des lignes ; c'est *la* page à lire avant d'ajouter un composant.

> **🔧 Cas concret (homelab/admin sys)**
> On ajoute une carte réseau 10 Gb/s dans un slot PCIe libre, et le SSD NVMe principal s'effondre en performance. Cause : la carte réseau a « volé » les lignes partagées avec le port M.2. La solution est de déplacer la carte ou le SSD vers un port qui ne partage pas, d'après le tableau du manuel.

---

### 7. La mémoire vive (RAM)

La RAM stocke temporairement ce que le CPU manipule maintenant.

- **Générations** : DDR3 (ancien), DDR4 (courant), DDR5 (récent). **Incompatibles entre elles** : encoche et tension différentes. Une carte DDR4 n'accepte pas de DDR5.
- **Fréquence** (3200, 6000 MHz…) : débit. *Note de rigueur : les fiches parlent par habitude de « MHz », mais pour la DDR on devrait dire **MT/s** (méga-transferts par seconde). La DDR transfère deux fois par cycle d'horloge, donc une mémoire « 3200 MHz » tourne en réalité à 1600 MHz d'horloge pour 3200 MT/s. « 6000 MHz » et « 6000 MT/s » désignent donc la même chose dans le langage courant.*
- **Latence CAS (CL)** : réactivité. À fréquence égale, CL plus basse = plus réactif.
- **Dual channel** : 2 (ou 4) barrettes doublent la bande passante mémoire. Impact très visible sur les machines à GPU intégré.
- **ECC** (Error-Correcting Code) : corrige les erreurs mémoire à la volée. Sur serveurs/stations, où une erreur silencieuse corrompt des données critiques. Nécessite CPU + carte compatibles.
- **XMP / EXPO** : profils à activer dans l'UEFI pour que la RAM tourne à sa fréquence annoncée (sinon elle reste à la fréquence de base, plus lente).

> **🎯 À retenir**
> Pour la plupart des usages, la **quantité** prime sur la vitesse : 16 Go lents battent 8 Go rapides en multitâche. Et toujours 2 barrettes pour le dual channel. Penser à activer **XMP/EXPO** : sans cela, une RAM « 6000 MHz » tourne souvent à 4800.

> **⚠️ Erreur fréquente**
> Mélanger des barrettes de fréquences/timings différents : le système aligne tout sur la plus lente, ou devient instable. Pour une mise à niveau fiable, on remplace l'ensemble par un kit assorti plutôt que d'ajouter une barrette dépareillée.

---

### 8. Le stockage (HDD, SSD SATA, NVMe, M.2)

| Type | Techno | Vitesse typique | Usage |
|---|---|---|---|
| **HDD** | Plateaux mécaniques | 100–250 Mo/s | Stockage de masse, archives, peu cher au To |
| **SSD SATA** | Flash sur interface SATA | ~550 Mo/s | Bon rapport prix/perf, plafonné par le SATA |
| **SSD NVMe** | Flash sur lignes PCIe | 3 500–14 000+ Mo/s | Système, jeux, montage, IA |

- **M.2** : un **format physique** (la barrette). ⚠️ Un SSD M.2 peut être **SATA** *ou* **NVMe** — la forme ne dit pas l'interface ni la vitesse. Brancher un M.2 SATA dans un port M.2 qui n'accepte que le NVMe (ou l'inverse) → non détecté. (Encore connecteur ≠ protocole.)
- **PCIe** : le bus que le NVMe utilise pour parler au CPU (voir chapitre 6 — un NVMe en PCIe 5.0 dans un port 3.0 sera bridé).

#### Endurance de la flash

Selon le nombre de bits stockés par cellule : **SLC** (1 bit, très endurant, rare) → **MLC** (2) → **TLC** (3) → **QLC** (4, plus de capacité, moins d'endurance et de vitesse soutenue).

**SMART** : système d'auto-surveillance intégré aux disques. Il remonte température, heures de fonctionnement, secteurs réalloués, usure de la flash. C'est l'outil de prévention de panne par excellence.

> **⚠️ Erreur fréquente**
> Se fier à la vitesse de la boîte. Les SSD QLC bon marché sont rapides sur les premiers Go (cache SLC), puis s'effondrent sur les gros transferts soutenus. La vitesse *soutenue* compte plus que la vitesse de pointe pour copier de gros volumes.

> **🔧 Cas concret**
> PC qui freeze de plus en plus, erreurs aléatoires : lancer un outil SMART (CrystalDiskInfo sous Windows, `smartctl` sous Linux). Un compteur de « secteurs réalloués » qui grimpe = disque mourant → **sauvegarder immédiatement** avant la panne totale.

---

### 9. La carte graphique (GPU)

Spécialiste du calcul massivement parallèle : afficher des millions de pixels, mais aussi calcul scientifique et IA.

- **iGPU (intégré)** vs **dédié** : l'intégré est dans le CPU (bureautique/vidéo) ; le dédié a sa propre mémoire, bien plus puissant.
- **VRAM** : mémoire dédiée. Cruciale en haute résolution, gros jeux et **IA** (un modèle qui n'y tient pas déborde en RAM système et devient des dizaines de fois plus lent).
- **CUDA** (NVIDIA) : écosystème de calcul parallèle dominant en IA/calcul.
- **Ray tracing** : calcul réaliste de la lumière, gourmand.
- **Encodage matériel** (NVENC, etc.) : pour streaming et montage.
- **Connectiques** : HDMI et DisplayPort (Partie 6). Sur PC à GPU dédié, brancher l'écran sur la **carte**, pas sur la carte mère.

> **⚠️ Erreur fréquente**
> Acheter une carte « avec beaucoup de VRAM » mais un GPU faible (cartes piège d'entrée de gamme). La VRAM ne sert à rien si le processeur graphique ne suit pas. On regarde les tests réels, pas la seule taille mémoire.

---

### 10. Alimentation, refroidissement et boîtier

#### Alimentation (PSU)

Convertit le 230 V AC en 3,3 / 5 / 12 V DC.

- **Watts** : à dimensionner sur la consommation réelle de pointe (surtout GPU), avec une marge raisonnable.
- **Certification 80 PLUS** (Bronze → Titanium) : indique le **rendement** (énergie utile vs perdue en chaleur).
- **Rail 12 V** : la ligne principale (CPU et GPU).
- **Modularité** : on ne branche que les câbles utiles (meilleur flux d'air).
- **Connecteurs** : ATX 24 broches (carte mère), EPS 8 broches (CPU), PCIe / **12VHPWR / 12V-2x6** (GPU récents très gourmands).

> **🎯 À retenir**
> Une alimentation de mauvaise qualité est le composant le plus dangereux : en défaillant, elle peut endommager *tout le reste*. C'est le dernier poste sur lequel rogner. Surdimensionner à l'extrême (1000 W pour un PC qui en consomme 300) gaspille de l'argent et réduit le rendement.

#### Refroidissement

- **Air** : radiateur + ventilateur. Simple, fiable, suffit à la majorité.
- **Watercooling AIO** : circuit fermé, pour CPU très puissants ou configs silencieuses.
- **Pâte thermique** : comble les micro-irrégularités CPU/radiateur ; sèche avec les années.
- **Flux d'air** : air frais qui entre, air chaud qui sort.
- **Températures repères** : ~30-50 °C au repos, 70-85 °C en charge sans souci. Au-delà de 90-95 °C prolongés, on cherche un problème.

#### Boîtier et formats

- **Formats de carte mère** (du plus grand au plus petit) : **ATX**, **micro-ATX**, **mini-ITX**. Le boîtier doit accepter le format.
- **Trois pièges de compatibilité** : longueur du GPU, hauteur du ventirad CPU, format/connecteurs de l'alimentation.

> **🔧 Cas concret**
> Tour bruyante et chaude après 2-3 ans : poussière dans les radiateurs. Un nettoyage à l'air sec fait souvent baisser les températures de 10-15 °C et le bruit avec.

---

### 11. Firmware, BIOS/UEFI, TPM et Secure Boot

Brique souvent absente des cours grand public, et pourtant centrale en sécurité et en dépannage.

#### Firmware : du logiciel gravé dans le matériel

Le **firmware** est un logiciel stocké dans une puce d'un appareil, qui le fait fonctionner à bas niveau. Tout en a un : carte mère, SSD, carte réseau, écran, routeur, imprimante, webcam. Il est mis à jour par « flash ». Un firmware obsolète peut empêcher de reconnaître un composant récent (chapitre 5) ou contenir des failles de sécurité (chapitre 44).

#### BIOS et UEFI

Le firmware de la carte mère qui démarre la machine.

- **BIOS** : l'ancien (interface texte, limité aux disques < 2,2 To, démarrage MBR).
- **UEFI** : le moderne (interface graphique, gros disques via GPT, démarrage plus rapide, **Secure Boot**). On dit encore « BIOS » par habitude, mais c'est presque toujours de l'UEFI aujourd'hui.

L'UEFI gère aussi les réglages matériels : ordre de démarrage, activation de la virtualisation (VT-x/AMD-V, indispensable pour les machines virtuelles), profils mémoire XMP/EXPO, ventilateurs.

#### TPM (Trusted Platform Module)

Le **TPM** est une puce de sécurité (soudée, ou intégrée au CPU sous le nom *fTPM*/*PTT*) qui stocke des secrets cryptographiques de façon isolée du reste du système. Ses usages :

- stocker les clés de **chiffrement de disque** (BitLocker, LUKS) pour qu'un disque volé reste illisible ;
- mesurer l'intégrité du démarrage ;
- c'est l'exigence **TPM 2.0** qui a conditionné l'installation de Windows 11.

> **🔒 Sécurité**
> Le TPM permet que le chiffrement de disque soit **transparent** (pas de mot de passe à taper au démarrage) tout en restant sûr : la clé n'est libérée que si le démarrage n'a pas été altéré. Sans TPM, soit on tape une phrase secrète à chaque démarrage, soit la clé est moins bien protégée.

#### Secure Boot

**Secure Boot** est une fonction de l'UEFI qui vérifie la **signature cryptographique** de chaque composant chargé au démarrage (bootloader, noyau). Objectif : empêcher un **bootkit/rootkit** de s'installer *avant* l'OS et de devenir invisible. Seuls les composants signés par des clés de confiance se lancent.

> **🔧 Cas concret (admin sys)**
> Une distribution Linux ou un pilote non signé refuse de démarrer avec Secure Boot actif. Deux voies : utiliser une distribution signée (la plupart des grandes le sont), ou désactiver temporairement Secure Boot dans l'UEFI. Désactiver n'est pas anodin côté sécurité : on le réactive dès que possible.

> **🎯 À retenir**
> Firmware, UEFI, TPM et Secure Boot forment la **racine de confiance** d'une machine : tout ce qui s'exécute ensuite en dépend. C'est aussi pour cela qu'une attaque visant le firmware (chapitre 44) est si grave : elle se situe *sous* l'OS et survit à une réinstallation.

---
## Partie 3 — Portables, mini-PC et stations de travail

---

### 12. PC portables et mini-PC

Un portable est un PC contraint par la **place** et la **chaleur**.

- **CPU basse consommation** : suffixes qui changent tout. Chez Intel, U (économe) < P < H < HX (proche d'un fixe) ; chez AMD, U < HS < H < HX. À nom proche, un portable est toujours plus lent qu'un fixe à cause des limites thermiques.
- **Batterie** : capacité en **Wh** (wattheures), la vraie mesure d'énergie.
- **Écran intégré** : non remplaçable, donc à bien choisir à l'achat (Partie 5).
- **Réparabilité** — les deux lignes décisives :
  - **RAM soudée** ou non : si soudée, jamais extensible.
  - **SSD** remplaçable (M.2) ou soudé.

#### Mini-PC, NUC, thin client

- **Mini-PC / NUC** : un PC complet miniature, idéal media-center, bureautique, ou petit serveur domestique discret (quelques watts).
- **Thin client** : machine légère conçue pour se connecter à un bureau distant (VDI) ; le calcul se fait sur le serveur. Courant en entreprise.

> **🎯 À retenir**
> Avant d'acheter un portable à garder longtemps : RAM soudée ? SSD remplaçable ? Ces deux réponses décident de sa durée de vie utile bien plus que la marque. Et un mini-PC d'occasion (ex-parc d'entreprise) à 10-15 W est souvent le meilleur *premier* serveur perso.

> **🔧 Cas concret (support)**
> « Mon portable de travail rame. » Si RAM soudée à 8 Go saturée : on optimise l'OS, on ne peut pas étendre. Si le « disque » est un vieux HDD et que le M.2 est libre/remplaçable : passage en SSD NVMe → machine transformée pour un coût modique. Connaître la réparabilité oriente tout le diagnostic.

---

### 13. Stations de travail

Machines pro taillées pour la **fiabilité** et le calcul lourd, pas le jeu.

- **CPU workstation** : beaucoup de cœurs (Xeon, Threadripper/EPYC).
- **GPU pro** (RTX/Quadro, Radeon Pro) : pilotes certifiés métier (CAO, 3D), fiabilité de calcul privilégiée.
- **RAM ECC** : pour ne pas corrompre un rendu de 12 h ou un calcul scientifique.
- **Certification** : les éditeurs (CAO, simulation) valident des configs précises.
- **Usages** : rendu 3D, CAO, calcul, montage haut de gamme, entraînement de modèles d'IA.

> **⚠️ Erreur fréquente**
> Croire qu'une station est « un PC gamer en mieux ». Priorités différentes : la station vise la **stabilité sur calculs longs** et la **certification logicielle**, pas le maximum d'images par seconde. Un PC gamer peut être plus rapide en jeu et moins fiable sur un rendu de 10 h.

---

## Partie 4 — Serveurs et infrastructure professionnelle

C'est l'une des parties les plus densifiées, car c'est aussi la moins couverte dans les cours grand public.

---

### 14. Qu'est-ce qu'un serveur ? Formats et redondance

Un serveur n'est pas un « gros PC » : c'est une machine conçue pour **rester disponible en continu**.

Différences clés :

- **Disponibilité** : tourner 24/7 pendant des années.
- **Redondance** : composants doublés (alimentations, disques, parfois ventilateurs) pour qu'une panne n'arrête pas le service.
- **Maintenance à chaud (hot-swap)** : remplacer un élément sans éteindre.
- **Gestion hors-bande** : administration même OS planté (chapitre 15).

#### Formats

- **Tower** : comme une tour PC, pour PME sans baie.
- **Rack** : format plat vissé dans une **baie 19 pouces**, mesuré en **U** (1U ≈ 4,4 cm). Serveurs 1U, 2U, 4U… Plus de U = plus de disques et un meilleur refroidissement. On dimensionne une baie en additionnant les U.
- **Blade** : lames ultra-compactes partageant un châssis commun (alimentation, refroidissement, réseau). Densité maximale en datacenter.
- **Appliance** : matériel + logiciel livrés ensemble pour une fonction (pare-feu, sauvegarde, stockage).

> **🎯 À retenir**
> Philosophie d'un PC : « être rapide ». Philosophie d'un serveur : « ne jamais s'arrêter ». Tout le matériel (redondance, ECC, hot-swap, gestion hors-bande) découle de cette différence.

---

### 15. Composants serveur et gestion hors-bande

- **CPU Xeon (Intel) / EPYC (AMD)** : beaucoup de cœurs, grande capacité de RAM ECC, multi-socket possible.
- **RAM ECC** : correction d'erreurs (chapitre 7), indispensable quand une corruption silencieuse aurait des conséquences graves.
- **Alimentations redondantes** : deux blocs (ou plus), souvent sur **deux circuits électriques distincts**. L'un lâche, l'autre prend le relais sans coupure.
- **Disques hot-swap** : extractibles à chaud par la façade (voir backplane, chapitre 16).
- **Ventilation redondante** et flux d'air contraint (couloirs chaud/froid en datacenter).

#### Gestion hors-bande (out-of-band) : iDRAC / iLO / IPMI

C'est un point essentiel et spécifique au monde serveur. Un **contrôleur de gestion (BMC, Baseboard Management Controller)** est un **mini-ordinateur indépendant intégré au serveur**, avec sa **propre adresse réseau** et sa propre alimentation de veille. Il fonctionne **même si le serveur principal est éteint ou planté**.

- **iDRAC** (Dell), **iLO** (HPE) : interfaces propriétaires.
- **IPMI** : le standard ouvert sous-jacent.

Ce qu'il permet, à distance, sans se déplacer :

- allumer / éteindre / redémarrer le serveur ;
- voir l'écran depuis le POST (console distante / KVM-over-IP) ;
- monter une image ISO pour **réinstaller l'OS à distance** ;
- lire l'état matériel (températures, ventilateurs, pannes de disque).

> **🔧 Cas concret (admin sys)**
> Un serveur ne répond plus à 3 h du matin. Via l'iDRAC/iLO (accessible indépendamment de l'OS), l'administrateur voit l'écran bloqué au démarrage, force un redémarrage, entre dans l'UEFI, corrige — depuis chez lui. C'est tout l'intérêt du hors-bande.

> **🔒 Sécurité**
> Un BMC est une cible de choix : il a un contrôle total sur le serveur et tourne en permanence. On ne l'expose **jamais** sur Internet, on le place sur un **réseau d'administration isolé (VLAN dédié)**, on change les identifiants par défaut et on maintient son firmware à jour. Un iLO/iDRAC compromis = serveur entièrement compromis, sous l'OS.

---

### 16. RAID matériel vs logiciel, HBA, backplane

#### Les niveaux de RAID

Le RAID assemble plusieurs disques pour la sécurité et/ou la performance.

| Niveau | Principe | Tolérance de panne | Remarque |
|---|---|---|---|
| **RAID 0** | Données réparties (striping) | ❌ Aucune | 1 disque mort = tout perdu. Rapide mais risqué. |
| **RAID 1** | Miroir (copie identique) | 1 disque | Simple et sûr, capacité divisée par 2. |
| **RAID 5** | Données + 1 parité (3+ disques) | 1 disque | Reconstruction longue et risquée sur gros disques. |
| **RAID 6** | Double parité (4+ disques) | 2 disques | Plus sûr que RAID 5 pour les grosses grappes. |
| **RAID 10** | Miroir + striping (4+ disques) | 1 par paire | Rapide *et* sûr, bon compromis. |

> **🎯 À retenir — LE point capital**
> **Un RAID n'est PAS une sauvegarde.** Il protège contre la *panne matérielle d'un disque*, pas contre la suppression accidentelle, un ransomware, une corruption logique ou un incendie — qui se répliquent instantanément sur toute la grappe. Une vraie sauvegarde est *séparée*, *versionnée*, et idéalement *hors site et déconnectée*.

#### RAID matériel vs logiciel : une distinction qui change la gestion

| | **RAID matériel** | **RAID logiciel** |
|---|---|---|
| Géré par | Une **carte contrôleur RAID** dédiée | L'OS (mdadm Linux, Storage Spaces Windows, **ZFS**, Btrfs) |
| Charge CPU | Déportée sur la carte | Sur le CPU de la machine (négligeable aujourd'hui) |
| Cache + batterie (BBU) | Souvent, protège le cache en cas de coupure | Géré autrement (journal, onduleur) |
| Portabilité | Liée au modèle de contrôleur (panne = même modèle requis) | Lisible sur n'importe quelle machine compatible |
| Visibilité des disques | Le contrôleur masque souvent l'état réel | L'OS voit chaque disque (SMART direct) |

> **🎯 À retenir**
> Le RAID **logiciel moderne** (ZFS en tête) est devenu très répandu, y compris en entreprise et en homelab : il offre intégrité des données (détection de corruption silencieuse), snapshots et portabilité, sans dépendre d'une carte propriétaire. Le RAID **matériel** reste fréquent sur les serveurs de marque pour le hot-swap intégré et le cache protégé par batterie.

#### HBA : le composant souvent confondu avec un contrôleur RAID

Un **HBA** (Host Bus Adapter) est une carte qui connecte des disques (SAS/SATA) à la machine **en les présentant directement à l'OS**, sans couche RAID intermédiaire. C'est précisément ce qu'on veut pour un RAID **logiciel** comme ZFS, qui a besoin d'un accès brut à chaque disque (et à son SMART).

> **⚠️ Erreur fréquente**
> Utiliser une carte RAID matériel configurée en RAID pour faire tourner ZFS par-dessus : ZFS perd la vision directe des disques et son intégrité est compromise. La bonne pratique est un **HBA** (ou une carte RAID basculée en mode « IT »/pass-through) qui expose les disques tels quels.

#### Backplane

Le **backplane** (fond de panier) est la carte à l'arrière des baies de disques en façade d'un serveur. Les disques hot-swap s'y enfichent directement : il distribue alimentation et données (SAS/SATA) et permet l'extraction à chaud sans câbler chaque disque individuellement. C'est ce qui rend possible le remplacement d'un disque défaillant en quelques secondes, sans éteindre la machine.

> **🔧 Cas concret**
> Une LED orange s'allume sur un tiroir de disque en façade. L'admin extrait le disque à chaud, insère un disque neuf : le backplane et le contrôleur lancent automatiquement la **reconstruction** (rebuild) de la grappe RAID, sans interruption de service. Pendant le rebuild, la grappe est vulnérable à une seconde panne — d'où l'intérêt du RAID 6 sur les grosses grappes.

---

### 17. Stockage en réseau : DAS, NAS, SAN

Trois façons de présenter du stockage, souvent confondues.

- **DAS** (Direct Attached Storage) : disques branchés *directement* à une machine (disque externe, baie reliée par SAS). Simple, non partagé sur le réseau.
- **NAS** (Network Attached Storage) : un boîtier de stockage *sur le réseau* qui partage des **fichiers** (SMB, NFS). Idéal maison/PME, accès multi-utilisateurs.
- **SAN** (Storage Area Network) : un réseau **dédié** haute performance (Fibre Channel ou iSCSI) qui présente du stockage *en mode bloc* — la machine le voit comme un disque local. Pour la virtualisation à grande échelle.

Distinction clé : **NAS = niveau fichier**, **SAN = niveau bloc**. Un NAS dit « voici un dossier partagé » ; un SAN dit « voici un disque, fais-en ce que tu veux ».

- **Snapshots** : « photos » instantanées de l'état du stockage pour revenir en arrière. Utiles mais ne remplacent pas une sauvegarde externe.

> **🔧 Cas concret (cyber)**
> Une entreprise touchée par un ransomware avait un NAS en RAID 6 « pour la sécurité ». Le rançongiciel a chiffré les fichiers, répliqués aussitôt sur toute la grappe. Sans sauvegarde déconnectée (*air gap*) ou hors site immuable, tout était perdu. La règle **3-2-1** (3 copies, 2 supports, 1 hors site) et des snapshots immuables auraient sauvé les données. RAID ≠ sauvegarde, en grandeur réelle.

---

### 18. La baie : switch, routeur, firewall, PDU, brassage

Les équipements d'une armoire réseau :

- **Switch** : aiguille le trafic *au sein* d'un réseau local (relie les machines). Notion détaillée en Partie 9.
- **Routeur** : relie *plusieurs réseaux* (typiquement le LAN à Internet).
- **Pare-feu (firewall)** : filtre le trafic selon des règles ; souvent une appliance dédiée.
- **Patch panel** : panneau où aboutissent les câbles fixes du bâtiment, reliés aux switchs par de courts cordons (**brassage**). Détaillé au chapitre 38.
- **Onduleur (UPS)** : batterie de secours (chapitre 42).
- **PDU** (Power Distribution Unit) : multiprise professionnelle de baie, parfois pilotable à distance (redémarrer électriquement un équipement bloqué — utile combiné au hors-bande du chapitre 15).

> **🎯 À retenir**
> Le **brassage** via patch panel distingue une baie pro propre d'un nid de câbles : les câbles fixes du bâtiment ne bougent jamais, on ne touche qu'aux cordons courts en façade. Une PDU pilotable + un BMC (iDRAC/iLO) permettent de relancer à distance un équipement totalement figé, sans déplacement.

---
## Partie 5 — Écrans et affichage

---

### 19. Comprendre un écran : résolution, densité, dalle

#### Les caractéristiques

- **Taille** : diagonale en pouces.
- **Résolution** : nombre de pixels (1920 × 1080…).
- **Densité (PPI)** : pixels par pouce — c'est *elle*, pas la résolution seule, qui détermine la netteté perçue. Un 4K en 27" est très net ; le même 4K en 65" l'est beaucoup moins vu de près.
- **Luminosité** (cd/m² ou nits) : cruciale en pièce lumineuse et pour le HDR.
- **Contraste** : écart entre le noir le plus profond et le blanc le plus clair.

#### Résolutions et formats

| Nom | Pixels (16:9) |
|---|---|
| Full HD | 1920 × 1080 |
| QHD | 2560 × 1440 |
| 4K / UHD | 3840 × 2160 |
| 5K | 5120 × 2880 |
| 8K | 7680 × 4320 |

Formats (ratio) : **16:9** (universel), **16:10** (plus haut, apprécié en bureautique/code), **21:9** (ultrawide, immersif), **32:9** (super ultrawide, deux 16:9 côte à côte).

#### Types de dalles

| Dalle | Forces | Faiblesses | Usage idéal |
|---|---|---|---|
| **TN** | Très rapide, pas chère | Couleurs/angles médiocres | Jeu compétitif petit budget |
| **IPS** | Excellentes couleurs et angles | Contraste moyen, « IPS glow » | Polyvalent, création, bureautique |
| **VA** | Très bon contraste | Flou en mouvement possible | Films, usage mixte |
| **OLED** | Noirs parfaits, ultra-rapide | Risque de marquage (burn-in), prix | Cinéma, création haut de gamme |
| **QD-OLED** | OLED + couleurs plus vives | Prix, jeunesse | Très haut de gamme couleur |
| **Mini-LED** | Très lumineux, bon HDR (LCD amélioré) | Halos lumineux (blooming) | HDR lumineux sans risque de burn-in |
| **Micro-LED** | Avantages OLED sans les défauts | Hors de prix, quasi inexistant | Futur / vitrine |

> **⚠️ Erreur fréquente**
> Confondre **OLED** (chaque pixel s'éclaire seul → noir parfait) et **Mini-LED** (LCD avec rétroéclairage zoné → très lumineux mais pas de noir parfait). Ce ne sont pas des variantes : l'OLED éteint le *pixel*, le Mini-LED éteint des *zones* de rétroéclairage.

> **🔧 Cas concret**
> Burn-in d'un OLED utilisé comme écran de bureau : la barre des tâches ou un logo statique finit par s'imprimer. Pour une interface fixe toute la journée, l'IPS ou le Mini-LED sont plus sûrs.

> **🎯 À retenir**
> La vraie question de netteté n'est pas « combien de pixels » mais « combien de pixels **par pouce** » à la distance d'utilisation. Et plus la résolution monte, plus le GPU travaille : viser une résolution que la machine peut réellement alimenter.

---

### 20. Fréquence, fluidité, VRR et latence

La **fréquence (Hz)** = images affichées par seconde. La différence 60 → 120 Hz est très visible (souris, défilement, jeu) ; au-delà, les gains diminuent.

- **60 / 75 / 120 / 144 / 240 / 360+ Hz** : de plus en plus fluide.
- **Tearing** : image « déchirée » quand le GPU et l'écran ne sont pas synchronisés.
- **VRR** (Variable Refresh Rate) : l'écran adapte sa fréquence à celle du GPU en temps réel. Marques : **FreeSync** (AMD), **G-Sync** (NVIDIA).
- **Temps de réponse** (ms) : rapidité de changement de couleur d'un pixel (flou de mouvement).
- **Input lag** : délai entre l'action (clic, touche) et l'affichage. Différent du temps de réponse ; critique en jeu.

> **⚠️ Erreur fréquente — le grand classique**
> « Écran 144 Hz mais Windows reste à 60 Hz. » Trois causes : (1) fréquence non réglée dans les paramètres d'affichage, (2) le **câble** ne supporte pas 144 Hz à cette résolution, (3) le **port/version** est limité (un vieux HDMI). C'est traité comme une panne complète au chapitre 47.

---

### 21. HDR, couleurs et calibration

#### HDR : la plage dynamique

Le **HDR** élargit l'écart entre zones sombres et claires. Formats : **HDR10** (base ouverte), **HDR10+** et **Dolby Vision** (métadonnées dynamiques, image par image), certification **VESA DisplayHDR** (400, 600, 1000…).

> **⚠️ Erreur fréquente**
> Acheter un écran « HDR » certifié **DisplayHDR 400** en croyant à un vrai HDR. C'est souvent un faux HDR : sans luminosité élevée (600+ nits) ni bon contraste (idéalement Mini-LED ou OLED), l'effet est négligeable, parfois pire que le SDR.

#### Espaces colorimétriques

- **sRGB** : standard du web et de la bureautique.
- **DCI-P3** : plus large, cinéma et HDR.
- **Adobe RGB** : impression / photo pro.

La **calibration** (sonde + logiciel) ajuste l'écran pour des couleurs fidèles — indispensable en photo/vidéo pro.

> **🔧 Cas concret (création)**
> Un graphiste constate que ses couleurs « changent » entre son écran et le rendu client. Cause : écran non calibré et/ou espace inadapté. Une sonde de calibration et le réglage sur sRGB règlent l'écart.

---

### 22. TV vs écran PC

| Critère | Écran PC | TV |
|---|---|---|
| **Input lag** | Faible (réactif) | Souvent élevé (traitement d'image) |
| **Traitement d'image** | Minimal | Lourd (lissage, upscaling) |
| **Densité de pixels** | Élevée (vue de près) | Faible (vue de loin) |
| **Texte net** | Oui | Parfois flou (chroma 4:2:0) |
| **Tuner / son intégré** | Non | Oui |

- **Chroma subsampling** : les TV compressent souvent l'info de couleur (4:2:0), rendant le **texte fin flou** en usage PC. Un écran PC, ou une TV en **mode PC (4:4:4)**, évite ça.
- **HDMI ARC/eARC** : la TV renvoie le son vers une barre de son/ampli (chapitre 33).
- **Smart TV** : OS intégré (apps), mais questions de confidentialité et de durée des mises à jour.

> **🎯 À retenir**
> Utiliser une TV comme écran PC : activer le **mode Jeu/PC** (réduit le lag), vérifier le **chroma 4:4:4** (texte net), accepter une densité faible de près. À l'inverse, un écran PC fait une piètre TV (pas de tuner, souvent pas de son).

---

## Partie 6 — Connectiques vidéo

Application directe du chapitre 2 : un connecteur, un câble et un protocole sont trois choses distinctes.

---

### 23. VGA et DVI (l'héritage analogique)

#### VGA

Connecteur trapèze bleu à 15 broches, **analogique**, conçu pour les écrans cathodiques. Qualité qui se dégrade avec la longueur et la résolution (image floue possible au-delà du Full HD). On le croise sur de vieux projecteurs et matériels pro. À éviter en achat neuf.

#### DVI

La transition VGA → HDMI, avec plusieurs variantes piégeuses : **DVI-A** (analogique), **DVI-D** (numérique), **DVI-I** (les deux). **Single link / Dual link** : le dual link ajoute des broches pour de plus hautes résolutions.

> **⚠️ Erreur fréquente**
> Vouloir convertir du DVI-D (numérique pur) vers du VGA (analogique) avec un adaptateur *passif* : impossible, il n'y a pas de signal analogique à récupérer. Il faut un convertisseur **actif**. La distinction analogique/numérique (chapitre 1) explique pourquoi.

---

### 24. HDMI (jusqu'à 2.2 / Ultra96)

Le standard roi du salon. **À la fois connecteur et protocole** (vidéo + audio).

#### Les versions — la version compte plus que le mot « HDMI »

| Version | Bande passante | Capacités typiques |
|---|---|---|
| HDMI 1.4 | ~10 Gb/s | 4K à 30 Hz |
| HDMI 2.0 | 18 Gb/s | 4K à 60 Hz, HDR |
| HDMI 2.1 | 48 Gb/s | 4K à 120 Hz, 8K, VRR, eARC |
| **HDMI 2.2** | **96 Gb/s** | 4K à 240 Hz, 8K à 60 Hz en 4:4:4, jusqu'à 12K/16K |

La version 2.2 de la spécification HDMI a été publiée le 25 juin 2025, portant la bande passante maximale à 96 Gb/s et prenant en charge des résolutions allant jusqu'à 16K à 60 Hz, ainsi que la 4K à 240 Hz et la 8K à 60 Hz en 4:4:4 avec 10 ou 12 bits de couleur.

#### Les câbles — la nouveauté Ultra96

Pour exploiter le HDMI 2.2, le câble doit suivre. Le câble « Ultra High Speed » existant gère jusqu'à 48 Gb/s ; pour les 96 Gb/s du HDMI 2.2, un nouveau câble certifié « Ultra96 » est nécessaire — sans lui, les pleines capacités du standard ne sont pas accessibles. « Ultra96 » est un nom de fonctionnalité que les fabricants sont encouragés à utiliser pour indiquer qu'un produit prend en charge un maximum de 64, 80 ou 96 Gb/s.

Bon réflexe d'achat : pour de la 4K/8K classique, un câble **Ultra High Speed (48 Gb/s)** suffit ; on ne paie l'**Ultra96** que pour de la 8K/16K non compressée ou de la 4K à très haute fréquence.

> **🎯 À retenir (veille, pas encore courant)**
> HDMI 2.2 est une norme **très récente** (publiée mi-2025) : les premiers appareils compatibles arrivent progressivement et resteront minoritaires pendant un temps, comme ce fut le cas lors de l'adoption du HDMI 2.1. À traiter comme une **information de veille** pour anticiper un achat durable, pas comme un standard déjà répandu. En 2026, l'immense majorité du matériel reste en HDMI 2.0/2.1.

#### Fonctions à connaître

- **ARC / eARC** : renvoi du son de la TV vers un ampli/barre de son. L'eARC gère l'audio non compressé (Dolby Atmos…).
- **CEC** : une seule télécommande pilote plusieurs appareils.
- **Câbles actifs / passifs** : au-delà de quelques mètres en haut débit, câble certifié ou actif (avec électronique).

> **⚠️ Erreur fréquente — le piège marketing « HDMI 2.1 »**
> Le standard autorise un support *partiel* : un appareil peut afficher « HDMI 2.1 » sans gérer le 4K 120 Hz ni le VRR. Le numéro de version ne garantit **pas** les fonctions. On vérifie les fonctions *réellement listées*, pas le seul chiffre. Le même piège guettera « HDMI 2.2 ».

> **🔧 Cas concret (gaming)**
> Console récente bloquée en 4K 60 Hz sur une TV « HDMI 2.1 » : souvent le câble n'est pas Ultra High Speed, ou le **port HDMI précis** utilisé ne gère pas les fonctions 2.1 (toutes les prises d'une même TV ne se valent pas). On change de câble, puis de port.

---

### 25. DisplayPort

Le pendant informatique de HDMI, souvent supérieur sur PC.

| Version | Capacités typiques |
|---|---|
| DP 1.2 | 4K à 60 Hz |
| DP 1.4 | 4K à 120 Hz, 8K, HDR (souvent avec compression DSC) |
| DP 2.0 / 2.1 | Jusqu'à ~80 Gb/s, 8K+ à haute fréquence |

- **MST** (Multi-Stream Transport) : chaîner plusieurs écrans sur un port (daisy-chain) ou via un hub.
- **DSC** (Display Stream Compression) : compression quasi sans perte permettant des résolutions/fréquences plus élevées sur une bande passante donnée.
- **Adaptateurs** : vers HDMI/DVI/VGA, un adaptateur **actif** est souvent nécessaire (surtout vers l'analogique ou en multi-écrans).

> **🎯 À retenir**
> Pour du PC en haute fréquence (144 Hz+), **DisplayPort est généralement le meilleur choix** : c'est la sortie reine des cartes graphiques et il gère souvent mieux ces fréquences que le HDMI de génération équivalente. Note : depuis HDMI 2.2 (96 Gb/s), le HDMI repasse devant le DisplayPort 2.1 (~80 Gb/s) en bande passante brute.

---

### 26. Vidéo sur USB-C et choix d'une connectique vidéo

Ici la distinction connecteur/protocole devient vitale : un port **USB-C** peut transporter de la vidéo… ou pas.

- **DisplayPort Alt Mode** : le mode qui fait passer un signal DisplayPort dans le câble USB-C. C'est *lui* qui permet de brancher un écran en USB-C. Sans ce mode, **aucune image**, quel que soit le câble.
- **HDMI Alt Mode** : équivalent pour HDMI, rare.
- **Charge + vidéo + données simultanées** : tout l'intérêt de l'USB-C (un dock alimente le PC, affiche l'écran et connecte les périphériques par un câble).

> **⚠️ Erreur fréquente — cause n°1 des écrans USB-C qui restent noirs**
> Tous les ports USB-C ne savent **pas** sortir de la vidéo. Il faut que le port supporte le **DisplayPort Alt Mode** (souvent un petit logo DP ou un éclair Thunderbolt à côté de la prise). Beaucoup de portables n'ont l'Alt Mode que sur *un seul* de leurs ports USB-C. Un port « données seulement » n'affichera jamais d'image.

#### Choisir sa connectique vidéo, en résumé

| Besoin | Choix recommandé |
|---|---|
| PC, haute fréquence (144 Hz+) | DisplayPort |
| Salon, TV, console | HDMI (version selon résolution/fréquence) |
| Portable/dock, un seul câble | USB-C (Alt Mode) ou Thunderbolt |
| 8K/16K non compressé, 4K très haute fréquence | HDMI 2.2 + câble Ultra96 |

> **🔧 Cas concret**
> Dock USB-C dont l'écran ne s'affiche pas : voir le diagnostic complet « dock qui ne sort pas la vidéo » au chapitre 47. En une phrase : le port hôte doit gérer l'Alt Mode (ou Thunderbolt), et le dock doit en tenir compte.

---
## Partie 7 — USB, Thunderbolt et périphériques

L'une des parties les plus densifiées, car c'est le terrain où la confusion connecteur/câble/protocole fait le plus de dégâts — et où les standards ont récemment beaucoup bougé.

---

### 27. Comprendre l'USB : connecteurs et standards

L'USB mélange deux choses qu'il faut séparer : **formes** et **vitesses**.

#### Les formes (connecteurs)

- **USB-A** : le rectangle classique.
- **USB-B** : carré (imprimantes, certains périphériques).
- **Mini-USB** / **Micro-USB** : anciens, sur vieux appareils et téléphones d'avant l'USB-C.
- **USB-C** : ovale, réversible, le standard actuel.

#### Les vitesses (standards) — et le chaos des renommages

| Standard | Débit | Ancien(s) nom(s) |
|---|---|---|
| USB 2.0 | 480 Mb/s | Hi-Speed |
| USB 3.0 / 3.1 Gen 1 / 3.2 Gen 1 | 5 Gb/s | SuperSpeed |
| USB 3.1 Gen 2 / 3.2 Gen 2 | 10 Gb/s | SuperSpeed+ |
| USB 3.2 Gen 2x2 | 20 Gb/s | — |
| USB4 | **20 ou 40 Gb/s** | « USB 20Gbps » / « USB 40Gbps » (intègre Thunderbolt 3) |
| **USB4 Version 2.0** | **80 Gb/s** (120 Gb/s asymétrique) | « USB 80Gbps » |

Le même débit de 5 Gb/s porte ainsi trois noms (USB 3.0, 3.1 Gen 1, 3.2 Gen 1), source de confusion entretenue par les renommages successifs de l'USB-IF. Attention aussi à ne pas réduire « USB4 » à 40 Gb/s : la première génération d'USB4 existe en **20 Gb/s** *ou* **40 Gb/s** selon les implémentations ; seule la **Version 2.0** monte à 80 Gb/s (et 120 Gb/s en mode asymétrique).

> **🎯 À retenir**
> La **forme** (USB-A, USB-C) ne dit pas la **vitesse**. Un port USB-C peut n'être que de l'USB 2.0 ; un port USB-A peut faire 10 Gb/s. Indice visuel fréquent : l'intérieur **bleu** d'un port USB-A signale (en général) de l'USB 3.x.

> **⚠️ Erreur fréquente**
> Transfert très lent sur un disque « USB 3 » : souvent branché sur un port USB 2.0, ou avec un câble USB 2.0. Le maillon le plus lent (port, câble, disque) impose sa vitesse — le principe du maillon faible, appliqué à l'USB.

---

### 28. USB-C, USB4 et USB Power Delivery

#### USB-C : un connecteur, des capacités très variables

Ce qu'un câble/port USB-C *peut* faire, indépendamment de sa forme :

- **Données** : de 480 Mb/s (USB 2.0) à 80 Gb/s (USB4 v2).
- **Charge** : de quelques watts à 240 W.
- **Vidéo** : seulement si DisplayPort Alt Mode présent (chapitre 26).
- **Thunderbolt** : seulement sur ports/câbles certifiés (chapitre 29).

> **🎯 À retenir — l'idée centrale de l'USB-C**
> Le connecteur USB-C est une **promesse de forme**, pas de fonction. Avant d'attendre vidéo, charge rapide ou haut débit, vérifier que **le câble ET le port** supportent cette fonction précise.

#### USB4 et USB4 Version 2.0 (80 Gb/s, mode asymétrique 120 Gb/s)

USB4 unifie l'écosystème en s'appuyant sur Thunderbolt 3, avec tunnelisation du DisplayPort et du PCIe sur le connecteur USB-C. Sa première génération existe en 20 ou 40 Gb/s. La **Version 2.0**, publiée par l'USB-IF le 18 octobre 2022 (en même temps que la spécification USB-C 2.2 et l'USB PD 3.1), double le débit symétrique à 80 Gb/s et introduit un **mode asymétrique** atteignant jusqu'à 120 Gb/s dans un sens (et 40 Gb/s dans l'autre).

Le principe de l'asymétrie : au lieu de répartir 80 Gb/s en 40 montants / 40 descendants, le système peut réallouer dynamiquement la bande passante — par exemple trois voies en émission et une en réception — pour atteindre 120 Gb/s vers un écran haute résolution tout en gardant 40 Gb/s en retour. Très utile pour piloter de l'affichage 8K/16K ou un eGPU.

Cette montée à 80 Gb/s repose sur un nouvel encodage du signal, le **PAM-3**, qui transmet plus de bits par cycle tout en restant compatible avec des câbles USB-C certifiés.

#### USB Power Delivery (PD) — jusqu'à 240 W

Au branchement, appareil et chargeur **négocient** tension et courant. L'USB-PD propose des paliers : 5 V, 9 V, 15 V, 20 V, puis en **PD 3.1** jusqu'à 28 V, 36 V et 48 V pour atteindre **240 W** (en mode EPR, Extended Power Range).

| Puissance | Usage typique |
|---|---|
| 30 W | Téléphone, petite tablette |
| 65 W | Ultraportable, gros téléphone |
| 100 W | PC portable performant |
| 140 W | Station mobile |
| **240 W** | Portables gaming/pro très gourmands (PD 3.1 EPR) |

#### Les logos USB-IF à reconnaître

L'USB-IF a introduit des logos de certification pour lever l'ambiguïté. Sur l'emballage des câbles, on trouve désormais des mentions claires de débit (« USB 40 Gbps », « USB 80 Gbps ») et de puissance (**« 60 W »** ou **« 240 W »**). Ces deux chiffres de puissance correspondent aux deux familles de câbles :

- **60 W (3 A)** : un câble USB-C standard, **sans puce e-mark** obligatoire.
- **240 W (5 A)** : un câble **e-marked** (avec puce d'identification) requis au-delà de 60 W, signalé par le logo « 240 W ».

> **⚠️ Erreur fréquente — « mon chargeur 240 W ne charge qu'à 60 W »**
> La puissance annoncée du chargeur est un **plafond** (chapitre 1). Trois maillons décident de la puissance réelle : le **chargeur** (ce qu'il peut donner), le **câble** (un câble non e-marked bride à 60 W), et l'**appareil** (ce que sa négociation autorise). Un câble basique « charge seule » bride tout l'ensemble. Le logo « 240 W » sur le câble est le signe qu'il est e-marked.

> **🔧 Cas concret (support)**
> « Mon PC charge lentement avec le chargeur du collègue. » Vérifier les trois maillons : chargeur de puissance suffisante ? câble e-marked (logo 240 W) ou bridé à 60 W ? port du PC qui accepte l'entrée d'alimentation ? Étiqueter ses câbles évite des heures de diagnostic.

---

### 29. Thunderbolt (jusqu'à Thunderbolt 5)

Le « couteau suisse » de la connectique, qui emprunte le connecteur USB-C.

| Version | Débit | Puissance (charge) | Particularité |
|---|---|---|---|
| Thunderbolt 3 | 40 Gb/s | jusqu'à 100 W selon l'implémentation | A inspiré l'USB4 |
| Thunderbolt 4 | 40 Gb/s | jusqu'à 100 W (généralement) | Base de l'USB4 v1 |
| **Thunderbolt 5** | **80 Gb/s** bidirectionnel | **jusqu'à 240 W** selon l'appareil (140 W requis) | **120 Gb/s** dans un sens (Bandwidth Boost) |

Thunderbolt 5, annoncé par Intel le 12 septembre 2023 (premiers appareils à partir de 2024, dont les Mac fin 2024), offre 80 Gb/s comme l'USB4 v2, avec un mode asymétrique « Bandwidth Boost » garantissant jusqu'à 120 Gb/s dans un sens sur **tous** les appareils certifiés (et non au cas par cas). Côté charge, c'est lui qui introduit le 240 W (via l'USB PD 3.1, selon l'appareil et le câble) ; Thunderbolt 3 et 4 plafonnaient à 100 W. Un monteur vidéo branché sur un eGPU Thunderbolt 5 bénéficie ainsi de 120 Gb/s vers la carte tout en conservant 40 Gb/s au retour.

Comme Thunderbolt 3/4, il fait passer des **lignes PCIe dans le câble** (PCIe over cable), ce qui débloque des usages impossibles en USB simple :

- **Docks** complets (un câble pour écrans, réseau, USB, charge) ;
- **eGPU** (carte graphique externe) ;
- **stockage NVMe externe** ultra-rapide ;
- **chaînage** de plusieurs périphériques (daisy-chain).

#### Thunderbolt vs USB-C, la clarification

- **USB-C** = la forme du connecteur.
- **Thunderbolt** = un protocole haut de gamme *utilisant* cette forme.

Tout port Thunderbolt est physiquement un USB-C et reste compatible USB-C ; l'inverse est faux. Le **logo éclair ⚡** à côté d'un port indique Thunderbolt (donc vidéo + données rapides + charge, en principe).

> **🔒 Sécurité — l'angle DMA, à connaître**
> Parce que Thunderbolt expose le **PCIe**, un périphérique malveillant branché peut tenter un accès **DMA** (Direct Memory Access) : lire ou écrire directement dans la mémoire de la machine, contournant l'OS — pour voler des clés, des mots de passe, ou injecter du code. C'est la base des attaques type « Thunderspy ». Détaillé au chapitre 44 ; à retenir ici : un port aussi puissant qu'un Thunderbolt est aussi une surface d'attaque puissante.

> **⚠️ Erreur fréquente**
> Acheter un câble « USB-C » bas de gamme pour un dock ou un eGPU Thunderbolt : il faut un câble **certifié Thunderbolt** (souvent marqué d'un éclair et d'un chiffre). Un câble de charge ne fera jamais passer 40-80 Gb/s ni du PCIe.

---

### 30. Périphériques, hubs et docks

- **Clavier / souris** : filaire (USB, latence minimale), Bluetooth, ou dongle radio 2,4 GHz dédié (plus réactif que le Bluetooth pour le jeu).
- **Webcam** : USB ; la qualité dépend du capteur, pas seulement de la résolution annoncée.
- **Imprimante / scanner** : USB-B, Ethernet, Wi-Fi (chapitre 43).
- **Disque externe** : vitesse réelle = type (HDD/SSD) ∩ standard USB du maillon le plus lent.
- **Hub USB** : multiplie les ports, qui **partagent** la bande passante et l'alimentation du port hôte. Un hub **alimenté** (prise propre) est nécessaire pour des périphériques gourmands.
- **Dock USB-C / Thunderbolt** : transforme un port en station complète (écrans, réseau, USB, charge). Les capacités dépendent du **port hôte** : Alt Mode pour la vidéo, Thunderbolt pour le multi-écrans haute résolution + débit.

> **⚠️ Erreur fréquente**
> Disque externe gourmand sur un hub non alimenté déjà chargé : pas assez de courant, le disque se déconnecte ou n'apparaît pas. Solution : hub alimenté ou branchement direct.

> **🔧 Cas concret**
> Dock affichant un seul écran alors qu'on en veut deux : un dock **USB-C simple (Alt Mode)** ne porte qu'un flux DisplayPort ; le multi-écrans haute résolution exige un dock **Thunderbolt** (ou MST + DSC selon les cas). Le port hôte et le type de dock décident, pas le nombre de prises présentes sur le dock.

---
## Partie 8 — Audio

---

### 31. Jack, audio numérique et DAC

#### Jack 3,5 mm

Prise audio analogique universelle. Le nombre d'anneaux change tout :

- **TRS** (2 anneaux) : stéréo *sans* micro.
- **TRRS** (3 anneaux) : stéréo *avec* micro.

Deux câblages TRRS incompatibles existent : **CTIA** (standard actuel) et **OMTP** (ancien). Croisés, le micro ne marche pas ou le son est déformé.

#### Analogique, numérique et DAC

- **Signal analogique** : la variation de tension qui *est* le son (vers le casque).
- **DAC** (Digital-to-Analog Converter) : convertit le numérique de l'appareil en analogique. Toute sortie casque en contient un.
- **ADC** : l'inverse, pour numériser un micro.
- **Carte son / interface audio** : DAC et ADC de meilleure qualité que ceux de base.

> **🎯 À retenir**
> Compter les anneaux : 2 = pas de micro (TRS), 3 = micro (TRRS). Et la qualité du **DAC** compte souvent plus que la résolution du fichier : un bon DAC externe transforme le rendu d'un casque.

> **🔧 Cas concret**
> Casque-micro dont l'audio marche mais pas le micro sur un appareil : incompatibilité CTIA/OMTP, ou port qui n'accepte que du TRS. Un adaptateur CTIA↔OMTP ou en Y (deux prises séparées) résout.

---

### 32. XLR, alimentation fantôme et audio pro

- **XLR** : connecteur rond verrouillable à 3 broches, **symétrique** : il annule les parasites sur de longues distances. D'où son usage en studio et sur scène.
- **Micro dynamique** : robuste, sans alimentation, pour la scène et les voix fortes.
- **Micro statique (condensateur)** : sensible et détaillé, **nécessite une alimentation fantôme 48 V** (notée +48V / P48).
- **Alimentation fantôme 48 V** : tension envoyée par l'interface/la table *dans le câble XLR* pour alimenter le micro statique.
- **Interface audio / table / préampli** : amplifient et numérisent le signal pour l'ordinateur.

> **⚠️ Erreur fréquente**
> Brancher un micro statique sans activer le +48V : aucun son ou signal très faible. Un grand classique du home-studio. Inversement, le 48V peut endommager certains matériels sensibles (anciens micros à ruban) — d'où l'interrupteur dédié.

---

### 33. Bluetooth et audio du salon

#### Bluetooth audio

- **Codecs** : SBC (base), AAC (Apple), aptX / aptX HD (Qualcomm/Android), LDAC (Sony, haute résolution).
- **Latence** : le Bluetooth introduit un délai — gênant en jeu et en vidéo (lèvres désynchronisées).
- **Multipoint** : connexion à deux appareils à la fois.

> **⚠️ Erreur fréquente**
> Vouloir jouer ou produire de la musique en Bluetooth : la latence le rend pénible. Pour le jeu compétitif et la production, filaire ou dongle radio dédié.

#### Audio du salon : RCA, optique, ARC/eARC

- **RCA** : fiches rouge/blanc, audio analogique stéréo.
- **Toslink (optique)** : audio **numérique** par fibre optique (lumière), insensible aux parasites électriques.
- **SPDIF** : le *protocole* audio numérique, en optique (Toslink) ou coaxial.
- **HDMI ARC/eARC** : la TV renvoie le son vers un ampli/barre de son ; l'**eARC** gère les formats non compressés (Dolby Atmos).

> **🎯 À retenir**
> Pour relier une TV à une barre de son aujourd'hui : **HDMI eARC** (qualité maximale + télécommande unique via CEC). L'optique reste un bon plan B mais limité pour les formats surround récents.

> **🔧 Cas concret**
> Barre de son en optique qui ne reçoit pas le surround d'un service de streaming : l'optique ne porte pas les formats les plus récents. Passer en HDMI eARC débloque le Dolby Atmos, si TV, câble et barre le supportent tous les trois.

---

## Partie 9 — Réseau physique et télécom

Partie fortement densifiée : c'est le socle du support, de l'admin sys et de la cyber.

---

### 34. RJ45, Ethernet et catégories de câbles

**RJ45 = connecteur** (prise carrée à clip) ; **Ethernet = protocole** qui y circule.

Le câble est fait de **paires torsadées** (les torsades réduisent la diaphonie et les interférences). Sa catégorie fixe le débit maximal :

| Catégorie | Débit max | Distance | Remarque |
|---|---|---|---|
| **Cat5e** | 1 Gb/s | 100 m | Le minimum aujourd'hui |
| **Cat6** | 1 Gb/s (10 Gb/s ≤ 55 m) | 100 m | Excellent choix domestique |
| **Cat6a** | 10 Gb/s | 100 m | 10 Gb/s sur pleine longueur |
| **Cat7** | 10 Gb/s (blindé) | 100 m | Connecteur parfois non standard |
| **Cat8** | 25–40 Gb/s | 30 m | Datacenter uniquement |

#### Blindage

- **UTP** : non blindé (le plus courant, suffit chez soi).
- **FTP / STP** : blindé, pour les environnements à fortes interférences (industriel, proximité de câbles électriques). Un câble blindé exige une mise à la terre correcte pour être efficace.

#### Vitesses négociées et auto-négociation

Deux équipements Ethernet **négocient** automatiquement la vitesse commune la plus élevée (100 Mb/s, 1 Gb/s, 2,5 Gb/s, 10 Gb/s). Si la négociation échoue (câble abîmé, paire coupée), la liaison retombe souvent à une vitesse basse.

> **🎯 À retenir**
> Pour une installation domestique, du **Cat6 UTP** est l'optimum : 1 Gb/s partout, prêt pour le 2,5/10 Gb/s sur longueurs raisonnables. Inutile de surpayer du Cat8 (datacenter). Le débit réel = le plus lent de la chaîne : carte réseau, câble, switch, port.

> **🔧 Cas concret**
> Liaison « fibre 2 Gb/s » qui plafonne à 1 Gb/s en filaire : vieux câble Cat5 (non e), ou carte réseau/port limité à 1 Gb/s. Le traitement complet « Ethernet bloqué à 100 Mb/s ou 1 Gb/s » est au chapitre 47.

---

### 35. PoE en détail

Le **PoE (Power over Ethernet)** fait transiter **l'alimentation électrique en plus des données** sur le câble réseau. Un seul câble alimente *et* connecte un appareil : caméra IP, point d'accès Wi-Fi au plafond, téléphone IP, serrure connectée.

#### Les standards et leur puissance

| Standard | Nom | Puissance à l'appareil (~) |
|---|---|---|
| 802.3af | PoE | ~12,95 W |
| 802.3at | PoE+ | ~25,5 W |
| 802.3bt Type 3 | PoE++ / 4PPoE | ~51 W |
| 802.3bt Type 4 | PoE++ | ~71 W |

(La puissance *injectée* par le switch est un peu plus élevée que celle reçue, à cause des pertes dans le câble — encore le principe : ce qui arrive est inférieur à ce qui part.)

#### Qui fournit le courant

- **Switch PoE** : alimente directement les appareils branchés.
- **Injecteur PoE** : ajoute le PoE sur une liaison quand le switch n'est pas PoE.
- **Splitter PoE** : sépare data et courant pour un appareil non-PoE.

> **🎯 À retenir**
> Le PoE simplifie énormément les installations : pas de prise électrique nécessaire là où l'on pose une caméra ou une borne Wi-Fi. Vérifier que le **budget PoE total** du switch (somme des watts pour tous les ports) couvre l'ensemble des appareils — un switch peut supporter le PoE sur 24 ports mais pas à pleine puissance sur tous en même temps.

> **🔧 Cas concret (admin sys)**
> Une caméra PoE qui redémarre en boucle : souvent le budget PoE du switch est dépassé (trop d'appareils gourmands), ou le câble est trop long/abîmé et la tension chute. On vérifie le budget PoE, la longueur et la catégorie du câble.

---

### 36. Fibre optique, SFP/SFP+ et téléphonie

#### Fibre optique

La donnée voyage en **lumière** dans un fil de verre : immunité aux interférences, hauts débits, longues distances.

- **FTTH** (Fiber To The Home) : la fibre jusqu'au logement.
- **Monomode** : cœur très fin, longues distances (opérateurs, inter-bâtiments).
- **Multimode** : cœur plus large, courtes distances (intérieur datacenter), moins cher.
- **Connecteurs SC / LC** : SC (carré, à pousser), LC (petit, à clip).
- **ONT** (Optical Network Terminal) : convertit la lumière en signal réseau pour la box.

#### SFP / SFP+ : les modules enfichables

Un **SFP** (Small Form-factor Pluggable) est un petit module qu'on enfiche dans un switch ou un serveur pour y connecter une liaison — fibre ou cuivre selon le module.

- **SFP** : jusqu'à 1 Gb/s.
- **SFP+** : 10 Gb/s.
- **SFP28** : 25 Gb/s ; **QSFP+/QSFP28** : 40/100 Gb/s.
- **DAC** (Direct Attach Copper) : un câble cuivre à modules SFP intégrés aux deux bouts, économique pour relier deux équipements proches (entre baies).

> **🎯 À retenir**
> Le SFP rend un switch **modulaire** : un même port accepte de la fibre monomode, multimode ou du cuivre selon le module inséré. Attention à la compatibilité : certains fabricants verrouillent leurs ports sur des modules de leur marque.

#### Téléphonie : RJ11

- **RJ11** : connecteur **plus petit** que le RJ45 (2-4 contacts), pour la ligne téléphonique et l'ADSL/VDSL.
- Le **cuivre téléphonique** (et donc le RJ11) disparaît progressivement avec la fibre ; en France, le réseau cuivre historique est en fermeture programmée.

> **⚠️ Erreur fréquente**
> Plier ou écraser un câble fibre comme un câble Ethernet : la fibre est **fragile**, un rayon de courbure trop serré casse le verre ou bloque la lumière. Une jarretière fibre pincée derrière un meuble = perte de connexion ; on remplace le cordon et on respecte le rayon de courbure.

---

### 37. Wi-Fi (jusqu'à Wi-Fi 7) et protocoles sans fil

#### Les générations

| Norme | Nom | Bandes |
|---|---|---|
| 802.11n | Wi-Fi 4 | 2,4 / 5 GHz |
| 802.11ac | Wi-Fi 5 | 5 GHz |
| 802.11ax | Wi-Fi 6 | 2,4 / 5 GHz |
| 802.11ax | Wi-Fi 6E | + 6 GHz |
| **802.11be** | **Wi-Fi 7** | 2,4 / 5 / 6 GHz |

#### Les bandes — un compromis portée/débit

- **2,4 GHz** : longue portée, traverse bien les murs, mais lent et encombré.
- **5 GHz** : plus rapide, moins encombré, portée plus courte.
- **6 GHz** (6E/7) : très rapide, très peu encombré, portée encore plus courte.

#### Ce qu'apporte le Wi-Fi 7

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

#### Autres protocoles sans fil de courte portée

| Techno | Portée | Usage |
|---|---|---|
| **Bluetooth** | ~10 m | Audio, claviers, accessoires |
| **NFC** | ~4 cm | Paiement, appairage, badges |
| **Zigbee** | maillé | Domotique (capteurs, ampoules) |
| **Thread** | maillé | Domotique moderne (base de Matter) |

Zigbee et Thread forment des **réseaux maillés** : chaque appareil relaie les autres, étendant la portée. Ils consomment très peu (des années sur pile), là où le Wi-Fi serait trop énergivore pour un capteur de porte. **Matter** unifie la domotique au-dessus de Thread/Wi-Fi pour faire dialoguer des marques différentes.

---

### 38. Câblage domestique et baie de brassage

Comment relier proprement un logement ou un petit bureau — souvent absent des cours, très utile en pratique.

#### Le principe : du fixe et du mobile

- **Câblage fixe** : les câbles dans les murs/goulottes, posés une fois, qui ne bougent plus. Ils relient chaque prise murale (RJ45) à un point central.
- **Point central** : un **coffret de communication** (résidentiel) ou une **baie de brassage** (bureau).
- **Patch panel (panneau de brassage)** : tous les câbles fixes y aboutissent, étiquetés. On relie ensuite chaque port du panel au switch par un **cordon de brassage** (court, mobile).

#### Pourquoi cette séparation

On ne touche jamais aux câbles muraux : tout le « routage » se fait en façade avec des cordons courts faciles à remplacer. Ajouter un équipement, changer un port défaillant, réorganiser le réseau : tout se fait au niveau du brassage, sans ouvrir un mur.

> **🎯 À retenir**
> Une installation propre repose sur trois éléments : **prises murales RJ45** → **câblage fixe** → **patch panel + switch** en baie. L'**étiquetage** des deux extrémités de chaque câble est ce qui sépare une infrastructure maintenable d'un cauchemar de dépannage. C'est aussi vrai chez soi (coffret de communication) qu'en entreprise.

> **🔧 Cas concret**
> Une prise murale ne donne plus de réseau. Grâce à l'étiquetage du patch panel, on identifie le port correspondant, on teste le cordon de brassage (souvent le coupable), puis on teste la liaison fixe avec un testeur de câble. Sans étiquetage, on perd des heures à deviner quelle prise correspond à quel port.

---
## Partie 10 — Énergie : chargeurs, batteries, protection

---

### 39. Chargeurs, charge rapide et charge sans fil

- **Charge lente** : ~5 W, ancien USB.
- **Charge rapide** : monte tension et/ou courant via un protocole de négociation : **USB-PD** (universel, chapitre 28), **Quick Charge** (Qualcomm), ou **protocoles propriétaires** (certaines marques chargent très vite *uniquement* avec leur chargeur maison).
- **Chauffe** : la charge rapide chauffe plus, et la chaleur use la batterie.

#### Charge sans fil

- **Qi** : standard universel par induction. **Qi2** ajoute des aimants d'alignement (inspirés de MagSafe) pour un meilleur rendement.
- **Rendement** : la charge sans fil est **moins efficace** que le filaire (perte en chaleur), donc plus lente et plus chaude.

> **⚠️ Erreur fréquente**
> Attendre la charge ultra-rapide d'un téléphone avec n'importe quel chargeur. Beaucoup de charges rapides sont **propriétaires** : sans le bon chargeur ET le bon câble de la marque, on retombe sur la vitesse USB-PD standard. Ce n'est pas une panne, c'est un protocole non reconnu.

> **🎯 À retenir**
> Un bon chargeur **USB-PD multiport** de qualité couvre presque tous les besoins (téléphone, tablette, PC) et évite la multiplication des blocs. Vérifier la puissance *par port* quand plusieurs appareils chargent ensemble (elle se partage). Le sans-fil privilégie le confort, pas la vitesse.

---

### 40. Batteries lithium-ion

- **Cycles** : un cycle = une charge complète cumulée (deux fois 50 % = un cycle). Quelques centaines à ~1000 cycles avant une perte notable de capacité.
- **Capacité** : en **mAh** ou, plus rigoureusement, en **Wh** (Wh = mAh × tension / 1000). Comparer en mAh n'a de sens qu'à tension égale ; le **Wh** est la vraie mesure d'énergie.
- **Vieillissement** : accéléré par la chaleur, les charges à 100 % prolongées, les décharges à 0 %.

Bonnes pratiques : éviter la chaleur, viser ~20-80 % au quotidien (beaucoup d'appareils proposent une limite de charge à 80 %), éviter les 0 % répétés.

> **⚠️ Danger**
> Une batterie qui **gonfle** est dangereuse : on cesse de l'utiliser, on ne la perce jamais, on la fait recycler. Le gonflement annonce une dégradation pouvant mener à l'emballement thermique (incendie).

> **🔧 Cas concret**
> Portable qui « tient 20 minutes » après 4 ans : batterie en fin de cycles. Si elle n'est pas collée, son remplacement redonne une seconde vie à la machine pour bien moins cher qu'un appareil neuf. (Le cas « batterie qui se vide même branché » est traité au chapitre 47.)

---

### 41. Charge des véhicules électriques

Domaine où l'AC/DC (chapitre 1) prend tout son sens.

#### AC vs DC : le point clé

- **Charge AC** : la borne fournit de l'AC ; c'est le **chargeur embarqué de la voiture** qui le convertit en DC. Limité par ce chargeur embarqué (souvent 7-22 kW). C'est la charge à domicile et sur bornes « lentes ».
- **Charge DC (rapide)** : la borne convertit elle-même et envoie du DC **directement** à la batterie, court-circuitant le chargeur embarqué. D'où les fortes puissances (50-350 kW).

#### Les prises

- **Prise domestique** : très lente (~2,3 kW), dépannage.
- **Wallbox** : borne murale domestique (AC, ~7-22 kW).
- **Type 2** : connecteur AC standard européen.
- **CCS** (Combo) : standard européen de charge rapide **DC**.
- **CHAdeMO** : ancien standard DC japonais, en déclin en Europe.

La charge ralentit volontairement au-delà de ~80 % pour préserver la batterie.

> **🎯 À retenir**
> Même logique que l'USB-PD : la puissance réelle est le **minimum** entre ce que la borne donne et ce que la voiture accepte. Une voiture limitée à 11 kW en AC ne chargera pas plus vite sur une wallbox 22 kW — exactement le principe du plafond de puissance (chapitre 1).

> **🔧 Cas concret**
> « Ma voiture charge lentement sur une borne AC 22 kW. » Souvent le chargeur embarqué de la voiture plafonne à 7 ou 11 kW : la borne n'y est pour rien, c'est la voiture qui limite.

---

### 42. Onduleurs et protection électrique

- **Multiprise simple** : ne protège de rien.
- **Parasurtenseur** : absorbe les pics de tension (foudre). Protège, mais ne fournit pas d'énergie en cas de coupure.
- **Onduleur (UPS)** : batterie qui prend le relais lors d'une coupure. Trois types :
  - **Offline (standby)** : bascule sur batterie en cas de coupure. Économique, PC bureautique.
  - **Line-interactive** : régule aussi les petites variations de tension. Bon pour NAS/petit serveur.
  - **Online (double conversion)** : alimente *en permanence* via la batterie, isolation totale du secteur. Serveurs et équipements critiques.

> **🎯 À retenir**
> Le rôle principal d'un onduleur n'est pas (que) de « continuer à travailler » : c'est de permettre un **arrêt propre** des équipements (NAS, serveur) pour éviter la corruption de données lors d'une coupure brutale. Beaucoup s'intègrent à l'OS pour déclencher l'extinction automatique quand la batterie faiblit.

> **🔧 Cas concret (homelab)**
> Un NAS subissant des coupures répétées risque la corruption de sa grappe RAID ou de son système de fichiers. Un onduleur line-interactive, configuré pour éteindre proprement le NAS, protège les données pour un coût modeste.

---

## Partie 11 — Matériel domestique, multimédia et sécurité matérielle

---

### 43. Box, TV connectée, consoles, NAS, impression

#### La box internet : plusieurs appareils en un

- **Modem** : convertit le signal opérateur (via ONT en fibre) en réseau utilisable.
- **Routeur** : distribue Internet et gère le réseau local.
- **Switch** : les ports Ethernet à l'arrière.
- **Point d'accès Wi-Fi** : la partie sans fil.

Fonctions intégrées : **NAT** (partage d'une IP publique), **DHCP** (attribution d'IP locales), **DNS** (traduit les noms de sites en adresses IP).

> **🔧 Cas concret (support)**
> « Internet est coupé. » Premier réflexe : un appareil en **Ethernet** fonctionne-t-il ? Si oui → problème Wi-Fi, pas Internet. Si non → voyants de la box/ONT, panne opérateur ? On décompose la chaîne (opérateur → routeur → local → Wi-Fi) au lieu de tout redémarrer au hasard. (Détaillé au chapitre 47.)

#### TV connectée

La qualité d'image dépend autant du **processeur vidéo** (upscaling, gestion du mouvement) que de la dalle. Le **système Smart TV** soulève des questions de mises à jour (limitées dans le temps) et de **collecte de données (ACR**, reconnaissance automatique de contenu pour la pub ciblée), souvent désactivable dans les réglages de confidentialité.

#### Consoles de jeu

Architecture proche du PC (CPU/GPU AMD, SSD NVMe), **HDMI 2.1** pour la 4K 120 Hz et le VRR, manettes sans fil, réseau Ethernet (recommandé) ou Wi-Fi.

#### NAS

Petit serveur de stockage en réseau : centralise les fichiers, héberge les sauvegardes des PC, parfois des services (médiathèque, conteneurs). RAID pour la tolérance de panne — mais **RAID ≠ sauvegarde** (chapitre 16), donc une copie hors NAS reste nécessaire.

#### Imprimantes et scanners

Connexion USB-B / Ethernet / Wi-Fi. **Jet d'encre** (photo/couleur, encre qui sèche si peu utilisée) vs **laser** (rapide, économique, idéal usage irrégulier et texte).

> **⚠️ Erreur fréquente**
> Une imprimante jet d'encre utilisée rarement coûte cher en têtes bouchées. Pour un usage occasionnel surtout textuel, une **laser** est plus économique et fiable sur la durée.

---

### 44. Sécurité matérielle : USB malveillant, firmware, DMA, équipements exposés

Chapitre transversal : tout le matériel vu jusqu'ici a une **surface d'attaque physique**. C'est un angle mort fréquent, et un sujet clé en cyber.

#### USB malveillant

Le port USB est une porte d'entrée privilégiée parce qu'il combine données et confiance implicite.

- **BadUSB** : une clé (ou un câble, un chargeur) dont le **firmware** a été reprogrammé pour se faire passer pour un autre périphérique — typiquement un **clavier**. Branchée, elle « tape » à toute vitesse des commandes malveillantes. L'OS lui fait confiance car « c'est un clavier ».
- **Rubber Ducky / câbles piégés** : des outils prêts à l'emploi de ce principe, parfois cachés dans un câble de charge d'apparence normale.
- **Juice jacking** : une borne de recharge USB publique (aéroport, gare) modifiée pour exfiltrer des données ou injecter du code via le port.

> **🔒 Sécurité — défenses USB**
> Ne jamais brancher une clé/un câble trouvé ou d'origine inconnue. Sur poste sensible : désactiver l'autorun, restreindre les classes USB autorisées (politiques d'OS, ports verrouillés), utiliser un **« USB condom »** (adaptateur data-blocker) sur les bornes publiques, ou charger sur une prise secteur plutôt qu'un port USB inconnu. En entreprise, le contrôle des périphériques (device control) bloque les classes non autorisées.

#### Attaques DMA (Thunderbolt / PCIe)

Parce que Thunderbolt (et le PCIe en général) donne un **accès mémoire direct (DMA)** pour la performance, un périphérique malveillant branché peut tenter de **lire/écrire directement dans la RAM** sans passer par l'OS — pour extraire des clés de chiffrement, des mots de passe, ou injecter du code (famille « Thunderspy »).

> **🔒 Sécurité — défenses DMA**
> Les protections modernes existent : **IOMMU / VT-d / Kernel DMA Protection** cloisonnent ce qu'un périphérique peut adresser en mémoire. Les réglages **Thunderbolt Security Levels** (autorisation utilisateur avant qu'un périphérique fonctionne) et le verrouillage de l'écran (qui bloque les nouveaux périphériques DMA) limitent le risque. À retenir : un ordinateur **verrouillé mais allumé**, laissé sans surveillance avec un port Thunderbolt ouvert, n'est pas à l'abri.

#### Sécurité du firmware

Le **firmware** (chapitre 11) s'exécute *sous* l'OS : une compromission y est très grave (persistante, invisible, survit à une réinstallation). Concerne UEFI, mais aussi BMC (iDRAC/iLO), cartes réseau, SSD.

> **🔒 Sécurité — défenses firmware**
> Maintenir les firmwares à jour (UEFI, BMC, périphériques), activer **Secure Boot** pour bloquer un bootkit non signé, s'appuyer sur le **TPM** pour mesurer l'intégrité du démarrage, et ne jamais exposer un **BMC (iDRAC/iLO/IPMI)** sur Internet — réseau d'administration isolé obligatoire (chapitre 15).

#### Équipements réseau souvent oubliés : box, NAS, imprimantes, caméras

Ce sont des **ordinateurs connectés à part entière** (CPU, firmware, parfois disque), et des cibles fréquentes parce qu'on les sécurise rarement :

- **Box / routeur** : changer les identifiants par défaut, mettre à jour le firmware, désactiver l'administration distante inutile, segmenter l'IoT sur un réseau séparé.
- **NAS** : ne **jamais** l'exposer directement à Internet ; accès via **VPN**, double authentification, mises à jour. Les NAS grand public sont des cibles régulières de ransomwares.
- **Imprimantes** : changer les mots de passe par défaut, mettre à jour le firmware ; elles stockent parfois des documents et offrent un point d'entrée discret sur le réseau.
- **Caméras IP / objets connectés** : mots de passe par défaut notoirement exploités (réseaux de botnets). À isoler sur un VLAN/réseau invité.

> **🎯 À retenir**
> La règle d'or de la sécurité matérielle tient en une phrase : **tout ce qui a un firmware et une adresse réseau est un ordinateur à sécuriser** — y compris la box, le NAS, l'imprimante et la caméra. Les trois réflexes universels : changer les identifiants par défaut, mettre à jour le firmware, segmenter le réseau (séparer l'IoT et l'administration du reste).

---
## Partie 12 — Choisir et diagnostiquer

Synthèse pratique de tout le cours : transformer la compréhension en décisions d'achat et en diagnostics méthodiques.

---

### 45. Lire une fiche technique (PC, écran, câble)

#### Lire une fiche PC

- **CPU** : pas le seul nom. Vérifier **génération** et **suffixe** (U/H/HX sur portable = chauffe et puissance très différentes). Comparer via des tests réels, pas la fréquence.
- **RAM** : quantité d'abord, puis fréquence. **Soudée ou non ?** (décisif sur portable).
- **Stockage** : SSD NVMe attendu ; emplacement libre pour extension ?
- **Connectiques** : combien de ports USB, lesquels sortent la vidéo (**Alt Mode / Thunderbolt** ?), HDMI/DP et leurs versions.
- **Autonomie** : annoncée en conditions idéales ; diviser mentalement par ~1,5.
- **Réparabilité** : RAM/SSD/batterie remplaçables ?

> **🎯 À retenir**
> Les deux pièges les plus coûteux d'une fiche PC : un **CPU à suffixe bridé** pris pour un modèle puissant, et une **RAM soudée** non extensible. Deux lignes à vérifier systématiquement.

#### Lire une fiche écran

- **Dalle** (TN/IPS/VA/OLED) → couleurs, contraste, angles.
- **Résolution + taille** → en déduire la **densité** (vraie netteté).
- **Fréquence** : et *via quelle connectique* l'atteindre.
- **HDR** : méfiance sur « DisplayHDR 400 » (faux HDR) ; regarder les nits réels.
- **Connectiques** : **versions exactes** (HDMI 2.0/2.1/2.2, DP 1.4/2.1) — elles conditionnent résolution + fréquence *simultanées*.

> **⚠️ Erreur fréquente**
> Voir « 4K » et « 144 Hz » et supposer les deux *en même temps*. Cela dépend de la version de la connectique et du câble : un port trop ancien oblige à choisir. Toujours croiser résolution + fréquence + version du port + câble.

#### Lire une fiche câble

Le maillon le plus sous-estimé.

- **Norme exacte** : « USB-C » ne suffit pas → vitesse (USB 2.0 ? 10 Gb/s ? 80 Gb/s ? Thunderbolt ?), puissance, vidéo ou non.
- **Longueur** : au-delà de certaines longueurs, le haut débit exige un câble **actif** ou certifié court (1 m en USB4 80 Gb/s passif).
- **Puissance** et **e-mark** : logo **« 240 W »** = e-marked ; sans, plafond 60 W.
- **Certification** : « Ultra High Speed » (HDMI 2.1, 48 Gb/s), « Ultra96 » (HDMI 2.2, 96 Gb/s), logo Thunderbolt + chiffre, logos USB-IF « 40/80 Gbps ».
- **Actif / passif** : un câble actif contient de l'électronique pour tenir le débit sur la distance.

> **🎯 À retenir**
> Un câble n'est pas un détail interchangeable. Pour tout usage exigeant (4K 120 Hz, 240 W, 80 Gb/s), le câble doit être **explicitement certifié** pour cet usage. Étiqueter ses câbles évite des diagnostics interminables.

---

### 46. Choisir selon l'usage

| Usage | Priorités matérielles |
|---|---|
| **Bureautique** | 16 Go RAM, SSD, CPU modeste, écran confortable |
| **Gaming** | GPU avant tout, écran haute fréquence + VRR, bon refroidissement |
| **Montage vidéo** | CPU multicœur, RAM abondante, GPU à bon encodage, stockage rapide, écran calibré |
| **Cybersécurité** | RAM abondante (machines virtuelles), virtualisation activée (VT-x/AMD-V), SSD, plusieurs interfaces réseau utiles |
| **Homelab** | Faible consommation, RAM pour la virtualisation, stockage fiable (ZFS/HBA), gestion à distance, onduleur |
| **Mobilité** | Autonomie (Wh), poids, robustesse, charge USB-PD universelle |
| **Serveur domestique** | Fiabilité 24/7, stockage redondé, faible bruit/conso, ECC si possible, onduleur |

> **🎯 À retenir**
> Pas de « meilleur matériel » dans l'absolu, seulement un matériel **adapté à un usage**. On part de l'usage réel, on en déduit le composant prioritaire (GPU pour le jeu, RAM pour la virtualisation, autonomie pour la mobilité), et on ne surpaie pas le reste.

---

### 47. Manuel de diagnostic matériel

La méthode universelle, valable pour les onze cas : **changer une seule variable à la fois**, du plus simple et probable au plus complexe, en gardant en tête les deux principes du cours — *connecteur ≠ câble ≠ protocole*, et *le débit/la puissance réelle est celle du maillon le plus faible*.

Chaque panne suit le même format : **symptômes → causes probables → ordre de vérification → erreurs fréquentes → solution probable**.

---

#### 47.1 — PC qui ne démarre pas

**Symptômes.** Rien ne s'allume, ou les ventilateurs tournent mais aucun affichage, ou la machine s'allume puis s'éteint en boucle.

**Causes probables.** Alimentation (câble, prise, bloc), RAM mal enfichée, GPU mal détecté, court-circuit (entretoise mal placée), bouton/façade, firmware UEFI trop ancien pour le CPU.

**Ordre de vérification.**
1. Alimentation électrique : prise testée, interrupteur du bloc sur « I », câble bien enfoncé.
2. Signes de vie : LED de carte mère, ventilateurs. *Aucun signe* → alimentation ou court-circuit. *Des signes mais pas d'image* → étape POST.
3. Lire les **LED de diagnostic** (CPU/DRAM/VGA/BOOT) ou écouter les **bips** : ils indiquent l'étape qui bloque.
4. Réenfoncer fermement la RAM (clac des deux côtés), tester une seule barrette, puis l'autre.
5. Réenfoncer le GPU ; tester l'affichage sur le GPU, pas sur la carte mère.
6. Sur plateforme récente : firmware UEFI à jour pour reconnaître le CPU (BIOS Flashback).

**Erreurs fréquentes.** Brancher l'écran sur la sortie de la **carte mère** alors qu'un GPU dédié est installé (souvent désactivée). Oublier le connecteur d'alimentation **EPS/CPU 8 broches** (la machine ne POST pas). Conclure « CPU mort » sans avoir testé la RAM (cause bien plus fréquente).

**Solution probable.** Dans la majorité des cas : RAM à réenfoncer, ou erreur d'écran branché au mauvais endroit, ou connecteur d'alimentation oublié.

---

#### 47.2 — Écran noir (PC qui semble allumé)

**Symptômes.** Le PC tourne (ventilateurs, LED) mais l'écran reste noir ou affiche « Pas de signal ».

**Causes probables.** Mauvaise **source/entrée** sélectionnée sur l'écran, câble mort ou inadapté, mauvaise sortie utilisée, écran non alimenté, GPU non initialisé.

**Ordre de vérification.**
1. L'écran est-il allumé et sur la **bonne entrée** (HDMI 1 / HDMI 2 / DP) ? Beaucoup d'écrans ne basculent pas automatiquement.
2. Tester un **autre câble** et un **autre port** (réflexe Partie 6).
3. Brancher sur la sortie du **GPU dédié**, pas de la carte mère.
4. Tester l'écran sur un autre appareil (et le PC sur un autre écran) pour isoler.

**Erreurs fréquentes.** Confondre « écran noir » et « PC qui ne démarre pas » : si les LED de diagnostic montrent un POST réussi, le problème est l'affichage, pas le démarrage. Oublier de vérifier l'entrée sélectionnée — la cause la plus bête et la plus fréquente.

**Solution probable.** Entrée mal sélectionnée, ou écran branché sur la carte mère au lieu du GPU.

---

#### 47.3 — Câble HDMI/DP qui limite la résolution

**Symptômes.** Impossible d'atteindre la résolution maximale de l'écran (ex. bloqué en 1080p sur un écran 4K), ou scintillements/coupures par intermittence en haute résolution.

**Causes probables.** Câble de **version insuffisante** ou non certifié, port d'une **version trop ancienne** (HDMI 1.4 limité à 4K 30 Hz), adaptateur passif limitant, longueur excessive.

**Ordre de vérification.**
1. Identifier la **version** du port côté PC *et* côté écran (le plus faible des deux gagne).
2. Vérifier la certification du **câble** : Ultra High Speed (HDMI 2.1), Ultra96 (HDMI 2.2), bon DP.
3. Remplacer par un câble certifié court et tester.
4. Vérifier les réglages d'affichage de l'OS (résolution forcée trop basse).

**Erreurs fréquentes.** Croire que « HDMI = HDMI » : un vieux câble bride une chaîne récente. Le scintillement en numérique = câble en limite de tenue (effet tout-ou-rien, chapitre 1), pas un écran défectueux.

**Solution probable.** Câble sous-spécifié ou trop long → câble certifié à la bonne version.

---

#### 47.4 — Écran 144 Hz bloqué à 60 Hz

**Symptômes.** Écran haute fréquence qui n'affiche que 60 Hz.

**Causes probables.** Fréquence non sélectionnée dans l'OS, câble/port insuffisant pour le couple (résolution × fréquence), VRR non activé.

**Ordre de vérification.**
1. **Réglages d'affichage de l'OS** : sélectionner explicitement 144 Hz (cause n°1, souvent oubliée).
2. Vérifier que le couple résolution + fréquence tient dans la bande passante du **port** et du **câble** (ex. 1440p 144 Hz exige un bon DP ou HDMI 2.0+).
3. Préférer le **DisplayPort** pour le haut rafraîchissement.
4. Activer FreeSync/G-Sync (VRR) si pertinent.

**Erreurs fréquentes.** Penser que brancher l'écran suffit (Windows/macOS reste souvent à 60 Hz par défaut). Utiliser un câble HDMI ancien incapable de 144 Hz à la résolution voulue.

**Solution probable.** Régler 144 Hz dans l'OS ; si indisponible, changer pour un câble/port à la hauteur (DisplayPort).

---

#### 47.5 — USB-C qui ne charge pas (ou charge lentement)

**Symptômes.** L'appareil ne charge pas, charge lentement, ou se décharge même branché.

**Causes probables.** Chargeur sous-dimensionné, **câble non e-marked** (bride à 60 W) ou « charge seule », **port** qui n'accepte pas l'entrée d'alimentation, protocole propriétaire non reconnu.

**Ordre de vérification.**
1. Le **chargeur** délivre-t-il assez (logo « 240 W » ? puissance par port si multiport) ?
2. Le **câble** est-il e-marked (logo 240 W) ou bridé à 60 W ? Est-ce un câble de données ou « charge seule » ?
3. Le **port** du PC accepte-t-il l'alimentation (tous les USB-C ne le font pas) ?
4. Y a-t-il un **protocole propriétaire** (charge rapide maison) qui exige le chargeur de la marque ?

**Erreurs fréquentes.** Croire qu'un câble USB-C en vaut un autre. Utiliser un chargeur de téléphone (30 W) sur un PC qui consomme 90 W en charge de travail : il se décharge plus vite qu'il ne se charge (chapitre 1).

**Solution probable.** Câble bridé/charge-seule à remplacer, ou chargeur sous-dimensionné. Le trio chargeur + câble + port décide (chapitre 28).

---

#### 47.6 — Dock qui ne sort pas la vidéo

**Symptômes.** Le dock fonctionne (USB, réseau) mais aucun écran ne s'affiche, ou un seul alors qu'on en branche deux.

**Causes probables.** Port hôte sans **DisplayPort Alt Mode**, dock USB-C simple incapable de multi-écrans, câble hôte inadapté, dock Thunderbolt branché sur un port non-Thunderbolt.

**Ordre de vérification.**
1. Le **port hôte** gère-t-il l'Alt Mode (logo DP) ou le **Thunderbolt** (logo éclair) ? Beaucoup de portables n'ont l'Alt Mode que sur *un* port USB-C.
2. Le **câble** entre PC et dock est-il « full featured » (vidéo + données), pas un câble de charge ?
3. Pour **deux écrans** ou plus en haute résolution : un dock **Thunderbolt** est souvent nécessaire (l'USB-C simple ne porte qu'un flux DP, sauf MST/DSC selon les cas).
4. Pilotes du dock / DisplayLink à jour si le dock utilise cette techno.

**Erreurs fréquentes.** Brancher un dock Thunderbolt sur un port USB-C ordinaire et s'étonner des limitations. Espérer du multi-écrans haute résolution d'un dock USB-C d'entrée de gamme.

**Solution probable.** Utiliser le bon port (Alt Mode/Thunderbolt) et un câble adapté ; pour le multi-écrans, un dock Thunderbolt (chapitre 30).

---

#### 47.7 — SSD non détecté

**Symptômes.** Un SSD (surtout M.2 NVMe) n'apparaît pas dans l'UEFI ou l'OS après installation.

**Causes probables.** Confusion **M.2 SATA vs NVMe** (port incompatible), **partage de lignes PCIe** qui désactive le port, SSD mal enfiché, port M.2 non activé dans l'UEFI, disque neuf non initialisé/formaté.

**Ordre de vérification.**
1. Le SSD est-il **NVMe** ou **SATA**, et le port M.2 accepte-t-il ce type ? (chapitre 8 — connecteur ≠ protocole).
2. Consulter le **tableau de partage des lignes** de la carte mère : ce port M.2 désactive-t-il un port SATA, ou est-il désactivé par un slot PCIe occupé ? (chapitre 6).
3. Réenfoncer le SSD et revisser correctement (un M.2 mal incliné ne contacte pas).
4. Activer le port dans l'UEFI si nécessaire.
5. Disque neuf : il faut l'**initialiser/partitionner** (il n'apparaît pas dans l'explorateur tant qu'il n'est pas formaté).

**Erreurs fréquentes.** Acheter un M.2 SATA pour un port NVMe only (ou l'inverse). Oublier qu'occuper un 2e M.2 a désactivé des ports SATA (les disques SATA « disparaissent »).

**Solution probable.** Mauvais type de M.2, ou conflit de partage de lignes → déplacer le SSD vers le bon port d'après le manuel.

---

#### 47.8 — Ethernet bloqué à 100 Mb/s ou 1 Gb/s

**Symptômes.** Liaison filaire plafonnée bien en dessous de l'attendu (100 Mb/s au lieu de 1 Gb/s, ou 1 Gb/s au lieu de 2,5/10 Gb/s).

**Causes probables.** **Catégorie de câble** insuffisante ou paire endommagée, **port/carte réseau** limité, négociation ratée, longueur excessive, switch d'ancienne génération.

**Ordre de vérification.**
1. Identifier la vitesse max de chaque maillon : **carte réseau**, **câble** (Cat5e/6/6a), **switch/port**, **box**. Le plus lent impose la vitesse.
2. Un câble bloqué à 100 Mb/s a souvent une **paire coupée** : un câble Gigabit utilise les 4 paires, le 100 Mb/s n'en utilise que 2. Tester un autre câble certifié.
3. Forcer/vérifier l'**auto-négociation** dans les paramètres de la carte (éviter un réglage manuel figé).
4. Réduire la longueur, éviter les rallonges/raccords douteux.

**Erreurs fréquentes.** Accuser l'opérateur alors qu'un vieux Cat5 ou un câble pincé bride la liaison. Oublier que le **port du switch** ou la **carte réseau** peut être l'élément limitant.

**Solution probable.** Câble sous-catégorie ou endommagé → câble Cat6 testé ; sinon, carte réseau/switch en cause.

---

#### 47.9 — Wi-Fi lent

**Symptômes.** Débit Wi-Fi faible, instable, ou qui s'effondre loin de la box.

**Causes probables.** Distance/obstacles, mauvaise bande (2,4 GHz saturée), canal encombré par les voisins, ancienne génération Wi-Fi, interférences, point d'accès unique pour une grande surface.

**Ordre de vérification.**
1. Comparer **près** et **loin** de la box. Lent partout → réglages/matériel ; lent seulement loin → couverture.
2. Choisir la bonne **bande** : 5/6 GHz près de la box (rapide, peu encombré), 2,4 GHz loin (portée).
3. Vérifier la **génération** supportée des deux côtés (un client Wi-Fi 5 ne profitera pas d'une box Wi-Fi 7).
4. Tester en **filaire** pour confirmer que le problème est bien le Wi-Fi et non Internet.
5. Grande surface/étages → **mesh** ou point d'accès relié en Ethernet, plutôt qu'un répéteur qui divise le débit.

**Erreurs fréquentes.** Confondre « Wi-Fi lent » et « Internet lent » (un test filaire tranche). Empiler des répéteurs qui dégradent la latence et le débit.

**Solution probable.** Mauvaise bande/canal, ou couverture insuffisante → bon réglage de bande ou passage en mesh (chapitre 37).

---

#### 47.10 — Surchauffe

**Symptômes.** Ventilateurs très bruyants, ralentissements après quelques minutes d'effort, arrêts brutaux, températures élevées (>90-95 °C soutenus).

**Causes probables.** Poussière dans les radiateurs, pâte thermique séchée, flux d'air bloqué, ventilateur en panne, charge anormale d'un processus.

**Ordre de vérification.**
1. Mesurer les **températures** (HWiNFO, capteurs) au repos et en charge.
2. Symptôme typique du **throttling** : performances qui chutent après montée en température (chapitre 4).
3. Nettoyer la **poussière** (air sec), vérifier que tous les **ventilateurs** tournent.
4. Contrôler le **flux d'air** (entrées/sorties non obstruées, sur portable : surface dure, pas un lit).
5. Si le problème persiste sur une machine âgée : **refaire la pâte thermique**.

**Erreurs fréquentes.** Conclure « CPU trop faible » ou « il faut changer de PC » alors qu'un nettoyage suffit. Utiliser un portable sur une surface molle qui bouche les aérations.

**Solution probable.** Nettoyage de la poussière (souvent -10 à -15 °C) ; sinon, nouvelle pâte thermique (chapitre 10).

---

#### 47.11 — Batterie qui se vide même branchée

**Symptômes.** Un portable branché se décharge quand même, ou ne charge que très lentement sous charge de travail.

**Causes probables.** **Chargeur sous-dimensionné** face à la consommation réelle, **câble non e-marked** bridant à 60 W, port USB-C qui n'accepte pas l'alimentation, batterie en fin de vie, charge de travail extrême (CPU+GPU à fond).

**Ordre de vérification.**
1. Comparer la **puissance du chargeur** à la consommation de pointe du PC (un PC gaming peut tirer 130-200 W ; un chargeur 65 W ne suit pas sous charge).
2. Vérifier le **câble** (e-marked, logo 240 W) et le **port** (entrée d'alimentation supportée).
3. Tester au repos : si ça charge au repos mais se vide en charge lourde, c'est un **sous-dimensionnement**, pas une panne.
4. État de la **batterie** (cycles, capacité résiduelle, gonflement éventuel → danger, chapitre 40).

**Erreurs fréquentes.** Utiliser un petit chargeur USB-C universel sur un portable puissant et croire à une panne. Ignorer un câble bridé à 60 W.

**Solution probable.** Chargeur à la bonne puissance et câble e-marked ; si la batterie est gonflée ou en fin de cycles, la remplacer.

---

### Conclusion : la culture matérielle en deux idées

Si tu ne retiens que cela de tout le cours :

> **1. Connecteur, câble et protocole sont trois choses distinctes.**
> **2. La performance réelle d'une chaîne est celle de son maillon le plus faible.**

Ces deux principes expliquent, d'un seul coup :

- pourquoi un câble USB-C ne charge pas ton PC (câble ou port insuffisant) ;
- pourquoi ton écran 144 Hz reste à 60 Hz (réglage, ou câble/port) ;
- pourquoi « HDMI 2.1 » ou « HDMI 2.2 » ne garantit pas les fonctions attendues (support partiel + câble requis) ;
- pourquoi un RAID n'est pas une sauvegarde (il protège du matériel, pas de l'erreur ni du ransomware) ;
- pourquoi un chargeur 240 W ne charge pas tout à 240 W (négociation + plafond + maillon faible) ;
- pourquoi un SSD NVMe « disparaît » quand on remplit un 2e port M.2 (partage de lignes PCIe) ;
- pourquoi un Ethernet « Gigabit » tombe à 100 Mb/s (paire coupée, maillon faible).

Tu disposes maintenant d'une grille de lecture transversale, d'un socle de notions à jour (HDMI 2.2/Ultra96, USB4 80 Gb/s, PD 240 W, Thunderbolt 5, Wi-Fi 7) et d'une méthode de diagnostic reproductible. La suite, c'est la pratique : démonte, branche, mesure, isole une variable à la fois, et reviens aux deux principes chaque fois qu'« en théorie, ça devrait marcher ».

---

*Fin du cours — Édition 2.1.*

---

## Annexes

---

### Annexe A — Sources et standards à surveiller

Le matériel évolue, et les chiffres de ce cours (débits, puissances, versions) bougent avec les normes. Pour vérifier une information ou suivre les évolutions, voici les **organismes officiels** qui publient et maintiennent chaque standard. En cas de doute, ce sont eux qui font foi — avant les blogs et revendeurs.

| Domaine | Organisme | Ce qu'il définit |
|---|---|---|
| Vidéo HDMI | **HDMI Forum** / HDMI Licensing Administrator | Versions HDMI (2.0, 2.1, 2.2), câbles (Ultra High Speed, Ultra96) |
| Vidéo PC | **VESA** | DisplayPort (1.4, 2.1), DisplayHDR, Adaptive-Sync |
| USB & USB-C | **USB-IF** (USB Implementers Forum) | USB 2.0/3.x, USB4, USB Power Delivery, logos de certification |
| Thunderbolt | **Intel** | Thunderbolt 3/4/5 |
| Wi-Fi | **Wi-Fi Alliance** / **IEEE 802.11** | Certifications Wi-Fi 6/6E/7, normes 802.11 sous-jacentes |
| Bus interne | **PCI-SIG** | PCI Express (3.0, 4.0, 5.0…) |
| Mémoire | **JEDEC** | DDR4, DDR5, vitesses en MT/s, ECC |
| Stockage flash | **NVM Express (NVMe)** | Interface NVMe des SSD |
| Stockage entreprise | **SNIA** | Concepts et standards de stockage (RAID, SAN…) |
| Réseau filaire | **IEEE 802.3** | Ethernet, catégories de câbles, PoE (802.3af/at/bt) |
| Électricité / sécurité | **IEC** (+ normes nationales) | Normes électriques, connecteurs, sécurité |

> **🎯 À retenir**
> Quand une fiche produit annonce un chiffre flatteur (« HDMI 2.1 », « 240 W », « Wi-Fi 7 »), le réflexe est de croiser avec l'organisme officiel correspondant : le standard autorise souvent des supports *partiels*, et c'est la source officielle qui dit ce que la mention garantit réellement.

---

### Annexe B — Fiches réflexes

Sept aide-mémoires condensés, à consulter en situation. Chacun renvoie au chapitre détaillé.

#### B.1 — Choisir un câble USB-C (ch. 28)

1. **Vidéo ?** → le port hôte doit gérer DisplayPort Alt Mode (logo DP) ou Thunderbolt (⚡), et le câble être « full featured » (pas charge seule).
2. **Charge > 60 W ?** → câble **e-marked** obligatoire, repérable au logo **« 240 W »**.
3. **Haut débit ?** → vérifier la mention USB-IF (« 40 Gbps », « 80 Gbps ») et la longueur (1 m max en passif pour 80 Gb/s).
4. **Thunderbolt / eGPU / dock ?** → câble **certifié Thunderbolt** (éclair + chiffre), pas un câble de charge.
5. **Règle d'or** : un câble est spécialisé. Étiqueter ses câbles évite des heures de diagnostic.

#### B.2 — Choisir un écran (ch. 19-21, 45)

1. **Usage** : bureautique/code (IPS, 16:10), jeu (haute fréquence + VRR), création (IPS/OLED calibrable, % DCI-P3).
2. **Densité** = résolution rapportée à la taille, pas la résolution seule.
3. **Fréquence** : vérifier *via quelle connectique* l'atteindre (DisplayPort pour 144 Hz+).
4. **HDR** : ignorer « DisplayHDR 400 » (faux HDR) ; viser 600+ nits, Mini-LED ou OLED.
5. **Connectique** : croiser résolution + fréquence + version de port + câble.

#### B.3 — Choisir un chargeur (ch. 1, 39, 28)

1. La puissance annoncée est un **plafond**, pas une dose imposée : un gros chargeur ne « grille » pas un petit appareil.
2. Privilégier un **USB-PD multiport** de qualité ; vérifier la puissance *par port* (elle se partage).
3. Pour un PC portable : viser la puissance réelle de pointe (un PC gaming peut tirer 130-200 W).
4. Charge rapide « maison » = souvent **propriétaire** (bon chargeur + bon câble de la marque requis).
5. Câble à la hauteur : e-marked (logo 240 W) si > 60 W.

#### B.4 — Diagnostiquer un écran noir (ch. 47.2)

1. Écran allumé, sur la **bonne entrée** (HDMI 1/2, DP) ? (cause la plus fréquente)
2. Tester **autre câble** + **autre port**.
3. Brancher sur le **GPU dédié**, pas la carte mère.
4. Isoler : écran sur un autre PC, PC sur un autre écran.
5. Si le POST réussit (LED de diagnostic), c'est l'affichage, pas le démarrage.

#### B.5 — Diagnostiquer un problème réseau (ch. 43, 47.8-47.9)

1. **Filaire fonctionne-t-il ?** Si oui → problème Wi-Fi, pas Internet.
2. Si rien : **voyants box/ONT** → panne opérateur ?
3. Décomposer la chaîne : opérateur → routeur → réseau local → Wi-Fi.
4. Filaire lent : catégorie du **câble** (paire coupée → bridé à 100 Mb/s), carte réseau, port du switch.
5. Wi-Fi lent : comparer près/loin, bonne bande (5/6 GHz près, 2,4 GHz loin), mesh si grande surface.

#### B.6 — Lire une fiche PC portable (ch. 45)

1. **CPU** : génération + suffixe (U/H/HX) bien plus que le nom.
2. **RAM** : quantité, et surtout **soudée ou non**.
3. **Stockage** : SSD NVMe, emplacement libre ?
4. **Connectiques** : quels ports USB-C sortent la vidéo / font Thunderbolt ?
5. **Autonomie** (Wh, à minorer d'un tiers) et **réparabilité**.

#### B.7 — Sécuriser une box / NAS / imprimante (ch. 44)

1. **Changer les identifiants par défaut** (le réflexe n°1).
2. **Mettre à jour le firmware** régulièrement.
3. **Ne jamais exposer** un NAS / une interface d'admin (BMC, box) directement à Internet → VPN.
4. **Segmenter** : IoT, caméras et invités sur un réseau séparé (VLAN/Wi-Fi invité).
5. Activer la **double authentification** là où c'est possible (NAS, accès distant).

---

### Annexe C — Cinq mini-labs de diagnostic (optionnels)

Des exercices pratiques pour ancrer la méthode. Chacun se fait avec du matériel courant ; l'objectif n'est pas de « réparer » mais d'**appliquer la démarche** : isoler une variable à la fois, identifier le maillon faible, vérifier connecteur/câble/protocole. Les pistes de correction renvoient au chapitre 47.

#### Lab 1 — L'écran capricieux
**Mise en situation.** Un écran 1440p 144 Hz n'affiche que 60 Hz une fois branché à un PC.
**À faire.** Lister, dans l'ordre, les vérifications à mener. Identifier les trois maillons possibles.
**Attendu.** (1) Réglage de fréquence dans l'OS ; (2) version/qualité du câble pour le couple 1440p+144 Hz ; (3) version du port utilisé. Tester en changeant *une* variable à la fois. → *ch. 47.4*

#### Lab 2 — La charge qui n'avance pas
**Mise en situation.** Un PC portable branché en USB-C se décharge quand même en pleine charge de travail.
**À faire.** Déterminer si c'est une panne ou un sous-dimensionnement, et le prouver.
**Attendu.** Comparer puissance du chargeur vs consommation de pointe ; vérifier câble (e-marked / logo 240 W) et port (entrée d'alimentation). Test décisif : ça charge au repos mais se vide en charge lourde → sous-dimensionnement, pas panne. → *ch. 47.11 et 1*

#### Lab 3 — Le SSD fantôme
**Mise en situation.** Un SSD M.2 neuf n'apparaît nulle part après installation.
**À faire.** Proposer les causes par ordre de probabilité et la vérification associée.
**Attendu.** Type M.2 (SATA vs NVMe) compatible avec le port ? Tableau de partage des lignes PCIe (un 2e M.2 peut désactiver des ports SATA) ? SSD bien enfiché/vissé ? Disque neuf à initialiser/formater ? → *ch. 47.7, 6 et 8*

#### Lab 4 — Le Gigabit qui n'en est pas
**Mise en situation.** Une liaison Ethernet censée faire 1 Gb/s plafonne à 100 Mb/s.
**À faire.** Identifier le maillon faible le plus probable et le test pour le confirmer.
**Attendu.** Un câble bridé à 100 Mb/s a souvent une **paire coupée** (le Gigabit utilise les 4 paires). Vérifier catégorie/état du câble, port du switch, carte réseau, auto-négociation. Tester un autre câble certifié. → *ch. 47.8 et 34*

#### Lab 5 — La baie mystère (orienté admin sys / homelab)
**Mise en situation.** Dans une petite baie, une prise murale ne donne plus de réseau, et un serveur ne répond plus.
**À faire.** Décrire la démarche en s'appuyant sur le brassage et la gestion hors-bande.
**Attendu.** Côté prise : suivre l'étiquetage jusqu'au patch panel, tester le cordon de brassage (souvent coupable), puis la liaison fixe au testeur. Côté serveur figé : se connecter à l'**iDRAC/iLO** (hors-bande) pour voir l'écran et forcer un redémarrage sans déplacement ; en dernier recours, couper/relancer via la **PDU** pilotable. → *ch. 47.8, 38, 15 et 18*

> **🎯 À retenir**
> Les cinq labs partagent la même colonne vertébrale : on ne devine pas, on **isole**. Une variable change à la fois, du plus probable au plus complexe, en se demandant toujours : est-ce le connecteur, le câble, ou le protocole ? Et quel est le maillon faible de la chaîne ?

---

*Fin des annexes — Édition 2.1.*
