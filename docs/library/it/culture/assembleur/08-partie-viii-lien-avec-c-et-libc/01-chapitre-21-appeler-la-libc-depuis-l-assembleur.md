---
title: Chapitre 21 — Appeler la libc depuis l'assembleur
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VIII — Lien avec C ET libc
  - index.md
---

## Le minimum à savoir

### Syscall vs fonction C : la différence

Tu sais utiliser `write` (syscall n°1) pour afficher du texte. Mais en C, on utilise plutôt **`printf`** : `printf("Bonjour\n")`. Quelle est la différence ?

| | Syscall (`write`, `read`, …) | Fonction libc (`printf`, `scanf`, …) |
|---|---|---|
| **Niveau** | Direct au noyau | Bibliothèque utilisateur |
| **Vitesse** | Plus rapide | Plus lent (mais plus pratique) |
| **Fonctionnalités** | Brutes (octets) | Formatage, conversion automatique |
| **Comment l'appeler** | `syscall` | `call` (comme une fonction normale) |
| **Convention** | `rax = num`, args dans `rdi, rsi, …` | Args dans `rdi, rsi, …`, retour dans `rax` |

> **À retenir :** une fonction libc comme `printf` **finit par appeler `write`** sous le capot. Elle ajoute juste tout le formatage (`%d`, `%s`…). C'est plus haut niveau.

### Linker avec gcc au lieu de ld

Pour utiliser des fonctions libc, on **doit** linker avec `gcc` (qui s'occupe d'ajouter la libc automatiquement) :

```bash
nasm -f elf64 prog.asm -o prog.o
gcc -no-pie prog.o -o prog       # linker avec gcc, pas ld
```


L'option `-no-pie` simplifie la pédagogie (sans elle, l'exécutable est PIE = Position Independent Executable, ce qui complique les adresses). Pour ce cours, garde `-no-pie`.

### Point d'entrée : `main` au lieu de `_start`

