---
title: PARTIE III — REGISTRES, CALCULS ET OBSERVATION
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 3
chapters: 10
---

---


## Chapitre 7 — Déplacer des données avec `mov`

### Le minimum à savoir

#### L'instruction la plus importante de l'assembleur

`mov` est l'instruction que tu vas écrire **le plus souvent**. Elle sert à **copier** une valeur d'un endroit à un autre.

> **Attention au nom !** `mov` vient de "move", mais en réalité, **c'est une copie, pas un déplacement**. La source garde sa valeur. C'est trompeur, mais c'est comme ça historiquement.

#### Les 4 formes de `mov`

| Forme | Exemple | Ce que ça fait |
|-------|---------|----------------|
| immédiate → registre | `mov rax, 42` | `rax = 42` |
| registre → registre | `mov rax, rbx` | `rax = rbx` (rbx inchangé) |
| mémoire → registre | `mov rax, [var]` | `rax = contenu à l'adresse var` |
| registre → mémoire | `mov [var], rax` | `var en mémoire = rax` |

#### La règle qui te suivra partout : pas de mémoire → mémoire (avec `mov`)

**Tu ne peux PAS faire :**

```nasm
mov [a], [b]     ; ❌ INTERDIT
```

Cette instruction n'existe pas en x86-64. Il **faut toujours passer par un registre** :

```nasm
mov rax, [b]     ; charger b dans rax
mov [a], rax     ; ranger rax dans a
```

> **Règle pédagogique :** pour les instructions courantes (`mov`, `add`, `cmp`, `sub`, …), tu **ne peux pas** manipuler **deux opérandes mémoire explicites** en même temps.
>
> **Nuance :** il existe des instructions spécialisées de **copie mémoire-à-mémoire** comme `movsb`, `movsq`, `rep movsb` qui passent par des registres **implicites** (`rsi`, `rdi`, `rcx`). Tu les croiseras en reverse (souvent dans `memcpy` ou `strcpy` optimisés), mais on ne les utilisera pas dans ce cours.

#### Choisir la bonne taille

`mov` ne sait pas tout seul si tu veux copier 1, 2, 4 ou 8 octets. Tu lui dis avec la **taille du registre** :

```nasm
mov rax, 5       ; 8 octets (qword)
mov eax, 5       ; 4 octets (dword)
mov ax,  5       ; 2 octets (word)
mov al,  5       ; 1 octet  (byte)
```

Pour la mémoire sans registre, tu dois préciser :

```nasm
mov byte  [var], 5     ; 1 octet
mov word  [var], 5     ; 2 octets
mov dword [var], 5     ; 4 octets
mov qword [var], 5     ; 8 octets
```

Sinon NASM se plaint : *"operation size not specified"*.

#### `mov rax, var` vs `mov rax, [var]`

C'est **la** confusion classique du débutant. Lis attentivement :

```nasm
section .data
    var dq 42

section .text
    mov rax, var      ; rax = ADRESSE de var (un nombre genre 0x404000)
    mov rax, [var]    ; rax = CONTENU à cette adresse  → rax = 42
```

Les crochets `[…]` veulent dire **"le contenu à l'adresse"**. Sans crochets, on a juste l'**adresse**.

### Très utile en pratique

#### Exemple détaillé avec plusieurs mov

```nasm
; mov_demo.asm — Démonstration des différentes formes de mov

section .data
    valeur dq 100

section .text
global _start

_start:
    mov rax, 42         ; rax = 42  (immédiate)
    mov rbx, rax        ; rbx = 42  (registre → registre)
    mov rcx, [valeur]   ; rcx = 100 (mémoire → registre)
    mov [valeur], rax   ; valeur en mémoire = 42 (registre → mémoire)
    mov rdx, valeur     ; rdx = adresse de valeur (un grand nombre)

    ; quitter
    mov rax, 60
    mov rdi, 0
    syscall
```

Tu ne **vois rien** quand tu exécutes ce programme. **C'est normal.** Au chapitre 9, on l'observera dans GDB pour voir tous les registres bouger.

#### Les sous-registres en pratique

Reprends l'exemple du chapitre 2 :

```nasm
mov rax, 0                  ; rax = 0
mov al, 0xFF                ; al = 0xFF, donc rax = 0x00000000000000FF
```

Mais **attention** à un comportement piège en x86-64 :

