---
title: Chapitre 19 — Le serveur applicatif
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE III — Les serveurs et l'exécution
  - index.md
---

## 19.1 À quoi ça sert

Exécuter la logique métier : calculer, décider, orchestrer, appeler la base.

**Pourquoi c'est le composant le plus important du chemin, en sécurité.** C'est le seul qui connaisse simultanément **l'utilisateur réel et l'action métier** — §43.3. Un journal de pare-feu dit *« une adresse a ouvert une connexion »* ; un journal d'applicatif dit *« Marie a exporté quatre mille lignes »*.

## 19.2 Ce qu'il fait à la donnée

Il la traite, la transforme, décide qui a le droit de la voir. **C'est là que réside la logique d'autorisation** — donc le composant dont la compromission permet de contourner les règles métier.

⚠️ **Une conséquence importante et mal connue** : l'applicatif interroge très souvent la base avec **un compte de service unique**, pas avec l'identité de l'utilisateur. **Le journal de la base ne voit donc pas l'utilisateur final.** Corréler exige de traverser deux journaux, et suppose une horloge commune — §34.1.

## 19.3 Pourquoi il est souvent le point de rupture

| Raison | Explication |
|---|---|
| **Il porte de l'état** | Sessions, files de traitement, caches applicatifs |
| **Il est difficile à redonder** | Deux exemplaires supposent que l'état soit partagé ou externalisé |
| **Les licences le limitent** | Un second exemplaire est parfois facturé au prix du premier — §4.6 |
| **Les traitements planifiés** | Certains ne doivent s'exécuter **qu'une fois** — deux exemplaires les dupliquent |

⚠️ **La dernière ligne est un piège classique de redondance.** Une application qui exécute un traitement nocturne, redondée sans précaution, l'exécute **deux fois** — avec des conséquences métier parfois graves. C'est l'une des raisons pour lesquelles la redondance applicative est plus difficile qu'elle n'en a l'air.

## 19.4 S'il disparaît

Le site s'affiche et **plus rien ne fonctionne**. C'est un symptôme reconnaissable : la page se charge, les boutons ne répondent plus, des erreurs apparaissent.

🔥 **SCÉNARIO — le site s'affiche, rien ne marche**

| Question | Réponse |
|---|---|
| Symptôme | La page d'accueil s'affiche normalement. Toute action produit une erreur |
| Hypothèse naïve | « Le site est tombé » |
| Dépendance réelle | Le serveur web va bien — **c'est ce qui est derrière qui ne répond plus** |
| Ce que le schéma aurait dû montrer | La séparation web / applicatif, et le contrôle de santé entre les deux |
| Comment vérifier en trente secondes | La page statique s'affiche → web ✅ · une action échoue → applicatif ou base ❌ |

**Ce diagnostic en deux temps est l'un des plus utiles du cours**, et il ne demande aucun accès technique.

## 19.5 Sur un schéma

Entre le web et la base. **Souvent en un seul exemplaire là où le web en compte trois** — et c'est le §1.1.

👁 **CE QU'IL FALLAIT OBSERVER** — la rupture de symétrie est une information, pas une erreur. Trois web et un applicatif signalent un arbitrage : ici, le coût de licence de 2021 — §4.6. **Un lecteur exercé voit la rupture et demande son histoire ; un débutant conclut à une incohérence.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le backend » | L'applicatif, ou la base, ou les deux | **Lequel exactement ?** |
| « L'appli est down » | Le service ne rend plus son objet | Le web répond-il encore ? La distinction oriente le diagnostic |
| « On ne peut pas le doubler » | Un second exemplaire est impossible | **Pourquoi ?** Licence · état local · traitement planifié · trois causes distinctes |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Séparer la logique de la présentation | Une couche, une latence, un composant de plus |
| Mutualiser la logique entre plusieurs frontaux | **Souvent un point de rupture**, car difficile à redonder |
| Concentrer les règles d'autorisation | Une compromission qui donne accès aux données métier |

---
