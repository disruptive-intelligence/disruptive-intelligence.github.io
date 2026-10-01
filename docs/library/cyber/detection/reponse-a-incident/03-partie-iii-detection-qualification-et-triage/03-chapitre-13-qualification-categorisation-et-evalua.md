---
title: Chapitre 13 — Qualification, catégorisation et évaluation de gravité
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie III — Détection, qualification et triage
  - index.md
---

## 13.1 Catégorisation de l'incident

La catégorisation identifie le type d'incident pour orienter vers le playbook approprié et conditionner les obligations réglementaires. La question n'est pas « qu'est-ce qui s'est passé techniquement ? » (ça, c'est l'investigation) mais « quel type de problème avons-nous ? » (ransomware, espionnage, compromission de compte, etc.).

Dans le cas de BLACKTIDE, la catégorisation initiale est « compromission de serveur critique avec mouvement latéral ». Elle évoluera vers « ransomware avec double extorsion et exfiltration massive » au fur et à mesure de l'investigation.

## 13.2 Évaluation de la gravité

La gravité s'évalue sur une grille multicritères. La **gravité technique** mesure le nombre de systèmes touchés, le niveau de privilèges compromis, et la propagation (en cours vs achevée). La **gravité métier** mesure l'impact sur la production, la facturation, la logistique, et les clients. La **sensibilité des données** qualifie les données potentiellement exposées (données personnelles, propriété intellectuelle, secret industriel, secret défense). La **criticité des systèmes** identifie les systèmes touchés (Active Directory, systèmes de paiement, systèmes OT, serveurs de production). Le **potentiel de propagation** évalue si l'attaquant est toujours actif et si la compromission peut s'étendre. L'**impact réglementaire** identifie les notifications obligatoires et les sanctions potentielles.

La grille de gravité complète avec les critères détaillés pour chaque niveau (P1 à P4) est en Annexe G.

## 13.3 Évaluation dynamique

La gravité n'est pas figée — elle doit être réévaluée à chaque nouvelle découverte. Un incident initialement classé P3 peut basculer P1 quand l'investigation révèle que le malware « isolé » était en fait un infostealer actif depuis des semaines, alimentant la compromission de l'AD. La réévaluation régulière est une discipline essentielle : à chaque SitRep (toutes les 4-6 heures en phase aiguë), la gravité est recalculée et les décisions ajustées.

## 13.4 Fil rouge — BLACKTIDE : réévaluation en cascade

> **🔍 BLACKTIDE — Épisode 13**
>
> La gravité est réévaluée 4 fois en 8 heures.
> - 22h30 : **P2** — alerte EDR sur un DC, compromission de serveur probable.
> - 01h00 : **P1** — 3 DC touchés, ransomware en cours de déploiement, compromission majeure confirmée.
> - 06h00 : **P1 / Crise** — exfiltration de 380 Go confirmée, 3 sites impactés dont un OIV, données RH de 8 000 personnes exposées.
> - 10h00 : **Crise confirmée** — publication sur le canal Telegram de PhantomCrypt avec compte à rebours de 10 jours, presse spécialisée informée par la revendication.

---
