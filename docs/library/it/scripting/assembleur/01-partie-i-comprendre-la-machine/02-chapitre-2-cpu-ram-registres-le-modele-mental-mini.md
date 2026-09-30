---
title: 'Chapitre 2 — CPU, RAM, registres : le modèle mental minimum'
source: IT/Culture/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie I — Comprendre LA machine
  - index.md
---

## Le minimum à savoir

### Où vivent les données et le code ?

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

### L'analogie à garder en tête

```
RAM         = ta bibliothèque  (grande, mais il faut se lever pour y aller)
Registres   = ton bureau       (petit, mais tout sous la main)
CPU         = toi qui travailles
Instruction = une action que tu fais
```


> **Règle d'or :** en pratique, beaucoup d'opérations passent par les registres, et **une instruction x86-64 ne peut pas manipuler deux zones mémoire en même temps**. Tu peux lire depuis la mémoire (`add rax, [x]`) ou écrire vers la mémoire (`add [x], rax`), mais dès qu'il faut **combiner deux valeurs mémoire**, il faut d'abord en charger une dans un registre.

### Disque dur ≠ RAM ≠ Registres

C'est une confusion classique :

| Stockage | Capacité typique | Vitesse | Volatilité |
|----------|------------------|---------|------------|
| **Disque dur / SSD** | 500 Go - plusieurs To | Lent | Persistant (survit à l'extinction) |
| **RAM** | 8 Go - 64 Go | Rapide | Volatile (vidée à l'extinction) |
| **Registres** | 16 cases × 8 octets = 128 octets | Ultra-rapide | Volatile (vidée à l'extinction) |

Quand tu lances un programme, son fichier passe du **disque** vers la **RAM**. Puis le CPU **charge** des morceaux de la RAM dans ses **registres** pour les manipuler.

### Les principaux registres x86-64

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

### Les sous-registres : `rax`, `eax`, `ax`, `al`

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

## Très utile en pratique

### Comment voir les registres ?

Tu ne peux pas voir les registres en regardant ton écran. Il faut un **debugger** comme GDB. C'est exactement ce qu'on apprendra au chapitre 9.

### Combien de registres utilise un vrai programme ?

Un programme C compilé utilise typiquement **5 à 10 registres** différents à un moment donné. Les 16 disponibles suffisent largement pour des calculs. Quand on en a besoin de plus, on **passe par la mémoire** (la pile, plus tard).

### `rip` : le registre que tu ne touches jamais

`rip` (Instruction Pointer) contient l'adresse de la **prochaine instruction** à exécuter. Tu ne le modifies **jamais** directement avec `mov`. Il est modifié par :

- Le simple fait d'exécuter une instruction (`rip` avance automatiquement).
- Les instructions de saut (`jmp`, `je`, `call`, `ret`…) qu'on verra plus tard.

## ❌ Erreur classique

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


## Exercices

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

## ✅ Tu sais maintenant…

- Ce qu'est un **CPU**, une **RAM**, un **registre**
- La différence registre / mémoire / disque
- Les **principaux registres** x86-64 (`rax`, `rbx`, `rcx`, `rdx`, `rsi`, `rdi`, `r8`-`r15`, `rsp`, `rbp`, `rip`)
- Les **sous-registres** (`rax`, `eax`, `ax`, `al`)
- Que **les registres sont l'espace de travail principal** du CPU (même si certaines instructions peuvent lire ou modifier directement la mémoire)
- Pourquoi on ne peut pas faire un calcul mémoire-à-mémoire direct

---
