---
title: Chapitre 11 — Le mandataire sortant
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

## 11.1 À quoi ça sert

Concentrer les accès des postes internes vers l'extérieur, en un point unique où l'on peut filtrer, journaliser et authentifier.

**Pourquoi ça existe.** Sans lui, six cents postes sortent chacun de leur côté à travers le pare-feu. On peut filtrer par adresse et par port — mais pas savoir *quel site* a été consulté, ni *par qui*, ni bloquer une catégorie de destinations. Le mandataire déplace le point de décision du niveau réseau au niveau applicatif.

## 11.2 Comment il fonctionne, juste assez pour raisonner

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

## 11.3 Deux architectures de sortie

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

## 11.4 Ce qu'il fait à la donnée

Il voit **toutes les destinations** consultées depuis l'organisation, et selon sa configuration, le contenu. C'est une source de journaux particulièrement riche sur le comportement des postes — chapitre 34.

📌 **Et c'est un point sensible en soi** : le journal d'un mandataire contient l'historique de navigation de chaque salarié, nominativement. Sa conservation et son accès relèvent d'obligations qui dépassent le cadre de ce cours.

## 11.5 S'il disparaît

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

## 11.6 Sur un schéma

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
