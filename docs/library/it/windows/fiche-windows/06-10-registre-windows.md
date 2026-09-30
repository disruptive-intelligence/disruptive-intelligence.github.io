---
title: 10. Registre Windows
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

## 10.1 Définition

Le **registre Windows** est une base de données hiérarchique qui stocke la configuration de Windows et de nombreuses applications.

Il contient :

- paramètres système ;
    
- configuration logicielle ;
    
- services ;
    
- pilotes ;
    
- profils utilisateurs ;
    
- paramètres de sécurité ;
    
- mécanismes de démarrage automatique.
    

Ouvrir l’éditeur de registre :

```cmd
regedit
```


Interroger le registre en ligne de commande :

```cmd
reg query <clé>
```


---

## 10.2 Vocabulaire

|Terme|Définition simple|
|---|---|
|Ruche / Hive|Grande racine logique du registre.|
|Key / clé|Équivalent d’un dossier.|
|Subkey / sous-clé|Sous-dossier dans une clé.|
|Value / valeur|Entrée contenant une donnée.|
|Data / donnée|Contenu de la valeur.|

Image mentale :

```text
Ruche = disque
Clé = dossier
Valeur = fichier
Donnée = contenu du fichier
```


---

## 10.3 Ruches principales

|Ruche|Abréviation|Contenu principal|
|---|---|---|
|`HKEY_LOCAL_MACHINE`|`HKLM`|Configuration globale machine : services, pilotes, logiciels, sécurité.|
|`HKEY_CURRENT_USER`|`HKCU`|Configuration du profil utilisateur courant.|
|`HKEY_CLASSES_ROOT`|`HKCR`|Associations de fichiers, COM, classes.|
|`HKEY_USERS`|`HKU`|Profils utilisateurs chargés, identifiés par SID.|
|`HKEY_CURRENT_CONFIG`|`HKCC`|Configuration matérielle courante.|

À retenir :

```text
HKLM = machine
HKCU = utilisateur courant
HKU  = tous les profils utilisateurs chargés
```


---

## 10.4 Fichiers physiques du registre

Les ruches système sont stockées dans :

```text
C:\Windows\System32\config\
```


|Fichier|Rôle|
|---|---|
|`SAM`|Comptes locaux.|
|`SYSTEM`|Configuration système.|
|`SECURITY`|Secrets et politiques de sécurité.|
|`SOFTWARE`|Configuration logicielle.|
|`DEFAULT`|Profil par défaut.|

La ruche utilisateur courante est stockée dans :

```text
C:\Users\<USERNAME>\NTUSER.DAT
```


---

## 10.5 Services dans le registre

Les services sont configurés dans :

```text
HKLM\SYSTEM\CurrentControlSet\Services\<ServiceName>
```


Exemple :

```powershell
Get-Acl -Path HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List
```


Interroger avec `reg` :

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services\wuauserv
```


---
