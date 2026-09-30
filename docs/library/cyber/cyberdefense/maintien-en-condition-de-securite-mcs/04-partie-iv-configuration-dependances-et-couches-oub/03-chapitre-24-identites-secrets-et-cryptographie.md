---
title: Chapitre 24 — Identités, secrets et cryptographie
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

## 24.1 La dette d'annuaire

Le §2.8 a posé le principe : un annuaire accumule, et aucune mise à jour ne réduit cette accumulation. Voici ce qu'elle contient.

| Objet accumulé | Origine | Risque |
|---|---|---|
| Comptes de personnes parties | Départs sans processus de sortie | Accès valides sans porteur |
| Comptes de service de projets abandonnés | Créations sans date de fin | Souvent surprivilégiés, mots de passe anciens |
| Délégations d'administration héritées | Migrations, réorganisations | Droits invisibles dans les vues standard |
| Appartenances à des groupes privilégiés | Ajouts temporaires jamais retirés | Élévation permanente |
| Protocoles d'authentification hérités | Compatibilité avec un logiciel disparu | Contournement des protections modernes |
| Relations d'approbation entre domaines | Fusions, acquisitions (§9.5) | Chemins d'attaque transverses |

**La méthode de réduction**, par ordre de rendement :

1. **Comptes inactifs** : identifier ceux sans authentification depuis 90 jours, désactiver avant de supprimer, observer 30 jours. Rendement immédiat, risque faible.
2. **Groupes privilégiés** : lister les membres, faire valider nominativement par un responsable, retirer les non confirmés.
3. **Délégations** : les extraire — elles n'apparaissent pas dans les vues courantes — et les faire valider.
4. **Protocoles hérités** : mesurer l'usage réel en mode observation, puis désactiver.

## 24.2 Comptes de service et comptes à privilèges

Les comptes de service sont le premier vecteur de propagation interne (§11.4).

| Problème | Pourquoi il persiste | Traitement |
|---|---|---|
| Mot de passe inchangé depuis des années | La rotation casse l'application qui l'utilise | Inventaire des consommateurs avant rotation (§24.10) |
| Droits d'administration sur de nombreux serveurs | Attribués « pour que ça marche » | Réduction progressive, mesurée en observation |
| Compte partagé entre plusieurs applications | Facilité de création | Un compte par usage |
| Aucun propriétaire | L'application a changé d'équipe | Rattachement obligatoire à un propriétaire (§10.4) |

**Les comptes de secours** — comptes d'urgence permettant d'accéder au système quand les mécanismes normaux échouent — méritent un traitement distinct : secret déposé de façon sécurisée, usage journalisé et alerté, test périodique de fonctionnement, et rotation après chaque usage. Un compte de secours non testé ne fonctionnera pas le jour où on en aura besoin ; un compte de secours non surveillé est une porte dérobée légitime.

## 24.3 Les secrets

**Le cycle de vie d'un secret** : création, distribution, stockage, usage, rotation, révocation. Chacune de ces étapes peut fuir.

| Localisation typique | Risque |
|---|---|
| Code source et dépôts | Persistance dans l'historique même après suppression |
| Fichiers de configuration | Lisibles par tout compte ayant accès au serveur |
| Code d'infrastructure et fichiers d'état | Souvent en clair, largement accessibles (§23.5) |
| Chaînes d'intégration | Accessibles aux agents d'exécution (ch. 28) |
| Documentation et messagerie | Copiés une fois, jamais retirés |
| Coffre-fort de secrets | Concentration : devient un actif de niveau 0 |

⚠️ **PIÈGE — la rotation non répercutée**
Le scénario le plus fréquent et le plus douloureux : le secret est modifié dans le coffre-fort, mais une application le lit depuis un fichier de configuration copié deux ans plus tôt. La rotation « réussit », l'ancien secret reste valide et utilisé. **Une rotation n'est effective que si l'ancien secret est révoqué** — et la révocation est ce qui casse les consommateurs oubliés. C'est douloureux, et c'est précisément l'intérêt : c'est ainsi qu'on les découvre.

## 24.4 Identités applicatives et autorisations déléguées

Dans les environnements en ligne, les identités non humaines sont devenues aussi nombreuses que les humaines, et bien moins surveillées.

| Objet | Risque spécifique |
|---|---|
| Identité d'application | Souvent créée avec des droits larges « en attendant », jamais réduits |
| Autorisation déléguée à une application tierce | Accorde un accès permanent aux données, sans mot de passe |
| Jeton de longue durée | Valable des mois, souvent stocké en clair |
| Identité de service managé | Pratique, mais l'attribution de droits est rarement revue |

