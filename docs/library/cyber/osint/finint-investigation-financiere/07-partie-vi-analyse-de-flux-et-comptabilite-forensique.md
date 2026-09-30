---
title: PARTIE VI — ANALYSE DE FLUX ET COMPTABILITÉ FORENSIQUE
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 7
chapters: 11
---

*Six chapitres pour passer de la lecture brute des relevés et bilans à une analyse structurée — détecter les anomalies, reconstituer les schémas, qualifier la cohérence économique, reconstituer le patrimoine.*

-----

## Chapitre 34 — Lire un relevé bancaire

### Objectif du chapitre

Maîtriser la **lecture analytique d’un relevé bancaire** — au-delà de la simple consultation. Le chapitre 9 a posé la structure du relevé ; ici, on développe les techniques d’analyse en profondeur.

### Le concept

Un relevé bancaire est une **série temporelle d’opérations**. Le lire analytiquement revient à le traiter comme un **dataset** : structurer les données, calculer des indicateurs, repérer des patterns, comparer à des références (sectorielles, historiques, comportementales).

### Les passes d’analyse (approfondissement chapitre 9)

**Passe 1 — Profilage statistique global.**

Indicateurs clés à calculer :

- Nombre total d’opérations sur la période.
- Volume crédité, volume débité, ratio.
- Solde moyen, médian, maximum, minimum.
- Nombre de contreparties uniques.
- Top 5, 10, 20 des contreparties (entrants et sortants).
- Distribution des montants : nombre d’opérations par tranche (< 1 K€, 1-10 K€, 10-50 K€, 50-100 K€, > 100 K€).
- Saisonnalité : opérations par jour de la semaine, par heure, par mois.

Outils : tableur Excel ou LibreOffice, ou pandas (Python) pour les gros volumes.

**Passe 2 — Concentration et asymétrie.**

- Concentration : si les top 5 contreparties représentent > 70 % du volume, le compte est *concentré* — atypique pour la plupart des comptes personnels.
- Asymétrie crédit/débit : un compte qui reçoit beaucoup mais peu sortant accumule la valeur ; un compte qui passe (entrant = sortant en cycle court) est un compte de **transit**.
- Cycles : entrée 100 K€, sortie 95-99 K€ dans les 48h — pattern de transit.

**Passe 3 — Vue temporelle.**

- Activité par mois : pics, creux.
- Détection de **ruptures de comportement** : avant/après un événement (changement d’activité, début ou fin d’une fraude).
- Saisonnalité cohérente avec le secteur ? (un commerce saisonnier a un profil annuel marqué).

**Passe 4 — Contreparties.**

- Identification des principales contreparties : sociétés (croisement registres), particuliers, comptes propres.
- Nouvelles contreparties (n’apparaissant pas dans l’historique antérieur).
- Contreparties géographiquement incohérentes.
- Contreparties dans des juridictions à risque (chapitre 10).

**Passe 5 — Libellés et références.**

- Mots clés vagues : « services », « avance », « régularisation », « paiement », « contractuel ».
- Libellés répétés à l’identique sur plusieurs flux.
- Libellés faisant référence à des factures (chercher les factures correspondantes).
- Absence de libellé ou libellé pauvre.

**Passe 6 — Cohérence économique.**

- Flux compatible avec l’activité ?
- Ratios sectoriels respectés ?
- Transferts au dirigeant (compte personnel) en proportion raisonnable ?

### Méthode — workflow type

Sur un relevé d’1 an, environ 3000-5000 lignes pour une PME active :

1. **Import** dans tableur ou pandas.
1. **Nettoyage** : harmonisation des libellés, parsing des montants.
1. **Catégorisation** : assigner chaque opération à une catégorie (CA encaissé, achats fournisseurs, salaires, charges fiscales, virements intra-groupe, dividendes, frais bancaires, prélèvements perso).
1. **Tableau de synthèse** : volume par catégorie, ratio, évolution.
1. **Tableau des contreparties** : top 20 en entrée, top 20 en sortie.
1. **Détection d’anomalies** : opérations sortant des patterns habituels.
1. **Annotation** : signaux faibles documentés.

### Mini-walkthrough — relevé NEXUS TRADING SAS

Année 1 (1er exercice clos), compte principal :

