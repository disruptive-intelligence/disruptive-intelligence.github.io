---
title: PARTIE VII — PILE ET FONCTIONS
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 7
chapters: 10
---

---


## Chapitre 18 — La pile avec `push`, `pop` et `rsp`

### Le minimum à savoir

#### C'est quoi, la pile ?

La **pile** (en anglais : *stack*) est une zone spéciale de la mémoire RAM. Elle fonctionne comme **une pile d'assiettes** :

```
        ┌─────────┐ ← sommet (la dernière déposée)
        │  100    │
        ├─────────┤
        │   42    │
        ├─────────┤
        │   17    │
        └─────────┘ ← base
```

- Tu peux **déposer** (push) une assiette sur le dessus.
- Tu peux **prendre** (pop) celle du dessus.
- Tu ne peux **pas** prendre celle du milieu sans enlever les autres.

C'est ce qu'on appelle une structure **LIFO** : *Last In, First Out* — la dernière entrée est la première à sortir.

#### Le registre `rsp` : le sommet de la pile

`rsp` (Stack Pointer) contient **l'adresse du sommet de la pile**. À chaque `push`, il **diminue** ; à chaque `pop`, il **augmente**.

> **Particularité de x86-64 :** la pile **grandit vers les adresses basses**. C'est contre-intuitif :
> - `push` fait `rsp -= 8` (descend en mémoire).
> - `pop` fait `rsp += 8` (remonte).

```
   Adresses hautes
        ↑
        │  ┌──────┐  ← rsp avant push
        │  │      │
        │  │      │
        │  ├──────┤  ← rsp après push (rsp - 8)
        │  │  42  │
        │  └──────┘
        ↓
   Adresses basses
```

#### `push` : empiler une valeur

```nasm
push rax        ; déposer rax sur la pile (rsp -= 8)
push 42         ; déposer la valeur 42
push qword [var] ; déposer le contenu de var
```

Effets :
1. `rsp = rsp - 8` (descend de 8 octets).
2. `[rsp] = valeur` (écrit la valeur au nouveau sommet).

#### `pop` : dépiler

```nasm
pop rax         ; prendre la valeur du sommet et la mettre dans rax (rsp += 8)
```

Effets :
1. `valeur = [rsp]` (lit le sommet).
2. `rsp = rsp + 8` (remonte).

#### Cas d'usage n°1 : sauvegarder temporairement

Tu as vu au chapitre 17 le pattern :

```nasm
push rcx        ; sauvegarder rcx
mov rax, 1      ; faire un syscall qui pourrait écraser rcx
mov rdi, 1
syscall
pop rcx         ; restaurer rcx
```

C'est l'utilisation la plus courante de la pile pour un débutant.

#### Cas d'usage n°2 : intervertir deux valeurs

```nasm
push rax        ; mémoriser rax
push rbx        ; mémoriser rbx
pop rax         ; rax reçoit l'ancien rbx
pop rbx         ; rbx reçoit l'ancien rax
```

Plus simple qu'un swap avec un troisième registre, et très pratique.

#### Voir la pile dans GDB

```
(gdb) x/10gx $rsp       ; afficher 10 qword à partir du sommet
```

Avec pwndbg, la pile est **affichée automatiquement** à chaque pas. Tu vois en direct ce qui s'empile/se dépile.

#### Exemple complet annoté

```nasm
; pile.asm — Démonstration de push/pop

section .text
global _start
_start:
    mov rax, 42
    mov rbx, 17

    push rax            ; pile : [42]              rsp -= 8
    push rbx            ; pile : [42, 17]          rsp -= 8

    pop rcx             ; rcx = 17  pile : [42]    rsp += 8
    pop rdx             ; rdx = 42  pile : [ ]     rsp += 8

    ; Vérification : rcx vaut 17, rdx vaut 42
    mov rdi, rdx        ; renvoyer 42 comme code retour
    mov rax, 60
    syscall
```

`./prog ; echo $?` → `42`. Lance dans GDB et observe `rsp` qui descend et remonte.

### Très utile en pratique

#### Règle d'or : push/pop équilibrés

