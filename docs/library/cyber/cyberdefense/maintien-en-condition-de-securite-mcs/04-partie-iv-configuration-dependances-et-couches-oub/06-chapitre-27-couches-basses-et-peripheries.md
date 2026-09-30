---
title: Chapitre 27 — Couches basses et périphéries
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

## 27.1 Micrologiciels : inventaire, déploiement, risque

Le §3.8 a posé les mécanismes. Voici la mise en œuvre.

**Ce qui compose réellement cette couche**, et qui est presque toujours sous-estimé :

| Objet | Où il se trouve | Fréquence de mise à jour constatée |
|---|---|---|
| Micrologiciel de carte mère | Tout serveur, tout poste | Rarement, souvent jamais |
| Contrôleur de gestion à distance | Serveurs physiques | Presque jamais — et c'est un accès privilégié complet |
| Micrologiciel de disque, de contrôleur de stockage | Serveurs, baies | Uniquement lors d'incidents |
| Cartes réseau, cartes d'extension | Serveurs | Jamais |
| Micrologiciel d'équipement réseau | Commutateurs, points d'accès | Traité au §19.6 |
| Périphériques | Imprimantes, caméras, contrôle d'accès | Jamais |

⚠️ **Le contrôleur de gestion à distance mérite un traitement particulier.** Il permet d'allumer, éteindre, réinstaller et prendre la main sur un serveur, indépendamment du système d'exploitation. Il dispose de sa propre pile réseau, de sa propre interface d'administration et de ses propres comptes — souvent les comptes par défaut du constructeur. C'est un **actif de niveau 0** au sens du §11.7, et il est presque systématiquement absent des inventaires.

**Les trois vérifications prioritaires** sur ces contrôleurs : sont-ils sur un réseau d'administration séparé ? les comptes par défaut ont-ils été changés ? à quelle version sont-ils ?

**Le déploiement**, quand il est décidé : il suit les anneaux du §18.4, avec deux précautions supplémentaires — un micrologiciel interrompu en cours d'écriture peut rendre le matériel inutilisable, et l'ordre entre composants importe (contrôleur de gestion avant carte mère, généralement).

## 27.2 Le risque *pre-boot*

Un composant qui s'exécute avant le système d'exploitation ne peut pas être surveillé par les protections qui s'exécutent dedans. Une compromission à ce niveau survit à une réinstallation complète, et parfois au remplacement du disque.

**Ce qui protège réellement, dans l'ordre :**

1. **Le démarrage sécurisé activé** — sans lui, les autres mécanismes ne servent à rien.
2. **Les bases de certificats à jour** — c'est le cas du §3.8, dont la dégradation est silencieuse.
3. **Le mot de passe de configuration du micrologiciel** — sans lui, quiconque a un accès physique désactive le reste.
4. **Le chiffrement du disque avec liaison au matériel** — rend inefficace l'extraction du disque.
5. **La protection contre le retour en arrière** du micrologiciel.

📌 **LIMITES** — Ces mesures se décident **à l'achat et au déploiement initial**. Les activer sur un parc existant est possible mais coûteux, et certaines opérations — activer le démarrage sécurisé, changer le mode de démarrage — peuvent nécessiter une réinstallation. C'est un cas typique où le MCS *by design* du chapitre 6 se paie très cher quand il a été négligé.

## 27.3 Équipements réseau et de sécurité : la fin de support de sécurité

Le §19.6 a traité le déploiement. Un point spécifique mérite d'être isolé, parce qu'il est méconnu et coûteux.

**Trois dates coexistent** sur un équipement réseau, et elles ne sont pas simultanées :

| Date | Signification |
|---|---|
| Fin de commercialisation | On ne peut plus l'acheter |
| **Fin de support de sécurité** | **Plus aucun correctif de sécurité — la seule qui compte pour le MCS** |
| Fin de support matériel | Plus de remplacement, plus d'assistance |

La fin de support de sécurité est souvent **antérieure de plusieurs années** à la fin de support matériel. Un équipement sous contrat de maintenance actif, remplacé en cas de panne, peut ne plus recevoir aucun correctif depuis longtemps. L'organisation, elle, a le sentiment d'un équipement « sous contrat ».

