---
title: Partie VI — Gestion des tiers et cloud
source: Cyber/08 Gouvernance & résilience/Gouvernance & conformité/Gouvernance, risques et conformité (GRC).md
note: Gouvernance, risques et conformité (GRC)
up:
- - Gouvernance, risques et conformité (GRC)
  - index.md
---

*Les tiers sont la surface d'attaque n°1 — NIS 2 impose leur gestion.*

---


## Chapitre 26 — Gouvernance des tiers

évaluation, scoring et surveillance

*Ce chapitre couvre la gouvernance des tiers — processus d'évaluation, scoring, surveillance continue. Les clauses contractuelles et la dimension juridique sont au Ch.19 pour éviter la redondance.*

Le risque tiers : les prestataires ont accès aux systèmes et aux données, les compromissions via tiers sont parmi les plus dévastatrices (SolarWinds, Cloud Hopper, incidents via infogérants), et NIS 2 impose explicitement la gestion de la supply chain.

L'évaluation et le scoring : chaque fournisseur est classé selon son niveau d'accès et de criticité. **Critique** (accès données sensibles ou SI critiques — hébergeur, infogérant, éditeur ERP) : PAS complet, audit ou certification exigée (ISO 27001, SOC 2 Type II, HDS), SLA sécurité renforcé, revue annuelle. **Important** (accès SI ou données internes — prestataire dev, support IT) : questionnaire sécurité structuré, clauses contractuelles, revue bisannuelle. **Standard** (pas d'accès SI ni données sensibles — fournitures, nettoyage) : clauses RGPD basiques si données personnelles traitées.

La due diligence AVANT contractualisation (pas après — quand le contrat est signé, le rapport de force est inversé). Le questionnaire fournisseur (gouvernance, accès, chiffrement, gestion des incidents, continuité, certifications, sous-traitance éventuelle). La surveillance continue (revue annuelle des fournisseurs critiques, surveillance des certifications — expiration, retrait, surveillance des incidents publics, et ratings externes — SecurityScorecard, BitSight — utiles pour le screening initial, insuffisants pour l'évaluation en profondeur). Le registre des tiers (document vivant — fournisseur, criticité, accès, score, date de dernière revue, prochaine revue).

---


## Chapitre 27 — Cloud, souveraineté et conformité

La sécurité du cloud vue GRC repose sur le modèle de **responsabilité partagée** : en IaaS, le fournisseur gère l'infrastructure physique et la virtualisation, le client gère tout le reste (OS, applications, données, accès) ; en PaaS, le fournisseur gère aussi l'OS et le middleware ; en SaaS, le fournisseur gère quasi tout, le client gère les accès et la configuration. La confusion sur ce modèle est la source n°1 des incidents cloud.

La **souveraineté des données** : le Cloud Act permet aux autorités US d'accéder aux données hébergées par des entreprises américaines (AWS, Azure, Google), même si les données sont physiquement en Europe. Le FISA 702 permet la surveillance des communications de personnes non américaines. Schrems II a invalidé le Privacy Shield. Les solutions : **SecNumCloud** (qualification ANSSI — hébergement souverain avec immunité aux lois extraterritoriales), chiffrement côté client (le fournisseur ne peut pas lire les données — mais cela limite les fonctionnalités), cloud souverain européen (3DS Outscale, OVHcloud, Scaleway — certifiés ou en cours de certification SecNumCloud), et C5 (certification cloud allemande — BSI).

Le questionnaire cloud : localisation des données (pays, région, transferts internationaux), chiffrement (en transit, au repos, gestion des clés — qui détient les clés ?), accès (qui accède aux données, depuis où, avec quel contrôle), conformité (certifications, audits, transparence), réversibilité (format d'export, délai, coût, destruction des données), et SLA (disponibilité, support, notification d'incident).

---
