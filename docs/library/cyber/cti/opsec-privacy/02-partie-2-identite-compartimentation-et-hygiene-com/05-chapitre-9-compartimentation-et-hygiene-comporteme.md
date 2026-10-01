---
title: Chapitre 9 — Compartimentation et hygiène comportementale
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 2 — Identité, compartimentation et hygiène comportementale
  - index.md
---

## 9.1 Principe directeur

La compartimentation consiste à structurer ta vie numérique en compartiments étanches, tels que la compromission de l’un n’expose pas les autres. C’est l’architecture défensive la plus puissante disponible à un individu, et celle qui demande le plus de discipline.

Règle : *deux choses qui ne doivent pas être reliées ne doivent jamais l’être par un identifiant commun*. Email, téléphone, photo, appareil, IP, mot de passe, style d’écriture, horaire — chacun peut être un pont.

## 9.2 Niveaux d’identité

Cinq niveaux typiques à distinguer :

1. **Identité légale** : nom civil, état civil, documents administratifs. Pour les démarches officielles, le travail, les contrats, les comptes bancaires.
1. **Identité professionnelle** : nom (peut différer si pseudonyme journalistique), email pro, présence professionnelle. Compartiment majeur pour beaucoup de profils.
1. **Pseudonyme stable** : présence en ligne sous nom de plume, militante, communautaire. Pas anonyme (long terme), mais distinct de l’identité civile.
1. **Pseudonyme jetable** : compte créé pour un usage ponctuel, abandonné après.
1. **Identité anonyme** : pour des actions où l’attribution doit être impossible (sources sensibles, lanceurs d’alerte avant divulgation).

Tous les niveaux n’ont pas le même besoin de défense. Mais ceux qui doivent rester séparés doivent l’être *complètement*.

## 9.3 Compartimenter par dimension

Cinq dimensions de compartimentation :

|Dimension          |Compartimentation faible            |Compartimentation forte                           |
|-------------------|------------------------------------|--------------------------------------------------|
|**Appareil**       |Profils OS séparés                  |Appareils physiquement distincts                  |
|**Compte**         |Comptes séparés sur même fournisseur|Fournisseurs différents par usage                 |
|**Numéro**         |Cartes SIM différentes              |Réseaux différents (eSIM + physique + service IP) |
|**Paiement**       |Cartes virtuelles différentes       |Cartes physiques + cash + dénoués géographiquement|
|**Lieu et horaire**|Distinction maison/bureau           |Lieux totalement disjoints, horaires distincts    |

Le niveau adéquat dépend du threat model. Un journaliste enquêtant sur la criminalité organisée a besoin d’une compartimentation forte de la dimension *appareil* et *numéro* au minimum.

## 9.4 Réutilisation : les corrélateurs silencieux

Les corrélations les plus efficaces ne demandent aucune compétence technique. La réutilisation d’un même identifiant entre deux compartiments les corrèle automatiquement :

- Même email : trivial à corréler.
- Même mot de passe entre comptes : la fuite de l’un dévoile l’autre.
- Même pseudo : `whatsmyname.app` te trouve sur 300 services en quelques secondes.
- Même numéro de téléphone : agrégateurs (Truecaller, Sync.me) corrèlent à grande échelle.
- Même photo de profil : reverse image trouve en quelques minutes.
- Même biographie textuelle : recherche exacte sur Google.

## 9.5 Corrélation par style, contacts, métadonnées

Au-delà des identifiants explicites, des corrélations probabilistes :

- **Style d’écriture** (stylométrie, Ch 35) : longueur de phrases, virgules, expressions, fautes typiques.
- **Horaires de connexion** : ton compte « anonyme » se connecte aux mêmes heures que ton compte nominal.
- **Contacts communs** : deux comptes qui suivent les mêmes 50 personnes sont probablement la même.
- **Appareil/navigateur** : même fingerprint navigateur (cf. Ch 23) = même session probable.
- **IP** : connexion depuis le même réseau domestique sur deux comptes les corrèle (à moins de VPN).
- **Métadonnées de fichiers** : un document publié sous pseudonyme avec l’auteur metadata DOCX = nom civil dans le PDF.

## 9.6 L’erreur ponctuelle qui suffit

La compartimentation rigoureuse, c’est une discipline continue. **Une seule erreur peut la détruire**. Trois exemples historiques :

