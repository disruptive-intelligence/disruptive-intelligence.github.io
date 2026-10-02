---
title: Chapitre 4 — Environnement de travail et premier programme
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie II — Installer, écrire, exécuter
  - index.md
---

## Le minimum à savoir

### Ce qu'il te faut

Pour suivre ce cours, tu as besoin de **Linux**. Trois options :

1. **Linux natif** (Ubuntu, Debian, Fedora…). Idéal.
2. **WSL2 sous Windows** (recommandé Windows 10/11). Suis [https://learn.microsoft.com/windows/wsl/install](https://learn.microsoft.com/windows/wsl/install) puis installe Ubuntu.
3. **Machine virtuelle** (VirtualBox, VMware…) avec Ubuntu/Debian. Fonctionne très bien.

> **Note :** macOS n'est pas un bon choix pour ce cours. Les syscalls sont différents, l'ABI est différente, GDB est limité. Si tu es sur Mac, utilise une VM Linux.

### Les outils à installer

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


### (Recommandé) Installer pwndbg pour un GDB plus lisible

GDB par défaut, c'est austère. Avec **pwndbg**, c'est nettement plus pédagogique (registres affichés automatiquement, pile visible, etc.).

```bash
cd ~
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```


> **Alternative :** `gef` (https://github.com/hugsy/gef) fait à peu près la même chose. Choisis l'un OU l'autre.

### La chaîne de compilation : du `.asm` au programme

```
   mon_prog.asm        ───nasm──→   mon_prog.o     ───ld──→   mon_prog
   (ton code)                       (fichier               (programme
                                     objet)                 exécutable)
```


- **NASM** lit ton fichier source (`.asm`) et le transforme en **fichier objet** (`.o`). Ce fichier contient du code machine **mais n'est pas exécutable** : il manque les "branchements" finaux.
- **`ld`** (le linker) prend le `.o` et en fait un vrai **exécutable** que tu peux lancer.

### Ton premier programme : `exit.asm`

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


### Assembler, linker, exécuter

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

## Très utile en pratique

### Un Makefile minimal

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


### Le drapeau `-g -F dwarf` : indispensable pour GDB

Sans `-g -F dwarf`, GDB peut afficher le code mais ne sait pas relier les instructions à ton fichier source. **Toujours compiler avec ces options en mode pédagogique.**

## ❌ Erreur classique

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


## Exercices

**Guidé :** Crée `exit.asm` comme ci-dessus. Compile-le, exécute-le, et vérifie que `echo $?` affiche bien 42.

**Autonome :** Modifie le programme pour qu'il retourne **123** au lieu de 42. Recompile, relance, vérifie.

**Défi :** Que se passe-t-il si tu mets `255` ? Et `256` ? Et `1000` ? **Indice :** le code de retour Unix est limité à 8 bits non signés (0-255). Au-delà, il "boucle".

## ✅ Tu sais maintenant…

- Installer **NASM, ld, gcc, GDB**
- (Optionnellement) installer **pwndbg**
- La chaîne : `.asm → .o → exécutable`
- Écrire un programme minimal avec `section .text`, `global _start`, `_start:` et `syscall`
- Utiliser **`nasm -f elf64`** et **`ld`** pour compiler
- Récupérer le code de retour avec **`echo $?`**
- Écrire un **Makefile** simple pour automatiser

---
