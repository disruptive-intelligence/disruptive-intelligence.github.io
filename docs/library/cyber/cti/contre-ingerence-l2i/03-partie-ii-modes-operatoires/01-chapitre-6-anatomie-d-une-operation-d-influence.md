---
title: Chapitre 6 — Anatomie d'une opération d'influence
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence (L2I)
up:
- - Contre-ingérence (L2I)
  - ../index.md
- - Partie II — Modes opératoires
  - index.md
---

le cycle opérationnel

## 6.1 Le modèle en 5 phases

Une opération d'influence structurée suit un cycle opérationnel qui peut être décomposé en cinq phases, inspiré du modèle kill chain adapté au domaine informationnel.

**Phase 1 — Reconnaissance.** L'opérateur cartographie l'environnement informationnel cible : fractures sociétales exploitables, sujets de polarisation, personnalités influentes, écosystème médiatique, fonctionnement algorithmique des plateformes ciblées, contexte politique (élections, crises, événements). Cette phase est analogue à la reconnaissance en cybersécurité — elle vise à identifier les vulnérabilités de l'espace informationnel. VIGINUM a documenté comment Storm-1516 adapte ses narratifs en fonction des contextes politiques de chaque pays cible, ciblant les thématiques les plus clivantes du moment (immigration en France, corruption présumée aux États-Unis, fractures sociétales en Allemagne).

**Phase 2 — Préparation.** L'infrastructure est mise en place : création de comptes sur les plateformes (avec photos de profil générées, biographies construites, historique factice de publications non politiques pour construire une apparence de légitimité), enregistrement de noms de domaine pour les sites de réinformation, mise en place des canaux d'amplification (Telegram, newsletters), production des contenus (articles, vidéos, deepfakes, memes). La préparation peut s'étaler sur plusieurs mois : le rapport VIGINUM sur Storm-1516 documente que certains comptes utilisés par le MOI ont été créés jusqu'à un an avant leur activation dans une opération.

**Phase 3 — Déploiement (injection).** Les narratifs sont injectés dans l'espace informationnel. Cette phase est critique et souvent le point le plus vulnérable de l'opération — le primo-diffuseur est le plus exposé à la détection. Storm-1516 utilise trois vecteurs de primo-diffusion : des comptes jetables sur X (créés et abandonnés après usage), des tiers rémunérés (influenceurs payés pour partager le contenu), et des publications sur le réseau de faux sites CopyCop. La primo-diffusion est souvent discrète et s'appuie sur un nombre limité de comptes.

**Phase 4 — Amplification.** Le contenu primo-diffusé est massivement amplifié par un réseau coordonné : retweets synchronisés, partages dans des groupes Facebook, republication sur des chaînes Telegram, intégration dans des newsletters. Le blanchiment (*laundering*) est une étape clé : le contenu passe de sources manifestement suspectes à des sources semi-légitimes (médias étrangers rémunérés, blogs d'opinion, comptes d'influenceurs idéologiques) puis potentiellement à des médias mainstream. Storm-1516 illustre cette mécanique : les contenus du MOI sont primo-diffusés par des comptes jetables, blanchis par des médias étrangers rémunérés et des comptes de réseaux sociaux rémunérés, puis amplifiés par des influenceurs liés à la Fondation pour combattre l'injustice (FCI) et l'Association des journalistes des BRICS (BJA), avant d'être repris par des médias d'État russes et des canaux Telegram russophones.

**Phase 5 — Exploitation.** L'opérateur capitalise sur l'impact : le narratif a pénétré le débat public, des médias mainstream en parlent (même pour le contester), des personnalités politiques le relayent ou le commentent, la perception publique est modifiée. Le rapport VIGINUM note que certains narratifs de Storm-1516 ont été repris par des sénateurs et membres de la Chambre des représentants américains, notamment pour justifier des positions sur l'aide à l'Ukraine. L'exploitation peut aussi inclure l'alimentation de la propagande interne — les narratifs anti-occidentaux de Storm-1516 sont systématiquement repris par des canaux Telegram russophones pour alimenter le récit domestique russe.

## 6.2 Le framework DISARM

Le framework DISARM (*Disinformation Analysis and Risk Management*), anciennement AMITT, est le principal cadre de référence pour décrire les opérations d'influence de manière structurée. Créé en 2018, il reprend la logique de la matrice MITRE ATT&CK en cybersécurité : une matrice de tactiques, techniques et procédures (TTPs) adaptée au domaine informationnel.

DISARM structure les opérations en quatre grandes phases — planification, préparation, exécution, évaluation — et décompose chaque phase en tactiques (étapes de haut niveau) et techniques (activités observables). Par exemple, la tactique « Élaborer les récits » (TA14) inclut des techniques comme « Exploiter des récits existants » (T0003), « Développer des récits contradictoires » (T0004), « Exploiter des théories conspirationnistes » (T0022) ou « Intégrer les vulnérabilités des audiences cibles dans les récits » (T0083).

