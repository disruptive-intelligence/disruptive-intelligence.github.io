---
title: ANNEXE G — Modèle de journal d'investigation
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 15
chapters: 15
---

Le **journal d'investigation** est la mémoire écrite et structurée de l'enquête. Tout est inscrit, daté, sourcé, coté. Modèle de référence pour usage en vault Obsidian / fichier Markdown local chiffré.

#### G.1 — Structure du journal

**Niveau 1 — Index du dossier.**
- Page d'index avec liens vers tous les éléments du dossier.

**Niveau 2 — Sections principales.**
- 0-mandat.md : Mandat reçu et cadrage.
- 1-methodologie.md : Méthodologie spécifique adoptée.
- 2-fiches/ : Dossier contenant les fiches entités.
- 3-journal/ : Dossier contenant les entrées chronologiques.
- 4-pieces/ : Dossier contenant les pièces archivées avec hashes.
- 5-analyse/ : Dossier contenant ACH, matrices, hypothèses.
- 6-livrables/ : Dossier contenant les versions du rapport.

#### G.2 — Entrée type de journal

Chaque entrée de journal contient :

```markdown
# Entrée [YYYY-MM-DD-HHmm] [Action]

## Contexte
[Pourquoi cette entrée, dans quel cadre]

## Action conduite
[Quoi exactement : recherche, capture, vérification]

## Sources consultées
- [URL 1] — [date d'accès] — [hash si applicable]
- [URL 2] — ...

## Résultats
[Ce qui a été trouvé]

## Cotation préliminaire
- Source : [A-F]
- Information : [1-6]

## Pivots possibles identifiés
- [Pivot 1]
- [Pivot 2]

## Limites / questions ouvertes
[Ce qui reste à investiguer]

## Liens dossier
- Fiches mises à jour : [[Fiche P-001]]
- Pièces archivées : pieces/[ref]

## Notes méthodologiques
[Bonnes pratiques, leçons, biais détectés]

---
Hash de cette entrée (post-rédaction) : [SHA-256]
```

#### G.3 — Exemple d'entrée de journal MIRAGE

```markdown
# Entrée 2026-05-17-1430 — Investigation Delta Consulting (Malte)

## Contexte
Investigation MIRAGE/IR1 (structures offshore Delaunay). Approfondissement
de la fiche entité Delta Consulting Ltd identifiée en MIRAGE 8.

## Action conduite
1. Consultation Companies Registry Malta directement.
2. Recherche cross-juridictions via OpenCorporates.
3. Vérification adresse domiciliation (Athinon Street, Valletta).

## Sources consultées
- https://registry.mfsa.com.mt/ (capture Hunchly 2026-05-17 14:32)
  Hash : 7a3f2b8c...
- https://opencorporates.com/companies/mt/[id] (capture Hunchly 2026-05-17 14:38)
  Hash : 9e1d4f5a...
- Cross-search adresse : 47 sociétés à la même adresse de domiciliation
  identifiées (typique registered agent).

## Résultats
- Delta Consulting Ltd, immatriculée 03/2020.
- Capital 1200 €.
- Director unique : Marc Delaunay.
- Activité déclarée : "consulting services".
- Adresse : 24 Athinon Street, Valletta (registered agent commun).
- UBO déclaré : Marc Delaunay 100 %.

## Cotation préliminaire
- Source (Companies Registry Malta) : A1 — registre officiel
- Information : 1 — confirmée par capture officielle

## Pivots possibles identifiés
- Cross-recherche adresse domiciliation : 47 autres sociétés.
- 12 d'entre elles ont directors avec prénoms français — cluster
  potentiel à explorer.
- Investigation Cyprus Confidential pour mention Delta.

## Limites / questions ouvertes
- Capital social symbolique (1200 €) : cohérent avec usage offshore mais
  pas démonstration de fonction.
- Comptes Delta non publiés sur Malta (pas obligation pour micro-entité).
- Activité réelle non observable directement.

## Liens dossier
- Fiches mises à jour : [[Fiche E-002 Delta Consulting]]
- Pièces archivées : pieces/mirage-014-companies-registry-malta.pdf, ...

## Notes méthodologiques
- Bonne intuition de cross-rechercher l'adresse de domiciliation : ouvre
  un cluster non anticipé.
- Cotation prudente : présence administrateur ≠ démonstration bénéfice
  économique direct.

---
Hash de cette entrée : 4b8c3e2a91d5f6c7...
```

#### G.4 — Bonnes pratiques

**Rédiger en temps réel.** Pas le soir, pas le lendemain. L'erreur de mémoire est aussi grave que l'erreur d'analyse.

**Niveau de détail.** Suffisant pour qu'un confrère puisse reproduire la démarche, sans tomber dans la verbosité.

**Citation des sources.** URL + capture archive + hash systématique pour chaque source significative.

**Cotation préliminaire.** Pas attendre la synthèse. Coter au fil de l'eau, ajustable.

**Pivots identifiés.** Lister explicitement, même si on n'a pas le temps de tous les explorer. Évite l'oubli.

**Notes méthodologiques.** Ce qui marche, ce qui ne marche pas. Capitalisation.

#### G.5 — Versioning et intégrité

**Vault Obsidian + Git local.**

```
mirage-investigation/
├── .git/
├── 0-mandat.md
├── 1-methodologie.md
├── 2-fiches/
│   ├── P-001-marc-delaunay.md
│   ├── E-001-technovert.md
│   └── ...
├── 3-journal/
│   ├── 2026-05-16-cadrage.md
│   ├── 2026-05-17-delta-consulting.md
│   └── ...
├── 4-pieces/
│   ├── pieces.json (catalogue avec hashes)
│   └── archived/
└── 6-livrables/
    ├── rapport-v0.1.md
    └── rapport-v1.0-final.pdf
```

**Commits Git réguliers.** À chaque session d'enquête.

**Backups chiffrés.** Quotidiens. 3-2-1.

#### G.6 — Confidentialité

**Chiffrement.** Disque VeraCrypt (recommandé container 50-200 Go selon enquête).

**Mot de passe.** Phrase de passe robuste, gestionnaire de mots de passe local (KeePassXC).

**Accès.** Strictement limité à l'analyste / cabinet.

**Pas de cloud sync.** Disable Dropbox, OneDrive, iCloud sur ce répertoire.

#### G.7 — Catalogue des pièces

Un fichier dédié `pieces.json` (ou table dans Obsidian) catalogue **chaque pièce** :

```json
{
  "ref": "mirage-014",
  "title": "Companies Registry Malta - Delta Consulting Ltd",
  "type": "capture_hunchly",
  "date_collected": "2026-05-17T14:32:00+02:00",
  "source_url": "https://registry.mfsa.com.mt/[...]",
  "hash_sha256": "7a3f2b8c...",
  "filepath": "4-pieces/archived/mirage-014.html",
  "captured_by": "AnalysteX",
  "tool": "Hunchly v3.2",
  "cotation_source": "A",
  "cotation_information": "1",
  "tags": ["delta-consulting", "malte", "registre-officiel"],
  "notes": "Capture intégrale page registre. Pages 1-3 utiles."
}
```

#### G.8 — Synthèse — discipline de journal

Le journal d'investigation est ce qui distingue **l'analyste mature** de l'amateur. Il transforme une recherche éparpillée en dossier défendable. C'est aussi ce qui rend le travail **reproductible**, **auditable**, **capitalisable**.

Sans journal, l'enquête meurt avec son auteur. Avec journal, elle survit, se transmet, s'améliore.

-----


### ANNEXE H — Templates de fiches

Templates standards pour les principaux types de fiches mobilisés dans une enquête OSINT mature. À adapter selon contexte.

#### H.1 — Template fiche personne physique

