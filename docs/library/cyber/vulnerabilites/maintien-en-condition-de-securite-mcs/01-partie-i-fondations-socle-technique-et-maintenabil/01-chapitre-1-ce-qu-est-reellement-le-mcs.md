---
title: Chapitre 1 — Ce qu'est réellement le MCS
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE I — Fondations, socle technique et maintenabilité
  - index.md
---

## 1.1 Définition, origine et périmètre

### Le modèle mental d'abord

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

### La définition de travail

Retenez celle-ci, elle sera utilisée dans tout le cours :

> **MCS** : ensemble des activités techniques et organisationnelles visant à maintenir, et si possible améliorer, le niveau de sécurité d'un système d'information pendant tout son cycle de vie, y compris son décommissionnement — et à en apporter la preuve.

Trois éléments de cette définition méritent qu'on s'y arrête.

**« techniques *et* organisationnelles ».** Le MCS n'est pas un problème d'outil. Une organisation peut disposer du meilleur scanner de vulnérabilités du marché et n'appliquer aucun correctif, faute de savoir qui est responsable du serveur concerné. Nous verrons au §1.4 que les causes d'échec les plus fréquentes ne sont presque jamais techniques.

**« pendant tout son cycle de vie, y compris son décommissionnement ».** Un serveur éteint mais dont l'enregistrement DNS existe toujours, dont le compte de service reste actif et dont la sauvegarde reste restaurable n'est pas décommissionné : c'est un actif fantôme, et c'est un problème de MCS. Le chapitre 35 y est entièrement consacré.

**« et à en apporter la preuve ».** Une activité de MCS non traçable est presque impossible à piloter, à défendre en audit et à financer. C'est une exigence à part entière, pas une formalité administrative ajoutée après coup. Nous y reviendrons constamment, et le chapitre 39 la traite pour elle-même.

### La boucle qui structure tout le cours

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

### Où se situe le MCS parmi les métiers voisins

Le MCS est régulièrement confondu avec trois fonctions voisines. Le tableau suivant sert de référence pour tout le cours.

| Fonction | Question centrale | Horizon | Ce qu'elle produit |
|---|---|---|---|
| **SOC / détection** | *Sommes-nous attaqués en ce moment ?* | Minutes à heures | Des alertes qualifiées |
| **CERT / CSIRT** | *Comment reprendre le contrôle ?* | Heures à jours | Une réponse à incident |
| **Exploitation** | *Est-ce que ça fonctionne ?* | Continu | Un service disponible |
| **MCS** | *Le niveau de sécurité tient-il dans la durée, et puis-je le prouver ?* | **Mois à années** | Un parc maintenu **et démontrable** |

**Les recouvrements sont réels et voulus.** Le MCS fournit au SOC un inventaire et une exposition à jour (ch. 10-11) ; le SOC fournit au MCS le signal d'exploitation (§14.5) ; le CERT hérite du MCS la capacité à savoir ce qui tournait où (§21.3). Ce qui distingue le MCS, c'est **l'horizon** : il est le seul de ces quatre métiers dont le succès se mesure sur plusieurs années.

### Une journée type

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

### Le vocabulaire du terrain

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

### D'où vient le terme

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

## 1.2 MCO et MCS : deux maintiens, un conflit structurel

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

## 1.3 Le périmètre réel du MCS : dix objets qui se dégradent

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

## 1.4 Les cinq causes récurrentes d'échec

Les retours d'expérience du domaine convergent vers un constat stable : les programmes de MCS échouent le plus souvent pour les mêmes raisons, et généralement dans le même ordre. Aucune n'est **exclusivement** technique.

**1. L'inventaire.** On ne maintient pas ce qu'on ne connaît pas. Un écart de 15 à 30 % entre l'inventaire théorique et la réalité est la norme, pas l'exception, dans une organisation qui n'a jamais fait ce travail. Tant que cet écart n'est pas mesuré et réduit, tous les indicateurs de MCS sont faux — non pas imprécis : **faux**, parce que leur dénominateur est inconnu. → Chapitre 10.

**2. La propriété.** Pour chaque actif, une question doit avoir une réponse nominative : *qui décide qu'on l'arrête pour le corriger ?* En l'absence de réponse, le correctif attend. Ce n'est pas un problème de bonne volonté : c'est un vide de décision, et personne ne prend spontanément une décision dont il n'a pas le mandat. → Chapitres 5 et 9.

