---
title: Chapitre 47 — Collecter et documenter une source légitime avec Hunchly
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IX — Navigation pratique et collecte défensive encadrée
  - index.md
---

Au-delà de la simple navigation, l'analyste documente. **Hunchly** est l'outil de référence pour la capture structurée d'investigation web (clearnet et .onion). Ce chapitre montre concrètement son usage sur une source légitime.

## 47.1 Pourquoi documenter une session ?

Une page visitée sans capture, sans horodatage et sans hash est une **observation fragile**. L'analyste peut s'en souvenir, mais il ne pourra pas forcément la démontrer, la transmettre, ou la réutiliser dans un rapport.

Sans outil structuré, la capture d'une session de navigation produit :

- Des screenshots éparpillés sans nommage cohérent.
- Pas d'horodatage fiable.
- Pas de hash garantissant l'intégrité.
- Pas de capture de la source HTML.
- Pas de lien entre observations et investigation globale.

## 47.2 Pourquoi Hunchly

Outil commercial développé par Justin Seitz (auteur de Bellingcat, OSINT). Extension Chrome/Firefox + application desktop. Capture **automatiquement** et **systématiquement** chaque page visitée pendant la session.

**Fonctions clés** :

- Capture HTML + screenshot + metadata pour chaque page visitée.
- Horodatage précis.
- Hashing automatique des contenus capturés.
- Annotations (selectors mode pour highlighter et noter).
- Cases d'investigation avec organisation.
- Export rapport structuré.

**Coût** : ~130 USD/an pour licence individuelle, options enterprise.

**Alternatives gratuites** : OSINT Cloner (open source, moins riche), captures manuelles structurées (chronophage).

## 47.3 Installation et configuration

**Téléchargement** : hunch.ly. Compte requis pour licence.

**Installation** :

1. Application desktop (Windows, macOS, Linux). Installation classique.
2. Extension navigateur (Chrome, Firefox/Tor Browser). Activer.
3. Authentification de l'extension avec compte Hunchly.

**Configuration pour Tor Browser**.

- Hunchly fonctionne dans Firefox (Tor Browser est basé sur Firefox ESR).
- Installer l'extension Firefox dans Tor Browser.

**Note OPSEC** : installer une extension dans Tor Browser modifie le fingerprint du navigateur. Pour les exercices sur sources légitimes, ce risque est acceptable. Pour une investigation sensible (cible paranoïaque, OPSEC critique), l'architecture de collecte doit être validée par l'équipe, et l'outil de capture ne doit pas être improvisé — éventuellement, scripts custom hors Tor Browser pour ne pas modifier le fingerprint.

**Premier test** :

