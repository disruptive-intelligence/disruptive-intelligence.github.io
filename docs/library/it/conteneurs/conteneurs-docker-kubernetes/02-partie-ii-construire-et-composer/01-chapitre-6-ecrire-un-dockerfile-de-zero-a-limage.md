---
title: 'Chapitre 6 — Écrire un Dockerfile : de zéro à l’image'
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie II — Construire et composer
  - index.md
---

## Le minimum à savoir

### Qu’est-ce qu’un Dockerfile ?

Un Dockerfile est un **fichier texte** qui décrit, étape par étape, comment construire une image Docker. C’est la recette de construction de ton container. Chaque ligne est une instruction que Docker exécute dans l’ordre.

### Le prérequis : comprendre YAML et les fichiers de configuration

Avant d’aller plus loin, un mot sur les fichiers de configuration. Docker utilise des Dockerfiles (syntaxe propre), Docker Compose utilise des fichiers YAML, et Kubernetes utilise aussi du YAML. Le YAML est un format texte structuré très lisible, basé sur l’**indentation** (comme Python). Voici un aperçu rapide :

```yaml
# Ceci est un commentaire YAML
nom: Alice
age: 25
langages:
  - Python
  - Bash
  - Go
serveur:
  host: 192.168.1.1
  port: 8080
```


Les règles essentielles du YAML : **2 espaces** pour l’indentation (pas de tabulations), les listes commencent par un tiret (`-`), les clés-valeurs sont séparées par un deux-points et un espace (`clé: valeur`). On utilisera le YAML à partir du chapitre 8 (Docker Compose) et du chapitre 14 (Kubernetes).

### Les instructions essentielles du Dockerfile

```dockerfile
# Chaque Dockerfile commence par FROM — l'image de base
FROM python:3.12-slim

# Définir le dossier de travail dans le container
WORKDIR /app

# Copier des fichiers depuis ta machine vers le container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables d'environnement
ENV FLASK_APP=app.py

# Port que l'application écoute (documentaire — n'expose pas réellement)
EXPOSE 5000

# La commande qui se lance quand le container démarre
CMD ["python", "app.py"]
```


Détaillons chaque instruction :

|Instruction |Rôle                                                  |Exemple                   |
|------------|------------------------------------------------------|--------------------------|
|`FROM`      |Image de base (obligatoire, toujours en premier)      |`FROM python:3.12-slim`   |
|`WORKDIR`   |Définit le dossier de travail                         |`WORKDIR /app`            |
|`COPY`      |Copie des fichiers de l’hôte vers l’image             |`COPY app.py /app/`       |
|`RUN`       |Exécute une commande pendant la construction          |`RUN pip install flask`   |
|`ENV`       |Définit une variable d’environnement                  |`ENV DEBUG=false`         |
|`EXPOSE`    |Documente le port utilisé (ne l’expose pas réellement)|`EXPOSE 8080`             |
|`CMD`       |Commande par défaut au démarrage du container         |`CMD ["python", "app.py"]`|
|`ENTRYPOINT`|Point d’entrée fixe (CMD devient les arguments)       |`ENTRYPOINT ["python"]`   |

### Construire et tester

**Étape 1 — Crée une application simple** (`app.py`) :

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello depuis un container Docker !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```


**Étape 2 — Crée le fichier des dépendances** (`requirements.txt`) :

```
flask==3.0.*
```


**Étape 3 — Crée le Dockerfile :**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```


**Étape 4 — Construis l’image :**

```bash
docker build -t mon_app .
```


`-t mon_app` donne un nom (tag) à l’image. Le `.` indique que le contexte de build est le dossier actuel.

**Étape 5 — Lance le container :**

```bash
docker run -d -p 5000:5000 mon_app
```


Ouvre `http://localhost:5000` — tu vois “Hello depuis un container Docker !”

### Le `.dockerignore`

