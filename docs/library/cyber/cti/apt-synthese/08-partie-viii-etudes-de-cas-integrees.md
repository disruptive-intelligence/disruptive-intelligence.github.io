---
title: Partie VIII — Études de cas intégrées
source: Cyber/01_CTI/APT_Synthese.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

*4 cas complets représentant 4 paradigmes et 3 blocs d'acteurs différents : supply chain (Russie), financement (DPRK), pré-positionnement (Chine), et investigation multi-hypothèses (fil rouge).*

---


## Chapitre 29 — SolarWinds/SUNBURST

la supply chain comme vecteur d'espionnage

Le paradigme de l'espionnage via supply chain — le cas le plus sophistiqué documenté publiquement.

**Acteur :** APT29 / Cozy Bear / Midnight Blizzard (SVR). **Attribution publique :** NSA, FBI, CISA, Five Eyes (janvier 2021). Confiance : élevée.

**Timeline complète :** septembre-octobre 2019 — activité suspecte dans l'environnement SolarWinds, modifications de « test » dans le code Orion. Février-mars 2020 — la backdoor SUNBURST est injectée dans les builds opérationnels. Mars 2020 — la mise à jour trojanisée est distribuée à ~18 000 organisations. Mars-décembre 2020 — APT29 sélectionne ~100 cibles de haute valeur (Trésor US, Commerce, Homeland Security, Microsoft, FireEye) et déploie des outils supplémentaires (TEARDROP, RAINDROP, GoldMax). Décembre 2020 — FireEye/Mandiant détecte l'intrusion en enquêtant sur le vol de ses propres outils Red Team. Divulgation publique.