- 1 421 crédits = 4,2 M€.
- 1 826 débits = 4,1 M€.
- Solde moyen 87 K€, max 542 K€.
- Top 5 entrées : 73 % du volume (4 sociétés étrangères + 1 compte personnel inconnu).
- Top 5 sorties : 51 % du volume (3 sociétés du réseau + 2 comptes personnels).

Vue temporelle : 3 pics d’activité en mars, juin, octobre — chaque pic précède de quelques jours un transfert vers la Suisse. Pattern de **cycles**.

Libellés : 75 % vagues, 22 % faisant référence à des factures non identifiables, 3 % explicites mais douteux.

Cohérence : la SAS déclare une activité de négoce de matériel agricole. Aucun fournisseur de matériel agricole identifié parmi les contreparties (entrants ou sortants). Aucun client final identifié. La SAS apparaît comme un compte de **pure intermédiation**, avec activité économique réelle non démontrée.

Hypothèses : transit financier (probable), TBML (possible à probable), pure structure d’opacification (probable).

### Erreurs fréquentes

- **Lire ligne à ligne sans agrégation préalable.** L’analyste se perd.
- **Ignorer les frais bancaires** : ils racontent une histoire (volume d’opérations, opérations rejetées, descouverts).
- **Sous-estimer la temporalité** : un même montant à un mois différent peut être un signal différent.

### Limites

Le relevé seul ne suffit jamais. Il faut croiser avec : comptes annuels, libellés détaillés (parfois enrichis par réquisition), correspondance entre flux et factures (chapitre 38), réquisitions des contreparties.

### Lien avec le fil rouge

> **CLEARFLOW — Analyse système des relevés**
> 
> Nassim consolide les analyses des relevés des 4 SAS françaises. Cumulés, ces relevés couvrent ~5 600 opérations sur 18 mois, ~22 M€ de volume crédit, 16 M€ vers l’étranger. La signature globale : système de **transit multi-comptes avec cycles** intra-groupe, sortie principale vers Suisse et destinations offshore. Activité commerciale réelle douteuse. Sous réserve de coopération internationale pour les contreparties étrangères.

### Points clés à retenir

- Relevé bancaire = série temporelle à traiter comme dataset.
- 6 passes d’analyse : profil, concentration, temps, contreparties, libellés, cohérence.
- Catégoriser, agréger, comparer.
- Tout pattern doit être confronté à l’activité économique réelle.

-----

## Chapitre 35 — Reconstituer des flux financiers

### Objectif du chapitre

Passer de la lecture d’un compte isolé à la **reconstitution d’un schéma multi-comptes** — suivre l’argent à travers plusieurs banques, plusieurs juridictions, plusieurs entités, pour comprendre l’organisation d’ensemble.

### Le concept

La reconstitution de flux consiste à **enchaîner les opérations** pour montrer le parcours de la valeur. Elle peut se faire dans deux directions :

- **Forward tracing** : partant d’une opération initiale, suivre où va l’argent.
- **Backward tracing** : partant d’une opération finale, remonter à l’origine.

Idéalement, les deux sont combinées pour valider mutuellement les chaînes.

### L’utilité opérationnelle

Reconstituer les flux permet :

- Identifier l’**origine probable** des fonds (infraction prédécesseur en blanchiment).
- Identifier la **destination finale** (UBO bénéficiaire, intégration dans l’économie légale).
- Identifier les **points de passage critiques** (banques, juridictions, sociétés).
- Identifier les **techniques de layering** (fractionnement, complexification, conversion).
- Quantifier le volume total et le ventiler.

### Méthode — workflow

1. **Identifier les comptes accessibles** : DS, réquisitions, EAR/CRS pour les comptes étrangers (en CRF).
1. **Construire un tableau de flux** : pour chaque opération, donneur, bénéficiaire, montant, devise, date, libellé, rail.
1. **Identifier les liens entre opérations** : opération A débite le compte 1 vers le compte 2, opération B (1-3 jours après) débite le compte 2 vers le compte 3, etc.
1. **Constituer des séquences** : chaîne d’opérations chronologiquement et économiquement liées.
1. **Construire le graphe de flux** : nœuds = comptes (ou entités), arcs = flux pondérés par montant.
1. **Calculer les agrégats** : total entré, total sorti, perte en route (différence = frais ou paiements masqués).

