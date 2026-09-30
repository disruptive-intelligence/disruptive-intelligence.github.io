---
title: Chapitre 18 — Le serveur web
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE III — Les serveurs et l'exécution
  - index.md
---

## 18.1 À quoi ça sert

Recevoir une demande venue d'un navigateur, servir ce qui est statique, et transmettre le reste à ce qui sait le traiter.

**Pourquoi ça existe comme couche séparée.** Servir un fichier et exécuter une logique métier n'ont ni les mêmes contraintes, ni les mêmes cycles de mise à jour, ni les mêmes profils de charge. Les séparer permet de redonder l'un sans redonder l'autre — et c'est exactement l'arbitrage du schéma 1.1.

## 18.2 Ce qu'il fait à la donnée

Il la met en forme et la transporte.

⚠️ **Une précision qui compte** : un serveur web n'est pas *par nature* dépourvu d'état. **L'absence d'état est une décision de conception**, prise précisément pour le rendre interchangeable. Un serveur web qui conserve des sessions localement, des fichiers téléversés ou un cache applicatif **a un état** — et il n'est alors plus interchangeable, quelle que soit la façon dont le schéma le représente. C'est le §31.2.

## 18.3 Trois architectures de frontal

```
  A — TOUT SUR UNE MACHINE
      [ web + application + base ]
      → simple · un seul composant à exploiter
      → une mise à jour applicative impose d'arrêter le tout
      → convient à une petite application interne — §48.1

  B — WEB SÉPARÉ DE L'APPLICATION
      [ web ×2 ] ──► [ application ] ──► [ base ]
      → le frontal se redonde facilement, l'application non
      → deux cycles de mise à jour indépendants
      → la redondance s'arrête à mi-parcours — c'est un ARBITRAGE

  C — CONTENU STATIQUE SÉPARÉ
      [ diffusion de contenu ] ──► fichiers, images, scripts
      [ web ×2 ] ──────────────► pages dynamiques
      → le trafic le plus volumineux ne touche plus vos serveurs
      → une dépendance à un tiers · §38
```


**La contrainte qui fait passer de A à B** n'est pas la charge : c'est **le besoin de mettre à jour l'un sans arrêter l'autre**. Beaucoup d'architectures à trois niveaux existent pour cette raison, pas pour la performance.

## 18.4 S'il disparaît

Si un exemplaire tombe et qu'il y en a d'autres derrière un répartiteur : rien. S'il est seul : le service s'arrête.

🔥 **SCÉNARIO — un serveur sur trois tombe, et un tiers des utilisateurs est déconnecté**

| Question | Réponse |
|---|---|
| Symptôme | Un serveur redémarre. **Un tiers des utilisateurs perd sa session en cours** |
| Hypothèse naïve | « La répartition ne fonctionne pas » |
| Dépendance réelle | **Les sessions étaient locales au serveur** — §31.2 |
| Ce que le schéma aurait dû montrer | Où vivent les sessions |
| Concevoir différemment | Un magasin de sessions partagé, **avec le composant supplémentaire que cela suppose** |

⚠️ **La redondance fonctionnait parfaitement.** Elle protégeait les nouveaux venus, pas les utilisateurs en cours de travail. **C'est une distinction que le schéma ne peut pas exprimer.**

## 18.5 Sur un schéma

En haut du groupe applicatif, souvent en plusieurs exemplaires. **Trois boîtes identiques côte à côte désignent presque toujours des serveurs web.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le frontal » | Le serveur web, ou le mandataire inverse | **Les deux mots désignent souvent deux composants différents** |
| « C'est du stateless » | Le serveur ne garde pas de session | **Et le panier ? Les fichiers téléversés ? Le cache ?** |
| « On a scalé horizontalement » | Des exemplaires ont été ajoutés | Sur des hôtes différents ? Les sessions suivent-elles ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Servir des contenus à grande échelle | Une couche de plus dans le chemin |
| Se redonder facilement, s'il a été conçu sans état | **Un état qu'il faut alors mettre ailleurs** — §31 |
| Séparer les cycles de mise à jour | Deux composants à exploiter au lieu d'un |

⚠️ **La deuxième ligne est le vrai sujet, et elle illustre le principe du coût.** Un serveur web est redondable **lorsqu'il a été conçu pour ne rien garder**. Ce « rien » doit alors vivre ailleurs, et ce déplacement crée de nouvelles dépendances, souvent un composant supplémentaire. **L'absence d'état n'est pas une propriété magique du frontal : c'est un compromis qui déplace le problème.**

---
