---
title: 'Fonctions et case : bloc de code réutilisable'
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

- Définir et appeler fonction : nom() { … }
    
    ```bash
    # 1. Définir la fonction
    saluer() {
        echo "Salut, bienvenue !"
    }
    
    # 2. L'appeler (juste son nom, sans parenthèses)
    saluer
    saluer
    ```
    
    ```bash
    function print_pars {
        echo $1 $2 $3
    }
    
    one="First parameter"
    two="Second parameter"
    three="Third parameter"
    
    print_pars "$one" "$two" "$three"
    ```
    
    - Règle : Définition doit apparaître avant l’appel dans le script
- Passer arguments à une fonction :
    - A l’intérieur de la fonction, $1, $2 … sont les arguments de la fonction (pas du script)
    
    ```bash
    saluer() {
        echo "Bonjour, $1 ! Tu as $2 ans." 
    }
    
    saluer "Alice" 25  # $1 = Alice / $2 = 25
    saluer "Bob" 30
    
    # Résultat 
    Bonjour, Alice ! Tu as 25 ans.
    Bonjour, Bob ! Tu as 30 ans.
    ```
    
    - Quand utiliser argument ? Ne pas créer fonction qui ne marche qu’avec valeur écrite en dur, faire fonction qui reçoit valeur en argument
        
        ```bash
        afficher_fichier() {
            cat "$1"
        }
        ```
        
        ```bash
        afficher_fichier notes.txt
        afficher_fichier rapport.txt
        ```
        
    - Ex
        - Script à ses propres arguments, la fonction à les sienne
            
            ```bash
            #!/bin/bash
            
            echo "Argument du script : $1"
            
            ma_fonction() {
                echo "Argument de la fonction : $1"
            }
            
            ma_fonction "test"
            
            # argument du script = bonjour
            # argument de la fonction = test
            ```
            
        - Même si utilise qu’une fois, le nom afficher_aide dit déjà ce que fait le bloc
            
            ```bash
            afficher_aide() {
                echo "Usage : $0 <option>"
            }
            ```
            
- Récupérer résultat d’une fonction : resultat=$(ma_fonction ...)
    - En bash, fonction “renvoie” souvent résultat en l’affichant avec **echo**, ensuite on récupère résultat avec :
        
        ```bash
        resultat=$(ma_fonction ...)
        ```
        
    - Ex :
        - Addition dans fonction
        
        ```bash
        addition() {
            echo $(( $1 + $2 ))
        }
        
        resultat=$(addition 15 27)
        echo "La somme est : $resultat"
        
        # - la fonction calcule `15 + 27`
        # - elle affiche `42`
        # - `$(...)` récupère cette sortie
        # - `resultat` reçoit `42`
        ```
        
    
    ```bash
    addition() {
        echo $(( $1 + $2 ))
    }
    
    resultat=$(addition "$1" "$2")
    echo "La somme est : $resultat"
    ```
    
- Variables dans fonctions : Globales v locales. local var
    - Par défaut : Var créée dans une fonction est souvent globale, ca veut donc dire qu’elle peut modifier le reste du script
        
        ```bash
        nom="Global"
        
        modifier() {
            nom="Local"
            echo "Dans la fonction : $nom"
        }
        
        echo "Avant : $nom"    # → Global
        modifier               # → Local
        echo "Après : $nom"    # → Local (affecté)
        ```
        
        - Résultat :
            - avant = Global
            - dans la fonction = Local
            - après = Local
        - La variable a été modifiée partout.
    - Garder var exclusive dans fonction
        - nom reste local à la fonction
        
        ```bash
        modifier() {
            local nom="Local"
            echo "Dans la fonction : $nom"
        }
        ```
        
        - Résultat :
            - avant = Global
            - dans la fonction = Local
            - après = Global
        
        ```bash
        #!/bin/bash
        
        nom="Global"
        
        modifier() {
            local nom="Local"
            echo "Dans la fonction : $nom"
        }
        
        echo "Avant : $nom"
        modifier
        echo "Après : $nom"
        
        remodifuer() {
            nom="Modif"
            echo "Dans le fonction test : $nom"
        }
        
        echo "Avant : $nom"
        remodifuer
        echo "Après : $nom"
        
        # résultat
        
        ┌──(kali㉿kali)-[~/Desktop/scripts]
        └─$ ./test.sh
        Avant : Global
        Dans la fonction : Local
        Après : Global
        Avant : Global
        Dans le fonction test : Modif
        Après : Modif
        ```
        
