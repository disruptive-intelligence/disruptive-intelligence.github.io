---
title: Partie 10 — Cloud, API, conteneurs et supply chain
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - index.md
---

### Chapitre 218 — Cloud security : principes

**Définition.** Ensemble des pratiques sécurisant les ressources et données hébergées dans le cloud (IaaS/PaaS/SaaS).

**Principe central : la responsabilité partagée.** Le fournisseur sécurise *l'infrastructure* (« sécurité *du* cloud ») ; le client sécurise *ses configurations, identités et données* (« sécurité *dans* le cloud »). La frontière varie selon le modèle (IaaS → plus de responsabilité client ; SaaS → moins). La majorité des incidents cloud viennent d'erreurs *côté client* (mauvaise configuration, identités, secrets).

🧭 **Taxonomie** — Dans le cloud, la *mauvaise configuration* (chapitre 67) et l'*identité* (chapitre 57) remplacent souvent la vulnérabilité logicielle comme cause première.

⚠️ **Erreur fréquente** — Croire que « migrer dans le cloud » délègue toute la sécurité au fournisseur.

🎯 **À retenir** — Comprendre la responsabilité partagée est le préalable : le fournisseur sécurise le socle, vous restez responsable de vos configurations, identités et données.


### Chapitre 219 — IAM cloud

1. **Définition.** Gestion des identités et des droits dans le cloud — qui (utilisateur, service, rôle) peut faire quoi sur quelles ressources.
2. **Famille.** Identité / autorisation (cœur de la sécurité cloud).
3. **Principe.** L'IAM cloud est extrêmement granulaire et puissant ; mal maîtrisé, il crée des permissions excessives et des *chemins d'élévation* (un rôle pouvant en assumer un autre, plus privilégié).
4. **Sous-types.** Permissions excessives, rôles assumables en chaîne, politiques trop larges, clés/identités de service surpuissantes.
5. **Exemple conceptuel.** Un rôle peu privilégié peut en assumer un autre plus puissant, ouvrant un chemin d'élévation non prévu.
6. **Impacts.** Élévation de privilèges, accès étendu aux ressources/données, prise de contrôle du tenant.
7. **Détection.** Analyse des politiques (permissions effectives), usage anormal de rôles, journaux cloud, surveillance.
8. **Prévention.** **Moindre privilège** strict, analyse des permissions effectives, suppression des chemins d'élévation, séparation, revue d'accès, journalisation, MFA.
9. ⚠️ **Erreur fréquente.** Politiques permissives « pour que ça marche » (wildcards de permissions) jamais resserrées.
10. 🎯 **À retenir.** L'IAM est le vrai périmètre du cloud : moindre privilège, analyse des permissions effectives et suppression des chemins d'élévation sont prioritaires.


### Chapitre 220 — Bucket public

1. **Définition.** Espace de stockage objet (bucket) exposé publiquement par mauvaise configuration.
2. **Famille.** Mauvaise configuration (chapitre 67) / exposition de données.
3. **Principe.** Un stockage destiné à être privé est rendu accessible à tous (lecture, voire écriture) par une configuration trop ouverte — cause récurrente de fuites massives.
4. **Sous-types.** Lecture publique (fuite), écriture publique (altération/empoisonnement), permissions héritées trop larges.
5. **Exemple conceptuel.** Un espace de stockage contenant des données sensibles est accessible sans authentification à cause d'un réglage public.
6. **Impacts.** Fuite massive de données, altération de contenus, atteinte réglementaire.
7. **Détection.** Outils de posture cloud (CSPM), audit des configurations d'accès, surveillance des accès anonymes.
8. **Prévention.** **Blocage de l'accès public par défaut**, CSPM, chiffrement, moindre privilège, revue régulière, journalisation des accès.
9. ⚠️ **Erreur fréquente.** Rendre un bucket public « temporairement » et l'oublier ; permissions héritées non vérifiées.
10. 🎯 **À retenir.** Le bucket public est une cause classique de fuite : bloquer l'accès public par défaut et surveiller la posture (CSPM).


### Chapitre 221 — Secret exposé

