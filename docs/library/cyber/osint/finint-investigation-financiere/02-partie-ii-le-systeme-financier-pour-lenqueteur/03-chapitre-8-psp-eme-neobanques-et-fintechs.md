---
title: Chapitre 8 — PSP, EME, néobanques et fintechs
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie II — Le système financier pour l’enquêteur
  - index.md
---

## Objectif du chapitre

Comprendre l’écosystème des **prestataires de services de paiement** (PSP), des **établissements de monnaie électronique** (EME), des **néobanques** et des **fintechs** : ce qu’ils sont, comment ils sont régulés, où ils se situent dans la chaîne de paiement, et pourquoi ils figurent souvent dans les schémas modernes de blanchiment et de fraude.

## Le concept

Le paysage est complexe et évolutif. Quelques distinctions clés.

Un **PSP** (Payment Service Provider) est un acteur agréé pour fournir des services de paiement (initiation, exécution, encaissement). Sa surface réglementaire est définie par la directive PSD2 (et bientôt PSR/PSD3). Tous les acteurs émettant des instruments de paiement ou opérant des comptes de paiement sont, à un titre ou un autre, PSP. Exemples : Stripe, Adyen, Worldline, PayPal, Mangopay, Lemon Way.

Un **EME** (Établissement de Monnaie Électronique) est agréé spécifiquement pour émettre de la monnaie électronique (e-money). Sa réglementation découle de la directive 2009/110/CE. Beaucoup de néobanques et fintechs sont juridiquement des EME plutôt que des banques. Exemples historiques : Revolut (initialement EME au UK puis banque), Wise (anciennement TransferWise — EME), Anytime, Qonto.

Une **néobanque** est une banque (ou EME ou hybride) opérant principalement en ligne, sans réseau d’agences physiques. Par abus de langage, le mot recouvre des statuts variés. N26 (banque allemande), Revolut (banque lituanienne pour ses comptes EU), Bunq (banque néerlandaise), Monzo et Starling (banques UK).

Une **fintech** est un terme générique qui désigne toute entreprise technologique opérant dans la finance — peut être un PSP, un EME, une néobanque, un agrégateur, un courtier, un assureur. Le terme n’a pas de portée réglementaire propre.

## L’utilité opérationnelle

Pourquoi ces acteurs concentrent l’attention FININT ?

**Onboarding rapide et 100 % digital.** Création de compte en quelques minutes via un smartphone, vérification d’identité automatisée. Cela permet à un fraudeur de créer rapidement plusieurs comptes (ou à un prête-nom de faciliter cela), beaucoup plus difficilement qu’avec une banque traditionnelle.

**Vitesse des opérations.** Virements instantanés intra-réseau (Revolut → Revolut), conversions multi-devises en un clic, virements internationaux à coût faible. Le **layering** se fait en heures, là où le circuit traditionnel prenait des jours.

**Effectifs compliance plus tendus.** Beaucoup de PSP/EME ont scalé leur base clients très rapidement et leurs équipes compliance moins. Conséquences observables : taux d’alerte traités en backlog, faux négatifs, parfois des sanctions ACPR/FCA/BaFin.

**IBANs « exotiques ».** Revolut (LT), Wise (BE/UK selon les comptes), N26 (DE), Bunq (NL), etc. La réglementation européenne facilite le passporting : une fintech agréée en Lituanie peut opérer dans toute l’UE. Un IBAN LT pour un résident français n’est pas suspect en soi (surtout depuis Revolut, Wise, etc.) — c’est l’absence de cohérence avec l’activité du compte qui peut l’être.

**Cartes prépayées.** Certaines fintechs émettent des cartes prépayées (rechargeables en ligne, parfois anonymes sous certains seuils dans certaines juridictions). Vecteur de placement et de cashout.

**Intégration native crypto.** Plusieurs fintechs proposent l’achat-vente de cryptos directement dans leur application (Revolut, Bitpanda en partenariat). Le passage fiat-crypto se fait sans changer d’environnement, ce qui complique la chaîne de surveillance (chapitre 48 et OSINT Crypto).

