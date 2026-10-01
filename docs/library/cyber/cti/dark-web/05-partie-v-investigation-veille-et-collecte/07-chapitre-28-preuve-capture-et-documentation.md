---
title: Chapitre 28 — Preuve, capture et documentation
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

La différence entre une observation intéressante et une preuve utilisable tient à la **documentation**. Ce chapitre couvre la préservation des preuves de manière admissible — pour rapport interne, pour coordination avec autorités, et le cas échéant pour usage judiciaire.

## 28.1 Les niveaux de documentation

**Niveau 1 — Documentation interne** : pour rapport à la cellule de crise, à la direction. Exigence : lisible, structuré, horodaté. Pas de formalisme judiciaire strict.

**Niveau 2 — Documentation pour autorités** : pour transmission à DGSI, ANSSI, CNIL. Exigence : chain of custody, horodatages fiables, hashes, traçabilité. Format standard (IOCs, STIX/TAXII si pertinent).

**Niveau 3 — Documentation admissible judiciairement** : pour usage dans procédure pénale. Exigence : chain of custody rigoureuse, capture forensically sound, témoin pour certaines captures, signature notariale ou équivalent pour éléments critiques. Un analyste privé produit rarement directement ce niveau ; il prépare les éléments pour que les forces de l'ordre puissent les reconstituer avec leur propre cadre.

**Niveau 4 — Documentation coopérative** : pour partage sectoriel (ISAC, pairs RSSI). TLP AMBER typiquement. Format structuré pour réutilisation par les pairs (indicators actionnables, sans données sensibles exposées).

## 28.2 La chain of custody

Principe : pour chaque élément de preuve, tracer **qui l'a collecté, quand, comment, et par qui il a été manipulé depuis**. Toute rupture dans la chaîne invalide potentiellement la preuve.

**Éléments à tracer pour chaque capture** :

- **Date et heure précise** (UTC recommandé, avec fuseau indiqué).
- **Analyste** qui a effectué la capture.
- **Source** : URL .onion, forum, thread ID, post ID.
- **Méthode** : capture d'écran, HTML source save, wget, screenshot d'une VM.
- **Hash cryptographique** du fichier capturé (SHA-256 minimum).
- **Emplacement de stockage** : chemin dans l'archive Athéna, sauvegarde sur stockage immutable.
- **Modifications** : aucune idéalement, ou documentées si nécessaires.

**Outils d'aide** :

- **Hunchly** : outil commercial qui automatise une grande partie de la chain of custody.
- **OSINT Cloner** : alternative open source, moins complète.
- **Custom scripts** : beaucoup d'équipes développent leurs propres scripts de capture structurée.

## 28.3 Types de preuves et méthodes de capture

**Pages web (HTML)**. Capture en deux formats :

- **Screenshot** : rendu visuel, incluant CSS et images. Utile pour le lecteur humain.
- **HTML source** : code source brut. Utile pour l'analyse technique et la reconstitution.

Outils : wget/curl (via torify), outils navigateur (save page as, print to PDF), Hunchly, Aquatone pour volumes.

**Threads de forums**. Capturer tous les posts d'un thread, même si longs et paginés. Hunchly ou scripts qui parcourent la pagination.

**Messages privés**. Dans une messagerie (XMPP, Telegram), exporter le log chiffré complet. Conserver les métadonnées (horodatages, clés de session, participants).

**Fichiers téléchargés**. Hash immédiat post-téléchargement. Pas de modification avant analyse en VM. Stockage du fichier original intact + copie de travail pour analyse.

**Adresses crypto et transactions**. Capture de l'adresse exacte (copier-coller, pas retranscrire). Capture de transactions via blockchain explorer avec screenshots. Exports via Chainalysis, TRM, etc. horodatés.

**Captures temporelles**. Un site peut changer entre 2 visites. Capture datée à chaque fois. Archive via service tiers (Internet Archive pour clearnet, mais difficile pour .onion — archives manuelles alors).

