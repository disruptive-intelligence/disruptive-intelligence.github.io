---
title: PARTIE IV — Les réseaux et les zones
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 5
chapters: 10
---

> Le chapitre 5 a posé les six zones de référence. Cette partie descend d'un cran : **comment une frontière est réellement matérialisée**, et ce qu'elle permet ou interdit.
>
> Deux chapitres traitent de zones que les schémas ne montrent presque jamais — l'administration et l'industriel — et ce sont les deux plus importants de la partie.

---

## Chapitre 24 — Le réseau local et la segmentation

### 24.1 Le segment, unité de base

**Un segment est un ensemble de machines qui se joignent directement**, sans traverser d'équipement de routage.

> **La règle de lecture, formulée précisément** :
>
> **Placer deux systèmes dans un même segment ne crée pas entre eux la frontière de filtrage inter-segments que le schéma fait apparaître.** Leur isolation éventuelle est à chercher ailleurs — et le schéma ne la montre pas.

📌 **Ce qui peut isoler deux machines d'un même segment**, et qu'aucun schéma de zones ne représente :

| Mécanisme | Où il s'applique | Ce qu'il coûte |
|---|---|---|
| Pare-feu local sur l'hôte | Sur chaque machine | Une configuration à déployer et maintenir sur chaque poste |
| Isolation de ports, réseaux virtuels isolés | Sur le commutateur | Une configuration réseau fine |
| Contrôle d'accès au réseau | À la connexion | Un composant supplémentaire, et des exceptions à gérer |
| Politiques distribuées, microsegmentation | Par un dispositif dédié | **Un système complet à exploiter** |

⚠️ **La conséquence à retenir** : un pare-feu entre deux zones ne dit rien des échanges **à l'intérieur** de chaque zone. Sans l'un des mécanismes ci-dessus, une compromission dans un segment de six cents postes atteint les autres sans traverser la frontière dessinée. **La question de lecture n'est donc pas « sont-ils isolés ? » mais « par quel mécanisme le seraient-ils ? »**

### 24.2 Segmenter, et jusqu'où

| Découpage | Ce qu'il isole | Coût | Quand il se justifie |
|---|---|---|---|
| Par **fonction** — postes, serveurs, impression | La contamination entre familles d'usage | Faible | **Presque toujours** |
| Par **sensibilité** — production, recette, développement | Les environnements | Faible à moyen | Dès qu'un environnement contient des données réelles |
| Par **service métier** | La propagation entre applications | **Moyen à élevé** | Quand les conséquences d'une propagation diffèrent fortement |
| Par **poste** — isolation totale | Tout | **Très élevé** | Rarement, et jamais sans outillage dédié |

⚖️ **CONTRAINTE ET COÛT — la segmentation fine**

| Résout | Coûte |
|---|---|
| Limiter la propagation latérale | Des dizaines de flux à ouvrir, documenter, maintenir |
| Appliquer des règles par population | **Un diagnostic plus long** — *« ça ne passe pas, mais où ? »* |
| Démontrer un cloisonnement | **Des contournements si le processus d'ouverture est trop lent** |

⚠️ **Principe du coût, appliqué** : la ligne du bas est la plus importante. Une segmentation dont l'ouverture de flux demande trois semaines produit, en dix-huit mois, un ensemble de contournements — machines à double interface, comptes partagés, règles « temporaires ». **Une segmentation contournée protège moins qu'une segmentation absente, parce qu'on croit qu'elle protège.**

### 24.3 Le coût réel d'une segmentation, chiffré

**Ce qu'on oublie d'évaluer avant de segmenter** :

```
   Segmenter un parc en 6 zones au lieu de 2

   ①  Recenser les flux existants        → 2 à 4 semaines
   ②  Les documenter et les valider      → chaque flux a un demandeur
                                            à retrouver
   ③  Écrire les règles                  → 50 à 300 règles selon le parc
   ④  Basculer                           → par lots, avec retours arrière
   ⑤  Traiter les flux oubliés           → ⚠️ LE PLUS LONG
                                            on ne les découvre qu'en cassant
   ⑥  Maintenir                          → chaque projet ajoute des flux
```

⚠️ **L'étape ⑤ est celle qui fait échouer les projets de segmentation.** On ne connaît pas les flux existants : on les découvre en les coupant. **La seule méthode qui fonctionne est d'observer d'abord, filtrer ensuite** — passer plusieurs semaines en mode « journalisation sans blocage » avant d'appliquer la moindre règle.

🔥 **SCÉNARIO — la segmentation casse un flux que personne ne connaissait**

| Question | Réponse |
|---|---|
| Symptôme | Trois semaines après la segmentation, une facturation mensuelle échoue |
| Hypothèse naïve | « Un problème applicatif » |
| Dépendance réelle | **Un flux mensuel entre deux serveurs**, jamais documenté, coupé par une règle |
| Ce que le schéma aurait dû montrer | Les flux périodiques — **ils n'apparaissent dans aucune observation courte** |
| Concevoir différemment | Observer **au moins un cycle métier complet** avant de filtrer — un mois, parfois un trimestre |

⚠️ **Les flux périodiques sont l'angle mort de toute observation.** Un flux trimestriel n'apparaît pas dans deux semaines de journalisation. **C'est la raison pour laquelle une segmentation casse toujours quelque chose, trois mois après.**

🔭 **À RECONNAÎTRE — VXLAN et EVPN**

**① Le problème.** Dans un grand environnement virtualisé, on veut parfois qu'une machine **conserve son segment logique quel que soit l'hôte physique où elle s'exécute** — y compris après une migration vers une autre baie, voire un autre site. Le découpage physique du réseau ne le permet pas naturellement.

**② La solution.** Construire des **réseaux logiques par-dessus une infrastructure IP existante**.

```
        RÉSEAU LOGIQUE (overlay)
   ╔══════════════════════════════════╗
   ║  segment « production »          ║   ← les machines s'y voient
   ║  segment « recette »             ║      comme si elles étaient
   ╚══════════════════════════════════╝      côte à côte
                  ▲  encapsulation
                  │
   ────────────────────────────────────
        RÉSEAU PHYSIQUE IP (underlay)
        [ commutateur ] ── [ commutateur ] ── [ commutateur ]
```

**③ Le vocabulaire à reconnaître, et rien de plus** :

| Terme | Ce que c'est |
|---|---|
| **Underlay** | Le réseau physique IP, qui transporte |
| **Overlay** | Le réseau logique construit au-dessus |
| **VXLAN** | Le mécanisme d'encapsulation qui rend cela possible |
| **VTEP** | Le point où l'encapsulation commence et se termine |
| **EVPN** | **Un mécanisme de contrôle** fréquemment employé pour distribuer les informations nécessaires à ces réseaux logiques |

**④ Ce que cela change en lecture.** Deux machines qui se voient dans le même segment **peuvent être dans deux baies différentes, voire deux salles**. Le schéma logique et le schéma physique divergent radicalement — c'est le §3.3 poussé à son extrême.

**⑤ Le coût.** Une complexité de diagnostic considérable — **un problème peut venir du réseau logique ou du réseau physique, et les symptômes se ressemblent** · une compétence rare · une dépendance au mécanisme de contrôle.

⚠️ **Un point de sécurité souvent mal compris** : étendre un segment entre deux salles ou deux sites **étend aussi le domaine de propagation d'une compromission** — §24.1. La souplesse d'exploitation se paie en surface d'attaque.

**⑥ En réunion** : *« c'est du VXLAN »* → **quel est le réseau physique sous-jacent ? un problème peut venir des deux** · *« on étend le VLAN entre les deux salles »* → **on étend aussi ce qui peut s'y propager**.

📚 **À approfondir ailleurs** : la conception d'un réseau de centre de données, la configuration des mécanismes de contrôle.

### 24.4 L'accès sans fil

> **Un trou visible dans la plupart des schémas** : les postes sont dessinés — quand ils le sont — reliés par un trait, comme s'ils étaient tous câblés. La majorité ne l'est plus.

#### Le chemin d'un poste sans fil

