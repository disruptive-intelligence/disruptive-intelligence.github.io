---
title: Chapitre 22 — Du C vers l'assembleur
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie VIII — Lien avec C et libc
  - index.md
---

## Le minimum à savoir

### Pourquoi ce chapitre ?

Tu as appris à **écrire** de l'assembleur à la main. Mais en pratique, l'ASM que tu vas lire en reverse vient **presque toujours** d'un compilateur C. Ce chapitre te montre :

1. Comment un programme C devient de l'assembleur.
2. À quoi ressemblent un `if`, une boucle, une fonction **compilés**.
3. Pourquoi le reverse est **plus simple sur `-O0`** que sur `-O2`.

### Compiler un `.c` en `.s` (assembleur)

```bash
gcc -O0 -masm=intel -S monprog.c -o monprog.s
```


- **`-O0`** : pas d'optimisation (assembleur verbeux, lisible).
- **`-masm=intel`** : syntaxe **Intel** (compatible avec ce qu'on a appris).
- **`-S`** : produit `.s` au lieu de compiler en `.o`.

Tu obtiens `monprog.s` que tu peux **lire**.

### Exemple : un programme C minimal

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

### Un `if` compilé

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

### Une boucle `for` compilée

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

### Une fonction qui en appelle une autre

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

### L'impact des optimisations

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

## Très utile en pratique

### Liste de patterns à reconnaître

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

### Comparer C et ASM côte à côte

L'outil **Godbolt Compiler Explorer** ([godbolt.org](https://godbolt.org)) affiche, en direct, l'ASM produit par un compilateur pour un code C. C'est **fantastique** pour s'entraîner :

1. Tape un petit C à gauche.
2. Choisis x86-64 gcc.
3. Ajoute `-O0 -masm=intel` dans les flags.
4. L'ASM apparaît à droite, avec un code-couleur reliant les lignes C aux lignes ASM.

**Indispensable** pour ce chapitre. Joue avec.

## Bonus

### Les niveaux d'optimisation

| Flag | Effet |
|------|-------|
| `-O0` | Aucune optimisation. ASM verbeux, lisible. **Pour debug et reverse pédagogique.** |
| `-O1` | Optimisations basiques. Élimine du code mort. |
| `-O2` | Optimisations standards. **Le défaut pour la prod.** |
| `-O3` | Optimisations agressives, parfois trop. |
| `-Os` | Optimise pour la **taille** du binaire. |

### Niveaux différents : ce qui change

Sur un même `if` :

- `-O0` : ~10 instructions, `cmp / jXX / mov / jmp / mov`.
- `-O2` : ~3 instructions, souvent `setXX` ou même expression mathématique sans saut.

Pour **commencer le reverse**, vise du `-O0`. Tu monteras en optimisation au fur et à mesure.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Écris ce `.c`, compile-le en `.s` avec `gcc -O0 -masm=intel -S`, et **lis le résultat**. Identifie le prologue, le calcul, l'épilogue.

```c
int double_plus_un(int n) {
    return 2 * n + 1;
}
```


**Autonome :** Écris un `.c` avec une fonction qui contient un **`if/else`**. Compile en `.s`. Repère le `cmp`, les sauts, les deux branches.

**Défi :** Écris un `.c` avec une **boucle `for` qui calcule une somme**. Compile en `-O0` et en `-O2`. Compare. Note les différences.

## 🧩 Mini-projet (chapitre 22) — Reverse mental

Écris en C un petit programme avec :

- Une fonction `f(int a, int b)` qui retourne `a * a + b`.
- Un `main` qui appelle `f(3, 4)` et affiche le résultat avec `printf`.

Compile en `-O0`. **Avant de lire le `.s`**, écris sur papier ce que tu **t'attendrais** à voir comme ASM (prologue, calculs, call, printf, épilogue).

Compare avec le `.s` réel. **Mesure ton intuition.**

## ✅ Tu sais maintenant…

- Compiler un C en ASM avec **`gcc -O0 -masm=intel -S`**
- Reconnaître les **patterns du compilateur** : prologue, locales, if, boucle, appel
- Comprendre que **les optimisations transforment le code**
- Préférer **`-O0`** pour apprendre le reverse
- Utiliser **Godbolt** pour s'entraîner
- Faire le pont entre **C** (que tu comprends grosso modo) et **ASM**

Ce chapitre est ton pont vers la **partie IX**, où tu vas plonger dans les binaires compilés sans avoir le `.c` sous les yeux.

---

## 🚩 Checkpoint — Fin de la Partie VIII (avant le reverse)

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

## 🧭 Méthode — Lire un désassemblage sans paniquer

Quand tu ouvres `objdump -d` sur un binaire pour la première fois, tu vois **des centaines de lignes**. Pas de panique. Voici une méthode en **5 étapes** à appliquer systématiquement :

### Étape 1 — Repérer les chaînes

```bash
strings ./binaire
```


Les chaînes te donnent des **indices énormes** : messages d'erreur, prompts, formats `printf`, parfois des mots de passe en clair. Note celles qui ont l'air pertinentes.

### Étape 2 — Repérer les appels libc

Cherche dans le désassemblage les `call <nom>@plt` :

- `printf@plt`, `puts@plt` → affichage.
- `scanf@plt`, `fgets@plt` → lecture utilisateur.
- **`strcmp@plt`, `memcmp@plt` → comparaison, souvent d'un mot de passe**.
- `malloc@plt`, `free@plt` → gestion mémoire.
- `system@plt`, `execve@plt` → exécution de commandes (méfiance).

C'est ta carte du programme.

### Étape 3 — Repérer `main`

Si le binaire n'est pas strippé : `nm ./bin | grep main`.

Sinon : passe par `_start` → `__libc_start_main` → l'adresse passée dans `rdi` juste avant. (Méthode vue au chapitre 23.)

### Étape 4 — Repérer conditions et boucles

Une fois dans `main`, balaye :

- Les **`cmp` + saut conditionnel vers une adresse en aval** → conditions (`if`).
- Les **sauts (conditionnels ou non) vers une adresse en amont** → boucles.
- Les **`call`** → appels de sous-fonctions à explorer ensuite.

### Étape 5 — Renommer mentalement (ou dans un cahier)

À mesure que tu comprends, **donne des noms** aux choses :

- `[rbp - 4]` → tu as compris que c'est un compteur ? Appelle-le `i` dans ta tête.
- `[rbp - 16]` → un buffer ? Appelle-le `password_buf`.
- `0x401200` (fonction sans nom) → appelle-la `check_password`.

> **C'est exactement ce que font Ghidra et IDA automatiquement.** Mais même à la main, ça transforme un désassemblage cryptique en un programme compréhensible. Garde un cahier ou un fichier `notes.md` à côté pendant tes analyses.

---

## 🔍 Boîte à patterns — ASM pour le reverse

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
