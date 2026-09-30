---
title: Python
source: IT/05_Scripting_Langage-Prog/Python.md
chapters: 20
---

### De zéro à l'automatisation défensive — Guide pour débutant absolu

-----

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code.
> Tout ce dont tu as besoin, c'est un ordinateur (Linux, Mac ou Windows) et l'envie d'apprendre.
>
> **Orientation :** ce cours enseigne Python en s'appuyant sur des exemples de **cybersécurité défensive** (SOC, analyse de logs, OSINT, CTI, forensic léger, manipulation d'IOC). On apprend à **automatiser l'analyse**, jamais à attaquer. Tous les exemples sont légitimes et défensifs.

-----

### Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou. On y mélange volontairement les termes Python et les termes cyber, car tu vas les croiser ensemble.

| Terme            | Définition simple                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| **Terminal**     | La fenêtre où tu tapes des commandes texte pour parler à ton ordinateur                               |
| **Script**       | Un fichier texte contenant des instructions Python à exécuter                                         |
| **Variable**     | Un conteneur avec un nom qui stocke une valeur (un nombre, du texte…)                                 |
| **Type**         | La nature d'une valeur : texte (`str`), entier (`int`), décimal (`float`), vrai/faux (`bool`)         |
| **Argument**     | Une info que tu donnes à un script quand tu le lances dans le terminal                                |
| **Fonction**     | Un bloc de code réutilisable auquel on donne un nom                                                   |
| **Boucle**       | Un mécanisme qui répète des instructions plusieurs fois                                               |
| **Module**       | Un fichier Python contenant des fonctions prêtes à l'emploi que tu peux importer                      |
| **Indentation**  | Les espaces en début de ligne qui délimitent les blocs de code en Python                              |
| **Liste**        | Une collection ordonnée de valeurs, modifiable                                                        |
| **Dictionnaire** | Une collection de paires clé-valeur (comme un vrai dictionnaire : mot → définition)                   |
| **Exception**    | Une erreur qui se produit pendant l'exécution du script                                               |
| **Log**          | Un fichier journal : chaque ligne enregistre un événement (connexion, erreur, accès…)                 |
| **IOC**          | *Indicator of Compromise* : une trace observable d'une attaque (IP, domaine, hash, URL malveillante…) |
| **IP**           | L'adresse numérique d'une machine sur un réseau (ex. `192.168.1.10`)                                  |
| **Hash**         | Une empreinte numérique unique d'un fichier ou d'un texte (ex. MD5, SHA-256)                          |
| **SOC**          | *Security Operations Center* : l'équipe qui surveille et défend un système d'information              |
| **SIEM**         | Outil qui centralise et analyse les logs de sécurité de toute une organisation                        |
| **CTI**          | *Cyber Threat Intelligence* : le renseignement sur les menaces (qui attaque, comment, avec quoi)      |
| **OSINT**        | *Open Source Intelligence* : le renseignement à partir de sources publiques et ouvertes               |

-----

### Comment penser un script

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. **Tout script suit le même schéma :**

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

En cyber défensive, ce schéma est partout :

```
  Un fichier   →   On extrait les    →  Une liste d'IP
  de logs          IP suspectes         à bloquer
```

Concrètement, il n'y a que 5 briques de base dans un script :

1. **Recevoir** des données (arguments, saisie utilisateur, fichier de log…)
2. **Stocker** des informations dans des variables
3. **Tester** si quelque chose est vrai ou faux (conditions)
4. **Répéter** une action plusieurs fois (boucles)
5. **Afficher ou enregistrer** un résultat (rapport, alerte, fichier de sortie)

Tous les scripts, même un parser de logs ou un extracteur d'IOC, sont une combinaison de ces 5 briques. Garde ça en tête à chaque chapitre.

-----

### La grande différence avec Bash

Si tu viens du cours Bash de cette collection, un point fondamental va changer : **Python n'est pas un langage de commandes système, c'est un langage de programmation généraliste.**

En Bash, tu enchaînes des commandes du système (`ls`, `grep`, `cat`…) et tu les relies avec des pipes. En Python, tu écris des **instructions** que Python exécute lui-même.

Concrètement :

- En Bash, `grep "Failed password" auth.log` appelle la commande `grep` du système.
- En Python, tu écris toi-même la logique : ouvrir le fichier, parcourir les lignes, tester si chacune contient `"Failed password"`. C'est plus de code, mais infiniment plus puissant : tu peux ensuite compter, regrouper par IP, exporter en JSON, interroger une API…

