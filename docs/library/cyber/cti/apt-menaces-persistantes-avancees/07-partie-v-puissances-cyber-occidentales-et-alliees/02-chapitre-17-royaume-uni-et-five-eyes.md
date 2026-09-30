---
title: Chapitre 17 — Royaume-Uni et Five Eyes
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie V — Puissances cyber occidentales ET alliées
  - index.md
---

## 17.1 GCHQ : agence SIGINT et partenaire NSA

**Government Communications Headquarters** (GCHQ) est l’agence britannique d’origine électromagnétique et cyber. Héritière de Bletchley Park (déchiffrement Enigma pendant la Seconde Guerre mondiale), GCHQ est un partenaire étroit de la NSA — la relation US-UK en matière de SIGINT est la plus intégrée au monde, formalisée par l’**UKUSA Agreement** (1946) qui a évolué vers les Five Eyes.

**Mission** : collecte SIGINT mondiale, analyse cyber, soutien aux opérations militaires britanniques, protection de la sécurité nationale.

**Structure** : GCHQ dispose d’une branche cyber offensive intégrée au **National Cyber Force** (voir 17.3) et d’une branche défensive dans le **NCSC** (voir 17.2). La Joint Forces Intelligence Group et d’autres structures complètent le dispositif.

**Publications** : GCHQ publie occasionnellement des analyses techniques, en coordination avec le NCSC. Les attributions GCHQ-NCSC sont parmi les premières dans les attributions coordonnées Five Eyes (NotPetya, SolarWinds, Volt Typhoon).

## 17.2 NCSC : le modèle de protection nationale

**National Cyber Security Centre** (NCSC), créé en 2016 comme branche publique du GCHQ, est l’organisme britannique de protection cyber nationale. Le modèle NCSC est largement considéré comme **une référence internationale** et a inspiré plusieurs agences européennes (ANSSI en partie, BSI en Allemagne).

**Caractéristiques du modèle NCSC** :

- **Publications accessibles** : documentation technique de haute qualité, formulée dans un langage accessible aux non-experts.
- **Collaboration directe avec le secteur privé** : « Active Cyber Defence » programme qui offre gratuitement des services aux organisations britanniques (DMARC, protective DNS, takedown de sites de phishing).
- **Early Warning et threat intelligence partagée** : le NCSC partage des alertes avec les organisations inscrites.
- **Cyber Essentials** : certification cybersécurité accessible aux PME britanniques — modèle qui a inspiré d’autres programmes européens.
- **Transparence** : le NCSC communique plus ouvertement que la plupart de ses homologues sur les incidents nationaux et les menaces — tout en respectant les classifications nécessaires.

**Attributions** : le NCSC (avec GCHQ) attribue publiquement des opérations étatiques. Les attributions NotPetya (2018), Volt Typhoon (2023-2024), APT31 (2024), Salt Typhoon (2024) ont été coordonnées avec les partenaires Five Eyes et relayées par le NCSC.

**NCSC Annual Review** : rapport annuel public qui documente les tendances de la menace sur le Royaume-Uni, les opérations de défense, et les points de mobilisation.

## 17.3 National Cyber Force : opérations offensives

**National Cyber Force** (NCF), créée publiquement en 2020, est l’organisation britannique dédiée aux opérations cyber offensives. Elle rassemble des personnels du GCHQ, du Ministry of Defence (notamment 77th Brigade pour les opérations d’information), et du Secret Intelligence Service (MI6/SIS).

**Mission** : conduire des opérations cyber offensives pour soutenir les intérêts britanniques, avec un focus sur la **disruption ciblée** plutôt que sur la destruction massive. Le NCF se positionne doctrinalement sur la « disruption by design » — désorganiser les adversaires sans détruire, contester sans escalader.

**Cas d’usage publics** :

- Opérations contre les infrastructures Daesh (héritage de JTRIG).
- Opérations contre des réseaux pédocriminels.
- Opérations cyber en soutien des opérations militaires britanniques.
- Opérations contre des groupes cybercriminels (contributions aux démantèlements internationaux).

La NCF est moins visible publiquement qu’USCYBERCOM, mais sa création formelle marque un jalon — le Royaume-Uni a ouvertement assumé ses capacités cyber offensives.

## 17.4 JTRIG : opérations d’information et disruption

**Joint Threat Research Intelligence Group** (JTRIG) est une branche historique du GCHQ, révélée publiquement par les fuites Snowden (2014). Ses capacités incluent des opérations d’influence en ligne, des disruptions de forums criminels et extrémistes, et des opérations d’information contre des cibles stratégiques.

