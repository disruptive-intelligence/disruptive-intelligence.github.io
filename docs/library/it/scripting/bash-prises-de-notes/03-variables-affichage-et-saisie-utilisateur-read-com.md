---
title: Variables, affichage et saisie utilisateur [read, $(commande), var env, readonly]
source: IT/07 Scripting & programmation/Shell/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

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
