---
title: Chapitre 18 — Pilotage du changement, des vulnérabilités et du patching
source: Cyber/08 Gouvernance & résilience/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - ../index.md
- - Partie IV — Sécurité opérationnelle vue GRC
  - index.md
---

*Ce chapitre reste à l'angle pilotage GRC — politique, SLA, arbitrage, exceptions, gouvernance. Les détails techniques (scan de vulnérabilités, outils, requêtes) sont dans les cours SOC (Ch.32 VOC) et CTI (Ch.21 vuln intel).*

Le **change management** vu GRC : tout changement sur le SI passe par un processus de validation (demande → analyse d'impact sécurité → approbation → implémentation → vérification post-changement). L'arbitrage sécurité : chaque changement est évalué pour son impact sur les risques (« ce changement ouvre-t-il une vulnérabilité ? nécessite-t-il une mise à jour de l'analyse de risques ? affecte-t-il l'homologation ? »). Les changements d'urgence (le patch critique à 2h du matin — procédure accélérée mais documentée a posteriori).

La **politique de patching** : SLA par criticité (critique < 48h, élevé < 15 jours, moyen < 30 jours, faible trimestriel), exceptions documentées (le système legacy qui ne peut pas être patché → compensatoire : segmentation + monitoring), et le suivi (% de conformité au SLA par mois — indicateur du Ch.9). L'articulation avec la CTI et le VOC : les vulnérabilités exploitées in the wild (CISA KEV, EPSS — cf. cours CTI Ch.21 et cours SOC Ch.32) sont prioritaires indépendamment du CVSS.

L'**assurance cyber vue pilotage** : les prérequis des assureurs sont devenus un socle de sécurité de fait (MFA, EDR, sauvegardes immutables, plan IR, segmentation). Le questionnaire assureur est un mini-audit qui révèle les gaps. L'assurance couvre le risque résiduel après réduction — ce n'est pas un substitut aux contrôles.

---
