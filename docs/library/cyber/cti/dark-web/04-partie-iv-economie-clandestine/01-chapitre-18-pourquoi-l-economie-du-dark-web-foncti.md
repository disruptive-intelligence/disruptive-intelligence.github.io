---
title: Chapitre 18 — Pourquoi l'économie du dark web fonctionne
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IV — Économie clandestine
  - index.md
---

À première vue, l'économie du dark web devrait être impossible. Des inconnus anonymes transigent pour des montants significatifs sans tribunaux, sans contrats exécutables, sans banque centrale, sans identité vérifiée. La tentation d'arnaque devrait être permanente et dévastatrice. Pourtant, des dizaines de millions de transactions se déroulent chaque année, avec un taux de complétion relativement élevé. Comprendre pourquoi c'est un problème économique fondamental — et sa solution éclaire l'investigation.

## 18.1 Le problème du trust sans tiers de confiance

Toute transaction économique pose un **problème de confiance**. Le vendeur craint le non-paiement, l'acheteur craint la non-livraison. Dans une économie classique, ce problème est résolu par plusieurs instruments :

- **Tribunaux** : en cas de litige, une juridiction neutre tranche selon un droit écrit.
- **Contrats** : engagements formalisés exécutables.
- **Intermédiaires** : banques, cartes de crédit avec mécanisme de chargeback, plateformes avec garanties.
- **Identité publique** : les parties sont identifiées, leur réputation est documentée, les arnaques laissent des traces traçables.

Dans le dark web, **aucun de ces instruments classiques n'est disponible**. Les parties sont pseudonymes, il n'y a pas de tribunal applicable aux transactions illégales, les paiements crypto sont irréversibles (pas de chargeback), aucune autorité ne peut légitimement contraindre une partie à exécuter.

Comment l'économie fonctionne-t-elle alors ? La réponse : par un **système de substitution institutionnelle** — les forums, marchés et communautés créent des institutions privées qui remplacent fonctionnellement les institutions publiques manquantes.

## 18.2 Les institutions de substitution

