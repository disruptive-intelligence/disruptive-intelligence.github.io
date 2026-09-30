---
title: 'Chapitre 15 — Mobile : iOS durci, Android, GrapheneOS'
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 3 — Sécurité matérielle, racine de confiance et isolation
  - index.md
---

> **Niveau de posture (cf. Ch 2.6)** : iPhone à jour + ADP + permissions auditées + reboot hebdomadaire = **Niveau 1**. iPhone + Lockdown Mode + reboot quotidien + Contact Key Verification, *ou* GrapheneOS sur Pixel dédié avec profils = **Niveau 2**. GrapheneOS avec profils stricts + MVT mensuel + iVerify + reboot biquotidien + sans aucune app Google Play Services privilégiée = **Niveau 3**.

## 15.1 Le constat brutal

Le smartphone est, pour la plupart des gens, le plus gros risque privacy. Il contient :

- L’historique de localisation continu.
- Les contacts et leurs métadonnées de communication.
- Les photos avec EXIF.
- Les comptes bancaires et messageries.
- La biométrie (empreinte, visage).
- Le microphone et la caméra (potentiellement actifs).

Aucun durcissement ne compense l’usage d’un smartphone non sécurisé pour des activités sensibles. Le choix de la plateforme et de sa configuration est plus important que l’ordinateur.

## 15.2 Identifiants mobiles

- **IMEI** : identifiant matériel du téléphone, transmis à chaque connexion cellulaire.
- **IMSI** : identifiant de la SIM, transmis au réseau (IMSI catchers le captent).
- **Numéro de téléphone** : visible à chaque appel/SMS.
- **eSIM** : équivalent fonctionnel à SIM physique, gérée logiciellement.
- **Wi-Fi MAC, BT MAC** : adresses uniques, randomisées sur les OS modernes (Ch 22).
- **Advertising ID** (IDFA iOS, AAID Android) : désactivables.

Les identifiants publicitaires mobiles — IDFA sur iOS, AAID sur Android, plus généralement MAID — ne doivent pas être vus comme de simples paramètres marketing. Dans l’écosystème publicitaire, ils peuvent servir de pivots de corrélation entre applications, lieux, horaires et comportements. Dans une logique ADINT, un identifiant publicitaire peut devenir un quasi-identifiant de renseignement : il ne donne pas directement le nom civil de la personne, mais permet souvent de la réidentifier par ses routines, ses lieux de vie, ses lieux de travail et ses déplacements récurrents. 

À côté des identifiants publicitaires fournis par l’OS, il faut également surveiller les initiatives d’identification publicitaire portées par les opérateurs télécoms. Des systèmes comme Utiq illustrent une tendance post-cookie : exploiter des signaux opérateur et des jetons pseudonymes pour permettre du ciblage publicitaire sans s’appuyer uniquement sur les cookies tiers ou les identifiants publicitaires classiques. Pour l’OPSEC, cela confirme qu’un téléphone personnel connecté à son abonnement mobile habituel reste un fort pivot de corrélation.

Pour un téléphone sensible, la règle est simple : moins il contient d’applications financées par la publicité, moins il émet de signaux exploitables. Un téléphone destiné à une manifestation, un rendez-vous source, une mission terrain ou une réunion confidentielle ne devrait pas contenir d’applications grand public à SDK publicitaires.

## 15.3 Téléphone personnel et lieux sensibles

Pour un profil exposé, le téléphone personnel ne doit pas être considéré comme un simple outil de communication. C’est un capteur permanent : localisation, Wi-Fi, Bluetooth, identifiants publicitaires, applications installées, SDK tiers, comptes personnels, habitudes de déplacement.

Dans un lieu sensible — base militaire, site industriel critique, réunion confidentielle, rendez-vous source, manifestation à risque, cabinet d’avocat, rédaction, ambassade, centrale nucléaire, site de défense — le téléphone personnel peut créer une fuite sans aucune compromission technique. Il suffit qu’une application collecte de la localisation ou qu’un identifiant publicitaire soit réobservé à plusieurs reprises pour reconstruire une routine.

Règle pratique : plus le lieu est sensible, plus l’appareil doit être minimaliste. Pour les usages critiques, préférer un téléphone dédié, sans compte personnel, sans applications publicitaires, avec localisation strictement limitée, identifiant publicitaire désactivé ou réinitialisé, et applications installées selon une logique de liste blanche.

## 15.4 Localisation

Cinq sources, agrégées :

- **GPS** : précision 5-10 m.
- **Wi-Fi** : géolocalisation par triangulation des SSID environnants (bases Google, Apple, Skyhook).
- **Bluetooth/BLE** : beacons commerciaux dans les magasins, AirTags.
- **Cellulaire** : antennes-relais, précision 100 m à 1 km en zone dense.
- **Magnétomètre, baromètre** : utilisés pour étage dans bâtiment.

