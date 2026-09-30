---
title: Partie 5 — Taxonomie des vulnérabilités
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

> Une **vulnérabilité** est une faiblesse exploitable. Cette partie classe les vulnérabilités par *nature de la faiblesse* (et non par surface). C'est le vocabulaire structuré que **CWE** formalise. Comprendre ces familles permet de prédire les attaques et de choisir les contrôles. Référence utile : **OWASP ASVS** pour vérifier la sécurité applicative.


### Chapitre 62 — Défaut d'authentification

**Définition.** Faiblesse dans la *vérification de l'identité* : il est possible de se faire passer pour un autre, ou de contourner la preuve d'identité.

**Famille / catégorie.** Authentification cassée (OWASP « Identification and Authentication Failures » ; CWE-287 et apparentés).

**Mécanisme.** Mots de passe faibles ou par défaut, absence de MFA, gestion de session défaillante, énumération de comptes, récupération de mot de passe non sécurisée, jetons prévisibles.

**Impacts.** Usurpation d'identité, prise de contrôle de comptes, accès non autorisé.

**Signaux de détection.** Pics d'échecs de connexion (brute force, spraying), connexions depuis lieux/appareils anormaux, multiples comptes ciblés.

🛡️ **Défense** — MFA (idéalement résistant au phishing), politiques de mots de passe modernes, anti-brute-force/limitation, gestion sécurisée de session, messages d'erreur non révélateurs.

⚠️ **Erreur fréquente** — Confondre authentification (qui ?) et autorisation (quels droits ?). Ce chapitre concerne uniquement la *preuve d'identité*.

🎯 **À retenir** — Tout ce qui permet de *prouver faussement qui l'on est* relève du défaut d'authentification. MFA est la parade reine.


### Chapitre 63 — Défaut d'autorisation

**Définition.** Faiblesse dans la *vérification des droits* : un utilisateur authentifié accède à des ressources ou fonctions qui ne lui sont pas destinées.

**Famille / catégorie.** Contrôle d'accès cassé (OWASP « Broken Access Control » — n°1 du Top 10 ; CWE-285, CWE-639, CWE-862).

**Mécanisme.** Contrôles d'accès absents, incohérents, ou réalisés *côté client*, références d'objets non vérifiées (IDOR/BOLA), élévation de privilèges, fonctions d'administration accessibles sans contrôle.

**Impacts.** Accès et modification de données d'autrui, élévation de privilèges, contournement de la logique métier.

**Signaux de détection.** Accès à des identifiants d'objets hors périmètre de l'utilisateur, appels à des endpoints privilégiés par des comptes standard, énumération d'identifiants.

🛡️ **Défense** — Contrôle d'accès *systématique côté serveur*, « deny by default », vérification de propriété de chaque objet, RBAC/ABAC, tests d'autorisation.

🎯 **À retenir** — L'autorisation cassée est la vulnérabilité web n°1. Toujours vérifier *les droits*, à chaque accès, côté serveur — l'authentification ne suffit pas.


### Chapitre 64 — Injection

**Définition.** Faiblesse où une *entrée non fiable* est interprétée comme *du code ou une commande* par un interpréteur incapable de distinguer données et instructions.

**Famille / catégorie.** Injection (OWASP Top 10 ; CWE-74 et enfants : CWE-89 SQLi, CWE-79 XSS, CWE-78 command injection…).

**Mécanisme.** L'application mélange données utilisateur et structure de la requête/commande. L'interpréteur (SQL, shell, navigateur, LDAP, moteur de templates) exécute la partie injectée.

**Sous-types (détaillés en Partie 6).** SQLi, XSS, command injection, LDAP injection, XPath injection, SSTI, NoSQL injection, CRLF/header injection.

**Impacts.** Lecture/modification de données, exécution de code, contournement d'authentification, compromission du serveur.

🛡️ **Défense** — Séparer code et données : requêtes paramétrées/préparées, API sûres, encodage contextuel des sorties, validation par allowlist, moindre privilège de l'interpréteur.

🧭 **Taxonomie** — *La* méta-famille applicative : un seul principe (« données traitées comme du code ») génère de nombreux sous-types selon l'interpréteur.

🎯 **À retenir** — Toute injection a la même racine : un interpréteur confond données et instructions. La parade universelle est de *séparer* les deux (paramétrage + encodage).


### Chapitre 65 — Mauvaise validation d'entrée

