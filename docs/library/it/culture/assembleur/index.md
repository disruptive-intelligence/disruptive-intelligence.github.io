---
title: Assembleur
source: IT/Culture/Assembleur.md
chapters: 10
---

### De zéro au reverse engineering débutant — Guide pour débutant absolu

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code, ne connaît pas l'algorithmique et ne connaît pas le fonctionnement interne d'un ordinateur.
> Tout ce dont tu as besoin, c'est un ordinateur avec Linux (Ubuntu/Debian recommandé) ou Windows avec WSL2.

---

### Avant de commencer — Lis ça

L'assembleur a une mauvaise réputation : "c'est trop dur", "c'est pour les génies", "c'est cryptique". **Ce n'est ni magique, ni réservé à une élite.**

Soyons honnête : l'assembleur est **plus exigeant** que Python ou Bash, parce qu'il demande de manipuler explicitement ce que les langages haut niveau te cachent — registres, mémoire, pile, tailles de données, appels système. La difficulté vient surtout du **niveau de détail**, pas d'une complexité inaccessible. Chaque ligne fait *une seule petite chose*. Ce qui rend l'assembleur intimidant, c'est :

1. Le **vocabulaire technique** qui s'accumule au début (registres, syscalls, flags, pile…) — ce cours t'introduit ces termes un par un, au bon moment.
2. Le fait qu'on ne voit **rien** par défaut (pas de `print()` automatique) — on apprend très vite à utiliser GDB pour voir ce qui se passe.
3. La **distance** avec ce qu'on connaît (cliquer, taper du texte) — ce cours fait sans cesse le pont avec Bash et Python.

> **Ce cours ne te transformera pas en hacker en 3 jours.** Il te donne les vraies fondations pour comprendre comment un ordinateur exécute du code, lire un binaire, comprendre GDB, et démarrer en reverse engineering. Le reste, c'est de la pratique.

---

### À qui s'adresse ce cours

- À quelqu'un qui n'a **jamais programmé**.
- À quelqu'un qui veut comprendre **comment un ordinateur fonctionne vraiment**.
- À quelqu'un qui s'intéresse à la **cybersécurité**, au **reverse engineering**, à l'**analyse de binaires** ou aux **CTF**.
- À quelqu'un qui a peur de GDB et veut le démystifier.

### Ce que ce cours n'est PAS

Pour rester pédagogique et accessible, certains sujets sont **volontairement exclus**. Ils méritent un cours à part, après celui-ci :

- ❌ Ce n'est **pas** un cours de **shellcode**.
- ❌ Ce n'est **pas** un cours d'**exploitation** (buffer overflow, ROP, format string…).
- ❌ Ce n'est **pas** un cours de **malware analysis** avancée.
- ❌ Ce n'est **pas** un cours de programmation **noyau** ou de drivers.
- ❌ Ce n'est **pas** un cours d'**optimisation CPU** (pipeline, cache, SIMD/SSE/AVX).
- ❌ Ce n'est **pas** un cours d'assembleur **Windows** (on reste sur Linux).
- ❌ Ce n'est **pas** un cours de **C inline assembly**.

Ces sujets peuvent venir **après**, une fois que les fondamentaux de ce cours sont acquis.

### 🎯 L'objectif final, concrètement

Pour que tu saches exactement où tu vas, voici ce que tu dois être capable de faire **à la fin de ce cours** :

- **Lire** un extrait d'assembleur simple et le comprendre.
- **Reconnaître** dans un désassemblage : une **condition** (`if`), une **boucle**, une **fonction**, un **appel à la libc** (`printf`, `strcmp`…).
- **Suivre les arguments** passés à une fonction dans GDB.
- **Résoudre un crackme débutant** (mot de passe en clair, comparaison caractère par caractère, transformation XOR simple).
- **Écrire** quelques petits programmes ASM, mais **ce n'est pas le but principal**. L'objectif réel est la **lecture** et la **reconnaissance de patterns**.

