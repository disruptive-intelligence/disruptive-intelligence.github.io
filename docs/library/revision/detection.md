---
title: Révision — Détection & réponse
revision: cyber/detection
domaine: Cyber
sources:
- Cyber/06 Détection & réponse/Réponse à incident.md
- Révision/Threat hunting — questions de révision.md
---

## Réponse à incident

*D'après le cours [Réponse à incident](../cyber/detection/reponse-a-incident/index.md)*

### Questions essentielles

- **Question :** Quelles sont les grandes phases de la réponse à incident ?
  - **Réponse type :** Le NIST 800-61 définit 4 phases : Préparation (avant l'incident — playbooks, outillage, exercices), Détection et Analyse (du signal faible à l'incident confirmé, triage, scoping), Confinement-Éradication-Restauration (isoler, nettoyer, reconstruire), et Post-Incident (retex, amélioration). En réalité, ces phases ne sont pas linéaires — on investigue pendant qu'on contient, on découvre de nouvelles compromissions pendant l'éradication. C'est itératif et parallèle.

- **Question :** Quelle est la différence entre un événement, une alerte, un incident et une crise ?
  - **Réponse type :** Un événement c'est tout fait observable dans le SI — il y en a des milliards par jour. Une alerte c'est un événement signalé comme potentiellement anormal par un système de détection. Un incident c'est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité ou la disponibilité. Une crise c'est un incident dont l'impact dépasse la capacité de réponse normale et nécessite une gouvernance exécutive. Ces distinctions déterminent le niveau de mobilisation, les processus activés, et les obligations de notification.

- **Question :** Un ransomware est en cours de déploiement — que faites-vous en priorité ?
  - **Réponse type :** Confinement immédiat. Chaque minute qui passe c'est des machines supplémentaires chiffrées. On isole les segments réseau touchés — on coupe la connectivité mais on n'éteint PAS les machines pour préserver la mémoire (qui contient les clés de chiffrement et les artefacts forensic). On désactive les comptes compromis. On protège les sauvegardes — si elles sont accessibles par les mêmes credentials, c'est la priorité absolue. En parallèle, on commence le scoping : l'attaquant est-il ailleurs dans le réseau ?

- **Question :** Pourquoi la préparation est-elle si importante en IR ?
  - **Réponse type :** Parce que le jour de l'incident, il est trop tard pour construire les processus. La préparation détermine tout : est-ce qu'on a un IRP avec des playbooks par type d'incident ? Est-ce qu'on a la télémétrie nécessaire pour investiguer ? Est-ce qu'on sait qui appeler à 2h du matin ? Est-ce qu'on a un contrat avec un prestataire PRIS ? Est-ce qu'on a testé la restauration des sauvegardes ? Une organisation préparée contient un ransomware en quelques heures. Une organisation non préparée met des semaines et paie souvent la rançon.

- **Question :** Comment construisez-vous une timeline d'attaque ?
  - **Réponse type :** La timeline reconstitue chronologiquement toutes les actions de l'attaquant. On croise plusieurs sources : les logs EDR/Sysmon (processus, connexions), les Event Logs Windows (4624 logons, 4698 scheduled tasks), les logs d'authentification AD, les logs proxy/DNS, et les artefacts forensic (prefetch, amcache, MFT). On cherche le point d'entrée initial, les pivots, les escalades de privilèges, les persistances, et les actions sur objectif. La timeline est le livrable central de l'investigation.

### Questions complémentaires

- **Question :** Quand décidez-vous de confiner immédiatement vs observer ?
  - **Réponse type :** Confinement immédiat si l'impact est destructif (ransomware en cours, exfiltration active, risque OT). Observation contrôlée si l'attaquant est discret et ne sait pas qu'il est détecté — ça permet de comprendre l'étendue avant de couper, et d'identifier tous les mécanismes de persistence. Mais cette décision est un arbitrage : observer c'est prendre le risque que l'attaquant accélère. En cas de doute, le confinement prime — surtout s'il y a un risque physique (OT) ou des données sensibles en jeu.

- **Question :** Quels sont les cadres méthodologiques IR que vous connaissez ?
  - **Réponse type :** Les deux principaux sont le NIST SP 800-61 (4 phases : Préparation, Détection-Analyse, Confinement-Éradication-Restauration, Post-Incident) et le SANS PICERL (6 phases : Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned). En France, on a aussi le cadre ANSSI/CERT-FR et le référentiel PRIS pour la qualification des prestataires d'IR. En parallèle, MITRE ATT&CK est utilisé comme grille de lecture pour mapper les TTP observées.

