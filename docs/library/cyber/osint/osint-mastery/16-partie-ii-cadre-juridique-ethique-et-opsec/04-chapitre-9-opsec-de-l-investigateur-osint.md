---
title: Chapitre 9 — OPSEC de l'investigateur OSINT
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE II — Cadre juridique, éthique et OPSEC
  - index.md
---

## 9.1 Pourquoi l'OPSEC

L'**OPSEC** (Operations Security, sécurité opérationnelle) est la discipline qui protège l'investigation et l'investigateur. Trois enjeux concrets.

**Protéger la mission.** Une cible qui détecte qu'elle est observée peut effacer ses traces, fuir, mettre en place des contre-mesures, ou alerter ses complices. L'OPSEC empêche la cible de remarquer l'investigation.

**Protéger l'investigateur.** Certaines cibles ont les moyens de retourner l'investigation contre l'enquêteur (criminels organisés, services étrangers, acteurs étatiques hostiles, harceleurs sophistiqués). L'OPSEC protège l'identité, le foyer, la famille, l'employeur de l'investigateur.

**Protéger les données.** Les données collectées sont sensibles (RGPD, contractuel, déontologique). Une fuite expose le commanditaire et la cible. L'OPSEC sécurise le stockage et la transmission.

## 9.2 Threat model — le concept central

L'OPSEC n'est pas une checklist universelle, c'est une **adaptation à la menace**. Le **threat model** est l'évaluation structurée de qui pourrait s'intéresser à votre investigation et avec quelles capacités.

**Questions du threat model.**

