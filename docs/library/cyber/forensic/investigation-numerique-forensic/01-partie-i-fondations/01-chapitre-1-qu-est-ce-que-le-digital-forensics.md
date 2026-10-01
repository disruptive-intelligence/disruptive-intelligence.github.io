---
title: Chapitre 1 — Qu'est-ce que le digital forensics
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 1.1 Définition : science de la preuve numérique

Le digital forensics — ou investigation numérique — est la discipline scientifique qui consiste à identifier, préserver, collecter, analyser et présenter des preuves numériques de manière à ce qu'elles soient recevables devant un tribunal ou exploitables pour une décision stratégique. Le mot clé est « scientifique » : le forensic n'est pas du bricolage technique, c'est un processus rigoureux, reproductible et documenté.

Le forensic numérique répond à des questions fondamentales : que s'est-il passé, quand, comment, par qui, et quelles données ont été impactées. Ces questions sont les mêmes qu'en criminalistique physique (qui a commis l'acte, avec quel outil, où, quand), transposées au monde numérique. Et comme en criminalistique physique, la qualité de la collecte de preuves détermine la qualité des conclusions. Un disque mal acquis, un log non préservé, un dump mémoire raté : autant de scènes de crime contaminées dont les conclusions seront contestables.

La particularité du numérique est la volatilité : contrairement à une empreinte digitale sur une poignée de porte, une connexion réseau disparaît quand le processus se termine, un fichier supprimé peut être écrasé par le système d'exploitation en quelques minutes sur un SSD, et un redémarrage de machine efface la mémoire vive avec tout ce qu'elle contenait — credentials en clair, processus malveillants, connexions C2 actives. L'urgence de la préservation est la contrainte fondamentale du forensic numérique.

## 1.2 Forensic ≠ incident response ≠ pentest ≠ threat intel

Le forensic s'inscrit dans un écosystème plus large de cybersécurité, et les confusions de posture entre disciplines sont fréquentes et dommageables.

Le **digital forensics** cherche à comprendre ce qui s'est passé et à produire des preuves exploitables. Son tempo est long (jours à semaines), sa contrainte clé est l'intégrité des preuves et la rigueur méthodologique. L'**incident response** cherche à contenir l'attaque, éradiquer la menace, et restaurer le service. Son tempo est court (heures à jours), sa contrainte clé est la rapidité et la continuité d'activité. Le **pentest / red team** cherche à trouver les vulnérabilités avant les attaquants. Son tempo est planifié (semaines), sa contrainte est le périmètre autorisé. La **threat intelligence** cherche à comprendre les menaces, les acteurs, et les tendances. Son tempo est continu, sa contrainte est la qualité des sources et la prudence de l'attribution.

En pratique, ces disciplines interagissent constamment. Le SOC détecte une alerte, l'IR qualifie et contient, le forensic investigue en profondeur, et la CTI contextualise (quel groupe, quelles TTP, quel objectif). Le forensic peut aussi intervenir hors incident : investigation sur un employé suspect (insider threat), due diligence lors d'une acquisition d'entreprise, analyse d'un litige commercial (preuve de suppression de fichiers), ou expertise judiciaire ordonnée par un magistrat.

Le cours IR de la bibliothèque traite de l'orchestration de la réponse ; le cours CTI/Écosystèmes traite de la contextualisation de la menace. Ce cours traite de l'investigation technique et de la production de preuves.

## 1.3 Les branches du forensic

Le forensic numérique se décline en plusieurs spécialités, chacune avec ses artefacts, ses outils et ses contraintes. Ces spécialités ne sont pas cloisonnées — une investigation complète les combine presque toujours.

Le **disk forensics** (analyse de supports de stockage) est la branche historique : acquisition bit-à-bit d'un disque, analyse du système de fichiers, récupération de fichiers supprimés, analyse des métadonnées et des artefacts système. C'est le socle du cours (Parties II-IV). Le **memory forensics** (analyse de mémoire vive) capture l'état instantané du système — processus, connexions, credentials, malware fileless. C'est devenu incontournable avec la montée des attaques sans fichier (Ch.17). Le **network forensics** (analyse réseau) examine les captures de trafic et les logs réseau pour reconstituer les communications de l'attaquant et caractériser l'exfiltration (Ch.19). Le **mobile forensics** analyse les smartphones et tablettes — terminaux qui contiennent souvent plus de données exploitables qu'un PC, mais avec des protections renforcées (Ch.23). Le **cloud forensics** investigue dans les environnements cloud (AWS, Azure, GCP, M365) avec des défis spécifiques : pas d'accès physique, données éphémères, multi-juridiction (Ch.21). Le **malware forensics** analyse le comportement d'un malware pour comprendre ses fonctionnalités et extraire les IoC, sans aller jusqu'au reverse engineering complet (Ch.18).

## 1.4 La tension fondamentale : forensic judiciaire vs triage DFIR

C'est la distinction la plus structurante du cours, et elle conditionne chaque décision que l'analyste prendra sur le terrain.

Le **forensic judiciaire** vise à produire des preuves recevables devant un tribunal. L'exhaustivité prime sur la rapidité : chaque élément de preuve est acquis dans le respect de la chaîne de custody, hashé, documenté, et traçable. L'intégrité est absolue. Le tempo est long (jours à semaines). Le destinataire est un juge, un expert contradictoire, ou un procureur.

Le **triage DFIR** vise à comprendre rapidement ce qui se passe pour contenir la menace et éradiquer l'attaquant. La rapidité prime sur l'exhaustivité : on collecte les artefacts les plus parlants sur les machines les plus critiques, on analyse en parallèle, on produit des IoC pour le SOC. Le tempo est court (heures à jours). Le destinataire est l'IR lead, le SOC, et le RSSI.

En pratique, ces deux régimes ne s'excluent pas — ils s'articulent. La plupart des investigations commencent en mode triage (comprendre l'urgence) et basculent en mode judiciaire si les constatations le justifient (vol de données avéré, fraude, attaque étatique). Savoir quand et comment basculer est une compétence critique : le triage initial ne doit pas compromettre les preuves nécessaires à la judiciarisation. C'est pourquoi, même en triage, les bonnes pratiques de chaîne de custody et de hashing doivent être respectées dès le début — on ne sait jamais si l'affaire finira devant un juge.

Trois axes de tension traversent toute investigation : rapidité vs exhaustivité (collecter 80 % en 2 heures ou 100 % en 2 jours), continuité d'activité vs gel des preuves (laisser la machine en production ou la saisir), et investigation interne vs perspective judiciaire (souplesse méthodologique vs procédure stricte, scellés, expert judiciaire).

## 1.5 Qui fait du forensic

Les acteurs du forensic sont variés. Les **CERT/CSIRT** (Computer Emergency Response Teams) combinent IR et forensic — en France, le CERT-FR (ANSSI) pour l'État et les OIV, les CSIRT sectoriels (santé, finance), et les CSIRT d'entreprise. Les **SOC** font du triage de premier niveau — qualification d'alertes, collecte initiale d'artefacts. Les **forces de l'ordre spécialisées** mènent les investigations judiciaires : le C3N (Centre de lutte contre les criminalités numériques, Gendarmerie), l'OCLCTIC (Office central de lutte contre la criminalité liée aux TIC), les ICC (Investigateurs en cybercriminalité) répartis dans les brigades territoriales, et la BL2C (Brigade de Lutte contre la Cybercriminalité, Préfecture de Police de Paris). Les **cabinets privés** et prestataires qualifiés PRIS interviennent pour des investigations internes, des due diligences, ou en appui des entreprises victimes. Les **experts judiciaires**, inscrits sur les listes des cours d'appel, sont mandatés par les magistrats pour les expertises contradictoires.

## 1.6 Le forensic dans la chaîne cybersécurité

Le forensic s'insère dans une chaîne plus large : détection (le SOC identifie une alerte via le SIEM ou l'EDR) → qualification (l'analyste SOC confirme le vrai positif et évalue la gravité) → triage/investigation (l'équipe DFIR collecte les artefacts et analyse) → remédiation (éradication de la menace, restauration, durcissement) → judiciarisation éventuelle (dépôt de plainte, expertise judiciaire). Le forensic intervient principalement dans la phase triage/investigation, mais il prépare aussi la judiciarisation et alimente la remédiation. Le cours IR de la bibliothèque détaille l'ensemble de cette chaîne ; ce cours se concentre sur la phase forensic.

## 1.7 Fil rouge — MUSIC BOX : l'alerte

> **🔬 MUSIC BOX — Épisode 1**
>
> Vendredi 7 mars 2026, 17h12. L'EDR déclenche sur le poste WKS-RD-047 (Windows 11, département R&D, utilisateur : Dr. Julien Mallet, chercheur principal sur la molécule NP-427). Alerte : « Process svchost.exe (PID 7284, parent: explorer.exe) attempting to access LSASS memory ».
>
> Romain (SOC) vérifie : svchost.exe avec explorer.exe comme parent est anormal — les svchost légitimes ont services.exe comme parent. L'accès à LSASS est un indicateur de credential dumping (T1003). C'est un vrai positif.
>
> Première décision : triage rapide ou investigation complète ? Claire (IR lead) tranche : triage immédiat pour évaluer la gravité (dump RAM du poste suspect, collecte des artefacts KAPE, vérification des connexions sortantes via le proxy). La machine n'est PAS éteinte, PAS isolée du réseau immédiatement — on veut d'abord comprendre avec qui elle communique. En parallèle, préservation de la chaîne de custody dès le début : l'experte judiciaire Maître Fournier est contactée et sera sur site samedi matin.
>
> La bascule vers une investigation complète sera décidée lundi, selon les premiers résultats. Mais la préservation des preuves commence maintenant — on ne sait pas encore si cette affaire finira devant un juge.

---
