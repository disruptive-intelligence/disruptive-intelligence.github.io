---
title: Chapitre 2 — Socle technique 1
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE I — Fondations, socle technique et maintenabilité
  - index.md
---

systèmes, paquets, cycles de support, réseau, identité

Ce chapitre installe les mécanismes concrets. Il ne suppose aucune expérience préalable d'administration, mais il ne survole rien : ces mécanismes expliquent la quasi-totalité des malentendus, des faux positifs et des échecs de correction que vous rencontrerez ensuite.

## 2.1 Anatomie d'un système à maintenir

Quand quelqu'un affirme « ce serveur est à jour », l'affirmation est ambiguë. Un système est un empilement de couches, mises à jour par des mécanismes différents, à des rythmes différents, souvent par des personnes différentes.

| Couche | Contenu | Qui la met à jour | Nécessite un redémarrage ? |
|---|---|---|---|
| Micrologiciel | BIOS/UEFI, contrôleur de gestion à distance, cartes | Constructeur, via un outil séparé | Oui, souvent complet |
| Noyau | Cœur du système d'exploitation | Éditeur du système | Oui, sauf correction à chaud |
| Bibliothèques partagées | Code commun réutilisé par de nombreux programmes | Éditeur du système | Non, mais redémarrage des services qui les utilisent |
| Services système | Serveur web, base de données, service d'annuaire | Éditeur du système ou éditeur tiers | Redémarrage du service |
| Applications | Logiciels métier, souvent installés hors gestionnaire de paquets | Éditeur métier, parfois manuellement | Variable |
| Agents | Sécurité, sauvegarde, supervision, gestion de parc | Console centrale correspondante | Variable |
| Environnements d'exécution embarqués | Machine virtuelle applicative, interpréteur livré avec l'application | Souvent **personne** | Variable |

⚠️ **PIÈGE — la couche que personne ne met à jour**
La dernière ligne est le trou noir classique. Une application métier livrée avec sa propre copie d'un environnement d'exécution ou d'une bibliothèque de chiffrement ne sera mise à jour par **aucun** mécanisme système. Le système d'exploitation sera parfaitement à jour, le scanner ne verra peut-être rien, et le composant vulnérable sera là depuis trois ans. Le chapitre 26 traite entièrement cette couche.

Point essentiel à retenir : **une bibliothèque partagée corrigée sur disque continue d'être exécutée dans sa version vulnérable par tous les processus déjà lancés**, jusqu'à leur redémarrage. Corriger et redémarrer sont deux actes distincts, et seul le second termine le travail. C'est la raison d'être des outils présentés au §2.6.

## 2.2 Comment un correctif est réellement produit et distribué

C'est le mécanisme le plus important du chapitre. Il explique à lui seul une grande partie des faux positifs que vous rencontrerez.

**Le trajet complet d'une correction :**

```
1. Découverte de la faille          → chercheur, éditeur, attaquant
2. Correction dans le code source   → projet « amont » (upstream)
3. Publication d'une version amont  → ex. version 3.2.4 du projet
4. Reprise par l'éditeur du système → décision : nouvelle version, ou backport
5. Construction du paquet           → compilation, tests, numérotation
6. Signature cryptographique        → l'éditeur signe le paquet
7. Publication sur un dépôt         → dépôt officiel, miroirs
8. Récupération par votre machine   → le client vérifie la signature
9. Installation                     → écriture des fichiers
10. Redémarrage du composant        → le code corrigé s'exécute enfin
```


Une correction devient effective **lorsque le code corrigé est réellement chargé et exécuté**. Dans certains cas, l'installation suffit — un binaire lancé à chaque exécution est corrigé immédiatement. Dans beaucoup d'autres, il faut redémarrer le processus, le service, voire le système. Un programme de MCS qui s'arrête à l'étape 9 sans vérifier l'étape 10 laisse donc, dans un nombre de cas non négligeable, du code vulnérable en cours d'exécution.

🖼 **SCHÉMA — Le trajet d'un correctif, de l'amont au chargement effectif.** *Chaîne linéaire à dix étapes, avec l'étape 10 (redémarrage) mise en évidence et la bifurcation « backport » à l'étape 4.*

### Le *backport* : la notion qui fausse tous les scanners

À l'étape 4, l'éditeur d'un système à support long a deux options. Soit il livre la nouvelle version amont — ce qui risque de casser les applications de ses utilisateurs. Soit il **extrait uniquement le correctif de sécurité et l'applique à la version ancienne** qu'il distribue déjà. Cette seconde option s'appelle le *backport*, et c'est le fonctionnement normal de toutes les distributions à support long.

