---
title: Partie 6 — Attaques web et applicatives
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
chapter: 7
chapters: 15
---

### Vue d'ensemble taxonomique de la Partie 6

Les attaques web se rangent en quelques grandes familles, qu'il faut garder en tête :

- **Contrôle d'accès cassé** : on accède à ce qui ne nous appartient pas (IDOR/BOLA, élévation de privilèges).
- **Injection** : on fait exécuter du code/des commandes (XSS, SQLi, command, LDAP, XPath, SSTI, XXE).
- **Falsification de requêtes** : on fait agir le serveur ou le navigateur à notre place (SSRF, CSRF).
- **Accès aux fichiers** : on lit/écrit des fichiers non prévus (LFI/RFI, path traversal, upload, Zip Slip).
- **Confiance et intégrité** : on abuse de la confiance accordée (désérialisation, CORS, open redirect, host header, prototype pollution).
- **Protocole/infrastructure web** : on exploite la couche HTTP/cache (request smuggling, cache poisoning, web cache deception).
- **Logique et abus** : on détourne le fonctionnement prévu (business logic, rate limit bypass, GraphQL abuse).

🧭 **Taxonomie** — Quand vous rencontrez une attaque web inconnue, rattachez-la d'abord à l'une de ces sept familles : vous saurez immédiatement quel type de défense s'applique.

---

### Chapitre 82 — Broken Access Control

