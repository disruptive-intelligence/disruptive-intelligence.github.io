---
title: Partie 2 — Grands principes défensifs
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - index.md
---

> Ces principes sont les **invariants** de la défense. Ils ne dépendent ni de la technologie ni de la mode. Maîtrisés, ils permettent d'évaluer n'importe quelle architecture.


## Chapitre 11 — Défense en profondeur

**Définition.** Empiler *plusieurs couches* de sécurité indépendantes, pour qu'aucune faille unique ne soit fatale. Métaphore du château : douves, remparts, herse, donjon, gardes.

**Principe.** Chaque couche peut échouer ; ce qui protège, c'est que l'attaquant doive *toutes* les franchir. Les couches doivent être **diverses** (pas dix firewalls identiques, mais firewall + segmentation + EDR + MFA + journalisation) pour qu'une même faille ne les traverse pas toutes.

🔧 **Exemple concret** — Un mail malveillant doit franchir : filtrage mail → sensibilisation de l'utilisateur → antivirus → EDR → segmentation → moindre privilège → détection SOC. Chaque couche réduit la probabilité de succès complet.

⚠️ **Erreur fréquente** — La « défense en largeur » : empiler des couches *redondantes* (même type) au lieu de *complémentaires*. Trois antivirus ne valent pas un antivirus + une segmentation.

🧭 **Taxonomie** — Méta-principe qui chapeaute presque tous les autres (segmentation, moindre privilège, MFA en sont des couches).

🎯 **À retenir** — Aucune couche n'est parfaite ; la profondeur transforme une faille unique en simple incident.


## Chapitre 12 — Moindre privilège

**Définition.** Accorder à chaque utilisateur, service ou processus *uniquement* les droits strictement nécessaires à sa fonction, et rien de plus (Principle of Least Privilege, PoLP).

**Principe.** Réduit l'impact d'une compromission : un compte limité, une fois volé, ne donne accès qu'à peu de choses. Inclut la *limitation dans le temps* (droits temporaires, just-in-time) et dans le *périmètre*.

🔧 **Exemple concret** — Une application web qui ne fait que *lire* une base ne doit pas avoir de droits d'*écriture* ni d'*administration*. Si elle est compromise par injection SQL, les dégâts restent limités à de la lecture.

⚠️ **Erreur fréquente** — Donner les droits administrateur « pour que ça marche tout de suite », puis ne jamais les retirer. L'accumulation de droits (privilege creep) est un fléau silencieux.

🧭 **Taxonomie** — Contre-mesure directe de l'*élévation de privilèges* (chapitre 84) et du *lateral movement* (chapitre 144). Pilier du Zero Trust.

🎯 **À retenir** — Le moindre privilège ne *prévient* pas l'intrusion, il en *limite l'impact*. C'est l'application de « assume breach ».


## Chapitre 13 — Besoin d'en connaître

**Définition.** Variante du moindre privilège appliquée à l'*information* : on n'accède à une donnée que si on en a besoin pour sa mission (need-to-know), même si on a l'habilitation théorique.

**Principe.** L'habilitation (niveau de confidentialité autorisé) et le besoin d'en connaître sont *cumulatifs* : avoir le niveau « secret » ne donne pas accès à *tous* les secrets, seulement à ceux nécessaires à sa tâche.

🔧 **Exemple concret** — Un analyste autorisé au niveau « confidentiel » n'a pas à consulter les dossiers RH d'un autre service, même classés au même niveau.

🧭 **Taxonomie** — Issu du monde militaire/renseignement, central dans la classification de l'information (chapitre 34).

🎯 **À retenir** — Habilitation ≠ accès. Le besoin d'en connaître ferme la porte même aux personnes « de confiance ».


## Chapitre 14 — Séparation des tâches

**Définition.** Répartir une action sensible entre *plusieurs personnes* pour qu'aucune seule ne puisse la mener de bout en bout (Separation of Duties, SoD). Le but : prévenir la fraude et l'erreur.

