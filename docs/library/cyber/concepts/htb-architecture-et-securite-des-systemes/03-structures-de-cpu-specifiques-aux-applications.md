---
title: Structures de CPU Spécifiques aux Applications
source: Cyber/04_Hardening/HTB_Architecture et sécurité des systèmes.md
note: HTB — Architecture et sécurité des systèmes
up:
- - HTB — Architecture et sécurité des systèmes
  - index.md
---

- Les CPU sont le composant exécutif de base de tous les systèmes informatiques, en particulier des PC et des systèmes de serveurs.
- Les CPU sont également développés et utilisés sous diverses formes en fonction d'exigences spécifiques.
- Tous les systèmes n’utilisent pas un CPU généraliste comme ceux des PC/serveurs. Selon les besoins, on utilise aussi des architectures spécialisées :

```
Microcontrôleur
FPGA
ASIC
```

- Le choix dépend notamment de :
	- performance ;
	- consommation ;
	- coût ;
	- flexibilité ;
	- capacité de reprogrammation ;
	- usage prévu.
## Microcontrôleur — MCU

- Un **microcontrôleur** regroupe dans un même circuit intégré :
    - CPU ;
    - mémoire ;
    - ports I/O ;
    - timers / counters ;
    - parfois interfaces de communication.

```
Microcontroller
├─ CPU
├─ RAM / Flash
├─ GPIO
├─ Timers
└─ Communication Interfaces
```

### Caractéristiques

- faible consommation ;
- faible coût ;
- petite taille ;
- programmable ;
- conçu généralement pour une tâche spécifique.

Le logiciel embarqué est souvent appelé **firmware**.

```
Hardware
+
Firmware
→ Embedded Device
```

### Domaines d’utilisation
Les microcontrôleurs sont très présents dans les **Systèmes embarqués** :

- IoT ;
- automobile ;
- dispositifs médicaux ;
- équipements industriels ;
- appareils électroniques.
- Exemples de familles :
	- PIC12 / PIC16 / PIC18 / PIC32 ;
	- MSP430 ;
	- STM32 ;
	- NXP LPC / S32K ;
	- Renesas RA / RX.
### Limites

- Généralement moins puissants qu’un CPU généraliste moderne.
	- Cette structure flexible entraîne une perte de vitesse et de performance par rapport aux CPU.
	- Peuvent pas être utilisés dans des environnements qui nécessitent grande puissance de traitement.
- Optimisés pour :
    - contrôle ;
    - faible consommation ;
    - temps réel ;
    - tâches spécifiques,

plutôt que pour exécuter des workloads lourds de PC ou serveur.

> En sécurité, les microcontrôleurs sont importants car une vulnérabilité dans le **firmware** peut compromettre directement un équipement embarqué ou IoT.
## FPGA — Field-Programmable Gate Array

- Un **FPGA** est un circuit intégré contenant des blocs logiques et interconnexions **reconfigurables**.
- Contrairement à un microcontrôleur, on ne programme pas seulement le logiciel exécuté : on peut modifier la **logique matérielle elle-même**.

```
Microcontroller
→ hardware fixe
→ software programmable

FPGA
→ logique hardware reconfigurable
```

### Programmation

- Les FPGA sont généralement décrits avec des **Hardware Description Languages (HDL)** :
	- Verilog ;
	- VHDL.

```
VHDL / Verilog
→ Hardware Description
→ Synthesis
→ FPGA Configuration
```

- Ils permettent de créer :
	- circuits logiques spécifiques ;
	- accélérateurs ;
	- interfaces matérielles ;
	- parfois un processeur soft-core.
### Caractéristiques

- Avantages :
	- forte parallélisation ;
	- haute performance sur certains traitements ;
	- reprogrammable ;
	- architecture personnalisable.
- Inconvénients :
	- coûts plus élevés que les microcontrôleurs, tant en termes d'acquisition que de mise en œuvre ;
	- développement plus complexe ;
	- besoin de compétences hardware/HDL.
### Domaines d’utilisation

- systèmes militaires ;
- satellites ;
- systèmes de traitement du signal nécessitant une grande vitesse ;
- télécommunications ;
- traitement du signal ;
- accélération matérielle ;
- applications nécessitant une faible latence.

Fournisseurs cités :

- Xilinx ;
- Lattice Semiconductor ;
- Intel / Altera ;
- Microchip ;
- QuickLogic.

> Xilinx appartient aujourd’hui à **AMD**, mais le nom Xilinx reste très présent dans l’écosystème FPGA.
## ASIC — Application-Specific Integrated Circuit

- Un **ASIC** est un circuit intégré conçu pour une **fonction précise**.
- Contrairement au FPGA, sa logique est essentiellement fixée lors de la fabrication.

```
FPGA
→ reconfigurable après fabrication

ASIC
→ architecture fixée à la fabrication
```

### Caractéristiques
Les ASIC sont optimisés pour une tâche particulière, ce qui permet généralement :

- performances élevées ;
- faible consommation ;
- faible latence ;
- meilleure efficacité pour la fonction ciblée.

Mais :

- conception complexe ;
- coût initial très élevé ;
- fabrication longue ;
- erreurs de design difficiles ou impossibles à corriger après production.

```
ASIC
→ High Development Cost
→ High Efficiency
→ Low Flexibility
```

### Domaines d’utilisation
Les ASIC peuvent être utilisés dans :

- smart cards ;
- cartes bancaires ;
- passeports électroniques ;
- équipements réseau ;
- accélérateurs cryptographiques ;
- hardware spécialisé.

> Une **smart card** peut contenir un circuit spécialisé avec CPU, mémoire et fonctions cryptographiques ; ce n’est pas forcément un ASIC « simple » au sens strict.
## Comparaison MCU / FPGA / ASIC

|               | Microcontrôleur      | FPGA                     | ASIC                             |
| ------------- | -------------------- | ------------------------ | -------------------------------- |
| Hardware      | Fixe                 | Reconfigurable           | Fixe                             |
| Programmation | Firmware/software    | HDL / logique matérielle | Conception avant fabrication     |
| Flexibilité   | Élevée côté software | Très élevée              | Faible                           |
| Performance   | Modérée              | Élevée selon usage       | Très élevée                      |
| Consommation  | Faible               | Variable                 | Très optimisée                   |
| Coût initial  | Faible               | Moyen / élevé            | Très élevé                       |
| Usage         | Embedded / IoT       | Traitement spécialisé    | Fonction dédiée à grande échelle |


```
MCU
→ flexible par software

FPGA
→ flexible par hardware

ASIC
→ optimisé pour une fonction fixe
```

## Vue sécurité

Ces composants peuvent présenter des surfaces d’attaque différentes :
### MCU

- firmware vulnérable ;
- debug interfaces ;
- insecure boot ;
- extraction de firmware.
### FPGA

- bitstream exposé ;
- configuration malveillante ;
- protection insuffisante de la logique.
### ASIC

- vulnérabilité matérielle difficile à corriger ;
- backdoor hardware ;
- erreurs de conception permanentes.

```
Plus le hardware est fixe
→ plus une erreur de conception peut être difficile à corriger
```
