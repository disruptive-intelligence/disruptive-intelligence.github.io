---
title: Chapitre 16 — Systèmes sans équipage
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie II — Le grand atlas
  - index.md
---

> **Périmètre de ce chapitre.** Il traite les plateformes sans équipage sous l'angle **technologique, industriel, économique et de gouvernance**. Il ne fournit aucun paramètre d'emploi, aucune méthode de mise en œuvre offensive, aucune technique de perturbation ou de contre-mesure — y compris lorsque ces informations sont publiquement accessibles. Cette règle s'applique phrase par phrase.
>
> **Ce que le chapitre ajoute.** Les chapitres 14 et 15 traitaient de machines opérant dans des espaces bornés. Celui-ci traite de machines qui opèrent **loin de leur opérateur**, ce qui introduit une contrainte nouvelle : la liaison.
>
> **Cinq entrées.**

---

## ◆◆◆ Drones aériens

**Niveau** — plateforme · **Couche** — agir, percevoir, relier

**En une phrase.** Des aéronefs sans équipage à bord, allant de quelques centaines de grammes à plusieurs tonnes, dont le point commun est d'être pilotés à distance ou de suivre un plan de vol automatique.

**Pourquoi on en parle.** Parce que **le mot désigne une vingtaine d'objets sans commune mesure** — et parce que dans la plupart des applications civiles, le verrou n'est pas technique.

**Comment ça fonctionne — et pourquoi les classes comptent.** La masse et le mode de sustentation déterminent presque tout : l'autonomie, la charge utile, le domaine de vol, et surtout le régime réglementaire applicable.

Un **multirotor** décolle verticalement, tient en vol stationnaire, et paie cette capacité par une autonomie qui se compte en dizaines de minutes — la sustentation consomme en permanence. Une **voilure fixe** est bien plus efficace en croisière, avec des autonomies d'un ordre de grandeur supérieures, mais exige une zone de décollage et ne peut pas stationner. Les architectures **hybrides** combinent les deux au prix d'une masse et d'une complexité accrues.

**La contrainte de la couche s'applique intégralement** : la boucle masse-énergie est ici la plus sévère de tout l'atlas, puisque toute masse ajoutée doit être sustentée en permanence.

**Où vous rencontrerez le terme.** Inspection d'infrastructures · cartographie et topographie · agriculture · cinéma · sécurité civile et secours · logistique · surveillance environnementale · applications de défense.

**Ce que ça permet.** Accéder à un point de vue aérien à un coût sans commune mesure avec celui d'un aéronef habité · inspecter sans échafaudage ni arrêt d'exploitation · couvrir rapidement une zone étendue.

**Ce qui bloque — et c'est le point principal.** Dans la majorité des applications civiles à valeur, **le verrou dominant est le cadre d'autorisation du vol hors vue directe de l'opérateur**. Tant qu'un opérateur doit garder la machine en vue, l'économie reste celle d'un travail humain déplacé ; l'automatisation ne devient intéressante qu'au-delà.

S'y ajoutent **l'assurabilité**, qui suit la maturité du cadre plus que celle de la technique ; **l'autonomie énergétique**, qui borne les missions ; **la détection et l'évitement** d'autres aéronefs, condition technique de l'autorisation ; et **l'intégration à l'espace aérien**, qui est un problème de coordination et non de plateforme.

**Ce que cela implique.** C'est un cas d'école du volume 1 : une technologie mûre, peu coûteuse, dont la diffusion est bornée par une condition institutionnelle. **La grandeur à surveiller n'est pas la performance des machines mais le nombre d'autorisations de vol hors vue délivrées** et les conditions qui les accompagnent.

**Sûreté et sécurité.** Un aéronef sans équipage est un objet volant dont la chute a des conséquences · la liaison de commande est une dépendance critique · la navigation repose souvent sur une référence satellitaire dont le chapitre 6 a établi la fragilité. Ces points sont traités au niveau du principe et de leurs conséquences systémiques.

