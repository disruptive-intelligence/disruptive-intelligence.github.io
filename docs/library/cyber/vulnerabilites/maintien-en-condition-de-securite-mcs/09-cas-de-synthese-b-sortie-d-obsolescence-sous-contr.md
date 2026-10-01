---
title: Cas de synthèse B — Sortie d'obsolescence sous contrainte et préparation d'un contrôle
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - index.md
---

> **Format** — Cas de pilotage, à traiter avec un tableur ouvert. Durée estimée : **3 heures**.
> **Livrables attendus** : trois options chiffrées (D.8) · plan de lots · fiche de sanctuarisation (D.4) · note d'arbitrage au comité de direction · préparation d'entretien de contrôle.
> **Prérequis** : chapitres 7, 8, 12, 13, 32, 39.

---

## B.1 Le dossier initial

**Nous sommes le lundi 5 octobre 2026.** Vous préparez le comité stratégique du 15 octobre.

### Artefact 1 — état du parc concerné

| Population | Nb | Système | Statut | Contexte |
|---|---|---|---|---|
| Postes bureautiques siège | 340 | Windows 10 22H2 | Hors support depuis le 14/10/2025 | Joints au domaine, gérés par l'infogérant |
| Postes R&D Nantes | 90 | Windows 10 22H2 | Idem | Idem |
| Postes commerciaux nomades | 40 | Windows 10 22H2 | Idem | Idem |
| Postes site industriel (bureautique) | 19 | Windows 10 22H2 | Idem | Idem |
| Postes de supervision industrielle | 11 | Windows 10 IoT LTSB 2016 | **Fin de support le 13/10/2026** | Classe C4, validation constructeur |
| Banc de test PX-40 | 1 | Windows 10 Entreprise LTSB 2016 | **Fin de support le 13/10/2026** | Validation réglementaire des pompes |
| Serveurs | 11 | Windows Server 2016 | **Fin de support le 12/01/2027** | Dont 3 portant des applications métier |

**Total postes hors support : 620** (340 + 90 + 40 + 19 + 11 + 1 arrondi au périmètre géré) · **11 serveurs**.

### Artefact 2 — courriel de l'infogérant, 12 juin 2026

> *« Concernant votre question sur Windows 10 : l'éditeur a annoncé la prolongation du programme de mises à jour de sécurité étendues jusqu'en octobre 2027. Votre parc est donc couvert et il n'y a pas d'urgence à planifier une migration cette année. Nous restons à votre disposition. »*

### Artefact 3 — extrait des conditions d'éligibilité du programme grand public

> Le programme de mises à jour de sécurité étendues destiné aux **appareils personnels** est disponible pour les appareils exécutant Windows 10 version 22H2. **Les appareils joints à un domaine Active Directory ou à Microsoft Entra, ainsi que les appareils gérés par une solution de gestion des appareils mobiles, ne sont pas éligibles à ce programme.** Les organisations doivent souscrire au programme commercial.

### Artefact 4 — compatibilité applicative

| Application | Postes concernés | Validée sur Windows 11 | Remarque |
|---|---|---|---|
| Suite bureautique | 620 | Oui | — |
| Gestion commerciale | 480 | Oui, depuis v9.2 | Migration applicative requise : v9.0 installée |
| Outil de paie | 22 | **Non** | Éditeur : « validation prévue T2 2027 » |
| Chaîne de développement | 90 | Oui | — |
| Suivi de production (lecture) | 19 | Oui | — |
| Conduite de ligne | 11 | **Non — et jamais** | Constructeur : produit en fin de vie |
| Logiciel de banc de test | 1 | **Non** | **Éditeur disparu en 2019** |

### Artefact 5 — contraintes financières et matérielles

- Budget d'investissement 2026 : **engagé à 94 %**. Reste disponible : 38 k€.
- Vote du budget 2027 : **mars 2027**.
- Parc matériel : 210 postes de plus de 5 ans, **incompatibles** avec le nouveau système sans remplacement.
- Coût unitaire de remplacement d'un poste : ordre de grandeur `[à renseigner selon votre contexte]`.
- Coût du support étendu commercial : facturation **par poste et par an**, avec un tarif **croissant chaque année** — le principe est stable, les montants doivent être obtenus par devis.

