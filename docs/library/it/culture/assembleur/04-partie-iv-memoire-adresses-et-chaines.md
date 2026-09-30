---
title: PARTIE IV — MÉMOIRE, ADRESSES ET CHAÎNES
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 4
chapters: 10
---

---


## Chapitre 10 — Mémoire, adresses et variables

### Le minimum à savoir

#### Une "variable" en assembleur, c'est quoi ?

En Python, `x = 5` crée une **variable**. En assembleur, le concept est plus terre-à-terre :

> **Une variable assembleur, c'est juste un nom (label) qu'on donne à une adresse mémoire.** Rien de plus.

Quand tu écris :

```nasm
section .data
    x dq 5
```

NASM réserve **8 octets** quelque part en mémoire, y met la valeur `5`, et garde en tête que cet endroit s'appelle `x`. Plus tard, quand tu écris `mov rax, [x]`, NASM remplace `x` par cette adresse.

#### Adresse vs contenu : LA confusion à comprendre

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

#### Lire et écrire en mémoire

```nasm
section .data
    nombre dq 100

section .text
    mov rax, [nombre]    ; lire :   rax = 100
    add rax, 50          ; rax = 150
    mov [nombre], rax    ; écrire : la mémoire à l'adresse "nombre" = 150
```

À la fin, `nombre` en mémoire contient `150`. Tu peux le vérifier dans GDB avec `x/gd &nombre`.

#### La règle d'or rappelée : pas de mémoire-à-mémoire

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

#### Choisir la taille en mémoire

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

#### Réserver un buffer dans `.bss`

Quand on veut juste **de la place vide** (par exemple pour stocker une saisie utilisateur), on utilise `.bss` :

```nasm
section .bss
    buffer  resb 64       ; 64 octets vides
    nb_lus  resq 1        ; 1 qword (8 octets) vide
```

C'est exactement comme `.data`, sauf qu'on **ne met pas de valeur initiale**.

#### Tableaux simples

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

#### Indexation avec un registre

Pour parcourir un tableau (au chapitre 17), on utilisera l'**indexation par registre** :

```nasm
    mov rcx, 0                       ; index
    mov rax, [notes + rcx*8]         ; notes[0]
    mov rcx, 2                       ; index = 2
    mov rax, [notes + rcx*8]         ; notes[2] = 18
```

La syntaxe `[base + index * échelle]` est un **mode d'adressage** qu'on creuse au chapitre 12.

### Très utile en pratique

#### Exemple complet

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

#### Récapitulatif des opérandes mémoire

| Syntaxe | Effet |
|---------|-------|
| `mov rax, x` | `rax = adresse de x` |
| `mov rax, [x]` | `rax = contenu à l'adresse x` |
| `mov [x], rax` | Écrit `rax` à l'adresse `x` |
| `mov rax, [x + 8]` | Lit 8 octets après `x` |
| `mov rax, [x + rcx*8]` | Adressage indexé |
| `mov byte [x], 5` | Écrit l'octet `5` (précise la taille) |

### Bonus

#### Little-endian en pratique

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

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée un programme qui déclare `x dq 5` et `y dq 7`, calcule `x + y`, met le résultat dans `resultat dq 0`, puis sort avec ce résultat comme code de retour. Vérifie au GDB que `resultat` en mémoire vaut bien `12` après exécution.

**Autonome :** Déclare un tableau `nombres dq 10, 20, 30, 40, 50`. Charge le 3ème élément (valeur 30) dans `rax`. Multiplie-le par 2. Range-le dans le 5ème élément. Vérifie dans GDB que la mémoire a changé.

**Défi :** En partant de `valeur dq 0x12345678`, fais en sorte que `rax` ne contienne que les **2 octets du milieu** (`0x3456`). **Indice :** lecture en `word`, avec un décalage de 2 octets.

### 🧩 Mini-projet (chapitres 7-10) — Moyenne de notes

Crée `moyenne.asm` qui :

