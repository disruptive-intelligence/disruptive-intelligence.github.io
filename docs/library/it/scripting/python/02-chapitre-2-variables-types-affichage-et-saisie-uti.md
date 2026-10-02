---
title: Chapitre 2 — Variables, types, affichage et saisie utilisateur
source: IT/07 Scripting & programmation/Langages/Python.md
note: Python
up:
- - Python
  - index.md
---

## Le minimum à savoir

### Qu'est-ce qu'une variable ?

Une variable, c'est un **conteneur avec une étiquette**. L'étiquette c'est le nom, à l'intérieur il y a une valeur.

```
┌──────────────────────────┐
│  ip_source = "203.0.113.5" │   ← "ip_source" est le nom, "203.0.113.5" la valeur
└──────────────────────────┘
```


### Créer une variable

```python
ip_source = "203.0.113.5"
utilisateur = "root"
port = 22
score_risque = 8.5
est_bloquee = True
```


> **Différence avec Bash :** en Python, on met des **espaces autour du `=`** (`ip_source = "..."`). C'est l'inverse de Bash.

**Règles pour les noms de variables :**

- Que des lettres, chiffres et underscores (`_`)
- Ne peut pas commencer par un chiffre
- Pas d'espaces, pas de tirets, pas de caractères spéciaux
- Sensible à la casse (`ip` et `IP` sont deux variables différentes)

> **Convention Python :** les noms s'écrivent en `snake_case` : minuscules, mots séparés par des underscores. `ip_source` plutôt que `ipSource`.

### Les types de données

C'est ici que Python diffère fondamentalement de Bash. **En Bash, tout est du texte.** En Python, chaque valeur a un **type**, et ce type détermine ce qu'on peut faire avec.

Les 4 types de base, avec des exemples cyber :

|Type           |Nom Python|Exemple cyber                 |Ce que c'est            |
|---------------|----------|------------------------------|------------------------|
|Texte          |`str`     |`"203.0.113.5"`, `"evil.com"` |Une chaîne de caractères|
|Nombre entier  |`int`     |`22`, `443`, `404`            |Un nombre sans virgule  |
|Nombre décimal |`float`   |`8.5`, `0.95`                 |Un nombre avec virgule  |
|Booléen        |`bool`    |`True`, `False`               |Vrai ou Faux            |

```python
ip = "203.0.113.5"       # str — une IP est du texte, pas un nombre !
port = 22                # int
score = 8.5              # float
est_malveillante = True  # bool
```


Pour vérifier le type d'une variable :

```python
print(type(ip))                # <class 'str'>
print(type(port))              # <class 'int'>
print(type(est_malveillante))  # <class 'bool'>
```


> **Très important en cyber :** une adresse IP, un domaine, un hash sont du **texte** (`str`), même s'ils contiennent des chiffres. `"203.0.113.5"` n'est pas un nombre. À l'inverse, un port (`22`) ou un code HTTP (`404`) sont des nombres entiers.

### Python détecte les types automatiquement

Tu n'as pas besoin de déclarer le type. Python le devine :

```python
x = 22          # int
x = "evil.com"  # maintenant str — Python s'adapte
x = 0.95        # maintenant float
```


C'est pratique, mais une variable peut changer de type en cours de route, ce qui peut créer des bugs si tu n'y fais pas attention.

### Afficher avec `print()`

`print()` affiche du texte à l'écran. C'est l'équivalent du `echo` de Bash.

```python
ip = "203.0.113.5"
port = 22

# Méthode 1 : virgules (ajoute un espace automatiquement)
print("Connexion depuis", ip, "sur le port", port)
# → Connexion depuis 203.0.113.5 sur le port 22

# Méthode 2 : f-strings (la meilleure)
print(f"[!] Connexion depuis {ip} sur le port {port}")
# → [!] Connexion depuis 203.0.113.5 sur le port 22
```


> **À retenir :** les **f-strings** (avec le `f` devant les guillemets) sont la manière recommandée d'insérer des variables dans du texte. Entre les `{}`, tu mets le nom de la variable, Python remplace par sa valeur.

### Guillemets simples et doubles

En Python, `"texte"` et `'texte'` sont **strictement équivalents**. L'intérêt est de pouvoir imbriquer :

```python
log = "L'utilisateur 'admin' s'est connecté"
log = 'Domaine suspect : "evil.com"'
```


> **Différence avec Bash :** en Python, il n'y a **aucune différence** de comportement entre guillemets simples et doubles. Les deux interprètent les variables de la même façon dans une f-string : `f"..."` et `f'...'`.

### Lire une saisie utilisateur avec `input()`

`input()` affiche un message et attend que l'utilisateur tape quelque chose :

```python
ip = input("IP à analyser : ")
print(f"[+] Analyse de {ip} en cours...")
```


Exécution :

```
IP à analyser : 203.0.113.5
[+] Analyse de 203.0.113.5 en cours...
```


C'est l'équivalent du `read -p` de Bash.

### Le piège fondamental de `input()`

**`input()` renvoie TOUJOURS du texte** (`str`), même si l'utilisateur tape un nombre :

```python
port = input("Port : ")
print(type(port))        # <class 'str'> — c'est du TEXTE, pas un nombre !
```


Si tu veux faire des calculs ou des comparaisons numériques, tu dois **convertir** :

```python
port = int(input("Port : "))   # On convertit en entier
if port < 1024:
    print("[!] Port système (privilégié)")
```


Les fonctions de conversion :

| Fonction  | Convertit vers | Exemple                |
| --------- | -------------- | ---------------------- |
| `int()`   | Nombre entier  | `int("443")` → `443`   |
| `float()` | Nombre décimal | `float("8.5")` → `8.5` |
| `str()`   | Texte          | `str(404)` → `"404"`   |

