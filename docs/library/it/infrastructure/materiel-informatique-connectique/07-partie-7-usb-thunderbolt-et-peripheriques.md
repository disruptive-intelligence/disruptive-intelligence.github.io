---
title: Partie 7 — USB, Thunderbolt et périphériques
source: IT/Culture/Materiel_informatique-connectique-andco.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

L'une des parties les plus densifiées, car c'est le terrain où la confusion connecteur/câble/protocole fait le plus de dégâts — et où les standards ont récemment beaucoup bougé.

---

## 27. Comprendre l'USB : connecteurs et standards

L'USB mélange deux choses qu'il faut séparer : **formes** et **vitesses**.

### Les formes (connecteurs)

- **USB-A** : le rectangle classique.
- **USB-B** : carré (imprimantes, certains périphériques).
- **Mini-USB** / **Micro-USB** : anciens, sur vieux appareils et téléphones d'avant l'USB-C.
- **USB-C** : ovale, réversible, le standard actuel.

### Les vitesses (standards) — et le chaos des renommages

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

## 28. USB-C, USB4 et USB Power Delivery

### USB-C : un connecteur, des capacités très variables

Ce qu'un câble/port USB-C *peut* faire, indépendamment de sa forme :

- **Données** : de 480 Mb/s (USB 2.0) à 80 Gb/s (USB4 v2).
- **Charge** : de quelques watts à 240 W.
- **Vidéo** : seulement si DisplayPort Alt Mode présent (chapitre 26).
- **Thunderbolt** : seulement sur ports/câbles certifiés (chapitre 29).

> **🎯 À retenir — l'idée centrale de l'USB-C**
> Le connecteur USB-C est une **promesse de forme**, pas de fonction. Avant d'attendre vidéo, charge rapide ou haut débit, vérifier que **le câble ET le port** supportent cette fonction précise.

### USB4 et USB4 Version 2.0 (80 Gb/s, mode asymétrique 120 Gb/s)

USB4 unifie l'écosystème en s'appuyant sur Thunderbolt 3, avec tunnelisation du DisplayPort et du PCIe sur le connecteur USB-C. Sa première génération existe en 20 ou 40 Gb/s. La **Version 2.0**, publiée par l'USB-IF le 18 octobre 2022 (en même temps que la spécification USB-C 2.2 et l'USB PD 3.1), double le débit symétrique à 80 Gb/s et introduit un **mode asymétrique** atteignant jusqu'à 120 Gb/s dans un sens (et 40 Gb/s dans l'autre).

Le principe de l'asymétrie : au lieu de répartir 80 Gb/s en 40 montants / 40 descendants, le système peut réallouer dynamiquement la bande passante — par exemple trois voies en émission et une en réception — pour atteindre 120 Gb/s vers un écran haute résolution tout en gardant 40 Gb/s en retour. Très utile pour piloter de l'affichage 8K/16K ou un eGPU.

Cette montée à 80 Gb/s repose sur un nouvel encodage du signal, le **PAM-3**, qui transmet plus de bits par cycle tout en restant compatible avec des câbles USB-C certifiés.

### USB Power Delivery (PD) — jusqu'à 240 W

Au branchement, appareil et chargeur **négocient** tension et courant. L'USB-PD propose des paliers : 5 V, 9 V, 15 V, 20 V, puis en **PD 3.1** jusqu'à 28 V, 36 V et 48 V pour atteindre **240 W** (en mode EPR, Extended Power Range).

| Puissance | Usage typique |
|---|---|
| 30 W | Téléphone, petite tablette |
| 65 W | Ultraportable, gros téléphone |
| 100 W | PC portable performant |
| 140 W | Station mobile |
| **240 W** | Portables gaming/pro très gourmands (PD 3.1 EPR) |

### Les logos USB-IF à reconnaître

L'USB-IF a introduit des logos de certification pour lever l'ambiguïté. Sur l'emballage des câbles, on trouve désormais des mentions claires de débit (« USB 40 Gbps », « USB 80 Gbps ») et de puissance (**« 60 W »** ou **« 240 W »**). Ces deux chiffres de puissance correspondent aux deux familles de câbles :

- **60 W (3 A)** : un câble USB-C standard, **sans puce e-mark** obligatoire.
- **240 W (5 A)** : un câble **e-marked** (avec puce d'identification) requis au-delà de 60 W, signalé par le logo « 240 W ».

> **⚠️ Erreur fréquente — « mon chargeur 240 W ne charge qu'à 60 W »**
> La puissance annoncée du chargeur est un **plafond** (chapitre 1). Trois maillons décident de la puissance réelle : le **chargeur** (ce qu'il peut donner), le **câble** (un câble non e-marked bride à 60 W), et l'**appareil** (ce que sa négociation autorise). Un câble basique « charge seule » bride tout l'ensemble. Le logo « 240 W » sur le câble est le signe qu'il est e-marked.

> **🔧 Cas concret (support)**
> « Mon PC charge lentement avec le chargeur du collègue. » Vérifier les trois maillons : chargeur de puissance suffisante ? câble e-marked (logo 240 W) ou bridé à 60 W ? port du PC qui accepte l'entrée d'alimentation ? Étiqueter ses câbles évite des heures de diagnostic.

---

## 29. Thunderbolt (jusqu'à Thunderbolt 5)

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

### Thunderbolt vs USB-C, la clarification

- **USB-C** = la forme du connecteur.
- **Thunderbolt** = un protocole haut de gamme *utilisant* cette forme.

Tout port Thunderbolt est physiquement un USB-C et reste compatible USB-C ; l'inverse est faux. Le **logo éclair ⚡** à côté d'un port indique Thunderbolt (donc vidéo + données rapides + charge, en principe).

> **🔒 Sécurité — l'angle DMA, à connaître**
> Parce que Thunderbolt expose le **PCIe**, un périphérique malveillant branché peut tenter un accès **DMA** (Direct Memory Access) : lire ou écrire directement dans la mémoire de la machine, contournant l'OS — pour voler des clés, des mots de passe, ou injecter du code. C'est la base des attaques type « Thunderspy ». Détaillé au chapitre 44 ; à retenir ici : un port aussi puissant qu'un Thunderbolt est aussi une surface d'attaque puissante.

> **⚠️ Erreur fréquente**
> Acheter un câble « USB-C » bas de gamme pour un dock ou un eGPU Thunderbolt : il faut un câble **certifié Thunderbolt** (souvent marqué d'un éclair et d'un chiffre). Un câble de charge ne fera jamais passer 40-80 Gb/s ni du PCIe.

---

## 30. Périphériques, hubs et docks

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
