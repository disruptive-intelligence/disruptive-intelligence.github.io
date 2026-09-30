---
title: PARTIE I — Fondations, socle technique et maintenabilité
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 2
chapters: 10
---

Cette première partie a un objectif précis : vous rendre autonome sur le reste du cours. Elle ne suppose aucune expérience préalable en gestion des vulnérabilités, en conformité ou en exploitation de parc. Elle suppose en revanche une culture informatique générale — vous savez ce qu'est un serveur, un réseau, une application.

Elle ne remplace pas un cours de systèmes, de réseau, de cloud ou de développement, et le dit franchement à chaque fois que le sujet dépasse son périmètre.

---

## Chapitre 1 — Ce qu'est réellement le MCS

### 1.1 Définition, origine et périmètre

#### Le modèle mental d'abord

Commençons par une image qui va vous servir pendant tout le cours.

Imaginez que vous installiez aujourd'hui un serveur neuf. Système à jour, configuration soignée, mots de passe robustes, aucune faille connue. Ce jour-là, son niveau de sécurité est le meilleur que vous puissiez connaître et valider. Appelons cela le jour J.

Le lendemain, vous ne touchez à rien. Personne ne s'y connecte, aucune configuration ne change, aucune ligne de code n'est modifiée. Et pourtant, la validité de votre évaluation a **déjà commencé à s'éroder**.

Pourquoi ? Parce que ce n'est pas le serveur qui a changé, c'est le monde autour de lui :

- un chercheur a publié une faille dans une bibliothèque qu'il utilise ;
- un attaquant a mis au point une technique qui contourne une de ses protections ;
- l'éditeur a annoncé que la version installée ne serait plus supportée dans dix-huit mois ;
- un certificat qu'il présente à ses clients a perdu un jour de sa durée de vie ;
- une autorité de certification dont dépend son démarrage sécurisé s'est rapprochée de sa date d'expiration.

C'est le point de départ de tout : **la sécurité n'est pas un état que l'on atteint, c'est un niveau qui se dégrade tout seul.** Sans effort continu, un système parfaitement sécurisé le jour J devient vulnérable, non par négligence ponctuelle, mais par simple écoulement du temps.

Le **maintien en condition de sécurité (MCS)** est l'ensemble des mesures techniques et organisationnelles qui compensent cette dégradation, pendant toute la durée de vie du système — de sa mise en service jusqu'à son retrait définitif.

#### La définition de travail

Retenez celle-ci, elle sera utilisée dans tout le cours :

> **MCS** : ensemble des activités techniques et organisationnelles visant à maintenir, et si possible améliorer, le niveau de sécurité d'un système d'information pendant tout son cycle de vie, y compris son décommissionnement — et à en apporter la preuve.

Trois éléments de cette définition méritent qu'on s'y arrête.

**« techniques *et* organisationnelles ».** Le MCS n'est pas un problème d'outil. Une organisation peut disposer du meilleur scanner de vulnérabilités du marché et n'appliquer aucun correctif, faute de savoir qui est responsable du serveur concerné. Nous verrons au §1.4 que les causes d'échec les plus fréquentes ne sont presque jamais techniques.

**« pendant tout son cycle de vie, y compris son décommissionnement ».** Un serveur éteint mais dont l'enregistrement DNS existe toujours, dont le compte de service reste actif et dont la sauvegarde reste restaurable n'est pas décommissionné : c'est un actif fantôme, et c'est un problème de MCS. Le chapitre 35 y est entièrement consacré.

**« et à en apporter la preuve ».** Une activité de MCS non traçable est presque impossible à piloter, à défendre en audit et à financer. C'est une exigence à part entière, pas une formalité administrative ajoutée après coup. Nous y reviendrons constamment, et le chapitre 39 la traite pour elle-même.

#### La boucle qui structure tout le cours

Un seul schéma suffit à décrire le métier. Chaque partie de ce cours travaille un segment de cette boucle, et chaque chapitre indique lequel.

```
                 ┌──────────────────────────────────────────┐
                 │                                          │
                 ▼                                          │
        ①  CONNAÎTRE ────► ②  OBSERVER ────► ③  DÉCIDER     │
        inventaire         veille,            triage,        │
        exposition         détection          priorisation   │
        propriété                                            │
                                     │                       │
                                     ▼                       │
        ⑥  PROUVER ◄──── ⑤  VÉRIFIER ◄──── ④  CORRIGER      │
        preuve,          état constaté,     ou compenser,    │
        indicateurs,     traîne longue      ou déroger       │
        audit                                                │
             │                                               │
             └───────────────────────────────────────────────┘
                        amélioration continue
```

| Segment | Question | Parties du cours |
|---|---|---|
| ① **Connaître** | Qu'est-ce que je dois maintenir, et qui en répond ? | I, II (ch. 10-13) |
| ② **Observer** | Qu'est-ce qui a changé, et cela me concerne-t-il ? | III (ch. 14-15) |
| ③ **Décider** | Que traiter, dans quel ordre, dans quel délai ? | III (ch. 16-17) |
| ④ **Corriger** | Appliquer, ou compenser, ou déroger | III, IV (ch. 18-28) |
| ⑤ **Vérifier** | Le code corrigé s'exécute-t-il vraiment ? | III (ch. 18) |
| ⑥ **Prouver** | Puis-je le démontrer dans six mois ? | VI (ch. 38-39) |

⚠️ **La boucle échoue toujours au même endroit** : au segment ①. Une organisation qui observe, décide, corrige et vérifie parfaitement sur un périmètre qu'elle ne connaît qu'à 70 % obtient d'excellents indicateurs sur 70 % de son parc — et ignore les 30 % restants, qui sont statistiquement les moins maintenus (§10.1).

🖼 **SCHÉMA — La boucle du MCS en six segments.** *Diagramme circulaire, six nœuds, flèche de retour « amélioration continue ». Chaque nœud porte son numéro de partie.*

#### Où se situe le MCS parmi les métiers voisins

Le MCS est régulièrement confondu avec trois fonctions voisines. Le tableau suivant sert de référence pour tout le cours.

| Fonction | Question centrale | Horizon | Ce qu'elle produit |
|---|---|---|---|
| **SOC / détection** | *Sommes-nous attaqués en ce moment ?* | Minutes à heures | Des alertes qualifiées |
| **CERT / CSIRT** | *Comment reprendre le contrôle ?* | Heures à jours | Une réponse à incident |
| **Exploitation** | *Est-ce que ça fonctionne ?* | Continu | Un service disponible |
| **MCS** | *Le niveau de sécurité tient-il dans la durée, et puis-je le prouver ?* | **Mois à années** | Un parc maintenu **et démontrable** |

**Les recouvrements sont réels et voulus.** Le MCS fournit au SOC un inventaire et une exposition à jour (ch. 10-11) ; le SOC fournit au MCS le signal d'exploitation (§14.5) ; le CERT hérite du MCS la capacité à savoir ce qui tournait où (§21.3). Ce qui distingue le MCS, c'est **l'horizon** : il est le seul de ces quatre métiers dont le succès se mesure sur plusieurs années.

#### Une journée type

Pour rendre le métier concret avant d'en décrire les mécanismes :

| Moment | Activité | Chapitre |
|---|---|---|
| 8 h 30 | Lecture de la veille : avis éditeurs, bulletins, signaux d'exploitation. Vingt minutes, tous les jours | 14 |
| 9 h 00 | Qualification des constats arrivés : fait vérifié, hypothèse, piste. Écarter les faux positifs de rétroportage | 14, 15 |
| 10 h 00 | Triage : passage dans l'arbre de décision. Ce qui part en urgence, en campagne, en surveillance | 16 |
| 11 h 00 | Comité de changement : défendre deux demandes, négocier une fenêtre | 5, 9 |
| 14 h 00 | Suivi des campagnes : relances, échecs d'installation, traîne longue à qualifier | 17, 18 |
| 15 h 30 | Une dérogation à instruire avec un propriétaire métier réticent | 7, 20 |
| 16 h 30 | Production de preuve : extraction, échantillon vérifié, archivage | 2, 39 |
| 17 h 00 | Une heure imprévue : un correctif qui casse, ou une alerte d'exploitation | 18, 21 |

**Ce que cette journée montre** : moins de la moitié du temps est technique. Le reste est de la qualification, de la négociation et de la preuve — ce qui explique la structure de ce cours.

#### Le vocabulaire du terrain

Ce cours emploie un vocabulaire rigoureux, parce que la précision évite des malentendus coûteux — notamment entre *couverture* et *conformité*, ou entre *dérogation* et *acceptation de risque*. En réunion, vous entendrez rarement ces mots. Voici la table de correspondance, à garder en tête tout au long du cours.

| Terme du cours | Ce que vous entendrez en réunion | Nuance à ne pas perdre |
|---|---|---|
| Correctif | « **le patch** », « la MAJ » | Un correctif est publié par un éditeur ; une « MAJ » peut aussi être une montée de version fonctionnelle |
| Campagne de correction | « **la campagne de patching** », « le patch tuesday » | — |
| Fenêtre de maintenance | « **la fenêtre** », « le créneau », « la patch window » | — |
| Ensemble des constats ouverts | « **le backlog** », « la pile », « les restes » | Le backlog n'est pas une file d'attente : il contient aussi des décisions prises de ne pas traiter |
| Constat | « **un finding** », « une vulné », « une CVE » | Un constat n'a pas nécessairement d'identifiant CVE — c'est tout le §14.2 |
| Dérogation | « **une exception** », « une déro », « un waiver » | « Exception » désigne aussi une exclusion d'outil : deux choses très différentes (§15.6) |
| Demande de changement | « **le change** », « la RFC », « le ticket de change » | — |
| Procédure d'exploitation | « **le runbook** », « la doc d'exploit » | — |
| Retour arrière | « **le rollback** » | — |
| Délai d'observation | « **le bake time** », « on laisse reposer » | — |
| Déploiement témoin | « **le canary** », « le pilote » | — |
| Durcissement | « **le hardening** » | — |
| Propriétaire d'actif | « **l'owner** », « le référent », « le responsable » | Le cours distingue propriétaire métier et technique : « l'owner » les confond souvent (§5.5) |
| Dette de sécurité | « **la dette** », « le legacy », « les vieilleries » | — |
| Gain rapide | « **un quick win** » | — |
| Périmètre de référence | « **le parc** », « le scope » | « Le parc » désigne souvent ce que l'outil connaît, pas le périmètre réel (§10.1) |

⚠️ **La règle à retenir** : parlez la langue de votre interlocuteur, mais **écrivez** la langue précise. Un compte rendu de comité qui dit « on a mis une exception sur la préprod » ne permet à personne, six mois plus tard, de savoir s'il s'agissait d'une dérogation signée, d'une exclusion de scan ou d'un risque accepté — et ces trois situations n'appellent ni le même suivi ni le même signataire.

#### D'où vient le terme

L'expression est une spécificité française. Elle est apparue par calque du **maintien en condition opérationnelle (MCO)**, terme d'origine militaire puis industrielle désignant l'ensemble des actions garantissant qu'un équipement reste disponible et fonctionnel. On la rencontre principalement :

- dans la doctrine et les guides de l'ANSSI (Agence nationale de la sécurité des systèmes d'information) ;
- dans les cahiers des charges de marchés publics, souvent sous la forme d'une clause « MCO/MCS » imposée au titulaire ;
- dans les dossiers d'homologation de sécurité, où le MCS conditionne le maintien de la décision d'homologation dans le temps.

Il n'existe pas d'équivalent unique en anglais. Le périmètre du MCS est couvert par plusieurs notions partiellement recouvrantes : *vulnerability management*, *patch management*, *security maintenance*, *continuous compliance*, *security operations*. Aucune ne correspond exactement, et c'est important : le MCS est **plus large que le patch management** et **plus étroit que « la sécurité »**.

⚠️ **PIÈGE — confondre MCS et gestion des correctifs**
C'est l'erreur la plus répandue du domaine, y compris chez des professionnels expérimentés. Un programme de MCS réduit aux correctifs laissera intacts : les configurations qui dérivent, les certificats qui expirent, les comptes de service jamais revus, les dépendances applicatives obsolètes, les micrologiciels jamais mis à jour, les règles de détection périmées, les systèmes retirés du service mais toujours joignables. Le §1.3 dresse la liste complète.

> ### 📌 Les quatre idées à retenir de ce chapitre
>
> Le chapitre 1 contient beaucoup de notions fondatrices. Si vous n'en gardez que quatre :
>
> 1. **La sécurité se dégrade toute seule.** Ce n'est pas le système qui change, c'est le monde autour de lui. Le MCS compense cette dégradation.
> 2. **Le MCS est plus large que la gestion des correctifs.** Dix familles d'objets se dégradent, et les versions logicielles n'en sont qu'une.
> 3. **Les cinq causes d'échec ne sont pas techniques** : inventaire, propriété, fenêtres, preuve, financement.
> 4. **Le MCS ne remplace ni la détection, ni la sauvegarde, ni l'architecture.** Il réduit la probabilité qu'une attaque connue réussisse. C'est tout, et c'est beaucoup.
>
> Le reste du chapitre est du contexte utile. Ces quatre points sont réutilisés dans les trente-neuf chapitres suivants.

### 1.2 MCO et MCS : deux maintiens, un conflit structurel

Le MCO répond à la question : *est-ce que ça marche ?*
Le MCS répond à la question : *est-ce que c'est encore sûr ?*

Ces deux questions sont portées par les mêmes équipes, sur les mêmes machines, dans les mêmes fenêtres d'intervention, avec le même budget. Elles entrent en conflit régulièrement, et ce conflit n'est ni un dysfonctionnement ni un problème de personnes : il est **structurel**.

| Situation | Ce que dicte le MCO | Ce que dicte le MCS |
|---|---|---|
| Correctif de sécurité disponible, non testé | Attendre : le risque de régression est réel | Appliquer vite : la faille est peut-être exploitée |
| Version majeure en fin de support, applicatif métier incompatible | Ne pas migrer : l'application casserait | Migrer : plus aucun correctif ne sera publié |
| Redémarrage nécessaire en pleine période d'activité | Reporter au prochain arrêt planifié | Le report allonge la fenêtre d'exposition |
| Équipement fonctionnel mais hors support constructeur | Il fonctionne, on le garde | Il ne recevra plus jamais de correctif |

La conséquence pratique est simple à énoncer et difficile à vivre : **le MCS ne s'impose jamais contre le MCO, il se négocie avec lui**. Toute organisation qui prétend faire du MCS en ignorant les contraintes de production produit soit du conflit permanent, soit des décisions non appliquées. Le chapitre 9 (gouvernance) et le chapitre 37 (facteur humain) traitent cette négociation comme un objet d'ingénierie à part entière, pas comme un problème relationnel.

> **Encadré terminologique — les termes qu'on vous opposera**
> Vous rencontrerez d'autres expressions : **MCP** (maintien en condition de performance), **MCF** (maintien en condition fonctionnelle), *continuous compliance*. Aucune n'est normalisée, et leur périmètre varie fortement d'une organisation à l'autre et d'un appel d'offres à l'autre.
> **Recommandation** : ne les importez pas. Si votre organisation les utilise, définissez-les explicitement dans votre politique interne, avec leur périmètre et leur propriétaire. Un terme non défini dans un contrat de prestation est une source de litige : chacun l'interprétera dans son intérêt le jour où quelque chose ne sera pas fait.

### 1.3 Le périmètre réel du MCS : dix objets qui se dégradent

**Ces dix familles ont un point commun**, et c'est lui qui les rassemble : elles perdent progressivement leur niveau de sécurité si personne ne les entretient, **indépendamment de toute action de votre part**. Voici ce qui, dans un système d'information, se dégrade avec le temps. La liste n'est pas exhaustive ; elle couvre l'essentiel de ce qu'un programme de MCS doit adresser. Chaque ligne correspond à un ou plusieurs chapitres du cours.

| Objet maintenu | Ce qui se dégrade | Rythme typique de dégradation | Traité au |
|---|---|---|---|
| **Versions logicielles** | Failles publiées, fin de support | Continu, accéléré à chaque publication de correctif | Ch. 15-19 |
| **Configurations** | Dérive par intervention manuelle, urgence, restauration | Lent mais irréversible sans contrôle | Ch. 22-23 |
| **Identités et droits** | Comptes orphelins, délégations héritées, droits accumulés | Très lent, jamais spontanément réversible | Ch. 24 |
| **Secrets** | Vieillissement, diffusion, absence de rotation | Se dégrade à chaque départ de collaborateur | Ch. 24 |
| **Certificats et confiance** | Expiration, algorithmes dépréciés, autorités qui expirent | Échéance **datée et connue à l'avance** | Ch. 24, 27 |
| **Dépendances logicielles** | Failles de composants tiers, projets abandonnés | Continu, hors de votre contrôle | Ch. 25 |
| **Micrologiciels** | Failles de bas niveau, fin de support matériel | Lent, mais correctifs rares et risqués | Ch. 27 |
| **Contenu de détection** | Signatures, règles, listes de blocage périmées | Quotidien | Ch. 34 |
| **Documentation et procédures** | Écart croissant avec la réalité | Se dégrade à chaque changement non documenté | Ch. 39 |
| **Compétences des personnes** | Départs, perte de savoir non transmis | Brutal (un départ) | Ch. 37 |

Deux observations sur ce tableau, qui structureront toute votre approche.

**Première observation : toutes ces échéances ne sont pas de même nature.** Une distinction utile, et souvent mal faite :

