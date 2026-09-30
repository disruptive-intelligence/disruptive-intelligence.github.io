---
title: Notions Bash
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
---

<aside>
💡

https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html

</aside>


## Introduction [Glossaire, penser un script]

- Glossaire
    
    
    | Terme | Définition simple |
    | --- | --- |
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

- Comment penser un script : Recevoir > Stocker > Tester > Répéter > Afficher ou enregistrer
    - Tout script suit le même schéma
        
        ```powershell
          ENTRÉE           TRAITEMENT           SORTIE
          Ce que le    →   Ce que le script  →  Ce que le script
          script reçoit    fait avec            produit comme résultat
        ```
        
    - 5 briques de base dans un script :
        1. Recevoir des données (arguments, saisie utilisateur, fichier…)
        2. Stocker des informations dans des variables
        3. Tester si quelque chose est vrai ou faux (conditions)
        4. Répéter une action plusieurs fois (boucles)
        5. Afficher ou enregistrer un résultat (sortie)

## Sommaire

- [Découverte de Bash et premier script](01-decouverte-de-bash-et-premier-script.md)
- [Variables, affichage et saisie utilisateur [read, $(commande), var env, readonly]](02-variables-affichage-et-saisie-utilisateur-read-com.md)
- [Arguments et variables spéciales [$0, $1, if -z …; then … exit 1 fi]](03-arguments-et-variables-speciales-0-1-if-z-then-exi.md)
- [Redirections, erreurs et pipes [>&2, 2>/dev/null, >, >>, tee]](04-redirections-erreurs-et-pipes-2-2-dev-null-tee.md)
- [Opérateurs, calculs et logique](05-operateurs-calculs-et-logique.md)
- [Conditions, comparaisons et tests [if, elif, else…]](06-conditions-comparaisons-et-tests-if-elif-else.md)
- [Boucles](07-boucles.md)
- [Fonctions et case : bloc de code réutilisable](08-fonctions-et-case-bloc-de-code-reutilisable.md)
- [Chaînes de caractères](09-chaines-de-caracteres.md)
- [Tableaux](10-tableaux.md)
- [Déboguer et écrire scripts propres](11-deboguer-et-ecrire-scripts-propres.md)
- [Cas pratique et automatisation](12-cas-pratique-et-automatisation.md)
- [Workflow divers [ { echo … echo … } >]](13-workflow-divers-echo-echo.md)
