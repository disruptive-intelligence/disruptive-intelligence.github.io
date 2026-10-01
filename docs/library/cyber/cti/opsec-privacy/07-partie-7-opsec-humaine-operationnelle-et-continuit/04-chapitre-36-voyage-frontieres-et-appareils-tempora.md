---
title: Chapitre 36 — Voyage, frontières et appareils temporaires
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 7 — OPSEC humaine, opérationnelle et continuité
  - index.md
---

## 36.1 Modèle de menace voyageur

La frontière est un lieu particulier : l’État a légalement le droit d’inspecter tes appareils dans des limites variables. Les douanes US peuvent demander à examiner ton téléphone et ordinateur, parfois à les retenir plusieurs jours. Singapour, Israël, certains pays asiatiques également. Européen entrant aux US : la liberté de refuser est limitée (refus = refus d’entrée).

Pour les voyages en pays à forte censure ou à DPI agressif, le choix du VPN doit être fait **avant le départ**. Installer un outil de contournement une fois sur place peut être impossible si les sites officiels, stores ou dépôts sont bloqués.

**Procédure** : installer, tester et documenter au moins deux options avant le départ : un VPN privacy classique, un outil anti-censure obfusqué, et Tor Browser avec bridges. Ne pas dépendre d’un seul canal.

Trois questions à se poser avant tout voyage :

1. **Ai-je vraiment besoin** de mes données habituelles sur cet appareil ?
1. **Que se passe-t-il si l’appareil est saisi, cloné, ou rendu après accès** ?
1. **Quelles sont les règles douanières spécifiques** au pays d’entrée ?

## 36.2 BFU vs AFU à la frontière (CRITICAL)

**Avant de passer une frontière** : éteindre complètement les appareils. Pas de verrouillage, pas de sommeil. **Vraie extinction**.

Effet : les appareils sont en BFU (Before First Unlock). La plupart des données utilisateur sont protégées par des clés dérivées du code de déverrouillage, qui ne sont pas en mémoire. Les outils forensics professionnels (Cellebrite UFED, GrayKey) sont **significativement moins efficaces** sur un appareil en BFU que sur un appareil en AFU.

Cinq secondes de discipline avant chaque passage frontalier = écart énorme en posture forensique.

## 36.3 Burner devices

Pour voyages sensibles (frontière hostile, pays à risque) : appareils dédiés au voyage, distincts du quotidien.

- **Téléphone de voyage** : ancien Pixel, GrapheneOS minimal, comptes burner (email dédié, Signal dédié), aucune photo ni contact personnel. Au retour : reset complet ou destruction.
- **Laptop de voyage** : Chromebook ou laptop minimal, comptes burner, données non sensibles uniquement, pas de cookies de session, pas de fichiers locaux. Si besoin d’accès, données récupérées via cloud E2EE après arrivée.

## 36.4 Procédures pre-voyage

1. **Audit** : qu’est-ce qui ne doit absolument pas franchir la frontière ?
1. **Cloud E2EE** des données nécessaires (Proton Drive, etc.), accessibles depuis l’arrivée.
1. **Backup** complet avant départ.
1. **Effacement des comptes sociaux non essentiels** sur l’appareil de voyage.
1. **Déconnexion** de tous les comptes critiques sur l’appareil de voyage (sessions révoquées, à reconnecter à l’arrivée si besoin).
1. **Compte burner** prêt pour communications de voyage.

## 36.5 À l’arrivée

- Vérifier l’intégrité physique (vis, scellés, comparaison photos).
- Si soupçon de manipulation : ne pas reconnecter aux comptes principaux, considérer l’appareil comme suspect.
- Reset à neuf si possible.
- Reconnexion progressive aux comptes nécessaires, en surveillant les notifications de connexion suspecte.

## 36.6 Au retour

- Reset complet de l’appareil de voyage, ou destruction physique si haut risque.
- Audit des appareils restés au domicile (intrusion physique pendant absence ?).
- Audit des comptes : sessions de l’étranger ? Connexions inhabituelles ?
- Changement préventif des credentials critiques si profil HVT.

## 36.7 Cas particuliers

- **Activistes vers Iran, Russie, Chine, certains pays Moyen-Orient** : VPN nécessaires mais souvent bloqués (utiliser Tor avec bridges, ou VPN avec protocoles obfusqués). Risques pénaux selon pays. Consulter ONG spécialisées (Access Now, EFF, RSF, Front Line Defenders) avant départ.
- **Journalistes en zones de conflit** : protocoles CPJ Digital Safety Kit, RSF guide journaliste, formations dédiées (Hostile Environment Awareness Training).
- **Dirigeants en mission commerciale Asie** : ANSSI publie des guides ; programme de sécurité économique gouvernemental français.

## 36.8 *Fil rouge* — Léa voyage à Kiev pour enquête terrain

Préparation :

- iPhone perso laissé à Bruxelles.
- Pixel 8a GrapheneOS avec profil enquête, contenant : Signal pro, SimpleX pour Karim, OnionShare, navigateur Vanadium, rien d’autre.
- Laptop dédié enquête (MacBook Air séparé), FileVault, Mullvad VPN, Tails sur clé USB de secours.
- Backup chiffré complet de toute son enquête sur Proton Drive avant départ.
- Compte SimpleX accessible depuis n’importe quel appareil avec ses clés.
- Numéro Signal communiqué à 3 contacts d’urgence : avocate, rédaction, ami de confiance.

À l’arrivée :

- Vérification matérielle : pas de manipulation visible.
- Premier contact local par téléphone non lié, lieu choisi par sa source locale.

Au retour :

- Reset complet du téléphone et laptop.
- Audit des comptes : aucune connexion suspecte.
- Documents rapatriés via Proton Drive en mode E2EE.

-----
