---
title: Chapitre 4 — Renseignement, soupçon, preuve et judiciarisation
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie I — Comprendre le renseignement financier
  - index.md
---

## Objectif du chapitre

Maîtriser **les quatre étapes** d’une chaîne d’information financière, de la donnée brute à la preuve judiciaire — et savoir où se situe le FININT dans cette chaîne. C’est le socle de la rigueur analytique qui distingue un professionnel d’un commentateur.

## Le concept

Quatre étapes hiérarchisées, chacune avec son **régime juridique** et son **régime de vérité**.

**1. La donnée.** Elle est ce qui est observable, factuel : un virement, une mention sur un registre, une déclaration de soupçon, une publication de presse. La donnée est le matériau brut. Elle peut être fiable ou non, complète ou non, datée ou non.

**2. Le soupçon.** Il naît quand la donnée présente des **éléments qualifiés** qui sortent de la normalité attendue. Le soupçon a un seuil légal en LCB-FT : il est l’élément déclencheur de la déclaration de soupçon (DS). Le seuil n’est ni la certitude ni la preuve — c’est un faisceau d’éléments objectifs qui justifie la déclaration. Le soupçon est une **lecture qualifiée** de la donnée.

**3. Le renseignement.** Il est produit par l’analyste à partir de plusieurs données et de plusieurs soupçons (DS convergentes, sources OSINT, sources fermées). Il **structure** une hypothèse, en évalue la confiance, identifie le réseau et les flux, et formule des recommandations. C’est le livrable FININT au sens strict.

**4. La preuve.** Elle est ce qui est **opposable devant un tribunal**. Elle doit avoir été obtenue dans un cadre légal admissible (réquisition judiciaire, audition, expertise judiciaire, perquisition autorisée). Le renseignement FININT n’est généralement pas une preuve directe : il est une **piste** qui oriente l’enquête judiciaire, laquelle, par ses propres actes, transforme certains éléments en preuves admissibles.

## L’utilité opérationnelle

Cette distinction structure tout le travail :

- **Au cadrage** : quelles sources puis-je mobiliser ? Quel est leur régime juridique ?
- **Pendant l’analyse** : ce que je vois, qu’est-ce que c’est — donnée, soupçon, renseignement ?
- **Dans le livrable** : quel vocabulaire, quel niveau d’affirmation ?
- **À la sortie** : à qui je transmets, sous quelles conditions, et que peut-on en faire ?

Mal positionner une information dans la chaîne, c’est **faire un faux pas opérationnel** : présenter une preuve quand on n’a qu’un soupçon (sur-promettre, faire du mal), ou inversement présenter un soupçon quand on a déjà du renseignement structuré (sous-vendre, faire perdre du temps).

## Méthode — la grille de qualification

Face à toute information, l’analyste applique une grille en quatre questions :

1. **Source** — qui est l’émetteur, dans quel cadre ai-je obtenu l’information ?
1. **Régime juridique** — l’information peut-elle être utilisée ouvertement, en interne, judiciairement ?
1. **Niveau de qualification** — donnée brute, soupçon, renseignement, preuve ?
1. **Niveau de confiance** — quasi-certain, probable, possible, indéterminable (chapitre 33) ?

Cette grille peut être tabulée pour chaque pièce du dossier. Elle accompagne ensuite la note d’analyse, comme matrice de sources.

## Mini-walkthrough — la chaîne CLEARFLOW

Reprenons un fragment du dossier Haddad pour illustrer la chaîne complète :

|Étape        |Élément                                                                                                                                                                                                                  |Régime                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
|Donnée       |Un virement de 92 000 € de SOCIETE_DUBAI vers NEXUS_FRANCE le 14 mars                                                                                                                                                    |Observation                                                      |
|Soupçon      |Le virement s’inscrit dans une série de 18 virements similaires sur 6 mois, libellés vagues, contrepartie nouvelle, sans cohérence apparente avec l’activité déclarée → DS de la banque                                  |Déclaration LCB-FT                                               |
|Renseignement|Recoupé avec 16 autres DS et OSINT, le schéma est compatible avec une activité de TBML (probable, niveau de confiance modéré)                                                                                            |Note FININT, exploitable par autorités, non opposable au tribunal|
|Preuve       |Le procureur, sur la base du renseignement, ouvre une enquête. La réquisition judiciaire des relevés permet d’obtenir les pièces exploitables au tribunal. L’expertise comptable d’un expert judiciaire qualifie les flux|Pièces du dossier judiciaire                                     |

À chaque étape, ce qui change : la **qualification** (de l’observation à la qualification typologique à la qualification pénale), le **régime** (fait observable, déclaration légale, livrable analytique, pièce judiciaire), et l’**autorité** qui en est responsable (banque → analyste → magistrat).

## Erreurs fréquentes

- **Confondre DS et preuve** : une DS est un signalement légal, pas une affirmation de culpabilité. Le déclarant n’a pas besoin d’être certain — il a besoin d’avoir un soupçon qualifié.
- **Présenter le renseignement comme « la vérité »** : le renseignement est une lecture qualifiée à un instant donné. Il peut être révisé.
- **Ne pas baliser ce qu’on transmet** : transmettre un livrable sans préciser sa nature (« renseignement », « pré-rapport », « note de cadrage ») expose à des malentendus.

## Limites

Cette taxonomie est claire en théorie ; en pratique, certains éléments sont **ambigus** : une expertise privée commandée par une partie a-t-elle valeur de preuve ? Un rapport d’audit forensique peut-il être versé au dossier ? Un relevé obtenu en EAR/CRS est-il directement opposable ? Les réponses dépendent du droit national applicable et de l’usage qui en est fait. L’analyste consulte le juriste de son service en cas de doute.

## Lien avec le fil rouge

> **CLEARFLOW — Posture de Nassim**
> 
> Sa note finale (chapitre 64) commencera par cette phrase : *« La présente note constitue un livrable de renseignement financier au sens de l’article L.561-29 CMF [équivalent fictif]. Elle vise à orienter l’enquête. Elle n’est pas opposable en l’état comme pièce judiciaire. Les éléments qu’elle expose sont calibrés en confiance ; les pièces sous-jacentes sont conservées dans le dossier de référence et peuvent être communiquées au magistrat sur demande, dans le cadre approprié. »* Cette phrase n’est pas une formalité : elle protège l’analyste, le service, et l’exploitabilité ultérieure.

## Points clés à retenir

- Quatre étapes : donnée → soupçon → renseignement → preuve.
- Chaque étape a son régime juridique et son régime de vérité.
- Le FININT produit du renseignement ; il ne produit pas de preuve directe.
- La grille de qualification (source / régime / qualification / confiance) accompagne tout livrable sérieux.

-----
