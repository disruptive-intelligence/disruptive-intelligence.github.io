---
title: PARTIE V — Les flux
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 6
chapters: 10
---

> **Le cœur du cours.** Sept chapitres, un par chose qui circule.
>
> **Pourquoi cette partie compte plus que les autres** : reconnaître un composant s'apprend en une heure. Suivre ce qui circule à travers dix composants, y compris ce qui n'est pas dessiné, est la compétence qui distingue un lecteur d'un spectateur.
>
> **Rappel du principe des trois flux** — trois familles, et ne jamais les confondre :
>
> | Famille | Question | Si elle s'arrête |
> |---|---|---|
> | **Métier** | Que transporte le service ? | Le service ne rend plus son objet |
> | **Dépendance** | Sans quoi ne peut-il pas s'établir ? | **Le service s'arrête, sans qu'on comprenne pourquoi** |
> | **Exploitation** | Comment tient-on, observe-t-on, restaure-t-on ? | Le service continue · **on devient aveugle** |

---

## Chapitre 29 — Suivre une requête

### 29.1 Les douze étapes d'une requête ordinaire

Un salarié tape une adresse dans son navigateur. Voici ce qui se passe réellement — et **sur ces douze étapes, cinq figurent au schéma**.

🖼 **SCHÉMA 29.1 — Une requête, de bout en bout** · *Version graphique : douze étapes numérotées, les flux de dépendance en pointillé d'une autre couleur.*

```
 ①  Le poste doit traduire le nom en adresse
        poste ┄┄┄► [ résolution de noms ]        ← DÉPENDANCE
 ②  Réponse : une adresse
 ③  Le poste ouvre une connexion vers cette adresse
        poste ────► [ pare-feu ]                 ← peut refuser
 ④  Traversée du filtrage
        [ pare-feu ] ────► [ mandataire inverse ]
 ⑤  Négociation du chiffrement
        poste ┄┄┄► validation du certificat      ← DÉPENDANCE
 ⑥  Le mandataire termine la connexion et en ouvre une autre
 ⑦  Le mandataire demande une authentification
        [ mandataire ] ┄┄┄► [ annuaire ]         ← DÉPENDANCE
 ⑧  Le répartiteur choisit un serveur web
        [ répartiteur ] ────► [ web 2 ]
 ⑨  Le serveur web transmet à l'applicatif
        [ web 2 ] ────► [ applicatif ]
 ⑩  L'applicatif vérifie les droits, interroge la base
        [ applicatif ] ────► [ base ]
 ⑪  Dans cette architecture simplifiée, la réponse suit le chemin inverse
 ⑫  Chaque composant traversé écrit un journal
        chacun ┄┄┄► [ collecte ]                 ← EXPLOITATION
```

⚠️ **Sur l'étape ⑪** : le chemin de retour identique est vrai **dans cette architecture**, où chaque composant termine la connexion et en ouvre une autre. Ce n'est pas une règle générale — un routage asymétrique, un réseau de diffusion de contenu, un cache intermédiaire ou une architecture distribuée produisent des chemins de retour différents, **et c'est précisément ce qui rend certains diagnostics difficiles**.

### 29.2 Ce que le schéma d'architecture montre de tout cela

| Étape | Sur le schéma 1.1 ? |
|---|---|
| ①② résolution de noms | ❌ |
| ③④ pare-feu | ✅ |
| ⑤ certificat | ❌ |
| ⑥ mandataire inverse | ✅ |
| ⑦ authentification | ❌ |
| ⑧ répartiteur | ✅ |
| ⑨⑩ web, applicatif, base | ✅ |
| ⑫ journalisation | ❌ |

**Cinq étapes visibles sur douze.** Et les sept invisibles comprennent **les trois qui peuvent faire échouer la requête sans qu'aucun composant dessiné ne soit en panne**.

⚠️ **PIÈGE — le diagnostic par le schéma**
Face à une requête qui échoue, un lecteur qui ne connaît que le schéma cherche parmi cinq composants. Un lecteur exercé en examine douze — et commence souvent par ceux qui ne sont pas dessinés, parce que ce sont ceux dont la panne est la moins visible.

### 29.3 Le même service, quatre chemins différents

**C'est la section qui change la lecture d'un schéma**, et elle est rarement enseignée.

🖼 **SCHÉMA 29.2 — Quatre chemins vers le même service**

```
  ① UTILISATEUR EXTERNE
     Internet ──► [ FW ] ──► [ mandataire ] ──► [ web ] ──► [ app ]
     → passe par TOUS les contrôles
     → authentifié en amont · journalisé au mandataire · inspecté

  ② UTILISATEUR INTERNE
     poste ──────────────────────────────────► [ web ] ──► [ app ]
     → NE PASSE PAS par le mandataire
     → la résolution interne renvoie l'adresse du serveur — §14.5
     → aucun des contrôles du mandataire ne s'applique

  ③ UTILISATEUR NOMADE
     poste ══tunnel══► réseau interne ─────────► [ web ]
        OU
     poste ──► Internet ──► [ mandataire ] ──► [ web ]
     → DEUX chemins possibles selon la configuration
     → et souvent, personne ne sait lequel est emprunté

  ④ APPEL ENTRE SERVEURS
     [ autre application ] ─────────────────────► [ app ]
     → pas d'utilisateur · pas de mandataire
     → authentification par certificat ou par secret — §33
     → souvent le chemin le moins contrôlé de tous
```

| Chemin | Contrôles traversés | Journalisé où |
|---|---|---|
| ① Externe | Pare-feu · mandataire · application | Trois endroits |
| ② Interne | **Application seulement** | Un endroit |
| ③ Nomade | Variable, selon le chemin | Variable |
| ④ Serveur à serveur | **Souvent aucun** | Application, si elle le fait |

⚠️ **Ce que ce tableau impose en lecture** : un schéma dessine généralement le chemin ①. **C'est le mieux contrôlé, et c'est le moins fréquent en volume.** Les chemins ② et ④ portent l'essentiel du trafic réel, et ils traversent le moins de contrôles.

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous placez un dispositif de contrôle sur le mandataire inverse. Est-ce que tous les accès au service sont contrôlés ?*
**Non — seulement les accès externes.** Les postes internes atteignent souvent le serveur directement, sans traverser le mandataire, parce que la résolution interne leur donne l'adresse du serveur. La mauvaise décision évitée : **croire qu'un contrôle placé sur un chemin couvre tous les chemins**, et découvrir en incident que la compromission est passée par l'intérieur. C'est le chapitre 44.

