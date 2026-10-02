---
title: Introduction [Glossaire, penser un script]
source: IT/07 Scripting & programmation/Shell/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

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
