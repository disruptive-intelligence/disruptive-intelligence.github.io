---
title: Bash
source: IT/07 Scripting & programmation/Shell/Bash.md
format: cours
revue: '2026-05-10'
---

*De zéro à l'automatisation — Guide pour débutant absolu*

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code.
> Tout ce dont tu as besoin, c'est un ordinateur avec Linux (ou un terminal Bash sur Mac/Windows via WSL).

---

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **Terminal** | La fenêtre noire où tu tapes des commandes texte |
| **Shell** | Le programme qui lit et exécute tes commandes (Bash est un shell) |
| **Script** | Un fichier texte contenant une liste de commandes à exécuter |
| **Variable** | Un conteneur avec un nom qui stocke une valeur |
| **Argument** | Une info que tu donnes à un script quand tu le lances |
| **Commande** | Une instruction que le shell sait exécuter (`echo`, `ls`, `cd`...) |
| **Sortie standard (stdout)** | Là où une commande affiche son résultat (l'écran par défaut) |
| **Sortie d'erreur (stderr)** | Là où une commande affiche ses erreurs (l'écran aussi par défaut) |
| **Code de retour** | Un nombre (0 = succès, autre = erreur) que chaque commande renvoie |
| **Boucle** | Un mécanisme qui répète des commandes plusieurs fois |
| **Fonction** | Un bloc de code réutilisable auquel on donne un nom |
| **Pipe** | Un "tuyau" (`\|`) qui envoie la sortie d'une commande vers une autre |

---

### Comment penser un script

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. **Tout script suit le même schéma :**

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```


Concrètement, il n'y a que 5 briques de base dans un script :

1. **Recevoir** des données (arguments, saisie utilisateur, fichier...)
2. **Stocker** des informations dans des variables
3. **Tester** si quelque chose est vrai ou faux (conditions)
4. **Répéter** une action plusieurs fois (boucles)
5. **Afficher ou enregistrer** un résultat (sortie)

Tous les scripts, même les plus complexes, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

---

### Table des matières

1. [Découverte de Bash et premier script](01-chapitre-1-decouverte-de-bash-et-premier-script.md)
2. [Variables, affichage et saisie utilisateur](02-chapitre-2-variables-affichage-et-saisie-utilisate.md)
3. [Arguments et variables spéciales](03-chapitre-3-arguments-et-variables-speciales.md)
4. [Redirections, erreurs et pipes](04-chapitre-4-redirections-erreurs-et-pipes.md)
5. [Opérateurs, calculs et logique](05-chapitre-5-operateurs-calculs-et-logique.md)
6. [Conditions, comparaisons et tests](06-chapitre-6-conditions-comparaisons-et-tests.md)
7. [Boucles](07-chapitre-7-boucles.md)
8. [Fonctions et case](08-chapitre-8-fonctions-et-case.md)
9. [Chaînes de caractères](09-chapitre-9-chaines-de-caracteres.md)
10. [Tableaux](10-chapitre-10-tableaux.md)
11. [Déboguer et écrire des scripts propres](11-chapitre-11-deboguer-et-ecrire-des-scripts-propres.md)
12. [Cas pratiques et automatisation](12-chapitre-12-cas-pratiques-et-automatisation.md)

---

## Sommaire

- [Chapitre 1 — Découverte de Bash et premier script](01-chapitre-1-decouverte-de-bash-et-premier-script.md)
- [Chapitre 2 — Variables, affichage et saisie utilisateur](02-chapitre-2-variables-affichage-et-saisie-utilisate.md)
- [Chapitre 3 — Arguments et variables spéciales](03-chapitre-3-arguments-et-variables-speciales.md)
- [Chapitre 4 — Redirections, erreurs et pipes](04-chapitre-4-redirections-erreurs-et-pipes.md)
- [Chapitre 5 — Opérateurs, calculs et logique](05-chapitre-5-operateurs-calculs-et-logique.md)
- [Chapitre 6 — Conditions, comparaisons et tests](06-chapitre-6-conditions-comparaisons-et-tests.md)
- [Chapitre 7 — Boucles](07-chapitre-7-boucles.md)
- [Chapitre 8 — Fonctions et case](08-chapitre-8-fonctions-et-case.md)
- [Chapitre 9 — Chaînes de caractères](09-chapitre-9-chaines-de-caracteres.md)
- [Chapitre 10 — Tableaux](10-chapitre-10-tableaux.md)
- [Chapitre 11 — Déboguer et écrire des scripts propres](11-chapitre-11-deboguer-et-ecrire-des-scripts-propres.md)
- [Chapitre 12 — Cas pratiques et automatisation](12-chapitre-12-cas-pratiques-et-automatisation.md)
