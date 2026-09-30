---
title: PARTIE IX — LECTURE DE BINAIRES ET REVERSE DÉBUTANT
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 9
chapters: 10
---

---


## Chapitre 23 — Désassembler un binaire ELF

### Le minimum à savoir

#### Le grand changement

Jusqu'ici, tu **écrivais** du code et tu en **observais** l'exécution. À partir d'ici, on **inverse** : tu reçois un binaire **sans le code source**, et tu dois comprendre ce qu'il fait. C'est le **reverse engineering**.

> **Le reverse débutant, c'est lire du code.** Pas écraser, pas modifier, pas exploiter. Juste **comprendre**.

#### Le format ELF

Sous Linux, **les exécutables binaires natifs sont généralement au format ELF** (Executable and Linkable Format) — les scripts (`#!/bin/bash`, `#!/usr/bin/env python3`, etc.) sont une autre histoire, gérée par le noyau via le shebang. C'est un format structuré, divisé en **sections** que tu connais déjà (`.text`, `.data`, …) et en **segments** (utilisés au chargement en mémoire).

#### Les 5 outils essentiels

| Outil | Rôle |
|-------|------|
| **`file`** | Identifier le type d'un fichier |
| **`strings`** | Extraire les chaînes lisibles d'un binaire |
| **`readelf`** | Inspecter la structure ELF (entêtes, sections, symboles) |
| **`nm`** | Lister les **symboles** (noms de fonctions, variables) |
| **`objdump`** | **Désassembler** un binaire en assembleur |

Ils sont tous fournis par `binutils` (déjà installé au chapitre 4).

#### `file` : qu'est-ce que c'est ?

```bash
$ file ./hello
hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, ...
```

Tu apprends :
- **ELF** : c'est bien un exécutable Linux.
- **64-bit, x86-64** : architecture.
- **dynamically linked** : il dépend de bibliothèques (libc, …). L'opposé serait **statically linked** (autonome).

#### `strings` : les chaînes en clair

```bash
$ strings ./hello
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__libc_start_main
GLIBC_2.34
Bonjour le monde !
GCC: (Ubuntu 11.4.0) ...
```

Les **chaînes affichables** apparaissent. Si un mot de passe ou un message d'erreur est en clair, tu le verras ici. **Premier réflexe en CTF.**

#### `readelf -h` : l'entête ELF

```bash
$ readelf -h ./hello
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 ...
  Class:                             ELF64
  Type:                              EXEC (Executable file)
  Entry point address:               0x401040
  ...
```

Important :
- **Entry point address** : adresse où le programme commence (le `_start`).
- **Class** : 64 bits (ELF64) ou 32 bits (ELF32).
- **Type** : EXEC, DYN, …

#### `readelf -S` : les sections

```bash
$ readelf -S ./hello
There are 30 section headers, starting at offset 0x3938:

Section Headers:
  [Nr] Name              Type             Address           Size
  [ 1] .interp           PROGBITS         0x000000000040038c
  [ 2] .note.gnu.property NOTE             0x00000000004003a8
  ...
  [12] .text             PROGBITS         0x0000000000401040    ← le code !
  [16] .rodata           PROGBITS         0x0000000000402000    ← les chaînes
  [22] .data             PROGBITS         0x0000000000404010    ← données initialisées
  [23] .bss              NOBITS           0x0000000000404020    ← données vides
```

| Section | Contenu | Permissions |
|---------|---------|-------------|
| **`.text`** | Code exécutable | Lecture + exécution |
| **`.rodata`** | Données en lecture seule (constantes, chaînes littérales) | Lecture seule |
| **`.data`** | Variables globales initialisées | Lecture + écriture |
| **`.bss`** | Variables globales non initialisées | Lecture + écriture |
| **`.plt`** / **`.got`** | Tables pour les appels libc | Spécial |

#### `nm` : lister les symboles

