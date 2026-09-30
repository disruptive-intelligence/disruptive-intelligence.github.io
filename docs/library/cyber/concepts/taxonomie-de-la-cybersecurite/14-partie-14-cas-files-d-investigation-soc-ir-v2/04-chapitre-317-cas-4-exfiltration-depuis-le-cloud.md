---
title: 'Chapitre 317 — Cas 4 : Exfiltration depuis le cloud'
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - ../index.md
- - Partie 14 — Cas filés d'investigation SOC/IR (V2)
  - index.md
---

**Contexte.** Environnement cloud IaaS. Une clé d'accès a fuité (dépôt public — ch. 222).

**Signal initial.** Les journaux d'audit cloud montrent un usage d'une clé d'accès depuis une adresse inhabituelle, avec une rafale d'opérations de **listing et de lecture sur des buckets** de stockage.

**Classement taxonomique.** Surface : cloud (ch. 46). Vulnérabilité-racine : secret exposé + permissions excessives (ch. 221/219). Attaque : usage de clé volée → accès aux données → exfiltration ; risque d'élévation (ch. 224) et de lateral movement cloud (ch. 225). Tactique ATT&CK : *Collection / Exfiltration*.

**Hypothèse.** « Une clé exposée est utilisée pour lire et exfiltrer des données ; l'attaquant peut tenter d'élever ses privilèges et de persister (nouvelle clé/utilisateur). »

**Sources de logs utiles.**

- Journaux d'audit cloud (type CloudTrail / journaux d'activité) : appels d'API, source, identité utilisée, opérations sur le stockage.
- Journaux d'accès au stockage : volumes lus/téléchargés (mesurer l'exfiltration).
- Journaux IAM : création de clés/utilisateurs/rôles, modifications de politiques (persistance/élévation).

**Investigation / pivots.**

1. Identifier la clé compromise et **toutes** ses actions (lecture, mais aussi création d'accès, modification de politiques).
2. Mesurer le périmètre de données exfiltrées (quels buckets, quel volume) — impact réglementaire potentiel.
3. Chercher la **persistance** : nouvelles clés/utilisateurs/rôles créés, politiques modifiées (auto-élévation — ch. 224).
4. Vérifier le rebond vers d'autres comptes/services (relations de confiance — ch. 225).

**Confinement.** **Révoquer/désactiver immédiatement la clé** compromise, restreindre les accès au stockage concerné, bloquer la source si possible.

**Éradication.** Supprimer toute persistance créée (clés/utilisateurs/rôles illégitimes), corriger les politiques modifiées, faire tourner les secrets potentiellement exposés.

**Rétablissement.** Émettre de nouveaux secrets à portée minimale, durcir les permissions (moindre privilège IAM — ch. 219), activer le blocage public par défaut (ch. 220), renforcer la surveillance.

**REX.** Déployer le **secrets scanning** (ch. 300) et un coffre-fort (ch. 244), appliquer le moindre privilège IAM et l'analyse des chemins d'élévation, activer/affiner les alertes « usage de clé depuis source inhabituelle » et « création d'accès IAM », gérer l'obligation de notification si fuite de données personnelles (ch. 268).

⚠️ **Erreurs à éviter.** Désactiver la clé sans chercher la persistance IAM créée entre-temps ; sous-estimer le périmètre de données (impact réglementaire) ; réémettre des secrets surprivilégiés.

🎯 **À retenir.** Une clé cloud volée mène vite à l'exfiltration *et* à la persistance IAM : révoquer la clé ne suffit pas, il faut traquer les accès créés et corriger le moindre privilège. La prévention de fond est le coffre-fort + le scanning.

---