### 29.4 Reconstituer un chemin quand on n'a pas le schéma

**La méthode, en quatre questions** — utilisable en réunion, sans document :

```
1. D'où part la demande ?     poste interne · Internet · autre serveur
2. Quel NOM est demandé ?     → quelle vue de résolution s'applique ?
3. Que répond ce nom          → l'adresse du mandataire, ou celle du serveur ?
   depuis CET endroit ?
4. Que traverse-t-on          → chaque frontière est un point de contrôle
   entre les deux ?              et un point de journalisation
```

⚠️ **La question 3 est celle qui révèle le plus.** Deux personnes qui demandent le même nom depuis deux endroits différents peuvent obtenir deux adresses différentes — et donc suivre deux chemins avec deux niveaux de contrôle. **Un schéma ne peut pas exprimer cela.**

### 29.5 Ce qui casse une requête, par étape

| Étape | Ce qui peut échouer | Symptôme caractéristique |
|---|---|---|
| ①② | Résolution indisponible ou mauvaise réponse | « Le site n'existe pas » · panne par vagues — §14.7 |
| ③④ | Règle de pare-feu, ou flux jamais ouvert | Délai d'attente, sans message |
| ⑤ | Certificat expiré, chaîne non reconnue | Avertissement de sécurité · **panne à un horaire net, sans intervention** — §17.4 |
| ⑥ | Mandataire arrêté ou saturé | Erreur immédiate, seulement de l'extérieur |
| ⑦ | Annuaire indisponible | Authentification refusée · cascade progressive — §16.3 |
| ⑧ | Tous les membres retirés par le contrôle de santé | **Le service tombe alors que les serveurs vont bien** — §13.2 |
| ⑨⑩ | Applicatif ou base indisponible | La page s'affiche, les actions échouent — §19.4 |

**Ce tableau est un outil de diagnostic à lui seul.** Le symptôme désigne l'étape, et l'étape désigne le composant — y compris quand il n'est pas dessiné.

---

## Chapitre 30 — Suivre une authentification

> Le flux de dépendance le plus universel, et le moins représenté.

### 30.1 Trois questions à ne jamais confondre

**La distinction que presque personne ne fait, et qui structure tout le chapitre** :

| Question | Nom | Où elle se traite |
|---|---|---|
| **Qui es-tu ?** | Authentification | Annuaire, fournisseur d'identité, mandataire |
| **As-tu le droit de faire ceci ?** | Autorisation | **L'application, presque toujours** |
| **Qu'as-tu fait ?** | Traçabilité | L'application, et les journaux |

⚠️ **Confondre les deux premières est une erreur de lecture courante sur ce sujet.** Un mandataire qui authentifie sait *qui* entre ; il ne sait pas *ce que cette personne a le droit de faire*. **L'autorisation reste dans l'application** — et c'est pourquoi une faille d'autorisation n'est pas rattrapée par un mandataire, si bien configuré soit-il.

### 30.2 Où l'on prouve son identité, et combien de fois

**Le constat** : dans une journée ordinaire, un utilisateur s'authentifie bien plus souvent qu'il ne le croit — et la plupart de ces authentifications sont invisibles.

| Moment | Contre quoi | Visible ? |
|---|---|---|
| Ouverture de session du poste | Annuaire | ✅ |
| Montage des lecteurs réseau | Annuaire | ❌ |
| Ouverture de la messagerie | Annuaire ou service en ligne | ❌ |
| Accès à une application interne | Annuaire, via le mandataire | ❌ |
| Accès à un service en ligne | Fédération ou compte propre | Selon |
| Appel d'un serveur vers un autre | Certificat ou secret — §33 | ❌ |
| Accès d'un administrateur | Second facteur, compte distinct | ✅ |

**Dans cet exemple, six des sept authentifications sont invisibles pour l'utilisateur**, et toutes dépendent d'un composant que le schéma ne montre pas.

### 30.3 Ce qui se passe quand l'annuaire tombe

🖼 **SCHÉMA 30.1 — La cascade**

```
   T+0        L'annuaire cesse de répondre
              │
   T+0        Les sessions ouvertes CONTINUENT     ← rien ne se voit
              │
   T+minutes  Toute nouvelle authentification échoue
              │  · nouveaux accès aux partages
              │  · connexions applicatives
              │
   T+heures   Les jetons expirent, les sessions tombent une à une
              │
   Au premier Un utilisateur ne peut plus ouvrir sa session.
   redémarrage Il est bloqué devant son poste.
```

⚠️ **La cascade est progressive, et c'est ce qui la rend difficile à diagnostiquer.** Pendant les premières minutes, la majorité des utilisateurs ne constate rien. Les signalements arrivent par vagues, sur des symptômes différents, et rien ne les relie apparemment.

🔥 **SCÉNARIO — l'annuaire répond, personne ne peut se connecter**

| Question | Réponse |
|---|---|
| Symptôme | Les contrôleurs répondent aux requêtes de test. Les ouvertures de session échouent |
| Hypothèse naïve | « L'annuaire est en panne » |
| Dépendance réelle | **La résolution de noms** : le poste ne trouve plus ses contrôleurs — §16.2 |
| Ce que le schéma aurait dû montrer | Que l'annuaire se localise par la résolution de noms |
| Comment le reconnaître | Interroger le contrôleur **par son adresse** fonctionne · par son nom, non |

⚠️ **C'est le chemin de diagnostic le plus difficile du cours** : deux composants invisibles, et l'un dépend de l'autre.

### 30.4 Les trois modèles d'authentification

```
  A — CHAQUE APPLICATION AUTHENTIFIE
      [ app 1 : ses comptes ]  [ app 2 : ses comptes ]  [ app 3 : ... ]
      → aucune dépendance commune : une panne n'affecte qu'une application
      → autant de bases d'identités que d'applications
      → un départ suppose N suppressions, et il y en aura N-2

  B — AUTHENTIFICATION CENTRALISÉE
      [ app 1 ] [ app 2 ] [ app 3 ] ──► [ annuaire ]
      → un départ = une action · une politique commune
      → ⚠️ UNE DÉPENDANCE UNIVERSELLE
      → une compromission de l'annuaire donne tout

  C — FÉDÉRATION
      [ app ] ──► [ fournisseur d'identité ] ──► [ annuaire interne ]
                          (souvent externe)
      → fonctionne pour des applications hors de votre réseau
      → ⚠️ la dépendance sort de l'organisation
      → si le fournisseur est indisponible, VOUS ne pouvez rien faire
```

