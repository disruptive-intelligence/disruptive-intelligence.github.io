---
title: PARTIE III — MÉTHODOLOGIE D’ENQUÊTE
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
chapter: 4
chapters: 10
---

> **Ce que cette partie apprend.** Structurer l’enquête crypto comme une démarche méthodologique, pas comme une exploration intuitive. Construire des fiches d’adresses opérationnelles, démarrer une enquête depuis n’importe quel indice, raisonner de l’indice au graphe, visualiser les flux de manière lisible, gérer la temporalité, comprendre les promesses et limites du clustering, calibrer l’attribution.
> 
> **Ce qu’elle ne couvre pas.** Les outils précis (Partie IV), les typologies d’abus (Partie V), les techniques d’obfuscation (Partie VI).
> 
> **Ce que vous saurez faire après cette partie.** Conduire une enquête crypto structurée et reproductible, depuis un indice initial jusqu’à une analyse calibrée, avec graphes lisibles, hypothèses formulées proprement, et niveaux de confiance documentés.

-----

## Chapitre 12 — Construire une fiche d’adresse

La **fiche d’adresse** est l’unité documentaire de base de l’enquête crypto. Pour chaque adresse pertinente, l’analyste constitue une fiche structurée qui synthétise tout ce qu’il sait. Les fiches s’agrègent en graphe d’enquête. Sans fiche, l’enquête se dilue dans le flou.

### 12.1 Pourquoi la fiche d’adresse

Trois fonctions :

**Mémoire**. L’enquête sur 50 adresses, sur 8 semaines, ne peut pas tenir « dans la tête ». La fiche externalise la mémoire et permet de retrouver instantanément ce qu’on sait sur une adresse spécifique.

**Communication**. Quand Sarah doit briefer la DGSI ou son directeur Athéna sur l’enquête, les fiches d’adresses sont son support. Synthèse précise, vérifiable.

**Calibration**. Tenir une fiche oblige à expliciter ce qu’on sait, ce qu’on suppose, et ce qu’on ne sait pas. Discipline anti-confusion entre observation et inférence.

### 12.2 Le template fiche d’adresse

Modèle complet à adapter selon l’enquête. À retrouver en Annexe B.

```markdown
# Fiche adresse — [Identifiant abrégé]

## Identification
- **Adresse complète** : [adresse exacte 42-56 caractères]
- **Blockchain** : [Bitcoin / Ethereum / TRON / Solana / etc.]
- **Type d'adresse** : [P2PKH / P2SH / SegWit / Taproot / EOA / Contract / autre]
- **Identifiant interne enquête** : [Akira-BTC-007 par exemple]

## Activité observable
- **Première transaction** : [date UTC, TXID]
- **Dernière transaction** : [date UTC, TXID]
- **Nombre total de transactions** : [N]
- **Solde actuel** : [montant et actif]
- **Actifs reçus historiques** : [montants par actif]
- **Actifs envoyés historiques** : [montants par actif]

## Contreparties
- **Adresses contreparties principales** : [top 5-10 par volume]
- **Services labellisés impliqués** : [exchanges, mixers, bridges identifiés]
- **Cluster Chainalysis (ou TRM)** : [ID cluster + nb adresses + label si applicable]

## Labels publics
- **Labels Etherscan / Tronscan / Mempool** : [liste]
- **Labels propriétaires Chainalysis / TRM** : [si accès]
- **Sanctions OFAC** : [oui/non + détail si oui]
- **Mentions OSINT** : [forums, presse, twitter, etc.]

## Hypothèses
- **Hypothèse principale** : [ex : « adresse de réception ransomware Akira »]
- **Niveau de confiance** : [WEP : très probable / probable / possible / spéculatif]
- **Hypothèses alternatives** : [autres explications possibles, à noter]
- **Éléments de preuve** : [observations supportant l'hypothèse principale]
- **Éléments d'incertitude** : [observations qui pourraient contredire ou nuancer]

## Captures et sources
- **Captures de pages d'explorateur** : [liens vers fichiers archivés + hashes]
- **Sources externes** : [URL forums, presse, etc.]
- **Cross-check effectués** : [outils utilisés, dates]

## Statut enquête
- **Date de création de la fiche** : YYYY-MM-DD
- **Dernière mise à jour** : YYYY-MM-DD
- **Statut** : [Active / Surveillance / Clôturée]
- **Investigateur** : [nom]
- **Liens vers fiches connexes** : [autres adresses du graphe]
```

### 12.3 Renseigner la fiche : ordre méthodologique

**Étape 1 — Identification**. Saisie immédiate dès qu’une adresse entre dans le périmètre d’enquête. Vérifier la blockchain (erreur classique : adresse Ethereum rentrée comme adresse Bitcoin).

**Étape 2 — Activité observable**. Lecture sur explorateur principal (Mempool, Etherscan, Tronscan). Captures systématiques. Hash de chaque capture.

**Étape 3 — Contreparties**. Lister les adresses qui ont reçu/envoyé. Pour les top contreparties (par volume), noter et identifier si elles sont dans le périmètre d’enquête ou nouvelles.

**Étape 4 — Labels**. Vérifier sur explorateurs publics. Si accès aux outils pro, croiser. Sanctions OFAC : vérifier sur SDN list.

**Étape 5 — OSINT externe**. Recherche sur l’adresse dans Google, Twitter, forums (parfois des adresses sont publiquement associées à des services ou acteurs). Recherche sur DeHashed/IntelX au cas où l’adresse apparaît dans des leaks. Cf. cours **Dark Web** et **OSINT Mastery** pour méthodes.

**Étape 6 — Hypothèses**. Formuler explicitement. Calibrer la confiance.

**Étape 7 — Documentation**. Toutes les sources, captures, dates.

### 12.4 Le piège de la fiche prématurée

Une fiche peut **figer prématurément** une hypothèse. Tentation : nommer l’adresse « Akira-Hot-Wallet-3 » alors qu’on ne sait pas encore que c’est un hot wallet d’Akira.

**Bonne pratique** :

- Identifiant interne **neutre** au début (« BTC-Investigation-007 ») jusqu’à preuve d’attribution suffisante.
- Hypothèse principale **calibrée** : « possible adresse de blanchiment Akira (confiance 50%) » plutôt que « adresse Akira ».
- **Mises à jour** quand de nouvelles infos arrivent. La fiche évolue.

### 12.5 Maintien de la fiche dans le temps

Une fiche n’est pas un document one-shot. Elle évolue.

**Mises à jour quotidiennes** pour adresses actives en surveillance.

**Vérification hebdomadaire** pour adresses moins actives.

**Reprise complète** lors de tournants d’enquête (nouvel angle, validation/invalidation d’hypothèse).

**Versioning** : noter les versions successives, dater chaque mise à jour. Outils Git ou systèmes de fichiers avec horodatage suffisent.

### 12.6 Fiches et graphe

Les fiches s’articulent en **graphe** :

- Chaque fiche = un **nœud**.
- Les contreparties identifiées = **arêtes** vers d’autres fiches.
- Les patterns (peeling chain, consolidation) sont représentés par séquences d’arêtes.

Outils de visualisation (Ch.21) consomment ce graphe pour produire des vues exploitables.

-----

## Chapitre 13 — Point de départ d’une enquête : typologie d’indices

L’enquête crypto démarre toujours par un **indice initial**. Sa nature détermine les premières actions et oriente l’enquête. Ce chapitre cartographie les types d’indices et la méthode pour les exploiter.

### 13.1 Adresse fournie par une victime

**Cas typique** : pig butchering. La victime communique l’adresse à laquelle elle a envoyé ses fonds.

**Étapes** :

