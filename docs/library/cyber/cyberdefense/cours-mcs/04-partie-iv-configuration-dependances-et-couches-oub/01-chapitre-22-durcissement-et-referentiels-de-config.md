---
title: Chapitre 22 — Durcissement et référentiels de configuration
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

## 22.1 Pourquoi une version à jour mal configurée reste vulnérable

Un correctif supprime un défaut de code. Il ne touche pas à la façon dont vous avez configuré le produit — et l'essentiel des compromissions réelles emprunte des chemins de configuration, pas des failles de code (§11.4).

**Les cinq configurations qui annulent l'effet de tous vos correctifs :**

| Configuration | Effet |
|---|---|
| Protocole ou méthode d'authentification héritée laissée active | Contournement possible des protections modernes |
| Compte par défaut conservé, ou mot de passe local identique partout | Propagation immédiate d'une compromission |
| Service exposé qui n'a pas besoin de l'être | Surface d'attaque inutile (ch. 11) |
| Droits excessifs sur un compte de service | Transforme une intrusion mineure en compromission majeure |
| Journalisation absente ou insuffisante | Interdit toute investigation (§21.3) |

**Le rapport coût/effet est très favorable** : ces cinq points se traitent par configuration, sans fenêtre de correction, sans risque de régression majeure, et une fois pour toutes.

## 22.2 Choisir et adapter un référentiel

| Type de référentiel | Origine | Caractéristique |
|---|---|---|
| Guides d'agences nationales | Autorités publiques | Contexte réglementaire proche, souvent en français, exigences justifiées |
| Référentiels communautaires | Consortiums | Très détaillés, couverture large, niveaux de sévérité gradués |
| Guides de durcissement gouvernementaux | Administrations | Les plus stricts, parfois inapplicables en entreprise |
| Guides constructeurs | Éditeurs | Fiables sur le produit, silencieux sur ce qui gêne le produit |

**La méthode d'adoption, en quatre étapes :**

1. **Choisir un référentiel de base** — n'en cumulez pas plusieurs, vous produiriez des exigences contradictoires.
2. **Le dériver** : chaque point est retenu, adapté ou écarté, et **chaque écart est motivé par écrit**. C'est ce document dérivé qui devient votre référence, pas le référentiel d'origine.
3. **Le versionner** : votre *baseline* est un artefact avec un numéro de version, un propriétaire et une date de revue.
4. **Le décliner par classe de service** : un niveau d'exigence pour C1, un autre pour C3.

⚠️ **PIÈGE — appliquer un référentiel sans dérivation**
Un référentiel appliqué intégralement, sans adaptation, produit systématiquement des ruptures fonctionnelles. L'équipe désactive alors les contrôles gênants un par un, sans les documenter, et la *baseline* devient une fiction. **La dérivation motivée n'est pas un affaiblissement : c'est ce qui rend la baseline applicable, donc réellement appliquée.**

## 22.3 Construire et maintenir une *baseline*

| Élément | Contenu |
|---|---|
| Référentiel source | Nom et version |
| Périmètre | Quels systèmes, quelles classes |
| Points retenus | Avec leur paramétrage exact |
| **Écarts motivés** | Point écarté, raison, risque accepté, revue |
| Méthode d'application | Modèle, script, politique centralisée |
| Méthode de contrôle | Comment on vérifie |
| Propriétaire et revue | Nom, fréquence |

**La question du niveau d'exigence** se tranche par classe de service, jamais globalement. Une exigence appliquée uniformément à tout le parc sera soit trop faible pour les actifs critiques, soit inapplicable aux actifs courants.

## 22.4 Automatiser le contrôle

Trois familles de mécanismes, complémentaires :

| Mécanisme | Principe | Fréquence réaliste |
|---|---|---|
| **Contrôle par script ou format standardisé** | Vérification périodique de chaque point de la *baseline* | Hebdomadaire à mensuelle |
| **Politiques centralisées natives** | La plateforme applique et vérifie en continu | Continu |
| **Contrôle dans la chaîne de construction** | L'image est vérifiée avant d'être publiée | À chaque construction |

**Le troisième est le plus efficace** : contrôler à la construction empêche la non-conformité d'exister, plutôt que de la constater après coup. C'est la traduction du principe du §10.7 — traiter à la source plutôt que rattraper.

## 22.5 Mesurer la conformité de configuration

**Deux mesures distinctes, à ne jamais fondre en un seul chiffre.**

Une *instance de contrôle* est la vérification d'un point de la *baseline* sur un actif donné. Si votre *baseline* comporte 80 points applicables et que vous contrôlez 120 serveurs, vous évaluez 9 600 instances.

