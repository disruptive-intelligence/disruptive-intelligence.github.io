---
title: 'Chapitre 20 — Outils professionnels : Chainalysis, TRM Labs, Elliptic'
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IV — Outils ET workflow
  - index.md
---

Les **outils professionnels de blockchain intelligence** sont les standards de l’industrie. Ils ne sont pas des « explorateurs en mieux » — ce sont des plateformes intégrées avec capacités cluster, label, scoring, visualisation, et workflow. Ce chapitre couvre les trois leaders et leur usage concret.

## 20.1 Le marché des outils pro

**Chainalysis** (US, fondé 2014). Leader historique. Solutions :

- **Reactor** : investigation forensique (l’outil détaillé ici).
- **KYT (Know Your Transaction)** : screening AML temps réel pour exchanges/banques.
- **Crypto Investigations Solution** : suite complète pour LEA (Law Enforcement Agencies).

**TRM Labs** (US, fondé 2018). Concurrent direct. Solutions :

- **Forensics / Investigations** : équivalent Reactor.
- **Know Your VASP** : risk rating sur exchanges et services.
- **Tactical Intelligence** : suite LEA.

**Elliptic** (UK, fondé 2013). Solutions :

- **Investigator** : plateforme forensique.
- **Discovery** : screening AML.
- **Lens** : monitoring DeFi.

**Autres acteurs** : CipherTrace (Mastercard), Crystal (Bitfury), Scorechain, Merkle Science, Coinpath / Bitquery, Glassnode (analytics), Nansen (Ethereum/Solana retail), Spot On Chain.

**Différenciateurs** :

- **Couverture** : nombre de chaînes supportées.
- **Profondeur de labels** : taille de la base label propriétaire.
- **Qualité de clustering** : précision des heuristiques.
- **UX et workflow** : ergonomie pour analystes quotidiens.
- **Prix** : varie de 30 k USD/an (petits tiers) à 500 k+ USD/an (full enterprise).

**Pour l’analyste polyvalent** : maîtriser **au moins un** des trois leaders (Chainalysis ou TRM ou Elliptic) est un standard de la profession. La maîtrise d’un permet apprentissage rapide des autres (logiques similaires).

## 20.2 Chainalysis Reactor : walkthrough

**Reactor** est le produit d’investigation phare de Chainalysis. Référence industrie.

**Interface** :

- **Search bar** : entrée par adresse, TXID, nom d’entité.
- **Graph view** : visualisation interactive des flux.
- **Wallet view** : vue détaillée d’un cluster.
- **Tracking** : suivi de fonds depuis un point de départ.
- **Reports** : génération de rapports.

**Workflow type pour enquête** :

**1. Saisir l’adresse de départ**. Reactor charge le **cluster** auquel elle appartient (basé sur heuristiques + labels propriétaires).

**2. Examiner le cluster** :

- Combien d’adresses dans le cluster.
- Solde total.
- Volume cumulé entrant/sortant.
- **Label propriétaire** si attribué (« Binance », « Tornado Cash », etc.).
- Risk score.

**3. Visualiser les flux**. Reactor affiche un graphe interactif où :

- Les nœuds sont des **clusters** (pas adresses individuelles), simplifiant la vue.
- Les arêtes représentent les flux entre clusters, avec montants agrégés.
- Couleurs encodent les types d’entités (exchange, mixer, sanctioned, unknown).

**4. Drill down**. Cliquer sur un nœud pour voir les adresses du cluster, les transactions, les flux.

**5. Tracking automatisé**. Reactor permet de suivre les flux depuis un point de départ, automatiquement, à travers multiple hops, en identifiant les services traversés. Excellent pour peeling chains et dispersions.

**6. Cross-chain tracking**. Reactor suit les flux à travers les bridges (avec couverture variable selon les bridges supportés).

**7. Export et rapport**. Génère des rapports avec graphes, listes d’adresses, captures pour intégration dans rapport externe.

## 20.3 TRM Labs Investigations : walkthrough

**TRM Labs Investigations** est l’équivalent. Logique similaire avec quelques différences.

**Forces TRM** :

- **Couverture multi-chaînes** souvent saluée.
- **Labels** sur exchanges régulés et VASPs (couplé à Know Your VASP, fort sur compliance).
- **UX** moderne, workflow fluide.
- **Risk rating** intégré, exploitable pour décisions AML.

**Différences avec Chainalysis** :

- Bases label distinctes (chaque vendor a fait sa recherche).
- Heuristiques de clustering avec calibrations différentes.
- UX différente, préférences personnelles.

**Bonne pratique** : **valider croisée** en utilisant TRM en complément de Chainalysis. Si les deux outils convergent sur une attribution / cluster, confiance plus élevée.

## 20.4 Elliptic Investigator : walkthrough

**Elliptic Investigator** complète le trio.

