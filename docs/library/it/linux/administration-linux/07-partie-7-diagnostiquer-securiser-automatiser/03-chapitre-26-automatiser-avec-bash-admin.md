---
title: Chapitre 26 — Automatiser avec Bash (admin)
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 7 — Diagnostiquer, sécuriser, automatiser
  - index.md
---

## Le minimum à savoir

### Du one-liner au script

Tout au long du cours, tu as enchaîné des commandes avec des pipes (chapitre 7). Un **script** Bash, c'est simplement plusieurs de ces commandes enregistrées dans un fichier, qu'on exécute d'un coup. C'est l'aboutissement naturel de l'administration : ce qu'on fait deux fois à la main, on l'automatise. Ce chapitre fait le **pont avec le scripting Bash** ; il en montre l'application à l'administration, sans réexpliquer ce que tu as déjà appris au chapitre 8 sur l'environnement (variables, `PATH`, alias, `.bashrc`).

### Un script minimal

Un script Bash est un fichier texte qui commence par une ligne spéciale, le *shebang*, indiquant quel interpréteur l'exécute :

```bash
#!/bin/bash
# Mon premier script d'administration
echo "Rapport du $(date)"
echo "Connecté en tant que : $(whoami)"
```


On le rend exécutable (chapitre 9 !) et on le lance :

```bash
chmod +x rapport.sh          # droit d'exécution
./rapport.sh                 # exécution (le ./ : le . n'est pas dans le PATH, chapitre 8)
```


> Tu retrouves ici trois notions du cours réunies : le droit `x` (chapitre 9), la raison du `./` (chapitre 8), et la substitution `$(commande)` qui insère le résultat d'une commande dans le texte (entrevue avec `$(date +%F)` au chapitre 22).

### Réutiliser tes acquis dans des scripts

Un script d'administration n'est rien d'autre que les commandes du cours, mises bout à bout. Par exemple, un script qui résume l'état du système :

```bash
#!/bin/bash
echo "=== État du système au $(date) ==="
echo ""
echo "--- Disque ---"
df -h /                                  # chapitre 21
echo ""
echo "--- Mémoire ---"
free -h                                  # chapitre 21
echo ""
echo "--- Charge ---"
uptime                                   # chapitre 24
echo ""
echo "--- Services clés ---"
systemctl is-active ssh                  # chapitre 14
```


Rien de neuf : juste l'assemblage de ce que tu sais déjà.

## Très utile en pratique

### Variables, environnement et alias (rappel d'application)

Le chapitre 8 t'a tout donné : variables, `export`, `PATH`, alias, `.bashrc`, `source`. En administration, on les **applique** :

- Ranger ses scripts dans `~/bin` (ajouté au `PATH`) pour les lancer **par leur nom**, de partout, comme de vraies commandes.
- Créer des **alias** pour les commandes d'admin fréquentes, dans `.bashrc` :

```bash
# Dans ~/.bashrc (après un .bak, chapitre 6)
alias maj='sudo apt update && sudo apt upgrade'
alias ports='sudo ss -tulpn'
alias monlog='sudo journalctl -u ssh -f'
```


Après `source ~/.bashrc`, taper `maj` met tout à jour, `ports` liste les ports, `monlog` suit SSH en direct. Tu façonnes ton environnement de travail autour de tes tâches réelles.

### Rediriger la sortie d'un script vers un rapport

Grâce aux redirections (chapitre 7), un script peut écrire son résultat dans un fichier horodaté :

```bash
./etat-systeme.sh > rapport-$(date +%F).txt        # enregistre le rapport du jour
./etat-systeme.sh | tee rapport-$(date +%F).txt     # affiche ET enregistre (tee)
```


### Planifier un script (le pont avec le chapitre 16)

Un script + cron = automatisation complète. On dépose le script dans `~/bin` ou un chemin absolu, et on l'inscrit en crontab :

```bash
# crontab -e : rapport d'état chaque matin à 7h, enregistré daté
0 7 * * * /home/alice/bin/etat-systeme.sh > /home/alice/rapports/etat-$(date +\%F).txt
```


> **Rappels du chapitre 16, qui prennent tout leur sens ici :** en cron, utilise des **chemins absolus** (l'environnement est minimal, tes alias et ton `PATH` personnels n'y sont pas), et note que le `%` doit être échappé (`\%`) dans une crontab.

> **Pour aller plus loin en scripting :** ce chapitre fait volontairement le lien sans tout réenseigner. Conditions, boucles, fonctions, gestion d'arguments, tests robustes — tout cela relève d'un cours de **scripting Bash** dédié, qui prolonge naturellement cette formation. Ici, l'essentiel est que tu saches **assembler tes commandes d'admin en scripts réutilisables et planifiés**.

## ❌ Erreur classique

```bash
# Oublier le shebang ou le droit d'exécution
./script.sh                  # ❌ "Permission denied" si pas de chmod +x
chmod +x script.sh           # ✅ (chapitre 9)

# Chemins relatifs dans un script planifié
df -h                        # ❌ ok à la main, mais en cron le contexte diffère
/bin/df -h /home/alice       # ✅ chemins absolus pour le planifié (chapitre 16)

# Oublier d'échapper le % en crontab
... > rapport-$(date +%F).txt    # ❌ le % a un sens spécial en crontab
... > rapport-$(date +\%F).txt   # ✅ échapper avec \

# Lancer un script non testé directement en production
# ✅ tester d'abord à la main, vérifier la sortie, PUIS planifier
```


## Exercices

**Guidé :** Crée un script `etat.sh` reprenant l'exemple « état du système » ci-dessus. Rends-le exécutable avec `chmod +x`, lance-le avec `./etat.sh`, et vérifie que toutes les sections s'affichent. Puis redirige sa sortie vers un fichier daté avec `./etat.sh > etat-$(date +%F).txt` et lis le rapport produit.

**Autonome :** Ajoute à ton `.bashrc` (après un `.bak` !) trois alias d'administration qui te seraient utiles au quotidien (par exemple mise à jour, ports en écoute, espace disque). Applique avec `source ~/.bashrc` et teste-les. Ouvre un nouveau terminal pour confirmer qu'ils sont permanents.

**Défi :** Planifie ton script `etat.sh` pour qu'il s'exécute chaque jour et enregistre un rapport horodaté dans un dossier dédié. Vérifie la syntaxe de ta ligne crontab (chemins absolus, `%` échappé). Le lendemain (ou en réglant l'heure proche), confirme qu'un rapport a bien été généré automatiquement. Tu viens de créer ta première surveillance automatisée.

## ✅ Tu sais maintenant…

- Qu'un **script** Bash assemble des commandes d'admin dans un fichier exécutable
- Écrire un script minimal (shebang `#!/bin/bash`, `chmod +x`, `./script`)
- Réutiliser tout le cours dans des scripts (disque, mémoire, services, logs…)
- **Appliquer** l'environnement du chapitre 8 : `~/bin` dans le `PATH`, alias d'admin dans `.bashrc`
- Produire des **rapports horodatés** avec redirections, `tee` et `$(date +%F)`
- **Planifier** un script avec cron (chemins absolus, `%` échappé)
- Que conditions/boucles/fonctions relèvent d'un cours de **scripting Bash** dédié, prolongement naturel

---
