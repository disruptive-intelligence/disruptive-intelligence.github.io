---
title: Chapitre 22 — Contre-élicitation et protection des informations
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie V — Défense ET contre-ingénierie sociale
  - index.md
---

## 22.1 Reconnaître une tentative d'élicitation

La détection d'une élicitation en cours est difficile précisément parce que l'élicitation est conçue pour ressembler à une conversation normale. Les signaux d'alerte sont subtils et contextuels.

**Questions inhabituellement spécifiques.** Une conversation de salon professionnel qui passe de « dans quel secteur travaillez-vous ? » à « quels algorithmes utilisez-vous pour la compensation inertielle ? » en quelques minutes présente une escalade de spécificité anormale.

**Flatterie excessive.** « Vous êtes vraiment la personne la plus compétente que j'ai rencontrée sur ce sujet » — en provenance d'un inconnu rencontré il y a 10 minutes — doit activer un signal d'alerte.

**Réciprocité forcée.** L'interlocuteur partage ostensiblement des informations (réelles ou fabriquées) sur son propre travail et attend visiblement un échange réciproque.

**Demande de confidentialité.** « Je préférerais qu'on continue cette discussion en dehors du cadre officiel » ou « pourrait-on en discuter par WhatsApp plutôt que par email professionnel ? » — la transition vers un canal non contrôlé est un signal fort.

**Intérêt disproportionné pour le réseau.** « Est-ce que vous connaissez le responsable du programme X ? » ou « pourriez-vous me mettre en contact avec votre collègue qui travaille sur Y ? » — l'utilisation de la cible comme vecteur vers d'autres cibles.

## 22.2 Les techniques de contre-élicitation

**Le pont.** Répondre à une question par une question. « Et vous, dans quel domaine travaillez-vous exactement ? » Le pont renverse la dynamique de l'élicitation et permet d'évaluer l'interlocuteur.

**La déviation.** Changer de sujet naturellement. « C'est intéressant. Au fait, vous avez vu la keynote de ce matin ? » La déviation n'éveille pas de soupçon si elle est exécutée avec fluidité.

**La réponse vague.** Donner l'impression de répondre sans rien dire d'exploitable. « On travaille sur des sujets similaires à ce qui se fait dans le secteur, avec les contraintes que vous pouvez imaginer. » La cible a l'impression d'avoir répondu, l'éliciteur n'a rien obtenu de spécifique.

**Le signalement discret.** Si l'interlocuteur est identifié comme une menace potentielle (signaux forts d'élicitation, profil incohérent, insistance), le signalement doit être fait au retour : briefing au RSSI ou au responsable sécurité, avec autant de détails que possible (nom, entreprise, carte de visite, sujets abordés, questions posées).

## 22.3 Protection en salon et en conférence

La protection des informations en contexte de salon professionnel repose sur un dispositif en trois temps : brief avant départ (quelles informations sont communicables, quelles informations sont interdites, quels sont les pays et les interlocuteurs à risque), comportement sur place (messages autorisés, gestion des sollicitations, utilisation des dispositifs numériques), et debriefing au retour (avec qui avez-vous échangé ? quelles questions vous ont été posées ? avez-vous observé quelque chose d'inhabituel ?). Ce dispositif est détaillé dans le cours Intelligence Économique (Ch.8) — il est repris ici dans sa dimension spécifique à la contre-ingénierie sociale.

## 22.4 Protection en voyage professionnel

Certains pays présentent des risques d'ingérence particulièrement élevés. Sans nommer de pays spécifiques (les listes évoluent et sont publiées par les services compétents — DGSI, ANSSI, services homologues), les risques incluent : la surveillance des communications (chambres d'hôtel, réseaux WiFi), les approches physiques (contacts « spontanés » dans les hôtels, les bars, les événements), et le ciblage des dispositifs numériques (inspection aux frontières, clonage de téléphone). Les règles de protection incluent : ne jamais laisser de dispositifs sans surveillance, utiliser un téléphone dédié (sans données sensibles), chiffrer les communications, ne pas discuter de sujets sensibles en public, et signaler toute approche suspecte au retour.

## 22.5 Protection des VIP et des cibles à haute valeur

Les dirigeants, les responsables R&D, les cadres travaillant sur des programmes sensibles, et les personnels ayant des habilitations de sécurité nécessitent un dispositif de protection adapté sans être transformés en paranoïaques. Le dispositif inclut : une évaluation de la surface d'exposition personnelle (OSINT sur eux-mêmes — que trouverait un attaquant ?), des recommandations de sécurité des réseaux sociaux (paramètres de confidentialité, gestion du contenu professionnel et personnel), un protocole de communication sécurisé pour les sujets sensibles, et une sensibilisation spécifique aux techniques d'élicitation et de ciblage qui visent leur profil.

---
