---
title: PARTIE III — Le cœur opérationnel
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 4
chapters: 10
---

Les deux premières parties ont construit le socle et le cadre. Celle-ci décrit la chaîne d'exécution, dans l'ordre où elle se déroule réellement : **savoir qu'il existe un problème** (ch. 14), **savoir s'il vous concerne** (ch. 15), **décider quoi traiter** (ch. 16), **piloter le traitement** (ch. 17), **corriger** (ch. 18 et 19), **faire quand on ne peut pas corriger** (ch. 20), et **réagir quand tout s'accélère** (ch. 21).

C'est la partie la plus dense du cours, et celle à laquelle vous reviendrez le plus souvent.

---

## Chapitre 14 — Veille et sources de constats

### 14.1 Cartographier ses besoins de veille à partir de l'inventaire

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

### 14.2 Le MCS n'est pas la gestion des CVE

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

### 14.3 Les sources primaires

Une source primaire est celle qui produit l'information d'origine. Elle fait foi.

| Source | Ce qu'elle apporte | Précaution |
|---|---|---|
| **Avis de sécurité de l'éditeur du produit** | La vérité sur les versions affectées et corrigées | C'est **la** source de vérité sur « suis-je vulnérable » (§2.2) |
| **Avis de sécurité de votre distribution** | L'état du paquet chez elle, correctifs rétroportés inclus | Indispensable sur les systèmes à support long |
| **Bulletins des centres de réponse nationaux** | Contexte, criticité, exploitation observée, recommandations | Généralement le meilleur point d'entrée quotidien |
| **Listes de diffusion sécurité des projets** | Information brute, souvent la plus rapide | Volume élevé, peu de mise en forme |
| **Avis lisibles par machine** | Automatisation du rapprochement (§4.8) | Adoption inégale selon les éditeurs |

✅ **BONNE PRATIQUE (P1)** — Pour chaque produit de classe C1 de votre parc, identifiez et **testez** le canal officiel de notification de l'éditeur. Beaucoup d'organisations découvrent au premier incident que l'adresse de contact enregistrée chez le fournisseur est celle d'un administrateur parti depuis trois ans. Vérifiez que vous recevez réellement, et faites-le figurer dans la matrice du §14.1.

### 14.4 Les sources agrégées, et pourquoi la redondance est devenue nécessaire

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

### 14.5 Le renseignement sur la menace appliqué au MCS

Beaucoup d'organisations consomment du renseignement sur la menace sans savoir qu'en faire. Pour le MCS, son apport se ramène à trois usages précis, et il faut se limiter à ceux-là.

| Usage | Question à laquelle il répond | Effet concret |
|---|---|---|
| **Exploitation observée** | Cette vulnérabilité est-elle utilisée en ce moment ? | Entrée directe dans la priorisation (ch. 16) |
| **Ciblage sectoriel** | Des campagnes visent-elles mon secteur, avec quels vecteurs ? | Priorise les technologies visées, avant l'entrée dans un catalogue public |
| **Comportement des attaquants** | Quels chemins empruntent-ils ? | Oriente la cartographie des chemins d'attaque (ch. 11) |

**Les sources sectorielles** — centres de réponse sectoriels, communautés de partage entre pairs, groupements professionnels — sont particulièrement utiles ici, parce qu'elles voient ce qui vise **votre** secteur avant que cela n'apparaisse dans les catalogues généralistes. C'est la seule réponse partielle à la limite structurelle du §4.6 : un catalogue public est en retard sur les campagnes ciblées.

📌 **LIMITES** — Le renseignement sur la menace ne dit rien de votre exposition, se prête mal à l'automatisation directe, et son coût peut être élevé pour une valeur ajoutée faible si l'organisation n'a pas d'abord traité l'inventaire et l'exposition. **Ne l'achetez pas avant d'avoir fait les chapitres 10 et 11.**

### 14.6 Automatiser la veille

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

### 14.7 Qualifier une alerte : fait, hypothèse, piste

Une discipline de langage qui évite beaucoup d'erreurs de décision, et qui sera reprise dans tout le cours.

| Statut | Définition | Ce qu'on peut en faire |
|---|---|---|
| **Fait vérifié** | Constaté directement, ou établi par une source de vérité | Fonder une décision engageante |
| **Hypothèse probable** | Cohérent avec plusieurs indices, non confirmé | Déclencher une vérification, préparer une action |
| **Piste exploratoire** | Possible, non étayé | Investiguer, ne rien décider |

**L'exemple type.** Un scanner remonte une vulnérabilité sur 42 serveurs. Statut réel : **piste exploratoire**, tant que la révision du paquet n'est pas vérifiée (§2.2). Après vérification sur trois machines représentatives : **hypothèse probable** pour les 39 autres. Après vérification exhaustive ou confirmation par l'avis de la distribution : **fait vérifié**.

✅ **BONNE PRATIQUE (P1)** — Faites figurer ce statut dans chaque communication interne, et particulièrement dans les remontées à la direction. « Nous avons 1 176 vulnérabilités critiques » est une affirmation non qualifiée ; « nous avons 1 176 constats candidats, dont 31 confirmés comme activement exploités et 7 sur des actifs exposés » est une information sur laquelle on peut décider. La différence de crédibilité est considérable, et elle se construit une fois.

### 14.8 La cadence humaine

Une chaîne de veille automatisée ne dispense pas d'un dispositif humain. Trois questions doivent avoir une réponse écrite.

| Question | Réponse type |
|---|---|
| **Qui lit quoi, et quand ?** | Un rôle nommé, une plage horaire, une liste de sources — pas « l'équipe sécurité » |
| **Quel est le délai maximal de prise en compte ?** | Par exemple : 4 h ouvrées pour une alerte d'exploitation active, 24 h pour le reste |
| **Que se passe-t-il en dehors des heures ouvrées, en congés, en arrêt ?** | Suppléance nommée, ou acceptation explicite du délai |

⚠️ **PIÈGE — la veille reposant sur une personne**
Configuration extrêmement courante : une personne, passionnée, suit tout, et le dispositif fonctionne remarquablement — jusqu'à son départ, son arrêt maladie ou ses congés d'août. Deux mesures suffisent : une **suppléance nommée** et une **procédure écrite d'une page** décrivant les sources, les accès et le critère de déclenchement. Les crises de vulnérabilité majeures des dernières années se sont produites, statistiquement, aussi souvent en août et fin décembre qu'en mars.

### 14.9 📌 Limites de la veille

- **Le délai structurel.** Entre l'exploitation réelle et sa publication, il s'écoule un temps incompressible. Une veille parfaite est en retard sur les attaquants, par construction.
- **Les vulnérabilités sans identifiant.** Corrigées silencieusement par un éditeur, elles n'apparaissent dans aucune base. C'est un argument fort pour appliquer les correctifs même sans avis, et pour suivre les notes de version.
- **Les avis inexacts.** Versions affectées incomplètes, correctifs annoncés mais non publiés, avis révisés après coup. La vérification vaut mieux que la confiance.
- **La surcharge.** Une veille trop large produit une fatigue qui dégrade la qualité de traitement de ce qui compte. Mieux vaut couvrir complètement les actifs C1 que partiellement tout le parc.

### 14.10 🔬 Mini-lab 3 — Qualifier un bulletin éditeur ambigu

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

### 14.11 🔴 FIL ROUGE — décembre 2026 : la matrice de couverture de veille

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

### Synthèse mentale du chapitre 14

La veille se construit à partir de l'inventaire, jamais l'inverse : la matrice de couverture révèle immédiatement les technologies sans source, qui sont presque toujours les progiciels métier, l'industriel et les services en ligne — c'est-à-dire des actifs critiques. Le MCS ne se réduit pas aux vulnérabilités identifiées : une quinzaine d'origines produisent des constats, dont la majorité n'a aucun identifiant, et la décision d'organisation la plus rentable du cours consiste à les faire toutes entrer dans une file unique avec la même priorisation. L'architecture de veille tient en trois étages complémentaires — vérité produit, couverture, signal d'exploitation — dont aucun ne remplace les autres. Dans le rapprochement automatique, le faux négatif est le vrai danger, d'où la règle d'archiver plutôt que supprimer ce qui est écarté. Qualifier chaque constat en fait vérifié, hypothèse probable ou piste exploratoire change radicalement la qualité des décisions et la crédibilité des remontées. Enfin, une veille reposant sur une seule personne fonctionne parfaitement jusqu'au mois d'août.

**Trois questions de vérification**

1. Votre flux de veille est abondant et vous êtes informé quotidiennement. Comment vérifiez-vous que cette abondance ne masque pas des angles morts, et par quel indicateur ?
2. Un rapport de test d'intrusion signale une interface d'administration exposée. Pourquoi ce constat progresse-t-il souvent moins vite qu'une vulnérabilité mineure de bibliothèque, et quelle décision d'organisation corrige cela ?
3. Vous recevez un bulletin sans identifiant, sans versions affectées et sans vecteur d'accès. Quelle est la seule information à obtenir en priorité, et pourquoi celle-là ?

---

## Chapitre 15 — Détection technique de l'exposition

Le chapitre 14 vous informe qu'une vulnérabilité existe. Celui-ci répond à la question suivante : **est-elle présente chez moi, et où exactement ?** C'est le chapitre des outils — et surtout de ce qu'ils ne savent pas faire.

### 15.1 Les familles d'outils et ce que chacune peut savoir

| Famille | Principe | Ce qu'elle peut établir | Ce qu'elle ne peut pas |
|---|---|---|---|
| **Scan réseau non authentifié** | Interroge les services exposés depuis le réseau | Ce qui répond, bannières, comportements observables | L'état interne de la machine |
| **Scan authentifié** | Se connecte avec un compte et inventorie | Versions exactes, correctifs installés, configuration | Ce qui n'est pas accessible au compte utilisé |
| **Agent installé** | Programme résident qui remonte l'état en continu | État permanent, y compris hors réseau | L'état des machines sans agent |
| **Analyse de composition logicielle** | Lit les dépendances déclarées d'une application | Composants tiers et versions | L'atteignabilité réelle du code (§11.6) |
| **Analyse d'image de conteneur** | Inspecte les couches d'une image | Composants embarqués avant déploiement | Ce qui est ajouté à l'exécution |
| **Découverte externe** | Vue depuis Internet | La surface réellement publiée (ch. 11) | Tout l'interne |
| **Validation d'exploitabilité** | Tente une exploitation contrôlée | La démonstration qu'un chemin fonctionne | Le reste du parc, et le risque de l'essai |

**Le principe de complémentarité, à retenir.** Ces familles ne se substituent pas. Un agent ne dit rien de l'exposition réseau ; un scan externe ne dit rien de l'état interne ; une analyse de composition ne voit pas ce que le système d'exploitation embarque. Une organisation qui n'utilise qu'une famille a nécessairement un angle mort structurel, et il est prévisible.

### 15.2 Ce qu'un scan non authentifié ne peut pas savoir

Le scan non authentifié observe un système de l'extérieur, sans identifiants. Il en déduit des informations à partir de ce que les services exposés laissent voir.

**Sa méthode d'inférence, et sa fragilité.** Il lit une bannière annonçant une version, observe un comportement caractéristique, teste une réponse. Puis il conclut à partir d'une base de correspondance version ↔ vulnérabilité.

**Les quatre sources de faux positifs structurels** :

| Cause | Mécanisme |
|---|---|
| **Rétroportage** | La bannière annonce une version amont ancienne, le correctif est présent (§2.2). C'est la première cause, et de loin |
| **Bannière modifiée** | Certaines configurations masquent ou falsifient la version annoncée |
| **Composant présent mais désactivé** | Le module vulnérable est installé, non chargé |
| **Correspondance approximative** | Le produit détecté n'est pas exactement celui de la base (§4.3) |

**Ce qu'il détecte que rien d'autre ne détecte**, et qui justifie son usage malgré tout : ce qui est **réellement joignable**. Un scan authentifié vous dira qu'un service est installé ; seul un scan non authentifié depuis un point donné du réseau vous dira qu'il répond depuis cet endroit. C'est une information d'exposition (chapitre 11), pas de vulnérabilité — et c'est sa vraie valeur.

### 15.3 Le scan authentifié, et la protection de ses secrets

Le scan authentifié se connecte à la machine avec un compte et lit directement l'état du système : paquets installés, révisions, correctifs, configuration. Il est **incomparablement plus fiable** et devrait constituer le mode par défaut sur tout le parc que vous administrez.

**Le compte de scan est un actif de niveau 0.** Il dispose d'un accès en lecture privilégié sur l'ensemble du parc, et ses identifiants sont stockés dans l'outil de scan. Quiconque compromet cet outil obtient un accès à tout le périmètre scanné.

✅ **BONNE PRATIQUE (P0) — les six règles du compte de scan**

1. Un compte **dédié**, jamais un compte d'administration existant réutilisé.
2. Les **privilèges minimaux** nécessaires à la lecture — pas d'administration complète quand la lecture suffit.
3. **Interdiction d'ouverture de session interactive** pour ce compte.
4. **Rotation** régulière du secret, et vérification que la rotation est bien répercutée dans l'outil (§24.10).
5. **Surveillance** de son usage : toute utilisation en dehors des fenêtres de scan est une alerte.
6. **Cloisonnement** : idéalement, un compte distinct par zone de sécurité, pour qu'une compromission ne donne pas tout le parc.

### 15.4 La sécurité de l'outil lui-même

Prolongement direct du point précédent, et l'un des angles morts les plus fréquents.

Un outil de scan de vulnérabilités concentre : les identifiants privilégiés du §15.3, la **cartographie complète** de vos faiblesses, et souvent une capacité d'exécution à distance. C'est un actif de niveau 0 au sens du §11.7, et il est fréquemment traité comme un outil secondaire — installé une fois, rarement mis à jour, avec une interface d'administration accessible largement.

⚠️ **PIÈGE — la console de sécurité oubliée**
Le raisonnement implicite est toujours le même : « c'est un outil de sécurité, donc il est sécurisé ». Il n'y a aucun lien logique entre les deux. Les outils de sécurité — scanners, consoles de protection des postes, plateformes de journalisation, consoles de sauvegarde — figurent régulièrement parmi les composants les plus en retard d'un parc. Le chapitre 34 leur est consacré.

### 15.5 La fraîcheur de la base de détection

Un scanner ne détecte que ce qu'il sait détecter. Entre la publication d'un avis et la disponibilité du contrôle correspondant dans votre outil, il s'écoule un délai.

**Trois délais s'additionnent**, et c'est leur somme qui compte :

```
Publication de l'avis
   → l'éditeur de l'outil développe le contrôle          (heures à jours)
   → il le publie dans sa base                            (selon son rythme)
   → vous mettez à jour votre instance                    (selon VOTRE processus)
   → le prochain scan passe                               (selon votre cadence)
```

Le troisième délai est le seul que vous contrôlez entièrement, et c'est souvent le plus long. Une instance dont la base de détection date de trois semaines ne détectera aucune des vulnérabilités publiées depuis.

✅ **BONNE PRATIQUE (P0)** — Suivez la fraîcheur de la base de détection comme un indicateur à part entière, et rendez sa mise à jour automatique. C'est exactement le sujet du §1.3, ligne « contenu de détection » : votre outil de détection est lui-même un objet qui se dégrade quotidiennement.

⚠️ Pour toute vulnérabilité en crise (chapitre 21), **ne présumez jamais** que votre scanner la détecte. Vérifiez que le contrôle existe dans votre base, à sa version installée. Sinon, la vérification se fait autrement : requête sur l'inventaire par version, ou vérification directe sur un échantillon.

### 15.6 La couverture réelle : la calculer et la prouver

Le §10.11 a posé le principe ; voici la mise en œuvre.

**La formule**, qui suppose le périmètre de référence du chapitre 10 :

```
Couverture de scan = actifs scannés avec succès / actifs du périmètre de référence
```

**Les cinq populations à distinguer**, parce que les confondre produit la totalité des malentendus sur ce chiffre :

| Population | Signification | Traitement |
|---|---|---|
| Scannés avec succès, authentifiés | Donnée fiable | Base des indicateurs |
| Scannés, mais authentification échouée | Donnée dégradée, faux positifs probables | À corriger en priorité : compte, droits, filtrage |
| Non joignables au moment du scan | Éteints, nomades, intermittents | **À lister explicitement**, jamais à ignorer |
| Exclus volontairement | Systèmes industriels, actifs fragiles | Exclusion **documentée**, avec son motif et sa compensation |
| Hors périmètre de l'outil | Cloud, services en ligne, produits | Couverts par un autre moyen, ou déclarés non couverts |

⚠️ **PIÈGE — l'exclusion silencieuse**
Le mécanisme le plus insidieux de tout ce chapitre. Un actif provoque des dysfonctionnements pendant un scan ; on l'exclut « temporairement » ; l'exclusion n'est jamais revue. Deux ans plus tard, il ne figure plus dans aucun rapport — et comme il ne remonte aucune vulnérabilité, il améliore même les indicateurs.
**Le garde-fou** : la liste des exclusions est un document de gouvernance, revu au comité MCS, avec pour chacune un motif, un propriétaire, une compensation et une date de revue. Une exclusion sans date de revue est une dérogation déguisée qui échappe au processus du §7.4.

### 15.7 Identifiants d'actifs, historique et continuité

Un problème banal qui détruit silencieusement toute capacité de mesure dans la durée.

Les outils identifient les actifs par une clé interne, construite à partir du nom, de l'adresse, d'un identifiant matériel ou d'une combinaison. Quand cette clé change — machine renommée, redéploiement, changement d'adresse, réinstallation d'agent — l'outil crée un **nouvel actif** et perd l'historique de l'ancien.

**Les conséquences concrètes :**

- l'ancienneté d'un constat est réinitialisée, ce qui embellit artificiellement l'indicateur d'âge du *backlog* ;
- le nombre d'actifs augmente sans que le parc change, faussant tous les dénominateurs ;
- l'ancien actif reste dans l'outil, sans être scanné, et finit par disparaître des rapports ;
- une vulnérabilité récurrente (§17.9) apparaît comme nouvelle à chaque redéploiement.

✅ **BONNE PRATIQUE (P1)** — Définissez une règle d'identification stable, réconciliée avec l'inventaire du chapitre 10, et suivez deux indicateurs simples : le nombre d'actifs créés et supprimés dans l'outil par mois, et le nombre d'actifs présents dans l'outil mais absents du périmètre de référence. Une variation anormale de l'un ou de l'autre signale un problème d'identification, pas un changement de parc.

### 15.8 ⚠️ « Non détecté », « non vulnérable », « non scanné »

C'est la distinction la plus coûteuse du domaine quand elle n'est pas faite, et elle mérite d'être affichée dans les bureaux.

| Formulation | Ce que ça signifie vraiment |
|---|---|
| **Non vulnérable** | L'outil a examiné cet actif et a établi qu'il n'est pas affecté. **Information positive.** |
| **Non détecté** | L'outil a examiné l'actif et n'a rien trouvé — ce qui peut vouloir dire qu'il ne sait pas chercher cela. **Absence d'information.** |
| **Non scanné** | L'outil n'a pas examiné l'actif : injoignable, authentification échouée, exclu, hors périmètre. **Absence totale d'information.** |

**Les trois se présentent identiquement dans un rapport** : la ligne est vide, l'actif n'apparaît pas dans la liste des vulnérables. Un tableau de bord qui ne les distingue pas transforme une absence d'information en information rassurante.

