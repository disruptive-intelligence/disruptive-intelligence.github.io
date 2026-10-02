---
title: Cybersécurité du quotidien
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
format: cours
revue: '2026-04-27'
---

*Se protéger • Détecter • Éviter • Réagir*

**Cours complet — 45 chapitres • 8 parties • 13 annexes • 1 parcours express**

*Hygiène numérique • Arnaques • Mobilité • Vie privée • Réflexes de survie*

---

## Comment lire ce cours

Ce cours peut se lire de **deux façons**.

**Parcours express (1 heure)** : la première section ci-dessous — *Les 10 actions prioritaires* — couvre 80 % du risque réel pour un particulier. C'est le minimum vital, configuré une fois pour toutes. Si vous ne lisez rien d'autre, lisez ça et appliquez-le ce soir.

**Parcours complet (45 chapitres)** : la suite du cours. Chaque chapitre approfondit un risque, un usage ou une situation de vie courante. Le but n'est pas de tout lire d'un trait — c'est d'avoir une référence à laquelle revenir : « comment je sécurise mon téléphone », « que faire si mon compte est compromis », « comment partager un document sensible », « mon enfant utilise une tablette, à quoi je dois faire attention ».

À la fin de chaque grande partie, un **encadré « Réflexes »** résume les actions à configurer, à éviter, à vérifier régulièrement, et à connaître en cas d'incident.

---

## ⚡ PARCOURS EXPRESS — 10 actions prioritaires en 1 heure

> *Si vous ne lisez rien d'autre, lisez ceci. Ces 10 actions, configurées une fois, couvrent 80 % du risque réel pour un particulier. Comptez environ 1 heure au total — 10 à 15 minutes pour les plus rapides, 20 minutes pour le gestionnaire de mots de passe. Une fois fait, c'est fait.*

**1. Mettre un code à 6 chiffres minimum sur le téléphone (5 min)**

Pas de date de naissance, pas de 123456, pas de 000000. Un code à 4 chiffres a 10 000 combinaisons — observable par-dessus l'épaule en 2 secondes ; un code à 6 chiffres en a 1 million. Activer Face ID ou Touch ID en complément (pas en remplacement). Le code est le vrai verrou — c'est lui qui déchiffre le téléphone au démarrage.

**2. Activer la localisation et l'effacement à distance (3 min)**

iPhone : Réglages > [votre nom] > Localiser > Localiser mon iPhone (activer tout). Android : Paramètres > Sécurité > Localiser mon appareil. À configurer MAINTENANT, pas le jour de la perte. Sans ça, un téléphone perdu = un téléphone potentiellement accessible à quiconque le ramasse, et impossible à effacer.

**3. Installer un gestionnaire de mots de passe (20 min)**

Bitwarden (gratuit, open source) ou 1Password (payant, très ergonomique). Créer un compte, choisir un mot de passe maître **long, mémorisable, et unique** — une phrase de 4-5 mots type « café.vélo.montagne.Jupiter.2024 ». Ce mot de passe ne doit JAMAIS être utilisé ailleurs et JAMAIS être stocké dans le téléphone. Importer les mots de passe enregistrés dans le navigateur, puis générer un mot de passe unique pour chaque nouveau compte. C'est l'investissement le plus rentable de toute la cybersécurité personnelle.

**4. Changer le mot de passe de l'email principal (5 min)**

L'email maître est le compte le plus critique — c'est lui qui reçoit les réinitialisations de mot de passe de tous les autres comptes. Le compromettre = tout perdre. Mot de passe unique, long, généré par le gestionnaire et stocké dedans.

**5. Activer le MFA sur les 5 comptes critiques (10 min)**

Email principal, banque, gestionnaire de mots de passe lui-même, cloud principal (iCloud/Google), messagerie principale. Préférer une **application TOTP dédiée** (Aegis, 2FAS, Ente Auth, Proton Authenticator, Authy selon plateforme et préférences) ou une clé physique pour les comptes vraiment critiques. Stocker les codes TOTP dans le gestionnaire de mots de passe est pratique et acceptable pour des comptes secondaires, mais moins idéal pour l'email maître, la banque ou le gestionnaire lui-même : si le gestionnaire est compromis, l'attaquant aurait à la fois le mot de passe et le second facteur. Pour la banque française : utiliser plutôt l'authentification forte de l'application bancaire. Le SMS reste mieux que rien mais vulnérable au SIM swap (cf. Ch.7).

