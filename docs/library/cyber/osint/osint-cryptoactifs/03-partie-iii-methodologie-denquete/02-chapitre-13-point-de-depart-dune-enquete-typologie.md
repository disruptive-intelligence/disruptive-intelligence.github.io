---
title: 'Chapitre 13 — Point de départ d’une enquête : typologie d’indices'
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

L’enquête crypto démarre toujours par un **indice initial**. Sa nature détermine les premières actions et oriente l’enquête. Ce chapitre cartographie les types d’indices et la méthode pour les exploiter.

## 13.1 Adresse fournie par une victime

**Cas typique** : pig butchering. La victime communique l’adresse à laquelle elle a envoyé ses fonds.

**Étapes** :

1. **Vérifier la blockchain**. La victime peut se tromper — elle dit « Bitcoin » alors qu’elle a envoyé USDT-TRON. Demander captures de transaction.
1. **Récupérer le TXID** si possible. Avec le TXID, on a une preuve plus solide que juste l’adresse.
1. **Lire la transaction sur explorateur**. Montant, timestamp, adresse de destination.
1. **Constituer fiche** sur l’adresse de destination.
1. **Suivre les flux sortants**. La destination redistribue probablement vers d’autres adresses.

## 13.2 Transaction hash (TXID)

**Cas typique** : alerte SOC sur transaction suspecte, victime de hack ayant capté la transaction de drain.

**Étapes** :

1. Identifier la blockchain (parfois implicite, parfois à vérifier).
1. Lire la transaction complète.
1. Identifier les parties (from, to, montants).
1. Étendre l’enquête depuis ces parties.

## 13.3 Capture d’écran

**Cas typique** : victime envoie capture de la confirmation reçue d’un wallet, screenshot Telegram, photo de QR code.

**Étapes** :

1. **Extraire l’adresse ou TXID** lisiblement de la capture (parfois OCR utile).
1. **Vérifier l’authenticité** : la capture peut être falsifiée. Recouper avec on-chain (l’adresse a-t-elle bien reçu cette transaction à ce timestamp ?).
1. Procéder ensuite comme avec adresse/TXID.

**Piège** : QR code dans la capture. Le décoder (outils en ligne, smartphone). Vérifier qu’il pointe bien vers l’adresse mentionnée.

## 13.4 Lien de paiement / payment URI

**Format BIP-21 Bitcoin** : `bitcoin:bc1q...?amount=0.5&label=Donation`.

**Format Ethereum** : `ethereum:0x...?value=1000000000000000000`.

**Étapes** :

1. Décoder l’URI.
1. Vérifier l’adresse extraite.
1. Procéder comme avec adresse classique.

## 13.5 Email de rançon

**Cas typique** : ransomware, sextortion, fausses menaces.

**Contenu type** : adresse Bitcoin/Monero pour paiement, montant demandé, deadline, instructions.

**Étapes** :

1. **Extraire l’adresse**.
1. Vérifier sur blockchain : a-t-elle été utilisée pour d’autres demandes de rançon (fiche enrichie de l’écosystème ransomware) ? A-t-elle reçu des paiements ?
1. **Croiser** avec bases publiques (databases ransomware tracking, AnyRun, autres).
1. Si sextortion classique de masse, l’adresse peut apparaître dans des centaines/milliers d’emails — pattern de fraude reconnaissable.
1. Si ransomware ciblé, adresse souvent fraîche, dédiée à la victime.

## 13.6 Message Telegram / canal

**Cas typique** : opérateurs ransomware via canaux Telegram, scammers via groupes Telegram, vendeurs de données.

**Étapes** :

1. **Documenter le contexte** : nom du canal, date du message, contenu.
1. Extraire les adresses crypto mentionnées.
1. Suivre méthodologie standard.
1. **Croiser** avec d’autres mentions du canal/acteur.

**Important** : pas de contact direct avec le canal sans cadre clair. Observation passive uniquement pour OSINT.

## 13.7 Wallet trouvé dans un malware

**Cas typique** : analyse de malware ransomware / clipper / stealer qui contient une adresse hardcodée.

**Étapes** :

1. Reverse engineering du malware (compétence cyber, voir cours **Forensique** ou **APT**).
1. Extraction de l’adresse hardcodée ou des adresses générées dynamiquement.
1. Procéder comme avec adresse classique.
1. **Croiser** avec autres souches du malware : la même famille ransomware utilise-t-elle les mêmes patterns ?

## 13.8 Adresse sur forum dark web

**Cas typique** : enquête sur un acteur dark web qui partage son adresse pour réception de paiements (vente de données, services).

**Étapes** :

1. **Documenter le contexte** : forum, post, date, vendeur, contenu vendu/proposé.
1. Extraire l’adresse.
1. Suivre méthodologie standard.
1. **Croiser** avec activités du vendeur (autres forums, autres pseudonymes).

Cf. cours **Dark Web** pour la méthodologie d’enquête sur les forums clandestins.

## 13.9 Adresse dans note de ransomware

Voir Ch.13.5.

## 13.10 Indice indirect : nom d’un acteur, alias, organisation

**Cas typique** : on demande à Sarah « investigue Lazarus » sans adresse de départ.

**Étapes** :

1. **Recherche dans bases publiques d’adresses associées**. OFAC SDN list (qui inclut désormais des adresses crypto). Reports Chainalysis, TRM, Elliptic publiquement disponibles.
1. **Recherche sur Twitter / X** : ZachXBT et autres chercheurs publient régulièrement des adresses associées à des hacks/acteurs.
1. **Recherche dans IndexedLeaks et bases CTI** : des wallets connus sont publiés.
1. **Avec point de départ obtenu**, suivre méthodologie standard.

Cas Lazarus : OFAC a sanctionné de multiples wallets liés. Plusieurs hacks majeurs (Ronin, Atomic Wallet, multiple exchanges) ont des adresses publiques documentées par Chainalysis et FBI.

## 13.11 Priorisation des indices

Quand l’analyste a **plusieurs indices** au démarrage (ce qui est commun dans les gros incidents), il priorise.

**Critères** :

**Solidité**. Un TXID est plus solide qu’une capture d’écran (qui peut être falsifiée). Une adresse confirmée par on-chain analysis est plus solide qu’une mention forum.

**Fraîcheur**. Une adresse active dernière 24h offre plus d’angles (suivre les flux en temps réel) qu’une adresse inactive depuis 2 ans.

**Centralité**. L’adresse principale d’un acteur (hot wallet ransomware) est plus critique qu’une adresse périphérique.

**Coopérabilité**. Une adresse qui transite vers un exchange régulé permet potentiellement réquisition. Une adresse 100% interne au réseau criminel sans interaction externe est plus opaque.

**Effort vs valeur**. Investir 20h sur une adresse Monero qui ne donnera rien vs 5h sur une adresse Bitcoin avec angles multiples → choix évident.

## 13.12 Fil rouge — MIXSHADOW : priorisation des branches

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
