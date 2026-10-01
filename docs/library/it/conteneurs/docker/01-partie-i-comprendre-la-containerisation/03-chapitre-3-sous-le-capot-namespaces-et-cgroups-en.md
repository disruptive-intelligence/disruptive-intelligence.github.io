---
title: 'Chapitre 3 — Sous le capot : namespaces et cgroups (en clair)'
source: IT/08 Conteneurs & automatisation/Docker.md
note: Docker
up:
- - Docker
  - ../index.md
- - PARTIE I — Comprendre la containerisation
  - index.md
---

## Le minimum à savoir

### Pourquoi ouvrir le capot ?

Au Ch. 2, on a dit qu'un conteneur est « un processus isolé ». Mais **isolé comment ?** Comprendre ça, ce n'est pas de la curiosité : c'est ce qui te permettra plus tard de comprendre **pourquoi** `--privileged` est dangereux, ou **pourquoi** un conteneur sans limites peut faire tomber une machine. Deux mécanismes du noyau Linux font tout le travail : les **namespaces** et les **cgroups**.

> Attention au piège de vocabulaire : ces **namespaces Linux** n'ont **rien à voir** avec les *namespaces de Kubernetes* (qui sont une autre notion, vue dans le cours K8s). Même mot, concepts différents.

### Les namespaces : des cloisons de visibilité

Un **namespace** Linux limite **ce qu'un processus peut voir**. Le noyau peut donner à un conteneur :

- sa propre **vue des processus** (il ne voit pas ceux des autres conteneurs ni de l'hôte) ;
- son propre **système de fichiers** (ses fichiers à lui) ;
- sa propre **vue réseau** (sa configuration, ses interfaces) ;
- son propre **nom d'hôte**, ses propres utilisateurs, etc.

> Image mentale : les namespaces, ce sont les **cloisons** qui font croire au conteneur qu'il est seul dans l'appartement, alors qu'il partage l'immeuble (le noyau) avec d'autres.

### Les cgroups : des limites de ressources

Un **cgroup** (*control group*) limite **ce qu'un processus peut consommer** : combien de **CPU**, combien de **mémoire**. Sans cgroup, un conteneur pourrait dévorer **toute** la RAM de la machine et faire tomber les voisins.

> Image mentale : si les namespaces sont les cloisons, les cgroups sont les **compteurs** (électricité, eau) qui empêchent un locataire de tout consommer.

### La grande révélation

> **L'isolation d'un conteneur n'est pas magique. C'est du Linux : des namespaces pour cloisonner la visibilité, des cgroups pour limiter les ressources.** Docker ne fait qu'orchestrer ces mécanismes du noyau pour toi.

Et la conséquence directe, côté sécurité : **affaiblir ces mécanismes affaiblit l'isolation**. C'est exactement ce que font les mauvaises configs qu'on verra en Partie VIII.

## Très utile en pratique

On peut **voir** qu'un conteneur n'est qu'un processus de l'hôte. L'idée de la manip (qu'on rejouera après avoir installé Docker au Ch. 4) :

```bash
# Dans un terminal : lancer un conteneur qui tourne
docker run -d --name demo nginx:1.27

# Depuis l'HÔTE : retrouver le(s) processus du conteneur
ps -ef | grep nginx        # le processus nginx du conteneur apparaît côté hôte !
```


Le processus du conteneur est **bien là, sur l'hôte** — simplement isolé par des namespaces. C'est la preuve concrète que « conteneur = processus isolé », pas « petite machine ».

## Application admin / cyber

- **Côté admin :** savoir que namespaces + cgroups = l'isolation t'aide à **diagnostiquer**. Un conteneur qui « voit trop » ou « consomme trop » est presque toujours un problème de namespace ou de cgroup mal réglé.
- **Côté SOC / cyber :** c'est **la clé** pour comprendre les risques de la Partie VIII :
  - 🛡️ **`--privileged`** **casse des cloisons** (namespaces) et redonne au conteneur un accès large à l'hôte.
  - 🛡️ **Absence de cgroup / de limites** = pas de garde-fou de ressources = un conteneur (ou un attaquant qui le contrôle) peut provoquer un **déni de service** sur la machine.

