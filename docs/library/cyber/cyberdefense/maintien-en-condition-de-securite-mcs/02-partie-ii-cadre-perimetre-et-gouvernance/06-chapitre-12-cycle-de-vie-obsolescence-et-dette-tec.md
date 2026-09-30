---
title: Chapitre 12 — Cycle de vie, obsolescence et dette technique
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

## 12.1 Le vocabulaire des fins de support, et ses pièges contractuels

L'obsolescence est la seule menace de ce cours dont la date est **annoncée à l'avance**. C'est aussi celle qui produit le plus de situations subies. Le décalage s'explique en grande partie par un vocabulaire flou, que les éditeurs n'ont aucun intérêt à clarifier.

| Terme | Ce qu'il signifie réellement | Ce que les gens comprennent |
|---|---|---|
| **Fin de commercialisation** | On ne peut plus l'acheter | Souvent confondu avec la fin de support |
| **Fin de vie fonctionnelle** | Plus de nouvelles fonctionnalités, mais correctifs de sécurité maintenus | « C'est fini » — alors que non |
| **Fin de support** | **Plus aucun correctif, y compris de sécurité.** La seule date qui compte pour le MCS | Souvent découverte après coup |
| **Support étendu** | Correctifs de sécurité uniquement, contre paiement, sous conditions strictes | « On pourra prolonger » — sans vérifier l'éligibilité |
| **Fin de support étendu** | Terme absolu | Rarement anticipée |
| **Support de sécurité prolongé par un tiers** | Un acteur autre que l'éditeur maintient des correctifs | Confondu avec un support officiel |

⚠️ **PIÈGE — les cinq clauses qui se découvrent trop tard**

1. **L'éligibilité conditionnelle.** Un support étendu est presque toujours réservé à certaines éditions, certaines versions minimales, certains modes de gestion, certains types de licence. La vérification doit être faite **actif par actif**, pas au niveau du produit.
2. **La tarification croissante.** Beaucoup de programmes voient leur tarif augmenter à chaque année reconduite, souvent en doublant. Un budget calculé sur la première année sous-estime gravement une prolongation de trois ans.
3. **Le prérequis d'état.** Certaines offres exigent que la machine soit déjà à jour d'un niveau de correctif précis au moment de la souscription. Une machine trop en retard peut être **inéligible**, ce qui supprime l'option de repli.
4. **La couverture partielle.** Le support étendu ne couvre en général que les vulnérabilités jugées critiques par l'éditeur, selon ses propres critères. Ce n'est pas un support normal prolongé.
5. **La date de décision.** Souscrire après la fin de support coûte souvent la rétroactivité complète des périodes écoulées — la procrastination est facturée.

✅ **BONNE PRATIQUE (P0)** — Pour chaque option de support étendu envisagée, produisez une note d'une page avant tout arbitrage budgétaire : périmètre exact d'éligibilité **vérifié sur votre parc**, coût sur toute la durée envisagée, ce qui est couvert et ce qui ne l'est pas, et date limite de décision. Cette note évite l'essentiel des mauvaises surprises du domaine.

## 12.2 Construire et tenir un référentiel de fin de support

**L'objectif** : pouvoir répondre à tout moment à la question *« combien d'actifs sortent du support dans les 24 prochains mois, et lesquels ? »*. Sans cette capacité, aucun plan pluriannuel n'est possible.

**Les sources, par fiabilité décroissante :**

| Source | Fiabilité | Remarque |
|---|---|---|
| Page officielle de cycle de vie de l'éditeur | **Fait vérifié** | Seule source opposable ; à consulter, pas à mémoriser |
| Contrat de support signé | Fait vérifié | Peut différer de la politique publique |
| Bases publiques agrégeant les dates de fin de vie | Hypothèse probable | Très pratiques pour le dégrossissage, à confirmer sur les décisions engageantes |
| Connaissance des équipes | Piste exploratoire | Souvent périmée |

**La méthode, en trois temps :**

1. **Extraire** de l'inventaire la liste des systèmes, versions et modèles matériels distincts. Cette liste est bien plus courte que le parc — souvent quelques dizaines de lignes pour plusieurs centaines d'actifs.
2. **Documenter** pour chaque ligne les trois dates : fin de support, fin de support étendu si applicable, source et date de vérification.
3. **Réinjecter** ces dates dans l'inventaire, au niveau de l'actif, pour pouvoir croiser avec la criticité et l'exposition.

⚠️ **PIÈGE — l'obsolescence par composant plutôt que par machine**
Le raisonnement s'arrête trop souvent au système d'exploitation. Or l'obsolescence frappe aussi les moteurs de bases de données, les environnements d'exécution applicatifs, les bibliothèques embarquées, les versions de clusters, les modèles de matériel, les micrologiciels et les certificats. Une machine dont le système est parfaitement supporté peut porter quatre composants hors support — c'est le sujet du chapitre 26.

