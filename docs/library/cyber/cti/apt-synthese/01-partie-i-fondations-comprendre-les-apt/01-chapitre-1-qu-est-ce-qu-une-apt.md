---
title: Chapitre 1 — Qu'est-ce qu'une APT
source: Cyber/01 CTI & renseignement/Menace cyber/APT — synthèse.md
note: APT — synthèse
up:
- - APT — synthèse
  - ../index.md
- - 'Partie I — Fondations : comprendre les APT'
  - index.md
---

## 1.1 Définition opérationnelle

Le terme APT (Advanced Persistent Threat) désigne un adversaire généralement state-sponsored ou state-aligned qui mène des cyberopérations sophistiquées, durables et ciblées. Chaque mot compte.

**Advanced** : l'adversaire dispose d'une capacité d'adaptation élevée, d'un tradecraft mature (OPSEC, évasion, persistence), de ressources conséquentes, et d'un renseignement préalable sur la cible. « Advanced » ne signifie pas forcément zero-day : beaucoup d'APT réussissent avec des credentials volés, des vulnérabilités connues non patchées, ou du Living off the Land. C'est la combinaison adaptation + OPSEC + ressources + mandat qui fait la différence.

**Persistent** : l'objectif n'est pas un coup unique mais un accès durable. L'adversaire investit dans la persistence (backdoors multiples, accès redondants, réinfection si éjecté). Le dwell time moyen (temps entre la compromission et la détection) se mesure en semaines à mois — et pour certaines opérations de pré-positionnement, en années.

**Threat** : c'est une menace intentionnelle, dirigée par des humains. Des opérateurs prennent des décisions en temps réel, adaptent leur approche, et ont des objectifs stratégiques définis par un commanditaire — un service de renseignement, un état-major militaire, ou un appareil gouvernemental.

## 1.2 APT vs cybercriminalité vs hacktivisme vs insider

| Critère | APT (étatique) | Cybercriminel | Hacktiviste | Insider |
|---------|:---:|:---:|:---:|:---:|
| Motivation | Espionnage, sabotage, influence, pré-positionnement | Profit financier | Idéologie, réputation | Vengeance, profit, négligence |
| Sponsor | État, proxy, contractor | Autonome ou groupe organisé | Groupe idéologique | Employé/contractant |
| Temporalité | Mois à années | Jours à semaines | Ponctuel | Variable |
| Sélection cibles | Très ciblé (secteur, organisation) | Opportuniste ou semi-ciblé | Symboles politiques | Leur propre organisation |
| OPSEC | Très élevé (furtivité maximale) | Variable | Faible à moyen | Variable |
| Tolérance au bruit | Très faible | Moyenne (smash & grab) | Haute (cherche la visibilité) | Variable |
| Critère de succès | Accès maintenu, données exfiltrées, effet stratégique | Monétisation | Impact médiatique | Dommage ou gain personnel |

Les frontières sont floues : APT41 mène à la fois de l'espionnage étatique et du cybercrime personnel. Les groupes ransomware russophones opèrent sous la tolérance tacite de l'État. La DPRK utilise le cybervol comme source de financement étatique. Ces zones grises sont traitées au Ch.15 et analysées au Ch.24.

## 1.3 Typologie d'objectifs APT

Le **cyberespionnage** est l'objectif le plus courant : vol de données stratégiques (propriété intellectuelle, plans militaires, communications diplomatiques, secrets commerciaux). Le **pré-positionnement** est l'objectif le plus inquiétant : maintenir un accès dormant dans des infrastructures critiques pour une activation future en cas de conflit (Volt Typhoon — Ch.22 et Ch.31). Le **sabotage** vise à endommager ou détruire des systèmes (NotPetya — $10 Mrd, Industroyer — blackouts Ukraine). L'**influence/désinformation** manipule l'opinion et déstabilise politiquement (ingérence électorale 2016, hack-and-leak). Et le **financement** génère des revenus pour contourner les sanctions (Lazarus — milliards volés en crypto — Ch.30).

## 1.4 Le vocabulaire terrain

Un **intrusion set** est un ensemble d'activités malveillantes regroupées par TTP, infrastructure et victimologie communes — c'est ce que les vendors appellent un « groupe APT », mais c'est un regroupement analytique, pas forcément une seule équipe physique. Un **cluster** (UNC chez Mandiant, DEV chez Microsoft historiquement) est un regroupement préliminaire pas encore attribué. Une **campaign** est une série d'intrusions liées par un objectif commun sur une période donnée. Les **TTP** (Tactics, Techniques, Procedures) décrivent le « comment » de l'attaquant — plus durables que les IoC. Le **tradecraft** est le savoir-faire opérationnel global de l'attaquant (OPSEC + TTP + habitudes).

## 1.5 Le naming chaos

Chaque éditeur CTI nomme les acteurs selon sa propre convention. CrowdStrike utilise des animaux par pays (Bear = Russie, Panda = Chine, Kitten = Iran, Chollima = DPRK, Spider = cybercrime). Microsoft utilise des phénomènes météo (Blizzard = Russie, Typhoon = Chine, Sandstorm = Iran, Sleet = DPRK, Tempest = cybercrime). Mandiant utilise APT/UNC/FIN. Résultat : APT28 = Fancy Bear = Forest Blizzard = Sofacy = Sednit — le même acteur avec 5+ noms. La navigation utilise Malpedia (base de données de référence avec les mappings croisés) et MITRE ATT&CK Groups. L'Annexe C fournit le tableau comparatif complet.

## 1.6 Fil rouge — BLACKOUT : le contexte

> **⚡ BLACKOUT — Épisode 1**
>
> L'alerte initiale vient du CERT mandaté : l'EDR a détecté un comportement anormal sur un poste d'ingénierie OT — un processus `rundll32.exe` chargeant une DLL non signée, avec un beaconing HTTPS régulier vers une IP aux Pays-Bas. Le parent process est un service légitime de l'application de supervision — la DLL a été placée dans son répertoire (DLL sideloading). Le CERT remonte la chaîne : l'infection initiale date de 6 semaines, via l'exploitation d'une vulnérabilité Ivanti. 6 semaines de présence non détectée. L'analyste CTI en charge doit répondre à la question : « qui est derrière ? ».

---
