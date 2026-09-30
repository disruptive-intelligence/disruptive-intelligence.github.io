---
title: PARTIE 7 — Diagnostiquer, sécuriser, automatiser
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
chapter: 7
chapters: 7
---

Voici la synthèse appliquée du cours. On ne découvre plus beaucoup de commandes nouvelles : on **mobilise tout ce qu'on a appris** pour résoudre des problèmes réels, sécuriser une machine et automatiser le travail. C'est ici que les six parties précédentes prennent tout leur sens et se rejoignent.

---


## Chapitre 24 — Diagnostic système (méthode)

### Le minimum à savoir

#### Une méthode, pas une liste de commandes

Face à un problème (« le serveur est lent », « un service ne démarre pas », « le disque est plein »), le débutant tape des commandes au hasard. L'administrateur suit une **méthode** : du symptôme vers la cause, en éliminant les pistes une à une. Ce chapitre ne t'apprend presque aucune commande nouvelle — tu les connais toutes. Il t'apprend à les **enchaîner intelligemment**.

La démarche générale :

1. **Observer le symptôme précisément.** « Lent » ne veut rien dire ; lent à quoi ? depuis quand ? pour qui ?
2. **Formuler des hypothèses.** CPU saturé ? Mémoire pleine ? Disque plein ? Réseau coupé ? Service planté ?
3. **Vérifier chaque hypothèse** avec l'outil adapté, en commençant par le plus probable.
4. **Lire les logs**, qui racontent souvent directement ce qui s'est passé.
5. **Corriger**, puis **vérifier** que le problème a disparu.

#### La trousse de diagnostic (tout ce que tu connais déjà)

| Question | Commande | Vu au chapitre |
|----------|----------|----------------|
| Depuis quand la machine tourne ? charge ? | `uptime` | (ici) |
| Quels processus consomment ? | `top`, `htop` | 13 |
| La mémoire est-elle saturée ? | `free -h` | 21 |
| Le disque est-il plein ? | `df -h` puis `du` | 21 |
| Un service est-il tombé ? | `systemctl status` | 14 |
| Que disent les journaux ? | `journalctl`, `/var/log` | 15 |
| Un souci matériel/noyau ? | `dmesg -T` | 15 |
| Le réseau répond-il ? | `ping`, `ip a`, `ss` | 17 |

`uptime` est le seul vrai nouveau venu, et il est simple :

```bash
uptime           # depuis quand la machine tourne + la "charge" (load average)
```

La **charge** (*load average*) donne trois chiffres (moyenne sur 1, 5 et 15 minutes). En première approche, comparée au nombre de cœurs du processeur : une charge durablement supérieure au nombre de cœurs indique un système surchargé.

### Très utile en pratique

#### Scénario 1 : « la machine est lente »

```bash
uptime           # la charge est-elle anormalement haute ?
top              # quel processus dévore le CPU ? (trie par %CPU)
free -h          # la mémoire est-elle pleine ? (le système "swappe"-t-il ?)
df -h            # le disque est-il plein ? (un disque plein ralentit tout)
```

On part du plus global (`uptime`, `top`) vers le plus précis. Le coupable est presque toujours l'un de ces quatre : un processus emballé, la mémoire saturée, le disque plein, ou un disque défaillant (`dmesg -T`).

#### Scénario 2 : « un service ne démarre pas »

```bash
sudo systemctl status nginx      # quel est l'état ? que dit le résumé ?
journalctl -u nginx -e           # le journal complet du service (fin)
journalctl -u nginx --since "10 min ago"   # juste avant l'échec
```

Le couple `status` + `journalctl -u` (chapitres 14-15) résout l'immense majorité des cas : le service écrit **pourquoi** il a échoué (port déjà utilisé, fichier de config invalide, permission manquante…). On lit, on comprend, on corrige.

#### Scénario 3 : « pas d'accès réseau »

```bash
ip a                     # ai-je une adresse IP ?
ip r                     # ai-je une passerelle (route par défaut) ?
ping 8.8.8.8             # le réseau répond-il par IP ?
ping exemple.com         # le DNS résout-il les noms ?
```

On remonte la chaîne : interface → adresse → passerelle → connectivité IP → DNS. Le premier maillon qui casse désigne la cause (souvenir du chapitre 17 : IP OK mais nom KO = problème DNS).

> **Le réflexe maître :** quel que soit le problème, **les logs parlent**. Avant de spéculer longuement, lis `journalctl -e` et le `status` du service concerné. La réponse y est souvent écrite noir sur blanc.

### ❌ Erreur classique