**Principe.** Celui qui *demande* n'est pas celui qui *approuve* ; celui qui *développe* n'est pas celui qui *met en production*. Implique aussi la *rotation* et le *double contrôle* (four-eyes principle).

🔧 **Exemple concret** — Un virement important nécessite un initiateur et un validateur distincts. Un seul compte compromis ne suffit alors pas à détourner les fonds.

🧭 **Taxonomie** — Contrôle organisationnel (GRC), contre-mesure de la fraude interne et de l'abus de privilèges. Complète le moindre privilège côté processus.

🎯 **À retenir** — Diviser une action critique entre plusieurs acteurs supprime le « point unique de malveillance ».


## Chapitre 15 — Cloisonnement et segmentation

**Définition.** *Découper* le système d'information en zones isolées pour qu'un incident dans l'une ne se propage pas aux autres.

- **Cloisonnement** : terme général de séparation logique ou physique entre environnements (prod/dev, métiers, niveaux de sensibilité).
- **Segmentation (réseau)** : découpage du réseau en sous-réseaux/VLAN avec filtrage entre eux, limitant la circulation latérale.

**Principe.** Sans segmentation, une fois un poste compromis, tout le réseau est atteignable (réseau « plat »). Avec segmentation, l'attaquant est contenu dans une zone.

🔧 **Exemple concret** — Isoler le réseau bureautique du réseau industriel (OT) empêche un ransomware bureautique d'arrêter l'usine.

🧭 **Taxonomie** — Contre-mesure majeure du *lateral movement* (chapitre 144). Précurseur de la microsegmentation (chapitre 16) et de la segmentation détaillée en Partie 12.

🎯 **À retenir** — Un réseau plat transforme une intrusion locale en compromission globale. Segmenter, c'est compartimenter le naufrage.


## Chapitre 16 — Microsegmentation

**Définition.** Forme fine de segmentation où l'on isole jusqu'à la *charge de travail individuelle* (machine, conteneur, application), avec des politiques de filtrage au plus près de chaque ressource, indépendantes de la topologie réseau physique.

**Principe.** Plutôt que de cloisonner par grands sous-réseaux, on définit *qui peut parler à qui* au niveau de chaque flux applicatif (par exemple : ce serveur web peut parler à cette base sur ce port, et à rien d'autre). C'est un fondement opérationnel du Zero Trust.

🔧 **Exemple concret** — Dans un datacenter, deux serveurs sur le même sous-réseau ne peuvent communiquer que si une règle explicite l'autorise — l'« est-ouest » est verrouillé.

🧭 **Taxonomie** — Évolution de la segmentation, fortement liée au Zero Trust (chapitre 17) et à la sécurité cloud/conteneurs (Partie 10).

🎯 **À retenir** — La microsegmentation passe du « cloisonner par zones » au « cloisonner par flux ». Le lateral movement devient très coûteux pour l'attaquant.


## Chapitre 17 — Zero Trust

**Définition.** Modèle de sécurité fondé sur « **ne jamais faire confiance, toujours vérifier** » : aucun utilisateur, appareil ou flux n'est implicitement de confiance du seul fait d'être « à l'intérieur » du réseau.

**Principes clés.** Vérification systématique de l'identité et de la posture à *chaque* accès ; accès au plus juste (moindre privilège) ; microsegmentation ; décision contextuelle (qui, quoi, d'où, quel appareil, quel risque) ; chiffrement généralisé. On abandonne le modèle « périmètre = château fort » au profit de « chaque ressource se défend elle-même ».

🔧 **Exemple concret** — Un employé connecté au VPN interne ne reçoit *pas* automatiquement l'accès à toutes les applications : chaque accès est réévalué selon son identité, son appareil et le contexte.

⚠️ **Erreur fréquente** — Croire que Zero Trust est un produit qu'on achète. C'est une *architecture* et une *philosophie*, mise en œuvre par de nombreux composants (IAM, MFA, ZTNA, microsegmentation, EDR).

