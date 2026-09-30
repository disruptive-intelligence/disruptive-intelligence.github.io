---
title: PARTIE II — Les composants d'infrastructure
source: IT/Architecture_SI.md
note: Architecture SI
chapter: 3
chapters: 10
---

> **Format uniforme, dix chapitres courts.** Chacun répond à cinq questions, toujours dans le même ordre :
>
> **① À quoi ça sert** · **② Que se passe-t-il s'il disparaît** · **③ Que fait-il à la donnée** *(principe 6)* · **④ Comment on le reconnaît sur un schéma** · **⑤ ⚖️ Contrainte résolue et coût introduit** *(principe du coût)*
>
> **Ce que cette partie n'enseigne pas** : la configuration, les commandes, le détail des protocoles. *Principe de coupe.*

---


## Préambule — Le socle réseau minimal

> **Pourquoi ce préambule existe.** Les dix chapitres qui suivent supposent quelques notions sans lesquelles on ne peut pas répondre à la question centrale du cours : **qu'est-ce qui rend deux zones joignables ?**
>
> **Application stricte du principe de coupe** : ce qui suit tient en cinq pages. Vous n'y trouverez ni calcul d'adressage, ni protocole de routage, ni commande. Uniquement ce qui permet de comprendre pourquoi un flux passe ou ne passe pas.

### P.1 Deux niveaux d'adressage, et pourquoi il en faut deux

```
   NIVEAU LIAISON        Adresse gravée dans l'interface réseau.
                         Sert à joindre une machine SUR LE MÊME SEGMENT.
                         Ne sort jamais du segment.

   NIVEAU RÉSEAU         Adresse IP, attribuée, modifiable.
                         Sert à joindre une machine N'IMPORTE OÙ.
                         Traverse les routeurs.
```

**Pourquoi deux ?** Parce qu'ils répondent à deux questions différentes : *qui est ici, à côté de moi* et *où se trouve cette machine dans l'ensemble*.

**Ce que cela explique en lecture de schéma** :

| Observation | Explication |
|---|---|
| Un commutateur relie sans routeur | Il travaille au niveau liaison : tout est « à côté » |
| Deux machines ne se joignent pas malgré un câble commun | Elles sont dans des sous-réseaux différents |
| Un routeur est nécessaire entre deux segments | Le niveau liaison ne sort pas du segment |

### P.2 Adresse, sous-réseau, passerelle

**Trois notions, et une seule règle à retenir.**

| Notion | Ce que c'est | À quoi ça sert en lecture |
|---|---|---|
| **Adresse** | L'identifiant d'une machine sur le réseau | Elle change · elle ment · elle est réattribuée |
| **Masque de sous-réseau** | Ce qui définit **jusqu'où s'étend « à côté »** | Il découpe l'espace d'adressage en segments |
| **Passerelle par défaut** | Où envoyer ce qui n'est pas « à côté » | **Sans elle, une machine ne sort pas de son segment** |

> **La règle unique** : une machine regarde si la destination est dans son sous-réseau. **Si oui**, elle la joint directement. **Si non**, elle envoie à sa passerelle, et c'est le routeur qui prend le relais.

🖼 **SCHÉMA P.1 — La décision que prend toute machine**

```
   Machine A veut joindre une destination
                    │
        ┌───────────┴────────────┐
        │  La destination est-elle  │
        │  dans MON sous-réseau ?   │
        └───────────┬────────────┘
             ┌──────┴──────┐
            OUI            NON
             │              │
       joindre         envoyer à
      directement    LA PASSERELLE
             │              │
      commutateur      routeur, puis
      seulement        éventuellement
                       d'autres routeurs
```

⚠️ **Ce que cela explique** : une machine sans passerelle configurée fonctionne parfaitement **à l'intérieur de son segment** et ne joint rien au-delà. C'est un symptôme fréquent, et il ressemble à une panne applicative.

### P.3 Ports et état d'une connexion

| Notion | Ce qu'il faut en savoir |
|---|---|
| **Port** | Un numéro qui identifie **le service** sur une machine. L'adresse dit *où*, le port dit *quoi* |
| **Connexion** | Un échange établi entre deux couples adresse-port, avec un état : en cours d'établissement, établie, fermée |
| **Sens d'établissement** | **Qui a initié.** C'est ce qui distingue un flux entrant d'un flux sortant |

> **La notion la plus utile du préambule** : un pare-feu qui autorise un flux **sortant** laisse revenir les réponses de ce flux, parce qu'il **suit l'état des connexions**. C'est pourquoi *« autoriser vers Internet »* ne signifie pas *« autoriser depuis Internet »*.

⚠️ **Ce que cela change en lecture** : sur un schéma, une flèche sans sens est ambiguë — §3.2. **Le sens d'établissement est l'information la plus déterminante d'un flux**, et c'est celle qui manque le plus souvent.

### P.4 Traduction d'adresses

**Un mécanisme omniprésent dans les architectures réelles, et quasi absent des schémas.**

**Le problème qu'il résout** : les adresses employées à l'intérieur d'une organisation ne sont pas utilisables directement sur Internet. Il faut donc les traduire au passage.

🖼 **SCHÉMA P.2 — Les deux traductions**

```
  SORTANTE — plusieurs machines internes derrière une adresse publique

     10.0.4.23 ──┐
     10.0.4.24 ──┼──► [ traduction ] ──► 203.0.113.7 ──► Internet
     10.0.4.25 ──┘
     → Vu de l'extérieur, les trois machines ont LA MÊME adresse.

  ENTRANTE — une adresse publique redirigée vers une machine interne

     Internet ──► 203.0.113.7:443 ──► [ traduction ] ──► 10.0.4.80:8443
     → C'est ainsi qu'un service interne devient joignable de l'extérieur.
```

**Les quatre conséquences en lecture**, et elles comptent toutes :

| Conséquence | Où elle se manifeste |
|---|---|
| **L'adresse observée n'est pas celle de la machine d'origine** | Journaux d'un serveur derrière une traduction · investigation |
| Plusieurs machines partagent une adresse vue de l'extérieur | Blocage d'une adresse : on bloque tout le monde |
| Un service exposé n'est pas à l'adresse qu'on croit | Publication, pare-feu |
| **Un composant intermédiaire peut aussi masquer l'origine** | Mandataire inverse, répartiteur de charge — §34.1 |

⚠️ **La première ligne est la plus lourde de conséquences.** Elle explique pourquoi corréler un journal applicatif avec un utilisateur réel est difficile — §34.1 — et pourquoi une adresse dans un journal n'identifie pas une machine sans information complémentaire.

### P.5 Deux familles d'adressage

📌 **Ce qu'il faut savoir, et rien de plus** :

| | **IPv4** | **IPv6** |
|---|---|---|
| Espace d'adressage | Limité — d'où la traduction d'adresses | Très vaste |
| Traduction d'adresses | **Structurante** : la quasi-totalité des réseaux internes en dépend | **Généralement inutile** — les machines peuvent avoir une adresse routable |
| Conséquence en lecture | L'adresse observée n'est souvent pas l'origine | **L'adresse observée peut être celle de la machine** |
| Présence | Partout | Croissante, souvent en parallèle du premier |

⚠️ **Pourquoi cela figure dans ce cours** : le modèle mental *« adresse interne + traduction »* que nous employons dans tout le volume **n'est pas universel**. Une machine peut disposer simultanément des deux familles — c'est la double pile — et suivre alors **deux chemins différents selon la famille employée**.

**La question de lecture qui en découle** : *ce schéma décrit-il un adressage, ou les deux ?* Dans la majorité des schémas, la question n'est pas tranchée — et un flux peut passer dans une famille et être bloqué dans l'autre.

### P.6 Ce que ce préambule permet de faire

☐ Expliquer pourquoi deux machines d'un même segment se joignent sans routeur
☐ Expliquer pourquoi une machine sans passerelle ne sort pas de son segment
☐ Distinguer le sens d'établissement d'un flux, et savoir pourquoi il détermine tout
☐ Comprendre pourquoi une adresse dans un journal n'identifie pas une machine
☐ Savoir qu'un service exposé n'est pas nécessairement à l'adresse annoncée
☐ Savoir que le modèle « adresse interne + traduction » n'est pas universel

**Ce qu'il ne permet pas, volontairement** : dimensionner un plan d'adressage, choisir un protocole de routage, configurer quoi que ce soit — *principe de coupe*.

---

### Chapitre 8 — Le commutateur

#### 8.1 À quoi ça sert

Relier des machines à l'intérieur d'un même segment, et acheminer les échanges de l'une à l'autre **sans les diffuser à toutes**.

**Pourquoi ça existe.** Avant le commutateur, les machines partageaient un même support : chacune voyait tout ce qui passait, et deux machines qui émettaient en même temps se gênaient. Le commutateur résout les deux problèmes d'un coup — il apprend quelle machine est derrière quel port, et n'envoie qu'à la bonne.

**Ce qu'il faut en retenir pour raisonner**, et rien de plus :

> **Un commutateur crée un espace où les machines se joignent directement. Il ne crée aucune frontière de filtrage.**

#### 8.2 Comment il fonctionne, juste assez pour raisonner

```
   ①  Une trame arrive sur le port 3
   ②  Le commutateur note : « cette machine est derrière le port 3 »
   ③  Il regarde la destination
        ├── il sait où elle est  ──► il envoie sur ce port UNIQUEMENT
        └── il ne sait pas       ──► il envoie sur TOUS les ports
   ④  La réponse lui apprend où se trouve la destination
```

**Trois conséquences en lecture d'architecture** :

| Mécanisme | Conséquence |
|---|---|
| Il **apprend** les emplacements | Une machine déplacée est retrouvée automatiquement |
| Il **diffuse** ce qu'il ne connaît pas | Un segment très large produit du trafic inutile partout |
| Il **ne filtre pas** | Deux machines du même segment se joignent, sauf mécanisme dédié — §24.1 |

#### 8.3 Les segments logiques

**Le mécanisme qui change tout, et qu'aucun schéma logique ne montre** : un même commutateur physique peut porter plusieurs segments logiques indépendants. Deux machines branchées côte à côte dans la même baie peuvent être **aussi séparées que si elles étaient dans deux bâtiments**.

```
   UN SEUL COMMUTATEUR PHYSIQUE

   ports 1-8    ─── segment « postes »      ┐
   ports 9-16   ─── segment « serveurs »    ├─ trois segments,
   ports 17-24  ─── segment « supervision » ┘  aucun ne voit les autres

   Pour qu'ils communiquent : il faut un ROUTEUR.
```

⚠️ **Ce que cela impose en lecture** : un schéma physique qui montre un seul commutateur peut décrire une architecture **logiquement segmentée**. Et l'inverse : deux commutateurs dessinés séparément peuvent porter **le même segment**. **La question à poser : combien de segments, et non combien d'équipements.**

#### 8.4 Trois architectures, trois usages

```
  A — COMMUTATEUR UNIQUE
      [ commutateur ] ─── 20 machines
      → simple · une panne = tout le site
      → convient quand l'interruption tolérable est large

  B — DEUX COMMUTATEURS EN CASCADE
      [ cœur ] ─── [ étage 1 ]
              └─── [ étage 2 ]
      → une panne d'étage n'affecte qu'un étage
      → une panne du cœur affecte tout · le cœur est le point de rupture

  C — CŒUR REDONDÉ
      [ cœur A ] ══╗
                   ╠═══ [ étage 1 ] [ étage 2 ]
      [ cœur B ] ══╝
      → une panne de cœur est absorbée
      → deux équipements à configurer de façon cohérente
      → ⚠️ **Principe de preuve** : sont-ils sur la même alimentation ?
```