```nasm
mov rax, 0x1234567890ABCDEF
mov eax, 5                  ; rax = 0x0000000000000005 (la partie haute est ZÉRO !)
```

> **Règle x86-64 :** écrire dans la version **32 bits** (`eax`, `ebx`, etc.) **efface automatiquement les 32 bits supérieurs**. Écrire dans les versions 8 et 16 bits, par contre, n'efface rien. C'est un piège.

### Bonus

#### Réponse au défi du chapitre 2

Si `rax` valait `0x1234567890ABCDEF` et qu'on fait `mov al, 0xFF`, alors `rax` devient `0x1234567890ABCDFF`. Seuls les 8 bits bas changent.

#### `mov` ne change jamais les flags

À l'inverse de `add` ou `sub`, l'instruction `mov` **ne modifie pas les flags du CPU**. On peut donc enchaîner plusieurs `mov` sans perdre l'état d'une comparaison faite avant. On reverra ça au chapitre 16.

### ❌ Erreur classique

```
Croire que mov "déplace" la source
→ Faux. mov COPIE. La source garde sa valeur.

Faire mov [a], [b]
→ Interdit en x86-64. Passe par un registre.

Oublier les crochets : mov rax, var au lieu de mov rax, [var]
→ Tu charges l'ADRESSE au lieu du CONTENU.

Ne pas spécifier la taille pour la mémoire
→ NASM crie : "operation size not specified".

Mélanger les tailles : mov rax, eax
→ Inconsistant. NASM crie : "mismatch in operand sizes".

Oublier que mov eax, 0 efface aussi les 32 bits hauts de rax
→ Piège classique. mov al, 0 ne fait pas pareil.
```

### Exercices

**Guidé :** Recopie et compile cet exemple. Tu n'auras pas de sortie visible (normal) :

```nasm
section .data
    a dq 10
    b dq 20

section .text
global _start
_start:
    mov rax, [a]
    mov rbx, [b]
    mov rcx, rax
    mov rdx, rbx
    mov rax, 60
    mov rdi, 0
    syscall
```

**Autonome :** Sans exécuter, **prédis sur papier** la valeur de `rax`, `rbx`, `rcx` après chaque ligne :

```nasm
mov rax, 100
mov rbx, 200
mov rcx, rax
mov rax, rbx
mov rbx, rcx
```

> **Question :** qu'est-ce que ce code vient de faire ? (Réponse en bas.)

**Défi :** Réécris ces lignes en assembleur :
- Python : `x = 5`, `y = 10`, `z = x`
- Suppose que `x`, `y`, `z` sont déclarés en `.data` avec `dq 0`.

> **Réponse autonome :** ce code **échange `rax` et `rbx`** (swap). C'est un pattern classique.

### ✅ Tu sais maintenant…

- Les **4 formes de `mov`** (immédiate, registre, mémoire, ou inverse)
- La règle d'or : **pas de mémoire → mémoire directe**
- La différence cruciale **`var`** (adresse) vs **`[var]`** (contenu)
- Comment **choisir la taille** (`rax`, `eax`, `al`, ou `byte/word/dword/qword`)
- Le **piège du 32 bits** qui efface les bits hauts
- Faire un **swap** entre deux registres

---


## Chapitre 8 — Calculer avec les registres

### Le minimum à savoir

#### L'arithmétique de base

L'assembleur sait faire les 4 opérations classiques, plus quelques instructions utiles :

| Instruction | Effet | Exemple |
|-------------|-------|---------|
| **`add`** | addition | `add rax, rbx` → `rax = rax + rbx` |
| **`sub`** | soustraction | `sub rax, rbx` → `rax = rax - rbx` |
| **`inc`** | incrémenter de 1 | `inc rax` → `rax = rax + 1` |
| **`dec`** | décrémenter de 1 | `dec rax` → `rax = rax - 1` |
| **`neg`** | négation (opposé) | `neg rax` → `rax = -rax` |
| **`imul`** | multiplication signée | `imul rax, rbx` → `rax = rax * rbx` |

> **Format identique à `mov` :** destination à gauche, source à droite. La destination reçoit le résultat.

#### Exemple complet

```nasm
section .text
global _start
_start:
    mov rax, 10
    mov rbx, 3
    add rax, rbx       ; rax = 10 + 3 = 13
    sub rax, 5         ; rax = 13 - 5 = 8
    inc rax            ; rax = 9
    dec rax            ; rax = 8
    imul rax, rbx      ; rax = 8 * 3 = 24
    neg rax            ; rax = -24

    ; on sort avec rax en code de retour (cf. ci-dessous)
    mov rdi, rax       ; copie le résultat dans rdi
    mov rax, 60        ; syscall exit
    syscall
```

