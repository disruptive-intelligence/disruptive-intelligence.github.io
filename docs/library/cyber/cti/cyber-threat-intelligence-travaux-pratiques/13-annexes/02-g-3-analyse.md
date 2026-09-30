---
title: G.3 Analyse
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - ANNEXES
  - index.md
---

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 19 | L'hypothèse unique | Le cerveau en produit une et la confirme | Trois hypothèses écrites ? |
| 20 | Chercher ce qui confirme | Au lieu de ce qui discrimine | Éléments compatibles avec toutes ? |
| 21 | L'accumulation d'indices faibles | Dix faibles ne font pas un fort | Combien ne vont **que** dans mon sens ? |
| 22 | La plausibilité prise pour la probabilité | Le récit cohérent convainc | Quelle observation la rendrait fausse ? |
| 23 | L'explication irréfutable | Aucune observation ne pourrait l'infirmer | C'est un défaut, pas une qualité |
| 24 | **Le regroupement par secteur** | Critère faible pris pour fort | Une victime hors secteur ? |
| 25 | Confirmation | « Plusieurs éléments confirment » | Grille §C.4 |
| 26 | Ancrage | La conclusion du premier jour survit | Ordre inversé, tiendrait-elle ? |
| 27 | Disponibilité | Explication sophistiquée par défaut | Fréquence de base ? |
| 28 | Saillance | Le romanesque prime sur le décisif | Quel élément discrimine ? |
| 29 | Récence | La dernière information l'emporte | Était-elle discriminante ? |
| 30 | Récit dominant | L'explication en vogue partout | Que dirait l'explication banale ? |
| 31 | **Biais du client** | Produire ce qui est attendu | Écrire avant de connaître l'usage |
| 32 | La piste non creusée | Ne laisse aucune trace | Relecture externe |
| 33 | Le consensus prématuré | Convergence en dix minutes | Écrire avant de discuter |
| 34 | Le pivot en chaîne | L'incertitude se multiplie | Premier niveau seulement |
| 35 | Le graphe qui ne sert à rien | Gratifiant et improductif | Quelle question tranche-t-il ? |


### G.4 Jugement et diffusion

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 36 | Refuser de conclure | Prudence apparente, transfert réel | Le destinataire doit analyser |
| 37 | Juger sans le dire | Appréciation présentée comme fait | Séparation des sections |
| 38 | « Possible » | Signifie « non exclu », donc rien | Test du remplacement |
| 39 | La fausse précision | « 73 % » sans calcul | Le chiffre suggère une méthode absente |
| 40 | Fusionner les trois axes | « Menace critique » | Probabilité + confiance + gravité séparés |
| 41 | La clause de réfutation absente | Huit fois sur dix | Section obligatoire |
| 42 | La conclusion en dernier | Réflexe scolaire | Première phrase |
| 43 | Le mélange des niveaux | Un produit, cinq destinataires | Un produit par niveau |
| 44 | **L'alerte de couverture** | Alerter « au cas où » | Les quatre conditions tracées |
| 45 | L'archivage sans motif | Indiscernable d'un oubli | Motif obligatoire |

---


## Annexe H — Sources et calendrier

> ⏱ **Annexe versionnée — vérifiée le 2 août 2026.**


### H.1 Les quatre sources qui suffisent

| Source | Cadence | Ce qu'elle couvre | Coût |
|---|---|---|---|
| **Catalogue d'exploitation avérée** | 5 min/jour | Le signal le plus fort | Gratuit |
| **Avis des éditeurs de vos produits critiques** | 10 min/jour | La source de vérité sur votre applicabilité | Gratuit |
| **Bulletins du centre de réponse national** | 15 min/semaine | Contexte, alertes | Gratuit |
| **Dispositif de partage sectoriel** | 20 min/semaine | Ce qui vise vos pairs, en avance | Adhésion |


### H.2 Sources complémentaires, par besoin

| Besoin | Source | Effort |
|---|---|---|
| Analyse technique approfondie | Publications de chercheurs et d'éditeurs | Moyen |
| Mentions de vos produits | Surveillance dédiée, ou signalements clients | Faible à moyen |
| Présence dans des fuites | Service de surveillance | Faible une fois en place |
| Ce qui est testé contre vous | **Vos journaux de filtrage** | 30 min/mois, gratuit |
| Vos angles morts | **Vos incidents** | 1 jour par fiche, gratuit |


### H.3 Rythmes de péremption

| Objet | Validité typique |
|---|---|
| Empreinte de fichier | Une variante |
| Adresse | Jours à semaines |
| Nom de domaine | Semaines |
| Artefact d'hôte | Mois |
| Outil employé | Mois à années |
| **Comportement** | **Années** |
| Évaluation de motivation | Années |
| Cartographie de couverture | **À revoir à chaque version majeure du référentiel** |