✅ **BONNE PRATIQUE (P0)** — Suivez la date de fin de support **de sécurité** dans votre référentiel d'obsolescence (§12.2), distinctement des autres. C'est cette date qui déclenche le remplacement, pas la panne.

## 27.4 Appliances et boîtiers fournisseur

Une appliance est une boîte noire dont vous ne maîtrisez ni le système, ni les composants, ni le calendrier.

| Caractéristique | Conséquence pour le MCS |
|---|---|
| Système d'exploitation non accessible | Vous ne pouvez ni scanner, ni corriger, ni durcir |
| Composants tiers non déclarés | Vous ne savez pas ce qu'elle embarque (§26.7) |
| Correctifs au rythme du fournisseur | Vous héritez de son délai |
| Mises à jour parfois imposées | Un changement peut survenir sans votre accord |
| Fin de vie décidée par le fournisseur | Parfois brutale, avec préavis court |

**Les quatre exigences à porter au contrat** (§13.3) : délai d'application des correctifs de sécurité par le fournisseur, notification des vulnérabilités affectant le produit, inventaire des composants, et préavis de fin de support.

**En l'absence de ces exigences** — cas fréquent sur les équipements déjà installés — le traitement est celui du chapitre 20 : mesurer l'exposition, isoler, surveiller, et documenter le risque accepté.

## 27.5 Périphériques et objets connectés d'entreprise

Imprimantes multifonctions, caméras, contrôle d'accès, visioconférence, affichage dynamique, capteurs de bâtiment.

**Pourquoi ils comptent réellement** :

- Ils sont **nombreux** et souvent connectés au réseau bureautique sans segmentation.
- Ils disposent de **fonctions étendues** : stockage, numérisation vers messagerie, comptes d'annuaire configurés, historiques de documents.
- Ils sont **rarement mis à jour** et parfois hors support depuis des années.
- Ils appartiennent souvent aux **services généraux**, pas à l'informatique.

**Le traitement réaliste**, sans prétendre à l'exhaustivité :

| Prio | Action |
|---|---|
| **P0** | Les inventorier et identifier un propriétaire — souvent hors DSI (§5.5) |
| **P0** | Changer les comptes par défaut, désactiver les services inutiles |
| **P0** | Les segmenter : aucun besoin d'être joignables depuis tout le réseau |
| P1 | Vérifier les comptes d'annuaire qu'ils utilisent — souvent surprivilégiés |
| P1 | Suivre leur fin de support avec le reste du parc |
| P2 | Mettre à jour les micrologiciels, par lots |

## 27.6 ⚠️ Les équipements de sécurité comme cible privilégiée

Un constat désormais établi : les équipements de sécurité exposés — passerelles d'accès distant, pare-feu, contrôleurs d'accès réseau — figurent parmi les cibles les plus recherchées.

**Les raisons sont structurelles**, et il faut les comprendre plutôt que les subir :

1. Ils sont **exposés par conception** — c'est leur fonction.
2. Ils disposent d'**accès étendus** au système d'information.
3. Ils sont **peu surveillés de l'intérieur** : on y installe rarement des agents de détection.
4. Ils sont **difficiles à corriger** : interruption de service, fenêtre rare, doctrine de version prudente (§2.7).
5. Une compromission y est **persistante** : elle survit souvent au correctif.

**Ce que cela impose au MCS**, et qui découle directement du fil rouge de juillet (§21.11) :

| Exigence | Prio |
|---|---|
| Classe C1 sans discussion, fenêtre récurrente dédiée | **P0** |
| Interface d'administration jamais publiée sur Internet | **P0** |
| Journalisation exportée hors de l'équipement, conservée longtemps | **P0** |
| Doctrine de version écrite, datée, revue (§2.7) | P1 |
| Après exploitation potentielle : **reconstruction**, pas correction | P1 |
| Configuration de référence permettant une reconstruction rapide | P1 |

## 27.7 🔴 FIL ROUGE — décembre 2027

la ligne « micrologiciels : non mesuré »

Depuis janvier 2026, la ligne « micrologiciels » du périmètre d'HELIOMED porte la mention *non couvert, propriétaire désigné, échéance de première mesure* (§3.9). Vingt-trois mois plus tard, Claire Nadeau la traite enfin — et elle explique au comité pourquoi elle l'a laissée en attente aussi longtemps.

