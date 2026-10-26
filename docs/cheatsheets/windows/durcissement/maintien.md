---
title: "Mises à jour, référentiel et maintien"
cours:
  - library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/index.md
---

# Mises à jour, référentiel et maintien

Tenir le poste durci dans la durée : système encore supporté, correctifs vérifiés (pas seulement déployés), logiciels à jour, référentiel de configuration versionné, conformité mesurée, dérive détectée, exceptions tracées, sauvegardes restaurables, horloge juste.

Les incontournables : `Get-ItemProperty …\CurrentVersion` (build + UBR) · `Get-HotFix` · `winget upgrade` · `gpresult /h` · `w32tm /query /status`
{ .kw-cs-top }

Un correctif supprime un défaut de code ; il ne touche pas à la configuration. Un poste à jour mais mal configuré reste vulnérable, et l'inverse aussi : correctifs et durcissement sont deux couches distinctes.

## Système et correctifs

### Vérifier que la version de Windows est encore supportée

Un système en fin de support ne reçoit plus de correctifs de sécurité. Le couple **build + révision (UBR)** donne le niveau réel de mise à jour cumulative.

```powershell title="Vérifier"
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild, UBR
```

`ProductName` affiche encore « Windows 10 » sur beaucoup de Windows 11 : se fier au build (`22000` et plus = Windows 11). Comparer `DisplayVersion` et build à la page de cycle de vie de Microsoft (learn.microsoft.com/lifecycle).

