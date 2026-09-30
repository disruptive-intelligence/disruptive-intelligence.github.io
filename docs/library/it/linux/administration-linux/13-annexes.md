---
title: Annexes
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - index.md
---

Ces sujets dépassent le cœur du cours débutant, mais valent d'être connus quand tu progresseras. Ils sont volontairement traités en survol : chacun mériterait un cours à part entière.

## Annexe A — Expressions régulières (regex)

Les **regex** sont des motifs de recherche puissants, utilisés par `grep`, `sed`, `awk` et bien d'autres. Le cours en a montré l'usage le plus simple (chercher un mot littéral). Les regex permettent bien plus : `^` (début de ligne), `$` (fin de ligne), `.` (n'importe quel caractère), `*` (répétition), `[0-9]` (un chiffre), etc. Par exemple, `grep -E "^[0-9]+" fichier` trouve les lignes commençant par un nombre. C'est un domaine entier à explorer une fois les bases acquises ; il décuple la puissance de la recherche et du filtrage de logs.

## Annexe B — `sed` et `awk` avancés

Le chapitre 4 en a montré l'usage minimal (substitution simple, extraction de colonne). En réalité, `sed` est un éditeur de flux complet (suppression de lignes, insertion, plages d'adresses) et `awk` est un véritable **langage de traitement de texte** (variables, conditions, calculs, agrégations par champ). Pour l'analyse de logs poussée, ils sont irremplaçables — mais leur apprentissage approfondi relève d'un module dédié.

## Annexe C — Stockage avancé : partitions, LVM, RAID

Le chapitre 21 s'est concentré sur l'**observation** du stockage. La gestion avancée comprend : le **partitionnement** (`fdisk`, `parted`), le **LVM** (*Logical Volume Manager*, qui permet de redimensionner et combiner des volumes à chaud), et le **RAID** (combiner plusieurs disques pour la performance ou la redondance). Ces opérations sont puissantes mais risquées pour les données : à aborder en lab, avec méthode, une fois les fondamentaux maîtrisés.

## Annexe D — Pare-feu avancé : `iptables` / `nftables`

Le chapitre 25 a utilisé `ufw`, qui est une surcouche simplifiée. En dessous se trouvent `iptables` (historique) et `nftables` (moderne), qui offrent un contrôle très fin du trafic réseau (règles par protocole, par interface, NAT, etc.). C'est le niveau qu'on atteint pour des configurations réseau complexes ou des passerelles.

## Annexe E — Conteneurs et virtualisation

Au-delà des VM utilisées pour ce cours, l'écosystème moderne s'appuie massivement sur les **conteneurs** (Docker, Podman) : une façon légère d'empaqueter et d'isoler des applications. C'est une compétence majeure aujourd'hui, qui s'appuie directement sur les notions Linux de ce cours (processus, systèmes de fichiers, réseau, permissions). Un excellent sujet pour la suite.

## Annexe F — Familles de distributions

Le cours s'est concentré sur **Debian/Ubuntu** (gestionnaire `apt`). Les autres grandes familles : **RHEL/CentOS/Fedora/Rocky** (gestionnaire `dnf`/`yum`, logs dans `/var/log/secure`), et **Arch** (`pacman`, philosophie « rolling release »). Les **concepts** (permissions, processus, systemd, réseau) sont identiques partout ; seules changent quelques commandes de gestion de paquets et l'emplacement de certains fichiers. Savoir cela te permet de t'adapter à n'importe quelle distribution.

---