```markdown
# FICHE PERSONNE — [Nom Prénom]

**Identifiant interne :** [MIRAGE/P-XXX]
**Statut :** [en cours / clos]
**Dernière mise à jour :** [YYYY-MM-DD]
**Cotation globale :** [niveau de confiance d'identification]
**Tags :** [#personne #IR1 #...]

## Sélecteurs forts vérifiés
- Nom complet : [...]
- Date de naissance : [date / "déduit, à confirmer"]
- Email perso : [...] (cotation)
- Téléphone : [...] (cotation)
- Identifiants officiels : [SIREN dirigeant, etc.]

## Identité civile
- Citoyenneté : [...]
- État civil : [...]
- Adresse résidentielle : [...] (cotation)
- Famille proche : [conjoint, enfants — avec déontologie]

## Parcours professionnel
- [Année] : [poste/société] — [source, cotation]
- ...

## Identités numériques
- LinkedIn : [URL] (cotation)
- Twitter/X : [@username]
- Instagram : [@username]
- Autres : [...]

## Patrimoine visible (avec déontologie)
- Immobilier : [...] (sources cotées)
- Sociétés détenues : [liens fiches société]
- Mobilier de luxe : [...] (si visible publiquement)

## Indicateurs de risque
- Sanctions : [aucune / liste]
- PEP : [non / oui : ...]
- Adverse media : [aucun / synthèse]
- Liens offshore : [aucun / [liens fiches société]]

## Réseau professionnel et personnel
- Cabinet conseil : [...]
- Réseau LinkedIn : [degré]
- Contacts identifiés : [liens]

## Liens vers autres fiches
- Société : [[Fiche E-XXX]]
- Domaine : [[Fiche D-XXX]]
- Compte : [[Fiche C-XXX]]

## Notes d'enquête
- [Observations, hypothèses, pistes]

## Sources principales (avec captures)
- [Source 1] — [date capture, hash]
- ...

## Historique des mises à jour
- [YYYY-MM-DD] : création.
- [YYYY-MM-DD] : ajout patrimoine.
- ...
```

#### H.2 — Template fiche société

```markdown
# FICHE SOCIÉTÉ — [Raison Sociale]

**Identifiant interne :** [MIRAGE/E-XXX]
**Statut :** [en cours / clos]
**Dernière mise à jour :** [YYYY-MM-DD]
**Cotation globale :** [niveau d'identification]
**Tags :** [#société #offshore #IR1]

## Identité légale
- Raison sociale : [...]
- Forme juridique : [SARL / SAS / Ltd / GmbH / autre]
- Numéro d'enregistrement : [SIREN / CRO number / etc.]
- Juridiction : [pays]
- Adresse de siège : [...]
- Date de création : [...]
- Capital social : [...]
- Activité (code) : [NAF / NACE / NAICS]

## Gouvernance
- Président / DG : [...]
- Autres dirigeants : [...]
- Conseil d'administration : [...]
- Commissaires aux comptes : [...]
- Procurations : [...]

## Actionnariat et UBO
- Structure : [...]
- UBO déclaré : [...] (source, cotation)
- Actionnaires identifiés : [...]

## Activité
- Activité déclarée : [...]
- Activité observable : [...]
- Marchés / clients principaux : [...]

## Indicateurs financiers (publiquement disponibles)
- CA dernier exercice : [...]
- Résultat : [...]
- Dette : [...]
- Évolution sur 3-5 ans : [...]

## Sociétés liées
- Société mère : [...]
- Filiales : [...]
- Sociétés liées via dirigeants partagés : [...]

## Indicateurs de risque
- Sanctions : [...]
- Adverse media : [...]
- Contentieux : [...]
- Juridiction à risque : [oui/non, justification]

## Infrastructure web
- Domaine principal : [...]
- Sous-domaines significatifs : [...]
- Technologies : [...]

## Sources principales (avec captures)
- [Source 1]
- ...

## Liens vers autres fiches
- Dirigeants : [[Fiche P-XXX]]
- Domaine : [[Fiche D-XXX]]
- Filiales : [...]

## Notes d'enquête
- [Observations, hypothèses, pistes]
```

#### H.3 — Template fiche compte (réseau social)

```markdown
# FICHE COMPTE — [@username sur Plateforme]

**Identifiant interne :** [MIRAGE/C-XXX]
**Statut :** [en cours / clos]
**Plateforme :** [X / LinkedIn / Telegram / Instagram / autre]
**Dernière mise à jour :** [YYYY-MM-DD]
**Cotation :** [identification / authenticité]

## Identification compte
- Username : [@...]
- URL du profil : [...]
- ID interne (si disponible) : [...]
- Date de création : [...]

## Profil affiché
- Photo de profil : [analyse — IA, recyclée, etc.] (cotation)
- Bio : [...]
- Localisation déclarée : [...]
- Site web déclaré : [...]

## Activité
- Volume posts : [N total, X par jour moyen]
- Cadence : [horaires actifs, heatmap]
- Sujets dominants : [...]
- Ton : [...]
- Langues : [...]

## Réseau social
- Followers : [N]
- Following : [N]
- Comptes notables suivis / suivants : [liste]
- Cluster identifié : [si applicable]

## Authenticité
- Signaux d'inauthenticité : [Hive Moderation IA score, etc.]
- Comparaison à patterns CIB : [...]
- Cotation authenticité : [...]

## Liens vers autres fiches
- Personne probable derrière : [[Fiche P-XXX]]
- Société associée : [...]
- Autres comptes liés : [[Fiche C-XXX]]

## Captures et préservation
- Captures Hunchly horodatées : [...]
- Hashes : [...]

## Notes d'enquête
- [Observations, hypothèses]
```

#### H.4 — Template fiche domaine / infrastructure

```markdown
# FICHE DOMAINE — [domain.tld]

**Identifiant interne :** [MIRAGE/D-XXX]
**Statut :** [en cours / clos]
**Dernière mise à jour :** [YYYY-MM-DD]
**Cotation :** [niveau de confiance]

## Domaine principal
- Nom : [...]
- Date de création : [WHOIS historique si disponible]
- Registrar : [...]
- Statut actuel : [actif / inactif]

## WHOIS
- WHOIS actuel : [REDACTED RGPD / détails]
- WHOIS historique : [si pre-2018, détails]

## DNS records
- A : [IPs]
- MX : [serveurs mail]
- NS : [nameservers]
- TXT : [vérifications domaines tiers, SPF, DKIM]
- SOA : [...]

## Sous-domaines identifiés
- [sous-domaine 1] : [IP] [usage]
- ...

## Certificats TLS
- Émetteurs : [Let's Encrypt, etc.]
- SAN : [...] (sous-domaines révélés)
- crt.sh : [URL recherche]

## Infrastructure
- IPs : [...]
- ASN : [...]
- Hébergement : [...]
- CDN : [...]
- Country : [...]

## Technologies
- Wappalyzer : [stack identifié]
- BuiltWith : [profil étendu]

## Trackers / analytics
- Google Analytics Property : [ID]
- Facebook Pixel : [ID]
- Autres : [...]

## Liens vers autres fiches
- Société associée : [[Fiche E-XXX]]
- Personne associée : [[Fiche P-XXX]]
- Autres domaines liés (mêmes trackers, etc.) : [[Fiche D-XXX]]

## Captures et historique
- Wayback snapshots : [URL]
- archive.today : [URL]
- Hunchly : [...]
```

#### H.5 — Template fiche contenu (image / vidéo / document)

