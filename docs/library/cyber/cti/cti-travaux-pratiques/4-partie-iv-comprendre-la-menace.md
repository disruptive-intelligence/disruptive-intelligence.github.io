---
title: PARTIE IV — Comprendre la menace
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
chapter: 4
chapters: 8
---

> **Où nous sommes dans la boucle analytique** : nous alimentons le segment ③ **ANALYSE**. Ces quatre chapitres ne sont pas un catalogue de connaissances : ce sont des **grilles de lecture**, destinées à être appliquées à un cas que vous rencontrerez et qui ne figurera dans aucun de ces chapitres.
>
> **Ce que cette partie ne fera pas** : vous apprendre des noms d'acteurs, décrire des maliciels, ou faire l'inventaire des techniques d'attaque. Ces contenus existent, ils se périment vite, et ils sont disponibles ailleurs.

---

## Chapitre 16 — Pourquoi certaines attaques existent

> Chapitre volontairement resserré. **Objectif unique** : comprendre les incitations qui expliquent les priorités adverses, parce qu'un analyste qui les ignore prédit mal et priorise mal.

### 16.1 Le modèle économique comme grille de lecture

**Le principe** : la plupart des attaques ne sont pas des exploits techniques, ce sont des **opérations** — avec des coûts, des délais, une rentabilité attendue et des contraintes de ressources.

**Ce que cette grille explique immédiatement**, et qui reste opaque sans elle :

| Observation courante | Explication économique |
|---|---|
| Une vulnérabilité critique reste inexploitée pendant des mois | Son exploitation coûte cher et le gain est incertain |
| Une vulnérabilité moyenne est exploitée massivement en 48 h | Elle est triviale à automatiser sur un produit très déployé |
| Les mêmes techniques banales reviennent depuis dix ans | Elles fonctionnent, et rien n'incite à en changer |
| Un attaquant abandonne après trois échecs | La cible suivante coûte moins cher |
| Les campagnes s'intensifient à certaines périodes | Congés, effectifs réduits, délais de réaction allongés |

**La formulation qui résume le chapitre** :

> **Un adversaire rationnel ne choisit pas la cible la plus intéressante. Il choisit celle dont le rapport entre le gain espéré et le coût d'accès est le plus favorable.**

⚠️ Le mot *rationnel* est important, et il ne signifie pas *intelligent*. Il signifie que l'acteur poursuit un objectif et arbitre ses moyens. Les acteurs non rationnels existent — vandalisme, action politique symbolique, erreur — et ils échappent à cette grille. Elle n'explique donc pas tout ; elle explique la majorité.

### 16.2 La spécialisation des rôles

Une page, pas davantage. L'essentiel tient dans le fait que **la chaîne d'attaque est fragmentée**, ce qui a trois conséquences analytiques.

| Rôle | Ce qu'il produit | Ce qu'il vend |
|---|---|---|
| **Développeur d'outillage** | Le code, l'infrastructure technique | Un produit ou une location |
| **Courtier d'accès** | Un accès initial à une organisation | L'accès, sans l'exploiter lui-même |
| **Opérateur** | La conduite de l'opération dans le réseau | Le résultat |
| **Prestataire de service** | Négociation, blanchiment, hébergement | Un service d'appoint |

**Les trois conséquences pour l'analyste** :

1. **L'entrée et l'exploitation peuvent être séparées de plusieurs mois.** Un accès obtenu en janvier peut être revendu et exploité en juin. Une intrusion détectée n'est pas nécessairement récente, et le vecteur d'entrée peut avoir été refermé depuis longtemps par un correctif appliqué entre-temps.
2. **Le mode opératoire n'identifie pas un acteur unique.** Le même outil, la même infrastructure et la même technique peuvent servir plusieurs opérateurs indépendants. C'est le §13.3.
3. **La cible n'a pas toujours été choisie.** Un courtier collecte des accès opportunistement, puis les propose. Beaucoup d'organisations attaquées n'ont jamais été « ciblées » — elles ont été **disponibles**.

**Le troisième point est celui qui change le plus de raisonnements.** La question « pourquoi nous ? » n'a souvent pas de réponse individuelle.

### 16.3 Structure de coût d'une attaque

Ce qui coûte à un adversaire, par ordre décroissant :

| Poste | Coût relatif | Ce qui le fait baisser |
|---|---|---|
| **Obtenir un accès initial** | Élevé | Une vulnérabilité automatisable, des identifiants en fuite, un utilisateur qui clique |
| **Progresser dans le réseau** | Moyen | Une segmentation absente, des identifiants réutilisés, des droits excessifs |
| **Rester non détecté** | Variable | Une journalisation absente, une détection non couverte |
| **Monétiser** | Élevé | Un écosystème de services, une victime qui paie vite |
| **Développer un outillage propre** | **Très élevé** | Réutiliser ce qui existe — et c'est ce qui est fait dans la majorité des cas |

**Ce que cette structure implique pour la défense**, et c'est la vraie utilité du chapitre :

> **Chaque mesure qui augmente le coût d'une étape déplace l'attaquant vers une autre cible — ou vers une autre étape.**

Une authentification multifacteur ne rend pas l'accès impossible : elle le rend cher. Face à mille cibles équivalentes, un adversaire opportuniste ira vers les neuf cent quatre-vingts qui n'en ont pas.

📌 **La limite de ce raisonnement** : il vaut pour l'opportunisme, pas pour le ciblage. Un adversaire déterminé sur une cible précise absorbera le surcoût. La question à se poser est donc : *sommes-nous une cible parmi mille, ou une cible en particulier ?* Elle est traitée au chapitre 17.

### 16.4 Ce qui fait d'une organisation une cible

Trois facteurs, indépendants, à évaluer séparément.

| Facteur | Question | Ce qui l'augmente |
|---|---|---|
| **Valeur** | Que peut-on tirer de nous ? | Données monnayables · capacité de paiement · position dans une chaîne · notoriété · continuité critique |
| **Accessibilité** | Combien coûte l'accès ? | Surface exposée · défenses connues comme faibles · dépendance à des tiers vulnérables |
| **Visibilité** | Nous voit-on ? | Publications · appels d'offres · communication · position sectorielle · présence dans des listes publiques |

**Le facteur le plus mal évalué est le troisième.** Beaucoup d'organisations se croient discrètes et sont parfaitement identifiables — par leurs certificats publics, leurs offres d'emploi, leurs clients qui les citent, ou leur adhésion à une fédération professionnelle. C'est l'objet du chapitre 34.

🧪 **EN PRATIQUE — l'auto-évaluation en dix minutes**

| Question | Notre réponse |
|---|---|
| Quelles données avons-nous qui se revendent ? | |
| Pourrions-nous payer une rançon rapidement ? | |
| Un arrêt de combien de temps devient-il insoutenable ? | |
| Combien de nos clients dépendent de nous ? | |
| Quelle est notre surface exposée ? *(ch. 22)* | |
| Sommes-nous nommés publiquement quelque part ? | |

