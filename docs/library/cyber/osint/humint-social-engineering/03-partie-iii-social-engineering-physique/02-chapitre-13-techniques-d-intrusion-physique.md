---
title: Chapitre 13 — Techniques d'intrusion physique
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie III — Social engineering physique
  - index.md
---

## 13.1 Le tailgating et le piggybacking

Le tailgating (suivre un employé à travers une porte contrôlée) est la technique d'intrusion physique la plus simple et statistiquement la plus efficace. Les gens tiennent la porte par politesse — c'est une norme sociale profondément ancrée que même les programmes de sensibilisation les plus rigoureux peinent à modifier.

La technique est élémentaire : attendre qu'un employé badge et ouvre une porte, puis le suivre en maintenant un flux naturel. Le succès dépend du timing (arriver juste derrière, pas trop loin pour ne pas être remarqué), du comportement (confiant, pressé, naturel — ne pas hésiter, ne pas regarder autour de soi de manière suspecte), et de l'apparence (tenue cohérente avec l'environnement).

Le piggybacking est une variante où le red teamer engage activement la conversation avec l'employé pendant l'approche de la porte, créant un lien social qui rend le refus d'accès encore plus improbable (« après vous — vous avez vu, ils ont encore changé le code du parking ! »).

**Contre-mesures** : tourniquets unitaires (sas qui ne laissent passer qu'une personne par badge), portiques de sécurité avec détection anti-passback, sensibilisation ciblée du personnel (autorisation de refuser poliment — « désolé, c'est la procédure, chacun doit badger »), culture où la vérification n'est pas perçue comme impolie.

## 13.2 L'impersonation

L'impersonation — se faire passer pour quelqu'un d'autre — est le cœur du social engineering physique. La crédibilité du pretexte est tout. Les pretextes les plus efficaces exploitent des rôles qui ont un accès légitime aux locaux et qui ne sont pas questionnés.

**Le prestataire IT.** Après identification du prestataire par OSINT, le red teamer se présente comme un technicien de ce prestataire pour une intervention planifiée ou d'urgence. Crédibilité renforcée par : un polo ou un gilet aux couleurs du prestataire (imprimé pour l'occasion), un faux bon d'intervention, le name-dropping du responsable IT interne et du responsable de compte chez le prestataire.

**L'inspecteur.** Inspecteur incendie, inspecteur sanitaire, auditeur qualité, contrôleur réglementaire — ces rôles confèrent une autorité qui réduit les questions. L'inspecteur est attendu, ou il arrive par surprise — dans les deux cas, il est rarement refusé.

**L'employé d'un autre site.** Dans les organisations multi-sites, les employés ne connaissent pas personnellement les collègues des autres sites. « Je suis Thomas du bureau de Paris, je suis venu pour la réunion avec Jean-Marc Duval — je ne retrouve pas la salle de réunion 3B » est un pretexte simple et efficace.

**Le visiteur.** Un faux rendez-vous avec un responsable identifié par OSINT, annoncé la veille par un appel de « l'assistante » (complice) au standard. Si le rendez-vous est enregistré dans le système de gestion des visiteurs, le red teamer reçoit un badge visiteur légitime.

## 13.3 La manipulation des gardiens et réceptionnistes

Les gardiens et réceptionnistes sont la première ligne de défense physique — et souvent la plus vulnérable. Ils sont formés à l'accueil et à la courtoisie, rarement au contre-social engineering.