**La contrainte qui fait passer de A à C** n'est pas le nombre de machines : c'est **la durée d'interruption tolérable comparée au délai de remplacement d'un équipement**. Si remplacer prend quatre heures et qu'une journée d'arrêt est acceptable, A suffit.

#### 8.5 Ce qu'il fait à la donnée

Il la transporte. Pour accomplir sa fonction, il interprète les informations d'adressage de niveau liaison — **sans avoir besoin d'interpréter le contenu applicatif**. Il voit passer ce qui traverse le segment, ce qui en fait un point d'observation possible — chapitre 43.

#### 8.6 S'il disparaît

| Ce qui tombe | Délai | Compréhensible pour l'utilisateur ? |
|---|---|---|
| Tout ce qui y est raccordé | Immédiat | ✅ « plus de réseau ici » |

**C'est la panne la plus localisée et la plus totale du cours** : un segment entier disparaît, et le reste du système ne s'en aperçoit pas — **sauf s'il en dépend**.

🔥 **SCÉNARIO — le commutateur de l'étage tombe**

| Question | Réponse |
|---|---|
| Symptôme observé | Quarante personnes sans réseau, le reste du site fonctionne |
| Hypothèse naïve | « Panne réseau générale » |
| Dépendance réelle | Ces quarante postes · **et tout service hébergé sur ce segment** |
| Ce que le schéma aurait dû montrer | Quels serveurs sont sur ce segment |
| Concevoir différemment | Ne pas mélanger postes et serveurs sur un même segment |

#### 8.7 Sur un schéma

Souvent absent. Quand il figure, c'est sur une vue physique. Sur une vue logique, il est **implicite** : deux machines dessinées dans la même zone sont supposées reliées.

⚠️ **Le piège de lecture** : l'absence de commutateur ne signifie pas qu'il n'y en a pas — elle signifie que la vue ne s'y intéresse pas. **La question « qui peut joindre qui à l'intérieur d'une zone » reste ouverte**, et la réponse par défaut est « tout le monde ».

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut probablement dire | À vérifier avant de le croire |
|---|---|---|
| « C'est sur le même switch » | Les machines sont sur le même segment | **Même équipement ≠ même segment.** Combien de segments logiques ? |
| « On a mis un VLAN » | Un segment logique a été créé | Le routage entre segments est-il filtré, ou juste routé ? |
| « Le cœur de réseau » | Le commutateur central | Est-il redondé ? Les deux exemplaires partagent-ils l'alimentation ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Relier des machines proches efficacement | Un équipement à alimenter, corriger, surveiller |
| Segmenter logiquement sans recâbler | **Une configuration à maintenir, souvent non documentée** |
| Redonder le cœur | Deux configurations à tenir cohérentes · un mécanisme de bascule à tester — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : 2, dont un pour l'atelier. HELIOMED : une trentaine, dont deux en cœur redondé. Novaris : plusieurs centaines. **La contrainte qui fait passer de 2 à 30 n'est pas le nombre de salariés, c'est le nombre de bâtiments et de segments à isoler.**

---

### Chapitre 9 — Le routeur

#### 9.1 À quoi ça sert

Faire communiquer des segments différents. Sans lui, deux segments coexistent sans se voir.

**Pourquoi ça existe.** Le niveau liaison ne sort pas du segment — §P.1. Dès qu'on découpe un réseau en plusieurs segments, il faut un composant capable de faire passer un échange de l'un à l'autre : c'est le routeur.

> **La formule qui distingue routeur et pare-feu, et qu'il faut retenir** :
> **Le routeur dit *où* ça va. Le pare-feu dit *si* ça a le droit.**

#### 9.2 Comment il fonctionne, juste assez pour raisonner

```
   ①  Un paquet arrive, avec une adresse de destination
   ②  Le routeur consulte sa table :
         « pour atteindre 10.0.7.0/24, envoyer vers l'interface 2 »
   ③  Il modifie certains champs de transit
   ④  Il transmet
   ⑤  Le routeur suivant recommence
```

**Ce qui compte en architecture, et rien de plus** :

| Notion | Pourquoi elle compte en lecture |
|---|---|
| **Table de routage** | Elle décide du chemin. **Une entrée manquante rend une zone injoignable sans qu'aucun filtre ne l'interdise** |
| **Route par défaut** | Où va ce qui n'est pas connu. Généralement vers Internet |
| **Chemin asymétrique** | L'aller et le retour peuvent emprunter des routes différentes — **c'est ce qui casse certains pare-feu à état** |

⚠️ **La troisième ligne explique une famille entière d'incidents.** Un pare-feu qui suit l'état des connexions doit voir l'aller **et** le retour. Si le retour passe ailleurs, il refuse un trafic pourtant légitime — et le diagnostic est difficile parce que la configuration paraît correcte.

🔭 **À RECONNAÎTRE — BGP**

**① Qu'est-ce que c'est.** Un protocole qui permet à des systèmes de routage indépendants d'**échanger des informations de joignabilité** et d'appliquer des **politiques** sur les chemins retenus.

**② Quel problème il résout.** À grande échelle, on ne maintient pas à la main *« pour joindre ce réseau, passer par ce routeur »*. Et surtout : quand plusieurs chemins existent, **il faut pouvoir choisir selon d'autres critères que la distance** — un contrat, un coût, une préférence, une politique.

**③ Où on le rencontre.**

```
                    Entreprise
                        │
              ┌─────────┴─────────┐
              │                   │
          [ FAI A ]           [ FAI B ]
              │                   │
              └──── Internet ─────┘
```

| Contexte | Pourquoi BGP apparaît |
|---|---|
| **Deux fournisseurs d'accès** | Annoncer ses adresses aux deux, et choisir par où sortir et entrer |
| Interconnexion avec un opérateur | Échanger les réseaux joignables de part et d'autre |
| Grands centres de données | Routage interne à grande échelle |
| Liaison privée vers un fournisseur cloud | L'échange de routes se fait fréquemment ainsi |

**④ Ce que cela change.** Le chemin **n'est plus déterminé par votre seule configuration** : il résulte d'un échange avec des systèmes que vous ne contrôlez pas. Une annonce mal formée peut rendre une plage d'adresses injoignable — ou détourner du trafic.

> ⚠️ **Le point qui compte en architecture** : *BGP ne demande pas simplement quel chemin est le plus court. Les politiques comptent, et elles sont décidées de part et d'autre.*

**⑤ Le coût.** Une compétence rare · une configuration dont une erreur a des effets externes visibles · **une dépendance à ce que le partenaire annonce**.

**⑥ Le vocabulaire à reconnaître** : **ASN** — le numéro qui identifie un système autonome · **préfixe** — une plage d'adresses annoncée · **annonce de route** · **peering** — l'accord d'échange entre deux systèmes.

🗣 **En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est en BGP avec les deux opérateurs » | **Multi-hébergement.** Que se passe-t-il si l'un tombe ? La bascule a-t-elle été testée ? |
| « On annonce notre préfixe » | Vos adresses sont visibles depuis Internet par ce chemin. **Qui peut modifier cette annonce ?** |
| « Ils ne nous annoncent plus la route » | Une destination est devenue injoignable **sans qu'aucun équipement ne soit en panne** |

📚 **À approfondir ailleurs** : les attributs de sélection de chemin, la sécurisation des annonces, la conception d'un routage de centre de données.

#### 9.3 Trois architectures de routage

```
  A — ROUTEUR UNIQUE, ROUTE PAR DÉFAUT
      segments internes ──► [ routeur ] ──► Internet
      → simple · tout passe par un point · un point de rupture

  B — ROUTAGE INTERNE + SORTIE SÉPARÉE
      segments ──► [ routeur interne ] ──► [ pare-feu ] ──► Internet
      → le routage interne survit à une panne de la sortie
      → deux équipements, deux configurations

  C — MULTI-SITES
      site A ──► [ routeur A ] ══lien══ [ routeur B ] ◄── site B
                       └────► Internet          └────► Internet
      → chaque site sort localement, et joint l'autre par le lien
      → si le lien tombe, chaque site reste autonome pour Internet
      → mais pas pour les services hébergés dans l'autre site — §26
```

**La contrainte qui décide entre B et C** : *un site doit-il continuer à fonctionner si le lien vers le siège tombe ?* — et la réponse est presque toujours partielle, §26.1.

#### 9.4 Ce qu'il fait à la donnée

Il l'achemine. Pour décider du chemin, il interprète les informations d'adressage réseau, et il modifie certains champs au passage — c'est le mécanisme normal du transit. **Il n'a pas besoin d'interpréter le contenu applicatif**, ce qui en fait un point de contrôle sur les trajets, pas sur les contenus.

#### 9.5 S'il disparaît

Les segments deviennent des îlots. Chacun fonctionne, aucun ne se parle.

🔥 **SCÉNARIO — le routeur inter-sites tombe**

| Question | Réponse |
|---|---|
| Symptôme | Les postes de Nantes n'atteignent plus les serveurs de Lyon. Internet fonctionne à Nantes |
| Hypothèse naïve | « Les serveurs de Lyon sont tombés » |
| Dépendance réelle | Le lien · **et tout ce qui est centralisé à Lyon** : annuaire, applications, fichiers |
| Ce que le schéma aurait dû montrer | **Ce qui est local à Nantes, et ce qui ne l'est pas** — §26.2 |
| Concevoir différemment | Un contrôleur d'annuaire et une résolution de noms locaux |

⚠️ **C'est une panne qui *ressemble* à une panne applicative** : les machines répondent, mais pas à travers les segments. C'est l'un des cas où le diagnostic est le plus souvent orienté au mauvais endroit.

#### 9.6 Sur un schéma

Représenté à la jonction de deux zones ou de deux sites. **Souvent fusionné avec le pare-feu** dans les petites organisations — un seul boîtier fait les deux, ce que le schéma ne dit pas.

⚠️ **Ce que cette fusion masque** : la question *« ce flux est-il permis, ou seulement possible ? »* — §3.2. Quand routeur et pare-feu sont un seul objet sur le schéma, on ne sait pas si un flux passe parce qu'il est autorisé ou parce que personne n'a écrit de règle.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est routé » | Un chemin existe entre les deux | **Routé ne veut pas dire autorisé.** Y a-t-il un filtre sur ce chemin ? |
| « Il n'y a pas de route » | La table ne connaît pas la destination | Est-ce un oubli, ou une décision ? |
| « Ça passe par le WAN » | Le trafic emprunte le lien inter-sites | Quelle latence ? Que se passe-t-il si le lien tombe ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Faire communiquer des segments séparés | Un point de passage supplémentaire à sécuriser |
| Choisir des chemins, en gérer plusieurs | Une configuration de routage à maintenir · **un diagnostic plus difficile** |
| Sortir localement par site | Autant de sorties à surveiller — §11 |

---

### Chapitre 10 — Le pare-feu

> **Le composant le plus dessiné du cours, et celui dont le schéma dit le moins.**

#### 10.1 À quoi ça sert

Autoriser ou refuser un flux entre deux zones, selon des règles.

