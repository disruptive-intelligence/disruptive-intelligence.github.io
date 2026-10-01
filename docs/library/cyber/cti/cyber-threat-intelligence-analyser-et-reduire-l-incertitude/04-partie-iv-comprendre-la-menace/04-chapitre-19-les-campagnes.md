---
title: Chapitre 19 — Les campagnes
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE IV — Comprendre la menace
  - index.md
---

## 19.1 Ce qu'est une campagne, et pourquoi la notion est utile

**Définition de travail** : une campagne est un **ensemble d'activités regroupées par l'analyste** parce qu'elles partagent suffisamment de caractéristiques pour être raisonnées ensemble.

Le mot important est *regroupées par l'analyste*. Une campagne n'est pas un objet du monde — c'est une **construction analytique**. L'adversaire ne se dit pas qu'il mène une campagne ; vous décidez que ces onze incidents forment un tout.

**Pourquoi la notion est utile malgré son caractère construit** :

| Apport | Mécanisme |
|---|---|
| **Elle permet de prévoir** | Ce qui a été fait chez les onze premiers indique ce qui sera fait ensuite |
| **Elle permet de prioriser** | Une vulnérabilité exploitée dans une campagne active n'est plus une vulnérabilité parmi d'autres |
| **Elle permet de partager** | C'est l'unité d'échange dans les dispositifs sectoriels |
| **Elle réduit le volume** | Onze signalements deviennent un dossier |

**C'est le niveau 2 de l'attribution** (§13.1) — le regroupement opérationnel. Il ne nécessite aucun nom d'acteur et c'est celui qui vous sert.

## 19.2 Les critères de regroupement, et leur solidité

Tous les critères ne se valent pas, et c'est ici que le chapitre 18 se rejoue.

| Critère | Solidité | Pourquoi |
|---|---|---|
| **Même vulnérabilité exploitée** | Moyenne | Beaucoup d'acteurs exploitent la même |
| **Même infrastructure** | Moyenne | Hébergement partagé, adresses réattribuées |
| **Même outillage** | Moyenne à faible | Les outils circulent (§13.3) |
| **Même séquence de comportements** | **Élevée** | Coûteuse à imiter, stable dans le temps |
| **Même erreur ou particularité** | **Élevée** | Un détail non fonctionnel est rarement copié |
| Même secteur visé | **Faible** | C'est souvent une conséquence, pas une cause |
| Même période | **Très faible** | Coïncidence fréquente (§4.2) |

**La règle** : un regroupement fondé sur un seul critère de solidité moyenne ou faible est une hypothèse, pas une campagne. Il faut au minimum **deux critères indépendants**, dont un de solidité élevée.

⚠️ **PIÈGE — le regroupement par secteur**
« Trois organisations du secteur médical » est le critère le plus employé et l'un des plus faibles. Il produit des campagnes fictives — et c'est exactement ce qui s'est passé au §7.9 du fil rouge, et ce que l'élément ③ du §8.9 a permis d'éviter.

## 19.3 Le cycle de vie d'une vulnérabilité exploitée

Comprendre ce cycle permet de savoir **où vous en êtes** quand une information vous parvient — et donc combien de temps il vous reste.

```
①  Découverte           par un chercheur, un éditeur, ou un attaquant
        ↓
②  Publication          avis, correctif disponible
        ↓  ← délai variable : heures à mois
③  Analyse publique     décomposition du correctif, compréhension du défaut
        ↓  ← délai souvent court
④  Code d'exploitation  publié, vendu, ou développé
        ↓
⑤  Exploitation ciblée  quelques cas, souvent invisibles
        ↓
⑥  Exploitation massive automatisée, opportuniste
        ↓
⑦  Persistance          la vulnérabilité reste exploitée des années
                        sur les systèmes non corrigés
```


**Les quatre observations qui comptent** :

| Observation | Conséquence |
|---|---|
| Le délai ②→⑥ est **très variable** — d'heures à jamais | Il dépend de l'automatisabilité et du déploiement (§16.3), pas de la gravité |
| L'étape ⑤ est **souvent invisible** | Quand vous apprenez qu'une vulnérabilité est exploitée, vous êtes déjà en ⑥ |
| L'étape ⑦ dure des années | Une vulnérabilité ancienne reste un vecteur majeur |
| Une information reçue à l'étape ③ vaut beaucoup plus qu'à l'étape ⑥ | C'est ce que le renseignement sectoriel peut apporter |

**La question à poser devant toute information de ce type** : *à quelle étape sommes-nous ?* La réponse détermine s'il vous reste des semaines ou des heures.

