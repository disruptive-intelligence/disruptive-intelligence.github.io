---
title: "Démarrage, chiffrement et périphériques"
cours:
  - library/it/windows/windows-en-profondeur/index.md
---

# Démarrage, chiffrement et périphériques

Protéger la machine avant même Windows et quand elle quitte le bureau : démarrage UEFI sécurisé, puce TPM, disque chiffré par BitLocker, micrologiciel verrouillé et à jour, supports amovibles sous contrôle.

Les incontournables : `Confirm-SecureBootUEFI` · `Get-Tpm` · `msinfo32` · `manage-bde -status` · `Get-BitLockerVolume`
{ .kw-cs-top }

## Le principe

```text
UEFI (Secure Boot) → bootmgr → winload.exe → noyau → … → ouverture de session
```

| Mécanisme | Rôle |
|---|---|
| UEFI + GPT | Base moderne, nécessaire aux protections suivantes |
| Secure Boot | Vérifie la signature de chaque composant de démarrage |
| Measured Boot + TPM | Enregistre des mesures d'intégrité dans le TPM, vérifiables à distance |
| ELAM (*Early Launch Anti-Malware*) | Pilote antimalware chargé avant les autres pilotes |
| BitLocker (avec TPM) | Le disque ne se déchiffre que si la chaîne de démarrage est intacte |

Un implant qui s'exécute avant le système (*bootkit*) passe sous l'EDR : Secure Boot à jour, micrologiciel à jour et Measured Boot sont la défense.