**Cet exercice ne produit pas un score.** Il produit une conversation avec les métiers, et c'est son intérêt : il est fréquent que la direction découvre à cette occasion que l'organisation est plus visible qu'elle ne le pensait.

### 16.5 Comment cette compréhension change une décision défensive

Quatre exemples concrets, parce qu'un chapitre d'économie qui ne débouche sur aucune décision serait hors sujet.

| Situation | Sans la grille économique | Avec la grille |
|---|---|---|
| Deux vulnérabilités critiques, une seule fenêtre | On traite la plus grave techniquement | On traite celle qui est **automatisable sur un produit très déployé** — le coût d'exploitation est plus bas, donc l'exploitation plus probable |
| Un fournisseur mineur est compromis | On considère l'incident comme extérieur | On évalue si nous sommes **accessibles par ce chemin** : c'est un accès à faible coût |
| Une campagne vise notre secteur | On mobilise | On demande d'abord **par où** : si le vecteur est un produit que nous n'avons pas, le coût d'accès chez nous reste inchangé |
| Un investissement en détection est arbitré | On raisonne en couverture | On raisonne en **augmentation du coût pour l'attaquant** : quelle étape rendons-nous chère ? |

🎯 **ET MAINTENANT ?**
*Une vulnérabilité de gravité maximale est publiée sur un produit que vous utilisez, et une vulnérabilité de gravité moyenne sur un autre. Vous ne pouvez en traiter qu'une cette semaine. Que demandez-vous avant de choisir ?*
**Réponse** : trois questions économiques, pas techniques. *L'exploitation est-elle automatisable ou requiert-elle un travail spécifique ? · Le produit est-il très déployé, donc rentable à cibler en masse ? · Un code d'exploitation est-il disponible publiquement ?* Une vulnérabilité de gravité moyenne, triviale à automatiser sur un produit très répandu et dont l'exploitation circule, sera exploitée avant une vulnérabilité maximale exigeant deux semaines de travail sur une cible unique. La gravité technique ne dit rien du coût d'exploitation — et c'est le coût qui décide de l'ordre.

### 16.6 📌 Ce que ce chapitre ne traite pas

Par honnêteté sur son périmètre volontairement restreint :

| Hors périmètre | Où l'apprendre |
|---|---|
| Le fonctionnement détaillé des marchés criminels | Publications spécialisées, formations dédiées |
| Les mécanismes de paiement et de blanchiment | Domaine de la lutte anti-blanchiment |
| La cartographie des groupes et de leurs relations | Périmé rapidement, et sans effet sur vos décisions (§13.4) |
| L'économie des vulnérabilités et des courtiers | Sujet réel, mais sans conséquence opérationnelle pour un défenseur |

**La règle appliquée ici** est celle de la doctrine : un développement n'a sa place dans ce cours que s'il change une décision. Les quatre sujets ci-dessus sont intéressants ; ils ne modifient pas ce que vous ferez lundi.

### Synthèse mentale du chapitre 16

La plupart des attaques sont des opérations, avec des coûts et une rentabilité attendue : un adversaire rationnel ne choisit pas la cible la plus intéressante mais celle dont le rapport gain/coût d'accès est le plus favorable. La chaîne est fragmentée entre développeurs, courtiers d'accès et opérateurs, ce qui a trois conséquences — l'entrée et l'exploitation peuvent être séparées de plusieurs mois, le mode opératoire n'identifie pas un acteur unique, et beaucoup d'organisations attaquées n'ont jamais été ciblées mais **disponibles**. Chaque mesure qui augmente le coût d'une étape déplace l'adversaire opportuniste vers une autre cible, ce qui ne vaut plus face à un adversaire déterminé. Trois facteurs font d'une organisation une cible — valeur, accessibilité, visibilité — et le troisième est le plus mal évalué : beaucoup d'organisations se croient discrètes et sont parfaitement identifiables. Enfin, la gravité technique ne dit rien du coût d'exploitation, et c'est le coût qui décide de l'ordre dans lequel les vulnérabilités sont exploitées.

**Trois questions de vérification**

1. Une vulnérabilité de gravité moyenne est exploitée massivement en 48 heures pendant qu'une vulnérabilité maximale reste inexploitée six mois. Expliquez, sans invoquer la chance.
2. Votre organisation demande « pourquoi nous ? » après un incident. Pourquoi cette question n'a-t-elle souvent pas de réponse individuelle ?
3. Vous arbitrez un investissement en sécurité. Reformulez le critère de choix en termes de coût pour l'adversaire.

→ **Chapitre 17 — Les acteurs, par leur logique** : comment raisonner sur un adversaire sans jamais avoir besoin de son nom.

---

## Chapitre 17 — Les acteurs, par leur logique et non par leur nom

### 17.1 Une typologie par motivation et contrainte

**Le principe de ce chapitre** : ce qui est utile chez un acteur n'est pas son identité mais **ce qui le contraint** — son objectif, ses moyens, son horizon, et ce qu'il ne peut pas se permettre.

Ces quatre paramètres se déduisent de l'observation, sans jamais nommer personne. Et ils sont stables sur des années, là où les noms se périment.

| Paramètre | Question | Ce qu'il permet de prévoir |
|---|---|---|
| **Objectif** | Que cherche-t-il à obtenir ? | Ce qu'il fera une fois entré |
| **Moyens** | Que peut-il se payer ? | Le niveau de sophistication attendu |
| **Horizon** | Combien de temps peut-il attendre ? | Discrétion ou rapidité |
| **Contrainte** | Que ne peut-il pas se permettre ? | Ce qui le fera renoncer |

### 17.2 Les criminels

| Paramètre | Valeur typique |
|---|---|
| Objectif | Un gain financier, le plus rapidement possible |
| Moyens | Variables, souvent achetés plutôt que développés |
| Horizon | **Court** — quelques jours à quelques semaines dans le réseau |
| Contrainte | **La rentabilité.** Une opération non rentable est abandonnée |

**Ce que cela permet de prévoir** : un comportement opportuniste, une préférence pour le volume, une progression rapide et bruyante, un abandon face à la résistance, et une monétisation directe — chiffrement, extorsion, revente, fraude.

**La conséquence défensive la plus utile** : contre un acteur contraint par la rentabilité, **augmenter le coût suffit**. Il ne s'agit pas de rendre l'attaque impossible, mais de la rendre moins rentable que la cible suivante.

### 17.3 Les acteurs étatiques

| Paramètre | Valeur typique |
|---|---|
| Objectif | Renseignement, positionnement, parfois sabotage — **non financier** |
| Moyens | Élevés, développement propre possible |
| Horizon | **Long** — des mois, parfois des années |
| Contrainte | **La discrétion.** Être découvert a un coût politique |

**Ce que cela permet de prévoir** : une progression lente, un souci de persistance, un évitement des actions bruyantes, un ciblage sélectif, et une absence de monétisation directe.

