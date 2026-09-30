---
title: Annexe 1 — Glossaire (120+ termes)
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Annexes
  - index.md
---

**A**

**ADINT (Advertising Intelligence)** — Exploitation de l’écosystème publicitaire numérique comme source de renseignement. Utilise notamment le ciblage publicitaire, le RTB, les identifiants publicitaires mobiles, les données de localisation et les bidstream data pour profiler, suivre ou cibler des personnes ou groupes. Les données publicitaires peuvent produire un risque physique ou opérationnel : identification d’agents, domiciles, trajets, lieux sensibles, patterns of life..

**AFU (After First Unlock)** — État d’un appareil mobile après le premier déverrouillage depuis allumage. Beaucoup de clés sont en mémoire ; vulnérabilité forensique élevée par rapport à BFU.

**Advanced Data Protection (ADP)** — Mode iCloud chiffrant en E2EE la majorité des données (Drive, photos, sauvegardes, notes, signets). Hors-périmètre : mail, contacts, calendrier. Nécessite tous les appareils Apple à jour et une clé de récupération.

**Adversary** — Acteur dont les actions contre toi sont à anticiper. Caractérisé par capacité, motivation, probabilité.

**Adversary of proximity** — Adversaire proche (ex-conjoint, harceleur, employeur intrusif). Faible capacité technique typique, mais forte connaissance préalable.

**Air gap** — Isolation physique d’un système (aucune connexion réseau). Mesure forte pour secrets long terme, coûteuse au quotidien.

**AmneziaVPN** — Client VPN open source multi-protocoles permettant d’utiliser Amnezia Premium ou de déployer un VPN self-hosted sur un VPS. Pertinent surtout pour l’anti-censure, le contournement de DPI et les configurations utilisant AmneziaWG, XRay Reality, Shadowsocks ou OpenVPN over Cloak.

**AmneziaWG** — Fork de WireGuard conçu pour rendre le trafic plus difficile à détecter et bloquer par des systèmes de DPI. Utile en environnement censuré, mais ne transforme pas un VPN en réseau d’anonymat.

**AppArmor** — Modèle de Mandatory Access Control sous Linux (Debian, Ubuntu, SUSE). Profils par application.

**APT (Advanced Persistent Threat)** — Acteur étatique ou paraétatique avec capacité, ressource et patience pour campagnes ciblées longues.

**Argon2id** — Fonction de dérivation de clé (KDF) moderne, résistante aux ASIC. À privilégier dans gestionnaires de mots de passe et FDE.

**Attribution** — Conclusion qu’une action est l’œuvre de telle personne ou entité. Niveau de confiance variable.

**B**

**BFU (Before First Unlock)** — État d’un appareil après redémarrage, avant déverrouillage. La plupart des clés sont scellées. Forensiquement le plus protecteur.

**Bidstream data** — Données transmises dans l’écosystème publicitaire lors des enchères en temps réel : appareil, IP, localisation, contexte, application, langue, horaires, segments d’intérêt, etc. Ces données peuvent être utilisées à des fins publicitaires, mais aussi détournées à des fins de renseignement.

**BEC (Business Email Compromise)** — Fraude par usurpation d’identité d’un dirigeant pour demande de virement. Pertes mondiales en milliards.

**BlackLotus** — Bootkit UEFI (2022-2023) contournant Secure Boot via signature vulnérable. Illustre que Secure Boot n’est pas inviolable.

**Bridge (Tor)** — Relais Tor non publié, utilisé pour contourner le blocage des relais publics dans pays censurés.

**C**

**C2PA (Coalition for Content Provenance and Authenticity)** — Standard de provenance cryptographique pour images/vidéos.

**Canvas fingerprint** — Technique de fingerprinting basée sur le rendu d’une image cachée. Variations GPU et drivers produisent signature unique.

**Capitalisme de surveillance** — Modèle économique fondé sur la collecte et exploitation massive de données personnelles.

**Chat Control / CSAR** — Proposition de règlement UE visant le scan des communications avant E2EE. Bloqué depuis 2022 en négociation.

**Cold boot attack** — Extraction de clés depuis la RAM peu après extinction (mémoire persiste quelques secondes).

**Compartmentation (compartimentation)** — Architecture défensive consistant à séparer les activités en compartiments étanches.