```python
# ❌ Si tu oublies de convertir :
port = input("Port : ")          # l'utilisateur tape 22
suivant = port + 1                # ❌ TypeError : "22" + 1 impossible

# ✅ Correct :
port = int(input("Port : "))
suivant = port + 1                # ✅ 23
```


## Très utile en pratique

### Modifier une variable

```python
statut = "inconnu"
print(f"Statut : {statut}")

statut = "malveillant"
print(f"Statut mis à jour : {statut}")
```


### Affectation multiple

```python
ip, port, protocole = "203.0.113.5", 443, "https"
```


### Concaténation de texte

Pour coller deux chaînes :

```python
protocole = "https"
domaine = "exemple.com"
url = protocole + "://" + domaine
print(url)      # → https://exemple.com
```


Mais on ne peut pas coller du texte et un nombre directement :

```python
port = 443
print("Port : " + port)        # ❌ TypeError
print("Port : " + str(port))   # ✅ Fonctionne mais lourd
print(f"Port : {port}")        # ✅ Beaucoup mieux avec f-string
```


> **Bonne pratique :** utilise les f-strings plutôt que la concaténation `+`. Plus lisible, moins d'erreurs de type.

### Les f-strings en détail

Les f-strings peuvent contenir des expressions, pas seulement des variables :

```python
echecs = 47
fenetre_min = 5
print(f"{echecs} échecs en {fenetre_min} min")          # → 47 échecs en 5 min
print(f"Taux : {echecs / fenetre_min:.1f} par minute")  # → Taux : 9.4 par minute
```


## Application cyber

Modélisons une **alerte de sécurité** avec des variables typées correctement — c'est exactement ce qu'on manipulera plus tard sous forme de dictionnaire.

```python
# Une alerte SOC décrite avec des variables
ip_source = "203.0.113.5"       # str
ip_dest = "10.0.0.12"           # str
port_dest = 22                  # int
protocole = "SSH"               # str
nb_tentatives = 47              # int
score_risque = 8.5              # float
est_critique = True             # bool

print(f"[!] ALERTE — risque {score_risque}/10")
print(f"    Source      : {ip_source}")
print(f"    Destination : {ip_dest}:{port_dest} ({protocole})")
print(f"    Tentatives  : {nb_tentatives}")
print(f"    Critique    : {est_critique}")
```


Résultat :

```
[!] ALERTE — risque 8.5/10
    Source      : 203.0.113.5
    Destination : 10.0.0.12:22 (SSH)
    Tentatives  : 47
    Critique    : True
```


Note bien les **types** : les IP et le protocole sont du texte, le port et le nombre de tentatives sont des entiers, le score est un décimal, et le caractère critique est un booléen. Choisir le bon type dès le départ évite des bugs plus tard (par exemple, on ne pourra comparer `score_risque > 7` que si c'est bien un nombre).

## Bonus

### `None` — l'absence de valeur

`None` représente « rien », « pas encore de valeur » :

```python
pays_source = None     # On ne connaît pas encore le pays de l'IP
print(pays_source)     # → None
```


C'est utile pour déclarer une variable qu'on remplira plus tard (par exemple après une requête à une API de géolocalisation).

### Les chaînes multi-lignes

```python
rapport = """=== Rapport d'analyse ===
IP analysée : 203.0.113.5
Verdict     : malveillante"""

print(rapport)
```


## ❌ Erreur classique

```python
# Oublier de convertir la saisie utilisateur
port = input("Port : ")
suivant = port + 1          # ❌ TypeError — "22" + 1 ne fonctionne pas
port = int(input("Port : "))
suivant = port + 1          # ✅ 23

# Traiter une IP comme un nombre
ip = 192.168.1.1            # ❌ SyntaxError — une IP n'est PAS un nombre
ip = "192.168.1.1"          # ✅ Une IP est du texte

# Utiliser un mot réservé comme nom de variable
class = "malware"            # ❌ "class" est un mot réservé Python
categorie = "malware"        # ✅ Correct

# Oublier le f devant la f-string
ip = "203.0.113.5"
print("Source : {ip}")      # → Source : {ip}  (les accolades s'affichent telles quelles)
print(f"Source : {ip}")     # → Source : 203.0.113.5
```


## Exercices

**Guidé :** Crée un script `profil_ip.py` qui demande une IP, un port et un protocole avec `input()`, convertit le port en entier, et affiche un résumé sous la forme `"[+] {ip}:{port} via {protocole}"` avec une f-string.

**Autonome :** Crée un script `score.py` qui demande le nombre de tentatives de connexion échouées (à convertir en entier) et affiche un score de risque calculé comme `tentatives * 0.2` (avec 1 décimale), puis le texte `"[!] Surveillance recommandée"` si tu le souhaites.

## 🧩 Mini-projet (chapitres 1-2)

Crée un script `fiche_ioc.py` qui :

1. Affiche `"=== Fiche IOC ==="`.
2. Demande une adresse IP suspecte.
3. Demande un nombre de connexions observées (converti en entier).
4. Demande un niveau de confiance entre 0 et 1 (converti en `float`).
5. Affiche une fiche récapitulative claire avec des f-strings, par exemple :
   `"[!] IOC 203.0.113.5 — 47 connexions — confiance 0.9"`.

## ✅ Tu sais maintenant…

- Créer une variable et l'afficher avec `print()` et les f-strings
- Les 4 types de base : `str`, `int`, `float`, `bool`
- Qu'une IP, un domaine, un hash sont du **texte**, mais qu'un port ou un code HTTP sont des **entiers**
- Lire une saisie utilisateur avec `input()`
- Convertir entre types avec `int()`, `float()`, `str()`
- Pourquoi `input()` renvoie toujours du texte et comment gérer ça

-----
