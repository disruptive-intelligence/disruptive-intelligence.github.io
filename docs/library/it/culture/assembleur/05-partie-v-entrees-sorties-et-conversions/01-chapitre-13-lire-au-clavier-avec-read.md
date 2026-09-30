---
title: Chapitre 13 — Lire au clavier avec read
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie V — Entrées, sorties ET conversions
  - index.md
---

## Le minimum à savoir

### Le syscall `read` (numéro 0)

Symétrique de `write`, le syscall **`read`** lit des octets depuis un file descriptor (généralement le clavier).

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro de syscall | `rax` | `0` (= read) |
| file descriptor | `rdi` | `0` (= stdin) |
| adresse du buffer | `rsi` | `buffer` |
| nombre max d'octets | `rdx` | `64` |

Après l'appel :

- **`rax`** contient le **nombre d'octets effectivement lus** (ou un nombre négatif en cas d'erreur).

### Préparer un buffer dans `.bss`

```nasm
section .bss
    buffer  resb 64       ; 64 octets vides pour stocker la saisie
```


### Lire et réafficher : ton premier programme interactif

Crée `echo.asm` :

```nasm
; echo.asm — Lit une ligne et la réaffiche

section .data
    prompt    db "Tape quelque chose : ", 0
    prompt_l  equ $ - prompt - 1     ; -1 pour ne pas inclure le 0 final

section .bss
    buffer    resb 64
    nb_lus    resq 1

section .text
global _start
_start:
    ; ─── Afficher le prompt ───
    mov rax, 1                ; write
    mov rdi, 1                ; stdout
    mov rsi, prompt
    mov rdx, prompt_l
    syscall

    ; ─── Lire la saisie ───
    mov rax, 0                ; read
    mov rdi, 0                ; stdin
    mov rsi, buffer
    mov rdx, 64               ; max 64 octets
    syscall

    ; rax contient maintenant le nombre d'octets lus
    mov [nb_lus], rax         ; on le mémorise

    ; ─── Réafficher ───
    mov rax, 1                ; write
    mov rdi, 1                ; stdout
    mov rsi, buffer
    mov rdx, [nb_lus]         ; on réutilise le nombre d'octets lus
    syscall

    ; ─── Quitter ───
    mov rax, 60
    mov rdi, 0
    syscall
```


Exécution :

```
$ ./echo
Tape quelque chose : Bonjour
Bonjour
```


> **Important :** quand tu tapes `Bonjour` + Entrée, le **retour ligne fait partie** des octets lus. C'est pour ça que la sortie se met à la ligne automatiquement.

### `rax` après `read` : c'est crucial

Tu **dois** récupérer `rax` après `read` parce que :

- Tu ne sais pas combien l'utilisateur a tapé.
- Tu vas vouloir afficher exactement cette quantité.
- Si tu mets `rdx = 64` pour le `write`, tu afficheras des **octets garbage** en plus de la saisie.

```nasm
mov rax, 0
mov rdi, 0
mov rsi, buffer
mov rdx, 64
syscall                ; rax = nombre lus (typiquement entre 1 et 64)

mov [nb_lus], rax      ; mémoriser pour plus tard
```


### Le retour ligne est lu

Si tu tapes `abc` + Entrée, le buffer contient `'a'`, `'b'`, `'c'`, `'\n'` (4 octets). Si tu veux **enlever** le retour ligne, il faut soustraire 1 à `nb_lus` ou modifier le buffer. Ça viendra avec les boucles (chapitre 17).

## Très utile en pratique

### Que faire si l'utilisateur ne tape rien ?

S'il appuie juste sur Entrée, `read` lit 1 octet (le `\n`) et retourne 1. Si stdin est fermé (Ctrl+D), `read` retourne 0. Si une erreur survient, `read` retourne une valeur **négative** (par exemple `-1`). On apprendra à tester ça au chapitre 16.

### Buffer trop petit ?

Si tu réserves 10 octets et que l'utilisateur tape 20 caractères, **seulement 10** seront lus. Les autres restent dans le tampon de stdin et seront lus à la prochaine lecture. Pas de crash, mais comportement à connaître.

### Buffer trop grand ?

Si tu réserves 1000 octets et que l'utilisateur tape "abc", `read` lit juste 4 octets (`abc\n`). `rax` te dit combien. **Aucun problème.**

## Bonus

### Lire un seul caractère

```nasm
mov rax, 0
mov rdi, 0
mov rsi, buffer
mov rdx, 1            ; max 1 octet
syscall
```


Pratique pour des menus simples (l'utilisateur tape `1`, `2`, `3`…).

### Lire silencieusement (ex: mots de passe)

Pas trivial en assembleur pur — il faut utiliser `tcsetattr` pour désactiver l'écho. Hors scope de ce cours, mais sache que c'est possible.

## ❌ Erreur classique

```
Oublier de récupérer rax après read
→ Tu ne sais pas combien d'octets sont valides dans le buffer.

Mettre rdx fixe pour le write au lieu de [nb_lus]
→ Tu affiches du garbage en plus de la saisie.

Buffer trop petit ET ne pas tester si nb_lus >= taille_max
→ Pas grave dans ce cours, mais à savoir pour la suite.

Lire avant d'avoir affiché le prompt
→ L'utilisateur ne sait pas qu'on attend une saisie. Toujours prompt → read.

Croire que read renvoie la chaîne directement
→ NON. Read remplit le buffer, et rax contient le nombre d'octets lus.

Oublier que '\n' est lu
→ Si l'utilisateur tape "abc", nb_lus = 4 (abc + \n).
```


## Exercices

**Guidé :** Recopie et exécute `echo.asm` ci-dessus. Vérifie que ce que tu tapes est bien réaffiché.

**Autonome :** Modifie `echo.asm` pour afficher d'abord `"Tu as ecrit : "` avant la saisie réaffichée.

**Défi :** Crée un programme qui affiche **deux fois** ce que l'utilisateur a tapé (en gros : `echo echo`).

## 🧩 Mini-projet (chapitre 13) — Mini-shell d'accueil

Crée `accueil.asm` qui :

1. Affiche `"Quel est ton prenom ? "` (sans retour ligne après).
2. Lit la saisie utilisateur.
3. Affiche `"Bonjour, "`.
4. Réaffiche le prénom saisi.

Exécution attendue :

```
$ ./accueil
Quel est ton prenom ? Alice
Bonjour, Alice
```


> **Note :** le retour ligne après "Alice" vient du `\n` qui a été lu avec la saisie. C'est OK.

## ✅ Tu sais maintenant…

- Utiliser le syscall **`read`** (n°0)
- La symétrie **`write`** ↔ **`read`** (même conventions)
- Le rôle du **file descriptor 0** (stdin)
- Pourquoi récupérer **`rax`** après `read`
- Préparer un **buffer dans `.bss`**
- Que le **retour ligne** fait partie de ce qui est lu
- Écrire un premier programme **interactif**

---
