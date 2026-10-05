---
title: "Réseau"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/cyber/detection/reponse-a-incident/index.md
---
# Réseau

Avec qui la machine parle, et quels services elle expose.

Les incontournables : `ss -tlnp` · `ss -tnp` · `lsof -i`
{ .kw-cs-top }

## Ports et connexions

![[cheatsheets/linux/fondamentaux/reseau#Voir les ports en écoute]]

![[cheatsheets/linux/fondamentaux/reseau#Voir les connexions établies]]

Étape suivante : [Persistance](persistance.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Ce qu'on regarde | Commande | Ce qui doit alerter |
|---|---|---|
| Ports en écoute | `ss -tulpn` | Port inattendu, processus inconnu à l'écoute |
| Connexions établies | `ss -tnp state established` | Connexion sortante persistante vers une IP inconnue (C2) |
| Processus d'un port | `lsof -i :<port>` | Programme lancé depuis `/tmp` ou `/dev/shm` |
