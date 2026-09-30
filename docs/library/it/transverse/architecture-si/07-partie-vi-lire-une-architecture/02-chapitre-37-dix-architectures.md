---
title: Chapitre 37 — Dix architectures
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE VI — Lire une architecture
  - index.md
---

> Complexité croissante. Chacune suit le format : schéma · questions · lecture commentée · **ce qu'il fallait observer**.
>
> Les quatre premières sont développées ici ; les six suivantes figurent en annexe F, avec leur lecture complète.

## 37.1 Architecture 1 — Une application interne, trois composants

```
   [ 40 postes ] ──► [ serveur applicatif ] ──► [ base ]
```


❓ **Trois questions** : où s'authentifie-t-on ? · qu'est-ce qui n'est pas dessiné ? · quel est le point de rupture ?

**Lecture** — c'est l'architecture d'Atelier Martin. Deux composants, un point de rupture par composant, aucune redondance. **Et c'est un choix cohérent** : quarante utilisateurs, une interruption d'une journée est tolérable, le coût d'une redondance n'est pas justifié par la contrainte.

👁 **CE QU'IL FALLAIT OBSERVER**
L'authentification n'est pas représentée. Deux cas possibles, et ils changent tout : soit l'application a sa propre base d'utilisateurs — auquel cas les mots de passe vivent dans la base, et leur qualité dépend de l'éditeur — soit elle interroge un annuaire, qui devient alors un troisième point de rupture invisible.

## 37.2 Architecture 2 — Un site web public

```
   Internet ──► [ pare-feu ] ──► [ mandataire ] ──► [ web ] ──► [ base ]
```


❓ Où passe la frontière 2 ? · qui voit le contenu en clair ? · que se passe-t-il si le certificat expire ?

**Lecture** — le mandataire termine le chiffrement : **il voit tout en clair**. C'est le point le plus sensible du schéma, et il est en zone démilitarisée, c'est-à-dire dans la zone dont on suppose qu'elle sera compromise.

👁 **CE QU'IL FALLAIT OBSERVER**
Aucune frontière n'est représentée entre le mandataire et le serveur web. Si elle n'existe pas, un mandataire compromis atteint directement le web, puis la base. **La DMZ n'en est alors pas une** — §25.1.

## 37.3 Architecture 3 — Trois niveaux, avec redondance partielle

C'est le schéma 1.1, celui d'HELIOMED.

❓ Où s'arrête la redondance ? · combien de points de rupture invisibles ? · pourquoi un seul applicatif ?

**Lecture** — quatre points de rupture, dont trois invisibles : base, applicatif, résolution de noms, annuaire. La redondance visible — trois serveurs web — porte sur le composant le plus facile à redonder et le moins critique.

👁 **CE QU'IL FALLAIT OBSERVER**
**La rupture de symétrie est une information, pas une erreur.** Trois web et un applicatif signalent un arbitrage : ici, le coût de licence de 2021 — §4.6. Un lecteur exercé demande l'histoire ; un débutant conclut à une incohérence. C'est le chapitre 4.

## 37.4 Architecture 4 — Un système hérité mal documenté

```
   [ postes ] ──► [ AS400-PROD ] ──► ?
                        │
                   [ HERMES ] ──► [ export nocturne ] ──► [ décisionnel ]
                        ▲
                        └─── [ automates usine ]
```


❓ Que fait `HERMES` ? · qui l'administre ? · que se passe-t-il s'il tombe ?

**Lecture** — c'est le cas du §4.6. Un composant de 2011, portant un ancien outil de gestion de production, recevant un flux quotidien de l'usine. **Personne ne sait exactement ce qu'il fait encore.**

👁 **CE QU'IL FALLAIT OBSERVER**
Trois signes convergent : un nom hors convention · une position à cheval entre deux mondes · un flux nocturne. **Les trois désignent une strate ancienne** — §4.2. La bonne réaction n'est pas de proposer sa suppression, c'est de demander sa date et son motif. Il porte peut-être une intégration que plus personne ne sait refaire.

## 37.5 Deux mauvaises architectures

> **Aussi formateur que les bonnes.** Apprendre à repérer l'excès d'architecture est aussi important que d'en repérer l'insuffisance.

### Architecture 4 bis — l'insuffisance

```
                       Internet
                          │
                    [ pare-feu ]
                          │
        ┌─────────┬───────┴───────┬─────────┐
        │         │               │         │
   [ postes ] [ admin ]    [ application ] [ base ]
```


