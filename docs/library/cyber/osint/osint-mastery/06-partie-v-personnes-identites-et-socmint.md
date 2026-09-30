---
title: PARTIE V — Personnes, identités et SOCMINT
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 6
chapters: 15
---

> **Ce que cette partie apprend.** Identifier de façon fiable une personne physique, exploiter les pivots email / téléphone / username / photo / document, déanonymiser un pseudonyme avec rigueur méthodologique, conduire une investigation SOCMINT multi-plateformes (LinkedIn, Facebook, X, Instagram, TikTok, YouTube, Telegram, Discord, VK, etc.), détecter les faux comptes et comportements coordonnés inauthentiques (CIB).
>
> **Ce qu'elle ne couvre pas.** L'investigation corporate (Partie VI), l'IMINT et la géolocalisation (Partie VII), la vérification de contenus synthétiques (Partie VIII).
>
> **Ce que vous saurez faire après cette partie.** Identifier une personne avec corroboration multi-sources, mobiliser les pivots email/username/téléphone/photo, conduire un SOCMINT sur les principales plateformes, détecter un cluster de faux comptes coordonnés.

-----

### Chapitre 26 — Identification de personne physique

#### 26.1 Identifier : un acte plus complexe qu'il n'y paraît

**Identifier** une personne en OSINT ne se réduit pas à trouver son nom. C'est confirmer, avec un faisceau d'éléments convergents, que la personne dont on parle est bien **celle qu'on croit** et **personne d'autre**. Les homonymes, les usurpations, les coïncidences sont des pièges récurrents.

Une identification mature s'appuie sur **plusieurs dimensions** (nom + date de naissance + lieu + parcours + photo + sélecteurs uniques) jusqu'à atteindre un niveau de confiance proportionné à l'enjeu.

#### 26.2 Désambiguïsation : le premier réflexe

**Avant** toute investigation approfondie sur une personne, vérifier qu'il n'y a pas confusion.

**Cas typique du piège.** Dans une enquête sur « Pierre Martin, DAF de société X », l'analyste trouve sur LinkedIn six profils nommés Pierre Martin. Investiguer le mauvais détruit l'enquête.

**Méthode.**
- Combiner nom + employeur actuel + secteur.
- Cross-vérifier date d'arrivée à l'employeur (presse, communiqué).
- Photo (LinkedIn, presse).
- Parcours antérieur (cohérence).

#### 26.3 Sources de désambiguïsation principales

**Presse.** Communiqués de l'employeur, articles avec photo, mentions sectorielles.

**LinkedIn.** Profil professionnel, parcours, connections.

**Pappers / Companies House.** Dirigeants déclarés officiellement.

**Wikipédia / Wikidata.** Pour personnalités publiques. Wikidata fournit identifiants structurés.

