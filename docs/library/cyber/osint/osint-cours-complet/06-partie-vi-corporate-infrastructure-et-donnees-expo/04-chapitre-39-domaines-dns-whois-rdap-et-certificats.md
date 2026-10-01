---
title: Chapitre 39 — Domaines, DNS, WHOIS/RDAP et certificats
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 39.1 L'infrastructure numérique comme objet d'enquête

L'**infrastructure numérique** d'une entité (domaines, serveurs, certificats, services exposés) est un terrain d'investigation OSINT majeur. Elle révèle :

- Qui possède quoi (via WHOIS, certificats).
- Comment c'est hébergé (révèle prestataires, géographie technique).
- Quelles technologies (révèle compétences, choix techniques).
- Quels services exposés (peut révéler activité).
- Liens entre entités (infrastructure partagée).

Ce chapitre couvre **domaines, DNS, WHOIS, certificats**. Le chapitre 40 couvre **sous-domaines, IP, ASN, BGP**. Le chapitre 41 couvre **surface d'attaque moderne**.

## 39.2 Le système de noms de domaine

Un **nom de domaine** (`technovert.fr`) est résolu par DNS en adresse(s) IP. Le domaine est enregistré auprès d'un **registrar** (OVH, Gandi, GoDaddy, etc.), qui transmet à un **registre** par TLD (Afnic pour `.fr`, Verisign pour `.com`).

L'enregistrement crée des informations stockées dans le **WHOIS** historiquement, et désormais le **RDAP** (Registration Data Access Protocol).

## 39.3 WHOIS : l'histoire

Le **WHOIS** historique exposait publiquement :

- Nom et email du propriétaire.
- Coordonnées du contact administratif, technique, facturation.
- Date de création et expiration.
- Registrar.
- Nameservers.

**Rupture RGPD 2018.** Depuis l'entrée en vigueur du RGPD, les registrars EU et la plupart des autres ont **masqué** les données personnelles dans le WHOIS public. Désormais, on voit typiquement « REDACTED FOR PRIVACY » ou un proxy de protection.

**Impact OSINT.** Le WHOIS direct est devenu moins utile pour l'investigation des domaines récents. Mais :

- WHOIS reste utile pour les domaines anciens (avant 2018).
- WHOIS historique conserve les enregistrements antérieurs.
- WHOIS de certaines juridictions reste partiellement ouvert.

## 39.4 RDAP : le successeur

Le **RDAP** (Registration Data Access Protocol) standardise l'accès aux données d'enregistrement. Fonctionnellement, le contenu est similaire au WHOIS (avec mêmes restrictions RGPD), mais format JSON, query HTTPS.

**Outils.**

- `rdap` CLI (linux).
- Sites RDAP : rdap.org, search.arin.net.
- API.

## 39.5 Outils WHOIS/RDAP modernes

**Sites publics.**

- **whois.icann.org** : standard.
- **DomainTools** (domaintools.com) : extensions payantes puissantes.
- **WhoIsHistory** : historique.
- **ViewDNS.info** : ensemble d'outils gratuits.
- **CentralOps**.

**CLI.**

```bash
whois technovert.fr
rdap technovert.fr
```


## 39.6 WHOIS historique : pépite OSINT

Le **WHOIS historique** (DomainTools, WhoIsHistory) conserve les enregistrements WHOIS **antérieurs à 2018**. Pour les domaines créés avant cette date, on peut souvent retrouver le propriétaire originel.

**Cas d'usage.** Un domaine `delaunay-patrimoine.fr` créé en 2017 (avant RGPD) → WHOIS historique peut révéler email et coordonnées du propriétaire à cette époque.

**Outils.**

- **DomainTools Historical WHOIS** (payant, ~$95/mois).
- **WhoIsHistory** (alternative moins riche).
- **WHOISology** (commercial).

C'est l'un des cas où l'investissement dans un outil payant se justifie.

## 39.7 DNS : enregistrements

