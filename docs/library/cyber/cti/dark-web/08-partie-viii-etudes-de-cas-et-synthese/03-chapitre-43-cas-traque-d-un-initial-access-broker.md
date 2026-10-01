---
title: Chapitre 43 — Cas traque d'un Initial Access Broker
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VIII — Études de cas et synthèse
  - index.md
---

Troisième cas type : la **traque d'un IAB** spécifique qui a posté une annonce concernant un type d'organisation que le client surveille.

## 43.1 Le contexte

**Organisation cible** : grand groupe industriel énergétique français, OIV. RSSI cherche à comprendre les acteurs IAB qui pourraient cibler son secteur.

**Mandat** : investigation sur un IAB spécifique, **acidproxy**, qui a posté il y a 3 jours sur XSS Forum une annonce d'« Access French energy operator, AD admin, 4500 endpoints ». Description compatible avec plusieurs opérateurs énergétiques français. Pas nécessairement le client lui-même, mais investigation requise.

**Objectifs** :

- Identifier (au mieux possible) l'opérateur ciblé.
- Caractériser le profil acidproxy.
- Évaluer si client est concerné directement ou via prestataire.
- Produire intelligence sur ce type d'IAB pour défense préventive.

## 43.2 Étape 1 — Profilage acidproxy

**Recherche XSS** : compte créé il y a 14 mois. 47 posts. Réputation : 2 reviews positives, 0 négative. Trois transactions confirmées par le forum (escrow). Profil intermédiaire.

**Posts antérieurs** : ventes d'accès dans manufacturing UK, retail DE, healthcare US. **Pas seulement énergie** — opportuniste large.

**Style linguistique** : anglais correct, quelques fautes typiques russophone (articles, prépositions). Tournures cohérentes.

**Pivots** :

- Exploit.in : pas de compte direct identifié.
- BreachForums : compte « acid_proxy » créé 8 mois, 12 posts. Style compatible. PGP **différente** — possible compte secondaire ou chemin distinct.
- Telegram : handle pas identifié dans posts publics.
- XMPP : `acidproxy@xmpp.is` mentionné — serveur classique.

**Wallet BTC** : adresse mentionnée pour 2 transactions antérieures. Cluster Chainalysis : ~25 adresses, ~85 000 USDT cumulés. Flux vers exchange non-KYC + quelques sorties identifiées vers wallet labellisé « Garantex » (avant sanctions 2022).

## 43.3 Étape 2 — Identification de la cible

**Le post acidproxy** détaille : « French energy operator, ~4500 endpoints, AD admin (DA), Citrix admin, ICS network bridged, sells with proof, PoC available ». Prix demandé : 75 000 USD.

**4 500 endpoints** dans énergie française = environ une dizaine d'opérateurs candidats : majors (EDF, Engie, TotalEnergies subsidiaries), opérateurs régionaux, grandes entreprises de services énergétiques.

**Démarche** : pas de contact direct (risque que acidproxy alerte la cible). Recherche indirect.

**Cross-référencement** :

- Stealer logs Russian Market sur les 10 candidats. Patterns observés : multiples logs sur 3 candidats, mais aucun avec accès AD admin clairement identifié dans les logs.
- Posts adjacents acidproxy mentionnent « access via Fortinet vulnerability » — date de la vulnérabilité Fortinet exploitée massivement courant 2025-2026.
- Recherche de communiqués publics récents — un opérateur régional (« Énergie X » anonymisé) a publié il y a 2 semaines un communiqué mentionnant « incident de sécurité maîtrisé ». Communiqué vague — possible cover up partiel.

**Hypothèse forte** : Énergie X est la cible probable. Pas certitude, mais forte probabilité (75%+).

## 43.4 Étape 3 — Décision et action

**Le client n'est pas Énergie X**. Mais Énergie X est un partenaire technique (interconnexions réseau électrique).

**Coordination** : le RSSI client contacte le RSSI Énergie X via canal sectoriel (ISAC énergie européen). Information partagée TLP RED.

**Réaction Énergie X** : confirme l'incident. Compromission identifiée 2 semaines plus tôt, en cours de remédiation. acidproxy peut effectivement avoir l'accès. Énergie X mobilise IR pour vérifier si l'accès est encore actif, déconnexion totale en cours. Communication avec ANSSI (déjà notifiée).

**Pour le client** : pas de compromission directe identifiée. Mais l'interconnexion réseau avec Énergie X est mise en revue. Pare-feux durcis, monitoring renforcé sur les flux concernés.

## 43.5 Étape 4 — Suivi de acidproxy

Au-delà du cas immédiat, la veille acidproxy continue.

**Monitoring posts** : nouvelles annonces sur XSS, Exploit, BreachForums.

**Monitoring wallet** : transactions reçues, flux. Si un acheteur paie acidproxy, la transaction sera traçable.

**Monitoring secondaires** : si Énergie X confirme déconnexion, acidproxy ne peut plus livrer son « produit » → comportement après ?

**Apprentissage durable** : acidproxy est désormais documenté dans la base CTI interne du client. Si acidproxy poste une nouvelle annonce contre un acteur énergie EU, alerte automatique.

## 43.6 Apprentissages

**Valeur de la veille IAB**. Détecter une annonce IAB **avant** qu'elle aboutisse à une attaque permet alerte précoce — soit pour la cible directe, soit pour l'écosystème adjacent.

**Identification probabiliste**. Sans contact direct (qui alerterait l'IAB), l'identification reste probabiliste. Mais 75%+ probabilité, croisé avec autres signaux (communiqué Énergie X), suffit pour action.

**Coopération sectorielle critique**. Sans ISAC, le client n'aurait pas pu transmettre l'alerte à Énergie X. Le canal ISAC fait la différence.

**Limites**. L'IAB peut continuer ses opérations contre d'autres cibles. La veille permet alertes ponctuelles, pas neutralisation de l'acteur.

**Doctrine**. Pour un OIV, la veille des IAB sectoriels devient stratégique. Investissement justifié par le ROI (une compromission majeure évitée vaut largement le coût annuel d'un programme de veille).

---