**Définition.** L'application accepte des entrées sans vérifier qu'elles sont conformes à ce qui est attendu (type, format, longueur, plage, jeu de caractères).

**Famille / catégorie.** Validation d'entrée incorrecte (CWE-20).

**Mécanisme.** Faute amont qui *alimente* de nombreuses autres failles (injection, débordement, logique métier). Distinguer validation (l'entrée est-elle bien formée ?) et encodage de sortie (l'afficher sans danger).

**Impacts.** Variés : injection, corruption de données, plantage, contournement de règles.

🛡️ **Défense** — Validation stricte côté serveur par **allowlist** (ce qui est autorisé) plutôt que blocklist (ce qui est interdit), contrôles de type/format/longueur, rejet par défaut.

⚠️ **Erreur fréquente** — Valider uniquement côté client (contournable) ou se fier à une blocklist (toujours incomplète).

🎯 **À retenir** — La validation par allowlist côté serveur est une défense en profondeur qui coupe la racine de nombreuses attaques.


### Chapitre 66 — Mauvaise gestion de session

**Définition.** Faiblesse dans la création, la protection ou l'invalidation des sessions, permettant de voler ou détourner la session d'un utilisateur.

**Famille / catégorie.** Gestion de session défaillante (CWE-384 fixation, CWE-613 expiration).

**Mécanisme.** Identifiants de session prévisibles, non régénérés après connexion (fixation), transmis sans chiffrement, sans expiration, ou stockés de façon vulnérable au vol (XSS volant les cookies).

**Impacts.** Détournement de session (session hijacking), usurpation, accès persistant.

🛡️ **Défense** — Jetons aléatoires forts, régénération à l'authentification, cookies `HttpOnly`/`Secure`/`SameSite`, expiration et invalidation à la déconnexion, transport chiffré (TLS).

🧭 **Taxonomie** — À l'intersection de l'authentification (chapitre 62) et des attaques web (CSRF, XSS, fixation — Partie 6).

🎯 **À retenir** — Une session mal gérée annule une authentification forte : protéger le jeton est aussi important que vérifier l'identité.


### Chapitre 67 — Mauvaise configuration

**Définition.** Le système est *fonctionnel mais mal réglé* du point de vue sécurité : options par défaut dangereuses, services inutiles, permissions trop larges, comptes par défaut.

**Famille / catégorie.** Security Misconfiguration (OWASP Top 10 ; CWE-16, CWE-732).

**Mécanisme.** Pas une faille de code, mais un *réglage*. Très fréquent dans le cloud (buckets publics), les bases de données (sans mot de passe), les en-têtes web manquants, les pages d'administration exposées.

**Impacts.** Exposition de données, accès non autorisé, point d'entrée facile.

🛡️ **Défense** — Durcissement selon des référentiels (CIS), secure by default, suppression des comptes/services par défaut, gestion de configuration (IaC, baseline), CSPM dans le cloud, revues régulières.

🧭 **Taxonomie** — Famille dominante dans le cloud (Partie 10) ; cousine du défaut de durcissement (chapitre 21).

🎯 **À retenir** — La majorité des incidents cloud viennent d'une *configuration*, pas d'une *vulnérabilité logicielle*. Le durcissement par défaut est la parade.


### Chapitre 68 — Chiffrement faible ou absent

**Définition.** Données sensibles non chiffrées, ou protégées par une cryptographie obsolète/mal implémentée.

**Famille / catégorie.** Cryptographic Failures (OWASP Top 10 ; CWE-327 algorithme faible, CWE-311 absence de chiffrement).

**Mécanisme.** Pas de chiffrement en transit/au repos, algorithmes cassés (MD5, SHA1, DES), clés mal gérées, mauvais modes, hachage de mots de passe inadéquat, certificats mal validés.

**Impacts.** Interception et lecture de données, vol d'identifiants, atteinte à la confidentialité et à l'intégrité.

🛡️ **Défense** — TLS récent en transit, chiffrement au repos, algorithmes éprouvés, hachage de mots de passe adapté (Argon2/bcrypt/scrypt), gestion de clés rigoureuse (rotation, séparation), validation stricte des certificats.

⚠️ **Erreur fréquente** — « Chiffrer » avec un algorithme obsolète ou des clés mal gérées : faux sentiment de sécurité. Et ne jamais inventer sa propre crypto.

