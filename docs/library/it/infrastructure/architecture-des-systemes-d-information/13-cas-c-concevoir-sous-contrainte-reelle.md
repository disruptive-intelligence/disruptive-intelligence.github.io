---
title: Cas C — Concevoir sous contrainte réelle
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - index.md
---

> **Durée** 2 h 30 · **Livrables** : architecture · registre des compromis · liste de ce qui reste à vérifier
> **Prérequis** : Partie IX

## C.1 La situation

**L'organisation** : 450 personnes, deux sites, fabricant de composants électroniques.

**Le besoin** : publier un portail permettant à 80 clients de suivre l'avancement de leurs commandes et de télécharger des documents techniques.

**Les contraintes**, telles qu'elles vous sont données — et deux ne sont pas chiffrées :

```
DISPONIBILITÉ   « Il faut que ce soit fiable »
PERFORMANCE     Non exprimée
COÛT            60 k€ d'investissement · 1,5 personne à l'exploitation, en tout
SÉCURITÉ        Documents techniques = propriété industrielle. Sensible.
CONFORMITÉ      Données de contact clients
HISTOIRE        L'ERP existant contient les données de commande.
                Version 2019, éditeur actif, interface applicative disponible.
                Aucune zone démilitarisée aujourd'hui. Rien n'est publié.
```


## C.2 Les questions

1. Que faites-vous des deux contraintes non chiffrées ?
2. Produisez deux options, avec leurs compromis.
3. Retenez-en une, et écrivez le registre.
4. Que reste-t-il à vérifier avant de s'engager ?

## C.3 Corrigé — les contraintes non chiffrées

**C'est la première tâche, et la plus déterminante** — §46.3.

| Contrainte | Ce qu'on demande | Pourquoi |
|---|---|---|
| **Disponibilité** | *« Si le portail est indisponible une demi-journée en semaine, que se passe-t-il ? »* | *« Fiable »* ne se conçoit pas. **Une réponse chiffrée détermine la moitié de l'architecture** |
| **Performance** | *« Combien de clients simultanés, et quelle taille de documents ? »* | 80 clients qui consultent occasionnellement et 80 qui téléchargent des fichiers lourds ne produisent pas la même architecture |

**Réponses obtenues** *(à supposer pour la suite)* : une demi-journée est tolérable · consultations occasionnelles, documents jusqu'à 50 Mo.

⚠️ **Ce que cette réponse change immédiatement** : une interruption d'une demi-journée tolérable **élimine la nécessité d'une redondance complète**, et libère l'essentiel du budget pour la sécurité — qui est la contrainte réellement forte ici.

## C.4 Corrigé — les deux options

| | **Option A — publication directe** | **Option B — zone démilitarisée avec mandataire** |
|---|---|---|
| Composants nouveaux | 1 serveur portail | Mandataire inverse · serveur portail · segment DMZ · règles |
| Accès à l'ERP | Le portail interroge l'ERP directement | **Le portail interroge une copie**, alimentée depuis l'ERP |
| Exposition de l'ERP | **L'ERP est atteignable depuis un serveur exposé** | L'ERP n'est jamais atteignable depuis l'extérieur |
| Investissement | ≈ 20 k€ | ≈ 45 k€ |
| Exploitation | 0,2 personne | **0,6 personne** |
| Une faille du portail | Donne accès à l'ERP de 2019, non supporté | Donne accès à une copie de données |

**Retenu : l'option B**, et le raisonnement tient en une ligne :

> **La contrainte forte de ce dossier n'est pas la disponibilité, c'est la propriété industrielle.** L'option A place un serveur exposé en communication directe avec un progiciel de 2019 — c'est-à-dire le composant le moins maintenable de l'organisation.

⚠️ **Le point de conception le plus important est la copie de données.** Le portail ne lit pas l'ERP : il lit une base alimentée par un export périodique. Cela dégrade la fraîcheur — les données ont jusqu'à une heure de retard — et **supprime tout chemin depuis l'extérieur vers l'ERP**. C'est un compromis, et il doit être écrit.

## C.5 Corrigé — le registre des compromis

| # | Compromis | Privilégié | Dégradé | Conséquence acceptée | Revoir si |
|---|---|---|---|---|---|
| **1** | Aucune redondance du portail | Coût, exploitation | Disponibilité | Interruption jusqu'à une demi-journée | La tolérance métier change · le nombre de clients croît |
| **2** | **Copie de données au lieu d'accès direct à l'ERP** | **Sécurité** | Fraîcheur | Données à jour à une heure près | Un besoin de temps réel apparaît |
| **3** | Mandataire inverse unique | Coût | Disponibilité externe | Le portail devient injoignable si le mandataire tombe | La disponibilité devient critique |
| **4** | Authentification par comptes locaux au portail | Simplicité, indépendance | Gouvernance des identités | 80 comptes à gérer séparément | Le nombre de clients dépasse ~200 |
| **5** | Pas de détection sur le serveur portail | Coût | Observabilité | On dépend des journaux du mandataire | Le budget le permet l'an prochain |

**Ce que le registre rend possible dans dix ans** : quelqu'un qui découvrira ce portail comprendra **pourquoi il lit une copie** au lieu de l'ERP — et ne conclura pas à une incohérence. C'est le chapitre 4, par anticipation.

## C.6 Corrigé — ce qui reste à vérifier

**La section qui distingue une proposition d'un engagement** — §7.3.

| # | À vérifier | Pourquoi | Qui |
|---|---|---|---|
| 1 | **L'interface de l'ERP 2019 permet-elle l'export nécessaire ?** | Toute l'option B en dépend | Éditeur |
| 2 | Quelle est la charge réelle des téléchargements de 50 Mo ? | Dimensionne le lien Internet | Métier + réseau |
| 3 | Le lien Internet actuel supporte-t-il un usage entrant ? | Aujourd'hui il ne sert qu'à sortir | Réseau |
| 4 | **Qui exploitera le mandataire ?** | 0,6 personne sur 1,5 disponible : est-ce tenable ? | DSI |
| 5 | Les documents techniques sont-ils tous partageables ? | Certains peuvent être sous accord de confidentialité | Juridique, R&D |
| 6 | Le basculement en cas de panne du portail a-t-il un mode dégradé ? | Envoi manuel par courriel ? | Métier |

⚠️ **La question 4 est celle qui peut faire échouer le projet**, et c'est le §47.3 : une architecture qui consomme 0,6 exploitant sur 1,5 disponible laisse 0,9 pour tout le reste du système d'information. **Si la réponse est non, l'option A revient sur la table — avec ses compromis, écrits.**

## C.7 Le barème

| Critère | Pts |
|---|---|
| Chiffrer les deux contraintes manquantes **avant** de concevoir | **25** |
| Identifier que la contrainte forte est la propriété industrielle, pas la disponibilité | **20** |
| Proposer la copie de données plutôt que l'accès direct à l'ERP | **20** |
| Registre des compromis complet, avec conditions de réexamen | 15 |
| Liste de ce qui reste à vérifier, dont la capacité d'exploitation | 15 |
| Ne pas surconcevoir | 5 |

**Élimination** : proposer une architecture redondée sans avoir chiffré la disponibilité tolérable.

📌 **Une autre architecture que l'option B est recevable** si elle est justifiée par un arbitrage écrit. Ce qui n'est pas recevable, c'est d'arbitrer sans avoir demandé les deux contraintes manquantes — §46.3.

---
