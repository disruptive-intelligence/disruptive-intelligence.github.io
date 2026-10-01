---
title: Préambule — Le socle réseau minimal
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
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

## Dans cette partie

- [P.4 Traduction d'adresses](01-p-4-traduction-d-adresses.md)
- [Chapitre 8 — Le commutateur](02-chapitre-8-le-commutateur.md)
- [Chapitre 9 — Le routeur](03-chapitre-9-le-routeur.md)
- [Chapitre 10 — Le pare-feu](04-chapitre-10-le-pare-feu.md)
- [Chapitre 11 — Le mandataire sortant](05-chapitre-11-le-mandataire-sortant.md)
- [Chapitre 12 — Le mandataire inverse](06-chapitre-12-le-mandataire-inverse.md)
- [Chapitre 13 — Le répartiteur de charge](07-chapitre-13-le-repartiteur-de-charge.md)
- [Chapitre 14 — La résolution de noms](08-chapitre-14-la-resolution-de-noms.md)
- [Chapitre 15 — L'attribution d'adresses](09-chapitre-15-l-attribution-d-adresses.md)
- [Chapitre 16 — L'annuaire](10-chapitre-16-l-annuaire.md)
- [Chapitre 17 — L'infrastructure de clés](11-chapitre-17-l-infrastructure-de-cles.md)
