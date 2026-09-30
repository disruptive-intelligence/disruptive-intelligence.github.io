---
title: PARTIE VI — Produire et diffuser
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
chapter: 6
chapters: 8
---

> **Où nous sommes dans la boucle analytique** : segment ④ **JUGEMENT**, dans sa dimension de transmission. L'analyse est faite ; il reste à ce qu'elle atteigne quelqu'un.
>
> **Pourquoi cette partie compte autant que la Partie II** : un jugement juste qui n'est pas lu ne vaut rien. Le §5.2 l'a établi — l'écriture occupe un quart du temps d'un analyste, et c'est la compétence la plus sous-estimée du métier.

---

## Chapitre 25 — Écrire pour être lu

### 25.1 La règle : conclusion d'abord

**Le principe** : votre destinataire lit dans un contexte de rareté d'attention. Il donnera à votre produit entre trente secondes et deux minutes avant de décider s'il continue.

**Ce que cela impose** : la conclusion en premier, la preuve ensuite.

| Structure académique | Structure de renseignement |
|---|---|
| Contexte → méthode → éléments → analyse → conclusion | **Conclusion → ce qui la fonde → détail** |
| Le lecteur doit tout lire pour savoir | Le lecteur sait après une phrase |
| Adaptée à un pair qui évalue le raisonnement | Adaptée à un décideur qui doit agir |

⚠️ **PIÈGE — le suspense**
Réserver la conclusion pour la fin est un réflexe scolaire profondément ancré. Il produit des documents où l'information la plus importante est à la page huit, et il est la première cause de non-lecture.

🧪 **EN PRATIQUE — la première phrase**

Elle contient quatre éléments, et rien d'autre :

```
[Nous estimons] [mot de probabilité] [l'affirmation] — [confiance], [en une ligne pourquoi]
```

> *Nous estimons **probable** que la vulnérabilité signalée le 11 juillet soit exploitée contre trois de nos clients — **confiance élevée**, fondée sur la correspondance exacte des versions et sur la cohérence des symptômes observés.*

Un lecteur qui s'arrête là a l'essentiel. C'est l'objectif.

### 25.2 La structure d'un produit

Reprise du §11.7, avec l'ordre de lecture en tête.

| Rang | Section | Qui la lit |
|---|---|---|
| 1 | **La conclusion**, en une phrase calibrée | Tout le monde |
| 2 | **Ce que cela implique** — 3 à 5 lignes | Tout le monde |
| 3 | **Ce que nous observons** | Ceux qui doivent vérifier |
| 4 | **Ce que nous en estimons** — le raisonnement | Ceux qui doivent contester |
| 5 | **Ce qui invaliderait** | Les rigoureux, et vous dans six mois |
| 6 | **Recommandations**, section séparée, avec coûts | Le décideur |
| 7 | Détail technique, indicateurs, annexes | Les opérationnels |

**Le rang 2 est celui qu'on oublie**, et c'est celui qui produit les décisions. Une conclusion sans implication laisse le lecteur devant un fait dont il ne sait que faire.

### 25.3 Séparer fait, évaluation et recommandation

Le §4.1 et le §11.5 ont posé le principe. Voici la mise en œuvre typographique, qui est ce qui le rend effectif.

**Trois sections, avec trois titres explicites** :

```
CE QUE NOUS OBSERVONS
    — uniquement des faits, avec source et date
    — aucun verbe d'intention

CE QUE NOUS EN ESTIMONS
    — hypothèses envisagées, ce qui les départage
    — conclusion calibrée
    — ce qui l'invaliderait

CE QUE NOUS RECOMMANDONS
    — actions, avec ordre de grandeur de coût
    — la décision appartient au destinataire
```

**Pourquoi la typographie compte** : un lecteur pressé lit les titres. Si vos titres sont « Contexte », « Analyse », « Conclusion », il ne sait pas où trouver ce dont il a besoin. S'ils sont ceux ci-dessus, il va directement à la section qui le concerne.

✅ **BONNE PRATIQUE (P0)** — Ces trois titres, tels quels, sur tous vos produits. Ils imposent la discipline à l'auteur autant qu'ils orientent le lecteur : il devient très difficile d'écrire un verbe d'intention sous un titre qui dit « ce que nous observons ».

### 25.4 ⚠️ Les défauts qui font qu'un produit n'est pas lu

Par fréquence décroissante, tous observés.

| Défaut | Effet |
|---|---|
| **La conclusion n'est pas en tête** | Le lecteur abandonne avant |
| **La longueur** | Au-delà de deux pages, le taux de lecture intégrale s'effondre |
| **Le jargon non défini** | Chaque terme opaque est une occasion d'abandonner |
| **L'absence d'implication** | Le lecteur ne sait pas ce qu'on attend de lui |
| **Le mélange des niveaux** | §3.6 — chacun cherche sa partie et ne la trouve pas |
| **Le ton alarmiste** | Fonctionne une fois, décrédibilise ensuite |
| **L'absence de date de validité** | §4.4 |
| **Les précautions en cascade** | Le lecteur ne sait plus ce qui est affirmé |

**Le deuxième mérite un chiffre** : dans les organisations où le taux de lecture est mesuré, la lecture intégrale décroche nettement au-delà de deux pages pour un produit non sollicité. Un rapport de onze pages a une audience réelle proche de zéro — c'est le §3.8 du fil rouge.

### 25.5 Longueur, format, canal

| Produit | Longueur cible | Canal |
|---|---|---|
| **Alerte** | 5 à 10 lignes | Le canal le plus rapide disponible |
| **Réponse à une question** | 3 à 15 lignes | Le canal de la question |
| **Fiche opérationnelle** | 1 à 2 pages | Document, avec résumé en corps de message |
| **Note d'orientation** | **1 page**, 2 au maximum | Document, présenté oralement si possible |
| **Jeu d'indicateurs** | Tableau | Format structuré, machine à machine |
| **Dossier de campagne** | Sans limite | Référence, consultée à la demande |

**La règle du corps de message** : ce qui est en pièce jointe n'est pas lu. Le message qui accompagne un produit doit contenir la conclusion et l'implication — la pièce jointe sert à ceux qui veulent vérifier.

