---
title: Chapitre 34 — Produire une note analytique
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VI — ANALYSE, renseignement et production
  - index.md
---

Forme pratique de livraison du renseignement. La **note analytique** (ou « intel note ») est le livrable type de l'analyste CTI. Ce chapitre couvre les conventions, la structure, et les pièges de rédaction.

## 34.1 Les types de notes

**Flash alert**. Note très courte (1-2 pages), livraison immédiate sur événement important. Exemple : un leak site affiche une victime critique, un 0-day exploité massivement. Ton : urgent. Action : immédiate.

**Intel note**. Note standard (3-8 pages), livraison régulière sur observations significatives. Exemple : investigation DARKSTREAM. Ton : structuré. Action : planifiée.

**Bulletin sectoriel**. Note périodique (10-30 pages), synthèse des tendances dans un secteur. Souvent mensuelle ou trimestrielle. Exemple : « Menaces dark web contre secteur aerospace T3 2025 ». Ton : analytique. Action : stratégique.

**Note stratégique**. Note de fond (15-50 pages), vision long terme. Rare (1-4 par an). Destinée à direction. Exemple : « Évolution de l'écosystème cybercriminel 2020-2026 et implications pour Vectris ».

**Advisory**. Communication publique ou semi-publique sur menace spécifique. Format court, diffusion large (ISAC, communauté CTI). Exemple : « Campagne de phishing ciblée aerospace — IoC et mesures recommandées ».

## 34.2 Structure standard d'une intel note

**En-tête**. Titre clair et précis, date de rédaction, auteur, destinataires, **classification TLP**, version/révision.

**Executive summary** (⅓-½ page). Réponse aux questions « so what ? » et « now what ? ». Le lecteur pressé ne lit que cette section — elle doit être suffisante.

- Qu'est-ce qui a été observé ?
- Pourquoi c'est important ?
- Qu'est-ce qu'il faut faire ?
- Quel niveau de confiance ?

**Contexte**. Pourquoi cette note est-elle produite ? Quel événement déclencheur ? Quelles observations antérieures pertinentes ?

**Observations**. Faits observés, avec sources et horodatages. Ton factuel, pas interprétatif ici.

**Analyse**. Interprétation des observations. Attribution, motivations, chaîne d'événements, liens avec autres renseignements. Ton analytique, WEP utilisés.

**Implications**. Pourquoi c'est important pour le destinataire. Risques concrets, impacts potentiels.

**Recommandations**. Actions concrètes, priorisées, avec destinataires et délais. Section la plus actionnable.

**Limites et incertitudes**. Ce qui n'est pas connu, ce qui pourrait changer l'analyse. Honnêteté méthodologique.

**Annexes**. IoC, détails techniques, captures, timelines détaillées, références.

## 34.3 Les règles de rédaction

**Clarté avant tout**. Phrases courtes, vocabulaire précis. Acronymes introduits avant usage. Pas de jargon non-nécessaire.

**Structure logique**. Chaque section répond à une question précise. Le lecteur doit pouvoir naviguer par table des matières.

**Factualité**. Distinction nette entre observation et interprétation. « Le vendeur a publié un échantillon » (observation) vs « le vendeur est un russophone professionnel » (interprétation fondée sur observations listées).

**Calibration**. WEP systématiques. Pas de « certain » sans preuve directe, pas de « impossible » sans démonstration.

**Sources**. Chaque observation est sourcée (URL .onion, forum/post ID, outil utilisé, plateforme). Niveau de détail adapté au TLP — à TLP RED, on peut détailler ; à TLP CLEAR, généralisation.

**Actionnabilité**. Chaque section « observations » et « implications » est suivie d'une conclusion exploitable, pas juste descriptive.

**Neutralité**. Pas de jugements moraux (« ces criminels répugnants… »). Pas de bias idéologique. Pas de « vendre » plus de sécurité à sa direction.

**Révisabilité**. Le rapport est une photo d'un instant T. Mentionner date, noter que nouvelles observations peuvent changer l'analyse.

## 34.4 Les pièges de rédaction

**Trop de détails techniques en exécutif**. L'executive summary pour la direction ne doit pas contenir « SHA-256 hashes a1b2c3... ». Les détails vont en annexes.

**Pas assez de détails pour les techniques**. Inverse — le SOC veut les IoC précis, pas des généralités. Adapter par destinataire.

**Redondance interne**. La même info répétée en executive summary, en analyse, en implications. Chaque section doit apporter quelque chose de différent.

**Over-narrativization**. Raconter une « histoire » trop fluide peut gommer les incertitudes. Le lecteur croit à une certitude que l'auteur n'a pas.

**Omissions politiques**. Éviter de parler d'un risque qui embarrasse la direction (« on a raté la détection depuis 3 mois »). Un rapport honnête peut déplaire mais maintient crédibilité long terme.

