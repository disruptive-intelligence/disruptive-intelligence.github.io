---
title: Chapitre 17 — L'infrastructure de clés
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

## 17.1 À quoi ça sert

Émettre, publier et révoquer des certificats.

**Ce qu'un certificat fait exactement**, parce que la formulation courante est imprécise :

> Un certificat **lie une identité — ou un attribut — à une clé publique**, et cette liaison est attestée par une autorité au sein d'une chaîne de confiance.

⚠️ **Un certificat ne chiffre rien par lui-même.** Il permet à un protocole de vérifier à qui l'on parle ; le chiffrement de l'échange est ensuite assuré par le protocole. Un certificat peut aussi servir à signer sans qu'aucun chiffrement de transport n'intervienne.

## 17.2 La chaîne de confiance, en une image

```
   [ AUTORITÉ RACINE ]        ← son certificat est INSTALLÉ sur les machines
            │                    C'est ce qui fonde toute la confiance
            ▼
   [ AUTORITÉ INTERMÉDIAIRE ] ← elle signe au quotidien
            │                    La racine reste hors ligne
            ▼
   [ CERTIFICAT DU SERVEUR ]  ← présenté au client

   Le client vérifie : ce certificat est-il signé par une autorité
   à laquelle JE fais confiance ?
        ├── OUI  ──► accepté
        └── NON  ──► avertissement, ou refus
```


⚠️ **Le point qui décide de tout** : *à quelles autorités le client fait-il confiance ?* Un navigateur fait confiance à une liste préinstallée d'autorités publiques. **Une machine de votre organisation fait en plus confiance à votre autorité interne, si vous l'y avez déployée.**

**D'où la formulation exacte** : un certificat émis par une autorité privée n'est reconnu que par **les systèmes qui font confiance à cette chaîne** — vos machines si vous l'y avez déployée, celles d'un partenaire à qui vous l'avez transmise, et **aucune machine que vous ne contrôlez pas si vous ne l'avez pas fait**.

## 17.3 La révocation, et pourquoi elle est le maillon faible

**Le problème** : un certificat a une date d'expiration. Que faire s'il faut l'invalider **avant** ?

```
   ①  L'autorité publie une liste de certificats révoqués
   ②  Le client la télécharge, ou interroge un service dédié
   ③  Il vérifie que le certificat présenté n'y figure pas

   ⚠️  Que se passe-t-il si l'étape ② échoue ?
        ├── mode strict   : le client REFUSE  → indisponibilité
        └── mode souple   : le client ACCEPTE → la révocation ne sert à rien
```


⚠️ **Le comportement varie fortement selon le client, le mécanisme et la configuration.** Certains refusent, beaucoup acceptent, d'autres ne vérifient pas du tout ; des mécanismes récents améliorent la situation en faisant transmettre l'état de révocation par le serveur lui-même.

> **Ce qu'il faut en retenir en architecture** : **on ne peut pas supposer qu'une révocation sera effective partout et immédiatement.** Ce n'est pas un mécanisme inutile, c'est un mécanisme dont l'effet dépend de choses que vous ne contrôlez pas.

📌 **Ce que cela impose en conception** : ne pas compter sur la révocation seule. **Des certificats de courte durée** réduisent la fenêtre d'exposition sans dépendre d'un mécanisme fragile — au prix d'un renouvellement fréquent, donc automatisé.

🔭 **À RECONNAÎTRE — HSM**

**① Qu'est-ce que c'est.** Un équipement matériel dédié qui **protège des clés cryptographiques et exécute les opérations qui les utilisent**.

**② Quel problème il résout.** La question fondamentale de tout ce chapitre :

> ### Où vit réellement la clé privée ?

Si elle est dans un fichier sur un serveur, **quiconque accède à ce serveur — ou à ses sauvegardes — l'obtient**. Le concept architectural du HSM n'est pas son fonctionnement cryptographique interne, c'est celui-ci :

> **La clé sensible peut être *utilisée* sans jamais être *exportée* comme un simple fichier.**

L'application demande une signature ou un déchiffrement ; l'équipement l'exécute et renvoie le résultat. **La clé ne sort pas.**

**③ Où on le rencontre.** À la racine d'une autorité de certification interne · pour signer du code ou des micrologiciels · dans les traitements de paiement · partout où une clé compromise aurait des conséquences irréversibles.