```
   [ poste ]
       │  ① association au point d'accès
       ▼
   [ point d'accès ]
       │  ② le poste est-il autorisé ? contre quoi ?
       ▼
   [ contrôleur ]  ── ou une configuration distribuée
       │  ③ dans quel segment le poste est-il placé ?
       ▼
   [ réseau d'accès ]
       │  ④ ce segment est-il filtré ? traité comme l'interne ?
       ▼
   [ le reste du système d'information ]
```

⚠️ **Les étapes ② et ③ sont invisibles sur tout schéma**, et ce sont elles qui décident de tout.

#### La question qui structure la lecture

> ### Le Wi-Fi est-il un réseau distinct, ou seulement une autre manière d'entrer dans le même segment ?

**Trois réponses possibles, et elles décrivent trois architectures très différentes** :

```
  A — LE WI-FI EST UNE PORTE SUR LE SEGMENT INTERNE
      [ poste sans fil ] ──► même segment que les postes câblés
      → simple · rien à configurer de plus
      → ⚠️ le périmètre physique du bâtiment ne protège plus rien :
        quiconque obtient la clé est DANS le réseau interne

  B — LE WI-FI EST UN SEGMENT À PART, ROUTÉ VERS L'INTERNE
      [ poste sans fil ] ──► segment sans fil ──► [ filtrage ] ──► interne
      → une frontière existe · on peut restreindre ce que le sans-fil atteint
      → le modèle courant, et le bon compromis dans la plupart des cas

  C — LE WI-FI EST TRAITÉ COMME L'EXTÉRIEUR
      [ poste sans fil ] ──► segment isolé ──► Internet
                                  └──► accès distant ──► interne
      → le poste sans fil n'a aucun privilège du fait d'être dans le bâtiment
      → il revient par le même chemin qu'un poste nomade — §6.3
      → cohérent, et exigeant : le tunnel devient obligatoire pour tous
```

⚠️ **Le mode A est fréquent et rarement assumé comme un choix.** Il transforme une clé partagée — ou un compte d'annuaire — en **entrée directe sur le réseau interne**, sans traverser aucune frontière. Le pare-feu du périmètre n'y peut rien : l'entrée se fait derrière lui.

#### Les réseaux multiples, et ce qu'ils ne garantissent pas

**Une même infrastructure sans fil porte généralement plusieurs réseaux annoncés** :

| Réseau | Qui s'y connecte | Où il devrait aboutir |
|---|---|---|
| **Entreprise** | Postes gérés, authentifiés individuellement | Segment interne ou segment sans fil filtré |
| **Invités** | N'importe qui, avec un code | **Internet seulement, jamais l'interne** |
| **Appareils** | Imprimantes, équipements industriels, capteurs | Un segment dédié, très restreint |
| **Personnel** | Téléphones des salariés | Souvent confondu avec « invités » — à trancher |

⚠️ **Deux réseaux annoncés séparément ne sont pas nécessairement deux segments.** C'est le §24.1 appliqué au sans-fil : **la séparation visible pour l'utilisateur ne dit rien de la séparation réseau**. La question à poser : *ces réseaux aboutissent-ils dans des segments différents, et qu'est-ce qui filtre entre eux ?*

#### Les deux façons d'autoriser un poste

| Méthode | Ce qui authentifie | Ce que ça implique |
|---|---|---|
| **Clé partagée** | Une clé, connue de tous les postes | **Un départ n'invalide rien** · la clé circule · aucune identité individuelle dans les journaux |
| **Authentification individuelle** | Le poste ou l'utilisateur, contre l'annuaire | Une identité par connexion · **une dépendance à l'annuaire pour se connecter au réseau** |

⚠️ **La seconde ligne crée une dépendance nouvelle et peu anticipée** : si l'annuaire est indisponible, **les postes sans fil ne se connectent plus au réseau du tout**. C'est un flux de dépendance de plus — principe des trois flux — et il précède même l'ouverture de session.

🔥 **SCÉNARIO — le sans-fil ne fonctionne plus, le câblé oui**

| Question | Réponse |
|---|---|
| Symptôme | Les postes câblés fonctionnent. Aucun poste sans fil ne se connecte |
| Hypothèse naïve | « Panne des points d'accès » |
| Dépendance réelle | **L'authentification sans fil s'appuie sur l'annuaire ou un service dédié**, indisponible |
| Ce que le schéma aurait dû montrer | Contre quoi le sans-fil authentifie |
| Comment le reconnaître | **Les postes déjà connectés restent connectés** · seules les nouvelles associations échouent |

🔥 **SCÉNARIO — un visiteur atteint un serveur interne**

| Question | Réponse |
|---|---|
| Symptôme | Un audit montre qu'un poste sur le réseau invités joint un serveur de fichiers |
| Hypothèse naïve | « Une erreur de configuration du point d'accès » |
| Dépendance réelle | **Les deux réseaux annoncés aboutissent dans le même segment** — mode A |
| Ce que le schéma aurait dû montrer | Où aboutit chaque réseau sans fil |
| Concevoir différemment | Un segment par usage, avec un filtrage explicite entre eux |

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On a un SSID invités » | Un réseau séparé est annoncé | **Aboutit-il dans un segment distinct ?** Annoncé ≠ segmenté |
| « Le Wi-Fi est en 802.1X » | Authentification individuelle | **Contre quoi ? Que se passe-t-il si ce service tombe ?** |
| « C'est le même réseau que le filaire » | Mode A | **Alors le périmètre physique ne protège plus rien** |
| « On a changé la clé » | Clé partagée | **Combien de fois en cinq ans ? Qui la connaît ?** |
| « Les AP sont gérés par un contrôleur » | Configuration centralisée | **Le contrôleur est-il un point de rupture ?** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Connecter des postes sans câblage | **Une entrée qui contourne le périmètre physique** |
| Authentifier individuellement | Une dépendance de plus, **avant même l'ouverture de session** |
| Séparer les usages par réseau annoncé | Autant de segments et de règles à tenir — sinon la séparation est cosmétique |
| Couvrir un site entier | Des équipements nombreux, à corriger et à surveiller |

🏭 **TROIS TAILLES** — Atelier Martin : un point d'accès, clé partagée, **même segment que les postes câblés** — mode A, non identifié comme un choix. HELIOMED : trois réseaux annoncés, authentification individuelle, segment sans fil filtré vers l'interne — mode B. Novaris : contrôleurs redondés par région, quatre usages séparés, **parce que des magasins accueillent du public et que le réseau invités doit être totalement disjoint**.

🔭 **À RECONNAÎTRE — NAC**

**① Qu'est-ce que c'est.** *Network Access Control* — un dispositif qui répond à une question que la plupart des réseaux ne posent jamais :

> ### Qui décide qu'un équipement a le droit d'entrer sur le réseau ?

**② Quel problème il résout.** Par défaut, **un câble branché fonctionne**. Un poste inconnu obtient une adresse — §15.5 — et se retrouve dans le segment, avec tout ce que cela implique — §24.1. Le NAC insère une décision avant l'accès.

**③ Où on le rencontre.** Sur le réseau filaire des sites accueillant du public ou des visiteurs, et **systématiquement associé au sans-fil d'entreprise** — §24.4.

**④ Ce que cela change.**

```
   SANS NAC
      [ terminal ] ──► réseau d'accès ──► segment ──► tout

   AVEC NAC
      [ terminal ]
           ▼
      réseau d'accès
           ▼
      [ CONTRÔLE D'ACCÈS ]   ← qui es-tu ? es-tu conforme ?
           ▼
      segment et politique APPROPRIÉS
           │
           ├── poste géré et conforme  → segment interne
           ├── poste géré non conforme → segment de remédiation
           ├── équipement reconnu       → segment dédié
           └── inconnu                  → segment invité, ou rien
```

⚠️ **Ce que le schéma montre et qui compte** : le NAC ne fait pas qu'autoriser ou refuser. **Il place le terminal dans un segment en fonction de ce qu'il est.** C'est un mécanisme de segmentation dynamique, et c'est ce qui le rend puissant.

**802.1X** est la technologie fréquemment associée — vous en entendrez le nom, vous n'avez pas à en connaître le détail.