**Pourquoi ça existe.** Un routeur fait passer tout ce qui est routable. Dès qu'on veut que certaines choses passent et d'autres non, il faut un composant qui décide — et qui garde une trace de sa décision.

#### 10.2 Comment il fonctionne, juste assez pour raisonner

**Trois générations coexistent**, et elles ne voient pas la même chose :

| Génération | Ce qu'elle examine | Ce qu'elle ne voit pas |
|---|---|---|
| **Filtrage simple** | Adresses, ports, sens | Si le flux correspond vraiment au service annoncé |
| **Suivi d'état** | Les mêmes, **plus l'état de la connexion** | Le contenu |
| **Inspection applicative** | Le contenu, si le flux n'est pas chiffré **ou s'il est déchiffré** | Ce qui reste chiffré de bout en bout |

> **La notion la plus utile : le suivi d'état.** Un pare-feu qui suit l'état sait qu'une réponse appartient à une connexion qu'il a déjà autorisée. **C'est pourquoi autoriser un flux sortant ne signifie pas autoriser un flux entrant** — §P.3.

🖼 **SCHÉMA 10.1 — Ce que le suivi d'état change**

```
  SANS SUIVI D'ÉTAT
     règle 1 : autoriser interne → Internet, port 443
     règle 2 : autoriser Internet → interne, ports 1024-65535
                                    ▲
                        il faut ouvrir le retour EN GRAND

  AVEC SUIVI D'ÉTAT
     règle 1 : autoriser interne → Internet, port 443
     (les réponses reviennent automatiquement)
                                    ▲
                        aucune règle entrante nécessaire
```

⚠️ **Ce que cela explique en lecture** : un jeu de règles qui autorise de larges plages entrantes signale souvent un équipement ancien, ou une configuration héritée d'une époque où le suivi d'état n'existait pas. **C'est un signe de strate** — §4.2.

#### 10.3 Le même composant, trois placements différents

**C'est en variant le placement qu'on comprend la fonction.**

```
  A — PARE-FEU UNIQUE, EN COUPURE
      Internet ──► [ FW ] ──► serveur
      → une seule frontière · le serveur est derrière un filtre
      → contourné ou compromis : plus rien ne protège

  B — DEUX PARE-FEU, ZONE INTERMÉDIAIRE
      Internet ──► [ FW-1 ] ──► DMZ ──► [ FW-2 ] ──► interne
      → deux frontières · un composant compromis en DMZ ne suffit pas
      → deux jeux de règles à maintenir, souvent deux constructeurs

  C — SERVICE EN LIGNE ET LIEN PRIVÉ
      Internet ──► [ service du fournisseur ]
                            │  lien privé
                            ▼
                     [ réseau interne ]
      → la frontière côté Internet ne vous appartient plus
      → le pare-feu ne protège plus que le lien privé
```

| Placement | Ce que le pare-feu protège | Ce qu'il ne protège pas |
|---|---|---|
| **A** | Le serveur, contre l'extérieur | Rien à l'intérieur · rien s'il est contourné |
| **B** | L'interne, même si la DMZ tombe | Les échanges au sein de chaque zone |
| **C** | Le lien privé | **Tout ce qui se passe côté fournisseur** |

**Les six questions à poser devant tout pare-feu sur un schéma** :

```
1. Quelle frontière matérialise-t-il exactement ?
2. Qu'est-ce qui le contourne ? (un lien direct, une machine à deux interfaces)
3. Combien de règles, et depuis quand ont-elles été revues ?
4. Qui l'administre, et depuis où ?  ← §27
5. Que se passe-t-il s'il tombe ?
6. Que signifie « paire redondée » ici ?  ← §10.5
```

⚠️ **La question 3 est celle qui révèle le plus.** Un pare-feu dont les règles n'ont pas été revues depuis six ans autorise probablement des flux dont personne ne connaît plus l'usage. **Une règle ne se supprime jamais spontanément** — chaque projet en ajoute, aucun n'en retire.

#### 10.4 Ce qu'il fait à la donnée

Selon sa génération : il regarde les extrémités et les ports, ou il inspecte le contenu applicatif, ou il déchiffre pour inspecter — auquel cas **il voit tout en clair**, ce qui en fait un actif extrêmement sensible.

#### 10.5 « Paire redondée » : ce que cela signifie réellement

**Deux pare-feu côte à côte sur un schéma peuvent décrire trois choses différentes.**

| Mode | Comportement | Ce que ça protège |
|---|---|---|
| **Actif / passif** | Le second attend. Il prend le relais si le premier tombe | Une panne matérielle · **pas une erreur de configuration, qui est répliquée** |
| **Actif / actif** | Les deux traitent du trafic | Une panne matérielle, et la charge |
| **En série** | Deux barrières successives, souvent de constructeurs différents | Une faille propre à un constructeur |

⚠️ **Principe de preuve, appliqué au pare-feu** — ce qu'une paire ne protège pas :

| Ce qui reste partagé | Conséquence |
|---|---|
| **La configuration** | Une règle erronée est répliquée sur les deux |
| **La version logicielle** | Une vulnérabilité les affecte tous les deux |
| **L'alimentation, la baie, le site** | Un incident physique les emporte ensemble |
| **L'administrateur** | Une erreur humaine s'applique aux deux |

> **Une paire redondée protège contre la panne d'un équipement. Elle ne protège contre à peu près rien d'autre.**

#### 10.6 S'il disparaît

**Trois cas opposés, et c'est ce qui rend ce composant intéressant** :

| Configuration | S'il tombe | Ce que ça révèle |
|---|---|---|
| En coupure, sans contournement | **Plus rien ne passe.** Le service s'arrête | La frontière était réelle |
| En redondance | Le second prend le relais | Si la bascule fonctionne — *principe de preuve* |
| **Contourné par un chemin oublié** | **Rien ne change** | **La frontière était fictive** |

🔥 **SCÉNARIO — le pare-feu tombe et rien ne se passe**

| Question | Réponse |
|---|---|
| Symptôme | Un pare-feu est arrêté pour maintenance. **Aucun utilisateur ne signale quoi que ce soit** |
| Hypothèse naïve | « La bascule a fonctionné » |
| Dépendance réelle | **Peut-être aucune** : le trafic passait peut-être déjà ailleurs |
| Ce que le schéma aurait dû montrer | Tous les chemins entre les deux zones, pas seulement celui-ci |
| Ce qu'il faut vérifier | Le compteur de sessions du pare-feu passif : **a-t-il vraiment repris le trafic ?** |

⚠️ **C'est l'un des tests les plus instructifs qu'on puisse faire sur une architecture** : arrêter un composant en fenêtre planifiée et regarder si quelque chose change. Quand rien ne change, ce n'est pas toujours une bonne nouvelle.

#### 10.7 Sur un schéma

Presque toujours dessiné, presque toujours à une frontière. **Deux pare-feu côte à côte** signalent une redondance ; **deux pare-feu en série** signalent une double barrière.

⚠️ **Le piège de lecture le plus fréquent du cours** : un pare-feu dessiné ne dit rien de ses règles. Une frontière peut être matérialisée par un équipement dont la règle est *« tout autoriser »*.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans la DMZ » | Le composant est publié | **Y a-t-il une seconde frontière ?** — §25.1 |
| « On a une paire HA » | Deux pare-feu redondés | Actif/passif ou actif/actif ? La bascule a-t-elle été testée ? |
| « Le flux est ouvert » | Une règle autorise ce trafic | Dans quel sens ? Depuis quand ? Qui l'a demandée ? |
| « On va mettre une règle any-any en attendant » | Autoriser tout, temporairement | **« En attendant » dure en moyenne plusieurs années** — §4.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Contrôler ce qui traverse une frontière | **Un ensemble de règles qui ne fait que croître** |
| Tracer les flux refusés | Un volume de journaux considérable |
| Inspecter le contenu | Une latence · un déchiffrement à opérer · **un point où tout passe en clair** |
| Redonder | Deux équipements, et une bascule à tester — *principe de preuve* |

🏭 **TROIS TAILLES** — Atelier Martin : un boîtier tout-en-un qui fait routeur, pare-feu et accès distant. HELIOMED : deux en redondance. Novaris : plusieurs dizaines. **La contrainte qui les multiplie est le nombre de frontières à contrôler, pas la taille.**

---

### Chapitre 11 — Le mandataire sortant

#### 11.1 À quoi ça sert

Concentrer les accès des postes internes vers l'extérieur, en un point unique où l'on peut filtrer, journaliser et authentifier.

**Pourquoi ça existe.** Sans lui, six cents postes sortent chacun de leur côté à travers le pare-feu. On peut filtrer par adresse et par port — mais pas savoir *quel site* a été consulté, ni *par qui*, ni bloquer une catégorie de destinations. Le mandataire déplace le point de décision du niveau réseau au niveau applicatif.

#### 11.2 Comment il fonctionne, juste assez pour raisonner

```
   SANS MANDATAIRE
      poste ──────────────────────► Internet
      Le pare-feu voit : une adresse interne, une adresse externe, un port.

   AVEC MANDATAIRE
      poste ──► [ mandataire ] ──► Internet
                      │
                      ├── il connaît L'UTILISATEUR (authentification)
                      ├── il connaît LA DESTINATION demandée
                      ├── il peut refuser selon une catégorie
                      └── il journalise les deux
```

**Deux modes de mise en œuvre**, et ils ne produisent pas le même résultat :

| Mode | Comment | Ce qui change |
|---|---|---|
| **Déclaré** | Le poste est configuré pour l'utiliser | **Contournable** : un logiciel qui ignore la configuration sort directement, si le pare-feu le permet |
| **Imposé** | Le trafic est redirigé sans que le poste le sache | Non contournable, mais certains protocoles s'en accommodent mal |

⚠️ **La différence est décisive en lecture.** Un mandataire déclaré protège les usages **coopératifs**. Il ne protège pas contre un logiciel malveillant, qui n'a aucune raison de respecter la configuration du navigateur. **La question à poser : le pare-feu autorise-t-il une sortie directe, ou tout doit-il passer par le mandataire ?**

#### 11.3 Deux architectures de sortie

```
  A — SORTIE CENTRALISÉE
      postes site A ──┐
      postes site B ──┼──► [ mandataire siège ] ──► Internet
      postes site C ──┘
      → un point de contrôle et de journalisation unique
      → un point de rupture pour tout accès Internet
      → depuis un site distant : le trafic remonte au siège, latence
      → si le lien inter-sites tombe : plus d'Internet sur le site

  B — SORTIE LOCALE PAR SITE
      postes site A ──► [ mandataire local ] ──► Internet
      postes site B ──► [ mandataire local ] ──► Internet
      → moins de latence, pas de dépendance au lien inter-sites
      → autant de points de contrôle à maintenir et à surveiller
      → journalisation répartie : la corréler devient un travail
```

**La contrainte qui décide** : *le site doit-il continuer à accéder à Internet si le lien vers le siège tombe ?*

⚠️ **Un troisième cas, de plus en plus fréquent** : les postes nomades. **Hors des murs, ils ne passent par aucun mandataire** — sauf si un tunnel les y ramène. Une organisation avec un tiers de postes nomades a donc, en pratique, **deux politiques de sortie différentes** : une pour les postes internes, une pour les nomades. Le schéma n'en montre qu'une.

#### 11.4 Ce qu'il fait à la donnée

