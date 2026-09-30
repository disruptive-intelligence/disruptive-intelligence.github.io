---
title: PARTIE X — SYNTHÈSE ET BOÎTE À OUTILS
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 10
chapters: 10
---

---


## Chapitre 25 — Récapitulatif complet du débutant

### Le minimum à savoir

Tu as parcouru 24 chapitres. Tu sais maintenant **lire et écrire** de l'assembleur x86-64. Ce chapitre est une **boîte à outils** : des tableaux récapitulatifs à imprimer et à garder à portée.

### Cheat-sheet 1 — Instructions essentielles

| Instruction | Effet | Exemple |
|-------------|-------|---------|
| `mov d, s` | Copie `s` dans `d` | `mov rax, 42` |
| `lea d, [expr]` | Calcule une adresse, pas de lecture | `lea rax, [rbx + rcx*8]` |
| `add d, s` | `d = d + s` | `add rax, rbx` |
| `sub d, s` | `d = d - s` | `sub rax, 5` |
| `inc d` | `d = d + 1` | `inc rcx` |
| `dec d` | `d = d - 1` | `dec rcx` |
| `neg d` | `d = -d` | `neg rax` |
| `imul d, s` | `d = d * s` (signé) | `imul rax, rbx` |
| `idiv s` | `rax = rdx:rax / s`, `rdx = reste` | `mov rdx, 0 ; idiv rbx` |
| `cmp a, b` | Met à jour les flags (`a - b`) | `cmp rax, 10` |
| `test a, b` | Met à jour les flags (`a AND b`) | `test rax, rax` |
| `jmp lbl` | Saut inconditionnel | `jmp .fin` |
| `je / jne` | Saut si égal / différent | `je egal` |
| `jl / jg` | Saut si < / > (signé) | `jl negatif` |
| `jle / jge` | Saut si <= / >= (signé) | `jge positif` |
| `jb / ja` | Saut si < / > (non signé) | `jb plus_petit` |
| `jz / jnz` | Saut si zéro / non zéro | `jz fin` |
| `call lbl` | Appel de fonction | `call ma_fn` |
| `ret` | Retour de fonction | `ret` |
| `push s` | Empile `s` (rsp -= 8) | `push rax` |
| `pop d` | Dépile dans `d` (rsp += 8) | `pop rax` |
| `syscall` | Appel système Linux | `syscall` |
| `xor d, s` | OU exclusif | `xor rax, rax` (= mov rax, 0) |
| `and d, s` | ET bit-à-bit | `and rax, 0xFF` |
| `or d, s` | OU bit-à-bit | `or rax, 1` |
| `shl d, n` | Décalage à gauche (× 2ⁿ) | `shl rax, 3` (rax × 8) |
| `shr d, n` | Décalage à droite (÷ 2ⁿ) | `shr rax, 1` |
| `leave` | `mov rsp, rbp ; pop rbp` | (épilogue compact) |
| `nop` | Ne fait rien | (utile en patching) |

### Cheat-sheet 2 — Registres x86-64

| 64 bits | 32 bits | 16 bits | 8 bits | Rôle conventionnel |
|---------|---------|---------|--------|---------------------|
| `rax` | `eax` | `ax` | `al` | Valeur de retour, résultats |
| `rbx` | `ebx` | `bx` | `bl` | Variable (callee-saved) |
| `rcx` | `ecx` | `cx` | `cl` | Compteur, 4ème arg |
| `rdx` | `edx` | `dx` | `dl` | 3ème arg, reste de div |
| `rsi` | `esi` | `si` | `sil` | 2ème arg |
| `rdi` | `edi` | `di` | `dil` | 1er arg |
| `rsp` | `esp` | `sp` | `spl` | **Pointeur de pile** |
| `rbp` | `ebp` | `bp` | `bpl` | Base de pile (callee-saved) |
| `r8`-`r15` | `r8d`-`r15d` | `r8w`-`r15w` | `r8b`-`r15b` | 5ème/6ème args, etc. |
| `rip` | — | — | — | Pointeur d'instruction (lecture seule directe) |

### Cheat-sheet 3 — Convention d'appel System V (Linux x86-64)