⚠️ **PIÈGE — l'attribution étatique par sophistication**
« C'était sophistiqué, donc c'est étatique » est un raisonnement circulaire et faux. Des acteurs criminels emploient des techniques avancées ; des acteurs étatiques emploient régulièrement des techniques banales, précisément parce qu'elles fonctionnent et qu'elles ne les distinguent pas. **La sophistication n'est pas un marqueur d'origine.**

### 17.4 Les hacktivistes

| Paramètre | Valeur typique |
|---|---|
| Objectif | La visibilité d'un message |
| Moyens | Souvent limités |
| Horizon | Court, souvent aligné sur un événement |
| Contrainte | **Ils ont besoin d'être vus** |

**Ce que cela permet de prévoir** : des actions à effet visible — indisponibilité, défiguration, divulgation — plutôt qu'une persistance discrète, et une revendication.

**Le point d'attention** : la revendication est facile à usurper. Une action revendiquée par un collectif n'a pas nécessairement été conduite par lui, et une revendication peut couvrir une opération d'une autre nature.

### 17.5 La menace interne

Deux cas distincts, qu'il faut séparer.

| | **Intentionnelle** | **Accidentelle** |
|---|---|---|
| Objectif | Gain, vengeance, conviction | Aucun |
| Contrainte | Ne pas être identifié — or il l'est presque toujours | — |
| Fréquence | Rare | **Très fréquente** |
| Détectabilité | Difficile : usage d'accès légitimes | Souvent invisible |

**Le rapport de fréquence est le point à retenir.** L'erreur — configuration exposée, envoi au mauvais destinataire, service ouvert par commodité — produit bien plus d'incidents que la malveillance interne. Une fonction CTI qui consacre son attention à la seconde en négligeant la première se trompe de priorité.

### 17.6 Prestataires et chaîne d'approvisionnement

Ce n'est pas un type d'acteur mais un **chemin**, et il mérite une place ici parce qu'il modifie l'application des quatre paramètres.

**Le mécanisme** : l'adversaire n'attaque pas votre organisation, il attaque quelqu'un qui a accès à votre organisation — infogérant, éditeur, partenaire d'échange.

**Ce que cela change** :

| Aspect | Effet |
|---|---|
| Le coût d'accès | **Fortement réduit** — un prestataire donne accès à plusieurs organisations |
| Le ciblage | Vous n'êtes pas ciblé, vous êtes atteignable |
| La détection | L'activité emprunte des accès **légitimes** |
| La défense | Elle ne dépend qu'en partie de vous (le chapitre 31 du cours MCS) |

**C'est le chemin dont le rapport coût/gain est le plus favorable**, ce qui explique sa fréquence croissante — et c'est précisément le raisonnement du §16.1.

### 17.7 ⚠️ Pourquoi ce cours ne contient aucun catalogue d'acteurs

Quatre raisons, dans l'ordre d'importance.

| Raison | Explication |
|---|---|
| **Péremption** | Les acteurs se recomposent, se scindent, changent d'outillage. Un catalogue a dix-huit mois de retard le jour où il est écrit |
| **Inutilité décisionnelle** | Vos mesures ne changent pas selon l'auteur (§13.4) |
| **Illusion de maîtrise** | Connaître des noms donne le sentiment de comprendre la menace, et dispense de comprendre les mécanismes |
| **Dépendance à une source** | Les désignations diffèrent selon les éditeurs ; les adopter revient à adopter leur découpage |

**Ce qui remplace le catalogue** : les quatre paramètres du §17.1, appliqués à ce que vous observez. Ils fonctionnent sur un acteur inconnu, ce qu'un catalogue ne fait jamais.

### 17.8 Raisonner sur un acteur inconnu

C'est la situation normale. Voici la méthode, en quatre questions.

```
1. OBJECTIF    Qu'est-ce qui a été fait une fois l'accès obtenu ?
               → chiffrement, exfiltration, persistance, rien ?

2. HORIZON     Combien de temps entre l'entrée et l'action ?
               → heures = opportuniste · mois = patient

3. MOYENS      L'outillage est-il public, acheté, ou propre ?
               → public = faibles moyens ou volonté de se fondre

4. CONTRAINTE  Qu'est-ce qui a été évité ?
               → bruit évité = discrétion prioritaire
               → rien évité = rapidité prioritaire
```

**Ce que ces quatre réponses produisent** : un profil suffisant pour anticiper la suite, sans aucun nom. Et surtout, **un profil révisable** : chaque nouvelle observation ajuste un paramètre, là qu'un nom, une fois posé, résiste aux éléments contraires (§7.3).

🎯 **ET MAINTENANT ?**
*Un incident est en cours. L'équipe de réponse vous demande : « à qui on a affaire ? ». Que répondez-vous dans l'heure ?*
**Réponse** : jamais un nom. Les quatre paramètres, avec ce que vous observez. *« L'accès date d'au moins six semaines et rien n'a été chiffré : horizon long, objectif probablement non financier. L'outillage est public, ce qui n'indique pas des moyens faibles — cela peut être délibéré. Aucune action bruyante n'a été relevée : la discrétion semble prioritaire. En conséquence, nous recommandons de privilégier la recherche de persistance et l'analyse des accès plutôt que la restauration immédiate. »* Ce profil est opérationnel dans l'heure, et il oriente réellement les opérations — ce qu'un nom n'aurait pas fait.

### 17.9 🔴 FIL ROUGE — mai 2030 : « pourquoi nous ? »

Le 6 mai, HELIOMED subit une tentative d'intrusion. Le vecteur : un compte de prestataire, dont les identifiants figuraient dans une fuite publiée deux mois plus tôt. L'authentification multifacteur, active, bloque la tentative. Aucun accès n'est obtenu.

**La question que Pierre Vasseur, directeur général, pose au comité de crise** :

> *« Pourquoi nous ? Qu'est-ce qu'on a fait pour être visés ? »*

**Ce que Nour aurait pu répondre en 2029** : chercher un acteur, un ciblage, une explication narrative.

**Ce qu'elle répond**, en appliquant les quatre paramètres et le §16.4 :

> *Nous n'avons probablement pas été visés en particulier — confiance moyenne.*
>
> *Les identifiants employés proviennent d'une fuite publique de mars, contenant environ deux cent mille comptes de nombreuses organisations. La tentative a eu lieu à 04 h 12, dans une série de tentatives séquentielles sur quatorze comptes de notre domaine, tous présents dans cette fuite. Aucun compte absent de la fuite n'a été essayé.*
>
> *Ce profil correspond à une exploitation automatisée de la fuite, sans sélection préalable de cible. **Nous n'étions pas choisis, nous étions présents dans la liste.***
>
> *Ce qui invaliderait cette évaluation : la découverte de tentatives sur des comptes absents de la fuite · une reconnaissance préalable de notre infrastructure · un ciblage d'actifs spécifiques plutôt que du portail générique.*

