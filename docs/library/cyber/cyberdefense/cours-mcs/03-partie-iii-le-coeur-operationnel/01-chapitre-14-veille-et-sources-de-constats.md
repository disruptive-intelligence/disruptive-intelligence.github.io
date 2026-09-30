---
title: Chapitre 14 — Veille et sources de constats
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

## 14.1 Cartographier ses besoins de veille à partir de l'inventaire

L'erreur de départ la plus commune consiste à s'abonner d'abord à des sources, puis à chercher ce qui, dans le flux reçu, pourrait concerner l'organisation. Le résultat est prévisible : un volume ingérable, une fatigue rapide, et paradoxalement des angles morts — parce que les sources choisies reflètent ce qu'on connaît déjà.

**La démarche inverse.** Partez de l'inventaire (chapitre 10), extrayez la liste des **technologies distinctes** présentes dans votre parc, et construisez la veille à partir de cette liste.

🧪 **EN PRATIQUE — la matrice de couverture de veille**

| Technologie présente | Nb d'actifs | Criticité max | Source de veille | Canal | Vérifié le |
|---|---|---|---|---|---|
| Système serveur A | 118 | C1 | Avis officiel éditeur | Flux + courriel | 30/07/2026 |
| Pare-feu constructeur B | 6 | C1 | Portail sécurité constructeur | Compte à créer | — |
| Progiciel métier C | 1 | C1 | **Aucune source identifiée** | — | — |
| Automate D | 12 | C4 | Bulletin constructeur, publication irrégulière | Courriel | 30/07/2026 |

**Ce que cette matrice révèle immédiatement**, et qui justifie à elle seule l'exercice : les lignes sans source. Elles correspondent presque toujours à des progiciels métier, des équipements industriels et des services en ligne — c'est-à-dire souvent des actifs critiques. Un flux de veille abondant sur les systèmes d'exploitation ne compense en rien ces trous ; il les masque en donnant le sentiment d'être informé.

✅ **BONNE PRATIQUE (P0)** — Construisez cette matrice avant de vous abonner à quoi que ce soit. Elle tient sur deux pages pour un parc de taille intermédiaire, et elle transforme la veille d'un flux subi en une couverture mesurable — avec un indicateur associé : *part des technologies du parc couvertes par au moins une source identifiée*.

## 14.2 Le MCS n'est pas la gestion des CVE

C'est l'un des points les plus importants de tout le cours, et il découle directement du §1.3 : dix objets se dégradent, et les vulnérabilités logicielles n'en sont qu'un.

**La typologie complète des constats** qui doivent entrer dans votre chaîne de traitement :

| Origine | Exemple de constat | A-t-il un identifiant de vulnérabilité ? |
|---|---|---|
| Avis d'éditeur | Correctif de sécurité publié | Souvent, pas toujours |
| Bulletin d'un centre de réponse aux incidents | Alerte sur une exploitation en cours | Généralement |
| **Test d'intrusion** | Interface d'administration sans authentification | **Non** |
| **Audit de configuration** | Écart à la baseline sur 40 serveurs | **Non** |
| **Programme de récompense / divulgation** | Faille signalée par un chercheur externe | Pas encore |
| **Incident** | Compte compromis, chemin d'entrée identifié | **Non** |
| **Recherche de menace proactive** | Persistance découverte sur un poste | **Non** |
| **Mauvaise configuration cloud** | Stockage ouvert publiquement | **Non** |
| **Secret exposé** | Clé d'accès trouvée dans un dépôt de code | **Non** |
| **Chemin d'attaque** | Compte de service surprivilégié (ch. 11) | **Non** |
| **Revue d'architecture** | Système non interruptible (ch. 6) | **Non** |
| **Obsolescence** | Composant hors support | **Non** |
| **Contenu de détection périmé** | Agents sans mise à jour depuis 21 jours | **Non** |
| Vulnérabilité matérielle | Faille de processeur ou de micrologiciel | Parfois |

⚠️ **PIÈGE — l'organisation qui ne traite que ce qui a un identifiant**
Le symptôme est facile à repérer : le processus de remédiation est branché sur le scanner de vulnérabilités, et sur lui seul. Les rapports de test d'intrusion finissent dans un dossier partagé, les écarts de configuration dans un tableur, les constats d'audit dans un plan d'action distinct. Résultat : plusieurs files de traitement parallèles, des priorités incomparables entre elles, et un constat majeur — l'interface d'administration exposée du mini-lab 1 — qui progresse moins vite qu'une vulnérabilité mineure de bibliothèque, uniquement parce qu'elle est arrivée par le mauvais canal.

