---
title: Chapitre 7 — I2P, Freenet et réseaux alternatifs
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie II — Infrastructures techniques et anonymat
  - index.md
---

Tor n'est pas le seul darknet. Plusieurs réseaux alternatifs coexistent, avec des propriétés différentes. Pour un analyste CTI, leur connaissance est utile : certains acteurs migrent vers ces réseaux quand Tor devient trop surveillé ou quand ils cherchent des propriétés spécifiques.

## 7.1 I2P (Invisible Internet Project)

**I2P** (invisibleinternet.net) est un darknet développé depuis 2003, conçu pour les communications peer-to-peer dans un réseau fermé (contrairement à Tor qui permet aussi de sortir vers l'Internet clearnet).

**Architecture — « garlic routing »** : variation de l'onion routing où plusieurs messages sont **regroupés en ail** (garlic) avant d'être chiffrés. Cette approche offre des propriétés d'obfuscation du trafic différentes.

**Tunnels unidirectionnels** : contrairement à Tor qui utilise des circuits bidirectionnels, I2P utilise des tunnels séparés pour l'entrée et la sortie. Un serveur a ses tunnels entrants, un client a ses tunnels sortants — cette séparation complique l'analyse de trafic.

**Distribution peer-to-peer** : I2P n'a pas de directory authorities centraux (contrairement aux 9 directory authorities Tor). Chaque nœud participe au routage. Cette décentralisation renforce la résilience mais complique le bootstrap.

**Terminologie propre** : les sites sur I2P s'appellent des **eepsites** et utilisent des adresses en `.i2p` (par exemple `stats.i2p`, `i2p-projekt.i2p`).

**Usages**. I2P est moins populaire que Tor — réseau plus petit (quelques dizaines de milliers de nœuds vs millions d'utilisateurs Tor), interface moins accessible, écosystème applicatif restreint. Les forums cybercriminels russophones maintiennent souvent un miroir I2P en plus de leur .onion, par résilience. Certains acteurs préfèrent I2P pour des communications ciblées où Tor est perçu comme trop surveillé (perception plutôt qu'évidence technique).

**Exemple concret** : IndustrialLeaks (le forum fictif de DARKSTREAM) mentionne un miroir I2P. C'est un pattern typique — un forum sérieux maintient deux points d'entrée indépendants pour résilience face aux saisies.

**Attaques et limites**. I2P a été moins étudié académiquement que Tor, et moins attaqué publiquement — mais les propriétés de sécurité sont similaires. La décentralisation peut être un faux confort : un adversaire qui participe en masse au réseau (sybil attack) peut potentiellement compromettre l'anonymat.

## 7.2 Freenet / Hyphanet

**Freenet** (rebaptisé **Hyphanet** en 2023) est l'un des plus anciens darknets, lancé en 2000 par Ian Clarke. Modèle radicalement différent de Tor et I2P : **stockage distribué**.

**Principe** : les utilisateurs contribuent de l'espace disque local au réseau. Les contenus publiés sont **chiffrés et dispersés** sur les machines des utilisateurs, sans qu'aucune ne connaisse l'intégralité d'un contenu. Les contenus populaires sont automatiquement répliqués ; les contenus oubliés s'effacent.

**Propriétés** :

- **Résistance à la censure** : supprimer un contenu de Freenet est très difficile — il faudrait saisir toutes les machines qui en hébergent un fragment.
- **Déni plausible** : un utilisateur hébergeant des fragments chiffrés peut plausiblement ignorer ce qu'il héberge.
- **Usage principal** : publication de contenu (sites statiques, blogs, fichiers) plutôt que communication en temps réel.

**Opennet vs Darknet** : Freenet offre deux modes. **Opennet** : tout nœud peut rejoindre. **Darknet** (« friend-to-friend ») : vous n'êtes connecté qu'à des nœuds opérés par des personnes que vous connaissez — résilience maximale mais effet réseau limité.

**Usages criminels** : Freenet a historiquement été un canal de diffusion de CSAM, raison pour laquelle de nombreuses opérations de police l'ont visé. La capacité à poursuivre un utilisateur sur la seule présence de fragments chiffrés (sans preuve qu'il connaissait le contenu) a été discutée dans plusieurs juridictions.

**Population** : très modeste par rapport à Tor. Usage résiduel, plutôt activiste/libertaire que cybercriminel organisé.

## 7.3 ZeroNet, Lokinet et autres

**ZeroNet** : réseau décentralisé basé sur Bitcoin (identité et signature via clés Bitcoin) et BitTorrent (hosting distribué). Usage modeste, quelques sites politiques, quelques activistes.

**Lokinet** : darknet associé à la cryptomonnaie Loki/Oxen, basé sur une architecture type onion routing mais incentivée par la crypto. Usage limité, écosystème jeune.

**Yggdrasil, cjdns** : réseaux expérimentaux de mesh networking, pas spécifiquement orientés anonymat mais parfois utilisés comme alternatives.

**GNUnet** : projet académique de longue date, très peu déployé en pratique.

**Matrix fédéré** : pas un darknet à proprement parler, mais Matrix (protocole de messagerie fédéré) est parfois utilisé sur Tor pour des communications chiffrées de groupe. Session (basé sur Oxen/Lokinet) est une messagerie qui a émergé.

## 7.4 Pourquoi la multiplicité des darknets ?

Aucun darknet ne domine totalement. Les raisons de la coexistence :

- **Préférences techniques** : Tor pour latence modérée + grande communauté ; I2P pour architectures peer-to-peer ; Freenet pour publication résistante.
- **Segmentation communautaire** : certains acteurs préfèrent se concentrer là où ils sont connus.
- **Redondance** : les opérateurs sérieux maintiennent souvent deux ou trois points d'entrée (onion, i2p, éventuellement Tor v3 authenticated + i2p) pour survivre à une saisie.
- **Évolution défensive** : quand un darknet devient intensément surveillé (perception), une partie de la population migre.

Pour l'investigateur CTI, l'implication pratique : **toujours vérifier si un service cible a un miroir sur un autre darknet**. Un forum saisi sur Tor peut rester opérationnel sur I2P pendant des semaines avant que les autorités l'attrapent aussi. Un acteur privé peut continuer ses activités via I2P après que son .onion est compromis.

---
