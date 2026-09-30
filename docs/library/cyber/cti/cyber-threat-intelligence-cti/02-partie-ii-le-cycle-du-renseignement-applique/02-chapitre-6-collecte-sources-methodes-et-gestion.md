---
title: 'Chapitre 6 — Collecte : sources, méthodes et gestion'
source: Cyber/01_CTI/CTI.md
note: Cyber Threat Intelligence (CTI)
up:
- - Cyber Threat Intelligence (CTI)
  - ../index.md
- - Partie II — Le cycle du renseignement appliqué
  - index.md
---

## 6.1 Taxonomie des sources CTI

Les sources CTI se répartissent en 6 catégories, chacune avec ses forces, ses biais, et son coût.

**Sources ouvertes (OSINT) :** les rapports publics d'éditeurs CTI (Mandiant, CrowdStrike, ESET, Kaspersky, Microsoft, Recorded Future — rapports de campagnes, profils d'acteurs, analyses de malware), les blogs de chercheurs en sécurité (souvent la première source de publication d'une nouvelle campagne ou d'une nouvelle vulnérabilité exploitée), les advisories des CERT (CERT-FR, CISA, NCSC — alertes officielles avec IoC et recommandations), les conférences et présentations (Black Hat, DEF CON, SSTIC, Botconf — présentations techniques avec des données exclusives), et les réseaux sociaux techniques (Twitter/X, LinkedIn — les chercheurs partagent des IoC et des analyses en temps réel, mais avec un bruit considérable). Forces : gratuites, abondantes, vérifiables. Limites : biais de publication (seules les campagnes détectées et analysées sont publiées — les opérations furtives restent invisibles), biais commercial (les éditeurs dramatisent parfois pour vendre), et volume (le bruit est massif — filtrer est un défi permanent).

**Sources commerciales :** les plateformes de threat intelligence (Recorded Future, Intel 471, Flashpoint, Mandiant Advantage, CrowdStrike Falcon Intelligence, Group-IB, Sekoia) offrent une couverture plus large (dark web, forums fermés, traductions, analystes humains) et des fonctionnalités d'enrichissement, de scoring, et d'alerting. Chaque plateforme a ses spécialités (Intel 471 et Flashpoint sont fortes sur le dark web et la cybercriminalité, Mandiant est forte sur les APT et l'IR, Recorded Future est forte sur la couverture large et l'automatisation). Forces : couverture élargie, analyse humaine, intégration API. Limites : coût élevé (50K-500K+ $/an), biais de couverture (chaque éditeur a ses angles morts), et risque de dépendance.

**Sources internes :** souvent les plus pertinentes car contextualisées pour l'organisation. Les logs SOC (alertes, incidents, patterns de faux positifs — qui révèlent ce que les attaquants tentent), les post-mortems d'IR (TTP observées dans les incidents passés = intelligence de première main sur les menaces qui ciblent réellement l'organisation), le vuln management (quelles vulnérabilités existent dans l'environnement = surface d'attaque réelle), l'email security (campagnes de phishing ciblant les utilisateurs), et l'IAM (tentatives de brute force, comptes compromis, anomalies d'authentification).

**Sources communautaires :** les ISACs sectoriels (EE-ISAC pour l'énergie, FS-ISAC pour la finance, H-ISAC pour la santé — échanges non publics entre pairs du même secteur), les cercles de confiance (FIRST, TF-CSIRT, InterCERT France, groupes de travail ANSSI), et les trusted groups (groupes Signal/Telegram entre analystes de confiance). Forces : contexte que les rapports publics ne donnent pas, réciprocité, confiance. Limites : accès restreint (il faut être membre et contribuer), couverture limitée au secteur/à la communauté.

**Sources dark web :** le monitoring des forums, marchés, leak sites, et canaux Telegram pour détecter les ventes de données, les ventes d'accès, les revendications de ransomware, et les discussions de ciblage qui concernent l'organisation ou son secteur. La collecte dark web est traitée en profondeur dans le cours Dark Web de la bibliothèque — ici on traite de comment intégrer le renseignement dark web dans le cycle CTI (le renseignement dark web est une source parmi d'autres, pas une fin en soi, et il doit être évalué avec la même rigueur que les autres sources — voir le chapitre pièges analytiques du cours Dark Web).

**Sources techniques :** les honeypots et honeynets (systèmes pièges qui capturent les activités des attaquants), les sinkholes (domaines de C2 saisis ou expirés dont le trafic est redirigé vers un serveur de collecte — révèlent les machines compromises qui tentent de contacter le C2), la telemetry de déploiement (les éditeurs d'EDR/antivirus ont une visibilité sur des millions de machines — leurs feeds de threat intelligence en découlent), le passive DNS (historique des résolutions DNS — révèle les changements d'infrastructure C2), et Certificate Transparency (logs publics des certificats TLS émis — permettent de détecter l'enregistrement de certificats pour des domaines de phishing ou de C2).

## 6.2 Gestion de la collecte

Le piège principal est la surcharge informationnelle : des centaines de rapports par semaine, des millions d'IoC dans les feeds, des dizaines d'alertes de monitoring. L'analyste qui essaie de tout lire et tout traiter se noie. La gestion de collecte impose de prioriser (les sources sont classées par pertinence pour les PIR actifs — les sources qui ne répondent à aucun PIR sont dé-priorisées), de documenter (chaque information est traçable jusqu'à sa source — qui, quand, où, avec quelle fiabilité), d'automatiser le traitement des feeds (l'injection d'IoC dans le SIEM/EDR est automatisée — l'analyste n'intervient que pour le scoring et la contextualisation), et de maintenir l'OPSEC (les identités de veille dark web sont compartimentées, l'infrastructure de collecte est séparée de l'infrastructure de production — les détails opérationnels sont dans le cours Dark Web).

## 6.3 Fil rouge — MERIDIAN : le plan de collecte

> **🔎 MERIDIAN — Épisode 5**
>
> Élise construit son plan de collecte pour les 5 PIR. Sources mobilisées : artefacts IR de l'incident EDE (source interne — haute fiabilité), rapports Mandiant et CrowdStrike sur les acteurs ciblant le secteur énergie (source commerciale — haute fiabilité, biais de couverture à considérer), ISAC énergie européen (source communautaire — fiabilité variable selon les contributeurs), passive DNS sur les 3 domaines C2 identifiés (source technique), Certificate Transparency sur les patterns d'enregistrement, monitoring dark web pour les credentials EDE (source dark web — fiabilité modérée, risque de scams), et CISA KEV pour les vulnérabilités Ivanti exploitées ITW (source technique — haute fiabilité).

---