✅ **BONNE PRATIQUE (P0) — la file unique**
Tous les constats, quelle que soit leur origine, entrent dans **la même file de traitement**, avec la même méthode de priorisation (chapitre 16) et le même cycle de vie (chapitre 17). C'est la décision d'organisation qui produit le plus d'effet dans tout ce cours, et elle ne coûte rien d'autre qu'une décision.

## 14.3 Les sources primaires

Une source primaire est celle qui produit l'information d'origine. Elle fait foi.

| Source | Ce qu'elle apporte | Précaution |
|---|---|---|
| **Avis de sécurité de l'éditeur du produit** | La vérité sur les versions affectées et corrigées | C'est **la** source de vérité sur « suis-je vulnérable » (§2.2) |
| **Avis de sécurité de votre distribution** | L'état du paquet chez elle, correctifs rétroportés inclus | Indispensable sur les systèmes à support long |
| **Bulletins des centres de réponse nationaux** | Contexte, criticité, exploitation observée, recommandations | Généralement le meilleur point d'entrée quotidien |
| **Listes de diffusion sécurité des projets** | Information brute, souvent la plus rapide | Volume élevé, peu de mise en forme |
| **Avis lisibles par machine** | Automatisation du rapprochement (§4.8) | Adoption inégale selon les éditeurs |

✅ **BONNE PRATIQUE (P1)** — Pour chaque produit de classe C1 de votre parc, identifiez et **testez** le canal officiel de notification de l'éditeur. Beaucoup d'organisations découvrent au premier incident que l'adresse de contact enregistrée chez le fournisseur est celle d'un administrateur parti depuis trois ans. Vérifiez que vous recevez réellement, et faites-le figurer dans la matrice du §14.1.

## 14.4 Les sources agrégées, et pourquoi la redondance est devenue nécessaire

Les bases agrégées collectent, dédoublonnent et enrichissent l'information issue des sources primaires. Elles apportent la couverture et l'exploitabilité automatique ; elles ajoutent une latence et un risque de dépendance.

**Ce qui a changé** (§4.9) : l'écosystème s'est fragmenté, l'enrichissement d'une base majeure est devenu sélectif, une base européenne est montée en charge, et d'autres initiatives d'identification existent. Une architecture de veille qui reposait sur une source unique enrichie ne fonctionne plus telle quelle.

**L'architecture de veille recommandée**, en trois étages complémentaires :

```
Étage 1 — Vérité produit     : avis de l'éditeur et de la distribution
                               → répond à « suis-je affecté, et quelle version corrige ? »
Étage 2 — Couverture          : base agrégée, quelle qu'elle soit
                               → répond à « qu'est-ce qui existe, sans rien manquer ? »
Étage 3 — Signal d'exploitation : catalogue d'exploitation avérée + renseignement
                               → répond à « est-ce réellement utilisé par des attaquants ? »
```


Les trois étages répondent à trois questions différentes, et aucun ne remplace les autres. C'est cette structure, et non le choix d'un fournisseur particulier, qui rend une veille robuste au changement.

## 14.5 Le renseignement sur la menace appliqué au MCS

Beaucoup d'organisations consomment du renseignement sur la menace sans savoir qu'en faire. Pour le MCS, son apport se ramène à trois usages précis, et il faut se limiter à ceux-là.

| Usage | Question à laquelle il répond | Effet concret |
|---|---|---|
| **Exploitation observée** | Cette vulnérabilité est-elle utilisée en ce moment ? | Entrée directe dans la priorisation (ch. 16) |
| **Ciblage sectoriel** | Des campagnes visent-elles mon secteur, avec quels vecteurs ? | Priorise les technologies visées, avant l'entrée dans un catalogue public |
| **Comportement des attaquants** | Quels chemins empruntent-ils ? | Oriente la cartographie des chemins d'attaque (ch. 11) |

**Les sources sectorielles** — centres de réponse sectoriels, communautés de partage entre pairs, groupements professionnels — sont particulièrement utiles ici, parce qu'elles voient ce qui vise **votre** secteur avant que cela n'apparaisse dans les catalogues généralistes. C'est la seule réponse partielle à la limite structurelle du §4.6 : un catalogue public est en retard sur les campagnes ciblées.

📌 **LIMITES** — Le renseignement sur la menace ne dit rien de votre exposition, se prête mal à l'automatisation directe, et son coût peut être élevé pour une valeur ajoutée faible si l'organisation n'a pas d'abord traité l'inventaire et l'exposition. **Ne l'achetez pas avant d'avoir fait les chapitres 10 et 11.**

