---
title: Chapitre 20 — Stack frame, rbp et variables locales
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VII — Pile et fonctions
  - index.md
---

## Le minimum à savoir

### Pourquoi des variables locales ?

Une fonction complexe a besoin de plus de "place de travail" que les 6 registres d'arguments. Et tu ne veux **pas** utiliser `.data` (qui est partagé, non-récursif). Solution : **allouer de la place sur la pile**, valable seulement pendant la durée de la fonction.

### Le stack frame : l'espace de travail d'une fonction

Quand une fonction s'exécute, elle se réserve un **cadre de pile** (stack frame) :

```
   Adresses hautes
       ↑
       │  ┌──────────────┐
       │  │ args 7+      │ (si plus de 6 arguments)
       │  ├──────────────┤
       │  │ adresse retour│ ← empilée par 'call'
       │  ├──────────────┤
       │  │ ancien rbp   │ ← sauvegardé par le prologue
       │  ├──────────────┤  ← rbp pointe ici
       │  │ var locale 1 │  ← [rbp - 8]
       │  ├──────────────┤
       │  │ var locale 2 │  ← [rbp - 16]
       │  ├──────────────┤
       │  │ ...          │  ← rsp pointe ici (sommet)
       │  └──────────────┘
       ↓
   Adresses basses
```


`rbp` est le **point de repère stable** du cadre. `rsp` peut bouger pendant la fonction. `rbp` ne bouge pas.

### Le prologue et l'épilogue : le squelette standard

Toute fonction qui utilise des locales suit ce squelette :

```nasm
ma_fonction:
    ; ─── PROLOGUE ───
    push rbp            ; sauvegarder l'ancien rbp
    mov rbp, rsp        ; nouveau cadre : rbp = sommet actuel
    sub rsp, 32         ; réserver 32 octets pour les locales (4 qword)

    ; ─── CORPS ───
    mov qword [rbp - 8], 100      ; locale 1 = 100
    mov qword [rbp - 16], 200     ; locale 2 = 200
    ; ... travailler ...

    ; ─── ÉPILOGUE ───
    mov rsp, rbp        ; libérer les locales
    pop rbp             ; restaurer l'ancien rbp
    ret
```


Mémorise ce **squelette par cœur**. C'est **exactement** ce que produit gcc, et **exactement** ce que tu verras en reverse engineering.

### Pourquoi `[rbp - 8]` et pas `[rbp + 8]` ?

Parce que la pile **descend**. Les variables locales sont **au-dessous** de `rbp` (vers les adresses basses), donc avec un décalage **négatif**.

| Décalage | Contenu |
|----------|---------|
| `[rbp + 16]` et +  | 7ème argument, 8ème, etc. (rares) |
| `[rbp + 8]` | adresse de retour (empilée par `call`) |
| `[rbp]` | ancien rbp |
| `[rbp - 8]` | **1ère variable locale** |
| `[rbp - 16]` | 2ème variable locale |
| `[rbp - 24]` | 3ème variable locale |

### Exemple complet : fonction avec locales

```nasm
; Fonction somme_carres(a, b) : rax = a*a + b*b
somme_carres:
    push rbp
    mov rbp, rsp
    sub rsp, 16                 ; 2 qword de locales

    mov [rbp - 8], rdi          ; locale1 = a
    mov [rbp - 16], rsi         ; locale2 = b

    mov rax, [rbp - 8]
    imul rax, rax               ; rax = a*a

    mov rcx, [rbp - 16]
    imul rcx, rcx               ; rcx = b*b

    add rax, rcx                ; rax = a*a + b*b

    mov rsp, rbp                ; libérer locales
    pop rbp
    ret

_start:
    mov rdi, 3
    mov rsi, 4
    call somme_carres           ; rax = 9 + 16 = 25
    mov rdi, rax
    mov rax, 60
    syscall
```


`./prog ; echo $?` → `25`.

### Stocker les arguments en locales : pourquoi ?

Tu remarques qu'on a copié `rdi` et `rsi` dans `[rbp - 8]` et `[rbp - 16]`. Pourquoi ne pas les utiliser directement depuis `rdi`/`rsi` ?