🎯 **ET MAINTENANT ?**
*Vous avez produit une analyse de six pages, bien construite, sur une campagne visant votre secteur. Comment la diffusez-vous ?*
**Réponse** : vous ne la diffusez pas telle quelle. Vous écrivez un message de huit lignes contenant la conclusion calibrée, les trois implications, et une phrase — *« le détail et les sources sont en pièce jointe »*. Six pages ne seront lues par personne ; huit lignes le seront par tout le monde. Et si vous avez trois destinataires à des niveaux différents, vous écrivez trois messages de huit lignes, pas un message de six pages.

### 25.6 🔴 FIL ROUGE — juin 2029 : le bon rapport que personne ne lit

*Cet épisode a été présenté au §3.8 sous l'angle des niveaux. Le voici sous l'angle de l'écriture — et ce sont deux problèmes distincts, souvent confondus.*

La note du 22 mai fait onze pages. Elle est bien documentée, correctement raisonnée, et sa section d'implications est page 9.

**Ce que Nour croit d'abord** : elle est trop longue.

**Ce que Claire lui montre**, en lui faisant relire la première page :

> *« La campagne dite [X] a été observée pour la première fois en février 2029 par plusieurs éditeurs. Elle vise principalement des établissements de santé européens. Le mode opératoire décrit comprend un accès initial par courriel, suivi d'une phase de reconnaissance… »*

**Le diagnostic** : ce n'est pas trop long, c'est **mal ordonné**. Aucune des trois premières phrases ne dit ce que le lecteur doit faire. La conclusion — *nous ne sommes probablement pas concernés, pour trois raisons* — est page 9.

**La réécriture, à contenu identique** :

> *Nous estimons **peu probable** qu'HELIOMED soit concernée par la campagne [X] — **confiance moyenne**.*
>
> *Le vecteur d'entrée décrit exploite un progiciel de gestion que nous n'utilisons pas. Les deux victimes documentées sont des distributeurs, non des fabricants. Aucun élément ne suggère un ciblage des fabricants.*
>
> *Ce que cela implique : aucune action immédiate. Nous recommandons de surveiller deux indicateurs de changement, listés page 2.*
>
> *Le détail, les sources et les indicateurs figurent ci-après.*

**Quatre-vingt-dix mots.** Le reste du document est inchangé.

**L'effet** : sur les sept destinataires, six lisent les quatre-vingt-dix mots. Deux ouvrent le détail.

**Ce que Nour retient**, et qui est différent de ce qu'elle avait compris au §3.8 :

> *Le problème du découpage et le problème de l'ordre sont deux problèmes. J'avais réglé le premier en faisant trois produits. Le second, c'est que dans chacun des trois, je commençais toujours par le contexte.*

**Livrable de l'épisode.** Le modèle de première phrase en quatre éléments, et la règle des trois titres explicites — annexe D.

→ La suite en 🔴 §26.7, quand un même événement produira cinq bulletins différents.

### Synthèse mentale du chapitre 25

Votre destinataire accorde entre trente secondes et deux minutes avant de décider s'il continue : la conclusion vient donc en premier, et la structure de renseignement est l'inverse de la structure académique. La première phrase contient quatre éléments — verbe d'estimation, probabilité, affirmation, confiance justifiée — et un lecteur qui s'arrête là a l'essentiel. La section qu'on oublie est la deuxième, *ce que cela implique* : une conclusion sans implication laisse le lecteur devant un fait dont il ne sait que faire. Trois titres explicites — ce que nous observons, ce que nous en estimons, ce que nous recommandons — orientent le lecteur et disciplinent l'auteur, parce qu'il devient difficile d'écrire un verbe d'intention sous un titre qui annonce des observations. Enfin, ce qui est en pièce jointe n'est pas lu : le corps du message porte la conclusion et l'implication.

**Trois questions de vérification**

1. Vous avez produit six pages solides. Comment les diffusez-vous, et pourquoi la longueur n'est-elle pas le problème principal ?
2. Écrivez une première phrase de produit contenant les quatre éléments requis.
3. Pourquoi les titres « Contexte, Analyse, Conclusion » desservent-ils un produit de renseignement ?

---

## Chapitre 26 — Adapter au destinataire

### 26.1 Une information, cinq produits

**Le principe** : le même événement, analysé une fois, produit plusieurs livrables différents — pas un livrable envoyé à plusieurs personnes.

**Ce qui change d'un destinataire à l'autre** :

| Dimension | Varie ? |
|---|---|
| Les faits établis | **Non** |
| L'évaluation et sa confiance | **Non** |
| Ce qui est retenu | **Oui** |
| Le niveau de détail | **Oui** |
| L'implication mise en avant | **Oui** |
| Le vocabulaire | **Oui** |
| La longueur | **Oui** |

⚠️ **La première ligne est une contrainte absolue.** Adapter au destinataire ne signifie jamais ajuster la conclusion. Une évaluation atténuée pour une direction et durcie pour l'exploitation est une faute — c'est le biais du client (§7.7) institutionnalisé.

### 26.2 Pour la direction générale

| Élément | Contenu |
|---|---|
| **Longueur** | 1 page, 10 lignes si possible |
| **Question à laquelle répondre** | *Est-ce que cela nous concerne, et devons-nous décider quelque chose ?* |
| **Ce qu'on retient** | L'implication métier, le coût, l'échéance |
| **Ce qu'on écarte** | Techniques, indicateurs, noms d'acteurs, détail du raisonnement |
| **Vocabulaire** | Aucun terme technique non défini |
| **Ce qu'on ajoute** | **Une demande explicite** : décision, arbitrage, ou information seule |

**La ligne à ne jamais omettre** : *« nous n'attendons pas de décision de votre part »* quand c'est le cas. Un produit envoyé à une direction sans indiquer ce qu'on attend d'elle crée une inquiétude inutile ou une inaction.

### 26.3 Pour le RSSI

| Élément | Contenu |
|---|---|
| **Longueur** | 1 à 2 pages |
| **Question** | *Est-ce que cela change mes priorités ?* |
| **Ce qu'on retient** | L'évaluation complète, les implications sur le dispositif existant |
| **Ce qu'on ajoute** | Ce que cela dit de nos angles morts |

