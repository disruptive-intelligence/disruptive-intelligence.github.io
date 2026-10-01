---
title: Chapitre 19 — Validation d'IP et réseaux avec ipaddress
source: IT/07 Scripting & programmation/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Pourquoi un module dédié ?

Au chapitre 4, on a vu qu'une IP est du texte et que la comparer avec `<` ne donne pas le résultat attendu. Le module `ipaddress` (inclus avec Python) comprend **vraiment** les adresses et les réseaux : il sait si une IP est privée, à quel réseau elle appartient, etc. C'est l'outil propre pour tout raisonnement réseau.

> **Note pédagogique importante — les IP de documentation :** dans tout ce cours, les plages `203.0.113.0/24`, `198.51.100.0/24` et `192.0.2.0/24` sont utilisées dans les exemples de logs. Ce sont des plages **réservées à la documentation** (RFC 5737), choisies pour ne jamais afficher de vraie IP publique. Attention : avec le module `ipaddress`, ces adresses ne sont **pas** considérées comme globalement routables — `is_private` peut donc renvoyer `True` pour elles (la sémantique de `is_private` correspond à « non globalement joignable », pas seulement aux plages privées RFC 1918, et ce comportement a été affiné dans Python 3.13). Donc, pour les exemples de **classification interne/externe** de ce chapitre, on utilise de **vraies IP publiques** comme `8.8.8.8` ou `1.1.1.1` (les DNS publics de Google et Cloudflare), uniquement comme exemples de classification — on ne fait **aucune** requête vers elles. Retiens : on extrait avec les IP de doc, mais on illustre `is_private`/`is_global` avec de vraies publiques pour obtenir des résultats fiables quelle que soit ta version de Python.

### Créer et inspecter une adresse IP

```python
import ipaddress

ip = ipaddress.ip_address("8.8.8.8")     # DNS public de Google (exemple)

print(ip.version)        # 4 (IPv4)
print(ip.is_private)     # False — c'est une IP publique (vient d'Internet)
print(ip.is_global)      # True
```


```python
interne = ipaddress.ip_address("10.0.0.4")
print(interne.is_private)    # True — réseau interne
```


> **Fini la fonction artisanale du chapitre 8 !** `ip.is_private` gère correctement **toutes** les plages privées (`10.x`, `192.168.x`, `172.16-31.x`), sans risque d'erreur — et bien plus de cas encore.

### Valider une IP

Si le texte n'est pas une IP valide, `ip_address` lève une `ValueError` — pratique pour valider une saisie :

```python
import ipaddress

def est_ip_valide(texte):
    try:
        ipaddress.ip_address(texte)
        return True
    except ValueError:
        return False

print(est_ip_valide("203.0.113.5"))    # True
print(est_ip_valide("999.1.1.1"))      # False (999 impossible)
print(est_ip_valide("pas une ip"))     # False
```


### Travailler avec des réseaux (CIDR)

Un réseau s'écrit en notation **CIDR** : `192.168.1.0/24` (les 24 premiers bits fixes). On teste facilement si une IP appartient à un réseau :

```python
import ipaddress

reseau = ipaddress.ip_network("192.168.1.0/24")

ip = ipaddress.ip_address("192.168.1.50")
print(ip in reseau)       # True — l'IP est dans ce réseau

ip2 = ipaddress.ip_address("10.0.0.1")
print(ip2 in reseau)      # False
```


L'opérateur `in` fonctionne directement entre une IP et un réseau — exactement ce qu'il faut pour vérifier une appartenance.

## Très utile en pratique

### Lister les adresses d'un réseau

```python
import ipaddress

reseau = ipaddress.ip_network("192.168.1.0/29")    # petit réseau
for ip in reseau.hosts():
    print(ip)
# 192.168.1.1 ... 192.168.1.6 (les adresses utilisables)
```


### Classer une liste d'IP en interne / externe

```python
import ipaddress

# On mélange des IP internes et de vraies IP publiques (DNS publics, en exemple)
ips = ["10.0.0.4", "8.8.8.8", "192.168.1.10", "1.1.1.1"]

internes, externes = [], []
for texte in ips:
    ip = ipaddress.ip_address(texte)
    if ip.is_private:
        internes.append(texte)
    else:
        externes.append(texte)

print("Internes :", internes)   # ['10.0.0.4', '192.168.1.10']
print("Externes :", externes)   # ['8.8.8.8', '1.1.1.1']
```


Séparer le trafic interne du trafic externe est une étape de triage très courante : une attaque venant de l'extérieur est généralement prioritaire.

