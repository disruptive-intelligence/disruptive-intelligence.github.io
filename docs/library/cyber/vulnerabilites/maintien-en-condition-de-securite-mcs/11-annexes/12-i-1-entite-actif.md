---
title: I.1 Entité ACTIF
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
---

| Champ | Type | Card. | Valeurs contrôlées / format | Obligatoire à la création |
|---|---|---|---|---|
| `id_actif` | str | 1 | Identifiant interne stable, **jamais réutilisé** | Oui |
| `ids_sources` | str | 0..n | `{source}:{identifiant natif}` — un par outil | Non |
| `nom` | str | 1 | Nom d'usage | Oui |
| `type` | enum | 1 | serveur · poste · mobile · réseau · sécurité · hyperviseur · conteneur · industriel · périphérique · service_en_ligne · identité_applicative · certificat | Oui |
| `proprietaire_metier` | ref | 0..1 | Personne ou rôle géré | Non — un actif découvert s'enregistre **sans** propriétaire |
| `suppleant_metier` | ref | 0..1 | | Non |
| `proprietaire_technique` | ref | 0..1 | | Non |
| `suppleant_technique` | ref | 0..1 | | Non |
| `criticite` | enum | 0..1 | C1 · C2 · C3 · C4 | Non |
| `exposition` | enum | 0..1 | internet · bureautique · administration · industriel · isolé · inconnue | Non |
| `environnement` | enum | 1 | production · recette · développement · laboratoire · formation · secours | Oui |
| `classification_donnees` | enum | 0..1 | publique · interne · confidentielle · sensible | Non |
| `perimetre_reglementaire` | enum | 0..n | santé · paiement · industriel · produit · aucun | Non |
| `systeme` / `version` | str | 0..1 | | Non |
| `composants` | ref | 0..n | → COMPOSANT | Non |
| `statut_support` | enum | 0..1 | supporté · support_étendu · hors_support · inconnu | Non |
| `date_fin_support` | date | 0..1 | | Non |
| `source_fin_support` | str | 0..1 | Référence + date de consultation | Si `date_fin_support` renseignée |
| `fournisseur` / `contrat` | ref | 0..1 | | Non |
| `fenetre_maintenance` | str | 0..1 | Expression récurrente | Non |
| `outils_couverture` | ref | 0..n | → OUTIL, avec rôle (déploiement / scan / protection / sauvegarde) | Non |
| **`first_seen`** | date | 1 | Première observation, toutes sources | Oui (automatique) |
| **`last_seen`** | date | 1 | Dernière observation | Oui (automatique) |
| **`confiance`** | enum | 1 | confirmée · probable · à_vérifier | Oui |
| **`source_decouverte`** | enum | 1 | cmdb · annuaire · scan · agent · hyperviseur · api_cloud · orchestrateur · comptabilité · déclaration · manuel | Oui |
| **`statut_cycle_vie`** | enum | 1 | découvert · en_service · orphelin · en_extinction · décommissionné | Oui |
| `motif_disparition` | enum | 0..1 | décommissionné · renommé · migré · perdu_de_vue · doublon | Si statut = décommissionné |
| `derniere_tentative_scan` | date | 0..1 | | Non |
| `dernier_succes_scan` | date | 0..1 | **Distinct du précédent** | Non |
| `derniere_preuve_conformite` | ref | 0..1 | → PREUVE | Non |
| `derogations_en_cours` | ref | 0..n | → DEROGATION | Non |

⚠️ **Aucun champ de propriété n'est obligatoire à la création.** Un actif découvert sans propriétaire doit pouvoir être enregistré avec `statut_cycle_vie = orphelin` — le rejeter par contrainte de champ obligatoire revient à effacer précisément ce qu'on cherche à découvrir.


### I.2 Entités liées

| Entité | Champs clés |
|---|---|
| **COMPOSANT** | `id` · `actif` (ref) · `type` (base_de_données / runtime / serveur_applicatif / bibliothèque / micrologiciel / pilote) · `nom` · `version` · `statut_support` · `date_fin_support` · `proprietaire_couche` (ref) |
| **CONSTAT** | `id` · `origine` (scan / avis / pentest / audit / incident / bug_bounty / configuration / secret / architecture) · `identifiant_externe` (0..1) · `statut_qualification` · `actifs` (0..n) · `decision_triage` · `horloge_risque_debut` · `horloge_sla_debut` · `temps_suspendu` |
| **DEROGATION** | Les champs de D.4 · `actifs` (0..n) · `nb_renouvellements` · `signataire` · `date_expiration` |
| **PREUVE** | `id` · `type` (état_constaté / rapport_console / journal / attestation) · `date_collecte` · `perimetre` · `methode` · `actifs_non_joignables` · `empreinte` |
| **OUTIL** | `id` · `nom` · `role` · `perimetre_theorique` · `date_derniere_extraction` · `format_export` |
| **CONTRAT** | `id` · `fournisseur` · `perimetre` · `delais_engages` · `restitution_donnees` (bool) · `date_echeance` |


### I.3 Relations

