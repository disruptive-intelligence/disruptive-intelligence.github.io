---
title: 'Chapitre 10 — Forums clandestins : culture, hiérarchie et codes'
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

Les forums sont l'ossature sociale du dark web. Contrairement aux marchés qui sont des points de transaction et aux messageries qui sont des canaux éphémères, les forums sont des **espaces de communauté persistants** où se construisent les réputations, se partagent les connaissances, et se recrutent les collaborations.

## 10.1 Typologie des forums

Les forums varient par leur **spécialité** et leur **langue**.

**Forums généralistes cybercriminels**. XSS Forum (ex-DamageLab, russophone, historique), Exploit.in (russophone), BreachForums (anglophone — succession de plusieurs instances après saisies, la plus récente opérée par ShinyHunters après l'arrestation de Pompompurin en 2023 puis de Baphomet en 2024). Ces forums couvrent un spectre large : vente de données, discussions sur le hacking, recherche de partenaires, ventes d'outils.

**Forums spécialisés par thématique**. Carding (BriansClub, WWH Club), fraude bancaire, ransomware, drogue (forums adjacents aux marchés), armes (très rares, majoritairement scams), CSAM (priorité 1 des forces de l'ordre).

**Forums géographiques**. Marchés régionaux — forums ukrainien, polonais, chinois, coréen, persophone, arabophone. Chaque bloc avec ses codes et ses acteurs.

**Forums de niche**. **IndustrialLeaks** (fictif, DARKSTREAM) est un exemple de ces forums nichés — spécialisation sur un segment (données industrielles) permet de concentrer une communauté de confiance plus étroite.

**Forums « respectables »** vs **forums low-end**. Les forums sérieux (XSS, Exploit) ont un KYC interne fort — vouching, tests techniques, réputation durable. Les forums low-end sont ouverts à tous, majoritairement peuplés de script kiddies et scammers.

## 10.2 Hiérarchie de membres

Structure typique d'un forum sérieux.

**Newcomer / Noob** : membre nouvellement inscrit, peu ou pas de posts. Accès limité — consultation des zones publiques, pas d'accès aux zones premium, pas droit de poster dans certains canaux.

**Member** : membre établi, quelques mois d'ancienneté, posts réguliers. Accès élargi, peut répondre à des posts, commencer à construire une réputation.

**Trusted / Verified** : membre vérifié — soit par **vouching** (parrainage par un membre établi qui engage sa réputation), soit par des transactions réussies, soit par un test technique. Peut vendre, peut poster dans les zones premium.

**VIP / Senior** : membre de très long terme avec réputation solide. Souvent des acteurs impliqués dans les activités majeures (opérateurs ransomware, IAB de premier plan). Accès à toutes les zones, peut parrainer des newcomers.

**Moderator** : modérateurs nommés par les admins. Arbitrent les litiges, bannissent les comptes indésirables, surveillent l'activité. Leur identité réelle est souvent connue des admins uniquement.

**Admin** : opérateurs du forum. Peuvent voir tout, décider des règles, collecter les droits d'entrée et commissions.

**Lurkers** : lecteurs silencieux. Les forums sérieux les tolèrent avec réserve — un compte inactif pendant 6 mois peut être supprimé. Les acteurs défensifs (analystes CTI, forces de l'ordre) sont presque toujours des lurkers par défaut.

## 10.3 Règles internes et modération

Les forums sérieux ont des règles publiées et appliquées. Variations selon les forums, mais constantes récurrentes.

**Interdictions typiques** :

- **Pédopornographie** : universellement interdite, même dans les forums criminels. Raison : attraction maximale des forces de l'ordre, destruction potentielle du forum.
- **Cibles sensibles** : dans les forums russophones, ciblage d'entités CEI souvent interdit par règle (protection politique implicite du Kremlin envers ces acteurs, en échange tacite d'un ciblage exclusif hors-CEI).
- **Dox personnels** : publication d'informations personnelles sur des membres, sauf dispute résolue par arbitrage.
- **Scam** : membre scammant un autre membre est bannissable — mais prouver le scam est toujours l'objet de débats.
- **Multi-accounts** : création de plusieurs comptes pour simuler la popularité (sock puppets).

**Sanctions** : warning avec perte temporaire de privilèges, bannissement temporaire (jours/semaines) ou définitif, bannissement étendu cross-forum parmi forums partenaires.

**Arbitrage** : en cas de litige commercial, un modérateur ou admin arbitre. Peut imposer un remboursement partiel, valider le scam, ou déclarer l'affaire non-résolue. Le pouvoir d'arbitrage est considérable — un admin corrompu ou compromis peut basculer le destin d'une dispute.

## 10.4 Codes culturels et jargon

Chaque forum a ses codes. Certains se retrouvent largement dans l'écosystème.

**Salutations et conventions**. « Hi all », « Greetings », « Bro » selon le style. Les forums russophones utilisent **Привет** (privet), **Коллеги** (kollegi — « collègues »), **Уважаемые** (uvazhaemye — « estimés »). Les usages trahissent parfois l'origine : un anglophone qui écrit « Privet all » tente probablement de se faire passer pour russophone.

**Termes techniques**. **FUD** (Fully Undetected — se dit d'un malware indétectable par les AV), **stub**, **crypter**, **binder**, **loader**. **IAB** (Initial Access Broker), **RaaS**, **CaaS**. Les forums spécialisés ont un lexique dense ; maîtriser ce lexique est essentiel pour comprendre les posts et ne pas se trahir.

**Formats de post standardisés**. Vente de données : description du contenu, échantillon gratuit, méthode de paiement acceptée, méthode de contact (Jabber/XMPP, Telegram, TOX, messagerie du forum). Annonce IAB : pays, secteur, type d'accès (VPN, RDP, Citrix, Active Directory), niveau de privilèges (user, admin local, admin domaine), revenue annuel de la cible, prix demandé.

**Signature et PGP**. Membres sérieux signent leurs posts en PGP — garantit que le compte n'a pas été usurpé. Un vendeur établi change rarement sa clé PGP sur la durée. Une rotation de clé PGP est un signal de changement d'opérateur (rachat de compte, compromis).

## 10.5 Économie des forums

Sources de revenus pour les opérateurs :

- **Droits d'entrée** : 50-500 USD typiquement. IndustrialLeaks demanderait 0,005 BTC (~250 USD). Barrière à l'entrée qui filtre les simples curieux.
- **Abonnements premium** : accès VIP, 100-1 000 USD/mois.
- **Commissions sur ventes** : 1-5% via l'escrow du forum.
- **Vente de services** : hosting pour membres, advertising, slots prioritaires.
- **Droits de vouching** : certains forums monétisent les droits de parrainage.

Un forum sérieux actif peut générer 50 000 à 500 000 USD/an pour ses opérateurs, parfois davantage.

## 10.6 Cycle de vie typique

**Phase 1 — Lancement** : recrutement initial, 6-12 mois de réputation à construire.

**Phase 2 — Croissance** : traction, modération, résilience. Peut durer 2-5 ans.

**Phase 3 — Maturité** : forum reconnu dans son segment, communauté stable.

**Phase 4 — Rupture** : saisie (Hydra 2022, Genesis 2023, BreachForums multiple), exit scam, épuisement opérationnel, guerre interne, ou désertion vers concurrent.

**Phase 5 — Reconstitution** : successeurs émergent. RaidForums → BreachForums → BreachForums v2 illustre cette cyclicité.

Pour l'investigateur, le cycle implique : **un forum étudié aujourd'hui n'existera peut-être plus dans 6 mois**. La documentation et la capture préservent la trace ; l'expertise historique est un actif d'investigation durable.

## 10.7 Fil rouge — DARKSTREAM : lecture d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 6 : exploration initiale**
>
> Après accès validé par vouching (Athéna a un membre partenaire dans un forum affilié qui a accepté de vouch une persona d'investigation, sous encadrement DGSI), Lucas explore IndustrialLeaks.
>
> **Structure du forum** : 8 zones publiques + 3 zones premium. Les zones publiques couvrent annonces, ventes générales de données, recherche de partenaires, discussions techniques. Les zones premium (accessibles après paiement additionnel) couvrent « industrial espionage », « government access », « supply chain intrusion ».
>
> **Activité récente** : ~30-40 nouveaux posts par semaine en zone publique, ~10 en zones premium. Rythme soutenu, pas un forum mort.
>
> **Le post aero_source** : posté il y a 11 jours dans la zone « Data sales ». Titre : « EU aerospace supplier, 420GB, propulsion R&D, defense programs inside ». Corps du post : brève description, liste d'échantillons disponibles (5 fichiers), prix 65 000 USDT. Méthode de contact : XMPP (aero_source@xmpp.jp — serveur non-custodial classique).
>
> **Profil aero_source** : compte créé il y a **8 mois**. 12 posts au total. 2 transactions confirmées précédemment (petits dumps, 5 000-15 000 USD). Pas de vouching publicly affiché. Pas de rating négatif.
>
> Lucas note : profil **intermédiaire** — pas un scammer opportuniste (historique transactionnel), pas un vétéran majeur. Possiblement un acteur qui a gradé de petites ventes à un dump plus gros. Possiblement aussi un proxy pour un acteur plus sophistiqué qui ne veut pas utiliser son propre pseudo.
>
> La première tâche est maintenant de **demander un échantillon** (via XMPP, avec une persona crédible). Avant cela, Lucas va continuer à cartographier : activités aero_source sur d'autres forums (Ch.26 pivoting), monitoring des posts d'aujourd'hui, observation du comportement conversationnel en zone commune.

---
