---
title: 'Chapitre 20 — VPN : utilité réelle, limites, choix'
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 5 — Réseau, anonymat et navigation web
  - index.md
---

## 20.1 Ce qu’un VPN fait vraiment

Un VPN établit un tunnel chiffré entre toi et un serveur distant. Tout ton trafic transite par ce tunnel. Du point de vue des sites distants, ton IP est celle du serveur VPN. Du point de vue de ton FAI, il ne voit qu’une connexion chiffrée vers le VPN.

**Effet net** : tu **déplaces** la confiance du FAI au fournisseur VPN. Tu ne supprimes pas la confiance, tu la transfères.

## 20.2 Ce qu’un VPN ne fait pas

- **Il n’anonymise pas**. Si tu te connectes à ton compte Gmail via VPN, Google sait toujours qui tu es.
- **Il ne chiffre pas tes données chez les services**. Le contenu envoyé à un service distant est en clair pour ce service.
- **Il ne te protège pas contre le fingerprinting** (cf. Ch 23). Le navigateur reste identifiable.
- **Il ne te protège pas contre un malware sur ton appareil**.

## 20.3 Critères de choix

1. **Juridiction** : siège du fournisseur. Suisse, Suède, Panama sont préférables aux US (Patriot Act), au RU (RIPA), à la France (lois antiterrorisme).
1. **No-logs prouvés** : politique no-logs vérifiée par audit indépendant *et*, idéalement, par contraintes judiciaires passées où le fournisseur n’a rien pu fournir. Mullvad et IVPN ont des historiques solides.
1. **Audits indépendants** : Cure53, Radically Open Security, etc. Récents (annuels).
1. **Paiement** : possibilité de paiement anonyme (cash par courrier pour Mullvad, Monero pour certains).
1. **Killswitch** : interruption du trafic si le tunnel tombe. Indispensable.
1. **Leak protection** : protection contre fuites IPv6, DNS, WebRTC.

## 20.4 Trois familles à ne pas confondre

VPN privacy, mixnet, VPN anti-censure

Tous les outils présentés comme des « VPN privacy » ne répondent pas au même besoin. Avant de comparer des services comme Mullvad, Proton VPN, NymVPN ou AmneziaVPN, il faut distinguer les grandes familles fonctionnelles.

Un VPN ne doit pas être choisi parce qu’il est dans une liste de « meilleurs VPN », mais parce qu’il correspond au problème opérationnel à résoudre : cacher son trafic à son FAI, réduire son exposition sur Wi-Fi public, éviter le tracking IP, contourner la censure, réduire les métadonnées, ou créer une infrastructure personnelle.

## 20.4.1 Les VPN privacy classiques

Les VPN privacy classiques sont les VPN au sens le plus courant : ils créent un tunnel chiffré entre l’utilisateur et un serveur VPN. Le FAI ne voit plus les destinations finales ; les sites visités voient l’adresse IP du serveur VPN au lieu de l’adresse IP réelle de l’utilisateur.

Leur intérêt principal est de **déplacer la confiance** du FAI vers un fournisseur VPN considéré comme plus fiable. Ils sont utiles pour :

- réduire l’exposition au FAI ;
- sécuriser une connexion sur Wi-Fi public ;
- masquer son IP réelle aux sites consultés ;
- compartimenter certains usages réseau ;
- limiter certains blocages géographiques ou filtrages simples.

Mais ils ne rendent pas anonyme. Si l’utilisateur se connecte à son compte Google, Apple, Facebook, bancaire ou professionnel, le service sait toujours qui il est. Le VPN protège la couche réseau, pas l’identité applicative.

Dans cette famille, on peut distinguer deux sous-profils :

**VPN privacy minimalistes** : Mullvad, IVPN.  
Ils privilégient la minimisation de données, l’absence de compte nominatif, les audits, la simplicité et la cohérence OPSEC. Mullvad est l’exemple typique : compte numéroté, pas d’email nécessaire, paiement possible en cash ou Monero, politique de logs très restrictive.

**VPN privacy grand public / écosystème** : Proton VPN.  
Proton VPN est solide, suisse, audité, confortable et bien intégré à l’écosystème Proton. Il est très pertinent pour un usage général privacy + confort, mais il est moins minimaliste qu’un service comme Mullvad, notamment parce qu’il s’inscrit dans un écosystème plus large : Proton Mail, Proton Drive, Proton Pass, Proton Calendar.

**Usage recommandé** : privacy quotidienne, Wi-Fi public, navigation classique, réduction de l’exposition au FAI.

