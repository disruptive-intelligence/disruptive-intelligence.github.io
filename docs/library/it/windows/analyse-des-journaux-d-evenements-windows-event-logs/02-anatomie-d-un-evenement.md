---
title: Anatomie d'un événement
source: IT/02 Windows/Journaux & investigation/Analyse des journaux d'événements Windows (Event Logs).md
note: Analyse des journaux d'événements Windows (Event Logs)
up:
- - Analyse des journaux d'événements Windows (Event Logs)
  - index.md
---

## Event ID

- Un **Event ID** est un identifiant numérique permettant d’identifier un type d’événement généré par un provider.

Exemple :
![Windows Event Log Analysis-009](../../../assets/analyse-des-journaux-d-evenements-windows-event-logs-windows-event-log-analysis-009.webp)

```
4624
→ Successful Logon
```


Un événement contient généralement plusieurs champs :

```
Event ID
Provider / Source
Timestamp
Computer
User
Level
Event Data
```


> ⚠️ Un Event ID n’est pas forcément **globalement unique dans tout Windows**. Sa signification doit être interprétée avec son **Provider / Source et son journal**.

Donc :

```
Event ID alone
≠ Complete Context
```


Exemple :

```
4624
+
Username
+
Logon Type
+
Source IP
+
Hostname
+
Timestamp
→ Useful Security Context
```

## Event Levels
Les événements peuvent être classés selon leur niveau.

| Level           | Signification                                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Critical**    | Indique un problème important dans une application ou un système nécessitant une attention urgente.                                  |
| **Error**       | Erreur ayant entraîné une perte de fonctionnalité                                                                                    |
| **Warning**     | Ce type d'événement signifie qu'il y a un problème mineur qui pourrait entraîner des problèmes plus importants à l'avenir.           |
| **Information** | Ce type d'événement signifie qu'une opération s'est terminée avec succès et qu'une description générale de celle-ci est enregistrée. |
| **Verbose**     | informations détaillées de diagnostic / progression                                                                                  |

> Le niveau indique la **nature / gravité opérationnelle du message**, pas nécessairement sa criticité cyber.

Par exemple :

```
Information Event
→ peut malgré tout être extrêmement intéressant en investigation
```

## Security Keywords
Dans le journal `Security`, on rencontre notamment :
### Audit Success

- Une opération soumise à audit a réussi.

Exemple :

```
Successful Logon
→ Audit Success
```

### Audit Failure

- Une opération soumise à audit a échoué.

Exemple :

```
Failed Logon
→ Audit Failure
```

> `Audit Failure` ne signifie pas forcément « attaque détectée » : cela signifie simplement que **l’action auditée a échoué**.
#### Exemple : authentification Windows

```
User attempts login
        ↓
Authentication
        ↓
Success?
├─ Yes → Event ID 4624
└─ No  → Event ID 4625
```

Pour l’analyse SOC, on ne cherche donc pas uniquement :

```
4624 / 4625
```

mais plutôt :

```
Who?
Where from?
Which host?
Which Logon Type?
When?
How often?
What happened next?
```

#### Utilité SOC / Incident Response
Les Windows Event Logs permettent notamment de reconstruire :

```
Initial Access
→ Execution
→ Persistence
→ Privilege Escalation
→ Credential Access
→ Lateral Movement
→ Impact
```

Exemples :

```
4624 → Logon
4688 → Process Creation
7045 → Service Installed
4698 → Scheduled Task Created
4720 → Account Created
1102 → Security Log Cleared
```


Mais :

```
Event ID
→ Indicator / Artifact
≠ preuve automatique d'activité malveillante
```


La valeur des Event Logs vient surtout de leur **corrélation dans le temps avec les utilisateurs, processus, machines, adresses IP et autres sources de télémétrie**.