Plusieurs raisons (et c'est ce que fait gcc en `-O0`) :

- Si on **appelle une autre fonction**, `rdi`/`rsi` sont caller-saved → écrasés.
- Si on a besoin des arguments **plus tard** dans la fonction, c'est plus sûr.
- Ça rend la fonction plus **lisible** à debug.

En `-O2` (avec optimisations), gcc évite cette copie inutile. Mais en `-O0` (sans), c'est systématique.

## Très utile en pratique

### Reconnaître le prologue/épilogue en reverse

C'est **L'indice n°1** pour repérer une fonction dans un binaire :

```
push rbp
mov  rbp, rsp
sub  rsp, ...
```


= **début de fonction**.

```
mov  rsp, rbp     (ou leave)
pop  rbp
ret
```


= **fin de fonction**.

Quand tu lis du code désassemblé, **chaque** apparition de `push rbp ; mov rbp, rsp` est le **début d'une fonction**. Tu peux ainsi cartographier un binaire entier.

### L'instruction `leave`

`leave` est un raccourci pour `mov rsp, rbp ; pop rbp`. Tu verras donc souvent :

```
leave
ret
```


= épilogue compact. C'est exactement la même chose, juste un peu plus court.

### Combien d'espace réserver ?

Multiplie `nombre de locales × 8` (pour des qword) et arrondis à 16 si tu vas appeler une autre fonction (alignement, voir ch. 21).

```nasm
; 3 variables locales qword
sub rsp, 24            ; non aligné sur 16
sub rsp, 32            ; aligné sur 16 → préférable
```


### Plus de 6 arguments : sur la pile

Si une fonction a 8 arguments, les 6 premiers vont dans `rdi, rsi, rdx, rcx, r8, r9`, et les 7ème et 8ème sont **empilés par l'appelant** avant le `call`. Tu les lis avec `[rbp + 16]` et `[rbp + 24]`. Cas rare en pédagogie débutante.

## Bonus

### Variables locales : taille fine

Tu peux mélanger des tailles :

```nasm
sub rsp, 16
mov byte  [rbp - 1], 'A'           ; 1 octet
mov dword [rbp - 8], 12345         ; 4 octets
mov qword [rbp - 16], 999999       ; 8 octets
```


En pratique, en pédagogie, **alloue tout en qword** : c'est plus simple à raisonner.

### Pourquoi rbp ?

Sans `rbp`, tu devrais référencer tes locales avec `rsp`, qui **bouge** (à chaque `push`/`pop`). `rbp` reste **fixe** pendant toute la fonction, donc `[rbp - 8]` désigne **toujours** la même locale.

En `-O1` ou `-O2`, gcc peut omettre `rbp` (`-fomit-frame-pointer`). Le code devient plus dense, mais **plus dur à lire en reverse**. C'est une des raisons pour lesquelles le reverse est plus simple sur du `-O0`.

## ❌ Erreur classique

```
Oublier de restaurer rsp avant ret
→ Crash au ret (l'adresse de retour est mal localisée).

Confondre [rbp - 8] (locale) et [rbp + 8] (adresse de retour)
→ Modifier l'adresse de retour = corruption mémoire = crash ou exploit.

Réserver de l'espace mais pas le libérer
→ Chaque appel de la fonction "fuit" sur la pile. Crash après quelques appels.

Mauvais offset (oublier que c'est en octets)
→ Pour 3 qword consécutifs : [rbp-8], [rbp-16], [rbp-24]. PAS -1, -2, -3.

Modifier rbp dans le corps de la fonction
→ Tu casses ta propre référence aux locales.

Oublier push rbp au début et pop rbp à la fin
→ La fonction appelante ne retrouve plus son cadre.
```


## Exercices

**Guidé :** Recopie et compile l'exemple `somme_carres` ci-dessus. Lance-le dans GDB, mets un breakpoint sur `somme_carres`, et observe `rbp` et `rsp` après le prologue. Affiche les locales avec `x/2gx $rbp - 16`.

**Autonome :** Réécris la fonction `factorielle(n)` du chapitre 19 en utilisant un stack frame propre avec **`push rbp / mov rbp, rsp` / `leave / ret`**. Stocke `n` dans une locale `[rbp - 8]`.

**Défi :** Crée une fonction `moyenne_quatre(a, b, c, d)` qui prend 4 arguments (tous dans des registres), les stocke en 4 locales, calcule la somme, divise par 4, et renvoie le résultat. Vérifie `moyenne_quatre(10, 20, 30, 40) = 25`.

## 🧩 Mini-projet (chapitres 18-20) — Mini-application structurée

Crée `app.asm` avec :

1. Une fonction **`afficher(adresse, longueur)`** qui fait un `write` propre.
2. Une fonction **`carre(n)`** qui renvoie `n*n`, avec stack frame.
3. Une fonction **`max(a, b, c)`** qui renvoie le maximum des trois, avec stack frame et 3 locales.
4. Une fonction **`exit_avec(code)`** qui appelle `exit` avec le code donné.

Dans `_start` :

- Affiche `"Bienvenue dans l'app !"`.
- Calcule `carre(7)` (= 49).
- Calcule `max(carre(7), 50, 42)` (= 50).
- Appelle `exit_avec(<le max>)`.

`echo $?` doit afficher `50`.

## ✅ Tu sais maintenant…

- Construire un **stack frame** : prologue (`push rbp ; mov rbp, rsp ; sub rsp, N`)
- Le terminer : épilogue (`mov rsp, rbp ; pop rbp ; ret`) ou `leave / ret`
- Allouer des **variables locales** sur la pile
- Y accéder avec **`[rbp - offset]`**
- Distinguer **locale** (`[rbp - N]`) et **adresse de retour** (`[rbp + 8]`)
- Reconnaître un **prologue de fonction** dans du code désassemblé
- L'instruction **`leave`** comme raccourci

À partir d'ici, tu maîtrises **TOUT le langage de base** de l'assembleur x86-64. Les chapitres suivants te montrent comment l'utiliser avec C et comment **lire** les programmes compilés.

---

## 🚩 Checkpoint — Fin de la Partie VII

C'est **le checkpoint le plus important** du cours. Tu dois pouvoir :

- [ ] Empiler et dépiler des valeurs avec `push` et `pop`, en gardant la pile équilibrée.
- [ ] Comprendre que la pile descend vers les adresses basses.
- [ ] Écrire une fonction simple avec `call` et `ret`.
- [ ] Respecter la convention d'appel System V (args dans `rdi, rsi, rdx, rcx, r8, r9`, retour dans `rax`).
- [ ] Distinguer registres **caller-saved** et **callee-saved**.
- [ ] Construire un **stack frame** avec prologue (`push rbp ; mov rbp, rsp ; sub rsp, N`) et épilogue (`leave ; ret`).
- [ ] Accéder à une variable locale via `[rbp - N]`.
- [ ] **Reconnaître un prologue de fonction** dans du code désassemblé.

> **Si ce checkpoint est solide, tu es prêt pour le reverse engineering.** Les parties suivantes ne font qu'appliquer ces réflexes à du code que tu n'as pas écrit.

---
