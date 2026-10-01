---
title: Chapitre 39 — L'autonomie mobile
source: IT/09 Technologies & prospective/Frontières technologiques (vol. 2).md
note: Frontières technologiques (vol. 2)
up:
- - Frontières technologiques (vol. 2)
  - ../index.md
- - Partie IV — Les grandes convergences
  - index.md
---

## ① La capacité recherchée

**Formulation retenue.**

> **Confier un déplacement à un système, dans un environnement partagé avec des humains non prévenus, sans supervision continue — et pouvoir le démontrer à un tiers.**

**La dernière clause est le dossier entier.** La capacité technique existe et fonctionne en exploitation commerciale dans un domaine restreint. **Ce qui borne l'extension n'est pas de faire, c'est de démontrer.**

---

## ② Les briques nécessaires

| Couche | Entrées d'atlas |
|---|---|
| **Percevoir** | lidar (6) · radar imageur (6) · bandes infrarouges (5) · optronique (5) · détecteurs (5) · fusion (7) · capteurs inertiels (6) · GNSS (6) · navigation sans GNSS (6) · capteurs quantiques (7) |
| **Apprendre** | modèles du monde (13) · sim-to-real (13) · automatisation-agentivité-autonomie (12) |
| **Agir** | véhicules autonomes (17) · domaine de conception opérationnelle (17) · localisation et cartographie (17) · autres modes (17) · autonomie supervisée (16) |
| **Relier** | edge/on-device (25) · réseaux non terrestres (24) · communications dégradées (24) |
| **Vérifier** | architecture de sûreté (30) · détection de sortie de domaine (30) · vérification formelle (30) · dossiers de sûreté (30) · dégradation maîtrisée (30) |

**Vingt-six entrées** — la dépendance la plus large de l'atlas, et de loin.

---

## ③ Ce qui empêche encore

**Premier — la démonstration de sûreté opposable.** On ne peut pas énumérer les situations d'un système ouvert sur le monde. La vérification exhaustive étant impossible, il faut lui substituer une argumentation acceptée par une autorité — et cette argumentation n'a pas de référentiel établi pour les systèmes apprenants.

**Deuxième — l'assurabilité.** Un assureur a besoin d'un historique de sinistres, d'une population comparable, de modes de défaillance caractérisés, d'une estimation du sinistre maximal et d'un cadre juridique stable. **Une technologie nouvelle ne fournit aucun des cinq.** Le volume 1 l'a établi : l'assurabilité est un meilleur indicateur avancé de déploiement que n'importe quelle annonce technique.

**Troisième — le ratio de supervision.** Un système supervisé à un opérateur pour un véhicule ne réduit pas le coût du travail : il le déplace. **C'est le paramètre qui décide de l'économie**, et il est presque jamais publié.

**Quatrième — l'extension du domaine d'emploi.** Chaque nouvelle ville, chaque nouveau type de voie, chaque nouvelle condition météorologique exige une validation. **L'extension se fait par négociation locale, non par effet d'échelle.**

---

## ④ Le maillon le plus en retard

**La démonstration de sûreté opposable, et son corollaire l'assurabilité.**

**L'argument.** La capacité technique est démontrée : des services commerciaux sans conducteur fonctionnent. Ce qui n'existe pas est un **référentiel permettant de démontrer, une fois, qu'un système est acceptablement sûr dans une classe de conditions** — et de transposer cette démonstration ailleurs.

**Ce qui le prouve.** L'extension se fait ville par ville. Si le verrou était la perception ou la décision, une amélioration du système permettrait une extension générale. **Le fait que l'extension soit géographique et négociée indique que le verrou est institutionnel.**

**Position par rapport à la thèse du volume.** Les couches éponymes sont *agir* et *percevoir*, qui fournissent dix-huit des vingt-six entrées. Le maillon en retard est dans *vérifier*. **La thèse est vérifiée, et c'est le cas le plus net des six.**

