---
title: Chapitre 2 — Le processus de démarrage
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie I — Architecture fondamentale
  - index.md
---

## 2.1 La séquence

```text
UEFI (POST, initialisation, Secure Boot)
 → bootmgr (lit le BCD)
   → winload.exe (charge le noyau, le HAL, les pilotes de démarrage, la ruche SYSTEM)
     → ntoskrnl.exe (initialise le noyau)
       → smss.exe
         ├─ session 0 : csrss.exe + wininit.exe → services.exe (services) + lsass.exe
         └─ session 1 : csrss.exe + winlogon.exe → LogonUI → (authentification) → userinit.exe → explorer.exe
```


| Étape | Composant | Ce qui se passe |
|---|---|---|
| 1 | Firmware **UEFI** | Tests matériels, recherche du support de démarrage, vérification Secure Boot |
| 2 | **bootmgr** | Lit le **BCD** (*Boot Configuration Data*, modifiable avec `bcdedit`) |
| 3 | **winload.exe** | Charge noyau, HAL, pilotes *boot-start* et ruche SYSTEM |
| 4 | **ntoskrnl.exe** | Initialise le noyau, lance `smss.exe` |
| 5 | **smss.exe** | Crée les sessions 0 (services) et 1 (utilisateur) |
| 6 | **wininit.exe** | Lance `services.exe` et `lsass.exe` |
| 7 | **services.exe** | Démarre les services automatiques |
| 8 | **winlogon.exe** | Écran d'ouverture de session |
| 9 | **explorer.exe** | Après authentification : le bureau |

## 2.2 Protéger la chaîne de démarrage

| Mécanisme | Rôle |
|---|---|
| **UEFI + GPT** (contre BIOS + MBR) | Base moderne nécessaire aux protections suivantes |
| **Secure Boot** | Vérifie la signature de chaque composant de démarrage |
| **Measured Boot + TPM** | Enregistre des mesures d'intégrité dans le TPM, vérifiables à distance (attestation) |
| **ELAM** (*Early Launch Anti-Malware*) | Pilote antimalware chargé avant les autres pilotes |
| **BitLocker** (avec TPM) | Le disque ne se déchiffre que si la chaîne de démarrage est intacte |

## 2.3 Persistance avant et après le système

- **Avant le système** (*bootkits*, implants firmware) : rares mais très difficiles à voir, car ils s'exécutent avant l'EDR. Exemples publics : BlackLotus (bootkit UEFI, 2023), LoJax (implant firmware attribué à APT28). Défenses : Secure Boot à jour (révocations), firmware à jour, Measured Boot.
- **Après le démarrage** : services, pilotes, tâches planifiées, clés Run, Winlogon, dossiers de démarrage. Visibles mais noyés dans le légitime — **Autoruns** les liste tous (Ch.23).

---
