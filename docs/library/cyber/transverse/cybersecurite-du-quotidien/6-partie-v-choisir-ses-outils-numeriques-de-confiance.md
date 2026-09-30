---
title: PARTIE V — CHOISIR SES OUTILS NUMÉRIQUES DE CONFIANCE
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
chapter: 6
chapters: 9
---

*Visio • Messageries • Cloud • IA • PDF • Transferts • Coffres numériques*

*Une fois qu'on a compris les risques (Parties I-IV), une question reste : « j'utilise quoi à la place ? ». Cette partie propose une méthode pour choisir le bon outil selon le niveau de sensibilité, le cadre (perso, pro, agent public), et les obligations de l'organisation. Aucun outil n'est « sûr » dans l'absolu ; le bon outil est celui qui correspond à ce que vous y mettez.*

---

<a id="chapitre-22"></a>
## Chapitre 22 — Classer la sensibilité avant de choisir l'outil

*Avant de demander « quel outil utiliser ? », demander « pour quoi faire ? ». Le bon réflexe n'est pas le réflexe technique, c'est le réflexe de classification.*

### 22.1 Quatre niveaux de sensibilité

| Niveau | Usage | Exemples | Exigence sur l'outil |
|--------|-------|----------|---------------------|
| **1 — Banal** | Communication quotidienne, organisation, loisir | Appel famille, photos vacances, organisation d'un repas, partage d'un article | Outil grand public acceptable, configuré sobrement |
| **2 — Personnel sensible** | Données qui engagent la personne | RIB, CNI, dossier de location, données de santé, contrats personnels | Canal chiffré, partage restreint, durée limitée |
| **3 — Professionnel** | Données de l'organisation | Document client, RH, projet interne, code source, fichier comptable | Outil **validé par l'organisation** uniquement |
| **4 — Institutionnel / régulé** | Secteur public, données très sensibles | Données administratives sensibles, secret professionnel, données de santé soignant-patient, gestion de crise | Outil institutionnel, souverain, qualifié ou explicitement autorisé |

**Le principe** : on ne choisit pas un outil parce qu'il est pratique, on le choisit parce qu'il est adapté au niveau de sensibilité de ce qu'on y met.

### 22.2 Le test des 4 questions

Avant de déposer un fichier ou de lancer une conversation sur un outil donné, se poser :

1. **Le contenu** : que va-t-il y avoir dedans (données personnelles, professionnelles, médicales, financières, confidentielles) ?
2. **La destination** : où le contenu est-il stocké, qui peut y accéder, sous quelle juridiction ?
3. **La durée** : combien de temps le contenu y reste-t-il, est-ce que je peux le supprimer effectivement ?
4. **Le cadre** : si je suis salarié(e) ou agent(e) public, mon organisation autorise-t-elle cet outil pour ce type de données ?

Si la réponse à l'une de ces questions est floue → ne pas utiliser cet outil pour ce contenu. Trouver une alternative locale, une alternative validée, ou demander à l'IT/DSI.

### 22.3 Le réflexe « contournement = signal »

Quand un utilisateur contourne l'outil officiel (Gmail perso pour un fichier pro, IA grand public pour résumer un rapport interne, WeTransfer pour un livrable client), ce n'est presque jamais par mauvaise intention. C'est presque toujours parce que l'outil officiel est trop lent, mal expliqué, ou inexistant. Le contournement individuel est le **symptôme d'un outil manquant** dans l'organisation. Le bon réflexe individuel n'est pas le contournement durable — c'est l'usage temporaire raisonné (anonymisation, contenu non sensible) **et** le signalement du besoin à l'IT/DSI pour qu'une vraie alternative soit fournie.

---

<a id="chapitre-23"></a>
## Chapitre 23 — Visioconférence : choisir l'outil selon le contexte

### 23.1 Le bon outil dépend du cadre

Pour une réunion personnelle peu sensible, un outil grand public (Zoom, Google Meet, Teams gratuit, FaceTime, Discord) est acceptable. Pour une réunion professionnelle, c'est l'outil **validé par l'organisation** qui s'impose, indépendamment des préférences personnelles. Pour une réunion d'agent public ou impliquant des données institutionnelles sensibles, des solutions souveraines existent et doivent être privilégiées quand elles sont disponibles.

| Situation | Outil par défaut | Réflexe |
|-----------|-----------------|---------|
| Visio familiale, apéro, appel d'amitié | Outil grand public, lien unique | Pas de lien permanent public, pas d'enregistrement inutile |
| Réunion professionnelle | Outil de l'organisation (Teams, Meet entreprise, Webex selon contrat) | Pas d'outil perso « lancé à l'arrache » |
| Réunion entre administrations / agents publics | **Visio de l'État** / Webconférence de l'État (DINUM, La Suite numérique) si disponible | Privilégier l'outil institutionnel souverain |
| Réunion **très sensible** (sujet stratégique, contexte régulé, personnalités exposées) | **Tixeo** (visio française certifiée CSPN par l'ANSSI ; certaines offres comme TixeoPrivateCloud peuvent s'appuyer sur un hébergement qualifié SecNumCloud) ou solution équivalente validée par l'organisation | Outil chiffré de bout en bout, hébergement souverain |
| Réunion sensible (médecine, juridique, données régulées) | Outil dédié au secteur (Doctolib pour téléconsultation, outil agréé HDS pour santé) | Ne pas improviser avec un outil grand public |
| Webinaire / formation publique | Webinaire de l'organisation, outil professionnel adapté | Gérer les droits intervenants/public, lien d'inscription contrôlé |

