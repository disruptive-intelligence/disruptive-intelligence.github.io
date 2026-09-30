---
title: Chapitre 6 — Le poste utilisateur
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

> Placé ici, en Partie I, parce que c'est là que commence la majorité des flux et la majorité des incidents — et qu'il ne figure sur presque aucun schéma.

## 6.1 Le grand absent

**Le réflexe de tout débutant** : *Internet → pare-feu → serveur*.

**La réalité, en volume** : dans une organisation ordinaire, la majorité écrasante des connexions part d'un poste **interne**, pas d'Internet. Et la majorité des compromissions y commence.

**Pourquoi il n'est jamais dessiné** :

| Raison | Effet |
|---|---|
| Il y en a des centaines | Les dessiner rendrait le schéma illisible |
| Ils sont considérés comme uniformes | **Ils ne le sont pas** — §6.3 |
| Ils appartiennent à un autre périmètre | Souvent gérés par une autre équipe |
| **Ils ne « produisent » rien** | Erreur : ils consomment tout, et ils accèdent à tout |

⚠️ **La conséquence de lecture** : sur un schéma sans poste, vous ne voyez ni le point de départ de la plupart des flux, ni la surface d'attaque principale. **C'est l'omission la plus lourde des schémas d'architecture.**

## 6.2 Ce qu'un poste contient et ce qu'il ouvre

🖼 **SCHÉMA 6.1 — Ce qu'un poste atteint**

```
                        [ services en ligne ]
                                  ▲
   [ Internet ] ◄───────────  [ POSTE ]  ───────────► [ serveurs internes ]
                                  │  │                  fichiers · applicatifs
                    stockage      │  └──► [ annuaire ]   messagerie · bases
                    amovible ◄────┘        (dépendance)
```


| Ce qu'il contient | Ce que ça implique |
|---|---|
| Des identifiants en mémoire | Une compromission donne accès à ce que l'utilisateur atteint |
| Des documents locaux | Souvent une copie de données sensibles |
| **Des sessions ouvertes** | Vers des services en ligne, **sans nouvelle authentification** |
| Des accès enregistrés | Mots de passe du navigateur, clés, jetons — §33 |
| Des logiciels non maîtrisés | Extensions, outils installés par l'utilisateur |

**Ce qu'il ouvre** : tout ce que son utilisateur a le droit d'atteindre — et **le poste ne fait aucune distinction entre un accès légitime et un accès détourné**.

⚠️ **La ligne des sessions ouvertes est celle qu'on sous-estime le plus.** Un second facteur d'authentification protège la connexion ; il ne protège pas une session déjà ouverte. **Un poste compromis hérite de toutes les sessions actives**, sans avoir à s'authentifier nulle part.

## 6.3 Les quatre types de postes

| Type | Où il est | Ce qui change |
|---|---|---|
| **Fixe interne** | Sur le réseau de l'organisation | Le cas de référence |
| **Nomade** | Partout | Il n'est plus derrière le pare-feu. **Il l'est parfois par un tunnel, parfois pas** |
| **Virtualisé** | Le poste est ailleurs, l'écran est ici | Les données ne quittent pas le centre. **Une dépendance forte au réseau** |
| **Non maîtrisé** | Poste personnel, poste de prestataire | **Le cas le plus mal traité** — §38.4 |

**Le poste nomade est celui qui casse le raisonnement en zones du chapitre 5.** Un poste hors des murs n'est plus dans la zone interne — mais il y accède.

🖼 **SCHÉMA 6.2 — Les deux chemins d'un poste nomade**

```
  A — TUNNEL COMPLET
      poste ══tunnel══► réseau interne ──► serveurs
                                       └─► Internet
      → tout le trafic remonte · les contrôles internes s'appliquent
      → le lien du siège porte tout le trafic Internet des nomades

  B — TUNNEL PARTIEL
      poste ══tunnel══► réseau interne ──► serveurs internes
      poste ──────────────────────────────► Internet (direct)
      → moins de charge sur le lien
      → ⚠️ le trafic Internet du poste n'est plus filtré ni journalisé
      → le poste est simultanément dans DEUX réseaux
```


⚠️ **Le mode B crée une situation que le chapitre 5 interdirait sur un serveur** : le poste est simultanément connecté au réseau interne et à Internet, **sans qu'aucun équipement ne s'interpose**. C'est un composant à cheval — §5.4 — et il y en a des centaines.

**La question à poser devant tout schéma** : *les postes nomades passent-ils par le même chemin que les postes internes ?*

🏭 **TROIS TAILLES — les postes**

| | Atelier Martin | HELIOMED | Novaris |
|---|---|---|---|
| Nombre | 35 | 620 | ≈ 11 000 |
| Nomades | 3 | 180 | ≈ 4 000 |
| Postes non maîtrisés | **Oui** — le gérant utilise son portable personnel | Prestataires, encadré | Encadré, avec accès dédié |
| Poste virtualisé | Non | Pour les prestataires uniquement | Pour plusieurs métiers |

⚠️ **Principe de la contrainte** : Atelier Martin n'a pas de poste virtualisé *parce qu'elle est petite* — elle n'en a pas **parce qu'aucune contrainte ne le justifie** : pas de prestataire distant, pas de données à confiner, pas de parc hétérogène à uniformiser. Une entreprise de 35 personnes avec des sous-traitants dans trois pays en aurait un.

## 6.4 Le poste dans les flux

Reprenons les trois familles du principe des trois flux, du point de vue du poste.