## 28.4 Le stockage des preuves

**Immutabilité**. Une fois capturées, les preuves ne doivent pas pouvoir être modifiées. Options :

- **Stockage WORM** (Write Once Read Many) : solutions enterprise (AWS S3 Object Lock, Azure immutable blobs, NAS avec WORM).
- **Blockchain timestamping** : horodatage sur blockchain publique (OpenTimestamps, Bitcoin via OP_RETURN) — prouve qu'un document existait à une date donnée.
- **Signature cryptographique** : GPG signature par l'analyste, horodatée.
- **Archive sur CD/DVD non réinscriptibles** (pratique moins moderne mais acceptée judiciairement).

**Confidentialité**. Les preuves stockées restent sensibles. Chiffrement au repos, contrôle d'accès granulaire, logs d'accès. Idéalement : accès nécessitant plusieurs personnes pour ouvrir (modèle multi-party).

**Rétention**. Politique documentée : combien de temps conserver ? La plupart des organisations retiennent 3-7 ans selon cadre réglementaire et risques. Destruction formalisée après fin de rétention.

**Localisation**. Stockage dans pays cohérent avec le cadre juridique (France pour les preuves servant enquêtes françaises, idéalement), éviter stockage dans juridictions où les preuves pourraient être saisies ou exposées.

## 28.5 La notarisation et l'horodatage qualifié

Pour les preuves à haute valeur, le **simple hash** ne suffit pas toujours. Techniques additionnelles :

**Horodatage qualifié**. En France et en UE, services d'horodatage qualifiés eIDAS. Un horodatage qualifié prouve juridiquement qu'un document existait à une date donnée. Plusieurs fournisseurs (Universign, Docapost, prestataires qualifiés).