| Modèle | Départ d'un salarié | Panne du composant central | Maîtrise |
|---|---|---|---|
| **A** | N actions, et des oublis | Une application seulement | Complète |
| **B** | Une action | **Tout est bloqué** | Complète |
| **C** | Une action | **Tout est bloqué, et vous n'y pouvez rien** | Partielle |

⚠️ **Le modèle C déplace la dépendance hors de l'organisation.** C'est un arbitrage classique : on gagne en simplicité et en fonctionnalités, on perd la maîtrise de la disponibilité. **Principe du coût.**

### 30.5 Le second facteur, et où il se place

| Placement | Ce qu'il protège | Ce qu'il ne protège pas |
|---|---|---|
| À l'ouverture de session du poste | L'accès au poste | Ce qui est déjà ouvert |
| Au mandataire inverse | Les accès **externes** | **Les accès internes directs** — §29.3 |
| Dans l'application | Cette application | Les autres |
| À l'accès distant | L'entrée sur le réseau | Ce qui se passe ensuite |

⚠️ **La deuxième ligne est une erreur de conception courante sur ce sujet** : placer le second facteur au mandataire, et croire l'application protégée. **Un poste interne l'atteint sans passer par là.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a du SSO » | Une authentification unique existe | **Contre quoi ? Pour quelles applications ? Et les autres ?** |
| « C'est fédéré » | Modèle C | **Le fournisseur est-il externe ? Que fait-on s'il tombe ?** |
| « On a mis du MFA » | Un second facteur | **Placé où ?** Il ne protège que ce qui passe par lui |
| « Il a les droits » | Confusion authentification / autorisation | **Qui les lui a donnés, et où sont-ils vérifiés ?** |

⚖️ **CONTRAINTE ET COÛT — l'authentification centralisée**

| Résout | Coûte |
|---|---|
| Une identité unique, des droits gérés en un point | **Une dépendance universelle** |
| Retirer un accès partout en une action | Une panne qui bloque tout progressivement |
| Appliquer une politique commune | Une compromission qui donne accès à tout |

---

## Chapitre 31 — Suivre une session

### 31.1 Ce qu'une session change

**Le problème** : la plupart des échanges web sont **sans mémoire**. Chaque requête arrive sans savoir ce qui la précède. Il faut donc un mécanisme pour se souvenir qu'un utilisateur est déjà authentifié.

**Ce mécanisme — un jeton, un cookie — a une conséquence d'architecture majeure** :

> **Là où la session est stockée détermine ce que la redondance peut réellement apporter.**

### 31.2 Les trois emplacements possibles

🖼 **SCHÉMA 31.1 — Où vit la session, et ce que ça change**

```
  A — SESSION LOCALE AU SERVEUR
      [web 1] session ici
      [web 2]                ← si l'utilisateur bascule ici : DÉCONNECTÉ
      → la redondance existe, elle ne protège pas l'utilisateur

  B — SESSION PARTAGÉE
      [web 1] ──┐
      [web 2] ──┼──► [ magasin de sessions ]
      [web 3] ──┘
      → bascule transparente · MAIS un composant de plus,
        et un nouveau point de rupture

  C — SESSION CHEZ LE CLIENT
      Le jeton est porté par le navigateur, signé, non stocké côté serveur
      → aucune dépendance à un magasin central
      → MAIS la révocation immédiate exige de réintroduire
        un mécanisme d'état ou de contrôle
```

| Modèle | Redondance réelle ? | Révocation immédiate ? | Composant de plus ? |
|---|---|---|---|
| **A — locale** | ❌ Apparente seulement | ✅ | Non |
| **B — partagée** | ✅ | ✅ | **Oui, et il devient critique** |
| **C — chez le client** | ✅ | ⚠️ **Différée, ou au prix d'un état réintroduit** | Non |

⚠️ **Le modèle A explique de nombreuses architectures où la redondance ne tient pas ses promesses.** Trois serveurs, un répartiteur, et pourtant les utilisateurs sont déconnectés dès qu'un serveur redémarre. Le schéma montre une redondance ; le comportement en session la contredit.

📌 **Le vrai compromis du modèle C**, plus intéressant que « on ne peut pas révoquer » :

Un jeton autoporté est vérifiable sans interroger personne — c'est tout son intérêt. **Le revers est qu'il reste valide jusqu'à son expiration, même si l'on souhaite l'invalider avant.** Plusieurs stratégies rétablissent une révocation, et **chacune réintroduit une part de ce que le modèle C cherchait à éviter** :

| Stratégie | Ce qu'elle réintroduit |
|---|---|
| Durée de vie très courte + renouvellement | Des appels fréquents au service d'émission |
| Liste de jetons révoqués | Un état partagé à consulter |
| Numéro de version de session | Une consultation à chaque requête |
| Introspection du jeton | Une dépendance au service d'émission |
| Révocation du jeton de renouvellement | Une révocation **différée**, pas immédiate |

⚠️ **C'est un compromis d'architecture, pas une impossibilité technique.** La question n'est pas *« peut-on révoquer ? »* mais **« à quel prix, et sous quel délai ? »**

### 31.3 Le magasin de sessions, composant invisible et critique

**Le modèle B ajoute un composant qui n'apparaît sur presque aucun schéma**, et qui a trois propriétés :

| Propriété | Conséquence |
|---|---|
| **Toutes les requêtes le consultent** | Une latence ajoutée à chaque requête |
| **Sa panne déconnecte tout le monde** | **Un point de rupture qui n'est pas dessiné** |
| Il contient les sessions actives | **Sa compromission permet d'usurper des sessions en cours** |

🔥 **SCÉNARIO — tout le monde est déconnecté d'un coup**

| Question | Réponse |
|---|---|
| Symptôme | Tous les utilisateurs sont déconnectés simultanément. Les serveurs web vont bien |
| Hypothèse naïve | « Un redémarrage applicatif » |
| Dépendance réelle | **Le magasin de sessions** — modèle B |
| Ce que le schéma aurait dû montrer | Ce composant, et le fait que toutes les requêtes le traversent |
| Concevoir différemment | Le redonder · ou accepter le modèle A avec ses limites, en le sachant |

