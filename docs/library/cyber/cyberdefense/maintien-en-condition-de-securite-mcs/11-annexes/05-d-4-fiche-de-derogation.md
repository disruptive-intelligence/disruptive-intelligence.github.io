---
title: D.4 — Fiche de dérogation
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
---

**Identifiant** `DER-[aaaa]-[nnn]` · **Version** `[ ]` · **Date d'émission** `[ ]`

| Champ | | Valeur |
|---|---|---|
| Objet précis | (O) | `[actif(s) · vulnérabilité ou écart · correctif concerné]` |
| Type d'impossibilité | (O) | `[ ] technique  [ ] contractuelle  [ ] métier  [ ] budgétaire  [ ] temporelle` |
| **Analyse de risque, en termes métier** | (O) | `[ce qui se passe si le risque se réalise : données, service, personnes, conséquences contractuelles]` |
| Exposition mesurée | (O) | `[ ] Internet  [ ] réseau bureautique  [ ] réseau d'administration  [ ] isolé` |
| Exploitation observée | (O) | `[ ] non  [ ] dans le monde  [ ] dans le secteur  [ ] indices chez nous` |
| Mesures compensatoires | (O) | `[1. ]  [2. ]  [3. ]` — hiérarchie du §20.2, en indiquant les rangs écartés et pourquoi |
| **Moyen de vérification** | (O) | `[test précis prouvant que la compensation est active]` |
| Fréquence du contrôle | (O) | `[mensuelle]` |
| Coût opérationnel | (O) | `[h/mois]` |
| Propriétaire de la compensation | (O) | `[nom]` |
| **Signataire** | (O) | `[nom, fonction — selon la grille C.4]` |
| Date de début | (O) | `[ ]` |
| **Date d'expiration** | (O) | `[date du calendrier, alignée sur un événement décisionnel réel]` |
| Conditions de sortie | (O) | `[correction réalisée]  [exploitation observée]  [changement d'exposition]` |
| **Conditions de révocation anticipée** | (O) | `[événements imposant de mettre fin immédiatement à la dérogation]` |
| Nombre de renouvellements | (O) | `[0]` — chaque renouvellement remonte d'un niveau de signature |
| Date de revue | (O) | `[trimestrielle]` |

**Règles de validation** — Rejet automatique si : pas de date d'expiration ou date exprimée en événement flou · compensation sans moyen de vérification · signataire non conforme à la grille C.4 · risque décrit en termes techniques uniquement.

**Quatre notions que le terrain confond, et qu'il faut séparer par écrit**

| Notion | Nature | Durée | Signataire | Ce qui la clôt |
|---|---|---|---|---|
| **Dérogation** | Exception temporaire à une règle existante | **Bornée** | Propriétaire métier, niveau selon C.4 | La correction, ou une condition de sortie |
| **Acceptation de risque** | Décision durable de porter un risque résiduel | **Non bornée**, mais revue | Niveau supérieur, selon C.4 | Une revue qui change la décision |
| **N/A** | La règle ne s'applique pas à cet actif | Permanente tant que le contexte tient | Propriétaire technique | Un changement de contexte |
| **Faux positif** | Le constat était erroné | Définitive | Analyste, **avec démonstration** | — |

⚠️ **Le mot « exception » recouvre les quatre dans le langage courant**, et il désigne en plus les exclusions d'outil (§15.6, §34.4). C'est la principale source d'ambiguïté d'un registre de dérogations. La règle interne : le mot « exception » ne figure dans aucun document formel de ce dispositif — on écrit toujours laquelle des cinq choses on désigne.

---


## D.5 — Demande de changement urgent

**Identifiant** `CHG-U-[aaaa]-[nnn]` · **Émission** `[date, heure]` · **Régularisation attendue sous** `[48 h]`

