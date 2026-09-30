---
title: PARTIE IV — ÉCONOMIE CLANDESTINE
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
chapter: 5
chapters: 10
---

> **Ce que cette partie apprend.** Comprendre **pourquoi** l'économie du dark web fonctionne malgré l'absence d'État, de contrats juridiquement exécutables, et de confiance interpersonnelle. Connaître les mécanismes (réputation, escrow, vouching, arbitrage), les pathologies (arnaques, exit scams, manipulation de la confiance), et les modèles économiques criminels qui structurent l'écosystème.
>
> **Ce qu'elle ne couvre pas.** Les techniques d'investigation de ces économies (Partie V), les analyses de traçage financier (Ch.31), les éléments réglementaires qui tentent de les contrer (Ch.40).
>
> **Ce que vous saurez faire après cette partie.** Lire un escrow pour y repérer les signaux d'intégrité, détecter les prémices d'un exit scam, situer un acteur dans un modèle économique (IAB, courtier, opérateur), et comprendre les incitations qui gouvernent les comportements observés.

---

## Chapitre 18 — Pourquoi l'économie du dark web fonctionne

À première vue, l'économie du dark web devrait être impossible. Des inconnus anonymes transigent pour des montants significatifs sans tribunaux, sans contrats exécutables, sans banque centrale, sans identité vérifiée. La tentation d'arnaque devrait être permanente et dévastatrice. Pourtant, des dizaines de millions de transactions se déroulent chaque année, avec un taux de complétion relativement élevé. Comprendre pourquoi c'est un problème économique fondamental — et sa solution éclaire l'investigation.

### 18.1 Le problème du trust sans tiers de confiance

Toute transaction économique pose un **problème de confiance**. Le vendeur craint le non-paiement, l'acheteur craint la non-livraison. Dans une économie classique, ce problème est résolu par plusieurs instruments :
- **Tribunaux** : en cas de litige, une juridiction neutre tranche selon un droit écrit.
- **Contrats** : engagements formalisés exécutables.
- **Intermédiaires** : banques, cartes de crédit avec mécanisme de chargeback, plateformes avec garanties.
- **Identité publique** : les parties sont identifiées, leur réputation est documentée, les arnaques laissent des traces traçables.

Dans le dark web, **aucun de ces instruments classiques n'est disponible**. Les parties sont pseudonymes, il n'y a pas de tribunal applicable aux transactions illégales, les paiements crypto sont irréversibles (pas de chargeback), aucune autorité ne peut légitimement contraindre une partie à exécuter.

Comment l'économie fonctionne-t-elle alors ? La réponse : par un **système de substitution institutionnelle** — les forums, marchés et communautés créent des institutions privées qui remplacent fonctionnellement les institutions publiques manquantes.

### 18.2 Les institutions de substitution

