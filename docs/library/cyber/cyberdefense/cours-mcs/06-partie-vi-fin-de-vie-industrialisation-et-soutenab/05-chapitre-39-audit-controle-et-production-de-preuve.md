---
title: Chapitre 39 — Audit, contrôle et production de preuve
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE VI — Fin de vie, industrialisation et soutenabilité
  - index.md
---

## 39.1 Ce que « prouver son MCS » signifie

Prouver, ce n'est ni affirmer ni montrer un tableau de bord. C'est établir quatre choses, et l'ordre compte :

| # | Ce qu'il faut établir | Sans quoi |
|---|---|---|
| 1 | **Le périmètre** : sur quoi porte le dispositif, et ce qui en est exclu | Tout le reste est invérifiable |
| 2 | **La règle** : ce que l'organisation s'engage à faire, écrit et daté | On ne peut mesurer aucun écart |
| 3 | **L'application** : ce qui a effectivement été fait, avec des données datées | L'engagement reste théorique |
| 4 | **Le traitement des écarts** : ce qui n'a pas été fait, et pourquoi c'est décidé | La preuve devient une fiction |

**Le quatrième point est celui qui distingue un dossier crédible d'un dossier de façade.** Un dossier sans écart n'est pas un bon dossier, c'est un dossier incomplet — aucune organisation n'applique 100 % de sa politique sur 100 % de son parc. Ce que regarde un auditeur, c'est si les écarts sont **connus, décidés et suivis**.

## 39.2 Le dossier de preuves

Structuré une fois, projeté ensuite sur chaque référentiel (§8.8). Onze pièces.

| # | Pièce | Contenu | Chapitre |
|---|---|---|---|
| 1 | **Périmètre de référence daté** | Sources, réconciliation, écarts expliqués, zones déclarées non couvertes | 10 |
| 2 | Politique MCS | Version, date, approbation nominative, classes de service | 7 |
| 3 | RACI et comitologie | Rôles, décideurs, fréquence | 9 |
| 4 | Arbre de décision de triage | Daté, validé | 16 |
| 5 | **Journaux de campagne** | Périmètre, exécution, échecs, traîne longue qualifiée | 18 |
| 6 | **Preuves d'état** | Relevés horodatés sur échantillon, indépendants des outils | 2 |
| 7 | Registre des dérogations | Sept champs, signataires, revues | 7, 20 |
| 8 | Registre des exclusions | Scan, protection des postes, avec motif et compensation | 15, 34 |
| 9 | Comptes rendus de comité | **Décisions**, pas discussions | 9 |
| 10 | Indicateurs historisés | Définitions, séries, ruptures marquées | 38 |
| 11 | Procès-verbaux de décommissionnement | Signés, avec vérification | 35 |

✅ **BONNE PRATIQUE (P0)** — Constituez ce dossier **en continu**, pas à l'approche d'un contrôle. Un dossier reconstitué après coup se voit immédiatement : les dates de production sont groupées, les preuves d'état sont postérieures aux campagnes qu'elles documentent, et les comptes rendus manquent d'aspérités.

## 39.3 Se préparer à un contrôle

| Type de contrôle | Ce qui est regardé en priorité |
|---|---|
| **Certification** | Existence et fonctionnement du système de management ; échantillonnage |
| **Autorité** | Conformité aux obligations applicables, traitement des incidents |
| **Client** | Ce qui concerne **son** périmètre : sa donnée, son service, ses délais |
| **Assureur** | Les points du questionnaire, et leur cohérence avec la réalité (§37.3) |
| **Audit interne** | Écart entre la règle et la pratique |

**Les six constats les plus fréquents**, et le chapitre qui les traite :

| Constat | Origine | Traité au |
|---|---|---|
| Périmètre non défini ou incohérent entre documents | Inventaire absent ou non réconcilié | 10 |
| Indicateurs sans dénominateur | Reporting produit par l'outil | 38 |
| Exceptions non formalisées | Constats anciens jamais qualifiés | 17, 20 |
| Absence de preuve d'application | Clôture sur déclaration | 17, 18 |
| Exclusions non documentées | Actifs difficiles sortis silencieusement | 15, 34 |
| Prestataires non contrôlés | Contrat sans clause de restitution | 13 |

## 39.4 L'audit interne du MCS

Se contrôler soi-même avant qu'un tiers ne le fasse, avec une méthode d'échantillonnage plutôt qu'une revue exhaustive.

