---
title: E.2 Les familles
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
---

| Famille | Exemples représentatifs | Modèle | Limites concrètes |
|---|---|---|---|
| **Scan de vulnérabilités** | Solutions commerciales de scan authentifié (Tenable, Qualys, Rapid7) · alternative libre : OpenVAS/Greenbone | Par actif · libre | Faux positifs de rétroportage · historique rarement portable · systèmes industriels et services en ligne hors champ |
| **Découverte externe** | Modules EASM des mêmes éditeurs · services spécialisés | Par domaine · sur devis | Peut attribuer à tort des actifs · ne voit rien de l'interne |
| **Déploiement Windows** | Configuration Manager · Intune · Windows Update for Business · WSUS (en fin de cycle) | Inclus dans des offres groupées · par poste | Applications tierces non couvertes nativement · reporting difficilement exportable |
| **Déploiement Linux** | Ansible · Red Hat Satellite · Landscape · SUSE Manager · dépôts internes | Libre · par nœud · abonnement | Orchestration des redémarrages à construire |
| **Applications tierces** | Gestionnaires de paquets Windows (winget, Chocolatey) · modules tiers des outils de déploiement | Libre · option payante | Couverture du catalogue variable sur les applications métier |
| **Gestion de flotte** | Intune · Jamf · solutions équivalentes | Par appareil | Ne couvre que les appareils enrôlés |
| **Analyse de composition** | Dependabot/Renovate · Snyk · OWASP Dependency-Check · Trivy | Libre · par développeur · par dépôt | Bruit élevé sans analyse d'atteignabilité |
| **Analyse d'images** | Trivy · Grype · modules de registres | Libre · inclus | Ne voit pas ce qui est ajouté à l'exécution |
| **Contrôle de configuration** | OpenSCAP · outils natifs de politique · Ansible | Libre · inclus | Référentiels génériques inadaptés aux applications métier |
| **Posture cloud** | Modules natifs des fournisseurs · solutions tierces | À la consommation · par ressource | Multi-cloud = dispositifs multiples à maintenir |
| **Gestion de secrets** | HashiCorp Vault · coffres natifs des fournisseurs | Libre · à la consommation | Devient un actif de niveau 0 · rotation à répercuter |
| **Inventaire / CMDB** | Modules ITSM · GLPI · solutions CAASM | Par actif · libre | Vaut ce que valent ses sources |
| **Ticketing / workflow** | Jira · GLPI · modules ITSM | Par utilisateur | Ne règle ni l'absence de propriétaire ni la capacité |
| **Journalisation** | Solutions SIEM · piles ouvertes (OpenSearch, Loki) | Par volume ingéré · libre | Le coût croît avec la rétention — arbitrage à faire tôt |
| **Découverte industrielle** | Solutions d'écoute passive OT | Sur devis | Ne voit que ce qui communique |


## E.3 Critères de sélection, par ordre d'importance

1. **Exportabilité des données brutes** et de l'historique en format ouvert — le critère décisif à cinq ans (§19.1).
2. Capacité à calculer la couverture sur **votre** périmètre de référence, pas sur le sien.
3. Granularité de ciblage : anneaux, exclusions documentées, populations.
4. Couverture réelle des applications tierces et des composants intermédiaires.
5. Fonctionnement hors réseau interne.
6. Coût total : licence **plus** intégration **plus** exploitation.

---