🧭 **Taxonomie** — Cadre englobant qui combine moindre privilège, microsegmentation, IAM/MFA et assume breach. ZTNA (chapitre 280) en est la brique d'accès réseau.

🎯 **À retenir** — Zero Trust supprime la « confiance par localisation ». Être dans le réseau ne prouve plus rien.


## Chapitre 18 — Assume Breach

**Définition.** Posture mentale et stratégique : *partir du principe qu'on est déjà, ou qu'on sera, compromis*. On ne conçoit plus seulement pour empêcher l'intrusion, mais pour *limiter*, *détecter* et *répondre* quand elle survient.

**Principe.** Renverse l'optimisme défensif. Au lieu de « comment empêcher toute entrée ? », on demande « si l'attaquant est déjà dedans, jusqu'où peut-il aller, et le verrions-nous ? ». Justifie l'investissement dans la détection, la segmentation, le moindre privilège, la sauvegarde et l'exercice de crise.

🧭 **Taxonomie** — Fondement philosophique du Zero Trust et de toute la Partie 11 (détection et réponse). Contre-pied du tout-préventif.

🎯 **À retenir** — « Assume breach » ne signifie pas renoncer à la prévention, mais refuser d'en dépendre exclusivement.


## Chapitre 19 — Tiering d'administration

**Définition.** Organiser les comptes et systèmes d'administration en *niveaux (tiers)* étanches, pour qu'une compromission d'un niveau bas ne permette pas d'atteindre les joyaux.

- **Tier 0** : contrôle de l'identité et de l'infrastructure critique (contrôleurs de domaine, IAM, PKI). Le « cœur du royaume ».
- **Tier 1** : serveurs et applications métier.
- **Tier 2** : postes de travail des utilisateurs.

**Règle d'or.** Un compte d'un tier ne doit *jamais* s'authentifier sur un système d'un tier inférieur (sinon ses identifiants y deviennent volables), et un tier bas ne doit pas contrôler un tier haut.

🔧 **Exemple concret** — Un administrateur du domaine (Tier 0) ne se connecte jamais sur un poste utilisateur (Tier 2) : sinon, un poste compromis exposerait des identifiants Tier 0, permettant la prise totale du domaine.

🧭 **Taxonomie** — Contre-mesure structurante des attaques Active Directory (Partie 8), notamment pass-the-hash et lateral movement. Lié au modèle ESAE.

🎯 **À retenir** — Le tiering empêche qu'un poste banal compromis devienne une prise de contrôle du domaine entier.


## Chapitre 20 — Bastion, PAM et comptes privilégiés

**Définition.** Mesures dédiées à la protection des accès *à hauts privilèges*, qui sont les cibles de plus grande valeur.

- **Bastion** (jump server) : machine d'administration unique et durcie par laquelle *tous* les accès privilégiés transitent et sont journalisés/enregistrés.
- **PAM** (Privileged Access Management) : ensemble d'outils gérant le cycle de vie des comptes à privilèges — coffre-fort de secrets, mots de passe à usage unique, accès « just-in-time », enregistrement de session.
- **Comptes privilégiés** : administrateurs, comptes de service, comptes d'urgence (break-glass).

🔧 **Exemple concret** — Au lieu que chaque admin connaisse le mot de passe « root », le PAM le détient, le change après chaque usage, et n'accorde un accès que temporairement et tracé.

🧭 **Taxonomie** — Brique du tiering (chapitre 19) et du Zero Trust ; défense centrale en Partie 8 et Partie 12.

🎯 **À retenir** — Les comptes privilégiés sont la cible n°1. Sans bastion ni PAM, ils sont aussi le maillon faible.


## Chapitre 21 — Durcissement système

**Définition.** *Hardening* : configurer un système pour réduire sa vulnérabilité — désactiver les services inutiles, fermer les ports superflus, appliquer des configurations sécurisées, supprimer les comptes/défauts d'usine.