**⑤ Le coût.** Un projet long, parce qu'il faut d'abord **savoir ce qui se connecte** — imprimantes, capteurs, équipements industriels, prestataires · des exceptions inévitables pour ce qui ne sait pas s'authentifier · **une dépendance de plus au démarrage** — §24.4 · un mode dégradé à définir : *que fait-on si le NAC tombe, on laisse tout entrer ou plus rien ?*

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a du NAC » | **Sur tout le parc, ou seulement le sans-fil ?** Le filaire est souvent laissé de côté |
| « On est en 802.1X » | Authentification à la connexion. **Contre quoi ? Et les équipements qui ne le savent pas ?** |
| « On a mis des exceptions par adresse matérielle » | Une liste de dérogations. **Combien ? Depuis quand ? Une adresse matérielle se falsifie** |
| « Si le NAC tombe, on ouvre tout » | Mode dégradé permissif. **C'est un choix — est-il assumé et écrit ?** |

### 24.5 Trois architectures de segmentation

```
  A — DEUX ZONES
      [ postes ] │ [ serveurs ]
      → simple · une frontière à tenir
      → une compromission de poste atteint tous les postes

  B — SEGMENTATION PAR FONCTION
      [ postes ] │ [ serveurs ] │ [ impression ] │ [ admin ] │ [ industriel ]
      → le modèle courant · bon rapport effet/coût
      → 5 frontières, quelques dizaines de règles

  C — MICROSEGMENTATION
      chaque machine a sa propre politique
      → propagation quasi impossible
      → ⚠️ un système complet à exploiter, et une visibilité
        totale des flux exigée en préalable
```

**La contrainte qui fait passer de A à B** : la présence d'actifs dont la compromission a des conséquences très différentes — un automate industriel, un serveur de sauvegarde, un poste d'administration.

⚠️ **Le mode C n'est pas une version améliorée de B.** C'est un changement de nature : il suppose de connaître **tous** les flux, en permanence. Une organisation qui n'a pas réussi B ne réussira pas C.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est segmenté » | Plusieurs zones existent | **Combien ? Et à l'intérieur de chacune ?** |
| « On a un VLAN par service » | Segmentation logique fine | **Le routage entre eux est-il filtré, ou juste routé ?** |
| « On va tout ouvrir en attendant » | Une règle large, temporaire | **« En attendant » dure des années** — §4.3 |
| « Ça marchait avant » | Un flux a été coupé | **Un flux périodique ?** — §24.3 |

🏭 **TROIS TAILLES**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Segments | **2** — bureautique, atelier | 9 | Plusieurs centaines |
| Ce qui les justifie | La séparation atelier/bureau, pour la disponibilité de production | Postes par site, serveurs, DMZ, administration, industriel, recette | **Cloisonnement par entité après acquisitions**, plus les usages |

**Novaris n'a pas des centaines de segments parce qu'elle est grande** : elle en a parce que **sept acquisitions ont apporté sept plans d'adressage** qu'aucune fusion n'a rationalisés. Une organisation de même taille née d'une croissance interne en aurait dix fois moins.

---

## Chapitre 25 — La zone démilitarisée

> **Le concept le plus cité du domaine et le moins compris.**

### 25.1 Ce que c'est réellement

**Le nom trompe.** Il évoque une zone neutre entre deux camps. La réalité est différente et plus simple :

> **La zone démilitarisée est l'endroit où l'on place ce qui doit être joignable depuis l'extérieur — en supposant qu'il sera compromis.**

**C'est une hypothèse de conception, pas une protection.** On n'y met pas des choses parce qu'elles y sont en sécurité ; on les y met **pour que leur compromission ne donne pas accès au reste**.

🖼 **SCHÉMA 25.1 — Les deux frontières**

```
        Internet
            │
      ┌─────┴─────┐  ← FRONTIÈRE 1 : ce qui entre, très filtré
      │  filtrage │     « seul le port 443 vers le mandataire »
      └─────┬─────┘
   ╔════════╪════════════════════════════════╗
   ║  ZONE DÉMILITARISÉE                     ║
   ║  [ mandataire ]  [ relais messagerie ]  ║
   ╚════════╪════════════════════════════════╝
      ┌─────┴─────┐  ← FRONTIÈRE 2 : LA PLUS IMPORTANTE
      │  filtrage │     « le mandataire peut joindre UNIQUEMENT
      └─────┬─────┘       le serveur web, sur le port 8080 »
   ╔════════╪════════════════════════════════╗
   ║  RÉSEAU INTERNE                         ║
   ╚═════════════════════════════════════════╝
```

⚠️ **La frontière 2 est celle qui définit une vraie zone démilitarisée**, et c'est celle qu'on oublie. Une « DMZ » qui peut joindre librement le réseau interne n'en est pas une : **c'est un segment exposé**.

**Le test qui tranche, en une question** : *si le mandataire était compromis, que pourrait-il atteindre ?*

| Réponse | Diagnostic |
|---|---|
| Un serveur, sur un port | **C'est une DMZ** |
| Plusieurs serveurs, sur plusieurs ports | Une DMZ affaiblie · à interroger |
| Tout le réseau interne | **Ce n'est pas une DMZ**, c'est un segment exposé |

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. La frontière 1 est dessinée — deux pare-feu. **La frontière 2 ne l'est pas.** C'est la question que le §5.3 posait sans pouvoir la trancher, et c'est la première à poser à l'auteur du schéma.

### 25.2 Le flux retour, et pourquoi il annule tout

**Le point le plus subtil du chapitre, et le plus souvent mal conçu.**

Une DMZ ne sert à rien si le flux **de la DMZ vers l'interne** est trop large. Or il faut bien qu'il existe : le mandataire doit joindre le serveur web.

```
   BIEN CONÇU
      mandataire ──► serveur web       port 8080, uniquement
      Rien d'autre. Le mandataire ne peut joindre aucun autre serveur.

   MAL CONÇU — cas 1
      mandataire ──► TOUT L'INTERNE    ports 80, 443
      « C'est juste du web » — mais tout serveur interne exposant
      du web devient atteignable depuis la DMZ.

   MAL CONÇU — cas 2
      mandataire ──► base de données   port 1433
      Le mandataire court-circuite l'applicatif.
      L'architecture en couches est contournée par une règle de pare-feu.

   MAL CONÇU — cas 3
      mandataire ──► annuaire          ports 389, 636
      Nécessaire s'il authentifie — mais cela signifie qu'un
      mandataire compromis peut interroger l'annuaire.
```

⚠️ **Le cas 3 est légitime et il a un coût.** Placer l'authentification sur le mandataire — §12.2, fonction 3 — impose de lui donner accès à l'annuaire. **C'est un compromis, pas une erreur** : on gagne un contrôle avant l'application, on donne à un composant exposé une visibilité sur l'annuaire. **Principe du coût.**

### 25.3 Les trois erreurs de conception classiques

| Erreur | Ce qu'elle produit |
|---|---|
| **Pas de frontière 2** | La DMZ devient un tremplin vers l'interne |
| **Un composant de la DMZ joignant la base de données** | Le contournement complet de l'architecture en couches |
| **Un serveur à double interface**, une patte dans chaque zone | **La frontière n'existe plus** — §5.4 |

⚠️ **La troisième est la plus discrète, et ses conséquences sont les plus larges.** Une machine avec deux interfaces réseau, une dans chaque zone, **ne traverse aucun pare-feu**. Elle est le pare-feu — et elle n'en a ni les règles, ni les journaux, ni la surveillance. Sur un schéma, elle apparaît comme un composant ordinaire à cheval sur une frontière.

### 25.4 Trois architectures de publication

```
  A — PUBLICATION DIRECTE
      Internet ──► [ FW ] ──► serveur (en interne)
      → aucune DMZ · le serveur exposé est dans le réseau interne
      → une faille du serveur donne un pied dans l'interne
      → convient quand rien de sensible n'est autour

  B — DMZ CLASSIQUE
      Internet ──► [ FW ] ──► DMZ ──► [ FW ] ──► interne
      → le modèle de référence
      → deux jeux de règles · un composant dédié à exploiter

  C — PUBLICATION PAR UN TIERS
      Internet ──► [ service du fournisseur ] ──► lien sortant ──► interne
      → rien n'est exposé : c'est VOTRE serveur qui va vers le tiers
      → aucun flux entrant à ouvrir
      → une dépendance complète au fournisseur — §38
```

