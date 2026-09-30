---
title: Chapitre 23 — Actionnaires, UBO et contrôle indirect
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie IV — Personnes, sociétés et contrôle
  - index.md
---

## Objectif du chapitre

Comprendre la **chaîne du contrôle** : actionnaires immédiats, sociétés interposées, UBO de dernier niveau, mécanismes de contrôle indirect au-delà du capital (conventions, usufruit, options, conventions de vote).

## Le concept

Trois niveaux à distinguer :

1. **Actionnariat / association** : qui détient les titres ou les parts au capital de l’entité — souvent une autre société, parfois une personne physique directement.
1. **UBO** : qui contrôle ultimement (personne physique). Peut être direct (actionnaire personne physique) ou indirect (via chaîne de sociétés, trusts, conventions).
1. **Contrôle effectif** : qui décide réellement — peut être différent de l’UBO de droit. Par exemple, un actionnaire majoritaire qui a délégué le contrôle par convention à un tiers.

**Mécanismes de contrôle indirect** :

- **Chaîne de holdings** : société A détenue par société B, elle-même détenue par société C, elle-même détenue par M. X. Le contrôle est traçable mais demande à remonter la chaîne.
- **Trusts** : la société est détenue par un trust. Le settlor a apporté les actifs ; le trustee les gère ; les bénéficiaires en jouissent. Le contrôle peut être chez le settlor (trust révocable), chez le trustee (trust irrévocable), ou ailleurs (protecteur).
- **Fondations** : entité juridique qui détient les titres. Le fondateur a apporté ; le conseil de fondation gère ; les bénéficiaires en jouissent.
- **Nominees** : prête-noms officiels (déclarés comme tels en common law).
- **Conventions de vote** : un actionnaire minoritaire peut contrôler par convention si la majorité accepte de voter selon ses instructions.
- **Usufruit** : démembrement de propriété. Le nu-propriétaire détient le capital ; l’usufruitier exerce les droits.
- **Options et promesses de vente** : un investisseur peut avoir une option d’achat lui permettant de prendre le contrôle à tout moment.
- **Pactes d’actionnaires** : conventions privées qui modulent les droits formels.
- **Démembrement entre associés** : un dirigeant détient peu mais a une convention lui donnant un pouvoir étendu.

## L’utilité opérationnelle

L’analyste cherche à répondre à : **qui contrôle réellement cette entité, et avec quel niveau de confiance ?**

Cela conditionne :

- L’identification du véritable décideur ;
- La compréhension de la stratégie économique ;
- L’attribution des responsabilités ;
- Le ciblage des coopérations et réquisitions.

## Méthode — remonter la chaîne

1. **Identifier les associés immédiats** (registre, statuts).
1. **Pour chaque associé personne morale, remonter** : qui sont ses associés ? (récursion).
1. **Arriver à une personne physique** OU **arriver à une structure opaque** (trust, IBC offshore sans accès).
1. **Mobiliser les leaks** (chapitre 18) si arrêt sur structure opaque.
1. **Mobiliser la coopération internationale** si toujours bloqué.
1. **Calibrer la confiance** : UBO de droit identifié ≠ UBO réel automatique. Le contrôle effectif peut résider ailleurs (conventions, options, pacte).

## Mini-walkthrough — chaîne CLEARFLOW (partielle)

Sur une des SAS françaises, NEXUS TRADING SAS :

- Associé unique au capital : NEXUS HOLDINGS LTD (Chypre).
- NEXUS HOLDINGS LTD : actionnaire majoritaire = OMEGA HOLDINGS TRUST (trust chypriote).
- OMEGA HOLDINGS TRUST : settlor = Karim Élie Haddad (identifié via Pandora Papers, chapitre 18). Trustee : cabinet professionnel chypriote (corporate service provider). Bénéficiaires : « la famille Haddad » (formulation typique d’un trust patrimonial — flou volontaire).

Chaîne : NEXUS FR ← NEXUS CY ← OMEGA TRUST ← Karim Haddad (settlor + bénéficiaire probable).

Niveau de confiance :

- Sur la chaîne juridique : *quasi-certain* (registres + leak).
- Sur l’identification de Haddad comme UBO réel : *probable* à *quasi-certain* selon recoupements ultérieurs (analyse de flux, contrôle effectif observable).

Lacunes : la formulation « famille Haddad » dans les bénéficiaires masque le pourcentage et la nature exacte du contrôle. Une coopération avec Mokas (CRF chypriote) serait nécessaire pour clarifier.

## Erreurs fréquentes

- **S’arrêter au premier niveau.** Identifier un associé personne morale sans remonter = travail incomplet.
- **Confondre actionnaire principal et UBO.** Un actionnaire détenant 24,9 % peut ne pas être UBO au sens UE (seuil 25 %), mais peut être UBO de fait par convention.
- **Ignorer le contrôle effectif.** Les statuts juridiques ne disent pas toujours qui dirige réellement.

## Limites

Lorsque la chaîne aboutit à une **structure opaque** (trust offshore, IBC sans accès), l’identification de l’UBO réel reste *probable* au mieux sur la base d’OSINT seul. La coopération internationale est nécessaire pour passer à *quasi-certain*.

## Lien avec le fil rouge

> **CLEARFLOW — Mapping du contrôle**
> 
> En remontant systématiquement chaque chaîne, Nassim aboutit à 4 « racines » principales du réseau : Karim Haddad (settlor du trust chypriote, UBO probable de plusieurs entités), un proche collaborateur basé à Dubaï (M. Y, PSC de plusieurs Limited UK), une fondation libanaise (rôle réel non clarifié), et un cabinet de trustees professionnel (mandant véritable inconnu — possible interposition supplémentaire). Cette carte du contrôle est l’un des livrables les plus stratégiques de la note.

## Points clés à retenir

- Distinguer associés / UBO / contrôle effectif.
- Remonter systématiquement la chaîne jusqu’à une personne physique ou une structure opaque.
- Mécanismes de contrôle indirect : trusts, fondations, nominees, conventions, options, usufruit.
- Niveau de confiance à calibrer à chaque étape de la chaîne.

-----
