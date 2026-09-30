---
title: PARTIE IV — Configuration, dépendances et couches oubliées
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 5
chapters: 10
---

La Partie III traitait la chaîne de correction des versions. Cette partie traite tout le reste de ce qui se dégrade : les configurations, les identités, les secrets, la cryptographie, le code applicatif et ses dépendances, les couches intermédiaires, les couches basses, et les environnements que personne ne regarde.

C'est ici que se joue la différence entre un programme de gestion des correctifs et un véritable maintien en condition de sécurité.

---

## Chapitre 22 — Durcissement et référentiels de configuration

### 22.1 Pourquoi une version à jour mal configurée reste vulnérable

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

### 22.2 Choisir et adapter un référentiel

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

### 22.3 Construire et maintenir une *baseline*

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

### 22.4 Automatiser le contrôle

Trois familles de mécanismes, complémentaires :

| Mécanisme | Principe | Fréquence réaliste |
|---|---|---|
| **Contrôle par script ou format standardisé** | Vérification périodique de chaque point de la *baseline* | Hebdomadaire à mensuelle |
| **Politiques centralisées natives** | La plateforme applique et vérifie en continu | Continu |
| **Contrôle dans la chaîne de construction** | L'image est vérifiée avant d'être publiée | À chaque construction |

**Le troisième est le plus efficace** : contrôler à la construction empêche la non-conformité d'exister, plutôt que de la constater après coup. C'est la traduction du principe du §10.7 — traiter à la source plutôt que rattraper.

### 22.5 Mesurer la conformité de configuration

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

### 22.6 ⚠️ Le durcissement qui casse la production

C'est le principal frein à l'adoption, et il est légitime : contrairement à un correctif, un durcissement modifie **intentionnellement** le comportement du système.

**La méthode qui fonctionne**, en cinq étapes :

1. **Mesurer avant d'appliquer.** Beaucoup de contrôles peuvent être évalués en mode observation : on journalise ce qui serait bloqué, sans bloquer.
2. **Appliquer par lots** de points, pas la *baseline* entière d'un coup — sinon un incident ne peut être imputé à aucun point précis.
3. **Utiliser les anneaux** du §18.4 : le durcissement est un changement comme un autre.
4. **Prévoir le retour arrière** point par point.
5. **Documenter les écarts découverts** : un point qui casse une application métier devient un écart motivé, pas un contrôle silencieusement désactivé.

### 22.7 📌 Limites

- **Les référentiels génériques ne couvrent pas les applications métier**, qui portent souvent les configurations les plus risquées. Pour elles, il faut construire ses propres points de contrôle.
- **Le coût de maintenance d'une baseline** est réel : chaque version majeure du système la rend partiellement obsolète.
- **La conformité de configuration ne dit rien de l'exposition.** Un serveur parfaitement durci mais publié inutilement reste un problème (ch. 11).
- **Le durcissement ne remplace pas les correctifs**, et l'inverse est également vrai. Ce sont deux couches distinctes.

### 22.8 ✅ Recommandations priorisées

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

### Synthèse mentale du chapitre 22

Un correctif supprime un défaut de code, il ne touche pas à votre configuration — et l'essentiel des compromissions réelles emprunte des chemins de configuration. Cinq réglages annulent à eux seuls l'effet de tous vos correctifs, et ils se traitent sans fenêtre ni risque majeur. N'adoptez qu'un seul référentiel de base, et dérivez-le en motivant chaque écart : la dérivation n'affaiblit pas la baseline, c'est ce qui la rend applicable donc réellement appliquée. Contrôler à la construction empêche la non-conformité d'exister plutôt que de la constater. Mesurez séparément les points critiques non conformes, car dix écarts mineurs ne compensent pas un compte administrateur par défaut. Enfin, un durcissement modifie intentionnellement le comportement du système : il s'applique par lots, en anneaux, après mesure en mode observation.

**Trois questions de vérification**

1. Votre parc est parfaitement à jour et un attaquant progresse quand même du poste bureautique jusqu'à la console de sauvegarde. Quelles configurations examinez-vous en premier ?
2. Pourquoi appliquer un référentiel de durcissement sans dérivation produit-il presque toujours une baseline fictive ?
3. Vous affichez 94 % de conformité de configuration. Quelles trois précautions de calcul devez-vous avoir prises pour que ce chiffre signifie quelque chose ?

---

## Chapitre 23 — Dérive de configuration, IaC et immutabilité

### 23.1 Les mécanismes de la dérive

Une configuration conforme le jour J ne le reste pas. Six mécanismes la dégradent, tous parfaitement légitimes pris isolément :

| Mécanisme | Illustration |
|---|---|
| **Intervention manuelle** | Un paramètre modifié pour résoudre un problème, jamais reversé |
| **Résolution d'urgence** | Un contrôle désactivé pendant un incident, jamais réactivé |
| **Intervention d'un prestataire** | Un tiers applique sa propre configuration de référence |
| **Mise à jour applicative** | L'installeur remet des valeurs par défaut |
| **Restauration** | Retour à un état antérieur à un durcissement |
| **Nouveau projet** | Une exigence projet contredit la *baseline*, sans arbitrage |

**Le point commun** : aucun de ces mécanismes n'est malveillant ni négligent. La dérive n'est pas un problème de discipline, c'est une propriété des systèmes vivants. Elle se traite par la détection et la convergence, pas par la réprimande.

### 23.2 Détecter la dérive

| Méthode | Principe | Signal / bruit |
|---|---|---|
| **Contrôle de conformité périodique** | Rejouer les points de la *baseline* (§22.4) | Bon, si la *baseline* est bien dérivée |
| **Empreinte de configuration** | Comparer un état complet à une référence | Bruit élevé : tout change tout le temps |
| **Détection de changement en temps réel** | Alerter sur modification de fichiers ou de paramètres sensibles | Excellent si le périmètre est **étroit** |
| **Comparaison code / réalité** | Écart entre la description et l'existant | Bon, limité au périmètre décrit |

⚠️ **PIÈGE — la détection de changement à périmètre trop large**
Surveiller « toutes les modifications de configuration » produit des milliers d'alertes quotidiennes légitimes, que personne ne traite. Ciblez : comptes à privilèges, règles de filtrage, paramètres d'authentification, tâches planifiées, points de démarrage. Vingt éléments bien choisis valent mieux que la surveillance exhaustive.

### 23.3 Corriger par convergence

Un outil de gestion de configuration applique un état désiré et le **réapplique périodiquement**. La dérive est corrigée automatiquement, sans intervention.

| Bénéfice | Effet pervers correspondant |
|---|---|
| La configuration revient toujours à la référence | Une correction manuelle légitime est écrasée sans prévenir |
| L'état désiré est documenté dans le code | Le code devient un actif critique à maintenir (§3.5) |
| Le déploiement est reproductible | Une erreur dans le code se propage à tout le parc en quelques minutes |
| L'écart est mesurable | Ce qui n'est pas décrit n'est pas surveillé — et donne une fausse assurance |

**Les deux règles qui évitent les effets pervers** : appliquer le code de configuration **par anneaux**, comme tout déploiement (§18.4) ; et prévoir un mécanisme d'exclusion explicite et tracé pour les actifs devant diverger temporairement.

### 23.4 L'approche immuable

Ne jamais modifier un système en fonctionnement : reconstruire et remplacer (§3.5, §6.10).

**Ce que cela change pour la dérive** : elle devient **impossible par construction** sur la durée de vie de l'instance, qui est courte. Une instance vit quelques jours ou semaines, puis est remplacée par une instance neuve issue d'une image à jour et conforme.

**Les trois conditions de faisabilité**, souvent sous-estimées : les données doivent être externalisées de l'instance ; la reconstruction doit être automatisée et rapide ; et l'application doit tolérer le remplacement de ses instances.

**Le déplacement du problème** : la conformité se joue entièrement dans la **construction de l'image**. C'est là que doivent porter les contrôles (§22.4), et c'est là qu'un défaut se propage à l'ensemble du parc.

### 23.5 Le MCS du code d'infrastructure

Le code qui décrit votre infrastructure est lui-même un actif :

