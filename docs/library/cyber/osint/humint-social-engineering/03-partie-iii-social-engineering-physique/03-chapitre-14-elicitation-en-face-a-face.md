---
title: Chapitre 14 — Élicitation en face-à-face
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie III — Social engineering physique
  - index.md
---

## 14.1 Définition et fondements

L'élicitation est l'extraction d'information dans le cadre d'une conversation apparemment normale et non menaçante. La cible ne sait pas qu'elle est interrogée — elle pense participer à une conversation ordinaire. C'est précisément ce qui rend l'élicitation si efficace et si difficile à détecter : il n'y a ni demande explicite suspecte, ni canal d'attaque technique, ni pièce jointe à analyser — seulement une conversation.

L'agence américaine NSA définit l'élicitation comme « l'extraction subtile d'information au cours d'une conversation apparemment normale et innocente ». Cette définition est opérationnellement exacte : le succès de l'élicitation repose sur le fait que la cible perçoit l'échange comme naturel, réciproque et bienveillant.

L'élicitation fonctionne pour des raisons psychologiques documentées : la plupart des gens souhaitent être perçus comme compétents et bien informés (ego), désirent aider un interlocuteur sympathique (réciprocité, politesse), sont mal à l'aise avec le silence et le comblent en parlant (anxiété sociale), et ne mentent pas spontanément quand la conversation semble anodine (honnêteté par défaut).

## 14.2 Les techniques d'élicitation

**La question ouverte.** « Comment se passe le projet de migration ? » La question ouverte invite un développement libre — la cible choisit les détails qu'elle partage, ce qui donne l'impression de contrôle alors que l'éliciteur oriente la conversation vers les sujets d'intérêt.

**La provocation (deliberate false statement).** Affirmer volontairement quelque chose de faux pour provoquer une correction. « J'ai entendu dire que vous migriez vers SAP S/4HANA ? » Si la réponse est « Non, on est sur Oracle depuis janvier, c'est tout nouveau », l'éliciteur a obtenu une information technique spécifique sans l'avoir demandée — la cible l'a « corrigé » spontanément. Cette technique exploite le besoin de précision et la difficulté à laisser une erreur non corrigée.

**La flatterie ciblée.** « Vous êtes probablement la personne la mieux placée pour comprendre ce sujet dans l'entreprise. » La flatterie active le mécanisme de réciprocité (la cible se sent valorisée et veut « mériter » le compliment en démontrant sa compétence) et l'ego (plaisir de la reconnaissance).

**Le partage réciproque.** Offrir une information (réelle ou fabriquée) pour créer une obligation de réciprocité. « Chez nous, on a eu un mal fou avec la certification DO-178C — et vous ? » L'éliciteur qui partage d'abord crée un précédent d'ouverture et une attente de réciprocité.

**Le silence stratégique.** Après avoir posé une question, ne pas combler le silence. La plupart des gens sont mal à l'aise avec le vide conversationnel et le comblent en développant — souvent au-delà de ce qu'ils avaient initialement prévu de partager. Le silence stratégique est l'un des outils les plus puissants et les plus sous-utilisés de l'élicitation.

**L'expression de l'ignorance.** « Je ne comprends pas du tout comment fonctionne votre système de badgeage — ça a l'air complexe. » L'ignorance affichée active le besoin d'expliquer et de démontrer sa compétence.

## 14.3 La gestion de la conversation

L'élicitation réussie suit une progression contrôlée : création du rapport → conversation anodine → transition naturelle vers les sujets d'intérêt → extraction d'information → désengagement propre.

**Créer le rapport.** Le rapport (relation de confiance conversationnelle) se construit par le mirroring (reproduire subtilement la posture, le rythme de parole, le vocabulaire de la cible), l'écoute active (reformulation, signaux d'attention — hochements de tête, « je vois », « intéressant »), l'identification de points communs (parcours, intérêts, expériences partagées) et le respect du tempo de la cible (ne pas presser, laisser la conversation se développer naturellement).

**Orienter sans diriger.** L'éliciteur guide la conversation par des questions de relance (« et comment ça se passe concrètement ? »), des ponts thématiques (« en parlant de sécurité, d'ailleurs... ») et des manifestations d'intérêt sélectif (approfondir les sujets utiles, survoler les autres). La cible ne doit jamais avoir l'impression d'être interrogée.

**Escalader progressivement.** Commencer par des sujets anodins (l'entreprise en général, le secteur, l'actualité professionnelle), puis avancer vers des sujets plus spécifiques (le projet en cours, les outils utilisés, les défis techniques) et enfin vers les sujets sensibles (les failles de sécurité, les informations confidentielles, les projets non annoncés). Chaque palier valide que la cible est à l'aise avant de monter au suivant.

**Désengager proprement.** La fin de la conversation doit être naturelle et ne pas éveiller de soupçons. Prétexte de départ (« je dois aller à ma prochaine réunion »), remerciement chaleureux, échange de coordonnées (renforce la perception de normalité de l'échange). La cible doit quitter la conversation en se sentant bien — pas en se demandant pourquoi on lui a posé autant de questions.

## 14.4 Les contextes d'élicitation

**Salon professionnel et conférence.** L'environnement idéal pour l'élicitation : la norme sociale est au networking, les barrières sont abaissées, les participants sont en mode « ouverture » et « échange ». Les pauses café, les cocktails et les dîners de gala sont les moments les plus propices. Le bar d'hôtel après une journée de conférence est le terrain de chasse classique de l'élicitation — fatigue, alcool et décompression réduisent la vigilance.

**Voyage professionnel.** Avion, train, salle d'attente d'aéroport — les voyages créent des opportunités de conversation prolongée avec une cible isolée de son contexte habituel. Les vols long-courriers offrent plusieurs heures de conversation potentielle.

**Événement d'entreprise.** Soirée de Noël, séminaire d'équipe, pot de départ — les événements internes mélangent registres professionnel et social, ce qui facilite l'élicitation (la conversation est à la fois professionnelle et personnelle, ce qui rend les questions sur le travail naturelles).

## 14.5 L'élicitation par les services de renseignement étrangers : signaux et continuum

Les services de renseignement utilisent l'élicitation comme technique de base pour évaluer les cibles potentielles et collecter de l'information avant une éventuelle tentative de recrutement. Le processus suit un continuum identifiable : spotting (identification de la cible), assessment (évaluation de l'accès et de la vulnérabilité), developmental contact (établissement d'un lien), cultivation (renforcement progressif de la relation), elicitation ladder (montée en sensibilité des sujets abordés), et potentiellement tentative de recrutement.

Les signaux d'alerte incluent : un interlocuteur dont le profil ou l'entreprise est difficile à vérifier, des questions qui semblent anodines mais qui portent systématiquement sur des sujets sensibles (projets R&D, contrats, technologies), une transition rapide vers un canal de communication privé (WhatsApp, Signal), des propositions de « consulting » ou de « collaboration académique » rémunérées mais vagues, un intérêt disproportionné pour le réseau professionnel de la cible, et une relation qui progresse anormalement vite (invitation à dîner dès la première rencontre).

Les techniques de contre-élicitation sont détaillées au Ch.22. Les cas d'ingérence documentés par la DGSI sont un excellent support de formation.

---
