---
title: Chapitre 32 — Paiements, traçabilité financière et cryptomonnaies
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

> **Cadre éditorial préalable** : ce chapitre est strictement éducatif et défensif. Il ne couvre pas le blanchiment, l’évasion fiscale, le contournement KYC ou la dissimulation d’origine illicite. Il aide à comprendre la traçabilité financière pour mieux protéger sa vie privée légitime, exercer sa liberté d’expression journalistique, ou se prémunir contre un harceleur exploitant tes traces de paiement.

## 32.1 Pourquoi le paiement est une fuite massive

Chaque transaction révèle :

- L’achat (objet, montant, lieu, heure).
- Le compte source (ton identité bancaire).
- Le compte destinataire (commerce, identité).
- Le contexte (carte fidélité ?, code postal, IP en ligne).

Agrégés, les paiements dessinent ta vie : où tu vis, où tu travailles, ce que tu manges, qui tu fréquentes, quelles consultations médicales tu as, quelles opinions tu soutiens (dons), quels médias tu consommes.

Les **banques** voient tout. Les **réseaux de paiement** (Visa, Mastercard) voient tout. Les **agrégateurs** (Plaid, Tink) si tu utilises des apps bancaires tierces voient tout. Les **commerçants** voient leurs achats, certains revendent.

## 32.2 Cartes et virements SEPA

CB classique : tracée intégralement, votre banque conserve l’historique.
Virement SEPA : motif transmis, libre. Traçabilité complète.
Prélèvement automatique : récurrence de fait, signal de relation contractuelle.

## 32.3 Cartes virtuelles

- **Revolut, N26, Lydia, Boursorama** : cartes virtuelles à usage unique ou jetables.
- **Privacy.com** (US) : cartes virtuelles à plafond, expirables.
- **Apple Card / Apple Pay** : tokenisation (le commerçant ne voit pas ton vrai numéro).

**Avantages** : limite la traçabilité commerciale, isole les fuites en cas de compromission du commerçant.
**Limites** : le fournisseur de la carte (Revolut, etc.) voit tout. Tu déplaces la confiance, tu ne l’élimines pas.

## 32.4 Cartes prépayées et cash en France/UE

L’achat anonyme de cartes prépayées avec montants substantiels n’est plus possible en UE depuis l’AMLD5 (2020) : KYC obligatoire au-delà de 150 € en physique, 50 € en ligne. AMLD6 a renforcé.

**Cash** : retrouve une valeur stratégique pour des achats que tu ne veux pas tracés. Limites légales : en France, les paiements professionnels > 1000 € sont interdits en cash ; entre particuliers, pas de limite spécifique mais déclaration au-delà de 10 000 €.

## 32.5 Cryptomonnaies : Bitcoin et Ethereum sont traçables

**Mythe à déconstruire** : Bitcoin et Ethereum ne sont **PAS** anonymes. Ils sont **pseudonymes**. Toutes les transactions sont publiques sur la blockchain. La société d’analyse Chainalysis et autres construisent des graphes complets liant adresses à identités via :

- Exchanges KYC-ed.
- Heuristiques d’analyse (multi-input, change address).
- Recoupement avec adresses connues.

**Cas réels** : nombreux ; les autorités américaines tracent quasi quotidiennement des transactions Bitcoin de criminalité.

## 32.6 Monero et Zcash

**Monero (XMR)** : confidentialité par défaut via ring signatures, stealth addresses, RingCT. Les transactions ne révèlent ni montant, ni expéditeur, ni destinataire. État actuel : pas d’analyse de chaîne efficace publiée à grande échelle (état de l’art 2025).

**Zcash (ZEC)** : confidentialité opt-in via zk-SNARKs (shielded addresses). Si tu utilises les shielded pools, confidentialité forte. Si tu utilises les transparent addresses, traçable comme Bitcoin.

**Limites réglementaires** :

- **MiCA** (Markets in Crypto-Assets) UE entré en vigueur 2024-2025 : transactions impliquant cryptomonnaies privacy-focused (Monero, Zcash shielded) seront plus restreintes sur exchanges régulés.
- **Travel Rule** : exchanges doivent partager certaines infos de bénéficiaires au-delà de seuils.
- **Delistings** : Monero retiré de Binance pour la plupart des marchés en 2024.

## 32.7 Cadre réglementaire 2025-2026

- **France** : déclaration de comptes crypto à l’étranger (formulaire 3916), imposition des plus-values, KYC sur exchanges français.
- **UE (MiCA)** : régulation harmonisée.
- **Sanctions** : adresses sanctionnées (OFAC US) inutilisables sur exchanges régulés.

## 32.8 La ligne rouge

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

## 32.9 Achats sensibles légitimes

Cas où limiter la traçabilité est légitime :

- **Santé** : consultations sensibles (IVG, addiction, santé mentale, IST).
- **Journalisme** : matériel pour mission, frais d’enquête.
- **Sécurité personnelle** : abonnement VPN, achat de matériel sécurité pour victime de violences.
- **Engagement politique** : adhésion partis, dons associatifs (les listes peuvent être indirectement révélées).
- **Recherche** : achat de livres, accès à bases qui révèlent un intérêt sensible.

## 32.10 Don anonyme à un journaliste / ONG

Plusieurs modèles légaux :

- **Cash en personne** : ancien et toujours fonctionnel.
- **Cash par courrier** : Mullvad VPN accepte (par exemple). Pour ONG, certaines aussi.
- **Cryptomonnaies** : Bitcoin avec wallet créé spécifiquement, jamais lié à exchange KYC. Monero pour confidentialité par défaut.
- **Intermédiaires** : certaines structures permettent dons anonymisés (fondations).

## 32.11 Paiement d’un VPN : le cas Mullvad, NymVPN et AmneziaVPN

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
