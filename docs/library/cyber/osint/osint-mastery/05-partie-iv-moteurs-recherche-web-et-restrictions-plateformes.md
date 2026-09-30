---
title: PARTIE IV — Moteurs, recherche web et restrictions plateformes
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
chapter: 5
chapters: 15
---

> **Ce que cette partie apprend.** Exploiter efficacement les moteurs de recherche généralistes et spécialisés, maîtriser les opérateurs avancés, intégrer les moteurs IA-assistés avec discernement, préserver et archiver le matériau collecté, comprendre et contourner intelligemment les restrictions plateformes 2024-2026.
>
> **Ce qu'elle ne couvre pas.** Les techniques spécifiques aux personnes/SOCMINT (Partie V), l'investigation corporate (Partie VI), l'analyse d'images (Partie VII).
>
> **Ce que vous saurez faire après cette partie.** Construire des requêtes précises, exploiter les moteurs alternatifs quand Google échoue, utiliser Shodan/Censys/FOFA pour l'infrastructure, mobiliser l'IA-search comme assistant, archiver méthodiquement, adapter sa méthodologie aux restrictions des plateformes.

-----

### Chapitre 19 — Moteurs de recherche généralistes

#### 19.1 Pourquoi Google ne suffit pas

Google reste le premier réflexe, mais sa dégradation 2024-2026 est documentée : résultats personnalisés (bulle de filtrage), suppression de l'opérateur `+`, dépréciation de `intitle:` et `inurl:` en effet, focus sur la « pertinence commerciale » au détriment de l'exhaustivité, dégradation du cache. L'analyste OSINT qui utilise uniquement Google rate une part significative de l'information accessible.

La règle 2026 : **multi-moteurs systématique**. Toute recherche significative doit être conduite sur au moins 2-3 moteurs complémentaires.

#### 19.2 Google : usage raisonné

Malgré sa dégradation, Google reste utile pour :
- Recherches en anglais et langues majeures.
- Indexation rapide de contenus récents.
- Recherche de fichiers (`filetype:`).
- Recherche site-spécifique (`site:`).
- Image search (Google Lens reste compétitif).

