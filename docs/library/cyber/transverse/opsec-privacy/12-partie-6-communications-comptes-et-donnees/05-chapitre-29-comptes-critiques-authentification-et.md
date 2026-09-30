---
title: Chapitre 29 — Comptes critiques, authentification et secrets
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

> **Note pédagogique** : ce chapitre est long. Il est structuré en trois sous-blocs majeurs : (A) comptes critiques et récupération, (B) mots de passe et coffres, (C) MFA, passkeys et clés physiques. Chacun peut être lu indépendamment, mais ensemble ils forment l’architecture d’authentification personnelle.

## A. Comptes critiques et récupération

## 29.1 L’email principal comme centre de gravité

L’email principal n’est pas un compte parmi d’autres. C’est le **pivot** :

- Récupération de mot de passe de la quasi-totalité des services.
- Réception des codes MFA par email (à éviter, mais courant).
- Notifications de connexion suspectes.
- Identifiant de récupération de comptes Apple/Google/Microsoft.

**Sa compromission cascade en compromission massive**. Sa protection prime sur tout.

Mesures concrètes :

- Mot de passe unique et long (gestionnaire obligatoire, Ch 29.7).
- MFA matériel ou TOTP (jamais SMS pour ce compte).
- Audit régulier des sessions actives.
- Surveillance des notifications de connexion (paramétrer alertes).
- Récupération configurée mais audit régulier (méthodes de récupération, contacts de récupération, codes).

## 29.2 Comptes pivots : Apple ID, Google, Microsoft

Selon l’écosystème, ces comptes contiennent : iCloud (photos, contacts, sauvegardes, mails, Keychain), Google (Gmail, Drive, photos, contacts, Android backup), Microsoft (OneDrive, Office, BitLocker recovery). Leur compromission = perte d’une grande partie de la vie numérique.

Mesures :

- Vérification en 2 étapes activée (FIDO2 idéalement).
- Clés de sécurité matérielles enregistrées.
- Mode protection avancée Google (Advanced Protection Program — pour cibles à risque).
- ADP iCloud activée.

## 29.3 Récupération de compte : le maillon faible

La compromission d’un compte sécurisé passe presque toujours par **la récupération**, pas par l’attaque directe :

- SIM swap pour intercepter les SMS de récupération.
- Réponse à questions de sécurité devinées (par OSINT sur la cible).
- Accès au mail de récupération.
- Social engineering du support client.

Audit régulier :

- Numéro de téléphone de récupération : à jour, sécurisé (cf. anti-SIM swap).
- Email de récupération : sur compte sérieusement sécurisé.
- Questions de sécurité : réponses **fausses** mais mémorisables (« nom de jeune fille de ta mère » → ne pas répondre la vraie ; répondre une chaîne aléatoire stockée dans le gestionnaire).
- Contacts de récupération (Apple « Account Recovery Contacts ») : choisir précautionneusement.

## 29.4 Sessions actives et appareils

Tous les services majeurs proposent une vue « appareils connectés » ou « sessions actives ». À auditer mensuellement :

- Quelles sessions sont actives ?
- Sur quels appareils, depuis où, depuis quand ?
- Y a-t-il des sessions inconnues ?
- Révoquer les sessions inactives ou suspectes.

## 29.5 Anti-SIM swap

Le SIM swap consiste, pour un attaquant, à convaincre ton opérateur de lui donner ta ligne sur sa SIM. Tous les SMS et appels arrivent chez lui. La récupération de comptes par SMS devient sienne. Cas documentés en Belgique, France, US, partout.

Défenses :

- **PIN opérateur** : pour appeler ton opérateur et faire un changement de SIM, exiger ce PIN. À mettre en place auprès de l’opérateur, à mémoriser, à ne jamais réutiliser.
- **eSIM** : moins facile à transférer (lié à un appareil, opérations généralement à distance avec auth forte).
- **MVNO sérieux** : certains opérateurs sont plus stricts sur les procédures.
- **Filtre par questions** : tes informations de contact sécurité avec l’opérateur ne sont pas dérivables d’OSINT.

## B. Mots de passe et coffres

## 29.6 Unicité > complexité mémorisée

L’ère du « mot de passe complexe à mémoriser » est révolue. Un mot de passe par service, généré aléatoirement, stocké dans un gestionnaire. C’est la seule approche soutenable :

- **Unicité** : la réutilisation est la première cause de compromission de comptes. Quand un service fuite (et il fuitera), tous tes autres comptes avec le même mot de passe tombent.
- **Longueur > complexité** : 20+ caractères aléatoires > 8 caractères « complexes ». Un gestionnaire les génère.
- **Mot de passe maître** : ton unique mot de passe humainement mémorisable. Doit être long, unique, aléatoire dans une certaine mesure. Phrase de passe Diceware (6-8 mots aléatoires) recommandé.

## 29.7 Gestionnaires : Bitwarden, KeePassXC, 1Password, Proton Pass

