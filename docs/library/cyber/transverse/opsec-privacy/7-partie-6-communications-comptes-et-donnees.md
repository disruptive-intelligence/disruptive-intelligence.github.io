---
title: Partie 6 — Communications, comptes et données
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 7
chapters: 8
---

> **Objectif** : protéger l’information à l’usage, au transit, au repos. Cette partie est la plus dense parce qu’elle couvre ce qui sera utilisé tous les jours.

-----

## Chapitre 25 — Cryptographie appliquée aux communications

### 25.1 Chiffrement de bout en bout (E2EE) : promesse et limites

L’**E2EE** signifie : seul l’émetteur et le destinataire peuvent lire le contenu. Les serveurs intermédiaires (fournisseur de messagerie, opérateur, FAI) voient du chiffré indéchiffrable. C’est la propriété fondatrice de Signal, WhatsApp (contenu), iMessage (avec Contact Key Verification), Proton Mail (côté E2EE entre comptes Proton), etc.

**Ce que l’E2EE protège** : le *contenu* des messages contre les intermédiaires.

**Ce que l’E2EE ne protège pas** :

- Les **métadonnées** (qui parle à qui, quand, combien).
- Les **endpoints** : un téléphone compromis lit les messages en clair après déchiffrement local.
- Le **destinataire** : si la personne avec qui tu parles fait une capture d’écran ou transfère, l’E2EE n’y change rien.
- Les **sauvegardes non chiffrées** : WhatsApp sauvegardé sur iCloud sans chiffrement, c’est le contenu en clair côté Apple/Google.

### 25.2 Forward secrecy

La **forward secrecy** (PFS) garantit qu’une clé compromise *aujourd’hui* ne permet pas de déchiffrer les messages *du passé*. Chaque session/message utilise une clé éphémère dérivée d’un échange Diffie-Hellman, puis détruite.

Sans forward secrecy : si l’attaquant capte aujourd’hui ta clé privée, il peut déchiffrer toutes tes communications passées qu’il aurait stockées en attendant. C’est exactement ce que font certaines agences avec leur stratégie « collect now, decrypt later ».

**Signal Protocol** (utilisé par Signal, WhatsApp, Wire) implémente la forward secrecy par double ratchet. **PGP/GPG** ne l’implémente pas (cf. Ch 27, l’une des grandes limites de PGP).

### 25.3 Post-compromise security

La **post-compromise security** (PCS) ou *future secrecy* : si l’attaquant a compromis ta clé à un moment T, le protocole peut « se réparer » : un nouvel échange de clés rétablit la confidentialité pour les messages futurs.

Le double ratchet de Signal combine forward secrecy et PCS. C’est l’état de l’art en 2025.

### 25.4 Deniability

La **deniability** (déniabilité) : tu peux nier de manière crédible avoir envoyé un message, parce que le protocole ne produit pas de preuve cryptographique irréfutable d’authorship. OTR (Off-the-Record) historique l’implémentait fortement. Signal Protocol l’implémente partiellement.

**Pour qui c’est important** : lanceurs d’alerte, sources, témoins. Si tu reçois une menace ou une preuve, tu ne veux pas qu’on puisse prouver mathématiquement qui te l’a envoyée. Pour la majorité, c’est un détail.

### 25.5 Métadonnées de communication

Le vrai enjeu opérationnel. Une messagerie peut avoir une E2EE parfaite et révéler massivement :

- Numéro de téléphone (identifiant).
- Carnet d’adresses uploadé sur le serveur.
- Horodatage de chaque message.
- Type (texte, image, audio, fichier) et taille.
- Statut en ligne, dernière connexion.

Hiérarchie 2025 sur la réduction de métadonnées :

1. **SimpleX** : pas d’identifiant utilisateur du tout.
1. **Briar** : peer-to-peer via Tor, pas de serveur central.
1. **Signal** : sealed sender, minimisation côté serveur, mais numéro de téléphone toujours requis (atténué par les usernames depuis 2024).
1. **Matrix (auto-hébergé)** : tu contrôles ton serveur, mais les métadonnées y sont visibles à l’admin (toi).
1. **WhatsApp** : contenu E2EE, métadonnées chez Meta.
1. **iMessage** : E2EE, métadonnées chez Apple (avec ADP, certaines plus protégées).

### 25.6 Vérification d’identité des contacts

L’E2EE ne sert à rien si tu communiques avec un imposteur. Les protocoles modernes proposent une vérification :

- **Safety Numbers (Signal)** : une chaîne de 60 chiffres dérivée des clés. À comparer manuellement, en personne ou par canal hors bande (vocal, vidéo). Si elle change, tu es alerté.
- **Contact Key Verification (iMessage)** : depuis iOS 17.2. Vérification cryptographique des clés iMessage entre contacts.
- **Fingerprints PGP** : à comparer hors bande.

Ces vérifications sont *à faire activement* pour les contacts critiques. La plupart des gens ne le font jamais. Pour un journaliste avec une source : c’est non négociable.

### 25.7 Compromission des endpoints

Le chiffrement E2EE ne sauve pas un appareil compromis. Si ton téléphone est infecté par Pegasus, l’attaquant lit Signal en clair après déchiffrement local — comme toi.

C’est pourquoi la sécurité des appareils (Ch 14-15) et la détection de compromission (Ch 33) priment sur le choix de la messagerie. Une messagerie parfaitement chiffrée sur un téléphone compromis = aucune protection.

### 25.8 Renvoi croisé

Le détail des primitives cryptographiques (AES, ECDH, double ratchet, etc.) est dans le cours dédié à la cryptographie de la bibliothèque. Ce chapitre s’arrête au niveau des propriétés, suffisant pour choisir des outils.

-----

## Chapitre 26 — Messageries chiffrées

> **Niveau de posture (cf. Ch 2.6)** : Signal pour tout + WhatsApp avec sauvegarde E2EE activée pour cercle qui ne migrera pas = **Niveau 1**. Signal avec username + iMessage avec Contact Key Verification pour cercle Apple + SimpleX pour quelques contacts particulièrement sensibles = **Niveau 2**. SimpleX comme canal primary + Signal sur GrapheneOS profil dédié + Briar pour offline / manifestations + vérification active des Safety Numbers en personne pour tous les contacts critiques = **Niveau 3**.

### 26.1 Anatomie d’une messagerie chiffrée

À évaluer pour chaque option :

- Protocole de chiffrement et ses propriétés (E2EE par défaut ou opt-in ? Forward secrecy ? Open source ?).
- Identifiant utilisateur requis (numéro, email, pseudonyme, rien).
- Métadonnées exposées au serveur.
- Juridiction du fournisseur.
- Audits indépendants.
- Maturité et adoption (réseau utile).

### 26.2 Signal

**Référence E2EE depuis 2014**. Signal Protocol open source, audité, déployé à 100+ millions d’utilisateurs. Propriétés :

- E2EE par défaut.
- Forward secrecy et PCS via double ratchet.
- Sealed sender : minimise l’information dont le serveur dispose (l’expéditeur d’un message ne lui est visible que sous certaines conditions).
- Numéros de téléphone historiquement requis ; depuis 2024, les **usernames** permettent de partager un identifiant de contact sans révéler le numéro. À comprendre précisément : **l’enregistrement initial du compte requiert toujours un numéro de téléphone** (lié à une SIM/eSIM, donc à un opérateur, donc en pratique à une identité civile dans la plupart des juridictions européennes). Ce que les usernames changent, c’est le partage de l’identifiant entre utilisateurs : tu peux donner ton @username à un nouveau contact sans lui dévoiler ton numéro. **Mais** les personnes qui ont déjà ton numéro dans leur carnet d’adresses continuent de te voir associé à ce numéro selon les réglages côté serveur Signal et le contexte. Pour réduire encore cette exposition, dans les paramètres Signal : « Téléphone » → « Qui peut me trouver par mon numéro » → *Personne*. Cela découple le numéro de la découverte sociale, mais l’enregistrement reste numérocentrique.
- **Disappearing messages** : expiration automatique configurable par conversation.
- **Safety Numbers** : vérification d’identité.