**Constat d'huissier**. Un huissier de justice peut constater le contenu d'un site web à un instant T. Coûteux (plusieurs centaines à milliers d'euros par constat) mais haute valeur probante en procédure judiciaire française.

**APCTA** (Authentification de Preuve Constatée par un Tiers Attentif) — services privés qui fournissent une forme d'attestation horodatée, moins formelle qu'un huissier mais plus accessible.

Pour une investigation CTI courante, horodatage + hash + chain of custody documentée suffit. Les procédures judiciaires plus lourdes (constat d'huissier) sont réservées aux cas où la preuve sera utilisée en contentieux.

## 28.6 Les indicators of compromise (IoC)

Au-delà de la documentation narrative, l'investigation produit des **indicators of compromise** — artefacts techniques réutilisables.

**Types d'IoC** :

- **Hashes de fichiers** (MD5, SHA-1, SHA-256 — le dernier préféré).
- **URLs / domaines** malveillants.
- **Adresses IP** C2, infrastructure.
- **Adresses crypto** utilisées par acteurs criminels.
- **Emails** utilisés dans phishing / scams.
- **Pseudonymes** de forum.
- **PGP fingerprints**.
- **YARA rules** : règles de pattern-matching pour détecter malwares.
- **Sigma rules** : règles de détection pour SIEM.
- **STIX objects** : format structuré pour interchange de TI.

**Format de partage** :

- **STIX/TAXII** : standard OASIS pour cyber threat intelligence, format structuré pour interchange machine-to-machine.
- **MISP** : plateforme communautaire de partage, format riche, TLP natif.
- **Feeds CSV / JSON** : formats simples pour intégration SIEM.
- **Emails structurés** pour partage ad hoc entre équipes.

**Coordination**. Les IoC sont partagés selon TLP :

- **TLP RED** : strictement entre équipes désignées.
- **TLP AMBER** : partage avec partenaires de confiance (ISAC, RSSI sectoriel).
- **TLP GREEN** : partage avec communauté élargie (CERT communautaire).
- **TLP CLEAR** : public.

## 28.7 La communication des résultats

Au-delà de la production des preuves, **communiquer les résultats** est une compétence à part entière.

**À la cellule de crise interne** :

- **Sommaire exécutif** : 1 page max, conclusions et recommandations.
- **Dossier technique** : détails pour l'équipe IR.
- **Capture préservée** : preuves accessibles en cas de besoin ultérieur.

**Aux autorités** :

- **Format standard** requis par l'autorité (DGSI a ses canaux, ANSSI a ses templates).
- **Anonymisation éventuelle** : parfois, certaines informations ne peuvent être transmises (sources, méthodes d'obtention).
- **Chain of custody maintenue**.

**Aux pairs sectoriels (ISAC)** :

- **Indicators anonymisés** : victim stripped, IoC techniques conservés.
- **Tactics observées** : utile pour détection chez les pairs.
- **TLP AMBER** typiquement.

**Publiquement (rare)** :

- **Rapports éditoriaux** : pour sensibilisation. Un cabinet CTI peut publier son investigation après anonymisation de la victime (si elle consent) ou généralisation.
- **Advisories** publiques : pour alerter la communauté sur des menaces spécifiques.

**Erreurs de communication à éviter** :

- **Sur-confidence** : présenter une hypothèse comme certitude. Calibrer.
- **Jargon excessif** : audience non-technique se perd. Ajuster le niveau.
- **Conclusions trop techniques** : ne pas traduire en action business.
- **Rigidité** : le rapport est un instantané, pas une vérité éternelle. Indiquer révisabilité.

## 28.8 Fil rouge — DARKSTREAM : la documentation finale

> **🌐 DARKSTREAM — Épisode 16 : la pochette de preuves**
>
> Après 6 semaines d'investigation, Lucas finalise la **pochette de preuves** de DARKSTREAM pour remise à Vectris et DGSI.
>
> **Contenu de la pochette** :
>
> 1. **Rapport principal** (42 pages, signature PGP de Lucas) — narration complète, analyse, recommandations.
> 2. **Annexe A : captures IndustrialLeaks** — 147 screenshots + HTML sources de tous les posts pertinents, chaque fichier horodaté et haché SHA-256. Index XLSX avec correspondance screenshots/horodatages.
> 3. **Annexe B : conversations XMPP avec aero_source** — export complet chiffré, hashé, horodaté. 18 échanges sur 4 semaines.
> 4. **Annexe C : échantillons reçus** — les 8 fichiers reçus, en archives chiffrées, avec hashes et analyses.
> 5. **Annexe D : analyse blockchain** — exports Chainalysis du cluster aero_source, graphes de relations, IoC (adresses crypto).
> 6. **Annexe E : logs Russian Market** — les 12 stealer logs Vectris identifiés, métadonnées et extraits pertinents.
> 7. **Annexe F : IoC structurés** — format MISP, prêt pour partage sectoriel après anonymisation.
> 8. **Annexe G : chain of custody** — liste chronologique de toutes les actions d'investigation, signées par Lucas avec horodatage qualifié.
> 9. **Annexe H : note méthodologique** — sources, outils, limites, biais.
>
> La pochette totale représente ~1,2 Go de données. Stockée sur share chiffré Athéna, accès contrôlé. Versions papier signées du rapport principal.
>
> Transmission : TLP:RED à Vectris (cellule de crise + RSSI), TLP:AMBER à la DGSI. La DGSI a indiqué qu'elle transmettra les éléments pertinents à ses partenaires internationaux (notamment si identifications complémentaires d'aero_source émergent via d'autres services).
>
> La solidité de cette pochette conditionne la solidité des actions défensives et coercitives qui en découleront. Si un jour aero_source est identifié physiquement et interpellé, les preuves collectées par Lucas pourront être remontées dans le dossier d'accusation. Si les données Vectris apparaissent ailleurs ultérieurement, la pochette fournira le baseline pour distinguer leak originel et recirculation.

---
