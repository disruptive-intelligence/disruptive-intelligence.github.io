---
title: Chapitre 37 — Économie du MCS, charge de travail et facteur humain
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE VI — Fin de vie, industrialisation et soutenabilité
  - index.md
---

## 37.1 Chiffrer le MCS

Un programme non chiffré n'est pas arbitrable, et un programme non arbitré est financé par défaut — c'est-à-dire mal.

**Les six postes de coût**, dont trois sont presque toujours omis :

| Poste | Contenu | Souvent omis ? |
|---|---|---|
| Personnel | ETP consacrés à la veille, au triage, au déploiement, à la preuve | Non |
| Licences et outillage | Scan, déploiement, gestion, journalisation | Non |
| **Coût d'interruption** | Production perdue pendant les fenêtres | **Oui** |
| **Coût de test** | Environnements, jeux de données, temps métier de validation | **Oui** |
| Dette d'obsolescence | Support étendu, migrations à venir | Parfois |
| **Coût des compensations** | Charge récurrente des mesures compensatoires (§20.7, attribut 5) | **Oui** |

**Les trois postes omis sont ceux qui rendent visible le coût de ne pas faire.** Ils apparaissent ailleurs dans les budgets — production, projets, exploitation — et jamais dans la ligne « sécurité », ce qui fausse tous les arbitrages.

## 37.2 Construire un dossier d'investissement

**La structure qui fonctionne**, en quatre parties :

| Partie | Contenu |
|---|---|
| **1. Situation** | Où nous en sommes, avec les indicateurs de résultat et leur tendance |
| **2. Point de bascule** | À quelle date, sans décision, la situation se dégrade mécaniquement |
| **3. Trois options chiffrées** | Sur la durée complète, jamais sur la première année |
| **4. Recommandation** | Une option, avec son risque résiduel assumé |

**Les trois options doivent toujours inclure le statu quo**, chiffré (§12.5). Une direction n'arbitre pas ce qu'elle ne peut pas comparer, et l'absence de troisième option est la première cause de non-décision.

**Le calcul du coût de ne rien faire** comprend : le coût des compensations maintenues, le surcoût des interventions en urgence, le coût du support étendu, la charge d'astreinte, l'écart de prime d'assurance, et le risque résiduel exprimé en termes métier — jours d'arrêt possibles, données concernées, conséquences contractuelles.

## 37.3 L'assurance cyber

Pour de nombreuses organisations, les questionnaires d'assurance constituent l'un des leviers les plus efficaces pour obtenir un arbitrage sur le MCS (§7.5) — souvent devant l'argument du risque.

**Ce qu'ils exigent typiquement**, et ce que ce cours vous permet de démontrer :

| Exigence du questionnaire | Chapitre correspondant |
|---|---|
| Processus documenté de gestion des correctifs | 7 |
| Délais de correction par criticité, et leur respect mesuré | 7, 38 |
| Inventaire des actifs | 10 |
| Part du parc hors support | 12 |
| Authentification multifacteur sur les accès distants | 24 |
| Sauvegardes testées et immuables | 34 |
| Gestion des accès à privilèges | 24 |
| Délai de détection et de réaction | 21 |

⚠️ **PIÈGE — la déclaration inexacte**
Répondre par l'affirmative à une exigence non tenue peut, en cas de sinistre, fonder un refus de garantie. La réponse honnête assortie d'un plan daté est préférable à une réponse flatteuse — et, en pratique, mieux reçue par les assureurs qu'on ne le croit.

## 37.4 Dimensionner l'équipe

**La méthode par la capacité**, seule fiable, en quatre étapes (§16.5) :

```
1. Mesurer le volume mensuel réel par catégorie de traitement
2. Mesurer le temps réel par unité — pas le temps théorique
3. Calculer la charge, en incluant la preuve et le suivi
4. Confronter à la capacité disponible, en déduisant l'incompressible
```


**Les quatre postes de charge incompressible**, systématiquement sous-estimés : les réunions et le reporting, les urgences non planifiées, la relance des propriétaires, et le traitement de la traîne longue (§18.10).

**Les seuils de rupture à connaître** :

| Signal | Ce qu'il indique |
|---|---|
| Le *backlog* grossit malgré une activité constante | Capacité structurellement insuffisante (§17.10) |
| La part de changements d'urgence dépasse 15-20 % | Le processus normal ne fonctionne pas (§5.1) |
| Les vérifications post-déploiement sont abandonnées | Premier symptôme de surcharge — et le plus coûteux |
| La preuve n'est plus produite | Second symptôme : le pilotage devient impossible |

