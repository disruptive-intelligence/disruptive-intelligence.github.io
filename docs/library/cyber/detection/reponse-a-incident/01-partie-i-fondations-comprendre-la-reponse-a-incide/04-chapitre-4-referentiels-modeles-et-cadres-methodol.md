---
title: Chapitre 4 — Référentiels, modèles et cadres méthodologiques
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie I — Fondations : comprendre la réponse à incident'
  - index.md
---

## 4.1 NIST SP 800-61 — le cadre de référence international

Le NIST Special Publication 800-61 (Computer Security Incident Handling Guide), publié par le National Institute of Standards and Technology américain, est le cadre de référence le plus largement adopté pour structurer la réponse à incident. Sa dernière révision majeure (Rev. 2) organise l'IR en quatre phases.

La **phase 1 — Preparation** couvre tout ce qui doit être en place avant l'incident : équipe, outils, processus, formation, exercices. Le NIST insiste sur le fait que la qualité de la réponse est directement proportionnelle à la qualité de la préparation — un constat que la Partie II de ce cours développe en 6 chapitres.

La **phase 2 — Detection & Analysis** couvre la détection de l'incident, sa confirmation, sa classification, sa notification aux parties prenantes, et l'analyse initiale. Le NIST distingue les vecteurs d'attaque (email, web, media amovible, attrition, etc.) et fournit des indicateurs de classification.

La **phase 3 — Containment, Eradication & Recovery** regroupe trois activités que d'autres cadres séparent. Le confinement stoppe la progression de l'attaquant. L'éradication supprime les mécanismes de compromission. La récupération restaure les systèmes à un état sûr. Le NIST reconnaît que ces trois activités sont souvent itératives et parallèles.

La **phase 4 — Post-Incident Activity** couvre le retour d'expérience, la capitalisation, et l'amélioration continue.

**Forces du NIST 800-61 :** structurant, adopté mondialement, applicable à toutes tailles d'organisation, régulièrement mis à jour. **Limites :** très conceptuel (peu de détails techniques opérationnels), centré contexte américain (les obligations réglementaires européennes ne sont pas couvertes), et pas de traitement explicite de la dimension « crise » (la gouvernance exécutive, la communication de crise, et la pression médiatique ne sont pas dans le périmètre du document).

## 4.2 SANS PICERL — les 6 phases

Le modèle SANS (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned) est plus granulaire que le NIST sur la distinction entre Containment, Eradication et Recovery — trois phases que le NIST regroupe. Cette granularité est utile pédagogiquement et opérationnellement : les trois phases mobilisent des compétences, des outils, et des temporalités différentes.

Le modèle SANS est la base des formations SANS les plus reconnues en IR : FOR508 (Advanced Incident Response, Threat Hunting, and Digital Forensics), FOR500 (Windows Forensic Analysis), et FOR578 (Cyber Threat Intelligence). Il est profondément ancré dans la communauté des praticiens.

**Limite principale :** la linéarité implicite du modèle (P→I→C→E→R→L) ne reflète pas la réalité itérative de l'IR. En pratique, on revient constamment en arrière : on identifie de nouveaux systèmes compromis pendant l'éradication (retour à l'identification), on découvre de nouvelles persistances pendant la recovery (retour à l'éradication), et les lessons learned commencent dès les premières heures de l'incident (pas seulement après la clôture).

## 4.3 ISO 27035 — le cadre normatif

La norme ISO 27035 (Information Security Incident Management), en trois parties, fournit un cadre formel pour la gestion des incidents dans un contexte de système de management de la sécurité de l'information (SMSI) conforme à ISO 27001. Elle est plus structurée sur la gouvernance et la documentation que les cadres NIST/SANS, mais moins technique.

ISO 27035 est pertinente pour les organisations certifiées ISO 27001 qui doivent intégrer la gestion des incidents dans leur SMSI, et pour les organisations qui ont besoin d'un cadre normatif reconnu pour justifier leur approche auprès d'auditeurs ou de régulateurs.

## 4.4 Cadre ANSSI, CERT-FR et PRIS

Le cadre français de la réponse à incident s'articule autour de plusieurs composantes.

L'**ANSSI** (Agence Nationale de la Sécurité des Systèmes d'Information) est l'autorité nationale en matière de cybersécurité. Elle opère le **CERT-FR**, qui fournit un service de réponse aux incidents pour les administrations et les OIV, publie des avis de sécurité et des alertes, et coordonne la réponse aux incidents d'ampleur nationale. Le CERT-FR peut déployer des équipes spécialisées (notamment en environnement OT/SCADA) en appui des organisations victimes.

Le référentiel **PRIS** (Prestataires de Réponse aux Incidents de Sécurité) définit les exigences de qualification pour les prestataires d'IR. La version 3.2, publiée en octobre 2025, couvre désormais cinq activités qualifiables : recherche d'indicateurs de compromission, investigation numérique (forensic), analyse de codes malveillants, pilotage et coordination des investigations, et — nouveauté de la v3.2 — gestion de crise d'origine cyber. Cette dernière activité, ajoutée après un appel à commentaires terminé en mai 2025, permet à l'ANSSI de délivrer des qualifications attestant la capacité d'un prestataire à gérer la dimension crise (pas seulement la dimension technique) d'un incident cyber.