**Limite principale** : le VPN voit techniquement une partie de ce que le FAI ne voit plus. Le problème de confiance est déplacé, pas supprimé.

## 20.4.2 Les réseaux orientés métadonnées et mixnet

Cette famille répond à un problème plus avancé : les métadonnées réseau.

Même lorsqu’un trafic est chiffré, il laisse des traces : horaires de connexion, volumes de données, régularité, durée des sessions, taille des paquets, points d’entrée et de sortie. Un adversaire capable d’observer ces signaux peut parfois corréler deux activités sans lire le contenu.

Les mixnets cherchent à réduire cette corrélation en mélangeant les flux, en ajoutant de la latence, en multipliant les sauts et parfois en ajoutant du bruit réseau. L’objectif n’est pas seulement de cacher l’IP, mais de rendre plus difficile l’analyse du trafic.

**NymVPN** appartient à cette logique. Il propose un mode rapide en deux sauts et un mode anonyme en cinq sauts via le mixnet Nym. Le mode anonyme vise à réduire la corrélation par métadonnées, au prix d’une latence plus importante.

Ce type d’outil est pertinent pour :

- des recherches sensibles ;
- des communications où les métadonnées comptent autant que le contenu ;
- des usages crypto ou financiers où la corrélation réseau est problématique ;
- des profils exposés qui veulent tester une couche supplémentaire contre l’analyse de trafic.

**Usage recommandé** : protection avancée contre la corrélation de métadonnées.

**Limite principale** : plus de complexité, plus de latence, moins de maturité qu’un VPN centralisé classique. Ce n’est pas forcément le meilleur choix pour le quotidien, le streaming ou les téléchargements lourds.

## 20.4.3 Les VPN anti-censure et protocoles obfusqués

Cette famille répond à un autre problème : non pas « qui voit mon IP ? », mais « est-ce que mon trafic VPN est détecté ou bloqué ? ».

Dans certains pays ou réseaux, les VPN classiques sont détectés par DPI, blocage IP, blocage protocolaire ou active probing. WireGuard et OpenVPN peuvent être bloqués ou fortement ralentis. Dans ce contexte, le besoin prioritaire est de **masquer la signature du VPN** pour le faire ressembler à du trafic web ordinaire ou difficilement classifiable.

**AmneziaVPN** est particulièrement pertinent dans cette famille. Il permet d’utiliser plusieurs protocoles orientés anti-censure, notamment AmneziaWG, XRay Reality, Shadowsocks et OpenVPN over Cloak.

- **AmneziaWG** est une variante de WireGuard conçue pour rendre le trafic plus difficile à identifier par DPI.
- **XRay Reality** vise à mieux résister à la détection et à l’active probing dans les pays à forte censure.
- **Shadowsocks** est un proxy chiffré largement utilisé dans les environnements censurés.
- **OpenVPN over Cloak** ajoute une couche d’obfuscation pour masquer OpenVPN.

Ce type d’outil est pertinent pour :

- pays censurés ;
- réseaux universitaires ou professionnels filtrants ;
- blocage de VPN classiques ;
- contournement de DPI ;
- préparation de voyage en environnement restrictif.

**Usage recommandé** : anti-censure, contournement réseau, résilience en pays restrictif.

**Limite principale** : l’anti-censure n’est pas l’anonymat. Un outil qui contourne le blocage VPN ne garantit pas que l’utilisateur soit anonyme.

## 20.4.4 Les VPN self-hosted

Le self-host consiste à déployer son propre serveur VPN sur un VPS ou une machine personnelle. L’intérêt est de ne pas dépendre directement d’un fournisseur VPN commercial pour l’infrastructure.

**AmneziaVPN** est aussi pertinent ici, car il facilite la création d’un VPN personnel sur un VPS avec plusieurs protocoles.

Le self-host peut être intéressant pour :

- avoir un serveur personnel stable ;
- contourner certains blocages ;
- maîtriser la configuration ;
- créer un accès privé à ses ressources ;
- fournir un accès VPN à quelques personnes de confiance.

Mais il faut comprendre la limite OPSEC : en self-host, l’adresse IP de sortie est souvent beaucoup plus unique qu’une IP Mullvad, Proton ou IVPN partagée par de nombreux utilisateurs. L’utilisateur ne se fond donc pas dans une grande foule. De plus, la confiance est déplacée vers le fournisseur VPS.

**Usage recommandé** : infrastructure personnelle, contournement, accès privé, usages techniques.

