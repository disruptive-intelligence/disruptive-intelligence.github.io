---
title: Conditions, comparaisons et tests [if, elif, else…]
source: IT/07 Scripting & programmation/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

- Structure if : if condition; then # … fi
    - Règles de syntaxe :
        - Espace après et avant
        - Espace autour de l’opérateur
        - then sur la même ligne (avec ;) ou sur la ligne suivante
    
    ```bash
    if [[ condition ]]; then
        # code si la condition est vraie
    fi
    ```
    
    - **Note :** `fi` c'est `if` à l'envers. C'est la fermeture du bloc.
    - Ex :
        
        ```bash
        nombre=15
        if [[ $nombre -gt 10 ]]; then
            echo "Le nombre est supérieur à 10"
        fi
        ```
        
- if … else
    
    ```bash
    nombre=5
    if [[ $nombre -gt 10 ]]; then
        echo "Supérieur à 10"
    else
        echo "Inférieur ou égal à 10"
    fi
    ```
    
- if … elif … else : Autant de elif que l’on veut, mais un seul else (à la fin), et un seul fi
    - Autant de elif que l’on veut, mais un seul else (à la fin), et un seul fi
    - Syntaxe
        - `if` = si
        - `elif` = sinon si
        - `else` = sinon
        - `fi` = fin du bloc `if`
        
        ```bash
        if [ condition ]
        then
            commandes
        elif [ autre_condition ]
        then
            autres_commandes
        else
            commandes_par_defaut
        fi
        ```
        
    - Ex :
    
    ```bash
    value=$1
    
    if [ $value -gt "10" ]
    then
        echo "Given argument is greater than 10."
    elif [ $value -lt "10" ]
    then
        echo "Given argument is less than 10."
    else
        echo "Given argument is not a number."
    fi
    ```
    
    ```bash
    # Check for given argument
    if [ $# -eq 0 ]
    then
        echo -e "You need to specify the target domain.\n"
        echo -e "Usage:"
        echo -e "\t$0 <domain>"
        exit 1
    elif [ $# -eq 1 ]
    then
        domain=$1
    else
        echo -e "Too many arguments given."
        exit 1
    fi
    ```
    
    ```bash
    age=$1
    
    if [[ $age -lt 13 ]]; then
        echo "Tu es un enfant."
    elif [[ $age -lt 18 ]]; then
        echo "Tu es un adolescent."
    elif [[ $age -lt 65 ]]; then
        echo "Tu es un adulte."
    else
        echo "Tu es un senior."
    fi
    ```
    
    ```bash
    if [[ $# -eq 0 ]]; then
        echo "Utilisation : $0 <chemin1> [chemin2] ..." >&2
        exit 1
    fi
    
    for chemin in "$@"; do
        if [[ -f "$chemin" ]]; then
            taille=$(wc -c < "$chemin")
            echo "✓ $chemin — fichier ($taille octets)"
        elif [[ -d "$chemin" ]]; then
            nb=$(ls "$chemin" | wc -l)
            echo "✓ $chemin — dossier ($nb éléments)"
        else
            echo "✗ $chemin — n'existe pas"
        fi
    done
    ```
    
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
    
- Comparer nombres : -eq (égal), -ne (différent), -lt (inférieur), -le (inférieur ou égal), -gt (supérieur), -ge (supérieur ou égal)
    
    
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
        
- Comparer chaînes de texte : = ou == (identiques), ≠ (! = différentes), -z (chaïne vide), -n (chaïne n’est pas vide)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `=` ou `==` | Les chaînes sont identiques |
    | `!=` | Les chaînes sont différentes |
    | `-z` | La chaîne est vide |
    | `-n` | La chaîne n'est pas vide |
    
    ```bash
    nom="Alice"
    [[ "$nom" == "Alice" ]]    # Vrai
    [[ "$nom" != "Bob" ]]      # Vrai
    [[ -z "$nom" ]]            # Faux (pas vide)
    ```
    
    - Ex :
        
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
        
