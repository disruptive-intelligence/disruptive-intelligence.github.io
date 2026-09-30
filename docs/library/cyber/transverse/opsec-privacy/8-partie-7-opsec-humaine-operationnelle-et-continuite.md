---
title: Partie 7 — OPSEC humaine, opérationnelle et continuité
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 8
chapters: 8
---

> **Objectif** : ce qui reste quand la technique est en place. Les attaques modernes contournent rarement la crypto — elles contournent l’humain, les routines, les frontières, les chaînes d’approvisionnement, les angles morts juridiques. Cette partie traite ce que les outils ne couvrent pas.

-----

### Chapitre 33 — Social engineering, phishing ciblé et spyware mercenaire

> **Niveau de posture (cf. Ch 2.6)** : la vigilance phishing concerne **tous les niveaux** (le phishing est l’attaque la plus statistiquement probable, indépendamment du profil). Lockdown Mode iOS, GrapheneOS et reboot quotidien relèvent du **Niveau 2** quand un indicateur de ciblage existe (publication sensible, contexte politique, threat notification reçue). MVT et iVerify systématiques, audit forensique périodique, plan de réponse spyware = **Niveau 3** réservé aux cibles documentées (journalistes investigation actuelle, opposants politiques, défenseurs droits humains exposés).

> **Note critique** : ne pas se dimensionner au Niveau 3 par fascination ou anxiété. Recevoir une vraie *Threat Notification* d’Apple, Google ou Meta est rare et conservateur. Les notifications de ce type sont envoyées à des cibles confirmées. Si tu n’en as jamais reçu et que ton profil ne correspond pas aux cibles documentées par Citizen Lab et Amnesty Security Lab, ton temps est mieux investi sur N1 et N2.

#### 33.1 Pourquoi l’humain reste le maillon faible

La cryptographie moderne tient. Les protocoles aussi. Ce qui se casse, c’est l’humain : il clique sur le lien, il fait confiance à la voix au téléphone, il branche la clé USB trouvée au sol, il déverrouille son téléphone parce qu’il a peur de manquer un appel important. Les attaquants sérieux investissent dans l’ingénierie sociale parce qu’elle est *plus rentable* que les exploits techniques.

#### 33.2 Phishing : taxonomie

- **Phishing de masse** : email générique envoyé à des millions. Faible taux de succès individuel mais volume.
- **Spear phishing** : message ciblé, personnalisé avec OSINT préalable (nom du destinataire, contexte professionnel, vocabulaire interne). Beaucoup plus efficace.
- **Whaling** : spear phishing visant un cadre supérieur ou une personne haut placée. Effets de levier importants (autorisation de virement, ouverture d’accès).
- **Smishing** : phishing par SMS. En croissance avec faux livreurs, fausses banques, faux opérateurs.
- **Vishing** : phishing vocal. Le téléphone légitime l’autorité ressentie.
- **Quishing** : phishing par QR code. Affichage en lieu public d’un QR qui pointe vers site malveillant.

#### 33.3 BEC : Business Email Compromise

Variante professionnelle. Un attaquant compromet (ou usurpe) le compte d’un dirigeant. Envoie au comptable une demande de virement urgent, plausible, semblant venir du DG. Le comptable exécute. Pertes annuelles mondiales : milliards.

Mitigation : procédures internes exigent confirmation par canal séparé (téléphone interne, en personne) pour tout virement au-dessus d’un seuil. Formation systématique. Vérification des en-têtes email (SPF, DKIM, DMARC).

#### 33.4 Reconnaissance préalable et OSINT offensif

Avant un spear phishing sérieux, l’attaquant a typiquement passé heures voire jours sur ta présence publique : LinkedIn, X, articles, slides de conférences, contributions GitHub, mentions dans la presse. Il connaît tes collègues, ton vocabulaire, tes projets en cours.

Conséquence : ta réduction d’empreinte publique (Ch 5-8) est *aussi* une mesure anti-phishing structurelle.

#### 33.5 Indicateurs et détection

À l’œil :

- **Domaine légèrement modifié** : `proton-mail.com` au lieu de `proton.me`, `microsoft0nline.com` au lieu de `microsoft.com`. Survoler les liens, lire l’URL réelle.
- **Sense d’urgence artificielle** : « action immédiate requise », « votre compte sera suspendu dans 24h ».
- **Émotion stimulée** : peur (« sécurité compromise »), curiosité (« document confidentiel pour vous »), cupidité (« vous avez gagné »), serviabilité (« j’ai besoin d’aide »).
- **Demande inhabituelle** : action que tu ne ferais normalement pas dans ce contexte.
- **Discordance signal/canal** : ton patron ne t’envoie jamais des emails à 22h pour des virements urgents.

Au-delà :

- **Vérification du sender** : analyser les en-têtes complets (Received, Authentication-Results).
- **Vérification du domaine** : `whois` du domaine, ancienneté (un domaine créé hier est suspect).
- **Bac à sable** pour pièces jointes (Ch 16).

#### 33.6 Spyware mercenaire : Pegasus, Predator, Graphite

**Pegasus (NSO Group)** : spyware iOS/Android le plus documenté. Capacités révélées par Citizen Lab, Amnesty Security Lab : exfiltration complète (messages, photos, contacts, localisation), activation du micro et de la caméra, contournement du chiffrement E2EE (lecture après déchiffrement local).

Vecteurs documentés :

- **Zero-click iMessage** (FORCEDENTRY, 2021) : exploit envoyé en iMessage qui s’exécute sans interaction. Patch Apple ultérieur.
- **Zero-click WhatsApp** (2019) : appel WhatsApp qui infecte même sans décrocher.
- **One-click via lien** : SMS contenant un lien qui exploite WebKit.
- **Réseau** : injection via opérateur cellulaire compromis.

**Predator (Intellexa / Cytrox)** : concurrent grec, capacités similaires, déploiement documenté en Grèce, Égypte, Vietnam, Madagascar, Soudan.

**Graphite (Paragon Solutions)** : plus récent (2024-2025), capacités équivalentes, déploiement contesté (révélations Citizen Lab fin 2024, WhatsApp a notifié des journalistes et activistes en janvier 2025).

**QuaDream, Candiru** : autres acteurs, plus en retrait.

**Cibles documentées 2020-2025** : journalistes (dont Jamal Khashoggi avant son assassinat — un des proches était sous Pegasus), activistes (Forbidden Stories Pegasus Project), avocats, opposants politiques, proches de cibles. Cas confirmés sur 6 continents.

#### 33.7 Lockdown Mode, GrapheneOS, durcissement

**Lockdown Mode iOS** (cf. Ch 15) désactive des fonctionnalités spécifiquement exploitées par les spyware mercenaires. Études de cas Citizen Lab montrent qu’il aurait bloqué plusieurs exploits documentés. Pour HVT : activation systématique.

**GrapheneOS** : durcissement kernel, sandboxing renforcé, attestation. N’élimine pas le risque mais relève la barre.

**Reboot quotidien** : la plupart des spyware modernes ne persistent pas au redémarrage. Cinq secondes par jour de discipline = grandes leçons d’élévation du coût pour l’attaquant.

#### 33.8 Détection : MVT, iVerify, notifications plateformes

