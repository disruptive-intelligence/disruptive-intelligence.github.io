---
title: PARTIE VIII — La vue cybersécurité
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 9
chapters: 10
---

> **Le raccordement à toute la collection.** Les mêmes schémas, la quatrième question : **où peut-on agir ?**
>
> Cette partie n'enseigne aucune technique de sécurité. Elle enseigne où une technique peut être appliquée — et surtout **où elle ne peut pas l'être**, parce que des décisions prises avant vous l'ont rendu impossible.

---

## Chapitre 43 — Où peut-on agir ?

### 43.1 Les cinq actions

Toute la sécurité opérationnelle se ramène à cinq actions applicables à un point d'une architecture.

🖼 **SCHÉMA 43.1 — Les cinq actions**

```
   OBSERVER      voir ce qui passe, sans l'empêcher
   FILTRER       empêcher ce qui ne doit pas passer
   AUTHENTIFIER  exiger une preuve d'identité avant de laisser passer
   SEGMENTER     empêcher deux choses de se joindre
   JOURNALISER   conserver la trace de ce qui s'est passé
```

**Deux propriétés qui structurent le chapitre** :

| Propriété | Conséquence |
|---|---|
| **Chaque action exige un point d'observation ou de décision** | Ce qui ne traverse aucun composant capable d'observer, de décider ou de tracer échappe à toute action |
| **Chaque action a un coût** | *Principe du coût* : latence, exploitation, faux positifs, volume |

> **Corollaire** : les points où l'on peut agir sont les **points de passage réseau** et les **composants capables de produire un événement**. Cartographier les uns revient largement à cartographier les autres — §34.4.

📌 **Nuance importante** : tout ne passe pas par le réseau. **Une application produit un événement métier — « Marie a exporté 4 000 lignes » — sans qu'aucun intermédiaire ne le voie passer.** C'est même la seule source capable de le produire, §34.2. De même, un poste observe une activité locale que rien ne traverse.

> **Le modèle du point de passage vaut pour le réseau. Pour l'observation, la question est plus large : quel composant est en position de savoir ?**

### 43.2 Où chaque action est possible

| Action | Points possibles | Où c'est **impossible** |
|---|---|---|
| **Observer** | Pare-feu · mandataires · commutateurs · postes · serveurs | Dans un flux chiffré non terminé · **chez un tiers** |
| **Filtrer** | Pare-feu · mandataires · segments | À l'intérieur d'un segment · **chez un tiers** |
| **Authentifier** | Mandataire inverse · applicatif · annuaire · accès distant | Entre deux serveurs qui se font confiance par adresse |
| **Segmenter** | Entre zones · entre segments · au niveau du poste | **Entre machines d'un même segment**, sans mesure explicite |
| **Journaliser** | Tout composant qui traverse un flux | Ce qui ne traverse aucun composant journalisant |

⚠️ **La colonne de droite est la plus utile du chapitre.** Elle dit ce qu'aucun produit ne résoudra, parce que l'architecture ne le permet pas. Trois cas reviennent :

**① À l'intérieur d'un segment.** Sans mécanisme dédié — pare-feu local, isolation de ports, microsegmentation — six cents postes d'un même segment se joignent librement, et aucun pare-feu périmétrique n'y change rien. §24.1.

**② Dans un flux chiffré non terminé.** Un flux chiffré de bout en bout ne s'observe pas en chemin. Pour le voir, il faut le terminer — c'est ce que fait un mandataire inverse en modes B et C, §12.3.

**③ Chez un tiers.** Sur un service en ligne, **les cinq actions ne sont pas applicables à son infrastructure**. Elles se déplacent vers ce que vous maîtrisez encore : configuration, identités, données, journaux exposés — §42.5.

### 43.3 Les points de passage d'une architecture type

Reprenons le schéma 1.1 et marquons ce qui est possible où.