> Tu ne deviendras pas développeur assembleur professionnel avec ce cours, **et ce n'est pas le but**. Tu deviendras un **lecteur d'assembleur** compétent, ce qui est exactement ce dont tu as besoin pour le reverse, les CTF, le debug et la cybersécurité.

---

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **CPU** | Le "cerveau" de l'ordinateur. Il exécute les instructions une par une |
| **RAM** | La mémoire vive, où sont stockées les données et le code pendant l'exécution |
| **Registre** | Une mini-case de stockage **dans** le CPU, ultra-rapide, qui contient une valeur (typiquement 64 bits) |
| **Instruction** | Un ordre élémentaire pour le CPU (`mov`, `add`, `jmp`…) |
| **Opcode** | La représentation **binaire** d'une instruction, telle que le CPU la voit |
| **Bit** | La plus petite unité d'information : 0 ou 1 |
| **Octet (byte)** | 8 bits, qui forment ensemble une valeur de 0 à 255 |
| **Binaire** | Système de numération à base 2 (0 et 1) |
| **Hexadécimal** | Système de numération à base 16 (0-9 puis A-F). Noté `0x...` |
| **Adresse mémoire** | Le numéro qui désigne une case précise dans la RAM |
| **Pointeur** | Une valeur qui contient une adresse mémoire |
| **Pile (stack)** | Une zone de mémoire spéciale où l'on empile et dépile des valeurs |
| **Syscall** | Une demande de service au noyau du système (afficher, lire, ouvrir un fichier…) |
| **Noyau (kernel)** | Le programme central de Linux qui gère le matériel et les processus |
| **Assembleur (langage)** | Le langage que tu vas apprendre |
| **Assembleur (logiciel)** | Le programme qui traduit ton code en code machine (NASM dans ce cours) |
| **NASM** | L'assembleur que nous utilisons (Netwide Assembler) |
| **Linker** | Le programme qui transforme un fichier objet en exécutable (`ld`, ou `gcc`) |
| **Exécutable** | Un fichier que le système peut lancer (en ELF sur Linux) |
| **ELF** | Le format des exécutables sous Linux (Executable and Linkable Format) |
| **GDB** | Le debugger : il permet de regarder un programme s'exécuter ligne par ligne |
| **Désassemblage** | L'opération inverse : prendre un binaire et retrouver de l'assembleur lisible |
| **Reverse engineering** | Comprendre un programme dont on n'a pas le code source |
| **ABI** | Les règles de communication entre fonctions (qui met quoi où) |
| **Fonction** | Un bloc de code réutilisable avec un nom, des arguments, un résultat |
| **Stack frame** | L'espace de travail d'une fonction sur la pile |
| **Flag (drapeau)** | Un mini-indicateur dans le CPU (0 ou 1) qui mémorise le résultat de la dernière opération |
| **Section** | Une zone du fichier `.asm` : code (`.text`), données (`.data`), réservées (`.bss`) |
| **Label (étiquette)** | Un nom que tu donnes à un endroit du code ou des données |
| **Syntaxe Intel** | La syntaxe utilisée dans ce cours : `mov destination, source` |
| **Syntaxe AT&T** | L'autre syntaxe (`mov source, destination`), qu'on apprendra **seulement à lire** plus tard |

---

### Comment penser un programme assembleur

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. En Bash ou Python, tu raisonnes en termes de :

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

En **assembleur**, le modèle mental change. Tu raisonnes en termes de **trois mondes** qui s'échangent des données :

```
  ┌─────────────┐    ┌─────────────┐    ┌──────────────────┐
  │  REGISTRES  │←──→│   MÉMOIRE   │←──→│ SYSCALLS/FONCTIONS│
  │    (CPU)    │    │    (RAM)    │    │     (SYSTÈME)     │
  └─────────────┘    └─────────────┘    └──────────────────┘
```

- Les **registres**, c'est ton bureau de travail (petit, rapide, mais limité).
- La **mémoire**, c'est ta bibliothèque (grande, plus lente, on y va chercher et on y range).
- Les **syscalls/fonctions**, c'est ton interface avec l'extérieur (afficher, lire, ouvrir un fichier).

Concrètement, **il n'y a que 10 briques de base** dans un programme assembleur :