Conséquence directe, et contre-intuitive : **le numéro de version affiché ne reflète plus la présence ou l'absence de la faille.**

🎯 **CE QUE ÇA CHANGE POUR VOUS** — Votre scanner vous signalera des vulnérabilités déjà corrigées, en volume, sur tout votre parc à support long. Si vous lancez une campagne sur ce signal sans vérifier, vous consommerez des fenêtres, des redémarrages et du temps d'équipe pour rien — et vous prendrez un risque de régression sans aucune contrepartie. C'est exactement ce qui arrive au §15.13, sur 42 serveurs.

**Exemple simplifié — volontairement fictif, pour isoler le mécanisme.** Une faille est corrigée en amont dans la version 3.0.15 d'une bibliothèque. Votre serveur affiche la version 3.0.11. Un scanner qui raisonne sur le seul numéro amont conclut : vulnérable. Or le paquet installé porte le numéro complet `3.0.11-1+deb12u3` : le suffixe indique une révision de sécurité de l'éditeur, qui contient précisément le correctif rétroporté. La machine n'est pas vulnérable, et le scanner a produit un **faux positif structurel**.

Deux précisions, parce que ce mécanisme est souvent mal reproduit :

- La **syntaxe varie selon le paquet et la distribution**. On rencontre aussi bien les formes `+debXuY` que `~debXuY`, et les familles RPM utilisent une numérotation de publication différente. Ne cherchez pas un motif universel : cherchez la révision propre à l'éditeur.
- Le raisonnement vaut pour les distributions à support long. Sur une distribution à version continue, le numéro amont redevient une information fiable.

🧪 **EN PRATIQUE — vérifier si un correctif est réellement présent**

```bash
# Famille Debian / Ubuntu : version exacte du paquet installé
dpkg -l | grep openssl
apt-cache policy openssl

# Le journal des modifications du paquet cite les CVE corrigées
zcat /usr/share/doc/openssl/changelog.Debian.gz | head -40
# ou, si le dépôt source est configuré :
apt changelog openssl | head -40

# Famille RHEL / Rocky / Alma : le changelog du paquet cite les CVE
rpm -q --changelog openssl | grep -i CVE-2024 | head

# Mises à jour disponibles
dnf updateinfo list security   # famille RHEL : filtre réellement sur la sécurité
apt list --upgradable          # famille Debian : TOUTES les mises à jour, pas seulement la sécurité
```


⚠️ **PIÈGE — deux sources qu'on prend à tort pour des preuves**
`apt list --upgradable` liste l'ensemble des mises à jour disponibles, **sans distinguer** ce qui relève de la sécurité. Ne le présentez jamais comme une liste de correctifs de sécurité dans un rapport.
De même, un journal des modifications local est un **indice**, pas une preuve : il peut être incomplet, tronqué à l'installation, ou ne pas mentionner l'identifiant de la faille. La **source de vérité** est l'avis de sécurité publié par la distribution ou l'éditeur, associé à l'état officiel du paquet dans son suivi de sécurité.

La règle opérationnelle : **ne jamais conclure à une vulnérabilité sur le seul numéro de version amont d'un système à support long**, et ne jamais conclure à l'absence de vulnérabilité sur le seul journal local. Croisez avis de sécurité de la distribution et version de paquet installée. Cette vérification est au cœur du chapitre 15 (interprétation des rapports de scan).

### Ce qui se passe quand l'éditeur ne reprend pas la correction

L'étape 4 peut aussi ne jamais avoir lieu. Trois cas fréquents :

- la version que vous utilisez n'est plus supportée : la correction existe en amont, elle ne viendra jamais chez vous ;
- l'éditeur juge la faille non applicable à sa configuration : c'est parfois justifié, parfois discutable, et cela doit être documenté ;
- le composant est fourni par un éditeur métier qui ne suit pas l'amont : vous dépendez alors entièrement de son bon vouloir, ce qui est un sujet contractuel (chapitre 13).

## 2.3 Chaînes de confiance : pourquoi vous pouvez installer ce paquet

Vous téléchargez du code exécutable depuis Internet et vous l'installez avec les privilèges les plus élevés du système. Ce qui rend cette opération acceptable, c'est une chaîne de confiance cryptographique.

