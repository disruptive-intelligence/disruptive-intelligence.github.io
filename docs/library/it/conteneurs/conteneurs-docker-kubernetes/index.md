---
title: Conteneurs — Docker & Kubernetes
source: IT/08 Conteneurs & automatisation/Conteneurs/Conteneurs — Docker & Kubernetes.md
format: cours
revue: '2026-04-15'
revision: library/revision/conteneurs.md
---

*De zéro à la maîtrise — Comprendre, déployer et sécuriser*

-----

> **Prérequis :** Aucune expérience avec les containers n’est nécessaire. Le cours part de zéro.
> Une familiarité basique avec le terminal Linux (naviguer dans les dossiers, éditer un fichier, lancer des commandes) est un plus, mais les commandes essentielles sont rappelées au fil du cours.

-----

### Guide de lecture — Comment utiliser ce cours

Ce cours couvre un domaine vaste. Tu n’as **pas besoin de tout maîtriser d’un coup**. Voici comment naviguer selon ton objectif.

**Chaque chapitre est organisé en 3 niveaux :**

|Section                   |Niveau               |Objectif                                                                                 |
|--------------------------|---------------------|-----------------------------------------------------------------------------------------|
|**Le minimum à savoir**   |🟢 Essentiel          |Ce qu’il faut comprendre pour ne pas être perdu. Si tu ne retiens qu’une chose, c’est ça.|
|**Très utile en pratique**|🟡 Bon à connaître    |Ce qui te rend opérationnel. Indispensable si tu vas travailler avec le sujet.           |
|**Bonus**                 |🔴 Avancé / Production|Ce qui fait la différence en poste. Tu peux y revenir plus tard.                         |

**Si tu prépares un entretien ou vises un poste junior :**
Concentre-toi sur les sections “Le minimum à savoir” de chaque chapitre. Avec ça, tu pourras expliquer clairement ce qu’est un container, pourquoi on utilise Docker et Kubernetes, comment ça fonctionne, et quels sont les risques de sécurité. C’est ce qu’on attend d’un profil junior.

**Si tu veux devenir opérationnel (poste DevOps, SRE, SecOps) :**
Lis tout, y compris les sections “Très utile en pratique”. Les “Bonus” viendront naturellement avec l’expérience.

**Les chapitres indispensables pour un entretien :**
Ch.1-5 (comprendre Docker), Ch.6-8 (construire et composer), Ch.11-14 (comprendre Kubernetes), Ch.21 (sécurité — risques), Ch.23 et Ch.25 (sécurité runtime et K8s). Avec ces chapitres, tu as 80% de ce qu’on attend d’un junior.

#### Parcours recommandés

|Parcours                 |Chapitres                |Objectif                                         |
|-------------------------|-------------------------|-------------------------------------------------|
|**🎯 Entretien / Junior** |Ch.1-8, 11-15, 21, 23, 25|Comprendre, expliquer, être crédible en entretien|
|**🔧 Opérationnel**       |Tout jusqu’au Ch.26      |Être autonome sur un poste qui utilise Docker/K8s|
|**🚀 Avancé / Production**|Ch.27-30 + annexes       |Architectures avancées, scaling, gouvernance     |

Tu n’as pas besoin de tout lire linéairement. Commence par le parcours qui correspond à ton objectif actuel, et reviens aux chapitres suivants quand tu en as besoin.

-----

### Glossaire — Les mots à connaître

Reviens ici chaque fois qu’un terme te semble flou. Tous ces termes seront expliqués en détail dans le cours.

|Terme                |Définition simple                                                                               |
|---------------------|------------------------------------------------------------------------------------------------|
|**Container**        |Un environnement isolé et léger qui fait tourner une application avec toutes ses dépendances    |
|**Image**            |Le modèle (template) à partir duquel on crée un container — comme un plan de construction       |
|**Docker**           |L’outil le plus populaire pour créer et gérer des containers                                    |
|**Dockerfile**       |Le fichier texte qui décrit comment construire une image Docker, étape par étape                |
|**Registry**         |Un entrepôt d’images Docker (comme Docker Hub — le “GitHub des images”)                         |
|**Volume**           |Un espace de stockage persistant qui survit à la destruction du container                       |
|**Docker Compose**   |Un outil pour lancer plusieurs containers ensemble (ex : application + base de données)         |
|**Kubernetes (K8s)** |Un système qui gère automatiquement des containers sur plusieurs serveurs                       |
|**Pod**              |La plus petite unité dans Kubernetes — contient un ou plusieurs containers                      |
|**Deployment**       |Un objet K8s qui gère le déploiement et le scaling d’une application                            |
|**Service**          |Un objet K8s qui donne une adresse réseau stable à un groupe de Pods                            |
|**Namespace**        |Un espace de noms qui sépare logiquement les ressources dans un cluster K8s                     |
|**YAML**             |Le format de fichier utilisé pour décrire les configurations Docker Compose et Kubernetes       |
|**Cluster**          |L’ensemble des serveurs (nœuds) gérés par Kubernetes                                            |
|**Orchestration**    |La gestion automatique de containers sur plusieurs serveurs (scaling, self-healing, déploiement)|
|**Kernel**           |Le cœur du système d’exploitation — les containers partagent le kernel de la machine hôte       |
|**Namespace (Linux)**|Un mécanisme du kernel Linux qui isole les processus, le réseau, les fichiers d’un container    |
|**RBAC**             |Role-Based Access Control — le système de permissions dans Kubernetes                           |
|**Network Policy**   |Une règle de pare-feu entre les Pods dans Kubernetes                                            |