- **L'expiration d'un certificat est intrinsèque.** Elle est encodée dans l'objet lui-même, dès son émission, et elle est absolue : à la seconde près, le certificat cesse d'être valide, quoi que décide qui que ce soit. C'est la seule échéance que personne ne peut déplacer.
- **Une fin de support est une échéance éditoriale ou contractuelle.** Elle est décidée par un tiers, annoncée à l'avance, et **elle peut être modifiée** — prolongée, raccourcie, assortie de conditions nouvelles. Planifier dessus est indispensable, mais il faut la resurveiller.
- **Les autres échéances sont des décisions internes** : rotation de clé, migration planifiée, fin de contrat. Elles ne s'imposent que si quelqu'un les tient.

L'ironie du domaine est que la catégorie la plus prévisible — l'expiration cryptographique — reste l'une des premières causes d'interruption de service. La raison est presque toujours la même : personne ne tient l'inventaire de ce qui expire.

⏱ **ÉTAT DE L'ART — l'illustration de l'année 2026 (vérifié le 30/07/2026)**
Les certificats Microsoft utilisés par le démarrage sécurisé (*Secure Boot*), émis en 2011 pour quinze ans, sont arrivés à échéance en juin 2026, une troisième suivant en octobre 2026. Les machines concernées continuent de démarrer et de recevoir leurs mises à jour habituelles ; elles perdent en revanche, silencieusement, la capacité de recevoir de futures protections de la chaîne de démarrage. Le mécanisme complet, les trois certificats et les cinq enseignements de MCS que ce cas contient sont traités au **§3.8**.
📎 [S-25]

**Seconde observation : aucun outil ne couvre les dix lignes.** Ne cherchez pas la plateforme unique. Elle n'existe pas, et les fournisseurs qui la promettent couvrent en réalité trois ou quatre lignes correctement, les autres superficiellement. Votre travail consiste à savoir *quelle ligne est couverte par quoi*, et surtout **quelle ligne n'est couverte par rien**.

### 1.4 Les cinq causes récurrentes d'échec

Les retours d'expérience du domaine convergent vers un constat stable : les programmes de MCS échouent le plus souvent pour les mêmes raisons, et généralement dans le même ordre. Aucune n'est **exclusivement** technique.

**1. L'inventaire.** On ne maintient pas ce qu'on ne connaît pas. Un écart de 15 à 30 % entre l'inventaire théorique et la réalité est la norme, pas l'exception, dans une organisation qui n'a jamais fait ce travail. Tant que cet écart n'est pas mesuré et réduit, tous les indicateurs de MCS sont faux — non pas imprécis : **faux**, parce que leur dénominateur est inconnu. → Chapitre 10.

**2. La propriété.** Pour chaque actif, une question doit avoir une réponse nominative : *qui décide qu'on l'arrête pour le corriger ?* En l'absence de réponse, le correctif attend. Ce n'est pas un problème de bonne volonté : c'est un vide de décision, et personne ne prend spontanément une décision dont il n'a pas le mandat. → Chapitres 5 et 9.

**3. Les fenêtres.** Corriger suppose souvent d'interrompre. Si l'organisation n'a pas négocié à l'avance des créneaux d'interruption acceptés par les métiers, chaque correctif devient une négociation individuelle — donc un coût, donc un report. → Chapitres 5, 18 et 37.

**4. La preuve.** Sans traçabilité, vous ne pouvez ni démontrer un progrès, ni justifier un budget, ni répondre à un auditeur, ni savoir si un correctif a réellement été appliqué sur les 2 300 postes concernés ou seulement sur les 1 800 qui étaient allumés ce soir-là. → Chapitres 38 et 39.

**5. Le financement.** Sortir de l'obsolescence coûte cher, et ce coût est visible immédiatement alors que le bénéfice est invisible et différé. Sans dossier d'investissement construit, l'arbitrage budgétaire est perdu d'avance, chaque année, indéfiniment. → Chapitre 37.

✅ **BONNE PRATIQUE — l'ordre d'attaque (P0)**
Si vous démarrez un programme de MCS, traitez ces cinq causes **dans cet ordre**. Investir dans l'outillage de déploiement avant d'avoir un inventaire fiable et des propriétaires nommés est l'erreur de séquencement la plus coûteuse du domaine : vous automatiserez le traitement d'un périmètre que vous ne connaissez pas, et vous produirez des tableaux de bord verts sur un dénominateur faux. Le chapitre 40 détaille la feuille de route complète.

### 1.5 Le MCS dans le cycle de vie : *build → run → sunset*

Le MCS est habituellement perçu comme une activité du *run* — la phase d'exploitation. C'est incomplet, et cette incomplétude coûte cher.

**Phase *build* (conception et construction).** Les décisions d'architecture prises ici déterminent le coût de tout le MCS futur. Un système sans redondance ne pourra jamais être corrigé sans interruption. Une application couplée à une version précise de son environnement d'exécution bloquera toutes les montées de version. Un produit sans mécanisme de mise à jour signé ne pourra jamais être corrigé chez le client en confiance. Le chapitre 6 est entièrement consacré à cette phase, sous le nom de *MCS by design*.

**Phase *run* (exploitation).** C'est le cœur du cours : veille, détection, triage, remédiation, configuration, preuve. Parties II à V.

**Phase *sunset* (fin de vie et retrait).** Elle commence bien avant l'arrêt : dès l'annonce de fin de support par l'éditeur, une trajectoire doit exister. Elle se termine par un décommissionnement complet et vérifié. Chapitres 12 et 35.

L'enseignement structurant tient en une phrase : **le coût du MCS d'un système est majoritairement déterminé pendant la phase où l'on n'y pense pas.**

### 1.6 La dette de sécurité comme grandeur mesurable

⚠️ **Une confusion à écarter d'emblée** : la dette de sécurité n'est pas le stock de vulnérabilités non corrigées. Elle comprend aussi les systèmes hors support, les configurations dérivées, les comptes jamais revus, les certificats non inventoriés, les dérogations accumulées et les architectures non interruptibles. Un parc sans aucune vulnérabilité ouverte peut porter une dette considérable.

L'analogie financière est ici juste, et pas seulement décorative.

Quand vous reportez une mise à jour, vous contractez une dette. Vous obtenez un bénéfice immédiat (pas d'interruption, pas de risque de régression, pas de charge de travail) contre un coût futur. Et comme toute dette, elle produit des **intérêts** : plus vous attendez, plus la migration devient difficile, parce que l'écart de versions grandit, que les chemins de migration directs disparaissent, que les compétences se perdent et que le nombre de failles cumulées augmente.

C'est ce qui explique un phénomène que vous observerez : le coût d'une migration ne croît pas proportionnellement au délai de report, il croît plus vite. Les mécanismes en sont identifiables un par un — chemins de migration directs qui disparaissent et imposent des étapes intermédiaires, matériel devenu incompatible, compétences perdues, dépendances applicatives qui se sont multipliées entre-temps. L'ampleur exacte dépend entièrement du contexte : ce qui est généralisable, c'est le mécanisme, pas un facteur multiplicateur.

Quatre grandeurs suffisent à rendre cette dette visible. Elles sont définies rigoureusement au chapitre 38 et détaillées en Annexe K ; à ce stade, retenez l'idée :

- le **nombre d'actifs hors support**, pondéré par leur criticité ;
- le **nombre de vulnérabilités critiques dont le délai de correction est dépassé** ;
- le **nombre et l'ancienneté des dérogations ouvertes** — une dérogation est une dette formalisée ;
- l'**âge moyen des constats non traités**, qui mesure la vitesse réelle de l'organisation.

⚠️ **PIÈGE — la dette invisible est la plus dangereuse**
Une organisation qui ne mesure pas ces grandeurs n'a pas moins de dette : elle a la même dette, sans le savoir. Et une dette non mesurée ne se finance jamais, puisqu'elle n'apparaît dans aucun arbitrage budgétaire.

### 1.7 Ce que le MCS ne résout pas

Un cours honnête doit énoncer clairement les limites de son sujet. Le MCS **ne protège pas** contre :

- **une vulnérabilité inconnue de tous** (*0-day*) : par définition, aucun correctif n'existe. Le MCS réduit la surface disponible et raccourcit le délai de réaction quand le correctif arrive ; il n'empêche pas l'attaque ;
- **l'hameçonnage et l'ingénierie sociale** : un poste parfaitement à jour n'empêche pas un utilisateur de saisir ses identifiants sur un site frauduleux ;
- **un défaut d'architecture** : un système à jour mais exposé sans nécessité sur Internet reste une cible. Fermer l'exposition est souvent plus efficace que corriger — c'est l'objet du chapitre 11 ;
- **l'usage légitime détourné** : un attaquant disposant d'identifiants valides n'a besoin d'aucune faille ;
- **une erreur de conception de sécurité** : une fonctionnalité dangereuse par construction ne sera pas corrigée par une mise à jour, puisqu'elle fonctionne comme prévu.

Le MCS se positionne donc comme **une couche parmi d'autres** : il réduit la probabilité qu'une attaque connue réussisse, il ne remplace ni la détection, ni la sauvegarde, ni la segmentation, ni l'architecture.

⚠️ **PIÈGE — les quatre illusions les plus coûteuses**

| Illusion | Ce qui cloche |
|---|---|
| « On applique tous les correctifs, donc on est à jour » | Vous appliquez les correctifs *des actifs que vous connaissez*, *que votre outil couvre*, *et qui étaient joignables*. Les trois filtres se cumulent |
| « Le tableau de bord est à 98 % de conformité » | 98 % de quel dénominateur ? Calculé quand ? Avec quelles exclusions ? Voir §38.3 |
| « C'est du cloud / du SaaS, c'est maintenu par le fournisseur » | Le fournisseur maintient sa couche. La vôtre — configuration, identités, extensions, intégrations — reste entièrement à votre charge. Chapitres 30 et 31 |
| « Le scanner ne remonte rien sur cette machine » | Peut-être qu'elle n'est pas vulnérable. Peut-être qu'elle n'a pas été scannée. Ce n'est pas la même information, et la distinction est traitée au §15.8 |

### 1.8 ⏱ État de l'art du domaine au 30 juillet 2026

*Bloc périssable. Vérifié le 30/07/2026. À réviser en priorité lors de la prochaine revue du cours.*

**Ce qui a changé récemment**

- **La priorisation par la seule gravité technique n'est plus défendable.** Le raisonnement « je corrige tout ce dont le score de gravité dépasse 7 » conduit à traiter plus de la moitié des vulnérabilités publiées, dont l'écrasante majorité ne sera jamais exploitée. Les approches par exploitation observée et par exposition réelle se sont imposées. Chapitre 16.
- **L'écosystème public de données de vulnérabilités s'est fragmenté.** Le NIST a annoncé qu'à compter du 15 avril 2026, l'enrichissement des fiches du NVD serait priorisé (vulnérabilités connues comme exploitées, logiciels utilisés par l'administration fédérale américaine, logiciels critiques), les autres pouvant porter la mention *Not Scheduled*. Attention à la formulation exacte : **toutes les vulnérabilités continuent d'être enregistrées** ; c'est l'enrichissement, c'est-à-dire l'analyse complémentaire, qui devient sélectif. En parallèle, la base européenne EUVD de l'ENISA est montée en charge et d'autres initiatives d'identification sont apparues. Chapitre 4. 📎 [S-16] [S-22]
- **La réglementation est passée du système d'information au produit.** Le Cyber Resilience Act européen impose des obligations aux fabricants de produits comportant des éléments numériques, y compris en matière de notification de vulnérabilités activement exploitées. Chapitres 8 et 33. 📎 [S-04] [S-05]

**Ce qui émerge**

- L'accélération de la découverte de vulnérabilités, notamment par des méthodes assistées par intelligence artificielle, accroît la pression sur la vitesse de remédiation plus que sur la qualité du triage. Chapitre 36.
- La généralisation progressive des inventaires de composants logiciels (SBOM) sous l'effet réglementaire, avec un usage réel encore très en retard sur la production de ces documents. Chapitre 25.

**Ce qui reste stable, et le restera**

L'inventaire, la propriété d'actif, la négociation des fenêtres, la preuve et le financement. Ces cinq points étaient les causes d'échec il y a vingt ans, ils le sont aujourd'hui, ils le seront encore quand les outils cités dans ce cours auront disparu.

**Ce qui devient obsolète**

- La campagne mensuelle unique et uniforme comme seule doctrine de correction, sans traitement différencié de l'urgence.
- Le pilotage par le nombre brut de vulnérabilités détectées, indicateur qui récompense l'inaction (ne rien scanner produit d'excellents chiffres).
- La dépendance à une source unique de données de vulnérabilités.

### 1.9 Comment lire ce cours

Le cours compte 40 chapitres, 3 cas de synthèse et 12 annexes. Il n'est pas conçu pour être lu intégralement d'un trait.

- **Partie I (ch. 1-6)** : à lire dans l'ordre. Elle installe le vocabulaire et le socle technique.
- **Parties II à VI** : consultables par thème. Chaque chapitre est autonome et renvoie explicitement aux autres.
- **Partie VII** : à traiter en dernier, en situation, avec les annexes ouvertes à côté.
- **Annexes** : ce sont des outils de travail, pas des compléments. Les annexes I (modèle de données), J (workflow de remédiation), K (indicateurs) et L (listes de contrôle) sont directement réutilisables.

Une matrice de parcours par profil figure en tête du document. Si vous découvrez le domaine, suivez le parcours « débutant technique » : il vous mènera à un niveau opérationnel sans passer par les chapitres de spécialisation.

🔴 **FIL ROUGE — octobre 2025 : la surprime**

*Le fil rouge de ce cours suit une organisation fictive, le groupe HELIOMED. Tout y est inventé — l'entreprise, les personnes, les incidents — mais rien n'y est irréaliste. Vous n'avez rien à connaître de ce contexte : il est décrit au fur et à mesure.*

HELIOMED est une entreprise de taille intermédiaire française : 1 380 salariés, 240 M€ de chiffre d'affaires. Elle fabrique des dispositifs médicaux connectés — des pompes à perfusion PX-40 — et édite une plateforme de télésuivi, HelioLink, complétée d'une passerelle hospitalière, HelioBox, et d'une application mobile de bien-être, HelioMove. Trois sites : Lyon (siège et direction des systèmes d'information), Saint-Étienne (usine), Nantes (recherche et développement logiciel).

Claire Nadeau prend son poste de responsable de la sécurité des systèmes d'information en octobre 2025. Elle est rattachée à la direction générale. Sa première semaine ne se passe pas comme prévu.

Le courtier en assurance appelle : l'assureur cyber ne renouvellera pas le contrat aux conditions précédentes. La cause tient en une ligne du rapport d'analyse : *absence de processus de gestion des correctifs démontrable*. Surprime demandée : 34 %.

Claire demande à voir le processus. Il existe. Il est écrit. Malik Ferhaoui, responsable de l'exploitation, applique consciencieusement les correctifs Microsoft chaque mois sur les serveurs. Ce qui n'existe pas, c'est :

- la liste exhaustive des actifs concernés — personne ne sait combien de serveurs sont réellement en service ;
- la trace de ce qui a été appliqué, où, et quand ;
- le traitement de tout ce qui n'est pas un serveur Windows : équipements réseau, hyperviseurs, automates de l'usine, applications hébergées chez des tiers ;
- une réponse à la question « qui décide d'arrêter tel serveur pour le corriger ? ».

Autrement dit : les cinq causes d'échec du §1.4, toutes présentes simultanément. Le processus n'est pas mauvais, il est *invisible* et *partiel*.

**Décision prise.** Claire ne lance pas d'appel d'offres outillage. Elle demande six semaines pour produire trois livrables : un inventaire réel du périmètre, une liste nominative de propriétaires d'actifs, et une mesure de l'écart entre ce que l'entreprise croit maintenir et ce qu'elle maintient effectivement.

**Livrable de l'épisode.** Une note d'une page à la direction générale, qui ne parle ni de vulnérabilités ni d'outils, et pose une seule question : *combien d'actifs devons-nous maintenir, et qui en est responsable ?*

→ La suite en 🔴 §2.9, où cette question rencontre son premier obstacle technique.

### Synthèse mentale du chapitre 1

La sécurité d'un système se dégrade sans qu'on y touche, parce que c'est le monde qui change autour de lui. Le MCS est l'ensemble des activités — techniques **et** organisationnelles — qui compensent cette dégradation sur tout le cycle de vie, décommissionnement compris, et qui en apportent la preuve. Il est plus large que la gestion des correctifs : dix objets se dégradent, dont les configurations, les identités, les certificats, les micrologiciels et le contenu de détection. Il est en tension permanente avec le maintien en condition opérationnelle, et cette tension se négocie, elle ne se tranche pas par autorité. Cinq causes expliquent la plupart des échecs — inventaire, propriété, fenêtres, preuve, financement — et aucune n'est technique. Enfin, le MCS ne protège ni contre une faille inconnue, ni contre l'hameçonnage, ni contre un défaut d'architecture : c'est une couche parmi d'autres.

**Trois questions de vérification**

1. Un serveur installé et parfaitement à jour, auquel personne ne touche pendant six mois, est-il toujours au même niveau de sécurité ? Justifiez en citant au moins trois des dix objets du §1.3.
2. Une organisation affiche 98 % de conformité aux correctifs. Quelles trois questions posez-vous avant d'accorder la moindre valeur à ce chiffre ?
3. Parmi les cinq causes d'échec du §1.4, laquelle doit être traitée en premier, et pourquoi investir dans l'outillage avant elle est-il une erreur de séquencement ?

---

## Chapitre 2 — Socle technique 1 : systèmes, paquets, cycles de support, réseau, identité

Ce chapitre installe les mécanismes concrets. Il ne suppose aucune expérience préalable d'administration, mais il ne survole rien : ces mécanismes expliquent la quasi-totalité des malentendus, des faux positifs et des échecs de correction que vous rencontrerez ensuite.

### 2.1 Anatomie d'un système à maintenir

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

### 2.2 Comment un correctif est réellement produit et distribué

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

