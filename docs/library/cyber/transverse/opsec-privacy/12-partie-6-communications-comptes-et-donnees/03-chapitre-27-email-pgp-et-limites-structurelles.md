---
title: Chapitre 27 — Email, PGP et limites structurelles
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

## 27.1 Pourquoi l’email est intrinsèquement mauvais pour la confidentialité

L’email a 50 ans. Il a été conçu avant la confidentialité moderne. Conséquences structurelles :

- **Métadonnées en clair** : expéditeur, destinataire, objet, horodatage. Tous visibles à chaque relais.
- **Transit en clair entre serveurs** : si l’expéditeur ou le destinataire utilise un service sans TLS systématique, le mail circule en clair sur certains hops. TLS opportuniste signifie « si possible » ; MTA-STS et DANE améliorent, sans garantir.
- **Pas de chiffrement par défaut** : sauf si tu utilises PGP/S-MIME (qui couvrent le contenu mais pas l’objet et pas les métadonnées).
- **Pas de forward secrecy** : la compromission de ta clé PGP permet de relire tous tes mails passés.

L’email reste indispensable (interopérabilité universelle). Pour les communications réellement sensibles, il faut autre chose (Ch 26 ou 28).

## 27.2 SMTP, headers, métadonnées

Un email arrive avec des en-têtes :

- `From`, `To`, `Cc`, `Date`, `Subject` (objet).
- `Received` : chaîne de serveurs traversés, avec IPs et horodatages — utile en forensique mais révèle ton parcours.
- `X-Originating-IP` : sur certains fournisseurs, ton IP au moment de l’envoi.
- `Message-ID`, `References` : identifiants uniques.
- `User-Agent` : ton client mail.

Tout ceci est visible à tout intermédiaire.

## 27.3 PGP / GPG : modèle, utilité, complexité

**PGP** (Pretty Good Privacy) ou son équivalent libre **GPG** chiffre le contenu d’un message avec la clé publique du destinataire. Modèle de confiance : *web of trust* (chaque utilisateur certifie les clés d’autres en qui il a confiance).

**Utilité** : pour communications sensibles entre parties techniques. Pour signature de logiciels, signature de mails, vérification d’identité.

**Limites majeures** :

- **Pas de forward secrecy** : la clé privée compromise expose toute la correspondance.
- **Complexité opérationnelle** : génération, gestion d’expiration, révocation, distribution. La plupart des utilisateurs s’y perdent.
- **Erreurs structurelles documentées** : EFAIL (2018) a montré qu’une mauvaise intégration côté client peut permettre exfiltration via images chargées.
- **Métadonnées non protégées** : objet, expéditeur, destinataire, horodatage restent en clair.
- **UX hostile** : presque toutes les implémentations grand public ont des frottements importants.

**Pour qui** : profils techniques qui peuvent vraiment maintenir une stack PGP. Pour les autres, Signal/SimpleX est mille fois préférable.

## 27.4 PGP en pratique

Outils :

- **Thunderbird** : intégration PGP native depuis 78+, avec gestion du trousseau, signature, chiffrement, vérification.
- **gpg en CLI** : pour profils techniques, complet.
- **Smartcards / clés matérielles** : YubiKey, Nitrokey supportent PGP. Clé privée jamais sur l’ordinateur, opérations cryptographiques sur la carte. Pour profil sensible : génération sur air gap (Ch 13), import sur Smartcard.

Cycle de vie d’une clé PGP :

1. Génération sur machine sûre (idéalement air gap), 4096 bits RSA ou Ed25519.
1. Sous-clés séparées pour signature et chiffrement, sous-clés avec expiration courte (1 an).
1. Sauvegarde de la clé maître en lieu sûr, hors ligne.
1. Diffusion de la clé publique (keyserver, site web, GitHub, mails de signature).
1. Renouvellement annuel des sous-clés.
1. Révocation prête à l’emploi en cas de compromission.

## 27.5 Proton Mail, Tuta, Mailbox.org, Fastmail

