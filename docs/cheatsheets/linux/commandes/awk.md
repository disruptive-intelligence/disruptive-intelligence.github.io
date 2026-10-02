---
title: "awk"
commande: "awk"
---
# `awk`

Découpe chaque ligne en champs et permet de filtrer, réarranger ou calculer — là où `cut` ne fait que découper.

```bash title="Syntaxe"
awk -F'<séparateur>' '<condition> {<action>}' <fichier>   # séparateur par défaut : espaces et tabulations
```

Pour comprendre : [Administration Linux, ch. 4](../../../library/it/linux/administration-linux/01-partie-1-survivre-dans-le-terminal/04-chapitre-4-chercher-filtrer-et-transformer-du-text.md)
{ .kw-cs-meta }

## Les options utiles

| Élément | Ce qu'il représente |
|---|---|
| `-F':'` | Séparateur de champs (ici `:`) |
| `$1`, `$2`… · `$0` · `$NF` | Champ 1, 2… · la ligne entière · le dernier champ |
| `NR` · `NF` | Numéro de la ligne · nombre de champs de la ligne |
| `{print $1, $3}` | Affiche les champs 1 et 3, séparés par un espace |
| `$3 >= 1000` · `/motif/` · `$7 ~ /bash$/` | Condition : comparaison · ligne qui contient · champ qui correspond à une regex |
| `!~` · `&&` · `||` | Ne correspond pas · ET · OU |
| `BEGIN {…}` · `END {…}` | Avant la première ligne · après la dernière (totaux) |
| `-v seuil=1000` | Passe une variable du shell au programme |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `awk -F: '$3 >= 1000 {print $1, $6}' /etc/passwd` | Séparateur `:` ; lignes dont l'UID (champ 3) vaut au moins 1000 ; affiche le nom et le dossier personnel |
| `awk -F: '$7 !~ /(nologin|false)$/ {print $1}' /etc/passwd` | Les comptes dont le shell n'est ni `nologin` ni `false` : ceux qui peuvent se connecter |
| `awk '{print $1}' access.log` | La première colonne de chaque ligne : l'IP du client |
| `awk '{s += $10} END {print s}' access.log` | Additionne la 10e colonne (octets envoyés) et affiche le total à la fin |
| `awk 'NR==10, NR==20' fichier` | Les lignes 10 à 20 |

## Pièges

- Le programme se met entre **guillemets simples** : entre guillemets doubles, le shell remplace `$1` avant awk.
- Par défaut, plusieurs espaces de suite comptent pour un seul séparateur (`cut -d' '`, lui, compte chaque espace).
- `print $1, $2` sépare par un espace ; `print $1 $2` colle les deux champs.
