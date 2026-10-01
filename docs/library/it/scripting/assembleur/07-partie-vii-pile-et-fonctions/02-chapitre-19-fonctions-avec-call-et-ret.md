---
title: Chapitre 19 — Fonctions avec call et ret
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VII — Pile et fonctions
  - index.md
---

## Le minimum à savoir

### Pourquoi des fonctions ?

Jusqu'ici, tu écris des programmes "tout en un bloc". Mais dès que tu fais quelque chose deux fois (afficher un message, calculer une somme…), tu **copies-colles**. Pénible et fragile.

Les **fonctions** sont des blocs de code **réutilisables**, qu'on appelle à plusieurs endroits. Comme `def` en Python ou les fonctions Bash.

> **À retenir :** une fonction en ASM, c'est juste un **label** où tu sautes, et duquel tu reviens.

### `call` et `ret` : aller et revenir

| Instruction | Effet |
|-------------|-------|
| **`call fn`** | (1) Empile l'adresse de l'instruction suivante, (2) saute à `fn` |
| **`ret`** | (1) Dépile une adresse, (2) saute à cette adresse |

```
     code principal              fonction
     ──────────────              ──────────
       mov rdi, 5                ma_fonction:
       call ma_fonction  ─┐         ; corps
       mov rax, rax       │         ret    ─┐
       ; ...            ◄─┘                  │
                                            ◄┘
```


Le couple **`call` / `ret`** utilise la pile pour mémoriser où retourner. C'est pour ça qu'on a appris la pile **avant** les fonctions.

### Une première fonction

```nasm
; Fonction qui renvoie 42 dans rax

ma_fonction:
    mov rax, 42
    ret

; Programme principal
_start:
    call ma_fonction        ; rax devient 42
    mov rdi, rax
    mov rax, 60
    syscall
```


`./prog ; echo $?` → `42`.

### La convention d'appel System V AMD64

Sous Linux x86-64, **toutes les fonctions** (les tiennes, celles de la libc, celles d'un programme compilé) suivent les **mêmes règles** pour passer des arguments et récupérer un résultat. C'est l'**ABI System V AMD64**.

| Élément | Registre(s) |
|---------|-------------|
| **1er argument** | `rdi` |
| **2ème argument** | `rsi` |
| **3ème argument** | `rdx` |
| **4ème argument** | `rcx` |
| **5ème argument** | `r8` |
| **6ème argument** | `r9` |
| Arguments suivants | sur la pile |
| **Valeur de retour** | `rax` |

> **Mémorise ces 6 registres dans l'ordre. C'est valable PARTOUT.** Pour appeler `printf`, `malloc`, ou ta propre fonction, c'est toujours pareil.

### Fonction `carre(x)` qui renvoie `x * x`

```nasm
; carre(x) : rax = x * x
carre:
    mov rax, rdi        ; rax = x
    imul rax, rax       ; rax = x * x
    ret

_start:
    mov rdi, 7          ; argument : 7
    call carre          ; rax = 49
    mov rdi, rax        ; mettre 49 en code de retour
    mov rax, 60
    syscall
```


`./prog ; echo $?` → `49`.

### Caller-saved et callee-saved

C'est **le concept** à comprendre pour les fonctions. Quand tu appelles une fonction, certains registres peuvent être **détruits** par elle, d'autres pas :

| Catégorie | Registres | Qui doit sauvegarder ? |
|-----------|-----------|------------------------|
| **Caller-saved** | `rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11` | L'**appelant** (toi) avant `call` |
| **Callee-saved** | `rbx, rbp, r12, r13, r14, r15` | La **fonction** elle-même, si elle les modifie |

**Traduction pratique :**

- Si tu utilises `rcx` et tu appelles une fonction, **suppose qu'elle a détruit `rcx`**. Sauvegarde-le si tu veux le récupérer (`push rcx` / `pop rcx`).
- Si **tu écris** une fonction qui utilise `rbx`, **tu dois le préserver** (push au début, pop à la fin).

> **Pourquoi ?** C'est un **contrat** entre fonctions. Ça permet à n'importe quelle fonction d'appeler n'importe quelle autre sans tout casser.

### Squelette d'une fonction propre

```nasm
ma_fonction:
    ; (optionnel) sauvegarder les callee-saved utilisés
    push rbx

    ; ... corps de la fonction ...
    ; rdi = arg 1, rsi = arg 2, etc.
    ; résultat dans rax

    ; restaurer
    pop rbx
    ret
```


### Exemple : fonction `max(a, b)`

```nasm
; max(a, b) : rax = plus grand des deux
max:
    mov rax, rdi        ; rax = a
    cmp rdi, rsi
    jge .fin            ; si a >= b, garder rax = a
    mov rax, rsi        ; sinon rax = b
.fin:
    ret

_start:
    mov rdi, 17
    mov rsi, 42
    call max            ; rax = 42

    mov rdi, rax
    mov rax, 60
    syscall
```


### Appels en cascade

Une fonction peut **en appeler une autre**. Chaque `call` empile son adresse de retour, chaque `ret` la dépile. C'est récursif et ça marche **automatiquement** grâce à la pile.

```nasm
double:
    add rdi, rdi
    mov rax, rdi
    ret

quadruple:
    call double         ; rax = 2 * arg
    mov rdi, rax        ; nouvel arg = 2 * arg
    call double         ; rax = 4 * arg
    ret

_start:
    mov rdi, 5
    call quadruple      ; rax = 20
    mov rdi, rax
    mov rax, 60
    syscall
```


## Très utile en pratique

### Fonction `print_msg` réutilisable

```nasm
; print_msg(rdi = adresse, rsi = longueur)
print_msg:
    mov rdx, rsi        ; rdx = longueur
    mov rsi, rdi        ; rsi = adresse
    mov rdi, 1          ; stdout
    mov rax, 1          ; write
    syscall
    ret

_start:
    mov rdi, msg1
    mov rsi, len1
    call print_msg
    mov rdi, msg2
    mov rsi, len2
    call print_msg
    mov rax, 60
    mov rdi, 0
    syscall
```


Plus de copier-coller des 5 lignes de `write` ! C'est exactement le but d'une fonction.

> **Note importante :** comme `syscall` détruit `rcx` et `r11` (rappel du chapitre 6), une fonction comme `print_msg` qui contient un `syscall` **ne peut pas promettre de préserver `rcx` ou `r11`** à son appelant. Ce n'est pas grave ici : `rcx` et `r11` sont déjà **caller-saved** par convention System V. Mais si tu écris une fonction qui doit préserver `rcx` (parce qu'elle l'utilise comme compteur, par exemple), pense à le sauvegarder avec `push rcx` / `pop rcx` autour du `syscall`.

### `jmp` vs `call`

- **`jmp fn`** : saute à `fn`, mais **sans retour possible**.
- **`call fn`** : saute à `fn`, **et `ret` reviendra ici**.

Utilise `call` pour les fonctions, `jmp` pour les sauts internes (boucles, if/else).

## Bonus

### `ret` sans `call` ?

Si tu fais `ret` sans `call` préalable, le CPU dépile **ce qu'il y a au sommet de la pile** (peut-être n'importe quoi) et saute à cette adresse. Crash quasi-garanti. **Ne jamais faire `ret` sans avoir été `call`é** (ou en sauvegardant proprement la pile).

