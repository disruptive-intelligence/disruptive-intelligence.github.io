---
title: PARTIE V — Contextes spécialisés
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 6
chapters: 10
---

Les parties précédentes ont construit un dispositif complet. Celle-ci le confronte à cinq contextes où ses règles ne s'appliquent pas telles quelles : l'industriel, le cloud, le logiciel en ligne, le legacy irréductible, et le produit livré à des clients. Chacun conserve le même niveau d'exigence — cas concret, livrable, erreur fréquente, limite explicite.

---

## Chapitre 29 — MCS en environnement industriel (OT / ICS)

### 29.1 Ce qui change fondamentalement

Le §3.7 a posé les repères. Voici ce que cela implique concrètement pour un programme de MCS.

| Dimension | Informatique de gestion | Industriel |
|---|---|---|
| Priorité | Confidentialité, intégrité | **Sûreté des personnes, puis disponibilité** |
| Durée de vie | 3 à 7 ans | 15 à 25 ans |
| Fenêtre | Nuit, week-end | **Arrêt de production planifié, souvent annuel** |
| Validation du correctif | Interne | **Constructeur**, sous peine de perte de garantie et de qualification |
| Conséquence d'une erreur | Perte de service | **Risque physique, rebut de production, arrêt de ligne** |
| Qui décide | DSI, métier | **Responsable de production et responsable sûreté** |

🏢 **VU EN ATELIER** — Première visite d'un RSSI sur un site de production. Il demande quand la ligne peut être arrêtée pour appliquer des correctifs. Le responsable de production répond : « en août, pendant trois jours, et il faudra me dire lequel des trois ». Ce n'était pas de l'obstruction : c'était la réponse exacte à la question posée.

**Le renversement à intégrer.** En informatique de gestion, l'argument « il faut corriger » l'emporte généralement sur « ça risque de casser ». En industriel, c'est l'inverse — et c'est **légitime** : une ligne à l'arrêt a un coût immédiat et mesurable, un défaut sur un automate peut avoir des conséquences physiques, et une modification non validée peut invalider une qualification réglementaire.

Un responsable sécurité qui arrive dans un environnement industriel avec ses réflexes bureautiques échoue en trois semaines. La démarche n'est pas « corriger plus vite », c'est **maîtriser l'exposition, préparer longtemps à l'avance, et appliquer pendant les arrêts**.

### 29.2 Le cadre normatif appliqué au maintien

La série de normes de sécurité des systèmes d'automatisation industriels fournit une structure directement utilisable, indépendamment de toute certification.

| Concept | Définition | Usage en MCS |
|---|---|---|
| **Zone** | Ensemble d'actifs partageant les mêmes exigences de sécurité | Détermine le périmètre d'une compensation |
| **Conduit** | Chemin de communication entre zones | C'est là que se placent les mesures de filtrage (§20.2) |
| **Niveau de sécurité** | Niveau de résistance attendu d'une zone | Calibre l'effort |
| **Répartition des rôles** | Exploitant / intégrateur / fabricant | Détermine **qui doit corriger** |

**L'apport principal pour le MCS** : la répartition des responsabilités. Beaucoup de blocages industriels viennent de ce que personne n'a établi qui, de l'exploitant, de l'intégrateur ou du fabricant, doit produire, valider et appliquer un correctif. Poser la question dans ces termes débloque plus de situations qu'une discussion technique.

### 29.3 L'inventaire industriel

Le chapitre 10 s'applique, avec des méthodes différentes.

| Méthode | Applicabilité | Précaution |
|---|---|---|
| **Écoute passive du trafic** | Méthode par défaut | Aucun risque pour le procédé ; nécessite un point de capture |
| **Extraction depuis les outils d'ingénierie** | Très riche : versions d'automates, programmes, configurations | Nécessite l'accès et la coopération de l'équipe automatisme |
| **Inventaire manuel** | Toujours possible | Chronophage, mais souvent le plus fiable sur les équipements anciens |
| **Documentation d'installation** | Fournie par l'intégrateur | Souvent périmée, mais c'est un point de départ |
| Scan actif | **Passif par défaut, actif sous procédure** | Validation explicite, test préalable, procédure d'arrêt, de préférence hors production (§3.7) |

✅ **BONNE PRATIQUE (P0)** — Commencez par l'inventaire manuel réalisé **avec** l'équipe de maintenance, pas par un outil. Deux journées passées avec le responsable automatisme produisent un inventaire plus fiable et plus utile qu'un mois d'outillage — et elles construisent la relation sans laquelle rien ne se fera ensuite.

### 29.4 Les correctifs industriels

**Le cycle réel**, très différent de celui du chapitre 18 :

```
Vulnérabilité publiée par le constructeur ou un centre de réponse
   → le constructeur qualifie l'applicabilité à VOTRE configuration
   → il publie (ou non) un correctif validé
   → l'intégrateur valide sur votre installation spécifique
   → planification sur le prochain arrêt de production
   → application, avec matériel de secours prêt
   → tests fonctionnels et de sûreté
   → remise en production, qualification si nécessaire
```

Ce cycle prend **des mois**. Entre la publication et l'application, la compensation n'est pas une solution dégradée : c'est le mode normal de traitement.

**Les trois cas de figure :**

| Cas | Fréquence | Traitement |
|---|---|---|
| Correctif validé par le constructeur | Minoritaire | Planification sur arrêt |
| Correctif existant, non validé | Fréquent | Compensation jusqu'à validation, relance du constructeur par écrit |
| Aucun correctif — produit hors support | Fréquent sur les équipements anciens | Compensation permanente et plan de remplacement (ch. 32) |

🖼 **SCHÉMA — Chaîne de mise à jour hors ligne.** *Flux linéaire à huit étapes, de la source officielle à la preuve d'installation, avec les points de double contrôle signalés.*

### 29.5 La chaîne complète de mise à jour hors ligne

C'est le livrable technique central du chapitre. Un environnement industriel n'est pas connecté à Internet ; les correctifs doivent donc y entrer par un chemin maîtrisé.

```
① SOURCE OFFICIELLE
   Portail constructeur, compte nominatif, canal identifié
        ↓
② POSTE DE TÉLÉCHARGEMENT CONTRÔLÉ
   Poste dédié, durci, à jour, hors du réseau industriel
        ↓
③ VÉRIFICATION D'INTÉGRITÉ
   Signature ou empreinte publiée par le constructeur — comparée, pas supposée
        ↓
④ ANALYSE ET VALIDATION
   Analyse antimalware multi-moteurs · vérification du contenu · validation fonctionnelle
        ↓
⑤ SUPPORT AMOVIBLE MAÎTRISÉ
   Support dédié, identifié, effacé avant usage, jamais utilisé ailleurs
        ↓
⑥ SAS DE TRANSFERT
   Station de décontamination ou poste dédié en zone intermédiaire
        ↓
⑦ ENVIRONNEMENT INDUSTRIEL
   Application selon la procédure constructeur, matériel de secours prêt
        ↓
⑧ PREUVE D'INSTALLATION
   Relevé de version, journal de transfert, procès-verbal signé
```

**La gouvernance de cette chaîne**, sans laquelle elle ne tient pas :

| Règle | Raison |
|---|---|
| **Double contrôle** aux étapes ③ et ④ | Deux personnes valident l'intégrité et l'analyse |
| **Journal des transferts** | Qui a transféré quoi, quand, vers quel équipement |
| **Supports dédiés et identifiés** | Marqués physiquement, stockés sous contrôle |
| **Interdiction stricte des supports personnels** | Vecteur d'entrée historique le plus documenté en industriel |
| **Dépôt miroir hors ligne** | Évite de retélécharger, conserve l'historique des versions validées |
| **Procédure de retour arrière** | Version précédente conservée et testée |
| **Pièces de rechange prépatchées** | Un équipement de remplacement stocké depuis trois ans porte une version ancienne (§28.7) |

⚠️ **PIÈGE — la clé USB du prestataire**
Le scénario le plus fréquent et le mieux documenté : un technicien du constructeur intervient pour une maintenance, connecte son propre support à un automate, et introduit ce qui s'y trouve. La règle — supports fournis par l'exploitant, analysés, dédiés — doit figurer dans le contrat de maintenance et être vérifiée à chaque intervention, pas seulement écrite.

### 29.6 La maintenance à distance des fournisseurs

Beaucoup d'installations industrielles disposent d'un accès distant permanent pour le constructeur. C'est souvent le chemin d'entrée le plus direct vers la zone industrielle.

**Les cinq exigences** :

1. **Accès à la demande**, activé pour une intervention, désactivé après — jamais permanent.
2. **Authentification multifacteur** et compte nominatif, pas un compte partagé du constructeur.
3. **Traçabilité** : enregistrement des sessions, journal accessible de votre côté.
4. **Supervision** : l'intervention est accompagnée côté exploitant.
5. **Contractualisation** : ces règles figurent au contrat de maintenance (§13.3).

### 29.7 Compensations spécifiques à l'industriel

| Mesure | Applicabilité |
|---|---|
| **Segmentation par zones et conduits** | Mesure structurante n° 1 |
| Filtrage sur les conduits | Contrôle des protocoles autorisés entre zones |
| **Suppression des flux devenus inutiles** | Souvent le gain le plus rapide (§20.11) |
| Postes d'ingénierie durcis et dédiés | Vecteur d'entrée majeur |
| Contrôle des supports amovibles | Voir §29.5 |
| Surveillance passive du trafic industriel | Détecte les anomalies sans perturber |
| Diodes de données | Pour les flux strictement sortants |

### 29.8 ✅ Livrable — Le plan de MCS industriel pluriannuel

Structuré par **arrêts de production**, et non par mois :

