---
title: Chapitre 7 — Doctrine et politique MCS
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

## 7.1 Ce qui distingue une politique appliquée d'un document mort

La plupart des organisations ont déjà une politique de sécurité qui mentionne les correctifs. La plupart de ces mentions ne sont pas appliquées. La différence entre les deux situations ne tient pas à la qualité rédactionnelle, mais à trois propriétés très concrètes.

**Une politique appliquée est décidable.** Chaque phrase doit permettre de trancher un cas réel. « Les correctifs de sécurité sont appliqués dans les meilleurs délais » ne permet de trancher aucun cas : quel délai, sur quel actif, décidé par qui. À l'inverse, « les correctifs concernant une vulnérabilité exploitée sur un actif exposé à Internet sont appliqués sous 72 heures, y compris hors fenêtre, sur décision du propriétaire technique » se vérifie et s'oppose.

**Une politique appliquée est finançable.** Si elle impose un scan authentifié mensuel du parc alors qu'aucune licence ni aucun temps homme n'y sont affectés, elle organise sa propre violation. Une politique qui dépasse les moyens engagés génère une non-conformité permanente, ce qui est pire que l'absence de politique : cela habitue tout le monde à ce que la règle ne soit pas tenue.

**Une politique appliquée prévoit sa propre transgression.** C'est le point le plus contre-intuitif et le plus important. Il existera toujours des situations où corriger est impossible. Si la politique ne prévoit pas de chemin légitime pour ces cas — la dérogation du §7.4 — les équipes emprunteront un chemin illégitime : le silence.

**Structure recommandée.** Un document court, de huit à douze pages, en sept sections :

| Section | Contenu | Longueur indicative |
|---|---|---|
| 1. Objet et périmètre | Ce qui est couvert, ce qui ne l'est pas et pourquoi | ½ page |
| 2. Définitions | Vocabulaire arrêté, notamment actif, propriétaire, couverture, conformité | 1 page |
| 3. Rôles et responsabilités | Renvoi au RACI, décideurs nommés par catégorie | 1 page |
| 4. Classes de service | Le cœur du document (§7.2) | 2-3 pages |
| 5. Processus | Veille, détection, triage, correction, vérification, preuve | 2-3 pages |
| 6. Dérogations | Procédure, durée, signataires, revue (§7.4) | 1 page |
| 7. Mesure et contrôle | Indicateurs, fréquence, destinataires | 1 page |

⚠️ **PIÈGE — la politique qui liste des outils**
Une politique qui nomme des produits devient obsolète au premier changement d'outillage, et elle transforme un document de doctrine en documentation technique. Les outils vivent dans les procédures d'exploitation, qui se modifient sans passer par le circuit d'approbation de la politique.

## 7.2 Les classes de service : le cœur du dispositif

C'est la section qui rend une politique opérationnelle. L'idée : **on ne traite pas tous les actifs de la même façon**, et cette différenciation doit être écrite, pas improvisée.

**Construire les classes.** Trois à quatre classes suffisent — au-delà, plus personne ne sait dans laquelle ranger un actif. Le critère de classement combine deux dimensions : la **criticité métier** (que se passe-t-il si cet actif tombe ou fuit ?) et l'**exposition** (qui peut l'atteindre ?).

| Classe | Définition | Exemples typiques |
|---|---|---|
| **C1 — Critique exposé** | Actif de niveau 0, ou joignable depuis Internet, ou portant une donnée sensible | Passerelle d'accès distant, annuaire, hyperviseur, console de sauvegarde, service public |
| **C2 — Important** | Actif métier significatif, non exposé directement | Serveurs applicatifs internes, bases de données métier |
| **C3 — Courant** | Actif dont l'indisponibilité est tolérable | Postes de travail standard, serveurs de fichiers secondaires |
| **C4 — Contraint** | Actif que l'on ne peut pas corriger normalement | Systèmes industriels, legacy sous contrat figé, appliances fermées |