Le **DNS** (Domain Name System) résout les noms en IPs et fournit d'autres informations via différents types d'enregistrements.

**Types d'enregistrements clés.**

- **A** : IPv4.
- **AAAA** : IPv6.
- **MX** : serveurs mail.
- **NS** : nameservers (DNS).
- **TXT** : texte libre (souvent SPF, DKIM, vérifications domaines tiers).
- **CNAME** : alias.
- **SOA** : autorité.

**Outils.**

- `dig` (CLI Linux/Mac).
- `nslookup` (multi-OS).
- **DNSDumpster** (dnsdumpster.com) : analyse rapide.
- **SecurityTrails** (securitytrails.com) : historique DNS riche, payant.
- **ViewDNS.info**.

```bash
dig technovert.fr ANY
dig technovert.fr MX
dig _dmarc.technovert.fr TXT
```


## 39.8 DNS records révélateurs

**MX records.** Révèlent le fournisseur email (Google Workspace, Microsoft 365, OVH, etc.).

**TXT records.** Souvent contiennent :

- SPF (qui peut envoyer email depuis ce domaine).
- DKIM (signature).
- Vérifications domaines tiers (Google Site verification, Atlassian, Office 365, Adobe, Stripe, etc.) → révèle quels services tiers sont utilisés.

**NS records.** Révèlent l'opérateur DNS (Cloudflare, OVH, AWS Route 53). Cohérence avec hébergement supposé.

**Exemple révélateur.**

```
technovert.fr TXT "google-site-verification=abc..."
technovert.fr TXT "atlassian-domain-verification=xyz..."
technovert.fr TXT "stripe-verification=def..."
```

→ TechnoVert utilise Google, Atlassian (Jira/Confluence), Stripe.

## 39.9 Passive DNS

Le **passive DNS** archive l'historique des résolutions DNS observées. Permet de voir l'évolution d'un domaine.

**Cas d'usage.**

- Un domaine pointait vers IP X en 2020, vers IP Y en 2024 → évolution d'hébergement.
- Sous-domaine ayant existé puis disparu.
- Reconstruction d'infrastructure ancienne.

**Outils.**

- **SecurityTrails** : historique passive DNS riche.
- **PassiveTotal / RiskIQ** (Microsoft).
- **Farsight DNSDB** (industrie référence).
- **DNSDumpster** (limité gratuit).
- **CIRCL Passive DNS** (CERT.lu, accès gratuit chercheurs).

## 39.10 Certificats TLS : pépite moderne

Les **certificats TLS/SSL** sont émis pour authentifier les sites HTTPS. Leur **transparence (Certificate Transparency, CT)** depuis 2018 a créé une mine OSINT majeure.

