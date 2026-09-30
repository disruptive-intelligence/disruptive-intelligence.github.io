---
title: 'Chapitre 5 — Sécuriser son téléphone : le maillon central'
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie II — Fondations : appareils, comptes ET continuité'
  - index.md
---

Le téléphone est le point central de la vie numérique. Il contient l'email, la banque, le MFA, les messageries, les photos, la localisation. Le perdre sans préparation est l'un des pires scénarios du quotidien.

Le **verrouillage** : code à 6 chiffres minimum (un code à 4 chiffres a 10 000 combinaisons — observable par shoulder surfing en 2 secondes ; un code à 6 chiffres en a 1 million). La biométrie (Face ID, Touch ID, empreinte digitale) est un complément, pas un remplacement — le code est le vrai verrou car c'est lui qui déchiffre le téléphone au démarrage. Ne jamais utiliser un code trivial (000000, 123456, date de naissance). Le **chiffrement** est activé par défaut sur iOS et Android récent — mais il dépend du code : pas de code = pas de chiffrement effectif. Les **mises à jour** : activer les mises à jour automatiques. Les patchs de sécurité corrigent des vulnérabilités exploitées activement. Un téléphone qui ne reçoit plus de mises à jour de sécurité (Android en fin de support, iPhone trop ancien) est un téléphone à remplacer à moyen terme.

La **localisation et l'effacement à distance** : Find My iPhone (iOS), Find My Device (Android) — à configurer MAINTENANT, pas le jour de la perte. Ces services permettent de localiser le téléphone, de le verrouiller avec un message, et de l'effacer à distance si nécessaire.

Les **permissions des applications** : chaque application demande des permissions (micro, caméra, localisation, contacts, photos, fichiers). Le réflexe : accorder uniquement ce qui est strictement nécessaire à la fonction de l'application. Une application de lampe torche n'a pas besoin d'accéder aux contacts ni au micro. Réviser les permissions régulièrement (Réglages > Confidentialité sur iOS, Paramètres > Applications > Autorisations sur Android). Les **stores officiels** (App Store, Google Play) : ne pas installer d'applications depuis des sources tierces (APK téléchargés depuis un site web, liens reçus par SMS). Les applications malveillantes existent aussi sur les stores officiels, mais elles sont nettement moins fréquentes et sont retirées plus rapidement.

Le root (Android) et le jailbreak (iOS) **désactivent les protections de sécurité** du système d'exploitation. Ne pas le faire sur un appareil du quotidien. L'argument « je veux personnaliser mon téléphone » ne vaut pas la perte de la sandbox de sécurité, des mises à jour automatiques, et de la protection contre les applications malveillantes.

**Ce que votre téléphone sait de vous** — et partage sans que vous le réalisiez : l'**historique de localisation** (Google Timeline sur Android, Lieux importants sur iOS — désactivable dans les réglages de confidentialité ; cet historique montre vos déplacements sur des mois ou des années), les **permissions abusives des apps** (une app de jeu gratuit qui demande l'accès aux contacts et au micro pour « améliorer l'expérience » → elle collecte et revend ces données), le **pistage publicitaire** (IDFA sur iOS, GAID sur Android — un identifiant unique qui permet aux annonceurs de suivre votre activité entre les applications ; réinitialisable dans les réglages — iOS : Réglages > Confidentialité > Suivi, Android : Paramètres > Google > Publicité), les **notifications sur l'écran de verrouillage** (un code MFA, un message WhatsApp, un SMS bancaire — visibles par quiconque regarde l'écran → configurer les notifications en mode « pas de prévisualisation » pour les apps sensibles), et le **clipboard partagé** (un mot de passe copié dans le gestionnaire est accessible pendant quelques secondes à toute app qui lit le clipboard — sur iOS 16+, une notification apparaît quand une app lit le clipboard).

---

<a id="chapitre-6"></a>
