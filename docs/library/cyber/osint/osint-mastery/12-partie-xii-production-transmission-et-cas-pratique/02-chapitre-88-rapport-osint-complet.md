---
title: Chapitre 88 — Rapport OSINT complet
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 88.1 Du flash au dossier

Un **rapport OSINT complet** est la formalisation finale d'une enquête de moyenne à longue durée. Là où la note courte tient sur une page, le rapport complet va de 10 à 100 pages selon la complexité, avec annexes pouvant ajouter autant.

Le rapport sert plusieurs publics : commanditaire opérationnel, hiérarchie, magistrat, expert tiers, archivage institutionnel. Il doit être **autonome** : un lecteur n'ayant pas participé à l'enquête doit pouvoir le comprendre intégralement.

## 88.2 Structure type d'un rapport OSINT complet

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

## 88.3 Page de garde et versioning

La page de garde porte une **mention de version** explicite : « v1.0 — émission initiale », « v1.1 — correction faits saillants section IR3 », etc.

Tout rapport remis fait l'objet d'un **hash** (SHA-256) calculé sur le PDF / Word final. Le hash est consigné dans un journal interne. Cela permet de prouver, en cas de litige, que le rapport délivré au commanditaire est bien identique à celui archivé.

**Pratique.** Le hash peut être horodaté via OpenTimestamps (blockchain). Cela ajoute une preuve temporelle indépendante. Coût : nul.

## 88.4 Executive summary : l'art de la synthèse

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

## 88.5 Cadrage du mandat : pourquoi c'est crucial

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

## 88.6 Méthodologie : transparence

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

## 88.7 Analyse par IR

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

## 88.8 Synthèse intégrée

La **synthèse intégrée** apparaît après les IR. Elle propose une **vue 360°** :

- Timeline globale (résumé).
- Graphe d'enquête (vue d'ensemble).
- Convergences entre IR.
- Tableau ACH consolidé.
- Discussion des hypothèses alternatives.

C'est dans cette section que se construit la **narration analytique** : pas un story-telling, mais une mise en cohérence rigoureuse.

## 88.9 Recommandations

Les **recommandations** sont actionnables. Pas « il faudrait », mais « nous recommandons de ».

**Niveaux.**

- **Immédiat** : actions à conduire dans les 7 jours (préservation, alertes).
- **Court terme** : 1 mois (escalades).
- **Moyen terme** : 3 mois (approfondissements, expertise).
- **Suivi** : monitoring à mettre en place.

## 88.10 Limites globales

Cette section honnête est **valorisée** par les commanditaires sérieux. Elle décrit :

- Sources qui n'ont pas pu être consultées (par contrainte de temps, de droit, de budget).
- Hypothèses non testées.
- Marges d'erreur identifiées.
- Conditions sous lesquelles les conclusions pourraient être révisées.

## 88.11 Annexes

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

## 88.12 Tonalité et registre

**Sobre.** Pas de pathos. Pas d'adjectifs jugeants.

**Précis.** Chaque mot pèse.

**Calibré.** WEP discipliné, pas de surenchère.

**Neutre.** Pas de prise de parti.

**Confiant.** L'analyste assume ses conclusions, sans arrogance.

## 88.13 Lisibilité visuelle

**Mise en page soignée.**

- Numérotation cohérente des sections.
- Table des matières en début.
- Tableaux pour ce qui se tableaute.
- Schémas pour ce qui se visualise.
- Citations distinctement formatées.
- Captures d'écran lisibles, légendées, sourcées.

**Police et taille adaptées** au public (magistrat appréciera Arial / Times 11pt avec interligne 1.15).

## 88.14 Délivrabilité

**Formats.**

- **PDF/A** pour archivage long terme.
- **DOCX** si édition par le commanditaire est prévue.
- **Hash** systématique du fichier final.
- **Signature électronique** (eIDAS, AdES) pour valeur juridique.

## 88.15 Synthèse — discipline de production

Un rapport OSINT complet est un **artefact professionnel**. Sa qualité formelle est inséparable de sa qualité analytique. Soigné, calibré, documenté, il inspire confiance et résiste au contre-expertise.

-----