| Élément | Registre(s) |
|---------|-------------|
| **Arguments 1 à 6** | `rdi, rsi, rdx, rcx, r8, r9` |
| **Arguments 7+** | Sur la pile (ordre inverse) |
| **Valeur de retour** | `rax` |
| **Caller-saved** (peuvent être détruits) | `rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11` |
| **Callee-saved** (à préserver) | `rbx, rbp, r12, r13, r14, r15` |
| **Alignement pile** | 16 octets avant `call` |
| **`rax` avant variadique** | Nombre de regs XMM (0 si pas de flottant) |

### Cheat-sheet 4 — Syscalls Linux x86-64 utiles

| Numéro (`rax`) | Nom | `rdi` | `rsi` | `rdx` | Notes |
|----------------|-----|-------|-------|-------|-------|
| 0 | `read` | fd | buf | count | Retour = octets lus |
| 1 | `write` | fd | buf | count | Retour = octets écrits |
| 2 | `open` | chemin | flags | mode | Retour = fd |
| 3 | `close` | fd | — | — | |
| 8 | `lseek` | fd | offset | whence | |
| 9 | `mmap` | adr | longueur | prot | (avancé) |
| 12 | `brk` | adr | — | — | |
| 35 | `nanosleep` | req | rem | — | |
| 39 | `getpid` | — | — | — | |
| 57 | `fork` | — | — | — | |
| 59 | `execve` | chemin | argv | envp | |
| 60 | `exit` | code | — | — | |
| 62 | `kill` | pid | sig | — | |

**Liste complète :** `cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h` (Ubuntu/Debian) ou `cat /usr/include/asm/unistd_64.h` (selon distribution) ou `man 2 syscalls`.

### Cheat-sheet 5 — Commandes GDB

| Commande | Effet |
|----------|-------|
| `gdb ./prog` | Lance GDB |
| `break <lbl>` / `b *0x...` | Pose un breakpoint |
| `info breakpoints` / `i b` | Liste les breakpoints |
| `delete N` | Supprime le breakpoint N |
| `run` / `r` | Lance le programme |
| `start` | Lance et casse à `main` |
| `continue` / `c` | Continue jusqu'au prochain break |
| `stepi` / `si` | 1 instruction (entre dans les call) |
| `nexti` / `ni` | 1 instruction (par-dessus les call) |
| `finish` | Sort de la fonction courante |
| `info registers` / `i r` | Affiche tous les registres |
| `print /x $rax` | Affiche `rax` en hexa |
| `print /d $rax` | Affiche en décimal |
| `print /t $rax` | Affiche en binaire |
| `x/10gx $rsp` | 10 qword en hexa à `rsp` |
| `x/s $rdi` | Affiche une chaîne |
| `x/8bx <adr>` | 8 octets en hexa |
| `disas` | Désassemble autour de `rip` |
| `disas <fn>` | Désassemble une fonction |
| `layout asm` | Vue divisée (asm + commande) |
| `set $rax = N` | Modifie un registre |
| `set $rip = 0x...` | Saute à une adresse |
| `set disassembly-flavor intel` | Force syntaxe Intel |
| `info functions` | Liste les fonctions |
| `info variables` | Liste les variables |
| `quit` / `q` | Quitter |

### Cheat-sheet 6 — Outils ELF / binaires

| Commande | Effet |
|----------|-------|
| `file ./prog` | Type de fichier |
| `strings ./prog` | Chaînes lisibles |
| `nm ./prog` | Symboles |
| `readelf -h ./prog` | Entête ELF |
| `readelf -S ./prog` | Sections |
| `readelf -s ./prog` | Symboles (alternative à `nm`) |
| `objdump -d -M intel ./prog` | Désassemblage Intel |
| `objdump -d -M intel --disassemble=main ./prog` | Désassemble juste `main` |
| `objdump -s -j .rodata ./prog` | Voir le contenu d'une section |
| `ltrace ./prog` | Trace les appels libc |
| `strace ./prog` | Trace les syscalls |
| `xxd ./prog` | Dump hex |
| `hexdump -C ./prog` | Dump hex + ASCII |
| `strip ./prog` | Enlève les symboles |

### Modèle 1 — Fichier `.asm` minimal (syscalls)

```nasm
; modele_syscall.asm — Squelette pour programmes basés syscalls

section .data
    msg db "Bonjour", 10
    len equ $ - msg

section .bss
    buffer resb 64

section .text
global _start

_start:
    ; ─── corps du programme ───

    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; ─── sortie ───
    mov rax, 60
    mov rdi, 0
    syscall
```

**Compilation :**

