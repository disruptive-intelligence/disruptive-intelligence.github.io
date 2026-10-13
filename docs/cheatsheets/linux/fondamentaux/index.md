---
title: "Fondamentaux"
---
# Fondamentaux

Comprendre et observer un système Linux : où sont les choses, quels processus tournent, qui est connecté,
ce que disent les journaux.

## Carte mentale

<div class="kw-mindmap" markdown>

- **Observer un système Linux**
    - [Système et arborescence](systeme.md)
        - Identifier la machine
            - [Distribution](systeme.md#connaitre-la-distribution-et-sa-version) : `cat /etc/os-release`
            - [Noyau, architecture](systeme.md#connaitre-le-noyau-et-larchitecture) : `uname -a`
            - [Nom, fuseau, heure](systeme.md#connaitre-le-nom-dhote-le-fuseau-et-lheure) : `hostnamectl` · `timedatectl`
            - [Allumée depuis](systeme.md#voir-depuis-quand-la-machine-tourne-et-sa-charge) : `uptime`
        - Où sont les choses
            - `/etc` : configuration
            - `/var/log` : journaux
            - `/home`, `/root` : dossiers personnels
            - `/tmp`, `/var/tmp` : temporaires, modifiables par tous
            - `/proc` : processus et noyau (virtuel)
            - `/usr/bin`, `/usr/sbin` : commandes
        - Qui est là
            - [Connectés maintenant](systeme.md#voir-qui-est-connecte-maintenant) : `w`
            - [Dernières connexions](systeme.md#voir-les-dernieres-connexions) : `last -a`
    - [Fichiers et recherche](fichiers-recherche.md)
        - Lire
            - [Fichier long](fichiers-recherche.md#lire-un-fichier-long) : `less`
            - [Début, fin](fichiers-recherche.md#lire-le-debut-ou-la-fin-dun-fichier) : `head` · `tail`
            - [Suivre en direct](fichiers-recherche.md#suivre-un-fichier-qui-grossit) : `tail -F`
        - Trouver
            - [Par nom](fichiers-recherche.md#trouver-un-fichier-par-son-nom) : `find / -name`
            - [Modifiés récemment](fichiers-recherche.md#trouver-les-fichiers-modifies-recemment) : `find -mmin -60`
            - [Gros fichiers](fichiers-recherche.md#trouver-les-gros-fichiers) : `find -size +100M`
            - [D'un utilisateur](fichiers-recherche.md#trouver-les-fichiers-dun-utilisateur) : `find -user`
        - Chercher dans le contenu
            - [Tout un dossier](fichiers-recherche.md#chercher-un-mot-dans-tout-un-dossier) : `grep -rni`
            - [Avec le contexte](fichiers-recherche.md#afficher-le-contexte-autour-dune-correspondance) : `grep -C 3`
        - Vérifier
            - [Comparer](fichiers-recherche.md#comparer-deux-fichiers) : `diff -u`
            - [Empreinte](fichiers-recherche.md#calculer-lempreinte-dun-fichier) : `sha256sum`
    - [Texte et filtres](texte-filtres.md)
        - Extraire
            - [Une colonne](texte-filtres.md#extraire-une-colonne) : `cut -d -f` · `awk '{print $1}'`
            - [Un motif](texte-filtres.md#extraire-avec-une-expression-reguliere) : `grep -oE`
            - [Exclure des lignes](texte-filtres.md#exclure-des-lignes-commentaires-lignes-vides) : `grep -v`
        - Compter et trier
            - [Top des occurrences](texte-filtres.md#trier-et-compter-les-occurrences) : `sort | uniq -c | sort -rn`
            - [Lignes](texte-filtres.md#compter-des-lignes) : `wc -l`
        - Transformer
            - [Remplacer](texte-filtres.md#remplacer-du-texte) : `sed 's/a/b/g'`
            - [Séparateur, casse](texte-filtres.md#changer-un-separateur-ou-la-casse) : `tr`
            - [Tableau aligné](texte-filtres.md#afficher-en-tableau-aligne) : `column -t`
        - Enchaîner
            - `|` passe la sortie · `>` écrit · `>>` ajoute
            - [Voir et enregistrer](texte-filtres.md#voir-la-sortie-et-lenregistrer-en-meme-temps) : `tee`
    - [Processus et services](processus.md)
        - Observer
            - [Tous les processus](processus.md#lister-tous-les-processus) : `ps aux`
            - [Arbre](processus.md#voir-larbre-des-processus) : `pstree -p`
            - [Parent d'un PID](processus.md#trouver-le-parent-dun-processus) : `ps -o ppid= -p`
            - [Tout sur un PID](processus.md#tout-savoir-sur-un-pid) : `/proc/<PID>/`
            - [Fichiers et connexions](processus.md#voir-les-fichiers-et-connexions-dun-pid) : `lsof -p`
        - Agir
            - [Arrêter](processus.md#arreter-un-processus-poliment-puis-de-force) : `kill`, puis `kill -9`
            - [Survivre à la déconnexion](processus.md#lancer-une-commande-qui-survit-a-la-deconnexion) : `nohup`
        - Services
            - [État](processus.md#voir-letat-dun-service) : `systemctl status`
            - [Actifs, en échec](processus.md#lister-les-services-actifs-ou-en-echec) : `systemctl --failed`
            - [Définition](processus.md#voir-la-definition-dun-service) : `systemctl cat`
    - [Réseau](reseau.md)
        - Configuration
            - [Adresses](reseau.md#voir-ses-adresses-ip) : `ip -br a`
            - [Routes, passerelle](reseau.md#voir-la-table-de-routage-et-la-passerelle) : `ip r`
            - [Voisins (ARP)](reseau.md#voir-la-table-arp-machines-voisines) : `ip neigh`
        - Ports et connexions
            - [En écoute](reseau.md#voir-les-ports-en-ecoute) : `ss -tulnp`
            - [Établies](reseau.md#voir-les-connexions-etablies) : `ss -tnp state established`
            - [Qui tient un port](reseau.md#savoir-quel-processus-utilise-un-port) : `ss -ltnp`
        - Tester
            - [Connectivité](reseau.md#tester-la-connectivite) : `ping -c`
            - [Nom](reseau.md#resoudre-un-nom) : `dig`
            - [Port distant](reseau.md#tester-un-port-distant) : `nc -zv`
            - [Service web](reseau.md#interroger-un-service-web) : `curl -I`
        - [Capturer](reseau.md#capturer-du-trafic) : `tcpdump -i -n -w`
    - [Logs et journaux](logs.md)
        - journalctl
            - [D'un service](logs.md#lire-le-journal-dun-service) : `journalctl -u`
            - [Par période](logs.md#filtrer-les-journaux-par-periode) : `--since` · `--until`
            - [Erreurs depuis le démarrage](logs.md#voir-seulement-les-erreurs-depuis-le-demarrage) : `-p err -b`
        - /var/log
            - `auth.log` / `secure` : SSH, sudo
            - `syslog` / `messages` : journal général
            - `wtmp` · `btmp` : `last` · `lastb`
            - [Échecs de connexion](logs.md#trouver-les-echecs-de-connexion) : `grep "Failed password"`
            - [Archives](logs.md#chercher-dans-les-logs-archives-rotation) : `zgrep`
    - [Droits et identités](droits.md)
        - Lire et changer
            - [Lire](droits.md#lire-les-droits-dun-fichier) : `ls -l` — `rwx` = 4 2 1
            - [Changer](droits.md#changer-les-droits-dun-fichier) : `chmod 640`
            - [Propriétaire](droits.md#changer-le-proprietaire-dun-fichier) : `chown`
            - [ACL](droits.md#voir-les-droits-fins-acl) : `getfacl`
        - Identités
            - [Qui je suis, sudo](droits.md#savoir-qui-je-suis-et-ce-que-sudo-mautorise) : `id` · `sudo -l`
            - [Comptes](droits.md#lister-les-comptes-du-systeme) : `getent passwd`
        - À surveiller
            - [SUID / SGID](droits.md#trouver-les-fichiers-suid-ou-sgid) : `find / -perm -4000`
            - [Modifiables par tous](droits.md#trouver-les-fichiers-modifiables-par-tous) : `find / -perm -o+w`
            - [Capabilities](droits.md#voir-les-capabilities-des-binaires) : `getcap -r`

</div>

## Les fiches


- [Système et arborescence](systeme.md) — Identifier la machine, se repérer dans l'arborescence, savoir qui est connecté.
- [Fichiers et recherche](fichiers-recherche.md) — Lire, trouver et comparer des fichiers ; chercher un mot dans un fichier ou tout un dossier.
- [Texte et filtres](texte-filtres.md) — Découper, trier, compter et transformer la sortie d'une commande ou le contenu d'un fichier.
- [Processus et services](processus.md) — Repérer un processus, remonter à son parent, voir ses enfants, ses fichiers et ses connexions, l'arrêter ; observer les services.
- [Réseau](reseau.md) — Voir ses adresses, routes, ports et connexions ; tester la connectivité et la résolution de noms ; capturer du trafic.
- [Logs et journaux](logs.md) — Lire les journaux d'un service, filtrer par période et par gravité, retrouver les authentifications et l'usage de sudo.
- [Droits et identités](droits.md) — Lire et changer les droits, savoir qui je suis et ce que je peux faire, repérer les droits dangereux.