```bash
# Taper des commandes au hasard sans hypothèse
# ❌ on s'agite sans avancer
# ✅ formuler une hypothèse, la tester, passer à la suivante

# Ignorer les logs et deviner
# ❌ spéculer sur la cause
journalctl -u service -e         # ✅ le service dit souvent POURQUOI il a échoué

# Confondre charge élevée et CPU élevé
uptime                           # charge haute peut aussi venir d'attente disque/IO
top                              # ✅ regarder CPU, mémoire ET état des processus

# Redémarrer sans comprendre
sudo reboot                      # ❌ "ça remarche" sans savoir pourquoi = ça reviendra
# ✅ comprendre la cause AVANT de redémarrer
```

### Exercices

**Guidé :** Fais un bilan de santé complet de ta machine en enchaînant : `uptime`, `free -h`, `df -h`, et `top` (quelques secondes, puis `q`). Pour chacun, note une conclusion : la charge est-elle normale ? reste-t-il de la mémoire ? de l'espace disque ? un processus consomme-t-il anormalement ?

**Autonome :** Choisis un service actif sur ta machine (vu au chapitre 14). Affiche son `systemctl status`, puis son journal récent avec `journalctl -u <service> --since "today"`. Entraîne-toi à lire ces sorties comme un diagnostic : le service est-il sain ? Y a-t-il des avertissements ou erreurs ?

**Défi :** Rédige ta propre **checklist de diagnostic** « machine lente », sous forme d'une liste ordonnée de commandes à lancer, avec pour chacune la question à laquelle elle répond et ce qui constituerait un résultat anormal. Tu construis là un véritable outil de travail réutilisable — exactement ce qu'un administrateur garde sous la main.

### ✅ Tu sais maintenant…

- Suivre une **méthode** : symptôme → hypothèses → vérification → logs → correction → vérification
- Mobiliser ta **trousse de diagnostic** (`uptime`, `top`, `free`, `df`/`du`, `systemctl`, `journalctl`, `dmesg`, `ping`/`ip`/`ss`)
- Lire la **charge** avec `uptime` et la relativiser au nombre de cœurs
- Dérouler les scénarios types : machine lente, service en panne, réseau coupé
- Que **les logs contiennent souvent la réponse** : les lire avant de spéculer
- Comprendre la cause **avant** de redémarrer

---


## Chapitre 25 — Sécurité de base (durcissement)

### Le minimum à savoir

#### Durcir, c'est réduire la surface d'attaque

**Durcir** (*hardening*) une machine, c'est diminuer le nombre de façons dont elle peut être attaquée. Le principe directeur, déjà rencontré au chapitre 11, est le **moindre privilège** appliqué à tout : moins de services qui tournent, moins de ports ouverts, moins de comptes, moins de droits, moins de logiciels. **Tout ce qui n'est pas nécessaire est une porte potentielle qu'on ferme.** Ce chapitre rassemble, sous l'angle défensif, beaucoup de réflexes vus tout au long du cours.

#### Les fondamentaux, dans l'ordre d'importance

1. **Maintenir à jour** (chapitre 20). La mesure la plus rentable, et de loin : beaucoup d'attaques exploitent des failles déjà connues et corrigées.

   ```bash
   sudo apt update && sudo apt upgrade
   ```

2. **Réduire les services et ports** (chapitres 14, 17). Désactiver ce qui ne sert pas.

   ```bash
   sudo ss -tulpn                       # qu'est-ce qui écoute ?
   sudo systemctl disable --now service-inutile   # arrêter et désactiver
   ```

3. **Durcir SSH** (chapitre 18). Pas de connexion root, clés plutôt que mots de passe.

4. **Gérer les comptes et privilèges** (chapitres 10, 11, 12). Comptes au minimum, sudo précis, audit des SUID/capabilities.

5. **Mettre un pare-feu** (ci-dessous).

### Très utile en pratique

#### Le pare-feu simple : `ufw`

Un **pare-feu** contrôle quelles connexions réseau sont autorisées. Sous Debian/Ubuntu, `ufw` (*Uncomplicated Firewall*) le rend accessible. La logique de durcissement : **tout bloquer par défaut, puis n'ouvrir que le nécessaire.**

```bash
sudo ufw default deny incoming       # bloquer toutes les connexions entrantes par défaut
sudo ufw default allow outgoing      # autoriser les connexions sortantes
sudo ufw allow 22/tcp                # autoriser SSH (sinon on se coupe l'accès !)
sudo ufw enable                      # activer le pare-feu
sudo ufw status verbose              # vérifier les règles actives
```

> **⚠️ Prudence (lien chapitre 18) :** avant d'activer le pare-feu sur une machine distante, **autorise SSH d'abord** (`ufw allow 22/tcp`). Sinon, `ufw enable` te couperait immédiatement ta propre connexion. Le même réflexe « ne te verrouille pas dehors » que pour SSH.

#### Se protéger de la force brute : `fail2ban` (notion)

`fail2ban` surveille les logs (chapitre 15) et **bannit automatiquement** les adresses IP qui multiplient les échecs de connexion (typiquement, les attaques par force brute SSH du chapitre 4). C'est la réponse automatisée à la menace qu'on a appris à **détecter** manuellement.

