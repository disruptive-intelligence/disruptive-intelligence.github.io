---
title: Chapitre 23 — Stratégies de confinement et arbitrages
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie V — Confinement, décision et préservation de preuve
  - index.md
---

## 23.1 Le dilemme fondamental

Contenir **trop tôt** alerte l'attaquant. S'il détecte que ses connexions C2 sont coupées ou que ses comptes sont désactivés, il peut réagir de manière destructrice : accélérer le chiffrement, activer un wiper, supprimer les logs, ou activer un mécanisme de persistance de secours. Contenir **trop tard** lui laisse le temps d'aggraver les dégâts : chiffrer davantage de systèmes, exfiltrer davantage de données, s'enraciner plus profondément.

Le timing optimal dépend du type d'attaque. **Ransomware en cours de déploiement** : confinement immédiat — chaque minute de retard signifie des dizaines de machines chiffrées en plus. La course contre le chiffrement est réelle. **Espionnage discret** : observation contrôlée possible — si l'attaquant ne sait pas qu'il est détecté, continuer à l'observer permet de comprendre l'étendue complète de la compromission avant de le couper. **Compromission de compte sans activité destructrice** : désactivation immédiate du compte — l'impact est limité et la mesure est réversible.

## 23.2 Confinement réseau

Les options de confinement réseau, de la plus chirurgicale à la plus radicale : isolation de machines spécifiques via EDR (network containment — la machine reste allumée mais ne peut plus communiquer, sauf avec la console EDR), isolation de segments via ACL pare-feu ou VLAN (couper les flux entre segments compromis et segments sains), coupure de l'accès Internet ciblée (bloquer les communications C2 sans couper toute la production), coupure de l'accès Internet totale (couper toutes les communications externes — radical mais efficace contre les ransomwares qui utilisent un C2 pour le chiffrement), et isolation inter-sites (couper les liens WAN entre sites pour empêcher la propagation d'un site compromis vers les autres).

Chaque option a un impact business mesurable. L'isolation d'un segment serveur arrête les services hébergés. La coupure Internet arrête les emails, le VPN, les services cloud, et potentiellement les systèmes de paiement. L'isolation inter-sites empêche la collaboration entre sites. Ces impacts doivent être évalués AVANT la décision, en concertation avec les métiers.

## 23.3 Confinement des comptes

Désactivation des comptes compromis (identifiés par l'investigation), reset des mots de passe des comptes à privilèges (la question du timing : quand fait-on le reset massif ?), révocation des sessions et tokens (M365, VPN, SSO, OAuth), rotation des secrets de service (mots de passe des comptes de service, clés API, certificates), et désactivation des accès tiers (VPN prestataires, interconnexions partenaires).

Le risque de lock-out massif : un reset de tous les mots de passe du domaine un samedi matin bloquera les 12 000 utilisateurs lundi matin s'il n'est pas coordonné avec une communication claire et un mécanisme de reset autonome (portail de self-service, assistance téléphonique renforcée).

## 23.4 Fil rouge — BLACKTIDE : la décision de confinement

> **🔍 BLACKTIDE — Épisode 23**
>
> Samedi 15 mars, 01h30. Le ransomware est en cours de déploiement. Nadia présente 3 options à la cellule de crise technique (Marc/RSSI valide).
>
> | Option | Action | Impact business | Risque sécurité |
> |--------|--------|----------------|----------------|
> | A — Chirurgical | Isoler les 3 DC + 40 machines identifiées via EDR | Production maintenue sauf serveurs de fichiers | Élevé — des machines compromises non identifiées restent actives |
> | B — Sites touchés | Coupure Internet + isolation inter-sites pour Fos, Lyon, Cologne | Production arrêtée sur 3 sites (40 % de la capacité) | Modéré — le confinement couvre le périmètre connu |
> | C — Total | Coupure réseau complète d'Arvantis | Production arrêtée partout (800 K€/jour) | Faible — tout est coupé |
>
> **Décision : Option B.** Les 3 sites touchés sont isolés (coupure Internet, isolation WAN inter-sites). Les 12 autres sites maintiennent leur activité avec surveillance renforcée et blocage des flux venant des 3 sites isolés. Le site OIV de Fos est isolé en priorité. La production est arrêtée sur les 3 sites impactés.

---
