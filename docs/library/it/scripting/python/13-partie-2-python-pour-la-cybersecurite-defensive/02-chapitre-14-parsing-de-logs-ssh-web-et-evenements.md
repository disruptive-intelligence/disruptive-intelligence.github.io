---
title: 'Chapitre 14 — Parsing de logs : SSH, web et événements structurés'
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Qu'est-ce que parser un log ?

**Parser**, c'est transformer une ligne de texte brute en données exploitables (un dictionnaire de champs). Chaque type de log a son format, mais la démarche est toujours la même :

```
Ligne brute  →  découper / extraire  →  dictionnaire structuré  →  analyse
```


On réutilise tout ce qu'on a vu : `split()`, regex, dictionnaires, fichiers.

### Parser un log SSH (Linux — auth.log)

Les tentatives SSH échouées sont un classique. Format typique :

```
Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5 port 51234 ssh2
```


```python
import re

ligne = "Jan 10 03:22:11 srv sshd[2451]: Failed password for root from 203.0.113.5 port 51234 ssh2"

m = re.search(r"Failed password for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})", ligne)
if m:
    evenement = {
        "type": "ssh_echec",
        "utilisateur": m.group(1),
        "ip": m.group(2),
    }
    print(evenement)
```


```
{'type': 'ssh_echec', 'utilisateur': 'root', 'ip': '203.0.113.5'}
```


### Parser un log web (Apache/Nginx — access.log)

Format « combined » typique :

```
203.0.113.5 - - [10/Jan/2025:14:30:55 +0000] "GET /admin HTTP/1.1" 403 512
```


```python
import re

ligne = '203.0.113.5 - - [10/Jan/2025:14:30:55 +0000] "GET /admin HTTP/1.1" 403 512'

m = re.search(r'(\d{1,3}(?:\.\d{1,3}){3}).*"(\S+) (\S+) [^"]+" (\d{3})', ligne)
if m:
    requete = {
        "ip": m.group(1),
        "methode": m.group(2),
        "chemin": m.group(3),
        "code": int(m.group(4)),
    }
    print(requete)
```


```
{'ip': '203.0.113.5', 'methode': 'GET', 'chemin': '/admin', 'code': 403}
```


### Parser un log « clé=valeur » (fréquent côté Windows/EDR exporté)

Beaucoup de logs Windows/SIEM exportés sont au format `clé=valeur` :

```
EventID=4625 Account=admin SourceIP=203.0.113.5 Status=failure
```


```python
ligne = "EventID=4625 Account=admin SourceIP=203.0.113.5 Status=failure"

champs = {}
for paire in ligne.split():
    if "=" in paire:
        cle, valeur = paire.split("=", 1)
        champs[cle] = valeur

print(champs["SourceIP"])    # 203.0.113.5
print(champs["EventID"])     # 4625
```


> **Note Windows :** l'`EventID` 4625 = échec d'ouverture de session, 4624 = succès. Connaître quelques ID clés aide à repérer l'essentiel sans tout mémoriser.

## Très utile en pratique

### Parser un fichier entier ligne par ligne

```python
import re

motif = re.compile(r"Failed password for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})")

evenements = []
with open("auth.log", "r", encoding="utf-8") as f:
    for ligne in f:
        m = motif.search(ligne)
        if m:
            evenements.append({"utilisateur": m.group(1), "ip": m.group(2)})

print(f"[+] {len(evenements)} échec(s) SSH")
```


On obtient une **liste de dictionnaires** — le format idéal pour analyser ensuite (compter par IP, par utilisateur…).

### Ignorer proprement les lignes qui ne matchent pas

Un log mélange beaucoup de types de lignes. Le motif ne matche que ce qui nous intéresse ; le reste est simplement ignoré (le `if m:` s'en charge). Pas besoin de `try/except` ici : si `search` ne trouve rien, il renvoie `None`.

## Application cyber — un parser SSH qui repère la force brute

```python
import re
import sys

def parser_ssh(chemin):
    """Retourne le nombre d'échecs SSH par IP."""
    motif = re.compile(r"Failed password for \S+ from (\d{1,3}(?:\.\d{1,3}){3})")
    echecs = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            m = motif.search(ligne)
            if m:
                ip = m.group(1)
                echecs[ip] = echecs.get(ip, 0) + 1
    return echecs

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <auth.log>")
        sys.exit(1)
    try:
        echecs = parser_ssh(sys.argv[1])
    except FileNotFoundError:
        print(f"[-] Fichier introuvable : {sys.argv[1]}")
        sys.exit(1)

    print("=== Tentatives SSH échouées ===")
    for ip, nb in sorted(echecs.items(), key=lambda x: x[1], reverse=True):
        if nb >= 5:
            print(f"[!] {ip} : {nb} échecs — force brute probable")
        else:
            print(f"    {ip} : {nb} échec(s)")

if __name__ == "__main__":
    main()
```


Cet outil lit un `auth.log` réel, extrait chaque IP en échec via regex, compte, trie, et signale les attaques par force brute. C'est un véritable script de triage SOC.

## Bonus

### Détecter une fenêtre temporelle (rafale d'échecs)

Pour aller plus loin, on peut extraire aussi l'horodatage et compter les échecs sur une courte fenêtre (ex. « 20 échecs en 1 minute » = signal fort). On s'appuierait sur `datetime` (chapitre 10) pour comparer les heures. C'est une bonne évolution de l'exercice une fois à l'aise.

## ❌ Erreur classique

```python
# Supposer un format unique alors que les logs varient
# → écris un motif tolérant et ignore ce qui ne matche pas

# split("=") sans limite sur une valeur contenant un "="
"url=http://x?a=b".split("=")          # ['url', 'http://x?a', 'b'] ❌
"url=http://x?a=b".split("=", 1)       # ['url', 'http://x?a=b'] ✅ (découpe 1 fois)

# Oublier que le code HTTP est extrait en texte
code = m.group(4)        # "403" (str)
if code >= 400:          # ❌ comparaison str/int
    pass
code = int(m.group(4))   # ✅
```


## Exercices

**Guidé :** Crée un script qui parse un `access.log` web et compte le nombre de réponses par code HTTP (200, 403, 404, 500…) dans un dictionnaire.

**Autonome :** Crée un script qui parse un log SSH et produit deux statistiques : les IP les plus actives en échec, **et** les noms d'utilisateurs les plus visés.

## ✅ Tu sais maintenant…

- Ce que signifie « parser » un log (texte brut → dictionnaire structuré)
- Parser des logs SSH (Linux), web (Apache/Nginx) et `clé=valeur` (Windows/SIEM)
- Transformer un fichier entier en liste de dictionnaires
- Construire un parser SSH qui repère la force brute

-----
