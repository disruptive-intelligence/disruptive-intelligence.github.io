---
title: Chapitre 13 — Le répartiteur de charge
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

## 13.1 À quoi ça sert

Distribuer les demandes entre plusieurs exemplaires d'un même rôle, et **retirer automatiquement ceux qui ne répondent plus**.

**Pourquoi ça existe.** Dès qu'on veut qu'une panne d'un serveur ne soit pas visible, il faut quelqu'un qui sache que ce serveur ne répond plus, et qui envoie ailleurs. C'est ce que fait le contrôle de santé — et c'est la vraie fonction du répartiteur, davantage que la répartition elle-même.

## 13.2 Le contrôle de santé : ce qui décide de tout

```
   Toutes les N secondes, le répartiteur interroge chaque membre :

   ①  TEST DE CONNEXION      le port répond-il ?
       → détecte une machine éteinte
       → ne détecte PAS une application bloquée

   ②  TEST APPLICATIF        une page de test répond-elle correctement ?
       → détecte une application en erreur
       → ne détecte PAS une base inaccessible derrière

   ③  TEST DE BOUT EN BOUT   une requête qui traverse toute la chaîne
       → détecte tout
       → coûte plus cher, et peut faire sortir TOUS les membres
         si la panne est en aval
```


⚠️ **Le troisième cas produit un incident classique** : la base tombe, le test de bout en bout échoue sur tous les serveurs, le répartiteur les retire tous, et **le service ne répond plus du tout** — alors qu'il aurait pu servir des pages d'erreur. **Un contrôle de santé trop profond transforme une dégradation en arrêt.**

## 13.3 Le paradoxe du composant de disponibilité

> **Il crée un point de rupture en résolvant un point de rupture.**

C'est pourquoi il est presque systématiquement redondé — et cette redondance pose exactement les mêmes questions que celle du pare-feu, §10.5.

## 13.4 La session, et pourquoi elle limite tout

**Répartir des demandes est simple. Répartir des demandes qui appartiennent à une session ne l'est pas.**

| Situation | Ce que le répartiteur doit faire |
|---|---|
| L'application ne garde aucun état | Rien de particulier — n'importe quel membre convient |
| L'application garde la session localement | **Renvoyer l'utilisateur toujours sur le même membre** |
| La session est partagée | N'importe quel membre convient |

⚠️ **Le deuxième cas est très répandu, et il annule une partie du bénéfice.** Si le répartiteur doit renvoyer chaque utilisateur sur « son » serveur, alors la panne de ce serveur **déconnecte ses utilisateurs** — la redondance protège les nouveaux venus, pas ceux qui étaient en cours de travail. C'est le §31.2.

## 13.5 Trois architectures de répartition

```
  A — RÉPARTITION PAR LA RÉSOLUTION DE NOMS
      Le nom renvoie plusieurs adresses, le client en choisit une.
      → aucun équipement · aucun coût
      → aucun contrôle de santé : un serveur mort reçoit quand même
      → les caches retardent tout changement

  B — RÉPARTITEUR DÉDIÉ
      [ répartiteur ] ──► [ web 1 ] [ web 2 ] [ web 3 ]
      → contrôle de santé · retrait automatique
      → un composant de plus, à redonder

  C — RÉPARTITION INTÉGRÉE À LA PLATEFORME
      L'orchestrateur ou le fournisseur cloud s'en charge.
      → rien à exploiter · rien à dessiner
      → une dépendance à la plateforme · une visibilité réduite
```


⚠️ **Le mode A explique un incident fréquent** : trois adresses derrière un nom, un serveur tombe, **et un tiers des utilisateurs obtient une erreur** — parce que rien ne retire l'adresse morte. Sur un schéma, la répartition paraît identique dans les trois modes.

## 13.6 Ce qu'il fait à la donnée

Il l'achemine. Selon son niveau, il lit le contenu — auquel cas il fait aussi office de mandataire inverse, et les deux composants se confondent souvent dans un même équipement — §12.4.

## 13.7 S'il disparaît

🔥 **SCÉNARIO — tout tombe alors que tous les serveurs vont bien**

| Question | Réponse |
|---|---|
| Symptôme | Service inaccessible. Les trois serveurs web répondent normalement en direct |
| Hypothèse naïve | « Un problème applicatif » |
| Dépendance réelle | Le répartiteur — **le seul composant sur le chemin qui ne soit pas redondé** |
| Ce que le schéma aurait dû montrer | S'il est unique ou en paire |
| Concevoir différemment | Le redonder · ou prévoir un chemin de secours documenté vers un serveur direct |

**C'est le composant dont la panne est la plus contre-intuitive du cours** : il a été ajouté pour la disponibilité, et son absence arrête tout.

## 13.8 Sur un schéma

Juste avant un groupe de boîtes identiques. **La présence de trois serveurs web sans répartiteur dessiné est une question à poser** : soit il existe et n'est pas représenté, soit la répartition se fait par la résolution de noms — mode A, qui n'a pas les mêmes propriétés.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça passe par le load balancer » | Un répartiteur est sur le chemin | **Est-il redondé ?** Quel type de contrôle de santé ? |
| « On a de la persistance de session » | L'utilisateur est renvoyé sur le même serveur | **Alors la redondance ne protège pas les sessions en cours** |
| « On a mis deux nœuds » | Deux membres derrière le répartiteur | Sur des hôtes différents ? — *principe de preuve* |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Continuer malgré la panne d'un membre | **Un composant à redonder lui-même** |
| Absorber une charge croissante | Un contrôle de santé à régler — trop profond, il aggrave |
| Retirer un serveur pour maintenance sans coupure | Une gestion de session à traiter — §31 |

---
