---
title: PARTIE IV — COMMUNICATIONS, ARNAQUES ET INGÉNIERIE SOCIALE
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
chapter: 5
chapters: 9
---

*Les attaques les plus fréquentes et les plus impactantes arrivent par les canaux de communication. Cette partie couvre les mécanismes, les signaux d'alerte, et les réflexes.*

---

<a id="chapitre-15"></a>
## Chapitre 15 — Email, SMS et messageries : reconnaître les pièges

Les vecteurs : **phishing par email** (faux email d'un service légitime — banque, impôts, La Poste, Netflix, PayPal, Amazon), **smishing par SMS** (faux SMS de livraison — « votre colis est en attente de confirmation de livraison », faux Ameli — « votre carte Vitale arrive à expiration », faux CPF — « votre solde CPF expire le 31/12 », faux contravention — « vous avez un PV non payé »), et **phishing par messagerie** (WhatsApp, Telegram, Instagram DM — « ton compte va être supprimé, vérifie-toi ici »).

Les **signaux d'alerte** : urgence (« action requise immédiatement », « votre compte sera fermé »), adresse d'expéditeur suspecte (service-client@banque-securite.com au lieu de @banque.fr — regarder l'adresse complète, pas seulement le nom affiché), lien qui ne correspond pas au domaine officiel (sur ordinateur : survoler le lien sans cliquer pour voir l'URL de destination ; sur mobile : appui long sur le lien pour afficher l'URL), fautes d'orthographe et de mise en page (en diminution avec l'IA — les phishings générés par IA sont de plus en plus parfaits), demande d'informations sensibles (aucune banque, aucune administration, aucun service légitime ne demande le code de carte, le mot de passe, ou le code SMS par email ou SMS), et pièces jointes inattendues (PDF, ZIP, HTML, fichiers Office — ne pas ouvrir sans vérification).

Les **bons réflexes** : ne pas cliquer sur le lien → aller directement sur le site officiel en tapant l'URL dans le navigateur. Ne pas appeler le numéro dans le message → appeler le numéro officiel trouvé sur le site ou au dos de la carte bancaire. Ne pas répondre au message suspect → le signaler (Signal Spam pour les emails, 33700 pour les SMS). Le **canal n'est pas une preuve de légitimité** : un SMS qui arrive dans la même conversation que les vrais SMS de la banque peut être frauduleux — les attaquants usurpent les identifiants d'envoi (spoofing de sender ID).

**Limite :** le phishing est de plus en plus sophistiqué — copies pixel-perfect, domaines visuellement identiques (paypa1.com), contextualisation personnalisée. Aucun réflexe ne garantit 100 % de protection — c'est pourquoi le MFA et la surveillance des comptes sont des filets de sécurité complémentaires.

---

<a id="chapitre-16"></a>
## Chapitre 16 — Faux support technique et faux conseillers

Le **faux support technique** : un pop-up alarmiste apparaît sur l'écran (« ALERTE VIRUS ! VOTRE ORDINATEUR EST INFECTÉ ! APPELEZ IMMÉDIATEMENT LE 01 XX XX XX XX ») ou un appel entrant prétendant être Microsoft/Apple/le FAI. Le « technicien » demande de prendre le contrôle à distance (via TeamViewer, AnyDesk, ou le partage d'écran intégré) → une fois le contrôle obtenu, il installe un logiciel malveillant, simule des « réparations » fictives, et demande un paiement (de 150 à 500 €). Le réflexe : fermer le pop-up (Alt+F4 ou forcer la fermeture du navigateur), ne JAMAIS appeler le numéro affiché, ne JAMAIS donner le contrôle de son ordinateur à un inconnu qui appelle. Microsoft, Apple, Google et les FAI ne contactent JAMAIS les utilisateurs de manière proactive pour signaler un virus.

Le **faux conseiller bancaire** : un appel entrant avec un numéro qui ressemble au numéro officiel de la banque (spoofing de numéro — l'identifiant d'appel affiché est falsifié, le vrai numéro d'origine est différent). Le « conseiller » connaît des informations partielles sur la victime (nom, banque, derniers chiffres de la carte — trouvés dans des fuites de données publiées en ligne) et demande de « confirmer » un virement suspect ou de « bloquer une opération frauduleuse » en dictant un code reçu par SMS.

Le **mécanisme** : le faux conseiller a initié lui-même une opération frauduleuse sur le compte de la victime (virement, ajout de bénéficiaire, souscription). Le code SMS que la victime « confirme » est en réalité le code qui valide cette opération. La victime valide elle-même la fraude en croyant la bloquer. C'est l'une des arnaques bancaires les plus documentées et les plus coûteuses observées en France en 2024-2025.

Le **réflexe absolu** : ne JAMAIS donner un code reçu par SMS à quelqu'un qui appelle — jamais, sous aucun prétexte, quelle que soit la raison invoquée. **Raccrocher et rappeler le numéro officiel** (celui au dos de la carte bancaire ou sur le site officiel de la banque). Un vrai conseiller bancaire ne demandera JAMAIS un code SMS par téléphone, ne demandera JAMAIS de valider une opération pendant un appel, et comprendra parfaitement que vous raccrochiez pour rappeler.

---

<a id="chapitre-17"></a>
## Chapitre 17 — Banque, paiements, e-commerce et marketplaces

Les **faux sites marchands** : copie d'un site légitime avec un domaine proche (soldes-decathlon.fr au lieu de decathlon.fr, amazon-deals-fr.com au lieu de amazon.fr). Les signaux : prix systématiquement 40-70 % en dessous du marché (« trop beau pour être vrai » est presque toujours vrai), pas de mentions légales, pas de numéro SIRET vérifiable, paiement uniquement par virement ou carte (pas de PayPal ni de solution connue), et un site récemment créé (vérifiable via un Whois). Le **faux espace bancaire** : lien de phishing → page de connexion identique au site de la banque → les identifiants sont capturés → l'attaquant se connecte au vrai site avec les identifiants volés. Le réflexe : ne JAMAIS accéder au site de la banque via un lien — toujours taper l'URL directement ou utiliser l'application mobile officielle.

La **fraude à la carte bancaire** : utilisation de la carte en ligne sans le consentement du porteur. Opposition immédiate via l'app bancaire (la plupart des apps permettent de bloquer la carte en un clic) ou le numéro de la banque. Remboursement garanti par la loi pour les opérations non autorisées (article L133-18 du Code monétaire et financier — la banque doit rembourser immédiatement sauf si elle prouve la négligence grave du porteur). Le **faux 3-D Secure** : un pop-up qui imite la page d'authentification forte de la banque mais qui capture les informations → vérifier que la page d'authentification est sur le domaine de la banque.

Les **arnaques marketplace** (Leboncoin, Vinted, Facebook Marketplace) : le faux vendeur qui demande un paiement hors plateforme (« mon lien de paiement est plus simple, passons par PayPal/virement »), le faux acheteur qui envoie un faux lien de paiement (« j'ai payé, validez la réception ici » → le lien est une page de phishing qui capture les informations bancaires du vendeur), et l'IBAN modifié (dans les transactions entre particuliers par email, l'IBAN peut être intercepté et modifié → confirmer l'IBAN par un second canal — appel téléphonique, SMS).

Les **dark patterns** et la manipulation commerciale : les abonnements cachés (essai gratuit 7 jours → prélèvement automatique de 49,99 €/mois si on n'annule pas avant — et l'annulation est volontairement difficile), les cases pré-cochées (« je souhaite recevoir des offres de nos partenaires »), les faux compteurs d'urgence (« plus que 2 articles à ce prix ! », « 15 personnes regardent ce produit en ce moment » — souvent fictifs), et les consentements forcés (cookie banners avec « Tout accepter » en gros bouton vert et « Gérer les préférences » en tout petit lien gris).

### 17.bis — Abonnements et prélèvements récurrents : reprendre la main

Au-delà des dark patterns à l'inscription, il y a la dérive lente des abonnements. Un foyer moyen accumule des abonnements actifs : streaming vidéo et musique, applications, cloud, presse, salle de sport, box mensuelle, services bancaires, assurances complémentaires. Beaucoup sont oubliés et continuent de prélever — l'essai à 0,99 € de l'an dernier facture aujourd'hui 19,99 €/mois.

**Inventorier** : la liste des prélèvements récurrents est visible dans l'app bancaire (« mandats SEPA », « abonnements »), dans les paramètres de l'App Store / Google Play (achats récurrents), et dans les paramètres PayPal (paiements automatiques). À faire au moins une fois par an — idéalement tous les 6 mois.

**Repérer les pièges fréquents** : essais gratuits qui basculent en payant sans alerte, abonnements à durée minimale (1 an) renouvelés tacitement, augmentations de tarif unilatérales (le service informe, l'utilisateur n'agit pas, le nouveau tarif s'applique), services dont l'annulation nécessite un appel téléphonique ou un courrier recommandé alors que l'inscription se fait en deux clics.

**Le droit de résiliation** : depuis la loi du 16 août 2022 et son décret d'application (juin 2023), tout service souscrit en ligne doit pouvoir être résilié en ligne en trois clics maximum (« bouton résiliation »). Si un service vous demande un courrier recommandé pour résilier alors que vous l'avez souscrit en ligne, c'est non conforme. Pour les **assurances et mutuelles**, la résiliation infra-annuelle est possible après 1 an pour la plupart des contrats (loi Hamon). Pour les **télécoms**, la résiliation est gratuite après la période d'engagement initial.

**Surveillance bancaire** : activer les notifications de prélèvement dans l'app bancaire (chaque opération déclenche une notification) — ça révèle immédiatement les prélèvements oubliés et les fraudes naissantes. Un prélèvement inconnu : opposition immédiate sur le mandat SEPA (la banque peut bloquer un créancier), contestation, remboursement (8 semaines pour contester un prélèvement SEPA autorisé, 13 mois pour un prélèvement non autorisé).

**Carte virtuelle / éphémère** pour les essais gratuits : la plupart des banques en ligne (Revolut, N26, Boursorama, BNP Hello bank!) proposent des cartes virtuelles à usage unique ou plafonnées. Utiliser une carte virtuelle pour les essais gratuits permet de bloquer automatiquement le passage en payant sans avoir à se souvenir d'annuler.

---

<a id="chapitre-18"></a>
## Chapitre 18 — Arnaques à l'investissement, crypto et faux placements

*Sujet majeur de 2024-2026 : les arnaques à l'investissement représentent le poste de pertes financières le plus élevé pour les particuliers — souvent plusieurs dizaines de milliers d'euros par victime. Elles ne ciblent pas uniquement les naïfs : les profils les plus touchés sont des personnes éduquées, financièrement à l'aise, à la recherche de rendement.*

Le **mécanisme général** suit toujours la même trame : (1) **prise de contact** (publicité Facebook/Instagram/TikTok mettant en scène une personnalité connue, message LinkedIn, appel à froid, recommandation d'un « ami » sur WhatsApp/Telegram, intervention d'un faux « conseiller » repéré sur un forum financier), (2) **mise en confiance** (promesses de rendement irréalistes — 10-30 % par mois — présentées comme « réservées à un petit cercle d'initiés » ; site web professionnel, faux avis clients, faux témoignages vidéo générés par IA, faux agréments AMF affichés), (3) **premier dépôt** (souvent modeste — 250 à 500 € — pour amorcer la relation ; l'application affiche une croissance immédiate du capital), (4) **escalade progressive** (l'utilisateur est encouragé à investir davantage ; il peut « retirer » de petites sommes au début pour renforcer la confiance ; les rendements affichés sur l'interface sont entièrement fictifs — c'est juste une page web), (5) **blocage** (au moment où la victime veut retirer une somme importante, on lui demande de payer des « frais », des « taxes », un « audit de conformité » avant le retrait — chaque paiement est encaissé, le retrait n'arrive jamais), (6) **arnaque à la récupération de fonds** (quelques semaines plus tard, la victime est recontactée par un faux « cabinet d'avocats spécialisé en récupération de fonds crypto » — qui demande un nouveau paiement pour récupérer l'argent perdu).

Les **types d'arnaques fréquents** :

Les **faux brokers / faux trading** : plateformes qui imitent l'interface d'un vrai broker, avec un faux conseiller dédié qui guide la victime au téléphone. Promesses de rendements garantis sur le forex, les CFD, les actions ou les matières premières. Les « gains » affichés à l'écran sont fictifs.

Les **arnaques crypto** : faux échanges de cryptomonnaies, fausses ICO, faux projets DeFi, fausses opportunités de yield farming, faux NFT à valeur garantie, fausses « formations crypto » qui débouchent sur un « accompagnement personnalisé » payant. Les arnaqueurs exploitent le fait que la crypto est mal comprise du grand public et que les promesses de gains rapides y semblent moins absurdes.

Les **faux livrets bancaires / faux placements** : pseudo-comptes à terme à 7-12 % par an (les vrais livrets en 2025-2026 plafonnent à des taux bien plus modestes), faux investissements dans des « obligations vertes », « crypto-livrets garantis par l'État ». Site qui imite une banque réelle ou crée une fausse banque crédible — souvent avec un nom proche d'un établissement existant pour exploiter la confusion.

Les **faux placements « verts »** et faux investissements dans la transition énergétique : « panneaux solaires à rentabilité garantie en 5 ans », « parts dans une centrale photovoltaïque locale », « investissement dans une coopérative éolienne », « financement participatif pour la rénovation énergétique avec rendement garanti à 8 % ». Le verbiage écologique sert à habiller une arnaque classique en projet citoyen attractif. Les promesses sont incompatibles avec les rendements réels du secteur, et les structures derrière sont souvent fictives ou non agréées. Vérification : agrément AMF pour le financement participatif (statut PSFP — Prestataire de Services de Financement Participatif), listes noires AMF, et registre REGAFI.

Les **faux démarchages à domicile** liés à l'énergie ou à la rénovation : « technicien de l'énergie », « conseiller MaPrimeRénov' », « audit gratuit obligatoire » → soit pour faire signer un contrat abusif (panneaux solaires surfacturés, isolation à 1 € qui ne tient pas ses promesses), soit pour collecter des informations personnelles (RIB, avis d'imposition) qui serviront à monter un dossier d'aide publique frauduleux au nom de la victime, soit les deux. Le réflexe : aucun organisme public ne fait du démarchage à domicile pour MaPrimeRénov', les CEE (Certificats d'Économies d'Énergie), ou les aides à la rénovation. Toute personne qui se présente comme « mandatée par l'État » à votre porte ou par téléphone est suspecte.

Le **pig butchering** (« dépeçage de cochon ») : une arnaque longue durée où l'arnaqueur établit une relation personnelle (souvent romantique ou amicale) avec la victime sur plusieurs semaines via WhatsApp, Telegram ou les réseaux sociaux, puis l'incite progressivement à investir dans une plateforme frauduleuse. Le mélange manipulation affective + arnaque financière rend cette arnaque particulièrement dévastatrice.

Les **influenceurs financiers douteux** : Instagram, TikTok, YouTube, Telegram — des « experts » mettant en scène voitures de luxe, voyages, gains supposés, qui orientent leur audience vers des plateformes affiliées (souvent frauduleuses) ou des « formations » à plusieurs milliers d'euros. La régulation française et européenne s'est durcie (les recommandations financières non agréées sont interdites), mais le phénomène reste massif.

Les **signaux d'alerte universels** :
- Promesse de rendement régulier élevé (au-dessus de 7-8 % par an, déjà douteux ; au-dessus de 15 %, c'est une arnaque dans 99 % des cas — un placement qui rapporte vraiment ce niveau ne serait pas démarché à un inconnu sur Instagram)
- Promesse de capital « garanti » associé à un rendement élevé (mathématiquement incompatible)
- Pression à investir rapidement avant la « fin de l'opportunité »
- Demande d'investir des sommes croissantes
- Frais demandés avant un retrait
- Plateforme non agréée par l'AMF (Autorité des marchés financiers) ou l'ACPR (Autorité de contrôle prudentiel)
- Conseiller dédié qui appelle quotidiennement
- Recommandation par une connaissance récente sur les réseaux sociaux

Les **vérifications à faire avant d'investir** :
1. Consulter les **listes noires de l'AMF** (sur listes-noires.amf-france.org) pour vérifier si la plateforme est signalée comme frauduleuse ou non autorisée — l'AMF publie en continu les noms des sites et entités frauduleuses signalés. Si la plateforme y apparaît, c'est une arnaque.
2. Vérifier l'**agrément** de l'entité sur **REGAFI** (Registre des agents financiers — regafi.fr) lorsque l'activité relève des services financiers réglementés. REGAFI n'est pas une liste noire : c'est le registre des entités autorisées à exercer en France ; une plateforme qui prétend offrir des services d'investissement et qui n'y figure pas est suspecte.
3. Vérifier le **domaine** : âge du nom de domaine (un Whois indique la date de création — un site « banque historique » créé il y a 2 mois est une arnaque), géolocalisation, mentions légales cohérentes.
4. **Rechercher le nom de la plateforme + « avis » + « arnaque »** sur Google et sur les forums d'investisseurs (Forum-Investisseur, Reddit r/vosfinances, etc.).

Le **réflexe de dernier recours** : si l'on a déjà commencé à investir et qu'on a un doute, **arrêter immédiatement** — ne pas répondre aux appels du « conseiller », ne pas verser un euro de plus pour un « retrait » ou des « frais », et signaler à l'AMF (epargne-info-service@amf-france.org) et déposer plainte (THESEE en ligne ou commissariat).

L'**arnaque à la récupération de fonds** : une fois victime, la victime devient cible. Des « cabinets de récupération » contactent les victimes connues (bases de données revendues entre arnaqueurs) en promettant de récupérer les fonds perdus moyennant un acompte. C'est une **seconde arnaque** sur le dos de la première. Aucun cabinet sérieux ne demande de paiement préalable pour récupérer des fonds — les vraies procédures passent par la justice et les banques.

---

<a id="chapitre-19"></a>
## Chapitre 19 — Réseaux sociaux, faux profils, sextorsion et arnaques relationnelles

L'**usurpation d'identité** : un faux profil utilise le nom, les photos et les informations d'une vraie personne → pour escroquer les contacts de la victime (« je suis bloqué à l'étranger, peux-tu m'avancer 200 € ? ») ou pour arnaquer des inconnus en se faisant passer pour quelqu'un de confiance. Le **catfishing et les romance scams** : faux profil romantique, relation développée sur plusieurs semaines ou mois (parfois via des messages quotidiens, des appels, des projets communs), puis demande d'argent (billet d'avion pour « venir te voir », urgence médicale, investissement « sûr » — souvent couplé avec l'arnaque à l'investissement du Ch.18 — c'est le pig butchering). Les pertes constatées sur ce type d'arnaque sont fréquemment élevées (plusieurs milliers d'euros par victime selon les cas remontés aux autorités), et le traumatisme psychologique associé est considérable.

### 19.1 Sextorsion et chantage intime

*Risque réel et fréquent, particulièrement pour les adolescents et jeunes adultes mais touchant tous les âges.*

Le **mécanisme classique** : l'attaquant approche la cible sur un réseau social (Instagram, Snapchat, TikTok, Tinder) ou une application de rencontre, déclenche rapidement une conversation à caractère sexuel, demande des photos ou une vidéo intime (souvent en proposant lui-même de partager — en réalité une vidéo récupérée ailleurs), enregistre ou capture le contenu envoyé par la victime, puis menace de diffuser le contenu à la famille, aux amis et aux contacts professionnels (souvent récupérés via le profil public LinkedIn ou la liste d'amis Facebook) si la victime ne paie pas — généralement en cryptomonnaie ou cartes cadeaux.

Les **variantes** : la **sextorsion par bluff** (l'attaquant prétend avoir piraté la webcam et avoir filmé la victime visitant un site pornographique, exige un paiement ; il n'a en réalité rien — c'est un email de masse envoyé à des millions de personnes, parfois avec un mot de passe de la victime trouvé dans une fuite de données pour donner du crédit à la menace), la **sextorsion sur un proche** (faux profil qui contacte un adolescent en se faisant passer pour un ami d'ami, escalade rapide), et la **sextorsion deepfake** (une photo « anodine » de la victime — visage public sur un réseau social — est utilisée pour générer un faux contenu sexuel par IA, et l'attaquant fait chanter avec ce faux contenu).

Le **réflexe absolu** : **NE PAS PAYER**. Payer ne fait que confirmer que la victime est exploitable, et la pression s'intensifie. Dans la majorité des cas où la victime paie, l'attaquant revient avec une seconde demande. Et dans un très grand nombre de cas où la victime ne paie pas, l'attaquant ne diffuse rien — la diffusion est une menace, mais elle ne sert pas son intérêt (s'il diffuse, il perd tout pouvoir et la victime n'a plus rien à perdre).

Les **actions à mener** :
1. **Bloquer immédiatement** l'attaquant sur la plateforme.
2. **Conserver les preuves** : captures d'écran de toutes les conversations, du profil de l'attaquant, des menaces, des demandes de paiement, des messages envoyés à votre entourage si l'attaquant a déjà mis ses menaces à exécution.
3. **Signaler à la plateforme** (chaque grand réseau social a un canal de signalement spécifique pour le chantage et la sextorsion).
4. **Signaler aux autorités** : Pharos (internet-signalement.gouv.fr) ou plainte (commissariat ou THESEE en ligne). En France, la sextorsion et le chantage sont des délits pénaux passibles de plusieurs années de prison — la justice prend ces dossiers au sérieux.
5. **Contacter une association d'aide** : e-Enfance / 3018 (gratuit, anonyme, 7j/7 de 9h à 23h, dédié notamment aux mineurs et jeunes adultes), Stop-Cyberviolence, France Victimes (116 006). L'accompagnement psychologique est important — la sextorsion est traumatisante, et la honte est l'un des leviers que l'attaquant exploite.
6. **Si la diffusion a déjà eu lieu** : la loi française protège les victimes de diffusion non consentie d'images intimes (« revenge porn » — article 226-2-1 du Code pénal). Saisir la plateforme pour retrait, déposer plainte, et solliciter la CNIL pour le déréférencement des moteurs de recherche.

La **prévention** : ne pas envoyer de contenu intime à un contact rencontré récemment en ligne (la confiance ne s'établit pas en quelques messages), se méfier des demandes qui escaladent rapidement vers la sphère intime, désactiver l'accès à la liste d'amis sur les réseaux sociaux (un attaquant qui ne peut pas voir vos contacts ne peut pas crédibiliser sa menace de diffusion), et **parler avec ses adolescents** de cette réalité avant qu'elle se présente.

### 19.2 Faux recrutements et arnaques à l'emploi

Offre d'emploi trop belle (salaire élevé, travail à domicile, flexibilité totale, aucune qualification requise) → « envoyez votre CV, pièce d'identité et RIB pour préparer le contrat » → usurpation d'identité (CNI et RIB utilisés pour ouvrir des comptes ou souscrire des crédits frauduleux).

Variante : la victime est recrutée comme « agent de transfert », « testeur de paiement » ou « gestionnaire logistique remote » → elle est utilisée comme **mule financière** pour transiter des fonds volés (réception sur son compte de virements frauduleux, retrait en cash ou retransfert vers un compte étranger ou en crypto). C'est un délit pénal (blanchiment, complicité de fraude) — même quand la mule ignore l'origine criminelle des fonds, elle peut être poursuivie et son compte bancaire est souvent bloqué et clôturé. Les profils ciblés : étudiants, demandeurs d'emploi, personnes en situation de précarité financière.

Variante moderne : le **faux entretien d'embauche par visio** où le recruteur demande l'installation d'une application de « test technique » (en réalité un malware) ou demande un partage d'écran prolongé (pour observer les sessions ouvertes, les emails, les comptes bancaires).

Les **signaux d'alerte** : aucun entretien réel ou entretien expéditif, salaire très supérieur au marché pour des qualifications faibles, demande de pièce d'identité et RIB AVANT la signature d'un contrat de travail, demande de réception et retransfert de fonds pour « tester le système », contrat envoyé sans en-tête vérifiable, entreprise non vérifiable sur Pappers/Infogreffe ou avec une création très récente.

Le **réflexe** : ne JAMAIS envoyer pièce d'identité + RIB avant la signature d'un contrat de travail vérifiable, et ne JAMAIS accepter un emploi qui consiste à recevoir et retransférer des fonds.

### 19.3 Faux logements et arnaques à la location

Arnaque massive en zones tendues (Paris, Lyon, Bordeaux, grandes villes étudiantes). Le mécanisme : annonce attirante (logement bien situé, prix sous le marché, photos professionnelles), faux propriétaire injoignable physiquement (« je suis à l'étranger pour mon travail »), demande d'envoi du dossier complet (CNI, bulletins de salaire, avis d'imposition, RIB) AVANT toute visite, demande d'un acompte ou d'un dépôt de garantie par virement pour « bloquer le logement » avant la visite physique.

Les variantes : annonce reprise frauduleusement (les photos sont celles d'une vraie annonce existante, copiées par un tiers qui n'a aucun lien avec le logement), exigences hors-cadre (le décret n°2015-1437 encadre strictement la liste des documents qu'un bailleur peut exiger — au-delà, c'est illégal et c'est un signal d'alerte).

Le **réflexe** : visite physique AVANT toute envoi de dossier complet, vérification que le « propriétaire » est bien le propriétaire (acte de propriété, taxe foncière), aucun virement avant la signature physique d'un bail vérifié, et utiliser DossierFacile (service public — dossierfacile.logement.gouv.fr) qui filigrane automatiquement les pièces avec la mention de destination.

### 19.4 Faux giveaways et faux influenceurs

Les **faux giveaways** (« iPhone 16 gratuit — likez, partagez et cliquez ici ») → collecte de données personnelles ou phishing. Les **faux influenceurs** et les « formations gratuites » (Instagram, Telegram — « je gagne 5 000 €/mois depuis mon téléphone, je t'explique comment ») → arnaques au trading, au dropshipping, aux crypto-monnaies (cf. Ch.18), ou recrutement de mules (cf. 19.2).

---

<a id="chapitre-20"></a>
## Chapitre 20 — Deepfakes, voix clonées et nouvelles fraudes IA

*Un clone vocal peut être généré à partir de quelques secondes d'audio. En 2025-2026, cette technologie est accessible à n'importe qui.*

Le **deepfake vocal** : un « proche » appelle et demande de l'argent en urgence. « Maman, j'ai eu un accident, je suis à l'hôpital, j'ai besoin que tu fasses un virement maintenant. » La voix est clonée par IA à partir d'un message vocal WhatsApp, d'une story Instagram, ou d'une vidéo YouTube. Le stress et l'émotion (c'est la voix de son enfant, de son parent, de son conjoint) court-circuitent totalement la réflexion rationnelle.

Le **réflexe** : raccrocher et rappeler le proche sur son numéro habituel. Poser une question personnelle que seul le vrai proche peut savoir (« comment s'appelle notre chat ? », « quelle est la couleur de la voiture de papa ? »). Convenir à l'avance d'un « mot de sécurité familial » — un mot ou une phrase convenu entre les membres de la famille, à demander dans toute situation d'urgence où l'identité doit être confirmée. L'IA peut cloner une voix et un visage — elle ne peut pas répondre à une question personnelle qui n'est pas dans les données d'entraînement.

Le **phishing IA** : emails et SMS générés par IA — plus aucune faute d'orthographe, style parfait, contextualisation poussée (l'email mentionne des informations vraies sur la victime trouvées en ligne). Le filtre historique « les arnaqueurs font des fautes » ne fonctionne plus. Le **deepfake vidéo** en visioconférence : moins courant en ciblage individuel mais en augmentation — un faux interlocuteur en visio demande un virement ou des informations.

Les **deepfakes pornographiques** non consentis : génération d'images ou vidéos sexuelles à partir de photos publiques de la victime. Utilisés pour la sextorsion (cf. 19.1) ou pour la diffusion malveillante. La loi française (article 226-8 du Code pénal, modifié en 2024) punit explicitement la production et la diffusion de contenus pornographiques deepfake non consentis. En cas de victimisation, la procédure est la même que pour le revenge porn : conserver les preuves, signaler aux plateformes, déposer plainte, solliciter le déréférencement.

La défense fondamentale : la **vérification hors canal**. Quand une demande urgente arrive par un canal (appel, message, email), la vérifier par un AUTRE canal. Rappeler sur le numéro connu. Envoyer un SMS. Poser une question personnelle. L'IA peut imiter la forme — elle ne peut pas (encore) reproduire la connaissance intime.

---

<a id="chapitre-21"></a>
## Chapitre 21 — Quand le confort remplace la sécurité : les compromis dangereux du quotidien

*Ce chapitre traite les compromis que les gens font consciemment ou inconsciemment entre confort et sécurité — et les moments où le confort coûte plus cher que prévu.*

Le « **je retiens mes mots de passe dans ma tête** » → 3 mots de passe pour 30 comptes = réutilisation massive. Le « **je reste connecté** » → les sessions ouvertes sur tous les services = un accès au navigateur = un accès à tout. Le « **j'accepte toutes les permissions** » → chaque app a accès à tout = surface d'attaque maximale. Le « **j'envoie vite par WhatsApp, c'est plus simple** » → documents sensibles dans une messagerie non maîtrisée. Le « **je sauvegarde sur mon téléphone, ça suffit** » → un téléphone perdu = des années de photos et documents perdues. Le « **je mets à jour demain** » → la fenêtre de vulnérabilité reste ouverte. Le « **ça ne peut pas m'arriver** » → la condition préalable à tout incident.

La **dette de sécurité personnelle** : chaque compromis crée une dette. Individuellement, chaque compromis est à faible risque. Accumulés, ils créent une surface d'attaque considérable — comme les petites dettes financières qui s'accumulent jusqu'à devenir ingérables. Le cours ne demande pas d'être parfait — il demande de faire les **5-10 choix qui réduisent 80 % du risque** : gestionnaire de mots de passe, MFA sur les comptes critiques, sauvegardes, mises à jour automatiques, verrouillage, localisation à distance, et le réflexe « vérifier avant d'agir » (cf. Parcours Express en début de cours).


---

> ### 🟦 Réflexes — Fin de Partie IV
>
> **À configurer** :
> - Notifications bancaires actives pour chaque opération
> - Filtres anti-spam configurés sur l'email
> - Mot de sécurité familial convenu avec les proches (anti-deepfake)
> - Outils IA d'entreprise utilisés exclusivement pour les contenus pro
>
> **Réflexes universels (à graver)** :
> - **Raccrocher et rappeler** pour tout appel inattendu sur un sujet sensible (banque, support, administration)
> - **Ne JAMAIS donner un code SMS reçu** à quelqu'un qui appelle, quel que soit le prétexte
> - **Ne pas cliquer sur les liens** dans SMS / email — accéder au site officiel directement
> - **Vérification hors canal** pour toute demande urgente (rappeler le proche, poser une question personnelle)
> - **Trop beau pour être vrai = c'est faux** (rendement à 20 %, iPhone gratuit, salaire mirobolant sans entretien)
> - **Avant de coller un fichier dans un outil en ligne** : les 4 questions du Ch.27
> - **Avant d'investir** : vérifier listes noires AMF (listes-noires.amf-france.org) et agrément sur REGAFI (regafi.fr)
>
> **À éviter absolument** :
> - Donner sa CNI + RIB avant un contrat de travail ou un bail signé
> - Payer une rançon en cas de sextorsion
> - Verser des « frais » pour débloquer un retrait d'investissement
> - Utiliser une IA grand public avec données pro non anonymisées
> - Transférer des fichiers pro vers des comptes perso
>
> **Si quelque chose arrive** :
> - Phishing détecté → signaler (Signal Spam / 33700) ; pas cliqué = pas grave
> - Phishing avec saisie d'identifiants → changer mot de passe + MFA + cf. Ch.41
> - Perte d'argent par arnaque → opposition + plainte THESEE + signalement AMF si investissement
> - Sextorsion → ne pas payer, conserver preuves, signaler, e-Enfance/Pharos
> - Deepfake reçu → vérifier hors canal, ne pas réagir dans l'urgence

---
