---
title: Chapitre 20 — Mini-projets cyber défensifs
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

> Voici huit mini-projets progressifs qui combinent tout le cours. Chacun est un vrai petit outil défensif. Commence par les premiers (plus simples) et garde les derniers comme défis. Pour chaque projet : un objectif, les notions mobilisées, et une trame de départ.

-----

### Projet 1 — Extracteur d'IOC depuis un texte

**Objectif :** lire un fichier texte (un email, un rapport) et extraire tous les IOC (IP, URLs, emails, hash), sans doublons, classés par type.

**Notions :** fichiers (ch. 10), regex (ch. 13), set/dictionnaires (ch. 7, 9), fonctions (ch. 8).

```python
import re
import sys

def extraire_iocs(texte):
    return {
        "ip": sorted(set(re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte))),
        "url": sorted(set(re.findall(r"https?://[^\s]+", texte))),
        "email": sorted(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte))),
        "hash": sorted(set(re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte))),
    }

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <fichier.txt>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        iocs = extraire_iocs(f.read())
    for type_ioc, valeurs in iocs.items():
        if valeurs:
            print(f"[+] {type_ioc.upper()} ({len(valeurs)}) : {valeurs}")

if __name__ == "__main__":
    main()
```


**Pour aller plus loin :** exporte le résultat en JSON ; ajoute la détection des hash défangés (`[.]`).

-----

### Projet 2 — Analyseur simple d'URL

**Objectif :** prendre une URL et produire une fiche : schéma, domaine, présence d'IP au lieu d'un domaine, extension suspecte, signaux d'alerte simples.

**Notions :** chaînes (ch. 6), regex (ch. 13), fonctions (ch. 8), conditions (ch. 5).

```python
import re
import sys

def analyser_url(url):
    fiche = {"url": url, "alertes": []}
    fiche["https"] = url.startswith("https://")
    sans_schema = re.sub(r"^https?://", "", url)
    fiche["domaine"] = sans_schema.split("/")[0].lower()

    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", fiche["domaine"]):
        fiche["alertes"].append("IP brute au lieu d'un domaine")
    if url.lower().endswith((".exe", ".scr", ".zip", ".js")):
        fiche["alertes"].append("extension potentiellement dangereuse")
    if not fiche["https"]:
        fiche["alertes"].append("connexion non chiffrée (http)")
    return fiche

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <url>")
        sys.exit(1)
    fiche = analyser_url(sys.argv[1])
    print(f"Domaine : {fiche['domaine']}")
    print(f"HTTPS   : {fiche['https']}")
    if fiche["alertes"]:
        for a in fiche["alertes"]:
            print(f"  [!] {a}")
    else:
        print("  [+] Aucun signal évident")

if __name__ == "__main__":
    main()
```


-----

### Projet 3 — Parser de logs SSH

**Objectif :** parser un `auth.log`, extraire les échecs par IP et par utilisateur, et afficher un résumé trié.

**Notions :** regex (ch. 13, 14), dictionnaires (ch. 9), fichiers (ch. 10), tri (ch. 7).

```python
import re
import sys

def parser(chemin):
    motif = re.compile(r"Failed password for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})")
    par_ip, par_user = {}, {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            m = motif.search(ligne)
            if m:
                user, ip = m.group(1), m.group(2)
                par_ip[ip] = par_ip.get(ip, 0) + 1
                par_user[user] = par_user.get(user, 0) + 1
    return par_ip, par_user

# (ajoute un main() avec vérif d'argument et try/except FileNotFoundError)
```


**Défi :** ajoute l'horodatage et signale les IP avec « ≥ N échecs en peu de temps ».

-----

### Projet 4 — Compteur d'échecs de connexion (détecteur de force brute)

**Objectif :** à partir des échecs par IP (projet 3), appliquer un seuil et produire une liste d'IP à bloquer, exportée en fichier.

**Notions :** dictionnaires (ch. 9), conditions (ch. 5), fichiers (ch. 10), `ipaddress` (ch. 19).