Les documents JTRIG révélés par Snowden ont documenté des opérations contre Anonymous, contre des forums djihadistes, et contre des cibles gouvernementales étrangères. L’exposition publique a suscité des débats sur la légitimité démocratique de certaines opérations (ciblage d’acteurs non étatiques, techniques de manipulation psychologique).

Post-Snowden, JTRIG a probablement été restructurée dans d’autres entités (NCF notamment) mais ses capacités et missions ne sont pas publiquement supprimées.

## 17.5 Five Eyes : l’alliance SIGINT intégrée

L’alliance **Five Eyes** (US, UK, Canada, Australie, Nouvelle-Zélande) est le partage de renseignement SIGINT et cyber le plus intégré au monde. Hérité de l’UKUSA Agreement de 1946, elle s’est étendue progressivement aux trois autres signataires du Commonwealth.

**Mécanismes** :

- **Partage de renseignement SIGINT** : les cinq agences (NSA, GCHQ, CSE Canada, ASD Australie, GCSB NZ) partagent leur collecte entre elles, avec des règles de retenue selon la sensibilité.
- **Partage cyber** : advisories conjoints, IoC et TTP partagés en quasi temps réel, coordination des attributions publiques.
- **Division du travail géographique et technique** : historiquement, chaque Eye couvrait des zones géographiques spécifiques ou des capacités techniques complémentaires.

**Autres agences Five Eyes** :

- **Canada — Communications Security Establishment** (CSE) et **Canadian Centre for Cyber Security** (CCCS, branche publique du CSE, créé 2018 sur le modèle NCSC).
- **Australie — Australian Signals Directorate** (ASD) et **Australian Cyber Security Centre** (ACSC).
- **Nouvelle-Zélande — Government Communications Security Bureau** (GCSB).

**Attributions coordonnées** : les grandes attributions cyber récentes ont presque toutes été Five Eyes avec relais dans chaque pays. NotPetya (2018), SolarWinds (2021), Hafnium/ProxyLogon (2021), Volt Typhoon (2023-2024), APT31 (2024), APT40 (2024), Salt Typhoon (2024-2025) ont toutes été attribuées dans des communiqués coordonnés des cinq pays (plus souvent étendus à des alliés européens et asiatiques : France, Allemagne, Japon, Corée du Sud, Pays-Bas, etc.).

**Étendues d’alliés** : au-delà des Five Eyes stricto sensu, les attributions et les partages s’étendent régulièrement à des « alliés +1 » ou « +X » — **AUKUS** (US, UK, Australie, avec dimension nucléaire), **Quad** (US, Japon, Inde, Australie), **UKUSA élargi** (incluant parfois France, Allemagne, Pays-Bas, Japon, Corée du Sud). La géographie du partage cyber s’étend continuellement.

## 17.6 Opérations documentées

**Disruption de botnets** : contribution britannique à de multiples démantèlements (Emotet, Qakbot, LockBit notamment, où la NCA britannique a été en lead).

**Opérations contre Daesh** : GCHQ et le Ministry of Defence ont publiquement reconnu des opérations cyber contre les infrastructures de communication et de propagande de Daesh (2015-2019).

**Attribution Volt Typhoon (2023)** : le NCSC a co-signé l’advisory Five Eyes de mai 2023 qui a publiquement attribué Volt Typhoon à la Chine. Le ciblage des infrastructures critiques britanniques par des acteurs chinois est un thème récurrent des déclarations publiques NCSC.

**Attribution APT31 (mars 2024)** : le UK a attribué APT31 à des ciblages de parlementaires britanniques et de la Commission électorale. Sanctions coordonnées avec les États-Unis.

**Operation Cronos (LockBit, février 2024)** : la NCA (National Crime Agency) a été en lead de l’opération internationale. Premier cas d’opération de démantèlement ransomware majeur avec le Royaume-Uni en tête.

## 17.7 Modèle de disruption by design

La doctrine britannique peut être résumée par le concept de **« disruption by design »** : contester les adversaires cyber en dégradant leurs capacités, sans nécessairement chercher des effets destructeurs majeurs. Le NCF articule des opérations proportionnées — désorganiser une campagne de phishing, rendre inopérants des outils spécifiques, exposer publiquement des opérateurs.

Cette doctrine est cohérente avec la tradition britannique d’intelligence operations — actions clandestines préférées à l’action militaire ouverte, usage stratégique du law enforcement et de la diplomatie, coordination étroite avec les partenaires.

-----