```
                        INTERNET
                            │
   ┌────────────────────────┼─────────────────────────────────┐
   │  [ pare-feu ]          │   OBS ✓  FILT ✓  AUTH ✗  SEG ✓  JOURN ✓
   ├────────────────────────┼─────────────────────────────────┤
   │  [ mandataire ]        │   OBS ✓✓ FILT ✓  AUTH ✓✓ SEG ✗  JOURN ✓✓
   │       ↑ le point le plus riche : il voit le contenu en clair
   │         MAIS uniquement pour les accès EXTERNES — §29.3
   ├────────────────────────┼─────────────────────────────────┤
   │  [ répartiteur ]       │   OBS ✓  FILT ~  AUTH ✗  SEG ✗  JOURN ✓
   ├────────────────────────┼─────────────────────────────────┤
   │  [ web ×3 ]            │   OBS ✓  FILT ✗  AUTH ~  SEG ✗  JOURN ✓
   ├────────────────────────┼─────────────────────────────────┤
   │  [ applicatif ]        │   OBS ✓  FILT ✗  AUTH ✓✓ SEG ✗  JOURN ✓✓
   │       ↑ le seul point qui connaisse l'UTILISATEUR
   │         et l'ACTION MÉTIER — §34.2
   ├────────────────────────┼─────────────────────────────────┤
   │  [ base ]              │   OBS ✓  FILT ✗  AUTH ~  SEG ✗  JOURN ✓
   │       ↑ voit les requêtes, PAS l'utilisateur final
   └────────────────────────┴─────────────────────────────────┘
```

👁 **CE QU'IL FALLAIT OBSERVER**

**Deux points concentrent la valeur, et ce ne sont pas les mêmes.**

Le **mandataire inverse** est le point le plus riche techniquement : il voit tout le trafic externe en clair, il peut filtrer, authentifier et journaliser. **Et il ne voit que les accès externes** — §29.3.

L'**applicatif** est le seul point qui connaisse simultanément **l'utilisateur réel et l'action métier**. Un journal d'applicatif dit *« Marie a exporté 4 000 lignes »* ; un journal de pare-feu dit *« une adresse a ouvert une connexion »*. **C'est la différence entre une trace exploitable et une trace technique.**

⚠️ **Aucun de ces deux points n'est celui où l'on met le plus de moyens en pratique** — les moyens vont majoritairement au périmètre, qui voit le moins.

### 43.4 Ce qui rend une action impossible, par cause

**Quatre causes, et elles n'appellent pas les mêmes réponses** :

| Cause | Exemple | Que faire |
|---|---|---|
| **Architecturale** | Pas de point de passage entre deux machines d'un segment | **Changer l'architecture**, ou déclarer non couvert |
| **Technique** | Le composant ne sait pas produire de journal | Observer ailleurs sur le chemin |
| **Contractuelle** | Un service en ligne ne donne pas accès à ses journaux | Négocier, ou accepter et déclarer |
| **Organisationnelle** | Le composant est administré par une autre équipe | **La plus fréquente, et la seule qui se résolve sans budget** |

⚠️ **La quatrième mérite d'être nommée** : beaucoup d'angles morts ne sont ni techniques ni budgétaires. **Ils existent parce que personne n'a demandé.** C'est le cas des journaux d'un équipement réseau, d'un progiciel métier, ou d'un service géré par une filiale.

### 43.5 Le coût de chaque action

⚖️ **CONTRAINTE ET COÛT**

| Action | Coût principal | Ce qui la fait abandonner |
|---|---|---|
| **Observer** | Volume, stockage, exploitation | **Personne ne regarde ce qui est collecté** |
| **Filtrer** | Faux blocages, règles à maintenir | Une règle trop stricte casse un usage légitime |
| **Authentifier** | Latence, dépendance à l'annuaire, friction | **Les utilisateurs contournent** — §24.2 |
| **Segmenter** | Flux à ouvrir, dépannage difficile | Le processus d'ouverture devient trop lent |
| **Journaliser** | Volume, rétention, coût de stockage | **La rétention est réduite pour tenir le budget** — §34.3 |

⚠️ **La dernière ligne est celle qui coûte le plus cher en incident.** La rétention est le premier poste réduit quand le budget serre, et c'est exactement ce qui empêche d'enquêter plus tard.

🔥 **SCÉNARIO — le contrôle existe, il ne voit rien**

| Question | Réponse |
|---|---|
| Symptôme | Une compromission interne s'est déroulée pendant onze jours. **Aucune alerte** |
| Hypothèse naïve | « Le dispositif de détection a échoué » |
| Dépendance réelle | **Il était placé au périmètre.** L'activité était entièrement interne — §44.4 |
| Ce que le schéma aurait dû montrer | Les points de passage internes, et ce qu'ils observent |
| Concevoir différemment | **Segmenter d'abord** : sans point de passage, il n'y a rien à observer |

