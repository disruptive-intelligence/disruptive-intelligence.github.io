---
title: Chapitre 24 — L'infrastructure adverse
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE V — Collecter
  - index.md
---

> ⚠️ **Avertissement de proportionnalité.** Ce chapitre décrit la compétence la plus technique et la plus séduisante du CTI. Elle est aussi celle dont le rapport entre le temps consacré et la valeur produite est le plus défavorable dans une organisation ordinaire. Lisez-le en gardant le §24.6 à l'esprit.

## 24.1 Ce qu'on appelle infrastructure

**Définition** : l'ensemble des ressources techniques employées par un adversaire pour conduire une opération.

| Élément | Ce qu'il permet | Durée de vie typique |
|---|---|---|
| Adresses | Hébergement, commande, exfiltration | Jours à mois |
| Noms de domaine | Résolution, apparence légitime | Semaines à mois |
| Certificats | Chiffrement, crédibilité | Mois |
| Hébergeurs et fournisseurs | Le socle | Longue |
| Empreintes de services exposés | Configuration caractéristique d'un outil | Variable |
| Adresses de messagerie | Enregistrement de domaines, contact | Variable |

**Ce qui rend cette matière analysable** : un adversaire réutilise. Créer une infrastructure coûte du temps et de l'argent (§16.3), et la réutilisation est la norme — ce qui permet de relier des éléments entre eux.

## 24.2 Le pivot

**Le principe** : partir d'un élément connu et découvrir les éléments qui lui sont liés.

```
Un domaine connu
     ├──► adresse de résolution ──► autres domaines résolvant vers elle
     ├──► certificat ──────────────► autres domaines couverts
     ├──► enregistrement ──────────► autres domaines du même déposant
     └──► empreinte de service ────► autres serveurs à configuration identique
```


**Ce que le pivot produit** : à partir d'un indicateur unique, un ensemble de plusieurs dizaines d'éléments potentiellement liés.

**Ce qu'il ne produit pas** : la certitude que ces éléments sont liés à la même opération. Chaque pivot est une **hypothèse de lien**, à évaluer comme telle.

⚠️ **PIÈGE — le pivot en chaîne**
Pivoter depuis un élément découvert par pivot multiplie l'incertitude. Au troisième niveau, on obtient couramment des centaines d'éléments dont la relation avec l'origine est purement hypothétique. **La règle** : un pivot au premier niveau est exploitable, au deuxième il demande une confirmation indépendante, au troisième il n'est plus qu'une piste.

## 24.3 Les sources d'enrichissement et leurs limites

| Source | Ce qu'elle apporte | Limite majeure |
|---|---|---|
| Résolution de noms passive | Historique des associations domaine/adresse | Couverture partielle, variable selon les régions |
| Journaux de certificats | Les noms couverts par un certificat public | Ne voit que le public |
| Registres d'enregistrement | Déposant, dates | **Largement anonymisés** aujourd'hui |
| Balayage d'Internet | Services exposés, configurations, empreintes | Photographie datée, souvent hebdomadaire |
| Bases de réputation | Signalements antérieurs | Faible qualité, forte circularité |
| Analyse de maliciel | Ce que le code contacte | Nécessite l'échantillon et la compétence |

**Le point commun de ces sources** : elles décrivent l'infrastructure **telle qu'elle était au moment de l'observation**. Une adresse associée à une activité malveillante en mars peut être parfaitement légitime en juin.

## 24.4 Durée de vie et conséquence sur vos blocages

**Le fait structurant** : l'infrastructure adverse est **jetable**. Elle est conçue pour être abandonnée.

| Conséquence | Explication |
|---|---|
| Un blocage vieillit mal | Une liste jamais purgée bloque des ressources devenues légitimes |
| Le rendement décroît vite | La majorité de la valeur d'un indicateur est consommée dans ses premiers jours |
| **Les faux positifs s'accumulent** | Adresses réattribuées, hébergement mutualisé, services légitimes compromis puis nettoyés |

✅ **BONNE PRATIQUE (P0) — la date d'expiration**
Tout indicateur d'infrastructure entre en blocage **avec une date de retrait**. Trente à quatre-vingt-dix jours selon le type, sauf réexamen explicite. Une liste de blocage sans mécanisme d'expiration devient, en dix-huit mois, une source majeure d'incidents pour les utilisateurs — et personne ne fait le lien.

