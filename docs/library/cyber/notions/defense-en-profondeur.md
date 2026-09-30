---
title: Défense en profondeur
source: Cyber/00_Notions/Fiche_Defense_en_profondeur.md
format: fiche
terms:
  Défense en profondeur: Empiler plusieurs couches de sécurité indépendantes, pour qu'aucune faille unique ne soit fatale.
---

> Fiche notion assemblée à partir de mes notes (sources sous chaque bloc).

## En bref

**Définition.** Empiler *plusieurs couches* de sécurité indépendantes, pour qu'aucune faille unique ne soit fatale. Métaphore du château : douves, remparts, herse, donjon, gardes.

**Principe.** Chaque couche peut échouer ; ce qui protège, c'est que l'attaquant doive *toutes* les franchir. Les couches doivent être **diverses** (pas dix firewalls identiques, mais firewall + segmentation + EDR + MFA + journalisation) pour qu'une même faille ne les traverse pas toutes.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 11)*

## Comment l'expliquer

C'est le fait de superposer plusieurs couches de sécurité plutôt que de compter sur un seul mécanisme. Si une couche est contournée, la suivante prend le relais. Par exemple : un firewall périmétrique + une segmentation réseau + un EDR sur les postes + du MFA sur les comptes + du chiffrement des données au repos. Aucune mesure seule ne suffit — un attaquant qui contourne le firewall sera détecté par l'EDR, et même s'il contourne l'EDR, les données chiffrées limitent l'impact.

*↳ [Questions d'entretien](../../it/culture/questions-d-entretien-cyber-sysadmin/index.md) (réponse type)*

**Defense in depth** : multiples couches de défense indépendantes, de manière à ce qu’une défaillance à une couche soit compensée par les suivantes. Couches typiques : sécurité périmétrique, endpoint, identity, cloud/SaaS, réseau interne, applicatif, données, détection/réponse. Un attaquant qui franchit une couche doit en franchir d’autres avant d’atteindre les données critiques.

*↳ [APT — version complète](../cti/apt-version-complete/index.md)*

## Exemples

🔧 **Exemple concret** — Un mail malveillant doit franchir : filtrage mail → sensibilisation de l'utilisateur → antivirus → EDR → segmentation → moindre privilège → détection SOC. Chaque couche réduit la probabilité de succès complet.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 11)*

La stratégie de défense en profondeur : code sécurisé (fondation) → tests automatisés (vérification) → WAF (filet) → monitoring et alerting (détection) → incident response (réaction). Si une couche échoue, la suivante rattrape.

*↳ [AppSec](../hardening/appsec/index.md)*

**Défense en profondeur** : ne jamais miser sur une seule barrière. Si ton mot de passe est ta seule défense, sa compromission est totale. Si tu as un mot de passe fort + MFA matériel + alertes de connexion + sessions audités + procédure de récupération hors-ligne, la compromission de l’un ne renverse pas tout.

*↳ [OPSEC & privacy](../cti/opsec-privacy/index.md)*

## Erreur fréquente

⚠️ **Erreur fréquente** — La « défense en largeur » : empiler des couches *redondantes* (même type) au lieu de *complémentaires*. Trois antivirus ne valent pas un antivirus + une segmentation.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 11)*

## À retenir

🎯 **À retenir** — Aucune couche n'est parfaite ; la profondeur transforme une faille unique en simple incident.

*↳ [Taxonomie cyber](../concepts/taxonomie-cyber/index.md) (chapitre 11)*

## Voir aussi

[Moindre privilège](moindre-privilege.md) · [Segmentation réseau](segmentation-reseau.md) · [MFA](mfa.md) · [Zero Trust](zero-trust.md)
