---
title: Annexe D — Cheat sheets techniques
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Annexes
  - index.md
---

## Commandes blockchain (Bitcoin via CLI/API)

```
# Explorer un wallet via OXT.me (interface web)
https://oxt.me/address/[ADRESSE_BTC]

# Explorer une transaction
https://oxt.me/transaction/[TXID]

# Vérifier un wallet Ethereum via Etherscan
https://etherscan.io/address/[ADRESSE_ETH]

# Arkham Intelligence (freemium, attribution avancée)
https://platform.arkhamintelligence.com/explorer/address/[ADRESSE]
```


## Requêtes d'infrastructure (identification de bulletproof hosting)

```bash
# WHOIS d'un domaine
whois [DOMAINE]

# WHOIS historique (nécessite DomainTools ou SecurityTrails)
# Via DomainTools API :
curl "https://api.domaintools.com/v1/[DOMAINE]/whois/history"

# Reverse IP (domaines sur la même IP)
# Via SecurityTrails :
curl "https://api.securitytrails.com/v1/ips/nearby/[IP]"

# Certificate Transparency (certificats émis pour un domaine)
# Via crt.sh :
curl "https://crt.sh/?q=%25.[DOMAINE]&output=json"

# Shodan (services exposés sur une IP)
shodan host [IP]

# Censys (alternative à Shodan)
censys search "[IP]"

# Vérifier la réputation d'une IP
# AbuseIPDB :
curl "https://api.abuseipdb.com/api/v2/check?ipAddress=[IP]"
```


## Requêtes Maltego (transforms clés pour la cartographie)

| Objectif | Transform recommandée | Source |
|----------|----------------------|--------|
| Enrichir un domaine | DNS → IP, WHOIS, Subdomains | Standard |
| Reverse IP | IP → Domaines co-hébergés | SecurityTrails |
| Certificats | Domaine → Certificats CT | crt.sh |
| Réputation hash | Hash → VirusTotal reports | VirusTotal |
| Recherche de pseudo | Pseudo → Profils sociaux | Sherlock/OSINT |
| Enrichissement email | Email → Breaches, domaines | DeHashed, HIBP |
| Analyse wallet | Wallet → Transactions, clusters | OXT.me, Chainalysis |

## Outils OSINT — Aide-mémoire

| Besoin | Outil | Gratuit/Payant | URL |
|--------|-------|---------------|-----|
| WHOIS historique | DomainTools | Payant | domaintools.com |
| WHOIS historique | SecurityTrails | Freemium | securitytrails.com |
| Certificate Transparency | crt.sh | Gratuit | crt.sh |
| Recherche de pseudo | Sherlock | Gratuit (OSS) | github.com/sherlock-project |
| Recherche de pseudo | WhatsMyName | Gratuit (OSS) | whatsmyname.app |
| Breaches | DeHashed | Payant | dehashed.com |
| Breaches | Have I Been Pwned | Gratuit (limité) | haveibeenpwned.com |
| Breaches | IntelX | Freemium | intelx.io |
| Scan de ports | Shodan | Freemium | shodan.io |
| Scan de ports | Censys | Freemium | search.censys.io |
| Blockchain Bitcoin | OXT.me | Gratuit | oxt.me |
| Blockchain Ethereum | Etherscan | Gratuit | etherscan.io |
| Blockchain attribution | Arkham Intelligence | Freemium | arkhamintelligence.com |
| Blockchain forensics | Chainalysis Reactor | Payant (institutions) | chainalysis.com |
| Blockchain forensics | TRM Labs | Payant | trmlabs.com |
| Blockchain forensics | Crystal Intelligence | Payant | crystalintelligence.com |
| Analyse de réseau | Gephi | Gratuit (OSS) | gephi.org |
| Cartographie relationnelle | Maltego | Freemium | maltego.com |
| Notes liées | Obsidian | Gratuit (personnel) | obsidian.md |
| Analyse formelle | i2 Analyst's Notebook | Payant (institutionnel) | ibm.com |
| Graphes simples | yEd | Gratuit | yworks.com |
| Monitoring dark web | Flare | Payant | flare.io |
| Monitoring forums | Recorded Future | Payant | recordedfuture.com |

---
