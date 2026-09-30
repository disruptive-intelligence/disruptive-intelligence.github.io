---
title: Chapitre 46 — Authentifier un miroir officiel .onion
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IX — Navigation pratique et collecte défensive encadrée
  - index.md
---

L'usurpation d'adresses .onion (typosquatting) est une menace réelle. Un faux miroir BBC peut imiter parfaitement le vrai, capturer les communications de visiteurs, ou injecter de la désinformation. Ce chapitre apprend une compétence très concrète : **ne jamais faire confiance à une adresse .onion simplement parce qu'elle « ressemble » à une adresse officielle**.

## 46.1 Le risque du typosquatting .onion

Le typosquatting .onion exploite une faiblesse **humaine**, pas une faiblesse cryptographique : l'adresse est sûre cryptographiquement, mais l'utilisateur peut se tromper d'adresse.

**Le mécanisme**. Comme expliqué Ch.45, on peut générer des adresses commençant par un préfixe choisi via vanity address generation. Un attaquant peut créer une adresse `bbcnewsd73XXX...` (différente de l'adresse officielle BBC) qui présentera le même préfixe.

**Risques pour le visiteur** :

- **Contenu altéré** : faux miroir injecte désinformation, propagande, contenus modifiés.
- **Phishing** : faux miroir avec formulaire de login récupère credentials d'utilisateurs (rare pour médias, plus pertinent pour SecureDrop usurpé qui pourrait piéger des sources).
- **Exploits navigateur** : faux site héberge NIT pour identifier IPs réelles.
- **Tracking** : faux site ajoute beacons pour identifier visiteurs.

**Cas réels documentés** : multiples miroirs imitant SecureDrop, de fausses versions de Tor Project lui-même, des copies cosmétiques de marketplaces (qui scament les acheteurs).

## 46.2 Identifier les sources d'autorité — par ordre de confiance

1. **Site clearnet officiel de l'organisation**. La méthode la plus fiable : trouver l'adresse .onion sur le site clearnet officiel.
2. **Header Onion-Location**. Les sites compatibles envoient un header HTTP `Onion-Location: <adresse.onion>` quand un visiteur arrive sur leur version clearnet. Tor Browser détecte ce header et propose une bannière « Cette page est disponible sur version .onion ». Garantie d'authenticité (le serveur officiel envoie l'info).
3. **Documentation officielle ou page d'aide** de l'organisation, mentionnant explicitement l'adresse.
4. **Répertoire officiel reconnu** — par exemple, **Freedom of the Press Foundation** (freedom.press) maintient une liste centralisée des SecureDrop déployés.
5. **Annuaire communautaire reconnu** (Tor.taxi, Dark.fail) — uniquement en complément, jamais comme source primaire.
6. **Hidden Wiki et listes anonymes** : non fiables comme source primaire.

**Recoupement multi-sources**. Pour confirmer une adresse .onion, exiger **au moins deux sources indépendantes** qui matchent — typiquement (1) + (2) ou (1) + (3) ou (1) + (4).

## 46.3 Walkthrough : authentifier le miroir BBC

Exemple complet, étape par étape.

**Étape 1 — clearnet officiel**.

- Naviguer sur bbc.com (depuis Tor Browser ou tout navigateur).
- Chercher « onion » ou « Tor » dans la barre de recherche du site, ou Google « BBC .onion site ».
- Trouver l'article officiel BBC : « The BBC's .onion site explained ».
- Adresse mentionnée : `bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion`.

**Étape 2 — Onion-Location header**.

- Visiter bbc.com depuis Tor Browser.
- Observer la bannière « .onion available ». Cliquer pour redirect.
- Confirmer que l'adresse correspond à celle de l'étape 1.

**Étape 3 — comparaison caractère par caractère**.

- Bien aligner les deux adresses : `bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion`.
- Comparer chaque caractère. Pas seulement le préfixe. La fin (`uqd.onion`) doit aussi matcher.

**Étape 4 — première visite**.

- Coller l'adresse dans Tor Browser.
- Vérifier que la page charge correctement (logo BBC, structure familière).
- Pas d'avertissement de certificat (si HTTPS sur .onion, le certificat doit être valide).
- Naviguer quelques articles, comparer avec bbc.com (les contenus doivent être cohérents).

**Étape 5 — bookmark et documentation**.

- Sauvegarder l'adresse dans Tor Browser bookmarks.
- Documenter dans le carnet d'investigation l'adresse, la date de vérification, et la source d'autorité.

**Livrable attendu** : note courte indiquant adresse officielle trouvée, source clearnet utilisée, date de vérification, méthode de comparaison, conclusion d'authenticité.

## 46.4 Walkthrough : authentifier un miroir SecureDrop

