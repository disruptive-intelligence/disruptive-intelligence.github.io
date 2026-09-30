---
title: Notions Bash
source: IT/05_Scripting_Langage-Prog/Notion_Bash.md
---

<aside>
💡

https://tldp.org/LDP/Bash-Beginners-Guide/html/index.html

</aside>

### Introduction [Glossaire, penser un script]

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

### Découverte de Bash et premier script

- Terminal (fenêtre où tape commandes) & shell (programme à l’intérieur du terminal qui comprend et exécute commandes)
    - Pour ouvrir terminal :
        - **Linux** : `Ctrl + Alt + T` ou cherche "Terminal" dans tes applications
        - **Mac** : cherche "Terminal" dans Spotlight
        - **Windows** : installe WSL (Windows Subsystem for Linux)
    - Vérifier quel shell on utiliser
        
        ```powershell
        echo $SHELL
        ```
        
- Premier script : plusieurs commandes rangées dans un fichier.
    1. Crée un dossier de travail 
        
        ```powershell
        mkdir -p ~/mes_scripts
        cd ~/mes_scripts
        ```
        
    2. Crée fichier 
        
        ```powershell
        nano hello.sh
        ```
        
    3. Ecrire script 
        
        ```powershell
        #!/bin/bash
        # Mon tout premier script
        echo "Hello, World !"
        echo "Je suis un script Bash !"
        ```
        
    4. Rendre exédcutable fichier
        
        ```powershell
        chmod +x fichier.sh
        ```
        
    5. Lancer le script
        
        ```powershell
        ./hello.sh
        ```
        
- Shebang : #!/bin/bash
    - Première ligne #!/bin/bash s’appelle shebang. Dit au système “ce fichier doit être lu par Bash”
    - Sans shebang, système ne sait pas quel langage utiliser.
    - Toujours mettre shebang en première des scripts
- Pourquoi ./ devant script ?
    - Quand tape ls ou date, système sait trouver ces commandes grâce à variable PATH.
    - Dossier perso pas dans PATH, donc préciser “cherche dans dossier actuel”.
- Commande exit
    - exit permet de terminer un script avec code de sortie
    - Code essentiels :
        
        
        | Code | Signification |
        | --- | --- |
        | 0 | Succès (tout s’est bien passé) |
        | 1 | Erreur générale |
        | 127 | Commande introuvable |
    - A retenir : en Bash, `0` = succès, tout autre nombre = erreur. C'est l'inverse de ce qu'on pourrait penser !
    - Pour info, d'autres codes existent (`2` = mauvaise utilisation, `130` = Ctrl+C, `126` = pas le droit d'exécuter), mais tu n'as pas besoin de les mémoriser maintenant.
- Cheat sheet
    
    
    | **Commande / Syntaxe** | **Effet** |
    | --- | --- |
    | #!/bin/bash | Shebang — dit au système d'utiliser Bash. Toujours en 1ère ligne |
    | echo $SHELL | Vérifie quel shell est actif (doit afficher /bin/bash) |
    | nano script.sh | Crée ou ouvre un fichier script dans l'éditeur nano |
    | chmod +x script.sh | Rend le script exécutable (à faire une seule fois) |
    | ./script.sh | Lance le script depuis le dossier actuel |
    | bash script.sh | Lance le script sans avoir fait chmod +x |
    | exit 0 | Termine le script — succès |
    | exit 1 | Termine le script — erreur |
    | # commentaire | Ligne ignorée par Bash, sert à documenter le code |
- ❌ Erreur classique
    
    ```powershell
    # Oublier le shebang → le script peut ne pas fonctionner avec ./script.sh
    # Oublier chmod +x → "Permission denied" quand tu lances le script
    # Oublier le ./ → "command not found"
    ```
    