Désactiver le « Service de localisation » d’un cran n’éteint pas les couches passives. Wi-Fi et Bluetooth peuvent renseigner sur ta position même avec GPS coupé.

## 15.5 iOS comme baseline

**Code long** : 6 chiffres minimum, alphanumérique idéalement. Face ID/Touch ID = confort, mais peuvent être contournés sous coercition.

**Lockdown Mode** (iOS 16+) : désactive des fonctionnalités exploitées par les spyware mercenaires : pièces jointes complexes en Messages, certaines APIs WebKit (JIT JavaScript), profils de configuration, accessoires filaires sur appareil verrouillé, etc. Coût ergonomique modéré, gain de sécurité réel. **À activer** pour les HVT (journalistes, dissidents, lanceurs d’alerte, avocats sensibles).

**Restrictions sur écran verrouillé** : désactiver les notifications, Siri, contrôle USB en lock screen, Wallet, retour d’appel.

**iCloud** : ADP activée (cf. Ch 14).

**Permissions** : audit Réglages → Confidentialité → revue par catégorie (Localisation, Contacts, Photos, Micro, Caméra, Suivi). Le « Tracking » d’apps (ATT) est désactivable globalement.

## 15.6 Advanced Data Protection iCloud

ADP, depuis fin 2022 (US) et étendu mondialement en 2023, bascule en chiffrement de bout en bout les catégories suivantes :