**Principe CT.** Chaque émission de certificat est loguée publiquement dans des logs CT (Google, Cloudflare, Let's Encrypt, etc.). Ces logs sont consultables.

**Ce qui est exposé.**

- Le **domaine principal** (Common Name CN).
- Les **Subject Alternative Names (SAN)** — domaines alternatifs couverts par le même certificat. Peut révéler des dizaines de domaines liés.
- Date d'émission, expiration, autorité émettrice.
- Empreinte du certificat (peut être utilisée pour corrélations cross-domaines).

**Outils.**

- **crt.sh** (crt.sh) : interface publique sur les logs CT. Gratuit, puissant.
- **Censys** : recherche avancée par certificats.
- **Shodan** : intègre certificats.

```
# Recherche crt.sh
crt.sh?q=technovert.fr
crt.sh?q=%25.technovert.fr   # tous les sous-domaines
```


**Cas d'usage.** Si TechnoVert a émis un certificat couvrant `technovert.fr` + `intranet.technovert.fr` + `dev.technovert.fr` + `staging.technovert.fr`, ces sous-domaines sont **révélés** même s'ils ne sont pas accessibles publiquement.

## 39.11 Pivot infrastructure → autres domaines

Un même propriétaire opère souvent plusieurs domaines. Les pivots :

**Email WHOIS commun.** Si deux domaines ont le même email administrateur (visible si pre-2018), ils sont liés.

**Nameservers communs.** Pas un signal fort (beaucoup de domaines partagent OVH ou Cloudflare), mais NS très spécifique peut être discriminant.

**SOA email commun** : email administratif technique dans le SOA record.

**Certificats partagés** : un certificat couvrant plusieurs domaines révèle relation.

**Hostings communs** (IP/ASN partagés — Ch.40).

**Trackers / analytics communs** : code Google Analytics, Facebook Pixel, Mixpanel partagé entre sites = signal fort de propriété commune.

**Outils trackers.**

- **DNSlytics** (dnslytics.com) : reverse Google Analytics, AdSense.
- **SpyOnWeb**.
- **NerdyData**.

## 39.12 Méthodologie complète domaine

Pour investiguer un domaine cible :

1. **WHOIS actuel** : minimal (RGPD).
2. **WHOIS historique** : DomainTools si pre-2018.
3. **DNS records** : A, MX, NS, TXT, SOA, etc.
4. **Passive DNS** : historique résolutions.
5. **Certificats TLS** : crt.sh pour SAN et sous-domaines.
6. **Trackers analytics** : DNSlytics pour cross-références.
7. **Sous-domaines** : voir Ch.40.
8. **Capture web** : archive.org + archive.today pour contenu historique.
9. **Technologies** : Wappalyzer, BuiltWith.
10. **Pivot** : domaines liés via mêmes traits.

> **MIRAGE — Épisode 9 : Infrastructure web et domaines**
>
> L'analyste investigue l'infrastructure web de la campagne de désinformation.
>
> **Domaine `verites-technovert.com`.** WHOIS actuel : masqué RGPD. WHOIS historique (DomainTools) : créé 12 octobre 2025, registrar Namecheap, email contact `proxy@withheldforprivacy.com` (masqué). DNS : NS Namecheap default, hébergement Cloudflare (IP origine masquée). MX : aucun mail handler configuré.
>
> **Certificat TLS** (crt.sh). Recherche : un certificat Let's Encrypt émis le 12 octobre 2025 couvre `verites-technovert.com` + `www.verites-technovert.com`. Pas de SAN révélateur d'autres domaines liés.
>
> **Trackers analytics.** Le site utilise Google Analytics avec un Property ID identifié. DNSlytics : reverse search sur ce GA ID → un autre site utilise le même : `info-finance-eu.com`. **Pivot critique** : les deux sites de désinformation sont liés par la même Property GA, donc opérés très probablement par le même opérateur.
>
> **Domaine `info-finance-eu.com`.** WHOIS historique : créé 18 octobre 2025 (6 jours après verites-technovert.com). Registrar Namecheap (identique). Email contact masqué. Trackers identiques. NS et hébergement Cloudflare.
>
> **Hypothèse confortée.** Les deux domaines sont opérés par le même opérateur, créés à 6 jours d'intervalle, utilisant la même stack technique. Cluster de désinformation confirmé.
>
> **Recherche complémentaire** : `crt.sh?q=verites-technovert.com` et `crt.sh?q=info-finance-eu.com` ne révèlent pas d'autres certificats liés (l'opérateur a évité de mutualiser).
>
> **Pivot suivant** : analyser le contenu publié sur les deux sites, archiver immédiatement (anticipation de retrait), identifier qui contribue (auteurs déclarés ? métadonnées documents ?), identifier les autres canaux d'amplification (cluster X de 8 comptes, canaux Telegram).
>
> **Cotation cluster désinformation.** Existence confirmée A1 (sites observables). Lien entre les deux sites : B1 (GA partagé + cohérences temporelles et techniques). Lien au commanditaire (Delaunay ou son entourage) : à confirmer (pas encore de pivot direct vers Delaunay).

-----
