---
title: Chapitre 25 — Sécurité de base (durcissement)
source: IT/01_Linux/Admin_Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 7 — Diagnostiquer, sécuriser, automatiser
  - index.md
---

## Le minimum à savoir

### Durcir, c'est réduire la surface d'attaque

**Durcir** (*hardening*) une machine, c'est diminuer le nombre de façons dont elle peut être attaquée. Le principe directeur, déjà rencontré au chapitre 11, est le **moindre privilège** appliqué à tout : moins de services qui tournent, moins de ports ouverts, moins de comptes, moins de droits, moins de logiciels. **Tout ce qui n'est pas nécessaire est une porte potentielle qu'on ferme.** Ce chapitre rassemble, sous l'angle défensif, beaucoup de réflexes vus tout au long du cours.

### Les fondamentaux, dans l'ordre d'importance

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

## Très utile en pratique

### Le pare-feu simple : `ufw`

Un **pare-feu** contrôle quelles connexions réseau sont autorisées. Sous Debian/Ubuntu, `ufw` (*Uncomplicated Firewall*) le rend accessible. La logique de durcissement : **tout bloquer par défaut, puis n'ouvrir que le nécessaire.**

```bash
sudo ufw default deny incoming       # bloquer toutes les connexions entrantes par défaut
sudo ufw default allow outgoing      # autoriser les connexions sortantes
sudo ufw allow 22/tcp                # autoriser SSH (sinon on se coupe l'accès !)
sudo ufw enable                      # activer le pare-feu
sudo ufw status verbose              # vérifier les règles actives
```


> **⚠️ Prudence (lien chapitre 18) :** avant d'activer le pare-feu sur une machine distante, **autorise SSH d'abord** (`ufw allow 22/tcp`). Sinon, `ufw enable` te couperait immédiatement ta propre connexion. Le même réflexe « ne te verrouille pas dehors » que pour SSH.

### Se protéger de la force brute : `fail2ban` (notion)

`fail2ban` surveille les logs (chapitre 15) et **bannit automatiquement** les adresses IP qui multiplient les échecs de connexion (typiquement, les attaques par force brute SSH du chapitre 4). C'est la réponse automatisée à la menace qu'on a appris à **détecter** manuellement.

```bash
sudo systemctl status fail2ban       # vérifier qu'il tourne
sudo fail2ban-client status sshd     # voir les IP bannies pour SSH
```


Pour débuter, retiens son principe : il transforme la détection (compter les échecs dans les logs) en **protection active** (bloquer l'attaquant). Sa configuration fine dépasse ce cours.

> **`fail2ban` n'est pas magique :** l'installer ne suffit pas toujours. Il faut **vérifier que la jail SSH est activée**, que les logs qu'il surveille correspondent bien à ta distribution (`auth.log` / `secure` / `journalctl`, chapitre 15), et **tester** que les bannissements fonctionnent réellement (`sudo fail2ban-client status sshd`). On l'utilise donc comme un mécanisme **à configurer et à tester**, pas comme une protection automatique garantie.

### La checklist de durcissement

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

## ❌ Erreur classique

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


## Exercices

**Guidé :** Fais un mini-audit de durcissement de ta machine, **sans rien modifier**. Vérifie : le système est-il à jour (`apt list --upgradable`) ? Quels ports écoutent (`sudo ss -tulpn`) ? Le pare-feu est-il actif (`sudo ufw status`) ? Y a-t-il une connexion root SSH autorisée (`grep PermitRootLogin /etc/ssh/sshd_config`) ? Note ce qui pourrait être amélioré.

**Autonome (en lab) :** Sur une machine de test (pas un accès distant unique !), configure `ufw` proprement : politique deny par défaut en entrée, autorise SSH, active-le, et vérifie avec `ufw status verbose`. Confirme que tu as toujours accès. Désactive-le ensuite si c'était juste un exercice (`sudo ufw disable`).

**Défi (orientation sécurité) :** Reprends la checklist de durcissement ci-dessus et applique-la, point par point, à ta machine d'apprentissage. Pour chaque ligne, note l'état actuel (conforme / à corriger) et la commande qui vérifie ou corrige. Tu produis ainsi un **rapport de durcissement** — exactement le livrable d'un travail de sécurisation réel.

## ✅ Tu sais maintenant…

- Que **durcir** = réduire la surface d'attaque (moindre privilège appliqué à tout)
- L'ordre des priorités : **mises à jour** d'abord, puis services/ports, SSH, comptes, pare-feu
- Configurer un pare-feu avec `ufw` (deny par défaut, ouvrir le strict nécessaire, autoriser SSH avant `enable`)
- Que `fail2ban` transforme la **détection** de force brute en **protection** automatique
- Dérouler une **checklist de durcissement** complète, qui réunit tout le cours
- Que le durcissement défensif est le miroir de l'énumération offensive

---