#### Le *backport* : la notion qui fausse tous les scanners

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

#### Ce qui se passe quand l'éditeur ne reprend pas la correction

L'étape 4 peut aussi ne jamais avoir lieu. Trois cas fréquents :

- la version que vous utilisez n'est plus supportée : la correction existe en amont, elle ne viendra jamais chez vous ;
- l'éditeur juge la faille non applicable à sa configuration : c'est parfois justifié, parfois discutable, et cela doit être documenté ;
- le composant est fourni par un éditeur métier qui ne suit pas l'amont : vous dépendez alors entièrement de son bon vouloir, ce qui est un sujet contractuel (chapitre 13).

### 2.3 Chaînes de confiance : pourquoi vous pouvez installer ce paquet

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

### 2.4 Modèles de support : lire une matrice de cycle de vie

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

### 2.5 Le monde Windows : ce qu'il faut comprendre du mécanisme

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

### 2.6 Le monde Linux : paquets, redémarrages et correction à chaud

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

### 2.7 Équipements réseau et de sécurité : le maintien le plus risqué

Pare-feu, routeurs, commutateurs, passerelles d'accès distant, répartiteurs de charge : ces équipements concentrent trois caractéristiques qui en font le point le plus délicat du MCS.

**Ils sont exposés.** Beaucoup sont, par construction, joignables depuis Internet. C'est précisément leur fonction.

**Ils sont monolithiques.** Vous ne corrigez pas un composant : vous remplacez l'image logicielle complète. Toute mise à jour est donc une montée de version, avec son risque fonctionnel propre.

**Ils imposent une interruption.** Le redémarrage est presque toujours nécessaire, et il coupe le trafic.

Deux mécanismes atténuent ce dernier point.

**La double partition d'image.** La plupart des équipements professionnels stockent deux images logicielles. Vous installez la nouvelle sur la partition inactive, vous basculez au redémarrage, et en cas d'échec vous revenez à la précédente. C'est le seul véritable retour arrière du domaine, et il faut le tester avant d'en dépendre.

**La haute disponibilité.** Sur un couple d'équipements redondants, la séquence est toujours la même : mettre à jour le membre passif, vérifier, basculer le trafic, mettre à jour l'ancien membre actif, rebasculer. Cette séquence n'est **pas** sans effet : selon la conception du cluster et le degré de synchronisation d'état entre les membres, la bascule peut entraîner la perte des sessions établies — certains équipements synchronisent les tables de sessions, d'autres non, et le comportement diffère souvent selon les protocoles. Par ailleurs, les deux membres fonctionnent temporairement dans des versions différentes, ce que tous les constructeurs ne supportent pas. Ces deux points se vérifient dans la documentation **avant** l'intervention, pas pendant.

⚠️ **PIÈGE — la doctrine « toujours N-1 » appliquée sans nuance**
Beaucoup d'organisations se donnent pour règle de rester une version derrière la dernière publiée, afin d'éviter les régressions. La règle est raisonnable en régime normal. Elle devient dangereuse dans deux cas : quand la version N-1 est justement celle qui contient la faille exploitée, et quand l'écart s'installe et devient N-3 ou N-4 sans que personne ne le mesure. **Une doctrine de version doit être une décision datée et revue, pas une habitude.**

### 2.8 Identité : ce qu'un correctif ne corrigera jamais

Les services d'annuaire — annuaire d'entreprise sur site, annuaire d'identité en ligne — appellent une distinction fondamentale.

**Ce qu'un correctif corrige** : les vulnérabilités du logiciel d'annuaire lui-même.

**Ce qu'un correctif ne corrige pas** : tout ce qui s'est accumulé dans les données de l'annuaire depuis sa création. Comptes de personnes parties depuis des années, comptes de service créés pour un projet abandonné, délégations d'administration accordées lors d'une migration en 2014, appartenances à des groupes privilégiés jamais revues, protocoles d'authentification anciens laissés actifs pour un logiciel qui n'existe plus.

Cette accumulation porte un nom dans ce cours : la **dette de configuration d'annuaire**. Elle ne se dégrade pas toute seule, elle **croît** toute seule, à chaque projet, à chaque incident résolu dans l'urgence, à chaque migration. Aucune mise à jour ne la réduira. Le chapitre 24 y est consacré.

⚠️ **PIÈGE — le correctif à activation différée**
Certaines corrections de sécurité importantes ne s'activent pas à l'installation. L'éditeur les livre d'abord en mode « observation » — la nouvelle règle est appliquée mais les cas non conformes sont seulement journalisés, pour ne pas casser les environnements — puis annonce une date à laquelle le mode « application » deviendra obligatoire.

Ces déploiements en plusieurs phases sont un piège classique : l'organisation installe le correctif, coche la case, et découvre plusieurs mois plus tard, à la date d'application forcée, que des authentifications échouent parce que le travail intermédiaire — analyser les journaux, corriger les cas non conformes — n'a jamais été fait.

✅ **BONNE PRATIQUE (P0)** — Pour tout correctif comportant un calendrier d'application en plusieurs phases, créez immédiatement **deux** échéances dans votre suivi : la date d'installation, et la date de bascule en mode application. Entre les deux, une tâche explicite d'analyse des journaux d'observation, avec un propriétaire nommé. Un correctif resté en mode observation peut apporter une protection partielle — certaines vérifications sont déjà actives — mais **il n'apporte pas encore la protection complète attendue**, et c'est bien celle-ci que vous croyez avoir déployée.

### 2.9 La journalisation minimale pour prouver qu'un correctif est appliqué

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

### 2.10 📌 Ce que ce cours ne couvre pas, et où l'acquérir

Par honnêteté envers le lecteur débutant, voici ce que ce chapitre suppose acquis ou n'enseigne pas :

| Domaine | Ce que le cours suppose | Où combler |
|---|---|---|
| Administration système | Savoir se connecter à une machine et lire un journal | Cours d'administration Linux/Windows |
| Réseau | Comprendre adressage, routage, filtrage | Cours réseau généraliste |
| Développement | Rien n'est supposé ; les notions utiles sont expliquées aux ch. 6 et 25 | — |
| Cryptographie | Rien n'est supposé ; les notions utiles sont expliquées au ch. 24 | — |
| Gestion de vulnérabilités | **Rien n'est supposé** : c'est l'objet du chapitre 4 | — |

Le cours est autonome sur son sujet. Il ne l'est pas sur les disciplines voisines, et prétendre le contraire vous desservirait.

### Synthèse mentale du chapitre 2

Un système est un empilement de couches mises à jour par des mécanismes différents, à des rythmes différents, souvent par des personnes différentes — et la couche embarquée dans les applications n'est mise à jour par personne. Un correctif suit un trajet long, de l'amont jusqu'au chargement effectif du code corrigé, et il n'est efficace qu'au bout de ce trajet. Le rétroportage explique qu'un numéro de version amont ne dit rien de la présence d'une faille sur une distribution à support long : c'est la source de faux positifs la plus structurelle du domaine. Les chaînes de confiance cryptographiques garantissent l'origine d'un paquet, pas son innocuité, et leur rupture est silencieuse. Sous Windows, la réversibilité d'un correctif ne se suppose jamais ; sous Linux, l'installation ne suffit pas sans redémarrage des services concernés. Un annuaire ne se corrige pas par mise à jour : sa dette de configuration croît toute seule. Enfin, une preuve exploitable comporte six champs, dont la liste des actifs non joignables — celui qu'on oublie et que l'auditeur demandera.

**Trois questions de vérification**

1. Un scanner signale une bibliothèque en version 3.0.11 alors que la faille est corrigée en 3.0.15 amont. Quelles vérifications faites-vous, dans quel ordre, et quelle source fait finalement foi ?
2. Vous venez d'appliquer un correctif de bibliothèque sur cinquante serveurs Linux. Le travail est-il terminé ? Que vérifiez-vous, et avec quelle commande ?
3. Votre plan de retour arrière pour une campagne de correctifs Windows repose sur la désinstallation du paquet. Pourquoi est-ce fragile, et par quoi le remplacez-vous ?

---

## Chapitre 3 — Socle technique 2 : virtualisation, conteneurs, cloud, IaC, OT et micrologiciels

Le chapitre 2 décrivait le maintien d'une machine. Celui-ci décrit le maintien de tout ce qui n'est plus une machine : couches d'abstraction, environnements éphémères, ressources dont vous ne possédez pas le matériel, et systèmes industriels qui obéissent à d'autres lois.

**Ces technologies n'ont rien en commun techniquement.** L'hyperviseur, le conteneur, l'orchestrateur, le cloud, l'automate et le micrologiciel appartiennent à des mondes séparés, avec des équipes, des outils et des cultures différentes. Ce qui les rassemble ici est ailleurs : **chacune modifie la façon dont le maintien est réalisé, et déplace la ligne qui sépare ce que vous devez faire de ce qu'un autre fait pour vous.**

Le fil conducteur est donc unique : **à chaque couche d'abstraction ajoutée correspond une frontière de responsabilité, et c'est toujours sur ces frontières que le MCS échoue.**

### 3.1 Hyperviseurs et appliances virtuelles

Un hyperviseur héberge des dizaines de machines virtuelles. Il faut y distinguer **quatre objets à maintenir**, souvent confondus :

| Objet | Ce que c'est | Interruption induite |
|---|---|---|
| L'hôte | Le système de l'hyperviseur lui-même | Migration à chaud des machines, puis redémarrage de l'hôte |
| Les invités | Les systèmes des machines virtuelles | Chacun selon sa nature (voir ch. 2) |
| Le plan de gestion | La console qui pilote l'ensemble | Interruption de l'administration, pas de la production |
| Le micrologiciel du matériel | Serveur physique sous l'hyperviseur | Redémarrage physique complet |

**Le bon côté.** La migration à chaud permet de déplacer les machines virtuelles d'un hôte à l'autre sans interruption, donc de mettre à jour les hôtes sans coupure de service. C'est l'un des rares cas où le MCS ne coûte pas de disponibilité — à condition d'avoir provisionné la capacité nécessaire pour fonctionner avec un hôte en moins.

**Le mauvais côté.** Le plan de gestion est un actif de **niveau 0** : quiconque le contrôle contrôle toutes les machines virtuelles, leurs disques et leurs sauvegardes. Il est régulièrement en retard de plusieurs versions, parce que le mettre à jour « n'apporte rien aux métiers » et interrompt l'outil que les administrateurs utilisent tous les jours. C'est une inversion complète des priorités : cet actif doit être parmi les premiers maintenus, pas parmi les derniers.

⚠️ **PIÈGE — l'appliance virtuelle**
Une *appliance* virtuelle est une machine virtuelle préconstruite livrée par un éditeur. Elle contient un système d'exploitation complet que **vous ne maintenez pas** : l'éditeur interdit généralement d'y appliquer les correctifs du système, et fournit ses propres mises à jour, souvent moins fréquentes. Vous héritez donc de son rythme, de ses composants tiers et de ses éventuels retards. Traitez chaque appliance comme un actif dont le MCS est délégué, avec les exigences contractuelles correspondantes (chapitre 13).

### 3.2 Conteneurs : on ne corrige pas, on reconstruit

Un conteneur est un processus isolé, exécuté à partir d'une **image** : une pile de couches en lecture seule contenant le système de fichiers minimal nécessaire à l'application.

Le changement de paradigme est total, et il faut le comprendre pour le reste du cours :

> **On ne met pas à jour un conteneur. On reconstruit son image, et on remplace le conteneur.**

Se connecter à un conteneur en fonctionnement pour y lancer une mise à jour est possible techniquement, et à proscrire : la correction disparaîtra au premier redémarrage, et l'écart entre l'image de référence et la réalité en production deviendra invisible.

**La chaîne de correction devient donc :**

```
Correctif publié pour un composant
   → mise à jour de l'image de base
   → reconstruction de l'image applicative
   → nouvelle version publiée dans le registre
   → redéploiement progressif des conteneurs
```

Cette chaîne est bien plus rapide et plus fiable qu'une correction classique — quand elle est automatisée. Elle est catastrophique quand elle ne l'est pas : une image construite il y a deux ans et jamais reconstruite accumule silencieusement toutes les vulnérabilités publiées depuis, et rien dans le système d'exploitation hôte ne le signalera.

⚠️ **PIÈGE — l'étiquette mouvante**
Une étiquette d'image comme `:latest` ne désigne pas un contenu figé : elle pointe vers ce que le registre considère comme la dernière version, à un instant donné. Deux déploiements « identiques » à une semaine d'écart peuvent donc contenir des composants différents. Inversement, une étiquette figée pour garantir la reproductibilité gèle aussi les vulnérabilités.
**La bonne pratique** consiste à référencer une empreinte immuable pour la reproductibilité, **et** à disposer d'un processus qui met à jour cette référence à cadence maîtrisée. La reproductibilité sans cadence de reconstruction est une machine à fabriquer de l'obsolescence.

✅ **BONNE PRATIQUE (P1)** — Définissez et suivez une **cadence maximale de reconstruction** des images (par exemple : toute image en production a été reconstruite il y a moins de 30 jours). Cet indicateur préventif remplace avantageusement des dizaines de constats individuels dans le pilotage courant — sans dispenser de l'analyse de vulnérabilités : une image reconstruite hier peut embarquer une dépendance vulnérable, et une image plus ancienne peut porter un correctif rétroporté.

### 3.3 Kubernetes : la cadence vous est imposée

Kubernetes orchestre des conteneurs sur un ensemble de machines. Trois particularités le rendent structurant pour le MCS.

**Un rythme de publication soutenu et un support court.** Le projet publie environ trois versions mineures par an. Chaque version mineure reçoit **environ douze mois de support standard, suivis d'environ deux mois de maintenance limitée** — soit près de quatorze mois avant la fin de vie de la branche. Concrètement : **rester sur une version pendant deux ans n'est pas une option**, c'est une sortie de support. Le MCS d'un cluster n'est pas une activité occasionnelle, c'est un processus permanent, à inscrire au calendrier au même titre qu'une campagne de correctifs.
Les offres managées appliquent leurs propres calendriers, parfois plus courts, parfois assortis d'un support étendu payant : ce point est traité au chapitre 30. 📎 [S-27]

**Un écart de version encadré.** Les composants d'un cluster ne peuvent pas diverger arbitrairement : les règles d'écart autorisé entre le serveur d'API et les nœuds imposent un ordre de mise à jour et un nombre maximal de versions de retard. On met à jour le plan de contrôle d'abord, les nœuds ensuite, jamais l'inverse, et jamais en sautant plusieurs versions d'un coup.

**Des ruptures d'interface programmées.** Chaque version retire des interfaces dépréciées. Une mise à jour peut donc casser des déploiements parfaitement fonctionnels, non par régression, mais parce que le format de description qu'ils utilisent n'existe plus. Ce risque est **prévisible et annoncé longtemps à l'avance** : c'est un travail d'anticipation, pas un aléa.

📌 **LIMITES — ce qu'un service managé ne vous enlève pas**
Un cluster managé chez un fournisseur cloud prend en charge le plan de contrôle. Restent intégralement à votre charge : le choix du moment de la montée de version (dans la fenêtre imposée), la mise à jour des images de nœuds, les composants additionnels installés dans le cluster, la compatibilité de vos propres déploiements, et la migration des interfaces dépréciées. Et si vous ne décidez pas dans la fenêtre, **le fournisseur décidera pour vous** : c'est le sujet du chapitre 30.

### 3.4 Cloud : la frontière de responsabilité, service par service

Le modèle dit de « responsabilité partagée » est souvent cité et rarement décodé. Voici sa traduction opérationnelle.

| Modèle | Le fournisseur maintient | Vous maintenez |
|---|---|---|
| **Infrastructure (IaaS)** | Matériel, hyperviseur, réseau physique | **Tout** le système invité, comme une machine classique |
| **Plateforme (PaaS)** | Système et environnement d'exécution | Le **choix de version** et sa migration avant fin de support, votre code, vos dépendances, la configuration |
| **Logiciel (SaaS)** | L'application entière | Configuration, identités, droits, extensions, intégrations tierces, données |
| **Fonctions (*serverless*)** | Exécution et système | Version de l'environnement d'exécution, dépendances applicatives, permissions attachées |

🖼 **SCHÉMA — Empilement des couches et frontières de responsabilité.** *Pile verticale : matériel · micrologiciel · hyperviseur · système · runtime · bibliothèque · application, avec une ligne de démarcation mobile selon le modèle d'exécution.*

#### Le tableau à mémoriser

| Modèle d'exécution | Qui met à jour quoi |
|---|---|
| **Machine physique** | Vous : micrologiciel, système, applications |
| **Machine virtuelle** | Vous pour l'invité · l'équipe hyperviseur pour l'hôte et le plan de gestion |
| **Conteneur** | Vous reconstruisez l'image · l'équipe plateforme maintient les nœuds |
| **Infrastructure cloud (IaaS)** | Vous : tout l'invité · le fournisseur : matériel et hyperviseur |
| **Plateforme cloud (PaaS)** | Le fournisseur : système et exécution · **vous : le choix de version et sa migration avant échéance** |
| **Logiciel en ligne (SaaS)** | Le fournisseur : l'application · **vous : configuration, identités, extensions, intégrations** |
| **Fonctions (serverless)** | Le fournisseur : exécution · vous : version d'environnement, dépendances, permissions |
| **Appliance fournisseur** | Le fournisseur, à son rythme · vous : rien, sauf l'exposition |
| **Système industriel** | Le constructeur valide · vous appliquez pendant les arrêts |

⚠️ Les deux lignes qui produisent le plus d'angles morts sont **PaaS** — on croit que le fournisseur gère la version alors qu'il ne gère que l'exécution — et **appliance**, où l'on n'a aucune prise sauf sur l'exposition.

Trois enseignements en découlent.

