---
title: Chapitre 35 — Du serveur au service
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

> Le chapitre qui transforme une lecture technique en décision métier.

## 35.1 Ce qu'est un service

> **Un service est ce qui produit une valeur pour l'organisation.** Il ne correspond à aucun composant : il en mobilise plusieurs, et personne ne le voit sur un schéma technique.

**Exemple, chez HELIOMED** :

| Service métier | Composants mobilisés |
|---|---|
| **« Télésuivi HelioLink »** | Mandataire inverse · répartiteur · 3 serveurs web · applicatif · base · annuaire · résolution de noms · lien Internet · certificats |

**Neuf composants pour un service.** Et parmi eux, trois — annuaire, résolution, certificats — ne figurent sur aucun schéma.

## 35.2 Ce qui tombe si ceci tombe

**La question centrale du cours**, et la méthode pour y répondre.

🖼 **SCHÉMA 35.1 — L'arbre de dépendance d'un service**

```
                  SERVICE « Télésuivi »
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   [ accès ]        [ traitement ]     [ données ]
        │                 │                 │
  ┌─────┼─────┐     ┌─────┼─────┐          ▼
  ▼     ▼     ▼     ▼     ▼     ▼      [ base ] ◄── point de rupture
lien  mandat. répart. web×3 applic.
      ▲         ▲          ▲
      │         │          │
      └─────────┴──────────┴──── [ résolution ] ◄── point de rupture invisible
                                 [ annuaire ]   ◄── point de rupture invisible
                                 [ certificats ]◄── point de rupture différé
```


**La lecture donne quatre points de rupture**, dont **trois ne sont pas sur le schéma d'architecture** :

| Composant | Effet de sa perte | Visible ? |
|---|---|---|
| **Base de données** | Service arrêté, données potentiellement perdues | ✅ |
| **Applicatif** | Service arrêté | ✅ |
| **Résolution de noms** | Service injoignable | ❌ |
| **Annuaire** | Authentification impossible | ❌ |
| **Certificats** | Service refusé par les navigateurs, **à une date connue d'avance** | ❌ |

## 35.3 La superposition des flux

**La section la plus importante du chapitre**, et celle qui transforme la lecture d'une architecture.

**Ce que le lecteur croit voir** :

```
   User ──────► App ──────► DB
```


**Ce qui existe réellement** :

🖼 **SCHÉMA 35.2 — Dix flux superposés sur un même service**

```
                        [ résolution ]
                              ▲
                              ┊ ①
                              ┊
   [ poste ] ══②══► [ frontal ] ══③══► [ app ] ══④══► [ base ]
       ┊  ┊              ┊  ┊             ┊  ┊           ┊
       ┊  └──⑤──► [ annuaire ] ◄──⑤──────┘  ┊           ┊
       ┊                    ┊                ┊           ┊
       ┊                    ┊         ⑥──► [ secrets ]   ┊
       ┊                    ┊                            ┊
       └──⑦──┐              ┊              ┊             ┊
              ▼             ▼              ▼             ▼
          [ collecte de journaux ] ◄──────⑦─────────────┘
                                                         ┊
   [ administration ] ══⑧══► tous les composants         ⑧
                                                         ┊
   [ sauvegarde ] ◄══⑨══════════════════════════════════┘
                                                         ┊
   [ supervision ] ◄══⑩══════════════════════════════════┘
```


| # | Flux | Famille | Dessiné ? | Si interrompu |
|---|---|---|---|---|
| ① | **Résolution de noms** | Dépendance | ❌ | Le service devient injoignable |
| ② | **Requête utilisateur** | Métier | ✅ | Le service ne rend plus son objet |
| ③ | **Frontal vers application** | Métier | ✅ | Idem |
| ④ | **Application vers base** | Métier | ✅ | Idem |
| ⑤ | **Authentification** | Dépendance | ❌ | Plus personne ne peut entrer |
| ⑥ | **Secrets** | Dépendance | ❌ | L'application ne démarre plus — §33.3 |
| ⑦ | **Journaux** | Exploitation | ❌ | Le service continue · **on devient aveugle** |
| ⑧ | **Administration** | Exploitation | ❌ | On ne peut plus intervenir |
| ⑨ | **Sauvegarde** | Exploitation | ❌ | On ne peut plus restaurer |
| ⑩ | **Supervision** | Exploitation | ❌ | On ne sait plus si ça marche |

**Trois flux sur dix sont dessinés.** Et les sept invisibles se répartissent exactement selon le principe des trois flux : **trois dépendances dont la rupture arrête le service, quatre flux d'exploitation dont la rupture rend aveugle sans arrêter.**

