---
title: Chapitre 9 — GDB pour observer les registres
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie III — Registres, calculs et observation
  - index.md
---

## Le minimum à savoir

### Pourquoi GDB tout de suite

Tu codes "à l'aveugle" depuis le chapitre 6. Tu fais `mov rax, 5`, mais tu **ne vois pas** que `rax` vaut 5. GDB, c'est ce qui te permet de **voir** ce que ton programme fait, instruction par instruction.

> **À retenir :** GDB est à l'assembleur ce que `print()` est à Python. C'est **l'outil de visibilité**. Sans lui, tu codes à l'aveugle.

### Compiler avec les symboles de debug

Pour que GDB t'affiche un maximum d'informations, compile avec `-g -F dwarf` :

```bash
nasm -f elf64 -g -F dwarf mon_prog.asm -o mon_prog.o
ld mon_prog.o -o mon_prog
```


Si tu utilises le Makefile du chapitre 4, c'est déjà fait.

### Lancer GDB

```bash
gdb ./mon_prog
```


Tu arrives dans le prompt GDB (`(gdb)`). À ce stade, **rien n'est lancé**. Tu prépares la session.

### Les 7 commandes vitales pour démarrer

| Commande | Raccourci | Effet |
|----------|-----------|-------|
| `break _start` | `b _start` | Pose un **breakpoint** au début |
| `run` | `r` | **Lance** le programme |
| `stepi` | `si` | Avance d'**une instruction** |
| `info registers` | `i r` | Affiche **tous les registres** |
| `print /x $rax` | `p /x $rax` | Affiche `rax` en **hexa** |
| `disassemble` | `disas` | Affiche le **désassemblage** autour de l'instruction courante |
| `quit` | `q` | **Quitter** GDB |

### Un exemple pas-à-pas

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

### Avec pwndbg : encore plus visuel

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

## Très utile en pratique

### Voir un registre en plusieurs formats

```
(gdb) print $rax          # décimal      → 42
(gdb) print /x $rax       # hexadécimal  → 0x2a
(gdb) print /t $rax       # binaire      → 101010
(gdb) print /c $rax       # caractère    → '*'  (42 = '*')
```


### Voir la mémoire

```
(gdb) x/10gx 0x404000     # 10 qword en hexa à partir de cette adresse
(gdb) x/10bx &var         # 10 octets en hexa de la variable var
(gdb) x/s &msg            # une chaîne ASCII à partir de msg
```


Le format `x/COUNT SIZE FORMAT` :

- COUNT : combien d'éléments
- SIZE : `b` (byte), `w` (word), `d` (dword), `g` (qword)
- FORMAT : `x` (hexa), `d` (décimal), `s` (chaîne), `c` (caractère)

### Avancer plus vite

| Commande | Effet |
|----------|-------|
| `stepi` (`si`) | 1 instruction |
| `stepi 5` | 5 instructions |
| `continue` (`c`) | Continuer jusqu'au prochain breakpoint ou la fin |
| `nexti` (`ni`) | 1 instruction, **sans entrer dans les `call`** (utile plus tard) |

### Lister son code dans GDB

```
(gdb) disas _start        # désassemble la fonction _start
(gdb) layout asm          # ouvre une fenêtre dédiée au désassemblage
```


`layout asm` est très pratique : tu vois le code en haut et le prompt en bas. Pour quitter ce mode : `Ctrl+X A`.

## Bonus

### Quelques commandes utiles supplémentaires

| Commande | Effet |
|----------|-------|
| `info breakpoints` | Liste tous les breakpoints |
| `delete N` | Supprime le breakpoint N |
| `watch <expr>` | Casse quand `<expr>` change |
| `set $rax = 100` | **Modifie un registre** à la volée (cheat code) |
| `start` | Lance et casse à `main` (utile en C, ch. 21) |

### Modifier un registre à la volée

```
(gdb) set $rax = 999
```


Ça permet de tester "que se passerait-il si `rax` valait 999 ici ?". Très utile en reverse engineering quand on veut **forcer une condition**.

### Un `.gdbinit` personnalisé

Tu peux créer `~/.gdbinit` avec :

```
set disassembly-flavor intel
set print pretty on
```


Ça force GDB à afficher en **syntaxe Intel** par défaut (au lieu d'AT&T qui est cryptique). À faire **maintenant**, ça t'évitera des migraines.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Reprends le programme `voir.asm` ci-dessus. Lance-le dans GDB. Pose un breakpoint sur `_start`. Avance `stepi` après `stepi` et vérifie que :

- Après `mov rax, 10` : `rax = 10`
- Après `mov rbx, 32` : `rbx = 32`
- Après `add rax, rbx` : `rax = 42`

**Autonome :** Écris un programme `calculs.asm` qui fait 5 opérations arithmétiques d'affilée (au choix). **Avant** d'exécuter, écris sur papier ce que tu attends pour `rax` après chaque ligne. Vérifie au GDB.

**Défi :** Lance `voir.asm` dans GDB. Avant `add rax, rbx`, **force** `rbx = 100` avec `set $rbx = 100`. Continue avec `stepi`. Quelle est la valeur finale de `rax` ? (Réponse : 110, car 10 + 100.)

## 🧩 Mini-projet (chapitres 7-9) — Carnet d'observations

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

## ✅ Tu sais maintenant…

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

## 🚩 Checkpoint — Fin de la Partie III

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
