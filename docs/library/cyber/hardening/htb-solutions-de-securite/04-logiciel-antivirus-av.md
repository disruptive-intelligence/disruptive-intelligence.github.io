---
title: Logiciel antivirus — AV
source: Cyber/99_Concepts/HTB_Solutions de sécurité.md
note: HTB — Solutions de sécurité
up:
- - HTB — Solutions de sécurité
  - index.md
---

## Antivirus — AV

- Logiciel de sécurité chargé de **détecter, bloquer et supprimer les malwares** présents sur un système.
- Il analyse régulièrement les fichiers et activités afin d’identifier les menaces avant qu’elles n’endommagent l’appareil.

```
Malware détecté
→ Block / Quarantine / Delete
```

## Types d’analyse
### Signature-Based Scanning

- Compare les fichiers analysés avec une **base de signatures de malwares connus**.
- Si une signature correspond :
    - le fichier est identifié comme malveillant ;
    - il peut être bloqué, mis en quarantaine ou supprimé.
- Très efficace contre les **malwares connus**.
- Nécessite une **mise à jour régulière de la base de signatures**.

```
File Hash / Signature
        ↓
AV Database
        ↓
Match → Malware connu
```

- Limite principale :
	- peut rater :
	    - nouveaux malwares ;
	    - variantes modifiées ;
	    - malware polymorphe ;
	    - menaces sans signature connue.
### Heuristic Scanning

- Analyse le **comportement** du fichier plutôt que seulement sa signature.
- Cherche des actions anormales ou potentiellement malveillantes.
- Exemple :

```
Executable
→ tente de modifier un fichier système sensible
→ comportement suspect
→ alerte
```

- Intérêt :
	- peut détecter des menaces **inconnues ou modifiées** ;
	- ne dépend pas uniquement d’une signature présente dans la base.
- Limite :

```
Détection comportementale plus large
→ risque de False Positive
```

## Fonctions de l’antivirus

- analyser régulièrement le système ;
- détecter les logiciels malveillants ;
- protéger contre les menaces externes ;
- bloquer ou isoler les fichiers suspects ;
- nettoyer/supprimer les malwares détectés.

```
Scan
→ Detect
→ Block / Quarantine
→ Remove
```

## AV vs EDR

|Antivirus|EDR|
|---|---|
|Détection malware|Détection comportementale étendue|
|Signature + heuristique|Télémétrie détaillée endpoint|
|Quarantaine / suppression|Investigation + réponse|
|Centré surtout sur le malware|Centré sur l’activité complète de l’endpoint|

```
AV  → Detect / Block Malware
EDR → Monitor / Detect / Investigate / Respond
```

> Les solutions modernes peuvent intégrer les deux fonctions dans un même produit.
