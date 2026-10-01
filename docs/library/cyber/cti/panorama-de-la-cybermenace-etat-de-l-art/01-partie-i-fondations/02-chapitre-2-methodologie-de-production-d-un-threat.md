---
title: Chapitre 2 — Méthodologie de production d'un Threat Landscape
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE I — Fondations
  - index.md
---

## 2.1 — Le cycle du renseignement appliqué au CTL

La production d'un Cyber Threat Landscape repose sur le cycle du renseignement — un processus itératif en six phases que l'ENISA a formalisé dans sa méthodologie CTL 2025 et que le CERT-EU opérationnalise dans son framework CTI.

**Phase 1 — Direction (planification).** Cette phase définit le « pourquoi » du CTL : quel est son objectif ? Pour qui est-il produit ? Quelles questions doit-il résoudre ? L'ENISA distingue trois éléments fondamentaux à établir : le périmètre (scope), l'audience (target audience) et les intelligence requirements (besoins en renseignement). Sans direction claire, le CTL risque de devenir un exercice de compilation sans valeur analytique.

Les intelligence requirements se déclinent en trois niveaux. Les Priority Intelligence Requirements (PIR) sont les questions stratégiques fondamentales : « Quels acteurs menacent notre secteur ? Quelles sont les tendances émergentes ? ». Les Specific Intelligence Requirements (SIR) détaillent les PIR en questions opérationnelles : « Quels groupes ransomware ciblent l'industrie de défense en Europe ? ». Les Requests for Information (RFI) sont des besoins ponctuels : « Quel est le TTP utilisé par APT28 dans la campagne X ? ».

**Phase 2 — Collecte.** La collecte consiste à identifier, valider et acquérir les données nécessaires pour répondre aux intelligence requirements. Le plan de collecte doit préciser les types de sources (OSINT, CTI feeds commerciaux, télémétrie interne, partage entre pairs, partenaires institutionnels), les critères de sélection et le scoring de fiabilité. La méthodologie ENISA 2025 insiste sur l'importance d'un score de pertinence EU (EU relevancy score) pour filtrer les données pertinentes dans un flux global massif.

Les sources se répartissent en plusieurs catégories. Les sources ouvertes (OSINT) incluent les rapports publics des agences nationales, les blogs de sécurité des éditeurs (Mandiant/Google TI, Microsoft MSTIC, CrowdStrike, Recorded Future), les publications académiques, et les communications officielles des CERT. Les sources fermées incluent les feeds CTI commerciaux, les échanges entre CERT au sein de réseaux de confiance (FIRST, TF-CSIRT, ISACs sectoriels), et la télémétrie interne des organisations. Les sources primaires — données brutes issues de l'observation directe d'incidents — sont les plus précieuses mais les plus difficiles à obtenir en dehors des CERT nationaux.

> **⚠️ Piège fréquent** : le biais de source unique. Un analyste qui ne consomme que les rapports d'un seul éditeur de sécurité hérite de tous les biais de cet éditeur (clientèle spécifique, géographie limitée, focus sectoriel). Le CERT-EU note dans son TLR 2025 que l'expansion de son propre monitoring par IA en 2025 a augmenté certaines métriques — ce qui reflète une meilleure capacité de collecte, pas nécessairement une augmentation des menaces. Ce type de biais méthodologique doit toujours être explicité.

**Phase 3 — Traitement.** Le traitement transforme les données brutes en un format exploitable pour l'analyse. Cette phase inclut la normalisation (conversion vers un format commun — typiquement STIX 2.1), la corrélation (rapprochement de données provenant de sources différentes), l'enrichissement (ajout de contexte aux indicateurs bruts) et le triage (priorisation selon les intelligence requirements). Le traitement linguistique est également un enjeu : les rapports collectés dans différentes langues doivent être traduits et normalisés en un langage cohérent, avec le risque de perdre des nuances.

**Phase 4 — Analyse et production.** C'est le cœur du processus — le passage de l'information à l'intelligence. L'analyse CTL combine plusieurs techniques : l'identification des key assessments (les conclusions principales que le CTL doit établir), l'analyse d'alternatives (considérer des hypothèses concurrentes), l'identification des drivers clés (les facteurs qui expliquent le mieux les phénomènes observés), et la gestion des inconsistances (les données qui contredisent les hypothèses de travail).

