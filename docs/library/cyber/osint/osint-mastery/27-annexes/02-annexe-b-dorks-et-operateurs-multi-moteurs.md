---
title: ANNEXE B — Dorks et opérateurs multi-moteurs
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - Annexes
  - index.md
---

> **État des connaissances : mai 2026.** Les opérateurs ci-dessous reflètent les fonctionnalités des moteurs à cette date. Les moteurs **modifient et restreignent régulièrement** leurs opérateurs (Google notamment a déprécié plusieurs opérateurs entre 2020 et 2025). Tester les dorks avant usage critique.

Inventaire pratique des **dorks** (requêtes structurées) pour les principaux moteurs et services OSINT. À utiliser avec discernement : certains dorks peuvent enfreindre CGU ou s'approcher de zones grises légales (recherche de credentials notamment).


## B.1 — Dorks Google

**Opérateurs principaux.**

- `"phrase exacte"` — recherche littérale.
- `-mot` — exclusion.
- `site:domaine.com` — restriction à un domaine.
- `inurl:mot` — mot dans URL.
- `intitle:mot` — mot dans titre.
- `intext:mot` — mot dans corps.
- `filetype:pdf` — type de fichier.
- `before:2024-12-31` / `after:2020-01-01` — date.
- `OR` ou `|` — alternative.
- `AND` ou `+` — conjonction (implicite).
- `*` — wildcard.

**Opérateurs dépréciés ou instables 2026.** `cache:`, `link:`, `info:` ne fonctionnent plus de manière fiable. `+` strict est partiellement réintroduit.

**Documents internes accidentellement exposés.**

```
site:technovert.fr filetype:pdf "confidential"
site:technovert.fr filetype:doc OR filetype:docx
site:technovert.fr filetype:xlsx
site:technovert.fr inurl:internal
"technovert" filetype:pdf "internal use only"
```


**Identités d'employés.**

```
site:linkedin.com/in/ "technovert"
"@technovert.fr" -site:technovert.fr
"works at technovert" site:facebook.com
"employé technovert" OR "salarié technovert"
```


**Credentials et fuites (à utiliser avec EXTRÊME prudence).**

```
"technovert" "password" filetype:txt
"@technovert.fr" "password"
inurl:wp-config.php "technovert"
"technovert" intext:"DB_PASSWORD"
"technovert" filetype:env
```


**Sous-domaines.**

```
site:*.technovert.fr -site:www.technovert.fr
```


**Erreurs révélatrices d'infrastructure.**

```
"technovert" intext:"Apache 2.4" inurl:phpinfo.php
"Index of /" "technovert"
intitle:"index of" "technovert" private
"technovert" intitle:"sql syntax error"
```


**Documents techniques.**

```
"technovert" filetype:log
"technovert" filetype:sql
"technovert" filetype:bak
"technovert" filetype:conf OR filetype:cfg
```



## B.2 — Dorks DuckDuckGo

DuckDuckGo accepte la plupart des opérateurs Google avec quelques spécificités :

- `!bang` redirige vers autres moteurs : `!g technovert` → Google, `!yt` → YouTube, `!w` → Wikipedia, `!gh` → GitHub.
- Plus respectueux privacy.
- Index propre + sources Bing.
- `region:fr-fr` — restriction régionale.

**Utile pour OSINT.** DuckDuckGo n'a pas la personnalisation Google. Résultats plus uniformes, sans bulle de filtre. Utile pour comparaison.


## B.3 — Dorks Bing

Opérateurs proches de Google avec spécificités :

- `contains:type` — pages contenant fichiers de ce type (`contains:pdf`).
- `feed:` — flux RSS.
- `hasfeed:` — pages avec flux RSS.
- `language:fr` — langue.
- `loc:FR` — localisation.
- `ip:192.168.x.x` — pages servies par cette IP (utile OSINT infrastructure).
- `linkfromdomain:domaine.com` — pages liées depuis ce domaine.

**Bing est souvent meilleur pour :** indexation profonde sites US, contenu Microsoft, archives OneDrive / SharePoint.


## B.4 — Dorks Yandex

Yandex utilise des opérateurs proches mais avec syntaxe propre :

- `mime:pdf` au lieu de `filetype:pdf`.
- `lang:fr` (codes ISO).
- `domain:technovert.fr`.
- `url:"path"` — recherche dans URL.
- `title:"phrase"` — dans titre.
- `<<` / `>>` — proximité (deux mots à N positions).
- `& & &` — opérateurs de proximité (mots dans même phrase, paragraphe, document).

**Très utile pour.** Requêtes en russe / CEI, recherches d'images, indexation différente.


## B.5 — Dorks Shodan

Spécifique à infrastructure exposée.

**Opérateurs.**

- `port:22` — port spécifique.
- `country:FR` — pays.
- `city:Paris`.
- `org:"TechnoVert"` — organisation.
- `hostname:technovert.fr` — hostname.
- `ssl.cert.subject.cn:technovert` — CN du certificat.
- `ssl.cert.issuer.cn:"Let's Encrypt"` — émetteur.
- `product:Apache` — produit.
- `version:"2.4"` — version.
- `os:Linux` — OS.
- `before:2024-01-01`, `after:2023-01-01` — date.
- `tag:vpn` / `tag:webcam` / `tag:ics` — tags Shodan.
- `has_screenshot:true` — captures disponibles.
- `vuln:CVE-2021-44228` — vulnérabilité spécifique.

**Exemples.**

```
hostname:technovert.fr port:443
org:"TechnoVert" country:FR
ssl.cert.subject.cn:technovert
"webcam" country:FR
port:3389 has_screenshot:true   # RDP exposés (très sensible)
product:"Apache" version:"2.2"  # versions obsolètes
"Apache/2.4.49" "X-Powered-By"  # vulnérables CVE-2021-41773
vuln:CVE-2021-44228             # Log4Shell exposés
```



