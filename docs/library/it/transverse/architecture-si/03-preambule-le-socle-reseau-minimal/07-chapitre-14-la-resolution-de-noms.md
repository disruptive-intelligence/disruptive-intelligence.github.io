---
title: Chapitre 14 — La résolution de noms
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

> **Un composant dont la disparition produit des effets particulièrement déroutants**, et l'un des moins dessinés.

## 14.1 À quoi ça sert

Traduire un nom en adresse. Rien de plus, et c'est un préalable à presque tout.

**Pourquoi ça existe.** Les adresses changent, et personne ne les retient. Le nom est un identifiant stable ; l'adresse est un détail d'implémentation. Cette indirection est ce qui permet de déplacer un service sans reconfigurer ses clients.

## 14.2 La séquence complète

🖼 **SCHÉMA 14.1 — Ce qui se passe réellement**

```
   Utilisateur saisit  www.exemple.fr
            │
            ▼
   ┌──────────────────┐
   │   RÉSOLVEUR      │  ← celui que le poste interroge (« récursif »)
   └────────┬─────────┘
            │
      ┌─────┴─────┐
      │ en cache ? │
      └─────┬─────┘
       ┌────┴────┐
      OUI       NON
       │         │
       │         ▼
       │    interroge les serveurs FAISANT AUTORITÉ
       │    pour ce nom, de proche en proche
       │         │
       │         ▼
       │    obtient l'adresse, et la MET EN CACHE
       │    pour la durée de vie annoncée
       │         │
       └────┬────┘
            ▼
        adresse
            │
            ▼
   Client ─────────► serveur
```


## 14.3 Les cinq notions qui suffisent à raisonner

| Notion | Ce qu'elle est | Pourquoi elle compte en architecture |
|---|---|---|
| **Résolveur récursif** | Celui que le poste interroge | **Sa panne arrête presque tout, en interne** |
| **Serveur faisant autorité** | Celui qui détient la réponse pour un nom | **Sa panne rend votre organisation injoignable de l'extérieur** |
| **Cache** | La réponse conservée un temps | Masque une panne, **puis l'aggrave d'un coup** |
| **Durée de vie** | Combien de temps la réponse est conservée | **Elle détermine le délai d'un changement d'adresse** |
| **Vue interne / vue externe** | Un même nom, deux réponses selon l'origine | Un service peut être atteint par deux chemins différents |

⚠️ **Deux pannes très différentes** que le mot « DNS » recouvre :

| Ce qui tombe | Qui est affecté | Symptôme |
|---|---|---|
| Le **résolveur récursif** | **Vos utilisateurs** | Plus rien ne fonctionne en interne |
| Le serveur **faisant autorité** | **Vos clients externes** | Votre organisation disparaît d'Internet, l'interne va bien |

**Confondre les deux conduit à chercher au mauvais endroit** — et c'est exactement le cas de synthèse B.

## 14.4 La durée de vie, et pourquoi elle décide d'une migration

**Le mécanisme, souvent mal compris** :

```
   Vous changez l'adresse d'un service à 10 h 00.
   La durée de vie annoncée est de 24 heures.

   10 h 00   ┃ nouvelle adresse publiée
             ┃
   10 h 05   ┃ un client qui n'a jamais résolu → nouvelle adresse ✅
             ┃ un client qui a résolu à 9 h 00 → ANCIENNE adresse ❌
             ┃
   Jusqu'à   ┃ des clients continuent d'aller à l'ancienne adresse
   le lende- ┃ ⚠️ L'ancien serveur doit rester en service
   main 9 h  ┃
```


⚠️ **La conséquence pratique** : **on ne coupe jamais l'ancien serveur le jour de la bascule.** Et si l'on prévoit une migration, on réduit la durée de vie **plusieurs jours avant** — sinon le changement met une journée à se propager, et personne ne sait quels clients sont passés.

## 14.5 Les deux vues, et le piège qu'elles créent

```
   VUE EXTERNE                       VUE INTERNE
   portail.exemple.fr → 203.0.113.7  portail.exemple.fr → 10.0.4.80
   (adresse du mandataire)            (adresse du serveur, en direct)

   → un client externe passe par le mandataire, et par ses contrôles
   → un poste interne va DIRECTEMENT au serveur
```


⚠️ **Ce que cela signifie en sécurité** : un contrôle placé sur le mandataire — authentification, inspection, journalisation — **ne s'applique pas aux accès internes**. C'est le §29.3, et c'est l'une des raisons pour lesquelles un dispositif placé en frontal couvre moins qu'on ne le croit — §44.4.