| Section | Contenu |
|---|---|
| Inventaire | Équipements, versions, statut de support, criticité procédé |
| Vulnérabilités connues | Par équipement, avec statut de validation constructeur |
| Compensations en place | Avec les sept attributs du §20.7 |
| Planification par arrêt | Ce qui sera appliqué au prochain arrêt, et pourquoi |
| Équipements sans correctif | Plan de remplacement ou sanctuarisation (ch. 32) |
| Relances constructeurs | Demandes écrites en cours, avec dates |
| Pièces de rechange | Versions stockées, plan de mise à niveau |

### 29.9 ⚠️ Les erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Scan actif sur réseau industriel sans validation | Défaut d'automate, arrêt de ligne, et perte durable de la confiance |
| Correctif appliqué hors validation constructeur | Perte de garantie, invalidation de qualification |
| Confondre sûreté et sécurité | Les systèmes de sûreté relèvent d'un régime propre, à ne jamais modifier sans processus dédié |
| Imposer les délais bureautiques | Rejet immédiat, et fin de la coopération |
| Traiter l'industriel comme un sous-ensemble de l'informatique | Erreur de posture : ce sont deux métiers |
| Négliger la relation humaine | Sans le responsable maintenance, aucun accès, aucune information, aucun résultat |

### 29.10 📌 Limites

- **Le temps long est irréductible.** Un cycle de validation constructeur ne se comprime pas ; il s'anticipe.
- **Certains équipements ne seront jamais corrigés.** Le fournisseur a disparu, ou le produit est hors support depuis dix ans. C'est le chapitre 32.
- **La visibilité restera partielle.** L'écoute passive ne voit que ce qui communique.
- **Le budget dépend de la production**, pas de la DSI. Les arbitrages se font dans un autre circuit, avec d'autres critères.

### 29.11 🔴 FIL ROUGE — février 2028 : le bilan de l'arrêt de novembre

L'arrêt de production de novembre 2027 a permis d'appliquer, sur la ligne 2 de Saint-Étienne, le correctif compensé depuis juin (§20.11). Thomas Berger et Claire Nadeau font le bilan de deux ans de MCS industriel chez HELIOMED.

**Ce qui a été réalisé.**

| Action | Résultat |
|---|---|
| Inventaire manuel avec l'équipe maintenance | 11 postes de supervision, 14 automates, 3 réseaux distincts documentés pour la première fois |
| Segmentation en zones et conduits | 4 zones définies, flux inter-zones réduits de 23 à 9 |
| Suppression des flux inutiles | 6 flux supprimés, dont l'export vers la bureautique (§20.11) |
| Chaîne de mise à jour hors ligne | Formalisée, testée, appliquée en novembre |
| Accès distants constructeurs | 3 accès permanents supprimés, remplacés par des accès à la demande |
| Correctifs appliqués | 4, pendant l'arrêt de novembre |
| Équipements sans correctif possible | 3 automates, fournisseur disparu — compensation permanente |

**Ce que révèle le bilan.** Sur deux ans, **4 correctifs ont été appliqués**. Rapporté aux standards de l'informatique de gestion, le chiffre paraît dérisoire. Mais la réduction d'exposition réelle vient d'ailleurs : suppression de 14 flux inter-zones, suppression de 3 accès distants permanents, et maîtrise des supports amovibles. Aucune de ces actions n'est un correctif.

**L'incident évité, et il est instructif.** En septembre, un technicien d'un constructeur se présente pour une intervention planifiée avec son propre support amovible contenant une mise à jour. La procédure du §29.5 est appliquée : refus du support, téléchargement depuis le portail officiel par HELIOMED, vérification d'empreinte, analyse. **L'empreinte ne correspond pas** à celle publiée par le constructeur. Après échange, il s'avère que le fichier du technicien datait d'une intervention précédente chez un autre client et avait été modifié localement. Aucune malveillance — mais un fichier non conforme, non tracé, qui aurait été installé sur un automate de production.

**Ce que Thomas Berger dit en comité**, et que Claire cite ensuite régulièrement : *« Il y a deux ans, j'aurais dit non à tout, parce qu'on me demandait d'appliquer des règles qui n'ont pas de sens ici. Aujourd'hui je dis oui à ce qui est validé, dans mes fenêtres, avec mes procédures. Ce qui a changé, ce n'est pas ma position, c'est qu'on me l'a demandé dans mes termes. »*

**Livrable de l'épisode.** Le plan de MCS industriel pluriannuel d'HELIOMED, calé sur les arrêts de production de 2028 et 2029, et la chaîne de mise à jour hors ligne documentée — Annexe L.

→ La suite en 🔴 §30.11, quand le fournisseur cloud imposera une échéance sans négociation possible.

→ **Chapitre 30 — MCS du cloud : infrastructure, plateforme et services managés** : le cloud, où vous pilotez l'anticipation plutôt que la correction.

### Synthèse mentale du chapitre 29

En industriel, la sûreté des personnes et la disponibilité priment, les équipements vivent quinze à vingt-cinq ans, les fenêtres sont annuelles et les correctifs doivent être validés par le constructeur : arriver avec des réflexes bureautiques garantit l'échec en trois semaines. La démarche n'est pas de corriger plus vite mais de maîtriser l'exposition, préparer très à l'avance, et appliquer pendant les arrêts — la compensation n'est pas un pis-aller, c'est le mode normal de traitement. L'inventaire commence par deux journées avec l'équipe de maintenance, pas par un outil : elles produisent plus d'information et construisent la relation sans laquelle rien ne se fera. La chaîne de mise à jour hors ligne en huit étapes, avec double contrôle, journal des transferts et supports dédiés, est le livrable technique central. Enfin, la réduction d'exposition réelle vient rarement des correctifs : elle vient de la suppression des flux inutiles, des accès distants permanents et de la maîtrise des supports.

**Trois questions de vérification**

1. Un responsable de production refuse toute intervention sur ses automates. Qu'avez-vous probablement mal formulé, et comment reprenez-vous la discussion ?
2. Décrivez les huit étapes de la chaîne de mise à jour hors ligne, et indiquez à quelles étapes le double contrôle s'applique.
3. En deux ans, vous n'avez appliqué que quatre correctifs sur votre parc industriel. Comment démontrez-vous à votre direction que le risque a néanmoins fortement diminué ?

---

## Chapitre 30 — MCS du cloud : infrastructure, plateforme et services managés

### 30.1 La responsabilité partagée, décodée

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

### 30.2 Images et instances

**Le mécanisme central** : une instance créée à partir d'une image porte tout le retard de cette image (§28.5). Dans le cloud, ce mécanisme est amplifié par la mise à l'échelle automatique — une montée en charge peut créer vingt instances à partir d'une image vieille de six mois.

| Objet | Traitement |
|---|---|
| Catalogue d'images | Images validées, versionnées, avec une cadence de reconstruction |
| Instances longue durée | Traitées comme des serveurs classiques, ou remplacées (§3.5) |
| Groupes à mise à l'échelle | **La correction passe par l'image**, jamais par l'instance |
| Instances éphémères | N'apparaissent pas dans un inventaire réseau : inventaire par l'interface du fournisseur |

**L'indicateur préventif central** dans ce contexte : **l'âge de l'image** en service. Une organisation qui maintient toutes ses images à moins de 30 jours réduit fortement le volume de constats individuels à traiter — sans supprimer le besoin d'analyse de vulnérabilités ni de mesure d'exposition, puisqu'une image récente peut embarquer un composant vulnérable.

### 30.3 Bases de données et services managés

| Événement | Ce que vous contrôlez |
|---|---|
| Correctif mineur | La fenêtre, parfois le report de quelques semaines |
| Version majeure disponible | Le moment de la migration, **jusqu'à une date limite** |
| Fin de support d'une version | Rien : la migration devient forcée |
| Changement de comportement par défaut | Rien, sauf à lire les annonces |

**La conséquence pour le MCS** : sur ces services, **vous ne pilotez pas la correction, vous pilotez l'anticipation**. Le travail consiste à connaître les échéances de fin de support des versions utilisées, et à planifier les migrations avant la date limite — faute de quoi elles seront subies, au moment choisi par le fournisseur.

✅ **BONNE PRATIQUE (P0)** — Intégrez les versions de services managés à votre référentiel d'obsolescence (§12.2), au même titre que les systèmes d'exploitation. C'est l'oubli le plus fréquent des programmes de MCS en environnement cloud.

### 30.4 Orchestrateurs managés et exécution sans serveur

| Objet | Contrainte | Anticipation nécessaire |
|---|---|---|
| Version du plan de contrôle | Support d'environ quatorze mois (§3.3), fenêtre imposée par le fournisseur | Planifier deux à trois montées par an |
| Images des nœuds | À votre charge | Cadence de remplacement |
| Interfaces dépréciées | Ruptures annoncées à l'avance | Inventaire des usages, migration progressive |
| Composants additionnels installés | Leur propre cycle | Souvent oubliés |
| Environnements d'exécution de fonctions | Support court, dépréciation forcée | Suivi par fonction, pas globalement |

⚠️ **PIÈGE — la version d'environnement d'exécution des fonctions**
Une organisation peut avoir déployé plusieurs centaines de fonctions au fil des années, chacune avec sa version d'environnement d'exécution. Quand le fournisseur déprécie une version, toutes les fonctions concernées doivent être migrées — et l'inventaire n'existe généralement pas. Constituez-le **avant** l'annonce de dépréciation, pas après.

### 30.5 Ce que le fournisseur corrige, et le prix

**Ce qu'il apporte** : les correctifs de l'infrastructure et, selon le service, du système et de l'environnement d'exécution, appliqués à une échelle et avec une rapidité qu'aucune organisation ne peut atteindre seule.

**Ce qu'il coûte** :

| Contrepartie | Manifestation |
|---|---|
| Perte du choix du moment | Les fenêtres sont imposées ou fortement contraintes |
| Changements sans préavis proportionné | Un comportement par défaut change à une date choisie par le fournisseur |
| Absence de retour arrière | Une fois la migration appliquée, elle n'est pas réversible |
| Preuve limitée | Vous ne pouvez pas produire de preuve technique sur la couche du fournisseur (§30.11) |