⚠️ **Le cas de l'hébergement mutualisé** : bloquer une adresse hébergeant des centaines de sites légitimes pour un site malveillant est une erreur fréquente et coûteuse. Vérifiez ce qui d'autre réside à cette adresse avant tout blocage.

## 24.5 ⚠️ Faux positifs et contre-mesures adverses

| Piège | Mécanisme | Comment l'éviter |
|---|---|---|
| **Infrastructure partagée** | Hébergeur mutualisé, réseau de diffusion, service légitime | Vérifier la colocation avant blocage |
| **Service légitime détourné** | L'adversaire emploie une plateforme grand public | Le blocage casse un usage légitime |
| **Adresse réattribuée** | Le fournisseur a réattribué l'adresse à un autre client | Vérifier la fraîcheur de l'observation |
| **Empoisonnement délibéré** | L'adversaire associe son activité à des ressources légitimes | Ne jamais bloquer sans vérification |
| **Infrastructure de recherche** | Balayeurs académiques, moteurs de recherche, chercheurs | Identifier les acteurs connus |

**Le quatrième mérite un mot** : un adversaire averti sait que ses indicateurs seront collectés et diffusés. Y mêler délibérément des ressources largement utilisées produit des blocages dommageables chez ses cibles — et discrédite les listes qui les diffusent.

## 24.6 📌 Ce qui relève de l'analyse et ce qui relève de l'illusion

**La section la plus importante du chapitre.**

| Activité | Valeur pour une organisation ordinaire |
|---|---|
| Vérifier la colocation avant un blocage | **Élevée** — évite des incidents |
| Vérifier la fraîcheur d'un indicateur reçu | **Élevée** — cinq minutes |
| Pivoter au premier niveau sur un élément d'un incident propre | **Correcte** — peut élargir le périmètre d'une recherche |
| Pivoter au deuxième niveau | Faible, sauf besoin explicite |
| Cartographier l'infrastructure d'un acteur | **Très faible** — c'est le niveau 3 de l'attribution (§13.1) |
| Suivre l'évolution d'une infrastructure dans la durée | **Très faible** sans moyens dédiés |

**Le constat honnête** : cette matière est passionnante, visuellement gratifiante — les graphes de relations sont impressionnants — et elle produit peu de décisions dans une organisation ordinaire.

> **Le test à s'appliquer** : *ce pivot va-t-il changer une décision, ou vais-je produire un graphe ?*

**Ce qui justifie néanmoins d'en maîtriser les bases** : la vérification avant blocage, le contrôle de fraîcheur, et la capacité à élargir la recherche autour d'un incident propre. Ces trois usages ont une valeur réelle et demandent trente minutes de compétence, pas trois mois.

🎯 **ET MAINTENANT ?**
*Un dispositif sectoriel vous transmet une liste de 200 adresses associées à une campagne active. Que faites-vous avant de les bloquer ?*
**Réponse** : trois vérifications, une heure. *La fraîcheur* — quelle est la date de dernière observation ? Tout élément de plus de 90 jours est écarté par défaut. *La colocation* — combien de ces adresses hébergent également des services légitimes ? Un échantillon de vingt suffit à estimer le risque. *L'applicabilité* — vos actifs communiquent-ils déjà avec certaines d'entre elles ? Si oui, c'est une recherche à mener avant tout blocage, parce que la réponse peut être « oui, légitimement ». Puis vous bloquez ce qui reste, **avec une date de retrait**.

## 24.7 🔬 Mini-lab 7 — Un pivot, une découverte, deux faux positifs

**Objectif** — Conduire un pivot, évaluer la solidité des liens, et éviter deux blocages dommageables.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** §24.2 à §24.5 · **Livrable** liste de blocage argumentée
**Compétences validées** — ✔ évaluer un lien issu d'un pivot ✔ vérifier une colocation ✔ contrôler la fraîcheur ✔ distinguer analyse et illusion ✔ justifier un non-blocage