```bash
nasm -f elf64 -g -F dwarf modele_syscall.asm -o modele_syscall.o
ld modele_syscall.o -o modele_syscall
```

### Modèle 2 — Fichier `.asm` avec libc

```nasm
; modele_libc.asm — Squelette pour programmes avec libc

default rel

section .data
    fmt db "Resultat : %ld", 10, 0     ; %ld pour un long (qword), cohérent avec un mov rsi 64 bits

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    ; ─── corps du programme ───
    lea rdi, [fmt]
    mov rsi, 42
    xor rax, rax
    call printf

    xor rax, rax            ; retour 0
    leave
    ret
```

**Compilation :**

```bash
nasm -f elf64 -g -F dwarf modele_libc.asm -o modele_libc.o
gcc -no-pie modele_libc.o -o modele_libc
```

### Modèle 3 — Makefile générique

```makefile
# Makefile générique pour les programmes ASM

NASM       = nasm
LD         = ld
GCC        = gcc
NASMFLAGS  = -f elf64 -g -F dwarf

# Pour les programmes purs syscalls
%.o: %.asm
	$(NASM) $(NASMFLAGS) $< -o $@

%: %.o
	$(LD) $< -o $@

# Pour les programmes avec libc, utiliser :
# make NAME_libc          (suffixe _libc dans le nom de la cible)
%_libc: %_libc.o
	$(GCC) -no-pie $< -o $@

clean:
	rm -f *.o
	@find . -maxdepth 1 -type f -executable ! -name '*.sh' -delete 2>/dev/null || true

.PHONY: clean
```

Usage :
```bash
make exit              # compile exit.asm en exécutable exit
make hello_libc        # compile hello_libc.asm avec gcc
make clean             # supprime tous les .o et exécutables
```

### Méthodologie — Analyser un petit binaire inconnu

Quand on te donne un binaire et qu'on te demande de le comprendre, suis **cet ordre** :

1. **`file ./bin`** → c'est quoi ? 64 bits ? statique ou dynamique ?
2. **`strings ./bin`** → des chaînes parlantes ? mot de passe ? URL ? format ?
3. **`nm ./bin`** → symboles visibles ? fonctions nommées ?
4. **`ltrace ./bin`** → quels appels libc fait-il ? `strcmp`, `memcmp`, `system` ?
5. **`strace ./bin`** → quels syscalls ? `open`, `read`, `connect` ?
6. **`objdump -d -M intel ./bin | less`** → désassemblage. Cherche `main`.
7. **GDB** → casse sur `main`, observe les registres, suis les arguments.
8. **Repère** : prologues, comparaisons, sauts arrière, appels à des fonctions clés.
9. **Hypothèse** → teste.

### Top 10 des erreurs classiques (transversal)

