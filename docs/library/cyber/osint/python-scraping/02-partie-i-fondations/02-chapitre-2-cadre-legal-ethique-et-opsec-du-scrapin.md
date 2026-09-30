---
title: Chapitre 2 — Cadre légal, éthique et OPSEC du scraping
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
up:
- - Python & scraping
  - ../index.md
- - Partie I — Fondations
  - index.md
---

> **Avertissement :** ce chapitre fournit des **repères**, pas un conseil juridique. Le droit applicable varie selon ton pays, ton statut (particulier, entreprise, journaliste, chercheur), la nature de la donnée et l’usage final. En cas de doute sur un projet réel, consulte un juriste.

## Le minimum à savoir

### Les 5 questions à se poser avant de scraper

Avant chaque collecte, ce mini-questionnaire :

```
1. La source est-elle publiquement accessible
   sans authentification ni contournement ?

2. Les CGU autorisent-elles cet usage automatisé ?

3. Le robots.txt comporte-t-il des restrictions
   pertinentes pour ce que je veux faire ?

4. La donnée comporte-t-elle des éléments personnels ?
   Si oui, ma collecte respecte-t-elle le principe
   de minimisation et un cadre juridique clair ?

5. Si le site m’écrivait demain pour me demander
   pourquoi je collecte, ma réponse serait-elle solide ?
```


> **Important :** CGU et robots.txt sont **deux choses distinctes**. Les CGU sont un texte contractuel, le robots.txt est une convention technique. Ils doivent être vérifiés séparément. Un robots.txt permissif ne dispense pas de lire les CGU, et inversement.

Si tu réponds **NON** ou **« je ne sais pas »** à l’une de ces questions, **arrête** la collecte automatisée et documente le doute avant d’aller plus loin. En enquête sérieuse, un doute non levé se transcrit dans la fiche d’enquête : c’est une trace honnête, pas une faiblesse.

### Données publiques ≠ données librement exploitables

C’est l’erreur la plus commune. Le fait qu’une donnée soit visible sans connexion ne signifie pas :

- qu’elle est libre de droits (un texte sur un blog reste protégé par le droit d’auteur),
- qu’elle peut être collectée massivement,
- qu’elle peut être republiée,
- qu’elle peut être traitée à des fins commerciales,
- qu’elle peut être croisée avec d’autres sources pour profiler des personnes.

**Une donnée publique reste soumise à un cadre.** Le scraping ne crée pas de droit ; il ne fait que techniquement automatiser une consultation.

### Le fichier `robots.txt`

C’est un fichier texte placé à la racine d’un site (`https://exemple.fr/robots.txt`) dans lequel le propriétaire indique aux robots ce qu’il accepte d’être parcouru.

Exemple :

```
User-agent: *
Disallow: /admin/
Disallow: /api/private/
Allow: /
Crawl-delay: 5

Sitemap: https://exemple.fr/sitemap.xml
```


Lecture :

- `User-agent: *` → règles pour tous les robots.
- `Disallow: /admin/` → ne pas parcourir cette section.
- `Crawl-delay: 5` → attendre 5 secondes entre deux requêtes.
- `Sitemap:` → emplacement du plan du site (bonus pour toi !).

> **Important :** `robots.txt` est une **convention**, pas une loi. Le respecter n’est pas une obligation juridique stricte, mais le **bafouer** est un signal très net que ta démarche est problématique. En pratique : on respecte robots.txt.

### Les CGU (Conditions Générales d’Utilisation)

Les CGU sont un **contrat** entre le service et toi. Beaucoup interdisent :

- l’accès automatisé,
- l’extraction massive,
- la réutilisation commerciale,
- la constitution de bases dérivées.

Lire les CGU avant de scraper professionnellement n’est pas optionnel. La portée juridique des CGU dépend de plusieurs facteurs (acceptation effective, position du droit local), mais leur violation peut t’exposer à des poursuites civiles, voire pénales selon le contexte.

### Le RGPD en 5 principes (UE)

Si tu touches à des **données personnelles** (un nom, un email, une photo identifiable…), tu entres dans le périmètre du RGPD. Cinq principes à retenir :

1. **Finalité** : tu dois savoir pour quoi tu collectes, et le dire clairement.
1. **Minimisation** : tu collectes le strict nécessaire.
1. **Base légale** : tu dois pouvoir justifier ta collecte (intérêt légitime, mission d’intérêt public, etc.).
1. **Conservation limitée** : tu ne gardes pas indéfiniment.
1. **Droits des personnes** : la personne peut demander accès, rectification, suppression.

Pour un projet OSINT défensif sérieux qui touche des données personnelles, un **registre des traitements** simplifié est une bonne pratique.

### Ce qu’on ne fait **jamais**

- Contourner une authentification.
- Utiliser un compte qui n’est pas le sien.
- Exploiter une faille technique (CAPTCHA bypass, exploitation d’une vulnérabilité).
- Scraper massivement des données personnelles pour profilage commercial.
- Republier des contenus protégés sans autorisation.
- Surcharger un site (assimilable à un déni de service).
- Constituer des listes de prospection à partir d’emails moissonnés.

## Très utile en pratique

### Le principe de minimisation, en action

Tu surveilles un blog d’expert pour de la veille. La minimisation, c’est :

- ❌ Aspirer tout le blog tous les jours pour tout garder.
- ✅ Récupérer la liste des nouveaux articles publiés depuis ta dernière collecte.

Tu surveilles les annonces d’embauche d’un concurrent. La minimisation, c’est :

- ❌ Stocker le profil complet de chaque candidat mentionné.
- ✅ Stocker uniquement intitulé du poste, date de publication et URL.

