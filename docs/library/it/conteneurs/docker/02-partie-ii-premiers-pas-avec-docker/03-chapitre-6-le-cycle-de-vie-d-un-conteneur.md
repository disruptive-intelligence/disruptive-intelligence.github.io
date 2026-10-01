---
title: Chapitre 6 — Le cycle de vie d'un conteneur
source: IT/08 Conteneurs & automatisation/Docker.md
note: Docker
up:
- - Docker
  - ../index.md
- - PARTIE II — Premiers pas avec Docker
  - index.md
---

## Le minimum à savoir

### Un conteneur a des états, comme un processus

Un conteneur n'est pas « allumé ou éteint ». Il traverse une **suite d'états** qu'il faut savoir lire, car c'est la base de tout diagnostic :

```
   docker run
       │
       ▼
   [Created] ──start──▶ [Running] ──stop──▶ [Exited/Stopped]
                            │                      │
                         (le process               └──start──▶ [Running]
                          principal                │
                          se termine)              └──rm──▶ [Supprimé] (n'existe plus)
                            │
                            ▼
                        [Exited]
```


- **Created** : le conteneur existe mais n'a pas démarré (rare en pratique, créé sans lancer).
- **Running** : il tourne, son processus principal est actif.
- **Exited / Stopped** : il s'est arrêté — soit parce qu'on l'a stoppé, soit parce que **son processus principal s'est terminé**.
- **Supprimé** : retiré de la machine (`rm`). Il n'apparaît plus nulle part.

### LE point qui déroute tous les débutants

> **Un conteneur vit tant que son processus principal vit.** Quand ce processus se termine, le conteneur passe en **Exited**. Ce n'est **pas** une panne : c'est le comportement normal.

C'est pour ça que `docker run hello-world` « disparaît » : son unique tâche (afficher un message) finit, donc le conteneur finit. Et c'est pour ça qu'un `docker run -it ubuntu bash` s'arrête quand tu fais `exit` : tu as terminé le processus `bash`.

### Voir les conteneurs : `ps` et `ps -a`

```bash
docker ps        # conteneurs EN COURS (Running) uniquement
docker ps -a     # TOUS les conteneurs, y compris les Exited
```


> **Piège classique :** `docker ps` ne montre **pas** les conteneurs arrêtés. Si « ton conteneur a disparu », il est probablement juste **Exited** — `docker ps -a` le retrouve.

## Très utile en pratique

```bash
docker ps -a                    # voir l'état de tous les conteneurs

docker stop web                 # arrêt propre (laisse le temps au process de finir)
docker start web                # redémarre un conteneur arrêté (il garde son nom et sa config)
docker restart web              # stop + start enchaînés

docker rm web                   # supprime un conteneur ARRÊTÉ
docker rm -f web                # ☠️ force la suppression même s'il TOURNE (pas de confirmation)
```


Lire la sortie de `docker ps -a` :

```text
CONTAINER ID   IMAGE     COMMAND                  STATUS                     NAMES
a1b2c3d4e5f6   nginx     "/docker-entrypoint.…"   Up 3 minutes               web
f6e5d4c3b2a1   ubuntu    "bash"                   Exited (0) 2 minutes ago   labo
```


