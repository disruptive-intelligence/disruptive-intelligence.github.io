---
title: Dark Web
source: Cyber/01_CTI/Dark_Web_vFULL.md
---

*Architecture • Écosystèmes • OPSEC • Investigation • Renseignement*

**Cours complet — 48 chapitres, 9 parties, 7 annexes.**

---

## Avant-propos

Ce cours apprend à **comprendre et investiguer le dark web** dans une posture professionnelle. Il s'adresse aux analystes CTI, investigateurs, RSSI, chercheurs en sécurité, et professionnels de la conformité et de la lutte contre la cybercriminalité. Il est conçu pour être **auto-suffisant** — un lecteur qui part de zéro, travaille le cours dans l'ordre, et fait les exercices proposés, acquiert un niveau professionnel.

**Ce que ce cours fait** : il vous apprend à situer le dark web dans le paysage numérique, comprendre ses infrastructures techniques (Tor, I2P, cryptomonnaies), cartographier ses écosystèmes (forums, marchés, leak sites, messageries), naviguer avec une OPSEC rigoureuse, investiguer une fuite de données ou une compromission, produire du renseignement actionnable, et coopérer avec les autorités. Il couvre aussi les cadres juridiques, les pièges analytiques, et les évolutions 2024-2026.

**Ce que ce cours ne fait pas** : il n'est pas un mode d'emploi pour l'activité criminelle. Il ne fournit pas de liens actifs vers des plateformes illicites, ne donne pas de techniques de contournement du law enforcement pour un usage criminel, et ne vend pas de sensationnel. Les exemples techniques sont suffisamment précis pour comprendre, pas assez pour reproduire une infraction.

