---
title: Chapitre 32 — Systèmes contraints, legacy et sanctuarisation
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE V — Contextes spécialisés
  - index.md
---

## 32.1 Typologie et décision structurante

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

## 32.2 Sanctuariser : ce que cela signifie réellement

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

## 32.3 La rupture physique

L'isolement physique complet est souvent invoqué et rarement réel.

| Mythe | Réalité |
|---|---|
| « Le système est isolé, il n'y a aucun risque » | Les transferts de fichiers et les interventions restent des vecteurs |
| « Rien n'entre ni ne sort » | Il faut bien exporter les données de production et importer les mises à jour |
| « L'isolement dispense de maintenir » | Un système isolé mais compromis reste compromis, et la détection y est plus faible |
| « C'est irréversible » | Une connexion temporaire est ajoutée un jour, pour un besoin ponctuel, et reste |

**Ce qui rend l'isolement réel** : une procédure de transfert écrite et appliquée (§29.5), un contrôle périodique de l'absence de connexion, et l'interdiction documentée d'ajouter une liaison sans processus formel.

## 32.4 Systèmes sous certification métier

Cas particulier fréquent dans la santé, l'industrie réglementée, l'aéronautique, la sûreté : toute modification du système invalide une qualification obtenue au prix d'un processus long et coûteux.

**Ce qu'il faut établir, et qui est souvent supposé à tort :**

1. La qualification porte-t-elle réellement sur la version du logiciel, ou sur la configuration du procédé ? Les deux cas existent, et la réponse change tout.
2. Existe-t-il une procédure de **requalification allégée** pour les correctifs de sécurité ? Beaucoup de référentiels sectoriels en prévoient une.
3. Le fournisseur propose-t-il des versions **pré-qualifiées** intégrant les correctifs de sécurité ?

⚠️ Beaucoup d'impossibilités invoquées au nom d'une certification n'ont jamais été vérifiées auprès de l'organisme concerné. Poser la question par écrit produit régulièrement une réponse plus favorable qu'attendu — et, dans le cas contraire, une justification écrite qui vaut mieux qu'une supposition.

## 32.5 Le plan de fin de vie

Sanctuariser sans plan de sortie revient à assumer indéfiniment. Un plan de fin de vie comporte cinq éléments :

| Élément | Contenu |
|---|---|
| Jalons | Étapes datées : étude, choix, migration, décommissionnement |
| Financement | Par exercice, avec la règle du lot suivant (§12.3) |
| Points de non-retour | Moments après lesquels le report devient impossible ou très coûteux |
| Déclencheurs de réexamen | Événements imposant de revoir la décision : exploitation observée, incident, évolution réglementaire |
| Conditions de sortie de la sanctuarisation | Ce qui met fin au régime d'exception |

## 32.6 ⚖️ La responsabilité de maintenir un système obsolète en connaissance de cause

Trois éléments sont regardés en cas d'incident ou de contrôle (§8.6) :

1. Le risque était-il **identifié** ? Un système obsolète non inventorié est une négligence ; un système obsolète documenté est une décision.
2. La décision a-t-elle été **prise au bon niveau** ? Une acceptation signée par un technicien n'engage pas l'organisation de la même façon qu'une décision de direction.
3. Des **mesures proportionnées** ont-elles été prises ? C'est le rôle des compensations du chapitre 20.

**La conclusion opérationnelle** : maintenir un système obsolète n'est pas fautif en soi. Le faire sans l'avoir identifié, décidé et compensé l'est. La dérogation formalisée du §7.4 n'est pas un exercice administratif — c'est ce qui distingue les deux situations.

## 32.7 🔴 FIL ROUGE — mai 2028

le banc de test et le serveur sans chaîne de construction

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

## Synthèse mentale du chapitre 32

Tout parc comporte des systèmes qu'on ne peut ni corriger ni migrer, et trois décisions seulement existent : remplacer, isoler, assumer. Le cas le plus fréquent n'est aucune des trois, c'est l'absence de décision — le système reste en service sans compensation, sans dérogation et sans plan, parce que personne n'a été mis en position de trancher. Sanctuariser suppose de traiter six dimensions, et ce qui fuit toujours ce sont les interventions de maintenance, les échanges de fichiers, les comptes de service, les sauvegardes et les supports de restauration. Beaucoup d'impossibilités invoquées au nom d'une certification n'ont jamais été vérifiées auprès de l'organisme concerné : poser la question par écrit produit souvent une réponse plus favorable qu'attendu. Maintenir un système obsolète n'est pas fautif en soi ; le faire sans l'avoir identifié, décidé et compensé l'est. Enfin, avant de chercher comment protéger un système non corrigeable, mesurez son usage réel : la réponse rend parfois la question inutile, pour un coût dérisoire.

**Trois questions de vérification**

1. Un système ne peut être ni corrigé ni migré et reste en service depuis quatre ans. Quelle est la question qui n'a probablement jamais été posée, et à qui ?
2. Quelles cinq voies d'entrée subsistent malgré une sanctuarisation réseau apparemment complète ?
3. En quoi une dérogation formalisée change-t-elle la situation juridique d'une organisation maintenant un système obsolète ?

---