**④ Ce que cela change.** Une dépendance nouvelle : **si l'équipement est indisponible, les opérations qui en dépendent échouent**. Et une question de sauvegarde qui n'a pas de réponse simple — une clé qu'on ne peut pas exporter ne se sauvegarde pas comme un fichier ; il existe des mécanismes de séquestre, et ils sont eux-mêmes sensibles.

**⑤ Le coût.** Un équipement onéreux · une exploitation spécialisée · **une cérémonie de clés** pour les opérations sensibles, avec plusieurs porteurs · une redondance qui doit être prévue dès l'origine.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « La racine est dans un HSM » | Bon signe. **Est-il redondé ? Où est le séquestre ?** |
| « La clé est dans un fichier sur le serveur » | **Alors elle est aussi dans les sauvegardes** — §33.2 |
| « On signe avec le HSM » | **Que se passe-t-il s'il est indisponible au moment de signer ?** |

📚 **À approfondir ailleurs** : les niveaux de certification, les cérémonies de clés, l'intégration applicative.

## 17.4 S'il disparaît

Rien **immédiatement**. Puis, à chaque expiration de certificat, un service tombe — sans préavis et sans lien apparent avec la panne.

🔥 **SCÉNARIO — un service tombe sans que rien n'ait changé**

| Question | Réponse |
|---|---|
| Symptôme | Un service refuse les connexions à un horaire précis et net. Aucune intervention |
| Hypothèse naïve | « Une tâche planifiée a cassé quelque chose » |
| Dépendance réelle | **Un certificat a expiré.** L'heure exacte est le signe distinctif |
| Ce que le schéma aurait dû montrer | Rien — les certificats ne sont jamais dessinés |
| Comment le reconnaître | **Une panne à un horaire net, sans intervention, oriente vers une échéance** : expiration de certificat, rotation de secret, fin de durée de vie. La date exacte d'un certificat est inscrite dedans — elle n'est pas nécessairement minuit |
| Concevoir différemment | Surveiller les dates d'expiration · automatiser le renouvellement |

🔥 **SCÉNARIO — la chaîne fonctionne, la révocation non**

| Question | Réponse |
|---|---|
| Symptôme | Certains clients — souvent les plus stricts — refusent la connexion. La plupart l'acceptent |
| Hypothèse naïve | « Un problème sur ces postes » |
| Dépendance réelle | Le service de révocation est injoignable. Les clients en mode strict refusent |
| Ce que le schéma aurait dû montrer | Que la vérification de révocation est **un flux sortant, vers un service souvent externe** |
| Concevoir différemment | Vérifier que ce flux est autorisé dans le pare-feu — **il ne l'est pas toujours** |

⚠️ **Ce second scénario est un cas d'école** : une organisation bloque les sorties Internet non autorisées, et bloque au passage la vérification de révocation. Les certificats fonctionnent, jusqu'au jour où un client strict apparaît.

## 17.5 Ce qu'il faut en savoir pour raisonner

| Notion | Pourquoi elle compte |
|---|---|
| **Autorité** | Qui signe. Publique ou interne, et cela change tout |
| **Chaîne de confiance** | Si un maillon n'est pas reconnu, le certificat est refusé |
| **Expiration** | **La première cause d'incident liée aux certificats** |
| **Révocation** | Un mécanisme fragile · rarement testé · **au comportement variable selon les clients** |
| **Interne contre publique** | Un certificat privé n'est reconnu que par les systèmes qui font confiance à cette chaîne |
| **Inventaire des certificats** | **Presque jamais tenu** — et c'est ce qui produit les expirations surprises |

## 17.6 Sur un schéma

Jamais. Les certificats sont invisibles tant qu'ils fonctionnent.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le certif a expiré » | Une date est dépassée | **Combien d'autres expirent dans les 90 jours ?** Existe-t-il un inventaire ? |
| « On a notre propre PKI » | Une autorité interne existe | Sa chaîne est-elle déployée partout où elle doit l'être ? |
| « Il y a une erreur de certificat » | Le client refuse ou avertit | Expiration · chaîne non reconnue · **nom qui ne correspond pas** — trois causes distinctes |
| « On a mis un wildcard » | Un certificat couvre plusieurs noms | **Sa compromission affecte tous ces noms à la fois** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Émettre des certificats sans passer par un tiers | **Une hiérarchie à maintenir des années** · des expirations à suivre |
| Émettre pour des noms ou des usages non couverts par les autorités publiques | Une révocation qui doit fonctionner réellement, et qui est rarement testée |
| Authentifier des machines entre elles | Un inventaire des certificats — **presque jamais tenu** |
| Un certificat couvrant plusieurs noms | Une compromission de portée élargie |