**Posture pédagogique** : factuelle, calibrée, vérifiable. Chaque affirmation forte renvoie à une source publique (rapport d'agence, publication journalistique reconnue, analyse vendor CTI sérieuse). Les ordres de grandeur sont donnés avec leurs limites. Les analyses sont honnêtes sur l'incertitude.

**Continuité avec la bibliothèque** : ce cours s'articule avec OSINT Mastery (techniques OSINT transposées au dark web), AU CŒUR DES APT (acteurs étatiques qui utilisent le dark web pour leurs opérations), Cartographie des écosystèmes cybercriminels (contexte structural), OSINT Crypto (traçage blockchain), et FININT (investigation financière). Les renvois explicites permettent d'approfondir sans dupliquer.

---

## Fil rouge : Opération DARKSTREAM

Pour ancrer la théorie dans la pratique, ce cours suit un cas fictif inspiré d'investigations réelles. **Opération DARKSTREAM** déroule, chapitre après chapitre, l'investigation d'une exfiltration de données industrielles.

**Le contexte.** **Vectris Aerospace** est un équipementier aérospatial européen (4 500 collaborateurs, coté SBF 120), partenaire de plusieurs programmes de défense et spatiaux. En mars 2026, son SOC détecte une anomalie de trafic sortant vers une IP résidentielle. L'investigation interne remonte à un poste R&D compromis. Volume exfiltré estimé : **420 Go** — spécifications techniques, documents de conception, bases clients, notes de conception propulsion. Compromission entre 8 et 14 semaines avant détection. Vectris classifie l'incident *critique*, notifie l'ANSSI et la DGSI (OIV défense), et mandate **Athéna Group**, un cabinet CTI français.

**L'analyste.** **Lucas Ferreira**, analyste CTI senior chez Athéna Group. 8 ans d'expérience dont 3 au CERT d'une grande banque. PASSI-qualifié. Le mandat d'Athéna : **(1)** confirmer ou infirmer la circulation des données Vectris sur le dark web ; **(2)** authentifier les données offertes ; **(3)** cartographier l'écosystème impliqué (vendeur, acheteurs potentiels, courtiers) ; **(4)** produire un rapport actionnable pour Vectris et la DGSI ; **(5)** si possible, contribuer à l'identification du vendeur.

**Les signaux initiaux.** Un service de monitoring (Recorded Future) a détecté une mention de « Vectris » et « propulsion specs » sur un forum .onion russophone, **IndustrialLeaks** — forum spécialisé dans les données industrielles, ~3 000 membres, créé en 2022. Un vendeur au pseudonyme **aero_source** propose « aerospace dump 420GB, EU supplier, reconnaissance française, propulsion R&D inside ». Prix demandé : 65 000 USDT.

**La méthode.** Lucas applique une méthode rigoureuse : OPSEC stricte pour la collecte, authentification par échantillons, pivoting OSINT sur le pseudonyme, traçage crypto des transactions connues, analyse linguistique, corrélation cross-forum, calibration de l'attribution. L'opération durera **6 semaines** — Ch.41 en détaillera la synthèse complète.

Les épisodes DARKSTREAM jalonnent le cours aux moments où le concept enseigné éclaire la progression de Lucas.

---

## Sommaire

- [Partie I — Fondations : COMPRENDRE LE DARK WEB](01-partie-i-fondations-comprendre-le-dark-web/index.md)
    - [Chapitre 1 — Internet, web visible, deep web, dark web](01-partie-i-fondations-comprendre-le-dark-web/01-chapitre-1-internet-web-visible-deep-web-dark-web.md)
    - [Chapitre 2 — Histoire et évolution des darknets](01-partie-i-fondations-comprendre-le-dark-web/02-chapitre-2-histoire-et-evolution-des-darknets.md)
    - [Chapitre 3 — Pourquoi le dark web existe](01-partie-i-fondations-comprendre-le-dark-web/03-chapitre-3-pourquoi-le-dark-web-existe.md)
    - [Chapitre 4 — Le dark web comme écosystème](01-partie-i-fondations-comprendre-le-dark-web/04-chapitre-4-le-dark-web-comme-ecosysteme.md)
- [Partie II — Infrastructures techniques et anonymat](02-partie-ii-infrastructures-techniques-et-anonymat/index.md)
    - [Chapitre 5 — Architecture de Tor](02-partie-ii-infrastructures-techniques-et-anonymat/01-chapitre-5-architecture-de-tor.md)
    - [Chapitre 6 — Onion services (hidden services)](02-partie-ii-infrastructures-techniques-et-anonymat/02-chapitre-6-onion-services-hidden-services.md)
    - [Chapitre 7 — I2P, Freenet et réseaux alternatifs](02-partie-ii-infrastructures-techniques-et-anonymat/03-chapitre-7-i2p-freenet-et-reseaux-alternatifs.md)
    - [Chapitre 8 — Cryptomonnaies et anonymat financier](02-partie-ii-infrastructures-techniques-et-anonymat/04-chapitre-8-cryptomonnaies-et-anonymat-financier.md)
    - [Chapitre 9 — Hébergement, infrastructure et résilience](02-partie-ii-infrastructures-techniques-et-anonymat/05-chapitre-9-hebergement-infrastructure-et-resilienc.md)
- [Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/index.md)
    - [Chapitre 10 — Forums clandestins : culture, hiérarchie et codes](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/01-chapitre-10-forums-clandestins-culture-hierarchie.md)
    - [Chapitre 11 — Marchés du dark web](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/02-chapitre-11-marches-du-dark-web.md)
    - [Chapitre 12 — Leak sites ransomware et vitrines de revendication](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/03-chapitre-12-leak-sites-ransomware-et-vitrines-de-r.md)
    - [Chapitre 13 — Canaux, chats et messageries clandestines](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/04-chapitre-13-canaux-chats-et-messageries-clandestin.md)
    - [Chapitre 14 — Données volées et marchés de la fuite](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/05-chapitre-14-donnees-volees-et-marches-de-la-fuite.md)
    - [Chapitre 15 — Stealer logs](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/06-chapitre-15-stealer-logs.md)
    - [Chapitre 16 — Services criminels et profils d'acteurs](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/07-chapitre-16-services-criminels-et-profils-d-acteur.md)
    - [Chapitre 17 — Marché des 0-day et chaîne exploit → attaque](03-partie-iii-ecosystemes-du-dark-web-espaces-acteurs/08-chapitre-17-marche-des-0-day-et-chaine-exploit-att.md)
- [Partie IV — Économie clandestine](04-partie-iv-economie-clandestine/index.md)
    - [Chapitre 18 — Pourquoi l'économie du dark web fonctionne](04-partie-iv-economie-clandestine/01-chapitre-18-pourquoi-l-economie-du-dark-web-foncti.md)
    - [Chapitre 19 — Réputation, escrow, vouching, arbitrage](04-partie-iv-economie-clandestine/02-chapitre-19-reputation-escrow-vouching-arbitrage.md)
    - [Chapitre 20 — Arnaques, exit scams et manipulation de la confiance](04-partie-iv-economie-clandestine/03-chapitre-20-arnaques-exit-scams-et-manipulation-de.md)
    - [Chapitre 21 — Modèles économiques criminels](04-partie-iv-economie-clandestine/04-chapitre-21-modeles-economiques-criminels.md)
- [Partie V — Investigation, veille et collecte](05-partie-v-investigation-veille-et-collecte/index.md)
    - [Chapitre 22 — Cadre juridique, éthique et sécurité de l'analyste](05-partie-v-investigation-veille-et-collecte/01-chapitre-22-cadre-juridique-ethique-et-securite-de.md)
    - [Chapitre 23 — OPSEC opérationnelle de l'investigation](05-partie-v-investigation-veille-et-collecte/02-chapitre-23-opsec-operationnelle-de-l-investigatio.md)
    - [Chapitre 24 — Naviguer et collecter : méthodes, outils, limites](05-partie-v-investigation-veille-et-collecte/03-chapitre-24-naviguer-et-collecter-methodes-outils.md)
    - [Chapitre 25 — Investigation dans un data leak : workflow](05-partie-v-investigation-veille-et-collecte/04-chapitre-25-investigation-dans-un-data-leak-workfl.md)
    - [Chapitre 26 — Pivoting, enrichissement et corrélation OSINT](05-partie-v-investigation-veille-et-collecte/05-chapitre-26-pivoting-enrichissement-et-correlation.md)
    - [Chapitre 27 — Veille dark web](05-partie-v-investigation-veille-et-collecte/06-chapitre-27-veille-dark-web.md)
    - [Chapitre 28 — Preuve, capture et documentation](05-partie-v-investigation-veille-et-collecte/07-chapitre-28-preuve-capture-et-documentation.md)
- [Partie VI — ANALYSE, renseignement et production](06-partie-vi-analyse-renseignement-et-production/index.md)
    - [Chapitre 29 — Dé-anonymisation : méthodes et limites](06-partie-vi-analyse-renseignement-et-production/01-chapitre-29-de-anonymisation-methodes-et-limites.md)
    - [Chapitre 30 — NIT, honeypots et infiltration policière](06-partie-vi-analyse-renseignement-et-production/02-chapitre-30-nit-honeypots-et-infiltration-policier.md)
    - [Chapitre 31 — Traçage crypto et analyse financière](06-partie-vi-analyse-renseignement-et-production/03-chapitre-31-tracage-crypto-et-analyse-financiere.md)
    - [Chapitre 32 — Pièges analytiques, désinformation et faux signaux](06-partie-vi-analyse-renseignement-et-production/04-chapitre-32-pieges-analytiques-desinformation-et-f.md)
    - [Chapitre 33 — Transformer les observations en renseignement actionnable](06-partie-vi-analyse-renseignement-et-production/05-chapitre-33-transformer-les-observations-en-rensei.md)
    - [Chapitre 34 — Produire une note analytique](06-partie-vi-analyse-renseignement-et-production/06-chapitre-34-produire-une-note-analytique.md)
    - [Chapitre 35 — Menaces dark web par secteur d'activité](06-partie-vi-analyse-renseignement-et-production/07-chapitre-35-menaces-dark-web-par-secteur-d-activit.md)
- [Partie VII — Cas d'usage, tendances et prospective](07-partie-vii-cas-d-usage-tendances-et-prospective/index.md)
    - [Chapitre 36 — Ransomware, extorsion et leak sites](07-partie-vii-cas-d-usage-tendances-et-prospective/01-chapitre-36-ransomware-extorsion-et-leak-sites.md)
    - [Chapitre 37 — Dark web, influence et opérations informationnelles](07-partie-vii-cas-d-usage-tendances-et-prospective/02-chapitre-37-dark-web-influence-et-operations-infor.md)
    - [Chapitre 38 — Hacktivisme, zones grises et usages légitimes](07-partie-vii-cas-d-usage-tendances-et-prospective/03-chapitre-38-hacktivisme-zones-grises-et-usages-leg.md)
    - [Chapitre 39 — IA et dark web : menaces émergentes et défensives](07-partie-vii-cas-d-usage-tendances-et-prospective/04-chapitre-39-ia-et-dark-web-menaces-emergentes-et-d.md)
    - [Chapitre 40 — Forces de l'ordre, disruption et coopération internationale](07-partie-vii-cas-d-usage-tendances-et-prospective/05-chapitre-40-forces-de-l-ordre-disruption-et-cooper.md)
- [Partie VIII — Études DE cas et synthèse](08-partie-viii-etudes-de-cas-et-synthese/index.md)
    - [Chapitre 41 — Cas DARKSTREAM complet — investigation d'une vente de données industrielles](08-partie-viii-etudes-de-cas-et-synthese/01-chapitre-41-cas-darkstream-complet-investigation-d.md)
    - [Chapitre 42 — Cas surveillance d'un leak site ransomware](08-partie-viii-etudes-de-cas-et-synthese/02-chapitre-42-cas-surveillance-d-un-leak-site-ransom.md)
    - [Chapitre 43 — Cas traque d'un Initial Access Broker](08-partie-viii-etudes-de-cas-et-synthese/03-chapitre-43-cas-traque-d-un-initial-access-broker.md)
    - [Chapitre 44 — Maturité analyste et programme de veille durable](08-partie-viii-etudes-de-cas-et-synthese/04-chapitre-44-maturite-analyste-et-programme-de-veil.md)
- [Partie IX — Navigation pratique et collecte défensive encadrée](09-partie-ix-navigation-pratique-et-collecte-defensiv/index.md)
    - [Chapitre 45 — Premier accès à Tor](09-partie-ix-navigation-pratique-et-collecte-defensiv/01-chapitre-45-premier-acces-a-tor.md)
    - [Chapitre 46 — Authentifier un miroir officiel .onion](09-partie-ix-navigation-pratique-et-collecte-defensiv/02-chapitre-46-authentifier-un-miroir-officiel-onion.md)
    - [Chapitre 47 — Collecter et documenter une source légitime avec Hunchly](09-partie-ix-navigation-pratique-et-collecte-defensiv/03-chapitre-47-collecter-et-documenter-une-source-leg.md)
    - [Chapitre 48 — Vérification défensive de l'exposition dans les bases de leaks publiques](09-partie-ix-navigation-pratique-et-collecte-defensiv/04-chapitre-48-verification-defensive-de-l-exposition.md)
    - [Exercice final de la Partie IX — Mini-investigation défensive légitime](09-partie-ix-navigation-pratique-et-collecte-defensiv/05-exercice-final-de-la-partie-ix-mini-investigation.md)
- [Annexes](10-annexes/index.md)
    - [Annexe A — Glossaire](10-annexes/01-annexe-a-glossaire.md)
    - [Annexe B — Typologie des espaces dark web](10-annexes/02-annexe-b-typologie-des-espaces-dark-web.md)
    - [Annexe C — OPSEC analyste : checklists](10-annexes/03-annexe-c-opsec-analyste-checklists.md)
    - [Annexe D — Outils d'investigation dark web](10-annexes/04-annexe-d-outils-d-investigation-dark-web.md)
    - [Annexe E — Grille d'évaluation de crédibilité](10-annexes/05-annexe-e-grille-d-evaluation-de-credibilite.md)
    - [Annexe F — Templates de livrables](10-annexes/06-annexe-f-templates-de-livrables.md)
    - [Annexe G — Ressources et veille](10-annexes/07-annexe-g-ressources-et-veille.md)
