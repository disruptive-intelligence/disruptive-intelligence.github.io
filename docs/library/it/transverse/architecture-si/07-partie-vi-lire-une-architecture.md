---
title: PARTIE VI — Lire une architecture
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 7
chapters: 10
---

> Tout ce qui précède devient ici une **méthode**. Trois chapitres : la grille, dix architectures de complexité croissante, et ce que les tiers ajoutent à un schéma.

---

## Chapitre 36 — La grille de lecture en sept passes

### 36.1 Pourquoi une méthode plutôt qu'un œil

**Le problème du lecteur non méthodique** : il regarde d'abord ce qui l'intéresse, ce qu'il reconnaît, ou ce qui est au centre du dessin. Il manque systématiquement les mêmes choses — les frontières implicites, les flux invisibles, ce qui n'a pas de doublure.

**Ce qu'une grille apporte** : un ordre fixe, qui garantit qu'on regarde ce qu'on n'aurait pas regardé.

🖼 **SCHÉMA 36.1 — Les sept passes**

```
  ①  LES ZONES        Où sont les frontières, et qu'est-ce qui les matérialise ?
  ②  L'ENTRÉE         Par où arrive un utilisateur externe ? Et un interne ?
  ③  LES DONNÉES      Où sont-elles, où vont leurs copies ?
  ④  L'IDENTITÉ       Où s'authentifie-t-on, contre quoi, combien de fois ?
  ⑤  LES FLUX         Quel chemin suit une requête ordinaire, en douze étapes ?
  ⑥  LES RUPTURES     Qu'est-ce qui n'a pas de doublure ?
  ⑦  L'INVISIBLE      Qu'est-ce qui n'est pas dessiné et existe pourtant ?
```

**L'ordre n'est pas négociable.** Chaque passe s'appuie sur la précédente : on ne peut pas suivre un flux (⑤) sans connaître les frontières (①) ; on ne peut pas identifier les ruptures (⑥) sans avoir suivi les flux.

### 36.2 Les sept passes, en détail

**① LES ZONES** — *Où sont les frontières ?*

| Question | Ce qu'on cherche |
|---|---|
| Combien de zones ? | Comparer aux six de référence — §5.2 |
| Qu'est-ce qui matérialise chaque frontière ? | Filtrage, segmentation, ou **rien** — §5.3 |
| Y a-t-il une seconde frontière après la DMZ ? | §25.1 |
| Un composant est-il à cheval ? | Frontière assumée ou brèche — §5.4 |

**② L'ENTRÉE** — *Par où entre-t-on ?*

Trois entrées à chercher, pas une : l'utilisateur **externe** · l'utilisateur **interne**, dont le chemin est souvent plus court · l'**administrateur**, dont le chemin n'est jamais dessiné — §27.

**③ LES DONNÉES** — *Où sont-elles ?*

On applique le §32.1 : base, réplicas, sauvegardes, recette, exports, rapports. **La question utile n'est pas où elles sont stockées, mais en combien d'endroits elles existent.**

**④ L'IDENTITÉ** — *Où s'authentifie-t-on ?*

| Question | Pourquoi |
|---|---|
| Contre quel composant ? | Annuaire, fédération, ou base applicative — §30.3 |
| Combien de fois sur un même parcours ? | Une seule authentification pour dix accès est un choix, avec ses conséquences |
| Que se passe-t-il si ce composant tombe ? | §30.2 |

**⑤ LES FLUX** — *Quel chemin suit une requête ?*

Les douze étapes du §29.1, en distinguant les trois familles. **C'est la passe la plus longue et la plus productive.**

**⑥ LES RUPTURES** — *Qu'est-ce qui n'a pas de doublure ?*

| Question | Piège |
|---|---|
| Quels composants sont uniques ? | Un rôle dessiné une fois peut être plusieurs — §3.1 |
| Les exemplaires sont-ils sur des hôtes différents ? | §23 — la redondance qui n'en est pas |
| Le basculement a-t-il été testé ? | §20 — une réplication non testée est une croyance |
| Où sont les sessions ? | §31.2 — la redondance qui ne protège pas |

