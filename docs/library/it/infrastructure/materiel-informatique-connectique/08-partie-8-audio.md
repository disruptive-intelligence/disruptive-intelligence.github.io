---
title: Partie 8 — Audio
source: IT/06 Infrastructure & architecture/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

---

## 31. Jack, audio numérique et DAC

### Jack 3,5 mm

Prise audio analogique universelle. Le nombre d'anneaux change tout :

- **TRS** (2 anneaux) : stéréo *sans* micro.
- **TRRS** (3 anneaux) : stéréo *avec* micro.

Deux câblages TRRS incompatibles existent : **CTIA** (standard actuel) et **OMTP** (ancien). Croisés, le micro ne marche pas ou le son est déformé.

### Analogique, numérique et DAC

- **Signal analogique** : la variation de tension qui *est* le son (vers le casque).
- **DAC** (Digital-to-Analog Converter) : convertit le numérique de l'appareil en analogique. Toute sortie casque en contient un.
- **ADC** : l'inverse, pour numériser un micro.
- **Carte son / interface audio** : DAC et ADC de meilleure qualité que ceux de base.

> **🎯 À retenir**
> Compter les anneaux : 2 = pas de micro (TRS), 3 = micro (TRRS). Et la qualité du **DAC** compte souvent plus que la résolution du fichier : un bon DAC externe transforme le rendu d'un casque.

> **🔧 Cas concret**
> Casque-micro dont l'audio marche mais pas le micro sur un appareil : incompatibilité CTIA/OMTP, ou port qui n'accepte que du TRS. Un adaptateur CTIA↔OMTP ou en Y (deux prises séparées) résout.

---

## 32. XLR, alimentation fantôme et audio pro

- **XLR** : connecteur rond verrouillable à 3 broches, **symétrique** : il annule les parasites sur de longues distances. D'où son usage en studio et sur scène.
- **Micro dynamique** : robuste, sans alimentation, pour la scène et les voix fortes.
- **Micro statique (condensateur)** : sensible et détaillé, **nécessite une alimentation fantôme 48 V** (notée +48V / P48).
- **Alimentation fantôme 48 V** : tension envoyée par l'interface/la table *dans le câble XLR* pour alimenter le micro statique.
- **Interface audio / table / préampli** : amplifient et numérisent le signal pour l'ordinateur.

> **⚠️ Erreur fréquente**
> Brancher un micro statique sans activer le +48V : aucun son ou signal très faible. Un grand classique du home-studio. Inversement, le 48V peut endommager certains matériels sensibles (anciens micros à ruban) — d'où l'interrupteur dédié.

---

## 33. Bluetooth et audio du salon

### Bluetooth audio

- **Codecs** : SBC (base), AAC (Apple), aptX / aptX HD (Qualcomm/Android), LDAC (Sony, haute résolution).
- **Latence** : le Bluetooth introduit un délai — gênant en jeu et en vidéo (lèvres désynchronisées).
- **Multipoint** : connexion à deux appareils à la fois.

> **⚠️ Erreur fréquente**
> Vouloir jouer ou produire de la musique en Bluetooth : la latence le rend pénible. Pour le jeu compétitif et la production, filaire ou dongle radio dédié.

### Audio du salon : RCA, optique, ARC/eARC

- **RCA** : fiches rouge/blanc, audio analogique stéréo.
- **Toslink (optique)** : audio **numérique** par fibre optique (lumière), insensible aux parasites électriques.
- **SPDIF** : le *protocole* audio numérique, en optique (Toslink) ou coaxial.
- **HDMI ARC/eARC** : la TV renvoie le son vers un ampli/barre de son ; l'**eARC** gère les formats non compressés (Dolby Atmos).

> **🎯 À retenir**
> Pour relier une TV à une barre de son aujourd'hui : **HDMI eARC** (qualité maximale + télécommande unique via CEC). L'optique reste un bon plan B mais limité pour les formats surround récents.

> **🔧 Cas concret**
> Barre de son en optique qui ne reçoit pas le surround d'un service de streaming : l'optique ne porte pas les formats les plus récents. Passer en HDMI eARC débloque le Dolby Atmos, si TV, câble et barre le supportent tous les trois.

---
