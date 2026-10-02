---
title: Chapitre 31 — Suivre une session
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

## 31.1 Ce qu'une session change

**Le problème** : la plupart des échanges web sont **sans mémoire**. Chaque requête arrive sans savoir ce qui la précède. Il faut donc un mécanisme pour se souvenir qu'un utilisateur est déjà authentifié.

**Ce mécanisme — un jeton, un cookie — a une conséquence d'architecture majeure** :

> **Là où la session est stockée détermine ce que la redondance peut réellement apporter.**

## 31.2 Les trois emplacements possibles

🖼 **SCHÉMA 31.1 — Où vit la session, et ce que ça change**

```
  A — SESSION LOCALE AU SERVEUR
      [web 1] session ici
      [web 2]                ← si l'utilisateur bascule ici : DÉCONNECTÉ
      → la redondance existe, elle ne protège pas l'utilisateur

  B — SESSION PARTAGÉE
      [web 1] ──┐
      [web 2] ──┼──► [ magasin de sessions ]
      [web 3] ──┘
      → bascule transparente · MAIS un composant de plus,
        et un nouveau point de rupture

  C — SESSION CHEZ LE CLIENT
      Le jeton est porté par le navigateur, signé, non stocké côté serveur
      → aucune dépendance à un magasin central
      → MAIS la révocation immédiate exige de réintroduire
        un mécanisme d'état ou de contrôle
```


| Modèle | Redondance réelle ? | Révocation immédiate ? | Composant de plus ? |
|---|---|---|---|
| **A — locale** | ❌ Apparente seulement | ✅ | Non |
| **B — partagée** | ✅ | ✅ | **Oui, et il devient critique** |
| **C — chez le client** | ✅ | ⚠️ **Différée, ou au prix d'un état réintroduit** | Non |

⚠️ **Le modèle A explique de nombreuses architectures où la redondance ne tient pas ses promesses.** Trois serveurs, un répartiteur, et pourtant les utilisateurs sont déconnectés dès qu'un serveur redémarre. Le schéma montre une redondance ; le comportement en session la contredit.

📌 **Le vrai compromis du modèle C**, plus intéressant que « on ne peut pas révoquer » :

Un jeton autoporté est vérifiable sans interroger personne — c'est tout son intérêt. **Le revers est qu'il reste valide jusqu'à son expiration, même si l'on souhaite l'invalider avant.** Plusieurs stratégies rétablissent une révocation, et **chacune réintroduit une part de ce que le modèle C cherchait à éviter** :

| Stratégie | Ce qu'elle réintroduit |
|---|---|
| Durée de vie très courte + renouvellement | Des appels fréquents au service d'émission |
| Liste de jetons révoqués | Un état partagé à consulter |
| Numéro de version de session | Une consultation à chaque requête |
| Introspection du jeton | Une dépendance au service d'émission |
| Révocation du jeton de renouvellement | Une révocation **différée**, pas immédiate |

⚠️ **C'est un compromis d'architecture, pas une impossibilité technique.** La question n'est pas *« peut-on révoquer ? »* mais **« à quel prix, et sous quel délai ? »**

## 31.3 Le magasin de sessions, composant invisible et critique

**Le modèle B ajoute un composant qui n'apparaît sur presque aucun schéma**, et qui a trois propriétés :

| Propriété | Conséquence |
|---|---|
| **Toutes les requêtes le consultent** | Une latence ajoutée à chaque requête |
| **Sa panne déconnecte tout le monde** | **Un point de rupture qui n'est pas dessiné** |
| Il contient les sessions actives | **Sa compromission permet d'usurper des sessions en cours** |

🔥 **SCÉNARIO — tout le monde est déconnecté d'un coup**

| Question | Réponse |
|---|---|
| Symptôme | Tous les utilisateurs sont déconnectés simultanément. Les serveurs web vont bien |
| Hypothèse naïve | « Un redémarrage applicatif » |
| Dépendance réelle | **Le magasin de sessions** — modèle B |
| Ce que le schéma aurait dû montrer | Ce composant, et le fait que toutes les requêtes le traversent |
| Concevoir différemment | Le redonder · ou accepter le modèle A avec ses limites, en le sachant |

## 31.4 Où passe le jeton, et où il fuit

| Endroit | Risque |
|---|---|
| Dans le navigateur | Vol par une extension, par un logiciel malveillant sur le poste |
| Dans les journaux | **S'il apparaît dans une adresse consultée, il est journalisé partout** |
| Chez le mandataire inverse | Il le voit en clair, en modes B et C — §12.3 |
| Dans les caches intermédiaires | Un jeton mis en cache peut être servi à un autre |

**La deuxième ligne est un cas d'école** : un jeton passé dans une adresse est enregistré par le poste, le mandataire, le pare-feu, le serveur web et la collecte de journaux. **Il devient lisible par tous ceux qui ont accès aux journaux** — et c'est le chapitre 34.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a de la persistance de session » | Le répartiteur renvoie sur le même serveur | **Modèle A** — la redondance ne protège pas les sessions |
| « Les sessions sont dans Redis » | Modèle B | **Le magasin est-il redondé ? Il n'est sur aucun schéma** |
| « On utilise des JWT » | Modèle C | **Quelle durée de vie ? Comment révoque-t-on ?** |
| « Les gens se font déconnecter » | Symptôme | **Tous en même temps, ou un tiers ?** La réponse désigne le modèle |

⚠️ **La dernière ligne est un excellent outil de diagnostic** : *tous en même temps* désigne le magasin partagé · *un tiers seulement* désigne un serveur redémarré avec des sessions locales.

---
