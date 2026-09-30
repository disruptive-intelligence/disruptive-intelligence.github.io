---
title: Chapitre 24 — Reverse engineering débutant avec GDB
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie IX — Lecture de binaires ET reverse débutant
  - index.md
---

## Le minimum à savoir

### Le reverse dynamique vs statique

Tu peux analyser un binaire de deux façons :

| Approche | Outils | Avantage |
|----------|--------|----------|
| **Statique** | `strings`, `objdump`, ghidra | Tu lis sans exécuter |
| **Dynamique** | `gdb`, `ltrace`, `strace` | Tu vois le programme tourner |

Tu maîtrises déjà les bases du statique (ch. 23). Maintenant : le **dynamique avec GDB**, qui complète parfaitement. Souvent, on **combine** les deux : on lit avec objdump, on vérifie avec GDB.

### Charger un binaire inconnu

```bash
gdb ./inconnu
```


Si le binaire est strippé, certaines commandes auront moins d'info. Mais l'essentiel marche pareil.

### Poser des breakpoints sur des adresses

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


### `start` : casser au tout début

```
(gdb) start
```


Si le binaire a un `main`, GDB s'arrête à son tout début. C'est l'équivalent de `break main ; run`. Pratique.

### Observer un programme en cours d'exécution

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

### Repérer un `if` dans le désassemblage

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

### Repérer une boucle dans le désassemblage

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

### Repérer un appel de fonction et ses arguments

```
0x401400:  mov    edi, 0x5         ← 1er arg
0x401405:  mov    esi, 0xa         ← 2ème arg
0x40140a:  call   0x401200 <calc>  ← appel
0x40140f:  mov    [rbp-8], eax     ← stocker le retour
```


**Décodage :** appel de `calc(5, 10)`, résultat stocké dans une locale.

### Suivre une comparaison de mot de passe

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

## Très utile en pratique

### Forcer une condition pour explorer

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


### Examiner ce qui est dans `rdi` quand `printf` est appelé

Pose un breakpoint sur `printf` et regarde le format :

```
(gdb) break printf
(gdb) continue
; ... arrive sur printf ...
(gdb) x/s $rdi
0x402004: "Saisis un mot de passe : "
```


Tu vois ce que **`printf` est sur le point d'afficher**, sans laisser tourner le programme. Très instructif.

### Voir ce que `read`/`scanf` reçoit

Casse après `read` ou `scanf` et regarde le buffer :

```
(gdb) x/s <adresse_buffer>
```


Tu vois ce que l'utilisateur a tapé (idéal pour comprendre comment le programme traite l'entrée).

## Bonus

### `ltrace` et `strace`

Deux outils hors GDB :

- `strace ./prog` : affiche tous les **syscalls** que le programme fait. Tu vois `write(1, "...", 5)`, `read(0, ...)`, etc.
- `ltrace ./prog` : affiche tous les appels à des fonctions de la **libc**.

Pour un débutant qui veut comprendre **vite** ce qu'un binaire fait, c'est une mine d'or.

```bash
ltrace ./crackme
strcmp("monessai", "secret123") = -1
```


Devine quoi : tu viens de **trouver le mot de passe**.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Reprends un de tes binaires (`hello_c` du ch. 21). Lance `gdb ./hello_c`, fais `start`, puis `disas main`, puis `nexti` plusieurs fois en regardant `rdi` à chaque appel à `printf`.

**Autonome :** Compile un petit C qui demande un nombre et **affiche "OK" si == 42, sinon "KO"**. Sans regarder le `.c`, retrouve dans GDB où se trouve le `cmp ..., 42`.

**Défi :** Compile un petit C avec un mot de passe `"secret"` comparé par `strcmp`. Lance-le dans GDB, casse sur `strcmp`, et **affiche le 2ème argument** (le mot de passe attendu) avec `x/s $rsi`.

## 🧩 Mini-projets finaux — 3 Crackmes progressifs

Voici trois **mini-binaires** à reverser. Pour chacun, ton boulot : **trouver le mot de passe**.

Tu peux toi-même les **fabriquer** en compilant les sources C ci-dessous (ce qui te donne un terrain d'entraînement reproductible). En CTF, tu n'aurais que le binaire — mais le but pédagogique est le même.

### Crackme 1 — Le mot de passe en clair (`strings` suffit)

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

### Crackme 2 — Comparaison caractère par caractère

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

### Crackme 3 — Transformation XOR simple

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

## ✅ Tu sais maintenant…

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