⚠️ **Ce scénario ferme la boucle du cours** : **segmenter n'est pas seulement une mesure de protection, c'est une condition de détection** — §45.3. Dans une architecture plate, un mouvement latéral ne traverse aucun point observable : **il est invisible par construction**.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a de la visibilité » | Des sondes ou des agents existent | **Sur quel périmètre ? Combien de flux y passent ?** |
| « Tout est loggé » | Beaucoup de sources sont collectées | **Combien de temps ? Et l'identité est-elle préservée ?** |
| « On a mis un WAF » | Un filtrage applicatif en frontal | **Il ne voit que les accès externes** — §29.3 |
| « Ce n'est pas possible techniquement » | Une action est écartée | **Architecturale, technique, contractuelle ou organisationnelle ?** — §43.4 |

---

## Chapitre 44 — Placer les dispositifs

### 44.1 Le principe

> **Le bon emplacement d'un dispositif dépend de l'architecture, pas du produit.**

Un même produit placé à deux endroits différents ne voit pas la même chose, ne protège pas les mêmes actifs, et ne produit pas les mêmes traces.

### 44.2 Les emplacements, par dispositif

| Dispositif | Emplacement pertinent | Ce qu'il voit | Ce qu'il **ne voit pas** |
|---|---|---|---|
| **Pare-feu** | Entre deux zones | Ce qui traverse la frontière | **Ce qui reste dans une zone** |
| **Détection sur poste** | Sur chaque poste et serveur | L'activité locale, les processus | Ce qui se passe sur ce qui n'en porte pas |
| **Sonde réseau** | Sur un point de passage, en dérivation | Les flux qui y transitent | **Les flux chiffrés · ceux qui ne passent pas là** |
| **Scanner de vulnérabilités** | Au plus près des cibles | Ce qu'il peut joindre | **Ce qui est derrière un filtre, ou éteint** |
| **Collecte de journaux** | Centralisée, alimentée par tous | Ce que les sources envoient | **Ce qui n'est pas configuré pour émettre** |
| **Point d'authentification** | Mandataire, applicatif, ou les deux | Les accès qui y passent | **Les accès internes directs** — §29.3 |

⚠️ **La colonne de droite définit la couverture réelle.** Un dispositif ne protège que ce qu'il voit, et un schéma dit exactement ce qu'il voit.

### 44.3 Le même dispositif, trois emplacements — l'exemple de la sonde

**C'est l'exercice qui installe le principe.**

```
  A — SONDE AU PÉRIMÈTRE
      Internet ──►[SONDE]──► [ FW ] ──► DMZ ──► interne
      VOIT     : ce qui entre et sort
      NE VOIT PAS : tout le trafic interne — postes vers serveurs
      COUVERTURE RÉELLE : faible en volume, forte en visibilité externe

  B — SONDE ENTRE POSTES ET SERVEURS
      [ postes ] ──►[SONDE]──► [ serveurs ]
      VOIT     : le mouvement latéral, la reconnaissance, la collecte
      NE VOIT PAS : ce qui reste entre postes
      COUVERTURE RÉELLE : la phase la plus longue d'une compromission

  C — SONDE DEVANT LA BASE
      [ applicatif ] ──►[SONDE]──► [ base ]
      VOIT     : les requêtes vers les données
      NE VOIT PAS : qui les a demandées — §34.2
      COUVERTURE RÉELLE : étroite, mais sur l'actif le plus sensible
```

| Emplacement | Volume de trafic observé | Phase d'attaque couverte |
|---|---|---|
| **A — périmètre** | Faible | Accès initial |
| **B — postes/serveurs** | **Élevé** | **Reconnaissance, mouvement latéral, collecte** |
| **C — devant la base** | Faible | Exfiltration |

⚠️ **Le placement A est un réflexe courant, et c'est celui qui observe le plus petit volume de trafic.** Le placement B couvre la phase la plus longue d'une compromission — celle qui dure des jours ou des semaines. **Et il exige un point de passage, donc une segmentation** : c'est le §45.3.

### 44.4 Les quatre emplacements impossibles, et ce qu'on fait alors

