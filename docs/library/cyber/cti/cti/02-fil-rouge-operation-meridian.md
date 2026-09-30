---
title: 'Fil rouge : Opération MERIDIAN'
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - index.md
---

> **Contexte narratif — ce fil rouge traverse les 33 premiers chapitres du cours et se conclut au Ch.34.**
>
> **Élise Moreau**, analyste CTI senior chez **Sentinelle Cyber** — MSSP français de 120 collaborateurs, clientèle ETI et grands groupes, SOC 24/7, CERT qualifié PRIS — reçoit une mission d'intelligence pour un client critique : **Européenne de Distribution Énergétique (EDE)**, opérateur de réseaux de distribution électrique dans 4 pays européens (France, Belgique, Allemagne, Pays-Bas), 6 200 collaborateurs, classé OIV en France et entité essentielle NIS 2.
>
> EDE a subi un incident de sécurité il y a 6 mois. L'équipe IR de Sentinelle a détecté et éradiqué l'intrusion (cf. cours IR de la bibliothèque). Les constats post-incident : l'attaquant a pénétré le réseau IT via un phishing ciblé sur un sous-traitant de maintenance, s'est déplacé latéralement via PsExec et RDP, a compromis l'Active Directory (Kerberoasting → DCSync), puis a pivoté vers le réseau de supervision SCADA via un poste d'ingénierie à double connexion. Il a été éjecté avant d'atteindre les automates, mais le CERT a identifié des mécanismes de persistance sophistiqués (DLL sideloading, tâches planifiées déguisées, modifications d'ACL AD) qui suggèrent un acteur de haut niveau. Aucune donnée exfiltrée confirmée, pas de ransomware, pas de sabotage — le positionnement semblait stratégique, pas financier.
>
> L'équipe IR a catalogué l'activité sous un cluster temporaire : **UNC-VOLT** (« UNC » pour uncategorized, convention Sentinelle). La mission d'Élise couvre cinq objectifs.
>
> **Objectif 1 — Profilage :** qui est UNC-VOLT ? Acteur étatique, mercenaire, cybercriminel sophistiqué ?
> **Objectif 2 — Attribution :** quel sponsor, quel pays, quel service de renseignement — avec quel niveau de confiance ?
> **Objectif 3 — Menace résiduelle :** UNC-VOLT va-t-il revenir ? Cible-t-il d'autres opérateurs d'énergie européens ?
> **Objectif 4 — Renseignement actionnable :** quelles TTP anticiper, quelles détections déployer, quelle posture défensive recommander à EDE ?
> **Objectif 5 — Contribution communautaire :** partager les conclusions avec l'ISAC énergie européen et contribuer à la connaissance collective sur ce cluster.
>
> L'investigation va mobiliser chaque compétence enseignée dans le cours : formulation de PIR, plan de collecte multi-sources, traitement et structuration dans OpenCTI, analyse structurée avec ACH (4 hypothèses concurrentes), gestion des biais, évaluation des sources, profilage d'acteur, analyse du tradecraft, attribution avec ses incertitudes, vulnerability intelligence (l'attaquant a exploité une vulnérabilité Ivanti), corrélation avec des campagnes connues, production de la note analytique, production de détections Sigma, briefing stratégique au COMEX d'EDE, et partage ISAC.

---
