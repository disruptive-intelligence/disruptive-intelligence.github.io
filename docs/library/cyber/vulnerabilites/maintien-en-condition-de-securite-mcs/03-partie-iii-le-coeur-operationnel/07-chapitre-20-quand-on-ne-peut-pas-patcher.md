---
title: Chapitre 20 — Quand on ne peut pas patcher
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

les mesures compensatoires

## 20.1 Taxonomie des impossibilités

« On ne peut pas patcher » recouvre cinq situations très différentes, qui n'appellent ni les mêmes réponses ni les mêmes interlocuteurs. Le premier travail consiste à identifier laquelle vous avez en face de vous.

| Type | Description | Qui peut la lever | Horizon |
|---|---|---|---|
| **Technique** | Le correctif n'existe pas, ou casse une dépendance | L'éditeur | Incertain |
| **Contractuelle** | La garantie ou la certification interdit la modification | Le constructeur, le contrat | Négociable |
| **Métier** | L'interruption n'est pas acceptée | Le propriétaire métier | Négociable |
| **Budgétaire** | La correction suppose une migration non financée | La direction | Cycle budgétaire |
| **Temporelle** | Fenêtre trop éloignée | La planification | Court terme |

⚠️ **PIÈGE — le motif générique**
« C'est un système critique, on ne peut pas y toucher » n'est pas un motif : c'est un refus non qualifié. Exiger le type exact d'impossibilité change la conversation, parce que chaque type a un interlocuteur et un horizon différents. Beaucoup d'impossibilités déclarées techniques se révèlent temporelles ou métier une fois qualifiées.

🖼 **SCHÉMA — Hiérarchie des compensations.** *Pyramide inversée à six rangs, du plus protecteur au moins protecteur, avec le coût récurrent en regard.*

## 20.2 La hiérarchie des mesures compensatoires

Toutes les compensations ne se valent pas. Voici l'ordre d'efficacité décroissante, à parcourir de haut en bas.

| Rang | Mesure | Effet | Coût récurrent |
|---|---|---|---|
| 1 | **Supprimer l'exposition** | Le chemin d'attaque disparaît, y compris pour les vulnérabilités futures (§11.8) | Nul |
| 2 | **Isoler** | L'actif n'est atteignable que depuis un périmètre restreint | Faible |
| 3 | **Désactiver la fonction vulnérable** | La vulnérabilité n'est plus atteignable | Nul si la fonction est inutile |
| 4 | **Filtrer** | Les tentatives connues sont bloquées en amont | Maintien des règles |
| 5 | **Renforcer la détection** | On ne bloque pas, on voit | **Élevé** — charge d'analyse permanente |
| 6 | **Accepter le risque** | Rien n'est fait, la décision est formalisée | Nul, mais le risque est porté |

**La règle d'or** : ne descendez d'un rang que si le rang supérieur est réellement impossible, et écrivez pourquoi. La majorité des organisations sautent directement au rang 5, qui est le plus coûteux et le moins protecteur — parce que c'est le seul qui ne demande de négociation avec personne.

## 20.3 La correction virtuelle

Bloquer l'exploitation d'une vulnérabilité en amont de l'actif, sans le modifier : règle de filtrage applicatif, signature de sonde réseau, restriction de protocole.

| Ce que ça apporte | Ce que ça n'apporte pas |
|---|---|
| Un délai — souvent quelques jours à quelques semaines | Une protection durable |
| Une couverture de masse rapide sur plusieurs actifs | Une garantie : les contournements de signature sont fréquents |
| Une trace des tentatives, précieuse en investigation | Une protection contre un attaquant déjà à l'intérieur du périmètre filtré |

📌 **LIMITES** — Une règle de correction virtuelle protège contre les **variantes connues** d'une exploitation. Elle est écrite à partir des exploits observés ; une variante suffisante la contourne. Traitez-la comme un **délai acheté**, jamais comme une correction, et donnez-lui une date d'expiration comme à toute compensation.

## 20.4 Réduire la surface

Souvent la mesure la plus efficace et la moins employée : la vulnérabilité concerne un composant que vous n'utilisez pas.

**Les quatre gestes**, par ordre d'application :