🎯 **À retenir** — Le chiffrement protège la donnée même en cas de vol — à condition d'algorithmes modernes et d'une *gestion de clés* sérieuse.


### Chapitre 69 — Fuite d'information

**Définition.** Le système révèle, involontairement, des informations utiles à un attaquant (détails techniques, données internes, secrets).

**Famille / catégorie.** Information Exposure (CWE-200 et apparentés).

**Mécanisme.** Messages d'erreur verbeux (traces de pile, versions, requêtes SQL), métadonnées, commentaires de code, endpoints de debug, en-têtes révélateurs, énumération de comptes.

**Impacts.** Facilite la reconnaissance et le ciblage ; parfois exposition directe de données ou de secrets.

🛡️ **Défense** — Messages d'erreur génériques, désactivation du mode debug en production, suppression des métadonnées/commentaires sensibles, en-têtes minimaux, réponses uniformes (anti-énumération).

🧭 **Taxonomie** — Souvent une faille *préparatoire* (aide la reconnaissance), parfois un impact en soi (exposition de secrets — chapitre 77).

🎯 **À retenir** — Chaque détail révélé est un cadeau à l'attaquant : la discrétion (erreurs génériques, pas de debug en prod) est une défense.


### Chapitre 70 — Vulnérabilités mémoire

**Définition.** Faiblesses dans la gestion de la mémoire des programmes (souvent en langages bas niveau comme C/C++) permettant de corrompre l'exécution.

**Famille / catégorie.** Memory safety (CWE-119 famille : CWE-787 écriture hors limites, CWE-416 use-after-free, CWE-476 déréférencement null).

**Mécanisme.** Débordement de tampon (buffer overflow), use-after-free, lecture/écriture hors limites, dépassement d'entier — pouvant mener à l'exécution de code arbitraire ou au plantage.

**Impacts.** Exécution de code (RCE), élévation de privilèges, déni de service, fuite mémoire de données.

🛡️ **Défense** — Langages à sûreté mémoire (Rust, Go, langages managés), protections compilateur/OS (ASLR, DEP, stack canaries), validation des tailles, fuzzing, revues de code, mises à jour.

