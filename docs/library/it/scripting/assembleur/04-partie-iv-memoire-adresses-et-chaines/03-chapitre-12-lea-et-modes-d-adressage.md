---
title: Chapitre 12 — lea et modes d'adressage
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie IV — Mémoire, adresses et chaînes
  - index.md
---

## Le minimum à savoir

### `lea` : "Load Effective Address"

`lea` est une instruction qu'on confond souvent avec `mov`. Elle a une particularité :

> **`lea` calcule une adresse mais ne lit pas la mémoire.**

```nasm
mov rax, [rbx]       ; rax = CONTENU à l'adresse rbx
lea rax, [rbx]       ; rax = rbx (juste copie l'adresse, ne lit rien)
```


Avec `mov`, les crochets veulent dire "lis la mémoire". Avec `lea`, ils signifient juste "calcule cette expression d'adresse". **Aucune lecture mémoire** n'est faite.

### Pourquoi `lea` est si fréquent en reverse engineering

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

### Les modes d'adressage de x86-64

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

### Cas d'usage typique : parcourir un tableau

Si tu as `tableau dq 10, 20, 30, 40` et que tu veux l'élément à l'index `rcx` :

```nasm
mov rax, [tableau + rcx*8]   ; rax = tableau[rcx]
```


Si tu veux l'**adresse** de cet élément (et non son contenu) :

```nasm
lea rax, [tableau + rcx*8]   ; rax = &tableau[rcx]
```


C'est exactement comme **`&tab[i]` vs `tab[i]`** en C.

### `mov` ou `lea` ? Comparaison

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

## Très utile en pratique

### `lea` pour des additions/multiplications rapides

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

### Avec les chaînes

Tu peux récupérer l'adresse d'un octet précis d'une chaîne :

```nasm
section .data
    msg db "Hello", 0

section .text
    lea rax, [msg + 2]    ; rax pointe sur le 'l' (3ème caractère)
    mov al, [rax]         ; al = 'l'
```


## Bonus

### `lea` dans le code généré par gcc

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

### `RIP-relative addressing`

En x86-64, on voit souvent `[rel msg]` ou `[rip + ...]`. C'est l'**adressage relatif à `rip`** (le pointeur d'instruction). C'est ce que les exécutables modernes utilisent pour être déplaçables en mémoire (PIE). Pour ce cours, NASM gère ça automatiquement quand on compile avec `default rel` ou quand on lie un programme dynamique. Ne t'en préoccupe pas tant que tu fais des programmes statiques avec `ld`.

## ❌ Erreur classique

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


## Exercices

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

## ✅ Tu sais maintenant…

- La différence entre **`mov`** (lit la mémoire) et **`lea`** (calcule juste une adresse)
- Les **modes d'adressage** : `[reg]`, `[reg + N]`, `[reg + reg*échelle]`, `[reg + reg*échelle + N]`
- Pourquoi **`lea` est partout** dans le code compilé
- Utiliser `lea` pour des **additions/multiplications rapides**
- Que les **échelles valides** sont 1, 2, 4 ou 8
- Reconnaître `lea` en **reverse engineering**

---
