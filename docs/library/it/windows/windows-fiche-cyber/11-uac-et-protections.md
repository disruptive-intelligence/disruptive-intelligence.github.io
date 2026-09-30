---
title: UAC et protections
source: IT/02_Windows/Fiche_Windows.md
note: Windows — fiche cyber
up:
- - Windows — fiche cyber
  - index.md
---

## 13. UAC — User Account Control

### 13.1 Définition

L’**UAC** est un mécanisme de sécurité Windows qui contrôle l’élévation de privilèges.

Il vise à empêcher qu’un programme réalise des actions administrateur sans validation.

Exemples d’actions déclenchant potentiellement l’UAC :

- installation d’un logiciel ;
    
- modification système ;
    
- écriture dans certains dossiers protégés ;
    
- modification de clés registre sensibles ;
    
- lancement d’un outil en administrateur.
    

---

### 13.2 Admin Approval Mode

Un utilisateur membre du groupe Administrators ne travaille pas forcément en permanence avec un token administrateur complet.

En pratique, il peut avoir :

- un token filtré, utilisé par défaut ;
    
- un token élevé, utilisé après validation UAC.
    

Schéma :

```text
Admin connecté
   ↓
Token standard filtré
   ↓
Demande d’élévation
   ↓
Prompt UAC
   ↓
Token administrateur élevé
```


À retenir :

```text
Être admin ≠ être élevé
```


---

## 14. Protections Windows

### 14.1 Windows Defender

Windows Defender Antivirus est l’antivirus intégré de Windows.

Fonctionnalités importantes :

- protection temps réel ;
    
- protection cloud ;
    
- soumission automatique d’échantillons ;
    
- Tamper Protection ;
    
- exclusions ;
    
- Controlled Folder Access ;
    
- protection contre certains comportements malveillants.
    

Commandes utiles :

```powershell
Get-MpComputerStatus
Get-MpPreference
```


---

### 14.2 Credential Guard

**Credential Guard** protège certains secrets d’authentification en les isolant via Virtualization-Based Security.

Objectif : réduire l’impact d’un accès au système en empêchant certains vols de credentials depuis LSASS.

---

### 14.3 LSA Protection / RunAsPPL

**LSA Protection** permet de lancer LSASS comme processus protégé.

Objectif : empêcher des processus non autorisés d’ouvrir ou de manipuler LSASS.

---

### 14.4 AppLocker

**AppLocker** permet de contrôler quels programmes peuvent être exécutés.

Il peut créer des règles sur :

- exécutables ;
    
- scripts ;
    
- fichiers MSI ;
    
- DLL ;
    
- applications packagées.
    

Types de règles :

|Type|Exemple|
|---|---|
|Publisher|Autoriser les binaires signés par Microsoft.|
|Path|Autoriser uniquement certains chemins.|
|Hash|Autoriser un fichier précis par son hash.|

Bon réflexe : commencer en **audit mode** avant de bloquer réellement.

---

### 14.5 WDAC

**Windows Defender Application Control** est une solution plus robuste de contrôle d’exécution applicative.

Différence simplifiée :

|Outil|Usage|
|---|---|
|AppLocker|Contrôle applicatif plus simple à déployer.|
|WDAC|Contrôle plus fort, plus adapté aux environnements très sécurisés.|

---