**La vérification que cette conclusion déclenche.** Puisque l'hypothèse retenue est l'exploitation d'une fuite, la question utile n'est pas « qui nous attaque » mais **« combien de nos comptes figurent dans cette fuite, et lesquels sont encore valides ? »**.

Résultat, en deux jours : **quarante et un comptes** d'HELIOMED figurent dans la fuite. Quatorze ont été essayés. Trente-sept sont encore actifs. Trois n'ont pas d'authentification multifacteur — deux comptes de service et un compte d'un prestataire dont le contrat s'est achevé en 2028.

**C'est ce dernier qui compte.** Il n'avait pas été détecté par les revues d'accès précédentes parce qu'il figurait dans un annuaire secondaire, hérité d'une acquisition.

**Ce que Pierre Vasseur retient**, et qu'il formule en séance :

> *« Donc la bonne question n'était pas "pourquoi nous", c'était "qu'est-ce qui traîne chez nous". »*

**Les trois décisions** : rotation des trente-sept comptes concernés · surveillance systématique des fuites contenant le nom de domaine d'HELIOMED, ajoutée au plan de collecte comme besoin B-07 · revue des annuaires secondaires, portée au dispositif de MCS.

**Ce que Nour note.** L'évaluation n'a nommé personne, et elle a produit trois décisions. Un nom en aurait produit zéro.

> *« "Pourquoi nous" est une question de récit. "Qu'est-ce qui est accessible" est une question de renseignement. »*

**Livrable de l'épisode.** La grille des quatre paramètres (§17.8), intégrée à la procédure de réponse à incident — et le besoin B-07.

→ La suite en 🔴 §18.8, quand une cartographie de couverture se révélera excellente là où c'était facile.

### Synthèse mentale du chapitre 17

Ce qui est utile chez un acteur n'est pas son identité mais ce qui le contraint : objectif, moyens, horizon, et ce qu'il ne peut pas se permettre — quatre paramètres déductibles de l'observation, stables sur des années, et applicables à un acteur inconnu. Un criminel est contraint par la rentabilité, donc augmenter le coût suffit à le déplacer ; un acteur étatique est contraint par la discrétion, donc la sophistication n'est pas un marqueur d'origine — le raisonnement inverse est circulaire et faux. La menace interne accidentelle produit bien plus d'incidents que l'intentionnelle, et une fonction qui privilégie la seconde se trompe de priorité. La chaîne d'approvisionnement n'est pas un acteur mais un chemin, dont le rapport coût/gain est le plus favorable — ce qui explique sa fréquence. Enfin, un catalogue d'acteurs se périme en dix-huit mois, ne change aucune décision, et donne l'illusion de comprendre : les quatre paramètres le remplacent avantageusement, parce qu'ils restent révisables là qu'un nom, une fois posé, résiste aux éléments contraires.

**Trois questions de vérification**

1. Une intrusion emploie un outillage public et progresse lentement sans rien chiffrer. Que déduisez-vous, et qu'est-ce que vous ne déduisez pas ?
2. Pourquoi « c'était sophistiqué, donc c'est étatique » est-il un raisonnement fautif, et dans les deux sens ?
3. Votre direction demande « pourquoi nous ? ». Reformulez la question de manière à ce qu'elle produise des décisions.

---

## Chapitre 18 — Modes opératoires et modèles de représentation

### 18.1 Pourquoi modéliser

**Le problème que les modèles résolvent** : sans langage commun, une intrusion se décrit en prose, et deux descriptions de la même intrusion ne se ressemblent pas. On ne peut ni comparer, ni agréger, ni mesurer une couverture.

**Ce qu'un modèle apporte**, et c'est tout ce qu'il apporte :

| Apport | Mécanisme |
|---|---|
| **Un langage partagé** | Analyste, détection et exploitation nomment la même chose de la même façon |
| **La comparabilité** | Deux incidents deviennent comparables |
| **La mesurabilité** | On peut dire ce qu'on couvre et ce qu'on ne couvre pas |
| **La complétude** | Une case vide se voit — comme dans la matrice du §8.2 |

📌 **Ce qu'un modèle n'apporte pas** : il ne dit pas ce qui est probable, ni ce qui est grave, ni ce qui vous concerne. C'est une **grille de description**, pas une grille d'évaluation. Confondre les deux produit des cartographies impressionnantes et sans valeur décisionnelle (§18.6).

### 18.2 Les référentiels de tactiques et techniques

**Le principe.** Un référentiel de ce type organise les comportements adverses observés en une hiérarchie à deux ou trois niveaux :

```
TACTIQUE      le but poursuivi à cette étape
   └── TECHNIQUE      la manière de l'atteindre
          └── SOUS-TECHNIQUE      la variante précise
```

**Ce qui fait leur force** : ils décrivent des **comportements observés**, pas des menaces théoriques. Chaque entrée est adossée à des cas documentés.

**Ce qui fait leur limite, et qui découle directement de la force précédente** :

> **Un référentiel décrit le passé observé. Ce qui n'y figure pas n'est pas inexistant — c'est simplement non encore documenté publiquement.**

C'est la formulation durable du §1.8, et elle survivra à toutes les versions.

**Les trois usages réels**, par ordre de valeur :

| Usage | Ce qu'il produit |
|---|---|
| **Décrire un incident** | Une description comparable et transmissible |
| **Mesurer une couverture de détection** | Une analyse d'écart (§30.3) |
| Décrire un acteur | Le moins utile — les acteurs partagent l'essentiel de leurs techniques |

### 18.3 Chaîne d'attaque et modèle du diamant

Deux autres modèles courants, avec leur domaine d'utilité propre.

| Modèle | Ce qu'il représente | Quand il est utile | Sa limite |
|---|---|---|---|
| **Chaîne d'attaque** | Une séquence linéaire d'étapes, de la reconnaissance à l'objectif | **Communiquer** avec des non-spécialistes · raisonner sur les points d'interruption | Les intrusions réelles ne sont ni linéaires ni complètes |
| **Modèle du diamant** | Quatre sommets — adversaire, infrastructure, capacité, victime — et leurs relations | **Pivoter** : d'un sommet connu vers les autres · relier des incidents | Ne dit rien de la chronologie |
| **Référentiel de techniques** | Un catalogue structuré de comportements | Décrire, mesurer, comparer | Volumineux, et sans hiérarchie de gravité |

**La règle de choix**, qui évite l'essentiel des débats stériles :

> **La chaîne pour expliquer. Le diamant pour relier. Le référentiel pour mesurer.**

Ces trois modèles ne sont pas concurrents. Les employer ensemble sur un même incident est le cas normal.

### 18.4 La pyramide de la difficulté

**Le principe** : tous les éléments qu'on peut détecter n'ont pas la même valeur, parce qu'ils ne coûtent pas la même chose à l'adversaire pour être changés.

