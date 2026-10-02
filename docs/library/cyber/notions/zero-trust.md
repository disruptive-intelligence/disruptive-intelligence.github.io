---
title: Zero Trust
source: Cyber/12 Fiches notions/Zero Trust.md
format: fiche
revue: '2026-10-02'
terms:
  Zero Trust: Modèle de sécurité fondé sur « ne jamais faire confiance, toujours vérifier » ; être dans le réseau ne donne aucune confiance implicite.
---

> Fiche notion assemblée à partir de mes notes (sources en fin de fiche).

## En bref

**Définition.** Modèle de sécurité fondé sur « **ne jamais faire confiance, toujours vérifier** » : aucun utilisateur, appareil ou flux n'est implicitement de confiance du seul fait d'être « à l'intérieur » du réseau.

**Principes clés.** Vérification systématique de l'identité et de la posture à *chaque* accès ; accès au plus juste (moindre privilège) ; microsegmentation ; décision contextuelle (qui, quoi, d'où, quel appareil, quel risque) ; chiffrement généralisé. On abandonne le modèle « périmètre = château fort » au profit de « chaque ressource se défend elle-même ».[^1]

## Comment l'expliquer

Le modèle traditionnel fait confiance au réseau interne — une fois à l'intérieur du périmètre, on accède à tout. Le Zero Trust part du principe que personne n'est de confiance par défaut, même en interne. Chaque accès est vérifié : identité forte (MFA), état du poste (conformité), moindre privilège, micro-segmentation. Le VPN est remplacé par des solutions d'accès conditionnel. C'est particulièrement pertinent avec le télétravail et le cloud.[^2]

## Exemple

🔧 **Exemple concret** — Un employé connecté au VPN interne ne reçoit *pas* automatiquement l'accès à toutes les applications : chaque accès est réévalué selon son identité, son appareil et le contexte.[^1]

## Ses briques

**Assume Breach — Définition.** Posture mentale et stratégique : *partir du principe qu'on est déjà, ou qu'on sera, compromis*. On ne conçoit plus seulement pour empêcher l'intrusion, mais pour *limiter*, *détecter* et *répondre* quand elle survient.[^3]

🎯 **À retenir** — La microsegmentation passe du « cloisonner par zones » au « cloisonner par flux ». Le lateral movement devient très coûteux pour l'attaquant.[^4]

🎯 **À retenir** — Le ZTNA remplace l'accès réseau large du VPN par un accès applicatif minimal et contextuel : mise en œuvre concrète du Zero Trust.[^5]

## Erreur fréquente

⚠️ **Erreur fréquente** — Croire que Zero Trust est un produit qu'on achète. C'est une *architecture* et une *philosophie*, mise en œuvre par de nombreux composants (IAM, MFA, ZTNA, microsegmentation, EDR).[^1]

## À retenir

🎯 **À retenir** — Zero Trust supprime la « confiance par localisation ». Être dans le réseau ne prouve plus rien.[^1]

## Voir aussi

[Moindre privilège](moindre-privilege.md) · [MFA](mfa.md) · [Segmentation réseau](segmentation-reseau.md) · [Défense en profondeur](defense-en-profondeur.md)

## Sources

[^1]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 17.
[^2]: [Infrastructure IT](../../it/infrastructure/infrastructure-it/index.md), réponse type.
[^3]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 18.
[^4]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 16.
[^5]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), ZTNA.