> **Astuce pédagogique :** comme on ne sait pas encore afficher un nombre proprement (il faut le convertir en texte, ch. 14), on **utilise le code de retour comme canal de sortie** pour vérifier nos calculs.

Compile, exécute, regarde :

```bash
make calcul
./calcul
echo $?              # → 232  (parce que -24 en non signé sur 8 bits = 232)
```

Le code de retour est limité à 0-255 (8 bits non signés). Pour des résultats simples, ça suffit largement.

#### La multiplication : `imul`

```nasm
mov rax, 6
mov rbx, 7
imul rax, rbx        ; rax = 42
```

Tu peux aussi faire :

```nasm
imul rax, rbx, 5     ; rax = rbx * 5  (trois opérandes !)
imul rax, 3          ; rax = rax * 3
```

> **`imul` vs `mul` :** `imul` est la multiplication **signée** (qui gère les nombres négatifs correctement). `mul` est la version non signée, à 1 opérande, et plus pénible. **Utilise `imul` par défaut.**

#### La division : `idiv` (prudemment)

`idiv` est plus tordue. Elle divise un nombre **128 bits** (formé par `rdx:rax`) par son opérande.

```nasm
mov rax, 100
mov rdx, 0          ; ESSENTIEL pour des nombres POSITIFS : partie haute à 0
mov rbx, 7
idiv rbx            ; rax = 100 / 7 = 14, rdx = 100 % 7 = 2
```

**Avant un `idiv`, il faut préparer `rdx` :**

- Pour un dividende **positif** (le cas habituel en pédagogie) : `mov rdx, 0` ou `xor rdx, rdx`.
- Pour un dividende **signé** qui peut être négatif : utilise **`cqo`**. Cette instruction étend le bit de signe de `rax` dans `rdx` (donc `rdx` devient `0` si `rax > 0`, ou `0xFFFFFFFFFFFFFFFF` si `rax < 0`).

```nasm
mov rax, -100
cqo                 ; rdx = 0xFFFFFFFFFFFFFFFF (extension du signe)
mov rbx, 7
idiv rbx            ; rax = -100 / 7 = -14, rdx = -2
```

> **Piège classique :** si tu mets `rdx = 0` alors que `rax` est négatif, le CPU interprète `rdx:rax` comme un énorme nombre positif. Résultat erroné garanti. **Avec `idiv` et des négatifs, toujours `cqo`.**

| Après `idiv` | Contenu |
|--------------|---------|
| `rax` | **quotient** |
| `rdx` | **reste** (modulo) |

### Très utile en pratique

#### Pourquoi pas d'affichage du résultat ?

Afficher un entier nécessite de le **convertir en texte** (chiffre par chiffre, en ASCII). On apprend cette conversion au chapitre 14. Pour l'instant :
- Soit on utilise `mov rdi, rax` puis `exit` pour voir le résultat dans `echo $?`.
- Soit on regarde dans GDB (chapitre suivant).

#### Récapitulatif des opérandes

| Instruction | Opérandes valides |
|-------------|-------------------|
| `add rax, 5` | registre, immédiate ✓ |
| `add rax, rbx` | registre, registre ✓ |
| `add rax, [var]` | registre, mémoire ✓ |
| `add [var], rax` | mémoire, registre ✓ |
| `add [a], [b]` | ❌ INTERDIT comme pour `mov` |

La règle "pas de mémoire-à-mémoire directe" vaut pour **toutes** les instructions arithmétiques.

#### Comparer avec Python

| Python | Assembleur |
|--------|------------|
| `a = 5` | `mov rax, 5` |
| `a = b` | `mov rax, rbx` |
| `a += b` | `add rax, rbx` |
| `a -= b` | `sub rax, rbx` |
| `a *= b` | `imul rax, rbx` |
| `a, b = b, a` | (chapitre 18 avec push/pop, ou 3 mov via rcx) |

### Bonus

#### `lea` pour des additions rapides

Petite astuce qu'on creuse au chapitre 12 : `lea` permet de faire **`rax = rbx + rcx`** en une instruction :

```nasm
lea rax, [rbx + rcx]    ; rax = rbx + rcx  (sans toucher aux flags)
```

