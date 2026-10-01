---
title: Chapitre 40 — Énergie et calcul
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie IV — Les grandes convergences
  - index.md
---

## ① La capacité recherchée

**Ce dossier ne vise pas une capacité mais une question.**

> **Qu'est-ce qui borne réellement la croissance de la capacité de calcul — et le calcul devient-il contraint par l'énergie avant de l'être par les transistors ?**

**Pourquoi ce dossier existe.** Parce que c'est la seule convergence de la partie où **les deux couches en amont de tout l'atlas se rencontrent**, et parce que la réponse détermine des décisions d'implantation, d'investissement et de politique publique.

---

## ② Les briques nécessaires

| Couche | Entrées d'atlas |
|---|---|
| **Calculer** | accélérateurs (8) · chiplets et assemblage (8) · mémoires à forte bande passante (8) · compute-in-memory (8) · calcul faible précision (8) · photonique intégrée (9) · calcul photonique (9) |
| **Alimenter** | réseaux électriques pilotés (23) · raccordement et files d'attente (23) · électronique de puissance (23) · petits réacteurs modulaires (22) |
| **Relier** | edge/on-device/embarqué (25) · continuum cloud-edge (25) |
| **Fabriquer** | semi-conducteurs à grand gap (19) · matériaux critiques (19) |

**Quinze entrées**, et la chaîne qu'elles forment est le sujet du dossier.

---

## ③ Ce qui empêche encore — la chaîne de goulets

**Ce dossier est le seul dont le verrou se lit comme une chaîne**, et le volume 1 en avait établi le mécanisme sans pouvoir l'observer sur un cas ouvert.

```text
   ① capacité de calcul par puce
        ↓  largement améliorée par la spécialisation et l'assemblage
   ② accès mémoire et bande passante
        ↓  attaqué par l'empilement, le calcul en mémoire, la faible précision
   ③ énergie consommée et densité de puissance
        ↓  attaqué par la spécialisation et les semi-conducteurs à grand gap
   ④ évacuation de la chaleur
        ↓  attaqué par le refroidissement liquide
   ⑤ raccordement électrique du site
        ↓  procédures, files d'attente, délais en années
   ⑥ fabrication d'équipements de réseau
        ↓  transformateurs, postes, lignes — carnets en années
```


**Chaque étage a été le goulet dominant, a été partiellement traité, et a révélé le suivant.** C'est le principe P8 du volume 1, observé sur une chaîne complète et documentée.

---

## ④ Le maillon le plus en retard

**Le raccordement électrique et les délais d'équipement de réseau.**

**L'argument, et il est arithmétique.** Construire un bâtiment de calcul se compte en mois ; obtenir la puissance se compte en années — sept à dix dans plusieurs marchés développés, jusqu'à une décennie dans certains pôles. **Le rapport des durées est de un à quatre.**

**Et une file d'attente n'est pas une capacité.** Sur l'ensemble des demandes de raccordement déposées aux États-Unis entre 2000 et 2019, une petite minorité avait atteint l'exploitation commerciale, l'essentiel ayant été retiré. **Confondre un carnet de projets annoncés avec une capacité future est une erreur d'échelon de preuve.**

**Ce que le dossier doit démontrer.** Une amélioration de l'efficacité par opération **ne change pas le calendrier d'un projet dont le raccordement est attendu pour dans plusieurs années**. C'est la démonstration la plus nette de tout le volume que le verrou n'est pas dans la couche où l'attention se porte.

**Position par rapport à la thèse.** Les couches éponymes sont *calculer* et *alimenter* ; le maillon en retard est **industriel et institutionnel** — procédure administrative et carnet de commandes de transformateurs. **La thèse est vérifiée.**

---

## ⑤ Quel mur domine

**La dissipation.** Un centre de calcul transforme la quasi-totalité de son électricité en chaleur — le résultat d'un calcul ne pèse rien et n'emporte aucune énergie. **La densité de puissance évacuable borne ce qu'on peut faire fonctionner**, à l'échelle de la puce comme à celle du bâtiment.

**Le coût du déplacement**, au sens de la bande passante mémoire à l'inférence : c'est l'étage ② de la chaîne, et il reste actif.

---

## ⑥ Ce qui est en train de changer

**L'assemblage avancé** est devenu le principal levier de performance, davantage que la réduction des dimensions.

**Le refroidissement liquide** se généralise, imposé par la densité de puissance par baie — ce n'est pas un raffinement mais un changement de nature de l'installation.

**Les contrats d'approvisionnement électrique dédiés** apparaissent, y compris avec des moyens de production construits pour l'usage.

**Ce qui n'a pas changé.** Les délais de raccordement. Les carnets de commandes des fabricants de transformateurs. Et l'énergie d'un accès à une mémoire externe.

---

## ⑦ Ce que la convergence débloquerait

**Rien de spectaculaire, et c'est le point.** Si le raccordement se desserrait, la capacité de calcul croîtrait au rythme de la production de composants — c'est-à-dire au rythme qu'elle aurait dû suivre.

**La conséquence intéressante est ailleurs, et elle est géographique.** Si le raccordement reste le verrou, **la localisation du calcul suit la disponibilité électrique et non la demande**. Les installations se déplacent vers les zones où la puissance est disponible et raccordable, indépendamment de la proximité des utilisateurs — sauf pour les charges sensibles à la latence, qui restent contraintes.

**C'est une prédiction de déplacement, pas de ralentissement**, et c'est ce que ce dossier apporte au-delà du volume 1.

---

## ⑧ Le verrou suivant

**La production d'équipements de réseau et la disponibilité de matériaux.**

Si les procédures s'accélèrent, le goulet devient industriel : transformateurs, postes, câbles, et les matériaux qu'ils consomment — cuivre notamment, dont l'offre minière ne répond pas avant quinze ans.

**Et un verrou de troisième ordre.** Si la capacité de réseau croît, le goulet devient la **production d'électricité pilotable disponible localement**, ce qui renvoie au chapitre 22.

---

## ⑨ La chronologie conditionnelle

```text
① si les procédures de raccordement se raccourcissent significativement
        → alors la fabrication d'équipements de réseau devient limitante

② si cette capacité industrielle croît
        → alors la production d'électricité pilotable disponible localement
          devient limitante

③ si aucun des trois ne se débloque
        → la localisation du calcul suit la disponibilité électrique,
          et non la demande

④ si l'efficacité énergétique par unité de travail utile progresse
   plus vite que la demande
        → la contrainte se desserre sans que rien ne soit débloqué
```


**L'étape ④ est la seule qui échappe à la chaîne**, et elle dépend d'un effet rebond : si le coût de l'unité de travail baisse et que la demande n'est pas saturée, l'usage augmente et absorbe le gain. **La question est celle de la saturation, et elle n'est pas tranchée.**

---

## ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** Les **délais de raccordement publiés par zone**, et leur évolution. Les **carnets de commandes des fabricants de transformateurs**. L'**efficacité énergétique par unité de travail utile** — non par opération, qui ne dit rien du système. Et les **contrats d'approvisionnement dédiés**, qui indiquent que les acteurs contournent le réseau plutôt que de l'attendre.

**Signaux non informatifs.** La puissance de calcul par puce. Les annonces de capacité en construction, qui sont des files d'attente. Les records d'efficacité sur des charges de référence.

**Ce qui réfuterait l'analyse.** Les délais de raccordement baissent nettement dans un marché majeur. La demande de calcul sature. Ou bien l'efficacité progresse assez vite pour que la demande électrique se stabilise — ce qui invaliderait la chaîne entière.

---