- Exercices
    
    **Guidé :** Crée un script `salut.sh` qui affiche deux lignes : "Bonjour !" puis "Bienvenue dans le monde du scripting."
    
    **Autonome :** Crée un script `info.sh` qui affiche ton nom d'utilisateur (`whoami`), la date (`date`), et le dossier actuel (`pwd`) sur des lignes séparées.
    
    ![image.png](attachment:8a8fc784-f60b-4af2-a4a9-3c92a090c4b5:image.png)
    

### Variables, affichage et saisie utilisateur [read, $(commande), var env, readonly]

- Variable : Conteneur avec étiquette, étiquette nom et à l’intérieur il y a valeur
    
    ```powershell
    │ prenom = Alice │ ← "prenom" est le nom, "Alice" est la valeur
    ```
    
- Créer et afficher variable
    
    ```powershell
    #!/bin/bash
    
    prenom="Alice"
    echo "Bonjour, $prenom !"
    ```
    
    - Règle critique : PAS d’espace autour du =
- Accèder au contenu d’une variable : Mettre $ devant son nom
    
    ```powershell
    echo "Bonjour, $prenom"     # → Bonjour, Alice
    echo "Bonjour, prenom"      # → Bonjour, prenom
    ```
    
    - Bonne pratique : Ecrire “$prenom” (avec guillemets plutôt que sans, évite problèmes si valeur contient espaces
- Forme avec accolades ${variable} : Eviter ambiguïtés
    
    ```powershell
    animal="chat"
    echo "J'ai 3 ${animal}s"    # → J'ai 3 chats
    echo "J'ai 3 $animals"      # → J'ai 3  (Bash cherche la variable "animals" qui n'existe pas)
    ```
    
- Modifier variable
    
    ```powershell
    #!/bin/bash
    humeur="content"
    echo "Je suis $humeur"
    
    humeur="fatigué"
    echo "Maintenant je suis $humeur"
    ```
    
- Guillemets simples (tout littéral) vs doubles (interprète variables)
    
    ```powershell
    prenom="Alice"
    
    echo "Bonjour, $prenom"    # Guillemets doubles → Bash remplace la variable
    # → Bonjour, Alice
    
    echo 'Bonjour, $prenom'    # Guillemets simples → tout est affiché tel quel
    # → Bonjour, $prenom
    ```
    
    > **À retenir :**
    > 
    > - **Guillemets doubles `" "`** → Bash interprète les variables
    > - **Guillemets simples `' '`** → tout est littéral, aucune interprétation
- Saisie utilisateur read (demande user de taper qque chose) : -s (invisible), -t (tiemout) | read -p “texte” variable
    - Commande read demande à l’user de taper quelque chose
        
        ```powershell
        #!/bin/bash
        
        read -p "Ton prénom : " prenom
        read -p "Ton âge : " age
        echo "Tu es $prenom et tu as $age ans."
        ```
        
        - -p permet de mettre message et saisie sur même ligne.
    - Saisie invisible : -s
        
        ```powershell
        read -p "Mot de passe : " -s motdepasse  # -s : saisie invisible
        ```
        
    - Timeout de 5 secondes : -t 5
        
        ```powershell
        read -p "Choix rapide : " -t 5 choix  # -t 5 : timeout de 5 secondes
        ```
        
    - Exemples
        - Faciliter scans nmap
            
            ```bash
            #!/bin/bash
            
            read -p "L'adresse à scanner : " ip_scan    # Va prendre ip saisie puis stocker dans variable ip_scan
            echo "Scan de $ip_scan en cours..."    
            nmap -F -sV "$ip_scan"
            ```
            
- ⚠️ Résutat / Substitut d’une commande dans variable : nom_var=$(commande)
    - Substitut de commande : directement dans sortie
    
    ```bash
    echo "Bienvenue sur cette machine : $(hostname) !"
    echo "La date du jour : $(date)"
    ```
    
    - Stocker résultat commande dans variable
    
    ```powershell
    #!/bin/bash
    
    aujourdhui=$(date)
    echo "Nous sommes le : $aujourdhui"
    
    utilisateur=$(whoami)
    echo "Connecté en tant que : $utilisateur"
    
    nb_fichiers=$(ls | wc -l)
    echo "Il y a $nb_fichiers éléments dans ce dossier"
    ```
    
    - Voir les 20 derniers caractères
        
        ```bash
        last_20=$(echo "$var" | tail -c 20)
        echo "$last_20"
        ```
        
    
    ```bash
    if [[ $counter -eq 35 ]]; then
        longueur=$(echo "$var" | wc -m)  
    ```
    
    - A retenir : $(commande) exécuter la commande et renvoie son résultat. Fonctionnalités les plus puissantes de bash.
- Variables d’environnement : Variables déjà définies : env
    - Connaitre var env :
        
        ```powershell
        env
        ```
        
    - Système contient des variables déjà définies :
        
        ```powershell
        #!/bin/bash
        
        echo "Utilisateur : $USER"
        echo "Dossier perso : $HOME"
        echo "Shell actuel : $SHELL"
        echo "Dossier actuel : $PWD"
        ```
        
- Variables lecture seule : Jamais être modifiée : readonly
    - Pour qu’une variable ne puisse jamais être modifiée
        
        ```powershell
        readonly TEST="Texte qu'on ne pourra pas modifier"
        TEST="Essayer de modifier var" 
        ```
        
- “Types” en Bash : Var surtout texte même nombre manipulé comme texte, sauf quand calcul, pas types strict comme autre langages
- Cheat sheet
    
    
    | **Syntaxe** | **Effet** |
    | --- | --- |
    | nom="Alice" | Crée une variable (pas d'espace autour du =) |
    | echo "$nom" | Affiche la valeur de la variable (toujours mettre les guillemets) |
    | echo '${nom}s' | Accolades pour éviter l'ambiguïté (ex: ${animal}s → chats) |
    | "texte $var" | Guillemets doubles → la variable est interprétée |
    | 'texte $var' | Guillemets simples → tout est littéral, rien n'est interprété |
    | result=$(commande) | Substitution : stocke le résultat d'une commande dans une variable |
    | read -p "Texte : " var | Demande une saisie à l'utilisateur et la stocke dans var |
    | read -s -p "MDP : " var | Saisie invisible (pour mots de passe) |
    | read -t 5 -p "..." var | Saisie avec timeout de 5 secondes |
    | readonly MA_VAR="x" | Variable constante, ne peut pas être modifiée |
    | $USER · $HOME · $SHELL · $PWD | Variables d'environnement déjà définies par le système |
- ❌ Erreur classique
    
    ```bash
    prenom = "Alice"     # ❌ Espaces autour du = → Bash croit que "prenom" est une commande
    prenom="Alice"       # ✅ Correct
    
    echo $prenom         # ⚠️ Fonctionne, mais risqué si la valeur contient des espaces
    echo "$prenom"       # ✅ Toujours préférer cette forme
    ```
    
- Ex
    
    Crée un script `bienvenue.sh` qui :
    
    1. Affiche "Bienvenue sur cette machine !"
    2. Affiche la date du jour (avec substitution de commande)
    3. Demande le prénom de l'utilisateur
    4. Affiche "Bonjour [prénom], connecté en tant que [whoami]"
    
    ```bash
    # Code initial 
    
    #!/bin/bash
    
    machine=$(hostname)
    echo "Bienvenue sur cette machine : "$machine" !"
    
    aujourdhui=$(date)
    echo "La date du jour : "$aujourdhui""
    
    read -p "Comment vous appelez-vous ? " name
    echo "Bonjour "$name", connecté en tant que $(whoami)"
    
    # Corrigé 
    
    #!/bin/bash
    
    echo "Bienvenue sur cette machine : $(hostname) !"
    echo "La date du jour : $(date)"
    
    read -p "Comment vous appelez-vous ? " name
    echo "Bonjour $name, connecté en tant que $(whoami)"
    ```
    

### Arguments et variables spéciales [$0, $1, if -z …; then … exit 1 fi]

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
        
        ![image.png](attachment:42d9bf9b-5228-4195-aee1-09781fba5821:image.png)
        
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
    

### Redirections, erreurs et pipes [>&2, 2>/dev/null, >, >>, tee]

- 3 flux de données : 0 stdin (entrée), 1 stdout (sortie normale), 2 stderr (erreurs) : chaque commande travaille avec ces flux
    - Chaque commande travaille avec trois flux :
        
        ```bash
                          ┌──────────────┐
          Entrée ───────▶ │   Commande   │ ──▶ 1 = Sortie normale (stdout)
          (clavier)       │              │ ──▶ 2 = Erreurs (stderr)
                          └──────────────┘
        ```
        
        | Numéro | Nom | Par défaut |
        | --- | --- | --- |
        | 0 | stdin (entrée) | Le clavier |
        | **1** | **stdout (sortie normale)** | **L'écran** |
        | **2** | **stderr (erreurs)** | **L'écran** |
    - Les redirections permettent de changer la destination de ces flux.
- Rediriger la sortie vers un fichier : Créer/écraser avec >, ajouter avec >> : echo “Text” > fichier.txt
    - Créer / Ecrasser avec > :
        
        ```bash
        echo "Bonjour" > message.txt    # Crée le fichier (ou l'écrase !)
        ls /etc > liste.txt             # La liste va dans le fichier
        ```
        
    - Ajouter avec >> :
        
        ```bash
        echo "Ligne 1" > journal.txt       # Crée le fichier
        echo "Ligne 2" >> journal.txt      # Ajoute à la suite
        echo "Ligne 3" >> journal.txt      # Ajoute encore
        ```
        
- Rediriger les erreurs : Envoyer erreurs dans fichiers 2> , Masquer erreur 2>/dev/null
    
    ```bash
    # Les erreurs vont dans un fichier, la sortie normale s'affiche à l'écran
    ls /dossier_inexistant 2> erreurs.txt
    
    # Masquer les erreurs en les envoyant dans le "trou noir"
    find / -name "mon_fichier" 2>/dev/null
    ```
    
    - /dev/null est une “poubelle”, tout ce qu’on y envoie disparaît.
- Rediriger tout (sortie + erreurs) : 2>&1 (tout → fichier, erreur et sortie), /dev/null 2>&1 (tout → poubelle)
    
    ```bash
    # Tout va dans le même fichier
    ./mon_script.sh > log.txt 2>&1  # > log.txt 2>&1 = "flux 1 va dans log.txt, et flux 2 suit flux 1" → tout finit dans log.txt.
    
    # Tout dans le vide (script silencieux)
    ./mon_script.sh > /dev/null 2>&1
    ```
    
    - Quand l’on fait > log.txt, rediges seulement flux 1
    - Explication de **`2>&1` :** "envoie le flux 2 (erreurs) au même endroit que le flux 1 (sortie normale)".
        - `> log.txt 2>&1` = "flux 1 va dans log.txt, et flux 2 suit flux 1" → **tout** finit dans `log.txt`.
    
    ```bash
    ./script.sh > log.txt          # stdout → fichier, erreurs → écran
    ./script.sh 2> log.txt         # erreurs → fichier, stdout → écran
    ./script.sh > log.txt 2>&1     # tout → fichier
    ./script.sh > /dev/null 2>&1   # tout → la poubelle (silence total)
    ```
    
- Ne pas polluer sortie dans fichier : echo “Erreur : …” >&2
    
    Imagine ce script :
    
    ```
    #!/bin/bash
    
    if [[-z"$1" ]];then
    echo"Erreur : argument manquant" >&2
    exit1
    fi
    
    echo"Dossier :$1"
    ```
    
    Si tu fais :
    
    ```
    ./script.sh > resultat.txt
    ```
    
    - Cas 1 : sans `>&2`
        - Le message d’erreur irait aussi dans `resultat.txt`.
            - Donc ton fichier pourrait contenir :
            
            ```
            Erreur : argument manquant
            ```
            
            - alors que ce n’est pas un “résultat”, c’est un problème.
    - Cas 2 : avec `>&2`
        - Le message d’erreur reste affiché à l’écran, et **ne va pas** dans `resultat.txt`.
        - Donc :
            - `resultat.txt` = sortie normale
            - écran = erreur
            - C’est plus propre.
- Pipes | : envoie sortie commande comme entrée d’une autre.
    - Chaque commande reçoit la sortie de la précédente. C’est une chaîne de traîtement.
    
    ```bash
    # Compter le nombre de fichiers
    ls | wc -l
    
    # Chercher un mot dans un résultat
    ps aux | grep firefox
    
    # Trier et garder les lignes uniques
    cat prenoms.txt | sort | uniq
    ```
    
- Tee : Afficher / sauvegarder en même temps : ls -la | tee log.txt
    - Syntaxe tee
        - **Voir et garder** :
        
        ```
        commande | tee fichier.txt
        ```
        
        - **Ajouter sans écraser** :
        
        ```
        commande | tee-a fichier.txt
        ```
        
        ```bash
        tee fichier # Ecrit dans fichier en écrasant son contenu
        
        tee -a fichier # Ajoute à la fin du fichier sans effacer ce qu'il y a déjà
        ```
        
    
    ```bash
    # Affiche à l'écran ET écrit dans log.txt
    ls -la | tee log.txt
    
    # Ajouter au fichier (au lieu d'écraser)
    date | tee -a journal.log
    
    # Prend ce qu'il reçoit, l'affiche à l'écran et l'écrit dans un fichier
    hosts=$(host $domain | grep "has address" | cut -d" " -f4 | tee discovered_hosts.txt)
    
    netrange=$(whois $ip | grep "NetRange\|CIDR" | tee -a CIDR.txt)
    ```
    
- Rediriger l’entrée avec < : commande < fichier : wc -l < fichier
    
    ```bash
    # Compter les lignes d'un fichier
    wc -l < mon_fichier.txt
    
    # Trier le contenu d'un fichier
    sort < liste_noms.txt
    ```
    
- Enchaîner plusieurs pipes : ls /etc | grep “\.txt” | wc -l
    
    ```bash
    # Les 5 plus gros fichiers
    ls -lS | head -5
    
    # Compter les fichiers .txt dans /etc
    ls /etc | grep "\.txt" | wc -l
    ```
    
- Cheat sheet
    
    
    | Syntaxe | Effet |
    | --- | --- |
    | `commande > fichier` | Sortie dans fichier (écrase) |
    | `commande >> fichier` | Sortie dans fichier (ajoute) |
    | `commande 2> fichier` | Erreurs dans fichier |
    | `commande > fichier 2>&1` | Tout dans fichier |
    | `commande < fichier` | Entrée depuis un fichier |
    | `cmd1 \| cmd2` | Sortie de cmd1 → entrée de cmd2 |
    | `commande \| tee fichier` | Affiche ET sauvegarde |
    | `commande > /dev/null 2>&1` | Silence total |
- ❌ Erreur classique
    
    ```bash
    # Confondre > et >> : tu écrases un fichier important !
    echo "nouveau" > config.txt     # ❌ Tout l'ancien contenu est perdu
    echo "nouveau" >> config.txt    # ✅ Ajoute à la fin
    
    # Oublier 2> : les erreurs s'affichent en vrac et polluent la sortie
    find / -name "*.log"            # ❌ Des dizaines de "Permission denied"
    find / -name "*.log" 2>/dev/null  # ✅ Erreurs masquées
    ```
    

### Opérateurs, calculs et logique

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
    

### Conditions, comparaisons et tests [if, elif, else…]

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
    

### Boucles : répètent des actions, deux façons de penser: [while, pause, sleep]

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
    

### Fonctions et case : bloc de code réutilisable

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
    

### Chaînes de caractères

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

### Tableaux

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

### Déboguer et écrire scripts propres

- Vérifier syntaxe avant exéc bash -n script.sh
    
    Ça ne lance pas le script, ça vérifie juste la syntaxe.
    
    Pourquoi en premier :
    
    - si un `fi`, `then`, `do`, `done` manque
    - tu le vois tout de suite
    - sans te mélanger avec d’autres bugs
    
    ```bash
    bash -n script_bug.sh
    ```
    
- echo de debug : echo "[DEBUG] fichier = '$fichier'”
    - Ajouter des echos pour voir les valeurs en cours de route
    
    ```bash
    fichier=$1
    echo "[DEBUG] fichier = '$fichier'"
    
    if [[ -f "$fichier" ]]; then
        echo "[DEBUG] Le fichier existe"
        nb_lignes=$(wc -l < "$fichier")
        echo "[DEBUG] nb_lignes = '$nb_lignes'"
    fi
    ```
    
    - Astuce : Utiliser préfixe [DEBUG] pour retrouver facilement messages et supprimer une fois bug corrigé
        - Utiliser echo pour voir ce que contient une variable, suivre exéc d’un script…
- Mode trace avec : bash -x [script.sh](http://script.sh) : Affiche chaque commande avant exéc
    - -x affiche chaque commande avant de l’exéc, avec les var remplacées par leurs valeurs :
        
        ```bash
        bash -x mon_script.sh
        ```
        
    - Peut aussi l’activer/désactiver dans le script
        
        ```bash
        set -x          # Active la trace
        echo "Ceci sera tracé"
        nombre=$((5 + 3))
        set +x          # Désactive la trace
        echo "Ceci ne sera plus tracé"
        ```
        
        ```bash
        # Sortie 
        
        + echo 'Ceci sera tracé'
        Ceci sera tracé
        + nombre=8
        + set +x
        Ceci ne sera plus tracé
        ```
        
- Mode verbeux combine avec trace : bash -x -v
    - Permet de voir le code lu, puis les commandes exécutées avec valeurs réelles, plus bavard mais pratique
    
    ```bash
    bash -x -v script.sh
    
    # -x : montre l'exécution réelle
    # -v : montre le code lu
    ```
    
    ```bash
    CamiiKazZ@htb[/htb]$ bash -x -v CIDR.sh
    
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
    + '[' 0 -eq 0 ']'
    + echo -e 'You need to specify the target domain.\n'
    You need to specify the target domain.
    
    + echo -e Usage:
    Usage:
    + echo -e '\tCIDR.sh <domain>'
        CIDR.sh <domain>
    + exit 1
    ```
    
- Vérifier arguments en début de script : if -lt 1; then…
    
    ```bash
    if [[ $# -lt 1 ]]; then
        echo "Erreur : argument manquant" >&2
        echo "Utilisation : $0 <fichier>" >&2
        exit 1
    fi
    ```
    
    - **Note :** `>&2` envoie le message vers stderr (la sortie d'erreur). C'est la bonne pratique pour les messages d'erreur.
- set -e : arrêt sur erreur / set -u : erreur si variable non définie / combinaison set -euo pipefail : eu + si pipe échoue dans commande
    - set -e
        - Par défaut, Bash continue même quand commande échoue, set -e change ça
        
        ```bash
        set -e
        
        echo "Étape 1"
        cd /dossier_inexistant     # ← Erreur ! Le script s'arrête ici
        echo "Étape 2"             # ← Jamais exécuté
        ```
        
    - set - u : Va vérifier si variable a une liason
        - Mettre au début du script puis lancer avec bash -x
        
        ```bash
        set -u
        
        echo "Mon nom est $nom"    # ← Erreur ! $nom n'est pas défini
        ```
        
    - set -euo pipefail
        - e : arrêt sur erreur
        - u : erreur si variable non définie
        - o pipefail : un pipe échoue si n'importe quelle commande du pipe échoue
        
        ```bash
        set -euo pipefail
        ```
        
- Erreurs les plus fréquentes : espace autour de =, then/fi oublié, do/done oublié, guillemets oubliés…
    
    
    | Erreur | Message | Solution |
    | --- | --- | --- |
    | Espaces autour de `=` | `command not found` | `var="valeur"` (pas d'espace) |
    | `then` ou `fi` oublié | `syntax error` | Vérifie chaque `if` a son `then` et son `fi` |
    | `do` ou `done` oublié | `syntax error` | Vérifie chaque boucle a son `do` et son `done` |
    | Guillemets oubliés | `unary operator expected` | Mets `"$var"` au lieu de `$var` |
    | `-eq` confondu avec `==` | Résultat inattendu | `-eq` pour nombres, `==` pour texte |
- Checklist de tests
    
    ```bash
    bash -n script_bug.sh
    bash script_bug.sh
    bash script_bug.sh inexistant.txt
    echo "bonjour" > test.txt
    bash script_bug.sh test.txt
    bash -x script_bug.sh test.txt
    ```
    
    - d’abord voir si le script est lisible par Bash
    - ensuite tester les cas d’erreur évidents
    - ensuite tester le cas normal
    - ensuite déboguer finement
    
    Règle à retenir
    
    Quand tu débugges un script Bash, demande-toi toujours :
    
    - est-ce qu’il **se lit** correctement ? (`bash -n`)
    - est-ce qu’il **reçoit bien** ses arguments ?
    - est-ce qu’il **entre dans la bonne branche** (`if/else`) ?
    - est-ce que les **variables contiennent bien ce que j’attends** ?
    - est-ce que la **commande produit bien ce que je crois** ?
- Structurer avec des fonctions
    
    ```bash
    # ❌ Script monolithique de 200 lignes
    
    # ✅ Script structuré
    verifier_arguments() { ... }
    traiter_fichier() { ... }
    generer_rapport() { ... }
    
    verifier_arguments "$@"
    traiter_fichier "$1"
    generer_rapport
    ```
    
- Toujours mettre variables entre guillemets
    
    ```bash
    cat $fichier       # ❌ Dangereux si $fichier contient des espaces
    cat "$fichier"     # ✅ Sûr
    ```
    

### Cas pratique et automatisation

- Planifier avec cron
    - Editer crontab
        
        ```bash
        crontab -e     # Ouvrir l'éditeur
        crontab -l     # Lister les tâches
        ```
        
    - Syntaxe cron
        
        ```bash
        ┌───────── minute (0-59)
        │ ┌─────── heure (0-23)
        │ │ ┌───── jour du mois (1-31)
        │ │ │ ┌─── mois (1-12)
        │ │ │ │ ┌─ jour de la semaine (0-7, 0 et 7 = dimanche)
        │ │ │ │ │
        * * * * * commande
        ```
        
        ```bash
        # Tous les jours à minuit
        0 0 * * * /home/user/scripts/backup.sh
        
        # Toutes les 6 heures
        0 */6 * * * /home/user/scripts/check_disk.sh
        
        # Tous les lundis à 8h
        0 8 * * 1 /home/user/scripts/rapport.sh
        ```
        
        - Penser à rediriger sortie vers un log
            
            ```bash
            0 0 * * * /home/user/scripts/backup.sh >> /home/user/logs/backup.log 2>&1
            ```
            
- Penser comme un automaticien, avant d’écrire un script, se poser trois questions :
    1. Qu'est-ce que je fais à la main régulièrement ?
    2. Est-ce que c'est toujours les mêmes étapes ?
    3. Est-ce que ça pourrait tourner tout seul ?
- Journaliser et accueillir
    - Script simple permettant de journaliser les conexions :
        
        ```bash
        #!/bin/bash
        
        LOG="$HOME/connexions.log"
        
        utilisateur=$(whoami)
        date_heure=$(date '+%Y-%m-%d %H:%M:%S')
        
        echo "Bienvenue, $utilisateur !"
        echo "[$date_heure] Connexion de $utilisateur" >> "$LOG"
        echo "Connexion enregistrée dans $LOG"
        ```
        
- Tester des fichiers/dossiers
    
    ```bash
    #!/bin/bash
    
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
    
- Sauvegarder des dossiers
    
    ```bash
    #!/bin/bash
    
    # --- Configuration ---
    dossiers=("/etc" "/home")
    destination="/tmp/backups"
    date_du_jour=$(date +%Y-%m-%d)
    
    # --- Préparation ---
    mkdir -p "$destination"
    
    echo "=== Sauvegarde du $date_du_jour ==="
    
    for dossier in "${dossiers[@]}"; do
        nom_archive=$(echo "$dossier" | tr '/' '_')
        fichier="${destination}/${nom_archive}-${date_du_jour}.tar.gz"
    
        echo -n "Sauvegarde de $dossier ... "
    
        if tar -czf "$fichier" "$dossier" 2>/dev/null; then
            taille=$(du -h "$fichier" | cut -f1)
            echo "OK ($taille)"
        else
            echo "ERREUR" >&2
        fi
    done
    
    echo "=== Terminé ==="
    ```
    
- Renommer fichiers en masse
    - Renommer tous les .jpeg en .jpg
        - **Explication :** `${fichier%.jpeg}` supprime `.jpeg` à la fin de la chaîne
    
    ```bash
    #!/bin/bash
    
    dossier=${1:-.}
    compteur=0
    
    for fichier in "$dossier"/*.jpeg; do
        [[ -f "$fichier" ]] || continue
    
        nouveau="${fichier%.jpeg}.jpg"
        mv "$fichier" "$nouveau"
        echo "Renommé : $fichier → $nouveau"
        ((compteur++))
    done
    
    echo "Total : $compteur fichier(s) renommé(s)."
    ```
    
- Créer archive avec nommage par date
    
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
    
- CIDR
    1. Va checker les arguments donnés car attend un domaine
    2. Création d’une fonction qui va faire un whois et identifier le range réseau pour l’ip spécifiée
    3. Va checker si l’hôte trouvé est atteignable et avec la boucle For, va ping toutes les IP du range et compter le résultat.
    4. Identifier l’ip du domaine spécifié
    
    ```bash
    #!/bin/bash
    
    # Check for given arguments
    if [ $# -eq 0 ]
    then
        echo -e "You need to specify the target domain.\n"
        echo -e "Usage:"
        echo -e "\t$0 <domain>"
        exit 1
    else
        domain=$1
    fi
    
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
    
    # Ping discovered IP address(es)
    function ping_host {
        hosts_up=0
        hosts_total=0
        
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
        
        echo -e "\n$hosts_up out of $hosts_total hosts are up."
    }
    
    # Identify IP address of the specified domain
    hosts=$(host $domain | grep "has address" | cut -d" " -f4 | tee discovered_hosts.txt)
    
    echo -e "Discovered IP address:\n$hosts\n"
    ipaddr=$(host $domain | grep "has address" | cut -d" " -f4 | tr "\n" " ")
    
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
    
- Template
    
    ```bash
    #!/bin/bash
    # =============================================================================
    # Nom        : mon_script.sh
    # Description : [Ce que fait le script]
    # Utilisation : ./mon_script.sh [options] <arguments>
    # =============================================================================
    
    # --- Fonctions ---
    afficher_aide() {
        echo "Utilisation : $0 [options] <argument>"
        echo "  -h    Afficher cette aide"
    }
    
    log() {
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    }
    
    # --- Vérification des arguments ---
    if [[ $# -lt 1 ]]; then
        afficher_aide
        exit 1
    fi
    
    case $1 in
        -h|--help) afficher_aide ; exit 0 ;;
    esac
    
    # --- Programme principal ---
    log "Début du script"
    
    # ... ton code ici ...
    
    log "Fin du script"
    ```
    

### Workflow divers [ { echo … echo … } >]

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
