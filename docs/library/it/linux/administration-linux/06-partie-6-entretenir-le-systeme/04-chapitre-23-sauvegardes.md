---
title: Chapitre 23 — Sauvegardes
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 6 — Entretenir le système
  - index.md
---

## Le minimum à savoir

### Pourquoi sauvegarder : la question n'est pas « si » mais « quand »

Un disque tombe en panne, un fichier est supprimé par erreur (`rm`, chapitre 5 !), une attaque chiffre les données… Tôt ou tard, **on perd des données**. La seule protection est la **sauvegarde** : une copie, ailleurs, qu'on peut restaurer. Ce n'est pas optionnel en administration ; c'est une responsabilité fondamentale.

### La règle 3-2-1

La référence en matière de sauvegarde tient en trois chiffres :

- **3** copies des données (l'originale + 2 sauvegardes)
- **2** supports différents (par exemple disque interne + disque externe)
- **1** copie hors site (ailleurs physiquement, pour survivre à un incendie, un vol, une attaque)

Pour débuter, retiens l'esprit : **une sauvegarde sur le même disque que l'original ne protège de presque rien.** Une vraie sauvegarde est ailleurs.

### Sauvegarde complète vs incrémentale

- Une sauvegarde **complète** copie tout, à chaque fois : simple, mais lourde et lente.
- Une sauvegarde **incrémentale** ne copie que ce qui a **changé** depuis la dernière fois : rapide et économe. C'est exactement ce que fait `rsync` (chapitre 19), ce qui en fait un excellent outil de sauvegarde.

## Très utile en pratique

### Sauvegarder avec `rsync`

`rsync` (vu au chapitre 19) est idéal : il ne copie que les changements, préserve les attributs, et fonctionne aussi bien en local que vers une machine distante.

```bash
# Sauvegarde locale vers un disque externe monté
rsync -av --delete ~/documents/ /mnt/backup/documents/

# Sauvegarde vers un serveur distant (à travers SSH, chapitre 18)
rsync -av ~/documents/ alice@serveur:/sauvegardes/documents/
```


L'option `--delete` rend la sauvegarde **identique** à la source (elle supprime côté sauvegarde ce qui a disparu côté source). Puissante, donc à manier avec soin :

> **⚠️ Prudence avec `--delete` :** combinée à une erreur de chemin, elle peut supprimer des fichiers de ta sauvegarde. **Teste toujours avec `--dry-run` d'abord** (chapitre 19) : `rsync -av --delete --dry-run ...`. C'est le même réflexe de prudence qui traverse tout le cours.

### Sauvegarder avec `tar` (archive datée)

Pour une sauvegarde ponctuelle sous forme d'archive unique (facile à stocker et à dater) :

```bash
tar -czvf backup-$(date +%F).tar.gz ~/documents/    # archive horodatée du jour
```


Le `$(date +%F)` insère la date (format `2025-01-10`) dans le nom : tu obtiens un historique clair de tes sauvegardes.

### Planifier les sauvegardes

Une sauvegarde n'a de valeur que si elle est **régulière**. On combine donc ce chapitre avec la planification du chapitre 16. Un petit script de sauvegarde, déposé en cron, et la machine se sauvegarde toute seule chaque nuit :

```bash
# Exemple de ligne crontab : sauvegarde chaque jour à 2h30
30 2 * * * /home/alice/scripts/sauvegarde.sh
```


> Souviens-toi du piège du chapitre 16 : dans un script planifié, utilise des **chemins absolus**, car cron s'exécute dans un environnement minimal.

### Le point le plus oublié : tester la restauration

**Une sauvegarde qu'on n'a jamais testée n'est pas une sauvegarde.** Beaucoup découvrent, le jour fatidique, que leurs sauvegardes étaient vides, corrompues ou incomplètes. Le réflexe professionnel : **restaurer régulièrement** un fichier au hasard pour vérifier que ça fonctionne.

```bash
# Vérifier qu'on peut bien extraire une archive de sauvegarde
tar -tzvf backup-2025-01-10.tar.gz | head     # le contenu est-il bien là ?
# Puis tester une vraie extraction dans un dossier temporaire
mkdir /tmp/test-restore && tar -xzvf backup-2025-01-10.tar.gz -C /tmp/test-restore
```


> **Très utile en sécurité :** face à une attaque par rançongiciel (qui chiffre les données), des sauvegardes **hors ligne, testées et régulières** sont souvent la seule façon de tout récupérer sans céder. C'est une pièce maîtresse de la résilience défensive.

## ❌ Erreur classique

```bash
# Sauvegarder sur le même disque que l'original
rsync -av ~/data/ /autre-dossier-du-meme-disque/   # ❌ le disque meurt = tout est perdu
rsync -av ~/data/ /mnt/disque-externe/             # ✅ support différent

# Utiliser --delete sans simuler
rsync -av --delete ~/data/ /mnt/backup/            # ❌ une erreur de chemin = perte
rsync -av --delete --dry-run ~/data/ /mnt/backup/  # ✅ simuler d'abord

# Ne jamais tester la restauration
# ❌ découvrir le jour J que la sauvegarde était inutilisable
tar -tzvf backup.tar.gz                            # ✅ vérifier régulièrement

# Croire qu'une copie unique suffit
# ❌ une seule copie n'est pas une stratégie : pense 3-2-1
```


## Exercices

**Guidé :** Crée un dossier `~/precieux/` avec quelques fichiers. Réalise une première sauvegarde complète vers un autre dossier avec `rsync -av ~/precieux/ ~/sauvegarde-precieux/`. Modifie ensuite un fichier de `~/precieux/`, relance le même `rsync`, et observe : seul le fichier modifié est transféré (c'est l'aspect incrémental).

**Autonome :** Crée une archive de sauvegarde horodatée de ton dossier `~/precieux/` avec `tar -czvf backup-$(date +%F).tar.gz ~/precieux/`. Vérifie son contenu sans l'extraire. Puis **teste la restauration** : extrais l'archive dans `/tmp/restore-test/` et confirme que tes fichiers sont bien là, intacts.

**Défi :** Conçois (sur le papier ou en vrai script) une stratégie de sauvegarde complète appliquant la règle 3-2-1 pour un dossier important. Décris : quoi sauvegarder, vers où (deux supports, une copie distante), à quelle fréquence (et comment la planifier avec cron), et comment tu vérifierais régulièrement que les sauvegardes sont restaurables. Tu mobilises ici rsync, tar, SSH et cron — toute la Partie 6.

## ✅ Tu sais maintenant…

- Pourquoi sauvegarder est une **responsabilité fondamentale**, pas une option
- La règle **3-2-1** (3 copies, 2 supports, 1 hors site)
- La différence entre sauvegarde **complète** et **incrémentale**
- Sauvegarder avec `rsync` (incrémental, local ou distant) et la prudence du `--delete` + `--dry-run`
- Créer des archives **horodatées** avec `tar` et `$(date +%F)`
- **Planifier** les sauvegardes avec cron (chemins absolus)
- Que **tester la restauration** est indispensable, et le rôle des sauvegardes contre les rançongiciels

---

> **🏁 CHECKPOINT 6 — Fin de la Partie 6**
>
> Tu sais maintenant **entretenir un système sur la durée** : installer et tenir les logiciels à jour, surveiller l'espace disque et la mémoire, archiver des données, et mettre en place des sauvegardes fiables et testées. Ce sont les gestes qui maintiennent une machine en bonne santé année après année.
>
> **Auto-évaluation — sauras-tu, sans aide :**
> - mettre à jour ton système proprement, et expliquer `update` vs `upgrade` ?
> - constater un disque plein avec `df`, puis trouver le coupable avec `du` ?
> - observer la structure de stockage avec `lsblk` et `findmnt` sans rien risquer ?
> - créer et extraire une archive `.tar.gz` ?
> - mettre en place une sauvegarde `rsync` incrémentale et tester sa restauration ?
>
> Si oui, tu sais faire vivre un système dans le temps. Il ne reste qu'à tout réunir : diagnostiquer, sécuriser et automatiser. Place à la **Partie 7 — Diagnostiquer, sécuriser, automatiser**, la synthèse appliquée du cours.

---

---
---