**La réputation individuelle persistante**. Chaque pseudonyme a un historique transactionnel, des reviews, des feedbacks. Un pseudonyme avec 500 transactions réussies et 2 ratings négatifs est plus digne de confiance qu'un pseudonyme avec 3 transactions. La **réputation est le capital principal** d'un acteur sérieux — et la perdre est coûteux (repartir de zéro sous un nouveau pseudo, temps d'accumulation de 6-18 mois).

**L'escrow de forum ou marché**. Mécanisme de dépôt : l'acheteur envoie le paiement à un tiers (le forum ou le marché), qui le retient jusqu'à confirmation de livraison. Si l'acheteur confirme, le vendeur est payé. Si litige, arbitrage. Ce mécanisme, quoique imparfait, réduit drastiquement le risque d'arnaque unilatérale (Ch.19).

**Le vouching (parrainage)**. Un membre établi engage sa propre réputation en garantissant un nouveau. Si le nouveau scam, le parrain est pénalisé. Cette **chaîne de confiance transitive** permet d'accepter des nouveaux sans qu'ils partent de zéro total.

**L'arbitrage communautaire**. En cas de litige, les modérateurs ou admins tranchent selon des principes publiés (règles du forum, précédents). La **publication du jugement** fait fonctionner le système — un vendeur déclaré scammer voit son pseudonyme sali sur toute la plateforme, souvent cross-platform.

**La pression sociale et la communauté**. Les forums actifs ont une **mémoire collective**. Les scammers notoires sont connus, leurs pseudonymes listés publiquement, leurs IPs parfois publiées. Cette publicité sociale fonctionne comme un ban industriel — un scammer identifié est grillé dans tout l'écosystème pour des mois.

**Les blacklists cross-forum**. Certains forums partagent leurs listes de bannis. Un scammer banni sur XSS peut se retrouver banni préventivement sur Exploit. Cette coordination inter-forums est imparfaite mais réelle.

### 18.3 La coûteuse construction de réputation

Pour un acteur sérieux, construire une réputation utilisable prend **6-18 mois au minimum**. Le processus typique :

**Mois 1-3 — entrée**. Création du compte sur un forum, posts de présentation, participation à des discussions. Lecture active, apprentissage des codes. Pas de vente immédiate (interdit par les règles de la plupart des forums sérieux pour les nouveaux).

**Mois 3-6 — premières transactions**. Petites ventes (50-500 USD), avec échantillons gratuits pour démontrer la qualité. Chaque transaction réussie ajoute une review positive. Les premiers 10-20 transactions sont les plus difficiles — pas encore de réputation établie, les acheteurs sont prudents.

**Mois 6-12 — consolidation**. Avec ~30-50 transactions réussies, le vendeur est **trusted**. Prix peuvent monter, qualité/spécificité de l'offre plus haute, accès aux zones premium du forum. Les gains commencent à être significatifs.

**Mois 12+ — établissement**. Après 100+ transactions, le vendeur est une figure reconnue. Clients récurrents, accès à des produits premium (0-day, accès corporate haut de gamme). Revenus potentiels de plusieurs centaines de milliers à plusieurs millions USD/an.

**Cette courbe explique plusieurs comportements** : les scammers ont tendance à opérer en rafales courtes (2-4 semaines de scam intensif, puis abandon du pseudo), parce que construire une réputation sérieuse prend trop de temps pour le petit gain à court terme. Les acteurs sérieux protègent leur réputation — ne scamment pas leurs clients, parce que la valeur actualisée de leur réputation est bien supérieure au gain d'un scam.

### 18.4 Les ruptures de confiance

Malgré ces mécanismes, les ruptures se produisent.

**Exit scams par opérateur**. Traitement Ch.20. Un opérateur de marché ou forum s'enfuit avec les fonds en escrow.

**Vendeurs seniors qui scamment**. Rare mais arrive. Un vendeur avec 500 transactions et excellente réputation qui scam massivement en une seule opération finale. Motivation : gain ponctuel considérable avec perte de la réputation acceptée. Plus fréquent quand le vendeur sent que sa réputation va tomber de toute façon (arrestation imminente, conflit interne).

**Attaques externes**. Un forum compromis par les forces de l'ordre ou par des concurrents peut voir son historique de transactions falsifié, ses escrows volés, ses membres dox. Disruption temporaire ou définitive de l'économie locale.

**Cyclic collapse**. Parfois, une cascade de méfiance se déclenche : un vendeur majeur scam → les acheteurs méfiants retirent leurs fonds en masse → l'opérateur ne peut honorer les retraits → exit scam de l'opérateur → plateforme fermée. Panique bancaire, version dark web.

### 18.5 Pourquoi ça marche malgré tout

Mathématiquement, l'économie fonctionne parce que :
- **Le nombre de transactions honnêtes dépasse les transactions frauduleuses**. Les acteurs sérieux, majoritaires en nombre et en volume, dominent l'activité globale.
- **La perte de réputation est coûteuse**. Pour un acteur établi, le gain d'un scam est typiquement inférieur à la valeur actualisée de sa réputation. L'incitation rationnelle est d'honorer les transactions.
- **Les mécanismes de substitution capturent la plupart des cas**. Escrow, arbitrage, blacklists gèrent la majorité des litiges.
- **Les pertes sont partagées**. Les acheteurs savent qu'un certain pourcentage de transactions échoueront. Ils calculent cette « taxe » dans leur modèle économique.

Pour un analyste, ces mécanismes sont autant de **points d'observation**. Un vendeur qui sort du schéma standard (pseudonyme neuf, pas de vouching, prix très bas, refus d'échantillon) est en probabilité très élevée un scammer — ce qui influe sur la priorisation des pistes d'investigation.

---

## Chapitre 19 — Réputation, escrow, vouching, arbitrage

Approfondissement des mécanismes fiduciaires du dark web. Ce chapitre détaille comment ils fonctionnent concrètement et comment l'investigateur peut les lire.

### 19.1 Le système de réputation

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

### 19.2 L'escrow

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

### 19.3 Le vouching

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

### 19.4 L'arbitrage

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

### 19.5 L'économie de la confiance

Ce système crée une **économie de la confiance**. La réputation est un actif :
- **Transférable partiellement** : un vendeur établi peut « migrer » vers un nouveau forum en apportant des vouches de ses pairs. Il ne repart pas de zéro, mais ne bénéficie pas immédiatement de son rang maximal ailleurs.
- **Monétisable directement** : certains pseudonymes établis sont **vendus** sur des forums (rare, interdit par la plupart des règles, mais existe). Prix : 1 000-50 000 USD selon la force du pseudo.
- **Coûteuse à perdre** : un scam détruit des années de construction.

