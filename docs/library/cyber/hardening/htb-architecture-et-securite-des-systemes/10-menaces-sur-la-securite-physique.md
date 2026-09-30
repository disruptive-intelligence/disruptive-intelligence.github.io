---
title: Menaces sur la sécurité physique
source: Cyber/04_Hardening/HTB_Architecture et sécurité des systèmes.md
note: HTB — Architecture et sécurité des systèmes
up:
- - HTB — Architecture et sécurité des systèmes
  - index.md
---

## Espionnage - Snooping

- **Snooping** : accès non autorisé à des informations confidentielles par observation ou fouille.
- Exemples :
    - **Dumpster Diving** : récupérer des documents jetés ;
    - fouiller bureaux, tiroirs ou armoires d’autres employés.
- Prévention
	- **Clean Desk Policy** : ne pas laisser de documents sensibles sans surveillance.
	- Stocker les documents dans des **armoires verrouillées** et zones sécurisées.
	- **Détruire/shredder** les documents avant de les jeter.

```
Document sensible
→ stockage sécurisé
→ destruction avant élimination
```

## Asset Lost / Stolen
Les laptops, smartphones et tablettes perdus ou volés peuvent exposer des données sensibles.

- Ne pas laisser les appareils visibles dans une voiture → risque de **smash-and-grab**.
- Les placer dans un endroit non visible/sécurisé, par exemple le coffre.
- Au bureau, utiliser des **lockdown/security cables** pour attacher :
    - laptops ;
    - écrans ;
    - projecteurs ;
    - desktops.

> Les câbles antivol sont surtout un **moyen de dissuasion** : ils ne résistent pas forcément à un attaquant déterminé.
## Remote Device Reset / Wipe

- Un appareil perdu ou volé doit être **signalé immédiatement**.
- **Remote Wipe** : le serveur envoie une commande demandant au device d’effacer :
    - données ;
    - configurations.

```
Device perdu
→ signalement
→ Remote Wipe
→ données supprimées
```


→ réduit le risque d’exposition des données présentes sur l’appareil.
## Device Security Measures

### Smartphones / Mobile Devices
Mesures principales :

- password/PIN ;
- **auto-lock** après une période d’inactivité ;
- fonctions de **device tracking** ;
- remote wipe.

L’objectif est qu’un appareil volé ne puisse pas être utilisé directement par l’attaquant.
### Laptops
Mesures possibles au niveau BIOS/UEFI :

- **Power-on password** ;
- password administrateur BIOS/UEFI ;
- limiter/modifier le **boot order** pour empêcher facilement le démarrage sur USB/CD externe.

```
Boot externe bloqué
→ plus difficile de démarrer un OS contrôlé par l'attaquant
```

### Full-Disk Encryption
Si un attaquant possède physiquement le disque, le chiffrement complet protège les données au repos.
Exemple Windows :

- **BitLocker**.

```
Disque volé
+
BitLocker
→ données chiffrées
```

**Complément :** BitLocker n’est pas simplement un « boot password ». Il chiffre le disque ; avec une configuration **TPM + PIN**, il peut également imposer une authentification avant le démarrage de Windows.
## Employee Mistakes
Les erreurs humaines peuvent provoquer des dégâts physiques.
### ESD — Electrostatic Discharge

- Une personne peut accumuler de l’électricité statique.
- En touchant un composant, cette charge peut être transférée et :
    - endommager ;
    - voire détruire le composant.

Exemple :

```
Technicien
→ électricité statique
→ touche motherboard/RAM
→ ESD
→ composant endommagé
```

Prévention :

- former les équipes support ;
- utiliser un **anti-static wrist strap** relié à la terre avant de manipuler les composants.
## Malicious Interference / Sabotage

- **Sabotage** : action volontaire visant à endommager ou perturber les systèmes.
- Peut notamment provenir d’un **disgruntled employee**, mais pas uniquement.

Exemple :

```
Employé malveillant
→ modification/suppression d'une base de données
→ interruption du service
```

Prévention / Résilience

- identifier les systèmes particulièrement exposés au sabotage ;
- limiter les privilèges ;
- disposer d’un **Recovery Plan** détaillé ;
- prévoir :
    - procédures de restauration ;
    - backups ;
    - pièces de rechange nécessaires.

Le but n’est pas seulement d’empêcher le sabotage, mais aussi de pouvoir **restaurer rapidement le service** après un incident.
