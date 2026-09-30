---
title: Surface d'attaque
source: Cyber/00_Notions/Fiche_Surface_d_attaque.md
format: fiche
terms:
  Surface d'attaque: L'ensemble des points par lesquels un attaquant peut tenter d'entrer ou d'agir (ports ouverts, formulaires web, comptes, API, employés…).
---

> Fiche notion assemblée à partir de mes notes (sources sous chaque bloc).

## En bref

**Définition.**

- **Surface d'attaque** : l'*ensemble des points* par lesquels un attaquant peut tenter d'entrer ou d'agir (ports ouverts, formulaires web, comptes, API, employés…). Plus elle est grande, plus il y a d'occasions d'attaque.
- **Exposition** : le *degré d'accessibilité* d'un actif depuis une zone dangereuse (Internet > réseau interne > réseau isolé). Un même actif est plus risqué s'il est exposé.
- **Chemin d'attaque** (attack path) : la *séquence d'étapes* reliant le point d'entrée de l'attaquant à son objectif final (souvent : Internet → phishing → poste → identité → serveur → données).

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 7)*

## Réduire la surface d'attaque

**Définition.** Diminuer activement le nombre de points exploitables : moins de services exposés, moins de comptes, moins de logiciels, moins de droits, moins de données conservées.

**Principe.** Chaque composant exposé est un risque potentiel. La sécurité la plus économique est souvent *l'absence* : ce qui n'existe pas ne peut être attaqué. Recoupe le durcissement, le moindre privilège et la minimisation des données.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 22)*

Le hardening est la réduction de la surface d'attaque par la configuration sécurisée. Principes : désactiver ce qui n'est pas nécessaire, changer les configurations par défaut, appliquer le moindre privilège, mettre à jour.

*↳ [Infrastructure IT](../../it/infrastructure/infrastructure-it/index.md)*

## Exemples

🔧 **Exemple concret** — Un serveur exposé sur Internet avec 30 ports ouverts a une grande surface d'attaque *et* une forte exposition. Le même serveur derrière un VPN, avec 2 ports, réduit les deux.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 7)*

🔧 **Exemple concret** — Supprimer une vieille application interne oubliée mais toujours en ligne élimine d'un coup toutes ses vulnérabilités potentielles.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 22)*

**Réduire la surface d'attaque** signifie avoir moins de cibles exposées. Chaque compte en ligne est une porte d'entrée potentielle. Chaque application installée est une permission accordée. Chaque appareil connecté est un maillon de la chaîne. Le réflexe : supprimer les comptes inutilisés (ce compte créé en 2018 pour tester un service et jamais réutilisé est toujours là, avec ses données, et potentiellement dans une fuite de données), désinstaller les applications qui ne servent plus, et révoquer les accès des applications tierces aux comptes principaux.

*↳ [Cybersécurité du quotidien](../concepts/cybersecurite-du-quotidien/index.md)*

## La gérer dans la durée

- **ASM — Attack Surface Management** consiste à identifier, évaluer, réduire et surveiller en continu les éléments exposés pouvant être exploités par un attaquant.

*↳ [HTB — Attack Surface Management](../cyberdefense/htb-attack-surface-management/index.md)*

**EASM** (*External Attack Surface Management*) est la sous-catégorie qui se concentre sur l'exposition externe (Internet-facing).

*↳ [Vulnerability management & intelligence](../cyberdefense/vulnerability-management-intelligence/index.md) (chapitre 29)*

## À retenir

🎯 **À retenir** — On défend mieux en *réduisant la surface* qu'en empilant les contrôles sur une surface tentaculaire.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 7)*

## Voir aussi

[Moindre privilège](moindre-privilege.md) · [Défense en profondeur](defense-en-profondeur.md) · [Segmentation réseau](segmentation-reseau.md)
