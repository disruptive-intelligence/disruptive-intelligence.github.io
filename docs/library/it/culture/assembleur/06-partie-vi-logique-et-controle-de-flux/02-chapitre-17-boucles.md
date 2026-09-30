---
title: Chapitre 17 — Boucles
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VI — Logique ET contrôle de flux
  - index.md
---

## Le minimum à savoir

### Une boucle, c'est juste un `if` + un saut arrière

En Python :

```python
i = 0
while i < 10:
    print(i)
    i += 1
```


En assembleur, c'est l'**exact même schéma**, mais explicite :

```nasm
    mov rcx, 0          ; i = 0
.boucle:
    cmp rcx, 10
    jge .fin            ; si i >= 10, sortir
    ; ... corps de la boucle (utiliser rcx) ...
    inc rcx             ; i++
    jmp .boucle         ; recommencer
.fin:
```


> **À retenir :** une boucle = un **label de début**, une **condition de sortie**, un **corps**, une **mise à jour du compteur**, et un **saut arrière** vers le label.

### Les labels locaux `.foo`

NASM permet d'utiliser des labels **locaux** commençant par un point. Ces labels sont liés au dernier label "principal" :

```nasm
_start:
.boucle:           ; label local lié à _start
    ; ...
    jmp .boucle
.fin:

autre_fonction:
.boucle:           ; AUTRE label local, lié à 'autre_fonction'
    ; ...
```


Ça permet de réutiliser des noms comme `.boucle`, `.fin`, `.suivant` dans plusieurs endroits sans collision. **Utilise les labels locaux pour les boucles.**

### Boucle `for` : compter de 0 à N-1

Le pattern le plus courant :

```nasm
    mov rcx, 0          ; i = 0
.boucle:
    cmp rcx, 10
    jge .fin            ; condition de sortie
    ; ... corps ...
    inc rcx
    jmp .boucle
.fin:
```


### Boucle `while` : tant que…

Très similaire, mais la condition est différente :

```nasm
    mov rcx, [valeur]
.boucle:
    test rcx, rcx
    jz .fin             ; tant que rcx != 0
    ; ... corps ...
    dec rcx
    jmp .boucle
.fin:
```


### Boucle infinie (à éviter en accident !)

```nasm
.boucle:
    ; ... rien qui sorte ...
    jmp .boucle
```


Ça tourne pour toujours. Si tu lances ça sans le faire exprès : **Ctrl+C** pour tuer le programme.

### Exemple complet : compter de 0 à 9 avec affichage

```nasm
; compte.asm — Affiche les chiffres 0 à 9

section .bss
    chiffre resb 2          ; 1 octet pour le chiffre + 1 pour \n

section .text
global _start
_start:
    mov byte [chiffre + 1], 10    ; le \n est fixe

    mov rcx, 0
.boucle:
    cmp rcx, 10
    jge .fin

    ; convertir rcx (chiffre) en ASCII
    mov rax, rcx
    add al, '0'
    mov [chiffre], al

    ; afficher 2 octets (chiffre + \n)
    push rcx              ; ← sauvegarder rcx (write va l'écraser)
    mov rax, 1
    mov rdi, 1
    mov rsi, chiffre
    mov rdx, 2
    syscall
    pop rcx               ; ← restaurer rcx

    inc rcx
    jmp .boucle

.fin:
    mov rax, 60
    mov rdi, 0
    syscall
```


> **Tu remarques `push rcx` / `pop rcx` ?** C'est parce que `syscall` peut écraser `rcx`. Pour préserver notre compteur, on l'empile avant et on le récupère après. On approfondit la pile au **chapitre 18**.

Compile et exécute :

```
$ ./compte
0
1
2
3
4
5
6
7
8
9
```


### Parcourir un tableau

```nasm
section .data
    nombres dq 10, 20, 30, 40, 50
    taille  equ 5

section .text
global _start
_start:
    mov rcx, 0          ; index
    mov rax, 0          ; somme

.boucle:
    cmp rcx, taille
    jge .fin

    add rax, [nombres + rcx*8]   ; somme += nombres[rcx]
    inc rcx
    jmp .boucle

.fin:
    ; rax contient la somme = 150
    mov rdi, rax
    mov rax, 60
    syscall
```


`./prog ; echo $?` → `150`.

🎉 **Tu viens de coder ta première vraie boucle utile.**

## Très utile en pratique

### `break` et `continue` équivalents

Pas d'instructions dédiées comme en Python, mais on les simule avec `jmp` :

- `break` → `jmp .fin`
- `continue` → `jmp .boucle` (sans le `inc`, attention à ne pas créer une boucle infinie !)

### L'instruction `loop` (à connaître mais à éviter)

`loop etiquette` décrémente `rcx` et saute à `etiquette` si `rcx != 0`. C'est très compact :

```nasm
    mov rcx, 10
.boucle:
    ; ... corps ...
    loop .boucle        ; rcx-- puis saute si rcx != 0
```