1. **Définition.** Faille permettant à un utilisateur d'agir au-delà de ses permissions : accéder, modifier ou supprimer des ressources/fonctions qui ne lui sont pas destinées.
2. **Famille.** Contrôle d'accès cassé (OWASP Top 10 n°1 ; CWE-285/862). Famille parente d'IDOR/BOLA et de l'élévation de privilèges.
3. **Principe.** Le contrôle d'autorisation est absent, incomplet, incohérent ou réalisé côté client. Le serveur exécute une action sans vérifier que l'appelant y a droit *pour cet objet précis*.
4. **Sous-types.** IDOR/BOLA (objets), BFLA (fonctions), élévation verticale/horizontale, forced browsing (accès direct à des URL non liées), contournement par paramètre, fonctions d'administration exposées.
5. **Exemple conceptuel.** Une page affiche « ma facture » via un identifiant dans l'URL ; en changeant l'identifiant, on accède à la facture d'autrui — parce que le serveur ne vérifie pas la propriété.
6. **Impacts.** Accès/modification de données d'autrui, élévation de privilèges, contournement de la logique métier, fuite massive de données.
7. **Détection.** Accès à des identifiants hors périmètre, appels d'endpoints privilégiés par des comptes standard, énumération séquentielle d'identifiants, schémas d'accès anormaux.
8. **Prévention.** Contrôle d'accès *systématique côté serveur*, « deny by default », vérification de propriété à chaque accès, RBAC/ABAC centralisé, refus d'exposer la logique d'autorisation au client, tests d'autorisation automatisés.
9. ⚠️ **Erreur fréquente.** Masquer un bouton dans l'interface et croire la fonction protégée : l'endpoint reste appelable directement (« sécurité par l'UI »).
10. 🎯 **À retenir.** N°1 du Top 10. L'authentification dit *qui* ; le contrôle d'accès doit dire *a-t-il le droit, pour cet objet précis* — à chaque requête, côté serveur.

### Chapitre 83 — IDOR / BOLA

1. **Définition.** *Insecure Direct Object Reference* (web) / *Broken Object Level Authorization* (API) : accéder à un objet en manipulant sa référence (identifiant), sans contrôle de propriété.
2. **Famille.** Sous-type majeur du Broken Access Control (chapitre 82).
3. **Principe.** L'application expose une référence directe à un objet (id numérique, nom de fichier, UUID) et se fie à cette référence sans vérifier que l'utilisateur courant en est bien le propriétaire/autorisé.
4. **Sous-types.** IDOR sur identifiants séquentiels (énumérables), sur UUID (devinables s'ils fuitent), en lecture vs écriture/suppression, sur fichiers, sur paramètres imbriqués.
5. **Exemple conceptuel.** Une API renvoie `/api/orders/{id}` ; en incrémentant `{id}`, on lit les commandes des autres clients faute de vérification d'appartenance.
6. **Impacts.** Fuite de données personnelles à grande échelle, modification/suppression de données d'autrui, violation de confidentialité réglementée.
7. **Détection.** Énumération d'identifiants, un même compte accédant à de nombreux objets distincts, accès à des id jamais « possédés » par l'utilisateur.
8. **Prévention.** Vérifier la *propriété/autorisation* de chaque objet côté serveur ; préférer des références indirectes ou liées à la session ; ne pas se reposer sur l'imprévisibilité d'un UUID ; tests d'autorisation par objet.
9. ⚠️ **Erreur fréquente.** Penser qu'un UUID « non devinable » protège : c'est de l'obscurité, pas du contrôle d'accès. Un UUID qui fuite (logs, référents) reste exploitable.
10. 🎯 **À retenir.** L'IDOR/BOLA est la faille d'autorisation la plus répandue (surtout en API) : *toujours* vérifier que l'utilisateur a le droit sur *cet objet*, jamais se fier à la seule référence.

### Chapitre 84 — Élévation de privilèges verticale et horizontale

1. **Définition.** Obtenir des droits supérieurs (verticale) ou accéder aux ressources d'un pair de même niveau (horizontale).
2. **Famille.** Broken Access Control (chapitre 82).
3. **Principe.** *Verticale* : un utilisateur standard accède à des fonctions d'administration. *Horizontale* : un utilisateur accède aux données d'un autre utilisateur de même rôle (l'IDOR en est une forme).
4. **Sous-types.** Verticale (user → admin), horizontale (user A → user B), via mass assignment (modifier son propre rôle), via fonctions cachées, via paramètres de rôle manipulables.
5. **Exemple conceptuel.** Un formulaire de profil accepte un champ `role` non prévu ; l'envoyer avec `role=admin` élève les privilèges si le serveur l'assigne aveuglément (mass assignment).
6. **Impacts.** Prise de contrôle de comptes, accès administrateur, compromission étendue de l'application.
7. **Détection.** Comptes standard exécutant des actions privilégiées, modifications de rôle inattendues, accès croisés entre utilisateurs.
8. **Prévention.** Contrôles d'accès par fonction *et* par objet, allowlist des champs modifiables (contre le mass assignment), séparation nette des rôles, refus par défaut, tests d'élévation.
9. ⚠️ **Erreur fréquente.** Lier des attributs de requête directement aux objets internes (mass assignment) sans filtrer les champs autorisés.
10. 🎯 **À retenir.** Verticale = monter en droits ; horizontale = aller chez le voisin. Les deux se préviennent par un contrôle d'accès strict, par fonction et par objet.

### Chapitre 85 — XSS — vue d'ensemble

1. **Définition.** *Cross-Site Scripting* : injection de scripts exécutés dans le navigateur d'autres utilisateurs, dans le contexte du site de confiance.
2. **Famille.** Injection (chapitre 64), côté client. CWE-79.
3. **Principe.** L'application renvoie une donnée contrôlée par l'attaquant *sans encodage adapté au contexte*, si bien que le navigateur l'interprète comme du code (HTML/JS) plutôt que comme du texte.
4. **Sous-types.** Reflected (86), Stored (87), DOM-based (88), Blind (89), Mutation/mXSS (90), Self-XSS, via fichiers/SVG/markdown (91) — et selon le *contexte* d'injection (HTML, attribut, JS, URL).
5. **Exemple conceptuel.** Un champ de recherche réaffiche le terme saisi sans encodage : un contenu actif soumis par un attaquant s'exécute dans le navigateur de la victime.
6. **Impacts.** Vol de session/cookies, actions au nom de la victime, keylogging, défiguration, hameçonnage dans la page, pivot vers le compte.
7. **Détection.** Présence de balises/contenu actif dans des champs de données, alertes WAF, anomalies dans les paramètres réfléchis, rapports CSP (violations).
8. **Prévention.** *Encodage de sortie contextuel* (la défense centrale), validation d'entrée, **CSP** (Content Security Policy), cookies `HttpOnly`, frameworks à échappement automatique, attention aux « sinks » dangereux côté JS.
9. ⚠️ **Erreur fréquente.** Filtrer « <script> » par blocklist : d'innombrables contextes et encodages contournent ce filtre. La bonne approche est l'encodage *selon le contexte de sortie*.
10. 🎯 **À retenir.** XSS = le serveur laisse une donnée devenir du code dans le navigateur. La parade reine est l'encodage contextuel des sorties, renforcé par CSP et HttpOnly.

### Chapitre 86 — Reflected XSS

1. **Définition.** XSS où le contenu injecté est *renvoyé immédiatement* dans la réponse à une requête (non stocké).
2. **Famille.** XSS (chapitre 85) / injection côté client.
3. **Principe.** Un paramètre de la requête (URL, formulaire) est réfléchi dans la page sans encodage. L'attaque exige que la victime suive un lien piégé.
4. **Sous-types.** Selon le contexte de réflexion (corps HTML, attribut, script, URL) ; via GET (lien) ou POST (formulaire piégé).
5. **Exemple conceptuel.** Une page d'erreur affiche « page introuvable : <valeur du paramètre> » sans encodage ; un lien spécialement formé fait exécuter du contenu actif chez qui le clique.
6. **Impacts.** Vol de session, actions au nom de la victime — limités à ceux qui suivent le lien.
7. **Détection.** Paramètres réfléchis sans encodage, clics sur des liens anormaux, alertes WAF/CSP.
8. **Prévention.** Encodage contextuel de toute donnée réfléchie, CSP, validation, méfiance envers les paramètres affichés.
9. ⚠️ **Erreur fréquente.** Considérer le reflected XSS « peu grave » car non persistant : couplé à du phishing, il suffit à compromettre des comptes ciblés.
10. 🎯 **À retenir.** Reflected = injection renvoyée à la volée, déclenchée par un lien piégé. Encoder la sortie réfléchie ferme la faille.

### Chapitre 87 — Stored XSS

1. **Définition.** XSS où le contenu injecté est *stocké* par l'application (base, fichier) puis *réaffiché* à d'autres utilisateurs.
2. **Famille.** XSS (chapitre 85).
3. **Principe.** L'attaquant dépose une fois le contenu actif (commentaire, profil, message) ; il s'exécute ensuite chez *tous* ceux qui consultent la page. Pas besoin de lien piégé : c'est persistant et « auto-propagé ».
4. **Sous-types.** Dans commentaires/messages, profils, noms de fichiers, métadonnées, champs admin (impact aggravé si vu par un administrateur).
5. **Exemple conceptuel.** Un champ « biographie » de profil accepte du contenu actif ; chaque visiteur du profil l'exécute dans son navigateur.
6. **Impacts.** Les plus graves des XSS : compromission de nombreux utilisateurs, propagation type « ver », prise de comptes admin si affiché dans une console.
7. **Détection.** Contenu actif persistant dans les données, pics d'événements XSS multi-utilisateurs, violations CSP en série.
8. **Prévention.** Encodage à l'affichage (sortie), validation/assainissement à l'entrée, CSP, assainisseur HTML pour le contenu riche, revue des champs affichés en zone privilégiée.
9. ⚠️ **Erreur fréquente.** Assainir uniquement à l'entrée et oublier l'encodage à la sortie (ou l'inverse) : les deux se complètent.
10. 🎯 **À retenir.** Stored XSS = injection persistante qui frappe tous les lecteurs. C'est la variante la plus dangereuse ; encodage de sortie + assainissement + CSP.

### Chapitre 88 — DOM-based XSS

1. **Définition.** XSS qui se produit *entièrement côté client*, lorsque du JavaScript de la page manipule des données contrôlables sans précaution.
2. **Famille.** XSS (chapitre 85), variante côté navigateur (le serveur peut ne jamais voir la charge).
3. **Principe.** Une « source » contrôlable (fragment d'URL, `location`, message) est passée à un « sink » dangereux (qui écrit du HTML/exécute du code) par le script de la page, sans encodage.
4. **Sous-types.** Selon source (hash d'URL, paramètres, `postMessage`, stockage) et sink (insertion HTML, évaluation dynamique, manipulation du DOM).
5. **Exemple conceptuel.** Un script lit la portion d'URL après `#` et l'insère telle quelle dans la page ; une valeur conçue par l'attaquant devient active sans aller au serveur.
6. **Impacts.** Identiques aux autres XSS ; particulièrement furtif (invisible côté serveur, donc des défenses serveur seules échouent).
7. **Détection.** Analyse du JS côté client (sources→sinks), tests DAST orientés DOM, rapports CSP, revue de code front.
8. **Prévention.** Éviter les sinks dangereux, API sûres de manipulation du DOM, encodage côté client, frameworks à liaison sûre, **Trusted Types**, CSP.
9. ⚠️ **Erreur fréquente.** Compter sur un WAF serveur : le DOM-XSS peut ne jamais transiter par le serveur (par ex. via le fragment d'URL).
10. 🎯 **À retenir.** DOM-XSS vit dans le navigateur : la défense est *côté client* (sinks sûrs, Trusted Types), pas seulement côté serveur.

### Chapitre 89 — Blind XSS

1. **Définition.** XSS stocké dont l'exécution survient dans un contexte *non visible* de l'attaquant (par ex. une interface d'administration interne).
2. **Famille.** Variante de Stored XSS (chapitre 87).
3. **Principe.** La charge est déposée dans un champ qui sera consulté plus tard par un tiers (support, admin) dans un panneau interne ; l'attaquant ne voit pas le rendu mais reçoit un signal lorsqu'elle s'exécute.
4. **Sous-types.** Via formulaires de contact, logs affichés en console admin, tickets de support, champs exportés vers des outils internes.
5. **Exemple conceptuel.** Un message envoyé au support s'affiche dans une console interne ; il s'y exécute quand un agent l'ouvre.
6. **Impacts.** Compromission de comptes *privilégiés* (admins/support), souvent à fort impact, malgré l'absence de retour visible immédiat.
7. **Détection.** Surveillance des consoles internes, CSP sur les back-offices, journalisation des rendus de champs utilisateur en zone admin.
8. **Prévention.** Traiter les données utilisateur *partout* où elles sont affichées (y compris back-offices internes), encodage de sortie, CSP sur les interfaces d'administration.
9. ⚠️ **Erreur fréquente.** Sécuriser le front public mais négliger les interfaces internes, considérées « de confiance ».
10. 🎯 **À retenir.** Le blind XSS frappe là où on ne regarde pas : les back-offices internes doivent être protégés comme le front public.

### Chapitre 90 — Mutation XSS (mXSS)

1. **Définition.** XSS où un contenu *réputé assaini* est ré-interprété (« muté ») par le navigateur lors de la normalisation du HTML, redevenant actif.
2. **Famille.** XSS (chapitre 85), catégorie avancée liée au parsing (chapitre 75).
3. **Principe.** L'assainisseur et le moteur de rendu du navigateur n'interprètent pas le HTML de la même façon ; après ré-écriture par le navigateur (innerHTML, normalisation), une chaîne inerte peut redevenir exécutable.
4. **Sous-types.** Via incohérences de parsing HTML/SVG/MathML, via re-sérialisation, via namespaces.
5. **Exemple conceptuel.** Un contenu validé par un assainisseur est ensuite ré-inséré et normalisé par le navigateur, produisant une structure active non anticipée.
6. **Impacts.** Contournement d'assainisseurs HTML, donc XSS malgré une protection apparente.
7. **Détection.** Tests avec des assainisseurs et navigateurs à jour, fuzzing de l'assainisseur, surveillance CSP.
8. **Prévention.** Assainisseurs HTML maintenus et éprouvés, éviter le re-traitement du HTML déjà assaini, Trusted Types, CSP, limiter le HTML riche.
9. ⚠️ **Erreur fréquente.** Faire confiance à un assainisseur maison ou obsolète : le mXSS exploite précisément ces écarts.
10. 🎯 **À retenir.** Le mXSS exploite le désaccord entre assainisseur et navigateur. Utiliser un assainisseur reconnu et à jour, et ne pas re-manipuler le HTML assaini.

### Chapitre 91 — XSS via fichiers, SVG, markdown ou éditeurs riches

1. **Définition.** XSS introduit par des *formats riches* : fichiers SVG/HTML uploadés, markdown converti en HTML, éditeurs WYSIWYG.
2. **Famille.** XSS (chapitre 85), à la frontière de l'upload (chapitre 112).
3. **Principe.** Ces formats peuvent contenir du contenu actif (un SVG est du XML pouvant porter du script ; le markdown peut produire du HTML ; un éditeur riche stocke du HTML). Servis ou rendus sans assainissement, ils exécutent du code.
4. **Sous-types.** SVG actif, upload HTML servi en ligne, markdown→HTML non assaini, contenu d'éditeur riche, métadonnées de fichiers affichées.
5. **Exemple conceptuel.** Un avatar au format SVG, contenant du contenu actif, s'exécute lorsqu'il est affiché en ligne dans le navigateur d'un visiteur.
6. **Impacts.** XSS stocké, souvent à large portée (avatars, documents partagés).
7. **Détection.** Inspection des fichiers riches uploadés, analyse du HTML généré par markdown/éditeurs, CSP, type MIME servi.
8. **Prévention.** Assainir le HTML issu du markdown/éditeurs, servir les fichiers uploadés depuis un domaine isolé avec `Content-Disposition` adapté et bon type MIME, désactiver le rendu en ligne du SVG non fiable, CSP.
9. ⚠️ **Erreur fréquente.** Traiter une image SVG comme une image inerte : c'est du code potentiellement actif.
10. 🎯 **À retenir.** Les formats riches (SVG, markdown, éditeurs) sont des vecteurs XSS : assainir le rendu et isoler le service des fichiers uploadés.

### Chapitre 92 — Injection SQL — vue d'ensemble

1. **Définition.** Injection où une entrée non fiable modifie une *requête SQL*, permettant de lire/écrire la base ou de contourner la logique.
2. **Famille.** Injection (chapitre 64). CWE-89.
3. **Principe.** L'application construit la requête en *concaténant* des données utilisateur ; l'attaquant injecte de la syntaxe SQL qui change le sens de la requête.
4. **Sous-types.** Union-based (93), error-based (94), boolean-blind (95), time-blind (96), out-of-band (97), second-order (98), plus NoSQL (99) et variantes (ORM injection).
5. **Exemple conceptuel.** Un champ de connexion concatène l'entrée dans la clause de filtrage ; une entrée structurée altère la condition et contourne le contrôle.
6. **Impacts.** Vol/altération massive de données, contournement d'authentification, parfois exécution de commandes ou compromission du serveur de base.
7. **Détection.** Erreurs SQL renvoyées, motifs d'injection dans les paramètres, requêtes anormales/lentes, alertes WAF, pics d'erreurs base.
8. **Prévention.** **Requêtes paramétrées/préparées** (défense reine), ORM utilisés correctement, validation par allowlist, moindre privilège du compte base, désactivation des messages d'erreur détaillés.
9. ⚠️ **Erreur fréquente.** « Échapper » manuellement les caractères au lieu de paramétrer : fragile et contournable. Le paramétrage sépare structurellement code et données.
10. 🎯 **À retenir.** SQLi = données traitées comme du SQL. Les requêtes paramétrées éliminent la racine du problème ; le moindre privilège limite l'impact résiduel.

### Chapitre 93 — Union-based SQL injection

1. **Définition.** SQLi exploitant l'opérateur d'union pour *ajouter* des résultats issus d'autres tables à la réponse légitime.
2. **Famille.** SQLi (chapitre 92), variante « in-band » (résultats directement visibles).
3. **Principe.** Quand la réponse affiche le résultat d'une requête, l'attaquant fusionne un second jeu de données (d'autres tables/colonnes) au résultat affiché.
4. **Sous-types.** Selon le nombre/type de colonnes à aligner, selon les données ciblées (identifiants, autres tables).
5. **Exemple conceptuel.** Une page listant des produits laisse l'attaquant adjoindre, à la liste affichée, des données provenant d'une autre table.
6. **Impacts.** Extraction directe et rapide de données arbitraires de la base.
7. **Détection.** Mots-clés d'union dans les paramètres, réponses contenant des données inattendues, erreurs de nombre de colonnes.
8. **Prévention.** Identiques à la SQLi (paramétrage, allowlist, moindre privilège) ; ne jamais refléter des résultats de requêtes construites par concaténation.
9. ⚠️ **Erreur fréquente.** Croire qu'afficher « peu de colonnes » protège : l'attaquant aligne ce qu'il faut.
10. 🎯 **À retenir.** L'union-based est la SQLi la plus directe quand les résultats sont affichés. Paramétrer la requête supprime le vecteur.

### Chapitre 94 — Error-based SQL injection

1. **Définition.** SQLi où les *messages d'erreur* de la base révèlent des données ou la structure.
2. **Famille.** SQLi in-band (chapitre 92).
3. **Principe.** L'attaquant provoque des erreurs dont le contenu (renvoyé à l'utilisateur) divulgue des informations (noms de tables, valeurs).
4. **Sous-types.** Selon le SGBD et les fonctions d'erreur exploitées.
5. **Exemple conceptuel.** Une requête mal formée renvoie un message technique détaillé contenant un fragment de donnée de la base.
6. **Impacts.** Extraction de données et cartographie de la base, reconnaissance facilitée.
7. **Détection.** Messages d'erreur SQL exposés, pics d'erreurs base, motifs d'injection.
8. **Prévention.** Paramétrage, **messages d'erreur génériques** en production (pas de détail technique), journalisation côté serveur uniquement, moindre privilège.
9. ⚠️ **Erreur fréquente.** Laisser les traces d'erreur détaillées en production : c'est à la fois une fuite d'information (chapitre 69) et un facilitateur de SQLi.
10. 🎯 **À retenir.** Les erreurs verbeuses transforment une SQLi en extraction facile. Génériciser les erreurs et paramétrer.

### Chapitre 95 — Boolean-based blind SQL injection

1. **Définition.** SQLi « à l'aveugle » où l'attaquant déduit l'information à partir de réponses *différentes selon une condition vraie/fausse*, sans voir les données.
2. **Famille.** SQLi inférentielle/blind (chapitre 92).
3. **Principe.** L'application ne renvoie pas les données ni les erreurs, mais son comportement (page différente, présence/absence d'un élément) change selon que la condition injectée est vraie ou fausse — permettant une extraction bit à bit.
4. **Sous-types.** Selon le signal observable (contenu, code de statut, longueur).
5. **Exemple conceptuel.** Selon qu'une condition injectée est vraie ou fausse, la page affiche « trouvé » ou « non trouvé » ; l'attaquant reconstitue l'information question après question.
6. **Impacts.** Extraction de données (plus lente mais fiable), même sans affichage direct.
7. **Détection.** Volume anormal de requêtes quasi identiques variant un paramètre, motifs d'inférence, sans limitation de débit.
8. **Prévention.** Paramétrage, réponses uniformes, **limitation de débit** (chapitre 79), détection d'anomalies, moindre privilège.
9. ⚠️ **Erreur fréquente.** Croire qu'« aucune donnée affichée » protège : l'inférence suffit à tout extraire.
10. 🎯 **À retenir.** L'absence d'affichage ne protège pas : le comportement de l'app suffit à fuiter. Paramétrer et limiter le débit.

### Chapitre 96 — Time-based blind SQL injection

1. **Définition.** SQLi à l'aveugle où l'information se déduit du *temps de réponse* (réponse retardée si la condition est vraie).
2. **Famille.** SQLi inférentielle/blind (chapitre 92).
3. **Principe.** Quand ni les données ni le comportement ne diffèrent, l'attaquant injecte une condition qui *retarde* la réponse selon vrai/faux, et mesure le délai.
4. **Sous-types.** Selon les fonctions de temporisation du SGBD.
5. **Exemple conceptuel.** Une réponse qui arrive « lentement » quand une condition est vraie, et « vite » sinon, révèle l'information par chronométrage.
6. **Impacts.** Extraction de données, plus lente encore, mais possible sans aucun retour visible.
7. **Détection.** Requêtes provoquant des délais anormaux et répétitifs, charge inhabituelle, absence de limitation.
8. **Prévention.** Paramétrage, limitation de débit, time-outs de requêtes, détection d'anomalies, moindre privilège.
9. ⚠️ **Erreur fréquente.** Ignorer les requêtes « lentes » répétées : ce sont des signaux d'inférence temporelle.
10. 🎯 **À retenir.** Même le *temps de réponse* fuit de l'information. Paramétrer, limiter le débit et surveiller les délais anormaux.

### Chapitre 97 — Out-of-band SQL injection

1. **Définition.** SQLi où les données sont exfiltrées par un *canal différent* (souvent une requête réseau sortante, ex. DNS/HTTP) plutôt que dans la réponse.
2. **Famille.** SQLi (chapitre 92), variante hors-bande.
3. **Principe.** Quand l'inférence est trop lente ou impossible, l'attaquant fait *émettre* à la base une requête réseau contenant la donnée, vers un serveur qu'il contrôle.
4. **Sous-types.** Via résolution DNS, via requêtes HTTP sortantes, selon les capacités du SGBD.
5. **Exemple conceptuel.** La base est amenée à effectuer une résolution de nom incluant une donnée, captée par l'attaquant côté serveur DNS.
6. **Impacts.** Exfiltration efficace, même sans retour applicatif.
7. **Détection.** Flux réseau sortants inattendus depuis le serveur de base (DNS/HTTP), corrélation avec des paramètres suspects.
8. **Prévention.** Paramétrage, **filtrage sortant** (la base ne doit pas initier de trafic Internet), durcissement du SGBD, moindre privilège, segmentation.
9. ⚠️ **Erreur fréquente.** Autoriser les serveurs de base à émettre du trafic sortant arbitraire.
10. 🎯 **À retenir.** Couper le trafic sortant des serveurs de base neutralise l'exfiltration hors-bande. Paramétrer reste la base.

### Chapitre 98 — Second-order SQL injection

1. **Définition.** SQLi où la donnée malveillante est *stockée* d'abord, puis exécutée *plus tard* lorsqu'elle est réutilisée dans une requête.
2. **Famille.** SQLi (chapitre 92), différée.
3. **Principe.** L'entrée passe les contrôles à la saisie (elle est juste stockée), mais une fonctionnalité ultérieure la réinjecte dans une requête sans paramétrage — l'injection se déclenche en différé.
4. **Sous-types.** Via champs de profil réutilisés, via traitements par lots, via fonctions d'export/reporting.
5. **Exemple conceptuel.** Une valeur enregistrée dans un profil est ensuite intégrée telle quelle à une requête lors d'un traitement administratif ultérieur.
6. **Impacts.** Identiques à la SQLi, mais plus furtifs (découplage saisie/exécution).
7. **Détection.** Difficile : nécessite de tracer le flux des données stockées vers les requêtes ; revue de code, tests ciblés.
8. **Prévention.** Paramétrer *toutes* les requêtes, y compris celles utilisant des données « déjà en base » ; ne jamais considérer une donnée stockée comme fiable (frontière de confiance — chapitre 80).
9. ⚠️ **Erreur fréquente.** Assainir à l'entrée puis traiter la donnée stockée comme sûre lors d'une réutilisation ultérieure.
10. 🎯 **À retenir.** Une donnée stockée n'est pas une donnée sûre : paramétrer partout, même en réutilisant des valeurs internes.

### Chapitre 99 — NoSQL injection

1. **Définition.** Injection ciblant les bases *NoSQL* (documents, clés-valeurs), manipulant la structure des requêtes/opérateurs.
2. **Famille.** Injection (chapitre 64), variante NoSQL. CWE-943.
3. **Principe.** Les requêtes NoSQL sont souvent des structures (objets/JSON) ; injecter des opérateurs ou altérer la structure modifie la logique (par ex. transformer une égalité en condition toujours vraie).
4. **Sous-types.** Injection d'opérateurs, injection par type (passer un objet là où une chaîne est attendue), injection dans des fonctions d'évaluation côté base.
5. **Exemple conceptuel.** Un filtre d'authentification attend une valeur simple ; recevoir une structure d'opérateur le rend toujours satisfait, contournant la vérification.
6. **Impacts.** Contournement d'authentification, accès/altération de données, parfois exécution côté base.
7. **Détection.** Types inattendus dans les paramètres (objets au lieu de chaînes), opérateurs dans les entrées, requêtes anormales.
8. **Prévention.** Validation stricte de type et de schéma, requêtes paramétrées propres au moteur, refus des structures non attendues, moindre privilège, éviter l'évaluation dynamique côté base.
9. ⚠️ **Erreur fréquente.** Croire que « NoSQL = pas d'injection ». Le principe d'injection demeure, sous une autre forme.
10. 🎯 **À retenir.** NoSQL n'immunise pas contre l'injection : valider type et schéma, et n'accepter que des structures attendues.

### Chapitre 100 — Command injection

1. **Définition.** Injection où une entrée non fiable est insérée dans une *commande système* exécutée par le serveur.
2. **Famille.** Injection (chapitre 64). CWE-78.
3. **Principe.** L'application appelle le système d'exploitation en concaténant des données utilisateur ; l'attaquant ajoute des commandes exécutées avec les droits du processus.
4. **Sous-types.** Injection directe, injection « aveugle » (sans retour), injection d'arguments (argument injection).
5. **Exemple conceptuel.** Une fonctionnalité « ping » qui passe une adresse fournie à une commande système permet, si concaténée sans contrôle, d'enchaîner une autre commande.
6. **Impacts.** Exécution de code sur le serveur (RCE), compromission complète, pivot vers le réseau.
7. **Détection.** Caractères de chaînage/échappement dans les paramètres, processus enfants inattendus, alertes EDR sur le serveur, trafic sortant anormal.
8. **Prévention.** Éviter d'appeler le shell ; utiliser des **API directes** sans interpréteur ; si nécessaire, passer des arguments via des API sûres (pas de concaténation), allowlist stricte, moindre privilège du processus.
9. ⚠️ **Erreur fréquente.** « Échapper » la chaîne de commande : approche fragile. Le mieux est de *ne pas* passer par un shell.
10. 🎯 **À retenir.** La command injection donne souvent un RCE direct : éviter le shell et n'utiliser que des API paramétrées avec moindre privilège.

### Chapitre 101 — LDAP injection

1. **Définition.** Injection ciblant les requêtes *LDAP* (annuaires), altérant les filtres de recherche/authentification.
2. **Famille.** Injection (chapitre 64). CWE-90.
3. **Principe.** Construction de filtres LDAP par concaténation ; l'attaquant injecte de la syntaxe de filtre pour modifier la logique (contourner une authentification, élargir une recherche).
4. **Sous-types.** Injection dans le filtre de recherche, injection dans le DN, contournement d'authentification.
5. **Exemple conceptuel.** Un filtre d'authentification construit avec l'entrée utilisateur peut être transformé en condition trop permissive.
6. **Impacts.** Contournement d'authentification, divulgation d'entrées d'annuaire, élévation.
7. **Détection.** Caractères spéciaux LDAP dans les entrées, recherches anormalement larges, motifs d'injection.
8. **Prévention.** Échappement LDAP via API dédiées, validation par allowlist, requêtes paramétrées, moindre privilège du compte de liaison.
9. ⚠️ **Erreur fréquente.** Réutiliser des entrées utilisateur directement dans des filtres LDAP de connexion.
10. 🎯 **À retenir.** L'annuaire LDAP est, lui aussi, un interpréteur : échapper via API dédiée et valider en allowlist.

### Chapitre 102 — XPath injection

1. **Définition.** Injection ciblant les requêtes *XPath* sur des documents XML.
2. **Famille.** Injection (chapitre 64). CWE-643.
3. **Principe.** Construction de requêtes XPath par concaténation ; l'attaquant modifie l'expression pour accéder à des nœuds non prévus ou contourner une condition.
4. **Sous-types.** XPath injection classique, « blind » (inférentielle, comme la SQLi aveugle).
5. **Exemple conceptuel.** Une authentification stockée en XML, interrogée par XPath construit avec l'entrée, peut voir sa condition contournée.
6. **Impacts.** Contournement d'authentification, lecture de données XML non autorisées.
7. **Détection.** Caractères de syntaxe XPath dans les entrées, accès anormaux, motifs d'injection.
8. **Prévention.** Requêtes XPath paramétrées, échappement via API, validation, éviter de stocker des données sensibles d'authentification en XML interrogé dynamiquement.
9. ⚠️ **Erreur fréquente.** Considérer le XML comme « inerte » : interrogé par XPath concaténé, il est injectable.
10. 🎯 **À retenir.** XPath est un interpréteur de plus : paramétrer et valider, comme pour toute injection.

### Chapitre 103 — SSTI (Server-Side Template Injection)

1. **Définition.** Injection dans un *moteur de templates* côté serveur, où l'entrée est évaluée comme expression de template.
2. **Famille.** Injection (chapitre 64). CWE-1336.
3. **Principe.** Quand une entrée utilisateur est insérée dans un template *interprété* (au lieu d'être passée en donnée), l'attaquant peut exécuter des expressions du moteur, menant souvent à l'exécution de code serveur.
4. **Sous-types.** Selon le moteur de template ; du simple accès d'objets à l'exécution de code (RCE) selon les capacités exposées.
5. **Exemple conceptuel.** Un message d'e-mail personnalisé qui insère directement une entrée dans le template fait évaluer une expression au lieu de l'afficher comme texte.
6. **Impacts.** De la fuite d'information jusqu'au RCE, selon le moteur et le bac à sable.
7. **Détection.** Expressions de template dans les entrées, comportements d'évaluation inattendus, alertes serveur/EDR.
8. **Prévention.** Ne jamais insérer d'entrée utilisateur *dans la structure* d'un template ; passer les données en *contexte* (variables), pas en template ; bacs à sable, moteurs logic-less, validation.
9. ⚠️ **Erreur fréquente.** Construire dynamiquement des templates à partir d'entrées « pour la personnalisation ».
10. 🎯 **À retenir.** Le SSTI mène souvent au RCE : les données doivent *alimenter* un template, jamais *le constituer*.

### Chapitre 104 — XXE (XML External Entity)

1. **Définition.** Attaque exploitant le traitement des *entités externes* XML par un analyseur mal configuré.
2. **Famille.** Erreurs de parsing (chapitre 75) / injection. CWE-611.
3. **Principe.** Un parser XML qui résout les entités externes peut être amené à lire des fichiers locaux, effectuer des requêtes réseau (SSRF), ou subir un déni de service (expansion d'entités).
4. **Sous-types.** XXE en lecture de fichier, XXE-vers-SSRF, XXE aveugle (out-of-band), « billion laughs » (DoS par expansion).
5. **Exemple conceptuel.** Un import de document XML déclenche, via une entité externe, la lecture d'un fichier du serveur renvoyé dans la réponse.
6. **Impacts.** Lecture de fichiers sensibles, SSRF, déni de service, exfiltration hors-bande.
7. **Détection.** Déclarations d'entités/DOCTYPE dans les entrées XML, accès fichiers/réseau anormaux depuis le parser.
8. **Prévention.** **Désactiver les entités externes et le DOCTYPE** dans les parsers XML, utiliser des configurations sûres par défaut, préférer des formats plus simples, limiter tailles/profondeur.
9. ⚠️ **Erreur fréquente.** Utiliser un parser XML aux réglages par défaut historiquement permissifs.
10. 🎯 **À retenir.** XXE = parser XML trop permissif. Désactiver entités externes et DOCTYPE règle l'essentiel.

### Chapitre 105 — SSRF (Server-Side Request Forgery)

1. **Définition.** Attaque où le serveur est *manipulé pour émettre des requêtes* vers des destinations choisies par l'attaquant.
2. **Famille.** Falsification de requêtes côté serveur (OWASP Top 10). CWE-918.
3. **Principe.** Une fonctionnalité qui récupère une ressource à partir d'une URL fournie peut être détournée pour atteindre des cibles internes (services privés, métadonnées cloud) non accessibles directement.
4. **Sous-types.** SSRF classique (réponse visible), blind (106), vers métadonnées cloud (107), via parser d'URL, via redirection ouverte (pivot), DNS rebinding.
5. **Exemple conceptuel.** Une fonction « prévisualiser une URL » est dirigée vers un service interne normalement inaccessible depuis l'extérieur.
6. **Impacts.** Accès à des services internes, vol de secrets cloud (via métadonnées), cartographie interne, pivot, parfois RCE indirect.
7. **Détection.** Requêtes sortantes du serveur vers des cibles internes/inhabituelles, accès au service de métadonnées, URL suspectes en paramètre.
8. **Prévention.** Allowlist stricte des destinations, interdiction des plages internes et du service de métadonnées, validation/normalisation d'URL, **filtrage sortant**, durcissement du service de métadonnées (cloud).
9. ⚠️ **Erreur fréquente.** Filtrer par blocklist d'IP : contournable (redirections, encodages, rebinding DNS, IPv6). Préférer l'allowlist.
10. 🎯 **À retenir.** SSRF = le serveur devient le proxy de l'attaquant vers l'interne. Allowlist des destinations + blocage des métadonnées + filtrage sortant.

### Chapitre 106 — Blind SSRF

1. **Définition.** SSRF où l'attaquant *ne voit pas* la réponse, mais confirme/agit via des canaux indirects.
2. **Famille.** SSRF (chapitre 105).
3. **Principe.** Même sans retour, le serveur peut être amené à atteindre des cibles internes ; l'attaquant détecte le succès par des signaux hors-bande (résolution DNS, requête reçue) et déclenche des effets.
4. **Sous-types.** Détection via DNS/HTTP hors-bande, exploitation d'effets de bord internes.
5. **Exemple conceptuel.** Une fonction de récupération d'URL, dont la réponse n'est pas affichée, provoque néanmoins une requête observable côté attaquant, prouvant l'accès interne.
6. **Impacts.** Cartographie interne, déclenchement d'actions, vol de secrets via cibles connues, même sans retour direct.
7. **Détection.** Trafic sortant inattendu, résolutions DNS anormales, corrélation avec des paramètres URL.
8. **Prévention.** Identiques à la SSRF : allowlist, blocage interne/métadonnées, filtrage sortant, normalisation d'URL.
9. ⚠️ **Erreur fréquente.** Penser qu'« absence de réponse affichée » signifie « pas exploitable ».
10. 🎯 **À retenir.** Le blind SSRF est exploitable sans retour : les mêmes défenses (allowlist + filtrage sortant) s'appliquent.

### Chapitre 107 — SSRF vers métadonnées cloud

1. **Définition.** SSRF visant le *service de métadonnées* des environnements cloud, qui peut exposer des identifiants temporaires.
2. **Famille.** SSRF (chapitre 105), cas cloud à fort impact.
3. **Principe.** Les instances cloud disposent d'un point interne fournissant configuration et *crédentiels temporaires* ; un SSRF qui l'atteint peut récupérer ces secrets et usurper le rôle de l'instance.
4. **Sous-types.** Selon le fournisseur et la version du service de métadonnées (les versions renforcées exigent une étape supplémentaire).
5. **Exemple conceptuel.** Une fonctionnalité serveur récupérant une URL est dirigée vers l'adresse interne de métadonnées, exposant des identifiants de rôle.
6. **Impacts.** Vol d'identifiants cloud, élévation et mouvement latéral dans le cloud, accès aux ressources (stockage, bases).
7. **Détection.** Accès au point de métadonnées depuis un composant qui ne devrait pas, usage anormal d'identifiants de rôle.
8. **Prévention.** Versions renforcées du service de métadonnées, blocage explicite de cette adresse depuis les applications, moindre privilège des rôles d'instance, allowlist SSRF.
9. ⚠️ **Erreur fréquente.** Laisser le service de métadonnées en version permissive et les rôles d'instance surprivilégiés.
10. 🎯 **À retenir.** Le SSRF vers métadonnées transforme une faille web en vol d'identifiants cloud : durcir le service de métadonnées et appliquer le moindre privilège aux rôles.

### Chapitre 108 — File inclusion (vue d'ensemble)

1. **Définition.** Attaques amenant l'application à *inclure/charger un fichier* contrôlé par l'attaquant.
2. **Famille.** Accès aux fichiers / injection de chemin. CWE-98, CWE-22.
3. **Principe.** Une application qui choisit dynamiquement un fichier à inclure à partir d'une entrée peut être détournée pour charger un fichier local sensible (LFI) ou distant (RFI).
4. **Sous-types.** LFI (109), RFI (110), path traversal (111) comme mécanisme sous-jacent.
5. **Exemple conceptuel.** Un paramètre « page » utilisé pour inclure un fichier permet, mal contrôlé, de désigner un autre fichier que ceux prévus.
6. **Impacts.** Lecture de fichiers sensibles, parfois exécution de code (selon le type de fichier inclus), divulgation de configuration/secrets.
7. **Détection.** Séquences de traversée et chemins inhabituels en paramètre, accès fichiers anormaux.
8. **Prévention.** Ne pas construire de chemins/inclusions à partir d'entrées ; allowlist d'identifiants mappés à des fichiers fixes ; désactiver l'inclusion distante ; moindre privilège.
9. ⚠️ **Erreur fréquente.** Filtrer naïvement les « ../ » : de multiples encodages contournent. Préférer l'allowlist mappée.
10. 🎯 **À retenir.** Ne jamais dériver un chemin de fichier d'une entrée libre : mapper des identifiants vers des fichiers prédéfinis.

### Chapitre 109 — LFI (Local File Inclusion)

1. **Définition.** Inclusion d'un *fichier local* du serveur choisi par l'attaquant.
2. **Famille.** File inclusion (chapitre 108).
3. **Principe.** L'application inclut un fichier dont le chemin dépend d'une entrée ; l'attaquant désigne des fichiers sensibles locaux (configuration, logs).
4. **Sous-types.** Lecture de fichiers sensibles ; dans certains contextes, chaînage vers exécution (par ex. via fichiers contrôlés ailleurs).
5. **Exemple conceptuel.** Un paramètre de langue utilisé pour inclure un fichier de traduction est détourné pour pointer vers un fichier de configuration.
6. **Impacts.** Divulgation de configuration/secrets, reconnaissance, parfois exécution indirecte.
7. **Détection.** Chemins de traversée, accès à des fichiers hors du répertoire prévu.
8. **Prévention.** Allowlist mappée, base path verrouillée, désactivation des wrappers dangereux, moindre privilège, normalisation des chemins.
9. ⚠️ **Erreur fréquente.** Concaténer une entrée à un chemin de base sans normalisation ni allowlist.
10. 🎯 **À retenir.** LFI = inclure un fichier local non prévu. Allowlist mappée et base path verrouillée.

### Chapitre 110 — RFI (Remote File Inclusion)

1. **Définition.** Inclusion d'un fichier *distant* (hébergé par l'attaquant), souvent menant à l'exécution de code.
2. **Famille.** File inclusion (chapitre 108).
3. **Principe.** Une configuration permettant l'inclusion d'une ressource distante laisse l'attaquant faire charger et exécuter un fichier qu'il contrôle.
4. **Sous-types.** Selon la techno et la configuration autorisant l'inclusion distante.
5. **Exemple conceptuel.** Un paramètre d'inclusion accepte une URL externe, faisant charger un contenu distant par le serveur.
6. **Impacts.** Exécution de code à distance (souvent), compromission du serveur.
7. **Détection.** URL externes en paramètre d'inclusion, trafic sortant inattendu, exécution anormale.
8. **Prévention.** **Désactiver l'inclusion distante**, allowlist locale stricte, moindre privilège, filtrage sortant.
9. ⚠️ **Erreur fréquente.** Laisser activées des options d'inclusion d'URL distantes.
10. 🎯 **À retenir.** RFI mène souvent au RCE : désactiver toute inclusion distante.

### Chapitre 111 — Path traversal / Directory traversal

1. **Définition.** Accès à des fichiers/répertoires *hors du dossier prévu* en manipulant le chemin.
2. **Famille.** Accès aux fichiers (CWE-22). Mécanisme sous-jacent du LFI et de nombreux abus de fichiers.
3. **Principe.** En insérant des séquences de remontée de répertoire (et leurs encodages), l'attaquant « sort » du dossier autorisé pour atteindre d'autres fichiers.
4. **Sous-types.** Traversée en lecture, en écriture, via encodages multiples, via chemins absolus.
5. **Exemple conceptuel.** Un paramètre de nom de fichier de téléchargement, mal contrôlé, désigne un fichier situé en dehors du répertoire public.
6. **Impacts.** Lecture/écriture arbitraire de fichiers, divulgation de secrets, parfois exécution.
7. **Détection.** Séquences de traversée et encodages suspects, accès hors périmètre.
8. **Prévention.** Normalisation puis vérification que le chemin résolu reste dans le répertoire autorisé, allowlist de noms, refus des chemins absolus/relatifs, moindre privilège.
9. ⚠️ **Erreur fréquente.** Filtrer « ../ » en surface sans normaliser : les variantes encodées passent.
10. 🎯 **À retenir.** Toujours *normaliser puis vérifier l'appartenance* du chemin résolu au dossier autorisé.

### Chapitre 112 — Unrestricted file upload

1. **Définition.** Upload de fichiers insuffisamment contrôlé, permettant de déposer un fichier dangereux (ex. webshell) ou abusif.
2. **Famille.** Accès aux fichiers / exécution. CWE-434.
3. **Principe.** L'application accepte un fichier sans vérifier type réel, contenu et emplacement de stockage/service ; un fichier exécutable ou actif peut alors être déposé puis déclenché.
4. **Sous-types.** Upload de webshell, contournement d'extension/type MIME (MIME confusion), upload de SVG/HTML actif (XSS — chapitre 91), écrasement de fichiers, archive abusive (Zip Slip — chapitre 113).
5. **Exemple conceptuel.** Un formulaire d'avatar acceptant tout fichier, servi ensuite depuis le domaine principal, permet de déposer un fichier actif déclenché par sa simple consultation.
6. **Impacts.** Exécution de code serveur (webshell), XSS stocké, déni de service (gros fichiers), écrasement de fichiers critiques.
7. **Détection.** Types/extensions inattendus, fichiers actifs uploadés, accès ultérieurs à ces fichiers, alertes EDR.
8. **Prévention.** Validation du *type réel* (pas seulement l'extension), renommage, stockage **hors webroot** ou sur domaine isolé sans exécution, `Content-Disposition`, taille limitée, analyse antivirus, moindre privilège.
9. ⚠️ **Erreur fréquente.** Se fier à l'extension ou au type MIME déclaré par le client (tous deux falsifiables).
10. 🎯 **À retenir.** Un upload mal maîtrisé peut donner un RCE. Valider le contenu réel, stocker hors zone exécutable, servir depuis un domaine isolé.

### Chapitre 113 — Zip Slip (archive extraction abuse)

1. **Définition.** Attaque où l'*extraction d'une archive* écrit des fichiers hors du répertoire cible via des chemins malveillants dans l'archive.
2. **Famille.** Path traversal (chapitre 111) appliqué aux archives. 
3. **Principe.** Les entrées d'une archive peuvent contenir des chemins de traversée ; une extraction qui ne valide pas les destinations écrit des fichiers ailleurs (écrasement de fichiers système/config).
4. **Sous-types.** Selon le format d'archive et le lien symbolique éventuel.
5. **Exemple conceptuel.** Une archive importée contient une entrée dont le chemin remonte hors du dossier d'extraction prévu, visant à écraser un fichier sensible.
6. **Impacts.** Écrasement de fichiers critiques, parfois exécution de code, compromission.
7. **Détection.** Chemins de traversée dans les entrées d'archive, écritures hors du dossier d'extraction.
8. **Prévention.** Valider chaque destination (chemin résolu dans le dossier cible), refuser les chemins absolus/traversants, ignorer les liens symboliques, bibliothèques d'extraction sûres, moindre privilège.
9. ⚠️ **Erreur fréquente.** Extraire une archive en faisant confiance aux chemins qu'elle contient.
10. 🎯 **À retenir.** Toute extraction d'archive doit valider la destination de chaque entrée, comme un path traversal.

### Chapitre 114 — Insecure deserialization

1. **Définition.** Reconstruction d'objets à partir de données sérialisées non fiables, menant à l'altération du comportement ou à l'exécution de code.
2. **Famille.** Désérialisation (chapitre 74) ; OWASP « Software and Data Integrity Failures ». CWE-502.
3. **Principe.** Désérialiser des données contrôlées par l'attaquant peut instancier des objets et déclencher des « chaînes de gadgets » aboutissant à l'exécution de code, surtout avec des formats binaires riches.
4. **Sous-types.** RCE par chaînes de gadgets, manipulation d'objets/état, déni de service.
5. **Exemple conceptuel.** Un jeton d'état sérialisé, modifié par l'attaquant, est désérialisé côté serveur et altère l'exécution.
6. **Impacts.** RCE (fréquent), élévation, contournement de logique, DoS.
7. **Détection.** Données sérialisées modifiées, comportements d'instanciation anormaux, alertes EDR.
8. **Prévention.** Ne pas désérialiser de données non fiables ; formats de données simples (sans types/objets) ; signer/chiffrer les données sérialisées ; allowlist de classes ; mises à jour.
9. ⚠️ **Erreur fréquente.** Transmettre au client des objets sérialisés « pour l'état » puis les désérialiser en confiance.
10. 🎯 **À retenir.** Désérialiser une entrée non fiable = exécuter potentiellement du code étranger. Éviter, ou signer/typer strictement.

### Chapitre 115 — CSRF (Cross-Site Request Forgery)

1. **Définition.** Attaque forçant le navigateur d'une victime *authentifiée* à émettre une requête non voulue vers une application de confiance.
2. **Famille.** Falsification de requêtes côté client / abus de confiance de session. CWE-352.
3. **Principe.** Le navigateur joint automatiquement les cookies de session ; un site malveillant déclenche une requête vers l'application cible, qui l'exécute en croyant qu'elle vient de l'utilisateur.
4. **Sous-types.** CSRF sur actions sensibles (changement d'e-mail, virement), login CSRF, CSRF sur API selon la gestion des jetons.
5. **Exemple conceptuel.** Une page piégée provoque, à l'insu de la victime connectée, une requête de modification de paramètre sur le site cible.
6. **Impacts.** Actions non autorisées au nom de la victime (modification de compte, transactions), parfois prise de contrôle.
7. **Détection.** Requêtes sensibles sans jeton anti-CSRF valide, référents/origines incohérents, schémas inhabituels.
8. **Prévention.** **Jetons anti-CSRF**, cookies `SameSite`, vérification d'origine, ré-authentification pour les actions sensibles, éviter les actions à effet de bord en GET.
9. ⚠️ **Erreur fréquente.** Croire que HTTPS ou l'authentification protègent du CSRF : ils ne le font pas (la requête « semble » légitime).
10. 🎯 **À retenir.** CSRF abuse de la session de la victime : jetons anti-CSRF + `SameSite` + vérification d'origine sont la parade.

### Chapitre 116 — Clickjacking

1. **Définition.** Tromper l'utilisateur pour qu'il clique sur un élément invisible/déguisé, déclenchant une action non voulue.
2. **Famille.** Abus de l'interface / UI redressing. CWE-1021.
3. **Principe.** L'attaquant superpose (souvent via une iframe) le site cible sous une page leurre transparente, de sorte que les clics de la victime atterrissent sur le site cible.
4. **Sous-types.** Clickjacking classique, likejacking, manipulation de glisser-déposer.
5. **Exemple conceptuel.** Un bouton « jouer » d'une page leurre est superposé à une action sensible du site cible chargé en transparence.
6. **Impacts.** Actions non voulues (validation, achat, changement de réglage), souvent couplées à d'autres attaques.
7. **Détection.** Site cible chargé en iframe par des tiers, absence d'en-têtes anti-cadrage.
8. **Prévention.** En-têtes **anti-cadrage** (`X-Frame-Options`/CSP `frame-ancestors`), confirmation explicite des actions sensibles, frame-busting moderne.
9. ⚠️ **Erreur fréquente.** Ne pas définir de politique de cadrage, laissant le site intégrable par n'importe qui.
10. 🎯 **À retenir.** Empêcher le cadrage du site (`frame-ancestors`) neutralise le clickjacking.

### Chapitre 117 — CORS misconfiguration

1. **Définition.** Mauvaise configuration du *partage de ressources entre origines* (CORS), exposant des données à des sites non autorisés.
2. **Famille.** Abus de confiance entre origines. CWE-942.
3. **Principe.** CORS assouplit la politique de même origine ; une configuration trop permissive (origines reflétées sans contrôle, autorisation des identifiants depuis n'importe quelle origine) laisse un site tiers lire des réponses authentifiées.
4. **Sous-types.** Reflet d'origine non validé, wildcard avec identifiants, confiance excessive en sous-domaines.
5. **Exemple conceptuel.** Une API renvoie une autorisation CORS reflétant toute origine *et* autorisant les identifiants, permettant à un site tiers de lire des données privées.
6. **Impacts.** Vol de données authentifiées par un site tiers, contournement de la politique de même origine.
7. **Détection.** En-têtes CORS reflétant des origines arbitraires, wildcard avec credentials, revue de configuration.
8. **Prévention.** Allowlist stricte d'origines, ne pas combiner wildcard et identifiants, valider l'origine côté serveur, limiter les méthodes/en-têtes exposés.
9. ⚠️ **Erreur fréquente.** Refléter dynamiquement l'origine reçue « pour que ça marche » avec les identifiants activés.
10. 🎯 **À retenir.** CORS doit reposer sur une allowlist d'origines ; jamais wildcard + identifiants.

### Chapitre 118 — Open redirect

1. **Définition.** Une fonctionnalité de redirection accepte une *destination contrôlable*, renvoyant l'utilisateur vers un site arbitraire.
2. **Famille.** Validation d'entrée / abus de confiance. CWE-601.
3. **Principe.** L'application redirige vers une URL fournie sans la restreindre ; un lien sur le domaine de confiance renvoie en réalité ailleurs.
4. **Sous-types.** Redirection directe, via paramètre encodé, pivot pour SSRF/OAuth, support de phishing.
5. **Exemple conceptuel.** Un lien de déconnexion qui redirige vers une URL fournie en paramètre est utilisé pour renvoyer la victime vers un site de phishing, tout en partant d'un domaine de confiance.
6. **Impacts.** Phishing crédibilisé, vol de jetons (flux OAuth), pivot SSRF, atteinte à la réputation du domaine.
7. **Détection.** Redirections vers des domaines externes via paramètre, schémas de phishing partant du domaine.
8. **Prévention.** Allowlist de destinations internes, redirections relatives uniquement, validation stricte, page d'avertissement pour les sorties.
9. ⚠️ **Erreur fréquente.** Considérer l'open redirect « mineur » : il crédibilise le phishing et casse des flux OAuth.
10. 🎯 **À retenir.** N'autoriser que des destinations en allowlist (ou relatives). Un open redirect est un multiplicateur d'autres attaques.

### Chapitre 119 — Host header injection

1. **Définition.** Abus de l'en-tête `Host` (ou apparentés) lorsque l'application lui fait confiance pour construire des URL ou prendre des décisions.
2. **Famille.** Rupture de frontière de confiance (chapitre 80) côté HTTP. CWE-644.
3. **Principe.** L'application réutilise un `Host` contrôlable (par ex. pour générer des liens de réinitialisation) ; l'attaquant le falsifie pour empoisonner ces liens ou contourner des contrôles.
4. **Sous-types.** Empoisonnement de liens (réinitialisation de mot de passe), routage/cache trompé, contournement d'autorisation basée sur l'hôte.
5. **Exemple conceptuel.** Un e-mail de réinitialisation construit son lien à partir du `Host` reçu ; falsifié, le lien pointe vers un domaine attaquant qui capte le jeton.
6. **Impacts.** Vol de jetons de réinitialisation, prise de comptes, empoisonnement de cache, contournement.
7. **Détection.** Valeurs de `Host` incohérentes avec le domaine attendu, liens générés anormaux.
8. **Prévention.** Ne pas faire confiance au `Host` ; utiliser une valeur canonique configurée côté serveur ; allowlist d'hôtes ; valider les en-têtes.
9. ⚠️ **Erreur fréquente.** Construire des liens absolus à partir de l'en-tête `Host` de la requête.
10. 🎯 **À retenir.** L'en-tête `Host` est contrôlable par le client : reposer dessus pour des décisions sensibles est une faille. Utiliser une valeur canonique fixe.

### Chapitre 120 — HTTP request smuggling

1. **Définition.** Attaque exploitant des *désaccords d'interprétation* des limites de requêtes HTTP entre deux serveurs en chaîne (frontal et back-end).
2. **Famille.** Erreurs de parsing (chapitre 75) au niveau protocole.
3. **Principe.** Quand le frontal et le back-end délimitent différemment les requêtes (longueur vs encodage par morceaux), l'attaquant « cache » une requête à l'un qui sera traitée par l'autre, désynchronisant le flux.
4. **Sous-types.** Selon l'incohérence exploitée entre composants ; variantes de désynchronisation.
5. **Exemple conceptuel.** Deux composants comptent différemment où finit une requête, si bien qu'un fragment est interprété comme une requête supplémentaire par le back-end.
6. **Impacts.** Contournement de contrôles, empoisonnement de cache, capture de requêtes d'autres utilisateurs, détournement de session.
7. **Détection.** Anomalies de framing HTTP, réponses désynchronisées, outils de détection spécialisés, journaux incohérents.
8. **Prévention.** Cohérence stricte du traitement HTTP entre composants, normalisation au frontal, rejet des requêtes ambiguës, configurations à jour, HTTP/2 de bout en bout bien configuré.
9. ⚠️ **Erreur fréquente.** Empiler des serveurs/proxys aux interprétations HTTP divergentes sans normalisation.
10. 🎯 **À retenir.** Le smuggling naît du désaccord entre serveurs sur « où finit une requête ». Normaliser et rejeter l'ambiguïté.

### Chapitre 121 — Cache poisoning

1. **Définition.** Empoisonnement d'un *cache* (web/CDN) pour servir un contenu malveillant à de nombreux utilisateurs.
2. **Famille.** Abus d'infrastructure web / parsing. CWE-444 apparenté.
3. **Principe.** Si le cache utilise comme clé une partie de la requête, mais que la réponse dépend d'éléments *non inclus dans la clé* (en-têtes non clés), l'attaquant peut faire stocker une réponse empoisonnée servie ensuite à tous.
4. **Sous-types.** Via en-têtes non clés, via paramètres ignorés par la clé, couplé à host header injection ou smuggling.
5. **Exemple conceptuel.** Un en-tête influençant la réponse mais ignoré par la clé de cache permet de faire mémoriser une version altérée de la page.
6. **Impacts.** Diffusion massive de contenu malveillant (XSS, redirection), déni de service, atteinte à l'intégrité.
7. **Détection.** Réponses en cache incohérentes, en-têtes inattendus influençant la réponse, surveillance du CDN.
8. **Prévention.** Inclure dans la clé de cache *tous* les éléments influençant la réponse, normaliser les entrées, durcir la configuration du cache, isoler les contenus dynamiques.
9. ⚠️ **Erreur fréquente.** Laisser des en-têtes influencer la réponse sans les inclure dans la clé de cache.
10. 🎯 **À retenir.** Tout ce qui modifie la réponse doit faire partie de la clé de cache, sinon le cache devient un amplificateur d'attaque.

### Chapitre 122 — Web cache deception

1. **Définition.** Tromper le cache pour qu'il stocke une page *contenant des données privées*, ensuite accessible à l'attaquant.
2. **Famille.** Abus d'infrastructure web (proche du cache poisoning, intention inverse).
3. **Principe.** En faisant croire au cache qu'une page dynamique privée est une ressource statique « cachable », l'attaquant l'amène à stocker la version personnalisée d'une victime, qu'il récupère ensuite.
4. **Sous-types.** Via extensions/chemins trompeurs, via règles de cache trop larges.
5. **Exemple conceptuel.** Une URL construite pour ressembler à une ressource statique amène le cache à mémoriser une page de profil personnalisée.
6. **Impacts.** Fuite de données privées d'autres utilisateurs, exposition d'informations de session.
7. **Détection.** Mise en cache de réponses authentifiées/personnalisées, règles de cache incohérentes.
8. **Prévention.** Ne jamais mettre en cache les réponses authentifiées/personnalisées, règles de cache strictes basées sur le type réel, en-têtes de cache explicites, normalisation des chemins.
9. ⚠️ **Erreur fréquente.** Règles « tout ce qui ressemble à du statique est cachable » sans vérifier le caractère privé de la réponse.
10. 🎯 **À retenir.** Le contenu privé ne doit jamais être mis en cache : des règles de cache précises évitent que des données personnelles soient partagées.

### Chapitre 123 — Prototype pollution

1. **Définition.** Attaque (écosystème JavaScript) altérant le *prototype partagé* des objets, modifiant le comportement global de l'application.
2. **Famille.** Rupture d'intégrité d'objets / injection de propriétés. CWE-1321.
3. **Principe.** En injectant des propriétés spéciales lors de fusions/copies d'objets non sécurisées, l'attaquant pollue le prototype hérité par tous les objets, ce qui peut altérer la logique, contourner des contrôles, voire mener à du XSS/RCE selon le contexte.
4. **Sous-types.** Côté client (vers XSS) et côté serveur (vers contournement/RCE), via fusion profonde, parsing, ou paramètres imbriqués.
5. **Exemple conceptuel.** Une fusion récursive d'un objet d'entrée injecte une propriété héritée qui modifie une valeur par défaut utilisée ailleurs dans l'application.
6. **Impacts.** Contournement de logique, déni de service, XSS, parfois RCE.
7. **Détection.** Propriétés spéciales dans les entrées, comportements globaux anormaux, audit des opérations de fusion/copie.
8. **Prévention.** Bloquer les clés dangereuses, objets sans prototype pour les données, fonctions de fusion sûres, validation de schéma, bibliothèques à jour, gel des prototypes le cas échéant.
9. ⚠️ **Erreur fréquente.** Fusionner récursivement des entrées non fiables dans des objets sans filtrer les clés spéciales.
10. 🎯 **À retenir.** La pollution de prototype contamine *tous* les objets : filtrer les clés dangereuses et n'utiliser que des fusions sûres.

### Chapitre 124 — Rate limit bypass

1. **Définition.** Contournement des mécanismes de *limitation de débit*, réactivant les attaques par répétition massive.
2. **Famille.** Abus / contournement de contrôle (lié au chapitre 79).
3. **Principe.** Si la limitation s'appuie sur un critère manipulable (en-tête d'IP falsifiable, casse d'URL, paramètres, comptes multiples), l'attaquant la contourne et reprend brute force, énumération ou scraping.
4. **Sous-types.** Via rotation d'IP/en-têtes, via variations d'URL/paramètres, via parallélisme, via comptes multiples.
5. **Exemple conceptuel.** Une limite appliquée selon un en-tête d'adresse falsifiable est contournée en variant cet en-tête à chaque requête.
6. **Impacts.** Réactivation du brute force/credential stuffing, énumération, déni de service, surcoûts.
7. **Détection.** Volume élevé malgré la limite, variations systématiques des critères de limitation, distribution d'IP anormale.
8. **Prévention.** Limiter sur des critères fiables (identité authentifiée, jetons), ne pas se fier aux en-têtes client, limitation côté serveur/passerelle, détection d'anomalies, défenses combinées.
9. ⚠️ **Erreur fréquente.** Limiter sur un en-tête d'IP fourni par le client (falsifiable) au lieu d'une source fiable.
10. 🎯 **À retenir.** Une limitation contournable n'en est pas une : s'appuyer sur des critères non manipulables.

### Chapitre 125 — Business logic abuse

1. **Définition.** Détournement du *fonctionnement légitime* de l'application pour obtenir un avantage non prévu, sans faille technique.
2. **Famille.** Logique métier (chapitre 72) côté attaque.
3. **Principe.** L'attaquant respecte la « technique » mais abuse des règles : ordre des étapes, cumuls, valeurs limites, conditions de course métier, automatisation d'actions prévues pour être manuelles.
4. **Sous-types.** Abus de remises/cumuls, contournement de workflow, manipulation de quantités/prix, exploitation de la concurrence (chapitre 73), automatisation abusive.
5. **Exemple conceptuel.** Enchaîner des étapes dans un ordre non prévu pour obtenir un bien sans franchir l'étape de paiement.
6. **Impacts.** Fraude, perte financière, contournement de contrôles, avantage indu — invisibles aux scanners.
7. **Détection.** Schémas d'usage anormaux, séquences d'actions atypiques, écarts métier, supervision fonctionnelle.
8. **Prévention.** Threat modeling métier, validation des règles et de l'ordre des étapes côté serveur, contrôles de cohérence, plafonds, idempotence, tests orientés abus, surveillance comportementale.
9. ⚠️ **Erreur fréquente.** Tester uniquement « est-ce que ça marche comme prévu », jamais « comment quelqu'un pourrait en abuser ».
10. 🎯 **À retenir.** L'abus de logique métier n'est pas un bug, c'est un usage détourné : seuls la réflexion métier et les tests d'abus le révèlent.

### Chapitre 126 — GraphQL abuse

1. **Définition.** Attaques propres aux API *GraphQL*, exploitant leur flexibilité de requêtage.
2. **Famille.** Abus d'API (Partie 10) appliqué à GraphQL.
3. **Principe.** GraphQL laisse le client composer ses requêtes (champs, profondeur, relations) ; sans garde-fous, cela ouvre la porte à la surcharge, à l'exposition excessive de données et au contournement d'autorisation par champ.
4. **Sous-types.** Requêtes profondes/imbriquées (DoS), introspection révélant le schéma, exposition excessive de champs, autorisation manquante au niveau champ/objet (BOLA/BFLA), batching abusif.
5. **Exemple conceptuel.** Une requête très imbriquée force le serveur à parcourir des relations en cascade, saturant les ressources.
6. **Impacts.** Déni de service, fuite de données (champs/objets non autorisés), reconnaissance via introspection.
7. **Détection.** Requêtes anormalement profondes/coûteuses, introspection en production, volumes inhabituels.
8. **Prévention.** Limites de profondeur/complexité/coût, autorisation *par champ et par objet*, désactivation/contrôle de l'introspection en production, limitation de débit, pagination obligatoire, validation de schéma.
9. ⚠️ **Erreur fréquente.** Exposer GraphQL avec introspection ouverte et sans limite de complexité ni contrôle d'autorisation fin.
10. 🎯 **À retenir.** La flexibilité de GraphQL est sa surface d'attaque : limiter la complexité et contrôler l'autorisation au niveau champ/objet.

---

> **Fin du Volume 3/8.**
>
> Vous disposez désormais d'une taxonomie complète des attaques web (chapitres 82–126), reliées à leurs familles, impacts, signaux de détection et défenses. Toutes se ramènent aux sept familles de la vue d'ensemble — et, plus en amont, aux familles de vulnérabilités de la Partie 5.
>
> **Suite — Volume 4 : Partie 7, Attaques réseau et infrastructure** (reconnaissance, sniffing, spoofing ARP/DNS/DHCP, MITM, replay, downgrade, exploitation de services, SMB/RDP/VPN, pivoting, mouvement latéral, DoS/DDoS, amplification/reflection, botnets, VLAN hopping, Wi-Fi evil twin, rogue AP, deauth, BGP hijacking).


---


## Taxonomie de la cybersécurité — Volume 4/8

> Partie 7 : Attaques réseau et infrastructure
>
> On quitte la couche applicative pour la couche réseau (chapitre 42). Ici, les attaques visent les *protocoles*, les *flux* et les *équipements*. Le fil conducteur : un attaquant qui a un pied dans le réseau (ou à proximité) cherche à *écouter*, *usurper*, *se déplacer* et *perturber*. Format en 10 points pour les attaques majeures.
>
> **Posture** : mécanismes et défenses, pas de procédure offensive opérationnelle.

---
