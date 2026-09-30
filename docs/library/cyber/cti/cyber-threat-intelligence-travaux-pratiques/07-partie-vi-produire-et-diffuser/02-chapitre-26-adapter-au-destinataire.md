---
title: Chapitre 26 — Adapter au destinataire
source: Cyber/01_CTI/CTI_Work.md
note: Cyber Threat Intelligence — travaux pratiques
up:
- - Cyber Threat Intelligence — travaux pratiques
  - ../index.md
- - PARTIE VI — Produire et diffuser
  - index.md
---

## 26.1 Une information, cinq produits

**Le principe** : le même événement, analysé une fois, produit plusieurs livrables différents — pas un livrable envoyé à plusieurs personnes.

**Ce qui change d'un destinataire à l'autre** :

| Dimension | Varie ? |
|---|---|
| Les faits établis | **Non** |
| L'évaluation et sa confiance | **Non** |
| Ce qui est retenu | **Oui** |
| Le niveau de détail | **Oui** |
| L'implication mise en avant | **Oui** |
| Le vocabulaire | **Oui** |
| La longueur | **Oui** |

⚠️ **La première ligne est une contrainte absolue.** Adapter au destinataire ne signifie jamais ajuster la conclusion. Une évaluation atténuée pour une direction et durcie pour l'exploitation est une faute — c'est le biais du client (§7.7) institutionnalisé.

## 26.2 Pour la direction générale

| Élément | Contenu |
|---|---|
| **Longueur** | 1 page, 10 lignes si possible |
| **Question à laquelle répondre** | *Est-ce que cela nous concerne, et devons-nous décider quelque chose ?* |
| **Ce qu'on retient** | L'implication métier, le coût, l'échéance |
| **Ce qu'on écarte** | Techniques, indicateurs, noms d'acteurs, détail du raisonnement |
| **Vocabulaire** | Aucun terme technique non défini |
| **Ce qu'on ajoute** | **Une demande explicite** : décision, arbitrage, ou information seule |

**La ligne à ne jamais omettre** : *« nous n'attendons pas de décision de votre part »* quand c'est le cas. Un produit envoyé à une direction sans indiquer ce qu'on attend d'elle crée une inquiétude inutile ou une inaction.

## 26.3 Pour le RSSI

| Élément | Contenu |
|---|---|
| **Longueur** | 1 à 2 pages |
| **Question** | *Est-ce que cela change mes priorités ?* |
| **Ce qu'on retient** | L'évaluation complète, les implications sur le dispositif existant |
| **Ce qu'on ajoute** | Ce que cela dit de nos angles morts |

C'est le destinataire le plus proche de l'analyste, et celui pour qui le produit standard convient le mieux.

## 26.4 Pour l'exploitation et la gestion des vulnérabilités

| Élément | Contenu |
|---|---|
| **Longueur** | Une demi-page, souvent moins |
| **Question** | *Que dois-je corriger en premier ?* |
| **Ce qu'on retient** | Les identifiants de vulnérabilités, l'applicabilité, l'ordre |
| **Ce qu'on écarte** | Tout le contexte, sauf ce qui justifie l'ordre |
| **Format** | **Une liste ordonnée**, pas un texte |

**Le format qui fonctionne** :

```
Priorité 1 — [identifiant] — exploitée activement, 4 actifs exposés concernés
Priorité 2 — [identifiant] — exploitée dans notre secteur, 12 actifs internes
Priorité 3 — [identifiant] — non exploitée, gravité élevée, 2 actifs

Non prioritaire — [identifiant] — composant non déployé chez nous
```


**La dernière ligne compte autant que les autres** : dire ce qui **n'est pas** prioritaire évite que l'équipe le traite quand même par prudence.

## 26.5 Pour la détection et la réponse