**Cet ordre s'observe fréquemment** : sous pression, une équipe abandonne souvent d'abord la vérification, puis la preuve, puis la qualification. Elle continue à déployer — l'activité visible — tout en perdant la capacité de démontrer quoi que ce soit. C'est le signal à surveiller.

## 37.5 Astreintes, nuits et week-ends

Le MCS consomme du temps hors horaires : fenêtres nocturnes, interventions de week-end, astreintes de crise.

| Point | Traitement |
|---|---|
| **Prévisibilité** | Fenêtres récurrentes plutôt qu'interventions négociées (§5.2) |
| **Rotation** | Jamais les mêmes personnes ; une astreinte concentrée sur deux personnes est une dépendance critique |
| **Compensation** | Récupération effective, pas théorique |
| **Réduction du besoin** | Redondance, correction à chaud, déploiement progressif (ch. 6) — c'est l'argument économique du §6.13 |

**Le point rarement fait explicitement** : investir dans l'architecture réduit le travail de nuit. C'est un argument qui parle aux équipes et à la direction des ressources humaines autant qu'à la direction financière.

## 37.6 La fatigue de la vulnérabilité

**Le mécanisme.** Une file qui ne se vide jamais, des constats en volume ininterrompu, et l'impression que l'effort ne produit aucun résultat visible. C'est une cause de démotivation documentée, et elle est **structurelle**, pas individuelle.

| Cause structurelle | Remède |
|---|---|
| File infinie | Priorisation qui **exclut** explicitement (§16.3), et campagnes plutôt que constats (§16.7) |
| Absence de résultat visible | Indicateurs de résultat, tendance sur plusieurs trimestres (§38.1) |
| Travail invisible des autres | Communication interne sur ce qui a été évité |
| Responsabilité sans autorité | Le RACI du §9.2 |
| Constats non traités qui s'accumulent | Qualification systématique : dérogation ou dépriorisation, jamais l'oubli (§17.10) |

**Le remède le plus efficace, et le moins coûteux** : mesurer et montrer les **actifs ramenés à un état de référence** plutôt que les vulnérabilités fermées (§16.7). La première mesure progresse et se voit ; la seconde donne l'impression de vider la mer.

## 37.7 Compétences et transmission

| Risque | Traitement |
|---|---|
| Dépendance à une personne clé | Suppléance nommée sur chaque rôle (§14.8) |
| Savoir non documenté | Procédures d'exploitation à jour, testées par une autre personne |
| Perte au départ | Passation formalisée, avec période de recouvrement |
| Outils maîtrisés par une seule personne | Formation croisée, documentation d'administration |

**Le test qui révèle la dépendance** : une personne est absente trois semaines. Que devient le processus ? Si la réponse est « il s'arrête », vous avez une dépendance critique, pas une équipe.

## 37.8 Communiquer vers les métiers

| Situation | Ce qui fonctionne |
|---|---|
| Annoncer une interruption | Préavis, créneau, durée, ce qui se passe si on ne le fait pas |
| Gérer un refus | Qualifier le motif (§20.1), proposer une alternative, formaliser si le refus persiste |
| Après un incident évité | Le dire — c'est la seule occasion où le travail devient visible |
| Demander un budget | Termes métier, options chiffrées, jamais le vocabulaire technique |

🏢 **VU EN RÉUNION** — Présentation d'un plan de sortie d'obsolescence au comité de direction. Le RSSI ouvre sur le nombre de vulnérabilités critiques. Au bout de quatre minutes, le directeur financier interrompt : « combien ça coûte, et qu'est-ce qui se passe si on ne le fait pas ? ». Ces deux questions figuraient en diapositive onze. Depuis, elles sont en diapositive deux.

⚠️ **PIÈGE — la communication par la peur**
Elle fonctionne une fois. À la deuxième, elle produit de la lassitude ; à la troisième, du discrédit. La communication qui tient dans la durée est factuelle, chiffrée, et propose des options.

## 37.9 🔴 FIL ROUGE — septembre 2028 : 62 heures par mois