## 19.4 Ce qui fait passer une menace du général au « nous »

Quatre conditions, cumulatives. Tant qu'elles ne sont pas toutes vérifiées, la menace reste générale — et le §7.9 est né de l'oubli de ce point.

| # | Condition | Question | Si non vérifiée |
|---|---|---|---|
| **1** | **Applicabilité** | Le produit, la version, la configuration existent-ils chez nous ? | La menace ne nous concerne pas |
| **2** | **Accessibilité** | Le vecteur est-il ouvert chez nous ? | La menace nous concerne, sans être exploitable |
| **3** | **Absence de neutralisation** | Une mesure existante l'annule-t-elle ? | La menace est neutralisée — et c'est le cas de §12.7 |
| **4** | **Plausibilité du ciblage** | Sommes-nous dans le périmètre visé, ou disponibles ? *(§16.4)* | La probabilité est faible, pas nulle |

**Les conditions 1 à 3 se vérifient chez vous, pas dans le renseignement reçu.** C'est l'étape 4 du chapitre 2 — le passage de la connaissance au renseignement — et c'est ce qui distingue une fonction utile d'un relais de publications.

🎯 **ET MAINTENANT ?**
*Un dispositif sectoriel signale une campagne active exploitant une vulnérabilité que vous n'avez pas corrigée. Que vérifiez-vous, dans quel ordre, avant de mobiliser ?*
**Réponse** : les quatre conditions, dans l'ordre, et cela prend une heure. *La version affectée est-elle bien celle déployée ?* — dans une majorité de cas, la réponse resserre déjà le périmètre. *L'actif est-il accessible par le vecteur décrit ?* *Une mesure existante neutralise-t-elle l'exploitation — authentification, filtrage, configuration durcie ?* *Sommes-nous dans le périmètre décrit, ou simplement dans le même secteur ?* Si les quatre sont vérifiées, vous mobilisez avec un dossier solide. Si l'une tombe, vous produisez une note de cinq lignes — et vous économisez la mobilisation de §7.9.

## 19.5 Suivre une campagne dans la durée

Une campagne n'est pas un événement, c'est un **dossier ouvert**. Quatre éléments à tenir.

| Élément | Contenu | Fréquence de mise à jour |
|---|---|---|
| **Le périmètre** | Ce qui est inclus, et les critères de regroupement employés | À chaque nouvel élément |
| **L'évaluation courante** | La conclusion calibrée, avec sa date | Mensuelle, ou à événement |
| **Ce qui l'invaliderait** | La clause de réfutation, mise à jour | À chaque révision |
| **Ce qui a été décidé** | Les actions engagées, et leur état | Continue |

**Le piège du dossier ouvert** : il se poursuit par inertie. Une campagne s'éteint, l'adversaire change d'objectif, et le dossier reste actif parce que personne ne décide de le fermer.

✅ **BONNE PRATIQUE (P1) — la clôture explicite**
Fixez un critère de clôture à l'ouverture du dossier : *sans nouvel élément pendant X semaines, la campagne est déclarée close, avec un résumé de ce qui en a été tiré.* La clôture n'est pas une conclusion sur l'adversaire — c'est une décision de gestion de votre capacité.

## 19.6 🔴 FIL ROUGE — juillet 2030 : trois signalements, une campagne

Entre le 2 et le 19 juillet, trois signalements sans rapport apparent entrent dans la file de Nour.

```
② juillet   — Un client hospitalier signale des tentatives d'authentification
              anormales sur son portail HelioLink.
11 juillet  — Le dispositif sectoriel diffuse une note sur l'exploitation
              d'une vulnérabilité affectant une bibliothèque d'authentification
              largement utilisée.
19 juillet  — Un second client signale un ralentissement de sa passerelle
              HelioBox, sans erreur applicative.
```


**Chacun pris isolément est mineur.** Le premier a été archivé comme *incident client, hors périmètre*. Le deuxième a été rattaché au besoin B-01 et transmis à Malik Ferhaoui. Le troisième était en cours de qualification.

**Ce qui déclenche le rapprochement.** Le 21 juillet, Nour applique la revue hebdomadaire de la file — une pratique instaurée en avril (§15.7) : relire les signalements archivés des trois dernières semaines, quinze minutes, à la recherche de recoupements.

Elle remarque que les deux clients concernés utilisent la même version d'HelioLink, et que la bibliothèque mentionnée le 11 juillet est **embarquée dans cette version**.

**Le regroupement, évalué selon le §19.2** :