Quand on linke avec gcc, le `_start` est **fourni** par gcc (c'est lui qui appelle `main`). Tu dois donc nommer ton point d'entrée **`main`** :

```nasm
section .text
global main           ; au lieu de _start
extern printf         ; on déclare qu'on va utiliser printf

main:
    ; ...
    ret               ; ret au lieu de syscall exit
```


> **Important :** ne fais **pas** `mov rax, 60 ; syscall` à la fin. Fais juste `ret` : gcc retournera dans le `_start` qu'il a fourni, qui appellera `exit` pour toi.

### `extern` : déclarer les fonctions externes

Pour utiliser `printf`, tu dois dire à NASM qu'elle existe quelque part (dans la libc) :

```nasm
extern printf
extern scanf
extern exit
extern malloc
; ...
```


### L'alignement à 16 octets : la règle critique

C'est **LA** règle à retenir pour appeler la libc. La convention System V exige que **`rsp` soit aligné sur 16 octets juste avant un `call`**. Sinon, certaines fonctions (notamment `printf` quand il utilise du SSE) crashent.

**Pourquoi un prologue `push rbp ; mov rbp, rsp` règle la question :**

Quand `_start` (fourni par gcc) appelle ton `main`, l'instruction `call main` **empile l'adresse de retour** (8 octets). À l'entrée de ta fonction `main`, `rsp` est donc à **`8 mod 16`** (désaligné de 8 octets).

```
Avant call main :  rsp = ...0x00     (aligné sur 16)
Pendant call    :  rsp -= 8          (push adresse retour)
À l'entrée main :  rsp = ...0x08     (DÉSALIGNÉ : 8 mod 16)
Après push rbp  :  rsp -= 8 encore
                   rsp = ...0x00     (RÉALIGNÉ sur 16) ✓
```


C'est pour ça que **le prologue classique `push rbp ; mov rbp, rsp` est exactement ce qu'il faut**. Il préserve `rbp` ET il réaligne la pile. Quand tu fais ensuite `call printf`, `rsp` est aligné, tout va bien.

> **Règle pratique :** **mets toujours un prologue dans `main`** (et dans toute fonction qui appelle la libc) et tu n'auras pas de souci.
>
> **Cas piège :** si tu fais un `push` solo (par exemple `push rcx` pour le sauvegarder) **juste avant** un `call printf`, tu re-désalignes la pile et tu crashes. Solution : faire des push **par paires** ou utiliser `sub rsp, 8` après le push (puis `add rsp, 8` avant le pop).

### Premier `printf` : "Hello"

```nasm
; hello_c.asm — Hello World avec printf

section .data
    fmt db "Bonjour depuis l'asm !", 10, 0    ; chaîne C terminée par 0

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    lea rdi, [rel fmt]    ; rdi = adresse de la chaîne (1er arg)
    xor rax, rax          ; rax = 0 (nombre de regs XMM utilisés)
    call printf

    xor rax, rax          ; retour 0
    leave
    ret
```


Compile et exécute :

```bash
nasm -f elf64 hello_c.asm -o hello_c.o
gcc -no-pie hello_c.o -o hello_c
./hello_c
```


Sortie :

```
Bonjour depuis l'asm !
```


### Le mystère du `xor rax, rax`

`xor rax, rax` est l'idiome compact pour `mov rax, 0` (un peu plus rapide et plus court). Pourquoi mettre 0 dans `rax` avant `printf` ?

**Parce que `printf` est variadique** (nombre d'arguments variable). La convention System V dit : avant d'appeler une fonction variadique, `rax` doit contenir **le nombre de registres XMM utilisés** (registres pour les flottants). Pour les `%d`, `%s`, etc., il n'y a aucun flottant, donc `rax = 0`.

> **Règle pratique :** avant `printf`, `scanf`, ou toute fonction variadique : **`xor rax, rax`**.

### Afficher un entier avec `printf`

```nasm
section .data
    fmt db "Resultat : %ld", 10, 0      ; %ld pour un long (qword), cohérent avec dq
    val dq 42

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    lea rdi, [rel fmt]
    mov rsi, [val]        ; 2ème arg : valeur à afficher (qword)
    xor rax, rax
    call printf

    xor rax, rax
    leave
    ret
```


Sortie : `Resultat : 42`.

### Lire un entier avec `scanf`

```nasm
section .data
    prompt db "Tape un nombre : ", 0
    fmt_in db "%ld", 0          ; format pour un long (qword)
    fmt_out db "Tu as tape : %ld", 10, 0

section .bss
    nombre resq 1

section .text
global main
extern printf
extern scanf

main:
    push rbp
    mov rbp, rsp

    ; printf(prompt)
    lea rdi, [rel prompt]
    xor rax, rax
    call printf

    ; scanf("%ld", &nombre)
    lea rdi, [rel fmt_in]
    lea rsi, [rel nombre]       ; ADRESSE de nombre (scanf y écrira)
    xor rax, rax
    call scanf

    ; printf("Tu as tape : %d\n", nombre)
    lea rdi, [rel fmt_out]
    mov rsi, [nombre]
    xor rax, rax
    call printf

    xor rax, rax
    leave
    ret
```


🎉 **Tu peux maintenant lire et afficher des nombres "comme en C", proprement.**

> **Détail à connaître :** quand un prompt **ne se termine pas par `\n`** (comme `"Tape un nombre : "`), il peut **rester bufferisé** par la libc et ne s'afficher qu'après la saisie. Sur un terminal interactif classique, ça passe généralement, mais pas toujours. Si tu rencontres ce souci, deux solutions :
> - Mettre un `\n` à la fin du prompt (peu élégant pour un prompt).
> - Appeler **`fflush(stdout)`** juste après le `printf` (`extern fflush` + `mov rdi, [stdout]` ou plus simple : `xor rdi, rdi ; call fflush` qui vide tous les buffers).
>
> Pour ne pas complexifier ce cours, on ne traite pas ce point en détail.

## Très utile en pratique

### Récapitulatif : checklist pour appeler la libc

Avant chaque appel libc, vérifie :

- [ ] Tu as `global main` (pas `global _start`).
- [ ] Tu as `extern <fonction>` pour chaque fonction utilisée.
- [ ] `main` commence par `push rbp ; mov rbp, rsp` (alignement).
- [ ] Tu lies avec `gcc -no-pie`.
- [ ] Les chaînes sont **terminées par 0** (style C).
- [ ] Avant un appel variadique (`printf`, `scanf`), tu fais `xor rax, rax`.
- [ ] Tu termines `main` par `leave ; ret` (pas par `syscall exit`).

### Le `lea ..., [rel ...]`

Tu vois `lea rdi, [rel fmt]` au lieu de `mov rdi, fmt`. C'est un détail technique :

- En 64 bits, on utilise généralement des adresses **relatives à `rip`**.
- `[rel ...]` est la syntaxe NASM pour ça.
- `lea` calcule cette adresse sans la lire (rappel du ch. 12).

Mets `default rel` en haut de ton fichier pour ne plus avoir à écrire `rel` partout :

```nasm
default rel

section .data
    fmt db "Hello", 0

section .text
    lea rdi, [fmt]    ; au lieu de [rel fmt]
```


## Bonus

### Le warning `.note.GNU-stack`

Quand tu lies un objet NASM avec gcc, tu peux voir ce message :

```
warning: ... missing .note.GNU-stack section implies executable stack
```


**Ce n'est pas une erreur, ton programme tourne quand même.** C'est juste un avertissement de sécurité : sans cette section, le linker pense que ta pile pourrait être exécutable (ce qui est dangereux). Pour le faire taire, ajoute en haut de ton `.asm` :

```nasm
section .note.GNU-stack noalloc noexec nowrite progbits
```


Ce point n'est pas essentiel pour les premiers exercices, mais c'est bon à savoir pour ne pas s'inquiéter du warning.

### Autres fonctions libc utiles pour démarrer

| Fonction | Usage |
|----------|-------|
| `puts(s)` | Affiche la chaîne `s` + un `\n`. Plus simple que printf. |
| `strlen(s)` | Calcule la longueur d'une chaîne C. |
| `strcmp(s1, s2)` | Compare deux chaînes. 0 si égales. |
| `malloc(n)` | Alloue `n` octets, retourne l'adresse dans `rax`. |
| `free(p)` | Libère la mémoire pointée par `p`. |
| `atoi(s)` | Convertit la chaîne `s` en entier. |
| `exit(code)` | Quitte avec un code de retour. |

Toutes s'utilisent avec la convention System V : args dans `rdi, rsi, …`, retour dans `rax`.

> **⚠️ À connaître mais à ne PAS utiliser : `gets(s)`.** Cette fonction lisait une ligne **sans contrôle de taille**, ce qui en faisait une porte ouverte aux buffer overflows. Elle a été **retirée des standards C modernes**. Tu en entendras parler uniquement parce qu'on la rencontre dans :
> - de vieux programmes vulnérables ;
> - des CTF où c'est précisément la vulnérabilité à exploiter.
>
> Pour lire une chaîne proprement, utilise `fgets(buf, taille, stdin)` (qui prend une taille max).

### `puts` : encore plus simple

```nasm
section .data
    msg db "Hello", 0          ; PAS de \n : puts l'ajoute

section .text
global main
extern puts

main:
    push rbp
    mov rbp, rsp
    lea rdi, [rel msg]
    call puts                  ; pas de xor rax, rax : puts n'est PAS variadique
    xor rax, rax
    leave
    ret
```


## ❌ Erreur classique

```
Lier avec ld au lieu de gcc
→ Erreur "undefined reference to printf".

Oublier extern printf
→ NASM se plaint : "symbol `printf' undefined".

Oublier le 0 final dans le format de printf
→ printf lit en dehors. Comportement indéfini.

Oublier xor rax, rax avant printf variadique
→ Marche parfois, plante d'autres fois (selon le format).

Désaligner la pile avec un push solo avant le call
→ Crash dans printf (souvent un SIGSEGV).

Terminer main avec syscall exit au lieu de ret
→ Marche, mais ce n'est pas la convention.

Donner la valeur au lieu de l'adresse à scanf
→ scanf veut une ADRESSE où écrire. Toujours lea ..., [var].

Mettre l'argument variadique au mauvais endroit
→ Le format va dans rdi, puis les valeurs dans rsi, rdx, ...
```


## Exercices

**Guidé :** Crée `hello_c.asm` comme ci-dessus. Compile avec gcc, exécute.

**Autonome :** Crée un programme qui affiche **deux entiers** avec un seul `printf` : `printf("a=%d, b=%d\n", a, b)`. Mets `a` dans `rsi`, `b` dans `rdx`. Vérifie le résultat.

**Défi :** Écris un programme qui :

1. Demande un nombre à l'utilisateur (avec `scanf`).
2. Le **double**.
3. Affiche le résultat.

Si l'utilisateur tape 21, ça doit afficher 42.

## 🧩 Mini-projet (chapitre 21) — Calculatrice à 2 opérandes

Crée `calc.asm` qui :

1. Affiche `"Premier nombre : "`.
2. Lit `a` avec `scanf`.
3. Affiche `"Deuxieme nombre : "`.
4. Lit `b` avec `scanf`.
5. Affiche `a + b`, `a - b`, `a * b` avec des `printf` séparés.

Exemple :

```
$ ./calc
Premier nombre : 12
Deuxieme nombre : 5
12 + 5 = 17
12 - 5 = 7
12 * 5 = 60
```


## ✅ Tu sais maintenant…

- La différence **syscall** vs **fonction libc**
- Linker avec **`gcc -no-pie`**
- Utiliser **`global main`** et **`extern printf`** (etc.)
- L'alignement à **16 octets** avec `push rbp / mov rbp, rsp`
- L'idiome **`xor rax, rax`** avant les fonctions variadiques
- Afficher avec **`printf`**, lire avec **`scanf`**
- Que `scanf` veut une **adresse** (`lea`), pas une valeur
- Terminer `main` par **`xor rax, rax ; leave ; ret`** (préparer la valeur de retour, puis démonter le stack frame)

---