**1. La responsabilité diminue, elle ne disparaît jamais.** Même en SaaS pur, la configuration du service, les comptes d'administration, les autorisations accordées à des applications tierces et les connecteurs restent à vous — et c'est précisément là que se produisent la majorité des incidents cloud. Chapitre 31.

**2. En PaaS, vous ne choisissez plus *si* vous migrez, seulement *quand*.** Le fournisseur annonce la fin de support d'une version d'environnement d'exécution ou de moteur de base de données, puis — selon le service et le contrat — impose une échéance, applique lui-même la migration, propose un support étendu payant, ou laisse le service fonctionner sans support. L'anticipation est le seul levier disponible dans les quatre cas.

**3. Les frontières se déplacent sans vous.** Un fournisseur peut modifier un comportement par défaut, retirer une option ou réinitialiser un paramètre de sécurité lors d'une mise à jour de son service. Votre configuration validée l'an dernier n'est pas garantie identique aujourd'hui. La veille sur les notes de version des services utilisés est une activité de MCS à part entière, traitée au chapitre 31.

### 3.5 Infrastructure décrite par le code et immutabilité

Deux idées, souvent confondues, qui changent profondément la façon de corriger.

**L'infrastructure décrite par le code** consiste à définir les ressources dans des fichiers versionnés plutôt que par des actions manuelles. Bénéfice pour le MCS : la configuration devient lisible, comparable et reproductible. Vous pouvez répondre à la question « quelle est la configuration de référence ? » — ce qui est impossible dans un environnement construit à la main.

**L'immutabilité** consiste à ne jamais modifier un serveur en fonctionnement : pour appliquer un correctif, on construit une nouvelle image, on déploie de nouvelles instances, et on retire les anciennes. C'est le modèle des conteneurs, transposé aux machines.

Ce que l'immutabilité apporte au MCS est considérable : la dérive de configuration locale disparaît largement, le retour arrière est simplifié — redéployer l'image précédente, à condition que données, schémas et dépendances restent compatibles —, et la correction devient un acte de déploiement standard plutôt qu'une opération d'exception.

⚠️ **PIÈGE — le code d'infrastructure est lui-même un actif à maintenir**
Les modules réutilisés, les connecteurs vers les fournisseurs cloud et les outils de description ont leurs propres versions, leurs propres vulnérabilités et leurs propres fins de support. Par ailleurs, l'écart entre ce que décrit le code et ce qui existe réellement — les ressources créées à la main dans l'urgence — est une forme de dérive particulièrement trompeuse, parce que le code donne l'illusion de la maîtrise. Chapitre 23.

### 3.6 Chaînes de construction et dépendances applicatives

Dans une application moderne, une part souvent importante — parfois majoritaire — du code exécuté n'a pas été écrite par l'équipe qui la maintient : bibliothèques externes, elles-mêmes dépendantes d'autres bibliothèques. La proportion exacte varie fortement selon le langage, l'écosystème et la maturité du projet ; ce qui est constant, c'est que cette part est rarement inventoriée.

**Deux notions à connaître dès maintenant.**

Le **fichier de verrouillage** enregistre la version exacte de chaque dépendance effectivement utilisée. Il garantit que la construction d'aujourd'hui produit le même résultat que celle d'il y a six mois. C'est indispensable à la reproductibilité — et c'est aussi un mécanisme de gel des vulnérabilités, exactement comme l'étiquette d'image figée du §3.2. Même remède : une cadence de mise à jour maîtrisée.

Les **dépendances transitives** sont celles que vous n'avez jamais choisies : votre application utilise A, qui utilise B, qui utilise C. La faille sera dans C. Vous ne pourrez la corriger qu'en attendant que B mette à jour C, sauf à forcer une résolution, ce qui comporte son propre risque.

**Les machines de construction sont des actifs à maintenir.** Les agents d'exécution des chaînes d'intégration disposent souvent d'accès étendus : registres d'images, environnements de déploiement, secrets. Ce sont des cibles de premier ordre, et ils échappent presque toujours à l'inventaire du parc. Le chapitre 28 leur est consacré.

### 3.7 Systèmes industriels (OT / ICS) : d'autres lois

Le monde industriel — automates, supervision, systèmes d'exécution de la production — obéit à des contraintes qui inversent plusieurs réflexes du monde bureautique.

**Le modèle de référence.** Le modèle de Purdue décrit une architecture en niveaux, du plus proche du terrain au plus proche de la bureautique :

```
Niveau 0   Capteurs, actionneurs — le procédé physique
Niveau 1   Automates, régulation
Niveau 2   Supervision (IHM), conduite locale
Niveau 3   Gestion de la production (MES), historisation
Niveau 3,5 Zone démilitarisée industrielle
Niveau 4/5 Systèmes d'information de gestion, bureautique
```

L'enjeu de MCS est concentré sur les niveaux 1 à 3, et sur l'étanchéité du niveau 3,5.

**Ce qui change fondamentalement.**

| Dimension | Informatique de gestion | Systèmes industriels |
|---|---|---|
| Contraintes dominantes | Confidentialité et intégrité | **Sûreté des personnes et disponibilité** — l'intégrité y est souvent directement liée à la sûreté |
| Durée de vie d'un équipement | 3 à 7 ans | **15 à 25 ans** |
| Fenêtre d'interruption | Nuit, week-end | **Arrêt de production annuel** |
| Validation d'un correctif | Interne | **Par le constructeur**, sous peine de perte de garantie |
| Conséquence d'une panne | Perte de service | **Risque physique** |

> **Le MCS ne change pas de principes en environnement industriel ; il change de contraintes.** Connaître, observer, décider, corriger, vérifier, prouver : la boucle est identique. Ce sont les fenêtres, les validations et les conséquences d'une erreur qui diffèrent.

**La conséquence pratique.** Appliquer un correctif non validé par le constructeur sur un automate peut faire tomber la garantie, invalider une certification, et — dans le pire des cas — perturber un procédé physique. La démarche du MCS industriel n'est donc pas « corriger plus vite », mais : **maîtriser l'exposition, préparer les correctifs longtemps à l'avance, et les appliquer pendant les arrêts planifiés.** Le chapitre 29 traite ce sujet en profondeur, y compris la chaîne complète de mise à jour hors ligne.

⚠️ **PIÈGE — le scan actif sur réseau industriel**
Un scan de vulnérabilités classique, banal en informatique de gestion, peut faire basculer un automate ancien en défaut : ces équipements ont des piles réseau minimalistes qui supportent mal les sollicitations inattendues. **Ne lancez pas de scan actif sur un réseau industriel sans validation explicite du constructeur ou de l'exploitant, sans test préalable et sans procédure d'arrêt.** La doctrine est : *passif par défaut, actif sous procédure* — un scan actif contrôlé reste possible, il ne s'improvise pas.

### 3.8 Micrologiciels, objets connectés et chaîne de démarrage

C'est la couche la plus basse, la moins visible, et celle où le retard est le plus important dans la plupart des organisations.

**Ce dont on parle.** Micrologiciel de carte mère (BIOS/UEFI), contrôleur de gestion à distance des serveurs, micrologiciels de disques et de cartes réseau, équipements connectés d'entreprise (impression, vidéosurveillance, contrôle d'accès, visioconférence).

**Pourquoi c'est critique.** Un composant qui s'exécute **avant** le système d'exploitation ne peut pas être surveillé par les protections qui s'exécutent **dans** le système d'exploitation. Une compromission à ce niveau survit à une réinstallation complète.

**Pourquoi c'est négligé.** La mise à jour est risquée (un échec peut rendre la machine inutilisable), rarement automatisable à grande échelle, souvent invisible des outils d'inventaire, et sans propriétaire clairement désigné entre l'équipe système, l'équipe poste de travail et les achats.

**Les mécanismes de protection à connaître.**

- **Le démarrage sécurisé** vérifie la signature de chaque composant chargé au démarrage, à partir de bases de certificats stockées dans le micrologiciel : une base d'autorisation et une base de révocation.
- **La signature des mises à jour** empêche l'installation d'un micrologiciel non authentique.
- **La protection contre le retour en arrière** empêche de réinstaller une version antérieure vulnérable — mécanisme indispensable, car sans lui un attaquant pourrait simplement « rétrograder » le composant pour retrouver une faille corrigée.

⏱ **ÉTAT DE L'ART — un cas d'école en cours (vérifié le 30/07/2026)**
Les certificats Microsoft de démarrage sécurisé émis en 2011 arrivent à expiration au terme de leurs quinze ans de validité : **KEK CA 2011** le 24 juin 2026, **UEFI CA 2011** le 27 juin 2026, **Windows Production PCA 2011** le 19 octobre 2026. Des certificats émis en 2023 les remplacent.

Ce cas mérite d'être étudié parce qu'il contient à lui seul cinq enseignements de MCS :

1. **La dégradation est silencieuse.** Une machine non mise à jour continue de démarrer normalement. Elle perd seulement la capacité de recevoir de futures révocations — donc toute protection contre les prochains logiciels malveillants de démarrage. Aucun tableau de bord de correctifs ne montrera ce manque.
2. **L'échéance était connue quinze ans à l'avance.** C'est le cas typique du §1.3 : la seule catégorie de dégradation entièrement prévisible est aussi celle qu'on découvre en retard.
3. **La correction dépend d'un tiers.** Sur une partie du parc, la mise à jour requiert une mise à jour de micrologiciel du constructeur. Sans elle, le processus reste en attente.
4. **Forcer la correction peut casser.** Contourner l'attente par une modification manuelle peut provoquer un échec de démarrage ou une demande de clé de récupération de chiffrement de disque. C'est l'illustration exacte du conflit MCO/MCS du §1.2.
5. **L'impact déborde l'éditeur concerné.** Les systèmes non-Windows dont le chargeur de démarrage est signé par la même autorité sont également concernés — une dépendance que peu d'organisations avaient cartographiée.

📎 [S-25] — documentation officielle et billet technique de l'éditeur, consultés le 30/07/2026.

✅ **BONNE PRATIQUE (P1)** — Créez une ligne d'inventaire dédiée aux micrologiciels, avec un propriétaire nommé, et traitez leur mise à jour par anneaux de déploiement comme n'importe quel correctif à risque (chapitre 18). Un parc dont aucun micrologiciel n'a jamais été mis à jour n'a pas « zéro vulnérabilité de micrologiciel » : il a **zéro visibilité**.

### 3.9 ⚠️ Les cinq endroits systématiquement oubliés

Synthèse des chapitres 2 et 3. Ces cinq zones échappent à presque tous les programmes de MCS naissants, et chacune a fait l'objet d'incidents majeurs documentés.

| # | Zone oubliée | Pourquoi elle échappe | Traité au |
|---|---|---|---|
| 1 | Environnements d'exécution et bibliothèques **embarqués dans les applications** | Hors gestionnaire de paquets, invisibles du système | Ch. 26 |
| 2 | **Plans de gestion** : hyperviseur, console de sauvegarde, outil de déploiement | « Ce n'est pas de la production » — alors que ce sont des actifs de niveau 0 | Ch. 28, 34 |
| 3 | **Micrologiciels** et chaîne de démarrage | Pas d'inventaire, pas de propriétaire, mise à jour risquée | Ch. 27 |
| 4 | **Modèles et images de référence** : images maîtres, modèles de machines virtuelles, instantanés | Une machine neuve naît vulnérable si son modèle ne l'est pas | Ch. 28 |
| 5 | **Configuration des services en ligne** : paramètres, extensions, connecteurs, autorisations déléguées | « C'est du SaaS, c'est maintenu » | Ch. 31 |

🔴 **FIL ROUGE — janvier 2026 : ce que la découverte réseau ne voyait pas**

L'inventaire de décembre (§2.9) aboutissait à un périmètre de référence de 221 actifs, dont 210 en service. En janvier, Claire Nadeau demande une seconde passe, orientée cette fois par les cinq zones ci-dessus plutôt que par le balayage réseau. Le résultat modifie l'échelle du problème.

- **Nantes (recherche et développement)** : quatre agents d'exécution de la chaîne d'intégration, créés par l'équipe de développement, hors du domaine, disposant d'un accès en écriture au registre d'images. Aucun n'apparaissait dans les 210 actifs en service : ils sont créés et détruits automatiquement, et n'existent souvent pas au moment où l'inventaire passe.
- **Saint-Étienne (usine)** : Thomas Berger, responsable maintenance, fournit un inventaire papier. Onze postes de supervision, dont deux sur des systèmes dont le support a pris fin en 2020, et trois automates dont le fournisseur ne publie plus de mise à jour depuis 2019. Aucun n'a jamais été scanné — et Thomas est formel : aucun ne le sera sans validation préalable.
- **Applications hébergées** : le service achats recense 38 abonnements à des services en ligne. Sept disposent de connecteurs avec accès en lecture à la messagerie de l'entreprise, autorisés entre 2019 et 2023, jamais revus depuis.
- **Modèles de machines virtuelles** : le modèle utilisé pour créer tout nouveau serveur Windows date de mars 2024. Chaque serveur créé depuis naît avec vingt-deux mois de correctifs de retard, rattrapés — quand ils le sont — au premier passage de la console de déploiement.
- **Micrologiciels** : aucune donnée. Le sujet n'a jamais eu de propriétaire.

**La décision qui compte.** Claire ne cherche pas à tout traiter. Elle formule une règle qui structurera tout le programme : *un actif sans propriétaire nommé n'est pas un actif maintenu, quelle que soit la qualité de l'outillage.* Chaque zone découverte reçoit un nom de propriétaire avant toute action technique — Malik pour les modèles et les micrologiciels, Yann Prigent pour les agents de construction, Thomas Berger pour l'usine, le service achats pour les abonnements en ligne.

**Livrable de l'épisode.** Un périmètre de référence en cinq domaines, avec un propriétaire par domaine, et une case explicite « micrologiciels : non couvert, propriétaire désigné, échéance de première mesure ». Déclarer un domaine non couvert **est** un livrable : c'est ce qui le rend finançable.

→ La suite en 🔴 §4.11, quand il faudra qualifier les premiers constats issus de ce périmètre.

### Synthèse mentale du chapitre 3

Chaque couche d'abstraction ajoute une frontière de responsabilité, et c'est sur ces frontières que le MCS échoue. Un hyperviseur impose de distinguer quatre objets à maintenir, dont un plan de gestion de niveau 0 souvent laissé en retard. Un conteneur ne se corrige pas : on reconstruit son image, ce qui rend la cadence de reconstruction plus informative que des dizaines de constats individuels. Un cluster d'orchestration impose son propre rythme, avec un support d'environ quatorze mois par version mineure et des ruptures d'interface annoncées à l'avance. Dans le cloud, la responsabilité diminue avec le niveau de service mais ne disparaît jamais, et les frontières se déplacent sans vous. L'infrastructure décrite par le code et l'immutabilité transforment la correction en déploiement standard — au prix de maintenir le code d'infrastructure lui-même. Le monde industriel inverse les priorités : disponibilité et sûreté des personnes d'abord, équipements sur quinze à vingt-cinq ans, correctifs validés par le constructeur, fenêtres annuelles. Enfin, la couche des micrologiciels est la plus basse, la plus critique et la moins inventoriée : sans propriétaire désigné, elle n'a pas zéro vulnérabilité, elle a zéro visibilité.

**Trois questions de vérification**

1. Votre organisation utilise une base de données managée chez un fournisseur cloud. Citez trois activités de MCS qui restent intégralement à votre charge.
2. Une image de conteneur en production a été construite il y a quatorze mois et n'a jamais été reconstruite. Le système d'exploitation des nœuds est parfaitement à jour. Où est le problème, et quel indicateur unique l'aurait révélé ?
3. Un responsable d'usine refuse tout scan de vulnérabilités sur son réseau industriel. A-t-il tort ? Que proposez-vous à la place, et quelle est la contrepartie de votre proposition ?

---


## Chapitre 4 — Socle vulnérabilités : identifiants, scores, écosystème

> ⚠️ **Avant de commencer.** Ce chapitre présente une dizaine de sigles en quelques pages. **N'essayez pas de les mémoriser à la première lecture.** Quatre d'entre eux suffisent au travail quotidien — ils sont identifiés au §4.10 — et les autres se consultent au besoin. Ce qui compte ici n'est pas de retenir les acronymes, c'est de comprendre **quelle question chacun répond, et laquelle il ne répond pas**.

Ce chapitre est le pivot du cours. Il installe le vocabulaire que tout le reste utilise, et il vous apprend surtout à **ne pas croire les chiffres** que produit cet écosystème — non parce qu'ils mentent, mais parce qu'ils ne mesurent presque jamais ce qu'on croit qu'ils mesurent.

Aucune connaissance préalable n'est supposée. Si vous n'avez jamais lu un bulletin de sécurité, vous saurez le faire à la fin.

### 4.1 Vocabulaire : six mots qu'on confond en permanence

| Terme | Définition précise | Ce qu'il n'est pas |
|---|---|---|
| **Faiblesse** | Un type de défaut de conception ou de programmation, décrit indépendamment de tout produit — par exemple « absence de vérification des droits avant une action » | Ce n'est pas une faille dans un logiciel précis |
| **Vulnérabilité** | L'instance concrète d'une faiblesse dans un produit et une version donnés | Ce n'est pas un risque : elle peut être inatteignable chez vous |
| **Exposition** | Le fait qu'un attaquant puisse **atteindre** le composant vulnérable | Une vulnérabilité sans exposition n'est pas exploitable |
| **Exploit** | Le code ou la procédure qui transforme la vulnérabilité en effet concret | Son existence publique ne prouve pas qu'il fonctionne partout |
| **Exploitation active** | L'observation, dans le monde réel, d'attaquants utilisant cette vulnérabilité | Ce n'est pas la simple existence d'un exploit |
| **Risque** | La combinaison vulnérabilité × exposition × exploitation × impact métier | Ce n'est jamais un score technique isolé |

