---
title: Partie IV — Corée du Nord, Iran et autres acteurs
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

---


## Chapitre 11 — DPRK : contexte, groupes et modèle unique

### 11.1 Le cyber comme source de revenus

La DPRK est un cas unique : c'est le seul État qui utilise le cyber principalement comme source de revenus pour contourner les sanctions internationales. Le RGB (Reconnaissance General Bureau) est le service de renseignement militaire qui supervise les opérations cyber. Les opérateurs sont formés dans des programmes dédiés et souvent stationnés à l'étranger (Chine, Russie, Asie du Sud-Est) pour des raisons de connectivité et d'OPSEC.

**Lazarus Group / Diamond Sleet** : le plus polyvalent — vol de cryptomonnaies (Ronin Network $620M, Bybit ~$1,5 Mrd), supply chain (3CX 2023), social engineering sophistiqué sur LinkedIn (Opération Dream Job — fausses offres d'emploi ciblant les développeurs), et malware multi-plateforme (Windows, macOS, Linux). **APT38 / BlueNoroff / Sapphire Sleet** : spécialisation finance — braquages SWIFT (Bangladesh Bank 2016 — $81M), ciblage des exchanges de cryptomonnaies, et des protocoles DeFi. **Kimsuky / Emerald Sleet** : espionnage diplomatique et nucléaire — credential harvesting ciblant des chercheurs, diplomates, think tanks spécialisés sur la péninsule coréenne. **APT43 / Velvet Chollima** : ciblage académique et think tanks.

Les **opérateurs IT DPRK** sont un phénomène unique : des milliers de nord-coréens travaillent sous de fausses identités comme développeurs freelance dans des entreprises occidentales, générant des revenus (estimés à $300M+/an par le gouvernement US) qui financent le régime. Ils utilisent des identités volées, des VPN, et des intermédiaires pour masquer leur nationalité.

---


## Chapitre 12 — DPRK : campagnes de référence

**WannaCry (2017)** : ransomware worm exploitant EternalBlue, propagation mondiale (200 000+ systèmes dans 150 pays), NHS britannique paralysé. Attribution à Lazarus par la NSA, le GCHQ, et le FBI. Le ransomware a généré peu de revenus ($140 000 en Bitcoin) mais causé des milliards de dégâts. Leçon : la DPRK est prête à causer des dommages collatéraux massifs.

**Bangladesh Bank (2016)** : APT38 a compromis le terminal SWIFT de la banque centrale du Bangladesh et transféré $81M vers des comptes aux Philippines. $951M supplémentaires ont été bloqués grâce à une faute de frappe dans un ordre de virement (« fandation » au lieu de « foundation »). Premier braquage bancaire majeur par un acteur étatique via le cyber.

**3CX supply chain (2023)** : Lazarus a compromis la chaîne de build du logiciel de communication VoIP 3CX (600 000+ clients) — le supply chain d'un supply chain (la compromission initiale venait d'un logiciel de trading compromis). TTP similaires à SolarWinds mais avec un acteur différent.

**Vols de cryptomonnaies massifs** : Ronin Network $620M (2022), Harmony Bridge $100M (2022), Atomic Wallet $100M (2023), Bybit ~$1,5 Mrd (2025 — le vol de crypto le plus important de l'histoire, attribué par le FBI). Le cumul est estimé entre $3 et $6 Mrd. Ces fonds financent le programme nucléaire et balistique nord-coréen — le cyber comme arme de prolifération. Les mécanismes de blanchiment (mixeurs — Tornado Cash sanctionné par l'OFAC, ponts cross-chain, mules) évoluent en permanence.

---


## Chapitre 13 — Iran : contexte et groupes APT

Priorités : rivalités régionales (Golfe, Israël), surveillance des dissidents, sabotage ponctuel, influence chiite. Structure : MOIS/VAJA (renseignement civil — APT34, MuddyWater) et IRGC (Gardiens de la Révolution — APT33, APT35, APT42).

