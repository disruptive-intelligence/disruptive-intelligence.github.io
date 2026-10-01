---
title: Chapitre 10 — Intrusion numérique par social engineering
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie II — Social engineering numérique
  - index.md
---

identité, SSO, MFA et workflows

## 10.1 Social engineering du helpdesk

Le helpdesk est la surface d'attaque la plus sous-estimée en matière de social engineering numérique. Les techniciens de support sont formés à résoudre les problèmes rapidement et avec courtoisie — deux objectifs qui entrent en conflit direct avec la sécurité lorsqu'un attaquant appelle en se faisant passer pour un employé bloqué.

Le scénario classique est le reset de credentials. L'attaquant appelle le helpdesk en se faisant passer pour un employé dont il a collecté les informations par OSINT (nom, poste, manager, identifiant employé si disponible) et demande un reset de mot de passe ou un reset de MFA. Si les procédures de vérification d'identité du helpdesk sont faibles (questions auxquelles les réponses sont trouvables en OSINT — date de naissance, nom du manager, identifiant employé), l'attaquant obtient un accès légitime au compte de l'employé.

Le rapport Unit 42 2025 documente plusieurs cas graves. Dans un cas, un attaquant a contacté le helpdesk à plusieurs reprises, chaque appel affinant le pretexte avec les informations glanées lors des appels précédents. Après avoir passé les vérifications d'identité, il a obtenu un reset MFA qui lui a donné accès aux systèmes internes. L'ensemble des actions post-compromission mimait un comportement utilisateur légitime, évitant de déclencher les alertes EDR.

**Défense P0** : les procédures de helpdesk pour les resets de credentials doivent inclure des vérifications que l'attaquant ne peut pas contourner par OSINT. Exemples : callback sur le numéro de téléphone enregistré dans l'annuaire (pas celui fourni par l'appelant), vérification en personne pour les comptes à privilèges, validation par le manager direct, utilisation de codes de vérification préétablis.

## 10.2 Le détournement de MFA

Le MFA (Multi-Factor Authentication) est une défense essentielle, mais il n'est pas infaillible face au social engineering.

**Le phishing en temps réel (reverse proxy).** Des outils comme Evilginx2, Modlishka et Muraena permettent de créer des proxies qui s'interposent entre la cible et le service légitime (Microsoft 365, Google Workspace). La cible saisit ses identifiants et son code MFA sur ce qui semble être la page de connexion légitime — mais le proxy capture le token de session authentifié. L'attaquant peut alors utiliser ce token pour accéder au compte sans avoir besoin de re-passer le MFA. Cette technique contourne toutes les formes de MFA basées sur des codes (OTP, push notification) — seul le MFA résistant au phishing (FIDO2/WebAuthn, qui vérifie l'origine du domaine) est immunisé.

**La push fatigue (MFA bombing).** L'attaquant, qui possède déjà les identifiants de la cible (obtenus par phishing, credential stuffing ou achat sur le darkweb), déclenche des demandes de validation MFA push en série. Submergé par les notifications, l'employé finit par approuver une demande — soit par lassitude, soit par erreur, soit pour « faire cesser les notifications ». Certains systèmes modernes (Microsoft Authenticator, Duo) ont implémenté des contre-mesures : number matching (l'utilisateur doit saisir un code affiché à l'écran, pas simplement approuver) et limitation du nombre de notifications.

**Le device code phishing.** Cette technique exploite le flux d'authentification « device code flow » de OAuth2, conçu pour les appareils sans navigateur (TV connectées, IoT). L'attaquant génère un code de device et envoie un lien à la cible (par phishing, vishing ou messagerie) en lui demandant de s'authentifier avec ce code. La cible se connecte sur une page Microsoft ou Google légitime et saisit le code — l'attaquant obtient un token d'accès. Cette technique est particulièrement insidieuse parce que la page d'authentification est 100 % légitime.

## 10.3 Exploitation des processus d'onboarding et d'offboarding

Les processus d'arrivée (onboarding) et de départ (offboarding) sont des fenêtres de vulnérabilité structurelles.

En phase d'onboarding, un attaquant peut se présenter comme un nouvel employé ou un nouveau prestataire pour obtenir des identifiants, un badge d'accès ou un poste de travail. Si le processus d'onboarding ne comporte pas de vérification robuste de l'identité (photo sur le contrat, validation par le manager, vérification d'identité officielle), l'usurpation est possible. Les cas de DPRK IT workers (travailleurs nord-coréens utilisant des identités fictives pour se faire embaucher comme freelances dans des entreprises technologiques) illustrent cette menace à un niveau de sophistication extrême.

En phase d'offboarding, les comptes non désactivés, les accès VPN non révoqués, les sessions OAuth non terminées constituent des portes d'entrée pour un attaquant qui a obtenu les identifiants d'un ancien employé (par social engineering de l'ancien employé lui-même, ou par achat de credentials).

## 10.4 La compromission de la supply chain humaine

La supply chain humaine — l'ensemble des prestataires, fournisseurs et sous-traitants qui ont un accès physique ou logique aux systèmes de l'organisation — est une surface d'attaque souvent négligée.

Le nettoyage de nuit a accès à tous les bureaux. La maintenance informatique a accès aux locaux serveurs. Le traiteur a accès à la cuisine et souvent aux couloirs. Le prestataire de reprographie a accès à des documents confidentiels. Cibler ces prestataires (par social engineering direct ou par compromission de leurs systèmes) permet un accès indirect à l'organisation cible avec un niveau de contrôle souvent inférieur à celui appliqué aux employés internes.

## 10.5 Red team scenarios et résultats typiques

Les résultats des tests de social engineering numérique sont systématiquement supérieurs aux attentes des commanditaires. Les taux de clic sur les campagnes de spear-phishing bien construites se situent typiquement entre 15 % et 40 %. Les taux de soumission d'identifiants (credential harvesting) entre 8 % et 25 %. Les tentatives de reset de credentials via le helpdesk réussissent dans 30 % à 60 % des cas si les procédures ne sont pas renforcées. Ces chiffres ne reflètent pas l'incompétence des employés — ils reflètent la qualité de la personnalisation et la puissance des leviers psychologiques exploités.

---