SecureDrop est plus sensible que BBC — destiné à des sources lanceurs d'alerte qui prennent des risques. L'authentification est cruciale.

**Le mécanisme officiel SecureDrop** :

- Chaque média qui déploie SecureDrop documente son adresse .onion sur **son site clearnet officiel**.
- L'adresse SecureDrop est différente du miroir « news » du média.
- La fondation **Freedom of the Press Foundation** (freedom.press) maintient une liste centralisée.

**Walkthrough — SecureDrop NYT**.

1. Aller sur nytimes.com.
2. Chercher « tips » ou « confidential tips » dans le menu.
3. Trouver la page « How to Tip the NYT » qui détaille les méthodes (post, encrypted email, Signal, SecureDrop).
4. Adresse SecureDrop NYT mentionnée explicitement.
5. Cross-check sur freedom.press/securedrop/directory : la NYT y est listée avec son adresse, qui doit matcher.
6. Si les deux sources concordent : adresse authentique.

**Précaution importante** : une instance SecureDrop ne se « teste pas » en envoyant un message factice. Un tel comportement pollue le canal de réception du média et peut déclencher une analyse inutile côté journalistes. La visite est strictement passive — observer la page d'accueil, capturer pour documentation, ne pas interagir.

## 46.5 Détecter un faux miroir — trois familles de signaux

Méthodologie pour vérifier si une adresse suspecte est un faux miroir.

**Signaux d'adresse** :

- Adresse trouvée uniquement sur sources tierces (pas sur clearnet officiel).
- Préfixe similaire mais corps différent.
- Adresse trouvée seulement sur annuaire communautaire ou hidden wiki.
- Différence d'un ou deux caractères avec l'adresse officielle (typo intentionnelle).

**Signaux de contenu** :

- Design proche mais contenu daté ou divergent.
- Articles modifiés vs version clearnet.
- Liens externes suspects (boutons « download » qui pointent vers des fichiers .exe).
- Demandes de login inhabituelles pour un site qui n'en exige pas habituellement.
- Formulaires absents de la version clearnet.

**Signaux techniques** :

- Absence d'Onion-Location quand le site officiel en propose un.
- Scripts inhabituels (en mode Safest, JS bloqué donne des indices indirects).
- Redirections vers domaines non cohérents.
- Téléchargements proposés sans justification.
- Latence anormalement faible (peut indiquer hosting non-Tor traditionnel masqué).

**En cas de doute** :

- Ne pas continuer la navigation.
- Documenter l'adresse suspecte (capture, hash de la page).
- Signaler au CSIRT compétent (CERT-FR pour France) pour évaluation.
- Pour les médias : signaler à l'organisation usurpée.

## 46.6 Le cas des moteurs de recherche .onion

Pour les exercices de cette partie, **seuls DuckDuckGo et Ahmia doivent être utilisés**. Les autres moteurs (Torch, Haystak, Tor66, Excavator) sont mentionnés pour culture générale, mais leur usage peut exposer à des résultats non maîtrisés, y compris illicites ou frauduleux.

- **Ahmia** : projet documenté, filtre CSAM strict, source d'autorité raisonnable. Adresse vérifiable sur ahmia.fi.
- **DuckDuckGo .onion** : indexe le clearnet via Tor exit, pas le contenu .onion. Moteur principal de Tor Browser par défaut.

Pour un analyste pro qui doit explorer du contenu .onion criminel dans le cadre d'une mission, l'élargissement aux autres moteurs est possible — mais relève alors du cadre Partie V, pas des exercices de cette partie.

## 46.7 Tenir une liste de référence interne

Pour un programme d'investigation durable, **constituer et maintenir une liste interne** de miroirs .onion légitimes vérifiés.

**Format suggéré** :

| Organisation | Type | Adresse .onion (extrait) | Source officielle | Date vérification | Vérificateur | Statut |
|---|---|---|---|---|---|---|
| BBC | Média | bbcnewsd73...uqd.onion | bbc.com (article ref) | YYYY-MM-DD | Analyste | Actif |
| Tor Project | Institution | 2gzyxa5ihm7...wid.onion | torproject.org | YYYY-MM-DD | Analyste | Actif |
| ProPublica | Média | p53lf57qovy...uqd.onion | propublica.org | YYYY-MM-DD | Analyste | Actif |
| SecureDrop NYT | Lanceur d'alerte | (adresse complète) | nytimes.com tips + freedom.press | YYYY-MM-DD | Analyste | Actif |

**Règle** : une adresse non revérifiée depuis plusieurs mois ne doit pas être considérée comme fiable par défaut. Revue trimestrielle minimum.

**Partage** : cette liste peut être partagée avec d'autres équipes internes (formation, communications, juridique). Pour le partage externe (ISAC), nettoyer ce qui est sensible et publier en TLP CLEAR.

---
