---
title: "Conventions"
---
# Conventions des cheat sheets

## Une entrée = un besoin

Le titre dit ce qu'on veut faire, verbe en premier (« Voir les processus enfants d'un PID »), pas le nom
de la commande : c'est ce qu'on cherche quand on est sur le poste.

Sous chaque besoin :

1. **Commande** — la forme neutre, à adapter.
2. **Exemple** — une version concrète qui fonctionne telle quelle.
3. **Exemple 2** — quand la commande est complexe : une variante, un filtre, un cas réel.
4. **Attention** — seulement si c'est risqué (droits root, destructif, bruyant).
5. **Ensuite** — l'étape logique suivante ; **Pour comprendre** — le chapitre du cours dans la Bibliothèque.

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
