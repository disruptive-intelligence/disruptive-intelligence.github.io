---
title: Chapitre 28 — Le réseau industriel
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE IV — Les réseaux et les zones
  - index.md
---

> **Où les règles s'inversent.** Le second chapitre décisif de la partie.

## 28.1 L'inversion des priorités

| | Système de gestion | Système industriel |
|---|---|---|
| Priorité 1 | **Confidentialité** | **Disponibilité et sûreté** |
| Priorité 2 | Intégrité | Intégrité |
| Priorité 3 | Disponibilité | Confidentialité |
| Cycle de vie d'un équipement | 3 à 6 ans | **15 à 30 ans** |
| Fenêtre d'arrêt | Nuits, week-ends | **Arrêts de production planifiés à l'année** |
| Correctif | Appliqué selon un processus | **Validé par le constructeur, ou interdit** |
| Conséquence d'une erreur | Perte de données, indisponibilité | **Atteinte à la sécurité des personnes** |
| Qui décide | La direction des systèmes d'information | **La production, et parfois un organisme certificateur** |

> **Ce n'est pas que l'industriel soit « en retard ».** Ses contraintes sont différentes, et elles sont plus fortes. Un système qui pilote une machine ne peut pas redémarrer parce qu'un correctif l'exige.

⚠️ **La dernière ligne est celle qu'on oublie et qui bloque tous les projets** : modifier un système industriel peut invalider une certification, une garantie constructeur, ou une homologation de sûreté. **Ce n'est pas une question de volonté.**

## 28.2 Ce qu'on y trouve

| Composant | Ce qu'il fait | Ce qui le caractérise |
|---|---|---|
| **Automate** | Pilote une machine ou un processus | Ancien, peu de mémoire, **souvent sans authentification** |
| **Poste de supervision** | Affiche et commande | Un système ancien, **figé par le constructeur** |
| **Historisation** | Enregistre les mesures | Souvent le point de contact avec le monde de gestion |
| **Poste d'ingénierie** | Programme les automates | **Le composant le plus sensible** — il peut modifier le programme |
| **Passerelle** | Fait communiquer les deux mondes | Le point le plus exposé |

⚠️ **Le poste d'ingénierie mérite une attention particulière.** Il détient les programmes des automates, souvent les seuls exemplaires. **Sa compromission permet de modifier ce qu'une machine fait physiquement** — et sa perte peut rendre un automate impossible à reprogrammer.

## 28.3 Pourquoi l'authentification y est souvent absente

**Ce n'est pas une négligence, et c'est important à comprendre pour ne pas juger** :

| Raison | Explication |
|---|---|
| **L'ancienneté** | Un automate de 2004 ne connaît pas la notion d'authentification |
| **La sûreté** | En cas d'urgence, un opérateur doit pouvoir agir **sans délai** |
| **La disponibilité** | Un mécanisme d'authentification est un composant de plus qui peut tomber |
| **L'isolement supposé** | Le réseau était censé être séparé — et il l'était, en 2004 |

> **La sécurité de ces systèmes reposait sur l'isolement physique. C'est cet isolement qui a disparu**, pas la conception qui était mauvaise.

## 28.4 La frontière entre les deux mondes

🖼 **SCHÉMA 28.1 — Les trois modèles de frontière**

```
  MODÈLE A — séparation totale
     [ gestion ]        [ industriel ]
     Aucun lien. Les données transitent par support amovible.
     → sûr, contraignant, de moins en moins praticable
     → ⚠️ le support amovible devient lui-même le vecteur

  MODÈLE B — passerelle unidirectionnelle
     [ gestion ] ◄──── [ historisation ] ◄──── [ industriel ]
     Les données remontent, rien ne descend.
     → le modèle de référence
     → ⚠️ suppose que RIEN n'ait besoin de descendre — vérifier

  MODÈLE C — lien filtré bidirectionnel
     [ gestion ] ◄───► [ pare-feu ] ◄───► [ industriel ]
     → le plus répandu en pratique, et le plus exposé
     → ⚠️ chaque règle ajoutée réduit la séparation
```


⚠️ **Le lien du §4.6 chez HELIOMED relève du modèle C**, créé en 2018 pour un export vers le contrôle de gestion, jamais reconsidéré. **La question de lecture devant toute passerelle industrielle** : *dans quel sens circule-t-elle, et qui l'a décidé quand ?*

