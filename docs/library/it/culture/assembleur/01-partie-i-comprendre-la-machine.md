---
title: PARTIE I — COMPRENDRE LA MACHINE
source: IT/Culture/Assembleur.md
note: Assembleur
chapter: 1
chapters: 10
---

---


## Chapitre 1 — Qu'est-ce que l'assembleur et pourquoi l'apprendre

### Le minimum à savoir

#### Les trois niveaux de langage

Quand tu écris un programme, il existe trois niveaux d'écriture, du plus humain au plus proche de la machine :

```
   PYTHON              C            ASSEMBLEUR        CODE MACHINE
 print("Hi")    printf("Hi");      mov rax, 1        01001000 10110000
                                   mov rdi, 1        00000001 ...
                                   mov rsi, msg
                                   mov rdx, 2
                                   syscall

  Très lisible    Moyennement      Une instruction    Que des 0 et 1
  pour l'humain   technique        par ligne          Que le CPU lit
```

- **Python**, c'est presque du français.
- **C**, c'est plus court mais déjà technique.
- **Assembleur**, c'est l'étape juste avant le code machine : chaque ligne correspond à **une instruction** que le CPU exécute.
- **Code machine**, c'est ce que la CPU lit vraiment : que des `0` et `1`. Personne n'écrit ça à la main.

#### Qu'est-ce que l'assembleur, exactement ?

L'assembleur, c'est **le langage du CPU, mais écrit avec des mots** au lieu de chiffres binaires. Chaque instruction (`mov`, `add`, `cmp`…) correspond à **un opcode**, c'est-à-dire à un motif binaire précis que le CPU reconnaît.

> **Important :** Le mot "assembleur" désigne **deux choses** :
> - Le **langage** (les mots `mov`, `add`, `jmp`…).
> - Le **logiciel** qui traduit ce langage en code machine. Dans ce cours, ce logiciel s'appelle **NASM**.

#### Pourquoi l'apprendre aujourd'hui ?

Tu te demandes peut-être : "Si Python existe, pourquoi apprendre quelque chose d'aussi bas niveau ?". Voici les vraies raisons :

| Cas d'usage | À quoi ça sert |
|-------------|----------------|
| **Reverse engineering** | Comprendre un programme dont tu n'as pas le code source (logiciel propriétaire, malware, binaire mystérieux) |
| **CTF / cybersécurité** | Les épreuves de catégorie "reverse" et "pwn" demandent toutes de lire de l'assembleur |
| **Debugging avancé** | Quand ton programme C plante avec un `segfault` cryptique, GDB te montre de l'assembleur |
| **Analyse de malware** | Les virus sont des binaires ; les analyser, c'est lire de l'assembleur |
| **Optimisation critique** | Dans certains cas (jeux, compression, crypto), connaître l'assembleur permet d'optimiser à l'extrême |
| **Comprendre les bugs "bizarres"** | Buffer overflow, integer overflow, race conditions… s'expliquent au niveau machine |
| **Curiosité légitime** | Comprendre comment ton ordinateur fonctionne *vraiment* |

#### Écrire de l'ASM vs lire de l'ASM

Une distinction cruciale pour ce cours :

- **Écrire de l'assembleur** est rare. Très peu de gens écrivent des programmes entiers en ASM aujourd'hui.
- **Lire de l'assembleur** est très courant. Quiconque fait du reverse, du CTF, ou du debug profond le fait tous les jours.

> **Ce cours t'apprend à écrire d'abord, pour pouvoir lire ensuite.** Tu ne pourras jamais lire correctement un langage que tu ne sais pas écrire un minimum.

### Très utile en pratique

#### Pourquoi l'ASM est "verbeux"

En Python, tu écris :

```python
c = a + b
```

C'est **une ligne**, et elle fait trois choses : lire `a`, lire `b`, additionner, stocker dans `c`.

En assembleur, ces quatre actions sont **explicites** :