| Famille | Ce qui part du poste |
|---|---|
| **Métier** | Requêtes web, ouverture de fichiers, messagerie, impression |
| **Dépendance** | Résolution de noms · authentification à l'ouverture de session · validation de certificats · **obtention d'une adresse au démarrage** |
| **Exploitation** | Remontée d'inventaire · télémétrie de sécurité · télédistribution de logiciels · sauvegarde éventuelle |

**Le flux de dépendance le plus méconnu** : à l'ouverture de session, un poste interne interroge l'annuaire, applique des politiques, monte des lecteurs réseau, synchronise son horloge. **Si l'un de ces éléments manque, l'utilisateur constate un poste « lent » ou « bloqué »** — et le diagnostic est difficile parce qu'aucun de ces flux n'est sur le schéma.

🔥 **SCÉNARIO — l'ouverture de session prend cinq minutes**

| Question | Réponse |
|---|---|
| Symptôme | Les sessions s'ouvrent, très lentement. Uniquement sur un site |
| Hypothèse naïve | « Les postes sont vieux » |
| Dépendance réelle | **Un des flux d'ouverture attend l'expiration d'un délai** : un lecteur réseau injoignable, un contrôleur d'annuaire distant, une politique qui référence un serveur disparu |
| Ce que le schéma aurait dû montrer | Ce que fait un poste au démarrage — **jamais représenté** |
| Comment le reconnaître | **Une lenteur constante, à la seconde près, est un délai d'attente, pas une charge** |

⚠️ **Un indice de diagnostic utile, et rien de plus** : une lenteur **qui varie** oriente vers une question de charge · une lenteur **constante et reproductible, à la seconde près**, oriente vers un délai d'attente sur quelque chose d'injoignable.

📌 **Ce n'est pas une loi.** Une lenteur constante peut aussi venir d'un traitement systématiquement coûteux, d'une résolution de noms lente mais réussie, ou d'un chiffrement mal négocié. **C'est une piste à explorer en premier, pas une conclusion.**

## 6.5 🔬 Mini-lab 3 — Où commence le flux ?

**Objectif** — Reconstituer le point de départ réel des flux d'une organisation.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §6.1 à §6.4

**La situation** : une organisation de 400 personnes. Un incident est survenu — un rançongiciel a chiffré un serveur de fichiers. Le schéma d'architecture montre : Internet → pare-feu → zone démilitarisée → serveurs internes → serveur de fichiers.

❓ **Questions**

1. En regardant ce schéma, par où l'attaquant est-il entré ?
2. Qu'est-ce que le schéma ne permet pas d'envisager ?
3. Quelle est l'hypothèse la plus probable, statistiquement ?

---

**Corrigé**

**1.** Le schéma suggère une entrée par Internet, via la zone démilitarisée. C'est la seule voie qu'il représente.

**2.** Il ne permet pas d'envisager **le poste utilisateur**, qui n'y figure pas. Ni le poste nomade, ni le prestataire, ni le stockage amovible, ni la messagerie ouverte sur un poste.

**3.** L'hypothèse la plus probable est **le poste** : pièce jointe ouverte, identifiants dérobés, session détournée. Le serveur de fichiers a été atteint **avec des droits légitimes**, depuis l'intérieur.

**La leçon** : *un schéma qui ne montre pas les postes oriente le diagnostic vers la mauvaise hypothèse.* Ce n'est pas un défaut du dessin — c'est un défaut de lecture, si le lecteur oublie ce qui n'est pas dessiné.

## 6.6 🔴 FIL ROUGE — décembre 2025 : 620 postes invisibles

Amélie demande à Malik où sont les postes sur le schéma 1.1.

> *« Ils ne sont pas dessinés. Il y en a 620, ça n'aurait pas de sens. »*

**Elle pose alors trois questions**, et les réponses la surprennent :

| Question | Réponse |
|---|---|
| Combien de postes nomades ? | **180** — un tiers du parc |
| Comment reviennent-ils sur le réseau interne ? | Par un tunnel, vers la passerelle d'accès distant — **qui n'est pas sur le schéma non plus** |
| Y a-t-il des postes non maîtrisés ? | **Oui** — ceux des prestataires de l'infogérant, qui administrent les serveurs |

**La troisième réponse est celle qui compte.** Des postes qu'HELIOMED ne maîtrise pas ont un accès d'administration à ses serveurs. Ils ne figurent sur aucun schéma, dans aucun inventaire, et personne n'en connaît le nombre.

⚠️ **Et le tunnel de la deuxième réponse pose une question qu'Amélie ne sait pas encore formuler** : complet ou partiel ? — §6.3. Personne, chez HELIOMED, ne connaît la réponse en décembre 2025.

**Ce qu'Amélie note** :

> *Le schéma montre ce qui est à nous. Il ne montre ni ce qui vient de l'extérieur, ni ce qui appartient à d'autres — alors que c'est par là que passent les accès les plus puissants.*

**Ce que cet épisode annonce** : la question des postes de prestataires reviendra en septembre 2029 dans le volume Renseignement, quand un prestataire compromis fera l'objet d'une évaluation — et en mai 2030, quand un compte de prestataire de 2028, toujours actif, sera découvert dans une fuite.

→ La suite en 🔴 §7.5, avec la question qu'Amélie finit par poser à Claire.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « L'utilisateur a cliqué » | Un poste est peut-être compromis | **Ce qui compte n'est pas le clic, c'est ce que ce poste atteint** |
| « Ils sont en télétravail » | Postes nomades | **Tunnel complet ou partiel ?** — §6.3 |
| « C'est un poste perso » | Poste non maîtrisé | **Qu'atteint-il ? Avec quels droits ?** |
| « Le poste rame » | Lenteur | **Constante ou variable ?** La réponse oriente la recherche — elle ne la conclut pas |

---
