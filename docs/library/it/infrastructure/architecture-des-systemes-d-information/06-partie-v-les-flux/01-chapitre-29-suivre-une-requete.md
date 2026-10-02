---
title: Chapitre 29 — Suivre une requête
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

## 29.1 Les douze étapes d'une requête ordinaire

Un salarié tape une adresse dans son navigateur. Voici ce qui se passe réellement — et **sur ces douze étapes, cinq figurent au schéma**.

🖼 **SCHÉMA 29.1 — Une requête, de bout en bout** · *Version graphique : douze étapes numérotées, les flux de dépendance en pointillé d'une autre couleur.*

```
 ①  Le poste doit traduire le nom en adresse
        poste ┄┄┄► [ résolution de noms ]        ← DÉPENDANCE
 ②  Réponse : une adresse
 ③  Le poste ouvre une connexion vers cette adresse
        poste ────► [ pare-feu ]                 ← peut refuser
 ④  Traversée du filtrage
        [ pare-feu ] ────► [ mandataire inverse ]
 ⑤  Négociation du chiffrement
        poste ┄┄┄► validation du certificat      ← DÉPENDANCE
 ⑥  Le mandataire termine la connexion et en ouvre une autre
 ⑦  Le mandataire demande une authentification
        [ mandataire ] ┄┄┄► [ annuaire ]         ← DÉPENDANCE
 ⑧  Le répartiteur choisit un serveur web
        [ répartiteur ] ────► [ web 2 ]
 ⑨  Le serveur web transmet à l'applicatif
        [ web 2 ] ────► [ applicatif ]
 ⑩  L'applicatif vérifie les droits, interroge la base
        [ applicatif ] ────► [ base ]
 ⑪  Dans cette architecture simplifiée, la réponse suit le chemin inverse
 ⑫  Chaque composant traversé écrit un journal
        chacun ┄┄┄► [ collecte ]                 ← EXPLOITATION
```


⚠️ **Sur l'étape ⑪** : le chemin de retour identique est vrai **dans cette architecture**, où chaque composant termine la connexion et en ouvre une autre. Ce n'est pas une règle générale — un routage asymétrique, un réseau de diffusion de contenu, un cache intermédiaire ou une architecture distribuée produisent des chemins de retour différents, **et c'est précisément ce qui rend certains diagnostics difficiles**.

## 29.2 Ce que le schéma d'architecture montre de tout cela

| Étape | Sur le schéma 1.1 ? |
|---|---|
| ①② résolution de noms | ❌ |
| ③④ pare-feu | ✅ |
| ⑤ certificat | ❌ |
| ⑥ mandataire inverse | ✅ |
| ⑦ authentification | ❌ |
| ⑧ répartiteur | ✅ |
| ⑨⑩ web, applicatif, base | ✅ |
| ⑫ journalisation | ❌ |

**Cinq étapes visibles sur douze.** Et les sept invisibles comprennent **les trois qui peuvent faire échouer la requête sans qu'aucun composant dessiné ne soit en panne**.

⚠️ **PIÈGE — le diagnostic par le schéma**
Face à une requête qui échoue, un lecteur qui ne connaît que le schéma cherche parmi cinq composants. Un lecteur exercé en examine douze — et commence souvent par ceux qui ne sont pas dessinés, parce que ce sont ceux dont la panne est la moins visible.

## 29.3 Le même service, quatre chemins différents

**C'est la section qui change la lecture d'un schéma**, et elle est rarement enseignée.

🖼 **SCHÉMA 29.2 — Quatre chemins vers le même service**

