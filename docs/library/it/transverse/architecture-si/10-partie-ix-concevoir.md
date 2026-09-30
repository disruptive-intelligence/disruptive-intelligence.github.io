---
title: PARTIE IX — Concevoir
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 10
chapters: 10
---

> **Le miroir de la lecture.** Quarante-cinq chapitres ont appris à reconstituer les arbitrages d'autrui ; cinq apprennent à énoncer les siens.
>
> ⚠️ **Cette partie ne rend pas architecte.** Elle apprend à proposer une architecture justifiée pour un besoin courant, à énoncer ses compromis, et à identifier ce qu'il reste à vérifier. C'est le §7.3, et il faut le relire avant d'aborder ces chapitres.

---

### Chapitre 46 — Les quatre questions du concepteur

#### 46.1 La symétrie

🖼 **SCHÉMA 46.1 — Lire et concevoir**

```
   LIRE                              CONCEVOIR
   ─────────────────────             ──────────────────────────
   ① Qu'est-ce qui circule ?    ⟷    ① Que doit-on servir, à qui ?
   ② Par où ?                   ⟷    ② Quelles contraintes s'imposent ?
   ③ Qu'est-ce qui tombe        ⟷    ③ Qu'accepte-t-on de perdre ?
     si ça tombe ?
   ④ Où peut-on agir ?          ⟷    ④ Quels compromis assume-t-on,
                                        et les a-t-on écrits ?
```

**La symétrie n'est pas décorative** : chaque question de conception se vérifie par la question de lecture correspondante. Une architecture qu'on ne saurait pas lire est une architecture mal conçue.

#### 46.2 ① Que doit-on servir, à qui ?

**La question qu'on saute**, et dont l'absence produit les architectures les plus coûteuses.

| Sous-question | Pourquoi elle compte |
|---|---|
| **Quel service métier ?** | Formulé du point de vue de l'utilisateur, pas de la technique — §35.1 |
| **Combien d'utilisateurs, où ?** | 40 sur un site et 4 000 sur trois continents ne produisent pas la même architecture |
| **Quels usages, à quels moments ?** | Charge continue ou pics · heures ouvrées ou permanent |
| **Quelles données, de quelle sensibilité ?** | **Principe 6** — c'est la donnée qui commande |
| **Qui exploitera ?** | Une personne à mi-temps ou une équipe de vingt |

⚠️ **La dernière est la plus négligée et la plus déterminante.** Une architecture qui exige davantage de compétences que l'organisation n'en possède **échouera**, quelle que soit sa qualité technique. C'est le facteur qui explique le plus d'échecs de modernisation.

#### 46.3 ② Quelles contraintes s'imposent ?

Les six contraintes du §1.4, appliquées au cas.

##### Le vocabulaire professionnel : les exigences non fonctionnelles

Les six contraintes du §1.4 portent un nom dans le métier : ce sont des **exigences non fonctionnelles**. Elles ne décrivent pas *ce que le système fait* — c'est le rôle des exigences fonctionnelles — mais **sous quelles conditions il doit le faire**.

| Exigence | La question qu'elle pose | Ce qui la chiffre |
|---|---|---|
| **Disponibilité** | Combien de temps peut-il être arrêté ? | **Durée d'interruption tolérable** |
| **Reprise** | Combien de données peut-on perdre ? | **Perte de données tolérable** |
| **Performance** | Combien de temps pour répondre ? | Temps de réponse, volume, concurrence |
| **Capacité** | Jusqu'où peut-il croître ? | Nombre d'utilisateurs, volume de données |
| **Sécurité** | Que doit-on protéger, et contre quoi ? | Sensibilité, exposition, obligations |
| **Maintenabilité** | Comment le fait-on évoluer ? | Fréquence des changements, interruptibilité |
| **Exploitabilité** | **Qui le tiendra au quotidien ?** | **Nombre d'exploitants disponibles** |

##### Les trois durées, et pourquoi il ne faut pas les confondre

**Le lecteur entendra deux acronymes en réunion. Ils ne désignent pas la même chose que la tolérance métier, et la confusion est très fréquente.**

| Notion | La question qu'elle pose | Qui la fixe |
|---|---|---|
| **Tolérance métier maximale** | *« Combien de temps puis-je supporter l'arrêt avant que cela devienne inacceptable ? »* | **Le métier**, et lui seul |
| **RTO** — objectif de délai de reprise | *« Sous combien de temps visons-nous effectivement la restauration ? »* | **Un engagement**, pris au regard des moyens |
| **RPO** — objectif de perte de données | *« Quelle quantité de données, exprimée en temps, acceptons-nous de perdre ? »* | Le métier, avec le coût comme contrainte |

⚠️ **La distinction entre les deux premières est celle qu'on manque presque toujours.** Elles peuvent être différentes, et elles le sont souvent :

```
   Tolérance métier   « quatre heures d'arrêt sont supportables »
   RTO visé           « nous nous engageons sur deux heures »
                      → une marge, choisie délibérément
   RTO réel MESURÉ    « la dernière restauration a pris six heures »
                      → ⚠️ l'écart entre l'engagement et le réel
```

> **Le RTO est un objectif, pas une propriété du système.** Un RTO de deux heures affiché sur une architecture dont la restauration n'a jamais été chronométrée est **une intention**, pas un engagement tenable — *principe de preuve*.

**Le RPO se traduit directement en décision d'architecture** :

| RPO exigé | Ce qu'il impose |
|---|---|
| 24 heures | Une sauvegarde quotidienne suffit |
| 8 heures | Trois sauvegardes par jour — §48.1 |
| 15 minutes | **Une réplication**, et probablement asynchrone |
| Zéro perte | **Une réplication synchrone** — coûteuse, et elle ralentit les écritures |

⚠️ **La dernière ligne est celle qui surprend** : exiger zéro perte de données **dégrade la performance**, parce que chaque écriture doit être confirmée des deux côtés avant d'être validée. **C'est un arbitrage, pas un idéal gratuit** — *principe du coût*.

⚠️ **Les deux premières exigences du tableau ci-dessus se chiffrent en durée, et ce sont elles qui déterminent l'essentiel d'une architecture.** *« Il faut que ce soit fiable »* n'est pas une exigence ; *« une interruption de quatre heures en journée est tolérable, une perte de plus de quinze minutes de données ne l'est pas »* en est une — et elle décide à elle seule de la présence ou non d'une redondance.

⚠️ **La dernière est celle que personne n'écrit**, et le §47.3 montre qu'elle fait échouer davantage d'architectures que toutes les autres réunies.

🧪 **EN PRATIQUE — la fiche de contraintes**

```
DISPONIBILITÉ   Interruption tolérable : ......  Perte de données tolérable : ......
PERFORMANCE     Temps de réponse attendu : ......  Volume : ......
COÛT            Budget d'investissement : ......  Budget récurrent : ......
SÉCURITÉ        Sensibilité des données : ......  Exposition nécessaire : ......
CONFORMITÉ      Obligations applicables : ......  Preuve à produire : ......
HISTOIRE        Existant à intégrer : ......  Ce qu'on ne peut pas changer : ......
```

**Les deux premières lignes sont celles qui se chiffrent, et qu'on ne chiffre jamais.** *« Il faut que ce soit disponible »* n'est pas une contrainte ; *« une interruption de quatre heures en journée est tolérable, une perte de données de plus de quinze minutes ne l'est pas »* en est une — et elle détermine à elle seule la moitié de l'architecture.

#### 46.4 ③ Qu'accepte-t-on de perdre ?

> **Principe 7 : concevoir, c'est choisir ce qu'on accepte de perdre.**

**Parce que les six contraintes se contredisent, il faut en dégrader certaines.** La question n'est pas *lesquelles satisfaire* mais **lesquelles sacrifier, et de combien**.

| Ce qu'on peut accepter de perdre | Ce que ça permet |
|---|---|
| De la disponibilité | Une architecture simple, peu coûteuse, exploitable par une personne |
| De la performance | Des contrôles supplémentaires, du chiffrement, de la journalisation |
| Du budget | De la redondance, de la segmentation, des compétences |
| De la simplicité | De la sécurité et de la disponibilité |
| **De la fonctionnalité** | La ligne qu'on n'envisage jamais, et qui règle beaucoup de problèmes |

⚠️ **La dernière ligne mérite un développement.** Beaucoup de complexité d'architecture vient de fonctionnalités marginales : un accès depuis l'extérieur pour trois personnes, un export en temps réel utilisé une fois par mois, une compatibilité avec un système que deux clients utilisent encore. **Renoncer à une fonctionnalité est souvent l'arbitrage le moins cher, et le moins proposé.**

#### 46.5 ④ Quels compromis assume-t-on, et les a-t-on écrits ?

**La différence entre un compromis assumé et un compromis subi** est qu'il est écrit.

🧪 **EN PRATIQUE — le registre des compromis**

| # | Compromis | Contrainte privilégiée | Contrainte dégradée | Conséquence acceptée | Décideur | Revoir si |
|---|---|---|---|---|---|---|
| 1 | Un seul serveur applicatif | Coût | Disponibilité | Interruption de 4 h possible | *(nom)* | Le coût de licence change |
| 2 | Pas de zone démilitarisée | Simplicité | Sécurité | Publication directe, aucun service publié aujourd'hui | *(nom)* | Un service devient public |

**Ce document est le vrai livrable d'une conception.** Le schéma montre le résultat ; le registre montre **pourquoi**, et c'est lui qui permettra, dans dix ans, de répondre à la question du chapitre 4 : *pourquoi c'est comme ça ?*

> **Une architecture livrée sans registre de compromis condamne ses successeurs à les redécouvrir — ou à les juger naïvement.**

---

### Chapitre 47 — Concevoir sous contrainte

#### 47.1 Les arbitrages classiques, et ce qu'ils coûtent

| Arbitrage | Ce qu'on gagne | Ce qu'on perd | Quand il est juste |
|---|---|---|---|
| **Redonder ou non** | Continuité | Coût ×2, complexité, un composant de plus à exploiter | Quand l'interruption tolérable est inférieure au délai de remise en service |
| **Segmenter finement ou non** | Limitation de la propagation | Flux à maintenir, dépannage plus long | Quand les conséquences d'une propagation sont graves |
| **Centraliser ou distribuer** | Simplicité, économies | Dépendance au lien, latence | Quand le lien est fiable et la latence acceptable |
| **Internaliser ou externaliser** | Maîtrise, ou compétences | Compétences à tenir, ou dépendance | Selon ce que l'organisation sait exploiter |
| **Chiffrer partout ou aux frontières** | Confidentialité | Visibilité perdue, complexité de gestion des clés | Selon la sensibilité et la capacité de détection |
| **Authentifier une fois ou à chaque étape** | Confort, ou cloisonnement | Un jeton unique qui ouvre tout, ou de la friction | Selon la sensibilité des étapes |

#### 47.2 L'architecture qui optimise tout n'existe pas

⚠️ **Le réflexe du débutant en conception** : produire une architecture qui coche toutes les cases. Elle est redondée, segmentée, chiffrée, journalisée, authentifiée à chaque étape.

**Ce qui se passe ensuite**, dans l'ordre :

```
Mois 1    L'architecture est validée. Elle est excellente sur le papier.
Mois 6    Le déploiement prend du retard : trop de composants à intégrer.
Mois 12   L'exploitation ne suit pas — deux personnes pour quinze composants.
Mois 18   Des contournements apparaissent pour tenir les délais.
Mois 24   La segmentation est partiellement désactivée « en attendant ».
Mois 36   L'architecture réelle ressemble à celle qu'on voulait éviter,
          avec le coût de celle qu'on a conçue.
```

> **Une architecture qu'une organisation ne sait pas exploiter se dégrade jusqu'à son niveau réel de compétence — en ayant coûté le prix de l'ambition.**

**Ce que ce principe explique, et qui vaut d'être énoncé explicitement** :

| Affirmation courante | Ce que le principe y oppose |
|---|---|
| « L'orchestration de conteneurs est plus moderne » | Elle introduit un système distribué complet à exploiter. **Plus moderne n'est pas plus adapté** |
| « Les microservices sont un signe de maturité » | Ils multiplient les composants et les flux. **La maturité est de savoir les exploiter** |
| « Plusieurs fournisseurs cloud, c'est plus résilient » | C'est deux plateformes à maîtriser au lieu d'une |
| « Plus de segmentation, c'est plus sûr » | Jusqu'au point où les flux deviennent ingérables et sont contournés — §24.2 |
| « Nous avons de la haute disponibilité » | **Une redondance non testée est une croyance** — *principe de preuve* |

> **Formulation générale, à rapprocher du principe du coût** : *un composant techniquement excellent que personne ne sait exploiter dégrade l'architecture au lieu de l'améliorer.*

**Le test à s'appliquer** : *combien de personnes faudra-t-il pour tenir cette architecture, et les avons-nous ?*

#### 47.3 Concevoir pour ce qu'on sait exploiter

| Signe qu'une architecture est trop ambitieuse | Ce qu'on fait |
|---|---|
| Elle exige une compétence que personne n'a | La simplifier, ou acquérir la compétence **avant** |
| Elle comporte plus de composants que d'exploitants | Réduire, ou externaliser une partie |
| Elle suppose des procédures qui n'existent pas | Les écrire, ou choisir un modèle qui s'en passe |
| **Son basculement n'est testable que rarement** | Choisir un modèle testable — §20 |

**La quatrième ligne est celle qu'on découvre le plus tard.** Une redondance qui ne peut être testée qu'une fois par an, pendant une fenêtre difficile à obtenir, **ne sera pas testée** — et une redondance non testée est une croyance.

---

### Chapitre 48 — Quatre conceptions guidées

> **Le vrai exercice de synthèse du cours.** Chaque cas suit dix étapes — et l'étape ④ est celle qui manque partout ailleurs.

#### 48.0 Avertissement sur les chiffres de ce chapitre