- iCloud Drive
- Photos
- Sauvegardes iCloud de l’appareil (incluant les sauvegardes WhatsApp si stockées dans iCloud)
- Notes, Rappels
- Signets et historique Safari
- Mémos vocaux
- et plusieurs autres catégories (Apple liste précisément sur https://support.apple.com)

**Important — ce qui reste NON chiffré de bout en bout, même avec ADP activé** : iCloud Mail, Contacts iCloud, et Calendrier iCloud restent accessibles à Apple. Apple le documente explicitement : ces trois services utilisent des standards d’interopérabilité (SMTP/IMAP pour Mail, CalDAV/CardDAV pour Calendrier et Contacts) qui imposent que les serveurs Apple traitent les contenus en clair pour pouvoir communiquer avec les autres fournisseurs et appareils tiers. Si la confidentialité de Mail, Contacts ou Calendrier est critique, il faut soit utiliser un autre fournisseur (Proton Mail, Proton Contacts, Proton Calendar), soit accepter que ces données restent visibles à Apple et exposées en cas de réquisition judiciaire.

**Conditions d’activation** : tous tes appareils Apple doivent être sur une version récente (iOS 16.2+, macOS 13.1+). Une clé de récupération doit être conservée (sinon perte totale des données ADP en cas d’oubli du code d’appareil et impossibilité d’utiliser un appareil de confiance). Apple ne peut plus aider à la récupération une fois ADP activé — c’est l’objet même du dispositif.

## 15.7 Android stock vs OEM

Android **AOSP** (Android Open Source Project) : propre, mais aucun OEM ne livre AOSP pur.

**Google Pixel + Android stock** : meilleure version d’Android pour mises à jour rapides, sécurité, mais entièrement intégré aux services Google.

**Samsung, Xiaomi, Oppo, Vivo, Huawei…** : surcouches OEM avec collecte propre, télémétrie additionnelle, apps préinstallées. Mises à jour de sécurité variables. Pour les Chinois (Xiaomi, Oppo, Vivo, Honor, Huawei) : préoccupations spécifiques liées à la juridiction d’origine et à des cas documentés de collecte excessive.

## 15.8 GrapheneOS

**Philosophie** : OS Android dégooglisé, durci, focalisé privacy et sécurité. Développement actif, mise à jour rapide des patches Android upstream.

**Caractéristiques** :

- Hardening kernel et userspace.
- Sandboxed Google Play : les services Google Play installés dans une sandbox utilisateur normale, pas en privilégié système. Tu peux utiliser des apps qui en dépendent sans donner à Google les privilèges habituels.
- **Profils utilisateurs** : isolation forte entre profils. Idéal pour séparer pro/perso/sensible.
- **Storage Scopes** : permission granulaire « cette app peut accéder à *ce dossier* seulement », alternative à « toutes les photos ».
- **Contact Scopes** : équivalent pour les contacts.
- **Network permission** : un toggle pour empêcher une app d’accéder au réseau, indépendamment du fait qu’elle le demande.
- Verified Boot avec clés signées par GrapheneOS, attestable.

**Limites** :

- Pixel uniquement (Pixel 6 et supérieurs sont privilégiés).
- Certaines apps (banking, gouvernementales) refusent de fonctionner sur ROM custom (anti-tampering).
- Pas de Google Wallet (Google Pay) — paiement sans contact via app bancaire dépend des apps.
- Carplay/Android Auto support limité.

**Pour qui** : tous ceux qui veulent un mobile sérieusement durci et peuvent vivre avec les contraintes. Recommandé pour journalistes, activistes, dirigeants exposés, professionnels cyber.

## 15.9 CalyxOS, LineageOS (et le cas DivestOS)

- **CalyxOS** : alternative à GrapheneOS, philosophie similaire mais MicroG préinstallé (réimplémentation libre des Google Play Services). Moins de hardening que GrapheneOS, mais position éthique intéressante. Maintenu activement.
- **LineageOS** : Android communautaire générique. Pas focalisé sécurité, mais utile pour prolonger la vie d’appareils non supportés par OEM. Important : LineageOS sans signatures Verified Boot du constructeur réduit la sécurité matérielle. À utiliser pour des appareils secondaires non sensibles.
- **DivestOS** : fork LineageOS focalisé sécurité, supportait plus de modèles que GrapheneOS. **Le projet a annoncé son arrêt fin 2024**, le développeur principal ayant cessé la maintenance active. À ne plus utiliser comme recommandation pour un déploiement nouveau ; les utilisateurs existants doivent planifier une migration vers une plateforme maintenue (GrapheneOS si Pixel disponible, CalyxOS sinon, ou retour à un OS constructeur à jour selon profil).

## 15.10 Choix matériel et support

GrapheneOS exige du **Pixel récent** (Pixel 6+). Pixel 8 et Pixel 8a sont actuellement (2025-2026) de bons points d’entrée : support OEM jusqu’en 2030-2031, Titan M2, performances correctes.

**Durée de mises à jour** : Pixel 8/8a → 7 ans (2030 pour le 8). iPhone → environ 6-7 ans en pratique. Samsung → 7 ans (Galaxy S22+ et plus). Reste du marché : 2-4 ans.

Acheter un téléphone sans support de mises à jour pour 5+ ans est une erreur d’investissement sécuritaire.

## 15.11 Permissions et hygiène applicative

- **Claviers tiers** : SwiftKey, Gboard avec sync cloud → mauvaise idée pour usage sensible. Pour GrapheneOS : utiliser le clavier intégré, ou AnySoftKeyboard sans cloud.
- **Presse-papiers** : surveillance possible par apps en arrière-plan. iOS 14+ alerte. Android 12+ aussi. Vigilance.
- **Trackers dans applis** : la plupart des applis grand public en intègrent. Outil utile : **Exodus Privacy** (analyse des trackers d’une app).
- **Permissions à scopes** : sur GrapheneOS, Storage Scopes et Contact Scopes ; sur iOS, sélection de photos précises plutôt que photo library complète.

## 15.12 Séparation pro/perso/sensible

Sur GrapheneOS : profils utilisateurs distincts. Chaque profil a son propre espace, ses apps, ses comptes. Bascule par swipe down.

Sur iOS : pas de profils utilisateurs (limitation iOS persistante). Solution : appareils distincts pour usages sensibles, ou « Focus Modes » avec filtres d’apps.

## 15.13 Reboot quotidien

Les spyware mercenaires modernes (Pegasus, Predator, Graphite) reposent souvent sur des exploits **non persistants** : un redémarrage les efface. L’attaquant doit alors re-infecter, ce qui multiplie ses traces et son coût.

Le **reboot quotidien** (ou hebdomadaire pour les moins exposés) est l’une des mesures les plus simples et les plus efficaces contre les attaques avancées. Cinq secondes par jour. À adopter systématiquement pour les HVT.

## 15.14 *Fil rouge* — Léa migre vers Pixel 8a + GrapheneOS

Léa, après son audit, achète un Pixel 8a en magasin (cash, anonymement), flashe GrapheneOS le soir même, et configure :

- **Profil principal** : usage quotidien sans Google, Signal, Proton Mail, navigateur Vanadium.
- **Profil pro** : son compte journalistique, Slack rédaction, outils pros.
- **Profil enquête** : compartiment dédié, SimpleX, Tor Browser sur mobile, aucun compte personnel.

Elle conserve son iPhone perso pour la vie civile (banque, photos famille), avec ADP activée. Reboot quotidien le matin. Six semaines de transition pour s’habituer.

> 🟩 **À retenir de la Partie 3**
> 
> - Hardware = racine de confiance. Tout ce qui suit en dépend.
> - Secure Boot + TPM = colonne vertébrale de la sécurité moderne. À activer, à comprendre, à mettre à jour.
> - FDE est indispensable, mais ne protège pas si l’appareil est saisi AFU.
> - Air gap : pour des secrets rares, pas pour le quotidien.
> - Mobile = plus gros risque privacy. iPhone durci ou GrapheneOS sont aujourd’hui les meilleurs choix.
> - Reboot quotidien : 5 secondes, gain réel.

-----
