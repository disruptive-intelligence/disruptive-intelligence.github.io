---
title: Chapitre 16 — Requêtes HTTP et APIs CTI avec requests
source: IT/07 Scripting & programmation/Langages/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Installer `requests`

`requests` est le seul module non inclus de ce cours. Installe-le :

```bash
pip install requests
# ou, selon ton système :
pip3 install requests
```


C'est la bibliothèque standard de fait pour faire des requêtes HTTP en Python. On l'utilise pour interroger des **APIs de threat intelligence** (réputation d'IP, infos sur un domaine, etc.).

> **Connexion Internet requise :** tous les exemples de ce chapitre utilisent `httpbin.org`, un service public de test, et nécessitent donc un accès Internet. Si tu es sur un réseau filtré, derrière un proxy, ou dans un environnement isolé, ces exemples peuvent échouer **même si ton code est correct**. Dans ce cas, ce n'est pas un bug : c'est le réseau. Le raisonnement et la structure du code restent valables.

### Une première requête GET

```python
import requests

reponse = requests.get("https://httpbin.org/get")

print(reponse.status_code)     # 200 (succès)
print(reponse.text[:80])        # le contenu (texte)
```


`requests.get(url)` renvoie un objet **réponse** avec :

- `.status_code` → le code HTTP (200 = OK, 404 = absent, 403 = interdit…)
- `.text` → le contenu brut en texte
- `.json()` → le contenu décodé si c'est du JSON (le plus utile pour les APIs)

### Lire une réponse JSON d'API

La plupart des APIs renvoient du JSON, que `requests` convertit directement en dictionnaire Python :

```python
import requests

reponse = requests.get("https://httpbin.org/json")
donnees = reponse.json()         # → dictionnaire Python

print(type(donnees))             # <class 'dict'>
print(donnees.keys())            # les clés disponibles
```


> **Lien clé :** `.json()` te rend un **dictionnaire** — tu retrouves tout ce que tu sais du chapitre 9 pour explorer la réponse.

### Vérifier le code de statut avant de traiter

```python
import requests

reponse = requests.get("https://httpbin.org/status/404")

if reponse.status_code == 200:
    print("[+] OK, traitement de la réponse")
    donnees = reponse.json()
else:
    print(f"[-] Erreur HTTP {reponse.status_code}")
```


## Très utile en pratique

### Passer des paramètres et un timeout

```python
import requests

params = {"ip": "203.0.113.5"}
reponse = requests.get(
    "https://httpbin.org/get",
    params=params,
    timeout=5            # toujours un timeout : ne pas bloquer indéfiniment
)
print(reponse.url)       # .../get?ip=203.0.113.5
```


> **Bonne pratique :** mets **toujours** un `timeout`. Sans lui, ton script peut rester bloqué si l'API ne répond pas.

### Envoyer une clé d'API dans les en-têtes

Les APIs CTI exigent souvent une clé d'authentification, transmise dans les en-têtes :

```python
import requests

headers = {"x-apikey": "TA_CLE_API"}      # ne JAMAIS écrire la clé en dur en vrai
reponse = requests.get("https://api.exemple-cti.test/ip/203.0.113.5",
                       headers=headers, timeout=5)
```


> **Sécurité :** ne mets jamais une vraie clé d'API directement dans le code. Lis-la depuis une variable d'environnement (`os.getenv("CTI_API_KEY")`) ou un fichier de config non versionné.

### Gérer les erreurs réseau

Le réseau peut échouer (pas de connexion, API en panne). On entoure d'un `try/except` :

```python
import requests

try:
    reponse = requests.get("https://httpbin.org/get", timeout=5)
    reponse.raise_for_status()       # lève une erreur si code 4xx/5xx
    donnees = reponse.json()
    print("[+] Réponse reçue")
except requests.exceptions.Timeout:
    print("[-] L'API n'a pas répondu à temps")
except requests.exceptions.RequestException as e:
    print(f"[-] Erreur réseau : {e}")
```


## Application cyber — un client de réputation d'IP (générique)

Voici un client simple qui interroge une API de réputation et interprète la réponse. On utilise une API publique de test (`httpbin`) pour que le code soit exécutable sans clé ; en réel, tu remplacerais l'URL par celle de ton fournisseur CTI.

```python
import requests

def verifier_ip(ip):
    """Interroge une API de réputation (ici simulée) et renvoie un verdict."""
    url = "https://httpbin.org/get"        # remplace par ton API CTI réelle
    try:
        rep = requests.get(url, params={"ip": ip}, timeout=5)
        rep.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"ip": ip, "statut": "erreur", "detail": str(e)}

    donnees = rep.json()
    # En réel, on lirait par ex. donnees["malicious_score"].
    # Ici on illustre juste l'accès aux champs renvoyés.
    return {
        "ip": ip,
        "statut": "ok",
        "echo_params": donnees.get("args", {}),
    }

for ip in ["203.0.113.5", "198.51.100.9"]:
    resultat = verifier_ip(ip)
    print(f"[+] {resultat['ip']} → {resultat['statut']} {resultat.get('echo_params')}")
```


La structure est celle de tous les clients CTI : construire l'URL, envoyer la requête avec un timeout, gérer les erreurs réseau, décoder le JSON, extraire les champs utiles et renvoyer un verdict structuré. Pour passer en réel, il suffit de changer l'URL, d'ajouter la clé d'API et de lire les bons champs de la réponse.

## Bonus

### Boucler sur une liste d'IOC (avec pause)

Quand tu interroges une API pour plusieurs IOC, respecte ses limites de débit :

```python
import time

for ip in ["203.0.113.5", "198.51.100.9"]:
    resultat = verifier_ip(ip)
    print(resultat)
    time.sleep(1)        # 1 seconde entre deux requêtes (politesse + quotas)
```


## ❌ Erreur classique

```python
import requests

# Oublier le timeout → script qui peut se bloquer
requests.get(url)                 # ❌
requests.get(url, timeout=5)      # ✅

# Appeler .json() sur une réponse qui n'est pas du JSON
reponse.json()                    # ❌ JSONDecodeError si c'est du HTML/texte
# → vérifie status_code et le type de contenu d'abord

# Écrire sa clé d'API en dur dans le script
headers = {"x-apikey": "abc123..."}   # ❌ ne jamais committer ça
import os
headers = {"x-apikey": os.getenv("CTI_API_KEY")}   # ✅

# Ne pas gérer les erreurs réseau → crash au moindre souci de connexion
```


## Exercices

**Guidé :** Crée un script `ping_api.py` qui fait un `requests.get` sur `https://httpbin.org/status/200`, vérifie le `status_code`, et affiche `"[+] API joignable"` ou `"[-] Problème"`.

**Autonome :** Crée une fonction `interroger(ioc)` qui interroge `https://httpbin.org/get` avec l'IOC en paramètre, gère les erreurs réseau avec `try/except`, et retourne un dictionnaire `{"ioc": ..., "statut": "ok"/"erreur"}`. Boucle sur une liste de 3 IOC avec une pause d'1 seconde.

## ✅ Tu sais maintenant…

- Installer et utiliser `requests` pour faire des requêtes HTTP
- Lire `.status_code`, `.text` et surtout `.json()` (→ dictionnaire)
- Passer des paramètres, des en-têtes (clé d'API) et un `timeout`
- Gérer les erreurs réseau avec `try/except`
- Construire un client de réputation d'IOC générique
- Protéger ses clés d'API (variables d'environnement)

-----
