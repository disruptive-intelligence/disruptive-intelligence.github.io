---
title: 'Chapitre 3 — Docker vs Kubernetes : la bascule'
source: IT/08 Conteneurs & automatisation/Conteneurs/Kubernetes.md
note: Kubernetes
up:
- - Kubernetes
  - ../index.md
- - PARTIE I — Comprendre pourquoi Kubernetes existe
  - index.md
---

## Le minimum à savoir

### La confusion à dissiper

« Docker ou Kubernetes ? » est une **fausse question**, comme « marteau ou maison ? ». Ils ne jouent pas dans la même catégorie :

- **Docker** (ou un autre moteur de conteneurs) fait tourner **un conteneur** sur **une machine**.
- **Kubernetes** **orchestre beaucoup de conteneurs** sur **beaucoup de machines**.

Kubernetes ne **remplace** pas Docker : il **l'utilise** (ou utilise un moteur équivalent) pour exécuter les conteneurs, et ajoute par-dessus toute la logique de coordination vue au Chapitre 1.

### La notion de runtime de conteneurs

Pour exécuter un conteneur, il faut un **moteur** (un *container runtime*). Docker en est un. Mais Kubernetes ne parle pas directement à « Docker » : il parle à un runtime standardisé, le plus souvent **containerd** (qui était d'ailleurs déjà le cœur de Docker).

> **À retenir sans te noyer dans les détails :** quand un Pod démarre sur un node, c'est un **runtime de conteneurs** (containerd, en général) qui lance réellement le ou les conteneurs. Kubernetes **commande**, le runtime **exécute**.

Voici la **chaîne complète**, du haut (ta commande) vers le bas (le conteneur qui tourne) — garde ce schéma en tête, il prépare directement la Partie II :

```text
   kubectl / API Kubernetes      ← tu déclares l'état désiré
            ↓
   kubelet (sur le node)         ← l'agent qui reçoit l'ordre et le réalise
            ↓
   container runtime (containerd) ← le moteur qui sait lancer un conteneur
            ↓
   conteneur(s) dans un Pod      ← ce qui tourne réellement
```


Tu as peut-être entendu « Kubernetes a abandonné Docker ». Nuance importante : Kubernetes a arrêté d'utiliser une couche d'intégration spécifique à Docker (*dockershim*), **pas** les images. **Tes images Docker fonctionnent toujours** — elles respectent un standard commun (**OCI**, *Open Container Initiative*).

### Même besoin, deux réponses

| Besoin | Réponse **Docker** (1 machine) | Réponse **Kubernetes** (cluster) |
|--------|-------------------------------|----------------------------------|
| Lancer une appli | `docker run` | Décrire un Pod/Deployment, `kubectl apply` |
| Relancer si ça plante | À ta charge (script, `--restart`) | **Automatique** (réconciliation) |
| 3 copies pour tenir la charge | 3 `docker run` à la main | `replicas: 3`, géré tout seul |
| Mettre à jour sans coupure | À ta charge | **Rolling update** intégré |
| Adresse stable vers l'appli | À ta charge | **Service** intégré |
| Répartir sur plusieurs machines | Impossible avec Docker seul | **C'est précisément son rôle** |

## Très utile en pratique

Tu n'as **rien à taper** dans ce chapitre — c'est un chapitre de **cadrage mental**. Mais retiens cette phrase qui te resservira souvent :

> **Docker, c'est « lance ce conteneur, ici, maintenant ». Kubernetes, c'est « voilà ce que je veux qui tourne en permanence, débrouille-toi pour que ce soit toujours vrai, partout ».**

La première est une **instruction ponctuelle**. La seconde est un **état désiré maintenu dans le temps** — exactement la boucle de réconciliation du préambule.

## Application admin / cyber

- **Côté admin :** en lab, Minikube utilisera souvent Docker **comme support** (le « driver ») pour faire tourner ton mini-cluster. C'est normal que les deux coexistent : Docker fournit la machinerie, Kubernetes l'orchestration.
- **Côté SOC / cyber :** la bascule Docker → Kubernetes **change l'échelle de la surface d'attaque**. Avec Docker, tu raisonnes sur **une machine**. Avec Kubernetes, tu raisonnes sur **un cluster entier piloté par une API** : plus de composants, plus de communications réseau internes, plus d'identités (utilisateurs **et** Pods). Le périmètre à surveiller **explose**.

🛡️ **Réflexe sécurité :** chaque fois que tu passes « d'une machine » à « un cluster », demande-toi *combien de nouvelles portes cela ouvre* : l'API, le réseau inter-Pods, les identités des Pods, les secrets partagés. Le cours va parcourir ces portes une à une.

## ❌ Erreur classique

> **Penser qu'il faut « choisir » entre Docker et Kubernetes, ou que savoir Docker dispense d'apprendre Kubernetes.**

Ce sont des outils **complémentaires** à des niveaux différents. Savoir lancer un conteneur avec Docker **ne** t'apprend **pas** à le maintenir en vie, le répliquer, l'exposer et le mettre à jour sur un parc de machines : ça, c'est le métier de Kubernetes. Inversement, Kubernetes a **besoin** d'un moteur de conteneurs en dessous. Les deux cohabitent.

## Exercices

**Guidé :** Reprends le tableau « Même besoin, deux réponses ». Pour chaque ligne, **dis à voix haute** (ou écris) **pourquoi** la réponse Docker devient ingérable à 50 machines, et pourquoi celle de Kubernetes passe à l'échelle. Tu relies ainsi ce chapitre au Chapitre 1.

**Autonome :** En 5 phrases, explique la différence entre « **lancer** un conteneur » et « **maintenir** un état désiré ». Utilise un exemple concret : une appli qui doit **toujours** tourner en 3 exemplaires, même si un serveur tombe à 4 h du matin.

**Défi :** On dit souvent « Kubernetes a supprimé le support de Docker ». En t'appuyant sur ce chapitre, explique en quelques lignes **pourquoi cette phrase est trompeuse**, et ce qui a réellement changé (indice : *dockershim* vs **images OCI**). Le but : savoir **nuancer** une affirmation qu'on entend partout.

## ✅ Tu sais maintenant…

- Que Docker et Kubernetes **ne sont pas concurrents** : l'un exécute un conteneur sur une machine, l'autre orchestre beaucoup de conteneurs sur beaucoup de machines.
- Ce qu'est un **runtime de conteneurs** (souvent **containerd**) et le rôle « Kubernetes commande, le runtime exécute ».
- Pourquoi « K8s a abandonné Docker » est une phrase **à nuancer** (dockershim ≠ images, qui restent compatibles via OCI).
- Que la bascule vers le cluster **multiplie la surface d'attaque** (API, réseau interne, identités, secrets).

---
