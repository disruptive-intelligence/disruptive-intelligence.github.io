---
title: Chapitre 5 — Bastion, PAM et Zero Trust
source: IT/06 Infrastructure & architecture/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - ../index.md
- - Partie I — Réseau, protocoles et services fondamentaux
  - index.md
---

Le **bastion/jump host** est un serveur renforcé, placé dans la zone d'administration, qui sert de point de passage obligatoire pour accéder aux serveurs internes. Principe : l'admin se connecte au bastion, puis du bastion vers le serveur cible (SSH ProxyJump — ssh -J bastion user@serveur_interne). Les serveurs cibles n'acceptent les connexions que depuis le bastion. Le bastion enregistre toute l'activité (commandes tapées avec horodatage, vidéo de session rejouable pour l'audit, fichiers transférés loggés). Comptes nominatifs obligatoires (pas de compte « admin » partagé — traçabilité individuelle). MFA obligatoire sur le bastion.

Le **PAM** (Privileged Access Management) est la solution de gestion des accès privilégiés : coffre-fort de mots de passe (stockage chiffré des credentials des comptes à privilèges), rotation automatique (les mots de passe sont changés après chaque utilisation), enregistrement de sessions (toutes les sessions privilégiées sont enregistrées), et injection de credentials (l'admin ne connaît pas le mot de passe root — le PAM l'injecte automatiquement). Solutions : CyberArk, Wallix, BeyondTrust, Delinea, Teleport, Apache Guacamole (open source).

**Zero Trust vs périmétrique :** le modèle périmétrique traditionnel (intérieur = sûr, extérieur = dangereux — le firewall est la frontière ; problème : une fois à l'intérieur, mouvement latéral facile) cède la place au Zero Trust (ne jamais faire confiance, toujours vérifier — chaque accès est authentifié et autorisé même depuis le LAN ; MFA, micro-segmentation, vérification continue, context-aware access).

---
