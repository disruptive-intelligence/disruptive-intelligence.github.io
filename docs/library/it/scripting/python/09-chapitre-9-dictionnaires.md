---
title: Chapitre 9 — Dictionnaires
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
chapter: 9
chapters: 20
---

## Le minimum à savoir

### Qu'est-ce qu'un dictionnaire ?

Un dictionnaire stocke des **paires clé-valeur** : tu cherches une clé et tu trouves sa valeur. En cyber, c'est l'outil parfait pour représenter une **alerte**, un **événement SIEM** ou une **fiche IOC** : chaque info a un nom.

```python
alerte = {
    "ip_source": "203.0.113.5",
    "port": 22,
    "type": "ssh_bruteforce",
    "severite": "haute",
    "nb_echecs": 47
}
```

> **Comparaison avec Bash :** équivalent des tableaux associatifs (`declare -A`), mais natif et omniprésent en Python.

### Accéder à une valeur

```python
print(alerte["ip_source"])     # "203.0.113.5"
print(alerte["severite"])      # "haute"
```

Si la clé n'existe pas → erreur `KeyError`. Pour éviter ça, utilise `.get()` :

```python
print(alerte["pays"])               # ❌ KeyError
print(alerte.get("pays"))           # None (pas d'erreur)
print(alerte.get("pays", "inconnu")) # "inconnu" (valeur par défaut)
```

> **Réflexe cyber :** les données venant d'un log ou d'une API sont souvent incomplètes. Utilise `.get(clé, défaut)` plutôt que `[clé]` pour ne pas planter sur un champ manquant.

### Ajouter et modifier

```python
alerte["pays"] = "RU"            # ajouter une clé
alerte["severite"] = "critique"  # modifier une valeur existante
```

### Supprimer

```python
del alerte["port"]               # supprimer une paire
valeur = alerte.pop("nb_echecs") # supprimer et récupérer
```

### Vérifier si une clé existe

```python
print("ip_source" in alerte)     # True
print("hash" in alerte)          # False
```

> **Note :** `in` teste les **clés**, pas les valeurs.

### Parcourir un dictionnaire

```python
alerte = {"ip": "203.0.113.5", "port": 22, "type": "ssh"}

# Les paires clé-valeur (le plus utile)
for cle, valeur in alerte.items():
    print(f"{cle} : {valeur}")
```

```
ip : 203.0.113.5
port : 22
type : ssh
```

La méthode `.items()` donne clés et valeurs ensemble — idéale pour afficher une fiche complète.

## Très utile en pratique

### Le dictionnaire comme fiche IOC

```python
ioc = {
    "valeur": "203.0.113.5",
    "type": "ip",
    "source": "feed_interne",
    "confiance": 0.9,
    "actif": True
}

print(f"[{ioc['type'].upper()}] {ioc['valeur']} — confiance {ioc['confiance']}")
```

C'est l'usage le plus courant : regrouper des informations liées dans une seule structure nommée.

### Liste de dictionnaires (pattern central)

Un export SIEM, une liste d'événements, un feed d'IOC : presque toujours une **liste de dictionnaires**.

```python
evenements = [
    {"ip": "203.0.113.5", "action": "echec", "user": "root"},
    {"ip": "10.0.0.4", "action": "succes", "user": "alice"},
    {"ip": "203.0.113.5", "action": "echec", "user": "admin"},
]

for ev in evenements:
    if ev["action"] == "echec":
        print(f"[!] Échec : {ev['user']} depuis {ev['ip']}")
```

```
[!] Échec : root depuis 203.0.113.5
[!] Échec : admin depuis 203.0.113.5
```

### Récapitulatif

| Opération        | Syntaxe                          |
| ---------------- | -------------------------------- |
| Créer            | `d = {"cle": "valeur"}`          |
| Lire (sûr)       | `d.get("cle", défaut)`           |
| Ajouter/modifier | `d["cle"] = valeur`              |
| Supprimer        | `del d["cle"]` ou `d.pop("cle")` |
| Tester une clé   | `"cle" in d`                     |
| Parcourir        | `for k, v in d.items():`         |
| Nombre de clés   | `len(d)`                         |

## Application cyber — compter et regrouper