**⑦ L'INVISIBLE** — *Qu'est-ce qui n'est pas dessiné ?*

La liste du §3.4, à passer systématiquement : résolution de noms · annuaire · horloge · administration · sauvegardes · postes · services en ligne · liens partenaires · certificats · versions · le temps.

### 36.3 Une lecture entièrement déroulée

**La méthode ne s'apprend pas en la lisant.** Voici les sept passes appliquées de bout en bout au schéma 1.1, telles qu'un lecteur exercé les conduirait — avec ses hésitations.

#### Passe ① — Les zones

*« Je compte trois zones dessinées : la DMZ, l'interne, l'industriel. Plus l'extérieur, implicite, et la bordure — les deux pare-feu. Cela fait cinq. »*

*« La frontière 1 est matérialisée : deux pare-feu. La frontière 2, entre DMZ et interne, **n'est pas dessinée**. Soit elle existe et n'est pas représentée, soit elle n'existe pas. C'est ma première question. »*

*« Le site industriel n'a qu'un lien. Par quoi passe-t-il ? Rien ne l'indique. Deuxième question. »*

**Constat de passe** : 5 zones · 1 frontière matérialisée sur 3 · 2 questions.

#### Passe ② — L'entrée

*« Utilisateur externe : Internet → pare-feu → mandataire. Clair. »*

*« Utilisateur interne : **rien n'est dessiné**. Les postes n'apparaissent pas. Or c'est de là que part la majorité des flux — §6.1. Et selon ce que répond la résolution interne, ils atteignent peut-être le serveur web directement, sans passer par le mandataire — §14.5. Troisième question. »*

*« Administrateur : **aucun chemin**. Quatrième question, et c'est celle qui compte le plus — §27.5. »*

**Constat de passe** : 1 entrée sur 3 dessinée.

#### Passe ③ — Les données

*« Une base est dessinée. Un serveur de fichiers aussi. Une sauvegarde. »*

*« Mais où sont les copies ? Réplicas ? Environnement de recette ? Exports ? Rapports ? **Rien** — §32.2. Cinquième question. »*

*« Et le chemin de la sauvegarde n'est pas dessiné : elle atteint la base, mais par où, et avec quel compte ? Sixième question — §21.4. »*

**Constat de passe** : 3 emplacements dessinés · nombre réel inconnu.

#### Passe ④ — L'identité

*« L'annuaire est dessiné. **Aucun trait ne s'y connecte.** C'est le cas canonique : tout s'y connecte, rien ne le montre — §1.1. »*

*« Combien de contrôleurs ? Un seul est dessiné. Si c'est le seul, c'est un point de rupture majeur. **Et même s'il y en a deux : sur des hôtes différents ?** — *principe de preuve*, §16.4. Septième question. »*

*« Où s'authentifie-t-on ? Sur le mandataire, ou dans l'application ? La réponse change ce qu'un poste interne traverse. Huitième question — §30.5. »*

**Constat de passe** : 1 composant dessiné, 0 relation, 2 questions.

#### Passe ⑤ — Les flux

*« Je suis une requête externe : douze étapes, cinq visibles — §29.1. »*

*« Je suis une requête interne : le chemin est plus court, et il ne traverse pas le mandataire. **Aucun des contrôles du mandataire ne s'y applique.** »*

*« Je suis une authentification : poste → annuaire. Non dessiné. »*

*« Je suis un journal : chaque composant → collecte. **La collecte n'est pas sur le schéma.** »*

**Constat de passe** : sur 4 flux suivis, 1 est partiellement dessiné.

#### Passe ⑥ — Les ruptures

*« Composants uniques dessinés : l'applicatif, la base, le mandataire — s'il est seul, ce que le schéma ne dit pas. »*

*« Composants uniques **non dessinés** : la résolution de noms, l'annuaire, les certificats. »*

*« Redondance apparente : trois serveurs web. **Sur des hôtes différents ? Où vivent les sessions ?** Sans réponse, je ne peux pas conclure — *principe de preuve*, §31.2. Neuvième et dixième questions. »*

