---
title: "Logs web"
---

# Logs web

Les journaux d'accès d'un serveur web (Apache, Nginx, IIS) et le `http.log` de Zeek : qui a fait quelle requête, vers quelle ressource, avec quel résultat. Les commandes pour le format « combined » et celles pour Zeek ne partagent pas les mêmes positions de champs.

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

## Zeek / Bro : analyser `http.log`

Le format texte Zeek standard est délimité par des **tabulations** et commence par des métadonnées `#separator`, `#fields` et `#types`. Une exportation JSON demande un traitement différent. Vérifie les champs de **ton** fichier avant d'employer des numéros de colonnes : le schéma peut varier.

```bash title="Vérifier le format et les positions"
head -n 8 http.log
awk -F '\t' '/^#fields/ {for (i=2; i<=NF; i++) printf "$%d %s\n", i-1, $i; exit}' http.log
```

Dans un `http.log` dont `#fields` confirme l'ordre ci-dessous :

| Position | Champ Zeek | Sens |
|---|---|---|
| `$1` | `ts` | Horodatage Unix |
| `$3` · `$4` | `id.orig_h` · `id.orig_p` | IP et port du client |
| `$5` · `$6` | `id.resp_h` · `id.resp_p` | IP et port du serveur |
| `$8` | `method` | Méthode HTTP |
| `$10` | `uri` | Ressource demandée |
| `$12` | `user_agent` | Client HTTP déclaré |
| `$15` | `status_code` | Code de réponse |

`zeek-cut` lit l'en-tête et sélectionne les **noms** de champs ; c'est le choix le plus sûr pour un journal Zeek standard. Pour afficher les requêtes utiles à l'enquête :

```bash title="Client, méthode, URI, code : première vue"
zeek-cut ts id.orig_h method uri status_code < http.log | head -n 20
zeek-cut ts id.orig_h method uri status_code < http.log | head -n 20 | column -t -s $'\t'
```

Si `zeek-cut` n'est pas installé **et que les positions ci-dessus sont confirmées**, écarte les lignes de métadonnées :

```bash title="Variante awk à positions vérifiées"
awk -F '\t' 'BEGIN {OFS="\t"} !/^#/ {print $3, $8, $10, $15}' http.log | head -n 20 | column -t -s $'\t'
```

### Mesurer l'activité et les réponses

```bash title="IP sources les plus actives"
zeek-cut id.orig_h < http.log | sort | uniq -c | sort -rn | head
```

```bash title="Méthodes et codes HTTP par fréquence"
zeek-cut method < http.log | sort | uniq -c | sort -rn
zeek-cut status_code < http.log | sort | uniq -c | sort -rn
```

Avec les positions vérifiées, `cut` donne les mêmes comptages. Le premier `grep` évite de compter `#fields`, `#types` et les autres métadonnées comme des événements :

```bash title="Variantes cut pour un TSV à colonnes confirmées"
grep -v '^#' http.log | cut -f3  | sort | uniq -c | sort -rn | head  # IP sources
grep -v '^#' http.log | cut -f8  | sort | uniq -c | sort -rn         # méthodes
grep -v '^#' http.log | cut -f15 | sort | uniq -c | sort -rn         # codes HTTP
```

| Code | Sens courant | À examiner |
|---|---|---|
| `200` | Réponse OK | URI accessible ; **ne prouve pas une compromission** |
| `301` / `302` | Redirection | Destination suivante |
| `401` | Authentification requise | Échecs répétés |
| `403` | Accès refusé | Ressources interdites sollicitées |
| `404` | Ressource introuvable | URI différentes et cadence des essais |
| `500` | Erreur serveur | Requête associée et réponse applicative |

### Examiner les URI accessibles et les outils déclarés

```bash title="Réponses 200 : conserver le client et la ressource"
zeek-cut id.orig_h method uri status_code < http.log |
  awk -F '\t' '$4 == 200 {print $1, $2, $3, $4}'
```

```bash title="User-Agents contenant un nom d'outil"
zeek-cut id.orig_h method uri user_agent status_code < http.log |
  awk -F '\t' 'tolower($4) ~ /(nmap|nikto|sqlmap|gobuster|dirbuster)/ {print}'
```

`grep -iE 'nmap|nikto|sqlmap|gobuster|dirbuster' http.log` sert de recherche rapide sur toute la ligne, mais peut aussi trouver une correspondance dans l'URI ou un autre champ. Un User-Agent est déclaratif et peut être falsifié.

```bash title="Examiner des requêtes HEAD vers des fichiers .nsf"
zeek-cut id.orig_h method uri user_agent status_code < http.log |
  awk -F '\t' '$2 == "HEAD" && $3 ~ /[.]nsf([?]|$)/ {print}'
```

Des requêtes `HEAD` vers de nombreuses URI `.nsf`, avec un User-Agent « Nmap Scripting Engine » et des `404`, suggèrent une reconnaissance automatisée. Croise l'IP, les horaires, la diversité des URI et les autres journaux avant de conclure. Un nombre élevé de `404` peut signaler une énumération ; un `200` indique seulement que le serveur a répondu avec ce code.

**Parcours court SOC** : 1. classer les IP sources ; 2. compter méthodes et codes ; 3. regarder les URI associées aux `200` et aux `404` ; 4. examiner le User-Agent et la chronologie ; 5. recouper avec les journaux proxy, pare-feu et serveur. Pour des commandes génériques, voir [`awk`](../../../linux/commandes/awk.md), [`cut`](../../../linux/commandes/cut.md), [`grep`](../../../linux/commandes/grep.md), [`sort`](../../../linux/commandes/sort.md), [`uniq`](../../../linux/commandes/uniq.md) et [`column`](../../../linux/commandes/column.md).

Référence du format : [Zeek, Log Formats and Inspection](https://docs.zeek.org/en/current/log-formats.html) et [champs du journal HTTP](https://docs.zeek.org/en/current/reference/logs/http.html).

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
