---
title: Chapitre 43 — Où peut-on agir ?
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VIII — La vue cybersécurité
  - index.md
---

## 43.1 Les cinq actions

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

## 43.2 Où chaque action est possible

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

## 43.3 Les points de passage d'une architecture type

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

## 43.4 Ce qui rend une action impossible, par cause

**Quatre causes, et elles n'appellent pas les mêmes réponses** :

| Cause | Exemple | Que faire |
|---|---|---|
| **Architecturale** | Pas de point de passage entre deux machines d'un segment | **Changer l'architecture**, ou déclarer non couvert |
| **Technique** | Le composant ne sait pas produire de journal | Observer ailleurs sur le chemin |
| **Contractuelle** | Un service en ligne ne donne pas accès à ses journaux | Négocier, ou accepter et déclarer |
| **Organisationnelle** | Le composant est administré par une autre équipe | **La plus fréquente, et la seule qui se résolve sans budget** |

⚠️ **La quatrième mérite d'être nommée** : beaucoup d'angles morts ne sont ni techniques ni budgétaires. **Ils existent parce que personne n'a demandé.** C'est le cas des journaux d'un équipement réseau, d'un progiciel métier, ou d'un service géré par une filiale.

## 43.5 Le coût de chaque action

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