VIGINUM a fait le choix stratégique d'exploiter DISARM pour standardiser ses pratiques et faciliter le partage de la connaissance au sein de la communauté de la lutte contre les manipulations de l'information. Le service a publié en février 2024 une traduction française de la matrice Red Team, déposée sur GitHub. L'EEAS utilise également DISARM dans le cadre STIX (*Structured Threat Information eXpression*) pour encoder les incidents FIMI de manière interopérable.

L'intérêt opérationnel de DISARM est double : il fournit un **langage commun** pour décrire les opérations (essentiel pour la coopération inter-agences et internationale) et il permet l'**analyse comparative** des TTPs entre différents acteurs et opérations, facilitant l'attribution (un acteur a un « style » opérationnel caractéristique). L'annexe B de ce cours présente la matrice de référence avec le mapping vers les chapitres.

## 6.3 Les indicateurs d'opération (IOI)

Par analogie avec les IoC (Indicators of Compromise) en cybersécurité, les IOI (*Indicators of Information Operations*) sont les marqueurs observables d'une opération d'influence. Ils portent sur trois dimensions.

**Indicateurs comportementaux** : création massive de comptes dans une fenêtre temporelle courte, patterns de publication coordonnés (publications à quelques minutes d'intervalle), ratios d'engagement anormaux (un compte avec 50 followers dont les posts obtiennent 5000 retweets), activité à des horaires incompatibles avec le fuseau horaire affiché, utilisation de copy-pasta (messages identiques ou quasi identiques publiés par de nombreux comptes).

**Indicateurs d'infrastructure** : domaines enregistrés récemment chez des registrars anonymes, serveurs hébergés chez des hébergeurs complaisants (*bulletproof hosting*), certificats SSL partagés entre plusieurs sites apparemment sans lien, utilisation de services d'anonymisation (Cloudflare, Njalla), templates WordPress identiques sur des sites différents.

**Indicateurs de contenu** : narratifs apparaissant simultanément sans antécédent organique, contenu traduit avec des erreurs idiomatiques spécifiques, images générées par IA avec des artefacts caractéristiques, documents fuitées dont la provenance ne peut être établie, contenu émotionnellement chargé et polarisant de manière systématique.

La détection repose sur la convergence de ces indicateurs — un indicateur isolé est un signal faible, un faisceau d'indicateurs convergents est un signal exploitable. La qualification comme opération d'influence suppose une analyse approfondie qui distingue la coordination inauthentique d'une mobilisation organique intense (Ch.12).

## 6.4 Le rapport coût/impact

Les opérations d'influence sont probablement l'arme la plus rentable du spectre hybride. Le budget mensuel de l'IRA pour l'opération 2016 était estimé à 1,25 million de dollars — une fraction infinitésimale du budget de défense d'un État, pour un impact politique considérable. Le coût d'une opération de type Storm-1516 est probablement encore plus faible : quelques opérateurs, des outils d'IA générative accessibles, une infrastructure web modeste. Le 4e rapport EEAS utilise d'ailleurs le concept de « FIMI Deterrence Playbook » qui vise précisément à augmenter le coût des opérations pour les acteurs malveillants, en frappant les maillons critiques (intermédiaires, proxies, fournisseurs de services).

L'asymétrie est structurelle : créer et diffuser une fausse information est rapide et peu coûteux. La détecter, la qualifier, l'attribuer et la contrer demande infiniment plus de temps, de compétences et de ressources. C'est le « dilemme du défenseur » informationnel — un concept qui résonne directement avec le même dilemme en cybersécurité.

## 6.5 Cas concret détaillé : reconstruction d'une opération documentée

Pour illustrer le cycle opérationnel, prenons l'exemple reconstitué d'une opération Storm-1516 documentée par VIGINUM. En octobre 2024, le MOI a diffusé un faux témoignage vidéo accusant Timothy Walz, colistier de Kamala Harris, d'avoir agressé sexuellement l'un de ses anciens élèves.

**Préparation.** La vidéo met en scène un individu se présentant comme « Matthew Metro », réel ancien élève du lycée concerné dont les traits ont probablement été usurpés à partir de photos collectées sur ses comptes de réseaux sociaux. Un compte X (@MattMetro) a été créé en octobre 2023, un an avant l'opération — illustrant l'anticipation dans la phase de préparation.

**Déploiement.** La vidéo a été publiée sur le compte @MattMetro et primo-diffusée par des comptes jetables maîtrisés par les opérateurs.

**Amplification.** Le contenu a été repris et amplifié par des influenceurs liés à la FCI et la BJA, relayé par des médias pro-russes, et partagé sur Telegram. En moins de 24 heures, la vidéo a atteint plus de cinq millions de vues sur X.

**Exploitation.** Le narratif visait à décrédibiliser le ticket démocrate à quelques semaines de l'élection présidentielle américaine. Le fait que des médias et fact-checkers aient dû répondre et démonter le faux témoignage a lui-même contribué à amplifier la visibilité du narratif — l'effet Streisand inversé.

---
