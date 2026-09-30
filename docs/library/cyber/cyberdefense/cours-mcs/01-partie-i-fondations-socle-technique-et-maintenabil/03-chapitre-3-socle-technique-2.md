---
title: Chapitre 3 — Socle technique 2
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE I — Fondations, socle technique et maintenabilité
  - index.md
---

virtualisation, conteneurs, cloud, IaC, OT et micrologiciels

Le chapitre 2 décrivait le maintien d'une machine. Celui-ci décrit le maintien de tout ce qui n'est plus une machine : couches d'abstraction, environnements éphémères, ressources dont vous ne possédez pas le matériel, et systèmes industriels qui obéissent à d'autres lois.

**Ces technologies n'ont rien en commun techniquement.** L'hyperviseur, le conteneur, l'orchestrateur, le cloud, l'automate et le micrologiciel appartiennent à des mondes séparés, avec des équipes, des outils et des cultures différentes. Ce qui les rassemble ici est ailleurs : **chacune modifie la façon dont le maintien est réalisé, et déplace la ligne qui sépare ce que vous devez faire de ce qu'un autre fait pour vous.**

Le fil conducteur est donc unique : **à chaque couche d'abstraction ajoutée correspond une frontière de responsabilité, et c'est toujours sur ces frontières que le MCS échoue.**

## 3.1 Hyperviseurs et appliances virtuelles

Un hyperviseur héberge des dizaines de machines virtuelles. Il faut y distinguer **quatre objets à maintenir**, souvent confondus :

| Objet | Ce que c'est | Interruption induite |
|---|---|---|
| L'hôte | Le système de l'hyperviseur lui-même | Migration à chaud des machines, puis redémarrage de l'hôte |
| Les invités | Les systèmes des machines virtuelles | Chacun selon sa nature (voir ch. 2) |
| Le plan de gestion | La console qui pilote l'ensemble | Interruption de l'administration, pas de la production |
| Le micrologiciel du matériel | Serveur physique sous l'hyperviseur | Redémarrage physique complet |

**Le bon côté.** La migration à chaud permet de déplacer les machines virtuelles d'un hôte à l'autre sans interruption, donc de mettre à jour les hôtes sans coupure de service. C'est l'un des rares cas où le MCS ne coûte pas de disponibilité — à condition d'avoir provisionné la capacité nécessaire pour fonctionner avec un hôte en moins.

**Le mauvais côté.** Le plan de gestion est un actif de **niveau 0** : quiconque le contrôle contrôle toutes les machines virtuelles, leurs disques et leurs sauvegardes. Il est régulièrement en retard de plusieurs versions, parce que le mettre à jour « n'apporte rien aux métiers » et interrompt l'outil que les administrateurs utilisent tous les jours. C'est une inversion complète des priorités : cet actif doit être parmi les premiers maintenus, pas parmi les derniers.

⚠️ **PIÈGE — l'appliance virtuelle**
Une *appliance* virtuelle est une machine virtuelle préconstruite livrée par un éditeur. Elle contient un système d'exploitation complet que **vous ne maintenez pas** : l'éditeur interdit généralement d'y appliquer les correctifs du système, et fournit ses propres mises à jour, souvent moins fréquentes. Vous héritez donc de son rythme, de ses composants tiers et de ses éventuels retards. Traitez chaque appliance comme un actif dont le MCS est délégué, avec les exigences contractuelles correspondantes (chapitre 13).

## 3.2 Conteneurs : on ne corrige pas, on reconstruit

Un conteneur est un processus isolé, exécuté à partir d'une **image** : une pile de couches en lecture seule contenant le système de fichiers minimal nécessaire à l'application.

Le changement de paradigme est total, et il faut le comprendre pour le reste du cours :

> **On ne met pas à jour un conteneur. On reconstruit son image, et on remplace le conteneur.**

Se connecter à un conteneur en fonctionnement pour y lancer une mise à jour est possible techniquement, et à proscrire : la correction disparaîtra au premier redémarrage, et l'écart entre l'image de référence et la réalité en production deviendra invisible.

**La chaîne de correction devient donc :**

```
Correctif publié pour un composant
   → mise à jour de l'image de base
   → reconstruction de l'image applicative
   → nouvelle version publiée dans le registre
   → redéploiement progressif des conteneurs
```