🧪 **EN PRATIQUE — les trois questions à poser devant tout rapport de scan**

1. Combien d'actifs du **périmètre de référence** ce rapport couvre-t-il ?
2. Parmi eux, combien ont été scannés **avec authentification réussie** ?
3. Où est la liste des actifs **non scannés**, avec le motif ?

Un rapport qui ne permet pas de répondre à ces trois questions n'est pas exploitable pour piloter, et il n'a aucune valeur probante en audit (§5.6).

### 15.9 Cas particuliers par type d'environnement

| Environnement | Contrainte | Approche recommandée |
|---|---|---|
| **Systèmes industriels** | Le scan actif peut provoquer un défaut (§3.7) | Écoute passive du trafic, extraction depuis les outils d'ingénierie, inventaire manuel assumé (ch. 29) |
| **Équipements réseau et de sécurité** | Peu ou pas d'accès pour un scan authentifié | Inventaire de versions par requête d'administration, corrélation avec les avis constructeurs |
| **Hyperviseurs et appliances** | Accès restreint par l'éditeur | Interface de gestion, versions déclarées, avis fournisseur |
| **Conteneurs** | Éphémères, l'exécution n'est pas le bon moment | Analyse à la construction et dans le registre, pas sur les conteneurs en cours d'exécution |
| **Cloud** | Le scan réseau classique ne voit pas la configuration | Interrogation des interfaces du fournisseur, contrôle de posture (ch. 30) |
| **Postes nomades** | Rarement présents au moment du scan | Agent, obligatoirement — un scan réseau les manquera systématiquement |
| **Services en ligne** | Aucun accès technique | Revue de configuration, déclarations du fournisseur (ch. 31) |

⚠️ **PIÈGE — la saturation des cibles**
Un scan agressif peut dégrader ou faire tomber des services fragiles : équipements anciens, imprimantes, systèmes embarqués, applications à ressources limitées. La règle est de **calibrer l'intensité par zone** et de tester sur un échantillon avant de généraliser. Un scan qui provoque un incident coûte bien plus que sa valeur informative — et il produit surtout un refus durable des équipes, qui vous fermera l'accès pendant des années.

### 15.10 Interpréter un rapport : les sept réflexes

| # | Réflexe | Ce qu'il évite |
|---|---|---|
| 1 | Vérifier le périmètre et le taux d'authentification avant tout | Raisonner sur un échantillon inconnu |
| 2 | Contrôler la révision éditeur avant de conclure sur une version | Le faux positif de rétroportage (§2.2) |
| 3 | Vérifier si le composant est **activé** | Traiter des services installés mais désactivés |
| 4 | Distinguer sévérité **héritée** de la base et sévérité contextuelle | Prioriser sur un score sans exposition (§4.10) |
| 5 | Repérer les doublons : même constat, plusieurs entrées | Compter plusieurs fois le même travail |
| 6 | Identifier les constats **déjà corrigés par l'éditeur** mais non redétectés | Rouvrir un sujet clos |
| 7 | Chercher ce qui **manque** : machines absentes du rapport | La fausse assurance du §15.8 |

### 15.11 ⚠️ Les dix faux positifs les plus coûteux en temps

| # | Faux positif | Comment le lever |
|---|---|---|
| 1 | Rétroportage non pris en compte | Comparer la révision de l'éditeur, consulter l'avis de la distribution |
| 2 | Service installé mais désactivé | Vérifier l'état d'activation |
| 3 | Composant présent mais non chargé par l'application | Analyse d'atteignabilité (§11.6), déclaration du fournisseur |
| 4 | Bannière modifiée ou générique | Scan authentifié |
| 5 | Correspondance produit erronée | Vérifier le produit réel, corriger la table de correspondance |
| 6 | Vulnérabilité affectant une configuration non utilisée | Lire les conditions d'exploitation dans l'avis |
| 7 | Détection sur un appareil qui n'est pas le vôtre (adresse réattribuée) | Réconcilier avec l'inventaire |
| 8 | Constat sur une image de base, déjà corrigé dans l'image dérivée | Analyser l'image finale, pas seulement la base |
| 9 | Doublon entre agent et scan réseau | Règle de déduplication par identifiant pivot |
| 10 | Constat sur un actif décommissionné mais toujours présent dans l'outil | Nettoyage périodique, réconciliation d'inventaire |

📌 **La leçon transversale.** Ces dix causes n'ont presque rien à voir avec la qualité de l'outil. Elles viennent de l'écart entre ce qu'un outil peut observer et ce qu'est réellement votre système. Changer d'outil n'en supprime aucune ; améliorer l'inventaire et la vérification en supprime la majorité.

### 15.12 📌 Limites et coûts réels

| Dimension | Ce à quoi s'attendre |
|---|---|
| **Modèle de licence** | Le plus souvent par actif, ou par volume analysé. Le coût croît avec la découverte — inventorier mieux augmente la facture, ce qui crée une incitation perverse à ne pas chercher |
| **Charge d'exploitation** | L'outil demande du temps : maintien des comptes, des exclusions, des correspondances, traitement des échecs d'authentification |
| **Dépendance éditeur** | Les données historiques sont rarement portables. Un changement d'outil fait perdre l'antériorité, donc la démonstration de progrès |
| **Qualité du reporting** | Très inégale. Beaucoup d'outils rendent difficile le calcul honnête du §15.6, précisément parce qu'il n'est pas flatteur |
| **Périmètre non couvert** | Systèmes industriels, services en ligne, composants embarqués, produits — c'est-à-dire une part importante du périmètre réel |

✅ **BONNE PRATIQUE (P1)** — Exigez, dès l'évaluation d'un outil, la capacité d'**exporter les données brutes** et l'historique dans un format ouvert. C'est ce qui vous permettra de calculer vos propres indicateurs (chapitre 38), de constituer une preuve indépendante de l'outil (§5.6), et de changer de fournisseur sans repartir de zéro.

### 15.13 🔴 FIL ROUGE — janvier 2027 : trois semaines perdues

Le premier scan authentifié couvrant l'ensemble du périmètre élargi d'HELIOMED remonte, parmi 3 800 constats, une vulnérabilité critique sur une bibliothèque de chiffrement présente sur **42 serveurs** de classe C1 et C2.

Malik Ferhaoui lance la campagne de correction. Elle prend trois semaines : planification, fenêtres, tests, déploiement en anneaux, vérification. Le travail est bien fait.

**Le problème.** À la fin de la campagne, un contrôle de routine sur trois serveurs révèle que la version installée **avant** la campagne contenait déjà le correctif. La distribution avait rétroporté la correction six mois plus tôt ; le numéro de version amont, lui, n'avait pas bougé. Les 42 serveurs n'ont jamais été vulnérables.

**Ce que coûte l'erreur.** Trois semaines de deux personnes, six fenêtres de maintenance consommées, deux redémarrages de serveurs de production hors nécessité — et, plus grave, une régression mineure sur une application métier lors de la montée de version, qui a occupé l'équipe applicative pendant deux jours.

**La cause racine, et elle n'est pas technique.** Le réflexe n° 2 du §15.10 n'était écrit nulle part. Malik connaissait le mécanisme du rétroportage — il l'avait lu — mais rien dans le processus ne l'obligeait à vérifier avant de lancer une campagne de 42 serveurs.

**Les trois mesures prises.**

1. **Un point de contrôle obligatoire** dans le processus : toute campagne portant sur plus de dix actifs exige une vérification préalable sur **trois actifs représentatifs**, avec preuve jointe au dossier de campagne. Coût : trente minutes. Le pilote du chapitre 18 est né de cet incident.
2. **Une règle de qualification** : un constat issu d'un scan sur système à support long reste au statut *piste exploratoire* (§14.7) tant que la révision éditeur n'est pas vérifiée. Il ne peut pas déclencher de campagne à ce statut.
3. **Un signalement à l'éditeur de l'outil**, avec demande de prise en compte des révisions de distribution. Réponse reçue : la fonctionnalité existe et n'était pas activée sur leur instance. Elle l'est depuis.

**Ce que Claire Nadeau retient**, et qu'elle formule au comité en une phrase que l'équipe reprendra ensuite : *le coût d'un faux positif n'est pas le temps perdu à l'analyser, c'est le travail inutile qu'il déclenche quand personne ne l'analyse.*

**Livrable de l'épisode.** Le point de contrôle des trois actifs représentatifs, intégré au dossier de campagne standard — il figure en Annexe L.

→ La suite en 🔴 §16.11, quand il faudra prioriser les 3 800 constats restants.

→ **Chapitre 16 — Triage et priorisation défendables** : décider quoi traiter, et pourquoi un seuil de gravité ne suffit pas.

### Synthèse mentale du chapitre 15

Les familles d'outils ne se substituent pas : un agent ignore l'exposition réseau, un scan externe ignore l'état interne, une analyse de composition ignore ce que le système embarque — n'en utiliser qu'une crée un angle mort prévisible. Le scan non authentifié produit du faux positif structurel, mais il est le seul à établir ce qui est réellement joignable depuis un point donné. Le compte de scan et l'outil lui-même sont des actifs de niveau 0, et ils comptent régulièrement parmi les composants les plus en retard d'un parc. La fraîcheur de la base de détection est un objet qui se dégrade quotidiennement, et le délai que vous contrôlez est souvent le plus long. La couverture se calcule sur le périmètre de référence, en distinguant cinq populations, dont les exclusions — qui sont des dérogations déguisées si elles n'ont ni motif, ni propriétaire, ni date de revue. Enfin, « non vulnérable », « non détecté » et « non scanné » se présentent identiquement dans un rapport et signifient trois choses radicalement différentes : les confondre transforme une absence d'information en information rassurante.

**Trois questions de vérification**

1. Un rapport indique 0 vulnérabilité critique sur un ensemble de serveurs. Quelles trois questions posez-vous avant d'en tirer la moindre conclusion ?
2. Pourquoi le compte utilisé par votre scanner mérite-t-il un traitement de niveau 0, et quelles règles lui appliquez-vous ?
3. Une machine provoque un incident pendant un scan et vous l'excluez. Que devez-vous produire au même moment pour que cette exclusion ne devienne pas un angle mort permanent ?

---

## Chapitre 16 — Triage et priorisation défendables

### 16.1 Pourquoi « tout ce qui dépasse 7 » ne fonctionne pas

Commençons par la démonstration chiffrée, parce que l'argument théorique ne convainc personne tant que les nombres ne sont pas posés.

**Le point de départ.** Un parc de taille intermédiaire produit, lors d'un premier scan authentifié complet, de l'ordre de plusieurs milliers de constats. Reprenons les chiffres du fil rouge : 4 312 constats, dont 1 176 de gravité supérieure ou égale à 7.

**Le calcul de capacité.** Comptez vingt minutes par constat — qualification, recherche du correctif, planification, suivi, vérification. C'est une estimation basse pour un constat non trivial.

```
1 176 constats × 20 min            = 392 heures
392 h / 2 personnes                = 196 h par personne
196 h à ~75 h disponibles par mois ≈ 2,6 mois de traitement
```

Deux mois et demi pour résorber le stock initial : à ce stade, la situation paraît tenable. **C'est le flux qui la rend impossible.**

**Le calcul qui compte est celui du régime permanent.** Un parc de cette taille produit typiquement 250 à 400 nouveaux constats par mois, dont une proportion comparable dépasse le seuil de gravité retenu — soit environ 70 à 110 constats mensuels à traiter selon cette règle.

```
90 nouveaux constats/mois × 20 min   ≈ 30 h/mois
Capacité disponible                   ≈ 150 h/mois pour deux personnes
Reste pour le stock initial           ≈ 120 h/mois
392 h de stock / 120 h                ≈ 3,3 mois
```

**Sur le papier, cela passe.** Dans la réalité, deux hypothèses de ce calcul sont fausses :

- Les 75 heures mensuelles supposent que la moitié du temps est consacrée au MCS. La mesure du §37.9 donne un ordre de grandeur bien plus faible une fois déduits l'exploitation courante, les changements, les incidents et les astreintes.
- Les 20 minutes par constat ne couvrent que le triage. Elles n'incluent ni la planification, ni la fenêtre, ni le déploiement, ni la vérification, ni la preuve — c'est-à-dire l'essentiel de la charge réelle (§37.9).

Avec des hypothèses réalistes, le stock ne se résorbe pas : il se stabilise à un niveau élevé, ou il croît. **Et c'est le meilleur des cas**, celui où le flux est régulier : une campagne d'exploitation sur un produit très déployé peut ajouter plusieurs centaines de constats en une semaine.

**Le second problème, plus grave que le premier.** Cette méthode ne se contente pas de produire trop de travail : elle produit le **mauvais** travail. Elle écarte des constats réellement dangereux — la vulnérabilité de gravité 5,9 activement exploitée sur une interface d'administration exposée du fil rouge — et inclut des milliers de constats qui ne seront jamais exploités. Elle est simultanément trop large et trop étroite.

**La conclusion, qui structure tout le chapitre.** Le seuil de gravité seul échoue parce qu'il utilise **une seule des cinq informations** nécessaires à une décision. Il connaît la gravité technique ; il ignore l'exploitation observée, l'exposition, la criticité métier et l'effort de correction.

### 16.2 Construire une fonction de priorisation

**Les cinq entrées**, et ce que chacune apporte :

| Entrée | Question | Source | Qui la détient |
|---|---|---|---|
| **Gravité technique** | Quels dégâts si c'est exploité ? | Score de gravité (§4.4) | Externe |
| **Exploitation** | Est-ce utilisé par des attaquants ? | Catalogue d'exploitation avérée, renseignement (§4.6) | Externe |
| **Probabilité** | Est-ce susceptible de l'être ? | Modèle de prédiction (§4.5) | Externe |
| **Exposition** | Est-ce atteignable, et par qui ? | Votre cartographie (ch. 11) | **Vous seul** |
| **Criticité** | Que vaut cet actif pour l'organisation ? | Votre inventaire (ch. 10) | **Vous seul** |

Une sixième entrée intervient à l'arbitrage, sans entrer dans l'évaluation du risque : l'**effort de correction**. Elle ne change pas la priorité d'un constat, elle change l'ordre dans lequel on traite des constats de priorité comparable — et elle justifie de regrouper (§16.7).

⚠️ **PIÈGE — la formule pondérée**
La tentation est forte de construire un score unique en pondérant les cinq entrées. C'est une mauvaise idée pour trois raisons : les pondérations sont arbitraires et indéfendables en audit ; un score composite masque le raisonnement au lieu de l'expliciter ; et une entrée manquante — cas fréquent depuis la fragmentation de l'écosystème (§4.9) — rend le score incalculable au lieu de simplement dégrader la décision. **Préférez un arbre de décision** : il produit une action, il se lit, il se discute, et il fonctionne même avec une information incomplète.

🖼 **SCHÉMA — Arbre de décision de triage.** *Arbre à six nœuds de décision et cinq feuilles colorées par urgence. C'est le visuel le plus utilisé du cours : à soigner particulièrement.*

### 16.3 L'arbre de décision opérationnel

Voici un arbre utilisable tel quel, à calibrer sur vos classes de service (§7.2).

```
① La vulnérabilité est-elle activement exploitée ?
   ├─ OUI ─→ ② L'actif est-il joignable depuis Internet ?
   │          ├─ OUI ─→ ████ AGIR EN URGENCE  (72 h, hors fenêtre autorisée)
   │          └─ NON ─→ ③ L'actif est-il de niveau 0 ou critique métier ?
   │                     ├─ OUI ─→ ███ TRAITER EN PRIORITÉ  (7 j)
   │                     └─ NON ─→ ██ TRAITER  (30 j)
   └─ NON ─→ ④ Probabilité d'exploitation élevée OU gravité critique ?
              ├─ OUI ─→ ⑤ Exposé ou actif critique ?
              │          ├─ OUI ─→ ██ TRAITER  (30 j)
              │          └─ NON ─→ █ PLANIFIER  (prochaine campagne)
              └─ NON ─→ ⑥ Corrigeable dans une campagne groupée ?
                         ├─ OUI ─→ █ PLANIFIER  (campagne trimestrielle)
                         └─ NON ─→ ░ SURVEILLER  (revue semestrielle)
```

**Les quatre propriétés qui en font un bon outil**, et qu'un score composite n'a pas :

1. **Il produit une action**, pas un nombre : chaque feuille correspond à un délai et à un mode de traitement.
2. **Il est auditable.** En cas de contestation, on ne discute pas d'une pondération, on relit le chemin parcouru : « exploitation non observée, non exposé, actif non critique ». C'est vérifiable.
3. **Il tolère l'information manquante.** Si la probabilité d'exploitation n'est pas disponible pour ce constat, la question ④ se résout sur la gravité seule. La décision est dégradée, pas bloquée.
4. **Il place les deux informations que vous seul détenez au cœur du raisonnement** : l'exposition et la criticité apparaissent à trois nœuds sur six.

✅ **BONNE PRATIQUE (P0)** — Écrivez votre arbre, faites-le valider en comité MCS, et **datez-le**. C'est le document que vous produirez le jour où l'on vous demandera pourquoi tel constat n'a pas été traité en priorité. Un arbre validé et appliqué est une défense solide ; une décision au cas par cas ne l'est pas.

### 16.4 Exploitabilité contextuelle

Le §11.6 a posé la notion. Trois vérifications rapides, à faire avant d'engager toute campagne, retirent une part significative du volume :

| Vérification | Durée | Question |
|---|---|---|
| **Activation** | 1 minute | Le service ou module vulnérable est-il actif sur cet actif ? |
| **Configuration requise** | 5 minutes | L'avis mentionne-t-il une condition — option activée, mode particulier — que vous n'avez pas ? |
| **Atteignabilité du code** | Variable | La fonction vulnérable est-elle appelable ? (déclaration du fournisseur, analyse) |

**Le résultat de ces vérifications ne clôt pas le constat**, il le **dépriorise avec justification** — nuance essentielle traitée au §16.6 et au chapitre 17. La distinction est ce qui vous protège le jour où la configuration change et où le service désactivé est réactivé par un autre projet.

### 16.5 Fixer des délais tenables

Les délais des classes de service (§7.2) doivent satisfaire trois contraintes simultanées, et c'est leur conjonction qui est difficile.

| Contrainte | Question |
|---|---|
| **Cohérence avec le risque** | Un délai de 30 jours sur un actif exposé portant une vulnérabilité exploitée est indéfendable |
| **Tenabilité** | Un délai que vous ne tenez pas produit une non-conformité permanente (§7.2) |
| **Justifiabilité** | Vous devez pouvoir expliquer d'où viennent ces chiffres |

**Sur le troisième point**, trois sources de justification acceptables : les délais imposés par un référentiel qui vous est applicable (chapitre 8) ; les délais issus d'un modèle méthodologique public reconnu, en le citant comme référence et non comme obligation (§8.7) ; ou votre propre calibrage documenté, fondé sur une mesure de votre capacité réelle. La troisième est parfaitement recevable — à condition d'être écrite.

**La méthode de calibrage par la capacité**, qui produit des chiffres tenables :

```
1. Mesurez le volume mensuel réel de constats atteignant chaque feuille de l'arbre
2. Mesurez le temps réellement consommé par constat, par catégorie
3. Confrontez à la capacité disponible
4. Ajustez soit les délais, soit la capacité — jamais l'affichage seul
```