**Limite principale** : moins bon pour se fondre dans la masse ; confiance déplacée vers l’hébergeur VPS.

## 20.4.5 Les réseaux d’anonymat : Tor, Whonix, Tails

Tor, Whonix et Tails ne doivent pas être classés comme de simples VPN. Ils appartiennent à une autre famille : les réseaux et environnements d’anonymat.

**Tor** route le trafic à travers plusieurs relais et permet l’accès aux services onion.  
**Whonix** force le trafic d’une machine de travail à passer par une passerelle Tor.  
**Tails** fournit un système live amnésique qui route tout via Tor.

Ces outils sont plus adaptés aux usages où l’anonymat réseau est prioritaire : contact source, SecureDrop, OnionShare, publication pseudonyme, session sensible ponctuelle.

**Usage recommandé** : anonymat réseau, services onion, journalisme sensible, lanceurs d’alerte.

**Limite principale** : latence, friction, risque de mauvaise OPSEC. Tor ne protège pas contre une connexion à un compte nominatif, un navigateur mal utilisé ou une erreur comportementale.

## 20.4.6 Règle finale

Un VPN privacy classique protège surtout contre le FAI, les réseaux locaux et l’exposition IP.  
Un mixnet cherche à réduire l’analyse des métadonnées.  
Un VPN anti-censure cherche à passer à travers des réseaux hostiles.  
Un self-host donne du contrôle, mais réduit souvent l’anonymat par la foule.  
Tor, Whonix et Tails restent les références pour l’anonymat réseau structuré.

Le bon choix n’est donc pas « quel est le meilleur VPN ? », mais : **quel problème réseau est-ce que je cherche à résoudre ?**

## 20.5 Acteurs principaux (2025-2026)

- **Mullvad** : référence privacy. Suède. VPN privacy classique, centralisé, mais très minimaliste : compte numéroté sans email, paiement possible en cash ou Monero, politique no-log détaillée, orientation forte vers la minimisation de données. C’est un bon choix de base pour réduire la visibilité du FAI, éviter l’exposition de son IP réelle aux sites, sécuriser les réseaux Wi-Fi publics et compartimenter des usages.
- **IVPN** : Gibraltar. Audits Cure53. Très privacy-friendly. Tier business pour multi-appareils.
- **Proton VPN** : Suisse, opéré par Proton. Bonne réputation, intégration avec l’écosystème Proton. Plan gratuit existant.
- **NymVPN** : service plus récent et conceptuellement différent d’un VPN classique. NymVPN propose un mode **Fast** en deux sauts, basé sur une architecture décentralisée et AmneziaWG, et un mode **Anonymous** en cinq sauts via le mixnet Nym avec ajout de bruit. À classer comme outil de réduction des métadonnées et de corrélation, davantage que comme simple VPN de confort. Bon candidat pour profils exposés qui veulent tester une approche plus robuste contre l’analyse de trafic, mais à manier avec prudence : réseau plus jeune, latence plus forte en mode anonymous, et modèle plus complexe qu’un VPN centralisé mature.
- **AmneziaVPN** : outil hybride : client open source multi-protocoles, service Premium, et surtout solution de self-hosting VPN. Surtout pertinent dans les contextes de censure, de filtrage ou de DPI agressif. Il permet soit d’utiliser une offre VPN classique, soit de déployer son propre VPN sur un serveur VPS, avec des protocoles comme AmneziaWG, XRay Reality, Shadowsocks ou OpenVPN over Cloak. Son intérêt principal n’est pas l’anonymat par foule d’utilisateurs, mais la capacité à contourner des blocages et à masquer la signature du trafic VPN. Moins adapté comme « VPN privacy puriste » si utilisé en self-host : l’utilisateur déplace alors la confiance vers son fournisseur VPS, et son IP de sortie peut être beaucoup plus unique qu’une IP partagée par des milliers d’utilisateurs chez un gros fournisseur. À privilégier pour voyage en pays restrictif, filtrage réseau, DPI, ou besoin de serveur VPN personnel.
- **NordVPN, ExpressVPN, Surfshark** : grands acteurs commerciaux. Marketing privacy mais à examiner par juridiction et structure de propriété.
  - **ExpressVPN** a rejoint **Kape Technologies** en 2021 (Kape opérant aussi CyberGhost, Private Internet Access et Zenmate, et historiquement associé à des activités contestées d’adware au début des années 2010, depuis une réorganisation et un changement de direction).
  - **NordVPN** et **Surfshark** ont annoncé en 2022 une fusion opérationnelle au sein du groupe Nord Security, tout en restant commercialisés comme deux marques distinctes avec des audits séparés.
  - Ces fournisseurs restent acceptables pour des cas d’usage simples (contournement géographique, protection sur Wi-Fi public). Pour les profils sensibles ou HVT, les acteurs spécifiquement focalisés privacy (Mullvad, IVPN, Proton VPN) sont préférables en raison de juridiction, ancienneté de l’engagement privacy et historique d’audits ciblés.
