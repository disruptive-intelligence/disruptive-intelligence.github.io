---
title: Partie VII — Géopolitique, attribution et prospective
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

---


## Chapitre 23 — Attribution : méthodes, limites et enjeux

Ce que signifie « attribuer » dans le contexte APT : relier une activité observée à un acteur (technique), un service (opérationnel), et un État (stratégique). Les 3 niveaux ont des seuils de preuve croissants. Les évidences d'attribution (TTP/tradecraft, infrastructure, malware, victimologie, timing géopolitique, renseignement humain/technique). Les pièges (false flags — Olympic Destroyer avec des fragments Lazarus plantés par le GRU ; outils partagés — Cobalt Strike utilisé par tout le monde ; infrastructure louée — VPS partagés ; biais géopolitiques — attribuer à la Russie « par défaut » parce que le contexte le rend plausible). Les niveaux de confiance (high, moderate, low — jamais « certain »). L'attribution publique par les gouvernements (naming and shaming, indictments DOJ — outil diplomatique autant que sécuritaire). Le cours CTI (bibliothèque) enseigne la méthode d'attribution en profondeur ; le cours APT fournit les données sur les acteurs qui la rendent possible.

> **⚡ BLACKOUT — Épisode 6**
>
> Processus d'attribution : matrice ACH avec 4 hypothèses (H1 Sandworm/GRU, H2 Volt Typhoon/Chine, H3 nouveau cluster étatique, H4 acteur non étatique). Évidences : beaconing compatible Sandworm (C pour H1, I pour H2), exploitation Ivanti compatible Chine (C pour H2, C pour H1 — Ivanti est exploité par les deux), LotL (C pour H2, I partiel pour H1 — Sandworm utilise typiquement des outils custom), victimologie énergie Europe (C pour H1, C pour H2), pas de malware custom identifié (I pour H1, C pour H2). Résultat : H1 et H2 restent plausibles, H4 est éliminée. Conclusion : confiance modérée pour H1 (Sandworm/GRU), confiance faible pour H2. Indicateurs de révision : si un outil custom Sandworm est identifié → H1 renforcée ; si un pattern d'infrastructure chinoise est trouvé → H2 renforcée.

---


## Chapitre 24 — L'écosystème cyber offensif mondial

Vision d'ensemble : plusieurs centaines de groupes APT sont suivis par les vendors CTI mondiaux. La **prolifération** des capacités est la tendance la plus préoccupante : les outils et techniques autrefois réservés aux acteurs les plus sophistiqués sont maintenant accessibles (Cobalt Strike cracké, Brute Ratel commercialisé, frameworks C2 open source — Sliver, Havoc, Mythic). L'économie de la surveillance privée (NSO, Intellexa) est un marché d'armement cyber qui vend des capacités étatiques à des États qui n'auraient pas pu les développer seuls.

**Lecture comparative des doctrines :** la Russie pratique la guerre hybride intégrée (espionnage + destruction + influence) ; la Chine pratique l'espionnage de masse et le pré-positionnement stratégique ; la DPRK pratique le financement du régime par le cybervol ; l'Iran pratique le ciblage régional et le destructif ponctuel ; les États-Unis pratiquent le defend forward et le law enforcement ; Israël pratique la préemption et la supériorité technologique ; le Royaume-Uni pratique la disruption coordonnée avec les Five Eyes. Ces doctrines reflètent les priorités stratégiques, les cultures bureaucratiques, et les cadres juridiques de chaque État.

---


## Chapitre 25 — Géopolitique des normes cyber, droit international et cadre français

### 25.1 Le droit international appliqué au cyberespace

Le processus de **Tallinn** (manuel rédigé par des experts, non contraignant mais référence académique) a posé les bases de l'application du droit international au cyberespace — les États sont responsables des cyberopérations qu'ils conduisent ou tolèrent, et les principes de souveraineté, de non-intervention, et de proportionnalité s'appliquent. Le **GGE** (Group of Governmental Experts) et l'**OEWG** (Open-Ended Working Group) à l'ONU négocient les normes de comportement responsable des États dans le cyberespace — avec des positions divergentes entre le bloc occidental (normes existantes suffisantes, à appliquer) et le bloc Russie/Chine (nouveau traité nécessaire, avec une définition de « sécurité de l'information » qui couvre aussi le contenu — contrôle de l'internet).

### 25.2 Attributions publiques et sanctions

Les attributions publiques par les Five Eyes, l'UE, et l'OTAN sont devenues un instrument diplomatique régulier (NotPetya 2018, SolarWinds 2021, Volt Typhoon 2024). Leur effet : réduction de la marge de déni plausible, signal de capacité de détection, et pression diplomatique. Les **indictments DOJ** (poursuites criminelles américaines) ont un effet de naming and shaming même si les inculpés ne seront probablement jamais jugés. L'**EU Cyber Sanctions Regime** (depuis 2019) permet des sanctions ciblées (gel des avoirs, interdiction de voyager) contre des personnes et entités impliquées dans des cyberattaques.

### 25.3 Le cadre français et européen

