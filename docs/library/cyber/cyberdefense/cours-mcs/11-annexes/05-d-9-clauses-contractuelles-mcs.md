---
title: D.9 — Clauses contractuelles MCS
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - ANNEXES
  - index.md
---

**Identifiant** `CLA-MCS-[nn]` — à insérer en annexe technique du contrat.

| # | Clause | Texte type | Obtenue |
|---|---|---|---|
| 1 | Délais par criticité | « Le Prestataire applique les correctifs de sécurité selon les délais figurant en annexe [X], décomptés à partir de la publication du correctif par l'éditeur. » | `[ ]` |
| 2 | Périmètre nominatif | « Le périmètre couvert est défini par la liste d'actifs annexée, mise à jour trimestriellement et contradictoirement. » | `[ ]` |
| 3 | **Restitution de données** | « Le Prestataire fournit mensuellement, dans un format exploitable et exportable, l'état de mise à jour de chaque actif du périmètre, **y compris la liste des actifs non joignables et leur motif**. » | `[ ]` |
| 4 | Notification | « Le Prestataire notifie sous 24 heures toute vulnérabilité activement exploitée affectant un actif du périmètre. » | `[ ]` |
| 5 | Transparence des versions | « Le Prestataire communique sur demande les versions déployées et son propre calendrier d'obsolescence. » | `[ ]` |
| 6 | Droit d'audit et de test | « Le Client peut faire réaliser un contrôle technique du périmètre, avec un préavis de [30] jours. » | `[ ]` |
| 7 | Sous-traitance | « Le Prestataire déclare ses sous-traitants intervenant sur le périmètre et leur impose les mêmes obligations. » | `[ ]` |
| 8 | **Escalade des impossibilités** | « Toute impossibilité de correction est notifiée sous [5] jours ouvrés, avec sa cause et une proposition de mesure compensatoire. » | `[ ]` |
| 9 | Accès aux preuves | « Le Prestataire met à disposition les journaux d'administration et les preuves d'application relatifs au périmètre. » | `[ ]` |
| 10 | Réversibilité | « En fin de contrat, le Prestataire restitue l'inventaire complet, **l'historique de mise à jour** et la documentation d'exploitation, dans un format ouvert. » | `[ ]` |
| 11 | Assistance au décommissionnement | « Le Prestataire assiste au retrait des accès, comptes et secrets le concernant, et en fournit la preuve. » | `[ ]` |
| 12 | Conséquence d'un manquement | « Le non-respect constaté deux mois consécutifs déclenche un plan de retour à la conformité sous contrôle du Client. » | `[ ]` |

**Priorité si vous ne pouvez en obtenir que trois** : 3, 8, 2.
**En cas de refus** : consigner la demande et le refus **par écrit** (§13.8), documenter le risque accepté, préparer l'architecture de sortie.

---


## D.10 — Questionnaire fournisseur

**Identifiant** `QF-[aaaa]-[nnn]` · **Fournisseur** `[ ]` · **Produit/service** `[ ]` · **Date** `[ ]`

| # | Question | Réponse | Preuve fournie |
|---|---|---|---|
| 1 | Politique de publication des correctifs de sécurité : fréquence, canaux, délai entre découverte et publication | `[ ]` | `[ ]` |
| 2 | Combien de versions maintenez-vous en sécurité, et pendant combien de temps ? | `[ ]` | `[ ]` |
| 3 | Quel préavis donnez-vous avant une fin de support ? | `[ ]` | `[ ]` |
| 4 | Comment nous notifiez-vous une vulnérabilité affectant votre produit ? | `[ ]` | `[ ]` |
| 5 | Fournissez-vous un inventaire des composants du produit ? Sous quel format ? | `[ ]` | `[ ]` |
| 6 | Publiez-vous des déclarations d'exploitabilité ? | `[ ]` | `[ ]` |
| 7 | Les postes utilisés pour administrer notre périmètre sont-ils **dédiés** à l'administration ? | `[ ]` | `[ ]` |
| 8 | Les comptes utilisés chez nous nous sont-ils propres ? | `[ ]` | `[ ]` |
| 9 | Comment cloisonnez-vous vos clients ? | `[ ]` | `[ ]` |
| 10 | Les actions d'administration sont-elles journalisées, et pouvons-nous obtenir ces journaux ? | `[ ]` | `[ ]` |
| 11 | **Quel est votre propre niveau de MCS, et comment le démontrez-vous ?** | `[ ]` | `[ ]` |
| 12 | Quelles données conservez-vous, où, et comment les restituez-vous en fin de contrat ? | `[ ]` | `[ ]` |

**Cotation** : `[ ]` réponse documentée avec preuve · `[ ]` réponse déclarative · `[ ]` sans réponse. Toute question sans réponse devient une ligne de risque documentée.

---


## D.11 — Journal de crise vulnérabilité

**Identifiant** `CRI-[aaaa]-[nnn]` · **Pilote** `[nom]` · **Greffier** `[nom]` · **Ouverture** `[date, heure]`

