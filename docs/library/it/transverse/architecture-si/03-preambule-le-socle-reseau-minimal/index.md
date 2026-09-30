---
title: Préambule — Le socle réseau minimal
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
---

> **Pourquoi ce préambule existe.** Les dix chapitres qui suivent supposent quelques notions sans lesquelles on ne peut pas répondre à la question centrale du cours : **qu'est-ce qui rend deux zones joignables ?**
>
> **Application stricte du principe de coupe** : ce qui suit tient en cinq pages. Vous n'y trouverez ni calcul d'adressage, ni protocole de routage, ni commande. Uniquement ce qui permet de comprendre pourquoi un flux passe ou ne passe pas.


## P.1 Deux niveaux d'adressage, et pourquoi il en faut deux

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


## P.2 Adresse, sous-réseau, passerelle

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


## P.3 Ports et état d'une connexion

| Notion | Ce qu'il faut en savoir |
|---|---|
| **Port** | Un numéro qui identifie **le service** sur une machine. L'adresse dit *où*, le port dit *quoi* |
| **Connexion** | Un échange établi entre deux couples adresse-port, avec un état : en cours d'établissement, établie, fermée |
| **Sens d'établissement** | **Qui a initié.** C'est ce qui distingue un flux entrant d'un flux sortant |

> **La notion la plus utile du préambule** : un pare-feu qui autorise un flux **sortant** laisse revenir les réponses de ce flux, parce qu'il **suit l'état des connexions**. C'est pourquoi *« autoriser vers Internet »* ne signifie pas *« autoriser depuis Internet »*.

⚠️ **Ce que cela change en lecture** : sur un schéma, une flèche sans sens est ambiguë — §3.2. **Le sens d'établissement est l'information la plus déterminante d'un flux**, et c'est celle qui manque le plus souvent.


## P.4 Traduction d'adresses

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


## P.5 Deux familles d'adressage

📌 **Ce qu'il faut savoir, et rien de plus** :

| | **IPv4** | **IPv6** |
|---|---|---|
| Espace d'adressage | Limité — d'où la traduction d'adresses | Très vaste |
| Traduction d'adresses | **Structurante** : la quasi-totalité des réseaux internes en dépend | **Généralement inutile** — les machines peuvent avoir une adresse routable |
| Conséquence en lecture | L'adresse observée n'est souvent pas l'origine | **L'adresse observée peut être celle de la machine** |
| Présence | Partout | Croissante, souvent en parallèle du premier |

⚠️ **Pourquoi cela figure dans ce cours** : le modèle mental *« adresse interne + traduction »* que nous employons dans tout le volume **n'est pas universel**. Une machine peut disposer simultanément des deux familles — c'est la double pile — et suivre alors **deux chemins différents selon la famille employée**.

**La question de lecture qui en découle** : *ce schéma décrit-il un adressage, ou les deux ?* Dans la majorité des schémas, la question n'est pas tranchée — et un flux peut passer dans une famille et être bloqué dans l'autre.


## P.6 Ce que ce préambule permet de faire

☐ Expliquer pourquoi deux machines d'un même segment se joignent sans routeur
☐ Expliquer pourquoi une machine sans passerelle ne sort pas de son segment
☐ Distinguer le sens d'établissement d'un flux, et savoir pourquoi il détermine tout
☐ Comprendre pourquoi une adresse dans un journal n'identifie pas une machine
☐ Savoir qu'un service exposé n'est pas nécessairement à l'adresse annoncée
☐ Savoir que le modèle « adresse interne + traduction » n'est pas universel

**Ce qu'il ne permet pas, volontairement** : dimensionner un plan d'adressage, choisir un protocole de routage, configurer quoi que ce soit — *principe de coupe*.

---

## Dans cette partie

- [Chapitre 8 — Le commutateur](01-chapitre-8-le-commutateur.md)
- [Chapitre 9 — Le routeur](02-chapitre-9-le-routeur.md)
- [Chapitre 10 — Le pare-feu](03-chapitre-10-le-pare-feu.md)
- [Chapitre 11 — Le mandataire sortant](04-chapitre-11-le-mandataire-sortant.md)
- [Chapitre 12 — Le mandataire inverse](05-chapitre-12-le-mandataire-inverse.md)
- [Chapitre 13 — Le répartiteur de charge](06-chapitre-13-le-repartiteur-de-charge.md)
- [Chapitre 14 — La résolution de noms](07-chapitre-14-la-resolution-de-noms.md)
- [Chapitre 15 — L'attribution d'adresses](08-chapitre-15-l-attribution-d-adresses.md)
- [Chapitre 16 — L'annuaire](09-chapitre-16-l-annuaire.md)
- [Chapitre 17 — L'infrastructure de clés](10-chapitre-17-l-infrastructure-de-cles.md)
