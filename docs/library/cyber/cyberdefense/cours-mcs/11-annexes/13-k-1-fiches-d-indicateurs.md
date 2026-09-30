---
title: K.1 Fiches d'indicateurs
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - ANNEXES
  - index.md
---

*Format complet : formule · numérateur · **population éligible** · dénominateur publié · période · exclusions et N/A · source · propriétaire · fréquence · seuils.*

⚠️ La population éligible se définit **par indicateur** (Annexe I.4). Le périmètre maître est le point de départ, jamais le dénominateur par défaut.

---

**K1 — Couverture d'inventaire**
Formule : `actifs identifiés / actifs estimés du périmètre × 100` · Numérateur : actifs enregistrés · Population éligible : tous types · Dénominateur : estimation argumentée du parc réel · Période : instantané mensuel · Exclusions : aucune · Source : réconciliation multi-sources · Propriétaire : exploitation · Seuils : `< 90 %` alerte, `< 80 %` blocage de tout autre indicateur.

**K2 — Couverture de scan**
Formule : `actifs scannés avec succès / actifs éligibles au scan × 100` · Numérateur : `dernier_succes_scan` dans la période · **Population éligible : actifs scannables** — exclut services en ligne, industriels non scannables, certificats · Dénominateur : population éligible, publié · Exclusions : documentées, listées avec l'indicateur · N/A : motif obligatoire · Fréquence : mensuelle · Seuils : `< 90 %` alerte.

**K3 — Conformité de correctifs**
Formule : `actifs conformes / actifs mesurés × 100` · **Population éligible** : actifs porteurs du composant concerné · Trois valeurs à publier ensemble : conformité dans la population mesurée · **ratio confirmé conforme sur périmètre** (K3 × K2) · **part non mesurée** · Fréquence : mensuelle.

**K4 — Respect des délais**
Formule : `constats clos dans le délai / constats arrivés à échéance × 100` · Population éligible : constats avec échéance SLA dans la période · Exclusions : suspendus — **mais leur horloge de risque reste publiée** · Publier : médiane, **P90**, maximum, volume · Seuils : `< 85 %` alerte.

**K5 — Âge du backlog**
Formule : distribution des durées depuis la première détection · Publier : **médiane · P90 · P95 · maximum · volume de population** · Population éligible : constats ouverts · Piège : la moyenne masque la traîne, le maximum peut être dominé par un cas aberrant.

**K6 — Dette critique échue**
Formule : nombre absolu de constats critiques dont le délai est dépassé · **Jamais en taux** · Population éligible : constats de gravité critique · Fréquence : hebdomadaire · Seuil : toute valeur `> 0` sur actif exposé déclenche une revue.

**K7 — Dérogations**
Trois valeurs : nombre ouvert · **âge moyen et P90** · **nombre renouvelées ≥ 1 fois** · Le nombre seul n'est pas interprétable (§38.9) · Fréquence : mensuelle · Seuil : toute dérogation renouvelée deux fois remonte en comité de direction.

**K8 — Taux de récurrence**
Formule : `occurrences réapparues / occurrences closes sur la période × 100` · Population éligible : occurrences closes il y a plus de 30 jours · Interprétation : signale une cause racine (modèle, image, restauration), pas une mauvaise exécution · Seuil : `> 10 %` déclenche une analyse de cause racine.

**K9 — Taux de retour arrière**
Formule : `déploiements annulés / déploiements réalisés × 100` · Piège : un taux **nul** peut signaler qu'on ne teste pas ou qu'on n'ose pas revenir en arrière · Seuils : `> 10 %` qualité de validation insuffisante ; `= 0 %` sur 12 mois, examiner.

**K10 — Taux d'échec de déploiement**
Formule : `actifs en échec / actifs ciblés × 100` · **Les non-joignables comptent au dénominateur** et sont publiés séparément · Fréquence : par campagne.

**Indicateurs complémentaires** : âge des images et modèles · temps sans redémarrage (P90) · part de changements d'urgence (seuil 15-20 %) · fraîcheur du contenu de détection · nombre d'actifs exposés et tendance · nombre d'orphelins · part des technologies couvertes par une source de veille · âge des exclusions · **écart entre horloge de risque et horloge SLA**.


