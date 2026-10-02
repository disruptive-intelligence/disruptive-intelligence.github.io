---
title: Chapitre 1 — Pourquoi le FININT est central aujourd’hui
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie I — Comprendre le renseignement financier
  - index.md
---

## Objectif du chapitre

Comprendre pourquoi le renseignement financier — discipline relativement récente dans sa formalisation — est devenu un **levier central** des politiques de sécurité, des stratégies de conformité et de la compréhension de la criminalité organisée moderne. Ce chapitre n’expose pas une nostalgie historique : il pose les enjeux concrets qui justifient le poids actuel du FININT, et qui structurent la demande professionnelle adressée aux analystes.

## Le concept

Le **Financial Intelligence (FININT)** est la discipline qui collecte, analyse et exploite l’information financière — bancaire, comptable, patrimoniale, commerciale, registrale — pour détecter, comprendre, entraver et documenter la criminalité économique et le financement d’activités illicites. Le FININT ne se limite pas à la lecture des relevés bancaires : il englobe toute la chaîne d’information qui permet de **suivre l’argent** dans l’économie réelle, depuis l’origine présumée des fonds jusqu’à leur intégration finale.

Le FININT s’enracine historiquement dans la **lutte contre le blanchiment de capitaux** (LCB), formalisée dans les années 1980-1990 (création du GAFI en 1989, réseau Egmont en 1995), et étendue après le 11 septembre 2001 à la lutte contre le **financement du terrorisme** (CFT). Ce socle initial, devenu LCB-FT, s’est progressivement élargi à la corruption transnationale (suite aux scandales Enron, FCPA, à la Convention de Mérida 2003), à la fraude fiscale internationale (lendemain de la crise 2008, montée en puissance de l’EAR/CRS), aux sanctions économiques (en particulier post-2014 et plus encore post-2022), et à la criminalité organisée transnationale dans son ensemble.

## L’utilité opérationnelle

Plusieurs facteurs expliquent la centralité actuelle du FININT.

**Le suivi de l’argent est l’un des seuls leviers communs à toutes les criminalités.** Que l’on parle de trafic de stupéfiants, de cybercriminalité, de corruption, de fraude fiscale ou de financement du terrorisme, à un moment ou à un autre, l’argent doit circuler, être stocké, ou être intégré dans l’économie légale. C’est ce passage qui laisse des traces — et que le FININT exploite.

**Les sanctions économiques sont devenues un instrument de politique extérieure majeur.** L’OFAC, l’UE et l’ONU produisent et font évoluer en continu des listes de personnes et entités sanctionnées. La détection de contournements (via pays tiers, sociétés écrans, cryptos, intermédiaires complaisants) est devenue une priorité opérationnelle pour les États comme pour les institutions financières.

**La transparence financière s’est imposée comme une norme internationale.** L’EAR/CRS (échange automatique de renseignements fiscaux entre plus de 100 juridictions), les directives DAC successives en UE (DAC6, DAC7, DAC8), les registres des bénéficiaires effectifs, l’évolution post-MiCA pour les VASP, dessinent un environnement où le secret bancaire historique a perdu une grande partie de son efficacité — au moins en théorie. Les analystes savent exploiter ce nouveau paysage.

**La criminalité organisée s’est financiarisée.** Les groupes criminels modernes utilisent des structures sophistiquées : holdings, trusts, fondations, montages multi-juridictionnels, corporate service providers professionnels, réseaux de prête-noms. Les comprendre exige une compétence FININT — pas seulement une compétence judiciaire.

**La cybercriminalité a un débouché financier obligatoire.** Les rançons, les fonds volés via BEC, les revenus de la fraude en ligne, les produits de la traite, doivent tous être convertis et intégrés. Le FININT et la cybercriminalité convergent. Dans un dossier moderne, les analystes financiers et cyber doivent souvent coopérer (chapitre 48).

## Méthode — comment se positionner intellectuellement face à un dossier FININT

Le FININT n’est pas un domaine où l’on accumule des informations « parce que c’est intéressant ». Il est strictement **finalisé** : chaque collecte, chaque analyse, chaque livrable répond à une question — une question de renseignement (QR). Cette discipline finalisée est la première compétence à acquérir.

**Cinq postures professionnelles** structurent l’approche :