-----

### Le schéma mental

Avant de plonger, voici le fil conducteur. **Tout ce cours suit une progression logique :**

```
  POURQUOI ?         COMMENT ?           EN SÉCURITÉ ?
  Pourquoi les   →   Comment les      →  Comment les
  containers ?       utiliser ?           sécuriser ?
```


**Partie I-II** : Comprendre et utiliser Docker (construire, lancer, composer)
**Partie III** : Comprendre et utiliser Kubernetes (orchestrer, déployer)
**Partie IV** : Opérer au quotidien (CI/CD, monitoring, troubleshooting)
**Partie V** : Sécuriser (images, runtime, réseau, Kubernetes)
**Partie VI-VII** : Aller plus loin (architectures, synthèse)

-----

### Table des matières

**PARTIE I — FONDATIONS (Ch.1-5)**

1. [Pourquoi les containers : du serveur physique au container](01-partie-i-fondations/01-chapitre-1-pourquoi-les-containers.md)
1. [L’architecture container : comment ça marche sous le capot](01-partie-i-fondations/02-chapitre-2-larchitecture-container.md)
1. [Installer Docker et premiers containers](01-partie-i-fondations/03-chapitre-3-installer-docker-et-premiers-containers.md)
1. [Images Docker : comprendre, chercher, utiliser](01-partie-i-fondations/04-chapitre-4-images-docker-comprendre-chercher-utili.md)
1. [Réseau, volumes et persistance](01-partie-i-fondations/05-chapitre-5-reseau-volumes-et-persistance.md)

**PARTIE II — CONSTRUIRE ET COMPOSER (Ch.6-10)**

6. [Écrire un Dockerfile : de zéro à l’image](02-partie-ii-construire-et-composer/01-chapitre-6-ecrire-un-dockerfile-de-zero-a-limage.md)
7. [Optimiser et durcir ses images](02-partie-ii-construire-et-composer/02-chapitre-7-optimiser-et-durcir-ses-images.md)
8. [Docker Compose : orchestrer plusieurs containers](02-partie-ii-construire-et-composer/03-chapitre-8-docker-compose-orchestrer-plusieurs-con.md)
9. [Registries et gestion des images](02-partie-ii-construire-et-composer/04-chapitre-9-registries-et-gestion-des-images.md)
10. [Capstone : containeriser une application complète](02-partie-ii-construire-et-composer/05-chapitre-10-capstone-partie-ii.md)

**PARTIE III — KUBERNETES : LES FONDAMENTAUX (Ch.11-16)**

11. [Pourquoi Kubernetes : quand Docker ne suffit plus](03-partie-iii-kubernetes-les-fondamentaux/01-chapitre-11-pourquoi-kubernetes-quand-docker-ne-su.md)
12. [Architecture Kubernetes : les composants du cluster](03-partie-iii-kubernetes-les-fondamentaux/02-chapitre-12-architecture-kubernetes-les-composants.md)
13. [Les objets Kubernetes essentiels](03-partie-iii-kubernetes-les-fondamentaux/03-chapitre-13-les-objets-kubernetes-essentiels.md)
14. [Déployer sur Kubernetes : kubectl et les manifests](03-partie-iii-kubernetes-les-fondamentaux/04-chapitre-14-deployer-sur-kubernetes-kubectl-et-les.md)
15. [Stockage, Ingress et configuration avancée](03-partie-iii-kubernetes-les-fondamentaux/05-chapitre-15-stockage-ingress-et-configuration-avan.md)
16. [Capstone : déployer une application sur Kubernetes](03-partie-iii-kubernetes-les-fondamentaux/06-chapitre-16-capstone-partie-iii.md)

**PARTIE IV — OPÉRATIONS ET CYCLE DE VIE (Ch.17-20)**

