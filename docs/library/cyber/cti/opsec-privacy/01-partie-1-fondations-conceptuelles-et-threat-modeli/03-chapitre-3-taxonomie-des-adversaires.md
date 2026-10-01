---
title: Chapitre 3 — Taxonomie des adversaires
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 1 — Fondations conceptuelles et threat modeling
  - index.md
---

Un adversaire n’est pas un autre. Confondre les catégories conduit à mal calibrer la défense. Voici les grandes familles, du moins ciblé au plus ciblé, avec leurs capacités, motivations et méthodes typiques.

## 3.1 Surveillance de masse étatique

**Acteurs** : agences de renseignement (NSA, GCHQ, DGSE, BND, FSB, etc.), services de signalisation (SIGINT), partenariats inter-services (Five Eyes, Nine Eyes, Fourteen Eyes).

**Capacités** : collecte passive massive (interception de câbles sous-marins, points d’échange internet), rétention de métadonnées sur des durées variables selon les juridictions, accès légal aux opérateurs (réquisitions, lettres de sécurité nationale), capacité de déchiffrement limitée (la crypto moderne tient — c’est l’OPSEC et les endpoints qui tombent), et exploitation de zero-days lorsque ciblage justifié.

**Modèle** : surveillance *non ciblée par défaut*, ciblage *à la demande* lorsqu’une personne devient pertinente. Tu n’es pas écouté *spécifiquement* aujourd’hui, mais tes métadonnées circulent dans des bases dont la rétention varie.

**Méthodes pertinentes pour toi** : collecte de métadonnées (qui parle à qui, quand), géolocalisation cellulaire, analyse de graphes sociaux, exploitation des relations entre individus.

**Ce contre quoi protéger** : minimisation des métadonnées (messageries adaptées, Tor), compartimentation des identités, prudence sur les graphes de relation.

**Limite réaliste** : si tu es activement ciblé par un service étatique majeur, tu ne pourras pas gagner seul cette guerre. Ton objectif est de *rendre coûteux* le suivi et de minimiser ce qu’ils ont déjà.

## 3.2 Capitalisme de surveillance

**Acteurs** : data brokers (Acxiom, LexisNexis, Spokeo, Intelius, Whitepages), ad-tech (Google, Meta, The Trade Desk, Criteo), courtiers de localisation (X-Mode, Cuebiq, Veraset — souvent revendus à des agences gouvernementales).

Une évolution préoccupante de ce modèle est l’ADINT (Advertising Intelligence) : l’exploitation des données et mécanismes publicitaires à des fins de renseignement. Des données initialement collectées pour le ciblage marketing — identifiants publicitaires, localisation, applications utilisées, signaux comportementaux — peuvent être revendues, agrégées ou exploitées pour suivre des individus, cartographier des groupes ou préparer des actions ciblées. L’ADINT illustre la porosité entre publicité, courtage de données, surveillance privée et renseignement étatique.

**Capacités** : agrégation massive de données issues d’applications mobiles, de cookies, de programmes de fidélité, de fuites, de registres publics, de réseaux sociaux. Construction de profils détaillés vendus à des fins publicitaires, mais aussi à des fins de scoring (crédit, assurance), de vérification (background check), voire à des forces de l’ordre via achat plutôt que mandat.

**Modèle** : profit par accumulation. Tu n’es pas la cible, tu es la marchandise.

**Méthodes** : SDK publicitaires dans les apps, cookies tiers (en déclin), fingerprinting (en croissance, cf. Ch 23), achat de bases de données fuitées, agrégation cross-device.

**Ce contre quoi protéger** : navigateurs anti-fingerprint (Ch 24), désinscription data brokers (Ch 6), minimisation des permissions mobiles (Ch 15), email aliasing (Ch 27), paiements compartimentés (Ch 32).

**Spécificité** : c’est l’adversaire le plus probable de tout lecteur. Et pourtant le moins fantasmé. La discipline anti-tracking quotidienne est le bénéfice immédiat de ce cours pour la grande majorité des gens.

## 3.3 Plateformes elles-mêmes : Google, Meta, Apple, Microsoft, TikTok