- **Question :** Qu'est-ce qu'un RETEX et pourquoi c'est essentiel ?
  - **Réponse type :** Le RETEX (retour d'expérience) est l'analyse post-incident : timeline complète, vecteur initial, chemins d'escalade, persistence, ce qui a fonctionné et ce qui a échoué, et les recommandations d'amélioration. C'est essentiel parce que sans RETEX, on ne corrige pas les causes racines et on revit le même incident. Un bon RETEX produit des actions concrètes priorisées — pas juste un rapport technique, mais un plan d'amélioration avec des responsables et des délais.

### Questions les plus probables en entretien

1. Phases de la réponse à incident ?
2. Événement vs alerte vs incident vs crise ?
3. Ransomware en cours : premières actions ?
4. Pourquoi la préparation est critique ?
5. Comment construire une timeline d'attaque ?
6. Confiner immédiatement ou observer ?

### Réponses flash

- **Phases NIST** → Préparation → Détection/Analyse → Confinement/Éradication/Restauration → Post-Incident. Itératif, pas linéaire.
- **Échelle** → Événement (fait brut) → Alerte (signalé anormal) → Incident (confirmé) → Crise (dépasse la capacité normale).
- **Ransomware** → Confiner immédiatement, ne PAS éteindre (préserver mémoire), protéger les sauvegardes, désactiver comptes compromis, scoper.
- **Préparation** → IRP, playbooks, télémétrie, contrat PRIS, exercices, test de restauration. Le jour J c'est trop tard.
- **Timeline** → Croiser EDR + Event Logs + proxy/DNS + artefacts forensic. Point d'entrée → pivots → persistence → actions sur objectif.
- **Confinement vs observation** → Destructif/exfiltration = confinement immédiat. Espionnage discret = observation possible si l'attaquant ne sait pas. Doute = confiner.
- **RETEX** → Timeline + causes racines + ce qui a marché/échoué + plan d'amélioration priorisé.

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à l'orchestration de la réponse à incident — la capacité de piloter une investigation, coordonner des acteurs hétérogènes, prendre des décisions sous pression, et ramener une organisation à un état de fonctionnement sûr.
>
> L'incident BLACKTIDE qui traverse les 38 premiers chapitres n'est pas un cas exceptionnel. C'est un incident représentatif de ce que vivent des centaines d'organisations chaque année : un phishing sur un sous-traitant, un infostealer qui vole des credentials VPN, un mouvement latéral progressif, un ransomware déployé un vendredi soir. Les montants, les noms et les circonstances sont fictifs, mais chaque décision, chaque tension, chaque erreur décrite dans le fil rouge est tirée de la réalité opérationnelle d'incidents réels.
>
> La réponse à incident n'est pas un exercice théorique. C'est une discipline qui se prépare (Partie II), se pratique en exercice (Ch.10), et s'améliore par le retour d'expérience (Ch.38). Le jour où l'incident arrive — et il arrivera —, ce qui fait la différence n'est pas la chance, c'est la préparation.
>
> *Préparer • Détecter • Qualifier • Investiguer • Contenir • Éradiquer • Restaurer • Capitaliser — avec méthode, rigueur et sang-froid.*

## Threat hunting

### Questions essentielles

- **Question :** Qu'est-ce que le threat hunting et en quoi c'est différent du SOC ?
  - **Réponse type :** Le threat hunting est la recherche proactive de menaces dans le SI, guidée par une hypothèse — pas par une alerte. Le SOC réagit aux alertes générées par les règles de détection. Le hunter cherche précisément ce qui échappe à ces règles : les attaquants qui ont délibérément évité de déclencher les alertes. L'objectif c'est de réduire le dwell time — le délai entre la compromission et sa détection, qui peut être de plusieurs semaines voire mois pour les attaquants discrets.

- **Question :** C'est quoi la Pyramid of Pain et comment ça guide le hunting ?
  - **Réponse type :** La Pyramid of Pain de David Bianco hiérarchise les indicateurs par leur valeur défensive. En bas : les hashes et IPs, très faciles à changer pour l'attaquant. En haut : les TTP, très coûteuses à changer car elles reflètent les compétences et habitudes de l'adversaire. Le hunting se positionne en haut de la pyramide : on cherche des comportements (IOA) et des TTP, pas des IOC statiques. Une hypothèse basée sur T1053.005 (Scheduled Task) détectera des centaines de variants d'attaques, là où un hash ne détecte qu'un seul binaire.

- **Question :** Comment formulez-vous une hypothèse de hunting ?
  - **Réponse type :** Une bonne hypothèse est une affirmation testable liée à une technique ATT&CK. Par exemple : « un attaquant pourrait avoir créé une tâche planifiée pour exécuter un payload via PowerShell ». La source peut être un rapport CTI, un incident récent, ou un gap de détection identifié. Ensuite, je sélectionne les sources de données (ici Event 4698 + Sysmon 1), je construis la requête, j'exécute, je trie le bruit, je pivote si je trouve quelque chose de suspect, et je documente ma conclusion — même si elle est négative.

- **Question :** C'est quoi le Minimum Viable Visibility ?
  - **Réponse type :** C'est l'ensemble minimal de sources de télémétrie sans lesquelles le hunting est impossible. Les essentielles : un EDR ou Sysmon pour l'activité endpoint, le PowerShell Script Block Logging (Event 4104), les logs d'authentification Windows (4624/4625/4769), les logs DNS, les logs proxy/firewall, et les logs d'identité cloud (Entra ID). Un hunter est aussi bon que sa télémétrie — sans les bonnes données, même la meilleure hypothèse ne produit rien.

- **Question :** Que faites-vous quand un hunt ne trouve rien ?
  - **Réponse type :** Un hunt négatif n'est pas un échec — c'est un résultat. Il confirme que la menace spécifique recherchée n'est pas présente dans le SI à cet instant, avec la visibilité disponible. Mais il peut aussi révéler un gap de visibilité : si je cherche du beaconing mais que les logs DNS ne sont pas collectés, le résultat négatif ne signifie rien. Je documente la conclusion, le scope, la confiance, et je recommande des améliorations de visibilité si nécessaire. Le hunt peut aussi se transformer en règle de détection automatisée pour le futur.

### Questions complémentaires

- **Question :** Quelle est la relation entre hunting et detection engineering ?
  - **Réponse type :** Le hunting et le detection engineering fonctionnent en boucle. Le hunter découvre un pattern suspect qui n'était pas couvert par les règles. Ce pattern est formalisé en règle Sigma ou KQL et intégré au SIEM. Les attaquants s'adaptent et contournent la règle, et le hunter doit chercher les variantes. C'est un cycle perpétuel : le hunting pousse la détection vers le haut, et les gaps de détection alimentent les hypothèses de hunting.

- **Question :** Comment gérez-vous le bruit en hunting ?
  - **Réponse type :** Le bruit vient surtout des opérations IT légitimes : déploiements SCCM, scripts de GPO, scans Nessus. La clé c'est la baseline : connaître le comportement normal de l'environnement avant de chercher l'anormal. Les exclusions doivent être chirurgicales — exclure un compte de service spécifique sur un host spécifique pour une action spécifique, pas « tout ce qui vient d'un compte admin ». Une exclusion trop large peut masquer un attaquant qui utilise précisément ces comptes à privilèges.

### Questions les plus probables en entretien

1. Threat hunting vs SOC : quelle différence ?
2. Pyramid of Pain : comment ça guide le hunting ?
3. Comment formuler une hypothèse de hunting ?
4. Minimum Viable Visibility : quelles sources ?
5. Boucle hunting → detection engineering ?

### Réponses flash

- **Hunting** → Proactif, guidé par hypothèse, cherche ce que les règles ne voient pas. Réduit le dwell time.
- **Pyramid of Pain** → Hashes (bas, facile à changer) → TTP (haut, coûteux). Hunter = haut de la pyramide.
- **Hypothèse** → Affirmation testable + technique ATT&CK + sources de données + requête + conclusion documentée.
- **MVV** → EDR/Sysmon, PowerShell 4104, auth logs (4624/4769), DNS, proxy, identité cloud.
- **Hunt négatif** → Pas un échec. Confirme absence (avec le scope et la confiance). Peut révéler un gap de visibilité.
- **Boucle** → Hunt → pattern → règle Sigma → SOC → attaquant s'adapte → nouveau hunt.
- **Bruit** → Baseline du normal, exclusions chirurgicales. Rareté ≠ malveillance, contexte essentiel.

---