Ensuite : [voir la version et le build](../fondamentaux/systeme.md#voir-la-version-et-le-build-de-windows) — Pour comprendre : [MCS, ch. 2 (connaître l'état réel d'une machine Windows)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/01-partie-i-fondations-socle-technique-et-maintenabil/02-chapitre-2-socle-technique-1.md) · [Sécurité système Windows, support du système](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#support-du-systeme-dexploitation)
{ .kw-cs-meta }

### Vérifier que les correctifs sont réellement installés

« Correctif déployé » ne veut pas dire « installé partout ». La liste des correctifs est incomplète sur les versions récentes : elle complète le build + UBR, elle ne le remplace pas.

```powershell title="Vérifier"
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending"   # True : redémarrage en attente
```

```powershell title="Exemple — le journal d'installation"
Get-WinEvent -LogName Setup -MaxEvents 50 | Where-Object { $_.Id -in 1,2,4 } | Select-Object TimeCreated, Id, Message
```

Un correctif installé mais pas encore suivi d'un redémarrage laisse le code vulnérable en mémoire. `RebootPending` n'est qu'un des signaux de redémarrage en attente.

Ensuite : [voir les mises à jour installées](../administration/logiciels.md#voir-les-mises-a-jour-windows-installees) — Pour comprendre : [MCS, annexe B.1 (Windows)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/11-annexes/03-annexe-b-cheat-sheets-par-plateforme.md) · [Élévation de privilèges, correctifs installés](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/03-enumeration-initiale.md)
{ .kw-cs-meta }

### Déployer les correctifs par anneaux

En entreprise, les correctifs passent par une plateforme centrale (WSUS, MECM, Intune) plutôt que machine par machine, et par vagues pour qu'un correctif défectueux ne touche pas tout le parc.

```text title="Processus"
Inventaire → correctifs manquants → priorisation → test → approbation → déploiement → suivi → rapport
Anneaux : pilote → petit groupe de production → déploiement général
```

Urgence (vulnérabilité exploitée, critique, exposée à Internet, exploit public, actif critique) : test rapide, approbation, déploiement d'urgence, vérification. La fenêtre d'urgence se décide à froid, pas pendant la crise. Ne jamais supposer qu'une mise à jour Windows sera désinstallable : prévoir instantané, sauvegarde ou image.

Pour comprendre : [Sécurité système Windows, gestion des MAJ](../../../library/cyber/hardening/securite-systeme-windows/05-gestion-des-maj-et-des-correctifs.md) · [MCS, ch. 18 (le processus de correctif)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/03-partie-iii-le-coeur-operationnel/05-chapitre-18-le-processus-de-correctif-de-bout-en-b.md)
{ .kw-cs-meta }

![[cheatsheets/windows/administration/logiciels#Chercher, installer, mettre à jour un logiciel]]

Les applications tierces (navigateurs, lecteurs PDF, Java, outils d'accès distant), les pilotes et le micrologiciel ne sont pas couverts par Windows Update : chacun se suit à part.
{ .kw-cs-meta }

## Référentiel de configuration

### Partir d'un référentiel et le dériver

On ne durcit pas « au feeling » : on part d'**un seul** référentiel (Microsoft Security Baselines, guides de l'ANSSI, CIS Benchmarks), on le **dérive** (chaque point retenu, adapté ou écarté, chaque écart motivé par écrit), on le **versionne** et on le décline par classe de machine (poste standard, poste d'administration, serveur).

| La baseline contient | |
|---|---|
| Référentiel source | Nom et version |
| Périmètre | Quelles machines, quelles classes |
| Points retenus | Avec leur paramétrage exact |
| Écarts motivés | Point écarté, raison, risque accepté, date de revue |
| Méthode d'application | GPO, Intune, script, image |
| Méthode de contrôle | Comment on vérifie |
| Propriétaire et revue | Nom, fréquence |

Appliquer un référentiel sans le dériver casse des applications ; l'équipe désactive alors les contrôles gênants sans le dire, et la baseline devient une fiction.

Pour comprendre : [MCS, ch. 22 (durcissement et référentiels)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/04-partie-iv-configuration-dependances-et-couches-oub/01-chapitre-22-durcissement-et-referentiels-de-config.md#222-choisir-et-adapter-un-referentiel) · [Windows en profondeur, ch. 27](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md)
{ .kw-cs-meta }

### Durcir sans casser la production

Un durcissement change volontairement le comportement du système : il s'applique comme un changement.

```text title="Méthode"
Inventorier → choisir la baseline → tester sur un groupe pilote, en mode audit quand il existe
→ déployer par lots et par anneaux → prévoir le retour arrière point par point
→ mesurer (conformité, incidents) → documenter les écarts découverts
```

Les modes audit à utiliser : AppLocker et App Control (« Auditer uniquement »), règles ASR (`AuditMode`), accès contrôlé aux dossiers (`AuditMode`), NTLM (*Restrict NTLM: Audit…*).

Pour comprendre : [Windows en profondeur, ch. 27.4 (durcir sans casser)](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#274-durcir-sans-casser) · [MCS, ch. 22.6](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/04-partie-iv-configuration-dependances-et-couches-oub/01-chapitre-22-durcissement-et-referentiels-de-config.md#226-le-durcissement-qui-casse-la-production)
{ .kw-cs-meta }

### Vérifier que les GPO de durcissement s'appliquent vraiment

Une GPO créée n'est pas une GPO appliquée : lien désactivé, filtrage de sécurité, blocage d'héritage, ordre LSDOU (local, site, domaine, OU : la dernière l'emporte).

```bat title="Vérifier"
gpresult /r                 :: résumé des GPO appliquées
gpresult /h C:\rsop.html    :: rapport complet, paramètre par paramètre
```

```bat title="Exemple — forcer puis revérifier"
gpupdate /force
```

Ensuite : [voir les GPO appliquées à un poste](../administration/active-directory/ou-ordinateurs-gpo.md#voir-les-gpo-appliquees-a-un-poste-et-a-un-utilisateur) — Pour comprendre : [PowerShell, ch. 25 (GPO, RSOP)](../../../library/it/windows/powershell/05-partie-v-gpo-et-services-windows-server/01-chapitre-25-group-policy-gpo.md) · [Sécurité système Windows, Local Policy vs Domain GPO](../../../library/cyber/hardening/securite-systeme-windows/03-strategie-de-securite-locale-group-policy-et-uac.md#local-policy-vs-domain-gpo)
{ .kw-cs-meta }

### Mesurer la conformité et repérer la dérive

Une configuration conforme le jour J dérive : intervention manuelle jamais reversée, contrôle coupé pendant un incident, installeur qui remet des valeurs par défaut, restauration ancienne. Contrôler régulièrement chaque point de la baseline (script, outil de conformité, politique centrale) et publier ensemble quatre valeurs.

| Valeur | Rôle |
|---|---|
| Couverture | Part des machines réellement évaluées |
| Conformité | Points conformes sur points applicables, parmi les machines évaluées |
| Points critiques non conformes | En valeur absolue : dix écarts mineurs ne compensent pas un compte administrateur par défaut |
| Machines non évaluables | Avec leur motif (injoignable, exclue, non applicable) |

Pour comprendre : [MCS, ch. 22.5 (mesurer)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/04-partie-iv-configuration-dependances-et-couches-oub/01-chapitre-22-durcissement-et-referentiels-de-config.md#225-mesurer-la-conformite-de-configuration) · [ch. 23 (dérive de configuration)](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/04-partie-iv-configuration-dependances-et-couches-oub/02-chapitre-23-derive-de-configuration-iac-et-immutab.md)
{ .kw-cs-meta }

### Tracer les exceptions

Une exception (application métier qui exige NTLM, SMBv1 pour un vieux copieur, compte de service privilégié) n'est acceptable que si elle est **justifiée, limitée dans le temps, compensée** (surveillance renforcée, segmentation) et **revue**. Non écrite, c'est un oubli ; écrite, datée et signée par la bonne personne, c'est une décision.

Pour comprendre : [Windows en profondeur, ch. 27.4](../../../library/it/windows/windows-en-profondeur/07-partie-vii-hardening-cas-de-synthese-et-reference.md#274-durcir-sans-casser) · [MCS, fiche de dérogation](../../../library/cyber/vulnerabilites/maintien-en-condition-de-securite-mcs/11-annexes/05-d-4-fiche-de-derogation.md)
{ .kw-cs-meta }

## Socle

### Synchroniser l'horloge

Kerberos refuse l'authentification au-delà d'un écart d'horloge (5 minutes par défaut) ; des horodatages faux rendent aussi les journaux inexploitables en investigation. Les postes du domaine se synchronisent sur la hiérarchie du domaine.

```bat title="Vérifier"
w32tm /query /status
w32tm /query /source
```

```bat title="Appliquer — resynchroniser"
w32tm /resync
```

Pour comprendre : [Sécurité système Windows, Clock Synchronization](../../../library/cyber/hardening/securite-systeme-windows/04-authentification-et-autorisation-sous-windows.md#clock-synchronization) — Ajout hors cours : les commandes `w32tm`
{ .kw-cs-meta }

### Sauvegarder et tester la restauration

Le durcissement réduit le risque, la sauvegarde permet de s'en remettre. Règle **3-2-1-1-0** : 3 copies, 2 supports différents, 1 hors site, 1 hors ligne ou immuable, 0 erreur à la restauration. Les sauvegardes elles-mêmes se protègent : comptes dédiés, MFA sur la console, droits minimaux, séparation de la production, alerte sur suppression. Un administrateur du domaine ne doit pas devenir automatiquement administrateur des sauvegardes.

Pour comprendre : [Sauvegardes et reprise d'activité, 3-2-1-1-0 et protection des backups](../../../library/cyber/gouvernance/sauvegardes-et-reprise-d-activite/05-sauvegardes-backups.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Système supporté | `…\Windows NT\CurrentVersion` → `DisplayVersion`, `CurrentBuild`, `UBR` | Version encore supportée, UBR du dernier cumul |
| Correctifs installés | `Get-HotFix` ; journal Setup | Dernier cumul installé |
| Redémarrage | `…\Component Based Servicing\RebootPending` | Absent |
| Déploiement | WSUS, MECM, Intune | Anneaux, taux de conformité suivi |
| Logiciels tiers | `winget upgrade` | Rien d'obsolète |
| Baseline | Document versionné | Un référentiel, dérivé, écarts motivés |
| GPO appliquées | `gpresult /h` | Les GPO de durcissement présentes |
| Conformité | Contrôle périodique | Couverture, conformité, points critiques, non évalués |
| Exceptions | Registre des dérogations | Justifiées, bornées, compensées, revues |
| Horloge | `w32tm /query /status` | Source du domaine, écart faible |
| Sauvegardes | Test de restauration | 3-2-1-1-0, restauration vérifiée |

Les cinq configurations qui annulent l'effet de tous les correctifs, à traiter en premier :

| Configuration | Effet | Fiche |
|---|---|---|
| Protocole ou méthode d'authentification ancienne active | Contournement des protections modernes | [Identifiants](identifiants.md#refuser-lm-et-ntlmv1) · [Réseau](reseau.md) |
| Compte par défaut conservé, mot de passe local identique partout | Propagation immédiate | [Comptes](comptes.md#neutraliser-les-comptes-par-defaut-invite-administrateur-integre) · [LAPS](identifiants.md#donner-a-chaque-poste-son-propre-mot-de-passe-administrateur-local-laps) |
| Service exposé sans besoin | Surface d'attaque inutile | [Réseau](reseau.md#reduire-les-regles-entrantes-au-strict-necessaire) · [Services](services.md#desactiver-les-services-inutiles) |
| Droits excessifs d'un compte de service | Intrusion mineure → compromission majeure | [Comptes](comptes.md#restreindre-les-comptes-de-service) |
| Journalisation absente ou insuffisante | Aucune investigation possible | [Journalisation](journalisation.md) |