**HATVP.** Pour PEP français (déclarations d'intérêt).

#### 26.4 Sélecteurs identifiants

Un **sélecteur identifiant** est une information qui distingue **uniquement** une personne.

**Sélecteurs très forts.**
- Numéro SIREN comme dirigeant.
- Email professionnel confirmé.
- Numéro de téléphone.
- Identifiant officiel (CNI, passeport, fiscal) — rarement publics.

**Sélecteurs forts.**
- Username unique cross-plateformes.
- Photo identifiable.
- Date et lieu de naissance précis.
- Adresse résidentielle exclusive.

**Sélecteurs faibles.**
- Nom seul.
- Année de naissance seule.
- Profession générale (« DAF »).
- Ville seule.

#### 26.5 Identité civile vs identité publique

**Identité civile.** Nom à l'état civil, adresse, date et lieu de naissance.

**Identité publique.** Ce que la personne expose sur les sources ouvertes.

Les deux ne coïncident pas toujours :
- Pseudonymes professionnels (artistes, journalistes).
- Changement de nom (mariage, naturalisation).
- Identités antérieures (ex-conjoint, naissance dans autre pays).

L'investigation doit parfois remonter à l'identité antérieure.

#### 26.6 People search engines américains (limites RGPD)

**TruePeopleSearch, FastPeopleSearch, Whitepages, BeenVerified.** Bases de données américaines de people search.

**Capacités.**
- Adresses passées et actuelles.
- Numéros de téléphone connus.
- Membres de famille.
- Voisins.

**Limites RGPD.** Ces services traitent données personnelles. Leur usage par analyste en UE doit reposer sur base légale (intérêt légitime documenté), et reste juridiquement délicat.

**Pour cibles US.** Restent référence. Pour cibles UE, à utiliser avec parcimonie et documentation rigoureuse.

#### 26.7 Outils français de people search

**Pages Jaunes, Annuaire.** Limités mais utiles pour adresses anciennes.

**Verif.com, Societe.com.** Croisement avec sociétés.

**Avis de naissance / mariage / décès.** Presse régionale (archives partiellement payantes).

**Geneanet, FamilySearch.** Généalogie. Utile pour cartographie familiale et héritages.

#### 26.8 Cohérence des éléments

Une identification mature **fait converger** plusieurs dimensions.

**Convergence forte (identification quasi-certaine).**
- Nom + photo + employeur + parcours cohérent + date naissance + adresse.
- Sources multiples indépendantes confirmant.

**Convergence moyenne.**
- Nom + photo + parcours probable.
- Source unique ou faisceau partiel.

**Convergence faible.**
- Nom + ville.
- Suggère une piste, pas une identification.

#### 26.9 Pièges classiques d'identification

**Homonymie.** Deux personnes du même nom dans le même secteur. Désambiguïsation par sélecteurs forts.

**Usurpation.** Un faux profil au nom de la cible. Cohérence interne du faux suffit parfois à tromper si on n'est pas vigilant.

**Vieillissement.** Photo récente vs photo d'archives. Détection des évolutions plausibles.

**Erreur d'attribution.** Confondre la personne réelle avec un mystificateur sur réseaux sociaux.

**Faux profils IA.** Photo générée par IA (Ch.30 et Ch.35).

#### 26.10 Cotation finale d'identification

Pour chaque identification, **cotation Admiralty** explicite.

**A1.** Identification multi-corroborée par sources officielles + cohérence parcours + photos + multiples sélecteurs.

**B2.** Identification probable, faisceau d'indices convergents, mais source unique ou corroboration partielle.

**C3.** Identification possible, signaux convergents mais pas suffisamment.

**D4-F6.** Identification douteuse ou non évaluable. Ne pas conclure.

> **MIRAGE — Épisode 4 : Identification de personne**
>
> L'analyste vérifie l'identification de Marc Delaunay, DAF de TechnoVert SAS, sujet central du mandat.
>
> **Sources convergentes.**
> - **Pappers TechnoVert** : « Marc Delaunay, Directeur Administratif et Financier, nommé le 15 juin 2019 » (A1).
> - **Communiqué TechnoVert** du 12 juin 2019 : annonce de nomination, photo officielle (A1).
> - **LinkedIn Marc Delaunay** : profil correspondant, photo identique au communiqué, parcours cohérent (X-Ponts, audit Big 4, DAF industrie depuis 2014, DAF TechnoVert depuis juin 2019) (A1 pour parcours déclaré).
> - **Interview vidéo professionnelle 2023** (chaîne YouTube secteur) : voix, image, prénom et nom mentionnés (A1).
> - **Mentions presse économique régionale** : 4 articles entre 2020 et 2024 mentionnant « Marc Delaunay, DAF de TechnoVert » (B1).
>
> **Désambiguïsation.** Plusieurs profils LinkedIn portent ce nom. Le profil cible est isolé par : photo correspondant communiqué + parcours déclaré cohérent avec presse + employeur actuel.
>
> **Sélecteurs forts retenus.**
> - Email professionnel : marc.delaunay@technovert.fr (déduit format standard TechnoVert ; à confirmer via Hunter.io).
> - SIREN TechnoVert : Delaunay listé comme représentant.
> - Photo : capturée et hashée.
> - Année de naissance estimée : 1976 (déduit X-Ponts promo 2002, généralement 23-26 ans à la sortie).
>
> **Cotation identification globale.** A1. Identification multi-corroborée, plusieurs sources indépendantes, photo confirmée, parcours cohérent.
>
> **Sélecteurs disponibles pour pivots ultérieurs.**
> - Nom complet : Marc Delaunay.
> - Email pro : marc.delaunay@technovert.fr (à valider).
> - Email perso : à rechercher.
> - Téléphone perso : à rechercher.
> - Username cross-plateformes : à investiguer (pseudonymes possibles).
> - Adresse résidentielle : à rechercher.
> - Famille proche : à investiguer avec déontologie.
>
> Ces sélecteurs seront mobilisés au fil des épisodes suivants.

-----

### Chapitre 27 — Pivots email, téléphone, username, photo

#### 27.1 Le pivot comme opération centrale

Une fois une **identité** confirmée (Ch.26), l'enquête mobilise des **pivots** : opérations qui transforment un sélecteur en plusieurs autres.

**Exemple.** Email → comptes liés sur multiples plateformes → usernames → autres emails → numéros de téléphone → photos → réseaux sociaux secondaires. Chaque pivot ouvre des dimensions nouvelles.

L'analyste maître les pivots fait des progrès **exponentiels** sur une cible. L'analyste qui ne maîtrise que les recherches frontales reste limité.

#### 27.2 Pivot email

**Validation de l'email.**

**Hunter.io.** Outil standard. Trouve les emails associés à un domaine. Vérifie la validité.

**Snov.io.** Alternative.

**Email Verifier services.** Vérification SMTP.

**Format guessing.** À partir du nom et du domaine, deviner le format probable (`prenom.nom@`, `pnom@`, `prenom@`, etc.).

**Pivots depuis un email confirmé.**

**Holehe** (open source, gratuit). Liste les comptes en ligne probablement associés à un email. Très large couverture (130+ services).

```bash
holehe marc.delaunay76@gmail.com
```

**Epieos** (epieos.com, freemium). Détection des comptes Google, autres comptes liés. Pivots automatisés.

**GHunt** (open source). Pour comptes Google. Reveal photo profil Google, ID Google, etc.

**HIBP, DeHashed, IntelX.** Recherche dans breaches (Ch.42).

**Hudson Rock.** Stealer logs (Ch.43).

**WHOIS historique.** Si email pre-2018, peut apparaître dans WHOIS de domaines.

**Forums et code public.** Recherche GitHub avec email, forums archivés.

**Cas MIRAGE.** L'email `marc.delaunay76@gmail.com` (déduit MIRAGE 4) ouvre énormément de pivots : Holehe → confirmation présence sur Twitter, Instagram, Pinterest, Spotify, Apple. HIBP → 6 breaches. Hudson Rock → stealer log avec credentials Binance. **Email = sélecteur pivot majeur.**

#### 27.3 Pivot téléphone

**Validation du format.** Standards internationaux (E.164). Bibliothèques (libphonenumber Google).

**Outils.**

**Truecaller.** Identification d'un numéro inconnu. Crowdsourcé.

**WhatsApp Web / Telegram.** Vérification de présence (déontologie attentive).

**Numverify, NumValidate.** Validation et opérateur.

**Recherches presse.** Numéros parfois publiés par cible (signature email pro).

**Pivots.**
- Téléphone → WhatsApp profil (photo, statut).
- Téléphone → Telegram profil (si non masqué).
- Téléphone → identité (Truecaller).
- Téléphone → adresse (recherche inverse limitée FR).

**Limites France.** Recherche directe numéro → identité **strictement limitée légalement** hors LEA.

#### 27.4 Pivot username

**Sherlock** (open source, GitHub). Standard pour recherche d'username cross-plateformes (300+ sites).

```bash
sherlock mdelaunay76
```

**WhatsMyName** (whatsmyname.app). Alternative web.

**NameCheckup, Knowem.** Alternatives commerciales.

**Méthode.**
1. Tester le username probable.
2. Examiner les hits : photo profil, bio, activité cohérente.
3. Cross-vérification par autres sélecteurs.
4. Cotation prudente (homonymie possible).

#### 27.5 Pivot photo

Voir Ch.30 pour reconnaissance faciale détaillée.

**Méthode rapide.**
1. Recherche inversée Yandex / Google Lens.
2. Examen des occurrences.
3. PimEyes / FaceCheck.ID si justification légale (UE).

**Pivots photo.**
- Photo profil partagée entre comptes → indique opérateur commun.
- Photo lieu identifiable → géolocalisation (Ch.48).
- Photo avec EXIF → métadonnées (Ch.29).

#### 27.6 Pivot document

Voir Ch.29 pour métadonnées documents.

**Pivots typiques.**
- Métadonnées Office / PDF révèlent auteur, modificateur, logiciel.
- Chemins absolus révèlent identité ou organisation.
- Co-auteurs révèlent réseau.

#### 27.7 Méthodologie pivot itératif

**Cycle.**

1. **Sélecteur initial** (nom).
2. **Premier pivot** (LinkedIn → email pro probable).
3. **Validation** (Hunter.io confirme format).
4. **Pivot suivant** (email → Holehe → autres comptes).
5. **Validation** de chaque hit.
6. **Pivot suivant** (comptes → usernames).
7. **Sherlock sur usernames** → autres plateformes.
8. **Pivot suivant** (photos partagées → reverse search).
9. ...

L'enquête s'élargit en arbre, jusqu'à épuiser les pivots productifs ou atteindre la cible des IR.

#### 27.8 Arrêt et discipline

**Discipline.** Ne pas se laisser **emporter** par la fascination des pivots. À chaque étape :
- Cet élément sert-il une IR ?
- Si non, est-il pertinent ?
- Si non, ne pas l'inclure.

L'enquête peut produire des centaines d'entités si l'analyste laisse les pivots aller sans contrôle. Discipline = focus sur IR.

#### 27.9 Cotation des pivots

Chaque pivot produit des éléments à coter.

**Pivot par sélecteur fort + corroboration multi-sources.** Cotation A1-B2.

**Pivot par sélecteur faible.** Cotation D3-F6 par défaut.

**Pivot par déduction sans confirmation.** Hypothèse, F6 jusqu'à validation.

#### 27.10 Outils synthèse

| Pivot | Outils principaux |
|---|---|
| Email validation | Hunter.io, Snov.io |
| Email → comptes | Holehe, Epieos, GHunt |
| Email → breaches | HIBP, DeHashed, IntelX |
| Email → stealer logs | Hudson Rock |
| Téléphone | Truecaller, WhatsApp Web (déontologie) |
| Username | Sherlock, WhatsMyName |
| Photo | Yandex, Google Lens, PimEyes |
| Document | ExifTool |

> **Principe.** Le pivot mature transforme une enquête. Mais le pivot non discipliné égare. Maîtriser les pivots = compétence d'analyste senior.

-----

### Chapitre 28 — Identité numérique et pseudonymes

#### 28.1 L'identité numérique : multi-couches

Une **identité numérique** est rarement monolithique. Une personne a typiquement :
- Une identité civile (vraie identité, parfois affichée).
- Une ou plusieurs identités professionnelles (LinkedIn, signature email).
- Une ou plusieurs identités semi-privées (Facebook, Instagram avec pseudo).
- Une ou plusieurs identités pseudonymes (X, Reddit, Discord, gaming).
- Éventuellement des identités cachées (forums spécialisés, dark web).

L'investigation OSINT cherche souvent à **relier ces couches** : qui est X sur Reddit ? Qui opère ce compte Twitter pseudonyme ? Cette dé-anonymisation prudente est l'un des défis méthodologiques majeurs.

#### 28.2 Pourquoi les couches existent

**Compartimentation légitime.** Un professionnel veut séparer pro / perso. Un militant peut craindre des représailles. Un journaliste protège ses sources.

**Évolution de l'usage.** Un compte pseudo créé pour un usage spécifique en 2015 a accumulé une histoire qui rend le rebranding coûteux.

**Compartimentation problématique.** Fraude, harcèlement, désinformation peuvent exploiter le pseudonymat.

L'analyste OSINT respecte le pseudonymat **sauf** quand l'investigation justifie sa percée — typiquement pour fraude, atteinte aux personnes, criminalité.

#### 28.3 Méthodologie de dé-anonymisation prudente

La dé-anonymisation se conduit avec rigueur méthodologique et éthique.

**Étape 1 — Justification.** Pourquoi dé-anonymiser ? Quelle est la base légitime et proportionnée ? La justification est documentée dans le SOR.

**Étape 2 — Sélecteurs cross-plateformes.** Username, photo de profil, style d'écriture, fuseau horaire, sujets, cercles sociaux.

**Étape 3 — Faisceau d'indices.** Aucun sélecteur isolé ne suffit. Le faisceau converge.

**Étape 4 — Vérification.** Avant de conclure, vérifier par sources indépendantes.

**Étape 5 — Cotation prudente.** « Hypothèse forte » ≠ « identification certaine ».

**Étape 6 — Diffusion contrôlée.** Une dé-anonymisation reste dans le périmètre du mandat, jamais publique.

#### 28.4 Username reuse comme signal

Un username identique cross-plateformes est un signal fort.

**Vérifications.**
- Photo de profil identique ?
- Bio cohérente ?
- Date de création comparable ?
- Activité corrélée (mêmes sujets, mêmes heures) ?
- Liens entre comptes (cross-promotion) ?

Plus de signaux convergents = hypothèse plus forte.

#### 28.5 Photo de profil comme signal

**Méthode.**
- Capturer la photo originale.
- Recherche inversée (Yandex, Google Lens) pour autres apparitions.
- Comparaison croisée avec autres comptes.

**Limites.**
- Photo générique (paysage, célébrité) = signal faible.
- Photo générée IA = potentiellement réutilisable mais détectable.
- Vol d'image (photo de tiers utilisée) = faux positif possible.

#### 28.6 Style d'écriture (stylométrie légère)

Le **style d'écriture** est un signal sous-utilisé en OSINT.

**Indicateurs stylométriques.**
- Vocabulaire récurrent (mots-fétiches).
- Fautes typiques (frappes, orthographe, ponctuation).
- Tournures de phrase.
- Émojis utilisés.
- Longueur moyenne des messages.
- Capitalisation, espaces.

**Outils.**
- **JStylo** (open source, académique).
- Analyses manuelles fines pour corpus limité.
- LLMs assistants (avec validation) pour comparaison de styles.

**Cas d'usage.** Comparer le style d'un compte pseudonyme suspect avec le style identifié de la cible (emails, posts publics).

**Limites en 2026.** Les LLMs permettent de masquer ou imiter un style. La stylométrie reste utile mais affaiblie.

#### 28.7 Fuseau horaire et cadence

**Signaux temporels.**
- Heures d'activité (post matinaux vs nocturnes).
- Jours de la semaine actifs vs inactifs.
- Vacances corrélées (silence à des dates précises).
- Décalage horaire perceptible.

**Méthode.** Compiler les timestamps de posts publics sur 4-8 semaines. Visualiser en heatmap. Comparer avec timezone supposé de la cible.

**Outil simple.** Pandas + matplotlib en notebook Jupyter.

#### 28.8 Sujets et cercles sociaux

**Sujets.** Les centres d'intérêt récurrents (industrie de niche, géographie spécifique, événements précis) sont discriminants.

**Cercles sociaux.** Les comptes suivis, suivants, mentionnés régulièrement forment un graphe social. Deux comptes pseudonymes avec un cercle social très similaire suggèrent un même opérateur ou un même milieu.

**Méthode.**
- Extraire les top 50 mentions/interactions du compte pseudonyme.
- Comparer avec le cercle connu de la cible.
- Recoupements significatifs = signal fort.

#### 28.9 Erreurs OPSEC de la cible

La dé-anonymisation réussit souvent grâce à des **erreurs OPSEC** de la cible elle-même.

**Erreurs classiques.**
- Tweet posté depuis le mauvais compte (compte pseudo vs compte officiel).
- Réutilisation d'un username dérivable du vrai nom.
- Photo de profil identique sur compte pseudo et compte civil.
- Email pseudo lié au téléphone civil.
- Géolocalisation activée dans EXIF d'une photo.
- Cross-promotion involontaire (mention d'un compte pseudo dans un post officiel).
- Confirmation par un proche (un parent qui tagge le compte pseudo).

Une investigation patiente expose souvent ces erreurs accumulées.

#### 28.10 Corrélations faibles vs fortes

| Type de corrélation | Force |
|---|---|
| Username identique | Forte |
| Photo profil identique | Très forte |
| Erreur OPSEC explicite (tweet depuis mauvais compte) | Quasi-certitude |
| Style d'écriture cohérent | Moyenne |
| Fuseau horaire cohérent | Faible (large population) |
| Sujets cohérents | Faible à moyenne |
| Cercle social recouvrant | Moyenne à forte |
| Mention par un tiers connu | Forte |

Une dé-anonymisation crédible repose sur **plusieurs corrélations** convergentes, idéalement de force variable mais incluant au moins une forte.

> **MIRAGE — Épisode 5 : Identité numérique et pseudonymes**
>
> L'analyste cherche à confirmer si l'username `mdelaunay76` détecté sur Twitter/Instagram/GitHub correspond bien à Marc Delaunay personne civile.
>
> Vérifications cross-comptes :
> - **Twitter @mdelaunay76** : compte verrouillé, créé en 2010. Photo profil : silhouette en costume sombre devant un fond uni. Description : « Finance & Tech enthusiast | Paris ». 87 followers, 312 following.
> - **Instagram mdelaunay76** : compte privé, photo de profil identique (silhouette costume). Bio : « 🌍 Voyages 🏠 Provence ».
> - **GitHub mdelaunay** : compte inactif depuis 2019, deux dépôts personnels (configurations Linux, scripts), email visible dans les commits : `marc.delaunay76@gmail.com`.
>
> Le **GitHub est l'élément déterminant** : les commits sont signés `marc.delaunay76@gmail.com`. Cross-vérification : cet email est-il bien personnel de Delaunay ?
>
> Holehe sur `marc.delaunay76@gmail.com` : présence détectée sur Twitter, Instagram, Pinterest, Spotify, Adobe, Apple. Cohérent avec un email personnel actif. GHunt sur cet email : compte Google actif, photo profil Google identique à celle des autres comptes (silhouette).
>
> Cross-recherche : `marc.delaunay76@gmail.com` apparaît également dans le WHOIS historique (DomainTools) du domaine `delaunay-patrimoine.fr` enregistré en 2017 (depuis abandonné). Ce domaine était une vitrine de conseil patrimonial personnel — cohérent avec un DAF qui aurait, en parallèle de son emploi, une activité personnelle accessoire.
>
> **Conclusion partielle (avec cotation prudente).** L'email `marc.delaunay76@gmail.com` est très probablement l'email personnel de Marc Delaunay (cotation B2 : faisceau d'indices convergents : GitHub + Holehe + WHOIS + cohérence des photos profil et bios).
>
> Implications : ce sélecteur ouvre de nouveaux pivots. Recherche HIBP / DeHashed sur cet email pour identifier exposition dans des stealer logs. Recherche WHOIS et certificats TLS sur tous les domaines potentiellement enregistrés. Ces pistes seront explorées dans MIRAGE 9 et MIRAGE 10.

-----

### Chapitre 29 — Documents, métadonnées et traces indirectes

#### 29.1 Les documents comme sélecteurs

Au-delà des sélecteurs personnels, les **documents publiés** (PDF, Word, Excel, présentations, images) contiennent fréquemment des traces exploitables : métadonnées d'auteur, chemins de fichier, versions, données EXIF. Le « document » devient un sélecteur secondaire majeur.

L'extraction de métadonnées est l'un des classiques de l'OSINT, mature et bien outillée.

#### 29.2 Métadonnées PDF

Un PDF contient typiquement :
- **Auteur** (champ `Author`).
- **Logiciel de création** (`Creator`, `Producer`).
- **Date de création** et **modification**.
- **Titre**, **sujet**, **mots-clés**.
- Parfois : **chemins absolus** (« C:\Users\Marc.Delaunay\Documents\... »).

**Outils.**
- **ExifTool** (Phil Harvey) : standard de fait, CLI, multi-formats.
- **pdfinfo** (Poppler) : Linux/Mac.
- **pdfmetadata online**.
- Adobe Acrobat Pro : interface graphique.

```bash
exiftool document.pdf
# Sortie typique
File Name        : document.pdf
Author           : Marc Delaunay
Creator          : Microsoft® Word 2019
Producer         : Microsoft® Word 2019
Create Date      : 2025:03:14 09:42:18+01:00
Modify Date      : 2025:03:14 09:42:18+01:00
Title            : Rapport préliminaire Delta
```

**Pivot.** L'auteur peut révéler une identité. Le chemin peut révéler une structure d'organisation. La date peut situer un événement.

#### 29.3 Métadonnées Office (Word, Excel, PowerPoint)

Office documents (.docx, .xlsx, .pptx) sont des archives ZIP. À l'intérieur, plusieurs fichiers XML contiennent des métadonnées riches.

**Métadonnées typiques.**
- Auteur (`dc:creator`).
- Dernier modificateur (`cp:lastModifiedBy`).
- Historique de versions.
- Macros (si présentes — attention sécurité).
- Liens externes (images, données).

**Méthode rapide.** Renommer en .zip, extraire `docProps/core.xml` et `docProps/app.xml`.

**Outil dédié.** **oxml** ou simplement `unzip` + lecture XML.

#### 29.4 Métadonnées images : EXIF

Les **métadonnées EXIF** des photos sont l'un des sélecteurs OSINT les plus puissants quand préservées.

**EXIF typique.**
- Modèle d'appareil (iPhone 15 Pro, Canon EOS R5).
- Date et heure de prise.
- **Coordonnées GPS** (latitude, longitude, altitude).
- Paramètres techniques (ouverture, ISO, focale).
- Logiciel de retouche.
- Auteur si renseigné.
- Hash de l'image.

**Outils.**
- **ExifTool** (universel).
- **Jeffrey's Image Metadata Viewer** (en ligne).
- **Metapicz**.

**Pivot.** GPS → géolocalisation précise. Date/heure → chronolocation. Appareil → corrélation cross-photos.

**Limite 2026.** Les plateformes sociales (Facebook, Instagram, Twitter) **suppriment** systématiquement les EXIF sensibles à l'upload. Donc EXIF utile principalement pour :
- Documents PDF/Office (non strippés).
- Photos téléchargées d'un site direct (blog, site institutionnel).
- Fichiers transmis par email.
- Photos issues d'un téléphone et partagées via service brut.

#### 29.5 Stripping EXIF côté investigateur

À l'inverse, l'investigateur doit **stripper systématiquement** les EXIF des captures qu'il transmet (sauf si pertinent pour preuve).

```bash
exiftool -all= image.jpg
# supprime toutes les métadonnées
```

Une capture transmise à un client avec les EXIF de votre téléphone est une fuite OPSEC.

#### 29.6 Chemins absolus et noms de machine

Certains documents PDF/Office contiennent des **chemins absolus** indiquant la machine d'origine.

**Exemples révélateurs.**
- `C:\Users\Marc.Delaunay\Documents\...` → confirme l'auteur Windows.
- `/Users/m.delaunay/Desktop/...` → confirme l'auteur Mac.
- `C:\Users\jdoe\AppData\...\Word\...` → révèle un éventuel ghost writer.
- Path UNC `\\fileserver01\projets\...` → révèle l'infrastructure interne.

Ces traces sont **précieuses** pour confirmer identité, organisation, infrastructure.

#### 29.7 Métadonnées des présentations

Les présentations PowerPoint / Keynote peuvent contenir :
- Auteurs successifs (multiple `lastModifiedBy`).
- Notes de présentateur cachées.
- Images intégrées avec leurs EXIF.
- Liens vers des fichiers externes (révèlent structure).

#### 29.8 Documents publiés en ligne : pivots

Les documents publiés par une organisation (rapports annuels, communiqués, notices techniques) sont riches en métadonnées.

**Méthode MIRAGE.** Télécharger tous les PDFs publics de TechnoVert (rapports, communiqués, notices), extraire les métadonnées en masse :

```bash
exiftool -r *.pdf > metadata.txt
```

Identifier les auteurs récurrents : Marc Delaunay, Sophie Martin (DRH), Pierre Dubois (DG). Cohérence avec les sources publiques.

#### 29.9 Watermarks invisibles et traces

Certaines organisations apposent des **watermarks invisibles** sur leurs documents : identifiant du destinataire, date d'export, etc. Détectables avec outils spécialisés.

**Cas d'usage.** Un leak interne contient un watermark unique → identification du leaker possible (côté défense).

#### 29.10 OCR pour documents scannés

Beaucoup de documents publics sont des PDFs scannés non textualisés (annonces légales anciennes, jugements). L'**OCR** rend exploitable.

**Outils.**
- **Tesseract** (open source).
- **Adobe Acrobat OCR** (commercial).
- **ABBYY FineReader** (commercial, qualité supérieure).
- **OCR.space API**.

**Cas d'usage.** Recherche par mot-clé dans archives BODACC anciennes scannées.

#### 29.11 Synthèse — workflow document

| Étape | Action |
|---|---|
| Collecte | Télécharger document depuis source officielle |
| Hash | SHA-256, consigné dans journal |
| Métadonnées | ExifTool, capture des champs auteur/dates/chemins |
| OCR | Si scanné, textualisation Tesseract |
| Pivot | Auteur, organisation, infrastructure révélée |
| Strip | Si transmission, supprimer EXIF pertinents |

-----

### Chapitre 30 — Reconnaissance faciale et image-to-person

#### 30.1 Une technologie puissante et controversée

La **reconnaissance faciale** est l'une des technologies OSINT les plus puissantes et **les plus encadrées** en 2026. L'AI Act européen restreint son usage privé. Le RGPD la classe comme donnée biométrique sensible. Plusieurs juridictions interdisent ou limitent ses outils commerciaux.

L'analyste OSINT doit maîtriser la technique tout en respectant un cadre légal strict.

#### 30.2 Comment ça fonctionne

La reconnaissance faciale convertit un visage en **vecteur biométrique** (embedding) — une représentation numérique des caractéristiques faciales. Comparer deux visages = comparer leurs vecteurs.

Les outils OSINT de reconnaissance faciale fonctionnent en :
1. Indexant des milliards de photos du web public.
2. Extrayant les vecteurs faciaux.
3. Permettant une recherche : photo query → photos similaires dans l'index.

#### 30.3 PimEyes : le standard controversé

**PimEyes** (pimeyes.com) est l'outil de reconnaissance faciale le plus connu.

**Capacités.**
- Indexation massive du web public.
- Recherche par photo.
- Identification de visages dans des photos, articles, blogs.

**Restrictions.**
- Tarification payante ($14.99-$299/mois).
- AI Act et RGPD : usage restreint en UE.
- PimEyes a introduit un système d'opt-out pour les personnes (à demande).

**Précautions OSINT.**
- Usage strictement professionnel et documenté.
- Base légale RGPD requise (intérêt légitime documenté).
- Pas de recherche « pour curiosité ».
- Documentation des résultats dans le journal.

#### 30.4 FaceCheck.ID et alternatives

**FaceCheck.ID** : outil concurrent, indexation différente. Parfois meilleur pour certaines populations géographiques.

**Search4Faces, FindClone** : moteurs russes, couverture forte pour la CEI.

**Clearview AI** : usage réservé aux LEA, non accessible au privé.

**Yandex Images** : reverse image incluant recherche faciale fonctionnelle (sans biométrie explicite).

**Google Lens** : recherche par image, parfois identifie des personnalités publiques.

#### 30.5 Limites de la reconnaissance faciale

**Faux positifs.**
- Photos à basse qualité ou angle défavorable génèrent des matches fragiles.
- Jumeaux ou ressemblances fortes peuvent confondre.
- Maquillage, vieillissement, lunettes peuvent perturber.

**Faux négatifs.**
- Photos très anciennes peuvent ne pas matcher avec photos récentes.
- Pose extrême peut empêcher reconnaissance.

**Biais.**
- Les modèles sont historiquement moins performants sur certaines populations (visages noirs, asiatiques, féminins) — biais d'entraînement documentés.
- L'analyste doit en tenir compte dans la cotation de ses résultats.

#### 30.6 Méthodologie : règles de prudence

**Règle 1 — Faux positifs.** Un match unique sur PimEyes n'est **jamais** une identification définitive. Cotation maximum « hypothèse à corroborer ».

**Règle 2 — Corroboration multi-sources.** Un match doit être confirmé par cross-recherche (nom retrouvé sur source citée, profil correspondant, etc.).

**Règle 3 — Pas de conclusion « C'est elle/lui ».** Formulation : « la recherche faciale a renvoyé une correspondance avec X, à confirmer par cross-vérification… ».

**Règle 4 — Pas pour identifier des inconnus.** L'usage est pour confirmer/contextualiser une identité **déjà supposée**, pas pour partir de zéro sur un inconnu.

**Règle 5 — Documentation rigoureuse.** Captures de recherche horodatées, hashes, sources.

#### 30.7 Photos générées par IA : nouveau défi

En 2026, les photos générées par IA (StyleGAN, Stable Diffusion, Midjourney, Flux) sont **omniprésentes** sur les réseaux sociaux. Un avatar peut être un visage 100 % synthétique.

**Détection.**
- **Hive Moderation** : score « AI-generated ».
- **Sensity AI** : détection de deepfakes.
- **Optic AI or Not** : interface simple.
- **Intel FakeCatcher** : analyse physiologique.

**Signaux visuels.**
- Asymétries faciales subtiles.
- Pupilles incohérentes (StyleGAN classique).
- Mains, oreilles, dents souvent défectueuses.
- Arrière-plan flou ou incohérent.
- Cheveux qui « fondent » au niveau du contour.

**Implication.** Avant toute recherche faciale, vérifier si la photo source n'est pas synthétique. Une recherche sur une photo IA produit du bruit.

#### 30.8 Image-to-person : workflow complet

Pour identifier une personne à partir d'une photo :

1. **Vérification authenticité.** Hive Moderation, ELA, recherche inversée pour origine.
2. **Recherche inversée multi-moteurs.** Yandex (en priorité), Google Lens, TinEye, Bing Visual.
3. **Recherche faciale dédiée.** PimEyes, FaceCheck (si cadre légal OK).
4. **Cross-recherche des hits.** Vérifier les pages mentionnant la photo : nom, contexte, cohérence.
5. **Corroboration multi-sources.** Pas de conclusion sur un seul hit.
6. **Documentation.** Captures, sources, cotation prudente.

#### 30.9 Limites légales en UE

L'**AI Act** classe la reconnaissance faciale comme **risque élevé** voire **inacceptable** selon usage.

**Inacceptable (interdit).** Identification biométrique en temps réel dans l'espace public (sauf exceptions strictes terrorisme).

**Risque élevé.** Identification biométrique différée. Soumis à conformité stricte.

**Pour OSINT privé.** Zone grise. L'usage de PimEyes pour due diligence est généralement toléré mais doit reposer sur une base légale claire (intérêt légitime documenté).

**Recommandation.** Documenter explicitement dans le SOR la finalité, la base légale, la proportionnalité. En cas de doute, consulter un avocat.

#### 30.10 Synthèse — usage prudent en 2026

| Cas | Recommandation |
|---|---|
| Confirmer une identité déjà supposée | OK avec corroboration |
| Identifier un inconnu à partir d'une photo | À éviter sauf cadre LEA |
| Verification photo profil = vraie personne | OK |
| Recherche dans cadre de stalking suspect | Refus mandat |
| Photo source potentiellement IA | Vérifier authenticité d'abord |
| Documentation | Toujours : capture, source, cotation prudente |

-----

### Chapitre 31 — SOCMINT : méthodologie générale

#### 31.1 Le SOCMINT comme volume principal

Le **SOCMINT** (Social Media Intelligence) est devenu, en volume, l'une des composantes principales de l'OSINT contemporaine. Les personnes publient massivement leur vie en ligne ; les organisations criminelles utilisent les réseaux comme plateformes opérationnelles ; les opérations d'influence s'y déploient ; la fraude s'y prépare.

Mais le SOCMINT est aussi le domaine où les **restrictions 2024-2026** frappent le plus durement (Ch.24). L'analyste doit conjuguer méthodologie rigoureuse et adaptation aux contraintes.

#### 31.2 Cycle SOCMINT

Le cycle SOCMINT spécifique :

1. **Cadrage** : quel objectif sur quelle cible ?
2. **Identification de comptes** : quels comptes appartiennent à la cible ?
3. **Maturation OPSEC** : avatars matures, archivage anticipé.
4. **Collecte** : captures, exports API, scraping résilient.
5. **Analyse de réseau** : qui suit qui, qui parle à qui, clusters.
6. **Analyse temporelle** : cadence, événements, corrélations.
7. **Analyse de contenu** : sujets, narratifs, signaux.
8. **Vérification** : authenticité, attribution.
9. **Cotation et formulation.**

#### 31.3 Identification de comptes

L'identification des comptes appartenant à une cible mobilise :
- Username search (Sherlock, WhatsMyName) — Ch.27.
- Email pivot (Holehe, Epieos) — Ch.27.
- Téléphone pivot (Telegram, WhatsApp).
- Photo pivot (recherche inversée) — Ch.30.
- Recherche presse (mentions de comptes).
- Cross-promotion (un compte mentionne l'autre).
- Mentions par tiers connus.

#### 31.4 Analyse de réseau social

Une fois les comptes identifiés, l'analyse de réseau révèle structures et dynamiques.

**Notions.**
- **Nœud** : compte / personne.
- **Arête** : lien (follow, mention, reply, retweet, like).
- **Degree centrality** : nombre de connexions.
- **Betweenness centrality** : à quel point un nœud relie des sous-graphes.
- **Communautés** : groupes densément connectés (algorithmes Louvain, modularité).
- **Influencers** : nœuds à forte centralité.

**Outils.**
- **Gephi** (open source). Standard académique.
- **Maltego** (commercial). Standard professionnel.
- **NetworkX** (Python). Pour pipelines reproductibles.
- **Cytoscape**.

**Cas d'usage MIRAGE.** Le cluster de 8 faux comptes X coordonnés amplifiant la diffamation contre Berthier sera analysé en graphe : qui retweete qui, quelles sont les communautés, qui est le nœud central.

#### 31.5 Analyse temporelle

**Indicateurs temporels.**
- Cadence de publication (postes / jour, / heure).
- Heures et jours actifs (heatmap).
- Délai de réponse / retweet.
- Synchronisations suspectes (plusieurs comptes publient simultanément).
- Périodes d'inactivité corrélées.

**Outil simple.** Pandas + matplotlib pour visualiser timestamps.

#### 31.6 Analyse de contenu

**Dimensions.**
- **Topics** : sujets récurrents (TF-IDF, topic modeling).
- **Sentiment** : tonalité (positif, négatif, agressif).
- **Langue** : maîtrise et niveau.
- **Style** : voir Ch.28 (stylométrie).
- **Visuels** : images partagées, leur origine, leur authenticité.

**Outils.**
- LLMs (Claude, GPT) pour analyse rapide de corpus (avec vérification).
- **VADER**, **TextBlob** pour analyse de sentiment.
- **BERTopic** pour topic modeling.

#### 31.7 Behavioral fingerprinting

Le **behavioral fingerprinting** combine plusieurs signaux pour caractériser le « comportement » d'un compte.

**Signaux.**
- Cadence (Ch.28).
- Heures d'activité.
- Lexique.
- Émojis.
- Types de contenu (photos perso, retweets, articles).
- Cercle social.
- Sujets.

**Cas d'usage.**
- Distinguer compte humain vs bot.
- Identifier un opérateur unique derrière plusieurs comptes.
- Détecter un changement d'opérateur (compte revendu, compromis).

#### 31.8 Influence et amplification

L'**analyse d'influence** mesure :
- **Reach** : combien de personnes voient les contenus.
- **Engagement** : ratio interactions / followers.
- **Amplification** : qui retweete / partage.
- **Pivots de viralité** : nœuds qui propulsent un contenu.

**Outils.**
- **Brandwatch**, **Talkwalker**, **Meltwater** (commerciaux haut de gamme).
- **NodeXL** (Excel, gratuit).
- Calculs manuels via API ou scraping.

#### 31.9 Détection d'inauthenticité

Le SOCMINT mature consacre une attention spécifique à la **détection des faux comptes et comportements coordonnés** (CIB — Coordinated Inauthentic Behavior). Voir Ch.35.

#### 31.10 Limites du SOCMINT

- **Bulle observable.** On ne voit que ce qui est public. Tout ce qui est privé échappe.
- **Réseaux fragmentés.** Pas une plateforme = une vue complète.
- **Manipulation.** Les comptes peuvent être faux, manipulés, vendus.
- **Inauthenticité industrielle.** Bots, fermes de comptes, IA-generated.
- **Restrictions API.** Volume limité (Ch.24).

> **Principe.** Le SOCMINT révèle une **représentation publique** de la cible, pas sa réalité complète. La cotation doit en tenir compte.

-----

### Chapitre 32 — Plateformes sociales occidentales

#### 32.1 Pourquoi un chapitre par plateforme

Chaque plateforme a sa logique, ses limites, ses sources, ses outils. Une méthodologie générale (Ch.31) ne suffit pas. Maîtriser le SOCMINT implique de connaître plateforme par plateforme.

Ce chapitre couvre les **plateformes occidentales majeures** en 2026. Telegram, Discord, et plateformes alternatives sont traités séparément (Ch.33-34).

#### 32.2 LinkedIn

**Usage OSINT.** Vérification d'identité et de parcours, due diligence, recherche d'experts, cartographie d'organisations.

**Forces.**
- Profils enrichis, généralement véridiques.
- Cartographie d'organisations (qui travaille où).
- Network effects visibles (qui connaît qui).
- Recommandations (signaux qualitatifs).

**Méthode.**
- Recherche directe (compte d'investigation mature).
- **Sales Navigator** pour recherches avancées (filtres profession, école, ancienneté).
- **PhantomBuster** pour automatisation légère (attention CGU et suspension).
- Google `site:linkedin.com/in/` pour recherche externe.
- Bing aussi indexe LinkedIn.

**Limites 2026.**
- Pas d'API publique.
- Détection agressive des bots.
- CGU strictes contre scraping.
- Profils en mode privé non visibles.

**Stratégie.** Compte d'investigation mature, observation discrète, captures Hunchly, pas d'interaction sans nécessité.

#### 32.3 Facebook

**Usage OSINT.** Sphère personnelle, événements, groupes, photos.

**Forces.**
- Volume d'informations personnelles élevé (mais en baisse depuis 2018).
- Groupes thématiques riches.
- Marketplace pour activité commerciale informelle.
- Events.

**Méthode.**
- Recherche directe (compte invest, attention restrictions).
- Recherche par nom + ville / employeur.
- **Sowsearch** (sowsearch.info, en évolution) : Facebook search avec UI dédiée.
- **Meta Content Library** (DSA art. 40) si statut chercheur.
- Search graph (recherche par interactions).

**Limites 2026.**
- Restrictions fortes sur recherches.
- Profils en mode privé très protégés.
- CrowdTangle fermé (cf. Ch.24).
- Photos sans EXIF (stripping à l'upload).

#### 32.4 Instagram

**Usage OSINT.** Visuel, géolocalisation, lifestyle.

**Forces.**
- Photos riches en signaux (lieux, train de vie, cercles).
- Stories (éphémères mais capturables).
- Stories highlights (persistantes).
- Tag de localisation.
- Mentions et tags.

**Méthode.**
- Compte invest (Meta).
- Recherche par hashtag, lieu, mention.
- Suivi de cercles (followings, followers).
- Captures Hunchly pour préserver.
- **InstaLoader** (open source, Python) pour download conforme.

**Limites.**
- Restrictions API.
- Stories disparaissent.
- Comptes privés non visibles aux non-followers.

#### 32.5 X (Twitter)

**Usage OSINT.** Expression publique, débat, breaking news, opérations d'influence.

**Forces.**
- Volume massif d'expressions.
- Plateforme de désinformation et d'influence.
- Métadonnées riches (geo si activé, timing précis).
- Trends en temps réel.

**Méthode 2026.**
- Compte d'investigation pour consultation directe.
- **X API Basic** ($100/mois) pour besoins ciblés.
- **X API Pro** ($5000/mois) pour gros usage.
- Archivage anticipé (Wayback + archive.today).
- Recherche via Google `site:twitter.com` ou `site:x.com`.

**Limites massives.** Voir Ch.24.

#### 32.6 TikTok

**Usage OSINT.** Investigation contemporaine sur publics jeunes, viralité, désinformation visuelle.

**Forces.**
- Volume de vidéos courtes.
- Algorithme révélateur (For You Page).
- Géolocalisation par hashtag et son.

**Méthode.**
- Compte invest.
- **TikTok Research API** (chercheurs académiques EU/US agréés).
- Outils tiers payants (Brandwatch).
- yt-dlp pour téléchargement.

**Limites.**
- API restrictive.
- Pas de timeline historique facile.
- Algorithme opaque.

#### 32.7 YouTube

**Usage OSINT.** Vidéos publiques, chaînes, commentaires, transcripts.

**Forces.**
- Archive vidéo massive.
- Transcripts automatiques (utilisables pour recherche full-text).
- Commentaires (sources d'expression).
- YouTube Data Viewer (Amnesty) pour extraction métadonnées.

**Méthode.**
- **YouTube Data API v3** : gratuit avec quota.
- **yt-dlp** pour download.
- **YouTube Data Viewer** (Amnesty International) pour metadata d'une vidéo.
- Recherche par chaîne, par mot-clé, par date.

**Limites.**
- Suppression possible des vidéos.
- Modération content.
- Limites de quota API.

#### 32.8 Reddit

**Usage OSINT.** Communautés thématiques, discussions, fuites informelles.

**Forces.**
- Communautés riches (subreddits).
- Discussions approfondies.
- Archive historique (avant fermeture Pushshift).

**Méthode 2026.**
- **Reddit API officielle** (payante depuis 2023).
- **undelete.pullpush** (mirror partiel).
- Recherche Google `site:reddit.com`.
- **PRAW** (Python Reddit API Wrapper) avec API officielle.

**Limites.**
- Fermeture Pushshift = perte d'archives historiques.
- API payante.

#### 32.9 Threads

**Usage OSINT.** Émergente, écosystème lié à Instagram.

**Forces.**
- Croissance rapide depuis 2023.
- Authentification via Instagram (cross-plateforme natif).
- Mode public majoritaire.

**Méthode.**
- Compte invest (lié Instagram).
- Pas d'API publique au lancement, en évolution.
- Captures manuelles.

#### 32.10 Bluesky et Mastodon

**Bluesky.** Protocole AT, plus ouvert que X. API publique. Cible des analystes en quête d'alternative à X.

**Mastodon.** Fédéré, protocole ActivityPub. Très ouvert. Outils OSINT en émergence (Magnifying.glass, Garlic.io).

**Méthode.**
- API ouvertes : automatisation possible.
- Captures simples.
- Mais volume encore limité (vs X).

#### 32.11 Synthèse plateformes occidentales

| Plateforme | Difficulté | Outils principaux | Stratégie 2026 |
|---|---|---|---|
| LinkedIn | Très haute | Sales Nav, compte invest | Maturation + Hunchly |
| Facebook | Très haute | Compte invest, MCL | Captures, archivage |
| Instagram | Très haute | Compte invest, InstaLoader | Captures stories urgentes |
| X | Très haute | API payante, compte invest | Archivage anticipé |
| TikTok | Très haute | Research API, compte invest | Captures, outils payants |
| YouTube | Moyenne | API, yt-dlp | Volume gérable |
| Reddit | Haute | API payante, Google site: | Reconstruction historique limitée |
| Threads | Faible-moyenne | Compte invest | Émergent |
| Bluesky | Faible | API ouverte | Confortable |
| Mastodon | Faible | API ActivityPub | Très ouvert |

> **MIRAGE — Épisode 6 : SOCMINT multi-plateformes**
>
> L'analyste mène la cartographie SOCMINT autour de Delaunay.
>
> **LinkedIn** : profil professionnel accessible via Camille Roux (avatar du cabinet). Parcours confirmé, 487 contacts, 23 recommandations, 4 posts publiés sur 5 ans (sobre, surtout repartages presse industrielle). Pas d'élément critique. Capture Hunchly.
>
> **Facebook** : un compte au nom de Marc Delaunay, photo de profil correspondante, mode privé. Aucun contenu public visible. Liste d'amis non accessible. Note dans la fiche.
>
> **Instagram** (sous username `mdelaunay76`) : compte privé, photo silhouette. Aucune story / post public. Pas exploitable directement.
>
> **X / Twitter** (`@mdelaunay76`) : compte verrouillé. Quelques retweets publics datant de 2014-2017 (sport, finance). Aucun contenu récent visible. Faible.
>
> **TikTok** : aucun compte identifié.
>
> **YouTube** : la vidéo interview 2023 (TechnoVert) est confirmée. Pas d'autres apparitions de Delaunay.
>
> **Reddit** : recherche `mdelaunay76` ne retourne aucun compte significatif.
>
> **Bluesky, Mastodon** : absence.
>
> **Conclusion SOCMINT** : Delaunay a une faible empreinte volontaire sur les réseaux sociaux. Stratégie OPSEC personnelle robuste. Les pivots SOCMINT sont limités pour Delaunay personnellement.
>
> **Bascule sur le volet désinformation** : le cluster des faux comptes amplifiant la diffamation contre Berthier sera l'objet du gros du SOCMINT. La recherche s'oriente vers l'identification de ces comptes, leur activité, leurs liens — sujet qui sera développé en MIRAGE 17 (Ch.76 désinformation).

-----

### Chapitre 33 — Telegram

#### 33.1 L'écosystème Telegram

**Telegram** (créé 2013 par les frères Durov) est devenu en 2024-2026 l'une des plateformes centrales pour OSINT, criminalité organisée, désinformation, et activités politiques.

**Caractéristiques.**
- Application chiffrée (E2EE pour secrets chats, non-E2EE pour conversations normales).
- Channels (broadcast unidirectionnel, jusqu'à millions d'abonnés).
- Groupes (conversations multi-utilisateurs, jusqu'à 200 000 membres).
- Bots (interfaces programmables).
- Stickers, médias.
- Mode anonyme (numéro caché, username affiché).

**Volume.** 900 millions d'utilisateurs en 2024. Géographie : forte présence Russie/CEI, Iran, Inde, Indonésie, Europe de l'Est. Croissance rapide en Occident.

#### 33.2 Évolution post-arrestation Durov 2024

L'arrestation de **Pavel Durov en France (août 2024)** par les autorités françaises (mise en examen pour complicité de complicité de crimes graves via la plateforme) a déclenché des évolutions :
- Coopération renforcée avec LEA (notamment françaises).
- Partage d'IP et numéros pour réquisitions pénales graves.
- Modération renforcée (CSAM, terrorisme).
- Mais cœur business (channels, bots, anonymat raisonnable) maintenu.

**Implication.** Telegram en 2026 reste accessible mais avec coopération LEA accrue. Pour OSINT privé, les méthodes restent identiques.

#### 33.3 Canaux publics : exploitation

Les **canaux publics** sont consultables sans connexion sur web (`t.me/nom_du_canal`).

**Sources OSINT.**
- **Telegago** (telegago.fr) : moteur de recherche Telegram public.
- **TGStat** (tgstat.com) : statistiques canaux publics.
- **Telemetr.io** : analyse de croissance.
- **Lyzem** : recherche dans messages historiques.
- **Combot** : statistiques de groupes.

**Méthode.**
- Recherche par mot-clé sur Telegago.
- Identification canaux suspects.
- Préservation : captures + export JSON via Telegram Desktop.

#### 33.4 Groupes et observation passive

Les **groupes** nécessitent invitation ou lien public.

**Méthode.**
- Compte d'investigation Telegram (numéro dédié).
- Joindre les groupes via lien public.
- Observation passive (pas d'interaction).
- Export régulier des messages (Telegram Desktop → Export chat history → JSON).

**OPSEC.**
- Numéro d'investigation séparé physiquement.
- Mode anonyme activé (username affiché, numéro masqué aux autres).
- Pas de photo profil identifiable.

#### 33.5 Bots Telegram

Les **bots** sont des comptes programmables. Pour OSINT :

**Bots utiles.**
- **@quotly_bot** : capture jolie de messages (preuves).
- **@combot** : stats de groupe.
- Bots d'archive : différents selon usage.

**Précaution.** Bots tiers voient ce que vous voyez. OPSEC : compte invest pour interactions bots.

#### 33.6 Pivots Telegram → autres plateformes

**Username Telegram** est souvent unique → pivot Sherlock vers autres plateformes.

**Numéro** : si visible (souvent caché), pivot Truecaller, WhatsApp.

**Photo profil** : recherche inversée.

**Liens partagés** : révèlent infrastructure (domaines, autres canaux, sites externes).

**Cross-promotions** : un canal mentionne un autre = lien d'écosystème.

#### 33.7 Cas d'usage criminels (compréhension, pas exploitation)

Telegram est utilisé pour :
- Marketplaces criminelles (vente fraudes, drogues, données).
- Recrutement (mules, hackers, terroristes).
- Diffusion de leaks et stealer logs.
- Coordination d'opérations cyber.
- Désinformation et trolling.

**Approche OSINT.**
- **Consultation** des canaux ouverts = légale.
- **Joindre** un groupe = à évaluer selon contenu (CSAM, terrorisme = refus immédiat).
- **Interaction / achat** = sortie du périmètre OSINT pur, réservé LEA.
- **Signalement** à Pharos / autorités si contenu illégal.

#### 33.8 Stealer logs sur Telegram

Une part majeure du marché stealer logs (Ch.43) se déploie sur Telegram (canaux de vente, dropbox de logs).

**Approche.**
- Observation possible (cadre légal documenté).
- Pas d'achat (zone pénale).
- Documentation pour orientation enquête.

#### 33.9 Méthodologie d'enquête Telegram

1. **Cartographie** : identifier les canaux/groupes pertinents (Telegago, recherche directe).
2. **Joindre** (compte invest) les groupes publics légaux.
3. **Préservation** : exports JSON réguliers.
4. **Analyse** : extraction d'entités, sélecteurs.
5. **Pivots** : usernames, numéros, liens externes.
6. **Documentation** : journal d'enquête détaillé.

#### 33.10 Limites

- Channels privés / payants inaccessibles.
- Chiffrement E2EE des secrets chats.
- Bots avec accès limité.
- Évolution rapide post-Durov.

> **MIRAGE — Épisode 7 : Telegram, forums et communautés**
>
> L'analyste explore Telegram pour identifier la coordination du cluster de désinformation.
>
> **Recherche Telegago** sur termes liés à TechnoVert, Berthier, Delaunay : aucun canal public significatif détecté avec ces termes en français.
>
> **Hypothèse étendue** : la coordination peut se faire dans un canal privé ou dans un groupe spécialisé en services de désinformation à louer.
>
> **Recherche par sujets connexes** : canaux d'achat-vente de comptes X / bot networks. Identification de 12 canaux/groupes Telegram proposant ce type de service en français. Observation passive via compte d'investigation Telegram (numéro dédié, mode anonyme).
>
> **Découverte significative** : un canal `@socialmedia_boost_fr` (15 000 abonnés) propose explicitement « campagnes coordonnées 8-20 comptes, narratif fourni, plateforme X et Telegram, livré sous 72h ». Tarif affiché : 1500-3500 € par campagne selon volume.
>
> **Vérification** : ce canal est-il actif sur la période suspecte (octobre 2025 à mai 2026) ? Examen des messages publics : oui, plusieurs « livraisons » mentionnées sur la période, avec captures de comptes X qui ont depuis été suspendus. Aucune mention explicite de TechnoVert ou Berthier (les clients sont anonymisés dans les communications publiques).
>
> **Note** : ce canal est une piste forte pour l'attribution de la campagne. Cotation B2. Approfondissement à venir (cross-référencement avec les comptes coordonnés effectifs, pivot infrastructure).
>
> **Sur le volet stealer logs** : recherche dans les canaux Telegram de vente de stealer logs (8 canaux principaux identifiés). Filtre par domaine `@gmail.com` avec `delaunay76` : un hit dans un dump de janvier 2026 publié sur canal `@cloudsec_dumps`. Capture (en mode lecture seule, sans téléchargement) : 47 credentials associés à l'email `marc.delaunay76@gmail.com`, dont des entrées Binance, ProtonMail, plusieurs sites e-commerce. **Pivot crypto majeur** : compte Binance identifié → renvoi à MIRAGE 14.

-----

### Chapitre 34 — Discord, forums et plateformes alternatives

#### 34.1 Discord : la plateforme dominante 2026

**Discord** (lancé 2015, orienté gaming initialement) est devenu en 2026 l'une des plateformes principales pour communautés thématiques, projets crypto, criminalité organisée, désinformation politique.

**Caractéristiques.**
- Serveurs (équivalents groupes Slack/Telegram, structure en channels).
- Channels (text, vocal, vidéo).
- Voix permanentes (audio chat continu).
- Rôles et hiérarchies internes.
- Bots programmables très puissants.
- Stages, événements live.

**Volume.** 200+ millions d'utilisateurs mensuels.

#### 34.2 Restrictions et accès Discord

**Limites OSINT.**
- Pas d'API publique pour observation tiers (uniquement bots dans serveurs où on est admis).
- Recherche cross-serveur impossible.
- CGU strictes contre observation.
- Modération réactive (suppression de comptes suspects).

**Stratégie.**
- Compte d'investigation Discord mature.
- Adhésion aux serveurs publics ou via invitations.
- Observation passive, pas d'interaction sauf nécessité.
- Capture systématique.

#### 34.3 Méthodes de capture Discord

**DiscordChatExporter** (Tyrrrz, GitHub) : outil open source qui exporte les channels d'un serveur dont vous êtes membre. Export en HTML, JSON, CSV, TXT.

**Usage.** Compte invest membre → export → archivage local. Respecter les CGU est tendu (export massif peut violer CGU).

**Captures manuelles.** Screenshots horodatés + hash. Méthode forensique stricte.

**Bots de logging.** Pour serveurs où on a droits admin (consentement explicite).

#### 34.4 Pivots Discord

- **Username Discord** → pivot Sherlock multi-plateformes (souvent réutilisé).
- **Avatar** → recherche inversée.
- **Servers communs** révèlent intérêts, milieux.
- **Mentions** révèlent réseau.

#### 34.5 4chan, 8kun et l'imageboard underground

**4chan** (créé 2003) et son fork **8kun** (anciennement 8chan) sont des imageboards anonymes, sources majeures de :
- Génération de mèmes politiques.
- Désinformation et harcèlement coordonné.
- Communautés extrémistes.
- Subcultures internet.

**Méthodologie.**
- Consultation prudente (contenu potentiellement traumatique, dont CSAM épisodique sur certaines boards — refus immédiat de consultation, signalement).
- Outils : **4plebs** (archive 4chan), **archive.4plebs.org**.
- Pas d'interaction.

**OPSEC.** Tor recommandé.

#### 34.6 Forums clandestins de surface

Au-delà de 4chan, plusieurs forums hostent des activités borderline ou criminelles.

**Exemples (compréhension, pas accès).**
- **BreachForums** et ses successeurs (vente de leaks).
- **RaidForums** (historique, fermé par LEA 2022).
- **XSS, Exploit** (forums russophones cybercriminels).
- **Dread** (forum dark web, accessible via Tor).

**Approche OSINT.**
- Forums **de surface** : consultation possible, OPSEC stricte.
- Forums **dark web** : voir Ch.44 (panorama) et Dark Web vFULL pour profondeur.

#### 34.7 VKontakte (VK)

**VK** (vk.com) est le « Facebook russe », dominant en CEI.

**Usage OSINT.**
- Investigation sur cibles russophones.
- Recherche d'identités, photos, groupes.
- API plus ouverte que Facebook (mais évolutive).

**Outils.** Search engines russes, scripts VK API, **220vk** (outil OSINT VK dédié).

**OPSEC.** Service russe, requêtes loguées potentiellement. VPN.

#### 34.8 OK.ru (Odnoklassniki)

**OK.ru** : « Copains d'avant russe », orienté plus 30+ ans, fortement utilisé CEI.

**Usage OSINT.**
- Investigation cibles slaves, anciennes générations.
- Photos de famille, événements.
- Souvent moins protégé que VK ou Facebook.

#### 34.9 Plateformes asiatiques

**Weibo** (Chine) : Twitter chinois. Très utilisé. Censure forte.

**Baidu Tieba** (Chine) : forums Baidu.

**KakaoTalk** (Corée).

**Line** (Japon, Asie du Sud-Est).

**Naver Cafe** (Corée) : forums.

Spécificités OSINT : langues locales (besoin traduction), restrictions politiques (Chine), faible présence outils OSINT internationaux.

#### 34.10 Autres plateformes émergentes

**Session.** Successeur Signal anonyme. Pas de numéro de téléphone requis. Utilisé dans certaines communautés cybercriminelles.

**Signal usage public.** Channels et groupes Signal publics émergent. Limité par design.

**SimpleX.** Application chiffrée sans identifiant utilisateur. Émergente.

**Matrix / Element.** Federated. Pour communautés tech et activistes.

#### 34.11 Synthèse — plateformes alternatives

| Plateforme | Région / usage | Accessibilité OSINT |
|---|---|---|
| Discord | Mondial, communautés | Compte invest, observation passive |
| 4chan / 8kun | Mondial anonyme | Consultation prudente, outils archive |
| Forums clandestins surface | Mondial | OPSEC stricte, observation |
| VK / OK.ru | CEI | Compte invest, VPN |
| Weibo / Tieba | Chine | Compte invest, traduction, VPN |
| Session / SimpleX | Anonymat fort | Limité |
| Matrix | Tech/activistes | API ouverte |

-----

### Chapitre 35 — Faux comptes, bots et comportements coordonnés

#### 35.1 L'industrialisation de l'inauthenticité

L'inauthenticité numérique s'est industrialisée. Bots, fermes de comptes, IA-generated content, services de désinformation à louer composent un marché mature. L'analyste OSINT doit savoir détecter ces phénomènes, parce qu'ils :
- Polluent l'enquête (faux signaux).
- Constituent eux-mêmes l'objet d'enquête (campagnes d'influence).
- Manipulent l'écosystème observable.

#### 35.2 Typologies d'inauthenticité

**Astroturfing.** Création de l'illusion d'un soutien populaire via faux comptes coordonnés.

**Bots automatiques.** Programmes qui publient/interagissent sans humain.

**Cyborgs.** Humains qui pilotent plusieurs comptes en parallèle, parfois avec assistance bot.

**Trolling coordonné.** Groupes humains qui attaquent une cible.

**Sock puppets.** Comptes opérés par un individu pour plusieurs identités (Ch.11 — cadre légitime ou frauduleux selon usage).

**Fermes de comptes.** Industries (Macédoine, Indonésie, Russie) qui créent et opèrent des milliers de faux comptes.

**Coordinated Inauthentic Behavior (CIB).** Terme Meta. Activités coordonnées simulant des opinions ou réactions organiques. Concept central.

#### 35.3 Signaux de bot automatique

- Cadence anormale (poste toutes les 15 secondes).
- Activité 24/7 sans pauses humaines.
- Volume disproportionné (1000 posts/jour).
- Contenus dupliqués ou paraphrasés.
- Pas de variation contextuelle.
- Réponses inappropriées (cohérence syntaxique mais sémantique faible).

#### 35.4 Signaux de ferme de comptes

- Comptes créés en lot (timestamps de création groupés).
- Photos de profil :
  - Recyclées (recherche inversée renvoie autres comptes).
  - Volées de banques d'images.
  - **Générées par IA** (signal 2026 majeur).
- Bios génériques ou absentes.
- Followings disproportionnés (50 000 follow, 200 follower).
- Activité corrélée temporellement.

#### 35.5 Signaux de Coordinated Inauthentic Behavior (CIB)

Le **CIB** combine plusieurs signaux indiquant qu'une activité apparemment organique est en fait coordonnée.

**Indicateurs.**
- **Coordination temporelle** : posts simultanés ou en cluster temporel.
- **Coordination de contenu** : narratif identique ou paraphrasé.
- **Coordination de hashtags** : usage synchronisé de hashtags spécifiques.
- **Réseau d'amplification** : retweets/likes mutuels formant clusters.
- **Origine technique commune** : VPN, infrastructure partagée.

**Outils.**
- **Hamilton 2.0** (Alliance for Securing Democracy) : monitoring Russie/Chine.
- **Information Laundromat** (Stanford Internet Observatory).
- Graphes Gephi avec algorithmes communautés.

#### 35.6 Détection des photos IA (signal 2026 majeur)

Une part croissante des faux comptes utilise des photos générées par IA.

**Détection.**
- **Hive Moderation** : score AI-generated.
- **Optic AI or Not** : interface simple.
- **Sensity AI** : détection deepfakes.
- Inspection visuelle (anomalies mains, dents, asymétries).

**Implication.** Vérifier systématiquement les photos de profil suspects.

#### 35.7 Méthodologie de détection de cluster

Pour une enquête sur un cluster de comptes suspects :

1. **Listing initial** : identifier 5-30 comptes suspects (cible affirmée + ramifications via mentions/retweets).
2. **Analyse de profil** : date création, follower count, ratio, photo profil (IA ?), bio.
3. **Analyse temporelle** : timestamps de posts, heatmaps.
4. **Analyse de contenu** : narratifs, mots-clés, hashtags.
5. **Analyse de réseau** : graphe d'interactions, communautés (Gephi).
6. **Signatures techniques** : si accès (peu probable hors LEA) : IPs, user-agents.
7. **Synthèse** : ces comptes sont-ils coordonnés ? Probabilité ? Attribution probable ?

#### 35.8 Attribution prudente

L'**attribution** d'une campagne CIB à un acteur est délicate.

**Niveaux d'attribution.**
- **Origine probable** (analyse linguistique, fuseaux horaires, narratifs idéologiques).
- **Infrastructure technique** (IPs, domaines, hostings).
- **Mode opératoire** (TTP comparables à campagnes connues).
- **Aveu** ou **leak** (rare).

L'attribution étatique (« cette campagne est russe / chinoise ») demande des éléments solides. Sans eux, formuler : « narratifs et patterns compatibles avec des opérations d'influence pro-X », pas « campagne menée par les services X ».

#### 35.9 Cas de référence

**Internet Research Agency (IRA, Russie).** Ferme de trolls Saint-Pétersbourg. Active 2014-2024. Documentée par Stanford, Mueller Report, Graphika.

**Doppelgänger (Russie).** Campagne de faux médias imitant Le Monde, Bild, etc., diffusée via X et Telegram. Documentée par VIGINUM (rapport 2024).

**Spamouflage (Chine).** Campagnes pro-PRC sur X, YouTube, Facebook. Volume massif. Documentée par Graphika.

**Indian Chronicles (EU DisinfoLab, 2019-2020).** 750+ faux médias en 116 pays orchestrés depuis l'Inde.

#### 35.10 Cadre légal et institutionnel France

**VIGINUM** (SGDSN) est l'acteur français de référence sur la détection et caractérisation des « phénomènes inauthentiques ». Le **DSA** européen impose des obligations aux plateformes (rapports, accès chercheurs).

#### 35.11 Synthèse — boîte à outils détection CIB

| Outil | Usage |
|---|---|
| Gephi + algorithmes communautés | Analyse de réseau |
| Hamilton 2.0 | Monitoring Russie/Chine |
| Hive Moderation | Détection photos IA |
| Sensity AI | Détection deepfakes |
| Information Laundromat | Cross-référencement narratifs |
| EU DisinfoLab méthodologie | Cas studies de référence |
| Maltego | Pivots multi-plateformes |
| API X/Bluesky/Mastodon | Collection de données |
| LLMs (avec validation) | Analyse de patterns linguistiques |

L'expertise CIB est devenue une spécialité OSINT en soi. Pour les cas avancés (campagnes étatiques massives), partenariat avec acteurs spécialisés (Bellingcat, EU DisinfoLab, Graphika) ou agences (VIGINUM).

-----