**TTP détaillées :** Supply Chain Compromise (T1195.002), Signed Binary Proxy Execution (T1218 — le malware exécuté comme composant légitime d'Orion, signé numériquement), Masquerading (T1036 — C2 via DNS camouflé en requêtes Orion Improvement Program), Application Layer Protocol (T1071 — C2 HTTPS), Account Discovery (T1087), Use Alternate Authentication Material (T1550 — GoldenSAML pour forger des tokens SAML et accéder à Azure AD/O365 sans credentials), Email Collection (T1114 — accès aux boîtes mail via Graph API), Exfiltration Over C2 (T1041).

**Leçons :** la supply chain logicielle est un vecteur APT majeur, le monitoring du plan de contrôle identity (SAML, OAuth, tokens) est indispensable, l'intégrité du build pipeline est un enjeu stratégique, et Zero Trust s'impose (la confiance implicite dans un fournisseur ne protège pas).

---


## Chapitre 30 — Lazarus et l'empire crypto de la DPRK

Le paradigme unique du financement étatique par le cybervol — le seul cas dans l'histoire où un État finance sa survie et son programme d'armement par le vol de cryptomonnaies.

**Acteur :** Lazarus Group / Diamond Sleet et sous-groupes (APT38/BlueNoroff). **Attribution publique :** FBI, DOJ, Treasury/OFAC (multiples entre 2018 et 2025). Confiance : élevée.

**Chronologie des vols majeurs :** Bangladesh Bank 2016 ($81M, SWIFT), échanges de crypto 2017-2021 (centaines de millions cumulés), Ronin Network 2022 ($620M, bridge Ethereum), Harmony Bridge 2022 ($100M), Atomic Wallet 2023 ($100M), et Bybit 2025 (~$1,5 Mrd — le vol de crypto le plus important de l'histoire, attribué par le FBI). Le cumul est estimé entre $3 et $6 Mrd.

**Le pipeline complet :** accès initial (social engineering LinkedIn — fausses offres d'emploi ciblant les développeurs et les employés d'exchanges ; supply chain — 3CX ; exploitation de vulnérabilités DeFi) → compromission des clés privées ou des systèmes de signature → transfert des fonds → blanchiment (mixeurs — Tornado Cash sanctionné par l'OFAC en 2022, ponts cross-chain, conversion via des exchanges à KYC faible, mules, et OTC desks en Chine).

**L'impact géopolitique :** ces fonds financent directement le programme nucléaire et balistique nord-coréen — le cyber est une arme de prolifération. Le ROI est extraordinaire : le coût d'une opération de vol de crypto est de quelques centaines de milliers de dollars ; le revenu peut être de centaines de millions à plus d'un milliard. C'est le retour sur investissement le plus élevé de l'histoire du renseignement.

**Contexte DIMEFIL :** Financial (contournement de sanctions, financement du régime), Economic (substitut aux exportations légales bloquées par les sanctions).

---


## Chapitre 31 — Volt Typhoon : le pré-positionnement stratégique

Le paradigme du pré-positionnement sans action — la menace la plus difficile à détecter et la plus lourde de conséquences.

**Acteur :** PRC state-sponsored (évalué comme PLA ou affilié, nommé Volt Typhoon par Microsoft). **Attribution publique :** advisory conjoint NSA/CISA/FBI + Five Eyes (mai 2023, réitéré en 2024). Confiance : élevée.

**Timeline :** au moins depuis mi-2021, probablement plus tôt. Les accès ont été découverts dans des opérateurs de télécoms, des fournisseurs d'énergie, des systèmes d'eau, et des infrastructures de transport aux États-Unis et dans les territoires du Pacifique (Guam).

**TTP :** exploitation d'appliances edge (routeurs SOHO, VPN, firewalls — exploitation de vulnérabilités connues sur des équipements non patchés), LotL quasi exclusif (PowerShell, WMI, net.exe, ntdsutil — aucun malware custom identifié), credentials légitimes (comptes admin compromis via credential dumping), et maintien d'accès long terme sans action visible. Les communications C2 transitent par des routeurs SOHO compromis (botnets de routeurs domestiques) — ce qui rend la détection réseau extrêmement difficile car le trafic semble provenir de localisations résidentielles légitimes.

**Signification stratégique :** Volt Typhoon est interprété par la communauté de renseignement américaine comme une capacité de dissuasion/représailles chinoise liée au scénario Taïwan. Le message : « si vous intervenez militairement, nous pouvons frapper vos infrastructures critiques ». C'est la menace qui définira la prochaine décennie en géopolitique cyber.

**Leçons :** la menace la plus dangereuse est celle qui ne fait rien — comment détecter ce qui ressemble à de l'activité normale (pas d'IoC, pas de malware, des LOLBins et des credentials légitimes). La réponse : monitoring comportemental, baseline des activités admin, corrélation multi-sources, et collaboration avec les agences nationales.

---


## Chapitre 32 — Synthèse BLACKOUT

attribution et réponse face à l'incertitude

Synthèse du fil rouge sous forme de cas autonome — de la détection à la réponse, en passant par l'attribution.

**Détection (J+42) :** l'EDR détecte un comportement anormal sur un poste d'ingénierie OT — rundll32 avec DLL non signée et beaconing HTTPS régulier. Le CERT remonte la chaîne.

**Investigation :** reconstitution de la timeline (exploitation Ivanti J0, persistence J+3, Kerberoasting J+5, mouvement latéral J+8, pivot OT J+15, inactivité J+30 à J+42). Collecte des artefacts (logs Sysmon, Event Logs AD, captures réseau, dump mémoire du poste OT). Analyse des TTP (mapping ATT&CK complet).

**Attribution :** matrice ACH avec 4 hypothèses. H1 : Sandworm/GRU (beaconing compatible, ciblage énergie compatible, contexte géopolitique cohérent — mais pas de malware custom Sandworm, exploitation Ivanti atypique → confiance modérée). H2 : Volt Typhoon ou acteur chinois similaire (exploitation Ivanti signature, LotL, pré-positionnement sans action — mais beaconing non compatible avec les profils chinois documentés → confiance faible). H3 : nouveau cluster étatique non attribué (possible, non réfutable → confiance faible). H4 : acteur non étatique sophistiqué (très peu probable — le ciblage OT sans monétisation élimine le cybecrime → éliminée). Conclusion : confiance modérée pour H1, indicateurs de révision identifiés.

**Réponse :** éradication de tous les accès (persistence, comptes backdoor, modifications AD), sécurisation du réseau OT (segmentation physique IT/OT renforcée, déploiement Sysmon/EDR sur les postes d'ingénierie OT, monitoring réseau OT dédié), signalement ANSSI (l'opérateur est OIV — notification obligatoire NIS 2), partage ISAC énergie européen (TLP:AMBER — IoC et TTP partagés → 2 autres opérateurs confirment des activités similaires), et monitoring renforcé post-éradication (l'attaquant essaiera probablement de revenir).

**La leçon centrale :** comprendre les acteurs est indispensable pour répondre. Sans la connaissance des profils APT par pays, l'analyste face à BLACKOUT ne sait pas interpréter le pré-positionnement OT (sabotage futur ? capacité de dissuasion ? reconnaissance ?), ne sait pas calibrer l'urgence de la réponse (un acteur qui prépare un sabotage nécessite une éradication immédiate ; un acteur en pré-positionnement stratégique peut justifier une phase de surveillance contrôlée), et ne sait pas qui alerter (le signalement ANSSI déclenche des processus différents selon que l'acteur est russe, chinois, ou inconnu). Un SOC ou un IR sans connaissance des APT est aveugle — c'est la raison d'être de ce cours.

---
