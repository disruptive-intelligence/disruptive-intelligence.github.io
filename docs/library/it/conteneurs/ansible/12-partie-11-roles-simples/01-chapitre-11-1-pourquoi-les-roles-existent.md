---
title: Chapitre 11.1 — Pourquoi les roles existent
source: IT/08 Conteneurs & automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 11 — Roles simples
  - index.md
---

## Le minimum à savoir

À force d'ajouter des tâches, un playbook devient **long et difficile à relire**. Et tu te retrouves à **copier-coller** les mêmes tâches d'un projet à l'autre. Les **roles** résolvent ça : ils **regroupent et réutilisent** le code.

> **Un role**, c'est un ensemble cohérent de tâches, templates, variables et handlers, **rangés** dans une structure standard, qu'on peut **réutiliser** dans n'importe quel playbook. Par exemple, un role `common` qui installe les paquets de base et applique la config commune à toutes tes machines.

## Très utile en pratique

L'intérêt des roles :

- **Organiser** : un gros playbook devient un role bien rangé.
- **Réutiliser** : le même role s'applique dans plusieurs projets.
- **Partager** : un role est facile à donner à un collègue.

## Exemple simple

Sans role, ton playbook contient 20 tâches en vrac. Avec un role `common`, ton playbook devient :

```yaml
- name: Configuration de base
  hosts: all
  become: true
  roles:
    - common          # tout le contenu du role en une ligne
```


Limpide, non ?

## ❌ Erreur classique

> **Vouloir créer des roles trop tôt, pour tout.**

Un débutant qui découvre les roles veut tout transformer en role immédiatement. C'est prématuré. Le réflexe correct : crée un role **quand un playbook devient gros** ou **quand tu veux réutiliser** du code. Pas avant. Un petit playbook simple n'a pas besoin d'être un role.

## Exercices

### Guidé
Regarde tes playbooks actuels. Lequel est devenu **assez gros** pour justifier un role ? Lequel est encore **trop simple** pour ça ? Justifie.

### Autonome
Liste trois choses que tu refais **souvent** d'un playbook à l'autre (installer des paquets de base, créer un utilisateur admin, durcir SSH…). Ce sont de bons candidats pour un role réutilisable.

### Défi
Explique en quelques lignes la différence entre **réutiliser** un role et **copier-coller** des tâches. Pourquoi le role est-il une meilleure approche à long terme ?

## ✅ Tu sais maintenant…

- Pourquoi les **roles** existent : organiser et réutiliser le code.
- Qu'un role regroupe tâches, templates, variables et handlers.
- Qu'on appelle un role en **une ligne** dans un playbook.
- Qu'il ne faut créer des roles **ni trop tôt, ni pour tout**.

---