**Constat de passe** : 3 ruptures visibles · 3 invisibles · 1 redondance non vérifiable.

#### Passe ⑦ — L'invisible

*« Je passe la liste de l'annexe H. »*

| Élément | Présent ? |
|---|---|
| Résolution de noms | ❌ |
| Annuaire | Dessiné, **non relié** |
| Synchronisation d'horloge | ❌ |
| Chemins d'administration | ❌ |
| Postes de travail | ❌ |
| Postes de prestataires | ❌ |
| Sauvegardes et leur chemin | Partiellement |
| Services en ligne | ❌ |
| Liens partenaires | ❌ |
| Certificats | ❌ |
| Environnements de recette | ❌ |
| Collecte de journaux | ❌ |
| Versions | ❌ |
| Le temps — date du schéma | ❌ |

**Constat de passe** : 12 éléments absents sur 14.

#### Le rendu, en une page

```
ARCHITECTURE : HELIOMED        DATE DU SCHÉMA : mars 2023 (non portée)
LU PAR : ...                   DATE DE LECTURE : ...

ZONES        5 · 1 frontière matérialisée sur 3
             frontière DMZ→interne : NON REPRÉSENTÉE
ENTRÉES      externe ✅ · interne ❌ · admin ❌
DONNÉES      3 emplacements dessinés · nombre réel inconnu
IDENTITÉ     1 annuaire dessiné, 0 relation · nombre de contrôleurs inconnu
FLUX         requête externe : 12 étapes, 5 visibles
             3 autres flux suivis : aucun dessiné
RUPTURES     3 visibles · 3 invisibles · 1 redondance non vérifiable
INVISIBLE    12 éléments absents sur 14

LES TROIS QUESTIONS À POSER À L'AUTEUR :
  1. Existe-t-il un filtrage entre la DMZ et le réseau interne ?
     → si non, ce n'est pas une DMZ
  2. Depuis quels postes administre-t-on ces serveurs ?
     → c'est le chemin le plus court vers la compromission totale
  3. Les trois serveurs web sont-ils sur des hôtes différents,
     et où vivent les sessions ?
     → sinon la redondance affichée ne protège pas
```

⚠️ **Sur les dix questions relevées, trois seulement sont posées.** C'est délibéré — §49.3, quatrième erreur : *une liste de dix recommandations est reçue comme un jugement global ; une recommandation unique, chiffrée et justifiée est reçue comme une contribution.* Les sept autres attendront.

**Durée réelle de cette lecture** : environ une heure, sans aucun accès technique, sans documentation, sans réunion.

### 36.4 Le rendu d'une lecture

**Une lecture produit un document d'une page**, pas une opinion.

```
ARCHITECTURE : ................  DATE DU SCHÉMA : ........
LU PAR : .............           DATE DE LECTURE : ........

ZONES        n zones · frontières matérialisées : ...
             frontières déclaratives : ...
ENTRÉES      externe : ...  interne : ...  admin : ...
DONNÉES      en n endroits : ...
IDENTITÉ     contre : ...  si indisponible : ...
FLUX         requête type : ... étapes, dont ... invisibles
RUPTURES     n identifiées, dont n invisibles
INVISIBLE    n éléments absents du schéma

LES TROIS QUESTIONS À POSER À L'AUTEUR :
  1. ...   2. ...   3. ...
```

**La dernière section est la plus utile.** Une lecture ne se conclut pas par un jugement mais par **trois questions** — et c'est aussi ce qui la rend acceptable par ceux qui ont conçu l'architecture. Le chapitre 49 y revient.

⚠️ **Le temps que prend une lecture complète** : une heure pour une architecture simple, une demi-journée pour un système réel. **Ce n'est pas un exercice de dix minutes**, et une lecture bâclée produit exactement les jugements naïfs du chapitre 4.

## Chapitre 37 — Dix architectures

> Complexité croissante. Chacune suit le format : schéma · questions · lecture commentée · **ce qu'il fallait observer**.
>
> Les quatre premières sont développées ici ; les six suivantes figurent en annexe F, avec leur lecture complète.

