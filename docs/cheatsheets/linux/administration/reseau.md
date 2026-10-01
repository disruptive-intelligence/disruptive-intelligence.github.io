---
title: "Réseau et résolution de noms"
cours:
  - library/it/linux/administration-linux/index.md
---

# Réseau et résolution de noms

Ajouter un nom dans /etc/hosts, changer de DNS, d'adresse ou de passerelle, rendre la configuration persistante, ouvrir un port.

Les incontournables : `tee -a /etc/hosts` · `resolvectl` · `ip addr add` · `nmcli` · `ufw allow`
{ .kw-cs-top }

## Noms

### Ajouter une IP dans /etc/hosts

```bash title="Commande"
echo "<IP> <nom> [<alias>]" | sudo tee -a /etc/hosts
```

```bash title="Exemple"
echo "192.168.1.50 intranet.local intranet" | sudo tee -a /etc/hosts
```

```bash title="Exemple 2"
getent hosts intranet.local   # vérifier que le nom est bien résolu
```

!!! warning "Attention"
    `sudo echo … >> /etc/hosts` échoue : la redirection est faite par ton shell, sans droits root. D'où `tee -a`.

Pour comprendre : [Administration Linux, ch. 17](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
{ .kw-cs-meta }

### Retirer une entrée de /etc/hosts

```bash title="Commande"
sudo sed -i.bak '/<nom>/d' /etc/hosts
```

```bash title="Exemple"
sudo sed -i.bak '/intranet.local/d' /etc/hosts
```

### Voir et changer le DNS utilisé

```bash title="Commande"
resolvectl status
sudo resolvectl dns <interface> <IP>
```

```bash title="Exemple"
resolvectl status | grep -A2 'DNS Servers'
```

```bash title="Exemple 2"
sudo resolvectl dns eth0 1.1.1.1   # jusqu'au prochain redémarrage du réseau
```

### Changer le nom d'hôte

```bash title="Commande"
sudo hostnamectl set-hostname <nom>
```

```bash title="Exemple"
sudo hostnamectl set-hostname srv-web-01
```

## Adresses et routes

### Ajouter une adresse IP temporaire

```bash title="Commande"
sudo ip addr add <IP>/<masque> dev <interface>
```

```bash title="Exemple"
sudo ip addr add 192.168.1.50/24 dev eth0
```

!!! warning "Attention"
    Perdue au redémarrage : voir l'entrée suivante pour la rendre persistante.

### Rendre une configuration IP persistante

```bash title="Commande"
nmcli con show
sudo nmcli con mod "<connexion>" <réglages>
```

```bash title="Exemple"
nmcli con show
```

```bash title="Exemple 2"
sudo nmcli con mod "Wired connection 1" ipv4.method manual ipv4.addresses 192.168.1.50/24 ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1
sudo nmcli con up "Wired connection 1"
```

### Changer la passerelle par défaut

```bash title="Commande"
sudo ip route replace default via <passerelle>
```

```bash title="Exemple"
sudo ip route replace default via 192.168.1.1
```

### Activer ou désactiver une interface

```bash title="Commande"
sudo ip link set <interface> up|down
```

```bash title="Exemple"
sudo ip link set eth1 down
```

## Pare-feu

### Ouvrir un port dans le pare-feu

```bash title="Commande"
sudo ufw allow <port>/<protocole>
```

```bash title="Exemple"
sudo ufw allow 443/tcp
```

```bash title="Exemple 2"
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp   # SSH depuis le réseau local seulement
```

Pour comprendre : [Linux — prises de notes, disques et pare-feu](../../../library/it/linux/linux-prises-de-notes/06-systeme-sauvegarde-disques-pare-feu-et-shell.md)
{ .kw-cs-meta }

### Voir les règles du pare-feu

```bash title="Commande"
sudo ufw status verbose
sudo iptables -L -n -v
```

```bash title="Exemple"
sudo ufw status numbered
```

```bash title="Exemple 2"
sudo nft list ruleset   # règles nftables
```
