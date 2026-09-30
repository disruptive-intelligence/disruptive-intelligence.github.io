---
title: Chapitre 24 — Navigateurs, moteurs de recherche et stratégies anti-fingerprint
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 5 — Réseau, anonymat et navigation web
  - index.md
---

## 24.1 Le navigateur : ton plus gros vecteur

Le navigateur exécute du code (JavaScript) reçu de tiers, dispose d’accès à ton réseau, à ton stockage local, à ton fingerprint. C’est *l’application la plus dangereuse* sur ton appareil, et celle que tu utilises le plus. Son choix et sa configuration sont disproportionnellement importants.

## 24.2 Tor Browser

**Modèle** : Firefox modifié pour anonymat maximal, intégré à Tor. Configuration standard : pas de plugins, JavaScript désactivable par niveau de sécurité (Standard/Safer/Safest), résolution standardisée, fingerprint uniformisé.

**Règle absolue** : **ne pas modifier Tor Browser**. Chaque modification te rend unique parmi les utilisateurs Tor, donc identifiable. Pas d’extensions ajoutées, pas de redimensionnement de fenêtre (Tor Browser uniformise par lettering), pas de changement de fuseau.

**Usage** : navigation anonyme ponctuelle, accès aux services onion, accès à des sites depuis des comptes anonymes.

## 24.3 Mullvad Browser

Lancé en 2023 par Mullvad et Tor Project en partenariat. **C’est Tor Browser, sans Tor**. Même hardening anti-fingerprint, mais le trafic passe par où tu veux (VPN, ou rien).

**Pour qui** : utilisateurs qui veulent l’anti-fingerprinting du Tor Browser sans la latence Tor, et qui acceptent l’idée d’être dans un « pool Mullvad Browser » d’utilisateurs uniformisés.

**Recommandation forte** : Mullvad Browser pour navigation privée quotidienne, Tor Browser pour anonymat.

## 24.4 Brave

Brave est un fork Chromium avec protections natives : bloqueur de trackers, anti-fingerprinting, mode Tor intégré (limité, à ne pas confondre avec Tor Browser).

**Avantages** : compatibilité Chromium (sites qui marchent partout), protections par défaut décentes, alternative Chrome pour qui ne peut pas Firefox.

**Limites** :

- Brave Rewards / Brave Search / Brave Ads : Brave a un modèle économique qui inclut sa propre régie publicitaire. Désactivable, mais à savoir.
- Modifications opaques par moments (par ex. ajout de référents dans certaines URLs cryptocurrency, fix dans 2020-2021).
- Mode Tor intégré : utilise le réseau Tor mais sans le hardening de Tor Browser. À ne pas utiliser comme substitut.

## 24.5 Firefox + arkenfox / LibreWolf

**Firefox** standard : bon, surtout en activant Enhanced Tracking Protection (Strict), bloquant les cookies tiers, désactivant la télémétrie.

**arkenfox/user.js** : ensemble de configurations Firefox durcies, maintenu par la communauté. Pour profils techniques qui veulent ajuster Firefox finement.

**LibreWolf** : fork Firefox avec hardening arkenfox par défaut, télémétrie supprimée. Plus simple si tu veux du Firefox durci sans toucher à user.js.

**Limite** : Firefox + arkenfox ne donne pas le même « blend in » que Mullvad Browser ; tu restes individuellement identifiable. Bon pour bloquer, pas pour anonymiser.

## 24.6 Safari, Vanadium

- **Safari** : intégration Apple, antitracking ITP correct, fingerprint relativement uniforme (du fait du peu de variation hardware iOS). Pas le plus configurable, mais pas le pire.
- **Vanadium** : navigateur intégré à GrapheneOS, basé sur Chromium avec hardening additionnel. Pas Firefox, donc différent profil de fuites mais bonne sécurité.

## 24.7 Multi-navigateurs par usage

La pratique gagnante : **plusieurs navigateurs pour des usages distincts**.

