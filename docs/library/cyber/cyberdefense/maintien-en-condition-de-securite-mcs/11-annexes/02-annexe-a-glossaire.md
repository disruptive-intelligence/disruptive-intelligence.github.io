---
title: Annexe A — Glossaire
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
---

**Accès conditionnel** — Mécanisme subordonnant l'accès aux ressources à l'état de conformité de l'appareil. §28.8
**Actif** — Élément matériel, logiciel, informationnel, humain ou de service ayant une valeur pour l'organisation ou participant au fonctionnement de son système d'information. Un actif sans propriétaire nommé est un actif *orphelin*, pas un non-actif.
**Actif de niveau 0** — Actif dont la compromission donne le contrôle d'un ensemble d'autres actifs : annuaire, hyperviseur, sauvegarde, coffre-fort, chaîne de construction. §11.7
**Actif d'entrée** — Actif par lequel un attaquant peut arriver, exposé par conception. §11.7
**Actif éphémère** — Actif créé et détruit automatiquement, absent des inventaires réseau. §10.8
**Actif maintenu** — Actif disposant d'un propriétaire nommé, d'une classe de service et d'une preuve de conformité.
**Actif orphelin** — Actif réel du périmètre, sans propriétaire désigné. Jamais exclu du dénominateur.
**Agent** — Programme résident remontant l'état d'une machine à une console centrale. §15.1
**Agilité cryptographique** — Capacité à changer d'algorithme ou de protocole sans reconstruire les applications. §24.8
**Anneau de déploiement** — Population successive recevant un correctif, avec critère de passage. §18.4
**Appliance** — Équipement ou machine virtuelle préconstruite dont le système n'est pas maintenable par le client. §3.1
**Arbre de décision** — Suite de questions ordonnées produisant une action plutôt qu'un score. §16.3
**Atteignabilité** — Possibilité effective d'appeler le code vulnérable dans un contexte donné. §11.6
**Autorisation déléguée** — Accès accordé à une application tierce au nom d'un utilisateur, matérialisé par un jeton, non révoqué par un changement de mot de passe. §31.6
**Backlog** — Ensemble des constats ouverts. §17.10
**Baseline** — Référentiel de configuration dérivé et versionné, propre à l'organisation. §22.3
**Bleu / vert** — Stratégie de déploiement à deux environnements complets, avec bascule du trafic. §6.4
**Chaîne de confiance** — Mécanisme cryptographique garantissant l'origine d'un paquet ou d'un micrologiciel. §2.3
**Chemin d'attaque** — Enchaînement d'étapes menant d'un point d'entrée à une cible. §11.4
**Classe de service** — Regroupement d'actifs partageant délais, fenêtres et niveau de test. §7.2
**CNA** — Organisation accréditée pour attribuer des identifiants de vulnérabilité. §4.2
**Combinaison toxique** — Ensemble d'éléments individuellement acceptables dont la conjonction crée un risque majeur. §11.5
**Compte de secours** — Compte d'urgence permettant l'accès quand les mécanismes normaux échouent. §24.2
**Conduit** — Chemin de communication entre zones, au sens des normes industrielles. §29.2
**Conformité** — Part des actifs se trouvant dans l'état attendu. Toujours accompagnée de son dénominateur. §38.2
**Constat** — Toute observation appelant une décision de remédiation : vulnérabilité, écart de configuration, résultat d'audit, secret exposé. §14.2
**Contrôleur de gestion à distance** — Composant permettant d'administrer un serveur indépendamment de son système d'exploitation. Actif de niveau 0. §27.1
**Convergence** — Réapplication périodique d'un état désiré par un outil de gestion de configuration. §23.3
**Correctif** — Modification publiée par un éditeur corrigeant un défaut.
**Correction virtuelle** — Blocage de l'exploitation en amont, sans modifier l'actif. §20.3
**Couverture** — Part du périmètre de référence atteinte par un outil ou un processus. §38.2
**CPE** — Nomenclature d'identification de produits, historique des bases de vulnérabilités. §4.3
**Critère d'arrêt** — Seuil chiffré interrompant automatiquement un déploiement. §18.4
**CSAF** — Format d'avis de sécurité lisible par machine. §4.8
**CVE** — Identifiant unique de vulnérabilité ; clé de dédoublonnage, pas jugement de gravité. §4.2
**CVSS** — Système de notation de la gravité technique intrinsèque d'une vulnérabilité. §4.4
**CWE** — Catalogue de types de faiblesses, indépendant des produits. §4.3
**Défaut d'autorisation** — Vulnérabilité applicative permettant d'accéder à des données d'autrui ; invisible à l'analyse automatique. §25.1
**Délai d'observation** — Temps volontairement laissé entre publication et déploiement pour que les régressions apparaissent ailleurs. §18.3
**Dénominateur** — Ensemble sur lequel un indicateur est rapporté ; l'attribut le plus important d'une mesure. §38.2
**Dépendance transitive** — Dépendance d'une dépendance, non choisie directement. §3.6
**Dépriorisation** — Décision documentée de ne pas traiter maintenant, avec date de revue. Un constat déprioritisé reste ouvert. §16.6
**Dérive de configuration** — Écart croissant entre l'état réel et la référence. §23.1
**Dérogation** — Décision formalisée, datée, bornée et compensée de ne pas appliquer la règle. §7.4
**Dette de sécurité** — Somme mesurable des corrections différées et de l'obsolescence. §1.6
**Découverte externe** — Cartographie de la surface exposée, réalisée depuis Internet. §11.2
**Démarrage sécurisé** — Vérification de la signature des composants chargés au démarrage. §3.8
**Effacement sécurisé** — Suppression de données avec preuve, sur tous les supports et copies. §35.4
**Époque** — Préfixe de version prenant le pas sur le reste dans les comparaisons de paquets. §2.6
**EPSS** — Modèle prédisant la probabilité d'exploitation d'une vulnérabilité à court terme. §4.5
**Exclusion** — Retrait volontaire d'un actif ou d'un chemin du périmètre d'un outil. Dérogation déguisée sans motif ni date de revue. §15.6, §34.4
**Exploit** — Code ou procédure transformant une vulnérabilité en effet concret. §4.1
**Exploitation active** — Observation réelle d'attaquants utilisant une vulnérabilité. §4.1
**Exposition** — Possibilité pour un attaquant d'atteindre un composant vulnérable. §11.1
**Faiblesse** — Type de défaut décrit indépendamment de tout produit. §4.1
**Fait vérifié / hypothèse probable / piste exploratoire** — Échelle de qualification d'une information. §14.7
**Fenêtre de maintenance** — Créneau pendant lequel une interruption est acceptée. §5.2
**Fichier de verrouillage** — Fichier figeant les versions exactes des dépendances. §3.6
**Fin de support** — Date après laquelle aucun correctif n'est publié, y compris de sécurité. §12.1
**Fin de support de sécurité** — Sur les équipements réseau, souvent antérieure à la fin de support matériel. §27.3
**Gel de production** — Période d'interdiction de changement, avec clause de levée pour vulnérabilité exploitée. §5.2
**Golden image** — Image de référence servant à créer les instances. §28.5
**Homologation** — Décision formelle autorisant l'usage d'un système, dont le maintien dépend du MCS. §39.5
**Immutabilité** — Principe de ne jamais modifier un système en service : reconstruire et remplacer. §3.5
**Interrupteur de fonctionnalité** — Paramètre activant ou désactivant un comportement sans redéploiement. §6.5
**Inventaire de composants (SBOM)** — Liste des composants d'un logiciel avec leurs versions. §4.8
**KEV (catalogue d'exploitation avérée)** — Recensement des vulnérabilités observées en exploitation. §4.6
**Live patching** — Application de correctifs au noyau sans redémarrage, à périmètre limité. §2.6
**MCO** — Maintien en condition opérationnelle : garantir que le système fonctionne. §1.2
**MCS** — Maintien en condition de sécurité : maintenir le niveau de sécurité sur tout le cycle de vie, preuve incluse. §1.1
**Mesure compensatoire** — Réduction de risque appliquée quand la correction est impossible ; sept attributs obligatoires. §20.7
**Micrologiciel** — Logiciel de bas niveau exécuté avant ou sous le système d'exploitation. §3.8
**Modèle de Purdue** — Découpage en niveaux d'une architecture industrielle. §3.7
**Non détecté / non vulnérable / non scanné** — Trois états distincts apparaissant identiquement dans un rapport. §15.8
**Périmètre de référence (périmètre maître)** — Union des sources d'inventaire, incluant orphelins et actifs à décommissionner. Point de départ du choix de dénominateur, **pas dénominateur universel** : chaque indicateur définit sa population éligible. §10.3, Annexe I.4
**Population éligible** — Sous-ensemble du périmètre maître auquel un contrôle donné s'applique effectivement. Annexe I.4
**Non mesuré** — Actif éligible à un contrôle mais non évalué. Ne devient jamais conforme par défaut. Annexe I.4
**N/A (non applicable)** — Actif hors de la population éligible d'un contrôle, avec motif documenté. Annexe I.4
**Horloge de risque** — Décompte du temps pendant lequel le risque existe ; ne se suspend jamais, contrairement au délai opérationnel de traitement. §17.5
**Ratio conservateur** — Taux calculé en traitant tout actif non mesuré comme non conforme. Hypothèse de prudence, pas mesure. Annexe K.2
**Point de non-retour** — Instant après lequel un retour arrière exige une restauration de données. §6.7
**Preuve d'état** — Version ou révision relevée directement sur l'actif, horodatée. §2.9
**Propriétaire métier** — Personne décidant de l'interruption et portant le risque. §5.5
**Propriétaire technique** — Personne exécutant la correction et produisant la preuve. §5.5
**Protection contre le retour en arrière** — Refus d'installer une version antérieure vulnérable. §6.11
**PSIRT** — Fonction traitant la sécurité des produits mis sur le marché. §33.2
**purl** — Nomenclature d'identification de paquets logiciels dans leur écosystème. §4.3
**Récurrence** — Réapparition d'un constat clos ; signale presque toujours un problème d'image de référence. §17.9
**Rétroportage (backport)** — Application d'un correctif à une version ancienne sans changer son numéro amont. §2.2
**Rolling update** — Déploiement progressif instance par instance. §6.4
**Sanctuarisation** — Réduction d'un système à un périmètre d'usage minimal, strictement contrôlé. §32.2
**Sas de transfert** — Étape contrôlée d'entrée de fichiers dans une zone industrielle. §29.5
**SSVC** — Approche de priorisation par arbre de décision. §4.7
**Support étendu** — Correctifs de sécurité au-delà de la fin de support, payants et conditionnés. §12.1
**Suspension de compteur** — Arrêt légitime et limitativement défini du décompte d'un délai. §17.5
**Témoin (canary)** — Déploiement sur une fraction du trafic ou du parc, avec mesure. §6.4
**Traîne longue** — Résidu d'actifs non traités en fin de campagne ; concentre une part disproportionnée du risque. §18.10
**VEX** — Déclaration d'exploitabilité d'un composant vulnérable dans un produit donné. §4.8
**Zone** — Ensemble d'actifs industriels partageant les mêmes exigences de sécurité. §29.2
**0-day** — Vulnérabilité sans correctif disponible. §4.1
**n-day** — Vulnérabilité corrigée mais non appliquée ; à l'origine de l'écrasante majorité des compromissions. §4.1

---
