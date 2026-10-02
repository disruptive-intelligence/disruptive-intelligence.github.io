---
title: Chapitre 26 — Cloud, documents collaboratifs et stockage
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie V — Choisir ses outils numériques de confiance
  - index.md
---

*Le cloud n'est pas un disque dur magique. C'est un espace partagé, synchronisé, accessible à distance, qui doit être configuré.*

## 26.1 Quel cloud pour quel usage

| Type de cloud | Usage adapté | Vigilances |
|---------------|--------------|------------|
| **Cloud personnel** (iCloud, Google Drive, OneDrive perso, Dropbox) | Photos personnelles, documents personnels, organisation du foyer | MFA activé, partages révisés, pas de documents d'identité en clair |
| **Cloud familial** (Apple Family, Google Family) | Achats partagés, photos familiales, calendriers | Compartimenter ce qui doit l'être, retirer les ex (cf. Ch.38) |
| **Cloud professionnel** (Microsoft 365 entreprise, Google Workspace, suites métier) | **TOUS** les fichiers professionnels | Outil validé par l'organisation, contrôles DLP, audit possible |
| **Cloud institutionnel** (La Suite numérique, NextCloud d'organisation, plateformes ministérielles) | Données administratives, agents publics | Outil souverain pour les données régulées |

## 26.2 Documents collaboratifs : qui voit quoi

Un document Google Docs / Word Online / Notion partagé en mode édition donne accès à toutes les versions historiques (les commentaires « supprimés » sont récupérables, les paragraphes effacés sont dans l'historique). Avant de partager :

- **Vérifier les droits** : lecture / commentaire / édition selon ce qui est strictement nécessaire.
- **Vérifier les destinataires** par leur email exact (un email mal tapé donne accès à la mauvaise personne).
- **Pas de lien public** pour des documents qui contiennent des données identifiables.
- **Vérifier l'historique** avant de partager un document hérité : il peut contenir d'anciennes versions confidentielles.

## 26.3 Chiffrement local pour les documents très sensibles

Pour des documents très sensibles que vous voulez stocker dans un cloud personnel sans faire confiance à 100 % au fournisseur (CNI numérisée, copies de documents administratifs critiques, sauvegarde du gestionnaire de mots de passe), ou pour préparer un envoi vers un destinataire identifié, une couche de chiffrement local est utile. Plusieurs outils répondent à des besoins différents :

| Outil | Usage principal | Profil |
|-------|-----------------|--------|
| **Cryptomator** | Coffre chiffré **synchronisé dans un cloud personnel** (iCloud, Drive, Dropbox) — le fournisseur ne voit que du chiffré | Particulier, gratuit, open source, multiplateforme |
| **Zed!** (PRIM'X) | **Conteneur chiffré pour échange** de fichiers sensibles avec destinataires identifiés (par certificat ou mot de passe partagé) | Professionnel / institutionnel, certifié ANSSI sur des versions et périmètres précis ; voir Ch.25.3 |
| **VeraCrypt** | Conteneur ou volume chiffré local, gestion fine, montage à la demande | Profil avancé, gratuit, open source |
| **ZIP avec mot de passe AES-256** | Protection ponctuelle simple d'un fichier (compatible partout) | Cas occasionnels, moins professionnel |

**La distinction essentielle** : Cryptomator et VeraCrypt sont d'abord des **coffres locaux** (le contenu reste chez vous, éventuellement synchronisé via un cloud que vous ne maîtrisez pas). Zed! est d'abord une **valise de transport** (le contenu est chiffré pour être envoyé à un destinataire précis). Les deux logiques sont complémentaires.

Ces solutions ne remplacent pas le bon comportement, mais ajoutent une couche pour les documents les plus sensibles.

---

<a id="chapitre-27"></a>
