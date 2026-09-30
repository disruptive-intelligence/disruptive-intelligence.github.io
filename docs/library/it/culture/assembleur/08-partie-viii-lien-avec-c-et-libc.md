---
title: PARTIE VIII — LIEN AVEC C ET LIBC
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 8
chapters: 10
---

---


## Chapitre 21 — Appeler la libc depuis l'assembleur

### Le minimum à savoir

#### Syscall vs fonction C : la différence

Tu sais utiliser `write` (syscall n°1) pour afficher du texte. Mais en C, on utilise plutôt **`printf`** : `printf("Bonjour\n")`. Quelle est la différence ?

| | Syscall (`write`, `read`, …) | Fonction libc (`printf`, `scanf`, …) |
|---|---|---|
| **Niveau** | Direct au noyau | Bibliothèque utilisateur |
| **Vitesse** | Plus rapide | Plus lent (mais plus pratique) |
| **Fonctionnalités** | Brutes (octets) | Formatage, conversion automatique |
| **Comment l'appeler** | `syscall` | `call` (comme une fonction normale) |
| **Convention** | `rax = num`, args dans `rdi, rsi, …` | Args dans `rdi, rsi, …`, retour dans `rax` |

> **À retenir :** une fonction libc comme `printf` **finit par appeler `write`** sous le capot. Elle ajoute juste tout le formatage (`%d`, `%s`…). C'est plus haut niveau.

#### Linker avec gcc au lieu de ld

Pour utiliser des fonctions libc, on **doit** linker avec `gcc` (qui s'occupe d'ajouter la libc automatiquement) :

```bash
nasm -f elf64 prog.asm -o prog.o
gcc -no-pie prog.o -o prog       # linker avec gcc, pas ld
```

L'option `-no-pie` simplifie la pédagogie (sans elle, l'exécutable est PIE = Position Independent Executable, ce qui complique les adresses). Pour ce cours, garde `-no-pie`.

#### Point d'entrée : `main` au lieu de `_start`

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

#### `extern` : déclarer les fonctions externes

Pour utiliser `printf`, tu dois dire à NASM qu'elle existe quelque part (dans la libc) :

```nasm
extern printf
extern scanf
extern exit
extern malloc
; ...
```

#### L'alignement à 16 octets : la règle critique

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

#### Premier `printf` : "Hello"

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

#### Le mystère du `xor rax, rax`

`xor rax, rax` est l'idiome compact pour `mov rax, 0` (un peu plus rapide et plus court). Pourquoi mettre 0 dans `rax` avant `printf` ?

