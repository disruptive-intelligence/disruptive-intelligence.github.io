---
title: Chapitre 3 — Le HUMINT dans le monde du renseignement
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 3.1 Définition et cadre

HUMINT (Human Intelligence) désigne la collecte de renseignement par l'intermédiaire de sources humaines. C'est le plus ancien des « INTs » — bien avant l'existence de SIGINT (interception de communications), IMINT (imagerie satellite) ou OSINT (sources ouvertes), les espions recueillaient de l'information par la conversation, l'observation et la relation interpersonnelle. Le HUMINT reste, en 2025, irremplaçable pour certains types d'information : les intentions d'un décideur, les projets non encore documentés, les arbitrages internes d'une organisation, les vulnérabilités d'un processus qui n'apparaissent dans aucun système.

Le HUMINT ne se confond pas avec le social engineering, même si les deux disciplines partagent des techniques communes (élicitation, pretexting, rapport building). Le social engineering vise généralement un objectif tactique précis (obtenir un mot de passe, un accès, une action) dans un temps court. Le HUMINT s'inscrit dans une logique stratégique, souvent sur des mois ou des années, avec un objectif de collecte continue. Le social engineering peut être le premier acte d'une opération HUMINT, mais le HUMINT est un processus structuré qui va bien au-delà.

## 3.2 Le cycle HUMINT

Le cycle HUMINT suit une progression méthodique en cinq phases. Chaque phase a ses techniques, ses risques et ses contre-mesures.

**Le repérage (spotting).** C'est l'identification de cibles potentielles — des individus qui ont accès à l'information recherchée et qui présentent des facteurs de vulnérabilité exploitables. Le repérage repose massivement sur l'OSINT : profils LinkedIn, publications professionnelles, présence en conférence, réseau social. Un ingénieur R&D qui publie régulièrement sur ses projets, participe à des conférences internationales et affiche un réseau LinkedIn ouvert est une cible de repérage évidente. Le repérage évalue aussi les facteurs de motivation : insatisfaction professionnelle, ambition bloquée, difficultés financières, ego surdimensionné.

**Le développement (development).** C'est l'établissement du contact et la construction progressive de la relation. Le « developmental contact » est conçu pour paraître naturel : rencontre en conférence, connexion LinkedIn via un intérêt commun, invitation à un séminaire, proposition de collaboration académique. L'objectif n'est pas d'obtenir de l'information immédiatement — c'est de créer un lien de confiance qui sera exploité ultérieurement. La patience est l'arme fondamentale du HUMINT : des semaines ou des mois de contacts apparemment anodins avant la première demande significative.