**Limites** :

- Service centralisé : Signal Foundation, basée aux États-Unis. Subpoena possible mais Signal a prouvé en justice ne posséder presque aucune donnée à fournir.
- L’enregistrement nécessite encore un numéro de téléphone (lié à un compte SIM, donc à un opérateur, donc à une identité).
- Apple/Google Play Store : la version officielle passe par eux ; alternative sur le site Signal pour Android.

**Pour qui** : tout le monde. C’est le minimum de l’hygiène 2025-2026.

### 26.3 SimpleX

**Modèle radicalement différent** : pas d’identifiant utilisateur global. Tu communiques via des liens de connexion ou QR codes que tu partages. Aucune base centrale ne sait que tu existes.

**Propriétés** :

- E2EE par défaut (double ratchet, similaire à Signal).
- **Pas de carnet d’adresses uploadé**.
- **Pas de numéro de téléphone** requis.
- Architecture en relais : tu choisis tes serveurs (incluant possibilité d’auto-hébergement).

**Contraintes** :

- UX moins fluide que Signal pour le grand public.
- Cercle social plus restreint (effet réseau plus faible).
- Découverte de nouveaux contacts par échange de lien (frottement à chaque nouvelle relation).

**Pour qui** : journalistes-sources, lanceurs d’alerte, profils où le numéro de téléphone est une corrélation à éviter absolument.

### 26.4 Briar

**Architecture P2P**, sans serveur central. Communications via Tor (par défaut) ou Bluetooth/Wi-Fi local (hors-ligne). Conçu pour environnements répressifs et coupures réseau.

**Cas d’usage** : manifestation, contexte sans internet, isolement réseau. Avec Briar, deux téléphones en proximité Bluetooth peuvent communiquer même sans aucun internet.

**Limites** : pas d’historique cloud, donc perte de téléphone = perte de tout. UX plus complexe. Pas d’appels (que des messages texte et forums).

### 26.5 Matrix / Element

**Décentralisé fédéré**. Chaque utilisateur a un compte sur un *homeserver* (hébergeur). Les homeservers fédèrent : tu peux échanger entre serveurs comme avec email.

**Propriétés** :

- E2EE possible (à activer par salon).
- Auto-hébergement possible (synapse, dendrite).
- Pas de numéro de téléphone requis.

**Limites** :

- E2EE non par défaut historiquement (en train de changer, mais à vérifier).
- Métadonnées : ton homeserver voit tout. Si tu utilises matrix.org, c’est l’organisation Matrix.
- Complexité opérationnelle de l’auto-hébergement.
- Historique des messages côté serveur (selon configuration).

**Pour qui** : communautés open source, ONG avec capacité d’auto-héberger, équipes techniques.

### 26.6 WhatsApp

**Le plus utilisé au monde (~3 milliards d’utilisateurs)**. Signal Protocol (E2EE) pour le contenu des messages. Mais :

- Métadonnées chez Meta (relations, fréquences, timings, statut en ligne).
- Carnet d’adresses uploadé sur les serveurs Meta (par défaut).
- Sauvegardes iCloud/Google Drive **non E2EE par défaut**. À activer manuellement (« Sauvegarde chiffrée de bout en bout ») depuis 2021.
- Intégration profonde aux services Meta.

**Pour qui** : usage avec contacts qui ne migreront jamais ailleurs. Ne pas y faire transiter du sensible. Activer la sauvegarde E2EE.

### 26.7 Telegram

**Confusion fréquente**. Telegram n’est PAS E2EE par défaut. Seuls les **« Secret Chats »** le sont, et :

- Disponibles uniquement en 1-à-1, pas en groupe.
- Pas de synchronisation multi-appareil pour les Secret Chats.
- Protocole maison (MTProto) critiqué par les cryptographes.

Tous les autres chats Telegram (groupes, channels) sont chiffrés en transit *vers les serveurs Telegram*, qui peuvent les lire. Telegram a coopéré sélectivement avec des forces de l’ordre.

**Pour qui** : ne pas y faire transiter du sensible. Telegram est un outil de diffusion (canaux publics, larges groupes), pas une messagerie privée.

### 26.8 iMessage

E2EE par défaut pour les iMessage (textos entre iPhones). SMS classiques (vers Android) : non E2EE.

**Contact Key Verification** (iOS 17.2+) : vérifie cryptographiquement les clés de tes contacts iMessage. Indispensable pour HVT.

**Limites** :

- Écosystème Apple uniquement (avec RCS support partiel en 2024-2025 mais pas E2EE).
- Sauvegardes iCloud : non-E2EE sans ADP activée (Ch 14).
- Pas d’audit indépendant du protocole côté Apple.

**Pour qui** : utilisateurs Apple-only, avec ADP activée et Contact Key Verification. Acceptable pour conversation modérément sensible entre Apple/Apple.

### 26.9 Session, Threema, Wire

- **Session** : fork de Signal sans numéro de téléphone, route via réseau Loki (similaire à Tor). Modèle intéressant, adoption modeste.
- **Threema** : commercial suisse, payant unique, pas de numéro requis. Bonne réputation, niche.
- **Wire** : suisse également, support entreprise. Plus orienté pro.

### 26.10 Choix par threat model

|Profil                |Stack recommandée                                                           |
|----------------------|----------------------------------------------------------------------------|
|Grand public durci    |Signal pour tout, WhatsApp si nécessaire avec sauvegarde E2EE               |
|Journaliste-source    |SimpleX pour canal source, Signal pour le reste                             |
|Activiste avant action|Signal avec disappearing messages, Briar pour offline                       |
|Dirigeant exposé      |Signal + iMessage avec ADP, vérification active des contacts                |
|HVT                   |SimpleX + Signal sur GrapheneOS, vérification systématique, reboot quotidien|

### 26.11 OPSEC messagerie : pratiques

- **Disappearing messages** : activer par défaut sur conversations sensibles. Durée selon contexte (24h, 7 jours, 1 mois).
- **View-once** : pour photos/vidéos. Signal et WhatsApp supportent. Note : capture d’écran possible, défense imparfaite.
- **Safety Numbers** : vérifier en première rencontre avec contact sensible.
- **Audit des contacts** : périodiquement, qui a accès à quoi. Suppression des contacts non utilisés.
- **Notification preview** : désactiver sur écran verrouillé, ou minimiser (nom de l’expéditeur seulement, pas le contenu).

### 26.12 Chat Control / CSAR UE : état du débat 2025-2026

La proposition de règlement « Chat Control » (CSAR — Child Sexual Abuse Regulation) circule en Europe depuis 2022, avec des versions successives. L’idée centrale : obliger les fournisseurs de messageries à scanner les contenus *avant* chiffrement E2EE pour détecter du CSAM (matériel pédopornographique).

**Position des cryptographes** : techniquement impossible sans casser l’E2EE. Le scanning côté client (« client-side scanning ») revient à insérer une backdoor, accessible à toute partie qui contrôlerait le mécanisme à terme. Signal a indiqué qu’il se retirerait de l’UE plutôt que d’introduire un tel scanning. ProtonMail, Threema et la plupart des fournisseurs E2EE européens ont des positions similaires.