1. **Définition.** Secret (mot de passe, jeton, certificat) rendu accessible dans un contexte cloud (configuration, stockage, variables, dépôt).
2. **Famille.** Exposition de secrets (chapitre 77) en contexte cloud.
3. **Principe.** Les secrets se retrouvent dans des fichiers de configuration, des images, des variables d'environnement, des dépôts — accessibles à qui ne devrait pas, offrant un accès direct.
4. **Sous-types.** Secrets dans le code/IaC, dans des images de conteneurs, dans des journaux, dans des buckets.
5. **Exemple conceptuel.** Un fichier de configuration exposé contient un secret donnant accès à un service cloud.
6. **Impacts.** Accès direct aux services/données, élévation, mouvement latéral cloud.
7. **Détection.** Secrets scanning, surveillance des dépôts/images/journaux, détection d'usage anormal de secrets.
8. **Prévention.** **Gestionnaire de secrets** dédié, interdiction des secrets en dur, scanning (pré-commit/CI), rotation/révocation rapide, moindre privilège.
9. ⚠️ **Erreur fréquente.** Stocker des secrets dans le code/l'IaC ou les variables, au lieu d'un coffre dédié.
10. 🎯 **À retenir.** Un secret exposé donne un accès immédiat : externaliser dans un coffre, scanner et faire tourner les secrets.


### Chapitre 222 — Clé API exposée

1. **Définition.** Cas particulier (et fréquent) de secret exposé : une clé d'API laissée accessible.
2. **Famille.** Exposition de secrets / accès aux services.
3. **Principe.** Les clés d'API authentifient des appels ; exposées (dépôt public, application cliente, journaux), elles permettent d'utiliser le service au nom du propriétaire, parfois avec des droits étendus et sans limite.
4. **Sous-types.** Clés dans dépôts publics, dans applications mobiles/front, dans journaux, surprivilégiées.
5. **Exemple conceptuel.** Une clé d'API trouvée dans un dépôt public permet d'appeler le service associé.
6. **Impacts.** Usage frauduleux (coûts), accès aux données, abus du service.
7. **Détection.** Secrets scanning, surveillance d'usage anormal des clés, alertes des fournisseurs.
8. **Prévention.** Coffre à secrets, **portée minimale** des clés, rotation, restriction (par IP/domaine/usage), ne pas exposer de clés sensibles côté client, scanning.
9. ⚠️ **Erreur fréquente.** Embarquer une clé puissante dans une application cliente (donc extractible).
10. 🎯 **À retenir.** Une clé d'API exposée est exploitable immédiatement : portée minimale, rotation, restriction et scanning sont indispensables.


### Chapitre 223 — Metadata service abuse