| Relation | Cardinalité |
|---|---|
| ACTIF `dépend de` ACTIF | 0..n |
| ACTIF `est construit depuis` MODELE | 0..1 |
| ACTIF `est couvert par` OUTIL | 0..n, avec rôle |
| ACTIF `porte` COMPOSANT | 0..n |
| ACTIF `utilise` COMPTE | 0..n |
| CONSTAT `affecte` ACTIF | 1..n |
| DEROGATION `couvre` CONSTAT | 1..n |
| PREUVE `atteste` ACTIF `pour` CONSTAT | 1..n |


### I.4 Périmètre maître et populations éligibles

Le périmètre de référence est le **périmètre maître** : l'union de tout ce qui est connu.

```
Périmètre maître = ∪ (toutes les sources d'inventaire)
   incluant : actifs orphelins · actifs en extinction · actifs de service
   excluant : rien — les exclusions sont documentées, jamais retirées
```


⚠️ **Le périmètre maître n'est pas le dénominateur de tout indicateur.** Un service en ligne n'est pas éligible à un indicateur de correctif système ; un automate n'est pas éligible au scan actif ; un actif arrêté en cours de décommissionnement n'est pas éligible à la conformité aux correctifs ; un certificat ne s'évalue pas avec les contrôles d'un serveur. Utiliser le périmètre maître comme dénominateur universel produit des taux artificiellement bas et indéfendables.

| Notion | Définition | Champ correspondant |
|---|---|---|
| **Périmètre maître** | Tout ce qui est connu, sans exclusion silencieuse | tous les ACTIF |
| **Population éligible** | Sous-ensemble auquel le contrôle **s'applique** | filtre explicite par indicateur |
| **Population mesurée** | Actifs éligibles effectivement évalués | `dernier_succes_scan` renseigné |
| **N/A** | Hors population éligible, **avec motif** | `motif_na` |
| **Non mesuré** | Éligible mais non évalué. **Jamais conforme par défaut** | éligible ∧ `dernier_succes_scan` vide |


### I.5 Règles de qualité et contrôles

| # | Règle | Requête | Fréquence |
|---|---|---|---|
| 1 | Aucun actif en service sans deux propriétaires | `statut = en_service ∧ (prop_metier vide ∨ prop_tech vide)` | Mensuelle |
| 2 | Aucun actif en service sans criticité ni exposition | `statut = en_service ∧ (criticite vide ∨ exposition vide)` | Mensuelle |
| 3 | Date de fin de support renseignée ou motif | `date_fin_support vide ∧ motif vide` | Trimestrielle |
| 4 | Couverture ou exclusion documentée | `outils_couverture vide ∧ exclusion vide` | Mensuelle |
| 5 | Actif décommissionné avec PV | `statut = décommissionné ∧ pv vide` | Trimestrielle |
| 6 | Actif non revu depuis N jours | `last_seen < aujourd'hui - 90` | Mensuelle |
| 7 | Écart entre sources supérieur au seuil | Réconciliation (§10.3) | Mensuelle |
| 8 | Orphelin depuis plus de 30 jours | `statut = orphelin ∧ first_seen < -30 j` | Mensuelle |


### I.6 Exemple d'enregistrement

```yaml
id_actif: SRV-0142
ids_sources: [cmdb:CI00873, scan:asset-51190, hyperviseur:vm-2201]
nom: srv-app-crm-02
type: serveur
proprietaire_metier: directeur.commercial
proprietaire_technique: m.ferhaoui
criticite: C2
exposition: bureautique
environnement: production
classification_donnees: confidentielle
systeme: "Linux LTS 12"
version: "12.7"
composants:
  - {type: runtime, nom: "runtime applicatif A", version: "8.3", statut_support: hors_support,
     date_fin_support: 2023-03-31, proprietaire_couche: equipe.applicative}
statut_support: supporté
date_fin_support: 2028-06-30
source_fin_support: "page officielle éditeur, consultée le 30/07/2026"
first_seen: 2019-04-11
last_seen: 2026-07-29
confiance: confirmée
source_decouverte: cmdb
statut_cycle_vie: en_service
dernier_succes_scan: 2026-07-28
derogations_en_cours: [DER-2027-014]
```


---


## Annexe J — Workflow et modèle de ticket de remédiation


### J.1 États et transitions

```
NOUVEAU ──qualification──► QUALIFIÉ ──────► FAUX POSITIF (clos + démonstration)
                              │
                         triage (§16.3)
                              ▼
                          AFFECTÉ ◄──────► CONFLIT DE PROPRIÉTÉ (délai borné)
                              │                      │
                      acceptation propriétaire       └──► arbitrage comité
                              ▼
                          PLANIFIÉ ────────► DÉROGATION (ouvert, D.4)
                              │              RISQUE ACCEPTÉ (ouvert, durable)
                              ▼              N/A (clos, motif)
                       EN CORRECTION
                              ▼
                        À VÉRIFIER ────────► ÉCHEC ──► retour à PLANIFIÉ
                              ▼
                            CLOS ◄────────── NOUVELLE OCCURRENCE (ticket lié)
```