1. **Vérifier la blockchain**. La victime peut se tromper — elle dit « Bitcoin » alors qu’elle a envoyé USDT-TRON. Demander captures de transaction.
1. **Récupérer le TXID** si possible. Avec le TXID, on a une preuve plus solide que juste l’adresse.
1. **Lire la transaction sur explorateur**. Montant, timestamp, adresse de destination.
1. **Constituer fiche** sur l’adresse de destination.
1. **Suivre les flux sortants**. La destination redistribue probablement vers d’autres adresses.

### 13.2 Transaction hash (TXID)

**Cas typique** : alerte SOC sur transaction suspecte, victime de hack ayant capté la transaction de drain.

**Étapes** :

1. Identifier la blockchain (parfois implicite, parfois à vérifier).
1. Lire la transaction complète.
1. Identifier les parties (from, to, montants).
1. Étendre l’enquête depuis ces parties.

### 13.3 Capture d’écran

**Cas typique** : victime envoie capture de la confirmation reçue d’un wallet, screenshot Telegram, photo de QR code.

**Étapes** :

1. **Extraire l’adresse ou TXID** lisiblement de la capture (parfois OCR utile).
1. **Vérifier l’authenticité** : la capture peut être falsifiée. Recouper avec on-chain (l’adresse a-t-elle bien reçu cette transaction à ce timestamp ?).
1. Procéder ensuite comme avec adresse/TXID.

**Piège** : QR code dans la capture. Le décoder (outils en ligne, smartphone). Vérifier qu’il pointe bien vers l’adresse mentionnée.

### 13.4 Lien de paiement / payment URI

**Format BIP-21 Bitcoin** : `bitcoin:bc1q...?amount=0.5&label=Donation`.

**Format Ethereum** : `ethereum:0x...?value=1000000000000000000`.

**Étapes** :

1. Décoder l’URI.
1. Vérifier l’adresse extraite.
1. Procéder comme avec adresse classique.

### 13.5 Email de rançon

**Cas typique** : ransomware, sextortion, fausses menaces.

**Contenu type** : adresse Bitcoin/Monero pour paiement, montant demandé, deadline, instructions.

**Étapes** :

1. **Extraire l’adresse**.
1. Vérifier sur blockchain : a-t-elle été utilisée pour d’autres demandes de rançon (fiche enrichie de l’écosystème ransomware) ? A-t-elle reçu des paiements ?
1. **Croiser** avec bases publiques (databases ransomware tracking, AnyRun, autres).
1. Si sextortion classique de masse, l’adresse peut apparaître dans des centaines/milliers d’emails — pattern de fraude reconnaissable.
1. Si ransomware ciblé, adresse souvent fraîche, dédiée à la victime.

### 13.6 Message Telegram / canal

**Cas typique** : opérateurs ransomware via canaux Telegram, scammers via groupes Telegram, vendeurs de données.

**Étapes** :

1. **Documenter le contexte** : nom du canal, date du message, contenu.
1. Extraire les adresses crypto mentionnées.
1. Suivre méthodologie standard.
1. **Croiser** avec d’autres mentions du canal/acteur.

**Important** : pas de contact direct avec le canal sans cadre clair. Observation passive uniquement pour OSINT.

### 13.7 Wallet trouvé dans un malware

**Cas typique** : analyse de malware ransomware / clipper / stealer qui contient une adresse hardcodée.

**Étapes** :

1. Reverse engineering du malware (compétence cyber, voir cours **Forensique** ou **APT**).
1. Extraction de l’adresse hardcodée ou des adresses générées dynamiquement.
1. Procéder comme avec adresse classique.
1. **Croiser** avec autres souches du malware : la même famille ransomware utilise-t-elle les mêmes patterns ?

### 13.8 Adresse sur forum dark web

**Cas typique** : enquête sur un acteur dark web qui partage son adresse pour réception de paiements (vente de données, services).

**Étapes** :

1. **Documenter le contexte** : forum, post, date, vendeur, contenu vendu/proposé.
1. Extraire l’adresse.
1. Suivre méthodologie standard.
1. **Croiser** avec activités du vendeur (autres forums, autres pseudonymes).

Cf. cours **Dark Web** pour la méthodologie d’enquête sur les forums clandestins.

### 13.9 Adresse dans note de ransomware

Voir Ch.13.5.

### 13.10 Indice indirect : nom d’un acteur, alias, organisation

**Cas typique** : on demande à Sarah « investigue Lazarus » sans adresse de départ.

**Étapes** :

1. **Recherche dans bases publiques d’adresses associées**. OFAC SDN list (qui inclut désormais des adresses crypto). Reports Chainalysis, TRM, Elliptic publiquement disponibles.
1. **Recherche sur Twitter / X** : ZachXBT et autres chercheurs publient régulièrement des adresses associées à des hacks/acteurs.
1. **Recherche dans IndexedLeaks et bases CTI** : des wallets connus sont publiés.
1. **Avec point de départ obtenu**, suivre méthodologie standard.

Cas Lazarus : OFAC a sanctionné de multiples wallets liés. Plusieurs hacks majeurs (Ronin, Atomic Wallet, multiple exchanges) ont des adresses publiques documentées par Chainalysis et FBI.

### 13.11 Priorisation des indices

Quand l’analyste a **plusieurs indices** au démarrage (ce qui est commun dans les gros incidents), il priorise.

**Critères** :

**Solidité**. Un TXID est plus solide qu’une capture d’écran (qui peut être falsifiée). Une adresse confirmée par on-chain analysis est plus solide qu’une mention forum.

**Fraîcheur**. Une adresse active dernière 24h offre plus d’angles (suivre les flux en temps réel) qu’une adresse inactive depuis 2 ans.

**Centralité**. L’adresse principale d’un acteur (hot wallet ransomware) est plus critique qu’une adresse périphérique.

**Coopérabilité**. Une adresse qui transite vers un exchange régulé permet potentiellement réquisition. Une adresse 100% interne au réseau criminel sans interaction externe est plus opaque.

**Effort vs valeur**. Investir 20h sur une adresse Monero qui ne donnera rien vs 5h sur une adresse Bitcoin avec angles multiples → choix évident.

### 13.12 Fil rouge — MIXSHADOW : priorisation des branches

> **🔗 MIXSHADOW — Épisode 9 : choix d’angles**
> 
> Au bout de 3 semaines, Sarah a identifié 62 adresses Bitcoin, 18 Ethereum, 47 TRON. Trop pour tout suivre en profondeur. Elle priorise.
> 
> **Branche prioritaire 1** : peeling chain principale Bitcoin. 27,5 BTC restent en circulation, mouvement continu. Suivi quotidien justifié.
> 
> **Branche prioritaire 2** : flux USDT-TRON. 290 000 USDT en dispersion. Plusieurs hubs identifiés. Coordination Tether possible.
> 
> **Branche secondaire 3** : Tornado Cash Ethereum. Les 12 ETH sont déposés. Analyse statistique des sorties à mener mais probabiliste — moins de certitude sur attribution mais utile pour profiler Akira.
> 
> **Branche tertiaire 4** : adresses externes du peeling chain non encore caractérisées. Chacune représente un dépôt de quelques BTC dans un service ou wallet. Plusieurs sont déjà identifiées comme exchanges non-KYC. Quelques-unes sont des inconnues à investiguer.
> 
> Sarah alloue son temps : 60% sur prioritaires 1+2, 20% sur Tornado, 20% sur les autres branches.
> 
> Elle demande aussi à un junior d’Athéna de prendre en charge la **fiche d’écosystème** Akira (ce qui n’est pas dans le périmètre crypto strict mais alimente l’attribution) : profil du groupe, historique des victimes connues, TTP, leak site Akira, infrastructure.