| Objet | Ce qui se dégrade | Traitement |
|---|---|---|
| Modules réutilisés | Vulnérabilités, abandon du mainteneur | Versionnement, revue, mise à jour périodique (ch. 25) |
| Connecteurs vers les fournisseurs | Fins de support, changements d'interface | Suivi des versions supportées |
| Fichier d'état | Contient des secrets, décrit toute l'infrastructure | **Actif de niveau 0** : chiffrement, accès restreint, journalisation |
| Écart code / réalité | Ressources créées à la main | Détection périodique et réconciliation |

⚠️ **PIÈGE — l'illusion de maîtrise**
Un environnement décrit par du code **donne le sentiment** d'être maîtrisé. Mais si 30 % des ressources ont été créées manuellement en dehors du code, la description est fausse — et plus dangereusement fausse qu'une absence de description, parce qu'on lui fait confiance.

### 23.6 Gérer les exceptions et les actifs non convergeables

Certains actifs ne peuvent pas converger : systèmes industriels, appliances fermées, applications imposant une configuration propre, matériel spécialisé.

**Le traitement** : les identifier explicitement, les rattacher à la classe C4 (§7.2), leur appliquer un contrôle manuel périodique documenté, et **les compter séparément** dans les indicateurs. Ce qui n'est pas acceptable, c'est qu'ils disparaissent silencieusement du périmètre contrôlé — c'est le mécanisme de l'exclusion silencieuse du §15.6.

### 23.7 🔴 FIL ROUGE — août 2027 : le serveur d'impression de 2019

Le premier contrôle de conformité automatisé d'HELIOMED, déployé sur les 176 serveurs internes, remonte un résultat global de 87 % — et sept serveurs sous 40 %.

**Le cas le plus instructif** : SRV-PRINT-01, serveur d'impression, 31 % de conformité. L'analyse retrace son histoire.

En novembre 2019, un incident bloque les impressions du siège pendant une demi-journée. Pour rétablir le service, l'administrateur de l'époque — parti depuis — élargit les droits d'un compte de service, désactive deux contrôles d'authentification, et ouvre l'accès depuis l'ensemble du réseau. Le service repart. L'incident est clos.

Rien n'a été reversé. Huit ans plus tard, le compte de service dispose de droits d'administration sur 34 serveurs, l'authentification héritée est toujours active, et le serveur est joignable depuis n'importe quel poste du groupe.

**Ce que révèle le croisement avec le chapitre 11.** SRV-PRINT-01 apparaît dans la matrice des chemins d'attaque comme **étape intermédiaire de trois chemins distincts** menant à des actifs de niveau 0. Il n'avait jamais été identifié comme critique : c'est un serveur d'impression.

**Les décisions.**

1. **Traitement immédiat** des trois points critiques : réduction des droits du compte de service, désactivation de l'authentification héritée après mesure en mode observation (§22.6), restriction de l'accès réseau.
2. **Règle de processus** : toute modification de configuration réalisée pendant un incident est enregistrée dans le journal de l'incident et **fait l'objet d'un ticket de reversion** à la clôture. Sans reversion possible, elle devient un écart motivé et documenté.
3. **Convergence** : le serveur d'impression entre dans le périmètre de l'outil de gestion de configuration, qui n'y avait jamais été déployé.

**Ce que Claire Nadeau retient**, et qu'elle formule au comité : *nous cherchions les serveurs critiques dans la liste des applications métier. Le chemin le plus court vers nos données passait par l'imprimante.*

**Livrable de l'épisode.** La règle de reversion post-incident, intégrée à la procédure de gestion des incidents, et l'extension du périmètre de convergence.

→ La suite en 🔴 §24.11, quand la revue des comptes de service révélera l'ampleur du sujet.

→ **Chapitre 24 — Identités, secrets et cryptographie** : les identités, les secrets et la cryptographie — ce qu'aucun correctif ne réduit.

### Synthèse mentale du chapitre 23

La dérive n'est pas un problème de discipline mais une propriété des systèmes vivants : six mécanismes la produisent, tous légitimes pris isolément, et elle se traite par la détection et la convergence plutôt que par la réprimande. Surveiller toutes les modifications produit un bruit ingérable ; vingt éléments bien choisis — comptes à privilèges, règles de filtrage, authentification, tâches planifiées, points de démarrage — valent mieux que l'exhaustivité. La convergence automatique corrige la dérive mais écrase les corrections légitimes et propage les erreurs en quelques minutes : elle s'applique par anneaux. L'approche immuable rend la dérive impossible par construction, et déplace toute la conformité vers la construction de l'image. Enfin, une infrastructure décrite par du code donne un sentiment de maîtrise qui devient dangereux dès qu'une part significative des ressources a été créée manuellement — une description fausse à laquelle on fait confiance est pire qu'une absence de description.

**Trois questions de vérification**

1. Un contrôle a été désactivé pendant un incident il y a trois ans. Quel mécanisme de processus aurait empêché qu'il le reste, et à quel moment précis s'applique-t-il ?
2. Pourquoi la surveillance exhaustive des changements de configuration produit-elle moins de sécurité qu'une surveillance de vingt éléments ?
3. Votre infrastructure est décrite par du code à 70 %. En quoi cette situation est-elle plus risquée qu'une absence totale de description ?

---

## Chapitre 24 — Identités, secrets et cryptographie

### 24.1 La dette d'annuaire

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

### 24.2 Comptes de service et comptes à privilèges

Les comptes de service sont le premier vecteur de propagation interne (§11.4).

| Problème | Pourquoi il persiste | Traitement |
|---|---|---|
| Mot de passe inchangé depuis des années | La rotation casse l'application qui l'utilise | Inventaire des consommateurs avant rotation (§24.10) |
| Droits d'administration sur de nombreux serveurs | Attribués « pour que ça marche » | Réduction progressive, mesurée en observation |
| Compte partagé entre plusieurs applications | Facilité de création | Un compte par usage |
| Aucun propriétaire | L'application a changé d'équipe | Rattachement obligatoire à un propriétaire (§10.4) |

**Les comptes de secours** — comptes d'urgence permettant d'accéder au système quand les mécanismes normaux échouent — méritent un traitement distinct : secret déposé de façon sécurisée, usage journalisé et alerté, test périodique de fonctionnement, et rotation après chaque usage. Un compte de secours non testé ne fonctionnera pas le jour où on en aura besoin ; un compte de secours non surveillé est une porte dérobée légitime.

### 24.3 Les secrets

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

### 24.4 Identités applicatives et autorisations déléguées

Dans les environnements en ligne, les identités non humaines sont devenues aussi nombreuses que les humaines, et bien moins surveillées.

| Objet | Risque spécifique |
|---|---|
| Identité d'application | Souvent créée avec des droits larges « en attendant », jamais réduits |
| Autorisation déléguée à une application tierce | Accorde un accès permanent aux données, sans mot de passe |
| Jeton de longue durée | Valable des mois, souvent stocké en clair |
| Identité de service managé | Pratique, mais l'attribution de droits est rarement revue |

✅ **BONNE PRATIQUE (P0)** — Faites l'inventaire des **autorisations déléguées** accordées à des applications tierces sur votre environnement de messagerie et de fichiers. C'est un exercice d'une demi-journée qui produit presque toujours des découvertes : connecteurs autorisés il y a plusieurs années, applications dont personne ne connaît l'usage, portées d'accès très supérieures au besoin. C'est le prolongement direct du §10.6 et du chapitre 31.

### 24.5 Les clés d'accès distant

Les clés d'authentification pour l'administration distante posent un problème particulier : elles sont **créées par les utilisateurs**, sans processus central, et ne périment pas.

Quatre questions à poser à votre parc : combien de clés autorisées existent sur vos serveurs ? à qui appartiennent-elles ? depuis quand ? combien appartiennent à des personnes ayant quitté l'organisation ? Dans une organisation qui n'a jamais fait cet inventaire, la quatrième réponse est rarement zéro.

**Le traitement** : centraliser la distribution, imposer une durée de validité, rattacher chaque clé à un propriétaire, et intégrer la révocation au processus de départ.

### 24.6 Certificats et infrastructure de confiance

**Le problème est double.** L'expiration provoque une interruption de service — c'est la seule échéance intrinsèque du §1.3. Et un certificat compromis ou mal émis permet l'usurpation.

| Objet | Ce qu'il faut savoir |
|---|---|
| Certificats de service | Inventaire, dates d'expiration, renouvellement automatisé |
| Certificats internes | Souvent oubliés, souvent de longue durée |
| Autorités de certification internes | **Actif de niveau 0** : leur compromission permet d'émettre n'importe quel certificat |
| Certificats de signature de code | Compromission = code malveillant signé par vous |
| Certificats de composants d'infrastructure | Expirations produisant des pannes difficiles à diagnostiquer |

