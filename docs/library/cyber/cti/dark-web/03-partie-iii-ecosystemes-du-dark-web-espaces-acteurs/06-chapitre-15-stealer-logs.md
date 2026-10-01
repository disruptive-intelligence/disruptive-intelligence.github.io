---
title: Chapitre 15 — Stealer logs
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

anatomie, marchés, investigation défensive

*Ce chapitre traite en profondeur le vecteur de compromission initiale le plus courant en 2025-2026. Les stealer logs sont devenus la matière première de l'écosystème cybercriminel — l'équivalent du pétrole brut qui alimente toute la chaîne de valeur.*

## 15.1 Qu'est-ce qu'un stealer log ?

Un **stealer log** est le produit de l'exécution d'un **infostealer** (malware spécialisé dans le vol de données de sessions) sur la machine d'une victime. Contrairement à un breach de base de données (qui produit des listes de credentials en masse), un stealer log capture **l'intégralité de l'environnement de la session utilisateur** sur un poste spécifique.

Un log typique contient :

- **Credentials du navigateur** : tous les logins/mots de passe enregistrés dans Chrome, Firefox, Edge, Brave, Opera — des dizaines voire des centaines de comptes par victime.
- **Cookies de session actifs** : permettent de se connecter à un service **sans mot de passe**, en contournant même le MFA. C'est **le vecteur le plus dangereux** de 2024-2026.
- **Données d'autofill** : noms, adresses, téléphones, données de cartes bancaires stockées.
- **Wallets crypto** : clés privées ou seed phrases stockées dans des extensions navigateur (MetaMask, Phantom, Exodus).
- **Données machine** : hostname, IP, OS, logiciels installés, capture d'écran au moment de l'exécution.
- **Sessions de messagerie** : tokens Discord, Telegram Desktop, WhatsApp Desktop.
- **Données Steam, Epic Games** : sessions gaming, de plus en plus ciblées.
- **Fichiers sélectifs** : certains stealers exfiltrent des fichiers selon patterns (documents avec mots-clés, certains types de fichiers).

La **puissance destructrice** d'un stealer log tient à sa granularité : ce n'est pas un seul couple login/mot de passe — c'est **l'intégralité de l'identité numérique** d'un utilisateur, capturée à un instant T, sur un poste spécifique.

## 15.2 Les infostealers dominants en 2025-2026

**Lumma Stealer** (aussi « LummaC2 »). Modèle d'abonnement, ~250 USD/mois. Extrêmement répandu. Évolution constante pour éviter la détection (polymorphic, updates hebdomadaires). En 2024-2025, dominant en volume.

**RedLine**. Historiquement dominant, toujours actif malgré tentatives de disruption. Développé par un acteur russophone. Large écosystème d'affiliés.

**Vidar** (dérivé d'Arkei). Populaire pour le ciblage de wallets crypto — modules spécifiques pour MetaMask, Coinbase Wallet, etc.

**Raccoon Stealer v2**. Relancé après l'arrestation de son opérateur initial en 2022.

**StealC**. Émergent, léger et polyvalent.

**RisePro**. Ciblage spécifique des applications crypto et des gestionnaires de mots de passe (LastPass, 1Password, Bitwarden).

**Meta Stealer, Phemedrone, DarkCrystal RAT** : autres familles documentées.

**Point d'entrée économique**. SOCRadar 2025 : **dès 15 USD en version de base**, avec modèles d'abonnement qui rendent les stealers accessibles à pratiquement n'importe quel acteur. Cette accessibilité explique leur adoption massive.

**Vecteurs de distribution** :

- **Malvertising** : publicités Google/Bing malveillantes redirigeant vers des téléchargements piégés. Technique en forte croissance 2024-2025.
- **Faux sites de téléchargement logiciels crackés**. Vecteur historique dominant — particulièrement efficace sur utilisateurs cherchant cracks.
- **YouTube tutorials malveillants** : descriptions de tutoriels contenant des liens vers des malwares sous couvert d'outils légitimes.
- **Pièces jointes email** : documents Office avec macros, archives protégées par mot de passe.
- **Packages npm/PyPI malveillants** : supply chain logicielle.
- **Telegram groupes** : liens de téléchargement douteux.

## 15.3 Les marchés de stealer logs

**Russian Market**. Successeur de facto de Genesis Market (saisi avril 2023, Operation Cookie Monster). Plus grand marché de logs actif en 2025-2026. Logs vendus individuellement avec système de **recherche par domaine** — l'acheteur cherche des logs contenant des credentials pour un domaine spécifique (par exemple, un VPN d'entreprise cible). Prix : 1-15 USD pour log basique, 50-500 USD pour log avec accès corporate (VPN, Citrix, RDP).

**Genesis Market (historique, saisi 2023)** — modèle innovant qui mérite mention. Genesis ne vendait pas seulement des credentials, mais des **bots** — navigateurs virtuels répliquant l'empreinte exacte de la victime (fingerprint navigateur, cookies, résolution d'écran, timezone, liste des plugins). Permettait d'usurper la session sans déclencher les contrôles anti-fraude basés sur fingerprint. Modèle repris par d'autres marchés.

**Canaux Telegram**. De nombreux logs distribués en bulk via canaux spécialisés, souvent **gratuitement** (« free logs ») pour attirer vers des services premium. Canaux gratuits contiennent logs anciens ou faibles valeur, mais constituent point d'entrée pour acteurs peu sophistiqués.

**2easy.gg historique**. Marché spécialisé fermé, opérations law enforcement en 2024.

**StealC Marketplace, LummaC2 Shop** : marchés adossés à des familles de stealers spécifiques.