### Walkthrough — séquence de transit

```
Schéma observé (sur 14 mois)

Société Y (Émirats) ──[3,8 M€ via 18 SWIFT MT103]──> SAS A (France)
SAS A (France) ──[3,2 M€ via 24 SCT vers]──> Sociétés liées du groupe
SAS A (France) ──[420 K€ via SCT Inst]──> Comptes personnels (M. X et liés)
SAS A (France) ──[300 K€ via 5 SWIFT MT103]──> Banque privée Suisse (compte K. Haddad présumé)

Détail temporel : entrées concentrées en début de mois, sorties dans les 7 jours.
```

Lecture FININT : le profil est compatible avec un **schéma de transit avec rétention de marge minimale** et **dilution dans le réseau** + **prélèvements personnels**. Le solde net de la SAS reste faible (~100 K€), cohérent avec un compte de passage.

Hypothèses : TBML (probable), corruption avec rétrocommissions (possible), simple optimisation fiscale agressive (peu probable seul à expliquer le schéma).

### Erreurs fréquentes

- **Ne suivre qu’un sens.** Toujours combiner forward et backward.
- **Ignorer les frais bancaires** : ils peuvent expliquer une partie de la perte en route.
- **Confondre transit et accumulation** : un compte peut être les deux selon les périodes.
- **Sur-attribuer une intention.** Un schéma de transit peut être légitime (intermédiation commerciale réelle).

### Limites

La reconstitution exige l’accès aux relevés détaillés de **chaque compte** dans la chaîne. Sans coopération internationale, des maillons restent inaccessibles, donc des hypothèses non confirmées.

### Lien avec le fil rouge

> **CLEARFLOW — Reconstitution globale**
> 
> Nassim, après 5 semaines, produit une cartographie des flux du dossier Haddad : sur 18 mois, ~22 M€ entrants dans le réseau (origine multi-juridictionnelle), ~16 M€ sortants vers l’étranger, ~6 M€ stationnés ou consommés (dépenses, immobilier, autres). Sur les 22 M€ entrants, l’origine reste partiellement floue : ~12 M€ proviennent de sociétés du même groupe (transit interne sans origine externe identifiée pour cette portion), ~10 M€ proviennent de tiers commerciaux dont la réalité économique reste à confirmer (TBML probable). C’est cette analyse qui structure la note finale.

### Points clés à retenir

- Forward + backward tracing combinés.
- Tableau de flux structuré, graphe de flux pondéré.
- Quantifier les totaux et les pertes en route.
- Identifier les techniques de layering.

-----

## Chapitre 36 — Lire un bilan et un compte de résultat

### Objectif du chapitre

Maîtriser la **lecture analytique** des documents comptables clés — bilan, compte de résultat, annexe — pour détecter cohérence et incohérence dans le profil économique d’une entreprise.

### Le concept

Le **bilan** est une photo à une date : actifs (ce que l’entreprise possède) = passifs (ce qu’elle doit, y compris ses fonds propres).

Le **compte de résultat** est un flux sur une période : produits (revenus) − charges (coûts) = résultat.

L’**annexe** explicite, contextualise, détaille.

### Lecture du bilan

**Actif** :

- **Immobilisations** : incorporelles (fonds de commerce, brevets), corporelles (terrains, bâtiments, matériel), financières (participations, prêts).
- **Actif circulant** : stocks, créances clients, autres créances, trésorerie.

**Passif** :

- **Capitaux propres** : capital social, réserves, report à nouveau, résultat de l’exercice.
- **Provisions pour risques et charges**.
- **Dettes** : emprunts bancaires, dettes fournisseurs, dettes fiscales et sociales, dettes diverses.

Indicateurs clés :

- **Ratio d’endettement** = dettes / fonds propres. Un ratio très élevé peut signaler une fragilité ; très faible peut signaler une accumulation atypique.
- **Liquidité** = actif circulant / dettes à court terme.
- **Capacité d’autofinancement** : produit la capacité de l’entreprise à financer ses investissements et son remboursement de dette.

### Lecture du compte de résultat

**Produits** :

