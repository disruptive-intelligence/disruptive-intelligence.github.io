---
title: Chapitre 1.1 — Control node et machines cibles
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 1 — Préparer le lab
  - index.md
---

## Le minimum à savoir

Ansible repose sur une distinction très simple :

```
   ┌─────────────────┐       SSH       ┌─────────────────┐
   │  MACHINE DE     │ ──────────────▶ │     CIBLE 1     │
   │  CONTRÔLE       │ ──────────────▶ │     CIBLE 2     │
   │  (Ansible ICI)  │ ──────────────▶ │   (Cible 3)     │
   └─────────────────┘                 └─────────────────┘
   Tu pilotes d'ici         Les machines administrées
```


- La **machine de contrôle** (*control node*) : c'est là, et **seulement** là, qu'on **installe Ansible**. C'est ton poste de pilotage.
- Les **machines cibles** (*managed nodes*) : ce sont les machines qu'Ansible **administre**. On **n'installe pas** Ansible dessus.

### Le point qui surprend : « agentless »

Ansible n'installe **aucun programme permanent** sur les cibles. On dit qu'il est **agentless** (sans agent). Il se connecte en **SSH** (comme tu le ferais à la main), fait son travail en s'appuyant sur **Python** (déjà présent sur la plupart des Linux), puis se déconnecte. Rien ne reste installé sur les cibles.

> **Conséquence pratique :** si une machine est accessible en **SSH** et qu'elle a **Python**, Ansible peut l'administrer **immédiatement**. Pas de déploiement d'agent, pas de configuration lourde sur les cibles.

## Très utile en pratique

Sur la **machine de contrôle**, une seule commande confirmera (plus tard) qu'Ansible est là :

```bash
ansible --version
```


Sur les **cibles**, tu ne vérifies **pas** « si Ansible est installé » (il ne l'est pas, et c'est normal). Tu vérifieras seulement qu'elles répondent en **SSH** — c'est l'objet des chapitres suivants.

## Exemple simple

Le lab de ce cours, c'est :

```text
control   → 1 VM Linux, on y installe Ansible
cible1    → 1 VM Linux, rien à installer
cible2    → 1 VM Linux, rien à installer
(cible3)  → optionnelle, pour s'entraîner aux groupes plus tard
```


Trois petites VMs Linux sur ton ordinateur, reliées par un réseau local. C'est tout.

## 🔀 À ne pas confondre

> **« Agentless » ne veut pas dire « rien sur les cibles ».**
> Les cibles ont besoin de **SSH** (pour la connexion) et de **Python** (pour exécuter le travail). Simplement, il n'y a **pas d'agent Ansible** à installer et à maintenir.

## ❌ Erreur classique

> **Vouloir « installer Ansible sur les machines cibles ».**

Si tu viens d'outils qui posent un agent partout, tu pourrais croire qu'il faut installer Ansible sur chaque cible. **C'est inutile.** Le réflexe correct : **Ansible s'installe uniquement sur la machine de contrôle**. Les cibles n'ont besoin que de SSH et Python. Si tu te surprends à vouloir installer Ansible sur « cible1 », arrête-toi : ce n'est pas comme ça que ça marche.

## Exercices

### Guidé
Sur une feuille, dessine ton futur lab : une machine de contrôle, deux cibles, et des flèches **SSH** qui partent du contrôle vers les cibles. Écris « Ansible installé ici » sur la machine de contrôle, et « SSH + Python » sur les cibles.

### Autonome
Explique avec tes mots ce que veut dire **agentless**, et donne **un avantage** concret pour quelqu'un qui doit administrer beaucoup de machines.

### Défi
Pourquoi est-ce pratique qu'Ansible utilise **SSH** plutôt qu'un protocole spécial à lui ? (Indice : pense à ce que tu sais déjà faire avec SSH, et à ce qui est déjà en place sur tes serveurs Linux.)

## ✅ Tu sais maintenant…

- La distinction **machine de contrôle** (Ansible installé) vs **cibles** (rien d'installé).
- Ce que veut dire **agentless** : pas d'agent permanent, juste **SSH + Python** sur les cibles.
- Qu'Ansible s'installe **uniquement** sur la machine de contrôle.
- À quoi ressemble le lab du cours (1 contrôle + 2-3 cibles Linux).

---