Si tu fais `push rax`, tu **dois** faire un `pop` à un moment, sinon `rsp` est désaligné et la suite (notamment les `ret` qu'on verra au prochain chapitre) va planter.

> **Toujours autant de `push` que de `pop`.** Sinon, crash assuré.

#### Préserver plusieurs registres

```nasm
push rax
push rbx
push rcx
; ... code ...
pop rcx           ; dans l'ORDRE INVERSE
pop rbx
pop rax
```

LIFO oblige : on dépile dans l'**ordre inverse** d'empilement.

#### Ne pas modifier `rsp` à la main (sauf si tu sais)

Tu peux écrire `sub rsp, 16` pour réserver 16 octets sur la pile, ou `add rsp, 16` pour les libérer. C'est utile pour allouer des **variables locales** dans une fonction (chapitre 20). Mais **toujours par paire** : ce que tu réserves, tu dois le libérer avant de quitter.

#### `rsp` est sacré

Si tu fais `mov rsp, 0` n'importe où dans ton programme, **tu détruis la pile** et tu crashes instantanément. Ne touche jamais à `rsp` directement, sauf de manière équilibrée (`sub` puis `add`).

### Bonus

#### Pourquoi la pile grandit-elle "à l'envers" ?

Historique : à l'époque des systèmes avec peu de mémoire, on plaçait :
- Le code et les données initiales en **bas** de la mémoire.
- La pile en **haut**, qui grandissait vers le bas.

Comme ça, la pile et le tas pouvaient grandir **l'un vers l'autre**, maximisant l'utilisation de la mémoire disponible. Le sens "à l'envers" est resté par compatibilité.

#### Aperçu : la pile et les fonctions

Quand tu fais `call fonction` (chapitre suivant), le CPU **empile l'adresse de retour** sur la pile, puis saute. C'est pour ça qu'on doit comprendre la pile **avant** les fonctions.

#### Alignement à 16 octets

Pour le **chapitre 21** (appel à la libc), il faudra que `rsp` soit aligné sur 16 octets juste avant un `call`. Ça veut dire que `rsp` doit se terminer par `0` en hexa (donc divisible par 16). Sinon, certaines fonctions C plantent. Détails et trucs au chapitre 21.

### ❌ Erreur classique

```
Déséquilibrer push et pop
→ Crash à coup sûr, surtout si la fonction se termine par ret.

Dépiler dans le mauvais ordre
→ Les valeurs reviennent dans les mauvais registres.
   Exemple : push rax / push rbx
            pop rax / pop rbx  ← inversé ! rax reçoit l'ancien rbx.

Modifier rsp à la main de manière non équilibrée
→ La pile est corrompue, le programme crashe.

Croire que push fait rsp + 8
→ NON. push fait rsp - 8 (la pile descend).

Oublier que push écrit à la mémoire pointée par rsp
→ Ce n'est pas magique : la valeur va vraiment en RAM.

Croire que pop "efface" la valeur de la pile
→ Non. La valeur reste en mémoire, mais rsp avance, donc on l'ignore.
   Un nouveau push écrasera ces octets.
```

### Exercices

**Guidé :** Recopie et exécute `pile.asm` ci-dessus. Lance-le dans GDB. À chaque `push`/`pop`, regarde `rsp` (avec `print /x $rsp`) et le contenu de la pile (`x/4gx $rsp`).

**Autonome :** Écris un programme qui empile **3 valeurs** (`100`, `200`, `300`), puis les dépile dans `rax`, `rbx`, `rcx`. Quel registre contiendra quoi ?

> **Réponse :** dans l'ordre LIFO : `rax = 300`, `rbx = 200`, `rcx = 100`.

**Défi :** Sans utiliser de troisième registre, **inverse 4 valeurs** : empile `1, 2, 3, 4`, puis dépile dans `r12, r13, r14, r15`. Quelle sera la valeur de chaque registre ?

### ✅ Tu sais maintenant…

- Ce qu'est la **pile** (LIFO) et comment elle vit en mémoire
- Le rôle du registre **`rsp`** (pointeur de pile)
- Empiler avec **`push`** (et `rsp -= 8`)
- Dépiler avec **`pop`** (et `rsp += 8`)
- La règle des **push/pop équilibrés**
- Sauvegarder temporairement un registre
- Que la pile grandit vers les **adresses basses**
- Observer la pile dans GDB

---


## Chapitre 19 — Fonctions avec `call` et `ret`

### Le minimum à savoir

#### Pourquoi des fonctions ?

Jusqu'ici, tu écris des programmes "tout en un bloc". Mais dès que tu fais quelque chose deux fois (afficher un message, calculer une somme…), tu **copies-colles**. Pénible et fragile.

Les **fonctions** sont des blocs de code **réutilisables**, qu'on appelle à plusieurs endroits. Comme `def` en Python ou les fonctions Bash.

> **À retenir :** une fonction en ASM, c'est juste un **label** où tu sautes, et duquel tu reviens.

#### `call` et `ret` : aller et revenir

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

#### Une première fonction

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

#### La convention d'appel System V AMD64

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

#### Fonction `carre(x)` qui renvoie `x * x`

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

#### Caller-saved et callee-saved

C'est **le concept** à comprendre pour les fonctions. Quand tu appelles une fonction, certains registres peuvent être **détruits** par elle, d'autres pas :

| Catégorie | Registres | Qui doit sauvegarder ? |
|-----------|-----------|------------------------|
| **Caller-saved** | `rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11` | L'**appelant** (toi) avant `call` |
| **Callee-saved** | `rbx, rbp, r12, r13, r14, r15` | La **fonction** elle-même, si elle les modifie |

**Traduction pratique :**

- Si tu utilises `rcx` et tu appelles une fonction, **suppose qu'elle a détruit `rcx`**. Sauvegarde-le si tu veux le récupérer (`push rcx` / `pop rcx`).
- Si **tu écris** une fonction qui utilise `rbx`, **tu dois le préserver** (push au début, pop à la fin).

> **Pourquoi ?** C'est un **contrat** entre fonctions. Ça permet à n'importe quelle fonction d'appeler n'importe quelle autre sans tout casser.

#### Squelette d'une fonction propre

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

#### Exemple : fonction `max(a, b)`

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

#### Appels en cascade

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

### Très utile en pratique

#### Fonction `print_msg` réutilisable

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

#### `jmp` vs `call`

- **`jmp fn`** : saute à `fn`, mais **sans retour possible**.
- **`call fn`** : saute à `fn`, **et `ret` reviendra ici**.

Utilise `call` pour les fonctions, `jmp` pour les sauts internes (boucles, if/else).

### Bonus

#### `ret` sans `call` ?

Si tu fais `ret` sans `call` préalable, le CPU dépile **ce qu'il y a au sommet de la pile** (peut-être n'importe quoi) et saute à cette adresse. Crash quasi-garanti. **Ne jamais faire `ret` sans avoir été `call`é** (ou en sauvegardant proprement la pile).