### La traçabilité, en pratique

Chaque enregistrement de ta collecte doit contenir, au minimum :

|Champ         |Exemple                         |
|--------------|--------------------------------|
|`source_url`  |`https://exemple.fr/article/123`|
|`collected_at`|`2026-05-17T14:32:11Z`          |
|`tool`        |`mon-collecteur/0.3.1`          |
|`status_code` |`200`                           |
|`content_hash`|`a3f5...` (SHA-256 du HTML brut)|

Ces métadonnées sont **non négociables**. Sans elles, ta collecte n’est pas reproductible et n’a aucune valeur d’enquête.

### Identifier honnêtement ton script

Quand tu envoies une requête, le serveur reçoit un header `User-Agent`. Par défaut, `requests` envoie quelque chose comme `python-requests/2.31.0`. C’est honnête, mais peu informatif.

**Bonne pratique** : un User-Agent identifiable, qui dit qui tu es et comment te contacter en cas de problème :

```
MonOutilOSINT/0.1 (+contact: osint-projet@example.org)
```


> **OPSEC :** utilise idéalement une adresse **dédiée au projet** (ex. `osint-veille@<ton-domaine>`, un alias, ou une boîte spécifique), **pas** ton adresse personnelle principale. Si quelqu’un veut te recontacter ou te signaler un problème, c’est très bien. Si l’adresse fuit dans des dumps, des spams ou des listes, tu veux que ce soit l’alias projet, pas ta boîte principale.

**Mauvaise pratique** : se faire passer pour un navigateur récent pour échapper aux filtres anti-bot. Sauf cas pédagogique très balisé, c’est un signal d’intention douteuse.

### Charte personnelle de l’analyste OSINT

Voici un modèle, à adapter et signer (au sens : à t’engager intérieurement à respecter) :

```
1. Je collecte des données publiques pour des finalités défensives,
   de veille, de recherche ou de transparence.
2. Je respecte robots.txt et les CGU des sites que je consulte.
3. Je collecte le minimum nécessaire à ma question d’enquête.
4. Je trace systématiquement la source, la date et la méthode.
5. Je ne contourne aucune protection technique.
6. Je n’utilise pas mes outils contre des personnes physiques
   sans cadre légal explicite (mission, mandat, ordre légitime).
7. Je ne republie pas de données protégées sans autorisation.
8. Je respecte le rythme des serveurs (rate limit volontaire).
9. Je m’identifie honnêtement (User-Agent, contact).
10. En cas de doute, je m’arrête et je consulte.
```


## ❌ Erreur classique

```
# Croire que robots.txt protège juridiquement
"Le site a un robots.txt qui interdit le scraping, donc je m’expose
 à des poursuites si je passe outre."
→ Pas si simple. robots.txt est une convention, pas un dispositif
   contractuel. Mais l’ignorer est un signal fort de mauvaise foi
   qui pèsera lourd si un litige survient.

# Croire que l’absence de robots.txt = autorisation
"Pas de robots.txt, donc je peux tout faire."
→ Faux. Les CGU s’appliquent, le droit d’auteur s’applique, le RGPD
   s’applique. robots.txt n’est qu’un signal additionnel.

# Tester le scraper agressif directement sur la cible
"Je veux voir à partir de combien de requêtes le site bloque."
→ Ne fais jamais ça. Tu peux dégrader un service public, exposer
   ton IP, et déclencher des procédures de sécurité automatiques.
   Pour tester un scraper, utilise des sites bac à sable
   (toscrape.com, httpbin.org).

# Confondre "données accessibles" et "données librement réutilisables"
"Cet article de presse est lisible sans abonnement, je peux le
 republier sur mon site."
→ Faux. Le droit d’auteur s’applique indépendamment du paywall.
```


## Bonus

### Affaires juridiques de référence (à titre culturel)

> Ces affaires sont citées **à titre indicatif**. Elles évoluent, leurs conclusions ne sont pas transposables tel quel à ton cas. Pour un projet réel, vérifie l’état du droit avec un juriste.

- **hiQ Labs vs LinkedIn (États-Unis)** : longue bataille judiciaire sur le scraping de profils publics, illustrant la complexité du « public » en pratique.
- **Ryanair vs PR Aviation (UE)** : a précisé que les CGU peuvent restreindre l’usage automatisé même si les données ne sont pas protégées par un droit sui generis.
- **Décisions CNIL** : sanctions répétées sur des moissonnages d’emails à des fins commerciales.

L’annexe C de ce cours liste des ressources pour aller plus loin.

## Exercices

**Guidé :** Récupère manuellement (dans ton navigateur) les fichiers `robots.txt` de trois sites de natures différentes :

1. un grand média (ex. `lemonde.fr/robots.txt`),
1. une administration publique (ex. `service-public.fr/robots.txt`),
1. un site bac à sable (`books.toscrape.com/robots.txt`).

Pour chacun, identifie :

- les sections interdites (`Disallow`),
- la présence éventuelle d’un `Crawl-delay`,
- la présence d’un `Sitemap`.

**Autonome :** Rédige ta propre charte OSINT en 10 règles maximum. Garde-la dans `config/charte.md` à la racine de ton projet. C’est un engagement, pas une décoration.

## ✅ Tu sais maintenant…

- Les 5 questions préalables à toute collecte
- Que « données publiques » ne signifie pas « données librement exploitables »
- Lire et interpréter un `robots.txt`
- Les 5 principes RGPD applicables aux données personnelles
- Ce qu’on ne fait jamais
- Identifier honnêtement son script via User-Agent
- Tenir un cadre éthique personnel

-----
