---
title: Chapitre 19 — Outillage de déploiement par plateforme
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

> **Note de lecture.** Ce chapitre traite des **familles d'outils**, de leurs mécanismes et de leurs limites structurelles. Les outils nommés, leurs modèles de licence et leurs limites propriétaires figurent en **Annexe E**, qui est datée et versionnée. Cette séparation est délibérée : les mécanismes ci-dessous resteront valables quand les produits auront changé.

## 19.1 La grille de choix, indépendante des produits

Neuf critères suffisent à évaluer n'importe quel outil de déploiement, et à comprendre pourquoi aucun ne suffit seul.

| Critère | Question | Piège fréquent |
|---|---|---|
| **Couverture** | Quels systèmes, quelles applications tierces, quels micrologiciels ? | La couverture annoncée inclut rarement les applications métier |
| **Hors domaine** | Gère-t-il les machines non jointes à l'annuaire ? | C'est précisément là que sont les actifs à risque |
| **Itinérance** | Fonctionne-t-il sans réseau interne ? | Sinon, les nomades décrochent (§18.12) |
| **Bande passante** | Cache local, distribution entre pairs, limitation ? | Sites distants saturés |
| **Granularité** | Peut-on cibler par anneau, par attribut, par exclusion ? | Sans cela, pas d'anneaux (§18.4) |
| **Critères d'arrêt** | Peut-on suspendre automatiquement une campagne ? | Rarement natif ; souvent à construire |
| **Reporting** | Peut-on exporter les données brutes, avec les non joignables ? | Le calcul honnête du §15.6 est souvent impossible nativement |
| **Réversibilité** | Peut-on revenir en arrière, et l'outil le trace-t-il ? | Dépend surtout de la plateforme (§2.5) |
| **Coût et dépendance** | Modèle de licence, portabilité de l'historique | L'historique est rarement exportable |

**Le critère décisif à long terme est le septième.** Un outil qui ne permet pas d'exporter ses données brutes vous empêche de calculer vos propres indicateurs (chapitre 38), de constituer une preuve indépendante (§2.9), et de changer de fournisseur sans perdre votre antériorité.

## 19.2 Écosystème Windows

**Les mécanismes.** Quatre approches coexistent, souvent combinées dans un même parc :

| Approche | Principe | Adaptée à |
|---|---|---|
| **Service de mise à jour interne** | Un serveur relaie et approuve les correctifs de l'éditeur | Parcs sur site, contrôle fin des approbations |
| **Gestion de configuration d'entreprise** | Déploiement centralisé, applications tierces incluses | Grands parcs, besoins de granularité |
| **Gestion de flotte depuis le cloud** | Politiques appliquées aux machines où qu'elles soient | Nomades, hors domaine, parcs distribués |
| **Anneaux natifs de l'éditeur** | Découpage et échelonnement gérés par le service de l'éditeur | Postes standards, faible charge d'administration |

**Les trois points d'attention propres à Windows :**

1. **Les applications tierces ne sont pas couvertes par défaut.** Navigateurs, lecteurs, environnements d'exécution, clients d'accès distant représentent une part majeure des vulnérabilités exploitées sur poste, et exigent un mécanisme complémentaire (§19.5).
2. **Le redémarrage se pilote séparément** du déploiement. Un correctif installé et jamais redémarré n'est pas effectif — et les machines qui ne redémarrent jamais sont fréquentes.
3. **La réversibilité ne se présume pas** (§2.5).

## 19.3 Écosystème Linux

| Mécanisme | Principe | Point d'attention |
|---|---|---|
| **Dépôts internes et miroirs** | Vous maîtrisez ce qui est publié et quand | Le miroir doit lui-même être maintenu et synchronisé |
| **Mise à jour non supervisée** | Le système applique seul les correctifs de sécurité | Efficace sur C3 ; à encadrer sur C1 (redémarrages, régressions) |
| **Gestion de configuration** | Un outil applique un état désiré sur un parc | Le plus flexible ; exige des compétences et du maintien |
| **Orchestration des redémarrages** | Détection et planification des redémarrages nécessaires | C'est ici que les campagnes Linux échouent (§2.6) |

⚠️ **PIÈGE — la mise à jour automatique sans orchestration du redémarrage**
Configuration très répandue : les correctifs s'appliquent automatiquement, personne ne redémarre les services, et l'organisation croit son parc à jour. Les bibliothèques corrigées sur disque continuent d'être exécutées en version vulnérable, parfois pendant des mois.

## 19.4 macOS et mobiles

Trois particularités : les mises à jour sont **imposées par l'éditeur** avec peu de latitude de report ; le déploiement passe par une solution de gestion de flotte, sans équivalent des dépôts internes ; et l'utilisateur conserve souvent un pouvoir de report, ce qui rend la conformité dépendante de son comportement.