⚠️ **Les valeurs employées dans les corrigés qui suivent — 0,3 personne, 0,6 personne, un coût multiplié par 2,5 — sont des données de scénario, pas des ratios universels.**

Elles servent à rendre un arbitrage lisible : *cette option consomme deux fois plus d'exploitation que celle-là*. **Elles ne se transposent pas.** La charge réelle d'exploitation d'un composant dépend de l'outillage, du niveau d'automatisation, des compétences en place, du nombre d'environnements et des engagements de service.

> **Ce qu'il faut retenir n'est pas le chiffre. C'est la démarche : chiffrer avant d'arbitrer, et confronter le total à la capacité réellement disponible.**

**Comment obtenir vos propres chiffres** : demandez à l'équipe d'exploitation combien de temps elle consacre par mois à un composant comparable déjà en service. C'est la seule source fiable, et elle est disponible en une conversation.

#### 48.1 Le déroulé en dix étapes

```
 ①  LE BESOIN            Quel service, pour qui, avec quelles données
 ②  LES CONTRAINTES      Chiffrées. Les non chiffrées se demandent
 ③  PREMIÈRE PROPOSITION La solution qui vient spontanément
 ④  CRITIQUE             On applique la grille du chapitre 49
                         A SA PROPRE proposition
 ⑤  SECONDE PROPOSITION  Ce que la critique fait changer
 ⑥  LES COMPROMIS        Le registre
 ⑦  LES FLUX             Une requête type, en douze étapes
 ⑧  LES RUPTURES         L'arbre de dépendance
 ⑨  L'EXPLOITATION       Qui tiendra cela, et le sait-on faire ?
 ⑩  CE QU'ON IGNORE      Ce qu'il reste à vérifier
```

⚠️ **Une remarque essentielle avant de commencer** :

> **Il n'existe pas *le* corrigé d'une architecture.** Chaque cas ci-dessous admet **plusieurs réponses défendables**. Ce qui distingue une bonne réponse d'une mauvaise n'est pas le schéma produit — c'est **la qualité de l'arbitrage énoncé et la lucidité sur ce qui reste à vérifier**.
>
> Si votre proposition diffère de celle présentée et que vous savez dire quelle contrainte vous avez privilégiée et laquelle vous avez dégradée, **votre réponse est valide**.

> Format des cas : le besoin · les contraintes · deux options · la critique · l'architecture retenue · le registre.

#### 48.2 Cas 1 — Une application interne pour 200 utilisateurs

**Le besoin** : une application de gestion, 200 utilisateurs sur un site, données internes non sensibles, budget contraint, une personne à mi-temps pour exploiter.

**Les contraintes chiffrées** :

```
DISPONIBILITÉ   Interruption tolérable : une demi-journée
                Perte de données tolérable : 24 h (sauvegarde quotidienne)
COÛT            Investissement limité · exploitation : 0,5 personne
SÉCURITÉ        Interne uniquement · aucune exposition externe
HISTOIRE        Aucun existant
```

**Deux options** :

| | **Option A — simple** | **Option B — redondée** |
|---|---|---|
| Composants | 1 applicatif, 1 base | 2 applicatifs, 1 répartiteur, base répliquée |
| Coût | ×1 | **≈ ×2,5** avec l'exploitation |
| Interruption en cas de panne | 2 à 4 h | Quelques minutes |
| Exploitants nécessaires | 0,3 personne | **≈ 1 personne** |

⚠️ **Le réflexe à installer ici, et à appliquer partout** :

| Ce que le schéma montre | Ce qu'il faut vérifier |
|---|---|
| Redondance **logique** | Redondance **physique** — hôtes, stockage, site, alimentation |
| Séparation **logique** | Séparation **physique** — ou mécanisme équivalent |
| Chemin **logique** | Chemin **réseau** réel — routage, traduction d'adresses |
| Service **logique** | Processus **réels** qui le rendent |

**Retenu : l'option A.** L'interruption tolérable est d'une demi-journée ; l'option B résout un problème qui n'existe pas, et **exige deux fois plus d'exploitation que l'organisation ne peut fournir** — §47.3.

**④ Critique de sa propre proposition** — grille du chapitre 49 :

| Point | Constat |
|---|---|
| ① Fort | Proportionnée à la capacité d'exploitation. Deux composants, 0,3 exploitant |
| ② Faible | Aucune tolérance de panne · la sauvegarde quotidienne laisse 24 h de saisie exposée |
| ③ Rupture | Les deux composants — **et l'hôte de virtualisation s'ils le partagent** — *principe de preuve* |
| ④ Dépendance cachée | **L'authentification** : contre quoi ? Si c'est l'annuaire, il devient une troisième rupture invisible |
| ⑤ Risque principal | Une panne matérielle un lundi matin : une demi-journée d'arrêt, acceptable · **et jusqu'à 24 h de saisie perdue, qui ne l'est peut-être pas** |
| ⑥ Amélioration | **Une seule** : passer la sauvegarde à trois fois par jour. Coût quasi nul, **ramène la perte maximale de 24 h à 8 h** |

**⑤ Ce que la critique fait changer** : l'architecture reste l'option A, **avec une sauvegarde trois fois par jour**. La critique n'a pas remis en cause la conception — elle a corrigé un paramètre dont personne n'avait chiffré l'effet.

**⑥ Registre des compromis** :

| Compromis | Privilégié | Dégradé | Conséquence acceptée | Revoir si |
|---|---|---|---|---|
| Aucune redondance | Coût, exploitabilité | Disponibilité | Interruption jusqu'à 4 h | L'application devient critique |
| Sauvegarde 3 fois par jour | Coût | Perte de données | Jusqu'à 8 h de saisie perdue **au lieu de 24 h** | Le volume de saisie augmente |
| Authentification contre l'annuaire | Simplicité, gouvernance | Disponibilité | L'annuaire devient une dépendance | L'annuaire devient instable |

**⑨ L'exploitation** : 0,3 personne. L'organisation en dispose. Validé.

**⑩ Ce qu'on ignore encore** : contre quoi l'application authentifie · si l'hôte est partagé avec d'autres services critiques · **si la restauration de la sauvegarde a déjà été testée** — *principe de preuve*.

#### 48.3 Cas 2 — Un service exposé sur Internet

**Le besoin** : publier un portail client, 3 000 clients, données personnelles, interruption tolérable de 2 h en journée.

**Les deux options portent sur l'exposition** :

| | **Option A — publication directe** | **Option B — mandataire inverse** |
|---|---|---|
| Le serveur est joignable | Directement depuis Internet | **Uniquement par le mandataire** |
| Authentification | Dans l'application | **Possible avant l'application** |
| Composants | 2 | 3 |
| Une faille applicative | Exploitable directement | **Nécessite d'abord de passer le mandataire** |

**Retenu : l'option B.** Le surcoût d'un composant est faible ; le gain est structurel — l'application n'est plus exposée, et l'authentification peut précéder son atteinte.

⚠️ **Ce que le registre doit écrire, et qu'on oublie** : le mandataire voit tout le trafic en clair. **C'est un compromis, pas un pur gain** — on concentre le risque en un point pour le retirer d'un autre.

#### 48.4 Cas 3 — Une extension cloud d'un existant

**Le besoin** : ajouter un service accessible depuis l'extérieur, en conservant les identités et une partie des données sur site.

**La question qui décide** : *que se passe-t-il si le lien tombe ?* — §40.3

| Option | Le lien tombe | Coût |
|---|---|---|
| **A — identités synchronisées** | Le cloud continue de fonctionner en autonomie | Une synchronisation à exploiter et superviser |
| **B — identités interrogées en direct** | **Le cloud devient inaccessible** | Plus simple, plus fragile |

**Retenu : l'option A**, avec une condition écrite au registre : **la synchronisation doit être supervisée**, faute de quoi son arrêt passera inaperçu jusqu'à ce que les mots de passe divergent — §40.2.

#### 48.5 Cas 4 — Une reprise d'existant

> **Le cas réel**, et le plus difficile. C'est celui que vous rencontrerez.

**La situation** : une application métier de 2009, base ancienne, client lourd sur 300 postes, un serveur unique jamais redémarré depuis quatorze mois, éditeur toujours actif mais version non supportée. Il faut « moderniser ».

**Ce qu'un débutant propose** : tout refaire.
**Ce que le chapitre 4 enseigne** : commencer par comprendre pourquoi c'est comme ça.

**Les quatre questions préalables** :

| Question | Pourquoi |
|---|---|
| **Qu'est-ce qui dépend de ce système ?** | Souvent plus que prévu — des exports, des interfaces oubliées |
| **Pourquoi n'a-t-il jamais été mis à jour ?** | La réponse est presque toujours *une dépendance qu'on ne sait pas refaire* |
| **Que se passe-t-il s'il tombe demain ?** | Cela chiffre l'urgence réelle |
| **Combien de temps l'éditeur le supportera-t-il ?** | Cela fixe l'horizon |

**Les trois stratégies possibles, et leurs compromis** :

| Stratégie | Ce qu'elle résout | Ce qu'elle coûte | Quand elle est juste |
|---|---|---|---|
| **Remplacer** | Tout | Long, cher, risqué, mobilise le métier | Quand l'éditeur arrête, ou que le besoin a changé |
| **Encapsuler** | L'exposition et la surveillance | Ne résout pas l'obsolescence | Quand le remplacement n'est pas finançable maintenant |
| **Sanctuariser** | Le risque immédiat | Fige le système, dette différée | **Quand rien d'autre n'est possible — et à condition de l'écrire** |

**Retenu, dans la majorité des cas réels : encapsuler, puis planifier le remplacement.** Isoler le système dans un segment dédié, placer un mandataire devant, journaliser ses accès, et inscrire son remplacement au plan avec une échéance.

⚠️ **Ce qui distingue une sanctuarisation d'un abandon** : une date de réexamen, un propriétaire nommé, et un compromis écrit. Sans ces trois éléments, ce n'est pas une décision — c'est un renoncement qui se déguise. **C'est exactement la doctrine du volume Maintien en condition de sécurité.**

#### 48.6 Le capstone — une conception qui évolue

> **L'exercice principal de la Partie IX.** Une architecture ne se conçoit pas d'un coup : elle se corrige à chaque contrainte nouvelle. Voici comment.

##### Version 0 — le besoin brut

> *Une organisation de 300 personnes veut publier un portail permettant à ses 600 clients de consulter leurs dossiers et de déposer des documents.*

**Rien d'autre.** Aucune contrainte chiffrée. C'est la situation réelle, et la première tâche est de le dire.

##### Version 1 — votre première proposition

**Avant de lire la suite, dessinez.** Une page, dix minutes.

Une proposition raisonnable ressemble à ceci :

```
   Internet ──► [ pare-feu ] ──► [ mandataire ] ──► [ portail ] ──► [ base ]
```

**Quatre composants.** C'est proportionné à un besoin qu'on ne connaît pas encore.

---

##### ⚡ ÉVÉNEMENT 1 — « L'entreprise exige 99,95 % de disponibilité »

**Ce que cela signifie réellement**, et c'est la première chose à faire :

| Engagement | Indisponibilité tolérée par an | Par mois |
|---|---|---|
| 99 % | 3,65 jours | 7 h 18 |
| 99,9 % | 8 h 45 | 43 min |
| **99,95 %** | **4 h 22** | **21 min** |
| 99,99 % | 52 min | 4 min |

⚠️ **Vingt et une minutes par mois** signifie qu'**aucune intervention manuelle n'est possible** : le temps de détecter, comprendre et agir dépasse déjà le budget. **Il faut donc de la bascule automatique.**

**Ce qui change** :

```
   Internet ──► [ pare-feu ×2 ] ──► [ mandataire ×2 ] ──► [ portail ×2 ]
                                                              │
                                                     [ base répliquée ]
```

**Ce que cela coûte, et qu'il faut écrire** : le nombre de composants double · une bascule automatique à configurer **et à tester** · les sessions doivent être partagées, sinon la redondance ne protège pas les utilisateurs en cours — §31.2. **Un composant de plus** : le magasin de sessions.

---

##### ⚡ ÉVÉNEMENT 2 — « Ce sont des données de santé »

**Ce que cela change** : la contrainte de sécurité devient dominante, et des obligations s'ajoutent.

**Quatre conséquences d'architecture** :

| Conséquence | Effet sur le schéma |
|---|---|
| Chiffrement de bout en bout exigé | **Le mandataire passe en mode C** — terminaison puis rechiffrement, §12.3 |
| Traçabilité des accès aux dossiers | La journalisation applicative devient **une exigence, pas un confort** |
| Cloisonnement renforcé | Une frontière entre le portail et la base, distincte de la DMZ |
| Localisation des données | **Contraint le choix d'hébergement** — potentiellement, tout ce qui précède |

⚠️ **Ce que beaucoup oublient** : les **sauvegardes** portent les mêmes données et les mêmes obligations. Et les **environnements de recette**, s'ils contiennent des données réelles — §32.2.

**Ce qui change** : le mode de terminaison, un segment supplémentaire, une journalisation applicative détaillée, et **une revue de tous les endroits où la donnée existe**.

---

##### ⚡ ÉVÉNEMENT 3 — « Le budget est réduit de 30 % »

**La première réaction, et elle est mauvaise** : retirer un exemplaire de chaque composant.

**La bonne démarche** : reprendre les contraintes et demander **laquelle on dégrade**.

| Option | Ce qu'on perd | Ce qu'on garde |
|---|---|---|
| Retirer la redondance du portail | **L'engagement de 99,95 %** — il faut le renégocier | La sécurité |
| Retirer le chiffrement interne | Une exigence liée aux données de santé | **Non négociable** |
| Retirer le magasin de sessions | La redondance ne protège plus les sessions en cours | Une redondance partielle |
| **Renoncer au dépôt de documents** | Une fonctionnalité | **Tout le reste**, et une simplification importante |

