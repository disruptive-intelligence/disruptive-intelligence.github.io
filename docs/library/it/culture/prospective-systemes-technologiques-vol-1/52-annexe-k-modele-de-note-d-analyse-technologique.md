---
title: Annexe K — Modèle de note d'analyse technologique
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-1.md
note: Prospective — systèmes technologiques (vol. 1)
chapter: 52
chapters: 53
---

### Format

| Section | Contenu | Longueur |
|---|---|---|
| Objet | ce dont on parle, à quel niveau, sans terme de récit | 1 ligne |
| État | échelon de preuve atteint | 3 lignes |
| Ce qui bloque | la condition dominante, et pourquoi | 3 lignes |
| Ce qui devrait devenir vrai | formulation conditionnelle | 4 lignes |
| Ordres de grandeur | deux ou trois chiffres qui calibrent | 3 lignes |
| Recommandation | l'une des cinq décisions, justifiée | 3 lignes |
| Signaux et réexamen | ce qui la ferait changer, et quand | 4 lignes |
| Ce que j'ignore | explicite | 2 lignes |

### Exemple rempli

> **Objet.** Système de perception embarquée destiné à la détection d'anomalies sur ligne de production — plateforme, non brique.
>
> **État.** Pilote chez trois industriels, sur des périmètres restreints, depuis moins de douze mois. Pas de retour d'exploitation sur une année complète. Échelon : pilote, pas produit.
>
> **Ce qui bloque.** Condition ③ — fiabilité. Le taux de détection annoncé est mesuré sur les défauts connus ; le comportement sur les défauts non représentés dans les données d'entraînement n'est pas caractérisé. Aucun domaine d'emploi n'est formellement défini.
>
> **Ce qui devrait devenir vrai.** Si un exploitant publie douze mois de données incluant les faux négatifs, et si un domaine d'emploi explicite est défini avec une détection de sortie de domaine, alors le déploiement sur nos lignes critiques devient envisageable. Si l'un des deux manque, l'usage reste limité aux lignes non critiques avec relecture humaine.
>
> **Ordres de grandeur.** Coût d'acquisition estimé : X par ligne. Coût d'un défaut non détecté parvenant au client : environ 30 fois supérieur. Volume : Y pièces par jour et par ligne.
>
> **Recommandation.** Expérimenter, sur une ligne non critique, six mois, avec relecture systématique et comptage des faux négatifs. Ne pas déployer.
>
> **Signaux et réexamen.** Réexamen dans neuf mois. Signaux : publication de données d'exploitation par un tiers ; apparition d'une offre assurable ; ou taux de faux négatifs mesuré chez nous sous le seuil défini.
>
> **Ce que j'ignore.** Le comportement du système sur nos défauts spécifiques, non représentés dans ses données. Le coût réel de maintenance et de réétalonnage sur trois ans.

---


## Annexe L — Plan de maintenance du volume

### Principe

> **Aucun chiffre daté ne doit être nécessaire à la validité d'un principe durable.**

Si une mise à jour oblige à réécrire un raisonnement, le passage est mal construit et doit être signalé comme dette de maintenance.

### Cycle recommandé

| Fréquence | Action |
|---|---|
| Annuelle | vérifier les entrées de classe A de l'Annexe I |
| À chaque réédition | vérifier les classes B et C ; relire les chapitres à forte teneur périssable |
| À chaque réédition | vérifier que les cinq affirmations à sourcer restantes ont été traitées |
| Tous les trois ans | réexaminer le corpus de la Partie IV : un cas en cours peut être devenu clos |

### Chapitres à surveiller en priorité

**Forte teneur :** 10 (coûts industriels), 12 (filières), 13 (densités, raccordement), 17 (séquençage, attrition), 18 (congestion orbitale), 25 (contrôles à l'export), 26 (délais de raccordement), 28 (cadre réglementaire).

**Faible teneur, relecture de vraisemblance suffisante :** 8, 9, 11, 14, 16, 19, 20, et l'ensemble des Parties I, IV et V.

### Cas particuliers

**Chapitre 15.** Le corps ne contient aucune donnée d'état de l'art, par conception. Vérifier à chaque réédition que cette discipline a été maintenue.

**Chapitre 19.** S'interdit toute projection. Si une trajectoire s'y clôt — une approche devient industrielle —, le cas doit migrer vers la Partie IV et non enfler le chapitre 19.

**Chapitre 35.3, véhicule électrique.** Cas explicitement non clos. Le réexaminer à chaque réédition : s'il se referme, il devient un cas de plein droit et le corpus passe à quatorze.

**Chapitre 28.6, règlement européen sur l'IA.** Le plus périssable du volume. Vérification obligatoire avant toute diffusion.

---
