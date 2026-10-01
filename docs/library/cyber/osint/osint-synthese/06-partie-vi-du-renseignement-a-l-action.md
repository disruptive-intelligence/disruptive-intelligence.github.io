---
title: Partie VI — Du renseignement à l'action
source: Cyber/02 OSINT/OSINT — synthèse.md
note: OSINT — synthèse
up:
- - OSINT — synthèse
  - index.md
---

*Transformer l'investigation en livrables exploitables — le rapport, le cadre judiciaire, la veille, la désinformation, et l'adaptation de la méthode aux contextes spécifiques.*

---


## Chapitre 21 — Rédaction du rapport d'investigation OSINT

La structure du rapport professionnel : **sommaire exécutif** (1 page pour le décideur — conclusions, confiance, recommandations critiques), **mandat et périmètre**, **méthodologie et sources** (transparence totale), **constatations** (chaque fait avec source, date, cotation A-F/1-6, capture horodatée en annexe), **analyse** (ACH, timeline, inférences), **conclusions** (réponse aux questions d'investigation avec niveau de confiance — « les éléments sont compatibles avec... » pas « il est coupable de... »), **recommandations** (pistes, réquisitions), **annexes** (captures hashées, graphes, timelines).

Le **graphe relationnel** (la visualisation la plus impactante pour le client). La **timeline** (le « quand » de chaque événement). Le **vocabulaire calibré** (renseignement ≠ verdict — le rapport fournit du renseignement, le tribunal établit la culpabilité).

---


## Chapitre 22 — OSINT et investigation judiciaire

Investigateur privé vs LEA : le privé fait l'OSINT en sources ouvertes, les LEA font les réquisitions (opérateurs télécom, plateformes, banques), interceptions, perquisitions, auditions, gel d'actifs. Le rapport OSINT fournit la trame investigative, les autorités complètent avec les moyens légaux.

La transmission : format exploitable par les enquêteurs, preuves préservées (hash, horodatage, chaîne de custody), pistes de réquisitions identifiées (quelles données, à quel opérateur, pour quel motif). Le dépôt de plainte (procureur, services spécialisés — C3N cyber, OCLCTIC criminalité financière, JUNALCO crime organisé). L'expertise judiciaire OSINT (expert mandaté par un magistrat, cadre contradictoire, rapport à valeur probante).

---


## Chapitre 23 — Veille opérationnelle et monitoring continu

La veille post-rapport : le suspect tente de supprimer des preuves (dissolution de sociétés, passage en privé, suppression de contenus) → l'archivage anticipé protège. Les outils de monitoring : alertes Google (noms, sociétés), monitoring DNS/Whois (SecurityTrails), monitoring réseaux sociaux (Mention, Brand24 — exemples à date), monitoring dark web/Telegram. La collecte en temps réel (surveillance d'événement en cours — agrégation X, Telegram, médias, webcams). Le geofencing (publications géolocalisées dans une zone). La coordination d'équipe (répartition, fusion, déconfliction).

> **🎯 MIRAGE — Épisode 9 :** Semaine 3 post-rapport. Alerte Google : dissolution volontaire de Delta Consulting Ltd (Malte). Le suspect tente de faire disparaître la structure avant les autorités. Capture immédiate (Hunchly). Le profil Instagram marc_del75 passe en privé — captures déjà réalisées. Le blog antiwhistleblower.com est mis hors ligne — Wayback Machine conserve le contenu.

---


## Chapitre 24 — Désinformation, influence et fact-checking

*Ce chapitre enseigne la détection et l'investigation de la désinformation comme compétence OSINT opérationnelle — pas comme un résumé académique.*

La **détection de faux comptes** : signaux (création récente, nom générique ou généré, photo AI-generated ou volée — recherche inversée, peu de publications originales, activité coordonnée, ratio followers/following anormal). L'**analyse de réseau coordonné** : les faux comptes interagissent entre eux et partagent les mêmes contenus dans les mêmes fenêtres temporelles (±5 minutes) → le réseau est identifiable par les patterns d'interaction et de timing. L'**analyse d'infrastructure** : les liens partagés pointent vers des domaines enregistrés récemment, souvent le même jour, hébergés sur la même infrastructure → DNS/Whois révèle les liens.

