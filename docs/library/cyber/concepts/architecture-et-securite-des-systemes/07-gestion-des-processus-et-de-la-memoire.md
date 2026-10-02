---
title: Gestion des Processus et de la Mémoire
source: Cyber/11 Concepts/Sous le capot/Architecture et sécurité des systèmes.md
note: Architecture et sécurité des systèmes
up:
- - Architecture et sécurité des systèmes
  - index.md
---

- Le système d’exploitation sert d’interface entre **hardware et software** et gère notamment :
    - processus ;
    - mémoire ;
    - fichiers ;
    - réseau.
- Comprendre ces mécanismes est important en **Incident Response** et **Threat Hunting**, car beaucoup d’activités malveillantes apparaissent sous forme de processus, threads ou modifications mémoire.
## Gestion des Processus — Process Management

- Le système d’exploitation gère les processus en cours d’exécution et leur attribue les ressources nécessaires :
    - CPU ;
    - mémoire ;
    - périphériques d’I/O.
- Il gère notamment leur création, leur état, leur priorité et leur temps CPU.
### Processus

- Un **processus** est une instance d’un programme en cours d’exécution.
- Il possède notamment :
    - un espace mémoire ;
    - des ressources ;
    - un identifiant (**PID**) ;
    - un ou plusieurs threads.

```
Program → fichier/code sur disque
Process → instance de ce programme en exécution
Thread  → unité d'exécution au sein du processus
```

- En sécurité, le couple **processus parent / enfant** est particulièrement utile pour détecter des comportements suspects.

```
winword.exe
   ↓
powershell.exe
```

→ peut mériter une investigation selon le contexte.
### État d’un processus

- Un processus peut passer par plusieurs états selon l’OS, par exemple :

```
Ready → Running → Waiting
          ↓
      Terminated
```

- **Running** → actuellement exécuté par le CPU.
- **Ready** → prêt à être exécuté, en attente de CPU.
- **Waiting / Blocked** → attend un événement ou une ressource.
- **Terminated** → exécution terminée.

> Les noms exacts et le nombre d’états varient selon le système d’exploitation.
### Process Scheduling

- Le **scheduler** décide quel processus/thread obtient du temps CPU et à quel moment.
- Il cherche à répartir efficacement les ressources entre les différentes tâches.
- Critères possibles :
	- priorité ;
	- temps CPU déjà utilisé ;
	- état du processus ;
	- type de charge ;
	- politique de scheduling de l’OS.
### Time Sharing

- Le CPU peut être partagé entre plusieurs processus en leur attribuant de petites périodes d’exécution appelées **time slices / quanta**.
- Offrant aux utilisateurs un temps de réponse rapide.

```
CPU
→ Process A
→ Process B
→ Process C
→ Process A
```

→ donne l’impression que plusieurs programmes s’exécutent simultanément.

> Sur plusieurs cœurs CPU, plusieurs threads peuvent réellement s’exécuter **en parallèle**.
### Priorisation

- Le système d’exploitation attribue des niveaux de priorité aux processus/threads.
- Une priorité plus élevée peut permettre à une tâche d’obtenir plus rapidement du temps CPU.

```
High Priority
→ planifié avant une tâche moins prioritaire
```

→ cela ne signifie pas forcément qu’elle reçoit systématiquement toutes les ressources disponibles.
### Ordre d’exécution

- L’ordre dépend de plusieurs facteurs :
	- priorité ;
	- état `Ready/Waiting` ;
	- algorithme de scheduling ;
	- temps CPU disponible ;
	- événements système.
### Concurrence / Parallélisme / Synchronisme

- À distinguer :

```
Concurrency
→ plusieurs tâches progressent dans le temps

Parallelism
→ plusieurs tâches s'exécutent réellement en même temps
```

Le parallélisme nécessite généralement plusieurs cœurs/processeurs.
### Intérêt sécurité des processus

- En Incident Response / Threat Hunting, on examine souvent :
	- PID / PPID ;
	- nom et chemin de l’exécutable ;
	- utilisateur ayant lancé le processus ;
	- ligne de commande ;
	- parent / enfant ;
	- connexions réseau ;
	- processus inhabituels ou non signés.

```
Process Tree
+ Command Line
+ User
+ Network Connections
→ contexte d'investigation
```

## Gestion de la Mémoire — Memory Management

- Le système d’exploitation gère :
    - allocation ;
    - suivi ;
    - partage ;
    - libération des zones mémoire.