## 14.6 Ce qu'il fait à la donnée

Rien — il ne voit pas le contenu. Mais il voit **toutes les intentions** : chaque nom demandé, par qui, quand. C'est une source de journaux particulièrement riche.

## 14.7 S'il disparaît

L'essentiel des connexions établies à partir d'un nom échoue, et de façon déroutante : le réseau fonctionne, les serveurs fonctionnent, et rien n'est joignable.

📌 **Ce qui continue de fonctionner, et qu'il faut savoir** :

| Cas | Pourquoi la résolution n'est pas nécessaire |
|---|---|
| Une connexion vers une adresse écrite en dur | Il n'y a pas de nom à traduire |
| Une connexion déjà établie | La traduction a eu lieu avant |
| Un nom encore en cache | Le cache répond à la place du serveur |
| Un service découvert par un autre mécanisme | Découverte de service, configuration distribuée |
| Un client qui passe par un intermédiaire résolvant lui-même | Le mandataire fait la traduction |

🔥 **SCÉNARIO — panne progressive de résolution**

| Question | Réponse |
|---|---|
| Symptôme | À 9 h 15, deux signalements. À 9 h 40, quarante. À 10 h, tout le site |
| Hypothèse naïve | « Ça se dégrade, c'est probablement la charge » |
| Dépendance réelle | **Les caches expirent un par un.** La panne date de 9 h 00 |
| Ce que le schéma aurait dû montrer | Le résolveur, et combien il y en a |
| Comment le reconnaître | **Une panne qui s'aggrave par vagues sans cause apparente est très souvent une panne de résolution ou de certificat** |

🔥 **SCÉNARIO — un résolveur sur deux tombe**

| Question | Réponse |
|---|---|
| Symptôme | Certaines résolutions sont lentes. La plupart fonctionnent |
| Hypothèse naïve | « Le réseau est chargé » |
| Dépendance réelle | Les clients interrogent le premier serveur, attendent l'expiration du délai, puis basculent sur le second |
| Ce que le schéma aurait dû montrer | Que les deux résolveurs sont **configurés sur les postes**, et dans quel ordre |
| Concevoir différemment | Vérifier que les postes connaissent bien les deux, et non un seul |

⚠️ **Ce second scénario est fréquent et rarement diagnostiqué correctement.** Une redondance de résolution ne fonctionne que si les clients connaissent les deux serveurs. Beaucoup n'en connaissent qu'un — et la redondance existe sur le schéma sans exister en pratique. **Principe de preuve.**

## 14.8 Sur un schéma

**Presque jamais.** C'est l'exemple canonique du flux de dépendance du principe des trois flux.

⚠️ **La question à poser devant tout schéma** : *où est la résolution de noms, et combien y en a-t-il ?* Si personne ne sait répondre, vous venez d'identifier une dépendance non maîtrisée — et c'est fréquemment l'une des plus structurantes du système.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le DNS est sur les DC » | Les contrôleurs d'annuaire assurent aussi la résolution | **Alors une panne d'annuaire est aussi une panne de résolution** — deux dépendances en une |
| « C'est un problème de DNS » | Une résolution échoue | Récursif ou faisant autorité ? Interne ou externe ? |
| « On a baissé le TTL » | La durée de vie a été réduite | Depuis quand ? Une migration est-elle en cours ? |
| « Il faut créer une entrée » | Ajouter un nom | Dans quelle vue — interne, externe, ou les deux ? |

⚠️ **La première ligne est structurante** : quand la résolution est portée par les contrôleurs d'annuaire, une seule panne produit **deux effets qui n'ont apparemment aucun rapport** — plus d'authentification, et plus de résolution. Le diagnostic devient difficile.

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Désigner les services par un nom stable | **Une dépendance universelle et invisible** |
| Changer une adresse sans changer les configurations | Un délai de propagation lié aux caches |
| Distinguer vue interne et externe | Une double configuration à maintenir cohérente · **des contrôles qui ne s'appliquent pas partout** |
| Redonder | Efficace **uniquement si les clients connaissent les deux serveurs** |

🏭 **TROIS TAILLES** — Atelier Martin : la résolution est portée par le boîtier tout-en-un, **et c'est un point de rupture assumé**. HELIOMED : deux résolveurs internes, portés par les contrôleurs d'annuaire. Novaris : une infrastructure dédiée, **parce que porter la résolution sur les contrôleurs d'annuaire cumule deux pannes en une, ce qu'une organisation de cette taille ne peut pas se permettre**.

---
