---
title: Chapitre 1.3 — Installer Ansible
source: IT/08 Conteneurs & automatisation/Automatisation/Ansible.md
note: Ansible
up:
- - Ansible
  - ../index.md
- - Partie 1 — Préparer le lab
  - index.md
---

## Le minimum à savoir

On installe Ansible **uniquement sur la machine de contrôle**. Les cibles, elles, n'ont besoin de rien (juste SSH + Python, déjà vus).

Il y a deux façons courantes d'installer Ansible sur un Linux :

1. **Via le gestionnaire de paquets** de ta distribution — simple, parfait pour un lab.
2. **Via `pipx`** — installe Ansible dans un environnement isolé, plus propre et à jour.

> Les commandes d'installation **évoluent** avec le temps et dépendent de ta distribution. En cas de doute, la **documentation officielle d'Ansible fait foi**. Voici les deux approches générales :

## Très utile en pratique

```bash
# Option 1 — simple, pour un lab (familles Debian/Ubuntu)
sudo apt update && sudo apt install -y ansible

# Option 2 — propre et isolée (recommandée si tu connais un peu Python)
pipx install --include-deps ansible

# Vérifier que c'est installé (sur la machine de contrôle)
ansible --version
```


`ansible --version` doit afficher un numéro de version. Si la commande est introuvable, c'est qu'Ansible n'est pas (encore) installé, ou pas dans le `PATH`.

## Exemple simple

```text
$ ansible --version
ansible [core 2.x.x]
  config file = ...
  python version = 3.x.x ...
```


Cet affichage = Ansible est prêt sur ta machine de contrôle.

## 🔀 À ne pas confondre

> **Installer Ansible (sur le contrôle) ≠ préparer les cibles.**
> Tu installes Ansible **une seule fois**, sur la machine de contrôle. Tu n'installes **rien** sur les cibles. Si tu te retrouves à lancer `apt install ansible` sur « cible1 », c'est une erreur.

## ❌ Erreur classique

> **Installer Ansible sur les cibles, ou s'attendre à un décalage de version.**

Deux pièges fréquents. D'abord, installer Ansible partout (inutile : seul le contrôle en a besoin). Ensuite, s'étonner que la version du paquet de la distribution soit un peu ancienne — c'est normal. Pour un lab, ce n'est pas grave. Si tu veux la version la plus récente, l'option `pipx` est préférable. Le réflexe correct : **Ansible sur le contrôle uniquement**, et la **doc officielle** comme référence en cas de doute.

## Exercices

### Guidé
Installe Ansible sur ta machine de contrôle (choisis l'option `apt` ou `pipx`). Lance `ansible --version` et vérifie qu'un numéro de version s'affiche. Note la commande qui a fonctionné pour ta distribution.

### Autonome
Connecte-toi à une de tes **cibles** et lance `ansible --version`. Que se passe-t-il ? Explique pourquoi c'est **normal** que la commande ne soit pas trouvée sur la cible.

### Défi
Compare les deux méthodes d'installation (`apt` vs `pipx`) en une ou deux phrases chacune : avantage principal de chacune pour un débutant. Laquelle choisirais-tu et pourquoi ?

## ✅ Tu sais maintenant…

- Qu'on installe Ansible **uniquement sur la machine de contrôle**.
- Les deux méthodes courantes : **paquet de la distribution** (`apt`) ou **`pipx`** (isolé).
- Vérifier l'installation avec **`ansible --version`**.
- Que la version du paquet peut être un peu ancienne (normal pour un lab).

---