-----

## Chapitre 14 — De l’indice au graphe : chaîne de raisonnement

Une fois l’indice initial exploité, l’enquête entre dans sa **phase exploratoire**. Construire le graphe de l’écosystème de l’acteur. Ce chapitre couvre la chaîne de raisonnement de l’analyste pour passer méthodiquement de l’indice au graphe documenté.

### 14.1 La distinction critique : observation, inférence, attribution

Trois niveaux à ne jamais confondre.

**Observation** : ce qu’on **voit** directement sur la blockchain. « L’adresse A a envoyé 10 BTC à l’adresse B le [date] ». Vérifiable, factuel.

**Inférence** : ce qu’on **déduit** des observations via raisonnement et heuristiques. « L’adresse B est probablement contrôlée par la même entité que A (heuristique de change) ». Probabiliste, justifiable.

**Attribution** : ce qu’on **affirme** sur l’identité ou la nature de l’entité. « Le cluster A-B est un wallet du groupe ransomware Akira ». Nécessite des **éléments externes** (recoupements OSINT, labels propriétaires, données KYC obtenues légalement).

**L’analyste sérieux** :

- Distingue ces niveaux dans son journal et ses rapports.
- Ne **promeut** pas une inférence en attribution sans preuve additionnelle.
- Calibre la confiance à chaque niveau.

### 14.2 La chaîne de raisonnement type

**Étape 1 — Identifier l’actif et la chaîne** (observation immédiate).

L’indice est sur quelle blockchain ? Quel actif ? Vérifications de base avant tout autre travail.

**Étape 2 — Vérifier l’existence de la transaction / activité de l’adresse** (observation).

L’indice n’est pas une fabrication. La transaction existe bien, l’adresse a bien l’historique attendu.

**Étape 3 — Lire la transaction / activité initiale en détail** (observation).

Toutes les composantes (inputs, outputs, value, logs, internal). Pas de raccourci.

**Étape 4 — Identifier les contreparties** (observation).

Qui sont les autres adresses dans la transaction. Lister sans interpréter encore.

**Étape 5 — Catégoriser les contreparties** (inférence).

Pour chaque contrepartie : est-ce un service connu (label) ? Une nouvelle adresse fraîche ? Une adresse à activité passée ? Catégorie initiale : exchange / mixer / bridge / wallet personnel inconnu / etc.

**Étape 6 — Suivre les flux pertinents** (observation + inférence).

Pour chaque contrepartie pertinente, lire ses transactions sortantes. Reconstituer le **chemin des fonds** post-réception.

**Étape 7 — Identifier les patterns** (inférence).

Peeling chain ? Consolidation ? Split ? Dépôt exchange ? Bridge ? Mixer ? Caractériser le type d’opération.

**Étape 8 — Formuler hypothèses** (inférence calibrée).

À partir des patterns, proposer des hypothèses sur la nature de l’activité (« blanchiment post-rançon », « collecte de victimes », « préparation cashout »).

**Étape 9 — Croiser avec sources externes** (recoupement).

Recherche OSINT sur les adresses, labels propriétaires, mentions publiques, base CTI Athéna interne.

**Étape 10 — Mettre à jour les fiches et le graphe** (documentation).

Synthétiser dans les fiches d’adresses + graphe global.

**Étape 11 — Itérer** (cycle).

Chaque nouvelle adresse identifiée comme pertinente devient indice de Étape 1. Le graphe s’étend.

### 14.3 Le piège de l’expansion sans bornes

**Erreur classique** : suivre **toutes** les adresses, à toutes les profondeurs. Le graphe explose. Au bout de 5 hops, on a des dizaines de milliers d’adresses, dont 99% sans rapport avec l’enquête initiale.

**Stratégie de bornage** :

**Profondeur limitée**. Ne pas dépasser 5-7 hops typiquement, sauf cas spécifique. Au-delà, le signal se perd dans le bruit.

**Filtrage par pertinence**. Ne suivre les adresses dont les flux sont significatifs (gros montants, patterns suspects). Ignorer les flux poussiéreux (dust).

**Stop conditions**. Arrêter sur :

- Dépôt exchange identifié → angle de coopération autorité, suivi terminé pour cette branche.
- Mixer / privacy coin → rupture de visibilité, documenter et passer.
- Adresse dormante (pas de mouvement depuis longtemps) → pas de progrès attendu.
- Cluster déjà attribué → information acquise.

**Priorisation continue**. Réévaluer hebdomadairement quelles branches méritent encore l’effort.

### 14.4 Distinguer un service d’un wallet utilisateur

Erreur fréquente : confondre une adresse de **service** (exchange, processeur de paiement, mixer) avec une adresse de **wallet utilisateur**.

**Signaux qu’une adresse est un service** :

**Volume très élevé**. Service principal d’exchange peut traiter des milliers de transactions par jour. Wallet utilisateur typique a quelques transactions par mois.

**Multi-counterparties**. Service interagit avec des centaines/milliers d’adresses différentes. Wallet utilisateur a un nombre limité de contreparties.

**Patterns automatisés**. Service consolide/dispatche selon patterns programmés (chaque 6h, chaque seuil atteint, etc.). Wallet utilisateur a des patterns plus erratiques.

**Solde stable ou cyclique**. Service maintient solde dans une fourchette opérationnelle. Wallet utilisateur peut avoir solde très variable.

**Labellisation**. Service souvent labellisé par les outils. Wallet rarement.

**Erreur si confusion** : analyser un service comme s’il était un acteur permet de l’attribuer à tort à l’acteur enquêté. Toutes les transactions d’un exchange ne sont pas des transactions de l’enquêteur — c’est l’**utilisateur final** dans le service qui compte.

### 14.5 Le raisonnement face à l’incertitude

Beaucoup d’observations sont **ambiguës**. L’analyste doit calibrer.

**Exemple typique** : adresse A envoie à adresse B 0,5 BTC. Adresse B est nouvelle, jamais vue.

Hypothèses possibles :

- B est une adresse de change de A (continuation interne).
- B est un wallet personnel de la même entité, géré séparément.
- B est un destinataire externe (paiement à un autre acteur).
- B est un dépôt exchange (bientôt vidé vers hot wallet de l’exchange).

Sans information additionnelle, **on ne peut pas trancher**. On documente toutes les hypothèses, on attend l’évolution (B fait quoi ensuite ?), on enrichit avec labels.

**Discipline** : ne pas trancher prématurément. Garder les hypothèses ouvertes. Ne refermer que quand des éléments solides arrivent.

### 14.6 Calibration WEP en pratique

L’analyste utilise un vocabulaire calibré (Words of Estimative Probability).

**Échelle type** (voir Annexe F pour matrice complète) :

|WEP              |Probabilité|Usage                                                               |
|-----------------|-----------|--------------------------------------------------------------------|
|Quasi-certain    |>95%       |Preuve directe, multiple corroboration. Rare dans l’OSINT pur.      |
|Très probable    |80-95%     |Multiple convergence, peu d’alternatives plausibles                 |
|Probable         |60-80%     |Convergence majoritaire, alternatives possibles mais moins probables|
|Possible         |40-60%     |Hypothèse parmi d’autres, pas dominante                             |
|Peu probable     |15-40%     |Possible mais des alternatives plus plausibles                      |
|Très peu probable|<15%       |Hypothèse marginale                                                 |
|Indéterminable   |N/A        |Données insuffisantes pour évaluer                                  |

**Bonne pratique** : utiliser **systématiquement** un WEP à chaque hypothèse formulée. Et expliciter ce qui pourrait faire évoluer le WEP (« si on apprend X, le WEP passerait à Y »).

