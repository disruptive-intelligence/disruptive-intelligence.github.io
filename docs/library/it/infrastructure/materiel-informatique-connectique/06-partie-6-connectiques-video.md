---
title: Partie 6 — Connectiques vidéo
source: IT/06 Infrastructure & architecture/Matériel/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

Application directe du chapitre 2 : un connecteur, un câble et un protocole sont trois choses distinctes.

---

## 23. VGA et DVI (l'héritage analogique)

### VGA

Connecteur trapèze bleu à 15 broches, **analogique**, conçu pour les écrans cathodiques. Qualité qui se dégrade avec la longueur et la résolution (image floue possible au-delà du Full HD). On le croise sur de vieux projecteurs et matériels pro. À éviter en achat neuf.

### DVI

La transition VGA → HDMI, avec plusieurs variantes piégeuses : **DVI-A** (analogique), **DVI-D** (numérique), **DVI-I** (les deux). **Single link / Dual link** : le dual link ajoute des broches pour de plus hautes résolutions.

> **⚠️ Erreur fréquente**
> Vouloir convertir du DVI-D (numérique pur) vers du VGA (analogique) avec un adaptateur *passif* : impossible, il n'y a pas de signal analogique à récupérer. Il faut un convertisseur **actif**. La distinction analogique/numérique (chapitre 1) explique pourquoi.

---

## 24. HDMI (jusqu'à 2.2 / Ultra96)

Le standard roi du salon. **À la fois connecteur et protocole** (vidéo + audio).

### Les versions — la version compte plus que le mot « HDMI »

| Version | Bande passante | Capacités typiques |
|---|---|---|
| HDMI 1.4 | ~10 Gb/s | 4K à 30 Hz |
| HDMI 2.0 | 18 Gb/s | 4K à 60 Hz, HDR |
| HDMI 2.1 | 48 Gb/s | 4K à 120 Hz, 8K, VRR, eARC |
| **HDMI 2.2** | **96 Gb/s** | 4K à 240 Hz, 8K à 60 Hz en 4:4:4, jusqu'à 12K/16K |

La version 2.2 de la spécification HDMI a été publiée le 25 juin 2025, portant la bande passante maximale à 96 Gb/s et prenant en charge des résolutions allant jusqu'à 16K à 60 Hz, ainsi que la 4K à 240 Hz et la 8K à 60 Hz en 4:4:4 avec 10 ou 12 bits de couleur.

### Les câbles — la nouveauté Ultra96

Pour exploiter le HDMI 2.2, le câble doit suivre. Le câble « Ultra High Speed » existant gère jusqu'à 48 Gb/s ; pour les 96 Gb/s du HDMI 2.2, un nouveau câble certifié « Ultra96 » est nécessaire — sans lui, les pleines capacités du standard ne sont pas accessibles. « Ultra96 » est un nom de fonctionnalité que les fabricants sont encouragés à utiliser pour indiquer qu'un produit prend en charge un maximum de 64, 80 ou 96 Gb/s.

Bon réflexe d'achat : pour de la 4K/8K classique, un câble **Ultra High Speed (48 Gb/s)** suffit ; on ne paie l'**Ultra96** que pour de la 8K/16K non compressée ou de la 4K à très haute fréquence.

> **🎯 À retenir (veille, pas encore courant)**
> HDMI 2.2 est une norme **très récente** (publiée mi-2025) : les premiers appareils compatibles arrivent progressivement et resteront minoritaires pendant un temps, comme ce fut le cas lors de l'adoption du HDMI 2.1. À traiter comme une **information de veille** pour anticiper un achat durable, pas comme un standard déjà répandu. En 2026, l'immense majorité du matériel reste en HDMI 2.0/2.1.

### Fonctions à connaître

- **ARC / eARC** : renvoi du son de la TV vers un ampli/barre de son. L'eARC gère l'audio non compressé (Dolby Atmos…).
- **CEC** : une seule télécommande pilote plusieurs appareils.
- **Câbles actifs / passifs** : au-delà de quelques mètres en haut débit, câble certifié ou actif (avec électronique).

> **⚠️ Erreur fréquente — le piège marketing « HDMI 2.1 »**
> Le standard autorise un support *partiel* : un appareil peut afficher « HDMI 2.1 » sans gérer le 4K 120 Hz ni le VRR. Le numéro de version ne garantit **pas** les fonctions. On vérifie les fonctions *réellement listées*, pas le seul chiffre. Le même piège guettera « HDMI 2.2 ».

> **🔧 Cas concret (gaming)**
> Console récente bloquée en 4K 60 Hz sur une TV « HDMI 2.1 » : souvent le câble n'est pas Ultra High Speed, ou le **port HDMI précis** utilisé ne gère pas les fonctions 2.1 (toutes les prises d'une même TV ne se valent pas). On change de câble, puis de port.

---

## 25. DisplayPort

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

## 26. Vidéo sur USB-C et choix d'une connectique vidéo

Ici la distinction connecteur/protocole devient vitale : un port **USB-C** peut transporter de la vidéo… ou pas.

- **DisplayPort Alt Mode** : le mode qui fait passer un signal DisplayPort dans le câble USB-C. C'est *lui* qui permet de brancher un écran en USB-C. Sans ce mode, **aucune image**, quel que soit le câble.
- **HDMI Alt Mode** : équivalent pour HDMI, rare.
- **Charge + vidéo + données simultanées** : tout l'intérêt de l'USB-C (un dock alimente le PC, affiche l'écran et connecte les périphériques par un câble).

> **⚠️ Erreur fréquente — cause n°1 des écrans USB-C qui restent noirs**
> Tous les ports USB-C ne savent **pas** sortir de la vidéo. Il faut que le port supporte le **DisplayPort Alt Mode** (souvent un petit logo DP ou un éclair Thunderbolt à côté de la prise). Beaucoup de portables n'ont l'Alt Mode que sur *un seul* de leurs ports USB-C. Un port « données seulement » n'affichera jamais d'image.

### Choisir sa connectique vidéo, en résumé

| Besoin | Choix recommandé |
|---|---|
| PC, haute fréquence (144 Hz+) | DisplayPort |
| Salon, TV, console | HDMI (version selon résolution/fréquence) |
| Portable/dock, un seul câble | USB-C (Alt Mode) ou Thunderbolt |
| 8K/16K non compressé, 4K très haute fréquence | HDMI 2.2 + câble Ultra96 |

> **🔧 Cas concret**
> Dock USB-C dont l'écran ne s'affiche pas : voir le diagnostic complet « dock qui ne sort pas la vidéo » au chapitre 47. En une phrase : le port hôte doit gérer l'Alt Mode (ou Thunderbolt), et le dock doit en tenir compte.

---
