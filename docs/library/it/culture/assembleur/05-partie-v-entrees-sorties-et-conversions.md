---
title: PARTIE V — ENTRÉES, SORTIES ET CONVERSIONS
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 5
chapters: 10
---

---


## Chapitre 13 — Lire au clavier avec `read`

### Le minimum à savoir

#### Le syscall `read` (numéro 0)

Symétrique de `write`, le syscall **`read`** lit des octets depuis un file descriptor (généralement le clavier).

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro de syscall | `rax` | `0` (= read) |
| file descriptor | `rdi` | `0` (= stdin) |
| adresse du buffer | `rsi` | `buffer` |
| nombre max d'octets | `rdx` | `64` |

Après l'appel :
- **`rax`** contient le **nombre d'octets effectivement lus** (ou un nombre négatif en cas d'erreur).

#### Préparer un buffer dans `.bss`

```nasm
section .bss
    buffer  resb 64       ; 64 octets vides pour stocker la saisie
```

#### Lire et réafficher : ton premier programme interactif

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

#### `rax` après `read` : c'est crucial

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

#### Le retour ligne est lu

Si tu tapes `abc` + Entrée, le buffer contient `'a'`, `'b'`, `'c'`, `'\n'` (4 octets). Si tu veux **enlever** le retour ligne, il faut soustraire 1 à `nb_lus` ou modifier le buffer. Ça viendra avec les boucles (chapitre 17).

### Très utile en pratique

#### Que faire si l'utilisateur ne tape rien ?

S'il appuie juste sur Entrée, `read` lit 1 octet (le `\n`) et retourne 1. Si stdin est fermé (Ctrl+D), `read` retourne 0. Si une erreur survient, `read` retourne une valeur **négative** (par exemple `-1`). On apprendra à tester ça au chapitre 16.

#### Buffer trop petit ?

Si tu réserves 10 octets et que l'utilisateur tape 20 caractères, **seulement 10** seront lus. Les autres restent dans le tampon de stdin et seront lus à la prochaine lecture. Pas de crash, mais comportement à connaître.

#### Buffer trop grand ?

Si tu réserves 1000 octets et que l'utilisateur tape "abc", `read` lit juste 4 octets (`abc\n`). `rax` te dit combien. **Aucun problème.**

### Bonus

#### Lire un seul caractère

```nasm
mov rax, 0
mov rdi, 0
mov rsi, buffer
mov rdx, 1            ; max 1 octet
syscall
```

