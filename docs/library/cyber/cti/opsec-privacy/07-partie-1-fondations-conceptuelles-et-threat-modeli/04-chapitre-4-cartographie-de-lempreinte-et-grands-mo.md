---
title: Chapitre 4 — Cartographie de l’empreinte et grands modèles d’exposition
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 1 — Fondations conceptuelles et threat modeling
  - index.md
---

L’objectif de ce chapitre est de produire une cartographie systématique de ce qui, depuis toi, s’échappe vers le monde extérieur. Sans cette cartographie, toute mesure défensive est aveugle.

## 4.1 Empreinte volontaire, involontaire et héritée

L’**empreinte volontaire** est ce que tu publies consciemment : posts, photos, opinions, profil professionnel, contributions GitHub, articles. Elle est, en théorie, sous ton contrôle. En pratique, sa permanence (Wayback Machine, archives, captures) la rend irréversible.

L’**empreinte involontaire** est ce qui fuit sans intention : métadonnées de fichiers, géolocalisation de photos, fingerprints navigateur, requêtes DNS, données vendues par des applications.

L’**empreinte héritée** est ce que d’autres exposent sur toi : photos taguées par des amis, mentions dans des publications, témoignages, registres publics, données vendues par des courtiers qui t’ont profilé sans ton accord.

Les trois s’accumulent. Et seule la première est en théorie sous ton contrôle.

## 4.2 Exposition par les comptes

L’email principal est le **centre de gravité** de l’identité numérique. Il est utilisé pour récupérer les mots de passe de la plupart des autres comptes. Sa compromission donne accès à la quasi-totalité de la vie numérique. Inversement, sa perte (faille, oubli, suspension par le fournisseur) cascade en perte massive.

L’audit des comptes consiste à dresser la liste de tous les services où tu as un compte. La plupart des gens, à cet exercice, en découvrent entre 100 et 500. Outils utiles : recherche dans les emails reçus (« welcome », « confirm your email »), historique de gestionnaire de mots de passe, vérification HaveIBeenPwned avec ton email principal.

Pour chaque compte critique, note : email associé, MFA activé ou non, type de MFA, dernière connexion, mot de passe unique ou non, données stockées.

## 4.3 Exposition par les appareils

Chaque appareil collecte et transmet :

- Identifiants matériels : adresse MAC (Wi-Fi, Bluetooth), IMEI pour les téléphones, numéros de série, identifiants TPM, identifiants publicitaires (Advertising ID Android, IDFA iOS — désactivables).
- Capteurs : GPS, accéléromètre (qui révèle des modes de transport, des activités physiques), microphone, caméra.
- Connectivité : Wi-Fi probing (le téléphone qui hurle les noms des réseaux passés), Bluetooth/BLE beacons.
- Logiciels installés : chaque application installe son SDK, qui collecte typiquement plus que ce que l’application semble faire.

## 4.4 Exposition par les applications

Les applications mobiles sont des vecteurs sous-estimés. Une appli météo typique demande accès à la localisation précise (raisonnable), au stockage (douteux), aux contacts (suspect), à l’identifiant publicitaire (mauvais signe). Beaucoup d’applis intègrent 5 à 30 SDK tiers, chacun avec ses propres flux de données.

**Test pratique** : sur ton téléphone, ouvre les paramètres → confidentialité → audit des permissions. Combien d’applis ont accès à ta localisation en arrière-plan ? À tes contacts ? À ton micro ? Réponse moyenne : beaucoup trop.

## 4.5 Exposition par le réseau

Chaque connexion réseau révèle :

- **IP source** : identifie ton FAI et ta localisation grossière (souvent ville).
- **Requête DNS** : révèle les noms de domaine que tu consultes (sauf DoH/DoT — Ch 19).
- **SNI** (Server Name Indication) : révèle l’hôte que tu joins, même en HTTPS (sauf ECH — Ch 19).
- **Métadonnées TLS** : horodatages, suites cryptographiques, taille des échanges.
- **Wi-Fi et Bluetooth** : émissions radio en clair de probes et de beacons.