La colonne **STATUS** est ta boussole : `Up …` = Running, `Exited (0) …` = arrêté proprement (code 0 = succès), `Exited (1) …` ou un autre code = arrêté sur **erreur** (un indice de diagnostic, qu'on exploitera au Ch. 7).

## Application admin / cyber

- **Côté admin :** la distinction `stop` (arrêt propre) / `rm` (suppression) / `rm -f` (suppression forcée) est exactement parallèle à ce que tu connais avec les services et processus Linux. `stop` envoie un signal d'arrêt poli ; au-delà d'un délai, le conteneur est arrêté plus fermement.
- **Côté SOC / cyber :** savoir lister **tous** les conteneurs (`-a`), y compris arrêtés, est un **réflexe d'investigation**. Un conteneur **Exited** peut être la trace d'une activité passée (un outil lancé puis arrêté). Le **code de sortie** (`Exited (N)`) et l'**ancienneté** racontent une histoire.

🔍 **Réflexe diagnostic :** un conteneur « qui ne marche pas » est presque toujours dans un de ces deux cas : soit il est **Exited** (et le code de sortie + les logs disent pourquoi — Ch. 7), soit il **redémarre en boucle** (mauvaise config). `docker ps -a` est **toujours** ta première commande.

## ❌ Erreur classique

> **Croire qu'un conteneur Exited est « cassé », alors qu'il a simplement fini son travail.**

Le cas le plus fréquent : on lance une image qui exécute une tâche courte (un script, une commande) et on s'étonne qu'« elle ne reste pas allumée ». Mais un conteneur **n'a pas vocation à rester en vie sans raison** : si son processus principal se termine avec succès (`Exited (0)`), tout va bien. Le réflexe correct : lire le **STATUS** et le **code de sortie** avant de parler de panne. Un `Exited (0)` n'est pas un problème ; un `Exited (1)` mérite un coup d'œil aux logs.

## Exercices

**Guidé :** Reprends ton conteneur `web` (nginx) du Ch. 5. Lance `docker ps` (il apparaît), puis `docker stop web` et `docker ps` (il a disparu de la liste). Maintenant `docker ps -a` : il est là, en **Exited**. Fais `docker start web`, vérifie qu'il est de nouveau **Up**. Tu viens de parcourir le cycle Running → Stopped → Running.

**Autonome :** Lance `docker run --name court alpine echo "fini"`. Observe qu'il s'arrête immédiatement. Avec `docker ps -a`, lis son **STATUS** : quel code de sortie ? Que signifie-t-il ? Puis nettoie avec `docker rm court`. Écris en une phrase pourquoi ce conteneur « ne reste pas allumé ».

**Défi :** Crée volontairement un conteneur qui s'arrête sur **erreur** : `docker run --name casse alpine sh -c "exit 3"`. Lis son STATUS avec `docker ps -a` : tu dois voir `Exited (3)`. Explique en quoi ce **code de sortie non nul** est un **indice de diagnostic** précieux, et fais le lien avec ce qu'on va apprendre au chapitre suivant (logs, inspect). Nettoie ensuite avec `docker rm casse`.

## ✅ Tu sais maintenant…

- Les états d'un conteneur : **Created → Running → Exited → (Supprimé)**.
- Que **le conteneur vit tant que son processus principal vit** (et qu'un arrêt n'est pas forcément une panne).
- La différence cruciale entre `docker ps` (Running) et `docker ps -a` (**tous**).
- Les commandes du cycle de vie : `stop`, `start`, `restart`, `rm`, `rm -f`.
- Lire la colonne **STATUS** et le **code de sortie** comme premiers indices de diagnostic.
- Que lister **tous** les conteneurs est un réflexe d'investigation côté SOC.

---

## 🚩 Checkpoint — Fin de la Partie II

Tu as maintenant **les mains dans Docker**. Avant de passer au diagnostic approfondi, tu dois pouvoir :

- [ ] Expliquer l'architecture **CLI → daemon → conteneurs** et le rôle du **socket**.
- [ ] Dire pourquoi **le daemon = root** et **le groupe `docker` ≈ root**.
- [ ] Vérifier une installation (`docker version`, `docker info`, `hello-world`) et diagnostiquer « cannot connect to the daemon ».
- [ ] Lancer un conteneur en **arrière-plan** (`-d`) et en **interactif** (`-it`), le **nommer**, **publier un port**, utiliser `--rm`.
- [ ] Lire les états d'un conteneur et la colonne **STATUS** (`docker ps` vs `docker ps -a`).
- [ ] Utiliser `stop`, `start`, `restart`, `rm`, et savoir que `rm -f` ne demande **aucune confirmation**.
- [ ] Comprendre qu'un conteneur **Exited (0)** n'est pas une panne.

> **🧩 Mini-projet — « Lancer, observer, nettoyer ».**
> 1. Lance **trois** conteneurs : un nginx nommé `web` en arrière-plan avec port publié, un `alpine` interactif que tu explores puis quittes, et un conteneur jetable avec `--rm`.
> 2. Avec `docker ps -a`, dresse l'inventaire : lesquels sont **Up**, lesquels **Exited**, lequel a **disparu** (et pourquoi).
> 3. Arrête proprement `web`, puis **nettoie** tout ce qui traîne (`stop` puis `rm`), en faisant **systématiquement un `docker ps -a` avant chaque `rm`** pour vérifier ce que tu supprimes.
> Objectif : intégrer le cycle complet **lancer → observer → arrêter → nettoyer**, avec le bon réflexe « regarder avant de supprimer ».

> **La suite :** en Partie III, on installe les **réflexes de diagnostic** — `logs`, `exec`, `inspect`, `stats`, `cp`, `events` — pour ne plus jamais être bloqué devant un conteneur qui « ne marche pas ». C'est ce qui te rend vraiment **autonome**.

---