```
                         Instances de contrôle conformes
Conformité (%)  =  ──────────────────────────────────────── × 100
                        Instances de contrôle applicables

                         Actifs éligibles effectivement évalués
Couverture (%)  =  ──────────────────────────────────────────── × 100
                         Actifs éligibles du périmètre
```


**Quatre valeurs à publier ensemble**, faute de quoi le chiffre ne veut rien dire :

| Valeur | Rôle |
|---|---|
| **Couverture** | Sur quelle part du périmètre éligible la mesure porte-t-elle |
| **Conformité dans la population mesurée** | L'état de ce qui a été évalué |
| **Points critiques non conformes** | En **valeur absolue**, sans pondération : dix écarts mineurs et un compte administrateur par défaut ne se compensent pas |
| **Actifs non évaluables** | Avec leur motif — non applicable, injoignable, exclu documenté |

⚠️ Le dénominateur de la conformité porte sur les points **applicables après dérivation** (§22.2), pas sur ceux du référentiel d'origine. Un point écarté et motivé n'est pas une non-conformité : il ne fait pas partie de la population éligible.

## 22.6 ⚠️ Le durcissement qui casse la production

C'est le principal frein à l'adoption, et il est légitime : contrairement à un correctif, un durcissement modifie **intentionnellement** le comportement du système.

**La méthode qui fonctionne**, en cinq étapes :

1. **Mesurer avant d'appliquer.** Beaucoup de contrôles peuvent être évalués en mode observation : on journalise ce qui serait bloqué, sans bloquer.
2. **Appliquer par lots** de points, pas la *baseline* entière d'un coup — sinon un incident ne peut être imputé à aucun point précis.
3. **Utiliser les anneaux** du §18.4 : le durcissement est un changement comme un autre.
4. **Prévoir le retour arrière** point par point.
5. **Documenter les écarts découverts** : un point qui casse une application métier devient un écart motivé, pas un contrôle silencieusement désactivé.

## 22.7 📌 Limites

- **Les référentiels génériques ne couvrent pas les applications métier**, qui portent souvent les configurations les plus risquées. Pour elles, il faut construire ses propres points de contrôle.
- **Le coût de maintenance d'une baseline** est réel : chaque version majeure du système la rend partiellement obsolète.
- **La conformité de configuration ne dit rien de l'exposition.** Un serveur parfaitement durci mais publié inutilement reste un problème (ch. 11).
- **Le durcissement ne remplace pas les correctifs**, et l'inverse est également vrai. Ce sont deux couches distinctes.

## 22.8 ✅ Recommandations priorisées

| Prio | Action |
|---|---|
| **P0** | Traiter les cinq configurations du §22.1 sur les actifs C1, indépendamment de toute *baseline* complète |
| **P0** | Mots de passe d'administration locaux uniques par machine |
| **P0** | Désactiver les protocoles et méthodes d'authentification hérités, après mesure en mode observation |
| P1 | Dériver une *baseline* versionnée à partir d'un référentiel unique, avec écarts motivés |
| P1 | Contrôle automatisé mensuel, avec indicateur de points critiques non conformes |
| P1 | Intégrer le contrôle de configuration à la chaîne de construction des images |
| P2 | Étendre aux applications métier avec des points de contrôle propres |

→ **Chapitre 23 — Dérive de configuration, IaC et immutabilité** : la dérive, propriété inévitable des systèmes vivants.

## Synthèse mentale du chapitre 22

Un correctif supprime un défaut de code, il ne touche pas à votre configuration — et l'essentiel des compromissions réelles emprunte des chemins de configuration. Cinq réglages annulent à eux seuls l'effet de tous vos correctifs, et ils se traitent sans fenêtre ni risque majeur. N'adoptez qu'un seul référentiel de base, et dérivez-le en motivant chaque écart : la dérivation n'affaiblit pas la baseline, c'est ce qui la rend applicable donc réellement appliquée. Contrôler à la construction empêche la non-conformité d'exister plutôt que de la constater. Mesurez séparément les points critiques non conformes, car dix écarts mineurs ne compensent pas un compte administrateur par défaut. Enfin, un durcissement modifie intentionnellement le comportement du système : il s'applique par lots, en anneaux, après mesure en mode observation.

**Trois questions de vérification**

1. Votre parc est parfaitement à jour et un attaquant progresse quand même du poste bureautique jusqu'à la console de sauvegarde. Quelles configurations examinez-vous en premier ?
2. Pourquoi appliquer un référentiel de durcissement sans dérivation produit-il presque toujours une baseline fictive ?
3. Vous affichez 94 % de conformité de configuration. Quelles trois précautions de calcul devez-vous avoir prises pour que ce chiffre signifie quelque chose ?

---