Tu verras `lea` partout en reverse engineering pour cette raison.

### ❌ Erreur classique

```
Croire que le résultat s'affiche
→ Non. On le met dans un registre. Pour voir : GDB ou code de retour.

Écraser un registre dont on a encore besoin
→ Classique : mov rax, calcul ; mov rax, autre_chose → premier résultat perdu.

Oublier rdx = 0 avant idiv
→ Bug silencieux ou crash. À retenir absolument.

Utiliser mul au lieu de imul pour des nombres positifs
→ mul est à 1 opérande et utilise rdx:rax. imul est plus simple.

Croire que add rax, [a], [b] existe
→ Non. add prend exactement 2 opérandes.

Confondre signé et non signé
→ -1 signé = 0xFFFFFFFFFFFFFFFF. En non signé, c'est un énorme nombre.
```

### Exercices

**Guidé :** Écris un programme qui calcule `(5 + 3) * 2` et place le résultat dans le code de retour. Vérifie avec `echo $?` que tu obtiens **16**.

**Autonome :** Écris un programme qui calcule `100 / 3` (quotient dans `rdi`) puis quitte. `echo $?` doit afficher **33**.

**Défi :** Calcule la suite : `((10 - 2) * 3 + 7) / 5`. Donne le résultat via le code de retour.

> **Réponse attendue :** `((10-2)*3+7)/5 = (24+7)/5 = 31/5 = 6` (reste 1).

### 🧩 Mini-projet (chapitres 7-8) — Mini-calculatrice

Écris `calc.asm` qui calcule sans aucune saisie (valeurs codées en dur) :

- Une variable `a dq 50` et `b dq 7`
- Affiche le code de retour égal à `(a + b) - (a / b)`

Étapes :
1. Charge `a` et `b` dans des registres.
2. Calcule `a + b` dans un registre.
3. Calcule `a / b` (attention `rdx = 0`) dans un autre.
4. Soustrais.
5. Mets le résultat dans `rdi` et appelle `exit`.

Résultat attendu : `(50 + 7) - (50 / 7) = 57 - 7 = 50`.

### ✅ Tu sais maintenant…

- Faire **addition, soustraction, multiplication, division**
- Utiliser **`inc`** et **`dec`** pour ±1
- Utiliser **`neg`** pour l'opposé
- La particularité d'**`idiv`** (quotient dans `rax`, reste dans `rdx`, `rdx = 0` avant pour des positifs, **`cqo` pour des signés négatifs**)
- Utiliser le **code de retour** comme canal de sortie temporaire
- Pourquoi on ne **voit pas** encore le résultat à l'écran

---


## Chapitre 9 — GDB pour observer les registres

### Le minimum à savoir

#### Pourquoi GDB tout de suite

Tu codes "à l'aveugle" depuis le chapitre 6. Tu fais `mov rax, 5`, mais tu **ne vois pas** que `rax` vaut 5. GDB, c'est ce qui te permet de **voir** ce que ton programme fait, instruction par instruction.

> **À retenir :** GDB est à l'assembleur ce que `print()` est à Python. C'est **l'outil de visibilité**. Sans lui, tu codes à l'aveugle.

#### Compiler avec les symboles de debug

Pour que GDB t'affiche un maximum d'informations, compile avec `-g -F dwarf` :

```bash
nasm -f elf64 -g -F dwarf mon_prog.asm -o mon_prog.o
ld mon_prog.o -o mon_prog
```

Si tu utilises le Makefile du chapitre 4, c'est déjà fait.

#### Lancer GDB

```bash
gdb ./mon_prog
```

Tu arrives dans le prompt GDB (`(gdb)`). À ce stade, **rien n'est lancé**. Tu prépares la session.

#### Les 7 commandes vitales pour démarrer

| Commande | Raccourci | Effet |
|----------|-----------|-------|
| `break _start` | `b _start` | Pose un **breakpoint** au début |
| `run` | `r` | **Lance** le programme |
| `stepi` | `si` | Avance d'**une instruction** |
| `info registers` | `i r` | Affiche **tous les registres** |
| `print /x $rax` | `p /x $rax` | Affiche `rax` en **hexa** |
| `disassemble` | `disas` | Affiche le **désassemblage** autour de l'instruction courante |
| `quit` | `q` | **Quitter** GDB |

#### Un exemple pas-à-pas

