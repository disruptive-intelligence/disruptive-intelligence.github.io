---
title: Chapitre 38 — Organiser la fonction
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

## 38.1 Où rattacher le CTI

| Rattachement | Avantage | Risque |
|---|---|---|
| **RSSI** | Proximité des besoins, légitimité transverse | Peut devenir un service du seul RSSI |
| **Centre opérationnel de sécurité** | Proximité de la détection, boucle courte | **Dérive vers le tactique uniquement** |
| **Équipe de réponse à incident** | Utile en crise | Absorption par l'opérationnel, pas de production régulière |
| **Direction des risques** | Vision stratégique | Éloignement du terrain, produits trop généraux |
| **Fonction autonome** | Indépendance de jugement | Isolement, difficulté à exister |

**Le critère de choix**, plus utile que le rattachement lui-même : **d'où viennent les besoins ?** Une fonction rattachée à un service qui n'exprime qu'un type de besoin produira un seul type de renseignement.

⚠️ **Le risque le plus fréquent est le deuxième** : rattachée à la détection, une fonction CTI devient un service d'alimentation en indicateurs — utile, mais qui abandonne les niveaux opérationnel et stratégique, c'est-à-dire l'essentiel de sa valeur (§3.4).

## 38.2 Une personne, une équipe, un service partagé

| Configuration | Ce qu'elle permet | Ce qu'elle exige |
|---|---|---|
| **Une fraction de poste** | Un niveau, quelques besoins | Un périmètre déclaré (§3.7) |
| **Une personne** | Deux niveaux, quatre à six besoins | Une relecture externe (§12.5) |
| **Deux à trois personnes** | Les trois niveaux, spécialisation possible | Une coordination, un partage de la file |
| **Service partagé entre entités** | Mutualisation des coûts | Une gouvernance des priorités entre entités |

**Le seuil qui compte** : à partir de deux personnes, la revue par les pairs devient interne et le chapitre 12 s'applique pleinement. En dessous, les substituts du §12.5 sont indispensables — ce n'est pas optionnel.

## 38.3 Les interfaces

**Ce qui doit être établi**, avec chaque fonction consommatrice :

| Interface | Ce qui doit exister | Fréquence |
|---|---|---|
| **Détection** | Un canal, un format (§30.7), un point régulier | Hebdomadaire |
| **Gestion des vulnérabilités** | Un format de contribution (§31.6) | Au rythme des campagnes |
| **Réponse à incident** | Une place en cellule, une procédure (§32) | À l'incident |
| **Produit** | Un canal, et le lien avec l'obligation de signalement | Continue |
| **Direction** | Un rendez-vous, pas des envois | Trimestrielle |
| **Juridique et protection des données** | Un référent identifié | À la demande, et au plan de collecte |

**La ligne « direction » mérite un développement.** Un produit stratégique envoyé par écrit a une audience faible ; le même contenu présenté en quinze minutes, avec une question explicite, produit une décision. C'est ce qu'HELIOMED découvre au §37.6.

## 38.4 ⚠️ L'anti-pattern : le CTI qui devient une veille documentaire

**Le mécanisme**, en quatre étapes :

```
1. La fonction est créée sans besoins formulés
2. Elle produit une lettre d'information périodique, faute de mieux
3. La lettre devient l'attendu — on la demande, on la mesure
4. La fonction est jugée sur sa régularité, plus sur son utilité
```


**Les signes**, tous observables :

| Signe | Ce qu'il indique |
|---|---|
| Le produit principal est périodique et non déclenché | La production suit le calendrier, pas le besoin |
| Le contenu est le même que ce qu'on trouve ailleurs | §2.3 — c'est de la connaissance redistribuée |
| Personne ne pose de question à la fonction | Elle n'est pas perçue comme utile |
| Le succès se mesure en régularité | §35.3 |

**Le remède**, et il est difficile : **arrêter la lettre**. Une fonction qui produit un livrable périodique attendu ne peut pas s'en libérer par ajout ; elle doit l'interrompre et le remplacer par des produits déclenchés par des besoins.

