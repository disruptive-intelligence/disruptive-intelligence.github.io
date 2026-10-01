---
title: Redirections, erreurs et pipes [>&2, 2>/dev/null, >, >>, tee]
source: IT/07 Scripting & programmation/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

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
