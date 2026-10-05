---
title: "Connexions et RDP"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md
  - library/it/windows/windows-en-profondeur/index.md
---

# Connexions et RDP

Qui s'est connecté, quand, depuis où, et vers quelles machines un poste compromis a rebondi. Côté machine **cible**, on lit ce qui est arrivé ; côté machine **source**, ce qui est parti.

Les incontournables : `Get-WinEvent` · `EvtxECmd` · `4624` · `1149` · `261` · `1102` · `Terminal Server Client`
{ .kw-cs-top }

## Ouvertures de session

### Retrouver les ouvertures de session, réussies ou non

- **Où :** `C:\Windows\System32\winevt\Logs\` ; journal `Security` (4624 réussite, 4625 échec, 4672 droits
  d'administrateur, 4688 processus créé, 4720 compte créé, 1102 journal effacé) ; RDP dans
  `TerminalServices-RemoteConnectionManager` (1149) et `TerminalServices-LocalSessionManager` (21, 24, 25).
- **Ce qu'il dit :** qui, quand, depuis quelle adresse, avec quel type de connexion (2 locale, 3 réseau,
  10 RDP).
- **Pour aller plus loin :** la note [Analyse des journaux d'événements Windows](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/index.md).

```powershell title="Commande"
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} -MaxEvents 50 | Format-Table TimeCreated, Id, Message -Wrap
```

```powershell title="Exemple"
EvtxECmd.exe -d E:\collecte\C\Windows\System32\winevt\Logs --csv E:\analyse\evtx   # tous les journaux, en un CSV normalisé
```

## RDP sur la machine cible

Les entrées suivantes viennent de la fiche [Journaux et événements](../../../windows/fondamentaux/logs.md) : elles n'y sont écrites qu'une fois.

![[cheatsheets/windows/fondamentaux/logs#Retrouver les connexions RDP reçues]]

![[cheatsheets/windows/fondamentaux/logs#Repérer les connexions RDP et les échecs d'authentification]]

## RDP depuis la machine source

![[cheatsheets/windows/fondamentaux/logs#Savoir vers quelles machines un poste s'est connecté en RDP]]

### Retrouver les serveurs RDP contactés depuis un poste (registre et fichiers)

- **Où :** dans `NTUSER.DAT` de l'utilisateur, `Software\Microsoft\Terminal Server Client\Default` (les dernières
  connexions, `MRU0` à `MRU9`) et `…\Terminal Server Client\Servers\<hôte>` (un sous-dossier par serveur, avec le
  nom d'utilisateur utilisé) ; le fichier `Documents\Default.rdp` ; la Jump List de `mstsc.exe` ; le cache
  d'images `AppData\Local\Microsoft\Terminal Server Client\Cache\`.
- **Ce qu'il dit :** vers quelles machines l'utilisateur s'est connecté en RDP, et sous quel compte — même
  quand le journal `RDPClient` a été vidé ou a tourné.
- **Limites :** l'utilisateur peut effacer l'historique de `mstsc` ; le cache d'images ne donne que des
  fragments d'écran, à reconstituer avec un outil dédié (bmc-tools).

```powershell title="Commande"
reg query "HKCU\Software\Microsoft\Terminal Server Client\Default"     # dernières destinations (machine vivante)
reg query "HKCU\Software\Microsoft\Terminal Server Client\Servers" /s  # un sous-dossier par serveur, avec UsernameHint
```

```powershell title="Exemple"
RECmd.exe -f "E:\collecte\C\Users\alice\NTUSER.DAT" --kn "Software\Microsoft\Terminal Server Client" --csv E:\analyse\rdp-client
```

??? example "Sortie"
    ```text
    HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers\192.168.1.30
        UsernameHint    REG_SZ    MERIDIAN\adm.martin
    ```

Pour comprendre : [Logs côté machine source RDP](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#logs-cote-machine-source-rdp)
{ .kw-cs-meta }

## Reconstituer un rebond RDP

Sur la cible : **261** (connexion TCP) → **1149** (authentification réussie) → **4624 type 10** (session) →
**21/25** (session ouverte ou reconnectée). Sur la source : **4648** (identifiants explicites), **1102** du client
RDP, registre `Terminal Server Client`. Chaque destination trouvée sur un poste compromis devient la cible
suivante de l'investigation.

```text
Poste A (source)                      Serveur B (cible)
4648 + RDPClient 1102  ───RDP───▶   261 → 1149 → 4624 type 10 → LocalSessionManager 21/25
Terminal Server Client\Servers\B          puis, depuis B : 4648 + 1102 vers C …
```

Pour comprendre : [Investigation du lateral movement via RDP](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#investigation-du-lateral-movement-via-rdp) · [Corrélation RDP recommandée](../../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/05-mouvement-lateral-et-rdp.md#correlation-rdp-recommandee)
{ .kw-cs-meta }
