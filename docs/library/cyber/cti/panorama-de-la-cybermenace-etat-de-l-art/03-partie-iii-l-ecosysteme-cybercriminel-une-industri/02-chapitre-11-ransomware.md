---
title: Chapitre 11 — Ransomware
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - 'PARTIE III — L''écosystème cybercriminel : une industrie de la menace'
  - index.md
---

anatomie d'une menace persistante et fragmentée

## 11.1 — État des lieux 2025

Le ransomware reste la menace cybercriminelle la plus directement impactante. L'ENISA documente que 81,1% des activités cybercriminelles ciblant les organisations EU impliquent du ransomware. Le FBI IC3 rapporte que le secteur healthcare/public health a reçu le plus de signalements ransomware (460 incidents), suivi des services financiers critiques (258) et de l'industrie manufacturière (189).

Le paysage est devenu plus fragmenté et compétitif. Là où LockBit dominait avec près d'un quart de toutes les revendications en 2023-2024, l'écosystème 2025 est plus éclaté : **Akira** est le variant le plus fréquemment déployé contre l'UE (11,6%), suivi de **SafePay** (10,1%) et **Qilin** (7,5%). LockBit, après la compromission de son panel d'affiliation en mai 2025 et la fuite de sa base de données interne, semble avoir cessé ses activités — remplacé par un opérateur appelé Syrphid utilisant LockBit4. BlackBasta a cessé de revendiquer des incidents depuis janvier 2025. 8Base a vu ses déploiements diminuer après des fuites d'infrastructure et des arrestations d'administrateurs.

**DragonForce** émerge comme un cas d'étude de la dynamique compétitive : engagé dans une « guerre de territoire » contre d'autres groupes ransomware, DragonForce a ciblé 19 organisations EU depuis le lancement de sa plateforme RaaS en juin 2024.

## 11.2 — Le modèle RaaS : économie des affiliés

Le modèle Ransomware-as-a-Service reste le modèle économique dominant. Un groupe central (core team) développe le ransomware, maintient l'infrastructure (portail de négociation, site de leak) et recrute des affiliés. Les affiliés mènent les attaques et partagent les revenus avec le core team — typiquement 75% pour l'affilié, 25% pour le développeur.

L'ENISA observe un phénomène de recomposition post-disruption : les affiliés des groupes démantelés migrent vers d'autres programmes ou créent leurs propres variants. Le CSE canadien évalue que « dans les deux prochaines années, l'écosystème ransomware deviendra presque certainement de plus en plus fragmenté. Les affiliés commenceront presque certainement à agir indépendamment et à créer leurs propres variants pour réduire leur vulnérabilité aux disruptions des forces de l'ordre. »

## 11.3 — La chaîne d'attaque complète

La chaîne d'attaque ransomware typique en 2025 suit un modèle multi-acteurs. Un infostealer (Lumma, RedLine, Vidar) collecte des credentials sur un poste utilisateur via malvertising ou logiciel craqué. Les credentials sont vendues sur un forum par un IAB. Un affilié ransomware achète l'accès, se connecte via VPN ou RDP, conduit une reconnaissance interne, se latéralise vers les systèmes critiques, exfiltre les données sensibles (pour l'extorsion double), puis déploie le ransomware. Microsoft documente cette chaîne dans son flux d'infostealer, montrant comment une infection par un infostealer se transforme en accès réseau complet en quelques étapes.

Le **délai entre compromission initiale et déploiement du ransomware** s'est raccourci. Historiquement mesuré en semaines ou mois, il peut désormais être de quelques jours — le temps pour l'affilié de conduire sa reconnaissance et d'identifier les actifs de valeur.

## 11.4 — L'évolution des techniques d'extorsion

Les techniques d'extorsion se sont considérablement sophistiquées. La **double extorsion** (chiffrement + menace de publication des données) est devenue standard. La **triple extorsion** ajoute des attaques DDoS comme pression supplémentaire. Certains groupes pratiquent la **quadruple extorsion** : chiffrement, leak, DDoS, et contact direct des clients/partenaires de la victime.

Le CSE documente des innovations coercitives croissantes : publication de comptes à rebours sur les sites de leak, appels téléphoniques directs aux victimes et à leurs clients, critique publique des organisations victimes pour endommager leur réputation, encouragement des clients des victimes à engager des poursuites judiciaires, et exploitation de nouvelles réglementations de notification d'incidents — un groupe ALPHV a déposé une plainte auprès de la SEC américaine contre sa propre victime pour défaut de signalement de l'incident.

## 11.5 — Statistiques croisées

Les données quantitatives croisées donnent une image plus complète. Le FBI IC3 rapporte 20,877 milliards de dollars de pertes totales liées au cybercrime en 2025, avec le ransomware et les data breaches représentant une part significative des plaintes liées aux infrastructures critiques. L'ENISA documente 82 variants de ransomware déployées contre l'UE. L'ANSSI rapporte avoir traité de multiples incidents de ransomware impactant des prestataires et causant des effets en cascade sur leurs clients.

Ces chiffres sous-estiment systématiquement la réalité : le sous-signalement est structurel (beaucoup de victimes ne déclarent pas), les pertes indirectes (interruption d'activité, atteinte réputationnelle, coûts de remédiation) ne sont pas incluses, et les incidents dans certaines juridictions ne sont pas comptabilisés.

## 11.6 — Résilience de l'écosystème

Malgré les disruptions, l'écosystème ransomware fait preuve d'une résilience structurelle. Le CSE canadien évalue que « les disruptions n'auront presque certainement pas d'impact durable sur l'environnement ransomware parce que, à moins que les membres du noyau des groupes RaaS soient arrêtés, les acteurs trouvent souvent des moyens de s'adapter, se renommer et reprendre leurs opérations ».

Le modèle CaaS lui-même est un facteur de résilience : « le réseau complexe de services habilitants et de cybercriminels interagissant dans des espaces en ligne sans frontières rend l'enquête sur la cybercriminalité difficile. Si les forces de l'ordre perturbent un fournisseur CaaS populaire, l'acteur derrière lui va souvent renommer et relancer son service, ou un autre service va rapidement prendre sa place. »

## 11.7 — 🔴 Fil rouge : attaque Qilin sur un prestataire

> **📌 FIL ROUGE — Épisode 11**
>
> En juillet 2025, le pire scénario se matérialise. Le sous-traitant IT dont les credentials étaient en vente est victime d'une attaque Qilin. Le ransomware chiffre l'ensemble de l'infrastructure du prestataire — y compris les serveurs de gestion de projet partagés avec EuroDefense. L'accès initial confirme l'hypothèse de Sophie : les credentials VPN vendues sur le forum avaient été achetées par un affilié Qilin.
>
> L'impact cascade est immédiat : EuroDefense perd l'accès aux outils de gestion de projet partagés, et l'investigation révèle que l'attaquant a traversé la connexion réseau vers le SI d'EuroDefense pendant 48 heures avant le déclenchement du ransomware. Sophie reconstitue la timeline : infostealer Lumma → vente de credentials sur forum → achat par affilié Qilin → intrusion via VPN → mouvement latéral → pivot vers EuroDefense → exfiltration de données de projet → déploiement ransomware.
>
> Mais l'enquête réserve une surprise que Sophie n'anticipe pas — elle sera révélée au Chapitre 17.

---
