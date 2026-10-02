---
title: Chapitre 20 — Capstone Partie IV
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - 'Partie IV — L''attaquant : perspectives offensives'
  - index.md
---

planification d'un red team SE complet

**Exercice intégrateur.** L'étudiant produit un plan de mission red team social engineering complet pour un scénario donné (groupe pharmaceutique, 3 sites, 800 employés, programme de R&D sensible, contexte de fusion-acquisition récente).

**Livrables attendus :**

1. Analyse du scope et des contraintes (lettre de mission rédigée, rules of engagement, limites éthiques explicites)
2. Plan de reconnaissance (OSINT + physique, sources, méthodologie, timeline)
3. Matrice des pretextes (par vecteur : phishing, vishing, intrusion physique, élicitation — pretexte principal et pretexte de secours pour chaque)
4. Timeline d'exécution (6 semaines, séquencement des phases)
5. Liste du matériel et de l'infrastructure
6. Plan OPSEC (légendes, compartimentation, gestion des preuves)
7. Protocole d'urgence (safe word, contacts, procédure de désescalade)
8. Modèle de rapport (structure, métriques, format de recommandations)

**Erreur fréquente** : produire un plan techniquement solide mais éthiquement fragile (limites floues, absence de protocole d'urgence, oubli de la gestion des résultats individuels).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 5**
>
> **L'incident réel.** En parallèle du red team, Lucie Ferraro alerte Nathan. Un ingénieur R&D senior du bureau parisien, Alexandre Petit, 45 ans, spécialiste des systèmes de navigation inertielle, a été contacté il y a trois mois sur LinkedIn par un certain « David Chen », se présentant comme recruteur chez « Meridian Consulting Asia ». Les échanges ont débuté par des compliments sur les publications d'Alexandre et une proposition de « consulting rémunéré » pour un client asiatique du secteur aéronautique.
>
> La conversation s'est déplacée vers WhatsApp. David Chen est passé progressivement de questions générales sur le secteur à des questions de plus en plus spécifiques : « Quelles sont les principales innovations en navigation inertielle actuellement ? », « Votre entreprise travaille sur des systèmes MEMS ou fibre optique ? », « Quels sont les principaux défis techniques du programme européen ? ». Alexandre a d'abord répondu avec enthousiasme (flatterie, intérêt professionnel, perspective de rémunération), puis a commencé à avoir des doutes quand David Chen a proposé un « rendez-vous confidentiel » lors d'un salon à Singapour.
>
> Nathan analyse les échanges et reconnaît un schéma d'élicitation classique : spotting (LinkedIn), assessment (publications, poste clé), developmental contact (connexion LinkedIn, flattery), cultivation (échanges WhatsApp, proposition de consulting), et escalade (questions de plus en plus spécifiques, proposition de rendez-vous physique). La progression suit le continuum HUMINT décrit au Ch.3. Le profil LinkedIn de David Chen présente des incohérences : photo qui ne retourne aucun résultat sur les recherches d'image inversée (probablement générée par IA), entreprise « Meridian Consulting Asia » sans présence web vérifiable, parcours professionnel vague.
>
> Nathan recommande d'alerter la DGSI (ingérence économique potentielle) et de débriefer Alexandre sans le blâmer — il est un insider involontaire, pas un traître. L'ingénieur est débriefé par la RSSI et Nathan : explication du mécanisme d'élicitation, rappel des signaux d'alerte, aucune sanction. La DGSI est informée et ouvre une enquête.

---
