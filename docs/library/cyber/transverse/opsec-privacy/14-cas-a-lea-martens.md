---
title: Cas A — Léa Martens
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - index.md
---

journaliste d’investigation, enquête transeuropéenne

**Clôture du fil rouge.** Mobilise les Parties 1-7. Renvois explicites entre chapitres.

## A.1 Contexte

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

## A.2 Architecture déployée

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

## A.3 Stack source-journaliste avec Karim

Karim, fonctionnaire AAI française, alerte interne. Premier contact via une rédaction tierce (Mediapart, qui sert d’intermédiaire neutre). Mediapart envoie un message à Léa : « Une personne souhaite te joindre confidentiellement, voici son indicateur de référence ».

Léa et Karim établissent leur canal :

- **Premier échange** : Léa publie un message dans un thread public sur son compte X pro contenant un détail spécifique qu’elle a convenu avec Mediapart. Karim, en voyant ce détail, reçoit la confirmation que Léa est bien la personne qu’il cherche.
- **Initialisation SimpleX** : Karim installe SimpleX sur un téléphone d’occasion qu’il a acheté cash dans un magasin choisi loin de ses lieux habituels (cf. Ch 9, Ch 15). Il crée un compte SimpleX sans numéro de téléphone.
- **Échange du lien** : Léa et Karim échangent leur lien de connexion SimpleX via le canal Mediapart, qui ne voit pas le contenu (la rédaction relaie un blob chiffré PGP fourni par Léa, déchiffré par Karim avec sa clé qu’il a générée pour l’occasion sur Tails).
- **Vérification d’identité** : premier appel SimpleX vocal court. Léa et Karim ne se connaissent pas physiquement. Ils ont convenu d’un proverbe à prononcer pour authentifier ; le vrai test est dans la cohérence de leur récit et le savoir détenu par Karim (informations vérifiables auprès de Léa).
- **Régime opérationnel** : disappearing messages 24 h pour toute la conversation. Vérification mutuelle hebdomadaire (Léa demande à Karim un détail convenu à l’avance qui change chaque semaine). Transferts de documents via OnionShare exclusivement, pas SimpleX (les fichiers SimpleX restent sur les serveurs SimpleX un temps).

## A.4 Workflow de réception et traitement des documents

À chaque paquet de documents reçu de Karim (3-7 paquets sur 14 mois) :

1. Réception du lien OnionShare via SimpleX.
1. Léa boot Tails sur sa clé USB enquête principale, depuis le MacBook Air dédié.
1. Téléchargement via Tor Browser à l’intérieur de Tails. Vérification du hash SHA-256 fourni hors-bande par Karim (sur SimpleX, message court non lié au transfert).
1. Passage des PDF par Dangerzone (dans Tails, ou re-importé dans une dispVM Qubes sur le Mac quand Léa migre vers Qubes au mois 8).
1. Audit métadonnées : ExifTool sur chaque fichier. À deux reprises sur les 14 mois, Léa trouve des métadonnées qui auraient révélé l’auteur : un PDF avec « Author = [nom de Karim au format administratif officiel] » dans le XMP, et un DOCX avec un commentaire interne contenant un nom de personne mentionnée dans le bureau de Karim. À chaque fois, nettoyage avant tout transfert ultérieur.
1. Archivage chiffré : import dans conteneur VeraCrypt sur disque externe, déchiffré uniquement lors de sessions de travail sur l’enquête. Le mot de passe du conteneur est un Diceware 8-mots, dérivé via Argon2id (memory ≥ 1 GiB, t=4, p=4).
1. Documentation : log interne (dans le conteneur) — date, source, hash, environnement utilisé, notes contextuelles. Pas pour partage, pour traçabilité d’enquête et audit interne du consortium.

## A.5 Incident — la tentative de spear phishing à T+5 mois

À cinq mois d’enquête, Léa reçoit sur son email pro un message d’apparence légitime, qui semble venir d’un correspondant d’un des médias partenaires du consortium. L’objet : « Suite à notre échange à la conférence Bruxelles — documents complémentaires ». Pièce jointe : un PDF.

Léa, par discipline, ne clique pas en client mail (la preview est désactivée par défaut sur sa stack). Elle examine les en-têtes : DKIM signature présente mais sur un domaine très proche du domaine légitime (`partner-media-org.com` au lieu de `partnermediaorg.com`). Récente création de domaine (Whois indique enregistrement il y a 9 jours). L’expéditeur n’est pas dans son carnet d’adresses vérifié.

Elle ne télécharge pas le PDF en environnement de quotidien. Elle bascule vers son MacBook Air enquête, isole le fichier dans un dispVM (Léa est passée à Qubes 2 mois plus tôt sur ce laptop), l’ouvre dans la dispVM. Le PDF, à l’œil nu, contient quelques lignes neutres. Mais l’analyse via ExifTool révèle un objet JavaScript embarqué. Léa n’exécute pas ; soumission du PDF anonymisé à un confrère analyste malware (via OnionShare). Diagnostic : tentative d’exploit, probablement non-zero-day, ciblant une ancienne version d’Acrobat Reader. La pièce jointe contient une chaîne d’infection plausible.

