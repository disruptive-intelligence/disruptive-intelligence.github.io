---
title: Chapitre 38 — Stalkerware et surveillance par un proche
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VII — Maison connectée, famille et frontière pro/perso
  - index.md
---

*Ce chapitre traite un sujet sensible et en croissance : la surveillance numérique exercée par un proche — actuel ou ex-partenaire, parent contrôlant, employeur abusif. Les outils existent, sont accessibles, et la victime ne sait souvent pas qu'elle est suivie. Si vous lisez ce chapitre dans le contexte d'une relation conjugale violente, des ressources spécialisées sont en bas de chapitre — n'agissez pas seule.*

## 38.1 Le contexte

La surveillance numérique d'un proche est différente d'une attaque externe. L'attaquant a un accès physique régulier au téléphone ou à l'ordinateur, connaît les mots de passe ou peut les voir être tapés, partage des comptes (Apple Family, Google Family, Netflix, etc.), et a une connaissance intime de la victime qui rend l'ingénierie sociale très efficace. Le contexte typique : ex-conjoint contrôlant ou violent, séparation conflictuelle, parent intrusif d'un jeune adulte, employeur dépassant le cadre légal de la surveillance. L'objectif de l'attaquant peut être le contrôle, la jalousie, le harcèlement, la collecte d'éléments pour une procédure (divorce, garde d'enfants), ou la coercition.

## 38.2 Les vecteurs concrets

