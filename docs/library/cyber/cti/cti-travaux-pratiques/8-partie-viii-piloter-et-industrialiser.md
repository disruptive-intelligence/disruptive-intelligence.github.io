---
title: PARTIE VIII — Piloter et industrialiser
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
chapter: 8
chapters: 8
---

> **Où nous sommes dans la boucle analytique** : segment ⑥ **RETOUR** — celui qui n'existe presque nulle part, et qui décide si une fonction progresse ou vieillit.
>
> Cette partie traite ce qui fait tenir une fonction CTI dans la durée : savoir ce qu'on révèle, mesurer ce qu'on produit, outiller sans se substituer au raisonnement, financer, organiser, et construire depuis zéro.

---

### Chapitre 34 — Votre empreinte informationnelle

#### 34.1 Ce que votre organisation révèle d'elle-même

**Le renversement de perspective** : jusqu'ici, vous collectiez du renseignement. Ce chapitre pose la question inverse — **que collecte-t-on sur vous, et gratuitement ?**

**Ce n'est pas du contre-renseignement au sens strict**, et il ne s'agit pas de secret. Il s'agit de savoir ce qu'un observateur attentif peut établir sans rien faire d'illicite.

| Ce que vous publiez | Ce qu'on en déduit |
|---|---|
| **Offres d'emploi** | Vos technologies, vos outils, vos projets, vos manques |
| Certificats publics | Vos noms d'hôtes, y compris internes |
| Enregistrements de noms | Votre infrastructure, vos environnements de test |
| Communication commerciale | Vos clients, vos secteurs, vos dépendances |
| Interventions en conférence | Votre architecture, vos difficultés |
| Publications de vos équipes | Vos outils, parfois vos configurations |
| **Signatures de messagerie** | Vos fonctions, vos formats de compte, votre organigramme |
| Documents publiés | Métadonnées : logiciels, chemins, noms d'utilisateurs |

**La première ligne est la plus riche et la plus négligée.** Une annonce recherchant « un ingénieur maîtrisant [produit A], [produit B] et [produit C], pour renforcer notre capacité de détection sur [périmètre] » décrit votre pile technique, votre organisation, et l'endroit où vous vous sentez faible.

#### 34.2 Fuites et données divulguées

| Type | Ce qu'il révèle | Ce qu'on peut faire |
|---|---|---|
| Fuite chez un tiers contenant vos identifiants | Vos comptes, vos formats, parfois des mots de passe | Rotation, surveillance (§17.9) |
| Fuite chez un fournisseur | Vos données confiées | Réclamation contractuelle, notification |
| Document interne publié par erreur | Ce qu'il contient, et vos processus | Retrait, évaluation d'impact |
| Dépôt de code exposé | Secrets, architecture, dépendances | **Rotation immédiate des secrets** |

**Le suivi des fuites contenant votre nom de domaine** est l'un des rares besoins que les sources ouvertes ne couvrent pas et que le payant couvre bien (§22.2). C'est aussi celui dont le rapport valeur/prix est le plus favorable.

#### 34.3 ⚠️ Ce que vos propres alertes et publications apprennent à l'adversaire

Le point le plus contre-intuitif du chapitre, esquissé au §28.6.

| Ce que vous faites | Ce que cela révèle |
|---|---|
| Vous partagez un indicateur | Que vous l'avez observé — donc que vous êtes touché ou visé |
| Vous publiez une analyse détaillée | Votre niveau de capacité, et vos sources |
| Vous corrigez une vulnérabilité en urgence | Que vous étiez exposé |
| Vous posez une question précise dans un dispositif | Où vous vous sentez vulnérable |
| **Vous ne dites rien pendant six mois** | Que vous n'observez rien, ou que vous ne pouvez rien dire |
| **Vous bloquez une infrastructure** | Que vous l'avez identifiée — un adversaire attentif le voit |

**Ce qu'il ne faut pas en conclure** : le repli. La valeur reçue d'un dispositif de partage dépasse largement ce risque, et une organisation qui ne partage rien s'exclut d'elle-même.

**Ce qu'il faut en faire** : relire ce qu'on publie en se demandant ce qu'un observateur en déduirait, et arbitrer au cas par cas — c'est exactement la grille du §28.7.

**Le cas du blocage mérite un mot** : un adversaire qui constate que son infrastructure ne répond plus chez une cible sait qu'il a été détecté. C'est un arbitrage réel entre protection immédiate et conservation de la visibilité, et il appartient au responsable de l'incident, pas à l'analyste.

#### 34.4 Mesures réalistes, et ce qui relève de la paranoïa

| Mesure | Coût | Valeur | Verdict |
|---|---|---|---|
| Revoir les offres d'emploi avant publication | Faible | Moyenne | **À faire** |
| Nettoyer les métadonnées des documents publiés | Faible | Moyenne | **À faire** |
| Surveiller les fuites contenant votre domaine | Moyen | **Élevée** | **À faire** |
| Auditer ce qui est visible de vous depuis l'extérieur | Moyen | Élevée | **À faire** (annuel) |
| Restreindre les interventions en conférence | Moyen | Faible | Non — coût culturel disproportionné |
| Anonymiser vos certificats publics | Élevé | Faible | Non |
| Cesser de partager en sectoriel | Faible | **Négative** | **Non** |

**La ligne du milieu marque la frontière.** Au-dessus : des mesures peu coûteuses et utiles. En dessous : des mesures qui dégradent le fonctionnement de l'organisation pour un gain marginal.

🎯 **ET MAINTENANT ?**
*Votre direction, alertée par ce sujet, propose de cesser toute publication technique et toute participation aux conférences. Que répondez-vous ?*
**Réponse** : que le calcul est défavorable. Ce que vos équipes publient est observable par un adversaire — mais il l'obtiendrait par d'autres moyens, et le coût est immédiat et certain : perte d'attractivité au recrutement, isolement de vos équipes, perte d'accès aux réseaux d'entraide qui vous alimentent. Ce que vous proposez à la place : une relecture avant publication, portant sur trois points — pas de configuration précise, pas de nom d'hôte interne, pas de description de vos angles morts. Dix minutes par publication. Vous conservez le bénéfice et vous supprimez l'essentiel du risque.

#### 34.5 🔴 FIL ROUGE — janvier 2031 : l'audit d'empreinte

Nour conduit le premier audit d'empreinte informationnelle d'HELIOMED, en trois jours, sans autre outil qu'un navigateur et les sources publiques.

**Ce qu'elle établit** :

| Élément | Constat |
|---|---|
| Offres d'emploi actives | 7 — dont une décrivant précisément la pile de sécurité et mentionnant « renforcement de notre capacité de détection sur le périmètre industriel » |
| Certificats publics | 43 noms d'hôtes, dont **11 correspondant à des environnements de recette** |
| Métadonnées de documents publiés | 6 documents commerciaux contenant noms d'utilisateurs et chemins internes |
| Interventions en conférence | 2 sur trois ans, sans information sensible |
| Fuites contenant le domaine | **3 jeux distincts**, dont un non identifié jusque-là |
| Mentions publiques de clients | 19 clients nommés dans la communication commerciale |

**Les trois constats qui produisent une action** :

**1. L'offre d'emploi.** Elle indique explicitement où HELIOMED se sait faible — le périmètre industriel, qui est effectivement sa zone aveugle (§18.8). L'annonce est reformulée : les compétences recherchées sont conservées, la mention du périmètre et de la finalité est retirée.

**2. Les onze noms d'hôtes de recette.** Ils apparaissent dans les journaux de certificats publics, et deux d'entre eux résolvent vers des adresses joignables. C'est transmis au dispositif de gestion des vulnérabilités : deux environnements de recette étaient accessibles depuis Internet, ce qu'aucun scan interne n'avait signalé.

**3. La troisième fuite.** Elle contient 22 comptes, dont 4 encore actifs. Rotation immédiate.

**Ce que l'audit ne produit pas** : aucune recommandation de restreindre la communication ou les interventions publiques. Nour l'écrit explicitement dans sa note, par anticipation :

> *Nous ne recommandons aucune restriction de la communication publique ni de la participation aux conférences. Le bénéfice de ces activités — recrutement, réputation, accès aux réseaux professionnels — dépasse largement le risque, et les informations concernées seraient obtenues autrement. Nous recommandons une relecture avant publication, sur trois points précis.*

**Ce que Claire relève** : l'audit a coûté trois jours et produit deux découvertes de sécurité — les environnements de recette exposés et la fuite non identifiée — qu'aucun autre dispositif n'avait remontées.

> *« Nous nous regardions de l'intérieur depuis trois ans. C'est la première fois que nous nous regardons de l'extérieur. »*

**Livrable de l'épisode.** La grille d'audit d'empreinte en six points, reconduite annuellement — annexe L.

→ La suite en 🔴 §35.8, quand il faudra répondre à la question posée en avril 2029.

#### Synthèse mentale du chapitre 34

La question inverse du reste du cours : que collecte-t-on sur vous, gratuitement et licitement ? Les offres d'emploi sont la source la plus riche et la plus négligée — elles décrivent votre pile technique, votre organisation, et l'endroit où vous vous sentez faible. Vos propres actions révèlent aussi : partager un indicateur signale que vous l'avez observé, poser une question précise signale où vous vous sentez vulnérable, et un silence prolongé signale que vous n'observez rien. Il n'en découle pas le repli : la valeur reçue d'un dispositif de partage dépasse largement ce risque, et une organisation qui cesse de publier paie un coût immédiat et certain pour un gain marginal. La frontière des mesures raisonnables passe entre celles qui coûtent peu — relecture, métadonnées, surveillance des fuites, audit annuel — et celles qui dégradent le fonctionnement de l'organisation.

**Trois questions de vérification**

1. Quelle publication de votre organisation décrit le mieux votre pile technique et vos zones de faiblesse ?
2. Votre direction propose de cesser toute publication technique. Que répondez-vous, et que proposez-vous à la place ?
3. Pourquoi le blocage d'une infrastructure adverse est-il un arbitrage, et à qui appartient-il ?

---

### Chapitre 35 — Mesurer le CTI

#### 35.1 Le problème : mesurer une réduction d'incertitude

**La difficulté est réelle et il faut la nommer** : le CTI produit de meilleures décisions. Une meilleure décision ne se voit pas — surtout quand elle consiste à ne rien faire.

**Les trois pièges qui en découlent** :

| Piège | Mécanisme |
|---|---|
| **Mesurer ce qui est facile** | Nombre de rapports, volume de flux, indicateurs ingérés |
| **Ne rien mesurer** | La fonction disparaît au premier arbitrage |
| **Sur-attribuer** | « Nous avons évité un incident » — invérifiable, et cela décrédibilise |

**La posture honnête** : mesurer ce qu'on peut mesurer, dire ce qu'on ne peut pas prouver, et assumer la différence.

#### 35.2 Trois familles d'indicateurs

| Famille | Question | Facilité | Valeur |
|---|---|---|---|
| **Production** | Qu'avons-nous produit ? | **Facile** | **Faible** |
| **Usage** | Qui l'a lu, qui l'a utilisé ? | Moyenne | Élevée |
| **Impact** | Qu'est-ce qui a été décidé différemment ? | **Difficile** | **Très élevée** |

**La corrélation est inverse entre facilité et valeur**, et c'est ce qui explique que la plupart des fonctions mesurent la production.

#### 35.3 ⚠️ Les faux indicateurs

| Indicateur | Pourquoi il ne mesure rien |
|---|---|
| **Nombre de rapports produits** | Mesure l'activité, pas l'utilité. Peut augmenter en dégradant la qualité |
| **Volume d'indicateurs ingérés** | Mesure ce que le fournisseur collecte (§22.4) |
| **Nombre de sources suivies** | Mesure une accumulation (§14.6) |
| **Nombre d'alertes émises** | **Devrait diminuer** avec la maturité (§27.2) |
| Temps de veille quotidien | Mesure une consommation, pas un résultat |
| Nombre de menaces identifiées | Dépend de l'actualité, pas de vous |

⚠️ Le quatrième est le plus pervers : présenté comme un indicateur d'activité, il incite exactement au comportement qui détruit la fonction.

#### 35.4 Mesurer l'usage

**C'est le compromis praticable** : plus facile que l'impact, infiniment plus utile que la production.

**Les trois questions**, envoyées deux semaines après chaque produit — celles du §15.7 :

```
1. L'avez-vous lu ?
2. Avez-vous décidé ou fait quelque chose ?
3. Qu'est-ce qui vous a manqué ?
```

**Ce qu'on en tire** :

| Indicateur | Ce qu'il révèle |
|---|---|
| Taux de lecture par destinataire | Qui vous lit, et qui ne vous lit plus |
| Taux de réponse au questionnaire | Un proxy de l'engagement |
| **Récurrence des manques signalés** | La lacune structurelle de vos produits |

**Le troisième est le plus précieux.** Quatre destinataires signalant la même absence — un coût estimé, un délai, une comparaison — désignent une amélioration à faire, invisible autrement.

#### 35.5 Mesurer l'impact

**Ce qui est mesurable** :

| Indicateur | Comment |
|---|---|
| **Décisions modifiées** | Registre des décisions, avec ce qui aurait été fait sans le renseignement |
| **Ordre de priorisation changé** | Comparaison avant/après (§31.6) |
| **Délai gagné** | Avance sur la publication publique (§22.3, test 3) |
| **Menaces neutralisées documentées** | Les archivages pour neutralisation (§29.9) |
| **Vérifications ayant évité une mobilisation** | Le cas de §8.9 : une journée au lieu de neuf mille euros |

**Ce qui n'est pas mesurable, et qu'il faut renoncer à mesurer** :

- Les incidents évités — invérifiable ;
- La valeur d'une information qui n'a pas servi cette fois ;
- L'effet dissuasif — inexistant en CTI défensif.

✅ **BONNE PRATIQUE (P0) — le registre des décisions**
Deux lignes par produit diffusé : *quelle décision a été prise, et qu'aurait-on fait sans ?* Cinq minutes par semaine. Au bout d'un an, ce registre est **la seule démonstration solide** de l'utilité de la fonction, et il résiste à un arbitrage budgétaire là où aucun indicateur de production ne résiste.

#### 35.6 Le retour d'expérience analytique

**C'est le segment ⑥ de la boucle, et il n'existe presque nulle part.**

**Ce que c'est** : relire ses propres estimations passées et vérifier si elles étaient justes.

**La méthode**, semestrielle, deux heures :

```
1. Reprendre les 10 dernières évaluations calibrées
2. Pour chacune : que s'est-il passé réellement ?
3. L'estimation était-elle juste ? La CONFIANCE était-elle juste ?
4. Quel biais, quelle lacune, quelle méthode a manqué ?
5. Qu'est-ce qui change dans ma pratique ?
```

**La distinction de l'étape 3 est essentielle** : une estimation fausse avec une confiance faible correctement exprimée est un **bon travail**. Une estimation juste avec une confiance excessive est un **mauvais travail** — c'est avoir raison par accident (§7.9).

| | Estimation juste | Estimation fausse |
|---|---|---|
| **Confiance élevée** | ✅ Excellent | ❌ **Le pire cas** — surconfiance |
| **Confiance faible** | ⚠️ Correct, mais la confiance était sous-évaluée | ✅ **Bon travail** — l'incertitude était annoncée |

**Ce que ce tableau change** : on ne juge pas un analyste sur son taux d'exactitude, mais sur **l'alignement entre sa confiance annoncée et sa justesse réelle**. C'est le §2.5, rendu mesurable.

#### 35.7 ✅ Livrable — Le tableau de bord CTI

Une page, trimestrielle, six indicateurs.

| Indicateur | Famille | Valeur |
|---|---|---|
| Besoins actifs, et leur statut | Production | n actifs, n reportés, n abandonnés |
| Produits diffusés, par niveau | Production | n stratégiques, n opérationnels, n tactiques |
| **Taux de lecture et de réponse** | Usage | n % |
| **Décisions modifiées** | Impact | n, avec 3 exemples |
| **Menaces neutralisées documentées** | Impact | n, avec la mesure qui protège |
| **Alignement confiance / justesse** | Retour | Résultat du dernier retour d'expérience |

**Les trois dernières lignes sont celles qui répondent à la question du financeur.** Les trois premières décrivent l'activité ; elles ne suffisent pas.

#### 35.8 🔴 FIL ROUGE — mai 2031 : deux ans après

En avril 2029, Karim Lebrun avait validé le poste de Nour à une condition : *démontrer, à l'issue de la période, quelles décisions ont été prises différemment* (§2.6).

**Le bilan présenté au comité du 14 mai 2031**, à vingt-quatre mois.

**Ce que Nour ne présente pas** : le nombre de produits, le volume d'éléments traités, le nombre de sources suivies.

**Ce qu'elle présente** :

