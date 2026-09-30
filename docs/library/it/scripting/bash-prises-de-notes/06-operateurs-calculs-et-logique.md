---
title: Opérateurs, calculs et logique
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

- Calcul en bash avec nombres entiers : $(( expression )), $((var1 + var2))
    
    ```bash
    a=10
    b=3
    
    echo "Addition      : $((a + b))"      # 13
    echo "Soustraction  : $((a - b))"      # 7
    echo "Multiplication: $((a * b))"      # 30
    echo "Division      : $((a / b))"      # 3 (entière, pas de virgule !)
    echo "Modulo        : $((a % b))"      # 1 (reste de la division)
    ```
    
    - Attention : la division est entière. 10 / 3 donne 3, pas 3.33.
    - Ex :
        
        ```bash
        result=$(($1 % 2))
        
        if (( result == 0 )); then
            echo "$1 est bien pair"
        else 
            echo "$1 impair"
        fi
        ```
        
- Opérateurs arithmétiques : +, -, *, /, %, **
    
    
    | Opérateur | Signification | Exemple | Résultat |
    | --- | --- | --- | --- |
    | `+` | Addition | `$((5 + 3))` | `8` |
    | `-` | Soustraction | `$((5 - 3))` | `2` |
    | `*` | Multiplication | `$((5 * 3))` | `15` |
    | `/` | Division entière | `$((5 / 3))` | `1` |
    | `%` | Modulo (reste) | `$((5 % 3))` | `2` |
    | `**` | Puissance | `$((2 ** 3))` | `8` |
    | `variable++` | incrémentation valeur de la variable par 1 |  |  |
    | variable— | décrémentation valeur de la variable par 1 |  |  |

    - En bash, les calculs prennent souvent la forme suivante :
        
        ```bash
        $(( ... ))
        
        echo $((10 + 10))
        ```
        
    - Ex :
        
        ```bash
        increase=1
        decrease=1
        
        echo "Addition: 10 + 10 = $((10 + 10))"
        echo "Subtraction: 10 - 10 = $((10 - 10))"
        echo "Multiplication: 10 * 10 = $((10 * 10))"
        echo "Division: 10 / 10 = $((10 / 10))"
        echo "Modulus: 10 % 4 = $((10 % 4))"
        
        ((increase++))
        echo "Increase Variable: $increase"
        
        ((decrease--))
        echo "Decrease Variable: $decrease"
        ```
        
    - Le modulo `%`
        
        ```
        $((10 % 4))
        ```
        
        donne :
        
        - reste de la division de 10 par 4
        - donc `2`
        
        ### Utilité concrète
        
        Très utile pour :
        
        - pair / impair
        - cycles
        - répétitions périodiques
        
        Exemple :
        
        - un nombre est pair si `nombre % 2 == 0`
- Stocker résultat : nom_var=$(var1 opérateur var2), prix_final=$((prix - reduction))
    
    ```bash
    prix=50
    reduction=15
    prix_final=$((prix - reduction))
    echo "Le prix final est $prix_final euros"
    ```
    
    - Ex :
        
        ```bash
        result=$(($1 % 2))
        
        if (( result == 0 )); then
            echo "$1 est bien pair"
        else 
            echo "$1 impair"
        fi
        ```
        
- Opérateurs chaînes de caractères : = ou == (identiques), ≠ (! = différentes), -z (chaïne vide), -n (chaïne n’est pas vide)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `=` ou `==` | Les chaînes sont identiques |
    | `!=` | Les chaînes sont différentes |
    | `-z` | La chaîne est vide |
    | `-n` | La chaîne n'est pas vide |
    | < | Plus petit dans alphabet ASCII |
    | > | Plus grand dans alphabet ASCII |
    
    ```bash
    nom="Alice"
    [[ "$nom" == "Alice" ]]    # Vrai
    [[ "$nom" != "Bob" ]]      # Vrai
    [[ -z "$nom" ]]            # Faux (pas vide)
    ```
    
    - Ex :
        - Tester si variable contient contenus d’une autre variable
            
            ```bash
            var="8dm7KsjU28B7v621Jls" 
            value="ERmFRMVZ0U2paTlJYTkxDZz09Cg" 
            
            if [[ "$var" == *"$value"* ]]; then 
            	echo "La variable "var" contient le même contenu que "value"" 
            fi 
            ```
            
        
        ```bash
        prenom="Camille"
        
        if [[ "$prenom" == "Camille" ]]; then
            echo "Bonjour Camille"
        fi
        ```
        
        ```bash
        nom=""
        
        [[ -z "$nom" ]] && echo "Le nom est vide"
        [[ -n "$nom" ]] && echo "Le nom n'est pas vide"
        ```
        
        ```bash
        # Check the given argument
        if [ "$1" != "HackTheBox" ]
        then
            echo -e "You need to give 'HackTheBox' as argument."
            exit 1
        
        elif [ $# -gt 1 ]
        then
            echo -e "Too many arguments given."
            exit 1
        
        else
            domain=$1
            echo -e "Success!"
        fi
        ```
        
    - Table ASCII
        
        
        | **Decimal** | **Hexadecial** | **Character** | **Description** |
        | --- | --- | --- | --- |
        | 0 | 00 | NUL | End of a string |
        | ... | ... | ... | ... |
        | 65 | 41 | A | Capital A |
        | 66 | 42 | B | Capital B |
        | 67 | 43 | C | Capital C |
        | 68 | 44 | D | Capital D |
        | ... | ... | ... | ... |
        | 127 | 7F | DEL | Delete |