```bash
$ nm ./hello
                 U __libc_start_main@GLIBC_2.34    ← fonction externe
0000000000404020 B __bss_start
0000000000401040 T _start                          ← point d'entrée
0000000000402000 R msg                             ← variable globale
0000000000401140 T main                            ← fonction main
0000000000401130 T addition                        ← une autre fonction
```

Lettres : **T** = code (`.text`), **R** = lecture seule, **B** = `.bss`, **U** = undefined (importé).

#### Binaire strippé : quand les symboles disparaissent

```bash
$ strip ./hello       # enlève tous les symboles internes
$ nm ./hello
nm: ./hello: no symbols
```

Un binaire **strippé** garde ses fonctions, mais **sans nom** dans `nm`. Tu verras juste des adresses (`sub_401130`) en désassemblage. C'est **le cas courant** des binaires en production. Plus dur à reverser.

#### `objdump -d -M intel` : le désassemblage

```bash
$ objdump -d -M intel ./hello
```

L'option **`-M intel`** est **cruciale** : sans elle, c'est de l'AT&T (cryptique). Sortie (extrait) :

```
0000000000401140 <main>:
  401140:       55                  push   rbp
  401141:       48 89 e5            mov    rbp,rsp
  401144:       48 8d 3d b9 0e 00..  lea    rdi, [rip+0xeb9]    # 402004 <msg>
  40114b:       e8 e0 fe ff ff      call   401030 <puts@plt>
  401150:       b8 00 00 00 00      mov    eax, 0x0
  401155:       5d                  pop    rbp
  401156:       c3                  ret
```

