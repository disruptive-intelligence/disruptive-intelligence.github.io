---
title: Chapitre 24 — Confinement par type d'incident
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie V — Confinement, décision et préservation de preuve
  - index.md
---

Ce chapitre détaille les stratégies de confinement spécifiques aux types d'incidents les plus courants.

**Ransomware :** confinement réseau immédiat des segments touchés (priorité absolue), isolation du C2 (blocage du domaine/IP au pare-feu), protection immédiate des sauvegardes (déconnexion physique du NAS si sur le même réseau), vérification de l'intégrité des sauvegardes offline. Ne PAS éteindre les machines avant collecte forensic (la RAM contient des preuves critiques).

**Compromission de compte / BEC :** désactivation du compte, reset du mot de passe, révocation de toutes les sessions actives, vérification des règles de forwarding email, notification aux contacts qui ont pu recevoir des emails frauduleux.

**Exfiltration / espionnage :** bloquer le canal d'exfiltration identifié (mais attention : l'attaquant peut avoir plusieurs canaux), évaluer si l'observation contrôlée est préférable au confinement immédiat (pour comprendre l'étendue avant de couper).

**OT :** confinement de l'interface IT/OT (coupure des passerelles de supervision, isolation du réseau OT via le pare-feu IT/OT), vérification de l'intégrité des configurations d'automates avec les ingénieurs de production. Ne JAMAIS redémarrer un automate sans validation des ingénieurs — un automate dans un état intermédiaire peut causer un accident physique.

**Supply chain :** isolation immédiate du lien avec le tiers compromis (désactivation VPN, blocage des flux réseau, révocation des API keys), notification du fournisseur.

---