1. **Désactiver le service** — si personne ne l'utilise, il n'a pas à tourner.
2. **Désactiver le module ou l'extension** vulnérable, quand le service est nécessaire mais pas cette fonction.
3. **Désactiver le protocole** — protocoles hérités, versions anciennes, méthodes d'authentification faibles.
4. **Restreindre les droits** du compte sous lequel s'exécute le service, pour limiter l'effet d'une exploitation réussie.

**La vérification préalable indispensable** : mesurer l'usage réel avant de désactiver. Un service qui semble inutilisé peut porter un traitement mensuel ou une intégration partenaire (§10.5, dépendance temporelle). Observez sur un cycle métier complet.

## 20.5 Isolation d'urgence : ce qui est faisable en 24 heures

| Mesure | Délai réaliste | Effet | Risque métier |
|---|---|---|---|
| Restreindre l'accès à des plages d'adresses connues | 1 à 4 h | Fort | Faible si le besoin est bien cerné |
| Placer l'actif derrière un accès distant authentifié | 4 à 24 h | Fort | Modéré : change l'usage |
| Couper l'exposition externe | **Minutes** | Total sur ce vecteur | Selon l'usage |
| Isoler dans un segment réseau dédié | Jours à semaines | Fort | Élevé : dépendances à recenser |
| Segmentation générale du réseau | Mois | Structurel | Projet |

**Les trois premières lignes sont réalisables dans la journée** et couvrent la majorité des besoins d'urgence. La segmentation générale est un projet d'architecture : utile, mais elle ne répond pas à une crise en cours.

## 20.6 La surveillance renforcée comme compensation

Elle est légitime, et son coût est systématiquement sous-estimé.

**Ce qu'elle exige réellement** : une règle de détection écrite et testée, une source de journaux couvrant l'actif, quelqu'un pour analyser les alertes, une procédure de réaction, et une durée de vie définie.

⚠️ **PIÈGE — la surveillance sans destinataire**
Une règle de détection dont les alertes arrivent dans une boîte que personne ne lit ne constitue pas une compensation. C'est la forme la plus courante de compensation fictive : elle coche la case, ne protège de rien, et donne une fausse assurance à toute la chaîne de décision.

**La question à poser avant d'accepter cette compensation** : *qui regarde, quand, et que fait-il exactement s'il voit quelque chose ?* Sans réponse nominative, la mesure n'est pas recevable.

## 20.7 Les sept attributs obligatoires

C'est le cœur du chapitre, et la règle qui empêche le pourrissement. **Toute mesure compensatoire porte ces sept attributs**, sans exception.

| # | Attribut | Pourquoi |
|---|---|---|
| 1 | **Propriétaire nommé** | Quelqu'un répond de son maintien |
| 2 | **Date de début** | Point de départ du décompte |
| 3 | **Date d'expiration** | Sans elle, la mesure devient permanente par défaut |
| 4 | **Moyen de vérification** | Comment sait-on qu'elle est toujours active ? |
| 5 | **Coût opérationnel** | Charge récurrente, à comparer au coût de la correction |
| 6 | **Condition de sortie** | Quel événement met fin à la compensation |
| 7 | **Contrôle périodique** | Fréquence de la vérification effective |

**Le quatrième attribut est celui qu'on oublie**, et c'est le plus important en pratique. Une règle de filtrage supprimée lors d'une refonte réseau, une isolation annulée par un nouveau routage, une surveillance désactivée lors d'un changement d'outil : la compensation disparaît sans que personne ne le sache, et le risque revient sans qu'aucune alerte ne se déclenche.

✅ **BONNE PRATIQUE (P0)** — Le contrôle périodique de l'existence effective des compensations est un **point d'ordre du jour du comité MCS** (§9.3). Cinq minutes par mois. C'est ce qui distingue une compensation d'une intention.

## 20.8 Formaliser l'acceptation de risque

Quand aucune compensation n'est possible, reste l'acceptation formelle. Les sept champs de la dérogation (§7.4) s'appliquent, avec trois exigences supplémentaires :

- le **signataire** est le propriétaire métier, à un niveau proportionné à l'enjeu (§9.2) ;
- le **risque est décrit en termes métier**, pas techniques : « une compromission de ce serveur exposerait les données de paie de 1 380 salariés » et non « exécution de code à distance » ;
- la **revue est datée**, et le renouvellement remonte d'un niveau (§7.4).

