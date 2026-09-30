---
title: Tableaux
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Notions Bash
up:
- - Notions Bash
  - index.md
---

- Créer tableau : tableau stocke plusieurs valeurs dans une seule variable, chaque valeur a index qui commence à 0. var=(”valeur1” “valeur2” “valeur3”) donc val1=index0 …
    
    Un tableau stocke **plusieurs valeurs** dans une seule variable. Chaque valeur a un index qui commence à 0.
    
    ```bash
    fruits=("pomme" "banane" "cerise")
    ```
    
    ```
    Index :     0         1         2
             ┌─────┐  ┌──────┐  ┌──────┐
             │pomme│  │banane│  │cerise│
             └─────┘  └──────┘  └──────┘
    ```
    
    ```bash
    domains=(www.inlanefreight.com ftp.inlanefreight.com vpn.inlanefreight.com www2.inlanefreight.com)
    ```
    
    - Attention, peut mettre plusieurs valeurs en une
        - Valeurs individuelles
        
        ```bash
        domains=(www.inlanefreight.com ftp.inlanefreight.com vpn.inlanefreight.com www2.inlanefreight.com)
        ```
        
        - Plusieurs valeurs en une car dans même guillemets
        
        ```bash
        domains=("www.inlanefreight.com ftp.inlanefreight.com vpn.inlanefreight.com" www2.inlanefreight.com)
        ```
        
- Accéder aux éléments : echo “${var[X]}”  / echo "${fruits[0]}"  peut @ = tout / tous index ${!var[@]}
    - Index commence par 0
    
    ```bash
    fruits=("pomme" "banane" "cerise")
    
    echo "${fruits[0]}"      # → pomme
    echo "${fruits[1]}"      # → banane
    echo "${fruits[@]}"      # → pomme banane cerise (tout)
    echo "${#fruits[@]}"     # → 3 (le nombre d'éléments)
    			`${!tab[@]}`       # Tous les index (0 1 2 3 4 ...)
    ```
    
- Ajouter élément / récup tous args : var+=(”valeur_ajout”) / fruits+=("kiwi") / var_tab=(”$@”)
    
    ```bash
    fruits+=("kiwi")
    echo "${fruits[@]}"      # → pomme banane cerise kiwi
    ```
    
    - Récupérer tous arguments dans tableau
        
        ```bash
        tab_names=("$@")
        
        tab_names=("$@")
        compteur=1
        
        for name in "${tab_names[@]}"; do
            echo "$compteur : $name"
            ((compteur++))
        done
        ```
        
- Modifier élément : var[X]=”nouvelle_valeur” / fruits[1]="fraise”
    
    ```bash
    fruits[1]="fraise"
    echo "${fruits[@]}"      # → pomme fraise cerise kiwi
    ```
    
- Supprimer élément : unset var[X]
    
    ```bash
    unset fruits[1]
    echo "${fruits[@]}"      # → pomme cerise kiwi
    ```
    
- Parcourir un tableau : boucle for var_tab in “${var_tab[@]}”; do echo “Valeurs : $var_tab” done
    
    ```bash
    fruits=("pomme" "banane" "cerise" "kiwi")
    
    for fruit in "${fruits[@]}"; do
        echo "Fruit : $fruit"
    done
    ```
    
    ```bash
    tab_name=("Camille" "Maya" "Manco" "Billal" "Alex")
    compteur=1
    
    for name in "${tab_name[@]}"; do
        echo "$compteur : $name"
        ((compteur++))
    done
    ```
    
    ```bash
    #!/bin/bash
    
    tab_names=("$@")
    compteur=1
    
    for name in "${tab_names[@]}"; do
        echo "$compteur : $name"
        ((compteur++))
    done
    ```
    