```
                    ▲  COÛT POUR L'ADVERSAIRE
                    │
      Comportements │  ████████████████  très coûteux à changer
   Outils employés  │  ██████████
      Artefacts     │  ██████
   Noms de domaine  │  ████
        Adresses    │  ██
       Empreintes   │  █  trivial à changer
                    │
```

**Ce que cela implique pour votre travail** :

| Niveau | Durée de vie | Coût de détection | Rendement |
|---|---|---|---|
| Empreinte de fichier | Une variante | Très faible | **Très faible** |
| Adresse | Jours à semaines | Faible | Faible |
| Nom de domaine | Semaines | Faible | Faible |
| Artefact d'hôte | Mois | Moyen | Moyen |
| Outil employé | Mois à années | Élevé | Élevé |
| **Comportement** | **Années** | **Élevé** | **Très élevé** |

**La conséquence sur la production de renseignement** : un jeu de cent indicateurs techniques vaut moins qu'une description précise de trois comportements. Le premier se périme en semaines et produit des faux positifs ; le second oriente durablement la détection.

⚠️ **PIÈGE — le volume d'indicateurs comme mesure de valeur**
C'est le §3.3, et c'est le mode de facturation de nombreuses offres commerciales. Un flux se vend au volume parce que le volume est mesurable ; sa valeur, elle, se situe en haut de la pyramide, là où le volume est faible.

### 18.5 ⚠️ Quand ne pas utiliser un modèle

Quatre situations, toutes fréquentes.

| Situation | Pourquoi le modèle nuit |
|---|---|
| **Communiquer avec une direction** | Une matrice de techniques est illisible. Le récit vaut mieux |
| **Un incident en cours** | La classification consomme du temps que la réponse exige |
| **Une menace nouvelle** | Elle ne rentre pas dans les cases, et forcer la classification déforme l'observation |
| **Quand la classification devient l'objectif** | On produit une cartographie au lieu de produire une décision |

**La quatrième est la plus insidieuse.** Une organisation peut consacrer des mois à cartographier sa couverture sans qu'aucune règle de détection ne soit écrite. La cartographie est un moyen ; elle devient un livrable auto-justifié avec une facilité déconcertante.

### 18.6 Une cartographie est un actif à maintenir

C'est le point durable de ce chapitre, et il vaut indépendamment de tout référentiel particulier.

**Le mécanisme du vieillissement** :

| Cause | Effet |
|---|---|
| Le référentiel évolue | Techniques ajoutées, renommées, scindées, dépréciées |
| Vos règles évoluent | Ajoutées, modifiées, désactivées sans mise à jour de la cartographie |
| Vos sources de journaux évoluent | Une règle cartographiée devient inopérante si sa source disparaît |
| Votre parc évolue | Une technique non applicable le devient, ou l'inverse |

**Ce qu'une cartographie non maintenue produit** : une image rassurante et fausse — exactement le problème du dénominateur inconnu au cours MCS.

✅ **BONNE PRATIQUE (P0) — les quatre attributs d'une cartographie exploitable**

Pour chaque case cartographiée :

| Attribut | Pourquoi |
|---|---|
| **La source de journaux** dont dépend la couverture | Si elle disparaît, la couverture disparaît |
| **La date du dernier test** | Une règle non testée est une intention |
| **Le niveau de couverture** — totale, partielle, théorique | « Couvert » sans nuance est presque toujours faux |
| **La version du référentiel** utilisée | Pour savoir ce qui devra être remappé |

⏱ **ÉTAT DE L'ART (vérifié le 2 août 2026)** — Le principal référentiel public de tactiques et techniques a connu en avril 2026 une évolution structurelle : l'une de ses tactiques historiques a été **scindée en deux**, l'une conservant l'identifiant d'origine. Une table de correspondance a été publiée. Toute cartographie, règle ou publication antérieure y faisant référence doit être remappée. 📎 [S-01]

**Ce que cet événement illustre**, et c'est l'enseignement à retenir quand la version aura changé : **un remaniement structurel d'un référentiel n'est pas un événement exceptionnel**, c'est un événement périodique. La question n'est pas de savoir s'il se reproduira, mais si votre cartographie porte les attributs qui permettront de la remapper — notamment le quatrième.

### 18.7 🔬 Mini-lab 6 — Lire une cartographie de couverture

**Objectif** — Interpréter une cartographie et identifier ce qu'elle ne dit pas.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §18.4, §18.6 · **Livrable** analyse d'écart priorisée
**Compétences validées** — ✔ distinguer couverture théorique et effective ✔ relier une couverture à sa source de journaux ✔ repérer le biais de facilité ✔ prioriser un développement de détection

**Le dossier fourni** — extrait d'une cartographie d'une organisation de 900 personnes, secteur industriel.

| Tactique | Techniques du référentiel | Déclarées couvertes | Taux affiché |
|---|---|---|---|
| Reconnaissance | 10 | 1 | 10 % |
| Accès initial | 11 | **9** | **82 %** |
| Exécution | 14 | **12** | **86 %** |
| Persistance | 20 | 7 | 35 % |
| Élévation de privilèges | 14 | 6 | 43 % |
| Contournement des défenses | 43 | 8 | 19 % |
| Accès aux identifiants | 17 | 5 | 29 % |
| Découverte | 32 | 3 | 9 % |
| Mouvement latéral | 9 | 4 | 44 % |
| Collecte | 17 | 2 | 12 % |
| Exfiltration | 9 | 2 | 22 % |
| Impact | 14 | **11** | **79 %** |
| **Total** | **210** | **70** | **33 %** |

**Informations complémentaires fournies :**

```
· 52 des 70 règles reposent sur les journaux du poste de travail.
· 9 reposent sur les journaux du pare-feu.
· 6 reposent sur les journaux d'annuaire.
· 3 reposent sur une source applicative.
· Aucune des 70 règles n'a de date de test enregistrée.
· La cartographie a été établie il y a 14 mois.
· Le référentiel a connu une évolution majeure il y a 4 mois.
· Les 3 derniers incidents de l'organisation ont impliqué :
    accès initial via identifiants valides · découverte · mouvement
    latéral · exfiltration.
```

**Questions** : (a) Que vous dit ce tableau, et que ne vous dit-il pas ? (b) Où est le biais ? (c) Quelles trois priorités ? (d) Quelle information manquante est la plus grave ?

---

**Corrigé commenté**

**(a) Ce que le tableau dit, et ne dit pas**

| Il dit | Il ne dit pas |
|---|---|
| 70 techniques sont déclarées couvertes sur 210 | Si ces règles **fonctionnent** — aucune date de test |
| La couverture est très inégale selon les tactiques | Si les techniques couvertes sont **pertinentes pour cette organisation** |
| Un taux global de 33 % | Ce que 33 % signifie — toutes les techniques ne se valent pas |
| — | Si la cartographie est encore **valide** : 14 mois, et une évolution du référentiel il y a 4 mois |

⚠️ **Le taux global de 33 % est le chiffre le moins informatif du tableau.** Il additionne des techniques de poids très différents et suppose que couvrir 210 techniques serait un objectif — ce qui n'a aucun sens.