- Chiffre d’affaires (ventes de marchandises, prestations de services).
- Production stockée et immobilisée.
- Subventions d’exploitation.
- Produits financiers, produits exceptionnels.

**Charges** :

- Achats consommés (matières premières, marchandises).
- Services extérieurs (sous-traitance, locations, honoraires, transports, etc.).
- Impôts et taxes.
- Charges de personnel (salaires, charges sociales).
- Dotations aux amortissements et provisions.
- Charges financières (intérêts), charges exceptionnelles.

**Soldes intermédiaires de gestion** :

- **Marge commerciale** = ventes − coût d’achat (pour les négoces).
- **Valeur ajoutée** = production de l’exercice − consommations en provenance des tiers.
- **EBE / Excédent Brut d’Exploitation** = VA − charges de personnel − impôts et taxes.
- **Résultat d’exploitation** = EBE − dotations.
- **Résultat courant avant impôts** = résultat d’exploitation + résultat financier.
- **Résultat net**.

### L’utilité opérationnelle FININT

Les comptes annuels permettent à l’analyste :

- **Apprécier la cohérence sectorielle** : la marge, la productivité, l’intensité capitalistique sont-elles vraisemblables ?
- **Détecter les anomalies** : postes anormalement gonflés, charges récurrentes douteuses, créances clients fictives, stocks invraisemblables.
- **Évaluer la substance économique** : présence ou absence de moyens humains et matériels.
- **Comprendre la stratégie financière** : endettement, distribution de dividendes, conventions intragroupe.

### Méthode — lecture rapide

1. **Vue d’ensemble** : taille (CA, total bilan), forme juridique, exercice, secteur.
1. **Ratios sectoriels** : marge commerciale, marge d’exploitation, productivité (CA/effectif), intensité capitalistique (immo/CA).
1. **Évolution** : sur 3 ans si disponibles — croissance, rupture, stabilité.
1. **Postes anormaux** : > 10 % de l’actif ou du résultat sans explication évidente.
1. **Annexe** : engagements hors bilan, conventions réglementées, événements postérieurs.

### Mini-walkthrough — NEXUS TRADING SAS suite

Comptes 1er exercice :

- CA 12,4 M€, achats consommés 11,9 M€, marge commerciale 0,5 M€ (4 %).
- Charges de personnel 32 K€ (1 dirigeant, pas de salariés).
- Services extérieurs : 195 K€ (dont 140 K€ « conseil » à NEXUS HOLDINGS LTD CY).
- EBE : 273 K€.
- Résultat d’exploitation : 80 K€ (après dotations).
- Résultat financier : -8 K€ (frais bancaires SWIFT importants).
- Résultat net : 60 K€.

Bilan :

- Actif immobilisé : 12 K€ (équipement minimum).
- Actif circulant : 350 K€ (créances clients 280 K€, trésorerie 35 K€, autres 35 K€).
- Total actif : 362 K€.
- Capitaux propres : 70 K€ (capital 10 K€ + résultat).
- Dettes fournisseurs : 215 K€.
- Dettes fiscales et sociales : 25 K€.
- Comptes courants associés (NEXUS HOLDINGS CY) : 52 K€.

Lecture FININT : profil typique d’une **société d’intermédiation à très faible substance**. Charges de « conseil » à la holding chypriote représentent 70 % des services extérieurs — *probable* canal d’évasion de bénéfices vers la juridiction chypriote (à juridiction CRS, mais le levier de taxation peut être différent). Marge brute de 4 % cohérente avec intermédiation pure, ne tranche pas en soi. Le faible niveau d’immobilisations (12 K€) et l’absence de salariés signalent une coquille sans substance économique réelle propre.

### Erreurs fréquentes

- **Lire les chiffres absolus** sans comparaison sectorielle ou ratiométrique.
- **Ignorer l’annexe** : conventions réglementées intragroupe, engagements, événements postérieurs y figurent.
- **Surinterpréter un seul exercice** : la cohérence se voit sur la trajectoire (3 ans+).

### Limites

La comptabilité est **construite par l’entreprise** ; sans CAC, le contrôle externe est limité. Les comptes peuvent être falsifiés. Le forensique poussé exige un expert-comptable de formation forensique (chapitre 37).

### Lien avec le fil rouge