**Forces Elliptic** :

- Solide intégration avec écosystème AML traditionnel.
- Capacités spécifiques DeFi via Elliptic Lens.
- Présence forte UK/Europe.

**Logique similaire** aux deux autres. Workflow : adresse → cluster → flux → labels → rapport.

## 20.5 Limites des outils pro

Ne pas idéaliser. Limites communes :

**Boîtes noires partielles**. Les heuristiques de clustering et les bases label sont propriétaires. L’analyste ne peut pas toujours **vérifier** comment un label a été attribué. Risque : faire confiance aveugle à une « vérité » de l’outil. Discipline : qualifier la source d’un label, croiser quand important.

**Erreurs persistantes**. Tous les outils ont des erreurs (clusters faux, labels obsolètes ou erronés). Réduits dans le temps mais non éliminés. La validation croisée et l’OSINT externe sont sécurisations.

**Couverture incomplète**. Certaines chaînes sont moins bien couvertes (Solana, certaines Layer-2, Cosmos écosystème). Performance varie.

**Lag temporel**. Les outils mettent à jour leurs bases label avec délai. Une adresse récemment attribuée peut ne pas être dans la base au moment de l’enquête.

**Coût**. Peu accessibles aux petites structures, journalistes indépendants, chercheurs académiques.

**Risque de dépendance**. Une organisation 100% dépendante d’un outil unique est vulnérable (changement contractuel, faillite, conflit). Diversifier.

## 20.6 Quand utiliser quoi

**Reactor / TRM / Elliptic** :

- Investigations à enjeu (paiements ransomware, gros vols, dossiers judiciaires).
- Clusters complexes nécessitant heuristiques avancées.
- Cross-chain tracking.
- Labels propriétaires nécessaires.
- Rapports formels.

**Outils gratuits** (Ch.19) :

- Vérifications ponctuelles.
- Analyses de routine.
- Cas simples bien circonscrits.
- Validation croisée.
- Recherche académique sans budget.

**Combinaison** :

- Étude pro pour analyse principale.
- Outils gratuits pour vérifications, captures publiques (les rapports peuvent référer à Mempool/Etherscan, plus accessible que captures Reactor pour le lecteur externe).

## 20.7 Fil rouge — MIXSHADOW : workflow Chainalysis + TRM

> **🔗 MIXSHADOW — Épisode 13 : usage des outils pro**
> 
> Sarah utilise **Chainalysis Reactor** comme outil principal et **TRM Labs Investigations** en validation croisée pour MIXSHADOW.
> 
> **Avantages observés** :
> 
> - **Reactor** identifie le cluster Akira BTC operational comme regroupant ~120 adresses (incluant les hops du peeling chain). Sans Reactor, Sarah avait identifié manuellement 62 adresses ; le cluster en révèle 60+ supplémentaires (extensions du peeling chain ou activités annexes du même opérateur).
> - **TRM** confirme le cluster avec ~115 adresses (légère différence de heuristiques, normale). Convergence sur l’essentiel — confiance élevée que le cluster est bien réel et attribué à un acteur Akira.
> - **Reactor** permet de tracker automatiquement les flux à partir du wallet Akira, en suivant à travers les services (FixedFloat, exchanges non-KYC). Visualisation graphe en quelques clics.
> - **TRM Risk Rating** sur les exchanges traversés : exchange non-KYC X est rated « very high risk », confirmant l’angle d’investigation.
> - **Labels propriétaires** : TRM identifie les Hubs TRON suspects comme « probable laundering service, internal cluster » — confirme l’hypothèse Sarah formulée par patterns. Le service n’est pas publiquement connu mais TRM le suit en interne.
> 
> **Limites observées** :
> 
> - **Solana** : un sous-flux mineur transite par Solana en cours de mission. La couverture Reactor est moins profonde sur Solana, certaines transactions ne sont pas labellisées. Sarah complète manuellement.
> - **Tornado Cash sorties** : aucun outil ne « démixe » Tornado Cash directement. Les capacités d’analyse statistique des sorties sont disponibles mais probabilistes, pas certaines.
> - **Erreur ponctuelle** : sur une transaction, Reactor labelise un destinataire comme « Binance hot wallet » alors qu’investigation manuelle révèle que c’est en fait un autre exchange (Bitstamp). Sarah signale l’erreur à Chainalysis support pour mise à jour. Discipline de validation croisée a évité une erreur dans le rapport.
> 
> Sarah produit ses graphes finaux via Reactor (pour visualisations propres), exporte les listes d’adresses, et complète avec captures Mempool/Etherscan/Tronscan pour les éléments référés dans le rapport.
> 
> Le coût des outils est justifié par le résultat : sans Reactor + TRM, l’enquête serait probablement 3x plus longue, avec couverture 50% inférieure. C’est l’investissement qui rend Athéna compétitif.

-----
