# Conventions

## Variables

Toutes les commandes du wiki utilisent ces variables. Définis-les une fois
(voir [Checklist](checklist.md)), puis copie-colle les commandes sans rien modifier.

| Variable | Contenu | Exemple |
|---|---|---|
| `IP` | IP de la cible | `10.10.11.42` |
| `DOMAIN` | Domaine AD / vhost | `corp.htb` |
| `DC` | FQDN du contrôleur de domaine | `dc01.corp.htb` |
| `USR` | Utilisateur compromis | `svc_sql` |
| `PASS` | Mot de passe | `'P@ssw0rd!'` |
| `HASH` | Hash NT | `aad3b...` |
| `LHOST` | Ton IP (VPN) | `10.10.14.7` |
| `LPORT` | Ton port d'écoute | `4444` |

!!! warning "`USR`, pas `USER`"
    `$USER` est une variable système Linux (ton nom de session). L'écraser casse des outils silencieusement.

!!! warning "Toujours des guillemets"
    `"$PASS"` et non `$PASS` : sinon `!`, `$` ou les espaces cassent la commande.

## Linux / Windows

=== "Linux (bash)"

    ```bash
    export IP=10.10.11.42
    echo $IP
    ```

=== "Windows (PowerShell)"

    ```powershell
    $env:IP = "10.10.11.42"
    echo $env:IP
    ```

## Placeholders

Ce qui n'est pas une variable reste entre chevrons et doit être adapté à la main :
`<nom_share>`, `<wordlist>`.

## Structure d'une fiche service

`Quick checks` → `Énumération` → sections spécifiques → `Attaques courantes` →
`Outils` → `Pièges / Gotchas` → `Voir aussi`
