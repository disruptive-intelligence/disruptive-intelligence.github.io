---
title: Chapitre 24 — Le réseau local et la segmentation
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE IV — Les réseaux et les zones
  - index.md
---

## 24.1 Le segment, unité de base

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

## 24.2 Segmenter, et jusqu'où

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

## 24.3 Le coût réel d'une segmentation, chiffré

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

## 24.4 L'accès sans fil

> **Un trou visible dans la plupart des schémas** : les postes sont dessinés — quand ils le sont — reliés par un trait, comme s'ils étaient tous câblés. La majorité ne l'est plus.

### Le chemin d'un poste sans fil

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

### La question qui structure la lecture

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

### Les réseaux multiples, et ce qu'ils ne garantissent pas

**Une même infrastructure sans fil porte généralement plusieurs réseaux annoncés** :

| Réseau | Qui s'y connecte | Où il devrait aboutir |
|---|---|---|
| **Entreprise** | Postes gérés, authentifiés individuellement | Segment interne ou segment sans fil filtré |
| **Invités** | N'importe qui, avec un code | **Internet seulement, jamais l'interne** |
| **Appareils** | Imprimantes, équipements industriels, capteurs | Un segment dédié, très restreint |
| **Personnel** | Téléphones des salariés | Souvent confondu avec « invités » — à trancher |

⚠️ **Deux réseaux annoncés séparément ne sont pas nécessairement deux segments.** C'est le §24.1 appliqué au sans-fil : **la séparation visible pour l'utilisateur ne dit rien de la séparation réseau**. La question à poser : *ces réseaux aboutissent-ils dans des segments différents, et qu'est-ce qui filtre entre eux ?*

### Les deux façons d'autoriser un poste

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

## 24.5 Trois architectures de segmentation

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