#### Aperçu : pourquoi les buffer overflows existent ?

Quand tu fais `ret`, le CPU dépile une adresse et y saute. Si un attaquant arrive à **écraser cette adresse** sur la pile (par exemple via un débordement de buffer), il peut détourner le programme. C'est la base de l'exploitation par buffer overflow. **Hors scope de ce cours**, mais tu vois pourquoi la pile et les fonctions sont si critiques en sécurité.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée une fonction `addition(a, b)` qui renvoie `a + b` dans `rax`. Appelle-la avec 30 et 12. Le résultat doit être `42` (à voir via le code de retour).

**Autonome :** Crée une fonction `est_pair(n)` qui renvoie `1` si `n` est pair, `0` sinon. **Indice :** `test rdi, 1` met `ZF=1` si le bit 0 est à 0 (donc pair).

**Défi :** Crée une fonction **récursive** `factorielle(n)` qui s'appelle elle-même. **Indice :** `factorielle(0) = 1`, sinon `factorielle(n) = n * factorielle(n-1)`. Attention à `push rdi` avant l'appel récursif.

### 🧩 Mini-projet (chapitre 19) — Bibliothèque mini

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

### ✅ Tu sais maintenant…

- Pourquoi on crée des **fonctions** : éviter la duplication
- Utiliser **`call`** pour appeler une fonction
- Utiliser **`ret`** pour en revenir
- Comment `call`/`ret` utilisent la pile sous le capot
- La **convention System V AMD64** : args dans `rdi, rsi, rdx, rcx, r8, r9`, retour dans `rax`
- La différence **caller-saved** / **callee-saved**
- Écrire une **fonction propre** avec préservation des registres
- Que tu peux **appeler des fonctions imbriquées** (récursivité comprise)

---


## Chapitre 20 — Stack frame, `rbp` et variables locales

### Le minimum à savoir

#### Pourquoi des variables locales ?

Une fonction complexe a besoin de plus de "place de travail" que les 6 registres d'arguments. Et tu ne veux **pas** utiliser `.data` (qui est partagé, non-récursif). Solution : **allouer de la place sur la pile**, valable seulement pendant la durée de la fonction.

#### Le stack frame : l'espace de travail d'une fonction

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

#### Le prologue et l'épilogue : le squelette standard

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

#### Pourquoi `[rbp - 8]` et pas `[rbp + 8]` ?

Parce que la pile **descend**. Les variables locales sont **au-dessous** de `rbp` (vers les adresses basses), donc avec un décalage **négatif**.

| Décalage | Contenu |
|----------|---------|
| `[rbp + 16]` et +  | 7ème argument, 8ème, etc. (rares) |
| `[rbp + 8]` | adresse de retour (empilée par `call`) |
| `[rbp]` | ancien rbp |
| `[rbp - 8]` | **1ère variable locale** |
| `[rbp - 16]` | 2ème variable locale |
| `[rbp - 24]` | 3ème variable locale |

