---
title: PARTIE V — CONFINEMENT, DÉCISION ET PRÉSERVATION DE PREUVE
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 6
chapters: 9
---

*L'étendue de la compromission est estimée. Il faut contenir l'attaquant, préserver les preuves, et prendre des décisions critiques — souvent avec des informations incomplètes.*

---

### Chapitre 23 — Stratégies de confinement et arbitrages

#### 23.1 Le dilemme fondamental

Contenir **trop tôt** alerte l'attaquant. S'il détecte que ses connexions C2 sont coupées ou que ses comptes sont désactivés, il peut réagir de manière destructrice : accélérer le chiffrement, activer un wiper, supprimer les logs, ou activer un mécanisme de persistance de secours. Contenir **trop tard** lui laisse le temps d'aggraver les dégâts : chiffrer davantage de systèmes, exfiltrer davantage de données, s'enraciner plus profondément.

Le timing optimal dépend du type d'attaque. **Ransomware en cours de déploiement** : confinement immédiat — chaque minute de retard signifie des dizaines de machines chiffrées en plus. La course contre le chiffrement est réelle. **Espionnage discret** : observation contrôlée possible — si l'attaquant ne sait pas qu'il est détecté, continuer à l'observer permet de comprendre l'étendue complète de la compromission avant de le couper. **Compromission de compte sans activité destructrice** : désactivation immédiate du compte — l'impact est limité et la mesure est réversible.

#### 23.2 Confinement réseau

Les options de confinement réseau, de la plus chirurgicale à la plus radicale : isolation de machines spécifiques via EDR (network containment — la machine reste allumée mais ne peut plus communiquer, sauf avec la console EDR), isolation de segments via ACL pare-feu ou VLAN (couper les flux entre segments compromis et segments sains), coupure de l'accès Internet ciblée (bloquer les communications C2 sans couper toute la production), coupure de l'accès Internet totale (couper toutes les communications externes — radical mais efficace contre les ransomwares qui utilisent un C2 pour le chiffrement), et isolation inter-sites (couper les liens WAN entre sites pour empêcher la propagation d'un site compromis vers les autres).

Chaque option a un impact business mesurable. L'isolation d'un segment serveur arrête les services hébergés. La coupure Internet arrête les emails, le VPN, les services cloud, et potentiellement les systèmes de paiement. L'isolation inter-sites empêche la collaboration entre sites. Ces impacts doivent être évalués AVANT la décision, en concertation avec les métiers.

#### 23.3 Confinement des comptes

Désactivation des comptes compromis (identifiés par l'investigation), reset des mots de passe des comptes à privilèges (la question du timing : quand fait-on le reset massif ?), révocation des sessions et tokens (M365, VPN, SSO, OAuth), rotation des secrets de service (mots de passe des comptes de service, clés API, certificates), et désactivation des accès tiers (VPN prestataires, interconnexions partenaires).

Le risque de lock-out massif : un reset de tous les mots de passe du domaine un samedi matin bloquera les 12 000 utilisateurs lundi matin s'il n'est pas coordonné avec une communication claire et un mécanisme de reset autonome (portail de self-service, assistance téléphonique renforcée).

#### 23.4 Fil rouge — BLACKTIDE : la décision de confinement

> **🔍 BLACKTIDE — Épisode 23**
>
> Samedi 15 mars, 01h30. Le ransomware est en cours de déploiement. Nadia présente 3 options à la cellule de crise technique (Marc/RSSI valide).
>
> | Option | Action | Impact business | Risque sécurité |
> |--------|--------|----------------|----------------|
> | A — Chirurgical | Isoler les 3 DC + 40 machines identifiées via EDR | Production maintenue sauf serveurs de fichiers | Élevé — des machines compromises non identifiées restent actives |
> | B — Sites touchés | Coupure Internet + isolation inter-sites pour Fos, Lyon, Cologne | Production arrêtée sur 3 sites (40 % de la capacité) | Modéré — le confinement couvre le périmètre connu |
> | C — Total | Coupure réseau complète d'Arvantis | Production arrêtée partout (800 K€/jour) | Faible — tout est coupé |
>
> **Décision : Option B.** Les 3 sites touchés sont isolés (coupure Internet, isolation WAN inter-sites). Les 12 autres sites maintiennent leur activité avec surveillance renforcée et blocage des flux venant des 3 sites isolés. Le site OIV de Fos est isolé en priorité. La production est arrêtée sur les 3 sites impactés.

---

### Chapitre 24 — Confinement par type d'incident

Ce chapitre détaille les stratégies de confinement spécifiques aux types d'incidents les plus courants.

**Ransomware :** confinement réseau immédiat des segments touchés (priorité absolue), isolation du C2 (blocage du domaine/IP au pare-feu), protection immédiate des sauvegardes (déconnexion physique du NAS si sur le même réseau), vérification de l'intégrité des sauvegardes offline. Ne PAS éteindre les machines avant collecte forensic (la RAM contient des preuves critiques).

**Compromission de compte / BEC :** désactivation du compte, reset du mot de passe, révocation de toutes les sessions actives, vérification des règles de forwarding email, notification aux contacts qui ont pu recevoir des emails frauduleux.

**Exfiltration / espionnage :** bloquer le canal d'exfiltration identifié (mais attention : l'attaquant peut avoir plusieurs canaux), évaluer si l'observation contrôlée est préférable au confinement immédiat (pour comprendre l'étendue avant de couper).

