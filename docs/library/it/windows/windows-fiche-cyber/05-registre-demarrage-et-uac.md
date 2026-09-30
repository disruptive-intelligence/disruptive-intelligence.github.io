---
title: Registre, démarrage et UAC
source: IT/02_Windows/Fiche_Windows.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 13. Registre Windows

### À retenir
Base de données hiérarchique de configuration de l'OS et des applications. Structure : **clés** (dossiers) → **sous-clés** → **valeurs** (données).

### Comment ça fonctionne
Le registre est organisé en **ruches (hives)**, dont les principales :

| Ruche                          | Contenu                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------- |
| **HKLM** (HKEY_LOCAL_MACHINE)  | Config machine globale : services, pilotes, SAM, SYSTEM, SOFTWARE               |
| **HKCU** (HKEY_CURRENT_USER)   | Config de l'utilisateur courant : préférences, programmes au démarrage          |
| **HKU** (HKEY_USERS)           | Tous les profils chargés (un SID par utilisateur) ; HKCU pointe vers l'un d'eux |
| **HKCR** (HKEY_CLASSES_ROOT)   | Associations de fichiers et COM                                                 |
| **HKCC** (HKEY_CURRENT_CONFIG) | Config matérielle courante                                                      |

Physiquement, les ruches machine sont dans `C:\Windows\System32\config\` (SAM, SYSTEM, SOFTWARE...) et la ruche utilisateur dans `C:\Users\<user>\NTUSER.DAT`. Types de valeurs courants : `REG_SZ` (chaîne), `REG_DWORD` (entier 32 bits), `REG_BINARY` (données brutes), `REG_EXPAND_SZ` (chaîne avec variables).

### Pourquoi c'est important en cyber
Le registre stocke des paramètres de sécurité, des points de persistance et parfois des identifiants. C'est un terrain d'analyse forensic central et un levier de durcissement.

### Commandes utiles

```cmd
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
regedit                     # Éditeur graphique
```


### Point clé à mémoriser
HKLM = machine (global), HKCU = utilisateur courant. Les fichiers sont sous `System32\config` et `NTUSER.DAT`.

---

## 14. Run / RunOnce

### À retenir
Clés de registre qui lancent des programmes **automatiquement** au démarrage ou à l'ouverture de session.

```
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\...\CurrentVersion\RunOnce
HKCU\...\CurrentVersion\RunOnce
```


### Comment ça fonctionne

- Les clés sous **HKLM** s'exécutent pour **tous les utilisateurs** au démarrage de la machine.
- Les clés sous **HKCU** s'exécutent **à l'ouverture de session** de l'utilisateur concerné.
- **Run** relance le programme à chaque fois ; **RunOnce** le supprime après une exécution.

### Pourquoi c'est important en cyber
C'est un mécanisme de **persistance** classique : ajouter une valeur pointant vers un binaire le fait relancer automatiquement. En réponse à incident, vérifier les clés Run/RunOnce fait partie des premiers réflexes pour repérer un programme indésirable qui se relance seul.

### Exemple concret
Une valeur `Updater → C:\Users\Public\update.exe` dans `HKCU\...\Run` qui ne correspond à aucun logiciel installé est un signe de persistance à investiguer.

### Commandes utiles

```cmd
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```


### Point clé à mémoriser
Run/RunOnce = persistance classique à vérifier en priorité.

---

## 15. UAC (User Account Control)

### À retenir
Fonctionnalité empêchant un programme d'effectuer des actions privilégiées **sans confirmation explicite**, même lancé par un administrateur.

### Comment ça fonctionne
Avec l'**Admin Approval Mode**, un administrateur travaille par défaut avec un token **standard** (privilèges réduits). Quand une action nécessite des droits élevés (installation, modif système), une **invite de consentement** apparaît : l'utilisateur doit confirmer, ce qui « élève » le programme vers un token administrateur complet. Un utilisateur standard, lui, doit fournir un mot de passe admin.

C'est ici la distinction clé : **être administrateur** ne signifie pas **s'exécuter en contexte élevé**. Tant que l'élévation n'a pas eu lieu, le programme tourne avec des droits limités.

### Pourquoi c'est important en cyber
L'UAC interrompt l'exécution silencieuse de scripts ou binaires malveillants jusqu'à confirmation. Mais ce **n'est pas une frontière de sécurité absolue** : il existe des techniques de contournement (UAC bypass). Côté durcissement, il faut le configurer correctement sans s'y fier comme unique protection.

### Exemple concret
Un script lancé par un admin qui tente de modifier le système déclenche l'invite UAC : sans clic de confirmation, l'action est bloquée.

### Point clé à mémoriser
Administrateur ≠ contexte élevé. L'UAC ralentit l'abus mais se contourne ; ce n'est pas une barrière infranchissable.

---
