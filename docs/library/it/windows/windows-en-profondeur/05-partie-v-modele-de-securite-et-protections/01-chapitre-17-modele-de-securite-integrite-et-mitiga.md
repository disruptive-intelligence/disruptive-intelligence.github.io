---
title: Chapitre 17 — Modèle de sécurité, intégrité et mitigations mémoire
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie V — Modèle de sécurité et protections
  - index.md
---

## 17.0 Les notions centrales en un coup d'œil

Les briques sur lesquelles repose toute la sécurité de Windows :

| Notion | Ce que c'est | En une phrase |
|---|---|---|
| **SID** | Identifiant unique d'un utilisateur, groupe, machine ou domaine (`S-1-5-21-…-RID`) | Windows raisonne sur le SID, jamais sur le nom affiché |
| **Access token** (jeton d'accès) | « Badge » créé à l'ouverture de session : SID de l'utilisateur, SID de ses groupes, privilèges, niveau d'intégrité | Hérité par tous les processus de la session |
| **Security descriptor** | Fiche de sécurité d'un objet : Owner, Primary Group, DACL, SACL | Décrit qui possède l'objet, qui y accède, ce qu'on audite |
| **ACE / ACL / DACL / SACL** | Les règles d'accès et d'audit posées sur un objet | Voir le tableau ci-dessous |
| **LSA** | Autorité de sécurité locale : fournit identités (SID) et secrets à l'authentification, applique la politique | La fonction |
| **LSASS** (`lsass.exe`) | Processus qui exécute la LSA : vérifie chaque connexion, crée les jetons, gère les changements de mot de passe et le cache des tickets Kerberos | Le processus — d'où sa sensibilité (Ch.11) |
| **SAM** | Base locale des comptes et de leurs secrets (`C:\Windows\System32\config\SAM`, `HKLM\SAM`), chiffrée par une clé rangée dans la ruche SYSTEM | Comptes **locaux** uniquement |
| **NTDS.dit** | Base AD sur les DC | Comptes **du domaine** |

```text
Utilisateur → authentification (LSASS) → jeton → processus → accès à un objet → DACL → Allow / Deny
                                                                              → SACL → événement d'audit
```


## 17.1 Le Security Reference Monitor, les tokens et les ACL

Tout, sous Windows, tient dans une seule phrase :

```text
Utilisateur → authentification → token → processus → accès à un objet → DACL → Allow/Deny
```


**Le token d'accès.** À la connexion, après vérification par LSASS, Windows crée un **access token** — le « badge » de l'utilisateur. Il contient le **SID** de l'utilisateur, les **SID de ses groupes**, ses **privilèges**, son **niveau d'intégrité**, son type de logon et d'éventuels *restricted SIDs*. Les processus qu'il lance **héritent** de ce token (explorer.exe en fait une copie pour chaque programme ouvert). Les tokens sont créés au logon et ne changent pas pendant la session.

**L'objet sécurisable et son Security Descriptor.** Beaucoup d'objets portent des permissions : fichiers, dossiers, clés de registre, services, tâches planifiées, processus, threads, imprimantes, partages. Chacun possède un **Security Descriptor** qui contient :

- **Owner** — le propriétaire (peut toujours modifier les permissions) ;
- **Primary Group** — le groupe principal ;
- **DACL** — qui a le droit de faire quoi ;
- **SACL** — quels accès sont audités/journalisés.

**ACE, ACL, DACL, SACL.** La terminologie se range simplement — *une ACE est à une ACL ce qu'une ligne est à un tableau* :

| Terme | Définition courte | À quoi ça sert | Où c'est stocké |
|---|---|---|---|
| **ACE** (*Access Control Entry*) | **Une ligne de règle** : *qui* (SID) → *quels droits* → *Allow* ou *Deny* (ou *Audit*) | Brique élémentaire des permissions | Dans une ACL |
| **ACL** (*Access Control List*) | **La liste** d'ACE d'un objet ; terme générique | Définit le comportement global d'accès | Dans le security descriptor |
| **DACL** (*Discretionary ACL*) | L'ACL des **autorisations** | *Qui a le droit de faire quoi ?* | Champ DACL du descripteur |
| **SACL** (*System ACL*) | L'ACL d'**audit** | *Quels accès journaliser (succès / échec) ?* | Champ SACL du descripteur |
| **Security descriptor** | Owner + Primary Group + DACL + SACL | Toute la sécurité d'un objet | `nTSecurityDescriptor` (objet AD), métadonnées NTFS (fichier), registre (service, clé) |

```text
Security Descriptor
├── Owner
├── Group
├── DACL
│   ├── ACE : Alice peut lire
│   ├── ACE : Bob peut écrire
│   └── ACE : Users ne peuvent pas modifier
└── SACL
    └── Auditer les échecs d'écriture
```


**L'access check.** À chaque tentative d'accès, le SRM déroule :

```text
1. Le processus présente son token.
2. Windows lit la DACL de l'objet.
3. Windows compare les SID du token aux ACE de la DACL.
4. Windows autorise ou refuse (une ACE Deny l'emporte sur une ACE Allow).
```


Une **ACE est explicite** (définie sur l'objet) ou **héritée** du parent. Côté sécurité, les permissions à repérer sont celles trop larges sur un objet sensible — `Everyone`, `BUILTIN\Users` ou `Authenticated Users` en Full Control ou Modify sur un binaire de service, par exemple.

L'**impersonation** complète le modèle : un thread peut adopter temporairement l'identité d'un autre utilisateur (niveaux Anonymous, Identification, Impersonation, Delegation) — mécanisme légitime des services, mais aussi levier d'élévation quand un compte dispose de `SeImpersonatePrivilege`.

## 17.2 Lire un descripteur au format SDDL

Windows sait exporter un security descriptor sous forme de texte, le **SDDL** (*Security Descriptor Definition Language*). On le croise partout : permissions d'un service (`sc sdshow <service>`), sortie de `Get-Acl … | Select Sddl`, objets Active Directory.

```text
O:BAG:SYD:(A;;CCLCSWRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)
│   │    │  └── une ACE entre parenthèses ──┘
│   │    └── D: = début de la DACL (S: = SACL)
│   └── G: = groupe principal (SY = SYSTEM)
└── O: = propriétaire (BA = Administrators)
```


Une ACE se lit en six champs séparés par `;` :

```text
(A ; ; CCLCSWRPLORC ; ; ; AU)
 │  │   │            │ │  └─ trustee : à qui s'applique la règle
 │  │   │            │ └──── GUID d'objet hérité (vide ici)
 │  │   │            └────── GUID d'objet (vide ici ; sert dans AD pour viser un attribut)
 │  │   └─────────────────── droits
 │  └─────────────────────── flags d'héritage (vide ici)
 └────────────────────────── type : A = Allow, D = Deny, AU = Audit (dans une SACL)
```


| Abréviation | Trustee |
|---|---|
| `SY` | SYSTEM |
| `BA` | Built-in Administrators |
| `AU` | Authenticated Users |
| `BU` | Built-in Users |
| `WD` | Everyone (*World*) |
| `DA` / `EA` | Domain Admins / Enterprise Admins |

| Code (service) | Droit | Signification |
|---|---|---|
| `CC` | SERVICE_QUERY_CONFIG | Lire la configuration du service |
| `LC` | SERVICE_QUERY_STATUS | Lire l'état (démarré, arrêté…) |
| `SW` | SERVICE_ENUMERATE_DEPENDENTS | Lister les services dépendants |
| `RP` | SERVICE_START | Démarrer le service |
| `WP` | SERVICE_STOP | Arrêter le service |
| `LO` | SERVICE_INTERROGATE | Demander au service de rafraîchir son état |
| `DC` | SERVICE_CHANGE_CONFIG | Modifier la configuration (droit sensible) |
| `RC` | READ_CONTROL | Lire le descripteur |
| `WD` / `WO` | WRITE_DAC / WRITE_OWNER | Modifier la DACL / le propriétaire (droits sensibles) |
| `SD` | DELETE | Supprimer |

Dans l'exemple, *Authenticated Users* peut lire la configuration et l'état du service et le démarrer — un profil normal ; seuls Administrators et SYSTEM ont les droits d'écriture. Si un groupe large (`AU`, `BU`, `WD`) apparaissait avec `DC`, `WD` ou `WO`, la configuration serait à corriger.

Les **flags d'héritage**, sous leur forme `icacls` (fichiers) :

| Code | Signification |
|---|---|
| `(OI)` | *Object Inherit* : s'applique aux fichiers du dossier |
| `(CI)` | *Container Inherit* : s'applique aux sous-dossiers |
| `(IO)` | *Inherit Only* : seulement par héritage, pas sur l'objet courant |
| `(NP)` | *No Propagate* : ne descend que d'un niveau |
| `(I)` | Permission héritée (non définie explicitement) |

## 17.3 Mandatory Integrity Control (MIC)

En plus de la DACL, chaque processus et chaque objet porte un **niveau d'intégrité**. Règle par défaut : un processus **ne peut pas écrire** dans un objet de niveau supérieur au sien (*no write up*), même si la DACL l'autoriserait.

| Niveau | Exemples |
|---|---|
| **Untrusted** | Processus anonymes |
| **Low** | Navigateur ou lecteur de documents en bac à sable ; dossier `AppData\LocalLow` |
| **Medium** | Processus d'un utilisateur standard, ou d'un administrateur non élevé |
| **High** | Processus élevés (« Exécuter en tant qu'administrateur ») |
| **System** | Services et processus système |

Voir son niveau : `whoami /groups`, ligne *Mandatory Label* (`Medium Mandatory Level`, `High Mandatory Level`).

## 17.4 UAC (User Account Control)

Un administrateur reçoit à l'ouverture de session **deux jetons** : un jeton **filtré** (intégrité Medium, privilèges retirés), utilisé par défaut, et un jeton **complet** (High), utilisé seulement après une demande d'élévation.

```text
Administrateur se connecte → jeton filtré (Medium) pour Explorer et les applications
                           → demande d'élévation (invite UAC) → processus avec le jeton complet (High)
```


UAC n'est **pas une frontière de sécurité** selon Microsoft : c'est un garde-fou contre les élévations involontaires. D'où les bonnes pratiques : utilisateurs sans droits d'administration au quotidien, niveau UAC « toujours notifier » pour les comptes d'administration, et surveillance des modifications des clés de registre liées à UAC.

## 17.5 Mitigations mémoire et code

*Les protections modernes qui rendent l'exploitation de vulnérabilités plus coûteuse.*

| Mitigation | Principe | Contre quoi |
|---|---|---|
| **DEP** | Les pages de données ne sont pas exécutables | Exécution de code injecté dans la pile ou le tas |
| **ASLR** | Adresses de chargement aléatoires | Prédiction des adresses par l'attaquant |
| **CFG** | Les appels indirects ne peuvent viser que des cibles valides | Détournement du flux d'exécution |
| **CET** (*shadow stack*) | Pile de retour protégée par le processeur | Corruption des adresses de retour |
| **ACG** | Interdit à un processus de créer du code dynamique exécutable | Génération de code à la volée |
| **CIG** | N'autorise que des DLL signées (Microsoft) | Chargement de DLL arbitraires |
| **HVCI** | L'hyperviseur vérifie le code noyau | Pilotes non conformes, code noyau modifié |

Ces protections se **cumulent** : un exploit moderne doit en contourner plusieurs, ce qui le rend plus rare, plus cher et plus détectable. Les vérifier : *Sécurité Windows → Contrôle des applications et du navigateur → Protection contre les exploits*, ou `Get-ProcessMitigation`.

---