### 30.6 Identités et droits cloud

La dette d'autorisations est au cloud ce que la dette d'annuaire est au monde classique (§24.1), avec deux aggravations : les droits sont **plus fins et plus nombreux**, et ils sont **attribués par des équipes techniques** sans processus de revue.

| Objet | Risque |
|---|---|
| Rôles trop permissifs | Attribués « pour débloquer », jamais réduits |
| Clés d'accès de longue durée | Souvent dans du code, des scripts, des fichiers d'état (§23.5) |
| Identités de service | Pratiques, mais leurs droits sont rarement revus |
| Rôles hérités entre comptes ou abonnements | Chemins d'accès transverses invisibles |
| Accès de prestataires | Configurés une fois, jamais retirés (§13.5) |

**La mesure la plus rentable** : identifier les identités disposant de droits d'administration sur un abonnement ou un projet entier, et les réduire. Elles sont peu nombreuses, et ce sont elles qui transforment un incident en catastrophe.

### 30.7 Configuration et dérive de *tenant*

Le cloud a déplacé une part importante du risque de la vulnérabilité vers la **configuration** : stockage ouvert, base de données accessible publiquement, règle de filtrage trop large, journalisation désactivée, chiffrement non activé.

| Mécanisme | Rôle |
|---|---|
| **Contrôle de posture** | Détecte les configurations non conformes, en continu |
| **Garde-fous préventifs** | Empêchent la création d'une ressource non conforme — plus efficace que la détection |
| Description par code | Rend la configuration lisible et reproductible (§23.5) |
| Revue périodique | Traite ce que l'automatisme ne couvre pas |

✅ **BONNE PRATIQUE (P0)** — Privilégiez les **garde-fous préventifs** aux contrôles détectifs. Empêcher la création d'un stockage public coûte une politique ; détecter et corriger des stockages publics coûte un processus permanent. C'est le principe du §22.4 appliqué au cloud.

### 30.8 Écart entre le code et la réalité

Le §23.5 s'applique avec une acuité particulière : dans le cloud, créer une ressource à la main prend trente secondes, et la tentation est constante en situation d'urgence.

**Les trois mesures** : détection périodique des ressources non décrites par le code ; interdiction de la création manuelle en production, avec une procédure d'exception tracée ; et réconciliation systématique après tout incident ayant nécessité une action manuelle (règle de reversion du §23.7).

### 30.9 Multi-cloud et zones d'atterrissage

Une **zone d'atterrissage** est un socle standardisé — comptes, réseau, identités, journalisation, garde-fous — sur lequel les projets se déploient.

**Son intérêt pour le MCS** est direct : elle fait de la conformité un état par défaut plutôt qu'un contrôle *a posteriori*. Tout nouveau projet hérite des garde-fous, de la journalisation et des politiques d'identité.

📌 **LIMITES** — Le multi-cloud multiplie les référentiels, les mécanismes de correction, les calendriers de dépréciation et les compétences nécessaires. Chaque fournisseur supplémentaire ajoute un dispositif complet de MCS à maintenir, pas une simple extension.

### 30.10 ✅ Livrable — Matrice de responsabilité MCS par service

| Service utilisé | Modèle | Ce que le fournisseur maintient | Ce que nous maintenons | Fenêtre imposée | Préavis | Preuve disponible | Propriétaire |
|---|---|---|---|---|---|---|---|

**Comment l'utiliser** : la renseigner service par service, la faire valider par l'équipe qui exploite le service, et l'annexer aux dossiers de conformité (§8.8). Les lignes où la colonne « preuve disponible » est vide sont vos zones à déclarer non mesurées (§7.7).

### 30.11 🔴 FIL ROUGE — mars 2028 : l'échéance qu'on ne négocie pas

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

### Synthèse mentale du chapitre 30

La responsabilité diminue avec le niveau de service mais ne disparaît jamais, et les incidents se produisent dans les zones grises — images fournies mais instanciées par vous, versions majeures que vous choisissez jusqu'à une date limite, configurations par défaut qui privilégient la mise en service. Dans le cloud, l'indicateur qui remplace des centaines de constats individuels est l'âge de l'image en service. Sur les services managés, vous ne pilotez pas la correction mais l'anticipation : leurs versions doivent entrer au référentiel d'obsolescence au même titre que les systèmes d'exploitation, ce qui est l'oubli le plus fréquent. Le risque s'est largement déplacé de la vulnérabilité vers la configuration, et les garde-fous préventifs coûtent une politique là où la détection coûte un processus permanent. Enfin, chaque fournisseur supplémentaire n'ajoute pas une extension mais un dispositif complet de MCS à maintenir.

**Trois questions de vérification**

1. Votre fournisseur annonce la fin de support d'une version de service managé dans quatre mois. Qu'est-ce qui est négociable, qu'est-ce qui ne l'est pas, et quel processus aurait dû vous alerter onze mois plus tôt ?
2. Un groupe d'instances à mise à l'échelle automatique porte une vulnérabilité. Pourquoi corriger les instances est-il une perte de temps, et quel indicateur unique aurait prévenu la situation ?
3. Pourquoi un garde-fou préventif est-il structurellement supérieur à un contrôle de posture détectif, et dans quel cas le second reste-t-il indispensable ?

---

## Chapitre 31 — MCS des services en ligne, extensions et intégrations

### 31.1 La perte de maîtrise assumée

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

### 31.2 La veille éditeur sur les services en ligne

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

### 31.3 Les changements unilatéraux

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

### 31.4 La configuration du locataire comme objet de MCS

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

### 31.5 Extensions, places de marché et intégrations tierces

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

### 31.6 Autorisations déléguées et jetons

Le mécanisme mérite d'être compris, parce qu'il est contre-intuitif pour qui vient du monde des mots de passe.

Une autorisation déléguée accorde à une application un accès à des ressources **au nom d'un utilisateur ou d'une organisation**, matérialisé par un jeton. Trois propriétés en découlent :

1. **La rotation du mot de passe ne révoque rien.** Le jeton reste valide.
2. **La portée est souvent excessive.** Une application qui n'a besoin que de lire un agenda demande fréquemment un accès complet à la messagerie.
3. **La durée est longue**, et le renouvellement automatique.

**La révocation** est le seul moyen de mettre fin à un accès. Elle doit figurer dans le processus de départ d'un collaborateur et dans le décommissionnement d'un service (chapitre 35).

### 31.7 Comptes d'administration et accès invités

| Objet | Vérification |
|---|---|
| Comptes d'administration du service | Combien, nominatifs, avec authentification renforcée, revus quand ? |
| Comptes de secours | Existent-ils, sont-ils testés, sont-ils surveillés (§24.2) ? |
| Comptes de prestataires | À la demande ou permanents (§13.5) ? |
| Accès invités | Combien, depuis quand, encore justifiés ? |
| Comptes d'application | Rattachés à un propriétaire, avec des droits proportionnés ? |

**Les accès invités sont l'angle mort le plus courant** : accordés pour un projet, ils survivent des années, et donnent accès à des espaces de travail entiers.

### 31.8 Journalisation

Trois questions à poser à chaque service en ligne, et à documenter dans la matrice du §30.10 :

1. **Quels événements** sont journalisés — connexions, accès aux données, modifications de configuration, actions d'administration ?
2. **Pendant combien de temps**, et à quel niveau de licence ? La rétention par défaut est souvent de quelques mois, parfois de quelques jours.
3. **Peut-on les exporter** vers votre propre système de collecte ?

⚠️ La question de la rétention est celle qui décide, le jour d'un incident, si vous pourrez conclure ou non (§21.3). Une rétention de 90 jours signifie que toute question portant sur une période antérieure restera sans réponse — comme dans le fil rouge du §25.22.

### 31.9 La preuve fournie par le fournisseur

Les rapports d'audit tiers et attestations fournis par les prestataires en ligne ont une valeur réelle, et des limites précises. Ils **ne suffisent pas à eux seuls** à établir la correction de votre configuration :

| Ce qu'ils établissent | Ce qu'ils n'établissent pas |
|---|---|
| Le fournisseur dispose d'un dispositif de sécurité audité | Que **votre** configuration est correcte |
| Le périmètre audité est décrit | Que ce périmètre couvre le service que vous utilisez |
| Les contrôles ont été testés à une date | L'état actuel |

**Ce qu'il faut lire dans un tel rapport** : le périmètre exact, la période couverte, les exceptions relevées, et la liste des contrôles laissés à la charge du client — cette dernière section est celle qui vous concerne directement, et c'est celle que personne ne lit.

### 31.10 Fin de vie d'une offre et réversibilité

Un fournisseur peut arrêter un service, être racheté, ou modifier son modèle. Trois questions à traiter **avant** la souscription, jamais après :

1. **Comment récupérer nos données ?** Format, exhaustivité, délai, coût.
2. **Quel préavis** en cas d'arrêt du service ?
3. **Que se passe-t-il pour les données à la fin du contrat ?** Suppression, délai, preuve.

### 31.11 ⚠️ « C'est du SaaS, c'est maintenu »

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

### 31.12 🔴 FIL ROUGE — avril 2028 : le connecteur de 2021

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

### Synthèse mentale du chapitre 31

Sur un service en ligne, la gestion des correctifs disparaît de votre périmètre et ce qui la remplace est plus difficile à outiller : veille sur les changements, configuration du locataire, contrôle des intégrations. Le mécanisme le plus fréquent d'élargissement involontaire de surface est la fonctionnalité activée par défaut chez tous les clients — votre configuration n'a pas changé, votre exposition si, d'où la nécessité d'un état de référence comparé périodiquement. Une autorisation déléguée accordée par un simple utilisateur crée un accès permanent que la rotation du mot de passe ne révoque pas, souvent surdimensionné, et invisible de tout inventaire d'application. Les rapports d'audit du fournisseur n'établissent jamais que votre configuration est correcte, et leur section la plus utile — les contrôles laissés à la charge du client — est celle que personne ne lit. Enfin, la rétention des journaux décide, le jour d'un incident, si vous pourrez conclure.

