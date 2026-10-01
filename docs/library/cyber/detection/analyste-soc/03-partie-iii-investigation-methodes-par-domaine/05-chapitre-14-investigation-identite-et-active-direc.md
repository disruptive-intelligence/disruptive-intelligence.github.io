---
title: Chapitre 14— Investigation identité et Active Directory
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

Investigation des compromissions d'identité appliquée au fil rouge.

**Détection du mouvement latéral :** Event ID 4624 type 3 sur WKS-IT-045 depuis `10.0.5.112` (WKS-PROD-112) avec le compte `marc.dubois` :

```
index=windows host="WKS-IT-045" EventCode=4624 LogonType=3 
| table _time TargetUserName IpAddress LogonType AuthenticationPackageName
```

Suivi immédiatement d'un Event ID 7045 (service PSEXESVC installé) — confirmation que PsExec a été utilisé pour le mouvement latéral.

**Détection du Kerberoasting :** Event ID 4769 sur DC01 avec encryption type 0x17 depuis WKS-PROD-112 :

```
index=windows host="DC01" EventCode=4769 TicketEncryptionType=0x17 
| stats count values(ServiceName) by IpAddress
| where count > 5
```

Résultat : 8 comptes de service ciblés, dont `svc-scada` (compte avec accès aux systèmes de supervision industrielle). L'attaquant a demandé des tickets Kerberos RC4 pour craquer les mots de passe offline. **C'est le moment pivot** : si `svc-scada` est cracké, l'attaquant a accès au réseau OT. Escalade immédiate.

**Vérification des modifications AD :** Event ID 5136 (modifications d'objets LDAP) et 4728/4732 (ajouts à des groupes) sur le DC dans la fenêtre temporelle de l'incident — aucune modification détectée. L'attaquant n'a pas encore utilisé le compte svc-scada — il est encore en phase de cracking offline.

---
