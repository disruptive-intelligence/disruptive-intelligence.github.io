---
title: 'Partie 10 — Énergie : chargeurs, batteries, protection'
source: IT/Culture/Materiel_informatique-connectique-andco.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

---

## 39. Chargeurs, charge rapide et charge sans fil

- **Charge lente** : ~5 W, ancien USB.
- **Charge rapide** : monte tension et/ou courant via un protocole de négociation : **USB-PD** (universel, chapitre 28), **Quick Charge** (Qualcomm), ou **protocoles propriétaires** (certaines marques chargent très vite *uniquement* avec leur chargeur maison).
- **Chauffe** : la charge rapide chauffe plus, et la chaleur use la batterie.

### Charge sans fil

- **Qi** : standard universel par induction. **Qi2** ajoute des aimants d'alignement (inspirés de MagSafe) pour un meilleur rendement.
- **Rendement** : la charge sans fil est **moins efficace** que le filaire (perte en chaleur), donc plus lente et plus chaude.

> **⚠️ Erreur fréquente**
> Attendre la charge ultra-rapide d'un téléphone avec n'importe quel chargeur. Beaucoup de charges rapides sont **propriétaires** : sans le bon chargeur ET le bon câble de la marque, on retombe sur la vitesse USB-PD standard. Ce n'est pas une panne, c'est un protocole non reconnu.

> **🎯 À retenir**
> Un bon chargeur **USB-PD multiport** de qualité couvre presque tous les besoins (téléphone, tablette, PC) et évite la multiplication des blocs. Vérifier la puissance *par port* quand plusieurs appareils chargent ensemble (elle se partage). Le sans-fil privilégie le confort, pas la vitesse.

---

## 40. Batteries lithium-ion

- **Cycles** : un cycle = une charge complète cumulée (deux fois 50 % = un cycle). Quelques centaines à ~1000 cycles avant une perte notable de capacité.
- **Capacité** : en **mAh** ou, plus rigoureusement, en **Wh** (Wh = mAh × tension / 1000). Comparer en mAh n'a de sens qu'à tension égale ; le **Wh** est la vraie mesure d'énergie.
- **Vieillissement** : accéléré par la chaleur, les charges à 100 % prolongées, les décharges à 0 %.

Bonnes pratiques : éviter la chaleur, viser ~20-80 % au quotidien (beaucoup d'appareils proposent une limite de charge à 80 %), éviter les 0 % répétés.

> **⚠️ Danger**
> Une batterie qui **gonfle** est dangereuse : on cesse de l'utiliser, on ne la perce jamais, on la fait recycler. Le gonflement annonce une dégradation pouvant mener à l'emballement thermique (incendie).

> **🔧 Cas concret**
> Portable qui « tient 20 minutes » après 4 ans : batterie en fin de cycles. Si elle n'est pas collée, son remplacement redonne une seconde vie à la machine pour bien moins cher qu'un appareil neuf. (Le cas « batterie qui se vide même branché » est traité au chapitre 47.)

---

## 41. Charge des véhicules électriques

Domaine où l'AC/DC (chapitre 1) prend tout son sens.

### AC vs DC : le point clé

- **Charge AC** : la borne fournit de l'AC ; c'est le **chargeur embarqué de la voiture** qui le convertit en DC. Limité par ce chargeur embarqué (souvent 7-22 kW). C'est la charge à domicile et sur bornes « lentes ».
- **Charge DC (rapide)** : la borne convertit elle-même et envoie du DC **directement** à la batterie, court-circuitant le chargeur embarqué. D'où les fortes puissances (50-350 kW).

### Les prises

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

## 42. Onduleurs et protection électrique

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
