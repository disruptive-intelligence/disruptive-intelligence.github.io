---
title: Chapitre 2 — Ce que l’enquête crypto permet vraiment (et ne permet pas)
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie I — Comprendre l’écosystème crypto sans fantasme
  - index.md
---

Avant de plonger dans les techniques, il est essentiel de **calibrer les attentes**. Un mandat client mal cadré ou un management qui croit que « le crypto est traçable, donc tout se résout » conduit à des frustrations et des rapports inadaptés.

## 2.1 Ce que l’enquête crypto permet

**Suivre des flux publics**. L’analyste peut, sur Bitcoin/Ethereum/etc., suivre les mouvements depuis une adresse de départ jusqu’à la dispersion finale ou la rupture de visibilité (mixer, privacy coin, off-ramp non coopératif). Cette traçabilité est gratuite, publique, vérifiable.

**Identifier des points de contact avec des services connus**. Quand les fonds passent par un exchange labellisé, un mixer connu, un bridge identifié — l’analyse capture ces points. Ils servent d’**ancrage** pour la suite (réquisition, coopération exchange, qualification de risque).

**Repérer des patterns**. Récurrence dans les flux, montants typiques, fenêtres temporelles, structures de wallets. Patterns qui aident à identifier la **typologie** d’activité (pig butchering, ransomware, fraude, etc.).

**Documenter un chemin de fonds**. Reconstituer, pas à pas, la trajectoire d’une somme entre l’adresse de départ et un point d’aboutissement (ou d’opacité). Cette documentation est un **livrable** essentiel — pour la victime, le procureur, l’autorité, ou la communauté CTI.

**Produire des hypothèses calibrées**. À partir des observations, formuler des hypothèses sur la nature de l’activité, les acteurs probables, les juridictions impliquées, les moyens de coopération.

**Appuyer un signalement ou une plainte**. Un rapport OSINT crypto solide permet à la victime de déposer plainte avec éléments tangibles, à TRACFIN de qualifier un signalement de soupçon, à un magistrat de fonder une commission rogatoire internationale, à une autorité de geler des fonds via émetteur stablecoin coopératif.

**Soutenir une saisie**. Quand la coopération internationale s’aligne, l’enquête OSINT prépare les éléments techniques permettant aux forces de l’ordre d’opérer une saisie effective (cf cas Bitfinex, Colonial Pipeline, Ch.41-42).

## 2.2 Ce que l’enquête crypto ne permet pas

**Identifier directement une personne à partir d’une adresse**. Sauf cas particulier (publication volontaire, mismatch OPSEC évident, données KYC obtenues via réquisition), l’OSINT crypto pure ne donne pas l’identité civile. Le mandat « identifie qui possède cette adresse » est un mandat **mal posé**.

**Récupérer des fonds dispersés sans intervention extérieure**. L’analyste documente le chemin ; la récupération nécessite une action **off-chain** (gel par émetteur stablecoin, saisie par autorité, coopération exchange). Sans cette action, les fonds restent où ils sont.

**Casser le chiffrement Monero**. Sauf cas spécifiques (vulnérabilités d’implémentation, decoy patterns exploitables), Monero reste opaque. L’enquête se déplace vers d’autres angles.

**Démixer avec certitude un mixer custodial**. Un mixer comme Tornado Cash mélange les fonds de centaines d’utilisateurs. Reconstituer **avec certitude** les paires entrée/sortie est dans la plupart des cas impossible — sauf erreurs spécifiques (montants atypiques, timings exploitables, patterns d’usage).

**Garantir la traçabilité cross-chain sans outil professionnel**. Les bridges complexifient considérablement le suivi. Un fonds qui passe d’Ethereum à BNB Chain via plusieurs bridges, swaps DEX, et conversions stablecoin peut devenir difficile à suivre avec les seuls outils gratuits.

**Obtenir des données KYC d’exchanges**. Réservé aux autorités via réquisition légale. L’analyste OSINT prépare la cible (« cette adresse est probablement un exchange deposit address de [exchange X] »), l’autorité opère la requête.

**Produire une attribution judiciairement opposable sans corroboration**. Un rapport OSINT seul, même excellent, ne suffit généralement pas à condamner devant un tribunal. Il sert à **orienter** une enquête, pas à la conclure judiciairement.

## 2.3 Les zones grises

Entre le « je peux » et le « je ne peux pas », plusieurs zones intermédiaires.

**Attribution probabiliste**. Avec recoupement de plusieurs signaux faibles (style d’usage, patterns temporels, infrastructure, mentions OSINT), on peut formuler une attribution **probable** (60-80% confiance). Utilisable opérationnellement, pas judiciairement.

**Identification d’une typologie d’activité**. Reconnaître qu’un cluster fait du pig butchering est généralement faisable (patterns de collection, tailles de transactions, flux vers exchanges). L’identification du **réseau précis** derrière est plus dure.

**Contribution à l’identification d’un VASP non coopératif**. Plusieurs investigations montrent qu’analyser les patterns d’un exchange permet d’identifier sa juridiction probable, ses banques partenaires, ses points faibles — utile pour pression réglementaire et coordination internationale.

**Détection de fraude en temps réel**. Avec des feeds adaptés, on peut alerter sur des transactions suspectes en cours (paiements vers des adresses sanctionnées, patterns de pump-and-dump). Capacité défensive valable, attribution post-hoc nécessaire.

## 2.4 Calibration des attentes du mandant

Un mandat client crypto bien cadré contient :

**Périmètre clair**. Quelles adresses, quels flux, quelle période. « Tracez tout » est un mandat creux.

**Objectifs réalistes**. « Documenter le chemin des fonds, identifier les points de contact avec des services, produire un rapport actionnable » plutôt que « identifier le criminel ».

**Livrables explicites**. Rapport, captures, IoC structurés, recommandations.

**Cadre coopératif**. Avec quelles autorités, quelle TLP, quelle politique de communication.

**Budget et délai**. Une investigation crypto sérieuse prend 2-12 semaines selon complexité. Pas 48h.

**Sortie attendue**. Que doit-il se passer après le rapport ? Plainte, signalement, gel d’actifs, communication interne, threat intel partagée ?

Sarah Marin, dans MIXSHADOW, opère sous mandat **bien cadré** : le DGSI et le client sont alignés sur des attentes réalistes — pas de promesse de récupération, pas d’attribution magique, valeur ajoutée par renseignement et coopération.

## 2.5 Le piège des promesses excessives

L’industrie de la blockchain intelligence est, à juste titre, en croissance. Mais elle peut aussi être tentée par le marketing excessif — promesses de « démixage parfait », « attribution garantie », « récupération assurée ». L’analyste sérieux résiste à ces promesses, autant pour préserver sa crédibilité que pour aligner les attentes du mandant sur la réalité opérationnelle.

Phrase à intérioriser : **« Je vais documenter tout ce que les données publiques permettent de dire. Je ne vais pas inventer ce qu’elles ne permettent pas de conclure. »** C’est la signature de l’analyste pro.

-----
