---
title: 'Chapitre 7 — Russie : campagnes de référence et influence'
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - ../index.md
- - Partie II — Russie
  - index.md
---

## 7.1 SolarWinds / SUNBURST (2020)

La campagne de supply chain la plus sophistiquée documentée. L'APT29/SVR a compromis le processus de build de SolarWinds Orion, injecté la backdoor SUNBURST dans les mises à jour légitimes (versions 2019.4 HF 5 à 2020.2.1 HF 1), et touché ~18 000 organisations. Environ 100 cibles de haute valeur ont été activement exploitées (Trésor US, Département d'État, Commerce, Microsoft). Les TTP post-compromission incluaient le forgeage de tokens SAML (GoldenSAML) pour accéder à Azure AD/O365 sans credentials, et l'accès massif aux boîtes mail via Graph API. Signaux observables : requêtes DNS vers avsvmcloud[.]com avec sous-domaines encodés, processus fils inhabituels de SolarWinds.BusinessLayerHost.exe, événements ADFS anormaux. Leçons : la confiance dans un fournisseur ne dispense pas de monitorer son comportement réseau, le monitoring du plan de contrôle identity (SAML, OAuth) est devenu indispensable.

## 7.2 NotPetya (2017)

Le wiper le plus destructeur de l'histoire. Distribué via une mise à jour piégée du logiciel comptable ukrainien M.E.Doc (supply chain). Se propageait via EternalBlue + Mimikatz. Ressemblait à un ransomware (demande de rançon affichée) mais était un wiper (la clé n'existait pas — false flag). Impact mondial non anticipé : Maersk (reconstruction complète du SI en 10 jours, 45 000 postes), Merck ($870M de pertes), FedEx/TNT ($400M), Saint-Gobain ($220M). Total : $10+ Mrd de dégâts mondiaux. Attribution à Sandworm/GRU par les Five Eyes en 2018. Contexte DIMEFIL : Military (appui au conflit Ukraine), Economic (déstabilisation économique).

## 7.3 Industroyer (2016) — sabotage du réseau électrique

Industroyer/CrashOverride est le malware le plus avancé conçu pour cibler les systèmes de contrôle industriel (ICS). Il manipule directement les protocoles industriels (IEC 104, IEC 61850, OPC DA) pour envoyer des commandes aux automates de distribution électrique. Déployé par Sandworm contre le réseau électrique ukrainien le 17 décembre 2016, il a causé un blackout d'environ 1 heure dans la région de Kiev. L'analyse de ce malware et le traitement approfondi des attaques OT sont développés dans la Partie VI.

## 7.4 Opérations d'influence russes

L'**Internet Research Agency** (IRA), basée à Saint-Pétersbourg, est la ferme à trolls qui a manipulé les réseaux sociaux US/UE avec des faux comptes, de la polarisation, et de la désinformation — active depuis au moins 2013. Le modèle russe combine cyberespionnage (le GRU vole les données — emails DNC), publication via des intermédiaires (DCLeaks, Guccifer 2.0, WikiLeaks), et amplification par l'IRA (faux comptes qui relaient et commentent). C'est l'approche intégrée espionnage + influence + désinformation la plus documentée au monde. L'ingérence dans les élections US 2016 reste le cas d'école : APT28/GRU a volé et publié les emails du DNC, l'IRA a amplifié les narratifs polarisants, et l'effet combiné a eu un impact mesurable sur le débat public.

## 7.5 Fil rouge — BLACKOUT : comparaison avec les profils russes

> **⚡ BLACKOUT — Épisode 3**
>
> Camille (l'analyste CTI en charge) compare les TTP de BLACKOUT avec les profils russes. Les patterns de beaconing (intervalles de 32 minutes avec jitter de 10 %) sont similaires à ceux documentés par ESET sur Sandworm/CaddyWiper (2022). La victimologie (opérateur d'énergie européen) est cohérente avec le ciblage Sandworm. Le pivot vers l'OT est une signature Sandworm. Mais l'exploitation d'Ivanti et l'absence de malware custom sont atypiques pour Sandworm (qui utilise typiquement des outils custom — Industroyer, CaddyWiper). L'hypothèse Sandworm/GRU est posée comme H1 avec confiance modérée.

---
