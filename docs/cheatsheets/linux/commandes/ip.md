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