- Opérateurs sur les nombres : -eq (égal), -ne (différent), -lt (inférieur), -le (inférieur ou égal), -gt (supérieur), -ge (supérieur ou égal)
    
    
    | Opérateur | Signification | Moyen mnémotechnique |
    | --- | --- | --- |
    | -eq | Égal | **eq**ual |
    | -ne | Différent | **n**ot **e**qual |
    | -lt | Inférieur | **l**ess **t**han |
    | -le | Inférieur ou égal | **l**ess or **e**qual |
    | -gt | Supérieur | **g**reater **t**han |
    | -ge | Supérieur ou égal | **g**reater or **e**qual |
    
    ```bash
    age=25
    [[ $age -ge 18 ]]    # Est-ce que 25 ≥ 18 ? → Vrai
    [[ $age -eq 30 ]]    # Est-ce que 25 = 30 ? → Faux
    ```
    
    - Ex
        - Vérifier si variable à plus de n caractères
            
            ```bash
            if [[ ${#var} -gt 113450 ]]; then
            ```
            
        
        ```bash
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
        if [ $# -lt 1 ]
        then
            echo -e "Number of given arguments is less than 1"
            exit 1
        
        elif [ $# -gt 1 ]
        then
            echo -e "Number of given arguments is greater than 1"
            exit 1
        
        else
            domain=$1
            echo -e "Number of given arguments equals 1"
        fi
        ```
        
        ```bash
        age=25
        
        if [[ $age -ge 18 ]]; then
            echo "Majeur"
        fi
        ```
        
        ```bash
        tentatives=5
        
        if [[ $tentatives -gt 3 ]]; then
            echo "Trop de tentatives"
        fi
        ```
        
- Opérateur sur les fichiers : Test fichiers/dossiers : -e (fichier existe), -f (fichier normal), -d (c’est dossier), -s (fichier pas vide), -r (fichier est lisible), -w (fichier est modifiable), -x
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `-e fichier` | Le fichier existe |
    | `-f fichier` | C'est un fichier normal |
    | `-d fichier` | C'est un dossier |
    | `-s fichier` | Le fichier n'est pas vide |
    | `-r fichier` | Le fichier est lisible |
    | `-w fichier` | Le fichier est modifiable |
    | `-x fichier` | Le fichier est exécutable |
    | -s fichier | Taille > 0 |
    
    ```bash
    [[ -f "/etc/passwd" ]]    # Vrai (le fichier existe)
    [[ -d "/home" ]]          # Vrai (c'est un dossier)
    [[ ! -d $1 ]]             # $1 n'est pas un dossier
    ```
    
    - Ex :
        - -e : existe
            
            ```bash
            if [[-e"notes.txt" ]];then
            echo"Le fichier existe"
            fi
            ```
            
            ```bash
            [[ -e "$1" && -r "$1" ]]
            ```
            
        - -f : fichier normal
            
            ```bash
            if [[ -f "notes.txt" ]]; then
                echo "C'est un fichier"
            fi
            ```
            
        - -d : dossier
            
            ```bash
            if [[ -d "/home/kali" ]]; then
                echo "C'est un dossier"
            fi
            ```
            
        - -s : pas vide
            
            ```bash
            if [[ -s "rapport.txt" ]]; then
                echo "Le fichier contient quelque chose"
            fi
            ```
            
        - -r : lisible
            
            ```bash
            if [[ -r "/etc/passwd" ]]; then
                echo "Le fichier est lisible"
            fi
            ```
            
        - -w : modifiable
            
            ```bash
            if [[ -w "rapport.txt" ]]; then
                echo "Je peux écrire dedans"
            fi
            ```
            
        - -x : exécutable
            
            ```bash
            if [[ -x "script.sh" ]]; then
                echo "Le script est exécutable"
            fi
            ```
            
        - Combiner plusieurs
            
            ```bash
            chemin="$1"
            
            if [[ -z "$chemin" ]]; then
                echo "Erreur : vous devez indiquer un chemin"
                exit 1
            elif [[ ! -e "$chemin" ]]; then
                echo "Erreur : $chemin n'existe pas"
                exit 1
            elif [[ -f "$chemin" ]]; then
                echo "$chemin est un fichier"
            
                [[ -r "$chemin" ]] && echo "Le fichier est lisible" || echo "Le fichier n'est pas lisible"
                [[ -w "$chemin" ]] && echo "Le fichier est modifiable" || echo "Le fichier n'est pas modifiable"
                [[ -x "$chemin" ]] && echo "Le fichier est exécutable" || echo "Le fichier n'est pas exécutable"
            
            elif [[ -d "$chemin" ]]; then
                echo "$chemin est un dossier"
                nbr_elements=$(ls "$chemin" | wc -l)
                echo "Il y a $nbr_elements éléments dans le dossier"
            
            else
                echo "$chemin existe, mais ce n'est ni un fichier ni un dossier"
            fi
            ```
            