## 12.3 Le plan de sortie d'obsolescence

Un plan de sortie d'obsolescence n'est pas une liste : c'est une **trajectoire financée**, avec des jalons et un séquencement.

**Les cinq composants d'un plan crédible :**

| Composant | Contenu | Erreur fréquente |
|---|---|---|
| **Trajectoire** | Quels lots, dans quel ordre, sur quels exercices | Tout traiter la même année |
| **Séquencement technique** | Dépendances : migrer l'annuaire avant les applications qui s'y appuient | Découvrir la dépendance en cours de migration |
| **Financement** | Coût par lot, réparti sur les exercices | Un montant global qui ne passe aucun arbitrage |
| **Jalons de décision** | Dates auxquelles une décision doit être prise, y compris de report | Absence de point de contrôle |
| **Plan de repli** | Que fait-on si le lot n'est pas prêt à l'échéance ? | Aucun — donc report subi |

**Le critère de séquencement qui fonctionne.** Ne triez pas par date de fin de support, triez par **produit criticité × exposition × effort**. Un actif hors support depuis deux ans mais isolé et peu critique passe après un actif exposé qui sortira du support dans six mois. La date n'est qu'une des trois entrées.

✅ **BONNE PRATIQUE (P1) — la règle du lot suivant**
À tout moment, le lot en cours doit être financé **et** le lot suivant doit être chiffré. Sans cette règle, chaque lot se négocie isolément et le plan pluriannuel n'existe que sur le papier.

## 12.4 ⏱ Panorama des échéances structurantes

*Bloc périssable, vérifié le 30/07/2026. Le calendrier complet et actualisé figure en **Annexe H**.*

**Les échéances majeures du poste de travail et du serveur Windows :**

| Objet | Date | Point d'attention |
|---|---|---|
| Windows 10 — fin de support | 14 octobre 2025 | Échéance **passée** |
| Windows 10 Entreprise LTSB 2016 — fin de support | 13 octobre 2026 | À ne pas confondre avec le Windows 10 grand public |
| Windows Server 2016 — fin de support étendu | 12 janvier 2027 | Souvent sous-estimée dans les parcs |

**Les échéances récurrentes à surveiller sans date fixe** — et c'est la partie la plus utile de cette section, parce qu'elle reste vraie quand les dates ci-dessus auront été franchies :

- **distributions Linux à support long** : cycles de 5 à 10 ans, avec des options de prolongation par abonnement ;
- **moteurs de bases de données** : cycles de 5 à 8 ans, avec des versions intermédiaires au support beaucoup plus court ;
- **environnements d'exécution applicatifs** : cycles souvent **très courts**, de 2 à 4 ans, et c'est la principale source d'obsolescence invisible (chapitre 26) ;
- **versions de clusters d'orchestration** : de l'ordre de quatorze mois (§3.3) ;
- **équipements réseau et de sécurité** : la fin de support **de sécurité** est souvent antérieure à la fin de vie matérielle — les deux dates doivent être suivies séparément ;
- **matériel serveur** : fin de support des micrologiciels, souvent 5 à 7 ans après la commercialisation.

## 12.5 ⏱ L'économie du support étendu, et un cas d'école

*Bloc périssable, vérifié le 30/07/2026.*

Le cas Windows 10 constitue actuellement l'illustration la plus complète des cinq pièges du §12.1, et il mérite d'être détaillé pour cette raison — le mécanisme vaut bien au-delà de cet éditeur.

**La situation.** Windows 10 est en fin de support depuis le 14 octobre 2025. Deux programmes de prolongation coexistent, et ils n'ont ni le même public, ni le même coût, ni la même échéance.

| Programme | Public | Échéance | Coût |
|---|---|---|---|
| Support étendu **grand public** | Appareils **personnels** | Prolongé jusqu'au 12 octobre 2027 | Gratuit ou faible, selon modalité d'inscription |
| Support étendu **commercial** | Organisations | Jusqu'à trois années après la fin de support | Payant, tarif croissant d'année en année |

⚠️ **LE PIÈGE, et il est majeur.** Le programme grand public **exclut explicitement les machines jointes à un annuaire d'entreprise ou gérées par une solution de gestion de flotte**. Autrement dit : un parc professionnel géré n'est **pas** couvert par la prolongation à octobre 2027, quelle que soit l'édition installée. Une organisation qui lit l'annonce de prolongation et en conclut qu'elle dispose d'un an de plus se trompe de programme — et le découvrira au moment où il sera trop tard pour arbitrer.

📎 [S-24]

