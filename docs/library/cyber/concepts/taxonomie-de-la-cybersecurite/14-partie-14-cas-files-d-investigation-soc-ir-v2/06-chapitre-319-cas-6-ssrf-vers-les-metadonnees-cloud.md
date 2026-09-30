---
title: 'Chapitre 319 — Cas 6 : SSRF vers les métadonnées cloud'
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - ../index.md
- - Partie 14 — Cas filés d'investigation SOC/IR (V2)
  - index.md
---

**Contexte.** Application web hébergée sur une instance cloud, exposant une fonctionnalité qui récupère une ressource à partir d'une URL fournie.

**Signal initial.** Le NDR/journaux applicatifs montrent que le **serveur applicatif initie des requêtes vers l'adresse interne du service de métadonnées** de l'instance, puis un usage anormal des identifiants de rôle de l'instance apparaît dans les journaux cloud.

**Classement taxonomique.** Surface : web + cloud (ch. 44/46). Vulnérabilité-racine : validation/allowlist d'URL insuffisante + confiance (ch. 80). Attaque : SSRF → métadonnées cloud (ch. 105/107). Tactique ATT&CK : *Credential Access / Discovery*.

**Hypothèse.** « Une SSRF est exploitée pour atteindre le service de métadonnées et récupérer les identifiants temporaires du rôle de l'instance, ensuite utilisés pour accéder aux ressources cloud. »

**Sources de logs utiles.**

- Journaux applicatifs / reverse proxy : URL fournies en paramètre, requêtes sortantes du serveur.
- NDR / journaux réseau : **accès au point de métadonnées** depuis l'application (signal fort).
- Journaux d'audit cloud : usage des identifiants de rôle d'instance depuis des contextes anormaux, opérations sur les ressources.

**Investigation / pivots.**

1. Confirmer la SSRF (paramètre d'URL menant à l'adresse de métadonnées) et son exploitation.
2. Déterminer si des **identifiants de rôle** ont été récupérés et utilisés (journaux cloud).
3. Mesurer les actions effectuées avec ce rôle (lecture/exfiltration, élévation, persistance — comme le Cas 4).
4. Identifier le périmètre des ressources accessibles via ce rôle (impact lié au moindre privilège).

**Confinement.** Corriger/bloquer la fonctionnalité vulnérable (allowlist stricte, blocage de l'adresse de métadonnées), **révoquer/roter les identifiants de rôle** potentiellement exposés, restreindre les actions du rôle.

**Éradication.** Supprimer toute persistance créée avec le rôle (cf. Cas 4), corriger le code de l'application (allowlist de destinations, normalisation d'URL — ch. 105).

**Rétablissement.** Déployer la version corrigée, activer la **version renforcée du service de métadonnées** (étape supplémentaire requise pour y accéder), appliquer le **moindre privilège** au rôle d'instance, renforcer la surveillance.

**REX.** Généraliser la version renforcée des métadonnées et le filtrage sortant (egress filtering), revoir les rôles d'instance (moindre privilège), ajouter une détection « accès applicatif au point de métadonnées », intégrer un test SSRF aux campagnes DAST (ch. 297).

⚠️ **Erreurs à éviter.** Corriger la SSRF sans roter les identifiants déjà exposés ; laisser le service de métadonnées en version permissive ; conserver un rôle d'instance surprivilégié.

🎯 **À retenir.** Une SSRF côté web devient un vol d'identifiants côté cloud : la réponse couvre les *deux* surfaces (corriger le code + roter le rôle + durcir les métadonnées). Prévention de fond : allowlist SSRF, métadonnées renforcées, moindre privilège des rôles.

---

> **Synthèse de la Partie 14.** Ces six cas illustrent un invariant : un incident traverse presque toujours *plusieurs surfaces* (un phishing devient un incident identité ; une SSRF devient un incident cloud ; un malware de poste devient un vol d'identifiants). Le réflexe opérationnel est donc : **comprendre la portée complète avant d'agir**, **confiner sans détruire les preuves**, **éradiquer exhaustivement** (toute la persistance) *avant* de **rétablir depuis du sain**, puis **apprendre** (REX). C'est l'application vivante du fil rouge et de la posture *assume breach*.

---
