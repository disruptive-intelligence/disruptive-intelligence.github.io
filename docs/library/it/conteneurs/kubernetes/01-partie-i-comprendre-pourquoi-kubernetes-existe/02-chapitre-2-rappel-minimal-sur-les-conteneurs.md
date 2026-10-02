---
title: Chapitre 2 — Rappel minimal sur les conteneurs
source: IT/08 Conteneurs & automatisation/Conteneurs/Kubernetes.md
note: Kubernetes
up:
- - Kubernetes
  - ../index.md
- - PARTIE I — Comprendre pourquoi Kubernetes existe
  - index.md
---

## Le minimum à savoir

### Pourquoi ce rappel ?

Kubernetes orchestre des **conteneurs**. Si la notion est floue, tout le reste le sera. Ce chapitre **nivelle** le prérequis : pas besoin d'être expert Docker, juste de comprendre **ce qu'est** un conteneur et **ce qu'il partage** avec la machine qui l'héberge (ce dernier point est crucial côté sécurité).

### Image vs conteneur

Deux mots qu'on confond souvent :

- Une **image** est un **modèle figé** : une appli + ses dépendances + sa config minimale, empaquetées. C'est un fichier inerte, comme un plan.
- Un **conteneur** est une **instance en cours d'exécution** de cette image. C'est le plan **devenu réalité** et qui tourne.

> Analogie : l'**image** est la recette, le **conteneur** est le plat cuisiné. Avec une seule recette, tu peux cuisiner **plusieurs** plats identiques.

```bash
# Une image (modèle figé) :        nginx:1.27
# Un conteneur (instance qui tourne) : lancé à partir de nginx:1.27
docker run nginx:1.27       # crée et démarre UN conteneur à partir de l'image
```


### Ce qu'un conteneur isole

Un conteneur fait croire à l'application qu'elle est **seule au monde** :

- Sa propre **vue des processus** (il ne voit pas ceux des autres).
- Son propre **système de fichiers** (ses fichiers à lui).
- Sa propre **vue réseau** (sa configuration).

Mais cette isolation est une **illusion soigneusement construite par le noyau Linux** (via des mécanismes appelés *namespaces* et *cgroups* — rien à voir avec les namespaces Kubernetes, attention au mot identique).

### LE point clé : un conteneur n'est PAS une VM

C'est **la** distinction à intégrer, surtout côté sécurité :

| | Machine virtuelle (VM) | Conteneur |
|---|------------------------|-----------|
| Contient | Un OS complet (son propre noyau) | Juste l'appli + ses dépendances |
| Noyau | **Le sien**, isolé | **Celui de l'hôte**, partagé |
| Taille | Gigaoctets | Mégaoctets |
| Démarrage | Dizaines de secondes | Quasi instantané |
| Isolation | **Forte** (noyau séparé) | **Plus légère** (noyau partagé) |

> **Le conteneur partage le noyau de la machine hôte.** Il ne transporte pas son propre système d'exploitation. C'est ce qui le rend léger et rapide… **et c'est aussi sa principale limite de sécurité.**

## Très utile en pratique

```bash
docker run -d --name web nginx:1.27   # lance un conteneur nginx en arrière-plan
docker ps                             # liste les conteneurs en cours d'exécution
docker stop web                       # arrête le conteneur "web"
docker rm web                         # supprime le conteneur arrêté
```


`docker ps` est l'équivalent conceptuel d'un `ps` pour les conteneurs : il te montre **ce qui tourne**. Garde ce réflexe — en Kubernetes, `kubectl get pods` jouera un rôle comparable.

## Application admin / cyber

- **Côté admin :** un conteneur, c'est un processus comme un autre **vu depuis l'hôte**. Tu peux d'ailleurs le retrouver dans la liste des processus de la machine. Ce n'est pas une boîte étanche magique : c'est du Linux, avec des barrières.
- **Côté SOC / cyber :** parce que **le noyau est partagé**, la surface d'attaque d'un conteneur **inclut l'hôte**. Une faille noyau exploitée depuis un conteneur peut, dans le pire des cas, toucher la machine entière et les autres conteneurs. C'est pour ça qu'on **durcit** les conteneurs (ne pas tourner en root, limiter les capacités…) — sujet qu'on approfondira au Ch. 26.

En sécurité, on parle de **« container escape »** (évasion de conteneur) lorsqu'une compromission **sort du conteneur** pour atteindre l'hôte ou ses voisins. Ce cours **n'enseigne pas** ces techniques (on reste défensif), mais tu dois comprendre **pourquoi** les mauvaises configurations de conteneurs (privilèges excessifs, root, montages dangereux) **augmentent** ce risque. Tout l'objectif du durcissement, c'est de rendre une telle évasion la plus difficile possible.

🛡️ **Réflexe sécurité :** « conteneur » ne veut **pas** dire « isolé comme une VM ». Quand tu évalues le risque d'un conteneur compromis, pense toujours : *qu'est-ce qu'il partage avec l'hôte et avec ses voisins ?*

## ❌ Erreur classique

> **Traiter un conteneur comme une mini-VM jetable et « forcément sûre ».**

Beaucoup de débutants supposent qu'un conteneur compromis « reste dans sa boîte ». La réalité est plus nuancée : l'isolation est **réelle mais plus fine** qu'une VM. Un conteneur mal configuré (privilégié, en root, avec trop de capacités) **affaiblit** cette barrière. Le réflexe correct : *un conteneur est isolé par défaut, mais cette isolation se mérite et peut être affaiblie par une mauvaise config*.

## Exercices

**Guidé :** Si tu as Docker, lance `docker run -d --name web nginx:1.27`, puis `docker ps`. Repère le **nom de l'image** et l'**ID du conteneur**. Ensuite, lance `docker stop web && docker rm web`. Tu viens de vivre le cycle **image → conteneur → arrêt → suppression**. (Pas de Docker pour l'instant ? Note la séquence ; on la rejouera après l'installation du lab au Ch. 4.)

**Autonome :** Rédige, avec tes propres mots, **3 différences concrètes** entre une VM et un conteneur, et **une conséquence de sécurité** pour chacune. Exemple de départ : « Le conteneur partage le noyau de l'hôte → une faille noyau peut déborder du conteneur. »

**Défi :** Explique pourquoi on peut démarrer **des dizaines de conteneurs** en quelques secondes sur une machine, alors qu'on ne pourrait y lancer que **quelques VM**. Relie ta réponse à **ce que chaque conteneur n'a pas besoin d'embarquer**. (Indice : pense au noyau et à l'OS.)

## ✅ Tu sais maintenant…

- La différence **image** (modèle figé) vs **conteneur** (instance qui tourne).
- Ce qu'un conteneur **isole** (processus, fichiers, réseau) et **comment** (mécanismes du noyau Linux).
- La distinction fondamentale **conteneur vs VM** : le **noyau partagé**.
- Pourquoi le noyau partagé rend le conteneur **léger** mais étend sa **surface d'attaque** à l'hôte.
- Que l'isolation d'un conteneur est **réelle mais affaiblissable** par une mauvaise configuration.

---