## 14.6 Automatiser la veille

L'automatisation consiste à rapprocher automatiquement les avis reçus et l'inventaire, pour ne présenter à un humain que ce qui concerne réellement le parc.

**La chaîne type :**

```
Avis reçus (flux, courriels, formats structurés)
   → normalisation (identifiant, produit, versions affectées, versions corrigées)
   → rapprochement avec l'inventaire enrichi (ch. 10)
   → filtrage : ne concerne aucun actif → archivé, pas supprimé
   → constats candidats → file unique de traitement (ch. 17)
```


⚠️ **PIÈGE — les quatre défaillances du rapprochement automatique**

| Défaillance | Effet | Atténuation |
|---|---|---|
| Nom de produit divergent entre l'avis et l'inventaire | Faux négatif : l'avis vous concerne, vous ne le voyez pas | Table de correspondance maintenue, revue périodique |
| Intervalle de versions imprécis dans l'avis | Faux positif ou faux négatif | Confirmation par l'avis éditeur |
| Rétroportage (§2.2) | Faux positif massif | Comparer la révision éditeur, pas la version amont |
| Composant embarqué non déclaré dans l'inventaire | Faux négatif silencieux | Inventaire de composants (ch. 25) |

**Le faux négatif est le vrai danger.** Un faux positif coûte du temps ; un faux négatif produit une exposition dont personne n'a connaissance. C'est pourquoi la règle est d'**archiver** ce qui est écarté automatiquement plutôt que de le supprimer : le jour où un avis écarté à tort refait surface, vous pouvez comprendre pourquoi il a été manqué et corriger la règle.

## 14.7 Qualifier une alerte : fait, hypothèse, piste

Une discipline de langage qui évite beaucoup d'erreurs de décision, et qui sera reprise dans tout le cours.

| Statut | Définition | Ce qu'on peut en faire |
|---|---|---|
| **Fait vérifié** | Constaté directement, ou établi par une source de vérité | Fonder une décision engageante |
| **Hypothèse probable** | Cohérent avec plusieurs indices, non confirmé | Déclencher une vérification, préparer une action |
| **Piste exploratoire** | Possible, non étayé | Investiguer, ne rien décider |

**L'exemple type.** Un scanner remonte une vulnérabilité sur 42 serveurs. Statut réel : **piste exploratoire**, tant que la révision du paquet n'est pas vérifiée (§2.2). Après vérification sur trois machines représentatives : **hypothèse probable** pour les 39 autres. Après vérification exhaustive ou confirmation par l'avis de la distribution : **fait vérifié**.

✅ **BONNE PRATIQUE (P1)** — Faites figurer ce statut dans chaque communication interne, et particulièrement dans les remontées à la direction. « Nous avons 1 176 vulnérabilités critiques » est une affirmation non qualifiée ; « nous avons 1 176 constats candidats, dont 31 confirmés comme activement exploités et 7 sur des actifs exposés » est une information sur laquelle on peut décider. La différence de crédibilité est considérable, et elle se construit une fois.

## 14.8 La cadence humaine

Une chaîne de veille automatisée ne dispense pas d'un dispositif humain. Trois questions doivent avoir une réponse écrite.

| Question | Réponse type |
|---|---|
| **Qui lit quoi, et quand ?** | Un rôle nommé, une plage horaire, une liste de sources — pas « l'équipe sécurité » |
| **Quel est le délai maximal de prise en compte ?** | Par exemple : 4 h ouvrées pour une alerte d'exploitation active, 24 h pour le reste |
| **Que se passe-t-il en dehors des heures ouvrées, en congés, en arrêt ?** | Suppléance nommée, ou acceptation explicite du délai |

⚠️ **PIÈGE — la veille reposant sur une personne**
Configuration extrêmement courante : une personne, passionnée, suit tout, et le dispositif fonctionne remarquablement — jusqu'à son départ, son arrêt maladie ou ses congés d'août. Deux mesures suffisent : une **suppléance nommée** et une **procédure écrite d'une page** décrivant les sources, les accès et le critère de déclenchement. Les crises de vulnérabilité majeures des dernières années se sont produites, statistiquement, aussi souvent en août et fin décembre qu'en mars.

## 14.9 📌 Limites de la veille