✅ **BONNE PRATIQUE (P0)** — Constituez un inventaire des certificats avec leurs dates d'expiration et une alerte à 60, 30 et 7 jours. C'est l'une des mesures au meilleur rapport effort/incidents évités de tout le cours. Le renouvellement automatisé, là où il est possible, supprime le problème plutôt que de l'alerter.

### 24.7 Magasins de confiance

Chaque système, chaque application, chaque environnement d'exécution embarque sa propre liste d'autorités de confiance. Trois sujets de MCS en découlent :

- **Les mises à jour** de ces listes ne suivent pas le même canal que les correctifs, et sont souvent oubliées — le cas du §3.8 en est l'illustration ;
- **les ajouts internes** — autorité interne, certificat de test ajouté un jour et jamais retiré — élargissent la confiance sans que personne ne le sache ;
- **les révocations** ne se propagent pas toujours, notamment sur les systèmes isolés ou anciens.

### 24.8 Agilité cryptographique

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

### 24.9 Accès distants et d'administration

Statistiquement le vecteur d'entrée dominant. Quatre exigences, sans lesquelles le reste importe peu :

1. **Authentification multifacteur** sur tous les accès distants et d'administration, sans exception tolérée.
2. **Postes d'administration dédiés**, sans messagerie ni navigation (§13.5, ch. 28).
3. **Accès bornés dans le temps** plutôt que permanents, pour les prestataires notamment.
4. **Journalisation** des actions d'administration, exportée hors de l'équipement administré.

### 24.10 Vérifier que les procédures fonctionnent

Un thème récurrent de ce chapitre : les procédures d'identité échouent silencieusement.

| Procédure | Test |
|---|---|
| Rotation de secret | Vérifier que l'ancien secret est **refusé** après rotation |
| Révocation de compte | Tenter une authentification après désactivation |
| Compte de secours | L'utiliser périodiquement, en conditions réelles |
| Renouvellement de certificat | Vérifier le certificat effectivement présenté par le service |
| Processus de départ | Auditer un échantillon de départs récents |

✅ **BONNE PRATIQUE (P1)** — Un test trimestriel sur un échantillon de chaque procédure. Trente minutes par procédure. C'est ce qui distingue une procédure qui existe d'une procédure qui fonctionne.

### 24.11 🔴 FIL ROUGE — septembre 2027 : la revue des comptes de service

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

### Synthèse mentale du chapitre 24

Un annuaire accumule et aucune mise à jour ne réduit cette accumulation : comptes orphelins, délégations héritées, groupes privilégiés, protocoles anciens forment une dette que seule une revue explicite traite. Les comptes de service sont le premier vecteur de propagation interne, et une rotation n'est effective que si l'ancien secret est révoqué — ce qui casse les consommateurs oubliés, et c'est précisément ainsi qu'on les découvre. Les identités non humaines et les autorisations déléguées à des applications tierces sont désormais aussi nombreuses que les identités humaines et bien moins surveillées : leur inventaire est un exercice d'une demi-journée qui produit toujours des découvertes. Les certificats sont la seule dégradation à échéance intrinsèque, et leur inventaire avec alertes est l'une des mesures au meilleur rapport effort/incidents évités du cours. En cryptographie, l'action actionnable aujourd'hui n'est pas de migrer mais de savoir où l'on utilise quoi. Enfin, les procédures d'identité échouent silencieusement : seul un test périodique distingue une procédure qui existe d'une procédure qui fonctionne.

**Trois questions de vérification**

1. Vous effectuez la rotation d'un secret et l'opération est déclarée réussie. Qu'est-ce qui n'est pas encore prouvé, et quel test le prouve ?
2. Pourquoi les autorisations déléguées à des applications tierces constituent-elles un angle mort plus important qu'un compte utilisateur oublié ?
3. Votre direction vous demande de préparer la transition cryptographique post-quantique. Quelle est la seule action réellement utile à engager cette année, et pourquoi les autres en dépendent-elles ?

---

## Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances

> **Angle mort corrigé dans ce chapitre.** Une application peut être vulnérable **sans qu'aucune de ses dépendances ne le soit**. Le MCS applicatif ne se réduit pas à mettre à jour des bibliothèques : il commence par le code que vous avez écrit vous-même.

---

### A — Le code détenu par l'organisation

### 25.1 Les vulnérabilités du code propriétaire

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

### 25.2 Les sources de constats applicatifs

| Source | Ce qu'elle trouve bien | Ce qu'elle manque |
|---|---|---|
| **Analyse statique du code** | Injections, secrets codés en dur, motifs dangereux | Logique métier, autorisation |
| **Analyse dynamique** | Comportements observables sur l'application en fonctionnement | Ce qui n'est pas atteint par les tests |
| **Test d'intrusion applicatif** | **Autorisation, logique métier, enchaînements** | Ce qui est hors périmètre ou hors budget |
| **Programme de récompense** | Ce qu'un attaquant réel trouverait | Nécessite maturité et budget |
| **Revue de code** | Faiblesses de conception | Coûteuse, non exhaustive |
| **Retours clients et incidents** | Le réel | Trop tard |

**La règle du §14.2 s'applique intégralement** : tous ces constats entrent dans **la même file** que les vulnérabilités de composants, avec la même priorisation. C'est ce qui évite qu'un défaut d'autorisation découvert en test d'intrusion progresse moins vite qu'une bibliothèque à mettre à jour.

### 25.3 Affecter un constat applicatif

La difficulté est différente de celle du chapitre 17 : le correcteur n'est pas un exploitant mais une **équipe de développement**, dont la charge est planifiée par sprints et arbitrée par un responsable produit.

**Les trois frictions caractéristiques :**

| Friction | Manifestation | Traitement |
|---|---|---|
| Concurrence avec le fonctionnel | Le correctif de sécurité concurrence des fonctionnalités attendues | Réserver une capacité fixe par cycle (10 à 20 %), négociée une fois |
| Absence de propriétaire de composant | Le code appartient à « l'équipe » | Propriété nominative par composant, comme pour les actifs (§5.5) |
| Constat mal formulé | « Vulnérabilité XSS » sans contexte | Fournir : chemin de reproduction, impact métier, correction attendue |

✅ **BONNE PRATIQUE (P0)** — Négociez une **capacité de sécurité récurrente** dans la planification des équipes de développement, plutôt que de négocier chaque correctif. C'est exactement le pré-arbitrage du §9.4 transposé au développement, et cela supprime la discussion à chaque constat.

### 25.4 Le cycle de remédiation applicative

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

### 25.5 Branches de maintenance et rétroportage

Si votre produit est déployé chez des clients en plusieurs versions, corriger la version courante ne suffit pas.

| Question | Décision à formaliser |
|---|---|
| Combien de versions maintenez-vous en sécurité ? | Deux ou trois au maximum — au-delà, la charge devient ingérable |
| Rétroportez-vous les correctifs de sécurité ? | Oui pour les versions maintenues, avec le mécanisme du §2.2 |
| Publiez-vous un correctif ponctuel ou une version complète ? | Le correctif ponctuel accélère l'adoption ; la version complète simplifie la maintenance |
| Comment les clients apprennent-ils qu'ils doivent mettre à jour ? | C'est le chapitre 33 |

### 25.6 Mesures temporaires côté applicatif

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

### B — Politique de versions applicatives

### 25.7 Définir la politique

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

### 25.8 Interfaces anciennes et compatibilité

Les points d'accès dépréciés sont des actifs à part entière : ils portent du code, souvent ancien, souvent moins protégé que les nouveaux, et souvent maintenus « parce qu'un client les utilise encore ».

**Le traitement** : les inventorier, mesurer leur usage réel, publier une date de retrait, et les traiter comme un décommissionnement (chapitre 35) — avec préavis, communication et vérification qu'ils ne sont plus appelés.

### 25.9 La dette de version applicative

Elle se mesure, comme la dette d'obsolescence du §12.6 : nombre de clients sur une version non supportée, ancienneté moyenne des versions déployées, nombre de branches maintenues, charge consommée par le rétroportage.

**L'argument à porter en interne** : chaque branche supplémentaire maintenue multiplie le coût de chaque correctif de sécurité. Réduire le nombre de branches n'est pas un confort d'équipe de développement, c'est une mesure de MCS.