**Trois questions de vérification**

1. Votre configuration d'un service collaboratif n'a pas été modifiée depuis six mois. Pourquoi votre exposition a-t-elle pu changer, et comment le détectez-vous ?
2. Un collaborateur quitte l'entreprise. Son compte est désactivé et son mot de passe changé. Qu'est-ce qui reste potentiellement actif, et comment y met-on fin ?
3. Un fournisseur vous transmet son rapport d'audit tiers. Quelle section lisez-vous en priorité, et pourquoi celle-là ?

---

## Chapitre 32 — Systèmes contraints, legacy et sanctuarisation

### 32.1 Typologie et décision structurante

Tout parc comporte des systèmes qu'on ne peut ni corriger, ni migrer. Ce chapitre traite ce cas de front, parce qu'il est universel et rarement documenté.

| Type | Cause | Espoir de résolution |
|---|---|---|
| Éditeur disparu | Faillite, rachat, abandon | Nul |
| Matériel spécifique indissociable | Le logiciel pilote un équipement unique | Nul sans remplacement de l'équipement |
| Application interne non reconstructible | Équipe dissoute, chaîne de construction perdue (§26.13) | Faible |
| Certification métier figée | Toute modification invalide une qualification | Long, réglementaire |
| Coût de migration disproportionné | Remplacement supérieur à la valeur de l'usage | Budgétaire |
| Dépendance externe bloquante | Partenaire ou client imposant une version | Contractuel |

**La décision structurante**, à prendre explicitement pour chaque cas, et à réexaminer périodiquement :

```
REMPLACER   → migration ou reconstruction, avec budget et échéance
ISOLER      → sanctuarisation, avec compensations permanentes
ASSUMER     → maintien en l'état, risque accepté et documenté
```

⚠️ **PIÈGE — la non-décision**
Le cas le plus fréquent n'est aucune de ces trois options : c'est l'absence de décision. Le système reste en service, sans compensation particulière, sans dérogation, sans plan — parce que personne n'a été mis en position de trancher. C'est le §17.10 appliqué à un actif entier.

### 32.2 Sanctuariser : ce que cela signifie réellement

Sanctuariser, c'est réduire un système à un périmètre d'usage minimal, strictement contrôlé.

**Les six dimensions à traiter**, aucune ne suffisant seule :

| Dimension | Mesure |
|---|---|
| **Réseau** | Flux réduits au strict nécessaire, dans les deux sens, avec liste explicite |
| **Accès humain** | Comptes nominatifs, nombre minimal, authentification renforcée |
| **Supports amovibles** | Interdits ou strictement contrôlés (§29.5) |
| **Données** | Ce qui entre, ce qui sort, sous quel format, avec quelle vérification |
| **Surveillance** | Toute connexion et toute modification alertent |
| **Maintenance** | Procédure écrite, intervenants identifiés, traçabilité |

**Ce qui fuit toujours**, et qu'il faut anticiper : les interventions de maintenance, les échanges de fichiers, les comptes de service utilisés par d'autres systèmes, les sauvegardes, et les supports de restauration. Une sanctuarisation qui ne traite pas ces cinq points est une sanctuarisation de façade.

### 32.3 La rupture physique

L'isolement physique complet est souvent invoqué et rarement réel.

| Mythe | Réalité |
|---|---|
| « Le système est isolé, il n'y a aucun risque » | Les transferts de fichiers et les interventions restent des vecteurs |
| « Rien n'entre ni ne sort » | Il faut bien exporter les données de production et importer les mises à jour |
| « L'isolement dispense de maintenir » | Un système isolé mais compromis reste compromis, et la détection y est plus faible |
| « C'est irréversible » | Une connexion temporaire est ajoutée un jour, pour un besoin ponctuel, et reste |

**Ce qui rend l'isolement réel** : une procédure de transfert écrite et appliquée (§29.5), un contrôle périodique de l'absence de connexion, et l'interdiction documentée d'ajouter une liaison sans processus formel.

### 32.4 Systèmes sous certification métier

Cas particulier fréquent dans la santé, l'industrie réglementée, l'aéronautique, la sûreté : toute modification du système invalide une qualification obtenue au prix d'un processus long et coûteux.

**Ce qu'il faut établir, et qui est souvent supposé à tort :**

1. La qualification porte-t-elle réellement sur la version du logiciel, ou sur la configuration du procédé ? Les deux cas existent, et la réponse change tout.
2. Existe-t-il une procédure de **requalification allégée** pour les correctifs de sécurité ? Beaucoup de référentiels sectoriels en prévoient une.
3. Le fournisseur propose-t-il des versions **pré-qualifiées** intégrant les correctifs de sécurité ?

⚠️ Beaucoup d'impossibilités invoquées au nom d'une certification n'ont jamais été vérifiées auprès de l'organisme concerné. Poser la question par écrit produit régulièrement une réponse plus favorable qu'attendu — et, dans le cas contraire, une justification écrite qui vaut mieux qu'une supposition.

### 32.5 Le plan de fin de vie

Sanctuariser sans plan de sortie revient à assumer indéfiniment. Un plan de fin de vie comporte cinq éléments :

| Élément | Contenu |
|---|---|
| Jalons | Étapes datées : étude, choix, migration, décommissionnement |
| Financement | Par exercice, avec la règle du lot suivant (§12.3) |
| Points de non-retour | Moments après lesquels le report devient impossible ou très coûteux |
| Déclencheurs de réexamen | Événements imposant de revoir la décision : exploitation observée, incident, évolution réglementaire |
| Conditions de sortie de la sanctuarisation | Ce qui met fin au régime d'exception |

### 32.6 ⚖️ La responsabilité de maintenir un système obsolète en connaissance de cause

Trois éléments sont regardés en cas d'incident ou de contrôle (§8.6) :

1. Le risque était-il **identifié** ? Un système obsolète non inventorié est une négligence ; un système obsolète documenté est une décision.
2. La décision a-t-elle été **prise au bon niveau** ? Une acceptation signée par un technicien n'engage pas l'organisation de la même façon qu'une décision de direction.
3. Des **mesures proportionnées** ont-elles été prises ? C'est le rôle des compensations du chapitre 20.

**La conclusion opérationnelle** : maintenir un système obsolète n'est pas fautif en soi. Le faire sans l'avoir identifié, décidé et compensé l'est. La dérogation formalisée du §7.4 n'est pas un exercice administratif — c'est ce qui distingue les deux situations.

### 32.7 🔴 FIL ROUGE — mai 2028 : le banc de test et le serveur sans chaîne de construction

Deux cas de systèmes contraints arrivent au comité MCS le même mois, et ils se traitent différemment — ce qui est l'essentiel de ce chapitre.

**Cas 1 — le banc de test de validation des pompes PX-40.**

Un poste unique, sous un système hors support depuis des années, pilotant un banc de mesure indispensable à la validation réglementaire des dispositifs médicaux. Le logiciel de pilotage n'existe pas sur une version plus récente ; son éditeur a cessé son activité en 2019. Remplacer le banc complet est chiffré à environ 300 k€ et représente dix-huit mois, requalification comprise.

*Décision : **ISOLER**.* Sanctuarisation complète — retrait de tout réseau, transferts par support dédié selon la procédure du §29.5, deux comptes nominatifs, journal papier des interventions, contrôle trimestriel de l'absence de connexion. Coût total : environ 14 k€, essentiellement du matériel réseau et deux jours d'ingénierie.

*La dérogation* est signée par le directeur général, avec revue semestrielle et trois déclencheurs de réexamen : panne matérielle du poste, évolution de l'exigence réglementaire, ou disponibilité d'une solution de remplacement. Une provision est inscrite au plan pluriannuel pour le remplacement du banc à l'horizon 2031.

**Cas 2 — le serveur d'applications sans chaîne de construction.**

Application développée en interne en 2019, portée par un serveur d'applications hors support depuis 2024 (§26.13). L'équipe a été dissoute, le code source existe, mais aucune chaîne de construction fonctionnelle — personne ne sait produire un binaire à partir des sources.

*L'analyse d'usage change tout.* Avant de décider, Malik Ferhaoui mesure l'usage réel : l'application est consultée par **onze personnes**, environ deux fois par mois, pour accéder à des données historiques de 2015 à 2019.

*Décision : **REMPLACER**, mais pas comme prévu.* Plutôt que de reconstruire l'application — plusieurs mois de développement pour un usage marginal —, les données historiques sont exportées vers un espace de consultation en lecture seule sur l'infrastructure existante. Trois semaines de travail. L'application et son serveur sont **décommissionnés** en juillet, selon le processus du chapitre 35.

**Ce que la comparaison enseigne, et c'est le point du chapitre.** Deux systèmes contraints, deux décisions opposées, et dans les deux cas la décision correcte a été rendue possible par une information qui n'était pas technique : le coût de remplacement du banc, et **le nombre réel d'utilisateurs** de l'application. Aucune analyse de vulnérabilité n'aurait produit ces deux décisions.

**Ce que Claire Nadeau formule en comité** : *avant de se demander comment protéger un système qu'on ne peut pas corriger, il faut se demander à quoi il sert encore. La réponse rend parfois la question inutile — et cela ne coûte qu'une mesure d'usage.*

**Livrable de l'épisode.** Deux fiches de systèmes contraints : une sanctuarisation avec plan de fin de vie daté, un décommissionnement planifié.

→ La suite en 🔴 §33.13, avec la qualification réglementaire des produits HELIOMED.

→ **Chapitre 33 — MCS côté produit : PSIRT, divulgation coordonnée et obligations réglementaires** : le maintien d'un produit livré chez des clients.

### Synthèse mentale du chapitre 32

