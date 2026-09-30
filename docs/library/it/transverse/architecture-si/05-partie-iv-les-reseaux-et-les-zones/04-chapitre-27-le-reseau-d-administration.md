---
title: Chapitre 27 — Le réseau d'administration
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE IV — Les réseaux et les zones
  - index.md
---

> **Invisible sur les schémas, décisif en sécurité.** L'un des deux chapitres les plus importants de la partie.

## 27.1 Pourquoi il existe

**Le constat de départ** : administrer un système suppose des accès **plus puissants** que ceux nécessaires pour l'utiliser.

| Ce qu'un utilisateur peut faire | Ce qu'un administrateur peut faire |
|---|---|
| Consulter ses données | Consulter toutes les données |
| Utiliser une application | Arrêter, modifier, contourner l'application |
| Ouvrir sa session | **Ouvrir n'importe quelle session** |
| — | **Effacer les traces de son passage** |

> **Le chemin d'administration est plus puissant que ce qu'il administre.** C'est pourquoi il justifie une zone à part.

⚠️ **La dernière ligne du tableau est celle qui change tout en réponse à incident** : un administrateur — ou quelqu'un qui a pris sa place — peut modifier les journaux. **C'est pourquoi les journaux d'administration doivent partir ailleurs, immédiatement** — §34.3.

## 27.2 Ce qu'on y trouve

🖼 **SCHÉMA 27.1 — Le chemin d'administration**

```
   [ poste d'administrateur ]
              │
              ▼  authentification renforcée
   ┌──────────────────────┐
   │  POSTE DE REBOND     │  ← unique point de passage
   │  (« bastion »)       │     journalisé, parfois enregistré
   └──────────┬───────────┘
              │
   ┌──────────┼──────────┬──────────────┐
   ▼          ▼          ▼              ▼
 serveurs   réseau   virtualisation   sauvegarde
                       (plan de
                        gestion)
```


| Composant | Rôle | Ce qui arrive s'il manque |
|---|---|---|
| **Poste dédié** | Un poste qui ne sert qu'à administrer | Un poste bureautique compromis donne l'administration |
| **Point de rebond** | Le passage unique et journalisé | Aucune trace centralisée des actions privilégiées |
| **Coffre de secrets** | Stocke et renouvelle les identifiants privilégiés | Des mots de passe partagés, jamais changés — §33 |
| **Segment isolé** | Non joignable depuis le réseau bureautique | Le rebond est atteignable par un poste compromis |

## 27.3 Les quatre chemins d'administration qu'on oublie

**Le rebond couvre les serveurs. Il ne couvre presque jamais ces quatre-là** :

| Chemin oublié | Pourquoi il échappe | Ce qu'il donne |
|---|---|---|
| **Le plan de gestion de virtualisation** | Interface web, souvent accessible depuis le bureautique | **L'accès aux disques de toutes les machines** — §23.4 |
| **Les interfaces d'administration matérielle** | Cartes de gestion à distance, sur un réseau à part | **Un accès en dessous du système** |
| **Les consoles des équipements réseau** | Administrées par une autre équipe | Le routage et le filtrage |
| **Les accès des prestataires** | Contractuels, hors processus | **Des postes que vous ne maîtrisez pas** — §38.4 |

⚠️ **Le deuxième est le plus méconnu.** Les cartes de gestion à distance permettent d'allumer, éteindre, réinstaller une machine et d'accéder à sa console **sans passer par son système d'exploitation**. Aucun contrôle placé dans le système ne les voit. **Elles sont sur un réseau à part, souvent oublié dans les revues.**

🔭 **À RECONNAÎTRE — PAM**

**① Qu'est-ce que c'est.** *Privileged Access Management* — l'ensemble des dispositifs qui **encadrent les accès privilégiés** : ceux qui permettent de tout faire.

**② Quel problème il résout.** Sans lui, les comptes d'administration sont partagés, leurs mots de passe ne changent jamais, et **rien ne dit qui a fait quoi**. Le §27.2 décrit les composants ; le PAM est le nom de leur assemblage.

**③ Ce qu'il apporte, selon les solutions** :

| Fonction | Ce qu'elle change |
|---|---|
| **Coffre de secrets privilégiés** | Le mot de passe d'administration n'est plus connu de personne — on l'emprunte |
| **Rotation automatique** | Il change après chaque usage · un départ n'oblige plus à tout changer à la main |
| **Contrôle d'accès** | Qui peut emprunter quel accès, quand, pour quelle durée |
| **Élévation à la demande** | On n'est pas administrateur en permanence, on le devient pour une tâche |
| **Traçabilité** | Qui a emprunté quoi, et quand |
| **Enregistrement de session** | Ce qui a été fait, rejouable |

⚠️ **La quatrième ligne est la plus structurante en architecture** : elle transforme un état permanent — *cette personne est administrateur* — en un **événement daté et motivé**. C'est ce qui rend l'accès privilégié auditable.

**④ Ce que cela change dans les flux.** Un composant de plus **sur le chemin de toute administration**. Et une dépendance : le §27.4 montre qu'un point de passage unique est aussi un point de rupture — **si le PAM est indisponible, on ne peut plus administrer**.

