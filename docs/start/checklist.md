---
tags:
  - checklist
---
# Checklist avant engagement

À dérouler au début de chaque CTF, box ou pentest.

## 1. Comprendre le contexte

- [ ] Type d'exercice : CTF / box / lab / pentest réel
- [ ] Périmètre (scope) : quelles IP, quels domaines, ce qui est **interdit**
- [ ] Objectif : flags user/root, compromission du domaine, rapport…
- [ ] Informations fournies au départ (identifiants, VPN, description)

## 2. Préparer l'environnement

- [ ] VPN connecté et IP VPN relevée
- [ ] Dossier de travail créé

```bash
mkdir -p ~/ctf/<nom_box>/{nmap,loot,exploits} && cd ~/ctf/<nom_box>
```

- [ ] Session `tmux` ouverte (les variables restent dans la session)

## 3. Définir les variables — une seule fois

Voir [Conventions](conventions.md) pour le détail.

```bash
cat > target.env <<'VARS'
export IP=<ip_cible>
export DOMAIN=<domaine>
export DC=<fqdn_dc>
export LHOST=<ip_vpn>
export LPORT=4444
VARS
source target.env
```

- [ ] Vérifier : `echo $IP $DOMAIN $LHOST`
- [ ] Dans un nouveau terminal : `source target.env`

## 4. Résolution de noms

- [ ] Ajouter la cible dans `/etc/hosts` si un nom de domaine est connu

```bash
echo "$IP $DOMAIN $DC" | sudo tee -a /etc/hosts
```

## 5. Prise de notes

- [ ] Note Obsidian ouverte pour la box (brute, privée)
- [ ] Rappel : ce qui est **générique** ira ensuite dans le wiki — jamais d'IP, flags ou mots de passe

## 6. Lancer

→ [Méthodologie](../methodology/index.md)
