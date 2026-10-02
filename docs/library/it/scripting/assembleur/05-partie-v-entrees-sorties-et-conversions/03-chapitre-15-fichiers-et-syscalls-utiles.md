---
title: Chapitre 15 — Fichiers et syscalls utiles
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie V — Entrées, sorties et conversions
  - index.md
---

## Le minimum à savoir

### Au-delà de stdin/stdout

Tu sais lire le clavier et écrire à l'écran. Mais comment **lire un fichier** ou **écrire dans un fichier** ? Réponse : avec d'autres syscalls.

### Les 5 syscalls de gestion de fichiers

| Syscall | Numéro | Rôle |
|---------|--------|------|
| **`open`** | 2 | Ouvre un fichier, renvoie un file descriptor (fd) |
| **`read`** | 0 | Lit depuis un fd |
| **`write`** | 1 | Écrit dans un fd |
| **`close`** | 3 | Ferme un fd |
| **`lseek`** | 8 | Déplace le curseur dans un fichier |

### Le syscall `open` (numéro 2)

> **Note :** dans les programmes Linux modernes et dans la libc d'aujourd'hui, on rencontre **souvent `openat`** (syscall n°257) plutôt que `open` — notamment dans les programmes compilés avec une libc récente, où c'est devenu la norme. Le principe reste identique : obtenir un file descriptor pour un fichier. `openat` accepte juste un répertoire de base en argument supplémentaire. Pour ce cours, on reste sur `open` qui est plus simple à manipuler. **En reverse engineering moderne, sois prêt à croiser `openat` plus souvent que `open`.**

