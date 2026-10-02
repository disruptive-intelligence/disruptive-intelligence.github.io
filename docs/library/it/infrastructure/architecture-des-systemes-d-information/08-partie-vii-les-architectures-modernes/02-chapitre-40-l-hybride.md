---
title: Chapitre 40 — L'hybride
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VII — Les architectures modernes
  - index.md
---

> **Un point de fragilité récurrent des architectures modernes**, et l'un des plus fréquents.

## 40.1 Ce qu'est une architecture hybride

Un système dont une partie est sur site et une partie chez un fournisseur, **avec des flux entre les deux**. C'est la situation de la quasi-totalité des organisations, et elle est rarement le résultat d'une décision unique.

⚠️ **C'est presque toujours un état de sédimentation**, pas un choix d'architecture : une application est passée en ligne, puis une autre, puis la messagerie — et personne n'a jamais dessiné l'ensemble.

## 40.2 Les trois liens, et leurs fragilités

🖼 **SCHÉMA 40.1 — Les trois liens d'une architecture hybride**

```
   ┌──────────────┐                        ┌──────────────┐
   │   SUR SITE   │                        │    CLOUD     │
   │              │  ① lien réseau         │              │
   │  [annuaire]──┼───────────────────────►│  [ services ]│
   │              │  ② synchronisation     │              │
   │  [postes]  ──┼───────────────────────►│              │
   │              │     d'identités        │              │
   │  [données] ──┼───────────────────────►│  [ copies ]  │
   └──────────────┘  ③ flux de données     └──────────────┘
```


| Lien | Ce qui le rend fragile |
|---|---|
| **① Réseau** | Souvent unique, parfois un simple accès Internet. **Sa perte coupe tout l'hybride** |
| **② Identités** | La synchronisation d'annuaire est un flux de dépendance critique. **Une panne bloque les authentifications côté cloud** |
| **③ Données** | Réplications, sauvegardes croisées, exports. **Le plus difficile à cartographier** |

## 40.3 Le lien d'identités, en détail

**Un composant particulièrement fragile, et presque jamais supervisé.**

```
   [ annuaire interne ]
            │
            │  un composant de synchronisation
            │  s'exécute quelque part — souvent sur UNE machine
            ▼
   [ fournisseur d'identité en ligne ]
            │
            ▼
   [ services en ligne ]
```


**Ce qui casse, par ordre de fréquence** :

| Cause | Symptôme | Délai |
|---|---|---|
| Le composant de synchronisation est arrêté | Les créations et suppressions ne remontent plus | **Invisible pendant des jours** |
| Son certificat ou son secret a expiré | Idem | Idem |
| La machine qui l'héberge a été migrée ou supprimée | Idem | Idem |
| Le lien réseau est coupé | Les authentifications échouent, si le mode est direct | Immédiat |

⚠️ **La première ligne produit un incident silencieux et grave** : un salarié qui part est désactivé dans l'annuaire interne, **et reste actif côté cloud**. Personne ne s'en aperçoit — jusqu'à un audit, ou pire.

🔥 **SCÉNARIO — tout fonctionne, personne ne peut se connecter**

| Question | Réponse |
|---|---|
| Symptôme | L'annuaire interne répond. Les services en ligne répondent. **Les nouveaux mots de passe ne fonctionnent pas** |
| Hypothèse naïve | « Les utilisateurs se trompent » |
| Dépendance réelle | **Le composant de synchronisation est arrêté depuis trois jours** |
| Ce que le schéma aurait dû montrer | Ce composant — il n'est presque jamais dessiné |
| Comment le reconnaître | **Les anciens mots de passe fonctionnent, les nouveaux non.** C'est signé |
| Concevoir différemment | Superviser le composant **et la fraîcheur de la synchronisation**, pas seulement son état |

## 40.4 La question à poser à toute architecture hybride

> **Que peut-on faire si le lien tombe ?**

| Réponse | Ce qu'elle révèle |
|---|---|
| Rien des deux côtés | Une dépendance mutuelle totale — le pire cas |
| Le local fonctionne, le cloud non | Le cas courant |
| Le cloud fonctionne, le local non | **Fréquent et rarement anticipé** : les postes nomades vont bien, le siège est bloqué |
| Les deux fonctionnent en autonomie | Rare, et coûteux à obtenir |

**Comme au §26.1, personne ne connaît la réponse**, parce que personne n'a coupé le lien pour voir.

## 40.5 Trois architectures hybrides

```
  A — EXTENSION SIMPLE
      [ sur site ] ══lien══► [ quelques services en ligne ]
      → identités synchronisées · données majoritairement sur site
      → si le lien tombe : le sur site continue, le cloud est isolé

  B — BASCULE PROGRESSIVE
      [ sur site : legacy ] ◄══lien══► [ cloud : nouveau ]
      → les deux côtés portent du métier · flux dans les deux sens
      → si le lien tombe : LES DEUX sont dégradés
      → ⚠️ un état très répandu, et le plus fragile des trois

  C — CLOUD PRINCIPAL, SUR SITE RÉSIDUEL
      [ cloud : tout ] ◄══lien══ [ sur site : industriel, legacy ]
      → le cloud est autonome · le résiduel dépend du lien
      → si le lien tombe : seul le résiduel est isolé
```


⚠️ **Le mode B est un état de transition qui dure des années.** Il combine les contraintes des deux mondes et les avantages d'aucun — et il n'a été choisi par personne.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est en hybride » | Une partie est en ligne | **Quel mode ? Que se passe-t-il si le lien tombe ?** |
| « Les identités sont synchronisées » | Un composant réplique l'annuaire | **Où s'exécute-t-il ? Est-il supervisé ? Quelle fraîcheur ?** |
| « On a une interco » | Un lien privé existe | Redondé ? Et l'identité passe-t-elle par là ? |
| « Ça marche depuis chez moi » | Le nomade accède au cloud directement | **Il ne teste pas le lien du siège** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Adopter des services en ligne sans tout migrer | **Une architecture à deux mondes, avec les contraintes des deux** |
| Conserver les identités internes | **Un composant de synchronisation critique et invisible** |
| Garder des données sur site | Des flux de données à cartographier — le plus difficile |

---