**OT :** confinement de l'interface IT/OT (coupure des passerelles de supervision, isolation du réseau OT via le pare-feu IT/OT), vérification de l'intégrité des configurations d'automates avec les ingénieurs de production. Ne JAMAIS redémarrer un automate sans validation des ingénieurs — un automate dans un état intermédiaire peut causer un accident physique.

**Supply chain :** isolation immédiate du lien avec le tiers compromis (désactivation VPN, blocage des flux réseau, révocation des API keys), notification du fournisseur.

---

### Chapitre 25 — Préserver les preuves sous pression

#### 25.1 L'ordre de volatilité

La collecte de preuves doit suivre l'ordre de volatilité — du plus éphémère au plus durable. La **mémoire vive** s'efface à l'extinction (collecte en 10-20 minutes avec DumpIt). L'**état des processus et connexions réseau** est dynamique (capture via EDR ou ligne de commande). Les **fichiers temporaires et artefacts système** persistent jusqu'à écrasement. Les **logs** persistent jusqu'à rotation (jours à mois). Les **disques** persistent indéfiniment (sauf chiffrement par le ransomware).

Le principe fondamental : collecter AVANT ou PENDANT le confinement, pas après. Le confinement peut impliquer l'extinction de machines (perte de RAM), la modification de configurations réseau (perte de l'état réseau), ou la restauration de systèmes (écrasement des artefacts).

#### 25.2 Chaîne de custody

Chaque acquisition est documentée avec un formulaire de chaîne de custody (template en Annexe C) : identifiant unique de la preuve, description (machine, type d'acquisition), analyste responsable, date et heure de l'acquisition, outil et version utilisés, hash SHA256 de l'image ou du fichier, lieu de stockage, et journal des accès ultérieurs.

#### 25.3 Les erreurs qui détruisent les preuves

Redémarrer un serveur compromis sans collecte mémoire préalable (RAM perdue — irréversible). Lancer un scan antivirus qui supprime ou met en quarantaine le malware (sample perdu — le hash est peut-être préservé dans les logs, mais le binaire est détruit). Restaurer un système depuis une sauvegarde avant acquisition forensic (tous les artefacts écrasés). Modifier des configurations réseau avant capture de l'état (connexions actives perdues). Ne pas documenter les actions prises (impossible de reconstituer la séquence pour le retex ou la procédure judiciaire).

Chacune de ces erreurs est commise régulièrement par des administrateurs IT qui agissent de bonne foi mais sans formation IR. La formation des IT à « ne pas toucher avant le forensic » est un investissement de préparation critique (Ch.5).

#### 25.4 Fil rouge — BLACKTIDE : la preuve perdue

> **🔍 BLACKTIDE — Épisode 25**
>
> Deux serveurs de fichiers (FS01-Lyon et FS01-Fos) ont été redémarrés par David (admin astreinte) à 23h30, avant l'arrivée du PRIS. Nadia documente factuellement : « Serveurs redémarrés sans collecte préalable — cause : absence de procédure. Conséquence : perte de la RAM et des artefacts de session. » Elle note dans ses recommandations RETEX : « Former les admins d'astreinte au premier réflexe IR : NE PAS redémarrer, APPELER l'IR lead. »

---

### Chapitre 26 — Décider sous incertitude

#### 26.1 La réalité de la prise de décision en IR

L'IR n'est pas seulement collecter, analyser, contenir. C'est **décider** — et décider avec des informations incomplètes, des contraintes métiers contradictoires, des coûts immédiats, des conséquences juridiques potentielles, et un stress intense.

À aucun moment de l'incident l'équipe IR ne dispose de « toutes les informations ». Le scoping est toujours approximatif. L'étendue de la compromission est toujours sous-estimée dans les premières heures. Le volume de données exfiltrées n'est jamais connu avec précision tant que l'investigation n'est pas terminée — et l'investigation prend des jours.

La discipline de décision consiste à expliciter ce qu'on sait, ce qu'on ne sait pas, et ce qu'on suppose, puis à décider en connaissance de cause de cette incertitude — pas à attendre la certitude qui ne viendra pas.

#### 26.2 Arbitrage sécurité vs production

La sécurité veut isoler le réseau (pour contenir). La production veut maintenir le réseau (pour ne pas arrêter les usines). Les deux ont raison dans leur logique. L'arbitrage est une décision de direction, pas une décision technique — mais la direction a besoin de données claires pour décider.

L'IR lead doit formuler des **options** (pas une recommandation unique), avec pour chaque option : l'impact sécurité (quel risque accepte-t-on ?), l'impact business (quel coût subit-on ?), les conséquences (que se passe-t-il si l'option se révèle insuffisante ?), et la réversibilité (peut-on revenir en arrière ?).

