---
title: Kubernetes
source: IT/08 Conteneurs & automatisation/Kubernetes.md
format: cours
revue: '2026-06-13'
---

*De zéro à l'opération, au diagnostic et à la sécurité défensive — Guide pour débutant*

---

> **Prérequis :** des bases en Linux, terminal, réseau (IP / port / DNS) et un peu de Docker. **Aucune** connaissance de Kubernetes n'est supposée, ni aucun niveau DevOps avancé. Si tu viens de l'administration système, du réseau, du SOC, du pentest débutant ou de la cloud security junior, ce cours est fait pour toi.
> Tout ce dont tu as besoin, c'est une machine Linux (ou Windows/Mac) capable de faire tourner un petit cluster local avec **Minikube**.

---

> **Variante de ce cours : "orienté cyber / cloud security junior".**
> Ce cours garde **tout le tronc commun admin/opérationnel** (Pods, Deployments, Services, config, diagnostic), parce qu'on ne sécurise bien que ce qu'on sait opérer. Mais il ajoute, partout, une **coloration cybersécurité défensive** : surface d'attaque, exposition de services, secrets, RBAC, namespaces, durcissement. L'esprit du cours tient en une phrase :
>
> **Kubernetes débutant IT/cyber : savoir opérer, diagnostiquer, puis sécuriser.**

---

### À qui s'adresse ce cours

- À un **admin Linux / réseau** qui doit comprendre Kubernetes sans devenir DevOps.
- À un **analyste SOC** qui verra passer des logs, des events et des alertes venant de clusters.
- À un **cloud security junior** qui doit auditer et durcir des clusters.
- À un **pentester débutant** qui veut comprendre la surface d'attaque K8s **côté défense** d'abord.
- À toute personne curieuse qui veut un modèle mental clair de Kubernetes avant de taper des commandes.

### Ce que ce cours n'est PAS

Pour rester pédagogique et accessible, certains sujets sont **volontairement exclus**. Ils méritent un cours à part, **après** celui-ci :

- ❌ Ce n'est **pas** un cours **DevOps expert** ni un bachotage de certification (CKA/CKAD).
- ❌ Ce n'est **pas** un cours **Helm avancé**, **GitOps**, **Terraform** ou **CI/CD**.
- ❌ Ce n'est **pas** un cours de **production avancée** (haute dispo du control plane, multi-cluster, service mesh, opérateurs).
- ❌ Ce n'est **pas** un cours **cloud provider** (EKS, GKE, AKS) — on reste en **lab local**.
- ❌ Ce n'est **pas** un cours d'**exploitation offensive** de Kubernetes. On reste **défensif** : comprendre les risques pour les **réduire**, pas pour les exploiter.