**Principe.** Un système installé par défaut est rarement sûr (services activés « au cas où », mots de passe par défaut, protocoles obsolètes). Le durcissement applique des référentiels (par ex. les benchmarks CIS) pour ramener le système à un état minimal et maîtrisé.

🔧 **Exemple concret** — Désactiver SMBv1, supprimer le compte invité, désinstaller les outils non utilisés, désactiver les macros par défaut.

🧭 **Taxonomie** — Réduit la surface d'attaque (chapitre 22) ; contre-mesure transversale (préventive). Détaillé en Partie 12.

🎯 **À retenir** — Un système non durci est une collection de portes ouvertes « par défaut ». Durcir = fermer ce qui ne sert pas.


## Chapitre 22 — Réduction de surface d'attaque

**Définition.** Diminuer activement le nombre de points exploitables : moins de services exposés, moins de comptes, moins de logiciels, moins de droits, moins de données conservées.

**Principe.** Chaque composant exposé est un risque potentiel. La sécurité la plus économique est souvent *l'absence* : ce qui n'existe pas ne peut être attaqué. Recoupe le durcissement, le moindre privilège et la minimisation des données.

🔧 **Exemple concret** — Supprimer une vieille application interne oubliée mais toujours en ligne élimine d'un coup toutes ses vulnérabilités potentielles.

🧭 **Taxonomie** — Principe transversal directement lié à la notion de surface d'attaque (chapitre 7) et à toute la Partie 4.

🎯 **À retenir** — La meilleure défense d'un composant inutile est sa suppression.


## Chapitre 23 — Sécurité par défaut

**Définition.** *Secure by default* : un système doit être sûr *dès l'installation*, sans que l'utilisateur ait à activer des protections. Les options sûres sont l'état par défaut ; l'insécurité doit être un choix explicite.

**Principe.** La plupart des utilisateurs ne modifient jamais les réglages par défaut. Si le défaut est non sécurisé (chiffrement désactivé, mot de passe « admin/admin », tout ouvert), la majorité du parc restera vulnérable.

🔧 **Exemple concret** — Une base de données qui, par défaut, n'écoute que sur localhost et exige un mot de passe — plutôt qu'ouverte au monde sans authentification.

🧭 **Taxonomie** — Couplé à « secure by design » (chapitre 24). Tendance lourde des cadres modernes (CISA « Secure by Design/Default »).

🎯 **À retenir** — Si la sécurité dépend d'une case à cocher que personne ne coche, elle n'existe pas.


## Chapitre 24 — Secure by design

**Définition.** Intégrer la sécurité *dès la conception* d'un système, et non comme une couche ajoutée à la fin. La sécurité est une exigence au même titre que la fonctionnalité.

**Principe.** Corriger une faille à la conception coûte une fraction de ce qu'elle coûte en production. « Secure by design » implique modélisation de menace en amont, choix d'architectures sûres, et exigences de sécurité dans les spécifications. Concept jumeau du *privacy by design* pour les données personnelles.

⚠️ **Erreur fréquente** — Le « bolt-on security » : tenter de sécuriser après coup un produit conçu sans sécurité. C'est cher, partiel et fragile.

🧭 **Taxonomie** — Englobe threat modeling (chapitre 25) et secure by default (chapitre 23). Pilier du développement sécurisé (SAST/DAST en Partie 12).

🎯 **À retenir** — La sécurité ajoutée à la fin est toujours plus chère et moins efficace que la sécurité conçue dès le départ.


## Chapitre 25 — Threat modeling

**Définition.** *Modélisation de menace* : démarche structurée pour identifier, en amont, ce qui peut mal tourner dans un système — quels actifs, quels attaquants, quelles menaces, quelles contre-mesures.