**La conséquence pour le MCS** : sur ces plateformes, vous pilotez surtout par la **politique** (exiger une version minimale pour accéder aux ressources) plutôt que par le déploiement. L'accès conditionnel fondé sur le niveau de mise à jour est le levier réel — traité au §28.8.

## 19.5 Applications tierces : le trou noir du poste de travail

**Le constat.** Une part majeure des vulnérabilités réellement exploitées sur les postes concerne des applications tierces : navigateurs et leurs extensions, lecteurs de documents, environnements d'exécution, outils de compression, clients d'accès distant, utilitaires métier.

**Pourquoi elles échappent au dispositif :** elles ne sont pas couvertes par le mécanisme natif du système ; elles sont souvent installées hors processus ; leur inventaire est incomplet ; et elles se mettent à jour chacune selon son propre mécanisme, parfois en demandant des droits d'administration.

**Les trois approches**, par efficacité :

| Approche | Principe | Limite |
|---|---|---|
| Gestionnaire de paquets pour Windows | Catalogue centralisé, déploiement et mise à jour scriptables | Couverture du catalogue variable selon les applications métier |
| Module de mise à jour d'applications tierces intégré à l'outil de déploiement | Cohérence avec le reste du dispositif | Souvent une option payante, catalogue limité |
| Mise à jour automatique native de l'application | Aucun effort | Aucun contrôle, aucune visibilité, aucune preuve |

✅ **BONNE PRATIQUE (P0)** — Commencez par **inventorier** les applications tierces installées sur un échantillon de postes. La liste est presque toujours plus longue et plus ancienne qu'attendu, et cet inventaire suffit à justifier le budget du mécanisme de déploiement correspondant.

## 19.6 Réseau, sécurité et hyperviseurs

Ces plateformes se distinguent par l'absence d'outil de déploiement au sens classique : la mise à jour est une opération d'administration, unitaire ou orchestrée par la console du constructeur.

| Point | Exigence |
|---|---|
| Cadence | Doctrine de version écrite et datée (§2.7), pas une habitude |
| Séquence | Passif, vérification, bascule, actif — avec les précautions du §2.7 |
| Retour arrière | Double partition d'image, testée |
| Preuve | Version relevée directement sur l'équipement, pas dans un tableur |
| Micrologiciels | Traités comme une campagne à part entière, par anneaux (§3.8) |

## 19.7 Conteneurs et cloud

Le paradigme change complètement : on ne déploie pas un correctif, on **reconstruit et on remplace** (§3.2).

| Objet | Mécanisme de correction | Indicateur pertinent |
|---|---|---|
| Image de conteneur | Reconstruction depuis une image de base à jour | **Âge de l'image** en production |
| Nœuds de cluster | Remplacement des nœuds par de nouvelles images | Version des nœuds, écart avec le plan de contrôle |
| Instances cloud | Redéploiement depuis une image mise à jour | Âge de l'image, part d'instances hors modèle |
| Services managés | Fenêtre de mise à jour du fournisseur | Versions dépréciées et échéances (ch. 30) |

**Le déplacement du travail** est ici essentiel : le MCS ne se joue plus au déploiement mais dans la **chaîne de construction** — donc dans un périmètre souvent détenu par les équipes de développement, pas par l'exploitation. C'est un sujet d'organisation autant que d'outillage (chapitre 28).

## 19.8 ⏱ Consolider le reporting multi-outils

Une organisation de taille intermédiaire utilise couramment cinq à huit mécanismes de déploiement distincts. Chacun produit son propre rapport, avec son propre périmètre, son propre vocabulaire et son propre calcul.

**Le problème du chiffre unique.** Additionner ces rapports produit un nombre faux, pour trois raisons : les périmètres se recouvrent partiellement, les définitions de « conforme » diffèrent d'un outil à l'autre, et les actifs non couverts par aucun outil n'apparaissent nulle part.

✅ **BONNE PRATIQUE (P0) — la consolidation par le périmètre, pas par les outils**
Partez du **périmètre de référence** (chapitre 10), et pour chaque actif, indiquez quel outil le couvre et quel est son état. Les actifs couverts par aucun outil apparaissent alors explicitement — c'est l'information la plus importante que produise cette consolidation, et celle qu'aucun rapport d'outil ne donnera jamais.

## 19.9 📌 Limites communes à toutes les familles

- **Le coût croît avec la découverte.** Les licences par actif créent une incitation perverse : mieux inventorier augmente la facture.
- **Aucun outil ne couvre tout le périmètre réel.** Systèmes industriels, services en ligne, composants embarqués, produits livrés aux clients restent hors champ.
- **Le reporting natif est rarement honnête.** Il présente le taux de conformité sur les actifs que l'outil connaît — c'est-à-dire le chiffre flatteur du §10.11.
- **La dépendance à l'éditeur est forte**, et l'historique rarement portable.
- **L'outil ne crée pas de fenêtre.** La contrainte dominante reste organisationnelle.