Le dictionnaire brille pour **agréger** : compter les échecs par IP, regrouper les événements par type. Reprenons le comptage du chapitre 7, version dictionnaire complète.

```python
evenements = [
    {"ip": "203.0.113.5", "action": "echec"},
    {"ip": "203.0.113.5", "action": "echec"},
    {"ip": "10.0.0.4", "action": "succes"},
    {"ip": "203.0.113.5", "action": "echec"},
    {"ip": "198.51.100.9", "action": "echec"},
]

# Compter les échecs par IP
echecs_par_ip = {}
for ev in evenements:
    if ev["action"] == "echec":
        ip = ev["ip"]
        echecs_par_ip[ip] = echecs_par_ip.get(ip, 0) + 1

# Produire un résumé sous forme de dictionnaire d'alertes
resume = {
    "total_evenements": len(evenements),
    "ips_en_echec": len(echecs_par_ip),
    "detail": echecs_par_ip
}

print(f"[*] {resume['total_evenements']} événements analysés")
print(f"[*] {resume['ips_en_echec']} IP en échec")
for ip, nb in resume["detail"].items():
    if nb >= 3:
        print(f"  [!] {ip} : {nb} échecs — force brute probable")
```

Résultat :

```
[*] 5 événements analysés
[*] 2 IP en échec
  [!] 203.0.113.5 : 3 échecs — force brute probable
```

On a utilisé `.get(cle, 0) + 1` pour compter, et un dictionnaire pour structurer le résumé. C'est exactement la forme qu'aurait le résultat d'un mini-SIEM.

## Bonus

### Dictionnaires imbriqués (config d'outil)

```python
config = {
    "seuils": {"echecs_critique": 5, "score_alerte": 7},
    "sortie": {"format": "json", "fichier": "rapport.json"}
}

print(config["seuils"]["echecs_critique"])    # 5
```

C'est la forme typique d'un fichier de configuration JSON (chapitre 10).

### Compter les occurrences en une boucle

```python
texte = "Failed Failed Accepted Failed"
compteur = {}
for mot in texte.split():
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)    # {'Failed': 3, 'Accepted': 1}
```

## ❌ Erreur classique

```python
# Accéder à une clé inexistante sans get()
alerte = {"ip": "203.0.113.5"}
print(alerte["pays"])          # ❌ KeyError
print(alerte.get("pays", "?")) # ✅ "?"

# Confondre clé et valeur avec "in"
print("203.0.113.5" in alerte)            # False — c'est une valeur, pas une clé !
print("203.0.113.5" in alerte.values())   # True — là on cherche dans les valeurs

# Confondre liste et dictionnaire
ips = ["a", "b"]               # liste : indexée par des nombres
scores = {"a": 1, "b": 2}      # dict : indexé par des clés
```

## Exercices

**Guidé :** Crée un dictionnaire `alerte` avec les clés `ip`, `type`, `severite`, `nb_echecs`. Affiche chaque paire avec `.items()`, puis affiche `"[!] CRITIQUE"` si `severite` vaut `"haute"`.

**Autonome :** Crée un script qui prend une phrase de log en argument, découpe-la en mots avec `split()`, et compte les occurrences de chaque mot dans un dictionnaire. Affiche les résultats.

## 🧩 Mini-projet (chapitres 8-9)

Crée un script `fiches_ioc.py` qui :

1. Contient une **liste de dictionnaires** IOC (chaque IOC a `valeur`, `type`, `confiance`).
2. Définit une **fonction** `afficher_ioc(ioc)` qui affiche une fiche formatée.
3. Définit une **fonction** `iocs_fiables(liste, seuil)` qui retourne la liste des IOC dont la confiance dépasse le seuil.
4. Affiche toutes les fiches, puis seulement les IOC de confiance ≥ 0.8.

## ✅ Tu sais maintenant…

- Créer, lire, modifier, supprimer des éléments d'un dictionnaire
- Utiliser `.get(cle, défaut)` pour gérer les champs manquants (réflexe cyber)
- Parcourir avec `.items()`
- Modéliser une alerte / un événement / une fiche IOC avec un dictionnaire
- Le pattern « liste de dictionnaires » pour les exports SIEM et feeds d'IOC
- Agréger des données (compter les échecs par IP)

-----