⚠️ **La quatrième ligne est celle qu'on n'envisage jamais** — §46.4. Le dépôt de documents est ce qui impose le stockage, les analyses de contenu, une part importante des obligations et une bonne partie du volume. **Y renoncer en version 1, quitte à l'ajouter plus tard, peut absorber les 30 % à lui seul.**

> **Concevoir, c'est choisir ce qu'on accepte de perdre. Et la fonctionnalité est un candidat légitime.**

---

##### ⚡ ÉVÉNEMENT 4 — « Il y aura deux sites »

❓ **La question à poser avant de dessiner quoi que ce soit** : *deux sites pour quoi faire ?*

| Motif invoqué | Ce que cela impose réellement |
|---|---|
| **Continuité en cas de sinistre** | Une réplication des données · **un basculement testé** · un plan documenté |
| **Répartition de charge** | Des données cohérentes entre les deux — **très difficile** |
| **Proximité géographique** | Une réplication en lecture seule peut suffire |
| **« Parce qu'on a deux salles »** | **Rien.** Ce n'est pas une contrainte |

⚠️ **Le quatrième cas est très répandu**, et il produit des architectures à deux sites dont le second n'a jamais été testé — et ne fonctionnerait pas.

**Si le motif est la continuité**, ce qui change :

```
   SITE A                              SITE B
   [ pare-feu ×2 ]                     [ pare-feu ×2 ]
   [ mandataire ×2 ]                   [ mandataire ×2 ]
   [ portail ×2 ]                      [ portail ×2 ]
   [ base primaire ] ══réplication══► [ base secondaire ]
          │                                   │
          └────── résolution de noms ─────────┘
                  qui bascule les clients

   ⚠️ Trois questions nouvelles :
      · la réplication est-elle synchrone ? sinon, combien perd-on ?
      · qui décide de basculer, et en combien de temps ?
      · les certificats et l'annuaire sont-ils disponibles sur les deux sites ?
```

**Ce que cela coûte** : le double de tout · **un basculement à tester au moins deux fois par an** · une décision de bascule qui doit être prise par quelqu'un, la nuit.

---

##### ⚡ ÉVÉNEMENT 5 — « L'équipe d'exploitation compte trois personnes »

> **L'événement qui remet tout en cause**, et c'est volontaire.

**Le calcul** :

| Composant | Exploitants nécessaires |
|---|---|
| Deux sites, chacun complet | ≈ 1,5 |
| Base répliquée avec bascule testée | ≈ 0,5 |
| Magasin de sessions | ≈ 0,2 |
| Chiffrement de bout en bout, certificats | ≈ 0,3 |
| Journalisation applicative détaillée | ≈ 0,3 |
| **Total pour ce seul service** | **≈ 2,8** |

⚠️ **Trois personnes exploitent tout le système d'information**, pas seulement ce portail. **L'architecture consomme la quasi-totalité de la capacité pour un seul service.**

**Selon le §47.2, elle se dégradera** : la bascule ne sera pas testée, les certificats expireront, la réplication tombera sans que personne ne le voie.

**Les trois options honnêtes** :

| Option | Ce qu'elle implique |
|---|---|
| **Recruter** | Un coût récurrent, et un délai de plusieurs mois |
| **Externaliser l'exploitation** | Un prestataire · **et les accès privilégiés qui vont avec** — §38.4 |
| **Simplifier l'architecture** | Renégocier l'engagement de disponibilité |

⚠️ **La troisième est très répandue, et rarement avouée.** Elle suppose de retourner voir le métier et de dire : *« l'engagement de 99,95 % coûte deux exploitants que nous n'avons pas. Que se passe-t-il réellement si le portail est indisponible quatre heures ? »*

**Dans la majorité des cas, la réponse est « pas grand-chose »** — et l'engagement avait été énoncé sans avoir été chiffré.

---

##### ⑩ La question finale

> ### Expliquez ce que vous avez volontairement décidé de ne pas faire.

**C'est le livrable qui distingue un concepteur d'un assembleur de briques.**

**Une réponse attendue ressemble à ceci** :

> *Nous avons renoncé au dépôt de documents en version 1, ce qui absorbe la contrainte budgétaire et supprime une part importante des obligations liées au stockage. Nous avons renoncé au second site, faute de capacité d'exploitation pour le maintenir en état de fonctionner — un second site non testé aurait donné une illusion de continuité. Nous avons renégocié l'engagement à 99,9 %, ce qui autorise une intervention humaine et divise par deux la complexité. Nous avons conservé le chiffrement de bout en bout et la journalisation applicative, qui ne sont pas négociables au regard des données traitées.*
>
> *Ce que nous n'avons pas pu vérifier : le délai réel de restauration de la base · la capacité du lien Internet à absorber le volume · si l'équipe sait exploiter un magasin de sessions.*

⚠️ **Remarquez ce que cette réponse contient** : quatre renoncements motivés, deux non-négociables, et trois incertitudes déclarées. **Aucune ligne ne décrit un composant.**

##### Les cinq enseignements du capstone

| # | Enseignement |
|---|---|
| **1** | Une contrainte non chiffrée ne se conçoit pas — **elle se demande** |
| **2** | Un engagement de disponibilité se traduit en **minutes par mois**, et cela change tout |
| **3** | Une contrainte nouvelle ne s'ajoute pas : **elle oblige à en dégrader une autre** |
| **4** | **Renoncer à une fonctionnalité est un arbitrage légitime**, et souvent le moins cher |
| **5** | **La capacité d'exploitation est la contrainte qui décide**, et elle arrive toujours en dernier |

#### 48.7 🔬 Mini-labs 11 et 12

**🔬 Mini-lab 11 — Concevoir pour trois organisations** · *45 min · 🟠*
Même besoin — publier un service de suivi pour des clients — chez Atelier Martin, HELIOMED et Novaris. Produire trois architectures différentes, et **justifier chaque écart par une contrainte, jamais par la taille** — *principe de la contrainte*.

**🔬 Mini-lab 12 — Le registre des compromis** · *30 min · 🟠*
À partir d'une architecture fournie, reconstituer le registre des compromis qui l'a produite : quelle contrainte a été privilégiée à chaque endroit, laquelle a été dégradée, et ce qui devrait déclencher un réexamen.

---

### Chapitre 49 — Critiquer une architecture

> La compétence de fin de cours, et la plus délicate à exercer.

#### 49.1 La grille en six points

```
  ①  POINT FORT             Ce qui est bien pensé, et pourquoi
  ②  POINT FAIBLE           Ce qui est fragile, et sous quelle condition
  ③  POINT DE RUPTURE       Ce qui n'a pas de doublure
  ④  DÉPENDANCE CACHÉE      Ce dont tout dépend et qui n'est pas dessiné
  ⑤  RISQUE PRINCIPAL       Le scénario le plus probable et le plus coûteux
  ⑥  AMÉLIORATION           Le meilleur rapport effet/coût — une seule
```

**L'ordre compte, et le premier point aussi.** Une critique qui commence par les faiblesses ne sera pas entendue par ceux qui ont conçu l'architecture. **Commencer par ce qui est bien pensé n'est pas une politesse : c'est une condition d'efficacité.**

#### 49.2 Ce qui distingue une critique utile

| Critique inutile | Critique utile |
|---|---|
| « Il n'y a pas de zone démilitarisée » | « Aucun service n'est publié aujourd'hui. Si l'un devait l'être, la publication directe deviendrait un problème — c'est le déclencheur à surveiller » |
| « L'applicatif n'est pas redondé » | « L'applicatif est unique. Est-ce un arbitrage documenté ? Si oui, quelle interruption a été jugée tolérable ? » |
| « Cette passerelle ne devrait pas exister » | « Cette passerelle date de 2018 et porte un export vers le contrôle de gestion. Le besoin existe-t-il encore, et peut-il passer autrement ? » |
| « C'est du legacy » | « Ce composant a quinze ans. Que dépend de lui, et l'éditeur le supporte-t-il encore ? » |

⚠️ **Le point commun des critiques utiles** : elles **posent une question** au lieu d'énoncer un verdict, et elles supposent que la personne en face avait une raison — chapitre 4.

#### 49.3 Les cinq erreurs du critique débutant

| Erreur | Pourquoi c'est une erreur |
|---|---|
| **Juger sans demander l'histoire** | §4.4 — chaque anomalie a une date |
| **Comparer à un idéal théorique** | Aucune architecture réelle n'y ressemble |
| **Traiter la taille comme une norme** | *Principe de la contrainte* |
| **Proposer dix améliorations** | Aucune ne sera faite. **Une seule sera peut-être faite** |
| **Oublier le coût de sa propre proposition** | *Principe du coût* — ajouter n'est jamais gratuit |

**La quatrième est la plus coûteuse en crédibilité.** Une liste de dix recommandations est reçue comme un jugement global ; une recommandation unique, chiffrée et justifiée est reçue comme une contribution.

#### 49.4 Formuler une critique qui sera entendue

🧪 **EN PRATIQUE — le format en cinq lignes**

```
CE QUI FONCTIONNE      [1 à 2 éléments, précis]
CE QUE J'AI OBSERVÉ    [le constat, factuel, sans jugement]
CE QUE JE N'AI PAS SU  [ce qui manque pour conclure — souvent l'histoire]
LE RISQUE              [scénario, probabilité, conséquence]
CE QUE JE PROPOSE      [une action, son coût, son effet attendu]
```

**La troisième ligne est celle qui change la réception.** Dire *« je n'ai pas su pourquoi l'applicatif n'est pas redondé »* ouvre une conversation ; dire *« l'applicatif n'est pas redondé »* ferme la porte.

#### 49.5 🔬 Mini-lab 13 — Critiquer trois architectures

**Objectif** — Appliquer la grille en six points et produire une critique en cinq lignes.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** chapitres 36, 47, 49

Trois architectures : celle d'Atelier Martin · celle du mini-lab 7 · celle du §37.4, avec `HERMES`.

---

**Corrigé — Atelier Martin**

| Point | Constat |
|---|---|
| ① Fort | **L'architecture est proportionnée** : deux segments, peu de composants, exploitable par une personne à mi-temps. C'est cohérent |
| ② Faible | Les machines à commande numérique sont sur le segment bureautique |
| ③ Rupture | Le contrôleur d'annuaire unique · le pare-feu tout-en-un |
| ④ Dépendance cachée | Le prestataire local, **avec un accès permanent et aucune traçabilité** |
| ⑤ Risque principal | Un poste bureautique compromis atteint les machines de production. **Conséquence : arrêt de production, et potentiellement sûreté** |
| ⑥ Amélioration | **Une seule** : séparer le segment atelier. Coût faible, effet majeur |

**La critique en cinq lignes** :

> *Ce qui fonctionne : l'architecture est dimensionnée pour ce que l'organisation peut exploiter, ce qui est rare et précieux.*
> *Ce que j'ai observé : les deux machines à commande numérique sont sur le même segment que les postes bureautiques.*
> *Ce que je n'ai pas su : si cette situation résulte d'un choix ou de l'absence de question posée.*
> *Le risque : un poste compromis — une voie d'entrée majeure — atteint directement les machines de production. Conséquence : arrêt de production, et selon les machines, question de sûreté.*
> *Ce que je propose : séparer le segment atelier. Un commutateur et une règle de filtrage sur le boîtier existant. Coût faible, c'est la seule action que je recommande cette année.*

⚠️ **Ce que la critique ne dit pas** : que l'absence d'annuaire redondé est un problème. Elle en est un techniquement, et **elle n'est pas la priorité** — §49.3, quatrième erreur.

⚠️ **Cohérence avec le §36.4** : la grille en six points **relève** six éléments, la critique formulée **n'en propose qu'un**. Les cinq autres constats servent à établir que le sixième est bien le plus urgent — ils ne sont pas énoncés en réunion.

---

### Chapitre 50 — Ce qu'un schéma ne dira jamais

> **Clôture du cours.** Il apprend la leçon qui empêche de terminer ce livre avec une confiance excessive.

#### 50.1 Le tableau visible / invisible

| Ce qu'un schéma montre | Ce qu'il ne montrera jamais |
|---|---|
| Les segments et les zones | **Les procédures d'exploitation** |
| Les pare-feu | **Les règles réellement en place** |
| Les serveurs | **Ce qui s'y exécute vraiment** |
| Les liens | **Ce qui les traverse** |
| Les flux dessinés | **Les flux de dépendance** — principe des trois flux |
| Les services | **Les contraintes métier qui les ont produits** |
| La redondance | **Si elle a déjà été testée** |
| Les composants | **Les compétences pour les exploiter** |
| L'agencement | **Les décisions et les arbitrages** |
| Le nominal | **Les contournements en place depuis trois ans** |
| Les versions, parfois | **Les correctifs réellement appliqués** |
| L'instantané | **L'histoire, et ce qui est en cours de migration** |

**Les quatre dernières lignes font la leçon.** Un schéma décrit un système ; il ne décrit ni l'organisation qui le tient, ni l'histoire qui l'a produit, ni l'écart entre l'intention et le réel.

#### 50.2 Les deux écarts symétriques

| Écart | Fréquence | Comment on le détecte |
|---|---|---|
| **Dessiné et jamais construit** | Fréquent | Le composant n'apparaît dans aucun inventaire, aucun journal, aucune facture |
| **Construit et jamais dessiné** | **Plus fréquent encore** | Un flux observé sans origine documentée · une machine qui répond et n'est nulle part |

⚠️ **Le second est le plus dangereux.** Il désigne exactement ce que le volume Asset Management appelle un actif orphelin ou une informatique parallèle : quelque chose existe, fonctionne, expose — et n'est connu de personne.

#### 50.3 Comment on vérifie