**6. Imprimer les codes de récupération MFA (5 min)**

À chaque activation de MFA, le service propose des codes de récupération à usage unique. Les imprimer, les noter sur papier, les stocker dans un tiroir à la maison ou chez un proche de confiance. **Ne PAS les stocker uniquement dans le téléphone** — c'est le téléphone qu'on perd.

**7. Activer les mises à jour automatiques sur tous les appareils (3 min)**

Téléphone, ordinateur, navigateur, applications. Les mises à jour corrigent des vulnérabilités exploitées activement. Un appareil pas à jour = des serrures cassées. Aucune excuse à ne pas avoir activé l'auto-update — la fenêtre de vulnérabilité est la principale porte d'entrée des attaques opportunistes.

**8. Vérifier les sessions actives et déconnecter les inconnues (5 min)**

Email, banque, cloud, réseaux sociaux : chaque service a une page « Sessions actives » ou « Appareils connectés ». La consulter, déconnecter tout ce qui n'est pas reconnu (un vieux téléphone vendu, un ordinateur de bureau qui n'existe plus, une connexion suspecte). Faire ce nettoyage une fois maintenant, puis tous les 6 mois.

**9. Configurer une sauvegarde automatique des photos et des documents critiques (5 min)**

Photos : iCloud Photos (iPhone) ou Google Photos (Android), activé. Documents critiques (CNI numérisée, justificatifs, codes MFA) : sur un cloud chiffré (cf. Ch.35) ET sur un disque externe rangé hors ligne. Les photos irremplaçables ne se recréent pas.

**10. Préparer le mini-plan « téléphone perdu » (5 min)**

Sur un papier rangé chez vous, noter : le numéro de blocage SIM de votre opérateur, le numéro d'opposition de votre banque, l'adresse de récupération secondaire de votre email maître, et les sites Find My / Find My Device pour la localisation à distance. Ces 4 informations vous font gagner 30 minutes de panique le jour où ça arrive — et 30 minutes peuvent être la différence entre un désagrément et un désastre.

> **Bonus — Le mot de sécurité familial (5 min, à faire en famille)** : convenir avec ses proches (parents, conjoint, enfants) d'un mot ou d'une phrase à demander dans toute situation d'urgence où l'identité doit être confirmée. Protection contre le deepfake vocal — l'IA peut imiter une voix, elle ne peut pas répondre à une question convenue d'avance.

**Une fois ces 10 actions faites, vous avez fait l'essentiel.** La suite du cours approfondit, contextualise, et vous prépare aux situations spécifiques. Mais l'ossature de protection est en place.

---

<a id="fil-rouge--opération-vie-numérique"></a>
## Fil rouge : Opération VIE NUMÉRIQUE

> **Lina**, 28 ans, consultante en gestion de projet, vit à Lyon. Connectée, mobile, active — smartphone personnel (iPhone), MacBook perso, téléphone pro Android (BYOD partiel), 4 messageries (iMessage, WhatsApp, Signal, Teams), comptes sur une dizaine de plateformes (banque en ligne, Vinted, Booking, Doctolib, Spotify, Netflix, Amazon), un cloud iCloud pour les photos et Google Drive pour les documents, des réseaux sociaux (Instagram, LinkedIn), et un assistant vocal à la maison.
>
> Lina n'est ni naïve ni experte. Elle fait « attention » mais ne sait pas exactement à quoi. Au fil du cours, elle rencontre des situations réalistes — certaines qu'elle détecte, d'autres qui la piègent, d'autres qu'elle ne réalise même pas. Chaque épisode illustre un chapitre sans être ni gadget ni romancé.

---

## Sommaire

