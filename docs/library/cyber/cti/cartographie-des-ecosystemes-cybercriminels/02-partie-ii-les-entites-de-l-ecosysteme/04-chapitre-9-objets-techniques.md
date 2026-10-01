---
title: Chapitre 9 — Objets techniques
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie II — Les entités de l'écosystème
  - index.md
---

## 9.1 Infrastructures réseau

Les objets techniques constituent l'ossature matérielle d'un écosystème cybercriminel. Chaque objet technique — domaine, IP, serveur, certificat, malware — est un nœud potentiel dans le graphe et un point de pivot pour l'investigation.

Les **domaines** sont les identifiants les plus visibles de l'infrastructure. Un domaine C2 est utilisé pour la communication entre le malware et l'opérateur. Un domaine de phishing imite un site légitime pour capturer des credentials. Un domaine de leak site héberge les données des victimes. Les registrars utilisés (certains sont plus complaisants que d'autres), les TLD choisis (les extensions exotiques comme .xyz, .top, .click sont surreprésentées dans l'infrastructure malveillante mais aussi légitimement utilisées, attention aux biais), et les patterns de nommage (génération automatique vs noms plausibles) sont des indicateurs analytiques.

Les **adresses IP et ASN** (Autonomous System Number) permettent d'identifier l'hébergeur et le réseau. Le reverse IP (quels autres domaines partagent cette IP) est l'une des techniques de pivot les plus productives. L'ASN révèle le fournisseur d'hébergement et sa réputation. Certains ASN concentrent une proportion anormalement élevée de contenu malveillant, ce qui en fait des marqueurs d'hébergement bulletproof.

Les **certificats SSL/TLS**, enregistrés publiquement via Certificate Transparency, peuvent révéler des relations entre domaines (certificats wildcard partagés, certificats multi-domaines), des sous-domaines cachés, et des patterns d'infrastructure.

## 9.2 Hébergement bulletproof

L'hébergement bulletproof désigne des fournisseurs d'hébergement qui ignorent délibérément les plaintes d'abus (abuse reports), les requêtes des forces de l'ordre, et les demandes de retrait de contenu malveillant. Ces hébergeurs sont un facilitateur critique de l'écosystème cybercriminel.

Le mécanisme économique est simple : l'hébergeur facture un premium significatif par rapport à un hébergeur classique (5 à 50 fois plus cher pour des services équivalents) en échange de la garantie d'impunité. Les clients paient pour l'assurance que leur infrastructure ne sera pas coupée suite à une plainte.

L'identification d'un hébergeur bulletproof repose sur la concentration de contenu malveillant sur ses IP et ASN (les bases de données de réputation comme AbuseIPDB, Spamhaus, et les rapports CTI le signalent), l'absence de réponse aux abuse reports (un test basique : envoyer un abuse report et observer la réponse), la localisation dans des juridictions à faible coopération judiciaire internationale, et les témoignages et discussions sur les forums underground (les acteurs recommandent et notent les hébergeurs bulletproof).

## 9.3 Malware, builders, crypters et infrastructures C2

L'écosystème technique d'une attaque implique généralement plusieurs couches de logiciels malveillants et d'outils.

Le **malware principal** (ransomware, RAT, infostealer) est le payload final. Son analyse (reverse engineering) révèle la famille, le variant, le builder utilisé, les fonctionnalités, et parfois des artefacts de développement (chemins de fichiers, variables de débogage, commentaires en langue originale) qui peuvent fournir des indices d'attribution.

Le **builder** est l'outil qui permet de générer des variants personnalisées du malware. Dans un modèle RaaS, l'opérateur fournit le builder aux affiliés, qui génèrent leurs propres variants avec des paramètres spécifiques (adresse C2, extension des fichiers chiffrés, contenu de la note de rançon). L'identification du builder confirme le lien avec la plateforme RaaS.

Le **crypter** est un service d'obfuscation qui rend le malware indétectable par les antivirus et les EDR. Les crypters sont vendus comme des services spécialisés (Fully UnDetectable, ou FUD) avec des tarifs variant de 20 à 500 dollars par obfuscation, ou sous forme d'abonnements mensuels. Un même crypter peut être utilisé par des acteurs sans aucun lien entre eux — c'est un piège analytique majeur (voir section suivante).

Le **loader** est un malware de première étape, souvent distribué par email (pièce jointe ou lien), qui télécharge et exécute le payload principal une fois la machine compromise. Les loaders (comme IcedID, QakBot avant sa disruption, ou les successeurs apparus depuis) sont souvent des services indépendants du payload final.

L'**infrastructure C2** (Command and Control) est le réseau de serveurs que le malware utilise pour recevoir des instructions et exfiltrer des données. Les panels C2 — interfaces web accessibles aux opérateurs pour contrôler les machines compromises — sont parfois détectables via des scans réseau (Shodan, Censys) quand ils sont mal sécurisés.

## 9.4 Mutualisation de services techniques — le piège des faux liens

C'est un point critique pour la rigueur analytique : de nombreux services techniques sont mutualisés entre des acteurs qui n'ont aucun lien opérationnel entre eux.

Un même hébergeur bulletproof sert des dizaines de groupes différents. Un même crypter est utilisé par des opérations sans aucune connexion. Un même loader distribue des payloads de familles de malware distinctes. Un même registrar est utilisé pour enregistrer des milliers de domaines malveillants sans lien entre eux.

La conséquence analytique est que la **co-localisation technique n'est pas un lien opérationnel**. Deux domaines sur la même IP ne sont pas nécessairement gérés par le même acteur — ils peuvent simplement être hébergés chez le même prestataire. Deux malwares utilisant le même crypter ne sont pas nécessairement développés par le même groupe — ils utilisent le même service commercial.

Pour qu'un lien technique soit significatif, il faut des indicateurs supplémentaires de co-gestion : même certificat wildcard (qui implique un contrôle commun), même Google Analytics ou pixel de suivi, même code personnalisé dans les pages web, ou des configurations techniques identiques au-delà de ce que le prestataire fournit par défaut. Le détail de la qualification des liens est traité au Ch.11.

## 9.5 Fil rouge — NEXUS : l'infrastructure révèle ses liens

> **🔍 NEXUS — Épisode 9**
>
> L'analyse du malware par le CERT révèle que le sample est un variant de PhantomCrypt généré par le builder v3.2 de la plateforme. L'ID d'affilié est intégré dans le binaire (pratique courante pour le suivi des commissions) : `AFF-0x7A3`. Cet ID confirme le lien avec le programme RaaS PhantomCrypt.
>
> L'infrastructure C2 est explorée plus en profondeur. Le panel de contrôle `phcrypt-panel[.]xyz` est accessible via le port 8443 avec une interface de login. Shodan révèle que ce panel utilise un framework personnalisé avec un header HTTP distinctif (`X-Panel-Version: PC-3.2-aff`). Ce même header est trouvé sur deux autres IP dans des rapports CTI — il s'agit de l'infrastructure centralisée de PhantomCrypt, pas d'un déploiement spécifique à kr0n0s_ops.
>
> Le blog `phantom-news[.]press`, en revanche, partage avec le domaine C2 non seulement la même IP mais aussi le même Google Analytics ID et le même certificat wildcard. Ces indicateurs de co-gestion vont au-delà de la simple co-localisation. Samira qualifie le lien C2-blog comme « fort — co-gestion probable, pas simple mutualisation d'hébergement ».

---