### K.2 Règles de publication

1. Tout taux est publié **avec son dénominateur, sa population éligible et sa date**.
2. Les populations non mesurées apparaissent comme **« non mesuré »**, jamais comme conformes ni comme absentes.
3. Les exclusions et les N/A sont listés avec l'indicateur, avec leur motif.
4. Les ruptures — périmètre, outil, modèle de score — sont **marquées sur la série**. Lorsque c'est possible, recalculer la période de transition avec l'ancien et le nouveau modèle et publier les deux.
5. Les délais se publient en **médiane, P90 ou P95, maximum et volume**.
6. Le nombre d'indicateurs est **inversement proportionnel** au niveau hiérarchique.
7. Un produit *conformité × couverture* est un **ratio conservateur**, nommé comme tel.
8. Le temps suspendu au titre du SLA reste compté par **l'horloge de risque**.


### K.3 Modèle de maturité — critères de preuve par niveau

| Niveau | Nom | **Preuve exigée pour l'atteindre** |
|---|---|---|
| 0 | Inexistant | — |
| 1 | Réactif | Traces de corrections réalisées, sans processus documenté |
| 2 | Documenté | Politique approuvée · inventaire constitué et daté · propriétaires nommés sur ≥ 80 % du périmètre |
| 3 | Piloté | Délais définis **et mesurés** · registre de dérogations tenu · indicateurs publiés avec dénominateurs · comptes rendus de comité avec décisions |
| 4 | Industrialisé | Automatisation de la collecte, corrélation et vérification · campagnes tracées avec critères d'arrêt · **preuve d'état sur échantillon produite systématiquement** |
| 5 | Adaptatif | Priorisation par exposition et exploitation documentée · MCS *by design* en revue d'architecture · boucle d'amélioration démontrée sur ≥ 4 trimestres · audit interne par sondages |


### K.4 Grille d'auto-évaluation par domaine

| Domaine | Niveau | Preuve citée | Facteur limitant ? |
|---|---|---|---|
| Inventaire et périmètre | `[0-5]` | `[ ]` | `[ ]` |
| Exposition et chemins d'attaque | `[ ]` | `[ ]` | `[ ]` |
| Veille et sources de constats | `[ ]` | `[ ]` | `[ ]` |
| Triage et priorisation | `[ ]` | `[ ]` | `[ ]` |
| Remédiation et workflow | `[ ]` | `[ ]` | `[ ]` |
| Configuration et dérive | `[ ]` | `[ ]` | `[ ]` |
| Identités, secrets, certificats | `[ ]` | `[ ]` | `[ ]` |
| Applications et dépendances | `[ ]` | `[ ]` | `[ ]` |
| Obsolescence et décommissionnement | `[ ]` | `[ ]` | `[ ]` |
| Contextes spécialisés | `[ ]` | `[ ]` | `[ ]` |
| Mesure et preuve | `[ ]` | `[ ]` | `[ ]` |
| Gouvernance et financement | `[ ]` | `[ ]` | `[ ]` |

**Lecture** — Un niveau élevé dans dix domaines ne compense pas un niveau 1 sur l'inventaire : celui-ci **plafonne** la maturité de tout ce qui en dépend. Identifiez les domaines **critiques pour votre contexte** et traitez-les comme facteurs limitants ; la moyenne des douze notes n'a aucune valeur informative.

---


## Annexe L — Checklists de cycle de vie


### L.1 Mise en production
☐ Déclaré à l'inventaire · ☐ Deux propriétaires nommés · ☐ Criticité et exposition attribuées · ☐ Classe de service · ☐ Couvert par un outil de déploiement et de scan · ☐ Fenêtre définie · ☐ Journalisation activée et exportée · ☐ Sauvegarde configurée et testée · ☐ Grille de maintenabilité du §6.14 renseignée · ☐ Fin de support des composants connue.


