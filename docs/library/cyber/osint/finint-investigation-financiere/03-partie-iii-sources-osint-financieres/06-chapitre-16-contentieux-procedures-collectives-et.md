---
title: Chapitre 16 — Contentieux, procédures collectives et sanctions administratives
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Mobiliser les **données de contentieux et de procédures** comme indicateurs de risque, de tension, ou d’historique d’anomalies. Une société ou une personne avec un passif contentieux significatif n’est pas nécessairement coupable — mais elle a un historique à intégrer.

## Le concept

Plusieurs catégories de données :

**Procédures collectives** (sauvegarde, redressement judiciaire, liquidation judiciaire). En France : BODACC, Infogreffe. Au UK : The Gazette. Dans la majorité des juridictions, ces procédures sont publiques.

**Décisions de justice publiées** : selon les juridictions, certaines décisions sont publiées (avec ou sans anonymisation). En France : Légifrance, Doctrine, Dalloz, Lexbase. Plateformes payantes pour certains accès. Open data judiciaire en cours (depuis le décret « open data des décisions »).

**Sanctions administratives** :

- **AMF** (Autorité des marchés financiers) — sanctions sur les acteurs des marchés financiers en France.
- **ACPR** (Autorité de contrôle prudentiel et de résolution) — sanctions sur les banques, assurances, PSP, EME.
- **Commission des sanctions de l’AMF**, idem ACPR : décisions publiées.
- **CNIL** : sanctions RGPD.
- **Autorité de la concurrence**.
- Équivalents européens : ESMA, EBA, EIOPA.
- **OFAC**, **OFSI**, **DG Trésor — pôle sanctions financières internationales** : sanctions liées aux sanctions économiques.
- **SEC**, **DOJ**, **CFTC** aux US.

**Cybercrime / fraude** : décisions condamnatoires, signalements ANSSI, etc. (croisement CTI / FININT).

**Contentieux fiscaux** : majorations, redressements publiés, contentieux administratif.

## L’utilité opérationnelle

Pour l’analyste :

- Une **procédure collective récente** sur une contrepartie est un signal de risque ;
- Un **passif contentieux** chargé sur un dirigeant ou une société est un facteur de réputation ;
- Une **sanction AMF/ACPR** sur un acteur financier renseigne sur ses pratiques antérieures ;
- Une **condamnation pénale** publique antérieure (selon les juridictions) est un facteur clé.

L’analyste construit ainsi une **fiche réputationnelle** pour chaque acteur clé.

## Méthode — workflow rapide

1. **France** :
- BODACC pour les procédures collectives.
- Légifrance / Doctrine pour les décisions publiées.
- Site AMF (commission des sanctions) et site ACPR.
- Site Direction Générale du Trésor pour les sanctions économiques.
- Presse et adverse media (chapitre 17) pour les affaires non encore jugées ou anonymisées.
1. **UK** :
- The Gazette pour insolvency.
- BAILII et Caselaw.uk pour décisions.
- FCA register pour sanctions.
1. **US** :
- PACER (federal court records, payant).
- SEC press releases.
- DOJ press releases.
- CFTC.
- State courts.
1. **International** : ICIJ Aleph, OCCRP archives (chapitre 18).

## Mini-walkthrough

Sur le dirigeant Monsieur X (gestionnaire des SAS françaises liées à Haddad) :

- BODACC : 2 procédures collectives sur des sociétés antérieurement dirigées par M. X (liquidations 2018 et 2020).
- Légifrance : pas de décision publique le concernant directement.
- AMF/ACPR : non.
- Presse : un article de 2019 mentionne sa mise en cause dans une affaire de carrousel TVA (instruction en cours, présomption d’innocence).

Conclusion : profil avec **historique contentieux significatif**, à mentionner dans la fiche personne (chapitre 27) avec niveau de confiance approprié et précautions sur la présomption d’innocence.

## Erreurs fréquentes

- **Confondre instruction et condamnation.** La présomption d’innocence est un principe — l’analyste ne diabolise pas un mis en examen.
- **Ignorer les anonymisations.** Beaucoup de décisions modernes sont anonymisées (initials des parties) — l’identification exige souvent croisement.
- **Surinterpréter une procédure collective.** Beaucoup d’entreprises échouent sans fraude.

## Limites

Beaucoup de contentieux ne sont pas publics, notamment dans les juridictions opaques. Les contentieux fiscaux sont rarement publics dans le détail. La donnée est donc **indicative**, pas exhaustive.

## Lien avec le fil rouge

> **CLEARFLOW — Historique contentieux**
> 
> Le profil contentieux du réseau Haddad : 2 procédures collectives passées sur des sociétés du même gestionnaire (Monsieur X), une enquête fiscale française antérieure sur Haddad lui-même (réglée par transaction fiscale, presse 2018), aucune sanction AMF/ACPR. Le profil n’est pas immaculé. Cela alimente la fiche personne et oriente la priorisation du dossier.

## Points clés à retenir

- BODACC, Légifrance, AMF, ACPR, presse — sources clés en France.
- Présomption d’innocence à respecter dans tout livrable.
- Historique contentieux = facteur réputationnel, pas une preuve.
- Beaucoup d’angles morts (anonymisation, confidentialité, juridictions opaques).

-----
