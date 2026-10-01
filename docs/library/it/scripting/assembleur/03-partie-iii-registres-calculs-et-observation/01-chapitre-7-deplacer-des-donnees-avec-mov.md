---
title: Chapitre 7 — Déplacer des données avec mov
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie III — Registres, calculs et observation
  - index.md
---

## Le minimum à savoir

### L'instruction la plus importante de l'assembleur

`mov` est l'instruction que tu vas écrire **le plus souvent**. Elle sert à **copier** une valeur d'un endroit à un autre.

> **Attention au nom !** `mov` vient de "move", mais en réalité, **c'est une copie, pas un déplacement**. La source garde sa valeur. C'est trompeur, mais c'est comme ça historiquement.

### Les 4 formes de `mov`

| Forme | Exemple | Ce que ça fait |
|-------|---------|----------------|
| immédiate → registre | `mov rax, 42` | `rax = 42` |
| registre → registre | `mov rax, rbx` | `rax = rbx` (rbx inchangé) |
| mémoire → registre | `mov rax, [var]` | `rax = contenu à l'adresse var` |
| registre → mémoire | `mov [var], rax` | `var en mémoire = rax` |

### La règle qui te suivra partout : pas de mémoire → mémoire (avec `mov`)

**Tu ne peux PAS faire :**

```nasm
mov [a], [b]     ; ❌ INTERDIT
```


Cette instruction n'existe pas en x86-64. Il **faut toujours passer par un registre** :

```nasm
mov rax, [b]     ; charger b dans rax
mov [a], rax     ; ranger rax dans a
```


> **Règle pédagogique :** pour les instructions courantes (`mov`, `add`, `cmp`, `sub`, …), tu **ne peux pas** manipuler **deux opérandes mémoire explicites** en même temps.
>
> **Nuance :** il existe des instructions spécialisées de **copie mémoire-à-mémoire** comme `movsb`, `movsq`, `rep movsb` qui passent par des registres **implicites** (`rsi`, `rdi`, `rcx`). Tu les croiseras en reverse (souvent dans `memcpy` ou `strcpy` optimisés), mais on ne les utilisera pas dans ce cours.

### Choisir la bonne taille

`mov` ne sait pas tout seul si tu veux copier 1, 2, 4 ou 8 octets. Tu lui dis avec la **taille du registre** :

```nasm
mov rax, 5       ; 8 octets (qword)
mov eax, 5       ; 4 octets (dword)
mov ax,  5       ; 2 octets (word)
mov al,  5       ; 1 octet  (byte)
```


Pour la mémoire sans registre, tu dois préciser :

```nasm
mov byte  [var], 5     ; 1 octet
mov word  [var], 5     ; 2 octets
mov dword [var], 5     ; 4 octets
mov qword [var], 5     ; 8 octets
```


Sinon NASM se plaint : *"operation size not specified"*.

### `mov rax, var` vs `mov rax, [var]`

C'est **la** confusion classique du débutant. Lis attentivement :

```nasm
section .data
    var dq 42

section .text
    mov rax, var      ; rax = ADRESSE de var (un nombre genre 0x404000)
    mov rax, [var]    ; rax = CONTENU à cette adresse  → rax = 42
```


Les crochets `[…]` veulent dire **"le contenu à l'adresse"**. Sans crochets, on a juste l'**adresse**.

## Très utile en pratique

### Exemple détaillé avec plusieurs mov

```nasm
; mov_demo.asm — Démonstration des différentes formes de mov

section .data
    valeur dq 100

section .text
global _start

_start:
    mov rax, 42         ; rax = 42  (immédiate)
    mov rbx, rax        ; rbx = 42  (registre → registre)
    mov rcx, [valeur]   ; rcx = 100 (mémoire → registre)
    mov [valeur], rax   ; valeur en mémoire = 42 (registre → mémoire)
    mov rdx, valeur     ; rdx = adresse de valeur (un grand nombre)

    ; quitter
    mov rax, 60
    mov rdi, 0
    syscall
```


Tu ne **vois rien** quand tu exécutes ce programme. **C'est normal.** Au chapitre 9, on l'observera dans GDB pour voir tous les registres bouger.

### Les sous-registres en pratique

Reprends l'exemple du chapitre 2 :

```nasm
mov rax, 0                  ; rax = 0
mov al, 0xFF                ; al = 0xFF, donc rax = 0x00000000000000FF
```


Mais **attention** à un comportement piège en x86-64 :

```nasm
mov rax, 0x1234567890ABCDEF
mov eax, 5                  ; rax = 0x0000000000000005 (la partie haute est ZÉRO !)
```


> **Règle x86-64 :** écrire dans la version **32 bits** (`eax`, `ebx`, etc.) **efface automatiquement les 32 bits supérieurs**. Écrire dans les versions 8 et 16 bits, par contre, n'efface rien. C'est un piège.

## Bonus

### Réponse au défi du chapitre 2

Si `rax` valait `0x1234567890ABCDEF` et qu'on fait `mov al, 0xFF`, alors `rax` devient `0x1234567890ABCDFF`. Seuls les 8 bits bas changent.

### `mov` ne change jamais les flags

À l'inverse de `add` ou `sub`, l'instruction `mov` **ne modifie pas les flags du CPU**. On peut donc enchaîner plusieurs `mov` sans perdre l'état d'une comparaison faite avant. On reverra ça au chapitre 16.

## ❌ Erreur classique

```
Croire que mov "déplace" la source
→ Faux. mov COPIE. La source garde sa valeur.

Faire mov [a], [b]
→ Interdit en x86-64. Passe par un registre.

Oublier les crochets : mov rax, var au lieu de mov rax, [var]
→ Tu charges l'ADRESSE au lieu du CONTENU.

Ne pas spécifier la taille pour la mémoire
→ NASM crie : "operation size not specified".

Mélanger les tailles : mov rax, eax
→ Inconsistant. NASM crie : "mismatch in operand sizes".

Oublier que mov eax, 0 efface aussi les 32 bits hauts de rax
→ Piège classique. mov al, 0 ne fait pas pareil.
```


## Exercices

**Guidé :** Recopie et compile cet exemple. Tu n'auras pas de sortie visible (normal) :

```nasm
section .data
    a dq 10
    b dq 20

section .text
global _start
_start:
    mov rax, [a]
    mov rbx, [b]
    mov rcx, rax
    mov rdx, rbx
    mov rax, 60
    mov rdi, 0
    syscall
```


**Autonome :** Sans exécuter, **prédis sur papier** la valeur de `rax`, `rbx`, `rcx` après chaque ligne :

```nasm
mov rax, 100
mov rbx, 200
mov rcx, rax
mov rax, rbx
mov rbx, rcx
```


> **Question :** qu'est-ce que ce code vient de faire ? (Réponse en bas.)

**Défi :** Réécris ces lignes en assembleur :

- Python : `x = 5`, `y = 10`, `z = x`
- Suppose que `x`, `y`, `z` sont déclarés en `.data` avec `dq 0`.

> **Réponse autonome :** ce code **échange `rax` et `rbx`** (swap). C'est un pattern classique.

## ✅ Tu sais maintenant…

- Les **4 formes de `mov`** (immédiate, registre, mémoire, ou inverse)
- La règle d'or : **pas de mémoire → mémoire directe**
- La différence cruciale **`var`** (adresse) vs **`[var]`** (contenu)
- Comment **choisir la taille** (`rax`, `eax`, `al`, ou `byte/word/dword/qword`)
- Le **piège du 32 bits** qui efface les bits hauts
- Faire un **swap** entre deux registres

---
