---
title: Chapitre 15 — Détection technique de l'exposition
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

Le chapitre 14 vous informe qu'une vulnérabilité existe. Celui-ci répond à la question suivante : **est-elle présente chez moi, et où exactement ?** C'est le chapitre des outils — et surtout de ce qu'ils ne savent pas faire.

## 15.1 Les familles d'outils et ce que chacune peut savoir

| Famille | Principe | Ce qu'elle peut établir | Ce qu'elle ne peut pas |
|---|---|---|---|
| **Scan réseau non authentifié** | Interroge les services exposés depuis le réseau | Ce qui répond, bannières, comportements observables | L'état interne de la machine |
| **Scan authentifié** | Se connecte avec un compte et inventorie | Versions exactes, correctifs installés, configuration | Ce qui n'est pas accessible au compte utilisé |
| **Agent installé** | Programme résident qui remonte l'état en continu | État permanent, y compris hors réseau | L'état des machines sans agent |
| **Analyse de composition logicielle** | Lit les dépendances déclarées d'une application | Composants tiers et versions | L'atteignabilité réelle du code (§11.6) |
| **Analyse d'image de conteneur** | Inspecte les couches d'une image | Composants embarqués avant déploiement | Ce qui est ajouté à l'exécution |
| **Découverte externe** | Vue depuis Internet | La surface réellement publiée (ch. 11) | Tout l'interne |
| **Validation d'exploitabilité** | Tente une exploitation contrôlée | La démonstration qu'un chemin fonctionne | Le reste du parc, et le risque de l'essai |

**Le principe de complémentarité, à retenir.** Ces familles ne se substituent pas. Un agent ne dit rien de l'exposition réseau ; un scan externe ne dit rien de l'état interne ; une analyse de composition ne voit pas ce que le système d'exploitation embarque. Une organisation qui n'utilise qu'une famille a nécessairement un angle mort structurel, et il est prévisible.

## 15.2 Ce qu'un scan non authentifié ne peut pas savoir

Le scan non authentifié observe un système de l'extérieur, sans identifiants. Il en déduit des informations à partir de ce que les services exposés laissent voir.

**Sa méthode d'inférence, et sa fragilité.** Il lit une bannière annonçant une version, observe un comportement caractéristique, teste une réponse. Puis il conclut à partir d'une base de correspondance version ↔ vulnérabilité.

**Les quatre sources de faux positifs structurels** :

| Cause | Mécanisme |
|---|---|
| **Rétroportage** | La bannière annonce une version amont ancienne, le correctif est présent (§2.2). C'est la première cause, et de loin |
| **Bannière modifiée** | Certaines configurations masquent ou falsifient la version annoncée |
| **Composant présent mais désactivé** | Le module vulnérable est installé, non chargé |
| **Correspondance approximative** | Le produit détecté n'est pas exactement celui de la base (§4.3) |

**Ce qu'il détecte que rien d'autre ne détecte**, et qui justifie son usage malgré tout : ce qui est **réellement joignable**. Un scan authentifié vous dira qu'un service est installé ; seul un scan non authentifié depuis un point donné du réseau vous dira qu'il répond depuis cet endroit. C'est une information d'exposition (chapitre 11), pas de vulnérabilité — et c'est sa vraie valeur.

## 15.3 Le scan authentifié, et la protection de ses secrets

Le scan authentifié se connecte à la machine avec un compte et lit directement l'état du système : paquets installés, révisions, correctifs, configuration. Il est **incomparablement plus fiable** et devrait constituer le mode par défaut sur tout le parc que vous administrez.

**Le compte de scan est un actif de niveau 0.** Il dispose d'un accès en lecture privilégié sur l'ensemble du parc, et ses identifiants sont stockés dans l'outil de scan. Quiconque compromet cet outil obtient un accès à tout le périmètre scanné.

✅ **BONNE PRATIQUE (P0) — les six règles du compte de scan**

1. Un compte **dédié**, jamais un compte d'administration existant réutilisé.
2. Les **privilèges minimaux** nécessaires à la lecture — pas d'administration complète quand la lecture suffit.
3. **Interdiction d'ouverture de session interactive** pour ce compte.
4. **Rotation** régulière du secret, et vérification que la rotation est bien répercutée dans l'outil (§24.10).
5. **Surveillance** de son usage : toute utilisation en dehors des fenêtres de scan est une alerte.
6. **Cloisonnement** : idéalement, un compte distinct par zone de sécurité, pour qu'une compromission ne donne pas tout le parc.