Pour l'analyste, l'économie de la confiance est un point d'attaque :
- Un acteur établi a beaucoup à perdre — les approches de type « coopération avec les autorités » ou « retournement » peuvent fonctionner là où un nouveau scammer ne céderait rien.
- Un scammer jetable est plus facile à identifier par patterns (neuf, prix bas, refus d'échantillon) mais aussi plus difficile à poursuivre (disparaît rapidement, pseudo sans histoire, pas de levier).

---

## Chapitre 20 — Arnaques, exit scams et manipulation de la confiance

Malgré les mécanismes de confiance, l'arnaque est structurelle dans l'écosystème. Ce chapitre cartographie les grandes catégories, leurs mécanismes, et leurs signaux.

### 20.1 Taxonomie des arnaques

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

### 20.2 Signaux de scam typiques

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

### 20.3 Comment se protéger (pour acheteur, pour investigateur)

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

### 20.4 Les grands exit scams

Historique sélectif.

**Evolution Market (mars 2015)**. Ex-second plus grand marché de l'époque. Admins « Verto » et « Kimble » disparaissent avec environ 12 M USD de BTC en escrow. Communauté anéantie, migration massive vers Abraxas puis AlphaBay.

**Nucleus (avril 2016)**. Exit scam plus modeste, ~5 M USD.

**Empire Market (août 2020)**. ~30 M USD, un des plus gros de l'histoire. Admins s'évaporent sans annonce. Les spéculations ont évoqué soit exit volontaire, soit compromission par un tiers, soit panic mid-course face à une menace judiciaire.

**Monopoly Market (2023)**. Saisi par les autorités mais au même moment, des signaux d'exit étaient présents — confusion post-hoc sur le réel séquencement.

**Incognito Market (2024)**. Modèle hybride — exit scam avec menace de dox des utilisateurs non-payeurs.

### 20.5 La gestion d'un exit scam côté analyste

Quand un exit scam se produit sur un forum suivi, l'analyste peut :

**Capturer immédiatement** les dernières observations avant que le forum disparaisse (posts actifs, pseudonymes actifs, annonces récentes). Le forum peut re-disparaître définitivement.

**Monitorer la migration**. Les membres scammed se regrouperont sur d'autres forums, souvent avec posts « je viens de perdre 20k sur Empire, quelqu'un a des nouvelles ». Ces posts sont **riches en renseignement** — ils exposent des pseudonymes, des patterns de transaction, des sommes.

**Suivre les wallets**. Si l'admin exit scam, les fonds transitent. Les adresses reçoivent de gros montants en peu de temps, puis se dispersent. Tracking on-chain (Chainalysis, TRM) peut révéler des patterns (où vont les fonds, quelle méthode de blanchiment) et potentiellement identifier l'opérateur.

**Documenter**. Même si l'investigation ne peut pas pénaliser l'exit scammer, la documentation nourrit la connaissance de l'écosystème — profils d'admins, patterns d'opération, durées de vie typiques.

---

## Chapitre 21 — Modèles économiques criminels

Synthèse des modèles économiques observés sur le dark web. Ce chapitre articule les rôles de la Partie III en modèles financiers cohérents.

### 21.1 Le modèle du vendeur individuel

**Acteur** : individu ou petite équipe (1-5 personnes).

**Produit** : spécialisé — drogues, fullz, credentials, documents contrefaits, petits services.

**Volumes** : dizaines à centaines de transactions par mois.

**Revenus annuels** : 50 k - 500 k USD typiquement, jusqu'à quelques millions pour les meilleurs.

**Risques** : identification via patterns (timing, OPSEC faible), erreurs opérationnelles (réutilisation pseudonyme, leaks personnels), dispute avec un gros acheteur qui dox.

**Exemples publics** : les vendeurs condamnés sont légion dans la presse judiciaire US, UK, DE. Exemples emblématiques : « Xanax King » condamné pour vente de faux Xanax sur AlphaBay (2017-2019) ; multiples dealers saisis lors d'operations police.

### 21.2 Le modèle de l'opérateur de plateforme

**Acteur** : équipe structurée (5-20 personnes).

**Produit** : infrastructure + arbitrage pour la communauté.

**Revenus** : commissions sur transactions + fees + services premium. Quelques millions à dizaines de millions USD/an pour les grandes plateformes.

**Risques** : saisie (multiple précédents), exit scam devenant la sortie rationnelle, conflits internes, DDoS concurrents.

**Exemples** : Ulbricht (Silk Road), Cazes (AlphaBay), Khoroshev (LockBit). Plus récemment : Baphomet (BreachForums multiple).

### 21.3 Le modèle RaaS

**Acteur** : équipe opérationnelle (10-50 personnes au core).

**Produit** : ransomware + infrastructure + service aux affiliés.

**Revenus** : 20-30% des paiements de rançon perçus par les affiliés. Dizaines de millions USD/an pour les groupes dominants.

**Exemples** : LockBit (estimations 500 M+ USD cumulés 2020-2024 avant Cronos), Conti (estimé ~180 M USD dans la leak 2022), ALPHV (~22 M USD Change Healthcare avant disparition), Black Basta (estimations 100 M+ USD).

**Risques** : saisies d'infrastructure, inculpations nominales (LockBitSupp), conflits d'affiliés, érosion post-disruption (LockBit qui peine à rebondir).

### 21.4 Le modèle de l'IAB

**Acteur** : individu ou petite équipe.

**Produit** : accès préqualifiés.

**Volumes** : 10-50 accès vendus par an.

**Revenus** : 500-50 000 USD par accès, selon qualité. Revenus annuels typiques 200 k - 2 M USD.

**Risques** : identification via l'accès lui-même (si l'acheteur est infiltré, les comms peuvent remonter à l'IAB), erreurs d'OPSEC dans la compromission initiale.

### 21.5 Le modèle du service provider (CaaS)

**Acteur** : opérateur d'un service — phishing kit, DDoS booter, malware-as-service, etc.

**Produit** : service récurrent avec abonnement.

**Revenus** : abonnements (50-1 000 USD/mois par utilisateur), jusqu'à dizaines de milliers d'utilisateurs pour les plus grands. Revenus annuels de 100 k à 10 M USD selon scale.

**Exemples** : Lumma Stealer (estimation sur plusieurs milliers d'abonnés × 250 USD/mois), LabHost avant démantèlement.

**Risques** : saisies (LabHost démantelé avril 2024), inculpations d'opérateurs.

### 21.6 Le modèle de blanchiment

**Acteur** : spécialistes financiers, souvent liés à l'écosystème crypto.

**Produit** : conversion crypto → fiat utilisable.

**Revenus** : commissions 10-30% du montant blanchi. Volumes considérables possible — plusieurs entités (Suex, Bitzlato, Garantex historiquement, Chipmixer) ont traité des milliards USD avant saisie/sanction.

**Risques** : sanctions OFAC (Suex, Bitzlato, Garantex sanctionnés), saisies (Chipmixer mars 2023, Samourai avril 2024), inculpations (Larry Harmon condamné pour Helix, Alexey Pertsev pour Tornado Cash).

### 21.7 Le modèle de l'hébergeur bulletproof

**Acteur** : opérateur d'infrastructure.

**Produit** : hosting résistant.

**Revenus** : abonnements de hosting premium. Centaines à milliers de clients, 500-10 000 USD/mois chacun.

**Risques** : saisies (Cyberbunker 2019, multiples avant), pression upstream (de-peering, blocages).

### 21.8 La convergence des modèles

Les modèles se chevauchent et convergent. Un acteur peut opérer comme IAB **et** affilié RaaS, comme développeur malware **et** opérateur d'un service CaaS, comme plateforme **et** commanditaire de ransomware. Cette **polymorphie économique** rend l'attribution fine complexe.

Le dark web économique 2025-2026 est mieux décrit comme un **réseau de spécialistes interconnectés** que comme un écosystème de rôles purs. Un même individu ou groupe peut jouer plusieurs rôles selon les opportunités, les contraintes, les rythmes.

### 21.9 Implications analytiques

Pour l'analyste, cette structure économique suggère plusieurs focus.

**Suivre les flux financiers** : chaque modèle produit des patterns crypto distinctifs. Les IAB reçoivent des paiements moyens, les RaaS reçoivent de très gros paiements épisodiques, les stealer operators reçoivent des flux constants de petits paiements. Chainalysis et équivalents peuvent identifier le modèle économique par profil transactionnel.

**Reconstruire les chaînes de valeur** : identifier le modèle économique d'un acteur aide à identifier ses partenaires amont/aval. Un IAB « accès manufacturing EU » est probablement lié à un groupe RaaS anglophone ; un opérateur de stealer logs alimente des IAB multiples.

**Anticiper les transformations** : les modèles évoluent. Un vendeur individuel peut devenir IAB en montant en gamme, un IAB peut fonder son propre groupe RaaS, un opérateur RaaS peut se retirer en blanchisseur. L'analyste suit ces trajectoires pour anticiper les tendances.

**Calibrer l'attribution** : chaque modèle a ses OPSEC typiques. Un vendeur individuel fait plus d'erreurs personnelles ; un opérateur RaaS opère avec plus de rigueur ; un service provider a des infrastructures plus visibles. L'attribution est plus facile sur certains profils que sur d'autres.

---
