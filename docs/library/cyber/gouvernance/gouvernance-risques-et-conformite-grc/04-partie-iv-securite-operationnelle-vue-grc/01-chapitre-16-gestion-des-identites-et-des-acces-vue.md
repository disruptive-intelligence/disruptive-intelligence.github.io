---
title: Chapitre 16 — Gestion des identités et des accès vue GRC
source: Cyber/08 Gouvernance & résilience/Gouvernance & conformité/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - ../index.md
- - Partie IV — Sécurité opérationnelle vue GRC
  - index.md
---

Les principes de gouvernance IAM : moindre privilège (ne donner que les droits nécessaires à la fonction), séparation des devoirs (l'approbateur n'est pas l'exécutant), besoin d'en connaître (l'accès à une information est conditionné par la nécessité fonctionnelle). Les processus : provisioning (création du compte avec les droits associés au profil de poste — automatisé via l'annuaire RH si possible), deprovisioning (désactivation immédiate au départ — le délai entre le départ d'un employé et la désactivation de ses comptes est un indicateur de maturité), et revue des accès (trimestrielle pour les accès privilégiés, semestrielle pour les accès standards — avec CR signé par le propriétaire des données, pas par l'IT). La gestion des comptes privilégiés (PAM — coffre-fort de mots de passe, enregistrement des sessions admin, rotation automatique des mots de passe de service). La politique de MFA (quels comptes : tous les admins + tous les accès distants + les utilisateurs avec accès aux données sensibles ; quels types : résistant au phishing pour les admins — FIDO2/clés physiques, push/TOTP pour les utilisateurs standard). La politique de mots de passe (longueur > complexité — NIST recommande 12+ caractères sans rotation obligatoire, gestionnaire de mots de passe, interdiction de réutilisation).

---
