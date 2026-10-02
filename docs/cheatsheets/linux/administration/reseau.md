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
echo "<IP> <nom> [<alias>]" | sudo tee -a /etc/hosts   # tee -a : ajoute à la fin, avec les droits root
```

```bash title="Exemple"
echo "192.168.1.50 intranet.local intranet" | sudo tee -a /etc/hosts
```

??? example "Sortie"
    ```text
    192.168.1.50 intranet.local intranet
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
sudo sed -i.bak '/<nom>/d' /etc/hosts   # d : supprime les lignes qui correspondent
```

```bash title="Exemple"
sudo sed -i.bak '/intranet.local/d' /etc/hosts
```

### Voir et changer le DNS utilisé

```bash title="Commande"
resolvectl status                       # DNS par interface
sudo resolvectl dns <interface> <IP>    # changer (jusqu'au redémarrage du réseau)
```

```bash title="Exemple"
resolvectl status | grep -A1 'DNS Servers'
```

??? example "Sortie"
    ```text
           DNS Servers: 192.168.1.1
            DNS Domain: home.lan
    ```

```bash title="Exemple 2"
sudo resolvectl dns eth0 1.1.1.1
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
sudo ip addr add <IP>/<masque> dev <interface>   # ip addr del pour la retirer
```

```bash title="Exemple"
sudo ip addr add 192.168.1.51/24 dev eth0
```

!!! warning "Attention"
    Perdue au redémarrage : voir l'entrée suivante pour la rendre persistante.

### Rendre une configuration IP persistante

```bash title="Commande"
nmcli con show                                # nom des connexions
sudo nmcli con mod "<connexion>" <réglages>   # modifier, puis nmcli con up
```

```bash title="Exemple"
nmcli con show
```

??? example "Sortie"
    ```text
    NAME                UUID                                  TYPE      DEVICE
    Wired connection 1  7f3c1d2e-5a4b-4c3d-9e8f-0a1b2c3d4e5f  ethernet  eth0
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
sudo ip link set <interface> up     # activer
sudo ip link set <interface> down   # couper
```

```bash title="Exemple"
sudo ip link set eth1 down
```

## Pare-feu

### Ouvrir un port dans le pare-feu

```bash title="Commande"
sudo ufw allow <port>/<protocole>   # from <réseau> : seulement depuis ce réseau
```

```bash title="Exemple"
sudo ufw allow 443/tcp
```

??? example "Sortie"
    ```text
    Rule added
    Rule added (v6)
    ```

```bash title="Exemple 2"
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
```

Pour comprendre : [Linux — prises de notes, disques et pare-feu](../../../library/it/linux/linux-prises-de-notes/06-systeme-sauvegarde-disques-pare-feu-et-shell.md)
{ .kw-cs-meta }

### Voir les règles du pare-feu

```bash title="Commande"
sudo ufw status verbose    # UFW
sudo iptables -L -n -v     # iptables
sudo nft list ruleset      # nftables
```

```bash title="Exemple"
sudo ufw status numbered
```

??? example "Sortie"
    ```text
    Status: active

         To                         Action      From
         --                         ------      ----
    [ 1] 22/tcp                     ALLOW IN    192.168.1.0/24
    [ 2] 443/tcp                    ALLOW IN    Anywhere
    ```