### 31.4 Où passe le jeton, et où il fuit

| Endroit | Risque |
|---|---|
| Dans le navigateur | Vol par une extension, par un logiciel malveillant sur le poste |
| Dans les journaux | **S'il apparaît dans une adresse consultée, il est journalisé partout** |
| Chez le mandataire inverse | Il le voit en clair, en modes B et C — §12.3 |
| Dans les caches intermédiaires | Un jeton mis en cache peut être servi à un autre |

**La deuxième ligne est un cas d'école** : un jeton passé dans une adresse est enregistré par le poste, le mandataire, le pare-feu, le serveur web et la collecte de journaux. **Il devient lisible par tous ceux qui ont accès aux journaux** — et c'est le chapitre 34.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a de la persistance de session » | Le répartiteur renvoie sur le même serveur | **Modèle A** — la redondance ne protège pas les sessions |
| « Les sessions sont dans Redis » | Modèle B | **Le magasin est-il redondé ? Il n'est sur aucun schéma** |
| « On utilise des JWT » | Modèle C | **Quelle durée de vie ? Comment révoque-t-on ?** |
| « Les gens se font déconnecter » | Symptôme | **Tous en même temps, ou un tiers ?** La réponse désigne le modèle |

⚠️ **La dernière ligne est un excellent outil de diagnostic** : *tous en même temps* désigne le magasin partagé · *un tiers seulement* désigne un serveur redémarré avec des sessions locales.

---

## Chapitre 32 — Suivre une donnée

> **Principe 6 : le système d'information n'existe que pour traiter de la donnée.** Ce chapitre suit un enregistrement de sa création à sa destruction.

### 32.1 Le cycle complet

🖼 **SCHÉMA 32.1 — Une donnée, de la saisie à l'oubli**

```
  ①  SAISIE          poste utilisateur
  ②  TRANSIT         mandataire · web · applicatif
  ③  STOCKAGE        base de données
  ④  RÉPLICATION     base secondaire, éventuellement autre site
  ⑤  SAUVEGARDE      support de sauvegarde, souvent hors ligne
  ⑥  COPIE           export, tableur, rapport, environnement de recette
  ⑦  DIFFUSION       courriel, partage de fichiers, service en ligne
  ⑧  ARCHIVAGE       stockage long terme
  ⑨  SUPPRESSION     de la base — mais pas des copies
```

⚠️ **L'étape ⑨ ne supprime que ⑨.** Une donnée effacée de la base subsiste dans les sauvegardes, les réplicas, les exports, les courriels et les environnements de recette. **C'est le principal écart entre la suppression déclarée et la suppression réelle.**

### 32.2 Les copies qu'on ne voit jamais

| Copie | Où elle naît | Pourquoi elle échappe |
|---|---|---|
| **L'environnement de recette** | Copie de production pour tester | **Contient de vraies données, avec des protections moindres** |
| **L'export tableur** | Un utilisateur qui extrait | Part sur un poste, un partage, un courriel |
| **La sauvegarde** | Automatique | Souvent conservée bien au-delà du besoin |
| **Le cache** | Intermédiaires techniques | Invisible et temporaire — mais réel |
| **Le rapport** | Outil décisionnel | Une seconde base, avec ses propres droits |
| **Le journal applicatif** | La journalisation elle-même | **Il peut contenir la donnée** — §31.4 |
| **La messagerie** | Un fichier envoyé une fois | Conservé indéfiniment, chez l'expéditeur et le destinataire |

**La première ligne est la plus significative en sécurité** : un environnement de recette contient les données de production avec des protections inférieures, et il est **presque toujours hors du périmètre des schémas et des inventaires**.

⚠️ **La sixième mérite d'être signalée** : une application qui journalise le contenu de ses requêtes pour faciliter le diagnostic **duplique la donnée dans un système dont la rétention et les droits sont différents**. C'est une copie que personne n'a décidée.

### 32.3 Ce qui multiplie les copies sans qu'on le décide

| Mécanisme | Combien de copies il crée |
|---|---|
| Une réplication de base | +1, en permanence |
| Une sauvegarde quotidienne conservée 30 jours | **+30** |
| Un environnement de recette rafraîchi mensuellement | +1, à jour d'un mois |
| Un outil décisionnel | +1, avec ses propres droits |
| Un export mensuel envoyé par courriel | **+N, indéfiniment** |

⚠️ **Le calcul est instructif.** Une base unique, sauvegardée quotidiennement sur trente jours, répliquée, copiée en recette et alimentant un outil décisionnel, **existe en trente-quatre exemplaires** — dont trente-trois ne sont sur aucun schéma.

### 32.4 Le chemin de la sauvegarde, et pourquoi il compte

**Un flux d'exploitation qui n'apparaît nulle part, et qui est le plus transverse de l'architecture.**

```
   [ base ] ◄──── [ serveur de sauvegarde ] ────► [ support ]
       ▲                    │                        │
       │                    │  il atteint AUSSI :    │
       │                    ├──► serveurs de fichiers │
       │                    ├──► machines virtuelles  │
       │                    └──► annuaire             │
       │                                              │
   Trois questions :
      ① Qui initie ? (§3.6 — la sauvegarde, presque toujours)
      ② Avec quel compte ? (il atteint tout, donc il peut tout lire)
      ③ Le support est-il atteignable depuis le réseau ?
```

⚠️ **La troisième question décide de la gravité d'un rançongiciel.** Une sauvegarde atteignable en écriture depuis un compte compromis est chiffrée avec le reste. **C'est le scénario du §21.4**, et c'est ce qui distingue un incident d'une catastrophe.

🔥 **SCÉNARIO — la donnée effacée réapparaît**