🧭 **Taxonomie** — Famille reine des vulnérabilités *systèmes/binaires* (historiquement la base de l'exploitation). Concerne surtout logiciels natifs, OS, firmware.

🎯 **À retenir** — Les bugs mémoire restent une source majeure de RCE ; la tendance de fond est l'adoption de langages à *sûreté mémoire*.


### Chapitre 71 — Dépendances vulnérables

**Définition.** L'application intègre des composants tiers (bibliothèques, frameworks) qui contiennent des vulnérabilités connues.

**Famille / catégorie.** Vulnerable and Outdated Components (OWASP Top 10 ; CWE-1104, CWE-1395).

**Mécanisme.** Le code moderne est fait à 80–90 % de dépendances. Une faille dans l'une d'elles (souvent largement répandue) devient une faille de votre application, sans que vous ayez écrit le code fautif.

**Impacts.** Hérités de la dépendance : RCE, fuite, déni de service ; effet de masse (une CVE touche des millions d'applications).

🛡️ **Défense** — Inventaire des dépendances (**SBOM**), analyse de composition logicielle (**SCA**), mises à jour régulières, suivi des CVE, minimisation des dépendances, vérification d'intégrité.

🧭 **Taxonomie** — Pont vers la supply chain logicielle (chapitre 81, Partie 10). Distincte des dépendances *malveillantes* (typosquatting), qui relèvent de la supply chain offensive.

🎯 **À retenir** — Vous héritez des failles de tout ce que vous importez : connaître (SBOM) et surveiller (SCA) ses dépendances est indispensable.


### Chapitre 72 — Logique métier

**Définition.** Faiblesse non pas technique mais *fonctionnelle* : l'application fonctionne « comme codée » mais sa logique permet un abus que le concepteur n'avait pas prévu.

**Famille / catégorie.** Business Logic Flaws (CWE-840).

**Mécanisme.** Détournement des règles métier : enchaîner des étapes dans le désordre, manipuler des quantités/prix négatifs, abuser de remises cumulables, contourner des limites, exploiter des conditions de course métier.

**Impacts.** Fraude, perte financière, contournement de contrôles, abus de service — souvent invisibles aux scanners (rien n'est « techniquement » cassé).

🔧 **Exemple concret** — Appliquer un même bon de réduction des milliers de fois, ou commander une quantité négative pour se faire créditer.

🛡️ **Défense** — Modélisation de menace métier, validation des règles côté serveur, contrôles de cohérence, tests fonctionnels orientés abus, limites et plafonds, supervision des comportements anormaux.

⚠️ **Erreur fréquente** — Croire qu'un scanner automatique détecte ces failles : elles exigent une *compréhension du métier*, donc un test humain.

🎯 **À retenir** — La logique métier cassée n'est pas un bug technique mais un *abus de fonctionnement* : seuls la réflexion métier et le test humain la révèlent.


### Chapitre 73 — Race condition

**Définition.** Faiblesse où le résultat dépend de l'*ordre/temporalité* d'opérations concurrentes, exploitable en agissant dans une fenêtre temporelle critique.

**Famille / catégorie.** Concurrency / TOCTOU (CWE-362, CWE-367 « Time-of-check to time-of-use »).

**Mécanisme.** Entre le moment où une condition est *vérifiée* et celui où elle est *utilisée*, l'attaquant modifie l'état. Ou : des requêtes simultanées contournent une limite censée être unique.

**Impacts.** Double dépense, contournement de limites/quotas, élévation de privilèges, corruption de données.

🔧 **Exemple concret** — Lancer simultanément plusieurs retraits pour dépasser un solde censé être vérifié une seule fois (variante métier de la race condition).

🛡️ **Défense** — Opérations atomiques, verrous, transactions, contrôles d'idempotence, vérification *au moment de l'usage*, limitation de la concurrence.

🧭 **Taxonomie** — Recoupe la logique métier (chapitre 72) quand elle est exploitée fonctionnellement ; relève du système quand elle est bas niveau (TOCTOU).

🎯 **À retenir** — Une vérification suivie d'une action non atomique ouvre une fenêtre exploitable : l'atomicité est la parade.


### Chapitre 74 — Désérialisation

**Définition.** Faiblesse où des données sérialisées *non fiables* sont reconstruites en objets par l'application, permettant d'altérer l'exécution.

**Famille / catégorie.** Insecure Deserialization (CWE-502 ; OWASP « Software and Data Integrity Failures »).

**Mécanisme.** La désérialisation peut instancier des objets et déclencher du code (chaînes de gadgets), surtout dans les formats binaires riches. Une charge sérialisée malveillante peut alors mener à l'exécution de code.

**Impacts.** Exécution de code à distance (souvent), élévation de privilèges, manipulation d'objets, déni de service.

🛡️ **Défense** — Éviter de désérialiser des données non fiables, préférer des formats de données simples (JSON sans types), signer/chiffrer les données sérialisées, allowlist de classes, isolation.

🧭 **Taxonomie** — Famille « intégrité logicielle » ; détaillée côté attaque en Partie 6 (chapitre 114).

🎯 **À retenir** — Désérialiser une entrée non fiable revient souvent à exécuter du code étranger : ne jamais désérialiser sans contrôle d'intégrité et de type.


### Chapitre 75 — Erreurs de parsing

**Définition.** Faiblesses dans l'*analyse* de formats de données (XML, JSON, fichiers, URL, protocoles) : ambiguïtés, incohérences entre analyseurs, comportements inattendus.

**Famille / catégorie.** Improper Input Parsing (familles CWE liées à l'interprétation des entrées).

**Mécanisme.** Différences d'interprétation entre deux composants (parser differential), entités externes (XXE), expansion incontrôlée (« billion laughs »), confusion d'encodage, désynchronisation de protocole (request smuggling).

**Impacts.** Contournement de contrôles, déni de service, lecture de fichiers (XXE), désynchronisation HTTP, injection.

🛡️ **Défense** — Analyseurs robustes et à jour, désactivation des fonctionnalités dangereuses (entités externes XML), limites de taille/profondeur, normalisation des entrées, cohérence des composants en chaîne.

🧭 **Taxonomie** — Sous-tend XXE, request smuggling, certaines injections (Partie 6). Racine : *« deux composants ne lisent pas la même chose de la même façon »*.

🎯 **À retenir** — Quand deux analyseurs interprètent différemment la même donnée, l'écart devient exploitable. Normaliser et durcir les parsers ferme cette porte.


### Chapitre 76 — Permissions excessives

**Définition.** Comptes, fichiers, services ou rôles disposant de *plus de droits que nécessaire*, augmentant l'impact de toute compromission.

**Famille / catégorie.** Incorrect/Excessive Permissions (CWE-732, CWE-250 « exécution avec privilèges superflus »).

**Mécanisme.** Violation directe du moindre privilège : droits accordés « pour que ça marche » et jamais réduits, rôles cloud trop larges, fichiers world-writable, comptes de service surpuissants.

**Impacts.** Amplifie l'élévation de privilèges et le mouvement latéral ; transforme une petite faille en compromission étendue.

🛡️ **Défense** — Moindre privilège strict, revues d'accès régulières, just-in-time access, suppression du privilege creep, analyse des permissions (notamment IAM cloud), séparation des tâches.

🧭 **Taxonomie** — Manifestation concrète de la violation du moindre privilège (chapitre 12) ; aggrave presque toutes les autres familles.

🎯 **À retenir** — Les permissions excessives ne *créent* pas l'intrusion mais en *décuplent* l'impact. La revue d'accès est une hygiène continue.


### Chapitre 77 — Exposition de secrets

**Définition.** Des secrets (mots de passe, clés API, jetons, certificats, chaînes de connexion) se retrouvent accessibles là où ils ne devraient pas.

**Famille / catégorie.** Secrets Exposure (CWE-798 « identifiants codés en dur », CWE-312/522).

**Mécanisme.** Secrets dans le code source, les dépôts Git (et leur historique), les images de conteneurs, les fichiers de configuration, les logs, les variables d'environnement exposées, les buckets publics.

**Impacts.** Accès direct et immédiat aux systèmes/services protégés par ces secrets ; souvent un raccourci catastrophique pour l'attaquant.

🛡️ **Défense** — Gestionnaire de secrets dédié (coffre-fort), interdiction des secrets en dur, **secrets scanning** (pré-commit et CI), rotation, révocation rapide, principe « pas de secret dans le code/les logs ».

🧭 **Taxonomie** — Recoupe fuite d'information (chapitre 69) et mauvaise configuration (chapitre 67) ; vecteur récurrent dans le cloud et la CI/CD.

🎯 **À retenir** — Un secret exposé est une clé laissée sur la porte : scanner, externaliser dans un coffre, et faire tourner les secrets sont impératifs.


### Chapitre 78 — Logging insuffisant

**Définition.** Absence, insuffisance ou mauvaise protection des journaux, empêchant de détecter, comprendre et prouver une attaque.

**Famille / catégorie.** Security Logging and Monitoring Failures (OWASP Top 10 ; CWE-778).

**Mécanisme.** Événements de sécurité non journalisés, journaux locaux effaçables, absence de centralisation, pas d'alerte, horloges non synchronisées, rétention trop courte.

**Impacts.** Détection tardive ou nulle, investigation impossible, perte de preuves, temps de présence de l'attaquant (dwell time) prolongé.

🛡️ **Défense** — Journalisation des événements de sécurité, centralisation (SIEM) hors de portée de l'attaquant, intégrité et horodatage fiables, alerting, rétention adaptée, tests de détection.

🧭 **Taxonomie** — Symétrique défensif de la Partie 11 ; sans logs, pas de SOC ni de forensic. Relié à la traçabilité (chapitre 26).

🎯 **À retenir** — Ne pas journaliser, c'est être aveugle : une attaque non vue est une attaque non traitée, qui dure.


### Chapitre 79 — Absence de limitation de débit

**Définition.** Le système ne limite pas le *nombre de requêtes/actions* dans le temps, permettant l'abus par répétition massive.

**Famille / catégorie.** Improper Rate Limiting / Resource Consumption (CWE-770, CWE-799 ; OWASP API « Unrestricted Resource Consumption »).

**Mécanisme.** Sans plafond, l'attaquant peut brute-forcer des identifiants, énumérer des objets, scraper des données, ou épuiser les ressources (déni de service applicatif, surcoût cloud).

**Impacts.** Brute force/credential stuffing facilités, énumération de données, déni de service, explosion de coûts (cloud).

🛡️ **Défense** — Limitation de débit (par IP/compte/clé), quotas, throttling progressif, CAPTCHA ciblé, détection d'anomalies, contrôles de coût côté cloud.

🧭 **Taxonomie** — Facilitateur transverse : aggrave authentification (chapitre 62), autorisation (énumération), API (chapitre 45) et disponibilité.

🎯 **À retenir** — Sans limitation de débit, beaucoup d'attaques « lentes » deviennent triviales par la force brute. Plafonner est une défense simple et puissante.


### Chapitre 80 — Rupture de frontière de confiance

**Définition.** Faiblesse où une *frontière de confiance* (entre zones de niveaux de fiabilité différents) est franchie sans contrôle adéquat : on traite une donnée/un appelant non fiable comme fiable.

**Famille / catégorie.** Trust Boundary Violation (CWE-501).

**Mécanisme.** Données venant d'une zone non fiable (Internet, client, tiers) acceptées sans revalidation dans une zone de confiance ; confiance implicite accordée au réseau interne, au client, ou à un système amont.

**Impacts.** Sert de socle à l'injection, à la falsification de données, au contournement de contrôles ; cœur conceptuel de nombreux abus.

🔧 **Exemple concret** — Faire confiance à un prix calculé côté client, ou à un en-tête « interne » falsifiable, parce qu'il « vient de l'intérieur ».

🛡️ **Défense** — Identifier explicitement les frontières de confiance (threat modeling), revalider à chaque franchissement, ne jamais faire confiance au client ni à la localisation réseau (Zero Trust), contrôles côté serveur.

🧭 **Taxonomie** — Concept *transversal* qui sous-tend presque toutes les autres familles ; au cœur du Zero Trust (chapitre 17).

🎯 **À retenir** — Chaque fois qu'une donnée franchit une frontière de confiance, elle doit être revalidée. La confiance implicite est la racine de bien des failles.


### Chapitre 81 — Supply chain logicielle

**Définition.** Vulnérabilités introduites *par* ou *dans* la chaîne de production logicielle : dépendances, outils de build, distribution, mises à jour.

**Famille / catégorie.** Software Supply Chain (OWASP « Software and Data Integrity Failures » ; familles CWE liées à l'intégrité).

**Mécanisme.** Au-delà des dépendances simplement *vulnérables* (chapitre 71), la supply chain ajoute la dimension *malveillante et amont* : paquets piégés (typosquatting, dependency confusion), build compromis, mises à jour signées détournées, artefacts altérés.

**Impacts.** Compromission massive et « de confiance » (le code malveillant arrive par un canal légitime) ; très difficile à détecter.

🛡️ **Défense** — SBOM, provenance et intégrité (signatures, **SLSA**), dépôts internes filtrés, verrouillage des versions, vérification des paquets, isolation de la CI/CD, revue des mises à jour tierces.

🧭 **Taxonomie** — Pont entre la Partie 5 (faiblesse) et la Partie 10 (attaques supply chain) ; recoupe la gestion des tiers (chapitre 38).

🎯 **À retenir** — La supply chain transforme la confiance en vecteur d'attaque : ce qui arrive « par un canal de confiance » doit tout de même être vérifié (intégrité, provenance).

---

> **Fin du Volume 2/8.**
>
> **Acquis :** vous savez désormais cartographier *où* l'on peut être attaqué (Partie 4 — surfaces) et nommer *quelle faiblesse* est exploitée (Partie 5 — vulnérabilités, vocabulaire CWE).
>
> **Suite — Volume 3 : Partie 6, Attaques web et applicatives** (le plus dense : Broken Access Control, IDOR/BOLA, toute la famille XSS, toute la famille SQLi, command/LDAP/XPath injection, SSTI, XXE, SSRF, file inclusion, désérialisation, CSRF, clickjacking, CORS, request smuggling, cache poisoning, prototype pollution, GraphQL abuse…). Chaque grande attaque y suivra le format en 10 points : définition · famille · principe · sous-types · exemple conceptuel · impacts · détection · prévention · erreurs fréquentes · à retenir.


---


## Taxonomie de la cybersécurité — Volume 3/8

> Partie 6 : Attaques web et applicatives
>
> C'est la partie la plus dense du cours, car la surface web (chapitre 44) concentre le plus grand nombre de sous-types d'attaques. Les grandes attaques suivent le **format en 10 points** : 1) Définition · 2) Famille · 3) Principe · 4) Sous-types · 5) Exemple conceptuel (sans payload) · 6) Impacts · 7) Signaux de détection · 8) Prévention · 9) Erreurs fréquentes · 10) À retenir.
>
> **Rappel de posture** : on explique les *mécanismes* et les *défenses*, jamais de charge offensive exploitable. Les « exemples » restent conceptuels.

---