17. [CI/CD et containers : du code au déploiement](04-partie-iv-operations-et-cycle-de-vie/01-chapitre-17-ci-cd-et-containers-du-code-au-deploie.md)
18. [Monitoring, logs et observabilité](04-partie-iv-operations-et-cycle-de-vie/02-chapitre-18-monitoring-logs-et-observabilite.md)
19. [Troubleshooting containers et Kubernetes](04-partie-iv-operations-et-cycle-de-vie/03-chapitre-19-troubleshooting-containers-et-kubernet.md)
20. [Capstone : pipeline CI/CD et monitoring](04-partie-iv-operations-et-cycle-de-vie/03-chapitre-19-troubleshooting-containers-et-kubernet.md#chapitre-20-capstone-partie-iv-pipeline-cicd-et-monitoring)

**PARTIE V — SÉCURITÉ DES CONTAINERS (Ch.21-26)**

21. [Surface d’attaque des containers : comprendre les risques](05-partie-v-securite-des-containers/01-chapitre-21-surface-dattaque-des-containers.md)
22. [Sécuriser les images : de la construction au déploiement](05-partie-v-securite-des-containers/02-chapitre-22-securiser-les-images-de-la-constructio.md)
23. [Sécuriser le runtime : isolation et contrôle d’exécution](05-partie-v-securite-des-containers/03-chapitre-23-securiser-le-runtime-isolation-et-cont.md)
24. [Sécuriser le réseau : segmentation et chiffrement](05-partie-v-securite-des-containers/04-chapitre-24-securiser-le-reseau-segmentation-et-ch.md)
25. [Sécuriser Kubernetes : RBAC, Secrets et API Server](05-partie-v-securite-des-containers/05-chapitre-25-securiser-kubernetes-rbac-secrets-et-a.md)
26. [Détection et réponse aux incidents dans les containers](05-partie-v-securite-des-containers/06-chapitre-26-detection-et-reponse-aux-incidents-dan.md)

**PARTIE VI — ARCHITECTURES ET PATTERNS AVANCÉS (Ch.27-28)**

27. [Microservices, patterns et anti-patterns](06-partie-vi-architectures-et-patterns-avances.md#chapitre-27-microservices-patterns-et-anti-patterns)
28. [Multi-tenancy, scaling et production](06-partie-vi-architectures-et-patterns-avances.md#chapitre-28-multi-tenancy-scaling-et-production)

**PARTIE VII — SYNTHÈSE (Ch.29-30)**

29. [Cas de synthèse : audit de sécurité d’un environnement containerisé](07-partie-vii-synthese.md#chapitre-29-cas-de-synthese-audit-de-securite-dun-environnement-containerise)
30. [Le métier et les perspectives](07-partie-vii-synthese.md#chapitre-30-le-metier-et-les-perspectives)

**ANNEXES**

-----

### Fil rouge : Opération CONTAINER

> **Contexte narratif**
> 
> **Sami Khelil**, 29 ans, ingénieur sécurité infrastructure dans une ESN (800 personnes), est intégré à l’équipe projet de **MedFlow**, une startup healthtech (60 personnes) qui migre son application monolithique vers une architecture containerisée.
> 
> L’application MedFlow est une plateforme de gestion de dossiers patients. La stack technique : Python/Django (backend), PostgreSQL (base de données), Redis (cache), Celery (tâches asynchrones). L’application tourne actuellement sur 3 machines virtuelles classiques, configurées manuellement.
> 
> La cible : Docker en développement, Kubernetes managé (type EKS/AKS/GKE) en production.
> 
> Sami intervient en **double casquette** : accompagner la containerisation (ops) ET garantir la sécurité de l’architecture résultante. Il découvre en cours de projet que l’image Docker de base contient 147 CVE, que les secrets de l’application sont en clair dans les fichiers de configuration Kubernetes, et qu’un développeur a monté le Docker socket dans un container de CI — une faille qui donne le contrôle total de la machine hôte.
> 
> **Progression :** pourquoi containeriser → premiers containers Docker → construction d’images → Docker Compose → introduction Kubernetes → déploiement K8s → sécurisation progressive → incident et remédiation.

-----

## Sommaire

- [Partie I — Fondations](01-partie-i-fondations/index.md)
    - [Chapitre 1 — Pourquoi les containers](01-partie-i-fondations/01-chapitre-1-pourquoi-les-containers.md)
    - [Chapitre 2 — L’architecture container](01-partie-i-fondations/02-chapitre-2-larchitecture-container.md)
    - [Chapitre 3 — Installer Docker et premiers containers](01-partie-i-fondations/03-chapitre-3-installer-docker-et-premiers-containers.md)
    - [Chapitre 4 — Images Docker : comprendre, chercher, utiliser](01-partie-i-fondations/04-chapitre-4-images-docker-comprendre-chercher-utili.md)
    - [Chapitre 5 — Réseau, volumes et persistance](01-partie-i-fondations/05-chapitre-5-reseau-volumes-et-persistance.md)
- [Partie II — Construire et composer](02-partie-ii-construire-et-composer/index.md)
    - [Chapitre 6 — Écrire un Dockerfile : de zéro à l’image](02-partie-ii-construire-et-composer/01-chapitre-6-ecrire-un-dockerfile-de-zero-a-limage.md)
    - [Chapitre 7 — Optimiser et durcir ses images](02-partie-ii-construire-et-composer/02-chapitre-7-optimiser-et-durcir-ses-images.md)
    - [Chapitre 8 — Docker Compose : orchestrer plusieurs containers](02-partie-ii-construire-et-composer/03-chapitre-8-docker-compose-orchestrer-plusieurs-con.md)
    - [Chapitre 9 — Registries et gestion des images](02-partie-ii-construire-et-composer/04-chapitre-9-registries-et-gestion-des-images.md)
    - [Chapitre 10 — Capstone Partie II](02-partie-ii-construire-et-composer/05-chapitre-10-capstone-partie-ii.md)
- [Partie III — Kubernetes : les fondamentaux](03-partie-iii-kubernetes-les-fondamentaux/index.md)
    - [Chapitre 11 — Pourquoi Kubernetes : quand Docker ne suffit plus](03-partie-iii-kubernetes-les-fondamentaux/01-chapitre-11-pourquoi-kubernetes-quand-docker-ne-su.md)
    - [Chapitre 12 — Architecture Kubernetes : les composants du cluster](03-partie-iii-kubernetes-les-fondamentaux/02-chapitre-12-architecture-kubernetes-les-composants.md)
    - [Chapitre 13 — Les objets Kubernetes essentiels](03-partie-iii-kubernetes-les-fondamentaux/03-chapitre-13-les-objets-kubernetes-essentiels.md)
    - [Chapitre 14 — Déployer sur Kubernetes : kubectl et les manifests](03-partie-iii-kubernetes-les-fondamentaux/04-chapitre-14-deployer-sur-kubernetes-kubectl-et-les.md)
    - [Chapitre 15 — Stockage, Ingress et configuration avancée](03-partie-iii-kubernetes-les-fondamentaux/05-chapitre-15-stockage-ingress-et-configuration-avan.md)
    - [Chapitre 16 — Capstone Partie III](03-partie-iii-kubernetes-les-fondamentaux/06-chapitre-16-capstone-partie-iii.md)
- [Partie IV — Opérations et cycle de vie](04-partie-iv-operations-et-cycle-de-vie/index.md)
    - [Chapitre 17 — CI/CD et containers : du code au déploiement](04-partie-iv-operations-et-cycle-de-vie/01-chapitre-17-ci-cd-et-containers-du-code-au-deploie.md)
    - [Chapitre 18 — Monitoring, logs et observabilité](04-partie-iv-operations-et-cycle-de-vie/02-chapitre-18-monitoring-logs-et-observabilite.md)
    - [Chapitre 19 — Troubleshooting containers et Kubernetes](04-partie-iv-operations-et-cycle-de-vie/03-chapitre-19-troubleshooting-containers-et-kubernet.md)
- [Partie V — Sécurité des containers](05-partie-v-securite-des-containers/index.md)
    - [Chapitre 21 — Surface d’attaque des containers](05-partie-v-securite-des-containers/01-chapitre-21-surface-dattaque-des-containers.md)
    - [Chapitre 22 — Sécuriser les images : de la construction au déploiement](05-partie-v-securite-des-containers/02-chapitre-22-securiser-les-images-de-la-constructio.md)
    - [Chapitre 23 — Sécuriser le runtime : isolation et contrôle d’exécution](05-partie-v-securite-des-containers/03-chapitre-23-securiser-le-runtime-isolation-et-cont.md)
    - [Chapitre 24 — Sécuriser le réseau : segmentation et chiffrement](05-partie-v-securite-des-containers/04-chapitre-24-securiser-le-reseau-segmentation-et-ch.md)
    - [Chapitre 25 — Sécuriser Kubernetes : RBAC, Secrets et API Server](05-partie-v-securite-des-containers/05-chapitre-25-securiser-kubernetes-rbac-secrets-et-a.md)
    - [Chapitre 26 — Détection et réponse aux incidents dans les containers](05-partie-v-securite-des-containers/06-chapitre-26-detection-et-reponse-aux-incidents-dan.md)
- [Partie VI — Architectures et patterns avancés](06-partie-vi-architectures-et-patterns-avances.md)
- [Partie VII — Synthèse](07-partie-vii-synthese.md)
- [Annexes](08-annexes.md)