- Affecter valeur par défaut pour arguments : ${1:-"valeur"}
    - Si aucun argument n’est donné, prends cette valeur par défaut
        
        ```bash
        ${1:-"valeur"}
        
        # utilise $1 s’il existe, sinon mets "Inconnu"
        ```
        
    - Ex :
        
        ```bash
        saluer() {
            local nom=${1:-"Inconnu"}
            echo "Bonjour, $nom !"
        }
        
        saluer "Alice"
        saluer
        
        # résultat
        avec argument → Bonjour, Alice !
        sans argument → Bonjour, Inconnu !
        ```
        
- Code retour fonction return
    
    ```bash
    fichier_existe() {
        if [[ -f "$1" ]]; then
            return 0    # Succès
        else
            return 1    # Échec
        fi
    }
    
    if fichier_existe "/etc/passwd"; then
        echo "Le fichier existe."
    else
        echo "Le fichier n'existe pas."
    fi
    ```
    
    ```bash
    function given_args {
    
            if [ $# -lt 1 ]
            then
                    echo -e "Number of arguments: $#"
                    return 1
            else
                    echo -e "Number of arguments: $#"
                    return 0
            fi
    }
    
    # No arguments given
    given_args
    echo -e "Function status code: $?\n"
    
    # One argument given
    given_args "argument"
    echo -e "Function status code: $?\n"
    
    # Pass the results of the funtion into a variable
    content=$(given_args "argument")
    
    echo -e "Content of the variable: \n\t$content"
    
    # ------- shell
    CamiiKazZ@htb[/htb]$ ./Return.sh
    
    Number of arguments: 0
    Function status code: 1
    
    Number of arguments: 1
    Function status code: 0
    
    Content of the variable:
        Number of arguments: 1
    ```
    
    | **Return Code** | **Description** |
    | --- | --- |
    | `1` | General errors |
    | `2` | Misuse of shell builtins |
    | `126` | Command invoked cannot execute |
    | `127` | Command not found |
    | `128` | Invalid argument to exit |
    | `128+n` | Fatal error signal "`n`" |
    | `130` | Script terminated by Control-C |
    | `255\*` | Exit status out of range |

- Switch case : case <expression> in pattern_1) .. ;; pattern_2) .. ;; esac
    
    ```bash
    case <expression> in
        pattern_1 ) statements ;;
        pattern_2 ) statements ;;
        pattern_3 ) statements ;;
    esac
    ```
    
    ```bash
    # Available options
    echo -e "Additional options available:"
    echo -e "\t1) Identify the corresponding network range of target domain."
    echo -e "\t2) Ping discovered hosts."
    echo -e "\t3) All checks."
    echo -e "\t*) Exit.\n"
    
    read -p "Select your option: " opt
    
    case $opt in
        "1") network_range ;;
        "2") ping_host ;;
        "3") network_range && ping_host ;;
        "*") exit 0 ;;
    esac
    ```
    