L'étape 4 est un arbitrage de direction, pas une décision technique. Si la capacité ne permet pas des délais cohérents avec le risque, c'est un **constat à remonter** au comité stratégique (§9.3), avec les trois options du chapitre 12 : plus de moyens, moins de périmètre, ou plus de risque accepté.

### 16.6 La dépriorisation défendable

Décider de ne pas traiter maintenant est une décision normale et fréquente. Ce qui la rend acceptable, c'est sa **traçabilité**.

**Les quatre motifs légitimes**, avec ce qui doit être écrit pour chacun :

| Motif | À documenter | Risque associé |
|---|---|---|
| Non atteignable dans votre contexte | Le fait vérifié qui l'établit, et sa date | La configuration peut changer |
| Faible probabilité et exposition nulle | Les valeurs constatées et la date | Les deux peuvent évoluer |
| Correction groupée à venir | La campagne cible et sa date | La campagne peut glisser |
| Effort disproportionné au risque | La comparaison chiffrée | Jugement contestable |

⚠️ **PIÈGE — la dépriorisation qui devient un oubli**
Un constat déprioritisé sans **date de revue** disparaît. La règle est simple : toute dépriorisation porte une date de réexamen, et le réexamen est automatique — pas dépendant de la mémoire de quelqu'un. Les trois premiers motifs ci-dessus reposent sur un état du monde qui peut changer ; ils sont valables jusqu'à réexamen, pas définitivement.

**Dépriorisation ≠ clôture.** Un constat déprioritisé reste **ouvert** dans la file, avec une échéance repoussée. Un constat clos n'existe plus. Confondre les deux fait disparaître de votre pilotage la dette que vous venez d'accepter — et c'est ce que le chapitre 17 formalise.

### 16.7 Traiter la volumétrie : penser en campagnes

Le triage réduit la file ; il ne la vide pas. Le second levier consiste à changer d'unité de travail.

**Raisonner par constat individuel est la source principale d'inefficacité.** Trois regroupements produisent des gains considérables :

| Regroupement | Principe | Gain typique |
|---|---|---|
| **Par correctif** | Un correctif cumulatif corrige souvent des dizaines de constats sur le même actif | Le travail est celui d'un correctif, pas de trente |
| **Par actif** | Traiter tous les constats d'un actif en une intervention | Une seule fenêtre, un seul test, un seul redémarrage |
| **Par montée de version** | Passer à une version supportée règle simultanément le présent et le futur | Supprime des constats à venir |

**Le changement de perspective à opérer**, et il est plus profond qu'il n'y paraît : *ne mesurez pas votre travail en nombre de vulnérabilités fermées, mesurez-le en nombre d'actifs ramenés à un état de référence.* Un actif à jour ne produit plus de constats. C'est aussi ce qui rend l'approche immuable du §3.5 si efficace : la cadence de reconstruction remplace des centaines de traitements individuels.

### 16.8 ⏱ Reconstruire ce que l'on recevait gratuitement

*Bloc périssable, vérifié le 30/07/2026.*

La fragmentation de l'écosystème (§4.9) a une conséquence directe et concrète sur le triage : une part croissante des constats arrive **sans enrichissement** — sans score, sans correspondance produit fiable, parfois sans description exploitable.

**Les trois stratégies d'adaptation**, par ordre de robustesse :

| Stratégie | Principe | Effort |
|---|---|---|
| **Basculer le poids sur ce que vous détenez** | Faire porter la décision sur l'exposition et la criticité plutôt que sur le score reçu | Faible, et c'est déjà la bonne pratique |
| **Multiplier les sources** | Croiser plusieurs bases, dont une européenne, plus les avis éditeurs (§14.4) | Moyen |
| **Enrichir en interne** | Attribuer soi-même une gravité aux constats non enrichis, selon une grille écrite | Élevé, réservé aux actifs C1 |

**Le point encourageant**, et il vaut d'être souligné : une organisation qui a fait le travail des chapitres 10 et 11 est **beaucoup moins exposée** à cette fragmentation qu'une organisation qui dépendait entièrement d'un score externe. L'exposition et la criticité ne dépendent d'aucun fournisseur. C'est un argument de plus pour l'ordre de séquencement du §1.4.

### 16.9 📌 Limites du triage

- **Le triage ne crée aucune capacité de remédiation.** Il permet de dépenser au bon endroit une capacité qui reste constante. Si votre capacité est structurellement insuffisante, le triage la rend visible, il ne la résout pas.
- **Le risque de sur-ingénierie est réel.** Un dispositif de triage sophistiqué peut consommer plus de temps que la correction elle-même. Si votre arbre nécessite plus de cinq minutes par constat, il est trop complexe.
- **Les entrées externes sont volatiles.** Un constat déprioritisé aujourd'hui peut devenir urgent demain, sans qu'aucune information interne ne change. D'où l'obligation de rejeu périodique (§16.6).
- **Le triage ne remplace pas la correction de fond.** Un parc dont les images de référence sont anciennes reproduira les mêmes constats indéfiniment. Le triage traite le symptôme.

### 16.10 🔬 Mini-lab 4 — Construire une matrice de triage

**Objectif** — Appliquer l'arbre de décision et mesurer l'écart avec un tri par gravité.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §16.3, §11.7, §7.2 · **Livrable** priorisation argumentée des 10 constats.
**Compétences validées** — ✔ appliquer un arbre de décision ✔ intégrer exposition et criticité au triage ✔ reconnaître un actif de niveau 0 ✔ déprioriser avec justification et date de revue

**Données fournies.** Vingt-cinq constats issus d'un scan. Extrait représentatif de dix d'entre eux :

| # | Gravité | Exploitation observée | Probabilité | Actif | Exposition | Criticité |
|---|---|---|---|---|---|---|
| 1 | 9,8 | Non | Faible | Serveur de test | Interne | C3 |
| 2 | 5,9 | **Oui** | Élevée | Passerelle d'accès distant | **Internet** | C1 |
| 3 | 8,1 | Non | Faible | Poste bureautique ×340 | Interne | C3 |
| 4 | 7,5 | Non | Moyenne | Contrôleur de domaine | Interne | **C1 — niveau 0** |
| 5 | 6,1 | **Oui** | Élevée | Automate de production | Réseau industriel isolé | C4 |
| 6 | 9,1 | Non | Faible | Bibliothèque, service désactivé | Interne | C2 |
| 7 | 4,3 | Non | Faible | Serveur de fichiers | Interne | C2 |
| 8 | 8,8 | Non | **Élevée** | Serveur web public | **Internet** | C1 |
| 9 | 7,2 | Non | Faible | Console de sauvegarde | Interne | **C1 — niveau 0** |
| 10 | 9,4 | Non | Moyenne | Hyperviseur | Réseau d'administration | **C1 — niveau 0** |

**Questions.** (a) Classez ces dix constats avec l'arbre du §16.3. (b) Classez-les par gravité décroissante. (c) Comparez les cinq premiers de chaque classement. (d) Quels constats méritent une vérification avant tout traitement ? (e) Le constat n° 5 relève d'une classe particulière : que faites-vous ?

**Corrigé commenté**

**(a) Classement par l'arbre :**

| Rang | # | Chemin dans l'arbre | Décision |
|---|---|---|---|
| 1 | **2** | Exploitée → exposée Internet | **AGIR EN URGENCE — 72 h** |
| 2 | **5** | Exploitée → non exposée → actif critique (C4) | **TRAITER EN PRIORITÉ — mais régime C4 : compensation** |
| 3 | **8** | Non exploitée → probabilité élevée → exposé | **TRAITER — 30 j** |
| 4 | **10** | Non exploitée → gravité critique → actif de niveau 0 | **TRAITER — 30 j** |
| 5 | **4** | Non exploitée → gravité critique → niveau 0 | **TRAITER — 30 j** |
| 6 | **9** | Non exploitée → gravité élevée → niveau 0 | TRAITER — 30 j |
| 7 | **3** | Non exploitée → gravité élevée → non exposé, C3 | PLANIFIER — campagne, mais volume : 340 postes |
| 8 | **1** | Non exploitée → gravité critique → non exposé, C3 | PLANIFIER |
| 9 | **6** | Service désactivé | **DÉPRIORISER avec justification et date de revue** |
| 10 | **7** | Faible partout | SURVEILLER |

**(b) Classement par gravité décroissante :** 1 (9,8) · 10 (9,4) · 6 (9,1) · 8 (8,8) · 3 (8,1) · 4 (7,5) · 9 (7,2) · 5 (6,1) · 2 (5,9) · 7 (4,3).

**(c) La comparaison, et c'est tout l'objet du lab.**

| Méthode | Cinq premiers |
|---|---|
| Arbre de décision | **2, 5, 8, 10, 4** |
| Gravité seule | **1, 10, 6, 8, 3** |

Deux constats seulement sont communs. Surtout : le tri par gravité place en **première position** le constat n° 1 — un serveur de test interne, non exposé, non exploité — et relègue en **avant-dernière** le n° 2, la seule vulnérabilité activement exploitée sur un actif publié sur Internet. Il place également en troisième position le n° 6, dont le service est désactivé.

