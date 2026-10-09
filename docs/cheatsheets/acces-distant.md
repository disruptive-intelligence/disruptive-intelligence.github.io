---
title: "Accès distant — SSH, RDP et VNC"
---
# Accès distant — SSH, RDP et VNC

Pour ouvrir un terminal, choisis **SSH**. Pour un bureau graphique, choisis **RDP** si la machine cible le propose, ou **VNC** si elle héberge un serveur VNC. Remplace les noms de machine, d'utilisateur et les ports par ceux de ton environnement.

| Besoin | Depuis | Commande rapide |
|---|---|---|
| Terminal distant | Linux, macOS ou Windows avec OpenSSH | `ssh utilisateur@serveur.example.net` |
| Bureau RDP | Windows | `mstsc /v:serveur.example.net` |
| Bureau RDP | Linux avec FreeRDP | `xfreerdp3 /v:serveur.example.net /u:utilisateur` |
| Bureau VNC | Linux avec TigerVNC | `vncviewer serveur.example.net:1` |

## SSH — terminal distant

```bash title="Connexion"
ssh utilisateur@serveur.example.net
ssh -p 2222 utilisateur@serveur.example.net       # port SSH non standard
ssh -i ~/.ssh/cle_ed25519 utilisateur@serveur.example.net  # clé privée
ssh -J rebond.example.net utilisateur@interne.example.net   # via un bastion
```

Ces commandes fonctionnent aussi dans PowerShell avec le client OpenSSH installé ; adapte le chemin de la clé (`$HOME\.ssh\cle_ed25519`). Au premier accès, vérifie l'empreinte de la clé du serveur avant de l'accepter.

## RDP — bureau graphique

Sur **Windows**, `mstsc` est le client intégré :

```bat title="Invite de commandes ou PowerShell"
mstsc /v:serveur.example.net
mstsc /v:serveur.example.net:3390
```

La seconde ligne utilise un port RDP non standard (`3390`).

Sur **Linux**, FreeRDP fournit le client `xfreerdp3` (ou `xfreerdp` selon la version installée) :

```bash title="FreeRDP"
xfreerdp3 /v:serveur.example.net /u:utilisateur /dynamic-resolution
xfreerdp3 /v:serveur.example.net /u:'DOMAINE\utilisateur' /dynamic-resolution
```

Sans `/p:`, le client demande le mot de passe sans le placer dans l'historique du shell. Vérifie le certificat du serveur lors de la première connexion ; n'utilise pas `/cert:ignore` par réflexe.

**xrdp est le serveur RDP pour Linux**, pas le client. Sur une machine Debian ou Ubuntu avec un environnement graphique :

```bash title="Sur la machine Linux cible"
sudo apt install xrdp
sudo systemctl enable --now xrdp
sudo systemctl status xrdp
```

Le client `mstsc` ou `xfreerdp3` se connecte ensuite à cette machine. Le service écoute normalement sur `3389/tcp` ; limite son accès au réseau prévu (VPN ou bastion, par exemple).

## VNC — bureau graphique

Avec **TigerVNC**, `:1` désigne l'affichage VNC 1, généralement sur le port `5901` :

```bash title="Client VNC"
vncviewer serveur.example.net:1       # affichage 1
vncviewer serveur.example.net::5901    # même serveur, port explicite
```

Si le serveur VNC est accessible par SSH, fais passer VNC dans un tunnel et ouvre **deux terminaux** :

```bash title="Terminal 1 — garder ouvert"
ssh -N -L 5901:localhost:5901 utilisateur@serveur.example.net
```

```bash title="Terminal 2 — sur ton poste"
vncviewer localhost::5901
```

Ici, le port VNC `5901` doit être celui du serveur cible. Si ton poste utilise déjà ce port, remplace seulement le **premier** `5901` du tunnel par un port local libre et utilise ce même port dans `vncviewer localhost::<port-local>`.

Pour approfondir : [SSH dans la Bibliothèque](../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/02-chapitre-18-ssh-se-connecter-a-distance.md) · [RDP et ses journaux](../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md).

Références des commandes : [OpenSSH](https://man.openbsd.org/ssh.1), [Microsoft `mstsc`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc), [FreeRDP](https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface), [xrdp](https://github.com/neutrinolabs/xrdp), [TigerVNC `vncviewer`](https://tigervnc.org/doc/vncviewer.html).
