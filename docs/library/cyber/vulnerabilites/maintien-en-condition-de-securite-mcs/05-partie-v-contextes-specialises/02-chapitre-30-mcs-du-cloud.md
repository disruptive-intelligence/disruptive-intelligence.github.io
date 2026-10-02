---
title: Chapitre 30 — MCS du cloud
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE V — Contextes spécialisés
  - index.md
---

infrastructure, plateforme et services managés

## 30.1 La responsabilité partagée, décodée

Le §3.4 a posé le principe. Voici les zones grises, celles où les incidents se produisent.

| Zone grise | Question | Réponse fréquente |
|---|---|---|
| Image de machine fournie par le fournisseur | Qui la met à jour ? | **Vous**, dès l'instant où vous l'instanciez |
| Version mineure d'un service managé | Appliquée automatiquement ? | Souvent oui, dans une fenêtre que vous choisissez partiellement |
| Version majeure d'un service managé | Qui décide ? | Vous — **jusqu'à la date limite**, ensuite le fournisseur |
| Configuration de sécurité par défaut | Sécurisée ? | Non : les défauts privilégient la mise en service |
| Journalisation | Activée ? | Rarement par défaut, souvent facturée |
| Correctifs du système sous-jacent en plateforme | Qui ? | Le fournisseur, sans préavis systématique |

✅ **BONNE PRATIQUE (P0) — la matrice de responsabilité signée**
Pour chaque service que vous utilisez, une ligne : *qui maintient quoi, qui décide de la fenêtre, quel préavis, quelle preuve fournie*. C'est le livrable du §30.10, et sa vertu principale est de forcer la question là où personne ne se la pose — c'est-à-dire précisément dans les zones grises ci-dessus.

## 30.2 Images et instances

**Le mécanisme central** : une instance créée à partir d'une image porte tout le retard de cette image (§28.5). Dans le cloud, ce mécanisme est amplifié par la mise à l'échelle automatique — une montée en charge peut créer vingt instances à partir d'une image vieille de six mois.

| Objet | Traitement |
|---|---|
| Catalogue d'images | Images validées, versionnées, avec une cadence de reconstruction |
| Instances longue durée | Traitées comme des serveurs classiques, ou remplacées (§3.5) |
| Groupes à mise à l'échelle | **La correction passe par l'image**, jamais par l'instance |
| Instances éphémères | N'apparaissent pas dans un inventaire réseau : inventaire par l'interface du fournisseur |

**L'indicateur préventif central** dans ce contexte : **l'âge de l'image** en service. Une organisation qui maintient toutes ses images à moins de 30 jours réduit fortement le volume de constats individuels à traiter — sans supprimer le besoin d'analyse de vulnérabilités ni de mesure d'exposition, puisqu'une image récente peut embarquer un composant vulnérable.

## 30.3 Bases de données et services managés

| Événement | Ce que vous contrôlez |
|---|---|
| Correctif mineur | La fenêtre, parfois le report de quelques semaines |
| Version majeure disponible | Le moment de la migration, **jusqu'à une date limite** |
| Fin de support d'une version | Rien : la migration devient forcée |
| Changement de comportement par défaut | Rien, sauf à lire les annonces |

**La conséquence pour le MCS** : sur ces services, **vous ne pilotez pas la correction, vous pilotez l'anticipation**. Le travail consiste à connaître les échéances de fin de support des versions utilisées, et à planifier les migrations avant la date limite — faute de quoi elles seront subies, au moment choisi par le fournisseur.

✅ **BONNE PRATIQUE (P0)** — Intégrez les versions de services managés à votre référentiel d'obsolescence (§12.2), au même titre que les systèmes d'exploitation. C'est l'oubli le plus fréquent des programmes de MCS en environnement cloud.

## 30.4 Orchestrateurs managés et exécution sans serveur

| Objet | Contrainte | Anticipation nécessaire |
|---|---|---|
| Version du plan de contrôle | Support d'environ quatorze mois (§3.3), fenêtre imposée par le fournisseur | Planifier deux à trois montées par an |
| Images des nœuds | À votre charge | Cadence de remplacement |
| Interfaces dépréciées | Ruptures annoncées à l'avance | Inventaire des usages, migration progressive |
| Composants additionnels installés | Leur propre cycle | Souvent oubliés |
| Environnements d'exécution de fonctions | Support court, dépréciation forcée | Suivi par fonction, pas globalement |

