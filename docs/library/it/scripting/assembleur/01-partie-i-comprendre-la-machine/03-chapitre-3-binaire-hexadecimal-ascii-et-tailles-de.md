---
title: Chapitre 3 — Binaire, hexadécimal, ASCII et tailles de données
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie I — Comprendre LA machine
  - index.md
---

## Le minimum à savoir

### Bit et octet

- Un **bit**, c'est la plus petite unité d'information possible : `0` ou `1`.
- Un **octet** (en anglais : *byte*), c'est **8 bits** mis côte à côte.

Un octet peut donc prendre 2⁸ = 256 valeurs différentes, de 0 à 255.

```
   1 octet  =  8 bits
   ┌─┬─┬─┬─┬─┬─┬─┬─┐
   │1│0│1│1│0│1│0│1│   →   en décimal : 181
   └─┴─┴─┴─┴─┴─┴─┴─┘
```


### Binaire (base 2)

Le binaire utilise **seulement 0 et 1**. Chaque position vaut une puissance de 2 :

```
  Position :  7    6    5    4    3    2    1    0
  Valeur   : 128   64   32   16    8    4    2    1
  Bit      :  1    0    1    1    0    1    0    1   →  128+32+16+4+1 = 181
```


En NASM, on écrit le binaire avec le préfixe `0b` : `0b10110101`.

### Hexadécimal (base 16)

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

### Pourquoi l'hexadécimal partout en assembleur ?

Parce qu'**un octet = exactement 2 chiffres hexadécimaux**. C'est ultra-pratique.

```
  Binaire     :  1011 0101
  Hexadécimal :    B    5    →   0xB5
  Décimal     :    181
```


GDB, objdump, les dumps mémoire, les adresses : **tout** s'affiche en hexa. Tu vas en voir partout. Apprivoise-le maintenant.

### Conversions de base

#### Hexa → décimal

`0xFF` = 15 × 16 + 15 = 255
`0x10` = 1 × 16 + 0 = **16** (et non 10 !)
`0x100` = 1 × 256 + 0 + 0 = **256**

#### Décimal → hexa

42 = 2 × 16 + 10 → `0x2A`
255 = 15 × 16 + 15 → `0xFF`
1000 = 3 × 256 + 14 × 16 + 8 → `0x3E8`

> **Astuce :** Linux propose `printf "%x\n" 1000` qui te donne directement la conversion.

### Les tailles de données en x86-64

| Nom | Taille | Plage non signée | Exemples |
|-----|--------|------------------|----------|
| **byte** | 8 bits = 1 octet | 0 à 255 | un caractère ASCII |
| **word** | 16 bits = 2 octets | 0 à 65 535 | un petit entier |
| **dword** | 32 bits = 4 octets | 0 à 4 294 967 295 | un entier classique |
| **qword** | 64 bits = 8 octets | 0 à 18 446 744 073 709 551 615 | un long entier, une adresse |

> **À retenir :** sur x86-64, une **adresse mémoire** fait toujours **8 octets (qword)**. C'est pour ça que tous nos pointeurs feront 8 octets.

### ASCII : comment l'ordinateur stocke du texte

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

## Très utile en pratique

### Lire un dump mémoire

Voici ce que GDB peut t'afficher pour une chaîne en mémoire :

```
0x404000:  48  65  6c  6c  6f  21  0a  00
```


Tu lis : `0x48 = 'H'`, `0x65 = 'e'`, `0x6c = 'l'`, `0x6c = 'l'`, `0x6f = 'o'`, `0x21 = '!'`, `0x0a = '\n'`, `0x00 = '\0'`.

Donc la chaîne en mémoire, c'est `"Hello!\n\0"`.

### Outils Linux pour convertir

```bash
printf "%x\n" 255          # Décimal → hexa  → ff
printf "%d\n" 0xff         # Hexa → décimal  → 255
printf "%d\n" 0b1010       # Binaire → décimal (selon bash)
echo "obase=2; 42" | bc    # Décimal → binaire  → 101010
```


## Bonus

### Aperçu rapide des nombres négatifs (complément à 2)

Comment représenter `-1` avec seulement des 0 et des 1 ? Réponse simple : `-1` (en 8 bits) est représenté par `0xFF` (255 non signé). Le CPU interprète différemment selon le contexte (instruction signée ou non signée). On creuse ça dans l'**Annexe D**. Pour l'instant, retiens que `-1` = `0xFFFFFFFFFFFFFFFF` en 64 bits.

### Little-endian (aperçu)

Quand on stocke un `qword` en mémoire, **les octets de poids faible sont écrits en premier**. C'est ce qu'on appelle **little-endian**. Donc le nombre `0x1234` en mémoire ressemble à `34 12 00 00 00 00 00 00`. Pas intuitif au début ! On en reparle dans l'**Annexe E**.

## ❌ Erreur classique

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


## Exercices

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

## ✅ Tu sais maintenant…

- Ce qu'est un **bit**, un **octet**, un **word**, un **dword**, un **qword**
- Compter en **binaire**, en **décimal** et en **hexadécimal**
- Convertir entre les trois bases
- Pourquoi l'**hexadécimal** est partout en assembleur
- Le lien entre un **caractère** et son **code ASCII**
- Pourquoi `'5'` ≠ `5`
- (Aperçu) que les nombres négatifs et le little-endian seront vus en annexe

---
