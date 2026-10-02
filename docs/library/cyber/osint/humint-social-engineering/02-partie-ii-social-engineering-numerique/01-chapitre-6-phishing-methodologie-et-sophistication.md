---
title: 'Chapitre 6 — Phishing : méthodologie et sophistication'
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie II — Social engineering numérique
  - index.md
---

## 6.1 Anatomie d'un email de phishing

Un email de phishing est un système de composantes interdépendantes, chacune contribuant à la crédibilité globale du leurre. Comprendre ces composantes est essentiel pour le praticien — qu'il construise un test autorisé ou qu'il analyse une attaque en cours.

**L'expéditeur.** C'est le premier élément évalué par le destinataire — souvent le seul, sur mobile. L'attaquant dispose de plusieurs techniques pour simuler un expéditeur légitime. Le spoofing d'adresse exploite l'absence ou la mauvaise configuration de SPF/DKIM/DMARC pour envoyer un email qui affiche une adresse légitime dans le champ « From ». Le typosquatting utilise un domaine visuellement similaire (helios-aero.fr → heIios-aero.fr avec un « I » majuscule à la place du « l », ou helios-aer0.fr avec un zéro). Le display name spoofing modifie le nom affiché sans toucher à l'adresse réelle : « Marc Tessier - DG Helios » <attaquant@domaine-malveillant.com> — sur mobile, seul le display name est visible par défaut. La compromission d'email légitime (reply-chain attack) est la technique la plus difficile à détecter : l'attaquant compromet une boîte mail réelle et s'insère dans un fil de conversation existant.

**L'objet.** L'objet détermine l'ouverture de l'email. Les objets les plus efficaces combinent pertinence contextuelle et urgence modérée : « Mise à jour obligatoire — Portail RH » est plus efficace que « URGENT !!! Votre compte sera supprimé !!! » (trop agressif, signaux d'alerte). Les objets qui exploitent la curiosité (« Résultats évaluation annuelle 2025 ») ou l'intérêt professionnel (« Invitation keynote — Congrès Aéronautique Lyon ») ont des taux d'ouverture supérieurs.

**Le corps.** Le corps doit être cohérent avec l'expéditeur et l'objet, utiliser la terminologie de l'entreprise cible, et inclure un appel à l'action clair mais non agressif. Les erreurs de langue, autrefois marqueur fiable de phishing, sont en voie de disparition grâce aux LLM qui génèrent des textes grammaticalement parfaits et stylistiquement adaptés au contexte culturel.

**Le lien ou la pièce jointe.** C'est le vecteur technique : URL vers une landing page de collecte d'identifiants, document piégé (macro Office, fichier HTA, fichier ISO/IMG contenant un exécutable), QR code redirigeant vers un site malveillant, ou pièce jointe légitime (document PDF inoffensif) dans une reply-chain attack où le vrai piège est l'établissement de la confiance pour une demande ultérieure (BEC).

**La landing page.** Pour le credential harvesting, la landing page reproduit l'interface de connexion de la cible (Microsoft 365, Google Workspace, VPN d'entreprise, portail RH). Les kits de phishing modernes reproduisent ces interfaces pixel par pixel, y compris les certificats TLS (Let's Encrypt fournit des certificats gratuits — le cadenas vert ne garantit plus rien). Les techniques de reverse proxy (Evilginx, Modlishka) capturent non seulement les identifiants mais aussi les tokens de session, contournant ainsi le MFA classique (voir Ch.10 pour le détail).

## 6.2 Niveaux de sophistication

Le phishing n'est pas une technique unique — c'est un spectre de sophistication dont chaque niveau a ses techniques, ses cibles et ses contre-mesures.

**Le phishing de masse (spray & pray).** Campagnes non ciblées envoyées à des dizaines de milliers d'adresses. Faible taux de réussite individuel (1-3 %), mais rentable par le volume. Les leurres sont génériques : notification de livraison, facture impayée, mise à jour de sécurité bancaire. Contre-mesures : filtrage email, sensibilisation de base, DMARC strict.

**Le spear-phishing.** Campagnes ciblées sur un groupe restreint (une entreprise, un service, un groupe de projet). Les leurres sont personnalisés : terminologie interne, noms de projets, références aux supérieurs hiérarchiques. Taux de réussite significativement supérieur (15-40 % selon la qualité de la personnalisation). Contre-mesures : filtrage avancé avec analyse comportementale, sensibilisation ciblée, bannières « email externe », simulation de phishing régulière.

**Le BEC/whaling.** Attaques ciblées de haute valeur (dirigeants, DAF, comptabilité). Pas de malware, pas de lien malveillant — pure manipulation par email. L'attaquant usurpe l'identité d'un dirigeant, d'un avocat ou d'un fournisseur pour obtenir un virement ou une information sensible. Taux de réussite variable mais impact unitaire très élevé (dizaines de milliers à dizaines de millions d'euros par incident). Contre-mesures : processus de double validation pour les virements, callback sur numéro connu, culture de la vérification. Le BEC est traité en détail au Ch.9.