### 37.1 Architecture 1 — Une application interne, trois composants

```
   [ 40 postes ] ──► [ serveur applicatif ] ──► [ base ]
```

❓ **Trois questions** : où s'authentifie-t-on ? · qu'est-ce qui n'est pas dessiné ? · quel est le point de rupture ?

**Lecture** — c'est l'architecture d'Atelier Martin. Deux composants, un point de rupture par composant, aucune redondance. **Et c'est un choix cohérent** : quarante utilisateurs, une interruption d'une journée est tolérable, le coût d'une redondance n'est pas justifié par la contrainte.

👁 **CE QU'IL FALLAIT OBSERVER**
L'authentification n'est pas représentée. Deux cas possibles, et ils changent tout : soit l'application a sa propre base d'utilisateurs — auquel cas les mots de passe vivent dans la base, et leur qualité dépend de l'éditeur — soit elle interroge un annuaire, qui devient alors un troisième point de rupture invisible.

### 37.2 Architecture 2 — Un site web public

```
   Internet ──► [ pare-feu ] ──► [ mandataire ] ──► [ web ] ──► [ base ]
```

❓ Où passe la frontière 2 ? · qui voit le contenu en clair ? · que se passe-t-il si le certificat expire ?

**Lecture** — le mandataire termine le chiffrement : **il voit tout en clair**. C'est le point le plus sensible du schéma, et il est en zone démilitarisée, c'est-à-dire dans la zone dont on suppose qu'elle sera compromise.

👁 **CE QU'IL FALLAIT OBSERVER**
Aucune frontière n'est représentée entre le mandataire et le serveur web. Si elle n'existe pas, un mandataire compromis atteint directement le web, puis la base. **La DMZ n'en est alors pas une** — §25.1.

### 37.3 Architecture 3 — Trois niveaux, avec redondance partielle

C'est le schéma 1.1, celui d'HELIOMED.

❓ Où s'arrête la redondance ? · combien de points de rupture invisibles ? · pourquoi un seul applicatif ?

**Lecture** — quatre points de rupture, dont trois invisibles : base, applicatif, résolution de noms, annuaire. La redondance visible — trois serveurs web — porte sur le composant le plus facile à redonder et le moins critique.

👁 **CE QU'IL FALLAIT OBSERVER**
**La rupture de symétrie est une information, pas une erreur.** Trois web et un applicatif signalent un arbitrage : ici, le coût de licence de 2021 — §4.6. Un lecteur exercé demande l'histoire ; un débutant conclut à une incohérence. C'est le chapitre 4.

### 37.4 Architecture 4 — Un système hérité mal documenté

```
   [ postes ] ──► [ AS400-PROD ] ──► ?
                        │
                   [ HERMES ] ──► [ export nocturne ] ──► [ décisionnel ]
                        ▲
                        └─── [ automates usine ]
```

❓ Que fait `HERMES` ? · qui l'administre ? · que se passe-t-il s'il tombe ?

**Lecture** — c'est le cas du §4.6. Un composant de 2011, portant un ancien outil de gestion de production, recevant un flux quotidien de l'usine. **Personne ne sait exactement ce qu'il fait encore.**

👁 **CE QU'IL FALLAIT OBSERVER**
Trois signes convergent : un nom hors convention · une position à cheval entre deux mondes · un flux nocturne. **Les trois désignent une strate ancienne** — §4.2. La bonne réaction n'est pas de proposer sa suppression, c'est de demander sa date et son motif. Il porte peut-être une intégration que plus personne ne sait refaire.

### 37.5 Deux mauvaises architectures

> **Aussi formateur que les bonnes.** Apprendre à repérer l'excès d'architecture est aussi important que d'en repérer l'insuffisance.

#### Architecture 4 bis — l'insuffisance

```
                       Internet
                          │
                    [ pare-feu ]
                          │
        ┌─────────┬───────┴───────┬─────────┐
        │         │               │         │
   [ postes ] [ admin ]    [ application ] [ base ]
```

❓ **Qu'est-ce qui vous gêne ?**

