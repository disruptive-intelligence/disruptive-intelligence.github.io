---
title: Chapitre 33 — Données de santé numériques
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VI — VIE privée, images, documents et surexposition
  - index.md
---

*Les données de santé sont une catégorie particulièrement sensible — elles touchent à l'intime, peuvent affecter l'assurabilité, et l'usurpation médicale (utilisation des droits Sécu de quelqu'un d'autre) est un délit en croissance.*

Les **comptes santé numériques** :

**Doctolib / Maiia / Qare / autres** : prises de rendez-vous, téléconsultations, accès parfois aux comptes-rendus. Données stockées : motifs de consultation, historique de rendez-vous, parfois ordonnances et résultats. Sécurisation : mot de passe unique, MFA si proposé, vigilance phishing (« votre rendez-vous est confirmé, accédez à votre dossier »).

**Mon espace santé** (dossier médical national, lancé en 2022) : carnet de santé numérique, ordonnances, comptes-rendus d'hospitalisation, résultats d'analyses. Accès via FranceConnect — donc la sécurité de Mon espace santé dépend de la sécurité du compte pivot FranceConnect (cf. Ch.32). À sécuriser comme un compte critique.

**Espaces des mutuelles** : remboursements complémentaires, contrats, déclarations. Données financières + données de santé combinées.

**Apps de santé connectée** : Apple Santé, Samsung Health, Fitbit, Garmin, Withings, MyFitnessPal, Strava (course/vélo), Clue / Flo (cycles menstruels), Ouvre les données nutritionnelles ou médicales à des tiers selon les paramétrages — ces apps collectent des volumes considérables de données comportementales et physiologiques, parfois revendues à des courtiers de données.

Les **risques spécifiques** :

L'**usurpation médicale** : un attaquant utilise les droits Sécu de la victime pour se faire soigner ou obtenir des médicaments (notamment des médicaments détournés à la revente — opiacés, anxiolytiques). La victime découvre des consultations, ordonnances ou actes qu'elle n'a pas effectués sur son relevé Ameli. C'est aussi un risque d'antécédents médicaux faussés dans son dossier.

La **fuite de données médicales** : les hôpitaux et établissements de santé ont été ciblés massivement par des ransomwares en 2023-2026. Quand ces incidents touchent des serveurs contenant des dossiers patients, les données peuvent fuiter sur internet. Le particulier n'y peut pas grand-chose côté prévention, mais doit être attentif aux notifications de fuite et aux phishings ciblés qui s'ensuivent.

Les **photos d'analyses, ordonnances, comptes-rendus envoyées par messagerie** : un classique. Une analyse de sang envoyée à un proche par WhatsApp, une ordonnance photographiée et envoyée par SMS pour le pharmacien, un compte-rendu d'imagerie envoyé par email — ce sont des données sensibles qui sortent du circuit santé sécurisé. Le réflexe : utiliser Mon espace santé (qui permet le partage entre professionnels et patient), Doctolib (messagerie sécurisée avec le médecin), ou un canal chiffré (Signal) si nécessaire.

Les **applis grand public** posent une question de **politique de données** : qui est l'éditeur, où sont stockées les données (Europe ou hors Europe), avec qui sont-elles partagées, sont-elles utilisées pour de la publicité ciblée ? Pour une appli de cycles menstruels par exemple, la sensibilité est très forte — dans certains pays, ces données peuvent avoir des conséquences juridiques. Préférer les apps avec stockage local (qui ne transmettent rien aux serveurs de l'éditeur) ou les éditeurs européens soumis au RGPD avec une politique claire.

Les **bonnes pratiques** :

- Mot de passe unique sur chaque compte santé, MFA quand proposé.
- Pour Mon espace santé : sécuriser le compte du fournisseur d'identité utilisé pour s'y connecter via FranceConnect (Ameli en priorité, ou France Identité — cf. Ch.32).
- Ne pas envoyer d'analyses ou ordonnances par messagerie non chiffrée — utiliser Mon espace santé ou Doctolib pour les échanges patient-médecin.
- Vérifier périodiquement les remboursements Ameli pour détecter une éventuelle usurpation.
- Pour les applis de santé grand public : choisir avec attention, lire la politique de données, désactiver la synchronisation avec les réseaux sociaux, et ne pas accorder le partage au-delà du nécessaire.
- Conserver les codes de Mon espace santé hors du téléphone (comme tout code de récupération MFA).

---

<a id="chapitre-34"></a>