- ❎ Fonction + case
    - Case choisit quoi faire + fonction contient bloc d’action
        - Fonction pour CIDR + case
        
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
        
        <SNIP>
        
        # Identify IP address of the specified domain
        hosts=$(host $domain | grep "has address" | cut -d" " -f4 | tee discovered_hosts.txt)
        
        <SNIP>
        ```
        
        ```bash
        echo -e "Additional options available:"
        echo -e "\t1) Identify the corresponding network range of target domain."
        echo -e "\t2) Ping discovered hosts."
        echo -e "\t3) All checks."
        echo -e "\t*) Exit.\n"
        
        read -p "Select your option: " opt
        
        case $opt in
            "1") network_range ;;
            "2") ping_host ;;
            "3") network_range && ping_host ;;
            "*") exit 0 ;;
        esac
        ```
        
    
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
    
    # Résultat
    ./outil.sh -l      # Liste les fichiers
    ./outil.sh -d      # Affiche la date
    ./outil.sh -h      # Affiche l'aide
    ./outil.sh -z      # "Option '-z' inconnue."
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
    
- Menu interactif avec select
    - Syntaxe simple :
        
        ```bash
        echo "Que veux-tu faire ?"
        select choix in "Date" "Utilisateur" "Quitter"; do
            echo "Tu as choisi : $choix"
        done
        ```
        
    - Ex :
        
        ```bash
        echo "Que veux-tu faire ?"
        select choix in "Lister les fichiers" "Afficher la date" "Quitter"; do
            case $choix in
                "Lister les fichiers") ls ;;
                "Afficher la date") date ;;
                "Quitter") echo "Au revoir." "Compter les lignes d'un fichier"; break ;;
                *) echo "Choix invalide." ;;
            esac
        done
        ```
        
- Décaler les arguments shift : Traiter argument un par un
    - Sert à supprimer premier argument puis à décaler tous les autres
    - En gros : je regarde `$1` >je décide quoi en faire > je fais `shift` > je passe au suivant > Pour les scripts avec des flags comme `-n 42 -s "texte"`
    - Parcourir argument avec while + shift
        
        ```bash
        while [[ $# -gt 0 ]]; do
            echo "Argument courant : $1"
            shift
        done
        
        # ce qu'il se passe 
        $# = nombre d’arguments restants
        tant qu’il en reste, on continue
        shift enlève l’argument courant
        le suivant devient $1
        ```
        
    - Shift 2 : Parfois option prend 2 morceaux (flag et sa valeur)
        
        ```bash
        -n 42 
        # $1 = -n
        # $2 = 42
        ```
        
        - Si l’on veut consommer les deux d’un coup shift 2
        
        ```bash
        while [[ $# -gt 0 ]]; do
            case $1 in
                -n) nombre="$2" ; shift 2 ;;
                -s) texte="$2" ; shift 2 ;;
                -h) echo "Aide : $0 -n <nombre> -s <texte>" ; exit 0 ;;
                *) echo "Option inconnue : $1" ; exit 1 ;;
            esac
        done
        
        echo "Nombre : $nombre"
        echo "Texte : $texte"
        ```
        
        - Ce qu’il se passe concrétement
            
            ### Cas `n`
            
            Si l’utilisateur tape :
            
            ```
            ./script.sh-n42-s bonjour
            ```
            
            au début :
            
            - `$1 = -n`
            - `$2 = 42`
            
            Le script fait :
            
            - `nombre="$2"` → donc `nombre=42`
            - `shift 2` → on enlève `n` et `42`
            
            Ensuite il reste :
            
            - `$1 = -s`
            - `$2 = bonjour`
            
            Puis le script continue.
            
        - cas très simple : `./script.sh -u alice -p secret`
            
            Au départ :
            
            - `$1 = -u`
            - `$2 = alice`
            - `$3 = -p`
            - `$4 = secret`
            
            Si tu fais :
            
            - `shift 2`
            
            alors il reste :
            
            - `$1 = -p`
            - `$2 = secret`
            
            Tu as donc “consommé” :
            
            - `u`
            - `alice`
        
- Mini modèles à retenir
    - **Modèle 1 — fonction simple**
    
    ```bash
    saluer() {
        echo "Bonjour !"
    }
    
    saluer
    ```
    
    ---
    
    - **Modèle 2 — fonction avec arguments**
    
    ```bash
    saluer() {
        echo "Bonjour, $1 !"
    }
    
    saluer "Alice"
    ```
    
    ---
    
    - **Modèle 3 — fonction qui “renvoie” un résultat**
    
    ```bash
    addition() {
        echo $(( $1 + $2 ))
    }
    
    resultat=$(addition 3 4)
    echo "$resultat"
    ```
    
    ---
    
    - **Modèle 4 — fonction avec variable locale**
    
    ```bash
    saluer() {
        local nom=${1:-"Inconnu"}
        echo "Bonjour, $nom !"
    }
    ```
    
    ---
    
    - **Modèle 5 — `case` simple**
    
    ```bash
    case $1 in
        oui) echo "Oui" ;;
        non) echo "Non" ;;
        *) echo "Inconnu" ;;
    esac
    ```
    
    ---
    
    - **Modèle 6 — `case` + fonction**
    
    ```bash
    aide() {
        echo "Utilisation : $0 [option]"
    }
    
    case $1 in
        -h) aide ;;
        *) echo "Option inconnue" ;;
    esac
    ```
