---
title: Découverte de Bash et premier script
source: IT/07 Scripting & programmation/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

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