## 15.4 La sécurité de l'outil lui-même

Prolongement direct du point précédent, et l'un des angles morts les plus fréquents.

Un outil de scan de vulnérabilités concentre : les identifiants privilégiés du §15.3, la **cartographie complète** de vos faiblesses, et souvent une capacité d'exécution à distance. C'est un actif de niveau 0 au sens du §11.7, et il est fréquemment traité comme un outil secondaire — installé une fois, rarement mis à jour, avec une interface d'administration accessible largement.

⚠️ **PIÈGE — la console de sécurité oubliée**
Le raisonnement implicite est toujours le même : « c'est un outil de sécurité, donc il est sécurisé ». Il n'y a aucun lien logique entre les deux. Les outils de sécurité — scanners, consoles de protection des postes, plateformes de journalisation, consoles de sauvegarde — figurent régulièrement parmi les composants les plus en retard d'un parc. Le chapitre 34 leur est consacré.

## 15.5 La fraîcheur de la base de détection

Un scanner ne détecte que ce qu'il sait détecter. Entre la publication d'un avis et la disponibilité du contrôle correspondant dans votre outil, il s'écoule un délai.

**Trois délais s'additionnent**, et c'est leur somme qui compte :

```
Publication de l'avis
   → l'éditeur de l'outil développe le contrôle          (heures à jours)
   → il le publie dans sa base                            (selon son rythme)
   → vous mettez à jour votre instance                    (selon VOTRE processus)
   → le prochain scan passe                               (selon votre cadence)
```


Le troisième délai est le seul que vous contrôlez entièrement, et c'est souvent le plus long. Une instance dont la base de détection date de trois semaines ne détectera aucune des vulnérabilités publiées depuis.

✅ **BONNE PRATIQUE (P0)** — Suivez la fraîcheur de la base de détection comme un indicateur à part entière, et rendez sa mise à jour automatique. C'est exactement le sujet du §1.3, ligne « contenu de détection » : votre outil de détection est lui-même un objet qui se dégrade quotidiennement.

⚠️ Pour toute vulnérabilité en crise (chapitre 21), **ne présumez jamais** que votre scanner la détecte. Vérifiez que le contrôle existe dans votre base, à sa version installée. Sinon, la vérification se fait autrement : requête sur l'inventaire par version, ou vérification directe sur un échantillon.

## 15.6 La couverture réelle : la calculer et la prouver

Le §10.11 a posé le principe ; voici la mise en œuvre.

**La formule**, qui suppose le périmètre de référence du chapitre 10 :

```
Couverture de scan = actifs scannés avec succès / actifs du périmètre de référence
```


**Les cinq populations à distinguer**, parce que les confondre produit la totalité des malentendus sur ce chiffre :

| Population | Signification | Traitement |
|---|---|---|
| Scannés avec succès, authentifiés | Donnée fiable | Base des indicateurs |
| Scannés, mais authentification échouée | Donnée dégradée, faux positifs probables | À corriger en priorité : compte, droits, filtrage |
| Non joignables au moment du scan | Éteints, nomades, intermittents | **À lister explicitement**, jamais à ignorer |
| Exclus volontairement | Systèmes industriels, actifs fragiles | Exclusion **documentée**, avec son motif et sa compensation |
| Hors périmètre de l'outil | Cloud, services en ligne, produits | Couverts par un autre moyen, ou déclarés non couverts |

⚠️ **PIÈGE — l'exclusion silencieuse**
Le mécanisme le plus insidieux de tout ce chapitre. Un actif provoque des dysfonctionnements pendant un scan ; on l'exclut « temporairement » ; l'exclusion n'est jamais revue. Deux ans plus tard, il ne figure plus dans aucun rapport — et comme il ne remonte aucune vulnérabilité, il améliore même les indicateurs.
**Le garde-fou** : la liste des exclusions est un document de gouvernance, revu au comité MCS, avec pour chacune un motif, un propriétaire, une compensation et une date de revue. Une exclusion sans date de revue est une dérogation déguisée qui échappe au processus du §7.4.

