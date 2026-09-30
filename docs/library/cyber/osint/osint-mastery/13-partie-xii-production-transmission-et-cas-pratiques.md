---
title: PARTIE XII — Production, transmission et cas pratiques
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 13
chapters: 15
---

> **Ce que cette partie apprend.** Produire les livrables OSINT dans toute leur diversité (note courte, rapport complet, fiches opérationnelles, rapport judiciaire et précontentieux), maîtriser la diffusion (TLP, confidentialité), capitaliser dans la durée, et appliquer la méthodologie à neuf cas pratiques couvrant tout le périmètre du master, plus un exercice final non guidé avec son corrigé.
>
> **Ce qu'elle ne couvre pas.** Les passerelles spécialisées (Partie X), couvertes par les cours dédiés.
>
> **Ce que vous saurez faire après cette partie.** Produire un livrable OSINT professionnel et défendable à tous les formats utiles. Conduire de bout en bout un cas complexe en autonomie.

-----

### Chapitre 87 — Note courte OSINT

#### 87.1 La note courte : format de référence quotidien

La **note courte** est le format de référence pour communiquer rapidement un résultat OSINT à un commanditaire ou à une hiérarchie. Elle existe sous plusieurs formes selon les contextes : note de renseignement militaire (RM) dans les armées, brève dans la presse, alerte CTI dans la cybersécurité, note flash en cabinet de conseil.

Elle a en commun **brièveté**, **calibration**, **structure stable**. Une note courte rate sa cible si :
- elle se perd en contexte au lieu d'aller au fait ;
- elle sur-affirme ce que l'évidence ne soutient pas ;
- elle empile sans hiérarchiser ;
- elle masque les limites pour paraître plus convaincante.

#### 87.2 Structure standard de la note courte

Une note courte type comporte **5 sections** stables :

1. **En-tête identifiant.**
2. **BLUF (Bottom Line Up Front).**
3. **Contexte / cadrage minimal.**
4. **Faits saillants cotés.**
5. **Limites et recommandation.**

Une page A4, 400-700 mots, lisibilité en 3 minutes. Le destinataire saisit l'essentiel sans avoir à lire toute la note.

#### 87.3 En-tête identifiant

L'en-tête doit fournir en un coup d'œil :
- **Titre** clair et neutre.
- **Auteur** (cellule, signature ou identifiant).
- **Date** d'émission.
- **Référence interne** (numéro de dossier).
- **Diffusion / classification** (TLP, RGPD si données personnelles, confidentialité contractuelle).
- **Sujet** (entité concernée).
- **Niveau de confiance global** (probable / possible / quasi-certain / indéterminable).

L'en-tête sert aussi de **traçabilité** : retrouvable dans un système d'archivage, lié à un mandat précis.

#### 87.4 BLUF : la conclusion en première ligne

Le **BLUF** (Bottom Line Up Front) est l'usage militaire qui place la **conclusion** en tête. Le lecteur lit d'abord ce qui est conclu, puis lit les justifications.

**Exemple BLUF court.**

> **BLUF.** Les recherches effectuées sur la société Verde Holdings (Chypre) confirment son immatriculation, sa direction par Marc Delaunay et Marina Constantinidou, et son lien probable avec un montage offshore impliquant Delta Consulting Ltd (Malte) et TechnoVert SAS. Niveau de confiance : probable. Approfondissement et expertise complémentaires recommandés.

Le BLUF est calibré : « probable », pas « prouvé ». Il intègre la recommandation, pas seulement le constat. Il pose les enjeux : à lui seul, il informe.

#### 87.5 Contexte / cadrage minimal

**Cadrage** = pourquoi cette note, pour qui, dans quel mandat, avec quelles questions de renseignement.

**Exemple.**

> Note produite à la demande du cabinet Legrand & Associés (mandat 2026-05-16) dans le cadre d'une enquête de due diligence préalable à audit forensique sur la société TechnoVert SAS. La présente note concerne les volet « structures offshore » et « bénéficiaire effectif » du dossier global MIRAGE.

Cadrage = 2-5 lignes. Pas de remplissage. Le destinataire connaît son mandat.

#### 87.6 Faits saillants cotés

**Cœur de la note.** Liste structurée des faits clés, chacun avec sa cotation.

**Format recommandé.**

| Fait | Source | Cotation |
|---|---|---|
| Verde Holdings est immatriculée à Chypre depuis 01/2022 | Companies Registry CY | A1 |
| Marc Delaunay est administrateur déclaré et UBO 100 % | Registre UBO CY (accès partiel) | A1 |
| Marina Constantinidou est administratrice locale (probable nominee) | Cross-référence cabinets locaux | B2 |
| Verde a reçu des flux entrants depuis Delta Consulting Ltd | Cyprus Confidential (ICIJ leak) | B2 |
| Aucune sanction / PEP active | OpenSanctions | A1 |

Chaque fait est :
- **précisément formulé** (pas de généralité vague),
- **sourcé** (clic possible vers la source archivée),
- **coté** Admiralty,
- **autonome** (lisible isolément).

#### 87.7 Limites et recommandations

**Limites.**

> - L'accès au registre UBO chypriote est restreint depuis 2022 (arrêt CJUE). Les éléments retenus s'appuient sur la portion accessible et sur Cyprus Confidential. Une réquisition judiciaire permettrait l'accès complet.
> - L'analyse des flux financiers réels reste hors périmètre OSINT (comptes consolidés non publiés au-delà des obligations légales chypriotes).
> - L'attribution effective des bénéfices économiques de Verde reste à confirmer par audit comptable forensique.

**Recommandations.**

> - Inscrire Verde Holdings dans la procédure en cours et solliciter, dans le cadre judiciaire, les pièces complètes au registre chypriote.
> - Mandater expertise comptable forensique sur les comptes consolidés TechnoVert (2020-2025) pour identifier les écritures cohérentes avec flux vers Delta puis Verde.
> - Sécuriser l'archive des captures réalisées (en annexe), aux fins de cohérence en cas de procédure.

La note courte se termine par **action attendue** explicite, jamais en l'air.

#### 87.8 Cas d'usage de la note courte

**Note flash quotidienne.** Cellule de veille qui transmet à la direction l'élément du jour.

**Briefing matinal.** Avant une réunion, synthèse d'une recherche.

**Note d'alerte.** Élément critique nécessitant attention immédiate (un dirigeant cible vient d'être placé sur liste de sanctions, par exemple).

**Note préparatoire.** Avant une audition, négociation, ou démarche, synthèse de l'état des connaissances.

**Note de transition.** Passage de relai entre analystes (départ en congés, fin de mission, escalade).

#### 87.9 Variantes spécialisées

**Note CTI.** Format STIX/TAXII si transmise machine-to-machine. Sinon, version humaine adaptée : IOCs, TTPs, attribution, action recommandée.

**Note judiciaire.** Plus formelle (Ch.90). Vocabulaire calibré pour magistrat.

**Note de presse / pour journaliste.** Plus pédagogique, moins de jargon, mais maintien rigueur.

**Note interne RSSI.** Concentrée sur action défensive (patches, monitoring, communications).

#### 87.10 Erreurs fréquentes à éviter

**Verbosité.** Étirer ce qui pourrait être dit en 3 lignes. Le destinataire perd le fil.

**Pas de BLUF.** Forcer le lecteur à lire la note pour trouver la conclusion.

**Sur-affirmation.** Pour paraître convaincant, formuler comme une certitude ce qui est probable. Carrière courte.

**Empilement sans hiérarchisation.** Liste de 30 faits sans poids relatif.

**Pas de cotation.** Le lecteur ne sait pas évaluer la fiabilité.

**Pas de limites.** Apparence de complétude pour masquer ce qui manque.

**Pas de recommandation.** Note descriptive sans valeur ajoutée actionnable.

#### 87.11 Lisibilité et accessibilité

Une note courte doit être **lisible par un non-spécialiste**. L'analyste maîtrise le sujet ; le destinataire ne le maîtrise pas nécessairement.

**Pratique.**
- Acronymes développés à la première occurrence.
- Glossaire bref si nécessaire (en bas de page ou annexe courte).
- Pas de jargon inutile.
- Schémas / tableaux pour ce qui se visualise mieux qu'il ne s'explique.

#### 87.12 Modèle de note courte MIRAGE — entité Verde Holdings

```
NOTE COURTE — OSINT MIRAGE
Sujet : Société Verde Holdings (Chypre)
Mandat : 2026-05-16, Cabinet Legrand & Associés
Auteur : Cellule MIRAGE
Date : 2026-05-XX
Référence interne : MIRAGE/N-014
Diffusion : TLP:AMBER (cabinet, magistrat saisissant uniquement)
Niveau de confiance global : probable

BLUF
Verde Holdings (Chypre) est confirmée comme société détenue 
intégralement par Marc Delaunay, recevant des flux entrants depuis 
Delta Consulting Ltd (Malte) elle-même alimentée probablement par 
TechnoVert SAS. Niveau de confiance : probable. Approfondissement 
judiciaire et expertise comptable forensique recommandés.

Cadrage
Note produite dans le cadre du mandat MIRAGE (cabinet Legrand & 
Associés). Volet investigué : structures offshore et bénéficiaire 
effectif. Périmètre : sources ouvertes exclusivement.

Faits saillants cotés
[tableau de 5-7 faits cotés, comme ci-dessus]

Limites
- Registre UBO chypriote partiellement accessible (post-CJUE 2022).
- Comptes Verde non publiés.
- Attribution effective des bénéfices à confirmer par audit.

Recommandations
- Inscrire Verde dans procédure et solliciter pièces officielles.
- Mandater expertise comptable forensique TechnoVert 2020-2025.
- Préserver captures (annexe disponible sur demande).

Annexes (sur demande)
- Captures Companies Registry CY (Hunchly).
- Capture Cyprus Confidential mémo (avec hash).
- Synthèse cluster offshore (graphe Maltego).

Signature et hash de cette note : [SHA-256]
```

#### 87.13 Synthèse

La note courte est l'**outil de communication quotidien** de l'analyste OSINT. Maîtrisée, elle économise du temps à tout le monde, inspire confiance, et trace l'activité de la cellule.

-----

### Chapitre 88 — Rapport OSINT complet

#### 88.1 Du flash au dossier

Un **rapport OSINT complet** est la formalisation finale d'une enquête de moyenne à longue durée. Là où la note courte tient sur une page, le rapport complet va de 10 à 100 pages selon la complexité, avec annexes pouvant ajouter autant.

Le rapport sert plusieurs publics : commanditaire opérationnel, hiérarchie, magistrat, expert tiers, archivage institutionnel. Il doit être **autonome** : un lecteur n'ayant pas participé à l'enquête doit pouvoir le comprendre intégralement.

#### 88.2 Structure type d'un rapport OSINT complet

**Section 0 — Page de garde.**
- Titre.
- Sujet.
- Mandat (numéro, commanditaire).
- Auteur (cellule, signataires).
- Date.
- Versioning et hash.
- Classification / TLP.
- Niveau de confiance global.

**Section 1 — Executive summary.**
1-3 pages. Lisible isolément. Inclut BLUF, points clés, recommandations principales.

**Section 2 — Cadrage du mandat.**
- Commanditaire et finalité.
- Périmètre et bornes.
- Questions de renseignement (IR).
- Cadre déontologique et légal.
- Limites posées.

**Section 3 — Méthodologie.**
- Sources mobilisées.
- Outils mobilisés (avec versions).
- Cotation utilisée (Admiralty + WEP).
- LLMs et IA mobilisées (avec garde-fous).
- OPSEC mise en œuvre.

**Section 4 — Analyse par question de renseignement (IR).**
Cœur du rapport. Une section par IR. Chaque section :
- Reformulation de l'IR.
- Faits saillants cotés.
- Analyse (ACH, raisonnement).
- Conclusion calibrée WEP.
- Limites et zones d'ombre.

**Section 5 — Synthèse intégrée.**
- Vue 360° (timeline + graphe résumé).
- Convergences et incohérences.
- Hypothèses retenues.
- Hypothèses concurrentes non retenues (mais documentées pour devil's advocate).

**Section 6 — Recommandations actionnables.**
- Actions immédiates.
- Approfondissements suggérés.
- Escalades nécessaires (judiciaire, expertise, cours spécialisés).
- Suivi recommandé.

**Section 7 — Limites globales.**
- Ce qui n'a pas pu être investigué.
- Ce qui resterait à investiguer.
- Risques d'erreur identifiés.

**Section 8 — Annexes.**
- Fiches d'entités.
- Matrices ACH.
- Timeline détaillée.
- Graphe d'enquête (export visuel).
- Catalogue de pièces avec hashes.
- Glossaire.
- Méthodologie détaillée.
- Cotation détaillée.

#### 88.3 Page de garde et versioning

La page de garde porte une **mention de version** explicite : « v1.0 — émission initiale », « v1.1 — correction faits saillants section IR3 », etc.

Tout rapport remis fait l'objet d'un **hash** (SHA-256) calculé sur le PDF / Word final. Le hash est consigné dans un journal interne. Cela permet de prouver, en cas de litige, que le rapport délivré au commanditaire est bien identique à celui archivé.

**Pratique.** Le hash peut être horodaté via OpenTimestamps (blockchain). Cela ajoute une preuve temporelle indépendante. Coût : nul.

#### 88.4 Executive summary : l'art de la synthèse

L'**executive summary** est probablement la partie la plus lue du rapport. C'est souvent **la seule** lue par la direction.

**Discipline.**
- 1 à 3 pages, jamais plus.
- BLUF immédiat.
- 5 à 10 points clés cotés.
- Niveau de confiance global explicite.
- Recommandations principales.
- Si le rapport identifie urgence, elle apparaît dans l'exec summary.

**Exemple structure.**

> 1. Conclusion principale (BLUF) — un paragraphe.
> 2. Points clés (bulleted, 5-10).
> 3. Niveau de confiance global et limites majeures.
> 4. Recommandations actionnables.

Si l'exec summary contient déjà tout l'essentiel, le rapport complet vient en **approfondissement** et **justification**. Cohérent avec BLUF.

#### 88.5 Cadrage du mandat : pourquoi c'est crucial

La **section cadrage** documente, parfois en plusieurs pages, le périmètre exact de l'enquête. Elle protège l'analyste : si une critique future porte sur ce qui n'a pas été investigué, le cadrage prouve que cette zone était hors mandat.

**Éléments.**
- Identité du commanditaire et de son représentant signataire.
- Date du mandat, durée prévue, livrables attendus.
- Finalité explicite (due diligence pré-investissement, soutien procédure pénale, intelligence économique, etc.).
- Périmètre géographique, temporel, thématique.
- Cible(s) explicitement nommée(s).
- Bornes (« ne sont pas dans le périmètre : … »).
- Questions de renseignement (IR), formulées comme questions fermées.
- Cadre légal applicable (juridictions concernées).
- Engagements déontologiques.

#### 88.6 Méthodologie : transparence

La **section méthodologie** est la signature de la rigueur. Elle décrit :
- Les sources publiques mobilisées (catégories, exemples).
- Les outils (avec leurs limites).
- Les processus de vérification (cotation, ACH, validation pair).
- L'usage des LLMs et IA, et garde-fous appliqués (Retrieve-Store-Cite).
- L'OPSEC mise en œuvre.

**Bénéfice.** Un magistrat ou expert lisant le rapport sait **comment** l'analyse a été conduite. C'est ce qui rend le rapport défendable.

**Exemple section méthodologie.**

> Cette enquête a mobilisé exclusivement des sources publiques (registres officiels, presse établie, médias accessibles, leaks journalistiques vérifiés, plateformes ouvertes). Aucune intrusion technique, aucune ingénierie sociale active, aucune surveillance d'individu n'a été conduite. Les outils suivants ont été utilisés : Pappers Pro (registres FR), OpenCorporates (cross-juridictions), OpenSanctions (sanctions / PEP), Hunchly (captures), Yandex / Google Lens / TinEye (recherche inversée), ExifTool (métadonnées), crt.sh (certificats), Sensity AI et Hive Moderation (détection IA), parmi d'autres listés en annexe outils. L'analyse a appliqué la cotation Admiralty (A-F / 1-6) sur chaque fait, et les niveaux de confiance WEP sur chaque conclusion. Des analyses de hypothèses concurrentes (ACH) ont été conduites sur les 5 questions de renseignement principales (matrices en annexe). L'usage des LLMs (Claude Opus 4.7, Llama 3.3 local) a été circonscrit aux tâches d'extraction et de synthèse, sans qu'aucune affirmation produite par LLM n'ait été intégrée au rapport sans vérification directe contre la source primaire (protocole Retrieve-Store-Cite). L'enquête a mis en œuvre une OPSEC stricte : VPN no-log, navigateurs cloisonnés (Tor, Brave, Firefox profils dédiés), captures Hunchly avec hash, archivage local chiffré (VeraCrypt).

Cette section installe la confiance. Tout magistrat instruit comprend la posture professionnelle.

#### 88.7 Analyse par IR

Le **cœur du rapport** est l'analyse par question de renseignement.

**Pour chaque IR.**

1. **Reformulation explicite.** L'IR est rappelée.
2. **Faits cotés.** Liste avec sources et cotations.
3. **Analyse.** Lecture des faits, mise en cohérence, identification des patterns.
4. **ACH résumé.** Si applicable, mention de la matrice (annexée).
5. **Conclusion calibrée.** WEP, formulation prudente.
6. **Limites et zones d'ombre.**

**Exemple structure d'une section IR.**

> **IR1.** Marc Delaunay détient-il, contrôle-t-il ou bénéficie-t-il de sociétés offshore non déclarées ?
>
> **Faits clés.**
> - Delta Consulting Ltd (Malte) : administrateur unique Marc Delaunay (A1).
> - Verde Holdings (Chypre) : Marc Delaunay administrateur et UBO 100 % (A1).
> - Cyprus Confidential mémo : structure documentée, flux entrants depuis Delta vers Verde (B2).
> - Aucune mention de ces entités dans déclarations françaises identifiables publiquement (D3).
>
> **Analyse.** Les éléments collectés documentent l'existence formelle de Delta et Verde, leur contrôle juridique par Delaunay, et un lien organique entre les deux structures. Le mémo Cyprus Confidential, leak journalistique vérifié par ICIJ, atteste qu'à l'époque considérée (2022), Verde recevait des flux depuis Delta. La non-déclaration en France de ces entités est cohérente avec l'usage juridictionnel offshore typique, sans que cela constitue à soi seul une preuve d'irrégularité fiscale.
>
> **Hypothèses concurrentes (ACH, voir annexe ACH-1).**
> - H1 (préférée) : Delaunay détient et bénéficie personnellement des structures offshore — fortement soutenue.
> - H2 : Delaunay est nominee pour un tiers réel — résiduellement possible.
> - H3 : Pas de lien réel — réfutée.
>
> **Conclusion.** Il est probable que Marc Delaunay détient et opère, depuis 2020, un dispositif de structures offshore composé de Delta Consulting Ltd et Verde Holdings, dont il est le bénéficiaire économique direct. La preuve définitive de bénéfice personnel (par opposition à structure nominee) demanderait une expertise comptable judiciaire des flux et bénéfices effectifs. Niveau de confiance : probable.
>
> **Limites.** L'accès au registre UBO chypriote a été partiel (post-arrêt CJUE 2022). L'analyse des flux financiers réels reste hors périmètre OSINT.

Chaque IR fait l'objet d'une section similaire.

#### 88.8 Synthèse intégrée

La **synthèse intégrée** apparaît après les IR. Elle propose une **vue 360°** :
- Timeline globale (résumé).
- Graphe d'enquête (vue d'ensemble).
- Convergences entre IR.
- Tableau ACH consolidé.
- Discussion des hypothèses alternatives.

