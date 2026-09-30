---
title: Questions complémentaires
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - index.md
---

- **Question :** Quand décidez-vous de confiner immédiatement vs observer ?
  - **Réponse type :** Confinement immédiat si l'impact est destructif (ransomware en cours, exfiltration active, risque OT). Observation contrôlée si l'attaquant est discret et ne sait pas qu'il est détecté — ça permet de comprendre l'étendue avant de couper, et d'identifier tous les mécanismes de persistence. Mais cette décision est un arbitrage : observer c'est prendre le risque que l'attaquant accélère. En cas de doute, le confinement prime — surtout s'il y a un risque physique (OT) ou des données sensibles en jeu.

- **Question :** Quels sont les cadres méthodologiques IR que vous connaissez ?
  - **Réponse type :** Les deux principaux sont le NIST SP 800-61 (4 phases : Préparation, Détection-Analyse, Confinement-Éradication-Restauration, Post-Incident) et le SANS PICERL (6 phases : Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned). En France, on a aussi le cadre ANSSI/CERT-FR et le référentiel PRIS pour la qualification des prestataires d'IR. En parallèle, MITRE ATT&CK est utilisé comme grille de lecture pour mapper les TTP observées.

- **Question :** Qu'est-ce qu'un RETEX et pourquoi c'est essentiel ?
  - **Réponse type :** Le RETEX (retour d'expérience) est l'analyse post-incident : timeline complète, vecteur initial, chemins d'escalade, persistence, ce qui a fonctionné et ce qui a échoué, et les recommandations d'amélioration. C'est essentiel parce que sans RETEX, on ne corrige pas les causes racines et on revit le même incident. Un bon RETEX produit des actions concrètes priorisées — pas juste un rapport technique, mais un plan d'amélioration avec des responsables et des délais.


## Questions les plus probables en entretien

1. Phases de la réponse à incident ?
2. Événement vs alerte vs incident vs crise ?
3. Ransomware en cours : premières actions ?
4. Pourquoi la préparation est critique ?
5. Comment construire une timeline d'attaque ?
6. Confiner immédiatement ou observer ?
