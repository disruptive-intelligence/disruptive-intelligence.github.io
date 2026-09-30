---
title: 'Chapitre 5 — docker run : lancer son premier conteneur'
source: IT/10_virtualization-containers/Docker.md
note: Docker
up:
- - Docker
  - ../index.md
- - PARTIE II — Premiers PAS AVEC docker
  - index.md
---

## Le minimum à savoir

### La commande centrale, décortiquée

`docker run` est la commande que tu taperas le plus. Elle fait **deux choses d'un coup** : elle **crée** un conteneur à partir d'une image, puis elle le **démarre**. Voici son anatomie :

```
docker run [options]   IMAGE        [commande]
           ▲           ▲            ▲
           comment     à partir de  quoi exécuter dans
           le lancer   quelle image le conteneur (optionnel)
```


Exemple minimal :

```bash
docker run nginx        # lance un conteneur à partir de l'image nginx
```


Si l'image `nginx` n'est pas en local, Docker la **télécharge** d'abord (comme pour `hello-world`), puis lance le conteneur.

### Les options que tu utiliseras tout le temps

| Option | Rôle | Sans elle… |
|--------|------|------------|
| `-d` (*detached*) | Lance en **arrière-plan**, te rend la main | Le terminal reste « bloqué » par le conteneur |
| `-it` | Mode **interactif** + terminal (pour entrer dans le conteneur) | Pas de shell interactif |
| `--name <nom>` | Donne un **nom** lisible au conteneur | Docker en génère un aléatoire (ex. `nostalgic_tesla`) |
| `--rm` | **Supprime** le conteneur dès qu'il s'arrête | Le conteneur arrêté traîne dans `docker ps -a` |
| `-p <hôte>:<conteneur>` | **Publie** un port (vu au Ch. 13) | Le service n'est pas joignable depuis l'hôte |

### Deux façons de lancer, deux usages

**Détaché (`-d`) — pour un service qui tourne en fond :**

```bash
docker run -d --name web nginx
# Docker affiche un long identifiant et te rend la main.
```


**Interactif (`-it`) — pour entrer dans un conteneur et explorer :**

```bash
docker run -it --name labo ubuntu bash
# Tu te retrouves DANS un shell Ubuntu, isolé.
root@a1b2c3:/#  ls
root@a1b2c3:/#  exit      # quitter le shell → le conteneur s'arrête
```


> Le mode interactif est parfait pour **comprendre** : tu es « dans » le conteneur, tu vois son système de fichiers, tu constates qu'il est isolé. Quand tu fais `exit`, le processus principal (`bash`) se termine… et **le conteneur s'arrête avec lui**. Cette dernière phrase est la clé du chapitre suivant.

## Très utile en pratique

```bash
# Un serveur web en arrière-plan, nommé, avec un port publié
docker run -d --name web -p 8080:80 nginx
# → ouvre http://localhost:8080 dans un navigateur : la page nginx s'affiche

# Un conteneur jetable pour tester une commande, supprimé automatiquement
docker run --rm -it alpine sh
/ # echo "je teste, puis je disparais"
/ # exit        # grâce à --rm, le conteneur ne laisse aucune trace
```


`--rm` est ton meilleur ami en lab : il évite l'accumulation de conteneurs arrêtés. Pour un **service** que tu veux garder, ne le mets pas ; pour un **test jetable**, mets-le.

## Application admin / cyber

- **Côté admin :** `docker run` remplace tout un rituel (installer, configurer, démarrer un service) par **une ligne reproductible**. Lancer ≠ installer : tu ne « salis » pas la machine hôte, tout vit dans le conteneur.
- **Côté SOC / cyber :** chaque option de `run` est une **décision de surface d'attaque**. Quelques réflexes posés ici, détaillés plus loin :
  - 🛡️ `-p 8080:80` **publie un port** : ce qui était interne devient **joignable**. À ne faire qu'en conscience (Ch. 13).
  - 🛡️ `-v` / `--mount` **monte des chemins de l'hôte** : puissant et risqué (Ch. 12).
  - 🛡️ `--privileged`, `--user`, `--network host` : changent radicalement l'isolation (Ch. 17).

🔍 **Réflexe diagnostic :** quand un conteneur « ne se comporte pas comme prévu », la cause est souvent **dans les options de `run`** (mauvais port publié, image inattendue, commande surchargée). Relis la ligne `run` avant d'aller chercher plus loin.

## ❌ Erreur classique

> **Oublier `-d` et croire que « le terminal a planté ».**

Quand tu lances `docker run nginx` **sans** `-d`, le conteneur tourne au **premier plan** : ton terminal affiche les logs de nginx et **ne te rend pas la main**. Beaucoup de débutants pensent que c'est figé et ferment tout. En réalité, le conteneur **fonctionne**. Deux réflexes : soit lancer en arrière-plan avec `-d`, soit ouvrir un **second terminal** pour observer. (Et `Ctrl+C` arrête le conteneur au premier plan.)

## Exercices

**Guidé :** Lance `docker run -d --name web -p 8080:80 nginx`, puis ouvre `http://localhost:8080`. Tu dois voir la page d'accueil de nginx. Tu viens de publier un service conteneurisé et d'y accéder depuis l'hôte. Laisse-le tourner, on s'en sert au chapitre suivant.

**Autonome :** Lance un conteneur **interactif** Ubuntu (`docker run -it --name labo ubuntu bash`). Une fois dedans, crée un fichier (`touch /tmp/test`), liste-le, puis `exit`. Relance ensuite `docker run -it ubuntu bash` (nouveau conteneur) et vérifie que `/tmp/test` **n'existe pas**. Explique en une phrase ce que ça démontre sur la **jetabilité** et l'**isolation**.

**Défi :** Trouve la différence concrète entre ces deux commandes en les lançant : `docker run --rm alpine echo coucou` et `docker run alpine echo coucou`. Puis fais `docker ps -a`. Combien de conteneurs `alpine` arrêtés vois-tu, et **pourquoi** ? Tu viens d'observer l'effet de `--rm` — un réflexe d'hygiène essentiel.

## ✅ Tu sais maintenant…

- Que `docker run` **crée puis démarre** un conteneur à partir d'une image.
- L'anatomie `docker run [options] IMAGE [commande]`.
- Les options clés : `-d`, `-it`, `--name`, `--rm`, `-p`.
- La différence entre lancer en **arrière-plan** (service) et en **interactif** (exploration).
- Que quitter le processus principal **arrête le conteneur** (clé du Ch. 6).
- Que chaque option de `run` est une **décision de surface d'attaque**.

---
