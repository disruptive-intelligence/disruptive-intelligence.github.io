---
title: Chapitre 28 — Gestionnaires de mots de passe, coffres et clés physiques
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie V — Choisir ses outils numériques de confiance
  - index.md
---

*Les outils de sécurité eux-mêmes méritent un chapitre. Le meilleur gestionnaire est celui que la personne utilisera réellement, correctement et durablement — pas celui qu'un expert recommanderait dans un monde idéal.*

## 28.1 Quel gestionnaire pour quel profil

| Profil | Outil adapté | Pourquoi |
|--------|--------------|----------|
| **Débutant, usage simple** | Gestionnaire intégré (iCloud Trousseau / Google Password Manager / Microsoft Authenticator) ou Bitwarden gratuit | Déjà installé, gratuit, suffisamment robuste pour un usage standard |
| **Famille** | Bitwarden Families ou 1Password Families | Coffre familial avec partage contrôlé, abonnement modéré |
| **Profil avancé / souveraineté** | KeePassXC (local, open source) | Stockage local maîtrisé, pas de cloud du fournisseur, sauvegarde à organiser soi-même |
| **Comptes très critiques** | Clé physique (YubiKey, SoloKey) + codes de récupération papier | Résistance au phishing, deuxième facteur le plus robuste pour email maître ou compte privilégié |

## 28.2 Le mot de passe maître

C'est le seul mot de passe à retenir, donc le plus important :

- **Long** : au moins 4-5 mots, idéalement plus.
- **Mémorisé**, pas stocké numériquement.
- **Unique** : ne jamais le réutiliser ailleurs.
- **Mémorable** : une phrase de passe avec ponctuation et chiffres (« café.vélo.montagne.Jupiter.2024 » est meilleur que « M0t2P@sse! »).

## 28.3 Le débat TOTP : dans le gestionnaire ou dans une app dédiée ?

Avantages du TOTP dans le gestionnaire : tout est au même endroit, le remplissage est automatique, c'est plus pratique donc plus utilisé.

Inconvénient : si le gestionnaire est compromis, l'attaquant a à la fois le mot de passe ET le second facteur — le MFA perd son sens.

**Le compromis raisonnable** :

- **Comptes critiques** (email maître, banque quand TOTP applicable, gestionnaire lui-même, fournisseurs d'identité utilisés via FranceConnect, cloud principal) : application TOTP dédiée (Aegis sur Android ; 2FAS, Ente Auth ou Proton Authenticator sur iOS ; Authy ou Proton Authenticator pour un usage multiplateforme) ou clé physique.
- **Comptes secondaires** (réseaux sociaux, sites de shopping, services secondaires) : TOTP dans le gestionnaire, c'est acceptable et meilleur que pas de MFA du tout.
- **Banque française** : utiliser le moyen d'authentification forte proposé par l'établissement (application bancaire avec validation, Secure Key, biométrie), pas TOTP en général.

## 28.4 Codes de récupération et clés physiques

**Codes de récupération** : à chaque activation de MFA, le service génère des codes à usage unique pour récupérer l'accès en cas de perte du second facteur. Les imprimer ou les noter à la main, et les stocker hors du téléphone (un tiroir à la maison, un coffre, chez un proche de confiance, en double exemplaire). Ne JAMAIS les stocker uniquement dans le gestionnaire de mots de passe (qui devient inaccessible si le téléphone est perdu) ou uniquement dans le téléphone.

**Clé physique** (YubiKey, SoloKey, Titan Security Key) : pour les comptes les plus critiques, une clé physique connectée en USB ou en NFC est le second facteur le plus robuste (résistant au phishing, au clonage, au social engineering). Un usage typique : email maître + gestionnaire de mots de passe avec une clé physique principale et une clé de secours. Quand on choisit cette voie, prendre **toujours deux clés** — une à utiliser, une de secours rangée en lieu sûr. La perte d'une clé sans secours = potentielle perte d'accès.

## 28.5 Coffre papier minimal

Tout ne doit pas être numérique. Un **coffre papier minimal**, à imprimer et à stocker dans un lieu sûr (chez soi, chez un proche, dans un coffre, chez un notaire), contient :

- Le mot de passe maître du gestionnaire (ou la phrase mnémotechnique pour le retrouver).
- Les codes de récupération MFA des comptes critiques.
- Les numéros d'urgence (opposition SIM, opposition bancaire, FAI).
- Le mot de sécurité familial (cf. Ch.20).
- Le contact d'une personne de confiance qui sait où trouver l'essentiel.

L'Annexe J fournit un modèle de fiche d'urgence à imprimer.

---
