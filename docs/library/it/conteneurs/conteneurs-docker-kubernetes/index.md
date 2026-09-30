---
title: Conteneurs — Docker & Kubernetes
source: IT/10_virtualization-containers/Containers_Docker_K8s.md
chapters: 7
---

### De zéro à la maîtrise — Comprendre, déployer et sécuriser

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

1. [Pourquoi les containers : du serveur physique au container](1-partie-i-fondations.md#chapitre-1-pourquoi-les-containers-du-serveur-physique-au-container)
1. [L’architecture container : comment ça marche sous le capot](1-partie-i-fondations.md#chapitre-2-larchitecture-container-comment-ca-marche-sous-le-capot)
1. [Installer Docker et premiers containers](1-partie-i-fondations.md#chapitre-3-installer-docker-et-premiers-containers)
1. [Images Docker : comprendre, chercher, utiliser](1-partie-i-fondations.md#chapitre-4-images-docker-comprendre-chercher-utiliser)
1. [Réseau, volumes et persistance](1-partie-i-fondations.md#chapitre-5-reseau-volumes-et-persistance)

**PARTIE II — CONSTRUIRE ET COMPOSER (Ch.6-10)**
6. [Écrire un Dockerfile : de zéro à l’image](2-partie-ii-construire-et-composer.md#chapitre-6-ecrire-un-dockerfile-de-zero-a-limage)
7. [Optimiser et durcir ses images](2-partie-ii-construire-et-composer.md#chapitre-7-optimiser-et-durcir-ses-images)
8. [Docker Compose : orchestrer plusieurs containers](2-partie-ii-construire-et-composer.md#chapitre-8-docker-compose-orchestrer-plusieurs-containers)
9. [Registries et gestion des images](2-partie-ii-construire-et-composer.md#chapitre-9-registries-et-gestion-des-images)
10. [Capstone : containeriser une application complète](2-partie-ii-construire-et-composer.md#chapitre-10-capstone-partie-ii-containeriser-une-application-complete)

**PARTIE III — KUBERNETES : LES FONDAMENTAUX (Ch.11-16)**
11. [Pourquoi Kubernetes : quand Docker ne suffit plus](3-partie-iii-kubernetes-les-fondamentaux.md#chapitre-11-pourquoi-kubernetes-quand-docker-ne-suffit-plus)
12. [Architecture Kubernetes : les composants du cluster](3-partie-iii-kubernetes-les-fondamentaux.md#chapitre-12-architecture-kubernetes-les-composants-du-cluster)
13. [Les objets Kubernetes essentiels](3-partie-iii-kubernetes-les-fondamentaux.md#chapitre-13-les-objets-kubernetes-essentiels)
14. [Déployer sur Kubernetes : kubectl et les manifests](3-partie-iii-kubernetes-les-fondamentaux.md#chapitre-14-deployer-sur-kubernetes-kubectl-et-les-manifests)
15. [Stockage, Ingress et configuration avancée](3-partie-iii-kubernetes-les-fondamentaux.md#chapitre-15-stockage-ingress-et-configuration-avancee)
16. [Capstone : déployer une application sur Kubernetes](3-partie-iii-kubernetes-les-fondamentaux.md#chapitre-16-capstone-partie-iii-deployer-une-application-sur-kubernetes)

**PARTIE IV — OPÉRATIONS ET CYCLE DE VIE (Ch.17-20)**
17. [CI/CD et containers : du code au déploiement](4-partie-iv-operations-et-cycle-de-vie.md#chapitre-17-cicd-et-containers-du-code-au-deploiement)
18. [Monitoring, logs et observabilité](4-partie-iv-operations-et-cycle-de-vie.md#chapitre-18-monitoring-logs-et-observabilite)
19. [Troubleshooting containers et Kubernetes](4-partie-iv-operations-et-cycle-de-vie.md#chapitre-19-troubleshooting-containers-et-kubernetes)
20. [Capstone : pipeline CI/CD et monitoring](4-partie-iv-operations-et-cycle-de-vie.md#chapitre-20-capstone-partie-iv-pipeline-cicd-et-monitoring)

**PARTIE V — SÉCURITÉ DES CONTAINERS (Ch.21-26)**
21. [Surface d’attaque des containers : comprendre les risques](5-partie-v-securite-des-containers.md#chapitre-21-surface-dattaque-des-containers-comprendre-les-risques)
22. [Sécuriser les images : de la construction au déploiement](5-partie-v-securite-des-containers.md#chapitre-22-securiser-les-images-de-la-construction-au-deploiement)
23. [Sécuriser le runtime : isolation et contrôle d’exécution](5-partie-v-securite-des-containers.md#chapitre-23-securiser-le-runtime-isolation-et-controle-dexecution)
24. [Sécuriser le réseau : segmentation et chiffrement](5-partie-v-securite-des-containers.md#chapitre-24-securiser-le-reseau-segmentation-et-chiffrement)
25. [Sécuriser Kubernetes : RBAC, Secrets et API Server](5-partie-v-securite-des-containers.md#chapitre-25-securiser-kubernetes-rbac-secrets-et-api-server)
26. [Détection et réponse aux incidents dans les containers](5-partie-v-securite-des-containers.md#chapitre-26-detection-et-reponse-aux-incidents-dans-les-containers)

**PARTIE VI — ARCHITECTURES ET PATTERNS AVANCÉS (Ch.27-28)**
27. [Microservices, patterns et anti-patterns](6-partie-vi-architectures-et-patterns-avances.md#chapitre-27-microservices-patterns-et-anti-patterns)
28. [Multi-tenancy, scaling et production](6-partie-vi-architectures-et-patterns-avances.md#chapitre-28-multi-tenancy-scaling-et-production)

**PARTIE VII — SYNTHÈSE (Ch.29-30)**
29. [Cas de synthèse : audit de sécurité d’un environnement containerisé](7-partie-vii-synthese.md#chapitre-29-cas-de-synthese-audit-de-securite-dun-environnement-containerise)
30. [Le métier et les perspectives](7-partie-vii-synthese.md#chapitre-30-le-metier-et-les-perspectives)

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

1. [PARTIE I — FONDATIONS](1-partie-i-fondations.md)
2. [PARTIE II — CONSTRUIRE ET COMPOSER](2-partie-ii-construire-et-composer.md)
3. [PARTIE III — KUBERNETES : LES FONDAMENTAUX](3-partie-iii-kubernetes-les-fondamentaux.md)
4. [PARTIE IV — OPÉRATIONS ET CYCLE DE VIE](4-partie-iv-operations-et-cycle-de-vie.md)
5. [PARTIE V — SÉCURITÉ DES CONTAINERS](5-partie-v-securite-des-containers.md)
6. [PARTIE VI — ARCHITECTURES ET PATTERNS AVANCÉS](6-partie-vi-architectures-et-patterns-avances.md)
7. [PARTIE VII — SYNTHÈSE](7-partie-vii-synthese.md)