1. **Charger** une valeur dans un registre.
2. **Déplacer** une valeur entre registres et mémoire.
3. **Calculer** dans les registres (addition, soustraction, multiplication…).
4. **Comparer** deux valeurs.
5. **Sauter** vers une autre partie du programme (selon le résultat d'une comparaison ou pas).
6. **Lire/écrire** via le système (afficher, lire au clavier, ouvrir un fichier).
7. **Empiler/dépiler** des valeurs sur la pile.
8. **Appeler/retourner** d'une fonction.
9. **Observer** ce qui se passe avec GDB.
10. **Lire** du code désassemblé pour comprendre un binaire.

Tous les programmes assembleur, même les plus complexes, sont une combinaison de ces 10 briques. Garde ça en tête à chaque chapitre.

---

### La grande différence avec Bash et Python

Si tu viens des cours Bash et Python de cette collection, **trois différences fondamentales** sont à comprendre :

#### 1. Pas de variables typées

En Python, tu as `int`, `str`, `list`… En assembleur, **tout est des octets**. Que ce soit un nombre, une lettre ou une adresse, ce sont des octets. C'est toi qui décides comment les interpréter.

#### 2. Pas d'affichage automatique

En Python, `print(x)` affiche `x`. En assembleur, il n'y a **rien** d'automatique. Pour afficher, il faut **demander au système** via un syscall. C'est pour ça qu'on apprend très vite GDB : pour **voir** les valeurs sans devoir les afficher.

#### 3. Une seule micro-action par ligne

En Python, `c = a + b` fait deux choses en une ligne (calculer et stocker). En assembleur, il faut **deux instructions** : `mov rax, [a]` puis `add rax, [b]`. C'est plus verbeux, mais c'est aussi pour ça qu'on comprend exactement ce que le CPU fait.

> **À retenir :** l'assembleur n'est pas plus dur, il est plus **explicite et plus détaillé**. Ce que Python te cachait, l'assembleur te le montre. C'est précisément ce qui en fait un outil précieux pour la cybersécurité et le reverse.

---

### Méthode de travail recommandée

L'assembleur ne s'apprend pas en lisant — il s'apprend en **tapant** et en **observant**. Pour chaque programme du cours, applique systématiquement ce rituel en 6 étapes :

1. **Lire** le code et essayer de comprendre.
2. **Prédire** sur papier la valeur de chaque registre après chaque instruction.
3. **Recopier** à la main (pas copier-coller — ton cerveau retient mieux).
4. **Exécuter** normalement (vérifier `echo $?` ou la sortie).
5. **Exécuter dans GDB** (à partir du chapitre 9) et comparer avec ta prédiction.
6. **Modifier** une valeur, et **refaire l'observation**. Comprendre ce qui change.

> **Conseil important :** si un chapitre te paraît flou, **continue quand même**. Plusieurs notions ne s'éclairent qu'à la lumière du chapitre suivant. Reviens en arrière une fois que tu as vu la suite.

### Trois niveaux de maîtrise

Pour rester réaliste sur tes objectifs : il y a **trois niveaux** d'apprentissage de l'assembleur. Tu n'as pas besoin de tous les atteindre à 100 %.

| Niveau | Objectif | Importance pour ce cours |
|--------|----------|--------------------------|
| **Écrire** | Savoir produire un petit programme assembleur à la main | ⭐⭐ Important au début |
| **Lire** | Comprendre un extrait ASM qu'on te donne | ⭐⭐⭐ Cœur du cours |
| **Reconnaître** | Identifier un pattern (boucle, `if`, appel…) dans un binaire | ⭐⭐⭐ Objectif final |

> **L'objectif réaliste pour la cybersécurité : viser surtout "lire" et "reconnaître".** Très peu de gens écrivent de l'assembleur entier de nos jours. **Tout le monde**, en revanche, doit savoir le lire pour faire du reverse, du debug, du CTF.

### Sur la montée en difficulté

Le cours commence très doux (chapitres 1-9), puis devient progressivement plus dense. **À partir de la partie V** (entrées/sorties, conversions, fichiers), le cours reste accessible mais demande **plus de pratique**. Il est normal de devoir :

- Refaire un exemple plusieurs fois.
- Relire un chapitre à tête reposée.
- Bloquer sur la pile, les fonctions, ou le reverse — c'est **normal**.

Ne te juge pas. La patience compte plus que la vitesse.

---

### Table des matières

**PARTIE 0 — PRÉAMBULE** *(tu es ici)*

**PARTIE I — COMPRENDRE LA MACHINE**

1. [Qu'est-ce que l'assembleur et pourquoi l'apprendre ?](01-partie-i-comprendre-la-machine.md#chapitre-1-quest-ce-que-lassembleur-et-pourquoi-lapprendre)
2. [CPU, RAM, registres : le modèle mental minimum](01-partie-i-comprendre-la-machine.md#chapitre-2-cpu-ram-registres-le-modele-mental-minimum)
3. [Binaire, hexadécimal, ASCII et tailles de données](01-partie-i-comprendre-la-machine.md#chapitre-3-binaire-hexadecimal-ascii-et-tailles-de-donnees)

**PARTIE II — INSTALLER, ÉCRIRE, EXÉCUTER**

4. [Environnement de travail et premier programme](02-partie-ii-installer-ecrire-executer.md#chapitre-4-environnement-de-travail-et-premier-programme)
5. [Anatomie d'un fichier .asm](02-partie-ii-installer-ecrire-executer.md#chapitre-5-anatomie-dun-fichier-asm)
6. [Premier affichage avec `write`](02-partie-ii-installer-ecrire-executer.md#chapitre-6-premier-affichage-avec-write)

**PARTIE III — REGISTRES, CALCULS ET OBSERVATION**

7. [Déplacer des données avec `mov`](03-partie-iii-registres-calculs-et-observation.md#chapitre-7-deplacer-des-donnees-avec-mov)
8. [Calculer avec les registres](03-partie-iii-registres-calculs-et-observation.md#chapitre-8-calculer-avec-les-registres)
9. [GDB pour observer les registres](03-partie-iii-registres-calculs-et-observation.md#chapitre-9-gdb-pour-observer-les-registres)

**PARTIE IV — MÉMOIRE, ADRESSES ET CHAÎNES**

10. [Mémoire, adresses et variables](04-partie-iv-memoire-adresses-et-chaines.md#chapitre-10-memoire-adresses-et-variables)
11. [Chaînes de caractères et octets](04-partie-iv-memoire-adresses-et-chaines.md#chapitre-11-chaines-de-caracteres-et-octets)
12. [`lea` et modes d'adressage](04-partie-iv-memoire-adresses-et-chaines.md#chapitre-12-lea-et-modes-dadressage)

**PARTIE V — ENTRÉES, SORTIES ET CONVERSIONS**

13. [Lire au clavier avec `read`](05-partie-v-entrees-sorties-et-conversions.md#chapitre-13-lire-au-clavier-avec-read)
14. [Convertir texte et nombres](05-partie-v-entrees-sorties-et-conversions.md#chapitre-14-convertir-texte-et-nombres)
15. [Fichiers et syscalls utiles](05-partie-v-entrees-sorties-et-conversions.md#chapitre-15-fichiers-et-syscalls-utiles)

**PARTIE VI — LOGIQUE ET CONTRÔLE DE FLUX**

16. [Comparaisons, flags et sauts](06-partie-vi-logique-et-controle-de-flux.md#chapitre-16-comparaisons-flags-et-sauts)
17. [Boucles](06-partie-vi-logique-et-controle-de-flux.md#chapitre-17-boucles)

**PARTIE VII — PILE ET FONCTIONS**

18. [La pile avec `push`, `pop` et `rsp`](07-partie-vii-pile-et-fonctions.md#chapitre-18-la-pile-avec-push-pop-et-rsp)
19. [Fonctions avec `call` et `ret`](07-partie-vii-pile-et-fonctions.md#chapitre-19-fonctions-avec-call-et-ret)
20. [Stack frame, `rbp` et variables locales](07-partie-vii-pile-et-fonctions.md#chapitre-20-stack-frame-rbp-et-variables-locales)

**PARTIE VIII — LIEN AVEC C ET LIBC**

21. [Appeler la libc depuis l'assembleur](08-partie-viii-lien-avec-c-et-libc.md#chapitre-21-appeler-la-libc-depuis-lassembleur)
22. [Du C vers l'assembleur](08-partie-viii-lien-avec-c-et-libc.md#chapitre-22-du-c-vers-lassembleur)

**PARTIE IX — LECTURE DE BINAIRES ET REVERSE DÉBUTANT**

23. [Désassembler un binaire ELF](09-partie-ix-lecture-de-binaires-et-reverse-debutant.md#chapitre-23-desassembler-un-binaire-elf)
24. [Reverse engineering débutant avec GDB](09-partie-ix-lecture-de-binaires-et-reverse-debutant.md#chapitre-24-reverse-engineering-debutant-avec-gdb)

**PARTIE X — SYNTHÈSE**

25. [Récapitulatif complet du débutant](10-partie-x-synthese-et-boite-a-outils.md#chapitre-25-recapitulatif-complet-du-debutant)

**ANNEXES**

- A. [Syntaxe AT&T pour la lecture](10-partie-x-synthese-et-boite-a-outils.md#annexe-a-syntaxe-att-pour-la-lecture)
- B. [x86 32 bits vs x86-64](10-partie-x-synthese-et-boite-a-outils.md#annexe-b-x86-32-bits-vs-x86-64)
- C. [Linux System V ABI vs Windows x64 ABI](10-partie-x-synthese-et-boite-a-outils.md#annexe-c-linux-system-v-abi-vs-windows-x64-abi)
- D. [Nombres signés, complément à deux et débordements](10-partie-x-synthese-et-boite-a-outils.md#annexe-d-nombres-signes-complement-a-deux-et-debordements)
- E. [Little-endian](10-partie-x-synthese-et-boite-a-outils.md#annexe-e-little-endian)
- F. [Makefile et commandes utiles](10-partie-x-synthese-et-boite-a-outils.md#annexe-f-makefile-et-commandes-utiles)
- G. [Glossaire assembleur / reverse](10-partie-x-synthese-et-boite-a-outils.md#annexe-g-glossaire-assembleur-reverse)
- H. [Panorama des outils de reverse](10-partie-x-synthese-et-boite-a-outils.md#annexe-h-panorama-des-outils-de-reverse)
- I. [Suite logique après ce cours](10-partie-x-synthese-et-boite-a-outils.md#annexe-i-suite-logique-apres-ce-cours)

---

## Sommaire

1. [PARTIE I — COMPRENDRE LA MACHINE](01-partie-i-comprendre-la-machine.md)
2. [PARTIE II — INSTALLER, ÉCRIRE, EXÉCUTER](02-partie-ii-installer-ecrire-executer.md)
3. [PARTIE III — REGISTRES, CALCULS ET OBSERVATION](03-partie-iii-registres-calculs-et-observation.md)
4. [PARTIE IV — MÉMOIRE, ADRESSES ET CHAÎNES](04-partie-iv-memoire-adresses-et-chaines.md)
5. [PARTIE V — ENTRÉES, SORTIES ET CONVERSIONS](05-partie-v-entrees-sorties-et-conversions.md)
6. [PARTIE VI — LOGIQUE ET CONTRÔLE DE FLUX](06-partie-vi-logique-et-controle-de-flux.md)
7. [PARTIE VII — PILE ET FONCTIONS](07-partie-vii-pile-et-fonctions.md)
8. [PARTIE VIII — LIEN AVEC C ET LIBC](08-partie-viii-lien-avec-c-et-libc.md)
9. [PARTIE IX — LECTURE DE BINAIRES ET REVERSE DÉBUTANT](09-partie-ix-lecture-de-binaires-et-reverse-debutant.md)
10. [PARTIE X — SYNTHÈSE ET BOÎTE À OUTILS](10-partie-x-synthese-et-boite-a-outils.md)
