---
title: Chaînes de caractères
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Notions Bash
up:
- - Notions Bash
  - index.md
---

- Vérifier longueur d’une chaîne ${#mot}
    
    ```bash
    mot:="Bonjour"
    echo ${mot}
    ```
    
    - Utilité concrète : Vérifier si saisie est trop courte/longue, vérifier saisie user, vérifier qu’un arg n’est pas vide, tester format minimal
    - Exemple :
        - Demande mot de passer ou pseudo
        
        ```bash
        mdp="abc123"
        
        if [[ ${#mdp} -lt 8 ]]; then
            echo "Mot de passe trop court"
        fi
        ```
        
- Concaténation : Construire noms de fichiers, fabriquer paths, créer msg dynamiques result=$var1$var2
    
    ```bash
    debut="Bon"
    fin="jour"
    mot=$debut$fin
    echo "$mot"        # → Bonjour
    ```
    
    - Utilité concrète : construire un texte, un chemin, un nom de fichier, un message
    - Ex :
        - Créer un fichier de rapport avec date
        
        ```bash
        nom="rapport"
        date_jour="2026-03-30"
        fichier="${nom}_${date_jour}.txt"
        
        echo "$fichier"
        
        # résultat
        rapport_2026-03-30.txt
        ```
        
- Extraire une sous-chaîne : Récup préfixe, découper date, extraire partie d’un nom / code echo “${phrase:0:4}”
    
    ```bash
    phrase="Bash est génial"
    echo "${phrase:0:4}"     # → Bash     (4 caractères depuis la position 0)
    echo "${phrase:5:3}"     # → est      (3 caractères depuis la position 5)
    echo "${phrase:9}"       # → génial   (tout depuis la position 9)
    ```
    
    - **Rappel :** les positions commencent à 0.
    - Ex :
        - Obtenir 4 premiers caractères d’un identifiant
        
        ```bash
        id="ABCDEF1234"
        echo "${id:0:4}"
        
        # Resultat
        ABCD
        ```
        
        - Récupérer date
        
        ```bash
        date_du_jour="2026-03-30"
        annee="${date_du_jour:0:4}"
        mois="${date_du_jour:5:2}"
        jour="${date_du_jour:8:2}"
        
        echo "$jour/$mois/$annee"
        
        # Resultat
        30/03/2026
        ```
        
- Remplacer dans une chaîne : Modifier texte sans tout réécrire, transformer extension, adapter chemin echo “${var/pris/transformé}”
    
    ```bash
    phrase="J'adore les pommes"
    
    # Remplacer la première occurrence
    echo "${phrase/pommes/bananes}"
    # → J'adore les bananes
    
    # Remplacer TOUTES les occurrences (double slash)
    tel="01-23-45-67-89"
    echo "${tel//-/.}"
    # → 01.23.45.67.89
    ```
    
    - Ex :
        - Transformer une extension
            
            ```bash
            fichier="rapport.txt"
            echo "${fichier/.txt/.pdf}"
            
            # Résultat 
            rapport.pdf
            ```
            
        - Adapter chemin
            
            ```bash
            chemin="/home/kali/Documents"
            echo "${chemin/Documents/Desktop}"
            
            # Résultat
            /home/kali/Desktop
            ```
            
- Supprimer dans une chaine : Nettoyer valeur, retirer séparateur, préparer valeur pour script, normaliser nom de fichier : echo "${var//pris/}" / echo "${var//pris/_}"
    - Par défaut, remplace par rien
    
    ```bash
    tel="01-23-45-67-89"
    
    # Supprimer tous les tirets
    echo "${tel//-/}"
    # → 0123456789
    ```
    
    - Ex :
        - Supprimer espaces ou symboles
            
            ```bash
            nom_fichier="rapport final.txt"
            echo "${nom_fichier// /_}"
            
            # Résultat 
            rapport_final.txt
            ```
            
        - Nettoyer numéro
            
            ```bash
            port=":8080"
            echo "${port//:/}"
            
            # Résultat 
            8080
            ```
            
- Majuscules / minuscules : Normaliser écriture d’un texte : echo "${nom^^}" : tout MAJ, echo "${NOM,,}" tout MIN, echo "${nom^}"  1st mot MAJ
    
    ```bash
    nom="alice dupont"
    NOM="ALICE DUPONT"
    
    echo "${nom^^}"          # → ALICE DUPONT  (tout en majuscules)
    echo "${NOM,,}"          # → alice dupont  (tout en minuscules)
    echo "${nom^}"           # → Alice dupont  (première lettre en majuscule)
    ```
    
    - Ex :
        - Uniformiser réponses utilisateur
            
            ```bash
            reponse="oui"
            echo "${reponse^^}"
            
            # Résultat
            OUI
            ```
            
        - Mettre prenom en forme
            
            ```bash
            prenom="camille"
            echo "${prenom^}"
            
            # Résultat
            Camille
            ```
            
- Mini cas pratiques
    - Tester si une chaîne est vide
        
        ```bash
        nom=""
        [[ -z "$nom" ]] && echo "Nom est vide"       # → Nom est vide
        
        autre="Alice"
        [[ -n "$autre" ]] && echo "Autre n'est pas vide"  # → Autre n'est pas vide
        ```
        
    - Extraire extension d’un fichier
        
        ```bash
        fichier="rapport.tar.gz"
        echo "${fichier##*.}"    # → gz (tout après le dernier .)
        echo "${fichier%.*}"     # → rapport.tar (tout avant le dernier .)
        ```
        
    - Renommer rapport
        
        ```bash
        fichier="rapport.txt"
        nouveau="${fichier/.txt/.pdf}"
        echo "$nouveau"
        ```
        
    - Renommer un rapport
        
        ```bash
        fichier="rapport.txt"
        nouveau="${fichier/.txt/.pdf}"
        echo"$nouveau"
        ```
        
    - Vérifier un mot de passe trop court
        
        ```bash
        mdp="abc123"
        if [[${#mdp}-lt8 ]];then
        echo"Trop court"
        fi
        ```
        
    - Nettoyer un nom de fichier
        
        ```bash
        nom="mon rapport final.txt"
        echo"${nom// /_}"
        ```
        
    - Mettre un prénom proprement
        
        ```bash
        prenom="camille"
        echo"${prenom^}"
        ```
        

| Syntaxe | Effet |
| --- | --- |
| `${#var}` | Longueur |
| `${var:pos:len}` | Extraire une sous-chaîne |
| `${var/ancien/nouveau}` | Remplacer la 1ère occurrence |
| `${var//ancien/nouveau}` | Remplacer toutes les occurrences |
| `${var//ancien/}` | Supprimer toutes les occurrences |
| `${var^^}` | Tout en majuscules |
| `${var,,}` | Tout en minuscules |
| `${var^}` | 1ère lettre en majuscule |