**(d) Les vérifications préalables :** le n° 6 (état d'activation — déjà connu ici, à confirmer sur l'ensemble du parc), le n° 3 (340 postes : appliquer le point de contrôle des trois actifs représentatifs du §15.13), et le n° 1 (vérifier qu'il s'agit bien d'un serveur de test, et surtout **ce qu'il contient** — un serveur de test portant une copie de données de production n'est pas un actif C3, voir chapitre 28).

**(e) Le constat n° 5.** Vulnérabilité exploitée sur un automate en classe C4. Le régime applicable n'est pas la correction mais la **compensation sous 72 h** (§7.2) : vérifier l'isolation du réseau industriel, restreindre les accès, renforcer la surveillance, et planifier le correctif validé par le constructeur pour le prochain arrêt de production. La décision est écrite et signée par le propriétaire métier. C'est le chapitre 29.

**Les trois erreurs attendues.** Traiter le n° 5 comme un constat C1 et exiger une correction immédiate, ce qui est irréaliste et détruira la relation avec l'exploitant industriel. **Clore** le n° 6 au lieu de le dépriorer. Et sous-estimer le n° 3 en le voyant comme un constat unique alors qu'il représente 340 actifs, donc une campagne à part entière.

### 16.11 🔴 FIL ROUGE — février 2027 : la refonte du triage, un an après

Un an après la première tentative (§4.11), Claire Nadeau et Malik Ferhaoui formalisent l'arbre de décision d'HELIOMED et mesurent l'effet sur les 3 800 constats du scan de janvier.

**Le résultat, en une page.**

| Feuille de l'arbre | Constats | Charge estimée |
|---|---|---|
| Agir en urgence — 72 h | 4 | 1 jour |
| Traiter en priorité — 7 j | 19 | 4 jours |
| Traiter — 30 j | 143 | 3 semaines |
| Planifier — campagne | 1 890 | **21 campagnes groupées**, dont 6 montées de version |
| Surveiller | 1 604 | Revue semestrielle |
| Déprioritisé avec justification | 140 | Réexamen trimestriel automatique |

**Ce qui change réellement.** Ce ne sont pas les 4 constats urgents — ils auraient été traités de toute façon. C'est la ligne « Planifier » : 1 890 constats deviennent **21 campagnes**, parce que le regroupement par correctif et par actif (§16.7) transforme des milliers de traitements individuels en quelques dizaines d'interventions. Six de ces campagnes sont des montées de version qui supprimeront aussi les constats à venir.

La charge annuelle estimée passe de « impossible » à « tenable avec deux personnes, à condition de ne pas ajouter de périmètre ». Ce dernier point est écrit noir sur blanc dans la note au comité.

**La décision la plus discutée.** Les 1 604 constats en surveillance représentent 42 % du total, et le représentant commercial demande si l'on peut « laisser 1 604 vulnérabilités ouvertes ». Claire répond en trois points : elles ne sont ni exploitées, ni exposées, ni sur des actifs critiques ; elles sont **suivies et réexaminées**, pas oubliées ; et la majorité disparaîtra sans traitement individuel lors des campagnes de montée de version. Le comité valide, et la formulation retenue au compte rendu est celle qui compte : *« 1 604 constats en surveillance active, réexamen semestriel, aucun sur actif exposé ou critique »*.

**Ce qui n'était pas prévu.** En appliquant l'arbre, deux constats atteignent la feuille « urgence » sur des actifs de l'infogérant — les premiers depuis que la restitution mensuelle de données fonctionne (§13.9). Le délai contractuel de 7 jours s'applique. C'est la première fois qu'HELIOMED peut opposer un délai à son prestataire sur une base documentée.

**Livrable de l'épisode.** L'arbre de décision d'HELIOMED, daté et validé en comité, et la matrice de triage figurant en Annexe C.

→ La suite en 🔴 §17.14, quand ces 21 campagnes devront être suivies sans se perdre.

→ **Chapitre 17 — Workflow de remédiation et gestion du *backlog*** : piloter le traitement entre la décision et la correction.

### Synthèse mentale du chapitre 16

Un seuil de gravité échoue pour deux raisons cumulées : il produit un volume arithmétiquement intraitable, et il produit le mauvais travail — simultanément trop large et trop étroit. Cinq entrées sont nécessaires à une décision, dont deux que vous seul détenez : l'exposition et la criticité. Préférez un arbre de décision à un score composite, parce qu'il produit une action, se relit en audit, tolère l'information manquante et place au cœur du raisonnement ce que vous êtes seul à savoir. Trois vérifications de quelques minutes — activation, condition de configuration, atteignabilité — retirent une part importante du volume, mais elles déprioritisent, elles ne closent pas. Les délais se calibrent sur la capacité mesurée, et l'écart entre capacité et risque est un constat à remonter, pas à absorber. Enfin, le levier le plus puissant n'est pas le triage mais le changement d'unité de travail : ne comptez pas les vulnérabilités fermées, comptez les actifs ramenés à un état de référence.

**Trois questions de vérification**

1. Démontrez en quatre lignes de calcul pourquoi une règle « corriger tout ce qui dépasse 7 » est intenable sur un parc de 200 serveurs, puis expliquez pourquoi ce n'est pas le problème principal de cette règle.
2. Pourquoi un score composite pondéré est-il plus fragile qu'un arbre de décision, notamment depuis la fragmentation des sources de données ?
3. Un constat porte sur un service installé mais désactivé. Quelle est la bonne décision, en quoi diffère-t-elle d'une clôture, et que devez-vous prévoir pour que cette décision reste valable dans six mois ?

---

## Chapitre 17 — Workflow de remédiation et gestion du *backlog*

### 17.1 Pourquoi la décision ne suffit pas

Le chapitre 16 a produit une décision pour chaque constat. Entre cette décision et la correction effective, il se passe des semaines — parfois des mois — pendant lesquelles le constat doit **exister quelque part**, avec un propriétaire, une échéance et un état.

C'est ce que la plupart des organisations ne font pas. Le triage est soigné, la correction est bien exécutée, et **entre les deux il n'y a qu'un tableur**. Les symptômes sont toujours les mêmes :

- personne ne sait combien de constats sont réellement en cours de traitement ;
- un même problème est traité deux fois par deux personnes différentes ;
- un constat affecté à quelqu'un qui a quitté l'entreprise n'est jamais réaffecté ;
- une vulnérabilité corrigée réapparaît trois mois plus tard sans que personne ne s'en étonne ;
- on ne peut pas répondre à la question « depuis combien de temps ce constat est-il ouvert ? ».

**Le principe de ce chapitre** : le constat est un **objet de gestion** avec un cycle de vie, pas une ligne dans un rapport. C'est ce cycle de vie qui rend le MCS pilotable, mesurable et démontrable.

### 17.2 De la détection au ticket : agrégation et déduplication

Un scan produit des constats, pas des tickets. Créer un ticket par constat est une erreur qui noie l'organisation : 3 800 constats produiraient 3 800 tickets, dont personne ne ferait rien.

**La structure à adopter — le modèle parent / enfants :**

```
CONSTAT PARENT : « Vulnérabilité X dans le composant Y »
   ├─ Actif A  (version, état, échéance)
   ├─ Actif B
   ├─ … 42 actifs
   └─ Décision de triage, propriétaire, échéance : portés par le PARENT
```

Un ticket par **problème**, avec la liste des actifs concernés en pièces attachées. La décision, l'échéance et le propriétaire s'attachent au parent ; l'état d'avancement se mesure sur les enfants.

**Les quatre règles de déduplication**, qui évitent la majorité du bruit :

| Règle | Effet |
|---|---|
| Un même identifiant de vulnérabilité sur plusieurs actifs → **un** ticket parent | Divise le volume par un facteur important |
| Plusieurs constats corrigés par le **même correctif** → un ticket | Aligne le ticket sur l'unité de travail réelle |
| Constat remonté par deux outils différents → un ticket, deux sources | Évite le double traitement (§15.11, faux positif n° 9) |
| Constat réapparaissant sur un actif redéployé → **réouverture**, pas nouveau ticket | Préserve l'historique et révèle la récurrence (§17.9) |

⚠️ **PIÈGE — la déduplication trop agressive**
Regrouper des constats qui ne se corrigent pas de la même façon crée un ticket impossible à clore : il reste ouvert parce qu'un actif sur quarante-deux résiste. Le critère de regroupement doit être **l'action de correction**, pas la ressemblance du constat.

### 17.3 Campagnes ou traitement à l'unité

Deux modes de travail coexistent, et les confondre coûte cher.

| Mode | Quand l'employer | Unité |
|---|---|---|
| **À l'unité** | Constats urgents, actifs de niveau 0, cas particuliers | Le constat parent |
| **En campagne** | Volume, correctifs cumulatifs, montées de version | Un lot d'actifs, une fenêtre, un objectif d'état |

**La campagne est un objet de gestion distinct**, avec ses propres attributs : périmètre d'actifs, objectif d'état cible, fenêtre, anneaux de déploiement, critères d'arrêt, propriétaire, plan de retour arrière. Elle **absorbe** un ensemble de tickets, qui se ferment collectivement à sa vérification.

✅ **BONNE PRATIQUE (P1)** — Un tableau de bord de MCS mature affiche **deux compteurs distincts** : les constats en traitement unitaire, et les campagnes en cours avec leur avancement. Mélanger les deux dans un unique décompte de vulnérabilités ouvertes produit un chiffre qui n'a aucun sens opérationnel.

### 17.4 Propriétaires, refus d'affectation et constats orphelins

**L'affectation** relie le ticket au propriétaire technique de l'actif, issu de l'inventaire (§5.5 et §10.4). Si l'inventaire porte cette information, l'affectation est automatique — c'est l'un des bénéfices les plus concrets du travail des chapitres 5 et 10.

**Trois situations à traiter explicitement**, faute de quoi elles bloquent silencieusement la file :

| Situation | Traitement |
|---|---|
| **Aucun propriétaire** | Le constat porte sur un actif orphelin. Ce n'est pas un problème de remédiation, c'est un problème d'inventaire : il remonte au processus de désignation (§5.5), avec la procédure d'extinction programmée en dernier recours |
| **Refus d'affectation** | Le propriétaire estime que l'actif ne relève pas de lui. Délai de contestation borné — par exemple 5 jours ouvrés — puis arbitrage au comité. **Sans délai, le ticket reste en suspens indéfiniment** |
| **Propriétaire indisponible** | Départ, congé long, réorganisation. Règle de suppléance automatique, sinon le ticket vieillit sans que personne ne le sache |

🏢 **VU EN RÉUNION** — Un constat critique traîne depuis onze semaines. En comité, chacun explique de bonne foi pourquoi il ne s'agit pas de son périmètre : l'exploitation dit que c'est applicatif, l'équipe applicative dit que c'est système, le métier dit qu'il n'a pas été saisi. Tous ont raison. Ce qui manquait n'était pas de la bonne volonté, c'était un **délai de contestation borné** et une escalade automatique.

⚠️ **PIÈGE — le ticket affecté à une équipe**
Affecter à « l'équipe infrastructure » revient à n'affecter à personne : c'est la version outillée du problème du §5.5. L'affectation nominative est un prérequis, et le suivi de l'âge du *backlog* par personne révèle très vite les affectations fictives.

### 17.5 Échéances : départ du compteur et suspensions légitimes

**La question qui doit être tranchée une fois pour toutes** : à partir de quand court le délai ?

| Point de départ possible | Avantage | Inconvénient |
|---|---|---|
| Publication du correctif par l'éditeur | Reflète le risque réel | Vous pénalise pour un scan tardif |
| **Détection par votre outil** | Mesurable, sous votre contrôle | Récompense un scan peu fréquent |
| Création du ticket | Simple | Décale artificiellement le délai |

**La recommandation** : mesurer **les deux premiers**, et les présenter séparément. Le délai depuis la publication mesure le temps écoulé **depuis qu'une correction était disponible** ; le délai depuis la détection mesure votre **réactivité**. L'écart entre les deux mesure la fraîcheur de votre détection (§15.5) — un troisième indicateur, gratuit, et souvent le plus instructif.

⚠️ **Aucun des deux ne mesure la durée d'exposition réelle**, qui commence à l'introduction de la vulnérabilité dans votre parc — souvent des années plus tôt, comme le montre le cas de synthèse A. Ne présentez jamais le délai depuis la publication comme « l'exposition » : c'est une borne inférieure.

#### Les deux horloges

C'est la distinction qui empêche de rendre le retard invisible.

| Horloge | Départ | Se suspend ? | Ce qu'elle mesure |
|---|---|---|---|
| **Horloge de risque** | Connaissance pertinente, ou disponibilité d'une correction ou d'une mesure d'atténuation | **Jamais** | Le temps pendant lequel le risque est porté |
| **Horloge de traitement (SLA)** | Idem | Oui, dans des cas limitativement définis | Le respect de l'engagement opérationnel |

**Pourquoi les deux sont nécessaires.** Un gel de production, une attente de correctif éditeur ou une demande d'information suspendent légitimement l'**engagement opérationnel** — l'équipe n'est pas en faute. Mais **le risque, lui, continue de courir**. Une organisation qui ne publie que l'horloge de traitement affiche des délais tenus tout en portant une exposition croissante qu'aucun indicateur ne montre.

✅ **BONNE PRATIQUE (P0)** — Publiez les deux. L'horloge de traitement pilote l'équipe ; l'horloge de risque pilote la direction. Un écart croissant entre les deux est le signal le plus honnête d'un problème structurel — capacité, dépendance fournisseur ou gels trop nombreux.

**Les suspensions légitimes de l'horloge de traitement**, à définir limitativement :

| Motif | Condition |
|---|---|
| Attente d'un correctif éditeur | Le correctif n'existe pas encore — documenté, relance périodique, **et mesure compensatoire engagée** (ch. 20) |
| Attente d'une information demandée à un tiers | Demande écrite et horodatée (§14.10), avec date de relance |
| Fenêtre de gel de production | Prévue par la politique, avec sa clause de levée (§9.4) |

⚠️ **Une suspension ne suspend jamais le risque.** Toute suspension de plus de quelques jours doit s'accompagner d'une mesure compensatoire ou d'une acceptation formelle — sinon vous avez seulement rendu le retard invisible.

⚠️ **PIÈGE — la suspension comme échappatoire**
Sans liste limitative, la suspension devient le moyen de faire disparaître les retards des indicateurs. **Deux garde-fous** : le temps passé en suspension est mesuré et affiché séparément, et une suspension de plus de N jours déclenche une escalade automatique.

🖼 **SCHÉMA — Cycle de vie d'un constat.** *Machine à états, sept états principaux, transitions fléchées, états terminaux distingués des états ouverts (dérogation, dépriorisé).*

### 17.6 Le modèle d'états

Un cycle de vie en sept états, avec des transitions contrôlées. C'est le **livrable de référence** du chapitre, détaillé en Annexe J.

```
   NOUVEAU
      │  qualification (statut §14.7, vérifications §16.4)
      ▼
   QUALIFIÉ ──────────────────► FAUX POSITIF (clos, avec preuve)
      │  décision de triage (§16.3)
      ▼
   AFFECTÉ ───────────────────► DÉPRIORISÉ (ouvert, date de revue)
      │  propriétaire accepte
      ▼
   PLANIFIÉ ──────────────────► DÉROGATION (ouvert, §7.4)
      │  fenêtre, campagne
      ▼
   EN CORRECTION
      │  action réalisée
      ▼
   À VÉRIFIER ────────────────► ÉCHEC → retour à PLANIFIÉ
      │  preuve obtenue
      ▼
   CLOS ◄───────────────────── RÉOUVERTURE si réapparition
```

**Les champs obligatoires par état** — c'est ce qui empêche un ticket d'avancer sans le travail correspondant :

| État | Champs exigés pour y entrer |
|---|---|
| Qualifié | Statut de qualification, actifs confirmés, vérification d'activation |
| Affecté | Propriétaire nominatif, échéance, décision de triage |
| Planifié | Fenêtre ou campagne de rattachement, plan de retour arrière |
| À vérifier | Date d'action, méthode de vérification prévue |
| Clos | **Preuve** conforme au §2.9 |
| Déprioritisé | Motif parmi les quatre du §16.6, **date de revue** |
| Dérogation | Les sept champs du §7.4 |

### 17.7 Les issues possibles, et la preuve attendue pour chacune

| Issue | Signification | Preuve exigée |
|---|---|---|
| **Corrigé** | Le correctif est appliqué et effectif | État constaté sur l'actif, postérieur à l'action (§2.9) |
| **Atténué** | Le risque est réduit sans correction | Description de la mesure, vérification qu'elle est active, **date d'expiration** |
| **Dérogation** | Décision de ne pas corriger, bornée | Fiche complète signée par le propriétaire métier |
| **Faux positif** | Le constat était erroné | **Démonstration**, pas affirmation : révision vérifiée, capture, avis éditeur |
| **Risque accepté** | Décision définitive de ne pas traiter | Signature au niveau approprié, revue périodique |
| **Sans objet** | L'actif n'existe plus | Preuve de décommissionnement (ch. 35) |

⚠️ **PIÈGE — le faux positif déclaré sans démonstration**
C'est la fuite la plus commune d'un processus de remédiation. Un constat gênant est marqué « faux positif » et disparaît. Sans preuve jointe, cette issue devient un moyen de vider la file sans travailler. **La règle** : un faux positif se clôt avec une démonstration vérifiable par un tiers, et un échantillon de faux positifs est recontrôlé chaque trimestre.

### 17.8 Vérification et clôture

La règle est brutale et sans exception : **on ne clôt pas sur déclaration, on clôt sur preuve**.

| Méthode de vérification | Fiabilité | Usage |
|---|---|---|
| Nouveau scan de l'actif | Bonne | Méthode par défaut |
| Relevé direct de l'état (§2.9) | **Meilleure** | Actifs critiques, campagnes importantes |
| Rapport de l'outil de déploiement | Correcte, sous les trois conditions du §2.9 | Volume |
| Déclaration du propriétaire | **Insuffisante seule** | Jamais comme unique preuve |

**Le délai de vérification** doit être borné : un ticket qui reste en état « à vérifier » plus de X jours est en réalité non clos, et il pollue les indicateurs en donnant l'illusion que le travail est fait. Suivez cet état comme un indicateur à part entière.

### 17.9 Réouverture et récurrence

**Une vulnérabilité corrigée qui réapparaît** est l'un des signaux les plus riches du MCS, et l'un des moins exploités.

**Les cinq causes racines**, avec leur remède :

| Cause | Mécanisme | Remède |
|---|---|---|
| **Image de référence non corrigée** | Chaque nouvelle machine naît vulnérable | Corriger le modèle, pas les instances (ch. 28) |
| **Restauration de sauvegarde** | Retour à un état antérieur au correctif | Contrôle post-restauration systématique |
| **Redéploiement automatique** | La définition déployée pointe une version ancienne | Corriger la définition, pas l'instance |
| **Retour arrière non suivi** | Un retour arrière a annulé le correctif sans que le ticket soit rouvert | Lier retour arrière et réouverture automatique |
| **Réinstallation manuelle** | Procédure d'installation obsolète | Mettre à jour la procédure |

**Le point d'organisation décisif** : une réapparition doit **rouvrir le ticket d'origine**, pas en créer un nouveau. Sinon la récurrence est invisible — chaque occurrence semble être un problème neuf — et la cause racine n'est jamais traitée. Un ticket rouvert trois fois est un signal, un ticket créé trois fois est du bruit.

✅ **BONNE PRATIQUE (P1)** — Suivez le **taux de récurrence** : constats réapparus rapportés aux constats clos sur la période. Un taux élevé n'indique pas une mauvaise exécution de la correction, il indique presque toujours un problème d'image de référence ou de processus de déploiement — donc un gain considérable si vous le traitez.

### 17.10 Piloter le *backlog*

Le *backlog* est l'ensemble des constats ouverts. Trois lectures en donnent l'état réel.

**Le vieillissement.** Répartition des constats ouverts par tranche d'ancienneté :

| Tranche | Lecture |
|---|---|
| < 30 j | Flux normal |
| 30-90 j | Zone d'attention |
| 90-180 j | Difficulté structurelle : dépendance externe, effort sous-estimé, propriétaire absent |
| > 180 j | **Ce ne sont plus des constats, ce sont des dérogations non formalisées** |

La dernière ligne est la plus importante du chapitre. Un constat ouvert depuis plus de six mois sans décision formelle est une acceptation de risque **de fait**, prise par personne, revue par personne. La bonne action n'est pas de le corriger en urgence : c'est de le **qualifier** — dérogation, dépriorisation, ou correction planifiée avec engagement.

**L'écoulement.** Comparer entrées et sorties par période. Trois régimes possibles : la file se résorbe, elle est stable, elle grossit. Un *backlog* qui grossit malgré un travail intense signale un problème de capacité ou de périmètre, pas d'effort — et c'est un constat pour le comité stratégique.

**L'escalade.** Trois déclencheurs automatiques, sans intervention humaine : dépassement d'échéance, âge supérieur à un seuil, suspension prolongée. L'escalade suit les niveaux du §9.1.

### 17.11 Synchroniser scanner, outil de tickets et inventaire

Trois systèmes, trois référentiels d'actifs, trois vérités possibles. Les ruptures classiques :

| Rupture | Symptôme | Prévention |
|---|---|---|
| Identifiants d'actifs divergents | Le même serveur apparaît sous trois noms | Identifiant pivot commun (§10.3, §15.7) |
| Constat corrigé, ticket toujours ouvert | Le scan a détecté la correction, le ticket ne le sait pas | Synchronisation périodique de l'état |
| Ticket clos, constat toujours présent | Clôture sans vérification (§17.8) | Interdire la clôture sans preuve |
| Actif décommissionné, tickets orphelins | Tickets sur une machine qui n'existe plus | Chaînage avec le processus de décommissionnement (ch. 35) |
| Historique perdu au changement d'outil | Impossible de démontrer un progrès | Export périodique en format ouvert (§15.12) |

✅ **BONNE PRATIQUE (P0)** — **L'inventaire fait autorité.** Le scanner et l'outil de tickets s'y réfèrent, ils ne créent pas d'actifs. Toute divergence est un écart d'inventaire à traiter selon le §10.3, pas une bizarrerie d'outil à contourner.

### 17.12 📌 Ce qu'un outil de gestion ne réglera jamais

- **L'absence de propriétaire.** Un outil qui ne sait pas à qui affecter produit une file d'attente, pas une remédiation.
- **L'insuffisance de capacité.** Un *backlog* qui grossit ne se résout pas par une meilleure gestion du *backlog*.
- **La qualité de la preuve.** Un outil enregistre ce qu'on lui donne ; il ne vérifie rien.
- **Le contournement.** Si le processus est trop lourd, les corrections se feront hors outil, et vous perdrez à la fois la trace et la mesure. Le formalisme doit rester proportionné : dans une petite structure, une ligne dans un tableau tenu à jour vaut mieux qu'un outil que personne ne remplit.

### 17.13 ✅ Livrable — Le workflow de remédiation

**Ce qui doit être écrit et validé**, et qui constitue l'Annexe J :

1. Le **modèle d'états** du §17.6 et ses transitions autorisées.
2. Les **champs obligatoires** par état.
3. Les **règles de déduplication** et le modèle parent / enfants.
4. Les **règles d'échéance** : point de départ, suspensions limitatives, seuils d'escalade.
5. Les **issues possibles** et la preuve exigée pour chacune.
6. Les **règles de réouverture**.
7. Le **contrat de service interne** : délai de contestation d'affectation, délai de réponse, suppléance.

### 17.14 🔴 FIL ROUGE — mars 2027 : 3 800 constats, 21 campagnes, 187 tickets

Les 3 800 constats du scan de janvier, triés en février (§16.11), doivent maintenant être suivis. Malik Ferhaoui applique le modèle parent / enfants.

**La transformation du volume :**

| Étape | Volume |
|---|---|
| Constats bruts | 3 800 |
| Après déduplication par identifiant de vulnérabilité | 612 |
| Après regroupement par correctif | 244 |
| Après extraction des campagnes | **187 tickets + 21 campagnes** |

Les 187 tickets se répartissent en 23 en traitement unitaire, 140 déprioritisés avec date de revue, et 24 en attente d'un correctif éditeur — compteur suspendu, relance mensuelle.

**Le vieillissement révèle ce que le triage ne montrait pas.** Onze tickets dépassent 180 jours : ils datent des premiers scans de février 2026 et n'ont jamais été traités ni qualifiés. Ils concernent tous le même progiciel métier, dont l'éditeur exige une montée de version majeure facturée. Personne n'avait pris la décision — le sujet flottait entre l'exploitation, le métier et les achats.

Claire applique la règle du §17.10 : ce ne sont pas des constats en retard, ce sont des **dérogations non formalisées**. Elle les transforme en une dérogation unique, motivée, compensée par une restriction d'accès réseau, signée par le propriétaire métier, avec une date d'expiration alignée sur le budget 2028. Le *backlog* perd onze lignes ; l'organisation gagne une décision.

**Une découverte inattendue.** Le taux de récurrence sur les postes de travail atteint 18 % : près d'un constat clos sur cinq réapparaît dans les trois mois. L'analyse des cinq causes du §17.9 en identifie une seule : le modèle de machine virtuelle de mars 2024 (§3.9), jamais mis à jour. Chaque nouveau serveur créé depuis reproduit mécaniquement les mêmes constats. Corriger le modèle prend une demi-journée et supprime une source permanente de travail — ce que trois campagnes successives n'avaient pas réussi à faire.

**Ce que le comité retient.** Le nombre de « vulnérabilités ouvertes » a cessé d'être l'indicateur de référence. Il est remplacé par trois mesures : campagnes en cours et leur avancement, tickets dépassant leur échéance, et âge du plus ancien constat non qualifié. Ce dernier chiffre, en particulier, ne peut pas être embelli.

**Livrable de l'épisode.** Le workflow de remédiation d'HELIOMED, avec son modèle d'états et ses règles d'escalade — Annexe J.

→ La suite en 🔴 §18.14, lors de la nuit du déploiement raté sur le cluster de bases de données.

→ **Chapitre 18 — Le processus de correctif de bout en bout** : la chaîne complète d'un correctif, de la qualification à la preuve.

### Synthèse mentale du chapitre 17

Entre la décision de triage et la correction effective, le constat doit exister comme objet de gestion, avec un propriétaire, une échéance et un état — faute de quoi le travail se perd, se duplique et ne se démontre pas. Le modèle parent/enfants et quatre règles de déduplication transforment des milliers de constats en dizaines de tickets, à condition de regrouper par action de correction et non par ressemblance. Mesurez deux délais séparément : depuis la publication du correctif, qui donne votre exposition réelle, et depuis la détection, qui donne votre réactivité — leur écart mesure gratuitement la fraîcheur de votre détection. Chaque issue exige sa preuve, et le faux positif déclaré sans démonstration est la fuite la plus commune d'un processus de remédiation. Une réapparition rouvre le ticket d'origine, sinon la récurrence reste invisible et sa cause racine — presque toujours une image de référence — n'est jamais traitée. Enfin, un constat ouvert depuis plus de six mois sans décision formelle est une acceptation de risque prise par personne : la bonne action est de le qualifier, pas de le corriger en urgence.

**Trois questions de vérification**

1. Votre file contient 3 800 constats. Décrivez les quatre étapes qui la ramènent à un nombre de tickets gérable, et le critère qui doit gouverner tout regroupement.
2. Un constat est clos comme faux positif. Que devez-vous exiger avant d'accepter cette clôture, et quel contrôle périodique mettez-vous en place ?
3. 18 % des constats clos sur les postes réapparaissent dans les trois mois. Quelles causes racines examinez-vous, dans quel ordre, et pourquoi corriger l'instance est-il ici une perte de temps ?

---

## Chapitre 18 — Le processus de correctif de bout en bout

### 18.1 La chaîne complète

Neuf étapes, dont trois sont systématiquement escamotées : la qualification du correctif, la vérification post-déploiement, et la production de preuve.

```
1. Identification   → le constat existe et est qualifié (ch. 14-16)
2. Qualification    → que contient ce correctif, et qu'est-ce qu'il casse ?
3. Acquisition      → obtenir le correctif par un canal de confiance (§2.3)
4. Validation       → tester sur un environnement représentatif (§6.12)
5. Planification    → fenêtre, anneaux, plan de retour arrière
6. Déploiement      → progressif, avec critères d'arrêt
7. Vérification     → l'état constaté a-t-il changé ? (§2.9)
8. Clôture          → issue et preuve (§17.7)
9. Preuve           → archivage exploitable en audit (ch. 39)
```

**La règle de proportionnalité.** Les neuf étapes ne s'appliquent pas avec la même profondeur à tout. Un correctif de navigateur sur un poste C3 et une montée de version d'hyperviseur C1 suivent le même chemin, avec des exigences très différentes à chaque étape. La classe de service (§7.2) détermine cette profondeur — c'est à cela qu'elle sert.

### 18.2 Qualifier un correctif avant de le déployer

**Les six questions**, dont les réponses se trouvent dans les notes de version, la base de connaissances de l'éditeur et les retours de la communauté :

| Question | Où chercher | Pourquoi |
|---|---|---|
| Que corrige-t-il exactement ? | Notes de version | Vérifier qu'il traite bien votre constat |
| Quels **prérequis** exige-t-il ? | Notes de version | Un correctif qui exige un niveau antérieur non installé échouera silencieusement |
| Quelles **régressions** sont signalées ? | Base de connaissances, forums, retours communautaires | C'est l'information la plus rentable de la liste |
| Nécessite-t-il un **redémarrage** ? | Notes de version | Détermine la fenêtre nécessaire |
| Est-il **désinstallable** ? | Documentation, test | Détermine le plan de retour arrière (§2.5) |
| Y a-t-il un **effet différé** ? | Notes de version | Le correctif à activation différée du §2.8 |

⚠️ **PIÈGE — le correctif déjà connu comme problématique**
Beaucoup de régressions sont signalées publiquement dans les 48 à 72 heures suivant la publication. Une organisation qui déploie systématiquement dans les 24 heures s'expose à des problèmes que d'autres ont déjà documentés. C'est l'argument principal en faveur d'un **délai d'observation** avant le premier anneau — sauf urgence caractérisée (chapitre 21), où le calcul s'inverse.

### 18.3 Valider : environnements et jeux de tests

Le §6.12 a posé le problème de la représentativité. Voici la mise en œuvre.

**Trois niveaux de validation**, selon la classe de service :

| Niveau | Contenu | Pour quelle classe |
|---|---|---|
| **Aucune** | Déploiement direct en anneau pilote | C3, correctifs de sécurité courants |
| **Fonctionnelle** | Tests métier sur environnement de recette | C2 |
| **Complète** | Recette + tests de non-régression + validation métier formelle | C1, montées de version |

**Le délai d'observation** est un outil distinct des tests, et souvent plus efficace : laisser passer un temps défini entre la publication et le déploiement, pendant lequel les régressions apparaissent chez d'autres. Un délai de 3 à 7 jours capte l'essentiel des problèmes signalés publiquement, pour un coût nul.

✅ **BONNE PRATIQUE (P1)** — Formalisez ce délai dans la politique, avec sa dérogation : *délai d'observation de 5 jours, sauf vulnérabilité activement exploitée où il est ramené à zéro*. Cela transforme un comportement implicite en règle explicite, et cela évite la discussion à chaque campagne.

🖼 **SCHÉMA — Anneaux de déploiement et critères de passage.** *Cinq anneaux concentriques ou en cascade, avec la durée d'observation et le critère de passage entre chacun.*

### 18.4 Le déploiement par anneaux

**Le principe.** Découper le parc en populations successives, avec un critère de passage entre chacune.

| Anneau | Population | Taille indicative | Durée d'observation |
|---|---|---|---|
| 0 — Laboratoire | Machines de test | Quelques unités | 1 à 3 jours |
| 1 — Pilote | Volontaires, équipe informatique | 2 à 5 % | 3 à 5 jours |
| 2 — Représentatif | Échantillon couvrant tous les profils métier | 10 à 20 % | 3 à 7 jours |
| 3 — Général | Le reste | 75 à 85 % | — |
| 4 — Sensibles | Actifs critiques, cas particuliers | Quelques unités | Traitement unitaire |

**Les deux erreurs de conception des anneaux :**

1. **L'anneau pilote non représentatif.** Composé uniquement de machines de l'équipe informatique, il ne teste ni les applications métier, ni les configurations réelles, ni les usages. Il valide qu'un correctif s'installe, pas qu'il ne casse rien.
2. **L'absence de critère de passage.** On passe à l'anneau suivant « parce que ça semble aller ». Le critère doit être écrit, mesurable et vérifié : taux d'installation réussie, absence d'incident déclaré, indicateurs fonctionnels stables (§6.8).

**Les critères d'arrêt automatiques**, définis avant le déploiement :

```
Arrêt de la campagne si l'une de ces conditions est atteinte :
  · taux d'échec d'installation      > 5 %
  · incidents déclarés liés          ≥ 3 sur l'anneau
  · indicateur fonctionnel           baisse > 10 % sur 30 min
  · redémarrages inattendus          ≥ 2 machines
```

### 18.5 Ordre des opérations et dépendances

**Redémarrer quoi ?** Trois niveaux, du moins au plus coûteux : le **processus** (rechargement du binaire), le **service** (arrêt et relance du démon), le **système** (redémarrage complet). Le §2.6 fournit les commandes pour savoir lequel est nécessaire. Choisir le niveau minimal suffisant divise le coût d'une campagne.

**L'ordre entre composants.** Une chaîne applicative se met à jour dans un ordre déterminé par les dépendances : en général, du plus profond au plus superficiel — base de données, puis services applicatifs, puis frontaux — sauf indication contraire de l'éditeur. Un ordre inversé produit des erreurs de compatibilité pendant la transition.

**Les quatre opérations connexes** systématiquement oubliées dans les plans de campagne :

| Opération | Pourquoi elle compte |
|---|---|
| **Drainage des connexions** | Arrêter un service avec des sessions actives produit des erreurs visibles côté utilisateur |
| **Invalidation de cache** | Un cache contenant l'ancien comportement peut annuler l'effet du correctif ou produire des incohérences |
| **Bascule de cluster** | Ordre, temporisation, vérification de la synchronisation avant de basculer le second membre (§2.7) |
| **Réindexation ou migration de données** | Peut prendre des heures et n'est pas interruptible |

### 18.6 Contraintes d'infrastructure

Trois contraintes physiques qui font échouer des campagnes correctement conçues :

- **La bande passante.** Un correctif cumulatif de plusieurs centaines de mégaoctets multiplié par le nombre de postes d'un site distant saturera la liaison. Remède : cache local, distribution entre pairs, ou déploiement échelonné par site.
- **Le démarrage massif simultané.** Programmer le redémarrage de centaines de machines virtuelles à la même minute sature le stockage et allonge le démarrage de plusieurs dizaines de minutes. Remède : échelonnement aléatoire sur une plage.
- **La capacité en mode dégradé.** Corriger un cluster suppose de fonctionner temporairement avec un membre en moins (§6.3). Si la capacité restante ne suffit pas, la campagne provoque une dégradation de service.

### 18.7 Migrations et correctifs non réversibles

Le §6.7 a traité les migrations de schéma. Deux règles opérationnelles en découlent :

1. **Identifier le point de non-retour avant de commencer**, et l'écrire dans la demande de changement. La question exacte : *à partir de quel instant un retour arrière exigera-t-il une restauration de données ?*
2. **Vérifier la réversibilité réelle du correctif** (§2.5) sur une machine représentative, avant la campagne — pas pendant l'incident.

### 18.8 Le plan de retour arrière

| Élément | Exigence |
|---|---|
| Mécanisme | Nommé explicitement : instantané, sauvegarde, redéploiement, désinstallation vérifiée |
| **Durée mesurée** | Chronométrée lors du test. C'est cette durée qui décide si vous osez déployer |
| Point de non-retour | Identifié et daté |
| Décideur | Qui décide du retour arrière, et sur quel critère |
| Vérification post-retour | Comment s'assurer que l'état antérieur est bien restauré |

⚠️ **PIÈGE — le plan de retour arrière jamais testé**
Un plan non testé n'est pas un plan. Le test doit être fait au moins une fois par type d'actif et par mécanisme, et refait après tout changement significatif de l'environnement.

### 18.9 Vérification post-déploiement

Trois vérifications distinctes, souvent confondues :

| Vérification | Question | Méthode |
|---|---|---|
| **Technique** | Le correctif est-il appliqué ? | État constaté (§2.9) |
| **Effectivité** | Le code corrigé s'exécute-t-il ? | Redémarrage confirmé (§2.6) |
| **Fonctionnelle** | Le service fait-il toujours son travail ? | Indicateur fonctionnel (§6.8) |

La troisième est celle qui manque presque toujours, et c'est celle qui détecte les régressions silencieuses.

### 18.10 La traîne longue

Toute campagne laisse un résidu : machines éteintes, nomades absents, actifs en échec, cas particuliers. Ce résidu représente typiquement 2 à 5 % du parc, et il concentre une part disproportionnée des risques.

**Le traitement à trois niveaux :**

1. **Relance automatique** pendant une période définie — la majorité du résidu se résorbe seule.
2. **Traitement manuel** du reste, actif par actif, avec identification de la cause.
3. **Qualification formelle** de ce qui résiste : dérogation (§7.4) ou décommissionnement (chapitre 35).

**La règle** : une campagne n'est pas close tant que sa traîne longue n'est pas qualifiée. Une campagne « terminée à 97 % » avec 3 % non qualifiés est une campagne dont la partie la plus risquée n'a pas été traitée.

### 18.11 ⚠️ Quand le correctif casse

Les mises à jour défectueuses existent, y compris chez les éditeurs majeurs, et y compris sur des correctifs de sécurité. La doctrine à tenir n'est ni la naïveté ni l'immobilisme.

| Ce qui ne marche pas | Ce qui marche |
|---|---|
| Déployer immédiatement partout | Anneaux + délai d'observation + critères d'arrêt |
| Ne jamais déployer avant plusieurs mois | Délai borné et différencié par classe |
| Décider au cas par cas dans l'urgence | Doctrine écrite, avec dérogation prévue pour l'urgence |

**Le calcul à faire dans chaque cas**, et il est explicite : comparer le risque du correctif (probabilité de régression × impact de l'indisponibilité) et le risque du non-correctif (probabilité d'exploitation × impact de la compromission). Ce calcul est le sujet entier du cas de synthèse C.

### 18.12 🔬 Mini-lab 5 — Concevoir des anneaux de déploiement

**Objectif** — Découper un parc en anneaux réellement représentatifs et définir des critères de passage vérifiables.
**Durée** 45 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §18.4, §6.8 · **Livrable** tableau d'anneaux + grille de critères (D.6).
**Compétences validées** — ✔ composer un anneau pilote représentatif ✔ écrire des critères de passage vérifiables ✔ traiter une population intermittente ✔ arbitrer une échéance intenable plutôt que la subir

**Données fournies — parc de 340 postes**

| Population | Nb | Particularités | Applications métier critiques | Connexion réseau interne |
|---|---|---|---|---|
| Siège — bureautique | 180 | Poste standard, droits utilisateur | Gestion commerciale, paie (RH only) | Permanente |
| Siège — direction et RH | 22 | Données sensibles | Paie, gestion documentaire | Permanente |
| R&D Nantes | 90 | Droits d'administration locaux, environnements de développement, machines puissantes | Chaîne de développement, outils de build | Permanente |
| Commerciaux nomades | 40 | Se connectent 2 à 6 fois/mois | Gestion commerciale, hors ligne partiel | **Intermittente** |
| Site industriel — bureautique | 19 | Horaires 3×8, arrêts de ligne à éviter | Suivi de production (lecture) | Permanente |
| Site industriel — supervision | 11 | **Classe C4**, validation constructeur requise | Conduite de ligne | Réseau industriel |

**Contraintes** : la campagne doit être terminée en 21 jours · l'équipe dispose de 2 personnes · le correctif exige un redémarrage · deux régressions sur la gestion commerciale ont été signalées publiquement dans les 48 h suivant la publication.

**Questions**
(a) Proposez un découpage en anneaux, avec effectifs et justification.
(b) Écrivez les critères de passage entre anneaux.
(c) Traitez les nomades.
(d) Traitez les 11 postes de supervision.
(e) La contrainte de 21 jours est-elle tenable ? Que faites-vous si elle ne l'est pas ?

---

**Corrigé commenté**

**(a) Découpage proposé**

| Anneau | Composition | Nb | Durée d'observation | Justification |
|---|---|---|---|---|
| **0 — Laboratoire** | 4 machines de test, dont 1 image R&D | 4 | 1 j | Valide l'installation, pas l'usage |
| **1 — Pilote représentatif** | 6 siège bureautique · 4 R&D · **2 commerciaux** · 1 industriel bureautique | 13 | 3 j | **Les quatre profils dès le pilote** |
| **2 — Élargi** | 40 siège · 20 R&D · 10 commerciaux · 6 industriel | 76 | 5 j | Couvre les applications métier en usage réel |
| **3 — Général** | Reste siège (134) + reste R&D (66) | 200 | — | Volume |
| **4 — Sensibles et contraints** | 22 direction/RH · 12 industriel bureautique restant | 34 | Unitaire | Données sensibles, horaires 3×8 |
| **Hors anneaux** | 11 supervision C4 | 11 | — | Régime distinct |
| **Population séparée** | 28 nomades restants | 28 | Suivi propre | Voir (c) |

**Pourquoi la direction et les RH en anneau 4 et non en anneau 1** : ils portent les données les plus sensibles, et une régression sur la paie a un coût politique disproportionné. Ils bénéficient de l'observation faite sur les 289 postes précédents.

**(b) Critères de passage — formulaire D.6 rempli**

| Indicateur | Seuil d'arrêt | Mesuré par | Fenêtre |
|---|---|---|---|
| Taux d'échec d'installation | `> 5 %` | Console de déploiement | Continu |
| Incidents déclarés liés | `≥ 3 sur l'anneau` | Support N1 | 24 h |
| **Transactions abouties — gestion commerciale** | `baisse > 10 % sur 30 min` | Supervision applicative | Continu |
| **Éditions de paie abouties** | `tout échec` | Supervision applicative | Continu (anneau 4) |
| Redémarrages inattendus | `≥ 2 machines` | Supervision poste | Continu |

**Critère de passage** : tous les seuils respectés pendant la durée d'observation **et** aucun incident bloquant ouvert **et** validation explicite du référent métier de la gestion commerciale pour le passage à l'anneau 3.

Le dernier point est ajouté à cause des deux régressions signalées publiquement : il est justifié ici, et ne le serait pas sur un correctif sans antécédent.

**(c) Les nomades — trois mesures**

1. **Deux d'entre eux dès l'anneau 1.** C'est là que se révèlent les problèmes de déploiement hors réseau interne : téléchargement sur liaison lente, échec de reprise, interruption pendant l'installation.
2. **Mécanisme fonctionnant sur Internet**, sans passage obligatoire par le réseau interne.
3. **Population suivie séparément**, avec une échéance plus longue (`J+45` au lieu de `J+21`) mais **mesurée**. Ils ne sont ni fondus dans le taux global, ni exclus silencieusement (§15.6).

⚠️ Une erreur fréquente consiste à leur appliquer l'échéance générale et à constater un taux de conformité dégradé chaque mois, sans jamais traiter la cause.

**(d) Les 11 postes de supervision**

Régime C4 : hors campagne. Correctif soumis à validation constructeur, application lors de la fenêtre de relève d'équipe ou de l'arrêt de production. Dans l'intervalle, compensation selon le §20.2. Ils figurent au tableau de bord comme **population distincte**, avec leur propre indicateur de compensation vérifiée — jamais fondus dans le taux général (§10.11).

**(e) La contrainte de 21 jours**

Elle n'est **pas tenable** telle quelle : 1 + 3 + 5 jours d'observation = 9 jours avant l'anneau 3, auxquels s'ajoutent le déploiement sur 200 postes, l'anneau 4 unitaire, et la traîne longue. Le calendrier réaliste est de 28 à 32 jours pour l'ensemble, hors nomades.

**Trois réponses possibles, à arbitrer explicitement** :

| Option | Effet | Coût |
|---|---|---|
| Compresser les durées d'observation à 1 j / 3 j | Gain de 4 jours | Augmente le risque de régression massive — inacceptable ici vu les antécédents |
| Paralléliser les anneaux 3 et 4 | Gain de 3 jours | Prive l'anneau 4 du bénéfice de l'observation |
| **Négocier l'échéance à 30 jours** | Calendrier tenable | Documenter le dépassement et sa justification |

La troisième est la bonne réponse dans ce cas : le constat n'est pas exploité, et le §16.5 rappelle qu'un délai qu'on ne tient pas produit une non-conformité permanente. **Un délai renégocié et documenté vaut mieux qu'un délai affiché et manqué.**

**Les trois erreurs attendues**
1. Composer l'anneau 1 uniquement de postes de l'équipe informatique : le correctif s'installera parfaitement, et la régression sur la gestion commerciale apparaîtra en anneau 3, sur 200 postes.
2. Placer la direction et les RH en anneau 1 « parce qu'ils sont peu nombreux ».
3. Accepter les 21 jours sans le dire, et livrer un taux dégradé un mois plus tard sans explication.

### 18.13 🔬 Mini-lab 6 — Produire la preuve d'une campagne

**Objectif** — Constituer un dossier de preuve recevable en audit et distinguer preuve recevable, contestable et irrecevable.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** §2.9, §18.9, §15.6 · **Livrable** dossier de preuve en six pièces (D.13).
**Compétences validées** — ✔ constituer un dossier de preuve recevable ✔ identifier le vrai dénominateur d'une campagne ✔ vérifier un état sur échantillon ✔ classer une preuve en recevable / contestable / irrecevable

**Données fournies**

Campagne `CAMP-2027-04`, correctif système sur serveurs Linux. Extraits bruts fournis :

*Extrait 1 — rapport de la console de déploiement, exporté le 22/04/2027 à 09 h 14*
```
Campagne CAMP-2027-04 — cible : groupe "SRV-LINUX-PROD"
  Succès ................ 168
  Échec ................. 5
  Non joignable ......... 3
  Total ciblé ........... 176
```

*Extrait 2 — périmètre de référence, extraction du 01/04/2027*
```
Serveurs Linux, environnement = production ....... 181
   dont couverts par la console de déploiement ... 176
   dont hors console (motif non renseigné) ....... 5
```

*Extrait 3 — détail des échecs, journal de la console*
```
srv-app-07   ERR_DISK_SPACE      /var 98% plein
srv-app-11   ERR_DISK_SPACE      /var 97% plein
srv-bdd-03   ERR_LOCK            paquet verrouillé par une transaction en cours
srv-web-09   ERR_DEPENDENCY      prérequis manquant
srv-int-02   ERR_TIMEOUT         pas de réponse après 3 tentatives
```

*Extrait 4 — non joignables*
```
srv-lab-04   dernier contact 12/02/2027
srv-old-01   dernier contact 30/11/2026
srv-tst-06   dernier contact 19/04/2027
```

**Questions**
(a) Quelles six pièces produisez-vous ?
(b) Quel est le vrai dénominateur, et que vaut le taux de réussite annoncé ?
(c) Quelle est la faiblesse d'un rapport de console seul, et comment la comblez-vous ?
(d) Traitez les 8 actifs restants **et** les 5 hors console.
(e) Classez trois formulations en preuve recevable, contestable, irrecevable.

---

**Corrigé commenté**

**(a) Le dossier en six pièces**

| # | Pièce | Contenu pour ce cas |
|---|---|---|
| 1 | Périmètre | 181 serveurs éligibles, dont 176 ciblés et **5 hors console — motif à documenter** |
| 2 | Décision | Ticket de triage, chemin dans l'arbre, échéance |
| 3 | Exécution | Extrait 1 daté et non retouché, avec les trois populations |
| 4 | **Vérification indépendante** | État constaté sur 18 serveurs tirés au sort (≈ 10 %), horodaté, méthode décrite |
| 5 | Traîne longue | Les 8 en échec ou non joignables + les 5 hors console, avec cause et échéance |
| 6 | Clôture | Date, responsable, issue, preuve rattachée |

**(b) Le dénominateur**

| Formulation | Valeur | Statut |
|---|---|---|
| « 95 % de réussite » (168/176) | 95 % | **Réussite de la campagne dans sa cible** |
| Sur les serveurs éligibles | 168/181 = **93 %** | Le chiffre à publier |
| Non mesuré | 5 hors console + 3 non joignables = **8 (4,4 %)** | À publier séparément |

Les 5 serveurs hors console sont le point le plus important de l'exercice : ils n'apparaissent **ni** dans le numérateur, **ni** dans le dénominateur de la console. C'est l'écart de type 3 du §10.3 — déclarés, actifs, jamais atteints.

**(c) La faiblesse du rapport de console**

Il rapporte ce que l'outil **croit** avoir fait. Il n'établit ni que le code corrigé s'exécute — un redémarrage a-t-il eu lieu ? — ni que la console couvre bien le périmètre éligible.

Les trois conditions de recevabilité (§2.9) : périmètre défini et rapproché du périmètre de référence · intégrité de l'extraction (datée, non retouchée) · liste des non joignables fournie. L'échantillon vérifié indépendamment est ce qui transforme un rapport en preuve.

🧪 **La vérification à réaliser sur l'échantillon**

```bash
# Sur chacun des 18 serveurs tirés au sort
dnf history info $(dnf history list | awk 'NR==3{print $1}')   # ou dpkg/apt selon la famille
uptime -s                                                       # date du dernier démarrage
needs-restarting -r ; echo "code retour : $?"                   # redémarrage encore requis ?
```

Le troisième contrôle est le plus important : un correctif installé sans redémarrage laisse le code vulnérable en mémoire (§2.6).

**(d) Traitement des 13 actifs**

| Groupe | Cause | Action | Échéance |
|---|---|---|---|
| srv-app-07, srv-app-11 | Espace disque | Libérer `/var`, relancer. **Cause racine** : aucune supervision de l'espace disque sur ces serveurs | 48 h |
| srv-bdd-03 | Transaction verrouillée | Relancer hors fenêtre de traitement | 48 h |
| srv-web-09 | Prérequis manquant | Installer le prérequis puis relancer. Vérifier si d'autres serveurs sont concernés | 5 j |
| srv-int-02 | Pas de réponse | Vérifier l'état de la machine — agent, réseau, ou machine arrêtée | 5 j |
| srv-lab-04, srv-old-01 | Sans contact depuis 2 et 5 mois | **Candidats au décommissionnement** (§10.3) — vérifier l'existence, sinon PV | 15 j |
| srv-tst-06 | Sans contact depuis 3 jours | Probablement éteint temporairement : relance automatique | 15 j |
| **5 serveurs hors console** | **Motif non renseigné** | **Priorité maximale** : les rattacher à la console ou documenter l'exclusion | 10 j |

**(e) Recevable, contestable, irrecevable**

| Formulation | Statut | Pourquoi |
|---|---|---|
| « Rapport de console du 22/04/2027 09 h 14, périmètre 176 serveurs rapproché des 181 éligibles, 3 non joignables listés, complété d'un relevé d'état horodaté sur 18 serveurs tirés au sort » | **Recevable** | Périmètre, intégrité, non joignables, vérification indépendante |
| « Rapport de console : 95 % de réussite » | **Contestable** | Exact, mais sans périmètre ni dénominateur : l'auditeur demandera les 5 % et les 5 serveurs hors console |
| « L'équipe confirme que la campagne s'est bien déroulée » | **Irrecevable** | Déclaration sans donnée (§5.6) |

**Les deux erreurs attendues**
1. Publier 95 % sans mentionner les 5 serveurs hors console — le chiffre est exact et le périmètre est faux.
2. Considérer la campagne close à 95 % : les 4,4 % non traités concentrent l'essentiel du risque résiduel (§18.10).

### 18.14 🔴 FIL ROUGE — avril 2027 : la nuit du déploiement raté

Campagne de montée de version mineure sur le cluster de bases de données d'HelioLink — trois nœuds, classe C1. Correctif de sécurité, vulnérabilité non exploitée mais gravité élevée, échéance à 30 jours.

**Ce qui était prévu.** Fenêtre samedi 22 h - 2 h. Test préalable en recette : concluant. Retour arrière annoncé par instantané des trois machines virtuelles. Malik Ferhaoui et un ingénieur d'astreinte.

**Ce qui s'est passé.** À 22 h 40, le premier nœud est mis à jour et redémarre normalement. À 22 h 55, la réplication ne repart pas : les deux versions ne se synchronisent pas. Le correctif embarquait une modification du format de réplication, mentionnée en dernière ligne des notes de version, sous une rubrique que personne n'avait lue.

À 23 h 10, décision de retour arrière. L'instantané est restauré : le nœud revient à sa version antérieure. Mais la réplication ne repart toujours pas — le nœud restauré est désormais en retard de quarante minutes de transactions, et le mécanisme de rattrapage automatique refuse de s'engager au-delà d'un certain écart.

À 1 h 20, après une resynchronisation complète manuelle, le service est rétabli. Aucune donnée perdue. Quatre heures d'indisponibilité de la plateforme de télésuivi, un dimanche matin — période de faible usage, mais deux établissements clients ont appelé le support.

**Les quatre causes racines identifiées au retour d'expérience :**

| Cause | Ce qui aurait évité |
|---|---|
| Notes de version lues en diagonale | La qualification en six questions du §18.2, notamment « quels prérequis » |
| Test en recette sur un **nœud unique**, pas sur un cluster | L'écart de représentativité du §6.12, non mesuré |
| Plan de retour arrière testé sur une machine isolée | Le test du §18.8 sur un actif **représentatif**, cluster inclus |
| Aucun critère d'arrêt écrit | La décision de retour arrière a pris 15 minutes de discussion |

**Ce qui n'a pas mal fonctionné**, et que Claire Nadeau tient à souligner au comité : la fenêtre était correcte, l'astreinte était en place, l'instantané existait, et aucune donnée n'a été perdue. L'incident aurait pu être bien pire sans ces éléments.

**Les trois mesures.**

1. La qualification en six questions devient un **champ obligatoire** du dossier de campagne pour toute classe C1 — avec la référence exacte de la section des notes de version consultée.
2. Le test de retour arrière doit être réalisé **sur une topologie représentative**. L'écart entre recette et production est désormais mesuré sur les quatre axes du §6.12 et affiché dans le dossier de campagne.
3. Les critères d'arrêt et le décideur sont écrits **avant** l'intervention, dans la demande de changement.

**Livrable de l'épisode.** Le dossier de campagne standard d'HELIOMED, en Annexe D : qualification, écart de représentativité, anneaux, critères d'arrêt, plan de retour arrière chronométré, décideur nommé.

→ La suite en 🔴 §19.11, quand il faudra choisir l'outillage capable de porter tout cela.

→ **Chapitre 19 — Outillage de déploiement par plateforme** : l'outillage — familles, critères de choix et limites structurelles.

### Synthèse mentale du chapitre 18

Neuf étapes composent la chaîne, dont trois sont systématiquement escamotées : qualifier le correctif, vérifier après déploiement, produire la preuve. La qualification en six questions coûte quinze minutes et évite l'essentiel des incidents — la question des régressions déjà signalées est la plus rentable. Le délai d'observation est un outil distinct des tests, et souvent plus efficace pour un coût nul. Les anneaux échouent pour deux raisons : un pilote non représentatif, qui valide qu'un correctif s'installe et non qu'il ne casse rien, et l'absence de critère de passage écrit. Le plan de retour arrière doit être chronométré, car c'est sa durée mesurée qui décide si vous osez déployer. La vérification fonctionnelle est celle qui manque toujours et qui détecte les régressions silencieuses. Enfin, une campagne n'est pas close tant que sa traîne longue n'est pas qualifiée : ces 3 % concentrent une part disproportionnée du risque.

**Trois questions de vérification**

1. Citez les trois étapes de la chaîne les plus souvent escamotées et, pour chacune, la conséquence concrète de son absence.
2. Votre anneau pilote est composé des postes de l'équipe informatique. Qu'est-ce que cela valide réellement, et qu'est-ce que cela laisse passer ?
3. Une campagne affiche 97 % de réussite. Pourquoi ne pouvez-vous pas la clore, et que devez-vous produire sur les 3 % restants ?

---

## Chapitre 19 — Outillage de déploiement par plateforme

> **Note de lecture.** Ce chapitre traite des **familles d'outils**, de leurs mécanismes et de leurs limites structurelles. Les outils nommés, leurs modèles de licence et leurs limites propriétaires figurent en **Annexe E**, qui est datée et versionnée. Cette séparation est délibérée : les mécanismes ci-dessous resteront valables quand les produits auront changé.

### 19.1 La grille de choix, indépendante des produits

Neuf critères suffisent à évaluer n'importe quel outil de déploiement, et à comprendre pourquoi aucun ne suffit seul.

| Critère | Question | Piège fréquent |
|---|---|---|
| **Couverture** | Quels systèmes, quelles applications tierces, quels micrologiciels ? | La couverture annoncée inclut rarement les applications métier |
| **Hors domaine** | Gère-t-il les machines non jointes à l'annuaire ? | C'est précisément là que sont les actifs à risque |
| **Itinérance** | Fonctionne-t-il sans réseau interne ? | Sinon, les nomades décrochent (§18.12) |
| **Bande passante** | Cache local, distribution entre pairs, limitation ? | Sites distants saturés |
| **Granularité** | Peut-on cibler par anneau, par attribut, par exclusion ? | Sans cela, pas d'anneaux (§18.4) |
| **Critères d'arrêt** | Peut-on suspendre automatiquement une campagne ? | Rarement natif ; souvent à construire |
| **Reporting** | Peut-on exporter les données brutes, avec les non joignables ? | Le calcul honnête du §15.6 est souvent impossible nativement |
| **Réversibilité** | Peut-on revenir en arrière, et l'outil le trace-t-il ? | Dépend surtout de la plateforme (§2.5) |
| **Coût et dépendance** | Modèle de licence, portabilité de l'historique | L'historique est rarement exportable |

**Le critère décisif à long terme est le septième.** Un outil qui ne permet pas d'exporter ses données brutes vous empêche de calculer vos propres indicateurs (chapitre 38), de constituer une preuve indépendante (§2.9), et de changer de fournisseur sans perdre votre antériorité.

### 19.2 Écosystème Windows

**Les mécanismes.** Quatre approches coexistent, souvent combinées dans un même parc :

| Approche | Principe | Adaptée à |
|---|---|---|
| **Service de mise à jour interne** | Un serveur relaie et approuve les correctifs de l'éditeur | Parcs sur site, contrôle fin des approbations |
| **Gestion de configuration d'entreprise** | Déploiement centralisé, applications tierces incluses | Grands parcs, besoins de granularité |
| **Gestion de flotte depuis le cloud** | Politiques appliquées aux machines où qu'elles soient | Nomades, hors domaine, parcs distribués |
| **Anneaux natifs de l'éditeur** | Découpage et échelonnement gérés par le service de l'éditeur | Postes standards, faible charge d'administration |

**Les trois points d'attention propres à Windows :**

1. **Les applications tierces ne sont pas couvertes par défaut.** Navigateurs, lecteurs, environnements d'exécution, clients d'accès distant représentent une part majeure des vulnérabilités exploitées sur poste, et exigent un mécanisme complémentaire (§19.5).
2. **Le redémarrage se pilote séparément** du déploiement. Un correctif installé et jamais redémarré n'est pas effectif — et les machines qui ne redémarrent jamais sont fréquentes.
3. **La réversibilité ne se présume pas** (§2.5).

### 19.3 Écosystème Linux

| Mécanisme | Principe | Point d'attention |
|---|---|---|
| **Dépôts internes et miroirs** | Vous maîtrisez ce qui est publié et quand | Le miroir doit lui-même être maintenu et synchronisé |
| **Mise à jour non supervisée** | Le système applique seul les correctifs de sécurité | Efficace sur C3 ; à encadrer sur C1 (redémarrages, régressions) |
| **Gestion de configuration** | Un outil applique un état désiré sur un parc | Le plus flexible ; exige des compétences et du maintien |
| **Orchestration des redémarrages** | Détection et planification des redémarrages nécessaires | C'est ici que les campagnes Linux échouent (§2.6) |

⚠️ **PIÈGE — la mise à jour automatique sans orchestration du redémarrage**
Configuration très répandue : les correctifs s'appliquent automatiquement, personne ne redémarre les services, et l'organisation croit son parc à jour. Les bibliothèques corrigées sur disque continuent d'être exécutées en version vulnérable, parfois pendant des mois.

### 19.4 macOS et mobiles

Trois particularités : les mises à jour sont **imposées par l'éditeur** avec peu de latitude de report ; le déploiement passe par une solution de gestion de flotte, sans équivalent des dépôts internes ; et l'utilisateur conserve souvent un pouvoir de report, ce qui rend la conformité dépendante de son comportement.

**La conséquence pour le MCS** : sur ces plateformes, vous pilotez surtout par la **politique** (exiger une version minimale pour accéder aux ressources) plutôt que par le déploiement. L'accès conditionnel fondé sur le niveau de mise à jour est le levier réel — traité au §28.8.

### 19.5 Applications tierces : le trou noir du poste de travail

**Le constat.** Une part majeure des vulnérabilités réellement exploitées sur les postes concerne des applications tierces : navigateurs et leurs extensions, lecteurs de documents, environnements d'exécution, outils de compression, clients d'accès distant, utilitaires métier.

**Pourquoi elles échappent au dispositif :** elles ne sont pas couvertes par le mécanisme natif du système ; elles sont souvent installées hors processus ; leur inventaire est incomplet ; et elles se mettent à jour chacune selon son propre mécanisme, parfois en demandant des droits d'administration.

**Les trois approches**, par efficacité :

| Approche | Principe | Limite |
|---|---|---|
| Gestionnaire de paquets pour Windows | Catalogue centralisé, déploiement et mise à jour scriptables | Couverture du catalogue variable selon les applications métier |
| Module de mise à jour d'applications tierces intégré à l'outil de déploiement | Cohérence avec le reste du dispositif | Souvent une option payante, catalogue limité |
| Mise à jour automatique native de l'application | Aucun effort | Aucun contrôle, aucune visibilité, aucune preuve |

✅ **BONNE PRATIQUE (P0)** — Commencez par **inventorier** les applications tierces installées sur un échantillon de postes. La liste est presque toujours plus longue et plus ancienne qu'attendu, et cet inventaire suffit à justifier le budget du mécanisme de déploiement correspondant.

### 19.6 Réseau, sécurité et hyperviseurs

Ces plateformes se distinguent par l'absence d'outil de déploiement au sens classique : la mise à jour est une opération d'administration, unitaire ou orchestrée par la console du constructeur.

| Point | Exigence |
|---|---|
| Cadence | Doctrine de version écrite et datée (§2.7), pas une habitude |
| Séquence | Passif, vérification, bascule, actif — avec les précautions du §2.7 |
| Retour arrière | Double partition d'image, testée |
| Preuve | Version relevée directement sur l'équipement, pas dans un tableur |
| Micrologiciels | Traités comme une campagne à part entière, par anneaux (§3.8) |

### 19.7 Conteneurs et cloud

Le paradigme change complètement : on ne déploie pas un correctif, on **reconstruit et on remplace** (§3.2).

| Objet | Mécanisme de correction | Indicateur pertinent |
|---|---|---|
| Image de conteneur | Reconstruction depuis une image de base à jour | **Âge de l'image** en production |
| Nœuds de cluster | Remplacement des nœuds par de nouvelles images | Version des nœuds, écart avec le plan de contrôle |
| Instances cloud | Redéploiement depuis une image mise à jour | Âge de l'image, part d'instances hors modèle |
| Services managés | Fenêtre de mise à jour du fournisseur | Versions dépréciées et échéances (ch. 30) |

**Le déplacement du travail** est ici essentiel : le MCS ne se joue plus au déploiement mais dans la **chaîne de construction** — donc dans un périmètre souvent détenu par les équipes de développement, pas par l'exploitation. C'est un sujet d'organisation autant que d'outillage (chapitre 28).

### 19.8 ⏱ Consolider le reporting multi-outils

Une organisation de taille intermédiaire utilise couramment cinq à huit mécanismes de déploiement distincts. Chacun produit son propre rapport, avec son propre périmètre, son propre vocabulaire et son propre calcul.

**Le problème du chiffre unique.** Additionner ces rapports produit un nombre faux, pour trois raisons : les périmètres se recouvrent partiellement, les définitions de « conforme » diffèrent d'un outil à l'autre, et les actifs non couverts par aucun outil n'apparaissent nulle part.

✅ **BONNE PRATIQUE (P0) — la consolidation par le périmètre, pas par les outils**
Partez du **périmètre de référence** (chapitre 10), et pour chaque actif, indiquez quel outil le couvre et quel est son état. Les actifs couverts par aucun outil apparaissent alors explicitement — c'est l'information la plus importante que produise cette consolidation, et celle qu'aucun rapport d'outil ne donnera jamais.

### 19.9 📌 Limites communes à toutes les familles

- **Le coût croît avec la découverte.** Les licences par actif créent une incitation perverse : mieux inventorier augmente la facture.
- **Aucun outil ne couvre tout le périmètre réel.** Systèmes industriels, services en ligne, composants embarqués, produits livrés aux clients restent hors champ.
- **Le reporting natif est rarement honnête.** Il présente le taux de conformité sur les actifs que l'outil connaît — c'est-à-dire le chiffre flatteur du §10.11.
- **La dépendance à l'éditeur est forte**, et l'historique rarement portable.
- **L'outil ne crée pas de fenêtre.** La contrainte dominante reste organisationnelle.

### 19.10 ✅ Recommandations priorisées

| Prio | Taille d'organisation | Recommandation |
|---|---|---|
| **P0** | Toutes | Un mécanisme couvrant les systèmes d'exploitation, avec reporting exportable |
| **P0** | Toutes | Un mécanisme pour les applications tierces du poste de travail |
| **P0** | Toutes | La consolidation par le périmètre de référence (§19.8) |
| P1 | > 200 actifs | Anneaux et critères d'arrêt outillés (§18.4) |
| P1 | Parc distribué | Mécanisme fonctionnant hors réseau interne |
| P1 | Toutes | Orchestration des redémarrages, avec indicateur de temps sans redémarrage |
| P2 | > 500 actifs | Automatisation de la vérification post-déploiement |
| P2 | Environnements cloud | Reconstruction périodique automatisée des images |

### 19.11 🔴 FIL ROUGE — mai 2027 : l'inventaire des mécanismes

Avant tout achat, Claire Nadeau demande l'inventaire des mécanismes de déploiement réellement en usage chez HELIOMED. Le résultat surprend tout le monde.

| Mécanisme | Périmètre couvert | Reporting exportable |
|---|---|---|
| Console interne de l'exploitation | 176 serveurs Windows et Linux | Oui |
| Console de l'infogérant | 620 postes | Oui, depuis janvier (§13.9) |
| Mise à jour automatique native, non supervisée | 34 serveurs Linux découverts en 2026 | **Non** |
| Consoles constructeurs | 6 équipements réseau | Non — relevé manuel |
| Chaîne de construction de Nantes | Images de conteneurs | Oui, mais non rattachée au périmètre MCS |
| Aucun | **11 postes de supervision, 3 automates, 38 services en ligne, tous les micrologiciels** | — |

**Six mécanismes, aucune vue consolidée.** Le taux annoncé au comité provenait des deux premiers, soit 796 actifs sur un périmètre de référence en comptant nettement plus.

**Les trois décisions.**

1. **Pas d'achat.** Les deux mécanismes principaux couvrent l'essentiel ; le problème n'est pas l'outillage, c'est la consolidation. Une extraction mensuelle rapprochée du périmètre de référence est mise en place — quelques jours de travail, aucun coût de licence.
2. **Les 34 serveurs en mise à jour automatique non supervisée** sont rattachés à la console interne. Le contrôle révèle au passage que 12 d'entre eux appliquaient bien les correctifs mais n'avaient pas redémarré depuis plus de 400 jours — le piège exact du §19.3.
3. **Les applications tierces du poste de travail** deviennent le seul vrai sujet d'investissement. L'inventaire sur 30 postes remonte 47 applications distinctes, dont 9 hors support. C'est la ligne budgétaire retenue pour 2028.

**Ce que Claire écrit dans sa note.** *Nous n'avions pas un problème d'outil, nous avions un problème de dénominateur. L'achat d'un outil supplémentaire aurait produit un septième rapport partiel.*

**Livrable de l'épisode.** La consolidation par périmètre, et l'inventaire des applications tierces — première ligne du budget 2028.

→ La suite en 🔴 §20.11, quand une ligne d'assemblage ne pourra pas être arrêtée avant novembre.

→ **Chapitre 20 — Quand on ne peut pas patcher : les mesures compensatoires** : que faire quand corriger est impossible.

### Synthèse mentale du chapitre 19

Neuf critères évaluent n'importe quel outil de déploiement, et le plus décisif à long terme est l'exportabilité des données brutes : sans elle, pas d'indicateur propre, pas de preuve indépendante, pas de changement de fournisseur sans perte d'antériorité. Sous Windows, les applications tierces échappent au mécanisme natif alors qu'elles concentrent une part majeure des vulnérabilités exploitées sur poste. Sous Linux, la mise à jour automatique sans orchestration des redémarrages produit un parc que l'on croit à jour et qui exécute encore du code vulnérable. Sur les mobiles, on pilote par la politique d'accès plutôt que par le déploiement. Dans le cloud et les conteneurs, le MCS se déplace vers la chaîne de construction, souvent détenue par d'autres équipes. Enfin, additionner les rapports de cinq outils produit un chiffre faux : la consolidation part du périmètre de référence, et son résultat le plus précieux est la liste des actifs couverts par aucun outil.

**Trois questions de vérification**

1. Vous évaluez un outil de déploiement. Quel critère privilégiez-vous pour l'horizon à cinq ans, et quelles trois capacités perdez-vous s'il n'est pas rempli ?
2. Votre parc Linux applique automatiquement les correctifs de sécurité. Quelle vérification faites-vous avant de le considérer comme à jour ?
3. Cinq outils rapportent chacun plus de 95 % de conformité. Pourquoi ne pouvez-vous pas en déduire un taux global, et comment procédez-vous ?

---

## Chapitre 20 — Quand on ne peut pas patcher : les mesures compensatoires

### 20.1 Taxonomie des impossibilités

« On ne peut pas patcher » recouvre cinq situations très différentes, qui n'appellent ni les mêmes réponses ni les mêmes interlocuteurs. Le premier travail consiste à identifier laquelle vous avez en face de vous.

| Type | Description | Qui peut la lever | Horizon |
|---|---|---|---|
| **Technique** | Le correctif n'existe pas, ou casse une dépendance | L'éditeur | Incertain |
| **Contractuelle** | La garantie ou la certification interdit la modification | Le constructeur, le contrat | Négociable |
| **Métier** | L'interruption n'est pas acceptée | Le propriétaire métier | Négociable |
| **Budgétaire** | La correction suppose une migration non financée | La direction | Cycle budgétaire |
| **Temporelle** | Fenêtre trop éloignée | La planification | Court terme |

⚠️ **PIÈGE — le motif générique**
« C'est un système critique, on ne peut pas y toucher » n'est pas un motif : c'est un refus non qualifié. Exiger le type exact d'impossibilité change la conversation, parce que chaque type a un interlocuteur et un horizon différents. Beaucoup d'impossibilités déclarées techniques se révèlent temporelles ou métier une fois qualifiées.

🖼 **SCHÉMA — Hiérarchie des compensations.** *Pyramide inversée à six rangs, du plus protecteur au moins protecteur, avec le coût récurrent en regard.*

### 20.2 La hiérarchie des mesures compensatoires

Toutes les compensations ne se valent pas. Voici l'ordre d'efficacité décroissante, à parcourir de haut en bas.

| Rang | Mesure | Effet | Coût récurrent |
|---|---|---|---|
| 1 | **Supprimer l'exposition** | Le chemin d'attaque disparaît, y compris pour les vulnérabilités futures (§11.8) | Nul |
| 2 | **Isoler** | L'actif n'est atteignable que depuis un périmètre restreint | Faible |
| 3 | **Désactiver la fonction vulnérable** | La vulnérabilité n'est plus atteignable | Nul si la fonction est inutile |
| 4 | **Filtrer** | Les tentatives connues sont bloquées en amont | Maintien des règles |
| 5 | **Renforcer la détection** | On ne bloque pas, on voit | **Élevé** — charge d'analyse permanente |
| 6 | **Accepter le risque** | Rien n'est fait, la décision est formalisée | Nul, mais le risque est porté |

**La règle d'or** : ne descendez d'un rang que si le rang supérieur est réellement impossible, et écrivez pourquoi. La majorité des organisations sautent directement au rang 5, qui est le plus coûteux et le moins protecteur — parce que c'est le seul qui ne demande de négociation avec personne.

### 20.3 La correction virtuelle

Bloquer l'exploitation d'une vulnérabilité en amont de l'actif, sans le modifier : règle de filtrage applicatif, signature de sonde réseau, restriction de protocole.

| Ce que ça apporte | Ce que ça n'apporte pas |
|---|---|
| Un délai — souvent quelques jours à quelques semaines | Une protection durable |
| Une couverture de masse rapide sur plusieurs actifs | Une garantie : les contournements de signature sont fréquents |
| Une trace des tentatives, précieuse en investigation | Une protection contre un attaquant déjà à l'intérieur du périmètre filtré |

📌 **LIMITES** — Une règle de correction virtuelle protège contre les **variantes connues** d'une exploitation. Elle est écrite à partir des exploits observés ; une variante suffisante la contourne. Traitez-la comme un **délai acheté**, jamais comme une correction, et donnez-lui une date d'expiration comme à toute compensation.

### 20.4 Réduire la surface

Souvent la mesure la plus efficace et la moins employée : la vulnérabilité concerne un composant que vous n'utilisez pas.

**Les quatre gestes**, par ordre d'application :

1. **Désactiver le service** — si personne ne l'utilise, il n'a pas à tourner.
2. **Désactiver le module ou l'extension** vulnérable, quand le service est nécessaire mais pas cette fonction.
3. **Désactiver le protocole** — protocoles hérités, versions anciennes, méthodes d'authentification faibles.
4. **Restreindre les droits** du compte sous lequel s'exécute le service, pour limiter l'effet d'une exploitation réussie.

**La vérification préalable indispensable** : mesurer l'usage réel avant de désactiver. Un service qui semble inutilisé peut porter un traitement mensuel ou une intégration partenaire (§10.5, dépendance temporelle). Observez sur un cycle métier complet.

### 20.5 Isolation d'urgence : ce qui est faisable en 24 heures

| Mesure | Délai réaliste | Effet | Risque métier |
|---|---|---|---|
| Restreindre l'accès à des plages d'adresses connues | 1 à 4 h | Fort | Faible si le besoin est bien cerné |
| Placer l'actif derrière un accès distant authentifié | 4 à 24 h | Fort | Modéré : change l'usage |
| Couper l'exposition externe | **Minutes** | Total sur ce vecteur | Selon l'usage |
| Isoler dans un segment réseau dédié | Jours à semaines | Fort | Élevé : dépendances à recenser |
| Segmentation générale du réseau | Mois | Structurel | Projet |

**Les trois premières lignes sont réalisables dans la journée** et couvrent la majorité des besoins d'urgence. La segmentation générale est un projet d'architecture : utile, mais elle ne répond pas à une crise en cours.

### 20.6 La surveillance renforcée comme compensation

Elle est légitime, et son coût est systématiquement sous-estimé.

**Ce qu'elle exige réellement** : une règle de détection écrite et testée, une source de journaux couvrant l'actif, quelqu'un pour analyser les alertes, une procédure de réaction, et une durée de vie définie.

⚠️ **PIÈGE — la surveillance sans destinataire**
Une règle de détection dont les alertes arrivent dans une boîte que personne ne lit ne constitue pas une compensation. C'est la forme la plus courante de compensation fictive : elle coche la case, ne protège de rien, et donne une fausse assurance à toute la chaîne de décision.

**La question à poser avant d'accepter cette compensation** : *qui regarde, quand, et que fait-il exactement s'il voit quelque chose ?* Sans réponse nominative, la mesure n'est pas recevable.

### 20.7 Les sept attributs obligatoires

C'est le cœur du chapitre, et la règle qui empêche le pourrissement. **Toute mesure compensatoire porte ces sept attributs**, sans exception.

| # | Attribut | Pourquoi |
|---|---|---|
| 1 | **Propriétaire nommé** | Quelqu'un répond de son maintien |
| 2 | **Date de début** | Point de départ du décompte |
| 3 | **Date d'expiration** | Sans elle, la mesure devient permanente par défaut |
| 4 | **Moyen de vérification** | Comment sait-on qu'elle est toujours active ? |
| 5 | **Coût opérationnel** | Charge récurrente, à comparer au coût de la correction |
| 6 | **Condition de sortie** | Quel événement met fin à la compensation |
| 7 | **Contrôle périodique** | Fréquence de la vérification effective |

**Le quatrième attribut est celui qu'on oublie**, et c'est le plus important en pratique. Une règle de filtrage supprimée lors d'une refonte réseau, une isolation annulée par un nouveau routage, une surveillance désactivée lors d'un changement d'outil : la compensation disparaît sans que personne ne le sache, et le risque revient sans qu'aucune alerte ne se déclenche.

✅ **BONNE PRATIQUE (P0)** — Le contrôle périodique de l'existence effective des compensations est un **point d'ordre du jour du comité MCS** (§9.3). Cinq minutes par mois. C'est ce qui distingue une compensation d'une intention.

### 20.8 Formaliser l'acceptation de risque

Quand aucune compensation n'est possible, reste l'acceptation formelle. Les sept champs de la dérogation (§7.4) s'appliquent, avec trois exigences supplémentaires :

- le **signataire** est le propriétaire métier, à un niveau proportionné à l'enjeu (§9.2) ;
- le **risque est décrit en termes métier**, pas techniques : « une compromission de ce serveur exposerait les données de paie de 1 380 salariés » et non « exécution de code à distance » ;
- la **revue est datée**, et le renouvellement remonte d'un niveau (§7.4).

### 20.9 ⚠️ Le compensatoire permanent

**La mécanique du pourrissement**, en cinq étapes qui se répètent partout :

```
1. Correction impossible → compensation mise en place, durée 3 mois
2. À 3 mois, rien n'a changé → prolongation « le temps de »
3. La personne qui l'a mise en place change de poste
4. La compensation n'est plus vérifiée : personne ne sait si elle est active
5. Deux ans plus tard, l'actif est considéré comme « traité »
```

**Les trois garde-fous** qui cassent ce cycle : l'attribut n° 4 (moyen de vérification) contrôlé périodiquement ; le renouvellement remontant d'un niveau hiérarchique (§7.4) ; et l'indicateur **âge moyen des compensations actives**, présenté au comité — c'est la mesure la plus honnête de la dette réellement portée par l'organisation.

### 20.10 🔬 Mini-lab 7 — Rédiger une dérogation auditable

**Objectif** — Produire une fiche complète, défendable en audit, et arbitrer le niveau de signature.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §7.4, §20.2, §20.7, annexe C.4 · **Livrable** formulaire D.4 rempli.
**Compétences validées** — ✔ parcourir la hiérarchie des compensations ✔ écrire un risque en termes métier ✔ choisir le bon signataire ✔ aligner une date d'expiration sur un événement décisionnel ✔ distinguer horloge de risque et horloge de traitement

**Dossier fourni**

| Élément | Donnée |
|---|---|
| Actif | `SRV-CRM-02`, serveur applicatif, environnement production |
| Constat | Vulnérabilité critique sur un composant web · exploitable **à distance sans authentification** · exploitation non observée à ce jour |
| Correction disponible | Oui, mais elle exige la montée en version majeure de l'application métier |
| Coût de la correction | 40 k€ facturés par l'éditeur, **non budgétés sur l'exercice** |
| Délai éditeur | Version compatible disponible sous 3 mois après commande |
| Exposition | Réseau bureautique interne · **non publié sur Internet** |
| Utilisateurs | 60 personnes du service commercial |
| Données | Fichier clients — 2 800 enregistrements, données à caractère personnel |
| Classe de service | C2 · délai politique pour critique non exploitée : 30 jours |
| Journalisation | Accès applicatifs conservés 90 jours, exportés vers la plateforme centrale |
| Contexte | Exercice budgétaire clos ; vote du budget suivant en mars |

**Questions**
(a) Rédigez la fiche D.4 complète.
(b) Qui signe, et pourquoi ?
(c) Quelle date d'expiration retenez-vous, et sur quoi l'alignez-vous ?
(d) Que devient l'horloge de risque pendant la dérogation ?
(e) Quelles conditions de révocation anticipée écrivez-vous ?

---

**Corrigé commenté — fiche D.4 remplie**

| Champ | Contenu |
|---|---|
| **Identifiant** | `DER-2027-018` · version 1.0 · émise le 12/06/2027 |
| **Objet** | `SRV-CRM-02` · vulnérabilité `[identifiant]` sur composant web · correction nécessitant la montée en version majeure de l'application de gestion commerciale |
| **Type d'impossibilité** | ☑ **Budgétaire** — le correctif existe et est techniquement applicable |
| **Analyse de risque, en termes métier** | Un poste bureautique compromis permettrait à un attaquant d'atteindre ce serveur sans authentification et d'accéder au fichier clients : 2 800 enregistrements comportant nom, coordonnées et historique commercial. Conséquences : notification de violation de données, atteinte à la relation client, exposition contractuelle vis-à-vis de trois grands comptes dont le contrat comporte une clause de sécurité. Exploitation non observée à ce jour dans le monde. |
| **Exposition mesurée** | ☑ réseau bureautique — ☐ Internet · joignable depuis 340 postes avant compensation |
| **Exploitation observée** | ☑ non |
| **Mesures compensatoires** | **1.** Restriction d'accès réseau : le serveur n'est joignable que depuis les 60 postes du service commercial (rang 2 de la hiérarchie §20.2). **2.** Règle de filtrage applicatif bloquant les motifs d'exploitation publiés (rang 4). **3.** Alerte sur toute tentative d'accès depuis une origine non autorisée, destinataire nommé (rang 5). **Rangs écartés** : rang 1 — l'exposition interne est nécessaire à l'usage ; rang 3 — la fonction vulnérable est celle utilisée par l'application. |
| **Moyen de vérification** | Test mensuel d'accès depuis un poste hors périmètre autorisé — **doit échouer** · vérification de la présence effective de la règle de filtrage · test d'alerte trimestriel avec accusé de traitement |
| **Fréquence du contrôle** | Mensuelle, inscrite à l'ordre du jour du comité MCS |
| **Coût opérationnel** | ≈ 2 h/mois de vérification + charge d'analyse des alertes |
| **Propriétaire de la compensation** | `[responsable exploitation]` |
| **Signataire** | `[directeur commercial]` — propriétaire métier |
| **Date de début** | 12/06/2027 |
| **Date d'expiration** | **31/03/2028** |
| **Conditions de sortie** | Migration réalisée · **ou** exploitation de cette vulnérabilité observée dans le monde · **ou** compromission avérée d'un poste du service commercial |
| **Conditions de révocation anticipée** | Publication d'un exploit fonctionnel · entrée de la vulnérabilité dans un catalogue d'exploitation avérée · modification de l'exposition du serveur · incident de sécurité touchant le service commercial |
| **Nombre de renouvellements** | 0 |
| **Date de revue** | Trimestrielle — 12/09/2027, 12/12/2027, 12/03/2028 |

**(b) Le signataire — arbitrage**

Le propriétaire métier, ici le directeur commercial. **Trois raisons** :

1. C'est lui qui **porte le risque** : ce sont ses données clients et sa relation commerciale.
2. C'est lui qui **détient le levier** : le budget de 40 k€ relève de son arbitrage ou de son plaidoyer.
3. Faire signer la sécurité lui transférerait un risque qu'elle n'a pas les moyens de porter, et déresponsabiliserait le métier (§9.2).

⚠️ **Le cas limite** : si les données concernées relevaient d'un régime sensible — données de santé, données de paiement —, la grille C.4 imposerait une signature au niveau de la direction générale, indépendamment du fait que l'actif soit interne et de classe C2.

**(c) La date d'expiration**

Le **31 mars 2028**, alignée sur le vote du budget suivant. C'est le point du §7.4 : une date d'expiration doit correspondre à un **événement décisionnel réel**, pas à une durée arbitraire.

| Date envisageable | Évaluation |
|---|---|
| « jusqu'à la migration » | ❌ Ce n'est pas une date. Rejet automatique |
| 12/12/2027 — 6 mois | ⚠️ Tombe avant tout arbitrage budgétaire : le renouvellement sera mécanique |
| **31/03/2028 — vote du budget** | ✅ Le renouvellement coïncide avec le moment où quelque chose peut changer |
| 31/12/2028 | ❌ Trop long : 18 mois sans point de décision |

**(d) L'horloge de risque**

Elle **continue de courir** (§17.5). La dérogation suspend l'horloge de traitement — l'équipe n'est pas en faute — mais le risque est porté chaque jour. Concrètement :

- l'horloge SLA est suspendue au 12/06/2027, avec motif « dérogation `DER-2027-018` » ;
- l'horloge de risque affiche, au comité de décembre, **183 jours de risque porté** ;
- ce chiffre est celui qui apparaît au tableau de bord de direction, pas le taux de respect des délais.

C'est ce qui empêche la dérogation de rendre le retard invisible.

**(e) Les conditions de révocation anticipée**

Elles sont distinctes des conditions de sortie : la sortie met fin à la dérogation parce que le problème est résolu ; la **révocation** y met fin parce que l'hypothèse sur laquelle elle reposait a changé. Ici, l'hypothèse centrale est *« exploitation non observée »*. Les quatre conditions écrites la surveillent directement.

**Les quatre erreurs attendues**
1. Pas de date d'expiration, ou date exprimée comme un événement flou.
2. Compensations non vérifiables — « surveillance renforcée » sans destinataire ni test (§20.6).
3. Signature par la sécurité au lieu du métier.
4. Risque décrit en termes techniques — « exécution de code à distance » ne permet à aucun directeur commercial de décider en connaissance de cause.

### 20.11 🔴 FIL ROUGE — juin 2027 : la ligne 2 de Saint-Étienne

Une vulnérabilité activement exploitée est publiée sur le système de supervision de la ligne d'assemblage 2 — le constat n° 5 du mini-lab 4, désormais réel. Classe C4.

**Les faits.** Le correctif existe. Le constructeur ne l'a pas validé pour la configuration installée ; l'appliquer sans validation fait tomber la garantie et invalide la qualification du procédé, ce qui a des conséquences réglementaires sur la production de dispositifs médicaux. Le prochain arrêt de production est en novembre — cinq mois.

**Le parcours de la hiérarchie du §20.2.**

| Rang | Examiné ? | Résultat |
|---|---|---|
| 1 — Supprimer l'exposition | Oui | Le poste n'est pas exposé à Internet. Déjà acquis |
| 2 — **Isoler** | **Oui** | **Retenu** : le poste communiquait avec le réseau bureautique pour un export de données de production. L'export est basculé en dépôt de fichiers unidirectionnel |
| 3 — Désactiver la fonction | Oui | Impossible : la fonction vulnérable est celle utilisée par la supervision |
| 4 — **Filtrer** | **Oui** | **Retenu** : règle de filtrage sur le conduit entre zones industrielles |
| 5 — Détection renforcée | Oui | Retenue en complément, avec destinataire nommé et procédure |
| 6 — Accepter | — | Non atteint |

**Ce qui a rendu la solution possible.** Thomas Berger savait que l'export vers la bureautique n'était plus utilisé depuis dix-huit mois — l'outil qui le consommait avait été remplacé. Personne n'avait jamais posé la question. La suppression de ce flux, décidée en vingt minutes, retire le principal chemin d'accès au poste.

**La fiche produite.** Compensation valable jusqu'au 30 novembre 2027, date de l'arrêt de production. Propriétaire : Thomas Berger. Vérification mensuelle : test d'accès depuis le réseau bureautique — doit échouer — et contrôle de la règle de filtrage. Signataire : le directeur industriel. Condition de sortie : correctif validé par le constructeur et appliqué pendant l'arrêt de novembre.

**Le point que Claire Nadeau porte au comité.** La compensation n'est pas un pis-aller subi : dans ce cas précis, l'isolation obtenue est **plus protectrice que le correctif** n'aurait été, puisqu'elle protège aussi contre les vulnérabilités futures du même poste (§11.8). Elle sera maintenue **après** l'application du correctif en novembre.

**Livrable de l'épisode.** La fiche de compensation avec ses sept attributs, et une revue systématique des flux entrants des postes de supervision — qui révélera en juillet trois autres flux devenus inutiles.

→ La suite en 🔴 §21.11, quand une vulnérabilité sur la passerelle d'accès distant ne laissera pas cinq mois pour décider.

→ **Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j** : réagir quand tout s'accélère.

### Synthèse mentale du chapitre 20

« On ne peut pas patcher » recouvre cinq impossibilités distinctes, avec des interlocuteurs et des horizons différents : les qualifier change la conversation, et beaucoup d'impossibilités déclarées techniques se révèlent temporelles ou métier. La hiérarchie des compensations se parcourt de haut en bas — supprimer l'exposition, isoler, désactiver, filtrer, détecter, accepter — et l'on ne descend d'un rang qu'en écrivant pourquoi le précédent est impossible. La plupart des organisations sautent directement à la détection renforcée, la plus coûteuse et la moins protectrice, parce qu'elle ne demande de négociation avec personne. La correction virtuelle achète un délai, jamais une protection durable. Sept attributs rendent une compensation réelle, dont le moyen de vérification, celui qu'on oublie et qui empêche la disparition silencieuse de la mesure. Enfin, une compensation bien choisie peut être plus protectrice qu'un correctif, puisqu'elle couvre aussi les vulnérabilités futures du même actif.

**Trois questions de vérification**

1. Un exploitant vous répond « c'est un système critique, on ne peut pas y toucher ». Quelle est votre question suivante, et pourquoi change-t-elle la nature de la discussion ?
2. Pourquoi la surveillance renforcée est-elle simultanément la compensation la plus choisie et la moins protectrice ?
3. Une compensation mise en place il y a dix-huit mois est-elle encore active ? Comment le savez-vous, et qu'auriez-vous dû prévoir au moment de la décision ?

---

## Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j

### 21.1 Ce qui distingue une crise vulnérabilité d'un incident

| | Crise vulnérabilité | Incident de sécurité |
|---|---|---|
| Point de départ | Une faille est publiée ou exploitée **ailleurs** | **Vous** êtes touché |
| Question centrale | Suis-je exposé, et depuis quand ? | Que s'est-il passé, et jusqu'où ? |
| Objectif | Réduire l'exposition avant d'être atteint | Contenir, éradiquer, reconstruire |
| Horloge | Course contre l'automatisation des attaques | Course contre la progression de l'attaquant |

**Le lien entre les deux, et il est essentiel** : une crise vulnérabilité sur un actif exposé depuis plusieurs jours **peut déjà être un incident** sans que vous le sachiez. C'est le §21.3, et c'est ce qui distingue une réaction professionnelle d'une réaction naïve.

### 21.2 L'échelle de qualification en cinq niveaux

Toutes les vulnérabilités graves ne déclenchent pas une crise. Cinq niveaux, avec une réponse propre à chacun.

| Niveau | Situation | Réponse |
|---|---|---|
| **1** | Vulnérabilité critique, aucune preuve d'exploitation | Processus normal, délai de la classe de service |
| **2** | Exploitation active observée dans le monde | Accélération : arbre de décision, feuille « urgence » (§16.3) |
| **3** | Exploitation observée **dans votre secteur** | Déclenchement de la cellule, hypothèse de ciblage |
| **4** | Indices de compromission **chez vous** | Bascule en gestion d'incident |
| **5** | **Journalisation insuffisante pour conclure** | **Traiter comme le niveau 4 jusqu'à preuve du contraire** |

Le niveau 5 est celui que les organisations traitent le plus mal, parce qu'il n'y a rien à voir — et l'absence de signal est confondue avec l'absence d'événement.

### 21.3 La règle qu'il faut enseigner explicitement

> **L'absence de preuve de compromission n'est pas la preuve de l'absence de compromission — a fortiori quand la journalisation est insuffisante.**

**Pourquoi c'est capital en pratique.** Après la publication d'un exploit sur un équipement exposé, la question n'est pas seulement « corrigeons-nous ? » mais « avons-nous déjà été atteints ? ». Corriger ferme la porte ; cela ne fait pas sortir celui qui serait entré avant. Sur les équipements de bordure en particulier, les compromissions **persistent au-delà du correctif** : implants dans le micrologiciel, comptes créés, configurations modifiées, sessions volées.

**Les trois questions à poser dès la première heure :**

1. Depuis combien de temps cet actif est-il exposé et vulnérable ?
2. De quels journaux disposons-nous sur cette période, et à quelle granularité ?
3. Ces journaux permettraient-ils de **détecter** ce type d'exploitation, ou seulement de constater une indisponibilité ?

Si la réponse à la troisième question est négative, vous êtes au niveau 5. Il faut le dire dans ces termes à la direction : *« nous ne pouvons pas établir que nous n'avons pas été compromis »*. C'est une formulation inconfortable, et c'est la seule honnête.

### 21.4 Critères de déclenchement

Écrits à l'avance, sans discussion possible au moment des faits :

```
DÉCLENCHEMENT DE LA CELLULE si TOUTES ces conditions sont réunies :
   · vulnérabilité activement exploitée (source vérifiée)
   · au moins un actif du périmètre est affecté
   · cet actif est exposé à Internet OU de niveau 0 OU critique métier

DÉCLENCHEMENT si l'une de ces conditions est réunie :
   · indices de compromission sur un actif affecté
   · impossibilité d'établir l'absence de compromission (niveau 5)
   · demande d'une autorité ou d'un client majeur
```

### 21.5 La cellule de crise vulnérabilité

**Composition minimale** : un pilote qui décide et arbitre, un responsable technique qui conduit les actions, un référent métier pour les décisions d'interruption, un référent communication, et un **greffier** dont le seul rôle est de tenir le journal.

**Le rythme** : points fixes toutes les deux heures les premières douze heures, puis toutes les quatre à six heures. Points courts — dix minutes — avec trois questions invariables : qu'a-t-on appris, que décide-t-on, qui fait quoi d'ici au prochain point.

**Le journal de décision** est le livrable central de la crise. Pour chaque entrée : horodatage, information reçue et sa source, décision prise, décideur, action engagée. Il sert pendant la crise à éviter les redites et les contradictions ; après, il constitue la preuve, la base du retour d'expérience, et l'élément qui vous protège si les décisions sont contestées.

⚠️ **PIÈGE — le greffier improvisé**
Sans rôle dédié, personne ne tient le journal : tout le monde agit. Trois jours plus tard, il est impossible de reconstituer qui a décidé quoi, quand, et sur quelle information. Le greffier est le rôle le plus facile à supprimer sous pression, et celui dont l'absence coûte le plus cher après.

### 21.6 Les six premières heures

| Heure | Action | Livrable |
|---|---|---|
| H+0 | Vérifier l'information à la source (avis éditeur, pas un article de presse) | Constat qualifié (§14.7) |
| H+0 à H+1 | **Mesurer l'exposition** : quels actifs, joignables d'où, depuis quand | Liste nominative |
| H+1 | Vérifier l'existence d'un correctif et d'un contournement officiel | Options disponibles |
| H+1 à H+2 | **Décider d'une mesure d'urgence** : fermeture d'exposition en priorité (§11.8) | Décision tracée |
| H+2 à H+4 | Engager la recherche de compromission préalable (§21.7) | Périmètre d'investigation |
| H+4 à H+6 | Informer la direction, préparer la communication | Note de situation |

**La décision la plus fréquente et la plus efficace à H+2** n'est pas d'appliquer le correctif — il n'est pas toujours disponible, testé ni déployable en deux heures. C'est de **fermer l'exposition** : couper la publication Internet, restreindre à des plages d'adresses connues, désactiver le service. Quelques minutes, réversible, et cela arrête l'horloge.

### 21.7 La recherche de compromission préalable

**L'hypothèse de travail par défaut**, pour tout équipement de bordure exposé et exploité : *considérer qu'une compromission a pu avoir lieu, jusqu'à preuve raisonnable du contraire.*

**Les cinq vérifications de premier niveau :**

| Vérification | Ce qu'on cherche |
|---|---|
| Comptes | Comptes créés, modifiés, réactivés depuis la date d'exposition |
| Configuration | Écarts par rapport à la référence (§22.3) : règles, redirections, accès |
| Persistance | Tâches planifiées, services, scripts de démarrage inconnus |
| Journaux d'accès | Connexions depuis des origines inhabituelles, horaires atypiques |
| Trafic sortant | Communications vers des destinations inhabituelles |

**Quand basculer en gestion d'incident** : dès qu'une de ces vérifications produit un résultat non explicable. La bascule est une décision du pilote de cellule, et elle change la nature des opérations — l'objectif devient la préservation des traces et la reconstruction, ce qui peut **contredire** l'urgence de correction. Ce point doit être compris à l'avance : sur un équipement compromis, appliquer le correctif peut détruire les preuves.

### 21.8 Le correctif d'urgence

**Le principe.** Contourner le processus normal sans détruire ce qui le rend fiable.

| Étape normale | En urgence |
|---|---|
| Délai d'observation | **Supprimé** — le calcul de risque s'inverse (§18.11) |
| Validation en recette | Réduite à un test fonctionnel minimal |
| Anneaux | Conservés, mais compressés : pilote de quelques heures |
| Critères d'arrêt | **Conservés intégralement** — c'est ce qui rend la compression acceptable |
| Plan de retour arrière | **Conservé intégralement** |
| Demande de changement | Émise **a posteriori**, sous 48 h, avec le journal de décision |
| Preuve | Conservée intégralement |

**Ce qu'on ne supprime jamais** : les critères d'arrêt, le retour arrière et la preuve. Ce sont les trois éléments qui permettent de se tromper sans catastrophe — précisément ce dont on a besoin quand on va vite.

### 21.9 Communication

| Destinataire | Quand | Contenu |
|---|---|---|
| Direction générale | H+4 à H+6 | Situation, exposition, décisions prises, ce qui n'est pas encore su |
| Métiers concernés | Avant toute interruption | Ce qui va être coupé, quand, pour combien de temps |
| Utilisateurs | Si effet visible | Fait, durée, contournement |
| Clients | Si leur service est affecté, ou si contractuellement prévu | Factuel, sans spéculation |
| Assureur | Selon contrat, souvent sous 48-72 h | Déclaration conservatoire |
| Autorités | Selon obligations applicables (ch. 8, ch. 33) | Délais réglementaires, à connaître **avant** |

⚠️ **PIÈGE — annoncer trop tôt une conclusion**
« Nous n'avons pas été compromis » prononcé à H+6 est presque toujours prématuré, et devient très difficile à corriger si l'investigation dit l'inverse. Formulation à privilégier : *« à ce stade, les vérifications réalisées n'ont pas mis en évidence de compromission ; l'investigation se poursuit »*.

### 21.10 Sortie de crise et retour d'expérience

**Les critères de sortie**, à énoncer explicitement : correctif appliqué et vérifié sur l'ensemble du périmètre affecté · recherche de compromission conclue · mesures d'urgence soit levées, soit converties en compensations formelles (§20.7) · communication close.

**Le retour d'expérience utile** tient en cinq questions, et il porte sur le processus, jamais sur les personnes :

1. Quel a été le **délai de détection** — entre la publication et notre prise de connaissance ?
2. Quel a été le **délai de mesure d'exposition** — et pourquoi ?
3. Quelle information nous a **manqué**, et comment l'obtenir la prochaine fois ?
4. Quelle décision a été **retardée**, et par quel manque de mandat ?
5. Que faut-il **pré-arbitrer** pour ne plus reprendre cette discussion à chaud (§9.4) ?

### 21.11 🔴 FIL ROUGE — juillet 2027 : ce que la passerelle avait vécu

Le 9 juillet 2027, un avis constructeur publie une vulnérabilité critique sur la passerelle d'accès distant d'HELIOMED. Exploitation active confirmée dans les heures qui suivent.

**H+0 — la qualification.** Malik Ferhaoui vérifie à la source. La version installée est affectée. Un correctif existe depuis six heures.

**H+1 — l'exposition.** L'interface d'administration a été fermée en septembre 2026 (§11.12). Le service d'accès distant lui-même, lui, reste nécessairement publié : c'est sa fonction. 210 collaborateurs l'utilisent quotidiennement.

**H+2 — la décision.** Fermer l'exposition signifierait couper l'accès distant de 210 personnes un mercredi matin. Claire Nadeau applique le pré-arbitrage du §9.4 : le seuil d'urgence autorise l'interruption sur décision du propriétaire technique. Elle ne coupe pas — elle **restreint** : accès limité aux plages d'adresses des sites HELIOMED et aux connexions déjà établies, le temps du correctif. Sept collaborateurs en déplacement sont impactés et prévenus individuellement.

**H+3 — la question qui change tout.** Le greffier note une remarque de Malik : *« depuis quand cette version est-elle installée ? »* Réponse : mars 2022. Et l'interface d'administration, celle qui porte la fonction vulnérable, a été publiée sur Internet de mars 2022 à septembre 2026 — **quatre ans et demi**.

La vulnérabilité publiée aujourd'hui existait dans le code depuis la version de 2021.

**H+4 — le niveau 5.** Claire pose les trois questions du §21.3. Les journaux de la passerelle sont conservés 30 jours. Il n'existe **aucune donnée** sur la période 2022-2026. La question « avons-nous été compromis pendant ces quatre ans et demi ? » n'a pas de réponse possible.

Elle informe Pierre Vasseur dans ces termes exacts : *nous ne pouvons pas établir que nous n'avons pas été compromis.* C'est la phrase la plus difficile de tout le fil rouge, et c'est la seule honnête.

**H+6 à J+3 — les opérations.** Correctif appliqué la nuit suivante, en urgence, avec critères d'arrêt et retour arrière conservés. Recherche de compromission sur les cinq axes du §21.7 : deux comptes locaux non documentés sont découverts sur la passerelle. Leur date de création n'est pas déterminable. Ils sont supprimés, et l'équipement est intégralement reconstruit à partir d'une configuration de référence plutôt que corrigé — décision prise en application du §21.7.

**J+3 à J+30.** Investigation étendue : recherche des mêmes indicateurs sur les actifs joignables depuis la passerelle, rotation complète des secrets susceptibles d'avoir transité, revue des accès distants. Aucune trace d'activité malveillante n'est établie — ce qui, comme le rappelle Claire au comité, ne prouve rien sur la période non journalisée.

**Les quatre décisions structurelles issues du retour d'expérience.**

1. **Journalisation** : conservation portée à 12 mois pour tous les actifs de bordure et de niveau 0, avec export vers un système indépendant de l'équipement.
2. **Doctrine de version** sur les équipements de bordure : au plus N-1, revue trimestrielle, avec date (§2.7).
3. **Reconstruction plutôt que correction** pour tout équipement de bordure ayant subi une exploitation potentielle.
4. **Pré-arbitrage complété** : le seuil d'urgence distingue désormais *restreindre* et *couper*, avec un décideur différent pour chacun.

**Ce que Claire écrit en conclusion du retour d'expérience**, et qui vaut pour tout le cours : *la crise de juillet 2027 n'a pas commencé le 9 juillet. Elle a commencé en mars 2022, le jour où une exposition temporaire n'a pas été refermée, et où personne n'a écrit de date de fin.*

→ Le scénario complet, avec ses données et ses décisions à prendre, constitue le **cas de synthèse A**.

→ **Chapitre 22 — Durcissement et référentiels de configuration** : la configuration, qui annule l'effet des correctifs quand elle est mauvaise.

### Synthèse mentale du chapitre 21

Une crise vulnérabilité se distingue d'un incident par son point de départ, mais l'une peut être l'autre sans que vous le sachiez : sur un actif exposé depuis plusieurs jours, la question n'est pas seulement « corrigeons-nous » mais « avons-nous déjà été atteints ». Cinq niveaux de qualification, dont le cinquième — journalisation insuffisante pour conclure — se traite comme une compromission probable. L'absence de preuve de compromission n'est pas la preuve de l'absence de compromission, et cette phrase doit pouvoir être prononcée devant une direction. La décision la plus efficace des deux premières heures n'est pas d'appliquer le correctif mais de fermer ou restreindre l'exposition : quelques minutes, réversible, et l'horloge s'arrête. En urgence, on comprime le délai d'observation et la validation, jamais les critères d'arrêt, le retour arrière et la preuve — ce sont eux qui permettent de se tromper sans catastrophe. Enfin, sur un équipement de bordure potentiellement compromis, corriger ne suffit pas : on reconstruit.

**Trois questions de vérification**

1. Un équipement exposé porte une vulnérabilité exploitée depuis trois semaines. Quelles trois questions posez-vous avant même de parler du correctif, et que faites-vous si la réponse à la troisième est négative ?
2. Quelles étapes du processus normal comprimez-vous en urgence, lesquelles conservez-vous intégralement, et pourquoi cette distinction précise ?
3. Votre direction vous demande à H+6 si vous avez été compromis. Formulez la réponse exacte que vous donnez, et expliquez pourquoi chaque mot compte.

---

---

> ### 🎓 À ce stade de la Partie III, vous savez…
>
> - **construire** une veille à partir de l'inventaire, et faire entrer tous les constats — pentest, audit, configuration, secret, obsolescence — dans une file unique ;
> - **interpréter** un rapport de scan, calculer une couverture honnête, et ne jamais confondre « non détecté », « non vulnérable » et « non scanné » ;
> - **prioriser** par arbre de décision plutôt que par seuil de gravité, et défendre une dépriorisation devant un comité ;
> - **piloter** un constat de bout en bout : parent et occurrences, deux horloges, escalade automatique, preuve par type d'issue ;
> - **conduire** une campagne : qualification en six questions, anneaux représentatifs, critères d'arrêt chiffrés, retour arrière chronométré, traîne longue qualifiée ;
> - **compenser** quand corriger est impossible, en parcourant la hiérarchie de haut en bas et en attachant les sept attributs ;
> - **conduire** une crise vulnérabilité, y compris quand la journalisation ne permet pas de conclure.
>
> **Ce que vous ne savez pas encore** : tout ce qui se dégrade en dehors des versions logicielles. C'est l'objet de la Partie IV.