**Le plan de contrôle type**, six tests par sondage :

| Test | Méthode | Ce qu'il révèle |
|---|---|---|
| **Test de périmètre** | Prendre 20 actifs au hasard dans une source non utilisée pour le reporting, vérifier leur présence dans le périmètre | Trous d'inventaire |
| **Test d'état** | Vérifier directement sur 15 actifs l'état déclaré conforme | Écart entre déclaration et réalité |
| **Test de délai** | Prendre 10 constats clos, recalculer le délai réel | Fiabilité de l'indicateur |
| **Test de preuve** | Demander la preuve de 10 clôtures | Clôtures sur déclaration |
| **Test de dérogation** | Vérifier que les compensations de 5 dérogations sont **effectivement actives** | Compensations disparues (§20.7) |
| **Test de décommissionnement** | Vérifier les résidus de 5 décommissionnements anciens | Le §35.14 |

**Le cinquième test est le plus productif** : il vérifie une chose que personne ne vérifie jamais, et qui échoue souvent.

## 39.5 Homologation et réhomologation

Dans les contextes où une décision formelle d'autorisation d'usage est requise, le MCS conditionne le maintien de cette décision dans le temps.

| Élément | Ce que le MCS doit fournir |
|---|---|
| Dossier initial | État du système, dispositif de maintien prévu |
| **Maintien** | Preuve que le dispositif fonctionne — c'est le dossier du §39.2 |
| Changements significatifs | Ce qui déclenche un réexamen |
| Réhomologation | Bilan sur la période, écarts, plan |

**Le point pratique** : une homologation prononcée sur la base d'un dispositif de MCS qui n'a pas fonctionné devient contestable. C'est un argument utile en interne pour obtenir les moyens du maintien, et non seulement ceux de la mise en service.

## 39.6 ⚠️ Les preuves qui ne prouvent rien

| Preuve produite | Pourquoi elle ne vaut rien |
|---|---|
| Capture d'écran non datée | Ni date, ni périmètre, ni intégrité |
| Extraction d'outil sans périmètre | On ignore sur quoi elle porte (§15.8) |
| Chiffre agrégé sans dénominateur | Interprétation impossible |
| Politique non approuvée | Un projet n'engage personne |
| Compte rendu relatant des discussions | Aucune décision traçable |
| Déclaration d'un prestataire sans donnée | Confiance, pas preuve (§13.3) |
| Rapport présentant 100 % de conformité | Possible sur un petit périmètre maîtrisé, mais doit déclencher un examen du périmètre, des exclusions et des actifs non joignables |
| Dossier constitué en trois jours | Les métadonnées le montrent |

## 39.7 Conserver la preuve

| Exigence | Contenu |
|---|---|
| Durée | Alignée sur les obligations applicables et la durée de vie des actifs — souvent 3 à 5 ans |
| **Intégrité** | Horodatage, stockage non modifiable, ou signature |
| **Indépendance des outils** | Export en format ouvert : un changement d'outil ne doit pas effacer l'antériorité (§15.12) |
| Accessibilité | Retrouvable en heures, pas en jours |
| Continuité | Les changements de définition et de périmètre sont documentés (§38.7) |

## 39.8 🔴 FIL ROUGE — janvier 2029 : la revue interne

Trois ans après l'arrivée de Claire Nadeau, HELIOMED conduit sa première revue interne complète du dispositif de MCS, avec un auditeur externe mandaté par la direction générale — en préparation d'une exigence client et de la renégociation d'assurance.

**Le dossier présenté** : les onze pièces du §39.2, constituées en continu depuis 2026.

**Les quatre écarts constatés.**

| # | Écart | Origine |
|---|---|---|
| 1 | **12 actifs du périmètre de référence absents de tout outil de gestion** | Machines de laboratoire de Nantes, créées après la dernière réconciliation |
| 2 | **Compensations de 2 dérogations sur 5 testées non actives** | Une règle de filtrage supprimée lors d'une refonte réseau en juin 2028, sans que la dérogation ne soit alertée |
| 3 | **Preuve d'état manquante sur 3 campagnes de 2027** | Clôtures fondées sur le rapport de console seul, sans échantillon vérifié |
| 4 | **Registre des exclusions de la protection des postes incomplet** | 6 exclusions ajoutées après la revue de juillet 2028, non enregistrées |

