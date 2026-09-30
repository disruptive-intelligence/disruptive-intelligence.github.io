---
title: Chapitre 40 — Sous-domaines, IP, ASN, BGP et exposition technique
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 40.1 Au-delà du domaine principal

Le **domaine principal** (`technovert.fr`) n'est que la pointe de l'iceberg. Les organisations opèrent typiquement des dizaines à des milliers de **sous-domaines** (`intranet.technovert.fr`, `dev.technovert.fr`, `mail.technovert.fr`, `staging-eu.technovert.fr`). Identifier l'arbre complet des sous-domaines est un objectif majeur de l'investigation infrastructure.

## 40.2 Découverte de sous-domaines

**Sources passives (sans interaction avec la cible).**

- **Certificate Transparency** (crt.sh) : sous-domaines couverts par certificats émis.
- **Passive DNS** (SecurityTrails, DNSDumpster).
- **Search engines** : Google `site:technovert.fr -www`.
- **Wayback Machine** : URL historiques crawled.
- **DNS bruteforce list publics** (subdomains.txt sur GitHub).

**Sources actives (interaction modérée).**

- Bruteforce DNS (Amass, subfinder).
- ZoneTransfer (très rare, si serveur mal configuré).

**Outils combinés.**

**Amass** (OWASP). Le standard. Combine passif + actif. CLI.

```bash
amass enum -d technovert.fr -passive
amass enum -d technovert.fr -active
```


**subfinder** (ProjectDiscovery). Rapide, passif.

```bash
subfinder -d technovert.fr
```


**Sublist3r**, **assetfinder**, **findomain** : alternatives.

**Pour automatiser** : combiner les sorties (`sort -u`).

## 40.3 Sous-domaines révélateurs

Les sous-domaines révèlent :

- **Services internes** (`intranet.`, `crm.`, `erp.`, `wiki.`).
- **Environnements** (`dev.`, `staging.`, `preprod.`, `test.`).
- **Géographies** (`fr.`, `de.`, `apac.`, `us.`).
- **Filiales** (`subsidiary.`).
- **Outils tiers déployés** (`okta.`, `slack.`, `confluence.`).

Un sous-domaine `dev.api.payments.technovert.fr` révèle l'existence d'une API de paiements en développement.

## 40.4 Adresses IP : résolution et géolocalisation

Une fois les sous-domaines découverts, **résoudre en IPs** révèle l'hébergement.

**Outils.**

- `dig` : résolution DNS.
- `host`.
- **ipinfo.io**, **ipgeolocation.io** : géolocalisation et infos IP.
- **MaxMind GeoIP** : standard.

**Information par IP.**

- **Géolocalisation** : pays, ville (précision variable).
- **ASN** (Autonomous System Number) : qui possède l'IP.
- **Organization** : opérateur.
- **Hostname reverse** : nom DNS associé.
- **Services ouverts** (via Shodan, Censys).

## 40.5 ASN : Autonomous System Numbers

L'**ASN** identifie l'organisation propriétaire d'un bloc IP. Exemples :

- AS15169 : Google.
- AS16509 : Amazon AWS.
- AS13335 : Cloudflare.
- AS16276 : OVH.

**Outils.**

- **Hurricane Electric BGP** (bgp.he.net) : standard.
- **bgp.tools** (alternative moderne).
- **RIPEstat** (RIPE NCC) : Europe particulièrement.

**Cas d'usage.** Toutes les IPs de TechnoVert sont en AS16276 (OVH) → TechnoVert héberge chez OVH. Sauf si une IP est en AS13335 (Cloudflare) → utilisation Cloudflare devant.

## 40.6 BGP : routage Internet

Le **BGP** (Border Gateway Protocol) est le protocole de routage entre ASNs. Pour OSINT, peu d'usage direct (sauf cas avancés CTI), mais l'observation BGP peut révéler :

- Changements d'opérateur.
- Anomalies de routage (signal d'incident).
- Cartographie de connectivité.

## 40.7 Reverse IP : autres sites hébergés

Une **IP partagée** (typique en mutualisé) héberge potentiellement des centaines de sites. Reverse IP révèle ces sites.

**Outils.**

- **DomainTools Reverse IP** : payant.
- **ViewDNS.info reverse IP** : gratuit limité.
- **Shodan reverse**.

**Cas d'usage.** Identifier toutes les autres entités hébergées sur la même IP → peut révéler partenaires, infrastructure commune.

## 40.8 Shodan, Censys, FOFA, ZoomEye

Voir Ch.21 pour la présentation. Sur l'infrastructure d'une entité :

**Shodan dorks.**

```
hostname:technovert.fr
ssl.cert.subject.cn:technovert
org:"TechnoVert"
```


**Révèle.** Services ouverts (HTTP, SSH, FTP, RDP, RTSP, MQTT, ICS), bannières, versions, vulnérabilités connues, géographie.

## 40.9 GreyNoise et bruit Internet

**GreyNoise** filtre le « bruit » Internet (IPs qui scannent constamment).

**Cas d'usage OSINT.** Une IP suspecte qui contacte la cible : est-ce un scan opportuniste (bruit) ou un scan ciblé ? GreyNoise classe.

## 40.10 Méthodologie complète infrastructure

Pour investiguer l'infrastructure technique d'une entité :

1. **Domaine principal** (Ch.39).
2. **Sous-domaines** : Amass / subfinder passif puis actif modéré.
3. **Résolution IPs** : `dig` sur chaque sous-domaine.
4. **ASN** : Hurricane Electric, bgp.tools.
5. **Reverse IP** : autres sites hébergés.
6. **Services exposés** : Shodan + Censys.
7. **Technologies** : Wappalyzer + BuiltWith sur les sites.
8. **Cartographie** : graphe entités → domaines → sous-domaines → IPs → services.

## 40.11 Limites légales

**Scan actif (nmap, masscan).** Légalité variable selon juridiction. En France, scan modéré sans tentative d'exploitation est généralement toléré. **Scan agressif** = zone pénale (art. 323-1).

**Recommandation.** Privilégier outils passifs (Shodan, Censys agrègent des scans tiers). Scans actifs uniquement avec autorisation explicite.

-----