- **MVT (Mobile Verification Toolkit)** : développé et maintenu par *Amnesty Security Lab*, open source (https://github.com/mvt-project/mvt). Analyse les sauvegardes iPhone (iTunes/iCloud-style local backups, *pas* iCloud chiffré) et les *full filesystem dumps* Android pour détecter des indicateurs de compromission (IOCs) Pegasus, Predator, Graphite, QuaDream et d’autres familles documentées. Plus efficace en post-mortem (sur un appareil suspecté) qu’en temps réel. Les IOCs sont publiés et mis à jour par Amnesty et Citizen Lab à mesure de leurs investigations.
  
  *Limites* : MVT détecte les IOCs *connus*. Une variante neuve d’un spyware mercenaire peut ne pas être détectée. L’absence de détection ne prouve pas l’absence d’infection. C’est néanmoins un outil de référence — la majorité des cas Pegasus publiquement confirmés l’ont été après analyse MVT par Amnesty ou Citizen Lab.
  
  *Workflow typique* : sauvegarde locale iTunes du iPhone (cryptée, mais MVT peut traiter), import dans MVT, scan automatique contre les IOCs, génération d’un rapport. Pour Android, plus complexe (full image dump requis, possibilité de root requis).
- **iVerify** : outil commercial développé par *Trail of Bits* puis par une équipe dédiée. Application iOS / Android. Heuristiques pour détecter spywares connus, audit de la posture de sécurité de l’appareil (versions à jour, Lockdown Mode actif, services à risque), alertes en cas d’anomalie. Pratique au quotidien pour profils HVT — c’est un complément de MVT, pas un substitut. Modèle freemium, plans pro pour journalistes/ONG accessibles via partenariats avec Access Now.
- **Notifications plateformes** :
  - **Apple Threat Notifications** envoyées depuis 2021. Le wording standard est « Apple a détecté que vous êtes potentiellement la cible d’une attaque parrainée par un État ». Apple ne précise pas le vecteur, mais publie les critères généraux. Ces notifications sont conservatrices — Apple privilégie d’alerter à risque légèrement avéré plutôt que tarder à le faire.
  - **Google Threat Analysis Group (TAG)** envoie des notifications équivalentes sur Gmail et Workspace pour ciblage par acteurs étatiques.
  - **Meta** alerte via WhatsApp dans les cas de zero-click exploit (cas Paragon Graphite, janvier 2025 : ~90 utilisateurs notifiés dans plusieurs pays dont l’Italie).
  - **Si tu reçois une telle notification** : prends-la au sérieux. C’est rare. Ces notifications sont quasi systématiquement validées par des éléments concrets côté plateforme. Application immédiate de la procédure 33.9.

#### 33.9 Procédure post-compromission suspectée

1. **Isolation** : passer l’appareil en mode avion (vrai mode avion, vérifié). Faraday bag si disponible.
1. **Ne pas redémarrer** (perdrait des artefacts forensiques) — sauf si tu n’as pas accès à un analyste forensique.
1. **Contact d’experts** : Access Now Digital Security Helpline (gratuit pour HVT), Citizen Lab, Amnesty Security Lab.
1. **Sauvegarde** pour analyse (`idevicebackup2` ou Quicktime pour iOS sans iCloud).
1. **En attendant analyse** : appareil neuf, comptes audités, mots de passe critiques renouvelés, contacts prévenus.
1. **Long terme** : changement de modèle de menace, formation, montée en posture.

#### 33.10 *Fil rouge* — Anya reçoit une notification Apple

Anya V. reçoit un mail d’Apple Threat Notification : « Apple détecte que vous êtes potentiellement la cible d’une attaque par un attaquant parrainé par un État ». Elle :

1. Met immédiatement son iPhone en mode avion, le glisse dans une pochette Faraday.
1. Contacte la Digital Security Helpline d’Access Now.
1. Avec leur aide, fait une sauvegarde via Mac, soumet à analyse Citizen Lab.
1. Diagnostic : présence d’IOC Predator. Confirmation après 10 jours.
1. Change tous ses comptes critiques depuis appareils propres. Bascule définitivement sur GrapheneOS. Communique publiquement, ce qui est sa stratégie : la publicité protège.

-----

### Chapitre 34 — IA générative, LLM, deepfakes et privacy

#### 34.1 Quatre vagues qui changent le paysage

L’IA générative 2023-2026 a modifié quatre vecteurs :

- **Création de contenu falsifié** plausible (texte, image, vidéo, voix) à coût marginal nul.
- **Capacité d’attaque automatisée** (phishing personnalisé à grande échelle, génération de pretext crédibles).
- **Aspiration de données** : modèles entraînés sur du contenu massif incluant des données personnelles.
- **Intégration dans les appareils** (Apple Intelligence, Gemini sur Android, Copilot dans Windows) : nouvelles surfaces d’exposition.

#### 34.2 LLM cloud : ce que ton fournisseur voit

Quand tu utilises ChatGPT, Claude, Gemini, Mistral Le Chat depuis le navigateur ou l’app, tu envoies tes prompts à leurs serveurs. Conséquences :

- **Stockage** : par défaut, les conversations sont stockées et utilisables pour amélioration des modèles.
- **Logs** : disponibles à l’opérateur, accessibles sur réquisition légale.
- **Pas d’E2EE** : du contenu en clair entre toi et le fournisseur.
- **Sensitivity** : un prompt révèle ton sujet d’intérêt, ton vocabulaire, ton style, ton contexte professionnel.

**Comportements à éviter** : envoyer à un LLM cloud des informations personnelles identifiantes sensibles (numéros, noms de sources, contenus internes confidentiels, dossiers médicaux).

#### 34.3 Modes « privacy » des fournisseurs

Plusieurs fournisseurs proposent des options :

- **ChatGPT « Temporary Chat »** : pas de stockage long terme. À activer manuellement.
- **Claude.ai** : politique de non-entraînement sur conversations consumer par défaut depuis 2024-2025.
- **API mode** vs **interface chat** : l’API offre généralement de meilleures garanties contractuelles (pas d’entraînement, rétention configurable). Pour usage pro sérieux.
- **Plans entreprise** : politiques de rétention contrôlées contractuellement.

Lire la politique du fournisseur à jour est indispensable, les choses bougent vite.

#### 34.4 LLM locaux : Ollama, LM Studio, llama.cpp

L’alternative privacy : faire tourner un LLM **sur ta machine**. Le prompt ne quitte jamais ton appareil.

- **Ollama** : runner simple pour modèles ouverts (Llama, Mistral, Qwen, etc.). Installation en quelques commandes, modèles téléchargés localement.
- **LM Studio** : interface graphique, profil grand public.
- **llama.cpp** : moteur d’inférence efficace, base de plusieurs solutions.

**Performance** : sur Mac M-series ou laptop avec GPU récent, modèles 7-13B donnent qualité utilisable. Modèles 70B exigent matériel sérieux mais possibles. Qualité légèrement inférieure aux frontières (GPT-4, Claude 4, Gemini 2.5) mais en progression rapide.

**Pour qui** : profils qui traitent des informations confidentielles et veulent rester maîtres. Excellent pour analyse de documents sensibles, brainstorming privé, drafting de notes confidentielles.

#### 34.5 Connecteurs IA (MCP, plug-ins, agents)

L’année 2024-2025 a vu se généraliser les **connecteurs** entre LLM et données utilisateur : MCP (Model Context Protocol), plug-ins, agents qui lisent ton calendrier, tes emails, tes documents.

**Risques** :

- **Élargissement de surface** : l’agent peut accéder à tes données plus largement que tu ne le réalises.
- **Prompt injection** : un document piégé peut faire faire des actions à un agent (exfiltration, modifications, envoi de messages). Vecteur d’attaque actif documenté en 2024-2025.
- **Persistance** : agent qui s’authentifie une fois et tourne en arrière-plan.
- **Données exposées au fournisseur LLM** : tout ce que l’agent lit, le LLM l’a vu.

**Pratique défensive** :

- Privilégier connecteurs avec accès *en lecture* uniquement quand possible.
- Limiter la portée (scope minimal sur OAuth).
- Audit régulier des autorisations.
- Pour profil sensible : pas de connecteur sur comptes critiques.

#### 34.6 Apple Intelligence, Microsoft Copilot, Gemini sur Android

Intégrations IA system-level. Spécificités :

- **Apple Intelligence** : revendique « Private Cloud Compute » avec architecture attestable. Pour requêtes locales (Siri reformulation, etc.) : on-device. Pour requêtes complexes : Apple Cloud Compute en E2EE attestable. Garanties techniques sérieuses mais auditabilité limitée pour utilisateur externe.
- **Microsoft Copilot dans Windows et Recall** : Recall est annoncée comme une fonctionnalité réservée aux **Copilot+ PCs** (matériel récent intégrant un NPU dédié), **opt-in** au niveau de l’utilisateur (la fonctionnalité n’est pas activée par défaut depuis le re-lancement), avec snapshots stockés localement et index présentés par Microsoft comme chiffrés et liés au Secure Enclave de la machine. La fonctionnalité avait été initialement déployée sans ces garanties en 2024, ce qui avait suscité une vague de critiques de chercheurs en sécurité ; Microsoft a suspendu puis re-lancé Recall fin 2024 avec ces protections additionnelles. Les critiques de fond persistent : capture régulière de l’écran indexée par IA crée par construction une base d’informations sensibles, dont la sécurité repose entièrement sur la robustesse de la TEE locale et l’absence d’exploitation de la machine. Pour profils sensibles : laisser Recall désactivé.
- **Gemini sur Android** : intégration profonde aux services Google, transmission cloud par défaut.

**Pour profils sensibles** : désactiver autant que possible les fonctionnalités IA système qui transmettent du contenu hors appareil.

#### 34.7 Aspiration de données par entraînement

Les modèles LLM ont été entraînés sur des corpus massifs incluant du contenu public (web crawl) et parfois privé (litiges en cours sur sources illégales). Conséquence : il existe des cas documentés où des modèles **regurgitent** verbatim du contenu d’entraînement, y compris des données personnelles.

**Mitigation côté utilisateur** :

- Limiter ta présence publique (Ch 5-8) limite ce qui peut être ingéré.
- Demandes d’opt-out auprès des fournisseurs (parfois disponibles, parfois théoriques).
- Surveiller les outputs sur ton propre nom dans les LLM publics.

#### 34.8 Robots.txt, ai.txt, droit à l’opposition au scraping

Pour qui produit du contenu en ligne et veut limiter son ingestion :

- **robots.txt** : standard historique, respecté par Google et Bing, ignoré par certains crawlers d’entraînement.
- **ai.txt** : standard émergent 2024-2025, plus spécifique pour exclure entraînement IA.
- **Méta-tags HTML** : `<meta name="robots" content="noai, noimageai">` (efficacité variable).
- **Cloudflare AI bot blocking** : depuis 2024, option dans Cloudflare pour bloquer les bots IA identifiés.
- **Cadre légal** : le RGPD (art. 21) permet l’opposition au traitement, applicable au scraping pour entraînement selon une lecture progressivement reconnue. La directive sur le droit d’auteur de 2019 (art. 4) prévoit le « opt-out » pour le data mining commercial.

#### 34.9 Deepfakes vidéo : état 2025-2026

La qualité des deepfakes vidéo a passé en 2024-2025 le seuil de plausibilité pour observateur non averti. Outils : Sora (OpenAI), Veo (Google), Gen-3 (Runway), HeyGen, D-ID, plus une cohorte open source.

Cas documentés :

- Faux Zelensky annonçant capitulation (2022, peu convaincant à l’époque).
- Faux Macron en mai 2024 (deepfake politique en période électorale).
- Sextorsion par deepfake en croissance, particulièrement contre femmes (cf. Sensity, Cyber Civil Rights Initiative).
- Faux call vidéo CFO Arup, Hong Kong, début 2024 : virement de 25 M$ après deepfake convaincant en réunion vidéo.

#### 34.10 Deepfakes audio : voice cloning

Encore plus mature que la vidéo. Outils : ElevenLabs, Resemble AI, plus solutions open source. **Trois secondes** d’enregistrement de voix suffisent pour cloner avec qualité plausible.

Cas en croissance :

- Faux appels « ton enfant a un accident, envoie de l’argent » utilisant la voix clonée.
- Faux PDG demandant virement urgent.
- Phishing vocal personnalisé.

#### 34.11 Biométrie vocale et auth téléphonique

Implication : la sécurité par « reconnaissance de la voix » au téléphone (utilisée par certaines banques, services administratifs, parfois Apple ID via Siri) est devenue **structurellement faible**. Les institutions qui en dépendent migrent ou doivent.

**Pour toi** : si une institution te propose auth vocale comme seule MFA, refuser. Demander alternative.

#### 34.12 Procédures anti-deepfake en réunion

Pour réunions sensibles à distance :

- **Codes hors bande** : convenir d’un mot de passe convenu en personne, à prononcer en début de visio pour authentifier.
- **Vidéo conférencière** : un deepfake en temps réel est aujourd’hui difficile à maintenir sous gestures complexes ; demander à la personne de poser une main de manière inattendue, tourner la tête vivement, montrer une pièce d’identité — peut révéler artefacts.
- **Rappel sur canal vérifié** : si doute, raccrocher et rappeler sur le numéro connu.

#### 34.13 Détection de deepfake : état de l’art

Outils en croissance, fiabilité partielle :

- **Sensity AI, Reality Defender, Truepic** : commerciaux, focalisés enterprise.
- **Académiques** : suite d’outils universitaires (FaceForensics++, DFDC).
- **Limites** : course à l’armement permanente entre génération et détection. Pas de garantie.

**Stratégie défensive** : ne pas dépendre uniquement de détection ; combiner avec vérification hors bande systématique.

#### 34.14 Watermarking : C2PA, SynthID

- **C2PA (Coalition for Content Provenance and Authenticity)** : standard de provenance cryptographique d’images, vidéos, documents. Adobe, Microsoft, Sony, BBC. Embarque dans le fichier l’historique de capture/modifications, signé. Pour authentifier l’origine d’un contenu.
- **SynthID** (Google DeepMind) : watermark invisible dans contenus générés par IA Google. Détectable par outils dédiés.
- **Limites** : volontaire, supprimable, partiellement déployé. Utile mais pas suffisant.

#### 34.15 IA dans la pile attaquant

Du côté offensif :

- **Phishing personnalisé** : un LLM rédige des emails sur mesure à partir d’OSINT préalable. Qualité linguistique, registre, vocabulaire — quasi parfaits.
- **Vocal phishing** : voice cloning + LLM = conversation crédible.
- **Reconnaissance** : LLM analyse vastes corpus de données fuitées pour identifier patterns exploitables.
- **Génération de pretext** : LLM produit scénarios de social engineering convaincants.

**Conséquence** : la qualité moyenne des attaques augmente. Les indicateurs traditionnels (fautes, formulation maladroite) sont moins fiables. Le filtrage se déplace vers le **comportement** et le **canal** plutôt que le contenu.

#### 34.16 IA dans la pile défenseur

Du côté défensif :

- **Détection d’anomalies** : LLM dans EDR pour analyse comportementale.
- **Triage automatique** : assistance pour analystes SOC.
- **Génération de leurres** (honeypots intelligents).
- **Aide à la rédaction de procédures, formation, sensibilisation**.

L’asymétrie en 2026 : l’IA aide les deux camps à l’avantage de l’attaquant *à court terme* (l’attaque scale plus facilement que la défense), mais à l’avantage du défenseur à moyen terme si déploiement systématique.

#### 34.17 Cadre éthique : usage de l’IA dans son propre travail

Ce cours postule un usage IA éthique : compréhension, rédaction, analyse, formation. Pas de génération de contenu trompeur, pas d’impersonation, pas d’utilisation pour harceler. Le droit (loi française de 2024 sur deepfakes, AI Act UE) sanctionne désormais explicitement plusieurs usages malveillants.

#### 34.18 *Fil rouge* — Léa face à un deepfake de sa source

Trois mois après sa première rencontre avec Karim, Léa reçoit un appel vidéo Signal. Voix et image de Karim, ton paniqué : « Léa, j’ai besoin que tu rendes les documents, ils savent, c’est dangereux pour ma famille. » Léa ressent le malaise — le ton n’est pas tout à fait celui de Karim. Elle applique le protocole pré-convenu : « Karim, peux-tu me redire le proverbe qu’on a échangé la première fois ? ». Silence côté appel, puis raccrochage. Léa contacte ensuite Karim sur leur canal SimpleX par texte : Karim répond, c’est bien lui, et il n’a pas appelé. Tentative de deepfake confirmée. Bascule en alerte, audit complet des canaux, vérification que la stack tient toujours.

-----

### Chapitre 35 — OPSEC humaine : entourage, photos, voix, stylométrie, traces comportementales

#### 35.1 Entourage : maillon souvent ignoré

Ton meilleur OPSEC tombe si ton entourage publie ton anniversaire le jour, te tague sur une photo géolocalisée, ou répond à un appel de pretext en donnant ton emploi du temps.

**Mesures** :

- **Conversation explicite** avec les proches importants : pas de tag, pas de mention par nom, pas de photo en ligne sans accord, pas de réponse à des questions sur toi sans vérification.
- **Documents partagés** : ne pas mettre tes infos perso dans les listes Excel familiales partagées sur Google Sheets.
- **Réseaux familiaux** : ta mère a publié ton adresse sur Facebook ? Discussion privée, sans drame, avec aide à modifier les paramètres.
- **Enfants** : pas de prénom + école visible publiquement. Pas de photo géolocalisée.

#### 35.2 Photos : géolocalisation visuelle

Au-delà de l’EXIF (Ch 31), une photo révèle par son contenu visuel :

- Vue par la fenêtre permettant de trianguler le quartier.
- Arrière-plan industriel ou architectural identifiable.
- Plaques d’immatriculation visibles.
- Marquages d’entreprise locale.
- Reflets sur surfaces brillantes (vitre, miroir, écran, œil).

**OSINT géo-visuel** est une discipline mature (Bellingcat, GeoGuessr). Un combinaison d’indices banaux permet une géolocalisation au quartier voire au bâtiment.

**Pour la publication** : examiner chaque photo en imaginant ce qu’un attaquant motivé peut déduire. Recadrer, flouter agressivement les éléments contextuels.

#### 35.3 Voix : empreinte vocale et clonage

Cf. Ch 34. Implications spécifiques :

- Tes interviews publiques, conférences vidéo, podcasts sont des échantillons exploitables pour cloner ta voix.
- Stratégie : pour HVT, limiter la diffusion publique de longs échantillons vocaux. Pour usage public (journaliste qui doit témoigner), accepter et compenser par codes hors bande.

#### 35.4 Stylométrie : signature d’écriture

Ton style d’écriture est une empreinte. Caractéristiques :

- Longueur moyenne des phrases.
- Distribution des virgules, points-virgules, deux-points.
- Vocabulaire spécifique (mots favoris, tics).
- Formulations récurrentes.
- Erreurs typographiques personnelles.
- Préférences orthographiques (français de Belgique vs France, anglicismes).

Cas Bitcoin et Satoshi Nakamoto : analyses stylométriques ont éliminé/proposé plusieurs candidats sur la base du seul style.

**Quand c’est important** : pour publication sous pseudonyme stable, si l’attaquant peut soupçonner qui tu es, comparer ton écriture pseudonyme à ton écriture connue est trivial. Le pseudonyme tombe.

**Mitigations** :

- **Réécriture par LLM** : faire passer ton texte par un LLM pour reformulation neutre. Atténue ta signature.
- **Discipline volontaire** : raccourcir ou allonger systématiquement les phrases par rapport à ton naturel, modifier ponctuation. Coût cognitif élevé, durabilité limitée.
- **Pseudonymes à publication courte** : moins d’échantillons = moins de signature stable détectable.

#### 35.5 Traces comportementales : horaires, lieux, routines

Tu es prévisible. Tu te connectes à certaines heures. Tu visites certains sites. Tu écris à certaines personnes. Tu commandes la même chose. Tu prends le même chemin. Cette routine est une signature.

Pour une identité compartimentée : les routines doivent se compartimenter aussi. Le compte « anonyme » qui se connecte aux mêmes heures que ton compte nominal est trivialement corrélable.

**Pratique** :

- Pour compartiments sensibles, varier les fenêtres temporelles, les lieux de connexion, les rythmes.
- Pour rester crédible, ne pas adopter un comportement *trop* différent (qui devient un autre type de signature).

#### 35.6 Métadonnées comportementales hors numérique

- **Achats** : régularité, lieux, types (cf. Ch 32).
- **Déplacements** : transports en commun avec carte nominative (Navigo, Métro), péages, parking surveillé.
- **Présence physique** : caméras (CCTV public et privé), reconnaissance faciale en croissance dans certains pays.
- **Smart home** : assistants vocaux qui enregistrent, thermostats connectés qui révèlent présence/absence.

#### 35.7 Discipline du « jamais en ligne quand X »

Une discipline simple à grande efficacité : *ne jamais* utiliser le compte sensible quand tu es identifiable autrement. Si ton téléphone perso est allumé chez toi, ton compte sensible ne se connecte pas en même temps depuis ton FAI domestique — corrélation triviale.

Schéma :

- Compte sensible utilisé exclusivement depuis lieux/réseaux/appareils distincts.
- Téléphone perso physiquement absent de ces sessions (laissé chez soi, en faraday bag, etc.).
- Pas de cross-contamination horaire.

#### 35.8 *Fil rouge* — Léa adopte une routine stricte

Sur l’enquête, Léa s’impose :

- Téléphone perso laissé chez elle (chargeur sur la table, comme si elle ne sortait pas) les jours d’enquête sensible.
- Travail enquête uniquement depuis le bureau séparé (loué via le consortium), ou Tails sur laptop dédié dans un lieu calme.
- Horaires d’enquête : afternoon et soir, jamais matin (qui est son créneau pro public).
- Communications avec Karim : créneaux convenus, jamais réponse impulsive.

-----

### Chapitre 36 — Voyage, frontières et appareils temporaires

#### 36.1 Modèle de menace voyageur

La frontière est un lieu particulier : l’État a légalement le droit d’inspecter tes appareils dans des limites variables. Les douanes US peuvent demander à examiner ton téléphone et ordinateur, parfois à les retenir plusieurs jours. Singapour, Israël, certains pays asiatiques également. Européen entrant aux US : la liberté de refuser est limitée (refus = refus d’entrée).

Pour les voyages en pays à forte censure ou à DPI agressif, le choix du VPN doit être fait **avant le départ**. Installer un outil de contournement une fois sur place peut être impossible si les sites officiels, stores ou dépôts sont bloqués.

**Procédure** : installer, tester et documenter au moins deux options avant le départ : un VPN privacy classique, un outil anti-censure obfusqué, et Tor Browser avec bridges. Ne pas dépendre d’un seul canal.

Trois questions à se poser avant tout voyage :

1. **Ai-je vraiment besoin** de mes données habituelles sur cet appareil ?
1. **Que se passe-t-il si l’appareil est saisi, cloné, ou rendu après accès** ?
1. **Quelles sont les règles douanières spécifiques** au pays d’entrée ?

#### 36.2 BFU vs AFU à la frontière (CRITICAL)

**Avant de passer une frontière** : éteindre complètement les appareils. Pas de verrouillage, pas de sommeil. **Vraie extinction**.

Effet : les appareils sont en BFU (Before First Unlock). La plupart des données utilisateur sont protégées par des clés dérivées du code de déverrouillage, qui ne sont pas en mémoire. Les outils forensics professionnels (Cellebrite UFED, GrayKey) sont **significativement moins efficaces** sur un appareil en BFU que sur un appareil en AFU.

Cinq secondes de discipline avant chaque passage frontalier = écart énorme en posture forensique.

#### 36.3 Burner devices

Pour voyages sensibles (frontière hostile, pays à risque) : appareils dédiés au voyage, distincts du quotidien.

- **Téléphone de voyage** : ancien Pixel, GrapheneOS minimal, comptes burner (email dédié, Signal dédié), aucune photo ni contact personnel. Au retour : reset complet ou destruction.
- **Laptop de voyage** : Chromebook ou laptop minimal, comptes burner, données non sensibles uniquement, pas de cookies de session, pas de fichiers locaux. Si besoin d’accès, données récupérées via cloud E2EE après arrivée.

#### 36.4 Procédures pre-voyage

1. **Audit** : qu’est-ce qui ne doit absolument pas franchir la frontière ?
1. **Cloud E2EE** des données nécessaires (Proton Drive, etc.), accessibles depuis l’arrivée.
1. **Backup** complet avant départ.
1. **Effacement des comptes sociaux non essentiels** sur l’appareil de voyage.
1. **Déconnexion** de tous les comptes critiques sur l’appareil de voyage (sessions révoquées, à reconnecter à l’arrivée si besoin).
1. **Compte burner** prêt pour communications de voyage.

#### 36.5 À l’arrivée

- Vérifier l’intégrité physique (vis, scellés, comparaison photos).
- Si soupçon de manipulation : ne pas reconnecter aux comptes principaux, considérer l’appareil comme suspect.
- Reset à neuf si possible.
- Reconnexion progressive aux comptes nécessaires, en surveillant les notifications de connexion suspecte.

#### 36.6 Au retour

- Reset complet de l’appareil de voyage, ou destruction physique si haut risque.
- Audit des appareils restés au domicile (intrusion physique pendant absence ?).
- Audit des comptes : sessions de l’étranger ? Connexions inhabituelles ?
- Changement préventif des credentials critiques si profil HVT.

#### 36.7 Cas particuliers

- **Activistes vers Iran, Russie, Chine, certains pays Moyen-Orient** : VPN nécessaires mais souvent bloqués (utiliser Tor avec bridges, ou VPN avec protocoles obfusqués). Risques pénaux selon pays. Consulter ONG spécialisées (Access Now, EFF, RSF, Front Line Defenders) avant départ.
- **Journalistes en zones de conflit** : protocoles CPJ Digital Safety Kit, RSF guide journaliste, formations dédiées (Hostile Environment Awareness Training).
- **Dirigeants en mission commerciale Asie** : ANSSI publie des guides ; programme de sécurité économique gouvernemental français.

#### 36.8 *Fil rouge* — Léa voyage à Kiev pour enquête terrain

Préparation :

- iPhone perso laissé à Bruxelles.
- Pixel 8a GrapheneOS avec profil enquête, contenant : Signal pro, SimpleX pour Karim, OnionShare, navigateur Vanadium, rien d’autre.
- Laptop dédié enquête (MacBook Air séparé), FileVault, Mullvad VPN, Tails sur clé USB de secours.
- Backup chiffré complet de toute son enquête sur Proton Drive avant départ.
- Compte SimpleX accessible depuis n’importe quel appareil avec ses clés.
- Numéro Signal communiqué à 3 contacts d’urgence : avocate, rédaction, ami de confiance.

À l’arrivée :

- Vérification matérielle : pas de manipulation visible.
- Premier contact local par téléphone non lié, lieu choisi par sa source locale.

Au retour :

- Reset complet du téléphone et laptop.
- Audit des comptes : aucune connexion suspecte.
- Documents rapatriés via Proton Drive en mode E2EE.

-----

### Chapitre 37 — Cadre juridique et éthique

> **Note** : cette section est informative et générale, pas un avis juridique. Le droit évolue rapidement (Chat Control, AI Act, transpositions diverses). En cas d’enjeu réel, consulter un avocat spécialisé.

#### 37.1 Vie privée et CEDH article 8

L’article 8 de la Convention européenne des droits de l’homme garantit le droit au respect de la vie privée et familiale, du domicile et de la correspondance. Restrictions admises sous trois conditions cumulatives :

- **Prévue par la loi**.
- **Légitime** (sécurité nationale, ordre public, etc.).
- **Nécessaire dans une société démocratique** (proportionnée).

Jurisprudence CEDH abondante. Toute mesure de surveillance massive doit passer ce triple test ; plusieurs régimes nationaux ont été retoqués (UK GCHQ, France IOC, etc.).

#### 37.2 RGPD : droits utilisables

Articles directement utilisables par un individu :

- **Article 15** : droit d’accès. Tu peux demander à tout responsable de traitement quelle donnée il détient sur toi.
- **Article 17** : droit à l’effacement (« droit à l’oubli »).
- **Article 21** : droit d’opposition au traitement.
- **Article 20** : droit à la portabilité.

Recours : CNIL (FR), équivalent national (APD en Belgique, AEPD en Espagne, etc.), avec amendes croissantes en cas de violation.

#### 37.3 LCEN : chiffrement libre en France

L’article 30 de la loi sur la confiance dans l’économie numérique (LCEN, 2004) consacre la liberté d’usage des moyens de cryptologie en France. Le chiffrement personnel est **légal et garanti**. L’État ne peut pas l’interdire pour l’usage privé.

Limites : obligations de déclaration pour les fournisseurs de moyens de cryptologie ; régime spécifique pour l’exportation ; obligation de déchiffrer sur réquisition judiciaire (cf. 37.5).

#### 37.4 Secret des sources des journalistes

Loi française du 4 janvier 2010 sur la protection du secret des sources : pas d’atteinte au secret des sources sans impératif prépondérant d’intérêt public, et selon procédures strictes.

Règlement (UE) 2024/1083 dit *European Media Freedom Act* (EMFA) : renforcement, harmonisation européenne, encadrement strict de l’usage du spyware contre journalistes, droit d’opposition à la révélation des sources, protection contre les pressions économiques sur les rédactions. Le texte n’est pas une directive (qui aurait laissé une marge de transposition nationale) mais un règlement directement applicable.

**En pratique** : protégé en droit, mais des affaires (Édouard Tétreau, Le Monde, Mediapart vs renseignement) ont montré les fragilités. L’OPSEC technique du journaliste reste un complément indispensable à la protection légale.

#### 37.5 Obligation de remettre une convention secrète de déchiffrement

Cas français : l’article 434-15-2 du Code pénal sanctionne le **refus de remettre aux autorités judiciaires une convention secrète de déchiffrement d’un moyen de cryptologie susceptible d’avoir été utilisé pour préparer, faciliter ou commettre un crime ou un délit**. Peines : trois ans d’emprisonnement et 270 000 € d’amende ; aggravées à cinq ans et 450 000 € si le refus a empêché la prévention d’un crime ou délit.

Le Conseil constitutionnel a, à plusieurs reprises (notamment 2018 et 2025), validé le dispositif sous réserves d’interprétation, en précisant notamment les conditions dans lesquelles ce délit peut être retenu. La jurisprudence reste cependant nuancée :

- Distinction entre la **convention secrète** (clé cryptographique, mot de passe d’un volume chiffré) et le **code utilisateur** d’un appareil (qui sert à déverrouiller mais ne constitue pas en soi une convention de déchiffrement) — distinction qui a fait l’objet de jurisprudences contradictoires.
- Conditions de l’obligation : la convention doit concerner un moyen de cryptologie « susceptible d’avoir été utilisé » pour un crime ou délit, ce qui suppose un faisceau d’indices, et non une simple suspicion généralisée.
- Pratique des juridictions très variable selon contexte et selon avocats engagés.

**Cas comparés** :

- **Royaume-Uni** : RIPA section 49 prévoit une obligation équivalente (jusqu’à deux ans de prison pour refus, cinq ans pour terrorisme ou pédocriminalité).
- **États-Unis** : le Cinquième Amendement protège contre l’auto-incrimination forcée ; la jurisprudence sur l’usage forcé de la biométrie par rapport au code mémoire mémorisé reste mouvante (plusieurs décisions divergentes selon circuits fédéraux).
- **Suisse** : pas d’obligation équivalente à 434-15-2 ; position structurellement plus protectrice.

**Implication pratique** : il ne revient pas à ce cours de recommander une attitude (refuser ou non) face à une demande de communication d’une convention de déchiffrement, ni d’évaluer ce qui constitue ou non une telle convention dans un cas concret. Ces questions relèvent d’une analyse juridique individuelle. **Si tu es confronté à une telle demande, la seule action raisonnable est de consulter immédiatement un avocat spécialisé** (droit pénal, droit numérique, ou droit de la presse selon contexte). Refus mal calibré comme communication imprudente peuvent l’un et l’autre aggraver la situation.

Au plan opérationnel préventif, en revanche, ce cours observe que :

- Le code utilisateur **mémorisé** (non biométrique) est structurellement plus difficile à obtenir d’une personne sous contrainte qu’une empreinte digitale ou un visage qui peuvent être utilisés sans coopération active.
- L’état BFU (cf. Ch 12.8) protège les données mieux que l’état AFU contre les outils forensics commerciaux, indépendamment de la question juridique.

#### 37.6 Sapin II : lanceurs d’alerte en France

Loi Sapin II (2016), modifiée par la loi du 21 mars 2022 transposant la directive UE 2019/1937.

Protection accordée aux personnes signalant des faits :

- **Crimes ou délits**.
- **Violations graves de la loi**.
- **Menaces ou préjudices** pour l’intérêt général.

Procédure :

1. **Signalement interne** (en premier lieu, sauf exceptions).
1. **Signalement externe** : autorité compétente (Défenseur des droits, AAI sectorielle).
1. **Divulgation publique** : possible si signalements précédents sans suites, ou risque imminent.

Protections : non-licenciement, non-représailles, confidentialité de l’identité, soutien juridique du Défenseur des droits.

**Limite** : les sanctions effectives contre représailles restent partielles. Beaucoup de lanceurs d’alerte ont payé un prix professionnel et personnel important malgré la loi.

#### 37.7 Anti-doxxing

En France, plusieurs qualifications mobilisables :

- **Atteinte à la vie privée** (art. 226-1 CP).
- **Mise en danger** (si publication d’adresse avec menace).
- **Harcèlement moral** ou en meute (art. 222-33-2-2 CP).
- **Loi du 21 mars 2022** : aggravation des peines pour révélation d’information privée mettant en danger.

Signalement PHAROS. Plainte au parquet. Recours civil pour cessation et indemnisation.

#### 37.8 Chat Control / CSAR : suivi

Cf. Ch 26.12 pour le détail. État de synthèse : dossier toujours en négociation à la rédaction (2026). Le Conseil a pris position en novembre 2025 ; le Parlement européen a soutenu en mars 2026 l’extension temporaire de la dérogation ePrivacy jusqu’en août 2027, ce qui maintient la fenêtre légale actuelle pour les scans volontaires hors-E2EE pendant que les négociations sur le règlement principal continuent. Les positions nationales évoluent au gré des présidences tournantes et des élections.

Si la version finale impose un scanning côté client sur l’E2EE, l’impact serait majeur pour la disponibilité de la messagerie E2EE européenne grand public.

#### 37.9 AI Act UE

Règlement UE 2024/1689 (« AI Act ») : encadrement de l’IA dans l’UE, entré en vigueur progressivement 2024-2026. Pertinence privacy :

- **Article 5** : interdictions (notation sociale, certaines reconnaissances biométriques en temps réel par autorités).
- **Article 6+** : systèmes à haut risque, dont certains usages de reconnaissance faciale.
- **Article 50** : obligation de marquage des contenus IA (deepfakes).

Sanctions importantes pour fournisseurs IA.

#### 37.10 Comparaison FR / UE / US / UK / CH (synthèse)

|Aspect                  |France           |UE                   |US                   |UK               |Suisse                |
|------------------------|-----------------|---------------------|---------------------|-----------------|----------------------|
|**Chiffrement libre**   |Oui (LCEN 30)    |Oui (RGPD compatible)|Oui (constitutionnel)|Oui mais RIPA    |Oui (forte protection)|
|**Obligation clé**      |Oui (434-15-2 CP)|Variable             |5e amendement protège|Oui (RIPA s.49)  |Non                   |
|**Surveillance massive**|LRM 2015, ajustée|Encadrée (CJUE)      |FISA, NSL            |IPA 2016         |Forte protection      |
|**Anti-doxxing**        |Oui (loi 2022)   |Variable national    |Variable état        |Oui (M.Comms Act)|Oui                   |
|**Lanceurs d’alerte**   |Sapin II / 2022  |Directive 2019       |Patchwork sectoriel  |PIDA             |LWB                   |

#### 37.11 Cadre éthique du cours

Ce cours forme à des compétences défensives. Il ne couvre pas :

- Attaque, intrusion, exploitation.
- Contournement d’une enquête judiciaire légitime.
- Dissimulation d’activités illicites.
- Doxxing, harcèlement, fraude à pseudonymes.
- Usurpation d’identité.

Le pseudonymat, le chiffrement, l’anonymat sont des droits exercés dans un cadre légal. Leur usage à des fins illicites engage la responsabilité pénale de l’auteur, indépendamment de l’efficacité technique de l’outil.

-----

### Chapitre 38 — Maintenance opérationnelle, réponse à incident et architectures par profil

#### 38.1 La sécurité est un processus, pas un état

Une posture sécurisée installée en une semaine et jamais entretenue s’érode en six mois. Les mises à jour ne s’appliquent pas, les comptes oubliés s’accumulent, les habitudes glissent, les outils deviennent obsolètes. La maintenance n’est pas optionnelle.

#### 38.2 Routines : hebdo, mensuelle, trimestrielle, annuelle

**Hebdomadaire (15 minutes)** :

- Vérifier que les mises à jour OS et apps sont appliquées.
- Audit rapide des notifications de connexion suspecte.
- Vérification du fonctionnement des sauvegardes automatiques.
- Reboot des appareils sensibles (si pas quotidien).

**Mensuelle (1 heure)** :

- Audit des sessions actives sur comptes critiques (Google, Apple, Microsoft, Signal).
- Vérification HaveIBeenPwned sur emails principaux.
- Audit des permissions d’apps mobiles (revue de ce qui a accès localisation, micro, photos).
- Test rapide de restauration sauvegarde (juste vérifier qu’elle se monte et que les fichiers s’ouvrent).
- Mise à jour firmware si pas auto.

**Trimestrielle (2-3 heures)** :

- Audit complet OSINT défensif (Ch 5).
- Désinscription data brokers nouvellement apparus (Ch 6).
- Audit des appareils : intégrité physique, configuration, comptes connectés.
- Revue du threat model : a-t-il évolué ? Mes adversaires ont-ils changé ?
- Test de restauration complet (sur appareil neuf ou VM).
- Renouvellement des sous-clés PGP si applicable.

**Annuelle (1 jour)** :

- Audit complet de tous les comptes (suppression des inutilisés).
- Renouvellement des clés matérielles si signe d’usure.
- Revue de la stratégie globale : architecture, outils, threat model, formation.
- Documentation à jour (procédures personnelles, contacts d’urgence, codes de récupération).
- Décisions stratégiques : migration vers nouvel OS, nouveau matériel, nouvelle compartimentation.

#### 38.3 Réponse à incident : framework PICERL

Hérité de la cybersécurité d’entreprise, applicable au particulier :

- **P**reparation : avant tout incident, avoir une procédure documentée, contacts d’urgence, backups, outils prêts.
- **I**dentification : détecter qu’un incident a lieu. Notifications plateformes, alertes, comportement anormal.
- **C**ontainment : limiter la propagation. Isoler appareil, révoquer sessions, changer credentials des comptes touchés.
- **E**radication : éliminer la cause. Reset appareil, retrait de malware, fermeture des accès illégitimes.
- **R**ecovery : restaurer le fonctionnement normal. Restauration depuis backup propre, reconfiguration.
- **L**essons learned : analyse post-incident, mise à jour des procédures.

#### 38.4 Procédures par scénario

**Téléphone perdu/volé** :

1. Localisation à distance (Find My iPhone / Android Find My Device) si possible.
1. Effacement à distance si non récupérable.
1. Désactivation SIM auprès de l’opérateur.
1. Révocation sessions des comptes critiques.
1. Désinscription des passkeys liées à l’appareil.
1. Déclaration de vol (police, assureur).
1. Restauration sur appareil neuf depuis sauvegarde.

**Compte compromis** :

1. Changer immédiatement le mot de passe depuis appareil sain.
1. Révoquer toutes les sessions actives.
1. Audit : modifications récentes, filtre mail, méthodes MFA ajoutées.
1. Activer MFA matériel si pas déjà.
1. Vérifier comptes liés (cascade depuis email principal).
1. Communiquer aux contacts si phishing envoyé depuis ton compte.
1. Déposer plainte si dommages.

**Spyware suspecté** :

1. Mode avion + faraday bag immédiatement.
1. Ne pas redémarrer.
1. Contact Access Now Digital Security Helpline (+1-888-414-0100).
1. Sauvegarde pour analyse (iTunes/Quicktime pour iOS).
1. Soumission à Citizen Lab / Amnesty Security Lab pour confirmation.
1. Bascule appareil neuf, comptes audités, threat model révisé.

**Doxxing en cours** :

1. Documentation (captures, URLs, horodatages).
1. Signalement plateformes hébergeantes.
1. Évaluation menace physique, mise à l’abri si nécessaire.
1. Support psychologique et juridique (PEN America, RSF, La Quadrature selon profil).
1. Plainte (PHAROS, parquet).

#### 38.5 Architectures de référence par profil

**Profil 1 : particulier durci grand public**

- iPhone à jour avec ADP iCloud activée.
- Mac ou PC Windows 11 Pro avec chiffrement disque.
- Bitwarden + clés YubiKey (principal + backup).
- Signal pour communications, WhatsApp pour social, Proton Mail principal + alias.
- Mullvad ou IVPN.
- Routines mensuelles + trimestrielles appliquées.

**Profil 2 : journaliste freelance**

- Pixel 8a + GrapheneOS + iPhone perso séparé (ADP).
- MacBook Pro pro + MacBook Air enquête.
- Bitwarden + YubiKey 5 (principal + backup au coffre).
- Signal + SimpleX + Proton Mail pro + alias.
- Tails sur USB pour sessions ponctuelles ultra-sensibles.
- Mullvad VPN, Mullvad Browser quotidien, Tor Browser anonyme.
- Page « comment me joindre confidentiellement » publique.
- Routines complètes appliquées.

**Profil 3 : activiste, manifestation à risque**

- GrapheneOS sur Pixel d’occasion dédié manifestation.
- Aucune donnée personnelle, contacts limités à 3 numéros essentiels.
- Faraday bag.
- Numéros de hotline juridique et avocat sur papier.
- Procédure d’arrestation préparée (qui appeler, qui prévenir).
- Vrai téléphone perso laissé chez soi.

**Profil 4 : dirigeant PME exposé**

- MacBook avec ADP iCloud, FileVault, Lockdown Mode en voyage sensible.
- iPhone idem.
- 1Password famille (partage avec direction).
- Signal pour interne sensible, iMessage avec Contact Key Verification pour exec team.
- Compartimentation pro/perso strictes.
- Formation périodique des collaborateurs (BEC, phishing).
- Politique d’entreprise : MFA obligatoire, MDM Apple Business Manager / Intune.

**Profil 5 : opposant politique en exil (modèle Anya)**

- GrapheneOS dédié, profils stricts.
- Qubes OS pour travail public.
- Tor par défaut pour publications.
- Signal/SimpleX selon contacts.
- Liens hebdomadaires avec Citizen Lab / Access Now.
- Préparation à un éventuel ciblage spyware (MVT installé, iVerify).
- Documentation publique de la situation = stratégie protectrice.

**Profil 6 : RSSI ONG terrain (modèle Yann)**

- Qubes OS sur laptops équipe.
- Procédures écrites et formation continue.
- Cloud E2EE collectif (Proton Drive Business ou Tresorit).
- Stack messageries unifiée (Signal pour interne, Wire pour partenaires).
- Audit annuel par tiers de confiance.

**Profil 7 : particulier face à ex-conjoint abusif (cas D)**

- Changement complet de credentials après séparation.
- Nouveau téléphone, nouveau Apple ID / Google.
- Audit physique du domicile (caméras cachées, AirTags, stalkerware).
- Coalition Against Stalkerware ressources.
- Soutien : association locale, juriste, psychologue.
- Compartimentation totale avec l’ancien partenaire (canaux, comptes, lieux).

**Profil 8 : Personnel institutionnel, défense ou industrie sensible

Pour qui : militaires, policiers spécialisés, personnels de renseignement, protection rapprochée, agents pénitentiaires exposés, salariés de sites critiques, cadres de l’industrie de défense, sous-traitants sensibles.
Objectif : éviter qu’un téléphone personnel ou professionnel ne révèle des lieux sensibles, des routines, des domiciles, des proches ou des déplacements opérationnels.

- téléphone personnel interdit ou laissé hors zone sensible ;
- téléphone professionnel ou opérationnel dédié, géré par MDM/EMM ;
- liste blanche d’applications autorisées ;
- absence d’applications gratuites financées par la publicité ;
- localisation désactivée par défaut, activée seulement pour les usages strictement nécessaires ;
- identifiant publicitaire désactivé ou régulièrement réinitialisé ;
- séparation stricte entre usages personnels, professionnels et opérationnels ;
- formation régulière sur les risques AdTech, ADINT et data brokers ;
- procédures écrites : quels appareils sont autorisés dans quels lieux ;
- contrôles réguliers et sanctions internes en cas de non-respect des consignes.

Point clé : pour ces profils, le risque n’est pas seulement la compromission du téléphone. Le simple fonctionnement normal d’applications grand public peut suffire à exposer des données exploitables par un adversaire.

**Profil 9 : profil HVT extrême (combinaison)**

- Qubes OS + GrapheneOS combinés.
- Tor + VPN obfusqué.
- Multiples appareils air-gap pour secrets long terme.
- Procédures forensiques mensuelles (MVT auto-vérification).
- Réseau de soutien (avocats, ONG, contacts médias).
- Documentation publique stratégique.

#### 38.6 Quand simplifier

L’inverse de l’élévation de posture est aussi nécessaire à savoir gérer : quand l’enquête se termine, quand le threat ne s’applique plus, quand on quitte un poste à risque. Démantèlement contrôlé :

- Décommissioning des appareils dédiés.
- Fusion progressive des comptes si justifié.
- Effacement des secrets de l’enquête (en gardant copies légales et archives).
- Retour à un standard durci mais soutenable.

Le sur-durcissement permanent sans justification est aussi une faute opérationnelle.

-----

> 🟩 **À retenir de la Partie 7**
> 
> - L’humain est le principal vecteur d’attaque moderne. Le travail sur soi et son entourage compte autant que la technique.
> - L’IA générative a déplacé les seuils : phishing personnalisé indiscernable, deepfakes audio/vidéo accessibles.
> - Frontières : éteindre vraiment (BFU), burner devices pour pays sensibles.
> - Le droit protège, mais sa connaissance et son usage actif sont nécessaires. Pas d’OPSEC sans cadre légal éclairé.
> - La sécurité est un processus. Routines hebdo/mensuelle/trimestrielle/annuelle.
> - Architectures par profil : la posture suit le threat model, pas le mode.

-----


## Cas de synthèse finaux

> **Pourquoi ces cas** : les chapitres précédents ont introduit briques et concepts. Les cas montrent comment ces briques se combinent dans des scénarios réalistes complets. Chaque cas mobilise plusieurs parties du cours et fait l’objet de renvois croisés explicites. Le **Cas A** clôt le fil rouge de Léa. Les **Cas B, C, D** déploient les autres profils annoncés en avant-propos.

-----

### Cas A — Léa Martens : journaliste d’investigation, enquête transeuropéenne

**Clôture du fil rouge.** Mobilise les Parties 1-7. Renvois explicites entre chapitres.

#### A.1 Contexte

Léa Martens, 34 ans, journaliste freelance à Bruxelles, accréditée auprès du Parlement européen, membre d’un consortium international (12 médias partenaires sur 8 pays). Enquête : dossier de corruption impliquant un commissaire européen actuellement en exercice, une société israélienne de surveillance privée (qui aurait fourni des outils à des États tiers en violation du régime européen d’exportation de biens à double usage), et un oligarque russe en exil sous sanctions UE, qui aurait financé indirectement l’opération en échange de protection politique.

Durée prévue de l’enquête : 14 mois. Publication coordonnée prévue à T+12 mois. Diffusion simultanée sur les 12 médias partenaires. Léa porte la coordination technique des sources francophones et flamandes.

Sources principales :

- **Karim B.** : fonctionnaire dans une autorité administrative française, accès indirect aux échanges avec la société israélienne via dossier export. Lanceur d’alerte interne. Identité absolument à protéger.
- **Maria C.** : avocate roumaine, dossiers civils contre filiale locale de la société de surveillance. Source plus formelle, identité connue dans l’enquête mais nom à protéger dans la publication.
- **Trois autres sources** : ex-employés (deux de la société israélienne, un du cabinet du commissaire). Identité à compartimenter.

Adversaires plausibles :

- **Le commissaire et son cabinet** : capacité moyenne via réseau professionnel, motivation très forte à mesure que l’enquête se précise.
- **La société israélienne** : capacité technique élevée (c’est leur métier), accès commercial à du spyware mercenaire dans l’écosystème de leur cluster (Israël est l’épicentre du secteur).
- **L’oligarque russe** : capacité élevée via services achetés (réseau Wagner-style, ex-FSB privés). Motivation élevée.
- **Services russes** : capacité très élevée, motivation modérée à élevée selon avancement de l’enquête.
- **Trolls et harcèlement coordonné** : capacité faible mais effet réel d’épuisement et de doxxing à la publication.

Hors périmètre explicite :

- Résistance à une saisie judiciaire belge légale (Léa s’engage à respecter la procédure et à faire appel à son avocat).
- Anonymat auprès de sa rédaction et auprès des partenaires consortium.
- Protection contre criminalité opportuniste banale (couverte par hygiène standard).

#### A.2 Architecture déployée

À l’issue des 14 mois, Léa opère sur trois compartiments séparés.

**Compartiment 1 — Vie civile (Léa Martens, perso)** :

- iPhone 15 Pro perso avec ADP iCloud activée, Lockdown Mode désactivé (usage quotidien banal).
- MacBook Air perso, FileVault, comptes Apple iCloud familiaux, photos famille, vie courante.
- Email principal Proton Mail (migration progressive depuis Gmail terminée après 4 mois).
- Bitwarden + YubiKey 5C NFC principale + YubiKey backup au coffre familial.
- Mullvad VPN sur usage routier (cafés, voyages courts).
- Signal et iMessage avec famille et amis.

**Compartiment 2 — Vie professionnelle publique (journaliste freelance)** :

- MacBook Pro pro, FileVault, compte Apple distinct (sans liaison avec le perso).
- Email pro `lea.martens@[domaine consortium]`, PGP activé avec sous-clés tournantes annuelles, clé maître en air-gap (cf. infra).
- Bitwarden pro distinct (avec YubiKey distincts également).
- Réseaux sociaux pro publics (X, LinkedIn, Bluesky) maintenus activement, avec hygiène (pas de géotag, pas de routines visibles, pas de photo de famille).
- Signal pro (avec username, numéro de téléphone non communiqué publiquement), iMessage activé avec Contact Key Verification pour ses 30 contacts pro principaux.
- Page « comment me joindre confidentiellement » sur son site pro : clé PGP, lien SecureDrop du consortium, son username Signal, mention « pour transmissions sensibles, contactez-moi d’abord, on choisit ensemble le canal ».
- Mullvad Browser quotidien, Firefox + uBlock + arkenfox pour usage rédactionnel, Brave secondaire.

**Compartiment 3 — Enquête sensible (compartiment 3, sans pseudonyme distinct)** :

- Pixel 8a + GrapheneOS, acheté cash en magasin (Léa a marché 30 minutes pour aller au point de vente choisi au dernier moment, payé en liquide).
- Trois profils utilisateur GrapheneOS sur le Pixel : profil principal vide et utilisé seulement pour communication d’urgence ; profil « enquête » avec Signal/SimpleX/Vanadium ; profil « voyage » pour déplacements terrain.
- MacBook Air dédié enquête, FileVault, jamais connecté au compte Apple personnel, OS et apps minimales, mises à jour disciplinées.
- Tails sur deux clés USB neuves achetées en deux fois, en deux lieux différents : usage pour sessions sensibles ponctuelles (premier contact source, ouverture de documents particulièrement à risque).
- Stack messageries enquête : SimpleX (canal source primary avec Karim), Signal avec username (canaux source secondary avec Maria et autres sources), Proton Mail avec alias SimpleLogin (un alias par source pour les très rares occasions où l’email est utilisé).
- Air-gap minimal : un Mac Mini ancien acheté d’occasion, déconnecté de tout réseau, déconnecté physiquement quand non utilisé, dans un coffre. Sert à stocker la clé maître PGP utilisée pour signer les sous-clés annuelles, et à archiver les documents les plus sensibles.
- VPN Mullvad sur tous les terminaux enquête, plus Tor Browser pour navigation anonyme.
- Routine de reboot quotidien du Pixel.

**Stratégie cloud** :

- Documents quotidiens d’enquête : Proton Drive (E2EE par design), avec dossiers compartimentés.
- Archives ultra-sensibles : conteneurs VeraCrypt sur disque externe chiffré, en coffre.
- Sauvegarde 3-2-1-1-0 : 3 copies (Proton Drive + disque local chiffré + disque externe en coffre), 2 supports différents, 1 hors site (le disque externe est chez une avocate de confiance), 1 immuable (snapshot mensuel signé), 0 erreur (test de restauration trimestriel).
- Sauvegardes WhatsApp désactivées (Léa n’utilise pas WhatsApp pour l’enquête, et a activé sauvegarde E2EE pour son WhatsApp perso).

#### A.3 Stack source-journaliste avec Karim

Karim, fonctionnaire AAI française, alerte interne. Premier contact via une rédaction tierce (Mediapart, qui sert d’intermédiaire neutre). Mediapart envoie un message à Léa : « Une personne souhaite te joindre confidentiellement, voici son indicateur de référence ».

Léa et Karim établissent leur canal :

- **Premier échange** : Léa publie un message dans un thread public sur son compte X pro contenant un détail spécifique qu’elle a convenu avec Mediapart. Karim, en voyant ce détail, reçoit la confirmation que Léa est bien la personne qu’il cherche.
- **Initialisation SimpleX** : Karim installe SimpleX sur un téléphone d’occasion qu’il a acheté cash dans un magasin choisi loin de ses lieux habituels (cf. Ch 9, Ch 15). Il crée un compte SimpleX sans numéro de téléphone.
- **Échange du lien** : Léa et Karim échangent leur lien de connexion SimpleX via le canal Mediapart, qui ne voit pas le contenu (la rédaction relaie un blob chiffré PGP fourni par Léa, déchiffré par Karim avec sa clé qu’il a générée pour l’occasion sur Tails).
- **Vérification d’identité** : premier appel SimpleX vocal court. Léa et Karim ne se connaissent pas physiquement. Ils ont convenu d’un proverbe à prononcer pour authentifier ; le vrai test est dans la cohérence de leur récit et le savoir détenu par Karim (informations vérifiables auprès de Léa).
- **Régime opérationnel** : disappearing messages 24 h pour toute la conversation. Vérification mutuelle hebdomadaire (Léa demande à Karim un détail convenu à l’avance qui change chaque semaine). Transferts de documents via OnionShare exclusivement, pas SimpleX (les fichiers SimpleX restent sur les serveurs SimpleX un temps).

#### A.4 Workflow de réception et traitement des documents

À chaque paquet de documents reçu de Karim (3-7 paquets sur 14 mois) :

1. Réception du lien OnionShare via SimpleX.
1. Léa boot Tails sur sa clé USB enquête principale, depuis le MacBook Air dédié.
1. Téléchargement via Tor Browser à l’intérieur de Tails. Vérification du hash SHA-256 fourni hors-bande par Karim (sur SimpleX, message court non lié au transfert).
1. Passage des PDF par Dangerzone (dans Tails, ou re-importé dans une dispVM Qubes sur le Mac quand Léa migre vers Qubes au mois 8).
1. Audit métadonnées : ExifTool sur chaque fichier. À deux reprises sur les 14 mois, Léa trouve des métadonnées qui auraient révélé l’auteur : un PDF avec « Author = [nom de Karim au format administratif officiel] » dans le XMP, et un DOCX avec un commentaire interne contenant un nom de personne mentionnée dans le bureau de Karim. À chaque fois, nettoyage avant tout transfert ultérieur.
1. Archivage chiffré : import dans conteneur VeraCrypt sur disque externe, déchiffré uniquement lors de sessions de travail sur l’enquête. Le mot de passe du conteneur est un Diceware 8-mots, dérivé via Argon2id (memory ≥ 1 GiB, t=4, p=4).
1. Documentation : log interne (dans le conteneur) — date, source, hash, environnement utilisé, notes contextuelles. Pas pour partage, pour traçabilité d’enquête et audit interne du consortium.

#### A.5 Incident — la tentative de spear phishing à T+5 mois

À cinq mois d’enquête, Léa reçoit sur son email pro un message d’apparence légitime, qui semble venir d’un correspondant d’un des médias partenaires du consortium. L’objet : « Suite à notre échange à la conférence Bruxelles — documents complémentaires ». Pièce jointe : un PDF.

Léa, par discipline, ne clique pas en client mail (la preview est désactivée par défaut sur sa stack). Elle examine les en-têtes : DKIM signature présente mais sur un domaine très proche du domaine légitime (`partner-media-org.com` au lieu de `partnermediaorg.com`). Récente création de domaine (Whois indique enregistrement il y a 9 jours). L’expéditeur n’est pas dans son carnet d’adresses vérifié.

Elle ne télécharge pas le PDF en environnement de quotidien. Elle bascule vers son MacBook Air enquête, isole le fichier dans un dispVM (Léa est passée à Qubes 2 mois plus tôt sur ce laptop), l’ouvre dans la dispVM. Le PDF, à l’œil nu, contient quelques lignes neutres. Mais l’analyse via ExifTool révèle un objet JavaScript embarqué. Léa n’exécute pas ; soumission du PDF anonymisé à un confrère analyste malware (via OnionShare). Diagnostic : tentative d’exploit, probablement non-zero-day, ciblant une ancienne version d’Acrobat Reader. La pièce jointe contient une chaîne d’infection plausible.

Léa documente. Préviens son consortium. Vérification : aucun autre membre du consortium n’a reçu un message similaire ce mois-là — ciblage individuel donc, pas spray-and-pray. C’est un signal important : *quelqu’un sait que je travaille sur l’enquête*. Threat model révisé. Bascule vers Lockdown Mode aussi sur l’iPhone perso (qu’elle n’utilisait pas pour l’enquête, mais qui contient son carnet d’adresses personnel). Audit physique des appareils — rien d’anormal.

À ce stade, l’enquête continue mais Léa adopte une discipline encore renforcée : SimpleX uniquement pour Karim (plus aucun mail), tests MVT mensuels sur le Pixel (rien détecté), reboot deux fois par jour du Pixel, et iVerify installé sur l’iPhone perso (rien détecté).

#### A.6 Tentative de deepfake à T+9 mois

Cf. fil rouge Ch 34. Trois mois après l’incident phishing, Léa reçoit un appel vidéo SimpleX. Voix et image de Karim, ton paniqué : « Léa, j’ai besoin que tu rendes les documents, ils savent, c’est dangereux pour ma famille. » Léa applique le protocole pré-convenu : un proverbe convenu avec Karim au début de la relation, qu’elle lui demande de redire. Silence. Raccrochage côté appelant.

Léa contacte Karim sur SimpleX par texte. Karim répond : « Je n’ai pas appelé. Tout va bien. » Confirmation : deepfake. Léa et Karim audit complet de la stack — quelqu’un a obtenu des échantillons de la voix de Karim (possiblement via interception passive d’un appel téléphonique non sécurisé qu’il a passé à un proche, ou via achat de bases). L’image vidéo provient probablement de photos publiques de Karim (LinkedIn, photo officielle de son service).

Conséquences :

- Vérification que SimpleX lui-même n’est pas compromis : il ne l’est pas, l’attaquant n’a pas réussi à intercepter le canal, il a tenté un *appel sortant frauduleux* en se faisant passer pour Karim depuis un autre compte SimpleX en utilisant le lien public connu par certains tiers. Ce vecteur a été corrigé par SimpleX dans les versions ultérieures.
- Karim renforce sa discipline : aucun appel téléphonique avec proches sur sujets sensibles, audit téléphonique de son entourage qui pourrait être leveraged.
- Léa rappelle dans le protocole : *toute* communication d’urgence inattendue exige double vérification par canal séparé.

#### A.7 Publication coordonnée à T+12 mois

Préparation des 3 derniers mois :

- Caviardage destructif des documents publiés. Vérification croisée par deux confrères du consortium.
- Identification des éléments qui pourraient permettre par recoupement de remonter à Karim. Décision éditoriale : certaines informations sont retirées de la publication parce que trop révélatrices de la source — quitte à affaiblir certaines preuves. Le consortium adopte cette discipline collectivement.
- Préparation de Karim : mise en relation avec l’association *Maison des Lanceurs d’Alerte* en France, premier RDV avec un avocat spécialisé. Karim sait que son identité ne sera pas révélée publiquement par les médias, mais l’enquête interne dans son administration suite à la publication est probable.
- Soutien juridique pour Léa : convention écrite avec un avocat spécialisé en droit des médias, accessible 24/7 dans les 72h post-publication.

Publication simultanée sur les 12 médias partenaires à 06:00 CET. Couverture massive. Réaction politique : démissions, ouverture d’enquêtes parlementaires.

#### A.8 Post-publication : ce qui s’est passé

**Trois premiers jours** :

- Tentatives de doxxing de Léa sur deux canaux Telegram identifiés. Ses informations personnelles principales (adresse, téléphone) ne sont pas trouvables (domiciliation commerciale en place depuis 10 mois, ligne fixe résiliée 6 mois plus tôt). Quelques informations correctes mais anciennes circulent (poste précédent il y a 4 ans, photo d’identité publique). Effet limité.
- Harcèlement coordonné modéré sur X. Léa avait préparé : DMs fermés sauf abonnés, monitoring par un confrère, ne répond pas, archive pour preuves.
- Une notification Apple Threat Notification arrive sur son iPhone perso. Léa applique la procédure : isolement, contact Access Now, soumission Citizen Lab. Diagnostic 12 jours plus tard : présence d’IOCs Predator. Bascule iPhone neuf, threat model révisé en HVT permanent.

**Mois suivants** :

- Trois plaintes en diffamation contre le consortium, toutes rejetées en référé.
- Karim, identifié en interne (mais pas publiquement), placardisé puis détaché. Procédure aux prud’hommes pour licenciement abusif (lanceur d’alerte protégé). Soutien Maison des Lanceurs d’Alerte. Procédure en cours.
- Léa maintient sa stack durcie. Refus pendant 6 mois de toute interview ou apparition publique non strictement nécessaire. Reprend progressivement à 9 mois post-publication.

**12 mois post-publication** :

- Le commissaire visé est démissionnaire (a démissionné « pour raisons personnelles » à T+1 mois post-publication).
- Procédure pénale ouverte au niveau européen, ouverte également en Belgique et en France.
- Léa nominée à plusieurs prix journalistiques. Refuse une médiatisation personnelle excessive — discipline OPSEC en partie incompatible avec exposition.
- Karim, après procédure, obtient des indemnités significatives et une reconversion accompagnée. Son identité reste protégée publiquement.

#### A.9 Renvois croisés mobilisés

- **Threat modeling** : Ch 2 (cadre EFF), Ch 3 (taxonomie adversaires).
- **Réduction empreinte** : Ch 4 (cartographie), Ch 5-7 (OSINT défensif, data brokers, doxxing), Ch 8 (réseaux sociaux).
- **Compartimentation** : Ch 9 + Capstone 1.
- **Matériel et systèmes** : Ch 10-15 (Pixel cash, FDE, GrapheneOS, MacBook Air dédié).
- **Sessions sensibles** : Ch 16-18 + Capstone 2 (Tails, Qubes après bascule).
- **Réseau et navigation** : Ch 19-24 (Mullvad, Tor Browser, fingerprinting, multi-navigateurs).
- **Communications** : Ch 25-32 + Capstone 3 (SimpleX avec Karim, OnionShare pour transferts, PGP pour pivots, métadonnées rigoureusement traitées).
- **OPSEC humaine et juridique** : Ch 33-38 (phishing détecté, deepfake déjoué, Sapin II pour Karim, voyage, maintenance disciplinée).

-----

### Cas B — Sophie Roussel : activiste climat avant manifestation

#### B.1 Contexte

Sophie Roussel, 28 ans, activiste climatique française, exposée à une surveillance administrative et policière régulière en raison de sa participation à des mouvements visés par des dispositifs de renseignement de prévention. Participe à des manifestations dont certaines ont été qualifiées d’« interdites » ces dernières années. Domicile en colocation, vie sociale très active sur les réseaux sociaux militants. Elle s’apprête à participer à une manifestation à Paris contre un projet d’extension d’aéroport régional, manifestation que les organisateurs annoncent comme « pacifique mais désobéissante » — risque élevé d’arrestations, possibilité d’interpellations préventives, présence policière massive annoncée.

Adversaires plausibles :

- **Forces de l’ordre françaises** : capacité élevée localement, ordres judiciaires accessibles, IMSI catchers déployés régulièrement en manifestations (cas documentés par La Quadrature et amicus brief CEDH), reconnaissance faciale en croissance.
- **Infiltrés ou indicateurs** : capacité humaine, fait partie du modèle traditionnel français.
- **Contre-mouvements radicaux** : capacité faible, motivation modérée (harcèlement sur RS si Sophie est identifiée).
- **Employeur futur potentiel** : screening en cas de candidature, mais hors périmètre immédiat.

Hors périmètre :

- Résistance à un mandat de perquisition légal au domicile.
- Anonymat total dans son cercle militant.
- Empêcher la captation par caméra publique.

#### B.2 Préparation 72h avant manifestation

**Configuration de l’appareil de manifestation** :

- Pixel 4a d’occasion acheté il y a 18 mois (Sophie l’utilise spécifiquement pour les actions). GrapheneOS depuis l’achat.
- Profil utilisateur dédié manifestation : aucun compte personnel, contacts limités à : 1) avocat collectif activiste, 2) hotline juridique du Syndicat de la Magistrature, 3) un seul proche désigné référent (son colocataire), 4) le numéro d’urgence collectif de la manifestation.
- Apps : Signal (compte burner, créé avec une carte SIM prépayée — Sophie a vérifié que les SIM prépayées avec petit montant nominal restent achetables anonymement sous certaines conditions ; en pratique en France et Belgique, depuis 2017-2021, l’identité est demandée pour activation). Solution alternative : eSIM via service IP comme JMP.chat, financée en Monero. Signal username préféré.
- Briar installé en sauvegarde : permet communication Bluetooth/Wi-Fi local entre activistes voisins même si le réseau est coupé (cas en manifestation).
- Aucune photo, aucun document, aucun mail.
- Code de déverrouillage : 8 chiffres aléatoires, non lié à des données personnelles, *non biométrique* (Sophie a délibérément désactivé l’empreinte sur ce téléphone — la jurisprudence française permet à un officier de police de demander une biométrie, contraint à fournir code reste juridiquement nuancé).
- BFU forcé : Sophie va éteindre complètement le téléphone avant le départ et ne le déverrouillera que si nécessaire.

