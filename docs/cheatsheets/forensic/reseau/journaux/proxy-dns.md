---
title: "Proxy et DNS"
---

# Proxy et DNS

Quelle URL un poste a demandée, et quel domaine il a résolu. Le proxy voit l'URL et l'utilisateur ; le DNS voit l'intention de joindre un domaine, même si la connexion n'a jamais eu lieu.

Les incontournables : `grep` · `sed -n 's/…/…/p'` · `zeek-cut` · `jq` · `Get-WinEvent`
{ .kw-cs-top }

## Proxy

### Lister les requêtes bloquées par le proxy

```bash title="Commande"
grep 'action="blocked"' <journal> | sed -n 's/.*srcip=\([0-9.]*\).*hostname="\([^"]*\)".*/\1 \2/p' | sort | uniq -c | sort -rn | head   # poste, domaine bloqué
```

```bash title="Exemple"
grep 'action="blocked"' proxy.log | sed -n 's/.*srcip=\([0-9.]*\).*hostname="\([^"]*\)".*/\1 \2/p' | sort | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
        288 192.168.1.31 update-check.example-cdn.xyz
         12 192.168.1.20 www.jeux-en-ligne.example
          4 192.168.1.44 paste.example.net
    ```

Un domaine bloqué ne clôt pas l'incident : un poste qui y revient sans cesse (288 fois) a probablement un programme qui essaie de joindre son serveur. Chercher le processus responsable dans l'EDR.

Pour comprendre : [Proxy : connexions vers des URL suspectes, domaine bloqué ≠ incident terminé](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/04-proxy.md)
{ .kw-cs-meta }

### Repérer les plus gros envois

```bash title="Commande"
sed -n 's/.*srcip=\([0-9.]*\).*hostname="\([^"]*\)".*sentbyte=\([0-9]*\).*/\3 \1 \2/p' <journal> | sort -rn | head   # octets envoyés, poste, domaine
```

```bash title="Exemple"
sed -n 's/.*srcip=\([0-9.]*\).*hostname="\([^"]*\)".*sentbyte=\([0-9]*\).*/\3 \1 \2/p' proxy.log | sort -rn | head -3
```

??? example "Sortie"
    ```text
    2147483648 192.168.1.44 upload.cloud-storage.example
       5242880 192.168.1.20 sharepoint.example.com
       1048576 192.168.1.31 api.example.org
    ```

Un envoi de 2 Go vers un service de stockage, hors des usages habituels du poste : vérifier la méthode (`POST`, `PUT`), l'utilisateur et l'heure. Sans inspection TLS, le proxy ne voit que le domaine, pas le chemin.

Pour comprendre : [Proxy : POST requests, exfiltration, HTTPS et limites de visibilité](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/04-proxy.md)
{ .kw-cs-meta }

## DNS

### Lister les domaines interrogés par un poste

```bash title="Commande"
zeek-cut ts id.orig_h query qtype_name rcode_name < dns.log | awk '$2=="<IP>"'   # journal DNS de Zeek
jq -r 'select(.source_ip=="<IP>") | .query' <journal.json> | sort | uniq -c | sort -rn   # journal JSON, un événement par ligne
```

```bash title="Exemple"
zeek-cut id.orig_h query < dns.log | awk '$1=="192.168.1.31" {print $2}' | sort | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
        412 update-check.example-cdn.xyz
         37 www.example.com
          9 login.example.org
    ```

Pour comprendre : [DNS : DNS Query Logs, Query Type](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/08-dns.md)
{ .kw-cs-meta }

### Repérer un tunneling DNS

```bash title="Commande"
zeek-cut query < dns.log | awk 'length($0) > 50' | sort | uniq -c | sort -rn | head        # noms anormalement longs
zeek-cut query < dns.log | awk -F. 'NF>2 {print $(NF-1)"."$NF}' | sort | uniq -c | sort -rn | head   # domaines parents qui reçoivent le plus de requêtes
```

```bash title="Exemple"
zeek-cut query < dns.log | grep '\.example-c2\.net$' | head -3
```

??? example "Sortie"
    ```text
    aGVsbG8xd29ybGQ.example-c2.net
    dGVzdGRhdGEyMzQ.example-c2.net
    c2VjcmV0ZmlsZTM.example-c2.net
    ```

Des sous-domaines longs, aléatoires, nombreux et réguliers sous un même domaine parent : données encodées dans les noms. Un nom long seul ne prouve rien (CDN, télémétrie, jetons de validation) : combiner longueur, entropie, fréquence et réputation du domaine.

Pour comprendre : [DNS : DNS Tunneling, Long Domains / Subdomains](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/08-dns.md)
{ .kw-cs-meta }

### Repérer un malware à DGA (rafales de NXDOMAIN)

```bash title="Commande"
zeek-cut id.orig_h rcode_name < dns.log | awk '$2=="NXDOMAIN" {print $1}' | sort | uniq -c | sort -rn | head   # NXDOMAIN par poste
```

```bash title="Exemple"
zeek-cut id.orig_h query rcode_name < dns.log | awk '$1=="192.168.1.44" && $3=="NXDOMAIN" {print $2}' | head -3
```

??? example "Sortie"
    ```text
    ajskd92.com
    pqow81.net
    mxz19.org
    ```

Beaucoup de domaines aléatoires inexistants depuis un même poste : le malware essaie des noms générés jusqu'à trouver son C2 actif.

Pour comprendre : [DNS : NXDOMAIN, DGA](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/08-dns.md)
{ .kw-cs-meta }

### Voir les modifications d'enregistrements sur un serveur DNS Windows

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-DNSServer/Audit'; Id=515,516}   # enregistrement créé, supprimé
```

```powershell title="Exemple"
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-DNSServer/Audit'; Id=516} -MaxEvents 3 | Select-Object TimeCreated, Id, Message | Format-List
```

??? example "Sortie"
    ```text
    TimeCreated : 06/10/2026 02:47:12
    Id          : 516
    Message     : A resource record of type 1, name deneme and RDATA 192.168.1.50 was deleted from scope Default of zone dc.local.
    ```

Un enregistrement modifié vers une IP inconnue redirige le trafic d'un nom légitime. Vérifier le compte qui a fait le changement.

Pour comprendre : [DNS : DNS Server Audit Events](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/08-dns.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Source | Où | Champs utiles |
|---|---|---|
| Proxy (FortiGate) | Journal du proxy ou du SIEM | `srcip`, `hostname`, `url`, `action` (`blocked`…), `sentbyte` / `rcvdbyte`, `profile`, catégorie |
| DNS (Zeek) | `dns.log` du capteur | `id.orig_h`, `query`, `qtype_name`, `rcode_name` |
| DNS (JSON) | Journal du résolveur ou du SIEM | `source_ip`, `query`, `qtype_name` |
| DNS Windows (requêtes) | Journal de débogage DNS, si activé | Poste, nom demandé, type |
| DNS Windows (modifications) | Journaux des applications et des services → Microsoft → Windows → DNS-Server → Audit | 515 enregistrement créé, 516 supprimé |
| BIND | Selon la section `logging` de `named.conf` (souvent `/var/log/querylog`) | Client, nom, type |

| Pattern | Ce qu'il évoque |
|---|---|
| Domaine bloqué demandé en boucle par un poste | Programme qui essaie de joindre son C2 |
| Gros envoi vers un service de stockage | Exfiltration possible |
| Sous-domaines longs et aléatoires sous un même parent | Tunneling DNS |
| Rafale de NXDOMAIN sur des noms aléatoires | Malware à DGA |
| Domaine d'IOC dans l'historique DNS | Postes à investiguer (retro-hunting) |
