---
title: Chapitre 4 — Les profils vulnérables et les facteurs de risque
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 4.1 Qui est vulnérable ? Tout le monde

Le mythe de la victime naïve est l'un des plus dangereux en social engineering. Il crée un faux sentiment de sécurité chez les individus qui se considèrent trop informés, trop intelligents ou trop expérimentés pour être piégés. La réalité est exactement inverse : les experts se font piéger aussi souvent que les novices — simplement par des techniques adaptées à leur profil.

Un RSSI qui détectera un phishing grossier peut se laisser piéger par un spear-phishing hautement personnalisé qui exploite son ego professionnel (« votre expertise est reconnue dans le secteur, nous aimerions vous inviter comme keynote speaker »). Un ingénieur R&D qui ignore les emails suspects peut succomber à une élicitation de face-à-face menée par un faux chercheur universitaire qui parle son langage technique. Un dirigeant qui se méfie des appels inconnus peut être vulnérable à une fraude au président menée par deepfake vocal lors d'une visioconférence apparemment légitime.

La vulnérabilité n'est pas une caractéristique personnelle — c'est une situation. Le même individu peut être vigilant dans un contexte et vulnérable dans un autre. Comprendre les facteurs de risque contextuels est bien plus utile que de profiler des « victimes types ».

## 4.2 Les facteurs de risque contextuels

Certaines situations augmentent significativement la vulnérabilité au social engineering, indépendamment de la compétence ou de l'intelligence de l'individu.

**Le nouveau poste.** Un employé récemment arrivé ne connaît pas encore les procédures, les visages, les habitudes de l'organisation. Il est en mode d'adaptation et d'apprentissage, ce qui le rend réceptif aux demandes de personnes qui semblent connaître l'entreprise mieux que lui. Le pretexting classique « je suis de l'IT, je dois configurer votre poste » est particulièrement efficace sur les nouveaux arrivants.

**Le voyage professionnel.** L'isolement géographique, la désorientation culturelle, le décalage horaire et l'absence du cadre de sécurité habituel (collègues de confiance, procédures connues) créent une fenêtre de vulnérabilité. Les services de renseignement exploitent systématiquement les voyages professionnels dans certains pays : chambre d'hôtel surveillée, contacts « spontanés » dans les bars d'hôtel, invitations à des événements sociaux (voir Ch.22 pour les contre-mesures).

**Le salon professionnel.** L'ouverture sociale est la norme : échanger des cartes de visite, discuter de ses projets, nouer des contacts est le but même de la participation. Cette ouverture crée un environnement idéal pour l'élicitation : les barrières sociales habituelles sont abaissées, la curiosité intellectuelle est stimulée, et le contexte professionnel légitime les questions sur l'activité de l'entreprise.

**La période de stress ou de conflit professionnel.** Un employé en conflit avec sa hiérarchie, menacé de licenciement, sous-estimé ou frustré dans ses ambitions est plus réceptif aux approches extérieures — qu'il s'agisse d'un faux recruteur qui propose une « opportunité de carrière » ou d'un interlocuteur qui offre reconnaissance et écoute. Ce facteur est l'un des leviers classiques du recrutement de sources par les services de renseignement.

**La transition de carrière.** Un employé en fin de contrat, en pré-retraite ou en recherche active d'emploi est structurellement réceptif aux propositions professionnelles — et donc aux approches de faux recruteurs.

## 4.3 Le modèle MICE et ses extensions

Le modèle MICE (Money, Ideology, Coercion, Ego) est le cadre classique du renseignement pour analyser les motivations d'un individu à collaborer comme source. Il reste pertinent en 2025, mais il a été étendu pour mieux refléter la diversité des leviers.

**Money.** La motivation financière reste un levier puissant, particulièrement pour les individus qui perçoivent un décalage entre leur contribution et leur rémunération, ou qui traversent des difficultés financières. Les « consultations rémunérées » proposées par de faux cabinets de conseil sont un vecteur classique.

**Ideology.** L'adhésion à une cause — politique, environnementale, religieuse, nationaliste — peut motiver la divulgation d'informations. Ce levier est moins fréquent en contexte d'entreprise qu'en contexte étatique, mais il existe (lanceurs d'alerte convaincus de servir l'intérêt public, employés politisés ciblés par des acteurs étrangers partageant apparemment les mêmes convictions).

**Coercion.** Le chantage, la compromission (kompromat) et les menaces constituent le levier le plus risqué et le moins stable — une source recrutée par la coercition est une source hostile qui cherchera à se libérer. En contexte de red team, ce levier est formellement interdit.

