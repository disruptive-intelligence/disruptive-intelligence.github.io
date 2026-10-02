---
title: 'Chapitre 29 — Cas de synthèse : opération de social engineering multi-vecteurs'
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie VII — Synthèse et cas pratiques
  - index.md
---

**Scénario complet.** L'étudiant analyse une opération de social engineering reconstituée couvrant l'ensemble du spectre : reconnaissance OSINT → spear-phishing → vishing → intrusion physique → élicitation → exploitation → détection → investigation → remédiation.

**Contexte.** Un cabinet d'avocats d'affaires parisien (150 employés, données clients hautement confidentielles, associés voyageant fréquemment) est ciblé par un groupe criminel spécialisé dans le BEC. L'opération se déroule sur 4 semaines.

**Phase 1 — Reconnaissance.** Le groupe collecte les profils LinkedIn des associés et des assistants, identifie les dossiers en cours (via les communiqués de presse et les annonces de transactions), cartographie l'organigramme et les processus de communication interne.

**Phase 2 — Spear-phishing ciblé.** Un email de phishing se faisant passer pour le service IT du cabinet est envoyé à 8 assistants. 3 cliquent. Les identifiants de 2 assistants sont capturés.

**Phase 3 — Reply-chain BEC.** Les identifiants d'une assistante sont utilisés pour accéder à sa boîte mail. Le groupe lit les échanges récents avec un client sur une transaction immobilière de 2 millions d'euros. Un email est inséré dans le fil de conversation demandant un virement vers de nouvelles coordonnées bancaires, en invoquant un changement de domiciliation bancaire du notaire.

**Phase 4 — Vishing de confirmation.** Le groupe appelle l'assistante en se faisant passer pour le « cabinet du notaire » pour confirmer le changement d'IBAN et presser l'exécution du virement.

**Phase 5 — Détection et réponse.** Le virement est exécuté. 48h plus tard, le vrai notaire contacte le cabinet pour relancer le règlement. L'arnaque est découverte. Investigation, plainte, tentative de gel de fonds (partiellement réussie — 40 % des fonds récupérés).

**Analyse attendue.** L'étudiant identifie chaque technique utilisée, les leviers psychologiques exploités à chaque étape, les défenses qui auraient pu prévenir l'attaque (DMARC, bannière email externe, processus de vérification des changements d'IBAN, callback au notaire sur un numéro connu, formation des assistants au BEC), et rédige un rapport post-incident avec recommandations P0/P1/P2.

---
