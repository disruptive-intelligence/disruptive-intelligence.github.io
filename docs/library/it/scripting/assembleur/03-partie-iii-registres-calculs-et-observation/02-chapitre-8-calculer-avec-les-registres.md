---
title: Chapitre 8 — Calculer avec les registres
source: IT/07 Scripting & programmation/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie III — Registres, calculs et observation
  - index.md
---

## Le minimum à savoir

### L'arithmétique de base

L'assembleur sait faire les 4 opérations classiques, plus quelques instructions utiles :

| Instruction | Effet | Exemple |
|-------------|-------|---------|
| **`add`** | addition | `add rax, rbx` → `rax = rax + rbx` |
| **`sub`** | soustraction | `sub rax, rbx` → `rax = rax - rbx` |
| **`inc`** | incrémenter de 1 | `inc rax` → `rax = rax + 1` |
| **`dec`** | décrémenter de 1 | `dec rax` → `rax = rax - 1` |
| **`neg`** | négation (opposé) | `neg rax` → `rax = -rax` |
| **`imul`** | multiplication signée | `imul rax, rbx` → `rax = rax * rbx` |

> **Format identique à `mov` :** destination à gauche, source à droite. La destination reçoit le résultat.

### Exemple complet

```nasm
section .text
global _start
_start:
    mov rax, 10
    mov rbx, 3
    add rax, rbx       ; rax = 10 + 3 = 13
    sub rax, 5         ; rax = 13 - 5 = 8
    inc rax            ; rax = 9
    dec rax            ; rax = 8
    imul rax, rbx      ; rax = 8 * 3 = 24
    neg rax            ; rax = -24

    ; on sort avec rax en code de retour (cf. ci-dessous)
    mov rdi, rax       ; copie le résultat dans rdi
    mov rax, 60        ; syscall exit
    syscall
```


> **Astuce pédagogique :** comme on ne sait pas encore afficher un nombre proprement (il faut le convertir en texte, ch. 14), on **utilise le code de retour comme canal de sortie** pour vérifier nos calculs.

Compile, exécute, regarde :

```bash
make calcul
./calcul
echo $?              # → 232  (parce que -24 en non signé sur 8 bits = 232)
```


Le code de retour est limité à 0-255 (8 bits non signés). Pour des résultats simples, ça suffit largement.

### La multiplication : `imul`

```nasm
mov rax, 6
mov rbx, 7
imul rax, rbx        ; rax = 42
```


Tu peux aussi faire :

```nasm
imul rax, rbx, 5     ; rax = rbx * 5  (trois opérandes !)
imul rax, 3          ; rax = rax * 3
```


> **`imul` vs `mul` :** `imul` est la multiplication **signée** (qui gère les nombres négatifs correctement). `mul` est la version non signée, à 1 opérande, et plus pénible. **Utilise `imul` par défaut.**

### La division : `idiv` (prudemment)

`idiv` est plus tordue. Elle divise un nombre **128 bits** (formé par `rdx:rax`) par son opérande.

```nasm
mov rax, 100
mov rdx, 0          ; ESSENTIEL pour des nombres POSITIFS : partie haute à 0
mov rbx, 7
idiv rbx            ; rax = 100 / 7 = 14, rdx = 100 % 7 = 2
```


**Avant un `idiv`, il faut préparer `rdx` :**

- Pour un dividende **positif** (le cas habituel en pédagogie) : `mov rdx, 0` ou `xor rdx, rdx`.
- Pour un dividende **signé** qui peut être négatif : utilise **`cqo`**. Cette instruction étend le bit de signe de `rax` dans `rdx` (donc `rdx` devient `0` si `rax > 0`, ou `0xFFFFFFFFFFFFFFFF` si `rax < 0`).

```nasm
mov rax, -100
cqo                 ; rdx = 0xFFFFFFFFFFFFFFFF (extension du signe)
mov rbx, 7
idiv rbx            ; rax = -100 / 7 = -14, rdx = -2
```


> **Piège classique :** si tu mets `rdx = 0` alors que `rax` est négatif, le CPU interprète `rdx:rax` comme un énorme nombre positif. Résultat erroné garanti. **Avec `idiv` et des négatifs, toujours `cqo`.**

| Après `idiv` | Contenu |
|--------------|---------|
| `rax` | **quotient** |
| `rdx` | **reste** (modulo) |

