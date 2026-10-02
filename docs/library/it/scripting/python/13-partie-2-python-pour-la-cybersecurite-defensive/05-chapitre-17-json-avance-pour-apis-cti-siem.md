---
title: Chapitre 17 — JSON avancé pour APIs CTI/SIEM
source: IT/07 Scripting & programmation/Langages/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Rappel : JSON ⟷ Python

JSON est le langage commun des APIs de menaces et des SIEM. Python le traduit directement :

|JSON         |Python      |
|-------------|------------|
|objet `{}`   |dictionnaire|
|tableau `[]` |liste       |
|`"texte"`    |`str`       |
|`42`         |`int`       |
|`true`/`false`|`True`/`False`|
|`null`       |`None`      |

Deux paires de fonctions à connaître :

```python
import json

# Depuis/vers une CHAÎNE de texte (ex. réponse d'API)
donnees = json.loads('{"ip": "203.0.113.5", "score": 80}')   # texte → dict
texte = json.dumps(donnees)                                   # dict → texte

# Depuis/vers un FICHIER
with open("ioc.json") as f:
    donnees = json.load(f)        # fichier → dict
with open("sortie.json", "w") as f:
    json.dump(donnees, f, indent=4)   # dict → fichier
```


> **Moyen mnémotechnique :** `loads`/`dumps` (avec **s** comme *string*) travaillent sur du texte ; `load`/`dump` (sans s) travaillent sur des **fichiers**.

### Explorer une réponse d'API imbriquée

Les réponses CTI sont souvent imbriquées (dictionnaires dans des dictionnaires dans des listes). On y accède pas à pas :

```python
import json

reponse = json.loads("""
{
  "data": {
    "ip": "203.0.113.5",
    "reputation": {"score": 85, "verdict": "malicious"},
    "tags": ["c2", "scanner"]
  }
}
""")

print(reponse["data"]["ip"])                       # 203.0.113.5
print(reponse["data"]["reputation"]["score"])      # 85
print(reponse["data"]["tags"][0])                  # c2
```


Chaque `[...]` descend d'un niveau. C'est de la navigation dans des dictionnaires et listes — rien de nouveau, juste imbriqué.

### Accès sûr avec `.get()` (champs parfois absents)

Les réponses d'API varient. Ne suppose jamais qu'un champ existe :

```python
reputation = reponse["data"].get("reputation", {})
score = reputation.get("score", 0)        # 0 si absent
print(f"Score : {score}")
```


Enchaîner des `.get(..., {})` évite les `KeyError` quand un niveau manque.

## Très utile en pratique

### Parcourir une liste de résultats

```python
import json

reponse = json.loads("""
{"results": [
  {"ioc": "203.0.113.5", "type": "ip", "score": 90},
  {"ioc": "evil.example.com", "type": "domain", "score": 70},
  {"ioc": "8.8.8.8", "type": "ip", "score": 0}
]}
""")

for item in reponse["results"]:
    if item["score"] >= 80:
        print(f"[!] {item['ioc']} ({item['type']}) — score {item['score']}")
```


```
[!] 203.0.113.5 (ip) — score 90
```


### Construire un événement au format SIEM et l'exporter

```python
import json
from datetime import datetime

evenement = {
    "timestamp": datetime.now().isoformat(),
    "source": "parser_ssh",
    "alert": {
        "type": "ssh_bruteforce",
        "src_ip": "203.0.113.5",
        "count": 47,
        "severity": "high"
    },
    "iocs": ["203.0.113.5"]
}

with open("alerte_siem.json", "w", encoding="utf-8") as f:
    json.dump(evenement, f, indent=4, ensure_ascii=False)

print("[+] Alerte exportée au format JSON")
```


> **Astuce :** `ensure_ascii=False` garde les accents lisibles dans le fichier (`é` au lieu de `\u00e9`). `datetime.now().isoformat()` produit un horodatage standard exploitable par les SIEM.

### Transformer un CSV d'IOC en JSON (cas très courant)