⚠️ **Le mode C mérite d'être connu**, parce qu'il inverse la logique : au lieu d'ouvrir un flux entrant, le serveur interne établit lui-même une connexion **sortante** vers un service qui reçoit les clients. **Il n'y a plus rien à exposer** — et il y a un tiers dans le chemin, qui voit tout.

### 25.5 La passerelle d'interconnexion

> **Une fonction architecturale, pas un équipement.** C'est la notion que vous rencontrerez dans les recommandations publiques françaises, et elle mérite d'être nommée.

**La définition** :

> **Une passerelle d'interconnexion est l'ensemble des composants et des fonctions par lesquels deux systèmes ou deux zones de confiance distincts sont autorisés à échanger.**

⚠️ **C'est beaucoup plus juste que *« une passerelle, c'est un pare-feu »***. Un pare-feu est un composant possible de la passerelle ; il n'en est pas la définition.

🖼 **SCHÉMA 25.2 — Une passerelle comme assemblage**

```
                    PASSERELLE D'INTERCONNEXION
          ┌──────────────────────────────────────────┐
  SI A    │  filtrage réseau                         │   SI B
 ────────►│  relais ou mandataire applicatif         ├────────►
          │  contrôle protocolaire ou de contenu     │
          │  authentification                        │
          │  journalisation                          │
          │  éventuellement rupture de flux          │
          └──────────────────────────────────────────┘
```

**Le concept fort** :

> **Interconnecter deux systèmes d'information, ce n'est pas créer une route entre eux. C'est décider quels échanges sont permis, par quels intermédiaires, avec quelle confiance et quelle traçabilité.**

#### Les six choses que la passerelle matérialise

| # | Ce qu'elle établit | Pourquoi c'est une décision, pas une configuration |
|---|---|---|
| **1** | **Une frontière de confiance** | Les deux côtés n'ont pas le même niveau de confiance — c'est le §5.1 |
| **2** | **Une réduction des flux** | On n'ouvre pas les deux réseaux l'un à l'autre : on autorise ce qui est nécessaire |
| **3** | **Des fonctions intermédiaires** | Filtrage, mandataire, contrôle de contenu, terminaison — selon ce que l'échange exige |
| **4** | **Un point de concentration** | Excellent pour contrôler et observer · **et une dépendance forte** |
| **5** | **Une question de sens** | Un flux de A vers B n'implique en rien que B vers A soit autorisé — §P.3 |
| **6** | **Une question de protocoles** | Certaines architectures évitent même la communication directe, par un relais ou un échange contrôlé |

⚠️ **Le point 6 mérite un mot** : quand la différence de confiance est très forte, on renonce à la communication directe. Les données transitent par un relais qui les reconstitue, ou par un mécanisme d'échange où aucune connexion ne traverse la frontière. **C'est le modèle A du §28.4, appliqué au-delà de l'industriel.**

#### Connectivité et contrôle de frontière ne sont pas la même chose

**Un exercice qui vaut d'être fait, parce que les deux sont constamment confondus** :

```
                    CONNECTIVITÉ
   Site A ══════════════════════════════════ Site B
            MPLS · Internet · SD-WAN
                         ≠
                CONTRÔLE DE FRONTIÈRE
   SI A ─────► [ passerelle d'interconnexion ] ─────► SI B
```

| | Ce à quoi ça répond |
|---|---|
| **Connectivité** | *Comment les paquets rejoignent-ils l'autre environnement ?* |
| **Passerelle** | *Sous quelles conditions avons-nous décidé qu'ils pouvaient y entrer ?* |

**Un SD-WAN peut transporter un flux vers un autre site. Une passerelle décide ensuite si ce flux entre dans le système cible, et comment.** Les deux fonctions sont parfois portées par le même équipement ou le même contrat — **les responsabilités architecturales restent distinctes**.

#### Le principe à retenir

> ### Relier deux réseaux ne signifie pas qu'ils doivent devenir un seul périmètre de confiance.

**C'est la raison d'être de tout ce chapitre** : les zones, le filtrage, les mandataires, l'authentification, les flux explicitement autorisés — toutes ces notions existent pour que **l'interconnexion ne soit pas une extension de confiance**.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça passe par la passerelle d'interco » | Les échanges traversent une architecture de contrôle dédiée | **Quelles fonctions contient-elle réellement ?** |
| « On ouvre l'interconnexion » | De nouveaux flux entre deux périmètres vont être autorisés | **Quels flux exactement, dans quel sens ?** |
| « Les deux SI sont interconnectés » | Une connectivité existe | **Routage complet, ou seulement quelques services ?** |
| « C'est filtré » | Un mécanisme de contrôle existe | **À quel niveau, et selon quelle politique ?** |

⚠️ **La troisième ligne est celle qui révèle le plus.** *« Interconnectés »* recouvre aussi bien *« trois flux applicatifs autorisés »* que *« les deux réseaux se voient entièrement »* — et l'écart entre les deux est considérable.

### 25.6 Ce que la DMZ ne protège pas

| Elle protège | Elle ne protège pas |
|---|---|
| L'interne, si un composant exposé est compromis | **Les échanges entre composants de la DMZ** |
| Contre une exposition directe des serveurs internes | Contre une faille du mandataire lui-même |
| Contre un balayage depuis Internet | **Contre un poste interne compromis** — §6.1 |

⚠️ **La dernière ligne est celle qu'on oublie systématiquement.** Toute l'architecture de la DMZ suppose que la menace vient de l'extérieur. **Elle est sans effet sur la menace qui commence sur un poste** — et c'est une voie d'entrée majeure.

🔥 **SCÉNARIO — la DMZ n'a servi à rien**

| Question | Réponse |
|---|---|
| Symptôme | Compromission du serveur de fichiers interne. La DMZ n'a rien vu |
| Hypothèse naïve | « La DMZ a été franchie » |
| Dépendance réelle | **L'entrée s'est faite par un poste utilisateur.** La DMZ n'était pas sur le chemin |
| Ce que le schéma aurait dû montrer | Les postes — §6.1 |
| Concevoir différemment | Segmenter à l'intérieur, pas seulement au périmètre — §24.2 |

### 25.7 Sur un schéma

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans la DMZ » | Le composant est exposé | **Que peut-il joindre en interne ?** C'est la seule question qui compte |
| « On va ouvrir un flux depuis la DMZ » | Une règle de la frontière 2 | Vers quoi exactement ? Un serveur, ou une plage ? |
| « Le serveur a deux pattes » | Deux interfaces réseau, deux zones | **La frontière n'existe plus à cet endroit** |
| « C'est une DMZ, c'est sécurisé » | Confusion fréquente | La DMZ **suppose la compromission**, elle ne l'empêche pas |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Publier des services sans exposer l'interne | Des composants dédiés à exploiter et corriger en priorité |
| Contenir une compromission attendue | **Des flux traversants à définir finement** — et à ne pas élargir |
| Séparer les cycles de mise à jour | **Une administration à part** — chapitre 27 |
| Authentifier en amont | Un accès à l'annuaire depuis une zone exposée |

🏭 **TROIS TAILLES** — Atelier Martin : **aucune DMZ**, parce qu'elle ne publie aucun service. HELIOMED : une, parce qu'elle publie une plateforme client. Novaris : plusieurs, séparées par usage — publication web, échanges partenaires, accès distant — **parce que ces trois usages n'ont ni les mêmes flux entrants ni les mêmes conséquences en cas de compromission**.

---

## Chapitre 26 — Le réseau étendu et les sites distants

### 26.1 Ce que la distance change

| Contrainte | Effet |
|---|---|
| **Latence** | Certaines applications deviennent inutilisables au-delà d'un seuil |
| **Débit** | Partagé entre tous les usages du site |
| **Disponibilité** | Un lien unique est un point de rupture pour tout un site |
| **Coût** | La redondance d'un lien double une facture récurrente |

**La question de lecture** : *ce site fonctionne-t-il si le lien tombe ?* Trois réponses possibles, et chacune décrit une architecture différente :

| Réponse | Architecture |
|---|---|
| **Non, rien ne fonctionne** | Tout est centralisé. Site totalement dépendant |
| **Partiellement** | Des services locaux — annuaire, fichiers — subsistent |
| **Oui** | Site autonome, avec ses propres dépendances locales |

⚠️ **La deuxième est très répandue, et elle est rarement documentée.** Personne ne sait exactement ce qui subsiste, **parce que personne n'a coupé le lien pour voir**.