| Question | Réponse |
|---|---|
| Symptôme | Une donnée supprimée sur demande réapparaît trois mois plus tard |
| Hypothèse naïve | « Une erreur de manipulation » |
| Dépendance réelle | **Une restauration partielle depuis une sauvegarde antérieure à la suppression** |
| Ce que le schéma aurait dû montrer | Le cycle complet, et les points où la donnée persiste |
| Concevoir différemment | Traiter la suppression comme un **processus sur toutes les copies**, pas comme une action sur la base |

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous devez évaluer l'impact d'une compromission de la base de production. Où cherchez-vous ?*
**Pas seulement dans la base.** Vous listez les neuf étapes : où sont les réplicas, les sauvegardes, la recette, les exports, les rapports, les journaux. Dans la majorité des cas, **la donnée existe en plusieurs endroits**, dont plusieurs ne sont sur aucun schéma. La mauvaise décision évitée : **déclarer un périmètre d'impact qui ne couvre qu'une fraction des copies**, et devoir le corriger publiquement quelques jours plus tard.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « La donnée a été supprimée » | Effacée de la base | **Et les sauvegardes ? La recette ? Les exports ?** |
| « La recette est une copie de prod » | Données réelles hors production | **Avec quelles protections ? Qui y a accès ?** |
| « On sauvegarde tout » | Un dispositif existe | **Le support est-il atteignable depuis le réseau ?** |
| « On a extrait un fichier » | Un export a été fait | **Où est-il maintenant ?** C'est une copie de plus |

---

## Chapitre 33 — Suivre un secret

### 33.1 Ce qu'on appelle un secret

Mot de passe de service, clé d'interface applicative, certificat client, jeton d'accès, chaîne de connexion à une base. **Ils ont une propriété commune** : celui qui les détient est authentifié **sans être un utilisateur**.

⚠️ **C'est cette propriété qui les rend dangereux** : un secret volé ne déclenche aucun second facteur, aucune alerte de connexion inhabituelle, aucune expiration de session. **Il fonctionne exactement comme il est censé fonctionner.**

### 33.2 Où ils vivent, et qui les voit en clair

| Emplacement | Fréquence | Qui le voit en clair |
|---|---|---|
| **Dans un fichier de configuration** | **Très fréquent** | Toute personne ayant accès au serveur · **et aux sauvegardes** |
| Dans le code source | Fréquent, et grave | Tous ceux qui ont accès au dépôt · **son historique le conserve** |
| Dans une variable d'environnement | Fréquent | Les processus, les journaux de démarrage, les outils de diagnostic |
| Dans un coffre à secrets | Le bon modèle | L'application, à l'exécution seulement |
| **Dans un ticket, un courriel, un tableur** | **Fréquent, jamais avoué** | Tous les destinataires, indéfiniment |

⚠️ **La deuxième ligne mérite d'être soulignée** : un secret retiré du code source reste dans l'historique du dépôt. **Le supprimer ne le supprime pas.** Seule sa rotation le rend inoffensif.

⚠️ **La première ligne aussi, et pour une raison qu'on oublie** : un secret dans un fichier de configuration se retrouve **dans toutes les sauvegardes** de ce serveur. Une sauvegarde de trois ans conserve un secret de trois ans — qui n'a peut-être jamais été changé.

### 33.3 Le chemin d'un secret

```
  ① CRÉATION      qui le génère, et avec quelle qualité
  ② STOCKAGE      fichier · coffre · code
  ③ DISTRIBUTION  comment il arrive sur le serveur
                  → souvent manuellement, par quelqu'un qui l'a vu
  ④ USAGE         chargé en mémoire, parfois écrit dans un journal
  ⑤ ROTATION      changé, ou jamais
  ⑥ RÉVOCATION    ce qui se passe s'il fuit
```

**Les étapes ⑤ et ⑥ sont celles qui manquent presque toujours.** Un secret non tournant reste valide indéfiniment, et sa révocation n'a jamais été testée.

⚠️ **L'étape ③ est la plus sous-estimée.** Un secret distribué manuellement a été vu par au moins une personne, et il figure probablement dans un échange écrit — courriel, ticket, message. **La chaîne de confidentialité est rompue dès la mise en service.**

### 33.4 Le coffre à secrets, et son paradoxe

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne plus stocker de secret en clair | Un composant de plus, **dont la panne empêche les applications de démarrer** |
| Tourner automatiquement | Une intégration applicative — pas toujours possible |
| Tracer qui accède à quoi | Une exploitation supplémentaire |

⚠️ **Le paradoxe, et il est réel** : un coffre indisponible peut empêcher le démarrage de tout ce qui en dépend. **Principe du coût en action** — et une nouvelle dépendance circulaire : le coffre a lui-même besoin d'un secret pour démarrer.

📌 **Comment on résout ce paradoxe en pratique** : les applications conservent le secret en mémoire après l'avoir obtenu. Une panne du coffre n'arrête donc pas ce qui tourne — **elle empêche seulement ce qui redémarre**. C'est une nuance importante : la panne est **différée jusqu'au prochain redémarrage**, comme celle de l'attribution d'adresses, §15.3.

🔥 **SCÉNARIO — l'application ne redémarre plus**

| Question | Réponse |
|---|---|
| Symptôme | L'application tourne. Après un redémarrage planifié, elle refuse de se lancer |
| Hypothèse naïve | « La mise à jour a cassé quelque chose » |
| Dépendance réelle | **Le coffre à secrets est injoignable** — ou le secret a expiré |
| Ce que le schéma aurait dû montrer | Que l'application dépend du coffre **au démarrage** |
| Comment le reconnaître | **Elle fonctionnait, elle ne redémarre plus, rien d'autre n'a changé** |

### 33.5 Sur un schéma

Jamais. Un secret n'est ni un composant, ni un flux dessinable — c'est un attribut d'un flux existant.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le mot de passe est dans le fichier de conf » | Secret en clair sur le serveur | **Et dans toutes les sauvegardes** |
| « On l'a mis dans le vault » | Un coffre est utilisé | **Est-il un point de rupture au démarrage ?** |
| « On va le changer » | Rotation ponctuelle | **Combien d'endroits faut-il modifier ?** C'est ce qui empêche les rotations |
| « C'est un compte de service » | Une identité non humaine | **Depuis quand son secret n'a-t-il pas changé ?** |

---

## Chapitre 34 — Suivre un journal

> Le flux d'exploitation par excellence. **Sa rupture n'arrête aucun service — elle rend aveugle.**

### 34.1 D'où naît un journal, et ce que chacun voit

| Source | Ce qu'elle voit | Ce qu'elle ne voit pas |
|---|---|---|
| **Poste** | L'activité de l'utilisateur, les processus | Ce qui se passe sur le réseau après |
| **Pare-feu** | Ce qui traverse, et ce qui est refusé | Le contenu, sauf inspection |
| **Mandataire** | Les destinations, le contenu si déchiffré | **Ce qui ne passe pas par lui** — §29.3 |
| **Serveur web** | Les requêtes reçues | **L'identité réelle si un mandataire est devant** |
| **Applicatif** | Les actions métier, les autorisations | Ce qui se passe sous lui |
| **Base** | Les requêtes, parfois les données lues | **L'utilisateur final**, si l'applicatif utilise un compte unique |
| **Annuaire** | Les authentifications | Ce qui est fait après |

