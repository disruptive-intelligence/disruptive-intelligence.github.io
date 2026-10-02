---
title: 'Chapitre 65 — Coopération internationale : Egmont, GAFI, Europol, FIU'
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie X — Cas historiques, coopération et professionnalisation
  - index.md
---

## Objectif

Maîtriser les **principaux canaux de coopération internationale** mobilisables dans une enquête FININT — leurs périmètres, leurs limites, leurs délais.

## Le concept

Aucune enquête FININT multi-juridictionnelle n’aboutit sans coopération. Plusieurs niveaux et canaux coexistent :

**Egmont Group** : réseau mondial des **Cellules de Renseignement Financier (CRF / FIU)**, créé en 1995, basé à Toronto. ~170 CRF membres. Coopération CRF-CRF par échange sécurisé via Egmont Secure Web (ESW). Demandes de renseignement, réponses, dissémination. Pas une autorité opérationnelle : un canal d’échange. Délais variables (jours à mois selon membres).

**FIU.NET** : réseau européen des CRF de l’UE et apparentés. Plus rapide et plus structuré qu’Egmont pour les coopérations UE. Adossé à Europol.

**GAFI / FATF** : organisme intergouvernemental (basé à Paris, OCDE), 40 recommandations sur LCB-FT, listes (noire, grise) des juridictions à risque, méthodologie d’évaluation. Pas un canal de coopération opérationnel, mais cadre normatif.

**Europol** : agence européenne de police, basée à La Haye. ECTC (Centre Européen Contre le Terrorisme), EC3 (Centre Européen de Cybercriminalité), EFECC (Centre Européen Économique et Financier). Coopération entre services nationaux d’enquête (police, gendarmerie).

**Interpol** : organisation mondiale de police, 196 États membres, basée à Lyon. Notices (red notice pour arrestation, blue notice pour information, etc.). Coopération entre forces de police nationales.

**Eurojust** : agence européenne de coopération **judiciaire** (procureurs, magistrats). Particulièrement utile pour l’asset recovery et les saisies transfrontalières.

**Parquet européen (EPPO)** : créé en 2021, compétent pour les infractions portant atteinte aux intérêts financiers de l’UE (fraude TVA, détournement de fonds européens, corruption transnationale). Procédure judiciaire harmonisée entre les 22 États membres participants.

**Réseau Camden Asset Recovery Inter-agency (CARIN)** : réseau informel pour l’asset recovery international.

**Conventions** :

- **Convention OCDE Anti-Corruption** (1997).
- **Convention ONU contre la Corruption** (Mérida, 2003).
- **Convention de Strasbourg** sur le blanchiment (1990, révisée Varsovie 2005).
- **Conventions bilatérales d’entraide judiciaire** (MLA — Mutual Legal Assistance).

## Méthode — choix du canal selon le besoin

- **Renseignement entre CRF** : Egmont (mondial), FIU.NET (UE).
- **Coopération policière** : Europol, Interpol.
- **Coopération judiciaire** : Eurojust, EPPO si compétence, MLA bilatéral.
- **Asset recovery** : CARIN, MLA, Eurojust, EPPO selon contexte.
- **Standards et normes** : GAFI (cadre, pas opération).

## Délais réalistes

- FIU.NET : quelques jours à 2 semaines pour réponse standard.
- Egmont : 1 à 8 semaines.
- MLA bilatéral : 3 à 18 mois (parfois plus).
- EPPO : variable, mais procédure intégrée plus rapide.
- Réquisitions judiciaires directes (sans MLA) : impossible dans la grande majorité des cas.

## Mini-walkthrough

Dans CLEARFLOW, Nassim mobilise :

- FIU.NET pour fintechs européennes (réponse 8-11 jours).
- Egmont avec Mokas Chypre (réponse 3 semaines, partielle).
- Egmont avec CRF émiratie (réponse 6 semaines, partielle).
- Egmont avec Liban : pas de réponse exploitable.
- Préparation d’une MLA franco-suisse pour gel et coopération bancaire (délai estimé 3-6 mois).

## Erreurs fréquentes

- **Confondre les canaux** : Interpol n’est pas une autorité judiciaire ; Egmont n’est pas une police.
- **Sous-estimer les délais** : un dossier qui dépend de 5 coopérations parallèles prend des mois.
- **Oublier les coopérations sectorielles** : douanes (OMD), fiscalité (OCDE), sanctions (OFAC liaisons).

## Limites

La qualité et la rapidité de coopération varient énormément. Certaines juridictions sont coopératives (Suisse, UK, Allemagne, Pays-Bas) ; d’autres beaucoup moins (Liban, certains pays en conflit, juridictions opaques).

## Points clés à retenir

- Egmont (CRF mondial), FIU.NET (CRF UE), Europol (police UE), Interpol (police mondiale), Eurojust + EPPO (judiciaire UE).
- Choix du canal selon objectif (renseignement / police / judiciaire / asset recovery).
- Délais réalistes à intégrer dans la planification.

-----
