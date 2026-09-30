---
title: Services, processus et sessions
source: IT/02_Windows/Fiche_Windows.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 7. Services Windows

### À retenir
Un **service** est un processus long, qui démarre au boot sans session ouverte et tourne en arrière-plan (réseau, diagnostics, mises à jour...). Il est piloté par le **SCM** (Service Control Manager).

### Comment ça fonctionne
Chaque service a :

- un **état** : `Running`, `Stopped`, `Paused` ;
- un **type de démarrage** : `Automatic`, `Automatic (Delayed)`, `Manual`, `Disabled` ;
- un **compte d'exécution** (souvent LocalSystem) ;
- un **`BINARY_PATH_NAME`** : le chemin de l'exécutable lancé.

Seuls les administrateurs peuvent normalement créer ou modifier un service. Mais une mauvaise configuration (permissions trop larges, chemin inscriptible) ouvre des failles.

### Pourquoi c'est important en cyber
Les permissions de service sont un **vecteur classique d'élévation de privilèges et de persistance**. Si un utilisateur peut modifier le `BINARY_PATH_NAME` ou remplacer le binaire pointé, il fait exécuter son code avec les privilèges du service (souvent SYSTEM). C'est aussi un point d'analyse SOC : un service au chemin suspect doit alerter.

### Exemple concret

```cmd
sc qc wuauserv
# BINARY_PATH_NAME : C:\WINDOWS\system32\svchost.exe -k netsvcs
# SERVICE_START_NAME : LocalSystem
```

Si ce chemin pointait vers un binaire inhabituel dans un dossier inscriptible, ce serait un signe de compromission ou une opportunité d'élévation.

### Commandes utiles

```cmd
sc qc <service>             # Config : binaire, compte, démarrage
sc query <service>          # État
sc stop <service>           # Stopper (nécessite admin)
```

```powershell
Get-Service | ? {$_.Status -eq "Running"}
```


### Point clé à mémoriser
Toujours vérifier `BINARY_PATH_NAME` et le compte d'exécution d'un service.

---

## 8. Processus Windows importants

### À retenir
Certains processus sont critiques : les connaître permet de **repérer les imposteurs** (malwares qui usurpent un nom légitime).
Gère services système qui s’exécutent à partir de .dll, tels que 
### Comment ça fonctionne

| Processus      | Rôle                                                                        | À vérifier en analyse                                                   |
| -------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `lsass.exe`    | Authentifie les connexions, crée les jetons d'accès, gère les mots de passe | Un seul instance, chemin `System32`, pas de faute de frappe             |
| `svchost.exe`  | Héberge les services tournant à partir de DLL                               | Chemin, signature, processus parent (`services.exe`), services hébergés |
| `services.exe` | Démarre/arrête les services (le SCM)                                        | Parent = `wininit.exe`                                                  |
| `winlogon.exe` | Charge le profil à la connexion, gère le verrouillage                       | Chemin légitime                                                         |
| `smss.exe`     | Gestion des sessions (Session Manager)                                      | Premier processus utilisateur lancé                                     |
| `csrss.exe`    | Sous-système Windows en mode utilisateur                                    | Présence multiple normale                                               |
| `System`       | Exécute le noyau Windows                                                    | PID 4, pas un fichier sur disque                                        |

### Pourquoi c'est important en cyber
Les malwares se déguisent souvent en processus système (`svchost.exe`, ou `scvhost.exe` avec une faute volontaire) pour passer inaperçus. Vérifier le **chemin**, la **signature** et le **processus parent** permet de distinguer le légitime de l'imposteur. Essentiel en SOC et forensic.

### Exemple concret
Un `svchost.exe` lancé depuis `C:\Users\bob\AppData\` (au lieu de `System32`) et sans parent `services.exe` est presque certainement malveillant.

### Point clé à mémoriser
`svchost.exe` est souvent imité ou abusé : vérifier chemin, signature, parent et services hébergés.

---

## 9. Comptes de service

### À retenir
Trois comptes intégrés non-interactifs servent à exécuter les services :

| Compte                                  | Privilèges                                                           |
| --------------------------------------- | -------------------------------------------------------------------- |
| **LocalSystem** (`NT AUTHORITY\SYSTEM`) | Compte le plus puissant de la machine, au-dessus des admins locaux   |
| **NetworkService**                      | Droits locaux limités, présente l'**identité machine** sur le réseau |
| **LocalService**                        | Droits locaux limités, identité **anonyme** sur le réseau            |

### Comment ça fonctionne
La différence se joue sur deux plans : les **droits locaux** (élevés pour LocalSystem, limités pour les deux autres) et l'**identité réseau** (machine pour NetworkService, anonyme pour LocalService). SYSTEM dépasse l'administrateur local car il agit au niveau du système d'exploitation lui-même, sans les restrictions appliquées aux comptes utilisateurs.

### Pourquoi c'est important en cyber
Le **principe du moindre privilège** veut qu'un service ne tourne pas en LocalSystem s'il n'en a pas besoin. Un service privilégié mal sécurisé devient un tremplin vers SYSTEM. Côté offensif, obtenir SYSTEM = contrôle total de la machine.

### Exemple concret
Une application de monitoring installée par défaut en LocalSystem alors qu'un compte limité suffirait : si son binaire est modifiable, l'attaquant hérite directement de SYSTEM.

### Point clé à mémoriser
SYSTEM > Administrateur local. Obtenir SYSTEM, c'est obtenir toute la machine.

---

## 10. Sessions Windows

### À retenir

- **Session interactive** : un utilisateur saisit ses identifiants (connexion locale, RDP, ou `runas`).
- **Session non-interactive** : comptes système sans mot de passe classique, utilisés pour lancer services et tâches planifiées.

### Comment ça fonctionne
Une session interactive démarre par une authentification explicite et ouvre un environnement de travail (`explorer.exe` et son token). Une session non-interactive est créée automatiquement par l'OS au démarrage pour exécuter les services en arrière-plan, sans intervention humaine. **RDP** (port 3389) ouvre une session interactive distante avec interface graphique ; **`runas`** lance un programme sous une autre identité.

### Pourquoi c'est important en cyber
Distinguer les deux aide à comprendre comment les services s'exécutent et quels comptes sont exploitables sans identifiants. RDP est un vecteur d'accès distant fréquent (recherche de fichiers `.rdp` sauvegardés en pentest).

### Point clé à mémoriser
Interactive = un humain s'authentifie ; non-interactive = l'OS lance des services sans mot de passe classique.

---