**La leçon généralisable, qui survivra à ce cas particulier :**

> Une option de support ne se budgète jamais avant d'avoir vérifié, sur son propre parc et actif par actif, son périmètre d'éligibilité et ses conditions.

**Le calcul à faire systématiquement.** Comparez trois scénarios sur la durée complète, pas sur la première année :

| Scénario | Coûts à intégrer |
|---|---|
| Support étendu sur N années | Coût croissant par actif × N + coût de la migration ensuite, qui reste à payer |
| Migration immédiate | Licences, matériel, tests de compatibilité applicative, formation, charge projet |
| Ne rien faire | Mesures compensatoires, surveillance renforcée, risque accepté, position en cas d'incident ou de contrôle |

Le troisième scénario doit **toujours** figurer dans le tableau, chiffré. C'est en le voyant que les directions arbitrent, et son absence est la raison la plus fréquente pour laquelle un dossier d'obsolescence n'obtient pas de financement.

## 12.6 Mesurer la dette et la présenter à une direction

Le §1.6 a posé le principe. Voici la mise en œuvre.

**Les quatre grandeurs, et leur formulation.**

| Grandeur | Définition | Ce qu'elle démontre |
|---|---|---|
| **Actifs hors support, pondérés par la criticité** | Nombre d'actifs sans correctif disponible, pondéré C1 ×5, C2 ×3, C3 ×1 | L'ampleur structurelle |
| **Vulnérabilités critiques échues** | Constats critiques dont le délai de la classe de service est dépassé | Le retard opérationnel |
| **Dérogations ouvertes et leur âge** | Nombre et ancienneté moyenne | La dette **formellement acceptée** |
| **Âge moyen des constats non traités** | Durée depuis la première détection | La vitesse réelle de l'organisation |

**La présentation qui fonctionne en comité de direction**, en trois diapositives et pas une de plus :

1. **La trajectoire.** L'évolution de la dette sur quatre à huit trimestres. Une direction ne réagit pas à un niveau, elle réagit à une **pente**.
2. **Le point de bascule.** À quelle date, sans décision, la situation se dégrade mécaniquement — typiquement la prochaine échéance de fin de support majeure.
3. **Les trois options chiffrées.** Support étendu, migration, statu quo — avec pour chacune le coût et le risque résiduel.

⚠️ **PIÈGE — présenter la dette sans option**
Une présentation qui expose un problème sans proposer d'options chiffrées produit de l'anxiété, puis de l'évitement. La direction ne peut pas arbitrer ce qu'elle ne peut pas comparer, et l'arbitrage par défaut est le report.

## 12.7 ⚠️ « On migrera l'année prochaine »

mécanique du report perpétuel

Le report est rationnel du point de vue de chaque acteur pris isolément, et c'est pour cela qu'il est si difficile à casser.

| Acteur | Sa logique locale | Pourquoi elle est rationnelle pour lui |
|---|---|---|
| Le métier | « Ça marche, ne touchons à rien » | Il porte le risque d'interruption, pas le risque de sécurité |
| L'exploitation | « Nous n'avons pas la charge disponible » | C'est vrai, et la migration s'ajoute au reste |
| La direction financière | « Décalons d'un exercice » | Un décalage améliore le résultat de l'année en cours |
| L'éditeur métier | « Notre version compatible arrive bientôt » | Il n'a pas d'incitation à accélérer |
| La sécurité | Elle alerte, sans mandat pour trancher | Son alerte n'est pas une décision |

**La somme de comportements localement rationnels produit un résultat collectivement absurde.** Ce n'est pas un problème de personnes, et le traiter comme tel garantit l'échec.

**Les quatre leviers qui cassent réellement le cycle :**

1. **La date de bascule visible.** Rendre publique une date après laquelle le report devient une décision explicite de la direction générale, avec signature. Le report cesse d'être un non-choix.
2. **Le coût du report chiffré chaque année.** Support étendu, mesures compensatoires, heures supplémentaires. Un montant qui réapparaît chaque exercice finit par être comparé au coût de la migration.
3. **L'exigence externe.** Un client, un assureur ou un auditeur qui refuse de valider un système hors support (§7.5).
4. **Le lot pilote.** Migrer un périmètre restreint démontre la faisabilité et produit un chiffrage réel. L'argument « c'est trop risqué » ne résiste pas à une migration déjà réalisée ailleurs dans la maison.

## 12.8 🔴 FIL ROUGE — octobre 2026

620 postes et une échéance dans quinze jours

Le 13 octobre 2026 approche. HELIOMED est concerné par trois échéances distinctes, et Claire Nadeau commence par les séparer — parce qu'elles ont été confondues pendant six mois.

