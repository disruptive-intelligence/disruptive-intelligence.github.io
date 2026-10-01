---
title: Chapitre 23 — Désassembler un binaire ELF
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie IX — Lecture de binaires et reverse débutant
  - index.md
---

## Le minimum à savoir

### Le grand changement

Jusqu'ici, tu **écrivais** du code et tu en **observais** l'exécution. À partir d'ici, on **inverse** : tu reçois un binaire **sans le code source**, et tu dois comprendre ce qu'il fait. C'est le **reverse engineering**.

> **Le reverse débutant, c'est lire du code.** Pas écraser, pas modifier, pas exploiter. Juste **comprendre**.

### Le format ELF

Sous Linux, **les exécutables binaires natifs sont généralement au format ELF** (Executable and Linkable Format) — les scripts (`#!/bin/bash`, `#!/usr/bin/env python3`, etc.) sont une autre histoire, gérée par le noyau via le shebang. C'est un format structuré, divisé en **sections** que tu connais déjà (`.text`, `.data`, …) et en **segments** (utilisés au chargement en mémoire).

### Les 5 outils essentiels

| Outil | Rôle |
|-------|------|
| **`file`** | Identifier le type d'un fichier |
| **`strings`** | Extraire les chaînes lisibles d'un binaire |
| **`readelf`** | Inspecter la structure ELF (entêtes, sections, symboles) |
| **`nm`** | Lister les **symboles** (noms de fonctions, variables) |
| **`objdump`** | **Désassembler** un binaire en assembleur |

Ils sont tous fournis par `binutils` (déjà installé au chapitre 4).

### `file` : qu'est-ce que c'est ?

```bash
$ file ./hello
hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, ...
```


Tu apprends :

- **ELF** : c'est bien un exécutable Linux.
- **64-bit, x86-64** : architecture.
- **dynamically linked** : il dépend de bibliothèques (libc, …). L'opposé serait **statically linked** (autonome).

### `strings` : les chaînes en clair

```bash
$ strings ./hello
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__libc_start_main
GLIBC_2.34
Bonjour le monde !
GCC: (Ubuntu 11.4.0) ...
```


Les **chaînes affichables** apparaissent. Si un mot de passe ou un message d'erreur est en clair, tu le verras ici. **Premier réflexe en CTF.**

### `readelf -h` : l'entête ELF

```bash
$ readelf -h ./hello
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 ...
  Class:                             ELF64
  Type:                              EXEC (Executable file)
  Entry point address:               0x401040
  ...
```


Important :

- **Entry point address** : adresse où le programme commence (le `_start`).
- **Class** : 64 bits (ELF64) ou 32 bits (ELF32).
- **Type** : EXEC, DYN, …

### `readelf -S` : les sections

```bash
$ readelf -S ./hello
There are 30 section headers, starting at offset 0x3938:

Section Headers:
  [Nr] Name              Type             Address           Size
  [ 1] .interp           PROGBITS         0x000000000040038c
  [ 2] .note.gnu.property NOTE             0x00000000004003a8
  ...
  [12] .text             PROGBITS         0x0000000000401040    ← le code !
  [16] .rodata           PROGBITS         0x0000000000402000    ← les chaînes
  [22] .data             PROGBITS         0x0000000000404010    ← données initialisées
  [23] .bss              NOBITS           0x0000000000404020    ← données vides
```


| Section | Contenu | Permissions |
|---------|---------|-------------|
| **`.text`** | Code exécutable | Lecture + exécution |
| **`.rodata`** | Données en lecture seule (constantes, chaînes littérales) | Lecture seule |
| **`.data`** | Variables globales initialisées | Lecture + écriture |
| **`.bss`** | Variables globales non initialisées | Lecture + écriture |
| **`.plt`** / **`.got`** | Tables pour les appels libc | Spécial |

### `nm` : lister les symboles

```bash
$ nm ./hello
                 U __libc_start_main@GLIBC_2.34    ← fonction externe
0000000000404020 B __bss_start
0000000000401040 T _start                          ← point d'entrée
0000000000402000 R msg                             ← variable globale
0000000000401140 T main                            ← fonction main
0000000000401130 T addition                        ← une autre fonction
```


Lettres : **T** = code (`.text`), **R** = lecture seule, **B** = `.bss`, **U** = undefined (importé).

### Binaire strippé : quand les symboles disparaissent

```bash
$ strip ./hello       # enlève tous les symboles internes
$ nm ./hello
nm: ./hello: no symbols
```


Un binaire **strippé** garde ses fonctions, mais **sans nom** dans `nm`. Tu verras juste des adresses (`sub_401130`) en désassemblage. C'est **le cas courant** des binaires en production. Plus dur à reverser.

### `objdump -d -M intel` : le désassemblage

```bash
$ objdump -d -M intel ./hello
```


L'option **`-M intel`** est **cruciale** : sans elle, c'est de l'AT&T (cryptique). Sortie (extrait) :

```
0000000000401140 <main>:
  401140:       55                  push   rbp
  401141:       48 89 e5            mov    rbp,rsp
  401144:       48 8d 3d b9 0e 00..  lea    rdi, [rip+0xeb9]    # 402004 <msg>
  40114b:       e8 e0 fe ff ff      call   401030 <puts@plt>
  401150:       b8 00 00 00 00      mov    eax, 0x0
  401155:       5d                  pop    rbp
  401156:       c3                  ret
```


Lis-le comme tu lis ton propre code :

