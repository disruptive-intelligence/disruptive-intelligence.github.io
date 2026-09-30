---
title: 8) Réponses flash — Synthèse ultra rapide
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

| Thème | Réponse flash |
|-------|---------------|
| **Moindre privilège** | Uniquement les droits nécessaires, rien de plus |
| **Défense en profondeur** | Plusieurs couches de sécurité superposées |
| **TCP vs UDP** | TCP = connexion, fiable. UDP = sans connexion, rapide |
| **DNS** | Nom → IP. Cache → récursif → racine → TLD → autoritaire. Port 53/UDP |
| **HTTPS** | HTTP + TLS. Handshake → certificat → ECDHE → clé session → AES-GCM |
| **Hash** | Empreinte fixe, irréversible, déterministe. SHA-256 sûr, MD5 cassé |
| **Sym vs Asym** | Sym = même clé, rapide (AES). Asym = paire clés, lent (RSA). Hybride = les deux |
| **Switch vs Routeur** | Switch = L2, MAC, même réseau. Routeur = L3, IP, entre réseaux |
| **ARP** | IP → MAC en local. Risque = ARP spoofing → MITM |
| **VLAN** | Segmentation logique, domaines de broadcast séparés |
| **Container vs VM** | Container = partage kernel, léger. VM = OS complet, isolation forte |
| **RAID 0/1/5/6/10** | 0=perf. 1=miroir. 5=parité(1 disque). 6=double parité. 10=miroir+stripe |
| **NAS vs SAN** | NAS = fichiers (SMB/NFS). SAN = blocs (FC/iSCSI) |
| **SIEM** | Centralise logs, corrèle, détecte, investigue |
| **IOC** | Artefact de compromission (hash, IP, domaine). Fragile, facile à changer |
| **Phases IR (NIST)** | Préparation → Détection/Analyse → Confinement/Éradication/Restauration → Post-Incident |
| **Ransomware : premières actions** | Confiner, NE PAS éteindre, protéger les backups, scoper |
| **Persistence Windows** | Run keys, services, tasks, DLL hijack, COM hijack, WMI, Winlogon |
| **Persistence Linux** | Cron, systemd, init.d, .bashrc, authorized_keys, modules kernel |
| **Mouvement latéral** | PtH, PsExec, WMI, WinRM, RDP, schtasks — avec credentials volés |
| **SAM + SYSTEM** | SAM = hashes chiffrés. SYSTEM = Boot Key pour déchiffrer |
| **Arbre processus Windows** | System → smss → csrss + wininit → services → svchost. Vérifier parent, chemin, instances, user |
| **LOLBin** | Binaire légitime détourné (certutil, rundll32). Détection = Sysmon + command line |
| **Hardening AD top 5** | Audit Policy, LAPS, séparation comptes, SMB signing, désactiver LLMNR |
| **Kerberoasting** | TGS pour SPN → crack offline. Défense = gMSA, 25+ chars, AES |
| **Forward Secrecy** | ECDHE, clés éphémères. Compromise future ≠ déchiffrement du passé |
| **IPsec vs SSL VPN** | IPsec = couche 3, accès réseau complet. SSL = couche 7, accès applicatif |
| **DNSSEC/DoH/DoT** | DNSSEC = intégrité. DoT/DoH = confidentialité. Complémentaires |