1. **Confondre adresse (`var`) et contenu (`[var]`).**
2. **Oublier les crochets dans `mov`.**
3. **Mémoire-à-mémoire direct interdit** (`mov [a], [b]`).
4. **Mauvaise taille** (`mov al, ...` quand on attendait un qword).
5. **Push/pop déséquilibrés** → crash.
6. **Oublier `rdx = 0` avant `idiv`** → reste corrompu.
7. **Oublier `ret`** dans une fonction.
8. **Ne pas respecter la convention d'appel** (arg dans `rax` au lieu de `rdi`).
9. **Pile désalignée** avant un `call` libc.
10. **Lire/écrire avec la mauvaise taille** (`mov al, [qword_var]` ne lit qu'un octet).

### ✅ Tu sais maintenant…

Tu as toutes les bases pour :
- **Écrire** des programmes assembleur x86-64 simples
- **Compiler** et **linker** avec NASM, ld, ou gcc
- **Déboguer** au GDB en suivant les registres et la pile
- **Comprendre** le code généré par un compilateur C
- **Désassembler** un binaire ELF avec objdump
- **Reverser** un mini-crackme débutant
- **Reconnaître** prologues, conditions, boucles, appels dans du code désassemblé

---


## ANNEXES

---


## Annexe A — Syntaxe AT&T pour la lecture

### Pourquoi cette annexe ?

Tu rencontreras forcément du code en **syntaxe AT&T** (default GDB sans config, certaines docs Linux). Pas pour **écrire**, juste pour **lire**.

### Différences principales avec Intel

| Aspect | Intel (NASM) | AT&T |
|--------|--------------|------|
| Ordre des opérandes | `mov dest, src` | `mov src, dest` (**inversé !**) |
| Registres | `rax`, `eax` | `%rax`, `%eax` (préfixe `%`) |
| Valeurs immédiates | `5`, `0x42` | `$5`, `$0x42` (préfixe `$`) |
| Indirection mémoire | `[rax + 8]` | `8(%rax)` |
| Indexation | `[rax + rcx*8]` | `(%rax,%rcx,8)` |
| Suffixe de taille | dans le registre (`al`, `ax`, `eax`, `rax`) | sur l'instruction (`movb`, `movw`, `movl`, `movq`) |

### Exemples de traduction

| Intel | AT&T |
|-------|------|
| `mov rax, 5` | `movq $5, %rax` |
| `mov rax, rbx` | `movq %rbx, %rax` |
| `mov rax, [rbx]` | `movq (%rbx), %rax` |
| `mov rax, [rbx + 8]` | `movq 8(%rbx), %rax` |
| `mov rax, [rbx + rcx*4]` | `movq (%rbx,%rcx,4), %rax` |
| `add rax, rbx` | `addq %rbx, %rax` |
| `cmp rax, 10` | `cmpq $10, %rax` |
| `jne loop` | `jne loop` (identique) |
| `call printf` | `call printf` (identique) |

### Le piège du sens : `cmp`

C'est **le piège n°1** :

- Intel : `cmp rax, 10` + `jl ...` → saute si **`rax < 10`**.
- AT&T : `cmpq $10, %rax` + `jl ...` → saute aussi si **`%rax < 10`** (même sens, car `cmp` calcule `dest - src`, et AT&T met le src en premier).

Donc même si la syntaxe inverse les opérandes, le **sens du test** reste le même. Mais c'est très perturbant au début.

### Comment forcer GDB en Intel

Dans `~/.gdbinit` :
```
set disassembly-flavor intel
```

Ou ponctuellement :
```
(gdb) set disassembly-flavor intel
```

**Fais-le.** Tu n'auras presque plus à lire de l'AT&T.

---


## Annexe B — x86 32 bits vs x86-64

### Différences principales

| Aspect | x86 (32 bits) | x86-64 (64 bits) |
|--------|---------------|------------------|
| Registres généraux | 8 : `eax`-`ebp`, `esp` | 16 : `rax`-`rsp`, `r8`-`r15` |
| Taille des registres | 32 bits | 64 bits |
| Nom du pointeur de pile | `esp` | `rsp` |
| Nom du pointeur d'instr. | `eip` | `rip` |
| Adresses | 32 bits (max 4 Go) | 64 bits |
| Convention d'appel Linux | Args sur la **pile** | Args dans registres (System V) |
| Numéro de syscall | dans `eax` | dans `rax` |
| Instruction syscall | `int 0x80` | `syscall` (plus rapide) |
| Pile | 4 octets par push | 8 octets par push |

### Tu rencontreras du 32 bits si...

- Tu analyses un vieux binaire (avant 2010 environ).
- Tu joues à des CTF "old school".
- Tu fais du reverse sur des programmes embarqués légers.

### Conseil

**Reste en 64 bits pour apprendre.** Les concepts sont identiques, et tout est plus moderne. Le 32 bits sera évident pour toi le jour où tu en croiseras.

---


## Annexe C — Linux System V ABI vs Windows x64 ABI

### Pourquoi ça change ?

L'ABI (Application Binary Interface) définit **comment** les fonctions communiquent : où vont les arguments, où va le retour, etc. Linux et Windows ont **deux ABI différentes** en x86-64.

### Différences principales

| Aspect | System V (Linux/macOS) | Microsoft x64 (Windows) |
|--------|-------------------------|-------------------------|
| Args 1-4 | `rdi, rsi, rdx, rcx` | `rcx, rdx, r8, r9` |
| Args 5+ | `r8, r9`, puis pile | Pile (avec espace réservé) |
| Espace réservé | Aucun | **32 octets** (shadow space) sur la pile avant chaque `call` |
| Caller-saved | `rax, rcx, rdx, rsi, rdi, r8-r11` | `rax, rcx, rdx, r8-r11` |
| Callee-saved | `rbx, rbp, r12-r15` | `rbx, rbp, rdi, rsi, r12-r15` |
| Retour | `rax` | `rax` |
| Alignement pile | 16 octets avant `call` | 16 octets avant `call` |

### Conséquence pratique

Un binaire **Linux** et un binaire **Windows** se reversent **différemment** :
- Sur Linux, le 1er arg est dans `rdi`.
- Sur Windows, le 1er arg est dans `rcx`.

Si tu fais du reverse Windows un jour, **renverse tes réflexes**. C'est tout.

---


## Annexe D — Nombres signés, complément à deux et débordements

### Le problème

Comment représenter `-1` en binaire avec **seulement des 0 et des 1** ? La solution adoptée par tous les CPU modernes : **le complément à deux**.

### Le complément à deux en quelques règles

#### Représentation

Sur N bits, on peut représenter :
- Non signés : `0` à `2ᴺ - 1`.
- Signés (complément à deux) : `-2ᴺ⁻¹` à `2ᴺ⁻¹ - 1`.

Pour un octet (8 bits) :
- Non signé : 0 à 255.
- Signé : -128 à +127.

#### Le bit de signe

Le **bit le plus à gauche** indique le signe :
- `0` → positif.
- `1` → négatif.

#### Comment calculer `-N`

Pour obtenir le complément à deux de `N` :
1. **Inverser tous les bits** (complément à un).
2. **Ajouter 1**.

Exemple sur 8 bits, calcul de `-5` :
```
   5 = 0000 0101
  ~5 = 1111 1010   (inversion)
  -5 = 1111 1011   (+ 1) = 0xFB
```

Donc `-5` sur 8 bits = `0xFB` = `251` non signé.

Sur 64 bits, `-1` = `0xFFFFFFFFFFFFFFFF`.

### Conséquences

#### Une même valeur, deux interprétations

`0xFF` sur 8 bits :
- Non signé : 255.
- Signé : -1.

**C'est le CPU qui choisit comment l'interpréter** selon l'instruction utilisée (`jl` pour signé, `jb` pour non signé). C'est pour ça que tu dois bien distinguer.

#### Débordements (overflow)

Sur 8 bits non signés :
- `255 + 1 = 0` (débordement, le résultat "boucle").

Sur 8 bits signés :
- `127 + 1 = -128` (overflow signé).

Le CPU met le flag `OF` (Overflow Flag) pour signaler ça, mais ne plante pas.

### En reverse

Si tu vois un `cmp rax, -1` ou `cmp rax, 0xFFFFFFFFFFFFFFFF`, **c'est la même chose**. Souvent, c'est utilisé pour tester si une fonction a renvoyé une erreur.

---


## Annexe E — Little-endian

### Le concept

Quand on stocke un nombre multi-octets en mémoire, deux ordres sont possibles :

- **Big-endian** : l'octet de poids fort en premier (comme on écrit en français).
- **Little-endian** : l'octet de poids faible en premier (à l'envers).

