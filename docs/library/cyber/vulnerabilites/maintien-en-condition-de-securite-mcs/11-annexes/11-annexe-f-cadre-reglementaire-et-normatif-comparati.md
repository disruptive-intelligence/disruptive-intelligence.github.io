---
title: Annexe F — Cadre réglementaire et normatif comparatif
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
---

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** Les statuts évoluent ; revérifier à chaque revue.

| Texte | Qui est concerné | Exigence MCS principale | Preuve attendue | Statut au 30/07/2026 |
|---|---|---|---|---|
| **NIS2** (directive UE) | Entités essentielles et importantes, par secteur et taille | Gestion des risques, dont vulnérabilités et correctifs | Politique, inventaire, mesure, incidents | Transposition française **non promulguée** ; dossier législatif ouvert |
| **ReCyF** (ANSSI) | Entités visées par la transposition | Une vingtaine d'objectifs, avec moyens acceptables de conformité et proportionnalité | Analyse d'écart, preuve par objectif | **Version de travail** du 17/03/2026 — non opposable |
| **Cyber Resilience Act** — règlement (UE) 2024/2847 | **Fabricants** de produits à éléments numériques (voir aussi importateurs, distributeurs, art. 19-20) | **Art. 13** : gestion des vulnérabilités, période de support, inventaire des composants · **Art. 14** : signalement · **Art. 16** : plateforme unique · **Art. 69** : régime transitoire | Documentation technique, avis publiés, notifications via la plateforme | En vigueur (10/12/2024) · chapitre relatif aux organismes d'évaluation depuis le 11/06/2026 · **art. 14 à compter du 11/09/2026** · application générale au 11/12/2027 [S-04] [S-05] [S-06] |
| **ISO/IEC 27001 / 27002** | Volontaire, souvent exigé par les clients | Gestion des vulnérabilités techniques, des configurations, des changements | Processus documenté + preuve d'application sur échantillon | Version 2022 en vigueur |
| **IEC 62443** | Systèmes industriels : exploitants, intégrateurs, fabricants | Gestion des correctifs adaptée au contexte industriel, zones et conduits | Plan de MCS industriel, répartition des rôles | Série en vigueur |
| **Hébergement de données de santé** | Hébergeurs, et clients par ricochet | Maintien et traçabilité, obligations contractuelles | Certification, rapports | En vigueur |
| **SecNumCloud** | Fournisseurs cloud pour usages sensibles | Exigences détaillées de MCS et de transparence client | Qualification, rapports | En vigueur — vérifier la version applicable |
| **PCI DSS** | Traitement de données de paiement | Le plus prescriptif : délais chiffrés, scans périodiques internes et externes | Rapports de scan, journaux de correction | Version 4.x en vigueur |
| **DORA** | Secteur financier européen | Gestion du risque informatique, tests, maîtrise des tiers critiques | Registre des prestataires, tests, incidents | En vigueur |
| **RGPD art. 32** | Tout responsable de traitement | Mesures appropriées à l'état de l'art | Traçabilité des décisions et des écarts | En vigueur |
| **BOD 26-04 (CISA)** | **Agences civiles fédérales américaines uniquement** | Priorisation par le risque, délais différenciés | — | Publiée le 10/06/2026. **Modèle méthodologique, aucune obligation en Europe** |

**Ce qui reste incertain au 30/07/2026** : le calendrier de promulgation du texte français de transposition · la version définitive du ReCyF et l'éventuelle évolution de ses objectifs · les modalités pratiques d'exercice des obligations de signalement produit.

---


## Annexe G — Catalogue des faux positifs, pièges et illusions

*Classé par domaine. Pour chacun : le mécanisme, et le contrôle qui le détecte.*


### G.1 Scan et détection

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 1 | Faux positif de rétroportage | Le numéro amont ne bouge pas | Comparer la révision éditeur + avis de la distribution |
| 2 | Service installé mais désactivé | Présence ≠ exécution | Vérifier l'état d'activation |
| 3 | Composant non chargé | Dépendance déclarée, jamais appelée | Atteignabilité, déclaration du fournisseur |
| 4 | Bannière modifiée | Version annoncée fausse | Scan authentifié |
| 5 | Correspondance produit erronée | Nomenclatures divergentes | Table de correspondance maintenue |
| 6 | Doublon agent / scan réseau | Deux sources, un actif | Identifiant pivot |
| 7 | Constat sur actif décommissionné | Nettoyage non fait | Réconciliation d'inventaire |
| 8 | Adresse réattribuée | L'actif détecté n'est pas le vôtre | Réconciliation |
| 9 | Constat sur image de base déjà corrigé | Analyse de la mauvaise couche | Analyser l'image finale |
| 10 | Base de détection périmée | L'outil ne sait pas chercher | Suivre l'âge du contenu |
| 11 | **« Non scanné » lu comme « non vulnérable »** | Trois états identiques dans un rapport | Les trois questions du §15.8 |
| 12 | Exclusion silencieuse | Actif retiré « temporairement » | Registre des exclusions revu en comité |