❓ **Qu'est-ce qui vous gêne ?**

| # | Constat | Pourquoi c'est grave |
|---|---|---|
| 1 | **Une seule zone** | Le pare-feu ne protège que du dehors. Tout est joignable de partout à l'intérieur — §24.1 |
| 2 | **L'administration au même niveau que les postes** | Un poste compromis atteint les outils d'administration — §27 |
| 3 | **La base joignable depuis les postes** | L'architecture en couches n'existe pas : on peut contourner l'application |
| 4 | **Aucune DMZ** | Si un service est publié, il l'est depuis l'interne |
| 5 | Ce qu'on ne voit pas | Résolution, annuaire, sauvegarde, journalisation — §3.4 |

⚠️ **Et pourtant, cette architecture n'est pas nécessairement fautive.** Chez une organisation de trente personnes, sans service publié, sans données sensibles, avec un informaticien à mi-temps, **elle peut être un arbitrage défendable** — §48.1. Ce qui la rend fautive, c'est de la trouver dans une organisation de sept cents personnes qui publie un portail client.

> **La question n'est jamais « cette architecture est-elle bonne ? » mais « pour quelle contrainte a-t-elle été conçue, et cette contrainte est-elle encore la bonne ? »**

### Architecture 4 ter — l'excès

```
   40 salariés · 1 site · 1 application métier · 1 informaticien
                              │
                    2 centres de données
                              │
                        4 pare-feu
                              │
                     orchestration de conteneurs
                              │
                       maillage de services
                              │
                        12 microservices
                              │
                     2 fournisseurs cloud
```


❓ **Qu'est-ce qui justifie chacune de ces briques ?**

| Brique | Contrainte invoquée | Contrainte réelle |
|---|---|---|
| Deux centres de données | « Continuité » | **Quelle interruption est tolérable ? Personne ne l'a chiffrée** |
| Quatre pare-feu | « Sécurité » | Combien de frontières y a-t-il réellement à contrôler ? |
| Orchestration de conteneurs | « Modernité » | **Aucune** — une seule application, pas de variabilité de charge |
| Maillage de services | « Observabilité » | Aucune — douze services que rien n'obligeait à séparer |
| Douze microservices | « Agilité » | **Aucune** — une équipe, un cycle de livraison |
| Deux fournisseurs cloud | « Résilience » | **Deux plateformes à maîtriser au lieu d'une** |

⚠️ **Le diagnostic, et il est sévère** : cette architecture consomme probablement **cinq à huit exploitants** là où l'organisation en a **un**. Selon le §47.2, elle se dégradera en trois ans jusqu'au niveau réel de compétence disponible — **après avoir coûté le prix de l'ambition**.

**Ce qu'un lecteur exercé dit en réunion** :

> *« Je ne vois pas laquelle de ces briques répond à une contrainte chiffrée. Pouvez-vous me dire, pour chacune, quelle interruption ou quelle perte elle évite ? »*

**C'est la question du principe 9** — *ajouter n'est jamais gratuit* — appliquée à une architecture entière.

👁 **CE QU'IL FALLAIT OBSERVER, dans les deux cas**

| Architecture | L'erreur du lecteur débutant |
|---|---|
| **L'insuffisante** | Conclure « c'est mal fait » sans demander la taille, l'exposition et les moyens |
| **L'excessive** | Conclure « c'est bien fait » parce que les briques sont modernes |

> **Les deux erreurs sont la même** : juger l'architecture sans connaître la contrainte.

## 37.6 Les six architectures suivantes

Développées en annexe F, avec le même format :

| # | Architecture | Ce qu'elle enseigne |
|---|---|---|
| 5 | Haute disponibilité complète | Le coût de la symétrie, et ce qu'elle ne couvre pas |
| 6 | Multi-sites | L'autonomie locale, et ce qui manque pour l'obtenir |
| 7 | Hybride | Un point de fragilité récurrent — chapitre 40 |
| 8 | Industrielle | L'inversion des priorités — chapitre 28 |
| 9 | **Réelle et désordonnée** | Vingt ans de sédimentation, sans documentation |
| 10 | Le système complet d'HELIOMED | La synthèse du fil rouge |

⚠️ **La neuvième est la plus formatrice**, et c'est celle que vous rencontrerez en arrivant quelque part.

---
