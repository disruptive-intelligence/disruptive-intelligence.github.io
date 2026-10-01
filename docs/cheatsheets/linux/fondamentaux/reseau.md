---
title: "Réseau"
cours:
  - library/it/linux/administration-linux/index.md
  - library/it/linux/linux-prises-de-notes/index.md
---

# Réseau

Voir ses adresses, routes, ports et connexions ; tester la connectivité et la résolution de noms ; capturer du trafic.

Les incontournables : `ip -br a` · `ip route` · `ss -tulpn` · `ss -tnp` · `dig +short` · `curl -I`
{ .kw-cs-top }

## Configuration

### Voir ses adresses IP

```bash title="Commande"
ip -br a
```

```bash title="Exemple"
ip a show eth0   # détail d'une interface
```

Pour comprendre : [Administration Linux, ch. 17](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
{ .kw-cs-meta }

### Voir la table de routage et la passerelle

```bash title="Commande"
ip route
```

```bash title="Exemple"
ip route get 8.8.8.8   # interface et passerelle utilisées pour joindre cette IP
```

### Voir la table ARP (machines voisines)

```bash title="Commande"
ip neigh
```

```bash title="Exemple"
ip neigh show dev eth0
```

## Ports et connexions

### Voir les ports en écoute

```bash title="Commande"
sudo ss -tulpn
```

```bash title="Exemple"
sudo ss -tulpn | grep ':22 '   # qui écoute sur le port 22
```

Ensuite : [savoir quel processus utilise un port](#savoir-quel-processus-utilise-un-port) — Pour comprendre : [Linux — prises de notes, réseau](../../../library/it/linux/linux-prises-de-notes/05-reseau-et-services.md)
{ .kw-cs-meta }

### Voir les connexions établies

```bash title="Commande"
sudo ss -tnp state established
```

```bash title="Exemple"
sudo ss -tnp state established
```

```bash title="Exemple 2"
sudo ss -tnp dst 203.0.113.10   # connexions vers une IP précise
```

Ensuite : [tout savoir sur un PID](processus.md#tout-savoir-sur-un-pid)
{ .kw-cs-meta }

### Savoir quel processus utilise un port

```bash title="Commande"
sudo lsof -i :<port>
```

```bash title="Exemple"
sudo lsof -i :8080
```

## Tester

### Tester la connectivité

```bash title="Commande"
ping -c <N> <hôte>
```

```bash title="Exemple"
ping -c 4 1.1.1.1
```

```bash title="Exemple 2"
traceroute example.com   # le chemin, saut par saut
```

### Résoudre un nom

```bash title="Commande"
dig +short <nom>
getent hosts <nom>
```

```bash title="Exemple"
dig +short example.com
```

```bash title="Exemple 2"
getent hosts intranet.local   # suit /etc/hosts puis le DNS, comme les applications
```

Ensuite : [ajouter une IP dans /etc/hosts](../administration/reseau.md#ajouter-une-ip-dans-etchosts)
{ .kw-cs-meta }

### Tester un port distant

```bash title="Commande"
nc -zv <hôte> <port>
```

```bash title="Exemple"
nc -zv 192.168.1.10 22
```

### Interroger un service web

```bash title="Commande"
curl -I <url>
```

```bash title="Exemple"
curl -sI https://example.com | head -5   # code et en-têtes de réponse
```

```bash title="Exemple 2"
curl -s -o /dev/null -w '%{http_code} %{time_total}s\n' https://example.com   # code et temps de réponse
```

## Capturer

### Capturer du trafic

```bash title="Commande"
sudo tcpdump -i <interface> -n <filtre>
```

```bash title="Exemple"
sudo tcpdump -i eth0 -n host 192.168.1.10 and port 443
```

```bash title="Exemple 2"
sudo tcpdump -i eth0 -nn -w capture.pcap   # enregistrer pour l'ouvrir dans Wireshark
```

!!! warning "Attention"
    Une capture peut contenir des identifiants et des données personnelles : la stocker comme une donnée sensible.