Cette chaîne est bien plus rapide et plus fiable qu'une correction classique — quand elle est automatisée. Elle est catastrophique quand elle ne l'est pas : une image construite il y a deux ans et jamais reconstruite accumule silencieusement toutes les vulnérabilités publiées depuis, et rien dans le système d'exploitation hôte ne le signalera.

⚠️ **PIÈGE — l'étiquette mouvante**
Une étiquette d'image comme `:latest` ne désigne pas un contenu figé : elle pointe vers ce que le registre considère comme la dernière version, à un instant donné. Deux déploiements « identiques » à une semaine d'écart peuvent donc contenir des composants différents. Inversement, une étiquette figée pour garantir la reproductibilité gèle aussi les vulnérabilités.
**La bonne pratique** consiste à référencer une empreinte immuable pour la reproductibilité, **et** à disposer d'un processus qui met à jour cette référence à cadence maîtrisée. La reproductibilité sans cadence de reconstruction est une machine à fabriquer de l'obsolescence.

✅ **BONNE PRATIQUE (P1)** — Définissez et suivez une **cadence maximale de reconstruction** des images (par exemple : toute image en production a été reconstruite il y a moins de 30 jours). Cet indicateur préventif remplace avantageusement des dizaines de constats individuels dans le pilotage courant — sans dispenser de l'analyse de vulnérabilités : une image reconstruite hier peut embarquer une dépendance vulnérable, et une image plus ancienne peut porter un correctif rétroporté.

## 3.3 Kubernetes : la cadence vous est imposée

Kubernetes orchestre des conteneurs sur un ensemble de machines. Trois particularités le rendent structurant pour le MCS.

**Un rythme de publication soutenu et un support court.** Le projet publie environ trois versions mineures par an. Chaque version mineure reçoit **environ douze mois de support standard, suivis d'environ deux mois de maintenance limitée** — soit près de quatorze mois avant la fin de vie de la branche. Concrètement : **rester sur une version pendant deux ans n'est pas une option**, c'est une sortie de support. Le MCS d'un cluster n'est pas une activité occasionnelle, c'est un processus permanent, à inscrire au calendrier au même titre qu'une campagne de correctifs.
Les offres managées appliquent leurs propres calendriers, parfois plus courts, parfois assortis d'un support étendu payant : ce point est traité au chapitre 30. 📎 [S-27]

**Un écart de version encadré.** Les composants d'un cluster ne peuvent pas diverger arbitrairement : les règles d'écart autorisé entre le serveur d'API et les nœuds imposent un ordre de mise à jour et un nombre maximal de versions de retard. On met à jour le plan de contrôle d'abord, les nœuds ensuite, jamais l'inverse, et jamais en sautant plusieurs versions d'un coup.

**Des ruptures d'interface programmées.** Chaque version retire des interfaces dépréciées. Une mise à jour peut donc casser des déploiements parfaitement fonctionnels, non par régression, mais parce que le format de description qu'ils utilisent n'existe plus. Ce risque est **prévisible et annoncé longtemps à l'avance** : c'est un travail d'anticipation, pas un aléa.

📌 **LIMITES — ce qu'un service managé ne vous enlève pas**
Un cluster managé chez un fournisseur cloud prend en charge le plan de contrôle. Restent intégralement à votre charge : le choix du moment de la montée de version (dans la fenêtre imposée), la mise à jour des images de nœuds, les composants additionnels installés dans le cluster, la compatibilité de vos propres déploiements, et la migration des interfaces dépréciées. Et si vous ne décidez pas dans la fenêtre, **le fournisseur décidera pour vous** : c'est le sujet du chapitre 30.

## 3.4 Cloud : la frontière de responsabilité, service par service

Le modèle dit de « responsabilité partagée » est souvent cité et rarement décodé. Voici sa traduction opérationnelle.

| Modèle | Le fournisseur maintient | Vous maintenez |
|---|---|---|
| **Infrastructure (IaaS)** | Matériel, hyperviseur, réseau physique | **Tout** le système invité, comme une machine classique |
| **Plateforme (PaaS)** | Système et environnement d'exécution | Le **choix de version** et sa migration avant fin de support, votre code, vos dépendances, la configuration |
| **Logiciel (SaaS)** | L'application entière | Configuration, identités, droits, extensions, intégrations tierces, données |
| **Fonctions (*serverless*)** | Exécution et système | Version de l'environnement d'exécution, dépendances applicatives, permissions attachées |

🖼 **SCHÉMA — Empilement des couches et frontières de responsabilité.** *Pile verticale : matériel · micrologiciel · hyperviseur · système · runtime · bibliothèque · application, avec une ligne de démarcation mobile selon le modèle d'exécution.*