- Boléens et opérateurs logiques : && (ET, les conditions doivent être vraies), \|\| (OU, au moins une doit être vraie), ! (NON, inverse condition)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `&&` | ET — les deux conditions doivent être vraies |
    | `\|\|` / `||` | OU — au moins une doit être vraie |
    | `!` | NON — inverse la condition |
    
    ```bash
    age=25
    [[ $age -ge 18 && $age -le 65 ]]    # Vrai : entre 18 et 65
    
    [[ $age -lt 10 || $age -gt 60 ]]    # Faux : ni < 10, ni > 60
    
    [[ ! $age -lt 18 ]]                 # Vrai : 25 n'est PAS < 18
    [[ ! -d $1 ]]                       # $1 n'est pas un dossier
    ```
    
    - Ex :
        
        ```bash
        [[ -e "$1" && -r "$1" ]]
        ```
        
        ```bash
        age=25
        
        if [[ $age -ge 18 && $age -le 65 ]]; then
            echo "Âge dans la tranche"
        fi
        ```
        
        ```bash
        age=70
        
        if [[ $age -lt 18 || $age -gt 65 ]]; then
            echo "Tarif spécial"
        fi
        ```
        
        ```bash
        if [[ ! -d "$1" ]]; then
            echo "Ce n'est pas un dossier"
        fi
        ```
        
        ```bash
        # Check if the specified file exists and if we have read permissions
        if [[ -e "$1" && -r "$1" ]]
        then
            echo -e "We can read the file that has been specified."
            exit 0
        
        elif [[ ! -e "$1" ]]
        then
            echo -e "The specified file does not exist."
            exit 2
        
        elif [[ -e "$1" && ! -r "$1" ]]
        then
            echo -e "We don't have read permission for this file."
            exit 1
        
        else
            echo -e "Error occured."
            exit 5
        fi
        ```
        
        ```bash
        if [[ -f "$chemin" ]]; then
            echo "$chemin est un fichier"
        
            [[ -r "$chemin" ]] && echo "Le fichier est lisible" || echo "Le fichier n'est pas lisible"
            [[ -w "$chemin" ]] && echo "Le fichier est modifiable" || echo "Le fichier n'est pas modifiable"
            [[ -x "$chemin" ]] && echo "Le fichier est exécutable" || echo "Le fichier n'est pas exécutable"
        
        else
            echo "$chemin existe, mais ce n'est ni un fichier ni un dossier"
        fi
        ```
        
- Raccourcis avec && (mkdir dossier && echo “Dossier créé !” si commande réussit alors fait) et || (cd /inexistant || echo “Dossier existe pas” si commande échoue alors fait) entre commandes
    
    ```bash
    # Si la commande réussit, ALORS fait ceci
    mkdir mon_dossier && echo "Dossier créé !"
    
    # Si la commande échoue, ALORS fait cela
    cd /inexistant || echo "Le dossier n'existe pas"
    ```
    