### 14.7 Le journal d’enquête

Le **journal d’enquête** est la trace écrite quotidienne de la chaîne de raisonnement.

**Format type (Markdown)** :

```markdown
# Journal MIXSHADOW

## 2026-03-19

### 14:23 UTC — Suivi adresse Akira-BTC-007
- Observation : adresse a fait nouvelle transaction sortante.
- TXID : [hash]
- Lecture : peeling pattern continue, 0,4 BTC à external + 32,7 BTC à change.
- External destination : adresse fraîche, jamais vue.
- Action : créer fiche Akira-BTC-008 (external) et Akira-BTC-Change-008 (change).

### 14:45 UTC — Hypothèse sur Akira-BTC-008
- Pas encore d'activité sortante.
- Hypothèse : possible dépôt exchange (probable, 60%).
- Alternative : wallet personnel intermédiaire (possible, 30%).
- Alternative : OTC desk (possible, 20%).
- Surveillance : alerte Chainalysis activée pour mouvements futurs.

### 16:12 UTC — Réflexion sur progression globale
- 5 branches actives en parallèle.
- Branche peeling principale : 18 hops, 7,5 BTC dispersés, 27,5 BTC en circulation.
- Branche Ethereum/Tornado : 12 ETH déposés, sorties non analysées encore.
- Branche TRON/USDT : 290k USDT en dispersion.
- Décision : prioriser TRON + Bitcoin pour cette semaine. Tornado attend.
```

Ce journal **n’est pas le rapport final**. C’est la matière brute qui alimentera le rapport, mais aussi la **trace** pour reproduire/contester l’analyse plus tard.

-----

## Chapitre 15 — Construire un graphe de flux lisible

Le **graphe de flux** est la représentation visuelle de l’enquête. Bien construit, il rend l’enquête lisible en une page. Mal construit, il devient un **plat de spaghetti** illisible. Ce chapitre couvre la méthodologie de visualisation.

### 15.1 Pourquoi visualiser

**Comprendre soi-même**. La représentation visuelle révèle des patterns invisibles dans le tableau. Un peeling chain devient évident en graphe, opaque en liste.

**Communiquer**. Un rapport avec graphe est lu et compris ; un rapport texte-only est plus difficile à digérer pour décideurs.

**Coopérer**. Quand Sarah brieffe la DGSI, un graphe permet à l’auditoire d’absorber la topologie en quelques minutes.

**Soutenir la mémoire**. Une fois l’enquête archivée, le graphe permet de reconstituer rapidement l’analyse 6 mois plus tard.

### 15.2 Anatomie d’un graphe de flux

**Nœuds** : adresses crypto.

**Arêtes** : transactions (montant, direction, timestamp, actif).

**Attributs des nœuds** :

- Type d’entité présumée (wallet utilisateur / service / contrat / mixer / etc.).
- Solde actuel.
- Volume cumulé (entrées + sorties).
- Niveau de confiance d’attribution.

**Attributs des arêtes** :

- Direction (qui envoie à qui).
- Montant.
- Actif (BTC, ETH, USDT, etc.).
- Timestamp.
- TXID référence.

**Annotations contextuelles** :

- Légende (couleurs, formes).
- Période couverte.
- Source des données.

### 15.3 Codes visuels recommandés

**Couleur par type d’entité** :

- **Vert** : adresse cible / contrôlée par enquêté (acteur principal de l’enquête).
- **Rouge** : adresse à risque (sanctioned, mixer, etc.).
- **Bleu** : exchange / VASP régulé.
- **Orange** : exchange non-KYC ou à risque.
- **Gris** : adresse non encore caractérisée.
- **Jaune** : smart contract / DeFi.

**Forme par fonction** :

- **Cercle** : wallet (EOA Ethereum, adresse Bitcoin classique).
- **Carré** : smart contract.
- **Hexagone** : service (exchange, bridge).
- **Triangle** : adresse sanctionnée.

**Épaisseur d’arête** : proportionnelle au montant (logarithmique pour grosse plage de valeurs).

**Style d’arête** :

- Plein : transaction confirmée.
- Pointillé : flux inféré (pas observable directement, ex : sortie de mixer présumée).

### 15.4 Niveaux d’abstraction

Un même graphe peut être visualisé à différents niveaux.

**Niveau 1 — Adresses brutes**. Chaque adresse = un nœud. Trop dense pour une enquête à 100+ adresses. Utile pour analyse fine d’une zone.

**Niveau 2 — Clusters**. Les adresses du même cluster (heuristiques) sont fusionnées en un seul nœud. Donne le « squelette » de l’écosystème. Vue plus lisible pour acteurs majeurs.

**Niveau 3 — Entités**. Les adresses identifiées comme un même service (exchange, mixer) sont fusionnées en une entité. Donne la vue **business** : « Akira → exchange non-KYC X → Tornado Cash → exchange régulé Y ».

**Niveau 4 — Phases**. Synthèse en phases d’opération : « Réception → Layering → Cashout ». Vue ultime pour rapport exécutif.

L’analyste produit **plusieurs vues** selon l’audience :

- SOC / IR : niveau 1 et 2 (détail technique).
- CISO / direction : niveau 3 et 4 (stratégique).
- Autorités : niveau 2 et 3 (opérationnel).

### 15.5 Outils de visualisation

**Chainalysis Reactor** : visualisation native intégrée à l’outil de clustering. Excellente pour enquêtes utilisant Chainalysis. Limites : exports parfois rigides, dépendance plateforme.

**TRM Labs Investigations** : équivalent. Bon graphique intégré.

**Maltego** : référence transverse OSINT. Connecteurs blockchain via plugins (Maltego CTAS, Maltego Crypto). Très flexible, courbe d’apprentissage modérée. Excellent pour graphes multi-sources (crypto + OSINT classique + autres).

**Gephi** : open source, puissant pour grands graphes. Plus orienté analyse statistique réseau (centralité, communautés). Courbe d’apprentissage forte.

**Graphistry** : visualisation GPU pour très grands graphes (>100k nœuds). Cloud ou self-hosted. Cas avancés.

**Obsidian** : pour graphes simples avec annotations textuelles. Léger, rapide. Limité en taille.

**Mermaid (Markdown)** : pour graphes simples intégrables dans rapports Markdown. Limites visuelles fortes mais portable.

**Drawio / Excalidraw** : pour graphes manuels simples. Bons pour documents finaux. Peu adapté pour gros graphes.

**Cytoscape** : alternative à Gephi, JavaScript-based, customisable.

### 15.6 Quand ne PAS visualiser

**Trop peu de données**. Si l’enquête a 5 adresses et 3 transactions, un tableau suffit. Visualisation overkill.

**Trop de données sans abstraction**. 10 000 adresses sans cluster = spaghetti. Soit on abstractit (clusters, entités), soit on segmente (zoom sur une partie).

**Pour le draft d’analyse**. La visualisation soigneusement formattée prend du temps. Ne la produire qu’aux livraisons importantes (rapport intermédiaire, rapport final, briefing). En cours d’enquête, journal Markdown + tableau excel suffit.

### 15.7 Le graphe minimal pour rapport

Pour rapport exécutif (audience non-technique), un **graphe minimal** :

- 5-15 nœuds maximum.
- Niveau 3 (entités) ou Niveau 4 (phases).
- Couleurs claires, légende explicite.
- Annotations textuelles pour les éléments clés (« Étape 3 : conversion BTC → USDT-TRON via exchange non-KYC X »).
- Pas plus de 10-15 arêtes.

Si l’enquête a 100+ adresses, le rapport contient le **graphe minimal** dans le corps, et le **graphe détaillé** en annexe technique.

