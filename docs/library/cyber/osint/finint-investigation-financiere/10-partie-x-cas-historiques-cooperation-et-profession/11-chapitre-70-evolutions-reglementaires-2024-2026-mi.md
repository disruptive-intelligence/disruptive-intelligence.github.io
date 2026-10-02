---
title: 'Chapitre 70 — Évolutions réglementaires 2024-2026 : mise à niveau'
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie X — Cas historiques, coopération et professionnalisation
  - index.md
---

## Objectif du chapitre

Synthétiser les **principales évolutions réglementaires** qui structurent ou structureront le cadre du FININT et de la LCB-FT sur la période 2024-2026 et au-delà. Ce chapitre est conçu comme un **aide-mémoire évolutif** : il sera périmé partiellement à mesure que les textes s’appliquent ; l’analyste consulte les sources primaires (annexe N) pour la situation à date.

## 1. Le paquet AML européen et l’AMLA

L’**AML Package** européen a été publié au Journal officiel de l’UE le **19 juin 2024**. Il comprend principalement :

- **Le règlement AMLR** (Anti-Money Laundering Regulation) — règles harmonisées directement applicables.
- **La 6e directive AML** (AMLD6) — règles transposées par chaque État membre, encadrant notamment les supervisions nationales et les CRF.
- **Le règlement AMLA** — créant l’**Autorité européenne de lutte contre le blanchiment de capitaux et le financement du terrorisme** (AMLA), basée à Francfort.

**Frise chronologique simplifiée** :

- **19 juin 2024** : publication du paquet AML au JOUE.
- **26 juin 2024** : entrée en vigueur juridique de l’AMLA.
- **2025-2027** : montée en puissance institutionnelle de l’AMLA (recrutement, méthodes, sélection des entités).
- **À partir de 2028** : début de la **supervision directe** par l’AMLA des entités financières les plus risquées et complexes de l’UE (au nombre d’environ 40 selon les estimations en cours).
- **Parallèlement, jusqu’en 2027** : application progressive de l’AMLR et transposition d’AMLD6 dans les législations nationales.

**Conséquences opérationnelles pour l’analyste** :

- Harmonisation accrue des règles LCB-FT en UE.
- Standards de KYC, monitoring, déclaration de soupçon, vigilance renforcée plus convergents.
- Émergence de l’AMLA comme régulateur de référence pour les grandes institutions transfrontalières.
- Interconnexion européenne progressive des registres UBO (sous conditions strictes post-CJUE).
- Renforcement des coopérations entre CRF via FIU.NET et coordination AMLA.

## 2. Verification of Payee (VOP) et règlement Instant Payments

Le **règlement européen sur les paiements instantanés** introduit l’obligation, pour les PSP de proposer un **service de vérification du nom du bénéficiaire** (Verification of Payee — VOP) avant l’exécution d’un virement.

**Calendrier** :

- **PSP de la zone euro** : obligation opérationnelle à compter d’**octobre 2025**.
- **PSP hors zone euro** dans l’UE : obligation à compter de **juillet 2027**.

**Conséquences pour la fraude au virement (BEC, fraude au changement d’IBAN)** :

- Le VOP devient un **garde-fou systémique** : discrépance entre le nom du bénéficiaire affiché et le titulaire réel du compte IBAN renvoyée à l’émetteur avant exécution.
- Les fraudes type BEC voient leur efficacité réduite — sans la disparaître (les fraudeurs adaptent, créent des comptes au nom du fournisseur, exploitent les transitions, manipulent les utilisateurs).
- L’analyste FININT doit suivre la pratique réelle des PSP au moment de l’enquête.

## 3. Corporate Transparency Act (CTA) américain — trajectoire 2024-2025

Le **Corporate Transparency Act** de 2021 a connu une trajectoire **particulièrement instable** :

- 2024 : mise en œuvre démarrée par FinCEN. Obligation aux LLC et corporations US de déclarer leurs UBO à FinCEN.
- Fin 2024 - début 2025 : multiples décisions judiciaires contradictoires (injonctions, suspensions, levées).
- **Mars 2025 — interim final rule FinCEN** : les sociétés domestiques américaines (« domestic reporting companies ») sont **exemptées** de l’obligation de déclaration BOI à FinCEN. L’obligation **subsiste pour certaines entités étrangères enregistrées pour faire des affaires aux États-Unis**.
- Situation susceptible d’évolutions futures (contentieux, textes, administration).

**Conséquences pour l’analyste** :

- Les LLC Delaware, Wyoming, Nevada redeviennent quasi-totalement **opaques** sur l’UBO réel pour les analystes externes.
- L’accès à l’UBO de ces entités US passe presque exclusivement par les **enquêtes judiciaires** (réquisitions, coopérations DOJ).
- Vérifier l’état du droit FinCEN au moment de toute conclusion.

## 4. MiCA et basculement PSAN → CASP

Le règlement européen **MiCA (Markets in Crypto-Assets)** structure le marché européen des crypto-actifs.

**Calendrier** :

- **30 décembre 2024** : application aux nouveaux acteurs (désormais appelés **CASP** — Crypto-Asset Service Providers).
- **Jusqu’au 1er juillet 2026** : **période transitoire** pour les acteurs déjà enregistrés ou agréés PSAN sous le régime français PACTE (2019). Ils peuvent continuer leur activité dans l’attente de leur basculement sous MiCA.