### H.4 Échéances de veille structurelle

| Objet | Cadence de vérification |
|---|---|
| Versions majeures des référentiels de techniques | Semestrielle |
| Cadre juridique du partage | **Semestrielle, ou à échéance annoncée** |
| Obligations de signalement produit | Annuelle |
| Périmètre et statut de votre dispositif sectoriel | Annuelle |
| Contrat et performance de vos fournisseurs | Annuelle, avec les cinq tests |


### H.5 Formation et compétences

*Aucune certification ne couvre le contenu de ce cours.* Les compétences les plus utiles, par ordre :

| Compétence | Comment la développer |
|---|---|
| **Écrire clairement** | Pratique, relecture par des non-spécialistes |
| **Analyse structurée** | Littérature du renseignement, appliquée à des cas réels |
| Compréhension des systèmes et réseaux | Formation technique généraliste |
| Réponse à incident | Exercices, participation aux cellules |
| Compréhension juridique | Relation régulière avec le juridique et le délégué |

⚠️ Une certification atteste d'une connaissance, pas d'une pratique. Les compétences déterminantes de ce cours — tolérer l'incertitude, résister à la pression de conclure, savoir quand s'arrêter — ne s'enseignent pas en formation.

---


## Annexe I — Modèle de données


### I.1 Entité SIGNALEMENT

| Champ | Type | Card. | Valeurs | Obligatoire |
|---|---|---|---|---|
| `id` | str | 1 | Identifiant stable | Oui |
| `date_reception` | date | 1 | | Oui |
| `source` | ref | 1 | → SOURCE | Oui |
| `type` | enum | 1 | avis · bulletin · publication · signalement_client · incident_interne · journal_interne · question | Oui |
| **`besoin_rattache`** | ref | 0..1 | → BESOIN. **Vide = archivage** | Non |
| `statut` | enum | 1 | nouveau · qualifié · en_traitement · en_attente · diffusé · archivé | Oui |
| **`motif_archivage`** | str | 0..1 | **Obligatoire si statut = archivé** | Conditionnel |
| `decision` | enum | 0..1 | agir · préparer · surveiller · ignorer · différer | Si qualifié |
| `condition_reexamen` | str | 0..1 | | Si ignorer |
| `porteur` | ref | 0..1 | | Si agir ou préparer |
| `date_reexamen` | date | 0..1 | | Si surveiller ou ignorer |


### I.2 Entité BESOIN

`id` · `question` **(O)** · `demandeur` **(O)** · `decision_eclairee` **(O)** · `echeance` · `niveau` (strat/opé/tact) · `statut` (actif/satisfait/reporté/abandonné) · `date_creation` · `date_derniere_production` · `nb_decisions_produites`

⚠️ Le champ `date_derniere_production` permet la révision par obsolescence du §14.5 : un besoin sans production depuis six mois doit être réexaminé.


### I.3 Entité SOURCE

`id` · `nom` · `type` · `fiabilite` (élevée/moyenne/faible) · **`justification_fiabilite`** · `interet_identifie` · `primaire_ou_reprise` · `independance_de` (0..n → SOURCE) · `methodologie_declaree` (bool) · `perimetre_declare` (bool) · `cout_annuel` · `date_derniere_evaluation`

**Le champ `independance_de` est celui qui prévient la circularité** : il matérialise que deux sources ne sont pas indépendantes.


### I.4 Entité PRODUIT

`id` · `type` (note_orientation / fiche_operationnelle / jeu_indicateurs / alerte / reponse_question) · `besoin` (ref) · `destinataires` (0..n) · `date_diffusion` · `probabilite` · **`confiance`** · **`justification_confiance`** · `clause_refutation` · `date_reexamen` · `relecteur` · **`retour_demande`** (bool) · `retour_recu` · `decision_produite`


### I.5 Entité DÉCISION *(registre du §35.5)*

`id` · `produit` (ref) · `date` · `decideur` · `nature` · **`ce_qui_aurait_ete_fait_sans`** · `cout_evite_estime`

**Le champ en gras est celui qui rend le registre démontrable.** Sans lui, on ne mesure qu'une corrélation.


### I.6 Règles de qualité

| # | Règle | Fréquence |
|---|---|---|
| 1 | Aucun signalement archivé sans motif | Hebdomadaire |
| 2 | Aucun produit sans niveau de confiance justifié | À la diffusion |
| 3 | Aucun besoin sans production depuis 6 mois non réexaminé | Semestrielle |
| 4 | Aucune décision « surveiller » sans indicateur ni porteur | Mensuelle |
| 5 | Aucune source évaluée depuis plus de 12 mois | Annuelle |
| 6 | Aucun produit sans retour demandé | Hebdomadaire |

---