- Test sur fichiers & dossiers : -e (fichier existe), -f (fichier normal), -d (c’est dossier), -s (fichier pas vide), -r (fichier est lisible), -w (fichier est modifiable), -x (fichier est exec)
    
    
    | Opérateur | Signification |
    | --- | --- |
    | `-e fichier` | Le fichier existe |
    | `-f fichier` | C'est un fichier normal |
    | `-d fichier` | C'est un dossier |
    | `-s fichier` | Le fichier n'est pas vide |
    | `-r fichier` | Le fichier est lisible |
    | `-w fichier` | Le fichier est modifiable |
    | `-x fichier` | Le fichier est exécutable |
    
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
            
- Tests utiles : -f “fichier.txt”, -d "/home", -e "$1", -z "$nom", -n "$nom", $a -gt $b
    
    
    | Test | Signification | Exemple |
    | --- | --- | --- |
    | -f | Le fichier existe | -f “fichier.txt” |
    | -d | Le dossier existe | -d "/home" |
    | -e | Le chemin existe (fichier ou dossier) | -e "$1" |
    | -z | La chaîne est vide | -z "$nom" |
    | -n | La chaîne n'est pas vide | -n "$nom" |
    | -gt | Le nombre est supérieur | $a -gt $b |

- Ex concret :
    - Vérifier un fichier
        
        ```bash
        fichier=$1
        
        if [[ -z "$fichier" ]]; then
            echo "Erreur : donne un chemin en argument."
            exit 1
        fi
        
        if [[ -f "$fichier" ]]; then
            echo "$fichier est un fichier."
        elif [[ -d "$fichier" ]]; then
            echo "$fichier est un dossier."
        else
            echo "$fichier n'existe pas."
        fi
        ```
        
    - Combiner conditions
        
        ```bash
        age=$1
        nom=$2
        
        # ET : les deux doivent être vraies
        if [[ $age -ge 18 && "$nom" == "Alice" ]]; then
            echo "Alice est majeure."
        fi
        
        # OU : au moins une doit être vraie
        if [[ $age -lt 10 || $age -gt 80 ]]; then
            echo "Âge extrême."
        fi
        ```
        
- Conditions imbriquées : mettre if dans un autre if
    
    ```bash
    temperature=$1
    
    if [[ $temperature -gt 0 ]]; then
        if [[ $temperature -lt 15 ]]; then
            echo "Il fait frais."
        elif [[ $temperature -lt 25 ]]; then
            echo "Il fait bon."
        else
            echo "Il fait chaud."
        fi
    else
        echo "Il gèle !"
    fi
    ```
    
    - Si conditions imbriquées dépassent 2-3 niveaux, préférable de simplifier
- [ ] vs [](#) : Ancienne et syntaxe plus moderne
    - `[[ ]]` (la syntaxe moderne). Mais possible de voir `[ ]` dans scripts existants, c’est l’ancienne syntaxe. Elle fonctionne mais plis fragile (plante si une variable est vide et non protégée par des guillemets).
    
    ```bash
    # Avec [ ] — risqué si $nom est vide
    [ $nom = "Alice" ]     # ❌ Erreur si $nom est vide
    
    # Avec [[ ]] — pas de problème
    [[ $nom == "Alice" ]]  # ✅ Fonctionne même si $nom est vide
    ```
    
    **Règle simple :** utilise `[[ ]]` dans tes scripts. Si tu vois `[ ]` ailleurs, sache que c'est l'équivalent en plus ancien.
    
- ❌ Erreur classique
    
    ```bash
    # Oublier then
    if [[ $a -gt 5 ]]      # ❌ Erreur : "then" manquant
        echo "Grand"
    fi
    
    # Oublier les espaces
    if [[$a -gt 5]]; then   # ❌ Erreur : pas d'espace
    if [[ $a -gt 5 ]]; then # ✅ Correct
    
    # Utiliser > pour comparer des nombres
    if [[ $a > $b ]]; then      # ⚠️ Compare comme du TEXTE, pas des nombres
    if [[ $a -gt $b ]]; then    # ✅ Compare comme des NOMBRES
    
    # Oublier fi
    if [[ $a -gt 5 ]]; then
        echo "Grand"
                                 # ❌ Erreur : fi manquant
    ```