**Le point de départ** : lors d'un incident, un poste de votre organisation a contacté le domaine `sync-portal-update[.]net`. Ce domaine est confirmé malveillant.

**Les données d'enrichissement fournies** :

```
sync-portal-update[.]net
  └── résout vers 203.0.113.44  (observé du 12/03 au 02/05/2030)

203.0.113.44 — autres domaines ayant résolu vers cette adresse :
   ① sync-portal-update[.]net     12/03 → 02/05/2030
   ② client-sync-eu[.]net         14/03 → 29/04/2030
   ③ mail-portal-secure[.]net     11/03 → 05/05/2030
   ④ boutique-artisanale[.]fr     01/2019 → aujourd'hui
   ⑤ association-locale-92[.]org   06/2021 → aujourd'hui
   ⑥ cdn-assets-delivery[.]com     2017 → aujourd'hui

Certificat couvrant ① : couvre également ② et ③
Enregistrement de ① : déposant anonymisé, créé le 09/03/2030
Enregistrement de ② : déposant anonymisé, créé le 09/03/2030
Enregistrement de ③ : déposant anonymisé, créé le 10/03/2030
Enregistrement de ④ : déposant identifié, créé en 2019
Balayage de 203.0.113.44 : 341 sites hébergés
```


**Questions** : (a) Quels éléments retenez-vous, et avec quelle solidité ? (b) Que bloquez-vous ? (c) Quels sont les deux faux positifs, et que se passe-t-il si vous les bloquez ? (d) Quelle date de retrait ?

---

**Corrigé commenté**

**(a) Évaluation des liens**

| Élément | Lien avec ① | Solidité | Justification |
|---|---|---|---|
| ② `client-sync-eu[.]net` | **Fort** | **Élevée** | Trois critères indépendants : même certificat · création le même jour · fenêtre d'activité cohérente |
| ③ `mail-portal-secure[.]net` | **Fort** | **Élevée** | Idem, création à un jour près |
| ④ `boutique-artisanale[.]fr` | **Aucun** | — | Hébergé depuis 2019, déposant identifié |
| ⑤ `association-locale-92[.]org` | **Aucun** | — | Hébergé depuis 2021 |
| ⑥ `cdn-assets-delivery[.]com` | **Aucun** | — | Hébergé depuis 2017 |
| **L'adresse 203.0.113.44** | Partagé | — | **341 sites hébergés** |

**Le critère décisif** est la conjonction de trois éléments indépendants pour ② et ③ : le certificat commun, la date de création, et la fenêtre d'activité. Un seul de ces critères ne suffirait pas ; les trois ensemble constituent un lien solide.

**(b) Ce qu'on bloque**

| Élément | Décision | Motif |
|---|---|---|
| ① `sync-portal-update[.]net` | **Bloquer** | Confirmé malveillant |
| ② `client-sync-eu[.]net` | **Bloquer** | Trois critères indépendants |
| ③ `mail-portal-secure[.]net` | **Bloquer** | Idem |
| **203.0.113.44** | **NE PAS BLOQUER** | 341 sites hébergés |

**(c) Les deux faux positifs, et leurs conséquences**

**Faux positif n° 1 — bloquer l'adresse `203.0.113.44`.** C'est l'erreur principale du dossier, et elle est fréquente. Bloquer cette adresse coupe l'accès à **341 sites**, dont ④, ⑤ et ⑥ manifestement légitimes. L'un d'eux — ⑥ — est un service de diffusion de contenu, ce qui signifie que le blocage peut dégrader des sites tiers sans rapport, y compris des services utilisés par votre organisation.

**Faux positif n° 2 — bloquer ④, ⑤ ou ⑥ par association.** Un analyste pressé peut considérer que tout ce qui réside à cette adresse est suspect. Les dates d'hébergement — 2017, 2019, 2021 — l'excluent : ces domaines précèdent de plusieurs années la création de l'infrastructure malveillante. Ils sont **colocataires**, pas complices.

⚠️ Ce que ces deux faux positifs auraient produit : des tickets utilisateurs, une perte de confiance dans les blocages, et — c'est le plus grave — une pression pour désactiver les listes.

**(d) La date de retrait**

