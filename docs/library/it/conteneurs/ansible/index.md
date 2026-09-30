---
title: Ansible
source: IT/10_virtualization-containers/Ansible.md
format: cours
---

*Automatiser l'administration de machines Linux pas à pas*

---

> **Prérequis :** quelques bases en Linux (se déplacer dans les dossiers, éditer un fichier, lancer une commande) et savoir ouvrir un **terminal**. Le SSH est **rappelé dans le cours**. **Aucune** connaissance d'Ansible, de DevOps, de cloud ou d'« infrastructure as code » n'est nécessaire.
> Tout ce dont tu as besoin, c'est un petit **lab de machines virtuelles Linux** : une machine de contrôle et deux ou trois cibles, sous VirtualBox ou VMware.

---

### À qui s'adresse ce cours

- À un **débutant complet** en Ansible.
- À quelqu'un qui connaît **un peu Linux** et sait ouvrir un terminal.
- À quelqu'un qui a **déjà utilisé SSH**, ou qui va l'apprendre ici.
- À toute personne qui veut **automatiser l'administration de plusieurs machines Linux** sans répéter les mêmes commandes une par une.

### Ce que tu sauras faire à la fin

- Comprendre **à quoi sert Ansible** et le principe de l'**état souhaité**.
- Monter un **lab** (contrôle + cibles) et te connecter en **SSH par clé**.
- Décrire tes machines dans un **inventaire** et lancer des **commandes ad hoc**.
- Lire les **sorties** d'Ansible (`ok`, `changed`, `failed`, `skipped`, `unreachable`) et comprendre l'**idempotence**.
- Écrire des **playbooks** en YAML, lisibles et rejouables.
- Utiliser les **modules** essentiels : paquets, services, fichiers, utilisateurs.
- Rendre tes playbooks adaptables avec **variables**, **facts**, **conditions** et **boucles**.
- Générer de la configuration avec des **templates Jinja2** et redémarrer proprement avec des **handlers**.
- Protéger tes secrets avec **Ansible Vault**.
- **Organiser** un projet Ansible propre et créer un **role** simple.

---

### Comment penser Ansible (l'idée en une image)

Si tu ne retiens qu'une chose de ce cours, c'est ceci :

```
   TU DÉCRIS                 ANSIBLE COMPARE              ANSIBLE AGIT
   l'état souhaité     →     ce qui est déjà fait   →     seulement si nécessaire
   "nginx installé"          "nginx est-il là ?"          "non → je l'installe"
                                                          "oui → je ne touche à rien"
```


Avec Ansible, tu ne décris **pas** une suite d'ordres (« installe, puis démarre, puis vérifie »). Tu décris un **résultat souhaité** (« nginx doit être installé et démarré »), et Ansible se débrouille pour y arriver — **et** pour ne **rien** refaire si c'est déjà bon.

Cette propriété (« rejouer ne casse rien, ne refait que ce qui manque ») s'appelle l'**idempotence**. C'est le cœur d'Ansible, et c'est ce qui le distingue d'un simple script. On y reviendra en détail (Partie 3).

---

### Les encadrés du cours

Pour t'aider, tu croiseras de temps en temps de petits encadrés :

- **🔍 Réflexe diagnostic** — quoi regarder quand « ça ne marche pas ».
- **🛡️ Réflexe sécurité** — un bon réflexe simple (protéger une clé, ne pas écrire un mot de passe en clair).
- **🔀 À ne pas confondre** — deux notions proches à bien distinguer.
- **🧪 Lab vs production** — ce qui est acceptable pour apprendre, mais pas sur de vraies machines en service.

Ils restent **légers** : ce cours est un cours **débutant**, pas un cours d'expert.

---

### Sur la progression

Le cours est **très progressif**. On commence par comprendre (sans rien installer), puis on monte le lab, puis on agit **une commande à la fois**, et seulement ensuite on écrit des playbooks. Les notions plus avancées (variables, templates, roles) arrivent **quand tu es prêt**.

> **Conseil :** ne cherche pas à tout retenir par cœur. Le but est de comprendre le **cycle** : décrire un inventaire → agir → lire les sorties → écrire un playbook rejouable. Les commandes exactes, tu les retrouveras dans la cheat-sheet en annexe.

Ne te juge pas si un chapitre demande deux lectures. **La régularité compte plus que la vitesse.**

---

### Table des matières

**Partie 0 — Introduction** *(tu es ici)*

**Partie 1 — Préparer le lab**

**Partie 2 — Inventaire et premières commandes**

**Partie 3 — Comprendre les sorties et l'idempotence**

**Partie 4 — YAML et premiers playbooks**

**Partie 5 — Modules essentiels d'administration Linux**

**Partie 6 — Variables, facts, conditions et boucles**

**Partie 7 — Templates et handlers**

**Partie 8 — Bonnes pratiques débutant**

**Partie 9 — Ansible Vault et secrets**

**Partie 10 — Organiser un projet Ansible**

**Partie 11 — Roles simples**

**Partie 12 — Mini-projets pratiques (récapitulatif)**

**Annexes** — cheat-sheet, erreurs fréquentes, rappel YAML, rappel SSH, écosystème infra, roadmap

---
---

## Sommaire