```
  ① UTILISATEUR EXTERNE
     Internet ──► [ FW ] ──► [ mandataire ] ──► [ web ] ──► [ app ]
     → passe par TOUS les contrôles
     → authentifié en amont · journalisé au mandataire · inspecté

  ② UTILISATEUR INTERNE
     poste ──────────────────────────────────► [ web ] ──► [ app ]
     → NE PASSE PAS par le mandataire
     → la résolution interne renvoie l'adresse du serveur — §14.5
     → aucun des contrôles du mandataire ne s'applique

  ③ UTILISATEUR NOMADE
     poste ══tunnel══► réseau interne ─────────► [ web ]
        OU
     poste ──► Internet ──► [ mandataire ] ──► [ web ]
     → DEUX chemins possibles selon la configuration
     → et souvent, personne ne sait lequel est emprunté

  ④ APPEL ENTRE SERVEURS
     [ autre application ] ─────────────────────► [ app ]
     → pas d'utilisateur · pas de mandataire
     → authentification par certificat ou par secret — §33
     → souvent le chemin le moins contrôlé de tous
```


| Chemin | Contrôles traversés | Journalisé où |
|---|---|---|
| ① Externe | Pare-feu · mandataire · application | Trois endroits |
| ② Interne | **Application seulement** | Un endroit |
| ③ Nomade | Variable, selon le chemin | Variable |
| ④ Serveur à serveur | **Souvent aucun** | Application, si elle le fait |

⚠️ **Ce que ce tableau impose en lecture** : un schéma dessine généralement le chemin ①. **C'est le mieux contrôlé, et c'est le moins fréquent en volume.** Les chemins ② et ④ portent l'essentiel du trafic réel, et ils traversent le moins de contrôles.

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous placez un dispositif de contrôle sur le mandataire inverse. Est-ce que tous les accès au service sont contrôlés ?*
**Non — seulement les accès externes.** Les postes internes atteignent souvent le serveur directement, sans traverser le mandataire, parce que la résolution interne leur donne l'adresse du serveur. La mauvaise décision évitée : **croire qu'un contrôle placé sur un chemin couvre tous les chemins**, et découvrir en incident que la compromission est passée par l'intérieur. C'est le chapitre 44.

## 29.4 Reconstituer un chemin quand on n'a pas le schéma

**La méthode, en quatre questions** — utilisable en réunion, sans document :

```
1. D'où part la demande ?     poste interne · Internet · autre serveur
2. Quel NOM est demandé ?     → quelle vue de résolution s'applique ?
3. Que répond ce nom          → l'adresse du mandataire, ou celle du serveur ?
   depuis CET endroit ?
4. Que traverse-t-on          → chaque frontière est un point de contrôle
   entre les deux ?              et un point de journalisation
```


⚠️ **La question 3 est celle qui révèle le plus.** Deux personnes qui demandent le même nom depuis deux endroits différents peuvent obtenir deux adresses différentes — et donc suivre deux chemins avec deux niveaux de contrôle. **Un schéma ne peut pas exprimer cela.**

## 29.5 Ce qui casse une requête, par étape

| Étape | Ce qui peut échouer | Symptôme caractéristique |
|---|---|---|
| ①② | Résolution indisponible ou mauvaise réponse | « Le site n'existe pas » · panne par vagues — §14.7 |
| ③④ | Règle de pare-feu, ou flux jamais ouvert | Délai d'attente, sans message |
| ⑤ | Certificat expiré, chaîne non reconnue | Avertissement de sécurité · **panne à un horaire net, sans intervention** — §17.4 |
| ⑥ | Mandataire arrêté ou saturé | Erreur immédiate, seulement de l'extérieur |
| ⑦ | Annuaire indisponible | Authentification refusée · cascade progressive — §16.3 |
| ⑧ | Tous les membres retirés par le contrôle de santé | **Le service tombe alors que les serveurs vont bien** — §13.2 |
| ⑨⑩ | Applicatif ou base indisponible | La page s'affiche, les actions échouent — §19.4 |

**Ce tableau est un outil de diagnostic à lui seul.** Le symptôme désigne l'étape, et l'étape désigne le composant — y compris quand il n'est pas dessiné.

---