---

## ⑤ Quel mur domine

**La défaillance silencieuse**, sous la forme de la sortie de domaine non détectée : un système qui ne sait pas qu'il est hors de ses conditions de validation continue d'agir avec la même assurance apparente.

**L'incertitude**, au sens de l'impossibilité de vérification exhaustive — ce qui n'est pas un défaut du système mais une propriété du problème.

---

## ⑥ Ce qui est en train de changer

**L'exploitation commerciale sans conducteur existe** dans un nombre limité de villes, avec un domaine d'emploi qui s'étend progressivement. C'est un fait, et il déplace la question.

**Les architectures de sûreté** — enveloppe vérifiable entourant un système apprenant — entrent progressivement dans les référentiels sectoriels.

**La notion de domaine de conception opérationnelle** se normalise, ce qui rend les revendications comparables.

**Ce qui n'a pas changé.** Le renouvellement du parc, qui borne toute transformation à l'échelle du parc quel que soit le succès sur le flux — le volume 1 l'a chiffré. Et l'absence de référentiel transposable entre juridictions.

---

## ⑦ Ce que la convergence débloquerait

**Un transport dont le coût marginal ne comprend pas de conducteur** — ce qui change l'économie de la mobilité, de la logistique et de la desserte des zones peu denses.

**Mais borné par le parc.** Même une adoption totale sur les véhicules neufs mettrait plus d'une décennie à transformer le parc en circulation. **Le service de flotte n'a pas cette contrainte** — c'est pourquoi il précède et précédera le véhicule particulier.

---

## ⑧ Le verrou suivant

**Le renouvellement du parc et l'infrastructure de supervision.**

Si la sûreté se démontre et que l'assurabilité suit, la transformation reste bornée par deux choses : la durée de vie des véhicules en circulation — facteur cinq à dix entre part du flux et part du stock — et le **nombre d'opérateurs de supervision**, qui doit descendre sous un seuil pour que l'économie tienne.

---

## ⑨ La chronologie conditionnelle

```text
① si un référentiel de démonstration de sûreté applicable aux systèmes
   apprenants devient opposable dans une juridiction majeure
        → alors l'assurabilité devient traitable
          et le domaine d'emploi peut s'étendre par cadre et non par négociation

② si le ratio d'opérateurs de supervision descend sous un seuil économique
        → alors le renouvellement du parc devient limitant
          pour la transformation à l'échelle

③ si le référentiel n'apparaît pas
        → l'extension reste ville par ville, sans effet d'échelle,
          et l'économie reste celle d'un service local

④ si un accident majeur survient avant l'établissement du référentiel
        → durcissement des exigences, refermeture du domaine d'emploi,
          et report de plusieurs années
```


**L'étape ③ décrit l'état actuel** et doit être lue comme une trajectoire possible, non comme un échec. **L'étape ④ n'est pas une prédiction** : c'est un mécanisme établi au volume 1, et il doit figurer parce qu'il est le plus probable des facteurs de rupture.

---

## ⑩ Signaux, non-signaux, réfutation

**Signaux informatifs.** La publication d'un **référentiel de certification** pour système apprenant. L'apparition d'une **offre d'assurance standardisée**. Le **ratio opérateurs par véhicule**, publié. L'extension à un **type de voie ou de condition** non couvert jusque-là.

**Signaux non informatifs.** Le nombre de kilomètres parcourus, sans le domaine d'emploi correspondant. Le nombre de villes, sans les conditions. Les levées de fonds. Les comparaisons d'accidentologie sans population de référence comparable.

**Ce qui réfuterait l'analyse.** Le nombre de domaines d'emploi cesse de croître, ce qui indiquerait un verrou technique et non institutionnel. Le ratio de supervision ne baisse pas malgré l'expérience. Ou bien un référentiel apparaît et l'extension ne suit pas — ce qui invaliderait l'identification du maillon.

---
