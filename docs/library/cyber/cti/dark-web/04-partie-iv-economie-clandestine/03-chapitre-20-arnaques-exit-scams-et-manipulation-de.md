---
title: Chapitre 20 — Arnaques, exit scams et manipulation de la confiance
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IV — Économie clandestine
  - index.md
---

Malgré les mécanismes de confiance, l'arnaque est structurelle dans l'écosystème. Ce chapitre cartographie les grandes catégories, leurs mécanismes, et leurs signaux.

## 20.1 Taxonomie des arnaques

**Petits scams de vendeur** :

- **Non-livraison** : acheteur paie, produit jamais envoyé. Typique pour vendeurs jetables.
- **Produit de moindre qualité** : drogues diluées, données périmées, accès non fonctionnel, malware à la place du logiciel promis.
- **Volume réduit** : vendeur promet 500 Go, livre 50 Go. Espère que l'acheteur n'audite pas.
- **Données recyclées** : vente comme « fresh breach » de données publiquement disponibles depuis des mois.

**Scams structurés** :

- **Double selling** : la même donnée vendue en exclusivité à plusieurs acheteurs. Viole les termes annoncés, destruction de la valeur.
- **Fake breach** : annonce d'un breach qui n'a pas eu lieu, avec données fabriquées pour passer quelques vérifications superficielles.
- **Impersonation** : pseudonyme qui mime un vendeur établi (slight variation orthographique). Exploite la crédibilité de la cible impersonnée.

**Exit scams** (Ch.11.4).

**Meta-scams** :

- **Fake escrow** : un « tiers de confiance » se propose pour un escrow, disparaît avec les fonds. Les forums sérieux ont leurs escrows officiels ; tout escrow tiers « découvert récemment » est suspect.
- **Fake arbitres** : usurpation d'identité d'admin. Un « admin » qui contacte en privé pour résoudre un litige est probablement faux — les vrais arbitres interviennent dans les threads officiels.

**Scams contre les analystes / forces de l'ordre** :

- **Honeypots criminels** : vendeurs qui distribuent intentionnellement des données piégées (fichiers contenant des beacons web, scripts malveillants) à des profils soupçonnés d'être des analystes.
- **Faux dissidents** : pseudonymes qui prétendent vouloir quitter le crime, vendent des « informations » aux investigateurs, souvent fausses ou trompeuses.

## 20.2 Signaux de scam typiques

**Côté vendeur** :

- **Compte neuf** (< 3 mois) sans vouching.
- **Prix nettement inférieur** à la moyenne du marché pour le même type de produit.
- **Refus d'échantillon** systématique.
- **Pression temporelle** : « offre limitée 24h », pour empêcher la due diligence.
- **Communications incohérentes** : russe correct puis anglais bizarre puis retour russe — plusieurs opérateurs derrière un pseudo, parfois des scammers coopérant.
- **PGP non signé ou nouveau** : sérieux vendeur signe ses posts, avec clé stable.
- **Refus de multi-sig escrow** : préférence pour paiement direct ou FE. Légitime parfois, suspect souvent.

**Côté opérateur (forum/marché)** :

- **Dégradation des délais** : support qui ne répond plus, disputes qui traînent.
- **Retraits ralentis** : nouveaux délais imposés, vérifications additionnelles.
- **Buffer d'escrow visible anormalement élevé** : si le forum affiche (volontairement ou en leak) ses stocks en escrow qui grimpent alors que retraits diminuent, exit scam probable.
- **Communications des admins qui changent de ton** : plus promotionnelles, plus silencieuses, ou disparues.
- **Domaines .onion qui changent sans annonce cohérente**.
- **Partenariats communautaires qui se rompent** : anciens admins qui partent, voisins forums qui dé-vouchent publiquement.

## 20.3 Comment se protéger (pour acheteur, pour investigateur)

**Pour l'acheteur avisé** :

- Transiger **uniquement avec des vendeurs établis** (500+ transactions, 98%+ feedback, ancienneté > 12 mois).
- Utiliser **escrow du marché** systématiquement. Jamais de paiement direct.
- **Ne pas utiliser FE** sauf vendeur trustissime.
- **Ne pas laisser de gros stock** chez un marché (retirer rapidement après transactions).
- **Vérifier les PGP** : les clés des vendeurs réputés sont stables et cross-signed.
- **Monitoring des signaux** : si le forum commence à montrer des signes d'exit scam, retirer tout immédiatement.

**Pour l'investigateur** :

- **Considérer tout nouveau post suspect par défaut** — probabilité de scam plus élevée que probabilité d'authenticité.
- **Vérifier via échantillons** avant d'allouer des ressources à une piste.
- **Cross-checker les pseudonymes** sur multiple forums pour détecter les impersonations.
- **Ne jamais payer pour « débloquer » information** — les demandes de paiement pour information sont fréquemment des scams.
- **Valider via autorités ou victime** quand possible — un breach revendiqué mais non confirmé par la victime est à traiter avec scepticisme élevé.

## 20.4 Les grands exit scams

Historique sélectif.

**Evolution Market (mars 2015)**. Ex-second plus grand marché de l'époque. Admins « Verto » et « Kimble » disparaissent avec environ 12 M USD de BTC en escrow. Communauté anéantie, migration massive vers Abraxas puis AlphaBay.

**Nucleus (avril 2016)**. Exit scam plus modeste, ~5 M USD.

**Empire Market (août 2020)**. ~30 M USD, un des plus gros de l'histoire. Admins s'évaporent sans annonce. Les spéculations ont évoqué soit exit volontaire, soit compromission par un tiers, soit panic mid-course face à une menace judiciaire.

**Monopoly Market (2023)**. Saisi par les autorités mais au même moment, des signaux d'exit étaient présents — confusion post-hoc sur le réel séquencement.

**Incognito Market (2024)**. Modèle hybride — exit scam avec menace de dox des utilisateurs non-payeurs.

## 20.5 La gestion d'un exit scam côté analyste

Quand un exit scam se produit sur un forum suivi, l'analyste peut :

**Capturer immédiatement** les dernières observations avant que le forum disparaisse (posts actifs, pseudonymes actifs, annonces récentes). Le forum peut re-disparaître définitivement.

**Monitorer la migration**. Les membres scammed se regrouperont sur d'autres forums, souvent avec posts « je viens de perdre 20k sur Empire, quelqu'un a des nouvelles ». Ces posts sont **riches en renseignement** — ils exposent des pseudonymes, des patterns de transaction, des sommes.

**Suivre les wallets**. Si l'admin exit scam, les fonds transitent. Les adresses reçoivent de gros montants en peu de temps, puis se dispersent. Tracking on-chain (Chainalysis, TRM) peut révéler des patterns (où vont les fonds, quelle méthode de blanchiment) et potentiellement identifier l'opérateur.

**Documenter**. Même si l'investigation ne peut pas pénaliser l'exit scammer, la documentation nourrit la connaissance de l'écosystème — profils d'admins, patterns d'opération, durées de vie typiques.

---