Il voit **toutes les destinations** consultées depuis l'organisation, et selon sa configuration, le contenu. C'est une source de journaux particulièrement riche sur le comportement des postes — chapitre 34.

📌 **Et c'est un point sensible en soi** : le journal d'un mandataire contient l'historique de navigation de chaque salarié, nominativement. Sa conservation et son accès relèvent d'obligations qui dépassent le cadre de ce cours.

#### 11.5 S'il disparaît

**Plus aucun poste n'accède à Internet** — alors que le réseau fonctionne parfaitement.

🔥 **SCÉNARIO — « j'ai du réseau mais pas Internet »**

| Question | Réponse |
|---|---|
| Symptôme | Les postes joignent les serveurs internes. Aucun site externe ne s'ouvre |
| Hypothèse naïve | « Le lien Internet est coupé » |
| Dépendance réelle | Le mandataire · **et la résolution de noms, si elle est faite par lui** |
| Ce que le schéma aurait dû montrer | Que la sortie Internet est **applicative**, pas seulement réseau |
| Comment vérifier en trente secondes | Depuis un poste : tenter une connexion directe vers une adresse externe. Si elle passe, le réseau va bien |

⚠️ **C'est l'une des pannes les plus déroutantes pour un utilisateur**, parce que tous les symptômes qu'il connaît — « le réseau » — sont normaux.

#### 11.6 Sur un schéma

Entre le réseau interne et la bordure. **Souvent absent des schémas centrés sur les serveurs**, parce qu'il concerne les postes — chapitre 6.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça sort par le proxy » | Le flux passe par le mandataire sortant | Déclaré ou imposé ? **Une sortie directe est-elle possible ?** |
| « Il faut l'autoriser dans le proxy » | Ajouter une destination à la liste | Qui décide ? Combien d'exceptions existent déjà ? |
| « On a bypassé le proxy pour ce serveur » | Une exception a été créée | **Depuis quand ? Est-elle encore justifiée ?** — §4.3 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Contrôler et tracer les accès sortants | **Un point de rupture pour tout accès Internet** |
| Filtrer les destinations | Une liste à maintenir · des faux blocages · **des contournements si trop strict** |
| Authentifier les accès sortants | Une dépendance à l'annuaire |
| Journaliser la navigation | Un volume important, et des données nominatives à encadrer |

⚠️ **La ligne du filtrage illustre le principe du coût** : filtrer les destinations résout une contrainte réelle, et produit des contournements si le filtrage devient pénible — quelqu'un finira par ouvrir un accès direct « pour tester ». **Ajouter n'est jamais gratuit.**

🏭 **TROIS TAILLES** — Atelier Martin : **aucun mandataire**, sortie directe filtrée par le boîtier tout-en-un. HELIOMED : un mandataire au siège, sortie centralisée. Novaris : sortie locale par site, **parce que quarante sites qui remontent leur trafic au siège saturent les liens et ajoutent une latence inacceptable**.

---

### Chapitre 12 — Le mandataire inverse

> **Le composant que ce cours voit le plus souvent mal compris**, et celui dont le nom trompe le plus.

#### 12.1 À quoi ça sert

Recevoir les demandes venues de l'extérieur **à la place** des serveurs internes, et les relayer. L'extérieur ne parle jamais au serveur : il parle au mandataire.

🖼 **SCHÉMA 12.1 — Ce que le mandataire inverse change**

```
  SANS                Internet ──────────────► [ serveur web ]
                      Le serveur est joignable directement.
                      Son adresse est publique. Sa version est visible.
                      Une faille du serveur est directement exploitable.

  AVEC                Internet ──► [ mandataire ] ──► [ serveur web ]
                      Le serveur n'est joignable que par le mandataire.
                      L'extérieur ne connaît que l'adresse du mandataire.
                      Une faille du serveur exige d'abord de passer le mandataire.
```

#### 12.2 Les quatre fonctions qu'il assure réellement

**On croit qu'il en a une. Il en a quatre, et elles s'ajoutent progressivement dans une architecture.**

| # | Fonction | Ce qu'elle apporte | Quand elle apparaît |
|---|---|---|---|
| **1** | **Masquer** | Le serveur n'est pas exposé directement | Dès qu'un service est publié |
| **2** | **Terminer le chiffrement** | Un seul point où gérer les certificats | Dès qu'il y a plus d'un serveur |
| **3** | **Authentifier** | On prouve son identité **avant** d'atteindre l'application | **Souvent sa vraie raison d'être** |
| **4** | **Router selon le contenu** | Un même point d'entrée pour plusieurs applications | Quand les applications se multiplient |

⚠️ **La fonction 3 est celle qu'on oublie et qui compte le plus.** Placer l'authentification devant l'application signifie qu'une faille de l'application **n'est pas atteignable par un anonyme**. C'est un changement de nature, pas un raffinement.

#### 12.3 Ce qu'il fait à la donnée

Cela dépend du mode de terminaison retenu. **Dans le modèle employé dans ce cours, le mandataire termine le chiffrement** : il lit le contenu, parfois le modifie — en-têtes, cache, compression — et le rechiffre ou non vers le serveur. **C'est alors un point où le contenu est en clair**, donc un point d'observation et un point de risque.

⚠️ **Ce n'est pas une propriété obligatoire d'un mandataire inverse.** Un mandataire peut relayer un flux chiffré sans le terminer ; il ne voit alors que les extrémités.

🖼 **SCHÉMA 12.2 — Les trois modes de terminaison du chiffrement**

```
  A — TERMINAISON AU SERVEUR  (« passthrough »)
      client ══chiffré══════════════════════════► serveur
      Le mandataire relaie sans ouvrir.
      → aucune inspection possible · aucun contrôle applicatif
      → aucune authentification préalable possible
      → le certificat est géré sur chaque serveur

  B — TERMINAISON AU MANDATAIRE, PUIS CLAIR
      client ══chiffré══► [ mandataire ] ──clair──► serveur
      → inspection et authentification possibles
      → le trafic interne circule en clair
      → un seul certificat à gérer

  C — TERMINAISON PUIS RECHIFFREMENT
      client ══chiffré══► [ mandataire ] ══chiffré══► serveur
      → inspection ET trafic interne protégé
      → deux jeux de certificats à gérer
      → charge de chiffrement doublée
```

| Mode | Voit le contenu | Trafic interne protégé | Authentification possible | Coût |
|---|---|---|---|---|
| **A** | ❌ | ✅ | ❌ | Certificats sur chaque serveur |
| **B** | ✅ | ❌ | ✅ | Le plus simple, et le plus courant |
| **C** | ✅ | ✅ | ✅ | Deux gestions de certificats, charge doublée |

**Ce que le mode change en lecture** : la question *« qui voit le contenu en clair ? »* n'a pas la même réponse selon les trois — et **aucun schéma ne le dit**. C'est une question à poser.

⚠️ **La conséquence en sécurité, souvent mal comprise** : en mode B, le trafic entre le mandataire et le serveur est en clair **sur votre réseau interne**. Ce n'est un problème que si ce réseau n'est pas maîtrisé — c'est un arbitrage, pas une faute.

🔭 **À RECONNAÎTRE — WAF**

**① Qu'est-ce que c'est.** Un dispositif qui **analyse et filtre le trafic web applicatif** selon des règles de sécurité — contenu des requêtes, paramètres, en-têtes.

**② Quel problème il résout.** Un pare-feu réseau décide si un flux passe ; il ne regarde pas *ce que la requête demande*. Un mandataire inverse relaie ; il ne juge pas le contenu. **Le WAF comble cet écart.**

**③ Les trois se distinguent, et se confondent en pratique** :

| | **Pare-feu** | **Mandataire inverse** | **WAF** |
|---|---|---|---|
| Décide selon | Adresses, ports, état | Le chemin, le nom demandé | **Le contenu applicatif de la requête** |
| Question posée | *Ce flux a-t-il le droit de passer ?* | *Quel serveur doit répondre ?* | *Cette requête est-elle légitime ?* |
| Voit le contenu | Selon la génération | Si le chiffrement y est terminé | **Nécessairement** |

⚠️ **Les trois peuvent être trois équipements, un seul équipement, ou un service en ligne.** Sur un schéma, une même boîte peut porter les trois — et rien ne le dit.

**④ Ce que cela change.** Le WAF **doit voir le contenu en clair**, donc il impose le mode B ou C du §12.3. Il devient un point où tout le trafic web est lisible.

**⑤ Le coût.** Des faux blocages qui cassent des usages légitimes · un réglage long, souvent en mode observation pendant des semaines · une latence · **un composant de plus sur le chemin critique**.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a un WAF devant » | **En mode blocage ou en mode observation ?** Beaucoup restent en observation des années |
| « Le WAF bloque » | Une règle a été déclenchée. Légitime ou faux positif ? |
| « C'est protégé, il y a un firewall » | **Un pare-feu réseau ne juge pas le contenu d'une requête web** |

---

🔭 **À RECONNAÎTRE — CDN**

**① Qu'est-ce que c'est.** Un réseau de serveurs répartis qui **servent des contenus au plus près de l'utilisateur**, en s'intercalant devant votre serveur d'origine.

**② Quel problème il résout.** La latence, la charge, et l'absorption des pointes — y compris malveillantes.

**③ Ce que cela change au dessin naïf.**

```
   SANS          Utilisateur ──────────────► serveur d'origine

   AVEC          Utilisateur ──► [ CDN ] ──► serveur d'origine
                                    │
                              répond directement
                              si le contenu est en cache
```

**④ Les cinq questions que le CDN impose**, et ce sont elles qui font sa valeur pédagogique :

| Question | Pourquoi elle compte |
|---|---|
| **Où le chiffrement est-il terminé ?** | Chez le fournisseur du CDN — **il voit le contenu en clair** |
| **Qu'est-ce qui est mis en cache ?** | Une page personnalisée mise en cache par erreur est servie à un autre utilisateur |
| **Quelle adresse voit l'origine ?** | Celle du CDN, pas celle de l'utilisateur — §P.4, §34.2 |
| **Que se passe-t-il si le CDN tombe ?** | Selon la configuration : plus rien, ou un repli vers l'origine qui ne tiendra pas la charge |
| **Où placer le WAF ?** | Souvent chez le fournisseur du CDN, puisque c'est là que le contenu est lisible |

⚠️ **La deuxième ligne produit des incidents réels et embarrassants** : un contenu personnalisé — un panier, un nom, une page authentifiée — mis en cache et servi à d'autres. **La règle de cache est une décision de sécurité, pas un réglage de performance.**

**⑤ Le coût.** Une dépendance à un tiers pour la disponibilité de votre site · un point où le contenu est en clair hors de chez vous · **une origine qui doit rester protégée** — sinon on la contourne en s'adressant directement à elle.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est derrière un CDN » | **L'origine est-elle joignable directement ?** Si oui, le CDN se contourne |
| « Le CDN gère le TLS » | Il voit tout en clair. **Rechiffre-t-il vers l'origine ?** |
| « On a purgé le cache » | Un contenu obsolète était servi. **Combien de temps l'a-t-il été ?** |

#### 12.4 Mandataire inverse ou répartiteur de charge ?

**Une confusion fréquente, après celle avec le pare-feu**, et la distinction est utile.

