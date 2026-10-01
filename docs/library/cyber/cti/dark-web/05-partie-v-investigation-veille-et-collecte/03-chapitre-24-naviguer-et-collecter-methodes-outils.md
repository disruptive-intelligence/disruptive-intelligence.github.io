---
title: 'Chapitre 24 — Naviguer et collecter : méthodes, outils, limites'
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

Aspect pratique : comment on navigue effectivement sur le dark web, quels outils on utilise, et quelles sont les limites techniques et méthodologiques.

## 24.1 L'outillage de base

**Tor Browser** : navigateur de référence. Basé sur Firefox ESR, hardened, en mode Safest pour l'investigation. À télécharger **uniquement** depuis torproject.org (ou ses miroirs officiels).

**Tails** : distribution Linux live. Démarre sur clé USB, ne laisse aucune trace sur la machine. Recommandée pour les investigations les plus sensibles.

**Whonix** : architecture en deux VM (Gateway + Workstation). Isolation forte. Recommandée pour setup permanent d'investigation.

**Qubes OS** : système d'exploitation avec isolation par VM (AppVMs). Très sécurisé mais courbe d'apprentissage plus raide.

**VM dédiée dans VMware/VirtualBox** : alternative accessible si Whonix est trop lourd. Clone de l'OS avant chaque session, restauration post-session.

**Outils complémentaires** :

- **curl / wget via Tor** (torify) : récupération en ligne de commande.
- **OnionScan** : audit automatique de services .onion pour failles OPSEC.
- **tsocks / proxychains** : chaînage de proxies.
- **Aquatone, Eyewitness** : capture automatisée de screenshots en masse.
- **Hunchly** : outil commercial de capture structurée d'investigation (horodatage, archivage, notes).
- **Maltego** : graphing des relations entre entités (avec transformations spécifiques dark web).

## 24.2 Les sources et points d'entrée

**Comment trouve-t-on des .onion** ?

**Listes communautaires**. The Hidden Wiki (multiple instances, pas toutes fiables), Dark.fail, Tor.taxi. Ces listes sont **partielles et partiellement scam-compromised** — ne jamais cliquer aveuglément.

**Moteurs de recherche .onion**. Ahmia, Torch, Haystak, Excavator. Indexation **très partielle** du contenu .onion. Utile pour des recherches spécifiques, mais rarement exhaustif.

**Cross-references depuis forums**. Les forums mentionnent d'autres forums, marchés, canaux. Documentation par ce biais — plus fiable que les listes car vouchées par la communauté.

**Canaux Telegram**. Beaucoup d'acteurs postent leurs adresses .onion sur Telegram, ce qui les rend plus facilement découvrables. Surveiller les canaux pertinents.

**Services de monitoring commerciaux**. Recorded Future, SOCRadar, Flashpoint, Flare, Intel471, DarkOwl, Cybersixgill — tous maintiennent des bases d'entités dark web crawlées. Accès via abonnement entreprise.

**OSINT public**. Articles de presse, papers académiques, rapports vendors — regorgent de mentions d'adresses .onion qui ont fait l'actualité.

## 24.3 La collecte structurée

**Capture vs simple navigation**. La collecte doit être **structurée**, pas simple navigation. Capturer systématiquement :

- **URL complète** visitée.
- **Horodatage précis** (timestamp avec seconde, fuseau horaire).
- **Capture d'écran** du contenu.
- **HTML source** sauvegardé.
- **Hash** du contenu sauvegardé.
- **Pseudonyme utilisé** pour la session.

**Archivage**. Plusieurs options :

- **Hunchly** : outil commercial qui automatise capture + organisation + horodatage.
- **Archivage manuel** : dossiers structurés, nommage convention (YYYYMMDD-HHMMSS-source-description), fichiers immutables.
- **Container cryptographiquement signé** : après collecte, générer un hash global du dossier, horodater, signer (GPG), stocker en immutable.

**Organisation**. Par cas d'investigation, par source, par date. Éviter le « one big folder » — impossible à remonter après 6 mois.

## 24.4 Les challenges techniques

**Lenteur du réseau Tor**. Navigation 5-10× plus lente que clearnet. Planifier des sessions d'investigation longues, éviter la multitâche excessive.

**Disponibilité intermittente des .onion**. Un site .onion peut être down pour heures ou jours. Tenter plusieurs fois, utiliser des mirrors (si connus), noter les patterns de disponibilité.

