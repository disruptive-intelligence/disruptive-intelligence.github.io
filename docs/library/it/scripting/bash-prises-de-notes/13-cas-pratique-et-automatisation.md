---
title: Cas pratique et automatisation
source: IT/07 Scripting & programmation/Shell/Bash — prises de notes.md
note: Bash — prises de notes
up:
- - Bash — prises de notes
  - index.md
---

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