```markdown
# FICHE CONTENU — [titre / description]

**Identifiant interne :** [MIRAGE/T-XXX]
**Type :** [image / vidéo / audio / document]
**Statut :** [en cours / clos]
**Dernière mise à jour :** [YYYY-MM-DD]
**Cotation authenticité :** [...]
**Cotation pertinence :** [...]

## Identification
- URL source : [...]
- Date de découverte : [...]
- Date supposée de production : [...]
- Format : [JPG / MP4 / PDF / etc.]
- Taille : [...]
- Hash SHA-256 : [...]

## Métadonnées
- EXIF : [...]
- C2PA : [présent / absent, détails]
- Autres : [IPTC, XMP, etc.]

## Authenticité technique
- Détection IA (multi-outils) : [Hive, Optic, Sensity scores]
- ELA : [analyse]
- Signaux visuels : [...]
- Cotation : [...]

## Recherche inversée
- Yandex : [résultats]
- Google Lens : [résultats]
- TinEye : [première occurrence]
- Conclusion provenance : [...]

## Géolocalisation et chronolocation (si applicable)
- Lieu identifié : [coordonnées GPS]
- Date / heure : [...]
- Méthode : [shadow analysis, indices visuels]

## Authenticité contextuelle
- Cohérence avec récit présenté : [...]
- Comparaison avec autres sources : [...]

## Liens vers autres fiches
- Personne représentée : [[Fiche P-XXX]]
- Événement associé : [[Fiche EV-XXX]]
- Lieu : [[Fiche L-XXX]]

## Préservation
- Fichier archivé : [chemin local chiffré]
- Hash : [SHA-256]
- Horodatage qualifié : [OpenTimestamps, eIDAS]
```

#### H.6 — Template fiche événement

```markdown
# FICHE ÉVÉNEMENT — [description courte]

**Identifiant interne :** [MIRAGE/EV-XXX]
**Date :** [YYYY-MM-DD avec précision]
**Lieu :** [si applicable, coordonnées]
**Cotation :** [...]

## Description
[Description factuelle de l'événement]

## Acteurs
- Acteur 1 : [[Fiche P-XXX]] — [rôle]
- Acteur 2 : [...]

## Contexte
[Contexte plus large nécessaire à la compréhension]

## Sources
- [Source 1] — [date, cotation]
- ...

## Liens vers autres fiches
- Personnes : [...]
- Lieux : [...]
- Contenus associés : [...]

## Notes d'enquête
[Observations, importance pour IR concernées]
```

#### H.7 — Template fiche lieu

```markdown
# FICHE LIEU — [adresse / coordonnées]

**Identifiant interne :** [MIRAGE/L-XXX]
**Coordonnées GPS :** [...]
**Adresse :** [...]
**Cotation :** [identification]

## Description
- Type : [résidence / bureau / industriel / autre]
- Description : [...]

## Propriété
- Propriétaire (si connu) : [...]
- SCI / société : [[Fiche E-XXX]]
- Cadastre : [référence]

## Géolocalisation et confirmation
- Sources : [Google Maps, OSM, photos cible]
- Cross-vérification : [...]

## Photos
- Photos archivées : [...]
- Captures Street View / Mapillary : [...]

## Liens vers autres fiches
- Personne associée : [[Fiche P-XXX]]
- Société associée : [[Fiche E-XXX]]
- Événements liés : [...]

## Notes d'enquête
[Observations]
```

#### H.8 — Discipline de templates

**Constance.** Une fois adopté, le template est utilisé pour TOUTES les fiches de ce type. Cohérence permet exploitation systématique.

**Évolutions.** Si le template évolue, versionner. Mise à jour rétroactive si pertinent.

**Adaptation au contexte.** Templates ci-dessus sont génériques. Pour cas spécifiques (CTI, crypto, sanctions), créer templates dérivés.

**Outillage.** Vault Obsidian + plugin Templater permet d'instantier rapidement nouvelle fiche depuis template.

> **Principe.** Une fiche bien structurée est un actif. Mal structurée, c'est du bruit. La discipline de templates fait la différence entre un dossier exploitable et un capharnaüm.

-----


### ANNEXE I — Matrice piste / indice / fait / preuve

Cette annexe formalise la **gradation** des éléments collectés dans une enquête OSINT, depuis l'orientation la plus vague jusqu'à la preuve à valeur judiciaire potentielle. Elle complète Ch.4 (épistémologie) et Ch.84 (Admiralty).

#### I.1 — Quatre niveaux

**Piste.** Élément vague d'orientation, indication non encore confirmée par sources fiables. Ne soutient pas une conclusion. Sert à orienter la recherche.

*Exemple.* « Une rumeur sur X cybercriminel suggère que Delaunay aurait un compte ProtonMail. »

**Indice.** Élément factuel partiel, corroboré faiblement, qui pointe vers une conclusion sans la soutenir seul. Plusieurs indices convergents forment un faisceau.

*Exemple.* « Le stealer log Hudson Rock mentionne marc.delaunay76@gmail.com avec accès Binance. »

**Fait.** Élément confirmé par source fiable (cotation Admiralty A ou B avec confiance 1 ou 2), avec preuve documentaire archivée et hashée. Soutient une conclusion calibrée.

*Exemple.* « Marc Delaunay est administrateur unique de Delta Consulting Ltd selon le Companies Registry Malta (capture Hunchly horodatée, hash SHA-256). »

**Preuve.** Fait qui satisfait également aux exigences d'usage judiciaire : chain of custody, horodatage qualifié, signature électronique, conservation forensique, accessibilité au magistrat. Peut être ré-examinée par expertise judiciaire.

*Exemple.* « Document archivé sous référence MIRAGE/P-014, signé électroniquement PAdES-LT, horodatage eIDAS qualifié, hash SHA-256 publié, intégrité vérifiée 2 fois entre collecte et présentation. »

#### I.2 — Tableau de gradation

| Niveau | Source typique | Cotation min Admiralty | Cotation min WEP | Usage |
|---|---|---|---|---|
| Piste | Rumeur, forum, leak non-vérifié | C-F / 3-6 | Possible | Orientation |
| Indice | Source secondaire, faisceau partiel | B-C / 2-3 | Possible / Probable | Soutien partiel |
| Fait | Source primaire ou multi-corroboré | A-B / 1-2 | Probable / Très probable | Conclusion documentée |
| Preuve | Fait + chain custody | A1 + standards judiciaires | Quasi-certain | Usage judiciaire |

#### I.3 — Implications méthodologiques

**Discipline.** Chaque élément du dossier est **classé** à l'un de ces quatre niveaux. Le rapport mentionne le niveau.

**Pas d'auto-promotion.** Une piste ne devient pas un indice par accumulation. Une accumulation de pistes reste pistes. Pour passer indice → fait, il faut **corroboration par source distincte et fiable**.

**Honnêteté.** Ne pas présenter une piste comme fait. Ne pas présenter un fait comme preuve si la chain of custody n'a pas été appliquée.

**Vocabulaire du rapport.**
- Pour piste : « Une piste suggère que... à confirmer. »
- Pour indice : « Plusieurs indices convergent vers... »
- Pour fait : « Il est établi par sources convergentes que... » ou « Sources documentées attestent... »
- Pour preuve : « Élément documenté en pièce annexée [ref], chain of custody validée. »

#### I.4 — Évolution d'un élément

Un élément peut **évoluer** dans la gradation au fil de l'enquête :

**Exemple MIRAGE.**

**Jour 1 (piste).** « Rumeur sur forum X : un cadre TechnoVert aurait des structures offshore. »

**Jour 5 (indice).** « Un cadre nommé Delaunay est mentionné en relation avec une société à Malte (mention pressereg régionale anonyme). »

**Jour 10 (fait).** « Marc Delaunay est administrateur de Delta Consulting Ltd Malte (Companies Registry Malta + OpenCorporates, A1). »

**Jour 20 (preuve, après workflow judiciaire).** « Pièce MIRAGE/E-002, capture Hunchly archive HTML intégrale, hash SHA-256 [X], horodatage eIDAS qualifié [Y], signature PAdES-LT. »

#### I.5 — Cas particulier — stealer logs et leaks

**Stealer logs / leaks ICIJ** : statut **indice** par défaut, car la chain of custody amont est compromise (origine criminelle / journalistique). Ne peut typiquement pas accéder à statut « preuve judiciaire » sans validation par expertise indépendante ou réquisition.

**Implication.** Citation pour orientation, pas pour conclusion. Expertise complémentaire requise pour usage judiciaire.

#### I.6 — Cas particulier — contenus IA