| Méthode | Ce qu'elle révèle | Coût |
|---|---|---|
| **Suivre un flux en vrai**, avec l'exploitation | L'écart entre le chemin dessiné et le chemin réel | Une demi-journée |
| **Comparer avec l'inventaire** | Ce qui existe et n'est pas dessiné | Selon la qualité de l'inventaire |
| **Lire les règles de pare-feu** | Ce qui est réellement autorisé, contre ce qui est supposé l'être | Quelques heures, souvent instructives |
| **Regarder les journaux** | Les flux qui existent vraiment | Variable |
| **Demander à quelqu'un d'ancien** | L'histoire, les contournements, les raisons | **Une heure, le meilleur rapport du tableau** |

⚠️ **La dernière ligne est la plus efficace et la moins pratiquée.** Une conversation d'une heure avec quelqu'un présent depuis dix ans apprend davantage sur une architecture que trois jours de lecture de documents.

#### 50.4 La phrase de clôture

> ### Une architecture dessinée n'est pas une architecture réelle.

**Ce que cela impose** :

| Devant un schéma | La bonne posture |
|---|---|
| Il est complet | **Il ne l'est jamais** — la question est de savoir de combien |
| Il est à jour | **Datez-le**, et demandez ce qui a changé depuis |
| Il est vrai | Il représente une intention. Vérifiez ce qui a été construit |
| Il est neutre | **Il a été fait pour quelqu'un** — §5.5 |

#### 50.5 🔬 Mini-lab 14 — Dessiner l'architecture de votre organisation

**Objectif** — Produire un schéma, puis lister ce qu'il tait.
**Durée** 2 h · **Difficulté** 🔴 avancé · **Prérequis** l'ensemble du cours

```
1. Dessinez l'architecture de votre organisation, ou d'un service
   que vous connaissez. Une page, à la main.

2. Appliquez les sept passes du chapitre 36 à VOTRE schéma.

3. Listez les onze éléments du §3.4 qui n'y figurent pas.

4. Écrivez les trois questions que vous ne savez pas trancher.

5. Allez poser ces trois questions.
```

**Ce que l'exercice produit systématiquement** : entre trois et six découvertes, dont au moins une concerne un flux ou un composant dont l'existence n'était pas connue de la personne qui a dessiné.

#### 50.6 🔴 FIL ROUGE — décembre 2025 : ce qu'Amélie a compris

*Dernier épisode du cours. Il se raccorde au premier chapitre du volume Asset Management.*

Le 19 décembre, Amélie remet à Claire Nadeau un document de deux pages. Il ne contient aucun inventaire.

**Page 1 — le schéma redessiné.** Le même que celui de mars 2023, avec onze ajouts au crayon : la résolution de noms, l'annuaire relié à tout, la synchronisation d'horloge, le réseau d'administration, les 620 postes, les 180 nomades, la passerelle d'accès distant, le site de Nantes, les postes de prestataires, la collecte de journaux, et une zone marquée d'un point d'interrogation : *services en ligne — nombre inconnu*.

**Page 2 — ce que le schéma ne dit pas.** Vingt-trois lignes, chacune une question sans réponse.

**Ce que Claire lui dit en le lisant** :

> *« C'est la première fois en trois ans que je vois ce document. »*

**Ce qu'Amélie écrit en conclusion**, et qui est la phrase qui ouvre le volume suivant :

> *Le schéma de mars 2023 n'était pas faux. Il montrait ce que quelqu'un avait choisi de montrer, à un moment, pour une raison. Mon travail ne consiste pas à le corriger. Il consiste à savoir de combien il s'écarte de ce qui existe — et à écrire cet écart.*

**Le 5 janvier 2026, sa mission d'inventaire démarre.** Elle sait ce qu'elle regarde.

---

> ### 🎓 Ce que vous savez faire
>
> **Lire**
> ☐ Poser les quatre questions du lecteur devant n'importe quel schéma
> ☐ Appliquer les sept passes dans l'ordre, et produire une lecture d'une page
> ☐ Distinguer trois familles de flux, et savoir laquelle arrête un service
> ☐ Suivre une requête en douze étapes, dont sept ne sont pas dessinées
> ☐ Reconnaître une strate ancienne à trois signes convergents
> ☐ Identifier les points de rupture, y compris ceux qui ne sont reliés à rien
>
> **Comprendre**
> ☐ Expliquer ce que chaque composant résout et ce qu'il coûte
> ☐ Reconstituer l'arbitrage qui a produit une architecture
> ☐ Dire à partir de quelle contrainte un composant devient nécessaire
> ☐ Construire l'arbre de dépendance d'un service métier
> ☐ Dire où l'on peut agir, et où c'est structurellement impossible
>
> **Concevoir et critiquer**
> ☐ Chiffrer des contraintes plutôt que de les énoncer
> ☐ Proposer une architecture proportionnée à ce que l'organisation sait exploiter
> ☐ Écrire un registre des compromis
> ☐ Critiquer en six points, et ne recommander qu'une seule action
> ☐ Formuler une critique en cinq lignes qui sera entendue
>
> **Savoir ce qu'on ne sait pas**
> ☐ Lister ce qu'un schéma ne dit pas
> ☐ Distinguer ce qui a été dessiné et jamais construit de l'inverse
> ☐ Poser trois questions plutôt qu'un jugement
>
> ---
>
> **Ce que ce cours ne vous a pas appris** : dimensionner, choisir un produit, administrer un composant, concevoir un système à forte contrainte. Ces métiers existent, et ils s'apprennent ailleurs.
>
> **Ce que seule la pratique donne** : le sens de ce qui va casser avant que ça casse, la mémoire des architectures qu'on a vues échouer, et la patience de demander l'histoire avant de juger.

---


## Cas de synthèse

---

### Cas A — Le schéma qu'on vous donne le premier jour

> **Durée** 2 h · **Livrables** : lecture en sept passes · liste de l'invisible · trois questions
> **Prérequis** : chapitres 3, 4, 36, 50

#### A.1 La situation

Vous arrivez comme référent sécurité dans une organisation de 700 personnes, secteur des services, trois sites. On vous remet un schéma daté de **mars 2021** et un accès en lecture à l'outil d'inventaire.

```
                          Internet
                              │
                        [ FW-EXT ]
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   [ WEB-PUB ]          [ MAIL-RELAY ]        [ VPN-GW ]
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                        [ FW-INT ]
                              │
   ┌──────────────┬───────────┼───────────┬──────────────┐
   │              │           │           │              │
[ APP-01 ]   [ DB-01 ]   [ FILE-01 ]  [ DC-01 ]    [ SAUV-01 ]
                              │
                     [ segment postes ]
```

**Informations complémentaires** :

```
· L'outil d'inventaire compte 214 machines. Le schéma en montre 8.
· Le site de Bordeaux a été ouvert en 2023.
· Une migration de messagerie vers un service en ligne a eu lieu en 2024.
· MAIL-RELAY existe toujours dans l'inventaire.
· L'auteur du schéma a quitté l'organisation en 2022.
```

#### A.2 Les questions

| # | Question |
|---|---|
| 1 | Appliquez les sept passes. Que produisez-vous ? |
| 2 | Combien de zones, et lesquelles sont réellement matérialisées ? |
| 3 | Que manque-t-il, et pourquoi ? |
| 4 | Quels éléments ont probablement changé depuis mars 2021 ? |
| 5 | Quelles **trois questions** posez-vous, et à qui ? |
| 6 | Quatre anomalies sont insérées dans le dossier. Lesquelles ? |

#### A.3 Corrigé — les sept passes

**① LES ZONES** — Trois apparentes : extérieur, une zone entre les deux pare-feu, l'interne. **La seconde frontière existe** — c'est `FW-INT` — ce qui est rare et bon signe.

⚠️ **Mais** : rien ne matérialise de frontière **à l'intérieur** de la zone interne. `DC-01`, `DB-01` et le segment des postes semblent joignables entre eux. §24.1.

**② L'ENTRÉE** — Trois entrées dessinées : web, messagerie, accès distant. **Une quatrième n'est pas dessinée : l'administration** — §27.3. Et une cinquième, invisible : les postes eux-mêmes, qui ne figurent que comme « segment postes » sans détail.

**③ LES DONNÉES** — `DB-01` et `FILE-01` sont dessinés. Les copies ne le sont pas : réplicas, environnements de recette, exports, et depuis 2024 **les données de messagerie chez un fournisseur** — §32.2.

**④ L'IDENTITÉ** — `DC-01` est dessiné, **relié à rien**. Cas canonique du §1.1. Et depuis la migration de 2024, une question nouvelle : **la messagerie en ligne s'authentifie-t-elle contre `DC-01`, ou possède-t-elle ses propres identités ?**

**⑤ LES FLUX** — Une requête externe suit les étapes du §29.1. Aucun des sept flux invisibles n'est représenté.

**⑥ LES RUPTURES** — Au moins six, dont trois invisibles :

| Composant | Rupture ? | Visible ? |
|---|---|---|
| `FW-EXT`, `FW-INT` | Oui, sauf redondance non dessinée | ✅ |
| `APP-01`, `DB-01` | **Oui**, uniques | ✅ |
| `VPN-GW` | Oui, pour les nomades | ✅ |
| Résolution de noms | **Oui** | ❌ |
| `DC-01` | **Oui**, unique | ✅ dessiné, ❌ non relié |
| Certificats | **Oui**, à date connue | ❌ |

**⑦ L'INVISIBLE** — Onze éléments manquants (§3.4), plus quatre propres au dossier : **le site de Bordeaux**, ouvert deux ans après le schéma · **le service de messagerie en ligne** de 2024 · **les 206 machines** que l'inventaire connaît et que le schéma ignore · **les prestataires**.

#### A.4 Corrigé — les quatre anomalies insérées

| # | Anomalie | Ce qu'elle révèle |
|---|---|---|
| **1** | **`MAIL-RELAY` existe encore dans l'inventaire après la migration de 2024** | Un composant **construit, dessiné, et devenu inutile** — mais toujours exposé. C'est un actif zombie, encore joignable depuis Internet |
| **2** | **Le site de Bordeaux n'est pas sur le schéma** | Le schéma date de 2021, le site de 2023. **Ce n'est pas une erreur, c'est une péremption** — §50.4 |
| **3** | **8 machines dessinées contre 214 inventoriées** | Le schéma est une vue logique de rôles, pas de machines — §3.1. Mais l'écart de 206 n'est documenté nulle part |
| **4** | **`DC-01` est unique et relié à rien** | Deux problèmes en un : un point de rupture majeur, et l'invisibilité universelle de l'annuaire |

⚠️ **L'anomalie 1 est la plus discrète, et ses conséquences sont les plus larges.** Un relais de messagerie devenu inutile après une migration reste exposé sur Internet, n'est plus surveillé par personne, et **continue d'être corrigé au mieux par habitude**. C'est le cas d'école du décommissionnement inachevé, traité dans le volume Asset Management.

#### A.5 Corrigé — les trois questions

**À qui, et lesquelles** — trois questions seulement, et le choix des destinataires compte autant que celui des questions.

| # | Question | À qui | Pourquoi celle-ci |
|---|---|---|---|
| **1** | *« `MAIL-RELAY` est-il encore utilisé, et est-il encore joignable depuis Internet ? »* | Exploitation | **Un composant exposé sans usage est le meilleur rapport risque/effort du dossier** |
| **2** | *« Comment administre-t-on ces machines, et depuis quel poste ? »* | Exploitation | §27 — le chemin le plus court vers la compromission totale n'est pas dessiné |
| **3** | *« Depuis la migration de 2024, les identités de la messagerie viennent-elles de `DC-01` ? »* | DSI ou responsable messagerie | §40.2 — la synchronisation d'identités est un point de fragilité récurrent d'une architecture hybride |

**Ce qu'on ne demande pas le premier jour**, et pourquoi :

| Question écartée | Motif |
|---|---|
| *« Pourquoi n'y a-t-il qu'un seul serveur applicatif ? »* | Elle sonne comme un reproche. Elle viendra, après avoir compris l'histoire — §4.4 |
| *« Pourquoi le schéma n'est-il pas à jour ? »* | Sans objet : aucun schéma ne l'est. §50.4 |
| *« Où est la documentation ? »* | Elle n'existe probablement pas, et la demander ne produit rien |

⚠️ **Avertissement sur les barèmes de ces trois cas**

Les barèmes qui suivent notent **des comportements, pas des réponses**. Ils récompensent le fait de poser la bonne question, de dater un schéma, de relever une absence — jamais le fait d'écrire exactement la même phrase que le corrigé.

**Conformément au §48.0** : sur les cas de conception, **plusieurs architectures sont défendables**. Une proposition qui diffère du corrigé et qui énonce clairement la contrainte privilégiée et la contrainte dégradée **obtient le plein barème**.

**Et conformément au principe d'hypothèse** : une identification de composant formulée avec certitude perd des points, même si elle est juste. **Ce qu'on note est la démarche, pas la chance.**

#### A.6 Le barème

| Critère | Pts |
|---|---|
| Relever `MAIL-RELAY` comme zombie exposé | **20** |
| Relever l'absence de chemin d'administration | **20** |
| Dater le schéma et identifier les deux événements postérieurs | 15 |
| Identifier `DC-01` comme rupture, malgré l'absence de trait | 15 |
| Distinguer l'écart 8/214 comme choix de vue, pas comme erreur | 10 |
| Poser la question de la migration de messagerie | 10 |
| Formuler trois questions et pas dix | 10 |

**Élimination** : commencer par critiquer l'architecture avant d'avoir demandé son histoire — §4.4.

---

### Cas B — Le service qui tombe

> **Durée** 1 h 30 · **Livrable** : liste ordonnée des causes possibles, et vérifications
> **Prérequis** : chapitres 29 à 35, 43

#### B.1 La situation

**Mardi 10 h 15.** Le service « Portail clients » est inaccessible depuis l'extérieur. Vous n'avez que le schéma 1.1 et quinze minutes avant le point de crise.

**Les faits rapportés** :