| Élément | Contenu |
|---|---|
| **Question** | *Que dois-je chercher, et comment ?* |
| **Ce qu'on retient** | Comportements, techniques, indicateurs |
| **Ce qu'on ajoute obligatoirement** | **Date de première et dernière observation · source · confiance · action attendue** |
| **Format** | Structuré, exploitable machine si possible |

⚠️ Un indicateur livré sans ces quatre attributs est inexploitable (§3.3). C'est la faute la plus fréquente dans les échanges entre CTI et détection.

## 26.6 Pour le produit et la sécurité produit

| Élément | Contenu |
|---|---|
| **Question** | *Est-ce que cela touche nos produits, et devons-nous prévenir nos clients ?* |
| **Ce qu'on retient** | L'applicabilité produit par produit, version par version |
| **Ce qu'on ajoute** | L'obligation de signalement éventuelle, et son délai |
| **Sensibilité** | **Élevée** — ce produit peut déclencher une communication externe |

## 26.7 Pour un client ou un partenaire

| Élément | Contenu |
|---|---|
| **Question** | *Sommes-nous exposés par votre faute, et que faites-vous ?* |
| **Ce qu'on retient** | Ce qui les concerne, ce qui est fait, ce qu'ils doivent faire |
| **Ce qu'on écarte** | Notre organisation interne, nos angles morts, nos hypothèses non consolidées |
| **Validation** | **Systématique** — juridique, et direction selon l'enjeu |

**Le principe qui gouverne ce produit** : on ne transmet à l'extérieur que ce qu'on peut soutenir. Une hypothèse de travail interne devient, transmise à un client, une affirmation qu'on devra assumer.

## 26.8 🔬 Mini-lab 8 — Cinq bulletins, un événement

**Objectif** — Produire cinq livrables adaptés à partir d'une analyse unique, sans altérer la conclusion.
**Durée** 50 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §26.1 à §26.7, §25.1 · **Livrable** cinq textes courts
**Compétences validées** — ✔ adapter sans altérer ✔ identifier l'implication propre à chaque destinataire ✔ choisir le bon format ✔ dire ce qu'on attend du destinataire ✔ écarter ce qui ne le concerne pas

**L'analyse fournie** — le matériau commun, à ne pas modifier :

> **Conclusion.** Nous estimons **très probable** qu'une vulnérabilité affectant une bibliothèque d'authentification largement diffusée soit activement exploitée contre des organisations de notre secteur — **confiance élevée** : trois victimes documentées par deux sources indépendantes, mécanisme d'exploitation décrit publiquement, et signalements concordants de deux de nos clients.
>
> **Applicabilité.** La bibliothèque est embarquée dans trois de nos cinq versions déployées de notre produit principal. 43 clients utilisent une version affectée. Elle est également présente sur deux de nos serveurs applicatifs internes.
>
> **Exposition.** Le vecteur nécessite un accès au portail d'authentification, exposé par nécessité fonctionnelle. L'authentification multifacteur limite l'exploitation sans l'empêcher.
>
> **Correctif.** Publié par le mainteneur de la bibliothèque il y a 4 jours. Notre équipe de développement estime 6 jours pour l'intégrer aux trois versions maintenues.
>
> **Ce qui invaliderait.** Une victime utilisant une version non concernée · une cause applicative locale expliquant les symptômes observés chez nos clients.
>
> **Indicateurs.** 11 disponibles, première observation 28 juin, dernière 19 juillet.
>
> **Obligation.** Une vulnérabilité activement exploitée affectant un produit mis sur le marché déclenche une obligation de signalement, délai d'alerte précoce 24 h.

**Consigne** : produisez cinq livrables — direction générale, exploitation, détection, sécurité produit, clients. Respectez les longueurs cibles.

---

**Corrigé commenté**

**① Direction générale — 9 lignes**

