---
title: Chapitre 12 — Permissions avancées (panorama)
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 3 — Qui a le droit de quoi
  - index.md
---

## Le minimum à savoir

### Au-delà des r/w/x : un panorama

Le modèle r/w/x du chapitre 9 couvre 95 % des situations. Mais il existe des permissions **spéciales** qui résolvent des problèmes particuliers — et qui sont, justement pour cette raison, des **cibles privilégiées en sécurité**. L'objectif de ce chapitre n'est pas de te rendre expert, mais de te faire **reconnaître** ces mécanismes : tu dois savoir qu'ils existent, ce qu'ils font, et comment les repérer. C'est exactement ce qu'on regarde lors d'un audit ou d'une recherche d'élévation de privilèges.

### Le bit SUID : exécuter avec les droits du propriétaire

Normalement, quand tu lances un programme, il s'exécute avec **tes** droits. Le bit **SUID** (*Set User ID*) change cela : un programme avec SUID s'exécute avec les droits de **son propriétaire**, pas les tiens. Si le propriétaire est root, le programme tourne donc avec les pouvoirs de root, même lancé par un utilisateur normal.

Un exemple légitime et universel : `passwd`. Pour changer ton mot de passe, le système doit écrire dans `/etc/shadow` (réservé à root). `passwd` est donc SUID root : il te laisse modifier **ta** ligne, en toute sécurité, sans te donner root pour autant.

On repère le SUID dans un `ls -l` par un **`s`** à la place du `x` du propriétaire :

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
#    ↑ ce "s" = bit SUID
```


### Pourquoi le SUID est central en sécurité

Le SUID est puissant, donc dangereux. **Un programme SUID root mal conçu ou inattendu est une porte vers les privilèges root.** Si un attaquant trouve sur le système un binaire SUID qui lui permet, d'une manière ou d'une autre, d'exécuter ses propres commandes, il devient root. C'est l'une des voies d'escalade les plus connues.

D'où un réflexe fondamental, aussi bien pour l'auditeur défensif que pour le testeur d'intrusion : **lister tous les fichiers SUID du système**.

```bash
find / -type f -perm -4000 2>/dev/null
```


Décortiquons cette commande, qui réunit tout ce que tu as appris :

- `find /` → cherche à partir de la racine (chapitre 4)
- `-type f` → uniquement des **fichiers** (pas des dossiers ni autres objets)
- `-perm -4000` → qui ont le bit SUID activé (le `4000` octal)
- `2>/dev/null` → on jette les innombrables « Permission denied » (chapitre 7) pour ne garder que les résultats utiles

> **Orientation cyber / eJPT :** cette commande figure dans toute checklist d'énumération d'un système Linux. Côté défense, on compare la liste obtenue aux binaires SUID **attendus** (ceux livrés par la distribution) ; tout SUID inhabituel mérite une enquête immédiate.

## Très utile en pratique

### SGID et sticky bit, en bref

Deux autres bits spéciaux, à connaître de nom :

- **SGID** (*Set Group ID*) : comme le SUID mais pour le **groupe**. Sur un dossier, il fait hériter tous les nouveaux fichiers du groupe du dossier — pratique pour le travail collaboratif. Repérable par un `s` dans le triplet du groupe.
- **Sticky bit** : posé sur un dossier partagé (comme `/tmp`), il empêche chacun de supprimer les fichiers des autres — tu ne peux effacer que **tes** fichiers. Repérable par un `t` à la fin :

    ```bash
    ls -ld /tmp
    # drwxrwxrwt ... /tmp     ← le "t" final = sticky bit
    ```


### Les capabilities : des privilèges root « en pièces détachées »

Sur les systèmes modernes, une alternative plus fine au tout-puissant SUID existe : les **capabilities**. Plutôt que de donner *tous* les pouvoirs de root à un programme, on lui accorde **un privilège précis et limité**. Par exemple, la capability `cap_net_raw` autorise un programme (comme `ping`) à manipuler le réseau à bas niveau, sans pour autant lui donner le reste des pouvoirs root.

On **observe** les capabilities présentes sur le système avec `getcap` :

```bash
getcap -r / 2>/dev/null      # liste récursivement tous les binaires porteurs de capabilities
```


> **Si `getcap` n'est pas disponible** (installations minimales), installe le paquet qui le fournit : `sudo apt install libcap2-bin`.

C'est le pendant moderne de la recherche de SUID : un binaire doté d'une capability trop puissante (ou inattendue) peut, lui aussi, ouvrir une voie d'escalade.

> **Important — observation, pas manipulation :** à ton niveau, `getcap` s'utilise en **observation** (lister, auditer). La commande inverse, `setcap`, qui *attribue* une capability à un binaire, ne doit être expérimentée qu'en **lab contrôlé**, sur une **copie** de binaire ou un exemple jetable — **jamais** sur un binaire système réel sans comprendre précisément ce que l'on fait. Modifier les capabilities d'un binaire système peut affaiblir gravement la sécurité de la machine.

### Les ACL, en un mot

Le modèle u/g/o ne permet qu'**un** propriétaire et **un** groupe. Quand on a besoin de droits plus granulaires (« alice peut écrire, bob peut seulement lire, et ce groupe précis a un autre accès »), on utilise les **ACL** (*Access Control Lists*). On les consulte avec `getfacl` et on les modifie avec `setfacl`. Pour débuter, retiens simplement qu'elles **existent** et permettent des permissions plus fines que le modèle de base — tu n'as pas à les manipuler maintenant.

## ❌ Erreur classique

```bash
# Oublier 2>/dev/null et se noyer sous les erreurs
find / -type f -perm -4000           # ❌ noyé sous les "Permission denied"
find / -type f -perm -4000 2>/dev/null  # ✅ seulement les résultats utiles

