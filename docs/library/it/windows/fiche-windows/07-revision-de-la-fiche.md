---
title: Révision de la fiche
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

### Synthèse mentale

Tout le modèle de sécurité Windows tient dans une chaîne :

> **Utilisateur** → s'authentifie → **LSASS** vérifie l'identité (contre la **SAM** en local, ou Active Directory en domaine) → Windows crée un **access token** → ce token contient le **SID**, les **groupes** et les **privilèges** → l'utilisateur tente d'accéder à un **objet** (fichier, service, clé de registre) → Windows compare le token à la **DACL** de l'objet → **autorisation ou refus**.

Tout le reste s'y rattache : les **services** s'exécutent avec un compte (souvent SYSTEM) et donc un token privilégié ; les **permissions NTFS** définissent les DACL des fichiers ; le **registre** stocke la config et des points de **persistance** (Run/RunOnce) ; **LSASS** garde en mémoire les secrets qui rendent ce SSO possible — et en fait une cible. Comprendre cette chaîne, c'est comprendre où chercher une faille et comment Windows décide.

---

### Commandes à connaître par cœur

```cmd
systeminfo                            # Cartographie de la cible
whoami /user                          # SID du compte courant
whoami /groups                        # SIDs des groupes
whoami /priv                          # Privilèges actifs
ipconfig /all                         # Réseau
netstat -abon                         # Connexions + ports + PID
tasklist                              # Lister les processus
taskkill /PID <pid>                   # Tuer un processus
net share                             # Partages locaux
icacls <dossier>                      # Permissions NTFS
sc qc <service>                       # Config d'un service
reg query HKCU\...\CurrentVersion\Run # Persistance
```

```powershell
Get-Service | ? {$_.Status -eq "Running"}
Get-WmiObject -Class Win32_OperatingSystem | select Version,BuildNumber
```


---

### Erreurs fréquentes à éviter

- Croire que **System32 = 32 bits** → c'est **64 bits** (SysWOW64 = 32 bits).
- Confondre **NTFS permissions** et **Share permissions** → les deux s'appliquent, la plus restrictive gagne.
- Penser que l'**Execution Policy** PowerShell ou l'**UAC** sont des protections infranchissables → ils se contournent.
- Vouloir exploiter la **SAM seule** → il faut **SAM + SYSTEM**.
- Oublier que **SYSTEM est plus puissant qu'Administrateur**.
- Confondre **être administrateur** et **s'exécuter en contexte élevé** (UAC).
- Ignorer les **partages par défaut** (`C$`, `ADMIN$`) en énumération.
- Négliger les clés **Run/RunOnce** en analyse de persistance.

---

### Résumé ultra-court pour entretien

> Windows fonde sa sécurité sur les **SID** (identifiants uniques), les **access tokens** (qui portent SID, groupes et privilèges d'une session) et les **ACL/DACL** (qui décident, par comparaison avec le token, l'accès à chaque objet). L'authentification passe par **LSASS**, qui vérifie l'identité contre la **SAM** locale (ou Active Directory en domaine) et garde des identifiants en mémoire — ce qui en fait une cible de vol. Les **services** tournent souvent en **LocalSystem** : leurs mauvaises permissions sont un vecteur d'élévation vers SYSTEM. La **persistance** se cache dans le **registre** (clés Run/RunOnce) ou dans des services. **SMB** (port 445) gère les partages, avec des partages administratifs (`C$`, `ADMIN$`) actifs par défaut. L'**UAC** ralentit l'abus de privilèges mais n'est pas une barrière absolue.

---

### Mini quiz

1. Quelle commande donne une vue d'ensemble du système (OS, build, patchs) ?
2. System32 contient-il les binaires 32 ou 64 bits ?
3. Quel port utilise SMB ?
4. Quels sont les trois partages administratifs activés par défaut ?
5. Que contient un access token ?
6. Quel RID correspond toujours au vrai compte Administrateur ?
7. Quels deux fichiers faut-il pour exploiter la SAM ?
8. Quel processus est responsable de l'authentification et garde les identifiants en mémoire ?
9. Quelles clés de registre sont à vérifier en priorité pour détecter une persistance ?
10. Entre NTFS et Share permissions, laquelle l'emporte quand les deux s'appliquent ?
11. Pourquoi SYSTEM est-il plus puissant qu'un administrateur local ?
12. Comment Windows décide-t-il d'autoriser ou refuser un accès à un objet ?
13. Quelle est la différence entre une session interactive et non-interactive ?
14. L'UAC est-il une barrière de sécurité infranchissable ? Pourquoi ?
15. Où sont stockés physiquement les fichiers du registre machine ?


## Windows — Processus, Services et Sécurité

> Objectif : comprendre les mécanismes Windows utiles en cybersécurité : processus, services, LSASS, tokens, SID, ACL, registre, permissions de services, persistance et protections natives.

---

### 0. Vue d’ensemble

Windows exécute des programmes sous forme de **processus**. Chaque processus tourne dans un contexte précis : utilisateur, privilèges, espace mémoire, fichiers ouverts, DLL chargées, connexions réseau, etc.

Les **services Windows** sont des processus particuliers : ils sont conçus pour tourner longtemps, souvent en arrière-plan, parfois dès le démarrage de la machine et sans session utilisateur ouverte.

Côté sécurité, Windows s’appuie sur plusieurs notions centrales :

- **SID** : identifiant unique d’un utilisateur, groupe, machine ou service.
    
- **Access token** : “badge” attaché aux processus pour représenter les droits de l’utilisateur.
    
- **ACL / ACE / DACL / SACL** : règles d’accès appliquées aux objets sécurisables.
    
- **LSASS** : processus critique chargé de l’authentification et de la politique de sécurité locale.
    
- **Registre** : base de configuration de Windows, souvent utilisée pour les services, la sécurité et la persistance.
    

> Idée clé : pour comprendre Windows en cyber, il faut comprendre la chaîne suivante :
> 
> **Utilisateur → authentification → token → processus → accès aux objets → DACL → autorisation ou refus**.

---
