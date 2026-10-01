---
title: 'Chapitre 7 — La Russie : de l''espionnage au sabotage hybride'
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - ../index.md
- - PARTIE II — Les acteurs étatiques
  - index.md
---

## 7.1 — L'écosystème cyber russe

L'écosystème cyber offensif russe se distingue par sa **diversité institutionnelle et l'étendue de son réseau de proxies**. Trois services de renseignement opèrent des programmes cyber distincts, complétés par un réseau mouvant de cybercriminels patriotiques, de hacktivistes alignés et de « hackers-for-hire ».

Le **GRU** (Direction principale du renseignement militaire) opère les unités les plus offensives. L'unité 26165 (connue sous les noms APT28, Fancy Bear, Forest Blizzard) conduit des opérations d'espionnage stratégique ciblant les gouvernements, les organisations militaires et les secteurs d'intérêt pour le renseignement militaire russe. L'unité 74455 (connue comme Sandworm) est responsable des opérations les plus destructives — wipers en Ukraine, attaques contre les infrastructures énergétiques — et a été liée à l'opération de « faketivisme » Cyber Army of Russia Reborn.

Le **SVR** (Service de renseignement extérieur) opère APT29 (Nobelium, Midnight Blizzard, Cozy Bear). Le SVR se concentre sur l'espionnage stratégique de haut niveau — gouvernements, diplomatie, think tanks — avec des opérations caractérisées par leur sophistication et leur persistance. La compromission de SolarWinds (2020) et le ciblage de Microsoft en 2024 sont attribuées au SVR.

Le **FSB** (Service fédéral de sécurité) opère plusieurs groupes, dont Star Blizzard (anciennement Callisto), spécialisé dans le spearphishing ciblant les think tanks, les médias, les ONG et les personnalités impliquées dans les questions de politique étrangère. Le CERT-FR documente le ciblage par Callisto de l'ONG Reporters sans frontières. Le FSB opère également Turla, un acteur historique connu pour la sophistication de ses implants et sa capacité à compromettre d'autres acteurs pour obscurcir ses opérations.

L'écosystème russe inclut un réseau étendu de **proxies non-étatiques** — cybercriminels, hacktivistes, hackers-for-hire — motivés par un mélange de patriotisme, de profit et d'opportunisme. Le CSE canadien note que « cette stratégie hybride, qui fournit à la Russie un déni plausible, semble avoir été émulée par d'autres États, créant un environnement de cybermenace plus complexe ».

## 7.2 — Le contexte Ukraine

cyberattaques destructives et espionnage militaire

Le conflit en Ukraine reste le driver principal de l'activité cyber russe depuis février 2022. Les opérations combinent attaques destructives, espionnage militaire, ciblage logistique et opérations d'influence.

En mai 2025, l'ASD australien s'est joint à des partenaires internationaux pour alerter sur une campagne du GRU (unité 26165/APT28) ciblant les entités logistiques occidentales et les entreprises technologiques impliquées dans la livraison d'aide à l'Ukraine. La campagne utilisait un mix de TTPs connus — password spraying, spearphishing, modification de permissions Exchange — et ciblait spécifiquement les acteurs de la chaîne de transport et de coordination de l'aide. Le groupe a également ciblé des caméras de surveillance internet aux frontières ukrainiennes pour surveiller les flux d'aide.

En décembre 2023, un acteur russe a conduit une attaque destructive (wiper) contre l'opérateur télécom ukrainien Kyivstar, laissant des millions d'Ukrainiens sans internet ni service mobile pendant plusieurs jours. L'acteur avait maintenu un accès dans les systèmes de Kyivstar depuis au moins mai 2023 et a revendiqué l'attaque dans un post Telegram adressé au président Zelenskyy — illustrant la dimension psychologique de l'opération.

Le CERT-EU documente plusieurs campagnes d'espionnage cyber liées au conflit : APT29 imitant un ministère des affaires étrangères européen avec de fausses invitations à des dégustations de vin pour installer une backdoor modulaire furtive, et le groupe DoNot ciblant des entités diplomatiques d'Europe du Sud en se faisant passer pour des diplomates.

## 7.3 — L'évolution des TTPs : adoption d'outils commodity

Un phénomène notable documenté par l'ANSSI est l'adoption croissante d'outils cybercriminels « commodity » par les acteurs étatiques russes. Historiquement, les groupes APT russes développaient des outils propriétaires sophistiqués (Fancy Bear's X-Agent, Turla's Snake). Aujourd'hui, ils utilisent de plus en plus des outils disponibles publiquement ou dans l'écosystème cybercriminel — Cobalt Strike, Brute Ratel, outils de tunnelling légitimes — rendant l'attribution plus difficile.

Les campagnes d'APT28 « semblent répondre à des besoins de renseignement stratégique immédiat et présentent des niveaux de sophistication variables », note l'ANSSI. Certaines campagnes reposent sur des comptes légitimes compromis, des services de création d'adresses de messagerie temporaires, ou de l'usurpation d'adresses légitimes. D'autres utilisent l'exploitation de vulnérabilités, y compris zero-day. Cette variabilité suggère que les opérateurs adapte leur effort au niveau de valeur de la cible.

