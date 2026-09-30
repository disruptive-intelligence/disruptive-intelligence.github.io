---
title: Chapitre 35 — Cloud personnel et partage familial
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VII — Maison connectée, famille ET frontière pro/perso
  - index.md
---

Les risques du cloud personnel : la **synchronisation automatique** (iCloud, Google Photos, OneDrive — les photos prises sont automatiquement uploadées dans le cloud, y compris les captures d'écran de conversations privées, les photos de documents sensibles, et les photos accidentelles → vérifier régulièrement ce qui est synchronisé et supprimer ce qui ne devrait pas être dans le cloud). Les **liens de partage** (un lien Google Drive « toute personne ayant le lien » n'a aucun contrôle d'accès — si le lien est forwardé, intercepté, ou indexé par un moteur de recherche, le contenu est accessible à tous → pour les documents sensibles : partage nominatif avec authentification, durée limitée, et révocation possible).

La **corbeille** : les fichiers supprimés du cloud vont dans la corbeille pendant 30-60 jours. Ils sont récupérables — pratique en cas de suppression accidentelle, mais aussi accessibles à un attaquant qui a accès au compte. Les **photos « Récemment supprimées »** sur iOS/iCloud restent 30 jours dans un dossier dédié — accessible avec le compte. Pour une suppression réellement immédiate, vider également ce dossier après suppression.

Le **partage familial** : un compte partagé avec le conjoint ou les enfants (Apple Family, Google Family) signifie que les achats, les abonnements, la localisation, et parfois les photos sont visibles par tous les membres. Compartimenter ce qui doit l'être : si la localisation familiale est activée, savoir précisément qui voit quoi. Le partage familial n'est PAS adapté aux relations conflictuelles ou en transition (cf. Ch.38).

L'erreur classique : un Google Drive avec un dossier « Administratif » contenant CNI, passeport, bulletins de salaire, RIB, déclarations d'impôts — le tout accessible via un compte avec un mot de passe faible et sans MFA. Si le compte est compromis (et les comptes Google sont une cible fréquente de credential stuffing), c'est le kit complet d'usurpation d'identité. Le réflexe : ces documents ne doivent pas être stockés en clair dans le cloud principal — soit chiffrés (archive ZIP avec mot de passe fort, ou application de chiffrement type Cryptomator), soit dans un cloud séparé dédié uniquement à ces documents et avec MFA renforcé.

Les **partages anciens** : le lien partagé en 2021 pour un projet ponctuel est probablement encore actif en 2026. La majorité des comptes Google Drive / OneDrive contiennent des dizaines de partages oubliés. À réviser périodiquement — tous les 6 mois, lister les partages actifs et révoquer ce qui n'est plus pertinent.

> **🔵 Lina — Épisode 9 :** Lina partage un dossier Google Drive avec un ami pour un projet associatif. Le lien est en mode « toute personne ayant le lien ». Le dossier contient les documents du projet — mais aussi, dans un sous-dossier qu'elle a oublié, un scan de sa CNI et un RIB qu'elle avait stockés là « temporairement » il y a 6 mois. L'ami forward le lien par email à 5 autres personnes. Le scan de la CNI de Lina est maintenant accessible à des personnes qu'elle ne connaît pas. La leçon : un dossier partagé doit contenir UNIQUEMENT ce qu'on accepte de voir partagé. Les documents personnels n'y ont pas leur place, même temporairement.

---

<a id="chapitre-36"></a>
