---
title: Chapitre 13 — Regex avec re
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

extraire IP, emails, domaines, URLs et hash

## Le minimum à savoir

### C'est quoi une regex ?

Une **expression régulière** (regex) est un motif qui décrit une forme de texte. Au lieu de chercher un mot exact, tu décris *à quoi ressemble* ce que tu cherches : « quatre groupes de chiffres séparés par des points » (une IP), « du texte, un @, un domaine » (un email).

C'est l'outil n°1 pour **extraire des IOC** d'un texte brut (un log, un email, un rapport).

```python
import re

texte = "Connexion depuis 203.0.113.5 puis 198.51.100.9 détectée"
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", texte)
print(ips)    # ['203.0.113.5', '198.51.100.9']
```


`re.findall(motif, texte)` retourne **une liste** de toutes les correspondances. C'est la fonction que tu utiliseras le plus.

> **Extraction ≠ validation :** cette regex repère une *forme* qui ressemble à une IPv4, mais elle ne vérifie pas que chaque octet est bien compris entre 0 et 255. Elle matcherait aussi `999.999.999.999`, qui n'est pas une vraie IP. C'est parfait pour **extraire** des candidats d'un texte, mais pour **valider** réellement qu'une IP est correcte, on utilisera le module `ipaddress` au chapitre 19. Retiens cette distinction : on extrait largement, puis on valide proprement.

### Les briques de base d'un motif

|Symbole |Signifie                          |Exemple        |
|--------|----------------------------------|---------------|
|`\d`    |un chiffre (0-9)                  |`\d` → `7`     |
|`\w`    |une lettre, chiffre ou `_`        |`\w` → `a`, `3`|
|`.`     |n'importe quel caractère          |               |
|`\.`    |un vrai point (échappé)           |dans une IP    |
|`+`     |1 fois ou plus                    |`\d+` → `2025` |
|`*`     |0 fois ou plus                    |               |
|`{n}`   |exactement n fois                 |`\d{4}`        |
|`{a,b}` |entre a et b fois                 |`\d{1,3}`      |
|`[...]` |un caractère parmi l'ensemble     |`[a-f0-9]`     |

> **Le `r"..."` (raw string) :** on préfixe toujours les motifs regex par `r` pour que Python n'interprète pas les `\`. `r"\d"` est correct ; `"\d"` peut poser problème.

### Extraire les indicateurs les plus courants

```python
import re

texte = """
Source 203.0.113.5 a contacté evil.example.com
URL piégée : https://bad.example.net/payload
Contact : attaquant@example.com
Hash du fichier : 5d41402abc4b2a76b9719d911017c592
"""

# IP v4
ips = re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", texte)
print("IP   :", ips)

# Emails
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte)
print("Mails:", emails)

# URLs http/https
urls = re.findall(r"https?://[^\s]+", texte)
print("URLs :", urls)

# Hash hexadécimaux (MD5=32, SHA-1=40, SHA-256=64)
hashes = re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte)
print("Hash :", hashes)
```


Résultat :

```
IP   : ['203.0.113.5']
Mails: ['attaquant@example.com']
URLs : ['https://bad.example.net/payload']
Hash : ['5d41402abc4b2a76b9719d911017c592']
```


> Ne cherche pas à mémoriser ces motifs par cœur dès maintenant. Comprends leur logique (« des chiffres et des points pour une IP ») et garde-les sous la main comme une boîte à outils.

> **Pourquoi `(?:...{32}|...{40}|...{64})` pour les hash ?** On cible exactement les trois longueurs réelles : MD5 = 32, SHA-1 = 40, SHA-256 = 64 caractères hexadécimaux. Un motif plus simple comme `{32,64}` matcherait aussi des longueurs intermédiaires (33, 50…) qui ne correspondent à aucun hash standard. Le `(?:...)` est un groupe « non capturant » : il sert juste à regrouper les trois possibilités séparées par `|` (OU), sans créer de groupe de capture.

### `re.search()` : juste tester / trouver le premier

```python
import re

ligne = "Failed password for root from 203.0.113.5"

resultat = re.search(r"\d{1,3}(?:\.\d{1,3}){3}", ligne)
if resultat:
    print("IP trouvée :", resultat.group())   # 203.0.113.5
else:
    print("Aucune IP")
```


`re.search` renvoie le **premier** résultat (ou `None`). `.group()` donne le texte trouvé.

