---
title: Chapitre 92 — Veille post-rapport et capitalisation
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 92.1 Au-delà du rapport

Une enquête ne s'arrête pas à la remise du rapport. **Veille** sur l'évolution de la cible, **capitalisation** méthodologique, **archivage** rigoureux : trois dimensions post-rapport souvent négligées.

## 92.2 Veille post-rapport

Si le mandat le prévoit, **veille continue** sur la cible :

- Évolutions corporate (nouveaux dirigeants, dissolution, fusion).
- Nouvelles sanctions / PEP.
- Adverse media.
- Évolution infrastructure (nouveaux domaines, fuites).
- Évolution patrimoine (nouvelles acquisitions visibles).

**Outils.**

- **Google Alerts** : nom, raison sociale, domaines.
- **OpenSanctions monitoring**.
- **Hunchly continuous** : capture régulière.
- **Custom pipelines** : scripts qui scan périodiquement.

**Pour MIRAGE.** Si l'audience prud'homale Berthier doit avoir lieu plusieurs mois après le rapport, veille sur les acteurs : nouveau communiqué TechnoVert, nouvelle vidéo deepfake, évolution cluster désinformation.

## 92.3 Alertes et triage

Une veille produit des **alertes**. Triage rapide :

- **Pertinent** → note d'update au commanditaire.
- **À surveiller** → archivage interne pour suivi.
- **Non pertinent** → écarté avec justification.

**Pratique.** Note d'update mensuelle ou trimestrielle au commanditaire.

## 92.4 Capitalisation méthodologique

Chaque enquête enrichit l'analyste :

- **Outils** testés (qui marche, qui ne marche pas pour quel usage).
- **Méthodes** validées ou révisées.
- **Pièges** identifiés.
- **Sources** spécialisées découvertes.

**Pratique.** Après chaque enquête, **debriefing** interne :

- Qu'est-ce qui a bien fonctionné ?
- Qu'est-ce qui n'a pas bien fonctionné ?
- Quelles leçons pour la prochaine ?

Documentation dans un **carnet méthodologique** propre à l'analyste / cabinet.

## 92.5 Capitalisation factuelle (avec déontologie)

Certaines informations factuelles sont **réutilisables** d'une enquête à l'autre :

- Structures corporate publiques (immuables).
- Métadonnées infrastructures publiques.
- Méthodologies de groupes d'attaquants (TTP).

**Discipline.**

- Pas de mélange entre enquêtes différentes (mandat A ne nourrit pas mandat B).
- Information générale (sectorielle, publique) seule réutilisée.
- Données personnelles purgées par enquête.

**Pour cabinet.** Base de connaissances structurée distincte des dossiers d'enquête.

## 92.6 Archivage post-mandat

Selon mandat et juridiction :

- **Durée de conservation** documentée (typique 3-10 ans).
- **Chiffrement** maintenu.
- **Accès** restreint.
- **Intégrité** vérifiée périodiquement (re-hash).

**RGPD.** Justification de la conservation. Information aux personnes si pertinent.

## 92.7 Purge en fin de période

**Fin de la durée de conservation.**

- Suppression sécurisée (overwrite, wipe).
- Documentation de la purge.
- Conservation éventuelle d'un récapitulatif anonymisé.

**Pour MIRAGE.** Si la procédure se conclut sous 5 ans, archivage 7 ans (durée légale post-procédure), puis purge.

## 92.8 Suivi du commanditaire

Bonne pratique : **contact périodique** avec le commanditaire post-rapport :

- A-t-il pu utiliser le rapport efficacement ?
- Des éléments ont-ils été confirmés / infirmés par d'autres voies ?
- Y a-t-il besoin de mise à jour ?

Bénéfices : amélioration continue, relation long terme, opportunités futures.

## 92.9 Veille communautaire et formation continue

L'analyste se forme continûment :

- Suivi de Bellingcat, OCCRP, EU DisinfoLab, VIGINUM, Stanford SIO publications.
- Conférences (OSMOSIS, OSINT Day, NICAR, IRE).
- Formation en ligne (Bellingcat training, NATO StratCom).
- Communautés (Discord, Reddit /r/OSINT, Twitter/X OSINT communauté).

## 92.10 Synthèse — cycle complet de l'enquête

| Phase | Discipline |
|---|---|
| Cadrage | Mandat précis, IR formulées |
| Collecte | OPSEC, captures, cotation |
| Analyse | ACH, anti-biais, raisonnement adversaire |
| Production | Rapport calibré, fiches structurées |
| Diffusion | TLP, chiffrement, watermark |
| Veille | Alertes, updates |
| Capitalisation | Carnet méthodo, base sectorielle |
| Archivage | Chiffré, intégrité, durée |
| Purge | Sécurisée, documentée |

> **Principe.** L'enquête OSINT mature est un **cycle complet**, pas une production isolée. Chaque cycle nourrit le suivant, dans le respect strict de la déontologie de cloisonnement.

-----
