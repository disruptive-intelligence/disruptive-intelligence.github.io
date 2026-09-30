---
title: Chapitre 16 — Pourquoi certaines attaques existent
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE IV — Comprendre la menace
  - index.md
---

> Chapitre volontairement resserré. **Objectif unique** : comprendre les incitations qui expliquent les priorités adverses, parce qu'un analyste qui les ignore prédit mal et priorise mal.

## 16.1 Le modèle économique comme grille de lecture

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

## 16.2 La spécialisation des rôles

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

## 16.3 Structure de coût d'une attaque

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

## 16.4 Ce qui fait d'une organisation une cible

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

## 16.5 Comment cette compréhension change une décision défensive

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

## 16.6 📌 Ce que ce chapitre ne traite pas

Par honnêteté sur son périmètre volontairement restreint :

| Hors périmètre | Où l'apprendre |
|---|---|
| Le fonctionnement détaillé des marchés criminels | Publications spécialisées, formations dédiées |
| Les mécanismes de paiement et de blanchiment | Domaine de la lutte anti-blanchiment |
| La cartographie des groupes et de leurs relations | Périmé rapidement, et sans effet sur vos décisions (§13.4) |
| L'économie des vulnérabilités et des courtiers | Sujet réel, mais sans conséquence opérationnelle pour un défenseur |

**La règle appliquée ici** est celle de la doctrine : un développement n'a sa place dans ce cours que s'il change une décision. Les quatre sujets ci-dessus sont intéressants ; ils ne modifient pas ce que vous ferez lundi.

## Synthèse mentale du chapitre 16

La plupart des attaques sont des opérations, avec des coûts et une rentabilité attendue : un adversaire rationnel ne choisit pas la cible la plus intéressante mais celle dont le rapport gain/coût d'accès est le plus favorable. La chaîne est fragmentée entre développeurs, courtiers d'accès et opérateurs, ce qui a trois conséquences — l'entrée et l'exploitation peuvent être séparées de plusieurs mois, le mode opératoire n'identifie pas un acteur unique, et beaucoup d'organisations attaquées n'ont jamais été ciblées mais **disponibles**. Chaque mesure qui augmente le coût d'une étape déplace l'adversaire opportuniste vers une autre cible, ce qui ne vaut plus face à un adversaire déterminé. Trois facteurs font d'une organisation une cible — valeur, accessibilité, visibilité — et le troisième est le plus mal évalué : beaucoup d'organisations se croient discrètes et sont parfaitement identifiables. Enfin, la gravité technique ne dit rien du coût d'exploitation, et c'est le coût qui décide de l'ordre dans lequel les vulnérabilités sont exploitées.

**Trois questions de vérification**

1. Une vulnérabilité de gravité moyenne est exploitée massivement en 48 heures pendant qu'une vulnérabilité maximale reste inexploitée six mois. Expliquez, sans invoquer la chance.
2. Votre organisation demande « pourquoi nous ? » après un incident. Pourquoi cette question n'a-t-elle souvent pas de réponse individuelle ?
3. Vous arbitrez un investissement en sécurité. Reformulez le critère de choix en termes de coût pour l'adversaire.

→ **Chapitre 17 — Les acteurs, par leur logique** : comment raisonner sur un adversaire sans jamais avoir besoin de son nom.

---
