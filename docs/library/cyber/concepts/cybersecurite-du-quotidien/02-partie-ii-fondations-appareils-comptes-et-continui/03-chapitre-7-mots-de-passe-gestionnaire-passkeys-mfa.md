---
title: Chapitre 7 — Mots de passe, gestionnaire, passkeys, MFA et SIM swap
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie II — Fondations : appareils, comptes et continuité'
  - index.md
---

## 7.1 Le vrai problème : la réutilisation

Le risque le plus structurant n'est pas le mot de passe faible — c'est le mot de passe réutilisé. Quand un service est piraté (LinkedIn 2021, Deezer 2022, et des centaines d'autres chaque année), les mots de passe volés sont testés automatiquement sur des dizaines d'autres services — c'est le credential stuffing. Si le même mot de passe est utilisé sur Netflix ET sur la banque, la compromission de Netflix = la compromission de la banque. La vérification : Have I Been Pwned (haveibeenpwned.com) permet de vérifier gratuitement si un email ou un mot de passe a été exposé dans une fuite de données.

## 7.2 Le gestionnaire de mots de passe

La seule solution réaliste pour avoir des mots de passe uniques partout : un gestionnaire de mots de passe (Bitwarden — gratuit et open source, 1Password — payant et très ergonomique, KeePass — local et gratuit). Le gestionnaire génère un mot de passe unique et aléatoire pour chaque compte, le stocke de manière chiffrée, et le remplit automatiquement. L'utilisateur ne retient qu'un seul mot de passe : le mot de passe maître. Ce mot de passe maître doit être long, mémorisable, et UNIQUE — ne jamais l'utiliser ailleurs. Une phrase de passe de 4-5 mots est idéale : « café.vélo.montagne.Jupiter.2024 ». La migration vers le gestionnaire prend une heure ou deux — c'est l'investissement le plus rentable de toute la cybersécurité personnelle.

## 7.3 Le MFA (authentification multi-facteurs)

Le MFA ajoute un second facteur après le mot de passe : quelque chose que l'on possède (un téléphone, une clé physique) en plus de quelque chose que l'on connaît (le mot de passe). Les options : un **code TOTP** généré par une application (Aegis ou 2FAS pour leur orientation open source et confidentialité, Ente Auth pour la sauvegarde chiffrée de bout en bout, Proton Authenticator pour un usage multiplateforme, Authy pour la commodité ; Google Authenticator reste utilisable mais propose moins de garanties différenciantes), une **notification push** (app bancaire), ou une **clé physique** (YubiKey — la plus sécurisée, résistante au phishing).

**TOTP dans une app dédiée vs dans le gestionnaire** : la plupart des gestionnaires modernes (Bitwarden, 1Password, Proton Pass) intègrent un générateur TOTP. C'est pratique — tout est au même endroit, le remplissage est automatique. Le compromis : si le gestionnaire lui-même est compromis, l'attaquant a à la fois le mot de passe ET le second facteur. La règle de bon sens : pour les comptes vraiment critiques (email maître, banque quand TOTP applicable, gestionnaire lui-même), privilégier une application TOTP séparée ou une clé physique. Pour les comptes secondaires (réseaux sociaux, services en ligne courants), TOTP dans le gestionnaire est acceptable et souvent préférable au SMS. Pour la **banque** en France, l'authentification forte passe en pratique par l'application bancaire, Secure Key, ou la validation biométrique — le TOTP n'est généralement pas l'option proposée ; utiliser le moyen le plus robuste mis à disposition par l'établissement.

Les **passkeys** sont la direction de l'industrie en 2025-2026 — authentification sans mot de passe par clé cryptographique liée au device, résistante au phishing et au credential stuffing. Apple, Google et Microsoft les supportent largement, et la majorité des services majeurs (banques, email, réseaux sociaux) les proposent en option. Quand le service propose les passkeys, les activer.

Les **codes de récupération** : à chaque activation de MFA, le service fournit des codes de secours. Ces codes doivent être imprimés ou stockés dans un lieu sûr — PAS dans le téléphone (c'est le téléphone qu'on perd). Sans ces codes, la perte du téléphone = la perte de l'accès aux comptes. La **fatigue MFA** : les attaquants envoient des dizaines de notifications push MFA jusqu'à ce que la victime accepte par épuisement → ne JAMAIS accepter une notification MFA qu'on n'a pas déclenchée soi-même.

## 7.4 Le SMS comme second facteur, et l'attaque SIM swap

Le **MFA par SMS** est mieux que rien mais il a une vulnérabilité majeure : le **SIM swap** (ou « port-out fraud »). Le mécanisme :

1. L'attaquant rassemble des informations personnelles sur la victime (fuites de données, réseaux sociaux, ingénierie sociale).
2. Il contacte l'opérateur de la victime en se faisant passer pour elle (« j'ai perdu ma carte SIM, j'aimerais la transférer sur une nouvelle SIM ») ou demande une portabilité du numéro vers un autre opérateur.
3. Avec les informations rassemblées (nom, date de naissance, adresse, parfois numéro de pièce d'identité ou d'abonné), il convainc le service client de l'opérateur de procéder au transfert.
4. Une fois le transfert effectué, le téléphone de la victime perd son réseau (plus de signal, plus de SMS, plus d'appels). L'attaquant reçoit désormais TOUS les SMS — y compris les codes MFA bancaires.
5. L'attaquant utilise les codes MFA pour accéder aux comptes de la victime, vider les comptes bancaires, ou changer les mots de passe.

Le SIM swap est devenu suffisamment **documenté et industrialisé** pour devoir être intégré aux réflexes de sécurité des comptes critiques. Des cas documentés font état de pertes de plusieurs dizaines de milliers d'euros par victime. Les opérateurs ont renforcé leurs procédures, mais le risque reste réel.

Les **signaux d'alerte d'un SIM swap en cours** : perte soudaine et inexpliquée du réseau mobile (« pas de service », « SOS uniquement »), notifications de connexion sur des comptes que vous n'avez pas déclenchées, impossibilité de recevoir des SMS, opérations bancaires que vous n'avez pas faites.

La **réaction immédiate en cas de suspicion de SIM swap** : appeler l'opérateur DEPUIS UN AUTRE TÉLÉPHONE (le vôtre n'a plus de réseau) pour bloquer immédiatement la SIM frauduleuse, contacter votre banque pour bloquer les comptes et vérifier les opérations récentes, changer les mots de passe des comptes critiques (depuis un autre appareil), et déposer plainte.

La **prévention** :

- **Préférer les apps TOTP ou les passkeys au SMS** pour le MFA des comptes critiques (banque, email, gestionnaire de mots de passe). Le code TOTP est généré localement sur le téléphone, il ne dépend pas du réseau opérateur.
- **Activer le verrouillage de portabilité** chez votre opérateur (option « blocage de la portabilité » ou « sécurité du numéro » selon les opérateurs — gratuit, à activer en quelques clics dans l'espace client). Cette option ajoute une vérification supplémentaire avant tout transfert.
- **Mettre un code PIN** sur la carte SIM elle-même (Réglages > Mobile sur iOS, Paramètres > Sécurité > Configurer le verrouillage de la carte SIM sur Android). Ce code est demandé au démarrage du téléphone et après tout retrait/insertion de la SIM.
- **Limiter l'exposition publique du numéro de téléphone** sur les réseaux sociaux et les sites web — un numéro associé à un nom et une date de naissance trouvable en ligne facilite le SIM swap.

L'**eSIM** : la carte SIM virtuelle (eSIM) a un profil similaire au SIM swap traditionnel — un eSIM swap consiste à transférer le profil eSIM vers un nouveau téléphone. Les opérateurs ont mis en place des procédures spécifiques (vérification d'identité renforcée), mais le risque existe.

Le **numéro de téléphone n'est plus une preuve d'identité fiable**. C'est une réalité de 2025-2026 que beaucoup de services n'ont pas encore intégrée. Quand vous avez le choix, préférez une méthode d'authentification qui ne dépend PAS du numéro de téléphone.

---

<a id="chapitre-8"></a>
