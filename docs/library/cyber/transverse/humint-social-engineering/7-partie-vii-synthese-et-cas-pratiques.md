---
title: PARTIE VII — SYNTHÈSE ET CAS PRATIQUES
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 7
chapters: 7
---

---

### Chapitre 29 — Cas de synthèse : opération de social engineering multi-vecteurs

**Scénario complet.** L'étudiant analyse une opération de social engineering reconstituée couvrant l'ensemble du spectre : reconnaissance OSINT → spear-phishing → vishing → intrusion physique → élicitation → exploitation → détection → investigation → remédiation.

**Contexte.** Un cabinet d'avocats d'affaires parisien (150 employés, données clients hautement confidentielles, associés voyageant fréquemment) est ciblé par un groupe criminel spécialisé dans le BEC. L'opération se déroule sur 4 semaines.

**Phase 1 — Reconnaissance.** Le groupe collecte les profils LinkedIn des associés et des assistants, identifie les dossiers en cours (via les communiqués de presse et les annonces de transactions), cartographie l'organigramme et les processus de communication interne.

**Phase 2 — Spear-phishing ciblé.** Un email de phishing se faisant passer pour le service IT du cabinet est envoyé à 8 assistants. 3 cliquent. Les identifiants de 2 assistants sont capturés.

**Phase 3 — Reply-chain BEC.** Les identifiants d'une assistante sont utilisés pour accéder à sa boîte mail. Le groupe lit les échanges récents avec un client sur une transaction immobilière de 2 millions d'euros. Un email est inséré dans le fil de conversation demandant un virement vers de nouvelles coordonnées bancaires, en invoquant un changement de domiciliation bancaire du notaire.

**Phase 4 — Vishing de confirmation.** Le groupe appelle l'assistante en se faisant passer pour le « cabinet du notaire » pour confirmer le changement d'IBAN et presser l'exécution du virement.

**Phase 5 — Détection et réponse.** Le virement est exécuté. 48h plus tard, le vrai notaire contacte le cabinet pour relancer le règlement. L'arnaque est découverte. Investigation, plainte, tentative de gel de fonds (partiellement réussie — 40 % des fonds récupérés).

**Analyse attendue.** L'étudiant identifie chaque technique utilisée, les leviers psychologiques exploités à chaque étape, les défenses qui auraient pu prévenir l'attaque (DMARC, bannière email externe, processus de vérification des changements d'IBAN, callback au notaire sur un numéro connu, formation des assistants au BEC), et rédige un rapport post-incident avec recommandations P0/P1/P2.

---

### Chapitre 30 — Le métier d'expert en social engineering

#### 30.1 Les métiers

Le social engineering professionnel couvre plusieurs métiers distincts.

**Red teamer SE / pentester spécialisé.** Exécution de tests d'intrusion social engineering (phishing, vishing, intrusion physique, élicitation) pour des organisations clientes. Travail en cabinet de conseil en cybersécurité ou en équipe interne de sécurité offensive.

**Consultant en sensibilisation.** Conception et délivrance de programmes de formation adaptés aux profils de risque. Développement de simulations réalistes (campagnes de phishing, exercices de vishing, tabletop exercises).

**Analyste en contre-ingénierie sociale.** Détection et analyse des tentatives de social engineering ciblant l'organisation. Veille sur les menaces, coordination avec les services de renseignement (DGSI pour l'ingérence étrangère), investigation sur les incidents.

**Formateur.** Enseignement des techniques de social engineering et de contre-ingénierie sociale dans un contexte académique ou professionnel.

**Enquêteur spécialisé.** Investigation post-incident, analyse forensique de campagnes de phishing, expertise judiciaire.

#### 30.2 Les compétences

Le profil du praticien en social engineering est par nature transversal : psychologie appliquée (compréhension des biais, des leviers d'influence, des dynamiques interpersonnelles), communication (aisance orale, capacité d'adaptation, gestion du stress en situation d'imposture), OSINT (maîtrise des techniques de reconnaissance en sources ouvertes), technique (compréhension des systèmes email, des protocoles d'authentification, des technologies de contrôle d'accès, des outils d'infrastructure), rédaction (capacité à produire des rapports clairs, factuels et actionnables), et éthique (discernement, intégrité, capacité à tracer et respecter des limites).