**Configuration physique** :

- Sac avec pochette Faraday (achetée chez un fournisseur sérieux, testée — un téléphone en pochette Faraday correcte doit perdre 100 % du signal cellulaire et Wi-Fi).
- Téléphone secondaire et utilitaire (clés perso, etc.) restés au domicile, vraiment éteints.
- Bloc-notes papier dans le sac : numéros importants (avocat, hotline, référent) en clair. Si l’appareil est saisi, ces numéros restent accessibles à Sophie via la mémoire ou ce papier.
- Ne porte pas son portefeuille personnel — porte uniquement une CB prépayée chargée avec 60 € en cash dans une carte distincte, et 100 € en espèces.

**Configuration personnelle** :

- Pas de bijoux distinctifs, pas de tatouage visible (sans contrainte vestimentaire excessive), vêtements anonymes (sweat à capuche, masque selon contexte).
- Sac à dos générique sans signe distinctif personnel.
- Pas d’agenda imprimé contenant des noms.

#### B.3 Brief avant manifestation

Sophie participe à un brief avec son collectif la veille au soir, en présentiel dans un local fermé, téléphones dans une pile à l’entrée (« phone stack ») pour éviter écoute et géolocalisation partagée. Au brief :

- Plan de déplacement, lieux de rendez-vous, points de regroupement en cas de dispersion.
- Identification des sympathisants membres du collectif vs participants extérieurs (vigilance infiltrés).
- Procédure en cas d’arrestation : utiliser le droit au silence, ne rien dire avant arrivée de l’avocat, appeler le numéro de hotline juridique (mémorisé).
- Rappel des règles : pas de photo du visage des camarades sans accord explicite, pas de live sur les RS personnelles.