| Élément | Retrait proposé | Motif |
|---|---|---|
| ①, ②, ③ | **90 jours**, réexamen le 15 août | La dernière observation date du 05/05 ; l'infrastructure est probablement déjà abandonnée |

**La justification à écrire** : *« blocage de trois domaines liés par certificat commun et date de création, activité observée du 09/03 au 05/05/2030. Adresse d'hébergement non bloquée : 341 sites colocataires dont plusieurs légitimes antérieurs à 2020. Réexamen le 15/08/2030. »*

**Les trois erreurs attendues**

1. **Bloquer l'adresse.** C'est le réflexe, et c'est l'erreur la plus coûteuse du lab.
2. **Ne retenir que le domaine d'origine.** ② et ③ sont solidement liés ; les écarter perd de la couverture sans raison.
3. **Bloquer sans date de retrait.** Dans dix-huit mois, personne ne saura pourquoi ces trois domaines sont dans la liste, ni s'il faut les y laisser.

## 24.8 🔴 FIL ROUGE — mars 2030 : le graphe qui ne servait à rien

Après l'incident de février (§23.7), Nour dispose de quatorze indicateurs. Elle consacre deux journées à un travail de pivot approfondi.

**Le résultat** : un ensemble de 87 éléments — domaines, adresses, certificats — reliés à l'infrastructure de l'incident avec des degrés de confiance variables. Le graphe est impressionnant, et elle le présente au comité du 12 mars.

**La question de Claire** : *« qu'est-ce qu'on fait avec ça ? »*

**La réponse honnête**, que Nour donne après réflexion :

| Sur les 87 éléments | Usage |
|---|---|
| 9 | **Bloqués** — ceux du premier niveau de pivot, solidement liés |
| 12 | Recherchés rétrospectivement dans les journaux — **aucune correspondance** |
| 4 | Partagés au dispositif sectoriel |
| **62** | **Aucun usage identifié** |

**Le calcul qu'elle fait ensuite** : deux journées de travail pour neuf blocages et quatre partages. Les mêmes neuf blocages auraient été obtenus par un pivot de premier niveau en **quarante minutes**.

**Ce que Claire en tire**, et qui devient une règle :

> *« Le pivot de premier niveau, systématiquement. Au-delà, seulement si une question précise le justifie. »*

**Ce que Nour écrit dans son carnet**, et qui est plus honnête que la règle :

> *J'ai fait ce graphe parce qu'il était intéressant, pas parce qu'il servait. C'est la première fois que je m'en aperçois pendant que je le fais, et pas après.*

**L'exception qui confirme la règle**, six mois plus tard. En septembre 2030, un pivot de deuxième niveau est conduit — cette fois avec une question précise : *l'infrastructure de la campagne de juillet (§19.6) est-elle liée à celle de février ?* La réponse est non, et elle est obtenue en trois heures. **La question a rendu le travail utile ; c'est elle qui manquait en mars.**

**Livrable de l'épisode.** La règle du pivot de premier niveau, et le test à s'appliquer avant tout élargissement : *quelle question ce pivot va-t-il trancher ?*

→ **Fin de la Partie V.** La suite en Partie VI, quand il faudra transformer tout cela en produits que quelqu'un lit.

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> - **poser les quatre questions juridiques** avant toute collecte, et associer le délégué à la protection des données au moment du plan, pas du contrôle ;
> - **reconnaître qu'un accès techniquement possible n'est pas licite**, et connaître les sept interdits ;
> - **construire une veille tenable** en vingt minutes par jour, sur quatre sources ;
> - **reconnaître la fatigue de veille** et savoir que son remède est de réduire, pas d'ajouter ;
> - **évaluer un fournisseur en cinq tests** avant d'acheter, et substituer au volume la question du nombre d'éléments ayant produit une action ;
> - **exploiter la source la plus pertinente et la moins chère** : vos incidents, vos tentatives bloquées, vos dérogations, ce que savent vos métiers ;
> - **conduire un pivot d'infrastructure** au premier niveau, vérifier une colocation, et savoir quand un graphe ne sert à rien.
>
> **Ce que vous ne savez pas encore** : comment écrire tout cela pour que quelqu'un le lise, le comprenne et décide. C'est l'objet de la Partie VI.

---
