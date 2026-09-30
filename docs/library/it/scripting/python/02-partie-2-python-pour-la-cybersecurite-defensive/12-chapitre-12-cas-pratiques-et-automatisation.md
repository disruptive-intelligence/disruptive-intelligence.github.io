---
title: Chapitre 12 — Cas pratiques et automatisation
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

> Jusqu'ici, tu as appris les briques une par une. Maintenant on les **combine** dans de vrais petits outils défensifs.

## Penser comme un analyste qui automatise

Avant d'écrire un outil, pose-toi trois questions :

1. **Qu'est-ce que je fais à la main régulièrement ?** (chercher des IP dans des logs, calculer des hash…)
2. **Est-ce toujours les mêmes étapes ?**
3. **Est-ce que ça pourrait tourner tout seul ?** (planifié, ou lancé sur un dossier entier)

Trois « oui » → bon candidat pour un script.

## Cas pratique 1 — Extraire les IP uniques d'un log

```python
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <log>")
    sys.exit(1)

ips = set()    # un set : pas de doublons
with open(sys.argv[1], "r", encoding="utf-8") as f:
    for ligne in f:
        if "from " in ligne:
            ip = ligne.strip().split()[-1]
            ips.add(ip)

print(f"[+] {len(ips)} IP unique(s) :")
for ip in sorted(ips):
    print(f"    {ip}")
```


> **Illustre :** `set` pour dédoublonner, lecture ligne par ligne, `split`.

## Cas pratique 2 — Vérifier des chemins et repérer les fichiers sensibles

```python
import sys
from pathlib import Path

extensions_sensibles = (".exe", ".scr", ".bat", ".ps1")

for chemin_str in sys.argv[1:]:
    chemin = Path(chemin_str)
    if not chemin.exists():
        print(f"[-] {chemin} — introuvable")
    elif chemin.is_file():
        marque = "[!]" if chemin.suffix.lower() in extensions_sensibles else "[+]"
        taille = chemin.stat().st_size
        print(f"{marque} {chemin.name} — {taille} octets")
    elif chemin.is_dir():
        nb = len(list(chemin.iterdir()))
        print(f"[+] {chemin.name}/ — dossier ({nb} éléments)")
```


> **Illustre :** `pathlib`, `.suffix`, `.stat().st_size`, tuple d'extensions.

## Cas pratique 3 — Analyser un CSV d'événements

```python
import csv
import sys

if len(sys.argv) < 2:
    print(f"[-] Usage : python3 {sys.argv[0]} <evenements.csv>")
    sys.exit(1)

total = 0
echecs = 0
par_ip = {}

try:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            total += 1
            if ligne.get("action") == "echec":
                echecs += 1
                ip = ligne.get("ip", "inconnue")
                par_ip[ip] = par_ip.get(ip, 0) + 1
    print(f"[*] {total} événements, {echecs} échec(s)")
    for ip, nb in par_ip.items():
        if nb >= 3:
            print(f"  [!] {ip} : {nb} échecs")
except FileNotFoundError:
    print(f"[-] Fichier '{sys.argv[1]}' introuvable")
```


> **Illustre :** `csv.DictReader`, `.get()`, comptage, `try/except`.

## Les modules essentiels pour l'automatisation défensive

Tous inclus avec Python — rien à installer (sauf `requests`, chapitre 16).

|Module      |Utilité                          |Vu au chapitre|
|------------|---------------------------------|--------------|
|`sys`       |Arguments, quitter               |3             |
|`pathlib`   |Chemins, parcours de dossiers    |10            |
|`datetime`  |Horodatage des rapports          |10            |
|`json`      |APIs CTI, configs                |10, 17        |
|`csv`       |Exports SIEM, listes d'IOC       |10            |
|`re`        |Extraction d'IOC (regex)         |13            |
|`hashlib`   |Calcul de hash                   |18            |
|`ipaddress` |Manipulation d'IP/réseaux        |19            |
|`requests`  |Requêtes HTTP/API (à installer)  |16            |

## Script modèle réutilisable

Un squelette propre pour tes outils défensifs :

```python
#!/usr/bin/env python3
"""
Nom         : mon_outil.py
Description : [Ce que fait l'outil]
Usage       : python3 mon_outil.py <argument>
"""

import sys
from datetime import datetime


def log(message):
    """Affiche un message horodaté."""
    h = datetime.now().strftime("%H:%M:%S")
    print(f"[{h}] {message}")


def traiter(cible):
    """Traitement principal."""
    log(f"Analyse de {cible}")
    # ... ton code ...
    log("Terminé.")


def main():
    if len(sys.argv) < 2:
        print(f"Usage : python3 {sys.argv[0]} <cible>")
        sys.exit(1)
    traiter(sys.argv[1])


if __name__ == "__main__":
    main()
```


## Application cyber — assembler une mini-chaîne d'analyse

On combine plusieurs fonctions des chapitres précédents en un seul outil cohérent.

```python
import sys

def is_private_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.")

def analyser_log(chemin):
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            if "Failed password" not in ligne:
                continue
            ip = ligne.strip().split()[-1]
            echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <log>")
        sys.exit(1)
    echecs = analyser_log(sys.argv[1])
    print("=== Résumé d'analyse ===")
    for ip, nb in sorted(echecs.items(), key=lambda x: x[1], reverse=True):
        origine = "interne" if is_private_ip(ip) else "EXTERNE"
        verdict = "[!] bloquer" if nb >= 5 and not is_private_ip(ip) else "ok"
        print(f"{ip} ({origine}) : {nb} échecs → {verdict}")

if __name__ == "__main__":
    main()
```


Ici, `sorted(..., key=lambda x: x[1], reverse=True)` trie les IP de la plus active à la moins active (ne t'inquiète pas du `lambda`, c'est juste « trie selon le nombre d'échecs »). On combine fonction de classification, parcours de log, comptage et décision — la structure type d'un outil SOC.

## ❌ Erreur classique

```python
# Réécrire 5 fois le même bloc au lieu d'en faire une fonction
# → factorise dans une fonction réutilisable

# Tout mettre dans un seul gros bloc sans main()
# → structure avec des fonctions + if __name__ == "__main__"

# Oublier de gérer le fichier absent dans un outil "réel"
# → toujours un try/except autour de l'ouverture
```


## Exercices

**Guidé :** Crée un outil qui prend un dossier en argument et liste tous les fichiers `.log` qu'il contient (avec `pathlib.glob`), en affichant la taille de chacun.

**Autonome :** Crée un outil « boîte à outils » avec un menu (`while True` + `input()`) : 1) compter les échecs dans un log, 2) lister les IP uniques, 3) afficher la date/heure, 4) quitter. Chaque option appelle une **fonction** dédiée.

**Défi :** Crée un outil qui lit un CSV d'IOC, les filtre par confiance (≥ un seuil donné en argument) et exporte les IOC retenus dans un fichier JSON.

## ✅ Tu sais maintenant…

- Combiner toutes les briques dans de vrais outils défensifs
- Utiliser les modules essentiels (`sys`, `pathlib`, `datetime`, `json`, `csv`)
- Structurer un outil proprement avec le modèle réutilisable et `main()`
- Automatiser des tâches réelles : extraire des IP, analyser un CSV, produire un rapport

-----
