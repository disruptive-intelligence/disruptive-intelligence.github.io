---
title: Chapitre 45 — Construire son plan personnel et préparer l'héritage numérique
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie VIII — Quand ça tourne mal : réagir et se reconstruire'
  - index.md
---

*Le dernier chapitre transforme tout ce qui a été appris en un plan d'action concret et personnalisé — y compris la question rarement traitée mais essentielle de la transmission numérique.*

## 45.1 L'inventaire personnel

L'**inventaire des comptes critiques** : les 5-10 comptes dont la compromission serait la plus grave — email maître, banque, gestionnaire de mots de passe, cloud principal, messagerie principale, et les fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste, France Identité). Ce sont ceux qui doivent avoir les mots de passe les plus forts et le MFA le plus robuste.

L'**inventaire des appareils** : téléphone principal, ordinateur, éventuel second appareil — chacun doit être verrouillé, chiffré, à jour, avec la localisation à distance activée.

Le **plan de sauvegarde** : quelles données, sur quels supports, à quelle fréquence → les photos sur iCloud/Google Photos + un disque externe tous les 3 mois, les codes de récupération MFA imprimés dans un lieu sûr, la sauvegarde du gestionnaire de mots de passe.

Le **plan de réaction** : que faire si le téléphone disparaît ? (bloquer SIM → localiser/effacer → email maître → sessions → banque), si un compte est compromis ? (mot de passe → email maître → MFA → sessions → paramètres → comptes liés), si un prélèvement frauduleux apparaît ? (opposition → plainte → contestation bancaire → documentation).

## 45.2 Les 10 habitudes qui couvrent 80 % du risque

(1) gestionnaire de mots de passe avec un mot de passe unique par compte, (2) authentification forte sur les comptes critiques — application TOTP ou clé physique pour l'email, le cloud, le gestionnaire, et les fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste) ; pour la banque, utiliser le moyen d'authentification forte proposé par l'établissement (application bancaire, Secure Key, validation biométrique) plutôt que le SMS quand une alternative existe, (3) mises à jour automatiques sur tous les appareils, (4) verrouillage systématique (téléphone code 6+, ordinateur), (5) sauvegardes régulières (cloud + disque externe tous les 3 mois), (6) vérifier avant de cliquer (lien, QR code, appel — 10 secondes de vérification suffisent), (7) localisation à distance configurée (Find My / Find My Device), (8) nettoyer les images avant partage (flouter, recadrer, supprimer les EXIF), (9) raccrocher et rappeler pour tout appel suspect, (10) codes de récupération MFA stockés hors du téléphone.

Le **mot de sécurité familial** : convenir avec ses proches (parents, conjoint, enfants) d'un mot ou d'une phrase à demander dans toute situation d'urgence où l'identité doit être confirmée — protection contre le deepfake vocal. Ce mot ne doit jamais figurer en ligne, dans un message, ou dans une publication — il vit uniquement dans la mémoire des membres de la famille.

## 45.3 Préparer l'héritage numérique

*La question rarement abordée : que devient votre vie numérique si vous ne pouvez plus y accéder — accident, maladie, décès ?*

Sans préparation : les proches se retrouvent à devoir prouver leur lien à des fournisseurs étrangers, parfois sans succès. Les photos de famille restent verrouillées dans iCloud, les comptes en ligne continuent d'exister sans personne pour les fermer, les abonnements continuent de prélever, et les messages sur les réseaux sociaux restent en suspens.

**Les outils des plateformes** : la plupart des géants du numérique ont mis en place des mécanismes — encore mal connus — pour préparer la transmission.

- **Apple** : « Contact légataire » (Réglages > [votre nom] > Connexion et sécurité > Contact légataire) — désigne une personne qui pourra accéder à vos données iCloud après votre décès en présentant un certificat de décès.
- **Google** : « Gestionnaire de compte inactif » (myaccount.google.com/inactive) — définit ce qui doit se passer si le compte n'est pas utilisé pendant X mois (transmission de certaines données à des contacts désignés, suppression).
- **Facebook/Meta** : « Contact légataire » qui peut transformer le profil en compte de commémoration ou demander la suppression.
- **Microsoft** : pas d'équivalent direct, mais procédure de demande pour les ayants droit.