Python a ses propres outils, souvent plus puissants et plus lisibles que les commandes système. Ce cours t'apprend ces outils à partir de zéro.

-----

### Table des matières

#### Partie 1 — Fondamentaux Python (orientés cyber défensive)

1. [Découverte de Python et premier script](01-chapitre-1-decouverte-de-python-et-premier-script.md)
2. [Variables, types, affichage et saisie utilisateur](02-chapitre-2-variables-types-affichage-et-saisie-utilisateur.md)
3. [Arguments, terminal et scripts paramétrés](03-chapitre-3-arguments-terminal-et-scripts-parametres.md)
4. [Opérateurs, calculs et logique](04-chapitre-4-operateurs-calculs-et-logique.md)
5. Conditions
6. Chaînes de caractères
7. Listes et boucles
8. Fonctions
9. Dictionnaires
10. Fichiers, chemins, CSV, JSON
11. Erreurs, débogage et code propre
12. Cas pratiques et automatisation

#### Partie 2 — Python pour la cybersécurité défensive

13. Regex avec `re` — extraire IP, emails, domaines, URLs, hash
14. Parsing de logs : SSH, web et événements structurés
15. Manipulation d'IOC : IP, domaines, URLs, hash
16. Requêtes HTTP et APIs CTI avec `requests`
17. JSON avancé pour APIs CTI/SIEM
18. Calcul de hash avec `hashlib`
19. Validation d'IP et réseaux avec `ipaddress`
20. Mini-projets cyber défensifs

-----

## Sommaire

1. [Chapitre 1 — Découverte de Python et premier script](01-chapitre-1-decouverte-de-python-et-premier-script.md)
2. [Chapitre 2 — Variables, types, affichage et saisie utilisateur](02-chapitre-2-variables-types-affichage-et-saisie-utilisateur.md)
3. [Chapitre 3 — Arguments, terminal et scripts paramétrés](03-chapitre-3-arguments-terminal-et-scripts-parametres.md)
4. [Chapitre 4 — Opérateurs, calculs et logique](04-chapitre-4-operateurs-calculs-et-logique.md)
5. [Chapitre 5 — Conditions](05-chapitre-5-conditions.md)
6. [Chapitre 6 — Chaînes de caractères](06-chapitre-6-chaines-de-caracteres.md)
7. [Chapitre 7 — Listes et boucles](07-chapitre-7-listes-et-boucles.md)
8. [Chapitre 8 — Fonctions](08-chapitre-8-fonctions.md)
9. [Chapitre 9 — Dictionnaires](09-chapitre-9-dictionnaires.md)
10. [Chapitre 10 — Fichiers, chemins, CSV et JSON](10-chapitre-10-fichiers-chemins-csv-et-json.md)
11. [Chapitre 11 — Erreurs, débogage et code propre](11-chapitre-11-erreurs-debogage-et-code-propre.md)
12. [Chapitre 12 — Cas pratiques et automatisation](12-chapitre-12-cas-pratiques-et-automatisation.md)
13. [Chapitre 13 — Regex avec re : extraire IP, emails, domaines, URLs et hash](13-chapitre-13-regex-avec-re-extraire-ip-emails-domaines-urls-e.md)
14. [Chapitre 14 — Parsing de logs : SSH, web et événements structurés](14-chapitre-14-parsing-de-logs-ssh-web-et-evenements-structures.md)
15. [Chapitre 15 — Manipulation d'IOC : IP, domaines, URLs, hash](15-chapitre-15-manipulation-d-ioc-ip-domaines-urls-hash.md)
16. [Chapitre 16 — Requêtes HTTP et APIs CTI avec requests](16-chapitre-16-requetes-http-et-apis-cti-avec-requests.md)
17. [Chapitre 17 — JSON avancé pour APIs CTI/SIEM](17-chapitre-17-json-avance-pour-apis-cti-siem.md)
18. [Chapitre 18 — Calcul de hash avec hashlib](18-chapitre-18-calcul-de-hash-avec-hashlib.md)
19. [Chapitre 19 — Validation d'IP et réseaux avec ipaddress](19-chapitre-19-validation-d-ip-et-reseaux-avec-ipaddress.md)
20. [Chapitre 20 — Mini-projets cyber défensifs](20-chapitre-20-mini-projets-cyber-defensifs.md)