Arguments :

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro | `rax` | `2` |
| chemin du fichier | `rdi` | adresse de la chaîne du chemin (terminée par 0) |
| flags (mode d'ouverture) | `rsi` | voir tableau ci-dessous |
| permissions (si création) | `rdx` | `420` (= `0o644` en décimal) typiquement |

Valeurs courantes de `rsi` (flags) :

| Flag | Valeur | Effet |
|------|--------|-------|
| `O_RDONLY` | 0 | Lecture seule |
| `O_WRONLY` | 1 | Écriture seule |
| `O_RDWR` | 2 | Lecture/écriture |
| `O_CREAT` | 0x40 (= 64) | Créer si n'existe pas (combiner avec autre flag) |
| `O_TRUNC` | 0x200 (= 512) | Tronquer (vider) si existe |
| `O_APPEND` | 0x400 (= 1024) | Ajouter à la fin |

On les **combine avec OR bit-à-bit** (que NASM accepte avec `|`) :

```nasm
mov rsi, 1 | 64 | 512    ; O_WRONLY | O_CREAT | O_TRUNC
```


### `open` renvoie un fd

Après `open`, `rax` contient :

- Un **fd positif** (un entier ≥ 3) si tout s'est bien passé. **Mémorise-le**.
- Une **valeur négative** si erreur (`-1`, `-2`, etc.).

### Lire un fichier complet : `cat.asm`

```nasm
; cat.asm — Mini-cat : lit un fichier (chemin codé en dur) et l'affiche

section .data
    chemin db "/etc/hostname", 0

section .bss
    fd     resq 1
    buffer resb 1024

section .text
global _start
_start:
    ; ─── open(chemin, O_RDONLY) ───
    mov rax, 2              ; syscall open
    mov rdi, chemin
    mov rsi, 0              ; O_RDONLY
    mov rdx, 0
    syscall

    mov [fd], rax           ; mémoriser le fd

    ; ─── read(fd, buffer, 1024) ───
    mov rax, 0              ; syscall read
    mov rdi, [fd]
    mov rsi, buffer
    mov rdx, 1024
    syscall

    ; rax = nombre d'octets lus
    mov r12, rax            ; on sauvegarde dans r12

    ; ─── write(stdout, buffer, r12) ───
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, r12
    syscall

    ; ─── close(fd) ───
    mov rax, 3
    mov rdi, [fd]
    syscall

    ; ─── exit(0) ───
    mov rax, 60
    mov rdi, 0
    syscall
```


Exécute :

```
$ ./cat
mon-pc
```


🎉 **Tu viens de coder un mini-`cat` qui lit un vrai fichier.**

### Écrire dans un fichier

Même principe, avec `O_WRONLY | O_CREAT | O_TRUNC` et un mode (permissions Unix `0644`, soit `420` en décimal) :

```nasm
section .data
    nom     db "sortie.txt", 0
    contenu db "Salut depuis l'assembleur !", 10
    contenu_l equ $ - contenu

section .bss
    fd resq 1

section .text
global _start
_start:
    ; open(nom, O_WRONLY|O_CREAT|O_TRUNC, 0644)
    mov rax, 2
    mov rdi, nom
    mov rsi, 1 | 64 | 512
    mov rdx, 420             ; permissions 0644 en décimal (rw-r--r--)
    syscall
    mov [fd], rax

    ; write(fd, contenu, len)
    mov rax, 1
    mov rdi, [fd]
    mov rsi, contenu
    mov rdx, contenu_l
    syscall

    ; close(fd)
    mov rax, 3
    mov rdi, [fd]
    syscall

    ; exit(0)
    mov rax, 60
    mov rdi, 0
    syscall
```


Après exécution :

```
$ cat sortie.txt
Salut depuis l'assembleur !
```


### Toujours fermer ce qu'on a ouvert

Comme en Python (`f.close()`), on **doit** fermer ce qu'on ouvre. Sinon, fuite de descripteurs (le système en a un nombre limité).

## Très utile en pratique

### Détecter une erreur de syscall

Tous les syscalls renvoient :

- Une **valeur positive ou zéro** en cas de succès (selon le syscall).
- Une **valeur négative** en cas d'erreur (entre -1 et environ -4095).

```nasm
mov rax, 2          ; open
mov rdi, chemin
mov rsi, 0
syscall

cmp rax, 0
jl erreur           ; saut si rax < 0 (chapitre 16)
```


Pour tester ça proprement, il faut connaître les sauts conditionnels (chapitre suivant).

### Buffers et lecture par blocs

Si tu lis un fichier plus grand que ton buffer, **un seul `read` ne suffira pas**. Il faut **boucler** :

```
tant que read renvoie > 0 :
    écrire ce qu'on a lu
    relancer read
```


C'est exactement ce que fait `cat`. On le fera proprement après les boucles (ch. 17).

## Bonus

### Le syscall `lseek` (numéro 8)

`lseek` permet de **déplacer le curseur** dans un fichier (utile pour relire le début ou sauter une portion).

| Argument | Registre |
|----------|----------|
| numéro | `rax = 8` |
| fd | `rdi` |
| décalage | `rsi` |
| origine | `rdx` (0 = début, 1 = position actuelle, 2 = fin) |

### Erreurs typiques de `open`

| Code (valeur) | Signification |
|---------------|---------------|
| `-2` | Fichier introuvable (ENOENT) |
| `-13` | Permission refusée (EACCES) |
| `-17` | Fichier existe déjà (EEXIST), avec O_CREAT \| O_EXCL |

## ❌ Erreur classique

```
Oublier le 0 final du chemin
→ open() reçoit une chaîne corrompue. Erreur de fichier introuvable.

Oublier de fermer un fichier
→ Fuite. Pas grave pour un petit programme, mais mauvaise habitude.

Ignorer la valeur de retour
→ Tu manipules un fd invalide. Comportement indéfini.

Mauvaises permissions (rdx mal mis)
→ Le fichier sera créé sans droits d'écriture. Embêtant.

Oublier O_TRUNC quand on écrit dans un fichier existant
→ Le nouveau contenu se mélange à l'ancien.

Ne pas mémoriser le fd dans une variable
→ Si tu fais d'autres opérations, rax aura changé. Stocke-le.
```


## Exercices

**Guidé :** Crée `cat.asm` comme ci-dessus, mais en lisant un fichier que tu crées avec `echo "Bonjour" > test.txt`. Adapte le chemin dans le `.asm`.

**Autonome :** Écris un programme qui crée un fichier `salut.txt` contenant la chaîne `"Salut\n"`. Vérifie avec `cat salut.txt` que ça fonctionne.

**Défi :** Écris un programme qui :

1. Ouvre `test.txt` en lecture.
2. Lit son contenu (jusqu'à 256 octets) dans un buffer.
3. **Écrit ce contenu** dans `copie.txt`.
4. Ferme les deux fichiers.

C'est l'équivalent de `cp test.txt copie.txt` (pour les petits fichiers).

## 🧩 Mini-projet (chapitres 13-15) — Mini-cat avec saisie

Crée `cat_input.asm` qui :

1. Demande à l'utilisateur de taper du texte.
2. Le lit avec `read`.
3. L'écrit dans un fichier nommé `sortie.txt`.
4. Affiche un message de confirmation à l'écran.

Exemple :

```
$ ./cat_input
Tape un texte : Bonjour le monde
Texte sauvegarde dans sortie.txt
$ cat sortie.txt
Bonjour le monde
```


> **Limitation :** ne gère qu'une seule ligne (jusqu'à 1024 octets). C'est OK.

## ✅ Tu sais maintenant…

- Ouvrir un fichier avec **`open`** (numéro 2)
- Comprendre les **flags** : `O_RDONLY`, `O_WRONLY`, `O_CREAT`, `O_TRUNC`, etc.
- Récupérer un **file descriptor** dans `rax`
- Le **mémoriser** dans une variable
- Lire et écrire dans un fichier via `read`/`write` avec ce fd
- **Fermer** proprement avec `close` (numéro 3)
- Détecter (à venir) une erreur via une **valeur négative**
- Coder un **mini-`cat`** en assembleur pur

---

## 🚩 Checkpoint — Fin de la Partie V

À ce stade, tu sais écrire un vrai programme interactif. Vérifie que tu peux :

- [ ] Lire une saisie utilisateur avec `read` et récupérer le nombre d'octets lus.
- [ ] Convertir un caractère ASCII en chiffre (et vice-versa).
- [ ] Ouvrir, lire, écrire et fermer un fichier avec `open`, `read`, `write`, `close`.
- [ ] Comprendre pourquoi `'5'` ≠ `5`.
- [ ] Mémoriser un file descriptor dans une variable `.bss`.
- [ ] Identifier qu'un syscall a échoué (valeur négative dans `rax`).

**Si tu sais faire tout ça, tu maîtrises les I/O bas niveau de Linux.** La suite (logique, fonctions, reverse) s'appuie là-dessus.

---