### Artefact 6 — contexte de contrôle

- Un client hospitalier majeur annonce un **audit de sécurité fournisseur au premier trimestre 2027**, portant sur la chaîne HelioLink.
- La police d'assurance est en renouvellement en février 2027.
- Le référentiel applicable comporte un objectif explicite sur la maîtrise de l'obsolescence.

---

## B.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | L'affirmation de l'infogérant est-elle exacte ? Comment le vérifiez-vous ? | — |
| 2 | Construisez les trois options chiffrées. | D.8 |
| 3 | Proposez un plan de lots avec dépendances. | Tableau de lots |
| 4 | Traitez les 11 postes de supervision et le banc de test. | D.4 |
| 5 | Rédigez la note d'arbitrage au comité de direction. | Note 1 page |
| 6 | Préparez l'entretien de contrôle : six questions et vos réponses. | Grille |
| 7 | Que faites-vous du courriel du 12 juin ? | — |

---

## B.3 Corrigé — la vérification qui renverse la situation

**L'affirmation de l'infogérant est inexacte**, et la vérification prend quinze minutes : lire les conditions d'éligibilité du programme invoqué (artefact 3).

| Programme | Public | Éligibilité du parc HELIOMED |
|---|---|---|
| Support étendu **grand public** | Appareils **personnels** | **Non éligible** — parc joint au domaine et géré |
| Support étendu **commercial** | Organisations | Éligible, **payant**, tarif croissant |

**Conséquence** : les 620 postes n'ont **jamais** été couverts et ne reçoivent plus de correctifs de sécurité depuis le **14 octobre 2025**, soit près de **douze mois** au moment du constat.

⚠️ **La leçon du §12.1, piège n° 1** : une option de support ne se budgète jamais avant d'avoir vérifié, **actif par actif**, son périmètre d'éligibilité. Ici, la vérification n'avait pas été faite parce que l'information venait d'un tiers de confiance — ce qui ne dispense de rien.

**Ce que la découverte change** : le sujet cesse d'être un arbitrage de calendrier pour devenir un sujet de **responsabilité contractuelle** et de **documentation d'un écart de douze mois**.

---

## B.4 Corrigé — les trois options chiffrées

> Les montants ci-dessous sont exprimés en **structure de coût**, non en valeurs absolues : les tarifs de support étendu et de matériel se négocient et se périment. La méthode est ce qui compte.

### Fiche D.8 remplie

| Champ | Contenu |
|---|---|
| Population | 620 postes + 11 serveurs |
| Composant | Système d'exploitation |
| Date de fin de support | 14/10/2025 (postes) · 13/10/2026 (LTSB) · 12/01/2027 (serveurs) |
| Source et vérification | Pages officielles de cycle de vie, consultées le 05/10/2026 |
| Criticité / exposition | C2-C3 pour les postes · C1 pour 3 serveurs |
| **Éligibilité au support étendu** | ☑ **Vérifiée actif par actif** — programme grand public **non applicable** |

### Comparaison des options

| | **Option 1 — support étendu 2 ans** | **Option 2 — migration en 3 lots** | **Option 3 — statu quo** |
|---|---|---|---|
| **Coûts directs** | 620 postes × tarif an 1 + 620 × tarif an 2 (**croissant**) | 210 postes à remplacer + migration applicative gestion commerciale + charge projet | 0 |
| **Coûts indirects** | Coût de la migration, **qui reste dû** après les 2 ans | Tests, formation, support renforcé pendant 9 mois | Compensations · surveillance · urgences · astreinte |
| **Couverture** | Correctifs **critiques uniquement**, selon les critères de l'éditeur | Complète et durable | **Nulle** |
| **Risque résiduel** | Vulnérabilités non critiques non corrigées | Élevé pendant la transition, nul ensuite | 620 postes sans correctif |
| **Position en contrôle** | Défendable si daté et borné | Excellente | **Intenable** |
| **Position en assurance** | Acceptable avec plan | Excellente | Risque de refus de garantie |
| **Faisabilité** | Immédiate | 9 mois | Immédiate |