### 26.2 Les dépendances locales

**Ce qui doit être local pour qu'un site survive à une coupure** — et c'est le principe des trois flux appliqué à la géographie :

| Service | Local ? | Effet si distant et le lien tombe |
|---|---|---|
| **Résolution de noms** | Devrait l'être | Plus rien ne fonctionne sur le site |
| **Contrôleur d'annuaire** | Devrait l'être | Plus d'ouverture de session |
| **Attribution d'adresses** | Devrait l'être | Panne différée, au fil des redémarrages |
| Fichiers | Selon l'usage | Travail bloqué, service non |
| Applications métier | Rarement | Le site est à l'arrêt fonctionnel |
| Accès Internet | Selon | Sortie centralisée ou locale : deux architectures — §11.3 |

**Les trois premières lignes sont les trois flux de dépendance des chapitres 14 à 16.** Un site sans elles n'a aucune autonomie, quelle que soit la qualité de son réseau local.

⚠️ **Un piège fréquent sur le contrôleur d'annuaire local** : il existe, il fonctionne, **et il réplique depuis le siège**. Si le lien tombe longtemps, la réplication s'interrompt — les authentifications continuent, mais les changements de mot de passe faits au siège ne sont pas connus localement. **L'autonomie n'est pas totale, elle est datée.**

### 26.3 Trois architectures de sites

```
  A — TOUT CENTRALISÉ
      site distant ══lien══► [ siège : tout ]
      → simple · rien à exploiter sur site
      → le lien tombe : le site est à l'arrêt complet
      → convient si le lien est très fiable et l'arrêt tolérable

  B — SOCLE LOCAL
      site distant : [ résolution ] [ annuaire ] [ fichiers ]
                            ══lien══► [ siège : applications ]
      → les postes démarrent, les sessions s'ouvrent, le travail
        local continue
      → les applications métier restent indisponibles
      → ⚠️ c'est l'architecture la plus répandue, et son autonomie
        n'est presque jamais testée

  C — SITE AUTONOME
      site distant : tout ce dont il a besoin
                            ══lien══► [ siège : consolidation ]
      → autonomie complète
      → autant de systèmes à exploiter que de sites
```

**La contrainte qui décide** : *combien de temps le site peut-il rester arrêté ?* — et la réponse chiffrée détermine directement le choix.

🔭 **À RECONNAÎTRE — MPLS**

**① Qu'est-ce que c'est.** Vous le rencontrerez presque toujours comme **un service d'opérateur permettant d'interconnecter plusieurs sites** au sein d'un réseau privé porté par cet opérateur.

**② Quel problème il résout.** Relier dix agences au siège sans construire dix liaisons dédiées, avec des garanties de service que l'accès Internet ordinaire n'offre pas — débit engagé, latence, priorisation.

**③ Où on le rencontre.** *« Nos agences sont sur le MPLS »* est une phrase que vous entendrez. Elle désigne le réseau étendu de l'organisation, souscrit auprès d'un opérateur.

**④ Ce que cela change.**

```
   [ agence 1 ] ──┐
   [ agence 2 ] ──┼──► [ réseau de l'opérateur ] ──► [ siège ]
   [ agence 3 ] ──┘
```

Les sites se voient comme s'ils étaient sur un même réseau privé. **Le routage est simplifié**, et la qualité de service est contractuelle.

⚠️ **⑤ Le risque, et c'est l'erreur la plus fréquente sur ce sujet** :

> **Un réseau privé d'opérateur n'est pas un chiffrement de bout en bout.**

« Privé » signifie *séparé du trafic des autres clients par le mécanisme de l'opérateur*, pas *illisible par l'opérateur*. **La question professionnelle devient donc** : *quelles garanties le service apporte-t-il réellement, et faut-il ajouter du chiffrement au-dessus ?*

Autres coûts : une dépendance forte à un opérateur unique · un délai de raccordement d'un nouveau site en semaines ou en mois · un coût récurrent élevé comparé à un accès Internet.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « Les sites sont sur le MPLS » | **Le trafic est-il chiffré au-dessus ?** Et si le lien tombe, que reste-t-il ? |
| « On a du QoS sur le MPLS » | Des flux sont priorisés. **Lesquels, et selon quel engagement contractuel ?** |
| « On sort par le siège » | Sortie Internet centralisée — §11.3 |

---

🔭 **À RECONNAÎTRE — SD-WAN**

**① Qu'est-ce que c'est.** Et c'est ici qu'il faut être précis, parce que la confusion est constante :

> **Le SD-WAN n'est pas un nouveau type de liaison. C'est une couche de pilotage qui utilise plusieurs transports et décide comment les flux les empruntent, selon des politiques.**

**② Quel problème il résout.** Un site dispose souvent de plusieurs accès — un lien opérateur, un accès Internet, une connexion cellulaire de secours. Sans pilotage, on choisit **une** route par destination. Le SD-WAN permet de choisir **par flux**, selon des critères applicatifs.

**③ Où on le rencontre.** Dans les architectures multi-sites récentes, et dans toute organisation qui a migré des applications vers des services en ligne — parce que faire remonter au siège un trafic destiné à Internet devient absurde.

🖼 **SCHÉMA 26.1 — Ce que le SD-WAN ajoute**

```
                         ┌── MPLS ──────────┐
  [ Site A ] ─[SD-WAN]───├── Internet ──────┼───[SD-WAN]─ [ SI / Cloud ]
                         └── 4G / 5G ───────┘

  SANS SD-WAN      destination → route → lien
  AVEC SD-WAN      application + qualité du lien + politique → lien

     Téléphonie    → le lien de plus faible latence
     Progiciel     → le lien opérateur
     Web et SaaS   → sortie Internet locale
     Secours       → connexion cellulaire
```

**④ Les quatre implications architecturales**, et c'est ce que le lecteur doit retenir :

| # | Implication |
|---|---|
| **1** | **Il existe un plan de pilotage supplémentaire.** Des équipements appliquent sur site des politiques définies ailleurs. Une architecture qui paraît avoir trois liens indépendants **peut dépendre d'un contrôleur central** |
| **2** | **Le chemin devient dynamique.** Deux connexions vers la même application n'ont pas nécessairement emprunté le même lien. Cela complique le dépannage, la journalisation et le filtrage |
| **3** | **La sortie Internet locale contourne le datacenter.** Le modèle *agence → siège → pare-feu central → Internet* devient *agence → Internet directement* — **et les contrôles centraux ne s'appliquent plus** |
| **4** | **Le SD-WAN apporte de la connectivité et du pilotage**, pas de la sécurité par magie. Les fonctions de sécurité dépendent de l'architecture et du produit |

⚠️ **La troisième implication est la plus lourde en sécurité.** Elle déplace le point où l'on peut agir — chapitre 43 — sans que rien sur le schéma ne le signale.

**⑤ Le coût**

> **Le SD-WAN simplifie le pilotage de plusieurs liens, et rend le chemin réel d'un flux beaucoup moins évident à déduire d'un schéma statique.**

Plus : un plan de pilotage qui devient un composant critique · une dépendance à un fournisseur · des politiques à maintenir.

**⑥ En réunion**

| Ce que vous entendrez | Ce que cela signifie probablement | À vérifier |
|---|---|---|
| « Le site est en SD-WAN » | Plusieurs transports pilotés par une couche logique | **Quels transports ? Qui décide du chemin ?** |
| « On fait du breakout local » | Le trafic Internet sort directement du site | **Quels contrôles restent sur ce chemin ?** |
| « Ça bascule automatiquement » | Une politique choisit un autre lien | **Sous quelles conditions ? Testé ? En combien de temps ?** |
| « Le SD-WAN prend le meilleur lien » | Il applique des métriques et des politiques | **Meilleur selon quel critère ?** |

📚 **À approfondir ailleurs** : la conception d'une politique de pilotage, les mécanismes propres à chaque constructeur.

### 26.4 Le lien lui-même

| Configuration | Ce qu'elle protège | Principe de preuve |
|---|---|---|
| Lien unique | Rien | — |
| Deux liens, même opérateur | Une panne d'équipement | **Pas une panne de l'opérateur** |
| Deux liens, deux opérateurs | Une panne d'opérateur | **Pas une coupure de la tranchée commune** |
| Deux liens, deux opérateurs, deux arrivées physiques | La plupart des cas | Le coût est nettement supérieur |

