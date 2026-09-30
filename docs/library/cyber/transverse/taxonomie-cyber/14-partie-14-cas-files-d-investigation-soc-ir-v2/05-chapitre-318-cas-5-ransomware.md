---
title: 'Chapitre 318 — Cas 5 : Ransomware'
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - ../index.md
- - Partie 14 — Cas filés d'investigation SOC/IR (V2)
  - index.md
---

**Contexte.** Réseau d'entreprise mixte. Accès initial obtenu (ex. RDP exposé — ch. 140, ou phishing), suivi d'un mouvement latéral.

**Signal initial.** Vague d'alertes EDR/SIEM : **chiffrement massif de fichiers** sur plusieurs serveurs, **suppression des clichés/sauvegardes** accessibles, comptes d'administration utilisés à des heures inhabituelles. Souvent précédée (rétrospectivement) de signaux faibles : reconnaissance interne, désactivation de défenses.

**Classement taxonomique.** Surface : multiple (serveurs, identité, réseau). Vulnérabilité-racine : multiple (accès exposé, réutilisation d'identifiants, absence de segmentation/tiering). Attaque : ransomware (ch. 188), souvent avec double extorsion (exfiltration préalable). Tactique ATT&CK : *Impact (T1486)*, précédé de *Lateral Movement / Exfiltration*.

**Hypothèse.** « Un opérateur de ransomware est présent depuis un certain temps ; il a probablement exfiltré avant de chiffrer (double extorsion) et cherché à neutraliser les sauvegardes. »

**Sources de logs utiles.**

- EDR/SIEM : début du chiffrement, processus responsable, propagation, suppression de clichés/sauvegardes.
- Journaux d'authentification/AD : usage de comptes d'administration, mouvement latéral (ch. 182), accès au Tier 0.
- Journaux réseau/exfiltration : volumes sortants anormaux *avant* le chiffrement (double extorsion).
- Journaux des sauvegardes : tentatives de suppression/altération.

**Investigation / pivots.**

1. Déterminer l'**étendue** (machines chiffrées, données exfiltrées) et le **point d'entrée initial** (RDP, phishing, VPN — ch. 141).
2. Reconstituer le **mouvement latéral** et l'accès aux comptes privilégiés (krbtgt compromis ? ch. 171).
3. Évaluer l'**exfiltration** (impact réglementaire et négociation).
4. Identifier les sauvegardes **saines et hors-ligne/immuables** disponibles (ch. 287).

**Confinement.** **Segmenter/isoler** massivement (couper les liaisons entre zones) pour stopper la propagation, désactiver les comptes compromis, **déclencher la cellule de crise** (ch. 39/266) et activer le **PRA/PCA** (ch. 267). Communication de crise et obligations de notification (ch. 268).

**Éradication.** Identifier et supprimer *toute* la présence de l'attaquant (backdoors, comptes, persistance, krbtgt à roter deux fois si AD compromis — ch. 171) avant toute reconnexion. Une éradication partielle = rechiffrement.

**Rétablissement.** Restaurer depuis des **sauvegardes immuables et vérifiées** (ch. 287), reconstruire les systèmes critiques, corriger le vecteur initial, surveiller étroitement la réapparition de l'attaquant pendant la reprise.

**REX.** Supprimer les expositions (RDP/VPN — ch. 140/141), imposer MFA et tiering, déployer des sauvegardes immuables testées, segmenter, améliorer la détection précoce (reconnaissance interne, désactivation de défenses, suppression de clichés), réaliser des exercices de crise (tabletop — ch. 304).

⚠️ **Erreurs à éviter.** Restaurer avant d'avoir éradiqué (rechiffrement) ; restaurer depuis une sauvegarde elle-même compromise/en ligne ; négliger l'exfiltration (la double extorsion change la gestion de crise) ; payer en croyant que cela garantit la récupération (un wiper déguisé — ch. 189 — ne déchiffre rien).

🎯 **À retenir.** Le ransomware est l'aboutissement d'une intrusion complète : confiner (segmenter) + cellule de crise + éradication exhaustive *avant* restauration depuis l'immuable. La prévention de fond combine sauvegardes immuables testées, segmentation, tiering, MFA et détection précoce.

---