```nasm
mov rax, [a]    ; 1. Charger la valeur de 'a' dans le registre rax
add rax, [b]    ; 2. Ajouter la valeur de 'b' à rax
mov [c], rax    ; 3. Ranger le résultat de rax dans 'c'
```

> **À retenir :** l'assembleur est verbeux parce qu'il **n'a rien à cacher**. Ce que Python te cache (le chargement, le stockage, l'allocation mémoire), l'assembleur te le montre.

#### Le même programme à trois niveaux

Voici "Bonjour" en Python, C et assembleur. Tu ne dois rien comprendre, juste **regarder** :

**Python :**
```python
print("Bonjour")
```

**C :**
```c
#include <stdio.h>
int main() {
    printf("Bonjour\n");
    return 0;
}
```

**Assembleur (x86-64, Linux, syntaxe Intel) :**
```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg

section .text
global _start
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

Plus on descend, plus c'est verbeux. **Et c'est normal.** Plus on descend, plus chaque opération est explicite.

### ❌ Erreur classique

```
Croire qu'il faut être électronicien pour apprendre l'ASM
→ Faux. On ne touche jamais à du matériel.

Croire que l'ASM va "remplacer" Python ou C
→ Faux. Ce sont des outils différents pour des usages différents.

Croire qu'il faut tout comprendre dès le premier programme
→ Faux. On recopie sans comprendre au début, on comprend après.

Croire que l'ASM est "magique" ou ésotérique
→ Faux. C'est juste verbeux et minutieux.
```

### Exercices

**Guidé :** En 3 phrases, explique à un ami fictif ce qu'est l'assembleur et pourquoi tu l'apprends.

**Autonome :** Cite **3 métiers ou situations** où savoir lire de l'assembleur est utile. Pour chacun, explique en une phrase pourquoi.

**Défi :** Reprends les trois versions du "Bonjour" ci-dessus. Compte le nombre de **lignes utiles** dans chaque version (sans les lignes vides). Que conclus-tu sur le rapport "lisibilité / nombre de lignes" ?

### ✅ Tu sais maintenant…

- Ce qu'est l'assembleur (langage **et** logiciel)
- Les trois niveaux de langage (Python, C, ASM)
- Pourquoi l'assembleur est verbeux
- À quoi sert l'ASM en cybersécurité et reverse
- La différence entre **écrire** et **lire** de l'assembleur

---


## Chapitre 2 — CPU, RAM, registres : le modèle mental minimum

### Le minimum à savoir

#### Où vivent les données et le code ?

Pour comprendre l'assembleur, il faut un modèle mental clair de **ce qui se passe dans l'ordinateur** (version simplifiée — les CPU modernes font en réalité plein d'optimisations comme le pipelining et l'exécution spéculative, mais ce n'est pas le sujet ici). Inutile d'être ingénieur en électronique — il suffit d'avoir la bonne image en tête.

```
┌────────────────────────────────────────────────────────────┐
│                         ORDINATEUR                          │
│                                                             │
│   ┌──────────────────┐         ┌─────────────────────────┐ │
│   │       CPU        │         │          RAM            │ │
│   │                  │         │                         │ │
│   │  ┌────┬────┬───┐ │         │   ┌─────┬─────┬─────┐  │ │
│   │  │rax │rbx │...│ │ ←─────→ │   │ 0x1 │ 0x2 │ ... │  │ │
│   │  └────┴────┴───┘ │         │   └─────┴─────┴─────┘  │ │
│   │   (registres)    │         │   (adresses mémoire)    │ │
│   └──────────────────┘         └─────────────────────────┘ │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

- **Le CPU**, c'est la puce qui **exécute** les instructions. Une seule à la fois, mais des milliards par seconde.
- **La RAM**, c'est un immense tableau d'octets numérotés. Chaque numéro est une **adresse**. Le code et les données y vivent.
- **Les registres**, ce sont des mini-cases de stockage **à l'intérieur du CPU**. Ultra-rapides, mais peu nombreuses.

#### L'analogie à garder en tête