La classe C4 est indispensable et souvent oubliée. Sans elle, ces actifs sont classés dans une catégorie dont ils violeront en permanence les règles, ce qui pollue tous les indicateurs. Les nommer explicitement permet de leur appliquer un régime différent — compensation obligatoire plutôt que correction — et de mesurer honnêtement.

**Ce que chaque classe définit.** Pour chaque classe, six paramètres, et pas un de plus :

| Paramètre | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| Délai de correction — vulnérabilité exploitée | 72 h | 7 j | 30 j | Compensation sous 72 h |
| Délai de correction — critique non exploitée | 15 j | 30 j | 60 j | Compensation ou dérogation |
| Délai — reste | 30 j | 90 j | 180 j | Selon fenêtre constructeur |
| Fréquence de vérification | Hebdomadaire | Mensuelle | Mensuelle | Trimestrielle |
| Niveau de test avant déploiement | Recette + témoin | Témoin | Anneau pilote | Validation fournisseur |
| Fenêtre | Récurrente hebdomadaire + urgence autorisée | Mensuelle | Mensuelle | Arrêt planifié |

*Les valeurs ci-dessus sont un point de départ réaliste pour une organisation de taille intermédiaire, pas une norme. Ce qui compte n'est pas le chiffre, c'est qu'il soit **écrit, tenable et mesuré**.*

✅ **BONNE PRATIQUE (P0)** — Calibrez vos délais sur ce que vous pouvez réellement tenir, pas sur ce qui fait bien. Une politique annonçant 48 h que vous tenez trois fois par an vous met en position de non-conformité permanente devant un auditeur, un assureur ou un client. Une politique annonçant 15 jours et tenue à 92 % est infiniment plus solide — et vous pourrez la resserrer ensuite, ce qui est un progrès démontrable.

## 7.3 Le contrat interne entre sécurité et production

Le conflit MCO/MCS du §1.2 ne se résout pas par autorité. Il se résout par un engagement **réciproque**, formalisé dans la politique, et c'est la réciprocité qui le rend applicable.

**Ce que la sécurité s'engage à fournir :**

- un périmètre et une priorisation stables, pas une liste de 4 000 constats à trier soi-même ;
- un volume de demandes compatible avec les moyens de l'exploitation, avec un plafond mensuel assumé ;
- une qualification préalable de chaque demande urgente — exposition mesurée, exploitation vérifiée, pas de fausse alerte ;
- l'acceptation formelle du risque lorsqu'un report est décidé, portée par la sécurité et non par l'exploitant.

**Ce que la production s'engage à fournir :**

- des fenêtres récurrentes garanties, pas renégociées mensuellement ;
- l'application dans les délais définis par classe de service ;
- la remontée d'une preuve exploitable, pas une confirmation verbale ;
- l'alerte immédiate en cas d'impossibilité, plutôt que le silence — c'est la contrepartie de l'existence d'une procédure de dérogation.

Ce dernier point est le pivot. **Le silence est le pire résultat possible** : il produit un écart invisible, donc non compensé, donc non financé. Une organisation qui punit les remontées d'impossibilité fabrique mécaniquement son propre angle mort.

## 7.4 La procédure de dérogation

Une dérogation est une décision formelle de ne pas appliquer la règle, pour un actif, une vulnérabilité et une durée déterminés. Bien conçue, c'est un instrument de pilotage. Mal conçue, c'est une machine à dissimuler.

**Les sept champs obligatoires** — repris de la logique du §5.3 et développés au chapitre 20 :

| Champ | Pourquoi il est indispensable |
|---|---|
| Objet précis | Quel actif, quelle vulnérabilité, quel correctif — jamais « les serveurs de l'usine » |
| Motif | Technique, contractuel, métier, budgétaire — le motif oriente la solution |
| **Date d'expiration** | Une dérogation sans date est une renonciation |
| Mesure compensatoire | Obligatoire ; une dérogation nue n'est pas acceptable |
| Moyen de vérification | Comment saura-t-on que la compensation est toujours en place ? |
| Signataire | Le propriétaire métier, pas la sécurité — celui qui porte le risque le signe |
| Condition de sortie | Quel événement met fin à la dérogation |

