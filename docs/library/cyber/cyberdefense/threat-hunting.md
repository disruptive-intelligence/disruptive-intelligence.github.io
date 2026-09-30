---
title: Threat hunting
source: Cyber/05_Cyberdefense/ADD_Threat_Hunting.md
format: synthese
---

---

## Annexe — Questions types d'entretien et réponses types

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
