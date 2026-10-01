---
title: Chapitre 76 — Désinformation, influence et guerre cognitive
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - 'PARTIE X — Passerelles spécialisées : FININT, Crypto, CTI, Influence'
  - index.md
---

## 76.1 La désinformation comme objet OSINT

La **désinformation** et les **opérations d'influence** sont devenues des objets centraux d'investigation OSINT. Volume massif, sophistication croissante (IA generative, deepfakes), enjeux politiques majeurs.

## 76.2 Typologie

**Misinformation.** Information fausse diffusée sans intention de nuire (erreur, rumeur).

**Disinformation.** Information fausse diffusée avec intention de nuire (manipulation délibérée).

**Malinformation.** Information vraie diffusée pour nuire (doxxing, fuites sélectives).

## 76.3 Coordinated Inauthentic Behavior (CIB)

**CIB** (terme Meta). Activités coordonnées simulant des opinions ou réactions organiques.

Voir Ch.35 pour méthodologie détaillée.

## 76.4 Amplification et narratifs

**Amplification.**

- Bots et faux comptes.
- Cluster de retweets / partages.
- Trolls coordonnés.
- Médias relais (sympathisants idéologiques ou agents).

**Narratifs.**

- Histoire dominante propagée.
- Cohérence à travers comptes apparemment indépendants.
- Variations adaptées par audience.

## 76.5 Faux médias et faux experts

**Faux médias.** Sites imitant médias établis (Doppelgänger : imitation Le Monde, Bild, Welt, etc.).

**Faux experts.** Profils synthétiques (photo IA, bio fictive) présentés comme experts dans des domaines pour donner crédibilité.

**Cas d'usage MIRAGE.** Le faux média `info-finance-eu.com` créé pour amplifier le narratif diffamatoire contre Berthier.

## 76.6 Acteurs de référence à connaître

**Internet Research Agency (IRA, Russie).** Active 2014-2024. Saint-Pétersbourg.

**Doppelgänger (Russie).** Faux médias imitant Le Monde, Bild, etc. Documenté VIGINUM 2024.

**Spamouflage (Chine).** Campagnes pro-PRC sur X, YouTube, Facebook.

**Indian Chronicles (Inde, EU DisinfoLab 2019-2020).** 750+ faux médias.

**Storm-1516** (Russie, MS Threat Intelligence). Operations 2024-2026.

## 76.7 Méthodes de détection

Voir Ch.35 pour détail.

**Récap.**

- Cadence et patterns temporels.
- Réseaux d'amplification (Gephi).
- Narratifs convergents.
- Coordination de hashtags.
- Photos générées par IA.
- Métadonnées techniques (registrar, hosting).
- Infrastructure partagée (GA, tracker).

## 76.8 Cadre français : VIGINUM

**VIGINUM** (Service de vigilance et protection contre les ingérences numériques étrangères, SGDSN). Mission : détecter et caractériser les phénomènes inauthentiques affectant le débat public numérique.

**Publications.** Rapports techniques publics (notamment sur Doppelgänger).

**Coopération.** Avec acteurs européens, EU DisinfoLab.

## 76.9 Cadre européen : EEAS et DSA

**EEAS** (European External Action Service). EUvsDisinfo : monitoring désinformation Russie.

**DSA** (Digital Services Act 2024). Obligations plateformes sur modération, transparence, accès chercheurs.

## 76.10 Cas d'usage MIRAGE

Le volet désinformation MIRAGE intègre :

- Cluster 8 comptes X coordonnés.
- Cluster 9 canaux Telegram.
- 2 faux médias (`verites-technovert.com`, `info-finance-eu.com`).
- 3 fausses photographies (face swap + stock).
- 1 vidéo deepfake.
- Possible coordination via canal Telegram « social media boost » identifié.

