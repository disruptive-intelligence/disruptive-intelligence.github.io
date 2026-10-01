---
title: Chapitre 26 — Le réseau étendu et les sites distants
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE IV — Les réseaux et les zones
  - index.md
---

## 26.1 Ce que la distance change

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

## 26.2 Les dépendances locales

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

## 26.3 Trois architectures de sites

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

## 26.4 Le lien lui-même

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