C'est dans cette section que se construit la **narration analytique** : pas un story-telling, mais une mise en cohérence rigoureuse.

#### 88.9 Recommandations

Les **recommandations** sont actionnables. Pas « il faudrait », mais « nous recommandons de ».

**Niveaux.**
- **Immédiat** : actions à conduire dans les 7 jours (préservation, alertes).
- **Court terme** : 1 mois (escalades).
- **Moyen terme** : 3 mois (approfondissements, expertise).
- **Suivi** : monitoring à mettre en place.

#### 88.10 Limites globales

Cette section honnête est **valorisée** par les commanditaires sérieux. Elle décrit :
- Sources qui n'ont pas pu être consultées (par contrainte de temps, de droit, de budget).
- Hypothèses non testées.
- Marges d'erreur identifiées.
- Conditions sous lesquelles les conclusions pourraient être révisées.

#### 88.11 Annexes

Annexes typiques :
- **Fiches entités** (par personne, société, domaine, lieu).
- **Matrices ACH**.
- **Timeline détaillée**.
- **Graphe Maltego export**.
- **Catalogue de pièces** (avec captures, hashes, sources).
- **Glossaire**.
- **Cotations détaillées**.
- **Outils utilisés** avec versions.

Les annexes peuvent dépasser le rapport principal. Pour un rapport de 30 pages, annexes de 100 pages sont normales.

#### 88.12 Tonalité et registre

**Sobre.** Pas de pathos. Pas d'adjectifs jugeants.

**Précis.** Chaque mot pèse.

**Calibré.** WEP discipliné, pas de surenchère.

**Neutre.** Pas de prise de parti.

**Confiant.** L'analyste assume ses conclusions, sans arrogance.

#### 88.13 Lisibilité visuelle

**Mise en page soignée.**
- Numérotation cohérente des sections.
- Table des matières en début.
- Tableaux pour ce qui se tableaute.
- Schémas pour ce qui se visualise.
- Citations distinctement formatées.
- Captures d'écran lisibles, légendées, sourcées.

**Police et taille adaptées** au public (magistrat appréciera Arial / Times 11pt avec interligne 1.15).

#### 88.14 Délivrabilité

**Formats.**
- **PDF/A** pour archivage long terme.
- **DOCX** si édition par le commanditaire est prévue.
- **Hash** systématique du fichier final.
- **Signature électronique** (eIDAS, AdES) pour valeur juridique.

#### 88.15 Synthèse — discipline de production

Un rapport OSINT complet est un **artefact professionnel**. Sa qualité formelle est inséparable de sa qualité analytique. Soigné, calibré, documenté, il inspire confiance et résiste au contre-expertise.

-----

### Chapitre 89 — Fiches opérationnelles

#### 89.1 La fiche comme atome du dossier

Les **fiches opérationnelles** sont les briques élémentaires d'un dossier OSINT mature. Là où le rapport raconte, la fiche **structure**. Une fiche par entité, mise à jour au fil de l'enquête, exploitée en annexe du rapport, réutilisable d'une enquête à l'autre (avec déontologie de cloisonnement).

#### 89.2 Types de fiches

**Fiche personne physique.**
- Identité civile vérifiée.
- Identités numériques (comptes, emails, téléphones, usernames).
- Parcours (formation, carrière).
- Réseau personnel et professionnel.
- Patrimoine visible.
- Présence médiatique.
- Indicateurs de risque (sanctions, PEP, adverse media).
- Cotation globale et niveau de confiance.

**Fiche société.**
- Identité légale (numéro, juridiction, forme, capital, dates).
- Gouvernance (dirigeants, conseil, commissaires aux comptes).
- Actionnariat et UBO.
- Activité déclarée vs observée.
- Indicateurs financiers visibles.
- Sociétés liées (filiales, groupe, dirigeants partagés).
- Indicateurs de risque.
- Cotation globale.

**Fiche domaine / infrastructure.**
- Domaine principal et sous-domaines.
- WHOIS (actuel + historique).
- DNS records.
- Certificats TLS.
- Hébergement (IPs, ASN).
- Technologies (Wappalyzer).
- Trackers / analytics.
- Liens vers autres domaines (via WHOIS, certificats, trackers).
- Cotation globale.

**Fiche compte (réseau social).**
- Plateforme.
- Username, ID interne.
- Date de création.
- Profil (photo, bio).
- Activité (cadence, sujets, ton).
- Réseau social (followers / followings).
- Liens vers autres comptes.
- Indicateurs d'inauthenticité éventuels.
- Cotation globale.

**Fiche contenu (image, vidéo, audio, document).**
- Identification (URL, hash, taille, format).
- Métadonnées (EXIF, C2PA, IPTC).
- Source originelle (provenance).
- Recherche inversée (autres apparitions).
- Analyse technique (ELA, AI detection).
- Géolocalisation et chronolocation si applicable.
- Cotation d'authenticité.
- Cotation de pertinence.