### G.2 Triage et pilotage

| # | Piège | Mécanisme |
|---|---|---|
| 13 | Seuil de gravité seul | Ignore exposition et exploitation |
| 14 | Score composite pondéré | Pondérations indéfendables ; bloque si une entrée manque |
| 15 | Discontinuité de modèle de score | Tous les scores bougent sans qu'aucun correctif ne soit appliqué |
| 16 | Dépriorisation sans date de revue | Devient un oubli |
| 17 | Faux positif déclaré sans preuve | Vide la file sans travailler |
| 18 | Constat ouvert depuis 6 mois | Dérogation non formalisée, décidée par personne |
| 19 | Compter les vulnérabilités fermées | Récompense l'agitation, pas le résultat |


### G.3 Déploiement

| # | Piège | Mécanisme |
|---|---|---|
| 20 | Correctif installé, service non redémarré | Code vulnérable toujours en mémoire |
| 21 | Correctif en mode observation jamais activé | Protection incomplète, croyance complète |
| 22 | Anneau pilote non représentatif | Valide l'installation, pas la non-régression |
| 23 | Critères d'arrêt discutés pendant l'incident | Toujours interprétés « on continue » |
| 24 | Retour arrière jamais testé | Une intention, pas un plan |
| 25 | Point de non-retour non identifié | Migration de schéma franchie sans le savoir |
| 26 | Traîne longue non qualifiée | Les 3 % les plus risqués |
| 27 | Recette non représentative | Fausse confiance, pire que pas de test |


### G.4 Configuration et identités

| # | Piège | Mécanisme |
|---|---|---|
| 28 | Référentiel appliqué sans dérivation | Contrôles désactivés un par un, baseline fictive |
| 29 | Contrôle désactivé pendant un incident | Jamais reversé |
| 30 | Rotation non répercutée | Ancien secret toujours valide |
| 31 | Autorisation déléguée | Survit au changement de mot de passe |
| 32 | Compte de service partagé | Une compromission se propage |
| 33 | Compte de secours non testé | Ne fonctionnera pas le jour venu |
| 34 | Certificat interne oublié | Expiration = panne difficile à diagnostiquer |


### G.5 Périmètre et couverture

| # | Piège | Mécanisme |
|---|---|---|
| 35 | Taux calculé sur les actifs connus | Biaisé **dans le sens favorable** |
| 36 | Actif déclaré, actif, hors outil de gestion | Tout le monde le croit géré |
| 37 | Machine éteinte non décommissionnée | Comptes et enregistrements survivants |
| 38 | Agent absent | La machine n'apparaît pas comme non conforme, elle n'apparaît plus |
| 39 | Additionner les rapports de plusieurs outils | Périmètres recouvrants, définitions divergentes |
| 40 | Actif éphémère | Absent des inventaires réseau |


### G.6 Contractuel et fournisseurs

| # | Piège | Mécanisme |
|---|---|---|
| 41 | SLA de disponibilité seul | Pousse structurellement au report des correctifs |
| 42 | Éligibilité au support étendu supposée | Programme grand public ≠ parc géré |
| 43 | Prérequis de version imposé par un éditeur | Vous héritez de son calendrier |
| 44 | Accès prestataire permanent | Exposition permanente |
| 45 | Déclaration fournisseur sans donnée | Confiance, pas preuve |


### G.7 Industriel, cloud, services en ligne, produit

| # | Piège | Mécanisme |
|---|---|---|
| 46 | Scan actif sur réseau industriel | Défaut d'automate, perte durable de confiance |
| 47 | Support amovible du prestataire | Vecteur d'entrée historique |
| 48 | Pièce de rechange non prépatchée | Remise en service en version ancienne |
| 49 | Version de service managé hors référentiel d'obsolescence | Migration subie |
| 50 | Fonctionnalité activée par défaut par le fournisseur | Exposition élargie sans décision |
| 51 | « C'est du SaaS, c'est maintenu » | Configuration, identités, intégrations restent à vous |
| 52 | Correctif produit publié sans mesure d'adoption | Le risque client ne diminue pas |
| 53 | Qualification réglementaire par gamme | Un produit exclu masque des produits inclus |