## 35.4 La méthode, en cinq étapes

```
1. NOMMER LE SERVICE      du point de vue du métier, pas de la technique
2. SUIVRE LE FLUX MÉTIER  les douze étapes du §29.1
3. AJOUTER LES DÉPENDANCES résolution · identité · certificats
                           · secrets · temps
4. AJOUTER L'EXPLOITATION  journaux · supervision · sauvegarde
                           · administration
5. TESTER CHAQUE NŒUD     « si celui-ci tombe, le service rend-il
                            encore son objet ? »
```


⚠️ **Les étapes 3 et 4 distinguent une cartographie utile d'une cartographie décorative.** Sans elles, on obtient un arbre où tous les points de rupture sont déjà connus — et qui n'apprend rien.

**Le rendu attendu** — une page par service critique :

```
SERVICE : ..............................
FLUX MÉTIER      n composants : ........................
DÉPENDANCES      n composants : ........................
EXPLOITATION     n composants : ........................
POINTS DE RUPTURE   n dont n INVISIBLES sur le schéma
CE QUI N'EST PAS TESTÉ : ...............................
```


⚠️ **La dernière ligne est celle qui a le plus de valeur en comité.** Elle transforme une cartographie technique en constat décisionnel — **principe de preuve**.

## 35.5 Les trois niveaux de dégradation

| Niveau | Ce qui se passe | Exemple |
|---|---|---|
| **Arrêt** | Le service ne rend plus rien | Base indisponible |
| **Dégradation** | Le service fonctionne partiellement | Un serveur web sur trois : plus lent |
| **Cécité** | Le service fonctionne, on ne le voit plus | Collecte de journaux arrêtée |

**Les trois niveaux correspondent aux trois familles de flux de principe des trois flux** : métier → arrêt ou dégradation · dépendance → arrêt · exploitation → cécité. C'est ce qui rend la taxonomie utile.

⚠️ **Mais la correspondance n'est pas une loi, et il faut le dire.** La famille décrit **la fonction principale d'un flux, pas une garantie sur l'effet de sa panne**. Trois contre-exemples courants :

| Situation | Pourquoi elle sort du modèle |
|---|---|
| Un stockage saturé par les journaux | Un flux d'exploitation finit par **arrêter** le service |
| Une sauvegarde qui verrouille une ressource | Idem |
| Un outil de déploiement indispensable à un basculement | Un flux d'exploitation devient une dépendance en situation de panne |

**Et symétriquement** : certains flux métier disparaissent sans arrêter le service — une fonctionnalité secondaire, un export périodique.

> **La taxonomie est un modèle de raisonnement. Employez-la pour poser les bonnes questions, pas pour prédire des effets.**

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*On vous demande combien de temps le service « Télésuivi » peut rester indisponible. Que répondez-vous ?*
**Vous ne répondez pas — vous demandez d'abord de quoi il dépend.** Un service dont l'arbre comporte neuf composants dont trois invisibles n'a pas un seul délai de reprise : il en a autant que de causes possibles. La mauvaise décision évitée : **s'engager sur un délai de rétablissement calculé sur les seuls composants dessinés**, et découvrir en crise qu'une expiration de certificat ou une panne de résolution demande un délai tout autre.

---

## 🔬 Mini-lab 8 — Tracer six flux sur un même schéma

**Objectif** — Distinguer les trois familles sur une architecture unique.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 29 à 34

Sur le schéma 1.1, tracez et classez : ① une requête d'un client externe · ② une authentification d'un salarié interne · ③ une sauvegarde nocturne · ④ un journal du mandataire vers la collecte · ⑤ la mise à jour d'un certificat · ⑥ un export de données vers un tableur.

---

**Corrigé**

| # | Flux | Famille | Chemin | Visible sur le schéma ? |
|---|---|---|---|---|
| **①** | Requête client | **Métier** | Internet → pare-feu → mandataire → répartiteur → web → applicatif → base | **Partiellement** — la résolution et l'authentification manquent |
| **②** | Authentification interne | **Dépendance** | Poste → annuaire | ❌ **Aucun trait** |
| **③** | Sauvegarde nocturne | **Exploitation** | Base → serveur de sauvegarde → support | ❌ Le serveur est dessiné, **son chemin non** |
| **④** | Journal vers collecte | **Exploitation** | Chaque composant → collecte | ❌ **La collecte n'est pas sur le schéma** |
| **⑤** | Mise à jour de certificat | **Dépendance** | Autorité → mandataire, manuellement ou automatiquement | ❌ Rien |
| **⑥** | Export vers tableur | **Métier**, sortant | Base → applicatif → poste → **fichier local** | ❌ **Le poste n'est pas dessiné** |

