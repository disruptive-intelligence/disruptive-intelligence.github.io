---
title: 'Fil rouge : Opération BLACKOUT'
source: Cyber/01_CTI/APT_vFULL.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - index.md
---

> **Contexte narratif — ce fil rouge traverse le cours et se conclut au Ch.32.**
> 
> Un **opérateur de distribution d’énergie européen** (4 pays, 6 200 collaborateurs, classé OIV en France, entité essentielle NIS 2) subit une compromission sophistiquée détectée par son CERT mandaté.
> 
> **L’intrusion** : l’attaquant a exploité une vulnérabilité sur un VPN Ivanti (CVE-2024-21887) pour pénétrer le réseau IT, établi la persistence via DLL sideloading dans le répertoire d’une application de supervision, s’est déplacé latéralement via PsExec et Kerberoasting, puis a pivoté vers le réseau de supervision SCADA via un poste d’ingénierie à double connexion. Il a été détecté et éjecté avant d’atteindre les automates — mais le positionnement était clairement orienté vers les systèmes de contrôle industriel.
> 
> **Le mystère** : aucune donnée exfiltrée, aucun ransomware, aucun sabotage. L’attaquant se pré-positionnait — mais pourquoi, et pour qui ? Les TTP observées sont compatibles avec plusieurs acteurs étatiques : Sandworm/GRU (patterns de beaconing similaires, ciblage énergie cohérent, contexte géopolitique russo-ukrainien), Volt Typhoon (exploitation d’appliance edge, LotL, pré-positionnement infra critique sans action), ou un cluster inconnu.
> 
> L’investigation traverse le cours à travers une dizaine d’épisodes — chacun placé là où il apporte une clé analytique réelle : identification des TTP, comparaison aux profils par pays, analyse du ciblage OT, processus d’attribution et calibration de la réponse, synthèse finale au Ch.32.

-----