### 15.8 Fil rouge — MIXSHADOW : graphe à 4 semaines

> **🔗 MIXSHADOW — Épisode 10 : visualisation d’étape**
> 
> Sarah prépare un graphe pour le briefing intermédiaire DGSI à 4 semaines de mission. Il doit synthétiser ce qu’elle a compris jusque-là.
> 
> **Niveau 3 (entités)**, 12 nœuds principaux :
> 
> - Aurélien Médical (vert).
> - Akira receive address (rouge, central).
> - Akira BTC operational wallet (rouge, peeling chain principale).
> - FixedFloat (orange, exchange non-KYC).
> - Akira ETH wallet (rouge).
> - Tornado Cash 10 ETH pool (gris, mixer).
> - Tornado Cash 1 ETH pool (gris, mixer).
> - Exchange non-KYC X (orange).
> - Akira TRON wallet 1 (rouge).
> - Hub TRON 1 (orange, suspect service de blanchiment).
> - Hub TRON 2 (orange, suspect service de blanchiment).
> - Multiple destinations TRON (gris, à investiguer).
> 
> Arêtes annotées avec montants et timing.
> 
> Légende explicite. Phase indiquées sur le graphe : (1) réception, (2) peeling Bitcoin, (3) conversion ETH/Tornado, (4) conversion TRON/dispersion.
> 
> Le graphe tient sur une page. Le briefing à la DGSI utilise ce graphe + 5 slides additionnelles (contexte, observations clés, hypothèses, limites, prochaines étapes). Durée totale : 30 minutes + 30 min Q&A.
> 
> Retour DGSI : le graphe permet une lecture immédiate. Validation pour pousser la coordination Tether sur les adresses TRON principales. Validation aussi pour transmettre les 4 adresses des principaux exchanges non-KYC à Europol/FBI pour évaluation de coopération internationale.
> 
> Sarah note : sans ce graphe, l’enquête « 4 semaines, 130 adresses » serait incommunicable.

-----

## Chapitre 16 — Temporalité et chronologie d’enquête

La dimension **temporelle** est centrale en enquête crypto. Les transactions sont horodatées avec précision, et leur **séquence** porte de l’information. Mal traiter la temporalité = manquer des patterns clés.

### 16.1 Les timestamps blockchain

Toute transaction blockchain a un **timestamp précis**, en **UTC**. Précision :

- Bitcoin : timestamp du bloc, ~10 minutes de granularité.
- Ethereum : timestamp du bloc, ~12 secondes de granularité (post-Merge).
- TRON, Solana : seconde près.

**Important** : le timestamp est celui d’**inclusion dans un bloc**, pas de **broadcast**. Une transaction émise à 14:23:00 peut être incluse dans un bloc à 14:25:30. Pour les analyses fines, cette différence importe.

**Mempool** : sur Bitcoin notamment, les transactions « attendent » dans le mempool avant inclusion. Si congestion, elles peuvent attendre plusieurs heures. L’analyste sophistiqué regarde aussi les **logs mempool** (si disponibles) pour saisir le moment exact d’émission.

### 16.2 Patterns temporels remarquables

**Activité par fuseau horaire**. Les acteurs actifs uniquement entre 9h et 18h dans une fenêtre cohérente avec un fuseau (Moscou, Pyongyang, etc.) trahissent leur localisation probable. Adresses gérées par humains ont des patterns horaires ; bots ont des patterns non-humains.

**Jours fériés / chômés**. Inactivité pendant jours fériés russes (1-8 janvier, 8 mars, 1-9 mai), chinois (Nouvel An lunaire), iraniens (Nowruz), nord-coréens (Chuseok, Day of the Foundation), etc. — signal sur la juridiction d’opération.

**Cohérence horaire avec autres événements**. Un paiement crypto à H+0 d’une demande de rançon, un transfert post-hack à H+5 minutes, un dépôt exchange juste après hop d’obfuscation = patterns cohérents avec acteur unique pilotant l’opération.

**Bursts d’activité**. Soudaine multiplication de transactions sur 1-2h = signal de **dispersion en urgence** (peur d’alerte) ou **automatisation** (bot consolidant).

**Inactivité longue avec activité subite**. Wallet dormant pendant des mois qui se réveille = signal fort. Soit l’attaquant change de tactique, soit un nouveau cycle d’opération démarre.

### 16.3 Délais entre événements

**Délai paiement-rançon → premier mouvement**. Mesure le **temps de réaction** de l’opérateur. Quelques minutes = automatisation. Quelques heures = supervision humaine. Plusieurs jours = peut-être pas le vrai propriétaire (revente, intermédiaire).

**Délai dépôt exchange → retrait en autre actif**. Mesure le **temps de blanchiment**. Conversion BTC → USDT en 5 minutes = pattern automatisé. En 24h = manuel.

**Délai entre branches d’un peeling chain**. Trop régulier (toutes les heures pile) = bot. Variable et erratique = humain.

### 16.4 Construire une timeline d’enquête

Pour rapports, une **timeline** synthétise les événements clés en ordre chronologique.

**Format type** (Annexe D pour template) :

```markdown
## Timeline MIXSHADOW

| Date UTC | Événement | Adresse | Montant | Source |
|---|---|---|---|---|
| 2026-03-08 03:47 | Compromission initiale Aurélien Médical | - | - | Forensics Mandiant |
| 2026-03-08 04:30 | Démarrage chiffrement Akira | - | - | Logs internes |
| 2026-03-12 11:00 | Demande rançon initiale 80 BTC | bc1q[Akira-receive] | 80 BTC | Note ransomware |
| 2026-03-13 16:30 | Négociation : 35 BTC accepté | - | - | Comm. cellule crise |
| 2026-03-14 09:12 | Paiement Aurélien Médical | bc1q[Akira-receive] | 35 BTC | Mempool TXID [...] |
| 2026-03-14 15:28 | Réception clé déchiffrement | - | - | Comm. portail Akira |
| 2026-03-17 03:42 | Premier mouvement sortant Akira | bc1q[H1] | 35 BTC | Mempool TXID [...] |
| 2026-03-17 04:18 | Début peeling chain | bc1q[H2] | 0,5 + 34,5 BTC | Mempool TXID [...] |
| ... | ... | ... | ... | ... |
| 2026-03-19 11:43 | Conversion BTC → ETH via FixedFloat | 0xFixedFloat → 0xAk1 | 12,5 ETH | Etherscan TXID [...] |
| 2026-03-19 12:55 | Dépôts Tornado Cash (3 dépôts) | 0xAk1 → Tornado | 12 ETH | Etherscan TXIDs [...] |
| 2026-03-22 08:30 | Conversion via exchange non-KYC X | bc1q[H12] → exchange | 3 BTC | Mempool + monitoring |
| 2026-03-22 12:30 | Retrait USDT-TRON | exchange → TR[Akira-TRON] | 290 000 USDT | Tronscan TXID [...] |
| ... | ... | ... | ... | ... |
```

La timeline est **synthétique** (pas exhaustive — elle synthétise le journal complet). Elle est **enrichie de sources** (TXID, références internes). Elle est **chronologique stricte**.

### 16.5 Corrélation avec événements off-chain

L’enquête crypto **gagne** quand on corrèle avec des événements off-chain.

**Avec logs internes victime**. Le timestamp d’une transaction crypto peut être corrélé avec :

- Logs SIEM (compromission initiale, activité suspecte).
- Logs réseau (exfiltration de données précédant le ransomware).
- Logs téléphone/email du RSSI (notifications, négociations).