Voici un programme et la session GDB qui va avec.

**Le programme `voir.asm` :**

```nasm
section .text
global _start
_start:
    mov rax, 10
    mov rbx, 32
    add rax, rbx       ; rax devrait valoir 42
    mov rdi, rax
    mov rax, 60
    syscall
```

**La session GDB :**

```
$ gdb ./voir
(gdb) break _start
Breakpoint 1 at 0x401000
(gdb) run
Breakpoint 1, _start () at voir.asm:3
3           mov rax, 10
(gdb) info registers rax rbx
rax  0x0    0
rbx  0x0    0

(gdb) stepi              # exécute mov rax, 10
(gdb) print /x $rax
$1 = 0xa

(gdb) stepi              # exécute mov rbx, 32
(gdb) print /x $rbx
$2 = 0x20

(gdb) stepi              # exécute add rax, rbx
(gdb) print /x $rax
$3 = 0x2a                # 0x2a = 42 ✓

(gdb) quit
```

🎉 Tu as **vu** les registres bouger en temps réel. C'est ça, GDB.

#### Avec pwndbg : encore plus visuel

Si tu as installé pwndbg, à chaque `stepi`, GDB affiche **automatiquement** :
- Les **registres** (avec leur valeur en hexa et décimal).
- Le **désassemblage** autour de l'instruction courante.
- La **pile** (chapitre 18).
- Les **flags** (chapitre 16).

```
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─[ REGISTERS / show-flags off / show-compact-regs off ]──
*RAX  0x2a
 RBX  0x20
 RCX  0x0
 ...
─[ DISASM / x86-64 / set emulate on ]──
   0x401000 <_start>      mov    rax, 0xa
   0x401007 <_start+7>    mov    rbx, 0x20
 ► 0x40100e <_start+14>   add    rax, rbx
   0x401011 <_start+17>   mov    rdi, rax
   ...
```

C'est **beaucoup** plus pédagogique. Installe-le si ce n'est pas fait.

### Très utile en pratique

#### Voir un registre en plusieurs formats

```
(gdb) print $rax          # décimal      → 42
(gdb) print /x $rax       # hexadécimal  → 0x2a
(gdb) print /t $rax       # binaire      → 101010
(gdb) print /c $rax       # caractère    → '*'  (42 = '*')
```

#### Voir la mémoire

```
(gdb) x/10gx 0x404000     # 10 qword en hexa à partir de cette adresse
(gdb) x/10bx &var         # 10 octets en hexa de la variable var
(gdb) x/s &msg            # une chaîne ASCII à partir de msg
```

Le format `x/COUNT SIZE FORMAT` :
- COUNT : combien d'éléments
- SIZE : `b` (byte), `w` (word), `d` (dword), `g` (qword)
- FORMAT : `x` (hexa), `d` (décimal), `s` (chaîne), `c` (caractère)

#### Avancer plus vite

| Commande | Effet |
|----------|-------|
| `stepi` (`si`) | 1 instruction |
| `stepi 5` | 5 instructions |
| `continue` (`c`) | Continuer jusqu'au prochain breakpoint ou la fin |
| `nexti` (`ni`) | 1 instruction, **sans entrer dans les `call`** (utile plus tard) |

#### Lister son code dans GDB

```
(gdb) disas _start        # désassemble la fonction _start
(gdb) layout asm          # ouvre une fenêtre dédiée au désassemblage
```

`layout asm` est très pratique : tu vois le code en haut et le prompt en bas. Pour quitter ce mode : `Ctrl+X A`.

### Bonus

#### Quelques commandes utiles supplémentaires

| Commande | Effet |
|----------|-------|
| `info breakpoints` | Liste tous les breakpoints |
| `delete N` | Supprime le breakpoint N |
| `watch <expr>` | Casse quand `<expr>` change |
| `set $rax = 100` | **Modifie un registre** à la volée (cheat code) |
| `start` | Lance et casse à `main` (utile en C, ch. 21) |

#### Modifier un registre à la volée

```
(gdb) set $rax = 999
```

Ça permet de tester "que se passerait-il si `rax` valait 999 ici ?". Très utile en reverse engineering quand on veut **forcer une condition**.

#### Un `.gdbinit` personnalisé

Tu peux créer `~/.gdbinit` avec :

```
set disassembly-flavor intel
set print pretty on
```

