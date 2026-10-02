---
title: Chapitre 25 — Récapitulatif complet du débutant
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie X — Synthèse et boîte à outils
  - index.md
---

## Le minimum à savoir

Tu as parcouru 24 chapitres. Tu sais maintenant **lire et écrire** de l'assembleur x86-64. Ce chapitre est une **boîte à outils** : des tableaux récapitulatifs à imprimer et à garder à portée.

## Cheat-sheet 1 — Instructions essentielles

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

## Cheat-sheet 2 — Registres x86-64

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

## Cheat-sheet 3 — Convention d'appel System V (Linux x86-64)

| Élément | Registre(s) |
|---------|-------------|
| **Arguments 1 à 6** | `rdi, rsi, rdx, rcx, r8, r9` |
| **Arguments 7+** | Sur la pile (ordre inverse) |
| **Valeur de retour** | `rax` |
| **Caller-saved** (peuvent être détruits) | `rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11` |
| **Callee-saved** (à préserver) | `rbx, rbp, r12, r13, r14, r15` |
| **Alignement pile** | 16 octets avant `call` |
| **`rax` avant variadique** | Nombre de regs XMM (0 si pas de flottant) |

## Cheat-sheet 4 — Syscalls Linux x86-64 utiles

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

## Cheat-sheet 5 — Commandes GDB

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

## Cheat-sheet 6 — Outils ELF / binaires

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

## Modèle 1 — Fichier `.asm` minimal (syscalls)

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


## Modèle 2 — Fichier `.asm` avec libc

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


## Modèle 3 — Makefile générique

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


## Méthodologie — Analyser un petit binaire inconnu

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

## Top 10 des erreurs classiques (transversal)

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

## ✅ Tu sais maintenant…

Tu as toutes les bases pour :

- **Écrire** des programmes assembleur x86-64 simples
- **Compiler** et **linker** avec NASM, ld, ou gcc
- **Déboguer** au GDB en suivant les registres et la pile
- **Comprendre** le code généré par un compilateur C
- **Désassembler** un binaire ELF avec objdump
- **Reverser** un mini-crackme débutant
- **Reconnaître** prologues, conditions, boucles, appels dans du code désassemblé

---