**Sur-confidence post-hoc**. Écrit après les faits, l'analyse peut paraître trop facile. Mentionner ce qui était incertain avant action.

**Manque de graphiques / visuels**. Un graphe de chaîne d'attaque, une timeline, un cluster crypto valent 1 000 mots de prose. Utiliser les visuels.

## 34.5 Le template DARKSTREAM

Exemple concret de structure pour l'investigation DARKSTREAM.

**TITRE** : Opération DARKSTREAM — Investigation sur la circulation dark web des données exfiltrées de Vectris Aerospace — Rapport final

**MÉTADONNÉES** : Auteur Lucas Ferreira, Athéna Group ; Date 15/05/2026 ; Version 1.0 ; Classification TLP:RED ; Destinataires : Cellule crise Vectris + DGSI.

**EXECUTIVE SUMMARY** :

- 420 Go de données Vectris (R&D propulsion, specs défense, bases clients, emails) circulent sur forum russophone IndustrialLeaks.
- Vendeur aero_source, profil cybercriminel russophone individuel, pas d'acteur étatique identifié.
- Chaîne reconstituée : stealer Lumma → log Russian Market → IAB magnit_ru → exfiltration aero_source ou commanditaire.
- Confiance authentification : **très élevée** (marker interne + cohérence forensics).
- Confiance attribution technique : **élevée** (90%+).
- Confiance attribution personnelle : **faible** (identification civile hors d'atteinte de l'investigation privée).
- Menace élevée pour Vectris mais contenue — pas de preuve d'accès étatique actuel.

**CONTEXTE** : déclenchement investigation suite alerte Recorded Future, mandat Athéna + DGSI, 6 semaines d'investigation.

**OBSERVATIONS** :

- Post IndustrialLeaks (date, URL, capture).
- Profil aero_source (8 mois, 12 posts, 2 transactions antérieures).
- Échantillons authentifiés (fichiers, hashes, markers).
- 12 stealer logs Vectris identifiés sur Russian Market.
- Cluster crypto de 40 adresses, ~180 k USDT transactions, flux vers BlackSprut et Garantex (avant sanctions).
- Pseudonymes pivots : aerosrc (XSS), aero_src (Exploit.in).
- PGP commune, linguistique cohérente, fuseau MSK.

**ANALYSE** : [narration structurée de la chaîne, attribution technique, hypothèses alternatives testées et rejetées].

**IMPLICATIONS** :

- Risque de publication totale si non-acheteur trouvé (2-3 mois typiquement).
- Risque de revente à acteur étatique (possible, non déterminable).
- Exposure compliance (notification CNIL pour données personnelles, notification partenaires défense).
- Reputational — prédiction de question médiatique possible.

**RECOMMANDATIONS** :

1. **Immédiat** : poursuite isolation/reset des 3 postes compromis identifiés.
2. **Immédiat** : notification aux 4 partenaires défense concernés.
3. **7 jours** : préparation communication client top-20 (si escalade).
4. **30 jours** : durcissement politique téléchargement logiciels + EDR renforcé R&D.
5. **30 jours** : monitoring IndustrialLeaks continu, alerting sur évolution.
6. **90 jours** : revue complète politique credentials + formation sensibilisation.

**LIMITES** :

- Attribution personnelle impossible via moyens privés.
- Évolution possible (revente à étatique, publication totale) non prédictible.
- Biais possibles : sur-attribution à profil russophone (à confirmer par enrichissement).

**ANNEXES** :
A. Captures IndustrialLeaks (147 screenshots).
B. Conversations XMPP aero_source (18 échanges).
C. Échantillons authentifiés (8 fichiers).
D. Analyse blockchain cluster (graphe).
E. Logs Russian Market (12 logs).
F. IoC structurés MISP.
G. Chain of custody.
H. Note méthodologique.

## 34.6 La présentation orale

Une note écrite s'accompagne souvent d'une **présentation orale** à la cellule de crise, direction, autorités.

**Format type** : 20-30 minutes présentation + 30-60 min Q&A.

**Structure** :

1. Contexte et déclenchement (2 min).
2. Ce qui a été observé (5 min).
3. Ce que ça veut dire (5 min).
4. Ce qu'il faut faire (5 min).
5. Ce qui reste incertain (3 min).
6. Q&A (le plus long).

**Support** : slides simples, pas de murs de texte. Graphes, timelines, captures emblématiques. Backup slides détaillées pour Q&A.

**Ton** : calme, structuré, calibré. Pas d'alarmisme, pas de minimisation. Accepter de ne pas savoir.

**Audience mixte** : adapter au dénominateur commun. Exécutifs demanderont impact business ; techniques demanderont détails IoC. Satisfaire chaque typologie sans perdre l'autre.

---
