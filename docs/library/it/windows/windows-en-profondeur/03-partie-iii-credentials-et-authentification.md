---
title: Partie III — Credentials et authentification
source: IT/02 Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - index.md
---

*Où sont les secrets, comment ils sont volés, et comment les protéger.*

---


## Chapitre 11 — Stockage des credentials : SAM, SYSTEM, LSASS, DPAPI

Le **SAM** (Security Account Manager — hashes NTLM des comptes locaux, chiffré avec la boot key stockée dans SYSTEM ; SAM sans SYSTEM = coffre sans clé). Le **NTDS.dit** (base AD sur les DC — hashes de TOUS les comptes du domaine — renvoi cours AD). La **mémoire lsass.exe** (le processus d'authentification — contient en mémoire les tickets Kerberos, hashes NTLM, et parfois mots de passe en clair si WDigest activé ; c'est ce que Mimikatz extrait via sekurlsa::logonpasswords). Les **LSA Secrets** (HKLM\SECURITY\Policy\Secrets — mots de passe des comptes de service en clair, clés de chiffrement, mot de passe machine). Le **DPAPI** (Data Protection API — chiffre les secrets utilisateur : mots de passe Chrome/Edge, credentials WiFi, Vault ; la master key est dérivée du mot de passe de l'utilisateur ; la domain backup key sur les DC déchiffre TOUTES les master keys du domaine). Les **DCC2** (Domain Cached Credentials — hash dérivé du MdP domaine, mis en cache pour le login offline — par défaut les 10 derniers logons ; crackable avec hashcat -m 2100, plus lent que NTLM mais faisable). Les **GPP** (Group Policy Preferences — cpassword chiffré avec une clé publiée par Microsoft → déchiffrement trivial ; corrigé MS14-025 mais les GPP historiques restent souvent).

---


## Chapitre 12 — Extraction de credentials

techniques SAM/SYSTEM/LSASS et détection

L'extraction **SAM + SYSTEM** : reg save (commande native — admin local, Event 4688 command line), Volume Shadow Copy (plus discrète), backup wbadmin (offline), accès physique/Live USB (hors OS), Mimikatz lsadump::sam (détecté par EDR/AV). L'extraction **NTDS.dit** : ntdsutil, VSS, DCSync (renvoi cours AD). Le **dump mémoire LSASS** — 7 techniques avec traces et détection : Task Manager (Sysmon 10, fichier .dmp), comsvcs.dll (LoLBin — rundll32 comsvcs.dll,MiniDump, Sysmon 10 + 4688), procdump (Sysmon 10), Mimikatz sekurlsa::logonpasswords (signature AV, behavior EDR), nanodump/dumpert (contournement EDR — plus difficile à détecter), duplication de handle (subtil), et SSP injection (DLL chargée dans lsass — Sysmon 7). Ce qu'on trouve dans un dump LSASS : hashes NTLM (toujours sauf Credential Guard), tickets Kerberos (si session domaine), MdP en clair (si WDigest activé — UseLogonCredential=1), clés DPAPI master keys. Les LSA Secrets (secretsdump, Mimikatz lsadump::secrets — mots de passe de services en clair). Le DPAPI (master key déchiffrée avec le hash NTLM → accès Chrome/WiFi/Vault). Les DCC2 (secretsdump, Mimikatz lsadump::cache).

La **détection** : Sysmon 10 sur lsass.exe (processus source inhabituel), 4688/Sysmon 1 command line reg save sur hives sensibles, 7036+4688 VSS suspecte, Sysmon 7 DLL chargée dans lsass, Sysmon 13 modification registre SSP, Event 4662 pour DCSync.

---


## Chapitre 13 — Protections des credentials et hardening

**Credential Guard** (VBS — Virtualization-Based Security — isole les hashes NTLM + tickets Kerberos hors de lsass dans un environnement virtuel protégé par l'hyperviseur ; Mimikatz ne peut plus les extraire ; ne protège PAS les DCC2, ni SAM, ni LSA Secrets). **RunAsPPL** (Protected Process Light — protège lsass contre les injections de processus non protégés ; contournable avec un driver signé ou exploit kernel — moins fort que Credential Guard mais plus compatible). Désactiver WDigest (UseLogonCredential=0 — par défaut depuis 2012 R2, vérifier). **LAPS** (mot de passe admin local unique et roté par machine — élimine le PtH via admin local identique sur tout le parc). **Remote Credential Guard** (les credentials ne sont pas envoyées au serveur RDP — protection contre le dump sur le serveur de destination). **Protected Users** (groupe AD — pas de cache NTLM, pas de délégation, TGT 4h — renvoi cours AD). Réduire les DCC2 (GPO Interactive logon: Number of previous logons to cache = 1 ou 0). **BitLocker** (chiffrement disque — protège SAM/SYSTEM/NTDS.dit contre l'accès offline via Live USB ou vol de disque).

---
