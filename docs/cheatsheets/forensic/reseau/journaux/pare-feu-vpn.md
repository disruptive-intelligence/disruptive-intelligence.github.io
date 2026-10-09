---
title: "Pare-feu, NetFlow et VPN"
---

# Pare-feu, NetFlow et VPN

Qui a parlé à qui, sur quel port, avec quel volume ; qui s'est connecté à distance et ce qu'il a fait ensuite. Les exemples portent sur des journaux au format `clé=valeur` (FortiGate) ; les champs (`srcip`, `dstip`, `dstport`, `action`, `sentbyte`, `remip`, `user`) ont un équivalent chez tous les constructeurs.

Les incontournables : `grep` · `sed -n 's/…/…/p'` · `sort | uniq -c` · `awk` · `nfdump`
{ .kw-cs-top }

## Pare-feu

### Filtrer un journal de pare-feu par IP, port ou action

```bash title="Commande"
grep 'srcip=<IP>' <journal> | grep 'action="deny"'   # refus pour une source ; action : accept, deny, drop, close, client-rst, server-rst
grep 'dstport=<port>' <journal>                       # tout ce qui vise un port
```

```bash title="Exemple"
grep 'dstip=203.0.113.80' fw.log | grep 'action="accept"' | head -2
```

??? example "Sortie"
    ```text
    date=2026-10-06 time=02:14:51 srcip=192.168.1.31 srcport=50495 dstip=203.0.113.80 dstport=443 proto=6 action="accept" service="HTTPS" duration=72 sentbyte=2518 rcvdbyte=49503
    date=2026-10-06 time=02:19:51 srcip=192.168.1.31 srcport=50511 dstip=203.0.113.80 dstport=443 proto=6 action="accept" service="HTTPS" duration=70 sentbyte=2490 rcvdbyte=48820
    ```

Une IP d'IOC qui apparaît en `accept` : la connexion a eu lieu. Remonter ensuite au poste (`srcip`, et la table NAT si l'adresse a été traduite), puis à l'EDR pour le processus.

Pour comprendre : [Pare-feu : champs des traffic logs, action, NAT](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/02-pare-feu.md)
{ .kw-cs-meta }

### Repérer un scan de ports