🏭 **TROIS TAILLES** — Atelier Martin : **aucune infrastructure interne**, uniquement des certificats publics achetés. HELIOMED : une interne, **parce qu'elle doit émettre des certificats sur des noms internes que les autorités publiques ne délivrent pas, et parce qu'elle veut maîtriser sa propre chaîne de confiance**. Novaris : une hiérarchie à deux niveaux, pour cloisonner l'émission par entité.

---

## 🔬 Mini-lab 4 — Dix composants sans légende

**Objectif** — **Proposer le rôle le plus probable** de chaque composant, et dire ce qu'il faudrait vérifier.
**Durée** 30 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 8 à 17

```
                        Internet
                            │
                        ┌───┴───┐
                        │   A   │
                        └───┬───┘
              ┌─────────────┼─────────────┐
          ┌───┴───┐                   ┌───┴───┐
          │   B   │                   │   C   │
          └───┬───┘                   └───────┘
          ┌───┴───┐
          │   D   │
          └───┬───┘
        ┌─────┼─────┐
      [E1]  [E2]  [E3]
              │
          ┌───┴───┐        ┌───────┐        ┌───────┐
          │   F   │        │   G   │        │   H   │
          └───────┘        └───────┘        └───────┘
                          (aucun trait)    (aucun trait)

  Indices : C reçoit les courriels · G répond à des requêtes sur le port 53
            H répond sur les ports 389 et 636 · F contient les données
```


❓ **Pour chaque composant A à H** : proposez le rôle le plus probable, indiquez **ce qu'il faudrait vérifier pour le confirmer**, et dites lesquels sont probablement des points de rupture.

⚠️ **Le principe d'hypothèse s'applique** : un port, une position et un ensemble de connexions constituent un **faisceau**, pas une preuve. Un service peut écouter sur un port non standard, un composant peut cumuler deux rôles, et une position peut être trompeuse.

---

**Corrigé**

| Réf | Rôle **probable** | Sur quel faisceau | **À vérifier pour confirmer** | Rupture ? |
|---|---|---|---|---|
| **A** | Pare-feu | Position en bordure, tout converge | Est-ce un pare-feu seul, ou un boîtier cumulant routage et accès distant ? | Probable, sauf redondance non représentée |
| **B** | Mandataire inverse | Reçoit de l'extérieur, relaie vers l'intérieur | **Quel mode de terminaison** ? §12 · redondé ? | Probable, pour l'externe seulement |
| **C** | Relais de messagerie | L'indice fourni | Relaie-t-il vers un serveur interne, ou vers un service en ligne ? | Probable |
| **D** | Répartiteur de charge | Placé avant un groupe identique | La répartition se fait-elle bien ici, ou par la résolution de noms ? | **Probable** — §13 |
| **E1-E3** | Serveurs web | Trois exemplaires derrière un répartiteur | **Sur des hôtes différents ?** · **où vivent les sessions ?** — *principe de preuve*, §31.2 | **Indéterminé** |
| **F** | Base de données | L'indice, et la position en bas | Unique, ou répliquée sans que le schéma le montre ? | Probable, et le plus lourd de conséquences |
| **G** | Service de résolution de noms | Port 53 | Récursif, faisant autorité, ou les deux ? Combien y en a-t-il ? | Probable, **et invisible** |
| **H** | Service d'annuaire | Ports 389 et 636 | **Ces ports ne montrent que l'interrogation.** L'authentification passe par d'autres mécanismes — §16 | Probable, **et invisible** |

