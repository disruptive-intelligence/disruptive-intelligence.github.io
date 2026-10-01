---
title: Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

> **Angle mort corrigé dans ce chapitre.** Une application peut être vulnérable **sans qu'aucune de ses dépendances ne le soit**. Le MCS applicatif ne se réduit pas à mettre à jour des bibliothèques : il commence par le code que vous avez écrit vous-même.

---

## A — Le code détenu par l'organisation

## 25.1 Les vulnérabilités du code propriétaire

Elles n'ont pas d'identifiant, ne figurent dans aucune base, et aucun scanner du chapitre 15 ne les remontera. Elles constituent pourtant une part importante des chemins d'entrée réels.

| Famille | Ce que c'est | Comment on la découvre |
|---|---|---|
| **Défaut d'autorisation** | Un utilisateur accède à des données qui ne sont pas les siennes en modifiant un identifiant | Test d'intrusion, signalement client |
| **Injection** | Une entrée utilisateur est interprétée comme instruction | Analyse statique, test d'intrusion |
| **Erreur de logique métier** | Le processus permet une opération non prévue — remise cumulée, étape sautée | Test métier, incident |
| **Contrôle d'entrée insuffisant** | Données non validées côté serveur | Analyse, test |
| **Fuite d'information** | Messages d'erreur détaillés, données superflues dans une réponse | Test, observation |
| **Faiblesse cryptographique propre** | Algorithme inadapté, aléa prévisible, secret codé en dur | Revue de code |
| **Point d'administration exposé** | Fonction technique accessible sans contrôle | Découverte externe (ch. 11) |
| **Code historique non maintenu** | Fonctionnalité ancienne que plus personne ne comprend | Revue, incident |

**Le défaut d'autorisation mérite une mention particulière** : il figure de façon constante en tête des classements de vulnérabilités applicatives établis par les référentiels du domaine, sa détection automatique est difficile — elle dépend entièrement des règles et des jeux de tests utilisés —, et il ne produit aucune anomalie technique — l'application fonctionne parfaitement, elle répond simplement à des demandes auxquelles elle ne devrait pas répondre.

## 25.2 Les sources de constats applicatifs

| Source | Ce qu'elle trouve bien | Ce qu'elle manque |
|---|---|---|
| **Analyse statique du code** | Injections, secrets codés en dur, motifs dangereux | Logique métier, autorisation |
| **Analyse dynamique** | Comportements observables sur l'application en fonctionnement | Ce qui n'est pas atteint par les tests |
| **Test d'intrusion applicatif** | **Autorisation, logique métier, enchaînements** | Ce qui est hors périmètre ou hors budget |
| **Programme de récompense** | Ce qu'un attaquant réel trouverait | Nécessite maturité et budget |
| **Revue de code** | Faiblesses de conception | Coûteuse, non exhaustive |
| **Retours clients et incidents** | Le réel | Trop tard |

**La règle du §14.2 s'applique intégralement** : tous ces constats entrent dans **la même file** que les vulnérabilités de composants, avec la même priorisation. C'est ce qui évite qu'un défaut d'autorisation découvert en test d'intrusion progresse moins vite qu'une bibliothèque à mettre à jour.

## 25.3 Affecter un constat applicatif

La difficulté est différente de celle du chapitre 17 : le correcteur n'est pas un exploitant mais une **équipe de développement**, dont la charge est planifiée par sprints et arbitrée par un responsable produit.

**Les trois frictions caractéristiques :**

| Friction | Manifestation | Traitement |
|---|---|---|
| Concurrence avec le fonctionnel | Le correctif de sécurité concurrence des fonctionnalités attendues | Réserver une capacité fixe par cycle (10 à 20 %), négociée une fois |
| Absence de propriétaire de composant | Le code appartient à « l'équipe » | Propriété nominative par composant, comme pour les actifs (§5.5) |
| Constat mal formulé | « Vulnérabilité XSS » sans contexte | Fournir : chemin de reproduction, impact métier, correction attendue |

