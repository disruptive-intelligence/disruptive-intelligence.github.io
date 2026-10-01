---
title: Chapitre 30 — Cloud, sauvegardes et chiffrement côté client
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

## 30.1 Les trois états de la donnée

- **At rest** (au repos) : sur ton disque, sur un serveur cloud. Protégée par chiffrement disque/conteneur.
- **In transit** (en transit) : sur le réseau. Protégée par TLS/HTTPS.
- **In use** (en utilisation) : en RAM, déchiffrée, exploitable par un processus. Plus dur à protéger (TEE, enclaves matérielles).

Chaque état appelle des défenses différentes. Une chaîne complète doit traiter les trois.

## 30.2 Cloud par défaut

ce que Google Drive, OneDrive, Dropbox, iCloud peuvent lire

Sans précaution :

- **Google Drive** : Google peut lire (clé contrôlée par Google).
- **OneDrive** : Microsoft peut lire.
- **Dropbox** : Dropbox peut lire.
- **iCloud Drive** : Apple peut lire (sauf ADP activé).

Tous ces fournisseurs chiffrent les données au repos sur leurs serveurs (protection physique des serveurs), mais ils détiennent les clés. Conséquences :

- Réquisition judiciaire = accès complet.
- Faille interne ou attaquant qui compromet le fournisseur = accès complet.
- Politique de scanning automatique (CSAM, malware) = traitement du contenu.

## 30.3 Apple ADP : conditions et limites

Cf. Ch 14.6. Rappel : ADP active l’E2EE pour la majorité des données iCloud. Pas pour mail, contacts, calendrier.

**Conditions** : tous les appareils Apple à version récente, clé de récupération à conserver (perte = perte de données définitive).

**Pour qui** : tout utilisateur Apple avec données dans iCloud. À activer.

## 30.4 Cloud E2EE par design : Proton Drive, Tresorit, Mega

- **Proton Drive** : Suisse, E2EE par design, intégré écosystème Proton. Capacité variable selon plan.
- **Tresorit** : Suisse, E2EE par design, focalisé pro et entreprise, audits réguliers. Plus cher.
- **Mega** : Nouvelle-Zélande, E2EE par design. Capacité gratuite généreuse, historique controversé (Kim Dotcom) mais sécurité côté client réputée correcte.

**Pour qui** : utilisateurs voulant E2EE par défaut sans setup technique. Choisir selon juridiction et budget.

## 30.5 Chiffrement côté client par-dessus cloud généraliste

Tu veux garder Google Drive ou Dropbox pour des raisons d’écosystème, mais chiffrer ce que tu y mets ? Solutions :

- **Cryptomator** : conteneur de dossier transparent. Tu pointes Cryptomator vers un dossier dans Google Drive, il y crée une structure de fichiers chiffrés. Tu déverrouilles avec un mot de passe, ton OS voit un dossier monté. Multi-plateforme, open source, libre.
- **gocryptfs / EncFS** (Linux/macOS) : similaire, ligne de commande.
- **rclone + crypt backend** : pour scripts, sauvegardes automatisées vers cloud chiffré.

Tu peux utiliser le cloud que tu veux comme tu veux, et lui n’a plus accès au contenu. C’est l’option pragmatique pour beaucoup.

## 30.6 Nextcloud self-hosted

**Nextcloud** est un cloud privé auto-hébergé. Tu installes sur un VPS ou serveur domestique, tu as Drive + Calendrier + Contacts + Mail + plus.

**Avantages** : contrôle total, juridiction de ton choix, fonctionnalités étendues.

**Limites** :

- L’E2EE Nextcloud officielle a un historique mitigé. Pour E2EE sérieuse, combiner avec Cryptomator au-dessus.
- Maintenance technique nécessaire (mises à jour, sauvegardes, monitoring).
- Bande passante limitée à ta connexion.

## 30.7 Syncthing

**Syncthing** synchronise des dossiers entre appareils en peer-to-peer, sans cloud intermédiaire. Configuration sur chaque appareil, échange par identifiants. Chiffré bout-en-bout, open source.

Cas d’usage : sync notes entre laptop et téléphone sans aucun fournisseur tiers. Synchronisation continue.

## 30.8 Sauvegarde : règle 3-2-1

- **3 copies** des données importantes.
- **2 supports** différents (disque local + cloud, ou disque interne + externe).
- **1 hors site** (hors de chez toi).

Pour profils exposés : **3-2-1-1-0** ajoute :

- **1 sauvegarde immuable** (write-once, hors atteinte ransomware).
- **0 erreur** : tests de restauration réguliers.

## 30.9 Sauvegardes locales chiffrées

- **restic** : open source, déduplication, chiffrement par défaut. Backends multiples (local, S3, Backblaze B2, SFTP). Préférée pour script et automatisation.
- **Borg / BorgBackup** : similar à restic, déduplication efficace, communauté solide.
- **Time Machine** (macOS) + FileVault activé = sauvegarde chiffrée. Pratique pour utilisateurs Apple.
- **Windows Backup / File History** : moins puissant, OK pour basique.

## 30.10 Photos : sync auto et fuites

La synchronisation auto des photos vers iCloud/Google Photos remonte tout, avec EXIF, à chaque déclenchement. Pour profils sensibles :

- Désactiver la synchronisation auto.
- Tri manuel avant upload.
- Effacement EXIF avant publication (Ch 31).
- Pour photos sensibles d’enquête : jamais dans le cloud personnel.

## 30.11 Test de restauration

**La sauvegarde non testée n’existe pas**. Une fois par an au minimum : test de restauration complète sur appareil neuf. Sinon, tu découvres au moment critique que ton backup est corrompu, incomplet, ou inutilisable.

## 30.12 Sauvegarde des secrets

Clés PGP, codes de récupération, clé de récupération ADP, codes 2FA backup : ne pas oublier de sauvegarder.

Options :

- **Coffre matériel** : YubiKey backup avec mêmes clés que la principale.
- **Papier + coffre physique** : impression des codes, dans une enveloppe scellée, en coffre à la banque ou chez un avocat.
- **Cryptomator + cloud** : conteneur avec tous tes secrets, sauvegardé dans plusieurs clouds.

## 30.13 Plan en cas de perte ou vol

Préparé à l’avance :

1. **Effacement à distance** : Find My iPhone, Android Find My Device, Microsoft Find My Device.
1. **Révocation des sessions** sur tous les comptes.
1. **Désactivation des passkeys et certificats** liés à l’appareil.
1. **Notification de l’opérateur** pour bloquer la SIM si applicable.
1. **Déclaration de vol** (police, assureur).
1. **Restauration sur appareil neuf** depuis sauvegarde chiffrée.
1. **Audit** : changement préventif des mots de passe critiques si suspicion de compromission de l’appareil avant l’effacement.

-----