🔍 **Réflexe diagnostic :** quand un conteneur a un comportement « trop puissant » (il voit l'hôte, accède à des périphériques, consomme sans limite), pose-toi la question : *quelles cloisons ont été abaissées ?* La réponse est presque toujours dans les options de lancement.

## ❌ Erreur classique

> **Penser que « le conteneur est isolé » est une garantie binaire, vraie ou fausse.**

L'isolation est **graduée**. Un conteneur par défaut est raisonnablement cloisonné. Mais chaque option qui « ouvre » quelque chose (`--privileged`, montage de chemins hôte, partage de namespaces) **réduit** l'isolation d'un cran. Le réflexe correct : penser l'isolation comme un **curseur**, pas comme un interrupteur.

## Exercices

**Guidé :** Avec tes mots, complète ces deux phrases : « Les namespaces servent à _______ » et « Les cgroups servent à _______ ». Puis donne, pour chacun, **un exemple de ce qui se passe mal** si on les affaiblit ou les retire. (Indices : voir trop / consommer trop.)

**Autonome :** Reprends l'image de l'immeuble (cloisons = namespaces, compteurs = cgroups). Étends-la : qu'est-ce que représenterait, dans cette analogie, le fait de donner à un locataire **la clé de la chaufferie de l'immeuble** ? Relie ta réponse à l'idée de `--privileged` ou de Docker socket. (C'est un teaser de la Partie VIII.)

**Défi :** Sans encore l'exécuter si tu n'as pas Docker, **écris la séquence de commandes** qui permettrait de prouver qu'un conteneur nginx est visible comme un processus sur l'hôte. Explique en une phrase **pourquoi** c'est possible (indice : noyau partagé + namespaces). Tu rejoueras cette manip pour de vrai après le Ch. 4.

## ✅ Tu sais maintenant…

- Que l'isolation d'un conteneur repose sur deux mécanismes du **noyau Linux** : **namespaces** et **cgroups**.
- Que les **namespaces** cloisonnent la **visibilité** (processus, fichiers, réseau…).
- Que les **cgroups** limitent les **ressources** (CPU, RAM).
- Que ces **namespaces Linux** ≠ les **namespaces Kubernetes** (piège de vocabulaire).
- Que l'isolation est **graduée** : l'affaiblir (privilèges, montages) augmente la surface d'attaque.
- Pourquoi un conteneur est **visible comme un processus** sur l'hôte.

---

## 🚩 Checkpoint — Fin de la Partie I

C'est le moment de vérifier tes **fondations**. Avant de mettre les mains dans Docker, tu dois pouvoir :

- [ ] Expliquer en une phrase **pourquoi la conteneurisation existe** (enfer des dépendances, « ça marche sur ma machine »).
- [ ] Énoncer le modèle mental **isolation / reproductibilité / jetabilité** avec tes propres mots.
- [ ] Expliquer la différence **image vs conteneur** (recette vs plat).
- [ ] Expliquer pourquoi **un conteneur est un processus isolé**, pas une machine.
- [ ] Expliquer pourquoi **un conteneur n'est pas une VM** (noyau partagé) et la **conséquence de sécurité** (container escape).
- [ ] Dire à quoi servent les **namespaces** (cloisonner la visibilité) et les **cgroups** (limiter les ressources).
- [ ] Comprendre que l'isolation est **graduée** et qu'une mauvaise config peut l'affaiblir.

> **Si tu coches tout, tu as le socle mental.** La Partie II va te faire **installer Docker** et **lancer tes premiers conteneurs** — enfin de la pratique. On commencera par comprendre *qui parle à qui* (CLI, daemon, socket), parce que c'est là que se cache le premier grand réflexe de sécurité Docker : **le daemon tourne en root**.

---
---
---
