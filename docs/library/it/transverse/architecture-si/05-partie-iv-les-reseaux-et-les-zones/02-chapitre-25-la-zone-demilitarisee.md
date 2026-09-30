---
title: Chapitre 25 — La zone démilitarisée
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE IV — Les réseaux et les zones
  - index.md
---

> **Le concept le plus cité du domaine et le moins compris.**

## 25.1 Ce que c'est réellement

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

## 25.2 Le flux retour, et pourquoi il annule tout

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

## 25.3 Les trois erreurs de conception classiques

| Erreur | Ce qu'elle produit |
|---|---|
| **Pas de frontière 2** | La DMZ devient un tremplin vers l'interne |
| **Un composant de la DMZ joignant la base de données** | Le contournement complet de l'architecture en couches |
| **Un serveur à double interface**, une patte dans chaque zone | **La frontière n'existe plus** — §5.4 |

⚠️ **La troisième est la plus discrète, et ses conséquences sont les plus larges.** Une machine avec deux interfaces réseau, une dans chaque zone, **ne traverse aucun pare-feu**. Elle est le pare-feu — et elle n'en a ni les règles, ni les journaux, ni la surveillance. Sur un schéma, elle apparaît comme un composant ordinaire à cheval sur une frontière.

## 25.4 Trois architectures de publication

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

## 25.5 La passerelle d'interconnexion

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

### Les six choses que la passerelle matérialise

| # | Ce qu'elle établit | Pourquoi c'est une décision, pas une configuration |
|---|---|---|
| **1** | **Une frontière de confiance** | Les deux côtés n'ont pas le même niveau de confiance — c'est le §5.1 |
| **2** | **Une réduction des flux** | On n'ouvre pas les deux réseaux l'un à l'autre : on autorise ce qui est nécessaire |
| **3** | **Des fonctions intermédiaires** | Filtrage, mandataire, contrôle de contenu, terminaison — selon ce que l'échange exige |
| **4** | **Un point de concentration** | Excellent pour contrôler et observer · **et une dépendance forte** |
| **5** | **Une question de sens** | Un flux de A vers B n'implique en rien que B vers A soit autorisé — §P.3 |
| **6** | **Une question de protocoles** | Certaines architectures évitent même la communication directe, par un relais ou un échange contrôlé |

⚠️ **Le point 6 mérite un mot** : quand la différence de confiance est très forte, on renonce à la communication directe. Les données transitent par un relais qui les reconstitue, ou par un mécanisme d'échange où aucune connexion ne traverse la frontière. **C'est le modèle A du §28.4, appliqué au-delà de l'industriel.**

### Connectivité et contrôle de frontière ne sont pas la même chose

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

### Le principe à retenir

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

## 25.6 Ce que la DMZ ne protège pas

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

## 25.7 Sur un schéma

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