Les **obligations de notification** dans le cadre français sont multiples. Les OIV (Opérateurs d'Importance Vitale) doivent notifier l'ANSSI dans les délais prescrits par les arrêtés sectoriels. La directive NIS 2, en cours de transposition en France via la « Loi relative à la résilience des infrastructures critiques et au renforcement de la cybersécurité » (dite « Loi Résilience ») — adoptée en commission spéciale à l'Assemblée nationale en septembre 2025, promulgation attendue début 2026 —, imposera des obligations de notification aux entités essentielles (notification initiale sous 24h, notification complète sous 72h) et aux entités importantes. Le périmètre est considérablement élargi par rapport à NIS 1 : environ 15 000 entités seront concernées en France, contre quelques centaines sous le régime actuel.

L'articulation avec les **forces de l'ordre** passe par le dépôt de plainte auprès du procureur de la République, qui peut être traité par l'OCLCTIC (Office Central de Lutte contre la Criminalité liée aux Technologies de l'Information et de la Communication), le C3N (Centre de lutte Contre les Criminalités Numériques, Gendarmerie), la BL2C (Brigade de Lutte contre la Cybercriminalité, Préfecture de Police de Paris), ou la JUNALCO (Juridiction Nationale de Lutte contre la Criminalité Organisée, parquet de Paris — section J3 cybercriminalité).

## 4.5 Kill Chain, Diamond Model et ATT&CK comme outils d'investigation

Ces cadres ne sont pas des « modèles IR » au sens de NIST ou SANS — ce sont des outils que l'investigateur utilise pendant la réponse pour structurer ses observations et ses hypothèses.

La **Cyber Kill Chain** (Lockheed Martin) structure le raisonnement sur la progression de l'attaque en 7 étapes (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives). Elle est utile pour situer l'attaque dans son cycle de vie : si l'attaquant en est à « Actions on Objectives » (exfiltration, chiffrement), c'est qu'il a traversé toutes les étapes précédentes — et l'investigation doit les reconstituer.

Le **Diamond Model** (adversary, capability, infrastructure, victim) structure le raisonnement sur l'attribution et le contexte. Pour chaque événement de l'intrusion, l'analyste identifie l'adversaire (qui ?), la capacité utilisée (quel outil, quelle technique ?), l'infrastructure employée (quel C2, quel hébergement ?), et la victime ciblée (quel système, quelle donnée ?).

La **matrice MITRE ATT&CK** fournit un vocabulaire commun pour décrire les TTP (Tactics, Techniques, and Procedures) observées pendant l'investigation. Chaque étape du chemin d'attaque est mappée sur les tactiques ATT&CK (Initial Access, Execution, Persistence, etc.), ce qui normalise le rapport, facilite le partage avec la communauté, et oriente la remédiation (pour chaque technique utilisée : quelle détection ou quelle mesure préventive aurait pu la contrer ?).

## 4.6 Intérêt et limites des modèles

Aucun modèle ne reflète fidèlement la réalité d'un incident majeur. Les phases ne sont pas séquentielles mais itératives et parallèles : on contient pendant qu'on investigue, on investigue pendant qu'on éradique, on découvre de nouveaux problèmes pendant la reconstruction. L'incident avance sur plusieurs fronts simultanément, et les « phases » des modèles sont des repères intellectuels pour structurer la pensée, pas des check-lists rigides à suivre dans l'ordre.

Le danger des modèles est de créer une illusion de contrôle linéaire. L'analyste qui pense « je suis en phase de Containment, donc je ne fais pas d'Eradication » se trompe — si une opportunité d'éradiquer se présente pendant le confinement (par exemple, un mécanisme de persistance trivial à supprimer), il serait absurde de ne pas la saisir sous prétexte que « ce n'est pas la bonne phase ».

Les modèles doivent être connus, intériorisés, puis adaptés au contexte. Ils sont des garde-fous contre l'oubli (« avons-nous pensé aux lessons learned ? ») et des outils de communication (« nous sommes en phase de Containment, voici ce que cela signifie »), pas des carcans.

## 4.7 Fil rouge — BLACKTIDE : le cadre opérationnel

> **🔍 BLACKTIDE — Épisode 4**
>
> L'équipe IR d'Arvantis utilise le NIST 800-61 comme référence procédurale. L'IRP interne reprend les 4 phases NIST et les décline en actions concrètes. Le mapping ATT&CK est utilisé comme grille de lecture des TTP observées au fil de l'investigation — chaque technique identifiée est documentée avec son ID ATT&CK dans le journal d'incident.
>
> Le prestataire PRIS sous contrat, CyberForce, utilise son propre cadre méthodologique (basé sur SANS PICERL), compatible avec le cadre interne d'Arvantis. L'articulation a été définie contractuellement : CyberForce apporte l'expertise forensic et l'expérience d'incidents similaires, l'équipe interne apporte la connaissance du SI et du contexte métier. L'IR lead reste Nadia (interne) — le consultant senior de CyberForce est en support, pas en pilotage.
>
> L'ANSSI est notifiée à 08h00 (obligation OIV — site de Fos-sur-Mer). Le CERT-FR accuse réception et propose un appui : déploiement d'une équipe spécialisée OT pour auditer le réseau SCADA de Fos, prévu pour lundi.

---
