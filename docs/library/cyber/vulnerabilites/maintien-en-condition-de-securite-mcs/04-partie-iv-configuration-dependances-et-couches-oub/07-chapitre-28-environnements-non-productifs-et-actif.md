---
title: Chapitre 28 — Environnements non productifs et actifs d'administration
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

## 28.1 Pourquoi la non-production doit être maintenue

L'argument « ce n'est que de la préproduction » repose sur une hypothèse implicite fausse : que ces environnements ne contiennent rien d'intéressant et ne mènent nulle part.

**Les quatre raisons pour lesquelles ils comptent autant que la production :**

| Raison | Mécanisme |
|---|---|
| **Données de production copiées** | La recette est alimentée par une copie de la base réelle, sans anonymisation dans la majorité des cas |
| **Pivot** | Ces environnements sont souvent joignables depuis et vers la production |
| **Secrets persistants** | Les mêmes comptes de service, les mêmes clés, parfois les mêmes mots de passe |
| **Durcissement moindre** | Configuration relâchée « pour faciliter les tests », journalisation absente |

**La question qui tranche**, à poser à toute équipe défendant l'exclusion d'un environnement : *contient-il des données réelles, et depuis quelles machines est-il joignable ?* Dans une majorité de cas, la réponse fait entrer l'environnement dans le périmètre de classe C2 au minimum.

## 28.2 Cartographier l'oublié

| Environnement | Ce qu'il contient souvent | Pourquoi il échappe |
|---|---|---|
| Préproduction / recette | Copie de production | Considéré comme non critique |
| Développement | Données partielles, secrets | Géré par les équipes de développement |
| Laboratoire technique | Configurations expérimentales | Créé et oublié |
| Environnement de formation | Données factices ou réelles | Utilisé quelques jours par an |
| Démonstrateur commercial | **Données réalistes, exposé** | Hébergé hors DSI (§11.12) |
| Environnement de secours | Copie complète de la production | Non maintenu car « inactif » |

**L'environnement de secours mérite une attention particulière** : maintenu à l'identique de la production pour pouvoir la remplacer, il est souvent oublié des campagnes de correctifs parce qu'il n'est pas en service. Le jour où l'on bascule dessus, on bascule sur un système en retard de plusieurs mois — au moment précis où l'on est le plus vulnérable.

## 28.3 Postes de développement et chaînes d'intégration

| Actif | Risque spécifique |
|---|---|
| **Poste de développeur** | Droits locaux étendus, outils nombreux, code source, secrets, accès aux dépôts |
| **Agent d'exécution de la chaîne** | Accès aux registres, aux environnements de déploiement, aux secrets de construction |
| **Serveur de gestion de sources** | Contient tout votre code et son historique, y compris les secrets qui y ont transité |
| **Registre d'artefacts** | Une image compromise se propage à toute la production |

⚠️ **PIÈGE — l'agent d'exécution éphémère**
Les agents créés à la demande et détruits après usage n'apparaissent dans aucun inventaire réseau (§10.8). Ils sont pourtant souvent les actifs les plus privilégiés de l'organisation : ils déploient en production. L'inventaire doit se faire **depuis l'orchestrateur**, pas depuis le réseau, et leur configuration de référence doit être traitée avec le niveau d'exigence d'un actif de niveau 0.

## 28.4 Les actifs d'administration

Ce sont les premiers à maintenir, et ils sont souvent parmi les derniers traités.

| Actif | Pourquoi il est critique |
|---|---|
| **Poste d'administration** | Porte les sessions privilégiées ; sa compromission donne accès à tout ce qu'il administre |
| **Rebond / passerelle d'administration** | Point de passage obligé, donc cible concentrée |
| **Serveur de déploiement** | Capable d'exécuter du code sur l'ensemble du parc |
| **Console de gestion de virtualisation** | Contrôle de toutes les machines virtuelles (§3.1) |
| **Console de sauvegarde** | Accès à toutes les données, y compris historiques |
| **Coffre-fort de secrets** | Concentration de tous les accès |
| **Outil de scan** | Identifiants privilégiés et cartographie des faiblesses (§15.4) |

✅ **BONNE PRATIQUE (P0) — le poste d'administration dédié**
La mesure au meilleur rapport effort/risque de tout ce chapitre : les tâches d'administration se réalisent depuis un poste **dédié**, qui ne sert ni à la messagerie, ni à la navigation, ni à la bureautique. La raison est mécanique : un poste qui ouvre des pièces jointes et une session d'administration du domaine ne doivent pas être la même machine. Cette mesure ne coûte que de la rigueur, et elle casse le chemin d'attaque le plus fréquent (§11.4).

## 28.5 Modèles et images de référence

**Le mécanisme** : une machine créée à partir d'un modèle ancien naît avec tout le retard du modèle. Elle sera peut-être rattrapée par la campagne suivante — ou non, si elle est éphémère.