**(b) Le biais : la couverture suit la facilité, pas le risque**

Le croisement entre les taux et les sources de journaux est sans ambiguïté :

| Tactique | Taux | Source dominante | Difficulté de détection |
|---|---|---|---|
| Accès initial, Exécution, Impact | **79-86 %** | Poste de travail | **Facile** — les journaux existent |
| Découverte, Collecte, Contournement | **9-19 %** | Réseau, annuaire, applicatif | **Difficile** — journaux absents ou bruités |

**52 des 70 règles reposent sur une seule source.** L'organisation ne couvre pas ce qui est risqué : elle couvre **ce qu'elle voit**, et elle ne voit qu'un poste de travail.

**La confirmation vient des incidents réels** : les trois derniers ont impliqué identifiants valides, découverte, mouvement latéral et exfiltration — soit quatre tactiques dont les taux sont respectivement 29 %, 9 %, 44 % et 22 %. **La cartographie est excellente là où rien ne s'est passé.**

**(c) Les trois priorités**

| Priorité | Action | Justification |
|---|---|---|
| **1** | **Obtenir les journaux d'annuaire complets** | Débloque simultanément *accès aux identifiants*, *découverte* et *mouvement latéral* — les trois tactiques présentes dans les incidents réels. Une source, trois tactiques |
| **2** | **Tester les 70 règles existantes** | Une couverture déclarée non testée est une hypothèse. Le taux réel est inconnu, et il est certainement inférieur à 33 % |
| **3** | **Remapper la cartographie** sur la version courante du référentiel | 4 mois après une évolution majeure, une partie des correspondances est fausse |

⚠️ **L'ordre compte.** La priorité 2 est moins visible que la 1 mais plus urgente sur le plan de la sincérité : on ne peut pas prioriser à partir d'un état des lieux dont on ignore s'il est vrai.

**(d) L'information manquante la plus grave**

**L'absence de date de test.** Elle rend l'ensemble du tableau inexploitable : sans test, « couvert » signifie *une règle existe*, pas *elle détecte*. Les autres lacunes — pertinence pour l'organisation, version du référentiel, niveau de couverture partielle ou totale — sont graves ; celle-ci invalide tout le reste.

**Les trois erreurs attendues**

1. **Conclure qu'il faut augmenter le taux global.** L'objectif n'est pas 210 techniques : c'est de couvrir ce qui est plausible dans le contexte.
2. **Prioriser sur les tactiques aux taux les plus bas.** *Reconnaissance* est à 10 % et c'est sans importance : cette activité est majoritairement externe et non détectable depuis l'organisation.
3. **Ignorer les incidents réels.** Ils constituent la seule donnée du dossier qui indique ce qui se passe réellement — et ils contredisent la cartographie.

### 18.8 🔴 FIL ROUGE — juin 2030 : excellents là où c'était facile

Nour et le référent détection conduisent le premier exercice de cartographie de couverture d'HELIOMED, en réponse au besoin B-05 (*ce que je ne détecte pas*).

**Le résultat brut** : 41 % de couverture déclarée. Le référent détection est satisfait — le chiffre est supérieur à ce qu'il attendait.

**Le croisement que Nour ajoute**, en une demi-journée : pour chaque règle, la source de journaux dont elle dépend.

| Source | Règles | Part |
|---|---|---|
| Poste de travail | 61 | **68 %** |
| Pare-feu | 14 | 16 % |
| Annuaire | 9 | 10 % |
| Applicatif métier | 5 | 6 % |
| **Systèmes industriels (Saint-Étienne)** | **0** | **0 %** |

**Le second croisement**, avec les quatre besoins actifs de la fonction : les techniques couvertes correspondent-elles aux menaces identifiées comme pertinentes pour HELIOMED ?

| Menace pertinente identifiée | Couverture |
|---|---|
| Compromission d'un prestataire d'infogérance *(épisode de septembre 2029)* | **Partielle** — 2 règles, aucune testée |
| Exploitation d'identifiants issus de fuites *(épisode de mai 2030)* | **Aucune** au moment de l'exercice |
| Atteinte à la plateforme de télésuivi via les serveurs applicatifs | Partielle |
| Activité sur le réseau industriel | **Aucune source de journaux** |

**Ce que l'exercice établit** : HELIOMED détecte bien ce qui se passe sur les postes de travail — parce que c'est là que les journaux existent — et ne détecte rien de ce qui correspond aux deux incidents réellement survenus en dix-huit mois.

**La réaction du référent détection**, qu'il faut noter parce qu'elle est saine :

> *« Je savais que je manquais de sources. Je ne savais pas que mes 41 % ne couvraient rien de ce qui nous est arrivé. »*

**Les trois décisions**, priorisées par source plutôt que par technique :

| # | Action | Effet attendu |
|---|---|---|
| 1 | Collecte des journaux d'annuaire complets — la source manquait, pas la volonté | Débloque trois tactiques |
| 2 | Test des 89 règles existantes, par lots de dix | Établir la couverture réelle |
| 3 | Écoute passive sur le réseau industriel — projet, échéance 2031 | Couvre une zone entièrement aveugle |

**Le résultat du point 2, trois mois plus tard** : sur 89 règles testées, **17 ne déclenchent pas** — sources modifiées, champs renommés, seuils devenus inopérants. La couverture réelle était de 33 %, pas 41 %.

**Ce que Claire porte au comité** : le chiffre a **baissé** de 41 à 33 %, et c'est un progrès. C'est la première fois qu'il est vrai.

> *« Nous avons perdu huit points et gagné la possibilité de décider »*, écrit-elle au compte rendu.

**Livrable de l'épisode.** La cartographie d'HELIOMED avec ses quatre attributs par case (§18.6), et la règle du test obligatoire avant déclaration de couverture.

→ La suite en 🔴 §19.5, quand plusieurs signalements isolés se révéleront être une seule campagne.

### Synthèse mentale du chapitre 18

Un modèle apporte un langage partagé, la comparabilité, la mesurabilité et la visibilité des manques — et rien d'autre : c'est une grille de description, jamais d'évaluation. Un référentiel décrit le passé observé, donc ce qui n'y figure pas n'est pas inexistant, seulement non documenté. Trois modèles coexistent sans se concurrencer : la chaîne pour expliquer, le diamant pour relier, le référentiel pour mesurer. La pyramide de la difficulté explique qu'un jeu de cent indicateurs techniques vaille moins qu'une description précise de trois comportements — le volume se vend parce qu'il se mesure, la valeur se situe là où le volume est faible. Une cartographie est un actif à maintenir, et sans ses quatre attributs — source de journaux, date de test, niveau réel, version du référentiel — elle produit une image rassurante et fausse. Enfin, une couverture suit presque toujours la facilité plutôt que le risque : on couvre ce qu'on voit, et on ne voit que là où les journaux existent.