**x86 et x86-64 sont little-endian.** Tous les PC modernes le sont.

### Exemple

Soit le nombre `0x12345678` (4 octets). En mémoire :

```
Adresse :  0x100  0x101  0x102  0x103
Big-endian :  12    34     56     78
Little-endian: 78    56     34     12   ← x86-64
```

### En GDB

```
(gdb) x/4bx &n
0x404000:  0x78  0x56  0x34  0x12
```

Tu lis le résultat **à l'envers** : la valeur est bien `0x12345678`.

Quand tu fais `x/wx &n`, GDB te le **réordonne** pour l'affichage :

```
(gdb) x/wx &n
0x404000:  0x12345678
```

C'est pour ça que `x/wx` est plus pratique que `x/bx` quand tu sais que c'est un dword.

### Conséquence

Quand tu débugges et que tu lis des octets bruts, **n'oublie pas que les nombres sont à l'envers**. Une suite `EF CD AB 90` à l'écran est en réalité le nombre `0x90ABCDEF`.

---


## Annexe F — Makefile et commandes utiles

### Makefile complet et commenté

```makefile
# ========================================
# Makefile pour cours d'assembleur x86-64
# ========================================

# Outils
NASM       = nasm
LD         = ld
GCC        = gcc

# Options
NASMFLAGS  = -f elf64 -g -F dwarf

# Règle générale pour les .o
%.o: %.asm
	$(NASM) $(NASMFLAGS) $< -o $@

# Programmes purs syscalls (linkés avec ld)
%: %.o
	$(LD) $< -o $@

# Programmes avec libc (linkés avec gcc, suffixe _libc)
%_libc: %_libc.o
	$(GCC) -no-pie $< -o $@

# Lancer un programme dans GDB
debug-%: %
	gdb ./$<

# Désassembler
disas-%: %
	objdump -d -M intel ./$< | less

# Nettoyer
clean:
	rm -f *.o
	@for f in *; do \
		[ -f "$$f" ] && [ -x "$$f" ] && [ "$${f%.*}" = "$$f" ] && rm "$$f" 2>/dev/null; \
	done || true

.PHONY: clean
```

