---
title: 'Chapitre 19 — Pile réseau : ce que voit chaque acteur'
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 5 — Réseau, anonymat et navigation web
  - index.md
---

## 19.1 Anatomie d’une requête web

Tu tapes `https://example.org` dans ton navigateur. Voilà ce qui se passe, et ce qui fuit à chaque étape :

1. **Résolution DNS** : ton OS demande à un résolveur DNS l’adresse IP de `example.org`. Sans DNS chiffré, cette requête est en clair sur le réseau local et le FAI voit le nom de domaine.
1. **Établissement TCP** : connexion à l’IP du serveur. Visible : IP source, IP destination.
1. **Négociation TLS** : ton navigateur envoie un *ClientHello* contenant, entre autres, le **SNI** (Server Name Indication) — c’est-à-dire le nom de domaine que tu joins, *en clair*, même si tu utilises HTTPS. C’est pour permettre à un serveur hébergeant plusieurs sites de savoir lequel servir.
1. **Échange chiffré** : à partir de là, contenu chiffré.

Conséquence : même en HTTPS, ton FAI sait **quel site tu visites** (via DNS et SNI), juste pas *ce que tu fais* sur ce site.

## 19.2 DNS en clair : mouchard universel

Le DNS classique (port 53, UDP) est en clair. Toute personne sur le chemin (FAI, opérateur Wi-Fi, employeur sur réseau d’entreprise) voit chaque résolution. C’est trivial à intercepter, à enregistrer, à monétiser, à censurer.

## 19.3 DoH, DoT, DNSCrypt, DNSSEC

Trois protocoles modernes de DNS chiffré :

- **DoH (DNS over HTTPS)** : DNS dans des requêtes HTTPS. Avantage : indiscernable du trafic HTTPS normal, contournement de certains blocages. Inconvénient : nécessite un résolveur DoH configurable, parfois géré par un acteur centralisé (Cloudflare 1.1.1.1, Google 8.8.8.8, Quad9, NextDNS, Mullvad DNS).
- **DoT (DNS over TLS)** : DNS dans une connexion TLS dédiée sur port 853. Détectable comme « DNS chiffré » (donc bloquable spécifiquement) mais propre techniquement.
- **DNSCrypt** : alternative open source plus ancienne, support variable.
- **DNSSEC** : signe cryptographiquement les réponses DNS pour vérifier leur intégrité (pas leur confidentialité). Complémentaire, pas substitut.

**Choix du résolveur** : Cloudflare est rapide et propose des audits, mais centralise massivement. **Quad9** (Suisse) ou **Mullvad DNS** sont des alternatives plus respectueuses. **NextDNS** offre filtrage personnalisable. Self-hosting d’un résolveur DoH (sur ton propre serveur via Pi-hole + Unbound) est l’option maximale pour qui peut.

## 19.4 SNI et ECH

Même avec DNS chiffré, le **SNI** trahit ta destination. Le **ECH (Encrypted Client Hello)** chiffre le SNI dans le ClientHello TLS, en s’appuyant sur une clé publique du serveur récupérée via DNS (typiquement via un enregistrement HTTPS / SVCB).

**État du déploiement (2025-2026)** :

- Côté client : Firefox supporte ECH depuis la version 118 (active par défaut depuis fin 2023 quand le serveur le supporte). Chrome supporte ECH derrière flag. Safari supporte partiellement. Tor Browser inclut ECH.
- Côté serveur : Cloudflare a activé ECH par défaut pour ses clients en 2023 ; Fastly et certains autres CDN ont suivi. Le déploiement reste partiel pour le web non-CDN.
- Effet réel : ECH ne fonctionne que si *les deux extrémités* le supportent **et** si le résolveur DNS retourne les enregistrements HTTPS contenant la clé ECH. Sans DNS chiffré (DoH/DoT), l’enregistrement HTTPS lui-même peut être altéré par un attaquant sur le chemin, désactivant ECH.

**Bonne pratique** : activer ECH dans le navigateur, utiliser un résolveur DoH qui supporte les enregistrements HTTPS (Cloudflare 1.1.1.1, NextDNS, Mullvad DNS), comprendre que le bénéfice réel dépend des sites visités.

## 19.5 QUIC et HTTP/3

**QUIC** est un protocole de transport conçu par Google et standardisé par l’IETF (RFC 9000+) en 2021. Il remplace TCP+TLS pour les nouveaux usages : intégration native du chiffrement TLS 1.3, établissement de connexion en 1-RTT (voire 0-RTT), multiplexage sans head-of-line blocking, migration de connexion sans rupture (utile pour mobile en bascule Wi-Fi → 4G).

