---
title: Partie V — Détection
source: IT/03 Active Directory/Active Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

*Voir ce qui se passe dans l'annuaire : la télémétrie minimale, les signaux par technique, la déception, puis la corrélation.*

---


## Chapitre 19 — Minimum Viable Visibility : la télémétrie indispensable

Sans journaux, même le meilleur SOC est aveugle sur AD. Les sources à activer et à centraliser, par ordre de priorité :

| # | Source | Ce qu'elle apporte |
|---|---|---|
| 1 | Journal **Security** de tous les DC (*Advanced Audit Policy*, Ch.12) | Authentifications, comptes, groupes |
| 2 | **Directory Service Changes** (5136) avec SACL sur les objets sensibles | Modifications d'objets et de permissions |
| 3 | **Kerberos détaillé** (4768, 4769, 4771) | Demandes de tickets, types de chiffrement |
| 4 | **PowerShell** Script Block (4104) et Module Logging (4103) | Scripts exécutés, y compris obfusqués |
| 5 | **Sysmon** sur DC et serveurs Tier 0/1 | Processus, réseau, accès à `lsass.exe` |
| 6 | **EDR** sur DC et PAW | Comportements, réponse |
| 7 | Journaux **AD CS** (4886/4887, modifications de modèles) | Émissions de certificats |
| 8 | **Requêtes LDAP coûteuses** (événement 1644, à activer ponctuellement) | Énumération massive de l'annuaire |
| 9 | **DNS** des DC | Résolutions, domaines suspects |
| 10 | Collecte **centralisée** (WEF ou agent SIEM) | Journaux hors de portée de l'attaquant |

> **À retenir.** Activer ne suffit pas : il faut vérifier que les événements arrivent bien dans le SIEM, avec une rétention suffisante (plusieurs mois pour pouvoir remonter le fil d'une intrusion).

---


## Chapitre 20 — Détecter les attaques AD dans le SIEM

Pour chaque famille de technique, trois questions : quel **signal** la trahit, quelle **corrélation** le rend fiable, quels **faux positifs** prévoir.

| Technique | Signal | Corrélation qui confirme | Faux positifs courants |
|---|---|---|---|
| Attaque hors ligne des comptes de service (Kerberoasting) | Rafale de 4769, surtout en RC4 | Un même compte demande des tickets pour de nombreux SPN en peu de temps | Outils d'inventaire, scanners |
| Comptes sans pré-authentification (AS-REP Roasting) | 4768 sans pré-authentification | Comptes listés avec ce drapeau | Comptes anciens légitimes |
| Pulvérisation de mots de passe | 4625 / 4771 en volume | Un même mot de passe essayé sur beaucoup de comptes, depuis une source | Mot de passe expiré sur un service |
| Réplication depuis une machine non-DC (DCSync) | 4662 avec les droits de réplication | Source qui n'est **pas** un DC connu | Outils de synchronisation légitimes (Entra Connect) à mettre en liste blanche |
| Réutilisation d'empreinte NTLM (Pass-the-Hash) | 4624 type 3 ou 9 en NTLM | Compte admin, source inhabituelle, violation de tiering | Administration légitime mal outillée |
| Ticket forgé (Golden Ticket) | Usage de tickets sans demande correspondante, durée ou SID incohérents | Absence de 4768 préalable sur les DC | Rares |
| Modification de permissions sensibles | 5136 sur AdminSDHolder, racine du domaine, GPO, comptes Tier 0 | Hors fenêtre de changement, auteur non habilité | Changements planifiés |
| Accès à la mémoire de LSASS | Sysmon 10 ciblant `lsass.exe` | Processus source inhabituel | Antivirus, EDR, outils de sauvegarde |
| Émission de certificat abusive (AD CS) | 4887 | Sujet du certificat différent du demandeur, modèle sensible | Inscriptions par agent légitimes |
| Ajout de clé sur un compte (Shadow Credentials) | 5136 sur `msDS-KeyCredentialLink` | Auteur qui n'est pas le compte lui-même ni un service Windows Hello | Enrôlements Windows Hello |

> **Un Event ID est un indice, pas une preuve.** Chaque signal se lit avec son contexte (compte, source, heure, habitude) et se compare à une baseline.

---


## Chapitre 21 — Deception et honey objects

La déception consiste à placer dans l'annuaire des **objets pièges** qu'aucun usage légitime ne touche. Toute interaction avec eux est donc suspecte : c'est la détection au taux de faux positifs le plus bas.

| Objet piège | Principe | Alerte sur |
|---|---|---|
| **Honey account** | Compte factice aux attributs attractifs (`adminCount = 1`, description évocatrice, ancien mot de passe) | Toute authentification ou demande de ticket (4624, 4768, 4769) |
| **Honey SPN** | SPN factice sur un compte piège | Toute demande de ticket de service pour ce SPN (4769) |
| **Honey token** | Faux identifiants laissés sur des machines (fichiers, registre, mémoire) | Leur utilisation n'importe où dans le domaine |
| **Canary file** | Fichier piège sur un partage (« salaires », « mots de passe ») | Lecture via SACL (4663) |

Règles de mise en œuvre : des objets crédibles (âge, nommage cohérent avec le reste), aucun droit réel, une alerte de haute priorité, et une documentation interne restreinte pour que les administrateurs ne les déclenchent pas par erreur.

> **🔵 KERBEROS — Épisode 5 (Blue Team)**
>
> La Blue Team de Meridian n'avait déployé aucun objet piège. Après le test de Thomas, elle crée un compte « svc_legacy » avec `adminCount = 1` et un SPN attractif (`MSSQLSvc/legacy-db.meridian.local`), deux fichiers « salaires_2025.xlsx » et « passwords.xlsx » sur un partage accessible, et de faux identifiants dans le registre de SRV-APP01. Au test suivant, la première demande de ticket sur svc_legacy déclenche une alerte immédiate.

---


## Chapitre 22 — Règles SIEM et corrélation avancée

### 22.1 Corréler plusieurs événements

Une règle fiable combine plusieurs conditions plutôt qu'un seul Event ID :

| Règle | Conditions combinées | Sévérité |
|---|---|---|
| Demandes de tickets anormales | 4769 en RC4 + volume au-dessus du seuil + compte hors baseline | Haute |
| Violation de tiering | 4624 (type 3 ou 10) + compte Tier 0 + machine Tier 1/2 | Critique |
| Persistance par permissions | 5136 sur AdminSDHolder ou GPO + hors fenêtre de maintenance + auteur non habilité | Haute |
| Abus de PKI | 4887 + modèle sensible + sujet ≠ demandeur | Critique |
| Clé ajoutée sur un compte | 5136 `msDS-KeyCredentialLink` + auteur inattendu | Haute |
| Réplication hors DC | 4662 droits de réplication + source ≠ DC | Critique |

### 22.2 Réduire les faux positifs

- construire une **baseline** : comptes de service et leurs serveurs, horaires d'administration, outils d'inventaire ;
- mettre en **liste blanche** nominativement ce qui est légitime (et documenter pourquoi) ;
- **ajuster** progressivement les seuils, règle par règle, avec un suivi du taux de faux positifs ;
- enrichir les alertes (tier du compte et de la machine, propriétaire) pour accélérer le tri.

### 22.3 Sigma

**Sigma** est un format de règles de détection portable, convertible vers Splunk, Elastic, Microsoft Sentinel et d'autres. La communauté maintient un large catalogue de règles AD : on part de ces règles, puis on les adapte à sa baseline.

---