---

### C — Chaîne logicielle et dépendances

### 25.10 Le code que vous n'avez pas écrit

Dans une application moderne, une part souvent importante — parfois majoritaire — du code exécuté provient de bibliothèques externes, elles-mêmes dépendantes d'autres bibliothèques (§3.6). Cette part est rarement inventoriée, et c'est le problème.

**Trois conséquences directes pour le MCS :**

1. Votre surface d'attaque comprend le code de dizaines d'organisations que vous ne connaissez pas.
2. Vous ne contrôlez ni le rythme de correction, ni la qualité, ni la pérennité de ces composants.
3. Une vulnérabilité dans une bibliothèque très répandue vous concerne **en même temps que des dizaines de milliers d'autres organisations** — donc dans un contexte où l'exploitation automatisée démarre en quelques heures.

### 25.11 L'inventaire des composants logiciels en pratique

| Question | Réponse opérationnelle |
|---|---|
| **Quand le générer ?** | À la construction, automatiquement. Un inventaire produit manuellement est périmé le jour de sa production |
| **Quelle granularité ?** | Composants directs **et** transitifs, avec versions exactes |
| **Où le stocker ?** | Associé à l'artefact produit, versionné, conservé aussi longtemps que la version est déployée |
| **Comment l'exploiter ?** | Rapproché en continu des sources de vulnérabilités, **rejoué à chaque nouvelle publication** |

⚠️ **PIÈGE — l'inventaire produit et jamais consommé**
C'est la situation la plus fréquente : l'organisation génère des inventaires de composants parce qu'un client ou un texte l'exige, les archive, et ne les rapproche jamais d'une base de vulnérabilités. Le document existe, la capacité n'existe pas. **La question qui tranche** : quand une vulnérabilité majeure est publiée dans une bibliothèque très répandue, combien de temps vous faut-il pour répondre « suis-je concerné, sur quels produits, dans quelles versions ? » Si la réponse dépasse quelques heures, votre inventaire ne sert à rien.

### 25.12 Analyse de composition et atteignabilité

L'analyse de composition rapproche vos dépendances déclarées des vulnérabilités connues. Elle produit beaucoup de bruit, pour des raisons structurelles :

| Cause de bruit | Mécanisme |
|---|---|
| Dépendances transitives | La vulnérabilité est à trois niveaux de profondeur, vous ne l'avez pas choisie |
| Composant non chargé | Présent dans les dépendances, jamais utilisé à l'exécution |
| Fonction non atteignable | Le composant est utilisé, mais pas la fonction vulnérable (§11.6) |
| Version corrigée par l'écosystème | Résolution de version différente de la déclaration |

**Le traitement** : appliquer l'arbre du §16.3, en utilisant l'atteignabilité comme critère de dépriorisation documentée — jamais de clôture (§16.6).

### 25.13 Politique de mise à jour des dépendances

| Approche | Principe | Risque |
|---|---|---|
| **Automatisée avec tests** | Un mécanisme propose les montées de version, les tests décident | Le meilleur rapport effort/résultat, si les tests existent |
| **Périodique groupée** | Une campagne mensuelle de mise à jour des dépendances | Simple, mais le retard s'accumule entre deux campagnes |
| **À la demande** | On met à jour quand une vulnérabilité l'impose | Chaque mise à jour devient une montée de plusieurs versions, donc risquée |

**Le cercle vicieux à connaître** : moins on met à jour, plus l'écart grandit, plus chaque mise à jour devient risquée, donc moins on met à jour. La mise à jour fréquente et automatisée est **moins risquée** que la mise à jour rare, contrairement à l'intuition — chaque saut est petit.

### 25.14 La santé d'une dépendance

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

### 25.15 Les attaques sur la chaîne d'approvisionnement

| Technique | Principe | Défense principale |
|---|---|---|
| **Typosquattage** | Un paquet au nom proche d'un paquet légitime | Verrouillage des versions, registre interne, revue des ajouts |
| **Confusion de dépendances** | Un paquet public prend la place d'un paquet interne homonyme | Espaces de noms réservés, priorité explicite du registre interne |
| **Compromission de mainteneur** | Le compte légitime publie une version malveillante | Verrouillage, délai avant adoption d'une version, vérification de provenance |
| **Compromission de la chaîne de construction** | L'attaquant modifie l'artefact produit | Protection des agents (ch. 28), attestations de provenance |
| **Dépendance abandonnée reprise** | Un tiers reprend un paquet inactif | Surveillance des changements de mainteneur (§25.14) |

**La défense la plus efficace et la moins coûteuse** : un **délai avant adoption** des nouvelles versions de dépendances — quelques jours suffisent à ce que la communauté détecte la majorité des paquets malveillants. C'est le délai d'observation du §18.3, transposé aux dépendances.

### 25.16 Provenance et intégrité

| Mécanisme | Ce qu'il garantit |
|---|---|
| Verrouillage des versions | Vous obtenez exactement ce que vous avez validé |
| Registre interne avec approbation | Vous contrôlez ce qui entre |
| Vérification d'empreinte ou de signature | L'artefact n'a pas été modifié |
| Attestation de provenance | L'artefact vient bien de la chaîne de construction attendue |
| Construction reproductible | La même source produit le même artefact — permet la vérification indépendante |

**L'ordre d'adoption réaliste** : verrouillage d'abord (immédiat, gratuit), registre interne ensuite (structurant), vérification et attestations après. Les constructions reproductibles sont un objectif exigeant, à ne pas placer en tête d'un programme.

### 25.17 Images de base et registres

Une image de conteneur hérite de tout ce que contient son image de base. Trois règles suffisent :

1. **Choisir des images de base minimales** — moins de composants, moins de vulnérabilités, moins de reconstruction.
2. **Fixer une cadence de reconstruction** (§3.2) : c'est l'indicateur qui remplace des centaines de constats individuels.
3. **Contrôler à la publication** dans le registre, pas à l'exécution : une image non conforme ne doit pas pouvoir être publiée (§22.4).

### 25.18 Protéger la chaîne de construction

Traité en profondeur au chapitre 28. Trois points à retenir ici : les agents d'exécution disposent d'accès étendus et échappent souvent à l'inventaire ; les secrets de la chaîne sont un objectif de premier ordre ; et une compromission de la chaîne contamine **tous** les artefacts produits, y compris ceux livrés à vos clients.

### 25.19 Déclarations d'exploitabilité et avis lisibles par machine

Le §4.8 a présenté les formats. Voici l'usage réel, dans les deux sens :

**En consommation.** Un fournisseur vous déclare qu'un composant vulnérable présent dans son produit n'est pas exploitable. Cela vous permet de dépriorer sans analyser — à condition de conserver la déclaration comme justification, et de la réexaminer si le contexte change.

**En production.** Si vous éditez un produit, ces déclarations vous évitent de recevoir cent fois la même question de vos clients à chaque vulnérabilité majeure d'une bibliothèque répandue. C'est un gain considérable pour le PSIRT (chapitre 33).

📌 **LIMITES** — La maturité de l'outillage reste inégale, et l'adoption est très variable selon les éditeurs. Ne construisez pas un processus qui **dépend** de la réception de ces déclarations : traitez-les comme un enrichissement quand elles arrivent.

### 25.20 ⚖️ Ce que la réglementation produit impose sur les composants

Pour les fabricants de produits numériques, les obligations émergentes portent notamment sur : la fourniture d'un inventaire des composants, la gestion des vulnérabilités affectant les composants tiers, la mise à disposition de correctifs pendant une durée déterminée, et la notification des vulnérabilités activement exploitées. Le détail et le calendrier figurent au chapitre 33.

**La conséquence pratique**, même sans être fabricant : ces exigences se propagent le long de la chaîne (§13.7). Vos fournisseurs devront vous fournir ces éléments, et vos clients vous les demanderont.

### 25.21 📌 Limites

- **Le code sans propriétaire** : une application dont l'équipe a été dissoute ne sera pas corrigée, quelle que soit la qualité du constat.
- **L'éditeur métier non coopératif** : vous détectez, il ne corrige pas. C'est un sujet contractuel (ch. 13), pas technique.
- **L'application sans jeu de tests** : corriger devient un pari, et le pari est souvent perdu — d'où le report systématique.
- **Le coût d'un correctif dans du code non testé** peut dépasser celui d'une réécriture partielle. Cela doit être dit, chiffré, et arbitré.

