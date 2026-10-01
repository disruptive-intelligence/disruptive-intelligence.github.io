---
title: Chapitre 16 — L'annuaire
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

> ⚠️ **Précision de vocabulaire, à poser avant tout.**
>
> **Service d'annuaire** est le concept général : un composant qui détient des identités, des groupes et des règles.
> **Active Directory** en est l'implémentation la plus répandue en entreprise, et c'est elle que ce chapitre décrit — parce qu'elle rend le concept concret.
>
> **Les propriétés décrites ici — contrôleurs, domaines, forêts, relations d'approbation, politiques — sont celles de ce modèle.** D'autres services d'identité existent et fonctionnent autrement : annuaires ouverts, fournisseurs d'identité en ligne, bases d'identités applicatives. Ne transportez pas ce modèle sur eux sans vérifier.
>
> ⚠️ **Et surtout** : **LDAP n'est pas l'authentification.** C'est un protocole d'interrogation et de modification d'annuaire. Dans un domaine Active Directory, l'authentification s'appuie principalement sur **Kerberos**, et la résolution de noms y joue un rôle structurant. Un schéma qui montre uniquement un flux LDAP vers l'annuaire ne montre donc pas tout le mécanisme d'authentification.

## 16.1 À quoi ça sert

Détenir les identités, les groupes et les règles, et répondre à deux questions : *qui es-tu* et *à quoi as-tu droit*.

**Pourquoi ça existe.** Sans lui, chaque application détient ses propres comptes. Un salarié qui part doit être retiré de trente endroits — et il le sera de vingt-huit. La centralisation résout le problème du cycle de vie des identités, et en crée un autre : **une dépendance universelle**.

## 16.2 Les trois mécanismes, et pourquoi il faut les distinguer

| Mécanisme | Ce qu'il fait | Sur un schéma |
|---|---|---|
| **LDAP** | Interroge et modifie l'annuaire : chercher un utilisateur, lister un groupe | Ports 389 / 636 |
| **Kerberos** | **Authentifie** : délivre un ticket qui prouve l'identité, sans renvoyer le mot de passe | Rarement dessiné |
| **Résolution de noms** | **Localise les contrôleurs** eux-mêmes | Jamais dessiné |

⚠️ **La troisième ligne explique un incident très fréquent** : dans un domaine Active Directory, un poste trouve ses contrôleurs **par la résolution de noms**. Si celle-ci est défaillante, **le poste ne trouve pas l'annuaire** — et le symptôme est une panne d'authentification, alors que l'annuaire fonctionne parfaitement.

> **Deux composants invisibles, et l'un dépend de l'autre.** C'est le chemin de diagnostic le plus difficile du cours.

## 16.3 La cascade d'une panne

```
   T+0        L'annuaire cesse de répondre
              │
   T+0        Les sessions ouvertes CONTINUENT      ← rien ne se voit
              │  (les tickets déjà délivrés restent valides)
              │
   T+minutes  Toute nouvelle authentification échoue
              │  · nouveaux accès aux partages
              │  · connexions applicatives
              │
   T+heures   Les tickets expirent · les sessions tombent une à une
              │
   Au premier Un utilisateur ne peut plus ouvrir sa session.
   redémarrage Il est bloqué devant son poste.
```


🔥 **SCÉNARIO — un contrôleur sur deux tombe**

| Question | Réponse |
|---|---|
| Symptôme | Certaines ouvertures de session sont lentes. La plupart fonctionnent |
| Hypothèse naïve | « Les postes sont lents » |
| Dépendance réelle | Les clients tentent le premier contrôleur, attendent l'expiration du délai, basculent |
| Ce que le schéma aurait dû montrer | Combien de contrôleurs, **et s'ils sont sur des hôtes différents** — *principe de preuve* |
| Concevoir différemment | Vérifier que la bascule est effective, et non seulement configurée |

## 16.4 Les notions qui suffisent à raisonner

| Notion | Pourquoi elle compte |
|---|---|
| **Contrôleur** | La machine qui répond. **Un domaine fonctionne avec un seul ; deux ou plus sont recommandés pour la disponibilité** — ⚠️ **Principe de preuve** : deux contrôleurs sur le même hôte ne constituent pas une redondance |
| **Domaine, forêt** | *(vocabulaire Active Directory)* Le périmètre d'une identité. Une acquisition en ajoute souvent un |
| **Relation d'approbation** | Ce qui permet à une identité d'un périmètre d'accéder à un autre — **et ce qui propage une compromission** |
| **Groupe** | L'unité de droit réelle. Les droits individuels restent minoritaires dans les modèles bien tenus |
| **Politiques** | Des règles appliquées automatiquement aux postes à l'ouverture de session |

⚠️ **Sur les relations d'approbation** : elles sont pratiques et elles ont une conséquence lourde. Une compromission dans le périmètre A peut devenir une compromission dans le périmètre B. **Sur un schéma, une flèche entre deux annuaires mérite toujours une question : dans quel sens, et avec quelle portée ?**

## 16.5 Ce qu'il fait à la donnée

Il ne la voit pas. Mais il **décide qui la voit** — ce qui en fait, avec la sauvegarde, l'actif dont la compromission a les conséquences les plus larges.

## 16.6 Sur un schéma

Dessiné comme une boîte, **sans aucun trait** — le cas du §1.1. Tout s'y connecte, rien ne le montre.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Ça tape l'AD » | Le composant s'authentifie contre l'annuaire | **Par quel mécanisme ?** LDAP pour interroger, ou Kerberos pour authentifier ? |
| « Il est dans le domaine » | La machine est jointe à l'annuaire | Alors elle dépend de lui **et de la résolution de noms** au démarrage |
| « On a un trust avec l'autre forêt » | Une relation d'approbation existe | **Dans quel sens ? Depuis quand ? Qui l'a demandée ?** |
| « Le DNS est sur les DC » | Deux fonctions sur les mêmes machines | **Une panne, deux effets sans rapport apparent** — §14 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Une identité unique pour de nombreux services | **Une dépendance universelle** · une compromission qui donne tout |
| Gérer les droits par groupes | Des groupes qui s'accumulent et ne se réduisent jamais seuls |
| Appliquer des politiques automatiquement | Un empilement difficile à auditer |
| Fédérer plusieurs périmètres | **Une compromission qui peut traverser la relation d'approbation** |

🏭 **TROIS TAILLES** — Atelier Martin : un contrôleur, **et c'est un point de rupture assumé faute de budget**. HELIOMED : deux contrôleurs, plus un annuaire hérité de l'acquisition de 2019 que personne n'a fusionné. Novaris : quatre forêts, **parce que sept acquisitions en quinze ans et trois fusions arbitrées comme trop risquées** — jamais parce que douze mille salariés.

---