- **Adresses** : `401140`, `401141`, …
- **Opcodes** (octets bruts) : `55`, `48 89 e5`, …
- **Mnémoniques** (instructions lisibles) : `push rbp`, `mov rbp, rsp`, …
- **Commentaires automatiques** : `# 402004 <msg>` (l'adresse pointée est nommée).

> **Tu reconnais tout ?** Le prologue (`push rbp ; mov rbp, rsp`), un `lea` pour charger l'adresse d'une chaîne, un `call puts@plt` (appel à puts via la PLT), l'épilogue (`pop rbp ; ret`). **Exactement** ce que tu as appris.

## Très utile en pratique

### Trouver `main` dans un binaire

Si `nm` montre `main`, super. Sinon (binaire strippé) :

1. Cherche le **point d'entrée** : `readelf -h` te donne l'adresse (c'est `_start`).
2. **Attention :** sous Linux avec la libc, `_start` n'appelle **pas** directement `main`. Il prépare les arguments puis appelle **`__libc_start_main`**, qui se charge d'appeler `main` ensuite.
3. L'adresse de `main` est généralement passée en **premier argument** à `__libc_start_main`, donc dans **`rdi`** (convention System V).
4. En désassemblage, cherche dans `_start` une instruction du type :
   ```
   mov  rdi, <adresse>        ; ← adresse de main
   ; ou
   lea  rdi, [rip + ...]
   ```
   juste avant `call __libc_start_main@plt`. Cette adresse, c'est `main`.

Exemple typique dans `_start` :

```
   ...
   lea  rdi, [rip + 0x101]    ← main ! (l'adresse calculée pointe sur main)
   ...
   call __libc_start_main@plt
```


### Filtrer le désassemblage à une fonction

```bash
objdump -d -M intel --disassemble=main ./hello
```


Cible une seule fonction. Indispensable quand le binaire est gros.

### Désassembler la section `.text` seule

```bash
objdump -d -M intel ./hello | less
```


Avec `| less`, tu peux scroller. Cherche `main` avec `/main` puis Entrée.

### Voir les chaînes contextualisées

```bash
objdump -s -j .rodata ./hello
```


Affiche le **contenu hex + ASCII** de la section `.rodata`. Tu vois exactement quelles constantes sont stockées et où.

## Bonus

### Pourquoi `puts@plt` et pas juste `puts` ?

`puts` est dans la **libc**, chargée dynamiquement. Le binaire ne contient pas le code de `puts` — juste un **stub** dans la section `.plt` qui sait où trouver `puts` à l'exécution. D'où le `@plt` (Procedure Linkage Table).

C'est un détail technique mais c'est le genre de chose qu'on rencontre **tout le temps** en reverse. Mémorise juste : `<fonction>@plt` = un appel à une fonction libc.

### `radare2` : pour les curieux

`radare2` (commande `r2`) est un outil de reverse engineering interactif plus puissant que `objdump`. Très utile pour les CTF. Hors scope de ce cours, mais à explorer ensuite.

### `ghidra` et `IDA` : les pros

Ces outils proposent du **désassemblage interactif avec décompilation** : ils te montrent l'ASM **et** une approximation du C correspondant. Magnifique mais gros à apprendre. Pour plus tard.

## ❌ Erreur classique

```
Oublier -M intel
→ Tu te retrouves avec mov %rax, %rbx (AT&T) au lieu de mov rbx, rax.
   Apprendre AT&T juste pour ça est inutile.

Chercher un main dans un binaire strippé sans le repérer via _start
→ Sans symboles, suis le call du _start.

Confondre l'adresse virtuelle (à l'exécution) et l'offset fichier
→ objdump affiche l'adresse virtuelle (0x401140), pas l'offset dans le .ELF.

Croire que tout le code est dans .text
→ Les fonctions C peuvent appeler la libc (via PLT). Les "_init", "_fini"
   font partie des sections initialisation.

Lire les opcodes au lieu des mnémoniques
→ Les opcodes (55, 48 89 e5) sont là pour info. Ce qui compte, c'est
   les mnémoniques (push rbp, mov rbp, rsp).
```


## Exercices

**Guidé :** Recompile l'un de tes propres programmes (par exemple `hello_c.asm` du ch. 21) et applique successivement :

- `file ./hello_c`
- `strings ./hello_c`
- `nm ./hello_c`
- `readelf -h ./hello_c`
- `objdump -d -M intel ./hello_c | less`

Identifie le `main`, le prologue, l'épilogue, le `call printf@plt`.

**Autonome :** Écris un petit `.c` avec une fonction `secret` qui contient une chaîne `"motdepasse123"` (juste en local : `char s[] = "motdepasse123";`). Compile. **Avant de lancer le programme**, retrouve la chaîne via `strings ./prog`.

**Défi :** Sur le même binaire, lance `strip ./prog`, puis refais `nm` et `objdump`. Que vois-tu en moins ? Peux-tu encore retrouver `main` ? (Indice : via le point d'entrée du ELF.)

## ✅ Tu sais maintenant…

- Ce qu'est un **binaire ELF** et ses **sections** (`.text`, `.rodata`, `.data`, `.bss`)
- Utiliser **`file`** pour identifier un binaire
- Utiliser **`strings`** pour extraire ses chaînes
- Utiliser **`readelf -h`** et **`-S`** pour son entête et ses sections
- Utiliser **`nm`** pour ses symboles
- **Désassembler** avec **`objdump -d -M intel`**
- La différence binaire **strippé / non strippé**
- Reconnaître **`fonction@plt`** pour les appels libc

---