### Vérifier si une IP est dans une plage à surveiller

```python
import ipaddress

# Plages internes "sensibles" (ex. serveurs critiques)
plages_sensibles = [
    ipaddress.ip_network("10.0.0.0/24"),
    ipaddress.ip_network("192.168.100.0/24"),
]

def est_sensible(ip_texte):
    ip = ipaddress.ip_address(ip_texte)
    return any(ip in reseau for reseau in plages_sensibles)

print(est_sensible("10.0.0.50"))      # True
print(est_sensible("172.16.0.1"))     # False
```


`any(...)` renvoie `True` dès qu'une des plages contient l'IP.

## Application cyber — enrichir des IP extraites d'un log

On combine extraction (regex, chapitre 13), déduplication (`set`, chapitre 7) et classification réseau (`ipaddress`) pour enrichir les IP d'un log.

```python
import re
import ipaddress

# Log d'exemple : IP internes + de vraies IP publiques (ici des DNS publics,
# utilisés uniquement comme exemples de classification — aucune requête n'est faite).
texte_log = """
Failed password for root from 8.8.8.8
Accepted password for alice from 10.0.0.4
Failed password for admin from 1.1.1.1
Connexion interne depuis 192.168.1.20
"""

# 1. Extraire et dédoublonner les IP
ips = set(re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte_log))

# 2. Enrichir chaque IP
print("=== Enrichissement des IP ===")
for texte in sorted(ips):
    try:
        ip = ipaddress.ip_address(texte)
    except ValueError:
        print(f"[-] {texte} — IP invalide, ignorée")
        continue
    origine = "interne" if ip.is_private else "EXTERNE"
    priorite = "ok" if ip.is_private else "[!] à investiguer"
    print(f"{texte:<16} {origine:<8} {priorite}")
```


Résultat :

```
=== Enrichissement des IP ===
1.1.1.1          EXTERNE  [!] à investiguer
10.0.0.4         interne  ok
192.168.1.20     interne  ok
8.8.8.8          EXTERNE  [!] à investiguer
```


> Dans un vrai `auth.log`, les IP externes seraient des adresses publiques quelconques (souvent des IP d'attaquants). On a pris ici des DNS publics connus seulement pour que `is_private` renvoie un résultat fiable et vérifiable.

On a une chaîne complète : du texte brut d'un log à une liste d'IP enrichies et priorisées. Les IP externes sont automatiquement marquées pour investigation. C'est le cœur d'un enrichissement automatique en SOC.

## Bonus

### Gérer aussi l'IPv6

`ipaddress` gère l'IPv6 de la même façon :

```python
import ipaddress

ip = ipaddress.ip_address("2001:db8::1")
print(ip.version)        # 6
print(ip.is_private)     # dépend de la plage
```


Ton code n'a pas besoin de changer : `ip_address` détecte automatiquement v4 ou v6.

## ❌ Erreur classique

```python
import ipaddress

# Comparer des IP comme du texte (chapitre 4)
"203.0.113.9" < "203.0.113.10"     # ❌ False (comparaison alphabétique !)
ipaddress.ip_address("203.0.113.9") < ipaddress.ip_address("203.0.113.10")  # ✅ True

# Oublier que ip_address plante sur une valeur invalide
ipaddress.ip_address("999.1.1.1")  # ❌ ValueError
# → entoure d'un try/except pour valider

# Confondre ip_address (une adresse) et ip_network (un réseau)
ipaddress.ip_address("192.168.1.0/24")   # ❌ ValueError (c'est un réseau)
ipaddress.ip_network("192.168.1.0/24")   # ✅
```


## Exercices

**Guidé :** Crée un script `valide_ip.py` qui prend une IP en argument et affiche si elle est valide, et si oui, si elle est privée ou publique.

**Autonome :** Crée un script `tri_ip.py` qui prend plusieurs IP en arguments, ignore les invalides (avec `try/except`), et affiche deux listes : les internes et les externes.

**Défi :** Crée un script qui prend un fichier de log, extrait toutes les IP, et affiche uniquement les IP **publiques uniques** (celles venant d'Internet), triées.

## ✅ Tu sais maintenant…

- Pourquoi `ipaddress` est meilleur que la manipulation de texte pour les IP
- Inspecter une IP (`.is_private`, `.is_global`, `.version`)
- Valider une IP avec `try/except ValueError`
- Tester l'appartenance d'une IP à un réseau CIDR (`ip in reseau`)
- Classer des IP en interne/externe et les enrichir depuis un log

-----
