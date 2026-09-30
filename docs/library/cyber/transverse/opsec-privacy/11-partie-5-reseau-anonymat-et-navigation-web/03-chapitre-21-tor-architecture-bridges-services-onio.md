---
title: 'Chapitre 21 — Tor : architecture, bridges, services onion, OPSEC'
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 5 — Réseau, anonymat et navigation web
  - index.md
---

> **Niveau de posture (cf. Ch 2.6)** : Tor n’est *pas* requis au Niveau 1 (la majorité des lecteurs n’en ont pas besoin pour leur posture quotidienne). Au Niveau 2, Tor Browser est utilisé ponctuellement pour navigation anonyme (recherches sensibles, accès à services onion légitimes, premières prises de contact source). Au Niveau 3, Tor devient routage par défaut pour certaines identités via Whonix, avec bridges et transports obfusqués si l’environnement le requiert. Tor n’est pas toujours protecteur — l’utiliser depuis un environnement qui t’identifie localement peut être contre-productif (cf. cas Eldo Kim, Annexe 8.2).

## 21.1 Architecture Tor en bref

Tor (The Onion Router) route ton trafic à travers **trois relais successifs** :

1. **Guard** : connaît ton IP réelle mais pas la destination.
1. **Middle** : ne connaît ni l’origine ni la destination.
1. **Exit** : connaît la destination mais pas l’origine.

Chaque couche est chiffrée de manière à ce qu’aucun relais individuel n’ait l’image complète. C’est l’essence du *onion routing*.

## 21.2 Limites du modèle

- **Corrélation de trafic** : un adversaire qui observe à la fois l’entrée *et* la sortie peut, par analyse statistique de volumes et timings, corréler les deux. Les services de renseignement majeurs (NSA et leurs équivalents) ont cette capacité partielle. C’est la principale limite de Tor pour les profils HVT.
- **Exit malveillant** : un nœud de sortie peut espionner le trafic non chiffré qui passe par lui. D’où : **toujours HTTPS** sur Tor.
- **Performances** : latence élevée, débit limité. Tor n’est pas pour le streaming.

## 21.3 Bridges et transports obfusqués

Dans les pays qui bloquent Tor (Chine, Iran, Russie, etc.), les IPs publiques des relais Tor sont bannies. Les **bridges** (relais non publiés) permettent un point d’entrée alternatif. Les **transports obfusqués** déguisent le trafic Tor en autre chose :

- **obfs4** : trafic indistinguable de trafic aléatoire. Le plus déployé.
- **meek** : trafic camouflé en HTTPS vers un CDN (Azure, Google, Amazon). Lourd mais très résistant.
- **Snowflake** : utilise des proxys volontaires via WebRTC. Rotatif, résistant à la censure récente.

Pour obtenir des bridges : `bridges.torproject.org`, ou via email (`bridges@torproject.org`), ou via Telegram bot (`@GetBridgesBot`).

## 21.4 Services onion v3

Les **services onion** (anciennement « hidden services ») permettent à un serveur d’être accessible *uniquement* via Tor, sous une adresse `.onion`. L’adresse onion est dérivée de la clé publique du serveur. Avantages :

- **Anonymat du serveur**, pas seulement du client.
- **Authentification cryptographique** intégrée : pas besoin de TLS pour vérifier qu’on parle au bon serveur (l’adresse onion *est* la clé).
- **Pas de sortie sur le réseau public** : le trafic ne passe pas par un exit node.

Usages : SecureDrop (Ch 28), partage de fichiers OnionShare, sites publiquement militants en environnement hostile (Facebook, NY Times et BBC ont des miroirs onion), Tor Browser lui-même.

## 21.5 OPSEC Tor

Tor *peut* être cassé par mauvais usage applicatif :

- **Ne pas mélanger** : tu ne te connectes pas à ton compte Gmail nominal via Tor. Ça ne sert à rien et ça t’identifie.
- **Tor Browser uniquement** : ne pas utiliser Tor avec Firefox normal, qui n’a pas le hardening fingerprint nécessaire (cf. Ch 24).
- **Pas de plugins** : Flash (historique), JavaScript non contrôlé, PDF viewers vulnérables = casse Tor.
- **Time zone** : Tor Browser force UTC ; si tu modifies, tu te révèles.
- **Identité dans le contenu** : tu peux être anonyme techniquement mais écrire « moi journaliste à Bruxelles 35 ans », ce qui annule l’effort.

## 21.6 Tor seul, VPN+Tor, Tor+VPN

Configurations possibles et leurs implications :

- **Tor seul** : configuration standard, recommandée pour la plupart.
- **VPN avant Tor (VPN→Tor)** : le VPN voit que tu utilises Tor ; le guard Tor ne voit pas ton IP réelle. Utile si tu veux cacher *à ton FAI* l’utilisation de Tor. Coût : tu fais confiance au VPN.
- **Tor avant VPN (Tor→VPN)** : presque toujours **mauvaise idée**. Casse le modèle Tor, identifie tes sessions au VPN.

**Recommandation** : Tor seul, ou Tor avec bridges si environnement bloquant.

## 21.7 Tests de fuite

- **check.torproject.org** : valide que tu es bien sur Tor.
- **dnsleaktest** depuis Tor Browser : valide que DNS passe par Tor.
- **AmIUnique** : pour vérifier le fingerprint.

## 21.8 Cas d’utilisateurs démasqués

- **Eldo Kim**, étudiant Harvard 2013 : envoie une fausse alerte à la bombe via Tor + Guerrilla Mail. Identifié parce qu’il était le seul étudiant connecté à Tor depuis le réseau Harvard à ce moment-là. Corrélation triviale. Cf. Annexe 8.
- **Ross Ulbricht** : son arrestation ne tient *pas* à un cassage de Tor, mais à une erreur OPSEC (pseudo réutilisé entre forum technique et identité civile, gmail nominatif). Cf. Annexe 8.

Leçon constante : **Tor tient techniquement, l’OPSEC casse**.

## 21.9 *Fil rouge* — Anya publie via Tor

Anya V., opposante russe en exil à Berlin, publie ses analyses politiques sur un blog. Stack : Tor Browser sur un laptop dédié, hébergement chez un fournisseur acceptant Tor, paiement en cryptomonnaies achetées en Allemagne. Pseudonymat stable mais isolation stricte de son identité civile berlinoise. Elle utilise le même mail Proton via Tor exclusivement, depuis le même appareil, depuis sa zone géographique habituelle (cohérence). Elle évite les heures de connexion suspectes (régularité = identifiable).

-----
