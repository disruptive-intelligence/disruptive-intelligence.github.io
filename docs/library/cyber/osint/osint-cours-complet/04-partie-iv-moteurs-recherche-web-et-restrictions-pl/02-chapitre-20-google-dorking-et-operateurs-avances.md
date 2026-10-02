---
title: Chapitre 20 — Google dorking et opérateurs avancés
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IV — Moteurs, recherche web et restrictions plateformes
  - index.md
---

## 20.1 Le dorking comme art

Le **Google dorking** (ou Google hacking) est l'art de construire des requêtes complexes pour extraire des informations précises. Inventé dans les années 2000, il reste pertinent en 2026 malgré la dégradation des opérateurs.

Un bon dork :

- Cible un type de résultat spécifique.
- Élimine le bruit.
- Utilise les opérateurs combinés.
- Reste lisible et reproductible.

## 20.2 Opérateurs Google de base

**site:** — Restreint à un domaine.

```
site:linkedin.com "Marc Delaunay"
site:.gov.fr "lanceur d'alerte"
```


**filetype:** — Type de fichier.

```
filetype:pdf "TechnoVert" 2024
filetype:xlsx "consultants" "honoraires"
```


**intitle:** — Mot dans le titre.

```
intitle:"index of" "backup"
intitle:"rapport annuel" 2024
```


**inurl:** — Mot dans l'URL.

```
inurl:rapport-annuel
inurl:wp-content
```


**intext:** — Mot dans le contenu (souvent redondant).

**ext:** — Extension de fichier (alternatif à `filetype:`).

**Guillemets `"..."`** — Recherche exacte.

```
"Marc Henri Delaunay"
```


**Parenthèses** — Groupements.

```
("TechnoVert" OR "Techno Vert") (DAF OR "directeur financier")
```


**`OR`** — Alternatives (capitales obligatoires).

**`-`** — Exclusion.

```
"Delaunay" -wikipedia -linkedin
```


**`*`** — Joker (résultats varient).

**`..`** — Plages numériques.

```
"chiffre d'affaires" 2020..2024
```


## 20.3 Dorks emblématiques

**Recherche d'index ouverts.**

```
intitle:"index of" "parent directory"
intitle:"index of" filetype:log
intitle:"index of" "backup"
```


**Recherche de fichiers exposés.**

```
filetype:env "DB_PASSWORD"
filetype:sql "INSERT INTO users"
"index of" filetype:bak
```


**Recherche d'organisations.**

```
"TechnoVert" filetype:pdf 2024
site:bodacc.fr "TechnoVert"
"Marc Delaunay" "DAF" OR "directeur administratif"
```


**Recherche de personnes.**

```
"Marc Delaunay" "X-Ponts" OR "Polytechnique"
"Marc Delaunay" 1976 site:linkedin.com
intext:"marc.delaunay@" -site:technovert.fr
```


**Recherche de présence Github.**

```
site:github.com "delaunay" "technovert"
site:gitlab.com "config" "password"
```


**Recherche d'archives.**

```
site:archive.org "verites-technovert.com"
site:web.archive.org "technovert"
```


## 20.4 Dorks Bing-spécifiques

**Bing** propose des opérateurs uniques.

**`contains:`** — Documents liés.

```
delta consulting contains:pdf
```


**`linkfromdomain:`** — Sites liés depuis un domaine.

```
linkfromdomain:technovert.fr -site:technovert.fr
```


**`ip:`** — Sites hébergés sur une IP.

```
ip:192.168.1.1
```


## 20.5 Dorks pour autres moteurs

**Yandex.** Opérateurs similaires à Google, plus quelques spécifiques (`rhost:`, `domain:`).

**Baidu.** Opérateurs `site:`, `intitle:`, `filetype:` fonctionnent.

**DuckDuckGo.** Bang operators (`!g` pour Google, `!yt` YouTube, `!w` Wikipedia) très utiles.

## 20.6 Limites modernes des dorks

En 2026, Google a **dégradé volontairement** plusieurs opérateurs.

**Limites constatées.**

- `+` supprimé depuis 2011.
- `link:` retiré en 2017.
- `cache:` largement dégradé / retiré.
- `intitle:` et `inurl:` parfois ignorés silencieusement.
- Résultats limités à ~300 même avec pagination.
- CAPTCHA fréquents pour requêtes complexes.
- Géo-personnalisation forte (deux utilisateurs voient des résultats différents).

**Compensation.**

- Utiliser plusieurs moteurs en parallèle.
- Préserver les snapshots de requêtes (Hunchly capture).
- Construire requêtes redondantes (chercher plusieurs formulations).

## 20.7 Catalogue de dorks par objectif

Voir **Annexe B** pour le catalogue complet par objectif (personne, email, username, domaine, document, leak, réseau social).

## 20.8 Recherche par opérateurs combinés : exemples MIRAGE

**Recherche financière publique.**

```
"TechnoVert" ("rapport annuel" OR "comptes consolidés") filetype:pdf 2022..2025
```


**Recherche Delaunay parcours.**

```
"Marc Delaunay" ("KPMG" OR "Deloitte" OR "Solucia") -site:linkedin.com
```


**Recherche faux compte coordonné.**

```
site:twitter.com "Antoine Berthier" ("escroc" OR "menteur" OR "manipulateur") since:2025-10
```


**Recherche structure offshore.**

```
"Delta Consulting" Malta filetype:pdf OR site:openml.gov.mt
```


**Recherche Berthier (lanceur d'alerte, pour contextualiser le narratif diffamatoire).**

```
"Antoine Berthier" "TechnoVert" OR "contrôleur de gestion" 
```


## 20.9 Pièges classiques

- **Sur-spécification** : requête trop précise → 0 résultat. Élargir progressivement.
- **Sous-spécification** : requête trop large → millions de résultats. Resserrer.
- **Personnalisation non désactivée** : résultats biaisés par votre profil.
- **Oubli de variations** : « TechnoVert » mais aussi « Techno Vert », « technovert.fr », « TechnoVert SAS ».
- **Oubli des langues** : un dork en français ne ramène pas les résultats anglais correspondants.

## 20.10 Bruit, personnalisation et signal

La principale difficulté du dorking en 2026 n'est plus l'efficacité technique mais la **qualité du signal**. Trop de résultats SEO commercial, trop de personnalisation, trop de spam de contenu généré par IA. La défense :

- Croiser plusieurs moteurs.
- Exclure les domaines pollueurs (`-site:pinterest.com -site:medium.com`).
- Privilégier les sources primaires (registres, archives, sites institutionnels).
- Utiliser Marginalia, Mojeek pour échapper au SEO.

-----
