---
title: PARTIE VI — LOGIQUE ET CONTRÔLE DE FLUX
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 6
chapters: 10
---

---


## Chapitre 16 — Comparaisons, flags et sauts

### Le minimum à savoir

#### Pourquoi ce chapitre est central

Jusqu'ici, tes programmes s'exécutent **toujours dans le même ordre**, de haut en bas. C'est ce qu'on appelle un programme **séquentiel**. Mais un vrai programme doit pouvoir **décider** : "si l'utilisateur tape oui, affiche ceci ; sinon, affiche cela". C'est ce qu'on appelle un **`if`** en Python ou Bash.

> **À retenir :** ce chapitre est **le pivot** du cours. Une fois que tu sais comparer et sauter, tu peux écrire de **vrais** programmes.

#### `cmp` : la comparaison

L'instruction **`cmp a, b`** fait deux choses :

1. Elle calcule **`a - b`** mentalement.
2. Elle **ne stocke pas** le résultat — elle met juste à jour les **drapeaux (flags)** du CPU.

```nasm
cmp rax, rbx     ; compare rax et rbx (ne modifie rien)
```

C'est comme dire au CPU : "regarde ces deux valeurs, mémorise leur relation". Aucun registre n'est changé. Seuls les flags bougent.

#### Les flags : les petits indicateurs du CPU

Le CPU a un **registre de flags** (`rflags`) avec plusieurs bits indicateurs. Les 4 importants pour démarrer :

| Flag | Nom | Signification |
|------|-----|---------------|
| **`ZF`** | Zero Flag | Mis à 1 si le résultat est **zéro** (donc si `a == b`) |
| **`SF`** | Sign Flag | Mis à 1 si le résultat est **négatif** (bit de signe = 1) |
| **`CF`** | Carry Flag | Mis à 1 en cas de **retenue** (utile pour les non signés) |
| **`OF`** | Overflow Flag | Mis à 1 en cas de **débordement signé** |

> **Pas de panique.** Tu n'as pas besoin de tout maîtriser. Les **sauts conditionnels** vont lire ces flags à ta place. Tu choisis juste le bon saut.

#### `jmp` : saut inconditionnel

`jmp etiquette` saute **toujours** vers cette étiquette, peu importe les flags :

```nasm
    mov rax, 1
    jmp fin            ; saute par-dessus le code suivant
    mov rax, 999       ; ← jamais exécuté
fin:
    mov rax, 60
    syscall
```

#### Sauts conditionnels : la suite logique

Après un `cmp`, tu peux sauter **selon le résultat** :

| Saut | Condition | Équivalent Python |
|------|-----------|-------------------|
| **`je`** | si égal (`==`) | `if a == b` |
| **`jne`** | si non égal (`!=`) | `if a != b` |
| **`jl`** | si **inférieur** (signé) | `if a < b` |
| **`jle`** | si inférieur ou égal | `if a <= b` |
| **`jg`** | si supérieur (signé) | `if a > b` |
| **`jge`** | si supérieur ou égal | `if a >= b` |
| **`jb`** | si inférieur (**non signé**) | (pour entiers non signés) |
| **`ja`** | si supérieur (**non signé**) | (pour entiers non signés) |

> **Règle d'or :** `jl/jg/jle/jge` pour les nombres **signés** (qui peuvent être négatifs). `jb/ja/jbe/jae` pour les nombres **non signés** (toujours positifs, ex : tailles, adresses).

#### Premier `if` en assembleur

Voici l'équivalent ASM de :
```python
if x == 42:
    exit(1)
else:
    exit(0)
```

En assembleur :

```nasm
section .data
    x dq 42

section .text
global _start
_start:
    mov rax, [x]
    cmp rax, 42        ; comparer rax et 42
    je egal            ; si rax == 42, saute à 'egal'

    ; bloc "else"
    mov rdi, 0
    jmp sortie

egal:
    ; bloc "if"
    mov rdi, 1

sortie:
    mov rax, 60
    syscall
```

Exécution : `./prog ; echo $?` → affiche `1` (car `x == 42`). Change `x dq 41`, recompile : ça affichera `0`.

#### Le piège du sens de `cmp`

`cmp a, b` fait `a - b`. Donc :

- `cmp rax, 10` + `jl ...` → saute si **`rax < 10`** (et non `10 < rax`).