Ça force GDB à afficher en **syntaxe Intel** par défaut (au lieu d'AT&T qui est cryptique). À faire **maintenant**, ça t'évitera des migraines.

### ❌ Erreur classique

```
Lancer "run" avant de poser un breakpoint
→ Le programme termine sans s'arrêter. Pose break _start AVANT.

Utiliser "step" au lieu de "stepi"
→ "step" attend des symboles source (pas en ASM pur).
→ Toujours "stepi" en assembleur.

Oublier de recompiler avec -g
→ GDB ne pourra pas relier les instructions aux lignes de l'.asm.

Sortir et relancer GDB pour chaque test
→ Tu peux relancer dans GDB avec "run" tout seul. Pas besoin de quitter.

Croire qu'AT&T == Intel
→ Si tu vois mov $5, %rax → c'est AT&T. mov rax, 5 → c'est Intel.
→ Pour passer en Intel : set disassembly-flavor intel
```

### Exercices

**Guidé :** Reprends le programme `voir.asm` ci-dessus. Lance-le dans GDB. Pose un breakpoint sur `_start`. Avance `stepi` après `stepi` et vérifie que :
- Après `mov rax, 10` : `rax = 10`
- Après `mov rbx, 32` : `rbx = 32`
- Après `add rax, rbx` : `rax = 42`

**Autonome :** Écris un programme `calculs.asm` qui fait 5 opérations arithmétiques d'affilée (au choix). **Avant** d'exécuter, écris sur papier ce que tu attends pour `rax` après chaque ligne. Vérifie au GDB.

**Défi :** Lance `voir.asm` dans GDB. Avant `add rax, rbx`, **force** `rbx = 100` avec `set $rbx = 100`. Continue avec `stepi`. Quelle est la valeur finale de `rax` ? (Réponse : 110, car 10 + 100.)

### 🧩 Mini-projet (chapitres 7-9) — Carnet d'observations

Écris `obs.asm` qui modifie `rax` exactement **6 fois** :

1. `mov rax, 1`
2. `add rax, 9`        → rax = 10
3. `imul rax, rax`     → rax = 100
4. `sub rax, 50`       → rax = 50
5. `inc rax`           → rax = 51
6. Sortir avec **`rax = 51`** comme code de retour

> **Attention à l'ordre des deux dernières instructions !** Si tu écris `mov rax, 60` en premier, tu écrases ton résultat (51). L'ordre correct est :
> ```nasm
>     ; après l'étape 5, rax = 51
>     mov rdi, rax       ; copier le résultat dans rdi AVANT d'écraser rax
>     mov rax, 60        ; puis seulement, numéro du syscall exit
>     syscall
> ```

Lance le programme dans GDB. **Note dans ton cahier** la valeur de `rax` après chaque `stepi` avant de regarder l'affichage GDB. Si tu te trompes, comprends pourquoi.

### ✅ Tu sais maintenant…

- Lancer un programme dans **GDB** : `gdb ./prog`
- Poser un **breakpoint** : `break _start`
- **Lancer** : `run`
- Avancer d'**une instruction** : `stepi`
- Afficher les **registres** : `info registers`, `print /x $rax`
- Afficher la **mémoire** : `x/10gx adresse`
- Désassembler : `disas`
- Modifier un registre à la volée : `set $rax = ...`
- Forcer la **syntaxe Intel** dans `.gdbinit`

À partir d'ici, **tous tes exercices se vérifient dans GDB**. C'est ta voix off.

---

### 🚩 Checkpoint — Fin de la Partie III

Avant de passer aux chapitres suivants, tu **dois** être capable de :

- [ ] Expliquer la différence entre `mov rax, x` et `mov rax, [x]` sans hésitation.
- [ ] Écrire un programme qui fait une addition entre deux registres.
- [ ] Compiler un `.asm` en exécutable (`nasm` puis `ld`).
- [ ] Lancer ce programme dans **GDB**, poser un breakpoint sur `_start`, et avancer avec `stepi`.
- [ ] Afficher la valeur de `rax`, `rbx`, `rsp` dans GDB.
- [ ] Lire un dump mémoire en hexadécimal et reconnaître quelques caractères ASCII.
- [ ] Utiliser le code de retour (`exit` + `echo $?`) pour vérifier un calcul simple.

Si tu coches tout, tu as les **vraies bases**. Si un point reste flou, **refais les exemples** avant de continuer. La suite suppose que ces réflexes sont acquis.

---
