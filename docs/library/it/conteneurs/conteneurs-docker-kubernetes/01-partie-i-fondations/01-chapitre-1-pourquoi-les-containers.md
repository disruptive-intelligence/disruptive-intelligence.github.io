---
title: Chapitre 1 — Pourquoi les containers
source: IT/08 Conteneurs & automatisation/Conteneurs — Docker & Kubernetes.md
note: Conteneurs — Docker & Kubernetes
up:
- - Conteneurs — Docker & Kubernetes
  - ../index.md
- - Partie I — Fondations
  - index.md
---

du serveur physique au container

## Le minimum à savoir

### Le problème de départ

Imagine que tu développes une application web. Elle a besoin de Python 3.12, de PostgreSQL 15, de Redis, et de quelques bibliothèques spécifiques. Ça fonctionne sur ton ordinateur. Mais quand tu la déploies sur le serveur de production, rien ne marche : le serveur a Python 3.9, une version différente de PostgreSQL, et il manque des bibliothèques.

C’est le problème classique du **“ça marche sur ma machine”**. Les containers le résolvent.

### L’évolution en 3 étapes

Pour comprendre les containers, il faut comprendre ce qui existait avant et pourquoi chaque étape a été inventée.

**Étape 1 — Le serveur physique (bare metal)**

Au début, chaque application tournait sur un serveur physique dédié. Un serveur = une application. Le problème : si l’application n’utilise que 10% du CPU, les 90% restants sont gaspillés. Et si tu as 20 applications, tu as besoin de 20 serveurs physiques — coûteux, lents à déployer, difficiles à maintenir.

**Étape 2 — La virtualisation (machines virtuelles)**

La virtualisation permet de faire tourner **plusieurs systèmes d’exploitation** sur un seul serveur physique. Chaque machine virtuelle (VM) a son propre OS complet, son propre kernel, ses propres ressources. Un hyperviseur (VMware, Hyper-V, KVM) gère le partage du matériel.

C’est un progrès énorme : un serveur physique peut héberger 10-20 VMs. Mais chaque VM embarque un OS complet (plusieurs Go), consomme de la RAM juste pour son kernel, et met 30 secondes à 2 minutes pour démarrer.

**Étape 3 — Les containers**

Les containers sont une forme d’isolation **sans OS complet**. Au lieu d’embarquer un kernel entier, le container **partage le kernel de la machine hôte** et n’embarque que l’application et ses dépendances.

Résultat :

- Une image container fait typiquement **50-200 Mo** au lieu de **5-20 Go** pour une VM
- Un container démarre en **quelques secondes** au lieu de minutes
- Tu peux faire tourner **des dizaines de containers** là où tu mettrais 5-10 VMs
- L’application se comporte **exactement de la même façon** partout (sur ton laptop, sur le serveur de test, en production)

### Container vs VM : la comparaison visuelle

```
  MACHINE VIRTUELLE                    CONTAINER
┌───────────────────────┐       ┌───────────────────────┐
│  App A  │  App B      │       │  App A  │  App B      │
│─────────│─────────────│       │─────────│─────────────│
│  Libs A │  Libs B     │       │  Libs A │  Libs B     │
│─────────│─────────────│       │─────────│─────────────│
│  OS     │  OS         │       │    Container Engine   │
│ complet │ complet     │       │     (Docker)          │
│─────────│─────────────│       │───────────────────────│
│      Hyperviseur      │       │    OS hôte (1 seul)   │
│───────────────────────│       │───────────────────────│
│     Matériel (CPU,    │       │     Matériel (CPU,    │
│     RAM, disque)      │       │     RAM, disque)      │
└───────────────────────┘       └───────────────────────┘
```


La différence fondamentale : **la VM virtualise le matériel** (chaque VM croit avoir son propre ordinateur), **le container virtualise l’OS** (chaque container croit avoir son propre système, mais ils partagent le même kernel).

> **À retenir pour un entretien :** “Un container partage le kernel de la machine hôte et n’embarque que l’application et ses dépendances. C’est plus léger et plus rapide qu’une VM, mais l’isolation est moins forte car le kernel est partagé.”

### Les 4 avantages concrets des containers

1. **Portabilité** : le container fonctionne partout de la même façon — sur ton laptop, sur le serveur de test, en production, chez un collègue. Plus jamais “ça marche sur ma machine”.
1. **Reproductibilité** : l’image container décrit exactement ce qui est installé. Pas de configuration manuelle, pas de “j’ai oublié d’installer cette bibliothèque”. Si l’image est la même, le résultat est le même.
1. **Isolation** : chaque container a son propre filesystem, ses propres processus, son propre réseau. L’application A dans son container ne peut pas interférer avec l’application B dans un autre container.
1. **Densité** : un serveur qui fait tourner 5 VMs peut faire tourner 50 containers. Les containers consomment beaucoup moins de ressources.

### Ce que les containers ne sont PAS

C’est important de le dire dès le départ :