## 15.7 Identifiants d'actifs, historique et continuité

Un problème banal qui détruit silencieusement toute capacité de mesure dans la durée.

Les outils identifient les actifs par une clé interne, construite à partir du nom, de l'adresse, d'un identifiant matériel ou d'une combinaison. Quand cette clé change — machine renommée, redéploiement, changement d'adresse, réinstallation d'agent — l'outil crée un **nouvel actif** et perd l'historique de l'ancien.

**Les conséquences concrètes :**

- l'ancienneté d'un constat est réinitialisée, ce qui embellit artificiellement l'indicateur d'âge du *backlog* ;
- le nombre d'actifs augmente sans que le parc change, faussant tous les dénominateurs ;
- l'ancien actif reste dans l'outil, sans être scanné, et finit par disparaître des rapports ;
- une vulnérabilité récurrente (§17.9) apparaît comme nouvelle à chaque redéploiement.

✅ **BONNE PRATIQUE (P1)** — Définissez une règle d'identification stable, réconciliée avec l'inventaire du chapitre 10, et suivez deux indicateurs simples : le nombre d'actifs créés et supprimés dans l'outil par mois, et le nombre d'actifs présents dans l'outil mais absents du périmètre de référence. Une variation anormale de l'un ou de l'autre signale un problème d'identification, pas un changement de parc.

## 15.8 ⚠️ « Non détecté », « non vulnérable », « non scanné »

C'est la distinction la plus coûteuse du domaine quand elle n'est pas faite, et elle mérite d'être affichée dans les bureaux.

| Formulation | Ce que ça signifie vraiment |
|---|---|
| **Non vulnérable** | L'outil a examiné cet actif et a établi qu'il n'est pas affecté. **Information positive.** |
| **Non détecté** | L'outil a examiné l'actif et n'a rien trouvé — ce qui peut vouloir dire qu'il ne sait pas chercher cela. **Absence d'information.** |
| **Non scanné** | L'outil n'a pas examiné l'actif : injoignable, authentification échouée, exclu, hors périmètre. **Absence totale d'information.** |

**Les trois se présentent identiquement dans un rapport** : la ligne est vide, l'actif n'apparaît pas dans la liste des vulnérables. Un tableau de bord qui ne les distingue pas transforme une absence d'information en information rassurante.

🧪 **EN PRATIQUE — les trois questions à poser devant tout rapport de scan**

1. Combien d'actifs du **périmètre de référence** ce rapport couvre-t-il ?
2. Parmi eux, combien ont été scannés **avec authentification réussie** ?
3. Où est la liste des actifs **non scannés**, avec le motif ?

Un rapport qui ne permet pas de répondre à ces trois questions n'est pas exploitable pour piloter, et il n'a aucune valeur probante en audit (§5.6).

## 15.9 Cas particuliers par type d'environnement

| Environnement | Contrainte | Approche recommandée |
|---|---|---|
| **Systèmes industriels** | Le scan actif peut provoquer un défaut (§3.7) | Écoute passive du trafic, extraction depuis les outils d'ingénierie, inventaire manuel assumé (ch. 29) |
| **Équipements réseau et de sécurité** | Peu ou pas d'accès pour un scan authentifié | Inventaire de versions par requête d'administration, corrélation avec les avis constructeurs |
| **Hyperviseurs et appliances** | Accès restreint par l'éditeur | Interface de gestion, versions déclarées, avis fournisseur |
| **Conteneurs** | Éphémères, l'exécution n'est pas le bon moment | Analyse à la construction et dans le registre, pas sur les conteneurs en cours d'exécution |
| **Cloud** | Le scan réseau classique ne voit pas la configuration | Interrogation des interfaces du fournisseur, contrôle de posture (ch. 30) |
| **Postes nomades** | Rarement présents au moment du scan | Agent, obligatoirement — un scan réseau les manquera systématiquement |
| **Services en ligne** | Aucun accès technique | Revue de configuration, déclarations du fournisseur (ch. 31) |