**Contenus IA-generated** (deepfake, fausses photos, voice cloning) : leur authenticité a été niée — c'est un **fait technique** (B2 typiquement, multi-outils convergents).

Mais leur attribution au commanditaire est typiquement **indice** (cohérence motivationnelle, temporelle, sans lien démonstrable en source ouverte).

#### I.7 — Synthèse

Cette matrice donne le **vocabulaire et la discipline** pour parler de la qualité épistémologique des éléments. Elle est l'un des piliers de la cotation rigoureuse.

> **Principe.** Confondre piste et fait est l'erreur la plus fréquente des analystes débutants. Une piste publiée comme fait est une erreur grave. Un fait minoré en piste est une timidité méthodologique. La calibration s'apprend.

-----


### ANNEXE J — Cotation Admiralty et niveaux de confiance WEP (synthèse rapide)

Annexe de référence rapide pour la cotation. Détails en Ch.84 et Ch.85.

#### J.1 — Cotation Admiralty (synthèse)

**Fiabilité de la source (lettre).**

| Lettre | Niveau | Description |
|---|---|---|
| A | Complètement fiable | Source dont la fiabilité est démontrée sans réserve |
| B | Habituellement fiable | Source avec historique de fiabilité élevé |
| C | Plutôt fiable | Source généralement fiable avec quelques erreurs |
| D | Plutôt non fiable | Source avec historique mixte |
| E | Non fiable | Source historiquement peu fiable |
| F | Non évaluable | Source sans historique |

**Crédibilité de l'information (chiffre).**

| Chiffre | Niveau | Description |
|---|---|---|
| 1 | Confirmée | Multiples sources indépendantes fiables |
| 2 | Probablement vraie | Cohérente, plausible |
| 3 | Possiblement vraie | Pas contredite, peu corroborée |
| 4 | Doute | Cohérence faible |
| 5 | Improbable | Contradictions |
| 6 | Non évaluable | Manque d'information |

**Combinaisons types.**
- **A1** : Source officielle confirmée par multiples sources (« meilleure » cotation usuelle).
- **A2** : Source officielle / établie, information très probable.
- **B2** : Source habituellement fiable, information probable.
- **C3** : Source plutôt fiable, information possible (incertitude documentée).
- **F6** : « Information non évaluable », souvent associée à rumeur ou source inconnue.

#### J.2 — Niveaux de confiance WEP (synthèse)

**Échelle.**

| Expression | Probabilité approximative |
|---|---|
| Quasi-certain (almost certainly) | >95 % |
| Très probable (very likely) | 80-95 % |
| Probable (likely) | 55-80 % |
| Possible (about even chance) | 45-55 % |
| Peu probable (unlikely) | 20-45 % |
| Très peu probable (very unlikely) | 5-20 % |
| Hautement improbable (almost no chance) | <5 % |
| Indéterminable | Insuffisance d'évidence |

**Usage.**
- WEP s'applique aux **conclusions**, pas aux faits individuels.
- Faits → Admiralty.
- Conclusions analytiques → WEP.

**Exemple combiné MIRAGE.**

> « Faits : Delaunay est administrateur de Delta Consulting (A1). Delaunay est UBO de Verde Holdings (A1). Cyprus Confidential mémo documente flux Delta → Verde (B2). Conclusion : il est probable que Delaunay opère un dispositif de structures offshore. »

Les faits sont en A1/B2 ; la conclusion est « probable » (probabilité estimée 55-80 %).

#### J.3 — Pièges fréquents

**Confondre cotation fait et cotation conclusion.** Un fait A1 ne donne pas une conclusion « quasi-certaine » automatiquement. Il faut **plusieurs faits convergents et indépendants** pour atteindre quasi-certitude.

**Cotation par défaut.** Coter F6 par défaut quand on ne sait pas. Ne pas inventer.

**Sur-cotation.** Tentation de coter A1 ce qui est en réalité B2. Garder discipline.

**Sous-cotation.** Par excès de prudence, sous-coter. Le vocabulaire calibré WEP doit refléter la réalité de l'évidence, ni plus ni moins.

#### J.4 — Cotation et publication

**Dans le rapport.**

| Forme à utiliser | Sens |
|---|---|
| « Fait : ... (A1) » | Fait coté |
| « Niveau de confiance : probable » | Conclusion WEP |
| « Faisceau d'indices (B2, B2, C3) convergeant vers... » | Faisceau coté |
| « Il est probable que... (probable, niveau de confiance) » | Conclusion explicite |

#### J.5 — Tableau de référence rapide

| Situation | Cotation typique |
|---|---|
| Registre officiel français | A1 |
| Communiqué officiel d'entreprise | A1 |
| Article presse établie (Le Monde, FT, etc.) | B1-B2 |
| Blog d'expert reconnu | C2-C3 |
| Tweet d'un journaliste réputé | B2-B3 |
| Tweet d'un compte anonyme | D3-D4 |
| Leak ICIJ vérifié | B2 |
| Stealer log | C3 |
| Rumeur de forum | E5 |
| Détection IA Hive 78 % | B2 sur le score |
| LLM cloud sans vérification | F6 (jamais cotable) |

#### J.6 — Discipline finale

> **Règle d'or.** Chaque fait coté Admiralty. Chaque conclusion WEP. Pas d'exception. Pas de surenchère. Pas de timidité.

-----


### ANNEXE K — Workflow OSINT en 10 étapes

Workflow synthétique en 10 étapes pour conduire une enquête OSINT. Référence rapide pour aide-mémoire.

#### K.1 — Étape 1 : Cadrage

**Action.** Définir mandat, périmètre, IR, bornes, OPSEC, livrables, durée.

**Livrable.** Statement of Request (SOR) écrit et validé.

**Référence cours.** Ch.12.

#### K.2 — Étape 2 : Cartographie des sources

**Action.** Identifier les sources prioritaires par IR. Vérifier accès, droits, coûts.

**Livrable.** Tableau sources × IR.

**Référence cours.** Ch.13.

#### K.3 — Étape 3 : Préparation OPSEC

**Action.** Configurer environnement d'investigation (VPN, navigateurs, comptes, captures, chiffrement). Vérifier maturité avatars.

**Livrable.** Checklist OPSEC validée (Annexe F).

**Référence cours.** Ch.10, Ch.11.

#### K.4 — Étape 4 : Collecte structurée

**Action.** Investigation systématique IR par IR. Captures, journal d'investigation rigoureux. Hashes systématiques.

**Livrable.** Journal d'enquête avec entrées datées et pièces archivées.

**Référence cours.** Ch.14, Ch.15.

#### K.5 — Étape 5 : Vérification et cotation

**Action.** Pour chaque élément, vérification source primaire (Retrieve-Store-Cite si LLM), cotation Admiralty.

**Livrable.** Catalogue de pièces avec cotations.

**Référence cours.** Ch.57, Ch.84.

#### K.6 — Étape 6 : Structuration

**Action.** Construction de fiches entités, timeline, graphe d'enquête. Entity resolution.

**Livrable.** Fiches entités, graphe Maltego / Obsidian, timeline.

**Référence cours.** Ch.66, Ch.82, Ch.83.

#### K.7 — Étape 7 : Analyse structurée

**Action.** ACH sur IR principales. Devil's advocate. Anti-biais. Identification convergences et incohérences.

**Livrable.** Matrices ACH, synthèse analytique.

**Référence cours.** Ch.79, Ch.80, Ch.81.

#### K.8 — Étape 8 : Cotation finale et formulation

**Action.** Pour chaque conclusion, niveau de confiance WEP. Formulation calibrée.

**Livrable.** Brouillon de conclusions calibrées.

**Référence cours.** Ch.85, Ch.86.

#### K.9 — Étape 9 : Production du livrable

**Action.** Rédaction rapport selon format (note courte, rapport complet, judiciaire). BLUF, structure, annexes. Hashage, signature électronique, horodatage.

**Livrable.** Rapport final + annexes.