## 20.9 ⚠️ Le compensatoire permanent

**La mécanique du pourrissement**, en cinq étapes qui se répètent partout :

```
1. Correction impossible → compensation mise en place, durée 3 mois
2. À 3 mois, rien n'a changé → prolongation « le temps de »
3. La personne qui l'a mise en place change de poste
4. La compensation n'est plus vérifiée : personne ne sait si elle est active
5. Deux ans plus tard, l'actif est considéré comme « traité »
```


**Les trois garde-fous** qui cassent ce cycle : l'attribut n° 4 (moyen de vérification) contrôlé périodiquement ; le renouvellement remontant d'un niveau hiérarchique (§7.4) ; et l'indicateur **âge moyen des compensations actives**, présenté au comité — c'est la mesure la plus honnête de la dette réellement portée par l'organisation.

## 20.10 🔬 Mini-lab 7 — Rédiger une dérogation auditable

**Objectif** — Produire une fiche complète, défendable en audit, et arbitrer le niveau de signature.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §7.4, §20.2, §20.7, annexe C.4 · **Livrable** formulaire D.4 rempli.
**Compétences validées** — ✔ parcourir la hiérarchie des compensations ✔ écrire un risque en termes métier ✔ choisir le bon signataire ✔ aligner une date d'expiration sur un événement décisionnel ✔ distinguer horloge de risque et horloge de traitement

**Dossier fourni**

| Élément | Donnée |
|---|---|
| Actif | `SRV-CRM-02`, serveur applicatif, environnement production |
| Constat | Vulnérabilité critique sur un composant web · exploitable **à distance sans authentification** · exploitation non observée à ce jour |
| Correction disponible | Oui, mais elle exige la montée en version majeure de l'application métier |
| Coût de la correction | 40 k€ facturés par l'éditeur, **non budgétés sur l'exercice** |
| Délai éditeur | Version compatible disponible sous 3 mois après commande |
| Exposition | Réseau bureautique interne · **non publié sur Internet** |
| Utilisateurs | 60 personnes du service commercial |
| Données | Fichier clients — 2 800 enregistrements, données à caractère personnel |
| Classe de service | C2 · délai politique pour critique non exploitée : 30 jours |
| Journalisation | Accès applicatifs conservés 90 jours, exportés vers la plateforme centrale |
| Contexte | Exercice budgétaire clos ; vote du budget suivant en mars |

**Questions**
(a) Rédigez la fiche D.4 complète.
(b) Qui signe, et pourquoi ?
(c) Quelle date d'expiration retenez-vous, et sur quoi l'alignez-vous ?
(d) Que devient l'horloge de risque pendant la dérogation ?
(e) Quelles conditions de révocation anticipée écrivez-vous ?

---

**Corrigé commenté — fiche D.4 remplie**

| Champ | Contenu |
|---|---|
| **Identifiant** | `DER-2027-018` · version 1.0 · émise le 12/06/2027 |
| **Objet** | `SRV-CRM-02` · vulnérabilité `[identifiant]` sur composant web · correction nécessitant la montée en version majeure de l'application de gestion commerciale |
| **Type d'impossibilité** | ☑ **Budgétaire** — le correctif existe et est techniquement applicable |
| **Analyse de risque, en termes métier** | Un poste bureautique compromis permettrait à un attaquant d'atteindre ce serveur sans authentification et d'accéder au fichier clients : 2 800 enregistrements comportant nom, coordonnées et historique commercial. Conséquences : notification de violation de données, atteinte à la relation client, exposition contractuelle vis-à-vis de trois grands comptes dont le contrat comporte une clause de sécurité. Exploitation non observée à ce jour dans le monde. |
| **Exposition mesurée** | ☑ réseau bureautique — ☐ Internet · joignable depuis 340 postes avant compensation |
| **Exploitation observée** | ☑ non |
| **Mesures compensatoires** | **1.** Restriction d'accès réseau : le serveur n'est joignable que depuis les 60 postes du service commercial (rang 2 de la hiérarchie §20.2). **2.** Règle de filtrage applicatif bloquant les motifs d'exploitation publiés (rang 4). **3.** Alerte sur toute tentative d'accès depuis une origine non autorisée, destinataire nommé (rang 5). **Rangs écartés** : rang 1 — l'exposition interne est nécessaire à l'usage ; rang 3 — la fonction vulnérable est celle utilisée par l'application. |
| **Moyen de vérification** | Test mensuel d'accès depuis un poste hors périmètre autorisé — **doit échouer** · vérification de la présence effective de la règle de filtrage · test d'alerte trimestriel avec accusé de traitement |
| **Fréquence du contrôle** | Mensuelle, inscrite à l'ordre du jour du comité MCS |
| **Coût opérationnel** | ≈ 2 h/mois de vérification + charge d'analyse des alertes |
| **Propriétaire de la compensation** | `[responsable exploitation]` |
| **Signataire** | `[directeur commercial]` — propriétaire métier |
| **Date de début** | 12/06/2027 |
| **Date d'expiration** | **31/03/2028** |
| **Conditions de sortie** | Migration réalisée · **ou** exploitation de cette vulnérabilité observée dans le monde · **ou** compromission avérée d'un poste du service commercial |
| **Conditions de révocation anticipée** | Publication d'un exploit fonctionnel · entrée de la vulnérabilité dans un catalogue d'exploitation avérée · modification de l'exposition du serveur · incident de sécurité touchant le service commercial |
| **Nombre de renouvellements** | 0 |
| **Date de revue** | Trimestrielle — 12/09/2027, 12/12/2027, 12/03/2028 |

