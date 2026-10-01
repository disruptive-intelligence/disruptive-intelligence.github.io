---
title: Chapitre 11 — Les types de liens
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie III — Liens, corrélations et rigueur analytique
  - index.md
---

## 11.1 Lien technique

Le lien technique est établi quand deux entités partagent un élément d'infrastructure : même adresse IP, même certificat SSL/TLS, même infrastructure C2, même malware ou builder, même serveur DNS, même registrar, ou même pattern de configuration technique.

Les liens techniques sont les plus faciles à établir automatiquement (les transforms Maltego, les requêtes Shodan, les bases de données CTI les révèlent) et les plus trompeurs. Le piège fondamental est la mutualisation : deux domaines hébergés sur la même IP partagent un lien technique, mais ce lien peut refléter une co-gestion intentionnelle (les deux domaines appartiennent au même acteur) ou une simple coïncidence d'hébergement (les deux domaines sont chez le même hébergeur bulletproof sans aucun lien entre les locataires).

Pour évaluer la significativité d'un lien technique, l'analyste doit estimer la spécificité de l'élément partagé. Un certificat wildcard partagé est très spécifique (il implique un contrôle administratif commun). Un même Google Analytics ID est très spécifique (il implique un accès au même compte Google). Un même ASN est peu spécifique (des milliers de clients partagent un ASN). Un même registrar est peu spécifique (un registrar populaire sert des millions de domaines).

## 11.2 Lien financier

Le lien financier est établi quand un flux de valeur (typiquement un transfert de cryptomonnaie) connecte deux entités. Les liens financiers sont généralement plus significatifs que les liens techniques, car un transfert d'argent implique une relation intentionnelle — on ne transfère pas des fonds à un inconnu par accident.

Les types de liens financiers incluent le paiement direct (A paie B pour un service — achat d'accès, commission RaaS, paiement de crypter), le transfert via intermédiaire (A envoie des fonds à B via un wallet de transit — le lien est indirect mais traçable), le partage de revenus (les fonds d'une rançon sont automatiquement répartis entre l'affilié et l'opérateur — la répartition révèle le modèle économique), et le blanchiment commun (deux acteurs utilisent le même service de mixing ou le même circuit de cash-out).

Les limites sont réelles : un transfert via un mixer ou un exchange centralisé rompt le lien traçable entre l'émetteur et le récepteur. Le mixer reçoit des fonds de centaines d'utilisateurs et redistribue des fonds mélangés — le fait que les fonds « ressortent » du mixer vers un wallet ne prouve pas qu'ils « proviennent » d'un wallet d'entrée spécifique (c'est un lien probabiliste, pas déterministe).

## 11.3 Lien identitaire

Le lien identitaire relie des comptes ou des profils à une même personne (ou à une entité prétendant être la même). Les indices identitaires incluent le même pseudo utilisé sur plusieurs plateformes, le même email, la même clé PGP (un identifiant fort — la possession de la clé privée prouve le contrôle), le même avatar ou photo de profil, et le même numéro de téléphone (pour les comptes Telegram notamment).

La force d'un lien identitaire dépend de la spécificité de l'identifiant. Une clé PGP est un identifiant fort (unique et non devinable). Un pseudo courant est un identifiant faible (des milliers de personnes peuvent utiliser le même pseudo). Un email ProtonMail unique est un identifiant modéré (il est probable, mais pas certain, qu'un seul acteur l'utilise).

## 11.4 Lien linguistique et comportemental

Le lien linguistique et comportemental est établi quand deux comptes ou profils partagent des caractéristiques stylistiques ou comportementales distinctives : même vocabulaire spécifique, mêmes tics de langage, mêmes erreurs grammaticales, mêmes heures d'activité, mêmes patterns de réponse.

Ces liens sont individuellement faibles — deux personnes du même pays et de la même génération auront des styles similaires. Mais en faisceau avec d'autres indicateurs, ils deviennent significatifs. Un même fuseau horaire d'activité + un même argot régional + les mêmes abréviations inhabituelles = un faisceau convergent.