✅ **BONNE PRATIQUE (P0)** — Négociez une **capacité de sécurité récurrente** dans la planification des équipes de développement, plutôt que de négocier chaque correctif. C'est exactement le pré-arbitrage du §9.4 transposé au développement, et cela supprime la discussion à chaque constat.

## 25.4 Le cycle de remédiation applicative

```
Constat
   ↓  reproduire — sinon on corrige à l'aveugle
Reproduction documentée
   ↓  analyser la cause racine — pas seulement le symptôme
Cause racine identifiée
   ↓  corriger le code
Correction
   ↓  test de sécurité : le chemin de reproduction échoue-t-il désormais ?
Test de sécurité passé
   ↓  test de non-régression fonctionnelle
Validation
   ↓  déploiement progressif (§6.4)
Déploiement
   ↓  vérification en production
Vérifié
   ↓  AJOUT D'UN TEST PERMANENT
Clos
```


**La dernière étape est celle qui distingue une correction d'une correction durable.** Le test qui reproduisait la vulnérabilité entre dans la suite de tests automatisés. Il échouera si quelqu'un réintroduit le défaut — dans six mois, lors d'une refactorisation, par une autre personne. Sans lui, la même vulnérabilité réapparaîtra, et vous la découvrirez au prochain test d'intrusion, deux ans plus tard.

**L'analyse de cause racine** mérite d'être conduite au-delà du cas isolé : si un défaut d'autorisation existe sur un point d'accès, la question est *combien d'autres points d'accès présentent le même défaut ?* Corriger un cas et ignorer la classe est le gaspillage le plus courant du domaine.

## 25.5 Branches de maintenance et rétroportage

Si votre produit est déployé chez des clients en plusieurs versions, corriger la version courante ne suffit pas.

| Question | Décision à formaliser |
|---|---|
| Combien de versions maintenez-vous en sécurité ? | Deux ou trois au maximum — au-delà, la charge devient ingérable |
| Rétroportez-vous les correctifs de sécurité ? | Oui pour les versions maintenues, avec le mécanisme du §2.2 |
| Publiez-vous un correctif ponctuel ou une version complète ? | Le correctif ponctuel accélère l'adoption ; la version complète simplifie la maintenance |
| Comment les clients apprennent-ils qu'ils doivent mettre à jour ? | C'est le chapitre 33 |

## 25.6 Mesures temporaires côté applicatif

Quand la correction demande du temps, la hiérarchie du §20.2 s'applique avec des moyens propres au logiciel :

| Mesure | Délai | Réversibilité |
|---|---|---|
| Désactiver la fonctionnalité concernée | Minutes si un interrupteur existe (§6.5) | Immédiate |
| Restreindre l'accès à la fonctionnalité | Heures | Immédiate |
| Ajouter une validation supplémentaire en amont | Heures à jours | Simple |
| Règle de filtrage applicatif en frontal | Heures | Immédiate |
| Surveillance ciblée sur le chemin vulnérable | Heures | — |

**Les sept attributs du §20.7 s'appliquent intégralement**, et notamment la date d'expiration. Un interrupteur de fonctionnalité désactivé « en attendant le correctif » rejoint sinon les 400 interrupteurs oubliés du §6.5.

---

## B — Politique de versions applicatives

## 25.7 Définir la politique

Sept décisions à prendre une fois, et à écrire :

| Décision | Question |
|---|---|
| Version courante | Laquelle est la référence ? |
| Versions supportées en sécurité | Combien, et lesquelles ? |
| Nombre maximal de branches | Au-delà, chaque correctif coûte N fois |
| Durée de support | Combien de temps après la publication d'une version ? |
| Critères de fin de support | Date fixe, nombre de versions ultérieures, seuil d'adoption ? |
| Préavis | Combien de temps avant la fin de support d'une version ? |
| Obligation de migration | Le support est-il conditionné à une version minimale ? |

