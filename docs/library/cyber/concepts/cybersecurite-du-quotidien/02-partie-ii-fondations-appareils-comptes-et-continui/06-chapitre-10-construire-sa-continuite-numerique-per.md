---
title: Chapitre 10 — Construire sa continuité numérique personnelle
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie II — Fondations : appareils, comptes et continuité'
  - index.md
---

*Que se passe-t-il si votre téléphone disparaît demain matin ? Si vous ne pouvez pas répondre à cette question en 30 secondes, ce chapitre est pour vous.*

L'**effet domino** : perdre le téléphone = perdre l'accès au MFA = perdre l'accès à l'email = perdre l'accès à tous les comptes liés = perdre l'accès à la banque, au cloud, aux messageries, aux réseaux sociaux. Chaque compte dépend d'un autre. Si le premier maillon tombe, tout tombe. La continuité numérique consiste à casser cette chaîne de dépendance pour que la perte d'un maillon ne fasse PAS tout tomber.

L'**ordre de reprise** en cas de perte/vol du téléphone : (1) bloquer la carte SIM (appeler l'opérateur — noter le numéro de blocage SIM AVANT d'en avoir besoin), (2) localiser et verrouiller/effacer le téléphone à distance (Find My), (3) changer le mot de passe de l'email maître (depuis un autre appareil), (4) révoquer les sessions actives sur les comptes critiques, (5) changer les mots de passe des comptes sensibles, (6) prévenir la banque si l'app bancaire était sur le téléphone, (7) prévenir l'employeur si le téléphone avait des usages pro.

Les **comptes critiques** à prioriser : email maître, banque, gestionnaire de mots de passe, cloud (photos, documents), messageries principales. Les comptes secondaires (Netflix, Spotify, Vinted) peuvent attendre.

Le **kit de survie numérique** — à préparer maintenant, pas le jour du sinistre : les codes de récupération MFA imprimés dans un lieu sûr, le mot de passe du gestionnaire mémorisé (pas stocké uniquement dans le téléphone), un second appareil avec les apps critiques, le numéro de blocage de la SIM, les numéros d'opposition bancaire, et un email de récupération secondaire configuré.

> **🔵 Lina — Épisode 4 :** Lina perd son téléphone dans le métro à Lyon. Elle n'a pas configuré Find My iPhone. Elle n'a pas ses codes de récupération MFA. Son email principal a le MFA par SMS — et la SIM est dans le téléphone perdu. Résultat : 3 jours pour reprendre le contrôle de ses comptes, un stress considérable, et 2 abonnements frauduleux souscrits entre-temps avec son compte compromis. Le chapitre montre ce qu'elle aurait dû préparer — et ce qu'elle met en place après l'incident pour que ça ne se reproduise plus.

---

> ### 🟦 Réflexes — Fin de Partie II
>
> **À configurer une fois pour toutes** :
> - Code 6+ chiffres + biométrie sur le téléphone
> - Mises à jour automatiques sur tous les appareils
> - Find My / Find My Device activé
> - Chiffrement disque sur l'ordinateur (BitLocker / FileVault)
> - Gestionnaire de mots de passe avec mot de passe maître unique et mémorisé
> - MFA application TOTP (pas SMS) sur les 5 comptes critiques
> - Email de récupération secondaire chez un autre fournisseur
> - Verrouillage de portabilité activé chez l'opérateur (anti-SIM swap)
> - Code PIN sur la carte SIM
>
> **À éviter absolument** :
> - Le même mot de passe sur deux comptes
> - MFA par SMS pour la banque ou l'email maître
> - Codes de récupération stockés uniquement dans le téléphone
> - Cracks et logiciels piratés
> - Macros Office « activées » sans raison
>
> **À vérifier tous les 6 mois** :
> - Sessions actives sur les comptes critiques
> - Permissions des applications mobiles
> - Extensions de navigateur (supprimer celles inutilisées)
> - Have I Been Pwned (votre email apparaît-il dans une nouvelle fuite ?)
>
> **Si quelque chose arrive** :
> - Signaux SIM swap : perte soudaine de réseau → appeler l'opérateur depuis un autre téléphone
> - Notification MFA non sollicitée → REFUSER, changer le mot de passe immédiatement
> - Compte compromis : voir Ch.41

---