1. Lancer Hunchly desktop.
2. Créer un nouveau **case** : « Test_Premiere_Session ».
3. Activer la capture (toggle on).
4. Visiter quelques pages clearnet (n'importe quoi : Wikipedia, un blog).
5. Observer : Hunchly capture chaque page automatiquement.
6. Retour à l'application desktop : pages capturées listées avec horodatages, screenshots.

## 47.4 Walkthrough : documenter SecureDrop NYT

Cas pratique : documenter le déploiement SecureDrop du New York Times pour une investigation sur l'écosystème journalisme protection sources.

**Setup**.

1. Tor Browser ouvert, mode Safest.
2. Hunchly extension activée.
3. Hunchly desktop : nouveau case « SecureDrop_Ecosystem_2026 ».
4. Activer la capture.

**Étape 1 — cadrage clearnet**.

- Visite nytimes.com.
- Navigation vers section « tips ».
- Page « How to Tip the NYT ».
- Hunchly capture chaque page automatiquement.
- Annotation : « Description officielle des canaux confidentiels par le NYT ».

**Étape 2 — vérification de l'adresse SecureDrop**.

- Sur la page tips, identification de l'adresse .onion SecureDrop NYT.
- Cross-check avec freedom.press/securedrop/directory.
- Visite freedom.press, vérification que l'adresse matche.
- Hunchly capture les deux pages.
- Annotation : « Cross-check freedom.press confirme l'adresse SecureDrop NYT ».

**Étape 3 — visite de l'adresse SecureDrop**.

- Coller l'adresse .onion dans Tor Browser.
- Page d'accueil SecureDrop : interface standard avec deux options (« Submit documents and messages » / « Check for replies »).
- Hunchly capture.
- Annotation : « Page d'accueil SecureDrop NYT, interface standard. Pas de soumission test. ».
- **NE PAS CLIQUER sur « Submit » ni interagir au-delà de la consultation passive**.

**Étape 4 — capture de la documentation SecureDrop**.

- Visite securedrop.org (clearnet) — projet officiel.
- Navigation dans documentation, FAQ.
- Hunchly capture.
- Section sur les déploiements actifs : capture de la liste.

**Étape 5 — autres déploiements similaires**.

- Visite Guardian SecureDrop (procédure identique).
- Visite ProPublica, The Intercept.
- Hunchly capture chaque session.

**Étape 6 — finalisation**.

- Désactivation de la capture.
- Dans Hunchly desktop : vérification que toutes les pages attendues sont capturées.
- Annotations finales sur le case.
- Export du case en PDF ou archive ZIP pour archivage long terme.

**Livrable attendu** :

- Page clearnet officielle documentant SecureDrop.
- Page Freedom of the Press Foundation confirmant l'adresse.
- Page .onion SecureDrop capturée.
- Annotations expliquant la méthode.
- Export Hunchly horodaté.
- Conclusion : miroir authentifié / non authentifié.

## 47.5 Documenter une page institutionnelle

Variante : documenter le site officiel d'une institution avec son miroir .onion.

**Cas — Tor Project** :

- Visite torproject.org (clearnet).
- Visite Tor Project .onion.
- Comparaison des deux versions : contenu identique, structure identique.
- Hunchly capture les deux versions de chaque page.
- Documentation de la cohérence : la version .onion est un miroir authentique, pas une version modifiée.

Cet exercice est particulièrement utile en sensibilisation interne : il montre à des profils non techniques qu'un service .onion peut être institutionnel, légitime et défensif.

## 47.6 Bonnes pratiques de collecte

**Avant la session** :

- Définir l'**objectif** de la collecte (qu'est-ce qu'on cherche à documenter ?).
- Préparer le **case Hunchly** avec nom explicite.
- S'assurer que la connexion Tor est fonctionnelle.
- Lister les URLs à visiter (planification).
- Vérifier que le mode Safest est actif.
- Validation hiérarchique si exercice non-routinier.

**Pendant la session** :

- **Capture activée** dès le début, désactivée seulement à la fin.
- **Annotations en temps réel** : ne pas attendre la fin pour documenter ses observations.
- Pas de téléchargement.
- Pas de soumission de formulaire.
- Pas d'activation JS sauf justification documentée.
- Pas de manipulation de fichiers téléchargés sans VM isolée séparée.

**Après la session** :

- **Revue des captures** : vérifier qu'aucune page critique n'a été oubliée.
- **Annotations finales** : synthèse, conclusions, hypothèses.
- **Export** : générer rapport ou archive pour conservation long terme.
- **Sauvegarde** : stockage immutable (Ch.28).
- **Mise à jour graphe d'investigation** : ajouter entités observées, relations.
- **Mise à jour de la base interne** (liste de référence Ch.46.7).

## 47.7 Limites et alternatives

**Limites Hunchly** :

- Coût (130 USD/an).
- Tier modeste — pour entreprises grandes, options plus puissantes (commerciales).
- Ne capture pas les flux dynamiques complexes (vidéos, APIs).
- Ne fonctionne pas en CLI (pour automatisation lourde).

**Alternatives partielles** :

- **OSINT Cloner** : extension navigateur open source, moins riche.
- **Wayback Machine** (archive.org) : pour clearnet uniquement, ne capture pas .onion.
- **archive.today** : alternative avec différentes couvertures.
- **Scripts custom** : Python avec Selenium ou Playwright + capture HTML, screenshots, hashing. Pour automatisation de masse.
- **Capture manuelle** : screenshots OS + sauvegarde HTML « Save Page As » + hash en CLI. Chronophage mais zéro coût.

**Important** : Hunchly ne remplace pas une vraie chaîne de conservation de preuve lorsqu'un dossier doit être exploité judiciairement. Il facilite la documentation, mais le niveau probatoire dépend aussi du contexte, de la procédure interne, du stockage, de la signature et de l'horodatage qualifié (Ch.28).

---