| | **Mandataire inverse** | **Répartiteur de charge** |
|---|---|---|
| Sa raison d'être | **Masquer et contrôler** | **Distribuer et absorber les pannes** |
| Décide selon | Le contenu de la demande — chemin, nom demandé | La disponibilité et la charge des membres |
| Nombre de cibles | Une ou plusieurs | **Plusieurs, par définition** |
| Authentifie | Souvent | Rarement |

⚠️ **En pratique, un même équipement fait souvent les deux** — et c'est pourquoi les deux termes sont employés indifféremment en réunion. **La question qui tranche** : *cet équipement existe-t-il pour cacher le serveur, ou pour en avoir plusieurs ?* La réponse dit à quoi on renoncerait en le supprimant.

#### 12.5 La confusion avec le pare-feu

Celle d'Amélie au §1.8, et elle est universelle.

| | Pare-feu | Mandataire inverse |
|---|---|---|
| Décide | Si le flux passe | Ce qui est servi, et par quel serveur |
| Voit | Les extrémités, parfois le contenu | Le contenu **si le chiffrement y est terminé** — modes B et C |
| Termine la connexion | Non | **Oui en modes B et C**, non en mode A |
| Peut authentifier | Rarement | **Oui, et c'est souvent sa vraie raison d'être** |
| S'il tombe | Selon la configuration | **Les accès externes seuls** |

#### 12.6 S'il disparaît

Tout ce qui est publié devient injoignable de l'extérieur — **et reste joignable de l'intérieur**.

🔥 **SCÉNARIO — le mandataire fonctionne, le service ne répond plus**

| Question | Réponse |
|---|---|
| Symptôme | Les clients externes obtiennent une erreur. Le mandataire répond, sa supervision est verte |
| Hypothèse naïve | « Le mandataire est en panne » |
| Dépendance réelle | **Le serveur derrière lui**. Le mandataire va bien : il n'a plus personne à qui parler |
| Ce que le schéma aurait dû montrer | Les contrôles de santé entre le mandataire et ses cibles |
| Comment vérifier | Le journal du mandataire : il enregistre l'échec de connexion vers l'arrière |

⚠️ **Ce scénario illustre une règle générale** : un composant intermédiaire en bonne santé ne dit rien de la santé du service. **La supervision d'un mandataire doit porter sur ce qu'il obtient de ses cibles, pas sur son propre état.**

#### 12.7 Sur un schéma

En zone démilitarisée, entre la bordure et l'interne. **Reconnaissable à sa position** : tout ce qui vient de l'extérieur y converge.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est derrière le reverse » | Le service n'est pas exposé directement | **Quel mode de terminaison ?** Y a-t-il un chemin direct depuis l'interne ? |
| « Le frontal termine le TLS » | Mode B ou C | Rechiffre-t-il vers l'arrière, ou le trafic interne est-il en clair ? |
| « C'est une VIP » | Une adresse virtuelle portée par le mandataire ou le répartiteur | Combien de cibles derrière ? Une seule ? |
| « Il faut publier l'appli » | La rendre joignable depuis l'extérieur | Par où ? Avec quelle authentification en amont ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne pas exposer directement les serveurs | Un composant de plus à exploiter et corriger |
| Concentrer le chiffrement et les certificats | Une gestion de certificats · **un point où tout est en clair, en modes B et C** |
| Authentifier avant d'atteindre l'application | **Une dépendance forte à l'annuaire** |
| Router selon le contenu | Une configuration qui devient vite complexe |
| Servir de point d'entrée unique | **Un point de rupture pour tous les accès externes** |

🏭 **TROIS TAILLES** — Atelier Martin : **aucun**. Elle ne publie aucun service : la contrainte n'existe pas. HELIOMED : un couple redondé, parce qu'elle publie une plateforme de télésuivi accessible à ses clients. Novaris : une ferme par région, parce que la latence et la réglementation imposent une terminaison locale.

---

### Chapitre 13 — Le répartiteur de charge

#### 13.1 À quoi ça sert

Distribuer les demandes entre plusieurs exemplaires d'un même rôle, et **retirer automatiquement ceux qui ne répondent plus**.

**Pourquoi ça existe.** Dès qu'on veut qu'une panne d'un serveur ne soit pas visible, il faut quelqu'un qui sache que ce serveur ne répond plus, et qui envoie ailleurs. C'est ce que fait le contrôle de santé — et c'est la vraie fonction du répartiteur, davantage que la répartition elle-même.

#### 13.2 Le contrôle de santé : ce qui décide de tout

```
   Toutes les N secondes, le répartiteur interroge chaque membre :

   ①  TEST DE CONNEXION      le port répond-il ?
       → détecte une machine éteinte
       → ne détecte PAS une application bloquée

   ②  TEST APPLICATIF        une page de test répond-elle correctement ?
       → détecte une application en erreur
       → ne détecte PAS une base inaccessible derrière

   ③  TEST DE BOUT EN BOUT   une requête qui traverse toute la chaîne
       → détecte tout
       → coûte plus cher, et peut faire sortir TOUS les membres
         si la panne est en aval
```

⚠️ **Le troisième cas produit un incident classique** : la base tombe, le test de bout en bout échoue sur tous les serveurs, le répartiteur les retire tous, et **le service ne répond plus du tout** — alors qu'il aurait pu servir des pages d'erreur. **Un contrôle de santé trop profond transforme une dégradation en arrêt.**

#### 13.3 Le paradoxe du composant de disponibilité

> **Il crée un point de rupture en résolvant un point de rupture.**

C'est pourquoi il est presque systématiquement redondé — et cette redondance pose exactement les mêmes questions que celle du pare-feu, §10.5.

#### 13.4 La session, et pourquoi elle limite tout

**Répartir des demandes est simple. Répartir des demandes qui appartiennent à une session ne l'est pas.**

| Situation | Ce que le répartiteur doit faire |
|---|---|
| L'application ne garde aucun état | Rien de particulier — n'importe quel membre convient |
| L'application garde la session localement | **Renvoyer l'utilisateur toujours sur le même membre** |
| La session est partagée | N'importe quel membre convient |

⚠️ **Le deuxième cas est très répandu, et il annule une partie du bénéfice.** Si le répartiteur doit renvoyer chaque utilisateur sur « son » serveur, alors la panne de ce serveur **déconnecte ses utilisateurs** — la redondance protège les nouveaux venus, pas ceux qui étaient en cours de travail. C'est le §31.2.

#### 13.5 Trois architectures de répartition

```
  A — RÉPARTITION PAR LA RÉSOLUTION DE NOMS
      Le nom renvoie plusieurs adresses, le client en choisit une.
      → aucun équipement · aucun coût
      → aucun contrôle de santé : un serveur mort reçoit quand même
      → les caches retardent tout changement

  B — RÉPARTITEUR DÉDIÉ
      [ répartiteur ] ──► [ web 1 ] [ web 2 ] [ web 3 ]
      → contrôle de santé · retrait automatique
      → un composant de plus, à redonder

  C — RÉPARTITION INTÉGRÉE À LA PLATEFORME
      L'orchestrateur ou le fournisseur cloud s'en charge.
      → rien à exploiter · rien à dessiner
      → une dépendance à la plateforme · une visibilité réduite
```

⚠️ **Le mode A explique un incident fréquent** : trois adresses derrière un nom, un serveur tombe, **et un tiers des utilisateurs obtient une erreur** — parce que rien ne retire l'adresse morte. Sur un schéma, la répartition paraît identique dans les trois modes.

#### 13.6 Ce qu'il fait à la donnée

Il l'achemine. Selon son niveau, il lit le contenu — auquel cas il fait aussi office de mandataire inverse, et les deux composants se confondent souvent dans un même équipement — §12.4.

#### 13.7 S'il disparaît

🔥 **SCÉNARIO — tout tombe alors que tous les serveurs vont bien**

| Question | Réponse |
|---|---|
| Symptôme | Service inaccessible. Les trois serveurs web répondent normalement en direct |
| Hypothèse naïve | « Un problème applicatif » |
| Dépendance réelle | Le répartiteur — **le seul composant sur le chemin qui ne soit pas redondé** |
| Ce que le schéma aurait dû montrer | S'il est unique ou en paire |
| Concevoir différemment | Le redonder · ou prévoir un chemin de secours documenté vers un serveur direct |

**C'est le composant dont la panne est la plus contre-intuitive du cours** : il a été ajouté pour la disponibilité, et son absence arrête tout.

#### 13.8 Sur un schéma

Juste avant un groupe de boîtes identiques. **La présence de trois serveurs web sans répartiteur dessiné est une question à poser** : soit il existe et n'est pas représenté, soit la répartition se fait par la résolution de noms — mode A, qui n'a pas les mêmes propriétés.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça passe par le load balancer » | Un répartiteur est sur le chemin | **Est-il redondé ?** Quel type de contrôle de santé ? |
| « On a de la persistance de session » | L'utilisateur est renvoyé sur le même serveur | **Alors la redondance ne protège pas les sessions en cours** |
| « On a mis deux nœuds » | Deux membres derrière le répartiteur | Sur des hôtes différents ? — *principe de preuve* |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Continuer malgré la panne d'un membre | **Un composant à redonder lui-même** |
| Absorber une charge croissante | Un contrôle de santé à régler — trop profond, il aggrave |
| Retirer un serveur pour maintenance sans coupure | Une gestion de session à traiter — §31 |

---

### Chapitre 14 — La résolution de noms

> **Un composant dont la disparition produit des effets particulièrement déroutants**, et l'un des moins dessinés.

#### 14.1 À quoi ça sert

Traduire un nom en adresse. Rien de plus, et c'est un préalable à presque tout.

**Pourquoi ça existe.** Les adresses changent, et personne ne les retient. Le nom est un identifiant stable ; l'adresse est un détail d'implémentation. Cette indirection est ce qui permet de déplacer un service sans reconfigurer ses clients.

#### 14.2 La séquence complète

🖼 **SCHÉMA 14.1 — Ce qui se passe réellement**

```
   Utilisateur saisit  www.exemple.fr
            │
            ▼
   ┌──────────────────┐
   │   RÉSOLVEUR      │  ← celui que le poste interroge (« récursif »)
   └────────┬─────────┘
            │
      ┌─────┴─────┐
      │ en cache ? │
      └─────┬─────┘
       ┌────┴────┐
      OUI       NON
       │         │
       │         ▼
       │    interroge les serveurs FAISANT AUTORITÉ
       │    pour ce nom, de proche en proche
       │         │
       │         ▼
       │    obtient l'adresse, et la MET EN CACHE
       │    pour la durée de vie annoncée
       │         │
       └────┬────┘
            ▼
        adresse
            │
            ▼
   Client ─────────► serveur
```

#### 14.3 Les cinq notions qui suffisent à raisonner

| Notion | Ce qu'elle est | Pourquoi elle compte en architecture |
|---|---|---|
| **Résolveur récursif** | Celui que le poste interroge | **Sa panne arrête presque tout, en interne** |
| **Serveur faisant autorité** | Celui qui détient la réponse pour un nom | **Sa panne rend votre organisation injoignable de l'extérieur** |
| **Cache** | La réponse conservée un temps | Masque une panne, **puis l'aggrave d'un coup** |
| **Durée de vie** | Combien de temps la réponse est conservée | **Elle détermine le délai d'un changement d'adresse** |
| **Vue interne / vue externe** | Un même nom, deux réponses selon l'origine | Un service peut être atteint par deux chemins différents |