**À ne pas confondre avec.** **Un aéronef autonome**, qui décide ; la plupart des drones exécutent un plan de vol et ne décident de rien. **Un modèle réduit**, dont le régime réglementaire et l'usage diffèrent.

**Termes voisins.** *UAV*, *UAS* — ce dernier désignant le système complet, plateforme, station sol et liaison, ce qui est plus juste.

> ⏱ **État au 23/08/2026** — 🏭 déployé. Filière mature en inspection et cartographie ; cadres d'autorisation du vol hors vue en construction progressive selon les juridictions, avec des rythmes très inégaux.
> 🔄 **À revoir si** une juridiction majeure ouvre le vol hors vue à un régime déclaratif plutôt qu'à autorisation individuelle.

**Renvois** — Couche : agir · Courant : drone economy (ch. 33) · Convergence : autonomie mobile (39).

---

## ◆ Systèmes terrestres sans équipage

**Niveau** — plateforme · **Couche** — agir

**En une phrase.** Des véhicules terrestres opérant sans conducteur à bord, hors du réseau routier ouvert.

**Où vous rencontrerez le terme.** Mines et carrières · agriculture · logistique de site · inspection · agriculture · applications de défense.

**Ce qui bloque.** **La mobilité en terrain non préparé** reste difficile et coûteuse en énergie. Et le domaine souffre d'une comparaison défavorable : là où l'environnement est structuré, un robot mobile d'entrepôt suffit ; là où il ne l'est pas, la difficulté croît fortement. **La zone où ces plateformes sont économiquement pertinentes est donc étroite** — sites industriels étendus, agriculture, environnements dangereux.

**Ce que cela implique.** Le déploiement le plus avancé se situe dans les mines à ciel ouvert : environnement clos, trajets répétitifs, conducteurs coûteux et exposés. C'est la configuration qui réunit toutes les conditions favorables.

**À ne pas confondre avec.** **Les véhicules autonomes routiers** (ch. 17), dont la contrainte principale est la cohabitation avec des humains non prévenus.

> ⏱ **État au 23/08/2026** — 🏭 déployé en site clos, 🔬 émergent ailleurs.
> 🔄 **À revoir si** une plateforme terrestre autonome atteint un coût d'exploitation compétitif en terrain agricole ouvert.

**Renvois** — Couche : agir.

---

## ◆◆ Systèmes maritimes et sous-marins

**Niveau** — plateforme · **Couche** — agir, relier

**En une phrase.** Des navires et engins submersibles opérant sans équipage, en surface ou en immersion.

**Pourquoi on en parle.** Parce que le milieu impose une contrainte que ne connaît aucune autre plateforme : **sous l'eau, les ondes électromagnétiques ne se propagent pratiquement pas**.

**Comment ça fonctionne.** En surface, un navire sans équipage relève d'une problématique proche de celle des autres plateformes : navigation, perception, liaison satellitaire, avec des temps de réaction longs et un environnement peu encombré — ce qui rend la tâche plus facile que sur route.

**En immersion, tout change.** Pas de positionnement satellitaire, pas de liaison radio, pas de retour vidéo à distance. La navigation repose sur l'inertiel recalé par des méthodes acoustiques ou par appariement de terrain, et la communication passe par l'acoustique, dont le chapitre 7 a rappelé qu'elle est lente et à très faible débit. **Un engin submersible est donc autonome par nécessité**, non par choix.

**Ce que ça permet.** Inspecter des ouvrages sous-marins sans plongeur ni navire support · cartographier les fonds · surveiller des installations · effectuer des transits longs à faible coût.

**Ce qui bloque.** **L'énergie**, avec des missions bornées par la batterie et une recharge difficile. **La récupération** : une plateforme perdue est perdue, ce qui impose une fiabilité élevée. **La communication**, qui interdit toute supervision continue et impose de faire confiance à la machine pendant toute la mission. Et **le cadre juridique** de la navigation sans équipage, encore en construction.

