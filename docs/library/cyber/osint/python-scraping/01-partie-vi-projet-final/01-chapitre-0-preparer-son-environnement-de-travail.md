---
title: Chapitre 0 — Préparer son environnement de travail
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie VI — Projet final
  - index.md
---

Avant d’écrire la moindre requête, on installe **l’atelier**. Un atelier propre, c’est ce qui distingue un script jetable d’un projet OSINT sérieux. Ce chapitre prend 15 minutes, et tu n’y reviendras presque jamais.

## Le minimum à savoir

### Pourquoi un atelier propre ?

Sans atelier, tes scripts vont :

- mélanger ton code, tes données collectées et tes configurations,
- installer des bibliothèques qui polluent ton Python système,
- perdre la trace de ce qui a été installé (et donc casser à la prochaine machine),
- exposer accidentellement tes clés API si tu versionnes le tout sur Git.

Un atelier propre règle ces quatre problèmes d’un coup.

### L’arborescence standard

Crée un dossier de travail pour le cours, et organise-le ainsi :

```
osint-collecte/
├── src/              ← ton code Python
├── data/
│   ├── raw/          ← collectes brutes (HTML, JSON), JAMAIS modifiées
│   └── processed/    ← données nettoyées et exploitables
├── logs/             ← journaux d’exécution
├── reports/          ← rapports lisibles par un humain
├── config/           ← paramètres (URLs, délais, etc.)
├── .gitignore        ← ce qu’on ne versionne pas
├── requirements.txt  ← liste des bibliothèques
└── README.md         ← documentation du projet
```


> **Règle d’or :** `data/raw/` est **intouchable**. Une fois une collecte écrite dedans, on n’y touche plus. Tout le travail se fait dans `data/processed/`. Si tu casses quelque chose, tu peux toujours rejouer depuis le brut.

### Les commandes pour créer la structure

**Linux / Mac :**

```bash
mkdir -p osint-collecte/{src,data/raw,data/processed,logs,reports,config}
cd osint-collecte
touch .gitignore requirements.txt README.md
```


**Windows (PowerShell) :**

```powershell
mkdir osint-collecte
cd osint-collecte
mkdir src, data\raw, data\processed, logs, reports, config
New-Item .gitignore, requirements.txt, README.md
```


### L’environnement virtuel : isoler les dépendances

Un environnement virtuel (`venv`) est un dossier qui contient une copie isolée de Python et ses bibliothèques. Tout ce que tu installes dedans **n’affecte que ce projet**.

**Créer et activer :**

```bash
# Création (une seule fois)
python3 -m venv .venv

# Activation (à chaque session)
# Linux / Mac :
source .venv/bin/activate
# Windows (PowerShell) :
.venv\Scripts\Activate.ps1
```


Tu sauras que c’est activé parce que ton prompt change : il commence par `(.venv)`.

Pour désactiver : `deactivate`.

> **À retenir :** dès que tu travailles sur le projet, tu actives le venv. Sinon, tu installes tes bibliothèques au mauvais endroit.

### Installer les bibliothèques du cours

Une fois le venv activé :

```bash
pip install requests beautifulsoup4 lxml
```


- **`requests`** : pour faire des requêtes HTTP.
- **`beautifulsoup4`** : pour parser le HTML.
- **`lxml`** : parser HTML/XML rapide, utilisé par BeautifulSoup.

Vérifie :

```bash
pip list
```


### Geler les dépendances dans `requirements.txt`

Pour qu’un autre puisse reproduire ton environnement :

```bash
pip freeze > requirements.txt
```


Ce fichier liste précisément les versions installées. Sur une autre machine :

```bash
pip install -r requirements.txt
```


> **Pourquoi c’est crucial en OSINT :** une enquête doit être **reproductible**. Sans `requirements.txt`, ton script qui marchait il y a six mois peut casser sur une version récente d’une bibliothèque, et tu ne pourras plus refaire la collecte.

### Le fichier `.gitignore`

Si tu utilises Git (recommandé), tu dois **exclure** :

- ton environnement virtuel (lourd, recréable),
- tes données collectées (parfois sensibles, parfois personnelles),
- tes logs (verbeux),
- tes secrets (clés API).

Contenu typique de `.gitignore` :

```
# Environnement virtuel
.venv/
__pycache__/
*.pyc

# Données et logs (selon le projet)
data/raw/
data/processed/
logs/

# Secrets
.env
config/secrets.*

# Système
.DS_Store
Thumbs.db
```


> **Risque réel :** sans `.gitignore`, tu peux pousser sur GitHub une clé API, et un bot la trouvera en moins d’une heure pour s’en servir à ta place.

## Très utile en pratique

### Le fichier `README.md` minimal

Un README, c’est la première chose qu’on lit. Même pour un projet personnel, écris-en un dès le début :

```markdown
# osint-collecte

Mon atelier d’apprentissage pour le cours OSINT & scraping.

## Installation

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Usage

À venir.

## Limites et cadre

Projet pédagogique. Ne pas utiliser contre des cibles non autorisées.
```


### Tester que tout fonctionne

Crée un fichier `src/test_install.py` :

```python
import requests
from bs4 import BeautifulSoup

print("Modules importés avec succès.")
print(f"Version requests : {requests.__version__}")
```


Lance-le :

```bash
python src/test_install.py
```


Si tu vois les versions sans erreur, ton atelier est prêt.

### L’éditeur

N’importe quel éditeur fait l’affaire, mais **VS Code** avec l’extension Python est un excellent choix pour ce cours :

- coloration syntaxique,
- détection automatique du venv,
- terminal intégré,
- gestion de Git directement dans l’interface.

## ❌ Erreur classique

```bash
# Installer sans avoir activé le venv
$ pip install requests
# → installe dans le Python système, pollue, et la prochaine fois
#   sur un autre projet tu auras des conflits.

# Solution : toujours activer le venv AVANT pip install.
```


```
# Versionner ses données collectées
git add data/raw/
# → tu pousses potentiellement des données personnelles sur GitHub.
#   Le .gitignore est là pour éviter ça.
```


```bash
# Lancer python tout court alors qu'on est en venv
$ python script.py
# → sur certains systèmes, ça contourne le venv.
# Sur Linux/Mac, utilise `python3` explicitement, ou vérifie avec :
$ which python
```


## Exercices

**Guidé :** Crée l’arborescence ci-dessus, active un venv, installe `requests` et `beautifulsoup4`, génère `requirements.txt`, et lance le script `test_install.py`.

**Autonome :** Écris un `README.md` complet pour ton atelier, avec : objectif, prérequis, installation, structure des dossiers, et un rappel sur le cadre éthique (3-4 lignes).

## ✅ Tu sais maintenant…

- Pourquoi un atelier propre est indispensable en OSINT
- Créer une arborescence standard `src` / `data` / `logs` / `reports` / `config`
- Créer et activer un environnement virtuel
- Installer des bibliothèques et figer les versions dans `requirements.txt`
- Protéger tes secrets et données avec `.gitignore`

-----
