---
title: Cas A — Le schéma qu'on vous donne le premier jour
source: IT/Architecture_SI.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - index.md
---

> **Durée** 2 h · **Livrables** : lecture en sept passes · liste de l'invisible · trois questions
> **Prérequis** : chapitres 3, 4, 36, 50

## A.1 La situation

Vous arrivez comme référent sécurité dans une organisation de 700 personnes, secteur des services, trois sites. On vous remet un schéma daté de **mars 2021** et un accès en lecture à l'outil d'inventaire.

```
                          Internet
                              │
                        [ FW-EXT ]
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   [ WEB-PUB ]          [ MAIL-RELAY ]        [ VPN-GW ]
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                        [ FW-INT ]
                              │
   ┌──────────────┬───────────┼───────────┬──────────────┐
   │              │           │           │              │
[ APP-01 ]   [ DB-01 ]   [ FILE-01 ]  [ DC-01 ]    [ SAUV-01 ]
                              │
                     [ segment postes ]
```


**Informations complémentaires** :

```
· L'outil d'inventaire compte 214 machines. Le schéma en montre 8.
· Le site de Bordeaux a été ouvert en 2023.
· Une migration de messagerie vers un service en ligne a eu lieu en 2024.
· MAIL-RELAY existe toujours dans l'inventaire.
· L'auteur du schéma a quitté l'organisation en 2022.
```


## A.2 Les questions

| # | Question |
|---|---|
| 1 | Appliquez les sept passes. Que produisez-vous ? |
| 2 | Combien de zones, et lesquelles sont réellement matérialisées ? |
| 3 | Que manque-t-il, et pourquoi ? |
| 4 | Quels éléments ont probablement changé depuis mars 2021 ? |
| 5 | Quelles **trois questions** posez-vous, et à qui ? |
| 6 | Quatre anomalies sont insérées dans le dossier. Lesquelles ? |

## A.3 Corrigé — les sept passes

**① LES ZONES** — Trois apparentes : extérieur, une zone entre les deux pare-feu, l'interne. **La seconde frontière existe** — c'est `FW-INT` — ce qui est rare et bon signe.

⚠️ **Mais** : rien ne matérialise de frontière **à l'intérieur** de la zone interne. `DC-01`, `DB-01` et le segment des postes semblent joignables entre eux. §24.1.

**② L'ENTRÉE** — Trois entrées dessinées : web, messagerie, accès distant. **Une quatrième n'est pas dessinée : l'administration** — §27.3. Et une cinquième, invisible : les postes eux-mêmes, qui ne figurent que comme « segment postes » sans détail.

**③ LES DONNÉES** — `DB-01` et `FILE-01` sont dessinés. Les copies ne le sont pas : réplicas, environnements de recette, exports, et depuis 2024 **les données de messagerie chez un fournisseur** — §32.2.

**④ L'IDENTITÉ** — `DC-01` est dessiné, **relié à rien**. Cas canonique du §1.1. Et depuis la migration de 2024, une question nouvelle : **la messagerie en ligne s'authentifie-t-elle contre `DC-01`, ou possède-t-elle ses propres identités ?**

**⑤ LES FLUX** — Une requête externe suit les étapes du §29.1. Aucun des sept flux invisibles n'est représenté.

**⑥ LES RUPTURES** — Au moins six, dont trois invisibles :

| Composant | Rupture ? | Visible ? |
|---|---|---|
| `FW-EXT`, `FW-INT` | Oui, sauf redondance non dessinée | ✅ |
| `APP-01`, `DB-01` | **Oui**, uniques | ✅ |
| `VPN-GW` | Oui, pour les nomades | ✅ |
| Résolution de noms | **Oui** | ❌ |
| `DC-01` | **Oui**, unique | ✅ dessiné, ❌ non relié |
| Certificats | **Oui**, à date connue | ❌ |

**⑦ L'INVISIBLE** — Onze éléments manquants (§3.4), plus quatre propres au dossier : **le site de Bordeaux**, ouvert deux ans après le schéma · **le service de messagerie en ligne** de 2024 · **les 206 machines** que l'inventaire connaît et que le schéma ignore · **les prestataires**.