- **Bitwarden** : open source, freemium, cloud par défaut (auto-hébergement via Vaultwarden possible). Audits Cure53 réguliers. Standard pour la plupart.
- **KeePassXC** : open source, 100 % local. Base chiffrée à synchroniser manuellement si multi-appareil (Syncthing, Nextcloud, Dropbox+Cryptomator). Pour profils techniques privacy-maximalistes.
- **1Password** : commercial, propre, cloud propre. Bonne UX. Audits réguliers. Canadien (juridiction acceptable). Plan famille.
- **Proton Pass** : nouveau, intégré à Proton, alias email intégrés.

**Anti-recommandation** : LastPass, après les fuites de 2022-2023 (compromission des coffres clients, exfiltration des données chiffrées qui permettent un brute-force offline). À éviter.

## 29.8 Vaultwarden self-hosted

**Vaultwarden** est une réimplémentation serveur compatible avec les clients Bitwarden. Auto-héberger sur un VPS ou un serveur domestique te donne :

- Contrôle total des données chiffrées.
- Latence faible.
- Pas de dépendance à un fournisseur externe.

Coût : maintenance technique (mises à jour, sauvegardes du serveur, monitoring). Si tu n’es pas en mesure de gérer cela, Bitwarden cloud est préférable.

## 29.9 KDF : Argon2id, scrypt, PBKDF2

La **Key Derivation Function** transforme ton mot de passe maître en clé de chiffrement. Sa résistance détermine la difficulté du brute-force offline en cas de fuite du coffre.

- **Argon2id** : référence 2025, résistant aux ASIC et GPU. À privilégier.
- **scrypt** : bonne alternative, plus ancienne.
- **PBKDF2** : ancienne génération, moins résistante. Par défaut historique de Bitwarden, qui a migré vers Argon2id en option en 2023.

Configurer son gestionnaire avec Argon2id et paramètres élevés (mémoire ≥ 64 MB, itérations ≥ 3, parallélisme ≥ 4). Compromis : un déverrouillage plus lent (quelques secondes) mais beaucoup plus de résistance.

## C. MFA, passkeys et clés physiques

## 29.10 MFA : hiérarchie de sécurité

|MFA                                         |Sécurité                              |Recommandation              |
|--------------------------------------------|--------------------------------------|----------------------------|
|**SMS**                                     |Faible (SIM swap, MITM)               |À éviter                    |
|**Email**                                   |Faible (cascade si mail compromis)    |À éviter                    |
|**TOTP** (Authenticator, Aegis, Raivo)      |Bon                                   |Acceptable                  |
|**Push notification** (Microsoft, Duo)      |Bon, mais vulnérable à « MFA fatigue »|Acceptable                  |
|**FIDO2 / WebAuthn**                        |Excellent (résistant phishing)        |**Recommandé**              |
|**Clé matérielle FIDO2** (YubiKey, Nitrokey)|Excellent (hardware-bound)            |**Recommandé pour critique**|

## 29.11 Passkeys

**Passkeys** sont l’implémentation grand public de WebAuthn. Une passkey est une paire de clés cryptographiques, stockée sur ton appareil (ou dans un trousseau cloud E2EE), qui s’authentifie auprès d’un service sans mot de passe.

Deux types :

- **Synchronisées** (via iCloud Keychain, Google Password Manager, Bitwarden, 1Password) : disponibles sur tous tes appareils, mais dépendantes du trousseau.
- **Device-bound** (sur clé physique FIDO2) : ne sortent jamais de la clé. Maximum de sécurité.

Adoption en 2025-2026 : Google, Apple, Microsoft, GitHub, Amazon, beaucoup d’autres supportent. Migration progressive.

## 29.12 Clés physiques : YubiKey, Nitrokey, SoloKey

- **YubiKey 5 series** : référence commerciale. Multiples protocoles (FIDO2/WebAuthn, FIDO U2F, OTP, OpenPGP smartcard, PIV). Pas open source côté firmware. Différents form factors (USB-A, USB-C, NFC).
- **Nitrokey 3** : open source matériel et logiciel. Allemagne. Bon pour profil sensible/transparence.
- **SoloKey** : open source, plus militante. Adoption modeste.

**Stratégie à deux clés** : toujours avoir une clé principale et une clé de secours, enregistrées toutes deux sur tes comptes critiques. La principale au quotidien, la secondaire dans un coffre. La perte d’une clé est gérable si la seconde existe.

## 29.13 Procédure en cas de compromission

Tu suspectes ton compte compromis :

1. **Changer immédiatement le mot de passe** depuis un appareil sain.
1. **Révoquer toutes les sessions actives**.
1. **Audit des modifications récentes** : email de récupération changé ? Filtre mail nouveau qui efface des notifications ? Méthodes MFA ajoutées par un tiers ?
1. **Vérifier les logs** (Google Account → Activité, Apple ID → Appareils, etc.).
1. **Si compromission confirmée du gestionnaire de mots de passe** : changer *tous* les mots de passe critiques, considérer le coffre comme exposé.
1. **Communication** : prévenir les contacts si phishing depuis ton compte ; déclarer aux plateformes ; déposer plainte si pertinent.

-----