## 7.4 — Le ciblage de l'Europe : du diplomatique au destructif

L'année 2025 marque un escalade avec les attaques destructives contre les infrastructures électriques polonaises — première attaque de ce type contre un État membre de l'UE. L'ANSSI note que cet événement « illustre concrètement le scénario auquel la France se prépare : une augmentation massive — d'ici 2030 — des attaques dites hybrides, dont les cyberattaques constituent un pan majeur, avec des effets concrets voire destructeurs sur nos infrastructures critiques ».

Le ciblage européen s'étend aux processus électoraux. Les élections dans plusieurs pays européens fin 2024 et courant 2025 ont constitué des opportunités d'attaques cyber ou d'influence. VIGINUM a documenté des manipulations de l'information ciblant l'élection présidentielle roumaine de 2024, où des modes opératoires informationnels ont artificiellement promu des contenus sur TikTok. Des DDoS hacktivistes pro-russes ont ciblé les sites de partis politiques danois le jour des élections en novembre 2025.

## 7.5 — La convergence état-cybercrime

NailoLocker et le brouillage des frontières

L'un des cas les plus révélateurs de la convergence étatique-criminelle est documenté par Orange CyberDefense, Fortinet et Trendmicro : la distribution du ransomware NailoLocker en Europe via les backdoors ShadowPad et PlugX — des outils historiquement associés à l'espionnage chinois, mais dans un contexte d'opération où les éléments d'attribution sont ambigus.

L'ANSSI documente un phénomène similaire côté russe : des outils d'espionnage étatiques utilisés en conjonction avec du ransomware, et des acteurs de cyberespionnage qui « adoptent des pratiques qui caractérisaient jusqu'à présent davantage » les cybercriminels. Le groupe ChamelGang illustre cette convergence — documenté par SentinelOne comme un groupe d'espionnage ciblant les infrastructures critiques avec du ransomware.

Les motivations possibles de cette convergence sont multiples : utiliser le ransomware comme couverture pour des opérations d'espionnage (le bruit du ransomware masque l'exfiltration), générer des revenus complémentaires, créer de la confusion pour compliquer l'attribution, ou combiner déstabilisation et gain financier.

## 7.6 — L'instrumentalisation des hacktivistes

La Russie a développé un modèle sophistiqué d'instrumentalisation des hacktivistes. Le groupe **Cyber Army of Russia Reborn (CARR)** est le cas le plus documenté : précédemment lié à Sandworm (GRU), CARR se présente comme un groupe hacktiviste indépendant mais ses opérations semblent coordonnées avec les objectifs militaires russes. Le département du Trésor américain a sanctionné des membres de CARR en juillet 2024.

**NoName057(16)** est le groupe hacktiviste pro-russe le plus actif contre l'UE, représentant 66,7% des attaques hacktivistes ciblant les administrations publiques européennes selon l'ENISA. Le groupe opère la plateforme DDoSia, qui permet à des volontaires de contribuer leur bande passante aux attaques DDoS. Si le lien direct avec l'État russe n'est pas publiquement établi, le timing des attaques — systématiquement aligné sur les événements géopolitiques favorables aux intérêts russes — suggère au minimum une coordination tacite.

## 7.7 — Les opérations d'influence

La Russie « voit presque certainement son programme cyber comme partie d'une stratégie multi-couches pour influencer et façonner l'environnement informationnel », évalue le CSE canadien. Les opérations combinent espionnage cyber (vol de documents), manipulation de l'information (diffusion de documents volés, création de faux récits) et amplification (bots, trolls, faux sites d'information).

Microsoft documente l'émergence d'acteurs « AI-first » russes qui privilégient les contenus générés par IA sur les méthodes traditionnelles, « inondant l'espace informationnel de médias synthétiques pour désensibiliser les audiences et épuiser les systèmes de détection ». L'utilisation de l'IA pour créer des répliques numériques de présentateurs de journaux télévisés (AI twinning) qui diffusent des narratifs pro-russes avec un vernis de crédibilité est documentée comme une technique émergente.

## 7.8 — 🔴 Fil rouge : campagne de phishing ciblant les contrats OTAN

> **📌 FIL ROUGE — Épisode 7**
>
> En avril 2025, le département « contrats OTAN » d'EuroDefense reçoit une série d'emails contenant des fichiers .rdp (Remote Desktop Protocol) malveillants. Les emails se présentent comme des documents de travail d'un fabricant de défense européen partenaire. Le CERT-EU a publié une alerte quelques semaines plus tôt sur exactement ce type de campagne, attribuée à un acteur Russia-nexus : des fichiers RDP malveillants usurpant l'identité d'un fabricant de défense d'un État membre.
>
> Sophie corrèle immédiatement : le vecteur (fichiers RDP), le lure (secteur défense), le timing (période de renouvellement de contrats OTAN) et l'alerte CERT-EU pointent vers un acteur Russia-nexus, probablement APT28 ou un groupe affilié. Elle attribue avec une confiance modérée (B2) à un intrusion set Russia-nexus et recommande : blocage immédiat des fichiers .rdp en pièce jointe, analyse des connexions RDP sortantes des dernières 48 heures, sensibilisation ciblée du département contrats OTAN, et notification au CERT-EU.

---
