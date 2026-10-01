---
title: Chapitre 66 — Knowledge graphs locaux
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 66.1 Pourquoi un knowledge graph

Une enquête OSINT mature génère **des centaines d'entités** (personnes, sociétés, domaines, comptes, contenus, lieux, événements) et **des milliers de relations** (employer, owner, communicates_with, located_at, etc.).

Un **knowledge graph** structure ces données en graphe interrogeable. C'est l'évolution naturelle du vault Obsidian (Ch.17) vers une structure plus formelle.

## 66.2 Bénéfices d'un knowledge graph local

**Requêtes complexes.** « Toutes les personnes liées à TechnoVert ET à une société offshore » → requête SPARQL en quelques lignes.

**Visualisation.** Graphe explorable, communautés détectées.

**Inférences.** Si A possède B et B possède C, on peut inférer relation transitive A-C.

**Réutilisabilité.** Données d'enquête A peuvent informer enquête B (avec déontologie).

**Souveraineté.** Local, chiffré, sous contrôle.

## 66.3 Modèle de données : RDF et OWL

**RDF** (Resource Description Framework). Standard W3C pour décrire des triplets (sujet, prédicat, objet) :

```
ex:MarcDelaunay  rdf:type      foaf:Person .
ex:MarcDelaunay  foaf:worksFor ex:TechnoVert .
ex:TechnoVert    rdf:type      ex:Company .
ex:MarcDelaunay  ex:director_of ex:DeltaConsulting .
```


**OWL** (Web Ontology Language). Pour définir des ontologies (taxonomies de classes, propriétés).

Pour OSINT, ontologie type comprend : Person, Company, Domain, Account, Document, Event, Place, Wallet, Phone, Email — plus relations diverses.

## 66.4 Outils graphes locaux

**Apache Jena** (open source). Stack Java complet pour RDF + SPARQL.

**Eclipse RDF4J** (anciennement OpenRDF Sesame).

**Stardog** (commercial, freemium).

**Blazegraph**.

**Pour graphes property graph (Neo4j-style).**

- **Neo4j Community** (free, local).
- **Memgraph**.
- **TigerGraph Cloud / Local**.

**Pour OSINT simplifié.**

- **Maltego Casefile** (offline).
- **Obsidian** avec plugin graphe.

## 66.5 SPARQL : langage de requête

**Exemple SPARQL.**

```sparql
PREFIX ex: <http://mirage-investigation.local/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?person ?company
WHERE {
  ?person foaf:worksFor ex:TechnoVert .
  ?person ex:director_of ?offshore_company .
  ?offshore_company ex:juridiction ?juridiction .
  FILTER(?juridiction IN ("Malta", "Cyprus", "BVI"))
}
```


Cette requête retourne toutes les personnes qui travaillent à TechnoVert ET dirigent une société offshore.

## 66.6 Architecture type pour enquête

**Vault Obsidian** comme couche éditoriale (rédaction, notes).

**Graphe local (Neo4j ou Jena)** comme couche structurée.

**Synchronisation** : scripts qui extraient entités/relations depuis Obsidian vers le graphe, et réciproquement.

**Visualisation** : Neo4j Bloom, Gephi (depuis export).

## 66.7 Knowledge graphs et LLMs

**Pattern émergent 2025-2026.** Combiner LLM + knowledge graph.

**Use case.**

- LLM extrait entités d'un document.
- Entités sont ajoutées au graphe.
- LLM peut interroger le graphe pour répondre à questions complexes.
- Permet « questions naturelles » répondues sur données structurées.

**Outils.**

- **LangChain** avec graph stores.
- **LlamaIndex** avec knowledge graph index.
- **GraphRAG** (Microsoft).

## 66.8 OPSEC du knowledge graph

**Localisation.** Stockage local. Chiffrement disque.

**Accès.** Limité à analystes autorisés.

**Sauvegarde.** Chiffrée, 3-2-1.

**Destruction.** Purge sécurisée en fin d'enquête (RGPD).

## 66.9 Pièges classiques

**Sur-modélisation.** Créer 50 types de relations alors que 10 suffisent. Complication inutile.

**Sous-cotation.** Oublier de coter les faits ajoutés au graphe.

**Pas de provenance.** Chaque triplet doit pointer vers une source (named graph).

**Bruit.** Ajouter tout au graphe → graphe ingérable.

## 66.10 Cas d'usage MIRAGE

Pour MIRAGE, knowledge graph résumant :

- 4 sociétés (TechnoVert, Delta Consulting, Verde Holdings, SCI La Provence Familiale).
- ~50 personnes (employés, dirigeants, contacts, journalistes mentionnés, etc.).
- ~30 domaines et comptes.
- ~100 événements datés.
- Relations : employer, director, owner, located_at, communicates_with, mentions, etc.

Requête type : « Quels sont les chemins de relations entre Delaunay et le cluster X de désinformation ? » → graphe répond en quelques lignes SPARQL.

## 66.11 Synthèse

| Bénéfice | Coût |
|---|---|
| Requêtes complexes | Apprentissage (RDF/Neo4j/SPARQL) |
| Visualisation | Maintenance technique |
| Inférence | Modélisation initiale |
| Souveraineté | Investissement temps |
| Réutilisabilité | Discipline (provenance, cotation) |

Pour enquêtes complexes (>200 entités), le knowledge graph devient un investissement rentable.

-----