✅ **BONNE PRATIQUE (P0)** — Faites l'inventaire des **autorisations déléguées** accordées à des applications tierces sur votre environnement de messagerie et de fichiers. C'est un exercice d'une demi-journée qui produit presque toujours des découvertes : connecteurs autorisés il y a plusieurs années, applications dont personne ne connaît l'usage, portées d'accès très supérieures au besoin. C'est le prolongement direct du §10.6 et du chapitre 31.

## 24.5 Les clés d'accès distant

Les clés d'authentification pour l'administration distante posent un problème particulier : elles sont **créées par les utilisateurs**, sans processus central, et ne périment pas.

Quatre questions à poser à votre parc : combien de clés autorisées existent sur vos serveurs ? à qui appartiennent-elles ? depuis quand ? combien appartiennent à des personnes ayant quitté l'organisation ? Dans une organisation qui n'a jamais fait cet inventaire, la quatrième réponse est rarement zéro.

**Le traitement** : centraliser la distribution, imposer une durée de validité, rattacher chaque clé à un propriétaire, et intégrer la révocation au processus de départ.

## 24.6 Certificats et infrastructure de confiance

**Le problème est double.** L'expiration provoque une interruption de service — c'est la seule échéance intrinsèque du §1.3. Et un certificat compromis ou mal émis permet l'usurpation.

| Objet | Ce qu'il faut savoir |
|---|---|
| Certificats de service | Inventaire, dates d'expiration, renouvellement automatisé |
| Certificats internes | Souvent oubliés, souvent de longue durée |
| Autorités de certification internes | **Actif de niveau 0** : leur compromission permet d'émettre n'importe quel certificat |
| Certificats de signature de code | Compromission = code malveillant signé par vous |
| Certificats de composants d'infrastructure | Expirations produisant des pannes difficiles à diagnostiquer |

✅ **BONNE PRATIQUE (P0)** — Constituez un inventaire des certificats avec leurs dates d'expiration et une alerte à 60, 30 et 7 jours. C'est l'une des mesures au meilleur rapport effort/incidents évités de tout le cours. Le renouvellement automatisé, là où il est possible, supprime le problème plutôt que de l'alerter.

## 24.7 Magasins de confiance

Chaque système, chaque application, chaque environnement d'exécution embarque sa propre liste d'autorités de confiance. Trois sujets de MCS en découlent :

- **Les mises à jour** de ces listes ne suivent pas le même canal que les correctifs, et sont souvent oubliées — le cas du §3.8 en est l'illustration ;
- **les ajouts internes** — autorité interne, certificat de test ajouté un jour et jamais retiré — élargissent la confiance sans que personne ne le sache ;
- **les révocations** ne se propagent pas toujours, notamment sur les systèmes isolés ou anciens.

## 24.8 Agilité cryptographique

**Le principe** : votre capacité à changer d'algorithme, de taille de clé ou de protocole **sans reconstruire vos applications**.

**Ce qui est actionnable aujourd'hui**, indépendamment de toute échéance future :

| Action | Effort | Bénéfice |
|---|---|---|
| Inventorier où la cryptographie est utilisée et laquelle | Moyen | Prérequis de tout le reste |
| Désactiver les suites et protocoles obsolètes | Faible | Immédiat |
| Réduire la durée de vie des certificats | Faible | Force l'automatisation du renouvellement |
| Éviter les algorithmes codés en dur dans les applications | Moyen | Rend le changement futur possible |
| Exiger l'agilité cryptographique dans les cahiers des charges | Nul | Structurant (§6.2) |

**Ce qui relève de la trajectoire** : la transition vers des algorithmes résistants aux futurs calculateurs quantiques est engagée au niveau des standards, avec des calendriers pluriannuels. Pour la quasi-totalité des organisations, l'action actionnable aujourd'hui n'est pas de migrer, c'est de **savoir où l'on utilise quoi** — c'est-à-dire la première ligne du tableau. Sans inventaire cryptographique, aucune migration future ne sera pilotable.

## 24.9 Accès distants et d'administration

Statistiquement le vecteur d'entrée dominant. Quatre exigences, sans lesquelles le reste importe peu :

1. **Authentification multifacteur** sur tous les accès distants et d'administration, sans exception tolérée.
2. **Postes d'administration dédiés**, sans messagerie ni navigation (§13.5, ch. 28).
3. **Accès bornés dans le temps** plutôt que permanents, pour les prestataires notamment.
4. **Journalisation** des actions d'administration, exportée hors de l'équipement administré.

## 24.10 Vérifier que les procédures fonctionnent

Un thème récurrent de ce chapitre : les procédures d'identité échouent silencieusement.

| Procédure | Test |
|---|---|
| Rotation de secret | Vérifier que l'ancien secret est **refusé** après rotation |
| Révocation de compte | Tenter une authentification après désactivation |
| Compte de secours | L'utiliser périodiquement, en conditions réelles |
| Renouvellement de certificat | Vérifier le certificat effectivement présenté par le service |
| Processus de départ | Auditer un échantillon de départs récents |