Ces sujets peuvent venir **après**, une fois les fondamentaux de ce cours acquis (voir l'annexe « Suite logique »).

### 🎯 L'objectif final, concrètement

Pour que tu saches exactement où tu vas, à la **fin de ce cours** tu dois être capable de :

- **Expliquer** ce qu'est un cluster, un node, un Pod, et le modèle « état désiré → état réel ».
- **Lire et écrire** un manifest YAML simple (Pod, Deployment, Service, ConfigMap, Secret, Ingress).
- **Déployer** une application, la **scaler**, la **mettre à jour** et faire un **rollback**.
- **Exposer** une application proprement (Service, puis Ingress).
- **Diagnostiquer** un Pod en panne avec `logs`, `describe`, `events`, `exec`.
- **Inventorier** un cluster et faire une « photo » de ce qui s'y trouve.
- **Repérer et corriger** les mauvaises configurations de sécurité les plus courantes (Secrets en clair, RBAC trop large, Pod root, NodePort inutile…).
- **Auditer** un petit cluster mal configuré et proposer un durcissement de base.

---

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici dès qu'un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **Conteneur** | Un processus isolé qui embarque une application et ses dépendances |
| **Image** | Le « modèle » figé à partir duquel on lance un conteneur |
| **Cluster** | L'ensemble des machines pilotées ensemble par Kubernetes |
| **Node (nœud)** | Une machine (physique ou virtuelle) du cluster |
| **Control plane** | Le « cerveau » du cluster : il décide et coordonne |
| **Worker node** | Une machine qui **exécute** réellement les applications |
| **Pod** | La plus petite unité déployable : un ou plusieurs conteneurs groupés |
| **kubectl** | L'outil en ligne de commande pour parler au cluster |
| **Manifest** | Un fichier (souvent YAML) qui décrit un objet Kubernetes |
| **YAML** | Le format texte structuré utilisé pour écrire les manifests |
| **Objet (ressource)** | Une « chose » gérée par Kubernetes (Pod, Service, Deployment…) |
| **Deployment** | Un objet qui gère le déploiement et la mise à jour d'une appli |
| **ReplicaSet** | L'objet qui maintient un nombre voulu de copies d'un Pod |
| **Service** | Une adresse réseau stable qui pointe vers un groupe de Pods |
| **Ingress** | La porte d'entrée HTTP/HTTPS du cluster vers tes apps |
| **Namespace** | Un « quartier » logique qui cloisonne les objets du cluster |
| **Label** | Une étiquette `clé: valeur` collée sur un objet |
| **Selector** | Un filtre qui sélectionne des objets d'après leurs labels |
| **ConfigMap** | Un objet qui stocke de la configuration non sensible |
| **Secret** | Un objet qui stocke des données sensibles (⚠️ **encodées**, pas chiffrées par défaut) |
| **Volume** | Un espace de stockage rattaché à un Pod |
| **etcd** | La base de données qui stocke **tout** l'état du cluster |
| **API server** | La porte d'entrée unique vers le cluster (tout passe par lui) |
| **RBAC** | Le système qui décide **qui a le droit de faire quoi** |
| **ServiceAccount** | L'identité utilisée par un Pod pour parler à l'API |
| **kubeconfig** | Le fichier qui contient **tes identifiants d'accès** au cluster |
| **État désiré** | Ce que tu **demandes** à Kubernetes (« je veux 3 copies ») |
| **État réel** | Ce qui **tourne vraiment** à un instant T |
| **Réconciliation** | Le travail permanent de Kubernetes pour faire coïncider réel et désiré |

---

### Comment penser Kubernetes

Avant de taper la moindre commande, il faut comprendre **la seule grande idée** qui structure tout Kubernetes. Si tu retiens une chose de ce cours, c'est celle-ci :

```
   TU DÉCRIS              KUBERNETES COMPARE            KUBERNETES AGIT
   l'état désiré    →     désiré vs réel en boucle  →   pour atteindre le désiré
  "je veux 3 Pods"        "il n'y en a que 2"           "j'en crée 1 de plus"
```


C'est ce qu'on appelle la **boucle de réconciliation**. Tu ne dis **pas** à Kubernetes *comment* faire les choses étape par étape (ça, c'est l'approche d'un script Bash). Tu lui dis **ce que tu veux**, et il s'efforce en permanence d'y arriver — et d'y **rester**.

Concrètement, presque tout dans Kubernetes se ramène à 4 idées :

1. **Décrire** un état désiré dans un manifest (« je veux cette appli, en 3 exemplaires, exposée sur ce port »).
2. **Soumettre** cet état désiré à l'API server (`kubectl apply`).
3. **Stocker** cet état dans etcd (la mémoire du cluster).
4. **Réconcilier** : des contrôleurs surveillent en boucle l'écart entre désiré et réel, et le corrigent (un Pod meurt ? il est recréé. Tu passes de 3 à 5 copies ? 2 de plus apparaissent).

> **Garde ce schéma en tête à chaque chapitre.** Quand un comportement de Kubernetes te surprendra (« pourquoi mon Pod renaît tout seul ?! »), la réponse sera presque toujours : *parce que tu as décrit un état désiré, et Kubernetes le maintient*.

---

### Les 3 lunettes : Lab, Production, Sécurité

Tout au long du cours, tu porteras **trois paires de lunettes**. On les pose dès maintenant pour ne jamais les confondre :

- **🧪 Lunette LAB** — ce qu'on fait sur ta machine pour **apprendre et casser sans risque**. Simplifié, mono-machine, jetable.
- **🏭 Lunette PRODUCTION RÉELLE** — ce qui changerait si de **vrais utilisateurs** dépendaient du cluster (haute disponibilité, sauvegardes, redondance). Le cours **signale** ces différences sans chercher à faire de toi un **SRE Kubernetes**.
- **🛡️ Lunette SÉCURITÉ** — ce qu'un **défenseur** doit surveiller : qu'est-ce qui est exposé, qui a quels droits, où sont les secrets, quelle est la surface d'attaque.

Tu verras régulièrement des encadrés qui changent de lunette. Quand tu liras **🧪 Lab vs 🏭 Production réelle**, c'est qu'une chose acceptable en lab serait dangereuse en vrai. Quand tu liras **🛡️ Réflexe sécurité** ou **🔍 Réflexe diagnostic**, c'est un automatisme à acquérir.

---

### Prérequis techniques et matériel recommandé

Kubernetes peut vite devenir **frustrant si ton lab ne démarre pas**. Autant cadrer ça tout de suite.

#### Connaissances supposées (rappels inclus dans le cours)

| Domaine | Niveau attendu | Où c'est rappelé |
|---------|----------------|------------------|
| **Linux de base** | Se déplacer, éditer un fichier, lire un log | Supposé acquis |
| **Terminal** | Lancer des commandes, lire une sortie | Supposé acquis |
| **Réseau** | Comprendre IP, port, DNS (juste les bases) | Rappelé au fil du cours |
| **YAML** | Aucune connaissance requise | **Chapitre 9 entier** |
| **Docker / conteneurs** | Avoir déjà vu `docker run` aide | **Rappel au Chapitre 2** |

> Si « IP », « port » et « DNS » sont totalement flous pour toi, fais d'abord un détour par les bases réseau. Le reste, le cours te le donne.

#### Matériel recommandé

Minikube lance un **petit cluster mono-machine**. C'est léger, mais pas inexistant.

| Ressource | Minimum | Confortable |
|-----------|---------|-------------|
| **RAM** | 2 Go libres pour le cluster | 4 Go ou plus |
| **CPU** | 2 cœurs | 4 cœurs |
| **Disque** | 20 Go libres | 40 Go ou plus |
| **OS** | Linux, macOS, ou Windows | Linux (le plus simple) |

#### Faut-il Docker ?

Minikube a besoin d'un **« driver »** pour faire tourner le cluster. Selon ta machine :

- **Driver `docker`** (le plus courant) : il faut **Docker installé**. Simple si tu as déjà Docker.
- **Driver `virtualbox` / `kvm` / `hyperkit`** : Minikube crée une petite VM, **sans** Docker installé sur l'hôte.

On détaillera le choix au **Chapitre 4**. Retiens juste : **oui, on aura probablement besoin de Docker** (driver par défaut), mais ce n'est pas la seule option.

#### ⚠️ Limites de WSL (Windows)

Si tu es sous Windows et que tu comptes utiliser **WSL2** :

- C'est **jouable**, mais c'est la configuration la **plus piégeuse** pour un débutant.
- Le driver `docker` via **Docker Desktop** est la voie la plus fiable.
- Les histoires d'IP, de réseau et d'accès aux Services depuis Windows sont **moins intuitives** depuis WSL.

> **Conseil honnête :** si tu peux, apprends Kubernetes sur une **VM Linux** ou une machine Linux. Tu t'épargnes une couche de complexité réseau qui n'a rien à voir avec Kubernetes lui-même.

---

### ⚠️ Encadré essentiel — Commandes Kubernetes à manipuler avec prudence

Avant d'aller plus loin, lis ceci **attentivement**. Certaines commandes Kubernetes sont **destructrices** et n'affichent **aucune demande de confirmation**. En lab, tu peux tout casser sans risque. Mais ces réflexes te suivront en production, alors prends les bonnes habitudes **maintenant**.

#### Les commandes qui détruisent

```bash
kubectl delete pod <nom>            # Supprime un Pod (souvent recréé s'il a un Deployment)
kubectl delete deployment <nom>     # Supprime un Deployment ET ses Pods
kubectl delete svc <nom>            # Supprime un Service (coupe l'accès réseau)
kubectl delete namespace <nom>      # ☠️ Supprime le namespace ET TOUT ce qu'il contient
kubectl delete pvc <nom>            # ☠️ Supprime un PVC → PERTE DE DONNÉES possible
kubectl delete -f .                 # Supprime TOUT ce que décrivent les YAML du dossier
kubectl apply -f . --prune          # ☠️ Supprime les objets "en trop" → effets de bord
kubectl replace --force             # Détruit puis recrée l'objet (interruption)
```


#### Les deux pièges qui font le plus de dégâts pour un débutant

```bash
kubectl delete namespace <nom>      # Tu crois supprimer "un truc"... tu supprimes une appli entière
kubectl delete pvc <nom>            # Tu crois nettoyer... tu effaces des données peut-être irrécupérables
```


#### Les 3 règles d'or

> **1. Vérifie TOUJOURS ton namespace courant avant d'agir.**
> Une commande `delete` lancée dans le mauvais namespace détruit les mauvaises ressources.
> ```bash
> kubectl config view --minify | grep namespace   # Quel namespace est actif ?
> ```
>
> **2. Fais TOUJOURS un `get` avant un `delete`.**
> Regarde **exactement** ce que tu t'apprêtes à supprimer.
> ```bash
> kubectl get pods                 # D'abord regarder...
> kubectl delete pod mon-pod       # ...ensuite supprimer.
> ```
>
> **3. Ne supprime JAMAIS un PVC sans comprendre l'impact sur les données.**
> Un PVC peut être la seule trace d'une base de données. Une fois supprimé, c'est parfois définitif.

🛡️ **Réflexe sécurité dès maintenant :** ces commandes destructrices sont aussi ce qu'un **attaquant** ou un **accident** peut déclencher si les droits (RBAC) sont trop larges. Tout le cours te montrera comment **réduire** qui peut faire ça.

---

### 🧨 La Boîte à risques Kubernetes

Voici la **carte des dangers** que tu vas apprendre à reconnaître et à neutraliser tout au long du cours. Tu n'as **pas** besoin de tout comprendre maintenant — c'est une **carte mentale** à garder sous les yeux. Chaque ligne sera traitée en détail dans le chapitre indiqué. C'est l'équivalent, pour Kubernetes, d'une check-list d'audit défensif.

| # | Risque de configuration | Pourquoi c'est dangereux | Traité au |
|---|-------------------------|--------------------------|-----------|
| 1 | **Secret commité dans Git** | Une fois dans l'historique, il est compromis à vie | Ch. 20 |
| 2 | **base64 confondu avec du chiffrement** | Un Secret K8s est **lisible**, pas protégé | Ch. 20 |
| 3 | **RBAC trop large** | Trop de droits = escalade de privilèges facile | Ch. 24 |
| 4 | **`cluster-admin` donné trop facilement** | Ce sont les clés de **tout** le cluster | Ch. 24 |
| 5 | **Token de ServiceAccount monté inutilement** | Un Pod compromis devient un pivot vers l'API | Ch. 25 |
| 6 | **Pod qui tourne en root** | Compromission = contrôle élargi sur le node | Ch. 26 |
| 7 | **Absence de `requests`/`limits`** | Un Pod peut épuiser les ressources du node (DoS interne) | Ch. 22 |
| 8 | **NodePort exposé inutilement** | Ouvre un port sur **chaque** node = surface d'attaque | Ch. 16 |
| 9 | **Absence de NetworkPolicies** | Réseau plat : un Pod compromis parle à tous les autres | Ch. 26bis |
| 10 | **Image `latest` ou non maîtrisée** | Tu ne sais pas vraiment **ce qui** tourne | Ch. 22 / 26 |
| 11 | **kubeconfig exposé** | C'est un accès complet au cluster, comme une clé SSH | Ch. 8 |
| 12 | **Namespace supprimé par erreur** | Détruit une appli entière d'un coup | Ch. 23 |
| 13 | **PVC supprimé sans comprendre l'impact** | Perte de données potentiellement irréversible | Ch. 21 |

> Tu retrouveras cette boîte, **complétée et exploitée**, dans la Partie VIII et dans le capstone « audit de sécurité d'un cluster mal configuré ».

---

### Sur la montée en difficulté

Le cours commence **très doux** : les Parties I et II ne contiennent **presque aucune commande qui modifie le cluster**. On installe le lab, on **observe**, on construit un modèle mental. La manipulation réelle commence en **Partie III**.

À partir de la Partie V (Deployments, réseau, config), le cours reste accessible mais demande **plus de pratique**. Il est normal de devoir :

- Refaire un exercice plusieurs fois.
- Relire un chapitre à tête reposée.
- Bloquer sur le réseau, RBAC ou les volumes — c'est **normal**.

> **Conseil important :** si un chapitre te paraît flou, **continue quand même**. Plusieurs notions ne s'éclairent qu'à la lumière du chapitre suivant (le réseau éclaire les Services, RBAC éclaire les ServiceAccounts…). Reviens en arrière une fois que tu as vu la suite.

Ne te juge pas. **La patience compte plus que la vitesse.**

---

### Table des matières

**PARTIE 0 — PRÉAMBULE** *(tu es ici)*

**PARTIE I — COMPRENDRE POURQUOI KUBERNETES EXISTE**

1. [Le problème que Kubernetes résout](01-partie-i-comprendre-pourquoi-kubernetes-existe/01-chapitre-1-le-probleme-que-kubernetes-resout.md)
2. [Rappel minimal sur les conteneurs](01-partie-i-comprendre-pourquoi-kubernetes-existe/02-chapitre-2-rappel-minimal-sur-les-conteneurs.md)
3. [Docker vs Kubernetes : la bascule](01-partie-i-comprendre-pourquoi-kubernetes-existe/03-chapitre-3-docker-vs-kubernetes-la-bascule.md)
4. [Monter son lab local avec Minikube](01-partie-i-comprendre-pourquoi-kubernetes-existe/04-chapitre-4-monter-son-lab-local-avec-minikube.md)

**PARTIE II — ANATOMIE D'UN CLUSTER**

5. Cluster, nodes, control plane, workers
6. Les composants internes (API server, scheduler, etcd…) + premiers namespaces
7. Le cycle de vie d'une requête Kubernetes

**PARTIE III — PREMIERS PAS AVEC KUBECTL ET LES PODS**

8. kubectl, le couteau suisse (impératif vs déclaratif, `get all`, namespaces)
9. Comprendre et écrire du YAML (`diff`, `--dry-run`)
10. Le Pod, l'unité de base

**PARTIE IV — DIAGNOSTIQUER UN POD**

11. Les 4 réflexes : logs, describe, events, exec
12. Les états d'un Pod et les pannes classiques

**PARTIE V — FAIRE TOURNER DES APPLICATIONS**

13. ReplicaSets et la réconciliation
14. Les Deployments (scaling, rolling update, rollback)

**PARTIE VI — EXPOSER ET CONNECTER**

15. Labels, selectors et l'art de relier les objets
16. Les Services (ClusterIP, NodePort)
17. Le réseau Kubernetes en clair
18. Ingress : la porte d'entrée HTTP

**PARTIE VII — CONFIGURER LES APPLICATIONS**

19. ConfigMaps
20. Secrets (et leurs pièges)
21. Volumes et persistance
22. Probes, requests et limits

**PARTIE VIII — ORGANISER ET SÉCURISER LE CLUSTER**

23. Namespaces : cloisonner le cluster
24. RBAC : qui a le droit de faire quoi
25. ServiceAccounts et identité des Pods
26. Durcissement de base et hygiène

26bis. NetworkPolicies : filtrer le réseau entre Pods

27. Inventaire et audit de cluster

**PARTIE IX — MINI-PROJETS INTÉGRATEURS**

**PARTIE X — 🔴 BONUS — ALLER PLUS LOIN** (Helm, observabilité, vers la prod)

**ANNEXES** (cheat-sheets kubectl & YAML, glossaire étendu, NetworkPolicies avancées, réflexes diagnostic & sécurité, suite logique)

---
---

## Sommaire

- [PARTIE I — Comprendre pourquoi Kubernetes existe](01-partie-i-comprendre-pourquoi-kubernetes-existe/index.md)
    - [Chapitre 1 — Le problème que Kubernetes résout](01-partie-i-comprendre-pourquoi-kubernetes-existe/01-chapitre-1-le-probleme-que-kubernetes-resout.md)
    - [Chapitre 2 — Rappel minimal sur les conteneurs](01-partie-i-comprendre-pourquoi-kubernetes-existe/02-chapitre-2-rappel-minimal-sur-les-conteneurs.md)
    - [Chapitre 3 — Docker vs Kubernetes : la bascule](01-partie-i-comprendre-pourquoi-kubernetes-existe/03-chapitre-3-docker-vs-kubernetes-la-bascule.md)
    - [Chapitre 4 — Monter son lab local avec Minikube](01-partie-i-comprendre-pourquoi-kubernetes-existe/04-chapitre-4-monter-son-lab-local-avec-minikube.md)