- **Quotidien (banking, mail, services connectés)** : Brave ou Firefox.
- **Recherche/exploration** : Mullvad Browser, déconnecté.
- **Anonymat** : Tor Browser.
- **Travail sensible** : navigateur dans un environnement isolé (qube Qubes, Tails).

## 24.8 Extensions : minimum utile

La règle est contre-intuitive : **moins tu installes d’extensions, mieux c’est**. Chaque extension :

- Te rend plus identifiable (signature unique).
- Est un vecteur potentiel de compromission (extension vendue, mise à jour malveillante).
- Augmente la surface d’attaque.

Le minimum viable :

- **uBlock Origin** : bloqueur de trackers et publicités, gold standard. À ne pas remplacer par AdBlock Plus (modèle « acceptable ads »).

Le reste est optionnel : NoScript pour contrôle granulaire JavaScript (mais lourd), HTTPS Everywhere (devenu inutile, HTTPS par défaut), Privacy Badger (utile en complément, parfois redondant avec uBlock).

Une extension de protection peut bloquer certains trackers, mais elle devient elle-même un signal de fingerprinting si elle modifie le comportement du navigateur d’une manière rare. L’objectif n’est donc pas d’empiler les extensions, mais d’utiliser un profil cohérent et commun à d’autres utilisateurs.

## 24.9 Profils, containers, sessions séparées

Firefox supporte des **Multi-Account Containers** : onglets séparés avec cookies isolés. Tu peux avoir un onglet « personnel » et un onglet « travail » qui se croient sur des navigateurs différents. Très utile pour ne pas connecter accidentellement tes comptes.

Sur tous les navigateurs : utiliser plusieurs profils utilisateur (Chrome, Brave, Firefox supportent) pour des compartiments différents.

## 24.10 Moteurs de recherche

- **Google Search** : profil publicitaire massif. Évite, ou ne l’utilise que connecté à ton identité civile pour les recherches non sensibles.
- **DuckDuckGo** : ne tracke pas par défaut. Bing en arrière-plan pour résultats. Acceptable mais incidents passés sur tracking Microsoft.
- **Brave Search** : propre index, modèle publicitaire séparé.
- **Startpage** : Google sans tracking (revend les requêtes anonymisées à Google).
- **SearXNG** : méta-moteur open source, agrège plusieurs moteurs. À auto-héberger ou utiliser sur instance de confiance.
- **Kagi** : payant, sans publicité. Modèle qui change l’incitatif : Kagi te facture, donc n’a pas besoin de vendre tes données. Recommandé pour qui peut payer.

Aucun moteur n’est parfait. Le choix dépend du compromis confidentialité/qualité/coût.

## 24.11 Comptes connectés : perte d’anonymat instantanée

Tant que tu es connecté à un compte (Google, Facebook, Microsoft) dans un navigateur, *toute l’activité de ce navigateur* est rattachable à ce compte. Pas seulement les actions sur le site du compte. Les pixels et trackers du site qui te tracent en arrière-plan croisent ta navigation avec ton identité.

**Conséquence** : *ne pas* utiliser le navigateur où tu es connecté à ton Google personnel pour activité sensible. Multi-navigateurs ou containers.

## 24.12 *Fil rouge* — Léa adopte Mullvad Browser

Léa configure son environnement de navigation :

- **MacBook Pro pro** : Firefox pour usage rédaction, Brave pour navigation rapide, Mullvad Browser pour recherche enquête.
- **Profil enquête sur GrapheneOS** : Vanadium pour mobile, Tor Browser disponible pour cas anonymes.
- **Pour les sessions Tails** : Tor Browser par défaut, jamais modifié.

Test post-config : AmIUnique et browserleaks sur chaque navigateur. Résultats : Mullvad Browser et Tor Browser sont en « pool » (similarité élevée à d’autres utilisateurs), Firefox + uBlock est intermédiaire, Brave varie selon Shields.

-----