C'est le destinataire le plus proche de l'analyste, et celui pour qui le produit standard convient le mieux.

### 26.4 Pour l'exploitation et la gestion des vulnérabilités

| Élément | Contenu |
|---|---|
| **Longueur** | Une demi-page, souvent moins |
| **Question** | *Que dois-je corriger en premier ?* |
| **Ce qu'on retient** | Les identifiants de vulnérabilités, l'applicabilité, l'ordre |
| **Ce qu'on écarte** | Tout le contexte, sauf ce qui justifie l'ordre |
| **Format** | **Une liste ordonnée**, pas un texte |

**Le format qui fonctionne** :

```
Priorité 1 — [identifiant] — exploitée activement, 4 actifs exposés concernés
Priorité 2 — [identifiant] — exploitée dans notre secteur, 12 actifs internes
Priorité 3 — [identifiant] — non exploitée, gravité élevée, 2 actifs

Non prioritaire — [identifiant] — composant non déployé chez nous
```

**La dernière ligne compte autant que les autres** : dire ce qui **n'est pas** prioritaire évite que l'équipe le traite quand même par prudence.

### 26.5 Pour la détection et la réponse

| Élément | Contenu |
|---|---|
| **Question** | *Que dois-je chercher, et comment ?* |
| **Ce qu'on retient** | Comportements, techniques, indicateurs |
| **Ce qu'on ajoute obligatoirement** | **Date de première et dernière observation · source · confiance · action attendue** |
| **Format** | Structuré, exploitable machine si possible |

⚠️ Un indicateur livré sans ces quatre attributs est inexploitable (§3.3). C'est la faute la plus fréquente dans les échanges entre CTI et détection.

### 26.6 Pour le produit et la sécurité produit

| Élément | Contenu |
|---|---|
| **Question** | *Est-ce que cela touche nos produits, et devons-nous prévenir nos clients ?* |
| **Ce qu'on retient** | L'applicabilité produit par produit, version par version |
| **Ce qu'on ajoute** | L'obligation de signalement éventuelle, et son délai |
| **Sensibilité** | **Élevée** — ce produit peut déclencher une communication externe |

### 26.7 Pour un client ou un partenaire

| Élément | Contenu |
|---|---|
| **Question** | *Sommes-nous exposés par votre faute, et que faites-vous ?* |
| **Ce qu'on retient** | Ce qui les concerne, ce qui est fait, ce qu'ils doivent faire |
| **Ce qu'on écarte** | Notre organisation interne, nos angles morts, nos hypothèses non consolidées |
| **Validation** | **Systématique** — juridique, et direction selon l'enjeu |

**Le principe qui gouverne ce produit** : on ne transmet à l'extérieur que ce qu'on peut soutenir. Une hypothèse de travail interne devient, transmise à un client, une affirmation qu'on devra assumer.

### 26.8 🔬 Mini-lab 8 — Cinq bulletins, un événement

**Objectif** — Produire cinq livrables adaptés à partir d'une analyse unique, sans altérer la conclusion.
**Durée** 50 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §26.1 à §26.7, §25.1 · **Livrable** cinq textes courts
**Compétences validées** — ✔ adapter sans altérer ✔ identifier l'implication propre à chaque destinataire ✔ choisir le bon format ✔ dire ce qu'on attend du destinataire ✔ écarter ce qui ne le concerne pas

**L'analyse fournie** — le matériau commun, à ne pas modifier :

> **Conclusion.** Nous estimons **très probable** qu'une vulnérabilité affectant une bibliothèque d'authentification largement diffusée soit activement exploitée contre des organisations de notre secteur — **confiance élevée** : trois victimes documentées par deux sources indépendantes, mécanisme d'exploitation décrit publiquement, et signalements concordants de deux de nos clients.
>
> **Applicabilité.** La bibliothèque est embarquée dans trois de nos cinq versions déployées de notre produit principal. 43 clients utilisent une version affectée. Elle est également présente sur deux de nos serveurs applicatifs internes.
>
> **Exposition.** Le vecteur nécessite un accès au portail d'authentification, exposé par nécessité fonctionnelle. L'authentification multifacteur limite l'exploitation sans l'empêcher.
>
> **Correctif.** Publié par le mainteneur de la bibliothèque il y a 4 jours. Notre équipe de développement estime 6 jours pour l'intégrer aux trois versions maintenues.
>
> **Ce qui invaliderait.** Une victime utilisant une version non concernée · une cause applicative locale expliquant les symptômes observés chez nos clients.
>
> **Indicateurs.** 11 disponibles, première observation 28 juin, dernière 19 juillet.
>
> **Obligation.** Une vulnérabilité activement exploitée affectant un produit mis sur le marché déclenche une obligation de signalement, délai d'alerte précoce 24 h.

**Consigne** : produisez cinq livrables — direction générale, exploitation, détection, sécurité produit, clients. Respectez les longueurs cibles.

---

**Corrigé commenté**

**① Direction générale — 9 lignes**

> **Objet : vulnérabilité exploitée affectant notre produit — signalement réglementaire en cours**
>
> Nous estimons très probable qu'une vulnérabilité affectant une bibliothèque intégrée à notre produit principal soit activement exploitée contre des organisations de notre secteur — confiance élevée.
>
> **Ce que cela implique.** 43 clients utilisent une version concernée. Un correctif sera disponible sous 6 jours. Une obligation réglementaire de signalement s'applique et sera honorée dans le délai de 24 heures.
>
> **Ce que nous attendons de vous.** Information, à ce stade. Une décision sera nécessaire si nous devions recommander une interruption de service chez nos clients, ce qui n'est pas le cas aujourd'hui.
>
> *Évaluation au 22 juillet. Point d'étape le 25.*

⚠️ **Ce qui a été écarté** : le nom de la bibliothèque, le mécanisme, les indicateurs, le raisonnement, les sources. **Ce qui a été ajouté** : l'obligation réglementaire, et surtout la ligne « ce que nous attendons de vous ».

**② Exploitation et gestion des vulnérabilités — 6 lignes**

