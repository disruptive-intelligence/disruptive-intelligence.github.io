---
title: Chapitre 37 — Cadre juridique et éthique
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 7 — OPSEC humaine, opérationnelle et continuité
  - index.md
---

> **Note** : cette section est informative et générale, pas un avis juridique. Le droit évolue rapidement (Chat Control, AI Act, transpositions diverses). En cas d’enjeu réel, consulter un avocat spécialisé.

## 37.1 Vie privée et CEDH article 8

L’article 8 de la Convention européenne des droits de l’homme garantit le droit au respect de la vie privée et familiale, du domicile et de la correspondance. Restrictions admises sous trois conditions cumulatives :

- **Prévue par la loi**.
- **Légitime** (sécurité nationale, ordre public, etc.).
- **Nécessaire dans une société démocratique** (proportionnée).

Jurisprudence CEDH abondante. Toute mesure de surveillance massive doit passer ce triple test ; plusieurs régimes nationaux ont été retoqués (UK GCHQ, France IOC, etc.).

## 37.2 RGPD : droits utilisables

Articles directement utilisables par un individu :

- **Article 15** : droit d’accès. Tu peux demander à tout responsable de traitement quelle donnée il détient sur toi.
- **Article 17** : droit à l’effacement (« droit à l’oubli »).
- **Article 21** : droit d’opposition au traitement.
- **Article 20** : droit à la portabilité.

Recours : CNIL (FR), équivalent national (APD en Belgique, AEPD en Espagne, etc.), avec amendes croissantes en cas de violation.

## 37.3 LCEN : chiffrement libre en France

L’article 30 de la loi sur la confiance dans l’économie numérique (LCEN, 2004) consacre la liberté d’usage des moyens de cryptologie en France. Le chiffrement personnel est **légal et garanti**. L’État ne peut pas l’interdire pour l’usage privé.

Limites : obligations de déclaration pour les fournisseurs de moyens de cryptologie ; régime spécifique pour l’exportation ; obligation de déchiffrer sur réquisition judiciaire (cf. 37.5).

## 37.4 Secret des sources des journalistes

Loi française du 4 janvier 2010 sur la protection du secret des sources : pas d’atteinte au secret des sources sans impératif prépondérant d’intérêt public, et selon procédures strictes.

Règlement (UE) 2024/1083 dit *European Media Freedom Act* (EMFA) : renforcement, harmonisation européenne, encadrement strict de l’usage du spyware contre journalistes, droit d’opposition à la révélation des sources, protection contre les pressions économiques sur les rédactions. Le texte n’est pas une directive (qui aurait laissé une marge de transposition nationale) mais un règlement directement applicable.

**En pratique** : protégé en droit, mais des affaires (Édouard Tétreau, Le Monde, Mediapart vs renseignement) ont montré les fragilités. L’OPSEC technique du journaliste reste un complément indispensable à la protection légale.

## 37.5 Obligation de remettre une convention secrète de déchiffrement

Cas français : l’article 434-15-2 du Code pénal sanctionne le **refus de remettre aux autorités judiciaires une convention secrète de déchiffrement d’un moyen de cryptologie susceptible d’avoir été utilisé pour préparer, faciliter ou commettre un crime ou un délit**. Peines : trois ans d’emprisonnement et 270 000 € d’amende ; aggravées à cinq ans et 450 000 € si le refus a empêché la prévention d’un crime ou délit.

Le Conseil constitutionnel a, à plusieurs reprises (notamment 2018 et 2025), validé le dispositif sous réserves d’interprétation, en précisant notamment les conditions dans lesquelles ce délit peut être retenu. La jurisprudence reste cependant nuancée :

- Distinction entre la **convention secrète** (clé cryptographique, mot de passe d’un volume chiffré) et le **code utilisateur** d’un appareil (qui sert à déverrouiller mais ne constitue pas en soi une convention de déchiffrement) — distinction qui a fait l’objet de jurisprudences contradictoires.
- Conditions de l’obligation : la convention doit concerner un moyen de cryptologie « susceptible d’avoir été utilisé » pour un crime ou délit, ce qui suppose un faisceau d’indices, et non une simple suspicion généralisée.
- Pratique des juridictions très variable selon contexte et selon avocats engagés.

**Cas comparés** :

- **Royaume-Uni** : RIPA section 49 prévoit une obligation équivalente (jusqu’à deux ans de prison pour refus, cinq ans pour terrorisme ou pédocriminalité).
- **États-Unis** : le Cinquième Amendement protège contre l’auto-incrimination forcée ; la jurisprudence sur l’usage forcé de la biométrie par rapport au code mémoire mémorisé reste mouvante (plusieurs décisions divergentes selon circuits fédéraux).
- **Suisse** : pas d’obligation équivalente à 434-15-2 ; position structurellement plus protectrice.