**Avec comms négociation**. Les portails de négociation Tor utilisés par les opérateurs ransomware ont leurs propres timelines (messages, deadlines, ultimatums). Croiser avec timeline crypto.

**Avec leak site**. La publication sur le leak site Akira d’Aurélien Médical (s’il y en a eu) a un timing à corréler. Avant paiement, après paiement, etc.

**Avec presse / médias**. Les annonces publiques de rançonnage / paiement / récupération forment une trame externe.

**Avec d’autres victimes**. Si Akira a frappé 5 victimes la même semaine, leurs timelines comparées peuvent révéler **patterns opérationnels** du groupe (séquencement d’attaques, ressource humaine consacrée, etc.).

### 16.6 Fuseaux horaires : la rigueur

**Toujours en UTC dans les rapports techniques**. Évite ambiguïté. Les blockchains sont en UTC.

**Conversion explicite si nécessaire**. « 09:12 UTC, soit 10:12 heure de Paris (UTC+1, hiver) ». Évite confusion lecteur.

**Ne jamais faire de raisonnement sans timezone**. « La transaction a eu lieu à 9h12 » est insuffisant. **9h12 où ?**

**Cohérence dans tout le rapport**. Si le rapport mélange UTC pour blockchain et heure locale pour comms, expliciter au début et marquer chaque mention.

### 16.7 Fil rouge — MIXSHADOW : insight temporel

> **🔗 MIXSHADOW — Épisode 11 : pattern horaire Akira**
> 
> Sarah analyse les **patterns temporels** des opérations Akira observées dans MIXSHADOW.
> 
> **Activité par heure UTC** (sur les 30+ transactions Akira analysées) :
> 
> - 0h-4h UTC : 35% de l’activité.
> - 4h-8h UTC : 8%.
> - 8h-12h UTC : 12%.
> - 12h-16h UTC : 5%.
> - 16h-20h UTC : 15%.
> - 20h-24h UTC : 25%.
> 
> **Décodage** : pic d’activité en deux fenêtres : 0h-4h UTC et 20h-24h UTC. Si on convertit :
> 
> - 0h-4h UTC = 3h-7h MSK (Moscou), ou 9h-13h KST (Séoul/Pyongyang).
> - 20h-24h UTC = 23h-3h MSK, ou 5h-9h KST.
> 
> Le pattern est **plus cohérent avec un fuseau Asie de l’Est** (KST, Pyongyang ou Séoul) qu’avec MSK. Heure de travail KST = pic d’activité crypto.
> 
> Mais Sarah reste prudente : c’est un **signal**, pas une preuve. Hypothèses alternatives :
> 
> - Acteur en Russie qui travaille de nuit (par choix ou contrainte).
> - Acteur dans une autre TZ qui imite délibérément patterns asiatiques.
> - Plusieurs membres dans des TZ différentes coordonnant.
> 
> WEP : « possible profil opérateur en fuseau Asie de l’Est (40%), profil russophone toujours plausible (30%), autre / mixte (30%) ».
> 
> Cette observation est **incertaine** mais alimente l’attribution. Elle est combinée avec d’autres signaux (langue dans portail négociation, infrastructure technique, patterns d’attaques précédentes) pour profiler Akira. Akira pourrait avoir des liens DPRK (cf Lazarus, Ch.29), ce qui collerait avec KST. Mais aussi des liens russophones documentés. Le profil pourrait être **hybride** (opérateurs DPRK + affiliés russophones, modèle observé chez d’autres groupes).
> 
> Sarah note dans le rapport : « les patterns horaires sont cohérents avec une activité d’opérateur en fuseau UTC+9 (KST), mais cette observation est insuffisamment robuste pour conclure sur localisation géographique ». Calibration honnête.

-----

## Chapitre 17 — Clustering : heuristiques, promesses et limites

Le **clustering** — regroupement d’adresses appartenant probablement à la même entité — est l’une des techniques fondamentales de l’enquête crypto. Mais c’est aussi un domaine où les illusions sont nombreuses. Ce chapitre détaille promesses et limites.

### 17.1 Le concept

**Clustering** : à partir des observations on-chain, on regroupe les adresses qui semblent contrôlées par la **même entité** (un même utilisateur, un même service, une même organisation).

**Pourquoi clusters** :

- Une entité utilise typiquement **multiples adresses** (rotation, séparation par usage, hot/cold).
- Reconstituer le **portefeuille complet** d’une entité permet une vue économique réaliste.
- Identifier l’entité (si possible) sur **n’importe quelle adresse du cluster** étend l’attribution à tout le cluster.

**Comment** : par application d’**heuristiques** sur les transactions observées.

### 17.2 Les heuristiques principales

**1. Heuristique du co-spend (multi-input)**. Sur Bitcoin, plusieurs inputs co-dépensés dans une transaction sont contrôlés par la même entité (qui possède les clés privées de tous). Forte mais cassée par CoinJoin.

**2. Heuristique du change**. Sur Bitcoin, l’output « change » d’une transaction est contrôlé par l’entité qui a émis. Diverses sous-heuristiques pour identifier le change (Ch.6).

**3. Heuristique du timing**. Adresses actives dans des fenêtres temporelles très proches sont possiblement liées.

**4. Heuristique du wallet**. Certains wallets (Electrum, Bitcoin Core, etc.) génèrent les adresses selon des patterns reconnaissables. Reconnaissance du wallet utilisé est un signal.

**5. Heuristique de l’address reuse**. Une adresse qui reçoit un dépôt unique puis envoie immédiatement vers une nouvelle adresse jamais vue suit un pattern HD wallet (transit).

**6. Heuristique des patterns de service**. Exchange consolide selon patterns reconnaissables (cadence, seuils). L’analyste expérimenté identifie les patterns d’exchange spécifiques.

**7. Heuristique des labels propriétaires**. Les outils Chainalysis/TRM/Elliptic ont des **bases label** internes (acquises par : recherche, KYC achetés, leaks, partenariats avec exchanges). Une adresse labellisée est un point d’attribution dans un cluster.

### 17.3 Le clustering Ethereum : différent

Ethereum n’a **pas** d’heuristique du co-spend (transactions à un seul émetteur). Le clustering Ethereum repose sur :

**Patterns d’activité**. Adresses contrôlées par une même entité se comportent souvent de manière cohérente (interactions avec mêmes smart contracts, paiements gas par même source, etc.).

**Funding source**. Si une adresse est créée et immédiatement financée par une autre adresse, c’est un signal de contrôle commun.

**Smart contract ownership**. Une adresse qui a déployé un smart contract est probablement liée aux adresses qui interagissent avec ce contrat de manière privilégiée.

**Cross-chain activity**. Une adresse Ethereum qui bridge des fonds vers TRON, et l’adresse TRON destinataire qui a un pattern d’activité similaire, suggère même entité.

**Limites** : clustering Ethereum est **moins robuste** que Bitcoin co-spend. Les outils s’appuient massivement sur **labels propriétaires** et heuristiques mixtes.

### 17.4 Promesses du clustering

**Quand le clustering fonctionne bien** :

**Wallets utilisateurs simples**. Un utilisateur basique avec wallet Bitcoin Core génère plusieurs adresses, fait des transactions classiques. Heuristique du co-spend reconstitue le wallet en cluster. Précision élevée.

**Services / exchanges**. Les services consolident des fonds utilisateurs vers hot wallets. Le co-spend massif et patterns reconnaissables identifient le service. Cluster Coinbase = des centaines de milliers d’adresses, identifié avec précision élevée.

**Acteurs criminels naïfs**. Les acteurs qui n’ont pas pris de précautions OPSEC (réutilisation d’adresses, co-spend entre wallets « privés » et wallets « publics ») sont rapidement identifiés.