Deux termes de calendrier viennent s'y ajouter, souvent employés à contresens :

- **0-day** : vulnérabilité pour laquelle **aucun correctif n'existe** au moment où elle est connue ou exploitée. L'éditeur a eu « zéro jour » pour corriger. Ce n'est pas synonyme de « très grave ».
- **n-day** : vulnérabilité pour laquelle un correctif existe depuis n jours. C'est **l'écrasante majorité des compromissions réelles** : les attaquants exploitent surtout ce qui est corrigé mais non appliqué. Retenez cette asymétrie, elle justifie à elle seule l'existence de ce cours.

⚠️ **PIÈGE — « c'est une 0-day » comme justification d'inaction**
Beaucoup d'organisations se rassurent en se disant qu'elles ne peuvent rien contre les 0-day. C'est vrai — et hors sujet, parce que ce n'est pas par là qu'elles se font attaquer. Le MCS traite les n-day, c'est-à-dire le cas où **vous aviez le correctif et ne l'avez pas appliqué**.

### 4.2 CVE : comment un identifiant naît, et pourquoi sa qualité varie

**Le besoin.** Sans identifiant commun, votre scanner, votre éditeur, votre prestataire et votre auditeur parlent de la même faille avec quatre noms différents. Le programme CVE (*Common Vulnerabilities and Exposures*) résout ce problème : un identifiant unique, de la forme `CVE-2026-12345`.

**Ce qu'un identifiant CVE est, exactement.** Une **clé de dédoublonnage**. Rien de plus. Il ne dit pas si la faille est grave, ni si elle est exploitée, ni si elle vous concerne.

**Qui les attribue.** Des organisations accréditées appelées **CNA** (*CVE Numbering Authorities*) : éditeurs de logiciels pour leurs propres produits, centres de réponse aux incidents, projets open source, chercheurs. Elles reçoivent un bloc d'identifiants et les attribuent de façon autonome.

C'est ce point qui explique la variabilité de qualité, et il faut le comprendre pour ne pas s'étonner ensuite :

| Ce qui varie selon la CNA | Conséquence pratique |
|---|---|
| Le niveau de détail de la description | Certaines fiches disent tout, d'autres une ligne vague |
| La présence et la justesse des versions affectées | Sans versions précises, aucune corrélation automatique n'est possible |
| L'attribution ou non d'un score de gravité | Deux CNA peuvent scorer différemment la même classe de défaut |
| La rapidité de publication | Certaines publient avant le correctif, d'autres bien après |
| La granularité | Un éditeur peut regrouper dix défauts sous un identifiant, un autre en créer dix |

**Le cycle de vie d'une fiche.** Réservation d'un identifiant → publication de la fiche → enrichissements successifs (versions, références, scores) → parfois contestation, rejet ou fusion. Une fiche consultée le jour de sa publication et la même fiche trois semaines plus tard peuvent être très différentes.

✅ **BONNE PRATIQUE (P1)** — Ne figez jamais une décision de triage sur la première version d'une fiche publiée dans les 48 heures. Prévoyez explicitement un **rejeu** des constats récents : ce qui semblait mineur lundi peut être requalifié vendredi.

### 4.3 Nommer les produits : CWE, CPE, purl — et pourquoi la corrélation échoue

Trois nomenclatures cohabitent, avec des rôles distincts.

**CWE — la nature du défaut.** Un catalogue de *types* de faiblesses : injection, débordement, mauvaise gestion des droits, condition de course. Une CVE peut être rattachée à une ou plusieurs CWE lorsque la nature de la faiblesse est connue et correctement renseignée — ce qui n'est pas systématique : certaines fiches n'ont pas de rattachement fiable, d'autres portent une catégorie générique, d'autres encore sont enrichies après publication. Utilité pour le MCS : repérer qu'un même type de défaut revient chez le même fournisseur, ce qui est un signal de qualité du produit — et un argument contractuel (chapitre 13).

**CPE — l'identification d'un produit.** Une chaîne normalisée décrivant éditeur, produit, version, édition. C'est ce qui permet à un outil de dire « la CVE affecte ce produit, or ce produit est installé ici ».

📌 **LIMITES — pourquoi la corrélation par CPE produit tant de bruit**
- Le nom du produit dans la fiche CVE et le nom du paquet installé sur votre machine ne se ressemblent pas toujours.
- Les intervalles de versions affectées sont souvent exprimés de manière imprécise, ou pas du tout.
- Le rétroportage (§2.2) rend la comparaison de version fausse par construction sur les systèmes à support long.
- Un même logiciel peut exister sous plusieurs identifiants selon qui l'a déclaré.
- Les composants embarqués dans une application n'ont généralement aucun identifiant produit.

**purl — l'identification d'un paquet logiciel.** Une notation plus récente et beaucoup plus adaptée aux écosystèmes de développement, de la forme `pkg:type/espace-de-noms/nom@version`. Elle décrit sans ambiguïté un paquet dans son écosystème d'origine. Il est largement utilisé dans les inventaires de composants logiciels modernes (§4.8), là où CPE reste le format historique des bases de vulnérabilités — avec une couverture qui varie selon les formats et les outils.

Retenez la conséquence opérationnelle : **une part importante des faux positifs de vos scanners ne vient pas de leur mauvaise qualité, mais de l'impossibilité structurelle de faire correspondre parfaitement deux nomenclatures conçues pour des usages différents.** Le chapitre 15 en fait un chapitre entier.

### 4.4 CVSS : ce que le score mesure, et ce qu'on lui fait dire

**CVSS** (*Common Vulnerability Scoring System*) attribue une note de 0 à 10. C'est le chiffre que tout le monde connaît, et le plus mal utilisé du domaine.

**Ce qu'il mesure.** La **gravité technique intrinsèque** d'une vulnérabilité : à quel point elle est difficile à exploiter, quels privilèges elle exige, quelle interaction utilisateur elle suppose, et quels impacts elle produit sur la confidentialité, l'intégrité et la disponibilité du composant touché.

**La structure, en quatre groupes.**

| Groupe | Contenu | Qui le renseigne |
|---|---|---|
| **Base** | Caractéristiques intrinsèques et invariantes de la vulnérabilité | L'éditeur ou la CNA |
| **Menace** | Maturité du code d'exploitation à un instant donné | Rarement renseigné en pratique |
| **Environnement** | Adaptation à **votre** contexte : criticité de l'actif, mesures déjà en place | **Vous** — et presque personne ne le fait |
| **Complémentaire** | Informations qualitatives (sûreté, automatisabilité, récupérabilité) | Optionnel |

La version 4 du standard a notamment clarifié la distinction entre l'impact sur le **système vulnérable** et l'impact sur les **systèmes en aval**, et introduit une notation explicite indiquant quels groupes ont été utilisés — un score « base seule » n'a pas le même statut qu'un score enrichi de la menace et de l'environnement.

⚠️ **PIÈGE — les cinq erreurs d'interprétation les plus coûteuses**

| Erreur | Pourquoi c'est faux |
|---|---|
| « Score 9,8 = à corriger en priorité » | Le score de base ignore totalement votre exposition. Une faille 9,8 sur un service désactivé n'est pas un risque |
| « Score 5,3 = pas urgent » | Certaines failles de gravité moyenne sont massivement exploitées parce qu'elles sont triviales à automatiser |
| « Le score est objectif » | Il est calculé à partir de choix humains dans une grille. Deux analystes peuvent diverger |
| « Le score évolue avec la menace » | Le groupe Base est conçu pour être stable dans le temps : il ne reflète pas l'apparition d'un exploit public. Un vecteur publié peut néanmoins être corrigé ou révisé par son émetteur |
| « C'est la même chose qu'un niveau de risque » | Il manque l'exposition, la criticité métier et l'impact organisationnel |

> ### 🎯 La phrase à retenir de ce chapitre
> **CVSS décrit la gravité technique d'une vulnérabilité. Il ne décrit pas votre priorité opérationnelle.**
> Toute la suite du cours découle de cette distinction.

**Le bon usage.** CVSS mesure une **sévérité**, pas un risque — la documentation du standard le dit explicitement 📎 [S-18]. Il répond à la question « **quelle est la gravité technique si cette faille est exploitée ?** ». C'est une entrée utile parmi d'autres. Il ne répond ni à « est-ce exploité ? », ni à « suis-je atteignable ? », ni à « qu'est-ce que ça me coûte ? ».

### 4.5 EPSS : la probabilité, et ses angles morts

**EPSS** (*Exploit Prediction Scoring System*) répond à une question différente et complémentaire : **quelle est la probabilité que cette vulnérabilité soit exploitée dans les trente prochains jours ?**

Le résultat est un nombre entre 0 et 1, accompagné d'un **percentile** indiquant la position relative de la vulnérabilité par rapport à toutes les autres.

**Ce qui change tout.** La distribution est extrêmement asymétrique : l'immense majorité des vulnérabilités publiées ont une probabilité d'exploitation très faible, et une petite fraction concentre presque tout le risque réel. C'est précisément ce qui rend une priorisation par gravité seule inefficace : elle traite comme équivalentes des milliers de vulnérabilités qui ne seront jamais exploitées et quelques dizaines qui le seront.

🧪 **EN PRATIQUE — lire correctement un couple de valeurs**
Une vulnérabilité à 0,08 de probabilité et 96ᵉ percentile signifie : *il y a environ 8 % de chances qu'elle soit exploitée dans les trente jours, et elle est malgré tout plus menaçante que 96 % des autres.* Les deux informations sont nécessaires : la probabilité pour dimensionner l'effort, le percentile pour arbitrer entre constats.

📌 **LIMITES — ce qu'EPSS ne sait pas**
- Il prédit l'exploitation **dans le monde**, pas chez vous. Il ignore totalement votre exposition et votre criticité métier.
- Il repose sur des signaux observables : une exploitation ciblée, discrète, contre un petit nombre d'organisations est mal captée par construction.
- La **transparence est partielle** : la méthode générale et les principes du modèle sont publics, mais le consommateur ne dispose ni des données d'entraînement, ni des poids, ni des signaux ayant produit un score donné — il ne peut donc ni reproduire ni auditer une valeur particulière.
- La probabilité est **volatile** : elle monte brutalement à la publication d'un exploit, puis redescend. Un score consulté il y a trois semaines n'a pas de valeur.

⚠️ **PIÈGE — la discontinuité entre versions de modèle**
Le modèle évolue par versions successives, et un changement de version **déplace tous les scores en même temps**. Conséquence directe et sous-estimée : une série temporelle qui traverse un changement de version n'est pas comparable. Si votre indicateur « nombre de vulnérabilités à forte probabilité » chute de 30 % en une semaine sans qu'aucun correctif n'ait été appliqué, cherchez d'abord un changement de modèle avant de féliciter vos équipes.

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — La version 5 du modèle a commencé à publier ses scores le **15 juin 2026**. Toute série historique franchissant cette date doit être signalée comme discontinue dans vos tableaux de bord. 📎 [S-17]

### 4.6 Les catalogues d'exploitation avérée

Un troisième signal, de nature complètement différente : non plus une prédiction, mais un **constat**.

L'agence américaine de cybersécurité maintient un catalogue de vulnérabilités **connues comme exploitées** (couramment appelé catalogue KEV). Trois critères d'inscription : un identifiant CVE attribué, une **preuve fiable d'exploitation active**, et une action de remédiation claire disponible.

**Pourquoi c'est un signal très fort.** Il n'y a ni probabilité, ni modèle, ni interprétation : quelqu'un a observé l'exploitation. En pratique, l'appartenance à ce catalogue est l'un des meilleurs déclencheurs d'une procédure d'urgence — mais pas un déclencheur suffisant à lui seul, puisqu'il ne couvre ni immédiatement les campagnes ciblées, ni les vulnérabilités sans identifiant.

📌 **LIMITES — ce que le catalogue ne dit pas**
- **Il est incomplet par construction.** Il recense ce qui a été observé **et** publié. Les attaques ciblées contre un secteur, ou celles détectées sans être divulguées, n'y figurent pas.
- **Il est en retard.** L'inscription suit l'observation, qui suit l'exploitation. Ne pas y figurer ne signifie pas « pas exploité », mais « pas encore observé publiquement ».
- **Il est orienté par son public.** Il sert d'abord les administrations américaines ; les produits dominants dans d'autres marchés peuvent y être sous-représentés.
- **Il ne dit rien de votre exposition.** Une vulnérabilité massivement exploitée sur un produit que vous n'utilisez pas ne vous concerne pas.

⚠️ Ne construisez jamais une doctrine du type « nous ne traitons en urgence que ce qui figure au catalogue ». Vous obtiendriez un processus lisible, défendable — et systématiquement en retard sur les campagnes visant votre secteur.

### 4.7 Décider plutôt que scorer : les approches par arbre de décision

Un score produit un nombre ; il faut ensuite décider quoi en faire. Les approches par **arbre de décision** franchissent directement l'étape suivante : elles produisent une **action**.

Le principe est simple et transposable à n'importe quelle organisation. On pose quelques questions binaires ou ternaires, dans un ordre fixé, et chaque combinaison de réponses mène à une décision explicite.

🧪 **EN PRATIQUE — la structure d'un arbre de décision de remédiation**

```
1. Exploitation observée ?        aucune / démonstration publique / active
2. Automatisable à grande échelle ?              oui / non
3. Impact technique en cas de succès ?      partiel / total
4. Effet sur les missions et les personnes ?  faible / … / critique
                       ↓
       Surveiller · Surveiller de près · Traiter · Agir en urgence
```

L'intérêt majeur de cette forme est qu'elle est **auditable** : on ne discute plus d'un chiffre, on discute des réponses aux questions. Et le jour où vous devez justifier de ne pas avoir corrigé, vous produisez le chemin parcouru dans l'arbre plutôt qu'un seuil arbitraire.

Une approche complémentaire, plus récente, consiste à estimer la probabilité qu'une vulnérabilité **ait déjà été exploitée par le passé**, en agrégeant l'historique des prédictions plutôt qu'en regardant leur valeur du jour. Elle répond à une limite réelle des catalogues d'exploitation avérée — leur incomplétude — sans prétendre la supprimer.

✅ **BONNE PRATIQUE (P0)** — Quelle que soit la méthode retenue, **écrivez-la**. Une règle de priorisation non écrite est une règle qui varie selon la personne, la fatigue et le mois. Le modèle complet est construit au chapitre 16 et formalisé en Annexe C.

### 4.8 De l'inventaire logiciel à l'exploitabilité déclarée : SBOM, VEX, CSAF

Trois briques récentes, souvent confondues, qui répondent à trois questions distinctes.

| Brique | Question à laquelle elle répond | Produite par |
|---|---|---|
| **SBOM** | *Que contient ce logiciel ?* | Le fournisseur, ou vous, à la construction |
| **VEX** | *Ce composant vulnérable rend-il ce produit exploitable ?* | Le fournisseur du produit |
| **CSAF** | *Comment publier un avis de sécurité lisible par une machine ?* | L'éditeur qui publie l'avis |

**SBOM** — l'inventaire des composants d'un logiciel, avec leurs versions et leurs relations de dépendance. Deux formats principaux coexistent, tous deux largement outillés. L'enjeu n'est pas de choisir : c'est de savoir **quoi en faire**. Un inventaire de composants que personne ne rapproche d'une base de vulnérabilités est un document mort.

**VEX** — la réponse à un problème très concret. Votre outil détecte un composant vulnérable dans un produit ; le fournisseur sait, lui, que le code vulnérable n'est jamais appelé dans son produit. Un document VEX transporte cette information sous une forme exploitable, avec quatre états possibles : *non affecté*, *affecté*, *corrigé*, *en cours d'analyse* — et, pour l'état « non affecté », une justification normalisée.

**CSAF** — le format d'avis de sécurité lisible par une machine. Il permet d'automatiser ce qui est aujourd'hui fait à la main : lire un bulletin, en extraire les produits et versions concernés, les rapprocher de l'inventaire.

📌 **LIMITES — l'écart entre la promesse et la réalité de terrain**
La production de ces documents progresse plus vite que leur consommation. Beaucoup d'organisations reçoivent des inventaires de composants qu'elles archivent sans jamais les exploiter, faute d'outillage ou de processus. Un inventaire fourni n'est utile que s'il est **à jour**, **rapproché de l'inventaire d'actifs**, et **rejoué à chaque nouvelle vulnérabilité publiée** — trois conditions rarement réunies. Le chapitre 25 traite la mise en œuvre réelle.

### 4.9 ⏱ L'écosystème des données de vulnérabilités au 30 juillet 2026

*Bloc périssable. Vérifié le 30/07/2026.*

Le point à comprendre est structurel, et il survivra aux détails ci-dessous : **l'écosystème s'est fragmenté**, et la dépendance à une source unique est devenue un risque opérationnel.

**Ce qui a changé.**

- Le NIST a annoncé qu'à compter du **15 avril 2026**, l'enrichissement des fiches de sa base nationale serait **priorisé** : vulnérabilités connues comme exploitées, logiciels utilisés par l'administration fédérale américaine, logiciels critiques. Formulation exacte, importante : **toutes les vulnérabilités continuent d'être enregistrées** ; ce sont les analyses complémentaires — scores, correspondances produit, classification — qui deviennent sélectives, les autres fiches pouvant porter la mention *non programmé*.
- L'agence européenne de cybersécurité a mis en service une **base européenne de vulnérabilités**, alimentée notamment par les CSIRT nationaux, qui constitue désormais une source alternative crédible.
- D'autres initiatives d'attribution d'identifiants, indépendantes du programme historique, ont vu le jour et sont utilisables en complément.

📎 [S-16] pour l'évolution du NVD · [S-22] pour la base européenne.