- Objectifs :
    - utiliser efficacement la RAM ;
    - isoler les processus ;
    - garantir stabilité et performances.
### Hiérarchie mémoire
Une hiérarchie simplifiée :

```
Registers
↓
CPU Cache
↓
RAM
↓
SSD / HDD
```

- Plus on monte :
	- plus rapide ;
	- plus petit ;
	- plus coûteux.
- Plus on descend :
	- plus lent ;
	- plus grande capacité.
### Mémoire principale — RAM

- La **RAM** contient notamment :
    - code actuellement exécuté ;
    - données des programmes ;
    - structures utilisées par l’OS.
- Elle est volatile :

```
Power Off
→ contenu RAM perdu
```

### Mémoire virtuelle — Virtual Memory

- La mémoire virtuelle fournit à chaque processus un **espace d’adressage virtuel** indépendant.
- Le système d’exploitation traduit les adresses virtuelles vers la mémoire physique.
- Un mécanisme d'extension de la mémoire créé sur un disque dur ou un autre périphérique de stockage, utilisé pour soutenir la mémoire principale.

```
Process
→ Virtual Address
→ OS / MMU
→ Physical RAM
```

- Lorsqu’il manque de RAM, certaines pages peuvent être déplacées vers un stockage secondaire :
	- Windows → **pagefile**
	- Linux → **swap**

> ⚠️ La mémoire virtuelle n’est pas simplement « de la RAM supplémentaire sur disque ». C’est avant tout un **mécanisme d’abstraction et de gestion de l’espace mémoire** ; le disque peut servir de backing storage.
### Opérations de gestion de la mémoire

- Cela inclut des processus tels que l'allocation, le suivi, la libération et le partage des espaces mémoire effectués par le système d'exploitation. Voici quelques-unes des principales opérations de gestion de la mémoire :
#### Allocation

- L’OS réserve de la mémoire aux processus selon leurs besoins.

```
Process requests memory
→ OS allocates memory
```

#### Suivi

- Le système maintient l’état des zones mémoire :
	- utilisées ;
	- libres ;
	- associées à certains processus ;
	- partagées.
#### Désallocation / Deallocation

- Lorsqu’une zone n’est plus nécessaire, elle peut être libérée et réutilisée.

```
Process ends
→ memory released
→ available again
```

#### Shared Memory

- Plusieurs processus peuvent partager certaines zones mémoire.
- Permet notamment :
    - communication inter-processus (**IPC**) ;
    - réduction des duplications ;
    - meilleure utilisation des ressources.

```
Process A ─┐
           ├→ Shared Memory
Process B ─┘
```

### Stratégies de gestion mémoire

-  Les stratégies de gestion de la mémoire du système d'exploitation concernent l'allocation de mémoire, la libération de mémoire, le partage de mémoire et la fragmentation de la mémoire. Voici quelques stratégies courantes de gestion de la mémoire :
#### Mémoire physique

- Le système d'exploitation alloue des blocs de mémoire physique aux programmes et effectue un suivi.

|Stratégie|Principe|
|---|---|
|**First-fit**|Utilise le premier bloc suffisamment grand|
|**Best-fit**|Cherche le bloc qui correspond le mieux à la taille nécessaire|
|**Worst-fit**|Utilise le plus grand bloc disponible|

→ elles illustrent les problématiques d’allocation et de **fragmentation**.

> Ces stratégies sont surtout associées aux modèles classiques d’allocation contiguë ; les OS modernes utilisent largement des mécanismes de **paging** et d’allocation plus complexes.
#### Gestion de la mémoire virtuelle

- L"'OS gère la mémoire dans une structure qui peut basculer entre la mémoire principale et la mémoire virtuelle
- Cela permet :
    - d’exécuter davantage de programmes ;
    - d’isoler leurs espaces mémoire ;
    - d’utiliser plus efficacement la RAM.

```
RAM pleine
→ certaines pages déplacées vers swap/pagefile
→ RAM libérée
```

- Un usage excessif du swap/pagefile peut cependant fortement dégrader les performances.
### Mémoire et sécurité
La mémoire est également importante lors d’une investigation car elle peut contenir :

- processus actifs ;
- connexions ;
- commandes ;
- clés/credentials présents temporairement ;
- malware exécuté uniquement en mémoire.

```
Fileless Malware
→ peu ou pas de fichier sur disque
→ activité principalement en mémoire
```

→ l’**analyse mémoire** peut donc révéler des éléments absents du disque.