### Commandes utiles à connaître par cœur

```bash
# Compilation
nasm -f elf64 -g -F dwarf prog.asm -o prog.o
ld prog.o -o prog
gcc -no-pie prog.o -o prog        # avec libc

# Exécution
./prog
echo $?                            # voir le code de retour

# Conversion de bases
printf "%x\n" 255                 # déc → hex
printf "%d\n" 0xff                # hex → déc
echo "obase=2; 42" | bc           # déc → bin

# Inspection rapide
file prog
strings prog
nm prog
readelf -h prog
readelf -S prog
objdump -d -M intel prog | less

# Tracing
strace ./prog
ltrace ./prog

# Compilation C → ASM
gcc -O0 -masm=intel -S prog.c -o prog.s
```

---


## Annexe G — Glossaire assembleur / reverse

| Terme | Définition |
|-------|------------|
| **ABI** | Application Binary Interface : règles d'appel de fonctions |
| **Adresse** | Numéro identifiant une case mémoire |
| **Adressage** | Manière d'exprimer une adresse (`[reg]`, `[reg + N]`, etc.) |
| **ASCII** | Table standard de correspondance caractère ↔ nombre |
| **ASM** | Assembleur (le langage) |
| **Big-endian** | Ordre des octets : poids fort en premier |
| **Bit** | Plus petite unité d'information : 0 ou 1 |
| **BSS** | Section pour variables non initialisées |
| **Buffer** | Zone mémoire pour stocker des données |
| **Caller-saved** | Registres qu'une fonction peut détruire |
| **Callee-saved** | Registres qu'une fonction doit préserver |
| **CFG** | Control Flow Graph : graphe des chemins d'exécution |
| **Complément à 2** | Représentation des entiers négatifs |
| **CPU** | Processeur central |
| **Crackme** | Petit binaire à reverser (avec un mot de passe par exemple) |
| **CTF** | Capture The Flag : compétition de sécurité |
| **Désassemblage** | Conversion binaire → assembleur lisible |
| **Drapeau (flag)** | Bit d'indicateur d'état dans le CPU |
| **dword** | Double word = 4 octets = 32 bits |
| **ELF** | Format des exécutables Linux |
| **Endianness** | Ordre des octets en mémoire |
| **Épilogue** | Code de fin de fonction (`leave ; ret`) |
| **GDB** | GNU Debugger |
| **ghidra** | Outil de reverse engineering NSA, gratuit |
| **Hexadécimal** | Base 16 (`0-9, A-F`), notée `0x...` |
| **IDA** | Outil de reverse propriétaire de référence |
| **Immédiate** | Valeur littérale (constante) dans une instruction |
| **Instruction** | Action élémentaire du CPU |
| **Kernel** | Noyau du système d'exploitation |
| **Label** | Nom symbolique pour une adresse |
| **`lea`** | Load Effective Address : calcul d'adresse sans lecture |
| **LIFO** | Last In, First Out (mode pile) |
| **Linker** | Programme qui combine fichiers objets en exécutable |
| **Little-endian** | Ordre des octets : poids faible en premier (x86) |
| **Loader** | Code qui charge un programme en mémoire |
| **MASM** | Microsoft Macro Assembler (Windows) |
| **NASM** | Netwide Assembler (utilisé dans ce cours) |
| **NOP** | "No Operation" — instruction qui ne fait rien |
| **NULL** | Pointeur invalide (généralement adresse 0) |
| **Octet (byte)** | 8 bits = 1 octet |
| **Opcode** | Représentation binaire d'une instruction |
| **PIE** | Position Independent Executable |
| **Pile (stack)** | Zone mémoire en mode LIFO |
| **PLT** | Procedure Linkage Table (appels libc dynamiques) |
| **Pointeur** | Variable contenant une adresse |
| **Prologue** | Code de début de fonction (`push rbp ; mov rbp, rsp`) |
| **qword** | Quad word = 8 octets = 64 bits |
| **`r2`/radare2** | Outil interactif de reverse engineering open-source |
| **RAM** | Mémoire vive |
| **Registre** | Mini-case de stockage dans le CPU |
| **Reverse engineering** | Analyser un programme sans son code source |
| **`rip`** | Instruction Pointer (adresse de la prochaine instruction) |
| **`rsp`** | Stack Pointer (sommet de la pile) |
| **`.bss`** | Section pour variables non initialisées |
| **`.data`** | Section pour variables initialisées |
| **`.rodata`** | Section read-only (constantes) |
| **`.text`** | Section du code exécutable |
| **Saut** | Instruction qui change `rip` |
| **Section** | Sous-partie d'un fichier `.asm` ou ELF |
| **Stack frame** | Cadre de pile d'une fonction |
| **Strip** | Enlever les symboles d'un binaire |
| **Symbole** | Nom associé à une adresse (fonction, variable globale) |
| **Syscall** | Demande de service au noyau |
| **System V** | ABI Unix/Linux standard |
| **Variadique** | Fonction à nombre variable d'arguments (`printf`) |
| **word** | 2 octets = 16 bits |

