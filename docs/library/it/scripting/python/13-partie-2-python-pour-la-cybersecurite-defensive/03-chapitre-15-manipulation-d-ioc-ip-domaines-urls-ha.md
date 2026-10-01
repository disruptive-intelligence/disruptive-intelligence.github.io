---
title: 'Chapitre 15 — Manipulation d''IOC : IP, domaines, URLs, hash'
source: IT/07 Scripting & programmation/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'un IOC, concrètement ?

Un **IOC** (*Indicator of Compromise*) est une donnée observable qui peut indiquer une compromission : une IP, un domaine, une URL, un hash de fichier. Manipuler des IOC, c'est les **extraire**, les **normaliser**, les **dédoublonner**, les **classer par type** et les **comparer à des listes connues**.

### Normaliser un IOC

Les IOC arrivent sous des formes variées. Avant toute comparaison, on les met en forme.

```python
def normaliser_ioc(valeur):
    return valeur.strip().lower()

print(normaliser_ioc("  EVIL.Example.COM "))   # "evil.example.com"
print(normaliser_ioc("ABCDEF123456"))           # "abcdef123456" (hash en minuscules)
```


### « Défanger » et « refanger »

Dans les rapports de menaces, les IOC sont souvent **défangés** pour éviter les clics accidentels : `hxxp://evil[.]com`. Il faut savoir les remettre en forme pour les traiter.

```python
def refang(ioc):
    """Remet un IOC défangé en forme normale."""
    return (ioc.replace("hxxp", "http")
               .replace("[.]", ".")
               .replace("(.)", "."))

print(refang("hxxps://evil[.]com/path"))    # https://evil.com/path
print(refang("203[.]0[.]113[.]5"))          # 203.0.113.5
```


> **Note défensive :** on défang justement pour **ne pas** activer un lien malveillant. Ces fonctions servent à analyser, jamais à visiter.

### Déterminer le type d'un IOC

```python
import re

def type_ioc(valeur):
    valeur = valeur.strip()
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", valeur):
        return "ip"
    if re.fullmatch(r"[a-fA-F0-9]{32}", valeur):
        return "hash_md5"
    if re.fullmatch(r"[a-fA-F0-9]{64}", valeur):
        return "hash_sha256"
    if valeur.startswith("http://") or valeur.startswith("https://"):
        return "url"
    if "." in valeur:
        return "domaine"
    return "inconnu"

for v in ["203.0.113.5", "evil.example.com", "https://bad.net/x",
          "5d41402abc4b2a76b9719d911017c592"]:
    print(f"{v} → {type_ioc(v)}")
```


```
203.0.113.5 → ip
evil.example.com → domaine
https://bad.net/x → url
5d41402abc4b2a76b9719d911017c592 → hash_md5
```


`re.fullmatch` exige que **tout** le texte corresponde au motif (contrairement à `search` qui en trouve une partie).

> **Version améliorée (à connaître après le chapitre 19) :** ici, `re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", valeur)` reconnaît la *forme* d'une IP, mais classerait aussi `999.999.999.999` comme `"ip"`. C'est la distinction extraction ≠ validation déjà vue. Une fois le module `ipaddress` connu, on peut valider réellement :
>
> ```python
> import ipaddress
>
> def est_ip(valeur):
>     try:
>         ipaddress.ip_address(valeur)
>         return True
>     except ValueError:
>         return False
> ```
>
> Le principe à retenir : **au début, on utilise une regex pour reconnaître une forme ; plus tard, on utilise `ipaddress` pour valider vraiment.** Dans `type_ioc`, tu pourrais remplacer le test regex de l'IP par `if est_ip(valeur): return "ip"`.

## Très utile en pratique

### Extraire le domaine d'une URL ou d'un email

```python
def domaine_de_url(url):
    sans_schema = url.replace("https://", "").replace("http://", "")
    return sans_schema.split("/")[0].lower()

def domaine_de_email(email):
    return email.split("@")[-1].lower()

print(domaine_de_url("https://bad.Example.com/login"))   # bad.example.com
print(domaine_de_email("attaquant@evil.example.net"))    # evil.example.net
```


