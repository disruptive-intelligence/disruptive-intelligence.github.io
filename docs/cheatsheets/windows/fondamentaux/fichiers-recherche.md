---
title: "Fichiers et recherche"
cours:
  - library/it/windows/ligne-de-commande-windows/index.md
  - library/it/windows/powershell/index.md
---

# Fichiers et recherche

Lire, trouver et comparer des fichiers ; chercher un mot dans un fichier ou tout un dossier ; calculer une empreinte ; repérer les flux cachés.

Les incontournables : `Get-Content` · `Get-ChildItem -Recurse` · `Select-String` · `findstr` · `Get-FileHash` · `Get-Item -Stream`
{ .kw-cs-top }

## Lire

### Afficher le contenu d'un fichier

```powershell title="Commande"
Get-Content <fichier>   # alias : cat, type, gc
```

```powershell title="Exemple"
Get-Content C:\Windows\System32\drivers\etc\hosts
```

??? example "Sortie"
    ```text
    # Copyright (c) 1993-2009 Microsoft Corp.
    #
    127.0.0.1       localhost
    192.168.1.20    intranet.meridian.local
    ```

```bat title="Exemple 2"
type C:\Windows\System32\drivers\etc\hosts
more C:\Logs\gros-fichier.log   :: page par page
```

### Lire la fin d'un fichier, ou la suivre en direct

```powershell title="Commande"
Get-Content <fichier> -Tail <n>          # n dernières lignes
Get-Content <fichier> -Tail <n> -Wait    # puis les nouvelles lignes au fil de l'eau (Ctrl+C pour arrêter)
```

```powershell title="Exemple"
Get-Content C:\inetpub\logs\LogFiles\W3SVC1\u_ex261002.log -Tail 2
```

??? example "Sortie"
    ```text
    2026-10-02 09:41:12 192.168.1.15 GET /index.html - 443 - 192.168.1.50 Mozilla/5.0 200 0 0 12
    2026-10-02 09:41:15 192.168.1.15 GET /login - 443 - 192.168.1.50 Mozilla/5.0 302 0 0 8
    ```

```powershell title="Exemple 2"
Get-Content .\app.log -TotalCount 20   # les 20 premières lignes (équivalent de head)
```

## Trouver

### Trouver un fichier par son nom

```powershell title="Commande"
Get-ChildItem -Path <dossier> -Recurse -Filter <motif> -ErrorAction SilentlyContinue
```

```powershell title="Exemple"
Get-ChildItem C:\Users -Recurse -Filter *.rdp -ErrorAction SilentlyContinue | Select-Object FullName
```

??? example "Sortie"
    ```text
    FullName
    --------
    C:\Users\alice\Documents\serveur-compta.rdp
    ```

```bat title="Exemple 2"
dir C:\Users\*.rdp /s /b   :: /s : sous-dossiers, /b : chemin seul
where /r C:\ notepad.exe   :: chercher un exécutable
```

### Trouver les fichiers modifiés récemment

```powershell title="Commande"
Get-ChildItem <dossier> -Recurse -File | Where-Object LastWriteTime -gt (Get-Date).AddDays(-<n>)
```

```powershell title="Exemple"
Get-ChildItem C:\Users\alice\AppData -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object LastWriteTime -gt (Get-Date).AddHours(-24) |
    Sort-Object LastWriteTime -Descending | Select-Object -First 3 LastWriteTime, FullName
```

??? example "Sortie"
    ```text
    LastWriteTime        FullName
    -------------        --------
    02/10/2026 09:15:02  C:\Users\alice\AppData\Local\Temp\maj.ps1
    02/10/2026 09:14:57  C:\Users\alice\AppData\Roaming\Microsoft\Windows\Recent\facture.lnk
    02/10/2026 08:02:41  C:\Users\alice\AppData\Local\Microsoft\Edge\User Data\Default\History
    ```