| # | Constat | Pourquoi c'est grave |
|---|---|---|
| 1 | **Une seule zone** | Le pare-feu ne protège que du dehors. Tout est joignable de partout à l'intérieur — §24.1 |
| 2 | **L'administration au même niveau que les postes** | Un poste compromis atteint les outils d'administration — §27 |
| 3 | **La base joignable depuis les postes** | L'architecture en couches n'existe pas : on peut contourner l'application |
| 4 | **Aucune DMZ** | Si un service est publié, il l'est depuis l'interne |
| 5 | Ce qu'on ne voit pas | Résolution, annuaire, sauvegarde, journalisation — §3.4 |

⚠️ **Et pourtant, cette architecture n'est pas nécessairement fautive.** Chez une organisation de trente personnes, sans service publié, sans données sensibles, avec un informaticien à mi-temps, **elle peut être un arbitrage défendable** — §48.1. Ce qui la rend fautive, c'est de la trouver dans une organisation de sept cents personnes qui publie un portail client.

> **La question n'est jamais « cette architecture est-elle bonne ? » mais « pour quelle contrainte a-t-elle été conçue, et cette contrainte est-elle encore la bonne ? »**

#### Architecture 4 ter — l'excès

```
   40 salariés · 1 site · 1 application métier · 1 informaticien
                              │
                    2 centres de données
                              │
                        4 pare-feu
                              │
                     orchestration de conteneurs
                              │
                       maillage de services
                              │
                        12 microservices
                              │
                     2 fournisseurs cloud
```

❓ **Qu'est-ce qui justifie chacune de ces briques ?**

| Brique | Contrainte invoquée | Contrainte réelle |
|---|---|---|
| Deux centres de données | « Continuité » | **Quelle interruption est tolérable ? Personne ne l'a chiffrée** |
| Quatre pare-feu | « Sécurité » | Combien de frontières y a-t-il réellement à contrôler ? |
| Orchestration de conteneurs | « Modernité » | **Aucune** — une seule application, pas de variabilité de charge |
| Maillage de services | « Observabilité » | Aucune — douze services que rien n'obligeait à séparer |
| Douze microservices | « Agilité » | **Aucune** — une équipe, un cycle de livraison |
| Deux fournisseurs cloud | « Résilience » | **Deux plateformes à maîtriser au lieu d'une** |

⚠️ **Le diagnostic, et il est sévère** : cette architecture consomme probablement **cinq à huit exploitants** là où l'organisation en a **un**. Selon le §47.2, elle se dégradera en trois ans jusqu'au niveau réel de compétence disponible — **après avoir coûté le prix de l'ambition**.

**Ce qu'un lecteur exercé dit en réunion** :

> *« Je ne vois pas laquelle de ces briques répond à une contrainte chiffrée. Pouvez-vous me dire, pour chacune, quelle interruption ou quelle perte elle évite ? »*

**C'est la question du principe 9** — *ajouter n'est jamais gratuit* — appliquée à une architecture entière.

👁 **CE QU'IL FALLAIT OBSERVER, dans les deux cas**

| Architecture | L'erreur du lecteur débutant |
|---|---|
| **L'insuffisante** | Conclure « c'est mal fait » sans demander la taille, l'exposition et les moyens |
| **L'excessive** | Conclure « c'est bien fait » parce que les briques sont modernes |

> **Les deux erreurs sont la même** : juger l'architecture sans connaître la contrainte.

### 37.6 Les six architectures suivantes

Développées en annexe F, avec le même format :

| # | Architecture | Ce qu'elle enseigne |
|---|---|---|
| 5 | Haute disponibilité complète | Le coût de la symétrie, et ce qu'elle ne couvre pas |
| 6 | Multi-sites | L'autonomie locale, et ce qui manque pour l'obtenir |
| 7 | Hybride | Un point de fragilité récurrent — chapitre 40 |
| 8 | Industrielle | L'inversion des priorités — chapitre 28 |
| 9 | **Réelle et désordonnée** | Vingt ans de sédimentation, sans documentation |
| 10 | Le système complet d'HELIOMED | La synthèse du fil rouge |

