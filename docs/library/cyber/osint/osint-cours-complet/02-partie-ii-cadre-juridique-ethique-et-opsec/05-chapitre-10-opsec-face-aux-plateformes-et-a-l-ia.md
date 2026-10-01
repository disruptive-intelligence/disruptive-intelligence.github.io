---
title: Chapitre 10 — OPSEC face aux plateformes et à l'IA
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE II — Cadre juridique, éthique et OPSEC
  - index.md
---

## 10.1 Pourquoi un chapitre spécifique en 2026

L'OPSEC technique du chapitre précédent (VM, VPN, Tor, chiffrement) reste nécessaire mais n'est plus suffisante. En 2026, deux ruptures redéfinissent ce qu'observer en ligne signifie : les **plateformes infusées d'IA** disposent de capacités d'inférence comportementale qui dépassent largement le fingerprinting technique, et les **outils OSINT que nous utilisons** (LLMs commerciaux, agents, SaaS) constituent eux-mêmes un vecteur de fuite d'intention. L'analyste qui maîtrise l'OPSEC classique mais ignore ces deux dimensions opère avec un faux sentiment de sécurité.

## 10.2 Empreinte comportementale au-delà du fingerprinting

Le fingerprinting technique (canvas, fonts, GPU, audio) identifie un navigateur. L'**empreinte comportementale** identifie une personne. Elle s'appuie sur des signaux que la plupart des outils OPSEC ne couvrent pas.

**Signaux comportementaux.**

- **Cadence de navigation** : vitesse de lecture, temps moyen par page, schémas de défilement.
- **Fuseau horaire d'activité** : heures de connexion, jours de la semaine.
- **Lexique de recherche** : choix de mots-clés, langue maternelle, niveau de spécialisation.
- **Patterns de pivots** : un investigateur navigue de façon caractéristique (recherche entité → registre → réseau social → archive).
- **Frappe clavier** : timing entre frappes (keystroke dynamics), reconstruction possible.
- **Mouvement souris** : trajectoires, micro-pauses, hover patterns.
- **Pile applicative** : combinaison de plugins, paramètres, langue système.

Une plateforme grand public ne réunit pas tous ces signaux par défaut. Une plateforme commerciale OSINT, un site spécialisé, un outil SaaS peuvent en collecter beaucoup. Et un acteur étatique disposant d'une intercept réseau peut reconstituer une grande partie. La menace n'est pas hypothétique : les services de renseignement étrangers traquent activement les analystes OSINT alliés selon plusieurs avertissements publics récents (avertissement du chef de l'ASIO australienne Mike Burgess en 2024-2025 sur la collecte étrangère ciblant le personnel de défense via les sources ouvertes et les services d'IA).

**Contre-mesures.**

- Varier sa cadence (ne pas être identifiable à un schéma temporel).
- Ne pas utiliser les mêmes patterns de navigation entre identités.
- Si la menace est élevée, automatiser via outils (Playwright, requêtes API) qui produisent une signature neutre — au prix d'une perte de finesse.

## 10.3 Fuite d'intention via les outils d'investigation

Les outils OSINT modernes communiquent avec leurs serveurs. Chaque requête révèle ce que vous cherchez.

**Vecteurs typiques.**

- **APIs OSINT commerciales** (Shodan, DeHashed, IntelX, Hunter) : le fournisseur sait ce que vous cherchez, par horodatage et IP. Logs conservés.
- **LLMs commerciaux** (ChatGPT, Claude, Gemini) : le contenu de vos prompts est conservé selon les conditions du fournisseur. Vos prompts d'investigation révèlent vos cibles, vos hypothèses, votre méthode.
- **Outils SaaS OSINT** (Maltego cloud, Hunchly cloud, plateformes commerciales) : centralisation des données d'enquête chez le fournisseur.
- **Reverse image cloud** : votre image cible est envoyée au serveur de recherche, indexée potentiellement.
- **Outils de géolocalisation IA** (GeoSpy, GeoSeer) : votre image cible est envoyée et conservée.

**Le risque réel.** Une compromission, une réquisition judiciaire, une faille, ou simplement un employé indiscret du fournisseur peut exposer l'ensemble de vos investigations. Pour des cibles étatiques avec capacités SIGINT, l'observation directe du trafic est possible.

## 10.4 Prompts vers LLMs : un sujet sous-estimé

Les LLMs commerciaux sont devenus des outils de recherche au quotidien. Leur utilisation dans un cadre OSINT mérite une attention spécifique.

**Risques.**

- **Conservation des prompts** : OpenAI, Anthropic, Google conservent les prompts (durées variables, politiques évoluant). En cas de réquisition judiciaire dans le pays du fournisseur, ces données peuvent être accessibles.
- **Apprentissage potentiel** : selon les politiques (variables et évolutives), certaines plateformes utilisent les prompts pour entraîner les modèles, ce qui peut faire ressurgir des éléments d'enquête dans des réponses ultérieures.
- **Profilage du compte** : le fournisseur peut profiler votre usage et inférer votre activité professionnelle.
- **Erreurs de saisie** : copier-coller d'un dossier contenant des données sensibles, fuite involontaire.

**Bonnes pratiques.**

- **Anonymiser les prompts** : ne pas inclure de noms réels, d'identifiants, de données personnelles si évitable. Utiliser des placeholders (« la cible », « l'individu A »).
- **Compte d'investigation dédié** : pas le compte personnel professionnel, pas le compte client.
- **Privilégier les modèles avec opt-out** : OpenAI Enterprise, Anthropic Claude avec opt-out, Mistral hébergé en UE.
- **LLMs locaux** pour les sujets sensibles (Ch.65) : Ollama, LM Studio, vLLM auto-hébergé.
- **Cloisonner les contextes** : ne pas mélanger plusieurs investigations dans la même session.