**Note souveraineté** : la DINUM (Direction interministérielle du numérique) propose dans **La Suite numérique** des outils destinés aux agents de l'État, dont **Visio** (visioconférence souveraine hébergée en France) et la **Webconférence de l'État**. Pour les usages les plus sensibles, **Tixeo** est une solution française de visioconférence chiffrée de bout en bout. Plus précisément : la solution Tixeo est **certifiée CSPN par l'ANSSI** sur une version et un périmètre précis ; et certaines offres cloud, notamment **TixeoPrivateCloud**, peuvent s'appuyer sur un hébergement **qualifié SecNumCloud**. Ce sont deux choses distinctes — la certification du produit d'un côté, la qualification de l'hébergement de l'autre. Pour les agents publics, ces outils sont à privilégier pour les usages institutionnels quand l'organisation les a déployés.

> **Note sur les certifications ANSSI** : la **CSPN** (Certification de Sécurité de Premier Niveau) et la **qualification** (Élémentaire, Standard, Renforcée) sont des évaluations sérieuses portant sur **une version, une configuration et un périmètre précis** d'un produit. Une certification n'est pas une garantie absolue, et elle ne dispense pas de respecter la politique de l'organisation. Citer un outil comme « certifié ANSSI » est un raccourci utile mais qui doit toujours s'accompagner de cette nuance.

### 23.2 Réglages quel que soit l'outil

- **Salle d'attente activée** pour les réunions externes (filtrer qui entre).
- **Lien unique par réunion**, pas de « lien permanent » réutilisé.
- **Mot de passe de réunion** activé pour les sujets sensibles.
- **Vérifier la liste des participants** avant de partager un contenu sensible — un nom inconnu n'est pas normal.
- **Partage d'écran** : fermer les onglets sensibles, les messageries personnelles, désactiver les notifications avant de partager (une notification WhatsApp privée pendant un partage d'écran professionnel est une fuite).
- **Enregistrement et transcription IA** : savoir qui enregistre, ce qui est transcrit, où c'est stocké. Beaucoup d'outils activent l'enregistrement et la transcription IA par défaut. Pour les réunions sensibles, désactiver explicitement et le rappeler en début de réunion.
- **Fond flou ou virtuel** quand l'arrière-plan révèle des informations (documents au mur, écrans visibles, autres personnes).

---

<a id="chapitre-24"></a>
## Chapitre 24 — Messageries : choisir le bon canal

*Toutes les messageries ne se valent pas. Le critère n'est pas seulement le chiffrement, c'est aussi le contexte d'usage et le destinataire.*

