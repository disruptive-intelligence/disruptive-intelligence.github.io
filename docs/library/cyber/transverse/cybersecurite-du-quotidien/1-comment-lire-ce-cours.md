---
title: Comment lire ce cours
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
chapter: 1
chapters: 9
---

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