## Très utile en pratique

### Les groupes de capture : extraire des morceaux précis

Les parenthèses `(...)` capturent une partie du motif :

```python
import re

ligne = "10/Jan/2025:14:30:55 GET /admin 403"
m = re.search(r"(GET|POST) (\S+) (\d{3})", ligne)
if m:
    methode = m.group(1)    # "GET"
    chemin = m.group(2)     # "/admin"
    code = m.group(3)       # "403"
    print(f"{methode} {chemin} → {code}")
```


`\S` = un caractère qui n'est pas un espace ; `\S+` = un mot. Les groupes te permettent de découper une ligne de log en champs nommés.

### Compiler un motif réutilisé

Si tu utilises le même motif des milliers de fois (gros log), compile-le une fois :

```python
import re

motif_ip = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}")

for ligne in lignes:
    for ip in motif_ip.findall(ligne):
        print(ip)
```


## Application cyber — un extracteur d'IOC

Voici un petit extracteur qui sort tous les IOC d'un texte et les range par type. C'est la base d'un outil de triage d'emails de phishing ou de rapports.

```python
import re

def extraire_iocs(texte):
    """Extrait IP, domaines, URLs, emails et hash d'un texte."""
    return {
        "ips": re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte),
        "urls": re.findall(r"https?://[^\s]+", texte),
        "emails": re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte),
        "hashes": re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte),
    }

texte = """De: attaquant@example.com
Cliquez sur https://bad.example.net/login
Serveur de commande : 203.0.113.5
Empreinte : 5d41402abc4b2a76b9719d911017c592
"""

iocs = extraire_iocs(texte)
for type_ioc, valeurs in iocs.items():
    if valeurs:
        print(f"[+] {type_ioc} ({len(valeurs)}) : {valeurs}")
```


Résultat :

```
[+] ips (1) : ['203.0.113.5']
[+] urls (1) : ['https://bad.example.net/login']
[+] emails (1) : ['attaquant@example.com']
[+] hashes (1) : ['5d41402abc4b2a76b9719d911017c592']
```


En quelques lignes, tu transformes un email brut en liste structurée d'indicateurs prêts à être vérifiés.

## Bonus

### `re.sub()` : remplacer / anonymiser

Utile pour **caviarder** des données sensibles dans un rapport (RGPD, partage externe) :

```python
import re

texte = "Utilisateur 203.0.113.5 a échoué 47 fois"
anonyme = re.sub(r"\d{1,3}(?:\.\d{1,3}){3}", "[IP_MASQUÉE]", texte)
print(anonyme)    # Utilisateur [IP_MASQUÉE] a échoué 47 fois
```


## ❌ Erreur classique

```python
import re

# Oublier le r devant le motif
re.findall("\d+", "abc 123")     # ⚠️ peut générer un avertissement
re.findall(r"\d+", "abc 123")    # ✅ correct

# Oublier d'échapper le point (. = n'importe quel caractère !)
re.findall(r"\d+.\d+", "1x2")    # matche "1x2" car . = n'importe quoi
re.findall(r"\d+\.\d+", "1.2")   # ✅ \. = un vrai point

# Croire que findall plante s'il ne trouve rien
re.findall(r"\d+", "aucun chiffre")   # → [] (liste vide, pas d'erreur)

# Oublier de tester si search a trouvé quelque chose
m = re.search(r"\d+", "rien")
print(m.group())    # ❌ AttributeError si m est None
if m:               # ✅ toujours tester
    print(m.group())
```


## Exercices

**Guidé :** Crée un script `extraire_ip.py` qui prend un fichier de log en argument, extrait toutes les IP avec `re.findall`, les dédoublonne (`set`) et les affiche triées.

**Autonome :** Crée un script `extraire_iocs.py` qui lit un fichier texte (un email sauvegardé, par exemple), utilise la fonction `extraire_iocs` ci-dessus, et écrit le résultat dans un fichier JSON.

## ✅ Tu sais maintenant…

- Ce qu'est une regex et pourquoi c'est central pour extraire des IOC
- Les briques de base (`\d`, `\w`, `+`, `{n}`, `[...]`, `\.`) et le `r"..."`
- `re.findall` (toutes les correspondances) et `re.search` (la première)
- Les groupes de capture `(...)` pour découper une ligne en champs
- `re.sub` pour anonymiser des données sensibles

-----
