---
title: 'Chapitre 18 — Leaks financiers : ICIJ, OCCRP, Aleph, Panama/Pandora'
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie III — Sources OSINT financières
  - index.md
---

## Objectif du chapitre

Maîtriser l’usage des **leaks financiers majeurs** comme source d’enquête FININT. Les leaks ne sont pas la totalité du métier, mais ils sont devenus une source de référence pour les structures opaques offshores et certaines révélations sectorielles.

## Le concept

Un **leak** est une fuite documentaire massive d’informations financières, généralement :

- issue d’un cabinet juridique, fiduciaire ou d’une institution financière ;
- obtenue par un lanceur d’alerte ou un hack ;
- transmise à un consortium de journalistes (ICIJ ou OCCRP étant les plus connus) qui en mène l’analyse coordonnée et la publication.

Ces leaks ont **changé** le paysage du FININT en rendant accessible (avec des limites — voir infra) une partie des structures historiquement opaques (BVI, Panama, Bahamas, etc.).

## Les principaux leaks et bases

**Panama Papers (2016)** — fuite de 11,5 millions de documents du cabinet Mossack Fonseca (Panama). Origine : un lanceur d’alerte anonyme (« John Doe ») au journaliste allemand Bastian Obermayer (Süddeutsche Zeitung), partagé avec ICIJ. Conséquence : révélation massive de structures offshores liées à des PEP, des hommes d’affaires, des criminels organisés. La base [Offshore Leaks](https://offshoreleaks.icij.org/) de l’ICIJ regroupe les structures identifiées et est consultable publiquement par nom.

**Paradise Papers (2017)** — fuite du cabinet Appleby (Bermudes) et de divers fournisseurs. ICIJ. Inclus dans la base Offshore Leaks.

**Pandora Papers (2021)** — fuite combinée de 14 prestataires offshore. ICIJ. Près de 12 millions de documents. Particulièrement riche sur les UBO et les bénéficiaires de trusts. Inclus dans la base Offshore Leaks.

**FinCEN Files (2020)** — fuite de SAR (Suspicious Activity Reports) américains. Différent des autres leaks : il s’agit de signalements internes de banques au régulateur US. Coordonné par BuzzFeed et ICIJ. Couvre 2 trillions USD de transactions suspectes.

**Suisse Secrets (2022)** — fuite de comptes Credit Suisse, coordonnée par OCCRP et plusieurs journaux européens.

**Cyprus Confidential (2023)** — fuite portant sur des prestataires de services chypriotes, ICIJ.

**Russian Asset Tracker (2022+)** — base OCCRP sur les actifs des oligarques russes sous sanctions.

**OCCRP Aleph** — plateforme **agrégée** de l’OCCRP qui regroupe des leaks, registres ouverts, sanctions, et bases de données journalistiques. Devenue une référence pour les analystes, accessible via partenariat avec OCCRP. Recherche unifiée, très utile.

**Aleph (instance ICIJ)** — moteur de recherche sur l’écosystème ICIJ. Accès journalistique principalement.

**Smaller leaks** : Bahamas Leaks (2016), Lux Leaks (2014), Swiss Leaks (HSBC, 2015), Malta Files, Glencore Leak, etc.

## L’utilité opérationnelle

Pour un analyste FININT, les leaks permettent :

1. **Identification de structures cachées** : une société BVI dont l’UBO n’est pas accessible en registre peut figurer dans Panama/Pandora avec ses bénéficiaires.
1. **Recoupement de réseaux** : les liens entre personnes via des trusts ou des fondations sont souvent visibles dans les documents leakés.
1. **Profilage de prestataires** : certains cabinets de domiciliation ou trust companies apparaissent récurremment dans des dossiers à risque.
1. **Documentation historique** : les leaks couvrent souvent des périodes anciennes — utile pour reconstituer l’historique d’un montage.

## Méthode — workflow leaks

1. **Recherche par nom de personne** dans Offshore Leaks (ICIJ) — gratuit, public.
1. **Recherche par nom de société** dans Offshore Leaks.
1. **Recherche dans Aleph (OCCRP)** si accès — agrège plus largement.
1. **Recherche dans les archives journalistiques** publiées (les articles ICIJ/OCCRP sont publics avec une partie des sources).
1. **Vérification croisée** : un nom dans un leak n’est pas un fait avéré — c’est un document supposé authentique. La présence ne vaut pas culpabilité (la détention d’une société offshore peut être parfaitement légale).
1. **Documentation** : capture, référence à l’article ou à la base, date de consultation.

## Mini-walkthrough — Pandora dans CLEARFLOW

- Recherche dans Offshore Leaks par « Karim Haddad » : 1 résultat — un trust chypriote enregistré en 2019, dont le settlor est nommé Karim Haddad, et dont les bénéficiaires incluent une SAS française et une LLC Delaware (toutes deux du réseau du dossier).
- Recherche par « OMEGA HOLDINGS » : 2 résultats — la société chypriote elle-même + une mention dans une entité liée à Beyrouth.
- Aleph (OCCRP) : recoupement avec un article OCCRP de 2023 sur les flux entre Liban et Afrique de l’Ouest, mentionnant un homme d’affaires correspondant à Haddad sans le nommer.
- Calibration : la présence dans Pandora est *quasi-certaine* (document authentique, attribution claire). L’usage du trust pour des fins illicites n’est pas démontré par le seul leak — il est *compatible* avec, et nécessite recoupement des flux et de l’activité.

## Erreurs fréquentes

- **Présence dans un leak = culpabilité.** Non. La détention d’une structure offshore peut être parfaitement légale (planification successorale, protection patrimoniale légitime, résidence à l’étranger).
- **Leak = source primaire complète.** Les leaks sont des extraits limités à ce qu’a obtenu le lanceur d’alerte. Ils peuvent omettre des éléments cruciaux.
- **Leak = preuve admissible.** En cadre judiciaire, l’admissibilité dépend du droit national et de l’origine. Certaines décisions (CEDH, en particulier) admettent les preuves issues de leaks sous conditions, d’autres non.
- **Surinterpréter une similitude de nom.** Un Karim Haddad dans un leak peut être un homonyme — vérifier les autres champs (date de naissance, adresse, autres mandats).

## Limites

Les leaks sont **datés** : ils reflètent un instant. Une société leakée en 2016 peut avoir été liquidée en 2018, ou son UBO peut avoir changé. Les leaks couvrent les juridictions dont les prestataires ont été leakés — d’autres juridictions restent dans l’ombre. L’accès complet aux bases (au-delà des recherches publiques) est généralement réservé à la presse partenaire.

## Lien avec le fil rouge

> **CLEARFLOW — Le leak comme accélérateur**
> 
> Sans le hit Pandora, l’identification de Haddad comme settlor du trust chypriote aurait demandé une coopération via Egmont avec Mokas — délai de plusieurs semaines, sans garantie. Le leak fournit *gratuitement* en quelques minutes une information dont la valeur opérationnelle est élevée. Nassim documente le hit et le qualifie *probable* à *quasi-certain* selon les recoupements. Cette information sera l’un des **piliers** de l’hypothèse centrale du dossier (chapitre 64).

## Points clés à retenir

- Panama, Paradise, Pandora, FinCEN Files, Suisse Secrets : leaks majeurs.
- Offshore Leaks (ICIJ) et Aleph (OCCRP) : bases consultables.
- Présence dans un leak ≠ culpabilité ; mais signal de structure offshore avérée.
- Les leaks accélèrent considérablement les enquêtes sur les juridictions opaques.
- Vérification croisée et calibration de la confiance impératives.

-----