**Le mécanisme.** L'éditeur signe ses paquets, ou l'index qui décrit les paquets, avec une clé privée. Votre machine détient la clé publique correspondante, installée à la mise en service. Avant toute installation, le gestionnaire de paquets vérifie que la signature correspond. Si elle ne correspond pas, l'installation échoue.

Ce mécanisme protège contre trois attaques : la modification d'un paquet en transit, la compromission d'un miroir de distribution, et la substitution d'un dépôt.

**Ce qu'il ne protège pas.** Il n'atteste **ni de la qualité, ni de l'innocuité** du contenu. Une signature valide signifie « ce paquet vient bien de cet éditeur », pas « ce paquet est sûr ». Si l'éditeur lui-même est compromis, la signature reste parfaitement valide — c'est le principe des attaques sur la chaîne d'approvisionnement, traitées au chapitre 25.

⚠️ **PIÈGE — les trois ruptures de confiance les plus fréquentes**

| Rupture | Comment elle se produit | Conséquence |
|---|---|---|
| Vérification désactivée | Options du type « ignorer la signature » ajoutées pour débloquer une installation, puis jamais retirées | Toute la chaîne s'effondre silencieusement |
| Dépôt tiers non maîtrisé | Ajout d'un dépôt externe pour obtenir un logiciel précis | Ce dépôt peut mettre à jour **n'importe quel** paquet du système |
| Clé expirée ou non renouvelée | La clé de signature du dépôt arrive à expiration | Les mises à jour s'arrêtent, souvent sans alerte visible |

La troisième mérite une attention particulière : **l'arrêt des mises à jour est silencieux**. La machine ne signale pas « je ne reçois plus de correctifs » ; elle signale, au mieux, une erreur dans un journal que personne ne lit. C'est exactement le type de dégradation que le §2.9 apprend à détecter.

## 2.4 Modèles de support : lire une matrice de cycle de vie

Chaque éditeur définit une politique de support. En comprendre le vocabulaire évite des erreurs de planification à plusieurs centaines de milliers d'euros.

| Modèle | Principe | Implication MCS |
|---|---|---|
| **Support long (LTS)** | Une version figée, maintenue par *backport* pendant 5 à 10 ans | Stabilité maximale, mais numéros de version trompeurs (§2.2) |
| **Version continue** (*rolling*) | Mise à jour permanente vers l'amont | Toujours à jour, mais chaque mise à jour est un changement fonctionnel |
| **Canal long terme** (LTSC) | Équivalent Windows du support long, sans nouvelles fonctionnalités | Adapté aux postes techniques figés, pas au parc bureautique |
| **Support étendu payant** (ESU/ELS/ESM) | Correctifs de sécurité au-delà de la fin de support normale | Solution transitoire, coûteuse, **au périmètre strictement conditionné** |

Trois dates différentes coexistent dans une matrice de cycle de vie, et les confondre est une erreur classique :

- **fin de vie fonctionnelle** : plus de nouvelles fonctionnalités ;
- **fin de support** : plus de correctifs, y compris de sécurité — c'est la seule date qui compte pour le MCS ;
- **fin de support étendu** : après souscription d'une offre spécifique.

⚠️ **PIÈGE — l'éligibilité au support étendu**
Une offre de support étendu n'est jamais universelle. Elle est conditionnée : édition du produit, version précise, mode de gestion de la machine, type de licence, parfois zone géographique. Budgéter une prolongation sans avoir vérifié **ligne à ligne** l'éligibilité de son propre parc est une erreur fréquente et coûteuse : elle se découvre au moment où l'échéance est déjà là, sans plan B.

⏱ **ÉTAT DE L'ART — le cas d'école (vérifié le 30/07/2026)**
Windows 10 est en fin de support depuis le 14 octobre 2025. Microsoft a prolongé fin juin 2026 son programme de support étendu **grand public** jusqu'au 12 octobre 2027 — mais ce programme est réservé aux **appareils personnels** et exclut explicitement les machines jointes à un annuaire d'entreprise ou gérées par une solution de gestion de flotte. Un parc professionnel géré n'est donc **pas** couvert par cette prolongation et relève d'une offre commerciale distincte, payante, dont la tarification augmente à chaque année reconduite. Deux autres échéances sont à distinguer soigneusement : Windows 10 Entreprise LTSB 2016 (13 octobre 2026) et Windows Server 2016 (12 janvier 2027).
La leçon dépasse le cas Microsoft : **une option de support ne se budgète jamais avant d'avoir vérifié précisément son périmètre et ses conditions d'éligibilité.**
📎 [S-24] — pages officielles de cycle de vie et de support étendu, consultées le 30/07/2026.