### Aperçu : pourquoi les buffer overflows existent ?

Quand tu fais `ret`, le CPU dépile une adresse et y saute. Si un attaquant arrive à **écraser cette adresse** sur la pile (par exemple via un débordement de buffer), il peut détourner le programme. C'est la base de l'exploitation par buffer overflow. **Hors scope de ce cours**, mais tu vois pourquoi la pile et les fonctions sont si critiques en sécurité.

## ❌ Erreur classique

```
Oublier ret à la fin de la fonction
→ Le CPU continue avec les instructions suivantes (ou des octets aléatoires).

Utiliser jmp au lieu de call
→ Pas de retour possible. La fonction continue dans la fonction suivante.

Ne pas respecter la convention d'appel
→ Tu mets l'arg dans rax au lieu de rdi → la fonction lit du garbage.

Modifier un registre callee-saved sans le sauvegarder
→ Quand tu reviens à l'appelant, son rbx (par ex) est cassé.

Appeler une fonction avec rsp désaligné
→ Pas grave pour tes propres fonctions, mais CRITIQUE pour la libc (ch. 21).

Mettre des labels en double : .fin dans deux fonctions
→ Si elles utilisent toutes deux .fin (label local), ça MARCHE car
   les labels locaux sont liés au label principal. C'est l'intérêt.

Confondre la valeur de retour avec un arg : "retourner dans rdi"
→ NON. Le retour est TOUJOURS dans rax.
```


## Exercices

**Guidé :** Crée une fonction `addition(a, b)` qui renvoie `a + b` dans `rax`. Appelle-la avec 30 et 12. Le résultat doit être `42` (à voir via le code de retour).

**Autonome :** Crée une fonction `est_pair(n)` qui renvoie `1` si `n` est pair, `0` sinon. **Indice :** `test rdi, 1` met `ZF=1` si le bit 0 est à 0 (donc pair).

**Défi :** Crée une fonction **récursive** `factorielle(n)` qui s'appelle elle-même. **Indice :** `factorielle(0) = 1`, sinon `factorielle(n) = n * factorielle(n-1)`. Attention à `push rdi` avant l'appel récursif.

## 🧩 Mini-projet (chapitre 19) — Bibliothèque mini

Crée `bib.asm` qui définit **quatre fonctions** et les utilise dans `_start` :

1. **`print_msg(adresse, longueur)`** : affiche un message.
2. **`addition(a, b)`** : renvoie `a + b`.
3. **`max(a, b)`** : renvoie le plus grand.
4. **`exit_success()`** : appelle `exit(0)`.

Dans `_start`, fais :

- Affiche un message d'accueil.
- Calcule et affiche `addition(15, 27)` (= 42).
- Calcule et affiche `max(8, 23)` (= 23).
- Appelle `exit_success()`.

> **Tu n'as pas encore d'afficheur d'entiers.** Pour ce mini-projet, mets juste un message statique "Resultat calcule" et vérifie les calculs dans GDB.

## ✅ Tu sais maintenant…

- Pourquoi on crée des **fonctions** : éviter la duplication
- Utiliser **`call`** pour appeler une fonction
- Utiliser **`ret`** pour en revenir
- Comment `call`/`ret` utilisent la pile sous le capot
- La **convention System V AMD64** : args dans `rdi, rsi, rdx, rcx, r8, r9`, retour dans `rax`
- La différence **caller-saved** / **callee-saved**
- Écrire une **fonction propre** avec préservation des registres
- Que tu peux **appeler des fonctions imbriquées** (récursivité comprise)

---
