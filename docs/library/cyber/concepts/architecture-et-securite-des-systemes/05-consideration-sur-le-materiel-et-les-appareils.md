---
title: Considération sur le matériel et les appareils
source: Cyber/11 Concepts/Architecture et sécurité des systèmes.md
note: Architecture et sécurité des systèmes
up:
- - Architecture et sécurité des systèmes
  - index.md
---

## BIOS /UEFI

- Le BIOS contient le code nécessaire à l’initialisation du matériel et permet de configurer différents paramètres via le setup BIOS/CMOS.
- Côté sécurité :
	- contrôler le **boot order** ;
	- éviter le boot depuis :
	    - USB ;
	    - CD/DVD ;
	    - réseau/PXE ;
	- privilégier le disque local.

```
Boot externe autorisé
→ attaquant démarre sur un Live OS
→ peut tenter d'accéder aux données locales
```


→ Protéger également l’accès au BIOS/UEFI avec un mot de passe administrateur.
## Sécurité USB

- Les clés USB facilitent le transport de données hors de l’entreprise.
- Mesures :
	- définir quelles données peuvent être stockées sur USB ;
	- interdire les supports personnels si nécessaire ;
	- mettre en place station blanche ;
	- dans les environnements sensibles, **désactiver complètement les ports USB**.

```
USB → risque d'exfiltration + introduction de malware
```

## Smartphones & Tablettes

- Les appareils mobiles contiennent souvent :
	- contacts professionnels ;
	- documents ;
	- emails ;
	- accès Internet et applications internes.
- Mesures principales :
	- gestion du cycle de vie, via mdm ;
	- verrouillage de l’appareil ;
	- chiffrement des données ;
	- analyser les vulnérabilités des appareils utilisés dans l’organisation.
- Vulnérables à plusieurs types d'attaques : 
	- Bluesnarfing : Connexion Bluetooth non autorisée permettant de **récupérer des données** depuis l’appareil.
	- Bluejacking : Envoi de **messages non sollicités** entre appareils Bluetooth.
	- Bluebugging : Exploit Bluetooth qui permet à un pirate d'accéder aux fonctionnalités du téléphone. Peut permettre, par exemple, de passer des appels via des commandes AT.

```
Bluesnarfing → récupérer des données
Bluejacking  → envoyer des messages
Bluebugging  → contrôler certaines fonctions
```

## Stockage amovible

- Les supports amovibles peuvent :
	- introduire des malwares ;
	- permettre l’exfiltration de données ;
	- être perdus ou volés.
- Exemple :

```
USB personnel infecté
→ connecté au poste professionnel
→ malware introduit sur le réseau
```

- Mesures :
	- interdire les supports amovibles si possible ;
	- interdire les supports personnels ;
	- interdire la sortie des supports ;
	- mettre en place station blanche ;
	- formaliser cette règle dans la politique de sécurité ;
	- lorsqu’ils sont nécessaires :
	    - les retirer lorsque l’utilisateur quitte son poste ;
	    - les stocker dans une armoire sécurisée.
	- La même logique peut s’appliquer aux laptops laissés sans surveillance.
## Stockage en réseau (NAS)

- Un **NAS** fournit un stockage central accessible via le réseau.
- La sauvegarde des données sur un NAS est essentielle, car il peut stocker toutes les données de l'entreprise en un seul endroit.
- Caractéristiques :
	- ses paramètres peuvent être gérés via une interface web ;
	- plusieurs disques ;
	- souvent RAID / tolérance aux pannes ;
	- partage de fichiers centralisé ;
	- compatible avec différents OS/protocoles.
- Exemples :

```
Windows → SMB
Linux   → NFS
```

### Risques / protections

- **Access Control**
    - un NAS compromis peut exposer une grande quantité de données ;
    - éviter son exposition directe à Internet.
- **Malware**
    - un malware peut toucher de nombreux fichiers centralisés ;
    - scanner régulièrement les données.
- **Authentication / Authorization**
    - contrôler précisément qui peut accéder aux fichiers.
- **Encryption**
    - protéger les données stockées et, si possible, les communications.
- **Backups**
    - RAID ≠ backup ;
    - conserver des sauvegardes séparées du NAS.
## PBX  - Téléphonie

