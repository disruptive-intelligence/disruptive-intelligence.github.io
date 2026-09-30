---
title: Différents types de logiciels malveillants
source: Cyber/99_Concepts/HTB_Identification des menaces et des logiciels malveillants.md
note: HTB — Identification des menaces et des logiciels malveillants
up:
- - HTB — Identification des menaces et des logiciels malveillants
  - index.md
---

## Spyware

- Logiciel espion, installé discrètement pour surveiller l'activité d'un utilisateur et transmettre les informations à un système distant.
- Peut notamment :
	- suivre la navigation ;
	- collecter des informations ;
	- modifier certains paramètres système ;
	- rediriger le navigateur ;
	- dégrader les performances réseau.
## Adware

- **Adware** : logiciel qui affiche automatiquement des publicités, souvent sous forme de pop-ups.
- Peut chercher à pousser l’utilisateur vers des produits ou services.
## Spam

- Le spam désigne les courriels commerciaux non sollicités qui inondent les boîtes de réception.
- Envoi massif d’**emails non sollicités**, généralement pour promouvoir produits/services.
- Les spammeurs peuvent récupérer des adresses via :
    - sites Web ;
    - forums/groupes de discussion ;
    - listes d’adresses achetées.
- Des **spambots** automatisent la collecte d’adresses visibles publiquement.
- Prévention :
	- filtres antispam ;
	- éviter d’exposer inutilement des adresses email publiques.
## Rootkit

- **Rootkit** : malware conçu pour maintenir un **accès privilégié et furtif** au système.
- Son objectif principal est souvent de **cacher sa présence ou celle d’autres composants malveillants**.

| Type                                                  | Principe                                                                                                                                                                                                                                |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rootkits au niveau applicatif - **Application-level** | Fichiers exécutables qui fonctionnent en mode utilisateur, tels que les virus de type cheval de Troie, permettant aux pirates d'accéder au système discrètement.                                                                        |
| rootkits au niveau bibliothèque - **Library-level**   | Remplacement/modification de DLL pour dissimuler l’activité                                                                                                                                                                             |
| rootkits au niveau du noyau - **Kernel-level**        | Chargés par le noyau du système d'exploitation, souvent en remplaçant des fichiers drivers. Ils fonctionnent en mode noyau, accordant un accès étendu au système et le potentiel de causer des dommages importants.                     |
| rootkits virtualisés - **Virtualized**                | Se charge sous/avant l’OS et l’exécute dans un environnement virtualisé. Leur furtivité réside dans le fait que le système d'exploitation reste inconscient de cette virtualisation.                                                    |
| rootkits de firmware - **Firmware**                   | Implanté directement dans le firmware d’un périphérique/système. indépendamment du système d'exploitation. Leur détection est particulièrement difficile en raison de leur intégration profonde dans les opérations au niveau matériel. |

- Plus le rootkit est bas dans la stack → plus sa détection peut être difficile
## Botnet

- **Botnet** : ensemble de systèmes compromis contrôlés par un attaquant.
- Chaque système compromis est appelé :
    - **bot** ;
    - **zombie**.
- Le botnet peut être utilisé pour :
    - spam ;
    - DoS/DDoS ;
    - autres attaques coordonnées.
- L’accès au botnet peut également être loué à d’autres attaquants.
## RAT — Remote Access Trojan

- Malware donnant à un attaquant un **accès distant au système compromis**.
- Peut arriver via :
    - logiciel apparemment légitime ;
    - pièce jointe ;
    - téléchargement malveillant.
- Une fois installé :
    - crée une backdoor ;
    - permet l’exécution de commandes à distance ;
    - peut servir à compromettre d’autres systèmes.

```
Trojan installé
→ backdoor
→ Remote Access
→ exécution de commandes
```

- RAT vs Trojan

```
Trojan → méthode de camouflage / installation
RAT    → fonctionnalité de contrôle distant
```

	- Un RAT peut donc être distribué sous forme de Trojan.
## Keylogger

- Outil logiciel ou matériel conçu pour capturer toutes les frappes de touches effectuées sur un système.
- Hardware Keylogger
	- Petit dispositif placé physiquement entre → l’attaquant le récupère ensuite pour consulter les données.
- Software Keylogger
	- fonctionne en arrière-plan ;
	- enregistre les touches :
	    - dans un fichier local ;
	    - ou les transmet à distance.
## Backdoor

- Méthode d’accès alternative permettant à l’attaquant de revenir sur le système sans utiliser le point d’entrée initial.
- Peut être créée via :
    - Trojan ;
    - service/port malveillant ;
    - compte utilisateur ajouté ;
    - autre mécanisme de persistence.

```
Compromission initiale
       ↓
Backdoor
       ↓
Accès futur
```

## Ransomware

- Malware qui chiffre ou bloque les données/systèmes afin d’exiger une rançon.
- L’attaquant conserve la possibilité de déchiffrement et demande un paiement.
## PUP — Potentially Unwanted Program

- Logiciel installé en même temps qu’un programme souhaité mais **non désiré par l’utilisateur**.
- Peut :
    - afficher de la publicité ;
    - installer des toolbars ;
    - ralentir le système ;
    - collecter certaines informations.
- Prévention :
	- lire les écrans d’installation ;
	- décocher les logiciels supplémentaires ;
	- anti-malware.

```
PUP ≠ forcément malware pur
mais
PUP → logiciel indésirable / potentiellement intrusif
```

## Virus sans fichier -  Fileless Malware

- Malware fonctionnant **principalement en mémoire** plutôt qu’en déposant un exécutable classique sur disque.
- Peut s’appuyer sur des processus ou outils déjà présents sur le système.

> **Fileless** ne veut pas nécessairement dire « absolument aucun fichier n’existe jamais », mais que l’exécution malveillante repose principalement sur la mémoire et/ou des composants légitimes.
## Command & Control — C2 / C&C

- Après compromission, les malwares peuvent communiquer avec un serveur **Command & Control**.
- Le C2 permet à l’attaquant :
    - d’envoyer des commandes ;
    - de contrôler les machines ;
    - d’exfiltrer des données ;
    - de perturber le système ;
    - de télécharger d’autres payloads.

```
Attacker
   ↓
C2 Server
   ↓
Compromised Host
```

- Le **C2 n’est pas un type de malware**, mais une infrastructure/méthode de communication utilisée par les malwares.
## Cryptomalware

- Malware qui **chiffre les fichiers sans autorisation**.
- Souvent utilisé comme composant d’un ransomware :
    - fichiers chiffrés ;
    - accès impossible ;
    - demande de paiement.

```
Cryptomalware → action = chiffrement
Ransomware    → objectif = extorsion
```

- Les deux concepts se recouvrent souvent, mais ne sont pas strictement synonymes.
## Polymorphic Malware

- Malware qui **modifie son apparence/code** afin d’éviter les détections basées sur des signatures statiques.
- Le comportement général peut rester identique malgré les modifications.

```
Version A → Signature A
Version B → Signature B
Version C → Signature C

même comportement général
```

→ rend les signatures antivirus traditionnelles moins efficaces.
## Virus blindé - Armored Virus

- Malware conçu pour rendre son **analyse / reverse engineering difficile**.
- Peut employer des techniques empêchant ou compliquant :
    - décompilation ;
    - debugging ;
    - analyse statique/dynamique.

```
Polymorphic → évite surtout la détection
Armored     → complique surtout l'analyse
```
