---
title: Partie 12 — Choisir et diagnostiquer
source: IT/06 Infrastructure & architecture/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - ../index.md
---

Synthèse pratique de tout le cours : transformer la compréhension en décisions d'achat et en diagnostics méthodiques.

---

## 45. Lire une fiche technique (PC, écran, câble)

### Lire une fiche PC

- **CPU** : pas le seul nom. Vérifier **génération** et **suffixe** (U/H/HX sur portable = chauffe et puissance très différentes). Comparer via des tests réels, pas la fréquence.
- **RAM** : quantité d'abord, puis fréquence. **Soudée ou non ?** (décisif sur portable).
- **Stockage** : SSD NVMe attendu ; emplacement libre pour extension ?
- **Connectiques** : combien de ports USB, lesquels sortent la vidéo (**Alt Mode / Thunderbolt** ?), HDMI/DP et leurs versions.
- **Autonomie** : annoncée en conditions idéales ; diviser mentalement par ~1,5.
- **Réparabilité** : RAM/SSD/batterie remplaçables ?

> **🎯 À retenir**
> Les deux pièges les plus coûteux d'une fiche PC : un **CPU à suffixe bridé** pris pour un modèle puissant, et une **RAM soudée** non extensible. Deux lignes à vérifier systématiquement.

### Lire une fiche écran

- **Dalle** (TN/IPS/VA/OLED) → couleurs, contraste, angles.
- **Résolution + taille** → en déduire la **densité** (vraie netteté).
- **Fréquence** : et *via quelle connectique* l'atteindre.
- **HDR** : méfiance sur « DisplayHDR 400 » (faux HDR) ; regarder les nits réels.
- **Connectiques** : **versions exactes** (HDMI 2.0/2.1/2.2, DP 1.4/2.1) — elles conditionnent résolution + fréquence *simultanées*.

> **⚠️ Erreur fréquente**
> Voir « 4K » et « 144 Hz » et supposer les deux *en même temps*. Cela dépend de la version de la connectique et du câble : un port trop ancien oblige à choisir. Toujours croiser résolution + fréquence + version du port + câble.

### Lire une fiche câble

Le maillon le plus sous-estimé.

- **Norme exacte** : « USB-C » ne suffit pas → vitesse (USB 2.0 ? 10 Gb/s ? 80 Gb/s ? Thunderbolt ?), puissance, vidéo ou non.
- **Longueur** : au-delà de certaines longueurs, le haut débit exige un câble **actif** ou certifié court (1 m en USB4 80 Gb/s passif).
- **Puissance** et **e-mark** : logo **« 240 W »** = e-marked ; sans, plafond 60 W.
- **Certification** : « Ultra High Speed » (HDMI 2.1, 48 Gb/s), « Ultra96 » (HDMI 2.2, 96 Gb/s), logo Thunderbolt + chiffre, logos USB-IF « 40/80 Gbps ».
- **Actif / passif** : un câble actif contient de l'électronique pour tenir le débit sur la distance.

> **🎯 À retenir**
> Un câble n'est pas un détail interchangeable. Pour tout usage exigeant (4K 120 Hz, 240 W, 80 Gb/s), le câble doit être **explicitement certifié** pour cet usage. Étiqueter ses câbles évite des diagnostics interminables.

---

## 46. Choisir selon l'usage

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

## 47. Manuel de diagnostic matériel

La méthode universelle, valable pour les onze cas : **changer une seule variable à la fois**, du plus simple et probable au plus complexe, en gardant en tête les deux principes du cours — *connecteur ≠ câble ≠ protocole*, et *le débit/la puissance réelle est celle du maillon le plus faible*.

Chaque panne suit le même format : **symptômes → causes probables → ordre de vérification → erreurs fréquentes → solution probable**.

---

### 47.1 — PC qui ne démarre pas

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

### 47.2 — Écran noir (PC qui semble allumé)

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

### 47.3 — Câble HDMI/DP qui limite la résolution

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

### 47.4 — Écran 144 Hz bloqué à 60 Hz

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

### 47.5 — USB-C qui ne charge pas (ou charge lentement)

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

### 47.6 — Dock qui ne sort pas la vidéo

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

### 47.7 — SSD non détecté

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

### 47.8 — Ethernet bloqué à 100 Mb/s ou 1 Gb/s

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

### 47.9 — Wi-Fi lent

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

### 47.10 — Surchauffe

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

### 47.11 — Batterie qui se vide même branchée

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

## Conclusion : la culture matérielle en deux idées

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

## Dans cette partie

- [Annexes](01-annexes.md)
