---
title: Chapitre 30 — Suivre une authentification
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

> Le flux de dépendance le plus universel, et le moins représenté.

## 30.1 Trois questions à ne jamais confondre

**La distinction que presque personne ne fait, et qui structure tout le chapitre** :

| Question | Nom | Où elle se traite |
|---|---|---|
| **Qui es-tu ?** | Authentification | Annuaire, fournisseur d'identité, mandataire |
| **As-tu le droit de faire ceci ?** | Autorisation | **L'application, presque toujours** |
| **Qu'as-tu fait ?** | Traçabilité | L'application, et les journaux |

⚠️ **Confondre les deux premières est une erreur de lecture courante sur ce sujet.** Un mandataire qui authentifie sait *qui* entre ; il ne sait pas *ce que cette personne a le droit de faire*. **L'autorisation reste dans l'application** — et c'est pourquoi une faille d'autorisation n'est pas rattrapée par un mandataire, si bien configuré soit-il.

## 30.2 Où l'on prouve son identité, et combien de fois

**Le constat** : dans une journée ordinaire, un utilisateur s'authentifie bien plus souvent qu'il ne le croit — et la plupart de ces authentifications sont invisibles.

| Moment | Contre quoi | Visible ? |
|---|---|---|
| Ouverture de session du poste | Annuaire | ✅ |
| Montage des lecteurs réseau | Annuaire | ❌ |
| Ouverture de la messagerie | Annuaire ou service en ligne | ❌ |
| Accès à une application interne | Annuaire, via le mandataire | ❌ |
| Accès à un service en ligne | Fédération ou compte propre | Selon |
| Appel d'un serveur vers un autre | Certificat ou secret — §33 | ❌ |
| Accès d'un administrateur | Second facteur, compte distinct | ✅ |

**Dans cet exemple, six des sept authentifications sont invisibles pour l'utilisateur**, et toutes dépendent d'un composant que le schéma ne montre pas.

## 30.3 Ce qui se passe quand l'annuaire tombe

🖼 **SCHÉMA 30.1 — La cascade**

```
   T+0        L'annuaire cesse de répondre
              │
   T+0        Les sessions ouvertes CONTINUENT     ← rien ne se voit
              │
   T+minutes  Toute nouvelle authentification échoue
              │  · nouveaux accès aux partages
              │  · connexions applicatives
              │
   T+heures   Les jetons expirent, les sessions tombent une à une
              │
   Au premier Un utilisateur ne peut plus ouvrir sa session.
   redémarrage Il est bloqué devant son poste.
```


⚠️ **La cascade est progressive, et c'est ce qui la rend difficile à diagnostiquer.** Pendant les premières minutes, la majorité des utilisateurs ne constate rien. Les signalements arrivent par vagues, sur des symptômes différents, et rien ne les relie apparemment.

🔥 **SCÉNARIO — l'annuaire répond, personne ne peut se connecter**

| Question | Réponse |
|---|---|
| Symptôme | Les contrôleurs répondent aux requêtes de test. Les ouvertures de session échouent |
| Hypothèse naïve | « L'annuaire est en panne » |
| Dépendance réelle | **La résolution de noms** : le poste ne trouve plus ses contrôleurs — §16.2 |
| Ce que le schéma aurait dû montrer | Que l'annuaire se localise par la résolution de noms |
| Comment le reconnaître | Interroger le contrôleur **par son adresse** fonctionne · par son nom, non |

⚠️ **C'est le chemin de diagnostic le plus difficile du cours** : deux composants invisibles, et l'un dépend de l'autre.

## 30.4 Les trois modèles d'authentification

```
  A — CHAQUE APPLICATION AUTHENTIFIE
      [ app 1 : ses comptes ]  [ app 2 : ses comptes ]  [ app 3 : ... ]
      → aucune dépendance commune : une panne n'affecte qu'une application
      → autant de bases d'identités que d'applications
      → un départ suppose N suppressions, et il y en aura N-2

  B — AUTHENTIFICATION CENTRALISÉE
      [ app 1 ] [ app 2 ] [ app 3 ] ──► [ annuaire ]
      → un départ = une action · une politique commune
      → ⚠️ UNE DÉPENDANCE UNIVERSELLE
      → une compromission de l'annuaire donne tout

  C — FÉDÉRATION
      [ app ] ──► [ fournisseur d'identité ] ──► [ annuaire interne ]
                          (souvent externe)
      → fonctionne pour des applications hors de votre réseau
      → ⚠️ la dépendance sort de l'organisation
      → si le fournisseur est indisponible, VOUS ne pouvez rien faire
```


| Modèle | Départ d'un salarié | Panne du composant central | Maîtrise |
|---|---|---|---|
| **A** | N actions, et des oublis | Une application seulement | Complète |
| **B** | Une action | **Tout est bloqué** | Complète |
| **C** | Une action | **Tout est bloqué, et vous n'y pouvez rien** | Partielle |

⚠️ **Le modèle C déplace la dépendance hors de l'organisation.** C'est un arbitrage classique : on gagne en simplicité et en fonctionnalités, on perd la maîtrise de la disponibilité. **Principe du coût.**

## 30.5 Le second facteur, et où il se place

| Placement | Ce qu'il protège | Ce qu'il ne protège pas |
|---|---|---|
| À l'ouverture de session du poste | L'accès au poste | Ce qui est déjà ouvert |
| Au mandataire inverse | Les accès **externes** | **Les accès internes directs** — §29.3 |
| Dans l'application | Cette application | Les autres |
| À l'accès distant | L'entrée sur le réseau | Ce qui se passe ensuite |

⚠️ **La deuxième ligne est une erreur de conception courante sur ce sujet** : placer le second facteur au mandataire, et croire l'application protégée. **Un poste interne l'atteint sans passer par là.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a du SSO » | Une authentification unique existe | **Contre quoi ? Pour quelles applications ? Et les autres ?** |
| « C'est fédéré » | Modèle C | **Le fournisseur est-il externe ? Que fait-on s'il tombe ?** |
| « On a mis du MFA » | Un second facteur | **Placé où ?** Il ne protège que ce qui passe par lui |
| « Il a les droits » | Confusion authentification / autorisation | **Qui les lui a donnés, et où sont-ils vérifiés ?** |

⚖️ **CONTRAINTE ET COÛT — l'authentification centralisée**

| Résout | Coûte |
|---|---|
| Une identité unique, des droits gérés en un point | **Une dépendance universelle** |
| Retirer un accès partout en une action | Une panne qui bloque tout progressivement |
| Appliquer une politique commune | Une compromission qui donne accès à tout |

---