# Oublier -type f et lister autre chose que des fichiers
find / -perm -4000 2>/dev/null       # mélange fichiers et autres objets
find / -type f -perm -4000 2>/dev/null  # ✅ uniquement des fichiers

# Confondre le "s" du SUID et le "s" du SGID
# -rwsr-xr-x → SUID (s dans le triplet PROPRIÉTAIRE)
# -rwxr-sr-x → SGID (s dans le triplet GROUPE)

# Utiliser setcap sur un binaire système "pour tester"
sudo setcap cap_setuid+ep /usr/bin/python3   # ❌❌ faille de sécurité majeure
# ✅ getcap pour OBSERVER ; setcap seulement en lab sur une copie jetable

# Ajouter du SUID par curiosité
sudo chmod u+s /un/binaire           # ❌ ne jamais "essayer" ça sur un système réel
```


## Exercices

**Guidé :** Liste les fichiers SUID de ton système avec `find / -type f -perm -4000 2>/dev/null`. Tu devrais y voir des classiques comme `/usr/bin/passwd` ou `/usr/bin/sudo`. Choisis-en un et confirme son bit SUID avec `ls -l` : repères-tu bien le `s` à la place du `x` du propriétaire ?

**Autonome :** Observe le sticky bit de `/tmp` avec `ls -ld /tmp` et identifie le `t` final. Explique en une phrase pourquoi ce bit est important sur un dossier où **tout le monde** peut écrire. Ensuite, liste les capabilities présentes sur ta machine avec `getcap -r / 2>/dev/null` : combien de binaires en portent ?

**Défi (orientation sécurité) :** Tu fais l'inventaire de sécurité d'une machine. Produis deux listes : (1) tous les fichiers SUID, (2) tous les binaires avec capabilities. Enregistre chacune dans un fichier (avec `>` ou `tee`, chapitre 7) pour garder une trace. Ces deux listes constituent une **base de référence** : sur un vrai système, on les comparerait régulièrement pour détecter tout ajout suspect. Quel intérêt défensif vois-tu à conserver une telle référence dans le temps ?

## ✅ Tu sais maintenant…

- Que des permissions **spéciales** existent au-delà des r/w/x
- Ce qu'est le **SUID** (exécuter avec les droits du propriétaire) et comment le repérer (`s`)
- Pourquoi le SUID est une **voie d'escalade** majeure, et comment lister les SUID : `find / -type f -perm -4000 2>/dev/null`
- Reconnaître le **SGID** (`s` du groupe) et le **sticky bit** (`t`, sur `/tmp`)
- Que les **capabilities** découpent les pouvoirs de root, et les observer avec `getcap -r /` (jamais `setcap` hors lab)
- Que les **ACL** existent pour des droits plus fins (`getfacl`/`setfacl`)
- À constituer une **base de référence** SUID/capabilities, réflexe défensif

---

> **🏁 CHECKPOINT 3 — Fin de la Partie 3 (le plus important pour la sécurité)**
>
> Tu comprends maintenant **le modèle de sécurité de Linux** : qui possède quoi, qui peut faire quoi, comment on élève ses privilèges proprement, et où se cachent les voies d'escalade. C'est le socle de toute administration sérieuse et de toute analyse défensive.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - lire une ligne de `ls -l` et dire exactement qui peut lire, écrire, exécuter ?
> - traduire `chmod 640` en `rw-r-----` et inversement ?
> - expliquer le principe de moindre privilège et pourquoi `sudo commande` vaut mieux que `sudo -i` ?
> - retrouver dans les logs qui a utilisé `sudo` et quand ?
> - lister les binaires SUID d'un système et expliquer pourquoi c'est un enjeu de sécurité ?
>
> Si oui, tu as franchi l'étape conceptuelle la plus exigeante du cours. La suite va te faire passer de « gérer des fichiers et des droits » à « piloter une machine vivante » : place à la **Partie 4 — Processus, services et logs**.

---

---
---
