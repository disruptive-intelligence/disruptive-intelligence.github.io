---
title: Chapitre 6 — Data brokers, courtiers de données et désinscription effective
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 2 — Identité, compartimentation et hygiène comportementale
  - index.md
---

## 6.1 Anatomie du marché

Les data brokers compilent, à partir de sources légales (registres publics, programmes de fidélité, applications mobiles vendant leurs données, fuites achetées, données dérivées des plateformes), des profils détaillés revendus à des annonceurs, des assureurs, des banques, et — point critique — à des forces de l’ordre via achat plutôt que mandat judiciaire (cas documenté aux États-Unis : ICE achète à des courtiers ce qu’ils ne pourraient obtenir sans mandat).

Aux États-Unis, l’industrie est florissante (Acxiom, LexisNexis, Spokeo, BeenVerified, Whitepages, Intelius, ID Analytics, etc.). En Europe, le RGPD limite — sans empêcher — la pratique. En France, des courtiers existent (Société.com, Pages Jaunes Pro, Easyfichiers, etc.) sur des bases plus limitées.

## 6.2 Cas français et européens

En France et en Europe, les sources principales de profilage sont :

- Le registre du commerce et des sociétés (gérants, adresses, capitaux).
- Les annuaires (Pages Jaunes, Pages Blanches — désinscription possible).
- Les listes électorales (consultables sous conditions).
- Les annonces légales (publications obligatoires).
- Le BODACC pour les dirigeants.
- Les sites de fuites agrégant des bases européennes.
- Les anciens annuaires d’écoles et d’universités.

Le RGPD permet d’invoquer le droit à l’effacement (article 17) et le droit d’opposition (article 21). Ces droits sont opposables à tout responsable de traitement basé en UE ou ciblant des résidents UE.

## 6.3 Désinscription manuelle vs services payants

Les services type DeleteMe (US), Optery, Incogni, Privacy Bee automatisent la désinscription auprès de centaines de courtiers. Avantages : gain de temps. Limites : couverture incomplète (surtout courtiers européens), efficacité partielle (certains courtiers réinscrivent), modèle économique qui suppose une renouvellement (les courtiers re-collectent en continu), confiance à accorder au service lui-même (qui reçoit en bonus une liste de tes données).

La désinscription manuelle reste l’option maximaliste : long, fastidieux, mais traçable. Pour la France, deux types de courriers utiles :

- Demande de droit à l’effacement (article 17 RGPD) avec justificatif d’identité, à adresser au DPO du courtier.
- Demande d’opposition (article 21) avec motif (généralement : « finalité de prospection commerciale »).

En cas de refus ou de non-réponse sous un mois : réclamation à la CNIL.

## 6.4 Le piège : la désinscription qui re-confirme

Certains courtiers exigent, pour te désinscrire, que tu confirmes ton identité et tes données déjà détenues. Cela peut paradoxalement *enrichir* leur base si tu fournis des données qu’ils n’avaient pas. Règle : fournis le strict minimum exigé légalement, et conserve une copie de tes envois.

Autre piège : la désinscription via un courtier *re-confirme* qu’un humain réel se cache derrière ce profil. Pour certains courtiers, c’est plus précieux que la donnée brute.

## 6.5 Maintenance : le ré-empilage et la routine semestrielle

Les courtiers ré-acquièrent constamment de nouvelles données (achats de bases, agrégation depuis applications). Une désinscription n’est pas définitive. Il faut prévoir un cycle semestriel ou annuel :

1. Recherche de soi sur les principaux courtiers.
1. Identification des nouveaux apparitions.
1. Réémission des demandes RGPD.
1. Suivi des réponses.

C’est un travail à organiser, à dater, à documenter. Sans cette routine, tout reflue en six mois.

## 6.6 Limite réelle

Tu ne nettoieras jamais à 100 %. Certaines bases ne sont pas indexables, certaines fuites sont irrécupérables (une fois sur Telegram, une donnée y reste), certaines juridictions n’appliquent pas le RGPD. La désinscription est *complémentaire* à la compartimentation, pas un substitut. Pour les nouveaux comptes, tu créeras une nouvelle empreinte ; à toi de l’architecturer mieux.

-----