⚠️ **La ligne « même tranchée » est réelle et fréquente.** Deux opérateurs différents peuvent emprunter le même fourreau à l'entrée du bâtiment. Une pelleteuse coupe les deux. **La question à poser : les deux liens entrent-ils par le même endroit ?**

🔥 **SCÉNARIO — le lien fonctionne, le site est bloqué**

| Question | Réponse |
|---|---|
| Symptôme | Le lien est supervisé au vert. Les utilisateurs du site ne peuvent plus travailler |
| Hypothèse naïve | « Problème réseau » |
| Dépendance réelle | **L'authentification centrale.** Le lien porte les paquets, mais un composant au siège ne répond plus |
| Ce que le schéma aurait dû montrer | Ce qui est local et ce qui est distant — §26.2 |
| Concevoir différemment | Superviser **le service rendu**, pas seulement le lien |

⚠️ **C'est l'illustration du §35.2** : la supervision d'un lien ne dit rien de la disponibilité d'un service qui l'emprunte.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le site est coupé » | Le lien est indisponible | **Ou un service central l'est.** Ce n'est pas la même chose |
| « On a un lien de secours » | Un second lien existe | Même opérateur ? Même arrivée physique ? **Testé ?** |
| « Ils ont un DC local » | Un contrôleur d'annuaire sur site | **Réplique-t-il ? Depuis quand ?** L'autonomie est datée |
| « Ils sortent par le siège » | Sortie Internet centralisée | Si le lien tombe : plus d'Internet non plus — §11.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Centraliser l'exploitation | **Un site totalement dépendant du lien** |
| Un socle local | Des composants à exploiter sur chaque site |
| Redonder le lien | Une facture récurrente doublée · **et souvent une fausse redondance** — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : un site, la question ne se pose pas. HELIOMED : trois sites, avec résolution et annuaire locaux à Nantes et Saint-Étienne, **mais applications centralisées à Lyon** — autonomie partielle, jamais testée. Novaris : quarante sites, socle local standardisé, **parce que la coupure d'un lien ne doit pas arrêter un magasin**.

---

## Chapitre 27 — Le réseau d'administration

> **Invisible sur les schémas, décisif en sécurité.** L'un des deux chapitres les plus importants de la partie.

### 27.1 Pourquoi il existe

**Le constat de départ** : administrer un système suppose des accès **plus puissants** que ceux nécessaires pour l'utiliser.

| Ce qu'un utilisateur peut faire | Ce qu'un administrateur peut faire |
|---|---|
| Consulter ses données | Consulter toutes les données |
| Utiliser une application | Arrêter, modifier, contourner l'application |
| Ouvrir sa session | **Ouvrir n'importe quelle session** |
| — | **Effacer les traces de son passage** |

> **Le chemin d'administration est plus puissant que ce qu'il administre.** C'est pourquoi il justifie une zone à part.

⚠️ **La dernière ligne du tableau est celle qui change tout en réponse à incident** : un administrateur — ou quelqu'un qui a pris sa place — peut modifier les journaux. **C'est pourquoi les journaux d'administration doivent partir ailleurs, immédiatement** — §34.3.

### 27.2 Ce qu'on y trouve

🖼 **SCHÉMA 27.1 — Le chemin d'administration**

```
   [ poste d'administrateur ]
              │
              ▼  authentification renforcée
   ┌──────────────────────┐
   │  POSTE DE REBOND     │  ← unique point de passage
   │  (« bastion »)       │     journalisé, parfois enregistré
   └──────────┬───────────┘
              │
   ┌──────────┼──────────┬──────────────┐
   ▼          ▼          ▼              ▼
 serveurs   réseau   virtualisation   sauvegarde
                       (plan de
                        gestion)
```

| Composant | Rôle | Ce qui arrive s'il manque |
|---|---|---|
| **Poste dédié** | Un poste qui ne sert qu'à administrer | Un poste bureautique compromis donne l'administration |
| **Point de rebond** | Le passage unique et journalisé | Aucune trace centralisée des actions privilégiées |
| **Coffre de secrets** | Stocke et renouvelle les identifiants privilégiés | Des mots de passe partagés, jamais changés — §33 |
| **Segment isolé** | Non joignable depuis le réseau bureautique | Le rebond est atteignable par un poste compromis |

### 27.3 Les quatre chemins d'administration qu'on oublie

**Le rebond couvre les serveurs. Il ne couvre presque jamais ces quatre-là** :

| Chemin oublié | Pourquoi il échappe | Ce qu'il donne |
|---|---|---|
| **Le plan de gestion de virtualisation** | Interface web, souvent accessible depuis le bureautique | **L'accès aux disques de toutes les machines** — §23.4 |
| **Les interfaces d'administration matérielle** | Cartes de gestion à distance, sur un réseau à part | **Un accès en dessous du système** |
| **Les consoles des équipements réseau** | Administrées par une autre équipe | Le routage et le filtrage |
| **Les accès des prestataires** | Contractuels, hors processus | **Des postes que vous ne maîtrisez pas** — §38.4 |

⚠️ **Le deuxième est le plus méconnu.** Les cartes de gestion à distance permettent d'allumer, éteindre, réinstaller une machine et d'accéder à sa console **sans passer par son système d'exploitation**. Aucun contrôle placé dans le système ne les voit. **Elles sont sur un réseau à part, souvent oublié dans les revues.**

🔭 **À RECONNAÎTRE — PAM**

**① Qu'est-ce que c'est.** *Privileged Access Management* — l'ensemble des dispositifs qui **encadrent les accès privilégiés** : ceux qui permettent de tout faire.

**② Quel problème il résout.** Sans lui, les comptes d'administration sont partagés, leurs mots de passe ne changent jamais, et **rien ne dit qui a fait quoi**. Le §27.2 décrit les composants ; le PAM est le nom de leur assemblage.

**③ Ce qu'il apporte, selon les solutions** :

| Fonction | Ce qu'elle change |
|---|---|
| **Coffre de secrets privilégiés** | Le mot de passe d'administration n'est plus connu de personne — on l'emprunte |
| **Rotation automatique** | Il change après chaque usage · un départ n'oblige plus à tout changer à la main |
| **Contrôle d'accès** | Qui peut emprunter quel accès, quand, pour quelle durée |
| **Élévation à la demande** | On n'est pas administrateur en permanence, on le devient pour une tâche |
| **Traçabilité** | Qui a emprunté quoi, et quand |
| **Enregistrement de session** | Ce qui a été fait, rejouable |

⚠️ **La quatrième ligne est la plus structurante en architecture** : elle transforme un état permanent — *cette personne est administrateur* — en un **événement daté et motivé**. C'est ce qui rend l'accès privilégié auditable.

**④ Ce que cela change dans les flux.** Un composant de plus **sur le chemin de toute administration**. Et une dépendance : le §27.4 montre qu'un point de passage unique est aussi un point de rupture — **si le PAM est indisponible, on ne peut plus administrer**.

**⑤ Le coût.** Une solution à exploiter et à sécuriser fortement — **elle détient les clés du système d'information** · une adoption difficile, parce qu'elle ajoute des étapes à des gens pressés · **des accès de secours à prévoir**, et à protéger tout autant.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a un PAM » | **Tous les accès privilégiés y passent-ils ?** Il y a presque toujours des exceptions |
| « Les mots de passe sont dans le coffre » | **Sont-ils tournés ? Quelqu'un les connaît-il encore ?** |
| « On a un compte de secours » | Légitime et nécessaire. **Où est-il ? Qui y accède ? Est-il surveillé ?** |
| « Les sessions sont enregistrées » | **Qui relit les enregistrements, et dans quel cas ?** |

⚠️ **Le compte de secours mérite l'attention** : toute solution de PAM en a un, parce qu'il faut pouvoir intervenir quand elle est en panne. **C'est le compte le plus puissant de l'organisation, et il est souvent le moins surveillé.**

📚 **À approfondir ailleurs** : c'est le sujet du volume *Identités et accès* de cette collection.

### 27.4 Les trois configurations réelles