**Attribution.** Cohérence d'éléments : narratifs convergents, infrastructure partagée (GA partagé), timing coordonné. **Attribution à Delaunay** : indirecte. Pas de lien direct identifiable Delaunay → service de désinformation. Cohérence d'intérêt (Delaunay cible Berthier qui l'a dénoncé). **Cotation B3** sur l'attribution à Delaunay : cohérent, non démontré, à approfondir judiciairement.

## 76.11 Cas Doppelgänger : étude détaillée

**Doppelgänger** (2022-2026, en cours) est l'opération d'influence russe la plus médiatisée depuis l'invasion de l'Ukraine. Documentée VIGINUM 2024, EU DisinfoLab, Recorded Future.

**Méthodologie.**

- Clonage de sites de médias établis (Le Monde, Bild, Welt, The Guardian, Fox News, etc.) avec domaines typosquattés.
- Production massive d'articles favorables à narratifs pro-russes.
- Diffusion via Twitter/X, Facebook, et notamment Telegram canaux russes.
- Amplification par bots et comptes coordonnés.

**Volume.** Plus de 1000 domaines typosquats identifiés. Production mensuelle de centaines d'articles. Touches multiples langues : anglais, français, allemand, espagnol, polonais, italien, hébreu.

**Attribution.** Selon rapports US Treasury 2024 et UE Sanctions, opérée par sociétés russes Structura National Technology et Social Design Agency, liées au Kremlin.

**Indicateurs détectables.**

- Domaines typosquattés enregistrés en lot.
- Infrastructure d'hébergement commune (analyses passives DNS).
- Patterns linguistiques (traductions automatiques détectables).
- Coordination temporelle de publication.
- Cross-amplification entre comptes connus pro-russes.

## 76.12 Cas Spamouflage : étude détaillée

**Spamouflage** (aussi appelé Dragonbridge par Mandiant) est l'opération d'influence chinoise documentée depuis 2017, intensifiée 2019-2026.

**Méthodologie.**

- Volume massif de faux comptes sur YouTube, Twitter/X, Facebook, TikTok.
- Production en masse de contenu vidéo, infographies, articles.
- Targets : sujets sensibles à Beijing (Hong Kong, Taïwan, Xinjiang, COVID origines).
- Adaptations linguistiques multiples.

**Volume.** Centaines de milliers de comptes identifiés sur durée. Plateformes ont supprimé par vagues (Twitter en 2019, 2020, 2021 ; YouTube régulier ; Meta).

**Faiblesses opérationnelles** documentées :

- Erreurs linguistiques (traduction faible).
- Bots peu sophistiqués (cadence anormale, photos volées).
- Amplification mutuelle artificielle (faible engagement organique).

**Documentation.** Graphika rapports successifs, Stanford Internet Observatory, Microsoft Threat Analysis Center, Mandiant.

## 76.13 Cas Storm-1516 : opérations 2024-2026

**Storm-1516** (Microsoft Threat Intelligence). Opération russe identifiée à partir de 2024.

**Caractéristiques.**

- Production de fausses vidéos « whistleblower » prétendument issues d'institutions ukrainiennes ou occidentales.
- Utilisation marquée de **deepfakes audio-vidéo** (IA générative).
- Cibles : élections, soutien à l'Ukraine.
- Distribution multi-plateformes.

**Sophistication.** Storm-1516 marque la **maturation de l'usage IA dans les opérations d'influence**. Distinction avec opérations précédentes : moins de comptes-zombies, plus de production de contenu synthétique convaincant.

**Pour OSINT.** Cas d'étude pour détection deepfakes (Partie VIII du cours). Outils : Sensity, Intel FakeCatcher, analyse contextuelle. Attribution par Microsoft / partenaires.

## 76.14 Méthodologie de détection de campagne CIB

**Étape 1 — Identification du signal.** Pic anormal de mentions sur sujet. Patterns inhabituels.

**Étape 2 — Cartographie.** Liste des comptes / domaines / canaux. Taille du cluster.

**Étape 3 — Analyse temporelle.** Heatmap d'activité. Coordination détectable.

**Étape 4 — Analyse de profils.** Photos IA, bios génériques, dates de création groupées.

**Étape 5 — Analyse de contenu.** Narratifs convergents. Indices LLM-generated.

**Étape 6 — Analyse de réseau.** Communautés détectées (Gephi Louvain). Nœuds pivots.

**Étape 7 — Analyse d'infrastructure.** Pour les domaines : registrar commun, hosting, trackers partagés.

**Étape 8 — Hypothèses d'attribution.** Acteur étatique ? Officine privée ? Concurrent ? Activiste authentique amplifié ?

**Étape 9 — Cotation et formulation.** Prudence sur attribution finale. Faisceaux d'indices.

**Étape 10 — Signalement / publication.** Plateformes, VIGINUM si applicable, communauté (EU DisinfoLab, Information Laundromat).

## 76.15 Contre-mesures et résilience

Pour une organisation visée par campagne de désinformation :

**Détection.**

- Monitoring proactif des mentions (Brandwatch, Talkwalker).
- Veille sur acteurs connus.
- Alertes sur nouvelles campagnes.

**Documentation.**

- Captures et préservation rigoureuse.
- Analyse forensique des contenus.
- Documentation des liens entre acteurs.

**Réponse.**

- Signalement aux plateformes (X, Meta, Telegram, YouTube).
- Communication factuelle ciblée (pas amplification du narratif).
- Action judiciaire si caractérisée (diffamation, atteinte à l'image).
- Plainte VIGINUM si caractère étatique étranger.

**Résilience long terme.**

- Surveillance continue.
- Construction d'une « bande son » authentique (présence médiatique légitime).
- Formation des porte-paroles.

## 76.16 Économie de la désinformation à louer

Un marché émergent : **désinformation as a service**. Officines proposent campagnes coordonnées clés en main.

**Acteurs documentés.**

- **Team Jorge** (Israël) : révélé par Forbidden Stories 2023. Campagnes ciblées politiques et corporates.
- **Cambridge Analytica** (UK, fermée 2018) : historique. Manipulation Brexit, Trump.
- **Officines russes** : Internet Research Agency (Prigozhin, dissoute 2024), Social Design Agency (Doppelgänger).
- **Officines diverses** au Moyen-Orient, Inde, Asie du Sud-Est, Afrique.

**Pour OSINT.** L'attribution à une officine commerciale (par opposition à étatique) est elle aussi complexe. Indicateurs : qualité technique commerciale, ciblage économique vs politique, mode opératoire.

## 76.17 Référentiels et bibliographies

**Référentiels CIB / désinformation 2026.**

- **DISARM Framework** (anciennement AMITT). Framework communautaire pour catégoriser désinformation, équivalent MITRE ATT&CK pour info-ops.
- **NATO StratCom Centre of Excellence** (Riga). Rapports techniques.
- **VIGINUM rapports** (France).
- **EU DisinfoLab** publications.
- **Stanford Internet Observatory** études.
- **Graphika** rapports CIB.
- **First Draft / Meedan** ressources fact-checking.

> **MIRAGE — Épisode 17 : Campagne d'influence coordonnée**
>
> L'analyste synthétise le volet désinformation.
>
> **Architecture identifiée.**
> 1. Cluster X : 8 comptes coordonnés (création septembre-octobre 2025, activité concentrée sur diffamation Berthier).
> 2. Cluster Telegram : 9 canaux retweetant et amplifiant.
> 3. Faux médias : `verites-technovert.com` + `info-finance-eu.com`, Google Analytics partagé.
> 4. Fausses photographies : 3 face swap sur backgrounds Unsplash/Pexels.
> 5. Vidéo deepfake : audio-vidéo composite avec voice cloning.
> 6. Possible prestataire : canal Telegram `@socialmedia_boost_fr` propose explicitement ce type de service (cohérence des prix, timing).
>
> **Narratif central.** « Berthier est un employé malveillant ayant manipulé les comptes pour nuire à TechnoVert ».
>
> **Cohérence temporelle.** Démarrage octobre 2025 (1 mois après licenciement Berthier). Pic en mars 2026 (avant audience prud'homale).
>
> **Attribution.**
> - Lien direct au commanditaire (Delaunay ou entourage TechnoVert) : non démontré directement.
> - Cohérence d'intérêt : forte (Berthier est le lanceur d'alerte des écritures suspectes liées à Delaunay).
> - Cohérence temporelle : forte.
> - Cotation B3 sur attribution à Delaunay : hypothèse cohérente, démonstration à approfondir judiciairement.
>
> **Pour le rapport.** « Une campagne de désinformation coordonnée a été identifiée, ciblant Antoine Berthier, lanceur d'alerte, articulée sur 8 comptes X, 9 canaux Telegram, 2 faux médias, 3 photographies fabriquées, 1 vidéo deepfake. La cohérence temporelle et thématique de cette campagne avec les intérêts de Marc Delaunay (mis en cause par le signalement Berthier) suggère un lien d'attribution probable, sans démonstration directe en sources ouvertes. Une expertise complémentaire dans le cadre judiciaire (réquisitions opérateurs Telegram et registrars) permettrait l'attribution formelle. »

-----