La méthodologie ENISA identifie plusieurs défis récurrents de cette phase : le manque de confiance dans les données collectées, la multiplicité des auteurs et des experts impliqués, et la nécessité de produire des statistiques fiables. La recommandation centrale est de maintenir une rigueur constante : vérifier ses assessments, considérer les alternatives, traiter les inconsistances, se concentrer sur les drivers clés et maintenir le contexte global.

**Phase 5 — Dissémination.** La dissémination livre le CTL à son audience. Elle peut prendre trois formes : push (envoi actif au destinataire), pull (mise à disposition sur une plateforme), ou interactive (briefing, présentation, échange). Le choix du modèle dépend de l'audience et de l'objectif. Un CTL destiné au COMEX sera typiquement disseminé en push (présentation + document), tandis qu'un CTL opérationnel sera disponible en pull sur une plateforme interne et en feeds machine-readable.

Le Traffic Light Protocol (TLP) régit les conditions de partage : TLP:RED (destinataires nommés uniquement), TLP:AMBER (organisation du destinataire), TLP:AMBER+STRICT (limité aux participants), TLP:GREEN (communauté élargie), TLP:CLEAR (diffusion publique). Le choix du TLP est un arbitrage entre la valeur du partage et la protection des sources.

**Phase 6 — Feedback.** Le cycle se boucle par la collecte du retour d'expérience de l'audience. Ce feedback informe la direction de la prochaine itération : les intelligence requirements étaient-ils pertinents ? Le format était-il adapté ? Quels sujets manquaient ? Le feedback transforme le CTL d'un produit ponctuel en un processus d'amélioration continue.

## 2.2 — La méthodologie ENISA CTL 2025 : principes directeurs et phases

L'ENISA a publié en août 2025 une version mise à jour de sa méthodologie de production du Cyber Threat Landscape. Ce document est la référence méthodologique la plus complète disponible publiquement pour la production de CTL à grande échelle.

La méthodologie ENISA repose sur une approche coopérative : la production du CTL implique des analystes internes, des parties prenantes externes (États membres, partenaires privés), et un processus de validation multi-niveaux. Le cycle de production est visualisé comme un processus itératif où chaque phase génère du feedback pour les phases précédentes.

Plusieurs principes méritent d'être soulignés. Le premier est l'importance des taxonomies conséquentes : la manière dont les menaces sont classifiées conditionne la qualité de l'analyse et la comparabilité des résultats dans le temps. Le second est l'ancrage dans des frameworks reconnus : STIX 2.1 pour la représentation, MITRE ATT&CK pour la structuration des TTPs, et la taxonomie ENISA des menaces comme grille de classification. Le troisième est la distinction entre formats textuels (pour la communication humaine) et machine-readable (pour l'opérationnalisation automatisée).

L'ENISA note que des changements sont prévus pour les templates CTL en 2025, signe que la méthodologie est un document vivant qui évolue avec les besoins de ses parties prenantes. L'automatisation croissante du traitement des données — y compris via l'IA — est identifiée comme un axe de développement futur, avec des implications sur la vitesse de production, la couverture, et les risques de biais algorithmique.

## 2.3 — Définir le périmètre, l'audience et les intelligence requirements

La qualité d'un CTL dépend de la qualité de son cadrage initial. Trois questions doivent être tranchées avant toute collecte.

**Le périmètre** définit ce que le CTL couvre et ce qu'il exclut. Un périmètre géographique (UE, France, mondial), sectoriel (défense, finance, santé), technique (IT, OT, cloud, spatial), ou temporel (12 mois, 6 mois, temps réel). Le périmètre doit être explicite et documenté, car il conditionne l'interprétation des résultats. Un CTL qui couvre uniquement l'UE ne peut pas prétendre évaluer la menace mondiale — même si les tendances sont souvent transposables.

**L'audience** détermine le niveau de détail, le format et le vocabulaire. Un CTL pour le COMEX sera synthétique, orienté décision, en langage business. Un CTL pour les analystes SOC sera technique, détaillé, riche en IOCs et en TTPs. Un CTL pour le régulateur sera structuré autour des obligations réglementaires. Le même corpus d'intelligence peut — et devrait — être décliné en plusieurs formats selon les audiences.

**Les intelligence requirements** transforment le besoin implicite de l'audience en questions explicites et actionnables. La formulation est essentielle : « Quelles sont les menaces ? » est une mauvaise question (trop large, pas actionnable). « Quels groupes ransomware ont ciblé le secteur aéronautique européen au cours des 12 derniers mois, avec quelles TTPs et quels taux de succès ? » est une bonne question (périmètre clair, actionnable, mesurable).

## 2.4 — Plan de collecte : types de sources, validation, scoring

Le plan de collecte opérationnalise les intelligence requirements en identifiant les sources nécessaires et les modalités de leur exploitation. Il doit répondre à trois questions : quelles données collecter ? Auprès de quelles sources ? Comment valider leur fiabilité ?

La validation des sources repose sur le scoring de confiance. La méthodologie ENISA et le framework CERT-EU utilisent tous deux le code Admiralty (NATO), qui évalue séparément la fiabilité de la source (de A — complètement fiable à F — fiabilité impossible à juger) et la crédibilité de l'information (de 1 — confirmée par d'autres sources à 6 — crédibilité impossible à juger). La combinaison des deux dimensions produit un score de confiance (par exemple A1, B2) qui conditionne l'utilisation de l'information dans le CTL. Le détail de ce système est traité au Chapitre 5.

