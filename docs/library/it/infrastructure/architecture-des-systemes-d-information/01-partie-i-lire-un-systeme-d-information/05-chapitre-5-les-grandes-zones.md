---
title: Chapitre 5 — Les grandes zones
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE I — Lire un système d'information
  - index.md
---

## 5.1 Pourquoi on sépare

**Le principe**, et il est unique :

> **On sépare ce qui n'a pas le même niveau de confiance, ni les mêmes conséquences en cas de compromission.**

Le reste — les noms, les technologies, le nombre de zones — en découle largement.

**Ce qu'une séparation apporte, et ce qu'elle coûte** :

⚖️ **CONTRAINTE ET COÛT — la segmentation**

| Contrainte résolue | Coût introduit |
|---|---|
| Limiter la propagation d'une compromission | Des flux à ouvrir, documenter et maintenir |
| Contrôler ce qui traverse une frontière | Un dépannage plus difficile — « ça ne passe pas, mais où ? » |
| Appliquer des règles différentes par niveau de sensibilité | Une complexité qui croît avec le nombre de zones |
| Démontrer un cloisonnement en audit | **Un risque de contournement si les flux deviennent trop pénibles** |

⚠️ **Le dernier point est le plus mal anticipé** : une segmentation trop stricte produit des contournements — un compte partagé, un flux ouvert « temporairement », une machine à cheval sur deux zones. **Une zone contournée est pire qu'une zone absente**, parce qu'on croit qu'elle protège.

## 5.2 Les six zones de référence

🖼 **SCHÉMA 5.1 — Les six zones** · *Bandes concentriques ou empilées, du moins fiable au plus sensible, avec les frontières marquées.*

```
   ╔═══════════════════════════════════════════════════════╗
   ║  EXTÉRIEUR — Internet, partenaires, mobilité          ║
   ║  Confiance : aucune                                   ║
   ╠═══════════════════════════════════════════════════════╣
   ║  BORDURE — pare-feu, accès distant, publication       ║
   ║  Rôle : filtrer, contrôler ce qui traverse            ║
   ╠═══════════════════════════════════════════════════════╣
   ║  ZONE DÉMILITARISÉE — ce qui est exposé volontairement ║
   ║  Confiance : faible. Compromettable par conception    ║
   ╠═══════════════════════════════════════════════════════╣
   ║  INTERNE — postes, serveurs métier, données           ║
   ║  Confiance : moyenne. C'est là qu'est la valeur       ║
   ╠═══════════════════════════════════════════════════════╣
   ║  ADMINISTRATION — ce qui pilote tout le reste         ║
   ║  Confiance : maximale requise. **Rarement dessinée**  ║
   ╠═══════════════════════════════════════════════════════╣
   ║  INDUSTRIEL / SPÉCIFIQUE — contraintes inversées      ║
   ║  Confiance : à part. Autres règles — chapitre 28      ║
   ╚═══════════════════════════════════════════════════════╝
```


| Zone | Ce qu'on y trouve | Ce qui la caractérise |
|---|---|---|
| **Extérieur** | Ce qu'on ne maîtrise pas | Aucune confiance, aucune hypothèse |
| **Bordure** | Pare-feu, passerelles d'accès distant | **Exposée par conception** — chapitre 10 |
| **Zone démilitarisée** | Ce qui doit être joignable de l'extérieur | On suppose qu'elle **sera** compromise |
| **Interne** | Postes, serveurs, données | Le plus grand volume, la plus grande valeur |
| **Administration** | Postes d'administration, consoles, orchestration | **Sa compromission donne tout le reste** |
| **Industriel** | Automates, supervision | Priorités inversées — chapitre 28 |

**La zone d'administration est la plus importante et la moins dessinée.** C'est le chapitre 27, et c'est le principal angle mort des schémas.

## 5.3 Ce qui définit une frontière

Une zone n'est pas définie par un trait sur un schéma, mais par **ce qui doit être traversé pour passer**.