✅ **BONNE PRATIQUE (P1)** — Un test trimestriel sur un échantillon de chaque procédure. Trente minutes par procédure. C'est ce qui distingue une procédure qui existe d'une procédure qui fonctionne.

## 24.11 🔴 FIL ROUGE — septembre 2027 : la revue des comptes de service

L'incident du serveur d'impression (§23.7) déclenche une revue complète des comptes de service d'HELIOMED. Trois semaines de travail, conduites par Malik Ferhaoui avec l'appui de l'infogérant.

**L'état des lieux : 213 comptes de service.**

| Constat | Nombre |
|---|---|
| Sans propriétaire identifié | 94 |
| Mot de passe inchangé depuis plus de 5 ans | 61 |
| Membres d'un groupe d'administration du domaine | 17 |
| Aucune authentification depuis plus de 12 mois | 38 |
| Utilisés par plusieurs applications distinctes | 22 |

**Le traitement, en trois vagues.**

*Vague 1 — les 38 inactifs.* Désactivation, observation 30 jours. Trois réactivations : deux traitements annuels de clôture, et un connecteur d'échange avec un partenaire dont l'usage est trimestriel — la dépendance temporelle du §10.5. Les 35 autres sont supprimés.

*Vague 2 — les 17 comptes d'administration du domaine.* Chacun est instruit individuellement. Onze n'avaient aucun besoin réel de ce niveau de droits : les droits sont réduits, sans incident. Quatre nécessitent des droits élevés mais sur un périmètre restreint : délégation ciblée. Deux relèvent d'applications métier dont l'éditeur exige l'administration complète du domaine — exigence documentée, contestée par écrit auprès de l'éditeur (§13.8), et compensée par une restriction d'usage et une surveillance dédiée dans l'attente.

*Vague 3 — la rotation des secrets.* C'est la plus douloureuse. La rotation des 61 comptes anciens est menée par lots de dix, avec un inventaire préalable des consommateurs. **Neuf incidents applicatifs** malgré cet inventaire : autant de consommateurs non documentés, découverts exactement comme le prévoit le §24.3 — par la révocation.

**Ce que la revue révèle en passant.** Deux comptes de service portaient encore le nom d'un prestataire dont le contrat s'était achevé en 2021. Ils étaient actifs, disposaient de droits sur le serveur de fichiers, et leur mot de passe n'avait jamais changé.

**Les trois mesures pérennes.**

1. **Aucun compte de service sans propriétaire ni date de revue** — même règle que pour les actifs (§5.5). Contrôle automatisé mensuel.
2. **Rotation obligatoire** avec inventaire préalable des consommateurs, par lots, avec fenêtre déclarée.
3. **Intégration au processus de départ** : la fin d'un contrat de prestation déclenche une revue des comptes associés.

**Ce que Claire Nadeau écrit dans sa note de synthèse** : *nous avons passé dix-huit mois à corriger des vulnérabilités logicielles. La revue des comptes de service a réduit davantage notre exposition réelle que les six dernières campagnes de correctifs réunies.*

→ La suite en 🔴 §25.22, quand la R&D de Nantes découvrira ce que contient réellement son application.

→ **Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances** : le code applicatif et ses dépendances, y compris celui que vous avez écrit.

## Synthèse mentale du chapitre 24

Un annuaire accumule et aucune mise à jour ne réduit cette accumulation : comptes orphelins, délégations héritées, groupes privilégiés, protocoles anciens forment une dette que seule une revue explicite traite. Les comptes de service sont le premier vecteur de propagation interne, et une rotation n'est effective que si l'ancien secret est révoqué — ce qui casse les consommateurs oubliés, et c'est précisément ainsi qu'on les découvre. Les identités non humaines et les autorisations déléguées à des applications tierces sont désormais aussi nombreuses que les identités humaines et bien moins surveillées : leur inventaire est un exercice d'une demi-journée qui produit toujours des découvertes. Les certificats sont la seule dégradation à échéance intrinsèque, et leur inventaire avec alertes est l'une des mesures au meilleur rapport effort/incidents évités du cours. En cryptographie, l'action actionnable aujourd'hui n'est pas de migrer mais de savoir où l'on utilise quoi. Enfin, les procédures d'identité échouent silencieusement : seul un test périodique distingue une procédure qui existe d'une procédure qui fonctionne.

**Trois questions de vérification**

1. Vous effectuez la rotation d'un secret et l'opération est déclarée réussie. Qu'est-ce qui n'est pas encore prouvé, et quel test le prouve ?
2. Pourquoi les autorisations déléguées à des applications tierces constituent-elles un angle mort plus important qu'un compte utilisateur oublié ?
3. Votre direction vous demande de préparer la transition cryptographique post-quantique. Quelle est la seule action réellement utile à engager cette année, et pourquoi les autres en dépendent-elles ?

---