## 10.5 Graphes de comportement et inférence des plateformes

Les grandes plateformes (Meta, Google, LinkedIn) construisent en interne des **graphes de comportement** qui peuvent corréler des comptes apparemment distincts.

**Signaux corrélatifs.**

- IP partagée (même VPN, même bureau).
- Empreinte navigateur similaire.
- Plages horaires identiques.
- Contacts communs (LinkedIn « personnes que vous pourriez connaître » est une fuite OPSEC majeure : il révèle les contacts implicites entre vos comptes).
- Géolocalisation téléphonique (si app activée).
- Carte de crédit, méthode de paiement.
- Adresse mail de récupération.

**Implication.** Vos comptes d'investigation peuvent être liés entre eux par la plateforme, et liés à votre identité personnelle, même sans erreur explicite de votre part. La défense est de **séparer physiquement** : IP différente, navigateur différent, téléphone différent, fenêtre temporelle différente.

## 10.6 Risque spécifique des agents autonomes

L'utilisation d'agents autonomes (Ch.67) en OSINT 2026 introduit un risque OPSEC nouveau.

**L'agent est une projection de l'investigateur.** Son schéma de comportement, ses pivots, ses choix de sources peuvent former une signature identifiable par les plateformes adverses. Un agent qui requête Shodan, puis Censys, puis crt.sh dans la même séquence pour un même domaine porte une signature distinctive.

**Risques spécifiques.**

- Agents qui interagissent avec des plateformes adverses (réponses qui peuvent influencer l'agent — *prompt injection* en environnement adversariale).
- Agents qui consultent un dump et le téléchargent inadvertamment (exposition pénale).
- Agents qui requêtent des API au-delà des CGU.
- Agents qui exposent leurs prompts en logs.

**Mesures.**

- Audit des agents : qui appelle quoi, quand, avec quels paramètres.
- Validation humaine systématique avant action sensible.
- Logs locaux des actions d'agents (pas dans le cloud).
- Mode dégradé en environnement adverse (humain au volant).

## 10.7 Détection de l'investigation par la cible

Une cible compétente peut détecter qu'elle est investiguée.

**Signaux côté cible.**

- **Recherches Google** : un dirigeant qui surveille « son nom » avec Google Alerts voit les nouvelles indexations.
- **Visites LinkedIn** : LinkedIn notifie qui consulte un profil (sauf mode privé, qui implique une perte de fonctionnalité d'investigation).
- **Notifications Twitter/X** : les retweets, likes, mentions remontent.
- **Audit des connexions** : les comptes consultés via une connexion suspecte sont signalés.
- **Honeypots** : la cible elle-même peut déposer des fichiers piégés (canary tokens) ou des liens piégés.

**Contre-mesures.**

- Mode privé LinkedIn (ou compte premium pour le voir).
- Pas d'interaction (pas de like, pas de retweet, pas de réponse).
- Connexion via VPN constante.
- Pas de téléchargement de fichiers d'origine suspecte sans isolation.
- Vigilance sur les liens cliqués dans les emails ou messages.

## 10.8 Counter-OSINT : la cible se défend

Les cibles aguerries pratiquent du **counter-OSINT** pour détecter et tromper les investigations.

**Méthodes typiques.**

- **Honeypot social** : profil dormant qui attire les curieux et les identifie.
- **Désinformation contrôlée** : informations fausses semées pour identifier les fuites.
- **Monitoring des consultations** : alertes sur les accès à leur profil, leurs documents partagés.
- **Identités secondaires** : compte public propre, activité réelle ailleurs.
- **Faux indices** : fausses pistes plantées pour égarer les enquêteurs.

**Implication.** L'analyste OSINT doit considérer que ses propres observations peuvent être manipulées. C'est l'objet du raisonnement adversaire (Ch.81).

## 10.9 Knowledge graphs locaux comme protection

Conserver l'enquête **localement** plutôt que dans un SaaS cloud limite la surface d'exposition. Le knowledge graph local (Ch.66) est l'illustration : graphe d'entités et de faits stocké chez l'investigateur, sans synchronisation cloud.

**Bénéfices OPSEC.**

- Pas de fuite d'intent vers un fournisseur tiers.
- Pas d'historique d'enquête centralisé hors de votre contrôle.
- Souveraineté complète sur les données.
- Possibilité de chiffrer entièrement.

**Coûts.**

- Pas de partage facilité avec une équipe distribuée (à compenser par chiffrement E2E).
- Pas de hosted intelligence (LLMs locaux moins puissants que les cloud).
- Maintenance technique.

Pour les sujets de haute sensibilité, le local est la règle.

## 10.10 Synthèse — boussole OPSEC 2026

| Vecteur de fuite | Mesure |
|---|---|
| Fingerprinting navigateur | Profil minimaliste, extensions standard, test fingerprint |
| Logs APIs OSINT commerciales | Compte d'investigation, anonymisation requêtes |
| Prompts LLMs cloud | LLMs locaux pour sensibles, anonymisation, opt-out |
| Graphes corrélatifs plateformes | Séparation IP, téléphone, mail, contacts |
| Agents autonomes | Audit, validation humaine, logs locaux |
| Détection par la cible | Mode privé, pas d'interaction, VPN constant |
| Counter-OSINT cible | Raisonnement adversaire, croisement sources |
| Centralisation cloud | Knowledge graph local pour sensibles |

> **Principe directeur 2026.** Plus votre boîte à outils OSINT est puissante, plus elle est observable. La maîtrise consiste à choisir consciemment quel outil pour quel niveau de sensibilité — pas à utiliser l'outil le plus puissant par défaut.

-----