⚠️ **L'option 3 doit figurer au tableau, chiffrée.** Son absence est la première cause de non-décision (§12.6). Ici, elle est **techniquement disponible mais contractuellement indisponible** : l'audit client de T1 2027 et le renouvellement d'assurance de février la rendent inacceptable. Ce point s'écrit, il ne se sous-entend pas.

### Décision recommandée

**Option 2, avec un pont ciblé** :

- Migration en trois lots sur neuf mois.
- Support étendu commercial limité à **140 postes** — ceux portant l'outil de paie (22) et une partie de la gestion commerciale en attente de validation (118).
- Le pont est **daté, borné et chiffré** : il se termine au T4 2027, à la migration du lot 3.

**Ce qui rend cette option supérieure** : sur deux ans, l'option 1 représente une fraction significative du coût de la migration **sans produire aucun bénéfice durable** — et la migration reste à financer ensuite. L'arbitrage se fait en quinze minutes une fois le tableau posé.

---

## B.5 Corrigé — le plan de lots

| Lot | Périmètre | Nb | Échéance | Prérequis | Dépendances |
|---|---|---|---|---|---|
| **0 — Pilote** | 15 postes, 4 profils représentés | 15 | Nov. 2026 | Aucun | Valide le processus et produit le chiffrage réel |
| **1** | Postes bureautiques standards, matériel compatible | 200 | T1 2027 | Lot 0 concluant | Aucune |
| **2** | Postes avec gestion commerciale, matériel compatible | 265 | T2 2027 | **Migration applicative v9.0 → v9.2** | Bloquant : à lancer **immédiatement** |
| **3** | Postes à remplacer + paie | 140 | T4 2027 | Budget 2027 voté · **validation éditeur paie (T2 2027)** | Sous pont de support étendu |
| **Hors lots** | 11 supervision + 1 banc de test | 12 | — | — | Voir §B.6 |

### Le séquencement, et pourquoi il ne suit pas les dates

La date de fin de support est **identique** pour les 620 postes. Le critère du §12.3 s'applique : **criticité × exposition × effort**.

- Le **lot 0** part en premier pour produire un chiffrage réel — c'est le levier n° 4 du §12.7 contre le report perpétuel : l'argument « c'est trop risqué » ne résiste pas à une migration déjà réalisée en interne.
- Le **lot 1** regroupe le plus simple : matériel compatible, aucune dépendance applicative. Il fait chuter le volume rapidement.
- Le **lot 2** est conditionné par une migration applicative de neuf semaines. **Elle doit être lancée dès octobre 2026** — le §26.10 rappelle que la négociation avec un éditeur métier doit démarrer six mois avant l'échéance.
- Le **lot 3** dépend d'un budget non voté et d'une validation éditeur non acquise : c'est lui qui porte le pont.

⚠️ **L'erreur de séquencement à éviter** : commencer par les cas difficiles « parce qu'ils sont les plus risqués ». Le lot 3 en premier bloquerait le programme sur une dépendance externe pendant six mois, sans qu'aucun poste ne soit migré.

---

## B.6 Corrigé — les deux systèmes contraints

### Cas 1 — les 11 postes de supervision

| Élément | Décision |
|---|---|
| Décision structurante (§32.1) | **Remplacer** — mais à l'échelle du système de conduite, pas du poste |
| Contrainte | Le constructeur a placé le produit en fin de vie ; aucune version compatible n'existera |
| Horizon | Renouvellement du système de conduite : projet industriel pluriannuel, hors périmètre DSI |
| **Traitement intérimaire** | **Isoler** : régime C4, réseau industriel séparé, compensation selon §20.2, fenêtre lors des arrêts de production |
| Dérogation | Signée par le directeur industriel, revue semestrielle |
| Provision | Inscrite au plan pluriannuel industriel |

### Cas 2 — le banc de test PX-40 (fiche D.4)

