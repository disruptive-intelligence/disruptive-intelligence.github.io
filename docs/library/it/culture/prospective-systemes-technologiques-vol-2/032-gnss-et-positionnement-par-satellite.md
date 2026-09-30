---
title: ◆◆ GNSS et positionnement par satellite
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — infrastructure · **Couche** — percevoir, relier

**En une phrase.** Déterminer sa position en mesurant le temps de propagation de signaux émis par plusieurs satellites.

**Pourquoi on en parle.** Parce qu'une part considérable du monde technologique en dépend — et pas seulement pour se déplacer.

**Comment ça fonctionne.** Chaque satellite émet en continu un signal horodaté par une horloge très stable. Un récepteur qui reçoit plusieurs de ces signaux compare leurs temps d'arrivée et en déduit sa distance à chaque satellite, donc sa position. **Positionner, c'est fondamentalement mesurer du temps** — et le récepteur obtient donc, en prime, une référence temporelle d'une précision inaccessible autrement.

**Où vous rencontrerez le terme.** Navigation · logistique · agriculture de précision · construction · **synchronisation des réseaux de télécommunications** · **horodatage de transactions** · **corrélation d'événements de sécurité** · réseaux électriques.

**Ce que ça permet.** Une position et un temps, gratuitement, partout, avec un récepteur devenu négligeable en coût et en taille.

**Ce qui bloque.** **Le signal reçu est extrêmement faible.** Il provient d'émetteurs distants de milliers de kilomètres et arrive au sol à un niveau très bas — il est donc facilement perturbable, y compris involontairement. Il ne fonctionne pas en intérieur, sous l'eau, sous terre, et mal en environnement urbain dense où les réflexions produisent des erreurs. Enfin, **les signaux civils historiques ne sont pas authentifiés** : rien dans le signal n'atteste son origine.

**Ce que cela implique.** C'est l'exemple le plus net de ce que le chapitre 2 appelle une **infrastructure** : un système dont d'innombrables autres dépendent sans le posséder, sans l'avoir choisi et souvent sans le savoir. La dépendance la plus critique n'est pas la navigation — c'est **le temps**.

**Sûreté et sécurité.** En cas de perte du signal, les systèmes ne s'arrêtent pas tous : certains basculent sur une référence interne et **dérivent lentement**, d'autres continuent avec une position ou un temps faux. La dégradation est progressive, hétérogène et silencieuse — la pire combinaison pour un diagnostic. Les parades relèvent du principe : référence de temps locale de bonne stabilité, constellations multiples, croisement avec des sources non spatiales, contrôle de vraisemblance.

**À ne pas confondre avec.** **« GPS »**, qui désigne l'une des constellations et s'emploie abusivement comme nom générique. **Les systèmes d'augmentation**, qui améliorent la précision par des corrections transmises séparément.

> ⏱ **État au 23/08/2026** — 🏭 déployé, infrastructure critique. Plusieurs constellations opérationnelles ; l'authentification des signaux civils progresse mais le parc de récepteurs déployés ne l'exploite pas.
> 🔄 **À revoir si** une part significative du parc de récepteurs critiques bascule sur des signaux authentifiés — ou si une source de temps alternative de précision comparable devient largement disponible.

**Renvois** — Couche : percevoir, relier · Convergences : autonomie mobile (39), intelligence distribuée (38) · Voir aussi : chapitre 45 — les dépendances que personne n'a décidées.

---
