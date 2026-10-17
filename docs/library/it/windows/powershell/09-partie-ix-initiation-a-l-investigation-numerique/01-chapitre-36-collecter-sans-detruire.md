---
title: Chapitre 36 — Collecter sans détruire
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IX — Initiation à l'investigation numérique
  - index.md
---

acquisition et chaîne de preuve

## 🟢 Le minimum à savoir

### Le paradoxe de l'investigation

Pour savoir ce qui s'est passé sur une machine, il faut l'interroger. Mais l'interroger la **modifie** : chaque commande que tu tapes crée un processus, écrit dans des journaux (le Script Block Logging du Ch.35 enregistre ton propre PowerShell !), touche des fichiers. C'est le **principe d'échange de Locard**, emprunté à la police scientifique : *tout contact laisse une trace*.

On ne peut pas l'éviter. On peut en revanche le **maîtriser**, avec quatre règles :

1. **Ne pas éteindre ni redémarrer par réflexe.** Tout ce qui vit en mémoire (processus, connexions, code malveillant sans fichier) disparaîtrait. Le premier geste le plus fréquent est d'**isoler la machine du réseau** (câble débranché, Wi-Fi coupé, isolement par l'antivirus d'entreprise) plutôt que de l'éteindre — mais même cela n'est pas automatique (voir l'encadré ci-dessous).
2. **Collecter du plus volatil au moins volatil** (voir plus bas).
3. **Ne rien écrire sur le disque suspect.** La collecte va sur un **support externe** : chaque fichier écrit sur `C:` peut écraser des données effacées mais encore récupérables.
4. **Tout documenter.** Ce que tu as fait, quand, avec quel outil : c'est ce qui permettra plus tard de distinguer **tes** traces de celles de l'attaquant.

> **⚠️ Une décision, pas un réflexe.** En situation réelle, le sort de la machine — la laisser tourner, l'isoler, la mettre en veille prolongée, l'éteindre — se **décide** selon la menace, les procédures de réponse à incident de l'organisation et l'objectif de l'investigation, par la personne qui pilote l'incident. Quelques situations qui font pencher la balance :
>
> - **Un rançongiciel en train de chiffrer** : stopper la destruction peut primer sur la préservation de la mémoire. Certaines procédures privilégient alors la mise en veille prolongée, qui interrompt tout en écrivant la RAM dans `hiberfil.sys`.
> - **Un attaquant qu'on veut observer** pour mesurer l'étendue de la compromission : couper le réseau le préviendrait. On peut choisir de laisser la machine connectée, sous surveillance.
> - **Un serveur critique** : l'isoler, c'est aussi interrompre un service dont l'entreprise dépend.
>
> Dans ton lab, applique les quatre règles telles quelles : elles sont le bon point de départ. En entreprise, suis la procédure. Et sans consigne : ne fais rien d'irréversible, documente, et alerte le responsable.

### Trois façons d'acquérir

« Acquérir », c'est copier les preuves pour les analyser ailleurs. Il en existe trois formes, et ce chapitre se concentre sur la première :

| Acquisition | Ce qu'on obtient | Outil | Dans ce cours |
|---|---|---|---|
| **Collecte à chaud** (*live response*) | Une sélection ciblée : processus, connexions, journaux… | **PowerShell** | ✅ Pratique complète |
| **Image mémoire** | Une copie brute de toute la RAM | Outils dédiés (WinPmem, DumpIt…) | Survol (🟡) |
| **Image disque** | Une copie bit à bit de tout le disque | Outils dédiés + bloqueur d'écriture | Mention seulement |