### 25.22 🔴 FIL ROUGE — octobre 2027 : ce que contenait HelioLink

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

### Synthèse mentale du chapitre 25

Une application peut être vulnérable sans qu'aucune de ses dépendances ne le soit : le défaut d'autorisation, le plus fréquemment exploité en conditions réelles, est invisible à l'analyse automatique et ne produit aucune anomalie technique. Les constats applicatifs entrent dans la même file que les vulnérabilités de composants, et la friction propre au développement se traite par une capacité de sécurité réservée dans chaque cycle plutôt que par une négociation à chaque constat. Le cycle de remédiation applicative se termine par l'ajout d'un test permanent — sans lui, la même vulnérabilité réapparaîtra lors d'une refactorisation dans six mois. L'analyse de cause racine doit s'étendre à la classe entière : corriger un cas et ignorer les quatre autres points d'accès identiques est le gaspillage le plus courant. Côté dépendances, la mise à jour fréquente et automatisée est moins risquée que la mise à jour rare, contrairement à l'intuition, et un délai de quelques jours avant adoption d'une nouvelle version est la défense la plus rentable contre les paquets malveillants. Enfin, un inventaire de composants qui ne permet pas de répondre en quelques heures à « suis-je concerné » n'a aucune utilité.

**Trois questions de vérification**

1. Votre analyse de composition est parfaite et votre parc de dépendances est à jour. Quelle catégorie de vulnérabilité reste entièrement invisible, et comment la découvre-t-on ?
2. Pourquoi mettre à jour ses dépendances rarement est-il plus risqué que les mettre à jour souvent ?
3. Un défaut d'autorisation est corrigé sur un point d'accès. Quelles deux actions restent indispensables avant de clore le constat ?

---

## Chapitre 26 — Bases de données, middlewares et *runtimes*

### 26.1 La couche intermédiaire : à jour côté système, vulnérable côté applicatif

C'est le cas le plus fréquent d'obsolescence invisible : le système d'exploitation est parfaitement à jour, les correctifs sont appliqués chaque mois, les indicateurs sont au vert — et l'application s'exécute sur un environnement dont le support a pris fin il y a deux ans.

**Pourquoi cette couche échappe au dispositif**, pour quatre raisons cumulées :

1. Elle est souvent **installée hors gestionnaire de paquets**, par l'éditeur métier ou par l'équipe applicative.
2. Elle est **embarquée dans l'application** : une même machine peut porter trois versions différentes d'un même environnement d'exécution.
3. Ses **cycles de support sont courts** — souvent deux à quatre ans, contre cinq à dix pour un système d'exploitation.
4. Elle n'appartient à personne : trop applicative pour l'exploitation, trop technique pour le métier.

### 26.2 Bases de données

| Objet | Ce qui se dégrade | Point d'attention |
|---|---|---|
| Version majeure | Fin de support, souvent 5 à 8 ans | Migration lourde : compatibilité applicative, tests |
| Version mineure | Correctifs de sécurité réguliers | Souvent différée par crainte d'indisponibilité |
| Moteur et extensions | Modules additionnels avec leur propre cycle | Rarement inventoriés |
| Configuration | Comptes par défaut, chiffrement, journalisation | Souvent la vulnérabilité réelle (ch. 22) |

**La spécificité opérationnelle** : une base de données est un composant **à état**. Les stratégies du §6.4 ne s'y appliquent pas directement, et le point de non-retour du §6.7 y est central. Trois configurations de correction, par ordre de préférence :

| Configuration | Interruption | Condition |
|---|---|---|
| Réplication avec bascule | Quelques secondes à minutes | Compatibilité entre versions pendant la transition (§2.7) |
| Fenêtre planifiée | Durée de l'opération | Standard, mais impose la fenêtre |
| Migration avec bascule applicative | Variable | Réservée aux montées de version majeures |

### 26.3 Compatibilité applicative et schémas

Ce qui bloque réellement une montée de version de base de données n'est presque jamais la base : c'est l'**application** qui s'appuie dessus.

| Blocage | Manifestation |
|---|---|
| Certification de l'éditeur métier | L'application n'est supportée que sur une version précise |
| Fonctionnalité dépréciée utilisée | Le code applicatif emploie une syntaxe supprimée |
| Comportement modifié | Tri, encodage, gestion des valeurs nulles : l'application fonctionne différemment |
| Pilote d'accès | Le connecteur ne supporte pas la nouvelle version |

**La conséquence pour le MCS** : la montée de version de base de données est un **projet applicatif**, pas une opération d'infrastructure. Elle se planifie avec l'équipe applicative et l'éditeur, avec le délai correspondant — souvent six à douze mois. D'où l'importance de l'anticipation du chapitre 12.

### 26.4 Serveurs web, mandataires et serveurs d'applications

Ces composants sont **exposés par nature** et traitent des entrées non fiables. Ils appartiennent presque toujours à la classe C1.

**Trois points spécifiques :**

- **Les modules et extensions** ont leur propre cycle : un serveur web à jour peut charger un module vulnérable non maintenu.
- **La configuration prime souvent sur la version** : en-têtes, méthodes autorisées, gestion des erreurs, limites de taille. Un serveur à jour mal configuré expose davantage qu'un serveur légèrement en retard bien configuré.
- **Le mandataire inverse est un point de contrôle privilégié** : c'est là que se placent les mesures compensatoires du §20.3, ce qui en fait aussi un actif critique.

### 26.5 Brokers, caches, moteurs de recherche, ordonnanceurs

Composants d'infrastructure applicative, souvent installés pour un besoin technique et jamais revus.

⚠️ **PIÈGE — le composant installé sans authentification**
Beaucoup de ces produits s'installent par défaut **sans authentification**, sur le principe qu'ils ne seront joignables que depuis un réseau de confiance. Cette hypothèse est fausse dès qu'un poste du réseau est compromis (§11.4). Ce sont des cibles de choix : ils contiennent souvent des données applicatives complètes, et parfois des secrets.

**Les trois vérifications** à mener sur chacun : authentification activée ? exposition réelle mesurée ? version supportée ?

### 26.6 Les *runtimes* applicatifs

Machines virtuelles applicatives, plateformes d'exécution, interpréteurs : c'est la source d'obsolescence invisible la plus fréquente.

| Caractéristique | Conséquence |
|---|---|
| Cycles de support courts | Une version sort du support avant que le projet ne soit terminé |
| Plusieurs versions cohabitent sur une même machine | L'inventaire par machine ne suffit pas |
| Souvent embarqué avec l'application | Aucun mécanisme système ne le met à jour |
| Version imposée par l'éditeur métier | Vous héritez de son calendrier (§13.6) |

✅ **BONNE PRATIQUE (P0)** — Inventoriez les environnements d'exécution **par application**, pas par machine, avec leur version et leur date de fin de support. C'est un exercice d'une à deux journées qui révèle presque toujours plusieurs composants hors support ignorés jusque-là.

### 26.7 Les bibliothèques natives embarquées

Le composant que personne ne déclare : bibliothèques de chiffrement, de compression, d'analyse de formats, livrées **à l'intérieur** d'une application, sans passer par le gestionnaire de paquets.

**Pourquoi c'est un angle mort complet** : le scanner système ne les voit pas (elles ne sont pas des paquets), l'analyse de composition ne les voit pas (elles ne sont pas dans les dépendances déclarées), et l'éditeur métier ne les mentionne pas. Elles n'apparaissent que dans un inventaire de composants fourni par l'éditeur — d'où l'importance de l'exiger (§13.6).

### 26.8 Pilotes, agents, extensions et greffons

Toute la surface ajoutée sur une machine par des besoins ponctuels : pilotes matériels, agents de supervision, extensions de navigateur, greffons applicatifs, utilitaires métier.

**Le traitement réaliste** : on n'inventorie pas tout. On inventorie ce qui s'exécute avec des privilèges élevés — pilotes et agents — et ce qui traite des entrées non fiables — extensions de navigateur, greffons de traitement de documents. Le reste relève de la maîtrise de ce qui est installé (§22.1).

### 26.9 Clients lourds et postes utilisateurs

Les postes portent eux aussi des environnements d'exécution et des bibliothèques embarquées, souvent installés par des applications métier et jamais mis à jour. C'est le prolongement du §19.5 : le trou noir du poste de travail ne se limite pas aux applications visibles.