## 28.5 Les quatre chemins qui traversent malgré la séparation

**Même en modèle A, quatre chemins existent souvent** — et aucun n'est dessiné :

| Chemin | Pourquoi il existe | Ce qu'il permet |
|---|---|---|
| **Le poste d'ingénierie** | Il est parfois connecté aux deux mondes | Un pont direct |
| **La télémaintenance constructeur** | Contractuelle, souvent permanente | **Un accès distant d'un tiers** |
| **Le support amovible** | Transferts de programmes et de données | Le vecteur classique |
| **Le poste portable d'un intervenant** | Il se branche sur les deux réseaux, à des moments différents | Un pont différé |

⚠️ **La deuxième ligne est celle qui inquiète le plus en audit.** Une télémaintenance constructeur donne un accès distant permanent à un système de production, souvent créé il y a dix ans, rarement révisé, et **presque jamais dessiné**.

🔥 **SCÉNARIO — la production s'arrête après une mise à jour bureautique**

| Question | Réponse |
|---|---|
| Symptôme | Une ligne de production s'arrête. Aucune intervention sur le réseau industriel |
| Hypothèse naïve | « Une panne mécanique » |
| Dépendance réelle | **Le poste de supervision dépend d'un service du réseau bureautique** — annuaire, résolution, licence |
| Ce que le schéma aurait dû montrer | Les dépendances du réseau industriel **vers** le réseau de gestion |
| Concevoir différemment | Rendre le réseau industriel autonome pour ses dépendances — §26.2 |

⚠️ **C'est le scénario qui justifie la séparation mieux que n'importe quel argument de sécurité** : une dépendance non maîtrisée du monde industriel vers le monde de gestion **transforme un incident bureautique en arrêt de production**.

## 28.6 Ce qu'on peut faire, et ce qu'on ne peut pas

| Action | Sur un réseau de gestion | Sur un réseau industriel |
|---|---|---|
| **Corriger** | Selon un processus | **Validé par le constructeur, ou interdit** |
| **Installer un agent** | Oui | **Non** — ressources, garantie, certification |
| **Scanner activement** | Oui | **Non** — un balayage peut arrêter un automate |
| **Observer passivement** | Oui | **Oui** — c'est la méthode de référence |
| **Segmenter** | Oui | **Oui, et c'est la mesure principale** |
| **Journaliser** | Oui | Partiellement — beaucoup d'équipements ne produisent rien |

⚠️ **La ligne du scan actif n'est pas une précaution excessive** : certains automates anciens cessent de fonctionner face à un trafic qu'ils n'attendent pas. **C'est un cas où un outil de sécurité peut provoquer l'incident qu'il devait prévenir.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est isolé » | Le réseau industriel est séparé | **Les quatre chemins du §28.5 existent-ils ?** |
| « On ne peut pas patcher » | Le constructeur ne valide pas | **Est-ce vérifié, ou supposé ?** Parfois la validation existe |
| « Le constructeur a un accès » | Télémaintenance | **Permanent ou à la demande ? Tracé ? Depuis quand ?** |
| « On a mis une DMZ industrielle » | Une zone intermédiaire | **Quel modèle — A, B ou C ?** Le sens des flux décide de tout |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Remonter des données de production vers la gestion | **Un chemin vers le monde industriel** |
| Superviser à distance | Un accès distant à protéger particulièrement |
| Séparer totalement | Des transferts manuels, lents, **eux-mêmes risqués** |
| Rendre l'industriel autonome | Des composants dupliqués — résolution, annuaire, temps |

🏭 **TROIS TAILLES** — Atelier Martin : deux machines à commande numérique, **sur le même segment que la bureautique** — et c'est le risque le plus élevé de son architecture, non identifié comme tel. HELIOMED : segment séparé à Saint-Étienne, avec le lien de 2018. Novaris : sans objet — pas d'activité industrielle.

⚠️ **La ligne Atelier Martin est la plus instructive de tout le tableau des trois tailles.** Une petite organisation n'échappe pas à la contrainte industrielle : **elle l'ignore**. L'absence de segmentation n'est pas un arbitrage quand personne n'a posé la question.

---

## 🔬 Mini-lab 7 — Tracer les zones sur un schéma qui n'en montre aucune

**Objectif** — Reconstituer un découpage en zones à partir des seuls composants et flux.
**Durée** 35 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 24 à 28