| Situation | Pourquoi c'est impossible | Ce qu'on fait |
|---|---|---|
| **Un agent sur un automate industriel** | Constructeur ne le supporte pas, ressources insuffisantes, garantie perdue | Observation passive du réseau · segmentation stricte · §28.6 |
| **Un scanner authentifié sur un système hérité** | Pas de compte disponible, risque d'indisponibilité | Inventaire déclaratif · scan passif · **périmètre déclaré non couvert** |
| **Une sonde sur un flux chiffré de bout en bout** | Rien à voir sans le terminer | Journalisation aux extrémités · métadonnées uniquement |
| **Un contrôle sur un service en ligne** | Ce n'est pas chez vous | Configuration du service · **journaux du fournisseur, s'il en donne** |

**Le point commun des quatre réponses** : quand une action est impossible à un endroit, **on la déplace, on la remplace, ou on déclare la zone non couverte**. On ne fait jamais semblant.

⚠️ **C'est exactement la doctrine des périmètres déclarés non couverts du volume Maintien en condition de sécurité.** Une zone où l'on ne peut pas agir est acceptable **si elle est déclarée** ; elle est dangereuse quand elle est ignorée.

### 44.5 L'erreur de placement la plus coûteuse

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous placez une sonde réseau sur le lien Internet pour détecter les intrusions. Quelle proportion de l'activité de votre organisation voyez-vous ?*
**Une fraction — et pas celle que vous croyez.** Vous voyez ce qui entre et sort. Vous ne voyez **rien** de ce qui se passe entre les six cents postes et les serveurs internes, c'est-à-dire là où se déroule l'essentiel d'une compromission après l'accès initial. La mauvaise décision évitée : **placer les moyens au périmètre en croyant couvrir l'organisation**, et découvrir en incident que les onze jours d'activité interne n'ont laissé aucune trace exploitable.

🔥 **SCÉNARIO — le scanner ne voit pas ce qu'il devrait voir**

| Question | Réponse |
|---|---|
| Symptôme | Un scan hebdomadaire remonte 40 machines. L'inventaire en compte 214 |
| Hypothèse naïve | « Le scanner est mal configuré » |
| Dépendance réelle | **Il est placé dans un segment, et le filtrage inter-segments le bloque** |
| Ce que le schéma aurait dû montrer | Depuis où le scanner opère, et ce qu'il peut joindre |
| Concevoir différemment | Un point de scan par zone · ou des règles dédiées, **et alors le scanner devient un chemin privilégié à protéger** |

⚠️ **La dernière ligne est un compromis qu'on oublie** : donner au scanner le droit de joindre tout le parc en fait **une cible de choix**. Un scanner compromis dispose d'un accès réseau que personne d'autre n'a. **Principe du coût.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est couverts à 95 % » | Un agent est déployé sur 95 % des machines | **Et les 5 % restants ? Ce sont souvent les plus anciennes** |
| « La sonde ne voit rien » | Peu d'alertes | **Est-elle bien placée ?** Peu d'alertes peut vouloir dire peu de trafic observé |
| « Le scan est passé » | Un balayage a eu lieu | **Combien de machines a-t-il vues, sur combien d'attendues ?** |
| « On mettra un agent plus tard » | Un périmètre non couvert | **Est-ce déclaré quelque part, ou oublié ?** |

---

## Chapitre 45 — Ce que l'architecture impose au reste

> Le chapitre de raccordement. Il explique pourquoi les autres volumes de la collection demandent d'assumer certains compromis : **ils sont déterminés ici**.

### 45.1 Ce que l'architecture impose au maintien en condition de sécurité

| Ce que l'architecture détermine | Conséquence sur le maintien |
|---|---|
| **L'interruptibilité** | Un composant qui ne peut pas s'arrêter ne sera pas corrigé — quelle que soit la politique |
| **La redondance** | Sans elle, toute correction impose une interruption |
| **Le nombre de composants uniques** | Chaque point de rupture est une fenêtre de maintenance négociée |
| **Les dépendances** | Corriger un composant peut arrêter un service qu'on ne soupçonnait pas |
| **Le cycle de vie du plus ancien composant** | Il fixe le plancher de modernisation de tout ce qui en dépend |

> **La formulation qui résume** : *aucune politique de correctifs ne rattrape une architecture non interruptible.*

