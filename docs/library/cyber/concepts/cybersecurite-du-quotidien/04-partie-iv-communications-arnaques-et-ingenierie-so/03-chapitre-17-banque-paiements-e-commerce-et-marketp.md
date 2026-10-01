---
title: Chapitre 17 — Banque, paiements, e-commerce et marketplaces
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie IV — Communications, arnaques et ingénierie sociale
  - index.md
---

Les **faux sites marchands** : copie d'un site légitime avec un domaine proche (soldes-decathlon.fr au lieu de decathlon.fr, amazon-deals-fr.com au lieu de amazon.fr). Les signaux : prix systématiquement 40-70 % en dessous du marché (« trop beau pour être vrai » est presque toujours vrai), pas de mentions légales, pas de numéro SIRET vérifiable, paiement uniquement par virement ou carte (pas de PayPal ni de solution connue), et un site récemment créé (vérifiable via un Whois). Le **faux espace bancaire** : lien de phishing → page de connexion identique au site de la banque → les identifiants sont capturés → l'attaquant se connecte au vrai site avec les identifiants volés. Le réflexe : ne JAMAIS accéder au site de la banque via un lien — toujours taper l'URL directement ou utiliser l'application mobile officielle.

La **fraude à la carte bancaire** : utilisation de la carte en ligne sans le consentement du porteur. Opposition immédiate via l'app bancaire (la plupart des apps permettent de bloquer la carte en un clic) ou le numéro de la banque. Remboursement garanti par la loi pour les opérations non autorisées (article L133-18 du Code monétaire et financier — la banque doit rembourser immédiatement sauf si elle prouve la négligence grave du porteur). Le **faux 3-D Secure** : un pop-up qui imite la page d'authentification forte de la banque mais qui capture les informations → vérifier que la page d'authentification est sur le domaine de la banque.

Les **arnaques marketplace** (Leboncoin, Vinted, Facebook Marketplace) : le faux vendeur qui demande un paiement hors plateforme (« mon lien de paiement est plus simple, passons par PayPal/virement »), le faux acheteur qui envoie un faux lien de paiement (« j'ai payé, validez la réception ici » → le lien est une page de phishing qui capture les informations bancaires du vendeur), et l'IBAN modifié (dans les transactions entre particuliers par email, l'IBAN peut être intercepté et modifié → confirmer l'IBAN par un second canal — appel téléphonique, SMS).

Les **dark patterns** et la manipulation commerciale : les abonnements cachés (essai gratuit 7 jours → prélèvement automatique de 49,99 €/mois si on n'annule pas avant — et l'annulation est volontairement difficile), les cases pré-cochées (« je souhaite recevoir des offres de nos partenaires »), les faux compteurs d'urgence (« plus que 2 articles à ce prix ! », « 15 personnes regardent ce produit en ce moment » — souvent fictifs), et les consentements forcés (cookie banners avec « Tout accepter » en gros bouton vert et « Gérer les préférences » en tout petit lien gris).

## 17.bis — Abonnements et prélèvements récurrents : reprendre la main

Au-delà des dark patterns à l'inscription, il y a la dérive lente des abonnements. Un foyer moyen accumule des abonnements actifs : streaming vidéo et musique, applications, cloud, presse, salle de sport, box mensuelle, services bancaires, assurances complémentaires. Beaucoup sont oubliés et continuent de prélever — l'essai à 0,99 € de l'an dernier facture aujourd'hui 19,99 €/mois.

**Inventorier** : la liste des prélèvements récurrents est visible dans l'app bancaire (« mandats SEPA », « abonnements »), dans les paramètres de l'App Store / Google Play (achats récurrents), et dans les paramètres PayPal (paiements automatiques). À faire au moins une fois par an — idéalement tous les 6 mois.

**Repérer les pièges fréquents** : essais gratuits qui basculent en payant sans alerte, abonnements à durée minimale (1 an) renouvelés tacitement, augmentations de tarif unilatérales (le service informe, l'utilisateur n'agit pas, le nouveau tarif s'applique), services dont l'annulation nécessite un appel téléphonique ou un courrier recommandé alors que l'inscription se fait en deux clics.

**Le droit de résiliation** : depuis la loi du 16 août 2022 et son décret d'application (juin 2023), tout service souscrit en ligne doit pouvoir être résilié en ligne en trois clics maximum (« bouton résiliation »). Si un service vous demande un courrier recommandé pour résilier alors que vous l'avez souscrit en ligne, c'est non conforme. Pour les **assurances et mutuelles**, la résiliation infra-annuelle est possible après 1 an pour la plupart des contrats (loi Hamon). Pour les **télécoms**, la résiliation est gratuite après la période d'engagement initial.

**Surveillance bancaire** : activer les notifications de prélèvement dans l'app bancaire (chaque opération déclenche une notification) — ça révèle immédiatement les prélèvements oubliés et les fraudes naissantes. Un prélèvement inconnu : opposition immédiate sur le mandat SEPA (la banque peut bloquer un créancier), contestation, remboursement (8 semaines pour contester un prélèvement SEPA autorisé, 13 mois pour un prélèvement non autorisé).

**Carte virtuelle / éphémère** pour les essais gratuits : la plupart des banques en ligne (Revolut, N26, Boursorama, BNP Hello bank!) proposent des cartes virtuelles à usage unique ou plafonnées. Utiliser une carte virtuelle pour les essais gratuits permet de bloquer automatiquement le passage en payant sans avoir à se souvenir d'annuler.

---

<a id="chapitre-18"></a>