## A.4 Corrigé — les quatre anomalies insérées

| # | Anomalie | Ce qu'elle révèle |
|---|---|---|
| **1** | **`MAIL-RELAY` existe encore dans l'inventaire après la migration de 2024** | Un composant **construit, dessiné, et devenu inutile** — mais toujours exposé. C'est un actif zombie, encore joignable depuis Internet |
| **2** | **Le site de Bordeaux n'est pas sur le schéma** | Le schéma date de 2021, le site de 2023. **Ce n'est pas une erreur, c'est une péremption** — §50.4 |
| **3** | **8 machines dessinées contre 214 inventoriées** | Le schéma est une vue logique de rôles, pas de machines — §3.1. Mais l'écart de 206 n'est documenté nulle part |
| **4** | **`DC-01` est unique et relié à rien** | Deux problèmes en un : un point de rupture majeur, et l'invisibilité universelle de l'annuaire |

⚠️ **L'anomalie 1 est la plus discrète, et ses conséquences sont les plus larges.** Un relais de messagerie devenu inutile après une migration reste exposé sur Internet, n'est plus surveillé par personne, et **continue d'être corrigé au mieux par habitude**. C'est le cas d'école du décommissionnement inachevé, traité dans le volume Asset Management.

## A.5 Corrigé — les trois questions

**À qui, et lesquelles** — trois questions seulement, et le choix des destinataires compte autant que celui des questions.

| # | Question | À qui | Pourquoi celle-ci |
|---|---|---|---|
| **1** | *« `MAIL-RELAY` est-il encore utilisé, et est-il encore joignable depuis Internet ? »* | Exploitation | **Un composant exposé sans usage est le meilleur rapport risque/effort du dossier** |
| **2** | *« Comment administre-t-on ces machines, et depuis quel poste ? »* | Exploitation | §27 — le chemin le plus court vers la compromission totale n'est pas dessiné |
| **3** | *« Depuis la migration de 2024, les identités de la messagerie viennent-elles de `DC-01` ? »* | DSI ou responsable messagerie | §40.2 — la synchronisation d'identités est un point de fragilité récurrent d'une architecture hybride |

**Ce qu'on ne demande pas le premier jour**, et pourquoi :

| Question écartée | Motif |
|---|---|
| *« Pourquoi n'y a-t-il qu'un seul serveur applicatif ? »* | Elle sonne comme un reproche. Elle viendra, après avoir compris l'histoire — §4.4 |
| *« Pourquoi le schéma n'est-il pas à jour ? »* | Sans objet : aucun schéma ne l'est. §50.4 |
| *« Où est la documentation ? »* | Elle n'existe probablement pas, et la demander ne produit rien |

⚠️ **Avertissement sur les barèmes de ces trois cas**

Les barèmes qui suivent notent **des comportements, pas des réponses**. Ils récompensent le fait de poser la bonne question, de dater un schéma, de relever une absence — jamais le fait d'écrire exactement la même phrase que le corrigé.

**Conformément au §48.0** : sur les cas de conception, **plusieurs architectures sont défendables**. Une proposition qui diffère du corrigé et qui énonce clairement la contrainte privilégiée et la contrainte dégradée **obtient le plein barème**.

**Et conformément au principe d'hypothèse** : une identification de composant formulée avec certitude perd des points, même si elle est juste. **Ce qu'on note est la démarche, pas la chance.**

## A.6 Le barème

| Critère | Pts |
|---|---|
| Relever `MAIL-RELAY` comme zombie exposé | **20** |
| Relever l'absence de chemin d'administration | **20** |
| Dater le schéma et identifier les deux événements postérieurs | 15 |
| Identifier `DC-01` comme rupture, malgré l'absence de trait | 15 |
| Distinguer l'écart 8/214 comme choix de vue, pas comme erreur | 10 |
| Poser la question de la migration de messagerie | 10 |
| Formuler trois questions et pas dix | 10 |

**Élimination** : commencer par critiquer l'architecture avant d'avoir demandé son histoire — §4.4.

---
