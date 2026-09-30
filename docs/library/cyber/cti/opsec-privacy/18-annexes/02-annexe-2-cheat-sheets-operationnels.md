---
title: Annexe 2 — Cheat sheets opérationnels
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Annexes
  - index.md
---

## 2.1 Audit initial en 90 minutes

1. HaveIBeenPwned : emails principaux + numéros de téléphone.
1. Google / Bing / DuckDuckGo : recherche nom complet, email, pseudos.
1. Sherlock ou WhatsMyName : recherche pseudonymes.
1. Reverse image (Yandex, Google Lens) sur photos publiques.
1. Audit Google Account → Sécurité (sessions, MFA, récupération).
1. Audit Apple ID → Appareils.
1. Audit iCloud → ADP activée ? Backup E2EE ?
1. Audit permissions mobiles (Localisation, Micro, Caméra, Photos, Contacts).
1. Audit gestionnaire de mots de passe : doublons, faibles, sans MFA.
1. Liste des comptes critiques sans MFA matériel.

## 2.2 Préparation manifestation

- Téléphone dédié GrapheneOS, profil manifestation, BFU avant départ.
- Code de déverrouillage 8 chiffres, biométrie désactivée.
- Faraday bag dans le sac.
- Numéros importants sur papier.
- Téléphone perso vraiment éteint chez soi.
- 100 € cash + CB prépayée.
- Pas de carte d’identité contenant adresse précise inutile.

## 2.3 Préparation voyage frontalier sensible

- Burner device (ou device durci, ADP, Lockdown Mode, FileVault).
- Données sensibles évacuées en cloud E2EE (Proton Drive).
- Sessions critiques révoquées.
- BFU absolu avant passage frontière.
- Photos macro des composants internes pour comparaison retour.
- Vis vernies pour détection d’intrusion physique.

## 2.4 Réception document sensible

1. Vérifier provenance (Safety Numbers, canal authentifié).
1. Hash SHA-256 confirmé hors bande.
1. Environnement isolé (Tails ou dispVM).
1. Dangerzone pour PDF.
1. ExifTool / MAT2 pour métadonnées.
1. Archivage chiffré.

## 2.5 Compte compromis suspecté

1. Mot de passe changé depuis appareil sain.
1. Toutes sessions actives révoquées.
1. Audit modifications récentes (mail récup, MFA, filtres).
1. MFA matériel activé.
1. Comptes liés vérifiés.
1. Communication aux contacts si phishing envoyé.
1. Plainte si dommages.

## 2.6 Spyware mercenaire suspecté

1. Mode avion immédiat + faraday bag.
1. Ne pas redémarrer (perte d’IOC).
1. Access Now Digital Security Helpline.
1. Sauvegarde locale (iTunes/Quicktime).
1. Soumission MVT et Citizen Lab.
1. Appareil neuf, comptes audités, threat model révisé.

## 2.7 Sauvegarde 3-2-1 minimale

- Disque local (chiffré).
- Cloud E2EE (Proton Drive, Tresorit, ou chiffré côté client).
- Externe en lieu sûr (chez avocat, parent, coffre).
- Test de restauration trimestriel.

-----