**Ce que cela implique.** C'est le domaine où **l'autonomie n'est pas une ambition mais une contrainte** — et c'est ce qui en fait un observatoire utile : les questions de mode dégradé, de décision hors supervision et de comportement en cas de perte de contact y sont traitées depuis longtemps.

**À ne pas confondre avec.** Les engins **filoguidés**, reliés à un navire par un câble qui fournit énergie et liaison — ils ne sont pas autonomes et couvrent la majorité des interventions actuelles.

> ⏱ **État au 23/08/2026** — 🏭 déployé pour l'inspection et l'hydrographie, 🔬 émergent pour les transits longs et la navigation de surface sans équipage.
> 🔄 **À revoir si** un cadre juridique international pour la navigation commerciale sans équipage entre en vigueur.

**Renvois** — Couche : agir · Voir aussi : acoustique sous-marine (ch. 7), navigation sans référence satellitaire (ch. 6).

---

## ◆◆◆ Essaims et coordination distribuée

**Niveau** — système et doctrine · **Couche** — agir, décider, relier

**En une phrase.** Faire opérer ensemble un grand nombre de plateformes dont le comportement collectif émerge de règles locales, sans coordination centrale.

**Pourquoi on en parle.** Parce que le terme est employé pour désigner tout regroupement nombreux — alors que **ce qui définit un essaim est l'absence de centre**, avec les propriétés et les difficultés que cela implique.

**Comment ça fonctionne.** Chaque unité observe son voisinage immédiat, applique des règles simples — maintenir une distance, suivre une direction moyenne, éviter une collision — et n'a de connaissance ni du plan d'ensemble, ni de l'état global. Le comportement collectif n'est programmé nulle part : il résulte des interactions locales.

**Ce que cela donne.** Une **robustesse remarquable** : la perte d'unités ne détruit pas le collectif, puisqu'aucune n'est indispensable. Une **scalabilité** : ajouter des unités ne complexifie pas la coordination, chacune ne dialoguant qu'avec ses voisines. Et une **absence de point unique de défaillance**.

**Ce que cela coûte, et c'est le point mal compris.** **La prévisibilité.** Un comportement émergent n'est pas spécifié : on peut le constater, difficilement le garantir. Vérifier qu'un collectif ne produira jamais un comportement indésirable est un problème ouvert, et c'est ce qui bloque l'emploi dans des contextes à conséquence.

S'y ajoute **la communication**, qui est le vrai verrou technique : une coordination locale suppose des échanges, donc de la bande passante, de l'énergie et une tolérance à la latence. Le cadrage biologique masque ce coût en suggérant que la coordination est gratuite — elle ne l'est pas.

**Ce que ça permet.** Couvrir une zone étendue avec des plateformes individuellement peu capables · maintenir une mission malgré des pertes · adapter la formation sans replanification centrale.

**Ce qui bloque.** La **vérification** du comportement collectif · la **communication** en environnement contraint · le **coût unitaire**, puisque l'approche suppose le nombre · et la **gouvernance**, un système sans centre étant difficile à interrompre proprement.

**Ce que cela implique.** L'essaim est un compromis explicite : **on échange de la prévisibilité contre de la robustesse**. Ce compromis convient à des missions tolérantes à l'incertitude du résultat — couverture, recherche, mesure distribuée — et convient mal là où le comportement doit être garanti.

**Traitement dual.** Les applications de défense de la coordination distribuée sont réelles et documentées. Ce volume les traite au niveau industriel, économique, doctrinal et de gouvernance — notamment la question de l'économie de l'attrition, abordée au chapitre 44 — et ne fournit aucun élément d'emploi.

**À ne pas confondre avec.** **Une flotte coordonnée depuis un centre**, qui est le cas le plus fréquent et n'est pas un essaim. **Les systèmes multi-agents** logiciels (ch. 12), dont l'architecture est généralement dirigée.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Démonstrations nombreuses, applications civiles limitées — spectacle, mesure distribuée — et développements soutenus en défense. La vérification du comportement collectif reste le verrou.
> 🔄 **À revoir si** une méthode de vérification permet de garantir des propriétés de sûreté sur un collectif à comportement émergent.

