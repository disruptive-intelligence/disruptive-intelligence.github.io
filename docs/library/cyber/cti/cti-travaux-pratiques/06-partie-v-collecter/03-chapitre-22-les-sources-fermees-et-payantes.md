---
title: Chapitre 22 — Les sources fermées et payantes
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE V — Collecter
  - index.md
---

## 22.1 Ce qu'un flux commercial apporte réellement

**Trois apports réels**, et il faut les nommer avant de critiquer :

| Apport | Mécanisme |
|---|---|
| **L'agrégation et la normalisation** | Vingt sources deviennent un format unique, exploitable automatiquement |
| **L'accès à des observations non publiques** | Télémétrie du fournisseur, réponse à incident, collecte dans des espaces fermés |
| **Le gain de temps** | Le tri et l'enrichissement sont faits |

**Le deuxième est le seul qui ne soit pas reproductible en interne.** L'agrégation et le gain de temps peuvent s'obtenir autrement ; l'accès à une télémétrie propriétaire, non.

**La question qui doit gouverner toute souscription** : *qu'est-ce que ce fournisseur voit que je ne peux pas voir autrement ?* Si la réponse est vague, l'offre vend de l'agrégation — utile, mais qui doit être payée à son prix.

## 22.2 Typologie des offres

| Type | Contenu | Pertinence typique |
|---|---|---|
| **Flux d'indicateurs** | Volume d'indicateurs techniques, souvent automatisés | **Variable et souvent faible** — §18.4 |
| **Rapports d'analyse** | Modes opératoires, campagnes, acteurs | Bonne, si l'analyse est de qualité |
| **Renseignement sectoriel** | Ciblé sur votre secteur | **Élevée**, quand le secteur est bien couvert |
| **Surveillance de marque et de fuites** | Mentions de votre organisation, données divulguées | **Élevée** — c'est un besoin que rien d'autre ne couvre |
| **Surveillance de surface exposée** | Ce qui est visible de vous depuis l'extérieur | Élevée, et chevauche le MCS |
| **Accès à des espaces fermés** | Ce qui circule dans des espaces criminels | Élevée si votre besoin le justifie ; §20.3 |
| **Renseignement sur mesure** | Réponse à vos questions spécifiques | Très élevée, très coûteuse |

**Les trois types dont le rapport valeur/prix est le plus favorable pour une organisation ordinaire** : surveillance de fuites et de marque · renseignement sectoriel · surveillance de surface exposée. Tous trois répondent à des besoins que les sources ouvertes ne couvrent pas.

**Le type dont le rapport est le moins favorable** : le flux d'indicateurs en volume. Il est le plus vendu et le plus facile à évaluer sur un critère fallacieux — le nombre.

## 22.3 ⚠️ Évaluer un fournisseur avant d'acheter

**La méthode**, en cinq tests. Elle demande deux à quatre semaines et un accès d'évaluation.

| # | Test | Ce qu'il mesure | Comment |
|---|---|---|---|
| **1** | **Recouvrement avec le gratuit** | Ce que vous payez et recevez déjà | Prendre 100 éléments du flux, chercher combien étaient disponibles gratuitement |
| **2** | **Pertinence** | Ce qui vous concerne réellement | Croiser avec votre inventaire : combien touchent vos produits, votre secteur ? |
| **3** | **Fraîcheur** | L'avance sur le public | Pour 20 éléments, comparer la date de publication du fournisseur et la date de publication publique |
| **4** | **Exploitabilité** | Le contexte fourni | Un indicateur sans date, source ni action attendue est inexploitable (§3.3) |
| **5** | **Taux de faux positifs** | Le coût caché | Appliquer 50 indicateurs en observation, mesurer le bruit |

**Le test 1 est celui qui élimine le plus d'offres.** Il est fréquent qu'une majorité substantielle d'un flux commercial soit constituée d'éléments disponibles publiquement — ce qui n'est pas malhonnête, l'agrégation ayant une valeur, mais qui doit être connu pour négocier.

**Le test 3 est celui qui justifie le plus une souscription.** Une avance moyenne de quelques jours sur la publication publique a une valeur réelle et mesurable (§19.3). Une avance nulle signifie que vous payez de l'agrégation.

✅ **BONNE PRATIQUE (P0) — la période d'évaluation contradictoire**
Exigez un accès d'évaluation d'au moins un mois, et conduisez les cinq tests **avant** toute négociation de prix. Un fournisseur qui refuse l'évaluation, ou qui ne fournit pas les données brutes permettant de la conduire, vous dit quelque chose sur son offre.

## 22.4 ⚠️ Le piège du volume

**Le mécanisme commercial** : le volume est le seul attribut d'un flux qui soit facile à mesurer, à comparer et à mettre en avant. Il devient donc l'argument principal — et le critère de choix de l'acheteur.

**Pourquoi c'est fallacieux**, en trois points :

| Point | Explication |
|---|---|
| Le volume mesure ce que le fournisseur collecte | Pas ce qui vous concerne |
| Un indicateur de bas de pyramide se périme en jours | Un flux de deux millions d'indicateurs contient surtout du périmé (§18.4) |
| Le coût de traitement croît avec le volume | Faux positifs, temps d'analyse, saturation des outils |

**La question à substituer** : *combien d'éléments de ce flux ont produit une action utile chez nous au cours des trois derniers mois ?* Ce chiffre est presque toujours de deux à trois ordres de grandeur inférieur au volume annoncé, et c'est lui qui mesure la valeur.

## 22.5 📌 Coût, dépendance, réversibilité

