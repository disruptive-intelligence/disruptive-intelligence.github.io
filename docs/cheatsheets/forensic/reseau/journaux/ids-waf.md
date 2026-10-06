---
title: "IDS / IPS et WAF"
---

# IDS / IPS et WAF

Les alertes des équipements qui reconnaissent des attaques : signatures IDS / IPS sur le réseau, règles WAF devant les applications web. Une alerte dit qu'une attaque a été **tentée** ; il faut ensuite vérifier si elle a réussi.

Les incontournables : `grep` · `sed -n 's/…/…/p'` · `sort | uniq -c` · `awk`
{ .kw-cs-top }

## IDS / IPS

### Compter les alertes par signature et par source

```bash title="Commande"
sed -n 's/.*attack="\([^"]*\)".*/\1/p' <journal> | sort | uniq -c | sort -rn | head                         # signatures les plus déclenchées
sed -n 's/.*srcip=\([0-9.]*\).*attack="\([^"]*\)".*/\1 \2/p' <journal> | sort | uniq -c | sort -rn | head   # source et signature
```

```bash title="Exemple"
grep 'severity="high"\|severity="critical"' ips.log | sed -n 's/.*srcip=\([0-9.]*\).*dstip=\([0-9.]*\).*action="\([^"]*\)".*attack="\([^"]*\)".*/\1 → \2 \3 \4/p' | sort | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
         14 203.0.113.12 → 192.168.1.10 detected DNS.Server.Label.Buffer.Overflow
          6 203.0.113.12 → 192.168.1.10 dropped DNS.Server.Label.Buffer.Overflow
          2 198.51.100.7 → 192.168.1.15 detected HTTP.URI.SQL.Injection
    ```

`detected` : l'IDS a vu passer l'attaque, elle a atteint la cible. `dropped` / `blocked` : l'IPS l'a arrêtée. Dans les deux cas, vérifier que le service ciblé existe sur la cible, qu'il est vulnérable, et ce que montrent ensuite l'EDR et le pare-feu.

Pour comprendre : [IDS / IPS : champs importants, action, détection ≠ exploitation réussie](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/05-ids-ips.md)
{ .kw-cs-meta }

## WAF

### Compter les attaques web par type et par source

```bash title="Commande"
sed -n 's/.*sub_type="\([^"]*\)".*/\1/p' <journal> | sort | uniq -c | sort -rn             # types d'attaque (SQL Injection, XSS…)
sed -n 's/.*src=\([0-9.]*\).*sub_type="\([^"]*\)".*/\1 \2/p' <journal> | sort | uniq -c | sort -rn | head   # source et type
```

```bash title="Exemple"
sed -n 's/.*src=\([0-9.]*\).*http_host="\([^"]*\)".*sub_type="\([^"]*\)".*action=\([A-Za-z]*\).*/\1 \2 \3 \4/p' waf.log | sort | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
         38 203.0.113.45 app.example.com SQL Injection Alert
          9 203.0.113.45 app.example.com Directory Traversal Alert
          3 198.51.100.7 app.example.com XSS Block
    ```

Une alerte en mode `Alert` (ou `Detect`) laisse passer la requête jusqu'au serveur : la retrouver dans les logs web, regarder le code de statut et la taille de la réponse.

Pour comprendre : [WAF : champs principaux, analyse d'une alerte SQL Injection](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/06-waf.md)
{ .kw-cs-meta }

### Retrouver dans les logs web ce que le WAF a laissé passer

```bash title="Commande"
grep '^<IP_source> ' <access.log> | awk '{print $4, $9, $10, $7}'   # date, code, taille, URI des requêtes de l'attaquant
```

```bash title="Exemple"
grep '^203.0.113.45 ' /var/log/nginx/access.log | grep -Ei 'union|select|%27' | awk '{print $4, $9, $10, $7}' | head -3
```

??? example "Sortie"
    ```text
    [06/Oct/2026:02:31:07 200 486 /?id=1%27%20UNION%20SELECT%20user(),2--
    [06/Oct/2026:02:31:09 200 214 /?id=2
    [06/Oct/2026:02:31:12 500 0 /?id=1%27
    ```

La même page renvoie 486 octets avec l'injection et 214 sans : l'application a probablement renvoyé des données supplémentaires. C'est la taille, plus que le code `200`, qui oriente.

Pour comprendre : [WAF : corrélation avec les logs web server](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/06-waf.md) · [Logs web](web.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Champ IDS / IPS | Signification | À regarder |
|---|---|---|
| `attack` / `attackid` | Signature déclenchée | Type d'attaque, CVE associée |
| `severity` | Gravité donnée par la signature | Ne suffit pas à écarter un faux positif |
| `action` | `detected` (IDS) ou `dropped` / `blocked` (IPS) | `detected` = l'attaque a atteint la cible |
| `direction` | `incoming` / `outgoing` | `outgoing` depuis un poste interne = poste compromis possible |
| `srcip` / `dstip` / `dstport` | Source, cible, service | Le service visé tourne-t-il sur la cible ? |

| Champ WAF | Signification | À regarder |
|---|---|---|
| `src` | IP de l'attaquant | Réputation, autres alertes |
| `http_host` / URL | Application visée | Application réellement vulnérable ? |
| `http_method` | Méthode HTTP | `PUT`, `DELETE`, `TRACE` inattendus |
| `sub_type` | Type d'attaque | SQL Injection, XSS, Directory Traversal, Command Injection |
| `signature_id` | Règle du WAF | Faux positif connu ? |
| `action` | `Alert` / blocage | `Alert` = la requête est arrivée au serveur |

| Question | Où chercher la réponse |
|---|---|
| L'attaque a-t-elle atteint la cible ? | `action` de l'IDS / IPS ou du WAF |
| A-t-elle réussi ? | Logs web (code, taille), EDR, logs applicatifs |
| La cible est-elle vulnérable ? | Version du service, inventaire, scan de vulnérabilités |
| Qui d'autre la source a-t-elle visé ? | Pare-feu, NetFlow |
