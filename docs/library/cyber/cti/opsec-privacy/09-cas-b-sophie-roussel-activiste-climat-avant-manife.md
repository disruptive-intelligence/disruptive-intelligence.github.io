---
title: 'Cas B — Sophie Roussel : activiste climat avant manifestation'
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - index.md
---

## B.1 Contexte

Sophie Roussel, 28 ans, activiste climatique française, exposée à une surveillance administrative et policière régulière en raison de sa participation à des mouvements visés par des dispositifs de renseignement de prévention. Participe à des manifestations dont certaines ont été qualifiées d’« interdites » ces dernières années. Domicile en colocation, vie sociale très active sur les réseaux sociaux militants. Elle s’apprête à participer à une manifestation à Paris contre un projet d’extension d’aéroport régional, manifestation que les organisateurs annoncent comme « pacifique mais désobéissante » — risque élevé d’arrestations, possibilité d’interpellations préventives, présence policière massive annoncée.

Adversaires plausibles :

- **Forces de l’ordre françaises** : capacité élevée localement, ordres judiciaires accessibles, IMSI catchers déployés régulièrement en manifestations (cas documentés par La Quadrature et amicus brief CEDH), reconnaissance faciale en croissance.
- **Infiltrés ou indicateurs** : capacité humaine, fait partie du modèle traditionnel français.
- **Contre-mouvements radicaux** : capacité faible, motivation modérée (harcèlement sur RS si Sophie est identifiée).
- **Employeur futur potentiel** : screening en cas de candidature, mais hors périmètre immédiat.

Hors périmètre :

- Résistance à un mandat de perquisition légal au domicile.
- Anonymat total dans son cercle militant.
- Empêcher la captation par caméra publique.

## B.2 Préparation 72h avant manifestation

**Configuration de l’appareil de manifestation** :

- Pixel 4a d’occasion acheté il y a 18 mois (Sophie l’utilise spécifiquement pour les actions). GrapheneOS depuis l’achat.
- Profil utilisateur dédié manifestation : aucun compte personnel, contacts limités à : 1) avocat collectif activiste, 2) hotline juridique du Syndicat de la Magistrature, 3) un seul proche désigné référent (son colocataire), 4) le numéro d’urgence collectif de la manifestation.
- Apps : Signal (compte burner, créé avec une carte SIM prépayée — Sophie a vérifié que les SIM prépayées avec petit montant nominal restent achetables anonymement sous certaines conditions ; en pratique en France et Belgique, depuis 2017-2021, l’identité est demandée pour activation). Solution alternative : eSIM via service IP comme JMP.chat, financée en Monero. Signal username préféré.
- Briar installé en sauvegarde : permet communication Bluetooth/Wi-Fi local entre activistes voisins même si le réseau est coupé (cas en manifestation).
- Aucune photo, aucun document, aucun mail.
- Code de déverrouillage : 8 chiffres aléatoires, non lié à des données personnelles, *non biométrique* (Sophie a délibérément désactivé l’empreinte sur ce téléphone — la jurisprudence française permet à un officier de police de demander une biométrie, contraint à fournir code reste juridiquement nuancé).
- BFU forcé : Sophie va éteindre complètement le téléphone avant le départ et ne le déverrouillera que si nécessaire.

**Configuration physique** :

- Sac avec pochette Faraday (achetée chez un fournisseur sérieux, testée — un téléphone en pochette Faraday correcte doit perdre 100 % du signal cellulaire et Wi-Fi).
- Téléphone secondaire et utilitaire (clés perso, etc.) restés au domicile, vraiment éteints.
- Bloc-notes papier dans le sac : numéros importants (avocat, hotline, référent) en clair. Si l’appareil est saisi, ces numéros restent accessibles à Sophie via la mémoire ou ce papier.
- Ne porte pas son portefeuille personnel — porte uniquement une CB prépayée chargée avec 60 € en cash dans une carte distincte, et 100 € en espèces.

**Configuration personnelle** :

- Pas de bijoux distinctifs, pas de tatouage visible (sans contrainte vestimentaire excessive), vêtements anonymes (sweat à capuche, masque selon contexte).
- Sac à dos générique sans signe distinctif personnel.
- Pas d’agenda imprimé contenant des noms.

## B.3 Brief avant manifestation

Sophie participe à un brief avec son collectif la veille au soir, en présentiel dans un local fermé, téléphones dans une pile à l’entrée (« phone stack ») pour éviter écoute et géolocalisation partagée. Au brief :