| Objet | Question à se poser |
|---|---|
| Modèle de machine virtuelle | De quand date-t-il ? Qui le met à jour, à quelle fréquence ? |
| Image de référence de poste | Idem |
| Image de conteneur de base | Cadence de reconstruction (§3.2) |
| Modèle d'infrastructure décrite par code | Versions des modules et connecteurs (§23.5) |
| Procédure d'installation manuelle | Encore plus problématique : elle vieillit sans que personne ne s'en aperçoive |

✅ **BONNE PRATIQUE (P0)** — Fixez une **cadence maximale de reconstruction des modèles**, suivez leur âge comme indicateur, et intégrez le contrôle de conformité à leur production (§22.4). C'est le remède à la récurrence du §17.9, et il traite la cause au lieu du symptôme.

## 28.6 Instantanés et supports de restauration

Un instantané pris avant une intervention et conservé six mois est une machine vulnérable en attente d'être réactivée.

| Objet | Risque | Traitement |
|---|---|---|
| Instantané de machine virtuelle | Restauration = retour à un état non corrigé | Durée de vie limitée, purge automatique |
| Sauvegarde restaurée | Réintroduit l'état d'origine | Contrôle de conformité systématique après restauration |
| Machine clonée pour test | Duplique les vulnérabilités et les secrets | Inventaire, durée de vie, suppression |
| Support d'installation | Contient une version ancienne | Régénération périodique |

**La règle** : toute restauration ou tout clonage déclenche un **contrôle de conformité** avant remise en service. C'est l'une des cinq causes de récurrence du §17.9, et c'est la plus facile à traiter.

## 28.7 Actifs intermittents

Postes nomades rarement connectés, matériel de secours stocké, équipements saisonniers, machines de laboratoire éteintes la plupart du temps, pièces de rechange préparées.

**Le problème commun** : ils ne sont pas là au moment des campagnes, et ils reviennent en service avec un retard proportionnel à leur absence.

**Les trois traitements** :

1. **Agent plutôt que scan réseau** : c'est la seule façon de les atteindre quand ils sont connectés, où qu'ils soient.
2. **Contrôle à la reconnexion** : une machine absente depuis plus de N jours passe par une phase de mise à jour avant d'accéder aux ressources.
3. **Mise à jour avant stockage** pour le matériel de secours — et acceptation qu'il vieillira quand même, d'où l'intérêt des pièces prépatchées du chapitre 29.

## 28.8 L'accès conditionnel fondé sur le niveau de mise à jour

**Le principe** : subordonner l'accès aux ressources à l'état de conformité de la machine. Une machine en retard de correctifs voit son accès restreint jusqu'à régularisation.

| Ce que cela apporte | Ce que cela ne règle pas |
|---|---|
| Traite les actifs intermittents sans campagne dédiée | Ne fonctionne que sur les machines enrôlées |
| Rend la conformité visible pour l'utilisateur | Ne dit rien des machines qui n'accèdent à rien |
| Déplace l'effort de la relance vers le mécanisme | Peut être contourné par des chemins d'accès non couverts |

⚠️ **PIÈGE — le blocage sans échappatoire**
Un mécanisme qui bloque brutalement provoque deux réactions : des tickets massifs au support, et la recherche de contournements par les utilisateurs. La mise en œuvre progressive — avertissement, puis restriction partielle, puis blocage — avec une procédure d'exception traçable, est la seule qui tienne dans la durée.

## 28.9 ⚠️ « Ce n'est que de la préprod » : reconstitution du chemin réel

```
Serveur de préproduction, non durci, non surveillé, hors périmètre de scan
   → contient une copie de la base de production de janvier
   → le compte de service applicatif y est le MÊME qu'en production
   → ce compte dispose de droits de lecture sur le serveur de fichiers de production
   → le serveur de fichiers contient les sauvegardes de configuration des équipements réseau
   → ces configurations contiennent les secrets d'administration
```


Cinq étapes, aucune vulnérabilité logicielle exploitée après la première. Chaque étape résulte d'une décision de commodité parfaitement rationnelle prise isolément — c'est la combinaison toxique du §11.5.

**Les trois ruptures les moins coûteuses** dans cette chaîne : des comptes de service **distincts** entre production et non-production ; l'anonymisation des données copiées en recette ; l'absence de joignabilité directe entre les deux environnements.

## 28.10 🔴 FIL ROUGE — janvier 2028 : l'agent d'exécution de Nantes

Les quatre agents d'exécution de la chaîne d'intégration de Nantes, identifiés en janvier 2026 (§3.9), n'avaient jamais été traités autrement que par la désignation d'un propriétaire — Yann Prigent. Deux ans plus tard, la revue des actifs d'administration les remet sur la table.

**Ce que l'analyse établit.**