> **Priorité 1** — [bibliothèque, version] — **exploitée activement**, présente sur 2 serveurs applicatifs internes exposés. Correctif disponible. À traiter sous 72 h.
>
> **Non prioritaire** — aucune autre occurrence de cette bibliothèque n'a été identifiée dans le parc interne. Vérification faite le 22 juillet sur l'inventaire complet.
>
> **Attention** : l'authentification multifacteur limite l'exploitation mais ne la neutralise pas. Ne pas considérer les serveurs comme protégés.

⚠️ Le périmètre interne — deux serveurs — est ce qui concerne ce destinataire. Les 43 clients ne le concernent pas.

**③ Détection — format structuré**

> **Contexte** : exploitation d'une vulnérabilité d'authentification, campagne active dans le secteur santé.
> **Comportement à rechercher** : tentatives d'authentification en volume anormal sur le portail, suivies d'une dégradation des performances applicatives.
> **Fenêtre de recherche rétrospective recommandée** : depuis le 28 juin.
>
> | Indicateur | Type | 1ʳᵉ obs. | Dernière obs. | Source | Confiance | Action |
> |---|---|---|---|---|---|---|
> | *(11 lignes)* | | 28/06 | 19/07 | Dispositif sectoriel + client | Élevée | Rechercher, ne pas bloquer sans vérification |

⚠️ **La colonne « action » est essentielle** : « rechercher, ne pas bloquer sans vérification » évite les faux positifs du §24.5.

**④ Sécurité produit — 12 lignes**

> **Applicabilité** : versions 4.2, 4.3 et 4.4 concernées. Versions 5.0 et 5.1 non concernées — vérification faite, la bibliothèque a été remplacée en 5.0.
> **Clients concernés** : 43, liste jointe.
> **Correctif** : 6 jours pour les trois versions maintenues.
> **Mesure d'atténuation immédiate** à communiquer aux clients : [restriction d'accès au portail].
>
> **Obligation de signalement** : déclenchée. Alerte précoce sous 24 h, soit avant le 23 juillet 18 h. Notification sous 72 h. Le dossier est prêt, validation juridique demandée.
>
> **Ce qui invaliderait** : une victime sur une version non concernée remettrait en cause l'analyse d'applicabilité.

**⑤ Clients — 8 lignes**

