---
title: Chapitre 8 — Espaces relationnels et médiatiques
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie II — Les entités de l'écosystème
  - index.md
---

## 8.1 Forums underground comme institutions sociales

Les forums underground ne sont pas de simples « marchés noirs en ligne ». Ce sont des institutions sociales complexes qui remplissent simultanément plusieurs fonctions essentielles au fonctionnement de l'écosystème.

**Fonction de marché.** Les forums abritent des sections dédiées à la vente de services (accès, malware, hébergement, carding, blanchiment), avec des annonces structurées, des prix, et des conditions de vente. Les transactions se font généralement en Bitcoin ou Monero, souvent via un système d'escrow intégré au forum (voir Ch.19).

**Fonction de réputation.** Chaque utilisateur accumule un historique visible : nombre de transactions, ratings des acheteurs et vendeurs, ancienneté du compte, contributions à la communauté (tutoriels, outils partagés). Ce capital réputationnel est le bien le plus précieux d'un acteur sur le forum — il est le garant de la confiance dans un environnement sans recours légal.

**Fonction de recrutement.** Les acteurs compétents se font remarquer par la qualité de leurs contributions et sont approchés directement (via messages privés ou via des canaux de communication off-forum comme Tox, Jabber/XMPP, ou Telegram) pour des opérations spécifiques.

**Fonction de gouvernance.** Les admins et modérateurs du forum fixent et appliquent les règles : interdiction de certaines activités (la plupart des forums russophones interdisent la vente de données de victimes russes), résolution des litiges commerciaux (l'admin ou un arbitre désigné tranche les conflits entre vendeur et acheteur), et sanctions (bannissement, exposition publique du scammer).

Les forums les plus significatifs historiquement et actuellement pour l'écosystème cybercriminel incluent XSS et Exploit (forums russophones majeurs, accès sur vouching ou paiement), RAMP (forum russophone plus récent, notable pour avoir hébergé des discussions RaaS après le bannissement de LockBit d'XSS et Exploit), BreachForums (forum anglophone centré sur les données, successeur de RaidForums après sa saisie en 2022, lui-même ayant connu des turbulences avec l'arrestation de son admin « Baphomet » en 2024 et des relances successives), et Cracked/Nulled (forums anglophone de niveau inférieur, plus accessibles mais moins réputés). Le paysage des forums évolue constamment — les saisies, les exit scams des administrateurs, et les migrations sont fréquentes.

## 8.2 Canaux Telegram et Discord

Telegram est devenu le moyen de communication privilégié des écosystèmes cybercriminels, supplantant largement les messageries plus anciennes comme Jabber/XMPP et Tox pour les communications semi-publiques.

**Canaux publics** : ils servent de vitrine — un IAB y publie ses nouvelles offres, un opérateur RaaS y annonce ses mises à jour, un vendeur de logs y partage des échantillons gratuits pour attirer des clients. Ces canaux sont facilement observables par les analystes CTI.

**Groupes privés** : accessibles sur invitation ou après vérification, ils servent d'espace opérationnel — coordination entre affiliés, partage d'outils, discussion technique, échange d'intelligence sur les cibles. L'accès à ces groupes est beaucoup plus difficile pour l'analyste sans franchir les limites légales (pas d'interaction active ni de fausse identité).

L'identification des administrateurs de canaux Telegram est une technique OSINT essentielle. Les outils automatisés (comme TGStat pour les statistiques de canaux, ou l'API Telegram elle-même pour les metadata publiques) peuvent révéler des informations sur la création du canal, les patterns de publication, et parfois les liens entre différents canaux administrés par la même personne. La prudence s'impose toutefois : Telegram a durci ses politiques de coopération avec les forces de l'ordre en 2024-2025 suite à l'arrestation de son fondateur Pavel Durov en France en août 2024, mais les métadonnées publiques restent accessibles.

