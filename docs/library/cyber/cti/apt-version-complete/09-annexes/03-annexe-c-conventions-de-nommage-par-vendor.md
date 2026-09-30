---
title: Annexe C — Conventions de nommage par vendor
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Annexes
  - index.md
---

Chaque vendor CTI utilise sa propre convention. La correspondance n’est jamais parfaite — deux vendors peuvent regrouper ou fragmenter les clusters différemment.

## C.1 Mandiant (Google Cloud)

- **APTxx** : groupes étatiques attribués. Ex : APT1, APT28, APT29, APT40, APT41.
- **UNCxxxx** : « Uncategorized » — clusters en analyse, pas encore promus. Ex : UNC2452 (cluster initial SolarWinds, devenu APT29), UNC4841 (Barracuda breach, Chine).
- **FINxx** : groupes financièrement motivés. Ex : FIN7, FIN8, FIN11.
- **TEMP.xxx** : préfixe temporaire historique. Ex : TEMP.Periscope (devenu APT40).

Promotion UNC → APT exige convergence de TTP, d’infrastructure et d’objectifs dans le temps.

## C.2 CrowdStrike — animaux par origine géographique

- **Bear** : Russie. Fancy Bear (APT28), Cozy Bear (APT29), Voodoo Bear (Sandworm), Venomous Bear (Turla), Energetic Bear (Dragonfly).
- **Panda** : Chine. Wicked Panda (APT41), Stone Panda (APT10), Judgment Panda (APT31), Vanguard Panda (Volt Typhoon).
- **Chollima** : DPRK. Stardust Chollima (APT38), Velvet Chollima (APT43), Silent Chollima (Andariel), Labyrinth Chollima.
- **Kitten** : Iran. Charming Kitten (APT35), Helix Kitten (APT34), Refined Kitten (APT33), Static Kitten (MuddyWater).
- **Buffalo** : Vietnam. OceanBuffalo (APT32).
- **Leopard** : Pakistan. Mythic Leopard (Transparent Tribe).
- **Tiger** : Inde.
- **Crane** : Corée du Sud.
- **Jackal** : hacktivisme.
- **Spider** : cybercrime. Scattered Spider, Wizard Spider.

## C.3 Microsoft — thèmes météo par origine

Refonte en 2023 — ancienne convention (éléments chimiques : NOBELIUM, STRONTIUM) abandonnée.

- **Blizzard** : Russie. Midnight Blizzard (APT29), Forest Blizzard (APT28), Seashell Blizzard (Sandworm), Aqua Blizzard (Gamaredon), Secret Blizzard (Turla).
- **Typhoon** : Chine. Volt Typhoon, Salt Typhoon, Flax Typhoon, Brass Typhoon (APT41), Silk Typhoon (Hafnium).
- **Sleet** : DPRK. Diamond Sleet (Lazarus), Sapphire Sleet (APT38), Emerald Sleet (Kimsuky), Onyx Sleet (Andariel).
- **Sandstorm** : Iran. Peach Sandstorm (APT33), Mint Sandstorm (APT35), Hazel Sandstorm (APT34), Mango Sandstorm (MuddyWater).
- **Storm-xxxx** : cybercrime non encore promu. Storm-0558, Storm-1516.
- **Tempest** : acteurs privés / PSO.
- **Flood** : DDoS hacktivisme.
- **Tsunami** : cybercrime sophistiqué.
- **Dust** : non attribué.

## C.4 Kaspersky

Nommage moins systématisé, souvent créatif : **Turla**, **Equation Group**, **BlueNoroff**, **ProjectSauron**, **Careto/The Mask**, **Sofacy** (APT28). Reflète l’histoire des découvertes.

## C.5 Secureworks — métaux par origine

- **Bronze** : Chine. Bronze Butler (Tick), Bronze President (Mustang Panda), Bronze Union (APT27).
- **Cobalt** : Russie et autres, parfois Iran. Cobalt Mirage (Iran).
- **Gold** : cybercrime.
- **Iron** : Iran (partiellement).
- **Tin** : DPRK.
- **Nickel** : autres.

## C.6 Palo Alto Networks / Unit 42

Nommage par nature plus descriptif, parfois par thématique :

- **Stately Taurus** = Mustang Panda.
- **Fighting Ursa** = APT28.
- **Mushroom Leviathan** = en lien avec APT40.
- Nommages plus variables.

## C.7 ESET

Nommage souvent simple, parfois hérité d’autres vendors. Publications avec focus technique marqué (Industroyer, Industroyer2, CaddyWiper, NightEagle).

## C.8 Correspondances pratiques pour l’analyste

Quand un rapport mentionne un nom inconnu :

- Rechercher sur **MITRE ATT&CK Groups** (`attack.mitre.org/groups/`) — la page de chaque groupe liste les alias connus.
- Rechercher sur **Malpedia** (`malpedia.caad.fkie.fraunhofer.de`) — base de données allemande qui consolide les correspondances.
- Consulter le **Thaicert APT Groups and Operations** (référence communautaire).
- Croiser 2-3 vendors sérieux (Mandiant, Microsoft, CrowdStrike) pour consolider la correspondance.

**Règle pratique** : noter systématiquement les alias Mandiant (APTxx) et Microsoft dans vos rapports — ce sont les deux conventions les plus largement partagées.

-----