### Comparer des IOC à une liste connue

```python
liste_noire = {"evil.example.com", "bad.example.net", "203.0.113.5"}

a_verifier = ["evil.example.com", "google.com", "203.0.113.5"]

for ioc in a_verifier:
    if ioc in liste_noire:
        print(f"[!] {ioc} — CONNU MALVEILLANT")
    else:
        print(f"[+] {ioc} — non listé")
```


Utiliser un `set` pour la liste noire rend la vérification très rapide, même avec des millions d'entrées.

## Application cyber — un mini-gestionnaire d'IOC

Réunissons extraction, normalisation, typage et déduplication dans un petit outil.

```python
import re

def extraire_et_classer(texte):
    """Extrait les IOC d'un texte et les range par type, sans doublons."""
    resultat = {"ip": set(), "url": set(), "email": set(), "hash": set()}

    for ip in re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", texte):
        resultat["ip"].add(ip)
    for url in re.findall(r"https?://[^\s]+", texte):
        resultat["url"].add(url.lower())
    for mail in re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", texte):
        resultat["email"].add(mail.lower())
    for h in re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", texte):
        resultat["hash"].add(h.lower())

    # On convertit les sets en listes triées pour l'affichage
    return {t: sorted(v) for t, v in resultat.items()}

rapport = """Source 203.0.113.5 et 203.0.113.5 (doublon)
URL : https://bad.example.net/x
Mail : Attaquant@Example.com
Hash : 5D41402ABC4B2A76B9719D911017C592
"""

iocs = extraire_et_classer(rapport)
for type_ioc, valeurs in iocs.items():
    if valeurs:
        print(f"[+] {type_ioc.upper()} : {valeurs}")
```


Résultat :

```
[+] IP : ['203.0.113.5']
[+] URL : ['https://bad.example.net/x']
[+] EMAIL : ['attaquant@example.com']
[+] HASH : ['5d41402abc4b2a76b9719d911017c592']
```


Le doublon d'IP a disparu (grâce au `set`), le mail et le hash sont normalisés en minuscules. C'est exactement ce qu'on veut avant d'envoyer une liste d'IOC à une plateforme CTI.

## Bonus

### Vers un format d'échange standard

Les IOC s'échangent souvent en JSON structuré (proche du standard STIX, simplifié) :

```python
ioc = {
    "type": "domain",
    "value": "evil.example.com",
    "confidence": 80,
    "source": "rapport_interne",
    "tags": ["phishing", "c2"]
}
```


On retrouve simplement un dictionnaire — exportable en JSON avec `json.dump` (chapitre 17).

## ❌ Erreur classique

```python
# Comparer des IOC sans les normaliser
"Evil.com" in {"evil.com"}        # False ❌
"Evil.com".lower() in {"evil.com"}  # True ✅

# Confondre search et fullmatch pour valider un format
import re
re.search(r"\d{1,3}(?:\.\d{1,3}){3}", "ip=203.0.113.5 !")    # matche (partie)
re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", "ip=203.0.113.5 !") # None (tout doit matcher)

# Garder les doublons (oublier set)
# → utilise set() pour dédoublonner automatiquement
```


## Exercices

**Guidé :** Crée une fonction `est_dans_liste_noire(ioc, liste)` qui normalise l'IOC puis vérifie son appartenance à une liste noire (un `set`). Teste avec des casses différentes.

**Autonome :** Crée un script qui lit un fichier texte, extrait tous les IOC (IP, URL, email, hash), les classe par type sans doublons, et écrit un rapport JSON structuré.

## ✅ Tu sais maintenant…

- Ce qu'est un IOC et les opérations clés (extraire, normaliser, typer, dédoublonner, comparer)
- Normaliser et « refanger » des IOC défangés (`hxxp`, `[.]`)
- Déterminer le type d'un IOC avec `re.fullmatch`
- Extraire le domaine d'une URL/email
- Comparer des IOC à une liste noire (avec un `set`)

-----