**⑤ Le coût.** Une solution à exploiter et à sécuriser fortement — **elle détient les clés du système d'information** · une adoption difficile, parce qu'elle ajoute des étapes à des gens pressés · **des accès de secours à prévoir**, et à protéger tout autant.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a un PAM » | **Tous les accès privilégiés y passent-ils ?** Il y a presque toujours des exceptions |
| « Les mots de passe sont dans le coffre » | **Sont-ils tournés ? Quelqu'un les connaît-il encore ?** |
| « On a un compte de secours » | Légitime et nécessaire. **Où est-il ? Qui y accède ? Est-il surveillé ?** |
| « Les sessions sont enregistrées » | **Qui relit les enregistrements, et dans quel cas ?** |

⚠️ **Le compte de secours mérite l'attention** : toute solution de PAM en a un, parce qu'il faut pouvoir intervenir quand elle est en panne. **C'est le compte le plus puissant de l'organisation, et il est souvent le moins surveillé.**

📚 **À approfondir ailleurs** : c'est le sujet du volume *Identités et accès* de cette collection.

## 27.4 Les trois configurations réelles

| Configuration | Description | Fréquence |
|---|---|---|
| **Aucune séparation** | On administre depuis son poste bureautique | **Fréquente**, surtout en petite structure |
| **Rebond sans isolation** | Un point de rebond existe, mais joignable depuis le réseau bureautique | Fréquente — **protection partielle** |
| **Isolation complète** | Poste dédié, segment isolé, rebond journalisé, coffre | Minoritaire |

⚠️ **La deuxième est trompeuse.** Un point de rebond joignable depuis un poste bureautique compromis ne protège pas : **il ajoute une étape, pas une frontière**. La question à poser : *depuis quel poste peut-on l'atteindre ?*

🔥 **SCÉNARIO — le poste d'un administrateur est compromis**

| Question | Réponse |
|---|---|
| Symptôme | Un administrateur a ouvert une pièce jointe |
| Hypothèse naïve | « Un poste de plus à réinstaller » |
| Dépendance réelle | **Ce poste atteint le rebond, donc tous les serveurs** — configuration 1 ou 2 |
| Ce que le schéma aurait dû montrer | Depuis quels postes le rebond est atteignable |
| Ce qui décide de la gravité | **L'administrateur utilise-t-il le même poste pour la messagerie et l'administration ?** |

🔥 **SCÉNARIO — on ne peut plus administrer pendant l'incident**

| Question | Réponse |
|---|---|
| Symptôme | Compromission en cours. **Le rebond est dans le périmètre suspect** |
| Hypothèse naïve | « On se connecte quand même, il faut agir » |
| Dépendance réelle | **S'y connecter expose des identifiants privilégiés à l'attaquant** |
| Ce que le schéma aurait dû montrer | Un chemin d'administration de secours, hors du périmètre courant |
| Concevoir différemment | **Prévoir un accès de secours** — c'est une décision d'architecture, prise des années plus tôt |

⚠️ **Ce second scénario est celui qu'on découvre en crise**, et il n'a pas de solution improvisée. C'est le §45.4.

## 27.5 Pourquoi il n'est jamais dessiné

| Raison | Réalité |
|---|---|
| Il ne sert pas le métier | Vrai, et sans importance |
| Il alourdirait le schéma | Vrai |
| **Il révèle comment on entre partout** | **La vraie raison, souvent inavouée** — §5.5 |

⚠️ **La conséquence en lecture** : un schéma sans chemin d'administration **ne montre pas le chemin le plus court vers la compromission totale**. C'est une omission lourde de conséquences, et elle est très répandue.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On passe par le bastion » | Un rebond existe | **Depuis quel poste peut-on l'atteindre ?** |
| « Les admins ont un compte séparé » | Deux identités par personne | **Sur le même poste ? Alors la séparation est partielle** |
| « L'infogérant se connecte en VPN » | Un accès distant de prestataire | **Vers quoi ? Depuis quel poste ? Tracé comment ?** |
| « L'iLO/iDRAC est sur un autre réseau » | Interfaces de gestion matérielle isolées | **Qui peut atteindre ce réseau ?** C'est le chemin le plus puissant |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Empêcher qu'un poste bureautique compromis donne l'administration | **Un poste supplémentaire par administrateur** |
| Journaliser et tracer les actions privilégiées | Un volume de journaux et un dispositif à exploiter |
| Cloisonner les identités d'administration | Des identités et des mots de passe supplémentaires à gérer |
| Un point de passage unique | **Un point de rupture** : s'il tombe, on ne peut plus rien administrer |

🏭 **TROIS TAILLES** — Atelier Martin : aucune séparation, **et c'est un risque assumé faute de moyens** — l'unique informaticien administre depuis son poste. HELIOMED : segment dédié, deux postes, accès depuis Lyon uniquement. Novaris : rebond avec enregistrement de session, coffre de secrets, **parce que 180 personnes ont des droits d'administration et qu'une traçabilité individuelle est exigée**.

---