**C'est le principe 7 du volume Maintien en condition de sécurité** — *le coût du maintien se décide en conception, pas en exploitation* — et ce chapitre en donne la démonstration architecturale.

🔥 **SCÉNARIO — le correctif ne sera jamais appliqué**

| Question | Réponse |
|---|---|
| Symptôme | Une vulnérabilité critique reste ouverte depuis quatorze mois |
| Hypothèse naïve | « L'équipe ne fait pas son travail » |
| Dépendance réelle | **Le composant est unique, et son arrêt stoppe une chaîne de production** |
| Ce que le schéma aurait dû montrer | Qu'aucune redondance n'existe sur ce composant |
| Concevoir différemment | **La décision qui a produit cette situation date de la conception**, pas de l'exploitation |

### 45.2 Ce que l'architecture impose à l'inventaire

| Ce que l'architecture détermine | Conséquence sur l'inventaire |
|---|---|
| **Ce qui est découvrable** | Un actif sur un segment non balayé n'apparaîtra pas |
| **Ce qui a une adresse stable** | Un actif éphémère échappe aux méthodes classiques — §41.4 |
| **Ce qui appartient à un tiers** | Ne se découvre pas : **se déclare** |
| **Ce qui est derrière un filtre** | Invisible au scanner, existant quand même — §44.5 |
| **Le nombre de zones** | Chaque zone est une campagne de découverte distincte |

**Les cinq lignes annoncent le chapitre 11 du volume Asset Management**, et elles expliquent pourquoi cinq zones sont restées non couvertes chez HELIOMED en février 2026 : **ce n'était pas un défaut de méthode, c'était une conséquence de l'architecture.**

### 45.3 Ce que l'architecture impose à la détection

| Ce que l'architecture détermine | Conséquence sur la détection |
|---|---|
| **Les points de passage** | Ce sont les seuls endroits où l'on peut observer — §43.1 |
| **Le chiffrement de bout en bout** | Rend la sonde réseau inopérante sur le contenu |
| **La position du mandataire** | Détermine si l'identité réelle est visible en aval — §34.2 |
| **La segmentation** | Détermine si un mouvement latéral traverse un point observable |
| **Les composants sans agent** | Créent des angles morts structurels |

⚠️ **La quatrième ligne est celle qui décide de tout.** Dans une architecture plate, un mouvement latéral ne traverse **aucun** point observable : il est invisible par construction. **Segmenter n'est donc pas seulement une mesure de protection, c'est une condition de détection.**

### 45.4 Ce que l'architecture impose à la réponse à incident

| Ce que l'architecture détermine | Conséquence sur la réponse |
|---|---|
| **Les dépendances** | Ce qu'on peut isoler sans arrêter un service |
| **La segmentation** | Si l'isolement est possible du tout |
| **Les chemins d'administration** | Si l'on peut encore administrer un système compromis — §27.4 |
| **Les sauvegardes et leur chemin** | Si la restauration est possible depuis un environnement sain |
| **La journalisation et sa rétention** | **Si l'on peut savoir ce qui s'est passé** — §34.3 |

⚠️ **La troisième ligne est celle qu'on découvre en crise.** Si le chemin d'administration passe par le réseau compromis, on ne peut plus administrer sans risquer d'exposer des identifiants privilégiés. **C'est une décision d'architecture prise des années plus tôt qui détermine ce qu'on peut faire un dimanche soir.**

🔥 **SCÉNARIO — on ne peut isoler que tout ou rien**

| Question | Réponse |
|---|---|
| Symptôme | Compromission confirmée sur un serveur. **Aucun confinement partiel possible** |
| Hypothèse naïve | « Il faut couper le réseau » |
| Dépendance réelle | **Une seule zone** : isoler ce serveur suppose de savoir ce qui en dépend, et rien ne le dit |
| Ce que le schéma aurait dû montrer | L'arbre de dépendance du service — §35.2 |
| Ce que cela coûte | **On coupe tout, ou on ne coupe rien.** Les deux options sont mauvaises |

### 45.5 Le tableau de synthèse

**Ce que le lecteur doit emporter du chapitre** :