## Annexe J — Workflow de traitement


### J.1 Les cinq états

```
NOUVEAU ──qualification──► QUALIFIÉ ──rattaché à un besoin ?──┐
                                                    │          │
                                          NON ──► ARCHIVÉ     OUI
                                                 (motif)       │
                                                               ▼
                                                        EN TRAITEMENT
                                                          │        │
                                          info manquante  │        │
                                                          ▼        ▼
                                                   EN ATTENTE   RELECTURE
                                                          │        │
                                                          └────────┤
                                                                   ▼
                                                              DIFFUSÉ
                                                                   │
                                                          retour à J+14
```



### J.2 Champs obligatoires par état

| État | Exigences |
|---|---|
| Qualifié | Source · date · type · **besoin rattaché ou motif d'archivage** |
| En traitement | Analyste · date de début |
| En attente | **Ce qui manque** · à qui la demande a été faite · date de relance |
| Relecture | Relecteur nommé · grille en six points passée |
| Diffusé | Destinataires · **probabilité et confiance justifiée** · clause de réfutation · **retour demandé** |
| Archivé | **Motif** · condition de réexamen le cas échéant |


### J.3 Délais indicatifs

| Transition | Délai cible |
|---|---|
| Nouveau → qualifié | 24 h |
| Qualifié → en traitement | Selon la décision |
| En attente → relance | 5 jours |
| Diffusé → retour demandé | 14 jours |
| Revue hebdomadaire des archivés des 3 dernières semaines | **15 min/semaine** |

⚠️ **La dernière ligne est celle du §19.6** : c'est la revue des archivés qui a produit le rapprochement des trois signalements. Un archivage n'est pas une suppression.


### J.4 Chaîne d'un signalement produit

```
Signalement (client, chercheur, veille)
        ▼
Qualification : applicabilité version par version
        ▼
Évaluation : exploitation active ? périmètre client ?
        ▼
┌── Obligation de signalement déclenchée ? ──┐
│                                            │
OUI                                         NON
│                                            │
▼                                            ▼
Alerte précoce (délai réglementaire)    Correctif planifié
Notification                             Notification client
▼                                            │
Rapport final                                │
        └────────────┬───────────────────────┘
                     ▼
        Correctif publié · clients notifiés · dossier clos
```


---


## Annexe K — Indicateurs et maturité


### K.1 Les six indicateurs

| # | Indicateur | Famille | Comment le produire | Piège |
|---|---|---|---|---|
| 1 | Besoins actifs et statut | Production | Registre | Ne mesure pas l'utilité |
| 2 | Produits diffusés par niveau | Production | Registre | Peut augmenter en dégradant |
| 3 | **Taux de lecture et de réponse** | Usage | Trois questions à J+14 | Taux de réponse ≈ 60 %, c'est normal |
| 4 | **Décisions modifiées** | Impact | Registre des décisions | Exige le champ « sans nous » |
| 5 | **Menaces neutralisées documentées** | Impact | Motifs d'archivage | Ne prouve pas que le CTI protège |
| 6 | **Alignement confiance / justesse** | Retour | Retour d'expérience semestriel | Exige d'avoir calibré |


### K.2 Les faux indicateurs

| Indicateur | Pourquoi |
|---|---|
| Nombre de rapports | Activité, pas utilité |
| Volume d'indicateurs ingérés | Ce que le fournisseur collecte |
| Nombre de sources | Une accumulation |
| **Nombre d'alertes** | **Devrait diminuer** avec la maturité |
| Temps de veille | Une consommation |
| Menaces identifiées | Dépend de l'actualité |


### K.3 Le tableau du retour d'expérience analytique

| | Estimation juste | Estimation fausse |
|---|---|---|
| **Confiance élevée** | ✅ Excellent | ❌ **Le pire cas** |
| **Confiance faible** | ⚠️ Confiance sous-évaluée | ✅ **Bon travail** |

**On ne juge pas un analyste sur son taux d'exactitude, mais sur l'alignement entre sa confiance annoncée et sa justesse réelle.**


### K.4 Modèle de maturité, par domaine

| Niveau | Caractéristique | Preuve exigée |
|---|---|---|
| **0** | Aucune activité | — |
| **1** | Veille informelle | Quelqu'un lit des bulletins |
| **2** | Besoins formulés | Registre des besoins, avec demandeurs nommés |
| **3** | Production calibrée | Échelle publiée · confiance justifiée · clause de réfutation |
| **4** | Boucle fermée | Retours demandés · registre des décisions · relecture croisée |
| **5** | Fonction apprenante | Retour d'expérience analytique · alignement mesuré · besoins révisés |

**Grille d'auto-évaluation par domaine** :