| Heure | Information reçue | **Source** | Statut | Décision | Décideur | Action | Responsable | Échéance |
|---|---|---|---|---|---|---|---|---|
| `[hh:mm]` | `[ ]` | `[ ]` | `[fait/hypothèse/piste]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Encadré permanent — état de la connaissance**

| Question | Réponse à l'instant `[hh:mm]` |
|---|---|
| Depuis quand l'actif est-il exposé et vulnérable ? | `[ ]` |
| Quels journaux couvrent cette période ? | `[ ]` |
| Permettraient-ils de détecter ce type d'exploitation ? | `[ ]` |
| **Peut-on établir l'absence de compromission ?** | `[ ] oui  [ ] non — préciser` |

**Clôture** : critères de sortie atteints `[ ]` · mesures d'urgence levées ou converties en compensations `[ ]` · retour d'expérience planifié le `[ ]`

---


## D.12 — Matrice de responsabilité cloud

**Identifiant** `RESP-CLOUD-[nn]` · **Revue** `[semestrielle]`

| Service | Modèle | Le fournisseur maintient | Nous maintenons | Fenêtre imposée | Préavis | **Preuve disponible** | Propriétaire |
|---|---|---|---|---|---|---|---|
| `[ ]` | `[IaaS/PaaS/SaaS/fonctions]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ] oui [ ] non` | `[ ]` |

**Ligne obligatoire par service** : version actuellement utilisée `[ ]` · **date de fin de support de cette version** `[ ]` · source `[ ]`.

**Validation** — Toute ligne dont la colonne « preuve disponible » est vide alimente l'annexe des périmètres non couverts de D.1.

---


## D.13 — Dossier de preuves

**Identifiant** `PRV-[aaaa]` · **Constitué en continu** · **Responsable** `[nom]`

| # | Pièce | Présente | Date de la dernière mise à jour | Emplacement |
|---|---|---|---|---|
| 1 | Périmètre de référence daté, avec sources réconciliées et zones non couvertes | `[ ]` | `[ ]` | `[ ]` |
| 2 | Politique MCS approuvée (D.1) | `[ ]` | `[ ]` | `[ ]` |
| 3 | RACI et comitologie (D.3) | `[ ]` | `[ ]` | `[ ]` |
| 4 | Arbre de décision de triage, daté et validé | `[ ]` | `[ ]` | `[ ]` |
| 5 | Journaux de campagne, dont traîne longue qualifiée | `[ ]` | `[ ]` | `[ ]` |
| 6 | **Preuves d'état sur échantillon**, indépendantes des outils | `[ ]` | `[ ]` | `[ ]` |
| 7 | Registre des dérogations (D.4) | `[ ]` | `[ ]` | `[ ]` |
| 8 | Registre des exclusions (scan, protection des postes) | `[ ]` | `[ ]` | `[ ]` |
| 9 | Comptes rendus de comité, avec **décisions** | `[ ]` | `[ ]` | `[ ]` |
| 10 | Indicateurs historisés, avec définitions et ruptures marquées | `[ ]` | `[ ]` | `[ ]` |
| 11 | Procès-verbaux de décommissionnement (D.14) | `[ ]` | `[ ]` | `[ ]` |

**Contrôle de crédibilité** — Si les dates de production de plus de la moitié des pièces sont groupées sur moins d'un mois, le dossier a été reconstitué : cela se voit, et cela se retourne contre vous (§39.2).

---


## D.14 — Procès-verbal de décommissionnement

**Identifiant** `PVD-[aaaa]-[nnn]` · **Actif** `[ ]` · **Mis en service le** `[ ]`

| # | Étape | Fait | Date | Preuve | Responsable |
|---|---|---|---|---|---|
| 1 | Usage réel mesuré avant décision | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 2 | Décision de retrait et préavis diffusé | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 3 | **Extinction avant suppression**, observation ≥ 1 cycle métier | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 4 | Dépendances identifiées et traitées | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 5 | Données migrées / archivées / **effacées avec attestation** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 6 | Enregistrements de noms et alias supprimés | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 7 | Publications externes retirées, vérifiées depuis l'extérieur | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 8 | Règles de filtrage supprimées | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 9 | **Comptes, clés, secrets, jetons, autorisations déléguées révoqués côté fournisseur** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 10 | Certificats traités (révocation **ou** destruction de clé documentée) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 11 | Retrait des outils, **historiques préservés** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 12 | Décision sur les sauvegardes, avec date de suppression | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 13 | Matériel et licences traités | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 14 | Contrats résiliés | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 15 | **Vérification à J+[90]** — contrôles du §35.11 | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Signatures** — Propriétaire métier `[nom, date]` · Propriétaire technique `[nom, date]`

**Validation** — Le décommissionnement n'est pas clos tant que la ligne 15 n'est pas renseignée. Un PV sans double signature est irrecevable.

---