> **Détail technique utile en reverse :** `loop` ressemble fortement à `dec rcx ; jnz`, mais **contrairement à `dec`, `loop` ne modifie pas les flags**. C'est parfois utile pour conserver l'état d'une comparaison précédente à travers la boucle.

Mais :

- Ça **impose** d'utiliser `rcx`.
- Ça oblige à compter **à l'envers** (10, 9, 8, …).
- C'est moins lisible et moins flexible.

> **Conseil :** retiens que `loop` existe (tu le verras en reverse), mais utilise le pattern `cmp + jXX` en pratique.

### Compter à l'envers

Souvent plus efficace en ASM :

```nasm
    mov rcx, 10
.boucle:
    ; corps qui utilise rcx (de 10 à 1)
    dec rcx
    jnz .boucle         ; saute si rcx != 0
```


Pas de `cmp` nécessaire : `dec` met `ZF=1` quand le résultat atteint 0. Idiome très courant.

## Bonus

### Boucles imbriquées

```nasm
    mov rcx, 0          ; boucle externe : i
.ext:
    cmp rcx, 3
    jge .fin_ext
    mov rdx, 0          ; boucle interne : j
.int:
    cmp rdx, 3
    jge .fin_int
    ; corps : utiliser rcx et rdx
    inc rdx
    jmp .int
.fin_int:
    inc rcx
    jmp .ext
.fin_ext:
```


> **Attention :** une boucle interne **ne doit pas écraser** le compteur de la boucle externe. Utilise des registres différents (`rcx`, `rdx`, `r12`, …).

### Convertir un entier en chaîne ASCII (algo complet)

Maintenant qu'on a les boucles, on peut afficher un entier multi-chiffres. L'algorithme :

```
buffer[20], i = 19
si nombre == 0 → buffer[i--] = '0'
sinon, tant que nombre > 0 :
    chiffre = nombre % 10
    buffer[i--] = chiffre + '0'
    nombre = nombre / 10
afficher buffer à partir de l'index i+1
```


C'est une excellente boucle pour s'entraîner — et c'est exactement le sujet du mini-projet final de ce chapitre.

## ❌ Erreur classique

```
Oublier l'incrément (inc rcx)
→ Boucle infinie. Ctrl+C.

Mauvais sens de saut : jge au lieu de jl
→ Boucle qui ne tourne jamais, ou qui ne s'arrête jamais.

Oublier d'initialiser le compteur
→ rcx contient une valeur aléatoire au départ.

Écraser rcx dans le corps (par un syscall, un imul, etc.)
→ La boucle perd son compte. Sauvegarde avec push/pop ou utilise r12-r15.

Confondre cmp rcx, 10 (sortir quand rcx >= 10) avec jl (sortir quand rcx < 10)
→ Toujours penser : "sous quelle condition je sors ?".

Indexer en éléments au lieu d'en octets : [tab + rcx] au lieu de [tab + rcx*8]
→ Bug classique pour les tableaux de qword.

Utiliser loop avec autre chose que rcx
→ Impossible : loop n'utilise que rcx.
```


## Exercices

**Guidé :** Crée `etoiles.asm` qui affiche **10 étoiles** sur la même ligne (`**********`) puis un retour ligne.

> **Indice :** utilise un buffer de 1 octet contenant `'*'`, et une boucle qui appelle `write` 10 fois. Plus un `write` final pour le `\n`.

**Autonome :** Crée un programme qui calcule **la somme des entiers de 1 à 100** dans `rax`. Renvoie le résultat comme code de retour modulo 256 (donc `5050 % 256 = 186` — vérifie avec `echo $?`).

**Défi :** Crée un programme qui calcule **factorielle(5)** = 1×2×3×4×5 = 120. Renvoie via le code de retour.

## 🧩 Mini-projet (chapitres 16-17) — Statistiques d'un tableau

Crée `stats.asm` qui :

1. Déclare `tab dq 42, 7, 89, 23, 56, 1, 100, 31, 4, 67` (10 nombres).
2. Calcule **la somme** dans `r12`.
3. Calcule **le maximum** dans `r13`.
4. Calcule **le minimum** dans `r14`.
5. Affiche le maximum comme code de retour (le minimum et la somme ne tiennent pas dans 0-255, on les regarde via GDB).

> **Indices :**
> - Une seule boucle qui parcourt le tableau.
> - Initialise `r13` (max) avec le premier élément avant la boucle.
> - Initialise `r14` (min) avec le premier élément aussi.
> - À chaque tour, `cmp rax, r13` puis `jle .pas_nouveau_max` etc.

Résultat attendu : `echo $?` → `100`.

## ✅ Tu sais maintenant…

- Construire une **boucle `for`** ou **`while`** en ASM
- Utiliser des **labels locaux** (`.boucle`, `.fin`)
- **Parcourir un tableau** avec un index dans un registre
- Faire des **boucles imbriquées**
- Préserver le compteur avec **`push`/`pop`** quand nécessaire
- Reconnaître l'instruction **`loop`** (mais préférer le pattern manuel)
- Compter à l'envers avec **`dec` + `jnz`**

---
