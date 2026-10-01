---
title: Chapitre 13 — Canaux, chats et messageries clandestines
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

Les **messageries et canaux** sont la couche temps réel du dark web. Là où forums et marchés sont persistants, les messageries sont éphémères — ce qui leur confère à la fois un intérêt opérationnel (communication rapide, pas de traces longues) et un défi investigatif (capturer les flux avant qu'ils disparaissent).

## 13.1 Les plateformes dominantes

**Telegram**. Dominant dans la cybercriminalité 2020-2024. Facilité d'usage, canaux publics avec des milliers d'abonnés, canaux privés invitation-only, groupes de discussion, bots. Historiquement perçu comme plus tolérant que les alternatives — politique de modération limitée.

**Impact de l'arrestation de Pavel Durov (août 2024)**. Suite à l'interpellation en France, Telegram a durci significativement sa modération — suppression massive de canaux criminels, coopération accrue avec les autorités sur les requêtes légales. Résultat : **migration partielle** de certains acteurs vers d'autres plateformes (Session, Matrix sur Tor, XMPP, retour aux forums .onion), mais Telegram reste dominant en volume absolu.

**XMPP (Jabber)**. Historiquement central dans la cybercriminalité russophone. Chaque utilisateur un JID (jabber ID) type `username@domain.com`. Chiffrement de bout en bout via OMEMO ou OTR. Serveurs non-custodial (l'admin du serveur ne peut pas lire les messages chiffrés). Résilient — si un serveur tombe, l'utilisateur peut migrer en changeant de JID. Usage encore courant chez les acteurs sérieux.

**TOX**. Protocole peer-to-peer chiffré de bout en bout. Pas de serveur central, pas de registrations. Moins populaire que XMPP mais utilisé pour communications très sensibles.

**Matrix (+ Element)**. Protocole fédéré, chiffrement E2E, parfois opéré sur Tor via onion routing des homeservers. Adoption lente dans la cybercriminalité mais croissante post-Durov.

**Session**. Messagerie basée sur Oxen/Lokinet, conçue pour anonymat. Pas de numéro de téléphone requis (contrairement à Signal, WhatsApp), pas de metadata centrale. Usage croissant chez acteurs paranoïaques.

**Signal**. Messagerie chiffrée grand public. **Moins utilisée** par cybercriminalité sophistiquée car requiert numéro de téléphone, metadata potentiellement saisissables via Twilio, cible fréquente de requêtes légales. Utilisée par activistes et journalistes plutôt que cybercrime organisé.

**IRC historique**. Usage résiduel pour certaines communautés de niche.

**Discord**. Usage modeste en cybercrime sérieux (modération forte, liens avec identités réelles fréquents), mais présent pour les marchés jeunes/gaming.

## 13.2 Les canaux Telegram cybercriminels

Les canaux Telegram publics cybercriminels peuvent être classés :

- **Canaux de leak** : publient des leaks gratuits (combo lists, databases publiées), souvent comme teasers pour des services payants. Des centaines de canaux, cumul de millions d'abonnés.
- **Canaux de CaaS** : phishing kits, DDoS, logs access. Interface commerciale, avec prix et méthodes de paiement.
- **Canaux de coordination** : groupes privés pour coordination opérationnelle entre membres d'une campagne. Typiquement invite-only.
- **Canaux d'hacktivisme** : revendiquent des attaques, publient des données volées dans un contexte idéologique (pro-russe, anti-israélien, etc.).
- **Canaux d'influence** : désinformation, amplification de narratifs, coordination d'opérations informationnelles.

## 13.3 L'investigation des messageries

**Capture de canaux publics**. Telegram notamment permet d'archiver les messages de canaux publics avec des outils comme Telethon (bibliothèque Python). Les canaux privés nécessitent une invitation — soit obtenue légitimement via un contact, soit impossible à obtenir.

**Métadonnées**. Même les messageries chiffrées laissent des métadonnées (qui a parlé à qui, quand, volume). Sur Telegram, les numéros de téléphone des membres de groupes peuvent parfois être extraits selon les paramètres de confidentialité.

**Corrélation avec pseudonymes**. Un pseudonyme sur un forum .onion peut avoir un handle Telegram affiché dans les posts. Suivre ce handle sur Telegram permet d'élargir la collecte.

**Identification par patterns**. Analyse stylométrique (Ch.29), timing d'activité, patterns de langue — permettent parfois de corréler des comptes supposés distincts.

**Actions légales**. Les autorités peuvent, dans certaines juridictions, exiger la coopération des plateformes. Telegram post-Durov coopère plus activement avec les requêtes légales.

## 13.4 Les limites investigatives

Les messageries sont plus difficiles à investiguer que les forums pour plusieurs raisons.

**Éphémérité**. Messages supprimés, canaux fermés, comptes bannis — la trace est vite perdue. Un analyste qui ne capture pas en temps réel perd l'information.

**Chiffrement**. Les messages chiffrés de bout en bout ne sont accessibles qu'aux participants — ni le serveur, ni les investigateurs ne peuvent les lire sans compromettre un endpoint.

**Volatilité des plateformes**. Un canal peut déménager ou disparaître du jour au lendemain. Maintenir le tracking nécessite de l'automatisation et de la réactivité.

**Faux comptes et sybil**. Les plateformes ouvertes permettent la création massive de faux comptes pour simuler l'activité, booster des narratifs, ou confondre les investigations.

## 13.5 L'usage des messageries dans DARKSTREAM

> **🌐 DARKSTREAM — Épisode 7 : XMPP avec aero_source**
>
> Lucas contacte aero_source via son XMPP affiché : `aero_source@xmpp.jp`. Serveur classique, non-custodial, fréquent dans la cybercriminalité russophone. Session chiffrée OTR négociée.
>
> Premier message de Lucas (persona « mapletech », se présente comme acheteur potentiel d'une entreprise tech intéressée par des specs aéronautiques — légende crédible côté profil Athéna) : demande d'échantillons supplémentaires, vérification du volume réel, méthode de paiement préférée.
>
> aero_source répond en 6 heures (cohérent avec un opérateur à temps plein sur fuseau horaire moscovite). Fournit 3 fichiers sample additionnels (1 spec technique de propulsion, 1 liste de fournisseurs, 1 extrait de notes de design). Confirme 420 Go total, paiement XMR préféré mais BTC accepté.
>
> Lucas note : style de langue russophone anglicisé (« I have all the data, you see ? ») — cohérent avec profil russophone. Fuseau horaire des réponses (toutes entre 08:00 et 22:00 MSK) conforte. Pas de fautes de tournure inhabituelles — acteur probablement expérimenté, pas un débutant.
>
> L'échantillon reçu sera analysé (Ch.25 — authentification). En parallèle, Lucas documente les métadonnées de la session : timestamps exacts, clé OTR négociée, serveur. Ces éléments pourront servir au rapport et au cross-matching avec d'autres pseudonymes.

---