### 26.10 Négocier la montée de version avec un éditeur métier

Situation la plus fréquente : votre environnement d'exécution est hors support, et l'éditeur de l'application refuse de supporter une version plus récente.

**La séquence qui fonctionne :**

1. **Écrire la demande**, avec la date de fin de support du composant et la référence de la source (§13.8).
2. **Demander un engagement daté** : à quelle date une version compatible sera-t-elle disponible ?
3. **En l'absence de réponse ou d'engagement**, formaliser une dérogation (§7.4) dont le signataire est le propriétaire métier, et dont le motif est explicitement *« l'éditeur ne fournit pas de version compatible »*.
4. **Inscrire le sujet au renouvellement contractuel** — c'est le seul moment où vous disposez d'un levier.
5. **Compenser** dans l'intervalle (chapitre 20).

**Ce que produit cette séquence**, au-delà de la protection technique : elle transforme un problème technique subi par l'exploitation en une décision de gestion assumée par le métier, avec une trace. C'est ce qui débloque, tôt ou tard, le budget de migration.

### 26.11 Environnements de développement, recette et préproduction

Ces environnements portent les mêmes composants intermédiaires que la production, et sont traités au chapitre 28. Un point ici : un environnement de recette dont l'environnement d'exécution diverge de la production **invalide les tests** (§6.12). L'écart de version fait partie des quatre axes à mesurer.

### 26.12 📌 Limites

- **Applications non maintenues** : l'éditeur a disparu, le code source n'est pas disponible. La seule voie est la sanctuarisation (chapitre 32).
- **Prérequis figés par contrat** : traité au §26.10, avec une issue souvent budgétaire.
- **Multiplicité des versions** : une organisation peut porter cinq versions d'un même environnement d'exécution pour cinq applications. La rationalisation est un projet en soi, dont le bénéfice de MCS est considérable.
- **Absence de propriétaire** : c'est la cause racine la plus fréquente. Cette couche doit être explicitement rattachée à un propriétaire technique (§10.4).

### 26.13 🔴 FIL ROUGE — novembre 2027 : l'application de gestion commerciale

L'inventaire des environnements d'exécution **par application** (§26.6) est mené chez HELIOMED sur les 176 serveurs internes. Une journée et demie de travail.

**Le résultat.**

| Composant | Applications concernées | Statut |
|---|---|---|
| Environnement d'exécution A, version ancienne | 3 applications, dont la gestion commerciale | **Hors support depuis 2023** |
| Environnement d'exécution A, version courante | 9 applications | Supporté |
| Moteur de base de données, version N-2 | 2 applications | Fin de support dans 7 mois |
| Serveur d'applications, version ancienne | 1 application | **Hors support depuis 2024** |
| Bibliothèque de chiffrement embarquée | Inconnue — non déclarée par l'éditeur | **Non mesuré** |

**Le cas central : l'application de gestion commerciale.** Utilisée par 60 personnes, elle porte le fichier clients. Elle s'exécute sur un environnement hors support depuis 2023 — c'est celle du mini-lab 7 (§20.10), dont la dérogation expire le 31 mars 2028.

L'éditeur a été relancé trois fois depuis juin. Réponse obtenue en novembre, par écrit : une version compatible existe, elle est facturée 40 k€, et la version actuelle ne sera plus supportée du tout à compter de septembre 2028.

**Ce que change la réponse écrite.** Le sujet cesse d'être un arbitrage technique. Trois faits sont désormais établis et datés : le composant est hors support depuis quatre ans, une solution existe et son prix est connu, et une seconde échéance arrive en septembre 2028. Karim Lebrun inscrit les 40 k€ au budget 2028 en quinze minutes — ce que dix-huit mois de discussions techniques n'avaient pas obtenu.

**La découverte annexe, plus préoccupante.** Le serveur d'applications hors support depuis 2024 porte une application développée en interne en 2019, dont l'équipe a été dissoute lors d'une réorganisation. Personne ne sait la reconstruire. Le code source existe, mais aucune chaîne de construction fonctionnelle. C'est le cas limite du §26.12, et il est renvoyé au chapitre 32.

**La ligne « non mesuré ».** La bibliothèque de chiffrement embarquée dans le progiciel métier n'est pas déclarée par l'éditeur. La demande d'inventaire des composants est intégrée au courrier de renouvellement contractuel, en application du §13.6 — première application concrète de l'effet de propagation réglementaire du §25.20.

**Livrable de l'épisode.** L'inventaire des composants intermédiaires par application, versé au référentiel d'obsolescence du chapitre 12, avec trois échéances datées et une ligne non mesurée assumée.

→ La suite en 🔴 §27.7, quand la question des micrologiciels reviendra sans avoir jamais eu de propriétaire.

→ **Chapitre 27 — Couches basses et périphéries** : les couches basses, les moins visibles et les plus en retard.

### Synthèse mentale du chapitre 26

La couche intermédiaire — bases de données, serveurs d'applications, environnements d'exécution, bibliothèques embarquées — est la source d'obsolescence invisible la plus fréquente : système parfaitement à jour, indicateurs au vert, et une application qui s'exécute sur un composant hors support depuis deux ans. Quatre raisons se cumulent : installation hors gestionnaire de paquets, embarquement dans l'application, cycles de support courts, et absence de propriétaire. Ce qui bloque une montée de version de base de données n'est presque jamais la base mais l'application : c'est donc un projet applicatif de six à douze mois, pas une opération d'infrastructure. Les brokers, caches et moteurs de recherche s'installent souvent sans authentification, sur l'hypothèse d'un réseau de confiance qui devient fausse au premier poste compromis. Enfin, l'inventaire doit se faire **par application** et non par machine, et la négociation avec un éditeur métier récalcitrant se gagne par une demande écrite, un engagement daté et une dérogation signée par le métier — pas par la persuasion technique.

**Trois questions de vérification**

1. Vos serveurs affichent 98 % de conformité aux correctifs système. Quelle question posez-vous pour savoir si vos applications s'exécutent sur des composants supportés ?
2. Pourquoi une montée de version de base de données se planifie-t-elle sur six à douze mois plutôt que sur une fenêtre de maintenance ?
3. Un éditeur métier refuse de supporter une version récente de l'environnement d'exécution. Décrivez les cinq étapes de la séquence à suivre, et expliquez ce que produit l'étape 3 au-delà de la protection technique.

---

## Chapitre 27 — Couches basses et périphéries

### 27.1 Micrologiciels : inventaire, déploiement, risque

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

### 27.2 Le risque *pre-boot*

Un composant qui s'exécute avant le système d'exploitation ne peut pas être surveillé par les protections qui s'exécutent dedans. Une compromission à ce niveau survit à une réinstallation complète, et parfois au remplacement du disque.

**Ce qui protège réellement, dans l'ordre :**

1. **Le démarrage sécurisé activé** — sans lui, les autres mécanismes ne servent à rien.
2. **Les bases de certificats à jour** — c'est le cas du §3.8, dont la dégradation est silencieuse.
3. **Le mot de passe de configuration du micrologiciel** — sans lui, quiconque a un accès physique désactive le reste.
4. **Le chiffrement du disque avec liaison au matériel** — rend inefficace l'extraction du disque.
5. **La protection contre le retour en arrière** du micrologiciel.

📌 **LIMITES** — Ces mesures se décident **à l'achat et au déploiement initial**. Les activer sur un parc existant est possible mais coûteux, et certaines opérations — activer le démarrage sécurisé, changer le mode de démarrage — peuvent nécessiter une réinstallation. C'est un cas typique où le MCS *by design* du chapitre 6 se paie très cher quand il a été négligé.

### 27.3 Équipements réseau et de sécurité : la fin de support de sécurité

Le §19.6 a traité le déploiement. Un point spécifique mérite d'être isolé, parce qu'il est méconnu et coûteux.

**Trois dates coexistent** sur un équipement réseau, et elles ne sont pas simultanées :

| Date | Signification |
|---|---|
| Fin de commercialisation | On ne peut plus l'acheter |
| **Fin de support de sécurité** | **Plus aucun correctif de sécurité — la seule qui compte pour le MCS** |
| Fin de support matériel | Plus de remplacement, plus d'assistance |

