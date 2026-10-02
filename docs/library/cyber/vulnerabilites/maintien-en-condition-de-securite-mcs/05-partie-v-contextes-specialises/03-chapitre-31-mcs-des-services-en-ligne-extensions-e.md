---
title: Chapitre 31 — MCS des services en ligne, extensions et intégrations
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE V — Contextes spécialisés
  - index.md
---

## 31.1 La perte de maîtrise assumée

Sur un service en ligne, vous ne choisissez ni la version, ni la date, ni le contenu de la mise à jour. Le fournisseur applique ce qu'il veut, quand il veut, à tous ses clients simultanément.

**Ce que cela change pour le MCS** : la gestion des correctifs du service lui-même sort de votre périmètre. Elle y reste pour tout ce qui l'accompagne — clients lourds, agents, connecteurs, extensions, composants auto-hébergés et interfaces que vous appelez. Ce qui la remplace est **plus difficile à outiller et plus facile à négliger** :

| Ce qui disparaît | Ce qui le remplace |
|---|---|
| Application de correctifs | Veille sur les changements du fournisseur |
| Gestion des versions | Anticipation des ruptures annoncées |
| Durcissement système | **Configuration du service** — l'objet central du chapitre |
| Gestion des accès locaux | Comptes d'administration, identités applicatives, autorisations déléguées |
| Scan de vulnérabilités | Revue de configuration et contrôle des intégrations |

**La conséquence pratique** : sur un parc de quarante services en ligne, le travail de MCS n'est pas quarante fois la même chose. C'est une **revue de configuration périodique** sur les services qui comptent, et une **surveillance des intégrations** sur tous.

## 31.2 La veille éditeur sur les services en ligne

C'est la ligne la plus faible de la plupart des matrices de couverture (§14.1), et l'épisode du §30.11 en montre le coût.

| Source | Contenu | Difficulté |
|---|---|---|
| Notes de version du service | Changements fonctionnels et de sécurité | Volume élevé, tri nécessaire |
| Annonces de dépréciation | Fonctions et interfaces retirées | Le signal le plus important, souvent le moins visible |
| Bulletins de sécurité du fournisseur | Vulnérabilités et incidents | Publication inégale selon les fournisseurs |
| Page d'état du service | Incidents en cours | Utile en exploitation, pas en MCS |
| Communications commerciales | Évolutions d'offre, fins de vie | À ne pas négliger : une fin d'offre est une échéance |

✅ **BONNE PRATIQUE (P1) — la veille proportionnée**
Ne cherchez pas à suivre quarante services. Classez-les : ceux qui traitent des données sensibles, ceux qui disposent d'un connecteur vers votre messagerie ou vos fichiers, et ceux dont l'indisponibilité arrête une activité. Sur ceux-là — souvent cinq à dix — la veille est nominative et mensuelle. Sur les autres, une revue annuelle suffit.

## 31.3 Les changements unilatéraux

| Type de changement | Effet possible |
|---|---|
| Fonctionnalité retirée | Un contournement de sécurité que vous aviez mis en place disparaît |
| **Paramètre de sécurité réinitialisé** | Votre configuration validée n'est plus celle que vous croyez |
| Comportement modifié | Une règle d'accès ne produit plus le même effet |
| Nouvelle fonctionnalité activée par défaut | Partage externe, intégration, assistance automatique : surface ajoutée sans décision de votre part |
| Modification des conditions d'usage | Localisation des données, sous-traitants, rétention |

⚠️ **PIÈGE — la nouvelle fonctionnalité activée par défaut**
C'est le mécanisme le plus fréquent d'élargissement involontaire de surface. Un fournisseur active une capacité de partage externe, d'intégration ou d'assistance sur l'ensemble des locataires, avec une option de désactivation que personne ne remarque. Votre configuration n'a pas changé ; votre exposition, si.
**La contre-mesure** : une revue de configuration périodique comparée à un état de référence documenté (§31.4), et non une revue « quand quelque chose change ».

## 31.4 La configuration du locataire comme objet de MCS

C'est le cœur opérationnel du chapitre. Sur un service en ligne, votre configuration **est** votre posture de sécurité.

**Les huit familles de paramètres à documenter et contrôler :**

| Famille | Exemples |
|---|---|
| Authentification | Facteurs exigés, exceptions, durée des sessions |
| Autorisations | Rôles d'administration, délégations, accès invités |
| Partage externe | Qui peut partager quoi, avec qui, avec quelle expiration |
| Intégrations | Applications tierces autorisées, portées accordées |
| Rétention et suppression | Durées, corbeilles, restauration |
| Journalisation | Événements collectés, durée, export |
| Chiffrement et clés | Gestion des clés, chiffrement au repos et en transit |
| Restrictions d'accès | Origines autorisées, conformité des appareils (§28.8) |