⚠️ **Deux pannes très différentes** que le mot « DNS » recouvre :

| Ce qui tombe | Qui est affecté | Symptôme |
|---|---|---|
| Le **résolveur récursif** | **Vos utilisateurs** | Plus rien ne fonctionne en interne |
| Le serveur **faisant autorité** | **Vos clients externes** | Votre organisation disparaît d'Internet, l'interne va bien |

**Confondre les deux conduit à chercher au mauvais endroit** — et c'est exactement le cas de synthèse B.

#### 14.4 La durée de vie, et pourquoi elle décide d'une migration

**Le mécanisme, souvent mal compris** :

```
   Vous changez l'adresse d'un service à 10 h 00.
   La durée de vie annoncée est de 24 heures.

   10 h 00   ┃ nouvelle adresse publiée
             ┃
   10 h 05   ┃ un client qui n'a jamais résolu → nouvelle adresse ✅
             ┃ un client qui a résolu à 9 h 00 → ANCIENNE adresse ❌
             ┃
   Jusqu'à   ┃ des clients continuent d'aller à l'ancienne adresse
   le lende- ┃ ⚠️ L'ancien serveur doit rester en service
   main 9 h  ┃
```

⚠️ **La conséquence pratique** : **on ne coupe jamais l'ancien serveur le jour de la bascule.** Et si l'on prévoit une migration, on réduit la durée de vie **plusieurs jours avant** — sinon le changement met une journée à se propager, et personne ne sait quels clients sont passés.

#### 14.5 Les deux vues, et le piège qu'elles créent

```
   VUE EXTERNE                       VUE INTERNE
   portail.exemple.fr → 203.0.113.7  portail.exemple.fr → 10.0.4.80
   (adresse du mandataire)            (adresse du serveur, en direct)

   → un client externe passe par le mandataire, et par ses contrôles
   → un poste interne va DIRECTEMENT au serveur
```

⚠️ **Ce que cela signifie en sécurité** : un contrôle placé sur le mandataire — authentification, inspection, journalisation — **ne s'applique pas aux accès internes**. C'est le §29.3, et c'est l'une des raisons pour lesquelles un dispositif placé en frontal couvre moins qu'on ne le croit — §44.4.

#### 14.6 Ce qu'il fait à la donnée

Rien — il ne voit pas le contenu. Mais il voit **toutes les intentions** : chaque nom demandé, par qui, quand. C'est une source de journaux particulièrement riche.

#### 14.7 S'il disparaît

L'essentiel des connexions établies à partir d'un nom échoue, et de façon déroutante : le réseau fonctionne, les serveurs fonctionnent, et rien n'est joignable.

📌 **Ce qui continue de fonctionner, et qu'il faut savoir** :

| Cas | Pourquoi la résolution n'est pas nécessaire |
|---|---|
| Une connexion vers une adresse écrite en dur | Il n'y a pas de nom à traduire |
| Une connexion déjà établie | La traduction a eu lieu avant |
| Un nom encore en cache | Le cache répond à la place du serveur |
| Un service découvert par un autre mécanisme | Découverte de service, configuration distribuée |
| Un client qui passe par un intermédiaire résolvant lui-même | Le mandataire fait la traduction |

🔥 **SCÉNARIO — panne progressive de résolution**

| Question | Réponse |
|---|---|
| Symptôme | À 9 h 15, deux signalements. À 9 h 40, quarante. À 10 h, tout le site |
| Hypothèse naïve | « Ça se dégrade, c'est probablement la charge » |
| Dépendance réelle | **Les caches expirent un par un.** La panne date de 9 h 00 |
| Ce que le schéma aurait dû montrer | Le résolveur, et combien il y en a |
| Comment le reconnaître | **Une panne qui s'aggrave par vagues sans cause apparente est très souvent une panne de résolution ou de certificat** |

🔥 **SCÉNARIO — un résolveur sur deux tombe**

| Question | Réponse |
|---|---|
| Symptôme | Certaines résolutions sont lentes. La plupart fonctionnent |
| Hypothèse naïve | « Le réseau est chargé » |
| Dépendance réelle | Les clients interrogent le premier serveur, attendent l'expiration du délai, puis basculent sur le second |
| Ce que le schéma aurait dû montrer | Que les deux résolveurs sont **configurés sur les postes**, et dans quel ordre |
| Concevoir différemment | Vérifier que les postes connaissent bien les deux, et non un seul |

⚠️ **Ce second scénario est fréquent et rarement diagnostiqué correctement.** Une redondance de résolution ne fonctionne que si les clients connaissent les deux serveurs. Beaucoup n'en connaissent qu'un — et la redondance existe sur le schéma sans exister en pratique. **Principe de preuve.**

#### 14.8 Sur un schéma

**Presque jamais.** C'est l'exemple canonique du flux de dépendance du principe des trois flux.

⚠️ **La question à poser devant tout schéma** : *où est la résolution de noms, et combien y en a-t-il ?* Si personne ne sait répondre, vous venez d'identifier une dépendance non maîtrisée — et c'est fréquemment l'une des plus structurantes du système.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le DNS est sur les DC » | Les contrôleurs d'annuaire assurent aussi la résolution | **Alors une panne d'annuaire est aussi une panne de résolution** — deux dépendances en une |
| « C'est un problème de DNS » | Une résolution échoue | Récursif ou faisant autorité ? Interne ou externe ? |
| « On a baissé le TTL » | La durée de vie a été réduite | Depuis quand ? Une migration est-elle en cours ? |
| « Il faut créer une entrée » | Ajouter un nom | Dans quelle vue — interne, externe, ou les deux ? |

⚠️ **La première ligne est structurante** : quand la résolution est portée par les contrôleurs d'annuaire, une seule panne produit **deux effets qui n'ont apparemment aucun rapport** — plus d'authentification, et plus de résolution. Le diagnostic devient difficile.

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Désigner les services par un nom stable | **Une dépendance universelle et invisible** |
| Changer une adresse sans changer les configurations | Un délai de propagation lié aux caches |
| Distinguer vue interne et externe | Une double configuration à maintenir cohérente · **des contrôles qui ne s'appliquent pas partout** |
| Redonder | Efficace **uniquement si les clients connaissent les deux serveurs** |

🏭 **TROIS TAILLES** — Atelier Martin : la résolution est portée par le boîtier tout-en-un, **et c'est un point de rupture assumé**. HELIOMED : deux résolveurs internes, portés par les contrôleurs d'annuaire. Novaris : une infrastructure dédiée, **parce que porter la résolution sur les contrôleurs d'annuaire cumule deux pannes en une, ce qu'une organisation de cette taille ne peut pas se permettre**.

---

### Chapitre 15 — L'attribution d'adresses

#### 15.1 À quoi ça sert

Donner automatiquement à une machine qui démarre son adresse, son masque, sa passerelle et l'adresse de son résolveur.

**Pourquoi ça existe.** Configurer six cents postes à la main est impossible ; et un plan d'adressage qui change imposerait de tous les reprendre. L'attribution automatique rend le poste **indifférent au réseau sur lequel il est branché**.

#### 15.2 La séquence, et ce qu'elle distribue

```
   ①  La machine démarre. Elle n'a pas d'adresse.
   ②  Elle demande, en diffusion : « quelqu'un peut-il me configurer ? »
   ③  Le serveur répond, et propose :
         · une adresse, pour une DURÉE limitée (le bail)
         · un masque de sous-réseau
         · une passerelle par défaut
         · l'adresse d'un ou plusieurs résolveurs
         · parfois : un domaine, un serveur de temps, un mandataire
   ④  La machine accepte, et renouvelle avant expiration du bail
```

⚠️ **Ce qu'il faut retenir de l'étape ③** : ce composant ne distribue pas seulement une adresse. **Il distribue la configuration réseau complète.** Une erreur dans l'adresse du résolveur distribuée, et six cents postes perdent la résolution de noms — §14.

#### 15.3 Le bail, et pourquoi la panne est différée

```
   Bail de 8 jours, renouvelé à mi-parcours.

   Jour 0    Le serveur tombe.
   Jour 0    RIEN ne se passe. Toutes les machines ont une adresse valide.
   Jour 4    Les premiers renouvellements échouent → les machines gardent
             leur adresse et réessaient
   Jour 8    Les premiers baux expirent → les premières machines
             perdent leur adresse
   Jour 8-16 Les machines tombent une par une, dans un ordre
             qui paraît aléatoire
```

⚠️ **C'est la panne différée par excellence**, et la plus difficile à relier à sa cause : **plusieurs jours peuvent séparer l'incident de ses premiers effets**, et les effets arrivent progressivement.

🔥 **SCÉNARIO — des postes tombent au hasard depuis trois jours**

| Question | Réponse |
|---|---|
| Symptôme | Chaque jour, quelques postes n'ont plus de réseau. Aucun point commun apparent |
| Hypothèse naïve | « Un problème matériel sur les postes » ou « le commutateur » |
| Dépendance réelle | Le serveur d'attribution, arrêté **il y a plusieurs jours** |
| Ce que le schéma aurait dû montrer | Ce composant — il n'y figure jamais |
| Comment le reconnaître | **Les postes touchés sont ceux qui ont redémarré ou dont le bail a expiré** — pas un groupe géographique |

#### 15.4 Ce qu'il fait à la donnée

Rien. Mais il sait **quelle machine est apparue, quand, et avec quelle identité matérielle** — une source précieuse pour l'inventaire, et presque jamais exploitée. C'est le chapitre 11 du volume Asset Management.

#### 15.5 Sur un schéma

Jamais. Flux de dépendance.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Il est en DHCP » | La machine reçoit sa configuration automatiquement | **Son adresse change-t-elle ?** Cela affecte les règles de filtrage par adresse |
| « On lui a mis une IP fixe » | Adresse configurée en dur, ou réservée | En dur sur la machine, ou réservée sur le serveur ? Ce n'est pas la même chose |
| « Un poste a pris une mauvaise IP » | Conflit ou serveur non autorisé | **Un serveur d'attribution non déclaré sur le réseau est un incident de sécurité** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne pas configurer chaque machine à la main | **Une machine peut apparaître sans être déclarée nulle part** |
| Changer un plan d'adressage sans toucher aux postes | Une dépendance de plus au démarrage |
| Distribuer toute la configuration réseau | **Une erreur se propage à l'ensemble du parc** |

⚠️ **La ligne du milieu à droite** est l'origine d'un problème traité dans deux autres volumes : une machine branchée obtient une adresse et fonctionne, **sans avoir été inventoriée, autorisée ni supervisée**.

---

### Chapitre 16 — L'annuaire

> ⚠️ **Précision de vocabulaire, à poser avant tout.**
>
> **Service d'annuaire** est le concept général : un composant qui détient des identités, des groupes et des règles.
> **Active Directory** en est l'implémentation la plus répandue en entreprise, et c'est elle que ce chapitre décrit — parce qu'elle rend le concept concret.
>
> **Les propriétés décrites ici — contrôleurs, domaines, forêts, relations d'approbation, politiques — sont celles de ce modèle.** D'autres services d'identité existent et fonctionnent autrement : annuaires ouverts, fournisseurs d'identité en ligne, bases d'identités applicatives. Ne transportez pas ce modèle sur eux sans vérifier.
>
> ⚠️ **Et surtout** : **LDAP n'est pas l'authentification.** C'est un protocole d'interrogation et de modification d'annuaire. Dans un domaine Active Directory, l'authentification s'appuie principalement sur **Kerberos**, et la résolution de noms y joue un rôle structurant. Un schéma qui montre uniquement un flux LDAP vers l'annuaire ne montre donc pas tout le mécanisme d'authentification.

