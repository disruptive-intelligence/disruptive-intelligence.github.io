---
title: Chapitre 48 — Quatre conceptions guidées
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE IX — Concevoir
  - index.md
---

> **Le vrai exercice de synthèse du cours.** Chaque cas suit dix étapes — et l'étape ④ est celle qui manque partout ailleurs.

## 48.0 Avertissement sur les chiffres de ce chapitre

⚠️ **Les valeurs employées dans les corrigés qui suivent — 0,3 personne, 0,6 personne, un coût multiplié par 2,5 — sont des données de scénario, pas des ratios universels.**

Elles servent à rendre un arbitrage lisible : *cette option consomme deux fois plus d'exploitation que celle-là*. **Elles ne se transposent pas.** La charge réelle d'exploitation d'un composant dépend de l'outillage, du niveau d'automatisation, des compétences en place, du nombre d'environnements et des engagements de service.

> **Ce qu'il faut retenir n'est pas le chiffre. C'est la démarche : chiffrer avant d'arbitrer, et confronter le total à la capacité réellement disponible.**

**Comment obtenir vos propres chiffres** : demandez à l'équipe d'exploitation combien de temps elle consacre par mois à un composant comparable déjà en service. C'est la seule source fiable, et elle est disponible en une conversation.

## 48.1 Le déroulé en dix étapes

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

## 48.2 Cas 1 — Une application interne pour 200 utilisateurs

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

## 48.3 Cas 2 — Un service exposé sur Internet

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

## 48.4 Cas 3 — Une extension cloud d'un existant

**Le besoin** : ajouter un service accessible depuis l'extérieur, en conservant les identités et une partie des données sur site.

**La question qui décide** : *que se passe-t-il si le lien tombe ?* — §40.3

| Option | Le lien tombe | Coût |
|---|---|---|
| **A — identités synchronisées** | Le cloud continue de fonctionner en autonomie | Une synchronisation à exploiter et superviser |
| **B — identités interrogées en direct** | **Le cloud devient inaccessible** | Plus simple, plus fragile |

**Retenu : l'option A**, avec une condition écrite au registre : **la synchronisation doit être supervisée**, faute de quoi son arrêt passera inaperçu jusqu'à ce que les mots de passe divergent — §40.2.

## 48.5 Cas 4 — Une reprise d'existant

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

## 48.6 Le capstone — une conception qui évolue

> **L'exercice principal de la Partie IX.** Une architecture ne se conçoit pas d'un coup : elle se corrige à chaque contrainte nouvelle. Voici comment.

### Version 0 — le besoin brut

> *Une organisation de 300 personnes veut publier un portail permettant à ses 600 clients de consulter leurs dossiers et de déposer des documents.*

**Rien d'autre.** Aucune contrainte chiffrée. C'est la situation réelle, et la première tâche est de le dire.

### Version 1 — votre première proposition

**Avant de lire la suite, dessinez.** Une page, dix minutes.

Une proposition raisonnable ressemble à ceci :

```
   Internet ──► [ pare-feu ] ──► [ mandataire ] ──► [ portail ] ──► [ base ]
```


**Quatre composants.** C'est proportionné à un besoin qu'on ne connaît pas encore.

---

### ⚡ ÉVÉNEMENT 1 — « L'entreprise exige 99,95 % de disponibilité »

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

### ⚡ ÉVÉNEMENT 2 — « Ce sont des données de santé »

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

### ⚡ ÉVÉNEMENT 3 — « Le budget est réduit de 30 % »

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

### ⚡ ÉVÉNEMENT 4 — « Il y aura deux sites »

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

### ⚡ ÉVÉNEMENT 5 — « L'équipe d'exploitation compte trois personnes »

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

### ⑩ La question finale

> ### Expliquez ce que vous avez volontairement décidé de ne pas faire.

**C'est le livrable qui distingue un concepteur d'un assembleur de briques.**

**Une réponse attendue ressemble à ceci** :

> *Nous avons renoncé au dépôt de documents en version 1, ce qui absorbe la contrainte budgétaire et supprime une part importante des obligations liées au stockage. Nous avons renoncé au second site, faute de capacité d'exploitation pour le maintenir en état de fonctionner — un second site non testé aurait donné une illusion de continuité. Nous avons renégocié l'engagement à 99,9 %, ce qui autorise une intervention humaine et divise par deux la complexité. Nous avons conservé le chiffrement de bout en bout et la journalisation applicative, qui ne sont pas négociables au regard des données traitées.*
>
> *Ce que nous n'avons pas pu vérifier : le délai réel de restauration de la base · la capacité du lien Internet à absorber le volume · si l'équipe sait exploiter un magasin de sessions.*

⚠️ **Remarquez ce que cette réponse contient** : quatre renoncements motivés, deux non-négociables, et trois incertitudes déclarées. **Aucune ligne ne décrit un composant.**

### Les cinq enseignements du capstone

| # | Enseignement |
|---|---|
| **1** | Une contrainte non chiffrée ne se conçoit pas — **elle se demande** |
| **2** | Un engagement de disponibilité se traduit en **minutes par mois**, et cela change tout |
| **3** | Une contrainte nouvelle ne s'ajoute pas : **elle oblige à en dégrader une autre** |
| **4** | **Renoncer à une fonctionnalité est un arbitrage légitime**, et souvent le moins cher |
| **5** | **La capacité d'exploitation est la contrainte qui décide**, et elle arrive toujours en dernier |

## 48.7 🔬 Mini-labs 11 et 12

**🔬 Mini-lab 11 — Concevoir pour trois organisations** · *45 min · 🟠*
Même besoin — publier un service de suivi pour des clients — chez Atelier Martin, HELIOMED et Novaris. Produire trois architectures différentes, et **justifier chaque écart par une contrainte, jamais par la taille** — *principe de la contrainte*.

**🔬 Mini-lab 12 — Le registre des compromis** · *30 min · 🟠*
À partir d'une architecture fournie, reconstituer le registre des compromis qui l'a produite : quelle contrainte a été privilégiée à chaque endroit, laquelle a été dégradée, et ce qui devrait déclencher un réexamen.

---