## 19.10 ✅ Recommandations priorisées

| Prio | Taille d'organisation | Recommandation |
|---|---|---|
| **P0** | Toutes | Un mécanisme couvrant les systèmes d'exploitation, avec reporting exportable |
| **P0** | Toutes | Un mécanisme pour les applications tierces du poste de travail |
| **P0** | Toutes | La consolidation par le périmètre de référence (§19.8) |
| P1 | > 200 actifs | Anneaux et critères d'arrêt outillés (§18.4) |
| P1 | Parc distribué | Mécanisme fonctionnant hors réseau interne |
| P1 | Toutes | Orchestration des redémarrages, avec indicateur de temps sans redémarrage |
| P2 | > 500 actifs | Automatisation de la vérification post-déploiement |
| P2 | Environnements cloud | Reconstruction périodique automatisée des images |

## 19.11 🔴 FIL ROUGE — mai 2027 : l'inventaire des mécanismes

Avant tout achat, Claire Nadeau demande l'inventaire des mécanismes de déploiement réellement en usage chez HELIOMED. Le résultat surprend tout le monde.

| Mécanisme | Périmètre couvert | Reporting exportable |
|---|---|---|
| Console interne de l'exploitation | 176 serveurs Windows et Linux | Oui |
| Console de l'infogérant | 620 postes | Oui, depuis janvier (§13.9) |
| Mise à jour automatique native, non supervisée | 34 serveurs Linux découverts en 2026 | **Non** |
| Consoles constructeurs | 6 équipements réseau | Non — relevé manuel |
| Chaîne de construction de Nantes | Images de conteneurs | Oui, mais non rattachée au périmètre MCS |
| Aucun | **11 postes de supervision, 3 automates, 38 services en ligne, tous les micrologiciels** | — |

**Six mécanismes, aucune vue consolidée.** Le taux annoncé au comité provenait des deux premiers, soit 796 actifs sur un périmètre de référence en comptant nettement plus.

**Les trois décisions.**

1. **Pas d'achat.** Les deux mécanismes principaux couvrent l'essentiel ; le problème n'est pas l'outillage, c'est la consolidation. Une extraction mensuelle rapprochée du périmètre de référence est mise en place — quelques jours de travail, aucun coût de licence.
2. **Les 34 serveurs en mise à jour automatique non supervisée** sont rattachés à la console interne. Le contrôle révèle au passage que 12 d'entre eux appliquaient bien les correctifs mais n'avaient pas redémarré depuis plus de 400 jours — le piège exact du §19.3.
3. **Les applications tierces du poste de travail** deviennent le seul vrai sujet d'investissement. L'inventaire sur 30 postes remonte 47 applications distinctes, dont 9 hors support. C'est la ligne budgétaire retenue pour 2028.

**Ce que Claire écrit dans sa note.** *Nous n'avions pas un problème d'outil, nous avions un problème de dénominateur. L'achat d'un outil supplémentaire aurait produit un septième rapport partiel.*

**Livrable de l'épisode.** La consolidation par périmètre, et l'inventaire des applications tierces — première ligne du budget 2028.

→ La suite en 🔴 §20.11, quand une ligne d'assemblage ne pourra pas être arrêtée avant novembre.

→ **Chapitre 20 — Quand on ne peut pas patcher : les mesures compensatoires** : que faire quand corriger est impossible.

## Synthèse mentale du chapitre 19

Neuf critères évaluent n'importe quel outil de déploiement, et le plus décisif à long terme est l'exportabilité des données brutes : sans elle, pas d'indicateur propre, pas de preuve indépendante, pas de changement de fournisseur sans perte d'antériorité. Sous Windows, les applications tierces échappent au mécanisme natif alors qu'elles concentrent une part majeure des vulnérabilités exploitées sur poste. Sous Linux, la mise à jour automatique sans orchestration des redémarrages produit un parc que l'on croit à jour et qui exécute encore du code vulnérable. Sur les mobiles, on pilote par la politique d'accès plutôt que par le déploiement. Dans le cloud et les conteneurs, le MCS se déplace vers la chaîne de construction, souvent détenue par d'autres équipes. Enfin, additionner les rapports de cinq outils produit un chiffre faux : la consolidation part du périmètre de référence, et son résultat le plus précieux est la liste des actifs couverts par aucun outil.

**Trois questions de vérification**

1. Vous évaluez un outil de déploiement. Quel critère privilégiez-vous pour l'horizon à cinq ans, et quelles trois capacités perdez-vous s'il n'est pas rempli ?
2. Votre parc Linux applique automatiquement les correctifs de sécurité. Quelle vérification faites-vous avant de le considérer comme à jour ?
3. Cinq outils rapportent chacun plus de 95 % de conformité. Pourquoi ne pouvez-vous pas en déduire un taux global, et comment procédez-vous ?

---