## B.6 — Dorks Censys

Syntaxe différente mais capacités similaires.

```
services.tls.certificates.leaf_data.subject.common_name:technovert
services.banner:"server: apache"
services.port:443
location.country_code:FR
autonomous_system.organization:"OVH SAS"
labels:`expired-cert`
last_updated_at:[2024-01-01 TO 2024-12-31]
```


Censys propose **Censys Search** (web) et **Censys ASM** (continu).


## B.7 — Dorks GitHub

Recherche de code et de secrets.

**Opérateurs.**

- `user:username` — utilisateur.
- `org:org-name` — organisation.
- `repo:user/repo` — dépôt spécifique.
- `filename:.env` — nom de fichier.
- `extension:py` — extension.
- `language:python`.
- `path:src/` — chemin.
- `created:>2024-01-01` — créé après.
- `pushed:>2024-01-01` — pushed après.
- `stars:>100` — étoiles.

**Dorks pour secrets exposés (déontologie attentive).**

```
"technovert" "password"
"@technovert.fr" extension:env
filename:.env "technovert"
"DB_PASSWORD" "technovert"
"api_key" "technovert"
"AWS_SECRET_ACCESS_KEY" "technovert"
filename:credentials "technovert"
"BEGIN RSA PRIVATE KEY" "technovert"
```


**Détection d'employés.**

```
"@technovert.fr" extension:py
user:* email:@technovert.fr
```



## B.8 — Dorks Telegram (via Telegago, Lyzem)

Telegram n'a pas d'opérateurs natifs riches en search public. Mais Telegago / Lyzem indexent canaux publics.

**Telegago.fr.**

- Recherche par mots-clés simples.
- Filtres par type de canal, taille.
- Tri par activité.

**Lyzem.com.**

- Recherche dans messages historiques.
- Filtres date, canal.
- Indexation plus large.

**Recherches typiques.**

- Nom de cible + secteur.
- Domaines suspects.
- Stealer logs (« cloud accounts », « combo list », etc.).
- Vente de données.


## B.9 — Dorks LinkedIn

LinkedIn restreint fortement. Quelques techniques :

**Recherche externe via Google.**

```
site:linkedin.com/in/ "technovert"
site:linkedin.com/in/ "ingénieur" "technovert"
site:linkedin.com/in/ inurl:"marc-delaunay"
site:linkedin.com/company "technovert"
```


**Filtres internes (Sales Navigator ou compte invest).**

- Industrie.
- Localisation.
- Ancienneté (« years of experience »).
- Postes actuels et passés.
- Écoles fréquentées.
- Compétences.
- Boolean : `("DAF" OR "CFO") AND "technovert" AND "Paris"`.

**Pour identifier transfuges.** Recherche par « previously at Technovert » via Sales Navigator.


## B.10 — Dorks Twitter / X

**X search avancée.** twitter.com/search-advanced (encore actif partiellement en 2026 selon évolutions).

**Opérateurs.**

- `from:username`.
- `to:username`.
- `since:2024-01-01`.
- `until:2024-12-31`.
- `near:"Paris" within:10km` (souvent désactivé).
- `lang:fr`.
- `filter:images`, `filter:videos`, `filter:links`.
- `min_retweets:50`.
- `min_likes:100`.
- `-filter:replies` — exclure réponses.

**Exemples.**

```
from:mdelaunay76 since:2024-01-01
"technovert" filter:images since:2025-09-01
"@mdelaunay76" -from:mdelaunay76   # mentions de
"technovert" lang:fr min_retweets:10
```



## B.11 — Dorks Wayback Machine

**Recherches Wayback.**

- `web.archive.org/web/*/technovert.fr` — toutes les versions.
- `web.archive.org/web/2020*/technovert.fr` — versions 2020.
- `archive.org/wayback/available?url=technovert.fr&timestamp=20200101` — API.

**Astuce.** Wayback indexe parfois des pages depuis longtemps supprimées de l'original. Très utile pour archives.


## B.12 — Dorks WHOIS / DomainTools

Via DomainTools (payant) :

- Recherche WHOIS historique par email.
- Recherche par nom du registrant (pre-RGPD).
- Recherche par adresse postale.
- Recherche par téléphone.
- Reverse IP, reverse NS.

**Outils gratuits.**

- ViewDNS.info : reverse IP, reverse WHOIS basique.
- crt.sh : Certificate Transparency (couvre indirectement).


## B.13 — Dorks moteurs académiques

**Google Scholar.**

- `author:"X. Smith"` — auteur.
- `intitle:"climate"` — dans titre.
- `source:"Nature"` — journal source.
- `year:2024..2026` — plage années.

**Semantic Scholar.** Recherche par auteur, sujet, citations.

**Sci-Hub** (controversé, copyright) : archive massive d'articles.


## B.14 — Discipline d'usage

**Bonne pratique.**

- Variations multiples sur même requête.
- Comparer résultats entre moteurs.
- Documenter les dorks ayant produit résultats utiles dans le journal d'enquête.
- Captures Hunchly systématiques.

**Limites éthiques et légales.**

- Dorks de recherche de credentials = zone grise (passage à exploitation = pénal).
- Reverse engineering de configurations privées = passage à zone Bluetouff.
- Respect CGU des moteurs (généralement larges pour recherche).

**Ressources.**

- **GHDB** (Google Hacking Database, exploit-db.com) : catalogue communautaire.
- **OSINT Combine Cheat Sheets** : références par sujet.
- **Awesome OSINT** (GitHub) : compilation.

-----
