---
title: 'Chapitre 5 — OSINT défensif : auditer son propre profil'
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 2 — Identité, compartimentation et hygiène comportementale
  - index.md
---

## 5.1 Pourquoi s’OSINTer soi-même est l’étape zéro

Un attaquant qui s’intéresse à toi commence par une recherche ouverte. Tant que tu n’as pas fait cette recherche à sa place, tu défends à l’aveugle. L’OSINT défensif inverse la posture : tu te mets dans la peau de l’adversaire, tu reproduis sa démarche, tu mesures ce qu’il trouvera, puis tu réduis. Ce chapitre est le miroir défensif du cours OSINT Mastery (voir cours dédié pour la méthode offensive complète).

## 5.2 Méthode systématique en six axes

L’OSINT défensif sérieux suit une méthode. Improviser conduit à manquer des angles.

**Axe 1 — Identité civile** : recherche par nom + prénom + ville sur Google, Bing, DuckDuckGo. Pas connecté à un compte. En navigation privée. Avec et sans guillemets. Puis variantes orthographiques. Puis combinaison nom + employeur, nom + ancien lieu d’études.

**Axe 2 — Emails** : tester chaque email connu sur HaveIBeenPwned, Intelligence X, DeHashed (limites légales selon juridictions). Identifier dans quelles fuites tu apparais, quelles données ont été exposées.

**Axe 3 — Pseudonymes** : faire la liste de tous tes pseudonymes (Twitter, Reddit, GitHub, forums, gaming, dating). Pour chacun, recherche directe et username pivot avec des outils comme WhatsMyName ou Sherlock.

**Axe 4 — Numéros de téléphone** : recherche du numéro sur Google, mais aussi sur Truecaller, Sync.me (gardez en tête : ces services sont eux-mêmes intrusifs ; recherchez via un compte temporaire ou via un proche).

**Axe 5 — Photos** : reverse image sur Yandex Images (souvent le plus efficace pour les visages), Google Lens, TinEye, PimEyes (payant, contestable éthiquement), FaceCheck.ID. Tester ses photos professionnelles, ses photos de profil, ses photos publiques.

**Axe 6 — Documents publics** : registres du commerce, archives administratives, listes électorales (selon pays), publications scientifiques, contributions GitHub, mailing-lists archivées.

## 5.3 Outils de référence (2025-2026)

- **HaveIBeenPwned** (gratuit, référence) : fuites de credentials.
- **Intelligence X** (freemium) : recherche dans des dumps, paste sites, Tor.
- **Epieos** (freemium) : recherche par email, téléphone, nom.
- **Hunter.io** : recherche d’emails par domaine (utile pour vérifier ce qu’on expose côté professionnel).
- **Wayback Machine** : archives du web ; vérifier ce qui de toi a été archivé.
- **WhatsMyName, Sherlock** (gratuits) : recherche de pseudonyme sur des centaines de plateformes.
- **PimEyes, FaceCheck.ID** : reverse image faciale (à utiliser avec une photo *non* affiliée à tes comptes principaux pour éviter d’alimenter leurs bases).

**Limite éthique et légale** : certains de ces outils opèrent en zone grise. PimEyes a été condamné en plusieurs juridictions. L’usage à des fins d’audit défensif sur soi-même est généralement légitime ; l’usage sur des tiers sans consentement ne l’est pas. Ce cours ne couvre pas l’usage offensif.

## 5.4 Cartographier les liens entre comptes

Le danger n’est pas chaque compte individuellement, c’est leur connexion. Si l’attaquant prouve que @LeaMartens (Twitter) et lea.martens@gmail.com et leam94 (GitHub) appartiennent à la même personne, il a un graphe complet. La carte que tu produis doit donc inclure ces ponts : reuse d’email entre comptes, photo identique sur deux profils, même biographie, références croisées (« mon GitHub : leam94 » dans le profil Twitter), mêmes contacts mutuels.

## 5.5 Limites de l’auto-OSINT

Tu ne trouveras pas tout ce qu’un attaquant motivé trouvera. Tes angles morts incluent : bases de données vendues qui ne sont pas publiquement indexées, données obtenues par requête judiciaire ou réquisition, données dans des forums fermés, données issues d’OSINT humain (questions posées à ton entourage). L’OSINT défensif est nécessaire mais pas suffisant. Il borne ce que *tout adversaire* trouvera trivialement — pas ce qu’un adversaire ressourcé reconstituera.

## 5.6 *Fil rouge* — Léa fait son OSINT

Léa applique la méthode. Découvertes notables :

- Une vieille photo de classe lycée scannée par une ancienne camarade et postée publiquement sur Facebook, indexée par Google Images, retrouvée par reverse image à partir de sa photo LinkedIn.
- Un mémo professionnel PDF, mis en ligne par un ancien employeur, contenant son nom dans les métadonnées XMP même si retiré du texte visible.
- Un compte de forum nutrition (2014, pseudo lea.m_94) avec son adresse email principale, son alimentation, et ses lieux fréquentés.
- Trois pages d’archives de mailing-lists journalistiques où son adresse pro apparaît en clair.

Elle constate que l’attaquant compétent reconstituerait son identité civile, sa carrière, ses fréquentations professionnelles, et un certain nombre de détails personnels en moins d’une heure. Elle priorise.

-----