**Conséquences** :

- Harmonisation européenne du régime des prestataires de services crypto.
- Conditions d’agrément renforcées (capital, gouvernance, KYC, custody, marchés).
- Pour l’analyste FININT : le périmètre des PSAN/CASP susceptibles d’opérer en France et en UE devient plus clair et plus encadré ; les coopérations avec ces acteurs se professionnalisent.
- À combiner avec le **Travel Rule** (TFR — Transfer of Funds Regulation, 2023, applicable 30/12/2024 en synchronie avec MiCA) qui impose la traçabilité des informations émetteur/bénéficiaire pour les transferts de crypto-actifs au-delà de seuils.

## 5. UBO post-CJUE : un paysage fragmenté

L’arrêt de la **CJUE du 22 novembre 2022** (affaires C-37/20 et C-601/20) a invalidé l’accès public généralisé aux informations UBO, au motif d’atteinte aux droits fondamentaux à la vie privée et à la protection des données.

**État du paysage 2025-2026** :

- **France (RBE)**, **Allemagne (Transparenzregister)**, **Luxembourg (RBE)**, **Pays-Bas (UBO-register)**, **Chypre**, etc. : accès public restreint. Accès maintenu pour autorités, assujettis LCB-FT, presse d’investigation sous conditions, professionnels avec intérêt légitime.
- **UK (PSC)** : non concerné par l’arrêt CJUE (hors UE depuis Brexit), reste **public et gratuit**.
- Variabilité d’application selon les États membres et les catégories d’acteurs.

**Conséquences** :

- L’analyste OSINT « grand public » a un accès **plus restreint** aux UBO européens qu’avant 2022.
- Les **journalistes d’investigation** peuvent dans certains pays bénéficier d’un accès au titre de l’intérêt légitime, sous conditions.
- L’**AMLA et l’interconnexion européenne** des registres devraient progressivement clarifier les modalités d’accès pour les catégories légitimes.

## 6. Sanctions : intensification post-2022

L’invasion russe de l’Ukraine (février 2022) a entraîné une **intensification massive et continue** des sanctions UE, US (OFAC), UK (OFSI), Suisse, Canada, Australie, Japon contre la Russie, la Biélorussie et des entités liées. Conséquences :

- Multiplication des paquets de sanctions UE (12+ depuis 2022).
- Renforcement OFAC, élargissement progressif.
- Accent sur le **contournement** via pays tiers (Émirats, Turquie, Géorgie, Asie centrale, Caucase).
- Mobilisation forte des CRF, douanes, banques sur ces flux.
- Création de cellules spécialisées dans plusieurs États (REPO Task Force aux US, gel d’avoirs UE).

L’analyste FININT a, depuis 2022, un **volet sanctions** quasi-systématique à intégrer dans les dossiers internationaux.

## 7. Veille à organiser

**Sources primaires à consulter régulièrement** (cf. annexe N — Bibliographie) :

- **GAFI / FATF** : recommandations, méthodologie, listes (noire, grise), rapports thématiques, mises à jour des typologies.
- **Egmont Group** : informations sur les coopérations, livrables annuels.
- **TRACFIN** : rapport annuel, tendances et analyses, points de vigilance, lignes directrices.
- **ACPR, AMF** : recommandations, sanctions publiques, lignes directrices LCB-FT.
- **DG Trésor — pôle sanctions financières internationales** : registre national des gels, communiqués sanctions.
- **FinCEN** : avis, alertes, mises à jour CTA, SAR statistics.
- **OFAC** : listes SDN, faqs, sanctions secondaires.
- **OFSI** : listes consolidées UK.
- **Commission européenne** : AML Package, MiCA, sanctions UE.
- **AMLA** (au fur et à mesure de sa montée en puissance) : méthodes de supervision, listes des entités sélectionnées.
- **Europol, Eurojust, EPPO** : rapports d’activité, tendances criminalité.
- **ICIJ, OCCRP** : leaks et investigations récentes.
- **Veille presse spécialisée** : Financial Times, Reuters, Bloomberg, Le Monde, Mediapart, OCCRP daily.

## Lien avec le fil rouge

> **CLEARFLOW — Pertinence des évolutions**
> 
> Pour le dossier Haddad, plusieurs évolutions ont un impact direct : (1) l’AMLA et l’interconnexion progressive des registres UBO pourraient, à terme, accélérer les recoupements multi-juridictionnels qui ont coûté à Nassim plusieurs semaines de coopérations bilatérales ; (2) la trajectoire instable du CTA US justifie d’avoir traité la LLC Delaware comme une zone d’opacité ; (3) l’environnement sanctions post-2022 explique la vigilance accrue sur les flux Turquie ; (4) le VOP réduira (mais n’éliminera pas) la vulnérabilité aux BEC type ALPHA INDUSTRIE.

## Points clés à retenir

- Paquet AML UE 2024 + AMLA opérationnelle à partir de 2028 (supervision directe).
- VOP obligatoire : oct. 2025 (zone euro), juill. 2027 (hors zone euro).
- CTA US : exemption des sociétés domestiques depuis mars 2025.
- MiCA en application 30/12/2024 ; transition PSAN→CASP jusqu’au 01/07/2026.
- UBO post-CJUE : paysage fragmenté, vérifier au cas par cas.
- Sanctions post-2022 : volet systématique des dossiers internationaux.
- Veille indispensable sur sources primaires.

-----
