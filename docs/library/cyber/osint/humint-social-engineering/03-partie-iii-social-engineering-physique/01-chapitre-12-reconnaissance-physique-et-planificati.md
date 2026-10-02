---
title: Chapitre 12 — Reconnaissance physique et planification
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie III — Social engineering physique
  - index.md
---

## 12.1 La reconnaissance du site

La reconnaissance physique complète la reconnaissance OSINT et fournit les informations nécessaires à la planification de l'intrusion. Elle se conduit en plusieurs passes, idéalement sur plusieurs jours et à différentes heures.

**Le périmètre.** Identifier toutes les entrées (accueil principal, livraisons, parking souterrain, accès technique, sortie de secours), leur niveau de contrôle (gardien, badge, interphone, portique, tourniquet), et les zones de transition (fumoir, parking, accès cantine externe). Les sorties de secours, souvent équipées d'alarme mais pas toujours surveillées, sont des points d'intérêt fréquents pour les red teamers.

**Les systèmes de contrôle d'accès.** Observer le type de lecteur (RFID basse fréquence 125 kHz — HID ProxCard, facile à cloner ; RFID haute fréquence 13.56 MHz — MIFARE, iCLASS, plus résistant ; NFC mobile), la présence de biométrie (empreintes, iris — rare en entreprise standard), les sas anti-piggyback (tourniquets, portiques à verrouillage unitaire). Les caméras : identifier leur emplacement, leur angle de couverture, la présence de zones d'ombre, et déterminer si elles sont en monitoring live (opérateur présent) ou en enregistrement passif (consultation a posteriori uniquement).

**Les horaires et les flux.** Les heures d'arrivée (8h-9h30 — flux maximum, contrôles relâchés) et de départ (17h-18h30), les pauses (12h-14h — mouvements entre bâtiments, accès cantine), les livraisons (généralement matin, accès souvent moins contrôlé). Le créneau idéal pour une intrusion physique est souvent 10h-11h ou 14h-15h : assez de monde dans les locaux pour ne pas être remarqué, mais assez calme pour éviter les flux où un inconnu serait plus visible.

## 12.2 L'observation comportementale

Au-delà de l'infrastructure physique, le red teamer observe les comportements des employés, qui constituent souvent la vulnérabilité principale.

**Le badge.** Les employés portent-ils leur badge de manière visible (autour du cou, au revers) ? Ou le gardent-ils dans leur poche/portefeuille et le présentent uniquement au lecteur ? Un environnement où le badge n'est pas porté visiblement est un environnement où un intrus sans badge ne sera pas immédiatement repéré.

**Le tailgating naturel.** Les employés tiennent-ils la porte aux personnes derrière eux ? Vérifient-ils le badge de la personne qui les suit ? Dans la grande majorité des entreprises, la norme sociale est de tenir la porte — refuser est perçu comme impoli.

**La vérification des visiteurs.** Les visiteurs sont-ils systématiquement accompagnés ? Ou sont-ils libres de se déplacer après le passage à l'accueil ? Les badges visiteurs sont-ils visuellement distincts des badges employés ? Sont-ils récupérés en fin de visite ?

**Les zones informelles.** Le fumoir, le café, la cantine sont des zones de socialisation où les barrières de sécurité sont naturellement abaissées. Ce sont les points de contact idéaux pour l'élicitation (Ch.14).

## 12.3 Le dumpster diving

La fouille des poubelles (dumpster diving) reste une technique de reconnaissance basique mais efficace. Les poubelles extérieures (sur le trottoir ou dans la zone de collecte) ne sont généralement pas protégées juridiquement (la jurisprudence varie selon les pays — en France, la fouille de poubelles sur la voie publique n'est pas constitutive d'une infraction ; en revanche, pénétrer dans une propriété privée pour accéder aux poubelles constitue une violation de domicile).

Les trouvailles typiques incluent : documents imprimés non déchiquetés (organigrammes, listes de diffusion, procès-verbaux de réunion, rapports intermédiaires), badges expirés (qui peuvent servir de modèle pour la fabrication d'un faux badge visuellement crédible), post-its avec des mots de passe ou des codes, matériel informatique mis au rebut (disques durs non effacés, clés USB, téléphones), et emballages de matériel révélant les technologies utilisées (cartons de serveurs, de switches, d'équipements de sécurité).

**Défense** : politique de destruction documentaire (déchiqueteuse cross-cut minimum — les déchiqueteuses en bandes sont reconstructibles), bennes fermées et cadenassées, sensibilisation au risque des documents jetés sans précaution.

## 12.4 Le matériel du red teamer

La préparation matérielle est critique pour la crédibilité du pretexte et le succès de l'opération.

**La tenue.** Adaptée au pretexte : costume et cravate pour un « auditeur » ou un « consultant », polo logotypé et jean pour un « technicien IT », bleu de travail et gilet haute visibilité pour un « prestataire de maintenance ». Le gilet haute visibilité est l'un des outils les plus puissants du social engineering physique : il confère une légitimité quasi automatique et réduit les questions.

**Le faux badge.** Les badges d'entreprise sont rarement vérifiés visuellement en détail au-delà de la couleur et de la présence d'un logo. Un badge imprimé sur un support similaire (même taille, même orientation, couleur cohérente, logo de l'entreprise récupéré en OSINT) suffit dans la majorité des cas pour l'examen visuel. Le badge ne passera pas un contrôle RFID si la technologie n'est pas clonée (Ch.27), mais dans les environnements où le badge est présenté visuellement (à un gardien) plutôt qu'électroniquement (sur un lecteur), la version imprimée est suffisante.

**Le clipboard.** Le « bouclier social » par excellence. Une personne qui se déplace dans des locaux avec un clipboard (ou un ordinateur portable et une mine concentrée) n'est presque jamais questionnée. Le clipboard projette l'image de quelqu'un en mission, qui a quelque chose à faire et qui sait où il va.

**Les outils techniques.** Dans le cadre d'un red team autorisé : implants réseau (LAN Turtle, rogue access point WiFi), clé USB malveillante (Rubber Ducky, Bash Bunny), keylogger hardware, lecteur RFID (Proxmark3 pour le clonage — voir Ch.27). Ces outils sont transportés discrètement et déployés une fois l'accès physique obtenu.

## 12.5 Le plan d'intrusion

Le plan d'intrusion est un document opérationnel qui couvre : les objectifs (accès à une zone spécifique, connexion d'un implant réseau, accès à un poste de travail, vol simulé d'un document classifié), le timing (jour, heure, durée maximale de présence), les pretextes (principal + au moins un pretexte de secours en cas d'échec du premier), le matériel nécessaire, le plan d'exfiltration (comment quitter les lieux proprement), et le protocole d'urgence.

Le **protocole d'urgence** est indispensable. Si le red teamer est intercepté, confronté ou arrêté par la sécurité, il doit pouvoir s'identifier immédiatement comme testeur autorisé. Le « safe word » est un mot ou une phrase convenu avec le commanditaire qui, prononcé au téléphone avec le contact de référence, confirme instantanément la légitimité de la mission. Le contact de référence (RSSI, DG, ou personne désignée) doit être joignable 24/7 pendant la durée du test.

---
