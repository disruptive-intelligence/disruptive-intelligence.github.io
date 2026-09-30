---
title: Workflow divers [ { echo … echo … } >]
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Notions Bash
up:
- - Notions Bash
  - index.md
---

- Retour à la ligne dans fichier de sortie : { echo … echo … } > fichier.txt
    - Commencer par accolade puis mettre echo + contenu et terminer par accolade et redirect
        
        ```bash
        {
                echo "Date : $(date)"
                echo "Dossier : $1"
                echo "Nombre de fichiers dans le dossier : $nbr_fichiers"
        } > rapport.txt
        
        cat rapport.txt
        ```
        
    - Ex :
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner un dossier en argument" >&2
                echo -e "Usage :\n\t$0 <dossier>"
                exit 1
        fi
        
        if [[ ! -d "$1" ]]; then
                echo "Erreur : $1 n'est pas un dossier valide" >&2
                exit 1
        fi
        
        nbr_fichiers=$(ls "$1" | wc -l)
        
        {
                echo "Date : $(date)"
                echo "Dossier : $1"
                echo "Nombre de fichiers dans le dossier : $nbr_fichiers"
        } > rapport.txt
        
        cat rapport.txt
        
        ```
        
- Vérifier que des chiffres / nombres en arguments : [[ "$1" =~ ^-?[0-9]+$ ]]
    
    ```bash
    if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
        echo "Erreur : les deux arguments doivent être des nombres entiers"
        exit 1
    fi
    ```
    
    - Ce que ça veut dire :
        - `!` : inverse le test
        - `=~` : “est-ce que `$1` correspond à ce motif ?”
        - ^-?[0-9]+$ : REGEX
        - `^` = début
        - `?` = signe  optionnel
        - `[0-9]+` = un ou plusieurs chiffres
        - `$` = fin
        - `||` : ou
        
        Donc ça accepte :
        
        - `2`
        - `45`
        - `8`
        
        Mais pas :
        
        - `abc`
        - `4a`
        - `12.5`
    - Ex :
        
        ```bash
        #!/bin/bash
        
        if [[ $# -ne 2 ]]; then
            echo "Erreur : il faut deux arguments"
            echo -e "Usage :\n\t$0 <nombre1> <nombre2>"
            exit 1
        fi
        
        if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
            echo "Erreur : les deux arguments doivent être des nombres entiers"
            exit 1
        fi
        
        echo "La somme de vos deux nombres est : $(($1 + $2))"
        echo "La différence de vos deux nombres est : $(($1 - $2))"
        echo "Le produit de vos deux nombres est : $(($1 * $2))"
        ```
        
- Faire menus différents types while true, select, case
    - While true
        - Exploiter différentes commandes
            
            ```bash
            #!/bin/bash
            
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
            
        - Associer tableaux et chercher dans index
            
            ```bash
            #!/bin/bash
            
            noms=("Alice" "Bob" "Charlie")
            emails=("alice@mail.com" "bob@mail.com" "charlie@mail.com")
            
            pause() {
                read -p "Appuyez sur la touche [Enter] pour continuer..." key
            }
            
            associer() {
            
            clear 
            
            for i in "${!noms[@]}"; do
                echo "Nom : "${noms[i]}" -- Emails : "${emails[i]}""
            done
            pause
            
            }
            
            while true; do
                clear
                echo "---------------------------------"
            	echo "	     Find the mail"
            	echo "---------------------------------"
                echo "1. Alice"
                echo "2. Bob"
                echo "3. Charlie"
                echo "4. Lister l'ensemble des agents"
                echo "5. Quitter script"
                echo "---------------------------------"
                read -r -p "L'adresse mail de quel agent souhaitez-vous ? " choix
            
                case $choix in
                    1|2|3)
                        index=$((choix - 1))
                        echo "Nom : ${noms[index]} -- Email : ${emails[index]}"
                        pause
                        ;;
                    4) 
                        associer 
                        ;;
                    5) 
                        echo "Vous quittez le script"
                        break 
                        ;;
                    "") 
                        echo "Veuillez indiquer la personne souhaitée"; 
                        pause 
                        ;;
                    *) echo "Sélectionnez votre choix"; pause ;;
                esac
            done
            
            ```
            
    - Select
        
        ```bash
        #!/bin/bash
        
        liste_all_txt(){
        
            list=$(find . -type f -name "*.txt" 2>/dev/null)
        
            if [[ -z "$list" ]]; then
                echo "Il n'y a aucun fichier .txt dans le répertoire actuel ni dans les sous-dossiers"
            else
                echo -e "Voici la liste des fichiers .txt \n\t "$list""
            fi
        }
        
        compter_nbr_lignes(){
            local file
        
            read -p "Quel fichier voulez-vous analyser ? " file
        
            file_lignes=$(wc -l "$file")
            if [[ -z "$file" ]]; then
                echo "Veuillez renseigner un fichier"
            else
                echo -e "Nombre de ligne(s) dans "$file" : "$file_lignes"" 
            fi
        }
        
        echo "Que veux-tu faire ?"
        select choix in "Lister les fichiers .txt" "Compter les lignes d'un fichier" "Quitter"; do
            case $choix in
                "Lister les fichiers .txt") liste_all_txt ;;
                "Compter les lignes d'un fichier") compter_nbr_lignes ;;
                "Quitter") echo "Au revoir." ; break ;;
                *) echo "choix invalide" ;;
            esac
        done   
        ```
        
- Modifier format date : date_heure=$(date '+%Y-%m-%d %H:%M:%S')
    
    ```bash
    $(date +%Y%m%d) # 20120902 
    date_heure=$(date '+%Y-%m-%d %H:%M:%S') # [2026-05-03 15:18:39]
    
    # Par défaut : [dim. 03 mai 2026 15:17:59 CEST]
    ```
    
- Enregistrer dans destination précise destination="/tmp/backups"
    - Ecrire variable avec destination souhaitée
    
    ```bash
    destination="$HOME/nom_dossier"
    ```
    
    ```bash
    destination="/tmp/backups"
    ```
    
- Contruire nom dossier / archive
    
    ```bash
    # --- Configuration ---
    dossiers="$1"
    destination="/tmp/backups"
    date_du_jour=$(date +%Y%m%d)
    archive="$destination/${date_du_jour}_${dossiers}.tar.gz"
    
    # --- Préparation ---
    mkdir -p "$destination"
    
    echo "=== Sauvegarde du $date_du_jour ==="
    
    tar -czf "$archive" "$dossiers"
    cd "$destination" && ls
    
    echo "=== Fin de la sauvegarde de "$dossiers" ==="
    ```
    
    - nom_archive=… : remplace les / par _ dans nom du dossier
        - si `dossier="/home/kali/Documents"`
        - alors `nom_archive="_home_kali_Documents"`
    - fichier=… construit chemin final de l’archive
        - /tmp/backups/_home_kali_Documents-2026-05-03.tar.gz
    
    ```bash
    nom_archive=$(echo "$dossier" | tr '/' '_')
    fichier="${destination}/${nom_archive}-${date_du_jour}.tar.gz"
    ```
    
    - Construire nom de fichier dynamiquement
        
        ```bash
        tar czf ~/www_backups/$(date +%Y%m%d-%H%M%S).tar.gz 
        ```
        
    - Construire archive avec date
        
        ```bash
        archive="$destination/$(date +%Y%m%d-%H%M%S).tar.gz"
        ```
        
    - Récupérer nom dossier propre
        
        ```bash
        nom_dossier=$(basename "$dossier")
        archive="$destination/${date_du_jour}_${nom_dossier}.tar.gz"
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
    
- Passer valeur en base64
    - Il faut bien réutiliser la même variable pour qu’elle soit encodé !!
    
    ```bash
    var="nef892na9s1p9asn2aJs71nIsm"
    
    for counter in {1..40}
    do
            var=$(echo $var | base64)
    done
    ```
    
- Tester si variable contient contenus d’une autre variable
    
    ```bash
    var="8dm7KsjU28B7v621Jls" 
    value="ERmFRMVZ0U2paTlJYTkxDZz09Cg" 
    
    if [[ "$var" == *"$value"* ]]; then 
    	echo "La variable "var" contient le même contenu que "value"" 
    fi 
    ```
    
- Vérifier si variable à plus de n caractères
    
    ```bash
    if [[ ${#var} -gt 113450 ]]; then
    ```
    
- Récupérer les 20 derniers caractères
    
    ```bash
    last_20=$(echo "$var" | tail -c 20)
    echo "$last_20"
    ```
    
- Sauvegarder sortie dans fichier tee
    - Syntaxe simple
        - **Voir et garder** :
        
        ```
        commande | tee fichier.txt
        ```
        
        - **Ajouter sans écraser** :
        
        ```
        commande | tee-a fichier.txt
        ```
        
    
    ```bash
    # Prend ce qu'il reçoit, l'affiche à l'écran et l'écrit dans un fichier
    hosts=$(host $domain | grep "has address" | cut -d" " -f4 | tee discovered_hosts.txt)
    
    netrange=$(whois $ip | grep "NetRange\|CIDR" | tee -a CIDR.txt)
    ```
    
- Retrouver valeur dans compteur avec if
    - Retrouver valeur d’un compteur
        
        ```bash
        var="nef892na9s1p9asn2aJs71nIsm"
        
        for counter in {1..40}
        do
            var=$(echo "$var" | base64)
        
        if [[ $counter -eq 35 ]]; then
            resultat_35="$var"
        fi
        done
        
        echo "$resultat_35"
        ```
        
    - Retrouver nombre de caractères d’une valeur
        
        ```bash
        var="nef892na9s1p9asn2aJs71nIsm"
        
        for counter in {1..40}
        do
            var=$(echo "$var" | base64)
        if [[ $counter -eq 35 ]]; then
            longueur=$(echo "$var" | wc -m)        
        fi
        done
        
        echo "$longueur"
        ```
        
- Calculer la valeur d’une variable : echo ${#variable} puis l’attribuer à une autre variable
    
    ```bash
    htb="HackTheBox"
    
    echo ${#htb}
    ```
    
    - Calculer longueur d’une variable
        
        ```bash
        longueur=$(echo "$var" | wc -m)
        echo "$longueur"
        ```
        
    - Calculer longueur puis définir résultat à une autre variable
        
        ```bash
        for counter in {1..28}
        do 
            var=$(echo "$var" | base64)
        if [[ $counter -eq 28 ]]; then
            longueur=$(echo "$var" | wc -m)
        fi
        done
        
        salt="$longueur"
        ```
        
- Entrainement divers
    - Script laisse choix avec argument (fonction+case)
        
        ```bash
        afficher_aide() {
            echo "Utilisation : $0 [option]"
            echo "  -l    Lister les fichiers"
            echo "  -d    Afficher la date"
            echo "  -h    Afficher cette aide"
        }
        
        case $1 in
            -l) ls -la ;;
            -d) date ;;
            -h) afficher_aide ;;
            "")
                echo "Erreur : aucune option fournie."
                afficher_aide
                exit 1 ;;
            *)
                echo "Option '$1' inconnue."
                afficher_aide
                exit 1 ;;
        esac
        ```
        
        ```bash
        afficher_aide() {
            echo "Options disponibles :"
            echo "  -h  aide"
            echo "  -d  date"
            echo "  -u  utilisateur"
        }
        
        case $1 in
            -h) afficher_aide ;;
            -d) date ;;
            -u) whoami ;;
            *)
                echo "Option inconnue"
                afficher_aide ;;
        esac
        ```
        
    - Faciliter scans nmap
        
        ```bash
        #!/bin/bash
        
        read -p "L'adresse à scanner : " ip_scan
        echo "Scan de $ip_scan en cours..."
        nmap -F -sV "$ip_scan"
        ```
        
        - Version optimisée avec sortie erreur
            
            ```bash
            #!/bin/bash
            
            read -p "Adresse IP ou hôte à scanner : " target
            
            if [[ -z "$target" ]]; then  # [[ .. ] : test de condition / -z : vide
                echo "Erreur : aucune cible saisie." >&2  # Affiche erreur
                exit 1  # 1 : arrêter script avec erreur
            fi  # fin du if
            
            echo "Scan de $target en cours..."
            nmap -F -sV "$target"
            ```
            
        - Evolution à faire
            - Vérifier que `$ip_scan` n'est pas vide avant de lancer le scan
            - Proposer plusieurs types de scans (rapide, complet, UDP...)
            - Sauvegarder le résultat dans un fichier
    - Faire un tableau avec plusieurs domaines à scanner
        
        ```bash
        domains=(www.inlanefreight.com ftp.inlanefreight.com vpn.inlanefreight.com www2.inlanefreight.com)
        echo ${domains[0]}
        ```
        
    - Fonction identifier plage réseau pour ip donnée
        
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
        
    - Comparaison fichier
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur, script attends <fichier1> et <fichier2>"
                exit 1
        fi
        
        echo "Comparaison de $1 et $2"
        echo "Taille de $1 :"
        wc -c < "$1"    # < "$1" = redirige le contenu du fichier $1 vers wc
        echo "Taille de $2 :"
        wc -c < "$2"
        
        ```
        
    - Traiter liste d’arguments un par un
        
        ```bash
        #!/bin/bash
        
        while [[ -n "$1" ]]; do
            echo "Argument courant : $1"
            shift
        done
        
        # lance ./script.sh un deux trois
        
        Argument courant : un
        Argument courant : deux
        Argument courant : trois
        ```
        
        ```bash
        #!/bin/bash
        while [[ $# -gt 0 ]]; do
            echo "Je traite : $1"
            shift          # on passe au suivant
        done
        ```

        ```
        ./script.sh Alice Bob Charlie
        → Je traite : Alice
        → Je traite : Bob
        → Je traite : Charlie
        ```
        
    - ❎ Prendre nom puis trouver emplacement fichier
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Veuillez renseigner le fichier que vous cherchez ./script <fichier>"
                exit 1
        fi
        
        echo "Le fichier "$1" est à l'emplacement suivant : "
        find / -iname "$1" 2>/dev/null
        ```
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez indiquer le nom d'un fichier"
                echo -e  "Usage :\n\t$0 <fichier>"
                exit 1
        fi
        
        emplacement=$(find / -iname "$1" 2>/dev/null)
        
        if [[ -z "$emplacement" ]]; then
                echo "Aucun fichier trouvé"
                echo "Le fichier $1 ne semble pas présent sur le système"
                exit 1
        fi 
        
        echo "L'emplacement de $1 :"
        echo "$emplacement"
        
        ```
        
    - Enregistrer nombre de ligne d’un fichier dans un nouveau fichier
        
        ```bash
        #!/bin/bash
        
        lignes_pass=$(cat /etc/passwd | wc -l)
        echo "Il y a "$lignes_pass" lignes dans le fichier passwd" | tee ex_pass.txt
        ```
        
    - Erreur argument expliquer comment utiliser script
        - Bien indiquer comment faire
            
            ```bash
            #!/bin/bash
            
            # Check for given argument
            if [ $# -eq 0 ]
            then
                echo -e "You need to specify the target domain.\n"
                echo -e "Usage:"
                echo -e "\t$0 <domain>"
                exit 1
            else
                domain=$1
            fi
            ```
            
            ```bash
            CamiiKazZ@htb[/htb]$ ./cidr.sh
            
            You need to specify the target domain.
            
            Usage:
                cidr.sh <domain>
            ```
            
    - Lancer commande générale pour fichier spécifique
        
        ```bash
        #!/bin/bash
        
        read -p "Quel fichier souhaitez vous analyser ?" fichier
        
        lignes=$(wc -l $fichier | tee nbr_lignes.txt)
        echo "Il y a $lignes dans $fichier"
        ```
        
    - Générer rapport concernant dossier et contenu
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner un dossier en argument" >&2
                echo -e "Usage :\n\t$0 <dossier>"
                exit 1
        fi
        
        if [[ ! -d "$1" ]]; then
                echo "Erreur : $1 n'est pas un dossier valide" >&2
                exit 1
        fi
        
        nbr_fichiers=$(ls "$1" | wc -l)
        
        {
                echo "Date : $(date)"
                echo "Dossier : $1"
                echo "Nombre de fichiers dans le dossier : $nbr_fichiers"
        } > rapport.txt
        
        cat rapport.txt
        
        ```
        
    - Menu boucle while, pause, fonctions
        
        ```bash
        #!/bin/bash
        
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
        

[cours_bash_v2.1](https://www.notion.so/cours_bash_v2-1-3263297e159780e290aae30a0564f18e?pvs=21)