**Acteurs** : les géants du numérique. Statut hybride entre fournisseurs et adversaires : tu leur confies des données pour utiliser leurs services, et eux les exploitent.

**Capacités** : accès intégral à ce que tu leur confies (emails Gmail, photos Google Photos, contacts iCloud, messages WhatsApp côté métadonnées, etc.). Capacité de réquisition judiciaire à laquelle ils répondent selon les juridictions et les procédures. Capacité d’analyse comportementale fine (Apple Intelligence, Gemini sur Android, etc.).

**Modèle** : variable selon la plateforme. Apple revendique un modèle moins intrusif (et Advanced Data Protection chiffre certaines données de bout en bout, cf. Ch 14 et 30). Google et Meta vivent du ciblage publicitaire. Microsoft est entre les deux. TikTok pose des questions spécifiques liées à sa juridiction.

**Méthodes pertinentes** : ce que tu leur donnes volontairement (essentiellement tout, si tu utilises leurs services sans précaution), enrichi par l’IA générative côté Microsoft Copilot et Apple Intelligence (Ch 34).

**Ce contre quoi protéger** : chiffrement côté client par-dessus le cloud (Ch 30), email auto-hébergé ou chez fournisseur E2EE (Ch 27), ADP iCloud activée si Apple, minimisation des comptes Google rattachés au principal.

## 3.4 Censure et restriction d’accès

**Acteurs** : États autoritaires (Chine, Iran, Russie, Émirats, Vietnam, etc.) mais aussi démocratiques sur certains contenus (filtrage DNS au RU et en France pour terrorisme et pédocriminalité, etc.), FAI qui appliquent les ordres, plateformes qui appliquent les politiques.

**Capacités** : blocage DNS, blocage IP, deep packet inspection (DPI), perturbation de protocoles (Tor, VPN), obligation d’enregistrement, sanctions pénales pour les contournements.

**Ce contre quoi protéger** : VPN (Ch 20), Tor avec bridges (Ch 21), DNS chiffré (Ch 19), résolveurs alternatifs.

**Cadre légal** : varie radicalement selon les juridictions. En Iran, l’usage de VPN est techniquement illégal mais massif. En Chine, le contournement du Great Firewall expose à des sanctions. En France, le RGPD protège l’usage privé d’outils légitimes.

## 3.5 Attaques ciblées : APT étatiques, mercenaires

**Acteurs étatiques** : APT chinois (APT10, APT41), russes (APT28, APT29, Turla), nord-coréens (Lazarus), iraniens (APT34, Charming Kitten), occidentaux aussi mais moins publiquement documentés. Les APT visent typiquement entreprises, gouvernements, ONG sensibles, dissidents.

**Acteurs mercenaires** : NSO Group (Pegasus), Intellexa (Predator), Paragon Solutions (Graphite), QuaDream, Candiru, Hacking Team (historique). Ces sociétés vendent à des États (parfois autoritaires) du spyware mobile de pointe.

**Capacités** : zero-days iOS/Android (zero-click parfois), exploits chaînés, infrastructure C2 résiliente, capacité de pivot et d’exfiltration.

**Cibles documentées par Citizen Lab et Amnesty Security Lab** : journalistes d’investigation, activistes des droits humains, avocats de la défense, leaders d’opposition, proches de cibles. Cas confirmés dans des dizaines de pays.

**Méthodes** : zero-click iMessage/WhatsApp (cas Pegasus FORCEDENTRY, cas Paragon Graphite 2024-2025), liens piégés ciblés, installation physique en transit, infection via Wi-Fi infrastructure compromise.

**Ce contre quoi protéger** : Lockdown Mode iOS (Ch 15), GrapheneOS, redémarrage régulier (zero-clicks souvent non persistants), MVT et iVerify (Ch 33), notifications Apple/WhatsApp/Google.

**Coût** : déploiement d’un spyware mercenaire coûte entre 10k$ et plusieurs millions selon la cible. *Tu n’es pas ciblé par défaut.* Si tu l’es, tu le sauras probablement par les notifications des plateformes.

## 3.6 Criminalité opportuniste

**Acteurs** : groupes de cybercriminalité organisée, opérateurs ransomware, vendeurs de credentials, brokers d’accès, phishers de masse.