Pratique pour des menus simples (l'utilisateur tape `1`, `2`, `3`…).

#### Lire silencieusement (ex: mots de passe)

Pas trivial en assembleur pur — il faut utiliser `tcsetattr` pour désactiver l'écho. Hors scope de ce cours, mais sache que c'est possible.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Recopie et exécute `echo.asm` ci-dessus. Vérifie que ce que tu tapes est bien réaffiché.

**Autonome :** Modifie `echo.asm` pour afficher d'abord `"Tu as ecrit : "` avant la saisie réaffichée.

**Défi :** Crée un programme qui affiche **deux fois** ce que l'utilisateur a tapé (en gros : `echo echo`).

### 🧩 Mini-projet (chapitre 13) — Mini-shell d'accueil

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

### ✅ Tu sais maintenant…

- Utiliser le syscall **`read`** (n°0)
- La symétrie **`write`** ↔ **`read`** (même conventions)
- Le rôle du **file descriptor 0** (stdin)
- Pourquoi récupérer **`rax`** après `read`
- Préparer un **buffer dans `.bss`**
- Que le **retour ligne** fait partie de ce qui est lu
- Écrire un premier programme **interactif**

---


## Chapitre 14 — Convertir texte et nombres

### Le minimum à savoir

#### Le problème : `'5'` ≠ `5`

Si l'utilisateur tape `5`, le buffer contient l'**octet 53** (le code ASCII de `'5'`), pas le nombre 5. Tenter de calculer `[buffer] + 1` te donnerait 54 (`'6'`), pas 6.

> **Confusion classique du débutant.** Mémorise : le caractère `'5'` vaut **53** en mémoire. Pour avoir le nombre 5, il faut **soustraire 48** (le code de `'0'`).

#### Convertir un caractère en chiffre

```nasm
mov al, '5'          ; al = 0x35 = 53
sub al, '0'          ; al = 53 - 48 = 5
```

Ou de façon équivalente :

```nasm
sub al, 0x30
```

Ces deux écritures sont identiques. La 1ère est plus lisible.

#### Convertir un chiffre en caractère

L'opération inverse :

```nasm
mov al, 7            ; al = 7
add al, '0'          ; al = 7 + 48 = 55 = '7'
```

#### Vérifier que c'est bien un chiffre

Avant de soustraire `'0'`, il vaut mieux vérifier que c'est entre `'0'` et `'9'`. On verra comment au chapitre 16 (avec `cmp` et les sauts).

#### Cas simple : lire et afficher un chiffre + 1

```nasm
; chiffre.asm — Lit un chiffre, ajoute 1, l'affiche

section .data
    prompt   db "Tape un chiffre (0-9) : ", 0
    prompt_l equ $ - prompt - 1

section .bss
    buffer  resb 4

section .text
global _start
_start:
    ; afficher le prompt
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, prompt_l
    syscall

    ; lire 2 octets (un chiffre + le \n)
    mov rax, 0
    mov rdi, 0
    mov rsi, buffer
    mov rdx, 2
    syscall

    ; convertir le caractère en nombre
    mov al, [buffer]       ; al = code ASCII du chiffre
    sub al, '0'            ; al = chiffre réel (0-9)
    inc al                 ; al = chiffre + 1
    add al, '0'            ; al = code ASCII du résultat
    mov [buffer], al       ; remplacer le 1er octet du buffer

    ; afficher le résultat (1 octet)
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 1
    syscall

    ; un retour ligne pour faire propre
    mov byte [buffer], 10
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 1
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

Sortie :

```
Tape un chiffre (0-9) : 4
5
```

🎉 **Tu viens de coder une mini-calculatrice à 1 chiffre.**

#### Et pour plusieurs chiffres ?

Convertir une chaîne comme `"123"` en l'entier 123 demande **une boucle** : on parcourt chaque chiffre, on accumule. L'algorithme :

```
résultat = 0
pour chaque chiffre c :
    résultat = résultat * 10 + (c - '0')
```

Sans boucle (ch. 17), on ne peut pas encore le coder. On va y revenir.

#### Algorithme inverse : nombre → chaîne

C'est encore plus tordu. Pour transformer 123 en `"123"` :

```
si nombre == 0 → afficher '0'
sinon, tant que nombre > 0 :
    chiffre = nombre % 10
    caractère = chiffre + '0'
    stocker dans buffer (à l'envers !)
    nombre = nombre / 10
puis afficher buffer dans l'ordre inverse
```

C'est pourquoi on dit qu'**afficher un nombre en ASM est non trivial**. On en fera un mini-projet de boucles (ch. 17).

### Très utile en pratique

#### Code ASCII des chiffres : à connaître par cœur

| Caractère | Décimal | Hexa |
|-----------|---------|------|
| `'0'` | 48 | `0x30` |
| `'1'` | 49 | `0x31` |
| `'2'` | 50 | `0x32` |
| `'9'` | 57 | `0x39` |

Donc :
- Pour **caractère → chiffre** : `sub al, 48` (ou `sub al, '0'`).
- Pour **chiffre → caractère** : `add al, 48` (ou `add al, '0'`).

#### Petite astuce mémo : la différence est toujours `0x30`

`'0' = 0x30`, `'1' = 0x31`, … `'9' = 0x39`. La différence entre le chiffre et son ASCII est **toujours 0x30 = 48**.

#### Avec d'autres caractères

Même logique pour les lettres :

```nasm
; transformer 'A'..'Z' en 'a'..'z'
sub al, 'A'         ; al = 0..25
add al, 'a'         ; al = 'a'..'z'
; ou plus directement :
add al, 0x20        ; +32 = passe en minuscule
```

### Bonus

#### Pourquoi `'0'` vaut 48 et pas 0 ?

Historiquement, ASCII range les caractères affichables après les codes de contrôle (0-31). Les chiffres viennent à `48-57`, les majuscules à `65-90`, les minuscules à `97-122`. La table est conçue pour que :
- Toutes les minuscules diffèrent de leur majuscule de exactement **32**.
- Les chiffres `'0'-'9'` se suivent.

C'est cette ergonomie qui rend les conversions si simples avec `sub` et `add`.

### ❌ Erreur classique

```
Additionner '5' + 3 et croire qu'on obtient '8'
→ '5' + 3 = 53 + 3 = 56 = '8'. OK !
→ Mais '5' + '3' = 53 + 51 = 104 ≠ '8'. Piège classique.

Oublier de convertir avant de faire un calcul
→ "5" en buffer = 53. "5" + 1 = 54 = '6' (heureusement, mais c'est par chance).

Oublier add '0' avant d'afficher un chiffre
→ Tu affiches un caractère de contrôle (invisible) au lieu d'un chiffre.

Croire que read renvoie un entier
→ NON. read renvoie un texte (octets). Toi de convertir.

Confondre la longueur du buffer et le nombre lu
→ Toujours utiliser rax (renvoyé par read) pour la longueur.
```

### Exercices

**Guidé :** Reprends et exécute `chiffre.asm` ci-dessus. Teste avec différents chiffres.

**Autonome :** Modifie le programme pour qu'il **double** le chiffre saisi (au lieu d'ajouter 1). Attention : si tu saisis 5, ça donne 10, qui ne tient plus sur un seul chiffre. **Limite ton test** à des saisies de 0 à 4 pour l'instant.

**Défi :** Écris un programme qui demande **deux** chiffres (en deux saisies successives via `read`) et affiche leur somme (si elle reste < 10).

### 🧩 Mini-projet (chapitres 13-14) — Addition à 1 chiffre

Crée `add_chiffres.asm` qui :

1. Affiche `"Premier chiffre : "`.
2. Lit (read avec rdx=2 pour avoir chiffre + \n).
3. Convertit (sub '0') et stocke dans une variable `a` en `.bss`.
4. Affiche `"Deuxieme chiffre : "`.
5. Lit, convertit, stocke dans `b`.
6. Calcule `a + b` (résultat dans `al`).
7. Reconvertit en ASCII (`add '0'`).
8. Affiche le résultat suivi d'un retour ligne.

> **Limitation :** ne fonctionnera correctement que si la somme est ≤ 9.

### ✅ Tu sais maintenant…

- Que `'5'` ≠ `5` : un caractère est un code ASCII
- Convertir **caractère → chiffre** avec `sub al, '0'`
- Convertir **chiffre → caractère** avec `add al, '0'`
- Lire un chiffre saisi et le manipuler comme un nombre
- Pourquoi convertir un **entier multi-chiffres** demande une boucle
- Que tu sais maintenant écrire des programmes **vraiment interactifs**

---


## Chapitre 15 — Fichiers et syscalls utiles

### Le minimum à savoir

#### Au-delà de stdin/stdout

Tu sais lire le clavier et écrire à l'écran. Mais comment **lire un fichier** ou **écrire dans un fichier** ? Réponse : avec d'autres syscalls.

#### Les 5 syscalls de gestion de fichiers

| Syscall | Numéro | Rôle |
|---------|--------|------|
| **`open`** | 2 | Ouvre un fichier, renvoie un file descriptor (fd) |
| **`read`** | 0 | Lit depuis un fd |
| **`write`** | 1 | Écrit dans un fd |
| **`close`** | 3 | Ferme un fd |
| **`lseek`** | 8 | Déplace le curseur dans un fichier |

#### Le syscall `open` (numéro 2)

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

#### `open` renvoie un fd

Après `open`, `rax` contient :
- Un **fd positif** (un entier ≥ 3) si tout s'est bien passé. **Mémorise-le**.
- Une **valeur négative** si erreur (`-1`, `-2`, etc.).

#### Lire un fichier complet : `cat.asm`

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

#### Écrire dans un fichier

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

#### Toujours fermer ce qu'on a ouvert

Comme en Python (`f.close()`), on **doit** fermer ce qu'on ouvre. Sinon, fuite de descripteurs (le système en a un nombre limité).

### Très utile en pratique

#### Détecter une erreur de syscall

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

#### Buffers et lecture par blocs

Si tu lis un fichier plus grand que ton buffer, **un seul `read` ne suffira pas**. Il faut **boucler** :

```
tant que read renvoie > 0 :
    écrire ce qu'on a lu
    relancer read
```

C'est exactement ce que fait `cat`. On le fera proprement après les boucles (ch. 17).

### Bonus

#### Le syscall `lseek` (numéro 8)

`lseek` permet de **déplacer le curseur** dans un fichier (utile pour relire le début ou sauter une portion).

| Argument | Registre |
|----------|----------|
| numéro | `rax = 8` |
| fd | `rdi` |
| décalage | `rsi` |
| origine | `rdx` (0 = début, 1 = position actuelle, 2 = fin) |

#### Erreurs typiques de `open`

| Code (valeur) | Signification |
|---------------|---------------|
| `-2` | Fichier introuvable (ENOENT) |
| `-13` | Permission refusée (EACCES) |
| `-17` | Fichier existe déjà (EEXIST), avec O_CREAT \| O_EXCL |

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée `cat.asm` comme ci-dessus, mais en lisant un fichier que tu crées avec `echo "Bonjour" > test.txt`. Adapte le chemin dans le `.asm`.

**Autonome :** Écris un programme qui crée un fichier `salut.txt` contenant la chaîne `"Salut\n"`. Vérifie avec `cat salut.txt` que ça fonctionne.

**Défi :** Écris un programme qui :
1. Ouvre `test.txt` en lecture.
2. Lit son contenu (jusqu'à 256 octets) dans un buffer.
3. **Écrit ce contenu** dans `copie.txt`.
4. Ferme les deux fichiers.

C'est l'équivalent de `cp test.txt copie.txt` (pour les petits fichiers).

### 🧩 Mini-projet (chapitres 13-15) — Mini-cat avec saisie

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

### ✅ Tu sais maintenant…

- Ouvrir un fichier avec **`open`** (numéro 2)
- Comprendre les **flags** : `O_RDONLY`, `O_WRONLY`, `O_CREAT`, `O_TRUNC`, etc.
- Récupérer un **file descriptor** dans `rax`
- Le **mémoriser** dans une variable
- Lire et écrire dans un fichier via `read`/`write` avec ce fd
- **Fermer** proprement avec `close` (numéro 3)
- Détecter (à venir) une erreur via une **valeur négative**
- Coder un **mini-`cat`** en assembleur pur

---

### 🚩 Checkpoint — Fin de la Partie V

À ce stade, tu sais écrire un vrai programme interactif. Vérifie que tu peux :

- [ ] Lire une saisie utilisateur avec `read` et récupérer le nombre d'octets lus.
- [ ] Convertir un caractère ASCII en chiffre (et vice-versa).
- [ ] Ouvrir, lire, écrire et fermer un fichier avec `open`, `read`, `write`, `close`.
- [ ] Comprendre pourquoi `'5'` ≠ `5`.
- [ ] Mémoriser un file descriptor dans une variable `.bss`.
- [ ] Identifier qu'un syscall a échoué (valeur négative dans `rax`).

**Si tu sais faire tout ça, tu maîtrises les I/O bas niveau de Linux.** La suite (logique, fonctions, reverse) s'appuie là-dessus.

---