**Parce que `printf` est variadique** (nombre d'arguments variable). La convention System V dit : avant d'appeler une fonction variadique, `rax` doit contenir **le nombre de registres XMM utilisés** (registres pour les flottants). Pour les `%d`, `%s`, etc., il n'y a aucun flottant, donc `rax = 0`.

> **Règle pratique :** avant `printf`, `scanf`, ou toute fonction variadique : **`xor rax, rax`**.

#### Afficher un entier avec `printf`

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

#### Lire un entier avec `scanf`

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

### Très utile en pratique

#### Récapitulatif : checklist pour appeler la libc

Avant chaque appel libc, vérifie :

- [ ] Tu as `global main` (pas `global _start`).
- [ ] Tu as `extern <fonction>` pour chaque fonction utilisée.
- [ ] `main` commence par `push rbp ; mov rbp, rsp` (alignement).
- [ ] Tu lies avec `gcc -no-pie`.
- [ ] Les chaînes sont **terminées par 0** (style C).
- [ ] Avant un appel variadique (`printf`, `scanf`), tu fais `xor rax, rax`.
- [ ] Tu termines `main` par `leave ; ret` (pas par `syscall exit`).

#### Le `lea ..., [rel ...]`

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

### Bonus

#### Le warning `.note.GNU-stack`

Quand tu lies un objet NASM avec gcc, tu peux voir ce message :

```
warning: ... missing .note.GNU-stack section implies executable stack
```

**Ce n'est pas une erreur, ton programme tourne quand même.** C'est juste un avertissement de sécurité : sans cette section, le linker pense que ta pile pourrait être exécutable (ce qui est dangereux). Pour le faire taire, ajoute en haut de ton `.asm` :

```nasm
section .note.GNU-stack noalloc noexec nowrite progbits
```

Ce point n'est pas essentiel pour les premiers exercices, mais c'est bon à savoir pour ne pas s'inquiéter du warning.

#### Autres fonctions libc utiles pour démarrer

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

#### `puts` : encore plus simple

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

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée `hello_c.asm` comme ci-dessus. Compile avec gcc, exécute.

**Autonome :** Crée un programme qui affiche **deux entiers** avec un seul `printf` : `printf("a=%d, b=%d\n", a, b)`. Mets `a` dans `rsi`, `b` dans `rdx`. Vérifie le résultat.

**Défi :** Écris un programme qui :
1. Demande un nombre à l'utilisateur (avec `scanf`).
2. Le **double**.
3. Affiche le résultat.

Si l'utilisateur tape 21, ça doit afficher 42.

### 🧩 Mini-projet (chapitre 21) — Calculatrice à 2 opérandes

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

### ✅ Tu sais maintenant…

- La différence **syscall** vs **fonction libc**
- Linker avec **`gcc -no-pie`**
- Utiliser **`global main`** et **`extern printf`** (etc.)
- L'alignement à **16 octets** avec `push rbp / mov rbp, rsp`
- L'idiome **`xor rax, rax`** avant les fonctions variadiques
- Afficher avec **`printf`**, lire avec **`scanf`**
- Que `scanf` veut une **adresse** (`lea`), pas une valeur
- Terminer `main` par **`xor rax, rax ; leave ; ret`** (préparer la valeur de retour, puis démonter le stack frame)

---


## Chapitre 22 — Du C vers l'assembleur

### Le minimum à savoir

#### Pourquoi ce chapitre ?

Tu as appris à **écrire** de l'assembleur à la main. Mais en pratique, l'ASM que tu vas lire en reverse vient **presque toujours** d'un compilateur C. Ce chapitre te montre :

1. Comment un programme C devient de l'assembleur.
2. À quoi ressemblent un `if`, une boucle, une fonction **compilés**.
3. Pourquoi le reverse est **plus simple sur `-O0`** que sur `-O2`.

#### Compiler un `.c` en `.s` (assembleur)

```bash
gcc -O0 -masm=intel -S monprog.c -o monprog.s
```

- **`-O0`** : pas d'optimisation (assembleur verbeux, lisible).
- **`-masm=intel`** : syntaxe **Intel** (compatible avec ce qu'on a appris).
- **`-S`** : produit `.s` au lieu de compiler en `.o`.

Tu obtiens `monprog.s` que tu peux **lire**.

#### Exemple : un programme C minimal

**`exemple.c` :**
```c
int main() {
    int a = 5;
    int b = 7;
    int c = a + b;
    return c;
}
```

Compile : `gcc -O0 -masm=intel -S exemple.c -o exemple.s`. Voici ce que gcc produit (extrait simplifié) :

```nasm
main:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4],  5     ; int a = 5
    mov     DWORD PTR [rbp - 8],  7     ; int b = 7
    mov     edx, DWORD PTR [rbp - 4]    ; edx = a
    mov     eax, DWORD PTR [rbp - 8]    ; eax = b
    add     eax, edx                     ; eax = a + b
    mov     DWORD PTR [rbp - 12], eax   ; c = eax
    mov     eax, DWORD PTR [rbp - 12]   ; return c
    pop     rbp
    ret
```

**Tu reconnais tout ?**
- `push rbp ; mov rbp, rsp` : prologue (ch. 20).
- `[rbp - 4]`, `[rbp - 8]`, `[rbp - 12]` : variables locales (ch. 20).
- `eax` au lieu de `rax` : parce que `int` en C fait 32 bits, pas 64 (ch. 2).
- `add eax, edx` : addition (ch. 8).
- `pop rbp ; ret` : épilogue (ch. 20).

> **C'est ça, comprendre l'ASM compilé** : reconnaître tous les patterns appris dans ce cours.

#### Un `if` compilé

**`exemple_if.c` :**
```c
int test(int x) {
    if (x > 10)
        return 1;
    else
        return 0;
}
```

Compile et regarde le `.s` :

```nasm
test:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4], edi   ; x dans une locale
    cmp     DWORD PTR [rbp - 4], 10    ; compare x à 10
    jle     .L2                         ; si x <= 10, saut "else"

    mov     eax, 1                      ; "if" : return 1
    jmp     .L3
.L2:
    mov     eax, 0                      ; "else" : return 0
.L3:
    pop     rbp
    ret
```

**Reconnaissance :**
- `cmp ... , 10 / jle ...` : test `if (x > 10)` (ch. 16).
- `.L2`, `.L3` : labels auto-générés par gcc.
- Le pattern **if/jmp/label/jmp/label** est le squelette `if/else` que tu connais déjà.

#### Une boucle `for` compilée

**`exemple_for.c` :**
```c
int somme() {
    int s = 0;
    for (int i = 0; i < 10; i++)
        s = s + i;
    return s;
}
```

Sortie ASM (extrait) :

```nasm
somme:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4], 0      ; s = 0
    mov     DWORD PTR [rbp - 8], 0      ; i = 0
    jmp     .L2                          ; aller au test
.L3:                                    ; corps de boucle
    mov     eax, DWORD PTR [rbp - 8]    ; eax = i
    add     DWORD PTR [rbp - 4], eax    ; s += i
    add     DWORD PTR [rbp - 8], 1      ; i++
.L2:
    cmp     DWORD PTR [rbp - 8], 9      ; i <= 9 ?
    jle     .L3                          ; si oui, recommencer
    mov     eax, DWORD PTR [rbp - 4]    ; return s
    pop     rbp
    ret
```

**Reconnaissance :**
- Un **saut arrière** (`jle .L3`) → c'est une **boucle** (ch. 17).
- Un compteur incrémenté → variable de boucle.
- Le pattern **jmp test ; label_corps ; corps ; label_test ; cmp ; jXX label_corps** est l'écriture typique d'une boucle `for` en gcc.

> **Astuce reverse :** quand tu vois un saut **vers une adresse précédente** dans le code, c'est **un indice très fort** de boucle (c'est l'écriture la plus naturelle d'une boucle, et c'est ce que gcc produit en `-O0`). Garde une petite réserve mentale pour des cas plus exotiques (sauts arrière qui font partie de `goto` complexes, ou de patterns optimisés), mais en pratique débutante : **saut arrière → boucle**.

#### Une fonction qui en appelle une autre

**`exemple_appel.c` :**
```c
int carre(int n) {
    return n * n;
}

int main() {
    int x = carre(7);
    return x;
}
```

ASM :

```nasm
carre:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4], edi    ; n dans locale
    mov     eax, DWORD PTR [rbp - 4]
    imul    eax, eax                     ; eax = n * n
    pop     rbp
    ret

main:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16
    mov     edi, 7                       ; arg pour carre
    call    carre                        ; rax = 49
    mov     DWORD PTR [rbp - 4], eax    ; x = rax
    mov     eax, DWORD PTR [rbp - 4]
    leave
    ret
```

**Reconnaissance :**
- `call carre` : appel de fonction (ch. 19).
- `mov edi, 7 ; call ...` : passage d'arg via `rdi` (ch. 19).
- `mov ..., eax` après le call : récupération de la valeur de retour (ch. 19).

#### L'impact des optimisations

**Le même `exemple_if.c` compilé avec `-O2`** :

```nasm
test:
    xor     eax, eax              ; eax = 0
    cmp     edi, 10               ; x > 10 ?
    setg    al                    ; al = 1 si x > 10, 0 sinon
    ret
```

**Quatre instructions au lieu de douze.** Le `if/else` a disparu, remplacé par `setg` (set if greater) qui produit 0 ou 1 directement. C'est plus rapide, mais **beaucoup plus dur à lire**.

> **Pour le reverse engineering débutant : préfère analyser des binaires en `-O0`.** En `-O2`, les patterns sont méconnaissables et il faut une expérience plus large.

### Très utile en pratique

#### Liste de patterns à reconnaître

| Pattern ASM | Construction C |
|-------------|----------------|
| `push rbp / mov rbp, rsp / sub rsp, N` | Début de fonction |
| `leave / ret` ou `mov rsp, rbp / pop rbp / ret` | Fin de fonction |
| `cmp ... , ... / jXX label` | `if (...)` |
| `cmp ... / jge label_corps` (saut arrière) | Boucle |
| `call fn` | Appel de fonction |
| `mov edi, X / call fn` | Appel avec arg |
| `mov [rbp - N], eax` | Affectation à une variable locale |
| `mov eax, [rbp - N]` | Lecture d'une variable locale |
| `test eax, eax / je ...` | `if (x == 0)` |
| `setg al / setl al / etc.` | Optimisation d'une comparaison (en `-O2`) |

#### Comparer C et ASM côte à côte

L'outil **Godbolt Compiler Explorer** ([godbolt.org](https://godbolt.org)) affiche, en direct, l'ASM produit par un compilateur pour un code C. C'est **fantastique** pour s'entraîner :

1. Tape un petit C à gauche.
2. Choisis x86-64 gcc.
3. Ajoute `-O0 -masm=intel` dans les flags.
4. L'ASM apparaît à droite, avec un code-couleur reliant les lignes C aux lignes ASM.

**Indispensable** pour ce chapitre. Joue avec.

### Bonus

#### Les niveaux d'optimisation

| Flag | Effet |
|------|-------|
| `-O0` | Aucune optimisation. ASM verbeux, lisible. **Pour debug et reverse pédagogique.** |
| `-O1` | Optimisations basiques. Élimine du code mort. |
| `-O2` | Optimisations standards. **Le défaut pour la prod.** |
| `-O3` | Optimisations agressives, parfois trop. |
| `-Os` | Optimise pour la **taille** du binaire. |

#### Niveaux différents : ce qui change

Sur un même `if` :
- `-O0` : ~10 instructions, `cmp / jXX / mov / jmp / mov`.
- `-O2` : ~3 instructions, souvent `setXX` ou même expression mathématique sans saut.

Pour **commencer le reverse**, vise du `-O0`. Tu monteras en optimisation au fur et à mesure.

### ❌ Erreur classique

```
Croire que gcc traduit ligne à ligne
→ Faux. gcc applique des optimisations, réorganise, fusionne.

Lire du -O2 en croyant que c'est du brut
→ Tu te perds. Identifie toujours le niveau d'optimisation d'un binaire.

Ne pas mettre -masm=intel
→ Tu te retrouves avec de l'AT&T (mov $5, %eax) que tu ne sais pas lire.

Croire que toutes les variables C sont sur la pile
→ En -O2, gcc met les variables fréquentes dans des registres directement.

Ne pas savoir où est le main quand on lit un .s
→ Cherche le label "main:" tout simplement. Les autres labels (.LCO,
  .LFB0, .Letext0…) sont des labels internes de gcc.
```

### Exercices

**Guidé :** Écris ce `.c`, compile-le en `.s` avec `gcc -O0 -masm=intel -S`, et **lis le résultat**. Identifie le prologue, le calcul, l'épilogue.

```c
int double_plus_un(int n) {
    return 2 * n + 1;
}
```

**Autonome :** Écris un `.c` avec une fonction qui contient un **`if/else`**. Compile en `.s`. Repère le `cmp`, les sauts, les deux branches.

**Défi :** Écris un `.c` avec une **boucle `for` qui calcule une somme**. Compile en `-O0` et en `-O2`. Compare. Note les différences.

### 🧩 Mini-projet (chapitre 22) — Reverse mental

Écris en C un petit programme avec :
- Une fonction `f(int a, int b)` qui retourne `a * a + b`.
- Un `main` qui appelle `f(3, 4)` et affiche le résultat avec `printf`.

Compile en `-O0`. **Avant de lire le `.s`**, écris sur papier ce que tu **t'attendrais** à voir comme ASM (prologue, calculs, call, printf, épilogue).

Compare avec le `.s` réel. **Mesure ton intuition.**

### ✅ Tu sais maintenant…

- Compiler un C en ASM avec **`gcc -O0 -masm=intel -S`**
- Reconnaître les **patterns du compilateur** : prologue, locales, if, boucle, appel
- Comprendre que **les optimisations transforment le code**
- Préférer **`-O0`** pour apprendre le reverse
- Utiliser **Godbolt** pour s'entraîner
- Faire le pont entre **C** (que tu comprends grosso modo) et **ASM**

Ce chapitre est ton pont vers la **partie IX**, où tu vas plonger dans les binaires compilés sans avoir le `.c` sous les yeux.

---

### 🚩 Checkpoint — Fin de la Partie VIII (avant le reverse)

Dernier checkpoint avant de plonger dans le reverse. Tu dois pouvoir :

- [ ] Linker avec **`gcc -no-pie`** et utiliser `extern printf`.
- [ ] Appeler **`printf`** et **`scanf`** depuis l'assembleur.
- [ ] Comprendre **pourquoi** il faut `xor rax, rax` avant un appel variadique.
- [ ] Compiler un `.c` en `.s` avec `gcc -O0 -masm=intel -S`.
- [ ] **Reconnaître dans un `.s`** :
  - [ ] Un prologue de fonction.
  - [ ] Un `if/else`.
  - [ ] Une boucle (saut arrière).
  - [ ] Un appel de fonction avec son argument.
- [ ] Comprendre la différence d'aspect entre `-O0` et `-O2`.

**Si tu coches tout, tu as toutes les armes pour le reverse débutant.** La partie IX ne fait que t'apprendre à appliquer ces réflexes à un vrai binaire.

---

### 🧭 Méthode — Lire un désassemblage sans paniquer

Quand tu ouvres `objdump -d` sur un binaire pour la première fois, tu vois **des centaines de lignes**. Pas de panique. Voici une méthode en **5 étapes** à appliquer systématiquement :

#### Étape 1 — Repérer les chaînes

```bash
strings ./binaire
```

Les chaînes te donnent des **indices énormes** : messages d'erreur, prompts, formats `printf`, parfois des mots de passe en clair. Note celles qui ont l'air pertinentes.

#### Étape 2 — Repérer les appels libc

Cherche dans le désassemblage les `call <nom>@plt` :
- `printf@plt`, `puts@plt` → affichage.
- `scanf@plt`, `fgets@plt` → lecture utilisateur.
- **`strcmp@plt`, `memcmp@plt` → comparaison, souvent d'un mot de passe**.
- `malloc@plt`, `free@plt` → gestion mémoire.
- `system@plt`, `execve@plt` → exécution de commandes (méfiance).

C'est ta carte du programme.

#### Étape 3 — Repérer `main`

Si le binaire n'est pas strippé : `nm ./bin | grep main`.

Sinon : passe par `_start` → `__libc_start_main` → l'adresse passée dans `rdi` juste avant. (Méthode vue au chapitre 23.)

#### Étape 4 — Repérer conditions et boucles

Une fois dans `main`, balaye :
- Les **`cmp` + saut conditionnel vers une adresse en aval** → conditions (`if`).
- Les **sauts (conditionnels ou non) vers une adresse en amont** → boucles.
- Les **`call`** → appels de sous-fonctions à explorer ensuite.

#### Étape 5 — Renommer mentalement (ou dans un cahier)

À mesure que tu comprends, **donne des noms** aux choses :
- `[rbp - 4]` → tu as compris que c'est un compteur ? Appelle-le `i` dans ta tête.
- `[rbp - 16]` → un buffer ? Appelle-le `password_buf`.
- `0x401200` (fonction sans nom) → appelle-la `check_password`.

> **C'est exactement ce que font Ghidra et IDA automatiquement.** Mais même à la main, ça transforme un désassemblage cryptique en un programme compréhensible. Garde un cahier ou un fichier `notes.md` à côté pendant tes analyses.

---

### 🔍 Boîte à patterns — ASM pour le reverse

Avant de plonger dans la partie IX, voici **les 12 patterns essentiels** à reconnaître dans n'importe quel désassemblage. Imprime ce tableau, garde-le sous les yeux pendant tes premières analyses :

| Pattern ASM | Signification probable |
|-------------|------------------------|
| `push rbp` puis `mov rbp, rsp` | **Début de fonction** |
| `leave ; ret` ou `mov rsp, rbp ; pop rbp ; ret` | **Fin de fonction** |
| `sub rsp, N` après le prologue | Réservation de **N octets de variables locales** |
| `cmp ... , ... ` suivi de `jXX` | **Une condition** (if, comparaison) |
| `test rax, rax ; je ...` | Test `if (x == 0)` (ou `if (ptr == NULL)`) |
| Saut conditionnel vers une **adresse plus basse** (en arrière) | **Une boucle** |
| `mov edi, X ; call fn` | **Appel de fonction avec 1 argument** (`X`) |
| `mov edi, ... ; mov esi, ... ; call fn` | Appel à 2 arguments |
| `lea rdi, [rip + ...]` puis `call puts/printf@plt` | **Affichage d'une chaîne** |
| `call strcmp@plt` ou `call memcmp@plt` | **Comparaison de chaînes** (souvent un mot de passe !) |
| `call malloc@plt` ; le retour dans `rax` | **Allocation mémoire** |
| `mov eax, 0` puis `ret` | `return 0;` — souvent en fin de `main` |

> **Méthode reverse débutant :** quand tu lis un désassemblage, ne lis pas chaque instruction — **cherche d'abord ces patterns**. Ils te donnent la structure globale du programme. Les détails viennent ensuite.

---