### L.2 Campagne périodique
☐ Périmètre défini et rapproché du périmètre de référence · ☐ **Vérification préalable sur 3 actifs représentatifs** · ☐ Qualification du correctif en 6 questions · ☐ Écart recette/production mesuré · ☐ Anneaux définis · ☐ **Critères d'arrêt chiffrés, écrits** · ☐ Plan de retour arrière chronométré · ☐ Décideur nommé · ☐ Vérification post-déploiement · ☐ **Traîne longue qualifiée** · ☐ Preuve archivée.


### L.3 Correctif urgent
☐ Information vérifiée à la source · ☐ Exposition mesurée · ☐ **Réduction d'exposition envisagée en premier** · ☐ Cellule constituée avec greffier · ☐ Délai d'observation supprimé — **critères d'arrêt, retour arrière et preuve conservés** · ☐ Recherche de compromission préalable · ☐ Communication direction et métiers · ☐ Demande de changement régularisée sous 48 h · ☐ Retour d'expérience.


### L.4 Système non patchable
☐ Type d'impossibilité qualifié (5 types) · ☐ **Usage réel mesuré** · ☐ Hiérarchie des compensations parcourue de haut en bas · ☐ Compensation avec les 7 attributs · ☐ Dérogation signée par le propriétaire métier · ☐ Date d'expiration · ☐ Contrôle périodique inscrit au comité · ☐ Plan de fin de vie ou de remplacement.


### L.5 Mise à jour hors ligne (industriel)
☐ Source officielle, compte nominatif · ☐ Poste de téléchargement dédié et durci · ☐ **Vérification de signature ou d'empreinte** (double contrôle) · ☐ Analyse antimalware multi-moteurs (double contrôle) · ☐ Support dédié, effacé, identifié · ☐ Sas de transfert · ☐ Validation constructeur écrite · ☐ Matériel de secours prêt · ☐ Application selon procédure · ☐ Tests fonctionnels et de sûreté · ☐ **Preuve d'installation et journal de transfert**.


### L.6 Renouvellement de certificat
☐ Inventaire à jour · ☐ Alertes à 60/30/7 jours · ☐ Renouvellement automatisé si possible · ☐ Déploiement sur **tous** les points d'usage · ☐ Vérification du certificat effectivement présenté · ☐ Ancien certificat révoqué · ☐ Magasins de confiance mis à jour.


### L.7 Migration de version majeure
☐ Fin de support de la version source confirmée à la source · ☐ Compatibilité applicative validée par l'éditeur, **par écrit** · ☐ Recette représentative sur les 4 axes · ☐ Migration de schéma découpée en expansion/contraction · ☐ **Point de non-retour identifié et écrit** · ☐ Plan de retour arrière testé sur topologie représentative · ☐ Fenêtre et communication · ☐ Vérification fonctionnelle post-migration.


### L.8 Changement de fournisseur
☐ Clauses MCS du §13.3 dans le nouveau contrat · ☐ **Restitution de données obtenue** · ☐ Périmètre nominatif annexé · ☐ Inventaire et historique récupérés de l'ancien prestataire · ☐ Accès de l'ancien prestataire révoqués · ☐ Comptes et clés associés supprimés · ☐ Documentation d'exploitation transférée.


### L.9 Décommissionnement
☐ Usage réel mesuré · ☐ Décision et préavis · ☐ **Extinction avant suppression, observation ≥ 1 cycle métier** · ☐ Dépendances identifiées et traitées · ☐ Données migrées/archivées/effacées avec preuve · ☐ Enregistrements de noms supprimés · ☐ Règles de filtrage supprimées · ☐ **Comptes, clés, secrets, jetons, autorisations déléguées révoqués côté fournisseur** · ☐ Certificats révoqués · ☐ Retrait de tous les outils · ☐ Décision sur les sauvegardes, avec date · ☐ Matériel et licences traités · ☐ Contrats résiliés · ☐ **Vérification à J+90** · ☐ Procès-verbal signé par les deux propriétaires.

---


## Ce que vous savez faire

Un cours ne se juge pas à ce qu'il a exposé, mais à ce que son lecteur est capable de faire ensuite. Voici la liste, formulée en actes plutôt qu'en connaissances. Elle sert aussi de grille d'auto-évaluation avant une prise de poste ou un entretien.