```
· Les clients externes obtiennent une erreur de connexion.
· Les salariés internes accèdent normalement au portail.
· La supervision est au vert sur les trois serveurs web,
  sur l'applicatif et sur la base.
· L'incident a commencé « vers 9 h 40 ».
· Aucune intervention n'était planifiée.
```

#### B.2 Les questions

1. Que vous dit le fait que l'interne fonctionne et l'externe non ?
2. Listez les causes possibles, **par ordre de probabilité**.
3. Quelles vérifications, dans quel ordre, et en combien de temps ?
4. Que dit la supervision au vert, et que ne dit-elle pas ?

#### B.3 Corrigé — ce que la dissymétrie révèle

**L'information la plus précieuse du dossier est que l'interne fonctionne.**

Elle élimine d'emblée tout ce qui est commun aux deux chemins :

| Éliminé | Pourquoi |
|---|---|
| Serveurs web | L'interne les atteint |
| Applicatif, base | Idem |
| Annuaire | L'authentification interne fonctionne |
| Segment serveurs | Joignable |

**Ce qui reste : ce qui est propre au chemin externe** — §29.3.

```
   CHEMIN EXTERNE          Internet → FW → mandataire → répartiteur → web
   CHEMIN INTERNE          poste → répartiteur → web
                                    ▲
                          la divergence est ici
```

#### B.4 Corrigé — les causes, par ordre de probabilité

| # | Cause | Probabilité | Pourquoi ce rang |
|---|---|---|---|
| **1** | **Certificat expiré** sur le mandataire | **Élevée** | Cause fréquente, effet exactement conforme aux symptômes, **survient sans intervention** — §17 |
| **2** | **Résolution de noms externe** défaillante | **Élevée** | Un enregistrement public **modifié, supprimé, ou dont les serveurs faisant autorité ne répondent plus**. L'interne utilise une vue différente — §14 |
| **3** | Mandataire inverse en panne ou saturé | Moyenne | Sa panne n'affecte que l'externe — §12 |
| **4** | Règle de pare-feu modifiée | Moyenne | « Aucune intervention planifiée » n'exclut pas une intervention non planifiée |
| **5** | Lien Internet dégradé | Faible | Affecterait aussi la sortie des postes |
| **6** | Attaque en déni de service | Faible | Possible, à ne pas privilégier faute d'élément |

⚠️ **Les deux premières partagent une propriété qui explique leur rang** : elles **peuvent survenir sans que personne n'ait rien fait de visible ce jour-là**.

📌 **Une précision, parce que le mot « expiration » recouvre trois choses différentes en résolution de noms** :

| Ce qui expire | Effet |
|---|---|
| **La durée de vie d'une réponse en cache** | Le client redemande. **Si les serveurs faisant autorité répondent, rien ne change** |
| **L'enregistrement du nom de domaine lui-même** | Le nom cesse d'être délégué — le service devient injoignable de l'extérieur |
| **Un certificat** | Le client refuse la connexion, à l'heure inscrite dans le certificat |

⚠️ **Seules les deux dernières arrêtent un service.** La première est un mécanisme normal — elle ne devient un problème que si la réponse obtenue au renouvellement a changé, ou si les serveurs faisant autorité ne répondent plus.

#### B.5 Corrigé — les vérifications, dans l'ordre

| Ordre | Vérification | Durée | Pourquoi ce rang |
|---|---|---|---|
| **1** | **Ouvrir le service depuis l'extérieur et lire l'erreur exacte** | 2 min | Une erreur de certificat, de nom ou de connexion **désigne directement une des trois premières causes** |
| **2** | Vérifier la date d'expiration du certificat du mandataire | 3 min | Coût nul, cause n° 1 |
| **3** | Résoudre le nom public depuis l'extérieur | 3 min | Cause n° 2 |
| **4** | État du mandataire : processus, charge, journaux depuis 9 h 30 | 5 min | Cause n° 3 |
| **5** | Journal du pare-feu : changement de configuration récent | 5 min | Cause n° 4 |

**Total : moins de vingt minutes**, et les trois premières vérifications couvrent les deux causes les plus probables pour huit minutes de travail.

⚠️ **L'erreur classique** : commencer par les serveurs web, parce qu'ils sont au centre du schéma et qu'on sait les vérifier. **Ils sont déjà éliminés par le fait que l'interne fonctionne.**

#### B.6 Corrigé — ce que la supervision au vert dit et ne dit pas

| Elle dit | Elle ne dit pas |
|---|---|
| Les processus tournent | Que le service est rendu |
| Les machines répondent | Que le certificat est valide |
| La base accepte des connexions | Que le chemin externe fonctionne |
| Les indicateurs surveillés sont normaux | **Ce qui n'est pas surveillé** |

> **Une supervision au vert pendant un incident signifie que l'incident se produit là où l'on ne regarde pas.** C'est une information, pas une contradiction.

**Ce que l'incident révèle sur la supervision**, et qui est le vrai livrable du cas : **rien ne surveille l'expiration des certificats, ni la résolution du nom depuis l'extérieur.** Ce sont deux flux de dépendance — principe des trois flux — et ils ne sont ni dessinés, ni supervisés.

#### B.7 Le barème

| Critère | Pts |
|---|---|
| Exploiter la dissymétrie interne/externe pour éliminer | **25** |
| Placer certificat et résolution en tête | **20** |
| Commencer par lire l'erreur exacte | 15 |
| Vérifications ordonnées par coût croissant | 15 |
| Expliquer ce que la supervision au vert signifie | 15 |
| Conclure sur ce qui n'est pas supervisé | 10 |

**Élimination** : commencer par redémarrer un serveur web.

---

### Cas C — Concevoir sous contrainte réelle

> **Durée** 2 h 30 · **Livrables** : architecture · registre des compromis · liste de ce qui reste à vérifier
> **Prérequis** : Partie IX

#### C.1 La situation

**L'organisation** : 450 personnes, deux sites, fabricant de composants électroniques.

**Le besoin** : publier un portail permettant à 80 clients de suivre l'avancement de leurs commandes et de télécharger des documents techniques.

**Les contraintes**, telles qu'elles vous sont données — et deux ne sont pas chiffrées :

```
DISPONIBILITÉ   « Il faut que ce soit fiable »
PERFORMANCE     Non exprimée
COÛT            60 k€ d'investissement · 1,5 personne à l'exploitation, en tout
SÉCURITÉ        Documents techniques = propriété industrielle. Sensible.
CONFORMITÉ      Données de contact clients
HISTOIRE        L'ERP existant contient les données de commande.
                Version 2019, éditeur actif, interface applicative disponible.
                Aucune zone démilitarisée aujourd'hui. Rien n'est publié.
```

#### C.2 Les questions

1. Que faites-vous des deux contraintes non chiffrées ?
2. Produisez deux options, avec leurs compromis.
3. Retenez-en une, et écrivez le registre.
4. Que reste-t-il à vérifier avant de s'engager ?

#### C.3 Corrigé — les contraintes non chiffrées

**C'est la première tâche, et la plus déterminante** — §46.3.

| Contrainte | Ce qu'on demande | Pourquoi |
|---|---|---|
| **Disponibilité** | *« Si le portail est indisponible une demi-journée en semaine, que se passe-t-il ? »* | *« Fiable »* ne se conçoit pas. **Une réponse chiffrée détermine la moitié de l'architecture** |
| **Performance** | *« Combien de clients simultanés, et quelle taille de documents ? »* | 80 clients qui consultent occasionnellement et 80 qui téléchargent des fichiers lourds ne produisent pas la même architecture |

**Réponses obtenues** *(à supposer pour la suite)* : une demi-journée est tolérable · consultations occasionnelles, documents jusqu'à 50 Mo.

⚠️ **Ce que cette réponse change immédiatement** : une interruption d'une demi-journée tolérable **élimine la nécessité d'une redondance complète**, et libère l'essentiel du budget pour la sécurité — qui est la contrainte réellement forte ici.

#### C.4 Corrigé — les deux options

| | **Option A — publication directe** | **Option B — zone démilitarisée avec mandataire** |
|---|---|---|
| Composants nouveaux | 1 serveur portail | Mandataire inverse · serveur portail · segment DMZ · règles |
| Accès à l'ERP | Le portail interroge l'ERP directement | **Le portail interroge une copie**, alimentée depuis l'ERP |
| Exposition de l'ERP | **L'ERP est atteignable depuis un serveur exposé** | L'ERP n'est jamais atteignable depuis l'extérieur |
| Investissement | ≈ 20 k€ | ≈ 45 k€ |
| Exploitation | 0,2 personne | **0,6 personne** |
| Une faille du portail | Donne accès à l'ERP de 2019, non supporté | Donne accès à une copie de données |

**Retenu : l'option B**, et le raisonnement tient en une ligne :

> **La contrainte forte de ce dossier n'est pas la disponibilité, c'est la propriété industrielle.** L'option A place un serveur exposé en communication directe avec un progiciel de 2019 — c'est-à-dire le composant le moins maintenable de l'organisation.

⚠️ **Le point de conception le plus important est la copie de données.** Le portail ne lit pas l'ERP : il lit une base alimentée par un export périodique. Cela dégrade la fraîcheur — les données ont jusqu'à une heure de retard — et **supprime tout chemin depuis l'extérieur vers l'ERP**. C'est un compromis, et il doit être écrit.

#### C.5 Corrigé — le registre des compromis

| # | Compromis | Privilégié | Dégradé | Conséquence acceptée | Revoir si |
|---|---|---|---|---|---|
| **1** | Aucune redondance du portail | Coût, exploitation | Disponibilité | Interruption jusqu'à une demi-journée | La tolérance métier change · le nombre de clients croît |
| **2** | **Copie de données au lieu d'accès direct à l'ERP** | **Sécurité** | Fraîcheur | Données à jour à une heure près | Un besoin de temps réel apparaît |
| **3** | Mandataire inverse unique | Coût | Disponibilité externe | Le portail devient injoignable si le mandataire tombe | La disponibilité devient critique |
| **4** | Authentification par comptes locaux au portail | Simplicité, indépendance | Gouvernance des identités | 80 comptes à gérer séparément | Le nombre de clients dépasse ~200 |
| **5** | Pas de détection sur le serveur portail | Coût | Observabilité | On dépend des journaux du mandataire | Le budget le permet l'an prochain |

**Ce que le registre rend possible dans dix ans** : quelqu'un qui découvrira ce portail comprendra **pourquoi il lit une copie** au lieu de l'ERP — et ne conclura pas à une incohérence. C'est le chapitre 4, par anticipation.

#### C.6 Corrigé — ce qui reste à vérifier

**La section qui distingue une proposition d'un engagement** — §7.3.

| # | À vérifier | Pourquoi | Qui |
|---|---|---|---|
| 1 | **L'interface de l'ERP 2019 permet-elle l'export nécessaire ?** | Toute l'option B en dépend | Éditeur |
| 2 | Quelle est la charge réelle des téléchargements de 50 Mo ? | Dimensionne le lien Internet | Métier + réseau |
| 3 | Le lien Internet actuel supporte-t-il un usage entrant ? | Aujourd'hui il ne sert qu'à sortir | Réseau |
| 4 | **Qui exploitera le mandataire ?** | 0,6 personne sur 1,5 disponible : est-ce tenable ? | DSI |
| 5 | Les documents techniques sont-ils tous partageables ? | Certains peuvent être sous accord de confidentialité | Juridique, R&D |
| 6 | Le basculement en cas de panne du portail a-t-il un mode dégradé ? | Envoi manuel par courriel ? | Métier |

⚠️ **La question 4 est celle qui peut faire échouer le projet**, et c'est le §47.3 : une architecture qui consomme 0,6 exploitant sur 1,5 disponible laisse 0,9 pour tout le reste du système d'information. **Si la réponse est non, l'option A revient sur la table — avec ses compromis, écrits.**

#### C.7 Le barème

| Critère | Pts |
|---|---|
| Chiffrer les deux contraintes manquantes **avant** de concevoir | **25** |
| Identifier que la contrainte forte est la propriété industrielle, pas la disponibilité | **20** |
| Proposer la copie de données plutôt que l'accès direct à l'ERP | **20** |
| Registre des compromis complet, avec conditions de réexamen | 15 |
| Liste de ce qui reste à vérifier, dont la capacité d'exploitation | 15 |
| Ne pas surconcevoir | 5 |

**Élimination** : proposer une architecture redondée sans avoir chiffré la disponibilité tolérable.

📌 **Une autre architecture que l'option B est recevable** si elle est justifiée par un arbitrage écrit. Ce qui n'est pas recevable, c'est d'arbitrer sans avoir demandé les deux contraintes manquantes — §46.3.

---


## ANNEXES

### Plan d'accès

| J'ai besoin de… | Annexe |
|---|---|
| Comprendre un terme | **A** — glossaire |
| Retrouver un composant et son rôle | **B** — fiches composants |
| Lire une architecture méthodiquement | **C** — la grille en sept passes |
| Comprendre une convention de dessin | **D** — conventions |
| Retrouver un schéma du cours | **E** — catalogue |
| Voir une architecture type commentée | **F** — dix architectures |
| Vérifier que je ne tombe pas dans un piège | **G** — pièges de lecture |
| Savoir ce qui n'est jamais dessiné | **H** — liste de contrôle |
| Placer un dispositif | **I** — les cinq actions |
| Concevoir et écrire mes compromis | **J** — grille de conception |
| Relier ce cours aux autres volumes | **K** — raccordement |
| Une liste à cocher | **L** — checklists |

---


## Annexe A — Glossaire

