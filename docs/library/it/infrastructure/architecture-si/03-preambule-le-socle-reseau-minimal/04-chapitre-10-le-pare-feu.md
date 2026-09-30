---
title: Chapitre 10 — Le pare-feu
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

> **Le composant le plus dessiné du cours, et celui dont le schéma dit le moins.**

## 10.1 À quoi ça sert

Autoriser ou refuser un flux entre deux zones, selon des règles.

**Pourquoi ça existe.** Un routeur fait passer tout ce qui est routable. Dès qu'on veut que certaines choses passent et d'autres non, il faut un composant qui décide — et qui garde une trace de sa décision.

## 10.2 Comment il fonctionne, juste assez pour raisonner

**Trois générations coexistent**, et elles ne voient pas la même chose :

| Génération | Ce qu'elle examine | Ce qu'elle ne voit pas |
|---|---|---|
| **Filtrage simple** | Adresses, ports, sens | Si le flux correspond vraiment au service annoncé |
| **Suivi d'état** | Les mêmes, **plus l'état de la connexion** | Le contenu |
| **Inspection applicative** | Le contenu, si le flux n'est pas chiffré **ou s'il est déchiffré** | Ce qui reste chiffré de bout en bout |

> **La notion la plus utile : le suivi d'état.** Un pare-feu qui suit l'état sait qu'une réponse appartient à une connexion qu'il a déjà autorisée. **C'est pourquoi autoriser un flux sortant ne signifie pas autoriser un flux entrant** — §P.3.

🖼 **SCHÉMA 10.1 — Ce que le suivi d'état change**

```
  SANS SUIVI D'ÉTAT
     règle 1 : autoriser interne → Internet, port 443
     règle 2 : autoriser Internet → interne, ports 1024-65535
                                    ▲
                        il faut ouvrir le retour EN GRAND

  AVEC SUIVI D'ÉTAT
     règle 1 : autoriser interne → Internet, port 443
     (les réponses reviennent automatiquement)
                                    ▲
                        aucune règle entrante nécessaire
```


⚠️ **Ce que cela explique en lecture** : un jeu de règles qui autorise de larges plages entrantes signale souvent un équipement ancien, ou une configuration héritée d'une époque où le suivi d'état n'existait pas. **C'est un signe de strate** — §4.2.

## 10.3 Le même composant, trois placements différents

**C'est en variant le placement qu'on comprend la fonction.**

```
  A — PARE-FEU UNIQUE, EN COUPURE
      Internet ──► [ FW ] ──► serveur
      → une seule frontière · le serveur est derrière un filtre
      → contourné ou compromis : plus rien ne protège

  B — DEUX PARE-FEU, ZONE INTERMÉDIAIRE
      Internet ──► [ FW-1 ] ──► DMZ ──► [ FW-2 ] ──► interne
      → deux frontières · un composant compromis en DMZ ne suffit pas
      → deux jeux de règles à maintenir, souvent deux constructeurs

  C — SERVICE EN LIGNE ET LIEN PRIVÉ
      Internet ──► [ service du fournisseur ]
                            │  lien privé
                            ▼
                     [ réseau interne ]
      → la frontière côté Internet ne vous appartient plus
      → le pare-feu ne protège plus que le lien privé
```


| Placement | Ce que le pare-feu protège | Ce qu'il ne protège pas |
|---|---|---|
| **A** | Le serveur, contre l'extérieur | Rien à l'intérieur · rien s'il est contourné |
| **B** | L'interne, même si la DMZ tombe | Les échanges au sein de chaque zone |
| **C** | Le lien privé | **Tout ce qui se passe côté fournisseur** |

**Les six questions à poser devant tout pare-feu sur un schéma** :

```
1. Quelle frontière matérialise-t-il exactement ?
2. Qu'est-ce qui le contourne ? (un lien direct, une machine à deux interfaces)
3. Combien de règles, et depuis quand ont-elles été revues ?
4. Qui l'administre, et depuis où ?  ← §27
5. Que se passe-t-il s'il tombe ?
6. Que signifie « paire redondée » ici ?  ← §10.5
```


⚠️ **La question 3 est celle qui révèle le plus.** Un pare-feu dont les règles n'ont pas été revues depuis six ans autorise probablement des flux dont personne ne connaît plus l'usage. **Une règle ne se supprime jamais spontanément** — chaque projet en ajoute, aucun n'en retire.