#### 26.3 Erreurs réversibles vs irréversibles

Un principe directeur en situation d'incertitude : **privilégier les actions réversibles**. Isoler un serveur via EDR est réversible (on peut lever l'isolation en un clic). Éteindre un serveur sans collecte mémoire est irréversible (la RAM est perdue pour toujours). Restaurer un système depuis une sauvegarde est irréversible (les artefacts forensic sont écrasés). Communiquer publiquement est irréversible (on ne peut pas « dé-communiquer »). Payer une rançon est irréversible (l'argent est parti).

Quand deux options offrent un niveau de sécurité comparable, choisir la plus réversible.

#### 26.4 Documentation des décisions

Chaque décision significative est documentée dans le journal d'incident : qui a décidé, quand, sur la base de quelles informations (y compris les incertitudes), quelles alternatives ont été considérées, et pourquoi cette option a été retenue. Cette documentation protège les décideurs (ils ont agi raisonnablement avec les informations disponibles), alimente le retex (quelles informations manquaient pour mieux décider ?), et sert de preuve de bonne foi en cas de contentieux.

#### 26.5 Comment formuler des options à la direction

La direction ne veut pas un briefing technique de 30 minutes. Elle veut 3 options, chacune sur une ligne, avec : ce qu'on fait, ce que ça coûte en arrêt de production, ce que ça risque en termes de sécurité, et le délai de reprise estimé. Un tableau situation/options/risques/recommandation sur une page, avec un niveau de confiance explicite, est le format le plus efficace.

#### 26.6 Fil rouge — BLACKTIDE : les arbitrages du COMEX

> **🔍 BLACKTIDE — Épisode 26**
>
> Samedi 10h00. Réunion de la cellule de crise exécutive. Le CEO, Pierre Gautier, pose la question directe : « On redémarre quand ? »
>
> Marc (RSSI) présente le tableau des options de reprise (voir Ch.3, épisode BLACKTIDE). Le CEO choisit l'option B (reprise contrôlée, J+5 à J+12). La décision est documentée dans le PV de la réunion de crise, avec les réserves du RSSI (« le risque résiduel de l'option B n'est pas nul — nous recommandons un threat hunting post-reprise de 4 semaines ») et la signature du CEO.
>
> Deuxième arbitrage : la demande de rançon de 4,2 M€ arrivée à 09h00 via le portail de négociation PhantomCrypt. Le RSSI recommande de ne pas payer (les sauvegardes offline sont intactes, la production peut reprendre sans les données chiffrées). Le directeur juridique confirme qu'il n'y a pas d'obligation de payer, et que le paiement pourrait exposer Arvantis à des risques si l'opérateur est sanctionné par l'OFAC. Le CEO valide : pas de paiement. Décision documentée.

---