#### 30.3 Les certifications

Plusieurs certifications couvrent le social engineering, avec des niveaux de profondeur variables.

**SANS SEC567 — Social Engineering for Penetration Testers.** La formation de référence pour le red team social engineering (phishing, vishing, impersonation, pretexting). Coûteuse (formation SANS) mais reconnue.

**OSCP (Offensive Security Certified Professional).** L'OSCP couvre le pentesting global avec un volet social engineering limité — c'est une certification de pentesting technique plus que de social engineering.

**GPEN (GIAC Penetration Tester).** Couvre le pentesting incluant les aspects de social engineering dans une perspective globale.

**Certified Social Engineer (Social-Engineer.org).** Certification spécialisée en social engineering développée par Christopher Hadnagy. Pertinente mais moins largement reconnue que les certifications SANS/GIAC.

L'état du marché des certifications SE en 2025 est en évolution : la demande de compétences en social engineering augmente, mais les certifications spécialisées restent rares comparées aux certifications de pentesting technique. L'expérience pratique (campagnes réelles, rapports de red team, portfolio de missions) reste le critère de différenciation principal pour les recruteurs.

#### 30.4 L'éthique comme compétence fondamentale

Le praticien de social engineering possède un savoir-faire de manipulation interpersonnelle. Cette compétence confère un pouvoir — et la responsabilité qui l'accompagne est non négociable. L'éthique n'est pas une contrainte externe imposée au praticien : c'est une compétence interne qui guide chaque décision opérationnelle.

Les questions éthiques récurrentes incluent : jusqu'où aller dans la manipulation pendant un test autorisé ? Comment gérer la découverte de vulnérabilités personnelles d'un employé (addiction, problèmes financiers) pendant la reconnaissance ? Comment rédiger un rapport qui améliore les défenses sans humilier les individus ? Comment gérer la pression d'un commanditaire qui demande des résultats individuels nominatifs pour sanctionner des employés ?

La réponse à ces questions n'est pas dans un code de conduite abstrait — elle est dans le discernement professionnel du praticien, formé par l'expérience, la réflexion et le dialogue avec ses pairs.

#### 30.5 Perspectives de carrière

La demande de compétences en social engineering est en croissance structurelle. Les entreprises réalisent que la technologie seule ne suffit pas à protéger contre une menace qui exploite le facteur humain. Les réglementations (NIS2, DORA pour le secteur financier) renforcent les obligations de test de résilience, y compris les tests de social engineering. La menace IA (deepfakes, phishing personnalisé) renforce le besoin de praticiens capables de tester et de former.