**Contact Key Verification** — Mécanisme iMessage (iOS 17.2+) de vérification cryptographique des clés contacts.

**Coreboot** — Firmware open source remplaçant les firmwares constructeur sur certains matériels.

**Corrélation (surface de)** — Ensemble des points par lesquels deux identités ou activités peuvent être reliées.

**Cryptomator** — Outil de chiffrement de dossier côté client, transparent, multi-plateforme.

**D**

**Dangerzone** — Outil FPF qui reconvertit un PDF en PDF propre via conteneur isolé, supprimant tout contenu actif et métadonnée.

**Deepfake** — Contenu synthétique (image, vidéo, audio) généré par IA, imitant une personne réelle.

**Disposable VM (dispVM)** — VM Qubes éphémère, créée à la demande, détruite à la fermeture.

**DKIM (DomainKeys Identified Mail)** — Signature cryptographique des emails par domaine émetteur, pour vérifier authenticité.

**DMARC (Domain-based Message Authentication, Reporting and Conformance)** — Politique de validation email combinant SPF et DKIM, avec gestion des échecs.

**DoH / DoT (DNS over HTTPS / DNS over TLS)** — Protocoles de DNS chiffré, à privilégier pour confidentialité des résolutions.

**Double ratchet** — Algorithme combinant forward secrecy et post-compromise security. Base de Signal Protocol.

**Doxxing** — Publication malveillante d’informations personnelles identifiantes sur une cible.

**DRM (Digital Rights Management)** — Hors périmètre privacy mais souvent confondu. Note : certains DRM (Widevine, etc.) collectent des données.

**E**

**E2EE (End-to-End Encryption)** — Chiffrement bout en bout : seuls expéditeur et destinataire peuvent lire le contenu.

**ECH (Encrypted Client Hello)** — Extension TLS qui chiffre le SNI dans le ClientHello.

**EXIF (Exchangeable Image File Format)** — Métadonnées intégrées aux photos (GPS, modèle, date).

**ExifTool** — Outil de référence pour lire/écrire les métadonnées de fichiers.

**Evil maid** — Attaque par accès physique temporaire (typiquement chambre d’hôtel) modifiant l’appareil.

**F**

**FDE (Full Disk Encryption)** — Chiffrement complet du disque (BitLocker, FileVault, LUKS).

**FIDO2 / WebAuthn** — Standard d’authentification cryptographique forte, base des passkeys.

**Fingerprint (navigateur)** — Signature unique dérivée des caractéristiques de ton navigateur et appareil.

**Forward secrecy** — Propriété cryptographique : la compromission d’une clé ne permet pas de déchiffrer le passé.

**fwupd** — Outil Linux pour mises à jour firmware via le LVFS.

**G**

**GrapheneOS** — OS Android durci et dégooglisé, sur Pixel exclusivement.

**Guard (Tor)** — Premier relais d’un circuit Tor, connaît ton IP réelle.

**H**

**Hardening (durcissement)** — Renforcement de la configuration sécurité d’un système.

**HaveIBeenPwned** — Service de référence pour identifier si un email/téléphone apparaît dans des fuites publiques.

**Heads** — Firmware sécurisé basé sur Coreboot, avec vérification cryptographique au démarrage.

**HVT (High Value Target)** — Cible à forte valeur pour adversaire ressourcé.

**I**

**IDFA / AAID** — Identifiants publicitaires iOS et Android. Désactivables.

**IMSI catcher** — Faux relais cellulaire captant les IMSI à proximité (Stingray, DRT box).

**IOC (Indicator of Compromise)** — Marqueur technique permettant d’identifier une compromission.

**iVerify** — Application de monitoring de sécurité iOS/Android, détection de spyware connus.

**K**

**KDF (Key Derivation Function)** — Fonction transformant un mot de passe en clé cryptographique. Argon2id, scrypt, PBKDF2.

**Killswitch (VPN)** — Interruption du trafic si le tunnel VPN tombe. Indispensable.

**L**

**LCEN** — Loi française de 2004 consacrant la liberté de cryptographie pour usage personnel.

**LinkedIn (réseau social)** — Plateforme professionnelle, source OSINT majeure.

**Linkability** — Possibilité de relier deux activités à la même entité (dimension LINDDUN).

**LINDDUN** — Taxonomie de menaces privacy (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Noncompliance).