⚠️ **PIÈGE — la saturation des cibles**
Un scan agressif peut dégrader ou faire tomber des services fragiles : équipements anciens, imprimantes, systèmes embarqués, applications à ressources limitées. La règle est de **calibrer l'intensité par zone** et de tester sur un échantillon avant de généraliser. Un scan qui provoque un incident coûte bien plus que sa valeur informative — et il produit surtout un refus durable des équipes, qui vous fermera l'accès pendant des années.

## 15.10 Interpréter un rapport : les sept réflexes

| # | Réflexe | Ce qu'il évite |
|---|---|---|
| 1 | Vérifier le périmètre et le taux d'authentification avant tout | Raisonner sur un échantillon inconnu |
| 2 | Contrôler la révision éditeur avant de conclure sur une version | Le faux positif de rétroportage (§2.2) |
| 3 | Vérifier si le composant est **activé** | Traiter des services installés mais désactivés |
| 4 | Distinguer sévérité **héritée** de la base et sévérité contextuelle | Prioriser sur un score sans exposition (§4.10) |
| 5 | Repérer les doublons : même constat, plusieurs entrées | Compter plusieurs fois le même travail |
| 6 | Identifier les constats **déjà corrigés par l'éditeur** mais non redétectés | Rouvrir un sujet clos |
| 7 | Chercher ce qui **manque** : machines absentes du rapport | La fausse assurance du §15.8 |

## 15.11 ⚠️ Les dix faux positifs les plus coûteux en temps

| # | Faux positif | Comment le lever |
|---|---|---|
| 1 | Rétroportage non pris en compte | Comparer la révision de l'éditeur, consulter l'avis de la distribution |
| 2 | Service installé mais désactivé | Vérifier l'état d'activation |
| 3 | Composant présent mais non chargé par l'application | Analyse d'atteignabilité (§11.6), déclaration du fournisseur |
| 4 | Bannière modifiée ou générique | Scan authentifié |
| 5 | Correspondance produit erronée | Vérifier le produit réel, corriger la table de correspondance |
| 6 | Vulnérabilité affectant une configuration non utilisée | Lire les conditions d'exploitation dans l'avis |
| 7 | Détection sur un appareil qui n'est pas le vôtre (adresse réattribuée) | Réconcilier avec l'inventaire |
| 8 | Constat sur une image de base, déjà corrigé dans l'image dérivée | Analyser l'image finale, pas seulement la base |
| 9 | Doublon entre agent et scan réseau | Règle de déduplication par identifiant pivot |
| 10 | Constat sur un actif décommissionné mais toujours présent dans l'outil | Nettoyage périodique, réconciliation d'inventaire |

📌 **La leçon transversale.** Ces dix causes n'ont presque rien à voir avec la qualité de l'outil. Elles viennent de l'écart entre ce qu'un outil peut observer et ce qu'est réellement votre système. Changer d'outil n'en supprime aucune ; améliorer l'inventaire et la vérification en supprime la majorité.

## 15.12 📌 Limites et coûts réels

| Dimension | Ce à quoi s'attendre |
|---|---|
| **Modèle de licence** | Le plus souvent par actif, ou par volume analysé. Le coût croît avec la découverte — inventorier mieux augmente la facture, ce qui crée une incitation perverse à ne pas chercher |
| **Charge d'exploitation** | L'outil demande du temps : maintien des comptes, des exclusions, des correspondances, traitement des échecs d'authentification |
| **Dépendance éditeur** | Les données historiques sont rarement portables. Un changement d'outil fait perdre l'antériorité, donc la démonstration de progrès |
| **Qualité du reporting** | Très inégale. Beaucoup d'outils rendent difficile le calcul honnête du §15.6, précisément parce qu'il n'est pas flatteur |
| **Périmètre non couvert** | Systèmes industriels, services en ligne, composants embarqués, produits — c'est-à-dire une part importante du périmètre réel |

✅ **BONNE PRATIQUE (P1)** — Exigez, dès l'évaluation d'un outil, la capacité d'**exporter les données brutes** et l'historique dans un format ouvert. C'est ce qui vous permettra de calculer vos propres indicateurs (chapitre 38), de constituer une preuve indépendante de l'outil (§5.6), et de changer de fournisseur sans repartir de zéro.

## 15.13 🔴 FIL ROUGE — janvier 2027 : trois semaines perdues

