---
title: Segmentation réseau
source: Cyber/12 Fiches notions/Segmentation réseau.md
format: fiche
revue: '2026-10-01'
terms:
  Segmentation réseau: Découpage du réseau en zones (sous-réseaux, VLAN) filtrées entre elles, pour contenir un incident et limiter le mouvement latéral.
  Microsegmentation: Segmentation fine au niveau de chaque charge de travail, avec des règles « qui peut parler à qui » flux par flux.
---

> Fiche notion assemblée à partir de mes notes (sources sous chaque bloc).

## En bref

**Définition.** *Découper* le système d'information en zones isolées pour qu'un incident dans l'une ne se propage pas aux autres.

- **Cloisonnement** : terme général de séparation logique ou physique entre environnements (prod/dev, métiers, niveaux de sensibilité).
- **Segmentation (réseau)** : découpage du réseau en sous-réseaux/VLAN avec filtrage entre eux, limitant la circulation latérale.

**Principe.** Sans segmentation, une fois un poste compromis, tout le réseau est atteignable (réseau « plat »). Avec segmentation, l'attaquant est contenu dans une zone.

*↳ [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md) (chapitre 15)*

## Comment l'expliquer

Sans segmentation, un attaquant qui compromet un poste utilisateur peut atteindre directement le contrôleur de domaine, le vCenter, les sauvegardes — le blast radius est maximal. La segmentation via VLANs et firewalls inter-zones limite le mouvement latéral. C'est la mesure la plus efficace contre la propagation d'un ransomware ou d'un attaquant dans le réseau.

*↳ [Infrastructure IT](../../it/infrastructure/infrastructure-it/index.md) (réponse type)*

On a généralement un firewall externe côté Internet, puis une DMZ qui héberge les services exposés (reverse proxy, bastion, VPN), un firewall interne, et le LAN avec les serveurs, l'AD, les bases de données. Les postes utilisateurs sont dans un réseau séparé. On ajoute un réseau de management isolé pour l'administration des équipements. L'idée c'est la défense en profondeur avec des zones de confiance décroissante.

*↳ [Infrastructure IT](../../it/infrastructure/infrastructure-it/index.md) (réponse type)*

## VLAN et DMZ

Un VLAN (Virtual LAN) segmente logiquement un réseau physique en plusieurs domaines de broadcast distincts. Des machines branchées sur le même switch physique peuvent être dans des VLANs différents et ne se voient pas — c'est comme si elles étaient sur des réseaux physiques séparés. Pour communiquer entre VLANs, il faut passer par un routeur (ou un switch L3).

Un VLAN est un mécanisme technique de segmentation réseau au niveau 2. Une DMZ est un concept d'architecture : c'est une zone réseau tampon entre Internet et le réseau interne, qui héberge les services exposés (reverse proxy, bastion, serveurs web publics). En pratique, une DMZ est souvent implémentée avec des VLANs et des firewalls.

*↳ Questions d'entretien (réponses types)*

## Exemple

🔧 **Exemple concret** — Isoler le réseau bureautique du réseau industriel (OT) empêche un ransomware bureautique d'arrêter l'usine.

*↳ [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md) (chapitre 15)*

## Microsegmentation

**Définition.** Forme fine de segmentation où l'on isole jusqu'à la *charge de travail individuelle* (machine, conteneur, application), avec des politiques de filtrage au plus près de chaque ressource, indépendantes de la topologie réseau physique.

**Principe.** Plutôt que de cloisonner par grands sous-réseaux, on définit *qui peut parler à qui* au niveau de chaque flux applicatif (par exemple : ce serveur web peut parler à cette base sur ce port, et à rien d'autre). C'est un fondement opérationnel du Zero Trust.

*↳ [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md) (chapitre 16)*

## À retenir

🎯 **À retenir** — Un réseau plat transforme une intrusion locale en compromission globale. Segmenter, c'est compartimenter le naufrage.

*↳ [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md) (chapitre 15)*

## Voir aussi

[Zero Trust](zero-trust.md) · [Défense en profondeur](defense-en-profondeur.md) · [Surface d'attaque](surface-d-attaque.md)