**Référence cours.** Ch.87, Ch.88, Ch.90.

#### K.10 — Étape 10 : Diffusion et clôture

**Action.** Diffusion sécurisée (TLP, chiffrement, watermark). Confirmation réception. Archivage chiffré. Veille post-rapport si applicable. Debriefing méthodologique. Purge programmée.

**Livrable.** Rapport diffusé, archivé. Carnet méthodologique mis à jour.

**Référence cours.** Ch.91, Ch.92.

#### K.11 — Boucles et itérations

Ce workflow est **idéalisé**. En pratique :
- Les étapes 4-7 sont **itératives** : la collecte alimente l'analyse qui alimente de nouvelles collectes.
- Les pivots inattendus peuvent réorienter (avec ajustement formel si nécessaire).
- La gestion des changements de cadrage doit être documentée explicitement.

#### K.12 — Adaptation au contexte

**Note courte d'1 heure.** Étapes 1, 4, 5, 8, 9 réduites au minimum. Pas de graphe ni d'ACH formel.

**Enquête rapide d'1 semaine.** Toutes étapes mais condensées.

**Enquête complète d'1 mois.** Toutes étapes développées.

**Enquête longue (3-6 mois).** Toutes étapes développées plusieurs cycles. Capitalisation continue.

#### K.13 — Synthèse — discipline du workflow

Le workflow ne **remplace pas** le jugement de l'analyste. Il structure le travail pour ne rien oublier et garantir la qualité. Discipline = pas zapper d'étape, pas chercher de raccourci sous pression.

> **Principe.** Un workflow bien suivi est l'assurance qualité de l'enquête. Une enquête sans workflow est une enquête qui s'écarte tôt ou tard de sa cible.

-----


### ANNEXE L — Modèles de livrables (gabarits)

Gabarits formatés pour les principaux livrables OSINT. À adapter selon contexte. Compléments aux Ch.87-90.

#### L.1 — Gabarit note courte (1 page)

```
[LOGO ou EN-TÊTE CABINET]

NOTE COURTE OSINT
Référence interne : [MANDAT/N-XXX]
Sujet : [...]
Auteur : [Cellule, Cabinet]
Date : [YYYY-MM-DD]
Classification / TLP : [TLP:AMBER+STRICT]
Niveau de confiance global : [Quasi-certain / Très probable / 
Probable / Possible / Indéterminable]

═══════════════════════════════════════════════════════════════

BLUF
[Conclusion principale en 3-5 lignes. Calibrée WEP. Recommandation 
principale en une phrase.]

CONTEXTE
[Cadrage : mandat, finalité, périmètre. 2-5 lignes.]

FAITS SAILLANTS COTÉS
| Fait | Source | Cot. |
|------|--------|------|
| [...] | [...] | A1 |
| [...] | [...] | B2 |
| [...] | [...] | C3 |
| ... (5-10 faits) ... | | |

LIMITES
- [Limite 1]
- [Limite 2]
- [Limite 3]

RECOMMANDATIONS
- Immédiat : [...]
- Court terme : [...]
- Moyen terme : [...]

ANNEXES (sur demande)
- [...]

═══════════════════════════════════════════════════════════════

Signature électronique : [PAdES-LT]
Hash SHA-256 de cette note : [...]
Horodatage : [YYYY-MM-DD HH:MM, eIDAS qualifié]
```

#### L.2 — Gabarit executive summary (2 pages)

```
EXECUTIVE SUMMARY — [TITRE DU DOSSIER]

Référence interne : [MANDAT/RAPPORT-XXX vY.Z]
Auteur : [Cabinet]
Date : [YYYY-MM-DD]
Classification : [TLP:AMBER+STRICT]
Niveau de confiance global : [Probable]

CONCLUSION PRINCIPALE (BLUF)

[Paragraphe de 5-8 lignes formulant la conclusion principale 
de l'enquête, calibrée WEP, intégrant la recommandation 
principale.]

POINTS CLÉS

1. [Premier point clé avec cotation] (A1)
2. [Deuxième point clé] (B2)
3. [Troisième point clé] (B2)
4. [Quatrième point clé] (C3)
5. [Cinquième point clé] (A1)
[... 5 à 10 points ...]

NIVEAU DE CONFIANCE PAR DIMENSION

- IR1 (structures offshore) : probable, élevé sur identification
- IR2 (flux financiers) : probable, modéré (expertise nécessaire)
- IR3 (patrimoine) : probable, élevé sur visible
- IR4 (désinformation) : très probable, élevé sur existence
- IR5 (contenus IA) : très probable, élevé

LIMITES MAJEURES

- [Limite 1 affectant niveau de confiance globalement]
- [Limite 2]

RECOMMANDATIONS PRINCIPALES

1. [Recommandation 1 actionnable]
2. [Recommandation 2]
3. [Recommandation 3]

[Page break]

Le rapport complet (corps + annexes) est joint pour 
approfondissement.
```

#### L.3 — Gabarit fiche briefing oral (slide format)

```
SLIDE 1 — Titre
- Sujet
- Référence
- Date
- Auteur

SLIDE 2 — BLUF
- Conclusion en 1-2 phrases
- Niveau de confiance

SLIDE 3 — Contexte
- Mandat
- Périmètre
- IR principales

SLIDE 4-7 — Faits saillants
(une slide par IR avec 3-5 faits cotés)

SLIDE 8 — Synthèse intégrée
- Convergences
- Graphe ou timeline résumé

SLIDE 9 — Limites
- 3-4 points

SLIDE 10 — Recommandations
- Actionnables
- Niveaux temporels

SLIDE 11 — Questions / discussion
```

**Durée standard.** 15-20 min présentation + 10 min questions.

#### L.4 — Gabarit note d'alerte CTI

```
NOTE D'ALERTE CTI
Référence : [CTI/A-XXX]
Sujet : [Menace identifiée]
Date : [YYYY-MM-DD HH:MM]
Auteur : [Analyste CTI]
TLP : [GREEN / AMBER]

═══════════════════════════════════════════════════════════════

SOMMAIRE

Type de menace : [malware / phishing / intrusion / exfil / autre]
Acteur supposé : [identifié / non identifié]
Cible : [client / sector / général]
Sévérité : [Faible / Modérée / Élevée / Critique]
Action recommandée : [Information / Vigilance / Mitigation / 
Incident response]

═══════════════════════════════════════════════════════════════

DESCRIPTION

[Description factuelle de la menace en 2-3 paragraphes.]

INDICATORS OF COMPROMISE (IOCs)

Hashs:
- [SHA-256]
- ...

Domaines:
- [domain1]
- ...

IPs:
- [IP1]
- ...

URLs:
- [URL1]
- ...

TTPs (MITRE ATT&CK)
- T[XXXX] : [technique]
- ...

═══════════════════════════════════════════════════════════════

RECOMMANDATIONS DÉFENSIVES

Immédiat :
- [Action 1]
- [Action 2]

Suivi :
- [Action 1]

═══════════════════════════════════════════════════════════════

RÉFÉRENCES
- [URL source 1]
- [Référence bulletin CISA / ANSSI / NCSC si applicable]
- Captures Hunchly : [...]

Distribution : [TLP:GREEN — partage communauté MISP autorisé]
```

#### L.5 — Gabarit rapport pour magistrat

Format renforcé Ch.90. Spécificités :

- Page de garde mentionnant statut judiciaire.
- Préambule explicitant cadre juridique.
- Méthodologie exhaustive.
- Chaque fait avec pièce annexée et hash.
- Conclusions strictement WEP.
- Annexe « catalogue de pièces » avec chain of custody.
- Signature PAdES-LT, horodatage eIDAS qualifié.

#### L.6 — Gabarit note d'update veille