**État au moment de la rédaction (2026)** : le dossier reste mouvant et hautement politique. Le Conseil de l’UE a adopté en novembre 2025 une orientation générale ouvrant la porte à un scanning « volontaire » étendu et discutant de plusieurs options sur le scanning obligatoire. En mars 2026, le Parlement européen a soutenu l’extension temporaire de la dérogation ePrivacy (qui autorise déjà certains scans volontaires de contenus non E2EE) jusqu’en août 2027, afin d’éviter un vide juridique pendant que les négociations se poursuivent. Les positions nationales restent contrastées — certains États (notamment l’Allemagne et l’Autriche pendant plusieurs phases) ont exprimé des réserves fortes sur l’atteinte à l’E2EE ; d’autres (France, Espagne, Italie sur certaines périodes) ont soutenu une version exigeante. La présidence tournante du Conseil influence fortement le calendrier.

**Implication pratique pour le lecteur** :

- Le risque que l’E2EE européenne soit affaiblie n’est pas conjuré.
- Le calendrier exact et la forme finale (scanning obligatoire, volontaire étendu, ciblé seulement) restent ouverts.
- Suivi recommandé via *European Digital Rights* (EDRi, https://edri.org), *La Quadrature du Net*, *Patrick Breyer* (eurodéputé qui suit le dossier de près sur https://patrick-breyer.de), et *Center for Democracy & Technology*.
- Pour profils sensibles : ne pas baser sa stack uniquement sur des fournisseurs européens E2EE sans plan B (SimpleX, Briar, hébergement en Suisse hors UE, etc.).

### 26.13 *Fil rouge* — Léa et Karim choisissent SimpleX

Léa reçoit, via une rédaction tierce, un signal que Karim B. veut entrer en contact. Premier échange via une boîte morte ProtonMail. Léa propose : SimpleX, parce que ni Karim ni elle n’ont besoin de révéler leur numéro de téléphone. Karim installe SimpleX sur un téléphone d’occasion qu’il a acheté cash. Première rencontre numérique : Léa envoie un lien d’invitation via le canal ProtonMail. Connexion établie. Vérification : ils s’appellent par appel SimpleX et se lisent les Safety Numbers. Puis, basculement en disappearing messages 24h pour toute la conversation.

-----

## Chapitre 27 — Email, PGP et limites structurelles

### 27.1 Pourquoi l’email est intrinsèquement mauvais pour la confidentialité

L’email a 50 ans. Il a été conçu avant la confidentialité moderne. Conséquences structurelles :

- **Métadonnées en clair** : expéditeur, destinataire, objet, horodatage. Tous visibles à chaque relais.
- **Transit en clair entre serveurs** : si l’expéditeur ou le destinataire utilise un service sans TLS systématique, le mail circule en clair sur certains hops. TLS opportuniste signifie « si possible » ; MTA-STS et DANE améliorent, sans garantir.
- **Pas de chiffrement par défaut** : sauf si tu utilises PGP/S-MIME (qui couvrent le contenu mais pas l’objet et pas les métadonnées).
- **Pas de forward secrecy** : la compromission de ta clé PGP permet de relire tous tes mails passés.

L’email reste indispensable (interopérabilité universelle). Pour les communications réellement sensibles, il faut autre chose (Ch 26 ou 28).

### 27.2 SMTP, headers, métadonnées

Un email arrive avec des en-têtes :

- `From`, `To`, `Cc`, `Date`, `Subject` (objet).
- `Received` : chaîne de serveurs traversés, avec IPs et horodatages — utile en forensique mais révèle ton parcours.
- `X-Originating-IP` : sur certains fournisseurs, ton IP au moment de l’envoi.
- `Message-ID`, `References` : identifiants uniques.
- `User-Agent` : ton client mail.

Tout ceci est visible à tout intermédiaire.

### 27.3 PGP / GPG : modèle, utilité, complexité

**PGP** (Pretty Good Privacy) ou son équivalent libre **GPG** chiffre le contenu d’un message avec la clé publique du destinataire. Modèle de confiance : *web of trust* (chaque utilisateur certifie les clés d’autres en qui il a confiance).

**Utilité** : pour communications sensibles entre parties techniques. Pour signature de logiciels, signature de mails, vérification d’identité.

**Limites majeures** :

- **Pas de forward secrecy** : la clé privée compromise expose toute la correspondance.
- **Complexité opérationnelle** : génération, gestion d’expiration, révocation, distribution. La plupart des utilisateurs s’y perdent.
- **Erreurs structurelles documentées** : EFAIL (2018) a montré qu’une mauvaise intégration côté client peut permettre exfiltration via images chargées.
- **Métadonnées non protégées** : objet, expéditeur, destinataire, horodatage restent en clair.
- **UX hostile** : presque toutes les implémentations grand public ont des frottements importants.

**Pour qui** : profils techniques qui peuvent vraiment maintenir une stack PGP. Pour les autres, Signal/SimpleX est mille fois préférable.

### 27.4 PGP en pratique

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

### 27.5 Proton Mail, Tuta, Mailbox.org, Fastmail

- **Proton Mail** : Suisse, E2EE entre comptes Proton (transparent pour l’utilisateur), bridging IMAP/SMTP local pour clients tiers, alias, hébergement sous juridiction protectrice. Modèle freemium. Audit Cure53. Référence pour la plupart.
- **Tuta (anciennement Tutanota)** : Allemagne, E2EE de bout en bout (y compris objet, ce que ne fait pas Proton historiquement). Recherche dans mails chiffrés côté client. Pas de support IMAP (limite).
- **Mailbox.org** : Allemagne, focalisé service mail propre et stable, bon support PGP.
- **Fastmail** : Australie, juridiction moins idéale (Five Eyes), mais excellent service et propre. Pas d’E2EE par défaut.

**Pour qui** : Proton ou Tuta pour profil privacy. Mailbox.org si tu veux du PGP propre dans un service européen sérieux.

### 27.6 Alias email

Un **alias** est une adresse email qui forwarde vers ta vraie adresse, sans révéler celle-ci.

- **SimpleLogin** (acquis par Proton) : adresses aléatoires ou personnalisées, gestion par projet. Intégré dans Proton si tu y es.
- **Addy.io** (anciennement Anonaddy) : open source, similaire.
- **Hide My Email** (Apple) : intégré iCloud+, alias par site.
- **DuckDuckGo Email Protection** : gratuit, transformation des trackers en plus du forward.

**Usage** : un alias par service. Quand le service fuite (et il fuitera), tu sais lequel a fuité, tu peux le retirer, et ton email principal reste intact.

### 27.7 Architecture multi-emails

Une bonne architecture email :

- **Email principal nominatif** : seulement pour services administratifs et professionnels critiques. Jamais utilisé ailleurs.
- **Email admin secondaire** : pour comptes utilitaires (services publics, opérateurs).
- **Email pro public** : pour ta présence professionnelle visible.
- **Email pseudonyme** : pour ton compartiment pseudonyme stable, si applicable.
- **Aliases par service** : pour tout le reste (commerce, newsletters, inscriptions).

Le centre de gravité (Ch 4 et Ch 29) est l’email principal. Sa protection prime.

### 27.8 Chiffrement de pièces jointes quand PGP exclu

Si ton destinataire ne sait pas utiliser PGP : chiffrer la pièce jointe avant envoi.

- **Cryptomator** : conteneur dossier (Ch 30), partageable comme dossier zippé.
- **7z avec mot de passe** : universellement lisible, AES-256, mot de passe partagé hors bande.
- **Zed!** : conteneurs auto-extractibles chiffrés (cas francophone, secteur public, justice). Le destinataire reçoit un exécutable qui demande un mot de passe pour extraire — pratique pour non-techniques. Mot de passe transmis par SMS, appel, hors bande.

Le mot de passe **ne doit pas circuler par email**. C’est l’erreur de débutant classique.

### 27.9 OPSEC email

- **Never reply** : ne pas répondre directement à un mail sensible (laisse une trace de la conversation). Plutôt initier un nouveau canal (Signal, appel).
- **Objets neutres** : pas « Documents confidentiels Acme Corp » mais « Suite à notre conversation ».
- **Signatures professionnelles** : standard, sans révéler l’organigramme interne.
- **Pas de footer corporatif systématique** sur les comptes pseudonymes.

### 27.10 *Fil rouge* — Léa configure son écosystème email

Léa migre :

- **Email principal Gmail** → Proton Mail, avec migration progressive (notification de nouvel email aux contacts important sur 3 mois). Gmail reste actif comme « catch-all » pour les services anciens, et désactivé pour récupérations d’autres services.
- **Aliases SimpleLogin** : un par service nouveau.
- **Email pro public** : `lea.martens@[domaine du consortium]`, hébergé par eux, PGP activé.
- **Email pseudonyme** : nouveau compte Proton, jamais croisé avec l’identité civile (créé via Tor, depuis Tails, paiement Monero).

Une semaine de configuration. Un mois pour stabiliser les habitudes.

-----

## Chapitre 28 — Partage sécurisé de fichiers et documents

### 28.1 OnionShare

**OnionShare** crée un service onion temporaire sur ton ordinateur. Tu choisis un fichier ou dossier, OnionShare génère une adresse `.onion`. Tu communiques cette adresse à ton destinataire, qui télécharge via Tor Browser. Le transfert est :

- Direct (P2P en pratique, via Tor).
- Anonyme côté serveur (tu) et côté client (destinataire).
- Temporaire (le service tombe à la fermeture).

**Cas d’usage** : envoi de documents par un journaliste à un correspondant, par un lanceur d’alerte. Très utile et sous-utilisé.

**Limites** : ton ordinateur doit rester allumé pendant le transfert ; le destinataire doit avoir Tor Browser ; vitesse limitée par Tor.

### 28.2 SecureDrop

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

### 28.3 GlobaLeaks

**GlobaLeaks** est l’équivalent open source pour ONG, autorités anti-corruption, structures juridiques. Modèle similaire à SecureDrop, déploiement plus accessible.

**Exemples** : Whistleblowing Italia, plusieurs structures européennes anti-corruption.

### 28.4 CryptPad

**CryptPad** est un suite collaborative chiffrée de bout en bout. Édition de documents (texte, tableur, présentations, kanban, code, formulaires) sans que le serveur ne lise le contenu. Open source, instance officielle française (CryptPad.fr) hébergée par XWiki, auto-hébergement possible.

**Pour qui** : collaboration sensible (rédaction d’une note avec une source, ONG, journalistes en équipe). Excellent positionnement E2EE pour des cas où Google Docs n’est pas envisageable.

### 28.5 Liens temporaires

Pour partage one-shot non sensible :

- **Bitwarden Send** : intégré au gestionnaire de mots de passe Bitwarden, fichier ou texte chiffré, expiration configurable. Limite gratuite à 500 MB par fichier (1 GB pour Premium).
- **Firefox Send (mort)** : Mozilla a retiré le service en 2020.
- **0bin, PrivateBin** : pour partager du texte / code, E2EE côté client, paste sites auto-hébergeables.

Tous ces outils sont **chiffrés côté client** : la clé est dans l’URL (fragment après `#`), jamais envoyée au serveur.

### 28.6 Chiffrement avant envoi

Quand tu utilises un canal non confiance (email, cloud, partage de fichier), chiffrer avant envoi. La hiérarchie :

- **GPG asymétrique** si destinataire l’utilise.
- **Conteneur Cryptomator** ou **VeraCrypt** pour gros volumes, mot de passe transmis hors bande.
- **7z avec mot de passe AES-256** pour cas généralistes.
- **Zed!** pour secteur public francophone.

### 28.7 Vérification d’intégrité

Quand tu reçois un fichier important d’une source, vérifier qu’il n’a pas été modifié :

- Hash SHA-256 calculé par la source et envoyé hors bande (Signal, vocal).
- Comparaison locale : `sha256sum fichier.pdf` (Linux/macOS), `Get-FileHash` (PowerShell).
- Si correspondance, intégrité confirmée.

### 28.8 Menaces liées aux documents reçus

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

### 28.9 *Fil rouge* — Léa met en place un point de contact OnionShare

Léa annonce sur son site professionnel (page « Comment me joindre confidentiellement ») :

- Sa clé PGP publique.
- Le lien `.onion` de son SecureDrop personnel (déployé avec aide technique d’un confrère).
- Son numéro Signal (username, pas son téléphone).
- Une mention claire : « Pour documents sensibles, contactez-moi d’abord, on choisit le canal ».

Le canal Signal sert au premier contact ; OnionShare/SecureDrop pour les transferts effectifs.

-----

## Chapitre 29 — Comptes critiques, authentification et secrets

> **Note pédagogique** : ce chapitre est long. Il est structuré en trois sous-blocs majeurs : (A) comptes critiques et récupération, (B) mots de passe et coffres, (C) MFA, passkeys et clés physiques. Chacun peut être lu indépendamment, mais ensemble ils forment l’architecture d’authentification personnelle.

### A. Comptes critiques et récupération

### 29.1 L’email principal comme centre de gravité

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

### 29.2 Comptes pivots : Apple ID, Google, Microsoft

Selon l’écosystème, ces comptes contiennent : iCloud (photos, contacts, sauvegardes, mails, Keychain), Google (Gmail, Drive, photos, contacts, Android backup), Microsoft (OneDrive, Office, BitLocker recovery). Leur compromission = perte d’une grande partie de la vie numérique.

Mesures :

- Vérification en 2 étapes activée (FIDO2 idéalement).
- Clés de sécurité matérielles enregistrées.
- Mode protection avancée Google (Advanced Protection Program — pour cibles à risque).
- ADP iCloud activée.

### 29.3 Récupération de compte : le maillon faible

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

### 29.4 Sessions actives et appareils

Tous les services majeurs proposent une vue « appareils connectés » ou « sessions actives ». À auditer mensuellement :

- Quelles sessions sont actives ?
- Sur quels appareils, depuis où, depuis quand ?
- Y a-t-il des sessions inconnues ?
- Révoquer les sessions inactives ou suspectes.

### 29.5 Anti-SIM swap

Le SIM swap consiste, pour un attaquant, à convaincre ton opérateur de lui donner ta ligne sur sa SIM. Tous les SMS et appels arrivent chez lui. La récupération de comptes par SMS devient sienne. Cas documentés en Belgique, France, US, partout.

Défenses :

- **PIN opérateur** : pour appeler ton opérateur et faire un changement de SIM, exiger ce PIN. À mettre en place auprès de l’opérateur, à mémoriser, à ne jamais réutiliser.
- **eSIM** : moins facile à transférer (lié à un appareil, opérations généralement à distance avec auth forte).
- **MVNO sérieux** : certains opérateurs sont plus stricts sur les procédures.
- **Filtre par questions** : tes informations de contact sécurité avec l’opérateur ne sont pas dérivables d’OSINT.

### B. Mots de passe et coffres

### 29.6 Unicité > complexité mémorisée

L’ère du « mot de passe complexe à mémoriser » est révolue. Un mot de passe par service, généré aléatoirement, stocké dans un gestionnaire. C’est la seule approche soutenable :

- **Unicité** : la réutilisation est la première cause de compromission de comptes. Quand un service fuite (et il fuitera), tous tes autres comptes avec le même mot de passe tombent.
- **Longueur > complexité** : 20+ caractères aléatoires > 8 caractères « complexes ». Un gestionnaire les génère.
- **Mot de passe maître** : ton unique mot de passe humainement mémorisable. Doit être long, unique, aléatoire dans une certaine mesure. Phrase de passe Diceware (6-8 mots aléatoires) recommandé.

### 29.7 Gestionnaires : Bitwarden, KeePassXC, 1Password, Proton Pass

- **Bitwarden** : open source, freemium, cloud par défaut (auto-hébergement via Vaultwarden possible). Audits Cure53 réguliers. Standard pour la plupart.
- **KeePassXC** : open source, 100 % local. Base chiffrée à synchroniser manuellement si multi-appareil (Syncthing, Nextcloud, Dropbox+Cryptomator). Pour profils techniques privacy-maximalistes.
- **1Password** : commercial, propre, cloud propre. Bonne UX. Audits réguliers. Canadien (juridiction acceptable). Plan famille.
- **Proton Pass** : nouveau, intégré à Proton, alias email intégrés.

**Anti-recommandation** : LastPass, après les fuites de 2022-2023 (compromission des coffres clients, exfiltration des données chiffrées qui permettent un brute-force offline). À éviter.

### 29.8 Vaultwarden self-hosted

**Vaultwarden** est une réimplémentation serveur compatible avec les clients Bitwarden. Auto-héberger sur un VPS ou un serveur domestique te donne :

- Contrôle total des données chiffrées.
- Latence faible.
- Pas de dépendance à un fournisseur externe.

Coût : maintenance technique (mises à jour, sauvegardes du serveur, monitoring). Si tu n’es pas en mesure de gérer cela, Bitwarden cloud est préférable.

### 29.9 KDF : Argon2id, scrypt, PBKDF2

La **Key Derivation Function** transforme ton mot de passe maître en clé de chiffrement. Sa résistance détermine la difficulté du brute-force offline en cas de fuite du coffre.

- **Argon2id** : référence 2025, résistant aux ASIC et GPU. À privilégier.
- **scrypt** : bonne alternative, plus ancienne.
- **PBKDF2** : ancienne génération, moins résistante. Par défaut historique de Bitwarden, qui a migré vers Argon2id en option en 2023.

Configurer son gestionnaire avec Argon2id et paramètres élevés (mémoire ≥ 64 MB, itérations ≥ 3, parallélisme ≥ 4). Compromis : un déverrouillage plus lent (quelques secondes) mais beaucoup plus de résistance.

### C. MFA, passkeys et clés physiques

### 29.10 MFA : hiérarchie de sécurité

|MFA                                         |Sécurité                              |Recommandation              |
|--------------------------------------------|--------------------------------------|----------------------------|
|**SMS**                                     |Faible (SIM swap, MITM)               |À éviter                    |
|**Email**                                   |Faible (cascade si mail compromis)    |À éviter                    |
|**TOTP** (Authenticator, Aegis, Raivo)      |Bon                                   |Acceptable                  |
|**Push notification** (Microsoft, Duo)      |Bon, mais vulnérable à « MFA fatigue »|Acceptable                  |
|**FIDO2 / WebAuthn**                        |Excellent (résistant phishing)        |**Recommandé**              |
|**Clé matérielle FIDO2** (YubiKey, Nitrokey)|Excellent (hardware-bound)            |**Recommandé pour critique**|

### 29.11 Passkeys

**Passkeys** sont l’implémentation grand public de WebAuthn. Une passkey est une paire de clés cryptographiques, stockée sur ton appareil (ou dans un trousseau cloud E2EE), qui s’authentifie auprès d’un service sans mot de passe.

Deux types :

- **Synchronisées** (via iCloud Keychain, Google Password Manager, Bitwarden, 1Password) : disponibles sur tous tes appareils, mais dépendantes du trousseau.
- **Device-bound** (sur clé physique FIDO2) : ne sortent jamais de la clé. Maximum de sécurité.

Adoption en 2025-2026 : Google, Apple, Microsoft, GitHub, Amazon, beaucoup d’autres supportent. Migration progressive.

### 29.12 Clés physiques : YubiKey, Nitrokey, SoloKey

- **YubiKey 5 series** : référence commerciale. Multiples protocoles (FIDO2/WebAuthn, FIDO U2F, OTP, OpenPGP smartcard, PIV). Pas open source côté firmware. Différents form factors (USB-A, USB-C, NFC).
- **Nitrokey 3** : open source matériel et logiciel. Allemagne. Bon pour profil sensible/transparence.
- **SoloKey** : open source, plus militante. Adoption modeste.

**Stratégie à deux clés** : toujours avoir une clé principale et une clé de secours, enregistrées toutes deux sur tes comptes critiques. La principale au quotidien, la secondaire dans un coffre. La perte d’une clé est gérable si la seconde existe.

### 29.13 Procédure en cas de compromission

Tu suspectes ton compte compromis :

1. **Changer immédiatement le mot de passe** depuis un appareil sain.
1. **Révoquer toutes les sessions actives**.
1. **Audit des modifications récentes** : email de récupération changé ? Filtre mail nouveau qui efface des notifications ? Méthodes MFA ajoutées par un tiers ?
1. **Vérifier les logs** (Google Account → Activité, Apple ID → Appareils, etc.).
1. **Si compromission confirmée du gestionnaire de mots de passe** : changer *tous* les mots de passe critiques, considérer le coffre comme exposé.
1. **Communication** : prévenir les contacts si phishing depuis ton compte ; déclarer aux plateformes ; déposer plainte si pertinent.

-----

## Chapitre 30 — Cloud, sauvegardes et chiffrement côté client

### 30.1 Les trois états de la donnée

- **At rest** (au repos) : sur ton disque, sur un serveur cloud. Protégée par chiffrement disque/conteneur.
- **In transit** (en transit) : sur le réseau. Protégée par TLS/HTTPS.
- **In use** (en utilisation) : en RAM, déchiffrée, exploitable par un processus. Plus dur à protéger (TEE, enclaves matérielles).

Chaque état appelle des défenses différentes. Une chaîne complète doit traiter les trois.

### 30.2 Cloud par défaut : ce que Google Drive, OneDrive, Dropbox, iCloud peuvent lire

Sans précaution :

- **Google Drive** : Google peut lire (clé contrôlée par Google).
- **OneDrive** : Microsoft peut lire.
- **Dropbox** : Dropbox peut lire.
- **iCloud Drive** : Apple peut lire (sauf ADP activé).

Tous ces fournisseurs chiffrent les données au repos sur leurs serveurs (protection physique des serveurs), mais ils détiennent les clés. Conséquences :

- Réquisition judiciaire = accès complet.
- Faille interne ou attaquant qui compromet le fournisseur = accès complet.
- Politique de scanning automatique (CSAM, malware) = traitement du contenu.

### 30.3 Apple ADP : conditions et limites

Cf. Ch 14.6. Rappel : ADP active l’E2EE pour la majorité des données iCloud. Pas pour mail, contacts, calendrier.

**Conditions** : tous les appareils Apple à version récente, clé de récupération à conserver (perte = perte de données définitive).

**Pour qui** : tout utilisateur Apple avec données dans iCloud. À activer.

### 30.4 Cloud E2EE par design : Proton Drive, Tresorit, Mega

- **Proton Drive** : Suisse, E2EE par design, intégré écosystème Proton. Capacité variable selon plan.
- **Tresorit** : Suisse, E2EE par design, focalisé pro et entreprise, audits réguliers. Plus cher.
- **Mega** : Nouvelle-Zélande, E2EE par design. Capacité gratuite généreuse, historique controversé (Kim Dotcom) mais sécurité côté client réputée correcte.

**Pour qui** : utilisateurs voulant E2EE par défaut sans setup technique. Choisir selon juridiction et budget.

### 30.5 Chiffrement côté client par-dessus cloud généraliste

Tu veux garder Google Drive ou Dropbox pour des raisons d’écosystème, mais chiffrer ce que tu y mets ? Solutions :

- **Cryptomator** : conteneur de dossier transparent. Tu pointes Cryptomator vers un dossier dans Google Drive, il y crée une structure de fichiers chiffrés. Tu déverrouilles avec un mot de passe, ton OS voit un dossier monté. Multi-plateforme, open source, libre.
- **gocryptfs / EncFS** (Linux/macOS) : similaire, ligne de commande.
- **rclone + crypt backend** : pour scripts, sauvegardes automatisées vers cloud chiffré.

Tu peux utiliser le cloud que tu veux comme tu veux, et lui n’a plus accès au contenu. C’est l’option pragmatique pour beaucoup.

### 30.6 Nextcloud self-hosted

**Nextcloud** est un cloud privé auto-hébergé. Tu installes sur un VPS ou serveur domestique, tu as Drive + Calendrier + Contacts + Mail + plus.

**Avantages** : contrôle total, juridiction de ton choix, fonctionnalités étendues.

**Limites** :

- L’E2EE Nextcloud officielle a un historique mitigé. Pour E2EE sérieuse, combiner avec Cryptomator au-dessus.
- Maintenance technique nécessaire (mises à jour, sauvegardes, monitoring).
- Bande passante limitée à ta connexion.

### 30.7 Syncthing

**Syncthing** synchronise des dossiers entre appareils en peer-to-peer, sans cloud intermédiaire. Configuration sur chaque appareil, échange par identifiants. Chiffré bout-en-bout, open source.

Cas d’usage : sync notes entre laptop et téléphone sans aucun fournisseur tiers. Synchronisation continue.

### 30.8 Sauvegarde : règle 3-2-1

- **3 copies** des données importantes.
- **2 supports** différents (disque local + cloud, ou disque interne + externe).
- **1 hors site** (hors de chez toi).

Pour profils exposés : **3-2-1-1-0** ajoute :

- **1 sauvegarde immuable** (write-once, hors atteinte ransomware).
- **0 erreur** : tests de restauration réguliers.

### 30.9 Sauvegardes locales chiffrées

- **restic** : open source, déduplication, chiffrement par défaut. Backends multiples (local, S3, Backblaze B2, SFTP). Préférée pour script et automatisation.
- **Borg / BorgBackup** : similar à restic, déduplication efficace, communauté solide.
- **Time Machine** (macOS) + FileVault activé = sauvegarde chiffrée. Pratique pour utilisateurs Apple.
- **Windows Backup / File History** : moins puissant, OK pour basique.

### 30.10 Photos : sync auto et fuites

La synchronisation auto des photos vers iCloud/Google Photos remonte tout, avec EXIF, à chaque déclenchement. Pour profils sensibles :

- Désactiver la synchronisation auto.
- Tri manuel avant upload.
- Effacement EXIF avant publication (Ch 31).
- Pour photos sensibles d’enquête : jamais dans le cloud personnel.

### 30.11 Test de restauration

**La sauvegarde non testée n’existe pas**. Une fois par an au minimum : test de restauration complète sur appareil neuf. Sinon, tu découvres au moment critique que ton backup est corrompu, incomplet, ou inutilisable.

### 30.12 Sauvegarde des secrets

Clés PGP, codes de récupération, clé de récupération ADP, codes 2FA backup : ne pas oublier de sauvegarder.

Options :

- **Coffre matériel** : YubiKey backup avec mêmes clés que la principale.
- **Papier + coffre physique** : impression des codes, dans une enveloppe scellée, en coffre à la banque ou chez un avocat.
- **Cryptomator + cloud** : conteneur avec tous tes secrets, sauvegardé dans plusieurs clouds.

### 30.13 Plan en cas de perte ou vol

Préparé à l’avance :

1. **Effacement à distance** : Find My iPhone, Android Find My Device, Microsoft Find My Device.
1. **Révocation des sessions** sur tous les comptes.
1. **Désactivation des passkeys et certificats** liés à l’appareil.
1. **Notification de l’opérateur** pour bloquer la SIM si applicable.
1. **Déclaration de vol** (police, assureur).
1. **Restauration sur appareil neuf** depuis sauvegarde chiffrée.
1. **Audit** : changement préventif des mots de passe critiques si suspicion de compromission de l’appareil avant l’effacement.

-----

## Chapitre 31 — Métadonnées et nettoyage de fichiers

### 31.1 Métadonnées : ce que c’est

Les métadonnées sont les données qui décrivent les données. Souvent invisibles, presque toujours révélatrices. Elles s’agrègent silencieusement à chaque création de fichier, à chaque modification, à chaque transmission. Plus dangereuses parce que sous-estimées.

### 31.2 EXIF photo et métadonnées image étendues

Standard EXIF (Exchangeable Image File Format), embarqué dans la plupart des formats image (JPEG, TIFF, certains RAW) :

- **Coordonnées GPS** (latitude, longitude, altitude, parfois cap et vitesse au moment de la prise).
- **Date et heure** de prise, avec fuseau horaire.
- **Modèle d’appareil** et numéro de série de l’appareil (sur certains modèles haut de gamme, c’est un identifiant unique par appareil — un signal forensique fort).
- **Paramètres techniques** (ouverture, ISO, focale, exposition, balance des blancs).
- **Orientation** physique au moment de la prise (capteur gyroscopique).

**Métadonnées image étendues, souvent négligées** :

- **Profil ICC personnalisé** : si tu utilises un écran calibré ou un workflow professionnel, le profil ICC embarqué peut identifier ton matériel ou ton studio.
- **Vignettes** : mini-images embarquées dans la version finale. Si tu retouches une photo (par exemple pour caviarder un visage), la vignette peut conserver la version originale non retouchée. Plusieurs scandales journalistiques ont reposé sur cette erreur. ExifTool peut extraire les vignettes avec `exiftool -b -ThumbnailImage`.
- **XMP** (Extensible Metadata Platform) : couche métadonnées étendue, utilisée par Adobe et autres. Peut contenir auteur, copyright, historique de modifications, mots-clés ajoutés par le logiciel de gestion (Lightroom, Photo Mechanic).
- **Maker Notes** : zone propriétaire dans laquelle chaque constructeur (Canon, Nikon, Sony, Apple, Samsung) stocke des informations supplémentaires. Sur iPhone, Apple stocke des données HEIC qui incluent parfois l’orientation gyroscopique fine.
- **CRS (Camera Raw Settings)** : pour les fichiers RAW retouchés, peut révéler la version du logiciel utilisé.

**Cas réel** : John McAfee en 2012 — photo prise par un journaliste de *Vice* avec son iPhone, EXIF GPS intact, révèle au monde la localisation au Guatemala. Arrestation suivie dans les jours. Cf. Annexe 8.6.

**Cas moins connu** : plusieurs analystes d’OSINT ont géolocalisé des reportages de guerre en croisant l’angle du soleil dans la photo avec l’horodatage EXIF — sans même besoin du GPS, à condition que le téléphone n’ait pas modifié l’horloge.

### 31.3 PDF

- **Auteur**, **Producteur** (logiciel), **Créateur** (logiciel d’export), **Mots-clés**, **Sujet**.
- **Historique de révisions** : versions précédentes embarquées si non purgées.
- **Objets cachés** : commentaires invisibles, annotations, formulaires masqués.
- **XMP** (Extensible Metadata Platform) : couche métadonnées additionnelle.
- **JavaScript embarqué** : si présent, exécutable à l’ouverture.

### 31.4 Office (DOCX, XLSX, PPTX)

- **Auteur** initial et dernier modificateur.
- **Date de création**, dernière modification, dernière impression.
- **Commentaires** et suivi des modifications, parfois conservés sans en avoir conscience.
- **Texte caché** (formatage en blanc, sections masquées).
- **Vignettes** des slides PPTX.

Office propose un « Inspecter le document » qui retire la plupart, mais pas tout. Vérifier toujours après nettoyage.

### 31.5 Audio / vidéo

- **Tags ID3** sur MP3 : artiste, album, paroles, image cover.
- **Métadonnées MP4/MOV** : géolocalisation pour vidéos téléphoniques, gyroscope, codecs.
- **Traces de montage** : marqueurs invisibles laissés par certains logiciels.
- **Gyroscope iPhone vidéo** : peut révéler modèle d’iPhone exact.

### 31.6 Yellow dots : tracking imprimantes

**Cas Reality Winner, 2017** : analyste NSA, fuite d’un document classifié au média The Intercept. Le document est scanné et publié. Sur l’impression : des **micro-points jaunes** quasi invisibles à l’œil nu, formant un code dérivé de la **machine spécifique**, **date** et **heure** d’impression. Le FBI remonte à l’imprimante de la NSA, à l’heure d’impression, à Reality Winner. Arrestation en quelques jours.

**Mécanisme** : la quasi-totalité des imprimantes couleur professionnelles intègrent depuis les années 2000 un système de marquage forensique. Les patterns varient selon le constructeur, mais le principe est universel. Non documenté par les constructeurs, mais documenté par EFF (« Machine Identification Code »).

**Défense** :

- Pour publication anonyme : ne pas imprimer.
- Si impression nécessaire : imprimer dans des lieux multiples non identifiables, ou utiliser des imprimantes sans MIC (rares).
- Pour transmission de document scanné : ré-imprimer après scan via une voie qui retire les artefacts (re-générer le PDF depuis le contenu, jamais re-scanner).

### 31.7 Outils de nettoyage

- **MAT2** : Metadata Anonymisation Toolkit v2 (Tails inclut). Multi-format, automatique. `mat2 fichier.jpg` nettoie en place.
- **ExifTool** : référence pour lire et écrire métadonnées. Plus puissant, plus complexe. `exiftool -all= fichier.jpg`.
- **« Inspecter le document »** (Word, PowerPoint, Excel) : intégré, bon mais incomplet.
- **Acrobat Pro « Suppression d’informations cachées »** : payant mais efficace sur PDF.

### 31.8 Dangerzone

Cf. Ch 16. Méthode différente : reconversion complète du PDF dans un conteneur isolé, qui produit un PDF *nettoyé par reconstruction*. Plus radical que MAT2 (qui retire les métadonnées sur le fichier existant) parce qu’il *recrée* le fichier à partir de l’image rendue. Aucun objet caché, aucun JavaScript, aucune révision n’y survit.

### 31.9 Zed!

Cf. Ch 12. Conteneur chiffré auto-extractible, secteur public francophone. Utile pour transmettre un dossier complet à un correspondant non technique en environnement français.

### 31.10 Redaction destructive vs masquage

Pour caviarder un nom dans un PDF :

- **Mauvaise méthode** : rectangle noir par-dessus le texte dans Acrobat → le texte est toujours là, sous le rectangle. Copier-coller révèle.
- **Bonne méthode** : redaction destructive (Acrobat Pro propose, ou re-générer le PDF depuis source). Le texte est physiquement supprimé.

**Cas réel** : documents Manning publiés par Le Monde et The Guardian — premières versions avec caviardage non destructif, noms révélés par copier-coller. Correctifs et leçons apprises depuis.

### 31.11 Workflow avant publication

1. Travailler dans un environnement isolé si document sensible.
1. Avant export final : passer par Dangerzone (PDF) ou MAT2 (autres formats).
1. Vérifier visuellement : ouvrir le résultat dans un visualiseur différent, examiner les métadonnées.
1. Tester copier-coller du contenu : ce qui ne devrait pas y être ne doit pas y être.
1. Vérifier les vignettes embarquées.
1. **Ne jamais publier directement depuis le logiciel de création**.

### 31.12 *Fil rouge* — Léa nettoie un PDF et découvre un nom

Léa s’apprête à publier un document de l’enquête. Avant publication, application du workflow :

- Ouverture du PDF dans ExifTool : champ XMP « Author » contient le nom de la source. Erreur d’export.
- Vérification visuelle : tout est OK sur l’image.
- Vérification métadonnées : `exiftool -all` → champ « Producer » indique « Microsoft Word 2019 - Bureau de [nom de la source dans son administration] ». Si publié, identifie la source.
- Action : reconstruction via Dangerzone, vérification, publication.

Sans cette étape, la source aurait pu être identifiée par n’importe quel lecteur attentif.

-----

## Chapitre 32 — Paiements, traçabilité financière et cryptomonnaies

> **Cadre éditorial préalable** : ce chapitre est strictement éducatif et défensif. Il ne couvre pas le blanchiment, l’évasion fiscale, le contournement KYC ou la dissimulation d’origine illicite. Il aide à comprendre la traçabilité financière pour mieux protéger sa vie privée légitime, exercer sa liberté d’expression journalistique, ou se prémunir contre un harceleur exploitant tes traces de paiement.

### 32.1 Pourquoi le paiement est une fuite massive

Chaque transaction révèle :

- L’achat (objet, montant, lieu, heure).
- Le compte source (ton identité bancaire).
- Le compte destinataire (commerce, identité).
- Le contexte (carte fidélité ?, code postal, IP en ligne).

Agrégés, les paiements dessinent ta vie : où tu vis, où tu travailles, ce que tu manges, qui tu fréquentes, quelles consultations médicales tu as, quelles opinions tu soutiens (dons), quels médias tu consommes.

Les **banques** voient tout. Les **réseaux de paiement** (Visa, Mastercard) voient tout. Les **agrégateurs** (Plaid, Tink) si tu utilises des apps bancaires tierces voient tout. Les **commerçants** voient leurs achats, certains revendent.

### 32.2 Cartes et virements SEPA

CB classique : tracée intégralement, votre banque conserve l’historique.
Virement SEPA : motif transmis, libre. Traçabilité complète.
Prélèvement automatique : récurrence de fait, signal de relation contractuelle.

### 32.3 Cartes virtuelles

- **Revolut, N26, Lydia, Boursorama** : cartes virtuelles à usage unique ou jetables.
- **Privacy.com** (US) : cartes virtuelles à plafond, expirables.
- **Apple Card / Apple Pay** : tokenisation (le commerçant ne voit pas ton vrai numéro).

**Avantages** : limite la traçabilité commerciale, isole les fuites en cas de compromission du commerçant.
**Limites** : le fournisseur de la carte (Revolut, etc.) voit tout. Tu déplaces la confiance, tu ne l’élimines pas.

### 32.4 Cartes prépayées et cash en France/UE

L’achat anonyme de cartes prépayées avec montants substantiels n’est plus possible en UE depuis l’AMLD5 (2020) : KYC obligatoire au-delà de 150 € en physique, 50 € en ligne. AMLD6 a renforcé.

**Cash** : retrouve une valeur stratégique pour des achats que tu ne veux pas tracés. Limites légales : en France, les paiements professionnels > 1000 € sont interdits en cash ; entre particuliers, pas de limite spécifique mais déclaration au-delà de 10 000 €.

### 32.5 Cryptomonnaies : Bitcoin et Ethereum sont traçables

**Mythe à déconstruire** : Bitcoin et Ethereum ne sont **PAS** anonymes. Ils sont **pseudonymes**. Toutes les transactions sont publiques sur la blockchain. La société d’analyse Chainalysis et autres construisent des graphes complets liant adresses à identités via :

- Exchanges KYC-ed.
- Heuristiques d’analyse (multi-input, change address).
- Recoupement avec adresses connues.

**Cas réels** : nombreux ; les autorités américaines tracent quasi quotidiennement des transactions Bitcoin de criminalité.

### 32.6 Monero et Zcash

**Monero (XMR)** : confidentialité par défaut via ring signatures, stealth addresses, RingCT. Les transactions ne révèlent ni montant, ni expéditeur, ni destinataire. État actuel : pas d’analyse de chaîne efficace publiée à grande échelle (état de l’art 2025).

**Zcash (ZEC)** : confidentialité opt-in via zk-SNARKs (shielded addresses). Si tu utilises les shielded pools, confidentialité forte. Si tu utilises les transparent addresses, traçable comme Bitcoin.

**Limites réglementaires** :

- **MiCA** (Markets in Crypto-Assets) UE entré en vigueur 2024-2025 : transactions impliquant cryptomonnaies privacy-focused (Monero, Zcash shielded) seront plus restreintes sur exchanges régulés.
- **Travel Rule** : exchanges doivent partager certaines infos de bénéficiaires au-delà de seuils.
- **Delistings** : Monero retiré de Binance pour la plupart des marchés en 2024.

### 32.7 Cadre réglementaire 2025-2026

- **France** : déclaration de comptes crypto à l’étranger (formulaire 3916), imposition des plus-values, KYC sur exchanges français.
- **UE (MiCA)** : régulation harmonisée.
- **Sanctions** : adresses sanctionnées (OFAC US) inutilisables sur exchanges régulés.

### 32.8 La ligne rouge

Ce cours ne couvre **pas** :

- Le blanchiment d’argent.
- L’évasion fiscale.
- Le contournement délibéré de la procédure KYC.
- L’usage de cryptomonnaies pour dissimuler des activités illicites.

Tout cela est pénalement répréhensible.

Ce que ce cours couvre :

- Comprendre que tes paiements sont des données personnelles.
- Utiliser des moyens légaux pour limiter ta surface d’exposition financière commerciale (cash, cartes virtuelles, alias).
- Comprendre le cadre des cryptomonnaies pour des cas légitimes (don anonyme à un journaliste, soutien à une ONG dans un pays répressif, paiement d’un VPN par Monero parce que tu ne veux pas que ton VPN sache qui tu es).

### 32.9 Achats sensibles légitimes

Cas où limiter la traçabilité est légitime :

- **Santé** : consultations sensibles (IVG, addiction, santé mentale, IST).
- **Journalisme** : matériel pour mission, frais d’enquête.
- **Sécurité personnelle** : abonnement VPN, achat de matériel sécurité pour victime de violences.
- **Engagement politique** : adhésion partis, dons associatifs (les listes peuvent être indirectement révélées).
- **Recherche** : achat de livres, accès à bases qui révèlent un intérêt sensible.

### 32.10 Don anonyme à un journaliste / ONG

Plusieurs modèles légaux :

- **Cash en personne** : ancien et toujours fonctionnel.
- **Cash par courrier** : Mullvad VPN accepte (par exemple). Pour ONG, certaines aussi.
- **Cryptomonnaies** : Bitcoin avec wallet créé spécifiquement, jamais lié à exchange KYC. Monero pour confidentialité par défaut.
- **Intermédiaires** : certaines structures permettent dons anonymisés (fondations).

### 32.11 Paiement d’un VPN : le cas Mullvad, NymVPN et AmneziaVPN

Le paiement d’un VPN est une fuite OPSEC souvent ignorée. Si un utilisateur paie son VPN avec sa carte bancaire nominative, le fournisseur VPN ou son prestataire de paiement peut relier l’achat à une identité civile, même si le trafic réseau n’est pas journalisé.

**Mullvad VPN** est particulièrement intéressant sur ce point : le service utilise des comptes numérotés sans email et accepte le paiement en cash par courrier ainsi qu’en Monero. C’est l’une des approches les plus cohérentes pour réduire le lien entre identité civile, paiement et usage du VPN.

**NymVPN** met en avant une logique de paiement unlinkable via mécanismes zero-knowledge et accepte plusieurs cryptomonnaies. C’est cohérent avec son objectif général : réduire non seulement l’exposition IP, mais aussi les liens entre paiement, compte et usage réseau.

**AmneziaVPN** dépend du mode d’usage. Avec Amnezia Premium, l’utilisateur reste dans un modèle de fournisseur VPN classique. Avec Amnezia self-hosted, le paiement du VPN disparaît en partie, mais il est remplacé par le paiement du VPS. La fuite OPSEC peut donc simplement se déplacer vers l’hébergeur du serveur.

**Règle pratique** : pour un VPN privacy, le paiement doit être pensé comme une métadonnée sensible. Un VPN payé par carte bancaire nominative reste utile contre le FAI, mais il n’offre pas la même séparation qu’un compte payé en cash ou via une méthode mieux compartimentée.

-----

> 🟦 **Capstone 3 — Auditer et durcir une chaîne source-journaliste**
> 
> **Scénario** : Tu es journaliste. Une source potentielle veut entrer en contact pour transmettre des documents sensibles concernant un dossier de corruption. Tu n’as jamais communiqué avec elle. Comment structures-tu la chaîne complète, de la prise de contact à l’archivage des documents, en mobilisant les chapitres précédents ?
> 
> **Procédure attendue** :
> 
> 1. **Avant tout contact** : avoir un canal public annonçant comment te joindre confidentiellement (Ch 28). Publié sur ton site, redirigé depuis tes profils.
> 1. **Premier contact** : la source utilise ton canal annoncé. Idéal : SimpleX (numéros invisibles) ou SecureDrop si tu en as un. Mauvais : ton email professionnel public.
> 1. **Vérification d’identité** : avant de continuer, vérification mutuelle. Toi : preuve que tu es bien la journaliste annoncée (clé PGP signée, présence publique cohérente). La source : tu ne peux pas vérifier qu’elle est qui elle dit, mais tu peux évaluer la plausibilité (cohérence du récit, accès à des éléments non publics, recoupements).
> 1. **Canal stable** : après prise de contact, établir un canal pérenne. Signal avec usernames ou SimpleX. Vérifier les Safety Numbers en personne ou par canal hors bande (vocal — la voix est difficile à falsifier face à un humain qui la connaît, sauf deepfake).
> 1. **Compartimentation** : appareil dédié pour cette enquête (Ch 9, Ch 15). Pas ton téléphone perso. GrapheneOS sur Pixel ou iPhone séparé.
> 1. **Reception des documents** : via OnionShare ou via le canal Signal lui-même. Téléchargement dans environnement isolé (Tails ou dispVM Qubes).
> 1. **Vérification d’intégrité** : hash SHA-256 confirmé par la source hors bande.
> 1. **Sas de purification** : passage par Dangerzone pour les PDF. Nettoyage des métadonnées avec MAT2 ou ExifTool sur les autres formats.
> 1. **Archivage chiffré** : conteneur VeraCrypt ou Cryptomator sur disque externe. Stocké physiquement en coffre ou lieu sûr. Sauvegarde redondante dans cloud E2EE (Proton Drive).
> 1. **Audit avant publication** : nouveau passage MAT2 / ExifTool / Dangerzone sur tout document destiné à publication. Le caviardage est destructif. Vérification finale en environnement isolé.
> 1. **Communication post-publication** : préparation d’un canal pour suite (la source peut avoir besoin de soutien juridique, de mise à l’abri ; cf. lanceurs d’alerte Ch 37).
> 
> **Léa et Karim, fil rouge** : application complète de cette procédure sur trois mois. Karim transmet par paquets successifs. Chaque paquet suit le workflow. Trois mois après le premier contact, l’enquête est solidifiée, prête à publication. Cf. cas A en fin de cours.

-----
