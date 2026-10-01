---
title: Partie IV — Profilage d'acteur et attribution
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - index.md
---

*Comment construire un profil d'acteur, analyser son tradecraft, et naviguer dans la discipline la plus sensible de la CTI : l'attribution.*

---


## Chapitre 15 — Construire un Threat Actor Profile

### 15.1 Les composantes du profil

Un profil d'acteur complet comprend : **identité et alias** (pseudos, clusters, noms selon les vendors — avec les mappings croisés), **sponsor présumé** (avec niveau de confiance explicite — « attribution GRU avec confiance modérée basée sur... »), **objectifs** (espionnage, sabotage, gain financier, pré-positionnement — déduits de la victimologie et des actions on objectives), **victimologie** (secteurs, géographies, profils d'organisations ciblées — l'outil d'attribution le plus sous-estimé : un acteur qui cible systématiquement les opérateurs d'énergie européens a un profil très différent d'un acteur qui cible des entreprises de toutes tailles dans tous les secteurs), **TTP** (mapping ATT&CK avec les procédures spécifiques — pas juste les techniques génériques), **outils** (malware custom, frameworks C2, outils légitimes détournés — la proportion custom/commodity/LOL est un indicateur de sophistication), **infrastructure** (patterns d'enregistrement de domaines, hébergement préféré, ASN récurrents, certificats — le « fingerprint infrastructurel »), **campagnes** (historique des opérations connues avec timeline), et **évolution** (comment le tradecraft change dans le temps — un acteur qui change ses TTP est un acteur qui apprend de ses détections).

### 15.2 La victimologie comme outil d'attribution

La victimologie est l'outil d'attribution le plus sous-estimé et le plus résistant aux faux drapeaux. Un attaquant peut imiter les TTP d'un autre acteur, utiliser la même infrastructure, et déployer un outil similaire — mais il ne peut pas facilement falsifier sa victimologie. Un acteur qui cible systématiquement les opérateurs d'énergie, les sous-traitants de défense, et les agences gouvernementales en Europe a un profil de victimologie qui pointe vers un nombre limité de sponsors possibles. La corrélation victimologique est donc un complément essentiel à la corrélation technique.

---


## Chapitre 16 — Analyse des TTP et du tradecraft

### 16.1 Au-delà du mapping ATT&CK

Le mapping ATT&CK (« l'acteur utilise T1059.001 PowerShell ») est nécessaire mais insuffisant pour le profilage. Ce qui distingue les acteurs entre eux, c'est la **procédure** — le « comment exactement ». Deux acteurs peuvent utiliser PowerShell (même technique) avec des méthodes radicalement différentes : l'un utilise `-EncodedCommand` avec un payload en base64, l'autre utilise `Invoke-Expression` avec un téléchargement depuis un serveur compromis. Ces différences procédurales sont le « fingerprint comportemental » de l'acteur — plus durable que les IoC et plus distinctif que les techniques ATT&CK génériques.

### 16.2 Le tradecraft comme signature

Le tradecraft est l'ensemble des choix opérationnels de l'attaquant : quel vecteur d'accès initial, quel outil pour le mouvement latéral, quel mécanisme de persistence, quel pattern de beaconing C2, quelle méthode d'exfiltration, et quel niveau d'OPSEC. Ces choix forment un « style » qui est relativement stable dans le temps (changer de tradecraft coûte cher en entraînement et en risque opérationnel). L'analyste CTI qui documente le tradecraft d'un acteur au niveau procédural — pas juste au niveau technique ATT&CK — construit un profil qui permet la détection et l'attribution même quand les IoC changent.

---


## Chapitre 17 — Attribution : méthode, rigueur et limites

### 17.1 Les niveaux d'attribution

L'attribution opère à trois niveaux de profondeur croissante. L'**attribution technique** (quel outil a été utilisé, quelle infrastructure) est la plus facile — c'est le domaine du forensic et de l'analyse de malware. L'**attribution opérationnelle** (quel groupe a conduit l'opération) est plus difficile — elle repose sur la corrélation de TTP, d'infrastructure, et de victimologie. L'**attribution stratégique** (quel État ou organisation a commandité l'opération) est la plus difficile — elle intègre le contexte géopolitique, les capacités connues, les intérêts stratégiques, et parfois du renseignement humain ou technique non public. Chaque niveau a son propre seuil de preuve et son propre niveau de confiance.

### 17.2 Les pièges de l'attribution

Les **false flags** sont la menace la plus sérieuse : un acteur imite délibérément les TTP, les outils, ou l'infrastructure d'un autre acteur pour brouiller l'attribution. Olympic Destroyer (2018) est le cas d'école : le malware contenait des fragments de code de Lazarus Group (DPRK), mais l'attaque a finalement été attribuée au GRU (Russie) qui avait planté ces faux indices. Les **outils partagés** compliquent l'attribution : Cobalt Strike est utilisé par des dizaines d'acteurs étatiques et criminels — sa présence ne discrimine aucun acteur. Les **biais géopolitiques** peuvent déformer l'analyse : attribuer à la Russie ou à la Chine « par défaut » parce que le contexte géopolitique le rend plausible, sans évidences techniques suffisantes.

### 17.3 Le devoir de prudence

Une attribution erronée a des conséquences réelles : décisions de sécurité mal orientées (si on croit que c'est un cybercriminel alors que c'est un État, les contre-mesures sont inadaptées), tensions diplomatiques (si un gouvernement attribue publiquement une attaque à un État sur la base d'une analyse CTI insuffisante), et poursuites judiciaires erronées. L'analyste qui attribue porte une responsabilité — d'où la discipline du niveau de confiance et du « what if I'm wrong ».

---


## Chapitre 18 — Le naming problem et la gestion des clusters

Chaque éditeur CTI nomme les acteurs selon sa propre convention : CrowdStrike utilise des animaux (Bear = Russie, Panda = Chine), Microsoft utilise des phénomènes météo (Blizzard = Russie, Typhoon = Chine), Mandiant utilise APT/UNC/FIN, ESET utilise des noms de créatures. Résultat : APT28 = Fancy Bear = Forest Blizzard = Sofacy = Sednit = Pawn Storm — le même acteur avec 6+ noms.

Le problème du **split/merge** aggrave le chaos : deux vendors peuvent traquer le même acteur sous deux clusters différents (split), ou regrouper deux acteurs distincts sous un même nom (merge). Les fusions sont rétrospectives : quand un vendor détermine que UNC-2452 et NOBELIUM sont le même acteur, il les fusionne — mais pendant des mois, les deux noms ont coexisté dans les rapports.

La discipline du cluster : quand l'analyste observe une activité nouvelle qui ne matche aucun acteur connu, il crée un cluster temporaire avec un nom interne (UNC-VOLT dans MERIDIAN). Le cluster est documenté comme « non attribué » jusqu'à ce que suffisamment de données s'accumulent pour soit l'attribuer à un acteur connu (merge), soit le confirmer comme un nouvel acteur (promotion en APT/FIN/etc.), soit le déclasser (l'activité s'arrête sans suite).

---


## Chapitre 19 — Cas de profilage et d'attribution documentés

### 19.1 SolarWinds / SUNBURST (2020) — attribution à APT29

La campagne supply chain la plus sophistiquée documentée publiquement. L'attaquant a compromis le processus de build de SolarWinds Orion, injecté une backdoor (SUNBURST) dans les mises à jour légitimes, et ciblé environ 18 000 organisations — dont le Trésor américain, le Département d'État, et Microsoft. L'attribution à APT29/SVR repose sur la convergence de multiples indices : TTP cohérentes (supply chain, abus de services cloud, furtivité extrême), infrastructure liée à des campagnes APT29 précédentes, et renseignement gouvernemental (l'attribution publique par les US, UK, et EU cite du renseignement classifié). Le niveau de confiance est élevé — c'est un cas d'école de faisceau d'indices convergents.

### 19.2 NotPetya (2017) — false flag ransomware

Le wiper le plus destructeur de l'histoire ($10 Mrd de dégâts mondiaux). Distribué via une mise à jour piégée du logiciel de comptabilité ukrainien MeDoc, il se propageait via EternalBlue + Mimikatz. Il ressemblait à un ransomware (demande de rançon affichée) mais était en réalité un wiper (la clé de déchiffrement n'existait pas). L'attribution à Sandworm/GRU repose sur le vecteur (supply chain via un logiciel spécifiquement ukrainien — cohérent avec les campagnes Sandworm contre l'Ukraine), les TTP (EternalBlue + credential dumping — signature Sandworm), et le contexte géopolitique (escalade du conflit russo-ukrainien). Le déguisement en ransomware est un false flag classique : faire croire à du cybercrime pour masquer du sabotage étatique.

### 19.3 Cloud Hopper (2016-2018) — attribution par victimologie

APT10 (MSS/Chine) a compromis des MSP (Managed Service Providers) pour accéder aux réseaux de leurs clients — des centaines d'entreprises dans des dizaines de pays. L'attribution repose fortement sur la victimologie : les données volées correspondaient aux priorités stratégiques de la Chine (propriété intellectuelle dans les secteurs technologique, industriel, et défense), et le ciblage systématique des MSP (qui donnent un accès à de multiples organisations) est cohérent avec les objectifs d'espionnage à grande échelle du MSS.

### 19.4 Un cas de révision d'attribution

L'attribution n'est pas définitive — elle peut être révisée quand de nouvelles données apparaissent. L'analyste mature accepte la révision comme un signe de rigueur, pas d'échec. Le cas Olympic Destroyer (2018) illustre ce point : les premiers indices (fragments de code Lazarus) pointaient vers la DPRK. Des analyses approfondies ont révélé que ces fragments étaient des faux drapeaux plantés par le GRU (Russie). L'attribution a été révisée — un processus douloureux mais nécessaire qui a renforcé la crédibilité de la communauté CTI.

---