**Le recrutement (recruitment).** C'est la transformation du contact en source active. Le recrutement peut être explicite (la source sait qu'elle collabore avec un service de renseignement) ou implicite (la source livre de l'information sans réaliser la nature réelle de son interlocuteur). Le recrutement exploite les leviers classiques du modèle MICE : Money (rémunération), Ideology (adhésion à une cause), Coercion (chantage, compromission), Ego (reconnaissance, flatterie). Dans la pratique contemporaine, le recrutement par l'ego et la rémunération est bien plus courant que le recrutement par la coercition — cette dernière étant plus risquée et moins stable.

**L'exploitation.** C'est la phase de collecte structurée. La source fournit de l'information selon un cadre défini par le traitant : questions ciblées, documents, accès à des réunions, identification d'autres cibles potentielles. L'exploitation est gérée avec soin pour ne pas « brûler » la source (ne pas la mettre en danger en demandant trop ou trop vite).

**La gestion (handling).** C'est la maintenance de la relation et de la sécurité opérationnelle : canaux de communication sécurisés, rendez-vous discrets, rémunération, soutien psychologique, gestion des crises (si la source est soupçonnée). La gestion est souvent la phase la plus longue et la plus délicate du cycle HUMINT.

## 3.3 Les services de renseignement et l'élicitation d'entreprise

Les services de renseignement étrangers ciblent activement les employés des entreprises stratégiques et des administrations. Ce n'est pas une menace théorique : la DGSI publie régulièrement des alertes sur les tentatives d'ingérence économique visant les entreprises françaises dans les secteurs de la défense, de l'aéronautique, de l'énergie, des télécommunications et de la recherche.

Les vecteurs de contact les plus fréquents sont les salons professionnels internationaux (où les cibles sont accessibles, ouvertes au networking et éloignées de leur cadre de sécurité habituel), les plateformes professionnelles en ligne (LinkedIn est devenu le terrain de chasse principal pour le repérage et le contact initial), les invitations à des séminaires académiques ou professionnels dans certains pays, et les approches par des « journalistes », « consultants » ou « recruteurs » dont l'identité est difficile à vérifier.

Les signaux d'alerte d'une tentative d'élicitation par un service de renseignement incluent : des questions inhabituellement spécifiques sur des projets ou des technologies internes, une insistance à déplacer la conversation vers un canal privé (WhatsApp, Signal), une progression relationnelle rapide (invitation à dîner dès le premier contact), des propositions de rémunération pour des « consultations » ou des « expertises » vagues, un intérêt disproportionné pour le réseau professionnel de la cible, et un profil difficile à vérifier (entreprise opaque, parcours incohérent, photos de profil douteuses). Les techniques de contre-élicitation sont détaillées au Ch.22.

## 3.4 HUMINT d'entreprise vs HUMINT de renseignement

L'HUMINT d'entreprise — collecte d'information concurrentielle par des moyens humains légaux — partage des techniques avec l'HUMINT de renseignement (élicitation, observation, debriefing) mais opère dans un cadre juridique et éthique radicalement différent.

L'HUMINT d'entreprise légal se limite à la collecte d'informations disponibles ou accessibles par des moyens licites : conversations en salon professionnel (sans faux pretexte), debriefing de collaborateurs après un événement, analyse des déclarations publiques de concurrents, observation du marché. Il ne recourt ni à la tromperie, ni à l'usurpation d'identité, ni au recrutement de sources internes chez un concurrent. Le cadre est celui de la veille concurrentielle et de l'intelligence économique (renvoi vers le cours IE, Ch.8).

La ligne de démarcation est claire dans le principe, mais parfois floue dans la pratique. Une conversation spontanée en conférence où un concurrent partage volontairement des informations est de l'intelligence économique légitime. La même conversation, si elle est orchestrée sous un faux pretexte (se faire passer pour un journaliste ou un universitaire pour obtenir des informations concurrentielles), bascule dans l'illégalité.

## 3.5 Le rôle de l'OSINT dans le HUMINT

La reconnaissance en sources ouvertes est la phase préparatoire obligatoire de toute opération HUMINT. Aucun professionnel sérieux — qu'il soit red teamer, analyste en contre-ingérence ou agent de renseignement — n'aborde une cible sans avoir préalablement collecté et analysé toute l'information disponible en source ouverte.

L'OSINT alimente le HUMINT à chaque étape du cycle. En phase de repérage, elle identifie les cibles potentielles et évalue leur accessibilité (profil LinkedIn ouvert vs fermé, présence en conférence, publications). En phase de développement, elle fournit les éléments de personnalisation du contact (intérêts communs, parcours partagé, sujets de conversation). En phase d'exploitation, elle permet de formuler des questions d'élicitation pertinentes et de valider les réponses obtenues.

La qualité de la reconnaissance OSINT détermine directement la crédibilité du pretexte et donc le taux de succès de l'opération de social engineering. Un phishing générique envoyé à 10 000 adresses aura un taux de clic de 2 à 5 %. Un spear-phishing construit à partir d'une reconnaissance OSINT approfondie (terminologie interne, noms de projets, prestataires identifiés) aura un taux de clic de 20 à 40 %. La reconnaissance est le multiplicateur de force du social engineering. Les méthodes de reconnaissance OSINT sont détaillées au Ch.5 (renvoi vers le cours OSINT Mastery pour la profondeur méthodologique).

---