## Très utile en pratique

### Pourquoi pas d'affichage du résultat ?

Afficher un entier nécessite de le **convertir en texte** (chiffre par chiffre, en ASCII). On apprend cette conversion au chapitre 14. Pour l'instant :

- Soit on utilise `mov rdi, rax` puis `exit` pour voir le résultat dans `echo $?`.
- Soit on regarde dans GDB (chapitre suivant).

### Récapitulatif des opérandes

| Instruction | Opérandes valides |
|-------------|-------------------|
| `add rax, 5` | registre, immédiate ✓ |
| `add rax, rbx` | registre, registre ✓ |
| `add rax, [var]` | registre, mémoire ✓ |
| `add [var], rax` | mémoire, registre ✓ |
| `add [a], [b]` | ❌ INTERDIT comme pour `mov` |

La règle "pas de mémoire-à-mémoire directe" vaut pour **toutes** les instructions arithmétiques.

### Comparer avec Python

| Python | Assembleur |
|--------|------------|
| `a = 5` | `mov rax, 5` |
| `a = b` | `mov rax, rbx` |
| `a += b` | `add rax, rbx` |
| `a -= b` | `sub rax, rbx` |
| `a *= b` | `imul rax, rbx` |
| `a, b = b, a` | (chapitre 18 avec push/pop, ou 3 mov via rcx) |

## Bonus

### `lea` pour des additions rapides

Petite astuce qu'on creuse au chapitre 12 : `lea` permet de faire **`rax = rbx + rcx`** en une instruction :

```nasm
lea rax, [rbx + rcx]    ; rax = rbx + rcx  (sans toucher aux flags)
```


Tu verras `lea` partout en reverse engineering pour cette raison.

## ❌ Erreur classique

```
Croire que le résultat s'affiche
→ Non. On le met dans un registre. Pour voir : GDB ou code de retour.

Écraser un registre dont on a encore besoin
→ Classique : mov rax, calcul ; mov rax, autre_chose → premier résultat perdu.

Oublier rdx = 0 avant idiv
→ Bug silencieux ou crash. À retenir absolument.

Utiliser mul au lieu de imul pour des nombres positifs
→ mul est à 1 opérande et utilise rdx:rax. imul est plus simple.

Croire que add rax, [a], [b] existe
→ Non. add prend exactement 2 opérandes.

Confondre signé et non signé
→ -1 signé = 0xFFFFFFFFFFFFFFFF. En non signé, c'est un énorme nombre.
```


## Exercices

**Guidé :** Écris un programme qui calcule `(5 + 3) * 2` et place le résultat dans le code de retour. Vérifie avec `echo $?` que tu obtiens **16**.

**Autonome :** Écris un programme qui calcule `100 / 3` (quotient dans `rdi`) puis quitte. `echo $?` doit afficher **33**.

**Défi :** Calcule la suite : `((10 - 2) * 3 + 7) / 5`. Donne le résultat via le code de retour.

> **Réponse attendue :** `((10-2)*3+7)/5 = (24+7)/5 = 31/5 = 6` (reste 1).

## 🧩 Mini-projet (chapitres 7-8) — Mini-calculatrice

Écris `calc.asm` qui calcule sans aucune saisie (valeurs codées en dur) :

- Une variable `a dq 50` et `b dq 7`
- Affiche le code de retour égal à `(a + b) - (a / b)`

Étapes :

1. Charge `a` et `b` dans des registres.
2. Calcule `a + b` dans un registre.
3. Calcule `a / b` (attention `rdx = 0`) dans un autre.
4. Soustrais.
5. Mets le résultat dans `rdi` et appelle `exit`.

Résultat attendu : `(50 + 7) - (50 / 7) = 57 - 7 = 50`.

## ✅ Tu sais maintenant…

- Faire **addition, soustraction, multiplication, division**
- Utiliser **`inc`** et **`dec`** pour ±1
- Utiliser **`neg`** pour l'opposé
- La particularité d'**`idiv`** (quotient dans `rax`, reste dans `rdx`, `rdx = 0` avant pour des positifs, **`cqo` pour des signés négatifs**)
- Utiliser le **code de retour** comme canal de sortie temporaire
- Pourquoi on ne **voit pas** encore le résultat à l'écran

---