**Trois questions de vérification**

1. Une cartographie affiche 33 % de couverture. Quelles trois questions posez-vous avant d'en tirer une priorité ?
2. Pourquoi une source de journaux manquante est-elle une meilleure unité de priorisation qu'une technique non couverte ?
3. Votre taux de couverture passe de 41 à 33 % après tests. Comment le présentez-vous à une direction ?

→ **Chapitre 19 — Les campagnes** : comment plusieurs signalements isolés deviennent un objet unique, et ce que cela change.

---

## Chapitre 19 — Les campagnes

### 19.1 Ce qu'est une campagne, et pourquoi la notion est utile

**Définition de travail** : une campagne est un **ensemble d'activités regroupées par l'analyste** parce qu'elles partagent suffisamment de caractéristiques pour être raisonnées ensemble.

Le mot important est *regroupées par l'analyste*. Une campagne n'est pas un objet du monde — c'est une **construction analytique**. L'adversaire ne se dit pas qu'il mène une campagne ; vous décidez que ces onze incidents forment un tout.

**Pourquoi la notion est utile malgré son caractère construit** :

| Apport | Mécanisme |
|---|---|
| **Elle permet de prévoir** | Ce qui a été fait chez les onze premiers indique ce qui sera fait ensuite |
| **Elle permet de prioriser** | Une vulnérabilité exploitée dans une campagne active n'est plus une vulnérabilité parmi d'autres |
| **Elle permet de partager** | C'est l'unité d'échange dans les dispositifs sectoriels |
| **Elle réduit le volume** | Onze signalements deviennent un dossier |

**C'est le niveau 2 de l'attribution** (§13.1) — le regroupement opérationnel. Il ne nécessite aucun nom d'acteur et c'est celui qui vous sert.

### 19.2 Les critères de regroupement, et leur solidité

Tous les critères ne se valent pas, et c'est ici que le chapitre 18 se rejoue.

| Critère | Solidité | Pourquoi |
|---|---|---|
| **Même vulnérabilité exploitée** | Moyenne | Beaucoup d'acteurs exploitent la même |
| **Même infrastructure** | Moyenne | Hébergement partagé, adresses réattribuées |
| **Même outillage** | Moyenne à faible | Les outils circulent (§13.3) |
| **Même séquence de comportements** | **Élevée** | Coûteuse à imiter, stable dans le temps |
| **Même erreur ou particularité** | **Élevée** | Un détail non fonctionnel est rarement copié |
| Même secteur visé | **Faible** | C'est souvent une conséquence, pas une cause |
| Même période | **Très faible** | Coïncidence fréquente (§4.2) |

**La règle** : un regroupement fondé sur un seul critère de solidité moyenne ou faible est une hypothèse, pas une campagne. Il faut au minimum **deux critères indépendants**, dont un de solidité élevée.

⚠️ **PIÈGE — le regroupement par secteur**
« Trois organisations du secteur médical » est le critère le plus employé et l'un des plus faibles. Il produit des campagnes fictives — et c'est exactement ce qui s'est passé au §7.9 du fil rouge, et ce que l'élément ③ du §8.9 a permis d'éviter.

### 19.3 Le cycle de vie d'une vulnérabilité exploitée

Comprendre ce cycle permet de savoir **où vous en êtes** quand une information vous parvient — et donc combien de temps il vous reste.

```
①  Découverte           par un chercheur, un éditeur, ou un attaquant
        ↓
②  Publication          avis, correctif disponible
        ↓  ← délai variable : heures à mois
③  Analyse publique     décomposition du correctif, compréhension du défaut
        ↓  ← délai souvent court
④  Code d'exploitation  publié, vendu, ou développé
        ↓
⑤  Exploitation ciblée  quelques cas, souvent invisibles
        ↓
⑥  Exploitation massive automatisée, opportuniste
        ↓
⑦  Persistance          la vulnérabilité reste exploitée des années
                        sur les systèmes non corrigés
```

**Les quatre observations qui comptent** :

| Observation | Conséquence |
|---|---|
| Le délai ②→⑥ est **très variable** — d'heures à jamais | Il dépend de l'automatisabilité et du déploiement (§16.3), pas de la gravité |
| L'étape ⑤ est **souvent invisible** | Quand vous apprenez qu'une vulnérabilité est exploitée, vous êtes déjà en ⑥ |
| L'étape ⑦ dure des années | Une vulnérabilité ancienne reste un vecteur majeur |
| Une information reçue à l'étape ③ vaut beaucoup plus qu'à l'étape ⑥ | C'est ce que le renseignement sectoriel peut apporter |

**La question à poser devant toute information de ce type** : *à quelle étape sommes-nous ?* La réponse détermine s'il vous reste des semaines ou des heures.

### 19.4 Ce qui fait passer une menace du général au « nous »

Quatre conditions, cumulatives. Tant qu'elles ne sont pas toutes vérifiées, la menace reste générale — et le §7.9 est né de l'oubli de ce point.

| # | Condition | Question | Si non vérifiée |
|---|---|---|---|
| **1** | **Applicabilité** | Le produit, la version, la configuration existent-ils chez nous ? | La menace ne nous concerne pas |
| **2** | **Accessibilité** | Le vecteur est-il ouvert chez nous ? | La menace nous concerne, sans être exploitable |
| **3** | **Absence de neutralisation** | Une mesure existante l'annule-t-elle ? | La menace est neutralisée — et c'est le cas de §12.7 |
| **4** | **Plausibilité du ciblage** | Sommes-nous dans le périmètre visé, ou disponibles ? *(§16.4)* | La probabilité est faible, pas nulle |

**Les conditions 1 à 3 se vérifient chez vous, pas dans le renseignement reçu.** C'est l'étape 4 du chapitre 2 — le passage de la connaissance au renseignement — et c'est ce qui distingue une fonction utile d'un relais de publications.

🎯 **ET MAINTENANT ?**
*Un dispositif sectoriel signale une campagne active exploitant une vulnérabilité que vous n'avez pas corrigée. Que vérifiez-vous, dans quel ordre, avant de mobiliser ?*
**Réponse** : les quatre conditions, dans l'ordre, et cela prend une heure. *La version affectée est-elle bien celle déployée ?* — dans une majorité de cas, la réponse resserre déjà le périmètre. *L'actif est-il accessible par le vecteur décrit ?* *Une mesure existante neutralise-t-elle l'exploitation — authentification, filtrage, configuration durcie ?* *Sommes-nous dans le périmètre décrit, ou simplement dans le même secteur ?* Si les quatre sont vérifiées, vous mobilisez avec un dossier solide. Si l'une tombe, vous produisez une note de cinq lignes — et vous économisez la mobilisation de §7.9.

### 19.5 Suivre une campagne dans la durée

Une campagne n'est pas un événement, c'est un **dossier ouvert**. Quatre éléments à tenir.

