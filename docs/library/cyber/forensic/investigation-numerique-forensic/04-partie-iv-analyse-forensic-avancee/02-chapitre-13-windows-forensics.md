---
title: Chapitre 13 — Windows forensics
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie IV — Analyse forensic avancée
  - index.md
---

activité utilisateur, navigateur et mouvement latéral

*Ce chapitre couvre ce que l'utilisateur (ou l'attaquant se faisant passer pour l'utilisateur) a fait sur la machine : quels fichiers ont été accédés, quels dossiers ont été navigués, quels sites ont été visités, et comment l'attaquant s'est déplacé vers d'autres machines.*

## 13.1 Artefacts d'activité utilisateur

**ShellBags** (stockés dans NTUSER.DAT et UsrClass.dat) : enregistrent chaque dossier navigué dans l'explorateur Windows, avec les dates d'accès et les préférences d'affichage — même si le dossier a été supprimé depuis, la trace persiste dans les ShellBags. Pour le forensic, ils révèlent les répertoires explorés par l'attaquant (partages réseau, dossiers sensibles, lecteurs USB). Outil : **SBECmd** — `SBECmd.exe -d "C:\Users\JMallet" --csv output/`.

**LNK files** (raccourcis, `.lnk`, dans `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\`) : créés automatiquement quand un fichier est ouvert. Chaque fichier .lnk contient le chemin complet du fichier cible (y compris les chemins réseau UNC — `\\SRV-RD-01\projets\`), le volume d'origine (nom du volume, numéro de série — identifie les clés USB), les timestamps MAC du fichier cible, et la taille du fichier. Outil : **LECmd** — `LECmd.exe -d "C:\Users\JMallet\AppData\Roaming\Microsoft\Windows\Recent" --csv output/`.

**Jump Lists** (dans `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\`) : listes de fichiers récemment ouverts par application. Chaque application a son propre fichier Jump List, identifié par un AppID. Les Jump Lists contiennent les mêmes informations que les LNK files mais organisées par application. Outil : **JLECmd** — `JLECmd.exe -d "AutomaticDestinations" --csv output/`.

**UserAssist** (dans NTUSER.DAT, clé `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`) : enregistre les programmes exécutés via l'interface graphique (GUI) avec un compteur d'exécutions et le dernier timestamp. Les données sont encodées en ROT13 (obfuscation triviale, pas du chiffrement).

## 13.2 Browser forensics

Les navigateurs web sont une source d'évidence massive et souvent sous-exploitée. Chrome, Firefox, et Edge stockent leurs données dans des bases SQLite accessibles dans le profil utilisateur.

**Chrome** (`C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\`) : `History` (historique de navigation et de téléchargements), `Cookies` (cookies de session — peuvent révéler des accès à des services cloud avec credentials volées), `Login Data` (credentials enregistrés — chiffrés avec DPAPI), `Web Data` (formulaires auto-remplies), `Preferences` (extensions installées — certaines extensions peuvent être malveillantes), `Favicons` (icônes des sites visités — preuve de visite même si l'historique a été effacé). Outil de parsing : **Hindsight** (open source) — `hindsight.py -i "C:\Users\JMallet\AppData\Local\Google\Chrome\User Data\Default" -o output/`.

**Firefox** (`C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\`) : `places.sqlite` (historique et favoris), `cookies.sqlite`, `formhistory.sqlite`, `logins.json` + `key4.db` (credentials). **Edge** (Chromium-based) utilise la même structure que Chrome mais dans un chemin différent.

L'historique de navigation peut révéler la préparation de l'attaque (l'attaquant a recherché des informations sur l'infrastructure de NovaPharma depuis le poste compromis), l'accès à des services de transfert de fichiers (mega.nz, transfer.sh), ou la consultation de forums underground.

## 13.3 Artefacts de mouvement latéral

Le mouvement latéral est la progression de l'attaquant d'un système à un autre au sein du réseau. Chaque technique de mouvement latéral laisse des artefacts spécifiques — tant sur la machine source que sur la machine destination.

**PsExec** : sur la machine destination, PsExec crée un service temporaire `PSEXESVC` (visible dans les Event Logs : Event ID 7045 — installation de service). Le binaire `PSEXESVC.exe` est copié dans `C:\Windows\` (visible dans la MFT et potentiellement dans le Prefetch). L'Event Log Security montre une authentification réseau (4624 type 3) suivie d'un accès au partage ADMIN$ (Event ID 5140). Sur la machine source, le Prefetch de `PSEXEC.EXE` confirme l'exécution avec le timestamp.

**RDP** : les connexions RDP laissent des traces riches. Sur la machine destination : Event IDs 21/22/25 dans le canal `TerminalServices-RemoteConnectionManager` (connexion établie, réussie, reconnexion), Event ID 4624 type 10 (logon RDP) dans Security, et le **RDP Bitmap Cache** (`C:\Users\<user>\AppData\Local\Microsoft\Terminal Server Client\Cache\`) qui contient des fragments visuels de la session RDP — potentiellement des captures d'écran de ce que l'attaquant a vu. L'outil **bmc-tools** ou **rdpieces** peut reconstituer des images à partir du cache bitmap. Sur la machine source : la clé registre `HKCU\Software\Microsoft\Terminal Server Client\Default` et les fichiers `.rdp` dans le profil listent les connexions RDP récentes.

**WMI** (Windows Management Instrumentation) : l'exécution de commandes à distance via WMI est plus discrète que PsExec. Les traces : Event ID 4688 (création de processus) avec `wmiprvse.exe` comme parent sur la machine destination, et les logs WMI dans `Microsoft-Windows-WMI-Activity/Operational`.

**SMB / Accès aux partages réseau** : Event IDs 5140 (accès à un partage) et 5145 (vérification d'accès à un fichier/dossier partagé — plus granulaire, nécessite l'activation de l'audit des partages). Ces événements sont essentiels pour tracer quels fichiers l'attaquant a accédé sur les serveurs de fichiers.

**Artefacts USB** : les connexions USB sont tracées dans le registre (SYSTEM\CurrentControlSet\Enum\USBSTOR), dans les logs PnP (Event ID 20001, 20003), et dans `C:\Windows\inf\setupapi.dev.log`. Ces artefacts identifient le type de périphérique, son numéro de série, les dates de première et dernière connexion — essentiels dans les investigations d'insider threat.

## 13.4 Fil rouge — MUSIC BOX : mouvement latéral détecté

> **🔬 MUSIC BOX — Épisode 12**
>
> L'analyse des artefacts de mouvement latéral de WKS-RD-047 révèle les connexions vers d'autres machines.
>
> **LNK files (LECmd) :** 15 fichiers .lnk pointent vers des chemins réseau `\\SRV-RD-01\projets\molecule-np427\` — l'attaquant a navigué dans les fichiers de recherche depuis le poste compromis.
>
> **RDP (registre + Event Logs) :** le registre montre une connexion RDP récente vers `SRV-RD-01` (le serveur Linux — l'accès SSH est possible via RDP Gateway ? Non — investigation complémentaire : l'attaquant a utilisé PuTTY, dont le Prefetch confirme l'exécution). Les fichiers `.rdp` du profil de l'attaquant montrent aussi une connexion vers `DC01` (le contrôleur de domaine).
>
> **PsExec :** le Prefetch confirme l'exécution de PsExec sur WKS-RD-047. Les Event Logs de DC01 (collectés au Ch.8) montrent la création du service PSEXESVC (Event ID 7045) à J-14 — c'est le moment où l'attaquant a utilisé PsExec pour exécuter le DCSync sur DC01.

---