- Un **PBX (Private Branch Exchange)** est un système téléphonique utilisé au sein d'une entreprise pour gérer tous les appels téléphoniques internes, permettant de gérer plusieurs extensions à partir de l’infrastructure téléphonique de l’entreprise.
-  Il permet à une entreprise d'avoir une seule ligne téléphonique externe tout en prenant en charge plusieurs systèmes et numéros de téléphone internes. Chaque téléphone de l'entreprise se voit attribuer un numéro de poste unique.
- Mesures de sécurité :
	-  Contrôle physique :
		- placer le PBX dans une salle verrouillée ;
		- accès limité ;
		- dispositifs anti-sabotage ;
		- inspection régulière du matériel.
	- Paramètres par défaut :
		- changer les comptes/passwords par défaut ;
		- sécuriser l’administration distante.
## Risques de sécurité avec les systèmes embarqués et spécialisés
### Raspberry Pi

- petit système contenant CPU, RAM et interfaces ;
- utilisé pour créer des systèmes personnalisés.

Sécurité :

- désactiver les fonctionnalités inutiles, ex. Bluetooth.
### FPGA - **Field-Programmable Gate Array**

- circuit intégré pouvant être programmé pour exécuter des fonctions matérielles personnalisées.
### Arduino

- carte basée sur microcontrôleurs ;
- utilisée pour créer des systèmes électroniques ;
- généralement programmée en C/C++.
#### Autres systèmes embarqués

| Technologie                                                | À savoir                                                                                                                                          |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HVAC / CVC**                                             | Systèmes informatisés contrôlant chauffage, ventilation, climatisation                                                                            |
| Système sur une puce **SoC**                               | Puce intégrant diverses fonctionnalités comme des processeurs (CPU) et des processeurs graphiques (GPU). Exemple : Raspberry Pi.                  |
| Système d'exploitation en temps réel **RTOS**              | OS conçus pour traiter les données en temps réel.                                                                                                 |
| Imprimantes/Appareils multifonctions **MFD / Imprimantes** | Peuvent stocker des documents dans leur mémoire/disque et exposer une interface Web                                                               |
| **Surveillance Systems**                                   | Comprennent des caméras avec des systèmes embarqués qui peuvent se connecter à un serveur central ou à Internet, posant des risques d'exposition. |
| **Drones**                                                 | Véhicules aériens pilotés à distance                                                                                                              |
| **VoIP**                                                   | Technologie pour la communication vocale sur des réseaux TCP/IP comme Internet.                                                                   |
## SCADA / ICS
### SCADA - Supervisory Control and Data Acquisition

- utilisé pour superviser et contrôler des processus industriels.
- Exemples :
    - HVAC ;
    - éclairage ;
    - réfrigération ;
    - systèmes industriels.
- La sécurité physique est importante car une manipulation peut perturber :
	- supervision ;
	- alarmes ;
	- fonctionnement industriel.
### ICS - Industrial Control Systems

- Terme plus large (qui inclut les systèmes SCADA) regroupant les systèmes utilisés pour surveiller/contrôler des équipements industriels.

```
ICS
 ├─ SCADA
 └─ autres systèmes de contrôle industriel
```

- Présents notamment dans :
	- usines ;
	- manufacturing ;
	- production d’énergie.
## IoT - Internet of Things

- Les appareils **IoT** communiquent avec d’autres systèmes via Internet ou des réseaux locaux.
- Leur sécurité peut être faible lorsque les fabricants privilégient la **connectivité et la simplicité** aux contrôles de sécurité.
-  Catégories
	- **Sensors**
	    - thermostats ;
	    - caméras ;
	    - capteurs environnementaux.
	- **Smart Devices** : appareils connectés au réseau qui communiquent avec d'autres en utilisant des technologies telles que :
	    - Wi-Fi ;
	    - Bluetooth ;
	    - réseau cellulaire.
	- **Wearables**
	    - smartwatch ;
	    - objets portés sur le corps ;
	    - souvent reliés au smartphone.
	- **Facility Automation** : Systèmes conçus pour contrôler les éléments de :
	    - HVAC/CVC ( (chauffage, ventilation et climatisation)) ;
	    - automatisation du bâtiment.
- Weak Default Settings
	- Problème fréquent :

```
Default username/password
Default services
Default network settings
```

→ les attaquants connaissent souvent ces configurations.

- Mesures :
	- changer les credentials par défaut ;
	- désactiver les services inutiles ;
	- patcher/mettre à jour si possible ;
	- segmenter les appareils IoT du reste du réseau.