**Lockdown Mode (iOS)** — Mode haute sécurité iOS désactivant des fonctionnalités exploitées par spyware mercenaires.

**LogoFAIL** — Vulnérabilité firmware (2023) dans le parsing d’images au démarrage, contournant Secure Boot.

**LUKS** — Standard Linux de chiffrement de disque.

**M**

**MAC randomization** — Génération d’adresses MAC aléatoires par les OS modernes pour réduire le tracking Wi-Fi/BT.

**MAID (Mobile Advertising ID)** — Identifiant publicitaire mobile. IDFA sur iOS, AAID sur Android. Conçu pour le ciblage publicitaire, mais exploitable comme pivot de corrélation dans des scénarios ADINT.

**Malvertising** — Usage de publicités en ligne pour diffuser du contenu malveillant, rediriger vers un site piégé ou préparer une attaque ciblée.

**Mandatory Access Control (MAC)** — Modèle de contrôle d’accès obligatoire (AppArmor, SELinux).

**Matrix** — Protocole de messagerie fédérée open source.

**MAT2 (Metadata Anonymisation Toolkit v2)** — Outil de nettoyage de métadonnées de fichiers.

**Mercenary spyware** — Spyware vendu commercialement à des États (Pegasus, Predator, Graphite).

**Mixnet** — Réseau d’anonymisation qui mélange les flux, ajoute de la latence et parfois du bruit réseau pour réduire l’analyse de trafic. Différent de Tor : Tor route en oignon avec trois relais ; un mixnet cherche surtout à réduire la corrélation temporelle et volumétrique.

**MFA (Multi-Factor Authentication)** — Authentification multifacteurs. Hiérarchie : FIDO2 > TOTP > SMS.

**Mullvad** — Fournisseur VPN suédois, référence privacy. Sans compte utilisateur.

**MVT (Mobile Verification Toolkit)** — Outil Amnesty pour détecter spyware (Pegasus, Predator) dans sauvegardes mobiles.

**N**

**Need-to-know** — Principe : partager une information sensible uniquement avec ceux qui en ont besoin pour leur rôle.

**Nextcloud** — Cloud auto-hébergé open source.

**NymVPN** — VPN décentralisé basé sur l’écosystème Nym. Propose un mode Fast en deux sauts et un mode Anonymous en cinq sauts via mixnet avec ajout de bruit. Pertinent pour la protection contre l’analyse de métadonnées réseau, avec un coût en latence selon le mode.

**O**

**OnionShare** — Outil de partage de fichiers via service onion temporaire.

**OPSEC (Operational Security)** — Discipline d’identification, contrôle et protection des indicateurs sensibles.

**OSINT (Open Source Intelligence)** — Collecte d’information via sources ouvertes.

**OSINT défensif** — Audit de soi-même par OSINT pour mesurer son exposition publique.

**P**

**Passkey** — Implémentation grand public de WebAuthn (clés cryptographiques remplaçant les mots de passe).

**Pegasus** — Spyware mercenaire de NSO Group, déployé contre journalistes, activistes, opposants.

**PGP / GPG** — Standard de chiffrement asymétrique pour email et fichiers.

**Phishing** — Tentative d’usurpation pour obtenir credentials ou exécution. Variantes : spear, whaling, smishing, vishing, quishing.

**Pluton (Microsoft)** — Coprocesseur de sécurité Microsoft intégré dans CPU récents.

**Post-compromise security (PCS)** — Capacité d’un protocole à se rétablir après compromission de clé.

**Predator** — Spyware mercenaire d’Intellexa/Cytrox, concurrent de Pegasus.

**Proton (Mail, Drive, VPN)** — Suite suisse de services E2EE par design.

**Pseudonymat** — Usage d’un nom de substitution stable. Distinct de l’anonymat.

**Q**

**Qubes OS** — OS basé Xen compartimentant chaque activité en VMs séparées.

**R**

**Recall (Microsoft)** — Fonctionnalité Windows 11 sur Copilot+ PCs, opt-in, capturant régulièrement l’écran et indexant le contenu par IA pour recherche ultérieure. Snapshots et index stockés localement, chiffrés et liés à la TEE. Controversée pour les implications privacy structurelles d’une telle base.

**Ring signature** — Primitive cryptographique de Monero pour masquer l’expéditeur.

**RGPD** — Règlement Général sur la Protection des Données (UE).

