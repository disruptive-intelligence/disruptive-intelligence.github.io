---
title: Cas B — Le service qui tombe
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - index.md
---

> **Durée** 1 h 30 · **Livrable** : liste ordonnée des causes possibles, et vérifications
> **Prérequis** : chapitres 29 à 35, 43

## B.1 La situation

**Mardi 10 h 15.** Le service « Portail clients » est inaccessible depuis l'extérieur. Vous n'avez que le schéma 1.1 et quinze minutes avant le point de crise.

**Les faits rapportés** :

```
· Les clients externes obtiennent une erreur de connexion.
· Les salariés internes accèdent normalement au portail.
· La supervision est au vert sur les trois serveurs web,
  sur l'applicatif et sur la base.
· L'incident a commencé « vers 9 h 40 ».
· Aucune intervention n'était planifiée.
```


## B.2 Les questions

1. Que vous dit le fait que l'interne fonctionne et l'externe non ?
2. Listez les causes possibles, **par ordre de probabilité**.
3. Quelles vérifications, dans quel ordre, et en combien de temps ?
4. Que dit la supervision au vert, et que ne dit-elle pas ?

## B.3 Corrigé — ce que la dissymétrie révèle

**L'information la plus précieuse du dossier est que l'interne fonctionne.**

Elle élimine d'emblée tout ce qui est commun aux deux chemins :

| Éliminé | Pourquoi |
|---|---|
| Serveurs web | L'interne les atteint |
| Applicatif, base | Idem |
| Annuaire | L'authentification interne fonctionne |
| Segment serveurs | Joignable |

**Ce qui reste : ce qui est propre au chemin externe** — §29.3.

```
   CHEMIN EXTERNE          Internet → FW → mandataire → répartiteur → web
   CHEMIN INTERNE          poste → répartiteur → web
                                    ▲
                          la divergence est ici
```


## B.4 Corrigé — les causes, par ordre de probabilité

| # | Cause | Probabilité | Pourquoi ce rang |
|---|---|---|---|
| **1** | **Certificat expiré** sur le mandataire | **Élevée** | Cause fréquente, effet exactement conforme aux symptômes, **survient sans intervention** — §17 |
| **2** | **Résolution de noms externe** défaillante | **Élevée** | Un enregistrement public **modifié, supprimé, ou dont les serveurs faisant autorité ne répondent plus**. L'interne utilise une vue différente — §14 |
| **3** | Mandataire inverse en panne ou saturé | Moyenne | Sa panne n'affecte que l'externe — §12 |
| **4** | Règle de pare-feu modifiée | Moyenne | « Aucune intervention planifiée » n'exclut pas une intervention non planifiée |
| **5** | Lien Internet dégradé | Faible | Affecterait aussi la sortie des postes |
| **6** | Attaque en déni de service | Faible | Possible, à ne pas privilégier faute d'élément |

⚠️ **Les deux premières partagent une propriété qui explique leur rang** : elles **peuvent survenir sans que personne n'ait rien fait de visible ce jour-là**.

📌 **Une précision, parce que le mot « expiration » recouvre trois choses différentes en résolution de noms** :

| Ce qui expire | Effet |
|---|---|
| **La durée de vie d'une réponse en cache** | Le client redemande. **Si les serveurs faisant autorité répondent, rien ne change** |
| **L'enregistrement du nom de domaine lui-même** | Le nom cesse d'être délégué — le service devient injoignable de l'extérieur |
| **Un certificat** | Le client refuse la connexion, à l'heure inscrite dans le certificat |

⚠️ **Seules les deux dernières arrêtent un service.** La première est un mécanisme normal — elle ne devient un problème que si la réponse obtenue au renouvellement a changé, ou si les serveurs faisant autorité ne répondent plus.

## B.5 Corrigé — les vérifications, dans l'ordre

| Ordre | Vérification | Durée | Pourquoi ce rang |
|---|---|---|---|
| **1** | **Ouvrir le service depuis l'extérieur et lire l'erreur exacte** | 2 min | Une erreur de certificat, de nom ou de connexion **désigne directement une des trois premières causes** |
| **2** | Vérifier la date d'expiration du certificat du mandataire | 3 min | Coût nul, cause n° 1 |
| **3** | Résoudre le nom public depuis l'extérieur | 3 min | Cause n° 2 |
| **4** | État du mandataire : processus, charge, journaux depuis 9 h 30 | 5 min | Cause n° 3 |
| **5** | Journal du pare-feu : changement de configuration récent | 5 min | Cause n° 4 |

**Total : moins de vingt minutes**, et les trois premières vérifications couvrent les deux causes les plus probables pour huit minutes de travail.

⚠️ **L'erreur classique** : commencer par les serveurs web, parce qu'ils sont au centre du schéma et qu'on sait les vérifier. **Ils sont déjà éliminés par le fait que l'interne fonctionne.**

## B.6 Corrigé — ce que la supervision au vert dit et ne dit pas

| Elle dit | Elle ne dit pas |
|---|---|
| Les processus tournent | Que le service est rendu |
| Les machines répondent | Que le certificat est valide |
| La base accepte des connexions | Que le chemin externe fonctionne |
| Les indicateurs surveillés sont normaux | **Ce qui n'est pas surveillé** |

> **Une supervision au vert pendant un incident signifie que l'incident se produit là où l'on ne regarde pas.** C'est une information, pas une contradiction.

**Ce que l'incident révèle sur la supervision**, et qui est le vrai livrable du cas : **rien ne surveille l'expiration des certificats, ni la résolution du nom depuis l'extérieur.** Ce sont deux flux de dépendance — principe des trois flux — et ils ne sont ni dessinés, ni supervisés.

## B.7 Le barème

| Critère | Pts |
|---|---|
| Exploiter la dissymétrie interne/externe pour éliminer | **25** |
| Placer certificat et résolution en tête | **20** |
| Commencer par lire l'erreur exacte | 15 |
| Vérifications ordonnées par coût croissant | 15 |
| Expliquer ce que la supervision au vert signifie | 15 |
| Conclure sur ce qui n'est pas supervisé | 10 |

**Élimination** : commencer par redémarrer un serveur web.

---