#### Exemple complet : fonction avec locales

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

#### Stocker les arguments en locales : pourquoi ?

Tu remarques qu'on a copié `rdi` et `rsi` dans `[rbp - 8]` et `[rbp - 16]`. Pourquoi ne pas les utiliser directement depuis `rdi`/`rsi` ?

Plusieurs raisons (et c'est ce que fait gcc en `-O0`) :
- Si on **appelle une autre fonction**, `rdi`/`rsi` sont caller-saved → écrasés.
- Si on a besoin des arguments **plus tard** dans la fonction, c'est plus sûr.
- Ça rend la fonction plus **lisible** à debug.

En `-O2` (avec optimisations), gcc évite cette copie inutile. Mais en `-O0` (sans), c'est systématique.

### Très utile en pratique

#### Reconnaître le prologue/épilogue en reverse

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

#### L'instruction `leave`

`leave` est un raccourci pour `mov rsp, rbp ; pop rbp`. Tu verras donc souvent :

```
leave
ret
```

= épilogue compact. C'est exactement la même chose, juste un peu plus court.

#### Combien d'espace réserver ?

Multiplie `nombre de locales × 8` (pour des qword) et arrondis à 16 si tu vas appeler une autre fonction (alignement, voir ch. 21).

```nasm
; 3 variables locales qword
sub rsp, 24            ; non aligné sur 16
sub rsp, 32            ; aligné sur 16 → préférable
```

#### Plus de 6 arguments : sur la pile

Si une fonction a 8 arguments, les 6 premiers vont dans `rdi, rsi, rdx, rcx, r8, r9`, et les 7ème et 8ème sont **empilés par l'appelant** avant le `call`. Tu les lis avec `[rbp + 16]` et `[rbp + 24]`. Cas rare en pédagogie débutante.

### Bonus

#### Variables locales : taille fine

Tu peux mélanger des tailles :

```nasm
sub rsp, 16
mov byte  [rbp - 1], 'A'           ; 1 octet
mov dword [rbp - 8], 12345         ; 4 octets
mov qword [rbp - 16], 999999       ; 8 octets
```

En pratique, en pédagogie, **alloue tout en qword** : c'est plus simple à raisonner.

#### Pourquoi rbp ?

Sans `rbp`, tu devrais référencer tes locales avec `rsp`, qui **bouge** (à chaque `push`/`pop`). `rbp` reste **fixe** pendant toute la fonction, donc `[rbp - 8]` désigne **toujours** la même locale.

En `-O1` ou `-O2`, gcc peut omettre `rbp` (`-fomit-frame-pointer`). Le code devient plus dense, mais **plus dur à lire en reverse**. C'est une des raisons pour lesquelles le reverse est plus simple sur du `-O0`.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Recopie et compile l'exemple `somme_carres` ci-dessus. Lance-le dans GDB, mets un breakpoint sur `somme_carres`, et observe `rbp` et `rsp` après le prologue. Affiche les locales avec `x/2gx $rbp - 16`.

**Autonome :** Réécris la fonction `factorielle(n)` du chapitre 19 en utilisant un stack frame propre avec **`push rbp / mov rbp, rsp` / `leave / ret`**. Stocke `n` dans une locale `[rbp - 8]`.

**Défi :** Crée une fonction `moyenne_quatre(a, b, c, d)` qui prend 4 arguments (tous dans des registres), les stocke en 4 locales, calcule la somme, divise par 4, et renvoie le résultat. Vérifie `moyenne_quatre(10, 20, 30, 40) = 25`.

### 🧩 Mini-projet (chapitres 18-20) — Mini-application structurée

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

### ✅ Tu sais maintenant…

- Construire un **stack frame** : prologue (`push rbp ; mov rbp, rsp ; sub rsp, N`)
- Le terminer : épilogue (`mov rsp, rbp ; pop rbp ; ret`) ou `leave / ret`
- Allouer des **variables locales** sur la pile
- Y accéder avec **`[rbp - offset]`**
- Distinguer **locale** (`[rbp - N]`) et **adresse de retour** (`[rbp + 8]`)
- Reconnaître un **prologue de fonction** dans du code désassemblé
- L'instruction **`leave`** comme raccourci

À partir d'ici, tu maîtrises **TOUT le langage de base** de l'assembleur x86-64. Les chapitres suivants te montrent comment l'utiliser avec C et comment **lire** les programmes compilés.

---

### 🚩 Checkpoint — Fin de la Partie VII

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
