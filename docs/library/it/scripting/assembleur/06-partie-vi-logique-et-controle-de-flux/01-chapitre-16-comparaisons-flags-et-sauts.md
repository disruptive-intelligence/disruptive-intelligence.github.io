---
title: Chapitre 16 — Comparaisons, flags et sauts
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VI — Logique et contrôle de flux
  - index.md
---

## Le minimum à savoir

### Pourquoi ce chapitre est central

Jusqu'ici, tes programmes s'exécutent **toujours dans le même ordre**, de haut en bas. C'est ce qu'on appelle un programme **séquentiel**. Mais un vrai programme doit pouvoir **décider** : "si l'utilisateur tape oui, affiche ceci ; sinon, affiche cela". C'est ce qu'on appelle un **`if`** en Python ou Bash.

> **À retenir :** ce chapitre est **le pivot** du cours. Une fois que tu sais comparer et sauter, tu peux écrire de **vrais** programmes.

### `cmp` : la comparaison

L'instruction **`cmp a, b`** fait deux choses :

1. Elle calcule **`a - b`** mentalement.
2. Elle **ne stocke pas** le résultat — elle met juste à jour les **drapeaux (flags)** du CPU.

```nasm
cmp rax, rbx     ; compare rax et rbx (ne modifie rien)
```


C'est comme dire au CPU : "regarde ces deux valeurs, mémorise leur relation". Aucun registre n'est changé. Seuls les flags bougent.

### Les flags : les petits indicateurs du CPU

Le CPU a un **registre de flags** (`rflags`) avec plusieurs bits indicateurs. Les 4 importants pour démarrer :

| Flag | Nom | Signification |
|------|-----|---------------|
| **`ZF`** | Zero Flag | Mis à 1 si le résultat est **zéro** (donc si `a == b`) |
| **`SF`** | Sign Flag | Mis à 1 si le résultat est **négatif** (bit de signe = 1) |
| **`CF`** | Carry Flag | Mis à 1 en cas de **retenue** (utile pour les non signés) |
| **`OF`** | Overflow Flag | Mis à 1 en cas de **débordement signé** |

> **Pas de panique.** Tu n'as pas besoin de tout maîtriser. Les **sauts conditionnels** vont lire ces flags à ta place. Tu choisis juste le bon saut.

### `jmp` : saut inconditionnel

`jmp etiquette` saute **toujours** vers cette étiquette, peu importe les flags :

```nasm
    mov rax, 1
    jmp fin            ; saute par-dessus le code suivant
    mov rax, 999       ; ← jamais exécuté
fin:
    mov rax, 60
    syscall
```


### Sauts conditionnels : la suite logique

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

### Premier `if` en assembleur

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

### Le piège du sens de `cmp`

`cmp a, b` fait `a - b`. Donc :

- `cmp rax, 10` + `jl ...` → saute si **`rax < 10`** (et non `10 < rax`).

Lis-le en français : "compare rax avec 10, saute si **rax est inférieur**". Comme `mov`, c'est destination/sujet à gauche, valeur de comparaison à droite.

### Pattern `if`/`else` classique

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


### Pattern `if` (sans `else`)

Si tu n'as pas de "sinon", c'est plus simple :

```nasm
    cmp rax, 0
    jne pas_zero       ; saute si rax != 0

    ; CODE SI rax == 0 ici
    ; ...

pas_zero:
    ; suite du programme
```


## Très utile en pratique

### Comparer un registre à zéro : `test`

Pour tester si un registre vaut 0, on utilise souvent **`test`** au lieu de `cmp` :

```nasm
test rax, rax          ; met ZF=1 si rax == 0
jz fin                 ; saute si rax == 0 (jz = je)
```


`test a, a` fait `a AND a`, ce qui donne `a`. Donc ZF=1 ssi `a == 0`. C'est un idiome **très courant** en reverse engineering. Quand tu vois `test eax, eax / je ...`, c'est `if (eax == 0)`.

### Tableau de correspondance complet

| Python | Assembleur |
|--------|------------|
| `if a == b: …` | `cmp a, b ; je …` |
| `if a != b: …` | `cmp a, b ; jne …` |
| `if a < b: …`  | `cmp a, b ; jl …` (signé) |
| `if a > b: …`  | `cmp a, b ; jg …` (signé) |
| `if a == 0: …` | `test a, a ; jz …` |
| `if a != 0: …` | `test a, a ; jnz …` |

### Détecter une erreur de syscall

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


## Bonus

### Voir les flags dans GDB

```
(gdb) info registers eflags
eflags  0x202  [ IF ]
```


Avec pwndbg, les flags sont **affichés en clair** à chaque pas, avec le nom des bits actifs (ZF, SF, CF, OF…). Encore une raison de l'installer.

### Sauts conditionnels rares mais utiles

| Saut | Effet |
|------|-------|
| `jz` / `jnz` | Synonymes de `je` / `jne` (saut si zéro / non zéro) |
| `js` / `jns` | Saut si négatif / positif (Sign Flag) |
| `jc` / `jnc` | Saut si Carry / no Carry |
| `jo` / `jno` | Saut si Overflow / no Overflow |

`jz`/`jnz` sont **identiques** à `je`/`jne` (juste un autre nom). Tu les verras tous les deux dans du code désassemblé.

## ❌ Erreur classique

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


## Exercices

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

## 🧩 Mini-projet (chapitre 16) — Comparaison de deux nombres

Crée `compare.asm` qui :

1. Déclare `a dq 25` et `b dq 17` dans `.data`.
2. Compare les deux valeurs.
3. Affiche un des trois messages :
   - `"A est plus grand"`
   - `"B est plus grand"`
   - `"A et B sont egaux"`
4. Quitte avec code 0.

Tu auras besoin de trois messages dans `.data`, et de **trois branches** (`jg`, `jl`, et le cas d'égalité par défaut).

## ✅ Tu sais maintenant…

- Ce qu'est un **flag** (ZF, SF, CF, OF)
- Comparer avec **`cmp a, b`** (qui calcule `a - b` et met à jour les flags)
- Sauter inconditionnellement avec **`jmp`**
- Sauter conditionnellement : **`je, jne, jl, jg, jle, jge, jb, ja, jbe, jae`**
- La différence **signé** (`jl, jg`) vs **non signé** (`jb, ja`)
- Le pattern **`test rax, rax / jz`** pour tester contre zéro
- Écrire un **`if/else` complet** en ASM

---
