---
title: Chapitre 83 — Timeline et graphe d'enquête
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XI — Analyse structurée, cotation et raisonnement
  - index.md
---

## 83.1 Deux structures complémentaires

**Timeline** : ordre temporel des événements.

**Graphe** : structure relationnelle des entités.

Les deux structures sont **complémentaires** et **indispensables** pour analyse mature.

## 83.2 Timeline : construction

**Champs.**

- Date (avec précision et incertitude).
- Événement.
- Acteurs.
- Lieu.
- Source.
- Cotation.

**Outils.**

- **Tableau structuré** (Markdown, Excel).
- **Timeline Explorer** (Zimmerman, gratuit).
- **Aeon Timeline** (commercial, puissant).
- **Knightlab Timeline JS** (publication web).

## 83.3 Lecture de timeline

**Patterns à chercher.**

- Séquences causales (A précède B qui mène à C).
- Simultanéités suspectes (deux événements coordonnés à la minute).
- Incohérences (un acte avant sa cause supposée).
- Périodes d'inactivité (silence anormal).

## 83.4 Exemple MIRAGE — extrait

| Date | Événement | Source | Cot. |
|---|---|---|---|
| 2002 | Diplôme X-Ponts Delaunay | LinkedIn | A1 |
| 2019-06 | Embauche TechnoVert DAF | Communiqué | A1 |
| 2020-03 | Création Delta Consulting | Companies Registry Malta | A1 |
| 2020-Q3 | Premiers flux TechnoVert→Delta | Cyprus Confidential indirect | B2 |
| 2022-01 | Création Verde Holdings | Companies Registry CY | A1 |
| 2025-04 | Audit interne révèle écritures suspectes | Berthier presse | B2 |
| 2025-05 | Berthier signale en interne | (présumé) | C3 |
| 2025-06 | Procédure interne TechnoVert | (présumé) | C3 |
| 2025-09-15 | Licenciement Berthier | Presse RH | B2 |
| 2025-10-12 | Création domaine verites-technovert.com | WHOIS historique | A1 |
| 2025-10-18 | Création domaine info-finance-eu.com | WHOIS historique | A1 |
| 2025-11-XX | Premiers posts blog | Wayback | A2 |
| 2026-01-XX | Cluster X actif | archive.today | A2 |
| 2026-03-03 | Vidéo deepfake publiée | yt-dlp capture | A1 |
| 2026-03-XX | Trois fausses photos publiées | Captures | A1 |
| 2026-05-16 | Mandat Legrand & Associés | Mandat | A1 |

**Patterns évidents.** Création des domaines de désinformation **5-8 semaines après le licenciement** de Berthier. Vidéo deepfake **avant audience prud'homale**. Cohérence temporelle forte.

## 83.5 Graphe d'enquête

**Construction.**

- Nœuds : entités (personnes, sociétés, comptes, domaines, contenus, lieux).
- Arêtes : relations (types diverses, cotées par force).

**Outils.**

- **Maltego** (Casefile pour offline).
- **Neo4j Community**.
- **Gephi**.
- **Obsidian** (avec plugin Graph View).

## 83.6 Analyse de graphe

**Métriques.**

- **Degree centrality** : connexions par nœud (nœud très connecté = central).
- **Betweenness centrality** : à quel point un nœud relie sous-graphes.
- **Communautés** (algorithme Louvain).

**Pour MIRAGE.**

- Delaunay : degree élevé (lié à TechnoVert, Delta, Verde, comptes, etc.).
- Cluster désinformation : communauté distincte, faiblement reliée à Delaunay directement (lien indirect via cohérence temporelle et intérêt).

## 83.7 Lisibilité

**Discipline.** Un graphe de 500 nœuds est illisible. Plusieurs vues :

- Vue d'ensemble (agrégée).
- Vues filtrées par type d'entité.
- Vues centrées sur une entité.
- Vues colorées par cotation.

## 83.8 Incertitude dans visualisations

**Représenter.**

- Liens forts = traits pleins.
- Liens faibles = traits pointillés.
- Couleurs par cotation.
- Tailles par centralité.

## 83.9 Synthèse — timeline + graphe = vue 360°

La combinaison **timeline + graphe** offre une vue 360° :

- Timeline : « quand ? dans quel ordre ? »
- Graphe : « qui ? avec qui ? »
- Croisement : « quel acteur s'active à quel moment ? quels patterns ? »

## 83.10 Analyses avancées de graphe

**Détection de communautés.** Algorithmes (Louvain, Leiden, Infomap) identifient des sous-groupes densément connectés. En MIRAGE : cluster TechnoVert, cluster offshore, cluster désinformation, cluster patrimoine sont identifiables algorithmiquement.

**Identification de ponts (bridges).** Nœuds dont la suppression déconnecterait des communautés. Souvent acteurs clés (intermédiaires, facilitateurs).

**Mesures de centralité.**