**Le schéma fourni** — aucune zone n'est représentée :

```
   Internet ─── [ P1 ] ─── [ P2 ] ─── [ S1 ] ─── [ S2 ] ─── [ S3 ]
                              │                     │
                           [ S4 ]                [ S5 ]
                              │
                        [ 400 postes ]
                              │
                           [ S6 ] ─── [ S7 ] ─── [ automates ]

   P1 : filtre les flux entrants          S4 : annuaire
   P2 : reçoit du 443, émet du 8080       S5 : base de données
   S1 : serveur web                       S6 : poste de supervision
   S2 : serveur applicatif                S7 : passerelle
   S3 : serveur de fichiers
```


❓ **Questions**

1. Combien de zones distinguez-vous, et où passent les frontières ?
2. Quels composants sont mal placés ?
3. Que manque-t-il ?

---

**Corrigé**

**1. Cinq zones**

| Zone | Composants | Frontière |
|---|---|---|
| Extérieur | Internet | — |
| Bordure | **P1** | Entre Internet et la DMZ |
| Zone démilitarisée | **P2** | **Frontière 2 non représentée** — §25.1 |
| Interne | S1, S2, S3, S4, S5, les 400 postes | — |
| Industriel | S6, S7, automates | Aucun équipement de filtrage entre l'interne et S6 |

**2. Trois anomalies de placement**

| Anomalie | Pourquoi c'est grave |
|---|---|
| **Aucune frontière entre la DMZ et l'interne** | P2 compromis atteint directement S1, puis tout le reste — §25.2 |
| **S6 est joignable depuis le segment des 400 postes** | Un poste compromis atteint la supervision industrielle **sans traverser aucun filtre** |
| **S4 (annuaire) dans le même segment que 400 postes** | Il devrait être dans un segment serveurs distinct |

**3. Ce qui manque** — au moins six éléments :

| Manquant | Effet |
|---|---|
| **Résolution de noms** | Sans elle, aucun de ces flux |
| **Réseau d'administration** | Comment administre-t-on ces sept serveurs ? Depuis les 400 postes ? |
| Sauvegarde | Aucun composant, alors que S5 contient les données |
| Les segments internes | 400 postes et 5 serveurs dans une même zone : sont-ils dans le même segment ? |
| Les sens de flux | Aucun trait n'est fléché |
| **Le sens de la passerelle S7** | Modèle B ou C ? La réponse change tout — §28.3 |

**Les trois erreurs attendues**

1. **Compter quatre zones** en oubliant la bordure. P1 et P2 ne jouent pas le même rôle.
2. **Ne pas relever l'absence de frontière 2.** C'est l'anomalie la plus discrète du dossier, et la plus lourde : rien ne la signale, seule son absence la trahit.
3. **Traiter le lien vers S6 comme normal** parce qu'il est dessiné. Un trait indique une possibilité, pas une autorisation — §3.2.

---

> ### 🎓 À ce stade de la Partie IV, vous savez…
>
> ✓ qu'un **pare-feu entre deux zones ne protège en rien des échanges à l'intérieur** de chaque zone ;
> ✓ qu'une **segmentation contournée protège moins qu'une segmentation absente** ;
> ✓ que la zone démilitarisée se définit par sa **seconde frontière**, celle qu'on oublie de dessiner ;
> ✓ que la question à poser à un site distant est : **qu'est-ce qui survit si le lien tombe** — et que personne ne le sait, faute d'avoir essayé ;
> ✓ que le **chemin d'administration est plus puissant que ce qu'il administre**, et qu'il n'est jamais dessiné — souvent pour de mauvaises raisons ;
> ✓ qu'un **rebond joignable depuis un poste bureautique ajoute une étape, pas une frontière** ;
> ✓ que dans le monde **industriel les priorités s'inversent**, et que ce n'est pas un retard mais une contrainte plus forte ;
> ✓ qu'une **absence de segmentation n'est pas un arbitrage quand personne n'a posé la question** ;
> ✓ que le **sans-fil peut être une porte directe sur le segment interne**, et que deux réseaux annoncés ne sont pas deux segments.
>
> **Ce que vous ne savez pas encore** : ce qui circule réellement dans tout cela, par quels chemins, et pourquoi certains chemins ne sont jamais dessinés. C'est l'objet de la Partie V — le cœur du cours.

---