### Le tableau à mémoriser

| Modèle d'exécution | Qui met à jour quoi |
|---|---|
| **Machine physique** | Vous : micrologiciel, système, applications |
| **Machine virtuelle** | Vous pour l'invité · l'équipe hyperviseur pour l'hôte et le plan de gestion |
| **Conteneur** | Vous reconstruisez l'image · l'équipe plateforme maintient les nœuds |
| **Infrastructure cloud (IaaS)** | Vous : tout l'invité · le fournisseur : matériel et hyperviseur |
| **Plateforme cloud (PaaS)** | Le fournisseur : système et exécution · **vous : le choix de version et sa migration avant échéance** |
| **Logiciel en ligne (SaaS)** | Le fournisseur : l'application · **vous : configuration, identités, extensions, intégrations** |
| **Fonctions (serverless)** | Le fournisseur : exécution · vous : version d'environnement, dépendances, permissions |
| **Appliance fournisseur** | Le fournisseur, à son rythme · vous : rien, sauf l'exposition |
| **Système industriel** | Le constructeur valide · vous appliquez pendant les arrêts |

⚠️ Les deux lignes qui produisent le plus d'angles morts sont **PaaS** — on croit que le fournisseur gère la version alors qu'il ne gère que l'exécution — et **appliance**, où l'on n'a aucune prise sauf sur l'exposition.

Trois enseignements en découlent.

**1. La responsabilité diminue, elle ne disparaît jamais.** Même en SaaS pur, la configuration du service, les comptes d'administration, les autorisations accordées à des applications tierces et les connecteurs restent à vous — et c'est précisément là que se produisent la majorité des incidents cloud. Chapitre 31.

**2. En PaaS, vous ne choisissez plus *si* vous migrez, seulement *quand*.** Le fournisseur annonce la fin de support d'une version d'environnement d'exécution ou de moteur de base de données, puis — selon le service et le contrat — impose une échéance, applique lui-même la migration, propose un support étendu payant, ou laisse le service fonctionner sans support. L'anticipation est le seul levier disponible dans les quatre cas.

**3. Les frontières se déplacent sans vous.** Un fournisseur peut modifier un comportement par défaut, retirer une option ou réinitialiser un paramètre de sécurité lors d'une mise à jour de son service. Votre configuration validée l'an dernier n'est pas garantie identique aujourd'hui. La veille sur les notes de version des services utilisés est une activité de MCS à part entière, traitée au chapitre 31.

## 3.5 Infrastructure décrite par le code et immutabilité

Deux idées, souvent confondues, qui changent profondément la façon de corriger.

**L'infrastructure décrite par le code** consiste à définir les ressources dans des fichiers versionnés plutôt que par des actions manuelles. Bénéfice pour le MCS : la configuration devient lisible, comparable et reproductible. Vous pouvez répondre à la question « quelle est la configuration de référence ? » — ce qui est impossible dans un environnement construit à la main.

**L'immutabilité** consiste à ne jamais modifier un serveur en fonctionnement : pour appliquer un correctif, on construit une nouvelle image, on déploie de nouvelles instances, et on retire les anciennes. C'est le modèle des conteneurs, transposé aux machines.

Ce que l'immutabilité apporte au MCS est considérable : la dérive de configuration locale disparaît largement, le retour arrière est simplifié — redéployer l'image précédente, à condition que données, schémas et dépendances restent compatibles —, et la correction devient un acte de déploiement standard plutôt qu'une opération d'exception.

⚠️ **PIÈGE — le code d'infrastructure est lui-même un actif à maintenir**
Les modules réutilisés, les connecteurs vers les fournisseurs cloud et les outils de description ont leurs propres versions, leurs propres vulnérabilités et leurs propres fins de support. Par ailleurs, l'écart entre ce que décrit le code et ce qui existe réellement — les ressources créées à la main dans l'urgence — est une forme de dérive particulièrement trompeuse, parce que le code donne l'illusion de la maîtrise. Chapitre 23.

## 3.6 Chaînes de construction et dépendances applicatives

Dans une application moderne, une part souvent importante — parfois majoritaire — du code exécuté n'a pas été écrite par l'équipe qui la maintient : bibliothèques externes, elles-mêmes dépendantes d'autres bibliothèques. La proportion exacte varie fortement selon le langage, l'écosystème et la maturité du projet ; ce qui est constant, c'est que cette part est rarement inventoriée.

