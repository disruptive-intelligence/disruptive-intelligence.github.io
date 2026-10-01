---
title: Partie VII — Incident response, hybrid identity et synthèse
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

---


## Chapitre 27 — Incident Response AD : méthodologie

Le scénario type (« l'EDR a détecté Mimikatz sur un serveur, l'attaquant semble avoir des credentials DA, des modifications ACL suspectes ont été détectées »). Le **triage** : quels comptes compromis ? (logs 4624, 4648, 4672), quels systèmes touchés ? (DC, serveurs, postes — signes de mouvement latéral ?), le Tier 0 est-il compromis ? (si un DC ou un DA est touché → scope maximal), depuis quand ? (date de première activité suspecte), y a-t-il de la persistence ? (Golden Ticket, ACL modifiées, GPO modifiées, comptes créés, certificats AD CS émis, Shadow Credentials ajoutées). Règle d'or : supposer le pire et vérifier.

---


## Chapitre 28 — Containment, nettoyage et rotation krbtgt

Le **containment** : isoler les systèmes compromis (couper le réseau, ne PAS éteindre — préserver la mémoire), désactiver les comptes compromis (pas supprimer), révoquer les sessions (klist purge ou rotation krbtgt si Golden Ticket suspecté), bloquer les IOCs, protéger les backups. La **rotation krbtgt** (double rotation espacée : 1ère rotation → attendre 10-12h → 2ème rotation → l'ancien hash est complètement invalidé ; ne PAS faire les deux simultanément — casse toutes les sessions).

Le **nettoyage de persistence** : comptes créés (4720 → supprimer), ACLs modifiées (comparer avec baseline → révoquer), GPOs modifiées (5136 → restaurer), SPNs ajoutés (supprimer), AdminSDHolder (nettoyer les ACEs), certificats AD CS (révoquer les certificats suspects), DCShadow (vérifier les objets nTDSDSA), Shadow Credentials (vérifier msDS-KeyCredentialLink sur les comptes sensibles — supprimer les clés non légitimes), Scheduled Tasks/Services (vérifier sur chaque DC et serveur touché).

---


## Chapitre 29 — Rebuild vs Clean et retour à la normale

Les critères : scope limité + durée courte + backups sains → clean ; Tier 0 compromis + durée longue/inconnue + pas de backup → rebuild. Le processus de rebuild (nouveaux DC, nouvelle forêt, migration — long et douloureux mais parfois nécessaire). La validation post-incident (PingCastle/BloodHound — chemins fermés ?, scanner les comptes à risque, vérifier les ACLs, confirmer la rotation krbtgt, vérifier les templates AD CS, auditer msDS-KeyCredentialLink). Le retex (timeline complète, vecteur initial, chemins d'escalade, persistence, ce qui a fonctionné/échoué, actions d'amélioration).

---


## Chapitre 30 — Entra ID / Hybrid : architecture et synchronisation

**Entra ID** (ex-Azure AD) : tenant plat (pas de forêt/domaine), protocoles OAuth 2.0/OIDC/SAML, Conditional Access au lieu de GPO, Intune au lieu de SCCM. La synchronisation **Azure AD Connect / Entra Connect** : 3 méthodes. **PHS** (Password Hash Sync — les hashes sont synchronisés vers le cloud ; le plus courant ; risque : si Entra ID est compromis, les hashes sont exposés). **PTA** (Pass-Through Auth — l'auth cloud est validée en temps réel par un agent on-prem ; l'agent PTA est Tier 0). **Federation/ADFS** (un serveur ADFS émet des tokens pour le cloud ; ADFS est Tier 0 — si compromis : Golden SAML).

**Azure AD Connect = Tier 0** — le serveur a accès aux credentials de TOUS les comptes synchronisés. Isolation, pas d'internet, accès restreint, monitoring. Les erreurs courantes : serveur AD Connect non isolé, pas dans le Tier 0, sans EDR, synchronisation de comptes DA vers le cloud, pas de filtering (tous les comptes synchronisés y compris les comptes de service).

---


## Chapitre 31 — Attaques et défense du cloud identity

Les attaques hybrid/cloud : **Token theft** (voler un access/refresh token → accès aux applications cloud sans MFA), **PRT theft** (Primary Refresh Token — le « TGT du cloud » ; vol via Mimikatz, ROADtools → SSO complet à toutes les apps Entra ID), **Consent phishing** (tromper un utilisateur pour autoriser une app malveillante → lecture emails, fichiers via Graph API), **Golden SAML** (forger des tokens SAML avec le certificat de signing ADFS → accès à toutes les apps fédérées — APT29/SolarWinds), **Azure AD backdoors** (service principals, credentials sur des apps, rôles persistants).

**Conditional Access Policies** (MFA obligatoire pour tous les admins, bloquer les connexions depuis des pays inhabituels, exiger un appareil conforme Intune, bloquer les protocoles legacy — SMTP auth, POP3, IMAP). **PIM** (Privileged Identity Management — activation temporaire JIT des rôles admin, approbation, justification, audit complet). Logs et détection cloud (Sign-in logs, Audit logs, Risky sign-ins — Entra ID Protection, Provisioning logs, MS Sentinel/Defender).

---


## Chapitre 32 — Cas de synthèse : rapport de pentest AD complet

Synthèse du fil rouge KERBEROS. Le rapport de pentest de Thomas sur Meridian Pharma.

**Résumé exécutif** (pour la direction — score PingCastle : 73/100, Domain Admin atteint en 4 heures par 2 chemins indépendants, recommandations critiques : 5 actions P0 pour réduire le risque de 80 %).

**Findings classés par criticité :**

**Critique :** ESC1 sur template VPN-User (Domain Admin en 90 secondes via AD CS), krbtgt jamais roté depuis 7 ans, 3 comptes DA avec sessions actives sur des serveurs Tier 1 (violation de tiering), Azure AD Connect non isolé avec accès internet, RODC Genève avec PRP trop large (45 comptes dont 3 comptes de service Tier 1).

**Élevé :** 12 comptes de service avec SPN et mot de passe > 3 ans (Kerberoasting surface), LLMNR/NBT-NS actifs (4 hashes capturés en 15 min), pas de Credential Guard (Mimikatz fonctionnel), pas de SMB signing (relay possible), svc_monitoring avec GenericWrite sur le groupe IT-Admins → chemin vers DA via ACL abuse.

**Moyen :** 47 comptes inactifs > 180 jours, 3 GPO modifiables par des utilisateurs non privilégiés, NTLM non restreint, pas de honey objects, logs AD CS non centralisés (la kill chain AD CS est passée inaperçue), msDS-KeyCredentialLink non monitoré.

**Kill chains documentées :** Chemin 1 (Responder → hash capture → Kerberoasting svc_backup → mouvement latéral SRV-APP01 → credential dumping → PtH vers DC → DCSync). Chemin 2 (Certipy ESC1 → certificat DA → PKINIT → TGT DA → DCSync). Chemin 3 (RODC Genève → PRP trop large → hash svc_monitoring → GenericWrite → ACL abuse → DA).

**Recommandations priorisées :** P0 immédiat (corriger ESC1, rotater krbtgt double rotation, séparer les comptes DA des serveurs Tier 1, isoler Azure AD Connect, réduire la PRP du RODC), P1 3 mois (déployer LAPS, gMSA pour les comptes de service, désactiver LLMNR/NBT-NS, SMB signing, centraliser les logs AD CS, monitorer msDS-KeyCredentialLink), P2 6 mois (Credential Guard sur les serveurs Tier 0/1, tiering complet, déployer honey objects, restreindre NTLM, audit ACL complet et remédiation BloodHound). Risques résiduels acceptés : 2 applications legacy nécessitant NTLM (compensatoire : monitoring renforcé + segmentation).

---
