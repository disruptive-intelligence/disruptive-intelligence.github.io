---
title: Chapitre 13 — Investigation endpoint
source: Cyber/06 Détection & réponse/Détection & SOC/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

*Le chapitre le plus dense de la partie — investigation complète sur un endpoint compromis, pas à pas, avec les requêtes réelles et les résultats.*

Le workflow d'investigation endpoint appliqué au fil rouge FALCONWATCH.

**Étape 1 — Lecture de l'alerte EDR :** l'alerte CrowdStrike montre le process tree complet. Karim identifie la chaîne `WINWORD.EXE → cmd.exe → certutil.exe → rundll32.exe`. Chaque processus est examiné : PID, arguments de ligne de commande, hash, connexions réseau, fichiers créés.

**Étape 2 — Reconstitution du process tree complet dans le SIEM :** requête SPL sur les logs Sysmon Event 1 pour WKS-PROD-112 sur les dernières 24h :

```
index=sysmon host="WKS-PROD-112" EventCode=1 
| eval parent=ParentImage." (PID:".ParentProcessId.")"
| eval child=Image." (PID:".ProcessId.")"
| table _time parent child CommandLine User
| sort _time
```

Le résultat montre la séquence complète avec les timestamps — et révèle un processus supplémentaire que l'alerte EDR n'avait pas mis en avant : après le rundll32, un `cmd.exe → whoami /all` puis un `cmd.exe → net group "Domain Admins" /domain` — reconnaissance post-exploitation.

**Étape 3 — Analyse des connexions réseau du processus malveillant :** requête Sysmon Event 3 :

```
index=sysmon host="WKS-PROD-112" EventCode=3 
  ProcessId=9284
| table _time DestinationIp DestinationPort Protocol
```

Résultat : connexion HTTPS vers `185.xx.xx.xx:443` toutes les 45 secondes — beaconing C2 confirmé.

**Étape 4 — Scope assessment :** la compromission est-elle limitée à ce poste ? Requête EDR pour le hash de lib.dll sur tout le parc Norexia :

```
index=sysmon EventCode=7 SHA256="a7f3e2d8..." 
| stats count by host
```

Résultat : 0 match sur les autres postes. Requête firewall pour les connexions vers le C2 :

```
index=firewall dest_ip="185.xx.xx.xx" 
| stats count by src_ip
| sort -count
```

Résultat : 2 IP sources — `10.0.5.112` (WKS-PROD-112, connu) et `10.0.3.45` (WKS-IT-045, **nouveau** — mouvement latéral découvert).

---