- **Le délai structurel.** Entre l'exploitation réelle et sa publication, il s'écoule un temps incompressible. Une veille parfaite est en retard sur les attaquants, par construction.
- **Les vulnérabilités sans identifiant.** Corrigées silencieusement par un éditeur, elles n'apparaissent dans aucune base. C'est un argument fort pour appliquer les correctifs même sans avis, et pour suivre les notes de version.
- **Les avis inexacts.** Versions affectées incomplètes, correctifs annoncés mais non publiés, avis révisés après coup. La vérification vaut mieux que la confiance.
- **La surcharge.** Une veille trop large produit une fatigue qui dégrade la qualité de traitement de ce qui compte. Mieux vaut couvrir complètement les actifs C1 que partiellement tout le parc.

## 14.10 🔬 Mini-lab 3 — Qualifier un bulletin éditeur ambigu

**Objectif** — Décider avec une information incomplète, et distinguer ce qui se fait le soir même de ce qui attend.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §14.7, §16.4 · **Livrable** décision argumentée + demande écrite au fournisseur.
**Compétences validées** — ✔ décider avec une information incomplète ✔ identifier l'information manquante déterminante ✔ formuler une demande fournisseur traçable ✔ poser une décision par défaut

**Énoncé.** Vous recevez, un vendredi à 17 h 40, le bulletin suivant d'un éditeur d'un progiciel métier utilisé par votre service comptable :

> *« Une vulnérabilité de sécurité importante a été identifiée dans notre plateforme. Nous recommandons à tous nos clients d'appliquer la mise à jour 8.4.2 dès que possible. Cette mise à jour corrige plusieurs problèmes de sécurité et de stabilité. Contactez votre référent en cas de question. »*

Aucun identifiant de vulnérabilité. Aucune version affectée précisée. Aucun vecteur d'accès. Vous êtes en version 8.3.7. Le progiciel est accessible depuis le réseau interne uniquement, utilisé par onze personnes, et traite des données de paie.

**Questions.** (a) Quel est le statut de ce constat ? (b) Quelles informations manquent, et par quel moyen les obtenir ? (c) Que faites-vous ce vendredi soir ? (d) Quelle est la décision par défaut si vous n'obtenez aucune réponse avant lundi ?

**Corrigé commenté**

**(a) Statut : hypothèse probable.** Le fait qu'un correctif de sécurité existe est vérifié — l'éditeur le dit. Que vous soyez affecté est probable, puisque votre version est antérieure, mais non confirmé faute de liste de versions affectées. La gravité réelle est une piste exploratoire : « importante » est un qualificatif commercial, pas une évaluation.

**(b) Cinq informations manquantes, et comment les obtenir :**

| Information | Moyen |
|---|---|
| Versions affectées, dont la 8.3.7 | Appel ou courriel au support, avec demande de réponse écrite |
| Vecteur d'accès : distant ou local, authentifié ou non | Même canal. C'est l'information la plus déterminante |
| Exploitation observée | Support, et vérification dans les sources d'exploitation avérée |
| Prérequis de la mise à jour, régressions connues | Notes de version, forum client |
| Existence d'une mesure de contournement | Support |

Le vecteur d'accès est celui qui change tout : une faille exploitable sans authentification depuis le réseau interne, sur une application traitant des données de paie, n'est pas du même ordre qu'une élévation de privilèges nécessitant un compte local.

**(c) Ce que vous faites vendredi soir — trois actions, vingt minutes :**

1. Enregistrer le constat dans la file unique, avec son statut, ce qui est connu et ce qui manque. Il existe désormais et ne dépend plus de votre mémoire.
2. Envoyer la demande écrite au support, avec les cinq questions. L'horodatage compte : il documente votre diligence.
3. Vérifier l'exposition réelle de l'application — qui peut l'atteindre, avec quels comptes. Cette vérification ne dépend d'aucune réponse de l'éditeur, et elle est souvent la plus informative.

Ce que vous ne faites **pas** : déployer la 8.4.2 en urgence un vendredi soir sur une application de paie, sans test ni fenêtre, sur la base d'un bulletin non qualifié. Le risque de régression est ici probablement supérieur au risque de la vulnérabilité — et cette comparaison est exactement le sujet du cas de synthèse C.

**(d) La décision par défaut, sans réponse avant lundi.** Traiter comme un constat de criticité moyenne sur un actif interne peu exposé : planification de la mise à jour dans la fenêtre normale suivante, avec test préalable. **Et** documenter que l'éditeur n'a pas répondu — c'est un élément d'évaluation fournisseur (§13.6), et un argument pour la prochaine renégociation.

**Les deux erreurs attendues.** Ne rien faire au motif que le bulletin est trop vague — le constat disparaît alors dans une boîte de réception. Ou déployer immédiatement en urgence — en transformant un risque incertain en indisponibilité certaine.