**Implication pratique** : il ne revient pas à ce cours de recommander une attitude (refuser ou non) face à une demande de communication d’une convention de déchiffrement, ni d’évaluer ce qui constitue ou non une telle convention dans un cas concret. Ces questions relèvent d’une analyse juridique individuelle. **Si tu es confronté à une telle demande, la seule action raisonnable est de consulter immédiatement un avocat spécialisé** (droit pénal, droit numérique, ou droit de la presse selon contexte). Refus mal calibré comme communication imprudente peuvent l’un et l’autre aggraver la situation.

Au plan opérationnel préventif, en revanche, ce cours observe que :

- Le code utilisateur **mémorisé** (non biométrique) est structurellement plus difficile à obtenir d’une personne sous contrainte qu’une empreinte digitale ou un visage qui peuvent être utilisés sans coopération active.
- L’état BFU (cf. Ch 12.8) protège les données mieux que l’état AFU contre les outils forensics commerciaux, indépendamment de la question juridique.

## 37.6 Sapin II : lanceurs d’alerte en France

Loi Sapin II (2016), modifiée par la loi du 21 mars 2022 transposant la directive UE 2019/1937.

Protection accordée aux personnes signalant des faits :

- **Crimes ou délits**.
- **Violations graves de la loi**.
- **Menaces ou préjudices** pour l’intérêt général.

Procédure :

1. **Signalement interne** (en premier lieu, sauf exceptions).
1. **Signalement externe** : autorité compétente (Défenseur des droits, AAI sectorielle).
1. **Divulgation publique** : possible si signalements précédents sans suites, ou risque imminent.

Protections : non-licenciement, non-représailles, confidentialité de l’identité, soutien juridique du Défenseur des droits.

**Limite** : les sanctions effectives contre représailles restent partielles. Beaucoup de lanceurs d’alerte ont payé un prix professionnel et personnel important malgré la loi.

## 37.7 Anti-doxxing

En France, plusieurs qualifications mobilisables :

- **Atteinte à la vie privée** (art. 226-1 CP).
- **Mise en danger** (si publication d’adresse avec menace).
- **Harcèlement moral** ou en meute (art. 222-33-2-2 CP).
- **Loi du 21 mars 2022** : aggravation des peines pour révélation d’information privée mettant en danger.

Signalement PHAROS. Plainte au parquet. Recours civil pour cessation et indemnisation.

## 37.8 Chat Control / CSAR : suivi

Cf. Ch 26.12 pour le détail. État de synthèse : dossier toujours en négociation à la rédaction (2026). Le Conseil a pris position en novembre 2025 ; le Parlement européen a soutenu en mars 2026 l’extension temporaire de la dérogation ePrivacy jusqu’en août 2027, ce qui maintient la fenêtre légale actuelle pour les scans volontaires hors-E2EE pendant que les négociations sur le règlement principal continuent. Les positions nationales évoluent au gré des présidences tournantes et des élections.

Si la version finale impose un scanning côté client sur l’E2EE, l’impact serait majeur pour la disponibilité de la messagerie E2EE européenne grand public.

## 37.9 AI Act UE

Règlement UE 2024/1689 (« AI Act ») : encadrement de l’IA dans l’UE, entré en vigueur progressivement 2024-2026. Pertinence privacy :

- **Article 5** : interdictions (notation sociale, certaines reconnaissances biométriques en temps réel par autorités).
- **Article 6+** : systèmes à haut risque, dont certains usages de reconnaissance faciale.
- **Article 50** : obligation de marquage des contenus IA (deepfakes).

Sanctions importantes pour fournisseurs IA.

## 37.10 Comparaison FR / UE / US / UK / CH (synthèse)

|Aspect                  |France           |UE                   |US                   |UK               |Suisse                |
|------------------------|-----------------|---------------------|---------------------|-----------------|----------------------|
|**Chiffrement libre**   |Oui (LCEN 30)    |Oui (RGPD compatible)|Oui (constitutionnel)|Oui mais RIPA    |Oui (forte protection)|
|**Obligation clé**      |Oui (434-15-2 CP)|Variable             |5e amendement protège|Oui (RIPA s.49)  |Non                   |
|**Surveillance massive**|LRM 2015, ajustée|Encadrée (CJUE)      |FISA, NSL            |IPA 2016         |Forte protection      |
|**Anti-doxxing**        |Oui (loi 2022)   |Variable national    |Variable état        |Oui (M.Comms Act)|Oui                   |
|**Lanceurs d’alerte**   |Sapin II / 2022  |Directive 2019       |Patchwork sectoriel  |PIDA             |LWB                   |

## 37.11 Cadre éthique du cours

Ce cours forme à des compétences défensives. Il ne couvre pas :

- Attaque, intrusion, exploitation.
- Contournement d’une enquête judiciaire légitime.
- Dissimulation d’activités illicites.
- Doxxing, harcèlement, fraude à pseudonymes.
- Usurpation d’identité.

Le pseudonymat, le chiffrement, l’anonymat sont des droits exercés dans un cadre légal. Leur usage à des fins illicites engage la responsabilité pénale de l’auteur, indépendamment de l’efficacité technique de l’outil.

-----