**Les quatre erreurs attendues** *(cohérentes avec le principe d'hypothèse)*

1. **Répondre avec certitude.** Aucune de ces identifications n'est établie. Un service peut écouter sur un port inhabituel, un composant peut cumuler deux rôles, une position peut être trompeuse. **Principe d'hypothèse.**
2. **Confondre A et B.** Les deux sont en bordure. La distinction se fait par ce qui les suit : A reçoit tout, B ne relaie que le web.
3. **Ne pas retenir G et H comme ruptures probables** parce qu'aucun trait ne les relie. **C'est le piège central** : leur absence de connexion ne signifie pas qu'ils sont isolés, mais que le dessinateur a renoncé à représenter des dépendances universelles.
4. **Conclure que E1-E3 constituent une redondance.** Rien ne l'établit : ils peuvent partager un hôte, et les sessions peuvent être locales. **Principe de preuve** — le schéma montre une *intention* de redondance.

**La leçon** : sur huit composants, **cinq sont des ruptures probables, dont deux ne sont reliés à rien** — et la seule redondance apparente n'est pas vérifiée.

---

## 🔬 Mini-lab 5 — Que se passe-t-il si on retire cette boîte ?

**Objectif** — Prévoir l'effet de la disparition d'un composant, y compris différé.
**Durée** 25 min · **Difficulté** 🟠 intermédiaire · **Prérequis** chapitres 8 à 17

Pour chacun, dire : **ce qui tombe · quand · et si l'utilisateur comprend**.

---

**Corrigé**

| Composant retiré | Ce qui tombe | Délai | L'utilisateur comprend-il ? |
|---|---|---|---|
| **Commutateur d'un étage** | Tout l'étage | Immédiat | ✅ Oui — « plus de réseau ici » |
| **Routeur inter-sites** | Les échanges entre sites | Immédiat | ⚠️ Partiellement — « le serveur de Lyon ne répond plus » |
| **Pare-feu en coupure** | Tout ce qui traverse | Immédiat | ⚠️ Non — tout paraît fonctionner localement |
| **Mandataire sortant** | L'accès Internet des postes | Immédiat | ❌ **Non** — « j'ai du réseau mais pas Internet » |
| **Mandataire inverse** | Les accès externes seuls | Immédiat | ❌ Non — l'interne fonctionne |
| **Répartiteur de charge** | **Tout le service**, malgré des serveurs sains | Immédiat | ❌ **Non** — c'est le plus contre-intuitif |
| **Résolution de noms** | Presque tout | **Différé** — les caches masquent, puis tout tombe | ❌ **Non — la panne la plus déroutante** |
| **Attribution d'adresses** | Les machines, une par une | **Différé de plusieurs heures ou jours** | ❌ Non — aucun lien apparent |
| **Annuaire** | Les authentifications, puis tout | Progressif | ⚠️ Partiellement |
| **Infrastructure de clés** | Un service à chaque expiration | **Différé de plusieurs mois** | ❌ **Non — la plus difficile à diagnostiquer** |

**Ce que le tableau enseigne, et qui est le cœur de la partie** :

> **Les composants dont la panne est la plus incompréhensible sont exactement ceux qui ne sont pas dessinés.**

Résolution de noms, attribution d'adresses, annuaire, certificats : quatre flux de dépendance, quatre pannes différées ou inexplicables, zéro représentation sur les schémas. C'est la règle principe des trois flux démontrée par ses conséquences.

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> ✓ ce que fait chacun des **dix composants d'infrastructure**, et surtout **ce qui se passe s'il disparaît** ;
> ✓ distinguer **routeur et pare-feu** — où ça va, et si ça a le droit ;
> ✓ distinguer **mandataire sortant et mandataire inverse**, deux fonctions opposées sous un même mot ;
> ✓ que le **répartiteur de charge crée un point de rupture en en résolvant un** ;
> ✓ que les **quatre composants les moins dessinés** produisent les pannes les plus incompréhensibles ;
> ✓ pour chaque composant, **la contrainte qu'il résout et le coût qu'il introduit** — et qu'ajouter n'est jamais gratuit ;
> ✓ qu'**aucun de ces composants n'apparaît par la taille de l'organisation**, mais par une contrainte identifiable ;
> ✓ **le socle réseau minimal** : deux niveaux d'adressage · sous-réseau et passerelle · sens d'établissement d'une connexion · traduction d'adresses · et que le modèle « adresse interne + traduction » n'est pas universel ;
> ✓ que **LDAP interroge et Kerberos authentifie** — trois mécanismes, pas un ;
> ✓ que **le chiffrement peut être terminé à trois endroits différents**, et que le schéma ne le dit jamais.
>
> **Ce que vous ne savez pas encore** : ce qui s'exécute sur les serveurs, et pourquoi on les sépare. C'est l'objet de la Partie III.

---