Pour extraire la liste et le nombre de ports visés par une source, ou limiter le calcul aux connexions autorisées, voir [Texte et filtres — ports distincts et actions](../../../linux/fondamentaux/texte-filtres.md#extraire-et-compter-des-ports-de-destination-distincts).

```bash title="Commande"
sed -n 's/.*srcip=\([0-9.]*\).*dstport=\([0-9]*\).*/\1 \2/p' <journal> | sort -u | awk '{print $1}' | uniq -c | sort -rn | head   # ports distincts par source (scan vertical)
sed -n 's/.*srcip=\([0-9.]*\).*dstip=\([0-9.]*\).*dstport=<port>.*/\1 \2/p' <journal> | sort -u | awk '{print $1}' | uniq -c | sort -rn | head   # hôtes distincts sur un port (scan horizontal)
```

```bash title="Exemple"
sed -n 's/.*srcip=\([0-9.]*\).*dstip=\([0-9.]*\).*dstport=445.*/\1 \2/p' fw.log | sort -u | awk '{print $1}' | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
        212 192.168.1.44
          3 192.168.1.10
          2 192.168.1.11
    ```

Un poste qui touche le port 445 de 212 machines en quelques minutes fait de la reconnaissance SMB, ou se propage. Les `sed` supposent l'ordre des champs FortiGate (`srcip` avant `dstip` avant `dstport`) : l'adapter pour un autre équipement.

Pour comprendre : [Pare-feu : Vertical Scan, Horizontal Scan, Lateral Movement](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/02-pare-feu.md)
{ .kw-cs-meta }

### Mesurer le volume envoyé vers chaque destination

```bash title="Commande"
sed -n 's/.*dstip=\([0-9.]*\).*sentbyte=\([0-9]*\).*/\1 \2/p' <journal> | awk '{s[$1]+=$2} END {for (i in s) print s[i], i}' | sort -rn | head   # octets envoyés par destination
```

```bash title="Exemple"
grep 'srcip=192.168.1.31' fw.log | sed -n 's/.*dstip=\([0-9.]*\).*sentbyte=\([0-9]*\).*/\1 \2/p' | awk '{s[$1]+=$2} END {for (i in s) print s[i], i}' | sort -rn | head -3
```

??? example "Sortie"
    ```text
    8642110233 203.0.113.80
       4120385 192.168.1.10
        512044 198.51.100.7
    ```

8 Go envoyés vers une destination rare, depuis un poste qui n'a pas de raison de le faire : piste d'exfiltration. Croiser avec le DNS (quel domaine) et le proxy (quelle URL).

Pour comprendre : [Pare-feu : Exfiltration](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/02-pare-feu.md)
{ .kw-cs-meta }

## NetFlow

### Voir les plus gros flux et les ports contactés

```bash title="Commande"
nfdump -R <dossier_des_flux> -s srcip/bytes -n 10                 # sources qui envoient le plus d'octets
nfdump -R <dossier_des_flux> 'src ip <IP>' -s dstport -n 20         # ports contactés par une source
```

```bash title="Exemple"
nfdump -R /var/cache/nfdump 'src ip 192.168.1.44 and dst port 445' -s dstip -n 5
```

??? example "Sortie"
    ```text
    Top 5 Dst IP Addr ordered by flows:
    Date first seen          Duration Proto      Dst IP Addr    Flows(%)     Packets(%)       Bytes(%)
    2026-10-06 02:31:07.120     0.004 TCP       192.168.1.10    1( 0.5)        2( 0.5)      104( 0.5)
    2026-10-06 02:31:07.131     0.003 TCP       192.168.1.11    1( 0.5)        2( 0.5)      104( 0.5)
    …
    ```

NetFlow ne donne pas le contenu, mais il est conservé longtemps : idéal pour la périodicité d'un beacon (mêmes source, destination et taille toutes les N minutes) et pour les premières connexions jamais vues.

Pour comprendre : [NetFlow : attributs d'un flow, port scanning, C2, limites](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/01-netflow.md)
{ .kw-cs-meta }

## VPN

### Retracer les connexions VPN d'un utilisateur

```bash title="Commande"
grep 'subtype="vpn"' <journal> | grep 'user="<utilisateur>"'                                          # tous ses événements VPN
sed -n 's/.*action="\([^"]*\)".*remip=\([0-9.]*\).*user="\([^"]*\)".*/\3 \2 \1/p' <journal> | sort | uniq -c   # utilisateur, IP publique, action
```

```bash title="Exemple"
grep 'subtype="vpn"' vpn.log | sed -n 's/.*action="\([^"]*\)".*remip=\([0-9.]*\).*user="\([^"]*\)".*/\3 \2 \1/p' | sort | uniq -c | sort -rn | head -4
```

??? example "Sortie"
    ```text
         41 jdoe 203.0.113.9 ssl-login-fail
          1 jdoe 203.0.113.9 tunnel-up
          6 asmith 192.0.2.40 tunnel-up
          3 mlopez 192.0.2.41 tunnel-up
    ```

41 échecs puis un `tunnel-up` depuis la même IP : brute force réussi. Ensuite, chercher la `tunnelip` attribuée à cette session, puis tout le trafic de cette adresse dans le pare-feu (`srcip=<tunnelip>`).

```bash title="Exemple 2"
sed -n 's/.*remip=\([0-9.]*\).*user="\([^"]*\)".*/\1 \2/p' vpn.log | sort -u | awk '{print $1}' | uniq -c | sort -rn | head -3   # comptes distincts par IP : password spraying
```

Pour comprendre : [VPN : remip et tunnelip, brute force, connexion VPN suspecte](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/03-vpn.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Champ (FortiGate) | Signification | À regarder |
|---|---|---|
| `srcip` / `srcport` | Source | Poste interne, ou `tunnelip` d'un client VPN |
| `dstip` / `dstport` | Destination | IP d'IOC, port d'administration (22, 445, 3389, 5985) |
| `action` | `accept`, `deny`, `drop`, `close`, `client-rst`, `server-rst` | `accept` vers un IOC = la connexion a eu lieu |
| `policyid` | Règle appliquée | Règle trop large, règle modifiée |
| `sentbyte` / `rcvdbyte` | Octets envoyés / reçus | Volume sortant anormal = exfiltration |
| `duration` | Durée de la session | Sessions courtes et régulières = beacon |
| `remip` | IP publique du client VPN | Pays, réputation, plusieurs comptes depuis la même IP |
| `tunnelip` | IP interne attribuée au client VPN | À rechercher ensuite comme `srcip` dans le pare-feu |
| `user` | Compte VPN | Même compte depuis des pays éloignés en peu de temps |

| Scénario | Pattern |
|---|---|
| Scan vertical | Une source, beaucoup de ports sur une même cible |
| Scan horizontal | Une source, un même port sur beaucoup de cibles |
| Mouvement latéral | Nouveaux flux est-ouest vers 445, 3389, 5985 / 5986, 22 |
| Beacon C2 | Même source, même destination, intervalle régulier, petite taille constante |
| Exfiltration | Gros volume sortant vers une destination rare |
| Brute force VPN | Beaucoup d'échecs pour un compte, puis un succès |