**Ransomware classique**. Les opérateurs ransomware qui collectent des dizaines de paiements vers un même wallet opérationnel forment un cluster identifiable.

### 17.5 Limites du clustering

**Quand le clustering échoue ou induit en erreur** :

**CoinJoin**. Wasabi et Samourai cassent l’heuristique du co-spend. Inputs co-dépensés ne sont **pas** d’une même entité. Un cluster constitué via co-spending sur des transactions CoinJoin est **faux**. Les outils modernes détectent les CoinJoin et excluent ces transactions du clustering — vérifier que c’est le cas.

**Wallets modernes anti-tracking**. Wallets qui randomisent volontairement la structure des transactions (montants non-ronds aléatoires, position du change, etc.) limitent l’efficacité des heuristiques.

**Multi-sig**. Adresses multisig sont contrôlées par plusieurs parties (M-of-N). Pas une seule entité. Heuristiques qui supposent contrôle unique se trompent.

**Smart contracts (Ethereum)**. Adresses contrôlées par smart contracts (exchanges décentralisés, pools de liquidité, comptes contrats) ont des patterns propres qui ne se prêtent pas au clustering classique.

**Adresses partagées implicites**. Certains wallets « shared » ou exchanges qui n’utilisent qu’un seul wallet pour multiples utilisateurs créent des « clusters » qui sont en fait des **agrégations**, pas des entités uniques.

**Erreurs en cascade**. Si une heuristique commet une erreur en début de chaîne, tout le cluster qui en découle est faux. Outils intègrent scores de confiance pour limiter, mais erreurs existent.

**Adversarial design**. Acteurs qui connaissent les heuristiques peuvent **délibérément** créer des transactions trompeuses pour brouiller (faux co-spending, fausses peeling chains).

### 17.6 Vocabulaire et calibration

**Cluster** : ensemble d’adresses regroupées comme appartenant probablement à la même entité.

**Niveau de confiance d’un cluster** :

- **Très fiable** : multiple heuristiques convergentes, peu de risques d’erreur (cluster d’exchange majeur, par exemple).
- **Fiable** : heuristique principale solide, validation par patterns secondaires.
- **Probable** : heuristique principale plausible, mais alternatives existent.
- **Spéculatif** : pattern observé mais sans fort support, à vérifier.

**Affirmer « le cluster X »** sans calibration de confiance est une erreur. Toujours expliciter.

**Vocabulaire à utiliser** :

- « Le cluster comprend X adresses, attribué par Chainalysis avec confiance « high » à l’entité Y ».
- « Le cluster reconstruit par heuristiques de co-spend regroupe N adresses ; cette construction est probable (~80%) sauf erreur de heuristique non détectée ».
- « L’entité présumée derrière le cluster est probablement [exchange/individu/groupe] (confiance Y%) ».

### 17.7 Validation croisée

**Multi-outils**. Si Chainalysis et TRM Labs concluent au même cluster, confiance plus élevée que si un seul outil. Validation indépendante.

**Cohérence comportementale**. Le cluster a-t-il un comportement **cohérent** dans le temps ? Patterns d’activité stables ? Si le cluster évolue brusquement (devient hyperactif, change de patterns), il peut s’agir d’un **changement de contrôle** (vente, hack, changement opérationnel).

**Recoupement OSINT**. Si le cluster correspond à une entité publiquement attribuée (annonce officielle, label vendor, mention OSINT), validation externe.

### 17.8 Le clustering n’est pas une preuve d’identité

**Message clé à intérioriser** :

> Le clustering ne prouve pas une identité. Il propose un regroupement probable d’adresses contrôlées par une même entité ou un même service, selon des heuristiques discutables.

Une entité du cluster peut être :

- Un wallet utilisateur unique.
- Un service (exchange, mixer).
- Un agrégat artificiel (erreur de heuristique).

L’**identité civile** derrière n’est pas dans le cluster. Elle nécessite des éléments **off-chain** (KYC exchange, mention publique, recoupement OSINT).

Le cluster est un outil pour **structurer la vue**, pas pour conclure. L’analyste avisé manipule les clusters comme des hypothèses calibrées, pas comme des vérités.

-----

## Chapitre 18 — Attribution : adresse → service → personne

L’**attribution** est l’opération qui consiste à associer une adresse, un cluster, ou un flux à une **entité identifiée**. Plusieurs niveaux existent. Ce chapitre les distingue et calibre les niveaux de preuve.

### 18.1 Les trois niveaux d’attribution

**Niveau 1 — Attribution à un service**. « Cette adresse est un dépôt Binance. » L’entité attribuée est un **service** (exchange, custodian, marchand). Le service connaît l’identité civile de l’utilisateur (via KYC), mais l’analyste OSINT ne la connaît pas — elle nécessite réquisition.

**Niveau 2 — Attribution à un acteur connu**. « Cette adresse est contrôlée par Lazarus / Akira / AlphaBay. » L’entité attribuée est un **acteur identifié** (groupe, individu connu, organisation). L’attribution s’appuie sur preuves publiques (annonces vendor, labels OFAC, recoupements OSINT).

**Niveau 3 — Attribution à une personne nommée**. « Cette adresse est contrôlée par [Nom de personne réelle]. » L’entité attribuée est un **individu civil identifié**. Très rare en OSINT pur, généralement issue de procédures judiciaires (saisies, inculpations).

L’analyste opère principalement aux niveaux 1 et 2. Niveau 3 relève des autorités.

### 18.2 Distinguer adresse, wallet, service, personne

**Adresse** : identifiant cryptographique. Singulier.

**Wallet** : ensemble d’adresses contrôlées par une même clé privée racine (HD wallet) ou une même infrastructure (multi-sig, custody). Peut contenir des centaines ou milliers d’adresses.

**Service** : entité qui opère un wallet (ou des wallets) pour servir des clients. Exchange, custodian, processeur de paiement, mixer. Le service contrôle les clés ; les utilisateurs ont des **comptes** chez le service mais pas les clés.

**Personne** : individu civil. Peut être :

- Utilisateur direct d’un wallet (non-custodial).
- Utilisateur d’un service (custodial).
- Salarié / dirigeant d’un service.
- Membre d’un groupe criminel utilisant un wallet collectif.

Chaque niveau requiert un type d’attribution différent.

**Erreur classique** : « cette adresse appartient à [personne] » alors que l’enquête montre seulement « cette adresse a déposé chez Binance ». Personne ≠ adresse de dépôt.

### 18.3 Sources d’attribution

**Preuve directe** :

- Publication volontaire par le propriétaire (« voici mon adresse de tip »).
- Données KYC obtenues via réquisition (autorités).
- Aveu / coopération (procédure judiciaire).

**Preuve forte** :

- Saisies officielles avec adresses publiquement attribuées (FBI press release, DOJ unsealed indictment).
- Sanctions OFAC (SDN list inclut adresses crypto).
- Documents judiciaires publics (acte d’accusation, jugement).

**Preuve modérée** :

- Labels d’outils professionnels (Chainalysis, TRM, Elliptic) — basés sur recherche propriétaire, parfois leaks, parfois partenariats.
- Annonces publiques de vendeurs, services (« notre adresse hot wallet est X »).
- Patterns d’usage cohérents avec attribution (très haut volume, pattern exchange).

**Preuve faible** :

- Recoupement par cluster avec une adresse labellisée.
- Mention sur forum non-vérifiée.
- Inférence par pattern.

**Les outils pro mélangent souvent ces niveaux** — un label dans Chainalysis peut être basé sur preuve forte (annonce officielle exchange) ou modérée (inférence pattern). La documentation interne précise généralement, mais l’analyste sérieux **vérifie la source**.