**Capacités** : kits de phishing prêts à l’emploi, base de credentials achetée sur forums, malware as a service, infrastructure botnet.

**Modèle** : volume. Tu n’es pas ciblé, tu es statistique. Si tu cliques sur le bon lien le bon jour, tu paies.

**Ce contre quoi protéger** : MFA fort, gestionnaire de mots de passe (Ch 29), méfiance des liens, mises à jour à jour, sauvegardes 3-2-1 (Ch 30).

## 3.7 Adversaires de proximité

**Acteurs** : ex-partenaire (cas particulièrement fréquent et dangereux, notamment dans les contextes de violences conjugales), harceleur (stalker), famille intrusive ou hostile, employeur intrusif, journaliste hostile, voisin curieux.

**Capacités** : faibles techniquement, mais **élevées en connaissance préalable** — ils savent ton anniversaire, le nom de ton chien (souvent ton mot de passe), tes habitudes, tes lieux de passage. Ils ont parfois eu accès physique à tes appareils (voir spyware *stalkerware* commercial : mSpy, FlexiSpy, etc.).

**Modèle** : motivation très forte, capacité technique faible mais compensée par la proximité.

**Méthodes** : devinette de mot de passe, accès physique, stalkerware installé pendant la relation, observation OSINT classique, exploitation des proches.

**Ce contre quoi protéger** : changement complet de credentials après rupture, audit des appareils (cf. annexe 8 ressources Coalition Against Stalkerware), MFA matériel, séparation des comptes Apple/Google, sortie des comptes partagés, prudence Find My et localisation.

> 🟧 **À noter** : ce threat model est sous-traité dans la plupart des cours de cybersécurité, qui se focalisent sur l’étatique. Or pour une fraction significative de la population, l’adversaire principal est dans son entourage. Le **Cas D** en fin de cours traite spécifiquement ce scénario.

## 3.8 Adversaires accidentels : l’entourage qui dénonce sans le savoir

Catégorie particulière. Ton frère qui te tague sur une photo Instagram à un anniversaire de famille révèle ta localisation à un harceleur. Ton collègue qui répond à un appel de prétexte donne ton emploi du temps à un ingénieur social. Tes parents qui rendent publique ta date de naissance et le nom de jeune fille de ta mère mettent la sécurité de tes questions de récupération en danger.

L’entourage n’est pas hostile mais constitue un vecteur d’exposition que tu ne contrôles pas. Une partie de la défense consiste à *éduquer* discrètement les personnes proches (Ch 35).

## 3.9 HVT (High Value Targets)

qui est vraiment ciblé, qui se croit ciblé

**HVT réels** : journalistes d’investigation publiant sur des dossiers critiques, leaders d’opposition dans des régimes autoritaires, lanceurs d’alerte avant publication, avocats de la défense sur des dossiers sensibles, militants sur des sujets visés (climat radical, droits humains dans certains pays). Catégories documentées par Citizen Lab et Amnesty Security Lab comme cibles répétées de spyware mercenaire.

**HVT autoperçus mais peu probables** : la plupart des « privacy enthusiasts », des professionnels cyber non exposés professionnellement, des particuliers durcis. Ils auraient *tout intérêt* à concentrer leurs efforts sur les menaces réelles (capitalisme de surveillance, criminalité opportuniste, doxxing), plus probables et plus traitables.

**Test honnête de HVT-ness** : as-tu publiquement, et dans le dernier exercice de ton activité, produit une information qui mette en danger un acteur capable et motivé ? Si non, tu n’es probablement pas HVT. Si oui, tu l’es peut-être — et il est temps de durcir sérieusement.

> 🟩 **À retenir du chapitre 3**
> 
> - Le capitalisme de surveillance est l’adversaire le plus probable de tout le monde.
> - Les adversaires de proximité sont sous-évalués et particulièrement dangereux car ils ont de la connaissance préalable.
> - Les attaques mercenaires (Pegasus & co) sont réelles mais ciblent un nombre restreint de profils ; ne pas dimensionner sa défense sur ce seul axe.
> - Définir honnêtement son profil de HVT-ness conditionne tout le reste.

-----