**Actif éphémère** — Composant dont la durée de vie est inférieure au cycle d'observation. §41
**Adresse** — Identifiant d'une machine sur le réseau. **Elle change, elle est réattribuée, et derrière une traduction elle n'identifie pas l'origine.** §P.2, §P.4
**Active Directory** — Implémentation de référence d'un service d'annuaire en entreprise. **Ce cours l'utilise pour rendre le concept concret ; ses propriétés ne sont pas celles de tous les services d'identité.** §16
**Double pile** — Coexistence des deux familles d'adressage sur une même machine. **Deux chemins possibles, deux jeux de règles.** §P.5
**Annuaire** — Composant détenant identités, groupes et règles. Répond à *qui es-tu* et *à quoi as-tu droit*. §16
**Arbitrage** — Choix entre deux contraintes contradictoires. **Toute architecture en est faite.** §1.4
**Bordure** — Zone de contact avec l'extérieur : pare-feu, accès distant. §5.2
**Chemin d'administration** — Voie par laquelle on pilote un système. **Plus puissante que ce qu'elle administre.** §27
**Compromis** — Arbitrage assumé et **écrit**. S'il n'est pas écrit, il est subi. §46.5
**Contrainte** — L'une des six forces qui produisent une architecture : disponibilité, performance, coût, sécurité, conformité, **histoire**. §1.4
**Dégradation** — État où le service fonctionne partiellement. À distinguer de l'arrêt et de la cécité. §35.4
**Flux de dépendance** — Ce sans quoi un service **ne peut pas s'établir**. Rarement dessiné. principe des trois flux
**Flux d'exploitation** — Ce qui permet de tenir, observer, restaurer. Sa rupture **rend aveugle sans arrêter**. principe des trois flux
**Flux métier** — Ce que le service transporte ou traite. Le seul généralement dessiné. principe des trois flux
**Frontière** — Ce qu'il faut traverser pour passer d'une zone à une autre. **Une frontière déclarative n'en est pas une.** §5.3
**Kerberos** — Protocole d'authentification employé dans un domaine Active Directory. **À ne pas confondre avec LDAP, qui interroge l'annuaire sans assurer l'authentification.** §16
**Mandataire inverse** — Reçoit de l'extérieur à la place des serveurs internes. **Voit le contenu si le chiffrement y est terminé — modes B et C du §12.**
**Masque de sous-réseau** — Ce qui définit jusqu'où s'étend « à côté ». §P.2
**Passerelle par défaut** — Où une machine envoie ce qui n'est pas dans son sous-réseau. **Sans elle, elle ne sort pas de son segment.** §P.2
**Mandataire sortant** — Concentre les accès internes vers l'extérieur. Fonction opposée du précédent. §11
**Point de rupture** — Ce qui, en tombant, arrête un service. **La notion la plus utile du cours.** §2.2
**Répartiteur de charge** — Distribue entre plusieurs exemplaires. **Crée un point de rupture en en résolvant un.** §13
**Résolution de noms** — Traduit un nom en adresse. **Sa panne est la plus déroutante d'un système d'information.** §14
**Réplication** — Copie continue vers un autre stockage. **Protège de la panne, pas de la suppression : celle-ci est répliquée aussi.** §23.4
**Sauvegarde** — Copie **indépendante**, sur un autre support. **La seule des trois qui protège de tout — si elle a été testée.** §23.4
**Instantané** — État figé à un instant, **sur le même stockage**. Protège d'une erreur récente, pas de la perte du stockage. §23.4
**Stockage bloc / fichier / objet** — Trois façons d'exposer du stockage : un disque · un dossier partagé · une adresse à appeler. §23.4
**RPO** — Objectif de perte de données, exprimé en temps. *Combien de minutes de données accepte-t-on de perdre ?* §46.3
**RTO** — Objectif de délai de reprise. *Sous combien de temps vise-t-on la restauration ?* **À ne pas confondre avec la tolérance métier maximale, qui est une contrainte, ni avec le délai réel, qui se mesure.** §46.3
**Courtier de messages** — Composant qui porte des messages entre un producteur et un consommateur. **Découple leur disponibilité, et devient le point dont tout dépend.** §42.4
**File d'échecs** — Où finissent les messages qu'un consommateur n'arrive jamais à traiter. **Personne ne la regarde.** §42.4
**Idempotence** — Propriété d'une opération qu'on peut rejouer sans changer le résultat. **Indispensable dès qu'un message peut être livré deux fois.** §42.4
**Overlay / underlay** — Réseau logique construit au-dessus d'un réseau physique IP. **Le schéma logique et le schéma physique divergent alors radicalement.** §24.3
**Passerelle d'interconnexion** — **L'ensemble des composants et fonctions** par lesquels deux zones de confiance distinctes sont autorisées à échanger. Ce n'est pas un équipement. §25.5
**Quorum** — Mécanisme par lequel un ensemble distribué décide **quelle partie a le droit de continuer** quand ses membres ne communiquent plus. §23.5
**Split-brain** — Situation où deux parties d'un même système, séparées, continuent chacune de leur côté avec des vérités divergentes. §23.5
**Sens d'établissement** — Qui a initié une connexion. **L'information la plus déterminante d'un flux, et la plus souvent absente des schémas.** §P.3
**Sédimentation** — Empilement de décisions prises à des époques différentes. **L'état normal de tout système en service.** Ch. 4
**Segment** — Ensemble de machines qui se joignent directement, sans traverser d'équipement de routage. **Les y placer ne crée pas entre elles la frontière de filtrage inter-segments visible sur le schéma ; leur isolation éventuelle est à chercher ailleurs.** §24.1
**Service** — Ce qui produit une valeur pour l'organisation. Ne correspond à aucun composant. §35.1
**Strate** — Couche historique d'une architecture, reconnaissable à ses conventions et ses technologies. §4.2
**Terminaison du chiffrement** — Point où un flux chiffré est ouvert. **Détermine qui voit le contenu en clair.** Trois modes, §12
**Traduction d'adresses** — Mécanisme qui remplace une adresse au passage. **L'adresse observée n'est alors pas celle de l'origine.** §P.4
**Vue** — Représentation partielle d'un système : physique, logique, flux, service. **Aucune ne ment.** §3.3
**Zone** — Regroupement de segments partageant un niveau de confiance. Six de référence. §5.2
**Zone démilitarisée** — Ce qui doit être joignable de l'extérieur, **en supposant que ce sera compromis**. Définie par sa **seconde** frontière. §25

---


## Annexe B — Fiches composants

*Format uniforme : rôle · s'il disparaît · effet sur la donnée · reconnaissance · contrainte et coût.*

| Composant | S'il disparaît | Délai | Compréhensible ? |
|---|---|---|---|
| **Commutateur** | Un segment entier | Immédiat | ✅ |
| **Routeur** | Les échanges entre segments | Immédiat | ⚠️ |
| **Pare-feu** | Tout ce qui traverse · **ou rien, s'il est contourné** | Immédiat | ⚠️ |
| **Mandataire sortant** | L'accès Internet des postes | Immédiat | ❌ |
| **Mandataire inverse** | Les accès externes seuls | Immédiat | ❌ |
| **Répartiteur** | **Tout le service**, malgré des serveurs sains | Immédiat | ❌ |
| **Résolution de noms** | Presque tout | **Différé — caches** | ❌ |
| **Attribution d'adresses** | Les machines une par une | **Différé, jours** | ❌ |
| **Annuaire** | Les authentifications, puis tout | Progressif | ⚠️ |
| **Infrastructure de clés** | Un service à chaque expiration | **Différé, mois** | ❌ |
| **Serveur web** | Rien si redondé | Immédiat | ✅ |
| **Applicatif** | Le service · le site s'affiche, rien ne marche | Immédiat | ⚠️ |
| **Base de données** | Tout ce qui en dépend · **perte possiblement définitive** | Immédiat | ⚠️ |
| **Serveur de fichiers** | Le travail, pas toujours le service | Immédiat | ✅ |
| **Messagerie** | Les courriels · **et la réinitialisation des mots de passe** | Immédiat puis différé | ⚠️ |
| **Hôte de virtualisation** | Ses machines | Immédiat | ⚠️ |
| **Stockage partagé** | **Toute la plateforme** | Immédiat | ⚠️ |
| **Stockage objet** | Ce qui l'appelle | Immédiat | ⚠️ — **joignable par clé, pas par le réseau** |
| **Plan de gestion** | Rien · **on ne peut plus rien administrer** | Immédiat | ❌ |

⚠️ **Les six lignes marquées ❌ sont les six composants dont la panne est incompréhensible.** Cinq d'entre eux ne sont jamais dessinés.

---


## Annexe B bis — Index des notions à reconnaître

> **Les vingt-deux technologies que vous rencontrerez sans avoir à les maîtriser.** Chacune est traitée là où elle devient naturelle, jamais en catalogue.

| Notion | Ce qu'il faut en retenir en une ligne | Où |
|---|---|---|
| **BGP** | Les politiques comptent autant que la distance · le chemin dépend de ce que d'autres annoncent | §9.2 |
| **MPLS** | Un réseau privé d'opérateur **n'est pas un chiffrement** | §26.3 |
| **SD-WAN** | Pas un nouveau câble : une couche de pilotage · **le chemin devient dynamique** | §26.3 |
| **VXLAN / EVPN** | Réseau logique au-dessus du physique · **étendre un segment étend la propagation** | §24.3 |
| **WAF** | Le seul des trois qui juge **le contenu** d'une requête web | §12.3 |
| **CDN** | Le chiffrement est terminé chez un tiers · **une page personnalisée en cache est servie à un autre** | §12.3 |
| **Passerelle d'interfaces** | Une façade **avec une politique**, pas un mandataire moderne | §42.3 |
| **Maillage de services** | Tous les environnements de microservices n'en ont pas besoin | §41.4 |
| **HSM** | La clé peut être **utilisée sans être exportée** | §17.3 |
| **PAM** | Transforme un état permanent en **événement daté et motivé** · attention au compte de secours | §27.3 |
| **NAC** | Place le terminal **dans un segment selon ce qu'il est** · que fait-on s'il tombe ? | §24.4 |
| **SASE / SSE / CASB** | Des familles de capacités, **pas des implémentations identiques** | §39.4 |
| **VDI** | *Où s'exécute réellement l'application ?* · une panne réseau **arrête** le travail | §23.3 |
| **Hyperconvergence** | La simplification physique **déplace la complexité dans le logiciel** | §23.3 |
| **Réseau de stockage dédié** | Une infrastructure entière absente de tous les schémas logiques | §23.5 |
| **Immutabilité** | Protège une copie existante · **n'empêche pas de cesser d'en créer** | §23.5 |
| **Quorum** | Un membre sain peut devoir **s'arrêter faute de majorité** · deux nœuds ne suffisent pas | §23.5 |
| **Consensus distribué** | La forte cohérence se paie en disponibilité ou en performance | §42.3 |
| **Mainframe** | **Ancien ne veut dire ni inutile, ni non critique** | §4.2 |
| **Calcul intensif** | Une zone aux priorités inversées, comme l'industriel | §5.4 |

⚠️ **Le contrat, rappelé** : ces vingt-deux notions relèvent du niveau 🔭. **On attend de vous que vous sachiez ce qu'elles impliquent, et quelle question poser — pas que vous sachiez les configurer.**

---


## Annexe C — La grille en sept passes

```
①  ZONES        Combien ? Qu'est-ce qui matérialise chaque frontière ?
                Y a-t-il une seconde frontière après la DMZ ?
                Un composant est-il à cheval ?

②  ENTRÉE       Utilisateur externe : par où ?
                Utilisateur interne : par où ? (souvent plus court)
                Administrateur : par où ? (jamais dessiné)

③  DONNÉES      Où sont-elles ? En combien d'endroits existent-elles ?
                Réplicas · sauvegardes · recette · exports · rapports

④  IDENTITÉ     Contre quoi s'authentifie-t-on ?
                Combien de fois sur un parcours ?
                Que se passe-t-il si ce composant tombe ?

⑤  FLUX         Quel chemin suit une requête, en douze étapes ?
                Quelle famille pour chaque flux ?

⑥  RUPTURES     Quels composants sont uniques ?
                Les exemplaires sont-ils sur des hôtes différents ?
                Le basculement a-t-il été testé ?
                Où sont les sessions ?

⑦  INVISIBLE    Les onze éléments de l'annexe H
```

**Rendu attendu** : une page, se terminant par **trois questions, pas un jugement**.
**Durée réelle** : 1 h pour une architecture simple, une demi-journée pour un système réel.

---


## Annexe D — Conventions de schéma

| Convention | Signification habituelle | Fiabilité |
|---|---|---|
| Position haute | Extérieur, Internet | Élevée |
| Position basse | Données | Élevée |
| Nuage | Ce qu'on ne maîtrise ou ne détaille pas | Élevée |
| Boîtes empilées | Plusieurs exemplaires | Moyenne |
| Trait pointillé | Flux logique, relation, lien non permanent | **Faible** |
| Double ligne | Redondance ou haut débit | **Faible** |
| Composant à cheval | Traverse une frontière — **toujours à interroger** | Élevée |

⚠️ **Aucune convention n'est normalisée.** Première question devant un schéma inconnu : *y a-t-il une légende ?*

**Ce qu'une boîte peut représenter** : machine · rôle · groupe · service · fournisseur externe. §3.1
**Ce qu'un trait peut représenter** : câble · flux · relation logique · adjacence · **rien de précis**. §3.2

---


## Annexe E — Catalogue des schémas

