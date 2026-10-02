---
title: Déboguer et écrire scripts propres
source: IT/07 Scripting & programmation/Shell/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

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