⚠️ **PIÈGE — la dérogation renouvelée par défaut**
Le mécanisme de dégradation est toujours le même : la dérogation arrive à échéance, rien n'a changé, on reconduit. Trois ans plus tard, elle est devenue un état permanent que plus personne n'interroge.
**Le garde-fou qui fonctionne** : le renouvellement d'une dérogation exige une signature de **niveau supérieur** à la précédente. Le premier renouvellement remonte au directeur des systèmes d'information, le second à la direction générale. Le coût politique croissant force l'arbitrage — soit on corrige, soit on assume au bon niveau.

✅ **BONNE PRATIQUE (P1)** — Suivez l'**âge moyen des dérogations ouvertes** comme indicateur de premier plan (chapitre 38). C'est la mesure la plus honnête de la dette de sécurité réellement acceptée par l'organisation, et elle est plus parlante en comité que n'importe quel décompte de vulnérabilités.

## 7.5 Obtenir le sponsor : construire l'argumentaire

Un programme de MCS sans soutien explicite de la direction générale échouera sur le premier arbitrage sérieux. Voici les quatre leviers qui fonctionnent, par ordre d'efficacité constatée.

**1. L'exigence externe.** Un assureur, un client, un auditeur ou un régulateur qui demande une preuve crée une obligation que la sécurité seule ne peut pas créer. C'est le levier le plus rapide, et il est souvent déjà disponible — il suffit de le lire.

**2. L'incident sectoriel.** Un concurrent ou un pair touché, publiquement, avec un vecteur d'entrée documenté que vous partagez. La fenêtre d'attention est courte : quelques semaines. Préparez le dossier à l'avance pour pouvoir le sortir au bon moment.

**3. Le coût du non-fait, chiffré.** L'approche du §6.13, appliquée à l'échelle du programme : coût des interventions en urgence, des mesures compensatoires, du support étendu, des heures d'astreinte, comparé au coût de la mise à niveau. Ce levier est le plus solide dans la durée, parce qu'il ne dépend pas de l'émotion.

**4. Le risque, en dernier.** Contre-intuitif, mais l'expérience est constante : l'argument « nous pourrions être attaqués » est le moins efficace des quatre auprès d'une direction générale, parce qu'il est invérifiable et que tout le monde l'a déjà entendu.

📌 **LIMITES** — Aucun de ces leviers ne produit un budget pérenne à lui seul. Ce qui pérennise, c'est la **démonstration de progrès mesuré** : un indicateur de résultat qui s'améliore trimestre après trimestre transforme une dépense en investissement aux yeux d'un directeur financier. C'est pourquoi le chapitre 38 arrive avant le chapitre 40.

## 7.6 ⚠️ Les politiques mort-nées : symptômes, causes, réanimation

| Symptôme observable | Cause profonde | Ce qui la réanime |
|---|---|---|
| Personne ne peut citer un délai de correction | Politique trop générale, non décidable | Réécrire la section classes de service, supprimer le reste |
| Aucune dérogation enregistrée depuis un an | Ce n'est pas que tout est corrigé : c'est que les écarts sont invisibles | Rendre la dérogation facile, rapide et non punitive |
| Les indicateurs sont excellents et personne n'y croit | Dénominateur faux (§2.9) | Publier le périmètre de référence avec le chiffre |
| Le document date de trois ans | Aucun propriétaire ni revue planifiée | Nommer un propriétaire et une date de revue annuelle |
| Elle s'applique à « tous les systèmes » | Aucune classe C4 : les cas contraints violent la règle en permanence | Créer la classe des actifs contraints et l'assumer |

## 7.7 🔴 FIL ROUGE — mai 2026

la politique MCS v1 et ses trois compromis

Claire Nadeau rédige la première politique MCS d'HELIOMED. Onze pages. Trois compromis y sont assumés explicitement, et c'est ce qui la rend applicable.