> **Image disque, en deux phrases.** Une image disque est une copie **bit à bit** de tout le support, y compris l'espace « vide » où dorment les fichiers effacés. On la réalise avec un matériel qui empêche toute écriture sur l'original (un *bloqueur d'écriture*), puis on n'analyse **jamais** l'original : uniquement une copie dont l'empreinte correspond. C'est un métier à part entière, hors du périmètre de ce cours.

### L'ordre de volatilité

Toutes les preuves ne disparaissent pas à la même vitesse. La référence en la matière (la RFC 3227) impose de collecter dans cet ordre :

| Ordre | Ce qu'on collecte | Durée de vie |
|---|---|---|
| 1 | Mémoire vive, processus en cours, connexions réseau, sessions ouvertes | Disparaît à l'extinction, change à chaque seconde |
| 2 | Cache DNS, cache ARP, fichiers temporaires | Minutes à heures |
| 3 | Journaux d'événements, fichiers sur disque, registre | Jours à mois |
| 4 | Sauvegardes, journaux centralisés | Mois à années |

> **Les journaux tournent.** Un journal d'événements a une taille maximale : une fois plein, les événements les plus anciens sont écrasés. Sur un poste actif, le journal Security peut ne couvrir que quelques jours. Raison de plus pour l'exporter tôt.

### Deux « premiers gestes » à ne pas confondre

Deux choses se disputent la première place, et elles ne relèvent pas de la même logique :

- **L'ordre d'acquisition des preuves** suit la volatilité : si une capture mémoire est prévue, elle passe **avant tout le reste**, y compris avant d'ouvrir PowerShell, car lancer PowerShell modifie déjà la mémoire.
- **L'enregistrement de tes actions** commence dès que tu agis. Avant PowerShell, il est **manuscrit** (carnet : heure, outil, ce que tu fais) ; dès que PowerShell est ouvert, `Start-Transcript` prend le relais.

La séquence complète d'une intervention ressemble donc à ceci :

| Étape | Action | Trace de l'action |
|---|---|---|
| 0 | Décision sur le sort de la machine (encadré plus haut), notes de départ | Carnet |
| 1 | Capture mémoire, si prévue, avec un outil dédié (🟡) | Carnet : heure, outil, empreinte du fichier produit |
| 2 | Ouverture de PowerShell, **`Start-Transcript` en toute première commande** | Transcript |
| 3 | Collecte du volatil : processus, connexions, caches | Transcript |
| 4 | Export des journaux d'événements | Transcript |
| 5 | `Stop-Transcript`, puis manifeste d'empreintes | Manifeste |

### Documenter avec `Start-Transcript`

Premier geste de la **phase PowerShell** : démarrer l'enregistrement de ta session (rappel Ch.35). Tout ce que tu tapes, et tout ce que PowerShell affiche, est consigné :

```powershell
$dest = "E:\Collecte_SRV01"          # support EXTERNE (clé USB, disque), jamais C:
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Start-Transcript -Path "$dest\journal_intervention.txt"

# ... toute la collecte ...

Stop-Transcript
```


### Collecter le volatil `[🔑 Admin]`

Rien de nouveau dans les commandes : ce sont celles des Parties II et III. Ce qui change, c'est l'**ordre** et la **destination**.

```powershell
# 0. Le contexte : qui collecte, quand (en UTC), et le fuseau horaire de la machine.
#    Indispensable pour reconstituer une chronologie au Ch.37.
[PSCustomObject]@{
    Machine       = $env:COMPUTERNAME
    DebutUtc      = (Get-Date).ToUniversalTime().ToString("o")
    FuseauHoraire = (Get-TimeZone).Id
    Analyste      = "$env:USERDOMAIN\$env:USERNAME"
} | ConvertTo-Json | Set-Content "$dest\00_contexte.json" -Encoding UTF8

# 1. Processus : ligne de commande, parent et date de création (Ch.11)
Get-CimInstance Win32_Process |
    Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine, CreationDate |
    Export-Csv "$dest\01_processus.csv" -NoTypeInformation -Encoding UTF8

# 2. Connexions réseau et processus propriétaire (Ch.17)
Get-NetTCPConnection |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, OwningProcess, CreationTime |
    Export-Csv "$dest\02_connexions_tcp.csv" -NoTypeInformation -Encoding UTF8

# 3. Cache DNS : les noms résolus récemment (Ch.16)
Get-DnsClientCache |
    Select-Object Entry, Data, TimeToLive |
    Export-Csv "$dest\03_cache_dns.csv" -NoTypeInformation -Encoding UTF8

# 4. Cache ARP : les machines du réseau local contactées récemment
Get-NetNeighbor -AddressFamily IPv4 |
    Select-Object IPAddress, LinkLayerAddress, State, InterfaceAlias |
    Export-Csv "$dest\04_cache_arp.csv" -NoTypeInformation -Encoding UTF8
```


> **Pourquoi ces commandes passent avant les journaux ?** C'est l'ordre de volatilité : une connexion réseau peut se fermer dans la seconde, un processus malveillant peut se terminer. Le journal Security, lui, sera encore là dans cinq minutes.

### Exporter proprement les journaux d'événements `[🔑 Admin]`

Les fichiers `.evtx` se trouvent dans `C:\Windows\System32\winevt\Logs`, mais **ne les copie pas à la main** : ils sont en cours d'utilisation par le service de journalisation, et une copie brute peut échouer ou être incohérente. On demande au service lui-même de faire l'export, avec l'outil natif `wevtutil` (PowerShell n'a pas de cmdlet pour exporter un journal) :

