---
title: PARTIE 0 — INTRODUCTION
source: IT/10_virtualization-containers/Ansible.md
note: Ansible
chapter: 1
chapters: 13
---

> **Objectif de la partie :** comprendre à quoi sert Ansible et dans quel cas on l'utilise — **sans rien installer**. On pose juste les idées.

---


## Chapitre 0.1 — Pourquoi Ansible existe

### Le minimum à savoir

Imagine que tu administres **un** serveur Linux. Tu te connectes en SSH, tu installes un paquet, tu modifies un fichier de configuration, tu redémarres un service. Cinq minutes, c'est réglé.

Maintenant, imagine que tu as **vingt** serveurs. La même tâche, vingt fois. À la main. Tu te connectes, tu tapes, tu recommences. C'est **long**, c'est **fastidieux**, et surtout : à la machine n°13, tu oublies une étape. Personne ne le remarque. Trois mois plus tard, cette machine se comporte différemment des autres, et personne ne sait pourquoi.

Ce problème porte un nom : la **dérive de configuration**. Des machines censées être identiques qui **divergent** lentement, parce qu'elles ont été modifiées à la main, à des moments différents, par des personnes différentes.

**Ansible existe pour résoudre exactement ça.** Au lieu de répéter les mêmes gestes machine par machine, tu **décris une fois** ce que tu veux, et Ansible l'applique à **toutes** les machines, de façon **identique** et **rejouable**.

> **En une phrase :** Ansible automatise l'administration de plusieurs machines, pour que tu ne répètes pas les mêmes commandes une par une, et pour que tes machines restent **cohérentes** dans le temps.

### Très utile en pratique

Voici les corvées d'admin que tu fais (ou ferais) à la main, et ce qu'Ansible change :

| À la main | Avec Ansible |
|-----------|--------------|
| Se connecter à chaque serveur pour installer un paquet | Une description, appliquée à toutes les machines |
| Refaire la même config sur 20 serveurs | Le même playbook, rejoué partout |
| Oublier une étape sur une machine | L'état décrit est appliqué **partout** pareil |
| Ne plus savoir quelles machines sont à jour | Rejouer pour **vérifier** et **corriger** d'un coup |

Tu n'as **rien à taper** dans ce chapitre. C'est de la mise en place mentale.

### Exemple simple

Sans Ansible, pour installer `htop` sur trois serveurs, tu ferais :

```bash
ssh serveur1     # puis : sudo apt install htop, puis exit
ssh serveur2     # puis : sudo apt install htop, puis exit
ssh serveur3     # puis : sudo apt install htop, puis exit
```

Avec Ansible, tu écriras **une seule** instruction qui s'applique aux trois d'un coup. Et si `htop` est déjà installé sur le serveur 2, Ansible le **constatera** et ne fera rien sur celui-là. C'est ça, l'idée de départ.

### ❌ Erreur classique

> **Croire qu'Ansible sert juste à « lancer une commande à distance plus vite ».**

C'est un raccourci trompeur. Lancer une commande sur plusieurs machines, une boucle SSH le fait aussi. Ce qu'Ansible apporte en plus, c'est l'**état souhaité** et l'**idempotence** : tu décris un **résultat** que tu peux **rejouer sans risque**, pas une commande à exécuter une fois. On verra la différence concrète très vite.

### Exercices

#### Guidé
Sur une feuille (ou un fichier texte), écris **3 tâches** que tu fais ou ferais à la main pour administrer un serveur Linux (par exemple : « installer un paquet », « créer un utilisateur », « démarrer un service »). Pour chacune, imagine que tu doives la faire sur **10 machines** : note ce qui devient pénible ou risqué.

#### Autonome
Décris en quelques lignes une situation (vécue ou imaginée) où **deux machines censées être identiques** se sont mises à se comporter différemment. Qu'est-ce qui a divergé ? Comment l'aurais-tu remarqué ?

#### Défi
Explique à un proche **non technique**, en 4-5 phrases, ce que fait Ansible — **sans** utiliser les mots « playbook » ni « serveur ». Utilise une image (une recette qu'on rejoue à l'identique, un chef qui donne les mêmes instructions à toute une brigade…).