**AirTags et trackers Bluetooth malveillants** : un AirTag glissé dans un sac, une voiture, une poche de manteau permet de suivre les déplacements de la victime. iOS et Android détectent les trackers inconnus qui voyagent avec vous et affichent une alerte (« un AirTag inconnu se déplace avec vous » sur iPhone, équivalent sur Android via l'app Tracker Detect ou les notifications natives Android 14+). Prendre ces alertes très au sérieux. Une alerte qui revient régulièrement n'est pas un faux positif.

**Partage de localisation** : Localiser/Find My, Google Maps « partage de position », Snap Map, partages familiaux. Vérifier qui a accès à votre localisation en permanence. Désactiver les partages anciens. Le partage Find My peut avoir été activé sans que vous le sachiez si quelqu'un a eu votre téléphone déverrouillé quelques minutes.

**Stalkerware** : applications de surveillance installées sur le téléphone de la victime, souvent vendues comme « contrôle parental » ou « contrôle conjugal » mais utilisées comme outils de surveillance. Elles transmettent SMS, appels, photos, localisation, frappes au clavier vers un compte distant. Sur Android, l'installation nécessite généralement un accès physique au téléphone et peut nécessiter de désactiver Play Protect. Sur iOS, c'est plus rare mais existe via la prise en main du compte iCloud (toutes les sauvegardes, photos, messages, localisation deviennent accessibles à qui contrôle le compte iCloud, sans application installée). Signaux possibles : batterie qui se vide anormalement vite, données mobiles consommées rapidement sans raison, téléphone qui chauffe au repos, applications inconnues, ou comportements suspects (le partenaire « sait » des choses qu'il ne devrait pas savoir).

**Comptes partagés** : iCloud familial avec accès aux photos, Apple ID partagé entre partenaires, comptes Google liés, gestionnaire de mots de passe partagé. Tout ce qui est partagé avec une personne dont la confiance est rompue devient un canal de surveillance.

**Caméras et micros de la maison** : les caméras de surveillance domestique installées « pour la sécurité » peuvent être réorientées vers l'intérieur, les babyphones peuvent être utilisés comme micros, les assistants vocaux peuvent enregistrer et l'historique peut être consulté par qui a accès au compte du foyer.

**Accès physique** : le partenaire connaît le code de déverrouillage (vu, deviné, partagé volontairement à un moment de confiance), accède au téléphone la nuit, lit les messages, installe ce qu'il veut.

## 38.3 Le diagnostic : signes d'une surveillance possible

- Le partenaire connaît votre localisation, vos messages, ou vos contenus sans que vous les ayez partagés.
- Le téléphone a un comportement inhabituel : batterie qui se vide vite, chauffe sans raison, notifications étranges, applications inconnues.
- Vous recevez des alertes de tracker inconnu.
- Vos comptes ont des sessions actives sur des appareils que vous ne reconnaissez pas.
- Vous découvrez un partage de localisation que vous n'avez pas activé.
- Vous remarquez un nouveau profil dans les paramètres MDM (Mobile Device Management) du téléphone.

Aucun de ces signes pris isolément ne prouve une surveillance — leur accumulation est ce qui doit alerter.

## 38.4 Que faire — avec précaution

**Le piège** : si vous êtes dans une situation de violence conjugale, la suppression brutale d'un stalkerware peut alerter l'agresseur et déclencher une escalade. Si la situation est dangereuse, ne pas agir seule — contacter le **3919** (violences conjugales, gratuit, anonyme, 24/7) pour être écoutée et orientée, une association spécialisée (Solidarité Femmes, France Victimes), ou un commissariat. **En cas de danger immédiat, le 3919 n'est pas un numéro d'urgence : appeler le 17 (police) ou le 112.** Des protocoles existent pour sécuriser numériquement une victime sans alerter l'agresseur.

**Si la situation n'est pas dangereuse mais que vous voulez reprendre le contrôle** :

1. Vérifier les **partages de localisation** actifs (iCloud > Localiser > Personnes ; Google Maps > Partage de position) et révoquer ceux qui ne devraient pas exister.
2. Vérifier les **sessions actives** sur les comptes principaux (Apple ID, Google, Facebook, Instagram, WhatsApp Web/Desktop) et déconnecter tout ce qui n'est pas à vous.
3. Vérifier les **profils MDM** sur iOS (Réglages > Général > VPN et gestion d'appareils) et Android (Paramètres > Sécurité > Applis d'administration de l'appareil) — supprimer ce qui n'a rien à faire là.
4. Vérifier les **applications installées** et désinstaller celles qui sont inconnues.
5. Changer **tous** les mots de passe critiques (email, banque, cloud, gestionnaire) depuis un appareil dont vous êtes sûre, et activer/changer le MFA.
6. Faire le **tour des trackers Bluetooth** dans le sac, les vêtements, le véhicule (utiliser l'app Tracker Detect d'Apple sur Android, ou la fonctionnalité native iOS qui scanne les trackers à proximité).
7. Sortir des **partages familiaux** (Apple Family, Google Family) si la relation est rompue — le faire au bon moment et dans le bon ordre.

Pour un nettoyage plus profond (ré-initialisation du téléphone, changement de SIM, nouveau compte) : se faire accompagner. La précipitation peut détruire des preuves utiles à une procédure judiciaire.

## 38.5 Reconstruction numérique après séparation

Une séparation est aussi une séparation numérique. Liste à parcourir : changer tous les mots de passe (email, banque, cloud, réseaux sociaux, streaming), retirer l'ex-partenaire du partage familial, retirer les accès aux comptes communs, vérifier les bénéficiaires sur les comptes bancaires et assurance-vie, réviser les sauvegardes automatiques (iCloud commun → désynchroniser), supprimer les appareils en commun des comptes personnels, et faire le tour des partages cloud (Drive, Dropbox, OneDrive). Cette liste prend du temps — la traiter méthodiquement, idéalement avec l'aide d'une personne de confiance.

## 38.6 Ressources

- **3919** — Violences Femmes Info, gratuit, anonyme, 24/7. Numéro d'écoute et d'orientation. **En cas de danger immédiat, appeler le 17 ou le 112.**
- **3018** — violences numériques pour mineurs et jeunes adultes, gratuit, anonyme, 7j/7 de 9h à 23h.
- **France Victimes** (116 006) — assistance aux victimes, écoute, orientation juridique.
- **Cybermalveillance.gouv.fr** — fiche dédiée au cyberharcèlement et à la surveillance par un proche.
- Coalition Against Stalkerware — ressources internationales.

---

<a id="chapitre-39"></a>