> **CLEARFLOW — Analyse des 2 SAS publiantes**
> 
> Sur les 2 SAS françaises publiant des comptes, Nassim repère : pattern récurrent de charges de conseil à des entités liées (15-25 % du résultat brut diverté vers Chypre par exercice), faible substance économique propre, profils de marge cohérents avec intermédiation mais non démontratifs d’une activité commerciale réelle. Cumulé avec l’analyse de flux, l’hypothèse de **structures de transit avec évasion de bénéfices** est *probable* à *quasi-certaine*.

### Points clés à retenir

- Bilan = photo ; compte de résultat = flux ; annexe = explication.
- Indicateurs : marge, EBE, résultat, ratios.
- Cohérence sectorielle et évolution sur 3 ans : essentiels.
- L’absence de substance économique (faible immo, pas de salariés) est un signal fort.

-----

## Chapitre 37 — Détecter anomalies comptables et signaux faibles

### Objectif du chapitre

Connaître les **anomalies comptables typiques** et les **signaux faibles** qui orientent vers une enquête approfondie : ventes fictives, charges fictives, prêts intragroupe sans contrepartie, ajustements de fin d’exercice douteux.

### Le concept

Une anomalie comptable est un poste, un mouvement ou une présentation qui s’écarte de ce qu’on attendrait pour une entreprise du secteur et de la taille concernée. Elle peut être :

- **Innocente** : choix méthodologique légitime, particularité sectorielle.
- **Suspecte** : indice d’un schéma à investiguer.
- **Frauduleuse** : preuve, après recoupement, d’une falsification.

L’analyste FININT cherche d’abord à identifier la suspicion, pas à conclure à la fraude.

### Familles d’anomalies courantes

**Côté revenus** :

- **Ventes fictives** : factures sans contrepartie réelle (marchandise, prestation). Détectables par : créances clients qui ne se règlent pas, croissance disproportionnée du CA, ventes à des clients sans existence vérifiable, marges anormalement élevées.
- **Cut-off** : décalage de la reconnaissance du revenu pour gonfler l’exercice (revenu reconnu en année N alors qu’il aurait dû l’être en N+1, ou inversement).
- **Vente fictive de stocks** entre entités liées pour gonfler les ventes.
- **Subventions non rapportées au bon exercice**.

**Côté charges** :

- **Charges fictives** : factures payées à des fournisseurs fictifs ou à des sociétés liées sans contrepartie réelle. Vecteur classique d’abus de biens sociaux (ABS — chapitre 43).
- **Charges de conseil** disproportionnées à des entités liées (signal d’évasion de bénéfices).
- **Voyages et frais de représentation** disproportionnés à l’activité.
- **Sous-traitance massive** sans personnel ni équipement chez le sous-traitant (chaîne fictive).

**Côté bilan** :

- **Créances clients gonflées** : créances qui restent en bilan sans recouvrement (cachent une absence de revenu réel).
- **Stocks invraisemblables** : volumes ou valeurs sans rapport avec l’activité.
- **Provisions douteuses** : sur-provisionnement ou sous-provisionnement pour modeler le résultat.
- **Prêts intragroupe** : si faits sans intérêts, sans documentation, sans remboursement, signal de transfert occulte de valeur.
- **Compte courant d’associé** anormalement gros (le dirigeant a prêté ou retiré beaucoup).

**Présentation et publication** :

- **Comptes publiés en retard récurrent**.
- **Confidentialité demandée alors que la société dépasse les seuils**.
- **Changement de cabinet de CAC** sans justification claire.
- **Réserves dans le rapport du CAC**.

### L’utilité opérationnelle

Détecter les anomalies oriente :

- La typologie probable du schéma (ABS, fraude fiscale, évasion, blanchiment).
- Les pièces à demander en réquisition (factures sous-jacentes, contrats, ordres de virement).
- Les acteurs à profiler (commissaire aux comptes, expert-comptable, dirigeants).

### Méthode — protocole de détection

1. **Comparer les ratios** sectoriels et historiques.
1. **Examiner les postes principaux** ligne par ligne pour les postes représentant > 5 % du total.
1. **Lire systématiquement l’annexe**.
1. **Identifier les conventions réglementées** (transactions avec parties liées).
1. **Confronter avec les flux observables** (relevés bancaires).
1. **Documenter les signaux** dans la fiche société (chapitre 28).