1. **Postulat du doute calibré** — toute information non vérifiée est une hypothèse. Toute corrélation n’est pas causalité.
1. **Discipline d’attribution** — chaque élément retenu doit être traçable à sa source. La fiabilité de la conclusion dépend de la fiabilité de la source.
1. **Calibration de la confiance** — chaque conclusion porte un niveau de confiance explicite (chapitre 33).
1. **Distinction faits / inférences / hypothèses** — vocabulaire calibré, formulations prudentes.
1. **Recul méthodologique** — pourquoi cherche-t-on cette information ? que va-t-elle changer dans la note ?

## Mini-walkthrough

Imaginons un mandat simple : *« Une équipe compliance d’une banque mutualiste signale qu’un client professionnel — une SAS de négoce de matériel agricole — reçoit depuis six mois des virements importants de Turquie, sans cohérence apparente avec l’activité déclarée. Que peut faire un analyste FININT ? »*.

Réponse opérationnelle : il **ne s’agit pas** de conclure que la SAS blanchit. Il s’agit de :

- formuler trois ou quatre questions de renseignement précises (QR1 : la SAS a-t-elle une activité réelle de négoce ? QR2 : qui sont les contreparties turques ? QR3 : quel est le profil du dirigeant ? QR4 : y a-t-il déjà des DS antérieures ou des éléments dans des leaks ?) ;
- identifier les sources mobilisables (registre français, registre turc, presse, leaks, OSINT sur la société, données bancaires si en cadre légal CRF) ;
- produire une **mini-note** à 45 minutes (parcours express) qui qualifie le dossier en *probable* / *à investiguer* / *peu d’éléments à ce stade* ;
- recommander si besoin l’approfondissement, ou la transmission à un autre service.

Tout l’art réside dans le passage de l’intuition (« ça sent mauvais ») à un livrable structuré et défendable.

## Erreurs fréquentes

- **Confondre intuition et analyse** : un signal n’est pas une conclusion. Il déclenche une enquête, il ne la termine pas.
- **Croire au mythe de la donnée parfaite** : un analyste FININT travaille toujours avec des données partielles, biaisées, parfois contradictoires. La méthode est ce qui transforme cette imperfection en livrable utile.
- **Sur-promettre** : *« on va trouver toute la vérité »*. Non. On va produire du renseignement actionnable, dans un cadre légal, dans un temps borné, avec des limites explicites.
- **Sous-estimer le judiciaire** : la note FININT n’est pas la fin de l’histoire. Elle est un point de bascule potentiel vers une procédure. La rigueur du livrable conditionne l’exploitabilité ultérieure.

## Limites

Le FININT ne **prouve pas** au sens judiciaire (chapitre 4). Il **oriente**. Il n’a pas accès direct aux moyens d’enquête réservés au judiciaire (perquisition, garde à vue, audition). Il dépend de la qualité des sources mobilisables — qui peuvent être fragmentaires, surtout dans les juridictions opaques (chapitre 10). Et il ne remplace pas l’expertise comptable, juridique, fiscale, sectorielle ; un analyste FININT travaille avec ces expertises, pas à leur place.

## Lien avec le fil rouge

> **CLEARFLOW — Cadrage**
> 
> Lorsque le dossier Haddad arrive sur le bureau de Nassim, il représente déjà 17 DS, une douzaine de sociétés présumées, sept juridictions et environ 22 M€ de flux. Si Nassim cherchait *« la vérité complète »*, il s’enliserait. Il commence donc par poser ses cinq questions de renseignement (QR1 à QR5) et estime un budget temps : 6 à 8 semaines pour produire une première note d’analyse robuste, avec coopérations engagées en parallèle. La discipline de cadrage est ce qui distingue une enquête FININT d’une accumulation de documents.

## Points clés à retenir

- Le FININT est une discipline **finalisée**, structurée par des questions de renseignement.
- Sa centralité actuelle découle de la convergence sanctions / transparence / financiarisation du crime / cyber.
- Le FININT produit du **renseignement orienté action**, pas de la connaissance pour la connaissance.
- Cinq postures professionnelles : doute calibré, attribution, calibration, distinction, recul.
- Les limites du FININT — non-preuve judiciaire, sources partielles, dépendance aux cadres légaux — sont à intégrer dès le cadrage.

-----
