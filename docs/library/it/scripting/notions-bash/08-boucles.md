---
title: Boucles
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Notions Bash
up:
- - Notions Bash
  - index.md
---

répètent des actions, deux façons de penser: [while, pause, sleep]

- for : répéter sur liste d’éléments : for var in X; do … done / for var in {1..10..2}; do … done
    - Pour parcourir : liste de mots, suite de nombres, fichiers, arguments d’un script
    - Qu’est-ce qui change à chaque tour ? souvent la variable (fruit; fichier, i)
    - Qu’est-ce qui arrête la boucle ? la liste est terminée
    - Forme générale
        
        ```bash
        for variable in liste; do
            commande
        done
        ```
        
        ```bash
        for variable in 1 2 3 4
        do
            echo $variable
        done
        
        ```
        
        ```bash
        for variable in file1 file2 file3
        do
            echo $variable
        done
        ```
        
        ```bash
        for ip in "10.0.10.170 10.0.10.174 10.0.10.175"
        do
            ping -c 1 $ip
        done
        ```
        
    - Ex typiques
        - Parcourir tous les fichiers logs
            
            ```bash
            for fichier in *.log; do
                echo "$fichier"
            done
            ```
            
        - Parcourir une liste de mot
            
            ```bash
            for fruit in pomme banane cerise; do
                echo "J'aime la $fruit"
            done
            
            # Resultat 
            J'aime la pomme
            J'aime la banane
            J'aime la cerise
            ```
            
        - Parcourir une plage de nombres
            
            ```bash
            for i in {1..5}; do
                echo "Tour numéro $i"
            done
            ```
            
            - Parcourir avec un pas
                
                ```bash
                # Compter de 2 en 2
                for i in {0..10..2}; do
                    echo $i
                done
                # → 0, 2, 4, 6, 8, 10
                ```
                
        - Parcourir les arguments
            
            ```bash
            for arg in "$@"; do
                echo "Argument : $arg"
            done
            ```
            
        - Afficher table de multiplication d’un nombre donné
            
            ```bash
            for i in {1..10}; do
                echo "$1 x $i = $(($1 * $i))"
            done
            ```
            
        - CIDR
            
            ```bash
            # Identify Network range for the specified IP address(es)
            function network_range {
                for ip in $ipaddr
                do
                    netrange=$(whois $ip | grep "NetRange\|CIDR" | tee -a CIDR.txt)
                    cidr=$(whois $ip | grep "CIDR" | awk '{print $2}')
                    cidr_ips=$(prips $cidr)
                    echo -e "\nNetRange for $ip:"
                    echo -e "$netrange"
                done
            }
            ```
            
    - ❌ Erreurs fréquentes
        - Oublier do ou done
            
            ```bash
            for i in {1..5}
                echo "$i"
            ```
            
        - Ne pas comprendre ce que contient la variable
            - fichier ne contient qu’un seul nom de fichier à la fois, pas toute la liste
            
            ```bash
            for fichier in *.txt; do
                echo "$fichier"
            done
            ```
            
- boucle while = répéter tant qu’une condition est vraie
    - Forme générale
        
        ```bash
        while condition; do
        	commande
        done
        ```
        
    - Pour : travailler avec compteur, lire fichier ligne par ligne, répéter action tant qu’une condition est vraie, traiter progressivement arguments
    - Qu’est-ce qui change à chaque tour ? souvent compteur, argument, ou ligne lue
    - Qu’est-ce qui arrête la boucle ? dans while : la condition devient fausse
    - Ex typiques :
        - Lire un fichier de cibles
        
        ```bash
        while read -r cible; do
            echo "Scan de $cible"
        done < cibles.txt
        ```
        
        - Lire fichier ligne par ligne
            - `-r` empêche `read` d'interpréter les caractères spéciaux comme `\`. C'est une bonne pratique.
        
        ```bash
        while read -r ligne; do
            echo "Lu : $ligne"
        done < mon_fichier.txt
        ```
        
        - Compteur
        
        ```bash
        compteur=1
        while [[ $compteur -le 5 ]]; do
            echo "$compteur"
            ((compteur++))
        done
        ```
        
        - Parcourir argument avec shift
        
        ```bash
        while [[ $# -gt 0 ]]; do
            echo "Argument courant : $1"
            shift
        done
        ```
        
    - ❌ Erreurs fréquentes
        - Boucle infinie
            - Ici, compteur change jamais, donc condition reste vraie pour toujours
            
            ```bash
            compteur=1
            while [[ $compteur -le 5 ]]; do
                echo "$compteur"
            done
            ```
            
            - Solution : évoluer condition avec `((compteur++))`
        - Oublier ce que lit read : Qu’une seule ligne à la fois
            
            ```bash
            while read -r ligne; do
                echo "$ligne"
            done < fichier.txt
            ```
            
- ✅ boucle while true = faire menu (remplace select), clear
    - Intéressant de clear pour rester exclusivement sur menu
    
    ```jsx
    while true; do
        clear
        echo "---------------------------------"
    		echo "	     M A I N - M E N U"
    		echo "---------------------------------"
        echo "1. Lister tous les fichiers .txt dans le répertoire courant et en-dessous"
        echo "2. Compter le nombre de lignes dans un fichier donné"
        echo "3. Quitter"
        echo "---------------------------------"
        read -r -p "Quel est votre choix ? " choix
    
        case $choix in
            -l|lister|1) liste_all_txt ;;
            -n|number|2) compter_nbr_lignes ;;
            -q|quit|3) echo "Au revoir." ; break ;;
        esac
    done
    ```
    
