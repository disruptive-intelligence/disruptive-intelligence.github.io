---
title: Chapitre 15 — Pourquoi raisonner en économie
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie IV — Comprendre L'économie cybercriminelle
  - index.md
---

## 15.1 La cybercriminalité comme économie de services

Comprendre la menace cybercriminelle uniquement par les TTP (comment ils attaquent) est nécessaire mais insuffisant. La dimension économique répond aux questions du « pourquoi » : pourquoi cette cible plutôt qu'une autre, pourquoi cette méthode plutôt qu'une autre, pourquoi cette demande de rançon plutôt qu'une autre.

Un affilié RaaS qui choisit entre attaquer une PME industrielle française et un cabinet d'avocats américain fait un calcul économique : probabilité de succès × montant espéré de la rançon × probabilité de paiement − coût de l'opération − risque d'arrestation. Ce calcul est implicite mais réel. Le comprendre permet de prédire les comportements.

## 15.2 Offre, demande, spécialisation et innovation

Les marchés criminels suivent les mêmes logiques que les marchés légitimes. Quand la demande d'accès initiaux augmente (parce que le RaaS se développe et que les affiliés ont besoin de cibles), des acteurs se spécialisent dans la fourniture d'accès (les IAB). Quand les défenses s'améliorent (les EDR détectent mieux les ransomwares), les outils d'attaque innovent (nouvelles techniques d'évasion, nouveaux crypters). Quand un service est disrupted (un mixer est saisi), un concurrent émerge pour capturer la demande insatisfaite.

Cette dynamique de marché signifie que la disruption d'un acteur individuel a un impact limité si la demande sous-jacente persiste. Fermer un mixer sans réduire la demande de blanchiment de fonds ne fait que rediriger les flux vers un mixer concurrent. La logique économique implique que les stratégies de disruption les plus efficaces ciblent les points de concentration (les rares nœuds qui servent une grande partie du marché) plutôt que les acteurs individuels.

## 15.3 Baisse des barrières d'entrée et industrialisation

Le modèle « as-a-Service » a radicalement abaissé les barrières d'entrée dans la cybercriminalité. En 2010, mener une attaque par ransomware exigeait de savoir développer un malware, de connaître les techniques d'intrusion, de maîtriser les communications chiffrées, et de savoir blanchir de la cryptomonnaie. En 2026, il suffit de louer un accès à une plateforme RaaS (quelques centaines de dollars), d'acheter un accès initial à un IAB (quelques milliers de dollars), et de suivre le mode d'emploi fourni par l'opérateur. Le support technique est inclus.

Cette démocratisation explique l'explosion du volume d'attaques. Le nombre d'affiliés actifs a considérablement augmenté parce que la compétence technique minimale requise a drastiquement diminué. La contrepartie est que de nombreux affiliés sont peu compétents, ce qui se traduit par des erreurs OPSEC exploitables par les défenseurs et les forces de l'ordre.

## 15.4 Arbitrage coûts/risques/profits

Chaque acteur de l'écosystème opère selon un calcul implicite d'arbitrage entre le profit espéré, le coût de l'opération, et le risque encouru. Ce calcul varie selon le rôle.

Pour un développeur de ransomware : profit régulier (salaire ou commission), coût faible (temps de développement), risque modéré (il n'interagit pas directement avec les victimes et opère souvent depuis une juridiction protectrice).

Pour un affilié RaaS : profit potentiellement élevé (70-80 % d'une rançon de plusieurs millions), coût modéré (achat d'accès + infrastructure), risque élevé (interaction directe avec la victime, exposition aux forces de l'ordre, risque de disruption de la plateforme).

Pour un IAB : profit régulier mais limité (quelques milliers de dollars par accès vendu), coût faible (campagnes de phishing automatisées, exploitation de vulnérabilités), risque modéré (pas de lien direct avec l'extorsion, mais poursuivable pour accès non autorisé).

## 15.5 Fil rouge — NEXUS : l'analyse économique commence

> **🔍 NEXUS — Épisode 14**
>
> Samira reconstruit l'économie de l'attaque contre Énergis.
>
> L'accès initial a été vendu par ghost_access pour 12 000 $ (prix observé sur le canal Telegram). C'est un prix élevé pour un accès IAB, ce qui reflète la valeur de la cible (OIV, secteur énergie, accès domain admin). L'accès a probablement été obtenu via un infostealer (le mode opératoire de ghost_access, selon ses annonces, repose sur des campagnes de phishing déployant Lumma) — coût d'acquisition pour l'IAB : quelques dizaines de dollars en infrastructure de phishing.
>
> Le déploiement du ransomware par kr0n0s_ops coûte environ 2 000-3 000 $ (infrastructure, crypter, temps). La rançon demandée à Énergis est de 3,5 M€. Si la rançon avait été payée, la répartition estimée serait : 70-80 % pour l'affilié (2,45-2,8 M€), 20-30 % pour l'opérateur PhantomCrypt (700 K€-1,05 M€). Le ratio investissement/profit potentiel pour l'affilié : environ 1:170.

---
