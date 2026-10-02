---
title: Chapitre 45 — Contournement de sanctions et biens dual-use
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies de criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre les **mécanismes de contournement de sanctions économiques** — sujet devenu central depuis 2022 — et les enjeux liés aux **biens à double usage** (dual-use).

## Le concept

Les **sanctions économiques** sont des mesures restrictives imposées par des États ou organisations internationales contre des personnes, entités ou pays. Trois sources principales :

- **ONU** : sanctions de l’ONU, contraignantes pour tous les États membres.
- **UE** : sanctions UE consolidées, contraignantes pour tous les opérateurs UE et leurs filiales.
- **US** : sanctions OFAC, avec portée extraterritoriale forte (sanctions secondaires impactant les opérateurs non-US qui font affaire avec les personnes sanctionnées).
- **UK** : sanctions OFSI.
- **Sanctions nationales** spécifiques (France via la DGT).

**Catégories** :

- **Sanctions ciblées** (PEP, dirigeants, entités spécifiques) : gel d’avoirs, interdiction de transactions.
- **Sanctions sectorielles** (banques, énergie, défense, etc.).
- **Embargos** : interdictions générales de commerce avec un pays.
- **Restrictions à l’exportation** de biens (dual-use, militaires, technologiques).

**Contournement** : techniques utilisées pour échapper aux sanctions.

## Mécanismes de contournement courants

- **Front companies** : société tierce non sanctionnée agit pour le compte d’une entité sanctionnée.
- **Sociétés écrans dans pays tiers** : Émirats, Turquie, Asie centrale, Caucase — par où transitent des flux et marchandises vers et depuis les juridictions sanctionnées.
- **Triangulation commerciale** : achat dans pays A, vente apparente vers pays B (non sanctionné), revente effective vers pays C (sanctionné).
- **Re-pavillonnement** : navires (notamment pétroliers), aéronefs sous pavillon de complaisance pour masquer l’identité réelle.
- **Falsification de documents** : certificats d’origine, bills of lading, documents douaniers.
- **Crypto** : utilisation de stablecoins pour les paiements (renvoi OSINT Crypto pour le détail on-chain).
- **Mixers et bridges** crypto pour brouiller la traçabilité.
- **AIS spoofing** ou éteignage : navires éteignent leur transpondeur AIS pour masquer leur trajectoire.

## Biens dual-use

Biens à **double usage** civil et militaire (semi-conducteurs avancés, capteurs, lasers, équipements de cryptographie, certains logiciels, drones, équipements industriels lourds). Régulation UE par le règlement 2021/821. Listes mises à jour régulièrement.

Détection FININT : flux financiers vers fournisseurs de biens dual-use, contreparties dans des juridictions à risque, schémas de triangulation, sous-traitance suspecte.

## L’utilité opérationnelle

Depuis 2022 (sanctions Russie), le contournement est un domaine en croissance forte. Les CRF dédient des ressources spécifiques. Les banques renforcent leur screening (filtres OFAC et UE).

## Méthode — signaux de contournement

- Flux soudains et significatifs vers une juridiction tierce (Émirats, Turquie, Géorgie, Arménie, Asie centrale).
- Sociétés intermédiaires récemment créées en juridictions tierces.
- Bénéficiaires effectifs liés à des entités sanctionnées (recherche dans OFAC SDN, UE consolidated list).
- Activités d’import-export de biens dual-use ou de technologies sensibles.
- Schémas de triangulation incohérents économiquement.
- AIS spoofing repérable via plateformes de tracking maritime.

## Mini-walkthrough — schéma simplifié

Une société turque récemment créée commence à recevoir des virements significatifs d’Europe pour « consulting services » et à envoyer des marchandises (semi-conducteurs) vers la Russie. L’UBO de la société turque est lié à une personne précédemment associée à une entreprise russe sanctionnée.

Lecture FININT : *probable* contournement de sanctions UE/US. Signalement et coopération sont prioritaires (CRF turque, sanctions UE et US, services nationaux dédiés).

## Erreurs fréquentes

- **Considérer toute opération avec un pays tiers comme contournement.** La grande majorité du commerce avec Émirats, Turquie, Géorgie est légitime.
- **Sous-estimer la portée extraterritoriale des sanctions OFAC.** Un opérateur européen peut être impacté.
- **Confondre dual-use et militaire.** Le dual-use est civil mais soumis à autorisation.

## Limites

Le contournement de sanctions est un domaine **politiquement sensible** et techniquement complexe. Les CRF travaillent en étroite collaboration avec services dédiés (DG Trésor — pôle sanctions financières, OFAC, OFSI, services douaniers).

## Lien avec le fil rouge

> **CLEARFLOW — Volet sanctions exploratoire**
> 
> Le dossier Haddad contient des flux passant par Émirats, Turquie. À ce stade, aucun lien direct avec une entité sanctionnée n’est démontré. La possibilité que certains flux relèvent d’un contournement *opportuniste* (vente vers juridictions sous embargo via réseau commercial) reste *possible*. La note finale signale ce volet exploratoire au PNF et recommande coopération avec la DG Trésor — pôle sanctions financières.

## Points clés à retenir

- Sanctions ONU, UE, OFAC, OFSI, nationales.
- Mécanismes de contournement : fronts, triangulation, crypto, re-pavillonnement.
- Dual-use = sujet sensible avec régulation propre.
- Coopération services dédiés (DG Trésor pôle sanctions, OFAC) essentielle.

-----