**DDoS permanents**. Les grands forums sont régulièrement DDoSés. Les pages chargent lentement, partiellement, ou pas du tout. Les meilleures heures d'investigation sont souvent les créneaux nocturnes (fuseau horaire attaquant).

**CAPTCHA pervasifs**. Pour limiter le scraping, beaucoup de sites .onion implémentent CAPTCHAs difficiles, parfois impossibles pour des outils automatisés.

**Protections anti-scraping**. Limites de requêtes, défis JS, tokens de session, fingerprinting — rendent la collecte automatisée complexe.

**Sites éphémères**. Un forum peut déménager d'adresse .onion sans préavis. Une capture d'il y a 6 mois peut pointer vers un site disparu. Les archives ont donc une valeur disproportionnée sur le dark web.

## 24.5 Les limites méthodologiques

**Biais de survivance**. Ce qu'on observe est ce qui existe actuellement. Les acteurs qui disparaissent ne sont plus observables. Les forums saisis ne sont plus accessibles (sauf archives). L'image du dark web à un instant T est partielle et biaisée vers les survivants.

**Biais de visibilité**. Les acteurs les plus sophistiqués sont souvent les moins visibles. Un APT étatique n'a pas besoin d'un leak site flashy — il opère discrètement. Les acteurs observables sur forums publics sont majoritairement de profil intermédiaire.

**Biais de représentation**. L'analyste observe à travers les forums qu'il connaît. L'écosystème russophone, chinois, arabophone, persan ont chacun leurs dynamiques propres, partiellement accessibles selon les compétences linguistiques de l'équipe.

**Biais de fraîcheur**. Les données anciennes disparaissent. Un forum actif il y a 2 ans peut être invisible aujourd'hui. L'histoire du dark web est partiellement perdue.

**Biais d'accès**. Les zones premium des forums (souvent les plus intéressantes analytiquement) nécessitent paiement, vouching, tenure. Un analyste privé n'a pas toujours les moyens d'accéder à toutes les zones utiles.

## 24.6 Automatisation et échelle

**Scraping automatisé** : possible mais difficile. Les protections anti-bot sont fortes. Nécessite infrastructure (plusieurs instances Tor, rotation d'identités), résilience (retry logic, gestion erreurs), légalité (certains ToS interdisent scraping même sur sites criminels).

**Plateformes commerciales** : outils SaaS qui font le crawling à grande échelle et exposent les résultats via API. Recorded Future, DarkOwl, Flare, Intel471, Cybersixgill. Coût : 50 k - 500 k USD/an selon scale.

**Open source** : quelques projets open source (OnionScan, TorBot, Dark-Scrape) mais moins robustes que solutions commerciales.

**Approche hybride** : scraping ciblé sur sources prioritaires + plateforme commerciale pour couverture large + veille humaine pour les signaux faibles.

## 24.7 Fil rouge — DARKSTREAM : l'accès à IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 13 : setup et navigation**
>
> Lucas utilise son environnement Whonix avec Tor Browser Safest. Accès initial à IndustrialLeaks via l'adresse .onion communiquée par le partenaire vouching. Vérification de l'adresse : 56 caractères, cross-check sur 2 sources indépendantes (mention dans un post Recorded Future + mention sur un forum russophone peer).
>
> Navigation lente — 2-3 secondes par clic. Le forum affiche un CAPTCHA proof-of-work (JS requis à minima pour le CAPTCHA). Lucas active JS **uniquement pour la page de login**, puis le désactive après. Session de navigation active, avec Hunchly en background pour capture systématique.
>
> Exploration structurée :
> 1. Captures de toutes les catégories publiques (arborescence du forum).
> 2. Lecture et capture du post aero_source + tous les posts du même user.
> 3. Navigation aux autres vendeurs du mois, pour profiling comparatif.
> 4. Règles du forum (capture).
> 5. Statistiques visibles (nombre de membres, posts, transactions).
>
> Cycle de 3 heures. 147 pages capturées, structurées par dossier. Hash du corpus calculé. Persona « mapletech » affiche activité cohérente (quelques réponses en threads, aucun message offensif, aucune tentative de solliciter info sensible au-delà de ce qui est publiquement affiché).
>
> Post-session, Lucas produit un **mémo d'observations** : architecture du forum, profils de vendeurs actifs, posts d'intérêt, observations sur aero_source. Ce mémo alimente le dossier DARKSTREAM et permet aux autres membres de l'équipe Athéna d'orienter leurs propres recherches sans re-naviguer manuellement.

---