### 34.2 La perte d'identité en chemin

**Le problème le plus structurant du chapitre.**

```
   Marie ──► [ mandataire ] ──► [ web ] ──► [ app ] ──► [ base ]

   JOURNAL DU MANDATAIRE   « marie.durand a demandé /dossiers/4821 »
   JOURNAL DU WEB          « 10.0.2.15 a demandé /dossiers/4821 »
                             ↑ l'adresse du MANDATAIRE, pas de Marie
   JOURNAL DE L'APPLICATIF « utilisateur marie.durand a consulté
                             le dossier 4821 »   ← le seul complet
   JOURNAL DE LA BASE      « svc_app a exécuté SELECT ... »
                             ↑ le COMPTE DE SERVICE, pas Marie
```

⚠️ **Quatre journaux, deux identités différentes, et un seul qui relie l'utilisateur à l'action métier.** C'est le §43.3 : **l'applicatif est le seul point qui connaisse simultanément l'utilisateur réel et l'action**.

**Ce que cela impose** : corréler un journal de base avec un utilisateur réel exige de traverser trois journaux — et **cela suppose qu'ils partagent une horloge**. C'est pourquoi la synchronisation d'horloge est un flux de dépendance, principe des trois flux.

📌 **Les mécanismes qui atténuent le problème** : un mandataire peut transmettre l'adresse d'origine dans un en-tête · une application peut propager l'identité de l'utilisateur jusqu'à la base. **Les deux existent, les deux se configurent, et ni l'un ni l'autre n'est activé par défaut.**

### 34.3 Le chemin d'un journal

```
  ① PRODUCTION     le composant écrit
  ② STOCKAGE LOCAL avec une rotation qui l'efface après N jours
  ③ TRANSPORT      vers une collecte centrale — souvent en clair
  ④ COLLECTE       normalisation, horodatage
  ⑤ CONSERVATION   pour une durée définie… ou pas
  ⑥ EXPLOITATION   recherche, alerte, corrélation
```

**Les trois points de perte** :

| Point | Ce qui se perd | Pourquoi personne ne le voit |
|---|---|---|
| **② → ③** | Si le transport échoue, la rotation locale efface | **Rien n'alerte sur l'absence de journaux** |
| **⑤** | Une conservation trop courte | On ne s'en aperçoit qu'au moment d'enquêter |
| **④** | Un format non reconnu est ingéré sans être exploitable | Le volume est correct, la recherche ne trouve rien |

⚠️ **Le premier est le plus pernicieux** : une chaîne de collecte cassée ne produit **aucun signal**. L'absence de journaux ressemble exactement à l'absence d'activité. **La seule protection est de superviser le volume reçu par source** — et de s'alerter quand il tombe à zéro.

⚠️ **Le deuxième est le plus coûteux.** Le délai moyen entre une compromission et sa détection dépasse souvent la durée de conservation des journaux. **On enquête alors sur une période dont il ne reste rien.**

🔥 **SCÉNARIO — l'enquête porte sur une période dont il ne reste rien**

| Question | Réponse |
|---|---|
| Symptôme | Une compromission est découverte. Elle date d'il y a quatre mois |
| Hypothèse naïve | « On va regarder les journaux » |
| Dépendance réelle | **La conservation est de 90 jours.** Il ne reste rien |
| Ce que le schéma aurait dû montrer | La durée de conservation, par source |
| Concevoir différemment | **Aligner la conservation sur le délai de détection observé**, pas sur le coût du stockage |

### 34.4 Ce que la journalisation dit de l'architecture

**Une observation qui vaut méthode**, et il faut la formuler précisément :

> **Un composant peut produire un journal s'il est *en position de savoir* quelque chose.**

**Deux façons de l'être** :

| Position | Ce que le composant sait | Exemples |
|---|---|---|
| **Sur un chemin** | Ce qui le traverse | Pare-feu, mandataire, commutateur, routeur |
| **À l'origine d'une décision** | Ce qu'il a décidé, **sans qu'aucun flux ne traverse quoi que ce soit** | Une application qui autorise ou refuse · un poste qui lance un processus · un annuaire qui valide une identité |

⚠️ **La seconde ligne est celle que le modèle du point de passage manque.** Une application qui journalise *« Marie a exporté 4 000 lignes »* produit un événement métier **que rien n'a traversé au sens réseau**. C'est même la seule source capable de le produire — §34.2.

**Ce que cela donne comme méthode de lecture** :

```
   Devant chaque composant, une seule question :
   « Est-il en position de savoir quelque chose que personne d'autre ne sait ? »

   → OUI, et il journalise           ✅
   → OUI, et il ne journalise pas    ⚠️ angle mort — c'est le plus grave
   → NON                             pas de journal à en attendre
```

⚠️ **La deuxième ligne définit un angle mort structurel** : un composant qui sait et qui ne dit rien. C'est le cas de la plupart des applications métier — elles connaissent l'utilisateur et l'action, et elles ne journalisent que les erreurs techniques.

C'est le chapitre 43.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On log tout » | Beaucoup de sources sont collectées | **Combien de temps ? Et l'identité est-elle préservée ?** |
| « On a un SIEM » | Une collecte centrale existe | **Toutes les sources y arrivent-elles réellement ?** |
| « On n'a pas les logs » | La période est hors rétention | Combien de jours ? **Aligné sur quoi ?** |
| « L'IP dans le log est celle du proxy » | La perte d'identité — §34.2 | L'en-tête d'origine est-il transmis ? |

---

## Chapitre 35 — Du serveur au service

> Le chapitre qui transforme une lecture technique en décision métier.

### 35.1 Ce qu'est un service

> **Un service est ce qui produit une valeur pour l'organisation.** Il ne correspond à aucun composant : il en mobilise plusieurs, et personne ne le voit sur un schéma technique.

**Exemple, chez HELIOMED** :

| Service métier | Composants mobilisés |
|---|---|
| **« Télésuivi HelioLink »** | Mandataire inverse · répartiteur · 3 serveurs web · applicatif · base · annuaire · résolution de noms · lien Internet · certificats |

**Neuf composants pour un service.** Et parmi eux, trois — annuaire, résolution, certificats — ne figurent sur aucun schéma.

