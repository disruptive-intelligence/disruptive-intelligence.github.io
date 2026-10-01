---
title: PARTIE VII — Cas de synthèse
source: Cyber/01 CTI & renseignement/Menace cyber/Panorama de la cybermenace — état de l'art.md
note: Panorama de la cybermenace — état de l'art
up:
- - Panorama de la cybermenace — état de l'art
  - index.md
---

## Chapitre 27 — Cas de synthèse n°1 : la convergence étatique-criminel

**Contexte** : En février 2025, un groupe pharmaceutique européen détecte un ransomware (NailoLocker) sur le réseau de sa filiale en Asie du Sud-Est. L'investigation forensique révèle la présence simultanée de backdoors ShadowPad et PlugX — outils historiquement associés à l'espionnage chinois. Le cas est basé sur des incidents réels documentés par Orange CyberDefense, Fortinet et Trendmicro en 2025, ainsi que par l'ANSSI.

**Chaîne d'attaque** : Exploitation d'une vulnérabilité dans un VPN Fortinet non patché (CVE connue, patch disponible depuis 3 mois) → déploiement de ShadowPad comme backdoor persistante → reconnaissance réseau et exfiltration de données R&D pendant 6 semaines → déploiement de NailoLocker comme couverture/monétisation. L'exfiltration de données précède le ransomware — le ransomware sert de diversion.

**Analyse d'attribution** : L'attribution est complexe. ShadowPad est historiquement associé aux acteurs chinois, mais l'outil a été utilisé par au moins cinq groupes distincts. PlugX est encore plus répandu. NailoLocker est un ransomware relativement peu sophistiqué. Trois hypothèses sont considérées :

- Hypothèse A (confiance modérée) : un acteur étatique chinois a conduit l'espionnage et déployé le ransomware comme couverture.
- Hypothèse B (confiance basse) : un affilié ransomware indépendant a acheté un accès déjà compromis par un acteur étatique (scénario « victimes multiples du même accès »).
- Hypothèse C (confiance basse) : un acteur hybride combine espionnage et cybercriminalité (modèle APT41).

**Leçons** : la convergence étatique-criminel rend l'attribution plus complexe et exige que la réponse traite simultanément les deux dimensions (remédiation ransomware + investigation espionnage). La présence d'outils d'espionnage change le calcul : le risque n'est plus « seulement » financier mais stratégique.

---


## Chapitre 28 — Cas de synthèse n°2 : supply chain attack multi-niveaux

**Contexte** : Basé sur les cas réels traités par l'ANSSI en 2025. Un prestataire de services IT (infogérance, hébergement, gestion de projets) servant plusieurs entités françaises est compromis. L'attaquant utilise les interconnexions existantes et les authentifiants volés pour se latéraliser sur les systèmes de plusieurs clients.

**Chaîne d'attaque** : Spearphishing ciblant un administrateur du prestataire → vol de credentials d'administration → accès au système de gestion centralisé → identification des connexions vers les clients → utilisation des authentifiants partagés pour accéder aux SI clients → actions différenciées selon les clients : exfiltration de données pour certains, déploiement de ransomware pour d'autres.

**Complexités** : La coordination de la réponse implique le prestataire (victime initiale), les clients (victimes secondaires), l'ANSSI (coordination), et les CERT respectifs. Chaque organisation a ses propres processus, ses propres contraintes et ses propres intérêts (le prestataire ne souhaite pas exposer l'étendue de la compromission à ses clients). La gestion des notifications NIS2 est complexe : qui notifie quoi, à qui, dans quel délai ?

**Leçons** : la sécurité de la supply chain ne peut pas être gérée par des clauses contractuelles seules. Elle exige : un audit régulier des postures de sécurité des prestataires critiques, une segmentation stricte des interconnexions, un monitoring des accès partagés, et un plan de réponse à incident incluant les scénarios supply chain.

---


## Chapitre 29 — Cas de synthèse n°3

incident multi-vecteurs sur une entité NIS2

**Contexte** : Un groupe industriel européen classé entité essentielle NIS2 fait face simultanément à :

1. Une campagne de spearphishing augmenté IA ciblant les cadres dirigeants (deepfake vocal + email coordonné)
2. Une revendication DDoS hacktiviste sur les portails web publics (NoName057(16))
3. Des signaux faibles d'un APT étatique sur un serveur Exchange interne (beaconing suspect)
4. Une campagne de désinformation sur les réseaux sociaux visant à discréditer un contrat public

**Exercice** : L'analyste doit trier les quatre événements par priorité, attribuer chacun à une catégorie d'acteur avec un niveau de confiance, déterminer si les événements sont corrélés ou indépendants, recommander les actions immédiates pour chaque événement, gérer la communication de crise (que dire au COMEX, au régulateur, aux médias ?), et rédiger la notification NIS2.

**Points clés** : La simultanéité d'événements hétérogènes est un test de la maturité d'un CERT. La capacité à distinguer le bruit (DDoS hacktiviste) du signal critique (APT étatique) sous la pression de la crise est une compétence fondamentale. La composante d'influence (désinformation) est hors du périmètre technique du CERT mais doit être gérée.

---


## Chapitre 30 — Cas de synthèse n°4

production d'un threat landscape sectoriel complet

**Exercice** : Produire un CTL sectoriel professionnel pour le secteur aéronautique/défense/spatial européen, en appliquant l'intégralité de la méthodologie du cours.

**Étapes** :

1. Cadrage : définir le périmètre (sectoriel, géographique, temporel), l'audience (COMEX + SOC + partenaires OTAN), les PIR (4-6 questions structurantes)
2. Plan de collecte : identifier les 10 sources principales, justifier leur sélection, documenter leurs biais
3. Collecte et traitement : sélectionner les données pertinentes dans le corpus du cours, normaliser et enrichir
4. Analyse : identifier les 5 menaces prioritaires, produire les assessments avec LCA et WEP, considérer les alternatives, documenter les inconsistances
5. Rédaction : executive summary (2 pages), rapport technique (10+ pages), langage analytique calibré
6. Recommandations : 5-10 recommandations priorisées P0/P1/P2 avec justification fondée sur le CTL
7. Validation : checklist de validation pré-publication (cohérence, sources, niveaux de confiance, biais documentés)
8. Dissémination : choix du TLP, format, canaux

**Critères d'évaluation** : rigueur méthodologique, qualité des assessments, calibrage de la confiance, pertinence des recommandations, qualité rédactionnelle, exploitabilité opérationnelle.

---