Discord est moins utilisé que Telegram pour la cybercriminalité « sérieuse » mais reste un espace actif pour les communautés de script kiddies, les marchés de carding de bas niveau, et les discussions techniques informelles.

## 8.3 Leak sites et sites de revendication

Les leak sites sont les plateformes sur lesquelles les opérateurs de ransomware publient les données des victimes qui refusent de payer la rançon. Ces sites, généralement hébergés sur le réseau Tor, remplissent une double fonction de pression directe sur la victime actuelle et de démonstration de capacité pour les victimes futures.

L'analyse des leak sites est une source d'intelligence précieuse. Elle révèle les cibles d'un opérateur (secteurs, pays, tailles d'entreprise), la fréquence des attaques (indicateur de l'activité et du nombre d'affiliés), le volume de données exfiltrées (indicateur de la sophistication de l'opération), les délais entre compromission et publication (indicateur du processus de négociation), et les patterns saisonniers ou géographiques.

Les leak sites sont aussi des espaces de communication stratégique. Les opérateurs y publient des « communiqués de presse » sur leurs nouvelles versions, des réfutations quand les forces de l'ordre annoncent des disruptions, et parfois des messages menaçants envers les chercheurs en sécurité qui les analysent.

## 8.4 Médias de façade et relais d'influence

Certains écosystèmes — notamment les écosystèmes para-étatiques — utilisent des médias de façade pour amplifier leurs opérations. Un blog « journalistique » qui publie un « article d'investigation » sur une entreprise victime de ransomware, en réalité rédigé par les attaquants eux-mêmes ou leurs relais, sert à maximiser la pression médiatique et réputationnelle.

Ces médias de façade sont identifiables par des indicateurs OSINT classiques : domaine récent, pas d'historique de publication avant l'événement, pas d'identité vérifiable des « journalistes », hébergement sur des infrastructures liées à l'écosystème criminel, et contenu aligné exclusivement avec les intérêts de l'attaquant.

La convergence entre cyber-attaque et opération d'influence est une tendance majeure de 2024-2026. Les groupes para-étatiques (et certains groupes purement criminels qui ont compris l'intérêt de la pression médiatique) orchestrent leurs attaques en combinant l'intrusion technique, l'exfiltration de données, la publication sur le leak site, et l'amplification via des canaux Telegram et des médias de façade — dans une séquence coordonnée qui maximise l'impact.

## 8.5 Fil rouge — NEXUS : la dimension informationnelle

> **🔍 NEXUS — Épisode 8**
>
> Le leak site de PhantomCrypt publie une revendication 72 heures après la détection du sample. Le site liste Énergis comme victime avec un compte à rebours de 10 jours et un extrait de données volées (des schémas d'architecture réseau et des documents internes marqués « Confidentiel Entreprise »). Cela signifie que le chiffrement a été bloqué par l'EDR, mais l'exfiltration a peut-être partiellement réussi avant la détection.
>
> Simultanément, le canal Telegram de PhantomCrypt relaie la publication avec un commentaire : « French energy giant — critical infrastructure — premium data. » Le message est repris par 3 autres canaux d'agrégation de leaks en 24 heures.
>
> Plus troublant : le blog `phantom-news[.]press` (identifié sur la même IP que le C2) publie un article en anglais, présenté comme du « journalisme d'investigation », titré « Major French Energy Provider Fails to Protect Critical Infrastructure ». L'article cite des « sources anonymes » et mentionne des détails techniques que seuls les attaquants peuvent connaître. L'article est partagé sur X/Twitter par des comptes qui semblent automatisés.
>
> Samira note : l'écosystème a une dimension informationnelle coordonnée. Le leak site, le canal Telegram, et le blog de façade fonctionnent en séquence pour maximiser la pression. C'est inhabituel pour un affilié RaaS purement opportuniste — les affiliés classiques se contentent du leak site et de la négociation directe. La coordination médiatique suggère soit un affilié sophistiqué, soit une dimension para-étatique.

---