## 6.3 Construction d'un lure crédible

La crédibilité d'un lure de phishing repose sur quatre piliers : le contexte, le timing, la personnalisation et l'urgence calibrée.

**Le contexte.** Le meilleur lure s'inscrit dans un contexte que la cible attend ou connaît. Si l'entreprise est en pleine migration vers Microsoft 365, un email sur la mise à jour des identifiants sera perçu comme normal. Si une conférence sectorielle approche, une invitation de dernière minute sera crédible. La reconnaissance OSINT (Ch.5) fournit ces contextes.

**Le timing.** Le lundi matin (accumulation d'emails du week-end, traitement rapide), le vendredi après-midi (fatigue, volonté de conclure la semaine), la veille de vacances (stress de dernière minute, départs précipités), la période de clôture comptable (pression, urgence des validations) sont des fenêtres de vulnérabilité documentées.

**La personnalisation.** L'utilisation du nom du destinataire, de son service, de son manager, d'un projet sur lequel il travaille, d'un événement récent (formation, séminaire, réorganisation) augmente la crédibilité de manière exponentielle. Un email qui mentionne « suite à votre réunion avec Frédéric Morin hier » est perçu comme interne avant même d'être analysé.

**L'urgence calibrée.** L'urgence doit être suffisante pour déclencher une action rapide mais insuffisante pour paraître suspecte. « Veuillez valider avant fin de journée » est plus efficace que « URGENT — action immédiate requise !!!». L'urgence fonctionne en réduisant le temps disponible pour la réflexion et la vérification.

## 6.4 L'infrastructure de phishing

La construction d'une infrastructure de phishing crédible est un savoir-faire technique qui évolue rapidement.

**Domaines lookalike et typosquatting.** L'enregistrement de domaines similaires à celui de la cible (heIios-aero.fr, helios-aero.com, helios-aeronautique.fr) permet de créer des adresses email et des URLs visuellement proches de l'original. Les domaines internationalisés (IDN — utilisant des caractères Unicode visuellement identiques aux caractères ASCII) ajoutent une couche de sophistication. Contre-mesure : surveillance proactive des enregistrements de domaines similaires, DMARC en mode « reject ».

**Compromission d'email légitime (reply-chain attack).** L'attaquant compromet une boîte mail réelle (par phishing préalable, credential stuffing ou achat sur le darkweb) et s'insère dans un fil de conversation existant. Cette technique est extrêmement difficile à détecter car l'email provient d'une adresse légitime, dans un fil de conversation légitime, avec un historique de conversation réel.

**Contournement de SPF/DKIM/DMARC.** SPF vérifie que le serveur d'envoi est autorisé par le domaine. DKIM signe cryptographiquement l'email. DMARC combine les deux et définit une politique de rejet. En configuration stricte (DMARC p=reject), ces protocoles bloquent le spoofing direct du domaine. Mais ils ne protègent pas contre le typosquatting, les domaines lookalike, le compromission d'email légitime ou le display name spoofing. La protection email est une défense en profondeur, pas une solution unique.

## 6.5 Red team phishing vs attaquant réel

Le red teamer et l'attaquant réel utilisent les mêmes techniques — mais dans un cadre radicalement différent. Le red teamer documente chaque étape (emails envoyés, taux de clic, identifiants collectés, temps avant signalement), ne compromet pas réellement les systèmes (les identifiants collectés sont stockés de manière sécurisée et jamais exploités), produit un rapport factuel et constructif, et forme les employés sur les mécanismes exploités. L'attaquant réel exploite immédiatement les identifiants collectés, latéralise dans le réseau, exfiltre des données et peut persister pendant des mois. Cette différence de finalité est fondamentale, mais les techniques sont identiques — ce qui permet au red team d'évaluer la vulnérabilité réelle de l'organisation.

---