### 35.2 Ce qui tombe si ceci tombe

**La question centrale du cours**, et la méthode pour y répondre.

🖼 **SCHÉMA 35.1 — L'arbre de dépendance d'un service**

```
                  SERVICE « Télésuivi »
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   [ accès ]        [ traitement ]     [ données ]
        │                 │                 │
  ┌─────┼─────┐     ┌─────┼─────┐          ▼
  ▼     ▼     ▼     ▼     ▼     ▼      [ base ] ◄── point de rupture
lien  mandat. répart. web×3 applic.
      ▲         ▲          ▲
      │         │          │
      └─────────┴──────────┴──── [ résolution ] ◄── point de rupture invisible
                                 [ annuaire ]   ◄── point de rupture invisible
                                 [ certificats ]◄── point de rupture différé
```

**La lecture donne quatre points de rupture**, dont **trois ne sont pas sur le schéma d'architecture** :

| Composant | Effet de sa perte | Visible ? |
|---|---|---|
| **Base de données** | Service arrêté, données potentiellement perdues | ✅ |
| **Applicatif** | Service arrêté | ✅ |
| **Résolution de noms** | Service injoignable | ❌ |
| **Annuaire** | Authentification impossible | ❌ |
| **Certificats** | Service refusé par les navigateurs, **à une date connue d'avance** | ❌ |

### 35.3 La superposition des flux

**La section la plus importante du chapitre**, et celle qui transforme la lecture d'une architecture.

**Ce que le lecteur croit voir** :

```
   User ──────► App ──────► DB
```

**Ce qui existe réellement** :

🖼 **SCHÉMA 35.2 — Dix flux superposés sur un même service**

```
                        [ résolution ]
                              ▲
                              ┊ ①
                              ┊
   [ poste ] ══②══► [ frontal ] ══③══► [ app ] ══④══► [ base ]
       ┊  ┊              ┊  ┊             ┊  ┊           ┊
       ┊  └──⑤──► [ annuaire ] ◄──⑤──────┘  ┊           ┊
       ┊                    ┊                ┊           ┊
       ┊                    ┊         ⑥──► [ secrets ]   ┊
       ┊                    ┊                            ┊
       └──⑦──┐              ┊              ┊             ┊
              ▼             ▼              ▼             ▼
          [ collecte de journaux ] ◄──────⑦─────────────┘
                                                         ┊
   [ administration ] ══⑧══► tous les composants         ⑧
                                                         ┊
   [ sauvegarde ] ◄══⑨══════════════════════════════════┘
                                                         ┊
   [ supervision ] ◄══⑩══════════════════════════════════┘
```

| # | Flux | Famille | Dessiné ? | Si interrompu |
|---|---|---|---|---|
| ① | **Résolution de noms** | Dépendance | ❌ | Le service devient injoignable |
| ② | **Requête utilisateur** | Métier | ✅ | Le service ne rend plus son objet |
| ③ | **Frontal vers application** | Métier | ✅ | Idem |
| ④ | **Application vers base** | Métier | ✅ | Idem |
| ⑤ | **Authentification** | Dépendance | ❌ | Plus personne ne peut entrer |
| ⑥ | **Secrets** | Dépendance | ❌ | L'application ne démarre plus — §33.3 |
| ⑦ | **Journaux** | Exploitation | ❌ | Le service continue · **on devient aveugle** |
| ⑧ | **Administration** | Exploitation | ❌ | On ne peut plus intervenir |
| ⑨ | **Sauvegarde** | Exploitation | ❌ | On ne peut plus restaurer |
| ⑩ | **Supervision** | Exploitation | ❌ | On ne sait plus si ça marche |

**Trois flux sur dix sont dessinés.** Et les sept invisibles se répartissent exactement selon le principe des trois flux : **trois dépendances dont la rupture arrête le service, quatre flux d'exploitation dont la rupture rend aveugle sans arrêter.**

### 35.4 La méthode, en cinq étapes

```
1. NOMMER LE SERVICE      du point de vue du métier, pas de la technique
2. SUIVRE LE FLUX MÉTIER  les douze étapes du §29.1
3. AJOUTER LES DÉPENDANCES résolution · identité · certificats
                           · secrets · temps
4. AJOUTER L'EXPLOITATION  journaux · supervision · sauvegarde
                           · administration
5. TESTER CHAQUE NŒUD     « si celui-ci tombe, le service rend-il
                            encore son objet ? »
```

⚠️ **Les étapes 3 et 4 distinguent une cartographie utile d'une cartographie décorative.** Sans elles, on obtient un arbre où tous les points de rupture sont déjà connus — et qui n'apprend rien.

**Le rendu attendu** — une page par service critique :

```
SERVICE : ..............................
FLUX MÉTIER      n composants : ........................
DÉPENDANCES      n composants : ........................
EXPLOITATION     n composants : ........................
POINTS DE RUPTURE   n dont n INVISIBLES sur le schéma
CE QUI N'EST PAS TESTÉ : ...............................
```

⚠️ **La dernière ligne est celle qui a le plus de valeur en comité.** Elle transforme une cartographie technique en constat décisionnel — **principe de preuve**.

### 35.5 Les trois niveaux de dégradation

| Niveau | Ce qui se passe | Exemple |
|---|---|---|
| **Arrêt** | Le service ne rend plus rien | Base indisponible |
| **Dégradation** | Le service fonctionne partiellement | Un serveur web sur trois : plus lent |
| **Cécité** | Le service fonctionne, on ne le voit plus | Collecte de journaux arrêtée |

**Les trois niveaux correspondent aux trois familles de flux de principe des trois flux** : métier → arrêt ou dégradation · dépendance → arrêt · exploitation → cécité. C'est ce qui rend la taxonomie utile.

⚠️ **Mais la correspondance n'est pas une loi, et il faut le dire.** La famille décrit **la fonction principale d'un flux, pas une garantie sur l'effet de sa panne**. Trois contre-exemples courants :

| Situation | Pourquoi elle sort du modèle |
|---|---|
| Un stockage saturé par les journaux | Un flux d'exploitation finit par **arrêter** le service |
| Une sauvegarde qui verrouille une ressource | Idem |
| Un outil de déploiement indispensable à un basculement | Un flux d'exploitation devient une dépendance en situation de panne |

**Et symétriquement** : certains flux métier disparaissent sans arrêter le service — une fonctionnalité secondaire, un export périodique.