#### 16.1 À quoi ça sert

Détenir les identités, les groupes et les règles, et répondre à deux questions : *qui es-tu* et *à quoi as-tu droit*.

**Pourquoi ça existe.** Sans lui, chaque application détient ses propres comptes. Un salarié qui part doit être retiré de trente endroits — et il le sera de vingt-huit. La centralisation résout le problème du cycle de vie des identités, et en crée un autre : **une dépendance universelle**.

#### 16.2 Les trois mécanismes, et pourquoi il faut les distinguer

| Mécanisme | Ce qu'il fait | Sur un schéma |
|---|---|---|
| **LDAP** | Interroge et modifie l'annuaire : chercher un utilisateur, lister un groupe | Ports 389 / 636 |
| **Kerberos** | **Authentifie** : délivre un ticket qui prouve l'identité, sans renvoyer le mot de passe | Rarement dessiné |
| **Résolution de noms** | **Localise les contrôleurs** eux-mêmes | Jamais dessiné |

⚠️ **La troisième ligne explique un incident très fréquent** : dans un domaine Active Directory, un poste trouve ses contrôleurs **par la résolution de noms**. Si celle-ci est défaillante, **le poste ne trouve pas l'annuaire** — et le symptôme est une panne d'authentification, alors que l'annuaire fonctionne parfaitement.

> **Deux composants invisibles, et l'un dépend de l'autre.** C'est le chemin de diagnostic le plus difficile du cours.

#### 16.3 La cascade d'une panne

```
   T+0        L'annuaire cesse de répondre
              │
   T+0        Les sessions ouvertes CONTINUENT      ← rien ne se voit
              │  (les tickets déjà délivrés restent valides)
              │
   T+minutes  Toute nouvelle authentification échoue
              │  · nouveaux accès aux partages
              │  · connexions applicatives
              │
   T+heures   Les tickets expirent · les sessions tombent une à une
              │
   Au premier Un utilisateur ne peut plus ouvrir sa session.
   redémarrage Il est bloqué devant son poste.
```

🔥 **SCÉNARIO — un contrôleur sur deux tombe**

| Question | Réponse |
|---|---|
| Symptôme | Certaines ouvertures de session sont lentes. La plupart fonctionnent |
| Hypothèse naïve | « Les postes sont lents » |
| Dépendance réelle | Les clients tentent le premier contrôleur, attendent l'expiration du délai, basculent |
| Ce que le schéma aurait dû montrer | Combien de contrôleurs, **et s'ils sont sur des hôtes différents** — *principe de preuve* |
| Concevoir différemment | Vérifier que la bascule est effective, et non seulement configurée |

#### 16.4 Les notions qui suffisent à raisonner

| Notion | Pourquoi elle compte |
|---|---|
| **Contrôleur** | La machine qui répond. **Un domaine fonctionne avec un seul ; deux ou plus sont recommandés pour la disponibilité** — ⚠️ **Principe de preuve** : deux contrôleurs sur le même hôte ne constituent pas une redondance |
| **Domaine, forêt** | *(vocabulaire Active Directory)* Le périmètre d'une identité. Une acquisition en ajoute souvent un |
| **Relation d'approbation** | Ce qui permet à une identité d'un périmètre d'accéder à un autre — **et ce qui propage une compromission** |
| **Groupe** | L'unité de droit réelle. Les droits individuels restent minoritaires dans les modèles bien tenus |
| **Politiques** | Des règles appliquées automatiquement aux postes à l'ouverture de session |

⚠️ **Sur les relations d'approbation** : elles sont pratiques et elles ont une conséquence lourde. Une compromission dans le périmètre A peut devenir une compromission dans le périmètre B. **Sur un schéma, une flèche entre deux annuaires mérite toujours une question : dans quel sens, et avec quelle portée ?**

#### 16.5 Ce qu'il fait à la donnée

Il ne la voit pas. Mais il **décide qui la voit** — ce qui en fait, avec la sauvegarde, l'actif dont la compromission a les conséquences les plus larges.

#### 16.6 Sur un schéma

Dessiné comme une boîte, **sans aucun trait** — le cas du §1.1. Tout s'y connecte, rien ne le montre.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça tape l'AD » | Le composant s'authentifie contre l'annuaire | **Par quel mécanisme ?** LDAP pour interroger, ou Kerberos pour authentifier ? |
| « Il est dans le domaine » | La machine est jointe à l'annuaire | Alors elle dépend de lui **et de la résolution de noms** au démarrage |
| « On a un trust avec l'autre forêt » | Une relation d'approbation existe | **Dans quel sens ? Depuis quand ? Qui l'a demandée ?** |
| « Le DNS est sur les DC » | Deux fonctions sur les mêmes machines | **Une panne, deux effets sans rapport apparent** — §14 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Une identité unique pour de nombreux services | **Une dépendance universelle** · une compromission qui donne tout |
| Gérer les droits par groupes | Des groupes qui s'accumulent et ne se réduisent jamais seuls |
| Appliquer des politiques automatiquement | Un empilement difficile à auditer |
| Fédérer plusieurs périmètres | **Une compromission qui peut traverser la relation d'approbation** |

🏭 **TROIS TAILLES** — Atelier Martin : un contrôleur, **et c'est un point de rupture assumé faute de budget**. HELIOMED : deux contrôleurs, plus un annuaire hérité de l'acquisition de 2019 que personne n'a fusionné. Novaris : quatre forêts, **parce que sept acquisitions en quinze ans et trois fusions arbitrées comme trop risquées** — jamais parce que douze mille salariés.

---

### Chapitre 17 — L'infrastructure de clés

#### 17.1 À quoi ça sert

Émettre, publier et révoquer des certificats.

**Ce qu'un certificat fait exactement**, parce que la formulation courante est imprécise :

> Un certificat **lie une identité — ou un attribut — à une clé publique**, et cette liaison est attestée par une autorité au sein d'une chaîne de confiance.

⚠️ **Un certificat ne chiffre rien par lui-même.** Il permet à un protocole de vérifier à qui l'on parle ; le chiffrement de l'échange est ensuite assuré par le protocole. Un certificat peut aussi servir à signer sans qu'aucun chiffrement de transport n'intervienne.

#### 17.2 La chaîne de confiance, en une image

```
   [ AUTORITÉ RACINE ]        ← son certificat est INSTALLÉ sur les machines
            │                    C'est ce qui fonde toute la confiance
            ▼
   [ AUTORITÉ INTERMÉDIAIRE ] ← elle signe au quotidien
            │                    La racine reste hors ligne
            ▼
   [ CERTIFICAT DU SERVEUR ]  ← présenté au client

   Le client vérifie : ce certificat est-il signé par une autorité
   à laquelle JE fais confiance ?
        ├── OUI  ──► accepté
        └── NON  ──► avertissement, ou refus
```

⚠️ **Le point qui décide de tout** : *à quelles autorités le client fait-il confiance ?* Un navigateur fait confiance à une liste préinstallée d'autorités publiques. **Une machine de votre organisation fait en plus confiance à votre autorité interne, si vous l'y avez déployée.**

**D'où la formulation exacte** : un certificat émis par une autorité privée n'est reconnu que par **les systèmes qui font confiance à cette chaîne** — vos machines si vous l'y avez déployée, celles d'un partenaire à qui vous l'avez transmise, et **aucune machine que vous ne contrôlez pas si vous ne l'avez pas fait**.

#### 17.3 La révocation, et pourquoi elle est le maillon faible

**Le problème** : un certificat a une date d'expiration. Que faire s'il faut l'invalider **avant** ?

```
   ①  L'autorité publie une liste de certificats révoqués
   ②  Le client la télécharge, ou interroge un service dédié
   ③  Il vérifie que le certificat présenté n'y figure pas

   ⚠️  Que se passe-t-il si l'étape ② échoue ?
        ├── mode strict   : le client REFUSE  → indisponibilité
        └── mode souple   : le client ACCEPTE → la révocation ne sert à rien
```

⚠️ **Le comportement varie fortement selon le client, le mécanisme et la configuration.** Certains refusent, beaucoup acceptent, d'autres ne vérifient pas du tout ; des mécanismes récents améliorent la situation en faisant transmettre l'état de révocation par le serveur lui-même.

> **Ce qu'il faut en retenir en architecture** : **on ne peut pas supposer qu'une révocation sera effective partout et immédiatement.** Ce n'est pas un mécanisme inutile, c'est un mécanisme dont l'effet dépend de choses que vous ne contrôlez pas.

📌 **Ce que cela impose en conception** : ne pas compter sur la révocation seule. **Des certificats de courte durée** réduisent la fenêtre d'exposition sans dépendre d'un mécanisme fragile — au prix d'un renouvellement fréquent, donc automatisé.

🔭 **À RECONNAÎTRE — HSM**

**① Qu'est-ce que c'est.** Un équipement matériel dédié qui **protège des clés cryptographiques et exécute les opérations qui les utilisent**.

**② Quel problème il résout.** La question fondamentale de tout ce chapitre :

> ### Où vit réellement la clé privée ?

Si elle est dans un fichier sur un serveur, **quiconque accède à ce serveur — ou à ses sauvegardes — l'obtient**. Le concept architectural du HSM n'est pas son fonctionnement cryptographique interne, c'est celui-ci :

> **La clé sensible peut être *utilisée* sans jamais être *exportée* comme un simple fichier.**

L'application demande une signature ou un déchiffrement ; l'équipement l'exécute et renvoie le résultat. **La clé ne sort pas.**

**③ Où on le rencontre.** À la racine d'une autorité de certification interne · pour signer du code ou des micrologiciels · dans les traitements de paiement · partout où une clé compromise aurait des conséquences irréversibles.

**④ Ce que cela change.** Une dépendance nouvelle : **si l'équipement est indisponible, les opérations qui en dépendent échouent**. Et une question de sauvegarde qui n'a pas de réponse simple — une clé qu'on ne peut pas exporter ne se sauvegarde pas comme un fichier ; il existe des mécanismes de séquestre, et ils sont eux-mêmes sensibles.

**⑤ Le coût.** Un équipement onéreux · une exploitation spécialisée · **une cérémonie de clés** pour les opérations sensibles, avec plusieurs porteurs · une redondance qui doit être prévue dès l'origine.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « La racine est dans un HSM » | Bon signe. **Est-il redondé ? Où est le séquestre ?** |
| « La clé est dans un fichier sur le serveur » | **Alors elle est aussi dans les sauvegardes** — §33.2 |
| « On signe avec le HSM » | **Que se passe-t-il s'il est indisponible au moment de signer ?** |

📚 **À approfondir ailleurs** : les niveaux de certification, les cérémonies de clés, l'intégration applicative.

#### 17.4 S'il disparaît

Rien **immédiatement**. Puis, à chaque expiration de certificat, un service tombe — sans préavis et sans lien apparent avec la panne.

🔥 **SCÉNARIO — un service tombe sans que rien n'ait changé**