| Canal | Bon usage | Limites / vigilances |
|-------|-----------|---------------------|
| **SMS** | Notifications, messages banals | Non chiffré, expéditeur usurpable (spoofing), inadapté au sensible |
| **iMessage** | Conversations courantes entre Apple, chiffrement de bout en bout entre iPhone | Bascule en SMS non chiffré quand le destinataire n'est pas Apple |
| **WhatsApp** | Échanges quotidiens chiffrés de bout en bout, groupes familiaux/amicaux | Métadonnées collectées par Meta (qui parle à qui, quand, durée) ; sauvegardes cloud parfois non chiffrées par défaut |
| **Signal** | Conversations privées sensibles, référence grand public | Repose sur le numéro de téléphone (en évolution avec les noms d'utilisateur) ; dépend du bon usage et de la sécurité du téléphone des deux côtés |
| **Olvid** | Échanges **très sensibles**, personnalités exposées, contexte souverain, réduction forte des métadonnées | Solution française ; chiffre messages, pièces jointes et appels ; **n'utilise pas le numéro de téléphone** comme identifiant principal ; cherche aussi à protéger les métadonnées (« qui parle à qui ») ; certifications CSPN ANSSI sur des versions et périmètres précis |
| **Telegram** | Communautés, canaux publics, groupes thématiques, veille | Conversations normales **non chiffrées de bout en bout** par défaut — seuls les « chats secrets » 1-à-1 le sont ; pas adapté aux conversations confidentielles par défaut |
| **Tchap** | Messagerie souveraine du secteur public français, chiffrée de bout en bout, gérée par l'administration | À privilégier pour les agents publics dans le cadre d'échanges entre agents quand l'organisation l'a déployée |
| **Email** | Documents formels, communications administratives | Non chiffré par défaut, pièces jointes potentiellement risquées, métadonnées exposées |

**La règle** : le bon canal n'est pas seulement celui qui chiffre, c'est celui qui correspond au **contexte**, au **destinataire** et à la **donnée échangée**. Un RIB ou une photo de pièce d'identité ne s'envoient pas par SMS, par email non chiffré, ou par Telegram en mode normal. Si c'est nécessaire, utiliser un canal chiffré (Signal, Olvid) ou un partage de fichier sécurisé (cf. Ch.25).

**Recommandations selon le contexte** :
- *Conversations privées sensibles d'un particulier* : **Signal** ou **Olvid**.
- *Échanges très sensibles, ou nécessitant une réduction forte des métadonnées* (personnalités exposées, journalisme, sources, contextes à risque) : **Olvid**.
- *Échanges professionnels entre agents publics* : **Tchap** quand déployé par l'administration.
- *Échanges pro entreprise* : la messagerie de l'organisation (Teams, Slack, ou autre selon contrat) avec les conventions internes.

**Note sur Olvid** : Olvid est une solution française de messagerie sécurisée qui ne s'appuie pas sur le numéro de téléphone comme identifiant principal — un point différenciant par rapport à Signal et WhatsApp. La protection vise non seulement le contenu mais aussi les métadonnées (qui parle à qui, quand). Olvid a obtenu des certifications **CSPN** auprès de l'ANSSI ; comme pour toute certification, **elle porte sur une version, une configuration et un périmètre précis** — c'est un signal de sérieux, pas une garantie absolue ni une recommandation universelle.

**Côté agent public** : Tchap est conçu pour les échanges du secteur public avec chiffrement de bout en bout, et permet d'inviter des personnes externes sous certaines conditions. Pour des échanges plus sensibles ou hors du périmètre Tchap, Olvid peut être pertinent quand l'organisation l'a validé.

---

<a id="chapitre-25"></a>
## Chapitre 25 — Transfert de fichiers : éviter les liens publics permanents

*Un lien « toute personne ayant le lien » n'est pas un partage privé. C'est une porte ouverte dont la clé peut être copiée à l'infini.*

### 25.1 Les pièges du transfert facile

WeTransfer, le lien Google Drive « toute personne ayant le lien », l'OneDrive partagé sans expiration, le lien Dropbox copié dans un email — ce sont les outils les plus pratiques et aussi les moins maîtrisés. Le lien fuite (forwardé, intercepté, indexé par un moteur de recherche public, capté dans un journal de proxy), et le contenu reste accessible à toute personne qui a la chaîne.

| Besoin | Mauvais réflexe | Meilleur réflexe |
|--------|-----------------|------------------|
| Envoyer un gros fichier banal à un proche | Lien public sans expiration | Lien temporaire (7-15 jours), mot de passe si possible |
| Envoyer CNI / RIB / document sensible | Pièce jointe email non chiffrée, lien public | Lien nominatif (le destinataire s'authentifie), mot de passe transmis par un autre canal, durée limitée |
| Envoyer un fichier professionnel | Drive perso, WeTransfer perso | Outil de partage de l'entreprise (avec DLP, audit, contrôle d'accès) |
| Agent public, fichier volumineux | Outil externe non validé | **France Transfert** (solution de l'administration) si disponible |

**Note souveraineté** : pour les fichiers volumineux (jusqu'à 20 Go), **France Transfert** permet aux agents de l'État d'envoyer des fichiers, y compris à des destinataires extérieurs, avec mot de passe optionnel et durée de conservation paramétrable. C'est l'alternative institutionnelle aux outils grand public type WeTransfer pour les contextes publics.

**Mais attention à ne pas confondre canal et protection du contenu** : France Transfert est conçu comme un **canal de transport** souverain pour des fichiers volumineux non sensibles. Il ne se substitue pas au chiffrement du contenu lui-même. Pour un fichier sensible, France Transfert seul n'est pas suffisant — le bon réflexe est de **chiffrer d'abord le fichier (par exemple avec Zed!)**, puis de l'envoyer via France Transfert (cf. Ch.25.3). Le canal transporte, le conteneur protège.

### 25.2 Les bons réflexes du partage

- **Lien nominatif** plutôt que « toute personne ayant le lien » (le destinataire doit s'authentifier).
- **Durée d'expiration** courte (7 jours par défaut, prolongeable au besoin).
- **Mot de passe** sur le lien, transmis via un canal différent (le lien par email, le mot de passe par SMS ou en personne).
- **Révocation** possible — connaître la procédure pour désactiver le lien si nécessaire.
- **Ne pas conserver d'historique de partages oubliés** — réviser semestriellement les partages actifs sur le cloud.

### 25.3 Chiffrer avant d'envoyer : Zed!, conteneurs chiffrés et alternatives

*Le canal transporte. Le conteneur protège.* Quand le contenu est sensible et que le canal de transport ne donne pas suffisamment de garanties (ou simplement parce qu'on veut une couche supplémentaire indépendante du canal), la bonne pratique est de **chiffrer le fichier avant l'envoi** dans un conteneur dédié. Le destinataire ouvre le conteneur avec une clé, et le canal — email, France Transfert, clé USB, dépôt cloud — n'a jamais accès au contenu en clair.

**Zed!** est une solution française développée par PRIM'X qui permet de créer des **conteneurs chiffrés `.zed`**. Concrètement, on glisse des fichiers ou des dossiers dans un conteneur, on définit les destinataires (par certificat ou par mot de passe partagé), et on envoie le conteneur via le canal de son choix. Zed! a fait l'objet de **certifications de l'ANSSI** sur des versions et configurations précises ; cette information vaut **selon la version, la configuration et le périmètre évalué** — c'est un gage de sérieux, pas une garantie absolue, et l'usage doit respecter la politique de l'organisation.

Une nuance importante : **Zed! est une « valise chiffrée de transport », pas un coffre-fort numérique probant d'archivage**. Sa vocation est de protéger un envoi (du dépôt jusqu'à l'ouverture par le destinataire), pas de remplacer un coffre-fort numérique au sens du Code civil avec valeur probante d'archivage long terme.

Le **couple Zed! + France Transfert** est particulièrement pertinent dans le secteur public ou pour des échanges sensibles entre organisations : Zed! chiffre le contenu, France Transfert assure le transport. Si l'un fuite, l'autre tient.

| Besoin | Solution |
|--------|----------|
| Envoyer un fichier sensible à un destinataire identifié, contexte pro/institutionnel | **Zed!** (conteneur chiffré) — éventuellement transporté via France Transfert, email, ou clé USB |
| Coffre chiffré synchronisé dans un cloud personnel (iCloud, Google Drive…) | **Cryptomator** (open source, gratuit) |
| Conteneur ou volume chiffré local plus avancé | **VeraCrypt** (open source, plus technique) |
| Protection ponctuelle simple d'un fichier | Archive **ZIP avec mot de passe AES-256** (compatible partout, mais moins professionnel) |

**Note méthodologique** : transmettre la clé/le mot de passe par un canal différent du conteneur. Si vous envoyez le `.zed` par email, le mot de passe se transmet par SMS, par téléphone, ou en personne. Le double canal divise drastiquement le risque.

---

<a id="chapitre-26"></a>
## Chapitre 26 — Cloud, documents collaboratifs et stockage

*Le cloud n'est pas un disque dur magique. C'est un espace partagé, synchronisé, accessible à distance, qui doit être configuré.*

### 26.1 Quel cloud pour quel usage

| Type de cloud | Usage adapté | Vigilances |
|---------------|--------------|------------|
| **Cloud personnel** (iCloud, Google Drive, OneDrive perso, Dropbox) | Photos personnelles, documents personnels, organisation du foyer | MFA activé, partages révisés, pas de documents d'identité en clair |
| **Cloud familial** (Apple Family, Google Family) | Achats partagés, photos familiales, calendriers | Compartimenter ce qui doit l'être, retirer les ex (cf. Ch.38) |
| **Cloud professionnel** (Microsoft 365 entreprise, Google Workspace, suites métier) | **TOUS** les fichiers professionnels | Outil validé par l'organisation, contrôles DLP, audit possible |
| **Cloud institutionnel** (La Suite numérique, NextCloud d'organisation, plateformes ministérielles) | Données administratives, agents publics | Outil souverain pour les données régulées |

### 26.2 Documents collaboratifs : qui voit quoi

Un document Google Docs / Word Online / Notion partagé en mode édition donne accès à toutes les versions historiques (les commentaires « supprimés » sont récupérables, les paragraphes effacés sont dans l'historique). Avant de partager :

- **Vérifier les droits** : lecture / commentaire / édition selon ce qui est strictement nécessaire.
- **Vérifier les destinataires** par leur email exact (un email mal tapé donne accès à la mauvaise personne).
- **Pas de lien public** pour des documents qui contiennent des données identifiables.
- **Vérifier l'historique** avant de partager un document hérité : il peut contenir d'anciennes versions confidentielles.

### 26.3 Chiffrement local pour les documents très sensibles

Pour des documents très sensibles que vous voulez stocker dans un cloud personnel sans faire confiance à 100 % au fournisseur (CNI numérisée, copies de documents administratifs critiques, sauvegarde du gestionnaire de mots de passe), ou pour préparer un envoi vers un destinataire identifié, une couche de chiffrement local est utile. Plusieurs outils répondent à des besoins différents :

| Outil | Usage principal | Profil |
|-------|-----------------|--------|
| **Cryptomator** | Coffre chiffré **synchronisé dans un cloud personnel** (iCloud, Drive, Dropbox) — le fournisseur ne voit que du chiffré | Particulier, gratuit, open source, multiplateforme |
| **Zed!** (PRIM'X) | **Conteneur chiffré pour échange** de fichiers sensibles avec destinataires identifiés (par certificat ou mot de passe partagé) | Professionnel / institutionnel, certifié ANSSI sur des versions et périmètres précis ; voir Ch.25.3 |
| **VeraCrypt** | Conteneur ou volume chiffré local, gestion fine, montage à la demande | Profil avancé, gratuit, open source |
| **ZIP avec mot de passe AES-256** | Protection ponctuelle simple d'un fichier (compatible partout) | Cas occasionnels, moins professionnel |

**La distinction essentielle** : Cryptomator et VeraCrypt sont d'abord des **coffres locaux** (le contenu reste chez vous, éventuellement synchronisé via un cloud que vous ne maîtrisez pas). Zed! est d'abord une **valise de transport** (le contenu est chiffré pour être envoyé à un destinataire précis). Les deux logiques sont complémentaires.

Ces solutions ne remplacent pas le bon comportement, mais ajoutent une couche pour les documents les plus sensibles.

---

<a id="chapitre-27"></a>
## Chapitre 27 — IA, traduction, OCR et PDF en ligne : pratique ou fuite invisible ?

*Beaucoup d'incidents du quotidien ne viennent pas d'une attaque sophistiquée, mais d'un mauvais choix d'outil : par confort, par urgence, ou par manque d'alternative connue. C'est probablement le chapitre le plus important de la Partie V — la catégorie de risque qui a le plus augmenté en 2024-2026 est l'externalisation involontaire de données vers des outils en ligne grand public.*

### 27.1 Le problème : l'externalisation invisible des données

Quand on dépose un fichier sur un convertisseur PDF gratuit, qu'on colle un mail dans un assistant IA pour le résumer, ou qu'on transfère un document professionnel vers son Gmail personnel pour « travailler ce weekend », on ne fait pas une erreur de sécurité au sens classique. On fait une **délégation invisible** : le fichier sort de son périmètre maîtrisé, et entre dans un périmètre sur lequel on n'a aucun contrôle réel.

Les questions qu'on ne se pose pas :
- Où le fichier est-il stocké, et pour combien de temps ?
- Qui peut y accéder ?
- Le service le réutilise-t-il pour entraîner un modèle, alimenter une base de données, le revendre, ou simplement le conserver « par défaut » ?
- Si le service est piraté demain, mon fichier sera-t-il exposé ?
- Si je veux supprimer le fichier, est-ce que je peux ? Et la suppression est-elle effective ?

Pour la majorité des outils gratuits en ligne, la réponse à toutes ces questions est : **on ne sait pas vraiment**. Et même si les conditions d'utilisation sont rassurantes, elles peuvent changer, l'éditeur peut être racheté, ou l'éditeur peut être piraté.

### 27.2 Les cas concrets

**Convertir, compresser, fusionner un PDF** sur un site gratuit (iLovePDF, Smallpdf, et des dizaines d'autres) : l'usage est massif et la majorité des utilisations sont sans gravité. Mais déposer un **contrat client**, un **bulletin de salaire**, un **avis d'imposition**, une **CNI numérisée**, ou un **document interne** sur un service tiers gratuit pose un vrai problème — le document quitte votre environnement, sa durée de conservation est floue, et vous n'avez pas signé de DPA (Data Processing Agreement) avec ce prestataire. Pour ces cas, préférer un outil local (Aperçu sur macOS, des outils desktop gratuits sur Windows, LibreOffice, Adobe Acrobat licencié).

**Coller un texte dans une IA conversationnelle publique** (ChatGPT, Claude, Gemini grand public) pour le résumer, le traduire, le reformuler : l'usage est devenu quotidien. Le risque : selon le service et le mode (gratuit, payant, entreprise), les données saisies peuvent être utilisées pour entraîner les modèles, conservées pour audit, ou exposées en cas d'incident de sécurité. Les éléments à NE JAMAIS coller dans une IA publique grand public sans politique d'entreprise dédiée :
- Documents internes confidentiels (rapports, comptes rendus, présentations stratégiques)
- Données clients (noms, emails, adresses, identifiants)
- Données RH (bulletins de salaire, évaluations, contrats)
- Code source propriétaire avec secrets, tokens, ou clés API
- Données de santé (résultats médicaux, ordonnances, dossiers patients)
- Informations financières non publiques
- Documents juridiques (contrats avec clauses de confidentialité)
- Logs ou exports techniques contenant des identifiants utilisateurs réels

La **règle simple** : *« Si je n'aurais pas le droit d'envoyer ce document à une personne extérieure, je ne dois pas le déposer dans un outil externe non validé. »* Cette règle s'applique aussi à l'usage personnel — un avis d'imposition collé dans une IA pour le « comprendre » est en train d'être transmis à un service tiers dont la politique de conservation n'est pas claire.

**Si l'usage IA est nécessaire**, plusieurs alternatives existent selon le contexte :

- **Compte IA entreprise avec engagement contractuel** : mode « workspace » ou « business » avec non-rétention pour entraînement, DPA signé, conformité RGPD. C'est le bon réflexe pour les usages professionnels.
- **Anonymisation forte avant collage** : remplacer les noms réels par des placeholders, masquer les chiffres précis, retirer les identifiants. Acceptable pour des cas ponctuels mais fragile par construction (les patterns peuvent rester reconnaissables).
- **IA locale qui tourne sur sa propre machine** : modèles open source comme **Mistral**, **Llama**, **Gemma**, accessibles via **Ollama**, **LM Studio** ou **GPT4All**. Pour un particulier, les performances sont plus modestes que les grands modèles cloud, mais la confidentialité est totale — rien ne sort de la machine.
- **Alternatives orientées confidentialité côté grand public** : **Lumo** (assistant IA de Proton, hébergé en Europe) annonce une approche « no logs », un chiffrement à divulgation nulle pour les conversations sauvegardées, et l'absence d'utilisation des conversations pour entraîner les modèles. C'est un positionnement explicitement orienté confidentialité, intéressant pour qui veut une IA cloud sans le compromis des grands acteurs grand public. **Nuance importante** : une IA cloud reste une IA cloud — le contenu doit nécessairement être traité côté serveur pour produire la réponse. Les garanties annoncées par l'éditeur sont sérieuses mais ne valent pas une exécution locale. À considérer comme « plus respectueux de la vie privée selon les garanties annoncées par l'éditeur », pas comme une confidentialité absolue.
- **Côté agents publics et administration** : la DINUM développe **Albert** (assistant IA d'État, Etalab) et **La Suite numérique** intègre progressivement des outils IA destinés à l'usage interne de l'administration. Ces solutions, hébergées en France, sont à privilégier pour les usages institutionnels quand elles sont disponibles.

Comme pour les autres outils, **aucune solution n'est « parfaite » dans l'absolu** : une IA locale a des limites de capacités, une IA cloud souveraine évolue dans le temps, une IA entreprise dépend du contrat signé. Le bon choix dépend du niveau de sensibilité du contenu et des obligations de l'organisation.

**Traduire un document confidentiel** dans un traducteur web gratuit : même logique que l'IA. Préférer un outil intégré au système (traduction Apple, traduction Microsoft Office en version entreprise) ou un outil local.

**Outils OCR en ligne** pour scanner un document : un scan d'identité, de bulletin médical, ou de contrat envoyé à un OCR en ligne quitte votre environnement. Préférer les fonctions OCR intégrées au téléphone (Apple Notes, Google Lens local), à un scanner dédié, ou à des logiciels installés.

**Outils de signature électronique gratuits** non agréés : pour un document important, la valeur juridique de la signature dépend du niveau du service. Préférer les services agréés (DocuSign, YouSign, Adobe Sign en version pro) plutôt que des outils gratuits inconnus, surtout pour les contrats avec valeur juridique forte.

### 27.3 Le mélange perso/pro : la fuite par déplacement

C'est le mauvais réflexe le plus banal et le plus fréquent :

- Transférer un document pro vers son Gmail personnel pour le lire ce weekend
- Déposer un fichier d'entreprise sur son Google Drive personnel pour « gagner du temps »
- Utiliser WhatsApp perso pour envoyer des documents internes sensibles à un collègue
- Photographier l'écran du PC pro avec son téléphone perso pour avoir l'info sous la main
- Travailler sur un ordinateur familial non maîtrisé (ordinateur de l'autre conjoint, ordinateur partagé en famille)
- Imprimer un document confidentiel chez soi sans nettoyer la corbeille à papier ni effacer la mémoire de l'imprimante

Le problème n'est pas que ces gestes soient « hackés » — c'est qu'ils créent une **perte de maîtrise** : on ne sait plus où est le document, qui peut y accéder, combien de temps il reste disponible, et comment le supprimer. Si l'entreprise subit un incident, ces fichiers personnels sont hors du périmètre de réponse. Si le particulier subit un incident (compte perso piraté, téléphone volé), les données pro sont compromises.

Le **réflexe** : utiliser exclusivement les outils validés par l'organisation pour les données pro. Si l'organisation n'a pas l'outil adapté, le signaler — c'est un manque qui doit être traité par l'IT, pas contourné par chaque salarié.

### 27.4 Les 4 questions à se poser avant de déposer un fichier

> **Avant d'envoyer ou de déposer un fichier, se poser 4 questions :**
>
> 1. Le document contient-il des données personnelles, professionnelles, médicales, bancaires ou confidentielles ?
> 2. Est-ce que je sais où le fichier est envoyé, et qui peut y accéder ?
> 3. Est-ce que je sais combien de temps il sera conservé, et si je peux le supprimer ?
> 4. Si je suis salarié(e) : mon organisation autorise-t-elle cet outil pour ce type de données ?
>
> Si la réponse à l'une de ces questions est floue, **ne pas déposer le fichier**. Trouver une alternative locale, une alternative validée, ou demander à l'IT.

> **🔵 Lina — Épisode 7 :** Lina doit préparer un document de synthèse pour un client à partir d'un long rapport interne de 80 pages. Elle pense le coller dans une IA grand public pour gagner du temps sur le résumé. Elle s'arrête : le rapport contient des données financières clients, des noms de personnes, des éléments stratégiques. Coller ce contenu dans un service grand public serait une fuite — le rapport est sous accord de confidentialité avec le client. Elle utilise l'outil IA d'entreprise (qui a une politique de non-rétention contractuelle), ou à défaut, elle anonymise fortement le contenu avant collage : noms remplacés, chiffres modifiés, projets renommés. C'est plus long mais c'est conforme.

---

<a id="chapitre-28"></a>
## Chapitre 28 — Gestionnaires de mots de passe, coffres et clés physiques

*Les outils de sécurité eux-mêmes méritent un chapitre. Le meilleur gestionnaire est celui que la personne utilisera réellement, correctement et durablement — pas celui qu'un expert recommanderait dans un monde idéal.*

### 28.1 Quel gestionnaire pour quel profil

| Profil | Outil adapté | Pourquoi |
|--------|--------------|----------|
| **Débutant, usage simple** | Gestionnaire intégré (iCloud Trousseau / Google Password Manager / Microsoft Authenticator) ou Bitwarden gratuit | Déjà installé, gratuit, suffisamment robuste pour un usage standard |
| **Famille** | Bitwarden Families ou 1Password Families | Coffre familial avec partage contrôlé, abonnement modéré |
| **Profil avancé / souveraineté** | KeePassXC (local, open source) | Stockage local maîtrisé, pas de cloud du fournisseur, sauvegarde à organiser soi-même |
| **Comptes très critiques** | Clé physique (YubiKey, SoloKey) + codes de récupération papier | Résistance au phishing, deuxième facteur le plus robuste pour email maître ou compte privilégié |

### 28.2 Le mot de passe maître

C'est le seul mot de passe à retenir, donc le plus important :
- **Long** : au moins 4-5 mots, idéalement plus.
- **Mémorisé**, pas stocké numériquement.
- **Unique** : ne jamais le réutiliser ailleurs.
- **Mémorable** : une phrase de passe avec ponctuation et chiffres (« café.vélo.montagne.Jupiter.2024 » est meilleur que « M0t2P@sse! »).

### 28.3 Le débat TOTP : dans le gestionnaire ou dans une app dédiée ?

Avantages du TOTP dans le gestionnaire : tout est au même endroit, le remplissage est automatique, c'est plus pratique donc plus utilisé.

Inconvénient : si le gestionnaire est compromis, l'attaquant a à la fois le mot de passe ET le second facteur — le MFA perd son sens.

**Le compromis raisonnable** :
- **Comptes critiques** (email maître, banque quand TOTP applicable, gestionnaire lui-même, fournisseurs d'identité utilisés via FranceConnect, cloud principal) : application TOTP dédiée (Aegis sur Android ; 2FAS, Ente Auth ou Proton Authenticator sur iOS ; Authy ou Proton Authenticator pour un usage multiplateforme) ou clé physique.
- **Comptes secondaires** (réseaux sociaux, sites de shopping, services secondaires) : TOTP dans le gestionnaire, c'est acceptable et meilleur que pas de MFA du tout.
- **Banque française** : utiliser le moyen d'authentification forte proposé par l'établissement (application bancaire avec validation, Secure Key, biométrie), pas TOTP en général.

### 28.4 Codes de récupération et clés physiques

**Codes de récupération** : à chaque activation de MFA, le service génère des codes à usage unique pour récupérer l'accès en cas de perte du second facteur. Les imprimer ou les noter à la main, et les stocker hors du téléphone (un tiroir à la maison, un coffre, chez un proche de confiance, en double exemplaire). Ne JAMAIS les stocker uniquement dans le gestionnaire de mots de passe (qui devient inaccessible si le téléphone est perdu) ou uniquement dans le téléphone.

**Clé physique** (YubiKey, SoloKey, Titan Security Key) : pour les comptes les plus critiques, une clé physique connectée en USB ou en NFC est le second facteur le plus robuste (résistant au phishing, au clonage, au social engineering). Un usage typique : email maître + gestionnaire de mots de passe avec une clé physique principale et une clé de secours. Quand on choisit cette voie, prendre **toujours deux clés** — une à utiliser, une de secours rangée en lieu sûr. La perte d'une clé sans secours = potentielle perte d'accès.

### 28.5 Coffre papier minimal

Tout ne doit pas être numérique. Un **coffre papier minimal**, à imprimer et à stocker dans un lieu sûr (chez soi, chez un proche, dans un coffre, chez un notaire), contient :
- Le mot de passe maître du gestionnaire (ou la phrase mnémotechnique pour le retrouver).
- Les codes de récupération MFA des comptes critiques.
- Les numéros d'urgence (opposition SIM, opposition bancaire, FAI).
- Le mot de sécurité familial (cf. Ch.20).
- Le contact d'une personne de confiance qui sait où trouver l'essentiel.

L'Annexe J fournit un modèle de fiche d'urgence à imprimer.

---

## Matrice de synthèse — Quels outils privilégier selon le contexte

*Ce tableau récapitule les options évoquées dans la Partie V. Il n'est pas exhaustif, ne prétend pas qualifier les outils dans l'absolu, et ne remplace pas la politique de votre organisation. Il sert de boussole : « pour ce besoin, dans ce contexte, vers quoi regarder ? ».*

| Besoin | Usage courant grand public | Sensible (particulier) | Pro / institutionnel sensible |
|--------|----------------------------|------------------------|-------------------------------|
| **Visioconférence** | Zoom, Meet, Teams, FaceTime | Outil grand public + bons réglages | **Visio de l'État / Webconférence de l'État** (DINUM) ; **Tixeo** pour le très sensible (solution certifiée CSPN ; offre TixeoPrivateCloud sur hébergement qualifié SecNumCloud) |
| **Messagerie instantanée** | iMessage, WhatsApp | **Signal**, **Olvid** | **Tchap** (agents publics), **Olvid** pour échanges très sensibles ou réduction des métadonnées |
| **Transfert de fichiers** | WeTransfer, lien Drive public | **Proton Drive**, **Tresorit**, ou Cryptomator + cloud | **France Transfert** + **Zed!** (chiffrer avant d'envoyer), **Oodrive**, **BlueFiles** selon contexte |
| **Conteneur chiffré** | ZIP avec mot de passe | **Cryptomator** (cloud personnel), **VeraCrypt** | **Zed!** (PRIM'X — certifié ANSSI sur versions/périmètres), **Cryptomator**, VeraCrypt |
| **Cloud / stockage** | iCloud, Google Drive, OneDrive perso | Cloud perso bien configuré + Cryptomator pour les documents très sensibles | Cloud d'entreprise ou solution **SecNumCloud** (Outscale, Oodrive, NumSpot, S3NS selon contexte) |
| **IA (résumer, traduire, reformuler)** | ChatGPT, Claude, Gemini grand public | IA locale (Mistral/Llama via Ollama), anonymisation forte, **Lumo** (Proton) pour cloud orienté vie privée | IA d'entreprise validée avec DPA et non-rétention ; côté État : **Albert** (Etalab) et IA de La Suite numérique quand disponibles |
| **Authentification forte** | Code SMS | Application TOTP (Aegis, 2FAS, Ente Auth, Proton Authenticator, Authy), passkeys | TOTP + clé physique (YubiKey, SoloKey) sur les comptes critiques |
| **Coffre-fort de mots de passe** | Gestionnaire intégré OS | Bitwarden, 1Password, KeePassXC | Gestionnaire validé par l'organisation, idéalement avec partages d'équipe contrôlés |

**Trois rappels pour bien lire ce tableau** :

1. *Le bon outil dépend du niveau de sensibilité.* Un même contenu peut basculer d'une catégorie à l'autre selon le contexte (un échange entre amis devient sensible si on partage un RIB).
2. *Le canal transporte. Le conteneur protège.* Combiner France Transfert (canal souverain) avec Zed! (conteneur chiffré) donne une défense en profondeur — si l'un fuite, l'autre tient.
3. *Une certification ANSSI (CSPN, qualification Élémentaire / Standard / Renforcée, qualification SecNumCloud) porte sur une version, une configuration et un périmètre précis.* C'est un signal fort de sérieux, mais ce n'est ni une garantie absolue ni une recommandation universelle. Toujours respecter la politique de l'organisation et vérifier que la version utilisée est bien celle qui est qualifiée.

---

> ### 🟦 Réflexes — Fin de Partie V
>
> **À configurer** :
> - Outil de visio adapté à chaque cadre (perso / pro / institutionnel) ; pour le très sensible : **Tixeo** ou solution équivalente certifiée, qualifiée ou validée par l'organisation selon le périmètre d'usage
> - **Signal** ou **Olvid** pour les conversations privées sensibles ; **Tchap** si agent public ; **Olvid** pour les échanges très sensibles ou nécessitant une réduction forte des métadonnées
> - Partages cloud nominatifs avec durée d'expiration, pas de lien public permanent
> - **Conteneur chiffré** pour envoyer des fichiers sensibles : **Zed!** côté pro/institutionnel, **Cryptomator** côté particulier
> - Gestionnaire de mots de passe en place avec mot de passe maître unique mémorisé
> - Codes de récupération MFA imprimés en lieu sûr
>
> **À éviter** :
> - Outil grand public par défaut quand un outil institutionnel ou validé existe
> - Lien « toute personne ayant le lien » pour des documents sensibles
> - Documents pro dans un cloud / une messagerie / une IA personnels
> - Données régulées dans une IA grand public
> - Stockage exclusif des codes de récupération dans le téléphone ou dans le seul cloud
>
> **À vérifier** :
> - Liste des partages cloud actifs (semestriel) — révoquer ce qui n'est plus utile
> - Outils utilisés au quotidien : sont-ils adaptés au niveau de sensibilité ?
> - Pour les agents publics : connaissance et activation des outils institutionnels disponibles
> - Présence d'au moins une clé physique de secours pour les comptes critiques (si cette voie est choisie)
>
> **Si quelque chose arrive** :
> - Document sensible déposé par erreur dans un outil public → supprimer la conversation, désactiver la rétention pour entraînement si possible, signaler à la DSI/RSSI si pertinent (cf. Annexe I)
> - Lien de partage qui a fuité → révoquer immédiatement, créer un nouveau lien nominatif si besoin
> - Perte de clé physique sans secours → utiliser les codes de récupération, recréer un MFA, racheter une nouvelle clé immédiatement

---