⚠️ **PIÈGE — la version d'environnement d'exécution des fonctions**
Une organisation peut avoir déployé plusieurs centaines de fonctions au fil des années, chacune avec sa version d'environnement d'exécution. Quand le fournisseur déprécie une version, toutes les fonctions concernées doivent être migrées — et l'inventaire n'existe généralement pas. Constituez-le **avant** l'annonce de dépréciation, pas après.

## 30.5 Ce que le fournisseur corrige, et le prix

**Ce qu'il apporte** : les correctifs de l'infrastructure et, selon le service, du système et de l'environnement d'exécution, appliqués à une échelle et avec une rapidité qu'aucune organisation ne peut atteindre seule.

**Ce qu'il coûte** :

| Contrepartie | Manifestation |
|---|---|
| Perte du choix du moment | Les fenêtres sont imposées ou fortement contraintes |
| Changements sans préavis proportionné | Un comportement par défaut change à une date choisie par le fournisseur |
| Absence de retour arrière | Une fois la migration appliquée, elle n'est pas réversible |
| Preuve limitée | Vous ne pouvez pas produire de preuve technique sur la couche du fournisseur (§30.11) |

## 30.6 Identités et droits cloud

La dette d'autorisations est au cloud ce que la dette d'annuaire est au monde classique (§24.1), avec deux aggravations : les droits sont **plus fins et plus nombreux**, et ils sont **attribués par des équipes techniques** sans processus de revue.

| Objet | Risque |
|---|---|
| Rôles trop permissifs | Attribués « pour débloquer », jamais réduits |
| Clés d'accès de longue durée | Souvent dans du code, des scripts, des fichiers d'état (§23.5) |
| Identités de service | Pratiques, mais leurs droits sont rarement revus |
| Rôles hérités entre comptes ou abonnements | Chemins d'accès transverses invisibles |
| Accès de prestataires | Configurés une fois, jamais retirés (§13.5) |

**La mesure la plus rentable** : identifier les identités disposant de droits d'administration sur un abonnement ou un projet entier, et les réduire. Elles sont peu nombreuses, et ce sont elles qui transforment un incident en catastrophe.

## 30.7 Configuration et dérive de *tenant*

Le cloud a déplacé une part importante du risque de la vulnérabilité vers la **configuration** : stockage ouvert, base de données accessible publiquement, règle de filtrage trop large, journalisation désactivée, chiffrement non activé.

| Mécanisme | Rôle |
|---|---|
| **Contrôle de posture** | Détecte les configurations non conformes, en continu |
| **Garde-fous préventifs** | Empêchent la création d'une ressource non conforme — plus efficace que la détection |
| Description par code | Rend la configuration lisible et reproductible (§23.5) |
| Revue périodique | Traite ce que l'automatisme ne couvre pas |

✅ **BONNE PRATIQUE (P0)** — Privilégiez les **garde-fous préventifs** aux contrôles détectifs. Empêcher la création d'un stockage public coûte une politique ; détecter et corriger des stockages publics coûte un processus permanent. C'est le principe du §22.4 appliqué au cloud.

## 30.8 Écart entre le code et la réalité

Le §23.5 s'applique avec une acuité particulière : dans le cloud, créer une ressource à la main prend trente secondes, et la tentation est constante en situation d'urgence.

**Les trois mesures** : détection périodique des ressources non décrites par le code ; interdiction de la création manuelle en production, avec une procédure d'exception tracée ; et réconciliation systématique après tout incident ayant nécessité une action manuelle (règle de reversion du §23.7).

## 30.9 Multi-cloud et zones d'atterrissage

Une **zone d'atterrissage** est un socle standardisé — comptes, réseau, identités, journalisation, garde-fous — sur lequel les projets se déploient.

**Son intérêt pour le MCS** est direct : elle fait de la conformité un état par défaut plutôt qu'un contrôle *a posteriori*. Tout nouveau projet hérite des garde-fous, de la journalisation et des politiques d'identité.

📌 **LIMITES** — Le multi-cloud multiplie les référentiels, les mécanismes de correction, les calendriers de dépréciation et les compétences nécessaires. Chaque fournisseur supplémentaire ajoute un dispositif complet de MCS à maintenir, pas une simple extension.

## 30.10 ✅ Livrable — Matrice de responsabilité MCS par service

| Service utilisé | Modèle | Ce que le fournisseur maintient | Ce que nous maintenons | Fenêtre imposée | Préavis | Preuve disponible | Propriétaire |
|---|---|---|---|---|---|---|---|