| Champ | Contenu |
|---|---|
| Objet | `BANC-PX40-01` · système hors support au 13/10/2026 · logiciel de pilotage sans version récente |
| Type d'impossibilité | ☑ **Technique** — éditeur disparu en 2019, aucun correctif ne viendra jamais |
| Analyse de risque en termes métier | Le banc valide la conformité réglementaire des pompes PX-40. Sa compromission pourrait altérer des résultats de validation, avec des conséquences sur la conformité des dispositifs mis sur le marché et sur la sécurité des patients. Le poste ne contient pas de données à caractère personnel. |
| Exposition avant compensation | Réseau industriel, joignable depuis 11 postes de supervision |
| **Décision structurante** | **ISOLER** — remplacer le banc complet représente ~300 k€ et 18 mois, requalification comprise |
| Compensations | **1.** Retrait de tout réseau (rang 1, §20.2). **2.** Transferts par support dédié, chaîne du §29.5. **3.** Deux comptes nominatifs, journal papier des interventions. **4.** Contrôle trimestriel de l'absence de connexion. |
| Moyen de vérification | Contrôle physique trimestriel : absence de câble, absence d'interface sans fil active, relevé du journal papier |
| Coût de la solution | ~14 k€ — matériel réseau et deux jours d'ingénierie |
| Signataire | **Directeur général** — la grille C.4 impose ce niveau : impact potentiel sur la conformité de dispositifs médicaux |
| Date d'expiration | 31/12/2028, alignée sur la revue du plan pluriannuel |
| Conditions de révocation anticipée | Panne matérielle du poste · évolution de l'exigence réglementaire de validation · disponibilité d'une solution de remplacement qualifiée |
| Provision | Remplacement du banc inscrit au plan pluriannuel, horizon 2031 |

**Le point à retenir** : deux systèmes également non corrigeables, deux décisions différentes. Ce qui les distingue n'est pas technique — c'est le **rapport entre le coût du remplacement et la valeur de l'usage**, et la disponibilité d'une trajectoire.

---

## B.7 Corrigé — la note d'arbitrage au comité de direction

> **Note — Sortie d'obsolescence du parc bureautique — 8 octobre 2026 — 1 page**
>
> **1. Situation.** 620 postes de travail ne reçoivent plus de correctifs de sécurité depuis le 14 octobre 2025. Le programme de prolongation évoqué en juin ne s'applique pas aux parcs professionnels gérés : la vérification des conditions d'éligibilité, réalisée le 5 octobre, l'établit sans ambiguïté. L'écart porte donc sur douze mois.
>
> **2. Ce que cela signifie.** Toute vulnérabilité publiée depuis un an sur ce système reste non corrigée sur l'ensemble du parc bureautique. Deux échéances externes rendent cette situation intenable : un audit de sécurité d'un client hospitalier au premier trimestre 2027, et le renouvellement de la police d'assurance en février.
>
> **3. Trois options.** *(tableau du §B.4)*
>
> **4. Recommandation.** Migration en trois lots sur neuf mois, avec un pont de support étendu commercial limité à 140 postes, daté et borné au quatrième trimestre 2027. Sur deux ans, l'option de support étendu seule représente une part significative du coût de la migration sans en produire aucun bénéfice durable, et la migration resterait à financer.
>
> **5. Ce que nous demandons.** L'inscription au budget 2027 du remplacement de 210 postes et du pont de support étendu · le lancement immédiat de la migration applicative de la gestion commerciale, prérequis bloquant du lot 2 · la signature de la dérogation relative au banc de test de validation.
>
> **6. Ce qui reste non résolu.** La validation de l'outil de paie par son éditeur est annoncée pour le deuxième trimestre 2027 sans engagement contractuel. En cas de retard, 22 postes resteront sous pont au-delà du quatrième trimestre 2027. Ce risque est identifié, il n'est pas maîtrisé par nous.

⚠️ **La section 6 est celle qui fait la différence.** Une note qui ne présente que des problèmes résolus n'est pas crédible. Celle-ci nomme ce qui échappe à l'organisation, et elle le nomme **avant** que cela ne se produise.

---

## B.8 Corrigé — l'entretien de contrôle