```python
import ipaddress

def ips_a_bloquer(echecs_par_ip, seuil=5):
    """Retourne les IP publiques dépassant le seuil d'échecs."""
    a_bloquer = []
    for ip, nb in echecs_par_ip.items():
        if nb < seuil:
            continue
        try:
            if not ipaddress.ip_address(ip).is_private:   # on ne bloque pas l'interne à la légère
                a_bloquer.append((ip, nb))
        except ValueError:
            continue
    return sorted(a_bloquer, key=lambda x: x[1], reverse=True)
```


> **Rappel (voir chapitre 19) :** si tu testes cette fonction avec des IP de documentation (`203.0.113.x`, `198.51.100.x`), `is_private` peut les considérer comme non publiques et donc ne pas les retenir. Pour vérifier la logique « bloquer l'externe », teste avec de vraies IP publiques comme `8.8.8.8`.

-----

### Projet 5 — Calculateur de hash de fichiers

**Objectif :** calculer MD5/SHA-1/SHA-256 d'un ou plusieurs fichiers et écrire une fiche d'empreintes.

**Notions :** `hashlib` (ch. 18), `pathlib` (ch. 10), arguments (ch. 3), JSON (ch. 17).

```python
import hashlib, json, sys
from pathlib import Path

def empreintes(chemin):
    algos = {"md5": hashlib.md5(), "sha1": hashlib.sha1(), "sha256": hashlib.sha256()}
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            for h in algos.values():
                h.update(bloc)
    return {nom: h.hexdigest() for nom, h in algos.items()}

# main() : boucle sur sys.argv[1:], écrit les fiches dans empreintes.json
```


-----

### Projet 6 — Convertisseur CSV → JSON pour des IOC

**Objectif :** transformer un export CSV d'IOC en JSON structuré, en typant et normalisant chaque IOC.

**Notions :** CSV (ch. 10), JSON (ch. 17), regex/typage (ch. 15), fonctions (ch. 8).

```python
import csv, json, sys

def typer(valeur):
    import re
    valeur = valeur.strip().lower()
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", valeur): return "ip"
    if re.fullmatch(r"[a-f0-9]{32}", valeur): return "md5"
    if re.fullmatch(r"[a-f0-9]{64}", valeur): return "sha256"
    if valeur.startswith("http"): return "url"
    return "domaine"

def convertir(csv_path, json_path):
    iocs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            valeur = ligne["valeur"].strip().lower()
            iocs.append({"value": valeur, "type": typer(valeur),
                         "confidence": int(ligne.get("confiance", 0))})
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(iocs, f, indent=4, ensure_ascii=False)
    return len(iocs)
```


-----

### Projet 7 — Mini-outil SOC : log → résumé

**Objectif :** lire un fichier de log, produire un résumé complet (total de lignes, échecs, IP uniques, top des IP en échec, part interne/externe) et l'afficher proprement.

**Notions :** tout ! fichiers, regex, dictionnaires, `ipaddress`, fonctions, robustesse.

```python
import re, sys, ipaddress

def resumer(chemin):
    motif_ip = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
    total, echecs = 0, 0
    par_ip = {}
    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            total += 1
            if "Failed password" in ligne:
                echecs += 1
                m = motif_ip.search(ligne)
                if m:
                    ip = m.group()
                    par_ip[ip] = par_ip.get(ip, 0) + 1

    externes = 0
    for ip in par_ip:
        try:
            if not ipaddress.ip_address(ip).is_private:
                externes += 1
        except ValueError:
            pass

    return {"lignes": total, "echecs": echecs,
            "ips_uniques": len(par_ip), "ips_externes": externes,
            "top": sorted(par_ip.items(), key=lambda x: x[1], reverse=True)[:5]}

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <log>"); sys.exit(1)
    try:
        r = resumer(sys.argv[1])
    except FileNotFoundError:
        print("[-] Fichier introuvable"); sys.exit(1)
    print("=== Résumé SOC ===")
    print(f"Lignes      : {r['lignes']}")
    print(f"Échecs      : {r['echecs']}")
    print(f"IP uniques  : {r['ips_uniques']} (dont {r['ips_externes']} externes)")
    print("Top IP en échec :")
    for ip, nb in r["top"]:
        print(f"  {ip} : {nb}")

if __name__ == "__main__":
    main()
```