- Parcourir avec les index for var_index in “${var_tab[@]}”; do echo “Index $var_index : ${var_tab[$var_index]}” done
    
    ```bash
    for i in "${!fruits[@]}"; do
        echo "Index $i : ${fruits[$i]}"
    done
    ```
    
    ```bash
    for var_index in “${var_tab[@]}”; do 
    	echo “Index $var_index : ${var_tab[$var_index]}” 
    done
    ```
    
- Parcourir index de plusieurs tableaux pour associer :  for var_index in “${var_tab_1[@]}”; do echo “Tab1 : “${var_tab_1[var_index]}" - Tab2 : "${var_tab_2[var_index]}” done
    
    ```bash
    var_tab_1=...
    var_tab_2=...
    
    for var_index in “${var_tab_1[@]}”; do 
        echo “Tab1 : "${var_tab_1[var_index]}" - Tab2 : "${var_tab_2[var_index]}” 
    done
    ```
    
    ```bash
    noms=("Alice" "Bob" "Charlie")
    emails=("alice@mail.com" "bob@mail.com" "charlie@mail.com")
    
    for i in "${!noms[@]}"; do
        echo "Nom : "${noms[i]}" -- Emails : "${emails[i]}""
    done
    ```
    
    - Dans menu, faire choix :
        
        ```bash
        case $choix in
                1|2|3)
                    index=$((choix - 1))
                    echo "Nom : ${noms[index]} -- Email : ${emails[index]}"
                    pause
                    ;;
                4) 
                    echo "Vous quittez le script"
                    break 
                    ;;
                "") 
                    echo "Veuillez indiquer la personne souhaitée"; 
                    pause 
                    ;;
                *) echo "Sélectionnez votre choix"; pause ;;
            esac
        ```
        
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
        
- Trier tableau avec sort : printf "%s\n" "${tab_names[@]}" | sort / boucle for done | sort
    
    ```bash
    tab_names=("$@")    #Récupérer tous arguments
    printf "%s\n" "${tab_names[@]}" | sort
    ```
    
    - Boucle for : done | sort
        
        ```bash
        tab_names=("$@")
            for name in "${tab_names[@]}"; do
                echo "$name"
            done | sort
        ```
        
- Tableaux multi-types : Valeurs de types différents
    
    ```bash
    infos=("Alice" 25 "Paris" "admin")
    
    echo "Nom  : ${infos[0]}"
    echo "Âge  : ${infos[1]}"
    echo "Ville: ${infos[2]}"
    echo "Rôle : ${infos[3]}"
    ```
    
- Tableaux associatifs (dictionnaires) : utilisent clés nommées au lieu d’index numériques. Chaque mot (clé) a une définition (valeur) : mot_clé[def_valeur]=”contenu”  mails[Alice]="alice@mail.com” …
    
    ```bash
    declare -A mails
    
    mails[Alice]="alice@mail.com"
    mails[Bob]="bob@mail.com"
    mails[Charlie]="charlie@mail.com"
    
    for names in "${!mails[@]}"; do
        echo -e "Nom : "$names" — Email : "${mails[$names]}""
    done
    ```
    
    ```bash
    declare -A capitales
    
    capitales[France]="Paris"
    capitales[Allemagne]="Berlin"
    capitales[Espagne]="Madrid"
    
    echo "${capitales[France]}"       # → Paris
    echo "${!capitales[@]}"           # → France Allemagne Espagne (les clés)
    
    # Parcourir
    for pays in "${!capitales[@]}"; do
        echo "La capitale de $pays est ${capitales[$pays]}"
    done
    ```
    

| Syntaxe | Effet |
| --- | --- |
| `tab=("a" "b" "c")` | Créer un tableau |
| `${tab[0]}` | Accéder à l'élément 0 |
| `${tab[@]}` | Tous les éléments |
| `${#tab[@]}` | Nombre d'éléments |
| `${!tab[@]}` | Tous les index |
| `tab+=("d")` | Ajouter un élément |
| `tab[1]="x"` | Modifier un élément |
| `unset tab[1]` | Supprimer un élément |