**RTB (Real-Time Bidding)** — Système d’enchères publicitaires en temps réel. Lorsqu’un utilisateur ouvre une page ou une application, des informations sur son profil publicitaire sont transmises à des annonceurs potentiels, qui enchérissent automatiquement pour afficher une publicité.

**S**

**Safety Numbers (Signal)** — Chaîne dérivée des clés permettant de vérifier l’identité d’un contact.

**Sandbox** — Isolement d’une application dans un environnement contrôlé (Flatpak, Firejail, Windows Sandbox).

**Sapin II** — Loi française de protection des lanceurs d’alerte (2016, modifiée 2022).

**Secure Boot** — Vérification cryptographique de la chaîne de démarrage UEFI.

**Secure Enclave** — Coprocesseur de sécurité Apple intégré aux SoC Apple Silicon.

**SecureDrop** — Plateforme open source pour soumission anonyme de documents aux rédactions.

**SELinux** — Modèle MAC sous Linux (Fedora, RHEL).

**SimpleX** — Messagerie E2EE sans identifiant utilisateur global.

**SIM swap** — Fraude consistant à faire transférer ta ligne sur la SIM d’un attaquant.

**Signal** — Référence E2EE, protocole open source audité, déployé à 100M+ utilisateurs.

**SNI (Server Name Indication)** — Extension TLS qui transmet en clair le nom de domaine joint.

**Snowflake** — Transport obfusqué Tor utilisant des proxys volontaires WebRTC.

**Spoofing** — Usurpation d’identité (catégorie STRIDE).

**Stalkerware** — Logiciel espion commercial visant le tracking de partenaires (mSpy, FlexiSpy).

**STRIDE** — Taxonomie de menaces sécurité (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).

**Stylométrie** — Analyse statistique du style d’écriture pour identification d’auteur.

**Surface d’attaque** — Ensemble des points par lesquels un adversaire peut t’attaquer techniquement.

**Surface d’exposition** — Ensemble des informations collectables sur toi sans attaque.

**Surveillance, capitalisme de** — Cf. capitalisme de surveillance.

**T**

**Tails** — OS live amnésique routant tout via Tor.

**Threat model** — Modèle structuré décrivant actifs, adversaires, mesures.

**TLS (Transport Layer Security)** — Protocole de chiffrement en transit, base de HTTPS.

**Tor** — Réseau d’anonymisation par routage en oignon à trois sauts.

**TOTP (Time-based One-Time Password)** — Code MFA généré par algorithme synchronisé en temps (Authenticator apps).

**TPM (Trusted Platform Module)** — Coprocesseur de sécurité pour stockage de clés et mesure de boot.

**Truecaller** — Service tiers révélant les identités derrière numéros de téléphone (intrusif).

**V**

**Vanadium** — Navigateur intégré à GrapheneOS, Chromium durci.

**Vault qube** — Qube Qubes offline pour secrets (gestionnaire de mots de passe, clés PGP).

**Vault7 (Wikileaks)** — Fuite de capacités CIA (2017), illustre capacités étatiques.

**VeraCrypt** — Conteneur chiffré portable, héritier de TrueCrypt.

**Vishing** — Phishing par appel vocal.

**VLAN (Virtual LAN)** — Segmentation réseau logique.

**VPN (Virtual Private Network)** — Tunnel chiffré vers serveur distant.

**Vulnerability** — Faiblesse exploitable d’un système.

**W**

**Wayland** — Protocole de gestion d’affichage Linux remplaçant X11, avec isolation des fenêtres.

**WebAuthn** — Standard d’authentification web cryptographique.

**Whaling** — Spear phishing visant un dirigeant.

**Whonix** — OS d’anonymisation Tor en architecture Gateway/Workstation.

**WireGuard** — Protocole VPN moderne, rapide, compact.

**Y**

**Yellow dots** — Micro-points jaunes invisibles imprimés par imprimantes couleur pour tracking forensique.

**YubiKey** — Clé matérielle FIDO2 / WebAuthn / OpenPGP.

**Z**

**Zed!** — Conteneur chiffré francophone, secteur public/justice.

**Zero-click** — Exploit nécessitant aucune interaction utilisateur (typique des spywares mercenaires sur iMessage, WhatsApp).

**Zero-day** — Vulnérabilité non publique, sans patch disponible.

-----
