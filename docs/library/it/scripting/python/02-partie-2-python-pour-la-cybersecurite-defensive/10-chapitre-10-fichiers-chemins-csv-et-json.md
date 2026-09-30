---
title: Chapitre 10 — Fichiers, chemins, CSV et JSON
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

> **Prépare tes fichiers de test avant de commencer ce chapitre.** À partir d'ici, tes scripts vont lire de vrais fichiers. Pour t'entraîner, crée-les toi-même (jamais sur des systèmes que tu n'es pas autorisé à analyser). Organise un dossier de travail comme ceci :
>
> ```
> scripts_cyber/
> ├── auth.log
> ├── access.log
> ├── iocs.csv
> ├── rapport.txt
> ├── scripts/      ← tes scripts .py
> └── sorties/      ← les rapports qu'ils produisent
> ```
>
> Crée par exemple un `auth.log` minimal avec quelques lignes factices (tu peux copier-coller ces lignes dans ton éditeur) :
>
> ```
> Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5 port 51234 ssh2
> Jan 10 03:22:14 srv sshd[2452]: Failed password for admin from 203.0.113.5 port 51240 ssh2
> Jan 10 03:25:02 srv sshd[2460]: Accepted password for alice from 10.0.0.4 port 51250 ssh2
> Jan 10 03:26:40 srv sshd[2471]: Failed password for root from 198.51.100.9 port 44102 ssh2
> ```
>
> Et un `iocs.csv` minimal :
>
> ```
> valeur,type,confiance
> 203.0.113.5,ip,90
> evil.example.com,domaine,70
> 5d41402abc4b2a76b9719d911017c592,hash,80
> ```
>
> Avec ces deux fichiers, tu pourras exécuter pour de vrai la quasi-totalité des exemples et exercices des chapitres 10 à 20.

## Le minimum à savoir

### Lire un fichier de log

```python
with open("auth.log", "r", encoding="utf-8") as f:
    contenu = f.read()

print(contenu)
```


> **Bonne pratique :** ajoute toujours `encoding="utf-8"` à l'ouverture d'un fichier texte. Sans ça, l'encodage varie selon l'OS et tu risques des erreurs sur les accents ou certains caractères. On ne le répétera pas à chaque exemple, mais prends le réflexe.

Le mot-clé `with` garantit que le fichier est **fermé proprement** à la fin, même en cas d'erreur. `open("fichier", "r")` ouvre en lecture (`"r"` = read), `as f` nomme le fichier ouvert `f`.

### Les modes d'ouverture

|Mode |Signification                  |Équivalent Bash|
|-----|-------------------------------|---------------|
|`"r"`|Lecture (par défaut)           |`cat fichier`  |
|`"w"`|Écriture (écrase le fichier !) |`>`            |
|`"a"`|Ajout (à la fin)               |`>>`           |

> **Attention :** `"w"` **écrase** tout le contenu. Pour un fichier de journal (rapport, log d'analyse), utilise `"a"` pour **ajouter** sans tout perdre.

### Lire ligne par ligne (le mode roi en analyse de logs)

```python
with open("auth.log", "r", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()       # enlève le \n de fin de ligne
        if "Failed password" in ligne:
            print(f"[!] {ligne}")
```


> **Bonne pratique :** `.strip()` à chaque ligne pour retirer le `\n` final, sinon tes comparaisons échouent.

Lire ligne par ligne fonctionne même sur des fichiers énormes (plusieurs Go) sans saturer la mémoire — essentiel pour les vrais logs.

### Écrire un rapport

```python
with open("rapport.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport d'analyse ===\n")
    f.write("IP suspecte : 203.0.113.5\n")
    f.write("Verdict : force brute\n")
```


> **Note :** `f.write()` n'ajoute **pas** de `\n` automatiquement, contrairement à `print()`. Mets-le toi-même.

### Vérifier qu'un fichier existe

```python
import os

if os.path.isfile("auth.log"):
    print("[+] Fichier trouvé")
else:
    print("[-] Fichier introuvable")
```


> **Comparaison avec Bash :** `os.path.isfile()` ≈ `[[ -f ... ]]`, `os.path.isdir()` ≈ `[[ -d ... ]]`, `os.path.exists()` ≈ `[[ -e ... ]]`.

-----

## Les chemins avec `pathlib` (la méthode moderne)

`pathlib` est la manière moderne et lisible de manipuler les chemins (recommandée depuis Python 3.4).

```python
from pathlib import Path

chemin = Path("logs/auth.log")

print(chemin.exists())     # True / False
print(chemin.name)         # "auth.log"
print(chemin.suffix)       # ".log" (l'extension)
print(chemin.parent)       # "logs"
```


### Parcourir un dossier de logs

```python
from pathlib import Path

dossier = Path("/var/log")

# Tous les fichiers .log
for fichier in dossier.glob("*.log"):
    print(f"[+] Log trouvé : {fichier.name}")

# Recherche récursive (sous-dossiers inclus)
for fichier in dossier.rglob("*.log"):
    print(fichier)
```


C'est exactement ce qu'on fait pour analyser tous les logs d'une arborescence d'un coup.

## Très utile en pratique

### Travailler avec des fichiers CSV (exports SIEM)

Les exports SIEM, listes d'IOC et inventaires sont souvent en CSV. Python a un module intégré :

```python
import csv

# Lire un CSV avec en-têtes → chaque ligne devient un dictionnaire
with open("iocs.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(f"{ligne['type']} : {ligne['valeur']} (confiance {ligne['confiance']})")

# Écrire un CSV (rapport d'IOC)
with open("rapport.csv", "w", newline="", encoding="utf-8") as f:
    ecrivain = csv.writer(f)
    ecrivain.writerow(["ip", "echecs", "verdict"])      # en-tête
    ecrivain.writerow(["203.0.113.5", "47", "bloquer"])
    ecrivain.writerow(["10.0.0.4", "1", "ok"])
```


Avec `DictReader`, chaque ligne est un dictionnaire dont les clés sont les en-têtes — on retrouve exactement le pattern du chapitre 9.

### Travailler avec du JSON (APIs CTI, configs)

JSON est le format standard des APIs de menaces et des configurations :

```python
import json

# Lire du JSON
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
print(config["seuils"]["score_alerte"])

# Écrire du JSON
rapport = {
    "ip": "203.0.113.5",
    "echecs": 47,
    "verdict": "bloquer"
}
with open("rapport.json", "w", encoding="utf-8") as f:
    json.dump(rapport, f, indent=4)    # indent=4 = joli formatage
```


> **Lien clé :** `json.load()` transforme un fichier JSON en **dictionnaire/liste Python**, et `json.dump()` fait l'inverse. C'est le pont entre tes scripts et les APIs CTI/SIEM (chapitre 17).

### Date et heure avec `datetime`

```python
from datetime import datetime

maintenant = datetime.now()
horodatage = maintenant.strftime("%Y-%m-%d %H:%M:%S")
print(horodatage)        # 2025-01-10 14:30:00

# Nom de fichier de rapport daté
nom = f"rapport_{maintenant.strftime('%Y%m%d')}.txt"
print(nom)               # rapport_20250110.txt
```


Horodater ses rapports et entrées de journal est indispensable en forensic et en SOC.

## Application cyber — un parser de logs qui écrit un rapport

Combinons lecture de log, comptage, et écriture d'un rapport horodaté. C'est un outil défensif complet, simple mais réel.

```python
import sys
from datetime import datetime
from pathlib import Path

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <fichier_log>")
    sys.exit(1)

fichier = Path(sys.argv[1])
if not fichier.is_file():
    print(f"[-] Fichier introuvable : {fichier}")
    sys.exit(1)

# 1. Lire et compter les échecs par IP
echecs_par_ip = {}
with open(fichier, "r", encoding="utf-8") as f:
    for ligne in f:
        if "Failed password" in ligne:
            ip = ligne.split()[-1]
            echecs_par_ip[ip] = echecs_par_ip.get(ip, 0) + 1

# 2. Écrire un rapport horodaté
horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("rapport_echecs.txt", "w", encoding="utf-8") as r:
    r.write(f"=== Rapport d'analyse ({horodatage}) ===\n")
    r.write(f"Fichier analysé : {fichier}\n\n")
    for ip, nb in echecs_par_ip.items():
        marque = "[BLOQUER]" if nb >= 5 else "[INFO]"
        r.write(f"{marque} {ip} : {nb} échec(s)\n")

print(f"[+] Rapport écrit dans rapport_echecs.txt ({len(echecs_par_ip)} IP)")
```


Lancement : `python3 parser.py auth.log`. Le script lit le log ligne par ligne, compte les échecs par IP, et produit un rapport texte daté marquant les IP à bloquer. Tu as réuni : arguments, vérification de fichier, lecture ligne par ligne, dictionnaire, et écriture de rapport.

## Bonus

### Exécuter une commande système (le pont avec Bash)

Si tu dois vraiment appeler un outil système (rare en pratique) :

```python
import subprocess

resultat = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(resultat.stdout)
```


Préfère les outils Python natifs (`pathlib`, `os`) quand c'est possible.

## ❌ Erreur classique

```python
# Ouvrir en lecture puis vouloir écrire
with open("rapport.txt", "r") as f:
    f.write("texte")          # ❌ io.UnsupportedOperation (mode "r")
with open("rapport.txt", "w") as f:
    f.write("texte")          # ✅

# Confondre "w" et "a" — "w" EFFACE le contenu existant
with open("journal.log", "w") as f:   # ❌ écrase tout le journal !
    f.write("nouvelle entrée\n")
with open("journal.log", "a") as f:   # ✅ ajoute à la fin
    f.write("nouvelle entrée\n")

# Oublier .strip() en lisant ligne par ligne
for ligne in f:
    if ligne == "STOP":        # ❌ ne matche jamais (ligne = "STOP\n")
        break
    if ligne.strip() == "STOP": # ✅
        break

# Ouvrir un fichier inexistant en lecture
with open("absent.log", "r") as f:    # ❌ FileNotFoundError
    f.read()
```


## Exercices

**Guidé :** Crée un script `compter_lignes.py` qui prend un fichier en argument, vérifie qu'il existe, et affiche le nombre total de lignes et le nombre de lignes contenant `"Failed"`.

**Autonome :** Crée un script `csv_vers_json.py` qui lit un fichier CSV d'IOC (colonnes `valeur`, `type`) avec `DictReader`, met chaque ligne dans une liste de dictionnaires, et écrit le tout dans un fichier `iocs.json` avec `json.dump(..., indent=4)`.

## 🧩 Mini-projet (chapitres 8-10)

Crée un script `journal_soc.py` qui :

1. Prend un message d'alerte en argument (ou le demande avec `input()` si absent).
2. Ajoute la date et le message dans un fichier `soc.log` au format `[2025-01-10 14:30] Message`.
3. Avec l'argument `--lire`, affiche tout le contenu du journal.
4. Utilise des **fonctions** : une pour ajouter une entrée, une pour lire le journal.

## ✅ Tu sais maintenant…

- Ouvrir, lire et écrire des fichiers avec `open()` et `with`
- La différence entre les modes `"r"`, `"w"` (écrase) et `"a"` (ajoute)
- Lire un log ligne par ligne (même très gros) et nettoyer avec `.strip()`
- Manipuler les chemins avec `pathlib` (`glob`, `rglob`, `.suffix`…)
- Lire/écrire du CSV (`DictReader`, `writer`) et du JSON (`json.load`, `json.dump`)
- Horodater un rapport avec `datetime`
- Construire un parser de logs qui produit un rapport

-----