- Ross Ulbricht (Silk Road) : pseudonyme « altoid » sur un forum cryptographique posté avec son email gmail au format `rossulbricht@gmail.com`. Cf. Annexe 8.
- Hector Monsegur (Sabu, LulzSec) : connexion une seule fois à IRC sans Tor depuis son IP domestique. Cf. Annexe 8.
- Cas Reality Winner : impression d’un document classifié sur l’imprimante de son employeur. Les yellow dots (Ch 31) identifiaient l’imprimante, la date, l’heure. Cf. Annexe 8.

Conséquence opérationnelle : **les routines tuent les erreurs**. Si un comportement sensible est automatique (par exemple : impossibilité physique de se connecter au compte sensible depuis le téléphone quotidien parce qu’aucune appli n’est installée), l’erreur est structurellement empêchée.

## 9.7 Fatigue OPSEC, impulsivité, urgence

La compartimentation est attaquée de l’intérieur par trois ennemis humains :

- **Fatigue** : maintenir deux téléphones, plusieurs comptes, plusieurs gestionnaires de mots de passe, c’est lourd. Au bout de six mois, on relâche.
- **Impulsivité** : « juste cette fois, je me connecte vite à mon compte X depuis ce téléphone ». Une fois suffit pour casser la séparation.
- **Urgence** : un événement (deadline, alerte familiale, opportunité professionnelle) pousse à enfreindre les règles « pour cette fois ».

Défenses : (a) automatiser et désautoriser ; (b) accepter que la friction est le prix de la sécurité ; (c) prévoir des protocoles d’urgence qui ne nécessitent pas d’enfreindre la compartimentation.

## 9.8 Routines pour limiter les erreurs

- Démarrer chaque session sensible par une checklist physique (carte plastifiée, post-it).
- Avoir un appareil dédié physiquement distinct, jamais le « téléphone du moment ».
- Établir des règles non négociables : « jamais cet email sur cet appareil », « jamais ce compte sans VPN ».
- Audit trimestriel des dérives.

## 9.9 Cadrage éthique

La compartimentation et le pseudonymat sont des outils défensifs *légitimes*. Un journaliste qui utilise un pseudonyme pour ses enquêtes, un lanceur d’alerte qui sépare ses canaux, une victime de violences conjugales qui restructure ses comptes pour échapper à un ex-partenaire abusif : tous exercent des droits.

Ce n’est pas le sujet de ce cours d’aborder l’usurpation d’identité, la création de faux profils trompeurs, ou la fraude à pseudonymes. Ces pratiques sont pénalement répréhensibles dans la plupart des juridictions et ne relèvent pas de la sécurité défensive.

-----

> 🟦 **Capstone 1 — Construire son architecture de compartimentation**
> 
> **Objectif** : produire pour soi une matrice de compartimentation opérationnelle, applicable dans les 7 jours.
> 
> **Livrable** : un tableau cinq colonnes (Identité / Appareils / Comptes / Paiements / Canaux) pour chacun de tes compartiments principaux. Pour chaque ligne, identifier les ponts existants (ce qui *relie* deux compartiments) et les éliminer un à un.
> 
> **Exemple — Léa, fin de capstone** :
> 
> |Compartiment         |Identité                            |Appareils                      |Comptes                                |Paiements              |Canaux                                   |
> |---------------------|------------------------------------|-------------------------------|---------------------------------------|-----------------------|-----------------------------------------|
> |Vie civile et famille|Léa Martens (nom civil)             |iPhone perso, MacBook Air perso|iCloud personnel, Gmail perso          |CB BNP perso           |iMessage, WhatsApp avec proches          |
> |Vie pro publique     |Léa Martens journaliste             |MacBook Pro pro                |Proton Mail pro, comptes sociaux pro   |CB pro                 |Email, Signal pro                        |
> |Enquête sensible     |Pseudo non utilisé (compte distinct)|Pixel 8a + GrapheneOS dédié    |Compte SimpleX dédié, Proton avec alias|Cash + cartes prépayées|SimpleX, OnionShare, Signal compartimenté|
> 
> **Ponts à éliminer identifiés par Léa** :
> 
> - Carnet d’adresses iCloud personnel contient des numéros de sources potentielles → migration vers carnet pro.
> - Synchronisation iCloud des photos perso pourrait remonter à des photos pro accidentelles → désactivation de la sync auto, tri manuel.
> - Même MacBook Air pour usage perso et certains comptes pro → bascule vers MacBook Pro pour tout pro.
> - Compte Twitter perso suit le pseudo qui sera utilisé pour publication d’enquête → désabonnement préalable.