| Type de frontière | Ce qui la matérialise | Force | Ce qui la contourne |
|---|---|---|---|
| **Physique** | Réseaux distincts, sans lien | Maximale — et rare | Un support amovible · un portable branché aux deux |
| **Filtrage** | Un pare-feu entre deux segments | Forte, si les règles sont fines | Une règle trop large · un chemin oublié |
| **Segmentation logique** | Des segments distincts, routés | Moyenne — dépend du routage | Une route ajoutée sans filtrage |
| **Applicative** | Un mandataire inverse, une passerelle | Forte sur un protocole, nulle sur les autres | Tout ce qui n'emprunte pas ce protocole |
| **Déclarative** | *« C'est la DMZ »*, sans mécanisme | **Nulle** | Rien à contourner |

⚠️ **La dernière ligne est le piège de lecture le plus fréquent.** Sur beaucoup de schémas, une zone est dessinée sans qu'aucun mécanisme ne la matérialise réellement. **La question à poser devant toute frontière** : *qu'est-ce qui empêche de passer ?*

👁 **CE QU'IL FALLAIT OBSERVER** — reprenez le schéma 1.1. La zone démilitarisée est matérialisée par des pare-feu en haut, mais **rien n'est dessiné entre elle et le réseau interne**. Soit la frontière existe et n'est pas représentée, soit elle n'existe pas. Le schéma ne permet pas de trancher — et c'est la question la plus importante qu'on puisse lui poser.

## 5.4 Les composants à cheval

**Le cas le plus intéressant en lecture** : un composant qui appartient à deux zones.

| Exemple | Pourquoi il est à cheval | Ce que ça implique |
|---|---|---|
| Un mandataire inverse | Il reçoit de l'extérieur, appelle l'intérieur | **C'est sa fonction** — chapitre 12 |
| Un serveur de sauvegarde | Il atteint toutes les zones | Sa compromission donne accès à toutes les données |
| Un poste d'administration | Il pilote plusieurs zones | Chapitre 27 |
| Un serveur avec deux interfaces réseau | Souvent un contournement historique | **À interroger systématiquement** |
| Un poste portable d'intervenant | Il se branche successivement sur deux réseaux | **Un pont différé** — §28.5 |

**La règle de lecture** : tout composant à cheval sur deux zones est **soit une frontière assumée, soit une brèche**. Il n'y a pas de troisième possibilité, et la distinction se fait en demandant si c'était voulu.

⚠️ **Le cas de la sauvegarde mérite une remarque.** C'est le composant le plus transverse d'une architecture : il atteint tout, pour tout copier. **Sa compromission donne accès à l'ensemble des données de l'organisation, sans jamais toucher à un seul serveur de production.** Et il n'est presque jamais dans la zone d'administration.

🔭 **À RECONNAÎTRE — architectures de calcul intensif**

**① Ce que c'est.** Des architectures optimisées pour des **calculs massifs, souvent parallèles** : simulation, recherche, modélisation, apprentissage automatique à grande échelle.

**② Ce qui les rend différentes d'un système d'information de gestion** :

| | Système de gestion | Calcul intensif |
|---|---|---|
| Ce qui compte | Disponibilité, cohérence, sécurité | **Débit de calcul, interconnexion entre nœuds, débit de stockage** |
| L'unité de travail | Une transaction | **Un travail soumis, qui dure des heures ou des jours** |
| Le réseau | Relie des services | **Relie des nœuds qui calculent ensemble** — la latence entre eux est structurante |
| L'arrêt | Un incident | **Une file d'attente qui s'allonge** |

**③ Ce qu'il faut en retenir en architecture.** Une zone de calcul intensif obéit à d'autres priorités, comme le réseau industriel du §28.1 — **et pour les mêmes raisons de fond : ses contraintes ne sont pas celles du reste du système d'information.** Y appliquer les règles du système de gestion sans discernement produit les mêmes blocages.