**La méthode** : établir un **état de référence documenté** pour chacune de ces familles, puis le comparer périodiquement à l'état réel. C'est exactement la *baseline* du chapitre 22, appliquée à un service dont vous ne maîtrisez pas le socle.

## 31.5 Extensions, places de marché et intégrations tierces

La surface que vous ajoutez vous-même, et la moins surveillée.

| Objet | Risque |
|---|---|
| Extension installée depuis une place de marché | Code tiers s'exécutant dans votre environnement, avec les droits accordés |
| Connecteur entre deux services | Fait transiter vos données par un troisième acteur |
| Application tierce autorisée par un utilisateur | Accès permanent, sans mot de passe, souvent surdimensionné |
| Automatisation créée par un utilisateur | Peut exfiltrer, transformer, republier des données en dehors de tout contrôle |

⚠️ **PIÈGE — l'autorisation accordée par un utilisateur**
Dans la plupart des environnements, un utilisateur ordinaire peut autoriser une application tierce à accéder à sa messagerie et à ses fichiers, en un clic, sans validation. L'accès est **permanent**, survit au changement de mot de passe, et n'apparaît dans aucun inventaire d'application.
**Les deux mesures** : restreindre le consentement utilisateur en imposant une validation administrative, et faire l'inventaire des autorisations déjà accordées (§24.4).

## 31.6 Autorisations déléguées et jetons

Le mécanisme mérite d'être compris, parce qu'il est contre-intuitif pour qui vient du monde des mots de passe.

Une autorisation déléguée accorde à une application un accès à des ressources **au nom d'un utilisateur ou d'une organisation**, matérialisé par un jeton. Trois propriétés en découlent :

1. **La rotation du mot de passe ne révoque rien.** Le jeton reste valide.
2. **La portée est souvent excessive.** Une application qui n'a besoin que de lire un agenda demande fréquemment un accès complet à la messagerie.
3. **La durée est longue**, et le renouvellement automatique.

**La révocation** est le seul moyen de mettre fin à un accès. Elle doit figurer dans le processus de départ d'un collaborateur et dans le décommissionnement d'un service (chapitre 35).

## 31.7 Comptes d'administration et accès invités

| Objet | Vérification |
|---|---|
| Comptes d'administration du service | Combien, nominatifs, avec authentification renforcée, revus quand ? |
| Comptes de secours | Existent-ils, sont-ils testés, sont-ils surveillés (§24.2) ? |
| Comptes de prestataires | À la demande ou permanents (§13.5) ? |
| Accès invités | Combien, depuis quand, encore justifiés ? |
| Comptes d'application | Rattachés à un propriétaire, avec des droits proportionnés ? |

**Les accès invités sont l'angle mort le plus courant** : accordés pour un projet, ils survivent des années, et donnent accès à des espaces de travail entiers.

## 31.8 Journalisation

Trois questions à poser à chaque service en ligne, et à documenter dans la matrice du §30.10 :

1. **Quels événements** sont journalisés — connexions, accès aux données, modifications de configuration, actions d'administration ?
2. **Pendant combien de temps**, et à quel niveau de licence ? La rétention par défaut est souvent de quelques mois, parfois de quelques jours.
3. **Peut-on les exporter** vers votre propre système de collecte ?

⚠️ La question de la rétention est celle qui décide, le jour d'un incident, si vous pourrez conclure ou non (§21.3). Une rétention de 90 jours signifie que toute question portant sur une période antérieure restera sans réponse — comme dans le fil rouge du §25.22.

## 31.9 La preuve fournie par le fournisseur

Les rapports d'audit tiers et attestations fournis par les prestataires en ligne ont une valeur réelle, et des limites précises. Ils **ne suffisent pas à eux seuls** à établir la correction de votre configuration :

| Ce qu'ils établissent | Ce qu'ils n'établissent pas |
|---|---|
| Le fournisseur dispose d'un dispositif de sécurité audité | Que **votre** configuration est correcte |
| Le périmètre audité est décrit | Que ce périmètre couvre le service que vous utilisez |
| Les contrôles ont été testés à une date | L'état actuel |

**Ce qu'il faut lire dans un tel rapport** : le périmètre exact, la période couverte, les exceptions relevées, et la liste des contrôles laissés à la charge du client — cette dernière section est celle qui vous concerne directement, et c'est celle que personne ne lit.

## 31.10 Fin de vie d'une offre et réversibilité

Un fournisseur peut arrêter un service, être racheté, ou modifier son modèle. Trois questions à traiter **avant** la souscription, jamais après :

1. **Comment récupérer nos données ?** Format, exhaustivité, délai, coût.
2. **Quel préavis** en cas d'arrêt du service ?
3. **Que se passe-t-il pour les données à la fin du contrat ?** Suppression, délai, preuve.

## 31.11 ⚠️ « C'est du SaaS, c'est maintenu »

Récapitulatif de ce qui reste intégralement à votre charge :

