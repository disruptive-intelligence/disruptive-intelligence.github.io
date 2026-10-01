---
title: Annexe M — Cadres d’accès aux sources
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Annexes
  - index.md
---

*Tableau de synthèse pour clarifier, à chaque consultation, qui peut accéder à quoi. Le FININT mobilise plusieurs cadres ; les confondre crée des erreurs juridiques et déontologiques.*

|Type de source                       |Exemples                                                                                                                                                                           |Accessible par                                                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|**OSINT public gratuit**             |Pappers (gratuit), Companies House UK, OpenCorporates, OpenSanctions, ICIJ Offshore Leaks, DVF, BODACC, BOAMP, presse                                                              |Tout analyste, journaliste, cabinet, étudiant, particulier. Pas de restriction d’usage hors RGPD et droit.                                         |
|**OSINT freemium**                   |Pappers Premium, MarineTraffic Premium, agrégateurs partiellement payants                                                                                                          |Tout analyste ayant un compte payant. Conditions d’utilisation à respecter.                                                                        |
|**Sources professionnelles payantes**|Sayari, Orbis (Moody’s/BvD), Dun & Bradstreet, World-Check (LSEG), Dow Jones Risk & Compliance, LexisNexis Bridger / Diligence, Factiva, Bloomberg, Refinitiv Eikon, S&P Capital IQ|Organisations abonnées (banques, cabinets, institutions). Licence individuelle ou entreprise.                                                      |
|**Sources assujetti LCB-FT**         |KYC interne, monitoring transactions, données clientèle, droits de communication LCB-FT                                                                                            |Banques, PSP, assurances, casinos, notaires, avocats sous condition, agents immobiliers, etc. Cadre de la 5e/6e directive AML et CMF.              |
|**Sources CRF (FIU)**                |DS reçues, FIU.NET, Egmont Secure Web, coopérations CRF étrangères, droits de communication CRF (CMF)                                                                              |TRACFIN et CRF homologues uniquement. Cadre légal strict (CMF, lois LCB-FT).                                                                       |
|**Sources judiciaires**              |Réquisitions bancaires, FICOBA, FICOVIE, FIBEN (sous condition), perquisitions, auditions, MLA, EAR/CRS via DGFiP, écoutes (sous mandat)                                           |Magistrats (juge d’instruction, procureur) ; policiers et gendarmes sous procédure ; officiers de police judiciaire mandatés. Cadre du CPP.        |
|**Sources fiscales et douanières**   |DGFiP (DNEF), DGDDI, échanges fiscaux internationaux (DAC, EAR/CRS), bases douanières internes                                                                                     |Administrations fiscales et douanières. Coopération inter-administrations sur cadre légal.                                                         |
|**Sources sanctions**                |Listes OFAC SDN, listes UE consolidées, listes ONU, OFSI, registre national des gels DG Trésor                                                                                     |Public pour consultation des listes. Action de gel : autorités compétentes (DG Trésor — pôle sanctions financières en France).                     |
|**Sources HATVP**                    |Déclarations d’intérêts et de patrimoine publiques (selon fonctions et seuils)                                                                                                     |Public selon les fonctions concernées et les seuils. Pas toutes les fonctions publiques sont couvertes de la même manière (selon les seuils HATVP).|
|**Sources presse / leaks**           |ICIJ Aleph (accès journalistique principal), OCCRP Aleph, Pandora Papers via ICIJ portal                                                                                           |Journalistes partenaires (Aleph complet) ; public pour la version publique des leaks ; analystes peuvent consulter le portail public.              |
|**Sources OSINT Crypto**             |Etherscan, Tronscan, Chainalysis Reactor, TRM Labs, Elliptic, Breadcrumbs                                                                                                          |Public pour explorers ; abonnés pour outils pro. Cadre à vérifier selon les juridictions.                                                          |

**Règles essentielles** :

1. **Ne pas confondre OSINT et sources fermées** : un analyste OSINT pur ne dispose pas de FICOBA, EAR/CRS, FIU.NET. Il doit l’expliciter dans tout livrable.
1. **Cadre du dossier détermine les sources accessibles** : un dossier de due diligence cabinet ≠ dossier CRF ≠ dossier judiciaire. Ne pas mobiliser des sources hors périmètre.
1. **Documenter la source de chaque élément** : la chain of custody (chapitre 53) impose la traçabilité de la provenance.
1. **RGPD applicable** : pour les données personnelles, vérifier la base légale, la finalité, la conservation, les droits des personnes.
1. **Secret professionnel** : pour les CRF, magistrats, policiers, avocats, le secret applicable limite la diffusion.

Cette annexe est l’**amélioration pédagogique la plus importante** du cours : elle clarifie, pour chaque chapitre et chaque source citée, qui peut effectivement y accéder. À chaque mobilisation d’une source dans un livrable, l’analyste se demande : *« Mon cadre d’exercice m’autorise-t-il à utiliser cette source ? »*

-----