- **Degree centrality** : nombre de connexions directes. Pour identifier les acteurs les plus visiblement connectés.
- **Betweenness centrality** : à quel point un nœud relie des sous-réseaux. Pour identifier les facilitateurs ou points faibles.
- **Eigenvector centrality** : importance pondérée par l'importance des voisins. Pour identifier les acteurs « influents » dans des réseaux denses.
- **PageRank** : variation de eigenvector. Pour identifier les nœuds vers lesquels convergent les flux.

**Chemins.**

- **Shortest path** : chemin le plus court entre deux nœuds. Pour comprendre « comment A est-il lié à B ».
- **All paths** : tous les chemins (filtre par longueur). Pour cartographier les relations indirectes.

**Pour MIRAGE.** Calculer le shortest path entre Delaunay et le cluster désinformation : combien d'arêtes séparent ? Quels nœuds intermédiaires ? Si chemin direct court, lien probable. Si chemin long, lien indirect plus difficile à attribuer.

## 83.11 Détection de motifs (graph motifs)

Certains **motifs** récurrents dans les graphes ont une signification :

**Triangle** (3 nœuds mutuellement connectés). Indicateur de structure forte : trois personnes en relation mutuelle = groupe ou famille / collaboration.

**Étoile** (un nœud central avec multiples branches). Indicateur de hub : une personne qui connaît beaucoup mais peu de connections mutuelles entre ses connaissances.

**Chaîne** (séquence de nœuds reliés). Indicateur de canal de transmission ou flux.

**Clique** (sous-graphe complètement connecté). Indicateur de groupe fermé.

**Pour MIRAGE.** Recherche de cliques dans le cluster désinformation (comptes X qui se suivent tous mutuellement) → signature forte CIB.

## 83.12 Timeline avancée et patterns temporels

**Patterns temporels à rechercher.**

**Burstiness.** Activité concentrée sur courtes périodes alternant avec inactivité. Caractéristique de campagnes plutôt que d'activité organique.

**Synchronisations.** Multiples acteurs publient simultanément ou avec délai constant. Indicateur de coordination.

**Cycles.** Périodicité (hebdomadaire, mensuelle) suggère automatisation ou planning structuré.

**Cascades.** Un événement initial déclenche série d'autres. Identifie les déclencheurs.

**Silences.** Périodes d'inactivité corrélées entre plusieurs acteurs. Indicateur de coordination indirect.

**Pour MIRAGE.** L'analyse temporelle révèle un pattern de cascade : licenciement Berthier (15/09/2025) → création domaines (12-18/10/2025) → activation cluster X (octobre-novembre 2025) → vidéo deepfake (mars 2026, avant audience prud'homale).

## 83.13 Outils de visualisation 2026

**Pour graphes.**

- **Maltego** (commercial + Casefile gratuit) : standard professionnel OSINT.
- **Gephi** (open source) : standard académique, algorithmes communautés.
- **Neo4j Bloom** : pour graphes property locaux.
- **yEd Graph Editor** : simple, exports clairs.
- **Cytoscape** : biologie mais utilisable.
- **vis.js, Cytoscape.js, D3.js** : pour intégration web.

**Pour timelines.**

- **Timeline Explorer (Eric Zimmerman)** : standard forensique gratuit.
- **Aeon Timeline** : commercial puissant pour multi-couches.
- **TimelineJS (Knightlab)** : publication web gratuite.
- **Plotly Python** : pour intégration scripted.

**Pour combinaisons.**

- **Sentinel** (Microsoft) : timeline + graphe pour SOC.
- **Splunk Enterprise Security** : équivalent.
- **Custom Python notebooks** : Pandas + NetworkX + Plotly = vue complète.

> **MIRAGE — Épisode 18 : Graphe d'entités et timeline**
>
> L'analyste finalise les deux structures.
>
> **Graphe final.** ~280 nœuds (60 personnes, 25 sociétés, 35 comptes sociaux, 8 domaines, 12 contenus, 5 lieux, 15 événements, 120 mentions). Maltego export.
>
> **Communautés identifiées par algorithme.**
> 1. Cluster TechnoVert (Delaunay + dirigeants + employés).
> 2. Cluster offshore (Delta + Verde + nominees).
> 3. Cluster patrimoine (SCI Provence + villa Marrakech + appartements).
> 4. Cluster désinformation (faux comptes + faux médias + contenus IA).
> 5. Cluster lanceur d'alerte (Berthier + presse + cabinets soutien).
>
> **Timeline.** Sur 6 années (2019-2026), patterns temporels révélés :
> - 2019-2022 : structuration offshore (Delta, Verde) en parallèle des montées en responsabilité TechnoVert.
> - 2025-04 à 2025-09 : escalade liée au signalement Berthier (audit interne, licenciement).
> - 2025-10 à 2026-03 : déploiement campagne désinformation (création domaines, faux comptes, contenus IA).
> - 2026-03 à 2026-05 : pic d'amplification (vidéo deepfake, mandat).
>
> Ces structures intégreront le rapport final en annexe.

-----