Lis-le en français : "compare rax avec 10, saute si **rax est inférieur**". Comme `mov`, c'est destination/sujet à gauche, valeur de comparaison à droite.

#### Pattern `if`/`else` classique

Voici le **squelette à mémoriser** :

```nasm
    cmp rax, rbx
    je egal            ; ← saute si vrai

    ; CODE DU "ELSE" ici
    ; ...
    jmp fin            ; ← ne pas exécuter le "if"

egal:
    ; CODE DU "IF" ici
    ; ...

fin:
    ; suite du programme
```

#### Pattern `if` (sans `else`)

Si tu n'as pas de "sinon", c'est plus simple :

```nasm
    cmp rax, 0
    jne pas_zero       ; saute si rax != 0

    ; CODE SI rax == 0 ici
    ; ...

pas_zero:
    ; suite du programme
```

### Très utile en pratique

#### Comparer un registre à zéro : `test`

Pour tester si un registre vaut 0, on utilise souvent **`test`** au lieu de `cmp` :

```nasm
test rax, rax          ; met ZF=1 si rax == 0
jz fin                 ; saute si rax == 0 (jz = je)
```

`test a, a` fait `a AND a`, ce qui donne `a`. Donc ZF=1 ssi `a == 0`. C'est un idiome **très courant** en reverse engineering. Quand tu vois `test eax, eax / je ...`, c'est `if (eax == 0)`.

#### Tableau de correspondance complet

| Python | Assembleur |
|--------|------------|
| `if a == b: …` | `cmp a, b ; je …` |
| `if a != b: …` | `cmp a, b ; jne …` |
| `if a < b: …`  | `cmp a, b ; jl …` (signé) |
| `if a > b: …`  | `cmp a, b ; jg …` (signé) |
| `if a == 0: …` | `test a, a ; jz …` |
| `if a != 0: …` | `test a, a ; jnz …` |

#### Détecter une erreur de syscall

Tu te souviens : les syscalls renvoient une valeur négative en cas d'erreur. Maintenant tu peux tester :

```nasm
mov rax, 2          ; open
mov rdi, chemin
mov rsi, 0
syscall

cmp rax, 0
jl erreur           ; rax < 0 → erreur

; suite normale
; ...
jmp fin

erreur:
; afficher un message d'erreur
; ...

fin:
```

### Bonus

#### Voir les flags dans GDB

```
(gdb) info registers eflags
eflags  0x202  [ IF ]
```

Avec pwndbg, les flags sont **affichés en clair** à chaque pas, avec le nom des bits actifs (ZF, SF, CF, OF…). Encore une raison de l'installer.

#### Sauts conditionnels rares mais utiles

| Saut | Effet |
|------|-------|
| `jz` / `jnz` | Synonymes de `je` / `jne` (saut si zéro / non zéro) |
| `js` / `jns` | Saut si négatif / positif (Sign Flag) |
| `jc` / `jnc` | Saut si Carry / no Carry |
| `jo` / `jno` | Saut si Overflow / no Overflow |

`jz`/`jnz` sont **identiques** à `je`/`jne` (juste un autre nom). Tu les verras tous les deux dans du code désassemblé.

### ❌ Erreur classique

```
Inverser les opérandes de cmp
→ cmp rax, 10 et "saute si inférieur" = rax < 10 (pas 10 < rax).

Utiliser jl quand il faut jb (ou inversement)
→ jl/jg pour signé, jb/ja pour non signé. Si tu manipules une taille
  ou une adresse, c'est jb/ja.

Oublier de sauter après le bloc "if" → tomber dans le "else"
→ Toujours mettre jmp fin à la fin du "if".

Confondre je et jmp
→ jmp = inconditionnel. je = seulement si égal.

Croire que cmp modifie un registre
→ Non, cmp modifie seulement les flags.

Faire un calcul entre cmp et le saut
→ Le calcul écrase les flags. Toujours cmp puis directement jXX.

Mettre des labels en double dans le même fichier
→ Erreur du linker. Utilise des labels uniques (préfixe avec un point
  pour les labels locaux : .boucle, .fin).
```

### Exercices

**Guidé :** Crée `if.asm` qui :
- charge `x dq 50`
- si `x > 30`, sort avec code 1
- sinon, sort avec code 0

Teste avec différentes valeurs de `x`.

