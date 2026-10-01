---
title: Chapitre 9 — Le routeur
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

## 9.1 À quoi ça sert

Faire communiquer des segments différents. Sans lui, deux segments coexistent sans se voir.

**Pourquoi ça existe.** Le niveau liaison ne sort pas du segment — §P.1. Dès qu'on découpe un réseau en plusieurs segments, il faut un composant capable de faire passer un échange de l'un à l'autre : c'est le routeur.

> **La formule qui distingue routeur et pare-feu, et qu'il faut retenir** :
> **Le routeur dit *où* ça va. Le pare-feu dit *si* ça a le droit.**

## 9.2 Comment il fonctionne, juste assez pour raisonner

```
   ①  Un paquet arrive, avec une adresse de destination
   ②  Le routeur consulte sa table :
         « pour atteindre 10.0.7.0/24, envoyer vers l'interface 2 »
   ③  Il modifie certains champs de transit
   ④  Il transmet
   ⑤  Le routeur suivant recommence
```


**Ce qui compte en architecture, et rien de plus** :

| Notion | Pourquoi elle compte en lecture |
|---|---|
| **Table de routage** | Elle décide du chemin. **Une entrée manquante rend une zone injoignable sans qu'aucun filtre ne l'interdise** |
| **Route par défaut** | Où va ce qui n'est pas connu. Généralement vers Internet |
| **Chemin asymétrique** | L'aller et le retour peuvent emprunter des routes différentes — **c'est ce qui casse certains pare-feu à état** |

⚠️ **La troisième ligne explique une famille entière d'incidents.** Un pare-feu qui suit l'état des connexions doit voir l'aller **et** le retour. Si le retour passe ailleurs, il refuse un trafic pourtant légitime — et le diagnostic est difficile parce que la configuration paraît correcte.

🔭 **À RECONNAÎTRE — BGP**

**① Qu'est-ce que c'est.** Un protocole qui permet à des systèmes de routage indépendants d'**échanger des informations de joignabilité** et d'appliquer des **politiques** sur les chemins retenus.

**② Quel problème il résout.** À grande échelle, on ne maintient pas à la main *« pour joindre ce réseau, passer par ce routeur »*. Et surtout : quand plusieurs chemins existent, **il faut pouvoir choisir selon d'autres critères que la distance** — un contrat, un coût, une préférence, une politique.

**③ Où on le rencontre.**

```
                    Entreprise
                        │
              ┌─────────┴─────────┐
              │                   │
          [ FAI A ]           [ FAI B ]
              │                   │
              └──── Internet ─────┘
```


| Contexte | Pourquoi BGP apparaît |
|---|---|
| **Deux fournisseurs d'accès** | Annoncer ses adresses aux deux, et choisir par où sortir et entrer |
| Interconnexion avec un opérateur | Échanger les réseaux joignables de part et d'autre |
| Grands centres de données | Routage interne à grande échelle |
| Liaison privée vers un fournisseur cloud | L'échange de routes se fait fréquemment ainsi |

**④ Ce que cela change.** Le chemin **n'est plus déterminé par votre seule configuration** : il résulte d'un échange avec des systèmes que vous ne contrôlez pas. Une annonce mal formée peut rendre une plage d'adresses injoignable — ou détourner du trafic.

> ⚠️ **Le point qui compte en architecture** : *BGP ne demande pas simplement quel chemin est le plus court. Les politiques comptent, et elles sont décidées de part et d'autre.*

**⑤ Le coût.** Une compétence rare · une configuration dont une erreur a des effets externes visibles · **une dépendance à ce que le partenaire annonce**.

**⑥ Le vocabulaire à reconnaître** : **ASN** — le numéro qui identifie un système autonome · **préfixe** — une plage d'adresses annoncée · **annonce de route** · **peering** — l'accord d'échange entre deux systèmes.