Le FAI voit *tout* ce qui passe par sa box (sauf si VPN). Les opérateurs cellulaires aussi. Les exploitants de Wi-Fi public également.

## 4.6 Exposition par le cloud

La synchronisation automatique est la fuite cloud la plus massive. Les photos iCloud/Google Photos s’uploadent automatiquement avec leurs métadonnées EXIF (Ch 31). Les contacts iCloud/Google synchronisent ton carnet d’adresses chez Apple/Google. Les sauvegardes WhatsApp dans iCloud/Google Drive ne sont pas chiffrées de bout en bout par défaut (et le sont seulement si activées explicitement).

Quand Apple Advanced Data Protection (ADP) est activée, une partie significative des données iCloud devient chiffrée de bout en bout (photos, sauvegardes iCloud, notes, rappels, signets Safari, etc.). Mais : les contacts, le calendrier, et les mails iCloud restent accessibles à Apple pour des raisons d’interopérabilité (Ch 14 et 30).

## 4.7 Exposition par les métadonnées

Les métadonnées sont le gisement le plus sous-estimé. À traiter en profondeur au Ch 31, mais à mentionner ici :

- **EXIF photo** : coordonnées GPS, modèle d’appareil, numéro de série, horodatage, profil ICC personnalisé qui peut identifier l’écran de prise de vue ou de retouche.
- **PDF** : auteur, logiciel de création, historique de révisions, objets cachés, signatures invisibles.
- **Office (DOCX/XLSX/PPTX)** : auteur, commentaires, suivi des modifications activé sans en avoir conscience.
- **Audio/vidéo** : tags, codecs, traces de montage, voire artefacts d’enregistrement (gyroscope révélant le modèle exact d’iPhone).

## 4.8 Exposition par l’entourage

Le graphe social est un identifiant en soi. Deux personnes ayant 15 contacts en commun sont probablement reliées d’une façon ou d’une autre. Les plateformes (Facebook, LinkedIn, Instagram, Snapchat) construisent ces graphes en permanence. Le « people you may know » est l’application directe de cette analyse.

Tes proches publient à ton sujet sans en mesurer l’impact : photo de famille géolocalisée, mention de ton lieu de travail dans un post de félicitations professionnelles, lien social public sur Facebook.

## 4.9 Exposition par les habitudes

L’analyse comportementale identifie des motifs : tu te connectes à Tor tous les jeudis à 22h ; tu écris en moyenne 60 mots par minute avec un certain rythme ; tu utilises certaines tournures (cf. stylométrie, Ch 35) ; tu consultes certains sites à certaines heures. Pris isolément, chaque indicateur est insignifiant. Agrégés, ils forment une signature.

**Conséquence opérationnelle** : si tu ouvres un nouveau pseudonyme et que tu le pratiques avec les mêmes habitudes que ton identité connue, le pseudonyme se corrélera à terme.

## 4.10 Exposition par les fuites

HaveIBeenPwned recense, en 2025-2026, plus de 13 milliards de credentials exposées issues de fuites passées. Si tu utilises internet depuis plus de cinq ans, ton email principal a presque certainement été inclus dans au moins une fuite. Le contenu varie : email + mot de passe (le plus courant), email + numéro de téléphone, profil complet (LinkedIn 2021), informations bancaires (rares mais existantes).

Ces fuites alimentent :

- Le *credential stuffing* : tentative automatisée de réutilisation des mots de passe fuités sur d’autres services. Première cause de compromission de comptes pour la majorité des utilisateurs.
- L’OSINT : un attaquant peut croiser ton email avec une fuite pour obtenir d’autres infos (numéro de téléphone, anciens mots de passe pouvant révéler des motifs).
- Le *doxxing* : agrégation pour produire un dossier ciblé.

## 4.11 Méthode d’audit personnel en 10 étapes

À faire une première fois sérieusement, puis à répéter tous les six mois.

