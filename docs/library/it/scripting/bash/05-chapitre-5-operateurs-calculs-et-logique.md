---
title: Chapitre 5 — Opérateurs, calculs et logique
source: IT/07 Scripting & programmation/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Le calcul en Bash

Bash peut faire des calculs avec des nombres entiers. La syntaxe est `$(( expression ))` :

```bash
#!/bin/bash

a=10
b=3

echo "Addition      : $((a + b))"      # 13
echo "Soustraction  : $((a - b))"      # 7
echo "Multiplication: $((a * b))"      # 30
echo "Division      : $((a / b))"      # 3 (entière, pas de virgule !)
echo "Modulo        : $((a % b))"      # 1 (reste de la division)
```


> **Attention :** la division est **entière**. `10 / 3` donne `3`, pas `3.33`.

### Stocker un résultat

```bash
prix=50
reduction=15
prix_final=$((prix - reduction))
echo "Le prix final est $prix_final euros"
```


### Les opérateurs arithmétiques

| Opérateur | Signification    | Exemple       | Résultat |
| --------- | ---------------- | ------------- | -------- |
| `+`       | Addition         | `$((5 + 3))`  | `8`      |
| `-`       | Soustraction     | `$((5 - 3))`  | `2`      |
| `*`       | Multiplication   | `$((5 * 3))`  | `15`     |
| `/`       | Division entière | `$((5 / 3))`  | `1`      |
| `%`       | Modulo (reste)   | `$((5 % 3))`  | `2`      |
| `**`      | Puissance        | `$((2 ** 3))` | `8`      |

### Comparer des nombres

Pour tester si un nombre est plus grand, plus petit, égal à un autre :

| Opérateur | Signification     | Moyen mnémotechnique     |
| --------- | ----------------- | ------------------------ |
| `-eq`     | Égal              | **eq**ual                |
| `-ne`     | Différent         | **n**ot **e**qual        |
| `-lt`     | Inférieur         | **l**ess **t**han        |
| `-le`     | Inférieur ou égal | **l**ess or **e**qual    |
| `-gt`     | Supérieur         | **g**reater **t**han     |
| `-ge`     | Supérieur ou égal | **g**reater or **e**qual |

```bash
age=25
[[ $age -ge 18 ]]    # Est-ce que 25 ≥ 18 ? → Vrai
[[ $age -eq 30 ]]    # Est-ce que 25 = 30 ? → Faux
```


> **Ne pas confondre :** `=` sert à **affecter** une valeur à une variable (`age=25`). `-eq` sert à **comparer** deux nombres dans un test.

### Comparer des chaînes de texte

| Opérateur   | Signification                |
| ----------- | ---------------------------- |
| `=` ou `==` | Les chaînes sont identiques  |
| `!=`        | Les chaînes sont différentes |
| `-z`        | La chaîne est vide           |
| `-n`        | La chaîne n'est pas vide     |

```bash
nom="Alice"
[[ "$nom" == "Alice" ]]    # Vrai
[[ "$nom" != "Bob" ]]      # Vrai
[[ -z "$nom" ]]            # Faux (pas vide)
```


### Les opérateurs logiques

| Opérateur | Signification                                |
| --------- | -------------------------------------------- |
| `&&`      | ET — les deux conditions doivent être vraies |
| `\|\|`    | OU — au moins une doit être vraie            |
| `!`       | NON — inverse la condition                   |

```bash
age=25
[[ $age -ge 18 && $age -le 65 ]]    # Vrai : entre 18 et 65

[[ $age -lt 10 || $age -gt 60 ]]     # Faux : ni < 10, ni > 60

[[ ! $age -lt 18 ]]                   # Vrai : 25 n'est PAS < 18
```


### Raccourcis avec `&&` et `||` entre commandes

```bash
# Si la commande réussit, ALORS fait ceci
mkdir mon_dossier && echo "Dossier créé !"

# Si la commande échoue, ALORS fait cela
cd /inexistant || echo "Le dossier n'existe pas"
```


## Très utile en pratique

### Les tests sur les fichiers

| Opérateur    | Signification             |
| ------------ | ------------------------- |
| `-e fichier` | Le fichier existe         |
| `-f fichier` | C'est un fichier normal   |
| `-d fichier` | C'est un dossier          |
| `-s fichier` | Le fichier n'est pas vide |
| `-r fichier` | Le fichier est lisible    |
| `-w fichier` | Le fichier est modifiable |
| `-x fichier` | Le fichier est exécutable |

```bash
[[ -f "/etc/passwd" ]]    # Vrai (le fichier existe)
[[ -d "/home" ]]          # Vrai (c'est un dossier)
```


### Incrémenter un compteur

```bash
compteur=0
((compteur++))       # → 1
((compteur++))       # → 2
((compteur += 5))    # → 7
```


## Bonus

### Le calcul décimal avec `bc`

Pour les nombres à virgule, utilise `bc` :

```bash
echo "scale=2; 10 / 3" | bc
# → 3.33

resultat=$(echo "scale=2; 10 / 3" | bc)
echo "Le résultat est $resultat"
```


### Comparer avec `(( ))` (syntaxe mathématique)

Dans les doubles parenthèses, tu peux utiliser les symboles habituels :

```bash
a=10
(( a > 5 ))     # Vrai
(( a == 10 ))   # Vrai
```


> **Note :** dans `(( ))`, pas besoin de `$` devant les variables.

## 🔧 Quand ça plante : lire un code de retour

Quand quelque chose ne marche pas, vérifie `$?` :

```bash
ma_commande
echo "Code de retour : $?"
# 0 = tout va bien, autre chose = problème
```


## ❌ Erreur classique

```bash
# Confondre = (affectation) et -eq (comparaison)
if [[ $age = 18 ]]; then     # ⚠️ Compare comme du TEXTE, pas un nombre
if [[ $age -eq 18 ]]; then   # ✅ Compare comme un NOMBRE

# Oublier $(( )) pour le calcul
resultat=5+3                  # ❌ resultat vaut le TEXTE "5+3"
resultat=$((5 + 3))           # ✅ resultat vaut le NOMBRE 8
```


## Exercices

**Guidé :** Crée un script `calculatrice.sh` qui prend deux nombres en arguments et affiche leur somme, différence et produit.

**Autonome :** Crée un script `est_pair.sh` qui prend un nombre en argument et dit s'il est pair ou impair (indice : un nombre est pair si `nombre % 2` vaut 0).

## ✅ Tu sais maintenant...

- Faire des calculs avec `$(( ))`
- Comparer des nombres (`-eq`, `-lt`, `-gt`...)
- Comparer des chaînes (`==`, `!=`, `-z`, `-n`)
- Combiner des conditions avec `&&`, `||`, `!`
- Tester des propriétés de fichiers (`-f`, `-d`, `-e`)

---
