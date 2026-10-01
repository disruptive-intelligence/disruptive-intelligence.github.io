---
title: Chapitre 21 — Moteurs spécialisés OSINT
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IV — Moteurs, recherche web et restrictions plateformes
  - index.md
---

## 21.1 Au-delà des moteurs généralistes

Les moteurs généralistes indexent le web visible. Les **moteurs spécialisés OSINT** explorent des espaces que Google n'indexe pas : services Internet exposés, leaks et breaches, dépôts de code, archives spécifiques. Maîtriser ces outils est l'un des sauts qualitatifs majeurs de l'analyste OSINT.

## 21.2 Shodan : le « moteur de l'Internet des choses »

**Shodan** (shodan.io) indexe les services Internet exposés (HTTP, SSH, FTP, RTSP, MQTT, etc.) en scannant systématiquement Internet.

**Cas d'usage OSINT.**

- Identifier l'infrastructure exposée d'une entité (serveurs, caméras, ICS).
- Recherche par bannière, technologie, version.
- Identification de devices compromis (vulnérabilités connues).
- Pivot infrastructure → entité propriétaire.

**Requêtes utiles.**

```
hostname:technovert.fr
ssl.cert.subject.cn:"technovert"
http.title:"TechnoVert"
port:22 country:FR org:"TechnoVert"
```


**Tarification.** Shodan a un freemium limité. La version Membership (annuelle) est nécessaire pour un usage professionnel.

## 21.3 Censys : complémentaire

**Censys** (censys.io) joue un rôle similaire à Shodan mais avec une approche différente (scan plus exhaustif, focus sur les certificats TLS).

**Forces.**

- Recherche par certificat TLS (toutes les variations).
- Données historiques (vue dans le temps).
- Interface plus structurée pour les queries complexes.

**Combinaison Shodan + Censys.** Standard professionnel. Ils se complètent : ce que l'un manque, l'autre l'attrape souvent.

## 21.4 FOFA et ZoomEye

**FOFA** (chinois) et **ZoomEye** (chinois) sont des équivalents Shodan d'origine chinoise. Indexation parfois différente (couvrent mieux certaines régions). Précaution OPSEC : services chinois, requêtes potentiellement loguées par autorités. À utiliser via VPN et compte d'investigation séparé.

## 21.5 GreyNoise : filtrer le bruit Internet

**GreyNoise** (greynoise.io) catégorise le « bruit Internet » — les IPs qui scannent constamment le web. Utile pour distinguer scans massifs (bruit) versus scans ciblés (peut-être pertinent pour l'enquête).

**Cas d'usage.**

- Une IP suspecte est-elle juste du bruit ou cible-t-elle quelque chose ?
- Détecter des campagnes de scan dirigées contre une entité.

## 21.6 Have I Been Pwned (HIBP)

**HIBP** (haveibeenpwned.com) est le moteur de référence pour les breaches publiques.

**Usage OSINT.**

- Tester si un email est dans une fuite (et lesquelles).
- API gratuite pour vérification simple.
- API payante (~$3/mois) pour usage professionnel.

**Limites.**

- Liste de breaches limitée à ce que Troy Hunt accepte (filtré, vérifié).
- Pas de mots de passe en clair (uniquement existence dans fuite).
- Pour breaches plus complètes, voir DeHashed, IntelX, Snusbase.

## 21.7 Intelligence X

**Intelligence X** (intelx.io) est un moteur spécialisé dans les **deep web et leaks**.

**Capacités.**

- Index des breaches, pastes, dumps, archives Tor.
- Recherche par email, username, domaine, BTC address, IP, etc.
- Snapshots historiques (capture l'éphémère).
- API solide.

**Tarification.** Freemium très limité, professionnel à plusieurs centaines $/mois. Standard pour CTI / DFIR.

## 21.8 PublicWWW et SearchCode

**PublicWWW** (publicwww.com) indexe le **code source** des pages web — utile pour trouver toutes les pages partageant un même tracker, une même API key exposée, un même framework custom.

**SearchCode** (searchcode.com) indexe le code dans les dépôts publics (GitHub, GitLab, Bitbucket, autres).

**Cas d'usage.**

- Identifier les sites utilisant un même tracker Google Analytics (peut révéler un opérateur commun).
- Trouver des credentials exposés dans des dépôts.
- Identifier les sites partageant une signature technique.

## 21.9 GitHub search avancé

**GitHub** lui-même propose un moteur très puissant.

**Dorks GitHub.**

```
"technovert" "password"
"@technovert.fr" extension:env
"DB_PASSWORD" "delaunay"
filename:.env "technovert"
```


**Pour des leaks de secrets corporate.** Toujours à manier avec déontologie : signaler à l'organisation concernée, ne pas exploiter.

## 21.10 Moteurs académiques

**Google Scholar.** Articles académiques. Pour investigation sur parcours universitaire.

**Semantic Scholar.** Index académique enrichi IA. Citations, papers liés.

**Connected Papers.** Visualisation des relations entre papers.

**HAL, theses.fr.** France spécifique pour thèses.

## 21.11 Moteurs spécialisés divers

**Wayback Machine API** (web.archive.org). Pour rechercher dans les archives.

**Aleph (OCCRP).** Base journalistique de millions de documents publics.

**Pacer / RECAP** (US). Documents judiciaires américains.

**EDGAR** (SEC). Filings boursiers US.

**OpenSecrets** (US). Financement politique US.

## 21.12 Synthèse — votre boîte à outils

| Besoin | Outil prioritaire | Alternative |
|---|---|---|
| Infrastructure exposée | Shodan | Censys, FOFA |
| Certificats TLS | Censys + crt.sh | Shodan |
| Breaches | HIBP | DeHashed, IntelX |
| Leaks deep web | Intelligence X | Snusbase |
| Code et secrets | GitHub search | PublicWWW, SearchCode |
| Académique | Google Scholar | Semantic Scholar |
| Documents OCCRP | Aleph |  |
| Archives web | Wayback Machine | archive.today |

-----