- [Partie I — Comprendre les risques du quotidien NUMÉRIQUE](01-partie-i-comprendre-les-risques-du-quotidien-numer/index.md)
    - [Chapitre 1 — Pourquoi la cybersécurité du quotidien mérite un vrai cours](01-partie-i-comprendre-les-risques-du-quotidien-numer/01-chapitre-1-pourquoi-la-cybersecurite-du-quotidien.md)
    - [Chapitre 2 — Les grands principes d'hygiène numérique](01-partie-i-comprendre-les-risques-du-quotidien-numer/02-chapitre-2-les-grands-principes-d-hygiene-numeriqu.md)
    - [Chapitre 3 — Pourquoi les gens intelligents se font piéger](01-partie-i-comprendre-les-risques-du-quotidien-numer/03-chapitre-3-pourquoi-les-gens-intelligents-se-font.md)
    - [Chapitre 4 — Cartographie de vos surfaces d'attaque personnelles](01-partie-i-comprendre-les-risques-du-quotidien-numer/04-chapitre-4-cartographie-de-vos-surfaces-d-attaque.md)
- [Partie II — Fondations : appareils, comptes et continuité](02-partie-ii-fondations-appareils-comptes-et-continui/index.md)
    - [Chapitre 5 — Sécuriser son téléphone : le maillon central](02-partie-ii-fondations-appareils-comptes-et-continui/01-chapitre-5-securiser-son-telephone-le-maillon-cent.md)
    - [Chapitre 6 — Sécuriser son ordinateur personnel](02-partie-ii-fondations-appareils-comptes-et-continui/02-chapitre-6-securiser-son-ordinateur-personnel.md)
    - [Chapitre 7 — Mots de passe, gestionnaire, passkeys, MFA et SIM swap](02-partie-ii-fondations-appareils-comptes-et-continui/03-chapitre-7-mots-de-passe-gestionnaire-passkeys-mfa.md)
    - [Chapitre 8 — Navigateur, sessions et hygiène web](02-partie-ii-fondations-appareils-comptes-et-continui/04-chapitre-8-navigateur-sessions-et-hygiene-web.md)
    - [Chapitre 9 — Sauvegardes, récupération et comptes de secours](02-partie-ii-fondations-appareils-comptes-et-continui/05-chapitre-9-sauvegardes-recuperation-et-comptes-de.md)
    - [Chapitre 10 — Construire sa continuité numérique personnelle](02-partie-ii-fondations-appareils-comptes-et-continui/06-chapitre-10-construire-sa-continuite-numerique-per.md)
- [Partie III — Mobilité, espaces publics et risques physiques](03-partie-iii-mobilite-espaces-publics-et-risques-phy.md)
- [Partie IV — Communications, arnaques et ingénierie sociale](04-partie-iv-communications-arnaques-et-ingenierie-so/index.md)
    - [Chapitre 15 — Email, SMS et messageries : reconnaître les pièges](04-partie-iv-communications-arnaques-et-ingenierie-so/01-chapitre-15-email-sms-et-messageries-reconnaitre-l.md)
    - [Chapitre 16 — Faux support technique et faux conseillers](04-partie-iv-communications-arnaques-et-ingenierie-so/02-chapitre-16-faux-support-technique-et-faux-conseil.md)
    - [Chapitre 17 — Banque, paiements, e-commerce et marketplaces](04-partie-iv-communications-arnaques-et-ingenierie-so/03-chapitre-17-banque-paiements-e-commerce-et-marketp.md)
    - [Chapitre 18 — Arnaques à l'investissement, crypto et faux placements](04-partie-iv-communications-arnaques-et-ingenierie-so/04-chapitre-18-arnaques-a-l-investissement-crypto-et.md)
    - [Chapitre 19 — Réseaux sociaux, faux profils, sextorsion et arnaques relationnelles](04-partie-iv-communications-arnaques-et-ingenierie-so/05-chapitre-19-reseaux-sociaux-faux-profils-sextorsio.md)
    - [Chapitre 20 — Deepfakes, voix clonées et nouvelles fraudes IA](04-partie-iv-communications-arnaques-et-ingenierie-so/06-chapitre-20-deepfakes-voix-clonees-et-nouvelles-fr.md)
    - [Chapitre 21 — Quand le confort remplace la sécurité](04-partie-iv-communications-arnaques-et-ingenierie-so/07-chapitre-21-quand-le-confort-remplace-la-securite.md)
- [Partie V — Choisir ses outils numériques de confiance](05-partie-v-choisir-ses-outils-numeriques-de-confianc/index.md)
    - [Chapitre 22 — Classer la sensibilité avant de choisir l'outil](05-partie-v-choisir-ses-outils-numeriques-de-confianc/01-chapitre-22-classer-la-sensibilite-avant-de-choisi.md)
    - [Chapitre 23 — Visioconférence : choisir l'outil selon le contexte](05-partie-v-choisir-ses-outils-numeriques-de-confianc/02-chapitre-23-visioconference-choisir-l-outil-selon.md)
    - [Chapitre 24 — Messageries : choisir le bon canal](05-partie-v-choisir-ses-outils-numeriques-de-confianc/03-chapitre-24-messageries-choisir-le-bon-canal.md)
    - [Chapitre 25 — Transfert de fichiers](05-partie-v-choisir-ses-outils-numeriques-de-confianc/04-chapitre-25-transfert-de-fichiers.md)
    - [Chapitre 26 — Cloud, documents collaboratifs et stockage](05-partie-v-choisir-ses-outils-numeriques-de-confianc/05-chapitre-26-cloud-documents-collaboratifs-et-stock.md)
    - [Chapitre 27 — IA, traduction, OCR et PDF en ligne](05-partie-v-choisir-ses-outils-numeriques-de-confianc/06-chapitre-27-ia-traduction-ocr-et-pdf-en-ligne.md)
    - [Chapitre 28 — Gestionnaires de mots de passe, coffres et clés physiques](05-partie-v-choisir-ses-outils-numeriques-de-confianc/07-chapitre-28-gestionnaires-de-mots-de-passe-coffres.md)
    - [Matrice de synthèse — Quels outils privilégier selon le contexte](05-partie-v-choisir-ses-outils-numeriques-de-confianc/08-matrice-de-synthese-quels-outils-privilegier-selon.md)
- [Partie VI — VIE privée, images, documents et surexposition](06-partie-vi-vie-privee-images-documents-et-surexposi/index.md)
    - [Chapitre 29 — Réseaux sociaux et surexposition personnelle](06-partie-vi-vie-privee-images-documents-et-surexposi/01-chapitre-29-reseaux-sociaux-et-surexposition-perso.md)
    - [Chapitre 30 — Photos, scans et captures d'écran](06-partie-vi-vie-privee-images-documents-et-surexposi/02-chapitre-30-photos-scans-et-captures-d-ecran.md)
    - [Chapitre 31 — Documents sensibles et usurpation d'identité](06-partie-vi-vie-privee-images-documents-et-surexposi/03-chapitre-31-documents-sensibles-et-usurpation-d-id.md)
    - [Chapitre 32 — Identité numérique administrative](06-partie-vi-vie-privee-images-documents-et-surexposi/04-chapitre-32-identite-numerique-administrative.md)
    - [Chapitre 33 — Données de santé numériques](06-partie-vi-vie-privee-images-documents-et-surexposi/05-chapitre-33-donnees-de-sante-numeriques.md)
    - [Chapitre 34 — Métadonnées, contexte et fuite involontaire](06-partie-vi-vie-privee-images-documents-et-surexposi/06-chapitre-34-metadonnees-contexte-et-fuite-involont.md)
- [Partie VII — Maison connectée, famille et frontière pro/perso](07-partie-vii-maison-connectee-famille-et-frontiere-p/index.md)
    - [Chapitre 35 — Cloud personnel et partage familial](07-partie-vii-maison-connectee-famille-et-frontiere-p/01-chapitre-35-cloud-personnel-et-partage-familial.md)
    - [Chapitre 36 — Maison connectée et objets du quotidien](07-partie-vii-maison-connectee-famille-et-frontiere-p/02-chapitre-36-maison-connectee-et-objets-du-quotidie.md)
    - [Chapitre 37 — Enfants, famille et entourage numérique](07-partie-vii-maison-connectee-famille-et-frontiere-p/03-chapitre-37-enfants-famille-et-entourage-numerique.md)
    - [Chapitre 38 — Stalkerware et surveillance par un proche](07-partie-vii-maison-connectee-famille-et-frontiere-p/04-chapitre-38-stalkerware-et-surveillance-par-un-pro.md)
    - [Chapitre 39 — Frontière pro/perso : les risques de la porosité](07-partie-vii-maison-connectee-famille-et-frontiere-p/05-chapitre-39-frontiere-pro-perso-les-risques-de-la.md)
    - [Chapitre 40 — Quand l'attaque personnelle devient un problème d'entreprise](07-partie-vii-maison-connectee-famille-et-frontiere-p/06-chapitre-40-quand-l-attaque-personnelle-devient-un.md)
- [Partie VIII — Quand ça tourne mal : réagir et se reconstruire](08-partie-viii-quand-ca-tourne-mal-reagir-et-se-recon/index.md)
    - [Chapitre 41 — Réagir à une compromission de compte](08-partie-viii-quand-ca-tourne-mal-reagir-et-se-recon/01-chapitre-41-reagir-a-une-compromission-de-compte.md)
    - [Chapitre 42 — Téléphone perdu, volé ou compromis](08-partie-viii-quand-ca-tourne-mal-reagir-et-se-recon/02-chapitre-42-telephone-perdu-vole-ou-compromis.md)
    - [Chapitre 43 — Revente, don et réparation : effacer avant de céder](08-partie-viii-quand-ca-tourne-mal-reagir-et-se-recon/03-chapitre-43-revente-don-et-reparation-effacer-avan.md)
    - [Chapitre 44 — Signaler, documenter, se faire assister](08-partie-viii-quand-ca-tourne-mal-reagir-et-se-recon/04-chapitre-44-signaler-documenter-se-faire-assister.md)
    - [Chapitre 45 — Construire son plan personnel et préparer l'héritage numérique](08-partie-viii-quand-ca-tourne-mal-reagir-et-se-recon/05-chapitre-45-construire-son-plan-personnel-et-prepa.md)
- [Annexes](09-annexes/index.md)
    - [Annexe A — Glossaire](09-annexes/01-annexe-a-glossaire.md)
    - [Annexe B — Checklists pratiques](09-annexes/02-annexe-b-checklists-pratiques.md)
    - [Annexe C — Tableau des signaux d'arnaque](09-annexes/03-annexe-c-tableau-des-signaux-d-arnaque.md)
    - [Annexe D — Configuration minimale recommandée](09-annexes/04-annexe-d-configuration-minimale-recommandee.md)
    - [Annexe E — Modèle de plan personnel de cybersécurité](09-annexes/05-annexe-e-modele-de-plan-personnel-de-cybersecurite.md)
    - [Annexe F — Cartographie des arnaques fréquentes](09-annexes/06-annexe-f-cartographie-des-arnaques-frequentes.md)
    - [Annexe G — Ressources utiles](09-annexes/07-annexe-g-ressources-utiles.md)
    - [Annexe H — Matrice de priorité](09-annexes/08-annexe-h-matrice-de-priorite.md)
    - [Annexe I — Que faire si... (situations courantes)](09-annexes/09-annexe-i-que-faire-si-situations-courantes.md)
    - [Annexe J — Fiche d'urgence à imprimer](09-annexes/10-annexe-j-fiche-d-urgence-a-imprimer.md)
    - [Annexe K — Sources et ressources officielles](09-annexes/11-annexe-k-sources-et-ressources-officielles.md)
    - [Annexe L — Avertissement éditorial et juridique](09-annexes/12-annexe-l-avertissement-editorial-et-juridique.md)
    - [Annexe M — Les 12 règles à retenir](09-annexes/13-annexe-m-les-12-regles-a-retenir.md)