### ✅ Tu sais maintenant…

- **Pourquoi** Ansible existe : éviter de répéter les tâches d'admin machine par machine.
- Ce qu'est la **dérive de configuration** (des machines identiques qui divergent).
- Qu'Ansible applique un **état souhaité**, de façon **identique** et **rejouable**.
- Qu'Ansible n'est **pas** seulement « lancer des commandes à distance ».

---


## Chapitre 0.2 — L'idée d'Ansible : l'état souhaité

### Le minimum à savoir

Voici la différence la plus importante à comprendre, et elle est simple.

Un **script** (en Bash, par exemple) est une **liste d'ordres** : « fais ceci, puis cela ». Il exécute, point. Si tu le relances, il refait tout — même ce qui était déjà fait. Et parfois, ça casse (par exemple, créer un utilisateur qui existe déjà provoque une erreur).

Ansible fonctionne autrement. Tu décris un **état souhaité** : « cet utilisateur **doit exister** », « ce paquet **doit être installé** », « ce service **doit tourner** ». Ansible regarde la machine, **compare** avec ce que tu as demandé, et n'agit **que** s'il y a un écart.

```
   SCRIPT (impératif)              ANSIBLE (état souhaité)
   "crée l'utilisateur bob"        "l'utilisateur bob doit exister"
   → erreur si bob existe déjà     → bob existe ? rien à faire.
                                     bob absent ? je le crée.
```

> **L'idée clé :** tu ne dis pas **comment** faire étape par étape, tu dis **ce que tu veux obtenir**. Ansible se charge d'y arriver, et de **ne rien refaire inutilement**.

### Très utile en pratique

Cette façon de penser change tout :

- Tu peux **rejouer** une description autant de fois que tu veux, sans crainte.
- Tu peux l'appliquer à **une** machine ou à **cent**, c'est la même description.
- Si une machine a **dévié**, rejouer la description la **ramène** à l'état voulu.

C'est pour ça qu'on dit qu'Ansible **maintient** un état, alors qu'un script **exécute** des ordres.

### Exemple simple

Une instruction Ansible typique ressemble à ça (ne t'inquiète pas de la syntaxe, on l'apprendra) :

```yaml
- name: S'assurer que nginx est installé
  ansible.builtin.apt:
    name: nginx
    state: present       # ← "present" = l'état souhaité : nginx DOIT être là
```

Remarque le mot **`present`** : tu ne dis pas « installe nginx », tu dis « nginx **doit être présent** ». Si c'est déjà le cas, Ansible ne fait rien. C'est subtil, mais c'est **toute** la philosophie.

### ❌ Erreur classique

> **Penser en « ordres à exécuter » au lieu de « résultat à obtenir ».**

Un débutant venant des scripts a le réflexe d'écrire « lance cette commande ». Ansible préfère « assure-toi que cet état est atteint ». Le réflexe correct : pour chaque tâche, demande-toi **« quel résultat je veux ? »** plutôt que **« quelle commande je tape ? »**. C'est ce changement d'état d'esprit qui rend Ansible puissant.

### Exercices

#### Guidé
Reformule ces trois ordres en **états souhaités** :
- « installe le paquet git » → « le paquet git doit… »
- « démarre le service ssh » → « le service ssh doit… »
- « crée le dossier /opt/app » → « le dossier /opt/app doit… »

#### Autonome
Explique avec tes mots la différence entre « exécuter une commande » et « décrire un état souhaité ». Donne un exemple où **relancer** un script poserait problème, mais où **relancer** une description Ansible ne poserait aucun problème.

#### Défi
Le mot `state: present` a un opposé : `state: absent`. Sans encore connaître la syntaxe, devine ce que voudrait dire une tâche avec `state: absent` pour un paquet. En quoi est-ce, là aussi, un **état souhaité** plutôt qu'un ordre ?

### ✅ Tu sais maintenant…

