---
title: Réponses flash
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - index.md
---

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