## 2.5 Le monde Windows : ce qu'il faut comprendre du mécanisme

**Le rythme.** Microsoft publie ses correctifs de sécurité le deuxième mardi de chaque mois. Des correctifs hors cycle sont publiés en cas d'urgence. Cette régularité est un avantage : elle permet de planifier des fenêtres récurrentes plutôt que de négocier chaque intervention.

**Le format.** Depuis plusieurs années, les correctifs sont **cumulatifs** : un paquet mensuel contient toutes les corrections des mois précédents. Vous ne « manquez » donc pas un correctif ancien en installant le plus récent. En contrepartie, le paquet est indivisible : vous ne pouvez pas choisir de n'appliquer qu'une seule correction.

**La réversibilité n'est pas garantie.** Le paquet cumulatif intègre également la mise à jour de la pile de maintenance, laquelle n'est pas désinstallable. Cela ne signifie pas que toute mise à jour cumulative soit impossible à retirer : la réversibilité réelle dépend du paquet concerné, de l'état du magasin de composants, des opérations de nettoyage déjà effectuées sur la machine, des prérequis installés et de la nature exacte de la régression rencontrée.

La doctrine opérationnelle qui en découle est prudente, et elle vaut d'être retenue telle quelle :

> **Ne construisez jamais un plan de retour arrière en supposant qu'une mise à jour Windows sera désinstallable.**

Si la désinstallation fait partie de votre plan, **vérifiez-la avant le déploiement**, sur une machine représentative. Et gardez comme plan principal un mécanisme qui ne dépend pas d'elle : instantané de machine virtuelle, sauvegarde restaurable, redéploiement à partir d'une image. Ce point est déterminant au chapitre 18.

🧪 **EN PRATIQUE — connaître l'état réel d'une machine Windows**

```powershell
# Ce que les correctifs installés racontent (liste souvent incomplète)
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10

# La vérité : version + numéro de build + révision (UBR)
Get-ComputerInfo -Property OsName, OsVersion, OsBuildNumber
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild, UBR

# Redémarrage en attente ? (contrôle partiel : un seul des signaux possibles)
Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending"
```


Le couple **build + révision (UBR)** est l'indicateur principal du niveau de mise à jour cumulative du système. Il ne couvre en revanche ni les applications, ni les composants facultatifs, ni l'environnement de récupération, ni les pilotes, ni les micrologiciels — chacun se vérifie séparément. La liste des correctifs installés, elle, est incomplète sur les versions récentes et ne doit pas servir de preuve.

**Le mécanisme durable : la correction à chaud.** Certaines corrections peuvent être appliquées directement au code en cours d'exécution en mémoire, sans redémarrer. Le principe général est toujours le même : une mise à jour cumulative de référence, avec redémarrage, est installée périodiquement ; entre deux références, les correctifs de sécurité sont appliqués à chaud. Le bénéfice porte sur la disponibilité, pas sur la couverture : certaines catégories de mises à jour restent hors périmètre et continuent d'exiger un redémarrage.

⏱ **ÉTAT DE L'ART — la correction à chaud Windows Server (vérifié le 30/07/2026)**
Pour Windows Server 2025 (éditions Standard et Datacenter), la correction à chaud est disponible sur les machines rattachées à Azure Arc, y compris hors Azure — sur site, en périphérie ou chez un autre fournisseur cloud. **Depuis le 19 mai 2026, ce service est fourni sans coût additionnel** : la facturation par cœur qui s'appliquait auparavant a été supprimée, y compris pour les machines déjà inscrites. Les éditions *Datacenter: Azure Edition* en bénéficient nativement.
Cadence : les mois de référence (janvier, avril, juillet, octobre) installent une mise à jour cumulative complète **avec redémarrage** ; les deux mois suivants reçoivent des correctifs à chaud sans redémarrage — soit environ quatre redémarrages planifiés par an au lieu de douze.
Prérequis notables : version minimale du système, sécurité basée sur la virtualisation activée, et démarrage sécurisé — ce qui relie directement ce dispositif au §3.8.
📌 Hors périmètre de la correction à chaud : plusieurs catégories de mises à jour, notamment les pilotes, les micrologiciels et certains composants applicatifs. La correction à chaud réduit le nombre de redémarrages ; elle ne les supprime pas et ne couvre pas tout le système.
⚠️ Ce bloc illustre pourquoi les offres commerciales ne doivent pas figurer dans le corps du cours : la même fonctionnalité était facturée par cœur onze mois plus tôt. Le **mécanisme** est stable, le **modèle économique** ne l'est pas.
📎 [S-26] — documentation officielle, consultée le 30/07/2026.