> **Objet : vulnérabilité exploitée affectant notre produit — signalement réglementaire en cours**
>
> Nous estimons très probable qu'une vulnérabilité affectant une bibliothèque intégrée à notre produit principal soit activement exploitée contre des organisations de notre secteur — confiance élevée.
>
> **Ce que cela implique.** 43 clients utilisent une version concernée. Un correctif sera disponible sous 6 jours. Une obligation réglementaire de signalement s'applique et sera honorée dans le délai de 24 heures.
>
> **Ce que nous attendons de vous.** Information, à ce stade. Une décision sera nécessaire si nous devions recommander une interruption de service chez nos clients, ce qui n'est pas le cas aujourd'hui.
>
> *Évaluation au 22 juillet. Point d'étape le 25.*

⚠️ **Ce qui a été écarté** : le nom de la bibliothèque, le mécanisme, les indicateurs, le raisonnement, les sources. **Ce qui a été ajouté** : l'obligation réglementaire, et surtout la ligne « ce que nous attendons de vous ».

**② Exploitation et gestion des vulnérabilités — 6 lignes**

> **Priorité 1** — [bibliothèque, version] — **exploitée activement**, présente sur 2 serveurs applicatifs internes exposés. Correctif disponible. À traiter sous 72 h.
>
> **Non prioritaire** — aucune autre occurrence de cette bibliothèque n'a été identifiée dans le parc interne. Vérification faite le 22 juillet sur l'inventaire complet.
>
> **Attention** : l'authentification multifacteur limite l'exploitation mais ne la neutralise pas. Ne pas considérer les serveurs comme protégés.

⚠️ Le périmètre interne — deux serveurs — est ce qui concerne ce destinataire. Les 43 clients ne le concernent pas.

**③ Détection — format structuré**

> **Contexte** : exploitation d'une vulnérabilité d'authentification, campagne active dans le secteur santé.
> **Comportement à rechercher** : tentatives d'authentification en volume anormal sur le portail, suivies d'une dégradation des performances applicatives.
> **Fenêtre de recherche rétrospective recommandée** : depuis le 28 juin.
>
> | Indicateur | Type | 1ʳᵉ obs. | Dernière obs. | Source | Confiance | Action |
> |---|---|---|---|---|---|---|
> | *(11 lignes)* | | 28/06 | 19/07 | Dispositif sectoriel + client | Élevée | Rechercher, ne pas bloquer sans vérification |

⚠️ **La colonne « action » est essentielle** : « rechercher, ne pas bloquer sans vérification » évite les faux positifs du §24.5.

**④ Sécurité produit — 12 lignes**

> **Applicabilité** : versions 4.2, 4.3 et 4.4 concernées. Versions 5.0 et 5.1 non concernées — vérification faite, la bibliothèque a été remplacée en 5.0.
> **Clients concernés** : 43, liste jointe.
> **Correctif** : 6 jours pour les trois versions maintenues.
> **Mesure d'atténuation immédiate** à communiquer aux clients : [restriction d'accès au portail].
>
> **Obligation de signalement** : déclenchée. Alerte précoce sous 24 h, soit avant le 23 juillet 18 h. Notification sous 72 h. Le dossier est prêt, validation juridique demandée.
>
> **Ce qui invaliderait** : une victime sur une version non concernée remettrait en cause l'analyse d'applicabilité.

**⑤ Clients — 8 lignes**