**Autonome :** Crée un programme qui charge `x dq -5` (déclare-le comme `dq -5`) et :
- sort avec code 1 si `x < 0`
- sort avec code 2 si `x == 0`
- sort avec code 3 si `x > 0`

> **Indice :** deux `cmp` + sauts en cascade.

**Défi :** Modifie le mini-`cat` du chapitre 15 pour qu'il affiche `"Erreur"` (sur stderr) si `open` renvoie une valeur négative, au lieu de continuer.

### 🧩 Mini-projet (chapitre 16) — Comparaison de deux nombres

Crée `compare.asm` qui :

1. Déclare `a dq 25` et `b dq 17` dans `.data`.
2. Compare les deux valeurs.
3. Affiche un des trois messages :
   - `"A est plus grand"`
   - `"B est plus grand"`
   - `"A et B sont egaux"`
4. Quitte avec code 0.

Tu auras besoin de trois messages dans `.data`, et de **trois branches** (`jg`, `jl`, et le cas d'égalité par défaut).

### ✅ Tu sais maintenant…

- Ce qu'est un **flag** (ZF, SF, CF, OF)
- Comparer avec **`cmp a, b`** (qui calcule `a - b` et met à jour les flags)
- Sauter inconditionnellement avec **`jmp`**
- Sauter conditionnellement : **`je, jne, jl, jg, jle, jge, jb, ja, jbe, jae`**
- La différence **signé** (`jl, jg`) vs **non signé** (`jb, ja`)
- Le pattern **`test rax, rax / jz`** pour tester contre zéro
- Écrire un **`if/else` complet** en ASM

---


## Chapitre 17 — Boucles

### Le minimum à savoir

#### Une boucle, c'est juste un `if` + un saut arrière

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

#### Les labels locaux `.foo`

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

#### Boucle `for` : compter de 0 à N-1

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

#### Boucle `while` : tant que…

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

#### Boucle infinie (à éviter en accident !)

```nasm
.boucle:
    ; ... rien qui sorte ...
    jmp .boucle
```

Ça tourne pour toujours. Si tu lances ça sans le faire exprès : **Ctrl+C** pour tuer le programme.

#### Exemple complet : compter de 0 à 9 avec affichage

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

#### Parcourir un tableau

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

### Très utile en pratique

#### `break` et `continue` équivalents

Pas d'instructions dédiées comme en Python, mais on les simule avec `jmp` :

- `break` → `jmp .fin`
- `continue` → `jmp .boucle` (sans le `inc`, attention à ne pas créer une boucle infinie !)

#### L'instruction `loop` (à connaître mais à éviter)

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

#### Compter à l'envers

Souvent plus efficace en ASM :

```nasm
    mov rcx, 10
.boucle:
    ; corps qui utilise rcx (de 10 à 1)
    dec rcx
    jnz .boucle         ; saute si rcx != 0
```

Pas de `cmp` nécessaire : `dec` met `ZF=1` quand le résultat atteint 0. Idiome très courant.

### Bonus

#### Boucles imbriquées

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

#### Convertir un entier en chaîne ASCII (algo complet)

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

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée `etoiles.asm` qui affiche **10 étoiles** sur la même ligne (`**********`) puis un retour ligne.

> **Indice :** utilise un buffer de 1 octet contenant `'*'`, et une boucle qui appelle `write` 10 fois. Plus un `write` final pour le `\n`.

**Autonome :** Crée un programme qui calcule **la somme des entiers de 1 à 100** dans `rax`. Renvoie le résultat comme code de retour modulo 256 (donc `5050 % 256 = 186` — vérifie avec `echo $?`).

**Défi :** Crée un programme qui calcule **factorielle(5)** = 1×2×3×4×5 = 120. Renvoie via le code de retour.

### 🧩 Mini-projet (chapitres 16-17) — Statistiques d'un tableau

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

### ✅ Tu sais maintenant…

- Construire une **boucle `for`** ou **`while`** en ASM
- Utiliser des **labels locaux** (`.boucle`, `.fin`)
- **Parcourir un tableau** avec un index dans un registre
- Faire des **boucles imbriquées**
- Préserver le compteur avec **`push`/`pop`** quand nécessaire
- Reconnaître l'instruction **`loop`** (mais préférer le pattern manuel)
- Compter à l'envers avec **`dec` + `jnz`**

---