## 25.8 Interfaces anciennes et compatibilité

Les points d'accès dépréciés sont des actifs à part entière : ils portent du code, souvent ancien, souvent moins protégé que les nouveaux, et souvent maintenus « parce qu'un client les utilise encore ».

**Le traitement** : les inventorier, mesurer leur usage réel, publier une date de retrait, et les traiter comme un décommissionnement (chapitre 35) — avec préavis, communication et vérification qu'ils ne sont plus appelés.

## 25.9 La dette de version applicative

Elle se mesure, comme la dette d'obsolescence du §12.6 : nombre de clients sur une version non supportée, ancienneté moyenne des versions déployées, nombre de branches maintenues, charge consommée par le rétroportage.

**L'argument à porter en interne** : chaque branche supplémentaire maintenue multiplie le coût de chaque correctif de sécurité. Réduire le nombre de branches n'est pas un confort d'équipe de développement, c'est une mesure de MCS.

---

## C — Chaîne logicielle et dépendances

## 25.10 Le code que vous n'avez pas écrit

Dans une application moderne, une part souvent importante — parfois majoritaire — du code exécuté provient de bibliothèques externes, elles-mêmes dépendantes d'autres bibliothèques (§3.6). Cette part est rarement inventoriée, et c'est le problème.

**Trois conséquences directes pour le MCS :**

1. Votre surface d'attaque comprend le code de dizaines d'organisations que vous ne connaissez pas.
2. Vous ne contrôlez ni le rythme de correction, ni la qualité, ni la pérennité de ces composants.
3. Une vulnérabilité dans une bibliothèque très répandue vous concerne **en même temps que des dizaines de milliers d'autres organisations** — donc dans un contexte où l'exploitation automatisée démarre en quelques heures.

## 25.11 L'inventaire des composants logiciels en pratique

| Question | Réponse opérationnelle |
|---|---|
| **Quand le générer ?** | À la construction, automatiquement. Un inventaire produit manuellement est périmé le jour de sa production |
| **Quelle granularité ?** | Composants directs **et** transitifs, avec versions exactes |
| **Où le stocker ?** | Associé à l'artefact produit, versionné, conservé aussi longtemps que la version est déployée |
| **Comment l'exploiter ?** | Rapproché en continu des sources de vulnérabilités, **rejoué à chaque nouvelle publication** |

⚠️ **PIÈGE — l'inventaire produit et jamais consommé**
C'est la situation la plus fréquente : l'organisation génère des inventaires de composants parce qu'un client ou un texte l'exige, les archive, et ne les rapproche jamais d'une base de vulnérabilités. Le document existe, la capacité n'existe pas. **La question qui tranche** : quand une vulnérabilité majeure est publiée dans une bibliothèque très répandue, combien de temps vous faut-il pour répondre « suis-je concerné, sur quels produits, dans quelles versions ? » Si la réponse dépasse quelques heures, votre inventaire ne sert à rien.

## 25.12 Analyse de composition et atteignabilité

L'analyse de composition rapproche vos dépendances déclarées des vulnérabilités connues. Elle produit beaucoup de bruit, pour des raisons structurelles :

| Cause de bruit | Mécanisme |
|---|---|
| Dépendances transitives | La vulnérabilité est à trois niveaux de profondeur, vous ne l'avez pas choisie |
| Composant non chargé | Présent dans les dépendances, jamais utilisé à l'exécution |
| Fonction non atteignable | Le composant est utilisé, mais pas la fonction vulnérable (§11.6) |
| Version corrigée par l'écosystème | Résolution de version différente de la déclaration |

**Le traitement** : appliquer l'arbre du §16.3, en utilisant l'atteignabilité comme critère de dépriorisation documentée — jamais de clôture (§16.6).

## 25.13 Politique de mise à jour des dépendances

