---
title: Annexe E — Playbooks types détaillés
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

Les playbooks complets sont structurés selon le format du Ch.7 : trigger, actions immédiates (0-15 min), actions d'investigation (15 min-4h), actions de confinement, critères d'escalade, communication, et clôture. Pour des raisons de volume, seuls les éléments clés de chaque playbook sont listés ici. Les versions complètes, avec les commandes exactes par outil (Splunk, CrowdStrike, Sentinel, Velociraptor), doivent être adaptées à l'environnement spécifique de chaque organisation.

## Playbook Ransomware — Éléments clés

**Trigger :** Détection EDR (chiffrement de fichiers, exécution de binaire suspect), ou découverte de fichiers chiffrés / note de rançon.

**Actions immédiates (0-15 min) :** Ne PAS éteindre les machines. Isoler via EDR (network containment). Protéger les sauvegardes (déconnexion physique immédiate du NAS réseau). Alerter l'IR lead.

**Actions critiques :** Identifier le variant (note de rançon, extension des fichiers, hash du binaire). Évaluer l'étendue du chiffrement (combien de machines, quel pourcentage du parc). Vérifier l'intégrité des sauvegardes (sont-elles chiffrées ? antérieures à la compromission ?). Vérifier la compromission de l'AD (DCSync ? krbtgt ?). Estimer l'exfiltration (double extorsion ?).

**Escalade :** P1 automatique si plus de 10 machines chiffrées OU si un DC est compromis OU si les sauvegardes sont touchées.

## Playbook Compromission de compte — Éléments clés

**Trigger :** Alerte SIEM (geo-impossible travel, connexion depuis IP suspecte, activité anormale), ou signalement utilisateur.

**Actions immédiates :** Désactiver le compte. Révoquer toutes les sessions actives et refresh tokens. Reset du mot de passe.

**Investigation :** Revue de l'activité du compte sur les 30 derniers jours (Sign-in Logs, UAL). Recherche de règles de forwarding email. Recherche de consentements OAuth suspects. Vérification : le phishing initial a-t-il touché d'autres utilisateurs ?

## Playbook Exfiltration — Éléments clés

**Trigger :** Alerte DLP, volume anormal de trafic sortant, notification externe (données trouvées sur un forum).

**Actions immédiates :** Identifier le canal d'exfiltration (destination, protocole, outil). Bloquer le canal si identifié.

**Investigation :** Identifier les données exfiltrées (quels partages accédés, quels fichiers, quel volume). Identifier la source (quelle machine, quel compte). Remonter au point d'entrée.

**Notification :** CNIL sous 72h si données personnelles.

---
