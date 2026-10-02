---
title: Chapitre 10 — Mémoire, adresses et variables
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie IV — Mémoire, adresses et chaînes
  - index.md
---

## Le minimum à savoir

### Une "variable" en assembleur, c'est quoi ?

En Python, `x = 5` crée une **variable**. En assembleur, le concept est plus terre-à-terre :

> **Une variable assembleur, c'est juste un nom (label) qu'on donne à une adresse mémoire.** Rien de plus.

Quand tu écris :

```nasm
section .data
    x dq 5
```


NASM réserve **8 octets** quelque part en mémoire, y met la valeur `5`, et garde en tête que cet endroit s'appelle `x`. Plus tard, quand tu écris `mov rax, [x]`, NASM remplace `x` par cette adresse.

### Adresse vs contenu : LA confusion à comprendre

C'est la confusion **n°1** du débutant. Lis ça **plusieurs fois** :

```nasm
section .data
    x dq 42

section .text
    mov rax, x       ; rax = ADRESSE de x (par exemple 0x402000)
    mov rax, [x]     ; rax = CONTENU à l'adresse de x → rax = 42
```


| Forme | Signification |
|-------|---------------|
| **`x`** sans crochets | "L'adresse à laquelle vit la variable" |
| **`[x]`** avec crochets | "Le contenu stocké à cette adresse" |

> **Analogie postale :** `x` est l'**adresse** d'une maison (123 rue de la Paix). `[x]` est **ce qu'il y a dans la maison** (les habitants).

### Lire et écrire en mémoire

```nasm
section .data
    nombre dq 100

section .text
    mov rax, [nombre]    ; lire :   rax = 100
    add rax, 50          ; rax = 150
    mov [nombre], rax    ; écrire : la mémoire à l'adresse "nombre" = 150
```


À la fin, `nombre` en mémoire contient `150`. Tu peux le vérifier dans GDB avec `x/gd &nombre`.

### La règle d'or rappelée : pas de mémoire-à-mémoire

```nasm
section .data
    a dq 5
    b dq 10

section .text
    mov [a], [b]     ; ❌ INTERDIT
```


Comme au chapitre 7, tu **dois** passer par un registre :

```nasm
    mov rax, [b]     ; charger
    mov [a], rax     ; ranger
```


### Choisir la taille en mémoire

Tu peux lire ou écrire 1, 2, 4 ou 8 octets selon ce que tu veux :

```nasm
section .data
    valeur dq 0x123456789ABCDEF0    ; 8 octets

section .text
    mov al,  [valeur]     ; lit 1 octet  → 0xF0
    mov ax,  [valeur]     ; lit 2 octets → 0xDEF0
    mov eax, [valeur]     ; lit 4 octets → 0x9ABCDEF0
    mov rax, [valeur]     ; lit 8 octets → 0x123456789ABCDEF0
```


> **Pourquoi `al` lit-il `0xF0` et pas `0x12` ?** À cause du **little-endian** (Annexe E) : les octets de poids faible sont stockés en premier. Pour `0x123456789ABCDEF0`, le premier octet en mémoire est `0xF0`.

### Réserver un buffer dans `.bss`

Quand on veut juste **de la place vide** (par exemple pour stocker une saisie utilisateur), on utilise `.bss` :

```nasm
section .bss
    buffer  resb 64       ; 64 octets vides
    nb_lus  resq 1        ; 1 qword (8 octets) vide
```


C'est exactement comme `.data`, sauf qu'on **ne met pas de valeur initiale**.

### Tableaux simples

Un tableau en assembleur, c'est juste **plusieurs valeurs côte à côte** :

```nasm
section .data
    notes dq 10, 14, 18, 7, 12      ; 5 qword consécutifs
```


Pour accéder à un élément, on utilise l'**adresse + un décalage**, **en octets** :

```nasm
    mov rax, [notes]         ; 1er élément (index 0)  → 10
    mov rax, [notes + 8]     ; 2ème élément (index 1) → 14
    mov rax, [notes + 16]    ; 3ème élément (index 2) → 18
```


> **Attention :** le décalage est en **octets**, pas en éléments. Pour un tableau de `qword` (8 octets), c'est `+0`, `+8`, `+16`, `+24`, `+32`. Pour un tableau d'octets (`db`), ce serait `+0`, `+1`, `+2`…

### Indexation avec un registre

Pour parcourir un tableau (au chapitre 17), on utilisera l'**indexation par registre** :

```nasm
    mov rcx, 0                       ; index
    mov rax, [notes + rcx*8]         ; notes[0]
    mov rcx, 2                       ; index = 2
    mov rax, [notes + rcx*8]         ; notes[2] = 18
```


La syntaxe `[base + index * échelle]` est un **mode d'adressage** qu'on creuse au chapitre 12.

## Très utile en pratique