| # | Schéma | Chapitre |
|---|---|---|
| 1.1 | HELIOMED, vue d'ensemble | §1.1 |
| 1.2 | Les quatre questions du lecteur | §1.3 |
| 1.3 | Trois arbitrages, trois architectures | §1.4 |
| 3.1 | Le même système, quatre vues | §3.3 |
| 4.1 | Les strates d'un système d'information | §4.2 |
| 5.1 | Les six zones | §5.2 |
| 6.1 | Ce qu'un poste atteint | §6.2 |
| 6.2 | Les deux chemins d'un poste nomade | §6.3 |
| 10.1 | Ce que le suivi d'état change | §10.2 |
| P.1 | La décision que prend toute machine | §P.2 |
| P.2 | Les deux traductions d'adresses | §P.4 |
| 12.1 | Ce que le mandataire inverse change | §12 |
| 12.2 | Les trois modes de terminaison du chiffrement | §12 |
| 14.1 | La place réelle de la résolution de noms | §14 |
| 20.1 | Pourquoi la base est au fond | §20 |
| 23.1 | La redondance qui n'en est pas | §23.3 |
| 23.2 | Bloc, fichier, objet · quatre architectures de stockage | §23.4 |
| 25.1 | Les deux frontières d'une DMZ | §25.1 |
| 27.1 | Le chemin d'administration | §27.2 |
| 28.1 | Les trois modèles de frontière industrielle | §28.3 |
| 29.1 | Une requête, de bout en bout | §29.1 |
| 29.2 | Quatre chemins vers le même service | §29.3 |
| 30.1 | La cascade d'une panne d'annuaire | §30.2 |
| 31.1 | Où vit la session | §31.2 |
| 32.1 | Une donnée, de la saisie à l'oubli | §32.1 |
| 35.1 | L'arbre de dépendance d'un service | §35.2 |
| 35.2 | Dix flux superposés sur un même service | §35.3 |
| 36.1 | Les sept passes | §36.1 |
| 38.1 | Les trois façons de dessiner un tiers | §38.2 |
| 39.1 | Où passe la frontière de responsabilité | §39.2 |
| 40.1 | Les trois liens d'une architecture hybride | §40.2 |
| 41.1 | Deux façons de dessiner un cluster | §41.2 |
| 43.1 | Les cinq actions | §43.1 |
| 46.1 | Lire et concevoir | §46.1 |

---


## Annexe F — Les dix architectures

| # | Architecture | Ce qu'elle enseigne | Où |
|---|---|---|---|
| 1 | Application interne, trois composants | Une architecture proportionnée · l'authentification non représentée | §37.1 |
| 2 | Site web public | Qui voit le contenu en clair · la frontière 2 | §37.2 |
| 3 | Trois niveaux, redondance partielle | **La rupture de symétrie est une information** | §37.3 |
| 4 | Système hérité mal documenté | Trois signes convergents d'une strate ancienne | §37.4 |
| 5 | Haute disponibilité complète | Le coût de la symétrie · ce qu'elle ne couvre pas | Cas B |
| 6 | Multi-sites | L'autonomie locale et ses trois dépendances | §26.2 |
| 7 | Hybride | Le lien d'identités, point de fragilité récurrent | §40 |
| 8 | Industrielle | L'inversion des priorités | §28 |
| 9 | **Réelle et désordonnée** | Vingt ans de sédimentation | Cas A |
| 10 | HELIOMED complet | La synthèse du fil rouge | §1.1 + ajouts §50.6 |

---


## Annexe G — Pièges de lecture

| # | Piège | Détection |
|---|---|---|
| 1 | Lire un **rôle** comme une machine | *Combien y en a-t-il réellement ?* |
| 2 | Croire qu'un **trait** signifie une autorisation | *Est-ce permis, ou seulement possible ?* |
| 3 | Confondre **mandataire sortant et inverse** | *Pour entrer, ou pour sortir ?* |
| 4 | Prendre une **frontière déclarative** pour une frontière | *Qu'est-ce qui empêche de passer ?* |
| 5 | Oublier la **seconde frontière** d'une DMZ | Elle n'est presque jamais dessinée |
| 6 | Croire une **redondance** dessinée | *Sur des hôtes différents ? Le basculement est-il testé ?* |
| 7 | Oublier que la **session** peut annuler la redondance | *Où vit la session ?* |
| 8 | Ne pas voir les composants **reliés à rien** | Annuaire, résolution : tout s'y connecte |
| 9 | Chercher une panne parmi les **composants dessinés** | Sept étapes sur douze sont invisibles |
| 10 | Juger une anomalie sans demander sa **date** | Chaque anomalie a une histoire |
| 11 | Déduire une architecture de la **taille** | *Principe de la contrainte* |
| 12 | Oublier le **poste utilisateur** | La majorité des flux et des incidents |
| 13 | Oublier le **prestataire** | Dessiné en nuage, présent au cœur de l'administration |
| 14 | Croire qu'un **service en ligne** se sécurise comme le reste | Les cinq actions ne s'appliquent pas à son infrastructure — elles se déplacent — §42.5 |
| 15 | Lire un **cluster** par ses instances | Quatre éléments : entrée, services, état, plan de contrôle |
| 16 | Placer un dispositif au **périmètre** en croyant tout couvrir | Il ne voit pas l'interne |
| 17 | Proposer **dix améliorations** | Une seule sera peut-être faite |
| 18 | Croire un schéma **à jour** | Datez-le |
| 19 | Prendre une **identification** pour une certitude | *Principe d'hypothèse* — port et position font un faisceau, pas une preuve |
| 20 | Conclure à une **redondance** parce qu'elle est dessinée | *Principe de preuve* — hôte, stockage, site, alimentation partagés ? |
| 21 | Croire qu'un mandataire inverse **voit toujours le contenu** | Trois modes de terminaison — §12 |
| 22 | Confondre **LDAP et authentification** | LDAP interroge · d'autres mécanismes authentifient — §16 |
| 23 | Croire qu'un **certificat chiffre** | Il lie une identité à une clé ; le protocole chiffre — §17 |
| 24 | Prendre une **adresse dans un journal** pour l'origine | Traduction d'adresses, mandataires — §P.4, §34.1 |
| 25 | Supposer que le modèle **IPv4 + traduction** est universel | §P.5 |
| 26 | Croire que **la base est la donnée** | Elle en porte une partie — §20, §32.2 |
| 27 | Croire qu'un **jeton autoporté ne peut pas être révoqué** | C'est un compromis de coût et de délai — §31.2 |
| 28 | Confondre **réplication et sauvegarde** | La réplication copie aussi les suppressions — §23.4 |
| 29 | Confondre **instantané et sauvegarde** | L'instantané vit sur le même stockage — §23.4 |
| 30 | Oublier le **stockage objet** parce qu'il n'a pas de lien réseau | Il est joignable par clé, depuis n'importe où — §23.4 |
| 31 | Croire que sur un service en ligne **on ne peut rien faire** | Les actions se déplacent vers la configuration et les identités — §42.6 |
| 32 | Croire que deux **réseaux sans fil annoncés** sont deux segments | Annoncé ≠ segmenté — §24.4 |
| 33 | Oublier que le **sans-fil contourne le périmètre physique** | Mode A : la clé donne l'accès interne — §24.4 |
| 34 | Croire qu'une **file asynchrone** protège de tout | Elle déplace la panne : accumulation silencieuse — §42.4 |
| 35 | Ne pas rendre un **consommateur idempotent** | Au moins une livraison ≠ exactement une — §42.4 |
| 36 | Confondre **tolérance métier, RTO visé et délai réel** | Trois choses différentes — §46.3 |
| 37 | Transposer un **ratio d'exploitation** d'un corrigé | Ce sont des données de scénario — §48.0 |

---


## Annexe H — Ce qui n'est jamais dessiné

**Liste de contrôle. À passer sur tout schéma, systématiquement.**

☐ **Résolution de noms** — sa panne arrête presque tout, de façon différée
☐ **Annuaire** — dessiné parfois, relié jamais
☐ **Synchronisation d'horloge** — sa dérive produit des rejets d'authentification
☐ **Chemins d'administration** — le chemin le plus court vers la compromission totale
☐ **Postes de travail** — la majorité des flux et des incidents
☐ **Postes de prestataires** — hors inventaire, avec des droits d'administration
☐ **Sauvegardes et leur chemin** — le serveur est parfois dessiné, jamais son chemin
☐ **Services en ligne** — pas chez vous, donc absents
☐ **Liens partenaires** — anciens, oubliés
☐ **Certificats et leur autorité** — invisibles tant qu'ils fonctionnent
☐ **Environnements de recette** — données de production, protections moindres
☐ **Collecte de journaux** — flux d'exploitation
☐ **Versions** — impossible de raisonner l'obsolescence sans elles
☐ **Le temps** — un schéma est un instantané, sans histoire ni migration en cours

⚠️ **Dessinez-les tous sur votre schéma : la page devient illisible en quatre minutes.** C'est pourquoi ils n'y sont pas — et pourquoi il faut savoir qu'ils existent.

---


## Annexe I — Les cinq actions et leurs emplacements

| Action | Possible | **Impossible** |
|---|---|---|
| **Observer** | Pare-feu · mandataires · commutateurs · postes · serveurs | Flux chiffré non terminé · **chez un tiers** |
| **Filtrer** | Pare-feu · mandataires · entre segments | **Dans un segment** · chez un tiers |
| **Authentifier** | Mandataire inverse · applicatif · annuaire · accès distant | Entre serveurs se faisant confiance par adresse |
| **Segmenter** | Entre zones · entre segments · au poste | **Dans un segment**, sans mesure explicite |
| **Journaliser** | Tout composant traversé | Ce qui ne traverse aucun composant journalisant |

**Les deux points les plus riches** :

| Point | Ce qu'il apporte | Sa limite |
|---|---|---|
| **Mandataire inverse** | Voit tout le trafic externe **en clair** · filtre · authentifie · journalise | **Ne voit que l'externe** |
| **Applicatif** | Le seul qui connaisse **l'utilisateur réel et l'action métier** | Reçoit rarement les moyens |

**Face à un emplacement impossible** : on **déplace**, on **remplace**, ou on **déclare non couvert**. Jamais on ne fait semblant.

⚠️ **Sur un service en ligne** : les cinq actions ne s'appliquent pas à son infrastructure, **et elles se déplacent** vers la configuration, les identités, les données et les journaux exposés — §42.5. **« Impossible » y signifie « pas sur ses couches internes », pas « rien à faire ».**

---


## Annexe J — Grille de conception et registre des compromis

### J.1 Fiche de contraintes

```
SERVICE         .................................
UTILISATEURS    Combien : ......  Où : ......  Quand : ......
DONNÉES         Nature : ......  Sensibilité : ......
DISPONIBILITÉ   Interruption tolérable : ......
                Perte de données tolérable : ......
PERFORMANCE     Temps de réponse : ......  Volume : ......
COÛT            Investissement : ......  Récurrent : ......
                EXPLOITANTS DISPONIBLES : ......   ← la ligne décisive
SÉCURITÉ        Exposition nécessaire : ......
CONFORMITÉ      Obligations : ......  Preuve à produire : ......
HISTOIRE        Existant à intégrer : ......
                Ce qu'on ne peut pas changer : ......
```

⚠️ **La ligne « exploitants disponibles » est celle qui explique le plus d'échecs.** §47.3

### J.2 Registre des compromis

| # | Compromis | Contrainte privilégiée | Contrainte dégradée | Conséquence acceptée | Décideur | **Revoir si** |
|---|---|---|---|---|---|---|

**C'est le vrai livrable d'une conception.** Le schéma montre le résultat ; le registre montre **pourquoi**.

### J.3 Ce qui reste à vérifier

| # | À vérifier | Pourquoi | Qui | Avant quand |
|---|---|---|---|---|

**Une proposition sans cette section est un engagement déguisé.**

### J.4 Grille de critique en six points

```
① POINT FORT          Ce qui est bien pensé, et pourquoi     ← toujours en premier
② POINT FAIBLE        Ce qui est fragile, sous quelle condition
③ POINT DE RUPTURE    Ce qui n'a pas de doublure
④ DÉPENDANCE CACHÉE   Ce dont tout dépend et qui n'est pas dessiné
⑤ RISQUE PRINCIPAL    Scénario le plus probable et le plus coûteux
⑥ AMÉLIORATION        UNE SEULE, avec son coût et son effet
```

**Format en cinq lignes** : ce qui fonctionne · ce que j'ai observé · **ce que je n'ai pas su** · le risque · ce que je propose.

---


## Annexe K — Raccordement aux autres volumes

| Ce que l'architecture détermine | Volume concerné | Chapitre |
|---|---|---|
| **L'interruptibilité** — un composant qui ne peut s'arrêter ne sera pas corrigé | Maintien en condition de sécurité | §45.1 |
| **Les fenêtres de maintenance** | MCS | §45.1 |
| **Ce qui est découvrable** — un actif derrière un filtre est invisible au scanner | Asset Management | §45.2 |
| **Les actifs éphémères** | Asset Management | §41 |
| **Les points de passage** — les seuls endroits où observer | Détection et journalisation | §45.3 |
| **La perte d'identité en chemin** | Détection | §34.1 |
| **La rétention des journaux** | Détection · Réponse à incident | §34.2 |
| **Ce qu'on peut isoler** | Réponse à incident | §45.4 |
| **Si l'on peut encore administrer un système compromis** | Réponse à incident | §45.4 |
| **Les chemins d'administration** | Identités et accès | §27 |
| **La fédération et ses dépendances** | Identités et accès | §30.3 |
| **L'exposition d'un composant** | Industrialiser la remédiation | §45.1 |

**Les huit volumes et leurs limites fondamentales** :

| Volume | Limite |
|---|---|
| **Architecture des SI** | **Toute architecture est un compromis sédimenté** |
| Asset Management | La représentation n'est jamais le système |
| Cyber Threat Intelligence | L'incertitude ne se supprime pas |
| Maintien en condition de sécurité | Le système change avec le temps |
| Détection et journalisation | On ne voit que là où l'on regarde |
| Industrialiser la remédiation | La capacité est finie, le flux ne l'est pas |
| Réponse à incident | On décide sans savoir |
| Identités et accès | Les droits s'accumulent, ils ne se réduisent jamais seuls |

---


## Annexe L — Checklists