| Configuration | Description | Fréquence |
|---|---|---|
| **Aucune séparation** | On administre depuis son poste bureautique | **Fréquente**, surtout en petite structure |
| **Rebond sans isolation** | Un point de rebond existe, mais joignable depuis le réseau bureautique | Fréquente — **protection partielle** |
| **Isolation complète** | Poste dédié, segment isolé, rebond journalisé, coffre | Minoritaire |

⚠️ **La deuxième est trompeuse.** Un point de rebond joignable depuis un poste bureautique compromis ne protège pas : **il ajoute une étape, pas une frontière**. La question à poser : *depuis quel poste peut-on l'atteindre ?*

🔥 **SCÉNARIO — le poste d'un administrateur est compromis**

| Question | Réponse |
|---|---|
| Symptôme | Un administrateur a ouvert une pièce jointe |
| Hypothèse naïve | « Un poste de plus à réinstaller » |
| Dépendance réelle | **Ce poste atteint le rebond, donc tous les serveurs** — configuration 1 ou 2 |
| Ce que le schéma aurait dû montrer | Depuis quels postes le rebond est atteignable |
| Ce qui décide de la gravité | **L'administrateur utilise-t-il le même poste pour la messagerie et l'administration ?** |

🔥 **SCÉNARIO — on ne peut plus administrer pendant l'incident**

| Question | Réponse |
|---|---|
| Symptôme | Compromission en cours. **Le rebond est dans le périmètre suspect** |
| Hypothèse naïve | « On se connecte quand même, il faut agir » |
| Dépendance réelle | **S'y connecter expose des identifiants privilégiés à l'attaquant** |
| Ce que le schéma aurait dû montrer | Un chemin d'administration de secours, hors du périmètre courant |
| Concevoir différemment | **Prévoir un accès de secours** — c'est une décision d'architecture, prise des années plus tôt |

⚠️ **Ce second scénario est celui qu'on découvre en crise**, et il n'a pas de solution improvisée. C'est le §45.4.

### 27.5 Pourquoi il n'est jamais dessiné

| Raison | Réalité |
|---|---|
| Il ne sert pas le métier | Vrai, et sans importance |
| Il alourdirait le schéma | Vrai |
| **Il révèle comment on entre partout** | **La vraie raison, souvent inavouée** — §5.5 |

⚠️ **La conséquence en lecture** : un schéma sans chemin d'administration **ne montre pas le chemin le plus court vers la compromission totale**. C'est une omission lourde de conséquences, et elle est très répandue.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On passe par le bastion » | Un rebond existe | **Depuis quel poste peut-on l'atteindre ?** |
| « Les admins ont un compte séparé » | Deux identités par personne | **Sur le même poste ? Alors la séparation est partielle** |
| « L'infogérant se connecte en VPN » | Un accès distant de prestataire | **Vers quoi ? Depuis quel poste ? Tracé comment ?** |
| « L'iLO/iDRAC est sur un autre réseau » | Interfaces de gestion matérielle isolées | **Qui peut atteindre ce réseau ?** C'est le chemin le plus puissant |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Empêcher qu'un poste bureautique compromis donne l'administration | **Un poste supplémentaire par administrateur** |
| Journaliser et tracer les actions privilégiées | Un volume de journaux et un dispositif à exploiter |
| Cloisonner les identités d'administration | Des identités et des mots de passe supplémentaires à gérer |
| Un point de passage unique | **Un point de rupture** : s'il tombe, on ne peut plus rien administrer |

🏭 **TROIS TAILLES** — Atelier Martin : aucune séparation, **et c'est un risque assumé faute de moyens** — l'unique informaticien administre depuis son poste. HELIOMED : segment dédié, deux postes, accès depuis Lyon uniquement. Novaris : rebond avec enregistrement de session, coffre de secrets, **parce que 180 personnes ont des droits d'administration et qu'une traçabilité individuelle est exigée**.

---

## Chapitre 28 — Le réseau industriel

> **Où les règles s'inversent.** Le second chapitre décisif de la partie.

### 28.1 L'inversion des priorités

| | Système de gestion | Système industriel |
|---|---|---|
| Priorité 1 | **Confidentialité** | **Disponibilité et sûreté** |
| Priorité 2 | Intégrité | Intégrité |
| Priorité 3 | Disponibilité | Confidentialité |
| Cycle de vie d'un équipement | 3 à 6 ans | **15 à 30 ans** |
| Fenêtre d'arrêt | Nuits, week-ends | **Arrêts de production planifiés à l'année** |
| Correctif | Appliqué selon un processus | **Validé par le constructeur, ou interdit** |
| Conséquence d'une erreur | Perte de données, indisponibilité | **Atteinte à la sécurité des personnes** |
| Qui décide | La direction des systèmes d'information | **La production, et parfois un organisme certificateur** |

> **Ce n'est pas que l'industriel soit « en retard ».** Ses contraintes sont différentes, et elles sont plus fortes. Un système qui pilote une machine ne peut pas redémarrer parce qu'un correctif l'exige.

⚠️ **La dernière ligne est celle qu'on oublie et qui bloque tous les projets** : modifier un système industriel peut invalider une certification, une garantie constructeur, ou une homologation de sûreté. **Ce n'est pas une question de volonté.**

### 28.2 Ce qu'on y trouve

| Composant | Ce qu'il fait | Ce qui le caractérise |
|---|---|---|
| **Automate** | Pilote une machine ou un processus | Ancien, peu de mémoire, **souvent sans authentification** |
| **Poste de supervision** | Affiche et commande | Un système ancien, **figé par le constructeur** |
| **Historisation** | Enregistre les mesures | Souvent le point de contact avec le monde de gestion |
| **Poste d'ingénierie** | Programme les automates | **Le composant le plus sensible** — il peut modifier le programme |
| **Passerelle** | Fait communiquer les deux mondes | Le point le plus exposé |

⚠️ **Le poste d'ingénierie mérite une attention particulière.** Il détient les programmes des automates, souvent les seuls exemplaires. **Sa compromission permet de modifier ce qu'une machine fait physiquement** — et sa perte peut rendre un automate impossible à reprogrammer.

### 28.3 Pourquoi l'authentification y est souvent absente

**Ce n'est pas une négligence, et c'est important à comprendre pour ne pas juger** :

| Raison | Explication |
|---|---|
| **L'ancienneté** | Un automate de 2004 ne connaît pas la notion d'authentification |
| **La sûreté** | En cas d'urgence, un opérateur doit pouvoir agir **sans délai** |
| **La disponibilité** | Un mécanisme d'authentification est un composant de plus qui peut tomber |
| **L'isolement supposé** | Le réseau était censé être séparé — et il l'était, en 2004 |

> **La sécurité de ces systèmes reposait sur l'isolement physique. C'est cet isolement qui a disparu**, pas la conception qui était mauvaise.

### 28.4 La frontière entre les deux mondes

🖼 **SCHÉMA 28.1 — Les trois modèles de frontière**

```
  MODÈLE A — séparation totale
     [ gestion ]        [ industriel ]
     Aucun lien. Les données transitent par support amovible.
     → sûr, contraignant, de moins en moins praticable
     → ⚠️ le support amovible devient lui-même le vecteur

  MODÈLE B — passerelle unidirectionnelle
     [ gestion ] ◄──── [ historisation ] ◄──── [ industriel ]
     Les données remontent, rien ne descend.
     → le modèle de référence
     → ⚠️ suppose que RIEN n'ait besoin de descendre — vérifier

  MODÈLE C — lien filtré bidirectionnel
     [ gestion ] ◄───► [ pare-feu ] ◄───► [ industriel ]
     → le plus répandu en pratique, et le plus exposé
     → ⚠️ chaque règle ajoutée réduit la séparation
```

⚠️ **Le lien du §4.6 chez HELIOMED relève du modèle C**, créé en 2018 pour un export vers le contrôle de gestion, jamais reconsidéré. **La question de lecture devant toute passerelle industrielle** : *dans quel sens circule-t-elle, et qui l'a décidé quand ?*

### 28.5 Les quatre chemins qui traversent malgré la séparation

**Même en modèle A, quatre chemins existent souvent** — et aucun n'est dessiné :