## 38.5 🔴 FIL ROUGE — septembre 2031 : où se rattache la fonction

L'ouverture d'un second poste pour 2032 (§35.8) pose une question restée implicite : **où la fonction se rattache-t-elle ?**

**La situation depuis 2029** : Nour est rattachée à Claire Nadeau, RSSI. Le rattachement n'a jamais été formalisé — il résultait du recrutement.

**Les trois options examinées** :

| Option | Argument pour | Argument contre |
|---|---|---|
| Rattachement au RSSI | Statu quo, ça fonctionne | Les besoins produit et détection passent par un intermédiaire |
| Rattachement à la détection | Boucle courte avec le principal consommateur tactique | **Perte des niveaux opérationnel et stratégique** |
| Fonction autonome sous la DSI | Indépendance de jugement, accès direct aux métiers | Isolement, et Nour serait seule à porter la légitimité |

**Ce qui tranche**, et ce n'est pas un argument d'organigramme. Nour reprend son registre des besoins :

| Besoin | Demandeur | Décisions produites en 24 mois |
|---|---|---|
| B-01 priorisation | MCS | **14** |
| B-02 mentions produit | Produit | 5 |
| B-03 ce qui arrive aux pairs | RSSI | 6 |
| B-05 écart de détection | Détection | 4 |
| B-07 fuites | RSSI | 4 |
| B-04 orientation investissement | DSI | **0** |

**Les besoins viennent de cinq services différents.** Un rattachement à l'un d'eux privilégierait structurellement ses besoins.

**La décision retenue** : maintien du rattachement au RSSI, **avec deux mesures correctives** :

1. **Un comité de priorisation trimestriel**, réunissant les cinq demandeurs, qui arbitre les besoins actifs et la capacité allouée à chacun. Ce n'est pas Claire qui décide seule de ce que la fonction traite.
2. **Un accès direct** de Nour aux demandeurs, sans passage par la hiérarchie — formalisé, pour éviter que ce soit perçu comme un contournement.

**Ce que Sonia Weber relève**, et qui est le point de l'épisode :

> *« Le problème n'était pas le rattachement. C'était que personne n'arbitrait entre les besoins, sauf Nour elle-même — et elle arbitrait forcément vers ceux qui lui répondaient. »*

**C'est le diagnostic exact du besoin B-04** : il n'a produit aucune décision parce qu'il était le plus coûteux à servir et le moins relancé, donc systématiquement dépriorisé par une analyste qui ne pouvait pas arbitrer contre elle-même.

**Livrable de l'épisode.** La charte de la fonction : rattachement, comité de priorisation trimestriel, accès direct, et règle d'arbitrage de la capacité — annexe D.

## Synthèse mentale du chapitre 38

Le critère de rattachement n'est pas l'organigramme mais l'origine des besoins : une fonction rattachée à un service qui n'exprime qu'un type de besoin produira un seul type de renseignement. Le risque le plus fréquent est le rattachement à la détection, qui transforme le CTI en service d'alimentation en indicateurs et lui fait abandonner les niveaux où se situe l'essentiel de sa valeur. En dessous de deux personnes, les substituts à la revue par les pairs ne sont pas optionnels. Un produit stratégique envoyé par écrit a une audience faible ; présenté en quinze minutes avec une question explicite, il produit une décision. Enfin, l'anti-pattern de la veille documentaire ne se corrige pas par ajout : il faut interrompre le livrable périodique, et c'est difficile parce qu'il est devenu l'attendu.

**Trois questions de vérification**

1. Vos besoins viennent de cinq services différents. Quel critère utilisez-vous pour décider du rattachement, et quelle mesure corrective ajoutez-vous ?
2. Pourquoi le rattachement à la détection est-il le risque le plus fréquent, et que perd-on ?
3. Un besoin ne produit aucune décision depuis deux ans. Quelle est l'explication la plus probable, et pourquoi l'analyste seul ne peut-il pas la corriger ?

---
