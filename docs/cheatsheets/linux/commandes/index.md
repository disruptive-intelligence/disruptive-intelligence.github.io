---
title: "Commandes clés"
---
# Commandes clés

Les « couteaux suisses » aux options innombrables : leur syntaxe, les options qui servent vraiment, des
commandes réelles décodées, les pièges, puis des exemples par usage. Chaque fiche liste aussi les besoins
où la commande sert et son équivalent Windows. Toutes les autres commandes : [🔤 Par commande](../../commandes.md).

## Fichiers et archives

- [`find`](find.md) — Parcourt une arborescence et sélectionne les fichiers selon leur nom, leur type, leur taille, leur date, leur propriétaire ou leurs droits ; peut ensuite agir sur chacun.
- [`tar`](tar.md) — Regroupe des fichiers dans une archive (souvent compressée), en liste le contenu ou l'extrait.

## Texte et filtres

- [`grep`](grep.md) — Affiche les lignes qui contiennent un motif — dans un fichier, dans tout un dossier ou dans la sortie d'une autre commande.
- [`awk`](awk.md) — Découpe chaque ligne en champs et permet de filtrer, réarranger ou calculer — là où `cut` ne fait que découper.
- [`sed`](sed.md) — Transforme du texte ligne par ligne : remplacer, supprimer, n'afficher qu'une partie — dans la sortie, ou dans le fichier avec `-i`.
- [`cut`](cut.md) — Garde certains champs d'une ligne selon un séparateur ; utile pour retirer `dstport=` après extraction.
- [`sort`](sort.md) — Trie les lignes ou les champs, numériquement ou alphabétiquement, et supprime les doublons avec `-u`.
- [`uniq`](uniq.md) — Regroupe ou compte les lignes identiques voisines, après un tri.
- [`wc`](wc.md) — Compte les lignes, les mots, les octets ou les caractères d'un résultat.
- [`column`](column.md) — Aligne des champs délimités pour les lire comme un tableau dans le terminal.
- [`less`](less.md) — Parcourt un fichier ou un pipeline, cherche un motif et fait défiler les lignes larges.

## Processus, services et journaux

- [`ps`](ps.md) — Photographie les processus à un instant donné : qui tourne, sous quel utilisateur, lancé par qui, avec quelles ressources.
- [`systemctl`](systemctl.md) — Pilote systemd : l'état, le démarrage et l'activation des services, et ce qui se lance avec la machine.
- [`journalctl`](journalctl.md) — Lit le journal de systemd : services, système, noyau — avec des filtres par service, période, gravité ou processus.

## Réseau

- [`ss`](ss.md) — Liste les sockets : ports en écoute et connexions, avec le processus derrière. Remplace `netstat`.
- [`ip`](ip.md) — Affiche et règle la configuration réseau : adresses, interfaces, routes, voisins. Remplace `ifconfig`, `route` et `arp`.
