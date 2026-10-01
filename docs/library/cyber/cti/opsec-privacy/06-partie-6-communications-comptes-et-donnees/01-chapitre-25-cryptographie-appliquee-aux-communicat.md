---
title: Chapitre 25 — Cryptographie appliquée aux communications
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

## 25.1 Chiffrement de bout en bout (E2EE) : promesse et limites

L’**E2EE** signifie : seul l’émetteur et le destinataire peuvent lire le contenu. Les serveurs intermédiaires (fournisseur de messagerie, opérateur, FAI) voient du chiffré indéchiffrable. C’est la propriété fondatrice de Signal, WhatsApp (contenu), iMessage (avec Contact Key Verification), Proton Mail (côté E2EE entre comptes Proton), etc.

**Ce que l’E2EE protège** : le *contenu* des messages contre les intermédiaires.

**Ce que l’E2EE ne protège pas** :

- Les **métadonnées** (qui parle à qui, quand, combien).
- Les **endpoints** : un téléphone compromis lit les messages en clair après déchiffrement local.
- Le **destinataire** : si la personne avec qui tu parles fait une capture d’écran ou transfère, l’E2EE n’y change rien.
- Les **sauvegardes non chiffrées** : WhatsApp sauvegardé sur iCloud sans chiffrement, c’est le contenu en clair côté Apple/Google.

## 25.2 Forward secrecy

La **forward secrecy** (PFS) garantit qu’une clé compromise *aujourd’hui* ne permet pas de déchiffrer les messages *du passé*. Chaque session/message utilise une clé éphémère dérivée d’un échange Diffie-Hellman, puis détruite.

Sans forward secrecy : si l’attaquant capte aujourd’hui ta clé privée, il peut déchiffrer toutes tes communications passées qu’il aurait stockées en attendant. C’est exactement ce que font certaines agences avec leur stratégie « collect now, decrypt later ».

**Signal Protocol** (utilisé par Signal, WhatsApp, Wire) implémente la forward secrecy par double ratchet. **PGP/GPG** ne l’implémente pas (cf. Ch 27, l’une des grandes limites de PGP).

## 25.3 Post-compromise security

La **post-compromise security** (PCS) ou *future secrecy* : si l’attaquant a compromis ta clé à un moment T, le protocole peut « se réparer » : un nouvel échange de clés rétablit la confidentialité pour les messages futurs.

Le double ratchet de Signal combine forward secrecy et PCS. C’est l’état de l’art en 2025.

## 25.4 Deniability

La **deniability** (déniabilité) : tu peux nier de manière crédible avoir envoyé un message, parce que le protocole ne produit pas de preuve cryptographique irréfutable d’authorship. OTR (Off-the-Record) historique l’implémentait fortement. Signal Protocol l’implémente partiellement.

**Pour qui c’est important** : lanceurs d’alerte, sources, témoins. Si tu reçois une menace ou une preuve, tu ne veux pas qu’on puisse prouver mathématiquement qui te l’a envoyée. Pour la majorité, c’est un détail.

## 25.5 Métadonnées de communication

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

## 25.6 Vérification d’identité des contacts

L’E2EE ne sert à rien si tu communiques avec un imposteur. Les protocoles modernes proposent une vérification :

- **Safety Numbers (Signal)** : une chaîne de 60 chiffres dérivée des clés. À comparer manuellement, en personne ou par canal hors bande (vocal, vidéo). Si elle change, tu es alerté.
- **Contact Key Verification (iMessage)** : depuis iOS 17.2. Vérification cryptographique des clés iMessage entre contacts.
- **Fingerprints PGP** : à comparer hors bande.

Ces vérifications sont *à faire activement* pour les contacts critiques. La plupart des gens ne le font jamais. Pour un journaliste avec une source : c’est non négociable.

## 25.7 Compromission des endpoints

Le chiffrement E2EE ne sauve pas un appareil compromis. Si ton téléphone est infecté par Pegasus, l’attaquant lit Signal en clair après déchiffrement local — comme toi.

C’est pourquoi la sécurité des appareils (Ch 14-15) et la détection de compromission (Ch 33) priment sur le choix de la messagerie. Une messagerie parfaitement chiffrée sur un téléphone compromis = aucune protection.

## 25.8 Renvoi croisé

Le détail des primitives cryptographiques (AES, ECDH, double ratchet, etc.) est dans le cours dédié à la cryptographie de la bibliothèque. Ce chapitre s’arrête au niveau des propriétés, suffisant pour choisir des outils.

-----
