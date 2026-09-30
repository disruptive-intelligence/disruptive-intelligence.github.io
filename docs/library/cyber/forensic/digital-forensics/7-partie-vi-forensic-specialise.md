---
title: PARTIE VI — FORENSIC SPÉCIALISÉ
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
chapter: 7
chapters: 9
---

---

### Chapitre 22 — Email forensics et messagerie

L'email est le vecteur d'intrusion initiale le plus courant (phishing, spearphishing). L'analyse des en-têtes complets (champs `Received` lus de bas en haut pour tracer le chemin de l'email), la vérification SPF/DKIM/DMARC (le domaine d'envoi est-il légitime ?), l'extraction de la pièce jointe pour analyse malware (Ch.18), et l'identification du domaine d'usurpation (typosquatting, homoglyphes) constituent le workflow standard.

Les formats de boîtes mail (PST pour Outlook, MBOX, EML), les outils d'extraction (pffexport, Kernel PST Viewer, Autopsy module email), et l'indexation full-text pour la recherche dans des boîtes de dizaines de milliers d'emails sont détaillés.

La messagerie instantanée (Teams, Slack, Signal, WhatsApp) devient une source forensic croissante. Teams stocke des bases SQLite locales et des logs Azure. Slack est exportable via l'API workspace. Signal et WhatsApp utilisent des bases SQLite chiffrées sur le terminal mobile — l'accès nécessite l'acquisition du terminal (Ch.23).

#### 22.1 Fil rouge — MUSIC BOX : l'email de spearphishing

> **🔬 MUSIC BOX — Épisode 19**
>
> L'email de spearphishing est retrouvé dans la boîte PST du Dr. Mallet. Headers : envoyé depuis un serveur compromis en Europe de l'Est (IP dans les Received). Domaine : `novapharma-partners.com` (typosquatting du domaine légitime `novapharma-partner.com`). SPF : pass (le domaine de typosquatting avait un SPF configuré — l'attaquant a préparé son infrastructure). Pièce jointe : `Rapport_collaboration_Q3.docx`. Analyse olevba : macro VBA obfusquée qui télécharge le RAT depuis un site WordPress compromis via certutil. Le vecteur initial est formellement identifié et documenté.

---

### Chapitre 23 — Mobile forensics

Le smartphone est un terminal d'une richesse informationnelle exceptionnelle : appels, SMS, emails, localisation GPS continue, photos géolocalisées, applications de messagerie, historique de navigation, credentials stockés. Mais les protections modernes (chiffrement intégral, Secure Enclave/TEE, verrouillage biométrique) rendent l'acquisition complexe.

**iOS forensics :** trois niveaux d'acquisition (logique via backup iTunes/libimobiledevice, filesystem via exploitation de vulnérabilités comme checkm8, physique — de plus en plus rare sur les modèles récents). La distinction AFU (After First Unlock — clés en mémoire, extraction possible) vs BFU (Before First Unlock — clés protégées, accès très limité) est fondamentale. Les données iCloud (backups, photos, messages) sont accessibles via les credentials ou par réquisition Apple.

**Android forensics :** plus de flexibilité d'accès. ADB (si activé), JTAG, chip-off (invasif), mode EDL (Qualcomm). Les bases SQLite contiennent l'essentiel des données applicatives.

**Outils :** Cellebrite UFED (référence forces de l'ordre), Magnet AXIOM, ALEAPP/iLEAPP (open source pour le parsing des artefacts). **Artefacts clés :** SMS/appels, bases de données messagerie (WhatsApp `msgstore.db`, Signal `signal.db`, Telegram `cache4.db`), photos EXIF (géolocalisation), historique de localisation, WiFi SSIDs connectés.

---

### Chapitre 24 — Anti-forensics : comprendre et détecter

L'anti-forensics regroupe les techniques de l'attaquant pour empêcher, ralentir ou tromper l'investigation. C'est un jeu du chat et de la souris : chaque technique anti-forensic a des contremesures, et les traces de l'anti-forensics elle-même sont souvent révélatrices.

**Destruction de données :** wiping sécurisé (SDelete, shred, DBAN), TRIM automatique sur SSD, destruction physique. Contremesure : le $UsnJrnl conserve la trace des fichiers supprimés, les traces de SDelete sont visibles dans la MFT (fichiers temporaires caractéristiques créés par l'outil).

**Dissimulation :** chiffrement (volumes VeraCrypt), stéganographie, ADS NTFS, rootkits. Contremesure : les ADS sont détectables avec `dir /r` ou les outils forensic, les rootkits sont détectables par l'analyse mémoire (Volatility malfind, modscan).

**Falsification :** timestomping (modification des timestamps $SI — détectable par comparaison avec $FN), falsification de logs (modification ou suppression sélective — détectable par les lacunes dans les séquences d'Event ID et par les logs centralisés dans le SIEM), planted evidence (fausses preuves — détectable par les incohérences dans la timeline).

**Évasion :** fileless malware (invisible au disk forensics — détectable uniquement par memory forensics), LOLBins (utilisation de binaires légitimes — certutil, PowerShell, bitsadmin — détectable par les Event Logs PowerShell et Sysmon), script-based attacks (détectables uniquement si le script block logging est activé).

**Détection de l'anti-forensics :** l'anti-forensics parfait est rare. L'Event ID 1102 (Security Log cleared) trahit le nettoyage de logs. Les incohérences de timestamps ($SI vs $FN) trahissent le timestomping. Le pagefile.sys et le hiberfil.sys conservent des fragments de mémoire anciens. Et les logs centralisés dans un SIEM préservent les événements même quand l'attaquant efface les logs locaux.

#### 24.1 Fil rouge — MUSIC BOX : l'anti-forensics détecté

> **🔬 MUSIC BOX — Épisode 20**
>
> L'attaquant a tenté de couvrir ses traces. **Timestomping détecté :** les timestamps $SI de 47 fichiers dans `/projets/molecule-np427/` montrent des dates de création en 2022, mais les timestamps $FN indiquent 2024 (détecté via MFTECmd). **Log clearing :** Event ID 1102 détecté sur DC01 à J-1, 03h42 — le Security Log a été effacé. Mais les événements antérieurs étaient centralisés dans le SIEM Splunk — l'anti-forensics a échoué. **Suppression de fichiers :** 47 fichiers supprimés dans le répertoire de recherche — mais le $UsnJrnl conserve les noms, dates, et comptes associés aux suppressions.

---

### Chapitre 25 — Investigation des mécanismes de persistance

Ce chapitre est une référence transversale : l'éradication post-incident (cours IR, Ch.27) nécessite d'avoir identifié TOUS les mécanismes de persistance de l'attaquant. Le forensicien doit savoir les trouver.

**Persistance Windows — registre :** Run/RunOnce, Winlogon (Userinit, Shell), Image File Execution Options (Debugger), AppInit_DLLs, et les clés de registre de services (voir Ch.12 pour le détail). **Persistance Windows — système :** Scheduled Tasks (Event ID 4698, fichiers XML dans `C:\Windows\System32\Tasks\`), services Windows (Event ID 7045, clé registre `HKLM\SYSTEM\CurrentControlSet\Services`), WMI Event Subscriptions (persistance via des événements WMI — très discrète, détectable via `Get-WMIObject -Namespace root\Subscription -Class __EventConsumer`), DLL hijacking (une DLL malveillante est placée dans un répertoire prioritaire du DLL search order), COM object hijacking (redirection d'un objet COM légitime vers un exécutable malveillant), et Startup folder (`C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`).

**Persistance Linux :** crontab (utilisateur et système), systemd timers, scripts dans `/etc/init.d/`, modification de `.bashrc`/`.profile` (exécution de code au login), SSH authorized_keys (ajout de clé non autorisée — le mécanisme le plus courant), modules noyau malveillants (chargés via insmod), et LD_PRELOAD (injection de bibliothèque partagée).

**Persistance cloud :** app registrations avec secrets (OAuth tokens persistants qui survivent au reset du mot de passe), service principals avec des permissions excessives, et IAM users/roles avec des access keys — tous survivent aux resets de mots de passe des comptes utilisateur classiques.

Pour chaque mécanisme : comment l'attaquant l'installe, comment le forensicien le détecte, quels artefacts il laisse (Event Logs, registre, système de fichiers), et comment l'éradiquer. L'outil **Autoruns** (Sysinternals) et les hunts Velociraptor sont les méthodes les plus complètes pour inventorier les points de persistance sur une machine Windows.

---