Tout parc comporte des systèmes qu'on ne peut ni corriger ni migrer, et trois décisions seulement existent : remplacer, isoler, assumer. Le cas le plus fréquent n'est aucune des trois, c'est l'absence de décision — le système reste en service sans compensation, sans dérogation et sans plan, parce que personne n'a été mis en position de trancher. Sanctuariser suppose de traiter six dimensions, et ce qui fuit toujours ce sont les interventions de maintenance, les échanges de fichiers, les comptes de service, les sauvegardes et les supports de restauration. Beaucoup d'impossibilités invoquées au nom d'une certification n'ont jamais été vérifiées auprès de l'organisme concerné : poser la question par écrit produit souvent une réponse plus favorable qu'attendu. Maintenir un système obsolète n'est pas fautif en soi ; le faire sans l'avoir identifié, décidé et compensé l'est. Enfin, avant de chercher comment protéger un système non corrigeable, mesurez son usage réel : la réponse rend parfois la question inutile, pour un coût dérisoire.

**Trois questions de vérification**

1. Un système ne peut être ni corrigé ni migré et reste en service depuis quatre ans. Quelle est la question qui n'a probablement jamais été posée, et à qui ?
2. Quelles cinq voies d'entrée subsistent malgré une sanctuarisation réseau apparemment complète ?
3. En quoi une dérogation formalisée change-t-elle la situation juridique d'une organisation maintenant un système obsolète ?

---

## Chapitre 33 — MCS côté produit : PSIRT, divulgation coordonnée et obligations réglementaires

> 🎓 **MODULE AVANCÉ — fabricants et éditeurs de produits numériques.**
> Ce chapitre ne concerne pas le maintien de votre système d'information, mais celui d'un **produit que vous mettez sur le marché** et qui s'exécute chez vos clients. Il n'est pas requis pour un parcours d'exploitation. Il est en revanche indispensable si votre organisation vend un logiciel, un équipement connecté, une application ou une appliance — et il le devient réglementairement.

### 33.1 Une différence de nature, pas de degré

| | Maintenir son SI | Maintenir un produit chez ses clients |
|---|---|---|
| Périmètre | Vos actifs | Toutes les versions déployées, chez tous les clients |
| Décision de corriger | Vous | Vous produisez le correctif, **le client décide de l'appliquer** |
| Délai | Le vôtre | Le vôtre **plus** celui d'adoption par le client |
| Visibilité | Vous voyez votre parc | Vous ne savez souvent pas qui utilise quelle version |
| Information | Vous recevez des avis | **Vous devez en publier** |
| Conséquence d'un défaut | Votre risque | Le risque de tous vos clients, simultanément |

**La conséquence structurante** : votre produit devient un composant du MCS de vos clients. Tout ce que ce cours leur enseigne à exiger de leurs fournisseurs (§13.6), ils vous le demanderont.

### 33.2 Construire un PSIRT

Un PSIRT — l'équipe qui traite la sécurité des produits — n'est pas nécessairement une équipe dédiée. Dans une organisation de taille intermédiaire, c'est un **rôle attribué** à deux ou trois personnes, avec un processus écrit.

**Les six fonctions à couvrir** :

| Fonction | Contenu |
|---|---|
| **Réception** | Point de contact unique, joignable, surveillé — y compris hors heures ouvrées |
| **Qualification** | Reproduire, évaluer l'impact, déterminer les versions affectées |
| **Coordination** | Faire corriger par les équipes de développement, arbitrer les priorités |
| **Publication** | Rédiger et diffuser l'avis de sécurité |
| **Notification** | Informer clients et autorités selon les obligations applicables |
| **Suivi** | Mesurer l'adoption du correctif chez les clients |

**Les trois décisions à prendre au démarrage**, et à écrire :

1. **Qui décide** de publier un avis, et selon quels critères ?
2. **Quel délai** vous engagez-vous à tenir entre la réception d'un signalement et la première réponse ?
3. **Qui est joignable** un samedi d'août, et comment ?

⚠️ **PIÈGE — le point de contact qui n'existe pas**
Beaucoup d'organisations découvrent, au premier signalement, qu'un chercheur a tenté de les contacter pendant trois semaines via le formulaire commercial du site, sans réponse. Le signalement finit alors publié sans coordination. **La mesure élémentaire** : une adresse de contact sécurité publiée, surveillée, avec un accusé de réception automatique et un délai de réponse annoncé.

### 33.3 La politique de divulgation coordonnée

**Le principe** : organiser la relation avec les personnes qui découvrent des vulnérabilités dans votre produit, de façon à ce que la correction précède la publication.

**Ce qu'une politique publiée doit contenir** :

| Élément | Contenu |
|---|---|
| Point de contact | Adresse dédiée, et moyen de chiffrer si nécessaire |
| Périmètre | Quels produits, quelles versions, ce qui est hors périmètre |
| Engagements | Délai d'accusé de réception, de qualification, de correction |
| Délai de publication | Le temps que vous demandez avant divulgation publique |
| Engagement de non-poursuite | Pour les recherches menées de bonne foi dans le périmètre |
| Reconnaissance | Mention du chercheur dans l'avis, si souhaité |

**Le fichier de découverte automatique** — un fichier `security.txt` normalisé par la **RFC 9116**, placé sous `/.well-known/security.txt` — est le geste le moins coûteux et le plus efficace : il permet à un chercheur de trouver comment vous joindre en dix secondes. Il comporte au minimum un champ `Contact` et un champ `Expires` [S-19].

**Sur les délais** : un délai de 90 jours entre le signalement et la publication est l'usage le plus répandu. Le chercheur peut publier au-delà, que vous ayez corrigé ou non. Négocier une prolongation est possible **si vous communiquez** — le silence est ce qui déclenche les publications anticipées.

### 33.4 Attribuer des identifiants

Deux voies : devenir vous-même autorité d'attribution pour vos produits, ou passer par un tiers.

| | Devenir autorité | Passer par un tiers |
|---|---|---|
| Maîtrise du calendrier | Totale | Dépendante |
| Charge | Processus, formation, obligations de qualité | Faible |
| Crédibilité | Signal de maturité | Neutre |
| Pertinent si | Publication régulière d'avis | Quelques avis par an |

Dans les deux cas, l'important n'est pas l'identifiant mais **l'avis** : un identifiant sans avis exploitable ne sert à rien à vos clients.

### 33.5 ⚖️ ⏱ Les obligations de signalement

*Bloc périssable, vérifié le 30/07/2026.*

Le règlement européen sur la cyberrésilience impose aux fabricants de produits comportant des éléments numériques des obligations de signalement — **article 14 du règlement** — applicables **à compter du 11 septembre 2026**, soit, à la date de vérification de ce bloc, une échéance encore à venir.

**Deux déclencheurs seulement**, et il faut les connaître précisément car ils sont plus étroits qu'on ne le croit :
1. le fabricant **a connaissance** d'une vulnérabilité de son produit **activement exploitée** ;
2. un **incident grave** affecte la sécurité du produit.

Une vulnérabilité découverte et corrigée avant toute exploitation, un correctif de routine ou une mise à jour préventive **ne relèvent pas** de l'article 14.

| Échéance | Objet | Point de départ |
|---|---|---|
| **≤ 24 h** | Alerte précoce | Prise de connaissance |
| **≤ 72 h** | Notification, avec les éléments connus et les mesures correctives ou d'atténuation disponibles | Prise de connaissance |
| **≤ 14 jours** | Rapport final, pour une **vulnérabilité activement exploitée** | **La mise à disposition d'une mesure corrective ou d'atténuation** |
| **≤ 1 mois** | Rapport final, pour un **incident grave** affectant la sécurité du produit | La notification initiale |

Le signalement s'effectue simultanément auprès de l'ENISA et du CSIRT désigné coordinateur, via la **plateforme unique de déclaration prévue à l'article 16**.

**Une obligation complémentaire souvent manquée** : l'article 14 impose également d'**informer les utilisateurs impactés** de la vulnérabilité ou de l'incident, et le cas échéant des mesures d'atténuation qu'ils peuvent déployer — de préférence dans un format structuré lisible par machine. C'est ce qui relie l'article 14 aux avis de sécurité du §33.10.

⚠️ **Ce que l'article 14 n'impose pas au 11 septembre 2026** : ni la publication d'une politique de divulgation coordonnée, ni la tenue d'un inventaire de composants, ni un processus complet de gestion des vulnérabilités. Ces exigences relèvent de l'**article 13**, applicable au 11 décembre 2027. Confondre les deux conduit à sur-dimensionner l'échéance de 2026 — ou, plus grave, à croire que l'article 14 se prépare seul.

📎 **Sources** — [S-04], [S-05], [S-06].

### 33.6 ⏱ Ce que ces délais exigent réellement en amont

C'est le point le plus important de ce chapitre, et le plus sous-estimé : **un délai de 24 heures n'est pas une obligation de formulaire, c'est une exigence de capacité organisationnelle.**

**Ce qu'il faut avoir construit avant** :

| Capacité | Sans elle |
|---|---|
| **Détecter** qu'une vulnérabilité de votre produit est activement exploitée | Vous ne déclencherez jamais le compteur, et vous serez informé par un client ou par la presse |
| **Qualifier rapidement** le périmètre affecté : quelles versions, quels clients | Vous ne pourrez pas remplir la notification |
| **Décider sans chaîne d'approbation longue** | Vingt-quatre heures ne suffisent pas pour un circuit de validation classique |
| **Rédiger vite et correctement** | Modèles préparés à l'avance |
| **Joindre les bonnes personnes** un jour férié | Astreinte, suppléance, coordonnées à jour |

✅ **BONNE PRATIQUE (P0) — l'exercice à blanc**
Réalisez au moins une fois par an un exercice : *une vulnérabilité de notre produit est signalée comme activement exploitée, un vendredi à 18 h*. Mesurez le temps réel nécessaire pour identifier les versions affectées, joindre le décideur, et produire un projet de notification. Le résultat du premier exercice est presque toujours très supérieur à 24 heures — et c'est précisément pourquoi il faut le faire avant, pas pendant.

### 33.7 ⏱ Les autres obligations structurantes