### L.1 — Devant un schéma inconnu
☐ Y a-t-il une légende ? · ☐ De quand date-t-il ? · ☐ **Pour qui a-t-il été fait ?** · ☐ Quelle vue est-ce ? · ☐ Que représente une boîte ici ? · ☐ Que représente un trait ?

### L.5 — Avant de conclure à un point de rupture
☐ Est-ce un rôle ou une machine ? · ☐ Combien d'exemplaires réels ? · ☐ Sur des hôtes différents ? · ☐ **Même stockage, même site, même alimentation ?** · ☐ **Le basculement a-t-il été testé, et quand ?** · ☐ Où vivent les sessions ?

### L.2 — Avant de croire à une sauvegarde
☐ Est-ce une réplication, un instantané ou une sauvegarde ? · ☐ **Sur quel stockage vit-elle ?** · ☐ Un compte d'exploitation compromis peut-il la supprimer ? · ☐ **Quand a-t-elle été restaurée pour de vrai ?**

### L.3 — Avant de croire à une séparation sans fil
☐ Combien de réseaux annoncés ? · ☐ **Chacun aboutit-il dans un segment distinct ?** · ☐ Qu'est-ce qui filtre entre eux ? · ☐ Le réseau entreprise aboutit-il dans le segment interne ? · ☐ **Contre quoi authentifie-t-on, et que se passe-t-il si ce service tombe ?**

### L.4 — Avant de croire à un découplage asynchrone
☐ Que se passe-t-il si le consommateur est arrêté ? · ☐ **Qui supervise la taille de la file et l'âge du plus ancien message ?** · ☐ Le consommateur est-il idempotent ? · ☐ **Qui regarde la file d'échecs ?** · ☐ Les messages en attente sont-ils persistés ?

### L.6 — Avant d'affirmer le rôle d'un composant
☐ Sur quel faisceau — port, position, connexions ? · ☐ **Le port peut-il être non standard ?** · ☐ Le composant cumule-t-il deux rôles ? · ☐ **Qu'est-ce qui confirmerait ?** · ☐ Ai-je écrit « probablement » plutôt qu'une affirmation ?

### L.7 — Avant de critiquer
☐ Ai-je demandé la date ? · ☐ Ai-je demandé le motif ? · ☐ Ai-je commencé par un point fort ? · ☐ **Ai-je une seule recommandation ?** · ☐ Ai-je chiffré son coût ?

### L.8 — Avant de concevoir
☐ Le service est-il formulé côté métier ? · ☐ L'interruption tolérable est-elle **chiffrée** ? · ☐ La perte de données tolérable est-elle chiffrée ? · ☐ **Combien d'exploitants disponibles ?** · ☐ Qu'accepte-t-on de perdre ? · ☐ Ai-je envisagé de renoncer à une fonctionnalité ?

### L.9 — Avant de livrer une conception
☐ Registre des compromis écrit ? · ☐ Conditions de réexamen ? · ☐ Ce qui reste à vérifier ? · ☐ L'architecture est-elle exploitable par l'organisation telle qu'elle est ?

### L.10 — Avant de placer un dispositif
☐ Que voit-il depuis cet emplacement ? · ☐ **Que ne voit-il pas ?** · ☐ Quelle proportion des flux y passe ? · ☐ Est-ce le point le plus riche disponible ? · ☐ Que déclare-t-on non couvert ?

---


## Journal des modifications

| Version | Date | Nature |
|---|---|---|
| 1.0 | 02/08/2026 | Première rédaction : 9 parties, 50 chapitres, 3 cas de synthèse, 14 mini-labs, 12 annexes, 26 schémas |
| 1.8 | 02/08/2026 | **Couche de culture architecturale.** Ajout de **trois niveaux de lecture explicites** — 🧠 à maîtriser · 🔭 à reconnaître · 📚 à approfondir — pour éviter qu'un lecteur ne mémorise vingt-deux acronymes au même rang que les notions fondamentales. **Vingt-deux blocs 🔭 À RECONNAÎTRE**, dispersés là où chaque notion devient naturelle et jamais en catalogue de fin d'ouvrage, chacun répondant à six questions : ce que c'est · le problème résolu · où on le rencontre · l'effet sur les flux et dépendances · le coût introduit · **ce qu'il faut demander en réunion**. Répartition : BGP (§9.2) · MPLS et SD-WAN (§26.3) · VXLAN et EVPN (§24.3) · WAF et CDN (§12.3) · passerelle d'interconnexion (§25.5) · HSM (§17.3) · PAM (§27.3) · NAC (§24.4) · SASE, SSE et CASB (§39.4) · VDI et hyperconvergence (§23.3) · réseau de stockage dédié, immutabilité et quorum (§23.5) · maillage de services (§41.4) · passerelle d'interfaces et consensus distribué (§42.3) · mainframe (§4.2) · calcul intensif (§5.4). **Index en annexe B bis.** Deux notions traitées avec une prudence particulière : les sigles de marché — *ils décrivent des familles de capacités, pas des implémentations identiques* — et la passerelle d'interconnexion, présentée comme **une fonction architecturale et non un équipement**, avec le principe qui la fonde : *relier deux réseaux ne signifie pas qu'ils doivent devenir un seul périmètre de confiance*. |
| 1.7 | 02/08/2026 | **Version de stabilisation. Contenu gelé.** ① **Numérotations corrigées** : sections 35.4 et 45.5 dupliquées · **annexe L normalisée en L.1 à L.10**. ② **Absolus résiduels** repris : dix-sept classements empiriques non démontrés reformulés — *la plus fréquente* devient *très répandue* ou *courante*, selon le cas. ③ **Responsabilité cloud harmonisée** : les données et les accès ne « ne bougent jamais » plus — ils **restent des responsabilités à gouverner, même lorsque leur mise en œuvre est partagée avec le fournisseur**. ④ **Chapitre 34 corrigé** : la journalisation ne suit plus *exactement les points de passage* mais **les points en position de savoir** — un composant peut être sur un chemin, ou à l'origine d'une décision sans qu'aucun flux ne le traverse. ⑤ **Renvois internes vérifiés** : 165 renvois contrôlés · **deux épisodes du fil rouge, perdus lors des réécritures des chapitres 5 et 6, ont été restaurés** — les six zones et les 620 postes invisibles. ⑥ **Catalogue des schémas complété** : les 4 schémas ajoutés en densification y figurent. ⑦ **Légende des blocs complétée** : les cinq blocs récurrents non documentés y sont. ⑧ **Les huit règles éditoriales sont devenues des principes nommés** — trois flux, contrainte, coupe, coût, visuel, modèle, hypothèse, **preuve** — et les références nues *R7*, *R8* du corps du texte ont été remplacées par leur nom. |
| 1.6 | 02/08/2026 | **Passe éditoriale finale.** **Superlatifs** : dix-neuf formulations qui prétendaient à une fréquence factuelle sans données ont été ramenées à des constats hedgés — *la voie d'entrée la plus fréquente* devient *une voie d'entrée majeure*, *l'état le plus fréquent* devient *un état très répandu*, *la base est toujours au fond* devient *dans le modèle à trois niveaux*. Les superlatifs exprimant un **jugement pédagogique assumé** — *le piège de lecture le plus fréquent du cours*, *la question la plus utile* — sont conservés : ils engagent l'auteur, pas une statistique. **Cohérence texte / corrigés** : avertissement ajouté en tête des barèmes des trois cas — ils notent des comportements, pas des réponses · une architecture différente du corrigé obtient le plein barème si l'arbitrage est écrit (§48.0) · une identification formulée avec certitude perd des points même si elle est juste *(principe d'hypothèse)* · rappel explicite dans le mini-lab 13 que la grille relève six points et n'en propose qu'un (§36.4, §49.3). |
| 1.5 | 02/08/2026 | **Comblement des trois manques de couverture.** **Accès sans fil** (§24.4) : le chemin poste → point d'accès → contrôleur → segment, la question *le sans-fil est-il un réseau distinct ou une autre porte sur le même segment ?*, les trois modes, réseaux multiples annoncés contre segments réels, clé partagée contre authentification individuelle. **Communication asynchrone** (§42.4) : file, courtier, publication/abonnement, journal d'événements · les cinq gains du découplage et **les sept problèmes qu'on achète** — accumulation, retard, doublons, ordre, rejeu, file d'échecs, observabilité · le courtier comme nouveau point de rupture · deux scénarios dont l'accumulation silencieuse. **RTO et RPO** (§46.3) : introduits en distinguant explicitement tolérance métier maximale, objectif de reprise et délai réel mesuré · traduction du RPO en décisions d'architecture. **Avertissement sur les chiffres d'exploitation** en tête du chapitre 48 : ce sont des données de scénario, pas des ratios transposables. Six pièges et deux checklists ajoutés. |
| 1.4 | 02/08/2026 | **Passe d'édition technique, après troisième revue.** Correction de **douze formulations erronées ou trop absolues** : erreur arithmétique sur la fréquence de sauvegarde (24 h → 8 h est une division par trois) · les trois sens du mot « expiration » en résolution de noms · un appel entre modules d'un monolithe **peut** échouer fonctionnellement, ce qui disparaît est la classe d'échec réseau · les transactions distribuées existent, avec leurs quatre approches et leur coût · la découverte de service n'est pas un remplacement du DNS, elle est souvent implémentée avec lui · sur un service en ligne les cinq actions **se déplacent** vers configuration, identités et données au lieu de disparaître · une action exige un **point d'observation ou de décision**, pas nécessairement un point de passage réseau · lenteur constante contre variable est un **indice**, pas une loi · un domaine d'annuaire fonctionne avec un seul contrôleur, deux étant recommandés · le comportement de vérification de révocation **varie fortement** selon les clients · une panne à horaire net **oriente** vers une échéance sans la prouver · le modèle de responsabilité cloud nuancé : *responsable* ne signifie pas *maître de tous les réglages*. **Ajout du stockage d'infrastructure** (§23.4) : bloc, fichier et objet · quatre architectures · et surtout la distinction **réplication / instantané / sauvegarde**, avec ce que chacune ne protège pas. Quatre pièges et une checklist ajoutés. |
| 1.3 | 02/08/2026 | **Achèvement de la densification.** 75 500 → 76 000 mots. Chapitres restés à moitié traités repris au même format : zones et frontières (§5), poste utilisateur avec les deux chemins d'un nomade (§6), segmentation avec son coût chiffré et l'angle mort des flux périodiques (§24), cycle de la donnée et calcul du nombre réel de copies (§32), placement d'une même sonde à trois endroits (§44), et **lecture entièrement déroulée des sept passes** sur le schéma d'HELIOMED, à la première personne (§36.3). Ajout du tableau de synthèse du chapitre 45 : cinq décisions d'architecture, cinq conséquences des années plus tard, aucune rattrapable par un produit ou un budget. **Totaux : 38 scénarios de panne · 34 tableaux de vocabulaire de réunion · 33 schémas.** |
| 1.2 | 02/08/2026 | **Passe de densification, après seconde revue externe.** +17 500 mots, placés uniquement là où le raisonnement manquait — aucune définition ajoutée. **Partie II entièrement réécrite** : chaque composant gagne son mécanisme interne « juste assez pour raisonner », des architectures comparatives, un scénario de panne au format *symptôme / hypothèse naïve / dépendance réelle / ce que le schéma aurait dû montrer*, et un tableau **vocabulaire de réunion** avec ce qu'il faut vérifier avant de croire une affirmation. **Parties III, IV et V densifiées** de la même façon. Ajouts structurants : les **quatre chemins vers un même service** (§29.3) · la **superposition de dix flux** sur un service unique, dont trois seulement sont dessinés (§35.3) · les **six comparaisons cloud** avec la grille *je n'exploite plus / je conçois toujours / quelle dépendance ai-je achetée* (§39.4) · le **lien de synchronisation d'identités** comme composant critique invisible (§40.3) · **deux mauvaises architectures**, l'insuffisante et l'excessive (§37.5) · et le **capstone de conception itérative** en cinq événements, où la capacité d'exploitation arrive en dernier et remet tout en cause (§48.5). Dix-huit scénarios de panne ajoutés. Vingt-quatre tableaux de vocabulaire de réunion. |
| 1.1 | 02/08/2026 | **Passe de précision technique, après revue externe.** Trois règles nouvelles : **R6** un modèle pédagogique n'est pas une loi technique · **R7** une observation produit une hypothèse, pas une identification · **R8** un schéma révèle une intention de redondance, seul un test établit une capacité. Ajout d'un **préambule « socle réseau minimal »** — deux niveaux d'adressage, sous-réseau, passerelle, sens d'établissement, traduction d'adresses, deux familles d'adressage. Ajout du **schéma des trois modes de terminaison du chiffrement**. Correction de treize formulations absolues devenues fausses hors de leur modèle : dépendance à la résolution de noms · service d'annuaire contre Active Directory · LDAP contre authentification · rôle exact d'un certificat · portée d'une autorité privée · ce qu'un commutateur et un routeur interprètent · isolation à l'intérieur d'un segment · terminaison du chiffrement · effet d'une panne de base · absence d'état d'un serveur web · révocation d'un jeton autoporté · chemin de retour d'une requête · correspondance entre familles de flux et niveaux de dégradation. **Mini-labs d'identification transformés en labs d'hypothèses.** Ajout du vocabulaire des **exigences non fonctionnelles**, du réflexe **logique contre physique**, de trois blocs **« le même composant, plusieurs placements »**, et du déroulé de conception en dix étapes avec autocritique. Passe anti-superlatifs et anti-fausse-précision. Deux principes de doctrine ajoutés. Neuf pièges ajoutés à l'annexe G. |

**Les huit principes appliqués** : R1 trois flux · R2 contrainte · R3 coupe · R4 coût · R5 visuel · R6 modèle · R7 hypothèse · R8 preuve.

**Prochaine revue recommandée** : février 2027. Ce cours contient peu de données périssables — c'est une conséquence du principe de coupe.

---

*Fin du document.*
