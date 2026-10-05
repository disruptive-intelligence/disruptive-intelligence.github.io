---
title: 'Synthèse : verrouillage et patterns SOC'
source: IT/02 Windows/Journaux & investigation/Analyse des journaux d'événements Windows (Event Logs).md
note: Analyse des journaux d'événements Windows (Event Logs)
up:
- - Analyse des journaux d'événements Windows (Event Logs)
  - index.md
---

## Account Lockout Policy

- Une **Account Lockout Policy** peut limiter certaines attaques par password guessing :
    - nombre maximal d’échecs ;
    - durée du lockout ;
    - délai avant reset du compteur.

```text
Repeated Failed Logons
→ Threshold reached
→ Account Locked
```


Mais il faut trouver un équilibre :

```text
Threshold too low
→ Attacker can intentionally lock accounts
→ Denial of Service
```


> Le lockout protège surtout contre les attaques de **password guessing**. Il ne bloque pas directement des techniques utilisant des credentials déjà compromis, comme **Pass-the-Hash**.

---

## Patterns SOC importants

### Brute Force

```text
One Account
+
Many 4625
+
Same Source
+
Short Time Window
→ Brute Force Suspicion
```


### Password Spray

```text
Many Accounts
+
Same Source
+
Few Password Attempts
→ Password Spray Suspicion
```


### Successful compromise

```text
Many 4625
        ↓
4624
        ↓
Suspicious Activity
→ High-Priority Investigation
```


### RDP Lateral Movement

```text
Compromised Host
+
RDPClient Events
+
4624 Type 10 on destination
+
1149
→ Possible Lateral Movement
```


---

## Vue d’ensemble

```text
Authentication Analysis
│
├─ 4624
│  → Successful Logon
│
├─ 4625
│  → Failed Logon
│
├─ Logon Type
│  ├─ 2  → Interactive
│  ├─ 3  → Network
│  ├─ 5  → Service
│  └─ 10 → RemoteInteractive / RDP
│
└─ RDP
   ├─ 261  → TCP connection
   ├─ 1149 → RDP authentication success
   ├─ 4624 Type 10 → Successful RDP logon
   ├─ 4625 Type 10 → Failed RDP logon
   ├─ 4648 → Explicit credentials
   └─ RDPClient 1102 → Destination information
```


Le point important est de ne jamais analyser uniquement **un Event ID** : pour reconstruire une authentification ou un lateral movement fiable, il faut corréler **Event ID + Provider + Logon Type + utilisateur + source IP + machine cible + timeline**.

Récapitulatif du cours, thème par thème :

| Thème | Journal | Event IDs |
|---|---|---|
| Authentification | Security | 4624, 4625 (+ Logon Type) |
| RDP, machine cible | Security · TerminalServices-RemoteConnectionManager | 4624 / 4625 Type 10 · 261, 1149 |
| RDP, machine source | TerminalServices-RDPClient · Security | 1102 · 4648 |
| Tâches planifiées | Security (si audit) · TaskScheduler/Operational | 4698, 4702, 4699, 4700 / 4701 · 106, 140, 141, 200, 201 |
| Services | System (Service Control Manager) · Security (si audit) | 7045, 7040, 7036 · 4697 |
| Gestion des comptes | Security | 4720, 4722, 4725, 4726, 4738, 4723 / 4724 · 4728 / 4732 / 4756 · 4729 / 4733 / 4757 |
