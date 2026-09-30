---
title: D.10 — Questionnaire fournisseur
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - ANNEXES
  - index.md
---

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