**Le coffre papier minimal** : un document — chez un notaire, dans un coffre, ou chez un proche de confiance — contenant le strict nécessaire pour qu'une personne de confiance puisse intervenir en cas d'incapacité ou de décès. Quoi y mettre : la liste des comptes essentiels (email, banque, gestionnaire de mots de passe — pas les mots de passe en clair, juste l'inventaire), les contacts utiles (employeur, banque, mutuelle, opérateurs), et le mot de passe maître du gestionnaire — soit dans le même document, soit dans une enveloppe scellée à part. Cette information doit être traitée avec autant de soin qu'un testament — c'est de fait un testament numérique.

**Le testament numérique** : la loi française reconnaît le droit de définir des directives concernant la conservation, l'effacement, et la communication des données après le décès (article 85 de la loi Informatique et Libertés modifiée). Ces directives peuvent être inscrites auprès d'un tiers de confiance certifié, ou plus simplement dans un testament classique chez un notaire.

**Le geste minimum**, même sans formaliser : informer une personne de confiance qu'il existe un gestionnaire de mots de passe, où les codes de récupération sont stockés, et qui contacter en cas d'urgence. Cette conversation de 5 minutes peut épargner des semaines de difficultés à vos proches.

## 45.4 Maintenir : la cybersécurité comme habitude, pas comme projet

La sécurité n'est pas un projet qui se termine. Les comptes évoluent, les outils changent, les menaces se transforment. Le réflexe d'entretien : une **revue annuelle** (15 minutes en début d'année — état des comptes critiques, mises à jour, sauvegarde fonctionne, codes de récupération à jour, contacts de récupération encore valides), et une **revue trimestrielle légère** (sessions actives sur les comptes principaux, partages cloud, abonnements actifs).

Le piège inverse : la sur-paranoïa qui paralyse. Si la cybersécurité personnelle devient une charge mentale qui empêche d'utiliser le numérique sereinement, c'est qu'elle est mal calibrée. Le but : un cadre qui rend le numérique plus serein, pas plus stressant.

> **🔵 Lina — Épilogue :** 6 mois après le début du cours. Gestionnaire de mots de passe (Bitwarden), authentification forte sur les 8 comptes critiques (TOTP pour email/cloud/gestionnaire/FranceConnect/Ameli/impôts/messagerie ; validation par l'app bancaire pour la banque), iPhone et MacBook chiffrés et à jour, Find My activé, codes de récupération imprimés chez ses parents, sauvegarde trimestrielle sur disque externe, profil Instagram en privé, partages Google Drive nominatifs, mot de sécurité familial convenu avec sa mère, et contact légataire Apple désigné. Elle n'est pas devenue paranoïaque — elle a construit des habitudes. Le jour où elle reçoit un faux appel de sa banque, elle raccroche, rappelle le vrai numéro, et signale la tentative. 30 secondes. Zéro dégât. La méthode a remplacé la vigilance vague — et c'est ce qui change tout.

---

> ### 🟦 Réflexes — Fin de Partie VIII
>
> **À configurer** :
> - Plan de réaction écrit : numéros opposition SIM/banque, ordre des actions
> - Contact légataire Apple / Gestionnaire de compte inactif Google
> - Coffre papier minimal chez un proche de confiance ou notaire
> - Revue annuelle planifiée (date dans l'agenda)
>
> **À éviter** :
> - Réinitialisation de téléphone/PC sans déconnecter d'abord les comptes Apple/Google
> - Vente d'appareil avec un formatage rapide (pas suffisant)
> - SAV qui demande votre mot de passe sans changement temporaire
> - Réinstallation depuis une sauvegarde d'un appareil qu'on suspecte compromis
>
> **À vérifier** :
> - Find My / Find My Device toujours actif et fonctionnel
> - Sessions actives sur les comptes critiques (trimestriel)
> - Partages cloud actifs (semestriel)
> - Vous savez où sont vos codes de récupération MFA
> - Une personne de confiance sait où trouver l'essentiel en cas d'urgence
>
> **Si quelque chose arrive** :
> - Compte compromis → MdP du compte → email maître → MFA → sessions → comptes liés
> - Téléphone perdu/volé → SIM → Find My → email → sessions → banque → plainte
> - Fraude bancaire → opposition immédiate → contestation 13 mois max → THESEE → médiateur si refus
> - Doute sur compromission → 17Cyber + Cybermalveillance.gouv.fr

---