```
UPDATE VEILLE — [Cible]
Référence : [MANDAT/U-NNN]
Période couverte : [YYYY-MM-DD à YYYY-MM-DD]
Date d'émission : [YYYY-MM-DD]
Classification : [TLP:AMBER+STRICT]

═══════════════════════════════════════════════════════════════

SYNTHÈSE

[Synthèse des évolutions significatives sur la période en 3-5 
lignes.]

ÉVOLUTIONS DÉTECTÉES

| Date | Évolution | Cot. | Impact |
|------|-----------|------|--------|
| [...] | [...] | A1 | [Élevé/Modéré/Faible] |
| ... | | | |

PAS D'ÉVOLUTION DÉTECTÉE
[Le cas échéant — confirme veille active.]

PROCHAINE NOTE
Date prévue : [...]
Points de vigilance : [...]
```

#### L.7 — Discipline éditoriale

**Cohérence visuelle.** Même mise en page entre rapports d'un cabinet. Charte graphique.

**Lisibilité.** Police lisible (Arial / Times 11pt, interligne 1.15-1.5). Marges raisonnables.

**Numérotation.** Pages numérotées « X / N ». Sections numérotées.

**Hyperliens.** Cross-références internes fonctionnelles.

**Tables des matières.** Pour rapports > 10 pages.

**Glossaire.** Pour rapports techniques avec public non-expert.

#### L.8 — Synthèse

Ces gabarits sont **modulaires**. Adapter selon contexte. La cohérence éditoriale est la signature du cabinet.

-----


### ANNEXE M — Templates graphes et timelines

Modèles de représentation visuelle pour graphes d'enquête et timelines. Cohérent avec Ch.83.

#### M.1 — Graphe d'enquête : conventions

**Types de nœuds (avec couleurs / formes recommandées).**

| Type | Forme | Couleur |
|---|---|---|
| Personne | Cercle | Bleu |
| Société | Carré | Vert |
| Domaine / Site | Losange | Orange |
| Compte (réseau social) | Triangle | Violet |
| Contenu (image, vidéo, doc) | Hexagone | Jaune |
| Lieu | Étoile | Rouge |
| Événement | Pentagone | Gris |
| Wallet crypto | Cercle pointillé | Marron |

**Types d'arêtes (avec styles).**

| Relation | Style | Description |
|---|---|---|
| Employer | Trait plein épais | Lien d'emploi (employeur → employé) |
| Director | Trait plein moyen | Direction d'entité juridique |
| Owner | Trait plein épais | Propriété |
| UBO | Trait plein très épais | Bénéficiaire effectif |
| Located at | Trait plein fin | Localisation |
| Communicates with | Trait pointillé | Communication |
| Mentions | Trait pointillé fin | Mention publique |
| Same operator | Trait double | Probabilité opérateur commun |
| Amplifies | Flèche fléchée | Amplification (RT, mention) |

**Sémantique force du lien.**
- Trait plein épais : lien démontré (A1).
- Trait plein moyen : lien établi (B2).
- Trait plein fin : lien probable (C3).
- Trait pointillé : lien suggéré (D-E).

#### M.2 — Graphe d'enquête MIRAGE : illustration

Structure :

- Marc Delaunay (cercle bleu central, taille élevée).
- TechnoVert SAS, Delta Consulting, Verde Holdings, SCI La Provence Familiale (carrés verts).
- 8 comptes X cluster désinformation (triangles violets).
- 9 canaux Telegram (triangles violets).
- 2 faux médias (losanges orange) connectés par GA partagé.
- Antoine Berthier (cercle bleu).
- Vidéo deepfake, fausses photos (hexagones jaunes).
- Mas Provence, villa Marrakech (étoiles rouges).

Arêtes principales :
- Delaunay → TechnoVert (employer, trait plein épais).
- Delaunay → Delta Consulting (director, A1).
- Delaunay → Verde Holdings (UBO, A1).
- Delta → Verde (flux financiers, B2).
- TechnoVert → Delta (flux probables, C3 pointillé épais).
- Faux médias ↔ comptes X (amplification).
- Berthier ← (cible) ← cluster désinformation.

#### M.3 — Outils de production graphes

**Maltego (commercial / Casefile gratuit).** Le standard professionnel. Pivots intégrés, exports propres.

**Gephi (open source).** Standard académique. Algorithmes communautés (Louvain), modularité.

**Neo4j Bloom.** Pour graphes property en local.

**Obsidian Graph View.** Pour vault personnel (limité visuellement).

**yEd Graph Editor.** Simple, exports clairs.

**Cytoscape.** Plus orienté biologie mais utilisable.

**Visualisations web : D3.js, Cytoscape.js, vis.js.** Pour intégration interactive.

#### M.4 — Bonnes pratiques graphe

**Lisibilité avant tout.** Un graphe de 500 nœuds bruts est illisible. Plusieurs vues :
- Vue d'ensemble (agrégée par communauté).
- Vues filtrées par type.
- Vues centrées sur entité principale.

**Hiérarchie visuelle.**
- Centralité → taille du nœud.
- Importance → couleur de bordure.
- Cotation → opacité.

**Annotations.** Légende, titre, date.

**Export.** PNG haute résolution + format vectoriel (SVG, PDF).

**Pour le rapport.** Export propre, légende explicite, références aux fiches.

#### M.5 — Timeline : conventions

**Axes.**
- Horizontal : temps.
- Vertical : type d'événement / acteur.

**Granularité.** Adaptée à l'enquête :
- Année : pour enquêtes pluriannuelles (MIRAGE 2019-2026).
- Mois : pour focus période (MIRAGE octobre 2025 - mai 2026).
- Jour / heure : pour analyse fine (suite déclenchement événement).

**Marqueurs.**
- Couleur par acteur ou type d'événement.
- Taille par importance.
- Forme par catégorie.

**Annotations.** Texte court, lisible.

#### M.6 — Timeline MIRAGE simplifiée

```
2019-06  TechnoVert : embauche Delaunay DAF
         ●
         
2020-03  Création Delta Consulting (Malte)
         ●
         
2020-Q3  Premiers flux supposés TechnoVert→Delta
         ○ (indice)
         
2022-01  Création Verde Holdings (Chypre)
         ●
         
2025-04  Audit interne TechnoVert
         ●
         
2025-05  Berthier signale en interne
         ○
         
2025-09-15  Licenciement Berthier
         ●●● (événement majeur)
         
2025-10-12  Création verites-technovert.com
         ●
         
2025-10-18  Création info-finance-eu.com
         ●
         
2026-03-03  Vidéo deepfake publiée
         ●●● (événement majeur)
         
2026-05-16  Mandat MIRAGE
         ●
```

#### M.7 — Outils timeline

**Timeline Explorer (Eric Zimmerman, gratuit).** Standard forensique.

**Aeon Timeline (commercial).** Très puissant pour multi-couches.

**Knightlab Timeline JS (gratuit).** Pour publication web.

**Tableau / Excel.** Simple, pour rapport.

**Plotly Python / R.** Pour intégration scripted.

#### M.8 — Synthèse — visualisations

**Graphe + Timeline = vue 360°.** Le graphe répond « qui avec qui ». La timeline répond « quand et dans quel ordre ». Le croisement révèle les patterns dynamiques.

> **Principe.** Une visualisation bien conçue rend visible ce que les pages de texte n'arrivent pas à dire. Une visualisation mal conçue cache plus qu'elle ne révèle. Discipline iconographique = compétence d'analyste mature.

-----


### ANNEXE N — Catalogue IA / agentic OSINT 2026

Catalogue détaillé des outils IA et agentic spécifiquement utiles à l'OSINT en 2026, compléments aux Ch.60-69.

#### N.1 — LLMs commerciaux cloud

**Claude (Anthropic).** Modèles : Claude Opus 4.7, Claude Sonnet 4.6, Claude Haiku 4.5. Forces : raisonnement structuré, capacités d'instruction precise, multimodal (texte + image), sécurité. Usages OSINT : analyse de corpus, extraction d'entités, raisonnement ACH-style, vérification de cohérence. Tarification : freemium / abonnement / API. Niveau OPSEC : standard cloud (sensible à enquêtes confidentielles).

