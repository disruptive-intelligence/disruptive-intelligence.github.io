---
title: Chapitre 19 — L'économie de la confiance dans l'illégal
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie IV — Comprendre L'économie cybercriminelle
  - index.md
---

## 19.1 Le problème fondamental

Comment des criminels qui ne se connaissent pas physiquement, ne se font pas confiance a priori, opèrent sous des pseudonymes, et ne peuvent pas recourir à la justice en cas de litige, coopèrent-ils malgré tout de manière efficace ? C'est le paradoxe fondamental de l'économie criminelle en ligne. La réponse est un système de gouvernance informel sophistiqué qui remplit les fonctions que le droit commercial remplit dans l'économie légale.

## 19.2 Réputation et vouching

Le capital réputationnel est le bien le plus précieux d'un acteur sur un forum underground. Un profil avec un historique de 50+ transactions réussies, un rating de 4.8/5, et une ancienneté de 3 ans sur le forum est l'équivalent d'un bilan financier AAA dans l'économie légale. Ce capital ne se construit que par le temps et la fiabilité — il ne s'achète pas (sauf en achetant un compte, pratique risquée car elle peut être détectée).

Le vouching — un membre respecté qui se porte garant d'un nouveau venu — est l'équivalent d'une recommandation professionnelle. Un vouch engage la réputation du garant : si le protégé arnaque quelqu'un, le garant perd également en crédibilité.

Ce système de réputation a une conséquence analytique importante : la destruction de la réputation est une forme de disruption extrêmement efficace. Quand les leaks internes de Conti ont révélé que les salariés étaient mal payés et que l'opérateur gardait une part disproportionnée, la confiance des affiliés s'est effondrée et le groupe s'est désintégré.

## 19.3 Escrow et arbitrage

L'escrow (séquestre) est le mécanisme qui permet les transactions entre inconnus. Fonctionnement : l'acheteur dépose les fonds auprès d'un tiers de confiance (le forum ou un service dédié), le vendeur livre le produit, l'acheteur confirme la réception, et le tiers libère les fonds. Si l'acheteur conteste, un arbitre examine le litige et tranche.

Les admins et modérateurs des forums jouent le rôle d'arbitres. Leur pouvoir de sanction (bannissement, gel des fonds en escrow, exposition publique) est le principal mécanisme de discipline dans l'écosystème.

## 19.4 Exit scams et sanctions internes

Quand un acteur accumule suffisamment de fonds en escrow ou de confiance, il peut être tenté de disparaître avec les fonds — c'est l'exit scam. Les exit scams les plus spectaculaires sont ceux des admins de forums ou de marchés eux-mêmes (qui détiennent les fonds de tous les escrow en cours). Plusieurs darknet markets ont fermé par exit scam, emportant des millions de dollars.

Les sanctions internes — bannissement, exposition publique du pseudo ou parfois du vrai nom, blacklisting sur les autres forums — sont les mécanismes de punition. Mais elles ont une portée limitée : un acteur banni d'un forum peut recréer un compte, changer de pseudo, et recommencer.

## 19.5 Service client criminel

La professionnalisation de la cybercriminalité se manifeste aussi dans la qualité du « service client ». Certains opérateurs RaaS offrent un support technique aux affiliés (FAQ, tutoriels, assistance en direct), des interfaces de négociation conviviales pour les victimes (portail web professionnel avec chat en direct, FAQ sur « comment acheter du Bitcoin », et même des « garanties » : si le déchiffreur ne fonctionne pas, l'opérateur le corrige). Cette professionnalisation n'est pas gratuite — elle reflète un calcul économique : un opérateur dont les affiliés sont satisfaits attire plus d'affiliés. Un opérateur dont les victimes croient que payer la rançon résoudra leur problème obtient plus de paiements.

## 19.6 Fil rouge — NEXUS : le marché structuré

> **🔍 NEXUS — Épisode 18**
>
> Le forum XSS, sur lequel opère kr0n0s_ops, utilise un système d'escrow intégré pour les transactions IAB. Le profil de ghost_access montre 47 transactions avec un rating de 4.8/5 et 3 « positive reviews » de clients identifiés comme affiliés RaaS actifs. Il offre une « garantie 48h » : si l'accès vendu ne fonctionne plus dans les 48 heures suivant la vente (parce que la victime a changé ses credentials entre-temps), il fournit un remplacement ou un remboursement.
>
> Le service de négociation nego_phantom a un « portail victime » professionnel avec chat en direct, FAQ multilingue (anglais, français, allemand, espagnol), et un délai de réponse garanti de 4 heures. Le design est soigné — plus professionnel que de nombreux sites de support client légitimes.

---
