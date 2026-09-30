---
title: Chapitre 9 — Comprendre les permissions
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 3 — Qui a le droit de quoi
  - index.md
---

## Le minimum à savoir

### L'idée : trois questions, trois réponses

Sous Linux, chaque fichier répond à trois questions :

1. **Qui possède ce fichier ?** → son **propriétaire** (*user*)
2. **Quel groupe y a accès ?** → son **groupe** (*group*)
3. **Et tous les autres ?** → les **autres** (*others*)

Pour chacune de ces trois catégories, le système définit ce qui est permis : **lire**, **écrire**, **exécuter**. C'est tout. Ce modèle simple (trois catégories × trois droits) gouverne l'accès à l'ensemble du système.

### Lire un `ls -l` : décrypter la première colonne

Tu as déjà vu `ls -l` au chapitre 2. Reprends-le maintenant avec un œil neuf :

```bash
ls -l rapport.txt
# -rw-r--r-- 1 alice equipe 1240 Jan 10 14:30 rapport.txt
```


Concentrons-nous sur le premier bloc, `-rw-r--r--`. Il se découpe ainsi :

```
  -        rw-       r--       r--
  │         │         │         │
type    propriétaire groupe   autres
```


- **1er caractère** : le **type**. `-` = fichier ordinaire, `d` = dossier (*directory*), `l` = lien symbolique.
- **Caractères 2 à 4** (`rw-`) : les droits du **propriétaire**.
- **Caractères 5 à 7** (`r--`) : les droits du **groupe**.
- **Caractères 8 à 10** (`r--`) : les droits des **autres**.

### Les trois droits : r, w, x

Chaque triplet se lit toujours dans le même ordre : `r`, `w`, `x`. Un tiret `-` signifie « ce droit est absent ».

| Lettre | Sur un fichier | Sur un dossier |
|--------|----------------|----------------|
| `r` (read) | lire le contenu | lister les fichiers qu'il contient |
| `w` (write) | modifier le contenu | créer/supprimer des fichiers dedans |
| `x` (execute) | exécuter le fichier (programme/script) | **entrer** dans le dossier (`cd`) |

> **Le piège des dossiers :** sur un **dossier**, `x` ne veut pas dire « exécuter » mais « traverser » (pouvoir faire `cd` dedans et accéder à son contenu). Un dossier sans `x` est inaccessible même si tu as `r`. Retiens : pour entrer dans un dossier, il faut le `x`.

Reprenons `-rw-r--r--` : c'est un fichier ordinaire, le propriétaire peut lire et écrire (`rw-`), le groupe peut seulement lire (`r--`), les autres aussi (`r--`). Personne ne peut l'exécuter. C'est typique d'un fichier de données.

## Très utile en pratique

### Modifier les permissions : `chmod` en notation symbolique

`chmod` (*change mode*) modifie les droits. La façon la plus lisible utilise des lettres :

- **Qui** : `u` (user/propriétaire), `g` (group), `o` (others), `a` (all/tous)
- **Action** : `+` (ajouter), `-` (retirer), `=` (fixer exactement)
- **Droit** : `r`, `w`, `x`

```bash
chmod u+x script.sh      # ajoute le droit d'exécution AU PROPRIÉTAIRE
chmod go-w fichier       # retire l'écriture au groupe ET aux autres
chmod a+r fichier        # donne la lecture à tout le monde
```


Le cas le plus fréquent de tout le cours : **rendre un script exécutable**.

```bash
chmod u+x mon-script.sh      # maintenant on peut le lancer avec ./mon-script.sh
```


> Ça boucle avec le chapitre 8 : un script fraîchement écrit n'est qu'un fichier texte. Pour que le système accepte de l'**exécuter**, il lui faut le droit `x`. Sans lui : « Permission denied ».

### La notation octale : les chiffres

Tu verras très souvent les permissions exprimées en **chiffres**, comme `chmod 755`. C'est la même chose, écrite autrement. Chaque droit vaut un nombre :

- `r` = **4**
- `w` = **2**
- `x` = **1**

On **additionne** pour chaque catégorie, ce qui donne un chiffre de 0 à 7 :