#### B.4 Le jour J

Sophie part du domicile avec :

- Téléphone manifestation, éteint complètement, en pochette Faraday dans son sac.
- Bloc-notes papier avec numéros essentiels.
- 100 € cash + CB prépayée.
- Bouteille d’eau, lunettes (utiles contre gaz lacrymogène), masque, badge de presse non — Sophie n’est pas journaliste.

Au point de rendez-vous, elle sort le téléphone de la pochette Faraday, le démarre (toujours en BFU à ce stade puisqu’elle ne l’a pas déverrouillé). Active le mode avion. Ne déverrouille que si elle doit envoyer un signal au référent ou contacter l’avocat. Reste majoritairement en BFU pendant la manifestation.

À 14h30, premiers heurts. Charge des forces de l’ordre. Sophie se replie. Plus tard, elle est interpellée en bord de cortège, malgré son comportement défensif (elle ne portait pas d’arme et n’avait pas commis de délit). Interpellation préventive : maintenue en garde à vue 24h pour vérification.

#### B.5 Procédure d’arrestation

- Téléphone éteint, en BFU. Saisie possible mais accès des outils forensics commerciaux structurellement plus difficile en BFU qu’en AFU.
- Au commissariat, les officiers demandent à Sophie de communiquer son code de déverrouillage. Sophie connaît l’enjeu juridique : l’article 434-15-2 du Code pénal sanctionne le refus de remettre une convention secrète de déchiffrement (jusqu’à 3 ans et 270 000 €). La jurisprudence sur le statut exact du code de déverrouillage d’un téléphone par rapport à une « convention secrète » au sens du texte est nuancée et a varié selon les juridictions et les faits (cf. Ch 37.5). Sophie ne tente pas d’apprécier seule cette question juridique.
- Elle indique aux officiers qu’elle souhaite consulter son avocat avant de répondre à toute demande, et invoque son droit au silence sur les éléments pénalement intéressants en attendant. Son colocataire, prévenu à H+2 par la procédure d’urgence, a contacté la hotline juridique du collectif. L’avocat collectif activiste arrive après quelques heures.
- En présence de l’avocat, Sophie discute des suites à donner à la demande de code, en tenant compte de la nature des faits qui lui sont reprochés (le motif initial d’interpellation), des conséquences possibles d’une communication ou d’un refus, et de la stratégie pénale globale. La décision est une décision juridique individuelle prise en conseil — ce cours n’a pas vocation à la recommander dans un sens ou dans l’autre.
- Le téléphone est saisi pour analyse forensique. Garde à vue prolongée à 48h. Libération sans poursuites au-delà de la qualification résiduelle qui sera examinée ultérieurement.

#### B.6 Post-arrestation

- Le téléphone n’est pas restitué immédiatement (rétention pour expertise). Sophie considère le téléphone comme **brûlé** : ne sera plus jamais utilisé même si restitué (pour ne pas le réintégrer compromis dans sa stack).
- Sophie poursuit la procédure avec son avocat. Continue ses communications collectives via le téléphone du colocataire pour la suite.
- Audit de son domicile : son colocataire vérifie qu’il n’y a pas eu visite (les vis du laptop perso de Sophie ont leur vernis intact, photo macro inchangée).
- Procédure : selon l’évolution juridique du dossier, Sophie peut être convoquée ultérieurement pour audition sur différents motifs. L’analyse juridique reste menée par son avocat, qui décide avec elle de la stratégie au fur et à mesure.

#### B.7 Leçons

1. **BFU vraiment.** Le téléphone vraiment éteint à l’arrivée fait la différence forensique : ce qui se passe en garde à vue dépend en partie de l’état dans lequel l’appareil est saisi.
1. **Code mémorisé > biométrie** structurellement. Sous coercition (ou simplement face à une demande d’un officier qui peut techniquement utiliser une empreinte sans coopération active), le code mémorisé non biométrique reste plus difficile à obtenir.
1. **Préparation collective**. La hotline juridique, l’avocat collectif, le référent désigné : la résilience repose sur le réseau, pas sur l’individu seul. Toute question juridique en garde à vue se traite avec un avocat, pas seule.
1. **Téléphone brûlé après saisie**, jamais réintégré dans la stack.
1. **Compartimentation totale** : la vie quotidienne de Sophie n’a pas été affectée. Son téléphone personnel, ses comptes personnels, son ordinateur restent intacts et utilisables.

-----

### Cas C — Olivier Mercier : dirigeant de PME tech, cible d’espionnage économique

#### C.1 Contexte

Olivier Mercier, 47 ans, dirigeant d’une PME française de 80 salariés, secteur chiffrement matériel (HSM, modules pour le secteur bancaire et défense). Capital majoritairement détenu par lui et deux cofondateurs. Carnet de commandes croissant, partenariats avec deux grands groupes français du secteur défense. Récemment, intérêt commercial de la part d’acteurs étrangers (chinois, américain), avec offres de rachat non sollicitées.

Adversaires plausibles :

- **Concurrents internationaux** : capacité d’espionnage économique élevée (services étatiques chinois APT documentés visant la cybersécurité européenne, hacking commercial américain également).
- **Services russes** : capacité très élevée, motivation modérée à élevée (le secteur intéresse).
- **Concurrents européens directs** : capacité moyenne.
- **Criminalité financière** : capacité moyenne, motivation forte si visibilité Olivier (médias spécialisés ont publié son nom).
- **Insiders mécontents** : capacité variable, motivation possible (en cas de conflit interne, peu probable actuellement).

Hors périmètre :

- Espionnage industriel par voie commerciale légitime (intelligence économique standard).
- Diligence raisonnable d’acheteurs potentiels (avec accords NDA).

#### C.2 Posture initiale et audit

À T0, posture standard de PME française : Microsoft 365 entreprise, Windows 11 sur la plupart des postes, quelques Mac chez l’équipe créa/dev. Compte O365 admin global tenu par le DSI. Pas de MFA matériel généralisé. Pas de procédure formelle anti-BEC. Backups Veeam dans le DC local. Pas de Pegasus Test (jamais évoqué).

Audit par RSSI externe à T0+2 mois (Olivier a sollicité après les premières offres de rachat) :

- Vulnérabilités identifiées : MFA SMS sur certains comptes, exposition VPN historique, partage de mots de passe entre dirigeants, comptes Apple ID familiaux mélangés.
- Hygiène réseau : VLAN absent, IoT corporate (impression, salle de réunion) sur même VLAN que postes admin.
- Manque de procédures : pas de processus anti-BEC, pas de Threat Modeling formalisé.
- Surface email externe : Olivier accessible via 4 emails publics, signatures professionnelles riches en information (téléphone direct, fonctions, organigramme implicite).

Plan d’action à 6 mois validé en CODIR.

#### C.3 Architecture cible déployée

**Niveau dirigeants (Olivier + 2 cofondateurs)** :

- iPhones 15 Pro avec Lockdown Mode activé. ADP iCloud. Contact Key Verification entre dirigeants et exec team.
- MacBooks Pro avec FileVault, Lockdown Mode en voyage. Mises à jour disciplinées via Apple Business Manager.
- 1Password Famille + Business (partage de credentials sensibles avec audit). YubiKey 5C NFC (chacun avec 2 clés).
- Signal entre dirigeants (vérification Safety Numbers en présentiel). iMessage en backup.
- Email pro avec MFA matériel obligatoire.
- Travel kit : MacBook Air burner pour voyages sensibles (Chine, US sensibles), GrapheneOS sur Pixel burner.

