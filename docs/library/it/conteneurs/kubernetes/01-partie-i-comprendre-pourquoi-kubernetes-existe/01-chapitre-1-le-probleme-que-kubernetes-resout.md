---
title: Chapitre 1 — Le problème que Kubernetes résout
source: IT/08 Conteneurs & automatisation/Kubernetes.md
note: Kubernetes
up:
- - Kubernetes
  - ../index.md
- - PARTIE I — Comprendre pourquoi Kubernetes existe
  - index.md
---

## Le minimum à savoir

### Pourquoi commencer par « le problème » ?

Beaucoup de gens apprennent Kubernetes en tapant des commandes qu'ils ne comprennent pas. Résultat : ils savent *faire* des choses, mais paniquent dès que ça casse. On va éviter ça. **Kubernetes est une réponse à des problèmes très concrets.** Si tu comprends les problèmes, les solutions deviennent évidentes.

### L'histoire d'un serveur unique

Imagine que tu administres **une application web** sur **un seul serveur Linux**. Au début, tout va bien. Puis les ennuis arrivent :

- **L'appli plante à 3 h du matin.** Personne ne la redémarre avant le lendemain. Downtime.
- **Le trafic explose un jour de pic.** Ton serveur unique sature. Tu ne peux pas « ajouter de la puissance » instantanément.
- **Tu dois mettre à jour l'appli.** Tu coupes tout, tu déploies, tu pries. Si ça casse, tu reviens en arrière à la main, sous pression.
- **Le serveur lui-même tombe.** Disque mort, coupure réseau. Toute l'appli est par terre.
- **« Ça marche sur ma machine ».** Le développeur jure que ça marche chez lui. Chez toi, non. Versions différentes, dépendances différentes.

Chacun de ces problèmes, un admin Linux le résout **à la main** : un script de redémarrage, un second serveur monté en urgence, un load balancer configuré manuellement, une procédure de rollback notée dans un coin. Ça marche… tant que tu as **peu** de serveurs et **peu** d'applis.

### Ce qui casse à grande échelle

Maintenant imagine **50 serveurs** et **30 applications**. Les corvées manuelles deviennent **ingérables** :

- Qui surveille que chaque appli tourne, partout, tout le temps ?
- Qui décide **quel serveur** héberge **quelle appli** pour équilibrer la charge ?
- Qui recrée automatiquement une appli quand son serveur meurt ?
- Qui gère les mises à jour progressives sans tout couper ?

C'est **exactement** ce travail que Kubernetes automatise. On appelle ça l'**orchestration de conteneurs**.

### La définition simple

> **Kubernetes est un système qui fait tourner tes applications (en conteneurs) sur un ensemble de machines, et qui s'occupe automatiquement de les démarrer, les redémarrer, les répartir, les mettre à l'échelle et les mettre à jour — pour que tu décrives ce que tu veux au lieu de tout faire à la main.**

On l'écrit souvent **« K8s »** (K, puis 8 lettres « ubernete », puis s).

## Très utile en pratique

Voici la traduction directe des corvées d'admin en **promesses de Kubernetes** :

| Corvée d'admin classique | Ce que Kubernetes fait à ta place |
|--------------------------|-----------------------------------|
| Redémarrer une appli plantée | **Self-healing** : il recrée automatiquement ce qui meurt |
| Ajouter des serveurs en cas de pic | **Scaling** : il lance plus de copies à la demande |
| Répartir les applis sur les serveurs | **Scheduling** : il place les charges là où il y a de la place |
| Mettre à jour sans coupure | **Rolling update** : il remplace progressivement les anciennes versions |
| Revenir en arrière après un bug | **Rollback** : il restaure la version précédente en une commande |
| Donner une adresse stable à une appli mouvante | **Services** : une IP/nom stable malgré les Pods qui changent |

> **À retenir :** Kubernetes ne « fait pas de magie ». Il automatise des tâches d'**admin système** et de **réseau** que tu pourrais faire à la main — mais à une échelle et avec une fiabilité impossibles manuellement.

## Application admin / cyber

- **Côté admin système :** Kubernetes remplace une pile de scripts maison (systemd pour relancer, scripts de déploiement, configuration manuelle de load balancers). Ce que tu sais déjà en Linux n'est **pas perdu** : c'est le socle sur lequel K8s s'appuie.
- **Côté SOC / cyber :** un cluster Kubernetes, c'est **beaucoup de machines et d'applications pilotées par une seule API**. C'est une formidable centralisation… donc une **cible de choix**. Comprendre *pourquoi* le cluster existe, c'est comprendre *ce qu'un attaquant cherche à contrôler* : l'API qui commande tout.

🛡️ **Réflexe sécurité (à garder en tête pour tout le cours) :** plus un système automatise et centralise, plus **le point de contrôle central** (ici, l'API de Kubernetes) devient précieux à protéger. On y reviendra en détail (Ch. 6, 24, 25).

## ❌ Erreur classique

> **Croire que Kubernetes « remplace » Linux, le réseau ou Docker.**

C'est faux, et c'est un contresens qui handicape les débutants. Kubernetes **s'appuie** sur Linux (processus, namespaces noyau, réseau), sur les **conteneurs** (Docker/containerd) et sur le **réseau** (IP, DNS, ports). Ce sont tes acquis d'admin qui rendent Kubernetes compréhensible, pas l'inverse. Kubernetes ajoute une **couche d'orchestration** au-dessus — il ne supprime rien en dessous.

## Exercices

**Guidé :** Sur une feuille (ou un fichier texte), liste **5 tâches** que tu fais ou ferais à la main pour maintenir une appli en ligne sur un serveur Linux (ex. : « relancer le service s'il plante »). En face de chacune, écris la promesse Kubernetes correspondante en t'aidant du tableau plus haut. Objectif : **traduire ton métier actuel en vocabulaire K8s**.

**Autonome :** Décris en 5 lignes une situation réelle (vécue ou imaginée) où **un seul serveur** a posé problème (panne, pic de charge, mise à jour ratée). Puis explique, en une phrase par point, **comment Kubernetes** aurait changé l'issue. Pas de commande ici : c'est un exercice de **modèle mental**.

**Défi :** En une demi-page, explique à un collègue **non technique** ce qu'est Kubernetes, **sans jamais utiliser** les mots « Pod », « conteneur » ou « cluster ». Utilise uniquement des analogies (un chef d'orchestre, un gérant d'immeuble, un service de livraison qui se réorganise tout seul…). Si tu y arrives, c'est que tu as **vraiment** compris le « pourquoi ».

## ✅ Tu sais maintenant…

- **Pourquoi** Kubernetes existe : automatiser des corvées d'admin ingérables à grande échelle.
- Les grandes promesses : **self-healing, scaling, scheduling, rolling update, rollback, adresses stables**.
- Que Kubernetes **s'appuie** sur Linux, le réseau et les conteneurs — il ne les remplace pas.
- Que la **centralisation** apportée par K8s en fait une cible de sécurité majeure (point de contrôle = l'API).
- Le sens du sigle **K8s**.

---