| Une décision d'architecture… | …détermine des années plus tard |
|---|---|
| Redonder ou non | **Si un correctif pourra être appliqué** |
| Segmenter ou non | **Si une compromission sera visible** |
| Isoler l'administration ou non | **Si l'on pourra intervenir pendant un incident** |
| Journaliser et conserver ou non | **Si l'on pourra savoir ce qui s'est passé** |
| Documenter les dépendances ou non | **Si l'on pourra confiner sans tout casser** |

> **Aucune de ces cinq lignes ne se rattrape par un produit, un budget ou une procédure.** Elles sont déterminées à la conception, et c'est pourquoi ce volume est le premier de la collection.

### 45.6 🔬 Mini-lab 10 — Placer les cinq actions

**Objectif** — Décider où placer chaque action sur une architecture donnée, et déclarer les zones non couvrables.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** chapitres 43 à 45

**L'architecture** : celle du mini-lab 7 — cinq zones, aucune frontière entre DMZ et interne, un annuaire dans le segment des 400 postes, une supervision industrielle joignable depuis les postes.

**Le budget** : trois actions seulement peuvent être financées cette année.

❓ Lesquelles, où, et que déclarez-vous non couvert ?

---

**Corrigé**

**Les trois actions retenues, et leur justification**

| # | Action | Emplacement | Pourquoi celle-ci |
|---|---|---|---|
| **1** | **Segmenter** | Entre les 400 postes et le segment industriel | **Un poste compromis atteint aujourd'hui la supervision sans traverser aucun filtre.** C'est le chemin le plus court vers le risque le plus grave — atteinte à la sûreté, §28.1 |
| **2** | **Segmenter** | Frontière 2, entre DMZ et interne | Sans elle, la DMZ n'en est pas une. Un composant exposé compromis atteint tout — §25.1 |
| **3** | **Journaliser** | Applicatif et annuaire | Les deux seuls points qui connaissent **l'utilisateur réel et l'action** — §43.3 |

**Pourquoi pas les autres**

| Écartée | Motif |
|---|---|
| Sonde réseau au périmètre | Voit ce qui entre, pas les 400 postes — §44.4 |
| Détection sur poste | Souhaitable, mais ne corrige pas les deux brèches structurelles |
| Authentification renforcée | Pertinente, et sans effet tant que la segmentation manque |

**Ce qu'on déclare non couvert**

> *Les échanges à l'intérieur du segment des 400 postes ne sont ni observés, ni filtrés. Une compromission d'un poste atteint les 399 autres sans traverser aucun point de contrôle. Cette situation est connue, non traitée cette année faute de moyens, et réexaminée au budget suivant.*

**Les trois erreurs attendues**

1. **Choisir la sonde réseau au périmètre.** C'est le réflexe, et c'est l'erreur du §44.4 — elle voit le moins de l'activité réelle.
2. **Choisir l'authentification renforcée en premier.** Elle est utile, et elle ne change rien tant qu'un poste compromis atteint la supervision industrielle par un chemin direct.
3. **Ne rien déclarer non couvert.** Trois actions ne couvrent pas tout. **Ce qui n'est pas traité doit être écrit** — sinon c'est un angle mort, pas un arbitrage.

---

> ### 🎓 À ce stade de la Partie VIII, vous savez…
>
> ✓ que toute la sécurité opérationnelle se ramène à **cinq actions**, et que chacune exige un **point d'observation ou de décision** ;
> ✓ que les points où l'on peut agir sont **exactement les points de passage** de l'architecture ;
> ✓ **où chaque action est impossible** — à l'intérieur d'un segment, dans un flux chiffré non terminé, chez un tiers ;
> ✓ que le **mandataire inverse** est le point le plus riche techniquement, et qu'il **ne voit que les accès externes** ;
> ✓ que l'**applicatif** est le seul point qui connaisse l'utilisateur réel et l'action métier — et qu'il reçoit rarement les moyens ;
> ✓ que le **bon emplacement dépend de l'architecture, pas du produit** ;
> ✓ que face à un emplacement impossible, on **déplace, on remplace, ou on déclare non couvert** — jamais on ne fait semblant ;
> ✓ que **segmenter est une condition de détection**, pas seulement une mesure de protection ;
> ✓ qu'une décision d'architecture prise il y a des années détermine **ce que vous pourrez faire un dimanche soir**.
>
> **Ce que vous ne savez pas encore** : comment proposer vous-même une architecture, et comment critiquer celle des autres. C'est l'objet de la Partie IX.

---
