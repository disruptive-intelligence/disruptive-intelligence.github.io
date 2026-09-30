---
title: Chapitre 18 — Calcul de hash avec hashlib
source: IT/05_Scripting_Langage-Prog/Python.md
note: Python
up:
- - Python
  - ../index.md
- - Partie 2 — Python pour la cybersécurité défensive
  - index.md
---

## Le minimum à savoir

### À quoi sert un hash en défense ?

Un **hash** est une empreinte numérique unique d'un fichier ou d'un texte. Le moindre changement dans le contenu change complètement le hash. En défense, on s'en sert pour :

- **Identifier un fichier** sans le partager (on échange le hash, pas le malware).
- **Vérifier l'intégrité** d'un fichier (a-t-il été modifié ?).
- **Comparer un fichier** à des bases de hash malveillants connus (CTI).

`hashlib` est inclus avec Python — rien à installer.

### Hasher un texte

```python
import hashlib

texte = "données à empreinter"
donnees = texte.encode("utf-8")        # hashlib travaille sur des octets

print(hashlib.md5(donnees).hexdigest())
print(hashlib.sha1(donnees).hexdigest())
print(hashlib.sha256(donnees).hexdigest())
```


> **Note :** il faut d'abord convertir le texte en **octets** avec `.encode("utf-8")`. `.hexdigest()` donne le hash en hexadécimal (le format qu'on voit partout).

### Les longueurs de hash (rappel utile)

|Algorithme |Longueur (caractères hex)|
|-----------|-------------------------|
|MD5        |32                       |
|SHA-1      |40                       |
|SHA-256    |64                       |

> **Choix défensif :** privilégie **SHA-256** pour l'identification de fichiers. MD5 et SHA-1 restent très présents dans les bases d'IOC existantes, donc tu les croiseras, mais ils sont considérés comme faibles aujourd'hui.

### Hasher un fichier (la vraie tâche du quotidien)

On lit le fichier **par blocs** pour gérer même les gros fichiers sans saturer la mémoire :

```python
import hashlib

def hash_fichier(chemin, algo="sha256"):
    h = hashlib.new(algo)
    with open(chemin, "rb") as f:        # "rb" = lecture binaire
        for bloc in iter(lambda: f.read(8192), b""):
            h.update(bloc)
    return h.hexdigest()

print(hash_fichier("rapport.pdf"))
```


> **Important :** on ouvre le fichier en mode binaire `"rb"` (pas `"r"`), car un hash se calcule sur les octets bruts, pas sur du texte. La ligne `iter(lambda: f.read(8192), b"")` lit le fichier par morceaux de 8 Ko jusqu'à la fin.

## Très utile en pratique

### Vérifier l'intégrité d'un fichier

```python
import hashlib

def hash_fichier(chemin, algo="sha256"):
    h = hashlib.new(algo)
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            h.update(bloc)
    return h.hexdigest()

attendu = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
calcule = hash_fichier("telechargement.iso")

if calcule == attendu:
    print("[+] Intégrité vérifiée")
else:
    print("[!] FICHIER ALTÉRÉ — hash différent !")
```


C'est exactement comme ça qu'on vérifie qu'un téléchargement n'a pas été corrompu ou trafiqué.

### Comparer un fichier à une liste de hash malveillants

```python
hash_malveillants = {
    "5d41402abc4b2a76b9719d911017c592",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}

h = hash_fichier("suspect.bin", "md5")
if h in hash_malveillants:
    print(f"[!] {h} — fichier connu malveillant")
else:
    print(f"[+] {h} — non listé")
```


## Application cyber — calculer les 3 hash d'un fichier (fiche d'identité)

Quand on documente un fichier suspect en forensic, on note ses trois empreintes. Voici un outil qui les calcule en une seule lecture du fichier (efficace).

```python
import hashlib
import sys

def empreintes(chemin):
    """Calcule MD5, SHA-1 et SHA-256 en une seule passe."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(8192), b""):
            md5.update(bloc)
            sha1.update(bloc)
            sha256.update(bloc)
    return {
        "fichier": chemin,
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest(),
    }

def main():
    if len(sys.argv) < 2:
        print(f"[-] Usage : python3 {sys.argv[0]} <fichier>")
        sys.exit(1)
    try:
        fiche = empreintes(sys.argv[1])
    except FileNotFoundError:
        print(f"[-] Fichier introuvable : {sys.argv[1]}")
        sys.exit(1)

    print(f"=== Empreintes de {fiche['fichier']} ===")
    print(f"MD5    : {fiche['md5']}")
    print(f"SHA-1  : {fiche['sha1']}")
    print(f"SHA-256: {fiche['sha256']}")

if __name__ == "__main__":
    main()
```


Lecture unique du fichier, mise à jour des trois algorithmes en parallèle, gestion du fichier absent : c'est l'outil que tout analyste garde sous la main pour produire la « carte d'identité » d'un fichier avant de le soumettre à une base CTI.

## Bonus

### Comparer en ignorant la casse

Les hash s'écrivent parfois en majuscules, parfois en minuscules. Normalise avant de comparer :

```python
a = "5D41402ABC4B2A76B9719D911017C592"
b = "5d41402abc4b2a76b9719d911017c592"
print(a.lower() == b.lower())     # True
```


## ❌ Erreur classique

```python
import hashlib

# Oublier d'encoder le texte en octets
hashlib.sha256("texte")              # ❌ TypeError
hashlib.sha256("texte".encode())     # ✅

# Ouvrir le fichier en mode texte au lieu de binaire
with open("f.bin", "r") as f:        # ❌ peut planter / hash faux
with open("f.bin", "rb") as f:       # ✅ binaire

# Comparer des hash de casses différentes
"ABC" == "abc"                       # ❌ False
"ABC".lower() == "abc".lower()       # ✅

# Croire qu'un hash MD5 identique = fichiers sûrs
# MD5 est faible : pour l'intégrité de sécurité, préfère SHA-256
```


## Exercices

**Guidé :** Crée un script `hash_texte.py` qui prend un texte en argument et affiche son MD5, SHA-1 et SHA-256.

**Autonome :** Crée un script `verif_hash.py` qui prend un fichier et un hash SHA-256 attendu en arguments, calcule le hash réel, et affiche si l'intégrité est vérifiée ou si le fichier a été altéré.

## ✅ Tu sais maintenant…

- À quoi servent les hash en défense (identification, intégrité, comparaison CTI)
- Hasher du texte (`.encode()` puis `.hexdigest()`)
- Hasher un fichier par blocs en mode binaire `"rb"`
- Vérifier l'intégrité et comparer à une liste de hash malveillants
- Privilégier SHA-256 et normaliser la casse avant comparaison

-----
