---
title: 'Chapitre 314 — Cas 1 : Phishing avec vol d''identifiants'
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - ../index.md
- - Partie 14 — Cas filés d'investigation SOC/IR (V2)
  - index.md
---

**Contexte.** Une PME en environnement cloud + SaaS. Un employé reçoit un e-mail « sécurité » imitant le fournisseur d'identité.

**Signal initial (événement → alerte).** Le SIEM corrèle : une connexion réussie à la messagerie cloud depuis un pays inhabituel, quelques minutes après que l'utilisateur a soumis ses identifiants sur un domaine récemment enregistré (vu dans les logs proxy/DNS).

**Classement taxonomique.** Surface : identité + messagerie (ch. 49, 57). Vulnérabilité-racine : confiance humaine + absence de MFA résistant au phishing (ch. 62). Attaque : phishing → vol d'identifiants (ch. 203), suivi possible d'un consent phishing (ch. 217). Tactique ATT&CK : *Initial Access / Credential Access*.

**Hypothèse.** « Un compte a été hameçonné ; l'attaquant teste l'accès et va chercher à persister (règles de boîte, octroi OAuth) puis à pivoter. »

**Sources de logs utiles.**

- Journaux de connexion du fournisseur d'identité (sign-in logs) : localisation, appareil, ASN, statut MFA.
- Journaux de la messagerie cloud : création de **règles de transfert/suppression** (signal faible majeur de compromission), accès inhabituels.
- Logs proxy/DNS : domaine de phishing visité.
- Journaux d'**octrois OAuth** : application tierce nouvellement autorisée.

**Investigation / pivots.**

1. Confirmer la connexion suspecte (lieu, appareil, heure) et son écart avec la ligne de base de l'utilisateur.
2. Chercher les **mécanismes de persistance** propres au cloud : règles de boîte cachées, octroi OAuth, inscription d'un nouveau facteur MFA par l'attaquant.
3. Vérifier les accès aux fichiers/SharePoint et les envois sortants (exfiltration, fraude type BEC — ch. 209).
4. Identifier les autres destinataires de la campagne (même expéditeur/domaine) pour mesurer l'ampleur.

**Confinement.** Invalider les sessions actives (révoquer les jetons), réinitialiser le mot de passe, désactiver temporairement le compte si besoin, bloquer le domaine de phishing (proxy/DNS/mail), retirer les règles de boîte malveillantes.

**Éradication.** Supprimer les octrois OAuth illégitimes, retirer tout facteur MFA ajouté par l'attaquant, confirmer l'absence de backdoor cloud. Élargir aux autres comptes ciblés par la campagne.

**Rétablissement.** Réactiver le compte avec **MFA résistant au phishing** (FIDO2/passkeys — ch. 282), surveiller étroitement les connexions, informer l'utilisateur.

**REX.** Renforcer le filtrage mail et SPF/DKIM/DMARC (ch. 294), passer au MFA anti-phishing, ajouter une détection « création de règle de transfert externe » et « octroi OAuth à risque », simuler un phishing de sensibilisation.

⚠️ **Erreurs à éviter.** Réinitialiser le mot de passe *sans* révoquer les sessions (le jeton volé reste valide — ch. 191) ; oublier les persistances cloud (règles, OAuth, MFA ajouté) ; ne pas chercher les autres victimes de la campagne.

🎯 **À retenir.** Un phishing cloud ne s'arrête pas au mot de passe : il faut révoquer les sessions *et* traquer la persistance (règles de boîte, OAuth, MFA ajouté). Le MFA anti-phishing est la correction de fond.

---