| Question du contrôleur | Réponse attendue | Pièce du dossier |
|---|---|---|
| « Combien d'actifs sont hors support ? » | Le chiffre, **avec son dénominateur** et la répartition par population : 620 postes sur 941 actifs du périmètre, 11 serveurs sur 187 | Périmètre daté (D.13, pièce 1) |
| « Depuis quand ? » | 14/10/2025 pour les postes. **Et la cause** : une information d'éligibilité inexacte reçue d'un tiers, non vérifiée à la source jusqu'au 05/10/2026 | Note interne datée |
| « Qu'avez-vous décidé ? » | Les trois options chiffrées, l'option retenue, le décideur, la date de décision | D.8 + note d'arbitrage |
| « Qu'est-ce qui n'est pas couvert ? » | L'annexe des périmètres non couverts, tenue depuis 2026 : banc de test, postes de supervision, avec compensations et échéances | Annexe de D.1 |
| « Comment le prouvez-vous ? » | Périmètre daté, journaux de campagne par lot, échantillon de preuve d'état sur chaque lot | D.13, pièces 1, 5, 6 |
| « Et si le lot 3 glisse ? » | Le risque est identifié dans la note du 08/10/2026, section 6. Le pont de support étendu est prolongeable, avec son coût connu | Note d'arbitrage |

### Ce qui fait la différence dans cet entretien

L'organisation **ne prétend pas être conforme**. Elle démontre trois choses :

1. Elle **connaît** ses écarts, et les chiffre avec leur dénominateur.
2. Elle les a **décidés au bon niveau**, avec une trace datée.
3. Elle en **suit** l'évolution, avec des échéances et un financement.

C'est exactement le §39.1. Un dossier qui prétendrait à 100 % de conformité sur ce parc serait immédiatement suspect.

### Barème d'évaluation de l'entretien

| Critère | Pts |
|---|---|
| Chiffres donnés avec dénominateur et population | 20 |
| Cause de l'écart assumée, sans dissimulation ni mise en cause | 15 |
| Trois options présentées, dont le statu quo | 20 |
| Périmètres non couverts présentés spontanément | 20 |
| Preuves produites, datées, avec périmètre | 15 |
| Risque non maîtrisé nommé avant d'être découvert | 10 |

**Élimination** : présenter le taux de conformité de la console de l'infogérant sans mentionner les 620 postes.

---

## B.9 Corrigé — le courriel du 12 juin

Trois usages, dans cet ordre.

1. **Contractuel.** L'information transmise était inexacte et a fondé une décision de report. Le sujet n'est plus « qui devait patcher » — le contrat ne comportait aucun engagement de délai — mais « quelle information avons-nous reçue ». C'est ce déplacement qui rend la renégociation possible (§13.9).
2. **Documentaire.** Le courriel devient une pièce du dossier de preuves : il établit la cause de l'écart de douze mois, ce qui est très différent d'une négligence non expliquée (§39.1).
3. **Préventif.** Il justifie l'ajout au contrat d'une clause de restitution de données et d'une clause d'escalade des impossibilités (D.9, clauses 3 et 8). Sans donnée restituée, l'organisation ne pouvait pas détecter elle-même que le parc n'était pas couvert.

⚠️ **Ce qu'il ne faut pas en faire** : un instrument de mise en cause personnelle. L'objectif est d'obtenir des clauses, pas d'avoir raison.

---

## B.10 Bilan à douze mois et ce qui n'a pas fonctionné

| Indicateur | Oct. 2026 | Oct. 2027 |
|---|---|---|
| Postes hors support | 620 | **140** (sous pont daté) |
| Serveurs hors support | 11 | **2** |
| Ratio confirmé conforme, parc bureautique | 34 % | **89 %** |
| Contrôle client T1 2027 | — | Passé, deux observations mineures |
| Surprime d'assurance | 34 % | Renégociée |

**Ce qui n'a pas fonctionné**, et qui doit figurer au retour d'expérience :

1. **Le lot 2 a glissé de six semaines.** La migration applicative de la gestion commerciale a démarré en novembre au lieu d'octobre : la commande a attendu une validation d'achat non anticipée. Le §26.10 aurait dû être appliqué six mois plus tôt.
2. **Deux postes du lot 1 ont dû être repris.** Du matériel incompatible n'avait pas été détecté à l'inventaire — les caractéristiques matérielles ne figuraient pas dans les attributs suivis (Annexe I.1).
3. **Le pont a coûté plus que prévu.** Le tarif de la deuxième année n'avait pas été intégré au chiffrage initial, alors que le §12.1 le signale explicitement.

---