Les techniques de manipulation incluent : le **name-dropping** (« je viens voir Frédéric Morin, on a un rendez-vous à 14h »), la **création d'urgence** (« mon technicien est déjà à l'intérieur, il m'attend dans le local serveur — c'est urgent, on a une panne de production »), l'**appel de confirmation** (un complice appelle le standard pendant que le red teamer est à l'accueil et confirme sa venue : « oui, c'est le technicien qu'on attend, faites-le monter »), et la **sympathie** (« je suis vraiment désolé de vous embêter, j'ai un problème de badge, ça fait 20 minutes que je suis bloqué dehors — vous pouvez m'ouvrir le temps que l'IT me refasse un badge ? »).

## 13.4 L'exploitation des badges

Le clonage de badges RFID est une technique de red team courante dont la faisabilité dépend fortement de la technologie utilisée.

**RFID basse fréquence (125 kHz)** — HID ProxCard, EM4100 : facilement clonable avec un Proxmark3, un Flipper Zero ou même des lecteurs/graveurs basiques disponibles en ligne. La lecture peut se faire à distance de quelques centimètres (suffisant pour lire un badge dans la poche d'un employé qui passe près de vous) et la copie sur un badge vierge prend quelques secondes.

**RFID haute fréquence (13.56 MHz)** — MIFARE Classic, MIFARE DESFire, iCLASS : plus résistant au clonage. MIFARE Classic a des faiblesses cryptographiques connues qui permettent le clonage avec un Proxmark3, mais les versions plus récentes (DESFire EV2/EV3) utilisent un chiffrement robuste. iCLASS Standard est également vulnérable, mais iCLASS SE est significativement plus résistant.

**NFC mobile et badges virtuels** — Apple Wallet, Google Wallet : difficiles à cloner car protégés par la cryptographie du smartphone. C'est l'une des raisons de la migration progressive vers les badges mobiles dans les entreprises à sécurité renforcée.

La défense contre le clonage passe par la migration vers des technologies résistantes (DESFire EV2+, badges mobiles), la combinaison badge + biométrie pour les zones sensibles, la détection des anomalies d'accès (même badge utilisé à deux endroits simultanément, accès à des heures inhabituelles) et l'audit régulier du parc de badges.

## 13.5 Le non-verbal et la crédibilité comportementale

En social engineering physique, le corps et le comportement comptent autant que le scénario. Un pretexte parfait sera ruiné par un comportement hésitant, un regard fuyant ou une posture qui trahit le stress.

**La proxémie.** La gestion de la distance interpersonnelle est culturellement déterminée, mais en contexte professionnel français, une distance de 80 cm à 1,2 m est la norme pour une interaction professionnelle. Trop proche : inconfort et suspicion. Trop loin : désengagement et manque de crédibilité.

**La posture.** Dos droit, épaules ouvertes, démarche assurée, regard droit. Le red teamer qui se déplace comme s'il connaissait les lieux ne sera pas questionné. Celui qui hésite à un croisement, regarde les plaques de porte, ou consulte son téléphone avec l'air perdu sera immédiatement repéré par un gardien attentif.

**Le tempo.** La vitesse de déplacement doit être cohérente avec le pretexte. Un « technicien en intervention urgente » se déplace vite et avec détermination. Un « auditeur en visite » se déplace calmement et observe. Un « employé qui va au café » est décontracté.

**La gestion du regard.** Contact visuel bref et naturel avec les personnes croisées (ni évitement ni insistance). Un hochement de tête accompagné d'un « bonjour » suffit à créer un micro-rapport qui désarme la suspicion.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 4**
>
> **Intrusion physique — Site de Bordeaux.** Nathan se présente à l'entrée du site de production de Bordeaux le mardi à 10h30. Tenue : polo gris avec logo brodé de « NetServ Solutions » (le prestataire de maintenance informatique identifié par OSINT — le polo a été imprimé la veille). Badge visiteur visuellement crédible (format Helios, photo de Nathan, nom « T. Beaumont — NetServ Solutions »). Clipboard avec un faux bon d'intervention mentionnant « vérification connectique baie serveur B2 — ref. ticket #NS-2025-0847 ».
>
> Le gardien, Jean-Pierre, vérifie la liste des interventions planifiées. Nathan n'y figure pas. « C'est bizarre, j'ai le ticket ici, c'est Jean-Marc Duval qui l'a ouvert vendredi. Il y a un switch qui pose problème dans la baie B2 depuis la semaine dernière. » Jean-Pierre hésite. Nathan sort son téléphone : « Attendez, je vais appeler mon responsable de compte. » Il appelle Thomas (son complice), qui répond : « Oui, c'est l'intervention NT-0847 pour Helios Bordeaux, technicien Beaumont. C'est bien planifié chez nous, peut-être un oubli de validation côté client. » Jean-Pierre consulte son écran une dernière fois, puis : « Allez-y, vous connaissez le chemin vers le local serveur ? — Oui, bâtiment B, au fond à droite. Merci Jean-Pierre. »
>
> En 45 minutes, Nathan connecte un implant réseau (Raspberry Pi configuré comme rogue access point) dans la baie serveur, prend des photos de trois salles de réunion (post-its sur les écrans avec mots de passe WiFi et codes de salle visioconférence), et photographie le tableau d'affichage du couloir RH (planning des absences, organigramme du site, numéros de téléphone internes).

---