C'est l'aboutissement du cours : un vrai mini-SIEM en une cinquantaine de lignes.

-----

### Projet 8 — Client API très simple (source générique)

**Objectif :** interroger une API (de réputation, ici simulée par `httpbin`) pour une liste d'IOC, gérer les erreurs réseau, et produire un rapport JSON des verdicts.

**Notions :** `requests` (ch. 16), JSON (ch. 17), fonctions, robustesse, boucles.

```python
import requests, json, time

def interroger(ioc):
    """Interroge une API (à remplacer par ton fournisseur CTI réel)."""
    try:
        rep = requests.get("https://httpbin.org/get",
                           params={"ioc": ioc}, timeout=5)
        rep.raise_for_status()
        return {"ioc": ioc, "statut": "ok"}     # en réel : lire le verdict renvoyé
    except requests.exceptions.RequestException as e:
        return {"ioc": ioc, "statut": "erreur", "detail": str(e)}

def main():
    iocs = ["203.0.113.5", "198.51.100.9", "evil.example.com"]
    resultats = []
    for ioc in iocs:
        r = interroger(ioc)
        print(f"[+] {r['ioc']} → {r['statut']}")
        resultats.append(r)
        time.sleep(1)                            # respecter les quotas de l'API
    with open("verdicts.json", "w", encoding="utf-8") as f:
        json.dump(resultats, f, indent=4, ensure_ascii=False)
    print("[+] Rapport écrit dans verdicts.json")

if __name__ == "__main__":
    main()
```


**Rappel :** mets ta clé d'API dans une variable d'environnement, jamais dans le code.

-----

### ✅ Tu sais maintenant…

- Combiner toutes les notions du cours dans de vrais outils défensifs
- Construire un extracteur d'IOC, un analyseur d'URL, un parser de logs SSH
- Détecter la force brute et produire une liste d'IP à bloquer
- Calculer des empreintes de fichiers et convertir des IOC entre formats
- Assembler un mini-outil SOC complet (log → résumé)
- Écrire un client API défensif robuste

-----


## Conclusion

Tu es parti de zéro et tu disposes maintenant d'une vraie base : écrire des scripts Python clairs, structurés et **orientés défense**.

**Partie 1 — Les fondamentaux :**

- Script, variables, arguments (ch. 1-3)
- Calculs, logique, conditions (ch. 4-5)
- Chaînes, listes, boucles, fonctions, dictionnaires (ch. 6-9)
- Fichiers, CSV, JSON, erreurs, automatisation (ch. 10-12)

**Partie 2 — La cybersécurité défensive :**

- Regex et extraction d'IOC (ch. 13)
- Parsing de logs (ch. 14)
- Manipulation d'IOC (ch. 15)
- APIs et `requests` (ch. 16)
- JSON avancé CTI/SIEM (ch. 17)
- Hash avec `hashlib` (ch. 18)
- IP et réseaux avec `ipaddress` (ch. 19)
- Mini-projets défensifs (ch. 20)

**Pour continuer à progresser :**

- Écris des scripts pour tes propres besoins d'analyse — c'est la meilleure façon d'apprendre.
- `help(fonction)` dans le mode interactif reste ton meilleur ami.
- La documentation officielle [docs.python.org](https://docs.python.org) est excellente.
- Entraîne-toi sur des **logs et données de test** que tu génères toi-même, jamais sur des systèmes qui ne t'appartiennent pas.

**Prochaines étapes possibles (toujours côté défense) :**

- Approfondir les regex pour des formats de logs plus variés.
- Automatiser l'enrichissement d'IOC via plusieurs sources CTI.
- Stocker tes résultats dans une base `sqlite3` pour les requêter.
- Découvrir des bibliothèques d'analyse comme `pandas` pour de gros volumes de logs.
- Planifier tes scripts (cron) pour une surveillance continue.

**Rappel final d'éthique :** ces compétences servent à **protéger, détecter et comprendre**. N'analyse que des systèmes et des données que tu es autorisé à examiner. La cybersécurité défensive, c'est d'abord une question de responsabilité.

Bon scripting, et bonne défense !