**HTTP/3** est HTTP au-dessus de QUIC. Adopté par Cloudflare, Google, Facebook, Akamai. Représente une part croissante du trafic web (≈ 30 % du trafic des grands sites en 2025).

**Implications privacy** :

- **Plus difficile à observer en surface** que TCP/TLS classique : QUIC chiffre une partie des en-têtes de transport, pas seulement l’application.
- **Fingerprint** : QUIC introduit un nouveau vecteur de fingerprinting (paramètres de connexion, comportement). JA4 est l’évolution de JA3 qui couvre QUIC.
- **Blocage par DPI** : QUIC en UDP/443 est plus difficile à classifier que TCP/443. Certains États (Russie, Iran) ont périodiquement bloqué UDP/443 dans son ensemble.
- **Pour les VPN** : WireGuard est en UDP par nature ; ECH+QUIC complète le tableau de protocoles modernes.

## 19.6 Fuites IP : WebRTC, IPv6, captive portals

- **WebRTC** : protocole de communication temps réel (visio, voix) qui peut révéler ton IP réelle même derrière un VPN, parce qu’il négocie des connexions P2P. À désactiver ou contrôler dans le navigateur.
- **IPv6 mal géré** : ton VPN tunnelise peut-être seulement IPv4 ; les requêtes IPv6 contournent le tunnel. À tester. À forcer IPv4-only si le VPN ne gère pas bien IPv6.
- **Captive portals** (Wi-Fi hôtel, café) : le navigateur tente de joindre des URLs de test pour détecter le portail. Ces requêtes révèlent ta présence avant que tu sois authentifié.
- **mDNS** (multicast DNS) : annonce des services locaux. Peut fuiter le nom de ton machine sur le réseau local.

## 19.7 Ce que voit chacun

|Acteur                 |Voit                                                                    |Ne voit pas                              |
|-----------------------|------------------------------------------------------------------------|-----------------------------------------|
|**FAI** (sans VPN)     |IP, DNS (sauf DoH), SNI (sauf ECH), métadonnées (volumes, timing)       |Contenu HTTPS                            |
|**VPN**                |IP source réelle, IP destination, SNI (sauf ECH), métadonnées           |Contenu HTTPS                            |
|**Site visité**        |IP source (FAI ou VPN), User-Agent, fingerprint, cookies, contenu envoyé|Identité réelle si pas de compte connecté|
|**App mobile**         |Tout ce qu’elle demande comme permission + traffic                      |(selon permissions)                      |
|**Réseau Wi-Fi public**|Mêmes choses que FAI, sur ton trafic clair                              |Contenu HTTPS                            |

> 🟧 **Évolution récente : l’opérateur comme acteur AdTech**
> 
> Les opérateurs télécoms ne sont pas seulement des transporteurs de trafic. Avec des initiatives comme Utiq, certains opérateurs européens cherchent à valoriser leur position dans l’infrastructure réseau pour proposer des identifiants publicitaires post-cookie. Cela ne signifie pas que l’opérateur lit le contenu HTTPS, mais cela rappelle qu’il dispose d’une position privilégiée : relation contractuelle avec l’abonné, attribution d’IP, connaissance du réseau d’accès, signaux mobiles, et capacité à participer à des mécanismes d’identification publicitaire sous consentement.

Cette table cadre toutes les décisions des chapitres suivants.

## 19.8 Corrélation par horaires, volumes, destinations

Au-delà des contenus, l’analyse statistique des métadonnées révèle énormément :

- Tu te connectes tous les jeudis à 22h à un même service (timing + destination = profil de comportement).
- Tu envoies un gros volume juste après avoir reçu un message (corrélation conversation/envoi).
- Tu ouvres une session de 3 heures sur Wikipedia (intérêt approfondi sur un sujet).

Cette analyse est faite à l’échelle massive par les FAI et les agences. Elle est à la base de la « surveillance par métadonnées » (cf. Ch 1).

## 19.9 Outils de diagnostic

- **dnsleaktest.com** : vérifie que tes requêtes DNS passent par où tu crois.
- **browserleaks.com** : audit complet (WebRTC, IPv6, fonts, canvas, etc.).
- **ipleak.net** : autre référence.
- **AmIUnique.org** : mesure le caractère unique de ton fingerprint navigateur (cf. Ch 23).
- **dnscheck.tools** (Mullvad) : utile pour valider config.

À tester systématiquement après installation d’un VPN, d’un navigateur, d’une config DNS.

-----