| Dimension | Ce à quoi s'attendre |
|---|---|
| **Coût affiché** | Abonnement annuel, souvent par utilisateur ou par volume |
| **Coût caché n° 1 — l'intégration** | Connecteurs, normalisation, maintenance : souvent supérieur à la licence |
| **Coût caché n° 2 — le traitement** | Le temps d'analyse du flux reçu |
| **Coût caché n° 3 — les faux positifs** | Alertes générées, temps de qualification |
| **Dépendance** | Un processus construit autour d'un fournisseur devient difficile à en séparer |
| **Réversibilité** | Les données historiques sont rarement exportables — vous perdez l'antériorité |

✅ **BONNE PRATIQUE (P1)** — Exigez contractuellement l'**export des données brutes** dans un format ouvert, et l'accès à l'historique en fin de contrat. C'est la même exigence qu'au cours MCS pour les outils de scan, et pour la même raison : sans elle, vous ne pouvez ni mesurer, ni comparer, ni changer de fournisseur.

## 22.6 ✅ Livrable — Grille d'évaluation d'un flux

| Section | Contenu |
|---|---|
| **Besoin** | Quel besoin du plan de collecte cette offre couvre-t-elle ? Réf : … |
| **Ce que le gratuit couvre déjà** | Résultat du test 1 : … % de recouvrement |
| **Pertinence** | Test 2 : … % des éléments concernent nos produits ou notre secteur |
| **Fraîcheur** | Test 3 : avance moyenne de … jours sur la publication publique |
| **Exploitabilité** | Test 4 : les éléments portent-ils date, source, contexte, action ? |
| **Bruit** | Test 5 : … faux positifs sur 50 indicateurs appliqués |
| **Coût total** | Licence + intégration + traitement estimé |
| **Réversibilité** | Export brut : oui / non · Historique en fin de contrat : oui / non |
| **Décision** | Souscrire / négocier / reporter / renoncer — avec motif écrit |

## 22.7 🔴 FIL ROUGE — avril 2030 : le test comparatif

Dix mois après avoir reporté la souscription de 2029 (§21.6), Nour dispose d'un besoin précis que rien ne couvre : **la surveillance des mentions des produits HELIOMED** — besoin B-02, exprimé par Yann Prigent dès mai 2029.

Trois fournisseurs sont mis en évaluation pendant un mois, sur les cinq tests du §22.3.

| Test | Fournisseur A | Fournisseur B | Fournisseur C |
|---|---|---|---|
| **1 — Recouvrement avec le gratuit** | 71 % | **34 %** | 88 % |
| **2 — Pertinence** | 12 % | **41 %** | 6 % |
| **3 — Fraîcheur** | +1,2 j | **+6,4 j** | 0 j |
| **4 — Exploitabilité** | Partielle | **Bonne** | Faible |
| **5 — Faux positifs sur 50** | 19 | **6** | 27 |
| **Prix annuel** | 34 k€ | **19 k€** | 41 k€ |

**Le fournisseur C est le plus cher, le plus volumineux, et le moins utile.** Son argumentaire commercial portait sur le nombre d'indicateurs — 4,2 millions contre 180 000 pour le fournisseur B. Son taux de recouvrement de 88 % avec des sources gratuites explique ce volume.

**Le fournisseur B est retenu.** Il est le moins cher, le moins volumineux, et le seul dont l'avance moyenne — 6,4 jours — a une valeur opérationnelle démontrable.

**Ce que le test 3 permet de chiffrer**, et c'est ce qui emporte la décision de Karim Lebrun :

> *Six jours d'avance sur trois signalements produits par ce fournisseur en un mois d'évaluation. Sur le cas de décembre 2029 (§11.8), six jours d'avance auraient permis de notifier les clients avant leur propre constatation — ce qui change la nature de la relation client.*

**Ce que Nour écrit dans sa note de recommandation**, et qui est repris tel quel :

> *Nous ne recommandons pas le fournisseur qui livre le plus. Nous recommandons celui qui livre le plus tôt ce qui nous concerne.*

**L'épilogue à douze mois.** Le fournisseur B est reconduit. Le rapport d'évaluation annuel montre 14 signalements exploités, dont 4 ayant produit une action produit. Coût par signalement exploité : environ 1 350 €. Nour le présente ainsi, plutôt qu'en volume — et c'est le chapitre 35.

**Livrable de l'épisode.** La grille d'évaluation à cinq tests, versée au référentiel achats d'HELIOMED — annexe D.

→ La suite en 🔴 §23.6, quand un incident interne produira plus de renseignement que douze mois de flux.

## Synthèse mentale du chapitre 22

Un flux commercial apporte trois choses — agrégation, accès à des observations non publiques, gain de temps — et seule la deuxième n'est pas reproductible en interne : la question qui gouverne toute souscription est donc *qu'est-ce que ce fournisseur voit que je ne peux pas voir autrement ?* Cinq tests s'appliquent avant d'acheter, et le premier — le recouvrement avec le gratuit — élimine le plus d'offres, tandis que le troisième — l'avance sur la publication publique — est celui qui justifie le plus une souscription. Le volume est le seul attribut facile à mesurer, ce qui en fait l'argument commercial principal et le critère de choix le plus fallacieux : la question à lui substituer est le nombre d'éléments ayant produit une action utile. Trois coûts cachés dépassent souvent la licence — intégration, traitement, faux positifs — et l'export des données brutes se négocie au contrat, sans quoi vous perdez votre antériorité en changeant de fournisseur.

**Trois questions de vérification**

1. Un fournisseur met en avant un volume de plusieurs millions d'indicateurs. Quelle question posez-vous, et pourquoi le volume n'y répond pas ?
2. Vous disposez d'un mois d'évaluation. Quel test conduisez-vous en premier, et lequel justifiera la dépense s'il est concluant ?
3. Le fournisseur le moins cher est aussi celui qui livre le moins d'éléments. Comment défendez-vous ce choix devant un directeur financier ?

---