**La France** dispose d'un appareil cyber structuré et croissant. L'**ANSSI** (Agence Nationale de la Sécurité des Systèmes d'Information, rattachée au SGDSN) protège les OIV et les entités essentielles NIS 2, publie des advisories de référence, qualifie les prestataires (PASSI, PDIS, SecNumCloud), et conduit les investigations sur les incidents d'envergure nationale. Le **COMCYBER** (Commandement de la cyberdéfense, ministère des Armées) conduit les opérations militaires cyber — la France a officialisé sa doctrine de **lutte informatique offensive (LIO)** en 2019 (revue stratégique de cyberdéfense) : la France se réserve le droit de mener des opérations offensives dans le cyberespace en réponse à une agression. La **lutte informatique défensive (LID)** et la **lutte informatique d'influence (L2I)** complètent le dispositif. La **DGSE** et la **DGSI** contribuent au renseignement cyber. Le **C4** (Centre de Coordination des Crises Cyber, créé 2022) coordonne la réponse aux crises cyber majeures.

Au niveau européen, l'**ENISA** coordonne la cybersécurité entre les États membres. La directive **NIS 2** (2024) étend les obligations de cybersécurité à un périmètre beaucoup plus large d'entités. L'**EU Cyber Solidarity Act** (2024) crée un réseau de SOC européens et un mécanisme de réponse d'urgence. Et l'**OTAN** a reconnu le cyberespace comme 5ème domaine d'opérations (Varsovie 2016) et intègre le cyber dans sa planification de défense collective (un cyberattaque peut déclencher l'article 5 — même si le seuil n'a jamais été formellement défini).

---


## Chapitre 26 — Tendances 2024-2026 et signaux d'anticipation

**Exploitation massive des appliances edge** : les VPN, firewalls, et passerelles exposés sont le vecteur n°1 des acteurs étatiques sophistiqués (Ivanti, Fortinet, Citrix, Barracuda — souvent exploités dans les heures suivant la publication d'un advisory). **Ciblage de l'identité cloud** : Azure AD/Entra ID, tokens SAML/OAuth, MFA bypass (AitM), SSO compromise — l'identité est le nouveau périmètre. **Convergence crime-État** : les frontières s'estompent (APT41, ransomware russophones tolérés, DPRK). **LotL comme standard** : Volt Typhoon a démontré qu'une opération étatique sophistiquée peut être conduite sans aucun malware custom. **IA offensive** : phishing amélioré par LLM, deepfakes vocaux pour le social engineering, aide au développement de malware — impact croissant mais pas encore transformatif. **Pré-positionnement dans les infras critiques** : la menace structurelle qui définira la prochaine décennie.

Les signaux géopolitiques à surveiller : tensions Taïwan → pré-positionnement chinois accru, escalade Ukraine → destructif russe contre les alliés, élections → influence, sanctions → espionnage/vol, crise énergétique → ciblage énergie.

---


## Chapitre 27 — Construire une défense APT-ready

Ce chapitre n'est pas un cours de SOC ou d'IR (voir les cours dédiés) — c'est une synthèse des principes de défense spécifiques aux APT. Les **contrôles minimum viables** (MFA résistant au phishing — P0, PAM — P0, EDR partout y compris serveurs — P0, patching edge devices < 48h — P0, segmentation réseau — P1, durcissement AD — P1, monitoring cloud/identity — P1, backup hors ligne testé — P1, plan IR formalisé — P1). La **visibilité minimum viable** : Sysmon, PowerShell ScriptBlock, DNS, auth logs, Azure AD, firewall/proxy, EDR, email gateway — sans ces sources, l'APT est invisible. La **détection TTP-driven** : détecter les comportements, pas les IoC (renvoi cours SOC). Le **containment APT** : scope AVANT de contenir (identifier TOUS les systèmes compromis, sinon l'attaquant active ses accès redondants), containment coordonné et simultané (pas séquentiel), et monitoring renforcé post-éradication (l'attaquant essaiera de revenir). Le **purple team orienté APT** : simuler les TTP des acteurs pertinents avec Atomic Red Team (renvoi cours SOC Ch.30).

---


## Chapitre 28 — Exercices de simulation

**Tabletop 1 — « APT29 a compromis votre Azure AD via phishing OAuth » :** scénario de 2h avec injections progressives (J0 : alerte sign-in suspect → J+1 : règle de forwarding détectée → J+3 : exfiltration SharePoint → J+5 : découverte de tokens SAML forgés). Questions clés : quand escaladez-vous ? qui informez-vous ? contenez-vous immédiatement ou scopez-vous d'abord ?

**Tabletop 2 — « Ransomware BlackBasta avec précurseur APT » :** discrimination APT vs cybercrime — l'investigation révèle que l'accès initial a été vendu par un IAB qui l'avait acheté à un acteur étatique. Implications pour la réponse, la notification, et l'attribution.

**Tabletop 3 — « Pré-positionnement OT détecté sans action destructive » :** l'attaquant est dans le réseau SCADA mais n'a rien fait. Éradiquez-vous immédiatement (risque de perdre le renseignement) ou surveillez-vous pour comprendre ses intentions (risque de laisser une menace active) ? Le dilemme fondamental du pré-positionnement.

---
