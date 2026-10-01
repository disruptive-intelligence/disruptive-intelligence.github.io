---
title: Chapitre 12 — Cas pratiques et automatisation
source: IT/07 Scripting & programmation/Bash.md
note: Bash
up:
- - Bash
  - index.md
---

> Jusqu'ici, tu as appris les briques du scripting Bash une par une. Maintenant, on les **combine** dans de vrais petits scripts, proches de situations réelles. C'est ici que tout prend son sens.

### Penser comme un automaticien

Avant d'écrire un script d'automatisation, pose-toi trois questions :

1. **Qu'est-ce que je fais à la main régulièrement ?**
2. **Est-ce que c'est toujours les mêmes étapes ?**
3. **Est-ce que ça pourrait tourner tout seul ?**

Si oui aux trois → c'est un bon candidat pour un script.

### Cas pratique 1 — Journaliser et accueillir

Un script simple qui journalise les connexions :

```bash
#!/bin/bash

LOG="$HOME/connexions.log"

utilisateur=$(whoami)
date_heure=$(date '+%Y-%m-%d %H:%M:%S')

echo "Bienvenue, $utilisateur !"
echo "[$date_heure] Connexion de $utilisateur" >> "$LOG"
echo "Connexion enregistrée dans $LOG"
```


> **Ce script illustre :** variables, substitution de commande, redirection `>>`.

### Cas pratique 2 — Tester des fichiers/dossiers

Un script qui vérifie l'état d'une liste de chemins :

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


> **Ce script illustre :** arguments, boucle `for`, conditions, tests de fichiers, pipes.

### Cas pratique 3 — Sauvegarder des dossiers

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


> **Ce script illustre :** tableaux, boucle `for`, conditions, redirections, substitution de commande.

### Cas pratique 4 — Renommer des fichiers en masse

Renommer tous les `.jpeg` en `.jpg` :

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


> **Explication :** `${fichier%.jpeg}` supprime `.jpeg` à la fin de la chaîne (vu au chapitre 9).

### Planifier avec `cron`

`cron` exécute des scripts **automatiquement** à des heures précises.

#### Éditer la crontab

```bash
crontab -e     # Ouvrir l'éditeur
crontab -l     # Lister les tâches
```


#### La syntaxe cron

```
┌───────── minute (0-59)
│ ┌─────── heure (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌─── mois (1-12)
│ │ │ │ ┌─ jour de la semaine (0-7, 0 et 7 = dimanche)
│ │ │ │ │
* * * * * commande
```


#### Exemples

```bash
# Tous les jours à minuit
0 0 * * * /home/user/scripts/backup.sh

# Toutes les 6 heures
0 */6 * * * /home/user/scripts/check_disk.sh

# Tous les lundis à 8h
0 8 * * 1 /home/user/scripts/rapport.sh
```


> **Astuce :** redirige la sortie vers un log :
> ```bash
> 0 0 * * * /home/user/scripts/backup.sh >> /home/user/logs/backup.log 2>&1
> ```

### Script modèle

Voici un squelette "propre" que tu peux réutiliser comme base :

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


### Exercices

**Guidé :** Crée un script de sauvegarde qui compresse un dossier donné en argument, le nomme avec la date, et le place dans `/tmp/backups/`.

**Autonome :** Crée un script "boîte à outils" avec un menu (`case` + boucle) : 1) Lister les fichiers, 2) Espace disque (`df -h`), 3) Info système (`uname -a`), 4) Quitter.

**Défi :** Planifie un de tes scripts pour qu'il s'exécute tous les jours à 8h avec `crontab -e`.

### ✅ Tu sais maintenant...

- Écrire des scripts d'automatisation complets
- Combiner toutes les notions apprises dans des cas concrets
- Planifier des scripts avec cron
- Structurer un script proprement avec un modèle réutilisable

---


## Conclusion

Tu as toutes les bases pour écrire des scripts Bash utiles et bien structurés :

- **Chapitres 1-3 :** Les fondamentaux — script, variables, arguments
- **Chapitre 4 :** Les flux — redirections et pipes
- **Chapitres 5-6 :** La logique — calculs, conditions, tests
- **Chapitre 7 :** La répétition — boucles
- **Chapitre 8 :** La structure — fonctions et case
- **Chapitres 9-10 :** Les données — chaînes et tableaux
- **Chapitre 11 :** La qualité — débogage et bonnes pratiques
- **Chapitre 12 :** La mise en pratique — automatisation et cron

**Pour continuer à progresser :**

- Écris des scripts pour tes propres besoins quotidiens
- Quand tu es bloqué, `man commande` est ton meilleur ami
- Lis les scripts des autres pour découvrir de nouvelles techniques
- La meilleure façon d'apprendre, c'est de pratiquer sur des problèmes réels

Bon scripting !
