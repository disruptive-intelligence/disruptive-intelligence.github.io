---
title: "Énumération et audit local"
cours:
  - library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/index.md
---
# Énumération et audit local

Faire l'état des lieux d'un poste Windows pour un audit de durcissement ou une recherche d'élévation de privilèges.

Les incontournables : `whoami /all` · `systeminfo` · `tasklist /svc` · `netstat -ano` · `net accounts`
{ .kw-cs-top }

## Parcours rapide

### Faire un premier inventaire local

| Étape | Commandes | À regarder |
|---|---|---|
| [Identité et droits](droits.md) | `whoami /all`, `whoami /priv`, `whoami /groups` | SID, groupes, privilèges, niveau d'intégrité du token courant |
| [Sessions](systeme.md#voir-qui-est-connecte-a-la-machine) | `query user`, `echo %USERNAME%` (CMD) | Sessions actives/déconnectées, compte courant |
| [Système et correctifs](systeme.md#voir-les-correctifs-installes) | `systeminfo`, `Get-HotFix` (PowerShell), `wmic qfe` (historique) | OS, build, architecture, dernier démarrage, domaine, KB |
| [Processus et services](processus.md#relier-les-processus-aux-services) | `tasklist /svc` | Processus habituels, logiciels tiers, PID et services hébergés |
| [Environnement](systeme.md#examiner-les-chemins-de-recherche-et-de-demarrage) | `set` (CMD), `Get-ChildItem Env:` (PowerShell) | `PATH`, profils, répertoires personnels et temporaires |
| [Logiciels](../administration/logiciels.md#lister-les-logiciels-installes) | `winget list`, `Get-ItemProperty` sur les clés `Uninstall` | Noms, versions, éditeurs, services et configurations associés |
| [Réseau](reseau.md) | `ipconfig /all`, `arp -a`, `route print` | Interfaces, DNS, voisins, routes ; machine sur plusieurs sous-réseaux |
| [Écoute et connexions](reseau.md#voir-les-ports-en-ecoute) | `netstat -ano`, `tasklist /FI "PID eq 3520"` | Port → PID → processus → service ; écoute locale ou sur toutes les interfaces |
| [Comptes et groupes](droits.md#enumerer-les-comptes-et-les-groupes-locaux) | `net user`, `net localgroup`, `net localgroup administrators` | Comptes de service, groupes inhabituels, administrateurs supplémentaires ; noms localisés |
| [Politique de comptes](droits.md#voir-la-politique-de-mot-de-passe-et-de-verrouillage) | `net accounts` | Longueur et historique, expiration, seuil/durée de verrouillage |
| [Protections](systeme.md#consulter-et-tester-la-politique-applocker) | `Get-MpComputerStatus`, `Get-AppLockerPolicy`, `Test-AppLockerPolicy` (PowerShell) | Composants Defender, règles AppLocker et mode d'application |

`wmic product get name` et `Get-WmiObject -Class Win32_Product | Select-Object Name, Version` figurent dans le cours : ces requêtes peuvent lancer des réparations MSI. Préférer l'[inventaire par le registre](../administration/logiciels.md#lister-les-logiciels-installes). `wmic.exe` peut être absent ; `Get-WmiObject` appartient à Windows PowerShell 5.1.

## Lire les résultats

- **Droits** : groupe Administrators, processus élevé et SYSTEM sont trois notions distinctes. SYSTEM local n'est pas Domain Admin. Un privilège `Disabled` reste présent dans le token ; un privilège absent ne s'active pas simplement.
- **Correctifs et logiciels** : rapprocher build, KB et versions des vulnérabilités applicables. Un inventaire incomplet ou un ancien redémarrage ne démontre pas une faille exploitable.
- **Réseau** : ARP n'est pas un historique de sessions. Une route indique un chemin configuré ; `0.0.0.0` indique une écoute sur toutes les interfaces IPv4. Le pare-feu peut bloquer le trafic dans les deux cas.
- **Durcissement** : vérifier les ACL des programmes et dossiers du `PATH`, réduire les appartenances privilégiées inutiles et examiner les protections désactivées. Une anomalie constitue une piste à valider dans son contexte.

Pour approfondir : [cours complet et outils d'énumération](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/index.md) · [démarche d'élévation locale](../../../privesc/windows.md).
