---
title: Chapitre 6 — Le système bancaire et la circulation de l’argent
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie II — Le système financier pour l’enquêteur
  - index.md
---

## Objectif du chapitre

Comprendre l’**architecture institutionnelle** du système bancaire — banques de détail, banques d’investissement, banques privées, correspondent banks, banques centrales — et la manière dont l’argent circule entre ces acteurs. C’est le socle sans lequel les flux observables n’ont pas de sens.

## Le concept

Le système bancaire est organisé en **plusieurs strates**.

Les **banques commerciales de détail** sont l’interface du grand public et des entreprises : comptes courants, dépôts, crédits, moyens de paiement. En France : banques mutualistes (Crédit Agricole, Crédit Mutuel, BPCE), grands réseaux (BNP Paribas, Société Générale, Crédit du Nord), banques en ligne (Boursorama, Fortuneo). Au UK : Barclays, HSBC, NatWest, Lloyds. Aux US : JPMorgan Chase, Bank of America, Wells Fargo, Citibank.

Les **banques privées** (private banking) servent une clientèle aisée à très aisée (seuils variables, souvent 1 M€+ d’actifs). Elles cumulent gestion de patrimoine, conseil patrimonial, fiscalité internationale. En Suisse : UBS, Credit Suisse historiquement (absorbé par UBS en 2023), Pictet, Julius Baer, Lombard Odier. Au Luxembourg : Banque de Luxembourg, BIL. Une partie significative des dossiers FININT touchant à la fraude fiscale ou à la corruption transnationale impliquent des banques privées.

Les **banques d’investissement** opèrent sur les marchés financiers, financent les grandes entreprises, structurent les fusions-acquisitions, émettent les obligations souveraines. Goldman Sachs, Morgan Stanley, J.P. Morgan, Deutsche Bank, BNP Paribas CIB, Rothschild & Co.

Les **banques correspondantes** (correspondent banks) jouent un rôle clé : elles permettent à des banques sans présence directe dans une juridiction d’y opérer en passant par elles. Quasiment toutes les grandes banques occidentales offrent ce service. C’est par ces points de passage que transite la majorité du commerce international et des paiements transfrontaliers.

Les **banques centrales** (BCE, Fed, BoE, BNS) régulent la masse monétaire, fixent les taux directeurs et opèrent les systèmes de règlement de gros (TARGET2 en zone euro, Fedwire aux US). Pour l’analyste FININT, leur intérêt opérationnel est limité, sauf en supervision et statistiques.

Les **banques offshore** sont des établissements implantés dans des juridictions à fiscalité réduite et à secret bancaire historique (chapitre 10). Beaucoup ont des relations correspondantes avec les banques internationales.

## L’utilité opérationnelle

Lire un flux suspect, c’est lire un parcours dans cette architecture.

Exemple : *« virement de 850 000 € depuis HSBC Hong Kong vers Crédit Agricole Île-de-France, transitant par Deutsche Bank Frankfurt »*. L’analyste voit immédiatement :

- une banque correspondante européenne (Deutsche Bank) — point de contrôle AML majeur ;
- un trajet HK → DE → FR — atypique pour un flux purement européen, ce qui interroge sur l’origine ;
- le passage par une banque privée à Hong Kong — clientèle particulière, vérifications KYC supposément renforcées.

Cette lecture en quelques secondes oriente les questions à poser au coordinateur du dossier.

## Méthode — décoder un flux à partir des codes BIC/IBAN

Tout virement bancaire transite par des banques identifiables via leurs **codes BIC (Bank Identifier Code)** SWIFT et les comptes via leurs **IBAN (International Bank Account Number)**.

**BIC** : 8 ou 11 caractères, structuré ainsi `AAAA BB CC XXX` :

- 4 lettres : code banque (ex : `BNPA` pour BNP Paribas, `CHAS` pour JPMorgan Chase, `DEUT` pour Deutsche Bank).
- 2 lettres : code pays ISO (ex : `FR`, `DE`, `US`, `GB`, `CH`).
- 2 caractères : code lieu/ville (ex : `PP` pour Paris, `LL` pour Londres).
- 3 caractères optionnels : code agence ou département.

**IBAN** : longueur variable selon le pays, structuré `[Pays 2 lettres][Clé contrôle 2 chiffres][Identifiant national bancaire]`. En France, l’IBAN fait 27 caractères ; en Lituanie 20 ; au Luxembourg 20 ; en Suisse 21.

Pour l’analyste, l’IBAN livre :

- le **pays** (premier indice : un IBAN LT ou EE pour un résident français en BTP, sans lien évident, est un signal contextuel) ;
- le **code banque** (les 5 caractères suivant la clé en France pointent l’établissement) ;
- le **type d’établissement** par recoupement (banque traditionnelle vs PSP/EME — chapitre 8).

Outils gratuits utiles : annuaires SWIFT BIC publics (sites de banques centrales, services en ligne), validateurs IBAN, tables ISO 9362 et ISO 13616.

## Mini-walkthrough

Un flux typique dans un dossier de TBML : *« 4 virements, libellés “trade payment”, 75 000 € à 95 000 € chacun, depuis IBAN AE [Émirats] via BIC HSBC Dubaï, passant par BIC HSBC Londres comme correspondant, vers IBAN FR d’une SAS de négoce agricole »*.

Lecture : (1) Émirats → UK → France, trajet avec étapes correspondantes en ligne avec les usages du commerce ; (2) HSBC est à la fois banque émettrice et correspondant — concentration sur un acteur donnant une bonne traçabilité par recoupement ; (3) montants tous sous le seuil de 100 000 € — pourrait être de la structuration intentionnelle ou un ordre de grandeur typique du secteur ; (4) libellés vagues, à creuser. Cette lecture rapide oriente la suite de l’analyse.

## Erreurs fréquentes

- **Confondre un IBAN national « exotique » avec une fraude.** Beaucoup de fintechs européennes (Revolut, Wise) opèrent depuis la Lituanie ou l’Estonie pour des raisons réglementaires parfaitement légales. Un IBAN LT n’est pas suspect en soi.
- **Ignorer la distinction banque émettrice / banque réceptrice / banques correspondantes.** Une « banque » sur un virement n’est jamais évidente : il peut y avoir 2 à 4 banques impliquées dans la chaîne.
- **Lire le BIC sans vérifier le réseau de l’établissement.** Une grande marque sur une plaque ne garantit pas que la filiale locale ait le même standard de conformité que la maison mère.

## Limites

L’analyse des codes ne dit rien sur l’**activité** bancaire (motifs réels du flux). Elle dit qui a transité, pas pourquoi. Le « pourquoi » exige les libellés, les contreparties, les volumes et le contexte économique du compte.

## Lien avec le fil rouge

> **CLEARFLOW — Lecture rapide des chaînes**
> 
> Sur un échantillon de 60 virements entrants, Nassim repère que 80 % transitent par seulement 3 banques correspondantes : Deutsche Bank (Francfort), JPMorgan Chase (Londres), HSBC (Hong Kong). C’est un indice de structuration de la chaîne de paiement choisie par le réseau. Cela oriente les coopérations : un signalement à BaFin (DE) et à FCA (UK) pourrait éclairer les pratiques de KYC sur les flux concernés.

## Points clés à retenir

- Le système bancaire est multi-strates : détail, privée, investissement, correspondant, centrale, offshore.
- Les banques correspondantes sont un point de passage — et de contrôle AML — majeur.
- Les codes BIC et IBAN permettent une lecture rapide des chaînes de paiement.
- Cette lecture oriente, mais ne conclut pas.

-----
