---
title: 'Chapitre 44 — Dark Web et DARKINT : panorama opérationnel'
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VI — Corporate, infrastructure et données exposées
  - index.md
---

## 44.1 Définition et périmètre

Le **dark web** désigne l'ensemble des services accessibles uniquement via des réseaux de routage anonymisé : principalement **Tor** (The Onion Router), mais aussi **I2P** (Invisible Internet Project), **Freenet**, et plus récemment des solutions émergentes.

Le **DARKINT** (Dark Web Intelligence) est la discipline OSINT spécialisée dans la collecte et analyse de ces espaces.

Ce chapitre fournit une **vue opérationnelle**. Pour la profondeur (architecture Tor, marketplaces, leak sites, méthodologies LEA, IA criminelle dans le dark web), **renvoi systématique vers Dark Web vFULL**.

## 44.2 Tor : architecture brève

**Tor** route le trafic via 3 relais successifs (entry guard, middle relay, exit node). Chaque relais ne connaît qu'une partie du chemin. Les services `.onion` sont accessibles uniquement via Tor.

**Anonymat fourni.** L'IP source est masquée. Mais OPSEC stricte nécessaire au-delà.

**Tor Browser.** Le navigateur officiel. Préconfigurations privacy par défaut.

## 44.3 Marketplaces dark web

**Évolution 2020-2026.** AlphaBay (fermé 2017, revenu 2021, refermé 2023), Hydra (RUS, fermé 2022 par opération germano-russe), Genesis Market (fermé 2023), divers successeurs en émergence-fermeture continue.

**Typologie.**

- Marketplaces drogues/fraudes (Mainstream).
- Forums clandestins cybercriminels (XSS, Exploit — surface borderline ; Russian Anonymous Marketplace en dark web).
- Leak sites ransomware (Conti, LockBit, etc.).
- Carding shops.
- Services divers (faux papiers, etc.).

**Pour OSINT.**

- **Consultation** : possible, OPSEC stricte.
- **Interaction** : réservée LEA et journalisme spécialisé strictement encadré.
- **Achat** : sortie immédiate du périmètre OSINT pur.

## 44.4 Leak sites ransomware

Les **leak sites** des gangs ransomware (Conti, LockBit, ALPHV/BlackCat, AlphV) publient les données des victimes qui n'ont pas payé.

**Pour OSINT corporate.**

- Vérifier si une entité figure sur un leak site = elle a été victime de ransomware.
- Données exposées = peuvent contenir des informations stratégiques.

**Approche.**

- Monitoring via outils CTI (Recorded Future, Flashpoint, KELA, Flare, Searchlight).
- Vue indirecte via rapports publiés (DarkOwl, Cybersixgill).

## 44.5 Outils de monitoring dark web

**Outils commerciaux.**

- **Flare** : monitoring dark web et leaks.
- **Recorded Future** : standard institutionnel CTI.
- **KELA** : focus dark web.
- **Cybersixgill** : standard CTI.
- **DarkOwl** : indexation deep web.
- **Searchlight Cyber**.

Tous payants, abonnements lourds (5-50 k€/an).

## 44.6 Méthodologie de consultation prudente

Si consultation directe nécessaire :

1. **VM Whonix** ou Tails sur clé USB.
2. **Tor Browser** uniquement.
3. **Pas de comptes** sauf strictement nécessaire (compte d'investigation dédié, créé sur cette VM uniquement).
4. **Pas d'interaction** active.
5. **Capture** via SingleFile dans la VM.
6. **Pas de téléchargement de contenus illégaux** (CSAM, données piratées exploitables) — **refus immédiat et signalement** si rencontre.
7. **Documentation** stricte dans journal d'enquête.

## 44.7 Cas d'usage OSINT légitime

**Investigation corporate.** Vérifier si données d'une cible figurent sur leak sites.

**Investigation criminelle (consultative).** Identifier réseaux, méthodes, prix.

**CTI.** Monitoring d'acteurs malveillants visant l'organisation cliente.

**Journalisme.** Documentation de l'écosystème criminel.

**Recherche.** Académique, droits humains.

## 44.8 Renvoi systématique Dark Web vFULL

Le présent cours s'arrête ici sur le dark web. **Tout approfondissement** (architecture détaillée, marketplaces vivantes, forums, opérations LEA, IA criminelle dans le dark web, OPSEC avancée, attribution) est traité dans **Dark Web vFULL**.

Ce renvoi est explicite parce que :

- Le dark web est un domaine où l'erreur (technique ou déontologique) a des conséquences graves.
- L'écosystème évolue très vite (marketplaces qui ouvrent / ferment mensuellement).
- Les protocoles d'investigation diffèrent du dark web vers le surface web.

> **MIRAGE — Épisode 15 : Piste dark web, renvoi Dark Web vFULL**
>
> L'analyste s'interroge sur d'éventuelles traces de Delaunay ou TechnoVert sur le dark web.
>
> **Vérification leak sites ransomware.** Recherche dans agrégateurs publics (DarkTracer, RansomLook) : aucune mention de TechnoVert. Pas victime ransomware identifiée.
>
> **Vérification marketplaces.** Hors de portée pour OSINT privé sans outil CTI premium. Si pertinence forte se révèle, escalade vers partenaire CTI ou inclusion dans réquisition judiciaire ultérieure.
>
> **Conclusion sur ce volet.** Aucune piste dark web significative identifiée à ce stade. Le cluster de désinformation observé semble opérer principalement sur surface web (X, Telegram, blogs). Pas de bascule dark web nécessaire pour l'enquête MIRAGE.
>
> **Documentation.** Le rapport mentionnera cette vérification (« couverture dark web limitée à la consultation de leak sites publics ; aucune mention de TechnoVert identifiée ; couverture marketplaces réservée à des outils CTI non mobilisés ») pour transparence sur les limites.
>
> Pour les enquêtes nécessitant approfondissement dark web (criminalité organisée, ransomware victims, marketplaces narcotiques), **renvoi vers Dark Web vFULL**.

-----