- Plan de déplacement, lieux de rendez-vous, points de regroupement en cas de dispersion.
- Identification des sympathisants membres du collectif vs participants extérieurs (vigilance infiltrés).
- Procédure en cas d’arrestation : utiliser le droit au silence, ne rien dire avant arrivée de l’avocat, appeler le numéro de hotline juridique (mémorisé).
- Rappel des règles : pas de photo du visage des camarades sans accord explicite, pas de live sur les RS personnelles.

## B.4 Le jour J

Sophie part du domicile avec :

- Téléphone manifestation, éteint complètement, en pochette Faraday dans son sac.
- Bloc-notes papier avec numéros essentiels.
- 100 € cash + CB prépayée.
- Bouteille d’eau, lunettes (utiles contre gaz lacrymogène), masque, badge de presse non — Sophie n’est pas journaliste.

Au point de rendez-vous, elle sort le téléphone de la pochette Faraday, le démarre (toujours en BFU à ce stade puisqu’elle ne l’a pas déverrouillé). Active le mode avion. Ne déverrouille que si elle doit envoyer un signal au référent ou contacter l’avocat. Reste majoritairement en BFU pendant la manifestation.

À 14h30, premiers heurts. Charge des forces de l’ordre. Sophie se replie. Plus tard, elle est interpellée en bord de cortège, malgré son comportement défensif (elle ne portait pas d’arme et n’avait pas commis de délit). Interpellation préventive : maintenue en garde à vue 24h pour vérification.

## B.5 Procédure d’arrestation

- Téléphone éteint, en BFU. Saisie possible mais accès des outils forensics commerciaux structurellement plus difficile en BFU qu’en AFU.
- Au commissariat, les officiers demandent à Sophie de communiquer son code de déverrouillage. Sophie connaît l’enjeu juridique : l’article 434-15-2 du Code pénal sanctionne le refus de remettre une convention secrète de déchiffrement (jusqu’à 3 ans et 270 000 €). La jurisprudence sur le statut exact du code de déverrouillage d’un téléphone par rapport à une « convention secrète » au sens du texte est nuancée et a varié selon les juridictions et les faits (cf. Ch 37.5). Sophie ne tente pas d’apprécier seule cette question juridique.
- Elle indique aux officiers qu’elle souhaite consulter son avocat avant de répondre à toute demande, et invoque son droit au silence sur les éléments pénalement intéressants en attendant. Son colocataire, prévenu à H+2 par la procédure d’urgence, a contacté la hotline juridique du collectif. L’avocat collectif activiste arrive après quelques heures.
- En présence de l’avocat, Sophie discute des suites à donner à la demande de code, en tenant compte de la nature des faits qui lui sont reprochés (le motif initial d’interpellation), des conséquences possibles d’une communication ou d’un refus, et de la stratégie pénale globale. La décision est une décision juridique individuelle prise en conseil — ce cours n’a pas vocation à la recommander dans un sens ou dans l’autre.
- Le téléphone est saisi pour analyse forensique. Garde à vue prolongée à 48h. Libération sans poursuites au-delà de la qualification résiduelle qui sera examinée ultérieurement.

## B.6 Post-arrestation

- Le téléphone n’est pas restitué immédiatement (rétention pour expertise). Sophie considère le téléphone comme **brûlé** : ne sera plus jamais utilisé même si restitué (pour ne pas le réintégrer compromis dans sa stack).
- Sophie poursuit la procédure avec son avocat. Continue ses communications collectives via le téléphone du colocataire pour la suite.
- Audit de son domicile : son colocataire vérifie qu’il n’y a pas eu visite (les vis du laptop perso de Sophie ont leur vernis intact, photo macro inchangée).
- Procédure : selon l’évolution juridique du dossier, Sophie peut être convoquée ultérieurement pour audition sur différents motifs. L’analyse juridique reste menée par son avocat, qui décide avec elle de la stratégie au fur et à mesure.

## B.7 Leçons

1. **BFU vraiment.** Le téléphone vraiment éteint à l’arrivée fait la différence forensique : ce qui se passe en garde à vue dépend en partie de l’état dans lequel l’appareil est saisi.
1. **Code mémorisé > biométrie** structurellement. Sous coercition (ou simplement face à une demande d’un officier qui peut techniquement utiliser une empreinte sans coopération active), le code mémorisé non biométrique reste plus difficile à obtenir.
1. **Préparation collective**. La hotline juridique, l’avocat collectif, le référent désigné : la résilience repose sur le réseau, pas sur l’individu seul. Toute question juridique en garde à vue se traite avec un avocat, pas seule.
1. **Téléphone brûlé après saisie**, jamais réintégré dans la stack.
1. **Compartimentation totale** : la vie quotidienne de Sophie n’a pas été affectée. Son téléphone personnel, ses comptes personnels, son ordinateur restent intacts et utilisables.

-----