Lors de l'entretien annuel, Malik Ferhaoui expose à Sonia Weber une mesure qu'il tient depuis six mois : **62 heures par mois** consacrées au MCS, sur un temps de travail théorique de 151 heures. Soit 41 % de son temps, pour une mission qui n'est pas dans sa fiche de poste.

**La décomposition qu'il présente.**

| Activité | Heures/mois |
|---|---|
| Qualification et triage des constats | 12 |
| Planification et coordination des campagnes | 14 |
| Exécution — dont 9 h hors horaires ouvrés | 18 |
| Vérification et production de preuve | 8 |
| Relance des propriétaires d'actifs | **7** |
| Comité, reporting, documentation | 3 |

**La ligne qui déclenche la discussion** est la cinquième : sept heures par mois passées à relancer des personnes qui ne répondent pas. Ce n'est pas du travail technique, c'est le symptôme d'un défaut de gouvernance — les propriétaires sont nommés (§5.5), mais l'affectation d'un ticket ne les engage à rien tant qu'aucun délai de contestation ni aucune escalade automatique n'existe (§17.4).

**Les quatre décisions, et leur effet mesuré trois mois plus tard.**

| Décision | Effet |
|---|---|
| Escalade automatique à J+5 sans réponse du propriétaire, vers son responsable | Relances : 7 h → **1 h** |
| Regroupement des campagnes de C3 en une seule fenêtre mensuelle | Planification : 14 h → 9 h |
| Automatisation de la vérification et de l'export de preuve (§36.1, rang 3) | Vérification : 8 h → 3 h |
| Recrutement d'un alternant en apprentissage sur le suivi et la preuve | Capacité ajoutée, et suppléance créée |

Total après trois mois : **62 h → 37 h**. Aucune de ces mesures n'a réduit le périmètre ni le niveau d'exigence.

**Ce que Sonia Weber retient**, et qu'elle porte au comité stratégique : le poste de charge le plus lourd n'était ni la technique ni le volume, c'était **l'absence de mécanisme d'engagement**. Sept heures mensuelles de relance représentaient, sur deux ans, l'équivalent de plus de vingt jours de travail consacrés à demander à des gens de répondre.

**Le point que Claire Nadeau ajoute.** Les 9 heures mensuelles hors horaires ouvrés ne diminuent pas : elles tiennent aux systèmes non interruptibles. Elles constituent la ligne d'argumentation du dossier d'investissement en redondance présenté au budget 2029 — l'application directe du §6.13, appuyée cette fois sur une mesure et non sur un principe.

**Livrable de l'épisode.** La mesure de charge par activité, reconduite trimestriellement, et l'escalade automatique intégrée au workflow de remédiation (Annexe J).

→ La suite en 🔴 §38.9, quand le directeur financier posera une question sur les indicateurs.

→ **Chapitre 38 — Indicateurs, tableaux de bord et maturité** : mesurer sans produire de chiffres faux.

## Synthèse mentale du chapitre 37

Trois postes de coût du MCS sont presque toujours omis — interruption, test, compensations — et ce sont précisément ceux qui rendent visible le coût de ne rien faire, parce qu'ils apparaissent dans d'autres budgets. Un dossier d'investissement présente toujours trois options chiffrées sur la durée complète, dont le statu quo : son absence est la première cause de non-décision. Les questionnaires d'assurance sont devenus le premier levier réel du MCS, et une réponse honnête assortie d'un plan daté vaut mieux qu'une réponse flatteuse qui peut fonder un refus de garantie. Sous surcharge, une équipe abandonne dans un ordre constant : d'abord la vérification, puis la preuve, puis la qualification — elle continue à déployer tout en perdant la capacité de démontrer quoi que ce soit. La fatigue de la vulnérabilité est structurelle, et son remède le moins coûteux consiste à mesurer les actifs ramenés à un état de référence plutôt que les vulnérabilités fermées. Enfin, le poste de charge le plus lourd est souvent l'absence de mécanisme d'engagement : la relance manuelle se remplace par une escalade automatique.

**Trois questions de vérification**

1. Votre direction estime que le MCS coûte cher. Quels trois postes de coût lui manquent probablement, et où apparaissent-ils actuellement ?
2. Votre équipe déploie toujours autant de correctifs mais ne produit plus de preuve. Que se passe-t-il, et quel symptôme l'a précédé ?
3. Une personne passe sept heures par mois à relancer des propriétaires d'actifs. Est-ce un problème de charge ou de gouvernance, et que corrigez-vous ?

---
