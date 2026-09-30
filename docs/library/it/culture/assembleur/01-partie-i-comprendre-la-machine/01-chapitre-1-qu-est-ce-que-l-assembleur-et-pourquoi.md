---
title: Chapitre 1 — Qu'est-ce que l'assembleur et pourquoi l'apprendre
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie I — Comprendre LA machine
  - index.md
---

## Le minimum à savoir

### Les trois niveaux de langage

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

### Qu'est-ce que l'assembleur, exactement ?

L'assembleur, c'est **le langage du CPU, mais écrit avec des mots** au lieu de chiffres binaires. Chaque instruction (`mov`, `add`, `cmp`…) correspond à **un opcode**, c'est-à-dire à un motif binaire précis que le CPU reconnaît.

> **Important :** Le mot "assembleur" désigne **deux choses** :
> - Le **langage** (les mots `mov`, `add`, `jmp`…).
> - Le **logiciel** qui traduit ce langage en code machine. Dans ce cours, ce logiciel s'appelle **NASM**.

### Pourquoi l'apprendre aujourd'hui ?

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

### Écrire de l'ASM vs lire de l'ASM

Une distinction cruciale pour ce cours :

- **Écrire de l'assembleur** est rare. Très peu de gens écrivent des programmes entiers en ASM aujourd'hui.
- **Lire de l'assembleur** est très courant. Quiconque fait du reverse, du CTF, ou du debug profond le fait tous les jours.

> **Ce cours t'apprend à écrire d'abord, pour pouvoir lire ensuite.** Tu ne pourras jamais lire correctement un langage que tu ne sais pas écrire un minimum.

## Très utile en pratique

### Pourquoi l'ASM est "verbeux"

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

### Le même programme à trois niveaux

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

## ❌ Erreur classique

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


## Exercices

**Guidé :** En 3 phrases, explique à un ami fictif ce qu'est l'assembleur et pourquoi tu l'apprends.

**Autonome :** Cite **3 métiers ou situations** où savoir lire de l'assembleur est utile. Pour chacun, explique en une phrase pourquoi.

**Défi :** Reprends les trois versions du "Bonjour" ci-dessus. Compte le nombre de **lignes utiles** dans chaque version (sans les lignes vides). Que conclus-tu sur le rapport "lisibilité / nombre de lignes" ?

## ✅ Tu sais maintenant…

- Ce qu'est l'assembleur (langage **et** logiciel)
- Les trois niveaux de langage (Python, C, ASM)
- Pourquoi l'assembleur est verbeux
- À quoi sert l'ASM en cybersécurité et reverse
- La différence entre **écrire** et **lire** de l'assembleur

---
