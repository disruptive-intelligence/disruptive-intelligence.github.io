---
title: Chapitre 46 — Les quatre questions du concepteur
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE IX — Concevoir
  - index.md
---

## 46.1 La symétrie

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

## 46.2 ① Que doit-on servir, à qui ?

**La question qu'on saute**, et dont l'absence produit les architectures les plus coûteuses.

| Sous-question | Pourquoi elle compte |
|---|---|
| **Quel service métier ?** | Formulé du point de vue de l'utilisateur, pas de la technique — §35.1 |
| **Combien d'utilisateurs, où ?** | 40 sur un site et 4 000 sur trois continents ne produisent pas la même architecture |
| **Quels usages, à quels moments ?** | Charge continue ou pics · heures ouvrées ou permanent |
| **Quelles données, de quelle sensibilité ?** | **Principe 6** — c'est la donnée qui commande |
| **Qui exploitera ?** | Une personne à mi-temps ou une équipe de vingt |

⚠️ **La dernière est la plus négligée et la plus déterminante.** Une architecture qui exige davantage de compétences que l'organisation n'en possède **échouera**, quelle que soit sa qualité technique. C'est le facteur qui explique le plus d'échecs de modernisation.

## 46.3 ② Quelles contraintes s'imposent ?

Les six contraintes du §1.4, appliquées au cas.

### Le vocabulaire professionnel : les exigences non fonctionnelles

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

### Les trois durées, et pourquoi il ne faut pas les confondre

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

## 46.4 ③ Qu'accepte-t-on de perdre ?

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

## 46.5 ④ Quels compromis assume-t-on, et les a-t-on écrits ?

**La différence entre un compromis assumé et un compromis subi** est qu'il est écrit.

🧪 **EN PRATIQUE — le registre des compromis**

| # | Compromis | Contrainte privilégiée | Contrainte dégradée | Conséquence acceptée | Décideur | Revoir si |
|---|---|---|---|---|---|---|
| 1 | Un seul serveur applicatif | Coût | Disponibilité | Interruption de 4 h possible | *(nom)* | Le coût de licence change |
| 2 | Pas de zone démilitarisée | Simplicité | Sécurité | Publication directe, aucun service publié aujourd'hui | *(nom)* | Un service devient public |

**Ce document est le vrai livrable d'une conception.** Le schéma montre le résultat ; le registre montre **pourquoi**, et c'est lui qui permettra, dans dix ans, de répondre à la question du chapitre 4 : *pourquoi c'est comme ça ?*

> **Une architecture livrée sans registre de compromis condamne ses successeurs à les redécouvrir — ou à les juger naïvement.**

---