```bash
sudo systemctl status fail2ban       # vérifier qu'il tourne
sudo fail2ban-client status sshd     # voir les IP bannies pour SSH
```

Pour débuter, retiens son principe : il transforme la détection (compter les échecs dans les logs) en **protection active** (bloquer l'attaquant). Sa configuration fine dépasse ce cours.

> **`fail2ban` n'est pas magique :** l'installer ne suffit pas toujours. Il faut **vérifier que la jail SSH est activée**, que les logs qu'il surveille correspondent bien à ta distribution (`auth.log` / `secure` / `journalctl`, chapitre 15), et **tester** que les bannissements fonctionnent réellement (`sudo fail2ban-client status sshd`). On l'utilise donc comme un mécanisme **à configurer et à tester**, pas comme une protection automatique garantie.

#### La checklist de durcissement

Voici une checklist de base pour un serveur fraîchement installé, qui réunit le cours :

```
□ Système à jour (apt update && apt upgrade)
□ Comptes : pas de compte inutile, mots de passe robustes (audit /etc/passwd)
□ sudo : règles précises, pas de connexion root directe
□ SSH : PermitRootLogin no, authentification par clé, PasswordAuthentication no
□ Services : seuls les nécessaires tournent (ss -tulpn, systemctl disable les autres)
□ Pare-feu : ufw activé, deny par défaut, seuls les ports utiles ouverts
□ fail2ban : installé et actif pour SSH
□ SUID/capabilities : liste de référence établie (find -perm -4000, getcap -r /)
□ Logs : journalisation active et surveillée (journalctl)
□ Sauvegardes : en place, testées, hors site (chapitre 23)
```

> **Orientation cyber / SOC / eJPT :** cette checklist est le **versant défensif** de l'énumération qu'un attaquant réalise. Là où l'attaquant cherche un service mal configuré, un SUID exploitable, un sudo trop permissif ou un système non patché, le défenseur ferme ces mêmes portes en amont. Tu connais maintenant les deux faces : tu sais où regarder, donc tu sais quoi protéger.

### ❌ Erreur classique

```bash
# Activer ufw sans autoriser SSH (sur une machine distante)
sudo ufw enable                  # ❌ connexion SSH coupée immédiatement
sudo ufw allow 22/tcp            # ✅ AVANT d'activer, sur une machine distante
sudo ufw enable

# Ouvrir tout "pour que ça marche"
sudo ufw allow from any to any   # ❌ revient à ne pas avoir de pare-feu
sudo ufw allow 22/tcp            # ✅ ouvrir port par port, le strict nécessaire

# Croire qu'un pare-feu seul suffit
# ❌ le pare-feu est UNE couche ; mises à jour, SSH durci, comptes comptent autant

# Laisser des services par défaut tourner sans réfléchir
sudo ss -tulpn                   # ✅ inventorier, puis désactiver l'inutile
```

### Exercices

**Guidé :** Fais un mini-audit de durcissement de ta machine, **sans rien modifier**. Vérifie : le système est-il à jour (`apt list --upgradable`) ? Quels ports écoutent (`sudo ss -tulpn`) ? Le pare-feu est-il actif (`sudo ufw status`) ? Y a-t-il une connexion root SSH autorisée (`grep PermitRootLogin /etc/ssh/sshd_config`) ? Note ce qui pourrait être amélioré.

**Autonome (en lab) :** Sur une machine de test (pas un accès distant unique !), configure `ufw` proprement : politique deny par défaut en entrée, autorise SSH, active-le, et vérifie avec `ufw status verbose`. Confirme que tu as toujours accès. Désactive-le ensuite si c'était juste un exercice (`sudo ufw disable`).

**Défi (orientation sécurité) :** Reprends la checklist de durcissement ci-dessus et applique-la, point par point, à ta machine d'apprentissage. Pour chaque ligne, note l'état actuel (conforme / à corriger) et la commande qui vérifie ou corrige. Tu produis ainsi un **rapport de durcissement** — exactement le livrable d'un travail de sécurisation réel.

### ✅ Tu sais maintenant…

- Que **durcir** = réduire la surface d'attaque (moindre privilège appliqué à tout)
- L'ordre des priorités : **mises à jour** d'abord, puis services/ports, SSH, comptes, pare-feu
- Configurer un pare-feu avec `ufw` (deny par défaut, ouvrir le strict nécessaire, autoriser SSH avant `enable`)
- Que `fail2ban` transforme la **détection** de force brute en **protection** automatique
- Dérouler une **checklist de durcissement** complète, qui réunit tout le cours
- Que le durcissement défensif est le miroir de l'énumération offensive

---


## Chapitre 26 — Automatiser avec Bash (admin)

### Le minimum à savoir

#### Du one-liner au script

Tout au long du cours, tu as enchaîné des commandes avec des pipes (chapitre 7). Un **script** Bash, c'est simplement plusieurs de ces commandes enregistrées dans un fichier, qu'on exécute d'un coup. C'est l'aboutissement naturel de l'administration : ce qu'on fait deux fois à la main, on l'automatise. Ce chapitre fait le **pont avec le scripting Bash** ; il en montre l'application à l'administration, sans réexpliquer ce que tu as déjà appris au chapitre 8 sur l'environnement (variables, `PATH`, alias, `.bashrc`).

#### Un script minimal

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

#### Réutiliser tes acquis dans des scripts

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

### Très utile en pratique

#### Variables, environnement et alias (rappel d'application)

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

#### Rediriger la sortie d'un script vers un rapport

Grâce aux redirections (chapitre 7), un script peut écrire son résultat dans un fichier horodaté :

```bash
./etat-systeme.sh > rapport-$(date +%F).txt        # enregistre le rapport du jour
./etat-systeme.sh | tee rapport-$(date +%F).txt     # affiche ET enregistre (tee)
```

#### Planifier un script (le pont avec le chapitre 16)

Un script + cron = automatisation complète. On dépose le script dans `~/bin` ou un chemin absolu, et on l'inscrit en crontab :

```bash
# crontab -e : rapport d'état chaque matin à 7h, enregistré daté
0 7 * * * /home/alice/bin/etat-systeme.sh > /home/alice/rapports/etat-$(date +\%F).txt
```

> **Rappels du chapitre 16, qui prennent tout leur sens ici :** en cron, utilise des **chemins absolus** (l'environnement est minimal, tes alias et ton `PATH` personnels n'y sont pas), et note que le `%` doit être échappé (`\%`) dans une crontab.

> **Pour aller plus loin en scripting :** ce chapitre fait volontairement le lien sans tout réenseigner. Conditions, boucles, fonctions, gestion d'arguments, tests robustes — tout cela relève d'un cours de **scripting Bash** dédié, qui prolonge naturellement cette formation. Ici, l'essentiel est que tu saches **assembler tes commandes d'admin en scripts réutilisables et planifiés**.

### ❌ Erreur classique

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

### Exercices

**Guidé :** Crée un script `etat.sh` reprenant l'exemple « état du système » ci-dessus. Rends-le exécutable avec `chmod +x`, lance-le avec `./etat.sh`, et vérifie que toutes les sections s'affichent. Puis redirige sa sortie vers un fichier daté avec `./etat.sh > etat-$(date +%F).txt` et lis le rapport produit.

**Autonome :** Ajoute à ton `.bashrc` (après un `.bak` !) trois alias d'administration qui te seraient utiles au quotidien (par exemple mise à jour, ports en écoute, espace disque). Applique avec `source ~/.bashrc` et teste-les. Ouvre un nouveau terminal pour confirmer qu'ils sont permanents.

**Défi :** Planifie ton script `etat.sh` pour qu'il s'exécute chaque jour et enregistre un rapport horodaté dans un dossier dédié. Vérifie la syntaxe de ta ligne crontab (chemins absolus, `%` échappé). Le lendemain (ou en réglant l'heure proche), confirme qu'un rapport a bien été généré automatiquement. Tu viens de créer ta première surveillance automatisée.

### ✅ Tu sais maintenant…

- Qu'un **script** Bash assemble des commandes d'admin dans un fichier exécutable
- Écrire un script minimal (shebang `#!/bin/bash`, `chmod +x`, `./script`)
- Réutiliser tout le cours dans des scripts (disque, mémoire, services, logs…)
- **Appliquer** l'environnement du chapitre 8 : `~/bin` dans le `PATH`, alias d'admin dans `.bashrc`
- Produire des **rapports horodatés** avec redirections, `tee` et `$(date +%F)`
- **Planifier** un script avec cron (chemins absolus, `%` échappé)
- Que conditions/boucles/fonctions relèvent d'un cours de **scripting Bash** dédié, prolongement naturel

---


## Chapitre 27 — Mini-projets pratiques

Voici trois projets fil rouge qui mobilisent **l'ensemble du cours**. Ils sont conçus pour être réalisés sur ta machine d'apprentissage ou une VM dédiée. Prends ton temps : la valeur est dans la réalisation, pas dans la lecture.

---

### Projet 1 — Mettre en service un serveur (orientation admin)

**Objectif :** partir d'une machine fraîchement installée et la rendre opérationnelle, propre et sécurisée. C'est la synthèse de l'administration classique.

> **⚠️ À faire en lab :** réalise ce projet dans une **VM locale ou un serveur de lab**. N'expose **pas** un service sur Internet tant que tu n'as pas solidement compris le pare-feu, les mises à jour, les logs et les sauvegardes. Un serveur mal préparé exposé au Web est attaqué en quelques minutes.

**Étapes proposées :**

1. **Première prise en main** (parties 1-2) : connecte-toi, repère-toi (`pwd`, `ls`, arborescence), mets à jour le système (`sudo apt update && sudo apt upgrade`).
2. **Comptes** (partie 3) : crée un utilisateur d'administration dédié (`adduser`), ajoute-le au groupe `sudo` (`usermod -aG sudo`), vérifie ses droits (`id`, `sudo -l`).
3. **Accès distant sécurisé** (partie 5) : mets en place l'authentification SSH par clé (`ssh-keygen`, `ssh-copy-id`), puis durcis `sshd_config` (`PermitRootLogin no`, clés uniquement) avec le réflexe `.bak`/`sudoedit`/`diff`. **Garde une session de secours.**
4. **Pare-feu** (partie 7) : configure `ufw` (deny par défaut, autorise SSH **avant** d'activer).
5. **Un service** (partie 4) : installe un service simple (par exemple un serveur web), vérifie son `systemctl status`, active-le au démarrage (`enable --now`), confirme qu'il écoute (`ss -tulpn`).
6. **Sauvegardes** (partie 6) : écris un petit script de sauvegarde (`rsync` ou `tar` horodaté), teste-le, puis planifie-le en cron.
7. **Vérification finale** : déroule la checklist de durcissement du chapitre 25.

**Livrable :** une machine opérationnelle + un court document décrivant ce que tu as configuré et pourquoi.

---

### Projet 2 — Script de surveillance défensive (orientation SOC)

**Objectif :** créer un tableau de bord texte qui donne, en un coup d'œil, l'état de santé et de sécurité de la machine. C'est l'outil quotidien d'un analyste.

**Ce que le script doit produire** (un rapport horodaté) :

1. **Santé système** (parties 4, 6) : charge (`uptime`), mémoire (`free -h`), espace disque (`df -h`).
2. **Services clés** (partie 4) : état des services importants (SSH, pare-feu…) via `systemctl is-active`.
3. **Réseau** (partie 5) : ports actuellement en écoute (`ss -tulpn`).
4. **Sécurité — connexions** (parties 1, 3, 4) : dernières connexions réussies, et surtout les **tentatives d'authentification échouées** récentes, en isolant les IP sources les plus fréquentes (le pipeline `grep`/`awk`/`sort`/`uniq -c` du chapitre 4, appliqué à `auth.log`/`secure` ou via `journalctl`).
5. **Mise en forme** : un rapport clair, horodaté (`$(date)`), enregistré dans un fichier daté et/ou affiché avec `tee`.

**Étapes :**

- Construis le script section par section (chapitre 26), en testant chaque bloc à la main d'abord.
- Rends-le exécutable, range-le dans `~/bin`.
- Planifie-le (cron) pour un rapport quotidien automatique.

**Livrable :** un script `surveillance.sh` fonctionnel + un exemple de rapport généré. C'est une véritable première brique de supervision défensive.

---

### Projet 3 — Investigation d'incident (orientation cyber / eJPT)

**Objectif :** à partir d'un jeu de logs (réels de ta machine, ou un jeu de logs d'entraînement que tu te constitues), **reconstituer le déroulé d'une activité suspecte**. C'est l'exercice central de l'analyse défensive.

**Trame d'investigation :**

1. **Collecte** (parties 1, 6) : rassemble les logs pertinents sans les altérer (`rsync`/`tar` qui préservent les dates, chapitre 19/22). Travaille sur des **copies**.
2. **Connexions** (parties 1, 4) : dans le journal d'authentification, distingue les connexions réussies des échecs. Y a-t-il une rafale d'échecs (signe de force brute) ? Suivie d'une réussite (compromission possible) ? Depuis quelles IP ? (pipeline du chapitre 4 / `journalctl` du chapitre 15.)
3. **Privilèges** (partie 3) : recherche les usages de `sudo` dans les logs. Une élévation de privilèges inattendue ? Par quel compte ?
4. **Persistance** (partie 4) : inspecte les tâches planifiées (`crontab -l`, `/etc/cron.*`) et les services (`systemctl list-units`). Quelque chose d'anormal aurait-il été ajouté ?
5. **Traces sur le système** (parties 2, 3) : cherche des fichiers récents ou suspects (`find` par date), des binaires SUID ou capabilities inattendus (`find -perm -4000`, `getcap -r /`, chapitre 12), des fichiers dans des emplacements inhabituels (`/tmp`).
6. **Synthèse** : rédige une **chronologie** de ce que tu as reconstitué — quoi, quand, depuis où, par quel compte — comme un mini-rapport d'incident.

**Livrable :** un rapport d'investigation : la chronologie reconstituée, les indices retenus, et les recommandations (que faudrait-il durcir pour empêcher la récidive ? → chapitre 25).

> **Note éthique :** cet exercice est **défensif**. On apprend à **comprendre et reconstituer** une activité pour mieux protéger, jamais à attaquer un système qui ne nous appartient pas. Entraîne-toi uniquement sur tes propres machines ou des environnements prévus pour l'apprentissage.

---

> **🏁 CHECKPOINT FINAL — Fin du cours**
>
> Tu es allé du tout début — ouvrir un terminal sans savoir quoi en faire — jusqu'à savoir **administrer, diagnostiquer, sécuriser et automatiser** un système Linux, avec les réflexes défensifs d'un analyste. C'est un parcours considérable.
>
> **Tu sais maintenant :**
> - survivre et te repérer dans le terminal (parties 1-2) ;
> - comprendre le modèle de sécurité de Linux : permissions, utilisateurs, privilèges (partie 3) ;
> - piloter une machine vivante : processus, services, logs, planification (partie 4) ;
> - administrer une machine à distance et en réseau (partie 5) ;
> - entretenir un système : paquets, disque, archives, sauvegardes (partie 6) ;
> - diagnostiquer, durcir et automatiser (partie 7).
>
> La suite t'appartient : pratique sur tes propres machines, approfondis le **scripting Bash**, et explore les pistes **SOC / pentest / eJPT** qui prolongent naturellement ces fondations.

---

---
---


## SYNTHÈSE FINALE

Cette section te sert de **référence rapide** une fois le cours terminé. Garde-la sous la main : ce sont les commandes et réflexes que tu utiliseras au quotidien.

### Cheat-sheets thématiques

#### Navigation et repérage

| Besoin | Commande |
|--------|----------|
| Où suis-je ? | `pwd` |
| Lister (détaillé, cachés, lisible) | `ls -lah` |
| Se déplacer / revenir | `cd chemin` / `cd -` / `cd ~` |
| Voir l'arbre | `tree -L 2` |
| Remonter d'un niveau | `cd ..` |

#### Fichiers et lecture

| Besoin | Commande |
|--------|----------|
| Type d'un fichier | `file fichier` |
| Lire (petit / gros) | `cat fichier` / `less fichier` |
| Début / fin | `head fichier` / `tail fichier` |
| Suivre en direct | `tail -f fichier` (sortie : `Ctrl+C`) |
| Compter les lignes | `wc -l fichier` |
| Créer / copier / déplacer | `touch` / `cp -r` / `mv` |
| Supprimer (prudence !) | `rm -i` / `rm -r` |
| Créer une arborescence | `mkdir -p a/b/c` |

#### Recherche et texte

| Besoin | Commande |
|--------|----------|
| Chercher du texte | `grep -i "motif" fichier` |
| Compter / inverser / numéroter | `grep -c` / `grep -v` / `grep -n` |
| Trouver un fichier | `find /chemin -name "*.ext"` |
| Extraire une colonne | `cut -d: -f1` / `awk '{print $1}'` |
| Remplacer du texte | `sed 's/ancien/nouveau/g'` |
| Trier / dédoublonner + compter | `sort` / `sort \| uniq -c` |
| Casse | `tr 'A-Z' 'a-z'` |

#### Flux et environnement

| Besoin | Commande |
|--------|----------|
| Enregistrer / ajouter | `cmd > fichier` / `cmd >> fichier` |
| Jeter les erreurs | `cmd 2>/dev/null` |
| Enchaîner | `cmd1 \| cmd2` |
| Voir ET enregistrer | `cmd \| tee fichier` |
| Voir une variable | `echo $PATH` |
| Toutes les variables | `env` |
| Localiser un programme | `which cmd` / `command -v cmd` |
| Variable / alias permanents | éditer `~/.bashrc` puis `source ~/.bashrc` |

#### Permissions et identité

| Besoin | Commande |
|--------|----------|
| Voir les droits | `ls -l` |
| Modifier (symbolique / octal) | `chmod u+x` / `chmod 755` |
| Rendre un script exécutable | `chmod +x script.sh` |
| Changer propriétaire / groupe | `chown user:grp` / `chgrp grp` |
| Mon identité | `id` / `whoami` / `groups` |
| Créer un user / l'ajouter à un groupe | `adduser bob` / `usermod -aG sudo bob` |
| Admin ponctuel | `sudo cmd` |
| Mes droits sudo | `sudo -l` |
| Lister les SUID / capabilities | `find / -type f -perm -4000 2>/dev/null` / `getcap -r / 2>/dev/null` |

#### Processus et services

| Besoin | Commande |
|--------|----------|
| Lister les processus | `ps aux` / `ps aux \| grep nom` |
| Temps réel | `top` / `htop` (sortie : `q`) |
| Arrêter (poli / forcé) | `kill PID` / `kill -9 PID` |
| Par nom | `killall nom` |
| État d'un service | `systemctl status nom` |
| Démarrer / arrêter / redémarrer | `sudo systemctl start\|stop\|restart nom` |
| Auto au démarrage | `sudo systemctl enable --now nom` |
| Lister les services | `systemctl list-units --type=service` |

#### Logs et diagnostic

| Besoin | Commande |
|--------|----------|
| Journal d'un service | `journalctl -u nom` |
| Suivre en direct | `journalctl -f` |
| Depuis quand / filtré | `journalctl --since "today"` |
| Messages noyau/matériel | `sudo dmesg -T \| tail` |
| Charge / uptime | `uptime` |
| Mémoire | `free -h` |
| Logs d'auth (selon distro) | `/var/log/auth.log` · `/var/log/secure` · `journalctl` |

#### Réseau et SSH

| Besoin | Commande |
|--------|----------|
| Mes adresses / routes | `ip a` / `ip r` |
| Tester la connectivité | `ping -c 4 cible` |
| Ports en écoute | `sudo ss -tulpn` |
| Résolution DNS | `dig nom` / `nslookup nom` |
| Tester un site | `curl -I url` |
| Connexion distante | `ssh user@machine` |
| Générer / copier une clé | `ssh-keygen -t ed25519` / `ssh-copy-id user@machine` |
| Copier / synchroniser | `scp` / `rsync -av --dry-run` |

#### Paquets, disque, archives

| Besoin | Commande |
|--------|----------|
| Mettre à jour | `sudo apt update && sudo apt upgrade` |
| Installer / supprimer | `sudo apt install nom` / `sudo apt purge nom` |
| Chercher un paquet | `apt search motclé` |
| Espace disque global | `df -h` |
| Taille d'un dossier | `du -sh dossier` |
| Plus gros dossiers | `du -h --max-depth=1 / \| sort -rh \| head` |
| Disques / montages (observer) | `lsblk` / `findmnt` |
| Archiver / extraire | `tar -czvf a.tar.gz dossier/` / `tar -xzvf a.tar.gz` |
| Lire un log compressé | `zcat fichier.gz` / `zgrep "motif" fichier.gz` |

### Récapitulatif des erreurs classiques

| Domaine | Le piège | Le bon réflexe |
|---------|----------|----------------|
| Suppression | `rm` est définitif, pas de corbeille | `pwd` → `ls` → `rm -i` ; relire `rm -rf` |
| Espace parasite | `rm -rf / chemin` détruit la racine | relire la ligne avant Entrée |
| Permissions | `chmod 777` = faille ouverte | donner le minimum (`644`, `755`, `600`) |
| Dossiers | `r` ne suffit pas pour entrer | il faut le `x` pour traverser |
| Groupes | `usermod -G` écrase les groupes | toujours `usermod -aG` |
| sudo | shell root permanent (`sudo -i`) | `sudo cmd` ponctuel |
| Services | `start` ≠ persistant | `enable --now` pour le démarrage auto |
| Redirection | `>` écrase sans prévenir | `>>` pour ajouter ; vérifier la cible |
| Recherche | confondre `find` (fichiers) et `grep` (texte) | `find` = noms, `grep` = contenu |
| Réseau | `netstat`/`ifconfig` absents | `ss` / `ip` (modernes) |
| Paquets | `upgrade` sans `update` | `update && upgrade` |
| Disque | confondre `df` (disque) et `du` (dossier) | `df` constate, `du` trouve le coupable |
| Montage | `mount`/`umount`/`fstab` sensibles | observer d'abord (`lsblk`, `findmnt`) |
| Archives | `f` mal placé dans `tar` | `f` toujours juste avant le nom |
| SSH | se verrouiller dehors | garder une session de secours, tester la clé d'abord |
| Pare-feu | `ufw enable` coupe SSH | `ufw allow 22/tcp` avant d'activer |
| cron | chemins relatifs, `%` non échappé | chemins absolus, `\%` |
| Variables | `echo PATH` au lieu de `$PATH` | `$` pour lire ; écraser le `PATH` casse tout |

### Arbre de décision — « Quelle commande pour quel besoin ? »

```
Je veux...
├─ me repérer / naviguer ........... pwd, ls, cd, tree
├─ lire un fichier
│   ├─ petit ....................... cat
│   ├─ gros ........................ less
│   └─ suivre en direct ........... tail -f / journalctl -f
├─ chercher
│   ├─ du texte DANS des fichiers .. grep
│   └─ des fichiers (par nom) ...... find
├─ modifier des fichiers .......... touch, cp, mv, rm, nano/sudoedit
├─ comprendre les droits .......... ls -l, chmod, chown, id
├─ faire une action admin ......... sudo
├─ voir ce qui tourne ............. ps aux, top/htop, systemctl
├─ comprendre un problème ......... journalctl, systemctl status, dmesg
├─ regarder le réseau ............. ip a, ss -tulpn, ping
├─ me connecter à distance ........ ssh
├─ transférer des fichiers ........ scp, rsync
├─ installer un logiciel .......... sudo apt install
├─ gérer l'espace disque .......... df -h, du -sh, lsblk, findmnt
├─ archiver / sauvegarder ......... tar, gzip, rsync
└─ automatiser .................... script Bash + cron
```

### Pour continuer

Tu as les fondations solides de l'administration Linux. Voici les prolongements naturels :

- **Scripting Bash approfondi** : conditions, boucles, fonctions, gestion d'arguments et de cas d'erreur. C'est le complément direct du chapitre 26, pour transformer tes commandes en véritables outils. *(Un cours de scripting Bash dédié prolonge idéalement cette formation.)*
- **Python pour l'automatisation défensive** : quand Bash atteint ses limites (parsing complexe, API, structures de données), Python prend le relais — particulièrement en analyse de logs, OSINT et traitement d'IOC.
- **Cybersécurité défensive / SOC** : approfondis l'analyse de logs, la détection d'intrusion, les SIEM. Les chapitres 4, 11, 12, 15 et le projet 3 en sont la porte d'entrée.
- **Pentest débutant / eJPT** : l'énumération système (chapitres 10-12), le réseau (chapitre 17) et SSH (chapitre 18) constituent exactement les bases attendues. Tu connais déjà le versant défensif de ce que cette certification aborde côté offensif.
- **La pratique, surtout** : monte un petit lab (quelques VM), casse-le, répare-le, automatise-le. C'est en administrant de vraies machines qu'on devient administrateur.

Bon parcours sous Linux.

---
---


## ANNEXES

Ces sujets dépassent le cœur du cours débutant, mais valent d'être connus quand tu progresseras. Ils sont volontairement traités en survol : chacun mériterait un cours à part entière.

### Annexe A — Expressions régulières (regex)

Les **regex** sont des motifs de recherche puissants, utilisés par `grep`, `sed`, `awk` et bien d'autres. Le cours en a montré l'usage le plus simple (chercher un mot littéral). Les regex permettent bien plus : `^` (début de ligne), `$` (fin de ligne), `.` (n'importe quel caractère), `*` (répétition), `[0-9]` (un chiffre), etc. Par exemple, `grep -E "^[0-9]+" fichier` trouve les lignes commençant par un nombre. C'est un domaine entier à explorer une fois les bases acquises ; il décuple la puissance de la recherche et du filtrage de logs.

### Annexe B — `sed` et `awk` avancés

Le chapitre 4 en a montré l'usage minimal (substitution simple, extraction de colonne). En réalité, `sed` est un éditeur de flux complet (suppression de lignes, insertion, plages d'adresses) et `awk` est un véritable **langage de traitement de texte** (variables, conditions, calculs, agrégations par champ). Pour l'analyse de logs poussée, ils sont irremplaçables — mais leur apprentissage approfondi relève d'un module dédié.

### Annexe C — Stockage avancé : partitions, LVM, RAID

Le chapitre 21 s'est concentré sur l'**observation** du stockage. La gestion avancée comprend : le **partitionnement** (`fdisk`, `parted`), le **LVM** (*Logical Volume Manager*, qui permet de redimensionner et combiner des volumes à chaud), et le **RAID** (combiner plusieurs disques pour la performance ou la redondance). Ces opérations sont puissantes mais risquées pour les données : à aborder en lab, avec méthode, une fois les fondamentaux maîtrisés.

### Annexe D — Pare-feu avancé : `iptables` / `nftables`

Le chapitre 25 a utilisé `ufw`, qui est une surcouche simplifiée. En dessous se trouvent `iptables` (historique) et `nftables` (moderne), qui offrent un contrôle très fin du trafic réseau (règles par protocole, par interface, NAT, etc.). C'est le niveau qu'on atteint pour des configurations réseau complexes ou des passerelles.

### Annexe E — Conteneurs et virtualisation

Au-delà des VM utilisées pour ce cours, l'écosystème moderne s'appuie massivement sur les **conteneurs** (Docker, Podman) : une façon légère d'empaqueter et d'isoler des applications. C'est une compétence majeure aujourd'hui, qui s'appuie directement sur les notions Linux de ce cours (processus, systèmes de fichiers, réseau, permissions). Un excellent sujet pour la suite.

### Annexe F — Familles de distributions

Le cours s'est concentré sur **Debian/Ubuntu** (gestionnaire `apt`). Les autres grandes familles : **RHEL/CentOS/Fedora/Rocky** (gestionnaire `dnf`/`yum`, logs dans `/var/log/secure`), et **Arch** (`pacman`, philosophie « rolling release »). Les **concepts** (permissions, processus, systemd, réseau) sont identiques partout ; seules changent quelques commandes de gestion de paquets et l'emplacement de certains fichiers. Savoir cela te permet de t'adapter à n'importe quelle distribution.

---
