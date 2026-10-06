---
title: "Logs web"
---

# Logs web

Les journaux d'accès d'un serveur web (Apache, Nginx, IIS) : une ligne par requête. Qui a frappé, quelle URL, avec quel résultat.

Les incontournables : `awk` · `grep -E` · `sort | uniq -c` · `/var/log/apache2/access.log` · `/var/log/nginx/access.log`
{ .kw-cs-top }

## Lire un journal d'accès

### Repérer les IP qui envoient le plus de requêtes

```bash title="Commande"
awk '{print $1}' <access.log> | sort | uniq -c | sort -rn | head   # champ 1 du format « combined » : IP source
```

```bash title="Exemple"
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -5
```

??? example "Sortie"
    ```text
      18432 203.0.113.45
        612 192.168.1.20
        388 192.168.1.31
         97 198.51.100.7
         41 192.168.1.44
    ```

```bash title="Exemple 2"
grep '203.0.113.45' /var/log/nginx/access.log | awk '{print $9}' | sort | uniq -c | sort -rn   # codes de statut obtenus par cette IP
```

Une IP qui écrase toutes les autres, surtout avec beaucoup de `404`, signe souvent un scanner ou un brute force.

Pour comprendre : [Logs web : Top Requesting IPs, status codes](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/07-logs-web.md)
{ .kw-cs-meta }

### Voir les URL, les codes de statut et les User-Agents

```bash title="Commande"
awk '{print $7}' <access.log> | sort | uniq -c | sort -rn | head        # URI les plus demandées
awk '{print $9}' <access.log> | sort | uniq -c | sort -rn               # répartition des codes de statut
awk -F'"' '{print $6}' <access.log> | sort | uniq -c | sort -rn | head  # User-Agents
```

```bash title="Exemple"
awk -F'"' '{print $6}' /var/log/apache2/access.log | grep -Ei 'sqlmap|nikto|nmap|gobuster|ffuf|curl|python-requests' | sort | uniq -c
```

??? example "Sortie"
    ```text
       5120 sqlmap/1.7.2#stable (https://sqlmap.org)
         44 curl/7.88.1
    ```

Un User-Agent d'outil (`sqlmap`, `nikto`, `gobuster`…) se falsifie facilement : son absence ne prouve rien, sa présence est un bon indice.

Pour comprendre : [Logs web : User-Agent, Most Requested URLs](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/07-logs-web.md)
{ .kw-cs-meta }

## Repérer les attaques

### Chercher des injections et des traversées de répertoire

```bash title="Commande"
grep -Ei 'union.*select|select.*from|%27|or(%20|\+|\s)1=1|sleep\(' <access.log>   # SQL injection
grep -Ei '<script|%3Cscript|onerror=|javascript:' <access.log>                    # XSS
grep -Ei '\.\./|%2e%2e|/etc/passwd|win\.ini' <access.log>                          # traversée de répertoire
grep -Ei '(;|%3B|%7C).*(id|whoami|cat|wget|curl)|\$\(' <access.log>                 # injection de commande
```

```bash title="Exemple"
grep -Ei 'union.*select|select.*from|%27' /var/log/apache2/access.log | awk '{print $1, $9, $7}' | head -3
```

??? example "Sortie"
    ```text
    203.0.113.45 200 /?id=1%27%20UNION%20SELECT%20user(),2--
    203.0.113.45 500 /?id=1%27
    203.0.113.45 200 /?id=SELECT+*+FROM+users
    ```

Un `200` ne prouve pas que l'attaque a réussi (page d'erreur personnalisée, requête rejetée par l'application), et un `500` peut révéler qu'elle a touché la base. Comparer la **taille de la réponse** (champ 10) avec celle des requêtes normales vers la même page.

Pour comprendre : [Logs web : SQL Injection, XSS, Directory Traversal, Command Injection](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/07-logs-web.md)
{ .kw-cs-meta }

### Repérer un brute force sur une page de connexion

```bash title="Commande"
grep '"POST <url_de_connexion>' <access.log> | awk '{print $1}' | sort | uniq -c | sort -rn | head   # POST par IP
```

```bash title="Exemple"
grep '"POST /wp-login.php' /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -3
```

??? example "Sortie"
    ```text
       2304 203.0.113.45
         12 192.168.1.31
          3 192.168.1.20
    ```

```bash title="Exemple 2"
grep '"POST /wp-login.php' /var/log/nginx/access.log | grep '^203.0.113.45 ' | awk '{print substr($4,2,17)}' | uniq -c | head   # tentatives par minute
```

Le corps des POST (identifiants testés) n'est pas journalisé par défaut : on voit le nombre et le rythme des tentatives, pas les mots de passe.

Pour comprendre : [Logs web : Brute Force Web, corps POST / PUT](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/07-logs-web.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Serveur | Journal d'accès | Journal d'erreurs |
|---|---|---|
| Apache (Debian, Ubuntu) | `/var/log/apache2/access.log` | `/var/log/apache2/error.log` |
| Apache (RHEL, Fedora) | `/var/log/httpd/access_log` | `/var/log/httpd/error_log` |
| Nginx | `/var/log/nginx/access.log` | `/var/log/nginx/error.log` |
| IIS | `C:\inetpub\logs\LogFiles\W3SVC<n>\u_ex<AAMMJJ>.log` (format W3C) | Journaux Windows → System |

| Champ du format « combined » | `awk` | À regarder |
|---|---|---|
| IP source | `$1` | IP la plus active, réputation |
| Date | `$4` | Rafales, horaires inhabituels |
| Méthode | `$6` | `PUT`, `DELETE`, `TRACE` inattendus |
| URI | `$7` | `UNION SELECT`, `<script`, `../`, `;id` |
| Code de statut | `$9` | Beaucoup de `404` = énumération ; `500` = erreur provoquée |
| Taille de la réponse | `$10` | Taille anormale pour une même page = données renvoyées |
| User-Agent | `awk -F'"' '{print $6}'` | Outils (`sqlmap`, `nikto`, `curl`) |