La fin de support de sécurité est souvent **antérieure de plusieurs années** à la fin de support matériel. Un équipement sous contrat de maintenance actif, remplacé en cas de panne, peut ne plus recevoir aucun correctif depuis longtemps. L'organisation, elle, a le sentiment d'un équipement « sous contrat ».

✅ **BONNE PRATIQUE (P0)** — Suivez la date de fin de support **de sécurité** dans votre référentiel d'obsolescence (§12.2), distinctement des autres. C'est cette date qui déclenche le remplacement, pas la panne.

### 27.4 Appliances et boîtiers fournisseur

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

### 27.5 Périphériques et objets connectés d'entreprise

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

### 27.6 ⚠️ Les équipements de sécurité comme cible privilégiée

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

### 27.7 🔴 FIL ROUGE — décembre 2027 : la ligne « micrologiciels : non mesuré »

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

### Synthèse mentale du chapitre 27

Le contrôleur de gestion à distance des serveurs est un actif de niveau 0 : il permet d'allumer, réinstaller et prendre la main indépendamment du système d'exploitation, dispose de ses propres comptes — souvent ceux du constructeur — et est presque systématiquement absent des inventaires. Le risque avant démarrage échappe à toutes les protections logicielles, et les mesures qui le traitent se décident à l'achat : les rétrofitter coûte très cher. Sur les équipements réseau, la fin de support **de sécurité** précède souvent de plusieurs années la fin de support matériel, ce qui donne le sentiment trompeur d'un équipement « sous contrat ». Les appliances sont des boîtes noires dont on hérite du calendrier : les quatre exigences se portent au contrat, avant l'installation. Enfin, les équipements de sécurité exposés sont des cibles privilégiées pour cinq raisons structurelles, et la conséquence opérationnelle est nette : après exploitation potentielle, on reconstruit plutôt qu'on corrige.

**Trois questions de vérification**

1. Vos scans de vulnérabilités ne remontent rien d'anormal sur vos serveurs. Quel équipement, présent sur chacun d'eux, échappe pourtant entièrement à cette mesure, et pourquoi est-il critique ?
2. Un équipement réseau est sous contrat de maintenance actif. Que devez-vous vérifier avant d'en conclure qu'il est maintenu en sécurité ?
3. Une passerelle d'accès distant a été exposée avec une vulnérabilité exploitable. Le correctif est appliqué. Pourquoi n'est-ce pas suffisant ?

---

## Chapitre 28 — Environnements non productifs et actifs d'administration

### 28.1 Pourquoi la non-production doit être maintenue

L'argument « ce n'est que de la préproduction » repose sur une hypothèse implicite fausse : que ces environnements ne contiennent rien d'intéressant et ne mènent nulle part.

**Les quatre raisons pour lesquelles ils comptent autant que la production :**

| Raison | Mécanisme |
|---|---|
| **Données de production copiées** | La recette est alimentée par une copie de la base réelle, sans anonymisation dans la majorité des cas |
| **Pivot** | Ces environnements sont souvent joignables depuis et vers la production |
| **Secrets persistants** | Les mêmes comptes de service, les mêmes clés, parfois les mêmes mots de passe |
| **Durcissement moindre** | Configuration relâchée « pour faciliter les tests », journalisation absente |

**La question qui tranche**, à poser à toute équipe défendant l'exclusion d'un environnement : *contient-il des données réelles, et depuis quelles machines est-il joignable ?* Dans une majorité de cas, la réponse fait entrer l'environnement dans le périmètre de classe C2 au minimum.

### 28.2 Cartographier l'oublié

| Environnement | Ce qu'il contient souvent | Pourquoi il échappe |
|---|---|---|
| Préproduction / recette | Copie de production | Considéré comme non critique |
| Développement | Données partielles, secrets | Géré par les équipes de développement |
| Laboratoire technique | Configurations expérimentales | Créé et oublié |
| Environnement de formation | Données factices ou réelles | Utilisé quelques jours par an |
| Démonstrateur commercial | **Données réalistes, exposé** | Hébergé hors DSI (§11.12) |
| Environnement de secours | Copie complète de la production | Non maintenu car « inactif » |

**L'environnement de secours mérite une attention particulière** : maintenu à l'identique de la production pour pouvoir la remplacer, il est souvent oublié des campagnes de correctifs parce qu'il n'est pas en service. Le jour où l'on bascule dessus, on bascule sur un système en retard de plusieurs mois — au moment précis où l'on est le plus vulnérable.

### 28.3 Postes de développement et chaînes d'intégration

| Actif | Risque spécifique |
|---|---|
| **Poste de développeur** | Droits locaux étendus, outils nombreux, code source, secrets, accès aux dépôts |
| **Agent d'exécution de la chaîne** | Accès aux registres, aux environnements de déploiement, aux secrets de construction |
| **Serveur de gestion de sources** | Contient tout votre code et son historique, y compris les secrets qui y ont transité |
| **Registre d'artefacts** | Une image compromise se propage à toute la production |

⚠️ **PIÈGE — l'agent d'exécution éphémère**
Les agents créés à la demande et détruits après usage n'apparaissent dans aucun inventaire réseau (§10.8). Ils sont pourtant souvent les actifs les plus privilégiés de l'organisation : ils déploient en production. L'inventaire doit se faire **depuis l'orchestrateur**, pas depuis le réseau, et leur configuration de référence doit être traitée avec le niveau d'exigence d'un actif de niveau 0.

### 28.4 Les actifs d'administration

Ce sont les premiers à maintenir, et ils sont souvent parmi les derniers traités.

| Actif | Pourquoi il est critique |
|---|---|
| **Poste d'administration** | Porte les sessions privilégiées ; sa compromission donne accès à tout ce qu'il administre |
| **Rebond / passerelle d'administration** | Point de passage obligé, donc cible concentrée |
| **Serveur de déploiement** | Capable d'exécuter du code sur l'ensemble du parc |
| **Console de gestion de virtualisation** | Contrôle de toutes les machines virtuelles (§3.1) |
| **Console de sauvegarde** | Accès à toutes les données, y compris historiques |
| **Coffre-fort de secrets** | Concentration de tous les accès |
| **Outil de scan** | Identifiants privilégiés et cartographie des faiblesses (§15.4) |

✅ **BONNE PRATIQUE (P0) — le poste d'administration dédié**
La mesure au meilleur rapport effort/risque de tout ce chapitre : les tâches d'administration se réalisent depuis un poste **dédié**, qui ne sert ni à la messagerie, ni à la navigation, ni à la bureautique. La raison est mécanique : un poste qui ouvre des pièces jointes et une session d'administration du domaine ne doivent pas être la même machine. Cette mesure ne coûte que de la rigueur, et elle casse le chemin d'attaque le plus fréquent (§11.4).

### 28.5 Modèles et images de référence

**Le mécanisme** : une machine créée à partir d'un modèle ancien naît avec tout le retard du modèle. Elle sera peut-être rattrapée par la campagne suivante — ou non, si elle est éphémère.

| Objet | Question à se poser |
|---|---|
| Modèle de machine virtuelle | De quand date-t-il ? Qui le met à jour, à quelle fréquence ? |
| Image de référence de poste | Idem |
| Image de conteneur de base | Cadence de reconstruction (§3.2) |
| Modèle d'infrastructure décrite par code | Versions des modules et connecteurs (§23.5) |
| Procédure d'installation manuelle | Encore plus problématique : elle vieillit sans que personne ne s'en aperçoive |

✅ **BONNE PRATIQUE (P0)** — Fixez une **cadence maximale de reconstruction des modèles**, suivez leur âge comme indicateur, et intégrez le contrôle de conformité à leur production (§22.4). C'est le remède à la récurrence du §17.9, et il traite la cause au lieu du symptôme.

### 28.6 Instantanés et supports de restauration

Un instantané pris avant une intervention et conservé six mois est une machine vulnérable en attente d'être réactivée.

| Objet | Risque | Traitement |
|---|---|---|
| Instantané de machine virtuelle | Restauration = retour à un état non corrigé | Durée de vie limitée, purge automatique |
| Sauvegarde restaurée | Réintroduit l'état d'origine | Contrôle de conformité systématique après restauration |
| Machine clonée pour test | Duplique les vulnérabilités et les secrets | Inventaire, durée de vie, suppression |
| Support d'installation | Contient une version ancienne | Régénération périodique |

**La règle** : toute restauration ou tout clonage déclenche un **contrôle de conformité** avant remise en service. C'est l'une des cinq causes de récurrence du §17.9, et c'est la plus facile à traiter.