- **VPN gratuits** : presque toujours pires que rien. Modèles économiques typiquement basés sur la revente de données ou l’insertion d’ads.

## 20.6 Protocoles : WireGuard vs OpenVPN

- **WireGuard** : moderne, rapide, code compact (< 4000 lignes), cryptographie up-to-date. Adopté en standard par la plupart des fournisseurs. Limite historique : IPs statiques par client (donc moins anonyme structurellement) — résolu par les fournisseurs sérieux qui rotationnent.
- **OpenVPN** : éprouvé, lent comparativement, complexe à auditer. Reste utile pour contourner certaines détections (TCP 443 indistinguable de HTTPS).
- **Shadowsocks, V2Ray, autres protocoles obfusqués** : pour contourner DPI agressifs (Chine, Iran). À combiner avec VPN ou Tor.
- **AmneziaWG** : fork de WireGuard conçu pour rendre le trafic VPN plus difficile à détecter par des systèmes de DPI. AmneziaWG ajoute des mécanismes d’obfuscation autour de la négociation et du profil réseau, afin que le trafic ressemble moins à du WireGuard standard. Ce n’est pas une garantie d’invisibilité, mais c’est une réponse pratique au blocage de WireGuard dans certains environnements censurés.
- **XRay Reality / VLESS Reality** : famille de protocoles utilisée dans les contextes de contournement de censure. Le principe est de rendre le trafic plus proche d’un trafic TLS web classique, avec résistance à l’active probing. C’est utile dans les pays où les censeurs testent activement les serveurs suspects pour déterminer s’ils hébergent un proxy ou un VPN.
- **OpenVPN over Cloak** : combinaison d’OpenVPN et d’un plugin d’obfuscation. Cloak masque le trafic VPN comme du trafic web et peut présenter une fausse façade en cas de probing non autorisé. Plus lourd qu’un WireGuard classique, mais pertinent dans des environnements où la simple utilisation d’un VPN est détectée ou bloquée.

## 20.7 Configuration

- **Killswitch activé** systématiquement.
- **Leak protection** : DNS, IPv6, WebRTC.
- **Multihop** (chaînage de deux serveurs) si threat model l’exige : Mullvad et IVPN proposent. Coût en latence et débit.
- **Split tunneling** : certaines apps hors VPN, d’autres dans. Utile pour banque qui bloque les IPs VPN.

## 20.8 Erreurs fréquentes

- **VPN + comptes nominaux** : ton VPN cache ton IP, mais ton compte Facebook révèle qui tu es. Pour des actions sensibles, séparer.
- **VPN « gratuits »** : risque très supérieur au bénéfice.
- **Compter sur le VPN seul pour la confidentialité** : sans navigateur durci, sans hygiène applicative, le VPN est un placebo coûteux.
- **VPN d’entreprise pour activité personnelle sensible** : ton employeur voit tout ce que voyait ton FAI avant. Pire.

## 20.9 Matrice de décision rapide

| Besoin principal                      | Famille pertinente                      | Exemples                                    |
| ------------------------------------- | --------------------------------------- | ------------------------------------------- |
| Réduire l’exposition au FAI           | VPN privacy classique                   | Mullvad, IVPN, Proton VPN                   |
| Privacy quotidienne minimaliste       | VPN privacy minimaliste                 | Mullvad, IVPN                               |
| Privacy + confort + écosystème        | VPN privacy grand public                | Proton VPN                                  |
| Réduction des métadonnées réseau      | Mixnet / réseau orienté métadonnées     | NymVPN                                      |
| Pays censuré / DPI agressif           | VPN anti-censure / obfuscation          | AmneziaVPN, AmneziaWG, XRay Reality         |
| VPN personnel sur VPS                 | VPN self-hosted                         | AmneziaVPN self-hosted                      |
| Session source / journalisme sensible | Réseau d’anonymat / environnement isolé | Tor, Tails, Whonix                          |
| HVT durable                           | Compartimentation + anonymat            | Qubes + Whonix, Tor, outils complémentaires |

-----
