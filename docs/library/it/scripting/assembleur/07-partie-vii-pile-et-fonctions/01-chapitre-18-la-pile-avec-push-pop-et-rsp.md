---
title: Chapitre 18 — La pile avec push, pop et rsp
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VII — Pile et fonctions
  - index.md
---

## Le minimum à savoir

### C'est quoi, la pile ?

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

### Le registre `rsp` : le sommet de la pile

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


### `push` : empiler une valeur

```nasm
push rax        ; déposer rax sur la pile (rsp -= 8)
push 42         ; déposer la valeur 42
push qword [var] ; déposer le contenu de var
```


Effets :

1. `rsp = rsp - 8` (descend de 8 octets).
2. `[rsp] = valeur` (écrit la valeur au nouveau sommet).

### `pop` : dépiler

```nasm
pop rax         ; prendre la valeur du sommet et la mettre dans rax (rsp += 8)
```


Effets :

1. `valeur = [rsp]` (lit le sommet).
2. `rsp = rsp + 8` (remonte).

### Cas d'usage n°1 : sauvegarder temporairement

Tu as vu au chapitre 17 le pattern :

```nasm
push rcx        ; sauvegarder rcx
mov rax, 1      ; faire un syscall qui pourrait écraser rcx
mov rdi, 1
syscall
pop rcx         ; restaurer rcx
```


C'est l'utilisation la plus courante de la pile pour un débutant.

### Cas d'usage n°2 : intervertir deux valeurs

```nasm
push rax        ; mémoriser rax
push rbx        ; mémoriser rbx
pop rax         ; rax reçoit l'ancien rbx
pop rbx         ; rbx reçoit l'ancien rax
```


Plus simple qu'un swap avec un troisième registre, et très pratique.

### Voir la pile dans GDB

```
(gdb) x/10gx $rsp       ; afficher 10 qword à partir du sommet
```


Avec pwndbg, la pile est **affichée automatiquement** à chaque pas. Tu vois en direct ce qui s'empile/se dépile.

### Exemple complet annoté

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

## Très utile en pratique

### Règle d'or : push/pop équilibrés

Si tu fais `push rax`, tu **dois** faire un `pop` à un moment, sinon `rsp` est désaligné et la suite (notamment les `ret` qu'on verra au prochain chapitre) va planter.

> **Toujours autant de `push` que de `pop`.** Sinon, crash assuré.

### Préserver plusieurs registres

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

### Ne pas modifier `rsp` à la main (sauf si tu sais)

Tu peux écrire `sub rsp, 16` pour réserver 16 octets sur la pile, ou `add rsp, 16` pour les libérer. C'est utile pour allouer des **variables locales** dans une fonction (chapitre 20). Mais **toujours par paire** : ce que tu réserves, tu dois le libérer avant de quitter.

### `rsp` est sacré

Si tu fais `mov rsp, 0` n'importe où dans ton programme, **tu détruis la pile** et tu crashes instantanément. Ne touche jamais à `rsp` directement, sauf de manière équilibrée (`sub` puis `add`).

## Bonus

### Pourquoi la pile grandit-elle "à l'envers" ?

Historique : à l'époque des systèmes avec peu de mémoire, on plaçait :

- Le code et les données initiales en **bas** de la mémoire.
- La pile en **haut**, qui grandissait vers le bas.

Comme ça, la pile et le tas pouvaient grandir **l'un vers l'autre**, maximisant l'utilisation de la mémoire disponible. Le sens "à l'envers" est resté par compatibilité.

### Aperçu : la pile et les fonctions

Quand tu fais `call fonction` (chapitre suivant), le CPU **empile l'adresse de retour** sur la pile, puis saute. C'est pour ça qu'on doit comprendre la pile **avant** les fonctions.

### Alignement à 16 octets

Pour le **chapitre 21** (appel à la libc), il faudra que `rsp` soit aligné sur 16 octets juste avant un `call`. Ça veut dire que `rsp` doit se terminer par `0` en hexa (donc divisible par 16). Sinon, certaines fonctions C plantent. Détails et trucs au chapitre 21.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Recopie et exécute `pile.asm` ci-dessus. Lance-le dans GDB. À chaque `push`/`pop`, regarde `rsp` (avec `print /x $rsp`) et le contenu de la pile (`x/4gx $rsp`).

**Autonome :** Écris un programme qui empile **3 valeurs** (`100`, `200`, `300`), puis les dépile dans `rax`, `rbx`, `rcx`. Quel registre contiendra quoi ?

> **Réponse :** dans l'ordre LIFO : `rax = 300`, `rbx = 200`, `rcx = 100`.

**Défi :** Sans utiliser de troisième registre, **inverse 4 valeurs** : empile `1, 2, 3, 4`, puis dépile dans `r12, r13, r14, r15`. Quelle sera la valeur de chaque registre ?

## ✅ Tu sais maintenant…

- Ce qu'est la **pile** (LIFO) et comment elle vit en mémoire
- Le rôle du registre **`rsp`** (pointeur de pile)
- Empiler avec **`push`** (et `rsp -= 8`)
- Dépiler avec **`pop`** (et `rsp += 8`)
- La règle des **push/pop équilibrés**
- Sauvegarder temporairement un registre
- Que la pile grandit vers les **adresses basses**
- Observer la pile dans GDB

---