### Exemple complet

```nasm
; memoire.asm — Manipulation de variables en mémoire

section .data
    x dq 10
    y dq 7
    resultat dq 0

section .text
global _start
_start:
    mov rax, [x]            ; rax = 10
    add rax, [y]            ; rax = 10 + 7 = 17
    mov [resultat], rax     ; resultat en mémoire = 17

    ; Sortir avec resultat en code de retour
    mov rdi, [resultat]
    mov rax, 60
    syscall
```


Exécute, puis :

```bash
./memoire ; echo $?     # → 17
```


Vérifie dans GDB avec `x/gd &resultat` que la mémoire a bien été modifiée.

### Récapitulatif des opérandes mémoire

| Syntaxe | Effet |
|---------|-------|
| `mov rax, x` | `rax = adresse de x` |
| `mov rax, [x]` | `rax = contenu à l'adresse x` |
| `mov [x], rax` | Écrit `rax` à l'adresse `x` |
| `mov rax, [x + 8]` | Lit 8 octets après `x` |
| `mov rax, [x + rcx*8]` | Adressage indexé |
| `mov byte [x], 5` | Écrit l'octet `5` (précise la taille) |

## Bonus

### Little-endian en pratique

Si tu fais :

```nasm
section .data
    n dq 0x1234567890ABCDEF
```


Et que tu regardes la mémoire dans GDB avec `x/8bx &n`, tu verras :

```
0x404000:  0xef  0xcd  0xab  0x90  0x78  0x56  0x34  0x12
```


Les octets sont **dans l'ordre inverse de l'écriture**. C'est du little-endian. Le CPU s'y retrouve automatiquement quand tu fais `mov rax, [n]` : tu récupères bien `0x1234567890ABCDEF`.

> **À retenir :** lorsque tu vois un dump mémoire, **les octets sont à l'envers** par rapport à comment tu écris la valeur. Détails complets dans l'**Annexe E**.

## ❌ Erreur classique

```
Oublier les crochets : mov rax, x au lieu de mov rax, [x]
→ Tu charges l'adresse au lieu de la valeur. Confusion n°1.

Lire avec la mauvaise taille : mov al, [x] quand x est un qword
→ Tu n'auras que les 8 bits bas. Souvent un bug silencieux.

Indexer en éléments au lieu d'octets : [notes + 1] pour le 2ème élément
→ Ça lit 1 octet plus loin, pas 8. Pour un dq, c'est [notes + 8].

Écrire dans la section .text
→ Crash. .text est en lecture seule.

Lire dans .bss sans avoir mis quelque chose dedans
→ Tu lis des octets nuls (0). Pas grave, mais à savoir.

Confondre label et valeur : mov rdi, msg vs mov rdi, [msg]
→ Pour write(rsi = msg), on veut l'adresse. Pour exit(rdi = code),
  on veut la valeur. Distinguer selon le syscall.
```


## Exercices

**Guidé :** Crée un programme qui déclare `x dq 5` et `y dq 7`, calcule `x + y`, met le résultat dans `resultat dq 0`, puis sort avec ce résultat comme code de retour. Vérifie au GDB que `resultat` en mémoire vaut bien `12` après exécution.

**Autonome :** Déclare un tableau `nombres dq 10, 20, 30, 40, 50`. Charge le 3ème élément (valeur 30) dans `rax`. Multiplie-le par 2. Range-le dans le 5ème élément. Vérifie dans GDB que la mémoire a changé.

**Défi :** En partant de `valeur dq 0x12345678`, fais en sorte que `rax` ne contienne que les **2 octets du milieu** (`0x3456`). **Indice :** lecture en `word`, avec un décalage de 2 octets.

## 🧩 Mini-projet (chapitres 7-10) — Moyenne de notes

Crée `moyenne.asm` qui :

1. Déclare un tableau `notes dq 12, 14, 18, 16, 10` (5 notes).
2. Additionne les 5 notes dans `rax` (en lisant `[notes]`, `[notes + 8]`, etc. — sans boucle, on n'en a pas vu).
3. Divise par 5 (`idiv` avec `rdx = 0`).
4. Sort avec la moyenne comme code de retour.

Résultat attendu : `(12+14+18+16+10) / 5 = 70 / 5 = 14`. Donc `echo $?` doit afficher **14**.

## ✅ Tu sais maintenant…

- Qu'une **variable assembleur = un label sur une adresse**
- La différence cruciale **`x`** (adresse) vs **`[x]`** (contenu)
- Lire et écrire en mémoire avec **`mov`**
- Choisir la **taille** (`al`, `ax`, `eax`, `rax`)
- Réserver un **buffer** dans `.bss`
- Accéder à un **élément de tableau** avec un décalage en octets
- L'idée du **little-endian** (les octets stockés "à l'envers")

---