## 15.4 Investigation défensive : workflow

Pour un analyste défensif surveillant l'exposition de son organisation.

**Étape 1 — Monitoring des domaines**. Configurer des alertes sur marchés de logs (via plateformes commerciales type Flare, Hudson Rock, SOCRadar, Breach.ai, Flashpoint) pour les domaines de l'organisation. Chaque nouveau log contenant des credentials du domaine déclenche une alerte.

**Étape 2 — Évaluation du log**. Pour chaque log détecté, évaluer la criticité :

- **Log avec credentials webmail uniquement** : préoccupant mais gérable (reset mot de passe + vérif MFA).
- **Log avec credentials VPN/Citrix + cookies de session actifs** : **urgence** — l'attaquant peut accéder au SI sans connaître le mot de passe actuel si le cookie est encore valide.
- **Log avec credentials cloud (Azure, AWS, GCP)** : critique — impact potentiellement majeur sur l'infrastructure.

**Étape 3 — Identification du poste source**. Les métadonnées du log (hostname, IP, OS, softwares installés) permettent souvent d'identifier le poste compromis. Ce poste est **potentiellement toujours infecté** par le stealer — **changer le mot de passe sans éradiquer le stealer ne fait que fournir un nouveau mot de passe à l'attaquant**. C'est l'erreur la plus fréquente et la plus dangereuse.

**Étape 4 — Remédiation**. Le poste source doit être **isolé et réimaginé**. Tous les credentials contenus dans le log doivent être réinitialisés — pas seulement les credentials corporate, mais aussi les comptes personnels qui pourraient servir de pivot (compte GitHub personnel avec accès à des repos de l'entreprise). **Sessions actives révoquées** (tokens, cookies invalidés).

**Étape 5 — Hunting**. Le SOC vérifie si les credentials du log ont été utilisés pour des connexions suspectes depuis la date estimée de compromission. Recherche dans logs d'authentification (VPN, AD, applications cloud) pour connexions depuis IPs inhabituelles, user agents inconnus, horaires atypiques.

## 15.5 Statistiques et géographie

Données SOCRadar 2025 : concentration des logs sur grandes plateformes consumer :

- Facebook : 93M+ logs
- Google : 67M+
- Roblox : 66M+
- Instagram : 34M+
- Microsoft Live : 31M+
- Amazon : 22M+
- Netflix : 22M+
- PayPal : 19M+

Géographie : Inde domine (2,7M logs), Brésil (1,9M), Indonésie (1,3M), États-Unis (1,2M). La position basse des US suggère meilleure détection ou remédiation plus rapide plutôt que taux d'infection inférieur.

**Implications** : plateformes gaming (Roblox, Twitch, Epic Games — utilisateurs jeunes avec hygiène credentials faible) et e-commerce/streaming (Amazon, Netflix — données de paiement stockées) sont cibles privilégiées. PayPal se distingue comme facilitateur direct de fraude.

## 15.6 Limites et faux positifs

**Expiration**. Les cookies expirent (typiquement 30-90 jours), les mots de passe peuvent avoir été changés, le poste peut avoir été réimaginé. Log ancien (6+ mois) a une probabilité d'exploitation réussie **beaucoup plus faible** qu'un log frais.

**Faux positifs**. Domaine similaire (typosquatting), employé utilisant email pro sur site grand public, log recyclé déjà traité. Filtrage humain indispensable.

**Bruit**. Un grand compte monitoring génère des dizaines d'alertes par jour — priorisation nécessaire (criticité, fraîcheur).

## 15.7 Fil rouge — DARKSTREAM : les stealer logs Vectris

> **🌐 DARKSTREAM — Épisode 9 : découverte collatérale**
>
> En parallèle de son investigation sur aero_source, Lucas vérifie l'exposition Vectris sur les marchés de logs. Recherche sur Russian Market via l'accès monitoring Athéna : **12 logs** contenant des credentials du domaine `vectris-aerospace.eu`.
>
> Analyse des 12 logs :
> - 3 logs contiennent **credentials VPN (Fortinet FortiClient) avec cookies de session** — **urgence maximale**.
> - 4 logs avec credentials webmail Outlook 365.
> - 2 logs avec accès à une application SaaS RH.
> - 3 logs avec credentials divers (Jira, GitLab enterprise).
>
> Les 3 logs VPN datent de **2 à 4 mois** — compatible avec la timeline de la compromission Vectris. **Hypothèse** : l'attaquant initial aurait utilisé un infostealer comme vecteur d'accès, les logs ont ensuite été revendus sur Russian Market par un courtier (possiblement distinct de l'auteur de l'exfiltration finale), et aero_source est soit le même acteur, soit un acheteur final qui revend les données.
>
> Hostnames des 3 logs VPN :
> - VECTRIS-SALES-047 : laptop commercial.
> - VECTRIS-RD-112 : poste R&D — **celui-ci est particulièrement préoccupant**, potentiellement le vecteur de l'exfiltration initiale des 420 Go.
> - VECTRIS-IT-008 : poste IT.
>
> Lucas escalade immédiatement au RSSI Vectris. Mandiant (IR prestataire) confirme : VECTRIS-RD-112 est bien le poste central de la compromission, déjà identifié comme point d'entrée. Les deux autres sont des compromissions collatérales non identifiées jusqu'ici — actions immédiates enclenchées (isolement, forensics, reset massif).
>
> Découverte collatérale précieuse : la surveillance dark web a révélé **deux postes compromis supplémentaires** que l'investigation interne n'avait pas identifiés. Illustration concrète de la valeur défensive de la veille dark web.

---
