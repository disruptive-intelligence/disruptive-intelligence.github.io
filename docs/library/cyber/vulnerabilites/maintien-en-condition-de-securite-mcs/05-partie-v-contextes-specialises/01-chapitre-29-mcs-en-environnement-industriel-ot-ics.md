---
title: Chapitre 29 — MCS en environnement industriel (OT / ICS)
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE V — Contextes spécialisés
  - index.md
---

## 29.1 Ce qui change fondamentalement

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

## 29.2 Le cadre normatif appliqué au maintien

La série de normes de sécurité des systèmes d'automatisation industriels fournit une structure directement utilisable, indépendamment de toute certification.

| Concept | Définition | Usage en MCS |
|---|---|---|
| **Zone** | Ensemble d'actifs partageant les mêmes exigences de sécurité | Détermine le périmètre d'une compensation |
| **Conduit** | Chemin de communication entre zones | C'est là que se placent les mesures de filtrage (§20.2) |
| **Niveau de sécurité** | Niveau de résistance attendu d'une zone | Calibre l'effort |
| **Répartition des rôles** | Exploitant / intégrateur / fabricant | Détermine **qui doit corriger** |

**L'apport principal pour le MCS** : la répartition des responsabilités. Beaucoup de blocages industriels viennent de ce que personne n'a établi qui, de l'exploitant, de l'intégrateur ou du fabricant, doit produire, valider et appliquer un correctif. Poser la question dans ces termes débloque plus de situations qu'une discussion technique.

## 29.3 L'inventaire industriel

Le chapitre 10 s'applique, avec des méthodes différentes.

| Méthode | Applicabilité | Précaution |
|---|---|---|
| **Écoute passive du trafic** | Méthode par défaut | Aucun risque pour le procédé ; nécessite un point de capture |
| **Extraction depuis les outils d'ingénierie** | Très riche : versions d'automates, programmes, configurations | Nécessite l'accès et la coopération de l'équipe automatisme |
| **Inventaire manuel** | Toujours possible | Chronophage, mais souvent le plus fiable sur les équipements anciens |
| **Documentation d'installation** | Fournie par l'intégrateur | Souvent périmée, mais c'est un point de départ |
| Scan actif | **Passif par défaut, actif sous procédure** | Validation explicite, test préalable, procédure d'arrêt, de préférence hors production (§3.7) |

✅ **BONNE PRATIQUE (P0)** — Commencez par l'inventaire manuel réalisé **avec** l'équipe de maintenance, pas par un outil. Deux journées passées avec le responsable automatisme produisent un inventaire plus fiable et plus utile qu'un mois d'outillage — et elles construisent la relation sans laquelle rien ne se fera ensuite.

## 29.4 Les correctifs industriels

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

## 29.5 La chaîne complète de mise à jour hors ligne

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

## 29.6 La maintenance à distance des fournisseurs

Beaucoup d'installations industrielles disposent d'un accès distant permanent pour le constructeur. C'est souvent le chemin d'entrée le plus direct vers la zone industrielle.

**Les cinq exigences** :

1. **Accès à la demande**, activé pour une intervention, désactivé après — jamais permanent.
2. **Authentification multifacteur** et compte nominatif, pas un compte partagé du constructeur.
3. **Traçabilité** : enregistrement des sessions, journal accessible de votre côté.
4. **Supervision** : l'intervention est accompagnée côté exploitant.
5. **Contractualisation** : ces règles figurent au contrat de maintenance (§13.3).

## 29.7 Compensations spécifiques à l'industriel

| Mesure | Applicabilité |
|---|---|
| **Segmentation par zones et conduits** | Mesure structurante n° 1 |
| Filtrage sur les conduits | Contrôle des protocoles autorisés entre zones |
| **Suppression des flux devenus inutiles** | Souvent le gain le plus rapide (§20.11) |
| Postes d'ingénierie durcis et dédiés | Vecteur d'entrée majeur |
| Contrôle des supports amovibles | Voir §29.5 |
| Surveillance passive du trafic industriel | Détecte les anomalies sans perturber |
| Diodes de données | Pour les flux strictement sortants |

## 29.8 ✅ Livrable — Le plan de MCS industriel pluriannuel

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

## 29.9 ⚠️ Les erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Scan actif sur réseau industriel sans validation | Défaut d'automate, arrêt de ligne, et perte durable de la confiance |
| Correctif appliqué hors validation constructeur | Perte de garantie, invalidation de qualification |
| Confondre sûreté et sécurité | Les systèmes de sûreté relèvent d'un régime propre, à ne jamais modifier sans processus dédié |
| Imposer les délais bureautiques | Rejet immédiat, et fin de la coopération |
| Traiter l'industriel comme un sous-ensemble de l'informatique | Erreur de posture : ce sont deux métiers |
| Négliger la relation humaine | Sans le responsable maintenance, aucun accès, aucune information, aucun résultat |

## 29.10 📌 Limites

- **Le temps long est irréductible.** Un cycle de validation constructeur ne se comprime pas ; il s'anticipe.
- **Certains équipements ne seront jamais corrigés.** Le fournisseur a disparu, ou le produit est hors support depuis dix ans. C'est le chapitre 32.
- **La visibilité restera partielle.** L'écoute passive ne voit que ce qui communique.
- **Le budget dépend de la production**, pas de la DSI. Les arbitrages se font dans un autre circuit, avec d'autres critères.

## 29.11 🔴 FIL ROUGE — février 2028 : le bilan de l'arrêt de novembre

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

## Synthèse mentale du chapitre 29

En industriel, la sûreté des personnes et la disponibilité priment, les équipements vivent quinze à vingt-cinq ans, les fenêtres sont annuelles et les correctifs doivent être validés par le constructeur : arriver avec des réflexes bureautiques garantit l'échec en trois semaines. La démarche n'est pas de corriger plus vite mais de maîtriser l'exposition, préparer très à l'avance, et appliquer pendant les arrêts — la compensation n'est pas un pis-aller, c'est le mode normal de traitement. L'inventaire commence par deux journées avec l'équipe de maintenance, pas par un outil : elles produisent plus d'information et construisent la relation sans laquelle rien ne se fera. La chaîne de mise à jour hors ligne en huit étapes, avec double contrôle, journal des transferts et supports dédiés, est le livrable technique central. Enfin, la réduction d'exposition réelle vient rarement des correctifs : elle vient de la suppression des flux inutiles, des accès distants permanents et de la maîtrise des supports.

**Trois questions de vérification**

1. Un responsable de production refuse toute intervention sur ses automates. Qu'avez-vous probablement mal formulé, et comment reprenez-vous la discussion ?
2. Décrivez les huit étapes de la chaîne de mise à jour hors ligne, et indiquez à quelles étapes le double contrôle s'applique.
3. En deux ans, vous n'avez appliqué que quatre correctifs sur votre parc industriel. Comment démontrez-vous à votre direction que le risque a néanmoins fortement diminué ?

---