**Le raisonnement assumé.** L'inventaire, l'exposition, la propriété d'actif, les comptes de service et le code applicatif produisaient chacun une réduction de risque supérieure pour un effort moindre. La ligne micrologiciels était déclarée, datée et visible : elle n'était pas oubliée, elle était **priorisée en dernier**, et cette décision figurait au compte rendu de chaque comité.

**La première mesure, en deux jours.**

| Constat | Résultat |
|---|---|
| Contrôleurs de gestion à distance des serveurs | 41 équipements, **tous sur le réseau bureautique**, 12 avec le compte constructeur par défaut |
| Micrologiciels de cartes mères serveurs | Version d'origine sur 38 des 41 |
| Micrologiciels des postes | Non mesurés — l'infogérant ne les remonte pas |
| Imprimantes multifonctions | 22 équipements, dont 6 hors support, 4 avec numérisation vers messagerie configurée avec un compte de service (§24.11) |
| Certificats de démarrage sécurisé | 214 postes n'ont pas reçu la mise à jour de 2026 |

**Ce qui est traité immédiatement, et ce qui ne l'est pas.**

*Traité en deux semaines, coût quasi nul* : les 12 comptes par défaut des contrôleurs de gestion, la segmentation des 41 contrôleurs sur un réseau d'administration séparé, et la désactivation de la numérisation vers messagerie sur les 4 imprimantes concernées.

*Planifié en 2028* : la mise à jour des micrologiciels de cartes mères, par lots, à l'occasion des redémarrages programmés. Aucune urgence identifiée, risque de brique réel, bénéfice modéré au regard de l'effort.

*Reporté avec justification* : le remplacement des 6 imprimantes hors support, inscrit au budget de renouvellement des services généraux pour 2029.

*Ajouté au contrat* : la remontée de l'état des micrologiciels des postes, dans le prochain avenant Numeria.

**Le point le plus instructif de l'épisode.** La segmentation des 41 contrôleurs de gestion à distance — deux jours de travail, aucun coût de licence — retire du réseau bureautique 41 accès permettant de prendre le contrôle complet de serveurs, indépendamment de leur système d'exploitation. Aucune de ces machines n'apparaissait dans les scans de vulnérabilités, aucune ne figurait dans les indicateurs, et aucune n'aurait jamais été détectée par le dispositif construit pendant deux ans.

**Ce que Claire écrit en conclusion.** *Déclarer un périmètre non mesuré ne le rend pas sûr. Mais cela garantit qu'il sera traité un jour, et qu'entre-temps personne ne croira qu'il l'a été.*

→ La suite en 🔴 §28.10, quand un agent d'exécution de la chaîne de construction se révélera administrateur du cluster.

→ **Chapitre 28 — Environnements non productifs et actifs d'administration** : les environnements que personne ne regarde.

## Synthèse mentale du chapitre 27

Le contrôleur de gestion à distance des serveurs est un actif de niveau 0 : il permet d'allumer, réinstaller et prendre la main indépendamment du système d'exploitation, dispose de ses propres comptes — souvent ceux du constructeur — et est presque systématiquement absent des inventaires. Le risque avant démarrage échappe à toutes les protections logicielles, et les mesures qui le traitent se décident à l'achat : les rétrofitter coûte très cher. Sur les équipements réseau, la fin de support **de sécurité** précède souvent de plusieurs années la fin de support matériel, ce qui donne le sentiment trompeur d'un équipement « sous contrat ». Les appliances sont des boîtes noires dont on hérite du calendrier : les quatre exigences se portent au contrat, avant l'installation. Enfin, les équipements de sécurité exposés sont des cibles privilégiées pour cinq raisons structurelles, et la conséquence opérationnelle est nette : après exploitation potentielle, on reconstruit plutôt qu'on corrige.

**Trois questions de vérification**

1. Vos scans de vulnérabilités ne remontent rien d'anormal sur vos serveurs. Quel équipement, présent sur chacun d'eux, échappe pourtant entièrement à cette mesure, et pourquoi est-il critique ?
2. Un équipement réseau est sous contrat de maintenance actif. Que devez-vous vérifier avant d'en conclure qu'il est maintenu en sécurité ?
3. Une passerelle d'accès distant a été exposée avec une vulnérabilité exploitable. Le correctif est appliqué. Pourquoi n'est-ce pas suffisant ?

---
