---
title: Chapitre 5 — Anatomie d'un fichier .asm
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie II — Installer, écrire, exécuter
  - index.md
---

## Le minimum à savoir

### La structure d'un fichier NASM

Un fichier `.asm` est divisé en **sections**. Chaque section a un rôle précis :

```nasm
section .data       ; ← données initialisées (variables avec une valeur)
    ; ...

section .bss        ; ← données réservées non initialisées
    ; ...

section .text       ; ← le code exécutable
global _start
_start:
    ; ...
```


| Section | Rôle | Analogie |
|---------|------|----------|
| **`.text`** | Le code exécutable (les instructions) | Les **recettes** de cuisine |
| **`.data`** | Données initialisées (variables avec une valeur) | Les **ingrédients** déjà préparés |
| **`.bss`** | Espace réservé non initialisé (buffers vides) | Les **bols vides** pour plus tard |
| **`.rodata`** | Données en **lecture seule** (constantes) — optionnel | Les **étiquettes** sur les pots |

> **À retenir :** `.text` est obligatoire (sinon il n'y a pas de code). `.data` et `.bss` sont optionnels.

### Les labels (étiquettes)

Un **label** est un nom que tu donnes à un endroit du fichier (un emplacement de code OU une variable). Tu utilises ensuite ce nom au lieu d'une adresse.

```nasm
section .data
    age db 25              ; "age" est un label pointant vers un octet de valeur 25
    nom db "Alice", 0      ; "nom" est un label pointant vers la chaîne "Alice\0"

section .text
global _start
_start:                    ; "_start" est un label pointant vers le début du code
    mov al, [age]          ; on utilise le label "age"
    ; ...
boucle:                    ; un label dans le code pour les sauts
    ; ...
```


> **Règle :** un label se termine par `:` quand on le **définit**. Quand on l'**utilise**, pas de `:`.

### Les directives de données

Dans la section `.data`, on déclare des variables avec des **directives** :

| Directive | Taille | Usage |
|-----------|--------|-------|
| **`db`** | **b**yte (1 octet) | `nom db "Alice", 0` |
| **`dw`** | **w**ord (2 octets) | `pixel dw 0x1234` |
| **`dd`** | **d**ouble word (4 octets) | `version dd 12` |
| **`dq`** | **q**uad word (8 octets) | `gros dq 1234567890` |

Dans la section `.bss`, on **réserve** sans initialiser :

| Directive | Taille | Usage |
|-----------|--------|-------|
| **`resb N`** | N octets | `buffer resb 64` (réserve 64 octets) |
| **`resw N`** | N × 2 octets | `tab resw 10` |
| **`resd N`** | N × 4 octets | `tab resd 10` |
| **`resq N`** | N × 8 octets | `tab resq 10` |

Et pour les **constantes** (pas en mémoire, juste un nom pour une valeur fixe) :

```nasm
section .data
    msg db "Bonjour", 10
    LEN equ $ - msg        ; equ = "égal" : LEN devient une constante
```


> **`$` en NASM** = "l'adresse actuelle, ici, à cet endroit". Donc `$ - msg` = "la longueur entre `msg` et maintenant". Astuce pratique pour calculer une longueur de chaîne.

### La syntaxe Intel : destination à gauche, source à droite

NASM utilise la **syntaxe Intel**, qui est la plus lisible :

```nasm
mov rax, 5         ; rax = 5    (destination = source)
add rax, rbx       ; rax = rax + rbx
mov [var], rax     ; var en mémoire = rax
```


Le **premier opérande** est la **destination**, le **second** est la **source**. C'est comme `x = 5` en Python : ce qui reçoit est à gauche.

> **Note :** la syntaxe AT&T (utilisée par défaut dans GDB et `objdump`) inverse cet ordre. On la verra **en lecture uniquement** dans l'Annexe A. Pour ce cours, on reste à 100 % en Intel.

### Les commentaires

NASM utilise `;` pour les commentaires (comme Bash utilise `#`) :

```nasm
mov rax, 1     ; ceci est un commentaire de fin de ligne
; ceci est un commentaire pleine ligne
```


> **Conseil pédagogique :** commente **chaque ligne** au début. Ça force à expliquer ce que tu fais, et c'est la meilleure façon d'apprendre.

## Très utile en pratique

### Exemple complet annoté

Voici un fichier `.asm` minimal qui contient les trois sections et plusieurs déclarations :

```nasm
; structure.asm — Démonstration de la structure d'un fichier NASM

; ─────────── SECTION DATA : variables initialisées ───────────
section .data
    nb_petit    db  42                  ; 1 octet  : 42
    nb_moyen    dw  1000                ; 2 octets : 1000
    nb_grand    dd  100000              ; 4 octets : 100000
    nb_enorme   dq  1234567890123       ; 8 octets : très grand
    message     db  "Bonjour", 0        ; chaîne terminée par 0
    LEN_MSG     equ $ - message         ; longueur de "message" (constante)

; ─────────── SECTION BSS : variables non initialisées ───────────
section .bss
    buffer      resb 64                 ; 64 octets réservés (vides)
    tab_int     resq 10                 ; 10 qword (80 octets) réservés

; ─────────── SECTION TEXT : le code ───────────
section .text
global _start

_start:
    ; ... ici on mettra des instructions au prochain chapitre ...

    ; pour l'instant, on quitte proprement
    mov rax, 60     ; syscall exit
    mov rdi, 0      ; code de retour 0
    syscall
```


Compile et exécute :

```bash
nasm -f elf64 structure.asm -o structure.o
ld structure.o -o structure
./structure
echo $?           # → 0
```


### Récapitulatif visuel

```
   ┌─────────────────────────────────────────────────────────┐
   │                FICHIER .asm                             │
   ├─────────────────────────────────────────────────────────┤
   │                                                         │
   │   section .data    ← variables initialisées             │
   │     var1 db 5                                           │
   │     msg  db "Hi", 0                                     │
   │                                                         │
   │   section .bss     ← buffers vides                      │
   │     buf  resb 64                                        │
   │                                                         │
   │   section .text    ← code                               │
   │   global _start                                         │
   │   _start:                                               │
   │     ; instructions                                      │
   │                                                         │
   └─────────────────────────────────────────────────────────┘
```


## Bonus

### Le label `_start` et `main`

Sous Linux, le point d'entrée par défaut pour `ld` est `_start`. Quand on linke avec `gcc`, le point d'entrée devient `main` (parce que gcc fournit un `_start` qui appelle `main`). On reverra ça au chapitre 21.

### Pourquoi `.bss` plutôt que `.data` pour les buffers ?

Si tu déclares 1 Mo de buffer dans `.data`, **ton exécutable fera 1 Mo** (la valeur initiale est stockée dans le fichier). Si tu le déclares dans `.bss`, **le fichier reste minuscule** (le système réserve l'espace au lancement). Pour des buffers vides, toujours `.bss`.

## ❌ Erreur classique

```
Confondre db (data byte) et resb (reserve byte)
→ db : initialisé.    resb : réservé non initialisé.

Oublier les deux-points après un label
→ "_start" est traité comme une instruction → erreur.

Confondre une instruction et une directive
→ mov est une instruction (exécutée par le CPU).
→ db est une directive (gérée par NASM avant exécution).

Inverser destination et source
→ mov 5, rax  est faux. C'est mov rax, 5.

Mettre du code dans .data
→ NON. Le code va dans .text uniquement.

Oublier le 0 final d'une chaîne pour la libc
→ Pour les syscalls Linux, pas obligatoire (on donne la longueur).
→ Pour printf et autres fonctions C, OBLIGATOIRE.
```


## Exercices

**Guidé :** Crée `decla.asm` avec :

- une variable `age` de type byte initialisée à 25
- une variable `annee` de type dword initialisée à 2024
- une variable `nom` de type chaîne contenant "Bob" + un 0
- un buffer `buf` de 32 octets dans `.bss`
- un `_start` qui ne fait que quitter avec code 0

Compile-le et exécute-le. Ça doit afficher rien et `echo $?` doit donner `0`.

**Autonome :** Écris un fichier `.asm` qui contient :

- 5 constantes (avec `equ`) : `PI`, `E`, `MAX`, `MIN`, `ZERO` avec des valeurs au choix.
- 5 variables initialisées (utilisant `db`, `dw`, `dd`, `dq`).
- Un `_start` qui quitte avec le code de retour 7.

Vérifie que tout compile sans erreur.

**Défi :** Que vaut `LEN` ici, à ton avis (sans exécuter) ?

```nasm
section .data
    msg db "Hello!", 10, 0
    LEN equ $ - msg
```


> **Indice :** compte les octets. `"Hello!"` = 6 caractères + 1 retour ligne + 1 zéro = ?

## ✅ Tu sais maintenant…

- Les sections **`.text`**, **`.data`**, **`.bss`**
- Les directives de données **`db`, `dw`, `dd`, `dq`**
- Les directives de réservation **`resb`, `resw`, `resd`, `resq`**
- Les **constantes** avec `equ`
- Les **labels** et leur syntaxe (`:` à la définition)
- La **syntaxe Intel** : `instruction destination, source`
- Comment **commenter** avec `;`
- La règle `$ - label` pour calculer une longueur

---