- [Partie 0 — Introduction](01-partie-0-introduction/index.md)
    - [Chapitre 0.1 — Pourquoi Ansible existe](01-partie-0-introduction/01-chapitre-0-1-pourquoi-ansible-existe.md)
    - [Chapitre 0.2 — L'idée d'Ansible : l'état souhaité](01-partie-0-introduction/02-chapitre-0-2-l-idee-d-ansible-l-etat-souhaite.md)
    - [Chapitre 0.3 — L'idempotence en une image](01-partie-0-introduction/03-chapitre-0-3-l-idempotence-en-une-image.md)
    - [Chapitre 0.4 — Ansible dans l'écosystème infra (court)](01-partie-0-introduction/04-chapitre-0-4-ansible-dans-l-ecosysteme-infra-court.md)
- [Partie 1 — Préparer le lab](02-partie-1-preparer-le-lab/index.md)
    - [Chapitre 1.1 — Control node et machines cibles](02-partie-1-preparer-le-lab/01-chapitre-1-1-control-node-et-machines-cibles.md)
    - [Chapitre 1.2 — SSH et clés](02-partie-1-preparer-le-lab/02-chapitre-1-2-ssh-et-cles.md)
    - [Chapitre 1.3 — Installer Ansible](02-partie-1-preparer-le-lab/03-chapitre-1-3-installer-ansible.md)
    - [Chapitre 1.4 — Snapshots et erreurs SSH classiques](02-partie-1-preparer-le-lab/04-chapitre-1-4-snapshots-et-erreurs-ssh-classiques.md)
- [Partie 2 — Inventaire et premières commandes](03-partie-2-inventaire-et-premieres-commandes/index.md)
    - [Chapitre 2.1 — L'inventaire INI](03-partie-2-inventaire-et-premieres-commandes/01-chapitre-2-1-l-inventaire-ini.md)
    - [Chapitre 2.2 — Variables simples d'inventaire](03-partie-2-inventaire-et-premieres-commandes/02-chapitre-2-2-variables-simples-d-inventaire.md)
    - [Chapitre 2.3 — Le ping et les commandes ad hoc](03-partie-2-inventaire-et-premieres-commandes/03-chapitre-2-3-le-ping-et-les-commandes-ad-hoc.md)
    - [Chapitre 2.4 — command et shell](03-partie-2-inventaire-et-premieres-commandes/04-chapitre-2-4-command-et-shell.md)
    - [Chapitre 2.5 — Lire les sorties : ok, changed, failed, skipped, unreachable](03-partie-2-inventaire-et-premieres-commandes/05-chapitre-2-5-lire-les-sorties-ok-changed-failed-sk.md)
- [Partie 3 — Comprendre les sorties et L'idempotence](04-partie-3-comprendre-les-sorties-et-l-idempotence/index.md)
    - [Chapitre 3.1 — ok vs changed](04-partie-3-comprendre-les-sorties-et-l-idempotence/01-chapitre-3-1-ok-vs-changed.md)
    - [Chapitre 3.2 — Voir l'idempotence en relançant](04-partie-3-comprendre-les-sorties-et-l-idempotence/02-chapitre-3-2-voir-l-idempotence-en-relancant.md)
    - [Chapitre 3.3 — Modules dédiés vs command/shell](04-partie-3-comprendre-les-sorties-et-l-idempotence/03-chapitre-3-3-modules-dedies-vs-command-shell.md)
- [Partie 4 — YAML et premiers playbooks](05-partie-4-yaml-et-premiers-playbooks/index.md)
    - [Chapitre 4.1 — YAML sans peur](05-partie-4-yaml-et-premiers-playbooks/01-chapitre-4-1-yaml-sans-peur.md)
    - [Chapitre 4.2 — Anatomie d'un playbook](05-partie-4-yaml-et-premiers-playbooks/02-chapitre-4-2-anatomie-d-un-playbook.md)
    - [Chapitre 4.3 — become : les droits root](05-partie-4-yaml-et-premiers-playbooks/03-chapitre-4-3-become-les-droits-root.md)
    - [Chapitre 4.4 — Vérifier avant d'agir : --syntax-check et --check](05-partie-4-yaml-et-premiers-playbooks/04-chapitre-4-4-verifier-avant-d-agir-syntax-check-et.md)
- [Partie 5 — Modules essentiels d'administration linux](06-partie-5-modules-essentiels-d-administration-linux.md)
- [Partie 6 — Variables, facts, conditions et boucles](07-partie-6-variables-facts-conditions-et-boucles.md)
- [Partie 7 — Templates et handlers](08-partie-7-templates-et-handlers/index.md)
    - [Chapitre 7.1 — Les templates Jinja2 (template)](08-partie-7-templates-et-handlers/01-chapitre-7-1-les-templates-jinja2-template.md)
    - [Chapitre 7.2 — copy vs template (bien choisir)](08-partie-7-templates-et-handlers/02-chapitre-7-2-copy-vs-template-bien-choisir.md)
    - [Chapitre 7.3 — Les handlers (notify)](08-partie-7-templates-et-handlers/03-chapitre-7-3-les-handlers-notify.md)
- [Partie 8 — Bonnes pratiques débutant](09-partie-8-bonnes-pratiques-debutant.md)
- [Partie 9 — Ansible vault et secrets](10-partie-9-ansible-vault-et-secrets.md)
- [Partie 10 — Organiser un projet ansible](11-partie-10-organiser-un-projet-ansible.md)
- [Partie 11 — Roles simples](12-partie-11-roles-simples/index.md)
    - [Chapitre 11.1 — Pourquoi les roles existent](12-partie-11-roles-simples/01-chapitre-11-1-pourquoi-les-roles-existent.md)
    - [Chapitre 11.2 — La structure d'un role](12-partie-11-roles-simples/02-chapitre-11-2-la-structure-d-un-role.md)
    - [Chapitre 11.3 — Créer et utiliser un role simple](12-partie-11-roles-simples/03-chapitre-11-3-creer-et-utiliser-un-role-simple.md)
- [Partie 12 — Mini-projets pratiques (récapitulatif)](13-partie-12-mini-projets-pratiques-recapitulatif.md)
- [Annexes](14-annexes.md)