> **Objet : vulnérabilité affectant votre version de [produit] — mesure immédiate recommandée**
>
> Une vulnérabilité affectant un composant de votre version de [produit] fait l'objet d'une exploitation active. Votre installation est concernée.
>
> **Ce que nous faisons** : un correctif sera mis à disposition sous 6 jours. Vous serez notifié dès sa publication.
>
> **Ce que nous vous recommandons de faire immédiatement** : [mesure d'atténuation], qui limite l'exposition sans interrompre le service. La procédure est jointe.
>
> **Contact** : [ligne dédiée], disponible jusqu'à la publication du correctif.

⚠️ **Ce qui a été écarté** : nos hypothèses, nos sources, le fait que deux clients nous ont signalé les symptômes, et toute mention de notre organisation interne. **Ce qui a été ajouté** : une action immédiate, et un contact.

**Les trois erreurs attendues**

1. **Envoyer les indicateurs à la direction générale.** Ils n'y ont aucun usage et créent l'impression que le CTI ne comprend pas son interlocuteur.
2. **Atténuer la conclusion pour les clients.** La tentation est réelle — « pourrait être affectée » plutôt que « est concernée ». C'est une altération, et elle se retourne au premier incident.
3. **Omettre « ce que nous attendons de vous »** dans le produit direction. Sans cette ligne, le destinataire ne sait pas s'il doit agir, et l'inaction par défaut est le résultat le plus fréquent.

### 26.9 🔴 FIL ROUGE — juillet 2030 : cinq bulletins en trois heures

L'épisode du §19.6 — trois signalements formant une campagne — produit sa suite immédiate. Le 22 juillet, Nour dispose de l'analyse. Elle a trois heures avant l'échéance de signalement réglementaire.

**Ce qu'elle produit** : les cinq livrables du mini-lab 8, à partir d'une analyse unique rédigée une seule fois.

**Le chronométrage réel**, qu'elle note :

| Tâche | Durée |
|---|---|
| Analyse consolidée | 1 h 40 |
| Bulletin direction | 8 min |
| Bulletin exploitation | 5 min |
| Bulletin détection | 20 min — la mise en forme des indicateurs |
| Bulletin sécurité produit | 25 min — vérification d'applicabilité version par version |
| Bulletin clients | 30 min — dont validation juridique |
| **Total diffusion** | **1 h 28** |

**Ce que le chronométrage démontre** : les cinq bulletins ont coûté moins de temps que l'analyse. C'est le point que Nour porte au comité, parce qu'il contredit l'objection habituelle — *« adapter à chaque destinataire, c'est trop long »*.

**L'effet observé** : les cinq destinataires agissent dans les vingt-quatre heures. Le signalement réglementaire est déposé dans le délai. Les 43 clients reçoivent la mesure d'atténuation le lendemain matin.

**Ce que Yann Prigent relève**, et qui n'était pas attendu : trois clients répondent au bulletin en signalant qu'ils avaient observé les mêmes symptômes sans les avoir signalés. **Le bulletin a produit du renseignement en retour** — trois observations supplémentaires qui confirment l'analyse et étendent le périmètre connu.

> *« Diffuser, c'est aussi collecter »*, note Nour dans son carnet.

**Livrable de l'épisode.** Les cinq modèles de bulletins, avec leurs longueurs cibles — annexe D.

→ La suite en 🔴 §27.6, quand une alerte de trop fera baisser le taux de réaction.

### Synthèse mentale du chapitre 26

Un même événement produit plusieurs livrables, jamais un livrable envoyé à plusieurs personnes — et ce qui varie est ce qu'on retient, le détail, l'implication et le vocabulaire, jamais les faits ni la conclusion : adapter n'est pas ajuster. Pour une direction, la ligne à ne jamais omettre est *ce que nous attendons de vous*, faute de quoi l'inaction est le résultat par défaut. Pour l'exploitation, dire ce qui n'est **pas** prioritaire compte autant que l'ordre, sinon l'équipe traite tout par prudence. Pour la détection, un indicateur sans date, source, confiance et action attendue est inexploitable. Pour un client, on ne transmet que ce qu'on peut soutenir : une hypothèse de travail devient une affirmation qu'il faudra assumer. Enfin, produire cinq bulletins coûte moins de temps que l'analyse elle-même — et diffuser produit du renseignement en retour.

**Trois questions de vérification**

1. Qu'est-ce qui varie et qu'est-ce qui ne varie jamais entre deux bulletins portant sur le même événement ?
2. Vous envoyez une note à votre direction générale. Quelle ligne omettez-vous le plus souvent, et quel effet produit son absence ?
3. Pourquoi l'objection « adapter à chaque destinataire prend trop de temps » ne résiste-t-elle pas à un chronométrage ?

---

## Chapitre 27 — Alerter

### 27.1 Ce qui justifie une alerte

**Une alerte est un produit qui interrompt.** C'est sa définition fonctionnelle : elle sort du rythme normal, mobilise de l'attention immédiate, et déclenche potentiellement des actions non planifiées.

**Ce statut a un coût, et ce coût est cumulatif.** Chaque alerte consomme du crédit d'attention. Une fonction qui alerte souvent obtient des réactions rapides les trois premières fois, puis de moins en moins.

**Les quatre conditions d'une alerte justifiée** — cumulatives :

| # | Condition | Question |
|---|---|---|
| **1** | **Applicabilité établie** | Cela nous concerne-t-il **factuellement** ? |
| **2** | **Urgence réelle** | Attendre le prochain point périodique aggrave-t-il la situation ? |
| **3** | **Action possible** | Le destinataire peut-il faire quelque chose maintenant ? |
| **4** | **Action nécessaire** | Ne rien faire est-il déraisonnable ? |

**La troisième est celle qu'on néglige.** Alerter sur une menace contre laquelle rien ne peut être fait immédiatement produit de l'anxiété sans produire d'action. Ce n'est pas une alerte, c'est une information — qui a sa place dans le rythme normal.

⚠️ **PIÈGE — l'alerte de couverture**
Alerter « au cas où », pour ne pas être celui qui n'a pas prévenu, est un réflexe compréhensible et destructeur. Il transfère la charge de la décision au destinataire, il consomme du crédit, et il produit exactement l'effet inverse de celui recherché : au bout de quelques mois, les alertes ne sont plus traitées avec urgence.

### 27.2 Le coût d'une fausse alerte, et celui d'une alerte manquée

**Les deux erreurs ne sont pas symétriques**, et il faut le dire clairement.

| | **Fausse alerte** | **Alerte manquée** |
|---|---|---|
| Coût immédiat | Mobilisation inutile, chiffrable | Potentiellement élevé |
| Coût différé | **Érosion du crédit** — cumulative, durable | Remise en cause de la fonction |
| Visibilité | Immédiate | Souvent invisible, sauf incident |
| Réversibilité | La confiance se reconstruit lentement | — |

**Ce que cette asymétrie implique** : le réflexe naturel est de privilégier la fausse alerte, parce que son coût est visible et paraît acceptable. Mais son coût **différé** — l'érosion du crédit — est ce qui produira, plus tard, l'alerte manquée : celle qu'on aura émise et que personne n'aura traitée avec urgence.

> **Une fonction qui alerte trop finit par ne plus être capable d'alerter.**

**Le repère pratique** : dans une organisation de taille intermédiaire, une fonction CTI mature émet de l'ordre de deux à six alertes par an. Au-delà de dix, le seuil de déclenchement est probablement trop bas — ou les conditions du §27.1 ne sont pas appliquées.

### 27.3 Formuler une alerte

**Le format**, cinq à dix lignes, sans exception.

```
① OBJET          Ce qui se passe, en une phrase calibrée
② APPLICABILITÉ  Pourquoi cela nous concerne — factuel, précis
③ DÉLAI          De quoi disposons-nous
④ ACTION         Ce que nous demandons, à qui, précisément
⑤ SUITE          Quand le prochain point aura lieu
```

**Exemple** :

> **Alerte — exploitation active d'une vulnérabilité affectant nos passerelles d'accès distant**
>
> Une vulnérabilité affectant la version installée sur nos deux passerelles fait l'objet d'une exploitation active confirmée depuis ce matin — confiance élevée, avis constructeur et signalement du centre de réponse national.
>
> **Nous sommes concernés** : version 4.2.11 installée sur GW-VPN-01 et 02, service publié sur Internet, 210 utilisateurs.
>
> **Délai** : le correctif est disponible. Nous recommandons une application cette nuit.
>
> **Ce que nous demandons** : validation par [nom] de l'interruption de service entre 22 h et 23 h.
>
> **Point suivant** : demain 9 h, ou immédiatement en cas d'élément nouveau.

⚠️ **Ce que l'exemple ne contient pas** : le nom de l'acteur, le mécanisme technique, l'historique de la campagne, les indicateurs. Tout cela suit dans un produit ultérieur. **Une alerte n'informe pas, elle déclenche.**

### 27.4 ⚠️ La fatigue d'alerte, et comment on la fabrique

**Le mécanisme**, en quatre étapes que toute organisation reconnaît :

```
1. La fonction alerte sur un sujet réel mais sans action possible
2. Le destinataire mobilise, constate qu'il n'y avait rien à faire
3. À l'alerte suivante, il attend avant de mobiliser
4. À la troisième, il traite l'alerte comme une information
```

**Les cinq façons de la fabriquer** :

| Façon | Mécanisme |
|---|---|
| Alerter sans applicabilité établie | §7.9 du fil rouge |
| Alerter sans action possible | Le destinataire subit |
| Alerter par prudence | §27.1 |
| Alerter sur une source unique non vérifiée | La rétractation détruit le crédit |
| **Ne pas clore l'alerte** | Le destinataire ne sait pas quand c'est fini |

**La cinquième est la plus négligée.** Une alerte ouverte indéfiniment maintient un état de mobilisation qui s'épuise. La clôture est une obligation : *« l'alerte du 22 juillet est close, le correctif est déployé et vérifié, aucune activité n'a été observée »*.

### 27.5 Le suivi : ce qui s'est passé après

**Trois questions, deux semaines après chaque alerte** — les mêmes que celles du §15.7 :

1. L'alerte a-t-elle été traitée dans le délai demandé ?
2. Quelle action a été engagée ?
3. **L'alerte était-elle justifiée, avec le recul ?**

**La troisième question est celle qui construit le crédit.** Une fonction qui reconnaît elle-même qu'une alerte n'était pas justifiée — comme au §7.9 — préserve sa capacité à alerter. Une fonction qui ne revient jamais dessus la perd progressivement.

✅ **BONNE PRATIQUE (P1)** — Tenez un registre des alertes avec, pour chacune, la justification a posteriori. Deux lignes. Au bout de deux ans, il constitue la meilleure démonstration de la fiabilité de la fonction — et le meilleur argument face à une direction qui demande si les alertes sont bien calibrées.

🎯 **ET MAINTENANT ?**
*Un dispositif sectoriel diffuse une alerte critique. Vous vérifiez : la vulnérabilité concerne un produit que vous utilisez, mais aucun correctif n'existe et aucune mesure d'atténuation n'est identifiée. Alertez-vous ?*
**Réponse** : non — pas au sens d'une alerte. Les conditions 1 et 2 sont remplies, la 3 ne l'est pas : le destinataire ne peut rien faire maintenant. Ce que vous produisez est une **information avec un engagement** : *« vulnérabilité sans correctif affectant [produit], nous suivons quotidiennement, nous alerterons dès qu'une action sera possible — prochaine mise à jour vendredi »*. Vous avez informé sans mobiliser, et vous avez conservé votre capacité à alerter pour le moment où elle servira. C'est exactement ce que la condition 3 protège.

### 27.6 🔴 FIL ROUGE — octobre 2030 : l'alerte de trop

Entre mai et septembre 2030, Nour émet **sept alertes**. Le rythme s'est accéléré après le succès de juillet (§26.9) — l'alerte de juillet a bien fonctionné, elle a produit une mobilisation efficace, et la fonction a gagné en légitimité.

**L'alerte du 2 octobre** porte sur une campagne visant le secteur, avec une applicabilité incertaine : le vecteur décrit concerne un composant qu'HELIOMED utilise, mais dans une configuration possiblement non affectée. Nour alerte quand même, par prudence.

**Ce qui se passe** : l'exploitation prend six heures. Résultat : la configuration d'HELIOMED n'est pas affectée. Personne n'avait rien à faire.

**Ce que Claire constate deux semaines plus tard**, en préparant le comité :

| Alerte | Délai de première réaction |
|---|---|
| Mai (1ʳᵉ) | 22 minutes |
| Juin | 35 minutes |
| Juillet | 18 minutes |
| Août (2) | 1 h 10 · 2 h 40 |
| Septembre | 3 h 15 |
| **Octobre** | **6 h 20** |

**Le délai de réaction a été multiplié par dix-sept en cinq mois.** Aucun destinataire ne s'en est plaint ; personne n'a dit qu'il ne traitait plus les alertes en urgence. Le comportement a simplement changé.

**L'analyse que Nour conduit**, en reprenant les sept alertes avec les quatre conditions du §27.1 :

| Alerte | Cond. 1 applicabilité | Cond. 2 urgence | Cond. 3 action possible | Cond. 4 nécessaire | Justifiée ? |
|---|---|---|---|---|---|
| Mai | ✅ | ✅ | ✅ | ✅ | **Oui** |
| Juin | ✅ | ✅ | ✅ | ✅ | **Oui** |
| Juillet | ✅ | ✅ | ✅ | ✅ | **Oui** |
| Août-1 | ✅ | ⚠️ | ✅ | ⚠️ | Discutable |
| Août-2 | ⚠️ | ✅ | ❌ | — | **Non** |
| Septembre | ✅ | ❌ | ✅ | ❌ | **Non** |
| Octobre | ❌ | ✅ | ✅ | — | **Non** |

**Trois alertes justifiées sur sept.** Les quatre autres relevaient de l'information, pas de l'alerte.

**Ce que Nour porte au comité**, sans détour :

> *J'ai émis quatre alertes qui n'en étaient pas. Le coût n'est pas les heures mobilisées — c'est que la prochaine alerte réelle mettra six heures à être traitée.*

**Les trois décisions** :

1. **Le seuil est écrit** : les quatre conditions du §27.1 doivent être toutes vérifiées, et la vérification est **tracée** dans le message d'alerte lui-même.
2. **Une catégorie intermédiaire est créée** : *information avec engagement de suivi*, qui n'interrompt pas. Elle absorbe ce qui relevait des alertes non justifiées.
3. **Le registre des alertes** est tenu, avec justification a posteriori à deux semaines.

**L'effet mesuré à six mois** : deux alertes émises entre novembre 2030 et avril 2031. Délais de première réaction : 19 et 24 minutes.

**Ce que Claire écrit au compte rendu**, et qui résume le chapitre :

> *« La capacité d'alerter n'est pas un droit acquis. C'est un crédit, et il se dépense. »*

**Livrable de l'épisode.** Le format d'alerte en cinq blocs, la catégorie « information avec engagement », et le registre avec justification a posteriori — annexe D.

→ La suite en 🔴 §28.6, quand HELIOMED devra décider ce qu'elle partage d'un incident qui la concerne.

### Synthèse mentale du chapitre 27

Une alerte est un produit qui interrompt, et ce statut consomme un crédit d'attention cumulatif : une fonction qui alerte trop finit par ne plus être capable d'alerter. Quatre conditions cumulatives la justifient, et la troisième — l'action est-elle possible maintenant ? — est celle qu'on néglige : alerter sur une menace contre laquelle rien ne peut être fait produit de l'anxiété, pas de l'action. Les deux erreurs ne sont pas symétriques : le coût d'une fausse alerte paraît acceptable parce qu'il est visible, mais son coût différé est l'érosion du crédit, laquelle produira plus tard l'alerte manquée. Une alerte tient en cinq à dix lignes et ne contient ni acteur, ni mécanisme, ni indicateurs — elle ne informe pas, elle déclenche. La clôture explicite est une obligation, faute de quoi la mobilisation s'épuise. Enfin, revenir soi-même sur une alerte injustifiée préserve la capacité à alerter ; ne jamais y revenir la détruit lentement.

**Trois questions de vérification**

1. Une vulnérabilité critique vous concerne, aucun correctif ni contournement n'existe. Alertez-vous ? Justifiez par la condition pertinente.
2. Pourquoi le coût d'une fausse alerte est-il plus élevé qu'il n'y paraît, et à quel moment se manifeste-t-il ?
3. Vos délais de réaction aux alertes s'allongent sans que personne ne se plaigne. Que se passe-t-il, et comment le diagnostiquez-vous ?

---

## Chapitre 28 — Partager à l'extérieur

### 28.1 Pourquoi partager, et ce qu'on y gagne réellement

**Les trois gains**, par ordre de valeur constatée :

| Gain | Mécanisme |
|---|---|
| **L'antériorité** | Savoir avant que ce ne soit public — §19.3, l'étape ③ plutôt que l'étape ⑥ |
| **Le contexte sectoriel** | Ce qui vise vos pairs vous concerne probablement |
| **La validation** | Un pair confirme ou infirme votre analyse |

**Le troisième est sous-estimé.** Un dispositif de partage est aussi un moyen de tester une hypothèse auprès de gens qui observent le même environnement — c'est l'analyse à plusieurs (§12.5) étendue hors de l'organisation.

**Ce qu'on n'y gagne pas** : une couverture exhaustive, une réactivité garantie, ou une information sur ce qui vous vise spécifiquement. Un dispositif sectoriel voit ce que ses membres partagent, ni plus ni moins.

### 28.2 Ce qui se partage et ce qui ne se partage pas

Reprise et approfondissement du §20.6.

| Catégorie | Se partage ? | Précaution |
|---|---|---|
| Indicateurs techniques anonymisés | **Oui, facilement** | Vérifier qu'ils ne révèlent pas votre architecture |
| Constats d'exploitation de vulnérabilités | **Oui** | Sans mention de vos actifs affectés |
| Modes opératoires observés | **Oui** | Sans détail permettant d'identifier la victime |
| Évaluations et analyses | Oui, avec le niveau de confiance | Ce qui protège juridiquement (§20.8) |
| Détails d'un incident propre | **Au cas par cas** | Décision de niveau direction |
| Éléments identifiant une victime tierce | **Non** | Y compris un client |
| Vos angles morts et vos lacunes | **Non** | C'est du renseignement sur vous (chapitre 34) |
| Ce qui est sous marquage restrictif reçu | **Non** | §20.5 |

⚠️ **Le point d'attention le plus fréquent** : un indicateur peut révéler votre architecture. Une adresse interne, un nom d'hôte, un format de compte, une plage horaire — ces éléments accompagnent parfois un partage sans que personne n'y prenne garde. **Relisez ce que vous transmettez comme si vous étiez le destinataire.**

### 28.3 Anonymisation et niveaux de diffusion

**Trois degrés d'anonymisation**, à choisir selon l'élément :

| Degré | Ce qui est retiré | Quand |
|---|---|---|
| **Aucun** | — | Indicateur purement externe : domaine adverse, adresse d'infrastructure |
| **Partiel** | Ce qui identifie l'actif touché, en conservant le contexte | Mode opératoire, séquence observée |
| **Complet** | Toute référence à l'organisation, y compris indirecte | Détail d'incident, statistique interne |

**Le piège de l'anonymisation partielle** : un ensemble d'éléments individuellement anonymes peut identifier l'organisation par recoupement — secteur, taille, technologie employée, date. Dans un dispositif sectoriel de vingt membres, la marge est mince.

**Le marquage de diffusion** (§20.5) accompagne systématiquement le partage, et il porte sur ce que le destinataire peut **retransmettre**, distinctement de ce qu'il peut **faire**.

### 28.4 Le fonctionnement réel d'un dispositif sectoriel

**Ce qu'on y trouve**, dans l'ordre de fréquence :

| Contenu | Fréquence | Valeur |
|---|---|---|
| Indicateurs partagés par les membres | Élevée | Variable |
| Alertes reprises de sources publiques | Élevée | **Faible** — vous les avez déjà |
| Questions posées par des membres | Moyenne | **Élevée** — c'est là que se joue l'entraide |
| Retours d'expérience d'incidents | **Faible** | **Très élevée** |
| Analyses produites par le dispositif | Variable | Élevée quand elles existent |

**La ligne des questions est celle qui surprend.** Un membre qui demande *« quelqu'un a-t-il observé ceci ? »* obtient souvent une réponse en quelques heures — et c'est le mécanisme le plus rapide et le moins coûteux de tout le dispositif. C'est aussi celui qui exige le plus de confiance mutuelle, donc celui qui se construit en dernier.

**Ce qui fait la valeur d'un dispositif** : moins la quantité partagée que **la vitesse de réponse aux questions**. Un dispositif où l'on obtient une réponse en trois heures vaut mieux qu'un dispositif qui diffuse trois cents indicateurs par semaine.

### 28.5 ⚠️ Le partage à sens unique

**Le constat** : dans tout dispositif, une minorité produit la majorité. Ce n'est pas un dysfonctionnement (§20.6) — mais il existe un seuil au-delà duquel le déséquilibre devient un problème.

| Situation | Diagnostic |
|---|---|
| Vous recevez trois fois plus que vous ne donnez | **Normal**, surtout la première année |
| Vous n'avez rien partagé depuis six mois | **À corriger** — la réciprocité est la règle implicite |
| Vous partagez uniquement ce qui ne coûte rien | Acceptable, mais limité |
| Vous ne posez jamais de question | **Vous n'exploitez pas le dispositif** |

**Les trois choses qu'une organisation peut toujours partager**, même sans capacité d'analyse :

1. **Une confirmation** : *« nous avons observé la même chose »*. Coût : cinq minutes. Valeur : élevée pour l'émetteur.
2. **Une infirmation** : *« nous avons vérifié, nous ne le voyons pas chez nous »*. Coût identique, valeur souvent supérieure — elle aide à cerner un périmètre.
3. **Une question** : elle enrichit le dispositif en signalant un sujet.

⚠️ Une organisation qui pense n'avoir rien à partager se trompe presque toujours : elle confond « produire une analyse » et « contribuer ».

### 28.6 Ce que le partage révèle de vous

**Le versant que personne n'examine**, et qui prépare le chapitre 34.

| Ce que vous partagez | Ce que cela révèle |
|---|---|
| Un indicateur | Que vous l'avez observé — donc que vous êtes visé ou touché |
| Une question précise | Ce qui vous préoccupe, donc où vous vous sentez vulnérable |
| Une analyse détaillée | Votre niveau de capacité — utile et exploitable |
| Un silence prolongé | Que vous n'observez rien, ou que vous ne pouvez rien dire |
| **Le moment où vous partagez** | Quand vous avez découvert |

**Ce qu'il faut en faire** : pas renoncer au partage — la valeur reçue dépasse largement ce risque dans un dispositif de confiance. Mais **relire ce qu'on transmet** en se demandant ce qu'un observateur attentif en déduirait.

🎯 **ET MAINTENANT ?**
*Vous subissez un incident. Un membre du dispositif sectoriel demande si quelqu'un a observé une activité correspondant à des indicateurs qu'il diffuse — ce sont les vôtres. Que faites-vous ?*
**Réponse** : vous répondez, et vous décidez du degré. Le minimum utile et sans risque : *« observé, période cohérente avec la vôtre »*. Cela confirme, aide l'émetteur, et ne révèle ni l'ampleur, ni le vecteur, ni le résultat. Si votre organisation le permet et que la confiance est établie, ajouter le vecteur d'entrée a une valeur considérable pour les autres membres — et c'est une décision de niveau direction, pas une décision d'analyste. Ce qui n'est jamais acceptable, c'est de ne pas répondre : vous savez, et le silence a un coût pour la communauté que vous exploitez par ailleurs.

### 28.7 🔴 FIL ROUGE — mars 2030 : ce qu'HELIOMED partage de son incident

L'incident de février (§23.7) a produit quatorze indicateurs, dont neuf encore valides. La question se pose au comité du 12 mars : que partage-t-on ?

**Les positions initiales**, et elles sont toutes défendables :

| Personne | Position |
|---|---|
| Nour | Partager les indicateurs et le mode opératoire — c'est utile aux membres |
| Yann Prigent | Prudence — nos clients sont membres du même dispositif |
| Le juridique | Vérifier ce que la charte engage, et ce que révèle chaque élément |
| Claire | Partager, mais décider **quoi** élément par élément |

**La décision, prise élément par élément** :

| Élément | Partagé ? | Motif |
|---|---|---|
| 9 indicateurs valides | **Oui**, sans anonymisation | Purement externes : domaines et adresses adverses |
| Le mode opératoire — 6 techniques | **Oui**, anonymisation partielle | Sans mention de l'actif touché ni du service concerné |
| Le vecteur d'entrée — pièce jointe, macro | **Oui** | Générique, aucune information sur HELIOMED |
| **L'exclusion de politique** qui a permis l'exécution | **Non** | Révèle une faiblesse de configuration propre |
| Le délai de détection — 11 jours | **Non** | Révèle une capacité |
| Le fait que la victime soit HELIOMED | **Non** | Anonymisation complète |
| Ce qui a arrêté l'adversaire | **Oui**, formulé génériquement | *« détection par alerte sur accès inhabituel à un dépôt de code »* — utile aux autres, sans révéler notre dispositif |

**La ligne la plus discutée est la dernière.** Yann Prigent objecte qu'elle révèle une capacité de détection. Nour répond que la formulation générique ne dit ni quel outil, ni quelle règle, ni quel seuil — et qu'elle est précisément l'information la plus utile aux autres membres, parce qu'elle indique **où regarder**.

Claire tranche pour le partage, avec la formulation exacte validée en séance.

**L'effet, dans les trois semaines** :

| Retour | Délai |
|---|---|
| Deux membres signalent une activité correspondant aux indicateurs | 8 et 19 jours |
| Un membre demande des précisions sur le vecteur | 4 jours |
| **Un membre signale avoir la même exclusion de politique** | 11 jours |

**Le dernier retour est celui que personne n'attendait.** Un membre, en lisant le mode opératoire, a vérifié sa propre configuration et découvert une exclusion équivalente — non partagée par HELIOMED, mais déduite du fait que la macro s'était exécutée.

**Ce que Claire en tire**, et qui nuance sa propre décision :

> *« Nous n'avons pas partagé l'exclusion. Ils l'ont déduite. C'est une information à garder en tête : ce qu'on tait n'est pas toujours invisible. »*

**Le bilan du partage à douze mois** figure au §20.8 : 34 éléments transmis, 91 exploités, quatre alertes reçues avant publication publique. Le rapport de 1 pour 2,7 est présenté sans gêne.

**Livrable de l'épisode.** La grille de décision élément par élément, et la règle : *ce qu'on partage se décide par élément, jamais par document*.

→ **Fin de la Partie VI.** La suite en Partie VII, quand il faudra transformer tout cela en décisions — et savoir quand ne rien faire.

---

> ### 🎓 À ce stade de la Partie VI, vous savez…
>
> - **placer la conclusion en tête**, et écrire une première phrase en quatre éléments ;
> - **structurer un produit** avec trois titres explicites qui disciplinent l'auteur autant qu'ils orientent le lecteur ;
> - **adapter à cinq destinataires** sans jamais altérer la conclusion — et savoir que cela coûte moins de temps que l'analyse ;
> - **dire ce que vous attendez du destinataire**, faute de quoi l'inaction est le résultat par défaut ;
> - **alerter selon quatre conditions cumulatives**, et savoir que la capacité d'alerter est un crédit qui se dépense ;
> - **clore une alerte**, et revenir dessus deux semaines plus tard ;
> - **décider ce qui se partage élément par élément**, et relire ce que vous transmettez comme si vous étiez le destinataire.
>
> **Ce que vous ne savez pas encore** : comment tout cela se transforme en décisions — y compris la décision de ne rien faire, qui est la plus fréquente. C'est l'objet de la Partie VII.

---