| Obligation | Contenu | Ce qu'elle implique |
|---|---|---|
| **Période de support** | Fournir des correctifs de sécurité pendant une durée déterminée après la mise sur le marché | Politique de versions (§25.7), et un modèle économique qui la finance |
| **Gestion des vulnérabilités du produit** | Processus documenté de traitement, y compris des composants tiers | Les chapitres 14 à 18, appliqués au produit |
| **Inventaire des composants** | Documenter les composants du produit | Le §25.11, automatisé à la construction |
| **Documentation et conformité** | Documentation technique, évaluation, marquage | Processus de conformité produit |
| **Application générale** | Échéance du **11 décembre 2027** pour l'essentiel des exigences | Le calendrier de mise en conformité se construit maintenant |

### 33.8 ⚖️ La méthode de qualification du périmètre

**Le principe** : certains produits sont exclus parce qu'ils relèvent d'un autre régime européen qui leur est propre — notamment les dispositifs médicaux couverts par la réglementation applicable, et plusieurs autres secteurs réglementés.

⚠️ **L'exclusion ne s'analyse jamais par gamme commerciale. Elle s'analyse produit par produit.**

**La grille de questions à instruire pour chaque objet de votre offre :**

| # | Question | Pourquoi elle compte |
|---|---|---|
| 1 | Comment le produit est-il commercialisé et **mis à disposition sur le marché** ? | Détermine l'applicabilité de principe |
| 2 | **Qui est juridiquement le fabricant** ? | Marque blanche, fabrication pour compte de tiers, sous-traitance de développement changent la réponse |
| 3 | Le **service distant** associé est-il nécessaire au fonctionnement du produit, ou constitue-t-il un service autonome ? | C'est la question la plus délicate, et celle qui décide pour les plateformes en ligne associées à un équipement |
| 4 | Ces composants forment-ils **un seul produit ou plusieurs produits distincts** ? | Un ensemble commercial peut relever de plusieurs régimes |
| 5 | Une partie relève-t-elle d'un **autre règlement qui s'applique effectivement** ? | L'exclusion suppose que l'autre régime s'applique réellement, pas qu'il pourrait s'appliquer |
| 6 | La conclusion est-elle **documentée et datée** ? | Elle est opposable, et devra être justifiée |

⚠️ **Point d'attention majeur.** Une solution en ligne n'entre pas dans le champ au seul motif qu'elle est **vendue avec** un équipement. Son rôle fonctionnel doit être analysé : un service dont dépend le fonctionnement du produit ne se traite pas comme un service autonome commercialisé séparément.

### 33.9 ⚠️ Les erreurs de qualification les plus fréquentes

| Erreur | Conséquence |
|---|---|
| Raisonner par gamme commerciale | Un produit exclu masque plusieurs produits inclus |
| **Confondre exclusion et absence d'exigences** | Le régime alternatif — notamment médical — impose ses propres exigences de cybersécurité |
| Traiter uniformément les produits **déjà mis sur le marché** | Distinction fixée par l'**article 69** : le paragraphe 2 prévoit que les produits mis sur le marché avant le 11/12/2027 ne relèvent des exigences générales qu'en cas de **modification substantielle** postérieure à cette date ; le paragraphe 3 y **déroge explicitement pour l'article 14**, dont les obligations de signalement s'appliquent à l'ensemble des produits déjà sur le marché. Un produit livré en 2020 et jamais modifié depuis doit donc disposer d'une capacité de signalement sous 24 h dès septembre 2026 [S-05] |
| Considérer la qualification comme définitive | Un changement de produit, d'usage ou de texte la remet en cause |
| Faire porter l'analyse par la seule équipe technique | C'est une analyse juridique et réglementaire, à conduire conjointement |

### 33.10 Les avis de sécurité produit

**Ce qu'un avis exploitable contient** — et c'est exactement ce que vos clients attendent pour alimenter les chapitres 14 et 16 :

| Élément | Pourquoi |
|---|---|
| Identifiant | Dédoublonnage (§4.2) |
| **Versions affectées et versions corrigées, précisément** | Sans cela, le client ne peut rien corréler (§14.6) |
| Description de la vulnérabilité et de son impact | Qualification |
| **Vecteur d'accès et conditions d'exploitation** | L'information la plus déterminante (§14.10) |
| Gravité, avec son mode de calcul | Priorisation |
| Exploitation observée, le cas échéant | Déclenche l'urgence |
| Mesures d'atténuation en attendant la mise à jour | Permet de compenser (ch. 20) |
| Date de publication et historique des révisions | Traçabilité |

**Publier un avis lisible par machine** (§4.8) démultiplie l'utilité de tout ce qui précède : vos clients peuvent l'intégrer automatiquement.

⚠️ **La cohérence entre ce que vous publiez et ce que vous corrigez** est un point de vigilance : corriger silencieusement une vulnérabilité sans publier d'avis prive vos clients de l'information dont ils ont besoin pour prioriser leur mise à jour. C'est un choix qui se retourne systématiquement contre le fournisseur au premier incident.

### 33.11 Maintenir les versions déployées chez les clients

| Sujet | Question |
|---|---|
| Matrice de support | Quelles versions recevront ce correctif ? |
| Rétroportage | Corrigez-vous les versions antérieures, et lesquelles (§25.5) ? |
| Mécanisme de mise à jour | Est-il sûr, atomique, réversible (§6.11) ? |
| Adoption | **Savez-vous combien de clients ont appliqué le correctif ?** |
| Clients refusant la mise à jour | Que faites-vous, et qu'avez-vous tracé ? |

**La question de l'adoption est celle que la plupart des éditeurs ne savent pas traiter.** Publier un correctif ne réduit le risque de personne tant qu'il n'est pas appliqué. Deux leviers : mesurer l'adoption quand le produit le permet, et **communiquer directement** aux clients concernés plutôt que de se contenter d'une publication passive.

**Le client qui refuse** relève du même raisonnement que le §32.6 : la trace écrite de votre notification, et de son refus, détermine la répartition des responsabilités le jour de l'incident.

### 33.12 📌 Limites

- **Marque blanche et fabrication pour compte de tiers** : qui publie l'avis, qui notifie ? À régler contractuellement, avant l'incident.
- **Composants intégrés fournis par des tiers** : vous dépendez de leur délai de correction, et vos clients dépendent du vôtre.
- **Sous-traitance de développement** : la responsabilité reste au fabricant, quel que soit l'auteur du code.
- **Produits anciens encore déployés** : la période de support engagée doit être tenue même si le produit n'est plus commercialisé.

### 33.13 🔴 FIL ROUGE — juin 2028 : la qualification produit par produit

Vingt et un mois après la mise en service du dispositif minimal de septembre 2026 (§8.10), HELIOMED conduit sa **revue de maturité produit**. Yann Prigent et le docteur Hélène Fabre reprennent la qualification réglementaire des quatre produits, cette fois avec un appui juridique externe et le temps de l'argumenter. Deux semaines de travail, une note de neuf pages.

**Ce que la revue confirme** : la qualification prudente de 2026 était correcte sur les trois cas tranchés. **Ce qu'elle corrige** : le statut d'HelioLink, traité par défaut comme inclus, méritait une analyse distinguant ses deux modes de commercialisation. **Ce qu'elle révèle** : le dispositif de 2026 n'aurait pas tenu un délai de 24 heures — c'est l'objet de l'exercice à blanc ci-dessous.

> ⚠️ **Les conclusions ci-dessous découlent des caractéristiques fictives décrites dans ce cas.** Elles illustrent une **méthode d'analyse**, non un résultat transposable : chaque produit réel doit faire l'objet de sa propre qualification.

**Les quatre produits, et leur traitement.**

| Produit | Description retenue dans le cas | Conclusion | Motif |
|---|---|---|---|
| **PX-40** — pompe à perfusion | Dispositif médical au sens de la réglementation applicable, marqué à ce titre | **Exclu du règlement cyberrésilience** | Le régime médical s'applique effectivement — question 5 de la grille |
| **HelioBox** — passerelle hospitalière | Équipement connecté générique, commercialisé séparément, non revendiqué comme dispositif médical | **Dans le périmètre** | Produit avec éléments numériques mis sur le marché — questions 1 et 4 |
| **HelioMove** — application mobile de bien-être | Application grand public, sans revendication médicale | **Dans le périmètre** | Logiciel mis sur le marché |
| **HelioLink** — plateforme de télésuivi | **Statut ouvert** | **À trancher** | Question 3 : le service est-il autonome, ou nécessaire au fonctionnement de HelioBox ? |

**Le cas HelioLink occupe l'essentiel de l'analyse.** La plateforme est commercialisée sous deux formes : un abonnement autonome souscrit par des établissements de santé, et une offre couplée où HelioBox ne fonctionne qu'avec elle. Selon la forme, le raisonnement diffère. La note conclut en distinguant explicitement les deux cas d'usage et retient l'hypothèse la plus contraignante pour la conception du dispositif — décision de prudence assumée et documentée.

**Ce que la qualification déclenche concrètement.**

1. **PSIRT** : le rôle minimal de 2026 est structuré — deux suppléants au lieu d'un, politique de divulgation coordonnée publiée avec un délai de 90 jours, fichier de découverte automatique conforme à la spécification en vigueur ajouté sur les sites.
2. **Capacité de notification** : modèles de notification préparés, chaîne de décision pré-autorisée — Yann peut déclencher une notification sans validation préalable de la direction générale, avec information immédiate.
3. **Exercice à blanc** : réalisé en juillet. Résultat du premier essai : **31 heures** pour produire un projet de notification exploitable, contre 24 exigées. Les deux points de blocage identifiés sont l'inventaire des versions déployées chez les clients, et la joignabilité du responsable juridique un dimanche. Corrigés en septembre ; le second exercice descend à 9 heures.
4. **Inventaire des versions déployées** : c'était le trou principal. HELIOMED ne savait pas quelle version de HelioBox tournait chez quel client. Un mécanisme de remontée de version est ajouté au produit — avec l'accord des clients, et avec une analyse d'impact sur les données personnelles conduite par Léa Cassin.
5. **Inventaire des composants** : généré automatiquement à la construction pour HelioLink et HelioBox (§25.11), conservé par version publiée.