**3. Les fenêtres.** Corriger suppose souvent d'interrompre. Si l'organisation n'a pas négocié à l'avance des créneaux d'interruption acceptés par les métiers, chaque correctif devient une négociation individuelle — donc un coût, donc un report. → Chapitres 5, 18 et 37.

**4. La preuve.** Sans traçabilité, vous ne pouvez ni démontrer un progrès, ni justifier un budget, ni répondre à un auditeur, ni savoir si un correctif a réellement été appliqué sur les 2 300 postes concernés ou seulement sur les 1 800 qui étaient allumés ce soir-là. → Chapitres 38 et 39.

**5. Le financement.** Sortir de l'obsolescence coûte cher, et ce coût est visible immédiatement alors que le bénéfice est invisible et différé. Sans dossier d'investissement construit, l'arbitrage budgétaire est perdu d'avance, chaque année, indéfiniment. → Chapitre 37.

✅ **BONNE PRATIQUE — l'ordre d'attaque (P0)**
Si vous démarrez un programme de MCS, traitez ces cinq causes **dans cet ordre**. Investir dans l'outillage de déploiement avant d'avoir un inventaire fiable et des propriétaires nommés est l'erreur de séquencement la plus coûteuse du domaine : vous automatiserez le traitement d'un périmètre que vous ne connaissez pas, et vous produirez des tableaux de bord verts sur un dénominateur faux. Le chapitre 40 détaille la feuille de route complète.

## 1.5 Le MCS dans le cycle de vie : *build → run → sunset*

Le MCS est habituellement perçu comme une activité du *run* — la phase d'exploitation. C'est incomplet, et cette incomplétude coûte cher.

**Phase *build* (conception et construction).** Les décisions d'architecture prises ici déterminent le coût de tout le MCS futur. Un système sans redondance ne pourra jamais être corrigé sans interruption. Une application couplée à une version précise de son environnement d'exécution bloquera toutes les montées de version. Un produit sans mécanisme de mise à jour signé ne pourra jamais être corrigé chez le client en confiance. Le chapitre 6 est entièrement consacré à cette phase, sous le nom de *MCS by design*.

**Phase *run* (exploitation).** C'est le cœur du cours : veille, détection, triage, remédiation, configuration, preuve. Parties II à V.

**Phase *sunset* (fin de vie et retrait).** Elle commence bien avant l'arrêt : dès l'annonce de fin de support par l'éditeur, une trajectoire doit exister. Elle se termine par un décommissionnement complet et vérifié. Chapitres 12 et 35.

L'enseignement structurant tient en une phrase : **le coût du MCS d'un système est majoritairement déterminé pendant la phase où l'on n'y pense pas.**

## 1.6 La dette de sécurité comme grandeur mesurable

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

## 1.7 Ce que le MCS ne résout pas

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

## 1.8 ⏱ État de l'art du domaine au 30 juillet 2026

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

## 1.9 Comment lire ce cours

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

## Synthèse mentale du chapitre 1

La sécurité d'un système se dégrade sans qu'on y touche, parce que c'est le monde qui change autour de lui. Le MCS est l'ensemble des activités — techniques **et** organisationnelles — qui compensent cette dégradation sur tout le cycle de vie, décommissionnement compris, et qui en apportent la preuve. Il est plus large que la gestion des correctifs : dix objets se dégradent, dont les configurations, les identités, les certificats, les micrologiciels et le contenu de détection. Il est en tension permanente avec le maintien en condition opérationnelle, et cette tension se négocie, elle ne se tranche pas par autorité. Cinq causes expliquent la plupart des échecs — inventaire, propriété, fenêtres, preuve, financement — et aucune n'est technique. Enfin, le MCS ne protège ni contre une faille inconnue, ni contre l'hameçonnage, ni contre un défaut d'architecture : c'est une couche parmi d'autres.

**Trois questions de vérification**

1. Un serveur installé et parfaitement à jour, auquel personne ne touche pendant six mois, est-il toujours au même niveau de sécurité ? Justifiez en citant au moins trois des dix objets du §1.3.
2. Une organisation affiche 98 % de conformité aux correctifs. Quelles trois questions posez-vous avant d'accorder la moindre valeur à ce chiffre ?
3. Parmi les cinq causes d'échec du §1.4, laquelle doit être traitée en premier, et pourquoi investir dans l'outillage avant elle est-il une erreur de séquencement ?

---