- Qui est la cible ? Quelles sont ses capacités techniques et financières ?
- A-t-elle des complices ? Quelles sont leurs capacités ?
- Y a-t-il des tiers (services d'État hostiles, groupes criminels) susceptibles d'intervenir ?
- Quelle est la valeur potentielle de la cible (qu'a-t-elle à perdre) ?
- Quels sont les vecteurs d'attaque réalistes contre l'investigateur ?
- Quelle est la durée de l'exposition ?

Un threat model rigoureux fait la différence entre une OPSEC adaptée et une OPSEC théâtrale (trop lourde pour rien) ou une OPSEC insuffisante (légère face à une menace réelle).

## 9.3 Catégories de menace

Quatre catégories types, à adapter à chaque cas.

**Cibles ordinaires.** Personne physique sans compétences techniques particulières, sans moyens financiers extraordinaires, sans réseau de complices. OPSEC légère suffit : navigateur dédié, VPN, comptes d'investigation. Délaunay du fil rouge MIRAGE rentre en partie dans cette catégorie initiale — mais sa compétence technique de DAF le rend plus sensible que la moyenne.

**Cibles sensibles.** Personnes avec ressources techniques (RSSI, ingénieurs sécurité), financières (chefs d'entreprise, fortunés), ou en position de pouvoir (élus, magistrats). OPSEC renforcée : VM dédiée, séparation stricte, OPSEC plateforme par plateforme.

**Cibles criminelles.** Organisations criminelles structurées, particulièrement crime organisé (mafia, cartels), groupes cybercriminels professionnels. Capacité à retourner l'investigation, à corrompre, à intimider. OPSEC forte : VM dédiée par enquête, Whonix, séparation infrastructure physique, anonymisation maximale.

**Cibles étatiques.** Services de renseignement étrangers, gouvernements hostiles, agences cyber étatiques. Capacités SIGINT, accès aux opérateurs télécom, capacité à monitorer Internet à grande échelle. OPSEC maximale : Tails sur clé USB, jamais de connexion depuis l'infrastructure habituelle, infrastructure dédiée et jetable. **Si vous êtes confronté à cette menace sans formation spécifique, vous transférez le dossier à un partenaire qualifié.**

## 9.4 Infrastructure d'investigation : VM, VPN, Tor

**Machine virtuelle (VM) dédiée par enquête** est le standard.

Avantages : isolation complète, possibilité de snapshot avant action sensible, destruction propre après mission, séparation entre identité d'investigateur et identité personnelle.

Outils : **VirtualBox** (gratuit, robuste), **VMware Workstation** (payant, plus performant), **QEMU/KVM** (Linux natif). Configuration recommandée : 4-8 Go RAM, 50-100 Go disque chiffré, snapshots à chaque étape clé.

**Systèmes d'exploitation.**

- **Ubuntu 24.04 LTS** : VM principale, bon compromis fonctionnalité/sécurité.
- **Tails** : Linux live amnésique sur clé USB, à utiliser pour les missions ponctuelles sensibles. Routage Tor par défaut.
- **Whonix** : architecture deux VM (Gateway Tor + Workstation), isolation forte. Pour les enquêtes nécessitant Tor de manière soutenue.
- **Qubes OS** : isolation par compartiments (qubes). Très robuste mais courbe d'apprentissage. Pour analystes avancés.

**VPN.**

- VPN **non corporate, sans logs vérifiés** par audit tiers (Mullvad, IVPN, Proton VPN avec parcimonie).
- Paiement anonyme si possible (crypto, espèces).
- Jamais le VPN personnel (qui peut remonter à l'identité civile).
- Vigilance sur les VPN gratuits — souvent compromis ou financés par exploitation des données utilisateurs.

**Tor.**

- Pour les cas de menace élevée.
- Tor Browser, **jamais d'identification personnelle** dans une session Tor.
- Performances dégradées (acceptable pour investigation, pas pour usage quotidien).
- Conscience des limites : Tor protège l'anonymat de connexion, pas le contenu si on s'identifie une fois connecté.

## 9.5 Navigateurs et empreinte

**Profil navigateur dédié.** Firefox ou Chromium avec profil isolé, jamais le profil personnel.

**Extensions sécurité.**

- **uBlock Origin** (blocage tracking).
- **NoScript** (contrôle JavaScript, à manier avec discernement).
- **Cookie AutoDelete** (purge des cookies à chaque session).
- **Privacy Badger** (anti-tracking heuristique).
- **CanvasBlocker** (lutte fingerprinting canvas).

**Empreinte navigateur (browser fingerprinting).** Au-delà des cookies, les sites identifient les visiteurs par la combinaison de paramètres (résolution, fonts, plugins, GPU, configuration audio). Tests : **AmIUnique**, **Cover Your Tracks** (EFF). En 2026, la déanonymisation par fingerprinting est mature — un profil unique vous identifie même sans cookie.

**Réflexes.**

- Profil minimaliste (peu d'extensions, configuration standard).
- Désactivation du WebRTC (peut révéler l'IP réelle même sous VPN).
- DNS chiffré (DoH ou DoT).
- Désactivation du géolocalisation, microphone, caméra par défaut.

## 9.6 DNS chiffré et fuites

Les requêtes DNS classiques sont visibles par votre FAI ou par un attaquant sur le réseau. Le DNS chiffré (**DoH** — DNS over HTTPS, ou **DoT** — DNS over TLS) le prévient.

**Configurations recommandées.**

- Cloudflare 1.1.1.1 (rapide, audit-friendly).
- Quad9 9.9.9.9 (filtrage malware par défaut).
- NextDNS (configurable, payant raisonnable).
- DNS auto-hébergé pour analystes avancés.

**Test de fuite.** `dnsleaktest.com`, `ipleak.net`. Vérifier régulièrement.

## 9.7 Stockage chiffré

Les données d'investigation doivent être chiffrées **au repos** et **en transit**.

**Au repos.**

- Disque chiffré complet : **LUKS** (Linux), **BitLocker** (Windows Pro), **FileVault** (macOS).
- Conteneurs chiffrés pour archives sensibles : **VeraCrypt** (multi-OS).
- Cloud chiffré côté client : **Cryptomator**, **Boxcryptor** (avant import dans cloud).
- Pas de stockage en clair, jamais.

**En transit.**

- Email chiffré : **PGP** via Thunderbird+Enigmail ou via **ProtonMail**.
- Messagerie chiffrée pour collaboration : **Signal** (à privilégier), **Wire**, **Element/Matrix**.
- Pas de transmission par WhatsApp pour sujets sensibles (chiffrement E2E mais propriété Meta).

**Gestion des clés.**

- Mot de passe maître robuste (gestionnaire type **Bitwarden**, **KeePassXC**).
- 2FA matériel pour les accès sensibles (clé YubiKey).
- Sauvegarde sécurisée des clés (coffre-fort, partage Shamir si critique).

## 9.8 Cloisonnement strict

Le **cloisonnement** entre identité personnelle, identité professionnelle générale, et identité d'investigation est central.

**Règles.**

- VM d'investigation **jamais** synchronisée avec compte cloud personnel.
- Email d'investigation **jamais** lié au téléphone personnel.
- Téléphone d'investigation séparé physiquement (SIM dédiée, IMEI distinct).
- Pas de copie-coller entre VM d'investigation et machine hôte (clipboard est un vecteur de fuite).
- Pas de USB partagée.
- Compte bancaire dédié pour les abonnements professionnels OSINT (DeHashed, PimEyes, etc.).

## 9.9 Téléphones d'investigation

Pour les investigations qui nécessitent une présence mobile (vérification compte SMS, app store country-specific, géolocalisation cible) :

- Téléphone **physiquement séparé** du téléphone personnel (idéalement modèle différent).
- **SIM prépayée** acquise en espèces (selon législation locale).
- **IMEI distinct** (ne pas réutiliser un ancien téléphone personnel).
- Profil système d'investigation, pas de comptes personnels.
- Géolocalisation désactivée par défaut, activée à la demande.
- Mode avion entre missions.
- Reset complet entre enquêtes critiques.

Légalité de la SIM prépayée : variable selon pays. En France, la SIM prépayée est désormais soumise à identification (loi sur les communications). Vérifier la conformité locale.

## 9.10 Gestion des mots de passe et 2FA

- **Gestionnaire de mots de passe** dédié (KeePassXC local, ou Bitwarden self-hosted pour les sensibles).
- Mots de passe **uniques par compte**, générés (16+ caractères aléatoires).
- **2FA matériel** pour les comptes critiques (YubiKey, Nitrokey).
- **2FA SMS à éviter** (SIM swapping possible).
- **Codes de récupération** stockés chiffrés.

## 9.11 Comptes d'investigation

Les comptes utilisés pour observer les plateformes (LinkedIn, X, Telegram) sont des **comptes d'investigation**, pas des comptes personnels. Pour leur création, voir Ch.11 (sock puppets).

**Règles minimales.**

- Email d'investigation (ProtonMail, Tutanota, ou domaine dédié).
- Téléphone d'investigation pour confirmation SMS si demandée.
- Pas d'informations personnelles dans la bio.
- Activité de maturation (quelques posts neutres, abonnements neutres) avant utilisation pour investigation.
- Cloisonnement strict entre comptes par investigation si menace élevée.

## 9.12 Erreurs classiques

Quelques erreurs récurrentes à éviter.

- LinkedIn d'investigation connecté au vrai téléphone (qui voit votre profil personnel via les contacts).
- VPN d'investigation et VPN personnel sur la même IP (corrélation possible).
- Métadonnées EXIF non purgées dans les captures envoyées au client.
- Copier-coller entre VM d'investigation et machine hôte (clipboard sync).
- Capture d'écran de l'investigation incluant la barre de tâches avec compte personnel.
- Réutilisation d'un username déjà utilisé personnellement.
- Posting via compte d'investigation depuis le wifi domestique sans VPN.
- Activation de la géolocalisation par défaut sur le téléphone d'investigation.

## 9.13 OPSEC parfaite n'existe pas

Aucune OPSEC n'est parfaite. L'objectif n'est pas l'invisibilité totale (théorique) mais la **réduction du risque à un niveau acceptable** pour la mission.

L'analyste qui surévalue sa sécurité (« je suis intracable ») est presque aussi dangereux que celui qui la néglige. Le premier prend des risques en croyant être invisible. La modestie OPSEC est une vertu.

## 9.14 OPSEC en équipe

Quand l'investigation se fait en équipe, l'OPSEC est le maillon faible.

**Pratiques.**

- Outils collaboratifs chiffrés (Signal, Wire, Element).
- Pas de partage de captures via canaux non chiffrés.
- Définir clairement qui voit quoi.
- Briefing OPSEC en début de mission.
- Debriefing en fin de mission (qu'est-ce qui a fuité, quoi corriger).

## 9.15 Synthèse — OPSEC par niveau

| Niveau menace | Infrastructure | Réseau | Téléphone | Stockage |
|---|---|---|---|---|
| **Ordinaire** | Profil navigateur dédié | VPN | Optionnel | Disque chiffré |
| **Sensible** | VM dédiée | VPN + DNS chiffré | Recommandé | Conteneur VeraCrypt par enquête |
| **Criminelle** | VM Whonix | VPN + Tor | Téléphone dédié SIM prépayée | Conteneur séparé + backup chiffré |
| **Étatique** | Tails clé USB | Tor seul, jamais VPN commercial | Téléphone jetable | Pas de stockage local longue durée |

Le chapitre suivant traite spécifiquement de l'OPSEC face aux plateformes et à l'IA — un sujet 2026 majeur.

-----