- sleep : ralentir pour afficher résultat et ne pas disparaître à cause de while
    
    ```bash
    sleep .5 # Waits 0.5 second.
    sleep 5  # Waits 5 seconds.
    sleep 5s # Waits 5 seconds.
    sleep 5m # Waits 5 minutes.
    sleep 5h # Waits 5 hours.
    sleep 5d # Waits 5 days.
    ```
    
    ```bash
    liste_all_txt(){
    
        list=$(find . -type f -name "*.txt" 2>/dev/null)
    
        if [[ -z "$list" ]]; then
            echo "Il n'y a aucun fichier .txt dans le répertoire actuel ni dans les sous-dossiers"
        else
            echo -e "Voici la liste des fichiers .txt \n "$list""
        fi
        sleep 60s
    }
    [...]
    while true; do
        # Affiche menu
        clear
        echo "---------------------------------"
    	echo "	     M A I N - M E N U"
    	echo "---------------------------------"
        echo "1. Lister tous les fichiers .txt dans le répertoire courant et en-dessous"
        echo "2. Compter le nombre de lignes dans un fichier donné"
        echo "3. Quitter"
        echo "---------------------------------"
        read -r -p "Quel est votre choix ? " choix
    
        
        case $choix in
            -l|lister|1) liste_all_txt ;;
            -n|number|2) compter_nbr_lignes ;;
            -q|quit|3) echo "Au revoir." ; break ;;
        esac
    done
    
    ```
    
- Faire un “pause” pour rester dans résultat et attendre retour utilisateur
    - Syntaxe simple, faire une fonction pause
    
    ```bash
    pause(){
    
    	read -p "Appuyer sur la touche [Enter] pour continuer..." key
        
    }
    ```
    
    - Usage dans boucle while
    
    ```bash
    pause(){
    
    	read -p "Appuyer sur la touche [Enter] pour continuer..." key
        
    }
    
    liste_all_txt(){
        local list
    
        list=$(find . -type f -name "*.txt" 2>/dev/null)
    
        if [[ -z "$list" ]]; then
            echo "Il n'y a aucun fichier .txt dans le répertoire actuel ni dans les sous-dossiers"
        else
            echo -e "Voici la liste des fichiers .txt \n "$list""
        fi
        pause
    
    }
    
    compter_nbr_lignes(){
        local file
        local file_lignes
    
        read -p "Quel fichier voulez-vous analyser ? " file
    
        if [[ -z "$file" ]]; then
            echo "Veuillez renseigner un fichier"
        elif [[ ! -f "$file" ]]; then
            echo "Erreur : ce fichier n'existe pas"
        else
            file_lignes=$(<"$file" wc -l)
            echo -e "Nombre de ligne(s) dans "$file" : "$file_lignes"" 
        fi
        pause
    
    }
    
    while true; do
        # Affiche menu
        clear
        echo "---------------------------------"
    	echo "	     M A I N - M E N U"
    	echo "---------------------------------"
        echo "1. Lister tous les fichiers .txt dans le répertoire courant et en-dessous"
        echo "2. Compter le nombre de lignes dans un fichier donné"
        echo "3. Quitter"
        echo "---------------------------------"
        read -r -p "Quel est votre choix ? " choix
    
        
        case $choix in
            -l|lister|1) liste_all_txt ;;
            -n|number|2) compter_nbr_lignes ;;
            -q|quit|3) echo "Au revoir." ; break ;;
            *) echo "Sélectionnez votre choix"; pause ;;
        esac
    done
    ```
    
- Boucle until : inverse de while : boucle tant que la condition est fause
    - En pratique, while est beaucoup plus courant, until est juste une autre façon d’écrire certaines boucles
    
    ```bash
    compteur=1
    until [[ $compteur -gt 5 ]]; do
        echo "Compteur : $compteur"
        ((compteur++))
    done
    ```
    
- break & continue : sortir de la boucle / sauteur au tour suivant
    
    ```bash
    if [ $counter == 2 ]
    then
        continue
    elif [ $counter == 4 ]
    then
        break
    fi
    ```
    
    - Break : sortir de la boucle
        
        ```bash
        for i in {1..10}; do
            if [[ $i -eq 6 ]]; then
                echo "Stop à $i"
                break
            fi
            echo "Numéro $i"
        done
        # Affiche 1, 2, 3, 4, 5 puis "Stop à 6"
        ```
        
    - Continue : sauter au tour suivant
        
        ```bash
        for i in {1..5}; do
            if [[ $i -eq 3 ]]; then
                continue
            fi
            echo "Numéro $i"
        done
        # Affiche 1, 2, 4, 5 (le 3 est sauté)
        ```
        
- Le for style C (pour les plages dynamiques)
    - Syntaxe {1005} ne fonctionne pas avec des variables, pour ça :
    
    ```bash
    limite=$1
    for (( i=1; i<=limite; i++ )); do
        echo "Tour $i"
    done
    ```
    
- Boucles imbriquées
    
    ```bash
    for i in {1..3}; do
        for j in {1..3}; do
            echo "i=$i, j=$j"
        done
    done
    ```
    
- Déboguer une boucle : Ajouter echo temporaires
    - Si pas de [DEBUG], c’est que la boucle ne s’exécute pas (peut-être qu’il n’y a aucun .txt dans le dossier).
    
    ```bash
    for fichier in *.txt; do
        echo "[DEBUG] fichier = '$fichier'"    # ← ajoute ça
        # ... le reste du code
    done
    ```