## 2.6 Le monde Linux : paquets, redémarrages et correction à chaud

**Deux grandes familles.** Les distributions dérivées de Debian utilisent le format `.deb` et les outils `apt`/`dpkg` ; celles dérivées de Red Hat utilisent le format `.rpm` et l'outil `dnf`. Les principes sont identiques, la syntaxe diffère.

**La numérotation.** Un numéro de paquet complet se lit ainsi : `1.2.3-4+deb12u2`. La partie `1.2.3` est la version amont, `-4` la révision de l'empaquetage, `+deb12u2` la révision de sécurité de l'éditeur. C'est cette dernière partie qui bouge lors d'un correctif de sécurité, et c'est elle que vous devez comparer (voir §2.2).

Un mécanisme piège existe également : la notion d'**époque**, un préfixe rarement visible (`1:1.2.3`) qui prend le pas sur tout le reste dans les comparaisons de version. Un outil de corrélation qui l'ignore peut conclure à tort qu'un paquet est plus ancien qu'il ne l'est.

**Le redémarrage des services.** C'est le point le plus souvent négligé sous Linux, précisément parce que le système, lui, n'a pas besoin de redémarrer.

🧪 **EN PRATIQUE — identifier ce qui doit être redémarré après une mise à jour**

```bash
# Famille Debian / Ubuntu
sudo apt install needrestart
sudo needrestart -r l          # liste les services utilisant du code obsolète

# Famille RHEL / Rocky / Alma
sudo dnf install dnf-utils
needs-restarting -s            # services concernés
needs-restarting -r            # le système requiert-il un redémarrage complet ?

# Vérification indépendante : processus utilisant des fichiers supprimés
sudo lsof -n | grep -i 'DEL.*\.so' | awk '{print $1, $2}' | sort -u
```


**La correction à chaud du noyau.** Plusieurs éditeurs proposent d'appliquer des correctifs de sécurité au noyau **sans redémarrer**, via un abonnement. C'est un outil précieux pour les systèmes à forte contrainte de disponibilité, mais son périmètre est étroit et doit être compris :

📌 **LIMITES — ce que la correction à chaud du noyau ne fait pas**

- Elle ne couvre **que le noyau**, pas les bibliothèques ni les services applicatifs, qui représentent la majorité des vulnérabilités exploitées.
- Elle ne couvre qu'une **partie** des vulnérabilités du noyau : certaines corrections sont structurellement inapplicables à chaud.
- Elle **diffère** le redémarrage, elle ne le supprime pas : un redémarrage reste nécessaire à échéance, et une machine qui n'a pas redémarré depuis 700 jours pose d'autres problèmes (dérive de configuration non testée, démarrage non validé, systèmes de fichiers jamais vérifiés).
- Elle repose sur un **abonnement payant** dont le périmètre de versions couvertes doit être vérifié.

✅ **BONNE PRATIQUE (P1)** — Traitez la correction à chaud comme un moyen de **gagner du temps sur la fenêtre**, pas comme une dispense de redémarrage. Fixez une durée maximale de fonctionnement sans redémarrage (par exemple 90 jours) et suivez-la comme un indicateur à part entière.

## 2.7 Équipements réseau et de sécurité : le maintien le plus risqué

Pare-feu, routeurs, commutateurs, passerelles d'accès distant, répartiteurs de charge : ces équipements concentrent trois caractéristiques qui en font le point le plus délicat du MCS.

**Ils sont exposés.** Beaucoup sont, par construction, joignables depuis Internet. C'est précisément leur fonction.

**Ils sont monolithiques.** Vous ne corrigez pas un composant : vous remplacez l'image logicielle complète. Toute mise à jour est donc une montée de version, avec son risque fonctionnel propre.

**Ils imposent une interruption.** Le redémarrage est presque toujours nécessaire, et il coupe le trafic.

Deux mécanismes atténuent ce dernier point.

**La double partition d'image.** La plupart des équipements professionnels stockent deux images logicielles. Vous installez la nouvelle sur la partition inactive, vous basculez au redémarrage, et en cas d'échec vous revenez à la précédente. C'est le seul véritable retour arrière du domaine, et il faut le tester avant d'en dépendre.