## 10.4 Ce qu'il fait à la donnée

Selon sa génération : il regarde les extrémités et les ports, ou il inspecte le contenu applicatif, ou il déchiffre pour inspecter — auquel cas **il voit tout en clair**, ce qui en fait un actif extrêmement sensible.

## 10.5 « Paire redondée » : ce que cela signifie réellement

**Deux pare-feu côte à côte sur un schéma peuvent décrire trois choses différentes.**

| Mode | Comportement | Ce que ça protège |
|---|---|---|
| **Actif / passif** | Le second attend. Il prend le relais si le premier tombe | Une panne matérielle · **pas une erreur de configuration, qui est répliquée** |
| **Actif / actif** | Les deux traitent du trafic | Une panne matérielle, et la charge |
| **En série** | Deux barrières successives, souvent de constructeurs différents | Une faille propre à un constructeur |

⚠️ **Principe de preuve, appliqué au pare-feu** — ce qu'une paire ne protège pas :

| Ce qui reste partagé | Conséquence |
|---|---|
| **La configuration** | Une règle erronée est répliquée sur les deux |
| **La version logicielle** | Une vulnérabilité les affecte tous les deux |
| **L'alimentation, la baie, le site** | Un incident physique les emporte ensemble |
| **L'administrateur** | Une erreur humaine s'applique aux deux |

> **Une paire redondée protège contre la panne d'un équipement. Elle ne protège contre à peu près rien d'autre.**

## 10.6 S'il disparaît

**Trois cas opposés, et c'est ce qui rend ce composant intéressant** :

| Configuration | S'il tombe | Ce que ça révèle |
|---|---|---|
| En coupure, sans contournement | **Plus rien ne passe.** Le service s'arrête | La frontière était réelle |
| En redondance | Le second prend le relais | Si la bascule fonctionne — *principe de preuve* |
| **Contourné par un chemin oublié** | **Rien ne change** | **La frontière était fictive** |

🔥 **SCÉNARIO — le pare-feu tombe et rien ne se passe**

| Question | Réponse |
|---|---|
| Symptôme | Un pare-feu est arrêté pour maintenance. **Aucun utilisateur ne signale quoi que ce soit** |
| Hypothèse naïve | « La bascule a fonctionné » |
| Dépendance réelle | **Peut-être aucune** : le trafic passait peut-être déjà ailleurs |
| Ce que le schéma aurait dû montrer | Tous les chemins entre les deux zones, pas seulement celui-ci |
| Ce qu'il faut vérifier | Le compteur de sessions du pare-feu passif : **a-t-il vraiment repris le trafic ?** |

⚠️ **C'est l'un des tests les plus instructifs qu'on puisse faire sur une architecture** : arrêter un composant en fenêtre planifiée et regarder si quelque chose change. Quand rien ne change, ce n'est pas toujours une bonne nouvelle.

## 10.7 Sur un schéma

Presque toujours dessiné, presque toujours à une frontière. **Deux pare-feu côte à côte** signalent une redondance ; **deux pare-feu en série** signalent une double barrière.

⚠️ **Le piège de lecture le plus fréquent du cours** : un pare-feu dessiné ne dit rien de ses règles. Une frontière peut être matérialisée par un équipement dont la règle est *« tout autoriser »*.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans la DMZ » | Le composant est publié | **Y a-t-il une seconde frontière ?** — §25.1 |
| « On a une paire HA » | Deux pare-feu redondés | Actif/passif ou actif/actif ? La bascule a-t-elle été testée ? |
| « Le flux est ouvert » | Une règle autorise ce trafic | Dans quel sens ? Depuis quand ? Qui l'a demandée ? |
| « On va mettre une règle any-any en attendant » | Autoriser tout, temporairement | **« En attendant » dure en moyenne plusieurs années** — §4.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Contrôler ce qui traverse une frontière | **Un ensemble de règles qui ne fait que croître** |
| Tracer les flux refusés | Un volume de journaux considérable |
| Inspecter le contenu | Une latence · un déchiffrement à opérer · **un point où tout passe en clair** |
| Redonder | Deux équipements, et une bascule à tester — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : un boîtier tout-en-un qui fait routeur, pare-feu et accès distant. HELIOMED : deux en redondance. Novaris : plusieurs dizaines. **La contrainte qui les multiplie est le nombre de frontières à contrôler, pas la taille.**

---
