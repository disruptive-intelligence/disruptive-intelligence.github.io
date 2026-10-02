---
title: "ip"
commande: "ip"
---
# `ip`

Affiche et règle la configuration réseau : adresses, interfaces, routes, voisins. Remplace `ifconfig`, `route` et `arp`.

```bash title="Syntaxe"
ip [options] <objet> <action>   # objets : addr (a), link, route (r), neigh (n)
```

Pour comprendre : [Administration Linux, ch. 17](../../../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/01-chapitre-17-les-bases-du-reseau-linux.md)
{ .kw-cs-meta }

## Les options utiles

| Commande | Ce qu'elle fait |
|---|---|
| `ip a` · `ip -br a` | Adresses de toutes les interfaces · en forme courte |
| `ip link` · `ip -s link` | Interfaces (état, MAC) · avec compteurs de paquets et d'erreurs |
| `ip route` · `ip route get <IP>` | Table de routage · route utilisée pour joindre cette IP |
| `ip neigh` | Table ARP : voisins du réseau local et leur MAC |
| `-4` · `-6` · `-c` · `-j` | IPv4 · IPv6 · en couleur · en JSON |
| `ip addr add <IP>/<masque> dev <if>` · `del` | Ajouter · retirer une adresse |
| `ip link set <if> up` · `down` | Activer · couper une interface |
| `ip route add <réseau> via <passerelle>` · `replace default via` | Ajouter une route · changer la passerelle |

## Des commandes décodées

| Commande | Se lit |
|---|---|
| `ip -br a` | Une ligne par interface : nom, état, adresses |
| `ip route get 8.8.8.8` | Par quelle interface et quelle passerelle sort un paquet vers 8.8.8.8 |
| `ip -s link show eth0` | Paquets et erreurs reçus et envoyés sur eth0 |
| `ip -4 -o addr show | awk '{print $2, $4}'` | Interface et adresse IPv4, une par ligne |

## Pièges

- Ce que fait `ip` est **perdu au redémarrage** : NetworkManager (`nmcli`) ou netplan pour le rendre persistant.
- Couper l'interface par laquelle on est connecté en SSH, c'est perdre la main sur la machine.
- Correspondances : `ifconfig` → `ip a` · `route -n` → `ip route` · `arp -a` → `ip neigh`.

## Exemples

??? example kw-cs-more "Voir"
    ```bash
    ip -br a                    # adresses, en bref
    ip -br link                 # interfaces et MAC, en bref
    ip -4 a show eth0           # IPv4 d'une interface
    ip route                    # routes IPv4
    ip -6 route                 # routes IPv6
    ip neigh                    # voisins (table ARP)
    ip -s link show eth0        # compteurs de paquets et d'erreurs
    ```

??? example kw-cs-more "Modifier (jusqu'au redémarrage)"
    ```bash
    sudo ip addr add 192.168.1.51/24 dev eth0
    sudo ip addr del 192.168.1.51/24 dev eth0
    sudo ip link set eth1 up
    sudo ip route add 10.20.0.0/16 via 192.168.1.254   # une route vers un autre réseau
    sudo ip route replace default via 192.168.1.1      # changer la passerelle
    sudo ip neigh flush dev eth0                       # vider le cache ARP
    ```

??? example kw-cs-more "Diagnostiquer"
    ```bash
    ip route get 8.8.8.8                           # quelle sortie pour joindre 8.8.8.8
    ip -br a | grep -v DOWN                        # interfaces actives
    ip -j a | jq -r '.[].addr_info[].local'        # toutes les adresses, via JSON
    ip monitor                                     # changements réseau en direct
    ip netns list                                  # espaces de noms réseau (conteneurs)
    ```