```powershell
foreach ($journal in "Security", "System", "Microsoft-Windows-PowerShell/Operational") {
    # Le "/" est interdit dans un nom de fichier : on le remplace par "_"
    $nomFichier = ($journal -replace '[/\\]', '_') + ".evtx"
    wevtutil epl $journal "$dest\$nomFichier"
    if ($LASTEXITCODE -ne 0) { Write-Warning "Export échoué : $journal (code $LASTEXITCODE)" }
}
```


`wevtutil` est un exécutable externe : on vérifie donc son code de sortie avec `$LASTEXITCODE` (rappel Ch.8).

### Empreintes et chaîne de preuve

Une preuve n'a de valeur que si l'on peut démontrer qu'elle **n'a pas été modifiée**. C'est le rôle de l'empreinte (le hash, rappel Ch.34) : si un seul octet change, l'empreinte SHA-256 change complètement. Mais attention à ce qu'elle prouve exactement : qu'un fichier est identique à ce qu'il était **au moment où son empreinte de référence a été calculée** — ni plus, ni moins. D'où la règle : calculer les empreintes **le plus tôt possible** après la collecte.

On calcule donc l'empreinte de **chaque** fichier collecté, et on les consigne dans un **manifeste**. Attention à l'ordre : on arrête le transcript **avant**, sinon le fichier `journal_intervention.txt` continuerait de changer après le calcul de son empreinte.

```powershell
Stop-Transcript     # d'abord : le journal d'intervention ne doit plus bouger

$manifeste = Get-ChildItem $dest -File |
    Where-Object Name -ne "manifeste.csv" |
    ForEach-Object {
        [PSCustomObject]@{
            Fichier      = $_.Name
            TailleOctets = $_.Length
            SHA256       = (Get-FileHash $_.FullName -Algorithm SHA256).Hash
            HashUtc      = (Get-Date).ToUniversalTime().ToString("o")
        }
    }
$manifeste | Export-Csv "$dest\manifeste.csv" -NoTypeInformation -Encoding UTF8

# L'empreinte du manifeste lui-même : à noter AILLEURS (carnet, ticket, message au responsable)
(Get-FileHash "$dest\manifeste.csv" -Algorithm SHA256).Hash
```


Plus tard, au moment de l'analyse, on vérifie que rien n'a bougé :

```powershell
Import-Csv "$dest\manifeste.csv" | ForEach-Object {
    $actuel = (Get-FileHash (Join-Path $dest $_.Fichier) -Algorithm SHA256).Hash
    [PSCustomObject]@{ Fichier = $_.Fichier; Intact = ($actuel -eq $_.SHA256) }
}
```


**Intégrité et chaîne de preuve : deux choses différentes.** On les confond souvent, alors précisons.