**Ce que l'auditeur relève comme point fort**, et c'est ce que Claire retient : *« L'organisation connaît ses écarts. Les quatre constats de cet audit portent sur des dispositifs qui existent et qui ont partiellement failli, pas sur des dispositifs absents. Le point le plus favorable du dossier est l'annexe des périmètres déclarés non couverts, tenue depuis 2026. »*

C'est l'annexe d'une page ajoutée à la politique v1 en mai 2026 (§7.7) — celle qui ressemblait à un aveu de faiblesse.

**L'écart n° 2 est celui qui préoccupe le plus l'équipe.** Une compensation disparue signifie qu'un risque accepté sous condition était en réalité porté sans condition, pendant sept mois, sans que personne ne le sache. C'est très exactement le mécanisme du §20.7, attribut 4 — le moyen de vérification existait sur la fiche, mais le contrôle mensuel n'avait pas été réalisé depuis mars.

**Les corrections décidées.**

1. **Contrôle des compensations** inscrit comme point d'ordre du jour permanent du comité MCS, avec test effectif et non déclaratif — cinq minutes par mois (§20.7).
2. **Réconciliation d'inventaire** portée de trimestrielle à mensuelle, automatisée (§10.7).
3. **Échantillon de preuve d'état** rendu obligatoire pour toute campagne de plus de 20 actifs, avec le point de contrôle du §15.13.
4. **Registre des exclusions** rattaché au workflow : aucune exclusion ne peut être ajoutée sans ticket (§34.4).

**Le résultat externe.** L'assureur accepte de ramener la surprime de 34 % à 6 %, sur la base du dossier de preuves et de la trajectoire sur huit trimestres. Le gain annuel dépasse le coût cumulé de l'outillage acquis depuis 2026.

**Ce que Pierre Vasseur dit en clôture du comité**, et qui referme le fil rouge ouvert au §1.9 : *« En octobre 2025, on nous a reproché de ne pas pouvoir démontrer un processus qui existait. Aujourd'hui, on nous reproche quatre écarts dans un processus que nous démontrons. C'est exactement la différence que je voulais. »*

→ **Fin de la Partie VI.** La suite en Partie VII, avec la construction d'un programme complet et les trois cas de synthèse.

→ **Chapitre 40 — Construire un programme MCS de zéro à douze mois** : mettre tout cela en séquence sur douze mois.

## Synthèse mentale du chapitre 39

Prouver son MCS suppose d'établir quatre choses dans l'ordre : le périmètre, la règle, l'application, et le traitement des écarts. Le quatrième distingue un dossier crédible d'un dossier de façade — un dossier sans écart n'est pas bon, il est incomplet, car aucune organisation n'applique 100 % de sa politique sur 100 % de son parc. Onze pièces composent le dossier, à constituer en continu : reconstitué après coup, il se voit immédiatement. L'audit interne se conduit par sondages, et le test le plus productif est celui que personne ne fait jamais — vérifier que les compensations des dérogations sont effectivement actives. Enfin, un rapport annonçant 100 % de conformité est statistiquement invraisemblable : il signale que les actifs non joignables ont été omis.

**Trois questions de vérification**

1. Un auditeur vous demande de démontrer votre gestion des correctifs. Quelles quatre choses devez-vous établir, et dans quel ordre ?
2. Pourquoi un dossier de preuves ne comportant aucun écart est-il un mauvais signe plutôt qu'un bon ?
3. Parmi les six tests d'audit interne, lequel échoue le plus souvent, et pourquoi personne ne le réalise-t-il spontanément ?

---

---

> ### 🎓 À ce stade de la Partie VI, vous savez…
>
> - **retirer** un système proprement, et vérifier qu'il ne survit pas dans les comptes, les clés, les certificats et les sauvegardes ;
> - **automatiser** dans le bon ordre, et reconnaître le seul critère qui autorise l'auto-remédiation ;
> - **chiffrer** le MCS, construire un dossier d'investissement à trois options, et repérer les seuils de rupture d'une équipe ;
> - **définir** un indicateur avec sa population éligible et son dénominateur, et distinguer une mesure d'un ratio conservateur ;
> - **constituer** un dossier de preuves en continu, et conduire un audit interne par sondages.
>
> **Ce qu'il vous reste** : mettre tout cela en séquence, et l'éprouver sur des cas. C'est l'objet de la Partie VII.