Comme un `.gitignore`, le `.dockerignore` exclut des fichiers du contexte de build. C’est important pour la **performance** (ne pas envoyer des Go de fichiers inutiles au daemon Docker) et la **sécurité** (ne pas inclure de secrets dans l’image).

```
# .dockerignore
.git
.env
__pycache__
*.pyc
node_modules
.vscode
```


> **📋 CONTAINER — Épisode 4 (partie 1)**
> 
> Sami écrit le Dockerfile pour l’application Django de MedFlow. Première version : image de base `python:3.12` (image complète), pas de `.dockerignore`, copie de tout le repo (y compris le `.git` de 200 Mo et le fichier `.env` avec les secrets). L’image fait 1.2 Go. Premier réflexe d’optimisation au chapitre suivant.

## Très utile en pratique

### L’ordre des instructions : optimiser le cache

Docker met en cache chaque couche. Si une instruction n’a pas changé, Docker réutilise le cache au lieu de la reconstruire. L’astuce : **mettre les instructions qui changent le moins souvent en premier**.

```dockerfile
# ✅ BON ORDRE — les dépendances changent rarement, le code change souvent
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .              # ← Change rarement
RUN pip install --no-cache-dir -r requirements.txt   # ← Mis en cache si requirements.txt n'a pas changé
COPY . .                              # ← Change à chaque modification du code
CMD ["python", "app.py"]

# ❌ MAUVAIS ORDRE — tout est reconstruit à chaque changement de code
FROM python:3.12-slim
WORKDIR /app
COPY . .                              # ← Change à chaque modification
RUN pip install --no-cache-dir -r requirements.txt   # ← Reconstruit à chaque fois !
CMD ["python", "app.py"]
```


### La différence CMD vs ENTRYPOINT

`CMD` est la commande par défaut, remplaçable à l’exécution. `ENTRYPOINT` est le point d’entrée fixe.

```dockerfile
# Avec CMD — la commande peut être remplacée
CMD ["python", "app.py"]
# docker run mon_app                    → exécute python app.py
# docker run mon_app python test.py     → exécute python test.py (remplace CMD)

# Avec ENTRYPOINT + CMD — ENTRYPOINT est fixe, CMD fournit les arguments par défaut
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run mon_app                    → exécute python app.py
# docker run mon_app test.py            → exécute python test.py
```


Pour un débutant, utilise `CMD`. `ENTRYPOINT` est utile quand ton container est un outil en ligne de commande.

## Bonus

### Les labels

Les labels ajoutent des métadonnées à l’image :

```dockerfile
LABEL maintainer="sami@example.com"
LABEL version="1.0"
LABEL description="Application MedFlow"
```


### Les arguments de build (ARG)

`ARG` permet de passer des variables au moment du build (pas au runtime) :

```dockerfile
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim
```


```bash
docker build --build-arg PYTHON_VERSION=3.11 -t mon_app .
```


> **Attention sécurité :** ne passe JAMAIS de secrets via `ARG`. Les valeurs `ARG` sont visibles dans l’historique des couches (`docker history`).

## ❌ Erreur classique

```dockerfile
# Mettre COPY . . avant RUN pip install → le cache est invalidé à chaque changement de code

# Oublier --no-cache-dir dans pip install → l'image est plus grosse pour rien
RUN pip install flask                        # ❌ Conserve le cache pip dans l'image
RUN pip install --no-cache-dir flask         # ✅ Pas de cache inutile

# Utiliser ADD au lieu de COPY (sauf besoin spécifique)
ADD app.py /app/     # ❌ ADD fait des choses en plus (décompression, URL) — trop magique
COPY app.py /app/    # ✅ COPY est simple et prévisible
```


## ✅ Tu sais maintenant…

- Écrire un Dockerfile de base (`FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`)
- Construire une image avec `docker build -t nom .`
- L’importance du `.dockerignore`
- L’optimisation du cache par l’ordre des instructions

-----
