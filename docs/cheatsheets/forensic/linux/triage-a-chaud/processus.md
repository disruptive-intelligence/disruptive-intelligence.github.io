---
title: "Processus"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/cyber/detection/reponse-a-incident/index.md
---
# Processus

Ce qui tourne en ce moment : à relever en premier, c'est le plus volatil.

Les incontournables : `ps auxf` · `pstree -p` · `ls -l /proc/<PID>/exe` · `lsof -p` · `cp /proc/<PID>/exe`
{ .kw-cs-top }

## Observer

![[cheatsheets/linux/fondamentaux/processus#Lister tous les processus]]

![[cheatsheets/linux/fondamentaux/processus#Voir les processus enfants d'un PID]]

![[cheatsheets/linux/fondamentaux/processus#Tout savoir sur un PID]]

![[cheatsheets/linux/fondamentaux/processus#Voir les fichiers et connexions d'un PID]]

## Préserver

### Préserver le binaire d'un processus suspect

```bash title="Commande"
sudo cp /proc/<PID>/exe ./preuve_<PID>.bin   # copie le binaire en cours d'exécution
sha256sum ./preuve_<PID>.bin | tee -a empreintes.txt   # son empreinte, notée dans la collecte
```

```bash title="Exemple"
sudo cp /proc/1234/exe ./preuve_1234.bin && sha256sum ./preuve_1234.bin | tee -a empreintes.txt
```

??? example "Sortie"
    ```text
    3f9a1c0e7b2d4a6f8e1c3b5d7f9a0c2e4b6d8f0a1c3e5b7d9f1a3c5e7b9d0f2a  ./preuve_1234.bin
    ```

```bash title="Exemple 2"
sudo cat /proc/1234/maps > preuve_1234_maps.txt   # bibliothèques chargées et régions mémoire
```

Marche même si le fichier a été supprimé du disque après le lancement. Ensuite seulement :
[arrêter le processus](../../../linux/fondamentaux/processus.md#arreter-un-processus-poliment-puis-de-force).
{ .kw-cs-meta }

Étape suivante : [Réseau](reseau.md)
{ .kw-cs-meta }