---


## Annexe H — Panorama des outils de reverse

Tu connais déjà **`objdump`** et **`GDB`** (vus aux chapitres 23-24). Mais en reverse, il existe d'autres outils qui complètent ces deux-là. Voici un panorama rapide, pour que tu saches lequel utiliser quand.

### Tableau de référence

| Outil | Type | Force principale | Faiblesse | Quand l'utiliser |
|-------|------|------------------|-----------|------------------|
| **`objdump`** | Statique | Rapide, scriptable, installé partout | Pas interactif, output brut | Premier coup d'œil, automatisation |
| **`GDB`** (+ pwndbg) | Dynamique | Voit le programme tourner, force les valeurs, modifie l'exécution | Pas de vue d'ensemble, pas de décompilation | Comprendre un comportement précis, contourner une protection |
| **`radare2`** / **Cutter** | Statique + dynamique | Très puissant, open-source, scriptable, graphe interactif | Courbe d'apprentissage raide | Reverse intermédiaire, CTF sérieux |
| **Ghidra** | Statique avec décompilation | **Décompile en pseudo-C** (très lisible), graphe, gratuit, open-source (NSA) | Lourd à lancer, interface Java | Comprendre vite un gros programme, lire du pseudo-C plutôt que de l'ASM |
| **IDA Free** | Statique avec décompilation | Référence historique, décompilation excellente | Version gratuite limitée (pas de x64 dans les vieilles versions), payant pour le reste | Reverse professionnel |
| **`strace`** | Dynamique syscalls | Voit tous les syscalls (`open`, `read`, `connect`…) | Pas de détail des calculs internes | Comprendre ce qu'un binaire **fait au système** |
| **`ltrace`** | Dynamique libc | Voit tous les appels libc avec leurs args | Mêmes limites que strace | **Souvent suffit pour trouver un mot de passe** (`strcmp("entrée", "secret")`) |
| **`xxd`** / **`hexdump -C`** | Statique brut | Voir le contenu hex + ASCII | Aucune interprétation | Inspecter un fichier inconnu, headers |

### Méthode recommandée pour un débutant

L'ordre dans lequel je te conseille de découvrir ces outils :

1. **Aujourd'hui (déjà fait dans ce cours) :** `objdump`, `GDB`, `strings`, `nm`, `readelf`.
2. **Étape suivante (1-2 mois) :** **`ltrace`** et **`strace`** — souvent les outils les plus rapides pour comprendre un petit binaire.
3. **Ensuite (3-6 mois) :** **Ghidra** — la décompilation transforme l'apprentissage. Tu vois du pseudo-C à la place de l'ASM.
4. **Plus tard :** **radare2** ou **Cutter** pour le reverse interactif et les CTF.
5. **Encore plus tard :** **IDA Free** ou **IDA Pro** si tu vises du reverse pro.

### Démarrage rapide avec Ghidra

Si tu n'es pas dépaysé par l'environnement Java :

```bash
# Sur Ubuntu/Debian
sudo apt install openjdk-17-jdk
# Télécharger Ghidra sur ghidra-sre.org, puis :
unzip ghidra_*.zip
cd ghidra_*
./ghidraRun
```

Crée un projet, importe ton binaire (`File → Import File`), double-clique pour l'analyser (laisse les options par défaut). En quelques secondes, tu auras :
- À gauche, la liste des fonctions.
- Au centre, le **désassemblage**.
- À droite, le **pseudo-C décompilé** correspondant.