| Chemin | Pourquoi il existe | Ce qu'il permet |
|---|---|---|
| **Le poste d'ingénierie** | Il est parfois connecté aux deux mondes | Un pont direct |
| **La télémaintenance constructeur** | Contractuelle, souvent permanente | **Un accès distant d'un tiers** |
| **Le support amovible** | Transferts de programmes et de données | Le vecteur classique |
| **Le poste portable d'un intervenant** | Il se branche sur les deux réseaux, à des moments différents | Un pont différé |

⚠️ **La deuxième ligne est celle qui inquiète le plus en audit.** Une télémaintenance constructeur donne un accès distant permanent à un système de production, souvent créé il y a dix ans, rarement révisé, et **presque jamais dessiné**.

🔥 **SCÉNARIO — la production s'arrête après une mise à jour bureautique**

| Question | Réponse |
|---|---|
| Symptôme | Une ligne de production s'arrête. Aucune intervention sur le réseau industriel |
| Hypothèse naïve | « Une panne mécanique » |
| Dépendance réelle | **Le poste de supervision dépend d'un service du réseau bureautique** — annuaire, résolution, licence |
| Ce que le schéma aurait dû montrer | Les dépendances du réseau industriel **vers** le réseau de gestion |
| Concevoir différemment | Rendre le réseau industriel autonome pour ses dépendances — §26.2 |

⚠️ **C'est le scénario qui justifie la séparation mieux que n'importe quel argument de sécurité** : une dépendance non maîtrisée du monde industriel vers le monde de gestion **transforme un incident bureautique en arrêt de production**.

### 28.6 Ce qu'on peut faire, et ce qu'on ne peut pas

| Action | Sur un réseau de gestion | Sur un réseau industriel |
|---|---|---|
| **Corriger** | Selon un processus | **Validé par le constructeur, ou interdit** |
| **Installer un agent** | Oui | **Non** — ressources, garantie, certification |
| **Scanner activement** | Oui | **Non** — un balayage peut arrêter un automate |
| **Observer passivement** | Oui | **Oui** — c'est la méthode de référence |
| **Segmenter** | Oui | **Oui, et c'est la mesure principale** |
| **Journaliser** | Oui | Partiellement — beaucoup d'équipements ne produisent rien |

⚠️ **La ligne du scan actif n'est pas une précaution excessive** : certains automates anciens cessent de fonctionner face à un trafic qu'ils n'attendent pas. **C'est un cas où un outil de sécurité peut provoquer l'incident qu'il devait prévenir.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est isolé » | Le réseau industriel est séparé | **Les quatre chemins du §28.5 existent-ils ?** |
| « On ne peut pas patcher » | Le constructeur ne valide pas | **Est-ce vérifié, ou supposé ?** Parfois la validation existe |
| « Le constructeur a un accès » | Télémaintenance | **Permanent ou à la demande ? Tracé ? Depuis quand ?** |
| « On a mis une DMZ industrielle » | Une zone intermédiaire | **Quel modèle — A, B ou C ?** Le sens des flux décide de tout |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Remonter des données de production vers la gestion | **Un chemin vers le monde industriel** |
| Superviser à distance | Un accès distant à protéger particulièrement |
| Séparer totalement | Des transferts manuels, lents, **eux-mêmes risqués** |
| Rendre l'industriel autonome | Des composants dupliqués — résolution, annuaire, temps |

🏭 **TROIS TAILLES** — Atelier Martin : deux machines à commande numérique, **sur le même segment que la bureautique** — et c'est le risque le plus élevé de son architecture, non identifié comme tel. HELIOMED : segment séparé à Saint-Étienne, avec le lien de 2018. Novaris : sans objet — pas d'activité industrielle.

⚠️ **La ligne Atelier Martin est la plus instructive de tout le tableau des trois tailles.** Une petite organisation n'échappe pas à la contrainte industrielle : **elle l'ignore**. L'absence de segmentation n'est pas un arbitrage quand personne n'a posé la question.

---

### 🔬 Mini-lab 7 — Tracer les zones sur un schéma qui n'en montre aucune

**Objectif** — Reconstituer un découpage en zones à partir des seuls composants et flux.
**Durée** 35 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 24 à 28

**Le schéma fourni** — aucune zone n'est représentée :

```
   Internet ─── [ P1 ] ─── [ P2 ] ─── [ S1 ] ─── [ S2 ] ─── [ S3 ]
                              │                     │
                           [ S4 ]                [ S5 ]
                              │
                        [ 400 postes ]
                              │
                           [ S6 ] ─── [ S7 ] ─── [ automates ]

   P1 : filtre les flux entrants          S4 : annuaire
   P2 : reçoit du 443, émet du 8080       S5 : base de données
   S1 : serveur web                       S6 : poste de supervision
   S2 : serveur applicatif                S7 : passerelle
   S3 : serveur de fichiers
```

❓ **Questions**
1. Combien de zones distinguez-vous, et où passent les frontières ?
2. Quels composants sont mal placés ?
3. Que manque-t-il ?

---

**Corrigé**

**1. Cinq zones**

| Zone | Composants | Frontière |
|---|---|---|
| Extérieur | Internet | — |
| Bordure | **P1** | Entre Internet et la DMZ |
| Zone démilitarisée | **P2** | **Frontière 2 non représentée** — §25.1 |
| Interne | S1, S2, S3, S4, S5, les 400 postes | — |
| Industriel | S6, S7, automates | Aucun équipement de filtrage entre l'interne et S6 |

**2. Trois anomalies de placement**

| Anomalie | Pourquoi c'est grave |
|---|---|
| **Aucune frontière entre la DMZ et l'interne** | P2 compromis atteint directement S1, puis tout le reste — §25.2 |
| **S6 est joignable depuis le segment des 400 postes** | Un poste compromis atteint la supervision industrielle **sans traverser aucun filtre** |
| **S4 (annuaire) dans le même segment que 400 postes** | Il devrait être dans un segment serveurs distinct |

**3. Ce qui manque** — au moins six éléments :

| Manquant | Effet |
|---|---|
| **Résolution de noms** | Sans elle, aucun de ces flux |
| **Réseau d'administration** | Comment administre-t-on ces sept serveurs ? Depuis les 400 postes ? |
| Sauvegarde | Aucun composant, alors que S5 contient les données |
| Les segments internes | 400 postes et 5 serveurs dans une même zone : sont-ils dans le même segment ? |
| Les sens de flux | Aucun trait n'est fléché |
| **Le sens de la passerelle S7** | Modèle B ou C ? La réponse change tout — §28.3 |

**Les trois erreurs attendues**

1. **Compter quatre zones** en oubliant la bordure. P1 et P2 ne jouent pas le même rôle.
2. **Ne pas relever l'absence de frontière 2.** C'est l'anomalie la plus discrète du dossier, et la plus lourde : rien ne la signale, seule son absence la trahit.
3. **Traiter le lien vers S6 comme normal** parce qu'il est dessiné. Un trait indique une possibilité, pas une autorisation — §3.2.

---

> ### 🎓 À ce stade de la Partie IV, vous savez…
>
> ✓ qu'un **pare-feu entre deux zones ne protège en rien des échanges à l'intérieur** de chaque zone ;
> ✓ qu'une **segmentation contournée protège moins qu'une segmentation absente** ;
> ✓ que la zone démilitarisée se définit par sa **seconde frontière**, celle qu'on oublie de dessiner ;
> ✓ que la question à poser à un site distant est : **qu'est-ce qui survit si le lien tombe** — et que personne ne le sait, faute d'avoir essayé ;
> ✓ que le **chemin d'administration est plus puissant que ce qu'il administre**, et qu'il n'est jamais dessiné — souvent pour de mauvaises raisons ;
> ✓ qu'un **rebond joignable depuis un poste bureautique ajoute une étape, pas une frontière** ;
> ✓ que dans le monde **industriel les priorités s'inversent**, et que ce n'est pas un retard mais une contrainte plus forte ;
> ✓ qu'une **absence de segmentation n'est pas un arbitrage quand personne n'a posé la question** ;
> ✓ que le **sans-fil peut être une porte directe sur le segment interne**, et que deux réseaux annoncés ne sont pas deux segments.
>
> **Ce que vous ne savez pas encore** : ce qui circule réellement dans tout cela, par quels chemins, et pourquoi certains chemins ne sont jamais dessinés. C'est l'objet de la Partie V — le cœur du cours.

---
