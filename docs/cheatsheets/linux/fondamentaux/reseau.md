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
ip -br a               # forme courte : interface, état, adresses
ip a show <interface>  # détail d'une interface
```

```bash title="Exemple"
ip -br a
```

??? example "Sortie"
    ```text
    lo      UNKNOWN  127.0.0.1/8 ::1/128
    eth0    UP       192.168.1.50/24 fe80::a00:27ff:fe4e:66a1/64
    ```

Pour comprendre : [Administration Linux, ch. 17](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
{ .kw-cs-meta }

### Voir la table de routage et la passerelle

```bash title="Commande"
ip route               # table de routage
ip route get <IP>      # route utilisée pour joindre cette IP
```

```bash title="Exemple"
ip route
```

??? example "Sortie"
    ```text
    default via 192.168.1.1 dev eth0 proto dhcp metric 100
    192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.50
    ```

```bash title="Exemple 2"
ip route get 8.8.8.8
```

### Voir la table ARP (machines voisines)

```bash title="Commande"
ip neigh   # IP, interface, adresse MAC, état
```

```bash title="Exemple"
ip neigh
```

??? example "Sortie"
    ```text
    192.168.1.1 dev eth0 lladdr 3c:52:82:aa:10:01 REACHABLE
    192.168.1.23 dev eth0 lladdr 08:00:27:3b:91:5e STALE
    ```

## Ports et connexions

### Voir les ports en écoute

```bash title="Commande"
sudo ss -tulpn   # t TCP, u UDP, l en écoute, p programme, n sans résolution de noms
```

```bash title="Exemple"
sudo ss -tulpn
```

??? example "Sortie"
    ```text
    Netid State  Local Address:Port  Peer Address:Port Process
    udp   UNCONN 127.0.0.53%lo:53      0.0.0.0:*         users:(("systemd-resolve",pid=611,fd=13))
    tcp   LISTEN 0.0.0.0:22           0.0.0.0:*         users:(("sshd",pid=812,fd=3))
    tcp   LISTEN 0.0.0.0:80           0.0.0.0:*         users:(("nginx",pid=1234,fd=6))
    tcp   LISTEN 127.0.0.1:3306       0.0.0.0:*         users:(("mysqld",pid=901,fd=21))
    ```

```bash title="Exemple 2"
sudo ss -tulpn | grep ':22 '   # qui écoute sur le port 22
```

Ensuite : [savoir quel processus utilise un port](#savoir-quel-processus-utilise-un-port) — Pour comprendre : [Linux — prises de notes, réseau](../../../library/it/linux/linux-prises-de-notes/05-reseau-et-services.md)
{ .kw-cs-meta }

### Voir les connexions établies

```bash title="Commande"
sudo ss -tnp state established   # connexions TCP en cours avec leur processus
```

```bash title="Exemple"
sudo ss -tnp state established
```

??? example "Sortie"
    ```text
    Recv-Q Send-Q Local Address:Port  Peer Address:Port  Process
    0      0      192.168.1.50:22     192.168.1.23:51544 users:(("sshd",pid=5123,fd=4))
    0      0      192.168.1.50:41870  203.0.113.10:443   users:(("curl",pid=6610,fd=5))
    ```

```bash title="Exemple 2"
sudo ss -tnp dst 203.0.113.10   # connexions vers une IP précise
```

Ensuite : [tout savoir sur un PID](processus.md#tout-savoir-sur-un-pid)
{ .kw-cs-meta }

### Savoir quel processus utilise un port

```bash title="Commande"
sudo lsof -i :<port>   # processus, utilisateur, connexion
```

```bash title="Exemple"
sudo lsof -i :8080
```

??? example "Sortie"
    ```text
    COMMAND  PID  USER FD  TYPE DEVICE SIZE/OFF NODE NAME
    python3 7012 alice  3u IPv4  52811      0t0  TCP *:http-alt (LISTEN)
    ```

## Tester

### Tester la connectivité

```bash title="Commande"
ping -c <N> <hôte>   # -c : nombre de paquets envoyés
traceroute <hôte>    # le chemin, saut par saut
```

```bash title="Exemple"
ping -c 2 1.1.1.1
```

??? example "Sortie"
    ```text
    64 bytes from 1.1.1.1: icmp_seq=1 ttl=57 time=11.8 ms
    64 bytes from 1.1.1.1: icmp_seq=2 ttl=57 time=12.1 ms
    --- 1.1.1.1 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    ```

```bash title="Exemple 2"
traceroute example.com
```

### Résoudre un nom

```bash title="Commande"
dig +short <nom>       # réponse du DNS seulement
getent hosts <nom>     # /etc/hosts puis DNS, comme les applications
```

```bash title="Exemple"
dig +short example.com
```

??? example "Sortie"
    ```text
    93.184.215.14
    ```

```bash title="Exemple 2"
getent hosts intranet.local
```

Ensuite : [ajouter une IP dans /etc/hosts](../administration/reseau.md#ajouter-une-ip-dans-etchosts)
{ .kw-cs-meta }

### Tester un port distant

```bash title="Commande"
nc -zv <hôte> <port>   # -z : test seulement, -v : affiche le résultat
```

```bash title="Exemple"
nc -zv 192.168.1.10 22
```

??? example "Sortie"
    ```text
    Connection to 192.168.1.10 22 port [tcp/ssh] succeeded!
    ```

### Interroger un service web

```bash title="Commande"
curl -I <url>   # -I : en-têtes seulement, -s : silencieux, -L : suit les redirections
```

```bash title="Exemple"
curl -sI https://example.com | head -3
```

??? example "Sortie"
    ```text
    HTTP/2 200
    content-type: text/html
    content-length: 1256
    ```

```bash title="Exemple 2"
curl -s -o /dev/null -w '%{http_code} %{time_total}s\n' https://example.com   # code et temps de réponse
```

## Capturer

### Capturer du trafic

```bash title="Commande"
sudo tcpdump -i <interface> -n <filtre>   # -n : pas de résolution de noms, -w fichier : enregistrer
```

```bash title="Exemple"
sudo tcpdump -i eth0 -n -c 2 host 192.168.1.10 and port 443
```

??? example "Sortie"
    ```text
    09:41:02.118 IP 192.168.1.50.41870 > 192.168.1.10.443: Flags [S], seq 3120558417, win 64240, length 0
    09:41:02.119 IP 192.168.1.10.443 > 192.168.1.50.41870: Flags [S.], seq 811203, ack 3120558418, win 65160, length 0
    ```

```bash title="Exemple 2"
sudo tcpdump -i eth0 -nn -w capture.pcap   # enregistrer pour l'ouvrir dans Wireshark
```

!!! warning "Attention"
    Une capture peut contenir des identifiants et des données personnelles : la stocker comme une donnée sensible.

## Vue d'ensemble

| Besoin | Linux | Équivalent Windows |
|---|---|---|
| Adresses IP | `ip -br a` | `Get-NetIPConfiguration` |
| Routes, passerelle | `ip route` | `Get-NetRoute` |
| Voisins (ARP) | `ip neigh` | `arp -a` |
| Ports en écoute | `ss -tulpn` | `Get-NetTCPConnection -State Listen` |
| Connexions établies | `ss -tnp state established` | `Get-NetTCPConnection -State Established` |
| Processus d'un port | `lsof -i :<port>` | `OwningProcess` de `Get-NetTCPConnection` |
| Connectivité | `ping -c` · `traceroute` | `Test-Connection` · `tracert` |
| Résolution de nom | `dig +short` · `getent hosts` | `Resolve-DnsName` |
| Port distant | `nc -zv <hôte> <port>` | `Test-NetConnection -Port` |
| En-têtes HTTP | `curl -I` | `Invoke-WebRequest -Method Head` |
| Capture | `tcpdump -i <interface> -w <fichier>` | `pktmon`, Wireshark |