### Mini-walkthrough — anomalies NEXUS TRADING

- Charges de conseil à NEXUS HOLDINGS LTD CY = 140 K€ sur l’exercice. Disproportionné pour une SAS de 12,4 M€ de CA avec un seul dirigeant. Convention réglementée à l’origine ? Service réel rendu ? *Probable* signal de transfert de bénéfices vers la juridiction chypriote.
- Créances clients = 280 K€, soit ~30 jours de CA. Niveau normal pour le négoce. Pas d’anomalie ici.
- Compte courant associé NEXUS HOLDINGS CY = 52 K€. Faible niveau, pas alarmant.
- Stocks = 0 €. Cohérent avec intermédiation pure.

Signal principal : **les charges de conseil**. *Probable* mécanisme d’évasion de bénéfices vers la holding chypriote, à investiguer (substance des prestations, contrats sous-jacents).

### Erreurs fréquentes

- **Considérer une anomalie comme une preuve.** L’anomalie est un signal d’investigation, pas une preuve.
- **Ignorer la perspective sectorielle.** Certaines anomalies apparentes sont des pratiques sectorielles courantes.
- **Ne pas chercher l’explication légitime** avant de conclure à la fraude.

### Limites

Le détecteur d’anomalies suppose une connaissance sectorielle ; sans elle, l’analyste risque d’attribuer une anomalie là où il n’y en a pas, ou inversement.

### Lien avec le fil rouge

> **CLEARFLOW — Signaux comptables consolidés**
> 
> Sur l’ensemble du réseau Haddad, Nassim recense 8 anomalies comptables convergentes : charges de conseil intragroupe disproportionnées (3 SAS), prêts intragroupe sans intérêts (5 entités), créances clients structurellement non recouvrées (1 SAS), absence systématique de stocks pour entités déclarées en négoce (4 SAS). Cumulés, ces signaux constituent un faisceau convergent de *probable* schéma d’évasion de bénéfices et de transferts intragroupe non justifiés économiquement.

### Points clés à retenir

- Anomalies = signaux d’investigation, jamais preuves seules.
- Familles : ventes fictives, charges fictives, postes de bilan douteux, présentation.
- Comparaison sectorielle + cohérence avec flux = clés.
- Conventions réglementées et annexe sont des mines d’information.

-----

## Chapitre 38 — Factures, marges, marchandises et cohérence économique

### Objectif du chapitre

Maîtriser la **vérification de la cohérence économique** : confronter les flux financiers à la réalité opérationnelle attendue — marchandises, marges, factures, transport, logistique.

### Le concept

Une fraude moderne (notamment TBML — chapitre 41) repose sur la **dissociation entre flux financier et flux physique**. Une facture peut être payée sans contrepartie réelle de marchandise ; une marchandise peut être surfacturée ou sous-facturée ; un transport peut être déclaré sans avoir lieu.

L’analyse de cohérence économique cherche à confronter :

- **Le flux financier déclaré** (virement, facture).
- **La marchandise présumée** (nature, quantité, valeur de marché).
- **La logistique attendue** (transport, douane, certificats).
- **La marge réalisée** (cohérence avec les pratiques sectorielles).

### L’utilité opérationnelle

Pour de nombreux schémas, c’est l’analyse de cohérence économique qui **trahit la fraude**. Une facture intracommunautaire de 800 K€ pour une marchandise dont la valeur de marché est de 200 K€ est un signal fort.

### Méthode — vérifier la cohérence

1. **Identifier la marchandise** (nature, quantité, qualité) via la facture, le contrat, les documents douaniers.
1. **Estimer la valeur de marché** : sources sectorielles, comparables, expertise.
1. **Vérifier la cohérence du prix** : sur-facturation ? sous-facturation ?
1. **Vérifier la logistique** : la marchandise a-t-elle été transportée ? Quels documents (CMR, BL, EUR1, certificats d’origine) ?
1. **Vérifier les contreparties** : le fournisseur et le client ont-ils l’activité, la capacité, les références pour cette opération ?
1. **Confronter avec les flux bancaires** : le paiement correspond-il en montant, en date, en parties ?

### Sources de référence pour les valeurs de marché

