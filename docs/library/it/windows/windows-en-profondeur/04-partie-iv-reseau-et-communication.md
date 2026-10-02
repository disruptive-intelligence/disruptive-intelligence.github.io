---
title: Partie IV — Réseau et communication
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

---


## Chapitre 14 — Stack réseau Windows et APIs

L'architecture réseau (Winsock → AFD.sys → TCP/IP stack → NDIS → driver réseau). Le **WFP** (Windows Filtering Platform — framework de filtrage sur lequel repose le Windows Firewall et certains EDR). Les APIs réseau (WinHTTP, WinINet — les APIs que les malwares utilisent pour communiquer ; URLDownloadToFile, HttpOpenRequest → détection par API monitoring et Sysmon 3). Le **firewall Windows** (profils Domain/Private/Public, règles entrantes/sortantes — un firewall host correctement configuré limite le mouvement latéral et bloque le C2 sortant sur les ports non standards). Les connexions réseau (netstat -anob, Get-NetTCPConnection, TCPView — ce que l'investigateur vérifie en premier lors du triage : quels processus communiquent avec quelles IP ?).

---


## Chapitre 15 — SMB, partages et accès distant

SMB (Server Message Block — port 445). Les versions : SMBv1 = EternalBlue → **désactiver immédiatement**, SMBv2 minimum, SMBv3 chiffré recommandé. Les partages administratifs (C$, ADMIN$, IPC$ — accessibles par les admins locaux → vecteur de mouvement latéral). Les techniques d'accès distant et leur profil de détection : **PsExec** (crée un service temporaire PSEXESVC — Event 7045 + 4624 type 3 + Sysmon 1 avec psexesvc.exe en child de services.exe), **WMI** (Event 4624 type 3 + 4688 avec parent wmiprvse.exe sur la cible), **WinRM** (PowerShell Remoting — Event 4624 type 3 + 4688 wsmprovhost.exe), **RDP** (Event 4624 type 10 — connexion interactive à distance), **DCOM** (appel COM à distance — mmc.exe, excel.exe comme parent de processus suspect), **schtasks** (tâche planifiée à distance — Event 4698 sur la cible). Chaque technique a un profil de détection différent — connaître ces profils est une compétence SOC fondamentale.

---


## Chapitre 16 — Résolution de noms et protocoles dangereux

DNS (résolution normale, DNS cache — artefact forensic volatil, DNS query logging — Sysmon 22). Les protocoles de fallback dangereux : **LLMNR** (Link-Local Multicast Name Resolution — port 5355, broadcast — Responder capture les hashes NTLM → désactiver par GPO), **NBT-NS** (NetBIOS Name Service — port 137 — même risque → désactiver), **mDNS** (Multicast DNS — port 5353). **WPAD** (Web Proxy Auto-Discovery — le client cherche un serveur proxy via DHCP puis DNS puis LLMNR → l'attaquant se déclare proxy et intercepte le trafic → désactiver par GPO). Fil rouge : LLMNR et NBT-NS sont actifs sur le réseau de Valtec, mais dans ce cas l'accès initial est par phishing — Léa note la vulnérabilité dans ses recommandations.

---