Le premier scan authentifié couvrant l'ensemble du périmètre élargi d'HELIOMED remonte, parmi 3 800 constats, une vulnérabilité critique sur une bibliothèque de chiffrement présente sur **42 serveurs** de classe C1 et C2.

Malik Ferhaoui lance la campagne de correction. Elle prend trois semaines : planification, fenêtres, tests, déploiement en anneaux, vérification. Le travail est bien fait.

**Le problème.** À la fin de la campagne, un contrôle de routine sur trois serveurs révèle que la version installée **avant** la campagne contenait déjà le correctif. La distribution avait rétroporté la correction six mois plus tôt ; le numéro de version amont, lui, n'avait pas bougé. Les 42 serveurs n'ont jamais été vulnérables.

**Ce que coûte l'erreur.** Trois semaines de deux personnes, six fenêtres de maintenance consommées, deux redémarrages de serveurs de production hors nécessité — et, plus grave, une régression mineure sur une application métier lors de la montée de version, qui a occupé l'équipe applicative pendant deux jours.

**La cause racine, et elle n'est pas technique.** Le réflexe n° 2 du §15.10 n'était écrit nulle part. Malik connaissait le mécanisme du rétroportage — il l'avait lu — mais rien dans le processus ne l'obligeait à vérifier avant de lancer une campagne de 42 serveurs.

**Les trois mesures prises.**

1. **Un point de contrôle obligatoire** dans le processus : toute campagne portant sur plus de dix actifs exige une vérification préalable sur **trois actifs représentatifs**, avec preuve jointe au dossier de campagne. Coût : trente minutes. Le pilote du chapitre 18 est né de cet incident.
2. **Une règle de qualification** : un constat issu d'un scan sur système à support long reste au statut *piste exploratoire* (§14.7) tant que la révision éditeur n'est pas vérifiée. Il ne peut pas déclencher de campagne à ce statut.
3. **Un signalement à l'éditeur de l'outil**, avec demande de prise en compte des révisions de distribution. Réponse reçue : la fonctionnalité existe et n'était pas activée sur leur instance. Elle l'est depuis.

**Ce que Claire Nadeau retient**, et qu'elle formule au comité en une phrase que l'équipe reprendra ensuite : *le coût d'un faux positif n'est pas le temps perdu à l'analyser, c'est le travail inutile qu'il déclenche quand personne ne l'analyse.*

**Livrable de l'épisode.** Le point de contrôle des trois actifs représentatifs, intégré au dossier de campagne standard — il figure en Annexe L.

→ La suite en 🔴 §16.11, quand il faudra prioriser les 3 800 constats restants.

→ **Chapitre 16 — Triage et priorisation défendables** : décider quoi traiter, et pourquoi un seuil de gravité ne suffit pas.

## Synthèse mentale du chapitre 15

Les familles d'outils ne se substituent pas : un agent ignore l'exposition réseau, un scan externe ignore l'état interne, une analyse de composition ignore ce que le système embarque — n'en utiliser qu'une crée un angle mort prévisible. Le scan non authentifié produit du faux positif structurel, mais il est le seul à établir ce qui est réellement joignable depuis un point donné. Le compte de scan et l'outil lui-même sont des actifs de niveau 0, et ils comptent régulièrement parmi les composants les plus en retard d'un parc. La fraîcheur de la base de détection est un objet qui se dégrade quotidiennement, et le délai que vous contrôlez est souvent le plus long. La couverture se calcule sur le périmètre de référence, en distinguant cinq populations, dont les exclusions — qui sont des dérogations déguisées si elles n'ont ni motif, ni propriétaire, ni date de revue. Enfin, « non vulnérable », « non détecté » et « non scanné » se présentent identiquement dans un rapport et signifient trois choses radicalement différentes : les confondre transforme une absence d'information en information rassurante.

**Trois questions de vérification**

1. Un rapport indique 0 vulnérabilité critique sur un ensemble de serveurs. Quelles trois questions posez-vous avant d'en tirer la moindre conclusion ?
2. Pourquoi le compte utilisé par votre scanner mérite-t-il un traitement de niveau 0, et quelles règles lui appliquez-vous ?
3. Une machine provoque un incident pendant un scan et vous l'excluez. Que devez-vous produire au même moment pour que cette exclusion ne devienne pas un angle mort permanent ?

---
