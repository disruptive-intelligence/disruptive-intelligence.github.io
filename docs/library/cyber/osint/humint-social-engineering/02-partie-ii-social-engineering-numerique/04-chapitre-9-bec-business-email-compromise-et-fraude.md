---
title: Chapitre 9 — BEC (Business Email Compromise) et fraude au président
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie II — Social engineering numérique
  - index.md
---

## 9.1 Le BEC comme menace n°1 en pertes financières

Le Business Email Compromise est la forme de cybercriminalité la plus coûteuse au monde en termes de pertes financières directes. Les données de l'IC3 (Internet Crime Complaint Center) du FBI indiquent des pertes cumulées de plusieurs milliards de dollars par an aux États-Unis seuls. En France, les pertes liées à la fraude au président et aux arnaques au fournisseur se chiffrent en centaines de millions d'euros annuellement.

Le BEC est redoutable parce qu'il ne repose sur aucun composant technique sophistiqué : pas de malware, pas de vulnérabilité logicielle, pas de zero-day. C'est une attaque de pure manipulation humaine — un email suffisamment crédible pour déclencher un virement vers un compte contrôlé par l'attaquant. La détection technique est donc intrinsèquement limitée : l'email ne contient ni lien malveillant ni pièce jointe piégée — seulement du texte convaincant.

## 9.2 Les variantes du BEC

**La fraude au président (CEO fraud).** L'attaquant usurpe l'identité du dirigeant de l'entreprise et ordonne un virement urgent et confidentiel au responsable financier ou au comptable. Les éléments clés sont : l'urgence (« c'est pour une acquisition confidentielle, il faut agir avant 17h »), la confidentialité (« n'en parlez à personne d'autre — c'est stratégique et sensible »), l'autorité (le DG qui s'adresse directement à un subordonné en court-circuitant la hiérarchie normale) et la pression émotionnelle (« je compte sur vous personnellement »).

**La fraude au fournisseur (vendor email compromise).** L'attaquant se fait passer pour un fournisseur existant et envoie une facture avec des coordonnées bancaires modifiées. La technique est souvent précédée par la compromission de la boîte mail du fournisseur réel (reply-chain) ou par l'enregistrement d'un domaine lookalike. La détection est rendue difficile par le fait que la relation commerciale est réelle — seul l'IBAN a changé.

**La compromission de boîte mail (reply-chain BEC).** L'attaquant compromet une boîte mail interne ou celle d'un partenaire et s'insère dans des fils de conversation existants pour demander des virements ou des modifications de coordonnées bancaires. Cette variante est la plus difficile à détecter parce que l'email provient d'une adresse légitime avec un historique de conversation réel.

**Le faux avocat.** L'attaquant se présente comme un avocat ou un conseiller juridique intervenant dans le cadre d'une transaction confidentielle (acquisition, règlement de litige). La confidentialité est utilisée comme arme : « en raison de la sensibilité juridique de cette opération, je vous demande de ne pas en discuter avec vos collègues ». Cette tactique isole la cible et neutralise le réflexe de vérification.

## 9.3 La construction de l'arnaque

