---
title: Partie 5 — Écrans et affichage
source: IT/06 Infrastructure & architecture/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

---

## 19. Comprendre un écran : résolution, densité, dalle

### Les caractéristiques

- **Taille** : diagonale en pouces.
- **Résolution** : nombre de pixels (1920 × 1080…).
- **Densité (PPI)** : pixels par pouce — c'est *elle*, pas la résolution seule, qui détermine la netteté perçue. Un 4K en 27" est très net ; le même 4K en 65" l'est beaucoup moins vu de près.
- **Luminosité** (cd/m² ou nits) : cruciale en pièce lumineuse et pour le HDR.
- **Contraste** : écart entre le noir le plus profond et le blanc le plus clair.

### Résolutions et formats

| Nom | Pixels (16:9) |
|---|---|
| Full HD | 1920 × 1080 |
| QHD | 2560 × 1440 |
| 4K / UHD | 3840 × 2160 |
| 5K | 5120 × 2880 |
| 8K | 7680 × 4320 |

Formats (ratio) : **16:9** (universel), **16:10** (plus haut, apprécié en bureautique/code), **21:9** (ultrawide, immersif), **32:9** (super ultrawide, deux 16:9 côte à côte).

### Types de dalles

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

## 20. Fréquence, fluidité, VRR et latence

La **fréquence (Hz)** = images affichées par seconde. La différence 60 → 120 Hz est très visible (souris, défilement, jeu) ; au-delà, les gains diminuent.

- **60 / 75 / 120 / 144 / 240 / 360+ Hz** : de plus en plus fluide.
- **Tearing** : image « déchirée » quand le GPU et l'écran ne sont pas synchronisés.
- **VRR** (Variable Refresh Rate) : l'écran adapte sa fréquence à celle du GPU en temps réel. Marques : **FreeSync** (AMD), **G-Sync** (NVIDIA).
- **Temps de réponse** (ms) : rapidité de changement de couleur d'un pixel (flou de mouvement).
- **Input lag** : délai entre l'action (clic, touche) et l'affichage. Différent du temps de réponse ; critique en jeu.

> **⚠️ Erreur fréquente — le grand classique**
> « Écran 144 Hz mais Windows reste à 60 Hz. » Trois causes : (1) fréquence non réglée dans les paramètres d'affichage, (2) le **câble** ne supporte pas 144 Hz à cette résolution, (3) le **port/version** est limité (un vieux HDMI). C'est traité comme une panne complète au chapitre 47.

---

## 21. HDR, couleurs et calibration

### HDR : la plage dynamique

Le **HDR** élargit l'écart entre zones sombres et claires. Formats : **HDR10** (base ouverte), **HDR10+** et **Dolby Vision** (métadonnées dynamiques, image par image), certification **VESA DisplayHDR** (400, 600, 1000…).

> **⚠️ Erreur fréquente**
> Acheter un écran « HDR » certifié **DisplayHDR 400** en croyant à un vrai HDR. C'est souvent un faux HDR : sans luminosité élevée (600+ nits) ni bon contraste (idéalement Mini-LED ou OLED), l'effet est négligeable, parfois pire que le SDR.

### Espaces colorimétriques

- **sRGB** : standard du web et de la bureautique.
- **DCI-P3** : plus large, cinéma et HDR.
- **Adobe RGB** : impression / photo pro.

La **calibration** (sonde + logiciel) ajuste l'écran pour des couleurs fidèles — indispensable en photo/vidéo pro.

> **🔧 Cas concret (création)**
> Un graphiste constate que ses couleurs « changent » entre son écran et le rendu client. Cause : écran non calibré et/ou espace inadapté. Une sonde de calibration et le réglage sur sRGB règlent l'écart.

---

## 22. TV vs écran PC

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