**Deux notions à connaître dès maintenant.**

Le **fichier de verrouillage** enregistre la version exacte de chaque dépendance effectivement utilisée. Il garantit que la construction d'aujourd'hui produit le même résultat que celle d'il y a six mois. C'est indispensable à la reproductibilité — et c'est aussi un mécanisme de gel des vulnérabilités, exactement comme l'étiquette d'image figée du §3.2. Même remède : une cadence de mise à jour maîtrisée.

Les **dépendances transitives** sont celles que vous n'avez jamais choisies : votre application utilise A, qui utilise B, qui utilise C. La faille sera dans C. Vous ne pourrez la corriger qu'en attendant que B mette à jour C, sauf à forcer une résolution, ce qui comporte son propre risque.

**Les machines de construction sont des actifs à maintenir.** Les agents d'exécution des chaînes d'intégration disposent souvent d'accès étendus : registres d'images, environnements de déploiement, secrets. Ce sont des cibles de premier ordre, et ils échappent presque toujours à l'inventaire du parc. Le chapitre 28 leur est consacré.

## 3.7 Systèmes industriels (OT / ICS) : d'autres lois

Le monde industriel — automates, supervision, systèmes d'exécution de la production — obéit à des contraintes qui inversent plusieurs réflexes du monde bureautique.

**Le modèle de référence.** Le modèle de Purdue décrit une architecture en niveaux, du plus proche du terrain au plus proche de la bureautique :

```
Niveau 0   Capteurs, actionneurs — le procédé physique
Niveau 1   Automates, régulation
Niveau 2   Supervision (IHM), conduite locale
Niveau 3   Gestion de la production (MES), historisation
Niveau 3,5 Zone démilitarisée industrielle
Niveau 4/5 Systèmes d'information de gestion, bureautique
```


L'enjeu de MCS est concentré sur les niveaux 1 à 3, et sur l'étanchéité du niveau 3,5.

**Ce qui change fondamentalement.**

| Dimension | Informatique de gestion | Systèmes industriels |
|---|---|---|
| Contraintes dominantes | Confidentialité et intégrité | **Sûreté des personnes et disponibilité** — l'intégrité y est souvent directement liée à la sûreté |
| Durée de vie d'un équipement | 3 à 7 ans | **15 à 25 ans** |
| Fenêtre d'interruption | Nuit, week-end | **Arrêt de production annuel** |
| Validation d'un correctif | Interne | **Par le constructeur**, sous peine de perte de garantie |
| Conséquence d'une panne | Perte de service | **Risque physique** |

> **Le MCS ne change pas de principes en environnement industriel ; il change de contraintes.** Connaître, observer, décider, corriger, vérifier, prouver : la boucle est identique. Ce sont les fenêtres, les validations et les conséquences d'une erreur qui diffèrent.

**La conséquence pratique.** Appliquer un correctif non validé par le constructeur sur un automate peut faire tomber la garantie, invalider une certification, et — dans le pire des cas — perturber un procédé physique. La démarche du MCS industriel n'est donc pas « corriger plus vite », mais : **maîtriser l'exposition, préparer les correctifs longtemps à l'avance, et les appliquer pendant les arrêts planifiés.** Le chapitre 29 traite ce sujet en profondeur, y compris la chaîne complète de mise à jour hors ligne.

⚠️ **PIÈGE — le scan actif sur réseau industriel**
Un scan de vulnérabilités classique, banal en informatique de gestion, peut faire basculer un automate ancien en défaut : ces équipements ont des piles réseau minimalistes qui supportent mal les sollicitations inattendues. **Ne lancez pas de scan actif sur un réseau industriel sans validation explicite du constructeur ou de l'exploitant, sans test préalable et sans procédure d'arrêt.** La doctrine est : *passif par défaut, actif sous procédure* — un scan actif contrôlé reste possible, il ne s'improvise pas.

## 3.8 Micrologiciels, objets connectés et chaîne de démarrage

C'est la couche la plus basse, la moins visible, et celle où le retard est le plus important dans la plupart des organisations.

**Ce dont on parle.** Micrologiciel de carte mère (BIOS/UEFI), contrôleur de gestion à distance des serveurs, micrologiciels de disques et de cartes réseau, équipements connectés d'entreprise (impression, vidéosurveillance, contrôle d'accès, visioconférence).