| Élément | Contenu | Fréquence de mise à jour |
|---|---|---|
| **Le périmètre** | Ce qui est inclus, et les critères de regroupement employés | À chaque nouvel élément |
| **L'évaluation courante** | La conclusion calibrée, avec sa date | Mensuelle, ou à événement |
| **Ce qui l'invaliderait** | La clause de réfutation, mise à jour | À chaque révision |
| **Ce qui a été décidé** | Les actions engagées, et leur état | Continue |

**Le piège du dossier ouvert** : il se poursuit par inertie. Une campagne s'éteint, l'adversaire change d'objectif, et le dossier reste actif parce que personne ne décide de le fermer.

✅ **BONNE PRATIQUE (P1) — la clôture explicite**
Fixez un critère de clôture à l'ouverture du dossier : *sans nouvel élément pendant X semaines, la campagne est déclarée close, avec un résumé de ce qui en a été tiré.* La clôture n'est pas une conclusion sur l'adversaire — c'est une décision de gestion de votre capacité.

### 19.6 🔴 FIL ROUGE — juillet 2030 : trois signalements, une campagne

Entre le 2 et le 19 juillet, trois signalements sans rapport apparent entrent dans la file de Nour.

```
② juillet   — Un client hospitalier signale des tentatives d'authentification
              anormales sur son portail HelioLink.
11 juillet  — Le dispositif sectoriel diffuse une note sur l'exploitation
              d'une vulnérabilité affectant une bibliothèque d'authentification
              largement utilisée.
19 juillet  — Un second client signale un ralentissement de sa passerelle
              HelioBox, sans erreur applicative.
```

**Chacun pris isolément est mineur.** Le premier a été archivé comme *incident client, hors périmètre*. Le deuxième a été rattaché au besoin B-01 et transmis à Malik Ferhaoui. Le troisième était en cours de qualification.

**Ce qui déclenche le rapprochement.** Le 21 juillet, Nour applique la revue hebdomadaire de la file — une pratique instaurée en avril (§15.7) : relire les signalements archivés des trois dernières semaines, quinze minutes, à la recherche de recoupements.

Elle remarque que les deux clients concernés utilisent la même version d'HelioLink, et que la bibliothèque mentionnée le 11 juillet est **embarquée dans cette version**.

**Le regroupement, évalué selon le §19.2** :

| Critère | Présent ? | Solidité |
|---|---|---|
| Même vulnérabilité exploitée | **Oui** — la bibliothèque | Moyenne |
| Même séquence de comportements | **Oui** — tentatives d'authentification suivies de dégradation de performance | **Élevée** |
| Même infrastructure | Non vérifié | — |
| Même secteur | Oui | Faible — écarté comme critère |

**Deux critères indépendants, dont un de solidité élevée.** Le regroupement tient.

**Les quatre conditions du §19.4, appliquées à HELIOMED elle-même** :

| # | Condition | Vérification | Résultat |
|---|---|---|---|
| 1 | Applicabilité | La bibliothèque est-elle dans nos versions ? | **Oui** — dans 3 versions sur 5 encore déployées |
| 2 | Accessibilité | Le vecteur est-il ouvert ? | **Oui** — le portail est exposé par nécessité |
| 3 | Neutralisation | Une mesure l'annule-t-elle ? | **Partiellement** — l'authentification multifacteur limite l'exploitation, sans l'empêcher |
| 4 | Plausibilité | Sommes-nous dans le périmètre ? | **Oui** — nos clients le sont déjà |

**Les quatre sont vérifiées.** Ce n'est pas une menace générale : c'est un dossier qui concerne directement le produit d'HELIOMED, chez ses clients.

**L'évaluation produite le 22 juillet**, avec les cinq blocs du §11.2 :

> *Nous estimons **très probable** que les trois signalements procèdent d'une exploitation de la vulnérabilité signalée le 11 juillet, affectant une bibliothèque embarquée dans trois versions déployées d'HelioLink — **confiance élevée**, fondée sur la correspondance des versions, sur la cohérence de la séquence observée chez deux clients distincts, et sur la description publique du mécanisme.*
>
> *Quarante-trois clients utilisent une version affectée. Le vecteur est accessible ; l'authentification multifacteur limite l'exploitation sans l'empêcher.*
>
> *Ce qui invaliderait : un troisième client affecté utilisant une version non concernée · une cause applicative locale expliquant la dégradation de performance.*

**Ce que la fonction déclenche** — et c'est ici que le CTI rejoint le produit, chapitre 33 :

| Action | Responsable | Délai |
|---|---|---|
| Vérification de la présence de la bibliothèque dans les cinq versions | Développement | 24 h |
| Correctif produit sur les trois versions maintenues | Développement | 6 jours |
| Notification aux 43 clients concernés, avec mesure d'atténuation immédiate | Sécurité produit | 48 h |
| Évaluation de l'obligation de signalement réglementaire | Sécurité produit + juridique | 24 h |

**L'obligation de signalement s'applique** : une vulnérabilité activement exploitée affectant un produit mis sur le marché. La procédure préparée en 2028 est déclenchée pour la première fois en conditions réelles, dans les délais.

**Ce que Claire relève au comité du 30 juillet.** Le rapprochement n'a pas été produit par un outil, ni par une source payante. Il a été produit par **quinze minutes de relecture hebdomadaire** d'une file dont 87 % du contenu est archivé.

> *« Le signalement du 2 juillet avait été archivé. C'est en le relisant qu'il est devenu utile »*, note-t-elle.

**Ce que Nour ajoute**, et qui devient une règle : les signalements archivés ne sont pas supprimés, ils restent consultables pendant douze mois, et la revue hebdomadaire porte sur les trois dernières semaines.

**Livrable de l'épisode.** Le dossier de campagne, avec ses quatre éléments (§19.5) et son critère de clôture — annexe D.

→ **Fin de la Partie IV.** La suite en Partie V, quand il faudra organiser la collecte que ce dossier a rendue nécessaire.

---

> ### 🎓 À ce stade des Parties III et IV, vous savez…
>
> - **transformer une demande floue** en besoin de renseignement formulé, avec un demandeur, une décision et une échéance ;
> - **construire un plan de collecte**, et découvrir que la majorité de vos besoins est déjà couverte ;
> - **écrire ce que vous avez décidé de ne pas suivre** — ce qui prouve qu'un plan existe ;
> - **remplacer le cycle du renseignement** par une file à cinq états, avec archivage motivé ;
> - **raisonner en coût pour l'adversaire** plutôt qu'en gravité technique ;
> - **profiler un acteur inconnu** en quatre paramètres, sans jamais avoir besoin d'un nom ;
> - **lire une cartographie de couverture** et repérer qu'elle suit la facilité, pas le risque ;
> - **regrouper des signalements en campagne** avec deux critères indépendants, et vérifier les quatre conditions qui font passer une menace du général au « nous ».
>
> **Ce que vous ne savez pas encore** : où chercher, dans quel cadre juridique, et à quel prix. C'est l'objet de la Partie V.

---