🗣 **En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est en BGP avec les deux opérateurs » | **Multi-hébergement.** Que se passe-t-il si l'un tombe ? La bascule a-t-elle été testée ? |
| « On annonce notre préfixe » | Vos adresses sont visibles depuis Internet par ce chemin. **Qui peut modifier cette annonce ?** |
| « Ils ne nous annoncent plus la route » | Une destination est devenue injoignable **sans qu'aucun équipement ne soit en panne** |

📚 **À approfondir ailleurs** : les attributs de sélection de chemin, la sécurisation des annonces, la conception d'un routage de centre de données.

## 9.3 Trois architectures de routage

```
  A — ROUTEUR UNIQUE, ROUTE PAR DÉFAUT
      segments internes ──► [ routeur ] ──► Internet
      → simple · tout passe par un point · un point de rupture

  B — ROUTAGE INTERNE + SORTIE SÉPARÉE
      segments ──► [ routeur interne ] ──► [ pare-feu ] ──► Internet
      → le routage interne survit à une panne de la sortie
      → deux équipements, deux configurations

  C — MULTI-SITES
      site A ──► [ routeur A ] ══lien══ [ routeur B ] ◄── site B
                       └────► Internet          └────► Internet
      → chaque site sort localement, et joint l'autre par le lien
      → si le lien tombe, chaque site reste autonome pour Internet
      → mais pas pour les services hébergés dans l'autre site — §26
```


**La contrainte qui décide entre B et C** : *un site doit-il continuer à fonctionner si le lien vers le siège tombe ?* — et la réponse est presque toujours partielle, §26.1.

## 9.4 Ce qu'il fait à la donnée

Il l'achemine. Pour décider du chemin, il interprète les informations d'adressage réseau, et il modifie certains champs au passage — c'est le mécanisme normal du transit. **Il n'a pas besoin d'interpréter le contenu applicatif**, ce qui en fait un point de contrôle sur les trajets, pas sur les contenus.

## 9.5 S'il disparaît

Les segments deviennent des îlots. Chacun fonctionne, aucun ne se parle.

🔥 **SCÉNARIO — le routeur inter-sites tombe**

| Question | Réponse |
|---|---|
| Symptôme | Les postes de Nantes n'atteignent plus les serveurs de Lyon. Internet fonctionne à Nantes |
| Hypothèse naïve | « Les serveurs de Lyon sont tombés » |
| Dépendance réelle | Le lien · **et tout ce qui est centralisé à Lyon** : annuaire, applications, fichiers |
| Ce que le schéma aurait dû montrer | **Ce qui est local à Nantes, et ce qui ne l'est pas** — §26.2 |
| Concevoir différemment | Un contrôleur d'annuaire et une résolution de noms locaux |

⚠️ **C'est une panne qui *ressemble* à une panne applicative** : les machines répondent, mais pas à travers les segments. C'est l'un des cas où le diagnostic est le plus souvent orienté au mauvais endroit.

## 9.6 Sur un schéma

Représenté à la jonction de deux zones ou de deux sites. **Souvent fusionné avec le pare-feu** dans les petites organisations — un seul boîtier fait les deux, ce que le schéma ne dit pas.

⚠️ **Ce que cette fusion masque** : la question *« ce flux est-il permis, ou seulement possible ? »* — §3.2. Quand routeur et pare-feu sont un seul objet sur le schéma, on ne sait pas si un flux passe parce qu'il est autorisé ou parce que personne n'a écrit de règle.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est routé » | Un chemin existe entre les deux | **Routé ne veut pas dire autorisé.** Y a-t-il un filtre sur ce chemin ? |
| « Il n'y a pas de route » | La table ne connaît pas la destination | Est-ce un oubli, ou une décision ? |
| « Ça passe par le WAN » | Le trafic emprunte le lien inter-sites | Quelle latence ? Que se passe-t-il si le lien tombe ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Faire communiquer des segments séparés | Un point de passage supplémentaire à sécuriser |
| Choisir des chemins, en gérer plusieurs | Une configuration de routage à maintenir · **un diagnostic plus difficile** |
| Sortir localement par site | Autant de sorties à surveiller — §11 |

---