**Recommandations.**
- Naviguer **déconnecté** d'un compte Google personnel (profil dédié ou navigation privée).
- Désactiver la personnalisation (paramètres avancés, `&pws=0` dans l'URL).
- Utiliser Google avec VPN pour éviter biais géographique.
- Limiter à `&num=100` pour voir plus de résultats par page.

#### 19.3 Bing : alternative crédible

**Bing** (Microsoft) a fortement progressé depuis 2023, notamment via l'intégration GPT (Copilot). Ses opérateurs sont robustes et certains spécifiques (`contains:`, `linkfromdomain:`).

**Avantages OSINT.**
- Indexation parfois différente de Google (sites manqués par Google peuvent apparaître).
- Image search compétitif (Bing Visual Search).
- Reverse image search dédié.
- API plus accessible que Google.

#### 19.4 Yandex : irremplaçable

**Yandex** (russe) est l'un des outils les plus précieux de l'OSINT contemporain, **pour deux raisons** distinctes :

**Reverse image search supérieur.** Yandex Images est régulièrement classé comme le meilleur moteur de recherche inversée pour visages, scènes, objets. Il indexe différemment et identifie des sources que Google et TinEye manquent.

**Contenus russophones et CEI.** Pour toute investigation touchant la Russie, l'Ukraine, la Biélorussie, l'Asie centrale, Yandex est incontournable.

**Précaution.** Yandex est un service russe. Vos requêtes sont visibles depuis la Russie. Pour usage OSINT sensible, utiliser via VPN et compte d'investigation séparé.

#### 19.5 Baidu : la Chine

**Baidu** est le moteur dominant en Chine. Indispensable pour :
- Recherches sur le web chinois (sites .cn, blogs domestiques).
- Recherche d'entités chinoises (sociétés, personnes, événements).
- Comprendre la version « domestique » d'un sujet international.

**Précautions.**
- Censure massive sur sujets politiques sensibles.
- Vos requêtes peuvent être loguées par les autorités chinoises.
- Interface en mandarin (utiliser DeepL ou Google Translate).
- Préférer accès via VPN japonais/coréen pour cohérence linguistique.

#### 19.6 DuckDuckGo, Brave Search, Mojeek, Marginalia

Moteurs alternatifs orientés privacy ou indexation indépendante.

**DuckDuckGo.** Pas de tracking, résultats Bing + sources indépendantes. Utile pour comparer rapidement avec Google sans empreinte.

**Brave Search.** Index indépendant (depuis 2023). Croissance rapide. Discovery panel intéressant.

**Mojeek.** Index totalement indépendant (UK). Petit mais authentique — pas une syndication. Utile pour découvrir des sites non bien indexés par les majors.

**Marginalia.** Moteur expérimental pour le « web non-commercial » (blogs, wikis, sites personnels). Excellent pour échapper au SEO industriel.

#### 19.7 Recherche multilingue

Toute investigation internationale doit considérer les langues locales.

**Stratégies.**
- Traduire les requêtes dans la langue de la juridiction (DeepL, Google Translate).
- Utiliser le moteur local (Yandex pour russe, Baidu pour chinois, Naver pour coréen, Yahoo Japan pour japonais).
- Indexation par caractères natifs (penser à utiliser cyrillique, arabe, japonais en script natif quand pertinent).
- Translittération inversée pour noms propres (un même nom russe peut s'écrire de plusieurs manières en latin).

**Outils.**
- **Google Translate** : large couverture, qualité moyenne.
- **DeepL** : qualité supérieure pour langues européennes.
- **OpenAI/Claude/Gemini** : pour traductions contextuelles.
- **ChatGPT/Claude pour translittération** : noms russes, chinois, arabes.

#### 19.8 Synthèse — choisir son moteur

| Contexte | Moteur(s) recommandé(s) |
|---|---|
| Recherche générale anglais/français | Google + Bing + DuckDuckGo |
| Reverse image search | Yandex (en premier) + Google Lens + TinEye |
| Contenu russe / CEI | Yandex + recherche cyrillique |
| Contenu chinois | Baidu + traduction |
| Échapper au SEO commercial | Marginalia + Mojeek |
| Privacy-friendly | DuckDuckGo + Brave Search |
| Académique | Google Scholar + Semantic Scholar + Connected Papers |
| Documents PDF | Google `filetype:pdf` + Bing `contains:pdf` |

-----

### Chapitre 20 — Google dorking et opérateurs avancés

#### 20.1 Le dorking comme art

Le **Google dorking** (ou Google hacking) est l'art de construire des requêtes complexes pour extraire des informations précises. Inventé dans les années 2000, il reste pertinent en 2026 malgré la dégradation des opérateurs.

Un bon dork :
- Cible un type de résultat spécifique.
- Élimine le bruit.
- Utilise les opérateurs combinés.
- Reste lisible et reproductible.

#### 20.2 Opérateurs Google de base

**site:** — Restreint à un domaine.
```
site:linkedin.com "Marc Delaunay"
site:.gov.fr "lanceur d'alerte"
```

**filetype:** — Type de fichier.
```
filetype:pdf "TechnoVert" 2024
filetype:xlsx "consultants" "honoraires"
```

**intitle:** — Mot dans le titre.
```
intitle:"index of" "backup"
intitle:"rapport annuel" 2024
```

**inurl:** — Mot dans l'URL.
```
inurl:rapport-annuel
inurl:wp-content
```

**intext:** — Mot dans le contenu (souvent redondant).

**ext:** — Extension de fichier (alternatif à `filetype:`).

**Guillemets `"..."`** — Recherche exacte.
```
"Marc Henri Delaunay"
```

**Parenthèses** — Groupements.
```
("TechnoVert" OR "Techno Vert") (DAF OR "directeur financier")
```

**`OR`** — Alternatives (capitales obligatoires).

**`-`** — Exclusion.
```
"Delaunay" -wikipedia -linkedin
```

**`*`** — Joker (résultats varient).

**`..`** — Plages numériques.
```
"chiffre d'affaires" 2020..2024
```

#### 20.3 Dorks emblématiques

**Recherche d'index ouverts.**
```
intitle:"index of" "parent directory"
intitle:"index of" filetype:log
intitle:"index of" "backup"
```

**Recherche de fichiers exposés.**
```
filetype:env "DB_PASSWORD"
filetype:sql "INSERT INTO users"
"index of" filetype:bak
```

**Recherche d'organisations.**
```
"TechnoVert" filetype:pdf 2024
site:bodacc.fr "TechnoVert"
"Marc Delaunay" "DAF" OR "directeur administratif"
```

**Recherche de personnes.**
```
"Marc Delaunay" "X-Ponts" OR "Polytechnique"
"Marc Delaunay" 1976 site:linkedin.com
intext:"marc.delaunay@" -site:technovert.fr
```

**Recherche de présence Github.**
```
site:github.com "delaunay" "technovert"
site:gitlab.com "config" "password"
```

**Recherche d'archives.**
```
site:archive.org "verites-technovert.com"
site:web.archive.org "technovert"
```

#### 20.4 Dorks Bing-spécifiques

**Bing** propose des opérateurs uniques.

**`contains:`** — Documents liés.
```
delta consulting contains:pdf
```

**`linkfromdomain:`** — Sites liés depuis un domaine.
```
linkfromdomain:technovert.fr -site:technovert.fr
```

**`ip:`** — Sites hébergés sur une IP.
```
ip:192.168.1.1
```

#### 20.5 Dorks pour autres moteurs

**Yandex.** Opérateurs similaires à Google, plus quelques spécifiques (`rhost:`, `domain:`).

**Baidu.** Opérateurs `site:`, `intitle:`, `filetype:` fonctionnent.

**DuckDuckGo.** Bang operators (`!g` pour Google, `!yt` YouTube, `!w` Wikipedia) très utiles.

#### 20.6 Limites modernes des dorks

En 2026, Google a **dégradé volontairement** plusieurs opérateurs.

**Limites constatées.**
- `+` supprimé depuis 2011.
- `link:` retiré en 2017.
- `cache:` largement dégradé / retiré.
- `intitle:` et `inurl:` parfois ignorés silencieusement.
- Résultats limités à ~300 même avec pagination.
- CAPTCHA fréquents pour requêtes complexes.
- Géo-personnalisation forte (deux utilisateurs voient des résultats différents).

**Compensation.**
- Utiliser plusieurs moteurs en parallèle.
- Préserver les snapshots de requêtes (Hunchly capture).
- Construire requêtes redondantes (chercher plusieurs formulations).

#### 20.7 Catalogue de dorks par objectif

Voir **Annexe B** pour le catalogue complet par objectif (personne, email, username, domaine, document, leak, réseau social).

#### 20.8 Recherche par opérateurs combinés : exemples MIRAGE

**Recherche financière publique.**
```
"TechnoVert" ("rapport annuel" OR "comptes consolidés") filetype:pdf 2022..2025
```

**Recherche Delaunay parcours.**
```
"Marc Delaunay" ("KPMG" OR "Deloitte" OR "Solucia") -site:linkedin.com
```

**Recherche faux compte coordonné.**
```
site:twitter.com "Antoine Berthier" ("escroc" OR "menteur" OR "manipulateur") since:2025-10
```

**Recherche structure offshore.**
```
"Delta Consulting" Malta filetype:pdf OR site:openml.gov.mt
```

**Recherche Berthier (lanceur d'alerte, pour contextualiser le narratif diffamatoire).**
```
"Antoine Berthier" "TechnoVert" OR "contrôleur de gestion" 
```

#### 20.9 Pièges classiques

- **Sur-spécification** : requête trop précise → 0 résultat. Élargir progressivement.
- **Sous-spécification** : requête trop large → millions de résultats. Resserrer.
- **Personnalisation non désactivée** : résultats biaisés par votre profil.
- **Oubli de variations** : « TechnoVert » mais aussi « Techno Vert », « technovert.fr », « TechnoVert SAS ».
- **Oubli des langues** : un dork en français ne ramène pas les résultats anglais correspondants.

#### 20.10 Bruit, personnalisation et signal

La principale difficulté du dorking en 2026 n'est plus l'efficacité technique mais la **qualité du signal**. Trop de résultats SEO commercial, trop de personnalisation, trop de spam de contenu généré par IA. La défense :
- Croiser plusieurs moteurs.
- Exclure les domaines pollueurs (`-site:pinterest.com -site:medium.com`).
- Privilégier les sources primaires (registres, archives, sites institutionnels).
- Utiliser Marginalia, Mojeek pour échapper au SEO.

-----

### Chapitre 21 — Moteurs spécialisés OSINT

#### 21.1 Au-delà des moteurs généralistes

Les moteurs généralistes indexent le web visible. Les **moteurs spécialisés OSINT** explorent des espaces que Google n'indexe pas : services Internet exposés, leaks et breaches, dépôts de code, archives spécifiques. Maîtriser ces outils est l'un des sauts qualitatifs majeurs de l'analyste OSINT.

#### 21.2 Shodan : le « moteur de l'Internet des choses »

**Shodan** (shodan.io) indexe les services Internet exposés (HTTP, SSH, FTP, RTSP, MQTT, etc.) en scannant systématiquement Internet.

**Cas d'usage OSINT.**
- Identifier l'infrastructure exposée d'une entité (serveurs, caméras, ICS).
- Recherche par bannière, technologie, version.
- Identification de devices compromis (vulnérabilités connues).
- Pivot infrastructure → entité propriétaire.

**Requêtes utiles.**
```
hostname:technovert.fr
ssl.cert.subject.cn:"technovert"
http.title:"TechnoVert"
port:22 country:FR org:"TechnoVert"
```

**Tarification.** Shodan a un freemium limité. La version Membership (annuelle) est nécessaire pour un usage professionnel.

#### 21.3 Censys : complémentaire

**Censys** (censys.io) joue un rôle similaire à Shodan mais avec une approche différente (scan plus exhaustif, focus sur les certificats TLS).

**Forces.**
- Recherche par certificat TLS (toutes les variations).
- Données historiques (vue dans le temps).
- Interface plus structurée pour les queries complexes.

**Combinaison Shodan + Censys.** Standard professionnel. Ils se complètent : ce que l'un manque, l'autre l'attrape souvent.

#### 21.4 FOFA et ZoomEye

**FOFA** (chinois) et **ZoomEye** (chinois) sont des équivalents Shodan d'origine chinoise. Indexation parfois différente (couvrent mieux certaines régions). Précaution OPSEC : services chinois, requêtes potentiellement loguées par autorités. À utiliser via VPN et compte d'investigation séparé.

#### 21.5 GreyNoise : filtrer le bruit Internet

**GreyNoise** (greynoise.io) catégorise le « bruit Internet » — les IPs qui scannent constamment le web. Utile pour distinguer scans massifs (bruit) versus scans ciblés (peut-être pertinent pour l'enquête).

**Cas d'usage.**
- Une IP suspecte est-elle juste du bruit ou cible-t-elle quelque chose ?
- Détecter des campagnes de scan dirigées contre une entité.

#### 21.6 Have I Been Pwned (HIBP)

**HIBP** (haveibeenpwned.com) est le moteur de référence pour les breaches publiques.

**Usage OSINT.**
- Tester si un email est dans une fuite (et lesquelles).
- API gratuite pour vérification simple.
- API payante (~$3/mois) pour usage professionnel.

**Limites.**
- Liste de breaches limitée à ce que Troy Hunt accepte (filtré, vérifié).
- Pas de mots de passe en clair (uniquement existence dans fuite).
- Pour breaches plus complètes, voir DeHashed, IntelX, Snusbase.

#### 21.7 Intelligence X

**Intelligence X** (intelx.io) est un moteur spécialisé dans les **deep web et leaks**.

**Capacités.**
- Index des breaches, pastes, dumps, archives Tor.
- Recherche par email, username, domaine, BTC address, IP, etc.
- Snapshots historiques (capture l'éphémère).
- API solide.

**Tarification.** Freemium très limité, professionnel à plusieurs centaines $/mois. Standard pour CTI / DFIR.

#### 21.8 PublicWWW et SearchCode

**PublicWWW** (publicwww.com) indexe le **code source** des pages web — utile pour trouver toutes les pages partageant un même tracker, une même API key exposée, un même framework custom.

**SearchCode** (searchcode.com) indexe le code dans les dépôts publics (GitHub, GitLab, Bitbucket, autres).

**Cas d'usage.**
- Identifier les sites utilisant un même tracker Google Analytics (peut révéler un opérateur commun).
- Trouver des credentials exposés dans des dépôts.
- Identifier les sites partageant une signature technique.

#### 21.9 GitHub search avancé

**GitHub** lui-même propose un moteur très puissant.

**Dorks GitHub.**
```
"technovert" "password"
"@technovert.fr" extension:env
"DB_PASSWORD" "delaunay"
filename:.env "technovert"
```

**Pour des leaks de secrets corporate.** Toujours à manier avec déontologie : signaler à l'organisation concernée, ne pas exploiter.

#### 21.10 Moteurs académiques

**Google Scholar.** Articles académiques. Pour investigation sur parcours universitaire.

**Semantic Scholar.** Index académique enrichi IA. Citations, papers liés.

**Connected Papers.** Visualisation des relations entre papers.

**HAL, theses.fr.** France spécifique pour thèses.

#### 21.11 Moteurs spécialisés divers

**Wayback Machine API** (web.archive.org). Pour rechercher dans les archives.

**Aleph (OCCRP).** Base journalistique de millions de documents publics.

**Pacer / RECAP** (US). Documents judiciaires américains.

**EDGAR** (SEC). Filings boursiers US.

**OpenSecrets** (US). Financement politique US.

#### 21.12 Synthèse — votre boîte à outils

| Besoin | Outil prioritaire | Alternative |
|---|---|---|
| Infrastructure exposée | Shodan | Censys, FOFA |
| Certificats TLS | Censys + crt.sh | Shodan |
| Breaches | HIBP | DeHashed, IntelX |
| Leaks deep web | Intelligence X | Snusbase |
| Code et secrets | GitHub search | PublicWWW, SearchCode |
| Académique | Google Scholar | Semantic Scholar |
| Documents OCCRP | Aleph |  |
| Archives web | Wayback Machine | archive.today |

-----

### Chapitre 22 — IA-search et moteurs conversationnels

#### 22.1 L'irruption des IA-search

Entre 2023 et 2026, une nouvelle génération de « moteurs conversationnels » a émergé : **Perplexity**, **Phind**, **You.com**, **Brave AI summaries**, et les fonctions search intégrées dans **ChatGPT**, **Claude**, **Gemini**. Ces outils combinent recherche web et synthèse LLM.

Pour l'analyste OSINT, ils sont à la fois utiles et dangereux. Utiles parce qu'ils permettent de naviguer rapidement dans un domaine inconnu, d'obtenir une synthèse, de formuler des questions complexes. Dangereux parce qu'ils hallucinent, citent mal, et créent une fausse impression de complétude.

#### 22.2 Perplexity

**Perplexity** (perplexity.ai) est le leader actuel des moteurs conversationnels.

**Avantages.**
- Synthèses avec citations sources (cliquables).
- Mode « Focus » (académique, Reddit, YouTube).
- Mode « Pro Search » plus profond.
- Suit l'actualité en continu.

**Limites.**
- Hallucinations résiduelles (citation correcte d'une affirmation incorrecte).
- Sources parfois faibles (Reddit, blogs SEO).
- Profondeur variable.
- Pas un substitut à la recherche directe.

#### 22.3 Phind

**Phind** (phind.com) est orienté développeurs (code, doc technique) mais utile pour OSINT technique.

**Cas d'usage OSINT.**
- Comprendre une technologie inconnue.
- Trouver de la documentation sur un outil.
- Synthèse d'articles techniques.

#### 22.4 You.com et Brave AI

**You.com** propose plusieurs modes (default, smart, research). Intégration multimodale (image, code).

**Brave AI Summaries** intègre des résumés AI dans les résultats Brave Search.

#### 22.5 ChatGPT, Claude, Gemini en mode search

Les grands LLMs proposent désormais des modes search intégrés.

**ChatGPT (OpenAI).** Browse with Bing intégré, mode search dédié.

**Claude (Anthropic).** Web search intégré dans claude.ai (selon plan).

**Gemini (Google).** Intégration Google Search native.

**Pour OSINT.**
- Utiles pour reformulation, synthèse, hypothèses de travail.
- **Jamais** comme source primaire.
- Vérifier chaque affirmation contre la source originale.

#### 22.6 Risque d'hallucination en contexte OSINT

L'hallucination est le risque central. Un LLM peut **inventer** :
- Une affirmation qu'aucune source ne soutient.
- Une citation d'une source qui n'existe pas.
- Une URL plausible mais inexistante.
- Un fait correctement attribué mais en réalité faux.
- Des chiffres précis mais fantaisistes.

**Pour un analyste OSINT, l'hallucination est catastrophique** : elle peut entraîner un rapport erroné, une action injuste, une compromission de crédibilité.

#### 22.7 Vérification systématique

Toute affirmation produite par un moteur conversationnel doit être **vérifiée contre la source primaire**.

**Protocole.**
1. Le moteur affirme « X selon source Y ».
2. Aller vérifier directement source Y.
3. La source Y contient-elle l'affirmation X ?
4. Si oui, la source Y est-elle fiable (cotation Admiralty) ?
5. Si non (= hallucination), discarder.
6. Si pas de source Y citée, discarder par défaut.

C'est lent. C'est la condition pour utiliser ces outils.

#### 22.8 Ne jamais citer un LLM comme source

**Règle absolue.** Un livrable OSINT **ne cite jamais** « selon ChatGPT », « d'après Perplexity ». La source citée est toujours la **source primaire** que le LLM a (peut-être) trouvée.

Cette règle évite les ridicules judiciaires et professionnels. Un rapport qui cite un LLM comme source est invalidé d'office.

#### 22.9 Usages légitimes de l'IA-search en OSINT

Malgré ces réserves, les IA-search ont des **usages utiles**.

**Reformulation.** Vous avez une intuition vague, l'IA aide à la formuler en questions précises.

**Cartographie d'un domaine inconnu.** Avant d'investiguer une industrie ou un sujet technique inconnu, l'IA fournit une vue d'ensemble (à vérifier mais utile pour s'orienter).

**Identification de sources.** L'IA suggère des sources que vous ne connaissiez pas. Vous allez ensuite directement à ces sources.

**Synthèse de corpus déjà connus.** Vous donnez à l'IA un corpus que vous avez vérifié, elle produit une synthèse (encore à relire).

**Traduction et transposition culturelle.** Comprendre des sources en langue ou contexte culturel inconnu.

#### 22.10 Protocole Retrieve-Store-Cite (anticipation Ch.63)

Le protocole **Retrieve-Store-Cite** (Ch.63 développe) opérationnalise l'usage de l'IA en OSINT.

1. **Retrieve.** L'IA récupère des éléments candidats.
2. **Store.** Vous stockez ces éléments avec leur source originale.
3. **Cite.** Dans le livrable, vous citez **la source originale**, pas l'IA.

Cette discipline rend l'IA utilisable sans compromettre la rigueur.

#### 22.11 Synthèse — usage 2026 des IA-search

| Usage | Recommandation |
|---|---|
| Question rapide hors enquête | OK |
| Cartographie domaine inconnu | OK, à vérifier |
| Reformulation de questions | OK |
| Suggestion de sources à consulter | OK, vérification ensuite |
| Source primaire dans un livrable | **JAMAIS** |
| Synthèse de corpus déjà vérifié | OK, relire |
| Action sur la base d'affirmation IA non vérifiée | **JAMAIS** |
| Vérification rapide d'un fait | À vérifier en source primaire |

> **Principe directeur.** L'IA-search est un raccourci, pas un oracle. Elle accélère votre recherche, elle ne se substitue pas à votre rigueur.

-----

### Chapitre 23 — Archivage et préservation web

#### 23.1 L'archivage anticipé comme stratégie

Le web est **éphémère**. Une page peut être modifiée, retirée, censurée à tout moment. Un compte peut être supprimé. Une vidéo peut être démonétisée et masquée. En 2026, avec la fermeture progressive des plateformes, l'éphémérité est devenue **un risque opérationnel majeur**.

L'**archivage anticipé** est devenu une stratégie défensive et offensive : capturer dès que vous voyez, ne pas attendre que la page soit citée dans le rapport. Une page non archivée à la date de consultation est une page que vous pouvez perdre.

#### 23.2 Wayback Machine (Internet Archive)

**Wayback Machine** (web.archive.org) est l'archive web la plus large du monde, opérée par Internet Archive (ONG).

**Usage.**
- **Consultation.** Voir les versions historiques d'une URL.
- **Sauvegarde manuelle.** Soumettre une URL pour archivage (`web.archive.org/save/[URL]`).
- **Sauvegarde via API.** Automatisable pour des batches.
- **CDX search.** Recherche sur les archives existantes (`web.archive.org/cdx/search/cdx`).

**Forces.**
- Gratuit, ouvert, large couverture.
- Historique parfois très profond (snapshots quotidiens des sites majeurs).
- Standard de fait pour citer des archives en investigation.

**Limites.**
- Pas tout est archivé (sites bloquant les crawlers, contenu derrière login).
- Snapshots irréguliers pour sites mineurs.
- Délais avant indexation.
- Risque de suppression sur demande (rare mais possible).

#### 23.3 archive.today

**archive.today** (ou archive.ph, archive.is) est complémentaire à Wayback.

**Forces.**
- Archive sur demande (snapshot immédiat).
- Capture meilleure du JavaScript-rendered content.
- Captures les pages Twitter/X mieux que Wayback.
- Pas affecté par les protections anti-crawler de certains sites.
- Snapshots persistants.

**Limites.**
- Pas de recherche full-text.
- Modèle économique opaque.
- Disponibilité variable.

**Combinaison.** Pour chaque archive critique : sauvegarder sur **Wayback Machine** ET **archive.today**. Redondance défensive.

#### 23.4 Conifer et Webrecorder

**Conifer** (conifer.rhizome.org) et **Webrecorder** offrent des solutions de capture web interactive : on enregistre une session de navigation complète (clics, scrolls, formulaires), pas juste une page.

**Cas d'usage OSINT.**
- Capturer une expérience utilisateur complète (formulaire interactif).
- Préserver une exploration de carte.
- Archiver une vidéo embarquée avec ses contrôles.

**Format.** WARC (Web ARChive), standard open archive.

#### 23.5 SingleFile : capture HTML complète

**SingleFile** (extension navigateur, gratuit) capture une page web complète dans un fichier HTML unique (HTML + CSS + images + scripts inlinés).

**Avantages.**
- 100 % local.
- Pas de dépendance à un service tiers.
- Hash directement calculable.
- Lisible hors-ligne par n'importe quel navigateur.

Indispensable pour les pages très sensibles ou éphémères que vous voulez préserver souverainement.

#### 23.6 Hunchly : la solution professionnelle

**Hunchly** est traité au Ch.15 pour son rôle de journal. Côté archivage, il capture **automatiquement chaque page consultée** pendant une session d'investigation, avec horodatage et hash. Génère un rapport complet exportable.

C'est la solution **professionnelle** de référence pour archivage couplé à investigation.

#### 23.7 FAW (Forensic Acquisition of Websites)

**FAW** est un outil professionnel forensique pour acquisition web. Plus lourd que Hunchly, orienté procédure judiciaire stricte (hash légaux, certificats horodatés). Utilisé en LEA et en expertise judiciaire.

#### 23.8 Captures vidéo

Pour les vidéos (YouTube, X, Telegram, TikTok, Twitch) :

**yt-dlp.** Successeur de youtube-dl. Multi-plateformes. Téléchargement direct, format original.

```bash
yt-dlp [URL]
yt-dlp --write-info-json [URL]   # avec métadonnées
yt-dlp -f bestvideo+bestaudio [URL]   # qualité max
yt-dlp --list-formats [URL]   # voir formats disponibles
```

**OBS** pour enregistrement live (streams Twitch, YouTube Live, X Spaces).

**Streamlink** pour téléchargement de streams.

**Combiné.** Téléchargement du média + capture de la page (Hunchly/SingleFile) + hash + métadonnées.

#### 23.9 Archivage Telegram

**Telegram** pose un défi spécifique : volume massif, contenu éphémère, restrictions API.

**Méthodes.**
- **TGStat / Telemetr.io** : statistiques de canaux publics.
- **Telegram Desktop + export** : pour canaux où on est membre.
- **Scripts Python (Telethon, Pyrogram)** : automatisation conforme aux CGU et limites API.
- **Telegago** : moteur de recherche Telegram (canaux publics).

**Captures.** Screenshots horodatés + hash + export JSON du canal si possible.

#### 23.10 Archivage Discord

**Discord** est encore plus restrictif. Pas d'API publique pour observation tiers, CGU strictes.

**Méthodes.**
- **DiscordChatExporter** (Tyrrrz, GitHub) : export des conversations dont vous êtes membre. Usage déontologique strict.
- Captures manuelles + horodatage + hash.
- Pour observation passive, accès limité à votre fenêtre membre.

#### 23.11 Archivage de livestreams et événements éphémères

Pour les événements en direct (X Spaces, Twitter Spaces, YouTube Live, Twitch streams) :

- **Enregistrement en temps réel.** OBS, Streamlink. Lancer dès que vous identifiez l'événement.
- **Multi-flux.** Si critique, deux machines redondantes.
- **Métadonnées.** Date, heure, intervenants apparents, hash du fichier final.

**Cas d'usage OSINT.** Un dirigeant qui parle sur X Spaces une seule fois et le retire ensuite. Une diffusion live d'événement controversé. Une intervention politique non rediffusée.

#### 23.12 Stratégie d'archivage par sensibilité

| Sensibilité du contenu | Stratégie d'archivage |
|---|---|
| Public stable | Wayback + lien dans journal |
| Public éphémère | Wayback + archive.today + capture locale |
| Critique pour enquête | Wayback + archive.today + Hunchly + SingleFile + hash |
| Judiciaire | Tout ci-dessus + horodatage qualifié + FAW si dispo |
| Vidéo importante | yt-dlp + capture page + hash + métadonnées EXIF |
| Live éphémère | OBS dual-stream + hash final |

#### 23.13 Outils en évolution rapide

L'écosystème change. En 2026, surveiller :
- L'évolution de Wayback Machine (financement, politique de retrait).
- Les nouvelles solutions de capture mobile.
- Les outils dédiés au capture des contenus AI-generated (provenance C2PA).
- Les outils d'archivage de **dark web** spécifiques (Onionland, OnionScan).

-----

### Chapitre 24 — Restrictions plateformes 2024-2026

#### 24.1 La grande fermeture

Entre 2022 et 2026, les grandes plateformes ont progressivement **fermé** l'accès libre à leurs données pour les chercheurs, journalistes et investigateurs OSINT. C'est l'une des transformations les plus importantes du métier.

Causes principales : (1) modèles économiques fondés sur l'accès payant aux données, (2) protection légale (RGPD, DSA), (3) compétition avec les LLMs (les plateformes craignent l'aspiration de leurs données pour entraînement IA), (4) durcissement vis-à-vis des outils tiers perçus comme parasites.

Conséquence : l'OSINT 2026 doit s'adapter à un paysage de plateformes hostiles ou semi-hostiles.

#### 24.2 X (Twitter) : la rupture la plus brutale

**X** (anciennement Twitter, racheté par Elon Musk en octobre 2022) est le cas d'école.

**Restrictions imposées 2023-2026.**
- API gratuite supprimée (mars 2023).
- API payante à partir de $100/mois (basic), $5000/mois (pro), entreprise sur devis.
- Limitation drastique des résultats par requête.
- Suppression de la consultation déconnectée pour de nombreux contenus.
- Dégradation puis fermeture de Nitter (alternative non-officielle).
- Removal de l'export TweetDeck classique.

**Impact OSINT.**
- Twint, snscrape (anciennement utilisés) : largement inopérants.
- TweetBeaver, Tweetdeck : dégradés.
- Recherche historique très limitée sans API payante.
- Beaucoup d'investigateurs ont basculé vers une combinaison : compte d'investigation actif + archivage anticipé + outils payants ciblés.

**Stratégies 2026.**
- Compte d'investigation maturé pour consultation directe.
- Archivage anticipé systématique (Wayback + archive.today).
- API payante pour besoins ponctuels (basic à $100/mois supportable).
- Outils tiers payants : Brandwatch, Talkwalker, Meltwater pour cas pro.
- Recherche via Bing/Google avec `site:twitter.com` (couverture partielle mais utile).

#### 24.3 Meta (Facebook, Instagram, Threads)

**Meta** a verrouillé son écosystème.

**Restrictions.**
- Graph API restreinte aux applications agréées.
- CrowdTangle (outil journalistique vital) fermé en août 2024 (rapatrié partiellement en Meta Content Library).
- Recherche par mot-clé sur Facebook quasi-impossible sans compte connecté.
- Stories Instagram : disparition après 24h sans archivage.
- Threads : API non publique au lancement.

**Impact OSINT.**
- Meta Content Library (depuis 2024) remplace partiellement CrowdTangle mais avec accès restreint (chercheurs agréés DSA art. 40).
- Outils tiers (Sowsearch, etc.) : largement obsolètes.
- Investigation passive uniquement, via compte d'investigation.

**Stratégies 2026.**
- Comptes Facebook/Instagram d'investigation maturés.
- Demande d'accès Meta Content Library si statut chercheur DSA.
- Archivage immédiat de tout contenu d'intérêt (stories surtout).
- Bing image search sur Instagram (couverture partielle).

#### 24.4 LinkedIn : forteresse

**LinkedIn** (Microsoft) est probablement la plateforme la plus restrictive.

**Restrictions.**
- Pas d'API publique pour observation tiers (uniquement applications Sales Navigator agréées).
- Sales Navigator coûteux ($79-150/mois).
- Limite stricte aux profils consultables par compte.
- Détection agressive des comptes d'investigation (suspension fréquente).
- CGU explicitement contre le scraping.

**Jurisprudence US.** L'affaire **hiQ Labs v. LinkedIn** (2022 SCOTUS) a établi que le scraping de données **publiques** ne viole pas le CFAA — mais reste contractuellement risqué (CGU). Pas de précédent équivalent UE.

**Stratégies 2026.**
- Comptes d'investigation matures (3-6 mois min).
- Sales Navigator pour les cabinets avec budget.
- Phantombuster (outil tiers payant) pour automatisation modérée — risque suspension.
- Combinaison consultation passive + Google `site:linkedin.com/in/` pour recherche externe.

#### 24.5 Reddit : la fermeture API 2023

**Reddit** a fermé son API gratuite en juin 2023, après une crise majeure (suppressions d'outils tiers populaires comme Apollo).

**Restrictions.**
- API payante à partir de $0.24 / 1000 calls (élevé).
- Apollo, RIF, BaconReader : fermés.
- Pushshift (archive Reddit historique vitale) : fermé pour public.
- Camas (UI Pushshift) : non maintenu.

**Stratégies 2026.**
- API officielle payante pour usage pro.
- undelete.pullpush (mirror partiel Pushshift) : utile mais limité.
- Recherche Google `site:reddit.com` pour découverte.
- Archivage manuel de threads critiques.

#### 24.6 Google : dégradation progressive

**Google** lui-même a dégradé son service de recherche.

**Restrictions.**
- Opérateurs avancés (cf. Ch.20) : silencieusement ignorés ou dégradés.
- Cache : largement retiré.
- Image search Reverse : moins puissant que Yandex.
- Personnalisation forte (deux utilisateurs voient des résultats différents).
- CAPTCHA fréquent pour requêtes complexes.

**Stratégies.**
- Multi-moteurs systématique (Bing, Yandex, Brave, Mojeek).
- Tools alternatifs (SearXNG instances).
- API Google Custom Search pour automatisation (payante, $5/1000 queries).

#### 24.7 TikTok : opacité

**TikTok** propose peu d'accès officiel.

**Restrictions.**
- TikTok Research API (depuis 2023) : restreinte aux chercheurs académiques agréés EU/US.
- Pas de scraping autorisé.
- Détection forte des comptes anormaux.

**Stratégies 2026.**
- Comptes d'investigation.
- Outils tiers payants (Brandwatch, Talkwalker — équivalents).
- Recherche directe via tags et profils.

#### 24.8 Telegram : encore relativement ouvert

**Telegram** reste relativement accessible mais la dynamique change.

**Évolution post-Durov 2024.** Arrestation de Pavel Durov en France (août 2024) a déclenché des évolutions : coopération avec autorités françaises et autres LEA, modération renforcée, partage d'IP pour requêtes pénales graves.

**Restrictions.**
- API utilisable mais limites rate.
- Channels privés non accessibles sans invitation.
- Bots Telegram pour interaction (avec limites).

**Stratégies 2026.**
- API Telethon / Pyrogram pour automatisation conforme.
- Compte d'investigation pour observation.
- Outils dédiés (TGStat, Telemetr.io, Lyzem).

#### 24.9 GitHub, GitLab : encore ouverts

**GitHub** et **GitLab** restent globalement accessibles pour recherche publique.

**Restrictions.**
- Rate limits sur API.
- Detection scraping agressif.
- Compte requis pour la plupart des features avancées.

**Bonne pratique.** Token API personnel pour rate limits raisonnables.

#### 24.10 Synthèse — niveau de difficulté par plateforme

| Plateforme | Difficulté 2026 | Solution principale |
|---|---|---|
| X (Twitter) | Très haute | API payante + archivage + compte invest |
| Facebook / Instagram | Très haute | Meta Content Library (si chercheur) + compte invest |
| LinkedIn | Très haute | Sales Navigator + compte invest |
| Reddit | Haute | API payante + Google site: |
| Google search | Moyenne | Multi-moteurs |
| TikTok | Très haute | Compte invest + outils payants |
| Telegram | Moyenne | API Telethon + compte invest |
| GitHub / GitLab | Faible | Token API |
| YouTube | Moyenne | yt-dlp + API officielle |
| Bluesky | Faible | API ouverte |
| Mastodon | Faible | Federated, ouvert |

#### 24.11 Tendance à anticiper : l'IA accélère la fermeture

Les LLMs scrapent massivement le web pour entraînement. Les plateformes réagissent en se fermant (Reddit cite explicitement la pression IA dans sa décision API 2023). La tendance est à la **fermeture continue**.

Pour l'analyste OSINT, c'est une réalité structurante : les outils gratuits d'aujourd'hui peuvent disparaître demain. La discipline d'archivage anticipé devient vitale.

-----

### Chapitre 25 — Adaptation méthodologique aux restrictions

#### 25.1 Survivre dans un écosystème hostile

Le chapitre précédent a décrit le paysage. Celui-ci propose des **stratégies opérationnelles** pour continuer à conduire des enquêtes OSINT efficaces malgré les restrictions.

Cinq stratégies se combinent : archivage anticipé, recherche multi-moteurs, sources secondaires, monitoring de disparition, automatisation conforme.

#### 25.2 Stratégie 1 — Archivage anticipé systématique

Le **réflexe d'archivage en début d'enquête** est devenu fondamental.

**Pratique.**
- À l'identification de toute entité d'intérêt, archiver immédiatement (Wayback + archive.today) les pages clés.
- Captures vidéo en yt-dlp.
- Storage local horodaté et hashé.
- Ne pas attendre la phase de rédaction.

**Investissement.** Cela prend 10-15 % de temps en plus mais sauve l'enquête. Une page perdue qu'on aurait pu archiver est un échec professionnel évitable.

#### 25.3 Stratégie 2 — Recherche multi-moteurs

Voir Ch.19 et Ch.20. La règle : **jamais un seul moteur**.

**Combinaison standard.**
- Google + Bing pour large couverture.
- Yandex pour reverse image et russophone.
- Brave/Mojeek pour échapper au SEO commercial.
- Marginalia pour web non-commercial.
- Moteur local pour juridiction concernée (Naver, Baidu, Yahoo Japan).

**Pratique.** Construire une liste de moteurs par investigation, exécuter les requêtes sur chacun, comparer les résultats.

#### 25.4 Stratégie 3 — Sources secondaires et leur cartographie

Quand une source primaire est inaccessible, mobiliser les **sources secondaires** : ce qui a été extrait, cité, republié, archivé ailleurs.

**Exemples.**
- Un tweet supprimé peut survivre dans des articles de presse qui l'ont cité.
- Un post Facebook restreint peut être visible dans une capture journalistique.
- Une page LinkedIn invisible peut apparaître dans le cache Google (parfois).
- Un communiqué retiré peut être archivé sur Wayback.

**Cartographie.** Pour chaque entité, lister non seulement les sources primaires mais aussi les sources secondaires probables (presse, blogs spécialisés, archives, fact-checkers).

#### 25.5 Stratégie 4 — Monitoring de disparition

Suivre activement la **disparition** d'éléments importants.

**Outils.**
- **Visualping** : alertes sur changements de pages.
- **Distill** : monitoring de changements web.
- **ChangeTower** : alertes sur disparition.

**Pratique pour MIRAGE.**
- Monitoring des domaines suspects (`verites-technovert.com`, `info-finance-eu.com`).
- Alertes sur changement de propriété WHOIS.
- Monitoring des comptes coordonnés (suspensions, rebrandings).

Le monitoring permet de réagir : capturer juste avant disparition, identifier le moment précis de la modification (signal de l'opérateur réagissant).

#### 25.6 Stratégie 5 — Comptes d'investigation et accès direct

Pour les plateformes verrouillées (LinkedIn, Meta, X), l'**accès direct via compte d'investigation** mature est devenu la voie principale.

**Pratique.**
- Maintenir un parc d'avatars matures (Ch.11).
- Cloisonner par juridiction et par plateforme.
- Renouveler régulièrement pour éviter brûlage.
- Documenter en journal d'enquête la provenance de chaque capture.

#### 25.7 Stratégie 6 — APIs payantes ciblées

Pour les besoins critiques, accepter le coût des APIs payantes.

**Calcul ROI.**
- Une enquête à 30 k€ de budget peut supporter $500-2000 d'APIs (HIBP Pro, Shodan, X API Basic, Intelligence X).
- Une enquête flash à 3 k€ doit s'en passer.

**Standard pro 2026.** Hunter, DeHashed, Shodan, IntelX, Pappers, OpenSanctions, HIBP. Budget annuel typique cabinet : 5-15 k€.

#### 25.8 Stratégie 7 — Scraping résilient et automatisation

Pour les besoins de volume, le scraping reste possible mais demande robustesse.

**Outils.**
- **Playwright** (Microsoft) : automatisation navigateur moderne, gestion JavaScript.
- **Selenium** : alternative classique.
- **Scrapy** : framework Python pour scraping structuré.
- **Splash / Browserless** : services managés.

**Anti-anti-scraping.**
- Rotation de User-Agents.
- Proxies résidentiels (BrightData, Smartproxy) : coûteux mais efficaces.
- Rate limiting auto-imposé (humaniser le comportement).
- Cloudscraper / FlareSolverr pour Cloudflare.
- CAPTCHA solvers (2Captcha, anti-captcha) — usage déontologique strict.

**Précaution juridique.** Le scraping massif peut violer les CGU (responsabilité contractuelle) voire entrer dans les frottements pénaux (selon juridiction). Toujours :
- Respecter robots.txt.
- Limiter le rate.
- Pas de charge sur serveur (DoS involontaire).
- Conserver la traçabilité.
- Préférer APIs officielles si disponibles.

#### 25.9 Stratégie 8 — Documenter les lacunes

Quand une source devrait exister mais est inaccessible, **documenter la lacune** dans le rapport.

**Formulation.**
> « Le profil LinkedIn de M. Delaunay a été consulté le 20 mai 2026 (capture Hunchly référencée). Le contenu publié sur X par les comptes coordonnés `@xyz1` à `@xyz8` n'a pas pu être collecté de manière exhaustive en raison des restrictions de l'API X (mars 2023+). Une couverture partielle a été obtenue via archive.today (références jointes) et capture manuelle. Le compte `@xyz3` a été suspendu le 12 mai 2026, suite à un signalement non identifié. »

Cette honnêteté sur les lacunes est un signal de professionnalisme. Le commanditaire comprend ce qui a été fait, ce qui n'a pas pu l'être, et pourquoi.

#### 25.10 Stratégie 9 — Cycles d'investigation adaptés

Les enquêtes longues (3+ mois) doivent intégrer la **dégradation continue** de l'accès.

**Pratique.**
- Re-collecte périodique des éléments critiques (mensuelle).
- Vérification de la persistance des archives.
- Adaptation du plan si une source-clé devient inaccessible.

#### 25.11 Stratégie 10 — Anticiper les évolutions

L'analyste OSINT 2026 fait de la **veille outils** active.

**Routines.**
- Newsletters spécialisées (Bellingcat, OSINT-FR, OSINT Curious).
- Tests réguliers des outils du parc (encore fonctionnels ?).
- Documentation des outils alternatifs.
- Backup de méthodologies (si X disparaît, comment investiguer Y ?).

#### 25.12 Synthèse — l'analyste 2026 résilient

| Restriction subie | Réponse |
|---|---|
| API plateforme fermée | Archivage anticipé + compte invest + API payante si critique |
| Outil tiers disparu | Alternative cartographiée, ou méthode manuelle |
| Plateforme verrouillée | Compte d'investigation mature |
| Source-clé indisponible | Sources secondaires + documentation lacune |
| Évolution constante | Veille outils + tests réguliers |

> **Principe directeur.** L'analyste OSINT 2026 n'est pas celui qui maîtrise les outils du moment. C'est celui qui maîtrise une **méthode** qui survit aux outils.

-----
