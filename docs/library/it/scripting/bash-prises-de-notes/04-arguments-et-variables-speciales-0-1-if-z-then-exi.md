---
title: Arguments et variables spéciales [$0, $1, if -z …; then … exit 1 fi]
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

- Argument : donner info directement ./script Info (=argument)
    
    ```bash
    ./saluer.sh Alice
    #                 ↑ c'est un argument
    ```
    
- Paramêtres positionnels : Argument stocké dans var numérotée ./script (=$0) Info1 (=$1) Info2 (=$2) Info3 (=$3)
    - Chaque argument stocké dans variable numérotée :
        
        ```bash
        ./mon_script.sh  pomme   banane  cerise
               $0          $1      $2      $3
        ```
        
        - `$0` → le nom du script
        - `$1` → le premier argument
        - `$2` → le deuxième
        - `$3` → le troisième...
    - Exemple : saluer.sh
        
        ```bash
        #!/bin/bash 
        echo "Bonjour, $1 !"
        ```
        
        ```bash
        ./saluer.sh Alice   # -> Bonjour, Alice !
        ./saluer.sh Bob     # -> Bonjour, Bob !
        ```
        
- ⚠️ Variables spéciales : $0 (Nom script), $1/$2/… (arguments par position), $# (nombre d’arguments), $@ (tous arguments (séparément)), $? (code de sortie de dernière commande)
    - Special variables use the [Internal Field Separator](https://bash.cyberciti.biz/guide/$IFS) (`IFS`) to identify when an argument ends and the next begins.
    
    | Variable | Contenu | Description |
    | --- | --- | --- |
    | $0 | Le nom du script | Contient le nom du script exécuté. |
    | $1, $2... | Les arguments par position | Permet d’accéder aux arguments individuellement selon leur position (ex : $1 = premier argument). |
    | $# | Le nombre d'arguments | Contient le nombre total d’arguments passés au script. |
    | $@ | Tous les arguments (séparément) | Permet de récupérer tous les arguments en ligne de commande, chacun traité séparément. |
    | $? | Le code de sortie de la dernière commande | Contient le code de retour de la dernière commande (0 = succès, autre valeur = erreur). |
    | $$ | PID du processus | Contient l’identifiant (PID) du processus en cours d’exécution. |
    | $n | Récup arg en fonction de sa position | Chaque argument peut être récupéré sélectivement en fonction de sa position.  |

    - Exemple :
        
        ```bash
        echo "Nom du script : $0"
        echo "Nombre d'arguments : $#"
        echo "Tous les arguments : $@"
        echo "Premier : $1"
        echo "Deuxième : $2"
        ```
        
        ```bash
        ./infos.sh pomme banane cerise
        ```
        
        ```bash
        Nom du script : ./infos.sh
        Nombre d'arguments : 3
        Tous les arguments : pomme banane cerise
        Premier : pomme
        Deuxième : banane
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
        
- Vérifier que argument fourni : if -z …; then … exit 1 fi, if ! -d …; then…
    - Script qui attend argument devrait toujours vérifiés qu’il a été donné :
        - -z : Chaîne vide
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then  # [[ .. ] : test de condition / -z : vide
                echo "Erreur : donne un argument !"  # sortie texte
                echo "Utilisation : $0 <prenom>"  # sortie texte, intéressant pour dire quoi faire
                exit 1  # 1 : arrêter script avec erreur
        fi # fin du if
        
        echo "Bonjour $1 !"  # si argument donné, sortie
        
        ```
        
        - Explication : -z teste si chaîne est vide. Si $1 est vide (= pas d’argument), affiche un message d’erreur et quitte.
    - ! -d : Vérifier si dossier en argument
        
        ```bash
        #!/bin/bash
        
        if [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner un dossier en argument"
                echo -e "Usage :\n\t$0 <dossier>"
                exit 1
        fi
        
        if [[ ! -d "$1" ]]; then
                echo "Erreur : $1 n'est pas un dossier valide"
                exit 1
        fi
        
        nbr_fichiers=$(ls "$1" | wc -l)
        
        echo "$(date) "$1" "$nbr_fichiers"" > rapport.txt
        cat rapport.txt
        
        ```
        
    - Ex :
        
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
        
    - Bien indiquer comment faire
        
        ```bash
        #!/bin/bash
        
        if
                [[ -z "$1" ]]; then
                echo "Erreur : Veuillez renseigner votre prénom" >&2
                echo -e "Usage :\n\t$0 <prenom>"
                exit 1
        fi
        
        echo "Bonjour, $1 !"
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
        
- Affichage sortie \n (retour à la ligne), \t (tabulation), echo -e
    - Bien indiquer echo -e pour que l’affichage soit correct
    - \n : Permet retour à la ligne
    - \t : Pemret tabulation
        
        ```bash
        if
                [[ -z "$1" ]]; then
                echo "Erreur : Veuillez indiquer le nom d'un fichier"
                echo -e  "Usage :\n\t$0 <fichier>"
                exit 1
        fi
        ```
        
        
        
- Utiliser plusieurs arguments : comparaison fichiers
    - Comparaison entre fichiers
        
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
        
- Variable $? : Renvoyer code de sortie dernière commande
    - Chaque commande renvoie un code de sortie : $? contient code de la dernière commande :
        
        ```bash
        ls /tmp
        echo $?    # → 0 (succès, le dossier existe)
        
        ls /dossier_inexistant
        echo $?    # → 2 (erreur, le dossier n'existe pas)
        ```
        
- Différence entre $@ (préserve chaque argument, 2 éléments) et $* (fusionne tout 1 seul bloc)
    
    ```bash
    ./test.sh "Jean Pierre" Marie
    ```
    
    - `"$@"` = 2 arguments : utiliser plus fréquemment
        - Jean Pierre
        - Marie
    - `"$*"` = 1 seul argument
        - Jean Pierre Marie
- Variable $$ : Contient numéro de processus (PID) du script, uttile script temp uniques : fichier_*temp*="/tmp/script_$$.tmp” : Moyen d'avoir numéro garanti unique à disposition dans  script.
    - Juste un moyen d'avoir un numéro garanti unique à disposition dans ton script.
    - Quand script lancé, système attribue numéro unique (PID). $$ contient ce numéro.
        
        ```bash
        echo "Mon PID est : $$"
        # → Mon PID est : 1234  (un nombre quelconque)
        
        Lancé deux fois de suite :
        ```
        → Mon PID : 1401
        → Mon PID : 1402
        
        # À chaque lancement num différent car nouveau programme qui démarre

        ```
        
    - Utile pour fichiers temporaires ? Parfois script besoin de créer fichier temp pour stocker données intermédiaires :
        
        ```bash
        fichier_temp="/tmp/mon_fichier.tmp"
        ```
        
        - Nom fixe, si quelqu’un lance script deux fois en même temps
            - Lancement 1 écrit dans `/tmp/mon_fichier.tmp`
            - Lancement 2 **écrase** `/tmp/mon_fichier.tmp` → le premier est corrompu
    - Avec $$ le nom devient unique automatiquement :
        
        ```bash
        fichier_temp="/tmp/mon_fichier_$$.tmp"
        # Lancement 1 → /tmp/mon_fichier_1401.tmp
        # Lancement 2 → /tmp/mon_fichier_1402.tmp  → pas de conflit
        ```
        
- shift : Décaler tous arguments d’une position : $2 devient $1…, traiter liste d’arguments un par un
    - Shift décale tous les arguments d’une position
    - Sert surtout à traiter liste d’arguments, un par un
        - Idée : lis premier argument > fais shift > passe au suivant > recommence
        
        ```bash
        #!/bin/bash
        
        echo "Avant shift :"
        echo "\$1 = $1"
        echo "\$2 = $2"
        echo "\$3 = $3"
        
        shift
        
        echo "Après shift :"
        echo "\$1 = $1"
        echo "\$2 = $2"
        echo "\$3 = $3"
        
        # lance ./script.sh alpha beta gamma
        
        Avant shift :
        $1 = alpha
        $2 = beta
        $3 = gamma
        
        Après shift :
        $1 = beta
        $2 = gamma
        $3 =
        ```
        
    - Exemple simple
        
        ```bash
        #!/bin/bash
        
        while [[ -n "$1" ]]; do # tant que le premier argument n’est pas vide, continue
            echo "Argument courant : $1"
            shift
        done
        
        # lance ./script.sh un deux trois
        
        Argument courant : un
        Argument courant : deux
        Argument courant : trois
        ```
        
        - `n` = la chaîne n’est pas vide
        - `$1` = premier argument courant
    - Au départ : `$1=Alice` `$2=Bob` `$3=Charlie/`Après un `shift` : `$1=Bob` `$2=Charlie` — Alice disparaît, tout glisse d'un cran.
        
        ```bash
        #!/bin/bash
        while [[ $# -gt 0 ]]; do  # tant qu’il reste au moins un argument, continue
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
        
        - `$#` = nombre d’arguments restants
        - `gt 0` = strictement supérieur à 0
- Cheat sheet
    
    
    | **Variable** | **Contenu** |
    | --- | --- |
    | $0 | Nom du script (ex: ./mon_script.sh) |
    | $1, $2, $3… | Arguments passés au script dans l'ordre |
    | $# | Nombre d'arguments passés |
    | "$@" | Tous les arguments séparément (préserve les espaces) — à préférer |
    | "$*" | Tous les arguments fusionnés en un seul bloc |
    | $? | Code de sortie de la dernière commande (0 = succès) |
    | $$ | PID du script — utile pour créer des fichiers temporaires uniques |
    | shift | Décale les arguments : $2 → $1, $3 → $2… (consomme $1) |
    | -z "$1" | Teste si $1 est vide → à utiliser pour vérifier qu'un argument a été donné |
    
    ⚠️ Erreurs classiques : ne pas vérifier si l'argument existe → comportement silencieux · ne pas mettre de guillemets autour de `"$1"` → plante si le fichier a des espaces dans son nom
    
- ❌ Erreur classique
    
    ```bash
    # Oublier de vérifier si l'argument existe
    echo "Bonjour, $1"    # Si lancé sans argument → "Bonjour, " (chaîne vide, pas d'erreur)
    
    # Ne pas mettre de guillemets
    cat $1                 # ❌ Plante si le fichier s'appelle "mon document.txt"
    cat "$1"               # ✅ Correct
    ```
