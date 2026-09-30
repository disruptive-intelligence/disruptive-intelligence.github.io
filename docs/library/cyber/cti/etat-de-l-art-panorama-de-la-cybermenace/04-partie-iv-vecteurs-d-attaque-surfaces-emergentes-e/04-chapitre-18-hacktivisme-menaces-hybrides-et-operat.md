---
title: Chapitre 18 — Hacktivisme, menaces hybrides et opérations d'influence
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - PARTIE IV — Vecteurs d'attaque, surfaces émergentes et tendances transversales
  - index.md
---

## 18.1 — La résurgence hacktiviste 2025

L'ENISA ETL 2025 documente que le hacktivisme représente une part très significative des incidents enregistrés contre l'UE. Les attaques DDoS hacktivistes constituent 81,4% des menaces les plus prévalentes tous secteurs confondus. L'administration publique est le secteur le plus ciblé (96,2% des incidents dans ce secteur sont des DDoS hacktivistes).

Cependant, l'impact opérationnel reste généralement limité : les sites web ciblés sont indisponibles pendant quelques heures, les services sont perturbés temporairement, mais les dommages structurels sont rares. La nuance analytique est essentielle : **volume élevé d'incidents ne signifie pas impact élevé**. Un CTL qui compte les incidents DDoS hacktivistes au même niveau que les compromissions d'espionnage étatique produit une image déformée du paysage de menace.

## 18.2 — Les alliances hacktivistes et la montée en capacité OT

L'écosystème hacktiviste a évolué vers des alliances transversales. La **Holy League**, annoncée en juillet 2024, rassemblerait 70 groupes incluant des acteurs pro-russes (NoName057(16)) et pro-palestiniens, ciblant l'Ukraine, Israël et les pays perçus comme les soutenant. L'**Union du 7 octobre** et d'autres alliances bilatérales complètent ce paysage.

La montée en capacité la plus préoccupante est le **ciblage OT** par les hacktivistes. **Z-PENTEST-ALLIANCE** s'est positionné comme le principal groupe hacktiviste ciblant les infrastructures critiques dans l'UE, avec un focus sur les infrastructures énergétiques. Le groupe partage des vidéos montrant des opérateurs manipulant des interfaces de systèmes OT — un acte de communication visant à amplifier l'impact psychologique. L'Italie est documentée comme l'État membre le plus fréquemment ciblé par les attaques OT hacktivistes, suivie de la Tchéquie, la France et l'Espagne.

L'**Infrastructure Destruction Squad (IDS)**, apparu en juin 2025, a développé le malware ICS **VoltRuptor**, décrit comme offrant un support multi-protocole et des capacités avancées de persistance et d'anti-forensique. VoltRuptor est disponible à la vente sur le dark web. L'ENISA note que l'attribution de l'IDS à un ensemble d'intrusion Russia-nexus est une « hypothèse de travail réaliste ».

## 18.3 — Opérations d'influence et interférence numérique

La convergence entre opérations cyber et opérations d'influence est l'un des phénomènes les plus structurants documentés dans le corpus. Cette convergence prend plusieurs formes.

Le **hack-and-leak** combine l'intrusion technique (vol de documents) avec la manipulation informationnelle (diffusion sélective des documents pour créer un narratif). Le **cyber-enabled influence operation** utilise les capacités cyber pour amplifier des campagnes de désinformation — création de faux sites, automatisation de la diffusion, génération de contenu par IA.

Les cas documentés incluent les manipulations ciblant l'élection présidentielle roumaine de 2024 (promotion artificielle de contenus sur TikTok), les DDoS ciblant les sites de partis politiques danois le jour des élections, et les campagnes de désinformation russes utilisant des répliques IA de présentateurs TV.

VIGINUM (France) est l'opérateur étatique chargé de détecter et caractériser les ingérences numériques étrangères. L'ANSSI et VIGINUM travaillent en coordination, l'ANSSI traitant le volet technique (intrusions) et VIGINUM le volet informationnel (manipulation).

## 18.4 — 🔴 Fil rouge : DDoS + désinformation sur un contrat OTAN

> **📌 FIL ROUGE — Épisode 18**
>
> En septembre 2025, EuroDefense annonce l'obtention d'un contrat OTAN majeur pour des systèmes de surveillance aérienne. Le jour de l'annonce, trois événements simultanés :
>
> 1. Une campagne DDoS sous le hashtag #OPDefense rend indisponibles les portails web publics d'EuroDefense pendant 4 heures. Revendiquée par NoName057(16) et relayée par le Telegram de la Holy League.
> 2. Un compte Twitter/X se présentant comme un « lanceur d'alerte interne » publie des documents prétendument confidentiels sur les coûts du contrat — les documents sont des faux, mais suffisamment crédibles pour être repris par des médias marginaux.
> 3. Un article sur un site de « pink slime » (faux site d'information local) allègue que le système de surveillance a des « failles de sécurité connues non corrigées » — information invérifiable mais anxiogène.
>
> Sophie identifie l'opération comme une campagne hybride coordonnée : la composante cyber (DDoS) est le signal visible, la composante informationnelle (faux documents, faux article) est le payload réel. L'objectif n'est pas de paralyser EuroDefense mais de **discréditer le contrat** et d'**éroder la confiance** dans le groupe. Elle coordonne avec VIGINUM pour la caractérisation de l'ingérence informationnelle et recommande au service communication d'EuroDefense de préparer une réponse factuelle ciblée.

---