L'**attribution** : relier les faux comptes à leur opérateur (infrastructure — les domaines sont enregistrés avec un email identifiable, patterns linguistiques, fuseaux horaires). Le **fact-checking** : vérification de l'image originale (TinEye — recyclage), vérification géographique (Street View), vérification temporelle (archives météo), vérification de source (le média cité existe-t-il ? l'expert a-t-il dit ce qu'on lui attribue ?).

**Limites :** l'attribution de campagnes de désinformation est intrinsèquement incertaine — les opérateurs utilisent des VPN, des domaines jetables, et des identités multiples. Un réseau de faux comptes coordonnés est un signal fort, mais l'attribution au commanditaire final nécessite souvent des preuves que seules les LEA peuvent obtenir (réquisitions aux plateformes, aux registrars). **Risque :** accuser publiquement un acteur de désinformation sans preuves solides = diffamation potentielle.

> **🎯 MIRAGE — Épisode 10 :** Blog antiwhistleblower.com — Whois historique → email de création marc.consulting@proton.me, même email dans le SPF de deltaconsulting.mt. Lien Delaunay → blog établi. 8 faux comptes Twitter amplifient le blog — création le même jour, photos AI-generated, patterns de publication identiques. Campagne documentée.

---


## Chapitre 25 — Adapter la méthodologie OSINT aux contextes spécialisés

*Ce chapitre ne liste pas des domaines — il montre comment la même méthodologie OSINT s'adapte à différents contextes, ce qui change et ce qui reste constant.*

### 25.1 Le noyau méthodologique invariant

Quel que soit le contexte (financier, criminel, géopolitique, corporate), le cycle du renseignement reste le même (orientation → collecte → traitement → analyse → diffusion), la logique du pivot reste la même (un sélecteur mène à un autre), la cotation de fiabilité reste la même (A-F/1-6), et la discipline de vérification reste la même (corroboration multi-sources, ACH). Ce qui change, c'est le **focus des sources**, les **types de sélecteurs prioritaires**, et les **red flags spécifiques** au domaine.

### 25.2 Les adaptations par contexte

L'**investigation financière/compliance** (KYC/AML, due diligence) : les sources prioritaires sont les registres d'entreprises, les comptes publiés, les listes de sanctions, et les leaks ICIJ. Le sélecteur prioritaire est la société (pas la personne — on part de la structure pour remonter à l'individu). Les red flags sont les montages multi-juridictions, les nominees, et les flux incohérents. L'erreur courante est de conclure « suspect » sur la base d'une seule société offshore sans autre élément.

L'**investigation criminelle** (personnes disparues, traite, extrémisme) : les sources prioritaires sont les réseaux sociaux (SOCMINT intensive), les messageries (Telegram, WhatsApp), les archives de données (Wayback Machine pour les profils supprimés). Le sélecteur prioritaire est la personne (dernier lieu connu, dernières connexions, réseau social). La spécificité est la dimension humanitaire (Trace Labs pour les personnes disparues) ou la dimension sécuritaire (surveillance de la radicalisation). L'erreur courante est de confondre un individu radicalisé en ligne avec un individu qui passe à l'acte — le discours n'est pas l'action.

L'**investigation conflits/géopolitique** (méthodologie Bellingcat) : les sources prioritaires sont l'imagerie satellite (Sentinel-2, Google Earth historique), les vidéos géolocalisées (GEOINT), et les bases de données de mouvements (FlightRadar24, MarineTraffic). Le sélecteur prioritaire est le lieu et le temps (pas la personne). La spécificité est la chronolocation et la vérification d'authenticité (Ch.13-14). L'erreur courante est de prendre une vidéo virale pour argent comptant sans vérifier le lieu, la date et l'authenticité.

L'**investigation réputationnelle** (e-réputation, défense) : les sources prioritaires sont les moteurs de recherche (Google — ce que les gens voient en premier), les réseaux sociaux (mentions, tags), et les avis en ligne. Le sélecteur prioritaire est le nom de la personne/marque. La spécificité est le volet défensif (droit à l'oubli RGPD, suppression de données personnelles, nettoyage de résultats).

---
