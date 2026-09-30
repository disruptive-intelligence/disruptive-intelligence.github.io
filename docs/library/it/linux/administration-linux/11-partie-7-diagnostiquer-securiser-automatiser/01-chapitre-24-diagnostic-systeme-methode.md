---
title: Chapitre 24 — Diagnostic système (méthode)
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 7 — Diagnostiquer, sécuriser, automatiser
  - index.md
---

## Le minimum à savoir

### Une méthode, pas une liste de commandes

Face à un problème (« le serveur est lent », « un service ne démarre pas », « le disque est plein »), le débutant tape des commandes au hasard. L'administrateur suit une **méthode** : du symptôme vers la cause, en éliminant les pistes une à une. Ce chapitre ne t'apprend presque aucune commande nouvelle — tu les connais toutes. Il t'apprend à les **enchaîner intelligemment**.

La démarche générale :

1. **Observer le symptôme précisément.** « Lent » ne veut rien dire ; lent à quoi ? depuis quand ? pour qui ?
2. **Formuler des hypothèses.** CPU saturé ? Mémoire pleine ? Disque plein ? Réseau coupé ? Service planté ?
3. **Vérifier chaque hypothèse** avec l'outil adapté, en commençant par le plus probable.
4. **Lire les logs**, qui racontent souvent directement ce qui s'est passé.
5. **Corriger**, puis **vérifier** que le problème a disparu.

### La trousse de diagnostic (tout ce que tu connais déjà)

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

## Très utile en pratique

### Scénario 1 : « la machine est lente »

```bash
uptime           # la charge est-elle anormalement haute ?
top              # quel processus dévore le CPU ? (trie par %CPU)
free -h          # la mémoire est-elle pleine ? (le système "swappe"-t-il ?)
df -h            # le disque est-il plein ? (un disque plein ralentit tout)
```


On part du plus global (`uptime`, `top`) vers le plus précis. Le coupable est presque toujours l'un de ces quatre : un processus emballé, la mémoire saturée, le disque plein, ou un disque défaillant (`dmesg -T`).

### Scénario 2 : « un service ne démarre pas »

```bash
sudo systemctl status nginx      # quel est l'état ? que dit le résumé ?
journalctl -u nginx -e           # le journal complet du service (fin)
journalctl -u nginx --since "10 min ago"   # juste avant l'échec
```


Le couple `status` + `journalctl -u` (chapitres 14-15) résout l'immense majorité des cas : le service écrit **pourquoi** il a échoué (port déjà utilisé, fichier de config invalide, permission manquante…). On lit, on comprend, on corrige.

### Scénario 3 : « pas d'accès réseau »

```bash
ip a                     # ai-je une adresse IP ?
ip r                     # ai-je une passerelle (route par défaut) ?
ping 8.8.8.8             # le réseau répond-il par IP ?
ping exemple.com         # le DNS résout-il les noms ?
```


On remonte la chaîne : interface → adresse → passerelle → connectivité IP → DNS. Le premier maillon qui casse désigne la cause (souvenir du chapitre 17 : IP OK mais nom KO = problème DNS).

> **Le réflexe maître :** quel que soit le problème, **les logs parlent**. Avant de spéculer longuement, lis `journalctl -e` et le `status` du service concerné. La réponse y est souvent écrite noir sur blanc.

## ❌ Erreur classique

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


## Exercices

**Guidé :** Fais un bilan de santé complet de ta machine en enchaînant : `uptime`, `free -h`, `df -h`, et `top` (quelques secondes, puis `q`). Pour chacun, note une conclusion : la charge est-elle normale ? reste-t-il de la mémoire ? de l'espace disque ? un processus consomme-t-il anormalement ?

**Autonome :** Choisis un service actif sur ta machine (vu au chapitre 14). Affiche son `systemctl status`, puis son journal récent avec `journalctl -u <service> --since "today"`. Entraîne-toi à lire ces sorties comme un diagnostic : le service est-il sain ? Y a-t-il des avertissements ou erreurs ?

**Défi :** Rédige ta propre **checklist de diagnostic** « machine lente », sous forme d'une liste ordonnée de commandes à lancer, avec pour chacune la question à laquelle elle répond et ce qui constituerait un résultat anormal. Tu construis là un véritable outil de travail réutilisable — exactement ce qu'un administrateur garde sous la main.

## ✅ Tu sais maintenant…

- Suivre une **méthode** : symptôme → hypothèses → vérification → logs → correction → vérification
- Mobiliser ta **trousse de diagnostic** (`uptime`, `top`, `free`, `df`/`du`, `systemctl`, `journalctl`, `dmesg`, `ping`/`ip`/`ss`)
- Lire la **charge** avec `uptime` et la relativiser au nombre de cœurs
- Dérouler les scénarios types : machine lente, service en panne, réseau coupé
- Que **les logs contiennent souvent la réponse** : les lire avant de spéculer
- Comprendre la cause **avant** de redémarrer

---