**Ego.** La flatterie, la reconnaissance, le sentiment d'être un interlocuteur privilégié sont des leviers extrêmement efficaces, en particulier auprès d'experts techniques qui manquent de reconnaissance dans leur organisation. Le modèle RASCLS (Reciprocity, Authority, Scarcity, Commitment, Liking, Social proof) étend l'analyse des leviers aux principes d'influence de Cialdini, offrant une grille d'analyse plus fine.

**Revenge.** La vengeance est un levier ajouté par les praticiens contemporains : un employé qui se sent trahi par son employeur (licenciement perçu comme injuste, promotion ratée, conflit avec la hiérarchie) peut être motivé par le désir de « punir » l'organisation.

## 4.4 Les insiders involontaires

La distinction entre insider malveillant et insider involontaire est fondamentale. L'insider malveillant agit délibérément contre les intérêts de son organisation (vol de données, sabotage). L'insider involontaire est un employé légitime, loyal et bien intentionné, qui divulgue des informations ou accorde des accès sans réaliser qu'il est manipulé.

L'insider involontaire est la cible privilégiée du social engineering et de l'élicitation. Il ne sait pas qu'il participe à une opération hostile. Le « recruteur » LinkedIn avec qui il échange depuis trois mois lui semble être un contact professionnel légitime. Le « technicien de maintenance » à qui il a tenu la porte dans le couloir avait un badge qui ressemblait au bon. L'email qui lui demandait de « mettre à jour ses identifiants » venait d'une adresse qui ressemblait à celle de la DSI.

La détection des insiders involontaires passe par la formation (reconnaître les signaux d'élicitation), les processus (vérification des demandes sensibles) et la surveillance comportementale (détection d'accès anormaux), mais aussi par une culture où le signalement d'un doute est encouragé sans conséquence négative pour celui qui signale.

## 4.5 Le profilage éthique en contexte red team

Dans un test de social engineering autorisé, le red teamer évalue la vulnérabilité des individus pour déterminer les cibles les plus probables et les pretextes les plus efficaces. Ce profilage est nécessaire — mais il doit respecter des limites strictes.

**Ce qu'on observe et exploite** : le rôle dans l'organisation (accès, responsabilités), le comportement professionnel observable (présence en conférence, publications, activité LinkedIn), les habitudes de travail visibles (horaires, déplacements, habitudes de pause), le niveau de familiarité avec les procédures de sécurité.

**Ce qu'on n'observe pas et n'exploite jamais** : les problèmes personnels (santé, finances, vie sentimentale, addictions), les situations de vulnérabilité individuelle (deuil, divorce, problèmes familiaux), les opinions politiques ou religieuses, les données sensibles au sens du RGPD.

La ligne est claire dans le principe, mais elle peut être floue en pratique. Un red teamer qui découvre, au cours de sa reconnaissance OSINT, qu'un employé traverse un divorce difficile (information visible sur les réseaux sociaux) ne doit pas utiliser cette information pour personnaliser son approche, même si un attaquant réel le ferait. Le red teamer teste les défenses de l'organisation, pas les faiblesses personnelles des individus.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 2**
>
> **Phase de reconnaissance.** Nathan et Yasmine lancent la reconnaissance OSINT sur Helios Aéronautique. En trois jours, ils collectent un volume d'information considérable.
>
> **LinkedIn** : 350 profils identifiés, dont 42 cadres et 28 ingénieurs R&D. L'organigramme est reconstitué à 80 %. Le DSI s'appelle Frédéric Morin. Le responsable de la production à Bordeaux est Jean-Marc Duval. Trois ingénieurs R&D publient régulièrement sur des conférences techniques. Le prestataire de maintenance informatique est identifié grâce à un post LinkedIn d'un de ses techniciens mentionnant une intervention chez Helios.
>
> **Offres d'emploi** : 12 annonces en cours révèlent la stack technique (Microsoft 365, Azure AD, SAP, SolidWorks, un ERP maison) et les compétences recherchées (ingénieur simulation, technicien qualité, développeur .NET).
>
> **Réseaux sociaux personnels** : photos de la soirée d'entreprise sur Instagram → badges visibles sur 4 photos (format, couleur, logo, puce RFID apparente). Post Facebook d'un employé : « Super formation incendie ce matin, on a tous évacué par la sortie Est ». Géolocalisation de posts TikTok par deux jeunes employés → identification de l'entrée fumoir côté parking.
>
> **Site web et presse** : communiqué de presse sur le contrat de sous-traitance défense (confirme l'enjeu stratégique), photos du siège (architecture, entrées, parking), rapport RSE mentionnant le prestataire de ménage et le traiteur de la cantine.
>
> Nathan rédige le dossier de reconnaissance et commence à construire les pretextes.

---