- Incrémenter un compteur : ((var++)), ((var +=)), ((compteur++)) → 1, ((compteur += 5)) → 6
    
    ```bash
    compteur=0
    ((compteur++))       # → 1
    ((compteur++))       # → 2
    ((compteur += 5))    # → 7
    ```
    
    - Ex :
        
        ```bash
        fichiers=0
        
        ((fichiers++))
        ((fichiers++))
        
        echo "Nombre de fichiers traités : $fichiers"
        ```
        
        ```bash
        #!/bin/bash
        
        tab_name=("Camille" "Maya" "Manco" "Billal" "Alex")
        compteur=0
        
        for name in "${tab_name[@]}"; do
            echo "$compteur $name "
            ((compteur++))
        done
        ```
        
        - Compter combien d’hôtes rép, combien d’hôtes ont été testés, quand sortir de la boucle
            
            ```bash
            ((stat--))
            ((hosts_up++))
            ((hosts_total++))
            
            # ------------ fin
            
            <SNIP>
                echo -e "\nPinging host(s):"
                for host in $cidr_ips
                do
                    stat=1
                    while [ $stat -eq 1 ]
                    do
                        ping -c 2 $host > /dev/null 2>&1
                        if [ $? -eq 0 ]
                        then
                            echo "$host is up."
                            ((stat--))
                            ((hosts_up++))
                            ((hosts_total++))
                        else
                            echo "$host is down."
                            ((stat--))
                            ((hosts_total++))
                        fi
                    done
                done
            <SNIP>
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
        
- Calcul décimal pour nombres virgules avec bc
    
    ```bash
    echo "scale=2; 10 / 3" | bc
    # → 3.33
    
    resultat=$(echo "scale=2; 10 / 3" | bc)
    echo "Le résultat est $resultat"
    ```
    
- Comparer avec (( )) (syntaxe mathématique) : (( var > 5 )), (( var == 10 ))
    - Dans doubles parenthèses, utiliser symboles habituels
        
        ```bash
        a=10
        (( a > 5 ))     # Vrai
        (( a == 10 ))   # Vrai
        ```
        
        - Dans (( )), pas besoin de $ devant les variables.
    - Ex :
        
        ```bash
        a=10
        
        if (( a > 5 )); then
            echo "a est supérieur à 5"
        fi
        ```
        
        ```bash
        tentatives=4
        
        if (( tentatives >= 3 )); then
            echo "Compte bloqué"
        fi
        ```
        
        - Modulo
        
        ```bash
        result=$(($1 % 2))
        
        if (( result == 0 )); then
            echo "$1 est bien pair"
        else 
            echo "$1 impair"
        fi
        ```
        
- Vérifier que des chiffres / nombres en arguments : [[ "$1" =~ ^-?[0-9]+$ ]]
    
    ```bash
    if [[ ! "$1" =~ ^-?[0-9]+$ || ! "$2" =~ ^-?[0-9]+$ ]]; then
        echo "Erreur : les deux arguments doivent être des nombres entiers"
        exit 1
    fi
    ```
    
    - Ce que ça veut dire :
        - `^` = début
        - `?` = signe  optionnel
        - `[0-9]+` = un ou plusieurs chiffres
        - `$` = fin
        
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
        
- Quand ça plante, lire code de retour : $?
    
    ```bash
    ma_commande
    echo "Code de retour : $?"
    # 0 = tout va bien, autre chose = problème
    ```
    
- Cheat sheet
    
    
    | Élément | Usage concret |
    | --- | --- |
    | `$((a + b))` | faire un calcul |
    | `prix_final=$((prix-reduction))` | stocker un résultat |
    | `-gt`, `-lt`, `-eq` | comparer des nombres |
    | `==`, `!=`, `-z`, `-n` | comparer du texte / tester vide |
    | `&&`, ` |  |
    | `-f`, `-d`, `-e` | tester fichier / dossier / existence |
    | `((compteur++))` | compter |
    | `bc` | faire des décimales |
    | `(( a > 5 ))` | comparer des nombres simplement |
    | `$?` | voir si une commande a réussi |

- ❌ Erreur classique
    
    ```bash
    # Confondre = (affectation) et -eq (comparaison)
    if [[ $age = 18 ]]; then     # ⚠️ Compare comme du TEXTE, pas un nombre
    if [[ $age -eq 18 ]]; then   # ✅ Compare comme un NOMBRE
    
    # Oublier $(( )) pour le calcul
    resultat=5+3                  # ❌ resultat vaut le TEXTE "5+3"
    resultat=$((5 + 3))           # ✅ resultat vaut le NOMBRE 8
    ```
