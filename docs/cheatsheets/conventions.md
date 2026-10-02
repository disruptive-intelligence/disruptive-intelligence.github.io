---
title: "Conventions"
---
# Conventions des cheat sheets

## Une entrée = un besoin

Le titre dit ce qu'on veut faire, verbe en premier (« Voir les processus enfants d'un PID »), pas le nom
de la commande : c'est ce qu'on cherche quand on est sur le poste.

Sous chaque besoin :

1. **Commande** — la forme neutre, à adapter ; un commentaire `#` dit ce que fait chaque ligne.
2. **Exemple** — une version concrète qui fonctionne telle quelle.
3. **Sortie** — à déplier : ce que l'exemple affiche (une seule fois par besoin ; absente pour une commande
   interactive ou qui n'affiche rien).
4. **Exemple 2** — quand la commande est complexe : une variante, un filtre, un cas réel.
5. **Attention** — seulement si c'est risqué (droits root, destructif, bruyant).
6. **Ensuite** — l'étape logique suivante ; **Pour comprendre** — le chapitre du cours dans la Bibliothèque.

## Trouver une commande

- **Par besoin** : [Que veux-tu faire ?](besoins.md) liste tous les besoins ; chacun affiche ses
  commandes, et taper une commande (`tail`, `ss`) montre les besoins qui l'utilisent.
- **Par commande** : [Par commande](commandes.md), de A à Z — ce qu'elle fait, où elle sert, son
  équivalent Windows. Les plus riches ont une [fiche détaillée](linux/commandes/index.md) : options utiles,
  commandes décodées, pièges.
- **Depuis Windows** : [Linux ↔ Windows](linux-windows.md), la même commande en CMD et en PowerShell.
- Les descriptions et équivalents Windows se tiennent dans `data/commandes.yml` ; les listes se font
  toutes seules à partir des fiches.

## Paramètres

- `<PID>`, `<fichier>`, `<utilisateur>` : à remplacer à la main.
- Les exemples utilisent des adresses privées (`192.168.1.x`) ou de documentation (`203.0.113.x`).
- Pentest & CTF garde ses variables shell (`$IP`, `$LHOST`…) : voir ses [conventions](../start/conventions.md).

## Deux sortes de fiches

- **Par système** (Linux, Windows) : chaque commande y est écrite une seule fois.
- **Par métier** (Forensic, Réponse à incident, Pentest & CTF) : des procédures dans l'ordre, qui
  **reprennent** les entrées système (« Repris de… ») et ajoutent ce qui est propre au métier.
  Pour reprendre une entrée : `![[cheatsheets/linux/fondamentaux/processus#Tout savoir sur un PID]]`
  sur une ligne seule.
