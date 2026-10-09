---
title: "Accès distant — SSH, RDP et VNC"
---
# Accès distant — SSH, RDP et VNC

Un terminal : **SSH**. Un bureau graphique : **RDP** si la cible le propose (Windows, ou Linux avec xrdp), **VNC** si elle héberge un serveur VNC.

Les incontournables : `ssh` · `ssh -J` · `mstsc /v:` · `xfreerdp3 /v:` · `vncviewer` · `ssh -L`
{ .kw-cs-top }

## SSH

### Ouvrir un terminal sur une machine distante

```bash title="Commande"
ssh <utilisateur>@<machine>                              # -p <port> si le port n'est pas 22
ssh -i <clé_privée> <utilisateur>@<machine>              # avec une clé
ssh -J <bastion> <utilisateur>@<machine_interne>         # en rebondissant par un bastion
```

```bash title="Exemple"
ssh -p 2222 -i ~/.ssh/cle_ed25519 m.laurent@srv-web01.meridian.local
```

```bash title="Exemple 2"
ssh -J rebond.meridian.local m.laurent@srv-db01.meridian.local   # srv-db01 n'est joignable que depuis rebond
```

Même syntaxe dans PowerShell avec le client OpenSSH (clé : `$HOME\.ssh\cle_ed25519`). Au premier accès, vérifier l'empreinte de la clé du serveur avant de l'accepter.

Pour comprendre : [Administration Linux, ch. 18 : SSH](../library/it/linux/administration-linux/05-partie-5-linux-en-reseau/02-chapitre-18-ssh-se-connecter-a-distance.md)
{ .kw-cs-meta }

## RDP

![[cheatsheets/windows/administration/reseau#Ouvrir une session de bureau à distance (RDP)]]

### Ouvrir un bureau RDP depuis Linux

```bash title="Commande"
xfreerdp3 /v:<machine> /u:<utilisateur> /dynamic-resolution    # xfreerdp selon la version de FreeRDP
```

```bash title="Exemple"
xfreerdp3 /v:srv-fs01.meridian.local /u:'MERIDIAN\m.laurent' /dynamic-resolution   # compte de domaine
```

```bat title="Exemple 2"
mstsc /v:srv-fs01.meridian.local:3390
```

Le second exemple, depuis Windows, vise un port RDP non standard. Sans `/p:`, le mot de passe est demandé et ne reste pas dans l'historique du shell. Vérifier le certificat du serveur à la première connexion ; pas de `/cert:ignore` par réflexe.

Pour comprendre : [RDP et ses journaux](../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md)
{ .kw-cs-meta }

### Accepter des connexions RDP sur une machine Linux (xrdp)

```bash title="Commande"
sudo apt install xrdp                  # xrdp = le serveur RDP de Linux, pas un client
sudo systemctl enable --now xrdp
sudo systemctl status xrdp
```

```bash title="Exemple"
sudo ss -tlnp | grep 3389              # le service écoute sur 3389/tcp
```

Debian ou Ubuntu avec un environnement graphique. `mstsc` ou `xfreerdp3` s'y connectent ensuite. Limiter l'accès au réseau prévu (VPN, bastion).

## VNC

### Ouvrir un bureau VNC

```bash title="Commande"
vncviewer <machine>:<affichage>        # :1 = affichage 1 = port 5901 en général
vncviewer <machine>::<port>            # deux-points doublés : le port lui-même
```

```bash title="Exemple"
vncviewer srv-lab01.meridian.local:1
```

```bash title="Exemple 2"
vncviewer 192.0.2.21::5901             # même serveur par son IP, port explicite
```

Client TigerVNC.

### Passer VNC dans un tunnel SSH

```bash title="Commande"
ssh -N -L <port_local>:localhost:<port_vnc> <utilisateur>@<machine>   # terminal 1, à garder ouvert
vncviewer localhost::<port_local>                                    # terminal 2, sur ton poste
```

```bash title="Exemple"
ssh -N -L 5901:localhost:5901 m.laurent@srv-lab01.meridian.local
vncviewer localhost::5901
```

Le second `5901` du tunnel est le port VNC de la cible. Si le port local est déjà pris, changer seulement le **premier** et le reporter dans `vncviewer`.

## Vue d'ensemble

| Besoin | Depuis | Commande rapide | Port par défaut |
|---|---|---|---|
| Terminal distant | Linux, macOS, Windows avec OpenSSH | `ssh <utilisateur>@<machine>` | `22/tcp` |
| Bureau RDP | Windows | `mstsc /v:<machine>` | `3389/tcp` |
| Bureau RDP | Linux avec FreeRDP | `xfreerdp3 /v:<machine> /u:<utilisateur>` | `3389/tcp` |
| Serveur RDP sur Linux | — | `sudo apt install xrdp` | `3389/tcp` |
| Bureau VNC | Linux avec TigerVNC | `vncviewer <machine>:1` | `5900 + affichage` |
| VNC chiffré | Linux | `ssh -N -L 5901:localhost:5901 …` | `22/tcp` |

Références : [OpenSSH](https://man.openbsd.org/ssh.1) · [Microsoft `mstsc`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc) · [FreeRDP](https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface) · [xrdp](https://github.com/neutrinolabs/xrdp) · [TigerVNC `vncviewer`](https://tigervnc.org/doc/vncviewer.html)