**Le bilan : un flux sur six est représenté, et partiellement.**

**Les trois erreurs attendues**

1. **Classer ③ en dépendance.** La sauvegarde n'arrête pas le service : elle empêche de le restaurer. C'est de l'exploitation — principe des trois flux.
2. **Oublier ⑥.** Un export n'est pas un flux technique, c'est pourtant celui par lequel les données sortent du périmètre contrôlé — §32.2.
3. **Tracer ② vers le mandataire** au lieu de l'annuaire. L'authentification d'un salarié interne ne passe pas par le mandataire inverse : le chemin interne est plus court, et différemment contrôlé — §29.3.

---

## 🔬 Mini-lab 9 — Les points de rupture d'un service

**Objectif** — Construire un arbre de dépendance et identifier les ruptures invisibles.
**Durée** 35 min · **Difficulté** 🔴 avancé · **Prérequis** chapitre 35

**Le service** : « Commande en ligne » d'une organisation de distribution. Composants connus : deux serveurs web, un applicatif, une base répliquée, un mandataire inverse, un lien Internet redondé, un service de paiement externe.

❓ Construisez l'arbre, identifiez les points de rupture, classez-les par visibilité.

---

**Corrigé**

| Composant | Rupture ? | Visible ? | Nuance |
|---|---|---|---|
| Lien Internet | ⚠️ **Indéterminé** | ✅ | Annoncé redondé. **Deux liens du même opérateur, sur le même point d'entrée du bâtiment, ne redondent pas grand-chose** — *principe de preuve* |
| Mandataire inverse | ⚠️ **Indéterminé** | ✅ | **Un seul est mentionné** — à vérifier |
| Serveurs web ×2 | ❌ | ✅ | Sauf si sessions locales — §31.2 |
| **Applicatif** | ✅ **Oui** | ✅ | Unique |
| Base répliquée | ⚠️ | ✅ | **Le basculement a-t-il été testé ?** — §20 |
| **Résolution de noms** | ✅ **Oui** | ❌ | |
| **Annuaire ou fournisseur d'identité** | ✅ **Oui** | ❌ | |
| **Certificats** | ✅ **Oui**, à date connue | ❌ | |
| **Service de paiement externe** | ✅ **Oui** | ✅ | **Hors de votre maîtrise** — chapitre 38 |
| **Magasin de sessions** | ⚠️ | ❌ | **N'a pas été mentionné : existe-t-il ?** |

**Sept points de rupture ou incertitudes, dont quatre invisibles.**

**Les deux questions qui font la différence** :

1. *Le mandataire inverse est-il redondé ?* Il n'est mentionné qu'au singulier. Un seul mandataire annule la redondance de tout ce qui est derrière.
2. *Où sont les sessions ?* Si elles sont locales aux serveurs web, la redondance affichée ne protège pas l'utilisateur en cours de commande — §31.2. **La question n'a pas été posée dans l'énoncé, et c'est volontaire.**

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> ✓ suivre une **requête en douze étapes**, dont sept ne figurent sur aucun schéma ;
> ✓ que **six authentifications sur sept sont invisibles** pour l'utilisateur, et toutes dépendent d'un composant non dessiné ;
> ✓ décrire la **cascade progressive** d'une panne d'annuaire, et pourquoi elle est difficile à diagnostiquer ;
> ✓ que **l'emplacement de la session détermine ce que la redondance apporte réellement** ;
> ✓ suivre une **donnée en neuf étapes**, et savoir que la supprimer de la base ne la supprime que de la base ;
> ✓ qu'un **secret retiré du code source reste dans l'historique** — seule sa rotation le rend inoffensif ;
> ✓ que la **rupture d'un journal n'arrête rien et rend aveugle**, et que la conservation est souvent plus courte que le délai de détection ;
> ✓ construire l'**arbre de dépendance d'un service** en ajoutant les invisibles — l'étape qui distingue une cartographie utile d'une cartographie décorative ;
> ✓ que les **trois niveaux de dégradation** — arrêt, dégradation, cécité — correspondent exactement aux trois familles de flux.
>
> **Ce que vous ne savez pas encore** : comment appliquer tout cela de façon systématique à une architecture inconnue. C'est l'objet de la Partie VI, et de sa grille en sept passes.

---
