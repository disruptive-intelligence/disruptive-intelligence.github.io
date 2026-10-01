---
title: Chapitre 6 — Premier affichage avec write
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie II — Installer, écrire, exécuter
  - index.md
---

## Le minimum à savoir

### Pourquoi il n'y a pas de `print()` en assembleur

En Python, `print("Bonjour")` semble magique. En réalité, sous le capot, Python finit par appeler une **fonction du système** qui écrit dans le terminal. Cette fonction s'appelle **`write`** sous Linux, et c'est un **syscall**.

> **À retenir :** en assembleur, on ne fait pas un `print` magique. On **demande directement au noyau** d'écrire pour nous. Cette demande s'appelle un **syscall** (system call).

### Qu'est-ce qu'un syscall ?

Un syscall, c'est une **demande de service au noyau** : "Noyau, je voudrais écrire ce texte sur l'écran", "ouvre-moi ce fichier", "donne-moi l'heure", etc.

**Analogie :** tu es au restaurant. Tu ne vas pas en cuisine — tu **commandes au serveur**. Le serveur (le noyau) va chercher ton plat (le service) et te le ramène. C'est exactement le rôle d'un syscall.

### La convention de syscall Linux x86-64

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

### Le syscall `write` (numéro 1)

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

### Le syscall `exit` (numéro 60)

Pour **terminer proprement** un programme :

1. **`rax`** : `60` (numéro de `exit`).
2. **`rdi`** : le code de retour (0 = succès).

Sans `exit` à la fin, **ton programme va crasher** (le CPU continuerait à exécuter ce qu'il y a après, qui n'est pas du code valide).

### Ton premier "Hello, World!"

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

## Très utile en pratique

### Pourquoi le `10` dans le message ?

`10` est le code ASCII du **retour ligne** (`\n`). Sans lui, ton message s'affiche, et le prompt du shell apparaît collé sur la même ligne. Tu peux d'ailleurs tester sans, pour voir.

### Pourquoi `len` plutôt que de compter à la main ?

Tu pourrais écrire `mov rdx, 21` à la main (en comptant les caractères). Mais :

- C'est fragile (si tu modifies le message, tu dois recompter).
- C'est source d'erreurs.
- `equ $ - msg` le calcule pour toi à la compilation.

### Les 4 file descriptors essentiels

| FD | Nom | Direction |
|----|-----|-----------|
| `0` | **stdin** | Entrée (clavier) |
| `1` | **stdout** | Sortie standard (écran) |
| `2` | **stderr** | Sortie d'erreur (écran aussi) |
| 3+ | fichiers ouverts | Fichiers que tu as toi-même ouverts |

Pour écrire un message d'erreur, on utilise `rdi = 2` au lieu de `rdi = 1`.

### Afficher plusieurs messages

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

## Bonus

### Trouver les numéros de syscall

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

### Différence syscall vs fonction C

Plus tard (chapitre 21), tu utiliseras `printf` au lieu de `write`. Ce sont **deux choses différentes** :

- `write` est un **syscall** : demande directe au noyau.
- `printf` est une **fonction de la libc** : elle formate du texte, puis appelle `write`.

Pour l'instant, on reste sur `write` : c'est plus simple, plus bas niveau, et plus instructif.

## ❌ Erreur classique

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


## Exercices

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


## 🧩 Mini-projet (chapitres 4-6) — Bannière

Crée un programme `banniere.asm` qui affiche cette bannière à l'écran :

```
==========================================
       BIENVENUE EN ASSEMBLEUR
       x86-64 sous Linux
==========================================
```


Chaque ligne est un message séparé, affiché avec un syscall `write` distinct. Le programme se termine avec `exit(0)`.

> **Bonus :** ajoute une ligne d'espacement au début et à la fin de la bannière.

## ✅ Tu sais maintenant…

- Ce qu'est un **syscall** et pourquoi il existe
- La **convention syscall** Linux x86-64 (`rax`, `rdi`, `rsi`, `rdx`, …)
- Utiliser **`write`** (n°1) pour afficher du texte
- Utiliser **`exit`** (n°60) pour quitter
- La différence **`msg`** (adresse) vs **`[msg]`** (contenu)
- Les file descriptors **0, 1, 2**
- Écrire ton premier programme **réellement utile**

---