**Fiche lieu.**
- Coordonnées GPS / adresse.
- Cadastre / immatriculation.
- Propriétaire (s'il est public).
- Photos et contexte.
- Indicateurs (visite cible documentée, etc.).

**Fiche événement.**
- Date / heure / lieu.
- Acteurs présents.
- Sources documentant.
- Patterns associés.

#### 89.3 Format standard d'une fiche

**Une fiche tient idéalement sur 1-3 pages** lisibles.

**Sections type.**

1. **En-tête.** Type d'entité, identifiant interne, statut (en cours / clos), dernière mise à jour.
2. **Sélecteurs forts.** Identifiants uniques (numéro entreprise, email confirmé, téléphone).
3. **Caractéristiques structurelles.**
4. **Liens vers autres entités.** Cross-références.
5. **Sources principales.**
6. **Cotation globale.** Avec justification.
7. **Notes d'enquête.** Observations, hypothèses, pistes.

#### 89.4 Cotation par fiche

Chaque fiche porte une **cotation globale** qui résume :
- Solidité de l'identification (l'entité est-elle bien celle qu'on pense ?).
- Complétude (combien de dimensions investiguées ?).
- Niveau de confiance des éléments retenus.

**Exemple.**
- Fiche Verde Holdings : identification A1 (registre officiel), complétude moyenne (registre UBO partiel post-CJUE), niveau de confiance global : élevé sur l'existence et le contrôle, modéré sur les flux financiers.

#### 89.5 Maintenance dans la durée

Une fiche **vit**. Elle est mise à jour à chaque nouvelle information pertinente.

**Discipline.**
- Versioning des fiches.
- Historique des modifications (git si vault).
- Mention de la date de dernière vérification de chaque fait.

#### 89.6 Fiches comme annexe du rapport

Dans le rapport final, les fiches apparaissent en annexe. Elles permettent au lecteur de retrouver rapidement le détail sur n'importe quelle entité mentionnée dans le corps du rapport.

**Format.** Fiches au sein du même document (PDF) ou liées (références hyperliens).

#### 89.7 Réutilisabilité (avec déontologie)

Les fiches sont **précieuses** : elles capitalisent le travail.

**Déontologie.**
- Pas de mélange entre enquêtes différentes (un mandat de cabinet A ne nourrit pas un cabinet B).
- Données personnelles purgées en fin de mandat (RGPD).
- Réutilisation des fiches « génériques » (organisations, infrastructure publique) seule.
- Documentation rigoureuse de l'origine.

#### 89.8 Exemple — fiche personne MIRAGE (extrait)

```
FICHE PERSONNE — Marc Delaunay
Identifiant interne : MIRAGE/P-001
Statut : en cours
Dernière mise à jour : 2026-05-XX
Cotation globale : élevée (identification multi-corroborée)

Sélecteurs forts
- Nom complet : Marc Henri Delaunay (cohérent multi-sources)
- Date de naissance : 1976-XX-XX (déduite, à confirmer)
- SIREN administrateur Delta Consulting Ltd
- UBO Verde Holdings 100 %
- Email perso présumé : marc.delaunay76@gmail.com (B2)

Identité civile vérifiée
- Citoyenneté : française (présomption forte)
- Adresse résidentielle : Paris 17e (confirmée, via Pappers SCI)
- État civil : marié, deux enfants (déduit photos LinkedIn)

Identités numériques
- LinkedIn : marc-delaunay-XX (vérifié)
- Twitter/X : @mdelaunay76 (verrouillé, faible activité)
- Instagram : mdelaunay76 (privé)
- GitHub : mdelaunay (inactif depuis 2019)
- Email perso : marc.delaunay76@gmail.com (HIBP, Holehe confirment)
- ProtonMail : ********** (existe selon stealer log, non confirmé)

Parcours
- 2002 : X-Ponts (LinkedIn, A1)
- 2007 : audit Big 4 (LinkedIn, A1)
- 2014 : DAF société industrielle (LinkedIn, A1)
- 2019-06 : DAF TechnoVert SAS (LinkedIn + communiqué TechnoVert, A1)

Patrimoine visible
- SCI La Provence Familiale (Goult, Vaucluse) : mas estimé 1.8 M€
- Villa Marrakech : 800 k€ (Cyprus Confidential mention)
- Appartements parisiens : SCI nominee, à confirmer
- Compte Binance perso (stealer log)

Indicateurs de risque
- Sanctions : aucune (OpenSanctions A1)
- PEP : non
- Adverse media : aucun public identifié
- Liens offshore : Delta Consulting (Malte), Verde Holdings (Chypre)
- Patrimoine vs revenus : incohérence apparente (élément d'alerte)

Réseau professionnel et personnel
- TechnoVert (DAF) : Pierre Dubois (DG), Sophie Martin (DRH)
- Réseau LinkedIn : 487 contacts, dont 12 PDG/DG identifiés
- Cabinet conseil : non identifié à ce stade

Liens vers autres fiches
- Société TechnoVert SAS (E-001)
- Société Delta Consulting Ltd (E-002)
- Société Verde Holdings (E-003)
- SCI La Provence Familiale (E-004)
- Compte Twitter/X @mdelaunay76 (C-007)
- Mas Goult (L-002)

Notes d'enquête
- Empreinte SOCMINT volontairement faible.
- Stealer logs offrent pivot crypto significatif.
- Profil patrimonial à approfondir judiciairement.

Sources principales avec captures
- LinkedIn (Hunchly 2026-XX-XX, hash)
- Pappers TechnoVert (Hunchly, hash)
- Companies Registry Malta (Delta Consulting, hash)
- Companies Registry Cyprus (Verde Holdings, hash)
- Cyprus Confidential ICIJ (capture, hash)
- HIBP / Hudson Rock (capture, hash)
- [autres]
```

Une fiche personne mature peut représenter 3-5 pages structurées.

#### 89.9 Pièges fréquents

**Sur-déclaration.** Affirmer ce qui n'est pas certain dans la fiche. Cotation absente.

**Sous-déclaration.** Ne pas documenter ce qui est connu, par paresse.

**Pas de cross-référence.** Fiches isolées, sans liens entre elles. Le dossier devient illisible.

**Pas de versioning.** Modifications non tracées. Une analyse contestée n'a pas d'historique.

#### 89.10 Synthèse

Les fiches sont le **squelette** du dossier d'enquête. Bien tenues, elles structurent le travail, soutiennent le rapport, capitalisent l'expertise. Mal tenues, elles désorganisent.

-----

### Chapitre 90 — Rapport judiciaire et précontentieux

#### 90.1 Spécificités du rapport judiciaire

Un rapport OSINT destiné à un **usage judiciaire** (transmission à un magistrat, dépôt dans un dossier pénal, soutien à une procédure civile) impose des exigences renforcées :
- **Chain of custody** stricte sur chaque pièce.
- **Horodatage qualifié** (eIDAS).
- **Signature électronique** AdES.
- **Vocabulaire calibré** sans qualification pénale.
- **Documentation méthodologique** exhaustive.
- **Préservation** des originaux numériques.

#### 90.2 L'analyste OSINT n'est pas un juge

**Principe.** L'analyste **identifie des éléments**, **les cote**, **propose des hypothèses**. Il **ne qualifie pas pénalement**.

**Mauvaise pratique.** « Delaunay a commis un détournement de fonds. »

**Bonne pratique.** « Les éléments collectés sont compatibles avec un montage de détournement de fonds, qualification dont l'établissement relève de l'autorité judiciaire après expertise complémentaire. »

L'analyste apporte le **substrat factuel** ; le magistrat **qualifie**.

#### 90.3 Chain of custody

Pour chaque pièce :
- **Capture** datée, horodatée, signée.
- **Hash** SHA-256 sur le fichier collecté.
- **Source** documentée (URL, date d'accès).
- **Outil** utilisé pour la collecte (Hunchly version X, ExifTool version Y).
- **Préservation** : stockage chiffré, intégrité périodiquement vérifiée.
- **Historique** : toute manipulation tracée.

Si la pièce est transmise au magistrat, **bordereau** mentionnant ces éléments.

#### 90.4 Horodatage qualifié eIDAS

Le règlement **eIDAS** (UE 910/2014) reconnaît les horodatages qualifiés émis par prestataires de services de confiance.

**Pour OSINT.**
- **OpenTimestamps** (open source, blockchain Bitcoin) : preuve d'antériorité non qualifiée mais robuste.
- **Prestataires qualifiés eIDAS** (LuxTrust, Certigna, etc.) : valeur juridique renforcée.
- **Cachet électronique qualifié** : pour personne morale (cabinet, organisation).

**Pratique.** Pour pièces centrales, double horodatage : OpenTimestamps + cachet électronique qualifié.

#### 90.5 Signature électronique AdES

**AdES** (Advanced Electronic Signatures) : signature électronique reconnue eIDAS.

**Pour rapport.**
- **PAdES** (PDF Advanced Electronic Signatures) : standard pour PDF.
- **CAdES** : pour ensemble de fichiers.
- **XAdES** : pour XML.

**Niveaux.**
- **AdES-B** : niveau de base.
- **AdES-T** : avec horodatage.
- **AdES-LT** : long terme (preuves intégrées).
- **AdES-LTA** : avec horodatage périodique de la chaîne entière.

**Pour OSINT judiciaire.** PAdES-LT au minimum.

#### 90.6 Vocabulaire judiciaire calibré

**À utiliser.**
- « Les éléments collectés documentent... »
- « Plusieurs sources convergentes attestent... »
- « Un faisceau d'indices suggère... »
- « Il est probable que... »
- « Les éléments ne permettent pas de conclure définitivement sur... »
- « Une expertise complémentaire serait nécessaire pour établir... »

**À éviter.**
- « Coupable », « auteur du délit », « fraude avérée » (qualifications pénales).
- « Sans aucun doute » (sur-affirmation).
- Adjectifs jugeants.

#### 90.7 Préservation des originaux numériques

**Discipline.**
- **Captures HTML originales** préservées (Hunchly).
- **Captures PDF horodatées** complémentaires.
- **Hashes** consignés.
- **Sauvegarde 3-2-1** : 3 copies, 2 supports différents, 1 hors site, **toutes chiffrées**.

Le commanditaire (cabinet, magistrat) doit pouvoir, à tout moment, demander la pièce originale et vérifier son intégrité par hash.

#### 90.8 Structure type d'un rapport judiciaire

Similaire au rapport complet (Ch.88), avec **renforcements** :

- **Page de garde** mentionne le statut judiciaire.
- **Préambule** explicite la finalité judiciaire et le cadre déontologique.
- **Méthodologie** exhaustive et reproductible.
- **Chaque fait** porte sa pièce annexe avec hash.
- **Conclusions** strictement calibrées WEP.
- **Annexe « catalogue de pièces »** liste chaque capture, hash, source, date d'accès.
- **Signature et horodatage** qualifiés.

#### 90.9 Témoin et auditionné

L'analyste OSINT peut être convoqué comme **témoin** dans la procédure. Sa préparation :
- Connaissance approfondie de son rapport.
- Capacité à expliquer la méthodologie en termes simples.
- Maîtrise des limites identifiées.
- Posture honnête : ne pas affirmer plus que le rapport.
- Adhésion à la cotation : ne pas céder à pression d'avocat pour sur-affirmer.

#### 90.10 Cas particulier — la procédure prud'homale

En cas MIRAGE, le volet désinformation contre Berthier impacte sa **procédure prud'homale** contre TechnoVert. Le rapport OSINT peut servir à :
- **Démontrer** que les pièces TechnoVert contre Berthier sont compatibles avec une fabrication.
- **Préciser** le contexte (campagne coordonnée).
- **Documenter** l'authenticité douteuse de pièces présentées comme « preuves » contre Berthier.

#### 90.11 Différence avec l'expertise judiciaire

**Expertise judiciaire.** Mandatée par le magistrat, conduite par un expert inscrit, soumise à serment, contradictoire avec parties.

**Rapport OSINT.** Mandaté par une partie privée (cabinet d'avocats, entreprise), conduite par un cabinet OSINT, sans serment.

**Statut.** Le rapport OSINT est **pièce contributive**, pas expertise. Le magistrat peut le verser au dossier ; il a la valeur d'un avis privé technique.

**Pratique.** L'analyste OSINT peut être ultérieurement nommé expert (s'il est inscrit). Distinction préservée.

#### 90.12 Synthèse — exigences renforcées

| Aspect | Rapport complet | Rapport judiciaire |
|---|---|---|
| Chain of custody | Recommandée | **Obligatoire** |
| Horodatage | OpenTimestamps | **eIDAS qualifié** |
| Signature électronique | DocuSign / similaire | **AdES PAdES** |
| Vocabulaire | Calibré WEP | **Renforcé sans qualification pénale** |
| Préservation pièces | 3-2-1 | **3-2-1 chiffré, intégrité vérifiée** |
| Annexes | Variables | **Catalogue exhaustif des pièces** |
| Tonalité | Sobre | **Strictement neutre** |

-----

### Chapitre 91 — Diffusion, confidentialité et TLP

#### 91.1 Diffusion comme acte professionnel

Produire un rapport n'épuise pas l'enquête. **Diffuser** intelligemment, **protéger** les informations, **respecter** les engagements de confidentialité sont des actes professionnels distincts.

#### 91.2 TLP : Traffic Light Protocol

Le **TLP** (Traffic Light Protocol) est le standard international de classification d'informations sensibles. Géré par FIRST (Forum of Incident Response and Security Teams). Version 2.0 depuis 2022.

**Quatre niveaux.**

- **TLP:RED.** Information personnelle, individuelle. Pas de diffusion au-delà du destinataire direct.
- **TLP:AMBER.** Information limitée. Diffusion restreinte à organisation du destinataire et à ses partenaires directs nécessaires.
- **TLP:AMBER+STRICT.** Limité à l'organisation du destinataire, pas de partage avec partenaires.
- **TLP:GREEN.** Information communautaire. Partage avec partenaires et homologues, mais pas publication ouverte.
- **TLP:CLEAR** (anciennement WHITE). Publication libre.

#### 91.3 Application TLP en OSINT

**Mandat type.**
- Rapport d'enquête sensible : **TLP:AMBER+STRICT** ou **TLP:RED**.
- IOCs CTI pour communauté : **TLP:GREEN** ou **AMBER**.
- Étude publique pour client : **TLP:CLEAR**.

**Marquage.** Chaque page du rapport porte la mention TLP. Email d'envoi mentionne TLP. Le destinataire est responsable du respect.

#### 91.4 RGPD et diffusion

Si le rapport contient **données personnelles**, le RGPD s'applique :
- Base légale documentée.
- Minimisation (que ce qui est nécessaire).
- Sécurité (chiffrement transmission).
- Droits des personnes (notamment droit d'accès, opposition).
- Durée de conservation.

**Pratique.** Anonymisation / pseudonymisation quand pertinent. Diffusion ciblée. Tracabilité.

#### 91.5 Confidentialité contractuelle

Le mandat impose typiquement **engagement de confidentialité** :
- Sur le rapport.
- Sur la méthodologie spécifique.
- Sur les sources particulières.
- Sur l'identité du commanditaire.

L'analyste **respecte** ces engagements même après la fin du mandat.

#### 91.6 Chiffrement de la transmission

**Pour transmission au commanditaire.**
- Email : **PGP/GPG** (mature mais peu utilisé), **S/MIME** (plus enterprise).
- Plateforme dédiée : **SecureDrop**, **OnionShare**, **Tresorit Send**, **ProtonMail Drive**.
- Remise physique avec support chiffré (très sensible).

**Pour transmission au magistrat.**
- Canal officiel (greffe, e-Barreau).
- Chiffrement complémentaire si pertinent.

#### 91.7 Marquage et watermarking

**Watermarking destinataire.** Un rapport peut porter un watermark visible (ou invisible) identifiant le destinataire. Si fuite, source identifiable.

**Pratique.** Watermark discret en pied de page (nom destinataire, date, hash). Watermark invisible (méthodes spécialisées).

#### 91.8 Archivage post-diffusion

Après diffusion :
- **Archivage** local chiffré (3-2-1).
- **Index** dans système de gestion des rapports (pour retrouver ultérieurement).
- **Durée de conservation** documentée.
- **Purge** programmée à fin de période.

**RGPD.** La durée doit être justifiée et limitée. Conservation indéfinie problématique.

#### 91.9 Sortie du périmètre du mandat

**Question.** Que faire si l'analyste découvre, en cours de mandat, des éléments **hors périmètre** qui semblent pertinents pour d'autres enquêtes (autres clients, autorités) ?

**Principe général.** Pas de diffusion hors mandat sans autorisation explicite.

**Exceptions.**
- **Obligation légale** (signalement d'infractions graves : terrorisme, CSAM, etc.).
- **Consentement** explicite du commanditaire.

**Pratique.** Documentation rigoureuse. Si signalement légal nécessaire, mention dans le rapport au commanditaire.

#### 91.10 Conférences, publications académiques, presse

Si l'analyste souhaite publier (article, conférence, presse), méthodologie :
- **Autorisation** explicite du commanditaire si données sensibles.
- **Anonymisation** du cas si nécessaire.
- **Cas générique** plutôt que cas réel.
- **Accord écrit** mentionné dans la publication.

#### 91.11 Synthèse — discipline de diffusion

| Phase | Action |
|---|---|
| Préparation | Définir TLP, chiffrement transmission |
| Diffusion | Canal sécurisé, watermark si pertinent |
| Réception | Confirmation par destinataire |
| Archivage | Chiffrement, durée documentée |
| Post-mandat | Purge programmée, anonymisation si publication |

> **Principe.** La diffusion est un acte professionnel. Elle protège le commanditaire, l'analyste, les personnes mentionnées. Une diffusion mal maîtrisée détruit la confiance bâtie pendant l'enquête.

-----

### Chapitre 92 — Veille post-rapport et capitalisation

#### 92.1 Au-delà du rapport

Une enquête ne s'arrête pas à la remise du rapport. **Veille** sur l'évolution de la cible, **capitalisation** méthodologique, **archivage** rigoureux : trois dimensions post-rapport souvent négligées.

#### 92.2 Veille post-rapport

Si le mandat le prévoit, **veille continue** sur la cible :
- Évolutions corporate (nouveaux dirigeants, dissolution, fusion).
- Nouvelles sanctions / PEP.
- Adverse media.
- Évolution infrastructure (nouveaux domaines, fuites).
- Évolution patrimoine (nouvelles acquisitions visibles).

**Outils.**
- **Google Alerts** : nom, raison sociale, domaines.
- **OpenSanctions monitoring**.
- **Hunchly continuous** : capture régulière.
- **Custom pipelines** : scripts qui scan périodiquement.

**Pour MIRAGE.** Si l'audience prud'homale Berthier doit avoir lieu plusieurs mois après le rapport, veille sur les acteurs : nouveau communiqué TechnoVert, nouvelle vidéo deepfake, évolution cluster désinformation.

#### 92.3 Alertes et triage

Une veille produit des **alertes**. Triage rapide :
- **Pertinent** → note d'update au commanditaire.
- **À surveiller** → archivage interne pour suivi.
- **Non pertinent** → écarté avec justification.

**Pratique.** Note d'update mensuelle ou trimestrielle au commanditaire.

#### 92.4 Capitalisation méthodologique

Chaque enquête enrichit l'analyste :
- **Outils** testés (qui marche, qui ne marche pas pour quel usage).
- **Méthodes** validées ou révisées.
- **Pièges** identifiés.
- **Sources** spécialisées découvertes.

**Pratique.** Après chaque enquête, **debriefing** interne :
- Qu'est-ce qui a bien fonctionné ?
- Qu'est-ce qui n'a pas bien fonctionné ?
- Quelles leçons pour la prochaine ?

Documentation dans un **carnet méthodologique** propre à l'analyste / cabinet.

#### 92.5 Capitalisation factuelle (avec déontologie)

Certaines informations factuelles sont **réutilisables** d'une enquête à l'autre :
- Structures corporate publiques (immuables).
- Métadonnées infrastructures publiques.
- Méthodologies de groupes d'attaquants (TTP).

**Discipline.**
- Pas de mélange entre enquêtes différentes (mandat A ne nourrit pas mandat B).
- Information générale (sectorielle, publique) seule réutilisée.
- Données personnelles purgées par enquête.

**Pour cabinet.** Base de connaissances structurée distincte des dossiers d'enquête.

#### 92.6 Archivage post-mandat

Selon mandat et juridiction :
- **Durée de conservation** documentée (typique 3-10 ans).
- **Chiffrement** maintenu.
- **Accès** restreint.
- **Intégrité** vérifiée périodiquement (re-hash).

**RGPD.** Justification de la conservation. Information aux personnes si pertinent.

#### 92.7 Purge en fin de période

**Fin de la durée de conservation.**
- Suppression sécurisée (overwrite, wipe).
- Documentation de la purge.
- Conservation éventuelle d'un récapitulatif anonymisé.

**Pour MIRAGE.** Si la procédure se conclut sous 5 ans, archivage 7 ans (durée légale post-procédure), puis purge.

#### 92.8 Suivi du commanditaire

Bonne pratique : **contact périodique** avec le commanditaire post-rapport :
- A-t-il pu utiliser le rapport efficacement ?
- Des éléments ont-ils été confirmés / infirmés par d'autres voies ?
- Y a-t-il besoin de mise à jour ?

Bénéfices : amélioration continue, relation long terme, opportunités futures.

#### 92.9 Veille communautaire et formation continue

L'analyste se forme continûment :
- Suivi de Bellingcat, OCCRP, EU DisinfoLab, VIGINUM, Stanford SIO publications.
- Conférences (OSMOSIS, OSINT Day, NICAR, IRE).
- Formation en ligne (Bellingcat training, NATO StratCom).
- Communautés (Discord, Reddit /r/OSINT, Twitter/X OSINT communauté).

#### 92.10 Synthèse — cycle complet de l'enquête

| Phase | Discipline |
|---|---|
| Cadrage | Mandat précis, IR formulées |
| Collecte | OPSEC, captures, cotation |
| Analyse | ACH, anti-biais, raisonnement adversaire |
| Production | Rapport calibré, fiches structurées |
| Diffusion | TLP, chiffrement, watermark |
| Veille | Alertes, updates |
| Capitalisation | Carnet méthodo, base sectorielle |
| Archivage | Chiffré, intégrité, durée |
| Purge | Sécurisée, documentée |

> **Principe.** L'enquête OSINT mature est un **cycle complet**, pas une production isolée. Chaque cycle nourrit le suivant, dans le respect strict de la déontologie de cloisonnement.

-----

### Chapitre 93 — Cas complet : synthèse MIRAGE

#### 93.1 Présentation du cas

Ce chapitre clôt l'épopée MIRAGE en rassemblant les 21 épisodes vus au fil du cours et en produisant la synthèse finale du dossier, telle qu'elle serait remise au cabinet Legrand & Associés.

L'objectif pédagogique est triple : (1) montrer comment des épisodes apparemment disparates s'assemblent en une enquête cohérente, (2) illustrer la production d'un livrable mature dans toutes ses dimensions, (3) servir de modèle de référence pour les enquêtes complexes que l'analyste sera amené à conduire.

#### 93.2 Rappel du mandat

**Cabinet** Legrand & Associés, mandaté par TechnoVert SAS (Pierre Dubois, DG), dans le cadre d'une procédure interne post-audit. Saisine également du PNF en parallèle (dénonciation art. 40 CPP).

**Périmètre.** Investigation OSINT sur Marc Delaunay (DAF de TechnoVert) et son entourage corporate proche, dans le cadre de 5 soupçons : détournement, blanchiment crypto, désinformation contre lanceur d'alerte Berthier, cluster faux comptes, vidéo deepfake.

**Bornes.** Sources ouvertes exclusivement, OPSEC stricte, déontologie défensive, escalade vers expertise forensique et procédure judiciaire pour profondeur.

**Durée.** 4 semaines.

#### 93.3 Architecture de l'enquête conduite

L'enquête s'est articulée en **5 volets** correspondant aux 5 IR formulées au cadrage (Ch.12 / MIRAGE 0).

**Volet 1 — Structures offshore (IR1).** Investigation sur Delta Consulting Ltd (Malte) et Verde Holdings (Chypre) : existence, contrôle, UBO, liens organiques.

**Volet 2 — Flux financiers visibles (IR2).** Indicateurs ouverts de transferts TechnoVert vers offshore.

**Volet 3 — Patrimoine et cohérence (IR3).** Patrimoine visible de Delaunay et cohérence avec revenus déclarés.

**Volet 4 — Désinformation contre Berthier (IR4).** Cluster X, Telegram, faux médias, contenu IA.

**Volet 5 — Contenus IA et attribution (IR5).** Authenticité des fausses photos et vidéo deepfake, attribution au commanditaire.

#### 93.4 Synthèse Volet 1 — Structures offshore

**Faits saillants cotés.**

| Fait | Source | Cot. |
|---|---|---|
| Delta Consulting Ltd immatriculée Malte 03/2020 | Companies Registry Malta | A1 |
| Director unique Marc Delaunay | Companies Registry Malta | A1 |
| Adresse domiciliation type registered agent | OpenCorporates | A1 |
| Verde Holdings Chypre 01/2022 | Companies Registry CY | A1 |
| UBO Marc Delaunay 100 % | Registre UBO CY (partiel) | A1 |
| Marina Constantinidou administratrice locale | Registre CY | A1 |
| Cyprus Confidential mémo flux Delta → Verde | ICIJ leak | B2 |
| Aucune sanction / PEP active | OpenSanctions | A1 |
| Aucune déclaration française publiquement visible | Recherches FR | D3 |

**Conclusion.** **Probable** : Marc Delaunay détient et opère, depuis 2020, un dispositif de structures offshore (Delta Consulting et Verde Holdings) bénéficiant de flux dont l'origine plausible est TechnoVert SAS. **ACH résiduellement ouverte** sur l'hypothèse alternative « nominee pour tiers ». Hypothèse « pas de lien réel » réfutée par convergence des éléments.

**Limites.** Registre UBO chypriote partiellement accessible. Comptes Verde non publiés. Flux financiers réels demandent expertise comptable judiciaire.

#### 93.5 Synthèse Volet 2 — Flux financiers visibles

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| Comptes TechnoVert publiés montrent ligne « prestations consulting externes » significative | Pappers / comptes consolidés | A1 |
| Croissance de cette ligne 2020-2024 | Comptes consolidés | A1 |
| Cohérence temporelle avec création Delta (03/2020) | Cross-référence | B2 |
| Cyprus Confidential mentionne flux Delta → Verde | ICIJ leak | B2 |
| Pas de bénéficiaire externe connu cohérent | Recherches | B2 |

**Conclusion.** **Probable** : des flux financiers de TechnoVert vers Delta Consulting (cohérents avec la ligne « prestations consulting externes » dans les comptes consolidés) alimentent Delta puis Verde, dans un schéma compatible avec un détournement par double-fausse-facturation. **Démonstration formelle** demande accès aux factures Delta émises à TechnoVert (hors OSINT, requérable judiciairement).

#### 93.6 Synthèse Volet 3 — Patrimoine et cohérence

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| SCI La Provence Familiale, mas Goult (Vaucluse) | Pappers / cadastre | A1 |
| Estimation mas : 1.5-2 M€ | Estimations locales | B2 |
| Villa Marrakech | Cyprus Confidential mention | B2 |
| Appartements parisiens (SCI nominee) | Indices Pappers | C3 |
| Compte Binance personnel | Stealer log Hudson Rock | B2 |
| Revenus DAF TechnoVert estimés 180-250 k€/an | Standards sectoriels | B2 |
| Cumul revenus 2019-2025 (avant fiscalité) ~1.3-1.8 M€ | Estimation | B3 |
| Patrimoine visible estimé 3-4 M€ | Cumul | B3 |

**Conclusion.** **Probable** : le patrimoine visible de Delaunay (estimation 3-4 M€) est en **incohérence apparente** avec son cumul de revenus déclarés (1.3-1.8 M€ brut sur 7 ans, ramené après fiscalité et charges courantes à ~600-900 k€ disponibles à l'épargne). L'écart suggère soit (a) revenus complémentaires non déclarés, soit (b) acquisitions partiellement financées par des moyens non identifiés. Une expertise patrimoniale judiciaire serait nécessaire pour conclure.

**Hypothèses concurrentes.** Héritage familial substantiel, mariage favorable, gains exceptionnels (gain crypto, héritage récent) — toutes plausibles, aucune documentée par sources ouvertes.

#### 93.7 Synthèse Volet 4 — Désinformation contre Berthier

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| Cluster X : 8 comptes coordonnés | Analyse graphe + temporelle | A1 |
| Cluster Telegram : 9 canaux amplifiant | Observation passive | A1 |
| Domaine `verites-technovert.com` créé 12/10/2025 | WHOIS historique | A1 |
| Domaine `info-finance-eu.com` créé 18/10/2025 | WHOIS historique | A1 |
| GA partagé entre les deux domaines | DNSlytics | A1 |
| Création concentrée après licenciement Berthier (15/09/2025) | Cross-références | A1 |
| Cohérence narrative entre les supports | Lecture humaine | B2 |
| Existence de prestataire potentiel (canal Telegram « social media boost ») | Observation passive | B2 |
| Lien direct avec Delaunay non démontré | (négatif) | — |

**Conclusion.** **Très probable** : une **campagne de désinformation coordonnée** vise Antoine Berthier, articulée sur 8 comptes X, 9 canaux Telegram, 2 faux médias, contenus IA, avec démarrage chronologiquement consécutif à son licenciement et pic d'amplification avant l'audience prud'homale. **Probable** : cohérence d'intérêt avec Delaunay (cible de l'alerte Berthier), suggérant attribution à Delaunay ou son entourage comme commanditaire le plus plausible. **Démonstration directe** non disponible en OSINT.

#### 93.8 Synthèse Volet 5 — Contenus IA

**Faits saillants.**

| Fait | Source | Cot. |
|---|---|---|
| 3 fausses photographies « Berthier en soirée privée » | Captures + recherche inversée | A1 |
| Faces swappés sur backgrounds Unsplash / Pexels | Recherche inversée + ELA | A1 |
| Vidéo deepfake « Berthier confessant » | yt-dlp capture | A1 |
| Detection IA convergente Sensity 89 %, FakeCatcher 92 % | Outils techniques | A1 |
| Voice cloning detecté Resemble 76 % | Audio analysis | A1 |
| Incompatibilité avec déclarations publiques Berthier | Presse régionale | A1 |
| Pic publication avant audience prud'homale | Chronologie | A1 |

**Conclusion.** **Très probable** : les trois fausses photographies et la vidéo deepfake de Berthier sont des **contenus synthétiques fabriqués**, dans le cadre d'une campagne de discrédit. La cohérence avec le calendrier procédural (avant audience) renforce l'intentionnalité.

**Recommandation.** Expertise judiciaire complémentaire (expert numérique inscrit) pour validation officielle. Le rapport OSINT fournit le substrat technique.

#### 93.9 Synthèse intégrée

Les **cinq volets convergent** :

- **Architecture économique** : montage offshore Delta-Verde sous contrôle Delaunay, vraisemblablement alimenté par TechnoVert via fausses factures de consulting.
- **Manifestation patrimoniale** : patrimoine visible de Delaunay en incohérence avec revenus déclarés, cohérent avec bénéfice du montage.
- **Réaction au signalement** : Berthier a déclenché audit interne en avril 2025, signalé en mai, licencié en septembre 2025.
- **Campagne défensive** : à partir d'octobre 2025, déploiement coordonné d'une campagne de désinformation et de discrédit contre Berthier, intensifiée avant l'audience prud'homale.
- **Sophistication** : usage d'IA générative (deepfakes, faces swap, voice cloning), infrastructure technique mature, possible prestataire externe.

**Cohérence d'ensemble : élevée.** Tous les éléments forment un **dispositif** cohérent ayant pour finalité (a) détournement, (b) protection du dispositif via discrédit du lanceur d'alerte.

**Niveau de confiance global : probable** sur l'architecture d'ensemble, **élevé** sur les éléments factuels individuels, **modéré** sur l'attribution explicite de la campagne de désinformation à Delaunay comme commanditaire direct.

#### 93.10 Recommandations actionnables

**Immédiat (sous 7 jours).**
- Préservation des pièces (intégrité maintenue, archive 3-2-1 chiffrée).
- Transmission de la note courte au PNF pour suite procédure pénale.
- Transmission au conseil de Berthier pour soutien à la procédure prud'homale.

**Court terme (1 mois).**
- Mandater expertise comptable forensique sur les comptes consolidés TechnoVert (2020-2025).
- Mandater expertise numérique sur les contenus IA identifiés (vidéo deepfake, fausses photos).
- Sollicitation par le PNF d'entraide judiciaire avec autorités maltaises et chypriotes.

**Moyen terme (3 mois).**
- Investigation crypto forensique professionnelle (clustering, attribution wallet, cashout patterns) — renvoi cours OSINT Crypto vFULL.
- Approfondissement réseau d'amplification (réquisitions Telegram, X).

**Suivi.**
- Veille post-rapport sur acteurs (TechnoVert, Delaunay, Berthier procédures).
- Mises à jour mensuelles au cabinet.

#### 93.11 Limites globales du rapport

**Périmètre OSINT.** Démonstration directe de détournement, qualification pénale, accès aux flux financiers réels demandent expertise judiciaire et procédure pénale.

**Attribution désinformation.** Lien direct Delaunay → service de désinformation non démontré en sources ouvertes. Réquisitions opérateurs permettraient confirmation.

**Crypto.** Triage limité, expertise dédiée requise.

**Sources opaques.** Stealer logs et leaks ICIJ utilisés comme orientations, non comme preuves directes pour usage judiciaire (l'expertise certifie).

**Temporalité.** Enquête conduite en 4 semaines. Approfondissement à 3-6 mois pourrait révéler éléments supplémentaires.

#### 93.12 Le rapport délivré

Le **rapport MIRAGE** finalisé fait :
- 47 pages (corps + executive summary).
- 134 pages d'annexes (fiches, matrices ACH, timeline détaillée, graphe export, catalogue de pièces).
- 287 pièces archivées avec hash, captures Hunchly.
- Signature électronique PAdES-LT, horodatage qualifié.
- Classification TLP:AMBER+STRICT.

Transmis au cabinet Legrand & Associés et, en copie, au PNF dans le cadre de la dénonciation art. 40.

> **MIRAGE — Épisode 20 : Rapport final intégré**
>
> Le rapport MIRAGE clôt formellement l'enquête de 4 semaines. Il documente un dispositif probable de détournement via structures offshore, accompagné d'une campagne de désinformation sophistiquée contre le lanceur d'alerte. Il fournit le substrat factuel et méthodologique au cabinet et au PNF pour les actions ultérieures (audits forensiques, expertise numérique, entraide judiciaire internationale).
>
> Le rapport ne « prouve » pas un délit ; il **documente** un faisceau cohérent que la procédure judiciaire confirmera ou non. C'est exactement le rôle de l'OSINT : produire le matériau structuré sur lequel les autorités compétentes prennent des décisions qualifiantes.

#### 93.13 Pédagogie du cas MIRAGE

À travers les 21 épisodes répartis sur le cours, MIRAGE a illustré :

- Le cadrage initial (Ch.12 / MIRAGE 0).
- La cartographie des sources et fiches initiales (Ch.13-14 / MIRAGE 1-2).
- La méthodologie d'enquête (Ch.18 / MIRAGE 3).
- L'identification de personne (Ch.26 / MIRAGE 4).
- Les pseudonymes et identités numériques (Ch.28 / MIRAGE 5).
- Le SOCMINT multi-plateformes (Ch.32 / MIRAGE 6).
- Telegram et forums (Ch.33 / MIRAGE 7).
- Sociétés, dirigeants, UBO (Ch.37 / MIRAGE 8).
- Infrastructure web (Ch.39 / MIRAGE 9).
- Breaches et stealer logs (Ch.43 / MIRAGE 10).
- Image suspecte et vérification (Ch.47 / MIRAGE 11).
- GEOINT et chronolocation (Ch.49 / MIRAGE 12).
- Signaux financiers ouverts (Ch.70 / MIRAGE 13).
- Piste crypto avec renvoi cours dédié (Ch.72 / MIRAGE 14).
- Piste dark web avec renvoi cours dédié (Ch.44 / MIRAGE 15).
- Deepfake et contenu synthétique (Ch.59 / MIRAGE 16).
- Campagne d'influence coordonnée (Ch.76 / MIRAGE 17).
- Graphe et timeline (Ch.83 / MIRAGE 18).
- Hypothèses concurrentes ACH (Ch.79 / MIRAGE 19).
- Rapport final intégré (Ch.93 / MIRAGE 20).

Chaque épisode illustre un aspect méthodologique. Le tout forme un parcours pédagogique complet.

-----

### Chapitre 94 — Cas pratique : GEOINT sur vidéo virale

#### 94.1 Présentation du cas

Une vidéo virale circule sur X et Telegram, montrant un convoi militaire dans un environnement non identifié. La vidéo est présentée comme « preuve d'incursion en territoire X ». L'analyste OSINT doit :
- Vérifier l'authenticité de la vidéo.
- Géolocaliser le lieu.
- Chronolocaliser la date de prise.
- Identifier les véhicules visibles.
- Évaluer la cohérence avec le narratif présenté.

#### 94.2 Étape 1 — Préservation

**Action.** Download via `yt-dlp` (avec X) ou capture manuelle (Telegram).

```bash
yt-dlp https://x.com/[user]/status/[id]
```

**Préservation.** Hash SHA-256, capture HTML de la page de partage, conservation des métadonnées disponibles.

#### 94.3 Étape 2 — Lecture méthodique

**Inventaire visuel.**
- Convoi de 6 véhicules militaires.
- Visibles : 2 chars (type à identifier), 3 véhicules de transport, 1 camion.
- Insignes au sol partiellement visibles.
- Paysage : terrain plat semi-aride, végétation rare, ligne d'horizon dégagée.
- Route asphaltée mais dégradée.
- Lampadaires de type est-européen.
- Ciel : ensoleillé, ombres modérées.
- Pas de panneaux routiers lisibles.

**Audio.** Bruits moteur + voix off en langue à identifier.

#### 94.4 Étape 3 — Authenticité technique

**Détection IA.**
- Sensity AI : 12 % « likely real ».
- FakeCatcher : signal physiologique cohérent.
- Pas de signaux visuels d'IA générative (cohérence frame par frame).

**Recherche inversée des frames clés.** Yandex + Google Lens : aucune occurrence antérieure à la date de publication. Pas de recyclage d'ancienne vidéo identifié.

**Conclusion préliminaire.** Probable authenticité. Cotation B2 (cohérence technique, sans certificat C2PA).

#### 94.5 Étape 4 — Identification des véhicules

**Chars.** Comparaison avec catalogues OSINT militaires : forme de la tourelle, position du canon, profil général.

**Hypothèses :**
- T-72B3 (Russie / soviétique).
- T-90 (Russie moderne).

**Affinement par détails.** Système de protection KMT-5/8 visible : compatible T-72B3 modernisé.

**Outils.**
- Janes Defense Equipment.
- Oryx Spioenkop (suivi pertes équipement Ukraine).
- ARES Database.

#### 94.6 Étape 5 — Géolocalisation

**Indices.**
- Terrain semi-aride.
- Lampadaires est-européens.
- Climat compatible Europe de l'Est / Asie centrale.
- Pas de végétation tropicale.

**Hypothèses initiales.** Sud Ukraine, Crimée, Russie sud, Kazakhstan, Asie centrale.

**Triangulation visuelle.** Identification d'un détail : une pylône électrique distinctive avec configuration spécifique visible en arrière-plan, et une station-service abandonnée à droite.

**Recherche.** Google Earth sur les régions hypothétiques, à proximité de routes principales avec terrain plat semi-aride. Mapillary pour Street View communautaire.

**Hit.** Identification de la station-service abandonnée sur Google Earth (image satellite 2024) le long d'une route en Ukraine sud (région Kherson). Vérification : pylône électrique correspondant.

**Conclusion.** Géolocalisation : route P-58, Ukraine, oblast Kherson, secteur précis identifié (coordonnées GPS X,Y). Cotation : A1.

#### 94.7 Étape 6 — Chronolocation

**Indices.**
- Saison : végétation sèche, vêtements légers visibles → été ou début automne.
- Ombres : modérées, soleil bas à droite → matin ou fin d'après-midi.

**Shadow analysis.** SunCalc sur coordonnées identifiées : ombres compatibles avec **10h30-11h30 heure locale**, période **juillet-août**.

**Cross-météo.** Wolfram Alpha sur région et période : pas de précipitation, ciel dégagé. Cohérent avec vidéo.

**Affinement.** Le compte X publie la vidéo le 18 août 2024. Cohérence : prise probable la veille ou jour même.

**Conclusion.** Date probable : entre le 15 et 18 août 2024, plage horaire 10h30-11h30. Cotation : B2.

#### 94.8 Étape 7 — Cohérence avec narratif

**Narratif accompagnant.** « Convoi russe entrant en région X ».

**Vérification.**
- Géolocalisation Ukraine sud, oblast Kherson : zone effectivement contestée à cette période.
- Chars compatibles T-72B3 modernisés : équipement Russe utilisé sur ce théâtre.
- Insignes au sol : à examiner avec experts militaires.

**Cohérence.** Globalement compatible avec narratif. Mais subtilité : direction du convoi, identification des marquages spécifiques (régiment) demandent expertise militaire complémentaire.

#### 94.9 Synthèse cas

**Conclusion globale.** La vidéo est probablement authentique (B2-A1 selon dimensions), géolocalisée en Ukraine sud (A1), datée août 2024 (B2). Le narratif d'accompagnement (convoi russe en région) est compatible avec les éléments observés, sans qu'une identification précise du régiment russe ou de la mission opérationnelle puisse être conduite en OSINT pur.

**Production.** Note courte (Ch.87) au commanditaire avec captures référencées, coordonnées GPS, hypothèses identifiées, limites mentionnées.

#### 94.10 Pédagogie

Ce cas illustre :
- Authentification multi-couches (technique + recherche inversée + cohérence).
- Géolocalisation par méthode Bellingcat.
- Chronolocation par shadow analysis.
- Identification d'équipements (limites OSINT pur, expertise militaire).
- Honnêteté méthodologique sur les limites.

#### 94.11 Variantes du cas

**Variante 1 — Vidéo recyclée d'un autre conflit.** L'analyse de recherche inversée révèle que la vidéo a déjà été publiée antérieurement dans un autre contexte. Manipulation : recyclage avec narratif trompeur. Cas fréquent sur réseaux sociaux après chaque crise.

**Variante 2 — Vidéo générée par IA.** Veo, Sora, Runway peuvent produire vidéos militaires plausibles. Détection : Sensity, Intel FakeCatcher, signaux visuels (cohérence physique des objets, fumée, mouvements).

**Variante 3 — Vidéo authentique mais hors contexte.** Vidéo réelle prise il y a 2 ans, présentée comme récente. Détection : chronolocation par shadow analysis + cross-référence événements.

**Variante 4 — Vidéo composite (morceaux assemblés).** Plusieurs vidéos authentiques montées pour créer narratif faux. Détection : analyse frame par frame, ruptures de continuité, EXIF résiduels.

#### 94.12 Workflow GEOINT vidéo type

1. **Préservation** : yt-dlp, hash, capture page partage.
2. **Lecture méthodique** : inventaire visuels et audio.
3. **Authenticité technique** : EXIF, ELA frames clés, détection IA (Sensity, FakeCatcher).
4. **Recherche inversée** : frames clés sur Yandex / Google Lens / TinEye.
5. **Identification éléments** : véhicules, uniformes, signalétique.
6. **Géolocalisation** : triangulation Google Earth / OSM / Mapillary.
7. **Chronolocation** : shadow analysis + cross-météo + saison.
8. **Cohérence narratif** : confrontation au récit.
9. **Cotation et limites** : prudente, expertise complémentaire si pièce centrale.

#### 94.13 Cas de référence Bellingcat

**MH17 (2014-2018).** Géolocalisation par Bellingcat de chaque étape du convoi BUK russe à travers Ukraine. Méthode reproductible documentée.

**Skripal (2018).** Identification des deux agents GRU par cross-recherche photos, voyages, identité.

**Khashoggi (2018-2019).** Reconstitution des mouvements de l'équipe saoudienne à Istanbul.

**Ukraine (2022-2026).** Volume massif de géolocalisations, suivi des conflits avec rigueur.

**Soudan (2023-2026).** Documentation des massacres et conflits via OSINT collaborative.

Ces cas constituent le **corpus pédagogique** de référence. Étude recommandée pour formation.

-----

### Chapitre 95 — Cas pratique : dé-anonymisation d'un pseudonyme

#### 95.1 Présentation du cas

Un compte X pseudonyme `@whistleblower_fr` publie depuis 6 mois des allégations détaillées de fraude contre une grande entreprise française, en revendiquant être un ancien employé. Le cabinet d'avocats de l'entreprise mandate l'analyste pour identifier qui se cache derrière, dans le but d'une procédure en diffamation potentielle.

**Cadrage éthique préalable.** L'identification d'un lanceur d'alerte présumé soulève des enjeux. Le mandat est documenté. L'analyste s'engage à :
- Vérifier d'abord si les allégations sont publiquement étayées.
- Documenter prudemment.
- Ne pas exploiter pour intimidation.
- Limiter la diffusion au mandat (avocats de l'entreprise, pas publication, pas réseau social).
- Refuser si glissements vers harcèlement.

#### 95.2 Étape 1 — Analyse du compte

**Profil.**
- @whistleblower_fr, créé en juillet 2025.
- Photo profil : avatar génériquement « business-like » (à tester pour origine IA).
- Bio : « Ancien employé. Je dis ce que vous taisez. »
- 1842 followers, 12 followings.
- 287 posts.

**Analyse photo profil.** Hive Moderation : 78 % « AI-generated ». Optic AI or Not : « AI ». **Conclusion : photo IA, pas un visage réel.**

**Cohérence linguistique.** Style soigné, vocabulaire de cadre supérieur, références à des processus internes (RH, comité de direction, audit) avec terminologie professionnelle.

#### 95.3 Étape 2 — Analyse des posts

**Patterns.**
- 287 posts en 6 mois ≈ 1.6 / jour.
- Horaires : majoritaire 19h-23h français.
- Jours : très peu le weekend, suggérant pratique professionnelle structurée.
- Allégations factuelles spécifiques (noms de dirigeants, processus internes, chiffres).
- Pas de réponse aux mentions techniques pointues (suggère prudence opérationnelle).

**Conclusion préliminaire.** Probablement un humain, vraisemblablement avec expérience effective dans l'entreprise (cohérence des détails internes). Pseudo prudent (avatar IA).

#### 95.4 Étape 3 — Stylométrie légère

**Échantillonnage de 30 posts longs.**

**Indicateurs récurrents.**
- Tournures spécifiques (« j'ajoute », « il faut savoir que », « rappelons que »).
- Ponctuation : usage généreux du point-virgule.
- Émojis : aucune utilisation.
- Capitalisations : sobre.
- Vocabulaire : « gouvernance », « processus », « conformité », « éthique ».

**Hypothèse.** Profil cadre supérieur, formation universitaire ou ingénieur, sensibilité gouvernance / conformité (possiblement audit ou contrôle).

#### 95.5 Étape 4 — Recherche cross-plateformes

**Sherlock sur `whistleblower_fr`.** Pas d'autres comptes ce username.

**Recherche dans documents internes (sites entreprise publics).** Recherche de tournures stylométriques spécifiques détectées sur les sites publics de l'entreprise (communiqués, blog interne consulté).

**Hit faible.** Aucune correspondance directe.

**Approche alternative.** Recherche par sujets abordés. Les allégations concernent un processus spécifique : « audit interne 2022 » d'une filiale.

#### 95.6 Étape 5 — Recherches LinkedIn

**Compte d'investigation LinkedIn (compte invest mature).**

**Recherche.** Anciens employés de l'entreprise sur la période (audit interne, finance, conformité, RH supérieures).

**Filtres.** Postes « audit », « contrôle », « risque », « gouvernance », « conformité », chez l'entreprise cible entre 2020 et 2024 (a quitté entre 2024 et 2025).

**Résultats.** 23 profils correspondants.

#### 95.7 Étape 6 — Triangulation

**Croisement.**
- Profil 1 : a quitté l'entreprise en juillet 2024 (timing aligné avec création @whistleblower_fr en juillet 2025).
- Profil 1 : poste senior en audit interne 2020-2024, exposition au processus mentionné dans les posts.
- Profil 1 : signatures de mémos publics avec mêmes tournures stylométriques (« il faut savoir », « rappelons »).
- Profil 1 : photo correspondant à description vague que le compte donne accidentellement de lui-même.

**Hypothèse forte.** Profil 1 est probablement @whistleblower_fr. Cotation B2.

#### 95.8 Étape 7 — Vérifications complémentaires

**Avant conclusion, vérifications.**

**Aliase numérique.** GitHub / autres comptes de Profil 1 ? Recherche Holehe / Sherlock sur email LinkedIn présumé : aucun lien direct.

**Cohérence temporelle.** Profil 1 a-t-il signalé en interne d'abord, est-il en procès, a-t-il témoigné ailleurs ? Recherche presse : oui, mentionné dans une enquête presse 2024 comme « source anonyme proche du dossier ».

**Cohérence motivationnelle.** Profil 1 aurait pu créer @whistleblower_fr pour continuer à dénoncer publiquement après son départ. Cohérent.

#### 95.9 Étape 8 — Cotation finale et formulation

**Cotation.** B2 forte (faisceau d'indices convergents : timing, expertise, stylométrie, photo, presse anonyme). Pas A1 (pas d'aveu direct, pas de lien email/IP démontré).

**Formulation pour rapport.**

> Plusieurs éléments convergents suggèrent fortement que le compte @whistleblower_fr est probablement opéré par [Nom], ancien auditeur interne ayant quitté l'entreprise en juillet 2024. Ces éléments sont : (a) cohérence temporelle entre départ et création du compte, (b) cohérence des sujets abordés avec son périmètre d'intervention en interne, (c) cohérence stylométrique avec mémos publics signés, (d) source anonyme mentionnée dans la presse 2024 dans des termes compatibles. Niveau de confiance : probable. **Démonstration directe par lien email / IP / aveu nécessiterait approche complémentaire (réquisition judiciaire si procédure engagée).**

#### 95.10 Étape 9 — Discussion éthique

**Pour le rapport.**
- L'analyste rappelle au cabinet que [Nom] a probablement le statut de **lanceur d'alerte** au sens des dispositifs européens (directive 2019/1937) et français (loi Sapin 2 modifiée).
- Procédure abusive en diffamation peut constituer une **infraction nouvelle** (procédure-bâillon, art. 712-1 et suivants du CPP modifié).
- Recommandation : avant action en justice, audit des allégations factuelles ; si certaines sont fondées, gestion par dialogue ou enquête interne, pas action judiciaire.

L'analyste a fait son travail technique ; il assume aussi sa responsabilité morale en alertant.

#### 95.11 Pédagogie

Ce cas illustre :
- Maturité OPSEC d'une cible (avatar IA, pseudonyme).
- Triangulation par stylométrie + cohérence temporelle + cohérence thématique.
- Cotation prudente (B2 plutôt que A1 sans aveu direct).
- Responsabilité éthique de l'analyste qui peut alerter sur les conséquences possibles.
- Limite OSINT : démonstration directe demande réquisition judiciaire.

-----

### Chapitre 96 — Cas pratique : désinformation et faux comptes IA

#### 96.1 Présentation du cas

Un acteur économique majeur subit une vague d'allégations soudaines sur les réseaux sociaux, accusant l'entreprise de pratiques environnementales nocives. Les allégations apparaissent simultanément sur X, LinkedIn, Telegram, en plusieurs langues. L'analyste OSINT est mandaté pour :
- Caractériser le phénomène : organique ou coordonné ?
- Identifier les acteurs derrière.
- Évaluer la sophistication.
- Documenter pour action ultérieure.

#### 96.2 Étape 1 — Cartographie initiale

**Collecte.**
- 47 comptes X identifiés relayant les allégations (recherche par mots-clés et hashtags).
- 23 profils LinkedIn équivalents (mais difficile : LinkedIn restreint).
- 12 canaux Telegram amplifiant.
- 3 blogs dédiés (« exposing-X.com », « X-truth.eu », « la-verite-X.fr »).

#### 96.3 Étape 2 — Analyse temporelle

**Heatmap d'activité.** Les 47 comptes X publient leur premier message dans une fenêtre de 8 heures, sur 3 jours consécutifs.

**Pattern remarquable.** Création de 23 comptes parmi les 47 dans la même semaine (4-10 mai 2026), tous il y a 6-8 mois avant le pic d'activité.

**Conclusion.** Coordination temporelle très forte. Probabilité d'organique : quasi-nulle.

#### 96.4 Étape 3 — Analyse de profils

**Photos profil.** Pour les 47 comptes :
- 38 photos identifiées comme **IA-generated** (Hive Moderation > 70 %).
- 6 photos volées de banques d'images.
- 3 photos non analysables (résolution basse).

**Bios.**
- Tons similaires : « citoyen engagé », « éco-citoyen », « activiste environnemental ».
- Tournures parfois identiques mot pour mot (avec variations mineures).
- Pas de cohérence biographique vérifiable.

**Conclusion.** Faux comptes industriels.

#### 96.5 Étape 4 — Analyse de contenu

**Narratifs.**
- 3-4 messages principaux récurrents.
- Variations linguistiques mais cohérence sémantique.
- Vocabulaire technique étonnamment proche entre comptes différents.

**Stylométrie comparative.** Plusieurs comptes partagent des tournures spécifiques suggérant rédaction commune ou LLM.

**Test LLM-generated.** GPTZero sur 30 posts longs : 24/30 « likely AI-generated ». Originality : équivalent.

**Conclusion.** Contenu probablement généré par LLM, distribué entre comptes.

#### 96.6 Étape 5 — Analyse de réseau

**Construction graphe.** Maltego + Gephi sur :
- Followings / followers entre les 47 comptes.
- Retweets / replies / mentions.

**Communautés détectées.** Algorithme Louvain identifie :
- Communauté 1 : 18 comptes « activistes francophones ».
- Communauté 2 : 14 comptes « eco-conscious anglophones ».
- Communauté 3 : 11 comptes hispanophones.
- 4 comptes pivots reliant les communautés.

**Centralité.** 4 comptes pivots ont degree centrality très élevée. Hypothèse : amplificateurs principaux.

#### 96.7 Étape 6 — Infrastructure technique

**Domaines.** WHOIS sur les 3 blogs :
- `exposing-X.com` : créé 8 février 2026, registrar Namecheap, masqué RGPD.
- `X-truth.eu` : créé 11 février 2026, registrar OVH, contact email Proton.
- `la-verite-X.fr` : créé 14 février 2026, registrar Gandi, masqué.

**Cohérence temporelle.** Créations sur 6 jours.

**Hébergement.** Tous derrière Cloudflare.

**Trackers.** Recherche Google Analytics commun entre les 3 sites : oui, GA Property partagé. Pivot critique.

**Recherche DNSlytics.** GA Property identifié sur un quatrième site, non encore dans le périmètre : `eco-watcher.net`. Cluster élargi.

#### 96.8 Étape 7 — Attribution

**Hypothèses concurrentes ACH.**

| H | Description | Soutien |
|---|---|---|
| H1 | Concurrent commanditant campagne | Cohérent intérêt commercial |
| H2 | Activisme authentique avec amplification artificielle | Inco. avec IA-generated content |
| H3 | Acteur étatique étranger | Cohérence avec patterns Doppelgänger |
| H4 | Officine privée (mercenaires désinformation) | Compatible |

**Indicateurs supplémentaires.**
- Aucun élément linguistique typique d'opération étatique (pas de signature russe/chinoise typique).
- Cohérence avec opération orientée business (concurrent ou officine).

**Conclusion ACH.** **Probable** : opération coordonnée par acteur commercial ou officine de désinformation à louer (H1 ou H4). H3 résiduellement possible mais moins soutenue. H2 réfutée.

#### 96.9 Étape 8 — Production

**Note courte au mandataire (Ch.87).**

> **BLUF.** L'examen des 47 comptes X, 12 canaux Telegram, 3 blogs et 4e site identifié confirme l'existence d'une **opération de désinformation coordonnée** ciblant l'entreprise. Caractéristiques : faux comptes industriels (photos IA), contenu généré par LLM, infrastructure technique mutualisée (GA partagé), coordination temporelle stricte. Attribution probable : acteur commercial ou officine de désinformation à louer. Niveau de confiance : probable. **Recommandation : signalement aux plateformes pour suppression, documentation pour action judiciaire, réponse communicationnelle calibrée.**

#### 96.10 Étape 9 — Suite

**Actions immédiates.**
- Signalement aux plateformes (X, Telegram, blogs).
- Préservation des pièces.
- Veille active.

**Actions moyen terme.**
- Si campagne persiste : action judiciaire (atteinte à l'honneur, diffamation, parfois denigrement commercial).
- Plainte VIGINUM si caractère étatique étranger se confirmait.
- Communication ciblée pour démentir les allégations spécifiques.

#### 96.11 Pédagogie

Ce cas illustre :
- Détection rapide d'inauthenticité industrielle.
- Identification du pattern par croisement multi-dimensions (temporel, profil, contenu, infrastructure).
- Outils complémentaires : photo IA detection + LLM detection + graphe + reverse trackers.
- Attribution prudente avec ACH.
- Recommandations actionnables en plusieurs niveaux.

-----

### Chapitre 97 — Cas pratique : société opaque

#### 97.1 Présentation du cas

Une banque mandate l'analyste pour due diligence sur un nouveau client : une société immatriculée à Limassol (Chypre), dont l'UBO déclaré semble peu transparent. Avant d'ouvrir le compte, due diligence approfondie.

#### 97.2 Étape 1 — Identification

**Société.** « Apollo Trading Ltd ». Companies Registry CY : immatriculée 09/2024, capital 1000 €, activité « general trading and consulting », adresse Limassol.

**Director.** « Andreas Antoniou », résidence Limassol.

**UBO déclaré.** « Petros Sokratis », résidence à Limassol (selon registre UBO CY accessible).

#### 97.3 Étape 2 — Profilage du UBO

**Recherche « Petros Sokratis » Chypre.**
- Aucun profil LinkedIn vérifiable.
- Aucune mention presse.
- Aucune autre société immatriculée à son nom.

**Photo / identité.** Aucune photo trouvable.

**Conclusion préliminaire.** Profil suspectment minimaliste. Possible identité nominee.

#### 97.4 Étape 3 — Profilage du director

**Recherche « Andreas Antoniou » Chypre.**
- Plusieurs profils correspondant (homonymie).
- Filtrage : un certain Andreas Antoniou est administrateur de 247 sociétés selon OpenCorporates.

**Conclusion.** Director est probablement un nominee professionnel.

#### 97.5 Étape 4 — Adresse de domiciliation

**24 Athinon Street, Limassol.** OpenCorporates : 312 autres sociétés enregistrées à cette adresse.

**Conclusion.** Registered agent typique. Anonymisation.

#### 97.6 Étape 5 — Search dans ICIJ leaks

**Cyprus Confidential.** Recherche : « Apollo Trading » → pas de hit. « Petros Sokratis » → pas de hit. « Andreas Antoniou » → trop de hits (homonymie).

**Pas de leak révélateur.**

#### 97.7 Étape 6 — OpenCorporates cross-search

**Cross-recherche.** Le director « Andreas Antoniou » à 24 Athinon Street est administrateur de 247 sociétés.

**Analyse de ces 247.** Filtres par activité similaire (trading, consulting) → 84 sociétés.

**Sociétés liées plausibles.** 12 d'entre elles ont des noms semblables à Apollo Trading (Apollo Marketing, Apollo Logistics, Apollo Properties, etc.).

**Hypothèse.** Cluster de sociétés liées sous structure nominee commune. UBO réel peut être unique acteur derrière 12 sociétés.

#### 97.8 Étape 7 — Réseau et empreinte

**Recherche du nom « Apollo Trading » dans presse internationale.**
- Pas de mention récente.
- Une mention dans un site russe d'analyse économique : Apollo Trading aurait été partenaire commercial d'une entreprise russe sanctionnée.

**Cross-recherche.** Cette entreprise russe est-elle sanctionnée ? OpenSanctions : oui, depuis 2023, sanctions UE pour contournement.

**Conclusion partielle.** Lien probable Apollo → entreprise sanctionnée. Risque sérieux pour la banque.

#### 97.9 Étape 8 — Synthèse

**Conclusion globale.**

> **BLUF.** Apollo Trading Ltd présente un profil hautement opaque (capital symbolique, director nominee, UBO superficiel, adresse registered agent partagée, cluster de 12 sociétés liées). Une mention publique partielle suggère un lien commercial avec une entreprise russe sanctionnée. **Recommandation : refus d'ouverture de compte ou KYC renforcé avec demande de pièces complémentaires** (justificatifs UBO, audit indépendant). Niveau de risque : élevé.

**Cotation.** B2 globale (faisceau d'indices convergents).

#### 97.10 Pédagogie

Ce cas illustre :
- Investigation corporate avec sources publiques (Pappers, OpenCorporates, ICIJ).
- Détection de nominee professionnels.
- Cross-recherche par adresse de domiciliation pour cluster.
- Importance du screening sanctions sur **partenaires** commerciaux.
- Recommandation actionnable proportionnée.

#### 97.11 Variantes du cas

**Variante 1 — Holding luxembourgeoise.** Société dont la structure de détention passe par holding luxembourgeoise. Plus accessible que BVI (registre UBO partiel post-CJUE) mais structure profonde possible. Approfondir avec : RCS Luxembourg + LBR.lu + leaks ICIJ.

**Variante 2 — Trust irrévocable.** Société dont UBO formel est trustee d'un trust. Le bénéficiaire effectif est masqué par trust. ICIJ Pandora Papers riche en trusts. Pour OSINT, identifier le settlor, les trustees, les beneficiaries (souvent partiellement révélés dans leaks).

**Variante 3 — Cluster de sociétés liées.** Plusieurs sociétés apparemment indépendantes mais liées par : même registered agent, même director nominee, même infrastructure web (sites partageant trackers), même adresse de domiciliation. Investigation par cross-recherche OpenCorporates et Aleph.

**Variante 4 — Société de façade pour pays sanctionné.** Société européenne servant d'intermédiaire pour entreprise iranienne / russe sanctionnée. Détectable par : analyse des partenaires commerciaux mentionnés en presse, signaux de contournement (changements fréquents de dirigeants, structures multi-couches).

#### 97.12 Niveaux de risque corporate

Pour standardiser l'évaluation, **échelle de risque** structurée :

| Niveau | Indicateurs typiques | Recommandation |
|---|---|---|
| Très faible | Société transparente, dirigeants identifiés, comptes publiés cohérents, sanctions clean, adverse media absent | Onboarding standard |
| Faible | Quelques zones d'ombre (filiale offshore raisonnable, dirigeant peu public mais identifiable) | Onboarding avec questions complémentaires |
| Modéré | Opacité partielle, nominee suspectée, juridiction grise | KYC renforcé, justificatifs UBO |
| Élevé | Multi-couches offshore, registered agents communs, signaux d'alerte multiples | KYB approfondi, audit indépendant |
| Très élevé | Lien probable sanctions, contentieux multiples, opacité totale | Refus d'engagement ou escalade conformité |

#### 97.13 Workflow due diligence intégrée

Pour due diligence approfondie (au-delà du triage initial) :

1. **Identification formelle** : numéro entreprise unique, juridiction.
2. **Cartographie structurelle** : forme, capital, dates, dirigeants, UBO déclaré.
3. **Cross-références** : leaks ICIJ, registre national, OpenCorporates.
4. **Adverse media** : presse multi-langues sur 5 ans.
5. **Contentieux** : recherches juridictions principales.
6. **Sanctions / PEP** : entité + dirigeants + UBO + actionnaires.
7. **Réseau** : sociétés liées via dirigeants partagés.
8. **Activité réelle** : comparaison déclaration / observable (site web, presse, références clients).
9. **Indicateurs financiers** : comptes publiés, évolution.
10. **Infrastructure web** : domaine, hébergement, technologies.
11. **Risque géopolitique** : juridiction(s) impliquées, contexte.
12. **Synthèse cotée** : décision proportionnée.

-----

### Chapitre 98 — Cas pratique : fuite de données

#### 98.1 Présentation du cas

Une organisation découvre via veille externe qu'une fuite de données semble la concerner : un dump apparu sur un forum cybercriminel, prétendant contenir des emails internes. Le RSSI mandate l'analyste OSINT pour :
- Confirmer ou infirmer la fuite.
- Évaluer le volume et la sensibilité.
- Identifier la source probable.
- Documenter pour action légale et notification CNIL (RGPD).

#### 98.2 Étape 1 — Préservation et accès

**OPSEC stricte.** Compte d'investigation sur forum cybercriminel (compte mature, OPSEC robuste).

**Capture.** Hunchly du post de vente. Capture du sample si fourni.

**Hash** systématique.

#### 98.3 Étape 2 — Vérification

**Sample analysis.** Le vendeur fournit un sample de 10 emails. Examination :
- Format cohérent avec format internes de l'organisation.
- Adresses email correspondent aux conventions internes.
- Sujets cohérents avec l'activité.
- Métadonnées cohérentes (timestamps plausibles, expéditeurs vérifiables sur LinkedIn).

**Conclusion préliminaire.** Sample probablement authentique. Fuite confirmée (B2).

#### 98.4 Étape 3 — Estimation du volume

**Selon le post de vente.** ~50 000 emails. Période couverte : janvier-décembre 2025.

**Tarif demandé.** 25 000 $ en BTC.

**Cohérence.** Cohérent avec dump de boîte email exploitée ou avec un leak structuré (employé compromis).

#### 98.5 Étape 4 — Source probable

**Hypothèses.**

| H | Source |
|---|---|
| H1 | Compte email d'un employé compromis (phishing, stealer log) |
| H2 | Accès serveur interne (intrusion réseau) |
| H3 | Insider |
| H4 | Fournisseur cloud compromis |

**Indices.**
- Vérification Hudson Rock / SpyCloud sur domaines emails de l'organisation : plusieurs employés ont machines compromises par stealer logs récents.
- Recherche dans canaux Telegram de vente stealer logs : un dump récent contient credentials de l'organisation, dont accounts cloud.

**Conclusion préliminaire.** H1 et H4 plausibles. Possiblement combinaison.

#### 98.6 Étape 5 — Attribution

**Posteur.** Username `cyberseller22` sur le forum.

**Recherche cross-plateformes.** `cyberseller22` actif sur 3 forums. Historique : vente régulière de dumps. Pas de signature étatique.

**Conclusion attribution.** Acteur criminel privé (broker). Pas opération étatique apparente. Pas attribution précise possible en OSINT.

#### 98.7 Étape 6 — Action

**Immédiat.**
- Notification CNIL (RGPD art. 33) : sous 72 heures de la confirmation de la fuite.
- Préservation des pièces (hash + captures Hunchly).
- Communication interne (RSSI + direction).
- Audit interne (qui est compromis ? quels emails ont fuité ?).
- Réinitialisation des accès des comptes compromis.
- Notification des personnes concernées si données personnelles (RGPD art. 34).

**Court terme.**
- Plainte pénale (intrusion, vol de données, recel).
- Recherche éventuelle d'acquisition contrôlée du dump (zone juridique : à valider avec avocats).
- Veille proactive pour d'autres apparitions.

#### 98.8 Étape 7 — Production

**Rapport RSSI.**

> **BLUF.** Une fuite de données a été identifiée sur forum cybercriminel, contenant probablement ~50 000 emails internes 2025. Cotation : B2 (sample vérifié, volume non confirmé). Source probable : compromission de comptes employés via infostealers. Risques : exposition de données commerciales, fuite RGPD, opportunités d'extorsion. **Recommandations : notification CNIL immédiate, réinitialisation comptes compromis, audit, communication maîtrisée.**

#### 98.9 Étape 8 — Suite

**Veille post-rapport.**
- Surveillance des autres forums.
- Surveillance des canaux Telegram pour publications progressives.
- Alertes en cas de leak public.

#### 98.10 Pédagogie

Ce cas illustre :
- OSINT pour CTI défensive.
- Workflow notification CNIL.
- Identification source via stealer logs (Hudson Rock).
- Cadre légal RGPD strict.
- Coordination avec RSSI / RGPD / avocats.

-----

### Chapitre 99 — Cas pratique : OPSEC défensive sur Telegram

#### 99.1 Présentation du cas

Un dirigeant d'organisation reçoit, via Telegram, des messages anonymes le menaçant et révélant des informations personnelles sur sa famille. L'analyste OSINT est mandaté pour :
- Identifier la source des messages.
- Évaluer la menace.
- Renforcer l'OPSEC de la cible.
- Documenter pour suite judiciaire.

#### 99.2 Étape 1 — Préservation

**Captures.** Tous les messages reçus, profil du compte expéditeur, photos partagées, liens.

**Hashes**, horodatage.

#### 99.3 Étape 2 — Profil du compte expéditeur

**Username.** `@MrAnonymous2026`.

**Photo profil.** Avatar générique.

**Bio.** Vide.

**Numéro.** Masqué (mode anonyme).

**Date de création.** 2 jours avant le premier message.

**Conclusion.** Compte burner créé pour l'opération.

#### 99.4 Étape 3 — Pivots

**Username search.** Sherlock sur `MrAnonymous2026` : aucun résultat ailleurs.

**Photo profil reverse search.** Yandex : photo apparaît sur Unsplash (image stock). Non discriminante.

**Analyse stylométrique des messages.** Style soigné, vocabulaire fluent, références culturelles françaises (proverbes, expressions idiomatiques).

#### 99.5 Étape 4 — Contenu des messages

**Informations révélées sur la famille de la cible.**
- Nom du conjoint (info publique LinkedIn).
- Nom des enfants (info publique via réseaux sociaux conjoint).
- Lieux fréquentés (école des enfants, club de sport).
- Détails sur l'emploi du temps.

**Conclusion.** L'expéditeur a accès à informations relatives à la famille — soit issues d'OSINT propre, soit issues d'observation physique, soit issues d'un proche.

#### 99.6 Étape 5 — Cartographie de l'exposition de la famille

**Recherche.** Que voit-on publiquement sur la famille ?
- Conjoint : LinkedIn public, Instagram public avec photos famille.
- Enfants : tags sur photos Instagram du conjoint.
- École : identifiable via géolocalisation des photos.
- Emploi du temps : posts réguliers permettant déduction.

**Conclusion.** Toutes les informations révélées par l'expéditeur peuvent être obtenues via OSINT sans observation physique. La source est plausiblement un OSINT-savvy adversaire.

#### 99.7 Étape 6 — Évaluation de la menace

**Tonalité.** Menaçante mais pas explicitement violente. Niveau intermediate.

**Demande.** Réclamations financières.

**Pattern.** Comparable à pattern d'extorsion classique.

**Conclusion.** Menace réelle mais probablement opérée par acteur isolé ou petit groupe. Pas signature crime organisé.

#### 99.8 Étape 7 — Identification de la source

**Limites OSINT.**
- Telegram coopère pour LEA mais pas pour OSINT privé.
- Réquisition judiciaire nécessaire pour obtenir IP et numéro de téléphone derrière le compte burner.

**Action.** Dépôt de plainte (extorsion, harcèlement). Le PNAT ou parquet local peut requérir Telegram (depuis l'arrestation Durov 2024, coopération renforcée).

#### 99.9 Étape 8 — Mesures défensives OPSEC

**Pour la cible.**
- Renforcement OPSEC familial : revue des comptes réseaux sociaux du conjoint et enfants, restrictions visibilité.
- Suppression des photos d'enfants identifiables.
- Géolocalisation strippée.
- Communication d'évitement avec l'expéditeur (pas répondre, conserver les messages).
- Plainte pénale.
- Vigilance physique renforcée si menaces persistent.

#### 99.10 Étape 9 — Production

**Note au dirigeant.**

> **BLUF.** Les messages anonymes proviennent d'un compte Telegram burner créé pour l'opération. Les informations révélées sont compatibles avec une collecte OSINT exclusive (pas nécessairement observation physique). Le pattern correspond à une extorsion par individu / petit groupe, sans signature crime organisé. **Recommandations : plainte pénale immédiate (réquisitions Telegram), renforcement OPSEC familial, vigilance physique, accompagnement juridique.**

#### 99.11 Pédagogie

Ce cas illustre :
- OSINT défensif (protection cible).
- Cartographie de la surface d'attaque personnelle.
- Évaluation de la menace.
- Recours nécessaire à la procédure judiciaire pour pivots techniques (réquisitions plateformes).
- Conseil OPSEC personnel.

-----

### Chapitre 100 — Cas pratique : CTI infrastructure suspecte

#### 100.1 Présentation du cas

Un SOC détecte des tentatives de connexion suspectes depuis une IP particulière vers l'infrastructure de l'organisation. L'analyste OSINT est mandaté pour caractériser l'infrastructure adverse en sources ouvertes : qui possède cette IP, quelle infrastructure y est associée, quel acteur potentiel.

#### 100.2 Étape 1 — IP de départ

**IP.** `185.XXX.XXX.XXX`.

**Première analyse.**
- ipinfo.io : géoloc Pays-Bas, ASN AS56xxx « XXX Hosting LLC ».
- AbuseIPDB : 47 signalements abus récents.
- VirusTotal : associée à plusieurs malwares.

#### 100.3 Étape 2 — ASN et reverse IP

**ASN.** `XXX Hosting LLC` : hébergement type « bulletproof » avec historique d'usage criminel.

**Reverse IP.** 87 sites hébergés sur cette IP. Examen :
- 12 domaines avec patterns de typosquatting bancaires.
- 23 domaines avec aspect phishing.
- 14 domaines avec activité douteuse (carding).

**Conclusion.** IP très probable d'infrastructure criminelle.

#### 100.4 Étape 3 — Domaines liés

**Sur l'IP.** Identification de domaines actifs avec dernière activité.

**Cross-recherche.** Un domaine `update-windows[.]com` est notamment actif et utilisé pour phishing crédentiels Windows.

**Recherche dans bases CTI.**
- abuse.ch URLhaus : confirmé URL malveillante.
- VirusTotal : associé à malware Vidar.
- MalwareBazaar : sample disponible (hash documenté).

#### 100.5 Étape 4 — Acteur

**Vidar.** Infostealer connu, vendu sur forums russophones depuis 2018.

**Operators.** Plusieurs groupes utilisent Vidar (modèle MaaS — Malware-as-a-Service). Attribution précise difficile.

**Recherche complémentaire.** Le domaine `update-windows[.]com` a été enregistré récemment (3 mois). Recherche WHOIS historique : email enregistrement masqué.

**Recherche dans canaux Telegram cybercriminels.** Un canal vend des « configs Vidar ready-to-use » avec mention d'un C2 server identique à l'IP examinée. Vendeur : `@vidar_panels`. Compte actif depuis 1 an.

#### 100.6 Étape 5 — Pivots supplémentaires

**Sur l'opérateur supposé `@vidar_panels`.**
- Username Telegram unique.
- Activité : vente de panels Vidar et de stealer logs associés.
- Géographie : posts en russe, anglais international.

**Cross-recherche.** `vidar_panels` apparaît également sur XSS forum (russophone cybercriminel). Membre depuis 18 mois.

**Conclusion.** Acteur cybercriminel privé opérant un C2 Vidar et vendant accès. Pas signature étatique apparente.

#### 100.7 Étape 6 — IOCs consolidés

**Liste d'IOCs.**
- IP `185.XXX.XXX.XXX`.
- Domaines : `update-windows[.]com`, `[autres]`.
- Hashes Vidar samples : [SHA-256].
- TTPs : phishing email → Vidar dropper → C2 → exfiltration browser data.

**Format STIX/TAXII** pour partage MISP communauté.

#### 100.8 Étape 7 — Recommandations défensives

**Pour l'organisation.**
- Bloquer IP + domaines identifiés.
- Hunt sur réseau : recherche d'IOCs sur logs historiques.
- Awareness employés : phishing Windows.
- Renforcement EDR sur postes Windows.
- Veille active sur acteur `@vidar_panels`.

**Partage.** IOCs partagés via MISP communauté (TLP:AMBER).

#### 100.9 Étape 8 — Production

**Note CTI.**

> **BLUF.** L'IP `185.XXX.XXX.XXX` identifiée comme C2 Vidar opéré par l'acteur cybercriminel privé `@vidar_panels`. Infrastructure associée comprend 87+ domaines, dont `update-windows[.]com` (phishing Windows). Pas de signature étatique. **Recommandations : blocage immédiat, hunt sur logs, awareness employés, partage IOCs MISP.**

#### 100.10 Pédagogie

Ce cas illustre :
- OSINT pour CTI.
- Pivots infrastructure → acteur.
- Combinaison sources publiques + Telegram observation.
- Partage MISP responsable.
- Limites attribution (acteur privé, pas étatique).

#### 100.11 Variantes et extensions du cas

**Variante 1 — Attribution étatique.** Si les signaux pointent vers acteur étatique (APT documenté), méthodologie différente :
- Cross-référence rapports vendeurs (CrowdStrike, Mandiant, Microsoft).
- Comparaison TTPs avec groupes connus.
- Identification de signatures spécifiques (custom malware, code patterns).
- Attribution avec cotation prudente (ICD-203).

**Variante 2 — Supply chain attack.** L'IP suspecte pointe vers fournisseur ou prestataire de l'organisation. Investigation cross-organisationnelle, coopération CSIRT.

**Variante 3 — Insider threat.** Pattern suggère origine interne. Investigation OPSEC sensible, collaboration RH et juridique.

**Variante 4 — Coordinated multi-target campaign.** L'infrastructure observée vise plusieurs organisations simultanément. Partage MISP critique pour défense collective.

#### 100.12 Threat hunting proactif

Au-delà de la réponse à incident, le **threat hunting** OSINT :

**Sources à monitorer en continu.**
- abuse.ch (URLhaus, MalwareBazaar, ThreatFox) : nouveaux IOCs.
- AlienVault OTX : community CTI.
- Twitter/X CTI community (chercheurs et SOCs).
- Telegram canaux cybercriminels (observation passive).
- Forums (XSS, Exploit en surface ; dark web pour avancé).
- ANSSI bulletins, CISA alerts, NCSC alerts.
- Vendor reports (CrowdStrike, Mandiant, Microsoft, Kaspersky, Group-IB).

**Workflow hunt.**
1. Sélection d'un acteur ou TTP à surveiller.
2. Collecte IOCs et TTPs publiquement attribués.
3. Recherche dans logs internes (SIEM).
4. Identification de signaux faibles.
5. Confirmation ou réfutation.
6. Documentation et alimentation MISP interne.

#### 100.13 Maturité CTI organisationnelle

**Niveau 1 — Reactive.** Réponse aux IOCs partagés par CERT-FR ou vendor. Outils basiques (SIEM, EDR).

**Niveau 2 — Proactive.** Monitoring veille externe, hunting régulier, partage MISP communauté.

**Niveau 3 — Strategic.** Analyse de tendances, anticipation, coordination internationale, sponsoring de recherche, threat modeling stratégique.

**Pour OSINT externe.** Le master OSINT permet d'atteindre niveau 2 sur les composantes externes. Niveau 3 demande investissement institutionnel (CrowdStrike Falcon X, Recorded Future, Mandiant Advantage, équipe dédiée).

-----

### Chapitre 101 — Cas pratique : triage financier / crypto

#### 101.1 Présentation du cas

Un cabinet d'avocats mandate l'analyste pour triage initial sur une affaire impliquant flux crypto suspects entre plusieurs entités. Objectif : déterminer si l'affaire mérite expertise crypto forensique professionnelle, ou si elle se limite à un triage simple.

#### 101.2 Étape 1 — Cadrage

**Sujet.** Société française « EuroTrade » suspecte des flux crypto vers entités opaques. Plainte du DAF.

**Périmètre.** Triage initial en sources ouvertes pour orienter la suite.

**Bornes.** Pas d'analyse on-chain profonde (renvoi cours OSINT Crypto vFULL si nécessaire).

#### 101.3 Étape 2 — Sociétés impliquées

**EuroTrade SAS (France).** Pappers : société de trading B2B, CA 23 M€.

**Partenaire 1 : Glacier Capital Ltd (BVI).** OpenCorporates : société BVI, données très limitées.

**Partenaire 2 : SkyChain DMCC (UAE).** Limited public info.

#### 101.4 Étape 3 — Flux observables

**Indicateurs.**
- Comptes EuroTrade montrent ligne « services financiers internationaux » de 4.2 M€ sur 2024-2025.
- Pas de détail public.

**Hypothèse.** Ces flux peuvent transiter en crypto.

#### 101.5 Étape 4 — Pivots crypto en surface

**Recherche.** EuroTrade publiquement enregistrée sur exchange crypto ? Pas de mention publique.

**Wallets connus.** EuroTrade a-t-elle wallet public connu (Etherscan ENS, mention site web) ? Non identifiable.

**SkyChain DMCC.** Dubai-based, mention dans rapports d'analyses sectorielles comme intermédiaire crypto-fiat.

**Glacier Capital BVI.** Aucune empreinte crypto identifiable en surface.

#### 101.6 Étape 5 — Limites du triage

**Constat.** En surface, peu d'éléments pour conclure. Les flux crypto, s'ils existent, transitent par adresses non publiquement liées aux sociétés en source ouverte.

**Pour aller plus loin.** Nécessaire :
- Identification de wallets via réquisitions exchanges (compétence judiciaire).
- Clustering on-chain par cabinet spécialisé (Chainalysis, TRM, Elliptic).
- Cross-référence avec adresses sanctionnées.
- Analyse des bridges utilisés (cross-chain).

**Renvoi.** Cours OSINT Crypto vFULL pour l'expertise approfondie. Recommandation au cabinet d'avocats : faire intervenir cabinet spécialisé crypto forensique.

#### 101.7 Étape 6 — Production

**Note de triage.**

> **BLUF.** Le triage OSINT initial sur EuroTrade et ses partenaires Glacier Capital (BVI) et SkyChain (UAE) ne permet pas de caractériser publiquement les flux crypto suspectés. Les éléments visibles (ligne comptable « services financiers internationaux » de 4.2 M€) sont cohérents avec hypothèse de flux opaques, sans démonstration directe en source ouverte. **Recommandation : expertise crypto forensique professionnelle pour clustering on-chain et identification des wallets ; coordination procédure pénale pour réquisitions exchanges.**

#### 101.8 Pédagogie

Ce cas illustre :
- Triage initial OSINT crypto.
- Identification rapide des limites du master.
- Renvoi explicite vers cours spécialisé.
- Recommandation actionnable proportionnée.
- Honnêteté méthodologique : ne pas sur-affirmer ce qu'on ne peut pas voir.

#### 101.9 Élargissement — variantes de triage crypto

**Variante 1 — Wallet identifié publiquement.** L'entité a publié son adresse ENS ou wallet en clair. Triage : Etherscan, historique transactions, contreparties. Pivots possibles si DeFi avec adresses labellisées.

**Variante 2 — Stealer log avec credentials exchange.** Email cible apparaît dans stealer log avec accès Binance / Coinbase. Triage : confirmation usage exchange, hypothèses sur volumes (sans accès au compte). Escalade : exchange réquisition.

**Variante 3 — Donation publique à organisation.** L'entité a fait donation crypto à organisation (publique sur Etherscan). Pivot : identité publique → wallet. Réutilisation du wallet pour autres flux.

**Variante 4 — Rug pull / scam identification.** Investigation d'un projet crypto frauduleux. Identification des wallets fondateurs, suivi du cashout, identification des plateformes utilisées. Souvent traçable sur quelques étapes avant mixer.

**Variante 5 — Sanctions evasion via crypto.** Investigation sur entité sanctionnée. Recherche d'adresses publiques (OFAC SDN crypto list). Suivi des contournements (mixers, bridges, P2P).

#### 101.10 Méthodologie triage spécifique sanctions

Pour vérification rapide :

1. **Liste OFAC** : OFAC SDN crypto addresses list à jour (mise à jour fréquente).
2. **Chainalysis Sanctions Screening** (gratuit pour adresses individuelles).
3. **TRM Labs Public** (limité gratuit).
4. **Cross-recherche** : adresses associées (clusters connus).

**Limites.** L'OSINT pur ne peut pas garantir absence de sanction (adresses nouvelles, clustering avancé requis). Pour conformité institutionnelle, outils payants nécessaires (Chainalysis KYT, TRM, Elliptic Lens).

#### 101.11 Coordination OSINT crypto + classique

Le cas typique mobilise OSINT classique ET crypto :

**OSINT classique.** Identifie entités, sociétés, contextes, indices de flux.

**OSINT crypto.** Identifie adresses, patterns on-chain, sanctions.

**Coordination.**
- Pivots email/username → adresse crypto via réseaux sociaux ou ENS.
- Pivots crypto → email/identité via leaks ou KYC d'exchange (judiciaire).
- Pattern d'ensemble (offshore + crypto + désinformation) en cohérence.

Pour MIRAGE : le compte Binance personnel de Delaunay identifié via stealer log (OSINT classique) ouvre le pivot crypto. La profondeur (clustering on-chain, attribution wallets) renvoie cours OSINT Crypto vFULL.

-----

### Chapitre 102 — Exercice final non guidé

#### 102.1 Présentation de l'exercice

Cet exercice **non guidé** est conçu comme un test de synthèse complet du master OSINT. L'apprenant le conduit en autonomie, avant consultation du corrigé (Ch.103).

**Scénario fictif.** Un cabinet d'avocats vous mandate (cabinet « Marchand & Partenaires », spécialisé en contentieux corporate) pour conduire une enquête OSINT préalable à un audit comptable. La cible est **Solène Faure**, directrice générale d'une société française « VenturaTech SAS » (PME dans la transition énergétique, CA 18 M€, 65 employés). 

Les soupçons portés par un actionnaire minoritaire qui mandate le cabinet :
1. Mme Faure aurait organisé des conventions réglementées avec une société de conseil « Lumière Stratégie » dont elle serait elle-même bénéficiaire indirecte.
2. Cette société de conseil aurait été créée à Luxembourg pour bénéficier d'un régime fiscal favorable, mais pourrait être en réalité un véhicule de détournement.
3. Plusieurs communiqués positifs récents sur VenturaTech sembleraient avoir été amplifiés artificiellement sur réseaux sociaux.
4. Le compagnon de Mme Faure (M. Vidal) aurait pu utiliser des informations privilégiées pour des opérations boursières (VenturaTech non cotée mais détient participation dans société cotée).

#### 102.2 Mandat formel

Cabinet **Marchand & Partenaires** mandate l'analyste pour :
- **Périmètre.** Investigation OSINT sur Solène Faure (DG VenturaTech), VenturaTech SAS, Lumière Stratégie (Luxembourg), et M. Pierre Vidal (compagnon). Sources ouvertes exclusivement.
- **Durée.** 3 semaines.
- **Livrable.** Rapport complet + fiches entités + recommandations actionnables.
- **Cadre.** Préparation procédure civile (action sociétaire) avec saisine éventuelle PNF si éléments le justifient.
- **TLP.** AMBER+STRICT.

#### 102.3 Tâche pour l'apprenant

**Formuler.**
- 5 questions de renseignement (IR) couvrant les 4 soupçons.
- Inventaire de sources prioritaires par IR.
- Plan de collecte sur 3 semaines.
- Identification des risques juridiques et éthiques.
- Configuration OPSEC initiale.

**Conduire mentalement / par écrit.**
- Pour chaque IR, identification des outils et méthodes mobilisés.
- Anticipation des cotations attendues.
- Identification des limites et zones d'ombre.
- Préparation des escalades possibles (cours spécialisés).

**Produire.**
- Structure du rapport final.
- Executive summary anticipé (BLUF).
- Plan des annexes.

#### 102.4 Aide minimale

L'exercice est **non guidé**. Cependant, quelques jalons sont fournis pour cadrage :

- L'enquête doit articuler les chapitres précédents (cadrage Ch.12, sources Ch.13, méthodologie Ch.18, identité Ch.26, SOCMINT Ch.31-35, sociétés Ch.36-38, infrastructure Ch.39-41, breaches Ch.42-43, deepfakes / désinfo Ch.53-59 et 76, FININT Ch.70-71, raisonnement Ch.79-86, production Ch.87-92).
- Le candidat doit utiliser le vocabulaire Admiralty + WEP systématiquement.
- Le candidat doit identifier explicitement les points d'escalade vers cours FININT vFULL et OSINT Crypto vFULL (si applicable).

#### 102.5 Critères d'évaluation

L'évaluation porte sur :

**Cadrage (15 %).**
- IR formulées correctement (fermées, vérifiables, couvrent le périmètre).
- Bornes explicites.
- OPSEC adaptée.

**Méthodologie (25 %).**
- Outils et sources pertinents par IR.
- Plan de collecte réaliste.
- Anticipation des limites.

**Cotation (15 %).**
- Application Admiralty / WEP.
- Discipline (pas de surenchère, pas de timidité).

**Anti-biais (15 %).**
- ACH sur IR principales.
- Identification des biais.
- Devil's advocate.

**Production (20 %).**
- Structure du rapport.
- Executive summary calibré.
- Recommandations actionnables.

**Éthique (10 %).**
- Respect des bornes.
- Posture défensive.
- Signalements éventuels (lanceur d'alerte ?).

#### 102.6 Recommandations pratiques

**Avant de commencer.**
- Prenez 1 heure pour structurer le cadrage.
- Identifiez les pivots probables avant de plonger dans la collecte mentale.
- Soyez réaliste sur les durées (3 semaines).

**Pendant.**
- Conservez un journal de votre raisonnement.
- Hiérarchisez les priorités (les 4 soupçons ne sont pas équivalents).
- Identifiez tôt les escalades probables.

**Après.**
- Comparez avec le corrigé (Ch.103).
- Identifiez les écarts et les leçons.

#### 102.7 Conditions de réalisation

L'exercice peut être conduit :
- **En totalité « papier »** : raisonnement écrit sans outils.
- **Avec outils mais sans cible réelle** : structuration d'un plan d'enquête avec les outils, sans investiguer une vraie personne (l'exercice est fictif).
- **En atelier collectif** : équipe d'apprenants discute et compare.

**Durée recommandée.** 4-6 heures pour cadrage et plan, sans aller jusqu'à exécution complète.

#### 102.8 Synthèse

Cet exercice met l'apprenant face à la **complexité réelle** d'une enquête OSINT multi-dimensionnelle. Il oblige à mobiliser **simultanément** ce qui a été appris au fil du cours. Le corrigé qui suit (Ch.103) propose une lecture détaillée des choix attendus.

-----

### Chapitre 103 — Corrigé détaillé de l'exercice final

#### 103.1 Approche du corrigé

Le présent corrigé n'est **pas une solution unique**. Plusieurs cadrages valides sont possibles. Il propose une trame de référence permettant à l'apprenant de comparer ses choix et d'identifier les axes de progression.

#### 103.2 Cadrage attendu — IR proposées

**IR1.** Solène Faure bénéficie-t-elle, directement ou indirectement, économiquement de Lumière Stratégie Sàrl (Luxembourg) ?

**IR2.** Les conventions réglementées entre VenturaTech SAS et Lumière Stratégie sont-elles conformes aux processus statutaires (autorisation conseil d'administration, déclaration commissaire aux comptes) ?

**IR3.** Les communiqués positifs récents sur VenturaTech ont-ils été amplifiés artificiellement sur les réseaux sociaux, et si oui, qui est plausiblement à l'origine ?

**IR4.** M. Pierre Vidal a-t-il, dans la période considérée, conduit des opérations boursières publiquement visibles compatibles avec usage d'informations privilégiées concernant la participation de VenturaTech dans une société cotée ?

**IR5.** Y a-t-il d'autres signaux d'alerte (sanctions, PEP, adverse media, contentieux) sur Solène Faure, M. Vidal, ou VenturaTech qui ressortiraient de l'investigation OSINT ?

#### 103.3 Bornes et OPSEC

**Bornes.**
- Sources ouvertes exclusivement.
- Pas d'ingénierie sociale active.
- Pas de surveillance physique.
- Pas d'accès aux comptes privés sans nécessité absolue.
- Respect RGPD strict.

**OPSEC.**
- VPN no-log + Tor pour les recherches sensibles.
- Comptes d'investigation matures (LinkedIn, X, Instagram).
- Captures Hunchly systématiques.
- Vault Obsidian local chiffré + knowledge graph local (Neo4j).
- LLMs locaux (Ollama Llama 3.3) pour tâches sensibles.

#### 103.4 Plan de collecte sur 3 semaines

**Semaine 1 — Cadrage et fondations.**

- Jours 1-2 : Cartographie sources, configuration outils, OPSEC.
- Jours 3-5 : Identification fiable de Solène Faure (LinkedIn, presse, Pappers).
- Jours 6-7 : Cartographie corporate VenturaTech (Pappers, BODACC, communiqués).

**Semaine 2 — Approfondissement.**

- Jours 8-9 : Investigation Lumière Stratégie Luxembourg (RCS Luxembourg, OpenCorporates, ICIJ leaks).
- Jours 10-11 : Investigation M. Vidal (identité, parcours, publications).
- Jours 12-13 : SOCMINT et analyse cluster communiqués (IR3).
- Jour 14 : Synthèse intermédiaire, ajustement.

**Semaine 3 — Convergence et production.**

- Jours 15-16 : Cross-référencement, ACH sur 5 IR.
- Jours 17-18 : Rédaction fiches entités.
- Jours 19-20 : Rédaction rapport.
- Jour 21 : Validation interne, hash, livraison.

#### 103.5 Outils mobilisés par IR

**IR1 — Bénéfice indirect.**
- Pappers / Infogreffe (TechnoVert structure).
- RCS Luxembourg + LBR.lu (Lumière Stratégie).
- ICIJ Offshore Leaks Database.
- OpenCorporates cross-juridictions.
- Recherche presse sur Faure / Lumière.

**IR2 — Conventions réglementées.**
- BODACC (modifications statutaires VenturaTech).
- Procès-verbaux AG si publics.
- Communiqués déclaration conventions.
- Presse spécialisée.

**IR3 — Amplification artificielle.**
- X / LinkedIn analyse réseau.
- Comptes amplificateurs : photos profil (Hive Moderation pour IA).
- Stylométrie comparative LLM-generated.
- Analyse temporelle (cadence, synchronisations).
- Recherche infrastructure (sites tiers amplifiant).

**IR4 — Usage information privilégiée par Vidal.**
- Presse boursière sur société cotée mentionnée.
- AMF déclarations dirigeants si Vidal lié.
- Publication des transactions au-dessus de seuils.
- LinkedIn / réseaux : indices sur intérêt boursier de Vidal.

**IR5 — Signaux d'alerte généraux.**
- OpenSanctions.
- WorldCheck si accessible.
- Adverse media multi-langues.
- Légifrance, Doctrine.fr (contentieux).

#### 103.6 Cotations anticipées

**Cotations attendues pour les faits clés.**

| Fait type | Cotation typique |
|---|---|
| Identification corporate via Pappers | A1 |
| Identification UBO Luxembourg via LBR | A1 |
| Présence dans ICIJ leak | B2 |
| Compte X verrouillé / privé | non cotable directement |
| Amplification artificielle détectée par signaux convergents | B2 |
| Communiqué officiel | A1 |
| Article presse établie | B2 |
| Stylométrie comparative LLM | B3 |
| Photo IA détectée Hive Moderation | A1 sur la détection, B2 sur l'attribution opérateur |

#### 103.7 ACH sur IR1 et IR3 (illustration)

**ACH IR1 — Bénéfice indirect Faure / Lumière.**

| Évidence | H1 (béné. dir) | H2 (consultante régulière) | H3 (pas de lien éco) |
|---|---|---|---|
| Faure ou famille citée RCS Lumière | (à vérifier) | — | — |
| Conventions réglementées TechnoVert ↔ Lumière | C | C | I |
| ICIJ Pandora mention | (à vérifier) | — | — |
| Taille des flux vs activité réelle | (à vérifier) | (à vérifier) | (à vérifier) |
| Capital symbolique Lumière | C | C | C |
| Pas d'autres clients connus de Lumière | C | I | C |

**ACH IR3 — Amplification artificielle.**

| Évidence | H1 (campagne coordonnée) | H2 (engagement organique) | H3 (mix légèrement amplifié) |
|---|---|---|---|
| Photos IA dans cluster amplificateur | C | I | C |
| Cadence parfois inhumaine | C | I | C |
| Tournures stylométriques répétées | C | I | C |
| Comptes créés en lot | C | I | C |
| Mentions par influenceurs authentiques | N | C | C |

**Lecture.** Sur IR3, H2 réfutée. H1 fortement soutenue. H3 plausible (campagne coordonnée + amplification organique consécutive).

#### 103.8 Limites identifiées

**À documenter dans le rapport.**
- Registre UBO Luxembourg accès partiel post-CJUE.
- Conventions réglementées détaillées non publiques (accès actionnaire seul, ou expertise comptable).
- Identification précise de chaque acteur derrière les comptes amplificateurs limitée sans réquisitions plateformes.
- Identification précise du commanditaire derrière la campagne d'amplification limitée.
- Transactions Vidar (si elles existent) non visibles publiquement sans accès aux comptes-titres.
- Cross-recherche crypto limitée (renvoi cours OSINT Crypto vFULL si signaux).

#### 103.9 Escalades à recommander

**Vers expertise dédiée.**
- Audit comptable forensique VenturaTech 2020-2025 (sur conventions réglementées et flux Lumière).
- Expertise crypto forensique si signaux apparaissent (renvoi OSINT Crypto vFULL).
- Expertise numérique sur contenus IA et campagne d'amplification.

**Vers procédure.**
- Action sociétaire (cabinet mandataire).
- Saisine PNF si éléments suggèrent fraude fiscale.
- Saisine AMF si Vidar lié à transaction boursière concrète.
- Signalement TRACFIN si élément blanchiment.

#### 103.10 Structure du rapport final

**Cohérente avec Ch.88.**

- Page de garde + classification.
- Executive summary 2 pages avec BLUF.
- Cadrage du mandat.
- Méthodologie.
- 5 sections IR avec faits cotés, ACH résumé, conclusion calibrée.
- Synthèse intégrée.
- Recommandations actionnables.
- Limites globales.
- Annexes : fiches entités, matrices ACH, timeline, graphe, catalogue pièces.

#### 103.11 Executive summary type

> **BLUF.** L'investigation OSINT conduite sur le périmètre Solène Faure / VenturaTech / Lumière Stratégie / Pierre Vidal identifie : (a) probable lien économique entre Faure et Lumière Stratégie Sàrl (B2, cohérence convergente, démonstration directe demande expertise), (b) conventions réglementées documentées mais opacité sur conditions économiques (B3), (c) campagne d'amplification artificielle des communiqués positifs très probable (B1-A1, signaux techniques convergents), (d) absence d'élément public direct concernant transactions boursières de M. Vidar (D-F selon signaux), (e) absence de sanctions, PEP, adverse media majeur sur les acteurs (A1). **Niveau de confiance global : probable** sur l'architecture des soupçons, **élevé** sur les signaux factuels individuels, **modéré** sur l'attribution finale des campagnes d'amplification.
>
> **Recommandations principales.** (1) Audit comptable forensique VenturaTech 2020-2025 par expert inscrit. (2) Action sociétaire prudente avec demande pièces conventions réglementées. (3) Signalement AMF et expertise complémentaire sur amplification réseaux sociaux. (4) Si éléments fraude fiscale se précisent, dénonciation art. 40 vers PNF.

#### 103.12 Pédagogie du corrigé

L'apprenant compare :
- Sa formulation d'IR (cohérence, couverture).
- Son plan de collecte (réalisme).
- Sa mobilisation d'outils (pertinence par IR).
- Sa pratique de cotation (discipline Admiralty + WEP).
- Son anti-biais (ACH, devil's advocate).
- Sa production (BLUF, structure, recommandations).
- Son éthique (bornes, signalements potentiels).

**Indicateurs de qualité dans la réponse.**
- IR fermées et vérifiables.
- OPSEC mentionnée explicitement.
- Cotations utilisées correctement.
- ACH mentionné.
- Limites assumées.
- Escalades vers cours spécialisés identifiées.
- Recommandations actionnables proportionnées.

**Indicateurs de faiblesse.**
- IR ouvertes ou vagues.
- Sur-affirmation (« il est certain que »).
- Pas de cotation.
- Pas de devil's advocate.
- Pas de limites mentionnées.
- Recommandations vagues.

#### 103.13 Synthèse du master

L'exercice final, et son corrigé, **achèvent** le master OSINT. L'apprenant a parcouru :
- Doctrine et cadre (Parties I-II).
- Méthodologie (Partie III).
- Sources et techniques (Parties IV-VIII).
- IA et automatisation (Partie IX).
- Passerelles spécialisées (Partie X).
- Analyse structurée (Partie XI).
- Production (Partie XII).

L'analyste OSINT 2026 issu de ce master :
- Maîtrise les sources et outils du domaine.
- Applique une cotation rigoureuse.
- Conduit une analyse anti-biais.
- Produit des livrables professionnels.
- Respecte un cadre déontologique strict.
- Coopère avec les domaines spécialisés.
- Évolue avec l'écosystème.

Le master n'est jamais achevé : la formation continue, la pratique sur cas réels (avec déontologie), la veille permanente sur outils et méthodes sont indispensables.

> **Mot final.** L'OSINT mature en 2026 est une discipline d'**équilibre** : entre rigueur et créativité, entre exhaustivité et économie, entre puissance des outils IA et garde de la responsabilité humaine, entre proximité et distance critique avec les sources. Cet équilibre n'est pas un point d'arrivée ; c'est une posture quotidienne. Le présent cours en donne les fondements ; le métier en révèle la profondeur.

-----