**Compromis n° 1 — des délais volontairement modestes.** Le premier projet annonçait 24 h pour une vulnérabilité exploitée en classe C1. Malik Ferhaoui démontre chiffres à l'appui que l'équipe, à deux personnes, ne peut pas le tenir en dehors d'une mobilisation exceptionnelle. Le délai retenu est **72 h**, avec un engagement de révision à 48 h une fois l'outillage d'anneaux en place. Claire préfère un engagement tenu à un affichage flatteur.

**Compromis n° 2 — l'usine sort du régime commun.** Les actifs de Saint-Étienne entrent en classe C4 : régime de compensation et non de correction, fenêtre unique lors de l'arrêt de production d'août, revue trimestrielle. Thomas Berger signe, parce que la règle correspond enfin à ce qu'il peut réellement faire. Les indicateurs les distinguent désormais du reste du parc — le taux de conformité global cesse d'être pollué par des actifs qu'on savait non corrigeables.

**Compromis n° 3 — le parc infogéré reste hors périmètre de mesure, temporairement.** Les 620 postes gérés par le prestataire Numeria ne peuvent pas être mesurés faute d'accès aux données de la console du prestataire. Plutôt que de publier un chiffre inventé, la politique déclare explicitement : *périmètre non mesuré, échéance de mise sous contrôle au 31/12/2026, traité par avenant contractuel.* Ce trou déclaré deviendra l'un des deux leviers de la renégociation du chapitre 13.

**La clause qui déclenche le plus de discussion** est celle du renouvellement de dérogation avec signature de niveau supérieur. Deux responsables y voient une marque de défiance. Pierre Vasseur, directeur général, tranche en trois phrases : si une exception est justifiée, la signer ne coûte rien ; si elle ne l'est pas, il vaut mieux qu'il l'apprenne maintenant.

**Livrable de l'épisode.** La politique MCS v1, plus une annexe d'une page listant les périmètres explicitement non couverts avec leur échéance de mise sous contrôle. Cette annexe, apparemment un aveu de faiblesse, sera l'élément le mieux noté lors de la revue de janvier 2027 (chapitre 39).

→ La suite en 🔴 §8.10, quand un référentiel publié en mars vient confronter cette politique à une grille externe.

→ **Chapitre 8 — Cadre réglementaire et normatif applicable** : ce que l'extérieur exige, et comment lire un référentiel sans s'y perdre.

## Synthèse mentale du chapitre 7

Une politique MCS n'est utile que si chacune de ses phrases permet de trancher un cas réel, si les moyens de l'appliquer sont engagés, et si elle prévoit un chemin légitime pour les cas où corriger est impossible — faute de quoi les équipes emprunteront le chemin du silence. Son cœur est la table des classes de service : trois à quatre classes croisant criticité métier et exposition, dont une classe explicite pour les actifs contraints qu'on sait ne pas pouvoir corriger. Les délais doivent être calibrés sur ce qu'on tient réellement, pas sur ce qui impressionne. Le conflit avec la production se résout par un engagement réciproque dont le pivot est la remontée immédiate des impossibilités. Une dérogation comporte sept champs, dont une date d'expiration et une mesure compensatoire, et son renouvellement doit coûter politiquement plus cher que le précédent. Enfin, l'argument qui obtient un sponsor est rarement le risque : c'est l'exigence externe, l'incident sectoriel ou le coût chiffré du non-fait.

**Trois questions de vérification**

1. Votre politique annonce un délai de correction de 48 heures que vous tenez trois fois par an. Pourquoi est-ce plus dangereux que d'annoncer 15 jours, et devant qui ?
2. Aucune dérogation n'a été enregistrée dans votre organisation depuis douze mois. Quelle est l'interprétation optimiste, quelle est l'interprétation réaliste, et comment tranchez-vous ?
3. Pourquoi une classe de service dédiée aux actifs non corrigeables améliore-t-elle la qualité de vos indicateurs plutôt que de la dégrader ?

---
