---
tags:
  - windows
---
# Élévation de privilèges — Windows

!!! info "📚 Cours de fond"
    Pour comprendre le fonctionnement avant la pratique :

    - [Windows en profondeur](../library/it/windows/windows-en-profondeur/index.md)
    - [Windows — fiche cyber](../library/it/windows/windows-fiche-cyber/index.md)
    - [PowerShell](../library/it/windows/powershell/index.md)
    - [Sécurité système Windows](../library/cyber/hardening/securite-systeme-windows/index.md)

!!! abstract "En bref"
    Identifier puis valider une faiblesse locale. Administrateur local, processus élevé et `NT AUTHORITY\SYSTEM` sont distincts ; SYSTEM local ne donne pas automatiquement les droits Domain Admin.

## Quick checks

Suivre la [fiche Énumération et audit local](../cheatsheets/windows/fondamentaux/enumeration.md) : identité et token → OS et correctifs → processus/services → logiciels et environnement → réseau → comptes, groupes et protections.

## Privilèges du token

Avec `whoami /priv` et `whoami /groups`, relever les privilèges sensibles, les groupes et l'intégrité. `Disabled` signifie présent mais désactivé ; les conditions d'utilisation et la version Windows restent à vérifier. Le token courant décrit les droits réellement disponibles dans ce processus.

## Services

Rapprocher `tasklist /svc`, `netstat -ano` et `tasklist /FI "PID eq 3520"`, puis examiner le compte d'exécution, la version, les ACL du service et du binaire. Un service en loopback peut mériter un audit même s'il est inaccessible depuis le réseau.

## Autres pistes

| Observation | Vérification suivante |
|---|---|
| Dossier du `PATH` modifiable | Ordre de recherche réellement utilisé, processus privilégié concerné |
| Administrateurs supplémentaires, partage trop ouvert | Justification des droits et exposition des sauvegardes/configurations |
| Correctif apparemment absent | Build exact, correctifs cumulatifs et prérequis de la CVE |

Le cours aborde aussi les groupes privilégiés, l'UAC, le noyau, la recherche d'identifiants et les erreurs de segmentation. Les outils (Seatbelt, winPEAS, PowerUp/SharpUp, JAWS, Sysinternals) orientent les recherches ; leurs résultats demandent une validation manuelle. La collecte de secrets ou les fonctions d'exploitation vont au-delà d'un simple inventaire.

## Voir aussi

- [Cours complet : introduction, outils, Situational Awareness et énumération initiale](../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/index.md)
- [Permissions NTFS et identités](../cheatsheets/windows/fondamentaux/droits.md) · [Processus et services](../cheatsheets/windows/fondamentaux/processus.md)