| Critère | Présent ? | Solidité |
|---|---|---|
| Même vulnérabilité exploitée | **Oui** — la bibliothèque | Moyenne |
| Même séquence de comportements | **Oui** — tentatives d'authentification suivies de dégradation de performance | **Élevée** |
| Même infrastructure | Non vérifié | — |
| Même secteur | Oui | Faible — écarté comme critère |

**Deux critères indépendants, dont un de solidité élevée.** Le regroupement tient.

**Les quatre conditions du §19.4, appliquées à HELIOMED elle-même** :

| # | Condition | Vérification | Résultat |
|---|---|---|---|
| 1 | Applicabilité | La bibliothèque est-elle dans nos versions ? | **Oui** — dans 3 versions sur 5 encore déployées |
| 2 | Accessibilité | Le vecteur est-il ouvert ? | **Oui** — le portail est exposé par nécessité |
| 3 | Neutralisation | Une mesure l'annule-t-elle ? | **Partiellement** — l'authentification multifacteur limite l'exploitation, sans l'empêcher |
| 4 | Plausibilité | Sommes-nous dans le périmètre ? | **Oui** — nos clients le sont déjà |

**Les quatre sont vérifiées.** Ce n'est pas une menace générale : c'est un dossier qui concerne directement le produit d'HELIOMED, chez ses clients.

**L'évaluation produite le 22 juillet**, avec les cinq blocs du §11.2 :

> *Nous estimons **très probable** que les trois signalements procèdent d'une exploitation de la vulnérabilité signalée le 11 juillet, affectant une bibliothèque embarquée dans trois versions déployées d'HelioLink — **confiance élevée**, fondée sur la correspondance des versions, sur la cohérence de la séquence observée chez deux clients distincts, et sur la description publique du mécanisme.*
>
> *Quarante-trois clients utilisent une version affectée. Le vecteur est accessible ; l'authentification multifacteur limite l'exploitation sans l'empêcher.*
>
> *Ce qui invaliderait : un troisième client affecté utilisant une version non concernée · une cause applicative locale expliquant la dégradation de performance.*

**Ce que la fonction déclenche** — et c'est ici que le CTI rejoint le produit, chapitre 33 :

| Action | Responsable | Délai |
|---|---|---|
| Vérification de la présence de la bibliothèque dans les cinq versions | Développement | 24 h |
| Correctif produit sur les trois versions maintenues | Développement | 6 jours |
| Notification aux 43 clients concernés, avec mesure d'atténuation immédiate | Sécurité produit | 48 h |
| Évaluation de l'obligation de signalement réglementaire | Sécurité produit + juridique | 24 h |

**L'obligation de signalement s'applique** : une vulnérabilité activement exploitée affectant un produit mis sur le marché. La procédure préparée en 2028 est déclenchée pour la première fois en conditions réelles, dans les délais.

**Ce que Claire relève au comité du 30 juillet.** Le rapprochement n'a pas été produit par un outil, ni par une source payante. Il a été produit par **quinze minutes de relecture hebdomadaire** d'une file dont 87 % du contenu est archivé.

> *« Le signalement du 2 juillet avait été archivé. C'est en le relisant qu'il est devenu utile »*, note-t-elle.

**Ce que Nour ajoute**, et qui devient une règle : les signalements archivés ne sont pas supprimés, ils restent consultables pendant douze mois, et la revue hebdomadaire porte sur les trois dernières semaines.

**Livrable de l'épisode.** Le dossier de campagne, avec ses quatre éléments (§19.5) et son critère de clôture — annexe D.

→ **Fin de la Partie IV.** La suite en Partie V, quand il faudra organiser la collecte que ce dossier a rendue nécessaire.

---

> ### 🎓 À ce stade des Parties III et IV, vous savez…
>
> - **transformer une demande floue** en besoin de renseignement formulé, avec un demandeur, une décision et une échéance ;
> - **construire un plan de collecte**, et découvrir que la majorité de vos besoins est déjà couverte ;
> - **écrire ce que vous avez décidé de ne pas suivre** — ce qui prouve qu'un plan existe ;
> - **remplacer le cycle du renseignement** par une file à cinq états, avec archivage motivé ;
> - **raisonner en coût pour l'adversaire** plutôt qu'en gravité technique ;
> - **profiler un acteur inconnu** en quatre paramètres, sans jamais avoir besoin d'un nom ;
> - **lire une cartographie de couverture** et repérer qu'elle suit la facilité, pas le risque ;
> - **regrouper des signalements en campagne** avec deux critères indépendants, et vérifier les quatre conditions qui font passer une menace du général au « nous ».
>
> **Ce que vous ne savez pas encore** : où chercher, dans quel cadre juridique, et à quel prix. C'est l'objet de la Partie V.

---
