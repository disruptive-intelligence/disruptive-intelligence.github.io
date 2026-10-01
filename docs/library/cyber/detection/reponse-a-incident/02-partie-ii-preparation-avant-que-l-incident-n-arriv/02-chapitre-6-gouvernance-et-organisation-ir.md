---
title: Chapitre 6 — Gouvernance et organisation IR
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie II — Préparation : avant que l''incident n''arrive'
  - index.md
---

## 6.1 L'équipe IR : composition et rôles

L'**IR lead** (ou incident commander) coordonne l'ensemble de la réponse. Il maintient la vision d'ensemble, assigne les questions aux analystes, arbitre les priorités, fait l'interface avec la direction et le RSSI, et documente les décisions. Dans une PME, c'est souvent le RSSI lui-même. Dans un grand groupe, c'est un rôle dédié au sein du CSIRT.

Les **analystes forensic** mènent l'investigation technique sur les endpoints : acquisition de preuves (RAM, disques, artefacts), analyse des artefacts système, analyse de malware first-pass, et production des IoC. Compétences requises : maîtrise des outils forensic (KAPE, Velociraptor, Volatility, FTK Imager), connaissance approfondie des artefacts Windows et Linux.

Les **analystes logs/réseau** analysent les logs centralisés (SIEM), les flux réseau (pare-feu, proxy, DNS, NDR), et construisent la timeline par corrélation des sources. Compétences requises : maîtrise du SIEM (requêtes SPL, KQL, ou ELK), compréhension des protocoles réseau, capacité de corrélation multi-sources.

L'**analyste CTI** contextualise la menace : identification de l'adversaire (groupe, plateforme RaaS, TTP connues), enrichissement des IoC (hash, domaines, IP — sont-ils connus ? associés à quelle campagne ?), et anticipation des comportements (si c'est un affilié PhantomCrypt, quels mécanismes de persistance sont typiques ?). Renvoi vers le cours CTI et le cours Cartographie des Écosystèmes.

Le **représentant IT/infra** apporte la connaissance du SI (architecture, systèmes critiques, dépendances), exécute les actions techniques décidées par l'IR lead (isolation réseau, reset de comptes, restauration), et identifie les impacts opérationnels des actions proposées.

Le **RSSI** fait l'interface entre la cellule technique et la direction. Il traduit la situation technique en termes business, valide les décisions à impact stratégique, et porte la responsabilité managériale de la réponse.

Ces rôles peuvent être portés par 3 personnes dans une PME ou 15 dans un grand groupe. Ce qui compte n'est pas le nombre de personnes mais le fait que chaque fonction soit assignée explicitement à quelqu'un qui sait ce qu'on attend de lui.

## 6.2 CSIRT interne vs prestataire PRIS

La décision entre réponse interne et mobilisation d'un prestataire qualifié PRIS dépend de plusieurs critères. La nature de l'incident (un phishing simple peut être traité en interne ; un ransomware avec compromission de l'AD nécessite presque toujours un PRIS), les compétences disponibles (l'organisation a-t-elle un forensicien capable d'analyser un dump mémoire de DC à 3h du matin un samedi ?), la charge (même si les compétences existent, l'équipe peut être submergée), le besoin d'indépendance (pour la plainte pénale, un rapport d'un tiers qualifié est plus crédible), et les exigences d'assurance (certaines polices imposent le recours à un PRIS de leur liste).

Le prestataire PRIS ne connaît pas le SI de l'organisation. Le temps d'on-boarding (comprendre l'architecture, les accès, les noms des serveurs, les personnes à contacter) est incompressible et peut prendre plusieurs heures, voire une demi-journée. Ce temps doit être anticipé : un document de synthèse du SI (architecture réseau, liste des systèmes critiques, comptes d'administration, outils de sécurité déployés) doit être préparé à l'avance et remis au PRIS dès son arrivée.

Le référentiel PRIS v3.2 de l'ANSSI (octobre 2025) qualifie les prestataires sur cinq activités : recherche d'indicateurs de compromission, investigation numérique, analyse de codes malveillants, pilotage et coordination des investigations, et gestion de crise d'origine cyber.

## 6.3 Chaîne d'escalade et RACI

La chaîne d'escalade définit qui appelle qui, dans quel ordre, avec quels critères de déclenchement. Elle doit être simple (pas plus de 3 niveaux pour atteindre le décideur), redondante (si le contact principal ne répond pas, qui est le suppléant ?), et testée régulièrement (voir Ch.10).

Le RACI de l'IR (Responsible, Accountable, Consulted, Informed) doit être défini avant l'incident. Qui est responsable de la décision de confinement réseau ? (typiquement : IR lead propose, RSSI valide). Qui est responsable de la notification ANSSI ? (typiquement : RSSI). Qui est responsable de la communication interne ? (typiquement : direction de la communication, validée par le RSSI et le juridique). L'ambiguïté des rôles pendant un incident est une source majeure de paralysie (personne ne décide) ou de décisions contradictoires (deux personnes décident des choses incompatibles). Un RACI type est proposé en Annexe G.

## 6.4 Modèle de permanence et astreinte

La réalité opérationnelle de l'IR est que l'incident n'arrive jamais à un moment pratique. L'alerte tombe le vendredi soir, l'expert AD est en vacances à l'étranger, le RSSI est dans un avion. Le modèle de permanence doit anticiper ces situations : astreinte formalisée (qui est joignable 24/7, avec quel délai de réponse), suppléances (si l'astreinte primaire ne répond pas dans les 15 minutes, qui prend le relais), et procédure de rappel d'effectifs (comment mobiliser l'équipe complète un dimanche matin).

La fatigue est un enjeu sous-estimé. Un incident majeur dure des jours, parfois des semaines. Les premières 24-48 heures sont intenses (adrénaline, urgence), mais au-delà, la fatigue dégrade la qualité des décisions, augmente le risque d'erreur, et peut conduire à des conflits interpersonnels. La rotation des équipes (shifts de 8 à 12 heures maximum, avec passage de relais structuré) est un enjeu de santé ET de qualité de réponse.

## 6.5 Fil rouge — BLACKTIDE : la mobilisation

> **🔍 BLACKTIDE — Épisode 6**
>
> Nadia (IR lead) est d'astreinte ce week-end — elle répond en 3 minutes. Marc (RSSI) est d'astreinte — il répond en 2 sonneries. Le prestataire PRIS CyberForce est mobilisé à 23h30 — le consultant senior forensic, Thomas Hartmann, et un consultant spécialiste AD, Léa Chen, seront sur site samedi à 08h15 (SLA contractuel : 12h le week-end).
>
> L'expert AD interne d'Arvantis, Youssef Benmoussa, est en congé en Tunisie. Il est injoignable par téléphone (pas de réseau dans la zone). Il sera briefé par visioconférence dimanche matin quand il retrouvera du réseau. En attendant, Léa Chen (PRIS) couvrira l'analyse AD.
>
> L'analyste SOC N2, Karim, est en poste depuis 14h (début de shift à 14h). À 02h, cela fait 12 heures qu'il travaille. Nadia lui demande de rester encore 2 heures pour le passage de relais au N2 suivant, puis de dormir. L'analyste suivant, Fatima Zeroual, prend le relais SOC à 04h.

---
