---
title: PARTIE II — INSTALLER, ÉCRIRE, EXÉCUTER
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 2
chapters: 10
---

---


## Chapitre 4 — Environnement de travail et premier programme

### Le minimum à savoir

#### Ce qu'il te faut

Pour suivre ce cours, tu as besoin de **Linux**. Trois options :

1. **Linux natif** (Ubuntu, Debian, Fedora…). Idéal.
2. **WSL2 sous Windows** (recommandé Windows 10/11). Suis [https://learn.microsoft.com/windows/wsl/install](https://learn.microsoft.com/windows/wsl/install) puis installe Ubuntu.
3. **Machine virtuelle** (VirtualBox, VMware…) avec Ubuntu/Debian. Fonctionne très bien.

> **Note :** macOS n'est pas un bon choix pour ce cours. Les syscalls sont différents, l'ABI est différente, GDB est limité. Si tu es sur Mac, utilise une VM Linux.

#### Les outils à installer

Sur Ubuntu/Debian, ouvre un terminal et tape :

```bash
sudo apt update
sudo apt install nasm binutils gcc gdb make
```

| Outil | À quoi ça sert |
|-------|----------------|
| **`nasm`** | L'assembleur : transforme ton `.asm` en `.o` (fichier objet) |
| **`binutils`** | Inclut `ld` (le linker) et `objdump` (qu'on verra plus tard) |
| **`gcc`** | Le compilateur C (qu'on utilisera comme linker plus tard) |
| **`gdb`** | Le debugger |
| **`make`** | L'outil de compilation automatisée |

Vérifie que tout est là :

```bash
nasm --version
ld --version
gcc --version
gdb --version
```

#### (Recommandé) Installer pwndbg pour un GDB plus lisible

GDB par défaut, c'est austère. Avec **pwndbg**, c'est nettement plus pédagogique (registres affichés automatiquement, pile visible, etc.).

```bash
cd ~
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

> **Alternative :** `gef` (https://github.com/hugsy/gef) fait à peu près la même chose. Choisis l'un OU l'autre.

#### La chaîne de compilation : du `.asm` au programme

```
   mon_prog.asm        ───nasm──→   mon_prog.o     ───ld──→   mon_prog
   (ton code)                       (fichier               (programme
                                     objet)                 exécutable)
```

- **NASM** lit ton fichier source (`.asm`) et le transforme en **fichier objet** (`.o`). Ce fichier contient du code machine **mais n'est pas exécutable** : il manque les "branchements" finaux.
- **`ld`** (le linker) prend le `.o` et en fait un vrai **exécutable** que tu peux lancer.

#### Ton premier programme : `exit.asm`

On ne commence **pas** par "Hello World" (trop d'éléments d'un coup). On commence par le programme le plus simple possible : un programme qui **ne fait rien**, sauf se terminer proprement avec un code de retour.

Crée un fichier `exit.asm` :

```nasm
; exit.asm — un programme qui se termine avec le code de retour 42

section .text
global _start

_start:
    mov rax, 60     ; numéro du syscall "exit"
    mov rdi, 42     ; code de retour
    syscall         ; demande au noyau de terminer le programme
```

#### Assembler, linker, exécuter

Dans le terminal, tape **dans l'ordre** :

```bash
nasm -f elf64 exit.asm -o exit.o   # 1. assembler → exit.o
ld exit.o -o exit                   # 2. linker    → exit (exécutable)
./exit                              # 3. exécuter
echo $?                             # 4. afficher le code de retour
```

Si tout va bien, l'étape 4 affiche `42`.

**Explication ligne par ligne du `.asm` :**

- `; …` : commentaire (Bash : `#`, Python : `#`, NASM : `;`).
- `section .text` : section du **code exécutable**.
- `global _start` : on dit au linker que l'étiquette `_start` est visible de l'extérieur. C'est le **point d'entrée** par défaut sous Linux.
- `_start:` : l'étiquette du point d'entrée. Quand on lance le programme, le CPU commence ici.
- `mov rax, 60` : on met **60** dans `rax`. C'est le numéro du syscall **exit** sous Linux x86-64.
- `mov rdi, 42` : on met **42** dans `rdi`. C'est l'argument du syscall (le code de retour qu'on veut).
- `syscall` : on **appelle le noyau**. Il regarde `rax` pour savoir quel service demander.

> **Promesse :** tu n'as pas besoin de tout comprendre maintenant. À la fin du chapitre 6, ces lignes seront limpides.

### Très utile en pratique

#### Un Makefile minimal

Pour ne pas retaper les commandes à chaque fois, crée un fichier `Makefile` (sans extension, et **avec une tabulation** devant les commandes, pas des espaces) :

```makefile
# Makefile générique pour ce cours

NASM = nasm
LD = ld
NASMFLAGS = -f elf64 -g -F dwarf

%.o: %.asm
	$(NASM) $(NASMFLAGS) $< -o $@

%: %.o
	$(LD) $< -o $@

clean:
	rm -f *.o
```

Maintenant, pour compiler `exit.asm`, tape juste :

```bash
make exit
./exit
```

#### Le drapeau `-g -F dwarf` : indispensable pour GDB

Sans `-g -F dwarf`, GDB peut afficher le code mais ne sait pas relier les instructions à ton fichier source. **Toujours compiler avec ces options en mode pédagogique.**

### ❌ Erreur classique

```
Essayer d'exécuter le .o au lieu de l'exécutable
→ ./exit.o ne marche pas. Il faut linker d'abord.

Oublier "global _start"
→ Erreur du linker : "undefined reference to _start".

Mettre _start dans une mauvaise section
→ _start doit être dans .text, sinon erreur.

Tabulations vs espaces dans le Makefile
→ Make exige des tabulations. Pas d'espaces. Sinon "missing separator".

Confondre les étapes : nasm = assembler, ld = linker
→ Les deux sont nécessaires, dans cet ordre.

Vouloir faire "syscall" sans avoir mis le numéro dans rax
→ Le syscall ne sait pas quoi faire. Tu vas crasher ou faire n'importe quoi.
```

### Exercices

**Guidé :** Crée `exit.asm` comme ci-dessus. Compile-le, exécute-le, et vérifie que `echo $?` affiche bien 42.

**Autonome :** Modifie le programme pour qu'il retourne **123** au lieu de 42. Recompile, relance, vérifie.

**Défi :** Que se passe-t-il si tu mets `255` ? Et `256` ? Et `1000` ? **Indice :** le code de retour Unix est limité à 8 bits non signés (0-255). Au-delà, il "boucle".

### ✅ Tu sais maintenant…

- Installer **NASM, ld, gcc, GDB**
- (Optionnellement) installer **pwndbg**
- La chaîne : `.asm → .o → exécutable`
- Écrire un programme minimal avec `section .text`, `global _start`, `_start:` et `syscall`
- Utiliser **`nasm -f elf64`** et **`ld`** pour compiler
- Récupérer le code de retour avec **`echo $?`**
- Écrire un **Makefile** simple pour automatiser

---


## Chapitre 5 — Anatomie d'un fichier `.asm`

### Le minimum à savoir

#### La structure d'un fichier NASM

Un fichier `.asm` est divisé en **sections**. Chaque section a un rôle précis :

```nasm
section .data       ; ← données initialisées (variables avec une valeur)
    ; ...

section .bss        ; ← données réservées non initialisées
    ; ...

section .text       ; ← le code exécutable
global _start
_start:
    ; ...
```

| Section | Rôle | Analogie |
|---------|------|----------|
| **`.text`** | Le code exécutable (les instructions) | Les **recettes** de cuisine |
| **`.data`** | Données initialisées (variables avec une valeur) | Les **ingrédients** déjà préparés |
| **`.bss`** | Espace réservé non initialisé (buffers vides) | Les **bols vides** pour plus tard |
| **`.rodata`** | Données en **lecture seule** (constantes) — optionnel | Les **étiquettes** sur les pots |

> **À retenir :** `.text` est obligatoire (sinon il n'y a pas de code). `.data` et `.bss` sont optionnels.

#### Les labels (étiquettes)

Un **label** est un nom que tu donnes à un endroit du fichier (un emplacement de code OU une variable). Tu utilises ensuite ce nom au lieu d'une adresse.

```nasm
section .data
    age db 25              ; "age" est un label pointant vers un octet de valeur 25
    nom db "Alice", 0      ; "nom" est un label pointant vers la chaîne "Alice\0"

section .text
global _start
_start:                    ; "_start" est un label pointant vers le début du code
    mov al, [age]          ; on utilise le label "age"
    ; ...
boucle:                    ; un label dans le code pour les sauts
    ; ...
```

> **Règle :** un label se termine par `:` quand on le **définit**. Quand on l'**utilise**, pas de `:`.

#### Les directives de données

Dans la section `.data`, on déclare des variables avec des **directives** :

| Directive | Taille | Usage |
|-----------|--------|-------|
| **`db`** | **b**yte (1 octet) | `nom db "Alice", 0` |
| **`dw`** | **w**ord (2 octets) | `pixel dw 0x1234` |
| **`dd`** | **d**ouble word (4 octets) | `version dd 12` |
| **`dq`** | **q**uad word (8 octets) | `gros dq 1234567890` |

Dans la section `.bss`, on **réserve** sans initialiser :

| Directive | Taille | Usage |
|-----------|--------|-------|
| **`resb N`** | N octets | `buffer resb 64` (réserve 64 octets) |
| **`resw N`** | N × 2 octets | `tab resw 10` |
| **`resd N`** | N × 4 octets | `tab resd 10` |
| **`resq N`** | N × 8 octets | `tab resq 10` |

Et pour les **constantes** (pas en mémoire, juste un nom pour une valeur fixe) :

```nasm
section .data
    msg db "Bonjour", 10
    LEN equ $ - msg        ; equ = "égal" : LEN devient une constante
```

> **`$` en NASM** = "l'adresse actuelle, ici, à cet endroit". Donc `$ - msg` = "la longueur entre `msg` et maintenant". Astuce pratique pour calculer une longueur de chaîne.

#### La syntaxe Intel : destination à gauche, source à droite

NASM utilise la **syntaxe Intel**, qui est la plus lisible :

```nasm
mov rax, 5         ; rax = 5    (destination = source)
add rax, rbx       ; rax = rax + rbx
mov [var], rax     ; var en mémoire = rax
```

Le **premier opérande** est la **destination**, le **second** est la **source**. C'est comme `x = 5` en Python : ce qui reçoit est à gauche.

> **Note :** la syntaxe AT&T (utilisée par défaut dans GDB et `objdump`) inverse cet ordre. On la verra **en lecture uniquement** dans l'Annexe A. Pour ce cours, on reste à 100 % en Intel.

#### Les commentaires

NASM utilise `;` pour les commentaires (comme Bash utilise `#`) :

```nasm
mov rax, 1     ; ceci est un commentaire de fin de ligne
; ceci est un commentaire pleine ligne
```

> **Conseil pédagogique :** commente **chaque ligne** au début. Ça force à expliquer ce que tu fais, et c'est la meilleure façon d'apprendre.

### Très utile en pratique

#### Exemple complet annoté

Voici un fichier `.asm` minimal qui contient les trois sections et plusieurs déclarations :

```nasm
; structure.asm — Démonstration de la structure d'un fichier NASM

; ─────────── SECTION DATA : variables initialisées ───────────
section .data
    nb_petit    db  42                  ; 1 octet  : 42
    nb_moyen    dw  1000                ; 2 octets : 1000
    nb_grand    dd  100000              ; 4 octets : 100000
    nb_enorme   dq  1234567890123       ; 8 octets : très grand
    message     db  "Bonjour", 0        ; chaîne terminée par 0
    LEN_MSG     equ $ - message         ; longueur de "message" (constante)

; ─────────── SECTION BSS : variables non initialisées ───────────
section .bss
    buffer      resb 64                 ; 64 octets réservés (vides)
    tab_int     resq 10                 ; 10 qword (80 octets) réservés

; ─────────── SECTION TEXT : le code ───────────
section .text
global _start

_start:
    ; ... ici on mettra des instructions au prochain chapitre ...

    ; pour l'instant, on quitte proprement
    mov rax, 60     ; syscall exit
    mov rdi, 0      ; code de retour 0
    syscall
```

Compile et exécute :

```bash
nasm -f elf64 structure.asm -o structure.o
ld structure.o -o structure
./structure
echo $?           # → 0
```

#### Récapitulatif visuel

```
   ┌─────────────────────────────────────────────────────────┐
   │                FICHIER .asm                             │
   ├─────────────────────────────────────────────────────────┤
   │                                                         │
   │   section .data    ← variables initialisées             │
   │     var1 db 5                                           │
   │     msg  db "Hi", 0                                     │
   │                                                         │
   │   section .bss     ← buffers vides                      │
   │     buf  resb 64                                        │
   │                                                         │
   │   section .text    ← code                               │
   │   global _start                                         │
   │   _start:                                               │
   │     ; instructions                                      │
   │                                                         │
   └─────────────────────────────────────────────────────────┘
```

### Bonus

#### Le label `_start` et `main`

Sous Linux, le point d'entrée par défaut pour `ld` est `_start`. Quand on linke avec `gcc`, le point d'entrée devient `main` (parce que gcc fournit un `_start` qui appelle `main`). On reverra ça au chapitre 21.

#### Pourquoi `.bss` plutôt que `.data` pour les buffers ?

Si tu déclares 1 Mo de buffer dans `.data`, **ton exécutable fera 1 Mo** (la valeur initiale est stockée dans le fichier). Si tu le déclares dans `.bss`, **le fichier reste minuscule** (le système réserve l'espace au lancement). Pour des buffers vides, toujours `.bss`.

### ❌ Erreur classique

```
Confondre db (data byte) et resb (reserve byte)
→ db : initialisé.    resb : réservé non initialisé.

Oublier les deux-points après un label
→ "_start" est traité comme une instruction → erreur.

Confondre une instruction et une directive
→ mov est une instruction (exécutée par le CPU).
→ db est une directive (gérée par NASM avant exécution).

Inverser destination et source
→ mov 5, rax  est faux. C'est mov rax, 5.

Mettre du code dans .data
→ NON. Le code va dans .text uniquement.

Oublier le 0 final d'une chaîne pour la libc
→ Pour les syscalls Linux, pas obligatoire (on donne la longueur).
→ Pour printf et autres fonctions C, OBLIGATOIRE.
```

### Exercices

**Guidé :** Crée `decla.asm` avec :
- une variable `age` de type byte initialisée à 25
- une variable `annee` de type dword initialisée à 2024
- une variable `nom` de type chaîne contenant "Bob" + un 0
- un buffer `buf` de 32 octets dans `.bss`
- un `_start` qui ne fait que quitter avec code 0

Compile-le et exécute-le. Ça doit afficher rien et `echo $?` doit donner `0`.

**Autonome :** Écris un fichier `.asm` qui contient :
- 5 constantes (avec `equ`) : `PI`, `E`, `MAX`, `MIN`, `ZERO` avec des valeurs au choix.
- 5 variables initialisées (utilisant `db`, `dw`, `dd`, `dq`).
- Un `_start` qui quitte avec le code de retour 7.

Vérifie que tout compile sans erreur.

**Défi :** Que vaut `LEN` ici, à ton avis (sans exécuter) ?

```nasm
section .data
    msg db "Hello!", 10, 0
    LEN equ $ - msg
```

> **Indice :** compte les octets. `"Hello!"` = 6 caractères + 1 retour ligne + 1 zéro = ?

### ✅ Tu sais maintenant…

- Les sections **`.text`**, **`.data`**, **`.bss`**
- Les directives de données **`db`, `dw`, `dd`, `dq`**
- Les directives de réservation **`resb`, `resw`, `resd`, `resq`**
- Les **constantes** avec `equ`
- Les **labels** et leur syntaxe (`:` à la définition)
- La **syntaxe Intel** : `instruction destination, source`
- Comment **commenter** avec `;`
- La règle `$ - label` pour calculer une longueur

---


## Chapitre 6 — Premier affichage avec `write`

### Le minimum à savoir

#### Pourquoi il n'y a pas de `print()` en assembleur

En Python, `print("Bonjour")` semble magique. En réalité, sous le capot, Python finit par appeler une **fonction du système** qui écrit dans le terminal. Cette fonction s'appelle **`write`** sous Linux, et c'est un **syscall**.

> **À retenir :** en assembleur, on ne fait pas un `print` magique. On **demande directement au noyau** d'écrire pour nous. Cette demande s'appelle un **syscall** (system call).

#### Qu'est-ce qu'un syscall ?

Un syscall, c'est une **demande de service au noyau** : "Noyau, je voudrais écrire ce texte sur l'écran", "ouvre-moi ce fichier", "donne-moi l'heure", etc.

**Analogie :** tu es au restaurant. Tu ne vas pas en cuisine — tu **commandes au serveur**. Le serveur (le noyau) va chercher ton plat (le service) et te le ramène. C'est exactement le rôle d'un syscall.

#### La convention de syscall Linux x86-64

Sous Linux x86-64, pour faire un syscall, il faut **toujours** :

1. Mettre le **numéro du syscall** dans `rax`.
2. Mettre les **arguments** dans `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9` (dans cet ordre).
3. Exécuter l'instruction `syscall`.
4. Le **résultat** revient dans `rax`.

```
   ┌─────────────────────────────────────────────┐
   │   AVANT le syscall                          │
   │   ─────────────                             │
   │   rax = numéro du syscall                   │
   │   rdi = 1er argument                        │
   │   rsi = 2ème argument                       │
   │   rdx = 3ème argument                       │
   │   r10 = 4ème argument                       │
   │   r8  = 5ème argument                       │
   │   r9  = 6ème argument                       │
   │                                             │
   │   syscall                                   │
   │                                             │
   │   APRÈS le syscall                          │
   │   ──────────────                            │
   │   rax = valeur de retour                    │
   └─────────────────────────────────────────────┘
```

> **À retenir tout de suite :** `rax` = numéro, `rdi` = arg 1, `rsi` = arg 2, `rdx` = arg 3. **Toujours dans cet ordre.**

> **⚠️ Effet de bord important :** l'instruction `syscall` **détruit toujours** les registres `rcx` et `r11` (le CPU s'en sert pour mémoriser l'adresse de retour et les flags). Si tu utilises `rcx` ou `r11` autour d'un syscall, **tu dois les sauvegarder** :
> ```nasm
>     push rcx          ; sauvegarder
>     mov rax, 1
>     mov rdi, 1
>     mov rsi, msg
>     mov rdx, len
>     syscall           ; rcx et r11 sont écrasés ici
>     pop rcx           ; restaurer
> ```
> Tu verras ce pattern partout dans le cours, notamment au chapitre 17 (boucles).

#### Le syscall `write` (numéro 1)

Le syscall **`write`** prend **3 arguments** :

1. **`rdi`** : le file descriptor (où écrire). `1` = sortie standard (le terminal).
2. **`rsi`** : l'adresse du début du texte à écrire.
3. **`rdx`** : le nombre d'octets à écrire.

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro de syscall | `rax` | `1` (= write) |
| file descriptor | `rdi` | `1` (= stdout) |
| adresse du buffer | `rsi` | `msg` (étiquette) |
| longueur en octets | `rdx` | `len` (constante) |

#### Le syscall `exit` (numéro 60)

Pour **terminer proprement** un programme :

1. **`rax`** : `60` (numéro de `exit`).
2. **`rdi`** : le code de retour (0 = succès).

Sans `exit` à la fin, **ton programme va crasher** (le CPU continuerait à exécuter ce qu'il y a après, qui n'est pas du code valide).

#### Ton premier "Hello, World!"

Crée `hello.asm` :

```nasm
; hello.asm — Premier programme qui affiche un message

section .data
    msg db "Bonjour Assembleur !", 10   ; le texte + retour ligne (10 = '\n')
    len equ $ - msg                      ; longueur calculée automatiquement

section .text
global _start

_start:
    ; ─── Appel write(1, msg, len) ───
    mov rax, 1          ; syscall write
    mov rdi, 1          ; file descriptor = stdout
    mov rsi, msg        ; adresse du message
    mov rdx, len        ; longueur
    syscall             ; demande au noyau d'écrire

    ; ─── Appel exit(0) ───
    mov rax, 60         ; syscall exit
    mov rdi, 0          ; code de retour 0
    syscall
```

Compile et exécute :

```bash
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello
./hello
```

Sortie :

```
Bonjour Assembleur !
```

🎉 **Bravo. Tu viens d'écrire ton premier programme assembleur.**

### Très utile en pratique

#### Pourquoi le `10` dans le message ?

`10` est le code ASCII du **retour ligne** (`\n`). Sans lui, ton message s'affiche, et le prompt du shell apparaît collé sur la même ligne. Tu peux d'ailleurs tester sans, pour voir.

#### Pourquoi `len` plutôt que de compter à la main ?

Tu pourrais écrire `mov rdx, 21` à la main (en comptant les caractères). Mais :
- C'est fragile (si tu modifies le message, tu dois recompter).
- C'est source d'erreurs.
- `equ $ - msg` le calcule pour toi à la compilation.

#### Les 4 file descriptors essentiels

| FD | Nom | Direction |
|----|-----|-----------|
| `0` | **stdin** | Entrée (clavier) |
| `1` | **stdout** | Sortie standard (écran) |
| `2` | **stderr** | Sortie d'erreur (écran aussi) |
| 3+ | fichiers ouverts | Fichiers que tu as toi-même ouverts |

Pour écrire un message d'erreur, on utilise `rdi = 2` au lieu de `rdi = 1`.

#### Afficher plusieurs messages

Il suffit de répéter le pattern :

```nasm
section .data
    msg1 db "Premier message", 10
    len1 equ $ - msg1
    msg2 db "Deuxieme message", 10
    len2 equ $ - msg2

section .text
global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg1
    mov rdx, len1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, msg2
    mov rdx, len2
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

> **Remarque :** c'est répétitif. Au chapitre 19, on transformera ce pattern en **fonction réutilisable**.

### Bonus

#### Trouver les numéros de syscall

Sous Linux x86-64, la liste des syscalls est dans :

```bash
# Le chemin peut varier selon la distribution. Essaye dans l'ordre :
cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h   # Ubuntu/Debian récents
cat /usr/include/asm/unistd_64.h                     # certaines distributions
# Ou plus directement :
grep __NR_write /usr/include/x86_64-linux-gnu/asm/unistd_64.h
man 2 syscalls
```

Voici les plus courants (à retenir progressivement) :

| Numéro | Nom | Description |
|--------|-----|-------------|
| 0 | `read` | Lire des octets |
| 1 | `write` | Écrire des octets |
| 2 | `open` | Ouvrir un fichier |
| 3 | `close` | Fermer un fichier |
| 8 | `lseek` | Se déplacer dans un fichier |
| 60 | `exit` | Quitter |

#### Différence syscall vs fonction C

Plus tard (chapitre 21), tu utiliseras `printf` au lieu de `write`. Ce sont **deux choses différentes** :
- `write` est un **syscall** : demande directe au noyau.
- `printf` est une **fonction de la libc** : elle formate du texte, puis appelle `write`.

Pour l'instant, on reste sur `write` : c'est plus simple, plus bas niveau, et plus instructif.

### ❌ Erreur classique

```
Oublier de mettre rax = 1 avant write
→ Tu fais un syscall avec un mauvais numéro. Comportement indéterminé.

Oublier rdx (la longueur)
→ Le noyau ne sait pas combien d'octets écrire. Affichage corrompu ou rien.

Confondre msg et [msg]
→ Pour write, on veut l'ADRESSE du message, donc msg (sans crochets).
→ [msg] = la valeur stockée à cette adresse (le premier octet = 'B' = 66).

Oublier le retour ligne dans le message
→ Le prompt du shell s'affiche collé. Pas grave, mais moche.

Oublier le syscall exit final
→ Le programme va crasher (Segmentation fault).

Confondre fd 1 (stdout) et fd 2 (stderr)
→ stderr est utilisé pour les messages d'erreur.
```

### Exercices

**Guidé :** Crée `hello.asm` comme ci-dessus. Compile, exécute. Modifie ensuite le message et la longueur (mais utilise `equ $ - msg`, ne compte pas à la main).

**Autonome :** Crée un programme `info.asm` qui affiche **3 lignes successives** :

```
Nom    : Alice
Age    : 30
Metier : Developpeur
```

Utilise 3 syscalls `write` à la suite. Pas de boucle (on n'en a pas encore vu).

**Défi :** Crée un programme qui affiche le **même message sur stdout ET sur stderr**. Teste avec :

```bash
./monprog              # affiche tout
./monprog 2>/dev/null  # stderr supprimé → ne reste que stdout
./monprog 1>/dev/null  # stdout supprimé → ne reste que stderr
```

### 🧩 Mini-projet (chapitres 4-6) — Bannière

Crée un programme `banniere.asm` qui affiche cette bannière à l'écran :

```
==========================================
       BIENVENUE EN ASSEMBLEUR
       x86-64 sous Linux
==========================================
```

Chaque ligne est un message séparé, affiché avec un syscall `write` distinct. Le programme se termine avec `exit(0)`.

> **Bonus :** ajoute une ligne d'espacement au début et à la fin de la bannière.

### ✅ Tu sais maintenant…

- Ce qu'est un **syscall** et pourquoi il existe
- La **convention syscall** Linux x86-64 (`rax`, `rdi`, `rsi`, `rdx`, …)
- Utiliser **`write`** (n°1) pour afficher du texte
- Utiliser **`exit`** (n°60) pour quitter
- La différence **`msg`** (adresse) vs **`[msg]`** (contenu)
- Les file descriptors **0, 1, 2**
- Écrire ton premier programme **réellement utile**

---
