---
title: Partie 1 — Fondations physiques
source: IT/Culture/Materiel_informatique-connectique-andco.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

Avant tout équipement, deux fondations. Sans elles, on confond énergie et données, et on croit qu'un connecteur identique garantit une fonction identique.

---

## 1. Électricité, signal et énergie

### Les trois grandeurs, par l'analogie de l'eau

- **Tension** (volts, V) = la *pression* dans le tuyau.
- **Courant** (ampères, A) = le *débit*, la quantité qui passe.
- **Puissance** (watts, W) = le *travail réellement fourni*.

Relation fondamentale, à connaître par cœur :

```
Puissance (W) = Tension (V) × Courant (A)
```


Un chargeur délivrant 20 V sous 5 A fournit `20 × 5 = 100 W`. Cette formule explique pourquoi l'USB Power Delivery monte la tension (jusqu'à 48 V) pour atteindre 240 W sans faire passer un courant énorme dans le câble : à puissance donnée, plus on monte la tension, moins il faut de courant, donc moins le câble chauffe.

### AC vs DC

- **Courant alternatif (AC)** : la prise murale (230 V en Europe, 50 Hz). Le sens du courant s'inverse 50 fois par seconde.
- **Courant continu (DC)** : ce dont l'électronique a besoin. Le courant va dans un seul sens.

Un **chargeur** ou une **alimentation** convertit l'AC en DC et abaisse la tension. C'est cette conversion qui produit de la chaleur — d'où le bloc qui chauffe.

### Pourquoi une puissance annoncée est un plafond, jamais une dose imposée

C'est le malentendu le plus répandu de tout le domaine. Un chargeur annonce une puissance **maximale**. L'appareil **demande** ce dont il a besoin via une négociation ; le chargeur fournit jusqu'à sa limite. Un téléphone qui n'accepte que 18 W ne tirera que 18 W sur un chargeur 100 W, sans danger.

> **⚠️ Erreur fréquente**
> « Mon chargeur est trop puissant, il va griller mon appareil. » Faux. Le danger vient des chargeurs *contrefaits* mal régulés, pas de la puissance élevée d'un chargeur de qualité. On retrouvera ce principe du plafond pour l'USB-PD (chapitre 28) et même la charge des voitures électriques (chapitre 41).

### Signal : analogique vs numérique

Un câble transporte trois choses possibles : **énergie**, **signal analogique**, **signal numérique** — parfois plusieurs à la fois.

- **Analogique** : variation continue, comme une vague. Se dégrade *progressivement* avec la distance et le bruit. Exemples : VGA, jack 3,5 mm.
- **Numérique** : suite de 0 et 1. Effet *tout ou rien* : soit l'information passe correctement, soit elle ne passe pas (scintillements, coupures). Exemples : HDMI, DisplayPort, USB, Ethernet.

> **🎯 À retenir**
> Un câble **analogique** trop long donne une image *floue*. Un câble **numérique** trop long donne une image *parfaite ou absente* (ou des décrochages). Ce comportement différencié est un outil de diagnostic : un signal qui « papillote » est numérique en limite de tenue ; un signal « baveux » est analogique dégradé.

### Le vocabulaire qui revient partout

- **Débit / bande passante** : volume de données par seconde (Mb/s, Gb/s). **8 bits = 1 octet** : une ligne « 1 Gb/s » fait au mieux ~125 Mo/s. Le facteur 8 piège tout le monde.
- **Latence** : délai avant que la donnée arrive. Une liaison peut avoir un gros débit *et* une mauvaise latence (cruciale en jeu, visio, audio live).
- **Blindage** : protection métallique contre les perturbations extérieures (UTP/FTP/STP en Ethernet, voir chapitre 34).
- **Interférences** : perturbations électromagnétiques qui dégradent un signal mal protégé.

---

## 2. Connecteur, câble, protocole : la distinction fondatrice

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