- **Proton Mail** : Suisse, E2EE entre comptes Proton (transparent pour l’utilisateur), bridging IMAP/SMTP local pour clients tiers, alias, hébergement sous juridiction protectrice. Modèle freemium. Audit Cure53. Référence pour la plupart.
- **Tuta (anciennement Tutanota)** : Allemagne, E2EE de bout en bout (y compris objet, ce que ne fait pas Proton historiquement). Recherche dans mails chiffrés côté client. Pas de support IMAP (limite).
- **Mailbox.org** : Allemagne, focalisé service mail propre et stable, bon support PGP.
- **Fastmail** : Australie, juridiction moins idéale (Five Eyes), mais excellent service et propre. Pas d’E2EE par défaut.

**Pour qui** : Proton ou Tuta pour profil privacy. Mailbox.org si tu veux du PGP propre dans un service européen sérieux.

## 27.6 Alias email

Un **alias** est une adresse email qui forwarde vers ta vraie adresse, sans révéler celle-ci.

- **SimpleLogin** (acquis par Proton) : adresses aléatoires ou personnalisées, gestion par projet. Intégré dans Proton si tu y es.
- **Addy.io** (anciennement Anonaddy) : open source, similaire.
- **Hide My Email** (Apple) : intégré iCloud+, alias par site.
- **DuckDuckGo Email Protection** : gratuit, transformation des trackers en plus du forward.

**Usage** : un alias par service. Quand le service fuite (et il fuitera), tu sais lequel a fuité, tu peux le retirer, et ton email principal reste intact.

## 27.7 Architecture multi-emails

Une bonne architecture email :

- **Email principal nominatif** : seulement pour services administratifs et professionnels critiques. Jamais utilisé ailleurs.
- **Email admin secondaire** : pour comptes utilitaires (services publics, opérateurs).
- **Email pro public** : pour ta présence professionnelle visible.
- **Email pseudonyme** : pour ton compartiment pseudonyme stable, si applicable.
- **Aliases par service** : pour tout le reste (commerce, newsletters, inscriptions).

Le centre de gravité (Ch 4 et Ch 29) est l’email principal. Sa protection prime.

## 27.8 Chiffrement de pièces jointes quand PGP exclu

Si ton destinataire ne sait pas utiliser PGP : chiffrer la pièce jointe avant envoi.

- **Cryptomator** : conteneur dossier (Ch 30), partageable comme dossier zippé.
- **7z avec mot de passe** : universellement lisible, AES-256, mot de passe partagé hors bande.
- **Zed!** : conteneurs auto-extractibles chiffrés (cas francophone, secteur public, justice). Le destinataire reçoit un exécutable qui demande un mot de passe pour extraire — pratique pour non-techniques. Mot de passe transmis par SMS, appel, hors bande.

Le mot de passe **ne doit pas circuler par email**. C’est l’erreur de débutant classique.

## 27.9 OPSEC email

- **Never reply** : ne pas répondre directement à un mail sensible (laisse une trace de la conversation). Plutôt initier un nouveau canal (Signal, appel).
- **Objets neutres** : pas « Documents confidentiels Acme Corp » mais « Suite à notre conversation ».
- **Signatures professionnelles** : standard, sans révéler l’organigramme interne.
- **Pas de footer corporatif systématique** sur les comptes pseudonymes.

## 27.10 *Fil rouge* — Léa configure son écosystème email

Léa migre :

- **Email principal Gmail** → Proton Mail, avec migration progressive (notification de nouvel email aux contacts important sur 3 mois). Gmail reste actif comme « catch-all » pour les services anciens, et désactivé pour récupérations d’autres services.
- **Aliases SimpleLogin** : un par service nouveau.
- **Email pro public** : `lea.martens@[domaine du consortium]`, hébergé par eux, PGP activé.
- **Email pseudonyme** : nouveau compte Proton, jamais croisé avec l’identité civile (créé via Tor, depuis Tails, paiement Monero).

Une semaine de configuration. Un mois pour stabiliser les habitudes.

-----