1. Déclare un tableau `notes dq 12, 14, 18, 16, 10` (5 notes).
2. Additionne les 5 notes dans `rax` (en lisant `[notes]`, `[notes + 8]`, etc. — sans boucle, on n'en a pas vu).
3. Divise par 5 (`idiv` avec `rdx = 0`).
4. Sort avec la moyenne comme code de retour.

Résultat attendu : `(12+14+18+16+10) / 5 = 70 / 5 = 14`. Donc `echo $?` doit afficher **14**.

### ✅ Tu sais maintenant…

- Qu'une **variable assembleur = un label sur une adresse**
- La différence cruciale **`x`** (adresse) vs **`[x]`** (contenu)
- Lire et écrire en mémoire avec **`mov`**
- Choisir la **taille** (`al`, `ax`, `eax`, `rax`)
- Réserver un **buffer** dans `.bss`
- Accéder à un **élément de tableau** avec un décalage en octets
- L'idée du **little-endian** (les octets stockés "à l'envers")

---


## Chapitre 11 — Chaînes de caractères et octets

### Le minimum à savoir

#### Une chaîne, c'est juste une suite d'octets

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

#### Pourquoi `db` ?

`db` = **define byte**. Comme une chaîne, c'est un **flux d'octets**, on l'écrit avec `db`. Le compilateur transforme automatiquement chaque caractère en son **code ASCII**.

```nasm
msg db "AB"          ; équivalent à : msg db 0x41, 0x42
```

#### Le retour ligne et le zéro final

Deux octets spéciaux à connaître :

- **`10`** (ou `0x0A`) = **retour ligne** (`\n`). On le met à la fin d'un message pour que la ligne suivante apparaisse.
- **`0`** (ou `0x00`) = **caractère NUL**. C'est le marqueur de fin de chaîne en C (mais **pas** pour les syscalls Linux).

```nasm
msg1 db "Hello", 10              ; pour les syscalls (write, etc.)
msg2 db "Hello", 0               ; pour les fonctions C (printf, etc.)
msg3 db "Hello", 10, 0           ; les deux, par sécurité
```

#### Deux styles de chaînes : Linux vs C

| Style | Comment ça marque la fin | Usage |
|-------|--------------------------|-------|
| **Style Linux** | Par sa **longueur** explicite (passée en argument) | Syscalls `write`, `read` |
| **Style C** | Par un **octet 0** à la fin | Fonctions `printf`, `strlen`, `strcmp` |

En clair : pour `write`, on donne la longueur. Pour `printf`, on met un `0` à la fin et `printf` s'arrête tout seul en le voyant.

#### Calculer la longueur avec `equ $ - msg`

```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg          ; len = nombre d'octets de msg
```

`$` signifie "ici", l'**adresse actuelle**. Donc `$ - msg` = "la distance entre `msg` et maintenant" = la longueur en octets.

> **Astuce :** mets toujours `equ $ - label` **juste après** la chaîne. Si tu mets autre chose entre les deux, le calcul est faux.

#### Modifier un caractère en mémoire

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

#### Accéder à un caractère par son index

```nasm
mov al, [msg]           ; al = 'B' = 0x42  (1er caractère)
mov al, [msg + 1]       ; al = 'o' = 0x6F  (2ème caractère)
mov al, [msg + 3]       ; al = 'j'         (4ème caractère)
```

Pour un tableau de caractères, l'index est **directement** le décalage (puisque chaque caractère fait 1 octet).

#### Afficher une portion seulement

`write` prend une longueur — donc tu peux n'afficher que **5 caractères** :

```nasm
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 5              ; n'afficher que 5 octets : "Bonjo"
syscall
```

#### Compter les caractères jusqu'à un délimiteur

C'est l'équivalent de `strlen()`. Sans boucle, on ne peut pas encore le coder proprement (on le fera au chapitre 17). Mais l'idée est de **parcourir octet par octet jusqu'à tomber sur un `0`** (style C) ou un `10` (style retour ligne).

### Très utile en pratique

#### Chaîne sur plusieurs lignes

```nasm
section .data
    menu db "1) Option A", 10
         db "2) Option B", 10
         db "3) Quitter",  10
    menu_len equ $ - menu
```

NASM concatène automatiquement les `db` successifs (puisque la mémoire est contiguë). Très pratique pour des menus.

#### Construire une chaîne caractère par caractère

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

#### Aperçu : pourquoi un `0` final pour la libc ?

Quand tu fais `printf("%s", msg)`, `printf` lit `msg` **caractère par caractère** jusqu'à rencontrer un octet `0`. Sans ce `0`, `printf` continuera à lire en mémoire **bien au-delà** de ta chaîne, affichant du garbage… jusqu'à crash. On en reparle au chapitre 21.

### Bonus

#### Caractères spéciaux

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

#### Convertir une lettre majuscule/minuscule

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

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée un programme `salut.asm` qui :
1. Déclare `msg db "Hello, World!", 10`.
2. Calcule `len equ $ - msg`.
3. Affiche le message via `write`.

**Autonome :** Modifie ton programme pour :
1. Remplacer le premier caractère par `'J'` avant d'afficher (→ "Jello, World!").
2. N'afficher que les **5 premiers caractères**.

**Défi :** Crée un programme qui affiche la lettre `'A'` seulement (1 octet, sans retour ligne). Puis modifie-le pour afficher la lettre `'A'` **puis** un retour ligne. Tu n'as droit qu'à 1 octet de buffer.

### 🧩 Mini-projet (chapitres 9-11) — Bannière dynamique

Crée `banniere2.asm` qui :

1. Déclare une chaîne `motif db "* * * BIENVENUE * * *", 10`.
2. Affiche la chaîne **trois fois** (3 syscalls write d'affilée).
3. **Bonus :** entre chaque affichage, modifie la première étoile en `'+'`.

> **Indice :** pour modifier, utilise `mov byte [motif], '+'`. Pour afficher, garde la même longueur.

### ✅ Tu sais maintenant…

- Qu'une **chaîne = suite d'octets** en mémoire
- Le rôle de **`db`** pour déclarer des octets
- La différence entre **style Linux (longueur)** et **style C (`0` final)**
- Les codes ASCII utiles : `10` pour `\n`, `0` pour la fin C
- Modifier un **caractère en mémoire** avec `mov byte [...]`
- Accéder à un caractère **par son index** (`[msg + N]`)
- Pourquoi NASM **n'interprète pas `\n`** dans une chaîne

---


## Chapitre 12 — `lea` et modes d'adressage

### Le minimum à savoir

#### `lea` : "Load Effective Address"

`lea` est une instruction qu'on confond souvent avec `mov`. Elle a une particularité :

> **`lea` calcule une adresse mais ne lit pas la mémoire.**

```nasm
mov rax, [rbx]       ; rax = CONTENU à l'adresse rbx
lea rax, [rbx]       ; rax = rbx (juste copie l'adresse, ne lit rien)
```

Avec `mov`, les crochets veulent dire "lis la mémoire". Avec `lea`, ils signifient juste "calcule cette expression d'adresse". **Aucune lecture mémoire** n'est faite.

#### Pourquoi `lea` est si fréquent en reverse engineering

Imagine que tu veux faire `rax = rbx + rcx*8 + 16`. Sans `lea`, ça prend plusieurs instructions :

```nasm
mov rax, rcx
imul rax, 8
add rax, rbx
add rax, 16
```

Avec `lea`, **une seule** instruction :

```nasm
lea rax, [rbx + rcx*8 + 16]
```

Du coup, les compilateurs C utilisent `lea` **partout**, même pour faire des additions simples. Tu verras `lea` en désassemblage **tout le temps**.

#### Les modes d'adressage de x86-64

Quand tu vois des `[...]` en assembleur, ce qui est dedans peut être plus complexe qu'un simple registre. Voici les **modes d'adressage** possibles :

| Mode | Exemple | Calcul |
|------|---------|--------|
| Direct | `[var]` | adresse de `var` |
| Registre | `[rax]` | adresse contenue dans `rax` |
| Base + déplacement | `[rax + 8]` | `rax + 8` |
| Base + index | `[rax + rcx]` | `rax + rcx` |
| Base + index × échelle | `[rax + rcx*4]` | `rax + 4*rcx` |
| Forme complète | `[rax + rcx*8 + 16]` | `rax + 8*rcx + 16` |

L'**échelle** ne peut être que `1`, `2`, `4` ou `8` (souvent 8 pour les `qword`, 4 pour les `dword`, 1 pour les `byte`).

#### Cas d'usage typique : parcourir un tableau

Si tu as `tableau dq 10, 20, 30, 40` et que tu veux l'élément à l'index `rcx` :

```nasm
mov rax, [tableau + rcx*8]   ; rax = tableau[rcx]
```

Si tu veux l'**adresse** de cet élément (et non son contenu) :

```nasm
lea rax, [tableau + rcx*8]   ; rax = &tableau[rcx]
```

C'est exactement comme **`&tab[i]` vs `tab[i]`** en C.

#### `mov` ou `lea` ? Comparaison

```nasm
section .data
    x dq 42

section .text
    mov rax, x         ; rax = adresse de x (compile-time)
    lea rax, [x]       ; rax = adresse de x (équivalent, plus moderne)

    mov rbx, [x]       ; rbx = 42 (contenu)
    lea rbx, [x]       ; rbx = adresse de x (PAS le contenu)
```

> **Règle :** si tu veux **le contenu** → `mov reg, [...]`. Si tu veux **l'adresse** ou **une formule d'addition** → `lea reg, [...]`.

### Très utile en pratique

#### `lea` pour des additions/multiplications rapides

Comme `lea` permet `base + index*échelle + déplacement`, on peut s'en servir pour des calculs sans `add`/`imul` :

```nasm
; rax = rbx + rcx
lea rax, [rbx + rcx]

; rax = rbx * 5  (= rbx + rbx*4)
lea rax, [rbx + rbx*4]

; rax = rbx * 3 + 7
lea rax, [rbx + rbx*2 + 7]
```

> **Avantage :** `lea` ne modifie **pas les flags** (contrairement à `add`). Ça permet de faire des calculs sans casser une comparaison en cours.

#### Avec les chaînes

Tu peux récupérer l'adresse d'un octet précis d'une chaîne :

```nasm
section .data
    msg db "Hello", 0

section .text
    lea rax, [msg + 2]    ; rax pointe sur le 'l' (3ème caractère)
    mov al, [rax]         ; al = 'l'
```

### Bonus

#### `lea` dans le code généré par gcc

Si tu compiles ceci en C :

```c
int f(int a, int b) {
    return a + b * 4 + 10;
}
```

`gcc -O0 -masm=intel -S` produit (extrait) :

```nasm
lea     eax, [rdi + rsi*4 + 10]
```

Une **seule instruction** au lieu de quatre. C'est pour ça que `lea` est partout. Comprendre `lea` = comprendre 30 % du code désassemblé.

#### `RIP-relative addressing`

En x86-64, on voit souvent `[rel msg]` ou `[rip + ...]`. C'est l'**adressage relatif à `rip`** (le pointeur d'instruction). C'est ce que les exécutables modernes utilisent pour être déplaçables en mémoire (PIE). Pour ce cours, NASM gère ça automatiquement quand on compile avec `default rel` ou quand on lie un programme dynamique. Ne t'en préoccupe pas tant que tu fais des programmes statiques avec `ld`.

### ❌ Erreur classique

```
Croire que lea charge le contenu mémoire
→ NON. lea calcule l'adresse, ne lit rien.

Utiliser lea quand on voulait mov : lea rax, [x] alors qu'on voulait le contenu
→ Bug silencieux : tu as l'adresse, pas la valeur.

Utiliser une échelle interdite : [rax + rcx*3]
→ Échelle = 1, 2, 4 ou 8 uniquement. 3 est interdit.

Oublier que dans [tab + rcx*8], rcx est en éléments
→ Si tableau de qword, rcx*8 est correct.
→ Si tableau de dword, ce serait rcx*4.
→ Si tableau d'octets, ce serait rcx*1.

Confondre [tab + rcx] et [tab + rcx*8] pour un tableau de qword
→ La 1ère lit à l'octet rcx, la 2nde à l'élément rcx.
```

### Exercices

**Guidé :** Recopie et compile :

```nasm
section .data
    x dq 100

section .text
global _start
_start:
    mov rax, x          ; adresse
    lea rbx, [x]        ; adresse aussi
    mov rcx, [x]        ; contenu
    lea rdx, [x + 8]    ; adresse + 8

    mov rdi, 0
    mov rax, 60
    syscall
```

Lance dans GDB. Compare `rax` et `rbx` (devrait être identiques). Compare `rax` et `rcx`. Comprends `rdx`.

**Autonome :** Soit le tableau `tab dq 10, 20, 30, 40, 50`. Sans utiliser `add` ni `imul`, écris une instruction **unique** qui met dans `rax` l'adresse de `tab[3]` (= adresse du `40`).

**Défi :** Réécris ces lignes en utilisant `lea` au lieu de `mov`/`add` :

```nasm
; version classique
mov rax, rbx
add rax, rcx
add rax, 100

; → ta version avec un seul lea ?
```

> **Réponse :** `lea rax, [rbx + rcx + 100]`

### ✅ Tu sais maintenant…

- La différence entre **`mov`** (lit la mémoire) et **`lea`** (calcule juste une adresse)
- Les **modes d'adressage** : `[reg]`, `[reg + N]`, `[reg + reg*échelle]`, `[reg + reg*échelle + N]`
- Pourquoi **`lea` est partout** dans le code compilé
- Utiliser `lea` pour des **additions/multiplications rapides**
- Que les **échelles valides** sont 1, 2, 4 ou 8
- Reconnaître `lea` en **reverse engineering**

---
