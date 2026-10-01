---
title: Chapitre 15 — Construire un graphe de flux lisible
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

Le **graphe de flux** est la représentation visuelle de l’enquête. Bien construit, il rend l’enquête lisible en une page. Mal construit, il devient un **plat de spaghetti** illisible. Ce chapitre couvre la méthodologie de visualisation.

## 15.1 Pourquoi visualiser

**Comprendre soi-même**. La représentation visuelle révèle des patterns invisibles dans le tableau. Un peeling chain devient évident en graphe, opaque en liste.

**Communiquer**. Un rapport avec graphe est lu et compris ; un rapport texte-only est plus difficile à digérer pour décideurs.

**Coopérer**. Quand Sarah brieffe la DGSI, un graphe permet à l’auditoire d’absorber la topologie en quelques minutes.

**Soutenir la mémoire**. Une fois l’enquête archivée, le graphe permet de reconstituer rapidement l’analyse 6 mois plus tard.

## 15.2 Anatomie d’un graphe de flux

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

## 15.3 Codes visuels recommandés

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

## 15.4 Niveaux d’abstraction

Un même graphe peut être visualisé à différents niveaux.

**Niveau 1 — Adresses brutes**. Chaque adresse = un nœud. Trop dense pour une enquête à 100+ adresses. Utile pour analyse fine d’une zone.

**Niveau 2 — Clusters**. Les adresses du même cluster (heuristiques) sont fusionnées en un seul nœud. Donne le « squelette » de l’écosystème. Vue plus lisible pour acteurs majeurs.

**Niveau 3 — Entités**. Les adresses identifiées comme un même service (exchange, mixer) sont fusionnées en une entité. Donne la vue **business** : « Akira → exchange non-KYC X → Tornado Cash → exchange régulé Y ».

**Niveau 4 — Phases**. Synthèse en phases d’opération : « Réception → Layering → Cashout ». Vue ultime pour rapport exécutif.

L’analyste produit **plusieurs vues** selon l’audience :

- SOC / IR : niveau 1 et 2 (détail technique).
- CISO / direction : niveau 3 et 4 (stratégique).
- Autorités : niveau 2 et 3 (opérationnel).

## 15.5 Outils de visualisation

**Chainalysis Reactor** : visualisation native intégrée à l’outil de clustering. Excellente pour enquêtes utilisant Chainalysis. Limites : exports parfois rigides, dépendance plateforme.

**TRM Labs Investigations** : équivalent. Bon graphique intégré.

**Maltego** : référence transverse OSINT. Connecteurs blockchain via plugins (Maltego CTAS, Maltego Crypto). Très flexible, courbe d’apprentissage modérée. Excellent pour graphes multi-sources (crypto + OSINT classique + autres).

**Gephi** : open source, puissant pour grands graphes. Plus orienté analyse statistique réseau (centralité, communautés). Courbe d’apprentissage forte.

**Graphistry** : visualisation GPU pour très grands graphes (>100k nœuds). Cloud ou self-hosted. Cas avancés.

**Obsidian** : pour graphes simples avec annotations textuelles. Léger, rapide. Limité en taille.

**Mermaid (Markdown)** : pour graphes simples intégrables dans rapports Markdown. Limites visuelles fortes mais portable.

**Drawio / Excalidraw** : pour graphes manuels simples. Bons pour documents finaux. Peu adapté pour gros graphes.

**Cytoscape** : alternative à Gephi, JavaScript-based, customisable.

## 15.6 Quand ne PAS visualiser

**Trop peu de données**. Si l’enquête a 5 adresses et 3 transactions, un tableau suffit. Visualisation overkill.

**Trop de données sans abstraction**. 10 000 adresses sans cluster = spaghetti. Soit on abstractit (clusters, entités), soit on segmente (zoom sur une partie).

**Pour le draft d’analyse**. La visualisation soigneusement formattée prend du temps. Ne la produire qu’aux livraisons importantes (rapport intermédiaire, rapport final, briefing). En cours d’enquête, journal Markdown + tableau excel suffit.

## 15.7 Le graphe minimal pour rapport

Pour rapport exécutif (audience non-technique), un **graphe minimal** :

- 5-15 nœuds maximum.
- Niveau 3 (entités) ou Niveau 4 (phases).
- Couleurs claires, légende explicite.
- Annotations textuelles pour les éléments clés (« Étape 3 : conversion BTC → USDT-TRON via exchange non-KYC X »).
- Pas plus de 10-15 arêtes.

Si l’enquête a 100+ adresses, le rapport contient le **graphe minimal** dans le corps, et le **graphe détaillé** en annexe technique.

## 15.8 Fil rouge — MIXSHADOW : graphe à 4 semaines

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
