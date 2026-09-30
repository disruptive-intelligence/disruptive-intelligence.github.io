---
title: 'Chapitre 6 — Russie : les groupes APT en détail'
source: Cyber/01_CTI/APT_Synthese.md
note: APT — synthèse
up:
- - APT — synthèse
  - ../index.md
- - Partie II — Russie
  - index.md
---

## 6.1 APT29 / Cozy Bear / Midnight Blizzard (SVR)

**Mission :** espionnage stratégique de haut niveau — gouvernements occidentaux, diplomatie, think tanks, grandes entreprises technologiques. **TTP dominants :** supply chain (SolarWinds/SUNBURST — backdoor dans le build process), phishing OAuth ciblé (emails imitant des invitations de collaboration Microsoft Teams), abus Azure AD/M365 (manipulation de tokens SAML — GoldenSAML, exploitation OAuth), credential spray (Azure AD à grande échelle), malware custom sophistiqué (EnvyScout — dropper HTML, BoomBox — downloader, NativeZone — loader, FoggyWeb — backdoor ADFS). **OPSEC :** très élevé. Infrastructure compartimentée (chaque cible a sa propre infrastructure C2), C2 via services légitimes (Azure, AWS, Slack), minimal footprint (peu de fichiers déposés, exécution en mémoire). **Campagnes majeures :** SolarWinds (2020 — supply chain, ~18 000 organisations touchées, ~100 cibles activement exploitées), Microsoft corporate breach (2023-2024 — password spray → compromission des emails de dirigeants Microsoft), campagnes de phishing diplomatiques continues (ciblant les ambassades, les ministères des affaires étrangères en Europe).

## 6.2 APT28 / Fancy Bear / Forest Blizzard (GRU Unit 26165)

**Mission :** espionnage militaire et politique + opérations d'influence. **TTP dominants :** spear-phishing (macros Word, faux portails de login OAuth), exploitation de vulnérabilités (0-days Outlook — CVE-2023-23397, exploitation de serveurs Exchange), credential harvesting (fausses pages de login, password spraying), outils custom (X-Tunnel, XAgent, Zebrocy), et Mimikatz pour le credential dumping. **OPSEC :** moyen à élevé — plus bruyant que le SVR. **Campagnes majeures :** DNC hack 2016 (vol et publication des emails → ingérence électorale), WADA 2016 (vol et publication de données anti-dopage), Bundestag 2015 (compromission du réseau du parlement allemand), campagnes anti-OTAN continues, exploitation CVE-2023-23397 Outlook (2023 — ciblage systématique des organisations européennes).

## 6.3 Sandworm / Seashell Blizzard (GRU Unit 74455)

**Mission :** opérations destructrices et sabotage — le bras armé du cyber russe. **TTP dominants :** wipers (NotPetya, CaddyWiper, HermeticWiper, IsaacWiper), attaques OT/ICS (Industroyer/CrashOverride — manipulation directe des protocoles industriels IEC 104/IEC 61850), supply chain (M.E.Doc pour NotPetya), exploitation d'edge devices (Cyclops Blink — botnet sur routeurs ASUS/WatchGuard). **Particularité :** Sandworm est le seul groupe APT à avoir causé des pannes d'électricité confirmées par cyberattaque — Ukraine 2015 (BlackEnergy/KillDisk, 230 000 foyers, 6h) et 2016 (Industroyer, Kiev, 1h). En 2022, la tentative Industroyer2 a été déjouée par le CERT-UA et ESET. **Note :** WhisperGate (2022) est attribué à GRU Unit 29155, pas à Sandworm/Unit 74455. **Campagnes majeures :** NotPetya (2017 — wiper mondial, $10+ Mrd), Olympic Destroyer (2018 — false flags Lazarus), Ukraine 2022-présent (multiple wipers, tentative Industroyer2).

## 6.4 Turla / Snake / Secret Blizzard (FSB Centre 16)

**Mission :** espionnage long terme contre des cibles gouvernementales et diplomatiques de haute valeur. **TTP :** malware ultra-sophistiqué (Snake — rootkit multi-plateforme actif depuis 2003, LightNeuron — backdoor Exchange, Kazuar — backdoor modulaire), infrastructure complexe (réseau de proxys par satellite pour masquer le C2), et technique unique de détournement d'infrastructure d'autres groupes APT (Turla a été observé en train de « pirater les pirates » — utiliser l'infrastructure de groupes iraniens pour mener ses propres opérations). Considéré comme l'un des groupes les plus techniquement avancés au monde. **Snake a été démantelé par le FBI en 2023** (opération Medusa — injection de commandes dans le malware pour le désactiver sur les machines infectées).

## 6.5 Gamaredon / Aqua Blizzard (FSB Centre 18)

**Mission :** ciblage massif de l'Ukraine. **TTP :** volume élevé, sophistication moindre que les autres groupes russes — phishing de masse, templates VBA, infrastructure Telegram pour le C2, persistence agressive (réinfection rapide après éradication). Gamaredon est le « marteau » là où Turla est le « scalpel ».

---