- **L'intégrité**, c'est ce que tu viens de faire : vérifier qu'un fichier n'a pas changé depuis son empreinte de référence. C'est technique, et PowerShell le fait très bien.
- **La chaîne de preuve** (*chain of custody*), c'est la **traçabilité** complète de la preuve : qui l'a collectée, quand, comment, où elle a été conservée, qui y a eu accès, et chaque fois qu'elle a changé de mains (qui l'a remise, à qui, quand, pourquoi). C'est surtout **procédural** : un registre, des signatures, un stockage sous clé.

Les empreintes ne suffisent pas à établir la chaîne de preuve, pour trois raisons. Une empreinte ne dit rien de **qui** a détenu le fichier ni de **qui l'a consulté**. Elle ne dit rien de ce qui s'est passé **avant** son calcul : une collecte mal faite, bien hachée, reste une collecte mal faite. Et elle ne vaut que si la référence elle-même est hors d'atteinte : quelqu'un capable de modifier les fichiers pourrait aussi régénérer le manifeste — c'est pourquoi l'empreinte du manifeste se note **ailleurs**, chez un tiers ou dans un système qu'on ne contrôle pas seul.

Concrètement, chaque étape de la vie d'une preuve donne une ligne dans un registre de ce type :

| Date et heure (UTC) | Action | Par | Remis à / lieu de stockage | Empreinte vérifiée ? |
|---|---|---|---|---|
| 2026-10-17 14:02 | Collecte sur SRV01 | A. Martin | Disque externe n° 3, armoire forte | Calculée : `4F2A…` |
| 2026-10-17 16:40 | Remise pour analyse | A. Martin | S. Bernard, équipe sécurité | ✅ Identique |

Le formalisme dépend du contexte : un incident interne n'exige pas la même rigueur qu'une affaire susceptible de finir devant un tribunal. Mais le principe ne change pas : **l'empreinte prouve que le contenu n'a pas bougé, le registre prouve par où il est passé**.

## 🟡 Très utile en pratique

### La mémoire vive : ce que PowerShell ne voit pas

La RAM contient des choses qu'aucun fichier ne garde : les processus et leur code (y compris du code **injecté** dans un processus légitime), les connexions réseau, des données déchiffrées, parfois des clés et des mots de passe. Et surtout, les **malwares sans fichier** (*fileless*) : un script téléchargé et exécuté directement en mémoire n'a jamais touché le disque. À l'extinction, tout disparaît.

**Pourquoi la collecte PowerShell ne suffit pas.** `Get-Process` et `Get-NetTCPConnection` interrogent les **API de Windows**. Sur une machine saine, elles disent la vérité. Mais un attaquant qui a compromis le noyau (un *rootkit*) peut les faire mentir, et cacher un processus ou une connexion. Une **image mémoire**, elle, copie la RAM telle quelle ; analysée sur une autre machine, elle ne dépend plus de l'honnêteté du système compromis.

**Capturer la mémoire.** Il faut des outils dédiés : **WinPmem** (open source), **DumpIt**, **Magnet RAM Capture**, **FTK Imager**. Quelques règles :

- La capture passe **en premier**, avant même d'ouvrir PowerShell (étape 1 de la séquence) : c'est la donnée la plus volatile. Comme le transcript n'existe pas encore, on la note **à la main** : heure, outil, empreinte du fichier produit.
- L'outil se lance depuis un support externe et écrit sur un support externe.
- Prévois la place : l'image fait la **taille de la RAM** (16 Go de RAM, c'est un fichier de 16 Go).
- L'outil modifie lui-même un peu la mémoire en s'exécutant (Locard, encore) : c'est un coût accepté et documenté.

**Analyser la mémoire.** C'est le domaine de **Volatility 3**, un outil open source écrit en Python, qui s'utilise sur la machine d'analyse avec des modules (*plugins*) : `windows.pslist` (les processus tels que Windows les liste), `windows.psscan` (les structures de processus trouvées en balayant toute la mémoire), `windows.netscan` (les connexions), `windows.cmdline` (les lignes de commande), `windows.malfind` (les signes d'injection de code). La technique classique illustre parfaitement la limite de PowerShell : un processus présent dans `psscan` mais absent de `pslist` a peut-être été **caché**.

