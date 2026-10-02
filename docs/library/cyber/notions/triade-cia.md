---
title: Triade CIA
source: Cyber/12 Fiches notions/Triade CIA.md
format: fiche
revue: '2026-10-02'
terms:
  Triade CIA: Confidentialité, intégrité, disponibilité (DIC en français) — la boussole de la sécurité ; toute mesure sert au moins l'une de ces trois propriétés.
  Triptyque CIA: Confidentialité, intégrité, disponibilité (DIC en français) — la boussole de la sécurité ; toute mesure sert au moins l'une de ces trois propriétés.
---

> Fiche notion assemblée à partir de mes notes (sources en fin de fiche).

## En bref

**Définition.** Le triptyque **CIA** (Confidentiality, Integrity, Availability — en français DIC : Disponibilité, Intégrité, Confidentialité) est la boussole de la sécurité. Toute mesure de sécurité sert au moins l'une de ces trois propriétés.

- **Confidentialité** : l'information n'est accessible qu'aux personnes autorisées. Atteinte = fuite, espionnage.
- **Intégrité** : l'information n'est ni altérée ni falsifiée sans autorisation. Atteinte = sabotage, fraude, manipulation de données.
- **Disponibilité** : l'information et les services sont accessibles quand on en a besoin. Atteinte = déni de service, ransomware, panne.

**Extensions fréquentes** : on ajoute parfois la **traçabilité/imputabilité** (preuve de qui a fait quoi) et la **non-répudiation** (impossibilité de nier une action). Certains parlent du modèle étendu « Parkerian hexad ».[^1]

## Exemples

🔧 **Exemple concret** — Un ransomware chiffre les fichiers : il attaque surtout la **disponibilité** (et parfois la confidentialité par double extorsion). Une falsification de relevé bancaire attaque l'**intégrité**. Un vol de base de données attaque la **confidentialité**.[^1]

**Disponibilité prioritaire.** En IT, la triade CIA priorise souvent la confidentialité. En OT, c'est l'inverse : la disponibilité prime, puis l'intégrité, puis la confidentialité. Un arrêt de production a un coût immédiat (et parfois un risque safety) qui dépasse souvent le risque d'une vulnérabilité.[^2]

Un incident c'est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité ou la disponibilité.[^3]

## Authentification, autorisation, traçabilité

Quatre piliers du contrôle d'accès, souvent regroupés sous **AAA** (Authentication, Authorization, Accounting) + imputabilité.

🎯 **À retenir** — Authentification = *qui*. Autorisation = *quoi*. Traçabilité = *preuve*. Imputabilité = *attribution*.[^4]

## À retenir

🎯 **À retenir** — Quand vous analysez une attaque, demandez : *quelle propriété CIA est visée ?* La réponse oriente immédiatement la défense.[^1]

## Voir aussi

[Défense en profondeur](defense-en-profondeur.md) · [MFA](mfa.md)

## Sources

[^1]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 5.
[^2]: [Vulnerability management & intelligence](../vulnerabilites/vulnerability-management-intelligence/index.md).
[^3]: [Réponse à incident](../detection/reponse-a-incident/index.md), réponse type.
[^4]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 6.