**APT33 / Peach Sandstorm (IRGC)** : énergie, aérospatial, pétrochimie. Password spraying massif, backdoors custom. **APT34 / OilRig / Hazel Sandstorm (MOIS)** : gouvernements Moyen-Orient, finance, énergie. DNS tunneling, webshells, credential harvesting. **APT35 / Charming Kitten / Mint Sandstorm (IRGC)** : social engineering ultra-ciblé — faux profils LinkedIn, impersonation de journalistes et d'universitaires, ciblage de chercheurs, dissidents, et opposants politiques. Le social engineering d'APT35 est considéré comme le plus sophistiqué au monde dans la catégorie « impersonation individuelle ». **APT42 / Calanque (IRGC-IO)** : surveillance ciblée, credential harvesting, opérations contre des cibles spécifiques de l'IRGC. **MuddyWater / Mango Sandstorm (MOIS)** : gouvernements et télécoms Moyen-Orient/Asie, PowerShell obfusqué, outils open source.

Le cyber iranien est croissant mais moins sophistiqué que la Russie et la Chine. Sa spécificité : les opérations destructives ponctuelles (wipers) comme substitut/complément aux opérations conventionnelles en période de tension régionale.

---


## Chapitre 14 — Iran : campagnes de référence

**Stuxnet (2010)** est traité ici sous l'angle du catalyseur : l'attaque US/Israël contre les centrifugeuses nucléaires iraniennes a détruit ~1 000 centrifugeuses et retardé le programme de 2-3 ans, mais elle a aussi catalysé le développement des capacités cyber iraniennes. L'Iran a répondu en investissant massivement dans son programme cyber offensif — Shamoon, développé 2 ans après Stuxnet, est la réponse iranienne. Stuxnet est aussi traité au Ch.18 (Israël) et au Ch.21 (OT/ICS).

**Shamoon v1/v2/v3 (2012-2018)** : wipers déployés contre Saudi Aramco (30 000 postes détruits en 2012 — l'un des incidents les plus destructeurs de l'histoire) et le secteur pétrolier. Attribution à APT33/Iran. Message : « si vous nous attaquez (Stuxnet), nous pouvons frapper votre industrie ».

**Opérations contre l'Albanie (2022)** : wipers et ransomware déployés contre les systèmes gouvernementaux albanais après que l'Albanie a hébergé un groupe d'opposition iranien (MEK). L'Albanie a rompu les relations diplomatiques avec l'Iran — premier cas de rupture diplomatique pour cause de cyberattaque.

---


## Chapitre 15 — Autres acteurs étatiques et zones grises

### 15.1 Acteurs régionaux documentés

**Vietnam — OceanLotus / APT32** : espionnage régional (ASEAN, dissidents vietnamiens, entreprises), sophistication croissante, macOS et mobile. **Pakistan — SideCopy, Transparent Tribe** : ciblage quasi exclusif de l'Inde (gouvernement, défense). **Turquie — Sea Turtle** : détournement DNS ciblant le Moyen-Orient et l'Europe (registrars compromis). **Amérique latine — Blind Eagle / APT-C-36** : ciblage régional (Colombie, Équateur).

### 15.2 Mercenaires cyber / PSO (Private Sector Offensive)

**NSO Group** (Israël — Pegasus) : spyware mobile exploitant des zero-days iOS/Android, vendu à des États pour la surveillance. Révélé par Citizen Lab et le consortium Pegasus Project (2021). Utilisé contre des journalistes, dissidents, opposants politiques, et même des chefs d'État. **Intellexa** (consortium européen — Predator) : concurrent de NSO, spyware similaire. **Candiru** (Israël) : spyware ciblant les navigateurs et les systèmes desktop.

Pourquoi la CTI les documente : leurs outils apparaissent dans les campagnes d'espionnage étatique — l'analyste qui identifie un spyware Pegasus sait que le commanditaire est un client étatique de NSO, pas un cybercriminel. Les régulations émergentes : Pall Mall Process, restrictions d'exportation, moratorium proposé par l'UE.

### 15.3 Zones grises crime-État

APT41 (double casquette espionnage/cybercrime), groupes ransomware russophones (tolérance étatique), DPRK (le vol de crypto est du cybercrime par la méthode, de l'action étatique par la finalité), et les hacktivistes instrumentalisés (KillNet, NoName057(16) — hacktivisme pro-russe avec des liens possibles avec les services, IT Army of Ukraine — coordination étatique d'un mouvement de volontaires).

---