> **Objet : vulnérabilité affectant votre version de [produit] — mesure immédiate recommandée**
>
> Une vulnérabilité affectant un composant de votre version de [produit] fait l'objet d'une exploitation active. Votre installation est concernée.
>
> **Ce que nous faisons** : un correctif sera mis à disposition sous 6 jours. Vous serez notifié dès sa publication.
>
> **Ce que nous vous recommandons de faire immédiatement** : [mesure d'atténuation], qui limite l'exposition sans interrompre le service. La procédure est jointe.
>
> **Contact** : [ligne dédiée], disponible jusqu'à la publication du correctif.

⚠️ **Ce qui a été écarté** : nos hypothèses, nos sources, le fait que deux clients nous ont signalé les symptômes, et toute mention de notre organisation interne. **Ce qui a été ajouté** : une action immédiate, et un contact.

**Les trois erreurs attendues**

1. **Envoyer les indicateurs à la direction générale.** Ils n'y ont aucun usage et créent l'impression que le CTI ne comprend pas son interlocuteur.
2. **Atténuer la conclusion pour les clients.** La tentation est réelle — « pourrait être affectée » plutôt que « est concernée ». C'est une altération, et elle se retourne au premier incident.
3. **Omettre « ce que nous attendons de vous »** dans le produit direction. Sans cette ligne, le destinataire ne sait pas s'il doit agir, et l'inaction par défaut est le résultat le plus fréquent.

## 26.9 🔴 FIL ROUGE — juillet 2030 : cinq bulletins en trois heures

L'épisode du §19.6 — trois signalements formant une campagne — produit sa suite immédiate. Le 22 juillet, Nour dispose de l'analyse. Elle a trois heures avant l'échéance de signalement réglementaire.

**Ce qu'elle produit** : les cinq livrables du mini-lab 8, à partir d'une analyse unique rédigée une seule fois.

**Le chronométrage réel**, qu'elle note :

| Tâche | Durée |
|---|---|
| Analyse consolidée | 1 h 40 |
| Bulletin direction | 8 min |
| Bulletin exploitation | 5 min |
| Bulletin détection | 20 min — la mise en forme des indicateurs |
| Bulletin sécurité produit | 25 min — vérification d'applicabilité version par version |
| Bulletin clients | 30 min — dont validation juridique |
| **Total diffusion** | **1 h 28** |

**Ce que le chronométrage démontre** : les cinq bulletins ont coûté moins de temps que l'analyse. C'est le point que Nour porte au comité, parce qu'il contredit l'objection habituelle — *« adapter à chaque destinataire, c'est trop long »*.

**L'effet observé** : les cinq destinataires agissent dans les vingt-quatre heures. Le signalement réglementaire est déposé dans le délai. Les 43 clients reçoivent la mesure d'atténuation le lendemain matin.

**Ce que Yann Prigent relève**, et qui n'était pas attendu : trois clients répondent au bulletin en signalant qu'ils avaient observé les mêmes symptômes sans les avoir signalés. **Le bulletin a produit du renseignement en retour** — trois observations supplémentaires qui confirment l'analyse et étendent le périmètre connu.

> *« Diffuser, c'est aussi collecter »*, note Nour dans son carnet.

**Livrable de l'épisode.** Les cinq modèles de bulletins, avec leurs longueurs cibles — annexe D.

→ La suite en 🔴 §27.6, quand une alerte de trop fera baisser le taux de réaction.

## Synthèse mentale du chapitre 26

Un même événement produit plusieurs livrables, jamais un livrable envoyé à plusieurs personnes — et ce qui varie est ce qu'on retient, le détail, l'implication et le vocabulaire, jamais les faits ni la conclusion : adapter n'est pas ajuster. Pour une direction, la ligne à ne jamais omettre est *ce que nous attendons de vous*, faute de quoi l'inaction est le résultat par défaut. Pour l'exploitation, dire ce qui n'est **pas** prioritaire compte autant que l'ordre, sinon l'équipe traite tout par prudence. Pour la détection, un indicateur sans date, source, confiance et action attendue est inexploitable. Pour un client, on ne transmet que ce qu'on peut soutenir : une hypothèse de travail devient une affirmation qu'il faudra assumer. Enfin, produire cinq bulletins coûte moins de temps que l'analyse elle-même — et diffuser produit du renseignement en retour.

**Trois questions de vérification**

1. Qu'est-ce qui varie et qu'est-ce qui ne varie jamais entre deux bulletins portant sur le même événement ?
2. Vous envoyez une note à votre direction générale. Quelle ligne omettez-vous le plus souvent, et quel effet produit son absence ?
3. Pourquoi l'objection « adapter à chaque destinataire prend trop de temps » ne résiste-t-elle pas à un chronométrage ?

---