> **La taxonomie est un modèle de raisonnement. Employez-la pour poser les bonnes questions, pas pour prédire des effets.**

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*On vous demande combien de temps le service « Télésuivi » peut rester indisponible. Que répondez-vous ?*
**Vous ne répondez pas — vous demandez d'abord de quoi il dépend.** Un service dont l'arbre comporte neuf composants dont trois invisibles n'a pas un seul délai de reprise : il en a autant que de causes possibles. La mauvaise décision évitée : **s'engager sur un délai de rétablissement calculé sur les seuls composants dessinés**, et découvrir en crise qu'une expiration de certificat ou une panne de résolution demande un délai tout autre.

---

### 🔬 Mini-lab 8 — Tracer six flux sur un même schéma

**Objectif** — Distinguer les trois familles sur une architecture unique.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 29 à 34

Sur le schéma 1.1, tracez et classez : ① une requête d'un client externe · ② une authentification d'un salarié interne · ③ une sauvegarde nocturne · ④ un journal du mandataire vers la collecte · ⑤ la mise à jour d'un certificat · ⑥ un export de données vers un tableur.

---

**Corrigé**

| # | Flux | Famille | Chemin | Visible sur le schéma ? |
|---|---|---|---|---|
| **①** | Requête client | **Métier** | Internet → pare-feu → mandataire → répartiteur → web → applicatif → base | **Partiellement** — la résolution et l'authentification manquent |
| **②** | Authentification interne | **Dépendance** | Poste → annuaire | ❌ **Aucun trait** |
| **③** | Sauvegarde nocturne | **Exploitation** | Base → serveur de sauvegarde → support | ❌ Le serveur est dessiné, **son chemin non** |
| **④** | Journal vers collecte | **Exploitation** | Chaque composant → collecte | ❌ **La collecte n'est pas sur le schéma** |
| **⑤** | Mise à jour de certificat | **Dépendance** | Autorité → mandataire, manuellement ou automatiquement | ❌ Rien |
| **⑥** | Export vers tableur | **Métier**, sortant | Base → applicatif → poste → **fichier local** | ❌ **Le poste n'est pas dessiné** |

**Le bilan : un flux sur six est représenté, et partiellement.**

**Les trois erreurs attendues**

1. **Classer ③ en dépendance.** La sauvegarde n'arrête pas le service : elle empêche de le restaurer. C'est de l'exploitation — principe des trois flux.
2. **Oublier ⑥.** Un export n'est pas un flux technique, c'est pourtant celui par lequel les données sortent du périmètre contrôlé — §32.2.
3. **Tracer ② vers le mandataire** au lieu de l'annuaire. L'authentification d'un salarié interne ne passe pas par le mandataire inverse : le chemin interne est plus court, et différemment contrôlé — §29.3.

---

### 🔬 Mini-lab 9 — Les points de rupture d'un service

**Objectif** — Construire un arbre de dépendance et identifier les ruptures invisibles.
**Durée** 35 min · **Difficulté** 🔴 avancé · **Prérequis** chapitre 35

**Le service** : « Commande en ligne » d'une organisation de distribution. Composants connus : deux serveurs web, un applicatif, une base répliquée, un mandataire inverse, un lien Internet redondé, un service de paiement externe.

❓ Construisez l'arbre, identifiez les points de rupture, classez-les par visibilité.

---

**Corrigé**

| Composant | Rupture ? | Visible ? | Nuance |
|---|---|---|---|
| Lien Internet | ⚠️ **Indéterminé** | ✅ | Annoncé redondé. **Deux liens du même opérateur, sur le même point d'entrée du bâtiment, ne redondent pas grand-chose** — *principe de preuve* |
| Mandataire inverse | ⚠️ **Indéterminé** | ✅ | **Un seul est mentionné** — à vérifier |
| Serveurs web ×2 | ❌ | ✅ | Sauf si sessions locales — §31.2 |
| **Applicatif** | ✅ **Oui** | ✅ | Unique |
| Base répliquée | ⚠️ | ✅ | **Le basculement a-t-il été testé ?** — §20 |
| **Résolution de noms** | ✅ **Oui** | ❌ | |
| **Annuaire ou fournisseur d'identité** | ✅ **Oui** | ❌ | |
| **Certificats** | ✅ **Oui**, à date connue | ❌ | |
| **Service de paiement externe** | ✅ **Oui** | ✅ | **Hors de votre maîtrise** — chapitre 38 |
| **Magasin de sessions** | ⚠️ | ❌ | **N'a pas été mentionné : existe-t-il ?** |

**Sept points de rupture ou incertitudes, dont quatre invisibles.**

**Les deux questions qui font la différence** :

1. *Le mandataire inverse est-il redondé ?* Il n'est mentionné qu'au singulier. Un seul mandataire annule la redondance de tout ce qui est derrière.
2. *Où sont les sessions ?* Si elles sont locales aux serveurs web, la redondance affichée ne protège pas l'utilisateur en cours de commande — §31.2. **La question n'a pas été posée dans l'énoncé, et c'est volontaire.**

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> ✓ suivre une **requête en douze étapes**, dont sept ne figurent sur aucun schéma ;
> ✓ que **six authentifications sur sept sont invisibles** pour l'utilisateur, et toutes dépendent d'un composant non dessiné ;
> ✓ décrire la **cascade progressive** d'une panne d'annuaire, et pourquoi elle est difficile à diagnostiquer ;
> ✓ que **l'emplacement de la session détermine ce que la redondance apporte réellement** ;
> ✓ suivre une **donnée en neuf étapes**, et savoir que la supprimer de la base ne la supprime que de la base ;
> ✓ qu'un **secret retiré du code source reste dans l'historique** — seule sa rotation le rend inoffensif ;
> ✓ que la **rupture d'un journal n'arrête rien et rend aveugle**, et que la conservation est souvent plus courte que le délai de détection ;
> ✓ construire l'**arbre de dépendance d'un service** en ajoutant les invisibles — l'étape qui distingue une cartographie utile d'une cartographie décorative ;
> ✓ que les **trois niveaux de dégradation** — arrêt, dégradation, cécité — correspondent exactement aux trois familles de flux.
>
> **Ce que vous ne savez pas encore** : comment appliquer tout cela de façon systématique à une architecture inconnue. C'est l'objet de la Partie VI, et de sa grille en sept passes.

---