- La différence entre un **script** (liste d'ordres) et Ansible (**état souhaité**).
- Que tu décris **ce que tu veux obtenir**, pas **comment** le faire étape par étape.
- Que cette approche rend les actions **rejouables** sans risque.
- Le sens d'un mot comme **`present`** (l'état voulu, pas l'ordre « installe »).

---


## Chapitre 0.3 — L'idempotence en une image

### Le minimum à savoir

Le mot fait peur, l'idée est simple. **Idempotent** veut dire : *qu'on l'applique une fois ou dix fois, le résultat est le même, et rejouer ne casse rien.*

Reprends l'idée de l'état souhaité. Si tu demandes « nginx doit être installé » :

- **1ʳᵉ fois** : nginx n'est pas là → Ansible l'installe. Il signale qu'il a **changé** quelque chose.
- **2ᵉ fois** : nginx est déjà là → Ansible **ne fait rien**. Il signale que tout était déjà **ok**.
- **3ᵉ, 4ᵉ, 100ᵉ fois** : toujours `ok`. Rien ne bouge.

```
   1er run :  [ nginx absent ]  →  Ansible installe  →  CHANGED  (j'ai agi)
   2e run :   [ nginx présent ] →  Ansible vérifie   →  OK       (rien à faire)
   3e run :   [ nginx présent ] →  Ansible vérifie   →  OK       (rien à faire)
```

> **C'est ça, l'idempotence :** tu peux rejouer une description Ansible autant de fois que tu veux. Elle n'agit **que** s'il y a un écart à corriger. Un script Bash avec `apt install`, lui, relancerait l'installation à chaque fois.

### Très utile en pratique

L'idempotence te donne une **tranquillité** énorme :

- Tu peux relancer un playbook **sans crainte** de tout casser ou dupliquer.
- Tu peux l'utiliser pour **vérifier** : si tout est `ok`, le parc est conforme ; si quelque chose passe en `changed`, c'est qu'une machine avait **dévié** et qu'Ansible l'a corrigée.

On reviendra **vraiment** dessus en Partie 3, avec une démonstration que tu feras toi-même. Pour l'instant, garde juste l'image.

### Exemple simple

Tu lances deux fois de suite la même description « htop doit être installé » :

```text
1er lancement →  changed   (Ansible a installé htop)
2e lancement →  ok         (htop était déjà là, rien à faire)
```

Si tu voyais `changed` **à chaque** relance, ce serait le signe que quelque chose n'est **pas** idempotent — un point qu'on apprendra à repérer.

### ❌ Erreur classique

> **Confondre « idempotent » avec « qui ne fait jamais rien ».**

Idempotent ne veut **pas** dire « passif ». Ansible **agit** quand il le faut (1ʳᵉ fois, ou quand une machine a dévié), et **se retient** quand tout est déjà bon. Le réflexe correct : voir l'idempotence comme « **agir juste ce qu'il faut, ni plus ni moins** ».

### Exercices

#### Guidé
Pour chacune de ces actions, dis si elle est naturellement **idempotente** (rejouer ne change rien si c'est déjà fait) ou non :
- « s'assurer qu'un fichier contient une ligne précise »
- « ajouter une ligne à la fin d'un fichier à chaque exécution »
- « s'assurer qu'un utilisateur existe »

#### Autonome
Explique en 3-4 phrases pourquoi l'idempotence rend Ansible **rassurant** à utiliser, comparé à un script qu'on hésite à relancer.

#### Défi
Imagine un script qui crée un utilisateur avec la commande `useradd bob`. Que se passe-t-il si on le lance **deux fois** ? Et comment une approche en **état souhaité** (« bob doit exister ») évite-t-elle ce problème ?

### ✅ Tu sais maintenant…

- Ce que veut dire **idempotent** : rejouer donne le même résultat, sans rien casser.
- Qu'Ansible agit **seulement s'il y a un écart** (`changed`), sinon il ne fait rien (`ok`).
- Que l'idempotence rend les playbooks **rejouables sans crainte**.
- Qu'« idempotent » ne veut **pas** dire « passif » : Ansible agit **juste ce qu'il faut**.

---


## Chapitre 0.4 — Ansible dans l'écosystème infra (court)

### Le minimum à savoir

Tu entendras souvent parler d'Ansible **à côté** d'autres outils : Terraform, Docker, Kubernetes. Pour éviter toute confusion, voici **en bref** qui fait quoi. Ce n'est **pas** un comparatif détaillé — juste de quoi situer Ansible.

| Outil | Ce qu'il fait | En une phrase |
|-------|---------------|---------------|
| **Ansible** | **Configure** des machines qui existent déjà | installer, paramétrer, administrer |
| **Terraform** | **Provisionne / crée** l'infrastructure | faire naître des serveurs, des réseaux |
| **Docker** | **Package** une application en conteneur | emballer une app et ses dépendances |
| **Kubernetes** | **Orchestre** des conteneurs | faire tourner beaucoup de conteneurs à l'échelle |

> **À retenir :** ces outils sont **complémentaires**, pas concurrents. Un parcours courant : Terraform **crée** les serveurs → Ansible les **configure** → Docker/Kubernetes y **font tourner** les applications. **Mais ce cours reste centré sur Ansible** : configurer des machines Linux existantes.

### Très utile en pratique

La seule chose à retenir pour la suite : **Ansible travaille sur des machines qui existent déjà**. On ne lui demande pas de **créer** des serveurs (c'est le rôle de Terraform), ni de **packager** des applications (c'est Docker). On lui demande de **configurer** et **administrer** les machines de notre lab.

### 🔀 À ne pas confondre

> **« Configurer » (Ansible) ≠ « Créer » (Terraform).**
> Ansible suppose que la machine **existe** et qu'on peut s'y connecter en SSH. Il l'**administre**. Il ne la fait pas apparaître.

### ❌ Erreur classique

> **Vouloir « tout faire avec Ansible », y compris créer des machines.**

Le débutant enthousiaste essaie parfois d'utiliser Ansible pour provisionner des serveurs (le rôle de Terraform). Ça mène à des montages bancals. Le réflexe correct : **Ansible configure l'existant**. Pour ce cours, nos machines existent déjà (on les crée à la main dans VirtualBox/VMware en Partie 1).

### Exercices

#### Guidé
Associe chaque besoin à l'outil : (a) « créer 3 serveurs », (b) « installer et configurer nginx sur ces serveurs », (c) « emballer une application en conteneur », (d) « faire tourner 50 conteneurs ». Lequel relève d'**Ansible** ?

#### Autonome
En 3 phrases, explique pourquoi ces outils sont **complémentaires** plutôt que concurrents, avec l'exemple Terraform → Ansible → Docker.

#### Défi
Sans chercher à les approfondir, explique pourquoi un cours **débutant Ansible** a raison de **ne pas** se disperser sur Terraform, Docker et Kubernetes en détail. Que gagne-t-on à rester focalisé ?

### ✅ Tu sais maintenant…

- Qu'Ansible **configure des machines existantes**.
- Que **Terraform** crée l'infra, **Docker** package les apps, **Kubernetes** orchestre les conteneurs.
- Que ces outils sont **complémentaires**, mais que **ce cours reste centré sur Ansible**.
- Que nos machines de lab **existent déjà** (on ne les crée pas avec Ansible).

---

### 🚩 Checkpoint — Fin de la Partie 0

Avant de monter le lab, assure-toi de pouvoir :

- [ ] Expliquer **pourquoi Ansible existe** (éviter la répétition, lutter contre la dérive de config).
- [ ] Dire ce qu'est un **état souhaité** (décrire un résultat, pas une suite d'ordres).
- [ ] Expliquer l'**idempotence** avec tes mots (rejouer ne change rien si c'est déjà fait).
- [ ] Situer Ansible : il **configure** des machines existantes (≠ Terraform/Docker/Kubernetes).

> **La suite :** en Partie 1, on **construit le lab** — une machine de contrôle et deux cibles Linux — et on établit la connexion **SSH par clé**. C'est le terrain sur lequel tu vas tout pratiquer.

---
---