## Méthode — lire un flux fintech

Un flux passant par une fintech présente des spécificités :

1. **L’IBAN du compte fintech** est dans le pays de licence (LT pour Revolut, BE pour Wise, DE pour N26, NL pour Bunq). Le titulaire peut être résident dans n’importe quel pays UE (passporting).
1. **Les libellés sont parfois plus pauvres** que dans la banque traditionnelle, mais s’améliorent (depuis ISO 20022).
1. **Les transferts intra-réseau** (Revolut → Revolut, par username ou tag) ne laissent pas de trace SEPA visible aux contreparties extérieures — il faut une réquisition pour les obtenir.
1. **Les conversions multi-devises** apparaissent sur le relevé (par exemple : EUR → USD interne, puis virement USD).

L’analyste qui rencontre un flux passant par une fintech doit :

- Identifier précisément le statut juridique et l’agrément (banque, EME, PSP, et pays).
- Identifier l’autorité de supervision (ACPR pour France, BaFin pour Allemagne, Bank of Lithuania, FCA pour UK, Bank of Lithuania pour la majorité des comptes Revolut européens, etc.).
- Pour les sollicitations bancaires (réquisitions, droits de communication), passer par le canal compétent (banque licence-holder).

## Mini-walkthrough

Un cas BEC : *« 215 000 € transitent depuis une PME française par 4 comptes Revolut (LT) → Wise (BE) → N26 (DE) → Bunq (NL) en 2 heures, avant conversion crypto »*.

Lecture FININT :

- Layering rapide multi-fintech, profil typique des fraudes BEC modernes.
- Quatre juridictions de licence, donc quatre coopérations potentielles avec les autorités locales (Banque de Lituanie, Banque nationale de Belgique, BaFin, DNB).
- Dans la pratique opérationnelle : la coopération via les autorités prend du temps. La réactivité passe par la **CRF** qui peut activer des canaux plus directs avec les compliance des fintechs concernées (FIU.NET en EU).
- Renvoi crypto pour la suite : vers Sarah Marin / OSINT Crypto.

## Erreurs fréquentes

- **Considérer toutes les fintechs comme « suspectes ».** Elles sont des outils financiers majeurs et largement légitimes. Le profil de risque dépend de l’usage par l’utilisateur, pas de la marque.
- **Ne pas distinguer banque / EME / PSP.** Cela change le cadre réglementaire et la liste des autorités à solliciter.
- **Croire qu’un IBAN LT/EE/BE est nécessairement « offshore ».** Ces IBANs sont européens et soumis à la réglementation UE complète.
- **Sous-estimer la richesse des données fintech.** Les fintechs ont souvent des **logs très détaillés** (géolocalisation des sessions, device fingerprinting, IP) — exploités sur réquisition, ils sont parfois plus utiles que les relevés bancaires classiques.

## Limites

La supervision peut varier en maturité d’une autorité nationale à l’autre. La **réactivité** dans la coopération aussi. L’analyste qui dépend de la coopération transfrontalière entre fintechs note les délais réels (parfois des semaines pour des demandes pourtant urgentes).

## Lien avec le fil rouge

> **CLEARFLOW — Branche fintech**
> 
> Plusieurs flux du dossier Haddad transitent par des comptes Wise (au nom d’une société chypriote, IBAN BE). Nassim demande à la CRF de solliciter — via FIU.NET — les KYB associés (qui contrôle le compte ?), les logs de session (depuis où sont effectuées les opérations ?), et les patterns de transferts intra-Wise qui ne seraient pas visibles sur les relevés bancaires classiques. La réponse arrive en 11 jours — ce qui, pour une coopération européenne, est un délai correct.

## Points clés à retenir

- PSP / EME / néobanque / fintech : termes recouvrant des statuts juridiques variés.
- L’écosystème est largement légitime ; l’attention FININT cible des **usages** spécifiques.
- Layering rapide, IBAN passportés, intégration crypto, cartes prépayées : facteurs typiques.
- La coopération exige d’identifier l’autorité de supervision compétente et le bon canal d’instruction.

-----