**④ En réunion** : *« c'est sur le cluster de calcul »* → **une zone à part, avec ses propres règles. Qui l'administre ? Quels flux la relient au reste ?**

📚 **À approfondir ailleurs** : c'est un domaine à part entière, avec sa propre ingénierie.

## 5.5 Combien de zones, et pourquoi

**La question qui revient en conception** : *faut-il six zones ?*

| Nombre de zones | Quand c'est justifié | Ce que ça coûte |
|---|---|---|
| **2** — interne, extérieur | Aucun service publié, aucun actif à part | Presque rien |
| **3** — + DMZ | Un service est publié | Deux jeux de règles |
| **4** — + administration | Il y a des administrateurs distincts des utilisateurs | Des postes dédiés |
| **5** — + industriel ou spécifique | Un environnement aux contraintes inversées | Une autonomie à construire |
| **6 et plus** | Des entités, des sensibilités ou des obligations distinctes | **Une complexité qui croît vite** |

⚠️ **Le principe de la contrainte s'applique intégralement** : le nombre de zones ne se déduit pas de la taille. **Il se déduit du nombre de niveaux de confiance réellement différents.** Une organisation de deux mille personnes avec un seul métier et aucun service publié peut légitimement n'avoir que trois zones.

🔥 **SCÉNARIO — la zone existe sur le schéma, pas sur le réseau**

| Question | Réponse |
|---|---|
| Symptôme | Un audit demande la preuve du cloisonnement. Le schéma montre trois zones |
| Hypothèse naïve | « Le schéma fait foi » |
| Dépendance réelle | **Aucun équipement ne filtre entre deux d'entre elles.** Elles sont routées, pas filtrées |
| Ce que le schéma aurait dû montrer | Ce qui matérialise chaque frontière |
| Comment le vérifier en dix minutes | Depuis une machine de la zone A, tenter de joindre une machine de la zone B |

⚠️ **Ce test est le plus rentable du chapitre**, et il ne demande aucun outil : **une connexion réussie entre deux zones censées être séparées vaut tous les schémas du monde.**

## 5.6 🔴 FIL ROUGE — décembre 2025 : combien de zones ?

Amélie compte les zones du schéma 1.1 : trois — démilitarisée, interne, industriel.

**Elle vérifie auprès de Malik.** Il y en a **six**.

| Zone | Sur le schéma ? | Réalité |
|---|---|---|
| Extérieur | Implicite | — |
| Bordure | Les deux pare-feu | Correct |
| Zone démilitarisée | Oui | Correct |
| Interne | Oui | **En réalité trois segments** : serveurs, postes Lyon, postes Nantes |
| **Administration** | **Non** | Existe : un segment dédié, deux postes, un accès depuis Lyon uniquement |
| Industriel | Oui | Correct, mais **le lien de 2018 le traverse** |

**Deux découvertes.**

La zone interne du schéma en cache trois, dont deux sur des sites différents. Le schéma représente une frontière là où il y en a plusieurs.

La zone d'administration n'est pas dessinée **et elle est la plus sensible**. Amélie demande pourquoi.

> *« Parce que ce schéma, on le montre aux clients »*, répond Malik.

**Ce qu'Amélie note**, et qui est un principe de lecture à part entière :

> *Un schéma est fait pour quelqu'un. Celui-ci est fait pour rassurer un client. Il ne ment pas — il ne montre pas ce qui ne le regarde pas. Je dois savoir pour qui un schéma a été dessiné avant de le lire.*

→ La suite en 🔴 §6.6, avec les 620 postes qui ne sont sur aucun schéma.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est dans une autre zone » | Une séparation existe sur le schéma | **Qu'est-ce qui la matérialise ?** — §5.3 |
| « C'est cloisonné » | Idem | Testé depuis quand ? |
| « Le serveur a une patte dans les deux » | Deux interfaces réseau | **La frontière n'existe plus à cet endroit** |
| « La sauvegarde accède à tout » | Constat de fait | **C'est le composant le plus transverse — où est-il ?** |

---
