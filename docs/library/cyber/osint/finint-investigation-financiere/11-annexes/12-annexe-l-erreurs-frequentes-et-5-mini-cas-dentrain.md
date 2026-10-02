---
title: Annexe L — Erreurs fréquentes et 5 mini-cas d’entraînement
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Annexes
  - index.md
---

## Top 12 erreurs fréquentes en FININT

1. **Conclure sur 2 attributs faibles** pour identifier une personne (homonymie).
1. **Confondre dénomination commerciale et dénomination sociale** (sociétés homonymes).
1. **Surinterpréter une présence dans un leak** sans qualification de la nature de la structure.
1. **Considérer toute société écran comme illégale** (beaucoup d’usages légitimes).
1. **Conclure « prête-nom » sans recoupement** (un cumul d’indices est nécessaire).
1. **Ignorer la cohérence sectorielle** lors de l’analyse comptable.
1. **Surcharger un graphe** au point de le rendre illisible.
1. **Confondre lien fort et contrôle** : co-présence dans un CA ne dit pas qui contrôle.
1. **Vocabulaire affirmatif sans calibration** : « il blanchit », « c’est l’UBO » sans WEP.
1. **Sous-estimer les délais** des coopérations internationales.
1. **Refaire OSINT Crypto** dans la note FININT au lieu de renvoyer au partenaire.
1. **Pas de mention des lacunes** : la note lisse trompe le lecteur.

## 5 mini-cas d’entraînement

*Cas courts à traiter mentalement ou sur tableur, avec correction synthétique en fin.*

### Mini-cas 1 — La SAS opportune

Une SAS française est créée il y a 6 mois. Capital 1 €. Président : un homme de 78 ans, ancien employé d’un garage automobile. Activité déclarée : « commerce de gros non spécialisé ». Domiciliation : cabinet parisien (89 autres entités). Sur 6 mois, CA déclaré (estimation via flux observables fournis) : 1,8 M€.

Que concluez-vous, et que faites-vous ?

*Éléments de réponse* : profil de signaux convergents (création récente, capital symbolique, dirigeant à profil incohérent, domiciliation cluster, CA disproportionné). Société probablement écran ou utilisée pour un schéma spécifique. Investigation : profil du dirigeant (fronting probable), flux observables (typologie), contreparties (cohérence sectorielle), liens à d’autres entités. À ce stade, qualification *probable* écran ; finalité (TBML, fraude TVA, BEC, blanchiment) *indéterminable* sans investigation des flux.

### Mini-cas 2 — Le virement urgent

Le DAF d’une PME reçoit un email du président, depuis l’adresse habituelle, demandant un virement urgent et confidentiel de 480 K€ vers un IBAN slovaque pour finaliser une « acquisition stratégique ». Le DAF s’apprête à valider.

Que doit-il faire ?

*Éléments de réponse* : pattern classique de fraude au président. À faire : vérification téléphonique du président (sur numéro connu, pas celui de l’email), validation par double signature, vérification VOP de la cohérence nom bénéficiaire / titulaire IBAN, suspension du virement si moindre doute. Si fraude avérée et virement effectué : contact immédiat banque (gel), plainte, FININT/CRF.

### Mini-cas 3 — Le marché public favori

Une PME du BTP remporte 12 marchés publics consécutifs dans une commune sur 4 ans, pour un total de 18 M€. La PME est dirigée par un cousin de l’adjointe aux travaux de la commune.

Que regardez-vous, et que concluez-vous ?

*Éléments de réponse* : pattern de favoritisme probable. Vérifications : conditions d’attribution (mode de passation, critères, concurrence réelle), valeur des marchés vs marché, déclarations d’intérêts de l’adjointe (HATVP, déport), liens familiaux confirmés. Si tout converge : signalement à l’AFA (Agence Française Anticorruption) et au PNF. Qualification *probable* favoritisme et prise illégale d’intérêts à ce stade ; *quasi-certain* sous condition de confirmation des éléments.

### Mini-cas 4 — Le client PEP

Une banque privée européenne reçoit pour client un ancien ministre africain ayant déposé 8 M€ sur 6 mois, présentés comme produit de cessions d’actifs personnels. La documentation justificative est partielle.

Quelle posture pour la banque ?

*Éléments de réponse* : statut PEP confirmé → vigilance renforcée. Documentation insuffisante = obstacle au monitoring. Demande de justificatifs complets (déclarations fiscales, contrats de cession, identification des acquéreurs). Sans documentation satisfaisante : DS à la CRF, évaluer rupture commerciale. La présomption d’innocence du client demeure ; la banque ne décide pas de la culpabilité — elle décide de sa propre exposition.

### Mini-cas 5 — Le pattern crypto

Un dossier en cours montre des conversions répétées EUR → USDT sur fintech européenne, puis transferts USDT vers wallets externes via plusieurs adresses. La banque sollicite votre analyse.

Comment procédez-vous ?

*Éléments de réponse* : FININT cadre (contexte client, comptes alimentant la fintech, motif déclaré). OSINT Crypto (partenaire ou interne) trace on-chain les USDT depuis dépôt sur fintech jusqu’aux off-ramps ou usages. Synthèse intégrée. Renvoi explicite vers OSINT Crypto pour les méthodes et résultats détaillés. La note FININT n’essaie pas de refaire l’analyse on-chain.

-----
