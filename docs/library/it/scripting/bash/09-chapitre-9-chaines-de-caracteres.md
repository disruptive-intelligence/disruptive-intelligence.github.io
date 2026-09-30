---
title: Chapitre 9 — Chaînes de caractères
source: IT/05_Scripting_Langage-Prog/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

## Le minimum à savoir

### Longueur d'une chaîne

```bash
mot="Bonjour"
echo ${#mot}       # → 7
```


### Concaténation (coller des chaînes)

```bash
debut="Bon"
fin="jour"
mot=$debut$fin
echo "$mot"        # → Bonjour
```


### Extraire une sous-chaîne

```bash
phrase="Bash est génial"

echo "${phrase:0:4}"     # → Bash     (4 caractères depuis la position 0)
echo "${phrase:5:3}"     # → est      (3 caractères depuis la position 5)
echo "${phrase:9}"       # → génial   (tout depuis la position 9)
```


> **Rappel :** les positions commencent à 0.

### Remplacer dans une chaîne

```bash
phrase="J'adore les pommes"

# Remplacer la première occurrence
echo "${phrase/pommes/bananes}"
# → J'adore les bananes

# Remplacer TOUTES les occurrences (double slash)
tel="01-23-45-67-89"
echo "${tel//-/.}"
# → 01.23.45.67.89
```


### Supprimer dans une chaîne

Supprimer, c'est remplacer par rien :

```bash
tel="01-23-45-67-89"

# Supprimer tous les tirets
echo "${tel//-/}"
# → 0123456789
```


### Majuscules et minuscules

```bash
nom="alice dupont"
NOM="ALICE DUPONT"

echo "${nom^^}"          # → ALICE DUPONT  (tout en majuscules)
echo "${NOM,,}"          # → alice dupont  (tout en minuscules)
echo "${nom^}"           # → Alice dupont  (première lettre en majuscule)
```


## Très utile en pratique

### Tester si une chaîne est vide

```bash
nom=""
[[ -z "$nom" ]] && echo "Nom est vide"       # → Nom est vide

autre="Alice"
[[ -n "$autre" ]] && echo "Autre n'est pas vide"  # → Autre n'est pas vide
```


### Récapitulatif

| Syntaxe                  | Effet                            |
| ------------------------ | -------------------------------- |
| `${#var}`                | Longueur                         |
| `${var:pos:len}`         | Extraire une sous-chaîne         |
| `${var/ancien/nouveau}`  | Remplacer la 1ère occurrence     |
| `${var//ancien/nouveau}` | Remplacer toutes les occurrences |
| `${var//ancien/}`        | Supprimer toutes les occurrences |
| `${var^^}`               | Tout en majuscules               |
| `${var,,}`               | Tout en minuscules               |
| `${var^}`                | 1ère lettre en majuscule         |

## Bonus

### Extraire l'extension d'un fichier

```bash
fichier="rapport.tar.gz"
echo "${fichier##*.}"    # → gz (tout après le dernier .)
echo "${fichier%.*}"     # → rapport.tar (tout avant le dernier .)
```


### Pattern matching avancé

```bash
# Supprimer un préfixe
chemin="/home/user/documents/fichier.txt"
echo "${chemin##*/}"     # → fichier.txt (garde juste le nom)

# Supprimer un suffixe
echo "${chemin%/*}"      # → /home/user/documents (garde juste le dossier)
```


## ❌ Erreur classique

```bash
# Oublier les accolades
echo "$phrase:0:4"       # ❌ Affiche le contenu de $phrase suivi de ":0:4"
echo "${phrase:0:4}"     # ✅ Extrait correctement

# Confondre / et //
echo "${tel/-/}"         # Supprime seulement le PREMIER tiret
echo "${tel//-/}"        # Supprime TOUS les tirets
```


## Exercices

**Guidé :** Crée un script qui prend un numéro de téléphone avec des tirets (`01-23-45-67-89`) et l'affiche reformaté avec des points (`01.23.45.67.89`).

**Autonome :** Crée un script qui prend une phrase en argument et affiche sa longueur, la phrase en majuscules, et la phrase en minuscules.

## ✅ Tu sais maintenant...

- Mesurer la longueur d'une chaîne
- Extraire, remplacer et supprimer des parties de chaîne
- Convertir entre majuscules et minuscules
- Les syntaxes `${var/...}` et `${var^^}`/`${var,,}`

---
