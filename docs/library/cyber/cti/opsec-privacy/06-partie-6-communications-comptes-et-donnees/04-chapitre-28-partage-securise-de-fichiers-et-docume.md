---
title: Chapitre 28 — Partage sécurisé de fichiers et documents
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

## 28.1 OnionShare

**OnionShare** crée un service onion temporaire sur ton ordinateur. Tu choisis un fichier ou dossier, OnionShare génère une adresse `.onion`. Tu communiques cette adresse à ton destinataire, qui télécharge via Tor Browser. Le transfert est :

- Direct (P2P en pratique, via Tor).
- Anonyme côté serveur (tu) et côté client (destinataire).
- Temporaire (le service tombe à la fermeture).

**Cas d’usage** : envoi de documents par un journaliste à un correspondant, par un lanceur d’alerte. Très utile et sous-utilisé.

**Limites** : ton ordinateur doit rester allumé pendant le transfert ; le destinataire doit avoir Tor Browser ; vitesse limitée par Tor.

## 28.2 SecureDrop

**SecureDrop** est une plateforme open source pour rédactions, permettant aux lanceurs d’alerte de soumettre anonymement des documents. Initialement conçue par Aaron Swartz et Kevin Poulsen sous le nom DeadDrop, reprise et durcie par la *Freedom of the Press Foundation* (FPF) à partir de 2013, elle est devenue le standard de facto pour les soumissions anonymes aux médias.

**Architecture** : trois machines distinctes, isolées physiquement.

- **Source server** : serveur public accessible *uniquement* via une adresse `.onion` Tor. Reçoit les soumissions, les chiffre par GPG vers la clé publique de la rédaction.
- **Journalist workstation** : utilisée par les journalistes pour consulter (en lecture seule) les soumissions chiffrées via une connexion authentifiée.
- **Secure viewing station (SVS)** : machine air-gapped où les documents sont déchiffrés et examinés. Connectée à aucun réseau. Tails par défaut. Les transferts depuis la journalist workstation se font par USB neuve.

**Cas d’usage documentés** : Le Monde, Mediapart, The Guardian, The Intercept, The Washington Post, The New York Times, Süddeutsche Zeitung, ProPublica, USA Today, AP, Bloomberg, NPR, et plusieurs dizaines d’autres rédactions opèrent un SecureDrop. La liste publique est maintenue sur https://securedrop.org/directory/.

**Workflow source** :

1. La source télécharge Tor Browser depuis https://torproject.org sur un appareil qu’elle considère propre.
1. Elle se rend à l’URL `.onion` du SecureDrop de la rédaction (URL communiquée publiquement par la rédaction sur son site, vérifiable).
1. À la première visite, le système génère un nom de code unique (codename) à mémoriser ou noter de manière sécurisée. Ce codename remplace toute identité — le système ne demande aucune info personnelle.
1. La source soumet documents et message. Tout est chiffré côté serveur avec la clé publique de la rédaction.
1. La source peut revenir ultérieurement (avec son codename) pour recevoir des réponses des journalistes.

**Workflow journaliste** :

1. Connexion à la journalist workstation, authentification.
1. Téléchargement des soumissions chiffrées.
1. Passage des fichiers sur USB neuve vers la SVS air-gapped.
1. Déchiffrement et examen sur la SVS, dans Tails.
1. Réponse éventuelle à la source via le codename (sans connaître son identité).

**Limites** :

- Déploiement complexe (matériel dédié, formation, maintenance). Pas pour une rédaction isolée sans budget cyber.
- Latence d’usage (consultation des soumissions sur machine air-gap).
- Pas pour particulier — c’est une infrastructure organisationnelle.
- L’identité de la source reste vulnérable à des erreurs OPSEC côté source (utilisation depuis le bureau, métadonnées des documents non purgées, etc.). SecureDrop protège le canal, pas l’OPSEC opérationnelle de la source.

**Pour qui** : rédactions et ONG sérieuses ; soutien FPF disponible pour le déploiement initial. **Pour une source qui veut joindre une rédaction qui a SecureDrop** : utiliser leur lien `.onion` officiel via Tor Browser, idéalement depuis Tails, depuis un lieu non identifiable, en respectant les principes OPSEC du Capstone 3.

## 28.3 GlobaLeaks

**GlobaLeaks** est l’équivalent open source pour ONG, autorités anti-corruption, structures juridiques. Modèle similaire à SecureDrop, déploiement plus accessible.

**Exemples** : Whistleblowing Italia, plusieurs structures européennes anti-corruption.

## 28.4 CryptPad

**CryptPad** est un suite collaborative chiffrée de bout en bout. Édition de documents (texte, tableur, présentations, kanban, code, formulaires) sans que le serveur ne lise le contenu. Open source, instance officielle française (CryptPad.fr) hébergée par XWiki, auto-hébergement possible.

**Pour qui** : collaboration sensible (rédaction d’une note avec une source, ONG, journalistes en équipe). Excellent positionnement E2EE pour des cas où Google Docs n’est pas envisageable.

## 28.5 Liens temporaires

Pour partage one-shot non sensible :

- **Bitwarden Send** : intégré au gestionnaire de mots de passe Bitwarden, fichier ou texte chiffré, expiration configurable. Limite gratuite à 500 MB par fichier (1 GB pour Premium).
- **Firefox Send (mort)** : Mozilla a retiré le service en 2020.
- **0bin, PrivateBin** : pour partager du texte / code, E2EE côté client, paste sites auto-hébergeables.

Tous ces outils sont **chiffrés côté client** : la clé est dans l’URL (fragment après `#`), jamais envoyée au serveur.

## 28.6 Chiffrement avant envoi

Quand tu utilises un canal non confiance (email, cloud, partage de fichier), chiffrer avant envoi. La hiérarchie :

- **GPG asymétrique** si destinataire l’utilise.
- **Conteneur Cryptomator** ou **VeraCrypt** pour gros volumes, mot de passe transmis hors bande.
- **7z avec mot de passe AES-256** pour cas généralistes.
- **Zed!** pour secteur public francophone.

## 28.7 Vérification d’intégrité

Quand tu reçois un fichier important d’une source, vérifier qu’il n’a pas été modifié :

- Hash SHA-256 calculé par la source et envoyé hors bande (Signal, vocal).
- Comparaison locale : `sha256sum fichier.pdf` (Linux/macOS), `Get-FileHash` (PowerShell).
- Si correspondance, intégrité confirmée.

## 28.8 Menaces liées aux documents reçus

Un PDF reçu peut contenir :

- JavaScript malveillant.
- Exploits de visionneuses (Adobe Reader a un long historique).
- Pixels traceurs (en cas d’ouverture en ligne).
- Métadonnées qui révèlent l’auteur, le logiciel, l’environnement.

Procédure défensive :

1. **Jamais ouvrir dans le client mail** (preview désactivée).
1. **Téléverser dans un environnement isolé** (VM jetable, Tails, dispVM Qubes).
1. **Passer par Dangerzone** pour produire un PDF propre.
1. **Auditer les métadonnées** avec ExifTool ou MAT2 (Ch 31).

## 28.9 *Fil rouge* — Léa met en place un point de contact OnionShare

Léa annonce sur son site professionnel (page « Comment me joindre confidentiellement ») :

- Sa clé PGP publique.
- Le lien `.onion` de son SecureDrop personnel (déployé avec aide technique d’un confrère).
- Son numéro Signal (username, pas son téléphone).
- Une mention claire : « Pour documents sensibles, contactez-moi d’abord, on choisit le canal ».

Le canal Signal sert au premier contact ; OnionShare/SecureDrop pour les transferts effectifs.

-----