**Comment l'utiliser** : la renseigner service par service, la faire valider par l'équipe qui exploite le service, et l'annexer aux dossiers de conformité (§8.8). Les lignes où la colonne « preuve disponible » est vide sont vos zones à déclarer non mesurées (§7.7).

## 30.11 🔴 FIL ROUGE — mars 2028 : l'échéance qu'on ne négocie pas

Le fournisseur cloud d'HELIOMED annonce la fin de support d'une version majeure de moteur de base de données utilisée par la plateforme HelioLink. Date limite : **quatre mois**. Passé ce délai, la migration sera appliquée automatiquement, dans une fenêtre choisie par le fournisseur.

**Ce que découvre l'équipe.** L'annonce a été publiée **onze mois plus tôt** dans les notes de service du fournisseur. Personne ne les suivait : la veille d'HELIOMED couvrait les éditeurs de logiciels et les constructeurs, pas les annonces de services cloud. C'est un trou identifié dans la matrice de couverture de décembre 2026 (§14.11), ligne « services en ligne : 11 % ».

**L'analyse d'impact.** La migration implique un changement de comportement sur le tri de certaines requêtes, ce qui affecte deux fonctionnalités d'HelioLink. Un test est nécessaire. Le développement correspondant représente trois semaines.

**Ce qui n'est pas négociable, et ce qui l'est.** La date limite ne se négocie pas. En revanche, le fournisseur accepte de fixer la fenêtre de migration à une date et une heure choisies par HELIOMED, dans la limite du délai. C'est le seul levier disponible, et il est réel.

**La séquence appliquée** : migration réalisée en environnement de recette dès la semaine suivante, correction des deux fonctionnalités, tests de non-régression, puis migration de production planifiée un samedi de juin — six semaines avant la date limite, pour conserver une marge en cas de problème.

**Les trois décisions structurelles.**

1. **La veille des services cloud** est intégrée à la matrice du §14.1, avec un responsable nommé et une revue mensuelle des annonces de service. C'était la ligne à 11 %.
2. **Les versions de services managés** entrent au référentiel d'obsolescence (§30.3), avec leurs dates de fin de support — comme n'importe quel système.
3. **La matrice de responsabilité** du §30.10 est constituée pour les onze services cloud utilisés. Elle révèle au passage deux autres échéances à moins de douze mois, jusque-là ignorées.

**Ce que Sonia Weber retient**, et qu'elle formule devant le comité : *« Nous avons passé deux ans à construire un dispositif pour décider quand nous corrigeons. Sur cette couche, la seule décision qui nous reste est celle de l'heure. »*

**Livrable de l'épisode.** La matrice de responsabilité MCS par service cloud, et l'intégration des échéances de services managés au plan d'obsolescence.

→ La suite en 🔴 §31.12, quand un connecteur autorisé en 2021 refera surface.

→ **Chapitre 31 — MCS des services en ligne, extensions et intégrations** : les services en ligne, où la configuration remplace le correctif.

## Synthèse mentale du chapitre 30

La responsabilité diminue avec le niveau de service mais ne disparaît jamais, et les incidents se produisent dans les zones grises — images fournies mais instanciées par vous, versions majeures que vous choisissez jusqu'à une date limite, configurations par défaut qui privilégient la mise en service. Dans le cloud, l'indicateur qui remplace des centaines de constats individuels est l'âge de l'image en service. Sur les services managés, vous ne pilotez pas la correction mais l'anticipation : leurs versions doivent entrer au référentiel d'obsolescence au même titre que les systèmes d'exploitation, ce qui est l'oubli le plus fréquent. Le risque s'est largement déplacé de la vulnérabilité vers la configuration, et les garde-fous préventifs coûtent une politique là où la détection coûte un processus permanent. Enfin, chaque fournisseur supplémentaire n'ajoute pas une extension mais un dispositif complet de MCS à maintenir.

**Trois questions de vérification**

1. Votre fournisseur annonce la fin de support d'une version de service managé dans quatre mois. Qu'est-ce qui est négociable, qu'est-ce qui ne l'est pas, et quel processus aurait dû vous alerter onze mois plus tôt ?
2. Un groupe d'instances à mise à l'échelle automatique porte une vulnérabilité. Pourquoi corriger les instances est-il une perte de temps, et quel indicateur unique aurait prévenu la situation ?
3. Pourquoi un garde-fou préventif est-il structurellement supérieur à un contrôle de posture détectif, et dans quel cas le second reste-t-il indispensable ?

---