| Constat | Détail |
|---|---|
| Configuration | Agents créés à la demande depuis une image construite en 2024 |
| Droits | Un jeton d'accès permanent avec droits d'écriture sur le registre d'images **et** droits de déploiement sur le cluster de production |
| Réseau | Joignables depuis le réseau de développement, non segmentés |
| Secrets | Trois secrets de production accessibles pendant la construction |
| Journalisation | Aucune : les agents sont détruits après usage, leurs journaux avec |
| Inventaire | Absents du périmètre de référence — créés et détruits automatiquement (§10.8) |

**Le chemin d'attaque reconstitué**, en quatre étapes : poste de développeur compromis → accès au dépôt de code → modification d'un fichier de définition de construction → l'agent exécute le code modifié avec ses droits de déploiement en production.

Aucune vulnérabilité logicielle n'intervient après la première étape. C'est exactement le schéma du §25.18 et du §28.9.

**Les décisions, en trois vagues.**

*Immédiat.* Le jeton permanent est remplacé par une identité à durée de vie courte, obtenue à l'exécution et limitée au strict nécessaire. Les droits de déploiement en production sont retirés des agents de construction : le déploiement devient une étape distincte, avec une approbation humaine pour la production.

*Sous un mois.* Segmentation du réseau des agents. Journalisation exportée avant destruction de l'agent. Reconstruction de l'image des agents, et cadence de reconstruction fixée à 30 jours (§28.5).

*Structurel.* Les agents d'exécution entrent au périmètre de référence, inventoriés **depuis l'orchestrateur** et non depuis le réseau. Ils sont classés C1, au titre d'actifs d'administration.

**La discussion la plus difficile.** L'équipe de développement conteste initialement l'approbation humaine avant déploiement en production, qui ralentit la livraison. L'arbitrage retenu, en comité, est un pré-arbitrage au sens du §9.4 : approbation requise pour la production uniquement, automatique pour tous les autres environnements, et déléguée à un rôle et non à une personne pour ne pas créer de goulot. La livraison perd quelques minutes ; la chaîne cesse d'être un chemin direct vers la production.

**Ce que Claire Nadeau note au comité.** *Nous avons mis deux ans à traiter quatre machines qui n'existent que quelques minutes à la fois, et qui disposaient de plus de droits que n'importe quel administrateur de l'entreprise.*

→ **Fin de la Partie IV.** La suite en 🔴 §29.11, avec l'arbitrage sur la ligne 2 de Saint-Étienne.

→ **Chapitre 29 — MCS en environnement industriel (OT / ICS)** : l'industriel, où toutes les règles précédentes s'inversent.

## Synthèse mentale du chapitre 28

« Ce n'est que de la préproduction » repose sur une hypothèse fausse : ces environnements contiennent des copies de données réelles, partagent les mêmes comptes de service, sont joignables depuis et vers la production, et sont moins durcis. L'environnement de secours est le cas le plus perfide : maintenu à l'identique pour remplacer la production, il est exclu des campagnes parce qu'il n'est pas en service — et l'on bascule dessus au moment où l'on est le plus vulnérable. Les agents d'exécution des chaînes de construction sont souvent les actifs les plus privilégiés de l'organisation et n'apparaissent dans aucun inventaire réseau : ils s'inventorient depuis l'orchestrateur. Le poste d'administration dédié est la mesure au meilleur rapport effort/risque du chapitre : un poste qui ouvre des pièces jointes et une session d'administration du domaine ne doivent pas être la même machine. Enfin, toute restauration ou clonage doit déclencher un contrôle de conformité — c'est la cause de récurrence la plus facile à traiter.

**Trois questions de vérification**

1. Une équipe demande d'exclure la préproduction du périmètre de scan. Quelles deux questions posez-vous, et quelle réponse ferait basculer l'environnement en classe C2 ?
2. Reconstituez en cinq étapes un chemin d'attaque partant d'un serveur de préproduction et aboutissant aux secrets d'administration réseau. Quelles sont les trois ruptures les moins coûteuses ?
3. Vos agents de construction sont créés à la demande et détruits après usage. Pourquoi n'apparaissent-ils dans aucun inventaire, et où faut-il aller les chercher ?

---

---

> ### 🎓 À ce stade de la Partie IV, vous savez…
>
> - **dériver** un référentiel de durcissement en motivant chaque écart, et mesurer une conformité de configuration sans produire un chiffre faux ;
> - **traiter** la dérive comme une propriété des systèmes vivants, par détection et convergence plutôt que par réprimande ;
> - **réduire** la dette d'annuaire, faire une rotation de secret qui soit réellement effective, et inventorier ce qui expire ;
> - **traiter** les vulnérabilités du code que vous avez écrit vous-même — celles qu'aucun outil de composition ne verra ;
> - **inventorier** les composants intermédiaires par application, et négocier une montée de version avec un éditeur récalcitrant ;
> - **atteindre** les couches que les outils ne remontent pas : micrologiciels, contrôleurs de gestion, périphériques ;
> - **traiter** les environnements que personne ne regarde : non-production, agents de construction, actifs d'administration.
>
> **Ce que vous ne savez pas encore** : comment adapter tout cela quand les règles changent. C'est l'objet de la Partie V.