Léa documente. Préviens son consortium. Vérification : aucun autre membre du consortium n’a reçu un message similaire ce mois-là — ciblage individuel donc, pas spray-and-pray. C’est un signal important : *quelqu’un sait que je travaille sur l’enquête*. Threat model révisé. Bascule vers Lockdown Mode aussi sur l’iPhone perso (qu’elle n’utilisait pas pour l’enquête, mais qui contient son carnet d’adresses personnel). Audit physique des appareils — rien d’anormal.

À ce stade, l’enquête continue mais Léa adopte une discipline encore renforcée : SimpleX uniquement pour Karim (plus aucun mail), tests MVT mensuels sur le Pixel (rien détecté), reboot deux fois par jour du Pixel, et iVerify installé sur l’iPhone perso (rien détecté).

## A.6 Tentative de deepfake à T+9 mois

Cf. fil rouge Ch 34. Trois mois après l’incident phishing, Léa reçoit un appel vidéo SimpleX. Voix et image de Karim, ton paniqué : « Léa, j’ai besoin que tu rendes les documents, ils savent, c’est dangereux pour ma famille. » Léa applique le protocole pré-convenu : un proverbe convenu avec Karim au début de la relation, qu’elle lui demande de redire. Silence. Raccrochage côté appelant.

Léa contacte Karim sur SimpleX par texte. Karim répond : « Je n’ai pas appelé. Tout va bien. » Confirmation : deepfake. Léa et Karim audit complet de la stack — quelqu’un a obtenu des échantillons de la voix de Karim (possiblement via interception passive d’un appel téléphonique non sécurisé qu’il a passé à un proche, ou via achat de bases). L’image vidéo provient probablement de photos publiques de Karim (LinkedIn, photo officielle de son service).

Conséquences :

- Vérification que SimpleX lui-même n’est pas compromis : il ne l’est pas, l’attaquant n’a pas réussi à intercepter le canal, il a tenté un *appel sortant frauduleux* en se faisant passer pour Karim depuis un autre compte SimpleX en utilisant le lien public connu par certains tiers. Ce vecteur a été corrigé par SimpleX dans les versions ultérieures.
- Karim renforce sa discipline : aucun appel téléphonique avec proches sur sujets sensibles, audit téléphonique de son entourage qui pourrait être leveraged.
- Léa rappelle dans le protocole : *toute* communication d’urgence inattendue exige double vérification par canal séparé.

## A.7 Publication coordonnée à T+12 mois

Préparation des 3 derniers mois :

- Caviardage destructif des documents publiés. Vérification croisée par deux confrères du consortium.
- Identification des éléments qui pourraient permettre par recoupement de remonter à Karim. Décision éditoriale : certaines informations sont retirées de la publication parce que trop révélatrices de la source — quitte à affaiblir certaines preuves. Le consortium adopte cette discipline collectivement.
- Préparation de Karim : mise en relation avec l’association *Maison des Lanceurs d’Alerte* en France, premier RDV avec un avocat spécialisé. Karim sait que son identité ne sera pas révélée publiquement par les médias, mais l’enquête interne dans son administration suite à la publication est probable.
- Soutien juridique pour Léa : convention écrite avec un avocat spécialisé en droit des médias, accessible 24/7 dans les 72h post-publication.

Publication simultanée sur les 12 médias partenaires à 06:00 CET. Couverture massive. Réaction politique : démissions, ouverture d’enquêtes parlementaires.

## A.8 Post-publication : ce qui s’est passé

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

## A.9 Renvois croisés mobilisés

- **Threat modeling** : Ch 2 (cadre EFF), Ch 3 (taxonomie adversaires).
- **Réduction empreinte** : Ch 4 (cartographie), Ch 5-7 (OSINT défensif, data brokers, doxxing), Ch 8 (réseaux sociaux).
- **Compartimentation** : Ch 9 + Capstone 1.
- **Matériel et systèmes** : Ch 10-15 (Pixel cash, FDE, GrapheneOS, MacBook Air dédié).
- **Sessions sensibles** : Ch 16-18 + Capstone 2 (Tails, Qubes après bascule).
- **Réseau et navigation** : Ch 19-24 (Mullvad, Tor Browser, fingerprinting, multi-navigateurs).
- **Communications** : Ch 25-32 + Capstone 3 (SimpleX avec Karim, OnionShare pour transferts, PGP pour pivots, métadonnées rigoureusement traitées).
- **OPSEC humaine et juridique** : Ch 33-38 (phishing détecté, deepfake déjoué, Sapin II pour Karim, voyage, maintenance disciplinée).

-----
