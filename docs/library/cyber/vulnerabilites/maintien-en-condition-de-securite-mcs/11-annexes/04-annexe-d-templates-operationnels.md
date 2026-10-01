---
title: Annexe D — Templates opérationnels
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
---

> **Quatorze formulaires remplissables.** Chacun porte un identifiant, une version et une date. Les champs `[ ]` sont à compléter, les champs marqués **(O)** sont obligatoires, **(F)** facultatifs. Les règles de validation indiquent ce qui bloque l'acceptation du document.
>
> ⚠️ Les valeurs numériques proposées (délais, seuils, durées) constituent un **modèle de référence de ce cours**, à adapter et faire approuver par votre organisation. Elles ne sont ni une norme ni une exigence externe.

---


## D.1 — Politique MCS

**Identifiant** `POL-MCS-[nn]` · **Version** `[x.y]` · **Date** `[jj/mm/aaaa]` · **Approbateur** `[nom, fonction]` · **Revue** `[annuelle]`

| § | Section | Contenu attendu | Longueur |
|---|---|---|---|
| 1 | Objet et périmètre | Ce qui est couvert · **ce qui ne l'est pas, et pourquoi** | ½ p. |
| 2 | Définitions | Actif · propriétaire · couverture · conformité · population éligible · non mesuré | 1 p. |
| 3 | Rôles | Renvoi au RACI D.3, décideurs nommés par type de décision | 1 p. |
| 4 | Classes de service | Le formulaire D.2 intégré | 2-3 p. |
| 5 | Processus | Veille · détection · triage · remédiation · vérification · preuve | 2-3 p. |
| 6 | Dérogations | Renvoi à D.4, niveaux de signature, règle de renouvellement | 1 p. |
| 7 | Mesure et contrôle | Indicateurs publiés, fréquence, destinataires | 1 p. |
| Ann. | **Périmètres non couverts** | Tableau ci-dessous | 1 p. |

**Annexe obligatoire — périmètres déclarés non couverts**

| Périmètre | Motif de non-couverture | Propriétaire désigné | Échéance de première mesure | Compensation en place |
|---|---|---|---|---|
| `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Règles de validation** — La politique ne peut être approuvée si : un délai annoncé n'a pas été confronté à une mesure de capacité (§16.5) · la procédure de dérogation est absente · l'annexe des périmètres non couverts est vide sans justification écrite.

---


## D.2 — Table des classes de service

**Identifiant** `CLS-[nn]` · **Version** `[ ]` · **Approbateur** `[DSI]`

| Paramètre | C1 — critique/exposé | C2 — important | C3 — courant | C4 — contraint |
|---|---|---|---|---|
| **Définition** (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| **Exemples d'actifs** (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Délai — vulnérabilité exploitée (O) | `[72 h]` | `[7 j]` | `[30 j]` | `[compensation 72 h]` |
| Délai — critique non exploitée (O) | `[15 j]` | `[30 j]` | `[60 j]` | `[compensation/dérogation]` |
| Délai — autres (O) | `[30 j]` | `[90 j]` | `[180 j]` | `[fenêtre constructeur]` |
| Fréquence de vérification (O) | `[hebdo]` | `[mensuelle]` | `[mensuelle]` | `[trimestrielle]` |
| Niveau de test (O) | `[recette + témoin]` | `[témoin]` | `[anneau pilote]` | `[validation fournisseur]` |
| Fenêtre (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Délai d'observation (F) | `[0-3 j]` | `[5 j]` | `[5 j]` | `[n/a]` |

**Validation** — Chaque délai doit être accompagné de la mesure de capacité qui le justifie. Un délai non tenu trois mois consécutifs déclenche une révision de la classe ou de la capacité.

---


## D.3 — RACI du MCS

**Identifiant** `RACI-MCS-[nn]` · **Version** `[ ]` · **Périmètre** `[IT / OT / cloud / produit]`

**R** réalise · **A** approuve (un seul par ligne) · **C** consulté · **I** informé

| Activité | RSSI | Exploitation | Propr. métier | DSI | Prestataire |
|---|---|---|---|---|---|
| Définir la politique et les classes | `[R]` | `[C]` | `[C]` | `[A]` | `[I]` |
| Tenir l'inventaire | `[C]` | `[R/A]` | `[C]` | `[I]` | `[R]` |
| Veille et qualification | `[R/A]` | `[C]` | `[I]` | `[I]` | `[C]` |
| Prioriser et fixer les délais | `[R]` | `[C]` | `[C]` | `[A]` | `[I]` |
| Planifier et exécuter | `[I]` | `[R/A]` | `[C]` | `[I]` | `[R]` |
| **Décider d'une interruption** | `[C]` | `[C]` | `[A]` | `[I]` | `[I]` |
| **Accorder une dérogation** | `[R]` | `[C]` | `[A]` | `[C]` | `[I]` |
| Produire la preuve | `[C]` | `[R]` | `[I]` | `[I]` | `[R]` |
| Escalader une impossibilité | `[C]` | `[R]` | `[C]` | `[A]` | `[R]` |
| Contrôler l'application | `[R/A]` | `[C]` | `[I]` | `[I]` | `[I]` |

**Validation** — Un seul **A** par ligne. Toute case **A** doit correspondre à une personne nommée disposant du mandat correspondant, pas à une entité collective.

---