**Niveau exec team (12 personnes)** :

- Même stack mais sans MacBook burner systématique.
- Formation BEC obligatoire trimestrielle.
- Procédure : tout virement > 10 k€ doit être validé par appel téléphonique sur ligne connue, jamais sur la seule base d’un email.

**Niveau salariés** :

- MFA via Microsoft Authenticator (push) sur tous les comptes O365.
- Politique de chiffrement disque automatique (BitLocker via Intune).
- Filtre email Microsoft Defender + sandbox pour pièces jointes.
- Formation phishing trimestrielle.

**Niveau infrastructure** :

- Segmentation VLAN : production / corporate / IoT / invités.
- Pare-feu sortant restrictif depuis le segment R&D.
- Bastion pour accès admin, journalisation.
- EDR (Microsoft Defender for Endpoint) déployé.
- SOC managé externalisé pour monitoring nuit/weekend.
- Backup 3-2-1 avec immutabilité + tests trimestriels.

**Politique BYOD** : pas de BYOD pour l’accès aux données sensibles. Mobile management via Intune sur les téléphones pro.

#### C.4 Incident à T+8 mois — tentative de BEC sophistiquée

Olivier est en déplacement à Tokyo pour un partenariat. Pendant son absence, la directrice financière (Sophie L.) reçoit un email d’Olivier. L’adresse semble correcte. Le sujet : « URGENT - virement Kazakhstan partenaire confidentiel ». Le message demande un virement de 380 000 € sur un IBAN kazakh, sous prétexte d’un acompte sur partenariat strictement confidentiel à conclure ce jour-là. Le ton est cohérent avec celui d’Olivier. Le mail est suivi 30 minutes plus tard d’un appel téléphonique sur ligne fixe de Sophie, prétendument d’Olivier, voix très similaire (deepfake vocal), insistant : « C’est confidentiel, ne dis rien aux autres, exécute. »

Sophie applique la procédure interne : tout virement > 10 k€ doit être validé par appel sur ligne *connue*. Sophie raccroche, appelle Olivier sur son numéro habituel — pas de réponse (Olivier est en réunion). Sophie attend. Olivier rappelle 2 heures plus tard sur sa ligne habituelle. Confirmation : il n’a rien demandé.

Investigation :

- Email envoyé depuis un domaine sosie (`mercieretassocies-fr.com` au lieu de `mercieretassocies.fr`). DKIM signé sur le domaine sosie.
- Appel téléphonique : numéro spoofé, voix probablement clonée (le SOC retrouve plus tard que la voix d’Olivier est disponible dans plusieurs interviews de presse sectorielle, suffisamment pour un voice clone qualité).
- Reconnaissance préalable : LinkedIn de Sophie L. comme DAF, mention publique du partenariat Tokyo prévu (Olivier l’avait évoqué en conférence 2 mois plus tôt), nom et numéro de Sophie public sur le site corporate.

Effet : pas de perte financière. Investigation par le SOC en lien avec ANSSI (PME stratégique secteur sécurité). Plainte déposée. Identification partielle : infrastructure compromise dans un pays tiers, attribution incertaine.

Réponse :

- Suppression du téléphone direct de Sophie du site corporate.
- Procédure renforcée : tout virement > 50 k€ exige double validation (Sophie + Olivier ou cofondateurs) avec hot-pin vocal convenu en présentiel, à renouveler trimestriellement.
- Communication interne : tous les collaborateurs sont informés du modus operandi. Formation spécifique BEC avec exemples concrets.
- Coordination avec ANSSI sur le partage d’IOCs (l’attaque cible peut être réutilisée sur d’autres entreprises du secteur).

#### C.5 Incident à T+11 mois — voyage Chine

Olivier doit se rendre à Shenzhen pour rencontrer un partenaire potentiel. Préparation :

- MacBook burner installé spécifiquement pour ce voyage, OS frais, aucun document d’entreprise, accès cloud E2EE (Proton Drive) à la demande.
- Pixel burner avec GrapheneOS, profil voyage. Aucun mail pro, aucun compte personnel. Signal username connu de 3 personnes (sa femme, son DSI, son associé).
- Pas de YubiKey emportée (laissée chez le DSI en France).
- Documents physiques minimaux. Notes professionnelles sur papier, à brûler à l’aéroport au retour.
- Avant départ : Olivier informe son DSI et son associé. Plan de communication : un check-in quotidien sur Signal à heure fixe. Si pas de check-in, escalade après 24h.

Pendant le voyage :

- À l’hôtel à Shenzhen, le MacBook burner reste en chambre uniquement quand il est dans le coffre de la chambre (modéré sécurisé, mais pas zero risque). Olivier le porte avec lui le plus souvent.
- Constatation au matin J+2 : la pochette de transport du MacBook a été manipulée (le pli systématique qu’Olivier fait sur la fermeture est défait). Pas de marquage évident sur le laptop lui-même.
- Olivier suspend l’usage du MacBook. Ne l’utilise plus pour les réunions sensibles ce jour. Bascule sur prise de notes papier.

Au retour en France :

- Le MacBook est livré directement à l’analyste forensique externe.
- Investigation : analyse du firmware, du SSD, des logs. Trace d’une connexion physique externe en heures non opérables (3h du matin local), pas de modification système identifiable (ou modification trop fine pour outils d’analyse standard).
- Décision conservative : le MacBook est physiquement détruit. Reset matériel impossible à garantir.
- Coût total du voyage en pertes matérielles : ~3 500 €. Coût en information sensible exfiltrée : zéro (le MacBook ne contenait aucun document sensible).

#### C.6 Posture à T+18 mois

L’entreprise a maintenant :

- Une posture cyber sérieuse, auditée annuellement.
- Une culture interne où la BEC est connue de tous, l’OPSEC voyage est partagée.
- Une relation établie avec l’ANSSI (programme DI/DCI pour entreprises stratégiques).
- Un budget annuel sécurité représentant 4-5 % du CA, contre 1 % à T0.

Les offres de rachat continuent. Olivier les évalue. Aucune compromission documentée. L’entreprise valorise sa posture cyber comme un actif (les acheteurs potentiels du secteur défense font des due diligences cyber poussées ; une bonne posture augmente la valorisation).

#### C.7 Leçons

1. **BEC > APT** comme threat principal pour PME, statistiquement et par retour d’expérience.
1. **Procédures de virement** : code anti-BEC, double validation par canal séparé. Non négociable.
1. **Voyage hostile = burner device**. Le coût d’un burner est inférieur au coût d’une compromission.
1. **Formation continue** des collaborateurs : sans la directrice financière disciplinée, l’entreprise aurait perdu 380 k€.
1. **Relation institutionnelle** : ANSSI pour la France, équivalents nationaux ailleurs. Une PME stratégique a accès à du conseil gratuit.
1. **Trade-off sécurité-business** : le sur-durcissement détruit l’agilité commerciale. La posture doit être proportionnée et soutenable.

-----

### Cas D — Particulier face à un ex-conjoint abusif

#### D.1 Contexte

Catherine, 39 ans, sépare de son conjoint Marc après 8 ans de relation marquée par violences psychologiques et économiques croissantes. Marc, ingénieur informatique de formation, a eu accès à tous les comptes et appareils du couple pendant la relation. Il a installé des outils de tracking sur ses appareils (Catherine suspecte mais ne l’a pas vérifié), connaît les mots de passe de la plupart des comptes, est ajouté comme contact de récupération sur plusieurs services, a accès au compte iCloud familial. Catherine quitte le domicile conjugal pour s’installer dans un studio. Elle craint :

- Que Marc accède à ses communications et localisation.
- Que Marc utilise leurs comptes joint contre elle dans la procédure judiciaire en cours.
- Que Marc l’agresse physiquement (un incident a déjà eu lieu, plainte déposée).
- Que Marc fasse pression sur leurs enfants (garde partagée en cours d’attribution).

Adversaires plausibles :

- **Marc lui-même** : capacité technique réelle, motivation très forte, accès historique considérable.
- **Cercle social et familial de Marc** : capacité variable, motivation modérée.
- **Plateformes et services** : non hostiles mais procédures de récupération exploitables par Marc.

Hors périmètre :

- Disparition complète (Catherine doit rester atteignable juridiquement, dans l’intérêt des enfants).
- Anonymat sur les comptes nominatifs (bancaires, administratifs).

**Particularité éditoriale** : ce profil est sous-traité dans la majorité des cours cyber, qui se focalisent sur l’étatique. Pour une fraction non négligeable de la population — femmes essentiellement — c’est *le* threat model réel.

#### D.2 Procédure d’urgence (J0-J7)

**Jour 0 (jour de la séparation effective)** :

- Catherine quitte le domicile avec ses affaires essentielles. Elle conserve son téléphone actuel pour le moment, mais avec discipline (ne pas s’y connecter à des comptes nouveaux).
- Établissement d’un téléphone neuf, acheté cash dans un magasin, opérateur différent (nouveau numéro non communiqué à Marc).
- Ce téléphone neuf reçoit immédiatement une nouvelle SIM nominale Catherine (KYC normal, pas tentative d’anonymisation — Catherine veut être joignable juridiquement, et c’est plus discret de fonctionner avec un compte normal).

**Jour 1** :

- Audit du téléphone précédent par une personne tierce de confiance (un cousin technicien). Recherche de stalkerware : examen des applications installées (sur Android avec écran de gestion des apps en mode usage avancé ; sur iOS, gestion des profils MDM installés). Résultat : présence d’une application déguisée en « calculatrice » (mSpy renommé), profil MDM Apple installé permettant suivi de localisation. Marc avait installé.
- Catherine décide : *ne pas* effacer immédiatement le téléphone (preuves utiles pour la procédure pénale en cours sur violences). Photos des installations malveillantes, dépôt de plainte additionnelle pour violation de vie privée et installation de logiciel espion (cf. art. 226-1 et 323-1 CP).

**Jour 2-3** :

- **Tous les mots de passe critiques changés** depuis le nouveau téléphone (ou depuis un cybercafé sécurisé) :
  - Apple ID Catherine (sortie du « Family Sharing » avec Marc, création nouveau compte distinct si elle migre vers iPhone neuf).
  - Compte Google.
  - Compte Microsoft.
  - Comptes bancaires (et procédure spécifique avec la banque pour bloquer Marc de l’accès en ligne sur comptes joints).
  - Messageries : Signal, WhatsApp réinstallés sur nouveau téléphone, anciennes sessions révoquées.
  - Réseaux sociaux : changement de mots de passe, retrait de Marc des contacts (Facebook, Instagram, LinkedIn).
  - Compte impôts, sécurité sociale, et autres administratifs.
  - Email principal (Gmail Catherine) : mot de passe, MFA, contacts de récupération vérifiés (retrait de Marc s’il était listé), questions de récupération mises à jour.
- **Contacts de récupération audités** : Apple Account Recovery Contacts (retrait de Marc s’il l’avait été), Google (idem).
- **Numéro de récupération** : remplacement par le nouveau numéro.
- **Comptes joints non clos immédiatement** (procédure légale en cours pour le partage), mais surveillés activement et logs préservés.

**Jour 4-5** :

- **Réseau social** : Facebook → profil verrouillé, audit des amis (suppression du cercle de Marc), publications passées masquées, retrait de toutes les photos taguées par Marc.
- **Localisation** : audit Find My iPhone et services Google (retrait du partage de localisation avec Marc s’il existait). Catherine a constaté qu’elle partageait sa localisation avec Marc sur Google Maps : retiré.
- **AirTags et trackers** : Catherine fait scan de ses affaires (sac, voiture, vêtements neufs) avec son téléphone neuf qui détecte les AirTags inconnus. iOS et Android (depuis 2023-2024) alertent en cas de tracker tiers suivant. Catherine trouve un AirTag dans sa voiture (Marc avait accès au véhicule). Retrait et archivage pour la procédure pénale.

**Jour 6-7** :

- Achat d’un PC neuf si ressources le permettent (laptop d’entrée de gamme, FileVault/BitLocker activés immédiatement, comptes neufs).
- Configuration d’un gestionnaire de mots de passe (Bitwarden gratuit) avec mots de passe nouveaux et uniques pour tous les comptes.
- Configuration de MFA matériel ou TOTP partout où possible (YubiKey si Catherine peut investir, sinon Aegis Authenticator sur le téléphone neuf).

#### D.3 Mois 1-3 : stabilisation

**Audit physique du studio** :

- Vérification absence de caméras cachées (achetée pour 30 € sur Amazon, détecteur RF + lentille caméra). Aucune trouvée.
- Vérification absence d’écoute (microphones discrets) — généralement par scan RF et inspection visuelle.
- Serrure changée (responsabilité du bailleur, demandée explicitement).

**Audit numérique continu** :

- Connexions inhabituelles sur comptes ? Catherine surveille hebdomadaire les sessions actives.
- Alertes de tentative de connexion ? Activées sur tous les comptes principaux.
- Email principal en monitoring HaveIBeenPwned (notification de nouvelle fuite — particulièrement utile si Marc tenterait de la doxxer).

**Communications avec les enfants** :

- Les enfants utilisent leurs propres téléphones (avec accord parental). Catherine et eux communiquent via Signal avec disappearing messages 30 jours pour les conversations non essentielles. Pas de discussion juridique avec les enfants par messages.
- En garde partagée, Catherine n’écrit pas aux enfants sur des sujets sensibles via canaux que Marc pourrait surveiller.

**Soutien externe** :

- Association locale (CIDFF en France, équivalents locaux) pour soutien juridique et psychologique.
- Avocate spécialisée violences conjugales.
- Psychologue spécialisée trauma post-séparation.
- Réseau de soutien (deux amies, une sœur) — un seul cercle de confiance restreint, choisi soigneusement (les autres « amis » communs avec Marc ne sont pas mis dans le secret).
- Coalition Against Stalkerware ressources internationales.

#### D.4 Incident à M+4 — tentative d’accès au compte Gmail

Catherine reçoit une notification : « Une tentative de connexion à votre compte Google a été refusée. Emplacement : [ville de Marc]. Heure : 22h17 ». Plus tard, deuxième notification similaire. Marc tente d’accéder. La MFA matérielle (YubiKey configurée) bloque.

Réponse :

- Catherine vérifie qu’aucune session n’est active.
- Changement préventif du mot de passe.
- Documentation de l’incident : capture des notifications, ajout au dossier juridique.
- Signalement à l’avocate qui transmet à l’instruction.

#### D.5 Incident à M+8 — tentative de doxxing

Marc, dans le contexte de la procédure de divorce conflictuel et de garde, publie sur un blog familial accessible au cercle élargi des informations privées de Catherine : sa nouvelle adresse, son nom d’employeur, des éléments de sa vie privée. Tentative manifeste d’intimidation.

Réponse :

- Capture immédiate (preuve), avec horodatage notarié si possible.
- Signalement à la plateforme.
- Dépôt de plainte additionnelle (atteinte à la vie privée, art. 226-1 ; et possiblement harcèlement).
- Demande de droit à l’effacement au blog hébergeur.
- Communication contrôlée avec l’employeur (Catherine prévient son N+1 de la situation pour qu’il sache à quoi s’attendre, sans détails).

Effet : le blog est retiré sous 72h après signalement à l’hébergeur. La plainte avance, le dossier de violences conjugales se renforce.

#### D.6 Mois 12+ : nouvelle normalité

Un an après la séparation, Catherine a :

- Une stack cyber complètement renouvelée, indépendante de Marc.
- Une procédure judiciaire qui avance (Marc condamné pour les violences initiales, garde partagée modifiée en sa défaveur).
- Une posture de monitoring qui devient routine sans plus être anxiogène.
- Un soutien externe pérenne.

Elle peut commencer à relâcher progressivement la vigilance (sans baisser la garde sur l’hygiène cyber de base), à reconstruire sa vie sociale et professionnelle.

#### D.7 Leçons

1. **L’adversaire de proximité est sous-évalué**. Marc avait des capacités modérées techniquement mais une connaissance préalable totale qui compensait largement.
1. **La rupture cyber doit accompagner la rupture sentimentale**. Sans cela, l’ex-conjoint conserve un accès massif.
1. **La détection de stalkerware** doit être une étape précoce, pas une découverte tardive. Coalition Against Stalkerware fournit ressources et outils.
1. **Les preuves comptent** : ne pas effacer trop vite les éléments compromis qui constituent des preuves utiles à la procédure pénale.
1. **Le soutien collectif** : associations, avocate, psychologue, réseau de proches choisis. Ne pas s’isoler. La défense individuelle pure ne suffit pas.
1. **Patience et durée** : la stabilisation prend des mois, pas des semaines. La posture doit être soutenable sur la durée.

-----


## Annexes

-----

### Annexe 1 — Glossaire (120+ termes)

**A**

**ADINT (Advertising Intelligence)** — Exploitation de l’écosystème publicitaire numérique comme source de renseignement. Utilise notamment le ciblage publicitaire, le RTB, les identifiants publicitaires mobiles, les données de localisation et les bidstream data pour profiler, suivre ou cibler des personnes ou groupes. Les données publicitaires peuvent produire un risque physique ou opérationnel : identification d’agents, domiciles, trajets, lieux sensibles, patterns of life..

**AFU (After First Unlock)** — État d’un appareil mobile après le premier déverrouillage depuis allumage. Beaucoup de clés sont en mémoire ; vulnérabilité forensique élevée par rapport à BFU.

**Advanced Data Protection (ADP)** — Mode iCloud chiffrant en E2EE la majorité des données (Drive, photos, sauvegardes, notes, signets). Hors-périmètre : mail, contacts, calendrier. Nécessite tous les appareils Apple à jour et une clé de récupération.

**Adversary** — Acteur dont les actions contre toi sont à anticiper. Caractérisé par capacité, motivation, probabilité.

**Adversary of proximity** — Adversaire proche (ex-conjoint, harceleur, employeur intrusif). Faible capacité technique typique, mais forte connaissance préalable.

**Air gap** — Isolation physique d’un système (aucune connexion réseau). Mesure forte pour secrets long terme, coûteuse au quotidien.

**AmneziaVPN** — Client VPN open source multi-protocoles permettant d’utiliser Amnezia Premium ou de déployer un VPN self-hosted sur un VPS. Pertinent surtout pour l’anti-censure, le contournement de DPI et les configurations utilisant AmneziaWG, XRay Reality, Shadowsocks ou OpenVPN over Cloak.

**AmneziaWG** — Fork de WireGuard conçu pour rendre le trafic plus difficile à détecter et bloquer par des systèmes de DPI. Utile en environnement censuré, mais ne transforme pas un VPN en réseau d’anonymat.

**AppArmor** — Modèle de Mandatory Access Control sous Linux (Debian, Ubuntu, SUSE). Profils par application.

**APT (Advanced Persistent Threat)** — Acteur étatique ou paraétatique avec capacité, ressource et patience pour campagnes ciblées longues.

**Argon2id** — Fonction de dérivation de clé (KDF) moderne, résistante aux ASIC. À privilégier dans gestionnaires de mots de passe et FDE.

**Attribution** — Conclusion qu’une action est l’œuvre de telle personne ou entité. Niveau de confiance variable.

**B**

**BFU (Before First Unlock)** — État d’un appareil après redémarrage, avant déverrouillage. La plupart des clés sont scellées. Forensiquement le plus protecteur.

**Bidstream data** — Données transmises dans l’écosystème publicitaire lors des enchères en temps réel : appareil, IP, localisation, contexte, application, langue, horaires, segments d’intérêt, etc. Ces données peuvent être utilisées à des fins publicitaires, mais aussi détournées à des fins de renseignement.

**BEC (Business Email Compromise)** — Fraude par usurpation d’identité d’un dirigeant pour demande de virement. Pertes mondiales en milliards.

**BlackLotus** — Bootkit UEFI (2022-2023) contournant Secure Boot via signature vulnérable. Illustre que Secure Boot n’est pas inviolable.

**Bridge (Tor)** — Relais Tor non publié, utilisé pour contourner le blocage des relais publics dans pays censurés.

**C**

**C2PA (Coalition for Content Provenance and Authenticity)** — Standard de provenance cryptographique pour images/vidéos.

**Canvas fingerprint** — Technique de fingerprinting basée sur le rendu d’une image cachée. Variations GPU et drivers produisent signature unique.

**Capitalisme de surveillance** — Modèle économique fondé sur la collecte et exploitation massive de données personnelles.

**Chat Control / CSAR** — Proposition de règlement UE visant le scan des communications avant E2EE. Bloqué depuis 2022 en négociation.

**Cold boot attack** — Extraction de clés depuis la RAM peu après extinction (mémoire persiste quelques secondes).

**Compartmentation (compartimentation)** — Architecture défensive consistant à séparer les activités en compartiments étanches.

