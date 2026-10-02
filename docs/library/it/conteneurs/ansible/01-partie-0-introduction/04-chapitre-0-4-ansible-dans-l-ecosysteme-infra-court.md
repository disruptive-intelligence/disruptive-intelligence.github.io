---
title: Chapitre 0.4 — Ansible dans l'écosystème infra (court)
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 0 — Introduction
  - index.md
---

## Le minimum à savoir

Tu entendras souvent parler d'Ansible **à côté** d'autres outils : Terraform, Docker, Kubernetes. Pour éviter toute confusion, voici **en bref** qui fait quoi. Ce n'est **pas** un comparatif détaillé — juste de quoi situer Ansible.

| Outil | Ce qu'il fait | En une phrase |
|-------|---------------|---------------|
| **Ansible** | **Configure** des machines qui existent déjà | installer, paramétrer, administrer |
| **Terraform** | **Provisionne / crée** l'infrastructure | faire naître des serveurs, des réseaux |
| **Docker** | **Package** une application en conteneur | emballer une app et ses dépendances |
| **Kubernetes** | **Orchestre** des conteneurs | faire tourner beaucoup de conteneurs à l'échelle |

> **À retenir :** ces outils sont **complémentaires**, pas concurrents. Un parcours courant : Terraform **crée** les serveurs → Ansible les **configure** → Docker/Kubernetes y **font tourner** les applications. **Mais ce cours reste centré sur Ansible** : configurer des machines Linux existantes.

## Très utile en pratique

La seule chose à retenir pour la suite : **Ansible travaille sur des machines qui existent déjà**. On ne lui demande pas de **créer** des serveurs (c'est le rôle de Terraform), ni de **packager** des applications (c'est Docker). On lui demande de **configurer** et **administrer** les machines de notre lab.

## 🔀 À ne pas confondre

> **« Configurer » (Ansible) ≠ « Créer » (Terraform).**
> Ansible suppose que la machine **existe** et qu'on peut s'y connecter en SSH. Il l'**administre**. Il ne la fait pas apparaître.

## ❌ Erreur classique

> **Vouloir « tout faire avec Ansible », y compris créer des machines.**

Le débutant enthousiaste essaie parfois d'utiliser Ansible pour provisionner des serveurs (le rôle de Terraform). Ça mène à des montages bancals. Le réflexe correct : **Ansible configure l'existant**. Pour ce cours, nos machines existent déjà (on les crée à la main dans VirtualBox/VMware en Partie 1).

## Exercices

### Guidé
Associe chaque besoin à l'outil : (a) « créer 3 serveurs », (b) « installer et configurer nginx sur ces serveurs », (c) « emballer une application en conteneur », (d) « faire tourner 50 conteneurs ». Lequel relève d'**Ansible** ?

### Autonome
En 3 phrases, explique pourquoi ces outils sont **complémentaires** plutôt que concurrents, avec l'exemple Terraform → Ansible → Docker.

### Défi
Sans chercher à les approfondir, explique pourquoi un cours **débutant Ansible** a raison de **ne pas** se disperser sur Terraform, Docker et Kubernetes en détail. Que gagne-t-on à rester focalisé ?

## ✅ Tu sais maintenant…

- Qu'Ansible **configure des machines existantes**.
- Que **Terraform** crée l'infra, **Docker** package les apps, **Kubernetes** orchestre les conteneurs.
- Que ces outils sont **complémentaires**, mais que **ce cours reste centré sur Ansible**.
- Que nos machines de lab **existent déjà** (on ne les crée pas avec Ansible).

---

## 🚩 Checkpoint — Fin de la Partie 0

Avant de monter le lab, assure-toi de pouvoir :

- [ ] Expliquer **pourquoi Ansible existe** (éviter la répétition, lutter contre la dérive de config).
- [ ] Dire ce qu'est un **état souhaité** (décrire un résultat, pas une suite d'ordres).
- [ ] Expliquer l'**idempotence** avec tes mots (rejouer ne change rien si c'est déjà fait).
- [ ] Situer Ansible : il **configure** des machines existantes (≠ Terraform/Docker/Kubernetes).

> **La suite :** en Partie 1, on **construit le lab** — une machine de contrôle et deux cibles Linux — et on établit la connexion **SSH par clé**. C'est le terrain sur lequel tu vas tout pratiquer.

---
---
