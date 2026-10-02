---
title: 'Chapitre 26 — Social engineering et IA : la révolution en cours'
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie VI — Dimensions avancées
  - index.md
---

## 26.1 Le phishing AI-powered

Les LLM (Large Language Models) transforment le phishing de deux manières fondamentales. Premièrement, la personnalisation à l'échelle : un LLM peut générer des centaines d'emails de spear-phishing, chacun personnalisé à partir du profil OSINT de la cible (poste, entreprise, intérêts, publications récentes), dans n'importe quelle langue, avec une qualité linguistique indistinguable d'un email humain. La barrière d'entrée qui protégeait les cibles francophones (les phishings en mauvais français étaient faciles à détecter) a disparu. Deuxièmement, l'adaptation culturelle : le LLM adapte le registre, le ton et les conventions de communication au contexte culturel de la cible — un email de phishing destiné à un cadre allemand ne ressemblera pas à celui destiné à un ingénieur japonais.

Le rapport Unit 42 2025 confirme cette tendance : dans plusieurs investigations, les acteurs de la menace ont utilisé l'IA générative pour créer des leurres hautement personnalisés à partir d'informations publiques, avec un niveau de ton et de timing qui nécessitait auparavant un opérateur humain qualifié.

**Implications pour la défense** : les marqueurs linguistiques de phishing (fautes, registre inapproprié, formulations inhabituelles) ne sont plus des indicateurs fiables. La défense doit se reporter sur les indicateurs structurels (domaine d'expéditeur, headers, comportement de l'email) et les processus de vérification (callback, double validation).

## 26.2 Le vishing deepfake

Le clonage vocal en temps réel atteint en 2025 un niveau de maturité opérationnelle. Les plateformes comme ElevenLabs ou les modèles open source (XTTS, Bark) permettent de cloner une voix à partir d'échantillons audio courts (30 secondes à quelques minutes suffisent pour un clone de qualité acceptable). L'intégration en temps réel dans un appel téléphonique est techniquement possible avec une latence de quelques centaines de millisecondes — souvent indétectable sur un réseau téléphonique standard.

Les cas d'utilisation offensifs documentés incluent : fraude au président par deepfake vocal (l'attaquant clone la voix du DG à partir d'interviews publiques et appelle le DAF), confirmation téléphonique pour renforcer un BEC email (le « DG » rappelle pour confirmer son email de demande de virement), et vishing de helpdesk avec la voix d'un employé légitime.

**Détection** : les détecteurs de deepfake vocal sont en cours de développement mais restent peu fiables en conditions réelles (compression téléphonique, bruit ambiant, diversité des technologies de synthèse). La défense la plus efficace reste procédurale : pour toute demande sensible par téléphone, vérification out-of-band obligatoire (callback sur un autre canal, validation en personne, code de vérification préétabli).

## 26.3 La vidéo deepfake en temps réel

La visioconférence deepfake en temps réel a franchi le seuil de l'opérationnel. Le cas de Hong Kong (début 2024) — 25 millions de dollars volés via une visioconférence où plusieurs participants étaient des deepfakes — est le cas le plus médiatisé, mais d'autres cas moins spectaculaires ont été rapportés par des cabinets de réponse à incident.

En 2025, la génération vidéo deepfake en temps réel est accessible via des plateformes commerciales et des outils open source. La qualité est variable mais suffisante pour une visioconférence de résolution standard, en particulier si l'attaquant simule une connexion internet de mauvaise qualité (réduction de la résolution et du framerate, ce qui masque les artefacts).

**Défense** : demander à l'interlocuteur un geste imprévu (tourner la tête, montrer ses mains, placer un objet devant le visage) peut révéler les artefacts des deepfakes actuels — mais cette parade deviendra obsolète à mesure que la technologie progresse. La vérification d'identité multi-facteur (question de sécurité, code préétabli, confirmation par un second canal) reste la défense la plus robuste.

## 26.4 Les chatbots de social engineering

L'IA agentic appliquée au social engineering représente la prochaine frontière. Des agents conversationnels autonomes, capables de maintenir des conversations cohérentes sur des jours ou des semaines, de s'adapter au style de leur interlocuteur, de gérer les objections et de progresser méthodiquement vers un objectif (collecte d'identifiants, élicitation d'information, construction d'une relation de confiance), permettent le passage à l'échelle de techniques qui étaient auparavant limitées par la disponibilité d'opérateurs humains qualifiés.

Le rapport Unit 42 2025 identifie l'IA agentic comme une couche émergente dans le paysage des menaces, avec des systèmes capables d'exécuter de manière autonome des tâches en plusieurs étapes avec un minimum d'intervention humaine. Bien que l'adoption reste limitée à ce jour, les cas observés incluent la reconnaissance multi-plateforme automatisée et la distribution de messages coordonnée.

Les implications sont considérables pour les romance scams (un seul opérateur peut gérer des centaines de « relations » simultanées via des chatbots IA), pour l'élicitation (des agents conversationnels capables de mener des conversations d'élicitation structurées en salon professionnel virtuel), et pour le phishing conversationnel (des agents qui répondent aux questions de la cible et adaptent leur pretexte en temps réel).

## 26.5 La course aux armements

La défense face à la menace IA s'organise autour de trois axes : la détection (analyse comportementale des communications, détection d'anomalies dans le style d'écriture, détecteurs de deepfake audio et vidéo — tous avec des taux de faux positifs significatifs en 2025), les processus (vérification out-of-band, double validation, codes de confirmation préétablis — les défenses procédurales sont agnostiques à la technologie utilisée par l'attaquant), et la sensibilisation (former les employés à la réalité de la menace deepfake et IA, sans verser dans l'alarmisme — l'objectif est la vigilance, pas la paranoïa).

L'enjeu stratégique est que l'IA avantage structurellement l'attaquant : l'attaquant n'a besoin de réussir qu'une fois, tandis que le défenseur doit réussir à chaque fois. L'IA permet à l'attaquant de multiplier les tentatives avec une qualité constante et un coût marginal décroissant. La seule réponse durable est de construire des processus qui fonctionnent même quand la manipulation est parfaite — c'est-à-dire des processus qui ne reposent pas sur la capacité d'un individu isolé à détecter une tromperie.

---