| Chiffre | Droits | Calcul |
|---------|--------|--------|
| 7 | `rwx` | 4+2+1 |
| 6 | `rw-` | 4+2 |
| 5 | `r-x` | 4+1 |
| 4 | `r--` | 4 |
| 0 | `---` | rien |

On écrit alors **trois** chiffres : propriétaire, groupe, autres.

```bash
chmod 755 script.sh      # rwx pour le proprio, r-x pour groupe et autres
chmod 644 fichier.txt    # rw- pour le proprio, r-- pour groupe et autres
chmod 600 secret.txt     # rw- pour le proprio, RIEN pour les autres
```


> **Les deux valeurs à mémoriser :** `644` pour un fichier de données normal (le propriétaire écrit, les autres lisent), `755` pour un programme ou un dossier (tout le monde peut exécuter/traverser, seul le propriétaire modifie). `600` pour un fichier privé (clé, secret) que toi seul peux lire. Ces trois valeurs couvrent l'immense majorité des cas.

### `umask` : les permissions par défaut

Quand tu crées un fichier, il reçoit des permissions par défaut. Celles-ci sont déterminées par le `umask`, un « filtre » qui **retire** des droits par défaut (typiquement, il enlève l'écriture aux autres) :

```bash
umask            # affiche le masque actuel (souvent 022)
```


Pour débuter, retiens simplement que `umask` **existe** et explique pourquoi tes nouveaux fichiers ne sont pas en écriture pour tout le monde. Tu n'as pas besoin de le modifier maintenant.

## ❌ Erreur classique

```bash
# Oublier de rendre un script exécutable
./mon-script.sh          # ❌ "Permission denied"
chmod u+x mon-script.sh  # ✅ puis ./mon-script.sh fonctionne

# Donner trop de droits "pour que ça marche"
chmod 777 fichier        # ❌ rwx pour TOUT LE MONDE : faille de sécurité béante
chmod 755 fichier        # ✅ juste ce qu'il faut

# Confondre l'ordre des chiffres
chmod 457 fichier        # rarement ce qu'on veut : réfléchis proprio/groupe/autres
chmod 644 fichier        # ✅ l'ordre est TOUJOURS proprio, groupe, autres

# Croire que r suffit pour entrer dans un dossier
chmod 600 dossier/       # ❌ sans x, impossible d'y faire cd
chmod 700 dossier/       # ✅ le x permet de traverser le dossier
```


> **Le réflexe `777` est un grand classique du débutant** : « ça ne marche pas, je mets tous les droits à tout le monde ». C'est exactement ce qu'un attaquant rêve de trouver. Donne **le minimum nécessaire**, jamais `777`.

## Exercices

**Guidé :** Crée un fichier `script.sh` contenant `echo "Bonjour"` (avec `echo "echo \"Bonjour\"" > script.sh`). Regarde ses permissions avec `ls -l`. Essaie de le lancer avec `./script.sh` — ça échoue. Rends-le exécutable avec `chmod u+x script.sh`, vérifie le changement avec `ls -l`, puis relance-le.

**Autonome :** Crée trois fichiers et donne-leur respectivement les permissions `644`, `600` et `755` en notation octale. Vérifie chacune avec `ls -l` et **traduis à voix haute** ce que chaque triplet signifie (qui peut faire quoi).

**Défi :** Pour un fichier donné, atteins exactement les permissions `rw-r-----` (le proprio lit/écrit, le groupe lit, les autres rien). Fais-le d'abord en notation symbolique (`chmod`), puis recommence sur un autre fichier en notation octale. Quel est le chiffre octal correspondant ? Vérifie avec `ls -l` que les deux méthodes donnent le même résultat.

## ✅ Tu sais maintenant…

- Le modèle **propriétaire / groupe / autres** (u/g/o) et les trois droits **r/w/x**
- **Lire** la ligne de permissions d'un `ls -l`, caractère par caractère
- Que `x` signifie « exécuter » sur un fichier mais « traverser » sur un dossier
- Modifier les droits avec `chmod` en **symbolique** (`u+x`, `go-w`…)
- La notation **octale** (r=4, w=2, x=1) et les valeurs clés `644`, `755`, `600`
- Pourquoi `chmod 777` est une mauvaise idée de sécurité
- Que `umask` détermine les permissions par défaut

---