| Approche | Principe | Risque |
|---|---|---|
| **Automatisée avec tests** | Un mécanisme propose les montées de version, les tests décident | Le meilleur rapport effort/résultat, si les tests existent |
| **Périodique groupée** | Une campagne mensuelle de mise à jour des dépendances | Simple, mais le retard s'accumule entre deux campagnes |
| **À la demande** | On met à jour quand une vulnérabilité l'impose | Chaque mise à jour devient une montée de plusieurs versions, donc risquée |

**Le cercle vicieux à connaître** : moins on met à jour, plus l'écart grandit, plus chaque mise à jour devient risquée, donc moins on met à jour. La mise à jour fréquente et automatisée est **moins risquée** que la mise à jour rare, contrairement à l'intuition — chaque saut est petit.

## 25.14 La santé d'une dépendance

Une dépendance saine aujourd'hui peut devenir un problème demain. Six signaux à surveiller sur les composants critiques :

| Signal | Ce qu'il annonce |
|---|---|
| Fréquence de publication en baisse | Projet en perte de vitesse |
| **Un seul mainteneur actif** | Fragilité majeure : maladie, lassitude, changement de vie |
| Signalements de sécurité sans réponse | Le projet ne traitera pas vos vulnérabilités |
| Changement de mainteneur ou de propriétaire | À examiner : plusieurs compromissions ont emprunté cette voie |
| Archivage ou dépréciation annoncée | Migration à planifier |
| Absence de politique de sécurité déclarée | Aucun canal pour signaler ou recevoir |

✅ **BONNE PRATIQUE (P1)** — Identifiez vos dix à vingt dépendances les plus critiques — celles dont l'abandon vous poserait un vrai problème — et surveillez ces six signaux. C'est un exercice annuel, pas continu.

## 25.15 Les attaques sur la chaîne d'approvisionnement

| Technique | Principe | Défense principale |
|---|---|---|
| **Typosquattage** | Un paquet au nom proche d'un paquet légitime | Verrouillage des versions, registre interne, revue des ajouts |
| **Confusion de dépendances** | Un paquet public prend la place d'un paquet interne homonyme | Espaces de noms réservés, priorité explicite du registre interne |
| **Compromission de mainteneur** | Le compte légitime publie une version malveillante | Verrouillage, délai avant adoption d'une version, vérification de provenance |
| **Compromission de la chaîne de construction** | L'attaquant modifie l'artefact produit | Protection des agents (ch. 28), attestations de provenance |
| **Dépendance abandonnée reprise** | Un tiers reprend un paquet inactif | Surveillance des changements de mainteneur (§25.14) |

**La défense la plus efficace et la moins coûteuse** : un **délai avant adoption** des nouvelles versions de dépendances — quelques jours suffisent à ce que la communauté détecte la majorité des paquets malveillants. C'est le délai d'observation du §18.3, transposé aux dépendances.

## 25.16 Provenance et intégrité

| Mécanisme | Ce qu'il garantit |
|---|---|
| Verrouillage des versions | Vous obtenez exactement ce que vous avez validé |
| Registre interne avec approbation | Vous contrôlez ce qui entre |
| Vérification d'empreinte ou de signature | L'artefact n'a pas été modifié |
| Attestation de provenance | L'artefact vient bien de la chaîne de construction attendue |
| Construction reproductible | La même source produit le même artefact — permet la vérification indépendante |

**L'ordre d'adoption réaliste** : verrouillage d'abord (immédiat, gratuit), registre interne ensuite (structurant), vérification et attestations après. Les constructions reproductibles sont un objectif exigeant, à ne pas placer en tête d'un programme.

## 25.17 Images de base et registres

Une image de conteneur hérite de tout ce que contient son image de base. Trois règles suffisent :