```python
import csv
import json

iocs = []
with open("iocs.csv", "r", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        iocs.append({
            "value": ligne["valeur"],
            "type": ligne["type"],
            "confidence": int(ligne.get("confiance", 0))
        })

with open("iocs.json", "w", encoding="utf-8") as f:
    json.dump(iocs, f, indent=4, ensure_ascii=False)

print(f"[+] {len(iocs)} IOC convertis en JSON")
```


## Application cyber — analyser une réponse CTI et produire un verdict

On reçoit une réponse JSON (comme une vraie API de réputation) et on la résume en un verdict clair.

```python
import json

# Réponse simulée d'une API CTI
brut = """
{
  "ioc": "203.0.113.5",
  "type": "ip",
  "engines": {"total": 80, "malicious": 12, "suspicious": 5},
  "tags": ["scanner", "bruteforce"],
  "last_seen": "2025-01-09"
}
"""

def verdict_cti(reponse_json):
    data = json.loads(reponse_json)
    engines = data.get("engines", {})
    malicious = engines.get("malicious", 0)
    total = engines.get("total", 1)

    ratio = malicious / total
    if ratio >= 0.10:
        niveau = "MALVEILLANT"
    elif malicious > 0:
        niveau = "SUSPECT"
    else:
        niveau = "PROPRE"

    return {
        "ioc": data.get("ioc"),
        "type": data.get("type"),
        "niveau": niveau,
        "detections": f"{malicious}/{total}",
        "tags": data.get("tags", [])
    }

resultat = verdict_cti(brut)
print(f"[{resultat['niveau']}] {resultat['ioc']} "
      f"({resultat['detections']}) tags={resultat['tags']}")
```


Résultat :

```
[MALVEILLANT] 203.0.113.5 (12/80) tags=['scanner', 'bruteforce']
```


On a décodé le JSON, navigué dans les champs imbriqués avec `.get()` (sans risque de plantage), calculé un ratio de détection et produit un verdict structuré — exactement le travail d'un script d'enrichissement CTI.

## Bonus

### Joindre le résultat d'une API et un fichier local

On peut fusionner une réponse d'API (chapitre 16) avec ses notes internes :

```python
enrichi = {
    "ioc": "203.0.113.5",
    "cti": verdict_cti(brut),          # le verdict ci-dessus
    "note_interne": "Vu sur 3 serveurs le 09/01"
}
print(json.dumps(enrichi, indent=2, ensure_ascii=False))
```


## ❌ Erreur classique

```python
import json

# Confondre loads (texte) et load (fichier)
json.loads(open("f.json"))     # ❌ loads attend du texte, pas un fichier
json.load(open("f.json"))      # ✅ load lit un fichier
json.loads('{"a": 1}')         # ✅ loads lit une chaîne

# Supposer qu'un champ imbriqué existe
data["reputation"]["score"]                 # ❌ KeyError si "reputation" absent
data.get("reputation", {}).get("score", 0)  # ✅ sûr

# Oublier de convertir les nombres lus depuis un CSV (texte)
"confidence": ligne["confiance"]        # "80" (str)
"confidence": int(ligne["confiance"])   # 80 (int)
```


## Exercices

**Guidé :** Crée un script qui charge un fichier JSON contenant une liste d'IOC (`[{"value":..., "score":...}]`) et affiche uniquement ceux dont le score dépasse 70.

**Autonome :** Crée un script `csv2json_ioc.py` qui convertit un CSV d'IOC en JSON structuré (avec conversion du champ confiance en entier) et écrit le résultat avec `indent=4` et `ensure_ascii=False`.

## ✅ Tu sais maintenant…

- La correspondance JSON ⟷ Python et les fonctions `loads`/`dumps`/`load`/`dump`
- Naviguer dans une réponse CTI imbriquée avec des `[...]` et des `.get()` sûrs
- Construire et exporter un événement au format SIEM (avec horodatage `isoformat`)
- Convertir un CSV d'IOC en JSON
- Produire un verdict structuré à partir d'une réponse d'API

-----
