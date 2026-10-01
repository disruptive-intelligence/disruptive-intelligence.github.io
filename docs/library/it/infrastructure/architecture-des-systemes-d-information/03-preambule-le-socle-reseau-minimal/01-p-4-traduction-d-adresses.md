---
title: P.4 Traduction d'adresses
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

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