## 14.11 🔴 FIL ROUGE — décembre 2026 : la matrice de couverture de veille

Claire Nadeau applique la matrice du §14.1 au périmètre élargi d'HELIOMED — parc interne, périmètre infogéré désormais mesurable (§13.9), usine, services en ligne et produits.

**Le résultat, en une page.**

| Domaine | Technologies distinctes | Couvertes par une source | Taux |
|---|---|---|---|
| Systèmes et bureautique | 14 | 14 | 100 % |
| Réseau et sécurité | 6 | 6 | 100 % |
| Bases de données et environnements d'exécution | 9 | 5 | 56 % |
| **Progiciels métier** | **7** | **2** | **29 %** |
| **Systèmes industriels (Saint-Étienne)** | **8** | **1** | **13 %** |
| Services en ligne | 38 | 4 | 11 % |
| Composants embarqués dans les produits HELIOMED | inconnu | — | **non mesuré** |

**Ce que le tableau démontre.** La veille d'HELIOMED était excellente là où elle était facile, et quasi inexistante là où les actifs sont les plus critiques. L'usine, dont les postes de supervision pilotent une ligne de production de dispositifs médicaux, était couverte à 13 %.

**Trois décisions prises.**

1. **Progiciels métier** : une clause de notification de vulnérabilité est ajoutée à chaque renouvellement de contrat de maintenance, en reprenant la clause 4 du §13.3. Cinq contrats sont concernés en 2027.
2. **Systèmes industriels** : Thomas Berger obtient un accès nominatif au portail sécurité de deux constructeurs — accès qui existait depuis toujours, sans que personne n'ait fait la demande. Pour les trois automates dont le fournisseur a disparu, la couverture est déclarée **impossible**, et la compensation est portée au chapitre 29.
3. **Services en ligne** : la veille éditeur n'est pas mise en place pour les 38 abonnements — ce serait ingérable. Elle l'est pour les 4 traitant des données sensibles ou disposant d'un connecteur vers la messagerie. Les 34 autres sont couverts par une revue annuelle de configuration (chapitre 31).

**Ce que Claire ne fait pas**, et qu'elle explique au comité : chercher à atteindre 100 % partout. La matrice sert à choisir où investir, pas à produire un objectif de complétude. La ligne « composants embarqués : non mesuré » restera telle quelle jusqu'au chapitre 25.

**Livrable de l'épisode.** La matrice de couverture de veille, avec son indicateur associé — *part des technologies de classe C1 couvertes par au moins une source identifiée* — qui entre au tableau de bord du comité MCS.

→ La suite en 🔴 §15.13, quand le premier scan authentifié complet fera perdre trois semaines à l'équipe.

→ **Chapitre 15 — Détection technique de l'exposition** : savoir s'il vous concerne, et pourquoi les outils se trompent si souvent.

## Synthèse mentale du chapitre 14

La veille se construit à partir de l'inventaire, jamais l'inverse : la matrice de couverture révèle immédiatement les technologies sans source, qui sont presque toujours les progiciels métier, l'industriel et les services en ligne — c'est-à-dire des actifs critiques. Le MCS ne se réduit pas aux vulnérabilités identifiées : une quinzaine d'origines produisent des constats, dont la majorité n'a aucun identifiant, et la décision d'organisation la plus rentable du cours consiste à les faire toutes entrer dans une file unique avec la même priorisation. L'architecture de veille tient en trois étages complémentaires — vérité produit, couverture, signal d'exploitation — dont aucun ne remplace les autres. Dans le rapprochement automatique, le faux négatif est le vrai danger, d'où la règle d'archiver plutôt que supprimer ce qui est écarté. Qualifier chaque constat en fait vérifié, hypothèse probable ou piste exploratoire change radicalement la qualité des décisions et la crédibilité des remontées. Enfin, une veille reposant sur une seule personne fonctionne parfaitement jusqu'au mois d'août.

**Trois questions de vérification**

1. Votre flux de veille est abondant et vous êtes informé quotidiennement. Comment vérifiez-vous que cette abondance ne masque pas des angles morts, et par quel indicateur ?
2. Un rapport de test d'intrusion signale une interface d'administration exposée. Pourquoi ce constat progresse-t-il souvent moins vite qu'une vulnérabilité mineure de bibliothèque, et quelle décision d'organisation corrige cela ?
3. Vous recevez un bulletin sans identifiant, sans versions affectées et sans vecteur d'accès. Quelle est la seule information à obtenir en priorité, et pourquoi celle-là ?

---