**Renvois** — Couche : agir, décider, relier · Courant : swarm intelligence (ch. 33) · Voir aussi : perception distribuée (ch. 7).

---

## ◆◆ Autonomie supervisée

**Niveau** — doctrine · **Couche** — décider

**En une phrase.** Une machine décide et agit ; un humain surveille et peut intervenir.

**Pourquoi on en parle.** Parce que **c'est le régime réel de la quasi-totalité des systèmes déployés**, et parce que son économie dépend d'un paramètre rarement publié.

**Comment ça fonctionne — trois configurations à distinguer.**

**Humain dans la boucle** : la machine propose, l'humain valide avant exécution. Sûr, mais le débit est borné par l'humain.

**Humain sur la boucle** : la machine agit, l'humain observe et peut interrompre. C'est le régime le plus courant, et le plus délicat.

**Humain en réserve** : la machine agit seule et sollicite l'humain uniquement en cas de blocage. C'est le régime qui permet à un opérateur de superviser plusieurs machines — et donc le seul qui produise un gain économique net.

**Ce qui bloque — et c'est un problème humain, pas technique.** **La vigilance.** Un opérateur qui surveille un système fiable pendant des heures n'est pas dans un état permettant de reprendre le contrôle en quelques secondes. Plus le système est fiable, moins l'humain est prêt — **la fiabilité dégrade la supervision qu'elle rend nécessaire**.

**Ce paradoxe n'est pas une intuition : il est établi dans la littérature des facteurs humains depuis les années 1980**, sous le nom d'*ironies de l'automatisation* — l'article fondateur de Lisanne Bainbridge, publié en 1983 dans *Automatica*, reste l'une des références les plus citées du domaine. Il décrit trois effets que quarante ans de travaux ont confirmés plutôt qu'infirmés : **la vigilance décroît** lors d'une surveillance prolongée d'un système qui ne défaille pas ; **les compétences s'atrophient** faute d'être exercées, précisément celles qu'exige la reprise ; et **la confiance excessive** conduit à suivre le système quand il se trompe et à ne pas voir qu'il a échoué — un mécanisme attentionnel que l'expérience et la formation ne suppriment pas.

**Ce que la littérature ne dit pas**, et qu'il faut se garder de lui faire dire : elle n'a pas produit de loi quantitative transposable. **Les durées au-delà desquelles la vigilance se dégrade dépendent de la tâche, du taux d'événements et de l'organisation** ; elles se mesurent sur un déploiement, elles ne se lisent pas dans un tableau. La conséquence pratique est en revanche stable : **on conçoit contre ce paradoxe** — par la rotation, la charge de travail maintenue, la conception des alertes — plutôt qu'on ne le résout par un supplément de fiabilité.

S'y ajoute **le délai de reprise** : entre l'alerte et l'action correcte, il faut comprendre la situation, ce qui prend du temps même pour un opérateur attentif.

**Ce que cela implique.** **Le ratio d'opérateurs par machine est la grandeur économique décisive** de tout déploiement autonome. Un ratio de un pour un ne réduit pas le coût du travail : il le déplace, éventuellement vers un lieu moins cher, ce qui est une décision différente de l'automatisation.

**À ne pas confondre avec.** **La téléopération** (ch. 15), où l'humain décide. Ici, la machine décide.

> ⏱ **État au 23/08/2026** — 🏭 déployé, régime dominant de tous les systèmes autonomes en exploitation.
> 🔄 **À revoir si** des exploitants publient couramment leur ratio de supervision, ce qui rendrait comparables les économies annoncées.

**Renvois** — Couche : décider · Convergence : autonomie mobile (39) · Voir aussi : automatisation, agentivité, autonomie (ch. 12).

---