Le BEC réussi repose sur une reconnaissance approfondie. L'attaquant identifie : l'organigramme (qui a le pouvoir de valider un virement, qui est le supérieur hiérarchique direct), les processus de validation financière (seuils, doubles signatures, circuits de validation), les habitudes de communication du dirigeant usurpé (ton, style, formules de politesse, horaires d'envoi), et les fenêtres d'opportunité (déplacement du DG — vérifiable par LinkedIn, agenda public, conférences ; absence du DAF ; périodes de clôture comptable).

Le timing est critique. Le vendredi après-midi (les virements envoyés le vendredi ne sont pas vérifiés avant lundi), la veille de vacances, les périodes de déplacement du dirigeant (impossible de vérifier en personne) sont les fenêtres les plus exploitées.

## 9.4 Deepfake et BEC

L'utilisation de deepfakes vidéo et vocaux dans les BEC représente une évolution qualitative de la menace. Le cas de Hong Kong de début 2024, où une entreprise a perdu l'équivalent de 25 millions de dollars suite à une visioconférence entièrement composée de deepfakes en temps réel, illustre le potentiel destructeur de cette convergence. L'employé ciblé a participé à un appel vidéo où plusieurs participants — dont le CFO — étaient des deepfakes générés en temps réel. La qualité était suffisante pour ne pas éveiller de soupçon pendant toute la durée de l'appel.

Cette évolution remet en question les défenses traditionnelles du BEC. Le callback vocal était considéré comme une contre-mesure fiable — mais si la voix de l'interlocuteur peut être clonée, le callback perd son pouvoir de vérification. La réponse passe par des vérifications multi-facteurs non reproductibles par l'IA : question de sécurité personnelle, vérification physique en présentiel, code de confirmation envoyé par un canal distinct et préétabli.

## 9.5 Défense contre le BEC

La défense contre le BEC est fondamentalement procédurale, pas technologique. Les solutions techniques (détection d'anomalies dans les emails, alerte sur les changements de comportement d'expéditeur) sont utiles mais insuffisantes face à des attaques qui n'utilisent aucun indicateur technique malveillant.

**P0 — Processus de double validation pour tout virement inhabituel.** Aucun virement supérieur à un seuil défini ne peut être exécuté sans validation par deux personnes distinctes, dont au moins une par callback sur un numéro de référence connu (annuaire interne, pas le numéro indiqué dans l'email).

**P0 — Procédure de vérification des changements de coordonnées bancaires.** Tout changement d'IBAN (fournisseur, prestataire, client) fait l'objet d'un callback au fournisseur sur un numéro de référence connu, indépendamment du canal par lequel le changement a été demandé.

**P1 — Formation ciblée.** Les profils à risque (DAF, comptabilité, assistantes de direction, service achats) reçoivent une formation spécifique sur les scénarios de BEC avec des simulations réalistes.

**P1 — Alertes techniques.** Règles email signalant les emails d'expéditeurs externes utilisant des display names identiques à ceux de dirigeants internes, bannières « email externe » clairement visibles, alertes sur les domaines lookalike.

**P2 — Culture de la vérification.** Créer un environnement où vérifier une demande — même du DG — est perçu comme professionnel, pas comme de l'insubordination.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 3**
>
> **Campagne de phishing.** Yasmine lance la campagne de phishing ciblé depuis l'infrastructure de test (domaine enregistré : heIios-rh.fr — « I » majuscule au lieu de « l »). Deux pretextes sont utilisés :
>
> **Pretexte 1** — « Mise à jour obligatoire du portail RH — Entretien annuel 2025 ». Email reproduisant le template visuel d'Helios (couleurs et logo récupérés sur le site web), renvoyant vers une page de connexion Microsoft 365 factice. Envoyé à 80 employés du siège et de Bordeaux le lundi matin à 8h15.
>
> **Pretexte 2** — « Invitation conférence Aéronautique & Défense — Lyon, juin 2025 ». Email ciblé sur 40 ingénieurs R&D et cadres, exploitant l'intérêt professionnel et la curiosité.
>
> **Résultats après 72h** : sur 120 emails envoyés, 34 clics (28,3 %), 18 identifiants collectés (15 %), dont 2 comptes avec des privilèges administrateurs IT (un admin Exchange et un admin Azure AD). Taux de signalement au SOC : 3 emails signalés (2,5 %) — tous dans les 4 premières heures, puis plus rien.
>
> Lucie Ferraro, la RSSI, est surprise par les résultats : « On fait des campagnes de sensibilisation e-learning chaque trimestre depuis deux ans. Les scores au quiz sont bons. » Nathan explique : « Le quiz mesure la reconnaissance théorique des signaux de phishing dans un contexte d'examen. Notre campagne mesure le comportement réel face à un leurre crédible, en conditions de stress et de multitâche. Ce sont deux choses différentes. »

---