| Question | Réponse |
|---|---|
| Symptôme | Un service refuse les connexions à un horaire précis et net. Aucune intervention |
| Hypothèse naïve | « Une tâche planifiée a cassé quelque chose » |
| Dépendance réelle | **Un certificat a expiré.** L'heure exacte est le signe distinctif |
| Ce que le schéma aurait dû montrer | Rien — les certificats ne sont jamais dessinés |
| Comment le reconnaître | **Une panne à un horaire net, sans intervention, oriente vers une échéance** : expiration de certificat, rotation de secret, fin de durée de vie. La date exacte d'un certificat est inscrite dedans — elle n'est pas nécessairement minuit |
| Concevoir différemment | Surveiller les dates d'expiration · automatiser le renouvellement |

🔥 **SCÉNARIO — la chaîne fonctionne, la révocation non**

| Question | Réponse |
|---|---|
| Symptôme | Certains clients — souvent les plus stricts — refusent la connexion. La plupart l'acceptent |
| Hypothèse naïve | « Un problème sur ces postes » |
| Dépendance réelle | Le service de révocation est injoignable. Les clients en mode strict refusent |
| Ce que le schéma aurait dû montrer | Que la vérification de révocation est **un flux sortant, vers un service souvent externe** |
| Concevoir différemment | Vérifier que ce flux est autorisé dans le pare-feu — **il ne l'est pas toujours** |

⚠️ **Ce second scénario est un cas d'école** : une organisation bloque les sorties Internet non autorisées, et bloque au passage la vérification de révocation. Les certificats fonctionnent, jusqu'au jour où un client strict apparaît.

#### 17.5 Ce qu'il faut en savoir pour raisonner

| Notion | Pourquoi elle compte |
|---|---|
| **Autorité** | Qui signe. Publique ou interne, et cela change tout |
| **Chaîne de confiance** | Si un maillon n'est pas reconnu, le certificat est refusé |
| **Expiration** | **La première cause d'incident liée aux certificats** |
| **Révocation** | Un mécanisme fragile · rarement testé · **au comportement variable selon les clients** |
| **Interne contre publique** | Un certificat privé n'est reconnu que par les systèmes qui font confiance à cette chaîne |
| **Inventaire des certificats** | **Presque jamais tenu** — et c'est ce qui produit les expirations surprises |

#### 17.6 Sur un schéma

Jamais. Les certificats sont invisibles tant qu'ils fonctionnent.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le certif a expiré » | Une date est dépassée | **Combien d'autres expirent dans les 90 jours ?** Existe-t-il un inventaire ? |
| « On a notre propre PKI » | Une autorité interne existe | Sa chaîne est-elle déployée partout où elle doit l'être ? |
| « Il y a une erreur de certificat » | Le client refuse ou avertit | Expiration · chaîne non reconnue · **nom qui ne correspond pas** — trois causes distinctes |
| « On a mis un wildcard » | Un certificat couvre plusieurs noms | **Sa compromission affecte tous ces noms à la fois** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Émettre des certificats sans passer par un tiers | **Une hiérarchie à maintenir des années** · des expirations à suivre |
| Émettre pour des noms ou des usages non couverts par les autorités publiques | Une révocation qui doit fonctionner réellement, et qui est rarement testée |
| Authentifier des machines entre elles | Un inventaire des certificats — **presque jamais tenu** |
| Un certificat couvrant plusieurs noms | Une compromission de portée élargie |

🏭 **TROIS TAILLES** — Atelier Martin : **aucune infrastructure interne**, uniquement des certificats publics achetés. HELIOMED : une interne, **parce qu'elle doit émettre des certificats sur des noms internes que les autorités publiques ne délivrent pas, et parce qu'elle veut maîtriser sa propre chaîne de confiance**. Novaris : une hiérarchie à deux niveaux, pour cloisonner l'émission par entité.

---

#### 🔬 Mini-lab 4 — Dix composants sans légende

**Objectif** — **Proposer le rôle le plus probable** de chaque composant, et dire ce qu'il faudrait vérifier.
**Durée** 30 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 8 à 17

```
                        Internet
                            │
                        ┌───┴───┐
                        │   A   │
                        └───┬───┘
              ┌─────────────┼─────────────┐
          ┌───┴───┐                   ┌───┴───┐
          │   B   │                   │   C   │
          └───┬───┘                   └───────┘
          ┌───┴───┐
          │   D   │
          └───┬───┘
        ┌─────┼─────┐
      [E1]  [E2]  [E3]
              │
          ┌───┴───┐        ┌───────┐        ┌───────┐
          │   F   │        │   G   │        │   H   │
          └───────┘        └───────┘        └───────┘
                          (aucun trait)    (aucun trait)

  Indices : C reçoit les courriels · G répond à des requêtes sur le port 53
            H répond sur les ports 389 et 636 · F contient les données
```

❓ **Pour chaque composant A à H** : proposez le rôle le plus probable, indiquez **ce qu'il faudrait vérifier pour le confirmer**, et dites lesquels sont probablement des points de rupture.

⚠️ **Le principe d'hypothèse s'applique** : un port, une position et un ensemble de connexions constituent un **faisceau**, pas une preuve. Un service peut écouter sur un port non standard, un composant peut cumuler deux rôles, et une position peut être trompeuse.

---

**Corrigé**

| Réf | Rôle **probable** | Sur quel faisceau | **À vérifier pour confirmer** | Rupture ? |
|---|---|---|---|---|
| **A** | Pare-feu | Position en bordure, tout converge | Est-ce un pare-feu seul, ou un boîtier cumulant routage et accès distant ? | Probable, sauf redondance non représentée |
| **B** | Mandataire inverse | Reçoit de l'extérieur, relaie vers l'intérieur | **Quel mode de terminaison** ? §12 · redondé ? | Probable, pour l'externe seulement |
| **C** | Relais de messagerie | L'indice fourni | Relaie-t-il vers un serveur interne, ou vers un service en ligne ? | Probable |
| **D** | Répartiteur de charge | Placé avant un groupe identique | La répartition se fait-elle bien ici, ou par la résolution de noms ? | **Probable** — §13 |
| **E1-E3** | Serveurs web | Trois exemplaires derrière un répartiteur | **Sur des hôtes différents ?** · **où vivent les sessions ?** — *principe de preuve*, §31.2 | **Indéterminé** |
| **F** | Base de données | L'indice, et la position en bas | Unique, ou répliquée sans que le schéma le montre ? | Probable, et le plus lourd de conséquences |
| **G** | Service de résolution de noms | Port 53 | Récursif, faisant autorité, ou les deux ? Combien y en a-t-il ? | Probable, **et invisible** |
| **H** | Service d'annuaire | Ports 389 et 636 | **Ces ports ne montrent que l'interrogation.** L'authentification passe par d'autres mécanismes — §16 | Probable, **et invisible** |

**Les quatre erreurs attendues** *(cohérentes avec le principe d'hypothèse)*

1. **Répondre avec certitude.** Aucune de ces identifications n'est établie. Un service peut écouter sur un port inhabituel, un composant peut cumuler deux rôles, une position peut être trompeuse. **Principe d'hypothèse.**
2. **Confondre A et B.** Les deux sont en bordure. La distinction se fait par ce qui les suit : A reçoit tout, B ne relaie que le web.
3. **Ne pas retenir G et H comme ruptures probables** parce qu'aucun trait ne les relie. **C'est le piège central** : leur absence de connexion ne signifie pas qu'ils sont isolés, mais que le dessinateur a renoncé à représenter des dépendances universelles.
4. **Conclure que E1-E3 constituent une redondance.** Rien ne l'établit : ils peuvent partager un hôte, et les sessions peuvent être locales. **Principe de preuve** — le schéma montre une *intention* de redondance.

**La leçon** : sur huit composants, **cinq sont des ruptures probables, dont deux ne sont reliés à rien** — et la seule redondance apparente n'est pas vérifiée.

---

#### 🔬 Mini-lab 5 — Que se passe-t-il si on retire cette boîte ?

**Objectif** — Prévoir l'effet de la disparition d'un composant, y compris différé.
**Durée** 25 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 8 à 17

Pour chacun, dire : **ce qui tombe · quand · et si l'utilisateur comprend**.

---

**Corrigé**

| Composant retiré | Ce qui tombe | Délai | L'utilisateur comprend-il ? |
|---|---|---|---|
| **Commutateur d'un étage** | Tout l'étage | Immédiat | ✅ Oui — « plus de réseau ici » |
| **Routeur inter-sites** | Les échanges entre sites | Immédiat | ⚠️ Partiellement — « le serveur de Lyon ne répond plus » |
| **Pare-feu en coupure** | Tout ce qui traverse | Immédiat | ⚠️ Non — tout paraît fonctionner localement |
| **Mandataire sortant** | L'accès Internet des postes | Immédiat | ❌ **Non** — « j'ai du réseau mais pas Internet » |
| **Mandataire inverse** | Les accès externes seuls | Immédiat | ❌ Non — l'interne fonctionne |
| **Répartiteur de charge** | **Tout le service**, malgré des serveurs sains | Immédiat | ❌ **Non** — c'est le plus contre-intuitif |
| **Résolution de noms** | Presque tout | **Différé** — les caches masquent, puis tout tombe | ❌ **Non — la panne la plus déroutante** |
| **Attribution d'adresses** | Les machines, une par une | **Différé de plusieurs heures ou jours** | ❌ Non — aucun lien apparent |
| **Annuaire** | Les authentifications, puis tout | Progressif | ⚠️ Partiellement |
| **Infrastructure de clés** | Un service à chaque expiration | **Différé de plusieurs mois** | ❌ **Non — la plus difficile à diagnostiquer** |

**Ce que le tableau enseigne, et qui est le cœur de la partie** :

> **Les composants dont la panne est la plus incompréhensible sont exactement ceux qui ne sont pas dessinés.**

Résolution de noms, attribution d'adresses, annuaire, certificats : quatre flux de dépendance, quatre pannes différées ou inexplicables, zéro représentation sur les schémas. C'est la règle principe des trois flux démontrée par ses conséquences.

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> ✓ ce que fait chacun des **dix composants d'infrastructure**, et surtout **ce qui se passe s'il disparaît** ;
> ✓ distinguer **routeur et pare-feu** — où ça va, et si ça a le droit ;
> ✓ distinguer **mandataire sortant et mandataire inverse**, deux fonctions opposées sous un même mot ;
> ✓ que le **répartiteur de charge crée un point de rupture en en résolvant un** ;
> ✓ que les **quatre composants les moins dessinés** produisent les pannes les plus incompréhensibles ;
> ✓ pour chaque composant, **la contrainte qu'il résout et le coût qu'il introduit** — et qu'ajouter n'est jamais gratuit ;
> ✓ qu'**aucun de ces composants n'apparaît par la taille de l'organisation**, mais par une contrainte identifiable ;
> ✓ **le socle réseau minimal** : deux niveaux d'adressage · sous-réseau et passerelle · sens d'établissement d'une connexion · traduction d'adresses · et que le modèle « adresse interne + traduction » n'est pas universel ;
> ✓ que **LDAP interroge et Kerberos authentifie** — trois mécanismes, pas un ;
> ✓ que **le chiffrement peut être terminé à trois endroits différents**, et que le schéma ne le dit jamais.
>
> **Ce que vous ne savez pas encore** : ce qui s'exécute sur les serveurs, et pourquoi on les sépare. C'est l'objet de la Partie III.

---