Les trajectoires de carrière incluent : le consulting (missions de red team SE pour des clients variés), le poste en interne (responsable de la sensibilisation, responsable du red team interne, analyste en contre-ingérence), le management (direction d'un service de sécurité offensive, RSSI avec une spécialité en facteur humain), et la formation/recherche (enseignement, publication, conférences — DEF CON SE Village, Black Hat, les conférences SANS).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode final**
>
> **Le rapport.** Après 6 semaines de test, Nathan livre son rapport à Marc Tessier (DG) et Lucie Ferraro (RSSI) lors d'une restitution de 2 heures en comité restreint.
>
> **Résultats :**
> - **Phishing** : taux de clic 28,3 % (34/120), 18 identifiants collectés dont 2 comptes admin
> - **Vishing** : 4 tentatives d'appel au helpdesk pour reset de credentials — 2 réussies (50 %), dont 1 reset MFA sur un compte à privilèges
> - **Intrusion physique** : réussie sur 2 sites sur 3 (Bordeaux et Paris — échec à Toulouse où le gardien a refusé l'accès et appelé le responsable sécurité)
> - **Élicitation** : 4 réussites sur 6 tentatives en contexte informel (cantine, fumoir, café)
> - **Implant réseau** : déployé à Bordeaux, actif 72h avant détection par l'équipe réseau (alerte sur un nouveau device inconnu)
> - **Taux de signalement** : 2,5 % (3 emails signalés au SOC sur 120 envoyés)
>
> **Impact potentiel si exploitation réelle :** les 2 comptes admin compromis auraient permis l'accès au tenant Azure AD, à l'ensemble des emails (Exchange Online), aux fichiers SharePoint (dont les documents du programme de défense) et au VPN. L'implant réseau aurait permis l'exfiltration de données depuis le réseau de production de Bordeaux.
>
> **Cas du « recruteur » étranger :** Nathan intègre le cas de David Chen dans le rapport comme illustration de la menace de niveau étatique. Le rapport souligne que la même vulnérabilité humaine (réceptivité à la flatterie, absence de contre-élicitation) a été exploitée par le red team (exercice contrôlé) et par un acteur de renseignement étranger (menace réelle).
>
> **Recommandations P0 :** (1) Déployer FIDO2 sur tous les comptes à privilèges, (2) Renforcer les procédures de helpdesk (callback obligatoire, interdiction des resets MFA par téléphone seul), (3) Mettre en place une procédure de double validation pour les virements > 5 000 €.
>
> **Recommandations P1 :** (4) Formation ciblée par profil de risque (ingénieurs R&D : contre-élicitation, DAF : BEC, helpdesk : pretexting, réception : intrusion physique), (5) Migration vers DESFire EV2 pour le contrôle d'accès physique, (6) Tourniquets anti-tailgating aux accès principaux.
>
> **Recommandations P2 :** (7) Programme de simulation de phishing mensuel avec retour individualisé, (8) Brief systématique avant les salons professionnels et les voyages, (9) Audit OSINT de la surface d'exposition de l'entreprise (informations accessibles en source ouverte).
>
> Helios lance un programme de remédiation sur 12 mois. Nathan conclut sa restitution : « La meilleure défense technique ne vaut rien si un humain tient la porte. Et la meilleure formation ne vaut rien si la culture d'entreprise punit ceux qui signalent un doute plutôt que de les remercier. »


---


## ANNEXES

---

### Annexe A — Glossaire (80+ termes)

| Terme | Définition |
|---|---|
| **APT (Advanced Persistent Threat)** | Groupe de menace étatique ou para-étatique menant des campagnes d'intrusion sophistiquées et persistantes |
| **Assessment** | Phase HUMINT d'évaluation d'une cible potentielle (accès, motivation, vulnérabilité) |
| **Baiting** | Technique consistant à laisser un support piégé (clé USB, CD) dans un lieu où il sera trouvé et utilisé |
| **Bash Bunny** | Outil d'intrusion USB multi-payload émulant divers périphériques |
| **BEC (Business Email Compromise)** | Compromission de messagerie d'entreprise — arnaque par email ciblant les processus financiers |
| **Callback verification** | Contre-mesure consistant à rappeler un interlocuteur sur un numéro de référence connu avant d'agir |
| **Caller ID spoofing** | Falsification du numéro affiché lors d'un appel téléphonique |
| **CIB (Coordinated Inauthentic Behavior)** | Comportement inauthentique coordonné sur les réseaux sociaux |
| **Cialdini (principes de)** | Six (puis sept) principes d'influence : réciprocité, engagement, preuve sociale, autorité, sympathie, rareté, unité |
| **Clonage RFID** | Copie d'un badge RFID légitime sur un support vierge |
| **Consent phishing** | Attaque exploitant les mécanismes OAuth pour obtenir des permissions d'accès persistantes |
| **Contre-élicitation** | Ensemble de techniques pour détecter et neutraliser une tentative d'élicitation |
| **Credential harvesting** | Collecte d'identifiants (login/mot de passe) via un formulaire frauduleux |
| **Cultivation** | Phase HUMINT de renforcement progressif de la relation avec une cible |
| **Deepfake** | Contenu audio ou vidéo synthétique généré par IA imitant une personne réelle |
| **DESFire** | Technologie de carte à puce RFID haute fréquence (13,56 MHz) avec chiffrement AES |
| **Device code phishing** | Attaque exploitant le flux OAuth2 device code pour obtenir des tokens d'accès |
| **DGSI** | Direction Générale de la Sécurité Intérieure — service de renseignement français (contre-espionnage, contre-ingérence) |
| **DKIM (DomainKeys Identified Mail)** | Protocole de signature cryptographique des emails |
| **DMARC** | Protocole d'authentification email combinant SPF et DKIM avec politique de rejet |
| **Dream Job (opération)** | Campagne du groupe Lazarus utilisant de faux recruteurs LinkedIn |
| **Dumpster diving** | Fouille des poubelles à la recherche d'informations exploitables |
| **Élicitation** | Extraction d'information dans une conversation apparemment normale |
| **Evilginx** | Outil de phishing reverse proxy capturant les tokens de session MFA |
| **FIDO2 / WebAuthn** | Standard d'authentification résistant au phishing basé sur la cryptographie à clé publique |
| **Flipper Zero** | Outil multi-protocole portable (RFID, NFC, IR, Sub-GHz) |
| **Fraude au président** | Variante de BEC où l'attaquant usurpe l'identité du dirigeant |
| **Fraude au fournisseur** | Variante de BEC exploitant un changement frauduleux de coordonnées bancaires |
| **HUMINT (Human Intelligence)** | Collecte de renseignement par des sources humaines |
| **IDN (Internationalized Domain Name)** | Domaine utilisant des caractères Unicode — exploitable pour le typosquatting |
| **Impersonation** | Fait de se faire passer pour une autre personne |
| **Implant** | Dispositif matériel ou logiciel déployé pour maintenir un accès persistant |
| **Insider involontaire** | Employé manipulé qui divulgue des informations sans réaliser la manipulation |
| **Insider malveillant** | Employé agissant délibérément contre les intérêts de son organisation |
| **ITDR (Identity Threat Detection and Response)** | Technologie de détection des menaces liées à l'identité |
| **LAN Turtle** | Implant réseau se branchant sur un port Ethernet |
| **Lettre de mission** | Document contractuel autorisant un test d'intrusion et définissant son scope |
| **Lock picking** | Crochetage de serrure mécanique |
| **Lure** | Appât — le message ou le pretexte utilisé pour tromper la cible |
| **MFA (Multi-Factor Authentication)** | Authentification multifacteur |
| **MFA bombing / push fatigue** | Attaque par envoi massif de demandes de validation MFA |
| **MICE** | Modèle d'analyse des motivations de recrutement : Money, Ideology, Coercion, Ego |
| **Mirroring** | Technique de rapport : reproduire subtilement le comportement de l'interlocuteur |
| **Name-dropping** | Mention de noms de personnes connues de la cible pour renforcer la crédibilité |
| **NFC (Near Field Communication)** | Communication en champ proche — technologie sans contact à courte distance |
| **No-blame post-mortem** | Retex sans blâme individuel, focalisé sur l'amélioration des processus |
| **OAuth** | Protocole d'autorisation permettant à des applications tierces d'accéder à des ressources |
| **OPSEC (Operational Security)** | Sécurité opérationnelle — protection des informations sur ses propres opérations |
| **OSINT (Open Source Intelligence)** | Renseignement en sources ouvertes |
| **Pacing-leading** | Technique de rapport : s'aligner sur l'interlocuteur puis le guider |
| **PEACE (modèle)** | Modèle d'entretien professionnel britannique (non confrontationnel) |
| **Phishing** | Hameçonnage — tentative de collecte d'informations via un message frauduleux |
| **Pig butchering** | Modèle industriel d'arnaque sentimentale avec « engraissement » de la victime |
| **Piggybacking** | Variante du tailgating avec interaction sociale active |
| **Pretexting** | Construction et utilisation d'un scénario fictif (pretexte) pour manipuler une cible |
| **Proxmark3** | Outil de recherche et de test RFID/NFC |
| **Quishing** | Phishing via QR code |
| **RASCLS** | Extension du modèle MICE : Reciprocity, Authority, Scarcity, Commitment, Liking, Social proof |
| **Red team** | Équipe simulant un adversaire pour tester les défenses d'une organisation |
| **Reply-chain attack** | Attaque par insertion dans un fil de conversation email légitime |
| **Reverse proxy phishing** | Phishing interceptant la communication entre la cible et le service légitime (Evilginx) |
| **RFID** | Identification par radiofréquence — technologie de badges sans contact |
| **Rubber Ducky** | Clé USB émulant un clavier pour exécuter des commandes |
| **Rules of engagement** | Règles d'engagement — cadre opérationnel d'un test d'intrusion |
| **Safe word** | Mot de passe convenu permettant l'identification immédiate du red teamer |
| **SIM swapping** | Transfert frauduleux d'un numéro de téléphone vers une nouvelle carte SIM |
| **Smishing** | Phishing par SMS |
| **Spear-phishing** | Phishing ciblé sur un individu ou un groupe restreint |
| **Spoofing** | Usurpation technique (adresse email, numéro de téléphone, adresse IP) |
| **Spotting** | Phase HUMINT d'identification de cibles potentielles |
| **SPF (Sender Policy Framework)** | Protocole définissant les serveurs autorisés à envoyer des emails pour un domaine |
| **STIR/SHAKEN** | Protocole d'authentification de l'identité de l'appelant dans les réseaux téléphoniques |
| **Supply chain humaine** | Ensemble des prestataires et partenaires ayant un accès physique ou logique |
| **Tailgating** | Suivre un employé à travers une porte contrôlée sans badger |
| **Typosquatting** | Enregistrement de domaines avec des fautes de frappe imitant un domaine légitime |
| **UEBA** | User and Entity Behavior Analytics — analyse comportementale des utilisateurs |
| **Vishing** | Phishing vocal — social engineering par téléphone |
| **Voice cloning** | Clonage vocal par IA — synthèse d'une voix imitant une personne réelle |
| **Watering hole** | Compromission d'un site web fréquenté par les cibles |
| **Whaling** | Phishing ciblant les dirigeants et cadres supérieurs |

---

### Annexe B — Cheat sheets

#### B.1 Pretextes classiques par vecteur

| Vecteur | Pretexte | Levier psychologique | Cible type |
|---|---|---|---|
| **Phishing** | Mise à jour portail RH | Obligation, urgence | Tous employés |
| **Phishing** | Invitation conférence | Curiosité, ego | Cadres, ingénieurs |
| **Phishing** | Facture / bon de commande | Routine, urgence | Comptabilité, achats |
| **Phishing** | Partage de document OneD/SharePoint | Normalité, confiance | Utilisateurs M365 |
| **Vishing** | Support IT — incident de sécurité | Autorité, peur, urgence | Tous employés |
| **Vishing** | Prestataire — intervention planifiée | Autorité, normalité | Helpdesk, réception |
| **Vishing** | Direction — demande urgente | Autorité, urgence, pression | DAF, assistants |
| **Vishing** | Recruteur — opportunité de carrière | Ego, cupidité | Ingénieurs, cadres |
| **Physique** | Technicien prestataire IT | Autorité, normalité | Gardien, réception |
| **Physique** | Inspecteur (incendie, qualité) | Autorité | Gardien, employés |
| **Physique** | Employé autre site | Normalité, sympathie | Employés, réception |
| **Élicitation** | Chercheur universitaire intéressé | Flatterie, réciprocité | Ingénieurs R&D |
| **Élicitation** | Consultant secteur / networking | Réciprocité, normalité | Cadres en salon |
| **Smishing** | Notification livraison | Curiosité, urgence | Tous |

#### B.2 Signaux d'alerte par technique

| Technique | Signaux d'alerte |
|---|---|
| **Phishing** | Expéditeur externe avec display name interne, urgence excessive, URL raccourcie ou lookalike, demande de credentials, pièce jointe inattendue |
| **Vishing** | Appel non sollicité demandant des informations sensibles, urgence, impossibilité de rappeler sur un numéro vérifié, name-dropping non vérifiable |
| **BEC** | Demande de virement urgente par email, confidentialité exigée, changement d'IBAN, pression hiérarchique anormale |
| **Intrusion physique** | Personne inconnue sans badge visible, pretexte de prestataire non vérifié, tentative de tailgating, comportement hésitant |
| **Élicitation** | Questions inhabituellement spécifiques, flatterie excessive, réciprocité forcée, transition vers canal privé, profil difficile à vérifier |

#### B.3 Checklist red team SE

- [ ] Lettre de mission signée par représentant habilité
- [ ] Rules of engagement documentées
- [ ] Scope (sites, employés, vecteurs, limites) défini
- [ ] Protocole d'urgence (safe word, contact de référence)
- [ ] Reconnaissance OSINT complétée
- [ ] Reconnaissance physique complétée
- [ ] Pretextes construits (principal + secours)
- [ ] Infrastructure technique déployée
- [ ] OPSEC praticien validé (légendes, compartimentation)
- [ ] Matériel préparé
- [ ] Documentation en temps réel planifiée
- [ ] Rapport final livré avec recommandations P0/P1/P2
- [ ] Debriefing commanditaire réalisé
- [ ] Implants physiques retirés
- [ ] Données de test détruites après livraison

---

### Annexe C — Tableau d'outils de référence

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|---|---|---|---|---|
| **Phishing simulation** | GoPhish | Gratuit (open source) | Simulation de campagnes de phishing | Nécessite infrastructure, pas de support commercial |
| **Phishing simulation** | KnowBe4 | Payant (SaaS) | Simulation + formation + métriques | Coût, dépendance SaaS |
| **Phishing simulation** | Cofense PhishMe | Payant | Simulation + signalement + analyse | Coût |
| **Phishing infrastructure** | Evilginx2 | Gratuit (open source) | Reverse proxy phishing (bypass MFA) | Usage offensif uniquement en cadre autorisé |
| **OSINT** | Maltego | Freemium | Cartographie de relations | Quotas version gratuite, coût version pro |
| **OSINT** | SpiderFoot | Gratuit (open source) | Reconnaissance automatisée | Nécessite configuration, quotas API |
| **OSINT** | theHarvester | Gratuit | Collecte d'emails, sous-domaines | Limité sans API keys |
| **RFID/NFC** | Proxmark3 | ~300 € | Lecture, analyse, clonage de badges | Compétence technique requise |
| **RFID/NFC** | Flipper Zero | ~200 € | Multi-outil portable (RFID, NFC, IR) | Capacités RFID limitées vs Proxmark3 |
| **Implants USB** | Rubber Ducky | ~80 € | Injection de frappes clavier | Détectable par EDR avancés |
| **Implants USB** | Bash Bunny | ~120 € | Multi-payload, émulation périphériques | Détectable par EDR avancés |
| **Implant réseau** | LAN Turtle | ~60 € | Accès réseau distant via Ethernet | Nécessite accès physique, détectable par NAC |
| **Caller ID spoofing** | SpoofCard | Payant | Spoofing numéro appelant | Réglementé, illégal pour fraude |
| **Deepfake vocal** | ElevenLabs | Freemium | Clonage vocal | Limites éthiques, coût à l'échelle |
| **Deepfake détection** | Hive Moderation | Payant | Détection de contenu généré par IA | Faux positifs, taux variable |
| **Vishing** | SET (Social Engineering Toolkit) | Gratuit (open source) | Cadre de social engineering | Nécessite Kali Linux, maintenance inégale |

> **⚠️ Avertissement** : ces outils sont listés à titre de référence pour les praticiens autorisés. Leur utilisation en dehors d'un cadre légal (test autorisé, recherche en sécurité) constitue une infraction pénale.

---

### Annexe D — Templates opérationnels

#### D.1 Structure de lettre de mission red team SE

1. Identification des parties (commanditaire, prestataire, testeurs nommés)
2. Objet de la mission
3. Scope géographique (sites concernés)
4. Scope humain (employés concernés — tous ou profils spécifiques)
5. Vecteurs autorisés (phishing, vishing, smishing, intrusion physique, élicitation)
6. Techniques exclues (chantage, exploitation de vulnérabilités personnelles, etc.)
7. Durée de la mission (dates de début et de fin)
8. Objectifs mesurables
9. Protocole d'urgence (safe word, contact de référence joignable 24/7)
10. Confidentialité des résultats individuels
11. Livrables attendus (rapport, restitution)
12. Conditions financières
13. Signatures (commanditaire habilité, prestataire)

#### D.2 Fiche de signalement d'un incident de social engineering

- Date et heure de l'incident / de la tentative
- Vecteur (email, téléphone, physique, messagerie, autre)
- Description de l'incident (qui, quoi, quand, comment)
- Actions effectuées par l'employé (a cliqué, a transmis des informations, a donné un accès)
- Informations sur l'attaquant (nom affiché, numéro de téléphone, adresse email, description physique)
- Impact potentiel (credentials compromis, information divulguée, accès accordé)
- Actions correctives immédiates prises
- Signalement transmis à (SOC, RSSI, manager)

#### D.3 Checklist de protection en salon professionnel

**Avant le départ :**
- [ ] Brief avec le RSSI : messages autorisés, informations interdites
- [ ] Identification des interlocuteurs à risque (pays, secteurs, profils)
- [ ] Dispositifs numériques sécurisés (téléphone dédié si risque élevé, VPN, chiffrement)
- [ ] Cartes de visite avec informations limitées (pas de numéro personnel)

**Pendant le salon :**
- [ ] Ne jamais laisser un dispositif sans surveillance
- [ ] Ne pas discuter de projets sensibles en public
- [ ] Appliquer les techniques de contre-élicitation si nécessaire (pont, déviation, réponse vague)
- [ ] Noter les contacts inhabituels (nom, entreprise, questions posées)

**Au retour :**
- [ ] Debriefing avec le RSSI
- [ ] Signalement des contacts suspects
- [ ] Vérification des dispositifs numériques (pas de malware, pas de modification)

#### D.4 Grille de formation par profil de risque

| Profil | Menaces prioritaires | Contenu de formation | Fréquence | Format |
|---|---|---|---|---|
| Tous employés | Phishing, tailgating | Sensibilisation générale, signalement | Annuelle | E-learning + simulation |
| DAF / Comptabilité | BEC, fraude fournisseur | Processus de vérification, callback | Semestrielle | Atelier + simulation |
| Helpdesk | Pretexting, MFA manipulation | Vérification d'identité renforcée | Trimestrielle | Exercice vishing |
| Ingénieurs R&D | Élicitation, faux recruteurs | Contre-élicitation, protection en salon | Annuelle | Atelier interactif |
| Réception / Sécurité | Intrusion physique, impersonation | Vérification visiteurs, refus poli | Semestrielle | Exercice pratique |
| Dirigeants | Ciblage personnel, deepfake, spear-phishing | Surface d'exposition, sécurité des communications | Annuelle | Briefing individuel |

---

### Annexe E — Ressources et formation

#### E.1 Certifications

| Certification | Organisme | Focus SE | Coût indicatif | Pertinence |
|---|---|---|---|---|
| SEC567 — Social Engineering for Pentesters | SANS | Élevé (dédié SE) | ~8 000 € (formation + examen) | Référence pour le red team SE |
| GPEN | GIAC | Moyen (SE dans pentest global) | ~3 000 € (examen seul) | Pentest généraliste |
| OSCP | Offensive Security | Faible (SE marginal) | ~1 600 € | Pentest technique |
| Certified Social Engineer | Social-Engineer.org | Élevé (dédié SE) | Variable | Spécialisé mais reconnaissance limitée |
| CEH | EC-Council | Faible | ~1 200 € | Entrée de gamme, couverture SE superficielle |

#### E.2 Conférences

- **DEF CON — Social Engineering Village** : la communauté de référence mondiale pour le SE. Compétitions de SE en direct (SECTF — Social Engineering Capture the Flag), présentations, ateliers.
- **Black Hat** : présentations techniques incluant régulièrement des tracks sur le social engineering.
- **BSides** : conférences communautaires locales avec des tracks SE.
- **Wild West Hackin' Fest** : conférence fondée par SANS avec un focus pratique.

#### E.3 Livres de référence

- **Christopher Hadnagy** — *Social Engineering: The Science of Human Hacking* (2e édition, Wiley, 2018) : le livre de référence pour les praticiens.
- **Christopher Hadnagy** — *Phishing Dark Waters* (Wiley, 2016) : focus sur le phishing offensif et défensif.
- **Kevin Mitnick** — *The Art of Deception* (Wiley, 2002) : classique fondateur, récits d'ingénierie sociale réels.
- **Robert Cialdini** — *Influence: The Psychology of Persuasion* (1984, rééditions multiples) : fondements psychologiques.
- **Robert Cialdini** — *Pre-Suasion* (2016) : le 7e principe (unité) et les techniques de pré-persuasion.
- **Joe Navarro** — *What Every BODY is Saying* (2008) : communication non verbale pour les praticiens.

#### E.4 Communautés

- **Social-Engineer.org** : ressources, podcast, framework, formation (Christopher Hadnagy).
- **SECTF** : Social Engineering Capture the Flag — compétitions DEF CON.
- **r/SocialEngineering** (Reddit) : discussions communautaires (qualité variable).

---

### Annexe F — Cadre juridique

#### F.1 France

| Infraction | Article du Code pénal | Peine maximale | Application au SE |
|---|---|---|---|
| Escroquerie | Art. 313-1 | 5 ans + 375 000 € | Fraude au président, BEC, phishing |
| Usurpation d'identité | Art. 226-4-1 | 1 an + 15 000 € | Impersonation (y compris en ligne) |
| Accès frauduleux à un STAD | Art. 323-1 | 3 ans + 100 000 € | Intrusion informatique post-phishing |
| Atteinte au secret des correspondances | Art. 226-15 | 1 an + 45 000 € | Compromission de boîte mail |
| Fabrication/usage de faux | Art. 441-1 | 3 ans + 45 000 € | Faux documents, faux badges |
| Violation de domicile | Art. 226-4 | 1 an + 15 000 € | Intrusion physique non autorisée |
| Collecte frauduleuse de données personnelles | Art. 226-18 | 5 ans + 300 000 € | Credential harvesting |

**Le red team autorisé** : la lettre de mission signée par un représentant habilité constitue le fondement juridique de l'autorisation. Elle ne crée pas un « droit à commettre des infractions » mais établit le consentement de l'organisation — ce qui élimine l'un des éléments constitutifs de la plupart des infractions (le caractère frauduleux, non autorisé ou sans le consentement de la victime). La lettre de mission doit être juridiquement robuste (rédaction par un avocat recommandée) et couvrir explicitement chaque technique utilisée.

**RGPD.** Les données personnelles collectées pendant un test de SE (identifiants, informations personnelles, photos) sont soumises au RGPD. Le traitement doit avoir une base légale (l'intérêt légitime du responsable de traitement, avec l'analyse d'impact correspondante), les données doivent être minimisées, sécurisées et détruites après la fin de la mission.

#### F.2 Comparatif international

| Aspect | France | Union européenne | États-Unis |
|---|---|---|---|
| Usurpation d'identité en ligne | Délit spécifique (art. 226-4-1) | Variable selon les États membres | Federal : 18 USC § 1028, variable selon les États |
| Enregistrement de conversations | Interdit sans consentement (art. 226-1) | Variable (certains pays autorisent avec une seule partie consentante) | Variable selon les États (one-party vs two-party consent) |
| Red team autorisé | Encadré par lettre de mission | Encadré par le droit national des États membres | Encadré par contrat, jurisprudence CFAA |
| Pretexting dans les enquêtes privées | Limité (pas de faux documents officiels) | Variable | Plus largement toléré (sauf pour obtenir des données financières — GLBA) |

---

### Annexe G — Mapping de la bibliothèque

| Cours de la bibliothèque | Articulation avec le présent cours |
|---|---|
| **Cybersécurité du quotidien** | Prisme victime (reconnaître, se protéger). Le présent cours explique comment les attaques sont construites et testées. |
| **Intelligence économique** | HUMINT d'entreprise légal, protection en salon. Le présent cours approfondit les techniques d'élicitation et la contre-ingérence. |
| **APT** | SE comme vecteur d'accès initial. Le présent cours détaille les techniques elles-mêmes. |
| **OSINT Mastery** | Méthodes de reconnaissance. Le présent cours montre l'application au SE. |
| **CTI** | Attribution et analyse des groupes de menace utilisant le SE. Le présent cours détaille les TTPs. |
| **GRC** | Cadre réglementaire, conformité. Le présent cours traite le cadre juridique spécifique au SE et au red team. |
| **Cryptographie** | Technologies de protection (FIDO2, chiffrement). Le présent cours explique les contournements par SE. |
| **Active Directory / Infrastructure IT** | Surface d'attaque technique. Le présent cours montre comment le SE fournit l'accès initial qui permet l'exploitation technique. |
| **Forensic** | Investigation post-incident. Le présent cours traite la dimension humaine de l'investigation SE. |

---

*Fin du cours — HUMINT et Social Engineering — Élicitation, manipulation et contre-ingénierie sociale*
*Version 2025-2026*