**Contact Key Verification** — Mécanisme iMessage (iOS 17.2+) de vérification cryptographique des clés contacts.

**Coreboot** — Firmware open source remplaçant les firmwares constructeur sur certains matériels.

**Corrélation (surface de)** — Ensemble des points par lesquels deux identités ou activités peuvent être reliées.

**Cryptomator** — Outil de chiffrement de dossier côté client, transparent, multi-plateforme.

**D**

**Dangerzone** — Outil FPF qui reconvertit un PDF en PDF propre via conteneur isolé, supprimant tout contenu actif et métadonnée.

**Deepfake** — Contenu synthétique (image, vidéo, audio) généré par IA, imitant une personne réelle.

**Disposable VM (dispVM)** — VM Qubes éphémère, créée à la demande, détruite à la fermeture.

**DKIM (DomainKeys Identified Mail)** — Signature cryptographique des emails par domaine émetteur, pour vérifier authenticité.

**DMARC (Domain-based Message Authentication, Reporting and Conformance)** — Politique de validation email combinant SPF et DKIM, avec gestion des échecs.

**DoH / DoT (DNS over HTTPS / DNS over TLS)** — Protocoles de DNS chiffré, à privilégier pour confidentialité des résolutions.

**Double ratchet** — Algorithme combinant forward secrecy et post-compromise security. Base de Signal Protocol.

**Doxxing** — Publication malveillante d’informations personnelles identifiantes sur une cible.

**DRM (Digital Rights Management)** — Hors périmètre privacy mais souvent confondu. Note : certains DRM (Widevine, etc.) collectent des données.

**E**

**E2EE (End-to-End Encryption)** — Chiffrement bout en bout : seuls expéditeur et destinataire peuvent lire le contenu.

**ECH (Encrypted Client Hello)** — Extension TLS qui chiffre le SNI dans le ClientHello.

**EXIF (Exchangeable Image File Format)** — Métadonnées intégrées aux photos (GPS, modèle, date).

**ExifTool** — Outil de référence pour lire/écrire les métadonnées de fichiers.

**Evil maid** — Attaque par accès physique temporaire (typiquement chambre d’hôtel) modifiant l’appareil.

**F**

**FDE (Full Disk Encryption)** — Chiffrement complet du disque (BitLocker, FileVault, LUKS).

**FIDO2 / WebAuthn** — Standard d’authentification cryptographique forte, base des passkeys.

**Fingerprint (navigateur)** — Signature unique dérivée des caractéristiques de ton navigateur et appareil.

**Forward secrecy** — Propriété cryptographique : la compromission d’une clé ne permet pas de déchiffrer le passé.

**fwupd** — Outil Linux pour mises à jour firmware via le LVFS.

**G**

**GrapheneOS** — OS Android durci et dégooglisé, sur Pixel exclusivement.

**Guard (Tor)** — Premier relais d’un circuit Tor, connaît ton IP réelle.

**H**

**Hardening (durcissement)** — Renforcement de la configuration sécurité d’un système.

**HaveIBeenPwned** — Service de référence pour identifier si un email/téléphone apparaît dans des fuites publiques.

**Heads** — Firmware sécurisé basé sur Coreboot, avec vérification cryptographique au démarrage.

**HVT (High Value Target)** — Cible à forte valeur pour adversaire ressourcé.

**I**

**IDFA / AAID** — Identifiants publicitaires iOS et Android. Désactivables.

**IMSI catcher** — Faux relais cellulaire captant les IMSI à proximité (Stingray, DRT box).

**IOC (Indicator of Compromise)** — Marqueur technique permettant d’identifier une compromission.

**iVerify** — Application de monitoring de sécurité iOS/Android, détection de spyware connus.

**K**

**KDF (Key Derivation Function)** — Fonction transformant un mot de passe en clé cryptographique. Argon2id, scrypt, PBKDF2.

**Killswitch (VPN)** — Interruption du trafic si le tunnel VPN tombe. Indispensable.

**L**

**LCEN** — Loi française de 2004 consacrant la liberté de cryptographie pour usage personnel.

**LinkedIn (réseau social)** — Plateforme professionnelle, source OSINT majeure.

**Linkability** — Possibilité de relier deux activités à la même entité (dimension LINDDUN).

**LINDDUN** — Taxonomie de menaces privacy (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Noncompliance).

**Lockdown Mode (iOS)** — Mode haute sécurité iOS désactivant des fonctionnalités exploitées par spyware mercenaires.

**LogoFAIL** — Vulnérabilité firmware (2023) dans le parsing d’images au démarrage, contournant Secure Boot.

**LUKS** — Standard Linux de chiffrement de disque.

**M**

**MAC randomization** — Génération d’adresses MAC aléatoires par les OS modernes pour réduire le tracking Wi-Fi/BT.

**MAID (Mobile Advertising ID)** — Identifiant publicitaire mobile. IDFA sur iOS, AAID sur Android. Conçu pour le ciblage publicitaire, mais exploitable comme pivot de corrélation dans des scénarios ADINT.

**Malvertising** — Usage de publicités en ligne pour diffuser du contenu malveillant, rediriger vers un site piégé ou préparer une attaque ciblée.

**Mandatory Access Control (MAC)** — Modèle de contrôle d’accès obligatoire (AppArmor, SELinux).

**Matrix** — Protocole de messagerie fédérée open source.

**MAT2 (Metadata Anonymisation Toolkit v2)** — Outil de nettoyage de métadonnées de fichiers.

**Mercenary spyware** — Spyware vendu commercialement à des États (Pegasus, Predator, Graphite).

**Mixnet** — Réseau d’anonymisation qui mélange les flux, ajoute de la latence et parfois du bruit réseau pour réduire l’analyse de trafic. Différent de Tor : Tor route en oignon avec trois relais ; un mixnet cherche surtout à réduire la corrélation temporelle et volumétrique.

**MFA (Multi-Factor Authentication)** — Authentification multifacteurs. Hiérarchie : FIDO2 > TOTP > SMS.

**Mullvad** — Fournisseur VPN suédois, référence privacy. Sans compte utilisateur.

**MVT (Mobile Verification Toolkit)** — Outil Amnesty pour détecter spyware (Pegasus, Predator) dans sauvegardes mobiles.

**N**

**Need-to-know** — Principe : partager une information sensible uniquement avec ceux qui en ont besoin pour leur rôle.

**Nextcloud** — Cloud auto-hébergé open source.

**NymVPN** — VPN décentralisé basé sur l’écosystème Nym. Propose un mode Fast en deux sauts et un mode Anonymous en cinq sauts via mixnet avec ajout de bruit. Pertinent pour la protection contre l’analyse de métadonnées réseau, avec un coût en latence selon le mode.

**O**

**OnionShare** — Outil de partage de fichiers via service onion temporaire.

**OPSEC (Operational Security)** — Discipline d’identification, contrôle et protection des indicateurs sensibles.

**OSINT (Open Source Intelligence)** — Collecte d’information via sources ouvertes.

**OSINT défensif** — Audit de soi-même par OSINT pour mesurer son exposition publique.

**P**

**Passkey** — Implémentation grand public de WebAuthn (clés cryptographiques remplaçant les mots de passe).

**Pegasus** — Spyware mercenaire de NSO Group, déployé contre journalistes, activistes, opposants.

**PGP / GPG** — Standard de chiffrement asymétrique pour email et fichiers.

**Phishing** — Tentative d’usurpation pour obtenir credentials ou exécution. Variantes : spear, whaling, smishing, vishing, quishing.

**Pluton (Microsoft)** — Coprocesseur de sécurité Microsoft intégré dans CPU récents.

**Post-compromise security (PCS)** — Capacité d’un protocole à se rétablir après compromission de clé.

**Predator** — Spyware mercenaire d’Intellexa/Cytrox, concurrent de Pegasus.

**Proton (Mail, Drive, VPN)** — Suite suisse de services E2EE par design.

**Pseudonymat** — Usage d’un nom de substitution stable. Distinct de l’anonymat.

**Q**

**Qubes OS** — OS basé Xen compartimentant chaque activité en VMs séparées.

**R**

**Recall (Microsoft)** — Fonctionnalité Windows 11 sur Copilot+ PCs, opt-in, capturant régulièrement l’écran et indexant le contenu par IA pour recherche ultérieure. Snapshots et index stockés localement, chiffrés et liés à la TEE. Controversée pour les implications privacy structurelles d’une telle base.

**Ring signature** — Primitive cryptographique de Monero pour masquer l’expéditeur.

**RGPD** — Règlement Général sur la Protection des Données (UE).

**RTB (Real-Time Bidding)** — Système d’enchères publicitaires en temps réel. Lorsqu’un utilisateur ouvre une page ou une application, des informations sur son profil publicitaire sont transmises à des annonceurs potentiels, qui enchérissent automatiquement pour afficher une publicité.

**S**

**Safety Numbers (Signal)** — Chaîne dérivée des clés permettant de vérifier l’identité d’un contact.

**Sandbox** — Isolement d’une application dans un environnement contrôlé (Flatpak, Firejail, Windows Sandbox).

**Sapin II** — Loi française de protection des lanceurs d’alerte (2016, modifiée 2022).

**Secure Boot** — Vérification cryptographique de la chaîne de démarrage UEFI.

**Secure Enclave** — Coprocesseur de sécurité Apple intégré aux SoC Apple Silicon.

**SecureDrop** — Plateforme open source pour soumission anonyme de documents aux rédactions.

**SELinux** — Modèle MAC sous Linux (Fedora, RHEL).

**SimpleX** — Messagerie E2EE sans identifiant utilisateur global.

**SIM swap** — Fraude consistant à faire transférer ta ligne sur la SIM d’un attaquant.

**Signal** — Référence E2EE, protocole open source audité, déployé à 100M+ utilisateurs.

**SNI (Server Name Indication)** — Extension TLS qui transmet en clair le nom de domaine joint.

**Snowflake** — Transport obfusqué Tor utilisant des proxys volontaires WebRTC.

**Spoofing** — Usurpation d’identité (catégorie STRIDE).

**Stalkerware** — Logiciel espion commercial visant le tracking de partenaires (mSpy, FlexiSpy).

**STRIDE** — Taxonomie de menaces sécurité (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).

**Stylométrie** — Analyse statistique du style d’écriture pour identification d’auteur.

**Surface d’attaque** — Ensemble des points par lesquels un adversaire peut t’attaquer techniquement.

**Surface d’exposition** — Ensemble des informations collectables sur toi sans attaque.

**Surveillance, capitalisme de** — Cf. capitalisme de surveillance.

**T**

**Tails** — OS live amnésique routant tout via Tor.

**Threat model** — Modèle structuré décrivant actifs, adversaires, mesures.

**TLS (Transport Layer Security)** — Protocole de chiffrement en transit, base de HTTPS.

**Tor** — Réseau d’anonymisation par routage en oignon à trois sauts.

**TOTP (Time-based One-Time Password)** — Code MFA généré par algorithme synchronisé en temps (Authenticator apps).

**TPM (Trusted Platform Module)** — Coprocesseur de sécurité pour stockage de clés et mesure de boot.

**Truecaller** — Service tiers révélant les identités derrière numéros de téléphone (intrusif).

**V**

**Vanadium** — Navigateur intégré à GrapheneOS, Chromium durci.

**Vault qube** — Qube Qubes offline pour secrets (gestionnaire de mots de passe, clés PGP).

**Vault7 (Wikileaks)** — Fuite de capacités CIA (2017), illustre capacités étatiques.

**VeraCrypt** — Conteneur chiffré portable, héritier de TrueCrypt.

**Vishing** — Phishing par appel vocal.

**VLAN (Virtual LAN)** — Segmentation réseau logique.

**VPN (Virtual Private Network)** — Tunnel chiffré vers serveur distant.

**Vulnerability** — Faiblesse exploitable d’un système.

**W**

**Wayland** — Protocole de gestion d’affichage Linux remplaçant X11, avec isolation des fenêtres.

**WebAuthn** — Standard d’authentification web cryptographique.

**Whaling** — Spear phishing visant un dirigeant.

**Whonix** — OS d’anonymisation Tor en architecture Gateway/Workstation.

**WireGuard** — Protocole VPN moderne, rapide, compact.

**Y**

**Yellow dots** — Micro-points jaunes invisibles imprimés par imprimantes couleur pour tracking forensique.

**YubiKey** — Clé matérielle FIDO2 / WebAuthn / OpenPGP.

**Z**

**Zed!** — Conteneur chiffré francophone, secteur public/justice.

**Zero-click** — Exploit nécessitant aucune interaction utilisateur (typique des spywares mercenaires sur iMessage, WhatsApp).

**Zero-day** — Vulnérabilité non publique, sans patch disponible.

-----

### Annexe 2 — Cheat sheets opérationnels

#### 2.1 Audit initial en 90 minutes

1. HaveIBeenPwned : emails principaux + numéros de téléphone.
1. Google / Bing / DuckDuckGo : recherche nom complet, email, pseudos.
1. Sherlock ou WhatsMyName : recherche pseudonymes.
1. Reverse image (Yandex, Google Lens) sur photos publiques.
1. Audit Google Account → Sécurité (sessions, MFA, récupération).
1. Audit Apple ID → Appareils.
1. Audit iCloud → ADP activée ? Backup E2EE ?
1. Audit permissions mobiles (Localisation, Micro, Caméra, Photos, Contacts).
1. Audit gestionnaire de mots de passe : doublons, faibles, sans MFA.
1. Liste des comptes critiques sans MFA matériel.

#### 2.2 Préparation manifestation

- Téléphone dédié GrapheneOS, profil manifestation, BFU avant départ.
- Code de déverrouillage 8 chiffres, biométrie désactivée.
- Faraday bag dans le sac.
- Numéros importants sur papier.
- Téléphone perso vraiment éteint chez soi.
- 100 € cash + CB prépayée.
- Pas de carte d’identité contenant adresse précise inutile.

#### 2.3 Préparation voyage frontalier sensible

- Burner device (ou device durci, ADP, Lockdown Mode, FileVault).
- Données sensibles évacuées en cloud E2EE (Proton Drive).
- Sessions critiques révoquées.
- BFU absolu avant passage frontière.
- Photos macro des composants internes pour comparaison retour.
- Vis vernies pour détection d’intrusion physique.

#### 2.4 Réception document sensible

1. Vérifier provenance (Safety Numbers, canal authentifié).
1. Hash SHA-256 confirmé hors bande.
1. Environnement isolé (Tails ou dispVM).
1. Dangerzone pour PDF.
1. ExifTool / MAT2 pour métadonnées.
1. Archivage chiffré.

#### 2.5 Compte compromis suspecté

1. Mot de passe changé depuis appareil sain.
1. Toutes sessions actives révoquées.
1. Audit modifications récentes (mail récup, MFA, filtres).
1. MFA matériel activé.
1. Comptes liés vérifiés.
1. Communication aux contacts si phishing envoyé.
1. Plainte si dommages.

#### 2.6 Spyware mercenaire suspecté

1. Mode avion immédiat + faraday bag.
1. Ne pas redémarrer (perte d’IOC).
1. Access Now Digital Security Helpline.
1. Sauvegarde locale (iTunes/Quicktime).
1. Soumission MVT et Citizen Lab.
1. Appareil neuf, comptes audités, threat model révisé.

#### 2.7 Sauvegarde 3-2-1 minimale

- Disque local (chiffré).
- Cloud E2EE (Proton Drive, Tresorit, ou chiffré côté client).
- Externe en lieu sûr (chez avocat, parent, coffre).
- Test de restauration trimestriel.

-----

### Annexe 3 — Matrice d’outils de référence (2025-2026)

#### Communication

|Outil             |Type               |Usage                 |Notes                                               |
|------------------|-------------------|----------------------|----------------------------------------------------|
|**Signal**        |Messagerie E2EE    |Quotidien             |Référence. Username permet de ne plus exposer numéro|
|**SimpleX**       |Messagerie E2EE    |Sources, HVT          |Pas d’identifiant utilisateur global                |
|**Briar**         |Messagerie P2P     |Manifestation, offline|Bluetooth/Tor, sans serveur                         |
|**iMessage**      |E2EE (Apple)       |Quotidien Apple       |Contact Key Verification recommandée                |
|**Matrix/Element**|Fédéré             |Communautés           |E2EE optionnelle, métadonnées chez homeserver       |
|**WhatsApp**      |E2EE (Meta)        |Compatibilité large   |Métadonnées chez Meta. Sauvegarde E2EE à activer    |
|**Telegram**      |Pas E2EE par défaut|Diffusion             |Seuls Secret Chats E2EE                             |

#### Email

|Outil                    |Type                       |Notes                             |
|-------------------------|---------------------------|----------------------------------|
|**Proton Mail**          |E2EE entre Proton          |Suisse. Alias SimpleLogin intégrés|
|**Tuta**                 |E2EE complet (objet inclus)|Allemagne. Pas d’IMAP             |
|**Mailbox.org**          |Email propre + PGP         |Allemagne                         |
|**Fastmail**             |Mail propre sans E2EE      |Australie (Five Eyes)             |
|**SimpleLogin / Addy.io**|Alias email                |À ajouter en front de tout        |

#### Navigateurs

|Outil                          |Usage                                |
|-------------------------------|-------------------------------------|
|**Tor Browser**                |Anonymat (ne jamais modifier)        |
|**Mullvad Browser**            |Anti-fingerprint quotidien (sans Tor)|
|**Brave**                      |Quotidien Chromium durci             |
|**Firefox + uBlock + arkenfox**|Quotidien Firefox durci              |
|**LibreWolf**                  |Firefox durci pré-configuré          |
|**Vanadium**                   |Mobile GrapheneOS                    |

#### VPN

| Outil                               | Usage principal                                      | Notes                                                                                                                                                    |
| ----------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mullvad VPN**                     | Privacy quotidienne                                  | Suède. Compte numéroté sans email. Paiement cash/Monero possible. No-log détaillé. Très bon choix par défaut.                                            |
| **IVPN**                            | Privacy quotidienne                                  | Gibraltar. Audits réguliers. Cure53. Très bon positionnement privacy.                                                                                    |
| **Proton VPN**                      | Privacy + confort                                    | Suisse. Bon compromis grand public, écosystème Proton, plan gratuit sérieux.                                                                             |
| **NymVPN**                          | Métadonnées / mixnet                                 | VPN décentralisé. Fast mode 2-hop, Anonymous mode 5-hop mixnet. Plus ambitieux contre l’analyse de trafic, mais plus jeune et potentiellement plus lent. |
| **AmneziaVPN**                      | Anti-censure / self-host                             | Multi-protocoles. AmneziaWG, XRay Reality, Shadowsocks, OpenVPN over Cloak. Très pertinent contre DPI et blocage VPN.                                    |
| **À éviter pour profils sensibles** | NordVPN/ExpressVPN pour HVT, VPN gratuits, Surfshark | Risque de logs, revente de données, juridiction opaque, propriété complexe.                                                                              |

#### Gestionnaires de mots de passe

|Outil          |Notes                                                          |
|---------------|---------------------------------------------------------------|
|**Bitwarden**  |Open source. Audits réguliers. Vaultwarden self-hosted possible|
|**KeePassXC**  |100 % local, sync manuelle                                     |
|**1Password**  |Commercial canadien. UX excellent                              |
|**Proton Pass**|Intégré Proton                                                 |
|**À éviter**   |LastPass (fuites 2022-2023)                                    |

#### Clés matérielles

|Outil               |Notes                           |
|--------------------|--------------------------------|
|**YubiKey 5 series**|Référence commerciale           |
|**Nitrokey 3**      |Open source hardware (Allemagne)|
|**SoloKey**         |Open source plus militant       |

#### Cloud E2EE

|Outil                      |Notes                               |
|---------------------------|------------------------------------|
|**Proton Drive**           |Suisse, E2EE par design             |
|**Tresorit**               |Suisse, focalisé pro                |
|**Mega**                   |Nouvelle-Zélande                    |
|**Cryptomator**            |Surcouche E2EE sur cloud generaliste|
|**Nextcloud + Cryptomator**|Self-hosted                         |

#### OS sensible

|Outil         |Usage                        |
|--------------|-----------------------------|
|**Tails**     |Sessions ponctuelles anonymes|
|**Whonix**    |Anonymat Tor persistant      |
|**Qubes OS**  |Compartimentation forte      |
|**GrapheneOS**|Mobile durci sur Pixel       |
|**Kicksecure**|Debian durcie au démarrage   |

#### Détection / monitoring

|Outil             |Notes                                 |
|------------------|--------------------------------------|
|**MVT**           |Détection Pegasus/Predator post-mortem|
|**iVerify**       |Monitoring iOS/Android au quotidien   |
|**HaveIBeenPwned**|Notifications de fuites               |
|**Exodus Privacy**|Audit trackers d’apps Android         |

#### Métadonnées et fichiers