**Le point le plus révélateur.** L'exercice à blanc montre que l'obstacle n'était ni juridique, ni technique : c'était l'**absence d'inventaire des versions déployées chez les clients**. HELIOMED savait maintenir son propre parc depuis deux ans ; elle ne savait pas ce qui tournait chez les siens.

**Ce que Yann Prigent écrit en conclusion de la note** : *nous avons appliqué à nos clients ce que nous reprochions à nos fournisseurs.*

→ La suite en 🔴 §34.12, quand la console de sauvegarde révélera son propre retard.

→ **Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes** : les outils de sécurité eux-mêmes, souvent les plus en retard.

### Synthèse mentale du chapitre 33

Maintenir un produit chez ses clients diffère en nature du maintien de son SI : vous produisez le correctif, le client décide de l'appliquer, et vous ignorez souvent quelle version tourne chez qui. Un PSIRT n'est pas nécessairement une équipe mais un rôle attribué couvrant six fonctions, dont la première — un point de contact réellement surveillé — manque à la plupart des organisations au moment du premier signalement. Les délais de notification réglementaires ne sont pas une obligation de formulaire mais une exigence de capacité organisationnelle : détecter l'exploitation, qualifier le périmètre, décider sans circuit long, et joindre les bonnes personnes un jour férié. L'exclusion du champ réglementaire s'analyse produit par produit, jamais par gamme, et exclusion ne signifie pas absence d'exigences. Enfin, publier un correctif ne réduit le risque de personne tant qu'il n'est pas appliqué : la mesure de l'adoption chez les clients est le sujet que la plupart des éditeurs ne traitent pas.

**Trois questions de vérification**

1. Une vulnérabilité de votre produit est signalée comme activement exploitée un vendredi à 18 h. Listez les cinq capacités que vous devez déjà posséder pour tenir un délai de 24 heures.
2. Votre gamme comprend un dispositif réglementé, un équipement générique et une application mobile. Pourquoi ne pouvez-vous pas conclure d'un seul examen, et quelles questions instruisez-vous pour chaque objet ?
3. Vous publiez un correctif de sécurité pour votre produit. Pourquoi le risque n'a-t-il pas encore diminué, et que faites-vous ?

---

## Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes

### 34.1 Pourquoi les outils de sécurité sont les plus en retard

Le constat est régulier, et contre-intuitif : les outils censés protéger le système d'information figurent souvent parmi ses composants les moins maintenus.

**Les cinq mécanismes qui produisent ce retard**, tous parfaitement rationnels pris isolément :

| Mécanisme | Raisonnement implicite |
|---|---|
| « C'est un outil de sécurité, donc il est sécurisé » | Aucun lien logique, mais le raisonnement est répandu |
| Mettre à jour interrompt la protection | Pendant la mise à jour, la surveillance est dégradée — argument réel |
| L'outil est utilisé quotidiennement par l'équipe | L'interrompre gêne ceux qui décident de l'interrompre |
| Aucun métier ne le réclame | Il ne figure sur aucune feuille de route |
| Il n'est pas exposé à Internet | Confusion entre exposition et criticité (§11.7) |

**Le rappel qui tranche** : ces outils sont des **actifs de niveau 0**. La console de sauvegarde accède à toutes les données, l'outil de déploiement exécute du code partout, le scanner détient les identifiants privilégiés du parc (§15.3), le coffre-fort concentre les accès. Leur compromission n'est pas un incident de sécurité parmi d'autres : c'est la fin de la partie.

### 34.2 Deux objets distincts : le logiciel et le contenu

C'est la distinction structurante du chapitre, et elle est presque toujours confondue.

| | Le logiciel | Le contenu |
|---|---|---|
| De quoi s'agit-il | Console, agents, serveurs | Signatures, règles, modèles, listes |
| Rythme de mise à jour | Mensuel à trimestriel | **Quotidien, parfois horaire** |
| Ce qui se dégrade | Vulnérabilités, fin de support | **Pertinence de la détection** |
| Comment on le mesure | Version installée | **Date du dernier contenu appliqué** |
| Qui s'en occupe | Exploitation | Souvent personne explicitement |

**Une console à jour dont les règles datent de trois mois dégrade fortement la couverture des menaces récentes.** Et symétriquement, un contenu parfaitement à jour sur un logiciel hors support s'exécute sur une base vulnérable. Les deux doivent être suivis séparément.

### 34.3 Maintenir le contenu de détection

**Les dix objets à suivre**, avec leur cadence propre :

| Objet | Cadence attendue | Indicateur |
|---|---|---|
| Signatures et moteur antimalware | Quotidienne | Âge du dernier contenu, par machine |
| Politiques de protection des postes | Mensuelle | Date de dernière revue |
| Règles de détection et de corrélation | Continue | Nombre de règles, date de dernière modification |
| Règles de filtrage applicatif | Continue | Couverture, faux positifs |
| Signatures de sonde réseau | Quotidienne à hebdomadaire | Âge du contenu |
| Listes de blocage et flux de réputation | Quotidienne | Fraîcheur, taux d'erreur |
| Base de détection du scanner | Quotidienne | Âge (§15.5) |
| Analyseurs de journaux | À chaque changement de format source | Taux d'événements non analysés |
| Connecteurs d'orchestration | À chaque évolution d'API | Taux d'échec |
| Certificats de confiance de la chaîne d'outillage | Selon expiration | Inventaire (§24.6) |

**Les deux lignes les plus négligées** sont les analyseurs de journaux et les connecteurs. Un changement de format de journal côté source casse silencieusement l'analyse : les événements arrivent, ne sont plus interprétés, et disparaissent des règles de détection. Le tableau de bord reste vert.

✅ **BONNE PRATIQUE (P0)** — Suivez le **taux d'événements non analysés** par source. Une hausse soudaine signale un changement de format, donc une perte de détection invisible à tous les autres indicateurs.

### 34.4 Le cycle de vie des exclusions

**Le mécanisme.** Une application métier déclenche des faux positifs ; on ajoute une exclusion pour débloquer la production. L'exclusion est légitime. Elle n'est jamais revue.

**Ce que produit l'accumulation**, après quelques années : des répertoires entiers exclus de l'analyse, parfois des extensions de fichiers, parfois des processus complets. Un attaquant qui découvre ces exclusions dispose d'un espace où déposer et exécuter ce qu'il veut sans être détecté.

**Le traitement**, identique à celui des dérogations (§7.4) :

| Exigence | Contenu |
|---|---|
| Inventaire | Liste complète des exclusions, tous outils confondus |
| Justification | Pourquoi, pour quelle application, sur demande de qui |
| Portée minimale | Un processus précis plutôt qu'un répertoire entier |
| Date d'expiration | Et revue à échéance |
| Compensation | Surveillance spécifique de la zone exclue |

⚠️ Une exclusion **large et permanente** sur un répertoire accessible en écriture par des comptes ordinaires est l'une des configurations les plus dangereuses qu'on rencontre en audit.

### 34.5 Vérifier que la protection fonctionne encore

Un agent installé n'est pas un agent qui fonctionne. Cinq états à distinguer, qui se ressemblent tous dans un tableau de bord mal conçu :

| État | Signification |
|---|---|
| Actif et à jour | Situation nominale |
| Actif, contenu ancien | Protection dégradée |
| Installé, service arrêté | **Aucune protection** |
| Installé, ne communique plus avec la console | Aucune visibilité — et souvent aucune protection |
| Non installé | Absent des indicateurs de l'outil |

**Le dernier état est le plus dangereux** : une machine sans agent n'apparaît pas dans la console, donc pas dans le taux de conformité. C'est très exactement le problème du dénominateur (§10.11), appliqué aux outils de sécurité. La couverture se calcule **sur le périmètre de référence**, jamais sur ce que l'outil connaît.

✅ **BONNE PRATIQUE (P1)** — Réalisez périodiquement un **test de fonctionnement contrôlé** : déposer sur un échantillon de machines un fichier de test standard prévu à cet effet, et vérifier que la détection remonte bien jusqu'à la console. Cela vérifie la chaîne complète — agent, communication, console, alerte — et non la seule présence du logiciel.

### 34.6 Sauvegardes : maintenir l'infrastructure qui vous sauvera

L'infrastructure de sauvegarde est simultanément le dernier recours et une cible privilégiée.

| Objet | Point d'attention |
|---|---|
| Console de sauvegarde | Actif de niveau 0 : accès à toutes les données. Jamais joignable depuis le réseau bureautique |
| Agents de sauvegarde | Présents sur toutes les machines, souvent privilégiés, rarement mis à jour |
| Support de stockage | Immuabilité : une sauvegarde modifiable par un attaquant n'est pas une sauvegarde |
| Comptes de service | Droits étendus par nature, mots de passe souvent anciens (§24.2) |
| Copies hors ligne | Le seul recours contre une compromission de l'infrastructure elle-même |

⚠️ **PIÈGE — la sauvegarde restaurée qui réintroduit la vulnérabilité**
Une restauration ramène le système à son état d'origine, correctifs compris — c'est-à-dire non compris. C'est l'une des cinq causes de récurrence du §17.9. **Tout retour à un état antérieur déclenche un contrôle de conformité** avant remise en service.

**Le test de restauration** est à la sauvegarde ce que le test de retour arrière est au correctif (§18.8) : sans lui, vous avez une intention, pas une capacité. Il se planifie, se chronomètre, et son résultat se documente.

### 34.7 Articulation avec la continuité d'activité