1. **Choisir des images de base minimales** — moins de composants, moins de vulnérabilités, moins de reconstruction.
2. **Fixer une cadence de reconstruction** (§3.2) : c'est l'indicateur qui remplace des centaines de constats individuels.
3. **Contrôler à la publication** dans le registre, pas à l'exécution : une image non conforme ne doit pas pouvoir être publiée (§22.4).

## 25.18 Protéger la chaîne de construction

Traité en profondeur au chapitre 28. Trois points à retenir ici : les agents d'exécution disposent d'accès étendus et échappent souvent à l'inventaire ; les secrets de la chaîne sont un objectif de premier ordre ; et une compromission de la chaîne contamine **tous** les artefacts produits, y compris ceux livrés à vos clients.

## 25.19 Déclarations d'exploitabilité et avis lisibles par machine

Le §4.8 a présenté les formats. Voici l'usage réel, dans les deux sens :

**En consommation.** Un fournisseur vous déclare qu'un composant vulnérable présent dans son produit n'est pas exploitable. Cela vous permet de dépriorer sans analyser — à condition de conserver la déclaration comme justification, et de la réexaminer si le contexte change.

**En production.** Si vous éditez un produit, ces déclarations vous évitent de recevoir cent fois la même question de vos clients à chaque vulnérabilité majeure d'une bibliothèque répandue. C'est un gain considérable pour le PSIRT (chapitre 33).

📌 **LIMITES** — La maturité de l'outillage reste inégale, et l'adoption est très variable selon les éditeurs. Ne construisez pas un processus qui **dépend** de la réception de ces déclarations : traitez-les comme un enrichissement quand elles arrivent.

## 25.20 ⚖️ Ce que la réglementation produit impose sur les composants

Pour les fabricants de produits numériques, les obligations émergentes portent notamment sur : la fourniture d'un inventaire des composants, la gestion des vulnérabilités affectant les composants tiers, la mise à disposition de correctifs pendant une durée déterminée, et la notification des vulnérabilités activement exploitées. Le détail et le calendrier figurent au chapitre 33.

**La conséquence pratique**, même sans être fabricant : ces exigences se propagent le long de la chaîne (§13.7). Vos fournisseurs devront vous fournir ces éléments, et vos clients vous les demanderont.

## 25.21 📌 Limites

- **Le code sans propriétaire** : une application dont l'équipe a été dissoute ne sera pas corrigée, quelle que soit la qualité du constat.
- **L'éditeur métier non coopératif** : vous détectez, il ne corrige pas. C'est un sujet contractuel (ch. 13), pas technique.
- **L'application sans jeu de tests** : corriger devient un pari, et le pari est souvent perdu — d'où le report systématique.
- **Le coût d'un correctif dans du code non testé** peut dépasser celui d'une réécriture partielle. Cela doit être dit, chiffré, et arbitré.

## 25.22 🔴 FIL ROUGE — octobre 2027 : ce que contenait HelioLink

La R&D de Nantes produit son premier inventaire complet des composants d'HelioLink, dans le cadre de la préparation réglementaire produit.

**Les chiffres.**

| Élément | Nombre |
|---|---|
| Dépendances directes déclarées | 87 |
| Dépendances totales, transitives incluses | **1 412** |
| Portant une vulnérabilité connue | 156 |
| Après analyse d'atteignabilité | **12 réellement problématiques** |
| Composants sans mainteneur actif depuis > 2 ans | 9 |
| Composants dont le mainteneur a changé en 2026-2027 | 3 |

**Le rapport 156 → 12** est ce qui frappe l'équipe. L'analyse d'atteignabilité et les déclarations d'exploitabilité de trois fournisseurs éliminent 92 % du volume. Les 12 restants sont traités en trois semaines.

**Mais ce n'est pas la découverte importante du mois.**

En parallèle, le test d'intrusion applicatif annuel — commandé pour la première fois sur HelioLink — remonte un **défaut d'autorisation** : en modifiant un identifiant dans une requête, un utilisateur authentifié d'un établissement de santé peut consulter les données de télésuivi des patients d'un **autre** établissement.