|Outil         |Notes                                 |
|--------------|--------------------------------------|
|**MAT2**      |Nettoyage automatique métadonnées     |
|**ExifTool**  |Référence lecture/écriture métadonnées|
|**Dangerzone**|Reconstruction PDF propre             |

#### Partage de fichiers

|Outil             |Notes                   |
|------------------|------------------------|
|**OnionShare**    |Service onion temporaire|
|**SecureDrop**    |Plateforme rédactions   |
|**GlobaLeaks**    |Équivalent ONG          |
|**CryptPad**      |Suite collaborative E2EE|
|**Bitwarden Send**|Lien temporaire chiffré |

-----

### Annexe 4 — Matrices de décision

#### 4.1 Quelle messagerie pour quel usage ?

|Usage                         |Premier choix         |Second choix                                     |
|------------------------------|----------------------|-------------------------------------------------|
|Famille / amis grand public   |Signal                |iMessage (Apple) ou WhatsApp avec sauvegarde E2EE|
|Source journalistique sensible|SimpleX               |Signal avec username                             |
|Manifestation, offline        |Briar                 |Signal avec disappearing messages                |
|Équipe pro (ONG, rédaction)   |Signal                |Wire ou Matrix                                   |
|Profil ultra-HVT              |SimpleX sur GrapheneOS|Signal sur GrapheneOS avec username              |

#### 4.2 Quel environnement de session sensible ?

|Besoin                                       |Choix                        |
|---------------------------------------------|-----------------------------|
|Action ponctuelle, traces nulles             |Tails                        |
|Identité pseudonyme durable + anonymat réseau|Whonix                       |
|Séparation durable plusieurs activités       |Qubes OS                     |
|HVT avec tous les besoins                    |Qubes + Whonix               |
|Quotidien grand public durci                 |OS durci classique (Ch 14-15)|

#### 4.3 Quelle MFA ?

|Compte                                 |MFA recommandée                    |
|---------------------------------------|-----------------------------------|
|Email principal                        |FIDO2 matériel (YubiKey)           |
|Comptes financiers                     |FIDO2 matériel + TOTP secondaire   |
|Réseaux sociaux                        |FIDO2 ou TOTP                      |
|Comptes utilitaires (boutique en ligne)|TOTP                               |
|Services SMS-only                      |Tenter de migrer ou minimum d’usage|

#### 4.4 Quel chiffrement disque selon OS ?

|OS               |Chiffrement               |Notes                                 |
|-----------------|--------------------------|--------------------------------------|
|macOS            |FileVault                 |Activer dès première utilisation      |
|Windows          |BitLocker (Pro/Enterprise)|TPM + PIN si profil sensible          |
|Linux            |LUKS2                     |Argon2id, systemd-cryptenroll pour TPM|
|Multi-OS portable|VeraCrypt                 |Conteneurs portables                  |

#### 4.5 Quel cloud selon profil ?

|Profil                               |Recommandation                                 |
|-------------------------------------|-----------------------------------------------|
|Grand public Apple                   |iCloud + ADP activée                           |
|Grand public privacy                 |Proton Drive                                   |
|Cloud générique gardé pour écosystème|Cryptomator par-dessus                         |
|Self-hosting                         |Nextcloud + Cryptomator pour E2EE additionnelle|
|Profil pro très sensible             |Tresorit (Suisse, entreprise)                  |

#### 4.6 Quel routage réseau selon contexte ?

| Contexte                               | Choix                                                     |
| -------------------------------------- | --------------------------------------------------------- |
| Quotidien grand public                 | DNS chiffré (DoH/DoT) + + navigateur durci + uBlock       |
| Wi-Fi public                           | + VPN (Mullvad/IVPN)                                      |
| Recherche anonyme                      | Mullvad Browser sur VPN ou Tor Browser                    |
| Action anonyme                         | Tor Browser sur Tor seul                                  |
| Environnement bloquant (Iran, etc.)    | Tor avec bridges obfs4 ou Snowflake                       |
| HVT durable                            | Whonix sur Qubes                                          |
| Navigation privacy quotidienne         | Mullvad Browser + Mullvad VPN                             |
| Session source / journalisme sensible  | Tor Browser sur Tails ou Whonix                           |
| Réduction de métadonnées réseau        | NymVPN Anonymous mode                                     |
| Usage rapide avec routage décentralisé | NymVPN Fast mode                                          |
| Pays censuré / DPI agressif            | AmneziaVPN avec AmneziaWG, XRay Reality ou Cloak          |
| Self-host VPN personnel                | AmneziaVPN sur VPS                                        |
| HVT durable                            | Qubes + Whonix ; VPN seulement comme outil complémentaire |


-----

### Annexe 5 — Architectures de référence par profil (récapitulatif synthétique)

> Renvoi détaillé : Chapitre 38. Cette annexe en propose la forme synthétique tabulaire.

|Profil                            |Mobile                                 |Laptop                              |Stack messageries         |Email                            |VPN                     |OS sensible             |MFA                            |Spécificités                               |
|----------------------------------|---------------------------------------|------------------------------------|--------------------------|---------------------------------|------------------------|------------------------|-------------------------------|-------------------------------------------|
|**Particulier grand public durci**|iPhone + ADP, Lockdown Mode off        |macOS ou Win11 Pro + FDE            |Signal + WhatsApp E2EE    |Proton Mail + alias              |Mullvad ponctuel        |–                       |YubiKey                        |Routines mensuelles                        |
|**Journaliste freelance**         |Pixel + GrapheneOS dédié + iPhone perso|MacBook Pro + MacBook Air enquête   |SimpleX (sources) + Signal|Proton + alias + PGP             |Mullvad permanent       |Tails + Qubes possible  |YubiKey x2                     |Page contact confidentiel publique         |
|**Activiste manifestation**       |Pixel GrapheneOS burner                |Laptop classique perso (non emporté)|Signal + Briar            |Standard                         |Mullvad mobile          |–                       |TOTP                           |Faraday bag, BFU absolu, papier d’urgence  |
|**Dirigeant PME tech**            |iPhone Lockdown + GrapheneOS voyage    |MacBook + burner voyage             |Signal + iMessage CKV     |Pro corporate + perso Proton     |Mullvad                 |–                       |YubiKey x2 + 1Password Business|Procédure anti-BEC, formation équipe       |
|**Opposant politique exil**       |GrapheneOS strict                      |Qubes OS                            |Signal + SimpleX          |Proton via Tor                   |Mullvad + Tor           |Qubes + Whonix          |YubiKey                        |MVT/iVerify mensuel, documentation publique|
|**RSSI ONG terrain**              |iPhone ou Pixel selon contexte         |Qubes OS sur laptops équipe         |Signal Business + Wire    |Proton Drive Business ou Tresorit|Mullvad ou IVPN business|Qubes standardisé       |Clés matérielles équipe        |Formation continue, audits annuels         |
|**Victime ex-partenaire abusif**  |Téléphone neuf cash                    |Laptop neuf si possible             |Signal + Briar urgence    |Email neuf E2EE                  |Mullvad                 |–                       |YubiKey                        |Audit stalkerware, soutien associatif      |
|**HVT extrême**                   |GrapheneOS + reboot 2x/jour            |Qubes OS + air-gap                  |SimpleX + Signal          |Proton via Tor permanent         |Tor + VPN obfusqué      |Qubes + Whonix + air-gap|YubiKey                        |Forensique mensuelle, équipe juridique     |

-----

### Annexe 6 — Templates opérationnels

#### 6.1 Template — Threat model personnel

```
[DATE] — [VERSION X.Y]
À RELIRE À : [DATE + 3 MOIS]

QUI JE SUIS (CONTEXTE) :
- Profession :
- Contexte spécifique (enquête, engagement, mission, situation) :
- Profil HVT-ness honnête (oui / non / partiel) :

ACTIFS PRIORITAIRES (top 5) :
1.
2.
3.
4.
5.

ADVERSAIRES PLAUSIBLES (top 5, par probabilité × capacité × motivation) :
1. [Nom] | Capacité : | Motivation : | Méthodes typiques :
2.
3.
4.
5.

HORS PÉRIMÈTRE EXPLICITE :
- 
- 
- 

MESURES PRIORITAIRES ACTUELLES :
1.
2.
3.
4.
5.

POINTS D'ATTENTION (à surveiller) :
- 
- 

SIGNATURE :
```

#### 6.2 Template — Brief manifestation

```
[DATE] — [LIEU] — [HEURE DE DÉBUT]

CONTEXTE :
- Nature de la manifestation :
- Risques anticipés (interpellations, gaz, charges, présence drones) :
- Présence de presse :

ÉQUIPE (présents au brief) :
-
-
-

RÉFÉRENT :
- Personne désignée hors manif :
- Procédure d'alerte si silence > X heures :

HOTLINE JURIDIQUE :
- Numéro :
- Avocat de garde :

CHECKLIST PERSONNELLE :
[ ] Téléphone manif chargé, BFU, faraday bag
[ ] Téléphone perso laissé éteint chez soi
[ ] Papier avec numéros essentiels
[ ] Cash + CB prépayée
[ ] Vêtements anonymes
[ ] Lunettes / protection
[ ] Pas de document compromettant

CHECKLIST RETOUR :
[ ] Compter les présents
[ ] Communication référent OK
[ ] Téléphone non saisi
[ ] Si saisie : protocole brûlure
[ ] Audit appareils (si perquisition possible)
```

#### 6.3 Template — Plan IR personnel

```
PROCÉDURE D'INCIDENT — VERSION [X.Y] — [DATE]

CONTACTS D'URGENCE :
- Avocat : [nom, téléphone]
- Référent technique (si applicable) : 
- Famille de confiance :
- Association de soutien :
- Hotline crisis : Access Now Digital Security Helpline +1 888 414 0100

EN CAS DE TÉLÉPHONE PERDU / VOLÉ :
1. Localisation à distance via [iCloud / Google] : [étapes]
2. Effacement à distance si nécessaire
3. Opérateur : [numéro support pour bloquer SIM]
4. Comptes à révoquer en priorité : Apple / Google / Microsoft / banques / messageries
5. Plainte police (numéro IMEI fourni à l'opérateur — noté dans 1Password sous "Matériel")

EN CAS DE COMPTE COMPROMIS :
1. Mot de passe changé depuis [appareil sain — préciser lequel]
2. Sessions actives révoquées
3. Audit modifications (mail récup, MFA, filtres)
4. Comptes liés vérifiés
5. Communication aux contacts si nécessaire

EN CAS DE SPYWARE SUSPECTÉ :
1. Mode avion + faraday
2. NE PAS REDÉMARRER
3. Access Now Helpline
4. MVT / Citizen Lab

EN CAS DE DOXXING :
1. Captures + horodatages
2. Signalement plateformes
3. Évaluation menace physique
4. Avocat + plainte
5. Soutien : [association locale]

CODES DE RÉCUPÉRATION :
- Stockés : [coffre — où exactement]
- Apple ID : ____
- Google : ____
- Bitwarden : ____
- 2FA backup codes : ____
```

#### 6.4 Template — Audit trimestriel

```
TRIMESTRE [TX] — [DATE]

OSINT DÉFENSIF :
[ ] Recherche nom complet sur Google / Bing / DDG
[ ] HaveIBeenPwned sur emails principaux
[ ] Reverse image sur photo de profil
[ ] WhatsMyName sur pseudonymes
[ ] Data brokers nouveaux apparus

SÉCURITÉ COMPTES :
[ ] Audit sessions Google / Apple / Microsoft
[ ] Audit MFA sur 20 comptes critiques
[ ] Revue gestionnaire de mots de passe (doublons, faibles)
[ ] Codes de récupération à jour

APPAREILS :
[ ] Mises à jour OS et firmware
[ ] Intégrité physique des appareils (vis, photos comparatives)
[ ] Permissions mobiles auditées
[ ] Reboot complet

SAUVEGARDES :
[ ] Test de restauration mini (un fichier)
[ ] Cloud E2EE fonctionnel
[ ] Disque externe en lieu sûr OK
[ ] Sauvegarde immuable mensuelle OK

THREAT MODEL :
[ ] Toujours pertinent ?
[ ] Évolutions à acter ?

NOTES :
```

#### 6.5 Template — Page « comment me joindre confidentiellement »

```
COMMENT ME JOINDRE CONFIDENTIELLEMENT

Je travaille sur des dossiers parfois sensibles. Si vous souhaitez 
me contacter de manière sécurisée, voici les canaux que je vérifie :

1. SECUREDROP : [lien .onion]
   À utiliser via Tor Browser (https://torproject.org).
   Anonyme. Préféré pour transmission de documents.

2. SIGNAL : @username (pas de numéro de téléphone)
   Pour discussion préalable et coordination.
   Vérification : Safety Numbers à comparer.

3. EMAIL CHIFFRÉ : email@domain.org
   Clé PGP : [fingerprint] — disponible sur Keys.OpenPGP.org
   Pour échanges techniques.

4. SIMPLEX : Sur demande, je peux fournir un lien d'invitation.

Avant tout envoi de documents sensibles, contactez-moi d'abord 
pour que nous choisissions ensemble le canal adapté.

Précautions à prendre de votre côté :
- Ne pas utiliser un appareil professionnel pour me contacter.
- Considérer Tor Browser sur Tails pour confidentialité maximale.
- Ne jamais transmettre depuis un réseau de votre employeur.

Cette page est à jour au [date].
```

-----

### Annexe 7 — Cadre juridique comparé (FR / UE / US / UK / CH)

#### 7.1 Chiffrement personnel

|Pays  |Légalité usage       |Obligation déchiffrer     |Notes                                           |
|------|---------------------|--------------------------|------------------------------------------------|
|France|Oui (LCEN art. 30)   |Oui (CP 434-15-2)         |3 ans / 270 k€ refus                            |
|UE    |Oui                  |Variable par État         |Pas d’harmonisation                             |
|US    |Oui (constitutionnel)|5e amendement = protection|Biométrie vs code mémoire jurisprudence mouvante|
|UK    |Oui                  |Oui (RIPA s. 49)          |2 ans / 5 ans selon contexte                    |
|Suisse|Oui (Cst. art. 13)   |Non                       |Forte protection                                |

#### 7.2 Surveillance des communications

|Pays  |Cadre                                                 |Contrôle               |Spécificités                                         |
|------|------------------------------------------------------|-----------------------|-----------------------------------------------------|
|France|LRM 2015, ajustée 2017, 2021                          |CNCTR + Conseil d’État |Algorithmes prédictifs, géolocalisation temps réel   |
|UE    |E-Privacy Regulation (en cours), CJUE limite rétention|Cours nationales + CJUE|Plusieurs régimes nationaux retoqués                 |
|US    |FISA section 702, NSL                                 |FISC                   |Loi étrangers + extension citoyens                   |
|UK    |IPA 2016                                              |IPCO                   |« Snooper’s Charter », interception massive autorisée|
|Suisse|LRens 2016                                            |DDPS                   |Surveillance plus strictement encadrée               |

#### 7.3 Protection des journalistes / sources

|Pays  |Cadre                                |Notes                                                    |
|------|-------------------------------------|---------------------------------------------------------|
|France|Loi 4 janvier 2010 + dir. UE 2024    |Secret protégé sauf impératif prépondérant intérêt public|
|UE    |Directive 2024 (Media Freedom Act)   |Limite spyware contre journalistes                       |
|US    |Shield laws variables par État       |Pas de loi fédérale unifiée                              |
|UK    |Sources Protection (limited)         |RIPA peut être invoqué                                   |
|Suisse|Forte protection légale et culturelle|–                                                        |

#### 7.4 Anti-doxxing

|Pays  |Cadre                                                                          |
|------|-------------------------------------------------------------------------------|
|France|CP 226-1 (vie privée), 222-33-2-2 (harcèlement), loi 2022 (aggravation), PHAROS|
|UE    |Variable national. Digital Services Act 2024 (modération)                      |
|US    |Variable par État. Pas de loi fédérale spécifique                              |
|UK    |Malicious Communications Act, Online Safety Act 2023                           |
|Suisse|Atteinte à l’honneur et à la personnalité                                      |

#### 7.5 Lanceurs d’alerte

|Pays  |Cadre                                                                 |
|------|----------------------------------------------------------------------|
|France|Sapin II (2016, mod. 2022) — Maison des Lanceurs d’Alerte             |
|UE    |Directive 2019/1937                                                   |
|US    |Whistleblower Protection Act, sectorielle (Sarbanes-Oxley, Dodd-Frank)|
|UK    |PIDA 1998                                                             |
|Suisse|LWB (récente)                                                         |

#### 7.6 RGPD et droits utilisables

Articles RGPD invocables comme particulier dans l’UE/EEE :

- **Art. 15** : droit d’accès (demander quelle donnée détenue).
- **Art. 16** : droit de rectification.
- **Art. 17** : droit à l’effacement (« droit à l’oubli »).
- **Art. 18** : droit à la limitation du traitement.
- **Art. 20** : droit à la portabilité.
- **Art. 21** : droit d’opposition.
- **Art. 22** : droit de ne pas faire l’objet d’une décision automatisée.

Recours : autorité de contrôle nationale (CNIL en France), avec amendes croissantes pour violation.

#### 7.7 AI Act UE (2024/1689)

- **Article 5** : interdictions absolues (notation sociale, certaines reconnaissances biométriques en temps réel par autorités).
- **Article 6+** : régime des « systèmes à haut risque ».
- **Article 50** : obligation de marquage des contenus IA (deepfakes).
- Sanctions importantes pour fournisseurs.

#### 7.8 Spécificité française : LRM et CNCTR

Loi sur le renseignement (2015, ajustée 2017, 2021) :

- Cadre des techniques de renseignement (interceptions, géolocalisation, balisage, algorithmes).
- Commission nationale de contrôle (CNCTR) : avis consultatif.
- Conseil d’État : juridiction de recours.

Critiques persistantes : asymétrie entre capacités et contrôle effectif. Plusieurs décisions du Conseil constitutionnel et CEDH ont contraint des ajustements.

-----

### Annexe 8 — Cas célèbres d’échec OPSEC : leçons défensives

> **Méthode** : chaque cas est traité selon le format **Contexte / Chaîne d’erreurs OPSEC / Mécanismes de corrélation et attribution / Leçons défensives transposables / Renvois croisés**. Un encart « Ce que ce cas n’enseigne pas » corrige les sur-généralisations classiques quand pertinent.
> 
> **Cadre éditorial** : ces cas sont publics, documentés, judiciairement clos. Leur étude pédagogique est légitime. L’objectif est défensif : comprendre les mécanismes pour les neutraliser, pas reproduire les opérations sous-jacentes.

-----

#### Annexe 8.1 — Ross Ulbricht / Silk Road (2013)

**Contexte**

Ross Ulbricht, opérateur du marché noir Silk Road sous le pseudonyme « Dread Pirate Roberts », arrêté en octobre 2013 à la Glen Park Library de San Francisco par le FBI. Silk Road, marché Tor accessible via service onion, avait facilité de 2011 à 2013 des transactions illicites en Bitcoin pour estimé à plus d’un milliard de dollars. Condamné à perpétuité en 2015. Sa peine a été commuée en janvier 2025.

**Chaîne d’erreurs OPSEC**

1. **Réutilisation de pseudonyme entre identités** : « altoid » utilisé en mars 2011 sur le forum Bitcoin Talk pour promouvoir Silk Road, *avant* qu’Ulbricht ne devienne « Dread Pirate Roberts ». Le pseudo « altoid » avait été utilisé peu de temps avant sur des forums de magic mushrooms.
1. **Email civil rattaché à un compte technique** : sur un forum Stack Overflow, Ulbricht a posé une question technique liée à Silk Road (en omettant ce contexte) sous son pseudonyme. Mais il a corrigé son post sous son nom réel `rossulbricht@gmail.com` peu après.
1. **OPSEC physique défaillante** : ordinateur portable ouvert et déverrouillé au moment de l’arrestation (par tactique du FBI qui a créé une diversion à la bibliothèque, des agents l’ont saisi en flagrant état AFU).
1. **Documentation incriminante non chiffrée** : journaux personnels, listes de tâches détaillées sur les opérations Silk Road, conservés en clair sur son ordinateur.
1. **Mauvaise hygiène des transactions** : commande de fausses pièces d’identité livrées à son adresse réelle pour tester un fournisseur.
1. **Confidences à des contacts** : conversations confidentielles avec des associés (dont des informateurs FBI infiltrés).

**Mécanismes de corrélation et attribution exploités**

Le FBI et la DEA ont remonté à Ulbricht non par un cassage de Tor mais par chaînage de signaux :

- Recherche du pseudonyme « altoid » sur Google par l’agent IRS Gary Alford → premiers posts retrouvés.
- Corrélation altoid/Stack Overflow → adresse Gmail réelle.
- Surveillance physique → identification.
- Saisie en AFU → accès complet aux journaux et clés.

Tor a tenu techniquement. L’OPSEC humaine et applicative a cédé sur six points indépendants.

