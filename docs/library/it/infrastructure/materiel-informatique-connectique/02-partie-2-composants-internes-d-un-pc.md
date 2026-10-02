---
title: Partie 2 — Composants internes d'un PC
source: IT/06 Infrastructure & architecture/Matériel/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

---

## 3. Vue d'ensemble et chaîne de démarrage

Un PC est un orchestre de composants spécialisés reliés par la **carte mère**. Qui fait quoi :

- **CPU** : le cerveau, calcule et coordonne.
- **RAM** : mémoire de travail rapide *mais volatile* (vidée à l'extinction).
- **Stockage (SSD/HDD)** : mémoire durable, plus lente.
- **GPU** : spécialiste du calcul massivement parallèle (affichage, IA).
- **Alimentation (PSU)** : convertit le 230 V AC en tensions DC.
- **Refroidissement** : évacue la chaleur pour éviter le bridage thermique.
- **Boîtier** : contient et organise, conditionne le flux d'air.
- **Firmware (UEFI)** : démarre la machine avant l'arrivée de l'OS.

### La chaîne de démarrage (essentielle pour diagnostiquer)

Comprendre l'ordre d'allumage permet de localiser une panne « PC qui ne démarre pas » :

1. **Alimentation** : reçoit l'ordre, fournit les tensions, envoie un signal « Power Good ».
2. **Firmware UEFI** : s'exécute depuis une puce de la carte mère.
3. **POST** (Power-On Self-Test) : l'UEFI teste CPU, RAM, GPU. Une erreur ici se manifeste par des **bips** ou des **LED de diagnostic** (souvent 4 LED : CPU / DRAM / VGA / BOOT).
4. **Détection du périphérique de démarrage** (SSD/clé/réseau).
5. **Chargement du bootloader**, puis de l'OS.

> **🎯 À retenir**
> Si un PC s'allume (ventilateurs tournent) mais n'affiche rien, le problème est presque toujours *avant* l'OS : RAM mal enfichée, GPU mal détecté, ou écran/câble. Les LED de diagnostic de la carte mère disent à quelle étape ça bloque — c'est l'outil n°1 du dépannage matériel.

---

## 4. Le processeur (CPU) : socket, cœurs, architecture

### Les notions de performance

- **Cœurs (cores)** : unités de calcul indépendantes. Plus de cœurs = plus de tâches en parallèle.
- **Threads** : fils d'exécution. Avec l'*hyper-threading* (Intel) / *SMT* (AMD), un cœur gère 2 threads.
- **Fréquence (GHz)** : cycles par seconde. Ne se compare *qu'à architecture égale*.
- **Cache** (L1/L2/L3) : mémoire ultra-rapide intégrée, évite d'aller en RAM.
- **Architecture** : x86 (Intel/AMD, PC et serveurs) vs ARM (Apple Silicon, Snapdragon, mobile, de plus en plus de serveurs) — très efficace énergétiquement.
- **TDP** : enveloppe thermique en watts ; indique grossièrement chaleur et besoin de refroidissement.

### Socket : le point de compatibilité n°1

Le **socket** est l'emplacement physique du CPU sur la carte mère. Il doit correspondre **exactement** : un CPU AMD AM5 n'entre pas dans une carte mère AM4 ; un Intel LGA 1700 ne va pas sur du LGA 1851. Le socket conditionne aussi indirectement la génération de RAM supportée (un socket AM5 implique de la DDR5).

> **⚠️ Erreur fréquente**
> Comparer deux CPU sur la seule fréquence (« 3 GHz > 2,8 GHz »). Entre générations ou marques, faux : un cœur récent à 2,8 GHz écrase souvent un ancien à 3,5 GHz grâce à l'**IPC** (instructions par cycle). On compare via des tests réels, jamais le seul nombre de GHz.

### Bridage thermique (throttling)

Quand le CPU chauffe trop, il **réduit volontairement** sa fréquence pour survivre. Un PC qui rame après quelques minutes d'effort souffre presque toujours d'un refroidissement insuffisant, pas d'un CPU « trop faible ».

> **🔧 Cas concret**
> Portable rapide au démarrage puis lent après 10 min de visio : pâte thermique sèche + ventilateur encrassé → throttling. Nettoyage et nouvelle pâte = machine relancée, sans rien remplacer d'autre.

---

## 5. Carte mère : chipset, VRM, lignes PCIe

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

## 6. PCIe en profondeur : lignes, versions, partage

Le **PCI Express (PCIe)** est l'autoroute qui relie le CPU/chipset aux composants rapides : carte graphique, SSD NVMe, cartes réseau, contrôleurs. C'est une notion centrale et souvent mal comprise.

### Lignes (lanes) et largeur de slot

Une **ligne PCIe** est une voie de communication bidirectionnelle. Les slots se notent par leur nombre de lignes :

- **x1** : une ligne (carte réseau, carte son).
- **x4** : typiquement un SSD NVMe.
- **x8 / x16** : cartes graphiques, cartes haute performance.

⚠️ Attention : **la taille physique d'un slot ne dit pas le nombre de lignes réellement câblées**. Un slot mécaniquement « x16 » peut n'être branché qu'en « x4 » électriquement. D'où la notation « x16 (x4) ».

### Versions et débit (le débit double à chaque génération)

| Version PCIe | Débit par ligne (~) | x16 (~) |
|---|---|---|
| PCIe 3.0 | ~1 Go/s | ~16 Go/s |
| PCIe 4.0 | ~2 Go/s | ~32 Go/s |
| PCIe 5.0 | ~4 Go/s | ~64 Go/s |

Les versions sont **rétrocompatibles** : une carte PCIe 4.0 fonctionne dans un slot 3.0, mais au débit du plus lent des deux (encore le maillon faible).

### Le partage des lignes : le piège qui ralentit un SSD

Le CPU n'offre qu'un **nombre limité de lignes** (souvent ~20-28 côté CPU sur grand public). Le reste passe par le **chipset**, relié au CPU par un lien lui-même limité. Conséquence pratique majeure :

> **⚠️ Erreur fréquente — la plus subtile de ce chapitre**
> Installer un SSD NVMe dans le « 2e port M.2 » et constater que la carte graphique passe de x16 à x8, ou que le SSD tombe à x2. Beaucoup de cartes mères **partagent** les lignes : remplir un port M.2 secondaire ou un slot PCIe désactive ou bride un autre. Le manuel de la carte mère contient toujours un tableau de partage des lignes ; c'est *la* page à lire avant d'ajouter un composant.

> **🔧 Cas concret (homelab/admin sys)**
> On ajoute une carte réseau 10 Gb/s dans un slot PCIe libre, et le SSD NVMe principal s'effondre en performance. Cause : la carte réseau a « volé » les lignes partagées avec le port M.2. La solution est de déplacer la carte ou le SSD vers un port qui ne partage pas, d'après le tableau du manuel.

---

## 7. La mémoire vive (RAM)

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

## 8. Le stockage (HDD, SSD SATA, NVMe, M.2)

| Type | Techno | Vitesse typique | Usage |
|---|---|---|---|
| **HDD** | Plateaux mécaniques | 100–250 Mo/s | Stockage de masse, archives, peu cher au To |
| **SSD SATA** | Flash sur interface SATA | ~550 Mo/s | Bon rapport prix/perf, plafonné par le SATA |
| **SSD NVMe** | Flash sur lignes PCIe | 3 500–14 000+ Mo/s | Système, jeux, montage, IA |

- **M.2** : un **format physique** (la barrette). ⚠️ Un SSD M.2 peut être **SATA** *ou* **NVMe** — la forme ne dit pas l'interface ni la vitesse. Brancher un M.2 SATA dans un port M.2 qui n'accepte que le NVMe (ou l'inverse) → non détecté. (Encore connecteur ≠ protocole.)
- **PCIe** : le bus que le NVMe utilise pour parler au CPU (voir chapitre 6 — un NVMe en PCIe 5.0 dans un port 3.0 sera bridé).

### Endurance de la flash

Selon le nombre de bits stockés par cellule : **SLC** (1 bit, très endurant, rare) → **MLC** (2) → **TLC** (3) → **QLC** (4, plus de capacité, moins d'endurance et de vitesse soutenue).

**SMART** : système d'auto-surveillance intégré aux disques. Il remonte température, heures de fonctionnement, secteurs réalloués, usure de la flash. C'est l'outil de prévention de panne par excellence.

> **⚠️ Erreur fréquente**
> Se fier à la vitesse de la boîte. Les SSD QLC bon marché sont rapides sur les premiers Go (cache SLC), puis s'effondrent sur les gros transferts soutenus. La vitesse *soutenue* compte plus que la vitesse de pointe pour copier de gros volumes.

> **🔧 Cas concret**
> PC qui freeze de plus en plus, erreurs aléatoires : lancer un outil SMART (CrystalDiskInfo sous Windows, `smartctl` sous Linux). Un compteur de « secteurs réalloués » qui grimpe = disque mourant → **sauvegarder immédiatement** avant la panne totale.

---

## 9. La carte graphique (GPU)

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

## 10. Alimentation, refroidissement et boîtier

### Alimentation (PSU)

Convertit le 230 V AC en 3,3 / 5 / 12 V DC.

- **Watts** : à dimensionner sur la consommation réelle de pointe (surtout GPU), avec une marge raisonnable.
- **Certification 80 PLUS** (Bronze → Titanium) : indique le **rendement** (énergie utile vs perdue en chaleur).
- **Rail 12 V** : la ligne principale (CPU et GPU).
- **Modularité** : on ne branche que les câbles utiles (meilleur flux d'air).
- **Connecteurs** : ATX 24 broches (carte mère), EPS 8 broches (CPU), PCIe / **12VHPWR / 12V-2x6** (GPU récents très gourmands).

> **🎯 À retenir**
> Une alimentation de mauvaise qualité est le composant le plus dangereux : en défaillant, elle peut endommager *tout le reste*. C'est le dernier poste sur lequel rogner. Surdimensionner à l'extrême (1000 W pour un PC qui en consomme 300) gaspille de l'argent et réduit le rendement.

### Refroidissement

- **Air** : radiateur + ventilateur. Simple, fiable, suffit à la majorité.
- **Watercooling AIO** : circuit fermé, pour CPU très puissants ou configs silencieuses.
- **Pâte thermique** : comble les micro-irrégularités CPU/radiateur ; sèche avec les années.
- **Flux d'air** : air frais qui entre, air chaud qui sort.
- **Températures repères** : ~30-50 °C au repos, 70-85 °C en charge sans souci. Au-delà de 90-95 °C prolongés, on cherche un problème.

### Boîtier et formats

- **Formats de carte mère** (du plus grand au plus petit) : **ATX**, **micro-ATX**, **mini-ITX**. Le boîtier doit accepter le format.
- **Trois pièges de compatibilité** : longueur du GPU, hauteur du ventirad CPU, format/connecteurs de l'alimentation.

> **🔧 Cas concret**
> Tour bruyante et chaude après 2-3 ans : poussière dans les radiateurs. Un nettoyage à l'air sec fait souvent baisser les températures de 10-15 °C et le bruit avec.

---

## 11. Firmware, BIOS/UEFI, TPM et Secure Boot

Brique souvent absente des cours grand public, et pourtant centrale en sécurité et en dépannage.

### Firmware : du logiciel gravé dans le matériel

Le **firmware** est un logiciel stocké dans une puce d'un appareil, qui le fait fonctionner à bas niveau. Tout en a un : carte mère, SSD, carte réseau, écran, routeur, imprimante, webcam. Il est mis à jour par « flash ». Un firmware obsolète peut empêcher de reconnaître un composant récent (chapitre 5) ou contenir des failles de sécurité (chapitre 44).

### BIOS et UEFI

Le firmware de la carte mère qui démarre la machine.

- **BIOS** : l'ancien (interface texte, limité aux disques < 2,2 To, démarrage MBR).
- **UEFI** : le moderne (interface graphique, gros disques via GPT, démarrage plus rapide, **Secure Boot**). On dit encore « BIOS » par habitude, mais c'est presque toujours de l'UEFI aujourd'hui.

L'UEFI gère aussi les réglages matériels : ordre de démarrage, activation de la virtualisation (VT-x/AMD-V, indispensable pour les machines virtuelles), profils mémoire XMP/EXPO, ventilateurs.

### TPM (Trusted Platform Module)

Le **TPM** est une puce de sécurité (soudée, ou intégrée au CPU sous le nom *fTPM*/*PTT*) qui stocke des secrets cryptographiques de façon isolée du reste du système. Ses usages :

- stocker les clés de **chiffrement de disque** (BitLocker, LUKS) pour qu'un disque volé reste illisible ;
- mesurer l'intégrité du démarrage ;
- c'est l'exigence **TPM 2.0** qui a conditionné l'installation de Windows 11.

> **🔒 Sécurité**
> Le TPM permet que le chiffrement de disque soit **transparent** (pas de mot de passe à taper au démarrage) tout en restant sûr : la clé n'est libérée que si le démarrage n'a pas été altéré. Sans TPM, soit on tape une phrase secrète à chaque démarrage, soit la clé est moins bien protégée.

### Secure Boot

**Secure Boot** est une fonction de l'UEFI qui vérifie la **signature cryptographique** de chaque composant chargé au démarrage (bootloader, noyau). Objectif : empêcher un **bootkit/rootkit** de s'installer *avant* l'OS et de devenir invisible. Seuls les composants signés par des clés de confiance se lancent.

> **🔧 Cas concret (admin sys)**
> Une distribution Linux ou un pilote non signé refuse de démarrer avec Secure Boot actif. Deux voies : utiliser une distribution signée (la plupart des grandes le sont), ou désactiver temporairement Secure Boot dans l'UEFI. Désactiver n'est pas anodin côté sécurité : on le réactive dès que possible.

> **🎯 À retenir**
> Firmware, UEFI, TPM et Secure Boot forment la **racine de confiance** d'une machine : tout ce qui s'exécute ensuite en dépend. C'est aussi pour cela qu'une attaque visant le firmware (chapitre 44) est si grave : elle se situe *sous* l'OS et survit à une réinstallation.

---