| Ce que la sauvegarde compense | Ce qu'elle ne compense pas |
|---|---|
| Perte de données | La compromission elle-même : restaurer un système compromis le restaure compromis |
| Destruction d'un système | Le temps de reconstruction, souvent très supérieur aux attentes |
| Erreur humaine | La fuite de données : une donnée exfiltrée reste exfiltrée |
| Défaillance matérielle | Une vulnérabilité présente dans la sauvegarde |

**La conclusion pour le MCS** : la sauvegarde n'est pas une alternative au maintien en condition de sécurité. Une organisation qui néglige le MCS en comptant sur ses sauvegardes découvre, le jour de l'incident, qu'elle restaure des systèmes vulnérables dans un environnement où l'attaquant est peut-être encore présent.

### 34.8 Remédiation après compromission : corriger ou reconstruire

C'est la question centrale d'un retour à un état de confiance, et elle a été rencontrée deux fois dans le fil rouge (§21.11).

| Situation | Décision |
|---|---|
| Vulnérabilité corrigée avant toute exploitation | Correction suffisante |
| Exploitation possible, aucune preuve de compromission, journalisation suffisante | Correction + recherche approfondie |
| Exploitation possible, **journalisation insuffisante** | **Reconstruction**, sauf si un état de confiance peut être démontré autrement |
| Compromission avérée | Reconstruction, après préservation des éléments d'enquête |
| Équipement de bordure ayant subi une exploitation | Reconstruction — la persistance y est fréquente et difficile à détecter |

**L'ordre des opérations** en cas de compromission avérée : préserver les traces avant toute action ; comprendre le périmètre avant de reconstruire ; reconstruire à partir d'une source de confiance, pas d'une sauvegarde postérieure à la compromission ; changer les secrets susceptibles d'avoir été exposés ; et rétablir la surveillance avant la remise en service.

⚠️ **Le conflit à connaître à l'avance** : corriger vite peut détruire les preuves. Sur un équipement suspecté compromis, la décision de préserver ou de corriger doit être prise consciemment, par le pilote de crise (§21.7), et non subie par réflexe.

### 34.9 Le MCS pendant une crise majeure

Pendant un incident majeur, le MCS courant doit être suspendu et repriorisé, sinon il consomme des ressources indispensables ailleurs.

| Décision | Contenu |
|---|---|
| **Gel du MCS courant** | Les campagnes en cours sont suspendues, sauf celles qui traitent le vecteur de l'incident |
| **Priorité au vecteur** | Le chemin d'entrée est corrigé partout, en priorité absolue |
| **Reconstruction propre** | Les systèmes reconstruits le sont à un niveau de correctif à jour, pas à l'état antérieur |
| **Reprise progressive** | Le MCS courant reprend après stabilisation, avec un rattrapage planifié |

**Le point de vigilance** : la reconstruction en urgence produit des configurations non conformes et des exceptions temporaires. Elles doivent être **inventoriées pendant la crise** — le journal de décision du §21.5 y sert — pour être traitées après, plutôt que découvertes deux ans plus tard comme le serveur d'impression du §23.7.

### 34.10 📌 Limites

- **La protection des postes ne remplace pas les correctifs** : elle détecte des comportements, elle ne supprime pas les vulnérabilités.
- **La détection dépend de la journalisation** : sans journaux, pas de règles, quel que soit l'outil.
- **Les outils de sécurité augmentent la surface** : agents privilégiés, consoles, connecteurs. Chaque outil ajouté est un actif de niveau 0 supplémentaire à maintenir.
- **Le contenu de détection ne couvre que le connu** : c'est utile, et insuffisant seul.

### 34.11 ✅ Recommandations priorisées

| Prio | Action |
|---|---|
| **P0** | Classer tous les outils de sécurité et plans de gestion en C1, avec fenêtre récurrente |
| **P0** | Retirer les consoles d'administration du réseau bureautique |
| **P0** | Suivre séparément la version du logiciel et l'âge du contenu de détection |
| **P0** | Calculer la couverture des agents sur le **périmètre de référence**, pas sur la console |
| P1 | Inventorier et borner les exclusions, avec compensation |
| P1 | Test de fonctionnement contrôlé périodique |
| P1 | Contrôle de conformité systématique après toute restauration |
| P1 | Test de restauration chronométré et documenté |
| P2 | Suivi du taux d'événements non analysés par source |

### 34.12 🔴 FIL ROUGE — juillet 2028 : la console de sauvegarde

La revue des outils de sécurité et des plans de gestion d'HELIOMED, conduite en juillet, produit le tableau suivant.

| Outil | Version | Retard | Exposition |
|---|---|---|---|
| Console de sauvegarde | N-4 | **14 mois** | Joignable depuis l'ensemble du réseau bureautique |
| Console de protection des postes | N-1 | 3 mois | Réseau d'administration |
| Outil de scan | N-2 | 7 mois | Réseau d'administration |
| Plateforme de journalisation | N-1 | 4 mois | Réseau d'administration |
| Console de virtualisation | N-3 | 11 mois | Réseau d'administration |

**Le cas de la console de sauvegarde.** Quatorze mois de retard, deux vulnérabilités critiques publiées sur cette version dont une figurant au catalogue d'exploitation avérée, et un accès depuis n'importe quel poste du siège. La console dispose d'un accès en lecture à l'intégralité des données sauvegardées — c'est-à-dire à tout.

**Pourquoi elle n'avait jamais été traitée**, et l'analyse est instructive : elle n'était pas exposée à Internet, donc n'apparaissait dans aucune priorisation fondée sur l'exposition externe ; sa mise à jour interrompt les sauvegardes, donc nécessitait une fenêtre que personne n'avait demandée ; et elle appartenait à l'équipe exploitation, qui la considérait comme son outil de travail plutôt que comme un actif à maintenir. Les trois mécanismes du §34.1, simultanément.

**Les décisions.**

*Immédiat, en deux jours* : la console est retirée du réseau bureautique et placée sur le réseau d'administration, accessible uniquement depuis les postes d'administration dédiés (§28.4). Cette seule mesure supprime le chemin d'attaque principal, sans aucune interruption de sauvegarde.

*Sous trois semaines* : mise à jour des cinq outils, par ordre de criticité, avec fenêtres dédiées. La console de sauvegarde d'abord.

*Structurel* : les cinq outils entrent en classe C1 avec fenêtre récurrente mensuelle. Un indicateur dédié — **âge de version des outils de sécurité et plans de gestion** — entre au tableau de bord du comité MCS.

**La découverte annexe.** L'inventaire des exclusions de la protection des postes remonte **37 exclusions**, dont 9 portant sur des répertoires complets, et 4 sans aucune justification documentée. L'une d'elles, ajoutée en 2022, exclut un répertoire de dépôt de fichiers accessible en écriture par tous les utilisateurs du siège. Elle est supprimée le jour même ; les 8 autres exclusions larges sont réduites à des processus précis en trois semaines.

**Le test de fonctionnement**, réalisé pour la première fois sur un échantillon de 30 postes : 27 détections remontées à la console, **3 machines sans réaction**. Analyse : deux agents dont le service était arrêté depuis plusieurs mois, un agent ne communiquant plus avec la console depuis un changement de configuration réseau en 2027. Aucune de ces trois machines n'apparaissait comme non conforme — elles n'apparaissaient simplement plus du tout.

**Ce que Claire Nadeau écrit au comité.** *Nous avons passé deux ans et demi à réduire notre exposition. Le chemin le plus direct vers l'ensemble de nos données passait par l'outil chargé de les protéger, et il était ouvert depuis le premier jour.*

→ **Fin de la Partie V.** La suite en 🔴 §35.14, avec le décommissionnement des systèmes que ces deux années ont rendus inutiles.

→ **Chapitre 35 — Décommissionnement sécurisé** : retirer proprement ce qui ne sert plus.

### Synthèse mentale du chapitre 34

Les outils de sécurité figurent régulièrement parmi les composants les moins maintenus, pour cinq raisons rationnelles prises isolément — dont la confusion entre exposition externe et criticité. Ce sont pourtant des actifs de niveau 0 : leur compromission n'est pas un incident parmi d'autres. Deux objets distincts doivent être suivis séparément, le logiciel et le contenu : une console à jour dont les règles datent de trois mois ne détecte rien de récent. Les exclusions s'accumulent sans jamais être revues et créent des zones où un attaquant peut opérer sans être vu ; elles se traitent comme des dérogations, avec portée minimale et date d'expiration. Une machine sans agent n'apparaît pas dans la console, donc pas dans le taux de conformité : la couverture se calcule sur le périmètre de référence. Enfin, la sauvegarde n'est pas une alternative au MCS — restaurer un système compromis le restaure compromis, et restaurer un système vulnérable réintroduit la vulnérabilité.

**Trois questions de vérification**

1. Votre console de protection des postes affiche 99 % de conformité. Quelles deux populations ce chiffre ignore-t-il structurellement, et comment les retrouvez-vous ?
2. Pourquoi une exclusion antimalware large et permanente est-elle plus dangereuse qu'une vulnérabilité critique non corrigée sur le même serveur ?
3. Un équipement de bordure a pu être exploité, mais vos journaux ne remontent que 30 jours. Corrigez-vous ou reconstruisez-vous, et sur quel critère tranchez-vous ?

---

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> - **aborder** un environnement industriel sans réflexes bureautiques, et construire une chaîne de mise à jour hors ligne gouvernée ;
> - **piloter** l'anticipation plutôt que la correction sur les services managés, et placer leurs versions au référentiel d'obsolescence ;
> - **traiter** un service en ligne par sa configuration, ses intégrations et ses autorisations déléguées, faute de pouvoir le corriger ;
> - **trancher** entre remplacer, isoler et assumer sur un système contraint — après avoir mesuré son usage réel ;
> - **construire** une capacité de signalement produit, et qualifier un périmètre réglementaire produit par produit ;
> - **maintenir** les outils de sécurité eux-mêmes, en distinguant le logiciel du contenu de détection.
>
> **Ce que vous ne savez pas encore** : comment faire tenir tout cela dans la durée. C'est l'objet de la Partie VI.