**La haute disponibilité.** Sur un couple d'équipements redondants, la séquence est toujours la même : mettre à jour le membre passif, vérifier, basculer le trafic, mettre à jour l'ancien membre actif, rebasculer. Cette séquence n'est **pas** sans effet : selon la conception du cluster et le degré de synchronisation d'état entre les membres, la bascule peut entraîner la perte des sessions établies — certains équipements synchronisent les tables de sessions, d'autres non, et le comportement diffère souvent selon les protocoles. Par ailleurs, les deux membres fonctionnent temporairement dans des versions différentes, ce que tous les constructeurs ne supportent pas. Ces deux points se vérifient dans la documentation **avant** l'intervention, pas pendant.

⚠️ **PIÈGE — la doctrine « toujours N-1 » appliquée sans nuance**
Beaucoup d'organisations se donnent pour règle de rester une version derrière la dernière publiée, afin d'éviter les régressions. La règle est raisonnable en régime normal. Elle devient dangereuse dans deux cas : quand la version N-1 est justement celle qui contient la faille exploitée, et quand l'écart s'installe et devient N-3 ou N-4 sans que personne ne le mesure. **Une doctrine de version doit être une décision datée et revue, pas une habitude.**

## 2.8 Identité : ce qu'un correctif ne corrigera jamais

Les services d'annuaire — annuaire d'entreprise sur site, annuaire d'identité en ligne — appellent une distinction fondamentale.

**Ce qu'un correctif corrige** : les vulnérabilités du logiciel d'annuaire lui-même.

**Ce qu'un correctif ne corrige pas** : tout ce qui s'est accumulé dans les données de l'annuaire depuis sa création. Comptes de personnes parties depuis des années, comptes de service créés pour un projet abandonné, délégations d'administration accordées lors d'une migration en 2014, appartenances à des groupes privilégiés jamais revues, protocoles d'authentification anciens laissés actifs pour un logiciel qui n'existe plus.

Cette accumulation porte un nom dans ce cours : la **dette de configuration d'annuaire**. Elle ne se dégrade pas toute seule, elle **croît** toute seule, à chaque projet, à chaque incident résolu dans l'urgence, à chaque migration. Aucune mise à jour ne la réduira. Le chapitre 24 y est consacré.

⚠️ **PIÈGE — le correctif à activation différée**
Certaines corrections de sécurité importantes ne s'activent pas à l'installation. L'éditeur les livre d'abord en mode « observation » — la nouvelle règle est appliquée mais les cas non conformes sont seulement journalisés, pour ne pas casser les environnements — puis annonce une date à laquelle le mode « application » deviendra obligatoire.

Ces déploiements en plusieurs phases sont un piège classique : l'organisation installe le correctif, coche la case, et découvre plusieurs mois plus tard, à la date d'application forcée, que des authentifications échouent parce que le travail intermédiaire — analyser les journaux, corriger les cas non conformes — n'a jamais été fait.

✅ **BONNE PRATIQUE (P0)** — Pour tout correctif comportant un calendrier d'application en plusieurs phases, créez immédiatement **deux** échéances dans votre suivi : la date d'installation, et la date de bascule en mode application. Entre les deux, une tâche explicite d'analyse des journaux d'observation, avec un propriétaire nommé. Un correctif resté en mode observation peut apporter une protection partielle — certaines vérifications sont déjà actives — mais **il n'apporte pas encore la protection complète attendue**, et c'est bien celle-ci que vous croyez avoir déployée.

## 2.9 La journalisation minimale pour prouver qu'un correctif est appliqué

Nous arrivons à l'exigence la plus négligée du socle technique. Vous devez pouvoir répondre, plusieurs mois après, à cette question : *cette correction a-t-elle été appliquée sur cet actif, et quand ?*

> **Un journal n'est pas une preuve parce qu'il existe.** Il devient une preuve lorsqu'on peut établir son intégrité, son périmètre et son contexte — c'est-à-dire ce qu'il couvre, ce qu'il ne couvre pas, et qu'il n'a pas été modifié.

**Trois niveaux de preuve, de la plus faible à la plus forte :**

| Niveau | Nature | Valeur | Faiblesse |
|---|---|---|---|
| 1 — Déclaratif | « Nous appliquons les correctifs chaque mois » | Nulle en audit | Aucune donnée |
| 2 — Console centrale | Rapport de l'outil de déploiement | Correcte | Ne couvre que les actifs connus de l'outil, et masque les machines injoignables |
| 3 — État constaté sur l'actif | Version ou révision relevée directement sur la machine, horodatée | Forte | Nécessite une collecte propre |