## 11.5 Lien social

Le lien social est établi quand deux acteurs interagissent directement : conversation observée sur un forum ou un canal Telegram, recommandation mutuelle (vouching), co-administration d'un canal, mention directe dans un message. Les liens sociaux révèlent les relations de confiance — un vouching sur un forum est l'équivalent d'une recommandation professionnelle.

## 11.6 Lien narratif et informationnel

Le lien narratif est établi quand deux entités relaient le même récit, utilisent les mêmes éléments de langage, ou participent à la même campagne de communication. Ce type de lien est caractéristique des écosystèmes d'influence (Ch.32) mais apparaît aussi dans les opérations ransomware quand le leak site, le canal Telegram, et un média de façade diffusent le même message.

## 11.7 Lien temporel

Le lien temporel est établi quand deux événements se produisent en séquence rapide, suggérant une relation causale. Un accès est mis en vente sur un forum le 3 mars ; un ransomware est déployé chez la même victime le 15 mars. La séquence temporelle (12 jours entre la vente d'accès et le déploiement) est un indicateur fort de lien opérationnel entre l'IAB et l'affilié.

Les liens temporels sont particulièrement utiles quand les autres types de liens sont absents (pas de lien technique direct, pas de lien financier traçable). La temporalité est un indice de causalité potentielle — pas une preuve de causalité, mais un signal qui justifie une investigation plus approfondie.

## 11.8 Qualifier un lien

direct/indirect, fort/faible, contextuel/structurel

Chaque lien identifié doit être qualifié selon trois axes.

**Direct vs indirect.** Un lien direct implique une relation sans intermédiaire (A paie B, A utilise le serveur de B, A et B communiquent directement). Un lien indirect passe par un intermédiaire (A et B utilisent le même mixer, A et B sont membres du même forum). Les liens directs sont plus significatifs.

**Fort vs faible.** Un lien fort est basé sur un indice hautement spécifique (même clé PGP, même certificat wildcard, transfert financier direct). Un lien faible est basé sur un indice peu spécifique (même hébergeur, même fuseau horaire, même forum). Un lien fort peut suffire à établir une connexion ; un lien faible nécessite une corroboration par d'autres liens.

**Contextuel vs structurel.** Un lien contextuel est ponctuel (A et B ont interagi une fois sur un forum). Un lien structurel est durable et récurrent (A achète régulièrement des accès à B depuis 6 mois). Les liens structurels révèlent la véritable architecture de l'écosystème.

## 11.9 Fil rouge — NEXUS : tableau de synthèse des liens

> **🔍 NEXUS — Épisode 11**
>
> Samira compile un tableau de synthèse des liens identifiés à ce stade de l'investigation.
>
> | Entité A | Entité B | Type de lien | Qualification | Confiance |
> |----------|----------|-------------|---------------|-----------|
> | Domaine C2 | Blog phantom-news | Technique (même IP + même certificat + même GA ID) | Direct, Fort, Structurel | Élevée (B1) |
> | Email proton.me | Pseudo kr0n0s_ops (XSS) | Identitaire (breach) | Direct, Fort | Élevée (B2) |
> | kr0n0s_ops (XSS) | kr0n0s_ops (GitHub) | Identitaire (même pseudo) + Comportemental (même style) | Direct, Modéré | Modérée (C2) |
> | kr0n0s_ops (Telegram) | ghost_access (Telegram) | Social (interaction directe, achat d'accès) | Direct, Fort, Structurel | Élevée (B1) |
> | ghost_access | Cible Énergis | Temporel (vente d'accès 12 jours avant le déploiement) | Indirect, Fort | Modérée (C2) |
> | Wallets PhantomCrypt | Exchange Dubaï | Financier (flux via mixer) | Indirect, Modéré | Modérée (C3) |
> | Wallets PhantomCrypt | Wallet para-étatique | Financier (flux via mixer) | Indirect, Faible | Faible (D3) |
>
> Chaque lien est qualifié, ce qui permet de distinguer les connexions solides des pistes exploratoires.

---