**ChatGPT / GPT-4 / o-series (OpenAI).** Multimodal très mature, écosystème riche. Usages OSINT : tous standards + génération de code. API mature.

**Gemini (Google).** Multimodal natif, intégration Google Search, contexte long (jusqu'à 1M tokens). Usages OSINT : analyse de très longs corpus.

**Mistral.** Européen. Open source partial. Mistral Large compétitif. Standard pour souveraineté EU.

#### N.2 — LLMs locaux open source

**Llama 3.3 / Llama 4 (Meta).** Référence open source 2026. Performances ~Claude 2023.

**Mistral Large.** Européen, déployable local.

**Qwen 2.5 / Qwen 3 (Alibaba).** Multilingue chinois fort, open source.

**DeepSeek R1.** Raisonnement avancé, open source.

**Gemma 2 / 3 (Google).** Compact, multilingue.

**Phi-4 (Microsoft).** Compact mais performant.

**Outils déploiement.**
- **Ollama** : standard, simple, multi-modèles.
- **LM Studio** : interface graphique.
- **vLLM** : production scale.
- **Llama.cpp** : low-level efficient.

#### N.3 — LLMs multimodaux (vision)

**GPT-4V (OpenAI).** Standard mature multimodal.

**Claude (avec vision).** Capacités équivalentes en analyse d'images.

**Gemini.** Multimodal natif.

**LLaVA (open source local).** Pour OPSEC stricte.

**Qwen-VL (open source).** Alternative multilingue.

#### N.4 — Agents et frameworks

**LangChain.** Framework standard pour agents (Python, JS).

**CrewAI.** Multi-agents orchestrés, simple.

**AutoGen (Microsoft).** Multi-agents conversationnels.

**OpenAI Assistants API.** Agents managés par OpenAI.

**Claude tool use.** Capacités d'orchestration d'outils par Claude.

**LlamaIndex.** RAG et knowledge graphs avec LLMs.

#### N.5 — Outils spécifiques OSINT IA

**Géolocalisation.**
- **GeoSpy** (geospy.ai) : géolocalisation par photo.
- **GeoSeer, PicArta** : alternatives.

**Détection contenus IA.**
- **Hive Moderation** : multi-modèles, standard.
- **Optic AI or Not** : interface simple.
- **Sensity AI** : deepfakes (institutionnel).
- **Intel FakeCatcher** : physiologique.
- **Reality Defender** : enterprise.
- **Resemble Detect** : voix.
- **GPTZero, Originality** : texte (faible fiabilité).

**Watermarking.**
- **SynthID** (Google) : détecteur intégré progressivement.

**Provenance.**
- **C2PA viewer** : extension navigateur.
- **contentcredentials.org/verify**.

**OSINT search assistants.**
- **Perplexity** : RAG avec citations.
- **You.com** : alternative.
- **Microsoft Copilot** : intégration Bing.

**Transcription / traduction.**
- **Whisper** (OpenAI, open source) : transcription standard.
- **Whisper.cpp** : local efficient.
- **DeepL** : traduction.

#### N.6 — Outils ASM agentic

**Bitsight, RiskIQ, SecurityScorecard.** Standards enterprise.

**Censys Continuous, Shodan Monitor.** ASM continu.

**Palo Alto Cortex Xpanse.** Enterprise ASM.

#### N.7 — Outils CTI agentic

**Recorded Future.** Référence standard CTI institutionnelle. AI-augmented.

**Mandiant Advantage.** Google / Mandiant.

**CrowdStrike Falcon X.** Enterprise.

**Flashpoint, KELA, Cybersixgill.** Dark web focused.

**Searchlight Cyber, DarkOwl, Flare.** Deep web monitoring.

#### N.8 — Outils SOCMINT agentic

**Brandwatch, Talkwalker, Meltwater.** Enterprise SOCMINT.

**Pulsar, Sprinklr.** Alternatives.

**Babel Street.** OSINT institutionnel multi-source.

**Fivecast.** Australien, suite agentic intégrée.

**ShadowDragon.** OSINT enterprise.

#### N.9 — Outils due diligence agentic

**Sayari.** OSINT moderne avec IA, fort sur opacité.

**Sigma Ratings.** AI-driven due diligence.

**Quantexa.** Entity resolution massive.

**OpenSanctions.** Gratuit, alimente l'écosystème.

#### N.10 — Knowledge graphs et IA

**Apache Jena, Neo4j Community.** Pour déploiement local.

**LangChain GraphRAG / LlamaIndex Knowledge Graph.** Couplage LLM + graphe.

**Microsoft GraphRAG.** Standard 2024-2026.

#### N.11 — Évaluation et benchmarking

**Pour comparer LLMs.**
- **Open LLM Leaderboard** (Hugging Face).
- **Chatbot Arena**.
- **MMLU, HumanEval** : benchmarks classiques.

**Pour évaluation spécifique OSINT.** Pas de benchmark standardisé en 2026. Évaluation au cas par cas.

#### N.12 — Stratégie de choix d'outils

**Pour budget limité (analyste indépendant).**
- LLMs locaux Ollama + Llama 3.3 70B.
- Outils OSINT classiques gratuits.
- Hive Moderation freemium.
- Investissements ciblés (Hunchly, Hudson Rock si nécessaire).

**Pour cabinet moyen.**
- Mix LLMs locaux + Claude / GPT-4 abonnements.
- Outils standards payants (Pappers Pro, OpenCorporates, DomainTools).
- Détection IA payante (Sensity si volume).
- Maltego.

**Pour institution.**
- Suite enterprise (Bitsight, Recorded Future, Sayari, Maltego enterprise, etc.).
- Custom agents (LangChain CrewAI développé interne).
- LLMs locaux + cloud premium.
- Capacités CTI / OSINT / ASM intégrées.

#### N.13 — Évolution rapide

L'écosystème évolue **mensuellement**. Veille trimestrielle minimum :
- Sorties LLMs majeures.
- Nouvelles applications agentic.
- Outils OSINT spécifiques émergents.
- Évolution des outils existants (deprecations, mises à jour API).

**Sources de veille.**
- HackerNews, /r/MachineLearning, /r/LocalLLaMA.
- AnalyticsIndiaMag, VentureBeat.
- Bellingcat resources / OSINT communities.
- Twitter/X de chercheurs et praticiens.

#### N.14 — Synthèse — discipline IA

L'analyste 2026 :
- **Maîtrise** une stack IA cohérente (locale + cloud).
- **Adapte** ses outils au niveau de menace de l'enquête (cloud OK pour standard, local pour sensible).
- **Vérifie** systématiquement les sorties (Retrieve-Store-Cite).
- **Veille** continuellement.
- **Forme** son équipe.

> **Principe.** L'IA est l'outil. L'analyste reste l'artisan. La compétence n'est pas dans l'outil, elle est dans la façon dont l'analyste l'oriente, le vérifie, et l'intègre dans sa méthodologie.

-----


### ANNEXE O — Mapping de la bibliothèque OSINT 2026

Cette annexe finale présente la **vue d'ensemble de la bibliothèque OSINT 2026** dont le présent cours fait partie, en clarifiant les liens entre cours et les usages recommandés.

#### O.1 — Architecture de la bibliothèque

La bibliothèque se compose de **5 cours principaux** :

1. **OSINT Mastery vFULL 2026** (présent cours). Cours maître. 103 chapitres, 15 annexes. Couvre l'ensemble de la discipline OSINT en vue maître.

2. **OSINT Crypto vFULL.** Cours spécialisé sur l'investigation crypto-actifs et blockchain. Profondeur sur clustering, attribution, mixers, bridges, cashout, NFTs forensique, DeFi, sanctions crypto, IA on-chain.

3. **Dark Web vFULL.** Cours spécialisé sur le Dark Web et DARKINT. Profondeur sur architecture Tor / I2P / Freenet, marketplaces, forums clandestins, leak sites ransomware, méthodologies LEA, IA criminelle.

4. **FININT Investigation Financière vFULL.** Cours spécialisé sur le renseignement financier. Profondeur sur UBO complexes, schémas de blanchiment, AML/CFT, asset recovery, comptabilité forensique, KYC/KYB approfondi, CSDDD.

5. **OSINT Synthèse.** Cours bref de synthèse. Vue très condensée pour révision rapide.

#### O.2 — Documents complémentaires

**OSINT Bible 2026 (.txt).** Compilation extensive de notes, références, ressources. Non structurée comme cours mais riche en pointeurs.

**Documents académiques et professionnels.**
- IntelTechniques OSINT (11/2025) — Michael Bazzell.
- 25 articles D. Mider.
- OSINT mini-guide 2026.
- Art of Open Source Intelligence (D. Bazzell).
- OSINT report final.
- OSINT practical guide 1.
- Présentation OSINT novembre 2026.
- Articles RGPD et OSINT.
- Allan Deneuville — OSINT Publictionnaire.
- Cart Thibault TB 2025.
- LJI Recherche — révolution numérique OSINT et guerre du renseignement (Romain D, Juliet P, 05/2025).
- GIJN Citizens Investigation Guide.

Ces documents enrichissent les références théoriques et historiques.

#### O.3 — Parcours recommandés

**Pour débutant en OSINT.**
- Démarrer par **OSINT Synthèse** (vue très rapide).
- Approfondir avec **OSINT Mastery vFULL 2026** (cours maître).
- Spécialiser ensuite selon besoins (Crypto / Dark Web / FININT).

**Pour praticien intermédiaire.**
- Direct sur **OSINT Mastery vFULL 2026** Parties I-V (rappels et calibration 2026).
- Approfondissement Parties VII-XII selon zones de progression.
- Spécialisation par cours dédié.

**Pour praticien senior.**
- **OSINT Mastery vFULL 2026** sélectivement : Partie VIII (deepfakes 2026), Partie IX (IA et agents), Partie X (passerelles), Partie XI (cotation 2026).
- Cours spécialisés selon spécialité.
- Documents complémentaires académiques pour réflexion.

#### O.4 — Lien entre cours et présent master

| Sujet | Master | Cours spécialisé |
|---|---|---|
| Investigation personne | Couverture complète Ch.26-35 | — |
| Investigation corporate | Vue maître Ch.36-41 | FININT pour profondeur |
| Infrastructure web | Couverture complète Ch.39-41 | — |
| FININT financier | Vue maître Ch.70-71 | **FININT vFULL** |
| Crypto | Vue maître Ch.72 | **OSINT Crypto vFULL** |
| Dark Web | Vue maître Ch.44 | **Dark Web vFULL** |
| CTI | Vue maître Ch.74-75 | (cours CTI dédié, à venir) |
| Désinformation | Couverture complète Ch.35, 76 | — |
| Deepfakes / Provenance | Couverture complète Ch.53-59 | — |
| IA et agents | Couverture complète Ch.60-69 | — |
| GEOINT | Couverture complète Ch.45-52 | — |
| Production / Rapports | Couverture complète Ch.87-92 | — |

#### O.5 — Capitalisation et mise à jour

**Politique de mise à jour.** L'écosystème OSINT évolue rapidement. Les cours sont **datés** (vFULL 2026 signifie cohérence au moment de la production, mai 2026).

**Révisions prévues.**
- Mises à jour trimestrielles sur outils en tableaux récap.
- Mises à jour majeures annuelles sur méthodologie.

**Veille des évolutions.**
- Suivi des publications Bellingcat, OCCRP, EU DisinfoLab, VIGINUM, Stanford SIO.
- Conférences (OSMOSIS, OSINT Day, NICAR).
- Communautés (Discord OSINT, Reddit /r/OSINT, Twitter/X OSINT).

#### O.6 — Articulation pédagogique

**Logique du master.** Couvrir l'ensemble de la discipline OSINT avec assez de profondeur pour autonomie complète sur les enquêtes standards, et signaler explicitement les seuils d'escalade vers cours spécialisés ou expertise externe.

**Logique des cours spécialisés.** Approfondir un domaine particulier au-delà de ce que le master peut traiter (sous peine d'exploser en volume).

**Logique de l'écosystème.** L'analyste OSINT 2026 maîtrise le **master**, se spécialise via **1-2 cours spécialisés** selon son métier, et **coopère** avec experts pour le reste.

#### O.7 — Évolution prévisionnelle

**Cours à venir (potentiels).**
- OSINT CTI vFULL : approfondissement cyber threat intelligence.
- OSINT Géopolitique vFULL : approfondissement renseignement géopolitique et conflits.
- OSINT Compliance vFULL : approfondissement KYC/KYB/CSDDD.
- OSINT Forensique vFULL : approfondissement preuve numérique et expertise.

**Évolutions du master 2026.** Les versions ultérieures intégreront :
- Évolutions IA (modèles plus puissants, nouveaux types de contenus synthétiques).
- Évolutions réglementaires (compléments AI Act, nouvelles directives UE).
- Évolutions plateformes (restrictions / ouvertures).
- Nouveaux outils émergents.

#### O.8 — Recommandations d'usage

**Comme manuel de référence.** À consulter au quotidien selon besoin (annexes en particulier).

**Comme support de formation.** Apprenants suivent le parcours en 6-12 semaines.

**Comme socle pédagogique d'équipe.** Cabinet adopte le master comme référence commune, déclinée par fiches méthodologiques internes.

**Comme outil de revue.** Pour audit interne d'une enquête (« a-t-on suivi le workflow ? »).

#### O.9 — Communauté et contribution

L'OSINT mature 2026 est une discipline **collaborative**.

**Communautés à suivre.**
- Bellingcat (training, articles).
- OCCRP (méthodologies, leaks).
- EU DisinfoLab (CIB).
- VIGINUM (FR, ingérences).
- Stanford Internet Observatory (académique).
- Recorded Future (CTI commercial).
- Trace Labs (missing persons OSINT).
- ProPublica (journalisme data).
- ICIJ (leaks investigations).

**Contribution.**
- Publication d'articles (médias, conférences).
- Partage de méthodologies (avec déontologie).
- Mentorat de débutants.
- Contribution à projets open source (outils, datasets).

#### O.10 — Mot final de la bibliothèque

> **Principe.** La bibliothèque OSINT 2026 est conçue comme un **écosystème cohérent** : master pour vue d'ensemble, cours spécialisés pour profondeur, documents complémentaires pour réflexion. L'analyste navigue cet écosystème selon ses besoins. Aucun cours n'est complet seul ; tous ensemble forment une discipline mature.
>
> L'OSINT 2026 est plus exigeante que jamais (cadre légal renforcé, contenus synthétiques omniprésents, restrictions plateformes, sophistication adverse). Mais elle est aussi plus puissante (outils IA, knowledge graphs, agents, infrastructure de partage).
>
> Cet équilibre demande **discipline méthodologique stricte**, **éthique rigoureuse**, **veille continue**, **collaboration** entre praticiens. Le master en pose les fondations. Le métier en révèle la profondeur. La vie professionnelle en révèle la dimension humaine — au service de la justice, de la transparence, de la sécurité, sans jamais oublier la dignité des personnes.

-----


## FIN DU COURS

> **OSINT Mastery vFULL 2026** — version exhaustive
>
> 103 chapitres répartis en 12 parties.
> 15 annexes complémentaires.
> Fil rouge MIRAGE en 21 épisodes intégrés.
> 11 cas pratiques + 1 exercice final.
>
> Conçu en mai 2026 comme cours maître de la bibliothèque OSINT. À utiliser de façon autonome ou en articulation avec les cours spécialisés (OSINT Crypto vFULL, Dark Web vFULL, FININT Investigation Financière vFULL) et la synthèse rapide (OSINT Synthèse).
>
> Discipline. Calibration. Éthique. Veille. Collaboration. — Les cinq piliers de l'analyste OSINT 2026.