| Section | Contenu |
|---|---|
| Constat et qualification | `[identifiant · statut : fait vérifié / hypothèse / piste · source]` |
| Exposition mesurée | `[nombre d'actifs · joignables depuis · depuis quand]` |
| Chemin dans l'arbre de décision | `[reproduire les réponses aux questions ① à ⑥]` |
| Justification de l'urgence | `[critère de déclenchement satisfait]` |
| Périmètre de l'intervention | `[liste ou requête d'actifs]` |
| **Écart recette / production** | `[versions · volumétrie · intégrations · configuration — chacun qualifié]` |
| **Critères go/no-go** | Renvoi D.6, **joints obligatoirement** |
| **Plan de retour arrière** | Renvoi D.7, **joint obligatoirement** |
| Point de non-retour | `[instant précis]` ou `[aucun]` |
| Décideur nommé | `[nom]` |
| Décideur du retour arrière | `[nom]` — peut différer |
| Communication prévue | `[direction] [métiers] [utilisateurs] [clients] [assureur] [autorités]` |
| Preuve à produire | `[nature · échantillon · responsable]` |

**Validation** — Le changement ne peut être exécuté sans D.6 et D.7 joints, ni sans décideur nommé pour le retour arrière.

---


## D.6 — Critères go / no-go

**Identifiant** `GNG-[aaaa]-[nnn]` · **Rattaché à** `[CHG-...]` · **Écrit le** `[avant l'intervention]`

| Indicateur | Seuil d'arrêt | Mesuré par | Fenêtre d'observation |
|---|---|---|---|
| Taux d'échec d'installation | `[> 5 %]` | `[outil]` | `[continu]` |
| Incidents déclarés liés | `[≥ 3 sur l'anneau]` | `[support]` | `[24 h]` |
| **Indicateur fonctionnel métier** (O) | `[baisse > 10 % sur 30 min]` | `[supervision]` | `[continu]` |
| Redémarrages inattendus | `[≥ 2 machines]` | `[supervision]` | `[continu]` |
| Temps de réponse | `[+ 50 % sur 15 min]` | `[supervision]` | `[continu]` |

**Critère de passage à l'anneau suivant** : `[tous les seuils respectés pendant [n] jours ET aucun incident bloquant ouvert]`

**Validation** — Au moins un indicateur **fonctionnel** est obligatoire : un service peut répondre correctement tout en ayant cessé de faire son travail (§6.8). Un formulaire rempli après le début de l'intervention est irrecevable.

---


## D.7 — Plan de retour arrière

**Identifiant** `RB-[aaaa]-[nnn]` · **Rattaché à** `[CHG-...]`

| Champ | Valeur |
|---|---|
| Mécanisme retenu | `[ ] instantané  [ ] sauvegarde  [ ] redéploiement d'image  [ ] désinstallation vérifiée  [ ] double partition  [ ] bascule bleu/vert` |
| **Testé le** (O) | `[date]` — sur `[topologie représentative : oui/non, écarts]` |
| **Durée mesurée** (O) | `[hh:mm]` |
| Périmètre couvert | `[ ] binaires  [ ] configuration  [ ] schéma de données  [ ] caches  [ ] files de messages  [ ] effets externes` |
| **Point de non-retour** (O) | `[instant précis]` ou `[aucun]` |
| Ce que le retour arrière **ne restaure pas** | `[transactions depuis l'instantané · état des systèmes tiers · notifications déjà émises]` |
| Critère de déclenchement | `[renvoi D.6]` |
| Décideur | `[nom]` |
| Vérification post-retour | `[contrôles à réaliser pour confirmer l'état antérieur]` |

**Validation** — Un plan dont la durée n'a pas été chronométrée sur une topologie représentative n'est pas un plan : c'est une intention (§18.8).

---


## D.8 — Fiche d'obsolescence d'actif

**Identifiant** `OBS-[aaaa]-[nnn]`

| Champ | Valeur |
|---|---|
| Actif ou population | `[ ]` · Nombre `[ ]` |
| Composant concerné | `[système / base de données / runtime / matériel / micrologiciel]` |
| **Date de fin de support** | `[ ]` · Type : `[ ] fonctionnelle [ ] support [ ] support de sécurité [ ] support étendu` |
| **Source et date de vérification** | `[page officielle, consultée le ...]` |
| Criticité / exposition | `[C1-C4]` / `[ ]` |
| Éligibilité au support étendu | `[ ] vérifiée actif par actif — résultat : [ ]` |

**Trois options chiffrées, sur la durée complète** *(le statu quo est obligatoire)*

| Option | Coût total | Risque résiduel | Faisabilité |
|---|---|---|---|
| Support étendu `[n]` ans | `[ ]` | `[ ]` | `[ ]` |
| Migration / remplacement | `[ ]` | `[ ]` | `[ ]` |
| **Statu quo** | `[compensations + urgences + astreinte + risque]` | `[ ]` | `[ ]` ou `[indisponible : motif]` |
| Retrait du service | `[ ]` | `[ ]` | `[ ]` |

**Décision** `[option]` · **Décideur** `[nom]` · **Date** `[ ]` · **Financement** `[exercice, montant]` · **Jalons** `[ ]` · **Point de non-retour** `[ ]`

---