### Vous savez établir un périmètre et le défendre

☐ Croiser quatre sources d'inventaire dont une non technique, et **interpréter les écarts** plutôt que choisir un chiffre
☐ Identifier les actifs orphelins et conduire une campagne de désignation de propriétaires
☐ Établir la carte des actifs réellement exposés, et fermer ce qui ne sert plus
☐ Nommer les actifs de niveau 0 de votre organisation — la liste tient sur une page
☐ Déclarer un périmètre non couvert **plutôt que de le laisser invisible**


### Vous savez décider

☐ Qualifier une information en fait vérifié, hypothèse probable ou piste exploratoire
☐ Écarter un faux positif de rétroportage avant de lancer une campagne de 42 serveurs
☐ Appliquer un arbre de décision, et **expliquer votre chemin** devant un comité qui conteste
☐ Défendre une dépriorisation, et savoir ce qui la distingue d'un oubli
☐ Reconnaître qu'un délai accordé par la politique est une ressource, et l'utiliser sans culpabilité


### Vous savez corriger sans casser

☐ Qualifier un correctif en six questions, en lisant les notes de version **en entier**
☐ Composer un anneau pilote qui teste l'usage réel, pas seulement l'installation
☐ Écrire des critères d'arrêt chiffrés **avant** l'intervention, avec un décideur nommé
☐ Identifier un point de non-retour et le déclarer dans la demande de changement
☐ Chronométrer un retour arrière sur une topologie représentative
☐ Qualifier une traîne longue au lieu de clore une campagne à 97 %


### Vous savez traiter ce qui ne se corrige pas

☐ Qualifier une impossibilité parmi ses cinq types, et identifier le bon interlocuteur
☐ Parcourir la hiérarchie des compensations de haut en bas, en écrivant pourquoi vous descendez
☐ Rédiger une dérogation avec ses sept champs, et la faire signer au bon niveau
☐ Vérifier, six mois plus tard, qu'une compensation est **encore active**


### Vous savez réagir

☐ Poser les trois questions qui déterminent si vous pouvez conclure quoi que ce soit
☐ Réduire une exposition en quinze minutes, avant même de parler de correctif
☐ Dire à une direction générale que vous ne pouvez pas établir l'absence de compromission
☐ Comprimer un processus en urgence sans supprimer les garde-fous qui permettent de se tromper
☐ Décider de reconstruire plutôt que corriger, sur un critère explicite


### Vous savez prouver et financer

☐ Publier un taux avec sa population éligible, son dénominateur et sa part non mesurée
☐ Distinguer une mesure d'un ratio conservateur, et nommer chacun correctement
☐ Constituer un dossier de preuves en continu, en onze pièces
☐ Répondre à six questions d'auditeur sans prétendre être conforme
☐ Construire un dossier d'investissement à trois options, dont le statu quo chiffré


### Vous savez ce que vous ne savez pas

C'est la compétence la plus difficile, et celle que ce cours travaille le plus.

☐ Reconnaître qu'un rapport à 100 % de conformité doit déclencher un examen, pas une satisfaction
☐ Identifier ce que votre journalisation ne vous permettra jamais d'établir
☐ Écrire « non mesuré » dans un tableau de bord plutôt que de laisser une case vide
☐ Nommer un risque non maîtrisé **avant** qu'il ne se réalise, dans une note à la direction

---

**Ce que ce cours ne vous a pas appris**, et qu'il faut aller chercher ailleurs : administrer un système, concevoir un réseau, développer une application, conduire une investigation numérique, plaider un dossier juridique. Le MCS s'appuie sur ces métiers ; il ne les remplace pas, et ce document ne prétend pas les enseigner (§2.10).

**Ce qui vous manquera encore après ce cours**, et que seule la pratique donne : le sens du moment où une négociation peut aboutir, la capacité à sentir qu'un chiffre est faux avant de savoir pourquoi, et la patience nécessaire pour obtenir en dix-huit mois ce qui paraissait évident dès le premier jour. Le fil rouge HELIOMED existe pour rendre cette durée sensible : trois ans, une centaine de décisions, et quatre écarts au dernier audit.

---