L'état constaté sur l'actif est **généralement la preuve technique la plus forte**, parce qu'il est indépendant de l'outil qui a réalisé le déploiement. Cela ne disqualifie pas le niveau 2 : un rapport de console constitue une preuve parfaitement recevable dès lors que trois conditions sont établies — le **périmètre** couvert par l'outil est défini et rapproché du périmètre de référence, l'**intégrité** du rapport est assurée (extraction datée, non retouchée), et la **liste des actifs non joignables** est fournie. Ce qui n'est pas recevable, c'est un rapport de console présenté sans ces trois éléments.

🧪 **EN PRATIQUE — les sources de preuve natives**

```bash
# Debian / Ubuntu : journal complet des opérations de paquets
grep -E "upgrade|install" /var/log/dpkg.log | tail -20
zcat -f /var/log/apt/history.log* | grep -A3 "Start-Date"

# RHEL / Rocky / Alma : historique des transactions
dnf history list | head -20
dnf history info <ID>          # contenu détaillé d'une transaction
```


```powershell
# Windows : journal d'installation des mises à jour
Get-WinEvent -LogName Setup -MaxEvents 50 |
    Where-Object { $_.Id -in 1,2,4 } |
    Select-Object TimeCreated, Id, Message
```


✅ **BONNE PRATIQUE (P0) — les six champs d'une preuve exploitable**
Identifiant de l'actif · état constaté (version, révision) · date et heure de la constatation · méthode de collecte · périmètre couvert par la collecte · **liste explicite des actifs non joignables au moment de la collecte**.
Le dernier champ est celui qu'on oublie, et c'est celui que l'auditeur demandera. Un rapport indiquant « 100 % conforme » sur les machines répondantes, sans mentionner les 140 machines injoignables, n'est pas une preuve : c'est une omission.

🔴 **FIL ROUGE — décembre 2025 : trois chiffres qui ne concordent pas**

Six semaines après la note de Claire Nadeau à la direction générale (§1.9), Malik Ferhaoui rend son premier inventaire. Il a croisé trois sources.

| Source | Ce qu'elle mesure | Effectif |
|---|---|---|
| **C** — Base de gestion de configuration (tenue manuellement) | Ce que l'entreprise **croit** posséder | 187 |
| **K** — Console de déploiement des correctifs | Ce qui est **effectivement géré** par le canal de correction | 164 |
| **D** — Découverte réseau + inventaire de l'hyperviseur | Ce qui **répond** réellement | 210 |

Trois sources, trois chiffres. Le réflexe naturel est de demander « lequel est le bon ? ». C'est la mauvaise question : aucun ne l'est, et c'est la **structure des écarts** qui porte l'information.

**Table de réconciliation des ensembles**

| Ensemble | Description | Effectif |
|---|---|---|
| K ⊆ C | Déclarées **et** gérées par la console | 164 |
| C ∩ D, hors K | Déclarées et actives, mais **jamais atteintes** par la console | 12 |
| C \ D | Déclarées mais ne répondant plus : éteintes sans décommissionnement | 11 |
| **C** (total) | 164 + 12 + 11 | **187** |
| C ∩ D | Déclarées et actives (164 + 12) | 176 |
| D \ C | Actives mais **non déclarées** | 34 |
| **D** (total) | 176 + 34 | **210** |
| **C ∪ D — périmètre de référence** | 176 actives déclarées + 34 actives non déclarées + 11 à décommissionner | **221** |

Les **23 machines** présentes dans la base de gestion mais absentes de la console se décomposent donc en deux populations très différentes : **12 machines actives** qui n'ont jamais reçu de correctif par ce canal — dont trois serveurs de préproduction contenant une copie des données de production (chapitre 28) — et **11 machines éteintes** dont les enregistrements réseau et les comptes de service existent toujours (chapitre 35).

Les **34 machines actives non déclarées** se répartissent en 19 machines créées pour des tests et jamais enregistrées, 13 appliances virtuelles livrées par des éditeurs métier (§3.1), et 2 serveurs appartenant à une filiale rattachée en 2022.

**Le chiffre qui compte, et les trois qu'on lui préfère habituellement.** La console affiche 97 % de conformité. Ce chiffre est exact — et il ne veut presque rien dire tant qu'on ne précise pas son dénominateur.