**Pourquoi c'est critique.** Un composant qui s'exécute **avant** le système d'exploitation ne peut pas être surveillé par les protections qui s'exécutent **dans** le système d'exploitation. Une compromission à ce niveau survit à une réinstallation complète.

**Pourquoi c'est négligé.** La mise à jour est risquée (un échec peut rendre la machine inutilisable), rarement automatisable à grande échelle, souvent invisible des outils d'inventaire, et sans propriétaire clairement désigné entre l'équipe système, l'équipe poste de travail et les achats.

**Les mécanismes de protection à connaître.**

- **Le démarrage sécurisé** vérifie la signature de chaque composant chargé au démarrage, à partir de bases de certificats stockées dans le micrologiciel : une base d'autorisation et une base de révocation.
- **La signature des mises à jour** empêche l'installation d'un micrologiciel non authentique.
- **La protection contre le retour en arrière** empêche de réinstaller une version antérieure vulnérable — mécanisme indispensable, car sans lui un attaquant pourrait simplement « rétrograder » le composant pour retrouver une faille corrigée.

⏱ **ÉTAT DE L'ART — un cas d'école en cours (vérifié le 30/07/2026)**
Les certificats Microsoft de démarrage sécurisé émis en 2011 arrivent à expiration au terme de leurs quinze ans de validité : **KEK CA 2011** le 24 juin 2026, **UEFI CA 2011** le 27 juin 2026, **Windows Production PCA 2011** le 19 octobre 2026. Des certificats émis en 2023 les remplacent.

Ce cas mérite d'être étudié parce qu'il contient à lui seul cinq enseignements de MCS :

1. **La dégradation est silencieuse.** Une machine non mise à jour continue de démarrer normalement. Elle perd seulement la capacité de recevoir de futures révocations — donc toute protection contre les prochains logiciels malveillants de démarrage. Aucun tableau de bord de correctifs ne montrera ce manque.
2. **L'échéance était connue quinze ans à l'avance.** C'est le cas typique du §1.3 : la seule catégorie de dégradation entièrement prévisible est aussi celle qu'on découvre en retard.
3. **La correction dépend d'un tiers.** Sur une partie du parc, la mise à jour requiert une mise à jour de micrologiciel du constructeur. Sans elle, le processus reste en attente.
4. **Forcer la correction peut casser.** Contourner l'attente par une modification manuelle peut provoquer un échec de démarrage ou une demande de clé de récupération de chiffrement de disque. C'est l'illustration exacte du conflit MCO/MCS du §1.2.
5. **L'impact déborde l'éditeur concerné.** Les systèmes non-Windows dont le chargeur de démarrage est signé par la même autorité sont également concernés — une dépendance que peu d'organisations avaient cartographiée.

📎 [S-25] — documentation officielle et billet technique de l'éditeur, consultés le 30/07/2026.

✅ **BONNE PRATIQUE (P1)** — Créez une ligne d'inventaire dédiée aux micrologiciels, avec un propriétaire nommé, et traitez leur mise à jour par anneaux de déploiement comme n'importe quel correctif à risque (chapitre 18). Un parc dont aucun micrologiciel n'a jamais été mis à jour n'a pas « zéro vulnérabilité de micrologiciel » : il a **zéro visibilité**.

## 3.9 ⚠️ Les cinq endroits systématiquement oubliés

Synthèse des chapitres 2 et 3. Ces cinq zones échappent à presque tous les programmes de MCS naissants, et chacune a fait l'objet d'incidents majeurs documentés.

| # | Zone oubliée | Pourquoi elle échappe | Traité au |
|---|---|---|---|
| 1 | Environnements d'exécution et bibliothèques **embarqués dans les applications** | Hors gestionnaire de paquets, invisibles du système | Ch. 26 |
| 2 | **Plans de gestion** : hyperviseur, console de sauvegarde, outil de déploiement | « Ce n'est pas de la production » — alors que ce sont des actifs de niveau 0 | Ch. 28, 34 |
| 3 | **Micrologiciels** et chaîne de démarrage | Pas d'inventaire, pas de propriétaire, mise à jour risquée | Ch. 27 |
| 4 | **Modèles et images de référence** : images maîtres, modèles de machines virtuelles, instantanés | Une machine neuve naît vulnérable si son modèle ne l'est pas | Ch. 28 |
| 5 | **Configuration des services en ligne** : paramètres, extensions, connecteurs, autorisations déléguées | « C'est du SaaS, c'est maintenu » | Ch. 31 |