- **Les containers ne sont PAS des VMs.** L’isolation est moins forte (kernel partagé). Une vulnérabilité dans le kernel affecte tous les containers de la machine.
- **Les containers ne sont PAS magiquement sécurisés.** Un container mal configuré (exécuté en root, avec trop de permissions, avec des secrets dans l’image) est une vulnérabilité.
- **Les containers ne remplacent PAS la virtualisation dans tous les cas.** Pour une isolation forte (multi-tenant, environnements hostiles), une VM reste plus sûre.
- **Les containers ne simplifient PAS tout.** Ils ajoutent une couche de complexité (réseau, stockage, orchestration). Le bénéfice vient quand cette complexité est maîtrisée.

> **📋 CONTAINER — Épisode 1**
> 
> Sami rejoint l’équipe MedFlow. L’application tourne sur 3 VMs : une pour Django (le serveur web), une pour PostgreSQL (la base de données), une pour Redis + Celery (le cache et les tâches en arrière-plan). Chaque VM est configurée manuellement par un administrateur système. Le dernier déploiement a cassé la production : la version de Python sur la VM de staging (3.11) n’était pas la même qu’en production (3.9). Le CTO demande à Sami d’accompagner la migration vers des containers. Objectif : “que l’application se comporte exactement pareil partout.”

## Très utile en pratique

### Les cas d’usage concrets

**Développement local reproductible :** au lieu d’installer PostgreSQL, Redis, Elasticsearch sur ton laptop (et de gérer les versions, les conflits, le nettoyage), tu lances des containers. Un `docker compose up` et tout ton environnement de développement est prêt. Un `docker compose down` et tout disparaît proprement.

**CI/CD (intégration et déploiement continus) :** les pipelines de test et de déploiement utilisent des containers pour garantir un environnement identique à chaque exécution. Les tests passent dans un container → on construit l’image de production → on la déploie.

**Microservices :** au lieu d’une grosse application monolithique, on découpe en services indépendants, chacun dans son container. Chaque service peut être développé, déployé et mis à l’échelle indépendamment.

**Labs de sécurité et pentest :** les containers sont parfaits pour lancer rapidement des environnements d’entraînement (DVWA, Juice Shop, Metasploitable) sans polluer ta machine.

### Container vs VM : le tableau comparatif

|Critère    |Machine Virtuelle                       |Container                 |
|-----------|----------------------------------------|--------------------------|
|Isolation  |Forte (kernel séparé)                   |Moyenne (kernel partagé)  |
|Taille     |5-20 Go                                 |50-500 Mo                 |
|Démarrage  |30s - 2 min                             |1-5 secondes              |
|Densité    |5-20 par serveur                        |50-200 par serveur        |
|OS embarqué|OS complet                              |Juste les libs nécessaires|
|Portabilité|Moyenne (format VMware, Hyper-V…)       |Excellente (standard OCI) |
|Performance|Légère perte (virtualisation matérielle)|Quasi native              |
|Sécurité   |Plus forte par défaut                   |Nécessite du hardening    |

## Bonus

### Un peu d’histoire

Les containers ne sont pas une invention récente. Les premières formes d’isolation de processus datent de `chroot` (1979) sous Unix. Puis sont venus les FreeBSD Jails (2000), Solaris Zones (2004), et LXC (Linux Containers, 2008). **Docker** (2013) a démocratisé le concept en le rendant simple d’utilisation avec un format d’image standardisé et un écosystème d’outils. Docker n’a pas inventé les containers — il les a rendus accessibles.

Aujourd’hui, le standard est **OCI** (Open Container Initiative) — un format ouvert pour les images et les runtimes de containers, indépendant de Docker. Kubernetes utilise `containerd` (un runtime OCI) plutôt que Docker directement.

### Le standard OCI en bref

L’OCI définit deux choses : un format d’image (comment une image est construite et distribuée) et un runtime (comment un container est exécuté). Docker, Podman, containerd — tous respectent le standard OCI. Une image construite avec Docker fonctionne avec Podman et vice versa.

## ❌ Erreur classique

```
# Croire que container = VM légère
→ Non. Le modèle d'isolation est fondamentalement différent (kernel partagé vs séparé).

# Croire que les containers sont sécurisés par défaut
→ Non. Un container en root avec le Docker socket monté est MOINS sécurisé qu'une VM.

# Vouloir mettre "tout en containers" sans réflexion
→ Une base de données de production avec de fortes contraintes de performance et de
  persistance n'est pas toujours le meilleur candidat pour la containerisation.
```


## ✅ Tu sais maintenant…

- La différence entre serveur physique, VM et container
- Pourquoi les containers existent (portabilité, reproductibilité, isolation, densité)
- Que les containers partagent le kernel de la machine hôte (conséquence en sécurité)
- Ce que les containers ne sont PAS (pas des VMs, pas magiquement sécurisés)

## 💬 Questions d’entretien typiques

- **Quelle est la différence entre un container et une machine virtuelle ?** → Le container partage le kernel de l’hôte et isole au niveau de l’OS (namespaces), la VM virtualise le matériel avec un kernel séparé. Le container est plus léger et rapide, la VM offre une isolation plus forte.
- **Quels sont les avantages des containers ?** → Portabilité, reproductibilité, isolation des dépendances, densité (plus de containers que de VMs par serveur), démarrage rapide.
- **Les containers sont-ils sécurisés ?** → Pas par défaut. L’isolation repose sur des mécanismes logiciels (namespaces, cgroups), pas sur une séparation matérielle. Un container mal configuré (root, Docker socket monté) peut être moins sécurisé qu’une VM.

-----
