---
title: Kubernetes
source: IT/10_virtualization-containers/Kubernetes.md
---

### De zéro à l'opération, au diagnostic et à la sécurité défensive — Guide pour débutant

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

1. [Le problème que Kubernetes résout](#chapitre-1-le-probleme-que-kubernetes-resout)
2. [Rappel minimal sur les conteneurs](#chapitre-2-rappel-minimal-sur-les-conteneurs)
3. [Docker vs Kubernetes : la bascule](#chapitre-3-docker-vs-kubernetes-la-bascule)
4. [Monter son lab local avec Minikube](#chapitre-4-monter-son-lab-local-avec-minikube)

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

## PARTIE I — COMPRENDRE POURQUOI KUBERNETES EXISTE

> Dans toute cette partie, on **ne modifie pas** le cluster. On installe juste de quoi observer plus tard, et surtout on construit le **modèle mental**. Résiste à l'envie de « faire » : ici, on **comprend**.

---

## Chapitre 1 — Le problème que Kubernetes résout

### Le minimum à savoir

#### Pourquoi commencer par « le problème » ?

Beaucoup de gens apprennent Kubernetes en tapant des commandes qu'ils ne comprennent pas. Résultat : ils savent *faire* des choses, mais paniquent dès que ça casse. On va éviter ça. **Kubernetes est une réponse à des problèmes très concrets.** Si tu comprends les problèmes, les solutions deviennent évidentes.

#### L'histoire d'un serveur unique

Imagine que tu administres **une application web** sur **un seul serveur Linux**. Au début, tout va bien. Puis les ennuis arrivent :

- **L'appli plante à 3 h du matin.** Personne ne la redémarre avant le lendemain. Downtime.
- **Le trafic explose un jour de pic.** Ton serveur unique sature. Tu ne peux pas « ajouter de la puissance » instantanément.
- **Tu dois mettre à jour l'appli.** Tu coupes tout, tu déploies, tu pries. Si ça casse, tu reviens en arrière à la main, sous pression.
- **Le serveur lui-même tombe.** Disque mort, coupure réseau. Toute l'appli est par terre.
- **« Ça marche sur ma machine ».** Le développeur jure que ça marche chez lui. Chez toi, non. Versions différentes, dépendances différentes.

Chacun de ces problèmes, un admin Linux le résout **à la main** : un script de redémarrage, un second serveur monté en urgence, un load balancer configuré manuellement, une procédure de rollback notée dans un coin. Ça marche… tant que tu as **peu** de serveurs et **peu** d'applis.

#### Ce qui casse à grande échelle

Maintenant imagine **50 serveurs** et **30 applications**. Les corvées manuelles deviennent **ingérables** :

- Qui surveille que chaque appli tourne, partout, tout le temps ?
- Qui décide **quel serveur** héberge **quelle appli** pour équilibrer la charge ?
- Qui recrée automatiquement une appli quand son serveur meurt ?
- Qui gère les mises à jour progressives sans tout couper ?

C'est **exactement** ce travail que Kubernetes automatise. On appelle ça l'**orchestration de conteneurs**.

#### La définition simple

> **Kubernetes est un système qui fait tourner tes applications (en conteneurs) sur un ensemble de machines, et qui s'occupe automatiquement de les démarrer, les redémarrer, les répartir, les mettre à l'échelle et les mettre à jour — pour que tu décrives ce que tu veux au lieu de tout faire à la main.**

On l'écrit souvent **« K8s »** (K, puis 8 lettres « ubernete », puis s).

### Très utile en pratique

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

### Application admin / cyber

- **Côté admin système :** Kubernetes remplace une pile de scripts maison (systemd pour relancer, scripts de déploiement, configuration manuelle de load balancers). Ce que tu sais déjà en Linux n'est **pas perdu** : c'est le socle sur lequel K8s s'appuie.
- **Côté SOC / cyber :** un cluster Kubernetes, c'est **beaucoup de machines et d'applications pilotées par une seule API**. C'est une formidable centralisation… donc une **cible de choix**. Comprendre *pourquoi* le cluster existe, c'est comprendre *ce qu'un attaquant cherche à contrôler* : l'API qui commande tout.

🛡️ **Réflexe sécurité (à garder en tête pour tout le cours) :** plus un système automatise et centralise, plus **le point de contrôle central** (ici, l'API de Kubernetes) devient précieux à protéger. On y reviendra en détail (Ch. 6, 24, 25).

### ❌ Erreur classique

> **Croire que Kubernetes « remplace » Linux, le réseau ou Docker.**

C'est faux, et c'est un contresens qui handicape les débutants. Kubernetes **s'appuie** sur Linux (processus, namespaces noyau, réseau), sur les **conteneurs** (Docker/containerd) et sur le **réseau** (IP, DNS, ports). Ce sont tes acquis d'admin qui rendent Kubernetes compréhensible, pas l'inverse. Kubernetes ajoute une **couche d'orchestration** au-dessus — il ne supprime rien en dessous.

### Exercices

**Guidé :** Sur une feuille (ou un fichier texte), liste **5 tâches** que tu fais ou ferais à la main pour maintenir une appli en ligne sur un serveur Linux (ex. : « relancer le service s'il plante »). En face de chacune, écris la promesse Kubernetes correspondante en t'aidant du tableau plus haut. Objectif : **traduire ton métier actuel en vocabulaire K8s**.

**Autonome :** Décris en 5 lignes une situation réelle (vécue ou imaginée) où **un seul serveur** a posé problème (panne, pic de charge, mise à jour ratée). Puis explique, en une phrase par point, **comment Kubernetes** aurait changé l'issue. Pas de commande ici : c'est un exercice de **modèle mental**.

**Défi :** En une demi-page, explique à un collègue **non technique** ce qu'est Kubernetes, **sans jamais utiliser** les mots « Pod », « conteneur » ou « cluster ». Utilise uniquement des analogies (un chef d'orchestre, un gérant d'immeuble, un service de livraison qui se réorganise tout seul…). Si tu y arrives, c'est que tu as **vraiment** compris le « pourquoi ».

### ✅ Tu sais maintenant…

- **Pourquoi** Kubernetes existe : automatiser des corvées d'admin ingérables à grande échelle.
- Les grandes promesses : **self-healing, scaling, scheduling, rolling update, rollback, adresses stables**.
- Que Kubernetes **s'appuie** sur Linux, le réseau et les conteneurs — il ne les remplace pas.
- Que la **centralisation** apportée par K8s en fait une cible de sécurité majeure (point de contrôle = l'API).
- Le sens du sigle **K8s**.

---

## Chapitre 2 — Rappel minimal sur les conteneurs

### Le minimum à savoir

#### Pourquoi ce rappel ?

Kubernetes orchestre des **conteneurs**. Si la notion est floue, tout le reste le sera. Ce chapitre **nivelle** le prérequis : pas besoin d'être expert Docker, juste de comprendre **ce qu'est** un conteneur et **ce qu'il partage** avec la machine qui l'héberge (ce dernier point est crucial côté sécurité).

#### Image vs conteneur

Deux mots qu'on confond souvent :

- Une **image** est un **modèle figé** : une appli + ses dépendances + sa config minimale, empaquetées. C'est un fichier inerte, comme un plan.
- Un **conteneur** est une **instance en cours d'exécution** de cette image. C'est le plan **devenu réalité** et qui tourne.

> Analogie : l'**image** est la recette, le **conteneur** est le plat cuisiné. Avec une seule recette, tu peux cuisiner **plusieurs** plats identiques.

```bash
# Une image (modèle figé) :        nginx:1.27
# Un conteneur (instance qui tourne) : lancé à partir de nginx:1.27
docker run nginx:1.27       # crée et démarre UN conteneur à partir de l'image
```

#### Ce qu'un conteneur isole

Un conteneur fait croire à l'application qu'elle est **seule au monde** :

- Sa propre **vue des processus** (il ne voit pas ceux des autres).
- Son propre **système de fichiers** (ses fichiers à lui).
- Sa propre **vue réseau** (sa configuration).

Mais cette isolation est une **illusion soigneusement construite par le noyau Linux** (via des mécanismes appelés *namespaces* et *cgroups* — rien à voir avec les namespaces Kubernetes, attention au mot identique).

#### LE point clé : un conteneur n'est PAS une VM

C'est **la** distinction à intégrer, surtout côté sécurité :

| | Machine virtuelle (VM) | Conteneur |
|---|------------------------|-----------|
| Contient | Un OS complet (son propre noyau) | Juste l'appli + ses dépendances |
| Noyau | **Le sien**, isolé | **Celui de l'hôte**, partagé |
| Taille | Gigaoctets | Mégaoctets |
| Démarrage | Dizaines de secondes | Quasi instantané |
| Isolation | **Forte** (noyau séparé) | **Plus légère** (noyau partagé) |

> **Le conteneur partage le noyau de la machine hôte.** Il ne transporte pas son propre système d'exploitation. C'est ce qui le rend léger et rapide… **et c'est aussi sa principale limite de sécurité.**

### Très utile en pratique

```bash
docker run -d --name web nginx:1.27   # lance un conteneur nginx en arrière-plan
docker ps                             # liste les conteneurs en cours d'exécution
docker stop web                       # arrête le conteneur "web"
docker rm web                         # supprime le conteneur arrêté
```

`docker ps` est l'équivalent conceptuel d'un `ps` pour les conteneurs : il te montre **ce qui tourne**. Garde ce réflexe — en Kubernetes, `kubectl get pods` jouera un rôle comparable.

### Application admin / cyber

- **Côté admin :** un conteneur, c'est un processus comme un autre **vu depuis l'hôte**. Tu peux d'ailleurs le retrouver dans la liste des processus de la machine. Ce n'est pas une boîte étanche magique : c'est du Linux, avec des barrières.
- **Côté SOC / cyber :** parce que **le noyau est partagé**, la surface d'attaque d'un conteneur **inclut l'hôte**. Une faille noyau exploitée depuis un conteneur peut, dans le pire des cas, toucher la machine entière et les autres conteneurs. C'est pour ça qu'on **durcit** les conteneurs (ne pas tourner en root, limiter les capacités…) — sujet qu'on approfondira au Ch. 26.

En sécurité, on parle de **« container escape »** (évasion de conteneur) lorsqu'une compromission **sort du conteneur** pour atteindre l'hôte ou ses voisins. Ce cours **n'enseigne pas** ces techniques (on reste défensif), mais tu dois comprendre **pourquoi** les mauvaises configurations de conteneurs (privilèges excessifs, root, montages dangereux) **augmentent** ce risque. Tout l'objectif du durcissement, c'est de rendre une telle évasion la plus difficile possible.

🛡️ **Réflexe sécurité :** « conteneur » ne veut **pas** dire « isolé comme une VM ». Quand tu évalues le risque d'un conteneur compromis, pense toujours : *qu'est-ce qu'il partage avec l'hôte et avec ses voisins ?*

### ❌ Erreur classique

> **Traiter un conteneur comme une mini-VM jetable et « forcément sûre ».**

Beaucoup de débutants supposent qu'un conteneur compromis « reste dans sa boîte ». La réalité est plus nuancée : l'isolation est **réelle mais plus fine** qu'une VM. Un conteneur mal configuré (privilégié, en root, avec trop de capacités) **affaiblit** cette barrière. Le réflexe correct : *un conteneur est isolé par défaut, mais cette isolation se mérite et peut être affaiblie par une mauvaise config*.

### Exercices

**Guidé :** Si tu as Docker, lance `docker run -d --name web nginx:1.27`, puis `docker ps`. Repère le **nom de l'image** et l'**ID du conteneur**. Ensuite, lance `docker stop web && docker rm web`. Tu viens de vivre le cycle **image → conteneur → arrêt → suppression**. (Pas de Docker pour l'instant ? Note la séquence ; on la rejouera après l'installation du lab au Ch. 4.)

**Autonome :** Rédige, avec tes propres mots, **3 différences concrètes** entre une VM et un conteneur, et **une conséquence de sécurité** pour chacune. Exemple de départ : « Le conteneur partage le noyau de l'hôte → une faille noyau peut déborder du conteneur. »

**Défi :** Explique pourquoi on peut démarrer **des dizaines de conteneurs** en quelques secondes sur une machine, alors qu'on ne pourrait y lancer que **quelques VM**. Relie ta réponse à **ce que chaque conteneur n'a pas besoin d'embarquer**. (Indice : pense au noyau et à l'OS.)

### ✅ Tu sais maintenant…

- La différence **image** (modèle figé) vs **conteneur** (instance qui tourne).
- Ce qu'un conteneur **isole** (processus, fichiers, réseau) et **comment** (mécanismes du noyau Linux).
- La distinction fondamentale **conteneur vs VM** : le **noyau partagé**.
- Pourquoi le noyau partagé rend le conteneur **léger** mais étend sa **surface d'attaque** à l'hôte.
- Que l'isolation d'un conteneur est **réelle mais affaiblissable** par une mauvaise configuration.

---

## Chapitre 3 — Docker vs Kubernetes : la bascule

### Le minimum à savoir

#### La confusion à dissiper

« Docker ou Kubernetes ? » est une **fausse question**, comme « marteau ou maison ? ». Ils ne jouent pas dans la même catégorie :

- **Docker** (ou un autre moteur de conteneurs) fait tourner **un conteneur** sur **une machine**.
- **Kubernetes** **orchestre beaucoup de conteneurs** sur **beaucoup de machines**.

Kubernetes ne **remplace** pas Docker : il **l'utilise** (ou utilise un moteur équivalent) pour exécuter les conteneurs, et ajoute par-dessus toute la logique de coordination vue au Chapitre 1.

#### La notion de runtime de conteneurs

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

#### Même besoin, deux réponses

| Besoin | Réponse **Docker** (1 machine) | Réponse **Kubernetes** (cluster) |
|--------|-------------------------------|----------------------------------|
| Lancer une appli | `docker run` | Décrire un Pod/Deployment, `kubectl apply` |
| Relancer si ça plante | À ta charge (script, `--restart`) | **Automatique** (réconciliation) |
| 3 copies pour tenir la charge | 3 `docker run` à la main | `replicas: 3`, géré tout seul |
| Mettre à jour sans coupure | À ta charge | **Rolling update** intégré |
| Adresse stable vers l'appli | À ta charge | **Service** intégré |
| Répartir sur plusieurs machines | Impossible avec Docker seul | **C'est précisément son rôle** |

### Très utile en pratique

Tu n'as **rien à taper** dans ce chapitre — c'est un chapitre de **cadrage mental**. Mais retiens cette phrase qui te resservira souvent :

> **Docker, c'est « lance ce conteneur, ici, maintenant ». Kubernetes, c'est « voilà ce que je veux qui tourne en permanence, débrouille-toi pour que ce soit toujours vrai, partout ».**

La première est une **instruction ponctuelle**. La seconde est un **état désiré maintenu dans le temps** — exactement la boucle de réconciliation du préambule.

### Application admin / cyber

- **Côté admin :** en lab, Minikube utilisera souvent Docker **comme support** (le « driver ») pour faire tourner ton mini-cluster. C'est normal que les deux coexistent : Docker fournit la machinerie, Kubernetes l'orchestration.
- **Côté SOC / cyber :** la bascule Docker → Kubernetes **change l'échelle de la surface d'attaque**. Avec Docker, tu raisonnes sur **une machine**. Avec Kubernetes, tu raisonnes sur **un cluster entier piloté par une API** : plus de composants, plus de communications réseau internes, plus d'identités (utilisateurs **et** Pods). Le périmètre à surveiller **explose**.

🛡️ **Réflexe sécurité :** chaque fois que tu passes « d'une machine » à « un cluster », demande-toi *combien de nouvelles portes cela ouvre* : l'API, le réseau inter-Pods, les identités des Pods, les secrets partagés. Le cours va parcourir ces portes une à une.

### ❌ Erreur classique

> **Penser qu'il faut « choisir » entre Docker et Kubernetes, ou que savoir Docker dispense d'apprendre Kubernetes.**

Ce sont des outils **complémentaires** à des niveaux différents. Savoir lancer un conteneur avec Docker **ne** t'apprend **pas** à le maintenir en vie, le répliquer, l'exposer et le mettre à jour sur un parc de machines : ça, c'est le métier de Kubernetes. Inversement, Kubernetes a **besoin** d'un moteur de conteneurs en dessous. Les deux cohabitent.

### Exercices

**Guidé :** Reprends le tableau « Même besoin, deux réponses ». Pour chaque ligne, **dis à voix haute** (ou écris) **pourquoi** la réponse Docker devient ingérable à 50 machines, et pourquoi celle de Kubernetes passe à l'échelle. Tu relies ainsi ce chapitre au Chapitre 1.

**Autonome :** En 5 phrases, explique la différence entre « **lancer** un conteneur » et « **maintenir** un état désiré ». Utilise un exemple concret : une appli qui doit **toujours** tourner en 3 exemplaires, même si un serveur tombe à 4 h du matin.

**Défi :** On dit souvent « Kubernetes a supprimé le support de Docker ». En t'appuyant sur ce chapitre, explique en quelques lignes **pourquoi cette phrase est trompeuse**, et ce qui a réellement changé (indice : *dockershim* vs **images OCI**). Le but : savoir **nuancer** une affirmation qu'on entend partout.

### ✅ Tu sais maintenant…

- Que Docker et Kubernetes **ne sont pas concurrents** : l'un exécute un conteneur sur une machine, l'autre orchestre beaucoup de conteneurs sur beaucoup de machines.
- Ce qu'est un **runtime de conteneurs** (souvent **containerd**) et le rôle « Kubernetes commande, le runtime exécute ».
- Pourquoi « K8s a abandonné Docker » est une phrase **à nuancer** (dockershim ≠ images, qui restent compatibles via OCI).
- Que la bascule vers le cluster **multiplie la surface d'attaque** (API, réseau interne, identités, secrets).

---

## Chapitre 4 — Monter son lab local avec Minikube

### Le minimum à savoir

#### Pourquoi un lab local (et pas le cloud) ?

Pour apprendre, tu as besoin d'un cluster que tu peux **casser, recréer et explorer sans risque ni facture**. Un cluster cloud (EKS, GKE, AKS) coûte de l'argent, ajoute de la complexité d'accès, et te détourne de l'essentiel. **On reste en local.**

> 🧪 **Lunette LAB :** ton cluster local sera **mono-machine** (un seul node qui joue à la fois le control plane et le worker). En production, ces rôles sont sur des machines séparées et redondées. Le lab **simplifie volontairement** — c'est parfait pour apprendre, dangereux à confondre avec la prod.

> **Note pour les curieux :** Minikube est utilisé ici en **mono-node** pour la pédagogie. Il peut aussi simuler certains scénarios plus avancés (multi-node, par exemple), mais **le cours se limite volontairement au mono-node** pour ne pas mélanger *apprentissage de Kubernetes* et *complexité d'infrastructure*.

#### Le choix de ce cours : Minikube

Il existe plusieurs outils pour un cluster local. **Ce cours utilise Minikube par défaut**, pour des raisons pédagogiques :

- **Mono-node simple** : un cluster « qui ressemble à un vrai » sans complexité multi-machines.
- **Commandes claires** (`minikube start`, `minikube status`, `minikube stop`).
- **Add-ons pratiques** : activer un Ingress, un dashboard, etc. en une commande (utile aux Ch. 18 et suivants).
- **Bon pour visualiser** : un tableau de bord graphique disponible si besoin.

> **Tous les exercices, manifests et commandes de ce cours sont testables avec Minikube par défaut.**

#### 🧰 Encadré — Les alternatives (Kind, k3d)

Tu peux réussir le cours avec une autre solution, mais **les commandes d'environnement** (démarrage, Ingress, accès aux Services) **diffèrent**. Si tu choisis une alternative, c'est à toi d'adapter ces parties-là (le cœur Kubernetes, lui, est identique).

| Outil | Idée | Pour qui |
|-------|------|----------|
| **Minikube** | Un mini-cluster (souvent dans une VM ou un conteneur) | **Débutants — recommandé ici** |
| **Kind** | Kubernetes *in Docker* : les nodes sont des conteneurs Docker | Tester/CI, dev de Kubernetes lui-même |
| **k3d** | k3s (Kubernetes allégé) dans Docker | Clusters très légers, multi-node faciles |

> Tu **n'as pas** à les installer tous. Choisis **Minikube**, et garde les autres en tête comme alternatives.

#### Le driver : comment Minikube fait tourner le cluster

Minikube a besoin d'un **driver** pour héberger le cluster (Minikube peut tourner via VM, conteneur ou bare-metal). Sur **Linux**, les deux choix les plus confortables sont :

- **`docker`** : simple si Docker est déjà installé, sans hyperviseur à gérer ni virtualisation à activer. Le cluster tourne dans un conteneur.
- **`kvm2`** : très propre si tu veux un **vrai backend VM Linux** dédié, sans dépendre de Docker.

D'autres drivers existent selon l'OS (`virtualbox`, `hyperkit`, `qemu`, `podman`…). Pour ce cours, on **privilégie `docker` pour la simplicité**, mais **`kvm2` est une excellente alternative sur Linux**.

### Très utile en pratique

#### Installation (vue d'ensemble)

> Les commandes exactes dépendent de ton OS et évoluent. **Les commandes d'installation sont la partie de ce cours la plus susceptible de vieillir.** En cas de doute, la **documentation officielle Kubernetes/Minikube fait foi** — suis-la plutôt qu'un copier-coller daté. Tu as besoin de **deux** outils : `minikube` (le lab) et `kubectl` (pour parler au cluster).

Sur **Linux (x86-64)**, l'installation ressemble à ceci :

```bash
# Minikube (commande officielle actuelle, depuis GitHub)
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

# kubectl (vérifie la version stable courante sur la doc officielle)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```

> **Note de compatibilité `kubectl` ↔ cluster :** `kubectl` doit rester proche de la version du cluster — en pratique, **à plus ou moins une version mineure** du control plane. Avec Minikube en lab, la dernière version stable de `kubectl` fonctionne généralement très bien. Cette règle devient importante en **entreprise**, où le cluster peut être plus ancien que ton poste.

#### Démarrer, vérifier, arrêter

```bash
minikube start                 # démarre le cluster (la première fois est la plus longue)
minikube status                # état du cluster et de ses composants
kubectl version                # versions du client kubectl et du serveur (le cluster)
kubectl cluster-info           # adresse de l'API server : la preuve que kubectl parle à une API
kubectl get nodes              # ton (unique) node doit apparaître en "Ready"
minikube stop                  # arrête le cluster sans le détruire
minikube delete                # ☠️ détruit complètement le cluster (on repart de zéro)
```

`kubectl cluster-info` est précieux pour un débutant : il affiche **l'adresse de l'API server**. C'est la confirmation visuelle que `kubectl` ne « fait pas de magie » — il **parle à une API** sur le réseau (on détaillera ce rôle central de l'API en Partie II).

> 🧰 **Solution de secours — `kubectl` pas encore installé ?** Minikube embarque sa propre version de `kubectl`, utilisable via :
> ```bash
> minikube kubectl -- get nodes
> ```
> Dans ce cours, on installe quand même `kubectl` **directement**, car c'est le **réflexe professionnel** (et c'est la commande que tu utiliseras partout ailleurs).

Choisir explicitement un driver :

```bash
minikube start --driver=docker        # si tu as Docker
minikube start --driver=virtualbox    # si tu préfères une VM
```

#### À quoi ressemble un démarrage réussi

```text
$ minikube start
😄  minikube v1.x.x on Ubuntu 22.04
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes ...
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster
```

```text
$ kubectl get nodes
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   45s   v1.x.x
```

> Vois ce **`Ready`** ? C'est ton premier signe de vie. Le node est prêt à accueillir des applis. On les déploiera en Partie III.

### Application admin / cyber

- **Côté admin :** `minikube start` te donne, en une commande, ce qui prendrait des heures à monter à la main (control plane configuré, réseau interne, stockage de base). C'est **le** terrain d'entraînement.
- **Côté SOC / cyber :** un lab local est aussi le bon endroit pour **rejouer des mauvaises configurations en sécurité**. Tout au long du cours, tu vas **créer volontairement** des situations risquées (Secret en clair, droits trop larges) pour apprendre à les **repérer et corriger** — chose impensable sur un vrai cluster de production.

🛡️ **Réflexe sécurité :** quand `kubectl version` ou `kubectl get nodes` répond, c'est que **ton kubectl est connecté à un cluster**. Cette connexion repose sur le fichier **kubeconfig** (souvent `~/.kube/config`). Retiens dès maintenant : **ce fichier contient des identifiants d'accès au cluster**. On le traitera comme une clé sensible au Ch. 8.

### ❌ Erreur classique

> **Lancer `minikube start` sans ressources suffisantes — puis croire que « Kubernetes est cassé ».**

Si la RAM ou le CPU manquent, le démarrage échoue ou le node reste `NotReady`, et le débutant accuse Kubernetes. Le réflexe correct : vérifier les **prérequis matériel** (section du préambule), lire le **message d'erreur** de `minikube start` (il est souvent explicite), et au besoin allouer plus de ressources :

```bash
minikube start --cpus=2 --memory=2200      # ajuste selon ta machine
```

Autres pièges fréquents : oublier d'installer **kubectl** (tu as le lab mais pas l'outil pour lui parler), ou être sous **WSL** sans Docker Desktop correctement configuré (voir « Limites de WSL » du préambule).

### Exercices

**Guidé :** Installe `minikube` et `kubectl` pour ton système, puis lance la séquence : `minikube start`, `minikube status`, `kubectl get nodes`. Tu dois voir **un node `Ready`**. Si ça échoue, **lis le message d'erreur** et relie-le aux prérequis (RAM, CPU, driver, Docker). Note la commande qui a fini par marcher.

**Autonome :** Démarre le cluster, puis `minikube stop`, puis `minikube start` à nouveau. Observe que **redémarrer** est plus rapide que **créer**. Ensuite, sans paniquer, fais `minikube delete` puis `minikube start` : tu viens de **détruire et recréer** ton lab. Cette aisance à repartir de zéro est exactement ce qui rend un lab **rassurant**.

**Défi :** Trouve **où se trouve ton fichier kubeconfig** sur ta machine (indice : `~/.kube/config` est l'emplacement par défaut) et **ouvre-le** pour l'observer (sans le modifier). Repère qu'il contient l'**adresse du cluster** et des **données d'authentification**. Ne le partage jamais. Tu viens de voir, en vrai, le fichier qui te donne les **clés du cluster** — on en reparlera sérieusement au Ch. 8.

### ✅ Tu sais maintenant…

- **Pourquoi** un lab local plutôt que le cloud pour apprendre (gratuit, jetable, sans risque).
- Pourquoi ce cours choisit **Minikube** comme environnement principal, et l'existence de **Kind/k3d** comme alternatives.
- Ce qu'est un **driver** Minikube (`docker` vs VM) et comment en choisir un.
- Démarrer, vérifier et arrêter ton cluster : `minikube start/status/stop/delete`, `kubectl get nodes`.
- Reconnaître un node **`Ready`** comme premier signe de vie.
- Que la connexion au cluster repose sur le **kubeconfig**, un fichier **sensible** à protéger.

---

### 🚩 Checkpoint — Fin de la Partie I

C'est le moment de vérifier tes **fondations**. Avant de passer à l'anatomie du cluster, tu dois pouvoir :

- [ ] Expliquer en une phrase **pourquoi Kubernetes existe** (orchestration, automatisation de corvées d'admin à grande échelle).
- [ ] Citer au moins **4 promesses** de Kubernetes (self-healing, scaling, scheduling, rolling update, rollback, adresses stables).
- [ ] Énoncer le modèle mental **« état désiré → réconciliation → état réel »** avec tes propres mots.
- [ ] Expliquer la différence **image vs conteneur**.
- [ ] Expliquer pourquoi **un conteneur n'est pas une VM** (noyau partagé) et la **conséquence de sécurité** associée.
- [ ] Dire pourquoi **Docker et Kubernetes ne sont pas concurrents**.
- [ ] Avoir un cluster **Minikube qui démarre**, avec un node **`Ready`** confirmé par `kubectl get nodes`.
- [ ] Savoir que le **kubeconfig** contient des identifiants d'accès au cluster.

> **Si tu coches tout, tu as le socle mental ET le terrain de jeu.** La Partie II va te faire **visiter** ce cluster de l'intérieur — sans rien y construire encore — pour que tu saches *qui fait quoi* avant de commander quoi que ce soit. C'est là que `kube-system` et les premiers **namespaces** entrent en scène.

---
