---
title: Chapitre 2 — VM vs conteneur, image vs conteneur, processus
source: IT/10_virtualization-containers/Docker.md
note: Docker
up:
- - Docker
  - ../index.md
- - PARTIE I — Comprendre la containerisation
  - index.md
---

## Le minimum à savoir

### Les 4 mots que tout le monde confond

Ce chapitre pose le vocabulaire qui piège **tous** les débutants. Prends ton temps ici : si ces 4 mots sont clairs, tout le reste du cours coule.

### Image vs conteneur

- Une **image** est un **modèle figé** : l'application + ses dépendances, empaquetées. C'est un fichier inerte, comme un plan ou une recette.
- Un **conteneur** est une **instance en cours d'exécution** de cette image. C'est le plan **devenu réalité** qui tourne.

> Analogie : l'**image** est la recette, le **conteneur** est le plat cuisiné. Avec une seule recette, tu peux cuisiner **plusieurs** plats identiques. De même, une image peut lancer **plusieurs** conteneurs identiques.

```
   IMAGE (figée)                CONTENEURS (qui tournent)
   nginx:1.27       ───run──▶   conteneur web-1
                    ───run──▶   conteneur web-2
                    ───run──▶   conteneur web-3
```


### Un conteneur EST un processus

Voici le point que personne ne te dit assez tôt : **un conteneur n'est pas une « petite machine ». C'est un processus** (ou un petit groupe de processus) qui tourne sur ton hôte, mais **isolé** pour qu'il croie être seul. Tu peux d'ailleurs le **voir** dans la liste des processus de la machine hôte (on le fera au Ch. 3).

### LE point clé : un conteneur n'est PAS une VM

C'est **la** distinction à intégrer, surtout côté sécurité :

| | Machine virtuelle (VM) | Conteneur |
|---|------------------------|-----------|
| Contient | Un OS complet (son propre noyau) | Juste l'appli + ses dépendances |
| Noyau | **Le sien**, isolé | **Celui de l'hôte**, partagé |
| Taille | Gigaoctets | Mégaoctets |
| Démarrage | Dizaines de secondes | Quasi instantané |
| Isolation | **Forte** (noyau séparé) | **Plus légère** (noyau partagé) |

```
   MACHINES VIRTUELLES                CONTENEURS
   ┌─────────┐ ┌─────────┐            ┌─────────┐ ┌─────────┐
   │  App A  │ │  App B  │            │  App A  │ │  App B  │
   │ OS + 🐧 │ │ OS + 🐧 │            │  deps   │ │  deps   │
   │ (noyau) │ │ (noyau) │            └─────────┘ └─────────┘
   └─────────┘ └─────────┘            ┌───────────────────────┐
   ┌───────────────────────┐         │   🐧 NOYAU PARTAGÉ    │
   │     Hyperviseur       │         │   (un seul, l'hôte)   │
   └───────────────────────┘         └───────────────────────┘
   Chaque VM = son noyau              Tous les conteneurs = même noyau
```


> **Le conteneur partage le noyau de la machine hôte.** Il ne transporte pas son propre système d'exploitation complet. C'est ce qui le rend léger et rapide… **et c'est aussi sa principale limite de sécurité.**

## Très utile en pratique

Garde cette grille de lecture, tu t'en serviras tout le cours :

- On **construit** ou on **télécharge** une **image**.
- On **lance** un **conteneur** à partir d'une image.
- Le conteneur est un **processus isolé**, pas une machine.
- Plusieurs conteneurs **partagent le noyau** de l'hôte.

## Application admin / cyber

- **Côté admin :** comprendre qu'un conteneur est « juste » un processus isolé démystifie tout. Pas de magie : des mécanismes Linux que tu connais déjà en partie (processus, droits, réseau).
- **Côté SOC / cyber :** parce que **le noyau est partagé**, la surface d'attaque d'un conteneur **inclut l'hôte**. Une faille du noyau exploitée depuis un conteneur peut, dans le pire des cas, toucher la machine entière et les autres conteneurs.

En sécurité, on parle de **« container escape »** (évasion de conteneur) lorsqu'une compromission **sort du conteneur** pour atteindre l'hôte ou ses voisins. Ce cours **n'enseigne pas** ces techniques (on reste défensif), mais tu dois comprendre **pourquoi** les mauvaises configurations (conteneur en root, `--privileged`, montages dangereux) **augmentent** ce risque. Tout l'objectif du durcissement (Partie VIII) sera de rendre une telle évasion la plus difficile possible.

🛡️ **Réflexe sécurité :** « conteneur » ne veut **pas** dire « isolé comme une VM ». Quand tu évalues le risque d'un conteneur compromis, pense toujours : *qu'est-ce qu'il partage avec l'hôte et avec ses voisins ?* C'est **la** question défensive de tout le cours.

## ❌ Erreur classique

> **Traiter un conteneur comme une mini-VM jetable et « forcément sûre ».**

Beaucoup de débutants supposent qu'un conteneur compromis « reste dans sa boîte ». La réalité est plus nuancée : l'isolation est **réelle mais plus fine** qu'une VM. Un conteneur mal configuré (privilégié, en root, avec des montages dangereux) **affaiblit** cette barrière. Le réflexe correct : *un conteneur est isolé par défaut, mais cette isolation se mérite et peut être affaiblie par une mauvaise config*.

## Exercices

**Guidé :** Avec tes propres mots, écris la différence entre une **image** et un **conteneur** en **une seule phrase** qui contient les mots « recette » et « plat ». Puis fais la même chose pour **VM vs conteneur** avec le mot « noyau ». Ces deux phrases sont ton ancrage pour tout le cours.

**Autonome :** Dessine (à la main, c'est très bien) deux schémas : à gauche, trois VM ; à droite, trois conteneurs. Fais clairement apparaître **où se trouve le noyau** dans chaque cas. Tu dois « voir » pourquoi le conteneur est plus léger.

**Défi :** Rédige **3 différences concrètes** entre VM et conteneur, et pour chacune une **conséquence de sécurité**. Exemple de départ : « Le conteneur partage le noyau de l'hôte → une faille noyau peut permettre une évasion vers l'hôte. » C'est exactement le type de raisonnement attendu d'un profil cyber.

## ✅ Tu sais maintenant…

- La différence **image** (modèle figé) vs **conteneur** (instance qui tourne).
- Qu'un conteneur **est un processus isolé**, pas une machine.
- La distinction fondamentale **conteneur vs VM** : le **noyau partagé**.
- Pourquoi le noyau partagé rend le conteneur **léger** mais étend sa **surface d'attaque** à l'hôte.
- La notion défensive de **container escape** et le réflexe « qu'est-ce qui est partagé avec l'hôte ? ».

---
