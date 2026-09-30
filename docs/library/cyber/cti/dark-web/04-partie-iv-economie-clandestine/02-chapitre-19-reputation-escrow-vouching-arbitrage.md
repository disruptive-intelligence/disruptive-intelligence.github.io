---
title: Chapitre 19 — Réputation, escrow, vouching, arbitrage
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IV — Économie clandestine
  - index.md
---

Approfondissement des mécanismes fiduciaires du dark web. Ce chapitre détaille comment ils fonctionnent concrètement et comment l'investigateur peut les lire.

## 19.1 Le système de réputation

**Composantes d'un profil de vendeur** :

- **Ancienneté** : date d'inscription sur le forum/marché, date du premier post, date de la première transaction.
- **Nombre de transactions** : total cumulatif.
- **Feedback positif / négatif / neutre** : généralement sur échelle eBay-like.
- **Commentaires** : remarques textuelles des acheteurs post-transaction.
- **Tags et ranks** : « Trusted », « VIP », « Verified Vendor », selon le forum.
- **Historique des posts** : contributions aux discussions, activité communautaire.
- **Vouches externes** : mentions positives par d'autres vendeurs établis.

**Lecture analytique** :

- **Feedback 98%+** : probable vendeur sérieux (rares disputes, bien résolues).
- **Feedback 80-95%** : zone ambiguë — soit vendeur correct avec quelques problèmes, soit vendeur médiocre mais non scammer.
- **Feedback < 80%** : **red flag** — fuir.
- **Volume soudain en hausse** : peut signaler build-up avant exit (si opérateur) ou simplement succès légitime (si vendeur). À contextualiser.
- **Disputes récentes non résolues** : signal négatif croissant.
- **Changement de PGP** : **très rouge** — rachat de compte possible, compromis d'opérateur, acteur différent derrière le pseudo.

## 19.2 L'escrow

**Mécanisme standard** :

1. **Listing** : vendeur crée une annonce, précise prix, escrow délai attendu (typiquement 3-14 jours).
2. **Commande** : acheteur commande, **envoie le paiement au wallet de l'escrow du marché** (pas au vendeur).
3. **Vendeur expédie** : vendeur est notifié du paiement reçu, expédie le produit.
4. **Confirmation de réception** : acheteur reçoit le produit, marque la transaction comme « finalized ».
5. **Libération** : marché libère les fonds au wallet du vendeur (moins la commission).

**En cas de litige** :

- Acheteur ouvre un dispute : explique pourquoi (non-livraison, produit non conforme, produit de moindre qualité).
- Vendeur répond : fournit preuve d'expédition, tracking, explications.
- Modérateur/admin arbitre : décision (total à l'acheteur, total au vendeur, split 50/50 ou autre).
- Feedback mutuel : les deux parties peuvent laisser des commentaires, affectant les réputations futures.

**Finalize Early (FE)**. Option disponible sur certains marchés : l'acheteur libère les fonds **avant** réception. Utilisé par vendeurs extra-fiables comme avantage compétitif (évite la trésorerie bloquée). **Risque majeur pour acheteur** — si le produit n'arrive pas, aucun recours. FE est typiquement réservée aux vendeurs top-tier.

**Multi-sig escrow**. Variante avancée : les fonds sont verrouillés sur une adresse multi-signature (2-of-3 typiquement : acheteur, vendeur, arbitre). Libération nécessite 2 signatures sur 3. Pour le vendeur : paiement libéré si acheteur confirme (2-of-3). Pour l'acheteur : remboursement possible si arbitre valide le litige (2-of-3 avec vendeur ou, en dispute, arbitre + acheteur). Le marché ne détient jamais les fonds directement — réduction du risque d'exit scam de l'opérateur. Techniquement plus complexe, pas universellement adopté.

## 19.3 Le vouching

**Mécanisme**. Un membre établi de la communauté (« voucher ») publie un endorsement d'un nouveau membre ou d'un vendeur. Cet endorsement engage la réputation du voucher. Si le vouché scam, le voucher subit une pénalité (baisse de rank, bannissement temporaire, perte de privilèges de vouching).

**Variantes** :

- **Vouching ouvert** : le post de vouch est public, visible de tous.
- **Vouching privé** : confirmation transmise à l'admin du forum, qui valide le nouveau sans exposer le voucher.
- **Vouching transactionnel** : un membre atteste avoir réalisé une transaction avec succès avec le vouché.
- **Vouching caractérologique** : un membre atteste que le vouché est « sérieux », « honorable », sans nécessairement avoir transigé.

**Limites** :

- **Chain of vouches vulnérable** : si un voucher senior est compromis, tout ce qu'il a vouché est suspect.
- **Vouching mercenaire** : certains membres vendent leurs endorsements à prix. Pratique mal vue mais existe.
- **Sybil vouching** : un acteur contrôle plusieurs comptes et vouche lui-même ses propres comptes secondaires. Difficile à détecter dans les petits forums.

## 19.4 L'arbitrage

**Qui arbitre** :

- **Modérateurs** du forum/marché, habituellement pour les petites disputes.
- **Admins** pour les disputes importantes ou les affaires sensibles.
- **Tiers arbitre** : certains forums ont des arbitres indépendants (membres seniors mandatés) pour réduire le conflit d'intérêt des admins.

**Processus type** :

1. Une partie ouvre le dispute, expose les faits avec preuves (screenshots, hashes, tracking, communications).
2. L'autre partie répond sous 48-72h avec sa version.
3. L'arbitre demande preuves supplémentaires si besoin.
4. Décision rendue, souvent avec argumentaire publié (visibilité pour la communauté).
5. Exécution : les fonds sont libérés selon la décision.

**Types de décisions** :

- **Full refund acheteur** : vendeur reconnu scammer ou incapable de prouver l'expédition.
- **Full release vendeur** : acheteur reconnu de mauvaise foi (dispute frauduleux après réception).
- **Split 50/50 ou autre** : incertitude, pas de preuve décisive pour l'une ou l'autre partie.
- **Dispute closed sans décision** : rare, typiquement quand les deux parties disparaissent.

**Intégrité de l'arbitrage**. Un admin corrompu peut favoriser systématiquement une partie (vendeur cartel, vendeur qui paie des bakchichs, etc.). Les forums sérieux ont des **audit trails** et parfois des **appeals** à un niveau supérieur. Un pattern de décisions biaisées finit par être identifié par la communauté, érode la confiance, et peut faire chuter le forum.

## 19.5 L'économie de la confiance

Ce système crée une **économie de la confiance**. La réputation est un actif :

- **Transférable partiellement** : un vendeur établi peut « migrer » vers un nouveau forum en apportant des vouches de ses pairs. Il ne repart pas de zéro, mais ne bénéficie pas immédiatement de son rang maximal ailleurs.
- **Monétisable directement** : certains pseudonymes établis sont **vendus** sur des forums (rare, interdit par la plupart des règles, mais existe). Prix : 1 000-50 000 USD selon la force du pseudo.
- **Coûteuse à perdre** : un scam détruit des années de construction.

Pour l'analyste, l'économie de la confiance est un point d'attaque :

- Un acteur établi a beaucoup à perdre — les approches de type « coopération avec les autorités » ou « retournement » peuvent fonctionner là où un nouveau scammer ne céderait rien.
- Un scammer jetable est plus facile à identifier par patterns (neuf, prix bas, refus d'échantillon) mais aussi plus difficile à poursuivre (disparaît rapidement, pseudo sans histoire, pas de levier).

---