**(b) Le signataire — arbitrage**

Le propriétaire métier, ici le directeur commercial. **Trois raisons** :

1. C'est lui qui **porte le risque** : ce sont ses données clients et sa relation commerciale.
2. C'est lui qui **détient le levier** : le budget de 40 k€ relève de son arbitrage ou de son plaidoyer.
3. Faire signer la sécurité lui transférerait un risque qu'elle n'a pas les moyens de porter, et déresponsabiliserait le métier (§9.2).

⚠️ **Le cas limite** : si les données concernées relevaient d'un régime sensible — données de santé, données de paiement —, la grille C.4 imposerait une signature au niveau de la direction générale, indépendamment du fait que l'actif soit interne et de classe C2.

**(c) La date d'expiration**

Le **31 mars 2028**, alignée sur le vote du budget suivant. C'est le point du §7.4 : une date d'expiration doit correspondre à un **événement décisionnel réel**, pas à une durée arbitraire.

| Date envisageable | Évaluation |
|---|---|
| « jusqu'à la migration » | ❌ Ce n'est pas une date. Rejet automatique |
| 12/12/2027 — 6 mois | ⚠️ Tombe avant tout arbitrage budgétaire : le renouvellement sera mécanique |
| **31/03/2028 — vote du budget** | ✅ Le renouvellement coïncide avec le moment où quelque chose peut changer |
| 31/12/2028 | ❌ Trop long : 18 mois sans point de décision |

**(d) L'horloge de risque**

Elle **continue de courir** (§17.5). La dérogation suspend l'horloge de traitement — l'équipe n'est pas en faute — mais le risque est porté chaque jour. Concrètement :

- l'horloge SLA est suspendue au 12/06/2027, avec motif « dérogation `DER-2027-018` » ;
- l'horloge de risque affiche, au comité de décembre, **183 jours de risque porté** ;
- ce chiffre est celui qui apparaît au tableau de bord de direction, pas le taux de respect des délais.

C'est ce qui empêche la dérogation de rendre le retard invisible.

**(e) Les conditions de révocation anticipée**

Elles sont distinctes des conditions de sortie : la sortie met fin à la dérogation parce que le problème est résolu ; la **révocation** y met fin parce que l'hypothèse sur laquelle elle reposait a changé. Ici, l'hypothèse centrale est *« exploitation non observée »*. Les quatre conditions écrites la surveillent directement.

**Les quatre erreurs attendues**

1. Pas de date d'expiration, ou date exprimée comme un événement flou.
2. Compensations non vérifiables — « surveillance renforcée » sans destinataire ni test (§20.6).
3. Signature par la sécurité au lieu du métier.
4. Risque décrit en termes techniques — « exécution de code à distance » ne permet à aucun directeur commercial de décider en connaissance de cause.

## 20.11 🔴 FIL ROUGE — juin 2027 : la ligne 2 de Saint-Étienne

