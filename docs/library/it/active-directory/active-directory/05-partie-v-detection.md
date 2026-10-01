---
title: Partie V — Détection
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

---


## Chapitre 19 — Minimum Viable Visibility : la télémétrie indispensable

Les 10 sources à activer et centraliser (par priorité) : (1) Security logs sur tous les DC (Advanced Audit Policy), (2) Directory Service Changes (Event 5136), (3) PowerShell ScriptBlock Logging + Module Logging, (4) Sysmon sur DC et Tier 0/1, (5) LDAP query logging (Event 1644), (6) Logs Kerberos détaillés (4768/4769/4771), (7) WEF ou agent SIEM vers centralisation, (8) EDR sur DC et PAW, (9) Logs AD CS (enrollment, modifications templates — Event 4887), (10) DNS query logging sur les DC DNS-intégrés. Sans cette télémétrie, même le meilleur SOC est aveugle sur AD.

---


## Chapitre 20 — Détecter les attaques AD dans le SIEM

Pour chaque technique, le triptyque : signal compatible + corrélation nécessaire + faux positifs courants. **Kerberoasting** (4769 RC4 en volume → vérifier la baseline du compte, l'encryption demandée). **AS-REP Roasting** (4768 sans pré-auth → lister les comptes DONT_REQUIRE_PREAUTH). **DCSync** (4662 avec droits de réplication depuis non-DC = alerte critique → vérifier : la machine source est-elle un DC connu ?). **Pass-the-Hash** (4624 logon type 3/9 avec processus source inhabituel → violation de tiering ?). **Golden Ticket** (TGT avec durée anormale, SID inexistant, absence d'AS-REQ). **Modifications ACL suspectes** (5136 sur objets sensibles — AdminSDHolder, GPOs, comptes DA). **Accès lsass** (Sysmon Event 10 ProcessAccess ciblant lsass.exe → processus source légitime ou suspect ?). **Password Spraying** (4625 en volume, 4771). **AD CS abuse** (4887 — enrollment avec SAN inhabituel, template sensible). **Shadow Credentials** (5136 sur msDS-KeyCredentialLink → qui a modifié cet attribut ? depuis quelle machine ?).

Un Event ID = un indice, pas une preuve. Chaque signal doit être évalué avec son contexte et comparé à une baseline.

---


## Chapitre 21 — Deception et honey objects

**Honey accounts** (comptes factices avec des attributs attractifs — adminCount=1, SPN, vieux mot de passe → toute interaction = alerte, zéro faux positif). **Honey SPNs** (SPNs factices sur des comptes pièges → Kerberoasting détecté immédiatement). **Honey tokens** (credentials factices sur des machines — fichiers, registre, mémoire → credential dumping détecté). **Canary files** (fichiers pièges sur des partages → énumération/exfiltration détectée). L'avantage de la deception : zéro faux positif — si un honey object est touché, c'est forcément suspect.

> **🔵 KERBEROS — Épisode 5 (Blue Team)**
>
> La Blue Team de Meridian n'avait pas déployé de honey objects. Après le pentest de Thomas, elle déploie : 1 honey account « svc_legacy » avec adminCount=1 et un SPN attractif (MSSQLSvc/legacy-db.meridian.local), 2 canary files « salaries_2025.xlsx » et « passwords.xlsx » sur un partage accessible, et des honey tokens (credentials factices) dans le registre du serveur SRV-APP01. Au prochain test, le premier Kerberoasting sur svc_legacy déclenche une alerte immédiate.

---


## Chapitre 22 — Règles SIEM et corrélation avancée

Les règles de corrélation multi-événements : **Kerberoasting avancé** (4769 RC4 + volume > seuil + pas dans la baseline = alerte haute), **mouvement latéral via tiering** (4624 logon type 3/10 + compte admin + machine Tier 2 + destination Tier 0 = violation de tiering = alerte critique), **persistence** (5136 modification AdminSDHolder/GPO + hors fenêtre de maintenance + compte non autorisé = alerte haute), **AD CS abuse** (4887 enrollment + template sensible + SAN ≠ demandeur = alerte critique), **Shadow Credentials** (5136 msDS-KeyCredentialLink + compte non attendu = alerte haute).

Réduction des faux positifs : baseline essentielle (whitelister les comptes de service légitimes, documenter les comportements attendus, tuner progressivement). Les **règles Sigma** (format portable de détection — convertibles en Splunk SPL, ELK KQL, Sentinel KQL — la communauté maintient un large set de règles AD).

---