- **Indices sectoriels** : matières premières (LME, ICE, CME), agricoles (Bourse de Chicago, Euronext Paris), énergie.
- **Statistiques douanières** : Eurostat Comext (UE), UN Comtrade, customs databases (CBP US).
- **Bases B2B** : Alibaba, plateformes sectorielles (prix indicatifs).
- **Expertise sectorielle** : cabinets spécialisés.

### Mini-walkthrough — TBML avec sur-facturation

Cas type : une SARL française importe du matériel agricole d’occasion (tracteurs) depuis un fournisseur émirati.

- Facture : 8 tracteurs Massey Ferguson 5710 SL d’occasion, 95 000 € chacun, soit 760 K€.
- Valeur de marché de référence (occasion, modèles 2018-2020) : environ 35-45 K€ pièce, soit 280-360 K€ pour 8 unités.
- Sur-facturation apparente : environ × 2.
- Documents : CMR sommaire, certificats d’origine douteux (mise en cause par presse régionale).

Lecture FININT : profil compatible avec une **sur-facturation TBML** où le surplus payé (~400 K€) est en réalité une **rétrocession** vers le payeur ou un destinataire désigné. C’est un schéma classique pour transférer de la valeur sous couvert de commerce.

### Erreurs fréquentes

- **Confondre prix sur facture et valeur réelle** : prendre la facture au pied de la lettre.
- **Ignorer les particularités sectorielles** : un matériel sur-spécifié peut être légitimement plus cher.
- **Conclure trop vite sans expertise** : la cohérence économique fine exige parfois un sectoriste.

### Limites

La vérification de cohérence économique exige une **expertise sectorielle** ou un accès à des bases de prix. Sans cela, l’analyste se borne à signaler une probable anomalie et propose une expertise.

### Lien avec le fil rouge

> **CLEARFLOW — Le marché ivoirien réexaminé**
> 
> Le marché public ivoirien de fourniture de matériel agricole remporté par NEXUS NEGOCE (Côte d’Ivoire) en 2023 pour 3,2 M€ peut être réexaminé : les types de tracteurs livrés (selon les documents publics ivoiriens) valent au marché européen environ 1,5 M€. Sur-facturation apparente : ×2. Compatible avec un schéma combinant favoritisme (marché remporté dans des conditions discutées) et sur-facturation (rétrocommissions probables). Le volet ivoirien est renvoyé en coopération internationale ; depuis la France, on documente la *probable* sur-facturation comme élément du faisceau.

### Points clés à retenir

- Dissociation flux financier / flux physique = vecteur classique de fraude.
- Vérifier marchandise, valeur de marché, logistique, contreparties.
- Sur-facturation et sous-facturation = signaux TBML.
- Expertise sectorielle souvent requise pour la qualification fine.

-----

## Chapitre 39 — Reconstitution patrimoniale et train de vie

### Objectif du chapitre

Reconstituer le **patrimoine d’une personne** : actifs visibles, actifs présumés, train de vie observable, et confronter cette reconstitution aux revenus déclarés. C’est l’une des analyses les plus délicates et les plus stratégiques du FININT.

### Le concept

Le patrimoine d’une personne se compose :

- **Actifs immobiliers** : biens en France (DVF, Patrim) et à l’étranger.
- **Actifs financiers** : participations dans sociétés, comptes bancaires, portefeuilles.
- **Actifs mobiliers de valeur** : véhicules, bateaux, aéronefs, œuvres, bijoux, montres, instruments de collection.
- **Cryptos** : adresses on-chain — renvoi à OSINT Crypto pour l’analyse détaillée.
- **Train de vie observable** : voyages, dépenses visibles, écoles privées, événements.

La **reconstitution patrimoniale** consiste à inventorier l’ensemble, l’évaluer, et le confronter aux revenus déclarés.

### L’utilité opérationnelle

La reconstitution patrimoniale sert à :

- **Détecter un train de vie incohérent** avec les revenus officiels.
- **Préparer l’asset recovery** : identifier les biens susceptibles de gel/saisie/confiscation.
- **Étayer les soupçons** d’enrichissement illicite (corruption, fraude fiscale, etc.).
- **Mesurer le préjudice** à la collectivité (en cas d’évasion fiscale, de corruption, etc.).

