---
title: Chapitre 4 — Cartographie de vos surfaces d'attaque personnelles
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie I — Comprendre les risques du quotidien NUMÉRIQUE
  - index.md
---

Chaque personne a une surface d'attaque — l'ensemble des points par lesquels quelqu'un de malveillant peut l'atteindre. La cartographier est le premier exercice concret du cours. Ce n'est pas de la paranoïa — c'est de la lucidité.

Le **téléphone** est le point central. Il contient l'email (qui contrôle les réinitialisations de mot de passe de tous les comptes), la banque (app et notifications), le MFA (les codes d'authentification), les messageries (WhatsApp, Signal, SMS — là où arrivent les arnaques ET les communications légitimes), les photos (y compris les captures d'écran de documents et de conversations), et la localisation (historique des déplacements). Perdre son téléphone sans préparation est l'un des pires scénarios numériques du quotidien.

L'**ordinateur** contient les documents (fichiers personnels, administratifs, professionnels), les sessions ouvertes dans le navigateur (email, banque, cloud, réseaux sociaux — quiconque ouvre le navigateur accède à tout), les téléchargements (fichiers potentiellement malveillants), et les mots de passe enregistrés dans le navigateur (moins sécurisés que dans un gestionnaire dédié).

Le **navigateur** est la fenêtre vers tous les services en ligne. Les sessions actives (cookies qui maintiennent la connexion), les extensions (chacune a accès à tout ce que le navigateur voit), l'auto-remplissage (mots de passe, adresses, numéros de carte — pratique mais accessible à quiconque a accès à la session), et les notifications push (canal de spam et de phishing si mal géré).

L'**email** est le maître de tous les comptes. Celui qui contrôle l'email contrôle les réinitialisations de mot de passe de tous les comptes liés. Un email principal compromis = tous les comptes liés sont compromis. C'est pourquoi l'email principal doit avoir le mot de passe le plus fort et le MFA le plus robuste de tous les comptes.

Les **messageries** (WhatsApp, Signal, Telegram, SMS, iMessage) sont le canal par lequel arrivent la majorité des arnaques (smishing, phishing, faux liens, faux colis). Elles sont aussi le canal par lequel on envoie des informations sensibles (documents, photos, codes) — souvent sans réfléchir à qui d'autre pourrait y accéder.

Le **cloud** (iCloud, Google Drive, OneDrive, Dropbox) synchronise automatiquement les photos (y compris les captures d'écran de conversations et de documents), les fichiers, les contacts, et les sauvegardes. Un cloud compromis = accès à des années de données personnelles.

La **banque** (app mobile, site web) est la cible financière directe. Les prélèvements, les virements, les cartes — tout est accessible depuis l'app. Les notifications bancaires sont le meilleur système d'alerte — les activer pour chaque opération.

Les **réseaux sociaux** (Instagram, Facebook, LinkedIn, TikTok) sont une source d'information majeure pour l'ingénierie sociale. Ce qu'on publie, ce qu'on like, ce qu'on commente, ce qu'on tague — chaque interaction est une pièce de puzzle exploitable.

L'**identité numérique administrative** est devenue centrale en 2025-2026. **FranceConnect** n'est pas un compte mais un mécanisme de fédération d'identité — vous vous y connectez via un fournisseur d'identité partenaire (Ameli, impots.gouv.fr, La Poste Identité Numérique, MSA, France Identité, Yris, TrustMe selon les disponibilités). Si l'un de ces comptes pivots est compromis, l'accès à des dizaines de services publics via FranceConnect est compromis — déclarations fiscales, droits sociaux, dossier médical, démarches administratives. Cette surface est traitée en détail au Chapitre 32.

Le **réseau domestique** (box Internet, Wi-Fi, objets connectés, NAS, imprimantes) est le périmètre physique. Un Wi-Fi avec le mot de passe par défaut est ouvert au voisinage. Les objets connectés (caméras, assistants vocaux, TV connectées) sont autant de microphones et de caméras potentiellement accessibles.

Les **déplacements** (Wi-Fi public, recharge USB, QR codes, shoulder surfing) créent des expositions temporaires mais réelles.

Les **documents** (ceux qu'on envoie, qu'on photographie, qu'on scanne, qu'on jette) sont des vecteurs d'usurpation d'identité quand ils finissent dans les mauvaises mains.

L'**entourage** (famille, amis, collègues) est le maillon qu'on ne contrôle pas. Un proche qui utilise le même mot de passe partout, qui partage des photos avec la localisation, ou qui a accès à vos comptes via le partage familial est une extension de votre surface d'attaque. C'est aussi parfois l'angle d'attaque le plus délicat : un ex-conjoint, un colocataire, un parent contrôlant peut avoir un accès légitime qui devient malveillant (cf. Ch.38).

> **🔵 Lina — Épisode 3 :** Lina fait l'exercice de cartographie. Elle réalise que son email principal (Gmail) est le maître de 23 comptes, que son iCloud synchronise automatiquement ses photos (y compris les captures d'écran de conversations médicales sur Doctolib et une photo de son RIB envoyée à un ami), que son mot de passe Netflix est le même que celui de Vinted et de Booking, que sa mère a accès à son compte Amazon via le partage familial, que son profil Instagram est public avec des photos géolocalisées de son appartement, de son bureau, et de ses lieux de vacances, et qu'elle utilise FranceConnect via son compte Ameli sans se souvenir du mot de passe Ameli ni avoir vérifié qu'il était unique. La surface est bien plus grande qu'elle ne le pensait.

---

> ### 🟦 Réflexes — Fin de Partie I
>
> **À comprendre** : la cybersécurité du quotidien est une discipline comportementale, pas technique. Les attaquants exploitent des leviers psychologiques universels (urgence, autorité, peur, récompense, familiarité, fatigue). Personne n'est immunisé.
>
> **À appliquer comme état d'esprit** :
> - Méfiance calme — ni paranoïa, ni naïveté
> - Vérifier avant d'agir, surtout quand c'est urgent
> - Comprendre que le confort et la sécurité sont parfois en tension — c'est OK, mais il faut le savoir
>
> **Exercice à faire avant la suite** : la cartographie de votre surface d'attaque (Ch.4). 15 minutes, papier et crayon. Lister les comptes, les appareils, les messageries, les clouds, les réseaux sociaux. C'est la base de tout ce qui suit.

---