1. **Définition.** Abus du *service de métadonnées* d'instance cloud pour récupérer des identifiants temporaires.
2. **Famille.** Credential access cloud (souvent via SSRF — chapitre 107).
3. **Principe.** Les instances exposent en interne un service fournissant configuration et crédentiels de rôle ; un accès indu (via SSRF ou compromission de l'instance) permet de récupérer ces identifiants et d'usurper le rôle.
4. **Sous-types.** Via SSRF, via compromission d'instance, selon la version (renforcée ou non) du service.
5. **Exemple conceptuel.** Une faille permet d'interroger le point de métadonnées et d'obtenir les identifiants du rôle de l'instance.
6. **Impacts.** Vol d'identifiants cloud, élévation, mouvement latéral, accès aux ressources.
7. **Détection.** Accès anormaux au point de métadonnées, usage inattendu d'identifiants de rôle, journaux.
8. **Prévention.** **Version renforcée** du service de métadonnées, blocage de cet accès depuis les applications, moindre privilège des rôles d'instance, allowlist SSRF, surveillance.
9. ⚠️ **Erreur fréquente.** Service de métadonnées en version permissive + rôles d'instance surprivilégiés.
10. 🎯 **À retenir.** Le service de métadonnées peut livrer des identifiants : le durcir et appliquer le moindre privilège aux rôles d'instance.


### Chapitre 224 — Privilege escalation cloud

1. **Définition.** Élévation de privilèges au sein d'un environnement cloud, souvent via l'IAM.
2. **Famille.** Privilege Escalation cloud.
3. **Principe.** En exploitant des permissions mal configurées (créer/modifier des politiques, assumer des rôles, modifier des identités), un accès limité peut être transformé en accès étendu, voire administrateur du tenant.
4. **Sous-types.** Via chaînes de rôles, via droits de modification de politiques, via secrets/métadonnées, via services privilégiés.
5. **Exemple conceptuel.** Un droit de modification de politique permet de s'octroyer des permissions supplémentaires.
6. **Impacts.** Contrôle étendu du tenant, accès aux données, persistance.
7. **Détection.** Modifications de politiques/rôles anormales, analyse des chemins d'élévation, journaux cloud, surveillance.
8. **Prévention.** Moindre privilège, suppression des permissions « dangereuses » de modification, analyse des chemins d'élévation, séparation, surveillance, MFA.
9. ⚠️ **Erreur fréquente.** Accorder des droits de modification d'IAM sans en mesurer le potentiel d'auto-élévation.
10. 🎯 **À retenir.** L'élévation cloud passe surtout par l'IAM : traquer et supprimer les chemins d'auto-élévation est la défense clé.


### Chapitre 225 — Lateral movement cloud

1. **Définition.** Déplacement entre ressources/comptes/services cloud après un accès initial.
2. **Famille.** Lateral Movement cloud.
3. **Principe.** L'attaquant rebondit via identités (rôles assumables), relations de confiance entre comptes, services interconnectés, secrets et métadonnées, jusqu'aux ressources de valeur.
4. **Sous-types.** Via rôles/identités, via relations inter-comptes, via services partagés, via secrets récupérés.
5. **Exemple conceptuel.** Des identifiants récupérés sur une ressource permettent d'accéder à d'autres services puis à un autre compte lié.
6. **Impacts.** Extension de la compromission, accès aux données, contrôle multi-comptes.
7. **Détection.** Usage anormal d'identités/rôles, accès inter-services/comptes inhabituels, journaux cloud, surveillance.
8. **Prévention.** Moindre privilège, segmentation des comptes/ressources, maîtrise des relations de confiance, gestion des secrets, surveillance, détection comportementale.
9. ⚠️ **Erreur fréquente.** Relations de confiance trop larges entre comptes/services, facilitant le rebond.
10. 🎯 **À retenir.** Le lateral movement cloud suit les identités et relations de confiance : les minimiser et surveiller leur usage le freine.


### Chapitre 226 — API security : principes

**Définition.** Pratiques sécurisant les API (chapitre 45), socle des applications modernes et des microservices.

**Principe.** Les API exposent directement données et fonctions. Leurs failles dominantes ne sont pas l'injection classique mais l'**autorisation** (par objet et par fonction), l'**exposition excessive de données**, et l'**absence de limites**. L'OWASP API Security Top 10 (2023) structure ces risques.

🧭 **Taxonomie** — Les chapitres 227–231 déclinent les principaux risques API ; BOLA/BFLA sont les équivalents API du Broken Access Control (Partie 6).

🎯 **À retenir** — La sécurité des API se joue surtout sur l'autorisation fine, la minimisation des données exposées et les limites de consommation.


### Chapitre 227 — BOLA (Broken Object Level Authorization)

1. **Définition.** Faille d'autorisation *au niveau objet* : accéder aux objets d'autrui faute de vérification de propriété (équivalent API de l'IDOR — chapitre 83).
2. **Famille.** API Security Top 10 (risque n°1). Contrôle d'accès cassé.
3. **Principe.** L'API identifie un objet par sa référence sans vérifier que l'appelant y a droit ; en changeant la référence, on accède à d'autres objets.
4. **Sous-types.** En lecture/écriture/suppression, sur identifiants séquentiels ou non.
5. **Exemple conceptuel.** Un endpoint renvoyant un objet par identifiant laisse accéder aux objets d'autres utilisateurs en variant l'identifiant.
6. **Impacts.** Fuite/altération massive de données, violation de confidentialité.
7. **Détection.** Accès à des objets hors périmètre, énumération d'identifiants, schémas anormaux, journaux API.
8. **Prévention.** **Vérification de propriété/autorisation par objet** côté serveur, deny by default, références liées à la session, tests d'autorisation.
9. ⚠️ **Erreur fréquente.** Se fier à l'imprévisibilité de l'identifiant plutôt qu'à un contrôle d'accès.
10. 🎯 **À retenir.** BOLA est le risque API n°1 : toujours vérifier que l'appelant a le droit sur *cet objet*.


### Chapitre 228 — BFLA (Broken Function Level Authorization)

1. **Définition.** Faille d'autorisation *au niveau fonction* : accéder à des opérations (souvent privilégiées/administratives) sans en avoir le droit.
2. **Famille.** API Security Top 10. Contrôle d'accès cassé (équivalent de l'élévation verticale).
3. **Principe.** Certaines fonctions (administration, actions sensibles) ne vérifient pas le rôle de l'appelant ; un utilisateur standard les invoque directement.
4. **Sous-types.** Accès à des endpoints d'administration, à des méthodes non autorisées, à des actions privilégiées.
5. **Exemple conceptuel.** Un endpoint d'administration est appelable par un compte standard faute de contrôle de rôle.
6. **Impacts.** Élévation de privilèges, actions non autorisées, compromission.
7. **Détection.** Appels à des fonctions privilégiées par des comptes non autorisés, journaux API, surveillance.
8. **Prévention.** **Contrôle d'autorisation par fonction** côté serveur, deny by default, séparation des rôles, tests d'autorisation, refus d'exposer des fonctions sans contrôle.
9. ⚠️ **Erreur fréquente.** Protéger les fonctions d'administration uniquement en les « cachant » de l'interface, sans contrôle serveur.
10. 🎯 **À retenir.** BFLA = fonctions privilégiées accessibles sans droit : vérifier le rôle pour *chaque* fonction, côté serveur.


### Chapitre 229 — Excessive data exposure

1. **Définition.** Une API renvoie *plus de données que nécessaire*, laissant au client le soin de filtrer (ce qui expose les champs sensibles).
2. **Famille.** API Security Top 10 (exposition de données).
3. **Principe.** L'API renvoie des objets complets (incluant des champs sensibles) en comptant sur le client pour n'afficher que l'utile ; l'attaquant lit la réponse brute.
4. **Sous-types.** Champs sensibles non filtrés, objets entiers renvoyés, données internes exposées.
5. **Exemple conceptuel.** Une réponse destinée à afficher un nom renvoie aussi des champs sensibles non utilisés par l'interface.
6. **Impacts.** Fuite de données sensibles, atteinte à la confidentialité.
7. **Détection.** Analyse des réponses (champs superflus/sensibles), revue de schéma, tests.
8. **Prévention.** **Filtrer côté serveur** (ne renvoyer que les champs nécessaires), schémas de réponse explicites, minimisation, revue, classification.
9. ⚠️ **Erreur fréquente.** Compter sur le client (interface) pour masquer des données pourtant transmises.
10. 🎯 **À retenir.** Ne jamais déléguer le filtrage au client : l'API ne doit renvoyer que les données strictement nécessaires.


### Chapitre 230 — Unrestricted resource consumption

1. **Définition.** Absence de limites sur la consommation de ressources via l'API, permettant l'épuisement ou la surfacturation.
2. **Famille.** API Security Top 10 (lié au rate limiting — chapitre 79).
3. **Principe.** Sans quotas/limites, l'attaquant déclenche des opérations massives ou coûteuses (requêtes, calculs, stockage), provoquant déni de service ou explosion des coûts cloud.
4. **Sous-types.** Volume de requêtes, opérations coûteuses, requêtes profondes (GraphQL — chapitre 126), consommation de stockage/calcul.
5. **Exemple conceptuel.** Des requêtes coûteuses répétées épuisent les ressources ou génèrent des coûts cloud importants.
6. **Impacts.** Déni de service, surcoûts, dégradation.
7. **Détection.** Volumes/coûts anormaux, requêtes coûteuses répétées, surveillance, alertes de coût.
8. **Prévention.** **Limitation de débit et quotas**, plafonds de complexité/taille, pagination, time-outs, contrôles de coût cloud, détection d'anomalies.
9. ⚠️ **Erreur fréquente.** Exposer des opérations coûteuses sans aucun plafond ni quota.
10. 🎯 **À retenir.** Sans limites, une API devient un levier de DoS et de surcoût : quotas, plafonds et contrôles de coût sont indispensables.


### Chapitre 231 — Unsafe consumption of APIs

1. **Définition.** Faire *trop confiance* aux données reçues d'API tierces/en amont, sans les valider.
2. **Famille.** API Security Top 10 / rupture de frontière de confiance (chapitre 80).
3. **Principe.** En consommant une API tierce, on suppose ses données sûres ; si cette API est compromise ou renvoie des données malveillantes, l'application aval les traite en confiance (injection, corruption).
4. **Sous-types.** Confiance excessive en réponses tierces, suivi aveugle de redirections, absence de validation des données amont.
5. **Exemple conceptuel.** Une application traite sans validation les données d'une API partenaire, propageant un contenu malveillant si celle-ci est compromise.
6. **Impacts.** Injection, corruption de données, propagation de compromission via la chaîne d'API.
7. **Détection.** Anomalies dans les données amont, comportements inattendus, surveillance des intégrations.
8. **Prévention.** **Valider et assainir** les données reçues des API tierces, traiter l'amont comme non fiable, time-outs/contrôles, surveillance des intégrations, segmentation.
9. ⚠️ **Erreur fréquente.** Considérer une API « partenaire » comme intrinsèquement fiable et ne pas valider ses réponses.
10. 🎯 **À retenir.** Les données d'une API tierce franchissent une frontière de confiance : les valider comme toute entrée non fiable.


### Chapitre 232 — Kubernetes RBAC abuse

1. **Définition.** Abus des droits (RBAC) au sein d'un cluster Kubernetes pour élever ses privilèges ou accéder à des ressources.
2. **Famille.** Conteneurs/orchestration (chapitre 47) / autorisation.
3. **Principe.** Le RBAC Kubernetes accorde des droits sur les ressources du cluster ; des permissions trop larges (créer des pods, lire des secrets, exécuter dans des pods) permettent l'élévation ou la prise de contrôle du cluster.
4. **Sous-types.** Droits excessifs sur pods/secrets/nœuds, comptes de service surprivilégiés, accès à l'API server.
5. **Exemple conceptuel.** Un compte de service au RBAC trop large peut lire des secrets ou créer des charges privilégiées.
6. **Impacts.** Élévation, accès aux secrets, prise de contrôle du cluster, mouvement latéral.
7. **Détection.** Analyse du RBAC (permissions effectives), actions anormales sur l'API server, journaux d'audit Kubernetes.
8. **Prévention.** **Moindre privilège RBAC**, comptes de service minimaux, restriction de l'accès à l'API server, audit, séparation, surveillance.
9. ⚠️ **Erreur fréquente.** Comptes de service par défaut surprivilégiés, RBAC permissif jamais audité.
10. 🎯 **À retenir.** Le RBAC Kubernetes est le contrôle d'accès du cluster : moindre privilège et audit des permissions effectives sont essentiels.


### Chapitre 233 — Container escape

1. **Définition.** Évasion d'un conteneur vers l'hôte (ou vers d'autres conteneurs), brisant l'isolation.
2. **Famille.** Conteneurs (chapitre 47) / élévation.
3. **Principe.** Un conteneur mal isolé (privilégié, capacités excessives, montages sensibles, vulnérabilité du runtime/noyau) permet à l'attaquant de « sortir » vers l'hôte, compromettant potentiellement toutes les charges hébergées.
4. **Sous-types.** Via conteneur privilégié, capacités/montages dangereux, vulnérabilité du runtime ou du noyau.
5. **Exemple conceptuel.** Un conteneur disposant de privilèges/montages excessifs accède à l'hôte sous-jacent.
6. **Impacts.** Compromission de l'hôte et des autres conteneurs, élévation, mouvement latéral.
7. **Détection.** Comportements d'évasion, accès anormaux à l'hôte, EDR/runtime security, audit.
8. **Prévention.** **Conteneurs non privilégiés**, capacités minimales, pas de montages sensibles, security contexts/policies, isolation renforcée, runtime à jour, durcissement du noyau, admission control.
9. ⚠️ **Erreur fréquente.** Exécuter des conteneurs en mode privilégié ou avec des montages hôte sensibles.
10. 🎯 **À retenir.** Un conteneur n'est pas une frontière de sécurité parfaite : minimiser privilèges/capacités/montages évite l'évasion vers l'hôte.


### Chapitre 234 — Image vulnérable

1. **Définition.** Image de conteneur contenant des composants vulnérables ou des configurations dangereuses.
2. **Famille.** Conteneurs / dépendances vulnérables (chapitre 71).
3. **Principe.** Les images embarquent un système et des dépendances ; si ceux-ci sont obsolètes/vulnérables (ou contiennent des secrets), chaque conteneur lancé hérite de ces faiblesses.
4. **Sous-types.** Dépendances vulnérables, image obsolète, secrets embarqués, configuration non durcie.
5. **Exemple conceptuel.** Une image basée sur un système non patché déploie partout les mêmes vulnérabilités.
6. **Impacts.** Exploitation à l'échelle des déploiements, fuite de secrets, point d'entrée.
7. **Détection.** **Scan d'images** (vulnérabilités, secrets), inventaire, surveillance.
8. **Prévention.** Images **minimales** et à jour, scan en CI et au registre, SBOM, base d'images de confiance, durcissement, pas de secrets en image, mises à jour régulières.
9. ⚠️ **Erreur fréquente.** Déployer des images jamais re-scannées ni mises à jour (vulnérabilités héritées en masse).
10. 🎯 **À retenir.** Une image vulnérable se réplique à chaque conteneur : images minimales, scannées et à jour, sans secrets.


### Chapitre 235 — Registre exposé

1. **Définition.** Registre d'images de conteneurs accessible/modifiable indûment.
2. **Famille.** Conteneurs / supply chain.
3. **Principe.** Un registre exposé permet de *lire* des images (fuite de code/secrets) ou d'y *pousser* des images malveillantes ensuite déployées en confiance (empoisonnement de la chaîne).
4. **Sous-types.** Lecture publique (fuite), écriture non contrôlée (empoisonnement), absence de contrôle d'intégrité.
5. **Exemple conceptuel.** Un registre accessible en écriture permet de remplacer une image légitime par une version piégée.
6. **Impacts.** Fuite de code/secrets, déploiement d'images malveillantes, compromission de la supply chain.
7. **Détection.** Accès/poussées anormaux, modifications d'images, surveillance du registre, vérification d'intégrité.
8. **Prévention.** Registres **privés** et authentifiés, contrôle d'accès strict, **signature et vérification d'images**, scan, journalisation, moindre privilège.
9. ⚠️ **Erreur fréquente.** Registre accessible largement, sans signature ni vérification des images déployées.
10. 🎯 **À retenir.** Un registre exposé empoisonne la chaîne : accès strict + signature/vérification des images sont indispensables.


### Chapitre 236 — CI/CD compromise

1. **Définition.** Compromission de la chaîne d'intégration/déploiement continus (chapitre 48).
2. **Famille.** Supply chain logicielle (à fort effet de levier).
3. **Principe.** La CI/CD a des droits puissants (déployer en production) et manipule code et secrets ; la compromettre permet d'injecter du code malveillant dans *tout ce qui est déployé*, « légitimement ».
4. **Sous-types.** Vol de secrets de pipeline, pipeline poisoning (chapitre 237), abus de tokens CI, compromission du build (chapitre 241).
5. **Exemple conceptuel.** Un accès au système de CI/CD permet d'altérer le processus de build pour insérer une charge dans les artefacts produits.
6. **Impacts.** Distribution massive de code malveillant, accès production, compromission profonde et de confiance.
7. **Détection.** Modifications anormales des pipelines/configurations, usage anormal de secrets/tokens, intégrité des artefacts, surveillance.
8. **Prévention.** **Moindre privilège** des pipelines, gestion des secrets dédiée, isolation des runners, revue de code obligatoire, **signature/provenance** (SLSA), SBOM, journalisation.
9. ⚠️ **Erreur fréquente.** Pipelines aux droits de production illimités, secrets en clair, runners non isolés.
10. 🎯 **À retenir.** Compromettre la CI/CD = empoisonner la source : moindre privilège, isolation, secrets gérés et provenance/signature sont critiques.


### Chapitre 237 — Pipeline poisoning

1. **Définition.** Injection de code/étapes malveillants *dans le processus de build* lui-même.
2. **Famille.** Supply chain / CI/CD.
3. **Principe.** En modifiant la configuration de pipeline, des scripts de build, ou en injectant via une dépendance/entrée de build, l'attaquant fait produire des artefacts piégés tout en gardant l'apparence d'un build légitime.
4. **Sous-types.** Modification de la définition de pipeline, injection via dépendances de build, abus d'entrées contrôlables du pipeline (poisoned pipeline execution).
5. **Exemple conceptuel.** Une étape ajoutée au pipeline insère une charge dans l'artefact final, sans alerter.
6. **Impacts.** Artefacts compromis distribués, accès, persistance, compromission de confiance.
7. **Détection.** Modifications de pipeline/scripts inattendues, écarts d'intégrité des artefacts, surveillance, revue.
8. **Prévention.** Contrôle/validation des définitions de pipeline, isolation des étapes, **provenance/signature** (SLSA), revue obligatoire, moindre privilège, builds reproductibles.
9. ⚠️ **Erreur fréquente.** Laisser modifier les définitions de pipeline sans revue ni contrôle d'intégrité des artefacts.
10. 🎯 **À retenir.** Le pipeline poisoning insère le mal dans le build : revue, isolation et provenance/signature des artefacts sont les parades.


### Chapitre 238 — Dependency confusion

1. **Définition.** Attaque où un paquet *public* malveillant, portant le nom d'un paquet *interne*, est récupéré à la place de ce dernier par le gestionnaire de dépendances.
2. **Famille.** Supply chain logicielle (chapitre 81).
3. **Principe.** Si le gestionnaire de paquets privilégie (ou peut atteindre) un dépôt public, un attaquant publie un paquet public au même nom qu'un paquet interne, avec une version supérieure ; le build récupère le paquet malveillant.
4. **Sous-types.** Selon l'écosystème de paquets et la configuration des dépôts.
5. **Exemple conceptuel.** Un nom de paquet interne, publié publiquement par un attaquant avec une version élevée, est résolu à la place du paquet interne légitime.
6. **Impacts.** Exécution de code malveillant dans le build/les déploiements, compromission.
7. **Détection.** Résolution de paquets depuis des sources inattendues, écarts de version/source, surveillance des dépendances.
8. **Prévention.** **Dépôts internes prioritaires/exclusifs** (scoping, namespaces réservés), verrouillage des sources et versions (lockfiles), vérification d'intégrité, allowlist de paquets, SBOM.
9. ⚠️ **Erreur fréquente.** Configuration de paquets autorisant la résolution publique pour des noms internes.
10. 🎯 **À retenir.** La dependency confusion exploite la résolution de noms : prioriser/réserver les dépôts internes et verrouiller sources et versions.


### Chapitre 239 — Typosquatting package

1. **Définition.** Publication de paquets malveillants aux noms proches de paquets populaires (fautes de frappe), pour piéger les développeurs.
2. **Famille.** Supply chain logicielle.
3. **Principe.** L'attaquant mise sur l'erreur de saisie ou la confusion ; un développeur installe par mégarde le paquet piégé, dont le nom imite un paquet légitime.
4. **Sous-types.** Variantes de nom (fautes, tirets, ordre), imitation de paquets populaires.
5. **Exemple conceptuel.** Un paquet au nom presque identique à une bibliothèque connue contient une charge malveillante.
6. **Impacts.** Exécution de code malveillant à l'installation/au build, compromission.
7. **Détection.** Dépendances aux noms suspects, écarts par rapport aux paquets officiels, scan, surveillance.
8. **Prévention.** Allowlist de paquets, vérification des noms officiels, verrouillage (lockfiles), SBOM, dépôts internes filtrés, revue des dépendances.
9. ⚠️ **Erreur fréquente.** Installer un paquet sans vérifier son nom/source exacts.
10. 🎯 **À retenir.** Le typosquatting piège par la ressemblance des noms : vérifier les sources officielles et verrouiller les dépendances.


### Chapitre 240 — Malicious package

1. **Définition.** Paquet/dépendance intentionnellement malveillant (au-delà du typosquatting/dependency confusion), incluant les paquets légitimes *détournés*.
2. **Famille.** Supply chain logicielle.
3. **Principe.** Un paquet contient du code malveillant dès l'origine, ou un paquet légitime est compromis (compte mainteneur piraté, mise à jour piégée), distribuant le mal à tous ses utilisateurs.
4. **Sous-types.** Paquet malveillant dès l'origine, paquet légitime compromis (mainteneur/mise à jour), charge déclenchée à l'installation ou à l'exécution.
5. **Exemple conceptuel.** Une mise à jour d'une bibliothèque répandue, compromise à la source, distribue une charge à ses utilisateurs.
6. **Impacts.** Compromission massive et de confiance, exécution de code, exfiltration.
7. **Détection.** Comportements anormaux de dépendances, analyse de composition (SCA), surveillance des mises à jour, intégrité.
8. **Prévention.** SCA, **SBOM**, verrouillage et revue des mises à jour, vérification d'intégrité/signature, dépôts internes filtrés, minimisation des dépendances, surveillance des avis.
9. ⚠️ **Erreur fréquente.** Mettre à jour automatiquement des dépendances sans revue ni contrôle d'intégrité.
10. 🎯 **À retenir.** Un paquet de confiance peut devenir malveillant : SBOM, SCA, verrouillage et revue des mises à jour réduisent le risque.


### Chapitre 241 — Build system compromise

1. **Définition.** Compromission directe du *système de build* (serveurs, outils, environnement) qui produit les artefacts.
2. **Famille.** Supply chain logicielle (la plus profonde).
3. **Principe.** En contrôlant le système qui compile/assemble, l'attaquant peut altérer les artefacts produits *même si* le code source est sain — d'où la nécessité de garantir l'intégrité et la provenance du build.
4. **Sous-types.** Compromission des serveurs de build, des outils/dépendances de build, de l'environnement d'exécution.
5. **Exemple conceptuel.** Un système de build compromis insère une modification dans l'artefact final, indépendamment du code source.
6. **Impacts.** Artefacts piégés et signés « légitimement », compromission massive et difficile à détecter.
7. **Détection.** Écarts d'intégrité, builds non reproductibles, anomalies de l'environnement de build, surveillance.
8. **Prévention.** **Builds isolés/éphémères et reproductibles**, **provenance** (SLSA), intégrité de l'environnement, moindre privilège, durcissement, journalisation, vérification des artefacts.
9. ⚠️ **Erreur fréquente.** Faire confiance à l'artefact « parce que le code source est revu », sans garantir l'intégrité du build.
10. 🎯 **À retenir.** Un build compromis produit du mal à partir d'un code sain : builds reproductibles et provenance (SLSA) sont la garantie.


### Chapitre 242 — Signature et intégrité logicielle

**Définition.** Mécanismes garantissant qu'un artefact (paquet, image, binaire) provient bien de sa source légitime et n'a pas été altéré.

**Principe.** La **signature** (cryptographique) atteste l'origine ; la **vérification** côté consommateur garantit l'intégrité. La **provenance** (qui a produit quoi, comment, à partir de quelles entrées — formalisée par SLSA) étend cette garantie à toute la chaîne. C'est la défense de fond contre la supply chain : ne déployer/exécuter que ce qui est signé et vérifié.

🧭 **Taxonomie** — Antidote transversal des chapitres 235–241 ; relie intégrité (chapitre 81), CI/CD et déploiement.

⚠️ **Erreur fréquente** — Signer sans *vérifier* à la consommation (la signature seule ne protège pas si personne ne contrôle).

🎯 **À retenir** — Signer *et vérifier* les artefacts, et tracer leur provenance (SLSA), est la parade structurante contre la compromission de la supply chain.


### Chapitre 243 — SBOM (Software Bill of Materials)

**Définition.** Inventaire détaillé des composants logiciels (dépendances, versions, origines) d'une application — sa « liste d'ingrédients ».

**Principe.** On ne peut sécuriser que ce qu'on connaît (chapitre 33). Le SBOM permet, lorsqu'une vulnérabilité (ou un paquet malveillant) est révélé, de savoir *immédiatement* si on est concerné et où. Il est le socle de la gestion des dépendances (chapitre 71), de la SCA et de la réponse aux incidents supply chain.

🔧 **Exemple concret** — À l'annonce d'une vulnérabilité critique dans une bibliothèque répandue, le SBOM indique en minutes quels systèmes l'embarquent, au lieu de jours de recherche.

🧭 **Taxonomie** — Inventaire au niveau logiciel ; pendant de la gestion des actifs (chapitre 33) côté code.

🎯 **À retenir** — Le SBOM transforme « sommes-nous touchés ? » d'une enquête longue en une requête immédiate : c'est un prérequis de la sécurité de la supply chain.


### Chapitre 244 — Secrets management

**Définition.** Gestion centralisée et sécurisée des secrets (mots de passe, clés, jetons, certificats) tout au long de leur cycle de vie.

**Principe.** Antidote transversal à l'exposition de secrets (chapitres 77, 221, 222). Un gestionnaire de secrets (coffre-fort) : stocke les secrets chiffrés hors du code, contrôle/audite les accès, distribue les secrets de façon dynamique (idéalement à durée de vie courte), assure la **rotation** et la **révocation** rapides. Couplé au secrets scanning (détecter les fuites) et au moindre privilège.

🧭 **Taxonomie** — Défense centrale du cloud, de la CI/CD et des conteneurs ; relie identité, configuration et supply chain.

⚠️ **Erreur fréquente** — Déployer un coffre à secrets tout en laissant subsister des secrets en dur dans le code/l'IaC.

🎯 **À retenir** — Centraliser, chiffrer, faire tourner et auditer les secrets (et scanner les fuites) coupe l'un des chemins d'attaque les plus directs.

---

> **Fin du Volume 7/8.**
>
> Vous savez sécuriser les surfaces modernes : cloud (responsabilité partagée, IAM, configuration, secrets, métadonnées, élévation/lateral movement), API (autorisation par objet/fonction, minimisation des données, limites, consommation sûre), conteneurs/Kubernetes (RBAC, évasion, images, registres), et supply chain (CI/CD, pipeline poisoning, dependency confusion, typosquatting, paquets/build compromis, signature/provenance, SBOM, gestion des secrets).
>
> **Suite — Volume 8 (final) : Parties 11 à 13 + Annexes** — Détection/SOC/réponse à incident ; taxonomie des défenses ; synthèse transversale (classer une attaque inconnue, relier attaque↔vulnérabilité↔contrôle↔détection, prioriser, carte mentale, erreurs de raisonnement, glossaire) ; et les annexes (glossaire, tableaux de correspondance, fiches réflexes, métiers cyber, méthode d'apprentissage légal, bibliographie).


---


## Taxonomie de la cybersécurité — Volume 8/8 (final)

> Parties 11 à 13 + Annexes
>
> Ce volume ferme la boucle du fil rouge : après *comprendre, classer, relier, défendre*, on traite **répondre** (Partie 11), on consolide la **taxonomie des défenses** (Partie 12), puis on apprend à **raisonner** transversalement (Partie 13). Les annexes fournissent les outils de référence (glossaire, tableaux de correspondance, fiches réflexes, métiers, méthode d'apprentissage légal, bibliographie).

---