Pour comprendre : [Windows en profondeur, ch. 2 (le processus de démarrage)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/02-chapitre-2-le-processus-de-demarrage.md#22-proteger-la-chaine-de-demarrage)
{ .kw-cs-meta }

## Démarrage

### Vérifier que le poste démarre en UEFI avec Secure Boot

```powershell title="Vérifier"
Confirm-SecureBootUEFI   # True : Secure Boot actif ; False : désactivé ; erreur : démarrage BIOS hérité
```

```bat title="Exemple"
msinfo32   :: « Mode BIOS : UEFI » et « État du démarrage sécurisé : Activé »
```

Un poste en mode BIOS hérité (MBR) ou Secure Boot coupé perd aussi Credential Guard, HVCI et BitLocker avec TPM dans leur forme la plus solide. Les certificats Microsoft de Secure Boot émis en 2011 expirent en 2026 (KEK et UEFI CA en juin, Windows Production PCA le 19 octobre) : un poste qui n'a pas reçu les certificats 2023 continue de démarrer, mais ne reçoit plus les futures protections de la chaîne de démarrage.

Pour comprendre : [MCS, ch. 3.8 (micrologiciels et chaîne de démarrage)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/01-partie-i-fondations-socle-technique-et-maintenabil/03-chapitre-3-socle-technique-2.md#38-micrologiciels-objets-connectes-et-chaine-de-demarrage) — Ajout hors cours : `Confirm-SecureBootUEFI` et la lecture de `msinfo32`
{ .kw-cs-meta }

### Vérifier la puce TPM

Le TPM garde les clés de BitLocker et les mesures du démarrage ; Credential Guard s'appuie dessus.

```powershell title="Vérifier"
Get-Tpm | Select-Object TpmPresent, TpmReady, TpmEnabled, ManufacturerVersion
```

```bat title="Exemple"
tpm.msc   :: état et version (2.0 attendue)
```

Pour comprendre : [Windows en profondeur, ch. 2.2](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/02-chapitre-2-le-processus-de-demarrage.md#22-proteger-la-chaine-de-demarrage) — Ajout hors cours : `Get-Tpm` et `tpm.msc`
{ .kw-cs-meta }

### Verrouiller le micrologiciel

Sans mot de passe sur l'UEFI, quiconque a la machine en main peut couper Secure Boot ou démarrer sur une clé USB. Mot de passe d'administration du micrologiciel, démarrage sur supports externes désactivé, micrologiciel mis à jour avec les correctifs du constructeur.

Pour comprendre : [Windows en profondeur, ch. 2.3 (persistance avant le système)](../../../library/it/windows/windows-en-profondeur/01-partie-i-architecture-fondamentale/02-chapitre-2-le-processus-de-demarrage.md#23-persistance-avant-et-apres-le-systeme) — Ajout hors cours : mot de passe et démarrage externe
{ .kw-cs-meta }

## Chiffrement

![[cheatsheets/windows/administration/disques#Voir l'état de BitLocker]]

### Chiffrer le disque système avec BitLocker

Sans chiffrement, un disque volé ou un démarrage sur un autre système donne accès à tous les fichiers, et aux ruches SAM, SYSTEM et SECURITY hors ligne. BitLocker avec TPM protège la machine éteinte ; **TPM + PIN** impose en plus une authentification avant le démarrage de Windows (portables, postes sensibles). Il ne protège pas une machine allumée et déverrouillée.

```bat title="Vérifier — les protecteurs du volume"
manage-bde -protectors -get C:   :: console administrateur
```

```text title="GPO"
Modèles d'administration → Composants Windows → Chiffrement de lecteur BitLocker → Lecteurs du système d'exploitation
→ Exiger une authentification supplémentaire au démarrage (TPM + code PIN)
→ Choisir comment les lecteurs du système d'exploitation protégés par BitLocker peuvent être récupérés
  (sauvegarder la clé de récupération dans l'AD DS / Entra ID avant d'activer le chiffrement)
```

Attendu : protecteur `TPM` (ou `TPM And PIN`) et un mot de passe de récupération **sauvegardé ailleurs que sur le poste**. Sans clé de récupération accessible, une mise à jour du micrologiciel peut rendre le disque illisible.

Pour comprendre : [Windows en profondeur, ch. 13.1 (BitLocker)](../../../library/it/windows/windows-en-profondeur/03-partie-iii-credentials-et-authentification.md#131-les-protections-et-ce-quelles-couvrent) · [ch. 27.2 (P1, mesure 13)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#272-p1-sous-trois-mois) · [Architecture et sécurité des systèmes](../../../library/cyber/concepts/architecture-et-securite-des-systemes/index.md) — Ajout hors cours : `manage-bde -protectors` et la GPO
{ .kw-cs-meta }

## Périphériques

### Couper l'exécution automatique des supports amovibles

Une clé USB ou un CD qui lance un programme à l'insertion est un vecteur d'infection classique.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer' -Name NoDriveTypeAutoRun -ErrorAction SilentlyContinue   # 255 : tous les lecteurs
```

```text title="GPO"
Modèles d'administration → Composants Windows → Stratégies d'exécution automatique
→ Désactiver l'exécution automatique → Activé, sur « Tous les lecteurs »
```

Pour comprendre : [Menaces, attaques et malwares](../../../library/cyber/concepts/menaces-attaques-et-malwares/index.md) — Ajout hors cours : toute l'entrée
{ .kw-cs-meta }

### Contrôler les supports de stockage amovibles

Les supports amovibles servent à faire entrer un logiciel malveillant et à sortir des données. Selon le besoin : interdire, n'autoriser que la lecture, ou réserver aux supports de l'entreprise ; dans tous les cas, auditer.

```text title="GPO"
Modèles d'administration → Système → Accès au stockage amovible
→ Toutes les classes de stockage amovible : refuser tout accès     (ou : Disques amovibles : refuser l'accès en écriture)
Paramètres de sécurité → Configuration avancée de la stratégie d'audit → Object Access → Removable Storage (succès + échec)
```

L'audit du stockage amovible (succès et échec) et celui de l'activité Plug-and-Play (succès) font partie de la stratégie d'audit recommandée. Une solution DLP sur le poste peut aller plus loin (bloquer la copie de données sensibles).

Ensuite : [activer la stratégie d'audit](journalisation.md#activer-la-strategie-daudit-avancee) — Pour comprendre : [Sécurité système Windows, stratégie d'audit](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#strategie-daudit-audit-policy) · [Solutions de sécurité, DLP sur le poste](../../../library/cyber/outils/solutions-de-securite/index.md) — Ajout hors cours : les paramètres de blocage
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| UEFI et Secure Boot | `Confirm-SecureBootUEFI` ; `msinfo32` | `True` ; mode UEFI |
| Certificats Secure Boot | Mises à jour du constructeur et de Windows | Certificats 2023 en place |
| TPM | `Get-Tpm` | `TpmPresent` et `TpmReady` à `True`, version 2.0 |
| Micrologiciel | Interface UEFI | Mot de passe, pas de démarrage externe, à jour |
| BitLocker | `manage-bde -status` ; `Get-BitLockerVolume` | `ProtectionStatus On`, 100 % chiffré |
| Protecteurs BitLocker | `manage-bde -protectors -get C:` | TPM (+ PIN pour les portables), clé de récupération sauvegardée dans l'AD / Entra ID |
| Exécution automatique | `NoDriveTypeAutoRun` | `255` |
| Stockage amovible | GPO *Accès au stockage amovible* ; audit | Selon la politique ; audit activé |

| Événement | Journal | Ce qu'il signale |
|---|---|---|
| 6416 | Journaux Windows → Security | Nouveau périphérique externe reconnu (audit Plug-and-Play) |
| 4663 | Journaux Windows → Security | Accès à un fichier sur un support amovible (audit du stockage amovible) |