**Leçons défensives transposables**

1. **Compartimentation absolue** entre identités. Un pseudonyme ne doit jamais croiser un identifiant civil (Ch 9). « Une seule erreur suffit. »
1. **Documentation chiffrée** systématique. Pas de journal d’opérations en clair (Ch 12).
1. **Ne pas tenir l’appareil sensible en AFU** dans un lieu public. BFU avant tout déplacement (Ch 12.8).
1. **Audit régulier de réutilisation de pseudonyme** via WhatsMyName / Sherlock (Ch 5).
1. **Minimalisme dans la confidence** : need-to-know strict (Ch 1.5).

**Ce que ce cas n’enseigne pas**

- ❌ « Tor est cassé. » Faux. Tor a tenu. Ce sont les erreurs applicatives qui ont fait tomber Ulbricht.
- ❌ « Bitcoin est anonyme et a permis Silk Road. » Faux. Bitcoin n’a jamais été anonyme. Les analyses de chaîne ont contribué à l’enquête.

**Renvois croisés** : Ch 1 (concepts), Ch 5 (OSINT défensif), Ch 9 (compartimentation), Ch 12 (chiffrement disque et BFU/AFU), Ch 21 (Tor OPSEC), Ch 32 (cryptomonnaies traçables).

-----

#### Annexe 8.2 — Eldo Kim / Harvard bomb threat (2013)

**Contexte**

Eldo Kim, 20 ans, étudiant à Harvard, envoie le 16 décembre 2013 une fausse alerte à la bombe via le service email anonyme Guerrilla Mail à l’administration de Harvard, dans le but de différer un examen final pour lequel il était mal préparé. Identifié et arrêté en quelques heures. A plaidé coupable. A bénéficié d’un sursis.

**Chaîne d’erreurs OPSEC**

1. **Usage de Tor depuis le réseau Harvard** : Kim a utilisé Tor depuis le Wi-Fi du campus. Or il était le **seul utilisateur de Tor sur le réseau Harvard à ce moment précis**.
1. **Coïncidence temporelle évidente** : l’envoi du mail anonyme correspondait exactement à la fenêtre de la connexion Tor.
1. **Identification par registre WPA d’authentification** : Harvard a corrélé les logs WPA enterprise (qui exigeaient login étudiant) avec les logs de session Tor sortant.

**Mécanismes de corrélation et attribution exploités**

Le mail a été envoyé via Guerrilla Mail à travers Tor. Les en-têtes du mail indiquaient l’IP du nœud de sortie Tor, comme prévu. Mais Harvard, en examinant ses propres logs réseau, a identifié quel(s) utilisateur(s) avai(en)t utilisé Tor pendant la fenêtre pertinente. Un seul étudiant : Kim. Confrontation rapide, aveux.

**Leçons défensives transposables**

1. **Tor protège contre l’observation à distance, mais pas contre la corrélation locale**. Si tu utilises Tor depuis un réseau qui peut t’identifier individuellement, le bénéfice est nul.
1. **Bridges et Snowflake** pour environnements où l’usage de Tor lui-même est observable et incriminant (Ch 21.3).
1. **Diversification des points de sortie** : ne pas utiliser Tor depuis chez soi pour activité dont la fenêtre est unique et identifiable.
1. **Ne pas faire d’OPSEC pour des actes illégaux** : ce cas illustre aussi qu’au-delà de la technique, l’opération elle-même était mal pensée — une fausse alerte n’a aucune justification, et le seul utilisateur Tor sur un réseau spécifique est trivialement identifiable.

**Renvois croisés** : Ch 21 (Tor OPSEC), Ch 9 (compartimentation horaires).

-----

#### Annexe 8.3 — Hector Monsegur / « Sabu » / LulzSec (2011)

**Contexte**

Hector Xavier Monsegur, alias « Sabu », figure centrale du collectif hacktiviste LulzSec et co-fondateur d’AntiSec. Identifié par le FBI en juin 2011, retourné comme informateur, a coopéré pendant plusieurs mois pour identifier d’autres membres du collectif (Jeremy Hammond entre autres).

**Chaîne d’erreurs OPSEC**

1. **Connexion à IRC sans Tor depuis IP domestique** : à une occasion, Sabu s’est connecté à un serveur IRC où LulzSec se coordonnait sans utiliser Tor. Son adresse IP réelle (NYC, immeuble HLM) a été enregistrée dans les logs IRC.
1. **Mauvaise hygiène opérationnelle** : utilisation de Twitter sous le pseudo Sabu pour communications publiques, occasionnellement croisé avec des éléments traçables.
1. **Identification croisée** : informations personnelles cohérentes à travers plusieurs sessions, dont une mention de famille reconnaissable.

**Mécanismes de corrélation et attribution exploités**

Le FBI surveillait IRC. La connexion non-Tor a fourni l’IP. Identification rapide via l’opérateur. Surveillance physique pour confirmation. Arrestation et retournement.

**Leçons défensives transposables**

1. **Une seule erreur ponctuelle suffit**. La compartimentation absolue ne tolère pas l’exception « juste cette fois » (Ch 9.6).
1. **Automatiser pour empêcher l’erreur** : configurer le client IRC pour refuser toute connexion non-Tor (proxy système, killswitch).
1. **Threat model honnête** : si tu es publiquement engagé dans des activités illégales (par exemple ici, intrusions), tu es structurellement vulnérable. La discipline OPSEC ne compense pas un threat model irréaliste.

**Renvois croisés** : Ch 9 (compartimentation), Ch 20 (VPN/killswitch), Ch 21 (Tor OPSEC).

-----

#### Annexe 8.4 — Paul Le Roux (2012)

**Contexte**

Paul Calder Le Roux, programmeur sud-africain originaire de Rhodésie, ancien créateur du logiciel de chiffrement E4M (puis TrueCrypt), opérait à partir des années 2000 une organisation criminelle internationale impliquée dans trafic de drogue, armes, et homicides commandités. Arrêté à Monrovia (Liberia) en septembre 2012 dans le cadre d’une opération de la DEA, retourné comme informateur, a permis l’arrestation de plusieurs collaborateurs.

**Chaîne d’erreurs OPSEC**

1. **Compartimentation insuffisante** entre la facette légale (entrepreneur informatique) et la facette criminelle (commerce de méthamphétamine, armes).
1. **Confidences à des associés** dont certains ont été retournés ou ont coopéré.
1. **Mouvements financiers traçables** : malgré l’usage de société offshore et de transferts informels, des traces ont permis aux enquêteurs de remonter.
1. **Géographie compromise** : présence régulière dans certaines juridictions où la DEA opérait (Philippines, Liberia).

**Mécanismes de corrélation et attribution exploités**

Coopération internationale entre DEA et services locaux. Témoins-clés retournés. Surveillance physique. L’opération s’étend sur années — l’OPSEC sur la durée est exponentiellement plus difficile que pour un acte ponctuel.

**Leçons défensives transposables**

Le cas Le Roux est éducatif principalement sur les **limites de l’OPSEC face à un threat model lourd dans la durée** :

1. **L’OPSEC ne compense pas un threat model intenable** : si on a comme adversaires des services de police internationale motivés et coopérants, sur une décennie, la probabilité d’échec tend vers 1.
1. **Le facteur humain reste le maillon faible** : les associés finissent souvent par coopérer.
1. **Compartimentation des facettes de vie** : c’est applicable à des contextes légitimes (journaliste-source, activiste-vie civile) qui empruntent les mêmes mécaniques sans la dimension illégale.

**Ce que ce cas n’enseigne pas**

- ❌ « TrueCrypt est compromis. » Faux. Le Roux a été l’un des programmeurs initiaux d’E4M (prédécesseur), mais cela n’a aucune implication pour la sécurité de TrueCrypt/VeraCrypt actuel.

**Renvois croisés** : Ch 1 (limites), Ch 9 (compartimentation), Ch 35 (OPSEC humaine).

-----

#### Annexe 8.5 — Reality Winner / Yellow dots (2017)

**Contexte**

Reality Leigh Winner, analyste de renseignement pour la NSA (sous contrat avec Pluribus International), a transmis en mai 2017 au média *The Intercept* un document classifié top-secret concernant des opérations cybernétiques russes contre les élections américaines de 2016. Arrêtée le 3 juin 2017, condamnée à 5 ans et 3 mois.

**Chaîne d’erreurs OPSEC**

1. **Impression du document sensible sur l’imprimante de son employeur** : laisser des traces forensiques imprimées (Machine Identification Code — yellow dots).
1. **Photographie ou scan du document imprimé** : transmise à The Intercept telle quelle, sans nettoyage des yellow dots.
1. **The Intercept a publié le document avec ses yellow dots intacts** sur leur site, permettant à toute personne d’extraire les métadonnées (identifiant d’imprimante, date, heure).
1. **Audit interne NSA rapide** : l’imprimante avait été utilisée par 6 personnes, dont Reality Winner. Croisement avec ses logs d’email récents (elle avait communiqué avec The Intercept), arrestation.

**Mécanismes de corrélation et attribution exploités**

Le **Machine Identification Code** (MIC) est un système de marquage par micro-points jaunes presque invisibles, généré par la quasi-totalité des imprimantes couleur professionnelles depuis ~2000. Les yellow dots encodent :

- Numéro de série de l’imprimante.
- Date et heure d’impression.

Documenté par l’EFF dès 2005, mais largement ignoré par le public.

**Leçons défensives transposables**

1. **Ne pas imprimer un document à publier** depuis une imprimante traçable (Ch 31.6).
1. **Re-générer le PDF depuis le texte plutôt que scanner un document imprimé** : élimine yellow dots et métadonnées originales.
1. **Audit des métadonnées avant publication** : ExifTool, MAT2, Dangerzone (Ch 31.7, 31.8).
1. **Responsabilité de la rédaction** : The Intercept a partagé un document non nettoyé, contribuant directement à l’identification. Procédures rédactionnelles à durcir, voir SecureDrop avec workflow approprié (Ch 28.2).

**Ce que ce cas n’enseigne pas**

- ❌ « Les imprimantes sont compromises et inutilisables. » Faux. Pour usage banal, les yellow dots sont sans importance. C’est dans le contexte d’une publication anonyme qu’ils deviennent critiques.

**Renvois croisés** : Ch 28 (partage sécurisé), Ch 31 (métadonnées et yellow dots), Ch 37 (cadre lanceurs d’alerte).

-----

#### Annexe 8.6 — John McAfee / EXIF Vice photo (2012)

**Contexte**

John McAfee, fondateur de l’antivirus éponyme, fuyait depuis le Belize après être soupçonné dans le meurtre de son voisin Gregory Faull (novembre 2012). En décembre 2012, Vice Magazine publie une photo de McAfee prise par un journaliste avec son iPhone. La photo contient les métadonnées EXIF GPS intactes, révélant la localisation précise au Guatemala. McAfee est arrêté par les autorités guatémaltèques dans les jours qui suivent. (Il s’est ultérieurement suicidé en prison en Espagne en 2021.)

**Chaîne d’erreurs OPSEC**

1. **EXIF GPS activé sur l’iPhone du journaliste**.
1. **Publication de la photo sans audit des métadonnées** par Vice.
1. **McAfee, lui-même célèbre pour son passé sécurité, n’a pas vérifié l’OPSEC de son interlocuteur journaliste**.

**Mécanismes de corrélation et attribution exploités**

Trivial. Tout utilisateur curieux pouvait télécharger la photo et lire les EXIF avec n’importe quel outil (ExifTool, ou simplement le clic-droit Propriétés sur Windows). Coordonnées GPS → localisation McAfee.

**Leçons défensives transposables**

1. **EXIF avant publication, toujours**. Vérifier avec ExifTool ou MAT2 (Ch 31.2).
1. **Audit du collaborateur** : ton OPSEC ne dépend pas que de toi. Si tu accordes une interview, vérifier ce que le journaliste va publier, demander à voir avant.
1. **Plateformes professionnelles** retirent généralement EXIF côté serveur (Instagram, Facebook, Twitter), mais beaucoup de petits sites et magazines ne le font pas. Ne pas présumer.

**Renvois croisés** : Ch 31 (métadonnées EXIF), Ch 35 (OPSEC humaine, entourage).

-----

#### Annexe 8.7 — Patron du Drug Enforcement (DOJ insider, 2015-2018)

**Contexte agrégé**

Plusieurs cas, anonymisés par regroupement, d’insiders DOJ/DEA/agences fédérales US ayant vendu des informations à des cartels ou à la criminalité organisée entre 2015 et 2018. Identifiés par audits internes croisant accès aux bases de données et patterns de consultations inhabituelles (queries sur des cibles sans dossier ouvert correspondant), corrélés avec mouvements financiers personnels suspects.

**Chaîne d’erreurs OPSEC commune**

1. **Consultations de bases internes pour des intérêts personnels** sans dossier officiel ouvert (laisse trace forensique sur les logs).
1. **Communications opérationnelles** avec contacts criminels via canaux non maîtrisés (téléphones personnels, comptes mail civils).
1. **Mouvements financiers** détectables (déclarations fiscales incohérentes, achats luxueux).
1. **Imprudences sociales** : confidences à proches, ostentation.

**Mécanismes de corrélation et attribution exploités**

Audit interne automatisé par les agences elles-mêmes, croisé avec analyses financières (FinCEN). UEBA (User and Entity Behavior Analytics).

**Leçons défensives transposables (légitimes)**

Cette série de cas n’a pas de transposition défensive directe pour un usage légitime. Elle est mentionnée pour rappel :

1. **Les organisations modernes monitor leurs employés** sur les accès aux données sensibles. Un salarié légitime ne peut pas masquer une consultation inhabituelle à terme.
1. **Pour un journaliste qui travaille avec un lanceur d’alerte interne d’une telle agence** : la fenêtre d’opportunité pour la source est courte. Procédures rapides, minimisation des traces, soutien légal avant divulgation.

**Renvois croisés** : Ch 37 (cadre lanceurs d’alerte, Sapin II).

-----

#### Annexe 8.8 — Cas Roman Storm / Tornado Cash (2023-2024)

**Contexte**

Roman Storm, co-développeur de Tornado Cash (un *mixer* Ethereum d’anonymisation), arrêté en août 2023 par les autorités américaines pour conspiration de blanchiment et violation de sanctions. Procès en 2024-2025.

**Particularité du cas**

Ce cas n’est pas un échec d’OPSEC personnelle au sens strict — Roman Storm vivait ouvertement et publiquement. C’est un cas d’**incertitude juridique du développeur d’outils privacy**.

**Leçons (juridiques, pas techniques)**

1. **Les développeurs d’outils privacy/anonymat opèrent dans une zone légale qui peut être contestée**, particulièrement aux États-Unis où le rattachement à des opérations sanctionnées (OFAC) peut entraîner des poursuites.
1. **Distinction code vs opération** : la défense Storm argumente que Tornado Cash est code open source publié, sans intermédiation active. La poursuite argumente qu’il y avait gestion opérationnelle.
1. **Implications pour les utilisateurs** : un service technique disponible aujourd’hui peut être sanctionné demain. Pour usages légitimes (don anonyme à un journaliste, par exemple), considérer cette volatilité juridique.

**Renvois croisés** : Ch 32 (cryptomonnaies), Ch 37 (cadre juridique).

-----

### Annexe 9 — Ressources, formations, communautés

#### 9.1 Documentation de référence (anglais)

- **EFF Surveillance Self-Defense** (https://ssd.eff.org) : référence pédagogique, threat modeling, guides par profil.
- **Privacy Guides** (https://privacyguides.org) : outils recommandés, philosophie, guides techniques.
- **The Practical Guide to Threat Modeling** (Adam Shostack) : pour profils techniques.
- **NIST SP 800-63 (Digital Identity Guidelines)** : authentification.
- **The Hitchhiker’s Guide to Online Anonymity** (AnonyPla) : ressource exhaustive sur l’anonymat, à utiliser avec recul critique.

#### 9.2 Documentation francophone

- **CNIL** (https://cnil.fr) : RGPD, droits, guides.
- **ANSSI** (https://ssi.gouv.fr) : guides cyber, recommandations.
- **La Quadrature du Net** (https://laquadrature.net) : veille libertés numériques en France.
- **Nothing2Hide** (https://nothing2hide.org) : formation journalistes / activistes francophones.
- **Bortzmeyer, blog** : technique réseau, DNS, Internet (https://www.bortzmeyer.org).
- **CECIL** (https://lececil.org) : libertés et internet.

#### 9.3 Organisations de soutien aux journalistes et sources

- **Reporters sans frontières (RSF)** : guide journaliste, hotline sécurité numérique.
- **Committee to Protect Journalists (CPJ)** : Digital Safety Kit, formations.
- **Forbidden Stories** : continuité d’enquêtes en cas de blocage.
- **Freedom of the Press Foundation (FPF)** : SecureDrop, Dangerzone, formations.
- **Global Investigative Journalism Network (GIJN)** : ressources investigation.
- **Tactical Tech** : Data Detox, formation activistes/journalistes.

#### 9.4 Organisations de soutien activistes et défenseurs

- **Access Now Digital Security Helpline** (+1 888 414 0100, https://accessnow.org/help) : assistance gratuite 24/7 pour profils à risque (journalistes, activistes, défenseurs droits humains).
- **Front Line Defenders** : protection physique et numérique des défenseurs.
- **EFF** (https://eff.org) : litiges stratégiques, ressources.
- **La Quadrature du Net** : recours juridiques France.
- **Privacy International** : recherche et litiges UK/international.

#### 9.5 Soutien lanceurs d’alerte (France)

- **Maison des Lanceurs d’Alerte** (https://mlalerte.org) : accompagnement juridique, psychologique, pratique.
- **Défenseur des droits** : autorité administrative pour signalements externes.
- **Whistleblower Network News** : ressources internationales.

#### 9.6 Soutien victimes violences conjugales et stalkerware

- **Coalition Against Stalkerware** (https://stopstalkerware.org) : ressources, outils, partenaires.
- **France : 3919** (numéro national violences conjugales).
- **CIDFF** (Centres d’information sur les droits des femmes et des familles).
- **Solidarité Femmes** (réseau associatif).
- **EFF Surveillance Self-Defense, section « Domestic Abuse Survivors »**.

#### 9.7 Analyse forensique mobile suspicion spyware

- **Citizen Lab** (Université de Toronto, https://citizenlab.ca) : recherche et analyse forensique, soumission de cas via Access Now.
- **Amnesty Security Lab** : recherches Pegasus, Predator. MVT outil officiel (https://github.com/mvt-project/mvt).
- **iVerify** (commercial) : application Android/iOS de monitoring.

#### 9.8 Communautés et apprentissage

- **r/privacy, r/privacytoolsIO, r/qubes, r/Tor (Reddit)** : discussions techniques (modération variable).
- **Privacy Guides forum** : technique, modéré.
- **Tor mailing-lists** : pour profils techniques.
- **Local CryptoParties** : ateliers d’initiation locaux, mouvement international.
- **Tactical Tech, Internews, Open Briefing** : formations professionnelles.

#### 9.9 Lectures pour aller plus loin

**Techniques** :

- Bruce Schneier, *Secrets and Lies*, *Data and Goliath*.
- Adam Shostack, *Threat Modeling: Designing for Security*.

**Sociologiques / politiques** :

- Shoshana Zuboff, *The Age of Surveillance Capitalism*.
- Glenn Greenwald, *No Place to Hide*.
- Bruce Schneier, *Click Here to Kill Everybody*.

**Reportages / enquêtes** :

- *Pegasus Project* (Forbidden Stories + 17 médias, 2021).
- *Predator Files* (Mediapart + EIC, 2023).

**Histoire** :

- Steven Levy, *Crypto: How the Code Rebels Beat the Government — Saving Privacy in the Digital Age*.
- David Kahn, *The Codebreakers*.

-----

> 🟩 **Mot final**
> 
> La sécurité parfaite n’existe pas. La sécurité *suffisante pour ton threat model, soutenable dans le temps*, est atteignable.
> 
> Ce cours t’a appris à raisonner. Les outils changeront, les protocoles évolueront, les adversaires se transformeront. Le raisonnement, lui, dure.
> 
> Trois principes à retenir au-delà de tous les chapitres :
> 
> 1. **Threat model d’abord, outil ensuite.** Toujours.
> 1. **Compartimentation et minimisation** sont plus puissantes que tout outil magique.
> 1. **Durer**. Une posture brillante trois semaines puis abandonnée vaut moins qu’une posture moyenne tenue dix ans.
> 
> Bonne route.

-----

*Fin du cours.*

*Version 1.0 — Manuel collectif, mis à jour 2025-2026. Pour signaler une erreur, suggérer un complément, contribuer : voir page de contact.*

*Le cours est diffusé sous licence Creative Commons BY-NC-SA 4.0. Reproduction libre à condition de citer la source, sans usage commercial, et de partager dans les mêmes conditions.*
