---
title: Chapitre 36 — La grille de lecture en sept passes
source: IT/Architecture_SI.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VI — Lire une architecture
  - index.md
---

## 36.1 Pourquoi une méthode plutôt qu'un œil

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

## 36.2 Les sept passes, en détail

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

## 36.3 Une lecture entièrement déroulée

**La méthode ne s'apprend pas en la lisant.** Voici les sept passes appliquées de bout en bout au schéma 1.1, telles qu'un lecteur exercé les conduirait — avec ses hésitations.

### Passe ① — Les zones

*« Je compte trois zones dessinées : la DMZ, l'interne, l'industriel. Plus l'extérieur, implicite, et la bordure — les deux pare-feu. Cela fait cinq. »*

*« La frontière 1 est matérialisée : deux pare-feu. La frontière 2, entre DMZ et interne, **n'est pas dessinée**. Soit elle existe et n'est pas représentée, soit elle n'existe pas. C'est ma première question. »*

*« Le site industriel n'a qu'un lien. Par quoi passe-t-il ? Rien ne l'indique. Deuxième question. »*

**Constat de passe** : 5 zones · 1 frontière matérialisée sur 3 · 2 questions.

### Passe ② — L'entrée

*« Utilisateur externe : Internet → pare-feu → mandataire. Clair. »*

*« Utilisateur interne : **rien n'est dessiné**. Les postes n'apparaissent pas. Or c'est de là que part la majorité des flux — §6.1. Et selon ce que répond la résolution interne, ils atteignent peut-être le serveur web directement, sans passer par le mandataire — §14.5. Troisième question. »*

*« Administrateur : **aucun chemin**. Quatrième question, et c'est celle qui compte le plus — §27.5. »*

**Constat de passe** : 1 entrée sur 3 dessinée.

### Passe ③ — Les données

*« Une base est dessinée. Un serveur de fichiers aussi. Une sauvegarde. »*

*« Mais où sont les copies ? Réplicas ? Environnement de recette ? Exports ? Rapports ? **Rien** — §32.2. Cinquième question. »*

*« Et le chemin de la sauvegarde n'est pas dessiné : elle atteint la base, mais par où, et avec quel compte ? Sixième question — §21.4. »*

**Constat de passe** : 3 emplacements dessinés · nombre réel inconnu.

### Passe ④ — L'identité

*« L'annuaire est dessiné. **Aucun trait ne s'y connecte.** C'est le cas canonique : tout s'y connecte, rien ne le montre — §1.1. »*

*« Combien de contrôleurs ? Un seul est dessiné. Si c'est le seul, c'est un point de rupture majeur. **Et même s'il y en a deux : sur des hôtes différents ?** — *principe de preuve*, §16.4. Septième question. »*

*« Où s'authentifie-t-on ? Sur le mandataire, ou dans l'application ? La réponse change ce qu'un poste interne traverse. Huitième question — §30.5. »*

**Constat de passe** : 1 composant dessiné, 0 relation, 2 questions.

### Passe ⑤ — Les flux

*« Je suis une requête externe : douze étapes, cinq visibles — §29.1. »*

*« Je suis une requête interne : le chemin est plus court, et il ne traverse pas le mandataire. **Aucun des contrôles du mandataire ne s'y applique.** »*

*« Je suis une authentification : poste → annuaire. Non dessiné. »*

*« Je suis un journal : chaque composant → collecte. **La collecte n'est pas sur le schéma.** »*

**Constat de passe** : sur 4 flux suivis, 1 est partiellement dessiné.

### Passe ⑥ — Les ruptures

*« Composants uniques dessinés : l'applicatif, la base, le mandataire — s'il est seul, ce que le schéma ne dit pas. »*

*« Composants uniques **non dessinés** : la résolution de noms, l'annuaire, les certificats. »*

*« Redondance apparente : trois serveurs web. **Sur des hôtes différents ? Où vivent les sessions ?** Sans réponse, je ne peux pas conclure — *principe de preuve*, §31.2. Neuvième et dixième questions. »*

**Constat de passe** : 3 ruptures visibles · 3 invisibles · 1 redondance non vérifiable.

### Passe ⑦ — L'invisible

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

### Le rendu, en une page

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

## 36.4 Le rendu d'une lecture

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
