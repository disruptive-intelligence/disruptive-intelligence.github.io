---
title: Chapitre 8 — Dissémination et feedback
source: Cyber/01_CTI/CTI.md
note: CTI
up:
- - CTI
  - ../index.md
- - Partie II — Le cycle du renseignement appliqué
  - index.md
---

## 8.1 Atteindre le bon public au bon moment

Le produit CTI le plus brillant est inutile s'il n'atteint pas son audience. La dissémination est la phase qui connecte le renseignement à l'action.

Les formats par audience : **IoC feed automatisé** (→ SIEM, EDR, pare-feu — format STIX/TAXII, intégration API, scoring automatique), **note tactique avec règles Sigma** (→ analystes SOC, hunters — format document technique avec détections prêtes à déployer), **briefing opérationnel** (→ IR lead, SOC manager — format présentation orale ou note de 2-3 pages), **note stratégique** (→ RSSI, direction, board — format rapport de 5-10 pages sans jargon), **flash alert** (→ toute l'équipe sécurité — format 1 page, urgence, actions immédiates).

## 8.2 Le TLP (Traffic Light Protocol)

Le TLP encadre la diffusion du renseignement partagé. **TLP:RED** (yeux seulement — ne pas diffuser au-delà des personnes présentes dans l'échange). **TLP:AMBER** (diffusion limitée à l'organisation et aux partenaires qui ont besoin de savoir — le niveau le plus courant pour les échanges communautaires). **TLP:AMBER+STRICT** (diffusion limitée à l'organisation uniquement). **TLP:GREEN** (diffusion au sein de la communauté — pas au grand public). **TLP:CLEAR** (diffusion libre).

L'erreur courante : sur-classifier en TLP:RED par excès de prudence. Résultat : l'information ne circule pas, et les organisations qui auraient pu se protéger ne sont pas informées. L'analyste doit appliquer le niveau TLP minimum nécessaire pour protéger la source sans bloquer l'utilité du renseignement.

## 8.3 Le feedback — la boucle la plus importante

Le feedback est la phase qui ferme le cycle et qui est la plus systématiquement négligée. Le SOC signale que les IoC d'un feed génèrent 80 % de faux positifs → la CTI réévalue le scoring du feed. L'IR signale que les TTP d'un rapport ne correspondent pas à ce qu'il observe sur le terrain → la CTI réévalue l'attribution ou identifie un nouveau cluster. Le RSSI signale que les rapports stratégiques sont trop techniques pour le board → la CTI ajuste le format. Le hunting signale qu'une hypothèse CTI a produit un résultat positif (ou négatif) → la CTI met à jour le profil d'acteur.

Sans feedback, le cycle est cassé : la CTI produit dans le vide, les consommateurs reçoivent du renseignement non calibré, et la qualité se dégrade.

---