Le CERT-EU applique un seuil strict : seules les informations de sources A ou B avec une crédibilité de 1 ou 2 sont utilisées dans ses produits CTI. Ce seuil garantit que les produits sont basés sur des sources ayant un track record démontré et une corroboration suffisante. C'est un choix méthodologique fort, qui sacrifie la couverture au profit de la fiabilité.

## 2.5 — Traitement et structuration des données collectées

Le traitement convertit les données brutes en formats exploitables. Trois opérations clés structurent cette phase.

La **normalisation** consiste à convertir les données hétérogènes (rapports textuels en différentes langues, feeds techniques en différents formats, communications informelles) en un format commun. Pour les données techniques, STIX 2.1 s'est imposé comme le standard de représentation. Pour les données textuelles, la normalisation passe par l'extraction des éléments structurants (acteurs, TTPs, victimes, dates, IOCs) et leur codification.

La **corrélation** rapproche des données provenant de sources différentes pour identifier des patterns. Un IOC technique repéré dans un feed commercial peut être corrélé avec un TTP documenté dans un rapport CERT, lui-même corrélé avec un incident observé en interne. La corrélation est le mécanisme qui transforme des données isolées en intelligence.

L'**enrichissement** ajoute du contexte aux données brutes. Un hash de malware brut a peu de valeur ; enrichi avec son historique de détection, ses associations à des groupes connus, et son comportement observé, il devient un indicateur exploitable. Les plateformes CTI (MISP, OpenCTI) automatisent partiellement cet enrichissement.

## 2.6 — Analyse et production du livrable

L'analyse est le passage de l'information à l'intelligence — la phase où l'analyste produit des assessments, identifie des tendances et formule des recommandations. C'est aussi la phase la plus exigeante intellectuellement.