**Ce que ça change pour vous, concrètement.**

| Si votre processus repose sur… | Alors |
|---|---|
| Le score de gravité fourni par une base unique | Une part croissante de vos constats arrivera sans score |
| La correspondance automatique produit fournie par cette base | Cette correspondance sera absente pour une partie des fiches |
| Un seuil du type « traiter au-dessus de 7 » | Ce seuil devient inapplicable sur les fiches non enrichies |

✅ **BONNE PRATIQUE (P0)** — Construisez votre chaîne de veille sur **au moins trois sources de nature différente** : l'avis de l'éditeur du produit concerné (source de vérité sur les versions), une base agrégée (dédoublonnage et couverture), et un signal d'exploitation avérée. Le détail opérationnel est au chapitre 14.

### 4.10 📌 Ce qu'aucun score ne saura jamais : votre exposition

Récapitulons ce que chaque signal apporte, et surtout ce qu'aucun n'apporte.

| Signal | Répond à | Ne répond pas à |
|---|---|---|
| Gravité technique | Si elle est exploitée, quel dégât ? | Est-elle exploitée ? Suis-je atteignable ? |
| Probabilité d'exploitation | Sera-t-elle exploitée dans le monde ? | Chez moi ? Sur cet actif ? |
| Catalogue d'exploitation avérée | A-t-elle été observée en exploitation ? | Suis-je concerné ? Suis-je exposé ? |
| Arbre de décision | Que dois-je faire ? | *(il faut lui fournir l'exposition en entrée)* |

Les trois premiers signaux sont produits **hors de chez vous**. Aucun ne connaît :

- si le service vulnérable est activé sur vos machines ;
- s'il est joignable depuis Internet, depuis le réseau bureautique, ou depuis nulle part ;
- si une mesure de contournement est déjà en place ;
- si l'actif porte une donnée critique ou un procédé industriel ;
- si sa compromission ouvre l'accès à d'autres actifs.

**C'est vous qui apportez la moitié manquante de l'équation, et personne d'autre ne peut le faire à votre place.**

#### Ce que vous manipulerez réellement au quotidien

Sur la dizaine de notions présentées dans ce chapitre, quatre seulement interviennent chaque jour :

| Au quotidien | Pourquoi |
|---|---|
| **L'avis de l'éditeur** du produit concerné | La seule source de vérité sur « suis-je affecté, et quelle version corrige » |
| **Le signal d'exploitation avérée** | Le déclencheur d'urgence le plus fiable |
| **Votre cartographie d'exposition** | Elle transforme un constat en priorité |
| **Votre inventaire enrichi de criticité** | Il transforme une priorité en décision |

Les autres — nomenclatures de produits, modèles de probabilité, formats d'inventaire et d'exploitabilité — sont des **outils de soutien** : utiles quand vous en avez besoin, à consulter plutôt qu'à mémoriser. C'est aussi pour cela que les deux dernières lignes du tableau, qui ne dépendent d'aucun fournisseur, sont les plus robustes de tout le dispositif. C'est aussi la raison pour laquelle le chapitre 11 (exposition et chemins d'attaque) est placé avant le chapitre 16 (triage) : sans connaissance de l'exposition, la meilleure méthode de priorisation du monde travaille sur une entrée manquante.

### 4.11 🔬 Mini-lab 1 — Qualifier dix constats hétérogènes

**Objectif** — Typer un constat avant de le prioriser, et reconnaître ceux qui n'ont pas d'identifiant de vulnérabilité.
**Durée** 30 min · **Difficulté** 🟢 débutant · **Prérequis** §4.1 à §4.7, §14.7 · **Livrable** tableau de qualification typée.
**Compétences validées** — ✔ distinguer les origines de constats ✔ identifier la source de vérité d'un constat ✔ qualifier en fait / hypothèse / piste ✔ repérer un constat qui n'a pas d'identifiant de vulnérabilité

**Énoncé.** Voici dix constats arrivés la même semaine dans la boîte de réception d'une équipe de sécurité. Pour chacun : (a) de quel **type de constat** s'agit-il ? (b) quelle est sa **source de vérité** ? (c) quelle **information manque** pour décider ? (d) fait vérifié, hypothèse probable ou piste exploratoire ?

| # | Constat |
|---|---|
| 1 | Le scanner remonte une bibliothèque de chiffrement en version antérieure à la version corrigée en amont, sur 42 serveurs à support long |
| 2 | Un bulletin d'éditeur annonce une « faille critique d'exécution de code », sans identifiant CVE, avec une version corrigée |
| 3 | Un rapport de test d'intrusion signale une interface d'administration accessible sans authentification sur un port non standard |
| 4 | Une vulnérabilité de gravité 5,3 vient d'entrer au catalogue d'exploitation avérée |
| 5 | L'équipe de développement signale qu'une dépendance transitive de l'application métier est marquée vulnérable par l'outil d'analyse de composition |
| 6 | Un fournisseur SaaS annonce qu'un paramètre de sécurité par défaut change à la prochaine mise à jour |
| 7 | Le service comptable a reçu une facture pour un abonnement à un service en ligne inconnu de la DSI |
| 8 | Un chercheur signale par courriel une faille dans votre produit, avec une preuve de concept fonctionnelle et un délai de 90 jours |
| 9 | La supervision remonte que 14 agents de sécurité n'ont pas mis à jour leur base de détection depuis 21 jours |
| 10 | Une vulnérabilité de gravité 9,8 est publiée sur un composant présent dans votre parc, mais uniquement exploitable en accès physique local |

**Corrigé commenté**

| # | Type | Source de vérité | Information manquante | Statut |
|---|---|---|---|---|
| 1 | Vulnérabilité de composant, **probable faux positif de rétroportage** | Avis de sécurité de la distribution + révision du paquet installée | La révision éditeur réelle sur les 42 serveurs (§2.2) | Piste exploratoire tant que la révision n'est pas vérifiée |
| 2 | Vulnérabilité sans identifiant — **le MCS ne se réduit pas aux CVE** | L'avis de l'éditeur lui-même | Versions exactes déployées ; l'absence de CVE n'atténue rien | Fait vérifié sur l'existence, hypothèse sur l'impact |
| 3 | Écart de configuration / **exposition**, pas une vulnérabilité logicielle | Le rapport de test, rejoué et confirmé | Qui possède cet actif ? Depuis quand ? Traces d'accès ? | Fait vérifié — et probablement le constat le plus grave des dix |
| 4 | Vulnérabilité **à exploitation avérée** | Le catalogue + l'avis éditeur | Suis-je exposé ? La gravité modérée est ici sans importance | Fait vérifié — traitement en urgence malgré le 5,3 |
| 5 | Vulnérabilité de **dépendance transitive** | Inventaire de composants + déclaration d'exploitabilité du fournisseur | Le code vulnérable est-il atteignable dans l'application ? (§25.12) | Hypothèse probable |
| 6 | **Changement fournisseur** — activité de MCS à part entière (§3.4) | Les notes de version du fournisseur | Quels paramètres, quel effet sur ma configuration validée ? | Fait vérifié, impact à instruire |
| 7 | **Actif orphelin** découvert par une source non technique | La facture, puis la confirmation métier | Quelles données ? Quel connecteur ? Quel propriétaire ? | Fait vérifié sur l'existence |
| 8 | **Divulgation coordonnée** reçue en tant que fabricant | Le chercheur, puis la reproduction interne | Reproductible ? Quelles versions livrées ? Horloge des 90 jours (ch. 33) | Hypothèse jusqu'à reproduction |
| 9 | **Dégradation du contenu de détection**, pas une vulnérabilité (§1.3, ch. 34) | La console de l'outil, recoupée sur les postes | Pourquoi 21 jours ? Agents muets ou machines éteintes ? | Fait vérifié |
| 10 | Vulnérabilité grave mais **non atteignable à distance** | L'avis éditeur, lu jusqu'au vecteur d'accès | Existe-t-il des accès physiques non maîtrisés ? | Fait vérifié — priorité basse malgré le 9,8 |

**Les trois erreurs attendues.** Trier ces dix constats par gravité technique — cela placerait le n° 10 en tête et le n° 3 en queue, exactement à l'envers. Écarter les constats 6, 7 et 9 comme « hors sujet MCS » — ils en font pleinement partie. Traiter le n° 1 comme un fait avant vérification de la révision éditeur — et engager 42 interventions inutiles.

🔴 **FIL ROUGE — février 2026 : la semaine des 4 300 constats**

Le premier scan authentifié sur le périmètre réconcilié (§2.9) produit 4 312 constats. Malik Ferhaoui applique la règle qu'il connaît : gravité supérieure ou égale à 7. Il obtient 1 176 constats à traiter. À raison de vingt minutes par constat pour deux personnes, cela représente près de deux ans de travail.

Claire Nadeau demande un autre découpage, en trois questions seulement : *est-ce observé en exploitation ? est-ce atteignable depuis l'extérieur ? l'actif est-il critique ?*

| Filtre | Constats restants |
|---|---|
| Total brut | 4 312 |
| Gravité ≥ 7 (méthode initiale) | 1 176 |
| Exploitation avérée, tous niveaux de gravité confondus | 31 |
| … dont sur un actif joignable depuis Internet | **7** |
| … dont sur un actif de niveau 0 ou critique métier | **3** |

Les sept constats exposés incluent une vulnérabilité de gravité 5,9 sur la passerelle d'accès distant, que la méthode initiale écartait. Elle sera au cœur du cas de synthèse A.

**Décision prise.** La priorisation ne sera plus fondée sur la gravité seule. Trois entrées obligatoires : exploitation observée, exposition, criticité de l'actif. Et une règle qui deviendra un principe de la maison : *un constat que l'on choisit de ne pas traiter doit être écrit, daté et signé — pas oublié dans un rapport.*

**Livrable de l'épisode.** Un premier arbre de décision d'une page, imparfait, appliqué dès la semaine suivante. La version aboutie est construite au chapitre 16.

→ La suite en 🔴 §5.5, quand il faudra désigner qui décide d'arrêter une machine.

### Synthèse mentale du chapitre 4

Un identifiant de vulnérabilité est une clé de dédoublonnage, pas un jugement : sa qualité dépend entièrement de l'organisation qui l'a attribué. La gravité technique mesure les dégâts en cas d'exploitation, jamais la probabilité qu'elle survienne ni votre exposition. La probabilité d'exploitation comble une partie du manque mais reste mondiale, volatile et discontinue entre versions de modèle. Les catalogues d'exploitation avérée sont le signal le plus fort et le plus incomplet : ne pas y figurer ne veut pas dire ne pas être exploité. Les approches par arbre de décision produisent directement une action et se défendent en audit, ce qu'un seuil chiffré ne fait pas. Les inventaires de composants, les déclarations d'exploitabilité et les avis lisibles par machine sont produits plus vite qu'ils ne sont consommés. Enfin, l'écosystème s'est fragmenté : dépendre d'une source unique est devenu un risque, et la moitié de l'équation — votre exposition — n'est produite par personne d'autre que vous.

**Trois questions de vérification**

1. Une vulnérabilité de gravité 5,3 vient d'entrer dans un catalogue d'exploitation avérée ; une autre est notée 9,8 mais n'exige aucun privilège et n'est exploitable qu'en accès physique. Laquelle traitez-vous en premier, et avec quel argument devant un comité ?
2. Votre tableau de bord « vulnérabilités à forte probabilité d'exploitation » chute de 30 % en une semaine sans aucun déploiement. Quelles sont les deux causes à vérifier avant de communiquer ce résultat ?
3. Un fournisseur vous transmet un inventaire des composants de son produit. Quelles trois conditions doivent être réunies pour que ce document ait une valeur opérationnelle chez vous ?

---

## Chapitre 5 — Socle processus : changement, risque, propriété, normes, preuve

Les chapitres 2 à 4 ont installé la technique. Celui-ci installe ce qui, dans la pratique, décide de tout : **qui a le droit de faire quoi, quand, et comment on le prouve**. C'est le chapitre le moins spectaculaire du cours et l'un des plus déterminants — les cinq causes d'échec du §1.4 sont toutes ici.

### 5.1 La gestion du changement, alliée ou frein

**Le principe.** Dans toute organisation structurée, modifier un système en production suppose une autorisation. Cette discipline existe pour une bonne raison : la première cause d'indisponibilité, statistiquement, n'est pas l'attaque, c'est le changement mal maîtrisé.

**Les trois catégories universelles.**

| Catégorie | Définition | Autorisation | Usage en MCS |
|---|---|---|---|
| **Changement standard** | Pré-autorisé, procédure connue, risque évalué une fois pour toutes | Aucune validation au cas par cas | **C'est ici que doit vivre le MCS courant** |
| **Changement normal** | Nouveau ou risqué, examiné individuellement | Comité de validation | Montées de version majeures, changements d'architecture |
| **Changement d'urgence** | Traité hors délai normal, régularisé après | Validation restreinte, souvent a posteriori | Correctif de crise (chapitre 21) |

**L'erreur de conception la plus répandue.** Faire passer chaque campagne de correctifs mensuelle en changement normal. Le résultat est mécanique : le comité devient un goulot d'étranglement, les délais s'allongent, et les équipes finissent par contourner le processus — ce qui détruit à la fois la traçabilité et la confiance.

✅ **BONNE PRATIQUE (P0) — faire du MCS courant un changement standard**
Construisez un dossier de changement standard couvrant votre campagne récurrente : périmètre, procédure, tests, critères d'arrêt, plan de retour arrière, fenêtre. Faites-le valider **une fois**. Ensuite, chaque campagne s'exécute sans repasser en comité, et seuls les cas sortant du cadre y remontent. Vous transformez un frein en accélérateur, sans perdre la traçabilité — au contraire, elle devient homogène.

🏢 **VU EN RÉUNION** — Un comité de changement examine une campagne mensuelle de correctifs. Le représentant métier demande la liste des serveurs concernés, puis : « et si ça casse ? ». L'exploitation répond « on a un instantané ». Le comité valide. Personne n'a demandé combien de temps prend la restauration d'un instantané sur ces serveurs — la réponse était de quarante minutes, et le service avait un engagement de disponibilité de quinze minutes. Le §18.8 existe à cause de ce genre de séance.

⚠️ **PIÈGE — le changement d'urgence qui devient la norme**
Quand le processus standard est trop lourd, tout devient une urgence. Symptôme mesurable : la part des changements d'urgence dans le total. Au-delà de 15 à 20 %, ce n'est plus un indicateur de réactivité, c'est le signe que votre processus normal ne fonctionne pas. Suivez ce ratio (chapitre 38).

### 5.2 Fenêtres, gels et calendriers métier

**La fenêtre de maintenance** est un créneau pendant lequel une interruption est acceptée par les métiers. C'est une ressource rare, et le MCS n'en est pas le seul consommateur : projets, montées de version applicatives, opérations d'infrastructure s'y disputent la place.

**Trois principes de négociation qui fonctionnent.**

1. **Négocier des fenêtres récurrentes, pas des interventions.** Obtenir « le deuxième jeudi de chaque mois, de 22 h à 2 h » une seule fois vaut mieux que douze négociations annuelles. Chaque négociation individuelle a un coût, et ce coût produit du report.
2. **Différencier par criticité.** Un actif de niveau 0 mérite une fenêtre courte et fréquente ; un serveur secondaire peut se contenter d'une fenêtre trimestrielle plus large. Les classes de service du chapitre 7 formalisent ce découpage.
3. **Prévoir la fenêtre d'urgence dès maintenant.** Le jour de la crise, personne n'a le temps de négocier. Faites acter à l'avance : *en cas de vulnérabilité exploitée sur un actif exposé, l'interruption est autorisée sous délai de X heures, par décision de Y.* C'est une décision de gouvernance qui se prend à froid (chapitre 9).

**Les gels de production.** Périodes où tout changement est interdit : clôture comptable, campagne commerciale, fin d'année, pic saisonnier. Elles sont légitimes et non négociables sur le principe. Deux points d'attention :

- Un gel n'est **jamais** absolu en sécurité : il doit comporter une clause explicite de levée pour vulnérabilité exploitée, avec le décideur nommé.
- L'accumulation des gels peut réduire l'année à quelques semaines réellement disponibles. Faites le calcul et présentez-le : *« nous disposons de 14 semaines exploitables sur 52 »* est un argument autrement plus efficace qu'une demande de moyens.

### 5.3 Analyse de risque appliquée au MCS

Vous n'avez pas besoin d'être expert en analyse de risque pour faire du MCS. Vous avez besoin de trois notions.

**Le risque résiduel.** Ce qui reste après application des mesures. Il n'est jamais nul, et le reconnaître explicitement est un acte de maturité, pas un aveu de faiblesse. Un programme de MCS qui prétend supprimer le risque est un programme qui ment à sa direction.

**L'acceptation formalisée.** Décider de ne pas corriger est une décision légitime — **à condition** qu'elle soit prise par la bonne personne, écrite, datée, bornée dans le temps, assortie de mesures compensatoires et revue à échéance. Non formalisée, c'est un oubli ; formalisée, c'est une décision de gestion. La différence entre les deux est ce que regarde un auditeur, et ce que regarde un juge.

**La méthode structurée, quand elle est utile.** Les démarches d'analyse de risque par ateliers successifs — cadrage et socle de sécurité, identification des sources de risque, scénarios stratégiques, scénarios opérationnels, traitement — apportent au MCS deux choses précises : elles obligent à nommer **qui** vous attaquerait et **pourquoi**, ce qui oriente la priorisation vers les chemins réellement plausibles ; et elles produisent une échelle de gravité **métier**, indispensable pour transformer une criticité technique en criticité d'actif.

⚠️ **PIÈGE — l'analyse de risque comme préalable bloquant**
N'attendez pas une analyse complète pour démarrer un programme de MCS. Une classification de criticité à trois niveaux, imparfaite mais appliquée, vaut infiniment mieux qu'une analyse exhaustive attendue pendant dix-huit mois. Commencez avec ce que vous avez, affinez ensuite.

### 5.4 Lire une exigence de conformité : la grille en trois niveaux

Vous allez rencontrer des référentiels — normes, réglementations, référentiels sectoriels, questionnaires clients. Une seule grille de lecture suffit à ne jamais s'y perdre.

| Niveau | Question | Exemple générique | Qui le fixe |
|---|---|---|---|
| **Exigence** | Que dois-je obtenir ? | « Les vulnérabilités techniques doivent être identifiées et traitées en temps utile » | Le texte |
| **Objectif de sécurité** | Quel résultat concret cela suppose-t-il ? | « Détecter les vulnérabilités du parc et les corriger selon des délais définis par criticité » | Le référentiel d'application |
| **Moyen de conformité** | Comment je le fais chez moi ? | « Scan authentifié mensuel, arbre de décision, délais de 7/30/90 jours, dérogations tracées » | **Vous** |

**Les deux erreurs symétriques.**

- **Confondre exigence et moyen** : croire qu'un texte impose un outil ou une fréquence précise. C'est presque toujours faux — les textes fixent des résultats, pas des implémentations. Cela vous laisse une liberté que beaucoup n'exploitent pas.
- **Croire que le moyen suffit** : avoir un scanner et une procédure ne démontre rien. Ce qui est évalué, c'est le **résultat** et sa **preuve**.

Le principe de **proportionnalité** figure dans la plupart des référentiels modernes : les mesures attendues sont proportionnées à la taille de l'organisation, à son exposition et à la criticité de ses activités. C'est un levier de négociation légitime, à condition d'être capable de **justifier** votre calibrage — donc de l'avoir écrit.

### 5.5 La propriété d'actif : la question qui débloque tout

Nous arrivons à la cause d'échec n° 2 du §1.4, et sans doute à la phrase la plus utile de ce cours.

> Pour chaque actif, une seule question doit avoir une réponse **nominative** : *qui décide qu'on l'arrête pour le corriger ?*

**Pourquoi cette formulation.** « Qui est responsable de ce serveur ? » obtient des réponses floues et collectives. « Qui décide de l'arrêter ? » n'admet qu'un nom. Et c'est exactement la décision qui bloque en pratique.

**Les cinq rôles à distinguer**, parce que les confondre produit l'essentiel des blocages :

| Rôle | Ce qu'il fait | Ce qu'il ne fait pas |
|---|---|---|
| **Propriétaire métier** | Décide de l'interruption, arbitre le risque, porte le budget | Il n'exécute pas |
| **Propriétaire technique** | Exploite, applique, vérifie, produit la preuve | Il ne décide pas de l'arrêt |
| **Éditeur / constructeur** | Produit le correctif, définit les prérequis | Il ne connaît pas votre contexte |
| **Intégrateur** | A construit le système, connaît ses dépendances | Il n'est souvent plus là |
| **Infogérant** | Exécute selon contrat | **Il ne porte jamais la décision d'accepter un risque** (chapitre 13) |

⚠️ **PIÈGE — la propriété collective**
« C'est l'équipe infrastructure » n'est pas une réponse. Une équipe ne prend pas de décision d'interruption à 3 h du matin ; une personne le fait. Exigez un nom, et un suppléant. Sans cela, votre programme s'arrêtera au premier arbitrage.

✅ **BONNE PRATIQUE (P0) — la campagne de désignation**
Nommer les propriétaires est un exercice de trois à six semaines, pas un projet. Méthode qui fonctionne : extraire la liste des actifs, proposer un propriétaire pressenti pour chacun, envoyer la liste aux responsables concernés avec une règle explicite — *sans retour sous quinze jours, la désignation proposée est réputée acceptée*. Le silence devient une acceptation, et la liste se remplit. Les actifs pour lesquels personne ne se reconnaît sont votre priorité réelle : ce sont les **actifs orphelins**, et ils sont presque toujours ceux qui posent problème.

🔴 **FIL ROUGE — mars 2026 : trois noms et un refus**

Claire Nadeau lance la campagne de désignation sur les 221 actifs du périmètre de référence. Trois retours illustrent tout le chapitre.

**Le cas simple.** Sonia Weber, directrice des systèmes d'information, accepte d'être propriétaire métier des serveurs d'infrastructure centraux et désigne Malik Ferhaoui comme propriétaire technique. Fenêtre récurrente négociée : deuxième jeudi du mois, 22 h - 2 h. Pour ces actifs, le MCS devient un changement standard dès avril.

**Le cas de la négociation.** Thomas Berger refuse d'être désigné propriétaire des onze postes de supervision de l'usine tant qu'aucune fenêtre n'est définie : « je ne peux pas m'engager sur quelque chose que je n'ai pas le droit d'arrêter ». Il a raison, et sa réponse est plus constructive qu'une acceptation de façade. La discussion aboutit à un compromis : il devient propriétaire, avec une fenêtre unique lors de l'arrêt de production d'août, et l'engagement écrit que toute intervention hors de cette fenêtre relève d'une décision de la direction générale, pas de la sécurité.

**Le cas révélateur.** Vingt-neuf actifs ne trouvent aucun propriétaire — l'essentiel des machines de test non déclarées et des appliances virtuelles d'éditeurs. Personne ne les revendique, et personne ne demande non plus leur arrêt. Claire applique une règle qui deviendra structurante : *tout actif orphelin depuis plus de trente jours entre dans une procédure d'extinction programmée, avec préavis de quinze jours diffusé largement.* Sur les vingt-neuf, onze trouvent immédiatement un propriétaire — le préavis a réveillé leurs utilisateurs. Huit sont éteints sans conséquence. Dix relèvent d'un décommissionnement en règle (chapitre 35).

**Décision prise.** La désignation nominative devient un prérequis d'entrée en production : aucun nouvel actif n'est mis en service sans propriétaire métier et propriétaire technique nommés.

**Livrable de l'épisode.** Le référentiel de propriété, intégré à la base d'inventaire — les champs correspondants figurent en Annexe I.

→ La suite en 🔴 §6.15, quand ces engagements rencontrent une architecture qui ne permet pas de les tenir.

### 5.6 Ce qui a valeur de preuve, et ce qui n'en a pas

Le §2.9 a posé les six champs d'une preuve technique. Élargissons au niveau organisationnel.

| Élément | Valeur probante | Condition |
|---|---|---|
| Politique écrite et validée | Faible seule, indispensable en support | Datée, versionnée, approuvée nominativement |
| Compte rendu de comité | Bonne pour les **décisions** | Décisions explicites, pas un relevé de discussion |
| Extraction d'outil | Bonne pour l'**état** | Datée, périmètre défini, non retouchée, actifs injoignables listés |
| Journal système | Forte | Horodaté, intègre, conservé |
| Fiche de dérogation | Forte pour justifier une **non-action** | Signataire, durée, mesure compensatoire, date de revue |
| Déclaration orale ou courriel | Nulle | — |

**La règle qui résume tout** : une preuve répond à *qui, quoi, quand, sur quel périmètre, et qu'est-ce qui manque*. Le dernier terme est celui qui distingue un professionnel d'un amateur — un rapport qui n'énonce pas ses trous est un rapport qu'on ne peut pas croire.

### 5.7 Trois familles d'indicateurs à ne pas confondre

Dernière notion du socle, et source d'innombrables tableaux de bord inutiles.

| Famille | Question | Exemple | Piège |
|---|---|---|---|
| **Activité** | Qu'avons-nous fait ? | Nombre de correctifs déployés ce mois | Récompense l'agitation ; ne dit rien du résultat |
| **Résultat** | Où en sommes-nous ? | Part des actifs critiques conformes, sur périmètre de référence | Nécessite un dénominateur solide |
| **Risque** | Que craignons-nous ? | Nombre d'actifs exposés portant une vulnérabilité exploitée | Le seul qui parle à une direction générale |

⚠️ **PIÈGE — l'indicateur qui récompense l'inaction**
« Nombre de vulnérabilités détectées » est un indicateur d'activité déguisé en indicateur de risque. Il s'améliore quand vous scannez moins. C'est l'archétype de la métrique qu'il ne faut pas présenter à un comité — le chapitre 38 en recense une dizaine d'autres, et l'Annexe K fournit les définitions rigoureuses.

→ **Chapitre 6 — Architecture maintenable : le MCS *by design*** : la conception — parce que le coût du MCS se décide avant la mise en service.

### Synthèse mentale du chapitre 5

Le MCS courant doit vivre en changement standard, pré-autorisé une fois pour toutes : le faire passer en comité à chaque campagne transforme la gouvernance en goulot d'étranglement et pousse les équipes à contourner le processus. Les fenêtres se négocient de façon récurrente et différenciée par criticité, et la fenêtre d'urgence se décide à froid, jamais pendant la crise. Décider de ne pas corriger est légitime dès lors que la décision est prise par la bonne personne, écrite, bornée, compensée et revue — c'est ce qui sépare un oubli d'une décision de gestion. Face à un référentiel, distinguez l'exigence, l'objectif et le moyen : les textes fixent des résultats, le moyen vous appartient, et c'est le résultat prouvé qui est évalué. La question qui débloque le plus de situations n'est pas « qui est responsable ? » mais « qui décide qu'on l'arrête ? », et elle n'admet qu'un nom. Enfin, une preuve dit qui, quoi, quand, sur quel périmètre — et ce qui manque.

**Trois questions de vérification**

1. Votre campagne mensuelle de correctifs passe en comité de validation à chaque itération et accuse trois semaines de retard moyen. Que changez-vous, et qu'obtenez-vous en échange de cette simplification ?
2. Un référentiel exige que « les vulnérabilités techniques soient traitées en temps utile ». Votre direction vous demande quel outil il faut acheter. Que répondez-vous ?
3. Quinze actifs de votre parc n'ont aucun propriétaire identifié depuis quatre mois. Quelle procédure appliquez-vous, et pourquoi le préavis est-il l'élément clé du dispositif ?

---

## Chapitre 6 — Architecture maintenable : le MCS *by design*

### 6.1 La thèse du chapitre

Les chapitres précédents décrivaient comment maintenir ce qui existe. Celui-ci change de moment : il traite des décisions prises **avant** la mise en service, et qui déterminent le coût de tout le reste.

> **Un système mal conçu pour être mis à jour produira de la dette de sécurité, quelle que soit la qualité du processus de MCS qui s'y applique.**

Ce n'est pas une opinion, c'est une conséquence mécanique. Si arrêter un système coûte 40 000 € de production perdue, aucune politique de correctifs ne convaincra qui que ce soit de l'arrêter chaque mois. Si une application est couplée à une version précise de son environnement d'exécution, aucun outil ne permettra de faire évoluer cet environnement. Si aucun retour arrière n'existe, chaque correctif restera une prise de risque non couverte, et sera reporté.

Le corollaire est encourageant : **les gains les plus importants du MCS ne s'obtiennent pas en exploitation, ils s'obtiennent en conception** — et ils ne coûtent presque rien s'ils sont décidés au bon moment.

Ce chapitre s'adresse à trois publics : ceux qui conçoivent des systèmes, ceux qui les achètent ou les font réaliser, et ceux qui les exploitent et doivent expliquer pourquoi ils n'y arrivent pas.

### 6.2 La maintenabilité comme exigence opposable

Le problème pratique : la maintenabilité de sécurité n'apparaît dans aucun cahier des charges, donc personne n'y répond, donc elle n'existe pas.

La solution consiste à la formuler comme une exigence explicite, vérifiable en revue de conception et opposable à un fournisseur. Sept exigences suffisent à couvrir l'essentiel.

| # | Exigence | Formulation opposable |
|---|---|---|
| 1 | Interruptibilité | « Le système supporte l'arrêt d'un composant sans interruption de service pour l'utilisateur » |
| 2 | Découplage de version | « Le système n'impose pas une version figée de son système d'exploitation, de son environnement d'exécution ou de sa base de données » |
| 3 | Réversibilité | « Toute mise à jour dispose d'une procédure de retour arrière documentée et testée » |
| 4 | Observabilité du changement | « Le système expose des indicateurs permettant de constater un effet de bord dans les minutes suivant une mise à jour » |
| 5 | Cadence supportée | « Le système supporte l'application de correctifs de sécurité à une cadence mensuelle » |
| 6 | Inventoriabilité | « Le système déclare ses composants et leurs versions de manière lisible par une machine » |
| 7 | Fin de vie | « Le fournisseur s'engage sur une durée de support et un préavis de fin de support » |

✅ **BONNE PRATIQUE (P0)** — Insérez ces sept exigences dans vos cahiers des charges et vos grilles de revue d'architecture. Elles ne coûtent rien à écrire, elles se négocient au moment où vous avez encore un levier — avant la signature — et elles vous éviteront des années de dérogations. Les exigences 2, 3 et 7 sont celles qui produisent le plus d'effet.

### 6.3 Redondance et haute disponibilité réellement compatibles avec la mise à jour

**L'idée de base.** Si un service tourne sur deux instances au lieu d'une, vous pouvez en arrêter une pour la corriger pendant que l'autre continue de servir. La redondance transforme une interruption de service en simple réduction de capacité. C'est le levier le plus direct entre architecture et MCS.

**Ce qui la rend inopérante en pratique.** Il existe beaucoup de redondances de façade.

⚠️ **PIÈGE — les cinq faux clusters**

| Configuration | Pourquoi ça ne tient pas |
|---|---|
| Deux instances, mais capacité dimensionnée pour deux | En arrêter une sature l'autre : vous ne pouvez plus jamais patcher aux heures ouvrées |
| Deux instances, une base de données unique | La base reste un point unique de panne — et c'est elle qu'il faut corriger |
| Redondance active/passive jamais basculée | La bascule n'a pas été testée depuis 2021 ; personne n'ose |
| Instances redondées, session utilisateur non partagée | Chaque bascule déconnecte les utilisateurs : les métiers refusent |
| Redondance sur le service, pas sur ses dépendances | Le service est doublé, l'annuaire ou le stockage ne l'est pas |

**Le test de vérité**, à poser en revue d'architecture : *pouvez-vous arrêter un membre de ce cluster, maintenant, en pleine journée, sans prévenir personne ?* Si la réponse n'est pas un oui franc, la redondance existe pour la panne, pas pour la maintenance — et c'est une distinction que beaucoup d'organisations découvrent trop tard.

### 6.4 Trois stratégies de déploiement, et quand chacune vaut son coût

| Stratégie | Principe | Coût | Retour arrière | Adaptée à |
|---|---|---|---|---|
| **Progressive** (*rolling*) | Remplacement instance par instance | Faible | Lent (repasser en sens inverse) | Services sans état, nombreuses instances |
| **Bleu / vert** | Deux environnements complets, bascule du trafic | Élevé (double infrastructure) | **Immédiat** | Systèmes critiques, fenêtres impossibles |
| **Témoin** (*canary*) | Une petite fraction du trafic sur la nouvelle version | Moyen | Rapide | Tout ce dont on veut mesurer l'effet réel |

**Ce qu'il faut vraiment retenir.** Ces stratégies ne servent pas seulement à déployer des fonctionnalités : elles sont l'outil qui permet d'appliquer un correctif **sans pari**. Le déploiement témoin en particulier répond exactement au dilemme du chapitre 18 — corriger vite tout en limitant l'impact d'une régression.

📌 **LIMITES** — Aucune de ces stratégies ne s'applique telle quelle à un composant à état : une base de données, un annuaire, un automate industriel. Elles supposent que l'on peut faire coexister deux versions, ce qui nous amène au point suivant.

### 6.5 Découpler le déploiement de l'activation

Un mécanisme simple change profondément la gestion du risque : séparer **installer le code** de **activer le comportement**.

Un interrupteur de fonctionnalité (*feature flag*) est un paramètre qui active ou désactive un comportement sans redéployer. Le bénéfice pour le MCS est direct et sous-estimé :

- vous déployez la nouvelle version avec le nouveau comportement désactivé, donc sans risque fonctionnel ;
- vous activez ensuite progressivement, sur une population réduite ;
- en cas de problème, vous **désactivez en quelques secondes** au lieu de redéployer l'ancienne version.

C'est aussi le mécanisme qui rend possible une mesure compensatoire propre : désactiver une fonctionnalité vulnérable en attendant le correctif, sans arrêter le service (chapitre 20).

⚠️ **PIÈGE** — Les interrupteurs s'accumulent. Un système comptant 400 interrupteurs dont personne ne connaît l'état est devenu impossible à raisonner, et les combinaisons non testées deviennent la norme. Fixez une durée de vie : un interrupteur temporaire qui dépasse six mois est soit supprimé, soit promu en paramètre de configuration documenté.

### 6.6 Compatibilité entre versions et contrats d'interface

Pour qu'un déploiement progressif fonctionne, deux versions doivent **coexister** — au moins quelques minutes, parfois plusieurs jours. Cela impose une discipline.

**La compatibilité descendante** : la nouvelle version doit continuer à comprendre ce que produit l'ancienne. **La compatibilité ascendante**, plus rarement pensée : l'ancienne version ne doit pas se casser en recevant ce que produit la nouvelle.

**Les règles pratiques qui suffisent dans 90 % des cas :**

- ajouter un champ, jamais en supprimer ni en renommer dans la même version ;
- ne jamais changer le sens d'un champ existant ;
- déprécier avant de supprimer, avec un délai annoncé et mesuré ;
- versionner explicitement les interfaces exposées à d'autres équipes ou à des clients ;
- traiter un point d'accès déprécié comme un actif à décommissionner (chapitre 35), avec une date.

**Le lien avec le MCS est direct** : une interface sans compatibilité impose un déploiement synchronisé de tous les composants, donc une interruption globale, donc une fenêtre rare, donc du report.

### 6.7 Migrations de schéma : le point de non-retour

C'est le cas le plus dangereux du chapitre, parce qu'il annule silencieusement votre plan de retour arrière.

**Le mécanisme.** Une mise à jour applicative modifie la structure de la base de données. Le code applicatif, lui, se réinstalle facilement en version antérieure. Les **données**, non : elles ont été transformées. Vous pouvez redéployer l'ancienne version du code, elle ne saura plus lire la base.

**Ce que ça implique.** Le retour arrière cesse d'être une opération technique de quelques minutes pour devenir une **restauration de sauvegarde**, avec perte de toutes les transactions depuis la migration. La différence, en durée d'indisponibilité, est d'un facteur cent.

🧪 **EN PRATIQUE — la migration en expansion / contraction**

La méthode qui préserve la réversibilité consiste à découper en trois temps ce qu'on fait habituellement en un seul :

```
Étape 1 — Expansion   : ajouter la nouvelle structure, SANS retirer l'ancienne
                        → les deux versions du code fonctionnent
Étape 2 — Migration   : le nouveau code écrit dans les deux structures
                        → réversible à tout moment
Étape 3 — Contraction : retirer l'ancienne structure, une fois la stabilité confirmée
                        → point de non-retour, franchi consciemment et à froid
```

Entre l'étape 1 et l'étape 3, le retour arrière reste trivial. Le point de non-retour n'est pas supprimé, il est **déplacé** à un moment que vous choisissez, au calme, plutôt que subi en pleine nuit.

✅ **BONNE PRATIQUE (P1)** — Toute demande de changement impliquant une migration de schéma doit indiquer explicitement, dans son plan de retour arrière : *à partir de quel instant précis le retour arrière ne sera plus possible sans restauration de données*. Cette seule ligne change la nature de la discussion en comité.

### 6.8 Observabilité et critères d'arrêt automatiques

Déployer progressivement ne sert à rien si vous ne savez pas détecter que ça se passe mal. C'est pourtant la situation la plus fréquente : on déploie sur 5 % du parc, puis on attend « un peu », puis on continue — sans critère.

**Ce qu'il faut mesurer, avant / pendant / après.** Trois familles suffisent :

| Famille | Exemples | Ce qu'elle détecte |
|---|---|---|
| Santé technique | Taux d'erreur, temps de réponse, redémarrages inattendus, consommation mémoire | Régression franche |
| Santé fonctionnelle | Nombre de transactions métier abouties par minute | Régression silencieuse : le service répond, mais ne fait plus son travail |
| Santé du déploiement | Taux d'échec d'installation, actifs non joignables, écarts de version | Problème de la campagne elle-même |

La deuxième ligne est celle qu'on oublie, et c'est la plus importante. Un service qui répond « 200 OK » à toutes les requêtes tout en ayant cessé d'enregistrer les commandes passe tous les contrôles techniques.

**Le critère d'arrêt automatique.** Un déploiement doit s'interrompre **tout seul** quand un seuil est franchi, sans attendre qu'un humain regarde un écran. Formulez-le à l'avance et de manière chiffrée : *si le taux d'erreur dépasse X sur Y minutes, ou si le volume de transactions abouties baisse de Z %, la campagne s'arrête et alerte.*

⚠️ **PIÈGE — le seuil défini après le déploiement**
Un seuil discuté pendant l'incident sera toujours interprété dans le sens de « on continue » : personne n'aime arrêter une campagne à moitié faite. Le seuil doit être écrit dans la demande de changement, avant.

### 6.9 Le retour arrière : ce qui est réellement réversible

Reprenons le §2.5 et généralisons.

| Objet | Réversibilité réelle | Mécanisme à privilégier |
|---|---|---|
| Application sans état | Élevée | Redéploiement de la version antérieure |
| Conteneur | Très élevée | Redéploiement de l'image précédente |
| Machine virtuelle | Élevée | Instantané pris avant l'intervention |
| Correctif de système d'exploitation | **Variable, à vérifier** | Instantané ou redéploiement, jamais la désinstallation seule |
| Micrologiciel | Faible à nulle | Double partition d'image quand elle existe (§2.7) |
| Migration de schéma | **Nulle après contraction** | Découpage expansion/contraction (§6.7) |
| Modification d'annuaire | Faible | Sauvegarde autorisée + procédure documentée |

**La règle unique** : un plan de retour arrière **non testé** n'est pas un plan, c'est une intention. Testez-le sur un environnement représentatif, chronométrez-le, et notez sa durée dans la demande de changement — parce que c'est cette durée, et non la probabilité de l'incident, qui déterminera si vous osez déployer.

### 6.10 Images immuables : la correction devient un déploiement ordinaire

Le §3.5 a présenté le principe. Voici ce qu'il change concrètement pour le MCS.

Dans un modèle mutable, corriger consiste à intervenir sur un système en fonctionnement : opération d'exception, à risque, difficile à répéter à l'identique, et qui laisse le système dans un état légèrement différent de tous les autres.

Dans un modèle immuable, corriger consiste à **reconstruire l'image de référence et à redéployer**. Autrement dit : la correction emprunte exactement le même chemin, les mêmes tests et les mêmes automatismes qu'une livraison applicative ordinaire. Elle cesse d'être un sujet à part.

Quatre bénéfices, tous directement mesurables :

1. la dérive de configuration disparaît par construction (chapitre 23) ;
2. le retour arrière devient trivial : redéployer l'image précédente ;
3. la preuve devient triviale : l'identifiant d'image porte l'information de version ;
4. le nombre de constats individuels s'effondre au profit d'un seul indicateur — l'âge de l'image.

📌 **LIMITES** — Le modèle ne s'applique pas à tout : composants à état, systèmes industriels, matériel physique, appliances fournisseur. Et il déplace la charge vers la chaîne de construction, qui devient elle-même un actif critique à maintenir (chapitre 28).

### 6.11 Concevoir un mécanisme de mise à jour sécurisé

Cette section concerne ceux qui **fabriquent** un produit installé chez des clients — matériel connecté, logiciel embarqué, appliance, application déployée sur site. Elle est reprise et approfondie au chapitre 33.

Un mécanisme de mise à jour est un chemin d'exécution privilégié offert au fournisseur. Mal conçu, il devient un chemin d'exécution privilégié offert à un attaquant. Six propriétés le rendent sûr.

| Propriété | Ce qu'elle empêche |
|---|---|
| **Authenticité** | Le produit vérifie la signature de la mise à jour avant installation — sinon n'importe qui peut livrer du code |
| **Intégrité** | Empreinte vérifiée, transport protégé — contre l'altération en chemin |
| **Protection contre le retour en arrière** | Refus d'installer une version antérieure vulnérable — sinon l'attaquant « rétrograde » pour retrouver une faille |
| **Atomicité** | Installation complète ou nulle, jamais à moitié — une coupure de courant ne doit pas produire un équipement inutilisable |
| **Repli sûr** | En cas d'échec, retour automatique à la version précédente fonctionnelle |
| **Traçabilité** | Le produit sait dire quelle version il exécute, et le fournisseur sait quelles versions sont déployées |

⚠️ **PIÈGE — le mécanisme qui n'existe pas**
Beaucoup de produits industriels et connectés se mettent à jour par intervention manuelle sur site, avec un support amovible. C'est un choix de conception dont la conséquence est mécanique : la cadence de correction sera annuelle au mieux. Si vous **achetez** un tel produit, sachez-le avant, pas après — c'est l'exigence n° 5 du §6.2. Si vous le **fabriquez**, c'est une dette qui deviendra réglementaire (chapitre 33).

### 6.12 Des environnements de test réellement représentatifs

Toutes les stratégies de ce chapitre supposent qu'on puisse tester avant. Or c'est le maillon le plus faible en pratique.

**Les cinq écarts qui font qu'un test ne prouve rien :**

| Écart | Ce qu'il laisse passer |
|---|---|
| Volume de données sans commune mesure | Les régressions de performance, invisibles sur 200 lignes |
| Versions différentes de celles de production | Le test valide autre chose que ce que vous déploierez |
| Intégrations tierces simulées | Tout ce qui casse à la frontière — c'est-à-dire l'essentiel |
| Configuration divergente | Les effets liés au durcissement, aux droits, au réseau |
| Environnement figé depuis des mois | Il ne représente plus rien, y compris sa propre sécurité (chapitre 28) |

✅ **BONNE PRATIQUE (P1)** — Plutôt que de viser un environnement de recette parfait — objectif rarement atteint —, mesurez et affichez l'**écart** entre recette et production sur quatre axes : versions, volumétrie, intégrations, configuration. Un écart connu se compense par un déploiement témoin plus prudent ; un écart ignoré produit de la fausse confiance, ce qui est bien pire que pas de test du tout.

### 6.13 Le coût réel d'un système impossible à arrêter

Voici l'argument à porter en comité, parce qu'il transforme une exigence technique en décision économique.

**La formulation.** Un système non interruptible impose un coût récurrent qui n'apparaît dans aucun budget :

- l'interruption est repoussée jusqu'à une fenêtre annuelle, donc le délai moyen de correction se compte en mois ;
- chaque intervention devient un projet, avec préparation, validation, mobilisation nocturne, astreinte ;
- l'exposition prolongée impose des mesures compensatoires, qui ont leur propre coût de mise en œuvre et de surveillance (chapitre 20) ;
- le risque résiduel est porté par l'organisation pendant toute la période.

**La comparaison à présenter.** Mettez face à face le coût d'ajout de la redondance — souvent une instance supplémentaire et quelques jours d'ingénierie — et le coût annuel du non-interruptible : heures d'astreinte, mesures compensatoires, surveillance dédiée, temps de négociation, et le montant du risque accepté. Dans la plupart des cas, l'écart est spectaculaire, et il n'a jamais été calculé.

C'est l'un des rares arguments de MCS qui se gagne sur le terrain financier plutôt que sur le terrain du risque. Le chapitre 37 en fait un outil de dossier d'investissement.

### 6.14 ✅ Livrable — Grille d'évaluation de la maintenabilité sécurisée

À utiliser en revue d'architecture, en évaluation d'un progiciel, ou en état des lieux d'un système existant. Notation : **0** absent · **1** partiel · **2** satisfaisant.

| # | Critère | Question de vérification | Prio |
|---|---|---|---|
| 1 | Interruptibilité | Peut-on arrêter un composant en journée sans impact utilisateur ? | **P0** |
| 2 | Redondance effective | La capacité restante suffit-elle avec un membre en moins ? | **P0** |
| 3 | Bascule testée | Quand la dernière bascule a-t-elle été réalisée, et par qui ? | **P0** |
| 4 | Retour arrière | Existe-t-il, est-il documenté, a-t-il été chronométré ? | **P0** |
| 5 | Point de non-retour | Est-il identifié et écrit dans la demande de changement ? | **P0** |
| 6 | Découplage de version | Le système impose-t-il une version figée d'un composant sous-jacent ? | **P0** |
| 7 | Cadence supportée | Le système supporte-t-il une correction mensuelle ? | P1 |
| 8 | Stratégie de déploiement | Progressive, bleu/vert ou témoin — laquelle, et est-elle outillée ? | P1 |
| 9 | Critères d'arrêt | Sont-ils chiffrés et automatiques ? | P1 |
| 10 | Observabilité fonctionnelle | Sait-on détecter un service qui répond mais ne fait plus son travail ? | P1 |
| 11 | Compatibilité d'interface | Deux versions peuvent-elles coexister ? | P1 |
| 12 | Inventaire des composants | Le système déclare-t-il ses composants et versions ? | P1 |
| 13 | Représentativité de la recette | L'écart avec la production est-il mesuré sur quatre axes ? | P1 |
| 14 | Mécanisme de mise à jour | Signé, atomique, avec repli et protection contre le retour en arrière ? | P1 |
| 15 | Engagement de support | Durée et préavis de fin de support contractualisés ? | P2 |
| 16 | Décommissionnement | La procédure de retrait est-elle prévue dès la conception ? | P2 |

**Lecture du résultat.** Un seul critère P0 à 0 suffit à qualifier le système de non maintenable en sécurité — et cette qualification doit figurer dans le dossier, avec ses conséquences chiffrées, plutôt que d'être découverte trois ans plus tard par l'équipe d'exploitation.

### 6.15 🔴 FIL ROUGE — avril 2026 : la revue d'architecture d'HelioLink

La grille du §6.14 est appliquée pour la première fois chez HELIOMED, non pas sur un système existant, mais sur la refonte de la plateforme de télésuivi HelioLink, dont le développement démarre à Nantes.

**Ce que la grille révèle en deux heures de réunion.**

| Critère | Note | Constat |
|---|---|---|
| Interruptibilité | 0 | Une seule instance applicative ; toute mise à jour coupe le service de télésuivi |
| Redondance effective | 0 | Base de données unique, non répliquée |
| Point de non-retour | 0 | Les migrations de schéma sont appliquées en une passe, sans découpage |
| Découplage de version | 1 | L'application impose une version précise d'un environnement d'exécution, déjà en fin de support dans 14 mois |
| Observabilité fonctionnelle | 0 | Supervision technique uniquement ; rien ne mesure les remontées de télésuivi abouties |

Yann Prigent, responsable produit, oppose l'argument habituel et parfaitement recevable : ajouter de la redondance représente quatre semaines d'ingénierie et une instance supplémentaire, alors que la mise sur le marché est déjà tendue.

**L'argument qui emporte la décision** n'est pas un argument de sécurité. Claire Nadeau applique le §6.13 et présente deux colonnes : le coût de la redondance, contre le coût annuel prévisionnel d'un système non interruptible sur un service de télésuivi médical — interventions nocturnes obligatoires, astreinte, fenêtres à négocier avec les établissements de santé clients, et surtout **impossibilité de corriger rapidement une vulnérabilité exposée sur un service traitant des données de santé**. La comparaison n'est pas serrée.

**Décisions prises.**

1. Redondance applicative et réplication de base de données ajoutées au périmètre initial — quatre semaines de décalage acceptées par la direction générale.
2. Découpage systématique des migrations de schéma en expansion / contraction, inscrit dans les règles de développement.
3. Deux indicateurs fonctionnels créés avant la mise en production, avec seuils d'arrêt automatique chiffrés.
4. Le point de découplage de l'environnement d'exécution est traité comme une dette datée, avec échéance inscrite au plan d'obsolescence (chapitre 12) — c'est un report assumé et tracé, pas un oubli.

**Livrable de l'épisode.** La grille du §6.14 devient un document de revue obligatoire pour tout nouveau projet chez HELIOMED, avec une règle simple : un critère P0 à zéro ne bloque pas le projet, mais impose une décision explicite de la direction générale, écrite et datée.

→ La suite en 🔴 §7.7, quand ces principes doivent devenir une politique applicable à l'ensemble du parc existant.

→ **Chapitre 7 — Doctrine et politique MCS** : la doctrine : transformer ces principes en une politique réellement applicable.

### Synthèse mentale du chapitre 6

Le coût du MCS se décide en conception, pas en exploitation : un système qu'on ne peut pas arrêter ne sera pas corrigé, quelle que soit la politique. Sept exigences de maintenabilité, écrites dans un cahier des charges, se négocient tant qu'on a encore un levier — avant la signature. La redondance ne sert le MCS que si elle survit au test « peut-on en arrêter un membre maintenant, en pleine journée » : les faux clusters sont nombreux. Les stratégies progressive, bleu/vert et témoin permettent de corriger sans pari, et les interrupteurs de fonctionnalité découplent le déploiement de l'activation, ce qui offre aussi une mesure compensatoire propre. Les migrations de schéma détruisent silencieusement la réversibilité : le découpage expansion/contraction déplace le point de non-retour à un moment choisi. Un déploiement doit s'arrêter tout seul sur des seuils chiffrés à l'avance, dont au moins un indicateur fonctionnel — un service peut répondre parfaitement tout en ayant cessé de faire son travail. Enfin, un plan de retour arrière non testé n'est pas un plan, et le coût d'un système non interruptible se démontre en euros, pas en risque.

**Trois questions de vérification**

1. Votre architecte affirme que le service est redondé et donc corrigeable sans interruption. Quelle question unique posez-vous pour vérifier, et quelles sont les trois réponses évasives typiques ?
2. Une mise à jour applicative comporte une migration de base de données. Que devez-vous obtenir avant d'autoriser le changement, et pourquoi cette information change-t-elle la nature du plan de retour arrière ?
3. Un chef de projet refuse d'ajouter une seconde instance pour cause de budget. Construisez l'argument économique en quatre postes de coût récurrent.

---

---

> ### 🎓 À ce stade de la Partie I, vous savez…
>
> - **distinguer** le MCS du maintien opérationnel, et nommer les cinq causes récurrentes d'échec — dont aucune n'est exclusivement technique ;
> - **expliquer** pourquoi un numéro de version amont ne dit rien de la présence d'une faille sur un système à support long, et le vérifier en trois commandes ;
> - **situer** une frontière de responsabilité sur n'importe quelle couche d'abstraction : hyperviseur, conteneur, orchestrateur, cloud, industriel, micrologiciel ;
> - **lire** un constat de vulnérabilité sans confondre gravité, probabilité, exploitation avérée et exposition — et savoir laquelle de ces informations personne ne produira à votre place ;
> - **qualifier** une information en fait vérifié, hypothèse probable ou piste exploratoire ;
> - **poser** la question qui débloque le plus de situations : *qui décide qu'on l'arrête pour le corriger ?* ;
> - **évaluer** la maintenabilité d'un système en conception, et chiffrer le coût d'un système impossible à arrêter.
>
> **Ce que vous ne savez pas encore** : sur quoi exactement porte votre dispositif, qui arbitre, et ce que l'extérieur exige. C'est l'objet de la Partie II.
