---
title: 'Chapitre 34 — Cas complet : profilage et attribution d''un cluster inconnu (synthèse MERIDIAN)'
source: Cyber/01 CTI & renseignement/Menace cyber/CTI — les fondamentaux.md
note: CTI — les fondamentaux
up:
- - CTI — les fondamentaux
  - ../index.md
- - Partie VIII — Études de cas et synthèse
  - index.md
---

Ce chapitre est la synthèse du fil rouge sous forme de cas autonome. Il reconstitue l'investigation complète d'Élise en un récit continu qui applique chaque compétence enseignée dans le cours.

**Phase 1 — Direction (Ch.5) :** Formulation des 5 PIR avec le RSSI d'EDE. Le plan de collecte identifie 7 catégories de sources à mobiliser.

**Phase 2 — Collecte (Ch.6) :** Artefacts IR de l'incident EDE (source interne, fiabilité A/1). Rapports Mandiant et CrowdStrike sur les acteurs ciblant l'énergie (source B/2). ISAC énergie européen (source B-C/2-3). Passive DNS sur les 3 domaines C2 (source technique, B/1). CISA KEV pour CVE-2024-21887 (source A/1). Monitoring dark web : aucune mention d'EDE — mais 2 mentions du secteur énergie européen sur XSS avec des discussions de ciblage (source C/3).

**Phase 3 — Traitement (Ch.7) :** Structuration dans OpenCTI. Création de l'objet Intrusion Set « UNC-VOLT ». Liaison avec les IoC, les TTP (mapping ATT&CK), les victimes (EDE + 3 opérateurs ISAC). Enrichissement automatisé des IoC (passive DNS, VirusTotal, ASN lookup).

**Phase 4 — Analyse (Ch.9-14) :** Application de l'ACH avec 4 hypothèses (voir épisode 6). Corrélation multi-sources : les patterns de beaconing (intervalles de 32 minutes avec jitter de 10 %) sont identiques à ceux documentés dans un rapport ESET sur Sandworm/CaddyWiper (2022). L'infrastructure C2 partage un registrar (NameCheap) et un pattern de nommage (subdomaines de services cloud légitimes) avec des campagnes Sandworm documentées par Mandiant. La victimologie (4 opérateurs d'énergie européens en 6 mois) est cohérente avec le programme de ciblage des infrastructures critiques européennes attribué au GRU. Key Assumptions Check : « nous supposons que les patterns de beaconing sont distinctifs » — vérification : les intervalles de 32 min + 10 % jitter ne sont documentés que pour Sandworm, pas pour d'autres acteurs. Conclusion : **attribution à Sandworm/GRU (Unit 74455) avec confiance modérée.** Modérée (pas élevée) car : pas de malware Sandworm identifié positivement (les outils custom de Sandworm comme Industroyer ou CaddyWiper n'ont pas été trouvés — l'attaquant utilisait principalement des LOLBins), et les faux drapeaux restent théoriquement possibles.

**Phase 5 — Production (Ch.26-28) :** Élise produit 3 livrables. (1) Note analytique stratégique pour le COMEX d'EDE (5 pages — résumé exécutif + analyse + recommandations business : « un acteur probablement lié au renseignement militaire russe vous cible pour un pré-positionnement dans vos systèmes de contrôle industriel — les mesures prioritaires sont la segmentation IT/OT physique, le patching des appliances Ivanti, et le déploiement des détections jointes »). (2) Note tactique pour le SOC d'EDE (10 pages — TTP détaillées + 12 règles Sigma + plan de hunting sur 4 semaines). (3) Profil d'acteur UNC-VOLT (15 pages, format OpenCTI — le profil est proposé à l'ISAC énergie pour enrichissement communautaire).

**Phase 6 — Partage et feedback (Ch.8, Ch.25) :** Partage ISAC (TLP:AMBER) → 2 opérateurs confirment des activités supplémentaires → le profil est enrichi. L'ANSSI est informée (EDE est OIV). Le feedback du SOC d'EDE après 4 semaines : 3 des 12 règles Sigma ont généré des FP nécessitant un tuning, 1 règle a détecté une activité suspecte qui s'est révélée être un test d'intrusion autorisé (FP documenté), et les hunts n'ont pas révélé de compromission résiduelle (renforcement de la confiance dans l'éradication).

---