| Population | Échéance | Situation réelle |
|---|---|---|
| Banc de test de Saint-Étienne, sous Windows 10 Entreprise LTSB 2016 | **13 octobre 2026** | 1 poste, critique pour la validation des pompes PX-40 |
| 620 postes bureautiques Windows 10, joints au domaine, gérés par l'infogérant | Fin de support depuis le 14/10/2025 | **Non éligibles** au programme grand public |
| 11 serveurs Windows Server 2016 | 12 janvier 2027 | Dont 3 portant des applications métier |

**La découverte qui change tout.** Le chargé de compte de l'infogérant Numeria avait indiqué en juin que « la prolongation annoncée par l'éditeur couvre le parc jusqu'en octobre 2027 ». Malik Ferhaoui vérifie ligne à ligne les conditions d'éligibilité, comme le recommande le §12.1 : le programme invoqué est le programme **grand public**, qui exclut les machines jointes au domaine. Les 620 postes n'ont **jamais** été couverts, et ne recevaient plus de correctifs de sécurité depuis douze mois.

Le sujet cesse d'être un sujet de calendrier. Il devient un sujet de responsabilité contractuelle — traité au chapitre suivant.

**Les trois options présentées au comité stratégique.**

| Option | Coût | Risque résiduel |
|---|---|---|
| Support étendu commercial, 2 ans, sur 620 postes | Coût par poste croissant d'une année sur l'autre + coût de la migration ensuite, qui reste dû | Correctifs critiques uniquement, aucun autre bénéfice |
| Migration en trois lots sur 9 mois | Renouvellement partiel du matériel, tests applicatifs, charge projet | Élevé pendant la période de transition, nul ensuite |
| Statu quo | Zéro budget affiché | 620 postes sans correctif, position intenable en cas d'incident ou de contrôle |

Karim Lebrun, directeur financier, tranche en quinze minutes une fois le tableau posé : la première option coûte, sur deux ans, une part significative du coût de la migration — sans en produire aucun bénéfice durable. La deuxième est retenue, avec un support étendu **partiel** limité à 140 postes portant des applications métier non encore validées sur le nouveau système : c'est un pont, chiffré et daté, pas une solution.

**Le cas du banc de test.** Un seul poste, non migrable — l'outil de validation constructeur n'existe pas sur une version plus récente, et le fournisseur a disparu. La décision relève du chapitre 32 : sanctuarisation, retrait du réseau, transferts par support maîtrisé, dérogation signée par le directeur général avec revue semestrielle. Coût de la solution : quelques milliers d'euros de segmentation, contre le coût d'un remplacement complet de la chaîne de validation.

**Livrable de l'épisode.** Un plan de sortie d'obsolescence sur dix-huit mois, en trois lots financés, avec un pont chiffré, une sanctuarisation documentée, et — ce que Claire considère comme le point le plus important — **une note écrite établissant que les 620 postes n'ont pas reçu de correctifs pendant douze mois**, avec sa cause. Cette note sera au cœur de la négociation contractuelle.

→ La suite en 🔴 §13.9, pour la renégociation du contrat d'infogérance.

→ **Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs** : ce qui se passe quand le maintien est confié à un tiers.

## Synthèse mentale du chapitre 12

L'obsolescence est la seule menace dont la date est annoncée à l'avance, et pourtant celle qui produit le plus de situations subies — un vocabulaire flou y contribue, que les éditeurs n'ont pas intérêt à clarifier. Cinq clauses se découvrent trop tard : éligibilité conditionnelle, tarification croissante, prérequis d'état, couverture partielle et rétroactivité. Un référentiel de fin de support se construit sur la liste des versions distinctes, bien plus courte que le parc, et doit couvrir les composants autant que les systèmes. Un plan crédible est une trajectoire financée avec des jalons, séquencée par criticité × exposition × effort plutôt que par date. Le report perpétuel résulte de comportements localement rationnels, ce qui interdit de le traiter comme un problème de personnes : il se casse par une date de bascule visible, un coût de report chiffré chaque année, une exigence externe et un lot pilote. Enfin, tout dossier d'obsolescence doit présenter trois options chiffrées, dont le statu quo — son absence est la première cause de non-financement.

**Trois questions de vérification**

1. Un éditeur annonce la prolongation du support de votre système d'exploitation. Quelles vérifications faites-vous avant d'inscrire cette prolongation dans votre plan, et sur quel niveau de granularité ?
2. Pourquoi trier un plan de sortie d'obsolescence par date de fin de support conduit-il à de mauvaises priorités ? Par quoi remplacez-vous ce critère ?
3. Votre direction a reporté la même migration trois années de suite, chaque fois pour de bonnes raisons. Quels leviers activez-vous, et lequel ne dépend pas d'elle ?

---