### 28.7 Actifs intermittents

Postes nomades rarement connectés, matériel de secours stocké, équipements saisonniers, machines de laboratoire éteintes la plupart du temps, pièces de rechange préparées.

**Le problème commun** : ils ne sont pas là au moment des campagnes, et ils reviennent en service avec un retard proportionnel à leur absence.

**Les trois traitements** :

1. **Agent plutôt que scan réseau** : c'est la seule façon de les atteindre quand ils sont connectés, où qu'ils soient.
2. **Contrôle à la reconnexion** : une machine absente depuis plus de N jours passe par une phase de mise à jour avant d'accéder aux ressources.
3. **Mise à jour avant stockage** pour le matériel de secours — et acceptation qu'il vieillira quand même, d'où l'intérêt des pièces prépatchées du chapitre 29.

### 28.8 L'accès conditionnel fondé sur le niveau de mise à jour

**Le principe** : subordonner l'accès aux ressources à l'état de conformité de la machine. Une machine en retard de correctifs voit son accès restreint jusqu'à régularisation.

| Ce que cela apporte | Ce que cela ne règle pas |
|---|---|
| Traite les actifs intermittents sans campagne dédiée | Ne fonctionne que sur les machines enrôlées |
| Rend la conformité visible pour l'utilisateur | Ne dit rien des machines qui n'accèdent à rien |
| Déplace l'effort de la relance vers le mécanisme | Peut être contourné par des chemins d'accès non couverts |

⚠️ **PIÈGE — le blocage sans échappatoire**
Un mécanisme qui bloque brutalement provoque deux réactions : des tickets massifs au support, et la recherche de contournements par les utilisateurs. La mise en œuvre progressive — avertissement, puis restriction partielle, puis blocage — avec une procédure d'exception traçable, est la seule qui tienne dans la durée.

### 28.9 ⚠️ « Ce n'est que de la préprod » : reconstitution du chemin réel

```
Serveur de préproduction, non durci, non surveillé, hors périmètre de scan
   → contient une copie de la base de production de janvier
   → le compte de service applicatif y est le MÊME qu'en production
   → ce compte dispose de droits de lecture sur le serveur de fichiers de production
   → le serveur de fichiers contient les sauvegardes de configuration des équipements réseau
   → ces configurations contiennent les secrets d'administration
```

Cinq étapes, aucune vulnérabilité logicielle exploitée après la première. Chaque étape résulte d'une décision de commodité parfaitement rationnelle prise isolément — c'est la combinaison toxique du §11.5.

**Les trois ruptures les moins coûteuses** dans cette chaîne : des comptes de service **distincts** entre production et non-production ; l'anonymisation des données copiées en recette ; l'absence de joignabilité directe entre les deux environnements.

### 28.10 🔴 FIL ROUGE — janvier 2028 : l'agent d'exécution de Nantes

Les quatre agents d'exécution de la chaîne d'intégration de Nantes, identifiés en janvier 2026 (§3.9), n'avaient jamais été traités autrement que par la désignation d'un propriétaire — Yann Prigent. Deux ans plus tard, la revue des actifs d'administration les remet sur la table.

**Ce que l'analyse établit.**

| Constat | Détail |
|---|---|
| Configuration | Agents créés à la demande depuis une image construite en 2024 |
| Droits | Un jeton d'accès permanent avec droits d'écriture sur le registre d'images **et** droits de déploiement sur le cluster de production |
| Réseau | Joignables depuis le réseau de développement, non segmentés |
| Secrets | Trois secrets de production accessibles pendant la construction |
| Journalisation | Aucune : les agents sont détruits après usage, leurs journaux avec |
| Inventaire | Absents du périmètre de référence — créés et détruits automatiquement (§10.8) |

**Le chemin d'attaque reconstitué**, en quatre étapes : poste de développeur compromis → accès au dépôt de code → modification d'un fichier de définition de construction → l'agent exécute le code modifié avec ses droits de déploiement en production.

Aucune vulnérabilité logicielle n'intervient après la première étape. C'est exactement le schéma du §25.18 et du §28.9.

**Les décisions, en trois vagues.**

*Immédiat.* Le jeton permanent est remplacé par une identité à durée de vie courte, obtenue à l'exécution et limitée au strict nécessaire. Les droits de déploiement en production sont retirés des agents de construction : le déploiement devient une étape distincte, avec une approbation humaine pour la production.

*Sous un mois.* Segmentation du réseau des agents. Journalisation exportée avant destruction de l'agent. Reconstruction de l'image des agents, et cadence de reconstruction fixée à 30 jours (§28.5).

*Structurel.* Les agents d'exécution entrent au périmètre de référence, inventoriés **depuis l'orchestrateur** et non depuis le réseau. Ils sont classés C1, au titre d'actifs d'administration.

**La discussion la plus difficile.** L'équipe de développement conteste initialement l'approbation humaine avant déploiement en production, qui ralentit la livraison. L'arbitrage retenu, en comité, est un pré-arbitrage au sens du §9.4 : approbation requise pour la production uniquement, automatique pour tous les autres environnements, et déléguée à un rôle et non à une personne pour ne pas créer de goulot. La livraison perd quelques minutes ; la chaîne cesse d'être un chemin direct vers la production.

**Ce que Claire Nadeau note au comité.** *Nous avons mis deux ans à traiter quatre machines qui n'existent que quelques minutes à la fois, et qui disposaient de plus de droits que n'importe quel administrateur de l'entreprise.*

→ **Fin de la Partie IV.** La suite en 🔴 §29.11, avec l'arbitrage sur la ligne 2 de Saint-Étienne.

→ **Chapitre 29 — MCS en environnement industriel (OT / ICS)** : l'industriel, où toutes les règles précédentes s'inversent.

### Synthèse mentale du chapitre 28

« Ce n'est que de la préproduction » repose sur une hypothèse fausse : ces environnements contiennent des copies de données réelles, partagent les mêmes comptes de service, sont joignables depuis et vers la production, et sont moins durcis. L'environnement de secours est le cas le plus perfide : maintenu à l'identique pour remplacer la production, il est exclu des campagnes parce qu'il n'est pas en service — et l'on bascule dessus au moment où l'on est le plus vulnérable. Les agents d'exécution des chaînes de construction sont souvent les actifs les plus privilégiés de l'organisation et n'apparaissent dans aucun inventaire réseau : ils s'inventorient depuis l'orchestrateur. Le poste d'administration dédié est la mesure au meilleur rapport effort/risque du chapitre : un poste qui ouvre des pièces jointes et une session d'administration du domaine ne doivent pas être la même machine. Enfin, toute restauration ou clonage doit déclencher un contrôle de conformité — c'est la cause de récurrence la plus facile à traiter.

**Trois questions de vérification**

1. Une équipe demande d'exclure la préproduction du périmètre de scan. Quelles deux questions posez-vous, et quelle réponse ferait basculer l'environnement en classe C2 ?
2. Reconstituez en cinq étapes un chemin d'attaque partant d'un serveur de préproduction et aboutissant aux secrets d'administration réseau. Quelles sont les trois ruptures les moins coûteuses ?
3. Vos agents de construction sont créés à la demande et détruits après usage. Pourquoi n'apparaissent-ils dans aucun inventaire, et où faut-il aller les chercher ?

---

---

> ### 🎓 À ce stade de la Partie IV, vous savez…
>
> - **dériver** un référentiel de durcissement en motivant chaque écart, et mesurer une conformité de configuration sans produire un chiffre faux ;
> - **traiter** la dérive comme une propriété des systèmes vivants, par détection et convergence plutôt que par réprimande ;
> - **réduire** la dette d'annuaire, faire une rotation de secret qui soit réellement effective, et inventorier ce qui expire ;
> - **traiter** les vulnérabilités du code que vous avez écrit vous-même — celles qu'aucun outil de composition ne verra ;
> - **inventorier** les composants intermédiaires par application, et négocier une montée de version avec un éditeur récalcitrant ;
> - **atteindre** les couches que les outils ne remontent pas : micrologiciels, contrôleurs de gestion, périphériques ;
> - **traiter** les environnements que personne ne regarde : non-production, agents de construction, actifs d'administration.
>
> **Ce que vous ne savez pas encore** : comment adapter tout cela quand les règles changent. C'est l'objet de la Partie V.