| Indicateur | Valeur sur 24 mois |
|---|---|
| **Décisions documentées comme modifiées par le renseignement** | **31** |
| — dont priorisations de remédiation réordonnées | 14 |
| — dont mobilisations évitées après vérification | 6 |
| — dont actions produit déclenchées | 5 |
| — dont règles de détection écrites | 4 |
| — dont décisions d'investissement éclairées | 2 |
| **Menaces documentées neutralisées par une mesure existante** | 89 |
| **Avance moyenne sur publication publique** *(source sectorielle)* | 4,1 jours |
| Alignement confiance / justesse *(dernier retour d'expérience)* | 8 sur 10 estimations correctement calibrées |

**Les deux chiffres qui emportent la décision**, et ce ne sont pas ceux attendus :

**Les 6 mobilisations évitées.** Chacune est chiffrée. La première — juillet 2029 — a coûté 9 000 € parce qu'elle n'a pas été évitée. Les six suivantes ont été évitées par vérification, pour un coût cumulé estimé de deux journées-homme.

**Les 89 neutralisations documentées.** Elles ne prouvent pas que le CTI a protégé quoi que ce soit — c'est le dispositif de sécurité qui protège. Mais elles **documentent que les mesures en place fonctionnent contre des menaces réelles**, ce qu'aucun autre dispositif ne produisait.

**La question de Karim Lebrun**, plus fine que celle de 2029 :

> *« Sur les 31 décisions, combien auraient été prises correctement sans vous ? »*

**La réponse de Nour**, qu'elle a préparée et qui est honnête :

> *Sur les 31, je peux démontrer que 19 auraient été différentes. Pour 8, je ne peux rien démontrer — elles auraient probablement été prises de la même façon, plus tard. Pour 4, la question n'a pas de réponse.*
>
> *Ce que je peux affirmer avec certitude, c'est que les 89 neutralisations n'auraient été documentées par personne. Et que sans elles, nous ne saurions pas ce qui fonctionne.*

**La décision du comité** : la fonction est pérennisée, et un second poste est ouvert pour 2032 — orienté sur le renseignement produit, qui est le besoin dont la croissance est la plus forte.

**Ce que Claire écrit en conclusion de la note** :

> *Le meilleur indicateur de cette fonction n'est pas dans le tableau. C'est qu'en deux ans, plus personne ne demande « pourquoi nous ? ». On demande « qu'est-ce qui est accessible ». Ce changement de question vaut les trente et une décisions.*

**Livrable de l'épisode.** Le tableau de bord en six indicateurs, et le registre des décisions tenu depuis avril 2029 — annexe K.

→ La suite en 🔴 §37.6, quand il faudra chiffrer ce que tout cela coûte.

#### Synthèse mentale du chapitre 35

Le CTI produit de meilleures décisions, et une meilleure décision ne se voit pas — surtout quand elle consiste à ne rien faire. Trois familles d'indicateurs existent, et la corrélation entre facilité et valeur est inverse : la production est facile à mesurer et sans valeur, l'impact est difficile et décisif. Le nombre d'alertes émises est le faux indicateur le plus pervers, parce qu'il devrait diminuer avec la maturité. Mesurer l'usage est le compromis praticable, et sa donnée la plus précieuse est la récurrence des manques signalés — quatre destinataires signalant la même absence désignent une lacune invisible autrement. Le registre des décisions, deux lignes par produit, est la seule démonstration qui résiste à un arbitrage budgétaire. Enfin, le retour d'expérience analytique juge l'alignement entre confiance annoncée et justesse réelle, pas le taux d'exactitude : une estimation fausse avec une confiance faible correctement exprimée est un bon travail ; une estimation juste avec une confiance excessive est le pire cas.

**Trois questions de vérification**

1. Pourquoi le nombre d'alertes émises est-il un indicateur pervers, et que devrait-il faire avec la maturité ?
2. Un financeur vous demande de démontrer l'utilité de la fonction. Que présentez-vous, et que ne présentez-vous surtout pas ?
3. Deux analystes : l'un s'est trompé en annonçant une confiance faible, l'autre a eu raison en annonçant une confiance élevée non justifiée. Lequel a bien travaillé ?

---

### Chapitre 36 — Les outils

> Chapitre volontairement placé en trente-sixième position sur quarante, et volontairement resserré. **Vous savez désormais pourquoi ces outils existent** — c'est ce qui permet de les traiter en quelques pages plutôt qu'en un tiers du cours.

#### 36.1 Ce qu'une plateforme de renseignement fait, et ne fait pas

| Elle fait | Elle ne fait pas |
|---|---|
| Ingérer, normaliser, dédoublonner | **Décider ce qui vous concerne** |
| Enrichir automatiquement | Évaluer une source (§10) |
| Conserver un historique | Produire un jugement (§11) |
| Diffuser vers d'autres outils | Formuler un besoin (§14) |
| Gérer des marquages de diffusion | Écrire pour un destinataire (§26) |

**La colonne de droite contient l'essentiel du métier.** Une plateforme est un outil de gestion de matière première ; elle ne remplace aucun des chapitres 4 à 13.

**Ce qui justifie d'en avoir une** : le volume. En dessous d'un certain seuil — quelques centaines d'éléments par mois — un tableur et une discipline suffisent, et coûtent infiniment moins cher à maintenir.

#### 36.2 Les formats structurés

**Pourquoi structurer** : permettre l'échange machine à machine et l'automatisation. C'est tout.

| Format | Rôle | Ce qu'il exprime bien | Ce qu'il exprime mal |
|---|---|---|---|
| **STIX** | Représentation d'objets de renseignement et de leurs relations | Indicateurs, campagnes, acteurs, relations | **Le raisonnement, la nuance, le niveau de confiance argumenté** |
| **TAXII** | Protocole d'échange | Collections, canaux, abonnements | — |
| **Formats d'analyste alternatifs** | Représentation de contexte et d'opinion | L'appréciation, la note d'analyste | Standardisation moindre |

**La limite structurelle à retenir**, et elle vaut au-delà de tout format particulier :

> **Un format structuré transporte des objets, pas des jugements.** La phrase *« nous estimons probable X — confiance moyenne, parce que les deux sources ne sont pas indépendantes »* ne se met dans aucun champ. Elle se transporte en prose, dans un produit écrit.

**La conséquence pratique** : les formats structurés servent le niveau tactique (§3.3) et le partage automatisé. Ils ne servent pas les niveaux opérationnel et stratégique, qui restent affaire d'écriture.

#### 36.3 Collecte, normalisation, déduplication, enrichissement

**Ce qui s'automatise bien** :

| Tâche | Gain |
|---|---|
| Ingérer plusieurs formats | Élevé |
| Dédoublonner | Élevé |
| Enrichir techniquement — résolution, réputation, géographie | Moyen |
| **Rapprocher avec l'inventaire** | **Très élevé — et c'est le plus négligé** |
| Diffuser vers la détection | Élevé |
| Appliquer une date d'expiration | **Élevé, et rarement fait** (§30.6) |

**La quatrième ligne est celle qui produit le plus de valeur** : rapprocher automatiquement un élément entrant avec l'inventaire répond au nœud ① de l'arbre d'exploitation (§29.2) — *est-ce applicable chez nous ?* — qui est la question la plus fréquente et la plus mécanique du métier.

#### 36.4 ⚠️ Automatiser un raisonnement absent

**Le risque central du chapitre.**

| Ce qu'on automatise | Ce qui se passe si le raisonnement manque |
|---|---|
| L'ingestion | On accumule (§14.6) |
| Le blocage automatique | On bloque des ressources légitimes (§24.5) |
| La diffusion automatique | On sature les destinataires |
| Le scoring automatique | On prend un chiffre pour un jugement |

**La formulation qui résume** :

> **Un outil accélère ce que vous faites. Si ce que vous faites est mal fondé, il accélère l'erreur.**

C'est la même conclusion qu'au cours MCS, et pour la même raison : l'automatisation ne crée aucune capacité de décision.

#### 36.5 L'assistance automatisée à l'analyse

**Les usages réellement utiles aujourd'hui, dans le périmètre de ce cours** :

| Usage | Valeur | Précaution |
|---|---|---|
| Résumer un rapport long | Élevée | Vérifier les affirmations reprises **à la source** |
| Traduire | Élevée | Attention aux nuances de calibrage |
| Reformuler pour un destinataire | Moyenne | La conclusion ne doit pas bouger (§26.1) |
| Générer des hypothèses alternatives | **Élevée** | Contre le biais de confirmation, c'est un usage pertinent |
| Extraire des indicateurs d'un texte | Élevée | Vérifier le contexte et la date |
| Rédiger une première version | Moyenne | La relecture reste entière |

**Le risque spécifique**, et il faut le nommer précisément :

> **Une sortie plausible mais fausse est plus dangereuse qu'une absence de réponse, parce qu'elle ne déclenche aucune vérification.**

Une version affectée inexacte, une source inventée, une affirmation attribuée à tort à un rapport : ces erreurs ont la forme d'une information correcte. Elles passent les relectures rapides.

✅ **BONNE PRATIQUE (P0)** — Toute affirmation issue d'une assistance automatisée et destinée à fonder une décision est **vérifiée à la source**. Le statut du §4.6 s'applique intégralement : une sortie d'outil n'est pas un fait, c'est une source — et une source dont la chaîne de provenance est opaque.

⚠️ **Le point aveugle** : ces outils sont particulièrement enclins à produire des synthèses cohérentes à partir de sources circulaires, parce qu'ils ne distinguent pas trois reprises d'une source unique de trois observations indépendantes. Le §10.4 s'applique avec une acuité accrue.

#### 36.6 📌 Coût d'intégration et dette d'outillage

| Coût | Ordre de grandeur |
|---|---|
| Licence | Visible, souvent le plus faible |
| **Intégration initiale** | Souvent supérieur à la licence |
| **Maintenance des connecteurs** | Récurrent, croissant avec le nombre de sources |
| Formation | Ponctuel |
| **Migration en cas de changement** | Élevé, et l'historique est rarement portable |

**La dette d'outillage** : chaque connecteur, chaque règle de normalisation, chaque automatisme est un actif à maintenir. Une chaîne non maintenue casse silencieusement — et personne ne s'en aperçoit avant qu'une information importante ne soit pas passée.

✅ **BONNE PRATIQUE (P1)** — Surveillez vos automatismes : date de dernière exécution réussie, volume traité, taux d'échec. Un automatisme arrêté est plus dangereux qu'un processus manuel, parce qu'on croit qu'il fonctionne.

🎯 **ET MAINTENANT ?**
*On vous propose une plateforme de renseignement à 45 k€ par an. Votre fonction traite environ 200 éléments par mois. Que répondez-vous ?*
**Réponse** : que le volume ne justifie pas l'outil. Deux cents éléments par mois se gèrent dans un tableur structuré avec cinq états (§15.4) et un rapprochement mensuel avec l'inventaire. Ce que vous demandez à la place, si le budget existe : la surveillance des fuites et des mentions de vos produits (§22.2), qui couvre un besoin que rien d'autre ne couvre. La plateforme deviendra justifiée quand le volume, le nombre de sources et le besoin d'échange automatisé l'imposeront — et vous saurez le dire, parce que vous aurez mesuré.

#### Synthèse mentale du chapitre 36

Une plateforme ingère, normalise, dédoublonne et diffuse ; elle ne décide pas ce qui vous concerne, n'évalue pas une source et ne produit pas de jugement — la colonne de ce qu'elle ne fait pas contient l'essentiel du métier. Un format structuré transporte des objets, pas des jugements : la phrase qui exprime une confiance argumentée ne se met dans aucun champ, et c'est pourquoi les formats servent le tactique et pas l'opérationnel. Ce qui s'automatise le mieux et se fait le moins, c'est le rapprochement avec l'inventaire — la question la plus fréquente et la plus mécanique du métier. Un outil accélère ce que vous faites, donc il accélère l'erreur si le raisonnement manque. Enfin, l'assistance automatisée produit un risque spécifique : une sortie plausible mais fausse ne déclenche aucune vérification, et ces outils sont particulièrement enclins à synthétiser des sources circulaires en ignorant leur dépendance.

**Trois questions de vérification**

1. Votre organisation traite deux cents éléments par mois. Une plateforme se justifie-t-elle ? Que demandez-vous à la place ?
2. Pourquoi un format structuré ne peut-il pas transporter un jugement analytique ?
3. Quel risque spécifique présente une assistance automatisée face à des sources circulaires ?

---

### Chapitre 37 — Économie de la fonction

#### 37.1 Chiffrer une fonction CTI

**Les cinq postes**, dont deux sont presque toujours omis :

| Poste | Contenu | Omis ? |
|---|---|---|
| Personnel | Le poste, ou la fraction de poste | Non |
| Sources payantes | Abonnements, adhésions | Non |
| Outillage | Plateforme, connecteurs, stockage | Non |
| **Intégration et maintenance** | Le coût récurrent de la chaîne | **Souvent** |
| **Le temps des destinataires** | Lecture, réunions, sollicitations | **Presque toujours** |

**Le cinquième mérite un calcul** : une fonction qui diffuse quatre produits par mois à sept destinataires, chacun y consacrant vingt minutes, consomme environ **quarante-cinq heures par an** de temps de cadres. Ce coût est réel, invisible, et il justifie à lui seul les chapitres 25 et 26 — un produit mal écrit coûte plus cher qu'il ne paraît.

#### 37.2 Construire ou acheter

| Critère | Plutôt construire | Plutôt acheter |
|---|---|---|
| Le besoin est **spécifique à votre contexte** | ✅ | |
| Le besoin est **générique** | | ✅ |
| L'information exige un **accès non public** | | ✅ |
| Vous disposez de la **compétence** | ✅ | |
| Le besoin est **durable** | ✅ | |
| Le besoin est **ponctuel** | | ✅ |

**La règle qui découle du chapitre 2** : ce qui relève de la **connaissance** s'achète ; ce qui relève du **renseignement** ne s'achète pas, parce qu'il suppose votre contexte. Une organisation qui achète du renseignement achète en réalité de la connaissance et devra faire le reste elle-même.

#### 37.3 Le coût caché de l'attention

**Développement du §37.1, cinquième poste.**

| Ce qui consomme l'attention | Effet |
|---|---|
| Un produit trop long | Multiplié par le nombre de destinataires |
| Un produit envoyé au mauvais destinataire | Coût pur, valeur nulle |
| Une alerte injustifiée | Coût élevé, plus l'érosion du crédit (§27.2) |
| Une question mal formulée | Le destinataire doit deviner ce qu'on attend |

**Ce que cela implique** : réduire la longueur, cibler les destinataires et restreindre les alertes ne sont pas des raffinements de style. Ce sont des **mesures d'économie**, chiffrables.

#### 37.4 Défendre un budget sur une fonction à impact difficilement prouvable

**Ce qui ne fonctionne pas** :

| Argument | Pourquoi il échoue |
|---|---|
| « Nous avons évité un incident » | Invérifiable, et cela décrédibilise |
| « Tout le monde en fait » | Ne répond à aucune question |
| « La menace augmente » | Vrai, général, et sans conséquence budgétaire |
| Le volume produit | §35.3 |

**Ce qui fonctionne**, dans cet ordre :

1. **Les décisions modifiées**, avec exemples nommés (§35.5).
2. **Les mobilisations évitées**, chiffrées — c'est l'argument le plus concret, parce qu'il compare un coût évité à un coût réel.
3. **Les menaces neutralisées documentées** — elles démontrent que les investissements passés fonctionnent, ce qui sert au-delà du CTI.
4. **L'avance obtenue**, en jours, sur les sources publiques.

**L'argument le plus solide n'est pas économique.** Il est le suivant : *sans cette fonction, l'organisation ne saurait pas ce qu'elle ignore.* Il ne se chiffre pas, et il se comprend.

#### 37.5 📌 Ce qu'une fonction CTI ne fera jamais économiser

Par honnêteté, et parce qu'un argumentaire qui promet trop se retourne :

- Elle ne réduit pas le budget de sécurité : elle en améliore l'allocation ;
- Elle ne remplace ni la détection, ni la remédiation, ni l'architecture ;
- Elle ne diminue pas le nombre d'incidents de façon démontrable ;
- Elle ne se substitue pas à une capacité de réponse.

**Ce qu'elle fait** : elle rend les mêmes moyens plus efficaces, en les orientant. Le §31.6 en est la démonstration la plus nette — même capacité, ordre différent, délai divisé par cinq.

#### 37.6 🔴 FIL ROUGE — juin 2031 : ce que ça coûte

Après le bilan à vingt-quatre mois (§35.8), Karim Lebrun demande le chiffrage complet — pas seulement le poste, mais tout ce que la fonction consomme.

**Le calcul, sur douze mois** :

| Poste | Montant estimé |
|---|---|
| Poste de Nour, charges comprises | Le principal |
| Adhésion au dispositif sectoriel | Modeste |
| Souscription commerciale (fournisseur B) | 19 k€ |
| Outillage | Néant — un tableur structuré et l'existant |
| Intégration et maintenance | ≈ 4 jours-homme/an |
| **Temps des destinataires** | **≈ 52 heures/an**, soit environ 1,5 semaine cumulée |

**Ce que le poste « temps des destinataires » provoque.** Karim Lebrun ne l'avait jamais vu chiffré. Sa réaction n'est pas celle attendue :

> *« Cinquante-deux heures de cadres pour trente et une décisions, ça me paraît très bon marché. Ce qui m'intéresse, c'est de savoir si ces cinquante-deux heures sont bien réparties. »*

**La question déclenche une analyse** : qui consomme les cinquante-deux heures ?

| Destinataire | Temps annuel estimé | Décisions produites |
|---|---|---|
| Malik Ferhaoui (MCS) | 14 h | **14** |
| Référent détection | 11 h | 4 |
| Yann Prigent (produit) | 9 h | 5 |
| Claire Nadeau (RSSI) | 8 h | 6 |
| Sonia Weber (DSI) | 5 h | 2 |
| **Comité de direction** | **9 h** | **0** |
| Dr Hélène Fabre | 0 h | 0 |

**La ligne du comité de direction** : neuf heures cumulées, zéro décision documentée. Les produits stratégiques — quatre en deux ans — ont été lus, et n'ont modifié aucun arbitrage.

**Ce que Nour en conclut**, sans se défendre :

> *Le besoin B-04, orientation des investissements, est le seul de mes besoins qui n'a jamais produit de décision. J'ai mis vingt-quatre mois à l'admettre. Soit je le sers correctement, soit je l'abandonne — mais je ne peux pas continuer à produire quatre notes par an que personne n'utilise.*

**La décision prise** : le besoin B-04 est **reformulé une dernière fois**, avec une échéance ferme calée sur le calendrier budgétaire et un format différent — une présentation orale de quinze minutes en comité, avec une question explicite, plutôt qu'une note écrite. Si aucune décision n'en résulte en 2032, il est abandonné et l'annexe des besoins non couverts le mentionnera.

**Ce que Claire écrit au compte rendu** :

> *« Nous avons passé deux ans à démontrer ce que la fonction produit. Le chiffrage nous a appris ce qu'elle ne produit pas. C'est aussi utile. »*

**Livrable de l'épisode.** Le chiffrage complet en six postes, dont le temps des destinataires, et son croisement avec les décisions produites — annexe K.

→ La suite en 🔴 §38.5, quand la fonction devra décider où elle se rattache.

#### Synthèse mentale du chapitre 37

Cinq postes composent le coût d'une fonction CTI, et deux sont presque toujours omis : la maintenance de la chaîne, et surtout **le temps des destinataires** — quarante à cinquante heures de cadres par an dans une organisation moyenne, ce qui fait de la brièveté et du ciblage des mesures d'économie chiffrables plutôt que des raffinements de style. Ce qui relève de la connaissance s'achète, ce qui relève du renseignement ne s'achète pas, parce qu'il suppose votre contexte. Défendre un budget se fait par les décisions modifiées et les mobilisations évitées chiffrées, jamais par les incidents évités — invérifiables et décrédibilisants. Une fonction CTI ne réduit pas le budget de sécurité, elle en améliore l'allocation : mêmes moyens, ordre différent. Enfin, le chiffrage apprend autant sur ce que la fonction ne produit pas que sur ce qu'elle produit — un besoin qui consomme du temps sans jamais produire de décision doit être servi autrement ou abandonné.

**Trois questions de vérification**

1. Quel poste de coût est presque toujours omis dans le chiffrage d'une fonction CTI, et pourquoi justifie-t-il l'exigence de brièveté ?
2. Pourquoi « nous avons évité un incident » est-il un mauvais argument budgétaire ?
3. Un destinataire consomme neuf heures par an et ne produit aucune décision. Que faites-vous, et en combien de temps devriez-vous l'avoir vu ?

---

### Chapitre 38 — Organiser la fonction

#### 38.1 Où rattacher le CTI

| Rattachement | Avantage | Risque |
|---|---|---|
| **RSSI** | Proximité des besoins, légitimité transverse | Peut devenir un service du seul RSSI |
| **Centre opérationnel de sécurité** | Proximité de la détection, boucle courte | **Dérive vers le tactique uniquement** |
| **Équipe de réponse à incident** | Utile en crise | Absorption par l'opérationnel, pas de production régulière |
| **Direction des risques** | Vision stratégique | Éloignement du terrain, produits trop généraux |
| **Fonction autonome** | Indépendance de jugement | Isolement, difficulté à exister |

**Le critère de choix**, plus utile que le rattachement lui-même : **d'où viennent les besoins ?** Une fonction rattachée à un service qui n'exprime qu'un type de besoin produira un seul type de renseignement.

⚠️ **Le risque le plus fréquent est le deuxième** : rattachée à la détection, une fonction CTI devient un service d'alimentation en indicateurs — utile, mais qui abandonne les niveaux opérationnel et stratégique, c'est-à-dire l'essentiel de sa valeur (§3.4).

#### 38.2 Une personne, une équipe, un service partagé

| Configuration | Ce qu'elle permet | Ce qu'elle exige |
|---|---|---|
| **Une fraction de poste** | Un niveau, quelques besoins | Un périmètre déclaré (§3.7) |
| **Une personne** | Deux niveaux, quatre à six besoins | Une relecture externe (§12.5) |
| **Deux à trois personnes** | Les trois niveaux, spécialisation possible | Une coordination, un partage de la file |
| **Service partagé entre entités** | Mutualisation des coûts | Une gouvernance des priorités entre entités |

**Le seuil qui compte** : à partir de deux personnes, la revue par les pairs devient interne et le chapitre 12 s'applique pleinement. En dessous, les substituts du §12.5 sont indispensables — ce n'est pas optionnel.

#### 38.3 Les interfaces

**Ce qui doit être établi**, avec chaque fonction consommatrice :

| Interface | Ce qui doit exister | Fréquence |
|---|---|---|
| **Détection** | Un canal, un format (§30.7), un point régulier | Hebdomadaire |
| **Gestion des vulnérabilités** | Un format de contribution (§31.6) | Au rythme des campagnes |
| **Réponse à incident** | Une place en cellule, une procédure (§32) | À l'incident |
| **Produit** | Un canal, et le lien avec l'obligation de signalement | Continue |
| **Direction** | Un rendez-vous, pas des envois | Trimestrielle |
| **Juridique et protection des données** | Un référent identifié | À la demande, et au plan de collecte |

**La ligne « direction » mérite un développement.** Un produit stratégique envoyé par écrit a une audience faible ; le même contenu présenté en quinze minutes, avec une question explicite, produit une décision. C'est ce qu'HELIOMED découvre au §37.6.

#### 38.4 ⚠️ L'anti-pattern : le CTI qui devient une veille documentaire

**Le mécanisme**, en quatre étapes :

```
1. La fonction est créée sans besoins formulés
2. Elle produit une lettre d'information périodique, faute de mieux
3. La lettre devient l'attendu — on la demande, on la mesure
4. La fonction est jugée sur sa régularité, plus sur son utilité
```

**Les signes**, tous observables :

| Signe | Ce qu'il indique |
|---|---|
| Le produit principal est périodique et non déclenché | La production suit le calendrier, pas le besoin |
| Le contenu est le même que ce qu'on trouve ailleurs | §2.3 — c'est de la connaissance redistribuée |
| Personne ne pose de question à la fonction | Elle n'est pas perçue comme utile |
| Le succès se mesure en régularité | §35.3 |

**Le remède**, et il est difficile : **arrêter la lettre**. Une fonction qui produit un livrable périodique attendu ne peut pas s'en libérer par ajout ; elle doit l'interrompre et le remplacer par des produits déclenchés par des besoins.

#### 38.5 🔴 FIL ROUGE — septembre 2031 : où se rattache la fonction

L'ouverture d'un second poste pour 2032 (§35.8) pose une question restée implicite : **où la fonction se rattache-t-elle ?**

**La situation depuis 2029** : Nour est rattachée à Claire Nadeau, RSSI. Le rattachement n'a jamais été formalisé — il résultait du recrutement.

**Les trois options examinées** :

| Option | Argument pour | Argument contre |
|---|---|---|
| Rattachement au RSSI | Statu quo, ça fonctionne | Les besoins produit et détection passent par un intermédiaire |
| Rattachement à la détection | Boucle courte avec le principal consommateur tactique | **Perte des niveaux opérationnel et stratégique** |
| Fonction autonome sous la DSI | Indépendance de jugement, accès direct aux métiers | Isolement, et Nour serait seule à porter la légitimité |

**Ce qui tranche**, et ce n'est pas un argument d'organigramme. Nour reprend son registre des besoins :

| Besoin | Demandeur | Décisions produites en 24 mois |
|---|---|---|
| B-01 priorisation | MCS | **14** |
| B-02 mentions produit | Produit | 5 |
| B-03 ce qui arrive aux pairs | RSSI | 6 |
| B-05 écart de détection | Détection | 4 |
| B-07 fuites | RSSI | 4 |
| B-04 orientation investissement | DSI | **0** |

**Les besoins viennent de cinq services différents.** Un rattachement à l'un d'eux privilégierait structurellement ses besoins.

**La décision retenue** : maintien du rattachement au RSSI, **avec deux mesures correctives** :

1. **Un comité de priorisation trimestriel**, réunissant les cinq demandeurs, qui arbitre les besoins actifs et la capacité allouée à chacun. Ce n'est pas Claire qui décide seule de ce que la fonction traite.
2. **Un accès direct** de Nour aux demandeurs, sans passage par la hiérarchie — formalisé, pour éviter que ce soit perçu comme un contournement.

**Ce que Sonia Weber relève**, et qui est le point de l'épisode :

> *« Le problème n'était pas le rattachement. C'était que personne n'arbitrait entre les besoins, sauf Nour elle-même — et elle arbitrait forcément vers ceux qui lui répondaient. »*

**C'est le diagnostic exact du besoin B-04** : il n'a produit aucune décision parce qu'il était le plus coûteux à servir et le moins relancé, donc systématiquement dépriorisé par une analyste qui ne pouvait pas arbitrer contre elle-même.

**Livrable de l'épisode.** La charte de la fonction : rattachement, comité de priorisation trimestriel, accès direct, et règle d'arbitrage de la capacité — annexe D.

#### Synthèse mentale du chapitre 38

Le critère de rattachement n'est pas l'organigramme mais l'origine des besoins : une fonction rattachée à un service qui n'exprime qu'un type de besoin produira un seul type de renseignement. Le risque le plus fréquent est le rattachement à la détection, qui transforme le CTI en service d'alimentation en indicateurs et lui fait abandonner les niveaux où se situe l'essentiel de sa valeur. En dessous de deux personnes, les substituts à la revue par les pairs ne sont pas optionnels. Un produit stratégique envoyé par écrit a une audience faible ; présenté en quinze minutes avec une question explicite, il produit une décision. Enfin, l'anti-pattern de la veille documentaire ne se corrige pas par ajout : il faut interrompre le livrable périodique, et c'est difficile parce qu'il est devenu l'attendu.

**Trois questions de vérification**

1. Vos besoins viennent de cinq services différents. Quel critère utilisez-vous pour décider du rattachement, et quelle mesure corrective ajoutez-vous ?
2. Pourquoi le rattachement à la détection est-il le risque le plus fréquent, et que perd-on ?
3. Un besoin ne produit aucune décision depuis deux ans. Quelle est l'explication la plus probable, et pourquoi l'analyste seul ne peut-il pas la corriger ?

---

### Chapitre 39 — Le CTI dans une petite organisation

> **Ce chapitre s'adresse à la majorité des lecteurs.** La plupart des organisations n'auront jamais une fonction CTI à temps plein. Ce qui suit décrit ce qui est réellement faisable, et ce à quoi il faut renoncer explicitement.

#### 39.1 Ce qui est faisable à temps partiel

**Le budget réaliste** : deux à quatre heures par semaine, pour quelqu'un qui a un autre métier.

**Ce que ce budget permet** :

| Activité | Temps hebdomadaire | Faisable ? |
|---|---|---|
| Veille sur quatre sources (§21.6) | 1 h 40 | ✅ |
| Rapprochement avec l'inventaire | 30 min | ✅ |
| Un produit court par mois | 30 min amorti | ✅ |
| Répondre aux questions posées | Variable | ✅ |
| Une revue hebdomadaire de la file | 15 min | ✅ |
| **Total** | **≈ 3 h** | |

**Ce que ce budget ne permet pas** : l'analyse structurée systématique, le suivi de campagnes, le pivot d'infrastructure, la production stratégique, la cartographie de couverture.

#### 39.2 Les trois sources qui suffisent

| Source | Temps | Ce qu'elle couvre |
|---|---|---|
| **Catalogue d'exploitation avérée** | 5 min/jour | Le signal le plus fort |
| **Avis des éditeurs de vos 3-4 produits critiques** | 10 min/jour | La source de vérité sur ce qui vous affecte |
| **Bulletins de votre centre de réponse national** | 15 min/semaine | Contexte, alertes, gratuité |

**Une quatrième si votre secteur en dispose** : un dispositif de partage sectoriel. C'est la seule source qui vous dira ce qui vise vos pairs, et son coût est une adhésion.

**Ce qu'il faut abandonner sans regret** : les réseaux professionnels comme source, les publications de chercheurs suivies systématiquement, les flux commerciaux généralistes.

#### 39.3 Le produit minimal viable

**Une page par mois**, cinq sections :

```
CE QUI NOUS CONCERNE CE MOIS-CI
    2 à 4 éléments maximum, avec l'action associée

CE QUE NOUS AVONS VÉRIFIÉ ET QUI NE NOUS CONCERNE PAS
    3 à 5 lignes — c'est la section qui rassure et qui prouve le travail

CE QUE NOUS SURVEILLONS
    1 à 2 éléments, avec ce qui déclencherait une action

CE QUE NOUS NE SAVONS PAS
    1 à 2 lignes

CE QUE NOUS DEMANDONS
    Une décision, ou rien — et le dire
```

**La deuxième section est la plus importante dans une petite structure**, parce qu'elle est celle qui démontre que le travail a lieu. Le §29.9 en est la version développée : *ce contre quoi nous sommes protégés*.

#### 39.4 Ce à quoi renoncer, et comment l'assumer

**La règle** : ce qui n'est pas fait doit être **écrit**, avec son motif.

| Renoncement | Formulation |
|---|---|
| Le niveau stratégique | *« Nous ne produisons pas d'analyse prospective. Nous nous appuierons sur des publications sectorielles en cas de besoin. »* |
| Le suivi de campagnes | *« Nous traitons les éléments à l'unité. Le regroupement en campagnes n'est pas assuré. »* |
| L'infrastructure adverse | *« Nous vérifions la fraîcheur et la colocation avant tout blocage. Nous ne conduisons pas de travail de pivot. »* |
| La cartographie de couverture | *« Non réalisée. Nous priorisons la détection sur les incidents réels. »* |
| Le partage actif | *« Nous consommons le dispositif sectoriel. Nous partageons les confirmations et infirmations. »* |

**Pourquoi l'écrire** : c'est le même principe que les périmètres déclarés non couverts du cours MCS. Un renoncement écrit est une décision ; un renoncement tacite est une lacune que personne ne verra jusqu'à l'incident.

#### 39.5 Les quatre gestes qui produisent le plus, dans l'ordre

**Si vous ne deviez faire que quatre choses** :

| # | Geste | Temps | Effet |
|---|---|---|---|
| **1** | Rapprocher le catalogue d'exploitation avérée avec votre inventaire | 15 min/jour | Le meilleur rapport effort/valeur du domaine |
| **2** | Relire vos incidents des 18 derniers mois | 2 jours, une fois | Vos angles morts réels (§23.5) |
| **3** | Exploiter vos tentatives d'exploitation bloquées | 30 min/mois | Ce qui est testé contre vous (§23.3) |
| **4** | Adhérer à un dispositif sectoriel et poser des questions | 30 min/semaine | L'antériorité, et l'entraide |

**Aucun des quatre ne coûte d'argent.** Trois d'entre eux exploitent des données que vous possédez déjà.

🎯 **ET MAINTENANT ?**
*Vous êtes administrateur système dans une organisation de 120 personnes. On vous demande de « faire du CTI ». Vous avez trois heures par semaine. Par quoi commencez-vous ?*
**Réponse** : pas par une source. Par **deux questions posées à trois personnes** — le dirigeant, le responsable métier principal, et vous-même : *quelles décisions devez-vous prendre où il vous manque quelque chose ?* et *qu'est-ce qui vous a surpris cette année ?* Une heure au total. Vous en tirerez deux ou trois besoins réels. Ensuite seulement, vous choisissez les sources qui y répondent — et il y en aura moins que vous ne pensiez. Commencer par les sources, c'est garantir de consommer vos trois heures sans jamais produire de décision.

#### 39.6 🔴 FIL ROUGE — le cas d'une PME cliente d'HELIOMED

*Cet épisode sort du fil rouge principal pour illustrer le chapitre.*

En 2031, HELIOMED propose à ses clients un modèle de dispositif CTI minimal, à la demande de plusieurs d'entre eux. L'un des premiers à l'adopter est un fabricant de matériel médical de 140 personnes, sans fonction de sécurité dédiée.

**Ce qui est mis en place**, par un administrateur système à trois heures par semaine :

| Élément | Mise en œuvre |
|---|---|
| Besoins | **2** — priorisation des correctifs · ce qui vise les fournisseurs du secteur |
| Sources | 3 gratuites + adhésion au dispositif sectoriel |
| Produit | Une page par mois, cinq sections |
| Destinataires | 2 — le dirigeant, le responsable production |
| Renoncements écrits | 5 |

**Le bilan à douze mois** :

| Indicateur | Valeur |
|---|---|
| Produits diffusés | 11 |
| Décisions documentées | **6** |
| — dont priorisations de correctifs réordonnées | 4 |
| — dont un fournisseur écarté après signalement sectoriel | 1 |
| — dont un investissement en authentification renforcée | 1 |
| Alertes émises | **1** |
| Coût direct | Adhésion sectorielle uniquement |

**Ce que l'administrateur écrit dans son bilan**, transmis à HELIOMED :

> *La section « ce que nous avons vérifié et qui ne nous concerne pas » est celle que mon dirigeant lit en premier. Il m'a dit que c'était la première fois qu'on lui expliquait pourquoi il ne fallait pas s'inquiéter.*

**Ce que Nour en tire pour le cours qu'elle finit par écrire** :

> *Six décisions en un an, pour trois heures par semaine et le prix d'une adhésion. Le rapport est meilleur que le nôtre. Ce n'est pas parce qu'il est meilleur analyste — c'est parce qu'il a deux besoins et qu'il les sert.*

**Livrable de l'épisode.** Le modèle de dispositif CTI minimal — deux besoins, trois sources, une page par mois, cinq renoncements écrits — annexe D.

#### Synthèse mentale du chapitre 39

Deux à quatre heures par semaine suffisent à couvrir la veille sur quatre sources, le rapprochement avec l'inventaire, un produit mensuel et une revue de file — et ne suffisent pas à l'analyse structurée systématique, au suivi de campagnes ni à la production stratégique. Trois sources gratuites couvrent l'essentiel, plus une adhésion sectorielle si le secteur en dispose. Le produit minimal tient en une page et cinq sections, dont la plus importante en petite structure est *ce que nous avons vérifié et qui ne nous concerne pas* — elle démontre que le travail a lieu. Ce à quoi on renonce doit être écrit avec son motif, sinon c'est une lacune et non une décision. Enfin, les quatre gestes au meilleur rendement ne coûtent aucun argent et trois d'entre eux exploitent des données que vous possédez déjà.

**Trois questions de vérification**

1. Vous disposez de trois heures par semaine. Par quoi commencez-vous, et pourquoi pas par une source ?
2. Quelle section du produit mensuel démontre le mieux que le travail a lieu, et pourquoi ?
3. Pourquoi un renoncement écrit vaut-il mieux qu'un renoncement tacite ?

---

### Chapitre 40 — Construire une fonction de zéro à douze mois

#### 40.1 Le diagnostic en dix jours : cinq questions

Avant tout plan, situez l'organisation. Cinq questions, et les réponses se trouvent en dix jours.

| # | Question | Ce que la réponse révèle |
|---|---|---|
| **1** | **Quelles décisions se prennent ici où il manque quelque chose ?** | L'existence ou non de besoins réels |
| **2** | **Qui prendrait ces décisions ?** | Les destinataires — sans eux, rien n'est possible |
| **3** | **Que recevons-nous déjà, et qui le lit ?** | Ce qui est couvert sans le savoir |
| **4** | **Qu'est-ce qui nous est arrivé ces dix-huit derniers mois ?** | Les angles morts réels, et la crédibilité de départ |
| **5** | **Que savons-nous de notre exposition ?** | Si l'étape 4 du chapitre 2 est possible |

**La lecture des réponses.** Si les questions 1 et 2 n'ont pas de réponse, ne souscrivez rien et ne collectez rien : construisez d'abord les besoins. Si la question 5 n'a pas de réponse, votre priorité n'est pas le CTI mais l'inventaire — sans lui, vous ne pourrez jamais vérifier l'applicabilité, donc jamais produire de renseignement.

#### 40.2 Jours 0-30 : les besoins et les destinataires

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Rencontrer chaque destinataire potentiel, avec les trois questions du §14.2 | Une liste de besoins bruts |
| **P0** | Formuler 3 à 6 besoins avec les cinq propriétés du §14.1 | Registre des besoins |
| **P0** | Inventorier ce qui est **déjà reçu** et jamais exploité | Matrice de couverture |
| **P0** | Relire les incidents des 18 derniers mois | Fiche de synthèse des angles morts |
| P1 | Identifier le référent juridique et protection des données | Contact établi |

**Ce qu'on ne fait pas ce mois-ci** : souscrire, installer un outil, produire un livrable périodique, suivre des sources.

⚠️ **L'erreur de séquencement la plus coûteuse** : commencer par les sources. Elle produit une fonction occupée qui, dix-huit mois plus tard, ne peut démontrer aucune décision modifiée.

#### 40.3 Jours 30-90 : le premier cycle mesuré

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Construire le plan de collecte, avec la colonne « déjà couvert » | Matrice besoins × sources |
| **P0** | Mettre en place la file à cinq états, avec archivage motivé | Processus |
| **P0** | Produire **un** premier produit, sur le besoin le plus actionnable | Fiche opérationnelle |
| **P0** | **Demander un retour** deux semaines après | Trois questions |
| P1 | Établir l'échelle de calibrage | Une page, validée |
| P1 | Organiser la relecture croisée | Grille en six points |

**Le premier produit doit porter sur le besoin le plus actionnable**, pas sur le plus intéressant. Dans la quasi-totalité des cas, c'est la priorisation de la remédiation : le destinataire est identifié, la décision est concrète, et le résultat est immédiatement visible.

#### 40.4 Jours 90-180 : le calibrage et les interfaces

| Prio | Action |
|---|---|
| **P0** | Appliquer l'échelle de calibrage à tous les produits |
| **P0** | Établir les interfaces avec la détection et la gestion des vulnérabilités |
| **P0** | Tenir le registre des décisions — deux lignes par produit |
| P1 | Adhérer à un dispositif sectoriel, avec le cadre juridique instruit |
| P1 | Produire la première fiche de renseignement post-incident |
| P2 | Évaluer, sans souscrire, ce qui manque réellement |

#### 40.5 Jours 180-365 : la mesure et le partage

| Prio | Action |
|---|---|
| **P0** | Premier tableau de bord, avec les trois familles d'indicateurs |
| **P0** | Premier retour d'expérience analytique — les dix dernières estimations |
| **P0** | Réviser les besoins : lesquels sont satisfaits, abandonnés, mal formulés ? |
| P1 | Premier partage sectoriel, même minimal |
| P1 | Audit d'empreinte informationnelle |
| P2 | Souscription commerciale, si et seulement si un besoin précis reste non couvert après les cinq tests |

#### 40.6 ⚠️ Les erreurs de séquencement

| Erreur | Conséquence |
|---|---|
| **Souscrire avant d'avoir des besoins** | Vous payez pour ce que vous ne lisez pas |
| **Installer une plateforme avant d'avoir du volume** | Vous maintenez un outil au lieu de produire |
| **Produire une lettre d'information** | §38.4 — l'anti-pattern, difficile à défaire ensuite |
| **Ne pas demander de retour dès le premier produit** | La boucle ne se ferme jamais |
| **Chercher la couverture avant l'utilité** | Vous suivez tout et ne servez personne |
| **Alerter tôt pour exister** | §27.6 — vous dépensez un crédit que vous n'avez pas encore |

#### 40.7 ✅ Feuille de route consolidée

**P0 — sans quoi rien ne fonctionne**

1. Trois à six besoins formulés, avec demandeur nommé et décision identifiée.
2. Un inventaire exploitable, permettant de vérifier l'applicabilité.
3. Une file à cinq états, avec **archivage motivé**.
4. Une échelle de calibrage, publiée en annexe de chaque produit.
5. Un premier produit sur le besoin le plus actionnable, avec **retour demandé**.
6. Un registre des décisions, tenu dès le premier jour.
7. Le cadre juridique de la collecte, instruit avec le référent.

**P1 — ce qui rend la fonction durable**

8. Une relecture croisée, avec la grille en six points.
9. Les interfaces avec la détection et la gestion des vulnérabilités.
10. L'exploitation du renseignement interne : incidents, tentatives bloquées, dérogations.
11. L'adhésion sectorielle, avec son cadre.
12. Le tableau de bord en six indicateurs.

**P2 — ce qui fait la différence dans la durée**

13. Le retour d'expérience analytique semestriel.
14. L'audit d'empreinte informationnelle annuel.
15. Une souscription commerciale, après les cinq tests et sur un besoin précis.
16. Un comité de priorisation, si les besoins viennent de plusieurs services.

#### 40.8 Ce qui fait un bon analyste

**Ce qui s'apprend** : les modèles, les formats, les techniques d'analyse structurée, le calibrage, l'écriture. Tout le contenu de ce cours s'apprend, et se pratique en quelques mois.

**Ce qui se pratique et ne s'enseigne pas** :

| Qualité | Comment elle se développe |
|---|---|
| **Tolérer l'incertitude** | En écrivant « nous ne savons pas » jusqu'à ce que ce soit confortable |
| **Sentir qu'un raisonnement est trop propre** | En s'étant trompé plusieurs fois de la même façon |
| **Savoir quand s'arrêter** | En ayant produit un graphe inutile (§24.8) |
| **Poser la question qui manque** | En ayant vu quelqu'un d'autre la poser |
| **Résister à la pression de conclure** | En ayant conclu trop vite une fois, et en l'ayant payé |

**Se tromper publiquement** est ce qui enseigne le plus, et le fil rouge est construit autour de cela : Nour se trompe en juillet 2029, et c'est cet épisode qui produit le calibrage, la clause de réfutation et le seuil de mobilisation. Une fonction qui ne s'est jamais trompée n'a probablement pas assez conclu.

> **Ce qui distingue un bon analyste n'est pas son taux d'exactitude. C'est l'alignement entre ce qu'il affirme et ce qu'il sait — et sa capacité à voir, avant les autres, quand cet alignement se dégrade.**

#### 40.9 La chaîne complète, en une page

🖼 **SCHÉMA — La boucle analytique complète.** *Poster récapitulatif pleine page, reprenant les six segments avec leurs chapitres. Destiné à l'impression séparée.*

```
  ┌─ ① QUESTION ───────────────────────────────────────────────┐
  │  Besoins prioritaires (14) ─► Plan de collecte (14)         │
  │  Trois niveaux (3) · Cinq objets (2) · Axiomes (4)          │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ② COLLECTE ───────────────────────────────────────────────┐
  │  Cadre juridique (20) ─► Sources ouvertes (21)              │
  │  Sources payantes (22) · Renseignement interne (23)         │
  │  Infrastructure adverse (24)                                │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ③ ANALYSE ────────────────────────────────────────────────┐
  │  Hypothèses concurrentes (6, 8) ─► Biais (7)                │
  │  Évaluation de source (10) · Acteurs (17) · Modèles (18)    │
  │  Économie de la menace (16) · Campagnes (19)                │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ④ JUGEMENT ───────────────────────────────────────────────┐
  │  Calibrer (9) ─► Produire un jugement (11) ─► Relire (12)   │
  │  Écrire (25) · Adapter (26) · Alerter (27) · Partager (28)  │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ⑤ DÉCISION ───────────────────────────────────────────────┐
  │  Cinq décisions (29) ─► Détection (30) · Vulnérabilités (31)│
  │  Réponse à incident (32) · Produit (33)                     │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ⑥ RETOUR ─────────────────────────────────────────────────┐
  │  Mesurer (35) ─► Retour d'expérience analytique (35.6)      │
  │  Empreinte (34) · Économie (37) · Organisation (38)         │
  └──────────────────────────┬─────────────────────────────────┘
                             │
                    nouvelle incertitude
                             │
                             └──────────► retour en ①
```

**Les huit règles qui résument le cours**

1. Le renseignement n'a de valeur que s'il modifie une décision.
2. Le besoin précède la collecte — toujours.
3. Une meilleure collecte ne compense jamais une mauvaise analyse.
4. Les faits sont observés ; les jugements sont argumentés.
5. La confiance s'exprime, et elle est indépendante de la gravité.
6. Une analyse qui ne dit pas ce qui l'invaliderait est une opinion.
7. Personne ne peut produire votre renseignement à votre place, parce que personne d'autre ne connaît votre contexte.
8. Ignorer est la décision la plus fréquente — et elle doit être tracée.

#### 40.10 La phrase fondatrice, reprise

Le chapitre 1 s'ouvrait sur elle. Elle clôt le cours :

> ### Le CTI n'est pas là pour prédire l'avenir. Il est là pour prendre de meilleures décisions malgré l'incertitude.

**Ce que quarante chapitres ont ajouté à cette phrase** : la certitude qu'elle est atteignable. Réduire l'incertitude ne demande ni moyens exceptionnels, ni sources rares, ni outillage coûteux. Cela demande de savoir ce qu'on cherche, de raisonner avec méthode, de dire ce qu'on ignore, et d'écrire pour quelqu'un.

Le reste — les référentiels, les formats, les plateformes — est du soutien.

#### 40.11 🔴 FIL ROUGE — décembre 2031 : ce que Nour écrit

Trente-deux mois après sa prise de poste, Nour rédige un document que Claire lui a demandé : un guide interne, destiné au second analyste qui arrivera en 2032.

**Le document fait onze pages.** Voici sa première.

> **Ce que j'aurais aimé savoir en arrivant**
>
> **1. Ne souscris rien pendant trois mois.** Tout ce dont tu as besoin est déjà là, et personne ne le lit. Ta première valeur, c'est de le lire.
>
> **2. Va voir les gens avant de lire quoi que ce soit.** Pose-leur deux questions : quelles décisions te manquent, et qu'est-ce qui t'a surpris cette année. Tu auras tes besoins en une semaine.
>
> **3. Le premier rapport que tu produiras ne sera pas lu.** Ce n'est pas grave, et ce n'est pas parce qu'il est mauvais. C'est parce que tu commenceras par le contexte. Mets la conclusion en premier.
>
> **4. Tu te tromperas, et probablement dans les six premiers mois.** Écris ce qui invaliderait tes analyses **avant** de te tromper. C'est la ligne qui t'aurait sauvée, et c'est celle qu'on oublie.
>
> **5. Quand quelqu'un te demandera qui nous attaque, ne réponds pas.** Explique-lui pourquoi la question ne change rien, et donne-lui ce qui change quelque chose.
>
> **6. La plupart de ton travail consistera à archiver des choses.** Écris toujours pourquoi. C'est ce qui distingue une décision d'un oubli, et tu ne t'en rendras compte que le jour où on te posera la question.
>
> **7. Fais-toi relire par quelqu'un qui n'y connaît rien.** Il verra ce que tu ne vois plus.
>
> **8. Mesure ce que tes produits ont changé, dès le premier.** Pas ce que tu as produit. Dans deux ans, on te le demandera, et ce sera trop tard pour reconstituer.
>
> **9. Une semaine sans décision d'agir n'est pas une semaine perdue.** C'est une semaine où trente-neuf fois, quelqu'un aurait pu s'inquiéter et n'a pas eu à le faire.
>
> **10. Tu ne prédiras jamais rien.** Ce n'est pas ton métier. Ton métier, c'est de faire en sorte que les gens décident mieux sans savoir tout.

**Ce que Claire ajoute en préface**, une phrase :

> *« Nour a mis trente-deux mois à écrire cette page. Lis-la en dix minutes, et reviens la relire dans un an — tu ne la comprendras vraiment qu'à ce moment-là. »*

---

> ### 🎓 À ce stade de la Partie VIII, vous savez…
>
> - **auditer ce que votre organisation révèle d'elle-même**, et distinguer les mesures utiles du repli ;
> - **mesurer une fonction** par ses décisions modifiées et non par sa production ;
> - **conduire un retour d'expérience analytique**, et juger l'alignement entre confiance et justesse ;
> - **placer les outils à leur place** : ils accélèrent, ils ne raisonnent pas ;
> - **chiffrer une fonction**, y compris le temps des destinataires ;
> - **organiser la fonction** selon l'origine des besoins, et reconnaître l'anti-pattern de la veille documentaire ;
> - **construire un dispositif minimal viable** à trois heures par semaine, avec des renoncements écrits ;
> - **séquencer les douze premiers mois** sans commettre les six erreurs classiques.

---


## Cas de synthèse

Les trois cas se travaillent en situation, annexes ouvertes. Chacun fournit un dossier de données, pose des questions dans l'ordre où elles se présentent, et propose un corrigé argumenté avec les erreurs volontairement insérées.

---

### Cas A — Campagne active visant votre secteur

> **Format** — Cas de décision sous incertitude et sous pression. Durée : **2 h 30**.
> **Livrables** : évaluation calibrée · décision d'exploitation · bulletin direction · bulletin client.
> **Prérequis** : chapitres 6 à 11, 19, 27, 29.

#### A.1 Le dossier

**Vous êtes analyste CTI** dans une entreprise de 900 personnes, fabricant d'équipements industriels, 60 clients dont 12 grands comptes. Nous sommes le **mardi 14 septembre, 9 h 15**.

##### Artefact 1 — le message reçu

> **Dispositif de partage sectoriel — Bulletin SEC-2031-0912 — 14/09, 07 h 40 — Diffusion : membres**
>
> *Trois membres du dispositif ont signalé, entre le 28 août et le 11 septembre, des intrusions présentant des caractéristiques communes. Les trois organisations sont des fabricants d'équipements industriels. Le vecteur d'entrée n'est pas établi à ce stade.*
>
> *Éléments communs relevés : utilisation d'un outil d'administration légitime pour le mouvement latéral · exfiltration vers un hébergeur à la demande · absence de chiffrement ou de demande de rançon.*
>
> *Les membres sont invités à renforcer leur vigilance et à signaler toute observation.*

##### Artefact 2 — ce que vous savez de votre organisation

```
Secteur              : fabricant d'équipements industriels ✅ correspond
Effectif             : 900 personnes
Sites                : 3 (siège, usine, R&D)
Outil d'administration cité : PRÉSENT — utilisé par l'exploitation
Journalisation       : postes 90 j · annuaire 12 mois · pare-feu 12 mois
                       serveur de fichiers : NON COLLECTÉ
Détection            : 89 règles, couverture testée 33 %
                       mouvement latéral : 44 % · exfiltration : 22 %
Dernier incident     : février, poste compromis, 11 j avant détection
```

##### Artefact 3 — le contexte du jour

- Votre RSSI est en déplacement, joignable.
- Le comité de direction se réunit **jeudi 16 à 14 h**.
- Un grand compte a demandé la semaine dernière un point sur votre dispositif de sécurité.
- Vous êtes seul sur la fonction.

#### A.2 Les questions, dans l'ordre

| # | Question | Livrable |
|---|---|---|
| 1 | Que faites-vous dans les deux premières heures ? | Actions listées |
| 2 | Quelle information manquante est la plus déterminante ? | — |
| 3 | Formulez trois hypothèses concurrentes. | Matrice |
| 4 | Quelle décision d'exploitation ? | Arbre §29.2 |
| 5 | Rédigez l'évaluation calibrée. | Une page |
| 6 | Que dites-vous au comité de jeudi ? | 10 lignes |
| 7 | Que dites-vous au grand compte qui a demandé un point ? | 8 lignes |
| 8 | Quatre erreurs sont insérées dans le dossier. Lesquelles ? | — |

#### A.3 Corrigé — les deux premières heures

**Ce qu'il ne faut pas faire** : alerter. Les conditions du §27.1 ne sont pas réunies — l'applicabilité n'est pas établie, et aucune action n'est identifiée.

**Ce qu'il faut faire, dans cet ordre** :

| Heure | Action | Justification |
|---|---|---|
| 9 h 15 | **Poser la question manquante au dispositif** : quel est le vecteur d'entrée ? | C'est la condition ① du §19.4 |
| 9 h 30 | Vérifier l'applicabilité des éléments connus : l'outil d'administration est-il présent, comment est-il utilisé, par qui | Nœud ① de l'arbre |
| 10 h 00 | Recherche rétrospective sur ce qui est disponible : usages inhabituels de l'outil dans l'annuaire sur 12 mois | Ne coûte rien, peut trancher |
| 10 h 45 | Établir ce qu'on **ne peut pas** vérifier : le serveur de fichiers n'est pas journalisé | §4.3 — l'absence appelle une question sur la capacité d'observation |
| 11 h 00 | Informer le RSSI — **information, pas alerte** | §27.1, condition 3 non remplie |

**La question posée au dispositif est l'action la plus rentable de la matinée.** Elle coûte deux minutes et conditionne tout le reste : sans le vecteur, l'applicabilité ne peut pas être établie.

#### A.4 Corrigé — l'information manquante

**Le vecteur d'entrée.** Sans lui :

| Ce qu'on ne peut pas faire | Pourquoi |
|---|---|
| Établir l'applicabilité | On ne sait pas si le chemin existe chez nous |
| Prioriser une remédiation | On ne sait pas quoi corriger |
| Écrire une règle de détection | On ne sait pas quoi chercher en amont |
| Décider d'une mesure d'atténuation | On ne sait pas quoi fermer |

**Ce que l'artefact 1 donne en revanche** : trois éléments de la **phase post-intrusion** — mouvement latéral, exfiltration, absence de rançon. Ils permettent une recherche rétrospective, mais pas une prévention.

⚠️ **La distinction est essentielle** : un bulletin qui décrit ce qui se passe **après** l'entrée permet de chercher, pas de se protéger.

#### A.5 Corrigé — les trois hypothèses

| Réf | Hypothèse | Origine |
|---|---|---|
| **H-A** | Ciblage sectoriel des fabricants d'équipements industriels | L'hypothèse spontanée, suggérée par le bulletin |
| **H-B** | Exploitation opportuniste d'un composant ou service commun au secteur | Par mécanisme (§8.3) |
| **H-C** | Compromission d'un prestataire ou fournisseur commun aux trois | Par inversion — **l'hypothèse ennuyeuse** |

**La matrice, avec les éléments disponibles** :

| Élément | H-A | H-B | H-C |
|---|---|---|---|
| Trois victimes du même secteur | `++` | `+` | `+` |
| Intervalle de 15 jours entre la première et la dernière | `+` | `++` | `++` |
| **Absence de chiffrement et de rançon** | `++` | `−` | `0` |
| Outil d'administration légitime employé | `+` | `+` | `++` |
| Exfiltration vers un hébergeur à la demande | `+` | `+` | `+` |
| **Vecteur d'entrée inconnu** | `0` | `0` | `0` |

**La lecture** : l'absence de chiffrement et de demande de rançon est l'élément le plus discriminant du dossier. Elle rend H-B moins probable — une exploitation opportuniste de masse aboutit généralement à une monétisation directe (§16.3). Elle soutient H-A.

**Mais aucune hypothèse n'est éliminée**, et c'est le point : avec cinq éléments dont aucun ne porte sur le vecteur, on ne peut pas trancher.

**Les hypothèses clés à identifier** (§8.6) :

| Présupposé | Vérifié ? | Si faux |
|---|---|---|
| Les trois victimes sont bien du même secteur | ✅ selon le bulletin | — |
| Elles n'ont pas de prestataire commun | ❌ **non vérifié** | H-C deviendrait dominante |
| Le bulletin rapporte tous les cas connus | ❌ non vérifiable | Une victime hors secteur éliminerait H-A |

**La deuxième ligne est celle qui manque**, et c'est exactement l'élément ③ du §8.9 du fil rouge.

#### A.6 Corrigé — la décision d'exploitation

**Parcours de l'arbre du §29.2** :

```
① Applicable chez nous ?     → INDÉTERMINÉ (vecteur inconnu)
                                Les éléments post-intrusion, eux, sont applicables
② Exploitable en l'état ?     → Indéterminé
③ Action possible maintenant ? → OUI, partiellement :
                                 recherche rétrospective sur l'outil d'administration
④ Inaction déraisonnable ?     → Non — aucune urgence caractérisée
```

**Décision : DIFFÉRER, avec une action de collecte et une recherche rétrospective.**

| Action | Délai | Porteur |
|---|---|---|
| Question au dispositif sur le vecteur | Immédiat | Vous |
| **Question au dispositif sur l'existence d'un prestataire commun** | Immédiat | Vous |
| Recherche rétrospective sur l'outil d'administration, 12 mois | 48 h | Vous + détection |
| Évaluation de la faisabilité d'une règle sur l'usage anormal de l'outil | 5 j | Détection |
| **Constat écrit** : le serveur de fichiers n'est pas journalisé, donc l'exfiltration ne serait pas détectable | Immédiat | Vous |

⚠️ **La dernière ligne est celle qu'on oublie.** Elle ne répond pas à la question du jour ; elle documente une lacune structurelle que le dossier vient de révéler.

#### A.7 Corrigé — l'évaluation calibrée

> **Objet** : campagne signalée contre des fabricants d'équipements industriels — évaluation au 14 septembre
>
> **Nous estimons *aussi probable qu'improbable* que notre organisation entre dans le périmètre de cette campagne — *confiance faible*.** Cette faible confiance tient à l'absence d'information sur le vecteur d'entrée, qui empêche d'établir notre applicabilité.
>
> **Ce que nous observons.** Un bulletin sectoriel du 14 septembre signale trois intrusions chez des fabricants d'équipements industriels entre le 28 août et le 11 septembre. Les éléments communs rapportés concernent la phase post-intrusion : emploi d'un outil d'administration légitime, exfiltration vers un hébergeur à la demande, absence de chiffrement et de demande de rançon. **Le vecteur d'entrée n'est pas établi.**
>
> **Ce que nous en estimons.** Trois hypothèses ont été envisagées : un ciblage sectoriel, une exploitation opportuniste d'un composant commun, ou la compromission d'un prestataire partagé. L'absence de monétisation directe est l'élément le plus discriminant et soutient l'hypothèse d'un ciblage. Aucune hypothèse n'est cependant éliminée, faute d'information sur le vecteur et sur l'existence éventuelle d'un prestataire commun aux trois victimes.
>
> **Ce qui trancherait.** Le vecteur d'entrée employé chez les trois victimes · l'existence d'un prestataire ou fournisseur commun · la survenue d'un cas hors secteur.
>
> **Ce qui invaliderait cette évaluation.** Une quatrième victime n'appartenant pas au secteur éliminerait l'hypothèse de ciblage · l'identification d'un prestataire commun aux trois la rendrait secondaire.
>
> **Ce que nous ne savons pas.** Nos journaux ne couvrent pas le serveur de fichiers. Une exfiltration comparable à celle décrite ne serait **pas détectable** chez nous, ni a posteriori. Cette lacune est structurelle et dépasse le cadre de cette évaluation.
>
> **Ce que nous recommandons.** Deux questions au dispositif sectoriel (immédiat, sans coût) · une recherche rétrospective sur l'usage de l'outil d'administration (48 h, 1 jour-homme) · l'évaluation d'une collecte des journaux du serveur de fichiers (à instruire, hors urgence).
>
> *Évaluation au 14 septembre. Réexamen à réception des réponses du dispositif, ou sous 7 jours.*

#### A.8 Corrigé — le comité de jeudi

> **Campagne signalée dans notre secteur — point d'information**
>
> Un dispositif de partage sectoriel a signalé mardi trois intrusions chez des fabricants d'équipements industriels au cours des trois dernières semaines.
>
> **Sommes-nous concernés ?** Nous ne pouvons pas l'établir : le vecteur d'entrée n'est pas connu. Nous avons posé la question et attendons une réponse.
>
> **Ce que nous avons fait.** Une recherche rétrospective sur douze mois n'a rien mis en évidence. Une évaluation complète est disponible.
>
> **Ce que nous avons découvert au passage.** Nos journaux ne couvrent pas notre serveur de fichiers. Une exfiltration de données comparable à celle décrite ne serait pas détectable chez nous. **C'est le point que nous portons à votre attention** ; il dépasse cette campagne.
>
> **Ce que nous attendons de vous.** Rien à ce stade sur la campagne. Sur la journalisation du serveur de fichiers, nous demanderons un arbitrage lorsque nous aurons chiffré la mesure.

⚠️ **Ce qui fait la valeur de cette note** : elle transforme un événement extérieur incertain en constat interne actionnable. C'est ce que la direction peut réellement décider.

#### A.9 Corrigé — le grand compte

> **Objet : votre demande de point sur notre dispositif de sécurité**
>
> Nous avons pris connaissance d'un signalement sectoriel concernant des intrusions chez des fabricants d'équipements industriels. Nous n'avons identifié aucune activité comparable dans notre environnement, sur la base d'une recherche rétrospective portant sur douze mois.
>
> Nous ne sommes pas en mesure d'établir si nous entrons dans le périmètre de cette campagne, le vecteur d'entrée n'ayant pas été communiqué. Nous avons demandé cette information.
>
> Nous restons disponibles pour un échange, et nous vous informerons si des éléments nouveaux nous concernaient.

⚠️ **Ce qui n'y figure pas** : nos hypothèses, notre lacune de journalisation, nos taux de couverture, et le nom du dispositif sectoriel. Ce sont des informations internes — §26.7.

#### A.10 Corrigé — les quatre erreurs insérées

| # | Erreur | Où | Effet |
|---|---|---|---|
| **1** | **Le bulletin ne donne pas le vecteur d'entrée** | Artefact 1 | C'est l'information la plus déterminante, et son absence n'est pas signalée comme une lacune par l'émetteur |
| **2** | **« Les trois organisations sont des fabricants »** — aucune mention d'une vérification d'exhaustivité | Artefact 1 | Le dispositif ne dit pas s'il connaît d'autres victimes hors secteur (§8.9) |
| **3** | **Le serveur de fichiers n'est pas journalisé** | Artefact 2 | La lacune est présente dans le dossier et facile à ne pas voir — c'est celle qui compte le plus |
| **4** | **La couverture de détection sur l'exfiltration est de 22 %** | Artefact 2 | Le dossier contient l'information disant que vous ne détecteriez pas ce qui est décrit |

**Les erreurs 3 et 4 se renforcent** : le dossier vous dit deux fois, de deux façons différentes, que vous ne verriez pas cette campagne si elle vous touchait. Un analyste qui se concentre sur « sommes-nous ciblés ? » les manque toutes les deux.

#### A.11 Barème

| Critère | Pts |
|---|---|
| Poser la question du vecteur en premier | 15 |
| Ne pas alerter, et justifier par la condition 3 | 10 |
| Trois hypothèses dont une par inversion | 15 |
| Identifier le présupposé du prestataire commun | 10 |
| **Relever la lacune de journalisation** | **20** |
| Évaluation calibrée avec confiance faible justifiée | 15 |
| Note comité transformant l'incertitude en constat actionnable | 10 |
| Bulletin client sans information interne | 5 |

**Seuil** : 70/100. **Élimination** : alerter, ou conclure au ciblage sur la base du bulletin seul.

#### A.12 Variante — une seconde source contredit la première

*Le 16 septembre, un éditeur publie une analyse portant sur la même campagne, et mentionne une quatrième victime : un distributeur de matériel électronique.*

**Ce que cela change** :

| Élément | Effet |
|---|---|
| H-A — ciblage sectoriel | **Fortement contredit** — une victime hors secteur |
| H-B — exploitation opportuniste | Renforcée |
| H-C — prestataire commun | Renforcée, si le distributeur partage un prestataire |
| Votre évaluation | À réviser, et **c'était écrit dans la clause de réfutation** |

**Ce que la variante enseigne** : la clause de réfutation du §A.7 n'était pas une précaution rhétorique. Elle avait nommé exactement l'observation qui allait se produire — et sa présence rend la révision naturelle plutôt qu'embarrassante.

**La note de révision, deux lignes** :

> *Notre évaluation du 14 septembre est révisée : l'hypothèse d'un ciblage sectoriel est écartée, une quatrième victime n'appartenant pas au secteur ayant été documentée le 16 septembre. Nous estimons désormais probable une exploitation opportuniste d'un composant commun — confiance moyenne.*

---

### Cas B — L'information qui n'était pas vraie

> **Format** — Cas de rétractation. Durée : **2 h**.
> **Livrables** : reconstitution de chaîne · note de rétractation interne · communication client · retour d'expérience analytique.
> **Prérequis** : chapitres 4, 9, 10, 12, 35.

#### B.1 Le dossier

**Vous êtes analyste CTI** dans un groupe de 1 400 personnes du secteur de l'énergie. Nous sommes le **3 mars**. Les faits qui suivent se sont déroulés sur cinq semaines, et vous les reconstituez.

##### Artefact 1 — le point de départ, 22 janvier

> **Rapport d'un fournisseur de renseignement — abonnement souscrit en 2030 — 22 janvier**
>
> *« Notre équipe a identifié une campagne visant le secteur de l'énergie en Europe occidentale. Parmi les organisations dont l'infrastructure a été observée dans le périmètre de reconnaissance de l'acteur figure [VOTRE ORGANISATION].*
>
> *Nous recommandons un renforcement immédiat de la surveillance des accès distants. »*

##### Artefact 2 — ce qui a été fait, du 23 janvier au 6 février

```
23 janv.  Évaluation produite en 4 h. Conclusion : "très probable que
          nous soyons ciblés". Confiance : non exprimée.
23 janv.  Alerte émise. Cellule constituée.
24-31 j.  Recherche rétrospective sur 90 jours : 5 jours-homme.
          Aucune activité anormale identifiée.
27 janv.  Restriction des accès distants aux plages d'adresses connues.
          14 collaborateurs en déplacement impactés.
30 janv.  Deux projets décalés pour libérer l'équipe.
3 févr.   Information du comité de direction.
5 févr.   Un grand compte informé "par transparence" que nous faisons
          l'objet d'une campagne de reconnaissance.
6 févr.   Levée de la restriction. Coût estimé : 23 000 €.
```

##### Artefact 3 — ce que vous découvrez le 28 février

En préparant le retour d'expérience trimestriel, vous relisez le rapport du 22 janvier et cherchez sa base. Vous écrivez au fournisseur.

> **Réponse du fournisseur, 2 mars**
>
> *« La mention de votre organisation provient de l'observation, dans un jeu de données de reconnaissance attribué à cet acteur, d'une adresse appartenant à une plage annoncée par votre fournisseur d'hébergement.*
>
> *Nous ne sommes pas en mesure de confirmer que cette adresse vous était attribuée à la date de l'observation. Notre formulation aurait dû être plus prudente. »*

##### Artefact 4 — vérification faite le 3 mars

```
Adresse concernée : appartenait à une plage d'hébergement mutualisé.
Attribuée à votre organisation : du 12 mars 2029 au 8 novembre 2030.
Date de l'observation citée : 14 décembre 2030.
                              → 5 semaines APRÈS la fin d'attribution.
```

#### B.2 Les questions

| # | Question |
|---|---|
| 1 | Reconstituez la chaîne de provenance et identifiez le point de rupture. |
| 2 | Quelles étapes du chapitre 10 auraient évité les 23 000 € ? |
| 3 | Où le calibrage a-t-il manqué, précisément ? |
| 4 | Rédigez la note de rétractation interne. |
| 5 | Que dites-vous au grand compte informé le 5 février ? |
| 6 | Conduisez le retour d'expérience analytique. |
| 7 | Quelles mesures pérennes ? |

#### B.3 Corrigé — la chaîne de provenance

```
Une adresse figure dans un jeu de données de reconnaissance
        │  observation réelle, non contestée
        ▼
L'adresse appartient à une plage d'hébergement mutualisé
        │  ← PREMIÈRE RUPTURE : rien n'établit qui l'utilisait
        ▼
Le fournisseur associe l'adresse à votre organisation
        │  ← DEUXIÈME RUPTURE : attribution périmée de 5 semaines
        ▼
Le rapport écrit : "figure dans le périmètre de reconnaissance"
        │  ← TROISIÈME RUPTURE : perte du mode, l'hypothèse devient constat
        ▼
Votre évaluation : "très probable que nous soyons ciblés"
        │  ← QUATRIÈME RUPTURE : reprise sans vérification, calibrage absent
        ▼
Alerte, mobilisation, 23 000 €, et information d'un client
```

**Le point de rupture décisif est le deuxième** : l'adresse n'était plus attribuée à l'organisation cinq semaines avant l'observation. Cette vérification demandait **une requête et dix minutes**.

**Ce que le cas illustre** : il ne s'agit pas de circularité (§10.4) — il n'y a qu'une source. Il s'agit d'une **chaîne de provenance non remontée** (§10.3), et de la quatrième question qui s'arrête toujours sur du vide : *sur quoi la source fonde-t-elle son affirmation ?*

#### B.4 Corrigé — ce qui aurait évité les 23 000 €

| Étape du chapitre 10 | Ce qu'elle aurait produit | Coût |
|---|---|---|
| **§10.3 — remonter la chaîne** | La question « sur quoi repose la mention ? » posée le 23 janvier | 5 min pour écrire |
| **§10.1 — fiabilité ≠ crédibilité** | Le fournisseur est fiable ; **cette affirmation précise** ne l'est pas nécessairement | 0 |
| **§10.6 — évaluer la publication** | La méthodologie n'est pas décrite, le niveau de confiance n'est pas exprimé | 10 min |
| **§10.8 — éléments propres apportés** | Une seule mention, aucun élément corroborant | 0 |

**Le geste unique qui aurait suffi** : écrire au fournisseur le 23 janvier, avant d'alerter. Cinq minutes, une réponse en quelques jours — et l'alerte aurait été remplacée par une vérification.

⚠️ **La difficulté réelle** : le 23 janvier, l'organisation est nommée dans un rapport payant. La pression à agir est maximale, et attendre une réponse paraît irresponsable. **C'est précisément la situation que le §29.4 traite** : gravité élevée, confiance faible non exprimée. La bonne décision était *vérifier en priorité*, pas *mobiliser*.

#### B.5 Corrigé — le calibrage manquant

**Ce qui a été écrit** : *« très probable que nous soyons ciblés »*.

**Ce qui manquait** :

| Élément | Effet de son absence |
|---|---|
| **Le niveau de confiance** | Le lecteur ignore que l'évaluation repose sur une source unique non vérifiée |
| **La base** | Personne ne sait sur quoi repose le « très probable » |
| **La clause de réfutation** | Personne ne sait ce qui la renverserait — or c'était vérifiable |
| **La distinction ciblé / observé** | « Figurer dans un périmètre de reconnaissance » ≠ « être ciblé » |

**La quatrième est celle qui aurait le plus changé la décision.** Même si l'attribution d'adresse avait été correcte, figurer dans un jeu de reconnaissance signifie que votre adresse a été balayée — ce qui est le cas de toute adresse publique, en permanence.

**L'évaluation qu'il aurait fallu écrire** :

> *Nous estimons **aussi probable qu'improbable** que notre infrastructure ait fait l'objet d'une reconnaissance par cet acteur — **confiance faible** : source unique, base de l'affirmation non communiquée, et « reconnaissance » ne constitue pas un ciblage.*
>
> *Ce qui trancherait : la nature de l'observation, et la confirmation que l'adresse citée nous était attribuée à la date concernée.*
>
> *Nous recommandons une vérification auprès du fournisseur avant toute mobilisation.*

**Le même dossier, correctement calibré, produit une décision à zéro euro.**

#### B.6 Corrigé — la note de rétractation interne

> **Objet : révision de l'évaluation du 23 janvier — campagne visant le secteur de l'énergie**
>
> **Notre évaluation du 23 janvier était erronée.** Nous avions estimé très probable que notre organisation soit ciblée par une campagne de reconnaissance. Cette conclusion ne tient pas.
>
> **Ce que nous avons établi.** La mention de notre organisation dans le rapport du 22 janvier repose sur l'observation d'une adresse appartenant à une plage d'hébergement mutualisé. Cette adresse ne nous était plus attribuée depuis le 8 novembre 2030, soit cinq semaines avant l'observation citée. Le fournisseur a confirmé le 2 mars ne pas être en mesure d'établir l'attribution à la date concernée.
>
> **Ce qui a manqué de notre part.** Nous n'avons pas remonté la chaîne de provenance avant d'agir, et nous n'avons pas exprimé de niveau de confiance. Une question écrite au fournisseur, le 23 janvier, aurait produit la même réponse en quelques jours et évité la mobilisation.
>
> **Ce que cela a coûté.** Environ 23 000 € en temps mobilisé, deux projets décalés de trois semaines, et l'information d'un client sur une base erronée.
>
> **Ce que nous changeons.** *(voir §B.9)*
>
> **Ce qui reste vrai.** La campagne visant le secteur de l'énergie est réelle et documentée. Nous n'avons simplement aucun élément indiquant qu'elle nous concerne.

⚠️ **Les trois choses que cette note fait, et qui la rendent acceptable** : elle affirme l'erreur en première phrase · elle établit les faits sans se dérober · elle distingue ce qui est faux de ce qui reste vrai.

#### B.7 Corrigé — la communication au grand compte

**La difficulté** : vous l'avez informé le 5 février « par transparence ». Ne rien dire est la pire option — il l'apprendra, ou il continuera à croire une information fausse.

> **Objet : précision sur notre information du 5 février**
>
> Le 5 février, nous vous avons informés qu'un signalement suggérait que notre infrastructure faisait l'objet d'une reconnaissance dans le cadre d'une campagne visant notre secteur.
>
> **Cette information n'est pas confirmée, et nous l'écartons.** La vérification que nous avons conduite établit que l'élément à l'origine du signalement concerne une adresse qui ne nous était plus attribuée à la date de l'observation.
>
> Nous n'avons identifié, à ce jour, aucun élément indiquant que notre organisation soit concernée. Les vérifications conduites entre le 24 et le 31 janvier, portant sur quatre-vingt-dix jours, n'ont mis en évidence aucune activité anormale.
>
> Nous avons revu notre processus de vérification des signalements externes. Nous restons à votre disposition.

**Ce que la dernière phrase du troisième paragraphe apporte** : elle transforme un aveu en démonstration de capacité. La recherche rétrospective a été faite, et son résultat est utile indépendamment de l'erreur d'origine.

#### B.8 Corrigé — le retour d'expérience analytique

**La méthode du §35.6, appliquée** :

| Question | Réponse |
|---|---|
| **L'estimation était-elle juste ?** | Non |
| **La confiance était-elle juste ?** | **Non exprimée** — donc implicitement élevée |
| Position dans le tableau du §35.6 | **Estimation fausse + confiance élevée = le pire cas** |
| Quel biais ? | Ancrage sur le nom de l'organisation dans un rapport payant · biais du client — la fonction avait besoin de justifier l'abonnement · absence de recherche d'hypothèse alternative |
| Quelle méthode a manqué ? | La chaîne de provenance (§10.3) et le calibrage (§9) |
| Qu'est-ce qui change dans ma pratique ? | *(§B.9)* |

**Le biais le plus difficile à admettre est le deuxième.** L'abonnement avait été souscrit en 2030 et n'avait produit aucun signalement majeur. Le rapport du 22 janvier était le premier à nommer l'organisation. Il y avait, sans intention consciente, un intérêt à ce qu'il soit important.

C'est le §7.7 — et il opère ici sur le fournisseur autant que sur le destinataire.

#### B.9 Corrigé — les mesures pérennes

| # | Mesure | Effet attendu |
|---|---|---|
| **1** | **Toute mention nominative de l'organisation dans une source externe déclenche une remontée de chaîne avant toute action** | C'est la mesure qui aurait tout évité |
| **2** | **Aucune évaluation sans niveau de confiance** — champ obligatoire | §9 |
| **3** | **Aucune alerte sur source unique non vérifiée** — la source unique déclenche une vérification | §27.1, §29.4 |
| **4** | **Toute évaluation destinée à déclencher une action porte une clause de réfutation** | §11.3 |
| **5** | **Communication externe sur une base non vérifiée : interdite** | Le 5 février n'aurait pas dû avoir lieu |
| **6** | Revue trimestrielle du fournisseur, avec les cinq tests du §22.3 | La méthodologie non décrite est un signal |

**La mesure 5 mérite un mot** : informer un client « par transparence » sur une information non vérifiée n'est pas de la transparence, c'est un transfert d'incertitude. La transparence consiste à dire ce qu'on sait, avec son niveau de confiance — ce qui, ici, aurait produit un message très différent.

#### B.10 Ce que le cas enseigne

**Trois enseignements, dans l'ordre d'importance** :

1. **Une source unique, fiable, peut transmettre une information fausse.** C'est le §10.1 : fiabilité et crédibilité sont deux axes. Le fournisseur n'a pas menti — il a formulé imprudemment une observation réelle.

2. **Le calibrage absent est ce qui transforme une erreur en catastrophe.** L'évaluation aurait pu être fausse sans conséquence si elle avait porté « confiance faible » : la décision aurait été de vérifier.

3. **Le coût d'une rétractation est très inférieur au coût de ne pas se rétracter.** L'organisation a informé un client sur une base fausse ; la correction, faite rapidement et complètement, a préservé la relation. Une non-correction découverte plus tard l'aurait détruite.

**Le barème** :

| Critère | Pts |
|---|---|
| Reconstituer la chaîne et identifier la deuxième rupture | 20 |
| Identifier le geste unique qui aurait suffi | 15 |
| Distinguer « reconnaissance » de « ciblage » | 15 |
| Note de rétractation affirmant l'erreur en première phrase | 15 |
| Communication client sans dérobade | 10 |
| Retour d'expérience situant le cas dans le tableau du §35.6 | 15 |
| Identifier le biais du client | 10 |

**Élimination** : ne pas corriger l'information transmise au client.

---

### Cas C — Une personne, zéro budget, six mois

> **Format** — Cas de construction. Durée : **2 h**.
> **Livrables** : diagnostic · besoins formulés · plan de collecte · premier produit · mesure à six mois.
> **Prérequis** : chapitres 14, 21, 23, 29, 39, 40.

#### C.1 Le dossier

**Vous êtes responsable informatique** d'une organisation de 210 personnes — un opérateur de services de santé à domicile, 4 agences régionales. Vous n'avez pas de fonction de sécurité dédiée.

**Le déclencheur** : un donneur d'ordre public a introduit en janvier une exigence nouvelle dans ses marchés — *« démontrer une capacité de suivi des menaces pertinentes pour l'activité »*. Le renouvellement du marché est en septembre.

**Ce dont vous disposez** :

```
Temps                : 3 h par semaine, prises sur votre poste actuel
Budget               : 0 € en investissement. Adhésions possibles si < 2 k€
Équipe               : vous, plus un technicien
Inventaire           : à jour pour les serveurs, partiel pour les postes
Détection            : antivirus et pare-feu, pas de centre opérationnel
Incidents 18 mois    : 2 — un rançongiciel évité (poste isolé, sauvegarde),
                       une fuite d'identifiants via un service tiers
Produits utilisés    : suite bureautique en ligne · logiciel métier
                       (éditeur unique) · outil de télégestion · VPN
Clients              : 1 donneur d'ordre public, 3 mutuelles
```

#### C.2 Les questions

| # | Question | Livrable |
|---|---|---|
| 1 | Que faites-vous les dix premiers jours ? | Diagnostic |
| 2 | Formulez les besoins. Combien ? | Registre |
| 3 | Construisez le plan de collecte. | Matrice |
| 4 | Que refusez-vous de faire, et comment l'écrivez-vous ? | Liste de renoncements |
| 5 | Rédigez le premier produit mensuel. | Une page |
| 6 | Comment démontrez-vous la capacité en septembre ? | Dossier |
| 7 | Que mesurez-vous à six mois ? | Trois indicateurs |

#### C.3 Corrigé — les dix premiers jours

**Ce qu'il ne faut pas faire** : chercher des sources, comparer des offres, ou produire une première lettre d'information.

**Ce qu'il faut faire** :

| Jour | Action | Durée |
|---|---|---|
| 1-2 | **Trois entretiens** : le directeur général, le responsable des opérations, vous-même. Deux questions : *quelles décisions vous manquent ?* et *qu'est-ce qui vous a surpris cette année ?* | 2 h |
| 3-4 | **Relire les deux incidents** des dix-huit derniers mois : vecteur, ce qui a fonctionné, ce qui n'a pas détecté | 3 h |
| 5 | Inventorier ce qui est **déjà reçu** : bulletins, avis d'éditeurs, notifications de services | 1 h |
| 6-7 | Lire l'exigence du donneur d'ordre **mot à mot** : que demande-t-elle exactement ? | 1 h |
| 8-10 | Formuler 2 à 3 besoins | 2 h |

**Ce que les entretiens produisent typiquement** :

| Interlocuteur | Réponse type | Besoin sous-jacent |
|---|---|---|
| Directeur général | *« Qu'on ne se retrouve pas à l'arrêt comme [concurrent] l'an dernier »* | Ce qui frappe les organisations comparables |
| Responsable des opérations | *« Savoir si nos logiciels ont des problèmes avant que ça casse »* | Vulnérabilités des produits utilisés |
| Vous-même | *« Savoir quoi corriger en premier »* | Priorisation |

**Ce que la relecture des incidents produit** : les deux incidents impliquaient un tiers — un service externe pour la fuite, et un poste isolé mal inventorié pour le rançongiciel. **Votre angle mort est la périphérie**, pas le cœur.

#### C.4 Corrigé — les besoins

**Deux besoins, pas plus.** C'est le §39.1 : trois heures par semaine ne servent pas quatre besoins.

| Réf | Besoin | Demandeur | Décision éclairée | Niveau |
|---|---|---|---|---|
| **B-01** | *Parmi les vulnérabilités affectant nos quatre produits, lesquelles sont activement exploitées ?* | Vous | Ordre de correction | Opérationnel |
| **B-02** | *Quelles menaces atteignent des organisations comparables à la nôtre, et par quel chemin ?* | Directeur général | Investissement, préparation | Opérationnel |

**Pourquoi ces deux-là** :

- **B-01** est le plus actionnable et le moins coûteux. Il produit une décision chaque mois.
- **B-02** répond à la question du dirigeant **et** à l'exigence du donneur d'ordre. Il est le plus difficile, mais c'est celui qui est demandé.

**Ce qu'on écarte, et qu'on écrit** : le suivi d'acteurs, le renseignement stratégique, la surveillance de marque, l'infrastructure adverse.

#### C.5 Corrigé — le plan de collecte

| Question | Source | Type | Fréquence | Coût | Couverte ? |
|---|---|---|---|---|---|
| B-01/1 — vulnérabilités exploitées | Catalogue d'exploitation avérée | Ouverte | 5 min/jour | 0 € | ✅ |
| B-01/2 — avis de nos 4 éditeurs | Portails éditeurs, listes de diffusion | Ouverte | 10 min/jour | 0 € | ⚠️ reçus, non exploités |
| B-01/3 — applicabilité | **Inventaire interne** | Interne | Continu | 0 € | ⚠️ partiel sur les postes |
| B-02/1 — incidents comparables | Bulletins du centre de réponse national | Ouverte | 15 min/sem | 0 € | ⚠️ non exploités |
| B-02/2 — ce qui vise notre secteur | Dispositif de partage sectoriel santé | Communautaire | 20 min/sem | Adhésion | ❌ |
| B-02/3 — ce qui est testé contre nous | **Journaux du pare-feu** | Interne | 30 min/mois | 0 € | ❌ jamais regardé |

**Le total** : environ 2 h 40 par semaine. **Une seule dépense** : l'adhésion sectorielle.

**Les deux lignes internes** — B-01/3 et B-02/3 — sont gratuites et non exploitées. La seconde, les tentatives d'exploitation bloquées par le pare-feu (§23.3), est celle qui produira le plus vite un résultat visible.

**L'action la plus urgente qui n'est pas du CTI** : compléter l'inventaire des postes. Sans lui, B-01/3 ne fonctionne pas, et l'un des deux incidents provenait précisément d'un poste mal inventorié.

#### C.6 Corrigé — les renoncements écrits

> **Ce que notre dispositif ne couvre pas**
>
> **1. Le renseignement stratégique.** Nous ne produisons pas d'analyse prospective sur l'évolution des menaces. En cas de besoin, nous nous appuierons sur les publications de notre centre de réponse national et de notre dispositif sectoriel.
>
> **2. Le suivi d'acteurs.** Nous ne suivons pas d'acteurs nominativement. Nos décisions ne dépendent pas de l'identité des attaquants.
>
> **3. L'infrastructure adverse.** Nous vérifions la fraîcheur et la colocation avant tout blocage. Nous ne conduisons pas de travail d'investigation d'infrastructure.
>
> **4. La surveillance de marque et des espaces criminels.** Nous n'en avons ni le besoin exprimé, ni les moyens, ni le cadre juridique instruit.
>
> **5. La production tactique en volume.** Nous n'ingérons pas de flux d'indicateurs. Notre détection repose sur les mesures en place et sur les recherches ponctuelles.
>
> *Ces renoncements sont réexaminés annuellement.*

**Pourquoi ce document est le plus important du dossier de septembre** : il démontre qu'un choix a été fait. Un donneur d'ordre distingue immédiatement une organisation qui a arbitré d'une organisation qui n'a rien fait.

#### C.7 Corrigé — le premier produit mensuel

> **Suivi des menaces — mars — page 1/1**
>
> **CE QUI NOUS CONCERNE CE MOIS-CI**
> — Une vulnérabilité activement exploitée affecte notre outil de télégestion, version installée concernée. Correctif disponible. **Application prévue le 18 mars.**
> — Deux comptes de notre domaine figurent dans une fuite publiée le 4 mars. **Mots de passe réinitialisés le 6 mars.**
>
> **CE QUE NOUS AVONS VÉRIFIÉ ET QUI NE NOUS CONCERNE PAS**
> — Une campagne visant les établissements hospitaliers exploite un logiciel de gestion que nous n'utilisons pas.
> — Trois vulnérabilités signalées sur notre suite bureautique en ligne : corrigées par l'éditeur avant notre prise de connaissance, aucune action requise.
> — Une technique d'attaque décrite dans un bulletin exploite un protocole que nous bloquons depuis 2029.
>
> **CE QUE NOUS SURVEILLONS**
> — Une campagne visant les prestataires de santé à domicile, signalée par notre dispositif sectoriel. Vecteur non communiqué. **Nous avons posé la question.** Si le vecteur concerne notre outil de télégestion, nous vous en informerons sous 24 h.
>
> **CE QUE NOUS NE SAVONS PAS**
> — Notre inventaire des postes est incomplet (environ 30 non référencés). Nous ne pouvons pas garantir que les correctifs les couvrent.
>
> **CE QUE NOUS DEMANDONS**
> — Une décision sur la complétion de l'inventaire des postes : 3 jours de travail du technicien, à arbitrer.

**Ce que cette page démontre**, et c'est ce qui compte pour le donneur d'ordre : deux actions engagées, trois vérifications documentées, une surveillance avec critère, une lacune assumée, et une demande de décision.

#### C.8 Corrigé — démontrer la capacité en septembre

**Le dossier**, six pièces :

| # | Pièce | Ce qu'elle démontre |
|---|---|---|
| 1 | **Le registre des besoins** — 2 besoins, demandeurs, décisions éclairées | Une capacité orientée, pas une veille |
| 2 | **Le plan de collecte** avec la colonne « couverte » | Un choix de sources argumenté |
| 3 | **Les renoncements écrits** | Un arbitrage assumé |
| 4 | **Les six produits mensuels** | Une production régulière et datée |
| 5 | **Le registre des décisions** — ce qui a été fait grâce à quoi | **La preuve d'utilité** |
| 6 | La preuve d'adhésion sectorielle | Une insertion dans un dispositif reconnu |

**Ce qui fera la différence** : les pièces 3 et 5. La première parce qu'elle montre un arbitrage, la seconde parce qu'elle montre un effet.

⚠️ **Ce qu'il ne faut pas mettre dans le dossier** : le nombre de bulletins lus, le nombre de sources suivies, une description des outils. Aucun ne démontre une capacité.

#### C.9 Corrigé — la mesure à six mois

**Trois indicateurs, pas davantage** :

| Indicateur | Valeur attendue à 6 mois | Ce qu'il mesure |
|---|---|---|
| **Décisions documentées** | 4 à 8 | L'impact — le seul qui compte |
| **Menaces vérifiées et écartées** | 15 à 30 | Que le travail a lieu, et ce contre quoi on est protégé |
| **Temps réellement consacré** | ≈ 2 h 30/semaine | Que le dispositif est soutenable |

**Le troisième est souvent omis, et il est décisif dans une petite structure** : un dispositif qui consomme cinq heures par semaine au lieu de trois sera abandonné en un an. Le mesurer permet de le corriger avant l'abandon.

#### C.10 Ce que le cas enseigne

| Enseignement | Développement |
|---|---|
| **Deux besoins suffisent** | Et deux besoins servis valent mieux que six besoins effleurés |
| **La majorité des sources est déjà là** | Quatre lignes sur six du plan de collecte sont gratuites ou internes |
| **L'action la plus urgente n'est pas du CTI** | L'inventaire des postes conditionne tout — c'est le §40.1, question 5 |
| **Les renoncements écrits sont un livrable** | Ils démontrent un arbitrage à un donneur d'ordre |
| **La section « ce qui ne nous concerne pas » est la plus lue** | Elle répond à l'inquiétude, et elle prouve le travail |

**Le barème** :

| Critère | Pts |
|---|---|
| Commencer par les entretiens, pas par les sources | 15 |
| Deux besoins seulement, justifiés | 15 |
| Identifier les deux sources internes gratuites | 15 |
| Relever que l'inventaire conditionne tout | 15 |
| Renoncements écrits, avec motifs | 15 |
| Produit mensuel avec les cinq sections | 15 |
| Trois indicateurs dont le temps consommé | 10 |

**Élimination** : proposer une souscription commerciale, ou plus de trois besoins.

---


## ANNEXES

Les annexes de ce cours sont une **boîte à outils active**, utilisable sans relire les chapitres.

### Plan d'accès — trouver la bonne annexe en dix secondes

| J'ai besoin de… | Annexe |
|---|---|
| Comprendre un terme | **A** — glossaire |
| Choisir ou évaluer une source | **B** — fiches par type de source |
| Calibrer, évaluer, construire une matrice d'hypothèses | **C** — grilles |
| Un formulaire à remplir | **D** — templates |
| Comprendre une famille d'outils | **E** — outils *(versionnée)* |
| Savoir ce que le cadre juridique impose | **F** — juridique *(versionnée)* |
| Vérifier si je tombe dans un piège connu | **G** — pièges analytiques |
| Retrouver une source de veille ou une échéance | **H** — sources et calendrier *(versionnée)* |
| Concevoir un référentiel de renseignement | **I** — modèle de données |
| Définir un processus de traitement | **J** — workflow |
| Définir un indicateur, m'auto-évaluer | **K** — indicateurs et maturité |
| Une liste à cocher | **L** — checklists |
| Vérifier d'où vient une affirmation datée | **M** — registre de sources *(versionnée)* |

**Apprendre ou consulter ?** A, C, G et K se **lisent**. B, D, I, J et L se **remplissent**. E, F, H et M se **vérifient** et se périment — ce sont elles qui portent la maintenance du document.

---


## Annexe A — Glossaire

**Alerte** — Produit qui interrompt le rythme normal et déclenche une action immédiate. Quatre conditions cumulatives. §27.1
**Analyse d'hypothèses concurrentes** — Technique consistant à évaluer plusieurs hypothèses contre les mêmes éléments, en cherchant ce qui discrimine. §8.2
**Ancrage** — Biais par lequel la première information reçue fixe le cadre d'interprétation. §7.3
**Applicabilité** — Le produit, la version ou la configuration concernés existent-ils chez vous. Première condition du passage du général au « nous ». §19.4
**Archivage motivé** — Décision de ne pas traiter un élément, avec son motif écrit. Ce qui distingue une décision d'un oubli. §15.4
**Attribution** — Rattachement d'une activité à son auteur. Quatre niveaux ; les deux derniers concernent rarement un défenseur. §13.1
**Avocat du diable** — Rôle explicitement attribué consistant à attaquer la conclusion retenue. §8.5
**Axiome** — L'un des six énoncés fondateurs du chapitre 4, réutilisés dans tout le cours.
**Besoin prioritaire de renseignement** — Question formulée par un décideur nommé, éclairant une décision datée. §14.1
**Biais du client** — Production, sans intention consciente, du renseignement que le destinataire attend. §7.7
**Boucle analytique** — Question → collecte → analyse → jugement → décision → retour. Le modèle mental du cours. §1.2
**Calibrage** — Expression explicite de la probabilité et du niveau de confiance. §9
**Campagne** — Ensemble d'activités regroupées **par l'analyste** parce qu'elles partagent assez de caractéristiques pour être raisonnées ensemble. Construction analytique, pas objet du monde. §19.1
**Chaîne d'attaque** — Modèle linéaire d'étapes. Utile pour expliquer. §18.3
**Chaîne de provenance** — Qui a dit quoi le premier, sur quelle base, par combien de mains. §10.3
**Circularité** — Plusieurs sources apparentes remontant à une source unique. §10.4
**Clause de réfutation** — Section indiquant ce qui invaliderait une analyse. Marqueur de maturité, absent huit fois sur dix. §11.3
**Collecte** — Segment ② de la boucle. Vient toujours après le besoin. §14
**Confiance (niveau de)** — Solidité de la base d'une évaluation. **Indépendante de la gravité et de la probabilité.** §9.1
**Connaissance** — Information intégrée à un ensemble extérieur. Troisième des cinq objets. §2.1
**Consensus prématuré** — Convergence rapide d'un groupe avant que des alternatives aient été formulées. §12.6
**Corroboration** — Confirmation par une source **indépendante**. À distinguer de la reprise. §10.4
**Destinataire** — Personne nommée à qui un produit est adressé. Sans lui, il n'y a pas de renseignement. §1.1
**Différer** — Décision de ne pas trancher faute d'information, avec une action de collecte. À distinguer de *surveiller*. §29.1
**Diamant (modèle du)** — Modèle à quatre sommets, utile pour relier. §18.3
**Donnée** — Fait brut, sans contexte. Premier des cinq objets. §2.1
**Empreinte informationnelle** — Ce que votre organisation révèle d'elle-même, licitement observable. §34
**Estimation** — Jugement argumenté, calibré. À distinguer d'un fait. §6.4
**Fatigue d'alerte** — Dégradation progressive de la réaction aux alertes, produite par les alertes injustifiées. §27.4
**Fatigue de veille** — Épuisement de la capacité de lecture, dont le remède est de réduire les sources. §21.4
**Fiabilité** — Qualité de la **source**. Distincte de la crédibilité, qui porte sur l'information. §10.1
**Fiche de renseignement post-incident** — Extraction, par le CTI, de ce qu'un incident apprend et qui servira ailleurs. §23.6
**Hypothèse** — Explication candidate. Il en faut toujours plusieurs. §6.1
**Hypothèse clé** — Présupposé tenu pour acquis sans avoir été formulé, et qui effondre le raisonnement s'il est faux. §8.6
**Ignorer** — Décision la plus fréquente. Légitime, à condition d'être tracée. §29.5
**Indicateur** — Élément technique observable. Bas de la pyramide de la difficulté, péremption rapide. §3.3
**Jugement analytique** — Évaluation argumentée, calibrée et réfutable. Cinquième des cinq objets. §2.1
**Marquage de diffusion** — Ce que le destinataire peut retransmettre. Distinct de la permission d'action. §20.5
**Niveau opérationnel** — Le plus utile et le moins produit, parce qu'il exige de connaître la menace **et** votre organisation. §3.4
**Niveau stratégique** — Le plus demandé et le plus mal fait. §3.5
**Niveau tactique** — Le plus périssable et le plus vendu. §3.3
**Non mesuré** — Ce dont on ignore l'état. Ne devient jamais « conforme » ni « absent » par défaut.
**Permission d'action** — Ce que le destinataire a le droit de faire d'une information. §20.5
**Pivot** — Découverte d'éléments liés à partir d'un élément connu. Exploitable au premier niveau. §24.2
**Plan de collecte** — Tableau reliant chaque question à une source, une fréquence, un responsable. Sa colonne la plus utile : « déjà couvert ». §14.4
**Probabilité** — Estimation sur le monde. Distincte de la confiance. §9.1
**Produit** — Tout livrable diffusé par la fonction. Cinq types. §5.3
**Pyramide de la difficulté** — Hiérarchie des objets détectables selon leur coût de contournement. §18.4
**Renseignement** — Connaissance répondant à un besoin de décision identifié. Quatrième des cinq objets. §2.1
**Reprise** — Source qui n'apporte aucun élément propre. Présumée telle jusqu'à preuve du contraire. §10.10
**Retour d'expérience analytique** — Relecture de ses propres estimations pour vérifier l'alignement confiance/justesse. Segment ⑥. §35.6
**Revue par les pairs** — Relecture en six points formels, douze minutes. Le relecteur n'a pas besoin d'être analyste. §12.2
**Surveiller** — Décision de définir ce qui déclencherait une action. À distinguer de *différer*. §29.1
**Veille** — Suivi de sources. **N'est pas du renseignement** : trois questions le distinguent. §1.4

---


## Annexe B — Fiches par type de source

> Format uniforme : ce qu'elle apporte · ce qu'elle ne donne pas · fiabilité · fraîcheur · effort · piège spécifique.

### B.1 Catalogue d'exploitation avérée
**Apporte** le signal le plus fort du domaine : l'exploitation observée · **Ne donne pas** votre applicabilité, ni le contexte · **Fiabilité** élevée · **Fraîcheur** bonne · **Effort** très faible, 5 min/jour · **Piège** il arrive tard : quand c'est publié, l'exploitation est massive (§19.3).

### B.2 Avis des éditeurs de vos produits
**Apporte** la source de vérité sur les versions affectées et corrigées · **Ne donne pas** l'exploitation observée, ni le ciblage · **Fiabilité** élevée sur le factuel · **Fraîcheur** excellente · **Effort** faible · **Piège** la formulation minimise parfois la portée ; lire la description technique, pas le résumé.

### B.3 Autorités et centres de réponse nationaux
**Apporte** alertes, contexte national, recommandations · **Ne donne pas** ce qui vous vise spécifiquement · **Fiabilité** élevée · **Fraîcheur** bonne · **Effort** faible · **Piège** prudence sur l'attribution : ce qui n'est pas dit ne l'est pas par choix.

### B.4 Dispositif de partage sectoriel
**Apporte** l'antériorité, le contexte sectoriel, la réponse aux questions · **Ne donne pas** une couverture exhaustive · **Fiabilité** élevée · **Fraîcheur** excellente · **Effort** adhésion + réciprocité · **Piège** « plusieurs sources publiques » masque souvent une source unique (§10.9).

### B.5 Publications de chercheurs et d'éditeurs
**Apporte** l'analyse technique la plus profonde disponible · **Ne donne pas** votre contexte · **Fiabilité** variable selon le domaine · **Fraîcheur** variable · **Effort** moyen · **Piège** l'intérêt commercial porte sur l'évaluation de portée, pas sur l'analyse technique (§10.5).

### B.6 Presse spécialisée
**Apporte** une alerte rapide · **Ne donne pas** de base vérifiable · **Fiabilité** faible · **Fraîcheur** excellente · **Effort** faible · **Piège** perte du mode systématique : une évaluation prudente devient un constat (§10.9, extrait 2).

### B.7 Réseaux professionnels
**Apporte** des signaux faibles, des retours d'expérience · **Ne donne pas** de vérification · **Fiabilité** faible · **Fraîcheur** excellente · **Effort** élevé, bruit important · **Piège** servent à **repérer**, jamais à **établir**.

### B.8 Flux commercial d'indicateurs
**Apporte** agrégation, normalisation, parfois une avance · **Ne donne pas** ce qui vous concerne · **Fiabilité** variable · **Fraîcheur** à mesurer (test 3) · **Effort** intégration · **Piège** le volume est l'argument commercial et le critère le plus fallacieux (§22.4).

### B.9 Surveillance de fuites et de marque
**Apporte** ce que rien d'autre ne couvre : mentions de vos produits, présence de votre domaine dans des fuites · **Ne donne pas** d'analyse · **Fiabilité** bonne · **Effort** faible une fois en place · **Piège** vérifier la fraîcheur avant d'agir.

### B.10 Vos incidents
**Apporte** vecteur réel, séquence, ce qui a arrêté l'adversaire, ce qui n'a pas détecté · **Ne donne pas** ce qui n'est pas encore arrivé · **Fiabilité** maximale · **Effort** 1 jour par fiche · **Piège** le rapport de réponse à incident n'est pas une fiche de renseignement (§32.5).

### B.11 Vos tentatives bloquées
**Apporte** ce qui est activement testé contre vous · **Ne donne pas** ce qui a réussi · **Fiabilité** maximale · **Effort** 30 min/mois · **Piège** existe partout, n'est presque jamais regardé (§23.3).

### B.12 Vos métiers et votre support
**Apporte** signaux faibles, tentatives d'ingénierie sociale, inquiétudes clients · **Ne donne pas** de contexte technique · **Effort** 15 min/trimestre par interlocuteur · **Piège** ils ne pensent pas détenir du renseignement : il faut demander.

---


## Annexe C — Grilles d'évaluation, de calibrage et d'analyse

### C.1 Les six axiomes — grille de relecture

| Axiome | Question posée au texte | ☐ |
|---|---|---|
| Observer ≠ conclure | Y a-t-il des verbes d'intention en section factuelle ? | ☐ |
| Corrélation ≠ causalité | Une concomitance est-elle présentée comme une cause ? | ☐ |
| Absence de preuve | Une conclusion est-elle tirée du vide ? | ☐ |
| Périssabilité | Le produit porte-t-il une date de validité ? | ☐ |
| Analyse ≠ description | Une conclusion est-elle assumée ? | ☐ |
| Source ≠ fait | Le mode des sources reprises a-t-il été conservé ? | ☐ |

### C.2 Échelle de probabilité

| Expression | Fourchette indicative |
|---|---|
| Quasi certain | > 90 % |
| Très probable | 75 - 90 % |
| Probable | 55 - 75 % |
| Aussi probable qu'improbable | 45 - 55 % |
| Peu probable | 25 - 45 % |
| Très peu probable | 10 - 25 % |
| Quasi exclu | < 10 % |

**Règles** — un seul mot par affirmation · le mot porte sur une affirmation précise · les chiffres sont indicatifs · l'échelle est publiée en annexe de chaque produit.

### C.3 Échelle de confiance

| Niveau | Caractéristiques |
|---|---|
| **Élevée** | Sources multiples et indépendantes · information récente · raisonnement sans zone d'ombre |
| **Moyenne** | Sources limitées ou corroboration incertaine · un présupposé non vérifié |
| **Faible** | Source unique · information ancienne · nombreux présupposés |

**Règle absolue** : le niveau est **toujours expliqué en une ligne**.

### C.4 Les sept biais — grille de relecture

| Biais | Signe dans le texte | ☐ |
|---|---|---|
| Confirmation | « Plusieurs éléments confirment » · aucune alternative | ☐ |
| Ancrage | La conclusion est celle du premier jour | ☐ |
| Disponibilité | Explication sophistiquée là où une banale suffirait | ☐ |
| Saillance | Le détail romanesque prime sur le décisif | ☐ |
| Récence | La conclusion a changé à la dernière information | ☐ |
| Groupe / récit dominant | Tous les produits concluent dans le même sens | ☐ |
| Client | Le produit conforte une décision en préparation | ☐ |

### C.5 Matrice d'hypothèses concurrentes

**Notation** : `++` fortement attendu · `+` compatible · `0` neutre · `−` peu compatible · `−−` fortement contredit

| Élément | Source | Date | H-A | H-B | H-C |
|---|---|---|---|---|---|
| | | | | | |

**Lecture** : on **élimine** les hypothèses portant un `−−`, on ne retient pas celle qui a le plus de `++`.

**Hypothèses clés** *(ce que je tiens pour acquis)* :

| Présupposé | Vérifié ? | Si faux |
|---|---|---|

### C.6 Fiche d'évaluation de source

| Champ | Valeur |
|---|---|
| Source, type, date | |
| **Position pour savoir** | |
| **Intérêt identifié** | |
| Fiabilité — **et pourquoi, une ligne** | |
| **Chaîne de provenance** : primaire ou reprise ? | |
| **Indépendance** des autres sources dont je dispose | |
| Méthodologie déclarée | ☐ oui ☐ non ☐ partielle |
| Périmètre d'observation déclaré | ☐ oui ☐ non |
| Crédibilité de l'information — **et pourquoi** | |
| **Éléments propres apportés** | |
| Décision | ☐ utilisable ☐ si corroboré ☐ écarter — motif : |

### C.7 Grille de relecture par les pairs — 12 minutes

| # | Point | Question | ☐ |
|---|---|---|---|
| 1 | Faits / estimations | Verbes d'intention en section factuelle ? | ☐ |
| 2 | Hypothèses alternatives | Présentes et discriminées ? | ☐ |
| 3 | Calibrage | Probabilité **et** confiance justifiée ? | ☐ |
| 4 | Sources | Provenance tracée, indépendance vérifiée ? | ☐ |
| 5 | Réfutation | Clause présente et opérationnelle ? | ☐ |
| 6 | Utilité | Le destinataire saura-t-il quoi faire ? | ☐ |

**Le relecteur n'a pas besoin d'être analyste.**

### C.8 Grille de couverture besoins × sources

| Besoin | Question | Source envisagée | Coût | **Déjà couvert ?** |
|---|---|---|---|---|

### C.9 Les quatre conditions du général au « nous »

| # | Condition | ☐ | Vérifié par |
|---|---|---|---|
| 1 | **Applicabilité** — le produit/version/configuration existent chez nous | ☐ | |
| 2 | **Accessibilité** — le vecteur est ouvert | ☐ | |
| 3 | **Absence de neutralisation** — aucune mesure existante ne l'annule | ☐ | |
| 4 | **Plausibilité** — nous sommes dans le périmètre visé, ou disponibles | ☐ | |

**Les conditions 1 à 3 se vérifient chez vous, pas dans le renseignement reçu.**

---


## Annexe D — Templates

> Douze formulaires remplissables. Champs `[ ]` à compléter, **(O)** obligatoires.

### D.1 — Registre des besoins

`BES-[aaaa]` · Révision semestrielle

| Réf | Question **(O)** | Demandeur **(O)** | Décision éclairée **(O)** | Échéance | Niveau | Statut |
|---|---|---|---|---|---|---|
| B-01 | `[question, avec un point d'interrogation]` | `[nom]` | `[ ]` | `[date]` | strat/opé/tact | actif / satisfait / reporté / abandonné |

**Section obligatoire — ce que nous avons décidé de ne pas suivre**

| Sujet écarté | Motif | Date | Réexamen |
|---|---|---|---|

**Validation** — un besoin sans demandeur nommé, sans décision identifiée ou sans échéance n'est pas un besoin.

### D.2 — Plan de collecte

| Question | Besoin | Source | Type | Fréquence | Coût | Responsable | **Déjà couvert ?** |
|---|---|---|---|---|---|---|---|

**La colonne « déjà couvert » est celle qui produit l'information la plus utile.**

### D.3 — Matrice d'hypothèses concurrentes

Voir §C.5. En-tête à compléter : question analytique · demandeur · date · **date de réexamen** · analyste · relecteur.

### D.4 — Évaluation

| Section | Contenu | Longueur |
|---|---|---|
| En-tête | Question · demandeur · date · **réexamen** · analyste · relecteur | 3 lignes |
| **Réponse en une phrase** | `[Nous estimons] [probabilité] [affirmation] — [confiance], [pourquoi]` | 1 phrase |
| **Ce que cela implique** | 3 à 5 lignes | 5 lignes |
| **Ce que nous observons** | Faits, source, date. Aucun verbe d'intention | ½ p. |
| **Ce que nous en estimons** | Hypothèses · discrimination · conclusion · hypothèse suivante | ½ à 1 p. |
| **Ce qui invaliderait** | 2 à 4 lignes opérationnelles | 4 lignes |
| **Ce qui trancherait** | Questions à poser, données à obtenir | 3 lignes |
| **Ce que nous recommandons** | Section séparée, **avec coût estimé** | ½ p. |
| **Ce que nous ne savons pas** | Lacunes et leur effet | 3 lignes |
| Annexe | Échelle de calibrage | 1 p. |

### D.5 — Alerte

`ALT-[aaaa]-[nn]` · **Vérification des quatre conditions, tracée dans le message**

```
① OBJET          [une phrase calibrée]
② APPLICABILITÉ  [factuel, précis : version, actif, exposition]
③ DÉLAI          [de quoi disposons-nous]
④ ACTION         [ce que nous demandons, à qui]
⑤ SUITE          [quand le prochain point]
```

☐ Applicabilité établie ☐ Urgence réelle ☐ **Action possible maintenant** ☐ Inaction déraisonnable

**5 à 10 lignes. Ni acteur, ni mécanisme, ni indicateurs.**

### D.6 — Information avec engagement de suivi

*Catégorie intermédiaire, quand la condition ③ n'est pas remplie.*

```
[Objet]. Nous suivons [fréquence]. Nous alerterons dès qu'une action
sera possible. Prochaine mise à jour : [date].
```

### D.7 — Les cinq bulletins

| Destinataire | Longueur | Ce qu'on retient | Ce qu'on écarte | Ligne obligatoire |
|---|---|---|---|---|
| **Direction** | 10 lignes | Implication métier, coût, échéance | Technique, indicateurs, acteurs | **« Ce que nous attendons de vous »** |
| **RSSI** | 1-2 p. | Évaluation complète, effet sur le dispositif | Ce qu'il a déjà lu | Ce que cela dit de nos angles morts |
| **Vulnérabilités** | ½ p. | Identifiants, applicabilité, ordre | Le contexte | **« Non prioritaire : … »** |
| **Détection** | Tableau | Comportements, techniques, indicateurs | Le contexte stratégique | **Date · source · confiance · action** |
| **Produit** | 12 lignes | Applicabilité version par version | — | Obligation de signalement et délai |
| **Client** | 8 lignes | Ce qui les concerne, ce qui est fait, ce qu'ils doivent faire | **Nos hypothèses, nos lacunes, notre organisation** | Un contact |

### D.8 — Fiche de renseignement post-incident

*Produite par le CTI, à la clôture. Critère : progression au-delà de l'actif initial, ou détection > 48 h.*

| Section | Contenu | Destinataire |
|---|---|---|
| **Vecteur d'entrée** | Précis, avec la mesure qui aurait dû l'empêcher | Vulnérabilités, architecture |
| **Séquence observée** | Étapes, techniques | Détection |
| **Indicateurs** | Avec 1ʳᵉ et dernière observation | Détection, sectoriel |
| **Ce qui a arrêté l'adversaire** | La mesure efficace, nommée | **Direction** |
| **Ce qui n'a pas détecté** | Écart localisé | Détection |
| **Délai entrée → détection** | En heures ou jours | Indicateur de capacité |
| **Ce qui est partageable** | Décidé élément par élément | Sectoriel |
| **Ce que cela change** | Décisions à réexaminer | Tous |

### D.9 — Contribution à la détection

```
CONTEXTE          [campagne, menace]
SÉQUENCE ATTENDUE [si cela nous atteignait, voici ce qu'on observerait]
CE QUI EST ANORMAL [le critère de distinction avec l'activité légitime]
SOURCES NÉCESSAIRES [disponibles / manquantes]
FENÊTRE DE RECHERCHE RÉTROSPECTIVE [depuis quand]
INDICATEURS        [en annexe, avec date · source · confiance · action]
```

### D.10 — Contribution à la priorisation

| Constat | **Apporté par le CTI** | | | **Apporté par la gestion des vulnérabilités** | | |
|---|---|---|---|---|---|---|
| | Exploitation | Facilité | Ciblage secteur | Applicabilité | Exposition | Criticité |

### D.11 — Grille d'évaluation d'un flux

| Test | Résultat |
|---|---|
| **1 — Recouvrement avec le gratuit** | `[ ]` % |
| **2 — Pertinence** | `[ ]` % concernent nos produits/secteur |
| **3 — Fraîcheur** | avance moyenne de `[ ]` jours |
| **4 — Exploitabilité** | date · source · contexte · action : ☐ |
| **5 — Faux positifs** | `[ ]` sur 50 appliqués |
| Coût total | licence + intégration + traitement |
| Réversibilité | export brut ☐ · historique en fin de contrat ☐ |
| **Décision** | souscrire / négocier / reporter / renoncer — motif : |

### D.12 — Dispositif CTI minimal *(petite organisation)*

| Élément | Cible |
|---|---|
| Besoins | **2**, pas plus |
| Sources | 3 gratuites + 1 adhésion sectorielle |
| Produit | Une page par mois, cinq sections |
| Destinataires | 2 à 3, nommés |
| **Renoncements écrits** | 5, avec motifs |
| Temps | ≈ 3 h/semaine, **mesuré** |

**Le produit mensuel** : ce qui nous concerne · **ce que nous avons vérifié et qui ne nous concerne pas** · ce que nous surveillons · ce que nous ne savons pas · ce que nous demandons.

---


## Annexe E — Familles d'outils

> ⏱ **Annexe versionnée — vérifiée le 2 août 2026.** Péremption recommandée : 12 mois.
> Organisée par **famille**. Aucun tarif : les prix se négocient, dépendent du périmètre et se périment. Seuls les modèles de facturation sont structurants.

### E.1 Les familles

| Famille | Ce qu'elle fait | Modèle | Quand elle se justifie | Limite |
|---|---|---|---|---|
| **Plateforme de renseignement** | Ingestion, normalisation, déduplication, enrichissement, diffusion | Par utilisateur · par volume · libre | **Au-delà de quelques centaines d'éléments/mois** | Ne raisonne pas (§36.1) |
| **Flux d'indicateurs** | Volume d'éléments techniques | Par abonnement | Rarement seul | Recouvrement élevé avec le gratuit |
| **Renseignement sectoriel** | Ciblé sur votre secteur | Adhésion · abonnement | **Souvent le meilleur rapport** | Dépend de l'activité des membres |
| **Surveillance de fuites et de marque** | Mentions, données divulguées | Par domaine · par marque | **Besoin non couvert autrement** | Faux positifs à qualifier |
| **Surveillance de surface exposée** | Ce qui est visible de vous | Par domaine | Chevauche la gestion des vulnérabilités | Vue externe uniquement |
| **Enrichissement d'infrastructure** | Résolution passive, certificats, balayage | À la requête · abonnement | Vérification avant blocage | Photographie datée |
| **Analyse de maliciel** | Décomposition d'échantillons | À la soumission | Si vous en recevez | ⚠️ **Confidentialité** de ce que vous soumettez |
| **Renseignement sur mesure** | Réponse à vos questions | Sur devis | Besoin précis, ponctuel | Très coûteux |

### E.2 Formats et protocoles

| Objet | Rôle | Ce qu'il exprime mal |
|---|---|---|
| **STIX** | Représentation d'objets et de relations | **Le raisonnement, la nuance, la confiance argumentée** |
| **TAXII** | Protocole d'échange | — |
| Formats d'analyste alternatifs | Contexte, appréciation | Standardisation moindre |

### E.3 Critères de sélection, par ordre

1. **Le besoin est-il formulé ?** Sinon, aucun outil ne convient.
2. **Le volume justifie-t-il l'outil ?** En dessous de quelques centaines d'éléments par mois, un tableur suffit.
3. **Les cinq tests du §22.3** ont-ils été conduits ?
4. **L'export brut** est-il contractuellement garanti ?
5. **Le rapprochement automatique avec l'inventaire** est-il possible ? C'est le gain le plus élevé (§36.3).
6. **Coût total** : licence + intégration + maintenance + traitement.

⚠️ **Sur la soumission d'échantillons à des services d'analyse** : ce que vous soumettez peut devenir accessible à des tiers, y compris à l'adversaire qui saura ainsi que vous l'avez détecté. C'est le §34.3.

---


## Annexe F — Cadre juridique

> ⏱ **Annexe versionnée — vérifiée le 2 août 2026.** Ce document ne constitue pas un avis juridique. Il indique quelles questions poser, à qui, et dans quel ordre.

### F.1 Les quatre questions préalables à toute collecte

| # | Question | Qui répond |
|---|---|---|
| 1 | L'information est-elle **publiquement accessible**, sans contournement ? | Vous, avec le critère du §20.1 |
| 2 | Contient-elle des **données à caractère personnel** ? | Délégué à la protection des données |
| 3 | Ai-je une **base légitime** pour la traiter et la conserver ? | Délégué + juridique |
| 4 | Puis-je **documenter** comment je l'ai obtenue ? | Vous |

### F.2 Régimes à instruire, par thème

| Thème | Ce qu'il faut établir | Interlocuteur |
|---|---|---|
| **Protection des données** | Finalité, minimisation, durée, information, sécurité · inscription au registre des traitements | Délégué |
| **Partage d'informations** | Régime applicable dans votre juridiction et celle du destinataire · protections éventuelles · clause de réexamen | Juridique |
| **Accès à des espaces fermés** | Ce qui constitue une intrusion · ce que l'inscription sous identité fictive implique | Juridique |
| **Détention de données divulguées** | Finalité, durée, accès restreint | Délégué + juridique |
| **Signalement produit** | Régime applicable, délais, plateforme | Juridique + affaires réglementaires |
| **Communication externe** | Ce qui engage l'organisation · validation requise | Juridique + direction |

### F.3 ⏱ État daté

Un régime de protection majeur du partage d'indicateurs, en vigueur depuis dix ans dans une juridiction de référence, a **expiré fin septembre 2025**, a fait l'objet de **deux prolongations sans modification de fond**, et arrive à échéance à la **fin du mois de septembre 2026** — soit huit semaines après la rédaction de ce document. Pendant la période de vacance, le partage a continué, mais plusieurs organisations ont réduit ce qu'elles transmettaient. 📎 [S-03]

**L'enseignement qui survivra à l'issue** : le cadre du partage peut disparaître. Prévoyez une clause de réexamen, et ne construisez pas un processus qui dépende d'un régime particulier.

### F.4 Les sept interdits

| # | Interdit |
|---|---|
| 1 | Accéder à un système sans autorisation, même pour observer |
| 2 | Acheter des données volées ou un accès |
| 3 | Conduire une action offensive, même en riposte |
| 4 | Usurper une identité pour obtenir de l'information |
| 5 | Conserver sans finalité des données personnelles collectées |
| 6 | Transmettre en violation d'un marquage reçu |
| 7 | Attribuer publiquement sans base solide |

### F.5 Marquage — les deux dimensions

| Dimension | Question | Niveaux indicatifs |
|---|---|---|
| **Diffusion** | À qui puis-je le retransmettre ? | libre · communauté · organisation · destinataire seul |
| **Action** | Qu'ai-je le droit d'en faire ? | agir · agir en interne · analyser seulement · rien sans accord |

⚠️ Marquer tout au niveau le plus restrictif rend votre renseignement inutilisable et vous coupe des échanges. Le marquage se décide **par produit**.

---


## Annexe G — Catalogue des pièges analytiques

*Quarante-cinq pièges, classés par étape de la boucle. Pour chacun : le mécanisme, et le contrôle qui le détecte.*

### G.1 Question et besoin

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 1 | Collecter sans besoin | Aucune question formulée | Le plan de collecte est vide |
| 2 | Le sujet pris pour un besoin | « La menace rançongiciel » | Pas de point d'interrogation |
| 3 | Le besoin sans demandeur | « La direction » | Aucun nom |
| 4 | Le besoin sans décision | « Pour information » | On ne peut pas nommer la décision |
| 5 | La question sans réponse concevable | « Sommes-nous ciblés ? » | Aucune source n'y répond |
| 6 | Le besoin sans échéance | Systématiquement dépriorisé | Aucune date |
| 7 | La collecte tous azimuts | Faute de savoir quoi chercher | Aucune source écartée |

### G.2 Collecte et sources

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 8 | **La circularité** | Trois reprises d'une source unique | Retirer une source : reste-t-il quelque chose ? |
| 9 | « Plusieurs sources publiques » | Compte des publications, pas des observations | Demander lesquelles |
| 10 | La perte du mode | Une évaluation devient un fait | Comparer avec la source d'origine |
| 11 | L'auréole de la source | Le crédit s'étend à tout ce qu'elle publie | Évaluer par domaine |
| 12 | Fiabilité confondue avec crédibilité | Source sérieuse, affirmation fausse | Deux axes distincts |
| 13 | Le biais de télémétrie | L'éditeur voit ses clients | Périmètre d'observation déclaré ? |
| 14 | Le volume pris pour la valeur | Argument commercial | Combien ont produit une action ? |
| 15 | Le flux gratuit ingéré non lu | Personne ne l'a relié à l'inventaire | Vérifier avant toute souscription |
| 16 | La source qui n'apporte rien de propre | Reprise déguisée | Colonne « éléments propres » |
| 17 | La fatigue de veille | Volume infini, pertinence faible | Retard de la file > 3 jours |
| 18 | Ajouter des sources pour se rassurer | Substitut à la décision | Le plan de collecte grossit sans besoin |

### G.3 Analyse

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 19 | L'hypothèse unique | Le cerveau en produit une et la confirme | Trois hypothèses écrites ? |
| 20 | Chercher ce qui confirme | Au lieu de ce qui discrimine | Éléments compatibles avec toutes ? |
| 21 | L'accumulation d'indices faibles | Dix faibles ne font pas un fort | Combien ne vont **que** dans mon sens ? |
| 22 | La plausibilité prise pour la probabilité | Le récit cohérent convainc | Quelle observation la rendrait fausse ? |
| 23 | L'explication irréfutable | Aucune observation ne pourrait l'infirmer | C'est un défaut, pas une qualité |
| 24 | **Le regroupement par secteur** | Critère faible pris pour fort | Une victime hors secteur ? |
| 25 | Confirmation | « Plusieurs éléments confirment » | Grille §C.4 |
| 26 | Ancrage | La conclusion du premier jour survit | Ordre inversé, tiendrait-elle ? |
| 27 | Disponibilité | Explication sophistiquée par défaut | Fréquence de base ? |
| 28 | Saillance | Le romanesque prime sur le décisif | Quel élément discrimine ? |
| 29 | Récence | La dernière information l'emporte | Était-elle discriminante ? |
| 30 | Récit dominant | L'explication en vogue partout | Que dirait l'explication banale ? |
| 31 | **Biais du client** | Produire ce qui est attendu | Écrire avant de connaître l'usage |
| 32 | La piste non creusée | Ne laisse aucune trace | Relecture externe |
| 33 | Le consensus prématuré | Convergence en dix minutes | Écrire avant de discuter |
| 34 | Le pivot en chaîne | L'incertitude se multiplie | Premier niveau seulement |
| 35 | Le graphe qui ne sert à rien | Gratifiant et improductif | Quelle question tranche-t-il ? |

### G.4 Jugement et diffusion

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 36 | Refuser de conclure | Prudence apparente, transfert réel | Le destinataire doit analyser |
| 37 | Juger sans le dire | Appréciation présentée comme fait | Séparation des sections |
| 38 | « Possible » | Signifie « non exclu », donc rien | Test du remplacement |
| 39 | La fausse précision | « 73 % » sans calcul | Le chiffre suggère une méthode absente |
| 40 | Fusionner les trois axes | « Menace critique » | Probabilité + confiance + gravité séparés |
| 41 | La clause de réfutation absente | Huit fois sur dix | Section obligatoire |
| 42 | La conclusion en dernier | Réflexe scolaire | Première phrase |
| 43 | Le mélange des niveaux | Un produit, cinq destinataires | Un produit par niveau |
| 44 | **L'alerte de couverture** | Alerter « au cas où » | Les quatre conditions tracées |
| 45 | L'archivage sans motif | Indiscernable d'un oubli | Motif obligatoire |

---


## Annexe H — Sources et calendrier

> ⏱ **Annexe versionnée — vérifiée le 2 août 2026.**

### H.1 Les quatre sources qui suffisent

| Source | Cadence | Ce qu'elle couvre | Coût |
|---|---|---|---|
| **Catalogue d'exploitation avérée** | 5 min/jour | Le signal le plus fort | Gratuit |
| **Avis des éditeurs de vos produits critiques** | 10 min/jour | La source de vérité sur votre applicabilité | Gratuit |
| **Bulletins du centre de réponse national** | 15 min/semaine | Contexte, alertes | Gratuit |
| **Dispositif de partage sectoriel** | 20 min/semaine | Ce qui vise vos pairs, en avance | Adhésion |

### H.2 Sources complémentaires, par besoin

| Besoin | Source | Effort |
|---|---|---|
| Analyse technique approfondie | Publications de chercheurs et d'éditeurs | Moyen |
| Mentions de vos produits | Surveillance dédiée, ou signalements clients | Faible à moyen |
| Présence dans des fuites | Service de surveillance | Faible une fois en place |
| Ce qui est testé contre vous | **Vos journaux de filtrage** | 30 min/mois, gratuit |
| Vos angles morts | **Vos incidents** | 1 jour par fiche, gratuit |

### H.3 Rythmes de péremption

| Objet | Validité typique |
|---|---|
| Empreinte de fichier | Une variante |
| Adresse | Jours à semaines |
| Nom de domaine | Semaines |
| Artefact d'hôte | Mois |
| Outil employé | Mois à années |
| **Comportement** | **Années** |
| Évaluation de motivation | Années |
| Cartographie de couverture | **À revoir à chaque version majeure du référentiel** |

### H.4 Échéances de veille structurelle

| Objet | Cadence de vérification |
|---|---|
| Versions majeures des référentiels de techniques | Semestrielle |
| Cadre juridique du partage | **Semestrielle, ou à échéance annoncée** |
| Obligations de signalement produit | Annuelle |
| Périmètre et statut de votre dispositif sectoriel | Annuelle |
| Contrat et performance de vos fournisseurs | Annuelle, avec les cinq tests |

### H.5 Formation et compétences

*Aucune certification ne couvre le contenu de ce cours.* Les compétences les plus utiles, par ordre :

| Compétence | Comment la développer |
|---|---|
| **Écrire clairement** | Pratique, relecture par des non-spécialistes |
| **Analyse structurée** | Littérature du renseignement, appliquée à des cas réels |
| Compréhension des systèmes et réseaux | Formation technique généraliste |
| Réponse à incident | Exercices, participation aux cellules |
| Compréhension juridique | Relation régulière avec le juridique et le délégué |

⚠️ Une certification atteste d'une connaissance, pas d'une pratique. Les compétences déterminantes de ce cours — tolérer l'incertitude, résister à la pression de conclure, savoir quand s'arrêter — ne s'enseignent pas en formation.

---


## Annexe I — Modèle de données

### I.1 Entité SIGNALEMENT

| Champ | Type | Card. | Valeurs | Obligatoire |
|---|---|---|---|---|
| `id` | str | 1 | Identifiant stable | Oui |
| `date_reception` | date | 1 | | Oui |
| `source` | ref | 1 | → SOURCE | Oui |
| `type` | enum | 1 | avis · bulletin · publication · signalement_client · incident_interne · journal_interne · question | Oui |
| **`besoin_rattache`** | ref | 0..1 | → BESOIN. **Vide = archivage** | Non |
| `statut` | enum | 1 | nouveau · qualifié · en_traitement · en_attente · diffusé · archivé | Oui |
| **`motif_archivage`** | str | 0..1 | **Obligatoire si statut = archivé** | Conditionnel |
| `decision` | enum | 0..1 | agir · préparer · surveiller · ignorer · différer | Si qualifié |
| `condition_reexamen` | str | 0..1 | | Si ignorer |
| `porteur` | ref | 0..1 | | Si agir ou préparer |
| `date_reexamen` | date | 0..1 | | Si surveiller ou ignorer |

### I.2 Entité BESOIN

`id` · `question` **(O)** · `demandeur` **(O)** · `decision_eclairee` **(O)** · `echeance` · `niveau` (strat/opé/tact) · `statut` (actif/satisfait/reporté/abandonné) · `date_creation` · `date_derniere_production` · `nb_decisions_produites`

⚠️ Le champ `date_derniere_production` permet la révision par obsolescence du §14.5 : un besoin sans production depuis six mois doit être réexaminé.

### I.3 Entité SOURCE

`id` · `nom` · `type` · `fiabilite` (élevée/moyenne/faible) · **`justification_fiabilite`** · `interet_identifie` · `primaire_ou_reprise` · `independance_de` (0..n → SOURCE) · `methodologie_declaree` (bool) · `perimetre_declare` (bool) · `cout_annuel` · `date_derniere_evaluation`

**Le champ `independance_de` est celui qui prévient la circularité** : il matérialise que deux sources ne sont pas indépendantes.

### I.4 Entité PRODUIT

`id` · `type` (note_orientation / fiche_operationnelle / jeu_indicateurs / alerte / reponse_question) · `besoin` (ref) · `destinataires` (0..n) · `date_diffusion` · `probabilite` · **`confiance`** · **`justification_confiance`** · `clause_refutation` · `date_reexamen` · `relecteur` · **`retour_demande`** (bool) · `retour_recu` · `decision_produite`

### I.5 Entité DÉCISION *(registre du §35.5)*

`id` · `produit` (ref) · `date` · `decideur` · `nature` · **`ce_qui_aurait_ete_fait_sans`** · `cout_evite_estime`

**Le champ en gras est celui qui rend le registre démontrable.** Sans lui, on ne mesure qu'une corrélation.

### I.6 Règles de qualité

| # | Règle | Fréquence |
|---|---|---|
| 1 | Aucun signalement archivé sans motif | Hebdomadaire |
| 2 | Aucun produit sans niveau de confiance justifié | À la diffusion |
| 3 | Aucun besoin sans production depuis 6 mois non réexaminé | Semestrielle |
| 4 | Aucune décision « surveiller » sans indicateur ni porteur | Mensuelle |
| 5 | Aucune source évaluée depuis plus de 12 mois | Annuelle |
| 6 | Aucun produit sans retour demandé | Hebdomadaire |

---


## Annexe J — Workflow de traitement

### J.1 Les cinq états

```
NOUVEAU ──qualification──► QUALIFIÉ ──rattaché à un besoin ?──┐
                                                    │          │
                                          NON ──► ARCHIVÉ     OUI
                                                 (motif)       │
                                                               ▼
                                                        EN TRAITEMENT
                                                          │        │
                                          info manquante  │        │
                                                          ▼        ▼
                                                   EN ATTENTE   RELECTURE
                                                          │        │
                                                          └────────┤
                                                                   ▼
                                                              DIFFUSÉ
                                                                   │
                                                          retour à J+14
```

### J.2 Champs obligatoires par état

| État | Exigences |
|---|---|
| Qualifié | Source · date · type · **besoin rattaché ou motif d'archivage** |
| En traitement | Analyste · date de début |
| En attente | **Ce qui manque** · à qui la demande a été faite · date de relance |
| Relecture | Relecteur nommé · grille en six points passée |
| Diffusé | Destinataires · **probabilité et confiance justifiée** · clause de réfutation · **retour demandé** |
| Archivé | **Motif** · condition de réexamen le cas échéant |

### J.3 Délais indicatifs

| Transition | Délai cible |
|---|---|
| Nouveau → qualifié | 24 h |
| Qualifié → en traitement | Selon la décision |
| En attente → relance | 5 jours |
| Diffusé → retour demandé | 14 jours |
| Revue hebdomadaire des archivés des 3 dernières semaines | **15 min/semaine** |

⚠️ **La dernière ligne est celle du §19.6** : c'est la revue des archivés qui a produit le rapprochement des trois signalements. Un archivage n'est pas une suppression.

### J.4 Chaîne d'un signalement produit

```
Signalement (client, chercheur, veille)
        ▼
Qualification : applicabilité version par version
        ▼
Évaluation : exploitation active ? périmètre client ?
        ▼
┌── Obligation de signalement déclenchée ? ──┐
│                                            │
OUI                                         NON
│                                            │
▼                                            ▼
Alerte précoce (délai réglementaire)    Correctif planifié
Notification                             Notification client
▼                                            │
Rapport final                                │
        └────────────┬───────────────────────┘
                     ▼
        Correctif publié · clients notifiés · dossier clos
```

---


## Annexe K — Indicateurs et maturité

### K.1 Les six indicateurs

| # | Indicateur | Famille | Comment le produire | Piège |
|---|---|---|---|---|
| 1 | Besoins actifs et statut | Production | Registre | Ne mesure pas l'utilité |
| 2 | Produits diffusés par niveau | Production | Registre | Peut augmenter en dégradant |
| 3 | **Taux de lecture et de réponse** | Usage | Trois questions à J+14 | Taux de réponse ≈ 60 %, c'est normal |
| 4 | **Décisions modifiées** | Impact | Registre des décisions | Exige le champ « sans nous » |
| 5 | **Menaces neutralisées documentées** | Impact | Motifs d'archivage | Ne prouve pas que le CTI protège |
| 6 | **Alignement confiance / justesse** | Retour | Retour d'expérience semestriel | Exige d'avoir calibré |

### K.2 Les faux indicateurs

| Indicateur | Pourquoi |
|---|---|
| Nombre de rapports | Activité, pas utilité |
| Volume d'indicateurs ingérés | Ce que le fournisseur collecte |
| Nombre de sources | Une accumulation |
| **Nombre d'alertes** | **Devrait diminuer** avec la maturité |
| Temps de veille | Une consommation |
| Menaces identifiées | Dépend de l'actualité |

### K.3 Le tableau du retour d'expérience analytique

| | Estimation juste | Estimation fausse |
|---|---|---|
| **Confiance élevée** | ✅ Excellent | ❌ **Le pire cas** |
| **Confiance faible** | ⚠️ Confiance sous-évaluée | ✅ **Bon travail** |

**On ne juge pas un analyste sur son taux d'exactitude, mais sur l'alignement entre sa confiance annoncée et sa justesse réelle.**

### K.4 Modèle de maturité, par domaine

| Niveau | Caractéristique | Preuve exigée |
|---|---|---|
| **0** | Aucune activité | — |
| **1** | Veille informelle | Quelqu'un lit des bulletins |
| **2** | Besoins formulés | Registre des besoins, avec demandeurs nommés |
| **3** | Production calibrée | Échelle publiée · confiance justifiée · clause de réfutation |
| **4** | Boucle fermée | Retours demandés · registre des décisions · relecture croisée |
| **5** | Fonction apprenante | Retour d'expérience analytique · alignement mesuré · besoins révisés |

**Grille d'auto-évaluation par domaine** :

| Domaine | Niveau | Preuve citée |
|---|---|---|
| Formulation des besoins | ☐ 0-5 | |
| Collecte et plan | ☐ | |
| Évaluation de source | ☐ | |
| Analyse et hypothèses | ☐ | |
| Calibrage | ☐ | |
| Production et diffusion | ☐ | |
| Exploitation et décision | ☐ | |
| Partage | ☐ | |
| Mesure et retour | ☐ | |
| Cadre juridique | ☐ | |

⚠️ Un domaine critique faible **plafonne** ce qui en dépend. Sans calibrage, la production ne peut pas dépasser le niveau 2 quelle que soit sa qualité par ailleurs.

### K.5 Chiffrage d'une fonction

| Poste | Souvent omis ? |
|---|---|
| Personnel | Non |
| Sources payantes et adhésions | Non |
| Outillage | Non |
| **Intégration et maintenance** | **Oui** |
| **Temps des destinataires** | **Presque toujours** |

**Calcul du dernier** : `nb produits × nb destinataires × temps de lecture`. Une fonction diffusant 4 produits/mois à 7 destinataires, 20 min chacun, consomme ≈ **45 h/an** de temps de cadres.

---


## Annexe L — Checklists

### L.1 Avant de diffuser un produit
☐ La conclusion est-elle en première phrase ? · ☐ Contient-elle probabilité **et** confiance justifiée ? · ☐ Les faits sont-ils séparés des estimations ? · ☐ Y a-t-il une clause de réfutation ? · ☐ Le destinataire sait-il ce qu'on attend de lui ? · ☐ Le produit est-il adapté à **ce** destinataire ? · ☐ Une date de réexamen figure-t-elle ? · ☐ Un retour est-il demandé ? · ☐ La relecture croisée a-t-elle eu lieu ?

### L.2 Avant d'alerter
☐ Applicabilité **établie** ? · ☐ Urgence réelle — attendre aggrave-t-il ? · ☐ **Action possible maintenant** ? · ☐ Inaction déraisonnable ? · ☐ Cinq à dix lignes ? · ☐ Décideur nommé ? · ☐ Prochain point annoncé ? · ☐ Les quatre conditions sont-elles tracées dans le message ?

### L.3 Avant de croire une source
☐ Primaire ou reprise ? · ☐ Sur quoi la source d'origine fonde-t-elle son affirmation ? · ☐ Les sources sont-elles **indépendantes** ? · ☐ Le mode a-t-il été conservé ? · ☐ Quels éléments propres apporte-t-elle ? · ☐ Quel est son intérêt ? · ☐ Le périmètre d'observation est-il déclaré ?

### L.4 Avant de conclure
☐ Trois hypothèses écrites, dont une bénigne et une ennuyeuse ? · ☐ Quel élément **discrimine** ? · ☐ Quelle observation rendrait ma conclusion fausse ? · ☐ Quels présupposés n'ai-je pas vérifiés ? · ☐ Ai-je passé la grille des sept biais ?

### L.5 Avant de bloquer un indicateur
☐ Fraîcheur — dernière observation ? · ☐ **Colocation** — combien d'autres services à cette adresse ? · ☐ Nos actifs communiquent-ils déjà avec ? · ☐ **Date de retrait fixée** ?

### L.6 Avant de partager à l'extérieur
☐ Que révèle chaque élément **de nous** ? · ☐ L'anonymisation résiste-t-elle au recoupement ? · ☐ Le marquage est-il posé ? · ☐ La décision est-elle prise **élément par élément** ? · ☐ Le niveau de confiance accompagne-t-il ?

### L.7 Avant de souscrire
☐ Le besoin est-il formulé ? · ☐ Les cinq tests ont-ils été conduits ? · ☐ Quel est le recouvrement avec le gratuit ? · ☐ Quelle avance sur la publication publique ? · ☐ L'export brut est-il garanti ? · ☐ Le volume justifie-t-il un outil ?

### L.8 Audit d'empreinte informationnelle *(annuel)*
☐ Offres d'emploi actives · ☐ Certificats publics et noms d'hôtes exposés · ☐ Métadonnées des documents publiés · ☐ Interventions publiques · ☐ Fuites contenant le domaine · ☐ Mentions de clients dans la communication

### L.9 Les douze premiers mois
☐ 3 à 6 besoins avec demandeur et décision · ☐ Inventaire permettant de vérifier l'applicabilité · ☐ File à cinq états avec archivage motivé · ☐ Échelle de calibrage publiée · ☐ Premier produit avec **retour demandé** · ☐ Registre des décisions tenu **dès le premier jour** · ☐ Cadre juridique instruit · ☐ Relecture croisée · ☐ Interfaces détection et vulnérabilités · ☐ Renseignement interne exploité · ☐ Tableau de bord six indicateurs · ☐ Premier retour d'expérience analytique

---


## Annexe M — Registre de sources

> ⏱ **Annexe versionnée — dernière vérification : 2 août 2026.**
> Niveau : `T` texte juridique · `D` documentation officielle · `N` norme ou standard · `S` source secondaire.

**[S-01]** — Projet ATT&CK (MITRE) — *notes de version v18 et v19*
Niveau `D` · Vérifié le 02/08/2026 · Utilisé au §1.8, §18.6, annexe H.
*Fait retenu* : la version 19, publiée le 28 avril 2026, scinde la tactique historique *Defense Evasion* en deux tactiques distinctes — *Stealth*, conservant l'identifiant TA0005, et *Defense Impairment*, TA0112. Volumétrie Entreprise : 15 tactiques, 222 techniques, 475 sous-techniques. La version 18, d'octobre 2025, avait introduit les objets *Detection Strategies* et *Analytics*. Une table de correspondance a été publiée pour le remappage.

**[S-02]** — Projet ATT&CK — *entrées documentant l'emploi de modèles de langage par des attaquants*
Niveau `D` · Vérifié le 02/08/2026 · Utilisé au §1.8, §10.7.
*Fait retenu* : des entrées de campagne et de logiciel documentent l'emploi de modèles de langage en opération, décrivant à la fois des opérations largement automatisées et un maliciel interrogeant un modèle en cours d'exécution.
⚠️ **Note de transparence** : l'un de ces cas concerne un usage détourné de Claude, l'assistant développé par Anthropic — l'organisation qui m'a créé. Ce cours le traite à partir des sources publiques, comme les autres.

**[S-03]** — Analyses juridiques concordantes sur le régime américain de partage d'indicateurs de 2015
Niveau `S` · Vérifié le 02/08/2026 · Utilisé au §1.8, §20.4, annexe F.3.
*Faits retenus* : le régime a expiré le 30 septembre 2025 · une première prolongation l'a porté au 30 janvier 2026 · une seconde au 30 septembre 2026 · aucune modification de fond n'a été apportée · pendant la période de vacance, le partage a continué avec une exposition juridique réévaluée par les participants.
⚠️ **Décision engageante** : à prendre sur le texte lui-même et sur avis juridique, jamais sur ces analyses.

**[S-04]** — OASIS — *STIX 2.1 et TAXII 2.1*
Niveau `N` · Vérifié le 02/08/2026 · Utilisé au §36.2, annexe E.2.
*Fait retenu* : standards OASIS stables depuis 2021.

### M.1 Ce qui n'est pas sourcé, et l'est assumé

Les éléments suivants relèvent d'une **doctrine proposée par ce cours**, non d'une exigence externe. Ils sont à adapter et à faire approuver :

| Élément | Où |
|---|---|
| L'échelle de probabilité en sept expressions et ses fourchettes | §9.3 |
| L'échelle de confiance en trois niveaux | §9.4 |
| Les quatre conditions d'une alerte justifiée | §27.1 |
| Le repère de 2 à 6 alertes par an | §27.2 |
| Les cinq tests d'évaluation d'un fournisseur | §22.3 |
| Le budget de 3 h/semaine en petite organisation | §39.1 |
| Les délais du workflow | Annexe J.3 |
| Le critère de production d'une fiche post-incident | §23.7 |
| Le modèle de maturité en six niveaux | Annexe K.4 |

⚠️ **Le principe** : mieux vaut une doctrine interne assumée qu'une valeur présentée comme une norme externe qu'elle n'est pas.

### M.2 À revérifier en priorité

| Priorité | Source | Motif |
|---|---|---|
| **1** | [S-03] | Échéance à huit semaines de la rédaction |
| **2** | [S-01] | Les référentiels évoluent structurellement, et pas seulement par ajout |
| **3** | [S-02] | Domaine en évolution rapide, forte couverture médiatique |
| 4 | [S-04] | Stable, revérification annuelle suffisante |

---


## Journal des modifications

| Version | Date | Nature |
|---|---|---|
| 1.0 | 02/08/2026 | Première rédaction : 8 parties, 40 chapitres, 3 cas de synthèse, 9 mini-labs, 13 annexes |

**Prochaine revue recommandée** : 28 février 2027, ou à la survenue d'un déclencheur.

**Déclencheurs de revue anticipée** : issue de l'échéance de septembre 2026 sur le régime de partage · nouvelle version majeure d'un référentiel de techniques · évolution des obligations de signalement produit · changement significatif dans le paysage des menaces assistées par modèles de langage.

**Sections à réviser en priorité** : §1.8 · §10.7 · §18.6 · §20.4 · annexes E, F, H et M.

---

*Fin du document.*
