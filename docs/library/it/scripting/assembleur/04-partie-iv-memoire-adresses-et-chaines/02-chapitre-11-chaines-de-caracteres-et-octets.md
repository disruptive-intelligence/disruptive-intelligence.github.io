---
title: Chapitre 11 — Chaînes de caractères et octets
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie IV — Mémoire, adresses et chaînes
  - index.md
---

## Le minimum à savoir

### Une chaîne, c'est juste une suite d'octets

En Python, `"Bonjour"` est un objet `str` avec plein de méthodes magiques. En assembleur, **une chaîne, c'est juste des octets côte à côte en mémoire**. Rien de plus.

```nasm
section .data
    msg db "Bonjour", 10
```


En mémoire, on a ces octets :

```
   B    o    n    j    o    u    r    \n
  0x42 0x6F 0x6E 0x6A 0x6F 0x75 0x72 0x0A
```


8 octets. C'est tout. Aucune "magie".

### Pourquoi `db` ?

`db` = **define byte**. Comme une chaîne, c'est un **flux d'octets**, on l'écrit avec `db`. Le compilateur transforme automatiquement chaque caractère en son **code ASCII**.

```nasm
msg db "AB"          ; équivalent à : msg db 0x41, 0x42
```


### Le retour ligne et le zéro final

Deux octets spéciaux à connaître :

- **`10`** (ou `0x0A`) = **retour ligne** (`\n`). On le met à la fin d'un message pour que la ligne suivante apparaisse.
- **`0`** (ou `0x00`) = **caractère NUL**. C'est le marqueur de fin de chaîne en C (mais **pas** pour les syscalls Linux).

```nasm
msg1 db "Hello", 10              ; pour les syscalls (write, etc.)
msg2 db "Hello", 0               ; pour les fonctions C (printf, etc.)
msg3 db "Hello", 10, 0           ; les deux, par sécurité
```


### Deux styles de chaînes : Linux vs C

| Style | Comment ça marque la fin | Usage |
|-------|--------------------------|-------|
| **Style Linux** | Par sa **longueur** explicite (passée en argument) | Syscalls `write`, `read` |
| **Style C** | Par un **octet 0** à la fin | Fonctions `printf`, `strlen`, `strcmp` |

En clair : pour `write`, on donne la longueur. Pour `printf`, on met un `0` à la fin et `printf` s'arrête tout seul en le voyant.

### Calculer la longueur avec `equ $ - msg`

```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg          ; len = nombre d'octets de msg
```


`$` signifie "ici", l'**adresse actuelle**. Donc `$ - msg` = "la distance entre `msg` et maintenant" = la longueur en octets.

> **Astuce :** mets toujours `equ $ - label` **juste après** la chaîne. Si tu mets autre chose entre les deux, le calcul est faux.

### Modifier un caractère en mémoire

Comme `msg` est une suite d'octets, on peut en modifier un seul :

```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg

section .text
global _start
_start:
    ; Remplacer le 'B' par 'X'
    mov byte [msg], 'X'         ; 'X' = 0x58 = 88
    ; ou : mov byte [msg], 0x58

    ; Afficher
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```


Sortie :

```
Xonjour
```


> **Le piège :** `mov [msg], 'X'` sans préciser `byte` donne une erreur ("operation size not specified"). En mémoire seule, NASM ne devine pas la taille.

### Accéder à un caractère par son index

```nasm
mov al, [msg]           ; al = 'B' = 0x42  (1er caractère)
mov al, [msg + 1]       ; al = 'o' = 0x6F  (2ème caractère)
mov al, [msg + 3]       ; al = 'j'         (4ème caractère)
```


Pour un tableau de caractères, l'index est **directement** le décalage (puisque chaque caractère fait 1 octet).

### Afficher une portion seulement

`write` prend une longueur — donc tu peux n'afficher que **5 caractères** :

```nasm
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 5              ; n'afficher que 5 octets : "Bonjo"
syscall
```


### Compter les caractères jusqu'à un délimiteur

C'est l'équivalent de `strlen()`. Sans boucle, on ne peut pas encore le coder proprement (on le fera au chapitre 17). Mais l'idée est de **parcourir octet par octet jusqu'à tomber sur un `0`** (style C) ou un `10` (style retour ligne).

## Très utile en pratique

### Chaîne sur plusieurs lignes

```nasm
section .data
    menu db "1) Option A", 10
         db "2) Option B", 10
         db "3) Quitter",  10
    menu_len equ $ - menu
```


NASM concatène automatiquement les `db` successifs (puisque la mémoire est contiguë). Très pratique pour des menus.

### Construire une chaîne caractère par caractère

```nasm
section .bss
    buffer resb 32

section .text
    mov byte [buffer + 0], 'H'
    mov byte [buffer + 1], 'i'
    mov byte [buffer + 2], '!'
    mov byte [buffer + 3], 10
    ; afficher 4 octets de buffer
```