| Domaine | Niveau | Preuve citée |
|---|---|---|
| Formulation des besoins | ☐ 0-5 | |
| Collecte et plan | ☐ | |
| Évaluation de source | ☐ | |
| Analyse et hypothèses | ☐ | |
| Calibrage | ☐ | |
| Production et diffusion | ☐ | |
| Exploitation et décision | ☐ | |
| Partage | ☐ | |
| Mesure et retour | ☐ | |
| Cadre juridique | ☐ | |

⚠️ Un domaine critique faible **plafonne** ce qui en dépend. Sans calibrage, la production ne peut pas dépasser le niveau 2 quelle que soit sa qualité par ailleurs.


### K.5 Chiffrage d'une fonction

| Poste | Souvent omis ? |
|---|---|
| Personnel | Non |
| Sources payantes et adhésions | Non |
| Outillage | Non |
| **Intégration et maintenance** | **Oui** |
| **Temps des destinataires** | **Presque toujours** |

**Calcul du dernier** : `nb produits × nb destinataires × temps de lecture`. Une fonction diffusant 4 produits/mois à 7 destinataires, 20 min chacun, consomme ≈ **45 h/an** de temps de cadres.

---


## Annexe L — Checklists


### L.1 Avant de diffuser un produit
☐ La conclusion est-elle en première phrase ? · ☐ Contient-elle probabilité **et** confiance justifiée ? · ☐ Les faits sont-ils séparés des estimations ? · ☐ Y a-t-il une clause de réfutation ? · ☐ Le destinataire sait-il ce qu'on attend de lui ? · ☐ Le produit est-il adapté à **ce** destinataire ? · ☐ Une date de réexamen figure-t-elle ? · ☐ Un retour est-il demandé ? · ☐ La relecture croisée a-t-elle eu lieu ?


### L.2 Avant d'alerter
☐ Applicabilité **établie** ? · ☐ Urgence réelle — attendre aggrave-t-il ? · ☐ **Action possible maintenant** ? · ☐ Inaction déraisonnable ? · ☐ Cinq à dix lignes ? · ☐ Décideur nommé ? · ☐ Prochain point annoncé ? · ☐ Les quatre conditions sont-elles tracées dans le message ?


### L.3 Avant de croire une source
☐ Primaire ou reprise ? · ☐ Sur quoi la source d'origine fonde-t-elle son affirmation ? · ☐ Les sources sont-elles **indépendantes** ? · ☐ Le mode a-t-il été conservé ? · ☐ Quels éléments propres apporte-t-elle ? · ☐ Quel est son intérêt ? · ☐ Le périmètre d'observation est-il déclaré ?


### L.4 Avant de conclure
☐ Trois hypothèses écrites, dont une bénigne et une ennuyeuse ? · ☐ Quel élément **discrimine** ? · ☐ Quelle observation rendrait ma conclusion fausse ? · ☐ Quels présupposés n'ai-je pas vérifiés ? · ☐ Ai-je passé la grille des sept biais ?


### L.5 Avant de bloquer un indicateur
☐ Fraîcheur — dernière observation ? · ☐ **Colocation** — combien d'autres services à cette adresse ? · ☐ Nos actifs communiquent-ils déjà avec ? · ☐ **Date de retrait fixée** ?


### L.6 Avant de partager à l'extérieur
☐ Que révèle chaque élément **de nous** ? · ☐ L'anonymisation résiste-t-elle au recoupement ? · ☐ Le marquage est-il posé ? · ☐ La décision est-elle prise **élément par élément** ? · ☐ Le niveau de confiance accompagne-t-il ?


### L.7 Avant de souscrire
☐ Le besoin est-il formulé ? · ☐ Les cinq tests ont-ils été conduits ? · ☐ Quel est le recouvrement avec le gratuit ? · ☐ Quelle avance sur la publication publique ? · ☐ L'export brut est-il garanti ? · ☐ Le volume justifie-t-il un outil ?


### L.8 Audit d'empreinte informationnelle *(annuel)*
☐ Offres d'emploi actives · ☐ Certificats publics et noms d'hôtes exposés · ☐ Métadonnées des documents publiés · ☐ Interventions publiques · ☐ Fuites contenant le domaine · ☐ Mentions de clients dans la communication


### L.9 Les douze premiers mois
☐ 3 à 6 besoins avec demandeur et décision · ☐ Inventaire permettant de vérifier l'applicabilité · ☐ File à cinq états avec archivage motivé · ☐ Échelle de calibrage publiée · ☐ Premier produit avec **retour demandé** · ☐ Registre des décisions tenu **dès le premier jour** · ☐ Cadre juridique instruit · ☐ Relecture croisée · ☐ Interfaces détection et vulnérabilités · ☐ Renseignement interne exploité · ☐ Tableau de bord six indicateurs · ☐ Premier retour d'expérience analytique

---