```
RAM         = ta bibliothèque  (grande, mais il faut se lever pour y aller)
Registres   = ton bureau       (petit, mais tout sous la main)
CPU         = toi qui travailles
Instruction = une action que tu fais
```

> **Règle d'or :** en pratique, beaucoup d'opérations passent par les registres, et **une instruction x86-64 ne peut pas manipuler deux zones mémoire en même temps**. Tu peux lire depuis la mémoire (`add rax, [x]`) ou écrire vers la mémoire (`add [x], rax`), mais dès qu'il faut **combiner deux valeurs mémoire**, il faut d'abord en charger une dans un registre.

#### Disque dur ≠ RAM ≠ Registres

C'est une confusion classique :

| Stockage | Capacité typique | Vitesse | Volatilité |
|----------|------------------|---------|------------|
| **Disque dur / SSD** | 500 Go - plusieurs To | Lent | Persistant (survit à l'extinction) |
| **RAM** | 8 Go - 64 Go | Rapide | Volatile (vidée à l'extinction) |
| **Registres** | 16 cases × 8 octets = 128 octets | Ultra-rapide | Volatile (vidée à l'extinction) |

Quand tu lances un programme, son fichier passe du **disque** vers la **RAM**. Puis le CPU **charge** des morceaux de la RAM dans ses **registres** pour les manipuler.

#### Les principaux registres x86-64

Sur un CPU x86-64 (la grande majorité des PC modernes), il y a 16 registres généraux de 64 bits. Tu n'as pas besoin de tous les retenir tout de suite. Voici ceux qu'on va utiliser :

| Registre | Nom historique | Usage typique |
|----------|----------------|---------------|
| **`rax`** | **A**ccumulator | Résultats de calculs, valeur de retour de fonction |
| **`rbx`** | **B**ase | Variable générale (à préserver) |
| **`rcx`** | **C**ounter | Compteur de boucle |
| **`rdx`** | **D**ata | Données générales, partie haute des résultats |
| **`rsi`** | **S**ource **I**ndex | Adresse source (copies, chaînes) |
| **`rdi`** | **D**estination **I**ndex | Adresse destination, premier argument de fonction |
| **`rsp`** | **S**tack **P**ointer | **Pointeur de pile** (chapitre 18) — n'y touche pas pour l'instant |
| **`rbp`** | **B**ase **P**ointer | **Base de la pile** (chapitre 20) |
| **`r8`** à **`r15`** | (nouveaux en x86-64) | Registres généraux supplémentaires |
| **`rip`** | **I**nstruction **P**ointer | Pointe sur la **prochaine instruction à exécuter** (en debug, c'est celle affichée comme courante). On ne le modifie pas directement |

> **À retenir tout de suite :** `rax`, `rdi`, `rsi`, `rdx`. Ce sont ceux qu'on utilise dès le chapitre 6.

#### Les sous-registres : `rax`, `eax`, `ax`, `al`

Chaque registre 64 bits peut être manipulé à différentes tailles. **Ce ne sont pas des registres séparés** : ce sont des **zooms** sur le même registre.

```
   ┌─────────────────────────────────────────────────────────────────┐
   │                          rax (64 bits)                          │
   │                                                                 │
   │                                ┌────────────────────────────────┤
   │                                │       eax (32 bits)            │
   │                                │                  ┌─────────────┤
   │                                │                  │ ax (16 bits)│
   │                                │                  ├──────┬──────┤
   │                                │                  │  ah  │  al  │
   │                                │                  │ (8b) │ (8b) │
   └────────────────────────────────┴──────────────────┴──────┴──────┘
```

| Taille | 64 bits | 32 bits | 16 bits | 8 bits hauts | 8 bits bas |
|--------|---------|---------|---------|--------------|------------|
| Registre A | `rax` | `eax` | `ax` | `ah` | `al` |
| Registre B | `rbx` | `ebx` | `bx` | `bh` | `bl` |
| Registre C | `rcx` | `ecx` | `cx` | `ch` | `cl` |
| Registre D | `rdx` | `edx` | `dx` | `dh` | `dl` |
| Source | `rsi` | `esi` | `si` | — | `sil` |
| Destination | `rdi` | `edi` | `di` | — | `dil` |
| Nouveaux | `r8`-`r15` | `r8d`-`r15d` | `r8w`-`r15w` | — | `r8b`-`r15b` |

> **À retenir :** si tu écris `mov al, 5`, tu modifies seulement les **8 bits bas** de `rax`. Le reste de `rax` n'est pas touché (sauf cas particulier en 32 bits, voir Annexe B).

### Très utile en pratique

#### Comment voir les registres ?

Tu ne peux pas voir les registres en regardant ton écran. Il faut un **debugger** comme GDB. C'est exactement ce qu'on apprendra au chapitre 9.

#### Combien de registres utilise un vrai programme ?

Un programme C compilé utilise typiquement **5 à 10 registres** différents à un moment donné. Les 16 disponibles suffisent largement pour des calculs. Quand on en a besoin de plus, on **passe par la mémoire** (la pile, plus tard).

#### `rip` : le registre que tu ne touches jamais

`rip` (Instruction Pointer) contient l'adresse de la **prochaine instruction** à exécuter. Tu ne le modifies **jamais** directement avec `mov`. Il est modifié par :
- Le simple fait d'exécuter une instruction (`rip` avance automatiquement).
- Les instructions de saut (`jmp`, `je`, `call`, `ret`…) qu'on verra plus tard.

### ❌ Erreur classique

```
Confondre RAM et disque dur
→ Ton programme ne tourne pas depuis le disque, il tourne depuis la RAM.

Croire qu'un registre est une variable Python
→ Une variable Python vit en mémoire (RAM). Un registre vit dans le CPU.

Croire que rax et eax sont des registres différents
→ NON. eax = la moitié basse de rax. Modifier eax modifie aussi rax.

Modifier rip directement
→ Interdit. Utilise jmp, call, ret. Sinon, crash.

Croire qu'on peut faire mov [a], [b] (mémoire à mémoire direct)
→ Interdit en x86-64. Il faut passer par un registre pour combiner
   deux zones mémoire.
```

### Exercices

**Guidé :** Complète ce tableau dans ton cahier :

| Registre 64 bits | Sous-registre 32 bits | Sous-registre 8 bits bas |
|------------------|----------------------|--------------------------|
| `rax` | ? | ? |
| `rcx` | ? | ? |
| `r10` | ? | ? |

**Autonome :** Explique en 3 phrases, avec tes propres mots, la différence entre :
- un registre,
- une case mémoire (RAM),
- un fichier sur disque.

**Défi :** Si je dis `mov al, 0xFF`, quelle est la valeur de `rax` après, **sachant que `rax` valait 0 avant** ? Et si `rax` valait `0x1234567890ABCDEF` avant ?

> **Indice :** `mov al` ne touche que les 8 bits bas. (Réponse au chapitre 7.)

### ✅ Tu sais maintenant…

- Ce qu'est un **CPU**, une **RAM**, un **registre**
- La différence registre / mémoire / disque
- Les **principaux registres** x86-64 (`rax`, `rbx`, `rcx`, `rdx`, `rsi`, `rdi`, `r8`-`r15`, `rsp`, `rbp`, `rip`)
- Les **sous-registres** (`rax`, `eax`, `ax`, `al`)
- Que **les registres sont l'espace de travail principal** du CPU (même si certaines instructions peuvent lire ou modifier directement la mémoire)
- Pourquoi on ne peut pas faire un calcul mémoire-à-mémoire direct

---


## Chapitre 3 — Binaire, hexadécimal, ASCII et tailles de données

### Le minimum à savoir

#### Bit et octet

- Un **bit**, c'est la plus petite unité d'information possible : `0` ou `1`.
- Un **octet** (en anglais : *byte*), c'est **8 bits** mis côte à côte.

Un octet peut donc prendre 2⁸ = 256 valeurs différentes, de 0 à 255.

```
   1 octet  =  8 bits
   ┌─┬─┬─┬─┬─┬─┬─┬─┐
   │1│0│1│1│0│1│0│1│   →   en décimal : 181
   └─┴─┴─┴─┴─┴─┴─┴─┘
```

#### Binaire (base 2)

Le binaire utilise **seulement 0 et 1**. Chaque position vaut une puissance de 2 :

```
  Position :  7    6    5    4    3    2    1    0
  Valeur   : 128   64   32   16    8    4    2    1
  Bit      :  1    0    1    1    0    1    0    1   →  128+32+16+4+1 = 181
```

En NASM, on écrit le binaire avec le préfixe `0b` : `0b10110101`.

#### Hexadécimal (base 16)

L'hexadécimal utilise **16 chiffres** : `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F`.

| Hexa | Décimal | Binaire |
|------|---------|---------|
| `0` | 0 | `0000` |
| `1` | 1 | `0001` |
| `5` | 5 | `0101` |
| `9` | 9 | `1001` |
| `A` | 10 | `1010` |
| `B` | 11 | `1011` |
| `F` | 15 | `1111` |

En NASM, on écrit l'hexadécimal avec le préfixe `0x` : `0xFF`, `0x41`, `0x100`.

#### Pourquoi l'hexadécimal partout en assembleur ?

Parce qu'**un octet = exactement 2 chiffres hexadécimaux**. C'est ultra-pratique.

```
  Binaire     :  1011 0101
  Hexadécimal :    B    5    →   0xB5
  Décimal     :    181
```

GDB, objdump, les dumps mémoire, les adresses : **tout** s'affiche en hexa. Tu vas en voir partout. Apprivoise-le maintenant.

#### Conversions de base

##### Hexa → décimal

`0xFF` = 15 × 16 + 15 = 255
`0x10` = 1 × 16 + 0 = **16** (et non 10 !)
`0x100` = 1 × 256 + 0 + 0 = **256**

##### Décimal → hexa

42 = 2 × 16 + 10 → `0x2A`
255 = 15 × 16 + 15 → `0xFF`
1000 = 3 × 256 + 14 × 16 + 8 → `0x3E8`

> **Astuce :** Linux propose `printf "%x\n" 1000` qui te donne directement la conversion.

#### Les tailles de données en x86-64

| Nom | Taille | Plage non signée | Exemples |
|-----|--------|------------------|----------|
| **byte** | 8 bits = 1 octet | 0 à 255 | un caractère ASCII |
| **word** | 16 bits = 2 octets | 0 à 65 535 | un petit entier |
| **dword** | 32 bits = 4 octets | 0 à 4 294 967 295 | un entier classique |
| **qword** | 64 bits = 8 octets | 0 à 18 446 744 073 709 551 615 | un long entier, une adresse |

> **À retenir :** sur x86-64, une **adresse mémoire** fait toujours **8 octets (qword)**. C'est pour ça que tous nos pointeurs feront 8 octets.

#### ASCII : comment l'ordinateur stocke du texte

Un ordinateur ne sait pas ce qu'est une "lettre". Il ne sait stocker que des nombres. Pour stocker du texte, on utilise une **table de correspondance** : la table ASCII.

Chaque caractère correspond à un nombre de 0 à 127 :

| Caractère | Décimal | Hexa |
|-----------|---------|------|
| `' '` (espace) | 32 | `0x20` |
| `'0'` | 48 | `0x30` |
| `'9'` | 57 | `0x39` |
| `'A'` | 65 | `0x41` |
| `'Z'` | 90 | `0x5A` |
| `'a'` | 97 | `0x61` |
| `'z'` | 122 | `0x7A` |
| `'\n'` (saut de ligne) | 10 | `0x0A` |

**Quelques règles à retenir :**

- Les chiffres `'0'` à `'9'` se suivent : `0x30` à `0x39`.
- Les majuscules `'A'` à `'Z'` se suivent : `0x41` à `0x5A`.
- Les minuscules `'a'` à `'z'` se suivent : `0x61` à `0x7A`.
- Pour passer de majuscule à minuscule : **ajouter 32** (`0x20`).
- Pour transformer le caractère `'5'` en nombre `5` : **soustraire 48** (`0x30`).

> **Important :** Le caractère `'5'` (qui vaut 53 en mémoire) **n'est pas** le nombre 5 ! C'est une confusion classique qu'on revoit au chapitre 14.

### Très utile en pratique

#### Lire un dump mémoire

Voici ce que GDB peut t'afficher pour une chaîne en mémoire :

```
0x404000:  48  65  6c  6c  6f  21  0a  00
```

Tu lis : `0x48 = 'H'`, `0x65 = 'e'`, `0x6c = 'l'`, `0x6c = 'l'`, `0x6f = 'o'`, `0x21 = '!'`, `0x0a = '\n'`, `0x00 = '\0'`.

Donc la chaîne en mémoire, c'est `"Hello!\n\0"`.

#### Outils Linux pour convertir

```bash
printf "%x\n" 255          # Décimal → hexa  → ff
printf "%d\n" 0xff         # Hexa → décimal  → 255
printf "%d\n" 0b1010       # Binaire → décimal (selon bash)
echo "obase=2; 42" | bc    # Décimal → binaire  → 101010
```

### Bonus

#### Aperçu rapide des nombres négatifs (complément à 2)

Comment représenter `-1` avec seulement des 0 et des 1 ? Réponse simple : `-1` (en 8 bits) est représenté par `0xFF` (255 non signé). Le CPU interprète différemment selon le contexte (instruction signée ou non signée). On creuse ça dans l'**Annexe D**. Pour l'instant, retiens que `-1` = `0xFFFFFFFFFFFFFFFF` en 64 bits.

#### Little-endian (aperçu)

Quand on stocke un `qword` en mémoire, **les octets de poids faible sont écrits en premier**. C'est ce qu'on appelle **little-endian**. Donc le nombre `0x1234` en mémoire ressemble à `34 12 00 00 00 00 00 00`. Pas intuitif au début ! On en reparle dans l'**Annexe E**.

### ❌ Erreur classique

```
Lire 0x10 comme 10
→ NON. 0x10 = 16. Le préfixe 0x est essentiel.

Confondre bit et octet
→ Un octet = 8 bits. "8 Go" et "8 Gb" ne sont pas la même chose.

Confondre le caractère '5' et le nombre 5
→ '5' = 53 en mémoire. 5 = 5. Ils ne se manipulent pas pareil.

Croire qu'un nombre s'écrit "0F" sans préfixe
→ En NASM, écris 0x0F ou 0Fh. Sans préfixe, c'est ambigu.

Confondre b (binaire NASM) avec le b de bx (registre)
→ 0b1010 (binaire), bx (registre). Le contexte tranche.
```

### Exercices

**Guidé :** Convertis ces valeurs (à la main, puis vérifie avec `printf "%x"`) :

| Décimal | Hexadécimal | Binaire |
|---------|-------------|---------|
| 10 | ? | ? |
| 16 | ? | ? |
| 100 | ? | ? |
| 255 | ? | ? |
| 256 | ? | ? |

**Autonome :** Trouve le code ASCII de chaque lettre de ton prénom, en décimal puis en hexa. Vérifie avec :

```bash
echo -n "A" | xxd       # Affiche 41
```

**Défi :** En mémoire, tu vois la séquence d'octets `48 65 6c 6c 6f`. Quelle est la chaîne ? Et que devient-elle si tu **ajoutes 32** à chaque octet ?

### ✅ Tu sais maintenant…

- Ce qu'est un **bit**, un **octet**, un **word**, un **dword**, un **qword**
- Compter en **binaire**, en **décimal** et en **hexadécimal**
- Convertir entre les trois bases
- Pourquoi l'**hexadécimal** est partout en assembleur
- Le lien entre un **caractère** et son **code ASCII**
- Pourquoi `'5'` ≠ `5`
- (Aperçu) que les nombres négatifs et le little-endian seront vus en annexe

---