> **Ce qui reste même après l'extinction.** Deux fichiers sur disque contiennent des fragments de mémoire : `pagefile.sys` (la mémoire paginée) et `hiberfil.sys` (l'image de mise en veille prolongée). Même une machine éteinte n'a donc pas tout oublié — mais on ne compte pas dessus.

## 🔴 Bonus

### Collecter à distance, sans exposer ses identifiants

Avec le remoting (Ch.29), tu peux collecter sans ouvrir de session interactive sur la machine suspecte :

```powershell
$processus = Invoke-Command -ComputerName SRV01 -ScriptBlock {
    Get-CimInstance Win32_Process |
        Select-Object ProcessId, ParentProcessId, Name, CommandLine, CreationDate
}
$processus | Export-Csv "E:\Collecte_SRV01\01_processus.csv" -NoTypeInformation -Encoding UTF8
```


Ce n'est pas qu'une question de confort. Se connecter en **RDP** avec un compte d'administrateur du domaine sur une machine compromise est une erreur classique : la connexion interactive laisse des **identifiants réutilisables en mémoire**, exactement là où l'attaquant peut aller les voler. Une connexion **réseau** comme celle du remoting (avec Kerberos, sans délégation) n'en laisse pas. Tu verras au Ch.37 comment ces deux types de connexion se distinguent dans les journaux.

## ❌ Erreur classique

```powershell
# Redémarrer « pour voir si ça règle le problème »
Restart-Computer     # ❌ mémoire, processus et connexions perdus à jamais

# Écrire la collecte sur le disque suspect
$dest = "C:\collecte"    # ❌ peut écraser des fichiers effacés encore récupérables
$dest = "E:\collecte"    # ✅ support externe

# Copier les journaux à la main
Copy-Item C:\Windows\System32\winevt\Logs\Security.evtx E:\   # ❌ fichier en cours d'utilisation
wevtutil epl Security E:\Security.evtx                         # ✅ export par le service

# Calculer les empreintes pendant que le transcript tourne
# ❌ journal_intervention.txt change encore → empreinte fausse dès la fin du script
# ✅ Stop-Transcript AVANT le manifeste

# Conclure de la collecte à chaud qu'« aucun processus n'est caché »
# ❌ elle passe par les API de Windows, qu'un rootkit peut tromper → image mémoire

# Se connecter en RDP avec un compte d'administrateur du domaine sur la machine suspecte
# ❌ tes identifiants restent en mémoire, à portée de l'attaquant (voir Bonus)
```


## 💡 Exercices

**Réflexion :** Classe du plus volatil au moins volatil, en justifiant : le journal System, les connexions TCP établies, une sauvegarde de la veille, le cache DNS, un processus en cours d'exécution.

**Réflexion :** Un collègue t'affirme : « J'ai vérifié avec `Get-Process`, aucun processus suspect, la machine est saine. » Que lui réponds-tu ?

**Guidé :** Sur ton poste (ou CLIENT01), crée un dossier de collecte sur une clé USB ou un second disque. Démarre un transcript, collecte les processus et les connexions TCP, exporte le journal System avec `wevtutil`, arrête le transcript, puis produis le manifeste d'empreintes.

**Autonome :** Écris `Test-EvidenceIntegrity`, qui prend un dossier de collecte, relit son manifeste, recalcule chaque empreinte, et signale trois cas : les fichiers **modifiés**, les fichiers **manquants**, et les fichiers **présents mais absents du manifeste**. Teste-la en modifiant volontairement l'un des CSV.

## 🧩 Mini-projet — `Invoke-LiveResponse.ps1`

Assemble le chapitre en un script de collecte réutilisable :