🔴 **FIL ROUGE — janvier 2026 : ce que la découverte réseau ne voyait pas**

L'inventaire de décembre (§2.9) aboutissait à un périmètre de référence de 221 actifs, dont 210 en service. En janvier, Claire Nadeau demande une seconde passe, orientée cette fois par les cinq zones ci-dessus plutôt que par le balayage réseau. Le résultat modifie l'échelle du problème.

- **Nantes (recherche et développement)** : quatre agents d'exécution de la chaîne d'intégration, créés par l'équipe de développement, hors du domaine, disposant d'un accès en écriture au registre d'images. Aucun n'apparaissait dans les 210 actifs en service : ils sont créés et détruits automatiquement, et n'existent souvent pas au moment où l'inventaire passe.
- **Saint-Étienne (usine)** : Thomas Berger, responsable maintenance, fournit un inventaire papier. Onze postes de supervision, dont deux sur des systèmes dont le support a pris fin en 2020, et trois automates dont le fournisseur ne publie plus de mise à jour depuis 2019. Aucun n'a jamais été scanné — et Thomas est formel : aucun ne le sera sans validation préalable.
- **Applications hébergées** : le service achats recense 38 abonnements à des services en ligne. Sept disposent de connecteurs avec accès en lecture à la messagerie de l'entreprise, autorisés entre 2019 et 2023, jamais revus depuis.
- **Modèles de machines virtuelles** : le modèle utilisé pour créer tout nouveau serveur Windows date de mars 2024. Chaque serveur créé depuis naît avec vingt-deux mois de correctifs de retard, rattrapés — quand ils le sont — au premier passage de la console de déploiement.
- **Micrologiciels** : aucune donnée. Le sujet n'a jamais eu de propriétaire.

**La décision qui compte.** Claire ne cherche pas à tout traiter. Elle formule une règle qui structurera tout le programme : *un actif sans propriétaire nommé n'est pas un actif maintenu, quelle que soit la qualité de l'outillage.* Chaque zone découverte reçoit un nom de propriétaire avant toute action technique — Malik pour les modèles et les micrologiciels, Yann Prigent pour les agents de construction, Thomas Berger pour l'usine, le service achats pour les abonnements en ligne.

**Livrable de l'épisode.** Un périmètre de référence en cinq domaines, avec un propriétaire par domaine, et une case explicite « micrologiciels : non couvert, propriétaire désigné, échéance de première mesure ». Déclarer un domaine non couvert **est** un livrable : c'est ce qui le rend finançable.

→ La suite en 🔴 §4.11, quand il faudra qualifier les premiers constats issus de ce périmètre.

## Synthèse mentale du chapitre 3

Chaque couche d'abstraction ajoute une frontière de responsabilité, et c'est sur ces frontières que le MCS échoue. Un hyperviseur impose de distinguer quatre objets à maintenir, dont un plan de gestion de niveau 0 souvent laissé en retard. Un conteneur ne se corrige pas : on reconstruit son image, ce qui rend la cadence de reconstruction plus informative que des dizaines de constats individuels. Un cluster d'orchestration impose son propre rythme, avec un support d'environ quatorze mois par version mineure et des ruptures d'interface annoncées à l'avance. Dans le cloud, la responsabilité diminue avec le niveau de service mais ne disparaît jamais, et les frontières se déplacent sans vous. L'infrastructure décrite par le code et l'immutabilité transforment la correction en déploiement standard — au prix de maintenir le code d'infrastructure lui-même. Le monde industriel inverse les priorités : disponibilité et sûreté des personnes d'abord, équipements sur quinze à vingt-cinq ans, correctifs validés par le constructeur, fenêtres annuelles. Enfin, la couche des micrologiciels est la plus basse, la plus critique et la moins inventoriée : sans propriétaire désigné, elle n'a pas zéro vulnérabilité, elle a zéro visibilité.

**Trois questions de vérification**

1. Votre organisation utilise une base de données managée chez un fournisseur cloud. Citez trois activités de MCS qui restent intégralement à votre charge.
2. Une image de conteneur en production a été construite il y a quatorze mois et n'a jamais été reconstruite. Le système d'exploitation des nœuds est parfaitement à jour. Où est le problème, et quel indicateur unique l'aurait révélé ?
3. Un responsable d'usine refuse tout scan de vulnérabilités sur son réseau industriel. A-t-il tort ? Que proposez-vous à la place, et quelle est la contrepartie de votre proposition ?

---
