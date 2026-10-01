---
title: 'Chapitre 36 — Cas complet : évaluation de menace sectorielle pour un board'
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - Partie VIII — Études de cas et synthèse
  - index.md
---

**Contexte :** Le RSSI d'un groupe hospitalier français (3 établissements, 5 000 employés, données de santé de 2 millions de patients) demande à Sentinelle Cyber un rapport stratégique sur la menace cyber pour le secteur santé, à présenter au conseil d'administration.

**L'analyste**, **Sofia Leclerc** (CTI senior, spécialisation sectorielle santé), dispose de 3 semaines pour produire un rapport de 10 pages maximum, sans jargon technique, lisible par des administrateurs non experts en cybersécurité.

**Phase collecte (semaine 1) :** Sofia compile les rapports sectoriels (ENISA Threat Landscape for Health, HHS Health Sector Cybersecurity report, rapports H-ISAC, CERT Santé français). Elle analyse les incidents du secteur santé sur les 18 derniers mois (ransomwares sur des hôpitaux français — CHU de Rennes 2023, CH de Cannes 2024, incidents européens documentés). Elle consulte les feeds commerciaux pour les ventes d'accès ciblant le secteur santé (3 annonces sur Exploit.in dans les 6 derniers mois ciblant des « healthcare EU organizations »). Elle analyse les vulnérabilités des technologies utilisées par le client (systèmes HIS, PACS, équipements biomédicaux connectés).

**Phase analyse (semaine 2) :** Sofia identifie 3 menaces prioritaires. (1) Ransomware (menace principale — 67 % des incidents santé en Europe sont des ransomwares ; les groupes LockBit, BlackBasta et Play ciblent activement les hôpitaux ; motivation : les hôpitaux paient parce qu'ils ne peuvent pas se permettre d'arrêter les soins). (2) Vol de données de santé (menace croissante — les dossiers médicaux valent 10-50× plus que les données bancaires sur le dark web, car ils permettent la fraude à l'assurance, l'usurpation d'identité, et le chantage). (3) Espionnage étatique sur la recherche pharmaceutique (menace ciblée — APT29 et APT41 ont ciblé la recherche vaccin COVID ; les groupes hospitaliers avec des programmes de recherche sont des cibles pour l'espionnage de propriété intellectuelle).

**Phase production (semaine 3) :** Le rapport est structuré pour le board. Page 1 : résumé exécutif (« le secteur santé est le 3ème secteur le plus ciblé par les ransomwares en Europe, avec un coût moyen de 4,5 M€ par incident ; notre groupe est exposé ; les mesures prioritaires sont A, B, C »). Pages 2-4 : les 3 menaces avec leur impact business (pas technique — « arrêt des soins pendant X jours », « notification de X millions de patients au titre du RGPD », « amende CNIL potentielle de X M€ »). Pages 5-7 : l'exposition du groupe (technologies vulnérables, surface d'attaque, comparaison avec les pairs du secteur). Pages 8-9 : les recommandations priorisées (avec coût estimé et calendrier). Page 10 : glossaire minimal (5 termes essentiels définis pour le board).

Le rapport est présenté au conseil d'administration par le RSSI, avec Sofia en support pour les questions. Le board approuve un budget de sécurité supplémentaire de 800 K€ sur 18 mois.

---