| Indicateur | Calcul | Valeur |
|---|---|---|
| Conformité **dans la population mesurée** | 159 conformes / 164 gérées | **97 %** |
| **Couverture** de la console sur les actifs en service | 164 gérées / 210 actives | **78 %** |
| **Ratio confirmé conforme** sur les actifs en service | 159 / 210 | **≈ 76 %** |
| **Ratio confirmé conforme** sur le périmètre maître | 159 / 221 | **≈ 72 %** |
| **Non mesuré** | 46 actifs en service, hors console | **22 % des actifs en service** |

⚠️ Les deux lignes de ratio sont **conservatrices** : elles traitent tout actif non mesuré comme non conforme. C'est une hypothèse de prudence, pas une mesure — la conformité réelle des 46 machines hors console est **inconnue**, et c'est précisément l'information qui manque (Annexe K.2).

⚠️ Notez le glissement de vocabulaire, qui est l'erreur la plus fréquente du domaine : **couverture** et **conformité** ne sont pas la même chose. La couverture mesure ce que l'outil atteint ; la conformité mesure l'état de ce qu'il atteint. Une organisation peut afficher 100 % de conformité sur 40 % de couverture, et l'annoncer de bonne foi. Les définitions rigoureuses de ces deux indicateurs figurent au §38.2 et en Annexe K.

**Décision prise.** Aucun achat d'outil. Trois règles sont posées : le périmètre de référence sera désormais l'union des sources, jamais l'une d'elles seule ; tout indicateur devra afficher son dénominateur et le nombre d'actifs non joignables ; et les mots « couverture » et « conformité » ne seront plus employés l'un pour l'autre dans aucun document interne.

**Livrable de l'épisode.** Un fichier de réconciliation à trois colonnes, avec pour chaque écart une cause identifiée et un propriétaire nommé — c'est exactement l'exercice du mini-lab 2, au chapitre 10.

→ La suite en 🔴 §3.9, quand l'inventaire rencontre les environnements que la découverte réseau ne voit pas.

## 2.10 📌 Ce que ce cours ne couvre pas, et où l'acquérir

Par honnêteté envers le lecteur débutant, voici ce que ce chapitre suppose acquis ou n'enseigne pas :

| Domaine | Ce que le cours suppose | Où combler |
|---|---|---|
| Administration système | Savoir se connecter à une machine et lire un journal | Cours d'administration Linux/Windows |
| Réseau | Comprendre adressage, routage, filtrage | Cours réseau généraliste |
| Développement | Rien n'est supposé ; les notions utiles sont expliquées aux ch. 6 et 25 | — |
| Cryptographie | Rien n'est supposé ; les notions utiles sont expliquées au ch. 24 | — |
| Gestion de vulnérabilités | **Rien n'est supposé** : c'est l'objet du chapitre 4 | — |

Le cours est autonome sur son sujet. Il ne l'est pas sur les disciplines voisines, et prétendre le contraire vous desservirait.

## Synthèse mentale du chapitre 2

Un système est un empilement de couches mises à jour par des mécanismes différents, à des rythmes différents, souvent par des personnes différentes — et la couche embarquée dans les applications n'est mise à jour par personne. Un correctif suit un trajet long, de l'amont jusqu'au chargement effectif du code corrigé, et il n'est efficace qu'au bout de ce trajet. Le rétroportage explique qu'un numéro de version amont ne dit rien de la présence d'une faille sur une distribution à support long : c'est la source de faux positifs la plus structurelle du domaine. Les chaînes de confiance cryptographiques garantissent l'origine d'un paquet, pas son innocuité, et leur rupture est silencieuse. Sous Windows, la réversibilité d'un correctif ne se suppose jamais ; sous Linux, l'installation ne suffit pas sans redémarrage des services concernés. Un annuaire ne se corrige pas par mise à jour : sa dette de configuration croît toute seule. Enfin, une preuve exploitable comporte six champs, dont la liste des actifs non joignables — celui qu'on oublie et que l'auditeur demandera.

**Trois questions de vérification**

1. Un scanner signale une bibliothèque en version 3.0.11 alors que la faille est corrigée en 3.0.15 amont. Quelles vérifications faites-vous, dans quel ordre, et quelle source fait finalement foi ?
2. Vous venez d'appliquer un correctif de bibliothèque sur cinquante serveurs Linux. Le travail est-il terminé ? Que vérifiez-vous, et avec quelle commande ?
3. Votre plan de retour arrière pour une campagne de correctifs Windows repose sur la désinstallation du paquet. Pourquoi est-ce fragile, et par quoi le remplacez-vous ?

---