La méthodologie ENISA recommande plusieurs disciplines analytiques : établir les key assessments (les conclusions principales que l'audience attend), considérer les alternatives (quelles autres explications sont possibles ?), identifier les drivers clés (quels facteurs expliquent le mieux les phénomènes ?), et traiter les inconsistances (les données qui contredisent les hypothèses).

La production du livrable final exige une structuration rigoureuse. Le CERT-EU recommande l'utilisation de templates standardisés qui guident la rédaction et assurent la cohérence entre les éditions successives. Le langage analytique doit être calibré : les mots de probabilité estimative (WEP) doivent être utilisés de manière cohérente, et les niveaux de confiance doivent être explicités pour chaque assessment.

La validation avant publication est une étape critique. Le CTL doit être revu par des pairs, des experts du domaine et la hiérarchie. Cette revue vérifie l'exactitude des données, la cohérence des assessments, et la pertinence des recommandations.

## 2.7 — Dissémination : formats, TLP et modèles d'interaction

La dissémination est souvent sous-estimée dans le processus CTL, alors qu'elle conditionne l'impact du produit. Un CTL excellent mais mal diffusé n'a aucune valeur.

Les formats textuels (rapports PDF, présentations) restent le vecteur principal pour la communication humaine. Les formats machine-readable (feeds STIX/TAXII, indicateurs enrichis) permettent l'opérationnalisation automatisée. L'ENISA note que ces deux catégories de formats servent des besoins complémentaires et que le choix dépend de l'audience et de l'objectif.

Le modèle d'interaction avec l'audience peut être push (envoi proactif), pull (mise à disposition) ou interactif (briefing, atelier). Les trois modèles ont des valeurs différentes : le push garantit que le livrable atteint sa cible, le pull permet une consultation à la demande, et l'interactif permet l'échange et l'approfondissement.

## 2.8 — Limites méthodologiques : biais et mitigation

Tout CTL est soumis à des biais qu'il convient d'identifier, de documenter et de mitiger.

Le **biais de collecte** résulte de la nature des sources utilisées. Un CERT national ne voit que les incidents qui lui sont signalés. Un éditeur de sécurité ne voit que les menaces qui touchent ses clients. Le CERT-EU note explicitement dans son TLR 2025 que sa propre télémétrie offre une meilleure visibilité sur les menaces ciblant les institutions de l'UE que les divulgations tierces — ce qui signifie que certaines catégories de menaces sont structurellement sur-représentées ou sous-représentées.

Le **biais de visibilité** favorise les menaces qui se manifestent bruyamment (ransomware, DDoS, défigurations) au détriment des menaces silencieuses (espionnage persistant, prépositionnement). L'espionnage étatique est systématiquement sous-représenté dans les statistiques d'incidents parce qu'il est conçu pour ne pas être détecté.

Le **biais de publication** favorise les menaces qui génèrent des rapports publics. Les éditeurs de sécurité publient sur les menaces qu'ils ont détectées — ce qui crée un biais en faveur des menaces que leurs produits sont capables de détecter. Les menaces qui échappent aux solutions de sécurité dominantes sont structurellement sous-documentées.

Le **biais linguistique** — identifié par l'ENISA — résulte de la collecte principalement en anglais. Les rapports publiés dans d'autres langues (chinois, russe, arabe, farsi) sont souvent sous-exploités, alors qu'ils contiennent des informations précieuses sur les acteurs et les victimes de ces régions.

La mitigation de ces biais passe par la **diversification des sources**, l'**explicitation des limites** dans le CTL, et la **distinction systématique entre ce qui est observé et ce qui est inféré**. Un CTL honnête ne cache pas ses angles morts — il les documente.

## 2.9 — 🔴 Fil rouge : Sophie structure sa méthodologie

> **📌 FIL ROUGE — Épisode 2**
>
> Sophie consacre sa première semaine à formaliser la méthodologie du CTL d'EuroDefense. Elle commence par les intelligence requirements, formulés avec le RSSI et les responsables de chaque BU :
>
> — PIR 1 : Quels acteurs étatiques menacent le secteur aéronautique/défense/spatial européen ?
> — PIR 2 : Quel est l'état de l'écosystème ransomware ciblant notre secteur ?
> — PIR 3 : Quels vecteurs d'attaque sont les plus utilisés contre nos systèmes (IT, OT, spatial) ?
> — PIR 4 : Quelle est la menace sur notre supply chain logicielle et matérielle ?
>
> Elle choisit ses frameworks : MITRE ATT&CK pour structurer les TTPs, le code Admiralty pour le scoring de confiance, le framework CERT-EU pour la catégorisation des menaces et le scoring des acteurs. Elle crée un template de livrable en deux versions : un executive summary de 10 pages pour le COMEX, et un rapport technique de 80+ pages pour les équipes CERT et SOC.
>
> Premier constat : le CERT d'EuroDefense manque de sources sur les filiales asiatiques. Sophie note ce biais de collecte dans son plan et prévoit de le combler par un abonnement à un feed CTI spécialisé Asie-Pacifique et un rapprochement avec l'ASD australien via le réseau FIRST.

---
