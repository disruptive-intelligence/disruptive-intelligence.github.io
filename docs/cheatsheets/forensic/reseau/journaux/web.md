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

Format texte Zeek : champs séparés par des **tabulations**, précédés de métadonnées `#separator`, `#fields`, `#types` (un export JSON se traite autrement). `zeek-cut` choisit les champs **par nom** : c'est le plus sûr, l'ordre des colonnes change selon la version.

### Repérer les champs d'un `http.log`

```bash title="Commande"
grep -m1 '^#fields' <http.log>                                   # noms des champs, dans l'ordre
zeek-cut <champ> <champ>… < <http.log>                           # extraire par nom, sans les métadonnées
```

```bash title="Exemple"
zeek-cut ts id.orig_h method uri status_code < http.log | head -n 20 | column -t -s $'\t'   # première vue, alignée
```

| Champ | Sens | Position (Zeek actuel) | Position (ancien Bro de l'exercice) |
|---|---|---|---|
| `ts` | Horodatage Unix | `$1` | `$1` |
| `id.orig_h` · `id.orig_p` | IP et port du client | `$3` · `$4` | `$3` · `$4` |
| `id.resp_h` · `id.resp_p` | IP et port du serveur | `$5` · `$6` | `$5` · `$6` |
| `method` | Méthode HTTP | `$8` | `$8` |
| `uri` | Ressource demandée | `$10` | `$10` |
| `user_agent` | Client HTTP déclaré | `$13` | `$12` |
| `status_code` | Code de réponse | `$17` | `$15` |

Zeek a ajouté `version` et `origin` avant `status_code` : les positions ne valent que pour **ton** fichier, d'où `#fields` ou `zeek-cut`.

??? example kw-cs-cas "Zeek : vérifier le format et les positions avant d'utiliser `$N`"
    ```bash
    head -n 8 http.log                                                                          # métadonnées puis premières requêtes
    awk -F '\t' '/^#fields/ {for (i=2; i<=NF; i++) printf "$%d %s\n", i-1, $i; exit}' http.log  # numéro de chaque nom
    awk -F '\t' '!/^#/ {for (i=1; i<=NF; i++) printf "$%d = %s\n", i, $i; exit}' http.log       # valeurs de la première requête
    grep -m1 -v '^#' http.log | tr '\t' '\n' | nl -ba                                           # idem, champs vides numérotés
    awk -F '\t' 'BEGIN {OFS="\t"} !/^#/ {print $3, $8, $10, $15}' http.log | head -n 20 | column -t -s $'\t'   # sans zeek-cut (positions Bro)
    ```
    La première ligne est `#separator`, pas une requête. Même méthode sur d'autres formats : [Linux › Repérer les champs d'un fichier](../../../linux/fondamentaux/texte-filtres.md#reperer-les-champs-dun-fichier)

### Mesurer l'activité et les réponses

```bash title="Commande"
zeek-cut <champ> < <http.log> | sort | uniq -c | sort -rn        # répartition d'un champ, la plus fréquente en tête
```

```bash title="Exemple"
zeek-cut id.orig_h < http.log | sort | uniq -c | sort -rn | head  # IP sources les plus actives
```

```bash title="Exemple 2"
zeek-cut method < http.log | sort | uniq -c | sort -rn            # méthodes
zeek-cut status_code < http.log | sort | uniq -c | sort -rn       # codes HTTP
```

| Code | Sens courant | À examiner |
|---|---|---|
| `200` | Réponse OK | URI accessible ; **ne prouve pas une compromission** |
| `301` / `302` | Redirection | Destination suivante |
| `401` | Authentification requise | Échecs répétés |
| `403` | Accès refusé | Ressources interdites sollicitées |
| `404` | Ressource introuvable | URI différentes et cadence des essais |
| `500` | Erreur serveur | Requête associée et réponse applicative |

??? example kw-cs-cas "Sans `zeek-cut` : les mêmes comptages avec `cut`"
    ```bash
    grep -v '^#' http.log | cut -f3  | sort | uniq -c | sort -rn | head  # IP sources
    grep -v '^#' http.log | cut -f8  | sort | uniq -c | sort -rn         # méthodes
    grep -v '^#' http.log | cut -f15 | sort | uniq -c | sort -rn         # codes HTTP (position Bro ; 17 dans Zeek actuel)
    ```
    Le `grep -v '^#'` évite de compter `#fields`, `#types`… comme des requêtes.

### Examiner les URI accessibles et les outils déclarés

```bash title="Commande"
zeek-cut id.orig_h method uri user_agent status_code < <http.log> | awk -F '\t' '<condition>'   # $1 IP, $2 méthode, $3 URI, $4 User-Agent, $5 code
```

```bash title="Exemple"
zeek-cut id.orig_h method uri status_code < http.log |
  awk -F '\t' '$4 == 200 {print $1, $2, $3, $4}'                  # réponses 200 : client et ressource
```

```bash title="Exemple 2"
zeek-cut id.orig_h method uri user_agent status_code < http.log |
  awk -F '\t' 'tolower($4) ~ /(nmap|nikto|sqlmap|gobuster|dirbuster)/ {print}'   # User-Agent d'outil connu
```

`grep -iE 'nmap|nikto|sqlmap|gobuster|dirbuster' http.log` va plus vite mais cherche sur toute la ligne (URI comprise). Un User-Agent est déclaratif : il peut être falsifié.

??? example kw-cs-cas "Requêtes `HEAD` vers des fichiers `.nsf` : reconnaissance automatisée ?"
    ```bash
    zeek-cut id.orig_h method uri user_agent status_code < http.log |
      awk -F '\t' '$2 == "HEAD" && $3 ~ /[.]nsf([?]|$)/ {print}'
    ```
    Beaucoup d'URI `.nsf` en `HEAD`, User-Agent « Nmap Scripting Engine », surtout des `404` : reconnaissance automatisée probable. Croiser IP, horaires, diversité des URI et autres journaux avant de conclure.

**Parcours court SOC** : 1. classer les IP sources ; 2. compter méthodes et codes ; 3. regarder les URI des `200` et des `404` ; 4. examiner User-Agent et chronologie ; 5. recouper avec proxy, pare-feu et serveur. Commandes en détail : [`awk`](../../../linux/commandes/awk.md), [`cut`](../../../linux/commandes/cut.md), [`grep`](../../../linux/commandes/grep.md), [`sort`](../../../linux/commandes/sort.md), [`uniq`](../../../linux/commandes/uniq.md), [`column`](../../../linux/commandes/column.md).

Référence du format : [Zeek, Log Formats and Inspection](https://docs.zeek.org/en/current/log-formats.html) et [champs du journal HTTP](https://docs.zeek.org/en/current/reference/logs/http.html).
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

| Champ Zeek `http.log` | `zeek-cut` | À regarder |
|---|---|---|
| IP source | `id.orig_h` | IP la plus active |
| Méthode | `method` | `HEAD` en rafale, `PUT`, `DELETE` |
| URI | `uri` | Beaucoup d'URI différentes en `404` = énumération |
| User-Agent | `user_agent` | Outils (`Nmap Scripting Engine`, `sqlmap`, `nikto`) |
| Code | `status_code` | `200` sur une ressource sensible, `401` répétés |