### 18.4 L’échelle de confiance d’attribution

**Format type** (Annexe E pour matrice complète) :

|Niveau       |Probabilité|Critères                                            |
|-------------|-----------|----------------------------------------------------|
|Certain      |>95%       |Preuve directe (saisie officielle, OFAC, KYC obtenu)|
|Très probable|80-95%     |Multiple labels convergents + comportement cohérent |
|Probable     |60-80%     |Label outil pro + patterns soutenant                |
|Possible     |40-60%     |Inférence par cluster + label faible                |
|Spéculatif   |<40%       |Pattern observé sans support fort                   |

**Bonne pratique** : noter le niveau dans la fiche d’adresse et dans le rapport.

**Évolution dans le temps** : attribution peut **monter** (nouvelles preuves) ou **descendre** (preuves contradictoires émergentes). La fiche évolue.

### 18.5 Cas typiques de mauvaise attribution

**Mauvaise attribution 1 — confondre dépôt exchange et exchange lui-même**.

Une adresse de **dépôt** chez un exchange (créée par l’exchange pour un utilisateur précis) est différente du **hot wallet** de l’exchange. L’adresse de dépôt est attribuée à **l’utilisateur** (via KYC exchange), pas à l’exchange en tant qu’entité criminelle.

Erreur : « cette adresse est Binance » alors que c’est en fait l’adresse de dépôt d’un utilisateur de Binance.

Bon : « cette adresse est une adresse de dépôt utilisateur chez Binance. L’identification de l’utilisateur nécessite réquisition ».

**Mauvaise attribution 2 — sur-attribution par cluster**.

Cluster reconstitué par heuristiques regroupe 50 adresses. Une des adresses est labellisée « possibly Lazarus ». Conclure « tout le cluster est Lazarus » est une **sur-attribution** : le label est faible, le cluster peut contenir d’autres entités, l’erreur peut se propager.

Bon : « cluster contient une adresse labellisée ‘possibly Lazarus’ avec confiance modérée. Le label peut être correct ou ne couvrir qu’une partie du cluster ».

**Mauvaise attribution 3 — attribution à un acteur étatique sans preuve**.

Un cluster qui utilise Tornado Cash et bridges → tentation de l’attribuer à Lazarus. Mais Lazarus n’est pas le seul à utiliser ces outils. Sans preuve spécifique (technique d’attaque, infrastructure, adresses précédemment attribuées), l’attribution étatique est spéculative.

Bon : « patterns cohérents avec acteurs étatiques type Lazarus, mais attribution requiert éléments additionnels pour confirmation ».

**Mauvaise attribution 4 — confondre opérateur et affilié**.

Dans le RaaS, l’opérateur (qui fournit le malware et l’infrastructure) est distinct des affiliés (qui exécutent les attaques). Une adresse de paiement ransomware peut être contrôlée par l’affilié, le service de blanchiment, l’opérateur, ou une combinaison.

Bon : « adresse contrôlée par un acteur du programme Akira, sans précision possible sur affilié ou opérateur sans preuves additionnelles ».

### 18.6 L’attribution dans les rapports

**Bonnes formulations** :

- « L’adresse X est très probablement (confiance >90%) une adresse de hot wallet de Binance, sur la base du label Chainalysis et du pattern d’activité cohérent. »
- « Le cluster Y contient une adresse précédemment attribuée par OFAC à Lazarus. Le cluster lui-même est probablement (confiance ~75%) lié à des opérations Lazarus, sans pouvoir préciser si l’ensemble du cluster est dédié ou partagé. »
- « L’adresse Z a un comportement cohérent avec un opérateur de pig butchering, mais sans label vendor ni recoupement OSINT, l’attribution reste possible (~50%). »
- « L’identification de l’utilisateur final derrière l’adresse de dépôt nécessite une réquisition auprès de l’exchange concerné, qui dépend des autorités compétentes. »

**Mauvaises formulations** (à éviter) :

- « L’adresse X est Lazarus. » (Sans calibration ni preuve.)
- « Le propriétaire de cette adresse est [nom]. » (Sans preuve directe.)
- « Le cluster est entièrement contrôlé par [groupe]. » (Sur-attribution.)

### 18.7 La responsabilité de l’analyste

L’attribution **engage**. Une attribution incorrecte peut :

**Nuire à un tiers innocent**. Si Sarah attribue à tort un wallet à un individu nommé, et que le rapport est utilisé contre cet individu, dommage réputationnel et juridique potentiel.

**Compromettre une enquête**. Mauvaise attribution oriente l’enquête dans la mauvaise direction, ressources gaspillées.

**Discréditer l’analyste et son organisation**. Une attribution démontrée fausse érode la crédibilité.

**Implications légales**. Diffamation crypto : possible si nom propre attribué sans base solide.

**Discipline** : l’analyste calibre **systématiquement**. Mieux vaut « probable » correct que « certain » incorrect. Mieux vaut « identité non déterminable sans réquisition » que « propriétaire X » erroné.

### 18.8 Fil rouge — MIXSHADOW : attribution prudente

> **🔗 MIXSHADOW — Épisode 12 : calibration d’attribution**
> 
> Sarah finalise l’attribution dans son rapport intermédiaire (semaine 4).
> 
> **Adresse de réception ransomware** :
> 
> - Niveau d’attribution : **probable**, dédiée à l’opération Aurélien Médical, contrôlée par un opérateur Akira ou affilié.
> - Confiance : ~85%.
> - Base : pattern dédié (adresse fraîche utilisée une seule fois pour cette victime), montant correspondant exactement à la rançon négociée, contexte (le portail de négociation Akira a fourni cette adresse).
> - Pas plus précis que « opérateur Akira ou affilié » — distinction non déterminable.
> 
> **Cluster Bitcoin opérationnel post-paiement** :
> 
> - Niveau d’attribution : **probable** Akira (contrôle continu post-paiement).
> - Confiance : ~80%.
> - Base : continuité du peeling chain depuis l’adresse de réception, pattern cohérent, pas de discontinuité.
> - Reste : pourrait être un **service de blanchiment** sous-traitant pour Akira, plutôt qu’Akira directement.
> 
> **Hubs TRON suspects (services de blanchiment)** :
> 
> - Niveau d’attribution : **possible** services de blanchiment.
> - Confiance : ~65%.
> - Base : patterns hub (multi-sources / multi-destinations), pas attribué dans labels Chainalysis/TRM mais cohérent avec services à risque.
> - Action : alerter labels Chainalysis pour enrichir leur base, croiser avec d’autres incidents Akira.
> 
> **FixedFloat / exchange non-KYC X / Tornado Cash** :
> 
> - Niveau d’attribution : **certain** (services publiquement identifiés).
> - Pas de confusion possible — ce sont des services connus.
> 
> **Acteur Akira lui-même (groupe)** :
> 
> - Niveau d’attribution : **certain** que ces fonds sont liés à l’opération ransomware Aurélien Médical attribuée à Akira (le groupe Akira a revendiqué via leak site et négocié avec Aurélien Médical).
> - Mais attribution **personnelle** (qui est dans Akira ?) : **non déterminable** dans le périmètre OSINT MIXSHADOW. Réservé aux autorités via coopération internationale.
> 
> Sarah documente chaque niveau dans le rapport. Pas de précipitation. Pas d’attribution civile spéculative. Calibration honnête. Le rapport est crédible parce qu’il est calibré.
> 
> Cette discipline va payer : la DGSI valide le rapport intermédiaire et le transmet à Europol pour exploitation, parce que les attributions sont exploitables (claires, calibrées, sourcées) — pas politiquement compromises par des sur-attributions.

-----