### Méthode — workflow de reconstitution

1. **Lister les actifs visibles** : sources ouvertes — DVF, Patrim, registres divers, presse, SOCMINT.
1. **Identifier les actifs présumés** : signaux visibles (voyages réguliers à Dubaï = possible résidence ; voiture de luxe sur Instagram = bien à identifier ; etc.).
1. **Estimer les valeurs** : recherche prix de marché, sources spécialisées.
1. **Lister les revenus déclarés** : presse (pour les dirigeants publics), déclarations HATVP, comptes annuels des sociétés détenues, distribution de dividendes traçable.
1. **Confronter** : patrimoine identifié versus revenus déclarés. Écart ? Plausibilité d’un héritage ? Activités antérieures ?
1. **Documenter les lacunes** : actifs étrangers non vérifiés, comptes bancaires inaccessibles, etc.

### Mini-walkthrough — patrimoine Haddad

Actifs visibles français :

- 3 biens immobiliers à Paris (SCI HADDAD INVESTISSEMENTS) : valeur estimée 11 M€.
- 2 véhicules de luxe (immatriculations parisiennes) : ~280 K€.
- Total France visible : ~11,3 M€.

Actifs présumés à l’étranger :

- Villa à Beyrouth (presse libanaise, photos) : valeur estimée 3-5 M€.
- Présence à Dubaï : appartement éventuel, non confirmé (~1-3 M€ si confirmé).
- Yacht (pavillon Malte, présence dans presse mondaine) : valeur estimée 4-7 M€.
- Participations dans le groupe Haddad : valorisation complexe (probablement 8-15 M€).
- Compte bancaire suisse présumé (DS) : montant non connu.
- Total présumé : 16 à 30 M€ (très large fourchette).

Train de vie observable :

- 4-6 voyages internationaux par an (Paris-Beyrouth-Dubaï-Genève).
- Événements professionnels et caritatifs fréquents.
- Réseau social haut de gamme.

Revenus déclarés (présomé sans accès aux déclarations fiscales) :

- Activité de dirigeant de Nexus Liban SAL et NEXUS INTERNATIONAL FZ.
- Plusieurs sources de revenus non publiques.

Estimation : le patrimoine total (France + étranger) est *probable* à **25-40 M€**. La cohérence avec les revenus déclarés sur 30 ans d’activité de négoce international est *possible* — un négoce international peut générer ces patrimoines légitimement. Cependant, la fraction *attribuée à des fonds d’origine illicite* serait à qualifier, *indéterminable* sans coopération internationale et accès aux déclarations.

Hypothèse : patrimoine global cohérent avec une activité réussie ; sa **construction multi-juridictionnelle opaque** est un signal de *probable* contournement fiscal et possiblement d’autres schémas, à confirmer.

### Erreurs fréquentes

- **Sous-estimer le patrimoine étranger.** Beaucoup de patrimoines de personnes d’affaires internationales sont majoritairement à l’étranger.
- **Surinterpréter le train de vie.** Un train de vie élevé peut être financé par des sources légitimes (héritage, succès commercial réel).
- **Confondre disponibilité de l’information et absence.** Un patrimoine non visible n’est pas un patrimoine nul.

### Limites

La reconstitution patrimoniale rigoureuse exige des sources fermées : déclarations fiscales, EAR/CRS pour les comptes étrangers, coopération internationale. En OSINT seul, on aboutit à des fourchettes larges et des hypothèses calibrées.

### Lien avec le fil rouge

> **CLEARFLOW — Patrimoine et asset recovery**
> 
> Sur la base de la reconstitution, Nassim identifie 11 M€ d’actifs français saisissables en théorie (sous procédure judiciaire) et présume 16-30 M€ étrangers à confirmer. La note finale recommande au PNF d’envisager des mesures conservatoires sur les actifs français, et de solliciter la coopération internationale pour qualifier et localiser les actifs étrangers.

### Points clés à retenir

- Reconstitution = actifs immobiliers + financiers + mobiliers + crypto + train de vie.
- Sources ouvertes (DVF, Patrim, registres) + SOCMINT + leaks.
- Confronter aux revenus déclarés et à la trajectoire professionnelle.
- Préparer l’asset recovery par juridiction.

-----