Une vulnérabilité activement exploitée est publiée sur le système de supervision de la ligne d'assemblage 2 — le constat n° 5 du mini-lab 4, désormais réel. Classe C4.

**Les faits.** Le correctif existe. Le constructeur ne l'a pas validé pour la configuration installée ; l'appliquer sans validation fait tomber la garantie et invalide la qualification du procédé, ce qui a des conséquences réglementaires sur la production de dispositifs médicaux. Le prochain arrêt de production est en novembre — cinq mois.

**Le parcours de la hiérarchie du §20.2.**

| Rang | Examiné ? | Résultat |
|---|---|---|
| 1 — Supprimer l'exposition | Oui | Le poste n'est pas exposé à Internet. Déjà acquis |
| 2 — **Isoler** | **Oui** | **Retenu** : le poste communiquait avec le réseau bureautique pour un export de données de production. L'export est basculé en dépôt de fichiers unidirectionnel |
| 3 — Désactiver la fonction | Oui | Impossible : la fonction vulnérable est celle utilisée par la supervision |
| 4 — **Filtrer** | **Oui** | **Retenu** : règle de filtrage sur le conduit entre zones industrielles |
| 5 — Détection renforcée | Oui | Retenue en complément, avec destinataire nommé et procédure |
| 6 — Accepter | — | Non atteint |

**Ce qui a rendu la solution possible.** Thomas Berger savait que l'export vers la bureautique n'était plus utilisé depuis dix-huit mois — l'outil qui le consommait avait été remplacé. Personne n'avait jamais posé la question. La suppression de ce flux, décidée en vingt minutes, retire le principal chemin d'accès au poste.

**La fiche produite.** Compensation valable jusqu'au 30 novembre 2027, date de l'arrêt de production. Propriétaire : Thomas Berger. Vérification mensuelle : test d'accès depuis le réseau bureautique — doit échouer — et contrôle de la règle de filtrage. Signataire : le directeur industriel. Condition de sortie : correctif validé par le constructeur et appliqué pendant l'arrêt de novembre.

**Le point que Claire Nadeau porte au comité.** La compensation n'est pas un pis-aller subi : dans ce cas précis, l'isolation obtenue est **plus protectrice que le correctif** n'aurait été, puisqu'elle protège aussi contre les vulnérabilités futures du même poste (§11.8). Elle sera maintenue **après** l'application du correctif en novembre.

**Livrable de l'épisode.** La fiche de compensation avec ses sept attributs, et une revue systématique des flux entrants des postes de supervision — qui révélera en juillet trois autres flux devenus inutiles.

→ La suite en 🔴 §21.11, quand une vulnérabilité sur la passerelle d'accès distant ne laissera pas cinq mois pour décider.

→ **Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j** : réagir quand tout s'accélère.

## Synthèse mentale du chapitre 20

« On ne peut pas patcher » recouvre cinq impossibilités distinctes, avec des interlocuteurs et des horizons différents : les qualifier change la conversation, et beaucoup d'impossibilités déclarées techniques se révèlent temporelles ou métier. La hiérarchie des compensations se parcourt de haut en bas — supprimer l'exposition, isoler, désactiver, filtrer, détecter, accepter — et l'on ne descend d'un rang qu'en écrivant pourquoi le précédent est impossible. La plupart des organisations sautent directement à la détection renforcée, la plus coûteuse et la moins protectrice, parce qu'elle ne demande de négociation avec personne. La correction virtuelle achète un délai, jamais une protection durable. Sept attributs rendent une compensation réelle, dont le moyen de vérification, celui qu'on oublie et qui empêche la disparition silencieuse de la mesure. Enfin, une compensation bien choisie peut être plus protectrice qu'un correctif, puisqu'elle couvre aussi les vulnérabilités futures du même actif.

**Trois questions de vérification**

1. Un exploitant vous répond « c'est un système critique, on ne peut pas y toucher ». Quelle est votre question suivante, et pourquoi change-t-elle la nature de la discussion ?
2. Pourquoi la surveillance renforcée est-elle simultanément la compensation la plus choisie et la moins protectrice ?
3. Une compensation mise en place il y a dix-huit mois est-elle encore active ? Comment le savez-vous, et qu'auriez-vous dû prévoir au moment de la décision ?

---