⚠️ **La neuvième est la plus formatrice**, et c'est celle que vous rencontrerez en arrivant quelque part.

---

## Chapitre 38 — Les tiers sur un schéma

### 38.1 Ce qui n'est pas chez vous et vous concerne

| Type de tiers | Ce qu'il apporte | Ce qu'il vous coûte en maîtrise |
|---|---|---|
| **Service en ligne** | Une fonction sans infrastructure | Aucune visibilité, aucun contrôle de disponibilité |
| **Prestataire d'infogérance** | Des compétences et une astreinte | **Des accès d'administration à votre système** |
| **Partenaire connecté** | Un échange automatisé | Un chemin d'entrée dont vous ne maîtrisez pas l'extrémité |
| **Fournisseur de composants** | Du logiciel intégré à vos produits | Une exposition héritée |
| **Fournisseur d'identité externe** | Une authentification simplifiée | **Une dépendance de disponibilité hors de vos mains** |

### 38.2 Comment on les représente

🖼 **SCHÉMA 38.1 — Les trois façons de dessiner un tiers**

```
  A — LE NUAGE           [ ~~~ service ~~~ ]
      Ce qu'on ne détaille pas. Honnête, et peu informatif.

  B — LA BOÎTE NOIRE     ┌───────────────┐
                         │  fournisseur  │  ← on dessine l'interface,
                         └───────┬───────┘     pas l'intérieur
                                 │
                          protocole, sens,
                          authentification

  C — L'OMISSION         (rien)
      Le cas majoritaire. Le tiers n'est pas dessiné du tout.
```

**Le modèle B est le seul utile.** Il ne prétend pas décrire ce qu'on ne connaît pas, et il documente ce qui compte : **l'interface, le sens du flux, et la nature de l'authentification.**

### 38.3 Les trois questions à poser à tout tiers

```
1. Que peut-il atteindre chez nous ?
   → un flux entrant · un accès d'administration · rien

2. Que pouvons-nous faire s'il tombe ?
   → rien, dégradé, ou fonctionnement autonome

3. Comment s'authentifie-t-il, et qui peut révoquer cet accès ?
   → et surtout : quelqu'un le pourrait-il en urgence, un dimanche ?
```

**La troisième est celle qu'on ne pose jamais.** Un accès de prestataire créé en 2018 fonctionne encore en 2026, et personne ne sait qui a le pouvoir de le couper.

### 38.4 Le cas du prestataire d'infogérance

**L'un des tiers les plus puissants et les moins représentés**, et le §6.6 l'a annoncé.

| Ce qu'il possède | Conséquence |
|---|---|
| Des comptes d'administration sur vos serveurs | Une compromission chez lui devient une compromission chez vous |
| Des postes que vous ne maîtrisez pas | Hors de votre inventaire, hors de votre supervision |
| Un accès distant permanent | Un chemin d'entrée toujours ouvert |
| Une connaissance de votre architecture | Souvent supérieure à la vôtre |

⚠️ **Sur un schéma, il apparaît au mieux comme un nuage à côté du pare-feu.** Sa position réelle est **au cœur de la zone d'administration** — §27. **C'est l'un des écarts les plus importants entre l'architecture dessinée et l'architecture réelle en matière de sécurité.**

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Des compétences et une astreinte sans les recruter | **Des accès privilégiés hors de votre maîtrise** |
| Une capacité 24 heures sur 24 | Une dépendance contractuelle à la sécurité d'un tiers |
| Un coût prévisible | **Une surface d'attaque qui n'apparaît sur aucun schéma** |

🏭 **TROIS TAILLES** — Atelier Martin : un prestataire local, **avec un accès permanent et aucune traçabilité** — le risque le plus élevé de son architecture après le segment industriel. HELIOMED : un infogérant sur le parc bureautique et le support, accès via le rebond. Novaris : plusieurs prestataires, accès nominatifs, sessions enregistrées — **parce que la traçabilité individuelle est une exigence contractuelle de ses clients**.

---
