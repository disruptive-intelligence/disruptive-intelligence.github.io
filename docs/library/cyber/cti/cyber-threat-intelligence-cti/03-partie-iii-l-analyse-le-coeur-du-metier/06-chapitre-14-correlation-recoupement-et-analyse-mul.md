---
title: Chapitre 14 — Corrélation, recoupement et analyse multi-sources
source: Cyber/01_CTI/CTI.md
note: Cyber Threat Intelligence (CTI)
up:
- - Cyber Threat Intelligence (CTI)
  - ../index.md
- - 'Partie III — L''analyse : le cœur du métier'
  - index.md
---

## 14.1 Les types de corrélation

La **corrélation technique** est la plus directe : le même IoC (hash, domaine, IP) apparaît dans deux sources indépendantes. Si le domaine C2 de l'incident EDE apparaît dans un rapport Mandiant sur une campagne Sandworm, c'est une corrélation technique forte — mais il faut vérifier que les deux sources sont réellement indépendantes (Mandiant n'a-t-il pas simplement ingéré les IoC d'EDE via un feed ?).

La **corrélation TTP** est plus nuancée : les mêmes techniques ATT&CK sont observées dans deux incidents. C'est un indice de possible lien — mais les techniques ATT&CK sont partagées par de nombreux acteurs (T1059.001 PowerShell est utilisé par quasiment tout le monde). C'est la procédure (le « comment exactement ») qui discrimine, pas la technique générique.

La **corrélation victimologique** est sous-utilisée et pourtant puissante : le même type de victime (secteur énergie, même géographie, même profil d'organisation) est ciblé dans plusieurs incidents. Si 4 opérateurs d'énergie européens sont ciblés en 6 mois avec des TTP similaires, la probabilité d'un même acteur avec un programme de ciblage systématique est élevée.

## 14.2 Le faisceau d'indices

Aucune corrélation isolée ne suffit pour une conclusion. C'est la convergence de multiples corrélations indépendantes qui construit la confiance. Un IoC partagé + des TTP similaires + une victimologie cohérente + un timing compatible + une infrastructure avec les mêmes patterns d'enregistrement = un faisceau d'indices qui soutient l'attribution. Un seul de ces éléments isolé ne suffit pas — les IoC sont réutilisables, les TTP sont partagées, et la victimologie peut être coïncidentielle.

## 14.3 Le danger de la circularité

La circularité est le piège le plus insidieux de la corrélation. La source A publie un rapport attribuant une campagne à APT28. La source B reprend cette attribution dans son propre rapport, en citant A. La source C cite B. L'analyste voit « 3 sources indépendantes attribuent à APT28 » — mais en réalité, une seule source a fait l'analyse, les deux autres l'ont propagée. La « corroboration » est illusoire. Contremesure : toujours remonter à la source primaire. Si les 3 rapports citent les mêmes IoC et la même analyse, c'est une seule source, pas trois.

---