---


## Annexe H — Calendrier des échéances et ressources

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** C'est l'annexe la plus périssable du document.


### H.1 Échéances datées

| Date | Objet |
|---|---|
| 14/10/2025 | Fin de support de Windows 10 |
| 15/04/2026 | Priorisation de l'enrichissement des fiches du NVD par le NIST |
| 11/06/2026 | Applicabilité du chapitre du CRA relatif aux organismes d'évaluation de la conformité |
| 15/06/2026 | Début de publication des scores EPSS v5 — **rupture de série** |
| 24 et 27/06/2026 | Expiration des certificats de démarrage sécurisé émis en 2011 (KEK CA, UEFI CA) |
| 11/09/2026 | Applicabilité des obligations de signalement du CRA |
| 13/10/2026 | Fin de support de Windows 10 Entreprise / IoT LTSB 2016 |
| 19/10/2026 | Expiration du certificat Windows Production PCA 2011 |
| 12/01/2027 | Fin de support étendu de Windows Server 2016 |
| 12/10/2027 | Fin du programme de support étendu **grand public** de Windows 10 — **exclut les machines gérées** |
| 11/12/2027 | Application générale du CRA |


### H.2 Échéances récurrentes sans date fixe

*À intégrer au référentiel d'obsolescence (§12.2), avec vérification à la source.*

| Objet | Cycle typique |
|---|---|
| Distributions Linux à support long | 5 à 10 ans, prolongations par abonnement |
| Moteurs de bases de données | 5 à 8 ans (versions majeures) |
| **Environnements d'exécution applicatifs** | **2 à 4 ans** — principale source d'obsolescence invisible |
| Versions d'orchestrateur de conteneurs | ~14 mois (12 standard + 2 limités) |
| Services managés cloud | Variable, annoncé plusieurs mois à l'avance |
| Équipements réseau — fin de support **de sécurité** | Souvent antérieure de plusieurs années à la fin de vie matérielle |
| Micrologiciels serveurs | 5 à 7 ans après commercialisation |
| Certificats publics | Durées en réduction progressive |


### H.3 Sources de veille et cadence

| Source | Cadence | Usage |
|---|---|---|
| Avis des éditeurs de vos produits C1 | Quotidienne | **Source de vérité** sur les versions |
| Avis des distributions | Quotidienne | Révisions rétroportées |
| Bulletins des centres de réponse nationaux | Quotidienne | Point d'entrée principal |
| Centres de réponse et communautés sectoriels | Hebdomadaire | Ciblage de votre secteur |
| Catalogues d'exploitation avérée | Quotidienne | Déclencheur d'urgence |
| Bases agrégées | Quotidienne | Couverture |
| **Notes de version des services cloud et en ligne** | **Mensuelle** | La ligne la plus faible de la plupart des dispositifs |
| Pages de cycle de vie des éditeurs | Trimestrielle | Référentiel d'obsolescence |
| Publications des agences nationales | Mensuelle | Doctrine, guides, référentiels |


### H.4 Formations et certifications

*Aucune certification ne porte spécifiquement sur le MCS. Les plus utiles au regard de ce cours :*

| Domaine | Utilité réelle |
|---|---|
| Management de la sécurité de l'information | Utile pour la partie gouvernance, preuve et audit |
| Sécurité industrielle | Indispensable si votre périmètre comprend de l'OT |
| Administration système et cloud | Le socle technique des chapitres 2, 3, 30 |
| Gestion des vulnérabilités (certifications éditeurs) | Utile sur l'outil, peu transférable |
| Analyse de risque (méthodes reconnues) | Utile pour la criticité et l'acceptation de risque |

⚠️ Une certification atteste d'une connaissance, pas d'une pratique. Les compétences réellement déterminantes de ce cours — négocier une fenêtre, obtenir un propriétaire, écrire une dérogation défendable — ne s'enseignent pas en formation.


### H.5 Ressources et communautés

Publications des agences nationales de cybersécurité · centres de réponse aux incidents nationaux et sectoriels · groupements professionnels de RSSI · communautés d'utilisateurs de vos outils · conférences sécurité généralistes et sectorielles · publications des éditeurs sur les incidents et les retours d'expérience.

---


## Annexe I — Modèle de données MCS

> Modèle relationnel minimal. Types : `str` texte · `enum` valeur contrôlée · `date` · `bool` · `ref` référence · `int`. Cardinalité : `1` obligatoire unique · `0..1` optionnel · `0..n` multiple.