1. **Lister ses comptes** : recherche dans email principal des termes “welcome”, “verify your email”, “confirm”. Compléter avec le gestionnaire de mots de passe.
1. **Tester son email principal sur HaveIBeenPwned** : noter les fuites confirmées.
1. **Audit des permissions mobiles** : sur iOS Réglages → Confidentialité ; sur Android Paramètres → Confidentialité → Gestionnaire d’autorisations.
1. **Recherche de son nom et email** sur les moteurs (Google, Bing, DuckDuckGo) — sans être connecté, sur navigateur privé.
1. **Reverse image search** sur ses photos publiques (Yandex Images, PimEyes, Google Lens).
1. **Audit des réseaux sociaux** : qui peut voir quoi, qui sont mes amis, qu’ai-je publié au cours de la dernière année, mes photos sont-elles taguées ?
1. **Audit des sessions actives** sur Google, Apple, Microsoft, Facebook : appareils connectés, dernière activité, sessions à révoquer.
1. **Audit du gestionnaire de mots de passe** : mots de passe réutilisés, mots de passe faibles, comptes sans MFA.
1. **Audit cloud** : que synchronise mon téléphone ? Mon ordinateur ? Ai-je activé ADP (Apple) ou équivalent ?
1. **Recherche de soi sur data brokers** : Spokeo, BeenVerified, Whitepages, Pages Jaunes (FR), Société.com.

À l’issue de cet audit, tu auras une carte. Le reste du cours t’apprendra à la réduire.

## 4.12 *Fil rouge* — Audit complet de Léa

Léa fait l’exercice. Ses résultats, en synthèse :

**Top 20 des fuites identifiées** :

1. Email professionnel dans 7 fuites HaveIBeenPwned (dont LinkedIn 2021 et Adobe 2013).
1. Numéro de téléphone trouvable sur LinkedIn (paramètre par défaut).
1. Adresse postale visible via une ancienne souscription à une association (avant RGPD).
1. Date d’anniversaire publique sur Facebook (paramètre par défaut).
1. Nom de jeune fille de sa mère trouvable via un faire-part de mariage scanné en ligne.
1. Photos d’enfance avec géolocalisation EXIF intacte sur Flickr (compte oublié de 2010).
1. Adresse email principale utilisée pour 200+ services (centre de gravité absolu).
1. Aucun MFA sur Gmail (récupération par SMS uniquement).
1. iCloud sans ADP activée.
1. WhatsApp synchronisé dans iCloud, sauvegardes non chiffrées par défaut.
1. Carnet d’adresses iCloud → contient les numéros de plusieurs sources potentielles.
1. Compte Twitter/X avec géotag occasionnel activé.
1. Account-pivoted via PimEyes : photos professionnelles publiques permettent reverse image vers comptes personnels.
1. Identifiants publicitaires actifs sur téléphone (IDFA + Android ID secondaire).
1. Réutilisation d’un même pseudo « LeaM » sur trois forums professionnels, dont un lié à son identité civile.
1. Présence Strava active avec parcours de course incluant son domicile et son bureau.
1. GitHub avec son nom civil et email pro, contributions horodatées révélant son rythme de travail.
1. Mailing-list professionnelle archivée publiquement avec ses anciennes adresses.
1. Photos taguées par son frère sur Instagram révèlent vacances, famille, lieux fréquentés.
1. Adresse postale et téléphone fixe dans le registre du commerce belge (entreprise individuelle).

**Décision** : avant tout outil de chiffrement, Léa décide de consacrer deux week-ends à réduire cette empreinte. Le reste du cours l’accompagne dans cette démarche.

> 🟩 **À retenir du chapitre 4**
> 
> - L’empreinte numérique a trois dimensions : volontaire, involontaire, héritée.
> - Neuf vecteurs d’exposition à auditer systématiquement.
> - L’audit personnel en 10 étapes est le préalable à toute action de durcissement.
> - L’email principal est le centre de gravité : sa protection prime sur tout.
> - Beaucoup de gens découvrent à l’audit que leurs « gros risques perçus » sont moins critiques que des fuites banales déjà acquises.

-----