Aucun scanner ne l'aurait trouvé. Aucun inventaire de composants ne l'aurait signalé. Le code fonctionne exactement comme il a été écrit. Et la vulnérabilité existe depuis la première version, mise en service en 2023.

**Le traitement, selon le §25.4.**

1. **Reproduction** documentée en une heure.
2. **Cause racine** : le contrôle d'appartenance à l'établissement est effectué à l'affichage, côté interface, mais pas dans le service qui sert les données.
3. **Extension de l'analyse** — et c'est le point décisif : combien d'autres points d'accès présentent le même défaut ? Réponse après revue : **quatre autres**, dont deux exposant des données de santé.
4. **Correction** des cinq points, avec contrôle centralisé plutôt que répété.
5. **Test permanent** ajouté à la suite automatisée : cinq tests vérifient désormais qu'un utilisateur d'un établissement ne peut pas accéder aux données d'un autre.
6. **Mesure temporaire** pendant les onze jours de développement : journalisation renforcée et alerte sur tout accès inter-établissements, avec destinataire nommé.

**La question qui occupe le comité de direction.** Léa Cassin, déléguée à la protection des données, pose la question inévitable : cette faille a existé quatre ans ; a-t-elle été exploitée ? Les journaux d'accès applicatifs sont conservés 90 jours. Sur cette période, aucun accès anormal n'est constaté. Sur les quatre années précédentes, **la question reste sans réponse** — exactement comme en juillet (§21.11), et pour la même raison.

**Ce que la direction décide.** Journalisation applicative portée à 24 mois sur HelioLink, avec export indépendant. Test d'intrusion applicatif annuel inscrit au budget récurrent. Et une capacité de sécurité de 15 % réservée dans chaque cycle de développement (§25.3).

**Ce que Yann Prigent écrit dans son rapport** : *nous avons passé six mois à surveiller 1 412 dépendances. La vulnérabilité la plus grave de notre produit, nous l'avions écrite nous-mêmes.*

→ La suite en 🔴 §26.13, quand un progiciel métier imposera son environnement d'exécution.

→ **Chapitre 26 — Bases de données, middlewares et *runtimes*** : la couche intermédiaire, source d'obsolescence invisible.

## Synthèse mentale du chapitre 25

Une application peut être vulnérable sans qu'aucune de ses dépendances ne le soit : le défaut d'autorisation, le plus fréquemment exploité en conditions réelles, est invisible à l'analyse automatique et ne produit aucune anomalie technique. Les constats applicatifs entrent dans la même file que les vulnérabilités de composants, et la friction propre au développement se traite par une capacité de sécurité réservée dans chaque cycle plutôt que par une négociation à chaque constat. Le cycle de remédiation applicative se termine par l'ajout d'un test permanent — sans lui, la même vulnérabilité réapparaîtra lors d'une refactorisation dans six mois. L'analyse de cause racine doit s'étendre à la classe entière : corriger un cas et ignorer les quatre autres points d'accès identiques est le gaspillage le plus courant. Côté dépendances, la mise à jour fréquente et automatisée est moins risquée que la mise à jour rare, contrairement à l'intuition, et un délai de quelques jours avant adoption d'une nouvelle version est la défense la plus rentable contre les paquets malveillants. Enfin, un inventaire de composants qui ne permet pas de répondre en quelques heures à « suis-je concerné » n'a aucune utilité.

**Trois questions de vérification**

1. Votre analyse de composition est parfaite et votre parc de dépendances est à jour. Quelle catégorie de vulnérabilité reste entièrement invisible, et comment la découvre-t-on ?
2. Pourquoi mettre à jour ses dépendances rarement est-il plus risqué que les mettre à jour souvent ?
3. Un défaut d'autorisation est corrigé sur un point d'accès. Quelles deux actions restent indispensables avant de clore le constat ?

---