| Domaine | Ce qui reste à vous |
|---|---|
| Configuration | Intégralement |
| Identités et droits | Intégralement |
| Extensions et intégrations | Intégralement |
| Autorisations déléguées | Intégralement |
| Données | Classification, rétention, partage |
| Journalisation | Activation, export, exploitation |
| Veille sur les changements | Intégralement |
| Décision d'usage | Quel service, pour quelles données |

## 31.12 🔴 FIL ROUGE — avril 2028 : le connecteur de 2021

La revue des autorisations déléguées, engagée par Claire Nadeau sur l'environnement collaboratif d'HELIOMED, produit une liste de 47 applications tierces disposant d'un accès.

**La répartition.**

| Catégorie | Nombre |
|---|---|
| Applications validées et connues de la DSI | 9 |
| Applications métier autorisées par un responsable, non déclarées | 14 |
| Applications autorisées par un utilisateur unique | 21 |
| **Applications dont plus personne ne connaît l'usage** | **3** |

**Le cas central.** Un outil de signature électronique, autorisé en mars 2021 par un utilisateur du service commercial pour un besoin ponctuel. L'application dispose d'un accès **en lecture à l'ensemble des messageries de l'organisation** — une portée accordée au moment du consentement, jamais réduite. L'utilisateur qui l'a autorisée a quitté l'entreprise en 2023 ; l'autorisation, elle, est restée active.

Trois faits aggravent le constat : l'éditeur de l'outil a été racheté en 2024 par une société dont HELIOMED ignore tout ; les journaux ne permettent pas de savoir si l'accès a été utilisé, et sur quelle période ; et l'application n'apparaissait dans aucun inventaire — ni celui du chapitre 10, ni celui des abonnements payés, puisque la version utilisée était gratuite.

**Les décisions.**

*Immédiat.* Révocation des 3 autorisations sans usage identifié, dont celle-ci. Aucun impact : personne ne signale de dysfonctionnement.

*Sous quinze jours.* Restriction du consentement utilisateur : toute nouvelle autorisation d'application tierce passe désormais par une validation administrative. Les 21 autorisations utilisateur existantes sont examinées une par une ; 12 sont révoquées, 6 conservées avec portée réduite, 3 régularisées.

*Structurel.* Les autorisations déléguées entrent au périmètre de référence comme **actifs de service**, avec propriétaire, date d'octroi et date de revue — au même titre que les machines (§10.4). Revue semestrielle.

**La question sans réponse.** Léa Cassin, déléguée à la protection des données, pose la même question qu'en juillet 2027 et en octobre 2027 : cet accès a-t-il été utilisé, et pour quoi ? Les journaux d'autorisation applicative ne sont conservés que 90 jours. **Sur sept ans, la question reste sans réponse.**

**Ce que Claire écrit dans sa note.** *C'est la troisième fois en un an que nous découvrons une exposition ancienne dont nous ne pouvons pas mesurer les conséquences. Le point commun n'est pas technique : à chaque fois, quelqu'un a accordé un accès sans date de fin.*

**Livrable de l'épisode.** L'inventaire des autorisations déléguées, la restriction du consentement utilisateur, et l'ajout des actifs de service au périmètre de référence.

→ La suite en 🔴 §32.7, avec le banc de test qu'on ne peut ni migrer ni remplacer.

→ **Chapitre 32 — Systèmes contraints, legacy et sanctuarisation** : les systèmes qu'on ne peut ni corriger ni migrer.

## Synthèse mentale du chapitre 31

Sur un service en ligne, la gestion des correctifs disparaît de votre périmètre et ce qui la remplace est plus difficile à outiller : veille sur les changements, configuration du locataire, contrôle des intégrations. Le mécanisme le plus fréquent d'élargissement involontaire de surface est la fonctionnalité activée par défaut chez tous les clients — votre configuration n'a pas changé, votre exposition si, d'où la nécessité d'un état de référence comparé périodiquement. Une autorisation déléguée accordée par un simple utilisateur crée un accès permanent que la rotation du mot de passe ne révoque pas, souvent surdimensionné, et invisible de tout inventaire d'application. Les rapports d'audit du fournisseur n'établissent jamais que votre configuration est correcte, et leur section la plus utile — les contrôles laissés à la charge du client — est celle que personne ne lit. Enfin, la rétention des journaux décide, le jour d'un incident, si vous pourrez conclure.

**Trois questions de vérification**

1. Votre configuration d'un service collaboratif n'a pas été modifiée depuis six mois. Pourquoi votre exposition a-t-elle pu changer, et comment le détectez-vous ?
2. Un collaborateur quitte l'entreprise. Son compte est désactivé et son mot de passe changé. Qu'est-ce qui reste potentiellement actif, et comment y met-on fin ?
3. Un fournisseur vous transmet son rapport d'audit tiers. Quelle section lisez-vous en priorité, et pourquoi celle-là ?

---