**La réputation individuelle persistante**. Chaque pseudonyme a un historique transactionnel, des reviews, des feedbacks. Un pseudonyme avec 500 transactions réussies et 2 ratings négatifs est plus digne de confiance qu'un pseudonyme avec 3 transactions. La **réputation est le capital principal** d'un acteur sérieux — et la perdre est coûteux (repartir de zéro sous un nouveau pseudo, temps d'accumulation de 6-18 mois).

**L'escrow de forum ou marché**. Mécanisme de dépôt : l'acheteur envoie le paiement à un tiers (le forum ou le marché), qui le retient jusqu'à confirmation de livraison. Si l'acheteur confirme, le vendeur est payé. Si litige, arbitrage. Ce mécanisme, quoique imparfait, réduit drastiquement le risque d'arnaque unilatérale (Ch.19).

**Le vouching (parrainage)**. Un membre établi engage sa propre réputation en garantissant un nouveau. Si le nouveau scam, le parrain est pénalisé. Cette **chaîne de confiance transitive** permet d'accepter des nouveaux sans qu'ils partent de zéro total.

**L'arbitrage communautaire**. En cas de litige, les modérateurs ou admins tranchent selon des principes publiés (règles du forum, précédents). La **publication du jugement** fait fonctionner le système — un vendeur déclaré scammer voit son pseudonyme sali sur toute la plateforme, souvent cross-platform.

**La pression sociale et la communauté**. Les forums actifs ont une **mémoire collective**. Les scammers notoires sont connus, leurs pseudonymes listés publiquement, leurs IPs parfois publiées. Cette publicité sociale fonctionne comme un ban industriel — un scammer identifié est grillé dans tout l'écosystème pour des mois.

**Les blacklists cross-forum**. Certains forums partagent leurs listes de bannis. Un scammer banni sur XSS peut se retrouver banni préventivement sur Exploit. Cette coordination inter-forums est imparfaite mais réelle.

## 18.3 La coûteuse construction de réputation

Pour un acteur sérieux, construire une réputation utilisable prend **6-18 mois au minimum**. Le processus typique :

**Mois 1-3 — entrée**. Création du compte sur un forum, posts de présentation, participation à des discussions. Lecture active, apprentissage des codes. Pas de vente immédiate (interdit par les règles de la plupart des forums sérieux pour les nouveaux).

**Mois 3-6 — premières transactions**. Petites ventes (50-500 USD), avec échantillons gratuits pour démontrer la qualité. Chaque transaction réussie ajoute une review positive. Les premiers 10-20 transactions sont les plus difficiles — pas encore de réputation établie, les acheteurs sont prudents.

**Mois 6-12 — consolidation**. Avec ~30-50 transactions réussies, le vendeur est **trusted**. Prix peuvent monter, qualité/spécificité de l'offre plus haute, accès aux zones premium du forum. Les gains commencent à être significatifs.

**Mois 12+ — établissement**. Après 100+ transactions, le vendeur est une figure reconnue. Clients récurrents, accès à des produits premium (0-day, accès corporate haut de gamme). Revenus potentiels de plusieurs centaines de milliers à plusieurs millions USD/an.

**Cette courbe explique plusieurs comportements** : les scammers ont tendance à opérer en rafales courtes (2-4 semaines de scam intensif, puis abandon du pseudo), parce que construire une réputation sérieuse prend trop de temps pour le petit gain à court terme. Les acteurs sérieux protègent leur réputation — ne scamment pas leurs clients, parce que la valeur actualisée de leur réputation est bien supérieure au gain d'un scam.

## 18.4 Les ruptures de confiance

Malgré ces mécanismes, les ruptures se produisent.

**Exit scams par opérateur**. Traitement Ch.20. Un opérateur de marché ou forum s'enfuit avec les fonds en escrow.

**Vendeurs seniors qui scamment**. Rare mais arrive. Un vendeur avec 500 transactions et excellente réputation qui scam massivement en une seule opération finale. Motivation : gain ponctuel considérable avec perte de la réputation acceptée. Plus fréquent quand le vendeur sent que sa réputation va tomber de toute façon (arrestation imminente, conflit interne).

**Attaques externes**. Un forum compromis par les forces de l'ordre ou par des concurrents peut voir son historique de transactions falsifié, ses escrows volés, ses membres dox. Disruption temporaire ou définitive de l'économie locale.

**Cyclic collapse**. Parfois, une cascade de méfiance se déclenche : un vendeur majeur scam → les acheteurs méfiants retirent leurs fonds en masse → l'opérateur ne peut honorer les retraits → exit scam de l'opérateur → plateforme fermée. Panique bancaire, version dark web.

## 18.5 Pourquoi ça marche malgré tout

Mathématiquement, l'économie fonctionne parce que :

- **Le nombre de transactions honnêtes dépasse les transactions frauduleuses**. Les acteurs sérieux, majoritaires en nombre et en volume, dominent l'activité globale.
- **La perte de réputation est coûteuse**. Pour un acteur établi, le gain d'un scam est typiquement inférieur à la valeur actualisée de sa réputation. L'incitation rationnelle est d'honorer les transactions.
- **Les mécanismes de substitution capturent la plupart des cas**. Escrow, arbitrage, blacklists gèrent la majorité des litiges.
- **Les pertes sont partagées**. Les acheteurs savent qu'un certain pourcentage de transactions échoueront. Ils calculent cette « taxe » dans leur modèle économique.

Pour un analyste, ces mécanismes sont autant de **points d'observation**. Un vendeur qui sort du schéma standard (pseudonyme neuf, pas de vouching, prix très bas, refus d'échantillon) est en probabilité très élevée un scammer — ce qui influe sur la priorisation des pistes d'investigation.

---