**Méthodes connues.** STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) pour catégoriser les menaces ; arbres d'attaque ; DREAD pour la cotation ; PASTA pour une approche centrée risque. Questions cardinales : *Que construit-on ? Qu'est-ce qui peut mal tourner ? Que fait-on ? A-t-on bien fait ?*

🔧 **Exemple concret** — Avant de développer une API, on liste : actifs (données clients), points d'entrée (endpoints), menaces STRIDE par endpoint, puis contre-mesures (authentification, contrôle d'accès, validation, journalisation).

🧭 **Taxonomie** — Outil central du secure by design ; relie systématiquement *menace → vulnérabilité potentielle → contre-mesure*, soit le fil rouge du cours appliqué à la conception.

🎯 **À retenir** — Le threat modeling déplace la découverte des failles du « après le piratage » vers « avant le code ».


## Chapitre 26 — Journalisation et traçabilité

**Définition.** Enregistrer de manière fiable les événements du système (connexions, actions, erreurs, accès) afin de pouvoir détecter, investiguer et prouver.

**Principe.** Sans journaux, une compromission est invisible et inexplicable. Les journaux doivent être *complets* (bonnes sources), *centralisés* (hors de portée de l'attaquant), *horodatés* (temps synchronisé), *intègres* (non modifiables) et *conservés* assez longtemps.

⚠️ **Erreur fréquente** — Journaliser localement uniquement : un attaquant qui compromet la machine efface ses traces. D'où la centralisation (SIEM) et l'immutabilité.

🧭 **Taxonomie** — Contrôle *détectif* fondamental ; matière première du SOC (Partie 11). Sert aussi l'imputabilité (chapitre 6) et le forensic (chapitre 263).

🎯 **À retenir** — Pas de journaux fiables = pas de détection, pas d'enquête, pas de preuve. La traçabilité est non négociable.


## Chapitre 27 — Supervision continue

**Définition.** *Continuous monitoring* : surveiller en permanence l'état de sécurité (journaux, alertes, vulnérabilités, conformité, posture) plutôt que par audits ponctuels.

**Principe.** Les menaces évoluent en continu ; une évaluation annuelle laisse 364 jours d'angle mort. La supervision continue (alimentée par journalisation, scanners, EDR, SIEM) donne une vue en temps quasi réel et raccourcit drastiquement le délai de détection (MTTD).

🧭 **Taxonomie** — Pilier de la fonction *Detect* (NIST CSF) ; relie journalisation (chapitre 26), SIEM/EDR (Partie 11) et gestion des vulnérabilités (chapitre 32).

🎯 **À retenir** — La sécurité n'est pas un état qu'on atteint, mais une surveillance qu'on maintient.


## Chapitre 28 — Sauvegarde, restauration et résilience

**Définition.**

- **Sauvegarde** : copie des données/systèmes permettant de revenir à un état antérieur sain.
- **Restauration** : capacité *éprouvée* à remettre en service à partir des sauvegardes.
- **Résilience** : aptitude globale de l'organisation à *continuer* et à *se rétablir* malgré l'incident.

**Règle 3-2-1 (et au-delà).** 3 copies, sur 2 supports différents, dont 1 hors site — étendue aujourd'hui à 3-2-1-1-0 : au moins 1 copie **immuable/hors-ligne** (résistante au ransomware) et 0 erreur de restauration vérifiée.

⚠️ **Erreur fréquente** — Sauvegarder sans jamais *tester la restauration*. Une sauvegarde qu'on n'a jamais restaurée n'est pas une sauvegarde, c'est un espoir. De plus, des sauvegardes accessibles en ligne sont chiffrées par le ransomware en même temps que la production.

🧭 **Taxonomie** — Contrôle *correctif/récupératif* clé ; cœur du PRA/PCA (chapitre 267) et seule vraie parade de fond au ransomware (chapitre 188).

🎯 **À retenir** — La sauvegarde immuable et testée est la dernière ligne de défense — souvent la seule qui sauve réellement face au ransomware.

---