Plus tard, avec des boucles, on automatisera ça.

### Aperçu : pourquoi un `0` final pour la libc ?

Quand tu fais `printf("%s", msg)`, `printf` lit `msg` **caractère par caractère** jusqu'à rencontrer un octet `0`. Sans ce `0`, `printf` continuera à lire en mémoire **bien au-delà** de ta chaîne, affichant du garbage… jusqu'à crash. On en reparle au chapitre 21.

## Bonus

### Caractères spéciaux

| Caractère | Décimal | Hexa | Effet |
|-----------|---------|------|-------|
| `\n` (LF) | 10 | `0x0A` | Saut de ligne (Linux) |
| `\r` (CR) | 13 | `0x0D` | Retour chariot (Windows utilise `\r\n`) |
| `\t` (TAB) | 9 | `0x09` | Tabulation |
| `\0` (NUL) | 0 | `0x00` | Fin de chaîne C |
| `\\` | 92 | `0x5C` | Antislash |

En NASM, **dans les chaînes classiques entre guillemets `"..."`, `\n` n'est PAS interprété** comme un retour ligne. Tu dois écrire `10` explicitement :

```nasm
msg db "Hello\n"        ; ❌ Affichera littéralement "Hello\n", barre oblique comprise
msg db "Hello", 10      ; ✅ correct
```


> **Détail :** NASM accepte des **backquotes** (`\`...\``) qui, elles, interprètent les échappements comme `\n`, `\t`. Mais on ne les utilisera pas dans ce cours pour rester simple — préfère toujours `, 10` à la fin de la chaîne.

### Convertir une lettre majuscule/minuscule

Comme `'A' = 0x41` et `'a' = 0x61`, la différence est **0x20** = 32. Donc :

```nasm
; transformer 'A' en 'a'
mov al, 'A'              ; al = 0x41
add al, 0x20             ; al = 0x61 = 'a'

; transformer 'a' en 'A'
mov al, 'a'              ; al = 0x61
sub al, 0x20             ; al = 0x41 = 'A'
```


C'est précisément ce que fait `str.lower()` en Python, mais à la main, octet par octet.

## ❌ Erreur classique

```
Croire qu'une chaîne est un "type" comme en Python
→ Non, c'est juste une suite d'octets.

Écrire "Hello\n" en pensant que \n est interprété
→ NASM affichera "Hello\n" littéralement. Utilise "Hello", 10.

Oublier le 0 final pour printf
→ printf lira en dehors de la chaîne, comportement indéfini.

Confondre longueur et adresse
→ rdx = LONGUEUR (un nombre, genre 8). rsi = ADRESSE (un pointeur).

Mettre len = $ - msg mais APRÈS avoir mis d'autres données
→ Le calcul inclura ces autres données. Toujours juste après le msg.

Modifier byte [msg], 'X' sans préciser "byte"
→ Erreur NASM "operation size not specified".

Faire mov [msg], 'A' au lieu de mov byte [msg], 'A'
→ Pareil. Toujours préciser la taille pour la mémoire.
```


## Exercices

**Guidé :** Crée un programme `salut.asm` qui :

1. Déclare `msg db "Hello, World!", 10`.
2. Calcule `len equ $ - msg`.
3. Affiche le message via `write`.

**Autonome :** Modifie ton programme pour :

1. Remplacer le premier caractère par `'J'` avant d'afficher (→ "Jello, World!").
2. N'afficher que les **5 premiers caractères**.

**Défi :** Crée un programme qui affiche la lettre `'A'` seulement (1 octet, sans retour ligne). Puis modifie-le pour afficher la lettre `'A'` **puis** un retour ligne. Tu n'as droit qu'à 1 octet de buffer.

## 🧩 Mini-projet (chapitres 9-11) — Bannière dynamique

Crée `banniere2.asm` qui :

1. Déclare une chaîne `motif db "* * * BIENVENUE * * *", 10`.
2. Affiche la chaîne **trois fois** (3 syscalls write d'affilée).
3. **Bonus :** entre chaque affichage, modifie la première étoile en `'+'`.

> **Indice :** pour modifier, utilise `mov byte [motif], '+'`. Pour afficher, garde la même longueur.

## ✅ Tu sais maintenant…

- Qu'une **chaîne = suite d'octets** en mémoire
- Le rôle de **`db`** pour déclarer des octets
- La différence entre **style Linux (longueur)** et **style C (`0` final)**
- Les codes ASCII utiles : `10` pour `\n`, `0` pour la fin C
- Modifier un **caractère en mémoire** avec `mov byte [...]`
- Accéder à un caractère **par son index** (`[msg + N]`)
- Pourquoi NASM **n'interprète pas `\n`** dans une chaîne

---