> **Effet "wow" pédagogique :** après avoir lu de l'ASM brut pendant des heures, voir Ghidra te montrer `if (strcmp(input, "secret") == 0)` directement, c'est libérateur. Mais **n'utilise pas Ghidra trop tôt** — les bases ASM apprises dans ce cours te permettront de comprendre ce que Ghidra te montre, et surtout de **repérer ses erreurs** (Ghidra se trompe parfois).

---


## Annexe I — Suite logique après ce cours

Tu as fini ce cours ? Bravo. Voici la suite naturelle, par niveau de difficulté :

### Niveau 1 — Consolidation

- **Pratique sur picoCTF** (catégorie *Reverse Engineering* niveau débutant).
- **Refaire les chapitres 23-24** avec d'autres binaires que tu compiles toi-même.
- **Lire des `.s` produits par gcc** avec différents codes et différentes optimisations.
- **Comparer C et ASM sur [Godbolt](https://godbolt.org)** régulièrement.

### Niveau 2 — Approfondir l'ASM

- **Apprendre la syntaxe AT&T** en lecture profonde (utile sur certains systèmes).
- **Découvrir SIMD/SSE/AVX** (calcul vectoriel) pour les performances.
- **Programmation noyau Linux** (modules, drivers).

### Niveau 3 — Approfondir le reverse engineering

- **Apprendre `radare2`** (`r2`) ou **ghidra** ou **IDA Free**.
- **CTF intermédiaires** sur HackTheBox, pwn.college, root-me.
- **Analyser des binaires strippés** avec des optimisations agressives.

### Niveau 4 — Sécurité offensive (à approfondir prudemment)

- **C orienté mémoire** : pointeurs, allocation, bugs courants.
- **Introduction au pwn** : buffer overflow, format string, ROP.
- **Shellcode** : écrire des charges utiles minimalistes.
- **Sécurité défensive** : ASLR, DEP/NX, PIE, canaries.

### Niveau 5 — Malware analysis et reverse Windows

- **Architecture Windows x64** (ABI différente, voir Annexe C).
- **Analyse de PE** (équivalent ELF côté Windows).
- **Sandbox et désobfuscation**.
- **Outils** : x64dbg, Cuckoo, Cutter.

### Livres recommandés

- *Practical Reverse Engineering* — Bruce Dang et al.
- *Hacking: The Art of Exploitation* — Jon Erickson.
- *The Shellcoder's Handbook* — Anley et al.
- *Computer Systems: A Programmer's Perspective* (CS:APP) — Bryant & O'Hallaron (fondations académiques).

### Communautés

- Reddit : r/ReverseEngineering, r/AskNetsec, r/lowlevel
- Discord : NightCTF, pwn.college, divers serveurs CTF
- Conférences : DEF CON, BSides, Black Hat (vidéos sur YouTube)

---


## Conclusion

Tu as toutes les bases pour lire, écrire et comprendre l'assembleur x86-64 sous Linux :

- **Chapitres 1-3 :** Le modèle mental — CPU, mémoire, registres, hex
- **Chapitres 4-6 :** Premiers programmes — NASM, sections, syscalls
- **Chapitres 7-9 :** Registres et observation — mov, calculs, GDB
- **Chapitres 10-12 :** Mémoire — variables, chaînes, lea, modes d'adressage
- **Chapitres 13-15 :** I/O — read, conversions, fichiers
- **Chapitres 16-17 :** Logique — comparaisons, sauts, boucles
- **Chapitres 18-20 :** Structure — pile, fonctions, stack frame
- **Chapitres 21-22 :** Lien avec C — libc, du C à l'ASM
- **Chapitres 23-24 :** Reverse — objdump, GDB sur binaires inconnus, crackmes
- **Chapitre 25 :** Synthèse et boîte à outils

**Pour continuer à progresser :**

- Écris des programmes ASM pour le plaisir — c'est la meilleure façon d'apprendre.
- Quand tu es bloqué, **GDB est ton meilleur ami**. Observe, n'imagine pas.
- Compile du C en ASM, lis le résultat. C'est ton meilleur prof.
- Lis le code des autres, surtout sur Godbolt.
- Fais des CTF — la pratique forge l'intuition.
- N'aie pas peur. L'assembleur n'est pas magique, c'est juste verbeux.

Bon code, bon reverse, bonne curiosité !