Lis-le comme tu lis ton propre code :
- **Adresses** : `401140`, `401141`, …
- **Opcodes** (octets bruts) : `55`, `48 89 e5`, …
- **Mnémoniques** (instructions lisibles) : `push rbp`, `mov rbp, rsp`, …
- **Commentaires automatiques** : `# 402004 <msg>` (l'adresse pointée est nommée).

> **Tu reconnais tout ?** Le prologue (`push rbp ; mov rbp, rsp`), un `lea` pour charger l'adresse d'une chaîne, un `call puts@plt` (appel à puts via la PLT), l'épilogue (`pop rbp ; ret`). **Exactement** ce que tu as appris.

### Très utile en pratique

#### Trouver `main` dans un binaire

Si `nm` montre `main`, super. Sinon (binaire strippé) :

1. Cherche le **point d'entrée** : `readelf -h` te donne l'adresse (c'est `_start`).
2. **Attention :** sous Linux avec la libc, `_start` n'appelle **pas** directement `main`. Il prépare les arguments puis appelle **`__libc_start_main`**, qui se charge d'appeler `main` ensuite.
3. L'adresse de `main` est généralement passée en **premier argument** à `__libc_start_main`, donc dans **`rdi`** (convention System V).
4. En désassemblage, cherche dans `_start` une instruction du type :
   ```
   mov  rdi, <adresse>        ; ← adresse de main
   ; ou
   lea  rdi, [rip + ...]
   ```
   juste avant `call __libc_start_main@plt`. Cette adresse, c'est `main`.

Exemple typique dans `_start` :

```
   ...
   lea  rdi, [rip + 0x101]    ← main ! (l'adresse calculée pointe sur main)
   ...
   call __libc_start_main@plt
```

#### Filtrer le désassemblage à une fonction

```bash
objdump -d -M intel --disassemble=main ./hello
```

Cible une seule fonction. Indispensable quand le binaire est gros.

#### Désassembler la section `.text` seule

```bash
objdump -d -M intel ./hello | less
```

Avec `| less`, tu peux scroller. Cherche `main` avec `/main` puis Entrée.

#### Voir les chaînes contextualisées

```bash
objdump -s -j .rodata ./hello
```

Affiche le **contenu hex + ASCII** de la section `.rodata`. Tu vois exactement quelles constantes sont stockées et où.

### Bonus

#### Pourquoi `puts@plt` et pas juste `puts` ?

`puts` est dans la **libc**, chargée dynamiquement. Le binaire ne contient pas le code de `puts` — juste un **stub** dans la section `.plt` qui sait où trouver `puts` à l'exécution. D'où le `@plt` (Procedure Linkage Table).

C'est un détail technique mais c'est le genre de chose qu'on rencontre **tout le temps** en reverse. Mémorise juste : `<fonction>@plt` = un appel à une fonction libc.

#### `radare2` : pour les curieux

`radare2` (commande `r2`) est un outil de reverse engineering interactif plus puissant que `objdump`. Très utile pour les CTF. Hors scope de ce cours, mais à explorer ensuite.

#### `ghidra` et `IDA` : les pros

Ces outils proposent du **désassemblage interactif avec décompilation** : ils te montrent l'ASM **et** une approximation du C correspondant. Magnifique mais gros à apprendre. Pour plus tard.

### ❌ Erreur classique

```
Oublier -M intel
→ Tu te retrouves avec mov %rax, %rbx (AT&T) au lieu de mov rbx, rax.
   Apprendre AT&T juste pour ça est inutile.

Chercher un main dans un binaire strippé sans le repérer via _start
→ Sans symboles, suis le call du _start.

Confondre l'adresse virtuelle (à l'exécution) et l'offset fichier
→ objdump affiche l'adresse virtuelle (0x401140), pas l'offset dans le .ELF.

Croire que tout le code est dans .text
→ Les fonctions C peuvent appeler la libc (via PLT). Les "_init", "_fini"
   font partie des sections initialisation.

Lire les opcodes au lieu des mnémoniques
→ Les opcodes (55, 48 89 e5) sont là pour info. Ce qui compte, c'est
   les mnémoniques (push rbp, mov rbp, rsp).
```

### Exercices

**Guidé :** Recompile l'un de tes propres programmes (par exemple `hello_c.asm` du ch. 21) et applique successivement :
- `file ./hello_c`
- `strings ./hello_c`
- `nm ./hello_c`
- `readelf -h ./hello_c`
- `objdump -d -M intel ./hello_c | less`

Identifie le `main`, le prologue, l'épilogue, le `call printf@plt`.

**Autonome :** Écris un petit `.c` avec une fonction `secret` qui contient une chaîne `"motdepasse123"` (juste en local : `char s[] = "motdepasse123";`). Compile. **Avant de lancer le programme**, retrouve la chaîne via `strings ./prog`.

**Défi :** Sur le même binaire, lance `strip ./prog`, puis refais `nm` et `objdump`. Que vois-tu en moins ? Peux-tu encore retrouver `main` ? (Indice : via le point d'entrée du ELF.)

### ✅ Tu sais maintenant…

- Ce qu'est un **binaire ELF** et ses **sections** (`.text`, `.rodata`, `.data`, `.bss`)
- Utiliser **`file`** pour identifier un binaire
- Utiliser **`strings`** pour extraire ses chaînes
- Utiliser **`readelf -h`** et **`-S`** pour son entête et ses sections
- Utiliser **`nm`** pour ses symboles
- **Désassembler** avec **`objdump -d -M intel`**
- La différence binaire **strippé / non strippé**
- Reconnaître **`fonction@plt`** pour les appels libc

---


## Chapitre 24 — Reverse engineering débutant avec GDB

### Le minimum à savoir

#### Le reverse dynamique vs statique

Tu peux analyser un binaire de deux façons :

| Approche | Outils | Avantage |
|----------|--------|----------|
| **Statique** | `strings`, `objdump`, ghidra | Tu lis sans exécuter |
| **Dynamique** | `gdb`, `ltrace`, `strace` | Tu vois le programme tourner |

Tu maîtrises déjà les bases du statique (ch. 23). Maintenant : le **dynamique avec GDB**, qui complète parfaitement. Souvent, on **combine** les deux : on lit avec objdump, on vérifie avec GDB.

#### Charger un binaire inconnu

```bash
gdb ./inconnu
```

Si le binaire est strippé, certaines commandes auront moins d'info. Mais l'essentiel marche pareil.

#### Poser des breakpoints sur des adresses

Sans symboles, tu casses sur des **adresses** :

```
(gdb) break *0x401140        ; étoile + adresse
```

Avec symboles, tu peux casser sur des **noms** :

```
(gdb) break main
(gdb) break printf
```

Tu peux aussi casser sur tous les `call` d'une fonction :

```
(gdb) disas main
; repère les "call ..." → casse à chacune si nécessaire
```

#### `start` : casser au tout début

```
(gdb) start
```

Si le binaire a un `main`, GDB s'arrête à son tout début. C'est l'équivalent de `break main ; run`. Pratique.

#### Observer un programme en cours d'exécution

Une fois arrêté à un breakpoint :

| Commande | Effet |
|----------|-------|
| `disas` | Désassembler autour de `$rip` |
| `info registers` | Voir tous les registres |
| `x/s $rdi` | Si `rdi` est un pointeur sur une chaîne, l'afficher |
| `x/10gx $rsp` | Voir la pile |
| `stepi` (`si`) | 1 instruction (entre dans les call) |
| `nexti` (`ni`) | 1 instruction (passe par-dessus les call) |
| `continue` (`c`) | Continuer jusqu'au prochain break |
| `finish` | Sortir de la fonction courante |

#### Repérer un `if` dans le désassemblage

Voici un schéma. Tu vois :

```
0x401200:  cmp    DWORD PTR [rbp-4], 0x2a
0x401204:  jne    0x401218
0x401206:  mov    eax, 0x1
0x40120b:  jmp    0x40121d
0x401218:  mov    eax, 0x0
0x40121d:  ...
```

**Décodage :**
- `cmp [rbp-4], 42` → on compare une variable locale à 42.
- `jne 0x401218` → si différent, saute au "else".
- Sinon : `eax = 1` puis saut au "fin".
- `0x401218:` (else) : `eax = 0`.

C'est `if (var == 42) return 1; else return 0;`.

#### Repérer une boucle dans le désassemblage

```
0x401300:  mov    rcx, 0
0x401307:  ; ...
0x40130d:  cmp    rcx, 0xa
0x401311:  jge    0x401330
0x401317:  ; ... corps ...
0x40131d:  inc    rcx
0x401320:  jmp    0x40130d        ← saut ARRIÈRE
0x401330:  ; ...
```

**Indice clé : le `jmp 0x40130d` saute en arrière** vers une adresse plus basse. C'est **un indice très fort** d'une boucle (et de loin le cas le plus fréquent en pratique).

#### Repérer un appel de fonction et ses arguments

```
0x401400:  mov    edi, 0x5         ← 1er arg
0x401405:  mov    esi, 0xa         ← 2ème arg
0x40140a:  call   0x401200 <calc>  ← appel
0x40140f:  mov    [rbp-8], eax     ← stocker le retour
```

**Décodage :** appel de `calc(5, 10)`, résultat stocké dans une locale.

#### Suivre une comparaison de mot de passe

Voici **l'objet d'un crackme classique** :

```
0x401500:  mov    rdi, ADDR1        ; ton entrée
0x401507:  mov    rsi, ADDR2        ; le mot de passe en mémoire
0x40150e:  call   strcmp@plt
0x401513:  test   eax, eax
0x401515:  jne    mauvais
0x40151b:  ; ... "Bon mot de passe !" ...
mauvais:
0x401530:  ; ... "Mauvais !" ...
```

**Si tu vois `strcmp`** → le mot de passe est probablement comparé brut. Examine ce qu'il y a à `ADDR2` (avec `x/s 0x...`). Bingo. Si c'est `memcmp`, idem.

### Très utile en pratique

#### Forcer une condition pour explorer

Tu veux **voir** la branche "succès" sans connaître le mot de passe ? Avant le `jne`, force le flag :

```
(gdb) set $eflags |= (1 << 6)     ; force ZF = 1 → ils sont "égaux"
```

Ou plus simple : **modifie l'instruction de saut**. Mais c'est du patching, hors scope.

Plus simple encore : casse **après** le `jne`, force `$rip` à la bonne adresse :

```
(gdb) set $rip = 0x40151b      ; saute directement au "bon" message
(gdb) continue
```

#### Examiner ce qui est dans `rdi` quand `printf` est appelé

Pose un breakpoint sur `printf` et regarde le format :

```
(gdb) break printf
(gdb) continue
; ... arrive sur printf ...
(gdb) x/s $rdi
0x402004: "Saisis un mot de passe : "
```

Tu vois ce que **`printf` est sur le point d'afficher**, sans laisser tourner le programme. Très instructif.

#### Voir ce que `read`/`scanf` reçoit

Casse après `read` ou `scanf` et regarde le buffer :

```
(gdb) x/s <adresse_buffer>
```

Tu vois ce que l'utilisateur a tapé (idéal pour comprendre comment le programme traite l'entrée).

### Bonus

#### `ltrace` et `strace`

Deux outils hors GDB :

- `strace ./prog` : affiche tous les **syscalls** que le programme fait. Tu vois `write(1, "...", 5)`, `read(0, ...)`, etc.
- `ltrace ./prog` : affiche tous les appels à des fonctions de la **libc**.

Pour un débutant qui veut comprendre **vite** ce qu'un binaire fait, c'est une mine d'or.

```bash
ltrace ./crackme
strcmp("monessai", "secret123") = -1
```

Devine quoi : tu viens de **trouver le mot de passe**.

### ❌ Erreur classique

```
Poser break main sur un binaire qui n'a pas le symbole main
→ Erreur "Function main not defined". Utilise break *0x... ou "start" si possible.

Utiliser step (et pas stepi) sur du binaire sans source
→ step suit les lignes source, qui n'existent pas. Toujours stepi/nexti.

Confondre stepi et nexti
→ stepi entre dans les call. nexti passe par-dessus. Choisis selon le besoin.

Croire qu'un saut vers une adresse plus haute = pas une boucle
→ Faux. Une boucle EST un saut arrière. Vérifie le sens (jXX vers plus bas).

Modifier rip à n'importe quelle adresse
→ Tu peux atterrir au milieu d'une instruction. Crash garanti. Choisis
  une adresse alignée sur le début d'une instruction.

Lire la pile sans connaître l'ABI
→ Sans la convention System V en tête, on ne sait pas où sont les args.
```

### Exercices

**Guidé :** Reprends un de tes binaires (`hello_c` du ch. 21). Lance `gdb ./hello_c`, fais `start`, puis `disas main`, puis `nexti` plusieurs fois en regardant `rdi` à chaque appel à `printf`.

**Autonome :** Compile un petit C qui demande un nombre et **affiche "OK" si == 42, sinon "KO"**. Sans regarder le `.c`, retrouve dans GDB où se trouve le `cmp ..., 42`.

**Défi :** Compile un petit C avec un mot de passe `"secret"` comparé par `strcmp`. Lance-le dans GDB, casse sur `strcmp`, et **affiche le 2ème argument** (le mot de passe attendu) avec `x/s $rsi`.

### 🧩 Mini-projets finaux — 3 Crackmes progressifs

Voici trois **mini-binaires** à reverser. Pour chacun, ton boulot : **trouver le mot de passe**.

Tu peux toi-même les **fabriquer** en compilant les sources C ci-dessous (ce qui te donne un terrain d'entraînement reproductible). En CTF, tu n'aurais que le binaire — mais le but pédagogique est le même.

#### Crackme 1 — Le mot de passe en clair (`strings` suffit)

**Code source (`crackme1.c`) :**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Mot de passe : ");
    scanf("%63s", input);
    if (strcmp(input, "OpenSesame") == 0)
        printf("Bravo !\n");
    else
        printf("Refuse.\n");
    return 0;
}
```

**Compile et joue :**

```bash
gcc -O0 -no-pie crackme1.c -o crackme1
```

**Mission :**
1. Sans regarder le `.c` (imagine que tu ne l'as pas).
2. `strings ./crackme1` → trouve le mot de passe.
3. Vérifie : `./crackme1` → tape-le → ça affiche "Bravo !".

#### Crackme 2 — Comparaison caractère par caractère

**Code source (`crackme2.c`) :**

```c
#include <stdio.h>

int main() {
    char input[8];
    printf("Code : ");
    scanf("%7s", input);

    if (input[0] != 'X') goto faux;
    if (input[1] != 'A') goto faux;
    if (input[2] != 'B') goto faux;
    if (input[3] != 'C') goto faux;
    if (input[4] != '\0') goto faux;
    printf("Bravo !\n");
    return 0;
faux:
    printf("Refuse.\n");
    return 1;
}
```

```bash
gcc -O0 -no-pie crackme2.c -o crackme2
```

**Mission :**
1. `strings ./crackme2` ne donne rien d'utile (les caractères sont éparpillés).
2. `objdump -d -M intel ./crackme2 | less`, cherche `main`.
3. Repère les **plusieurs `cmp ... , 0x??`** (comparaisons à des octets précis).
4. Reconstitue le mot de passe en convertissant les valeurs hexa en ASCII.
5. Vérifie.

> **Indice :** `0x58 = 'X'`, `0x41 = 'A'`, `0x42 = 'B'`, `0x43 = 'C'`. Le mot de passe est `XABC`.

#### Crackme 3 — Transformation XOR simple

**Code source (`crackme3.c`) :**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char input[8];
    char attendu[] = {0x18, 0x05, 0x07, 0x02, 0x00};   // chiffré
    char cle = 0x42;

    printf("Code : ");
    scanf("%7s", input);

    for (int i = 0; i < 4; i++)
        input[i] ^= cle;

    if (memcmp(input, attendu, 4) == 0)
        printf("Bravo !\n");
    else
        printf("Refuse.\n");
    return 0;
}
```

```bash
gcc -O0 -no-pie crackme3.c -o crackme3
```

**Mission :**
1. Lance dans GDB. Casse sur `main`. `disas main`.
2. Tu vois une **boucle** (saut arrière) qui XORe chaque octet.
3. Identifie la **clé XOR** (cherche `0x42` dans le code, ou pose un breakpoint et regarde un registre).
4. Identifie les **octets attendus** (cherche un tableau initialisé : `0x18, 0x05, 0x07, 0x02`).
5. **Inverse l'opération** : applique `^= 0x42` aux octets attendus pour retrouver l'entrée correcte.
   - `0x18 ^ 0x42 = 0x5A = 'Z'`
   - `0x05 ^ 0x42 = 0x47 = 'G'`
   - `0x07 ^ 0x42 = 0x45 = 'E'`
   - `0x02 ^ 0x42 = 0x40 = '@'`
6. Le mot de passe est `ZGE@`.
7. Vérifie : `./crackme3` → tape `ZGE@` → "Bravo !".

> **Méthode XOR :** la propriété clé est `(a XOR k) XOR k = a`. Donc si l'entrée est XORée avec une clé puis comparée, **on inverse en XORant la valeur attendue avec la même clé**.

### ✅ Tu sais maintenant…

- Lancer un binaire **inconnu** dans GDB
- Poser un breakpoint sur **adresse** ou sur **nom**
- Naviguer avec **`start`, `stepi`, `nexti`, `continue`, `finish`**
- **Repérer un `if`** : `cmp + jXX` vers une adresse plus haute
- **Repérer une boucle** : `cmp + jXX` vers une adresse plus basse
- **Repérer un appel** : `mov edi, ... ; call ...`
- Suivre les **arguments** passés à `printf`, `scanf`, `strcmp`
- **Forcer un saut** avec `set $rip` pour explorer
- Résoudre des **mini-crackmes** : mot de passe en clair, comparaison caractère par caractère, transformation XOR

🎉 **Bravo. Tu sais maintenant lire et reverser un petit binaire.** Tu es prêt pour des CTF de catégorie reverse débutant.

---