- Un paramètre `-Destination` obligatoire, et un **refus** si la destination se trouve sur le lecteur système (indice : compare `[System.IO.Path]::GetPathRoot($Destination)` à `$env:SystemDrive`). C'est le Réflexe n°2 du cours, appliqué à l'investigation : on teste avant d'agir.
- Le transcript démarré en toute première commande du script, arrêté avant le manifeste. (Une éventuelle capture mémoire a eu lieu avant, hors du script : voir la séquence.)
- Le contexte (machine, analyste, heure UTC, fuseau), puis la collecte dans l'ordre de volatilité : processus, connexions, cache DNS, cache ARP ; puis la persistance (services, tâches planifiées, clés Run, comme au Ch.34) ; puis l'export des journaux, **y compris celui de Sysmon s'il existe** (`Get-WinEvent -ListLog *Sysmon* -ErrorAction SilentlyContinue`), qu'on utilisera au Ch.37.
- Chaque étape dans son propre `try/catch` : un échec ne doit pas interrompre toute la collecte. C'est la même logique que l'état partiel du Ch.24 : mieux vaut une collecte incomplète et **honnête** (l'échec est noté dans le transcript) qu'aucune collecte.
- Le manifeste SHA-256 en fin de script, et l'affichage de l'empreinte du manifeste.

Tu réutiliseras le dossier produit au Ch.37.

## ✅ Tu sais maintenant...

- Pourquoi intervenir modifie la machine (Locard), et les quatre règles qui en découlent
- Les trois formes d'acquisition : collecte à chaud, image mémoire, image disque
- L'ordre de volatilité, et pourquoi on n'éteint pas une machine compromise **par réflexe** : son sort est une décision, prise selon la menace et la procédure
- Distinguer l'ordre d'acquisition des preuves (la mémoire d'abord) et l'enregistrement de tes actions (carnet, puis transcript)
- Collecter à chaud en PowerShell, sur un support externe, en documentant avec `Start-Transcript`
- Exporter proprement les journaux avec `wevtutil epl`
- Contrôler l'intégrité avec un manifeste d'empreintes SHA-256, et ne pas la confondre avec la chaîne de preuve, qui trace qui a détenu la preuve et quand
- Ce que contient la mémoire vive, pourquoi PowerShell ne suffit pas à l'examiner, et quels outils prennent le relais

## 💬 Questions d'entretien typiques

- **Une machine est compromise : que fais-tu en premier ?** → Rien d'irréversible : on documente et on alerte le responsable de l'incident, qui décide du sort de la machine (l'isoler est le cas le plus fréquent, mais pas automatique). Puis on collecte dans l'ordre de volatilité : la mémoire si une capture est prévue, puis processus et connexions, puis journaux.
- **Pourquoi ne pas éteindre par réflexe ?** → On perdrait tout ce qui ne vit qu'en mémoire : processus, connexions, code malveillant sans fichier, clés. L'extinction peut se justifier (un rançongiciel en train de chiffrer, par exemple), mais c'est une décision, pas un réflexe.
- **Comment montrer qu'une preuve n'a pas été altérée ?** → Par une empreinte SHA-256 calculée au plus tôt après la collecte et consignée dans un manifeste, qu'on recalcule à chaque étape. Elle prouve que le fichier n'a pas changé depuis ce calcul, pas davantage.
- **Une empreinte suffit-elle à établir la chaîne de preuve ?** → Non. Elle garantit l'intégrité du contenu ; la chaîne de preuve exige en plus la traçabilité (qui a collecté, détenu, consulté et transmis la preuve, quand et où), consignée dans un registre.
- **Qu'est-ce que l'ordre de volatilité ?** → Collecter d'abord ce qui disparaît le plus vite (mémoire, processus, réseau), en dernier ce qui dure (disque, sauvegardes). Référence : RFC 3227.
- **Pourquoi ne pas se connecter en RDP sur une machine compromise avec un compte d'admin du domaine ?** → La connexion interactive laisse des identifiants réutilisables en mémoire ; on préfère une connexion réseau (remoting) ou un compte dédié à l'intervention.

---
