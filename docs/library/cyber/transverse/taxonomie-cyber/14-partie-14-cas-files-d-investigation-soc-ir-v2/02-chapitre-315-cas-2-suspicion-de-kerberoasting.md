---
title: 'Chapitre 315 — Cas 2 : Suspicion de Kerberoasting'
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - ../index.md
- - Partie 14 — Cas filés d'investigation SOC/IR (V2)
  - index.md
---

**Contexte.** Domaine Active Directory on-premise. Un poste utilisateur a déjà été compromis (accès initial obtenu).

**Signal initial.** Le SIEM remonte un **volume anormal de demandes de tickets de service** (TGS-REQ) émanant d'un seul poste, ciblant plusieurs comptes de service dotés d'un SPN, avec demande d'un chiffrement faible.

**Classement taxonomique.** Surface : Active Directory / identité (ch. 43). Vulnérabilité-racine : comptes de service à mot de passe faible + SPN exposés (ch. 160). Attaque : Kerberoasting (ch. 163). Tactique ATT&CK : *Credential Access (T1558.003)*.

**Hypothèse.** « Un attaquant déjà présent récolte des tickets de comptes de service pour casser leurs mots de passe hors ligne et élever ses privilèges. »

**Sources de logs utiles.**

- Journaux Kerberos des contrôleurs de domaine : **demandes de tickets de service** (Event ID 4769), en filtrant sur les chiffrements faibles et le volume par compte source.
- EDR du poste source : processus à l'origine des demandes, comportement de collecte.
- Inventaire AD : comptes de service avec SPN, leurs privilèges et l'ancienneté de leurs mots de passe.

**Investigation / pivots.**

1. Identifier le poste/compte à l'origine des demandes (le « qui »).
2. Lister les comptes de service ciblés et **évaluer leur danger** : sont-ils privilégiés ? mots de passe faibles/anciens ?
3. Vérifier si un cassage a déjà abouti : connexions réussies récentes de ces comptes de service depuis des emplacements anormaux (signal d'élévation réussie).
4. Rechercher la suite logique : mouvement latéral (ch. 182), tentative vers le Tier 0 (ch. 162).

**Confinement.** Isoler le poste source (EDR), désactiver/forcer le changement des comptes de service à risque, surveiller le Tier 0.

**Éradication.** Réinitialiser les mots de passe des comptes de service compromis (idéalement migrer vers **gMSA** à rotation automatique — ch. 163), retirer les SPN inutiles, vérifier l'absence de persistance (tickets forgés — ch. 171/172, shadow credentials — ch. 179).

**Rétablissement.** Remettre le poste en service après reconstruction, durcir les comptes de service, renforcer la surveillance Kerberos.

**REX.** Imposer gMSA / mots de passe longs aléatoires aux comptes de service, appliquer le tiering (ch. 162), créer/affiner la détection « TGS-REQ en volume + chiffrement faible », auditer régulièrement les SPN et privilèges.

⚠️ **Erreurs à éviter.** Traiter l'alerte comme un simple « bruit Kerberos » sans vérifier le cassage réussi ; réinitialiser les comptes de service sans corriger leur faiblesse de fond (gMSA) ; ignorer la progression possible vers le Tier 0.

🎯 **À retenir.** Le Kerberoasting est silencieux et hors-ligne : la détection se fait sur le *comportement de demande* (volume TGS-REQ, chiffrement faible), et la correction de fond est gMSA + tiering.

---