### J.2 Droits de transition

| Transition | Qui peut la déclencher |
|---|---|
| Nouveau → Qualifié | Analyste sécurité |
| Qualifié → Faux positif | Analyste sécurité, **avec démonstration jointe** |
| Qualifié → Affecté | Automatique, depuis le propriétaire d'actif |
| Affecté → Conflit de propriété | Propriétaire désigné, sous 5 j ouvrés |
| Conflit → Affecté | Comité MCS uniquement |
| Planifié → Dérogation | Propriétaire métier (signature D.4) |
| Planifié → Risque accepté | Selon grille C.4 |
| À vérifier → Clos | **Seulement avec preuve rattachée** |
| Clos → réouverture | Interdite : créer une **nouvelle occurrence liée** (J.6) |


### J.3 Champs obligatoires par état

| État | Exigences |
|---|---|
| Qualifié | Statut de qualification · actifs confirmés · vérification d'activation · **origine du constat** |
| Affecté | Propriétaire nominatif · échéance SLA · **chemin dans l'arbre reproduit** |
| Planifié | Fenêtre ou campagne · plan de retour arrière (D.7) |
| En correction | Date de début · intervenant |
| À vérifier | Date d'action · méthode de vérification prévue |
| Clos | **Preuve** conforme aux six champs du §2.9 |
| Dérogation | Les champs de D.4 |
| Risque accepté | Signataire selon C.4 · date de revue · **pas de date d'expiration** (c'est ce qui le distingue de la dérogation) |
| N/A | Motif documenté · population éligible d'origine |


### J.4 Les deux horloges

| Élément | Règle |
|---|---|
| **Horloge de risque** | Départ : connaissance pertinente ou disponibilité d'une correction. **Ne se suspend jamais.** Publiée à la direction |
| **Horloge de traitement (SLA)** | Même départ, suspensions limitativement définies. Pilote l'équipe |
| Compteur complémentaire | Depuis la **détection** → réactivité de la veille |
| Suspensions admises (SLA uniquement) | Attente de correctif éditeur · attente d'information demandée par écrit · gel de production |
| Condition d'une suspension > 5 j | **Mesure compensatoire engagée ou acceptation formelle** |
| Temps suspendu | **Mesuré et affiché séparément** |
| Écart entre les deux horloges | Indicateur de premier plan : sa croissance signale un problème structurel |


### J.5 Règles de déduplication et modèle parent / enfants

| Règle | Application |
|---|---|
| Même identifiant sur plusieurs actifs | **Un** ticket parent, une occurrence enfant par actif |
| Constats corrigés par le **même correctif** | Un ticket parent |
| Même constat remonté par deux outils | Un ticket, deux sources tracées |
| Actifs de propriétaires, fenêtres ou criticités différents | **Occurrences enfants distinctes**, avec leurs propres échéances |

⚠️ Le parent porte la décision de triage et la cause racine ; **les enfants portent l'échéance, le propriétaire et la preuve**. Un parent ne se clôt que lorsque toutes ses occurrences sont closes ou qualifiées.


### J.6 Réouverture ou nouvelle occurrence

| Situation | Traitement |
|---|---|
| Le constat n'avait jamais été réellement corrigé | **Réouverture** de l'occurrence : le délai continue de courir |
| Le constat réapparaît après une correction vérifiée | **Nouvelle occurrence**, liée au ticket parent et à l'occurrence précédente |

Le second cas préserve la justesse des indicateurs de délai tout en rendant la **récurrence visible** : trois occurrences liées sur le même parent signalent une cause racine non traitée (§17.9), presque toujours un modèle ou une image de référence.


### J.7 Escalade — paramétrable par classe

| Déclencheur | C1 | C2 | C3 | Destinataire |
|---|---|---|---|---|
| Pas de réponse du propriétaire | 2 j | 5 j | 10 j | Responsable hiérarchique |
| Conflit de propriété non résolu | 3 j | 5 j | 10 j | Comité MCS |
| Échéance SLA dépassée | Immédiat | 5 j | 15 j | Comité MCS |
| Suspension prolongée | 10 j | 20 j | 30 j | Comité MCS |
| Constat non qualifié depuis | 90 j | 180 j | 180 j | **DSI — requalification obligatoire** |


### J.8 Issues et preuve exigée

| Issue | Nature | Preuve |
|---|---|---|
| **Corrigé** | Définitive | État constaté postérieur à l'action |
| **Atténué** | Temporaire | Mesure décrite, vérifiée active, **date d'expiration** |
| **Dérogation** | Temporaire, bornée | Fiche D.4 signée |
| **Risque accepté** | Durable | Signature C.4, revue périodique, **horloge de risque toujours active** |
| **N/A** | Définitive | Motif et population éligible d'origine |
| **Faux positif** | Définitive | **Démonstration vérifiable par un tiers** |
| **Sans objet** | Définitive | PV de décommissionnement (D.14) |

---


## Annexe K — Dictionnaire d'indicateurs et modèle de maturité