Ensuite : [calculer l'empreinte d'un fichier](#calculer-lempreinte-dun-fichier)
{ .kw-cs-meta }

### Trouver les plus gros fichiers

```powershell title="Commande"
Get-ChildItem <dossier> -Recurse -File -ErrorAction SilentlyContinue | Sort-Object Length -Descending | Select-Object -First <n> FullName, Length
```

```powershell title="Exemple"
Get-ChildItem D:\Partages -Recurse -File -ErrorAction SilentlyContinue | Sort-Object Length -Descending |
    Select-Object -First 3 FullName, @{n='Mo';e={[math]::Round($_.Length/1MB)}}
```

??? example "Sortie"
    ```text
    FullName                              Mo
    --------                              --
    D:\Partages\IT\images\win11.iso     6142
    D:\Partages\Compta\archives2024.zip 2210
    D:\Partages\RH\videos\accueil.mp4    845
    ```

## Chercher dans le contenu

### Chercher un mot dans un fichier ou un dossier

```powershell title="Commande"
Select-String -Path <fichiers> -Pattern "<motif>"   # alias : sls ; motif = expression régulière
```

```powershell title="Exemple"
Select-String -Path C:\Scripts\*.ps1 -Pattern "password" -SimpleMatch
```

??? example "Sortie"
    ```text
    C:\Scripts\sauvegarde.ps1:12:$password = Get-Content .\secret.txt
    C:\Scripts\deploy.ps1:4:# password : voir le coffre KeePass
    ```

```powershell title="Exemple 2"
Get-ChildItem C:\Scripts -Recurse -Include *.ps1,*.bat,*.config | Select-String -Pattern "pass(word)?\s*=" -List
```

```bat title="Exemple 3 (CMD)"
findstr /s /i /n "password" C:\Scripts\*.*   :: /s sous-dossiers, /i sans casse, /n numéro de ligne
```

### Filtrer la sortie d'une commande

```powershell title="Commande"
<commande> | Select-String "<motif>"       # sur du texte
<commande> | Where-Object <propriété> -like "*<motif>*"   # sur des objets PowerShell
```

```powershell title="Exemple"
Get-Service | Where-Object DisplayName -like "*Defender*" | Select-Object Status, Name
```

??? example "Sortie"
    ```text
    Status  Name
    ------  ----
    Running WinDefend
    Running WdNisSvc
    ```

```bat title="Exemple 2"
ipconfig /all | findstr /i "IPv4 DNS"
```

## Vérifier

### Calculer l'empreinte d'un fichier

```powershell title="Commande"
Get-FileHash <fichier> -Algorithm SHA256   # MD5, SHA1, SHA256 (défaut), SHA512
```

```powershell title="Exemple"
Get-FileHash C:\Users\alice\Downloads\facture.exe
```

??? example "Sortie"
    ```text
    Algorithm       Hash                                                                   Path
    ---------       ----                                                                   ----
    SHA256          9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08       C:\Users\alice\Downloads\facture.exe
    ```

```bat title="Exemple 2"
certutil -hashfile C:\Users\alice\Downloads\facture.exe SHA256
```

Ensuite : chercher l'empreinte dans une base de réputation (VirusTotal) sans envoyer le fichier.
{ .kw-cs-meta }

### Vérifier la signature d'un exécutable

```powershell title="Commande"
Get-AuthenticodeSignature <fichier>   # Valid, NotSigned, HashMismatch…
```

```powershell title="Exemple"
Get-AuthenticodeSignature C:\Windows\System32\svchost.exe | Select-Object Status, @{n='Signataire';e={$_.SignerCertificate.Subject}}
```

??? example "Sortie"
    ```text
    Status Signataire
    ------ ----------
     Valid CN=Microsoft Windows, O=Microsoft Corporation, L=Redmond, S=Washington, C=US
    ```

```bat title="Exemple 2"
sigcheck -a -h C:\Users\alice\Downloads\facture.exe   :: Sysinternals : signature, éditeur, empreintes
```

### Comparer deux fichiers

```powershell title="Commande"
Compare-Object (Get-Content <fichier1>) (Get-Content <fichier2>)   # <= : seulement dans 1, => : seulement dans 2
```

```powershell title="Exemple"
Compare-Object (Get-Content .\services-hier.txt) (Get-Content .\services-aujourdhui.txt)
```

??? example "Sortie"
    ```text
    InputObject           SideIndicator
    -----------           -------------
    UpdaterSvc            =>
    ```

```bat title="Exemple 2"
fc /n services-hier.txt services-aujourdhui.txt
```

### Voir les flux de données alternatifs (ADS) d'un fichier

```powershell title="Commande"
Get-Item <fichier> -Stream *                       # flux d'un fichier (:$DATA = contenu normal)
Get-Content <fichier> -Stream <nom_du_flux>        # lire un flux
```

```powershell title="Exemple"
Get-Content C:\Users\alice\Downloads\facture.exe -Stream Zone.Identifier
```

??? example "Sortie"
    ```text
    [ZoneTransfer]
    ZoneId=3
    ReferrerUrl=https://mail.example.com/
    HostUrl=https://203.0.113.15/facture.exe
    ```

`ZoneId=3` = Internet : c'est le **Mark of the Web**, qui déclenche SmartScreen et le mode protégé d'Office.

```bat title="Exemple 2"
dir /r C:\Users\alice\Downloads   :: /r : affiche les flux alternatifs
```

Pour comprendre : [Windows en profondeur, ch. 4 (NTFS)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/04-chapitre-4-le-systeme-de-fichiers-ntfs.md)
{ .kw-cs-meta }
