---
title: Chapitre 38 — Maintenance opérationnelle, réponse à incident et architectures par profil
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 7 — OPSEC humaine, opérationnelle et continuité
  - index.md
---

#### 38.1 La sécurité est un processus, pas un état

Une posture sécurisée installée en une semaine et jamais entretenue s’érode en six mois. Les mises à jour ne s’appliquent pas, les comptes oubliés s’accumulent, les habitudes glissent, les outils deviennent obsolètes. La maintenance n’est pas optionnelle.

#### 38.2 Routines : hebdo, mensuelle, trimestrielle, annuelle

**Hebdomadaire (15 minutes)** :

- Vérifier que les mises à jour OS et apps sont appliquées.
- Audit rapide des notifications de connexion suspecte.
- Vérification du fonctionnement des sauvegardes automatiques.
- Reboot des appareils sensibles (si pas quotidien).

**Mensuelle (1 heure)** :

- Audit des sessions actives sur comptes critiques (Google, Apple, Microsoft, Signal).
- Vérification HaveIBeenPwned sur emails principaux.
- Audit des permissions d’apps mobiles (revue de ce qui a accès localisation, micro, photos).
- Test rapide de restauration sauvegarde (juste vérifier qu’elle se monte et que les fichiers s’ouvrent).
- Mise à jour firmware si pas auto.

**Trimestrielle (2-3 heures)** :

- Audit complet OSINT défensif (Ch 5).
- Désinscription data brokers nouvellement apparus (Ch 6).
- Audit des appareils : intégrité physique, configuration, comptes connectés.
- Revue du threat model : a-t-il évolué ? Mes adversaires ont-ils changé ?
- Test de restauration complet (sur appareil neuf ou VM).
- Renouvellement des sous-clés PGP si applicable.

**Annuelle (1 jour)** :

- Audit complet de tous les comptes (suppression des inutilisés).
- Renouvellement des clés matérielles si signe d’usure.
- Revue de la stratégie globale : architecture, outils, threat model, formation.
- Documentation à jour (procédures personnelles, contacts d’urgence, codes de récupération).
- Décisions stratégiques : migration vers nouvel OS, nouveau matériel, nouvelle compartimentation.

#### 38.3 Réponse à incident : framework PICERL

Hérité de la cybersécurité d’entreprise, applicable au particulier :

- **P**reparation : avant tout incident, avoir une procédure documentée, contacts d’urgence, backups, outils prêts.
- **I**dentification : détecter qu’un incident a lieu. Notifications plateformes, alertes, comportement anormal.
- **C**ontainment : limiter la propagation. Isoler appareil, révoquer sessions, changer credentials des comptes touchés.
- **E**radication : éliminer la cause. Reset appareil, retrait de malware, fermeture des accès illégitimes.
- **R**ecovery : restaurer le fonctionnement normal. Restauration depuis backup propre, reconfiguration.
- **L**essons learned : analyse post-incident, mise à jour des procédures.

#### 38.4 Procédures par scénario

**Téléphone perdu/volé** :

1. Localisation à distance (Find My iPhone / Android Find My Device) si possible.
1. Effacement à distance si non récupérable.
1. Désactivation SIM auprès de l’opérateur.
1. Révocation sessions des comptes critiques.
1. Désinscription des passkeys liées à l’appareil.
1. Déclaration de vol (police, assureur).
1. Restauration sur appareil neuf depuis sauvegarde.

**Compte compromis** :

1. Changer immédiatement le mot de passe depuis appareil sain.
1. Révoquer toutes les sessions actives.
1. Audit : modifications récentes, filtre mail, méthodes MFA ajoutées.
1. Activer MFA matériel si pas déjà.
1. Vérifier comptes liés (cascade depuis email principal).
1. Communiquer aux contacts si phishing envoyé depuis ton compte.
1. Déposer plainte si dommages.

**Spyware suspecté** :

1. Mode avion + faraday bag immédiatement.
1. Ne pas redémarrer.
1. Contact Access Now Digital Security Helpline (+1-888-414-0100).
1. Sauvegarde pour analyse (iTunes/Quicktime pour iOS).
1. Soumission à Citizen Lab / Amnesty Security Lab pour confirmation.
1. Bascule appareil neuf, comptes audités, threat model révisé.

**Doxxing en cours** :

1. Documentation (captures, URLs, horodatages).
1. Signalement plateformes hébergeantes.
1. Évaluation menace physique, mise à l’abri si nécessaire.
1. Support psychologique et juridique (PEN America, RSF, La Quadrature selon profil).
1. Plainte (PHAROS, parquet).

#### 38.5 Architectures de référence par profil

**Profil 1 : particulier durci grand public**

- iPhone à jour avec ADP iCloud activée.
- Mac ou PC Windows 11 Pro avec chiffrement disque.
- Bitwarden + clés YubiKey (principal + backup).
- Signal pour communications, WhatsApp pour social, Proton Mail principal + alias.
- Mullvad ou IVPN.
- Routines mensuelles + trimestrielles appliquées.

**Profil 2 : journaliste freelance**

- Pixel 8a + GrapheneOS + iPhone perso séparé (ADP).
- MacBook Pro pro + MacBook Air enquête.
- Bitwarden + YubiKey 5 (principal + backup au coffre).
- Signal + SimpleX + Proton Mail pro + alias.
- Tails sur USB pour sessions ponctuelles ultra-sensibles.
- Mullvad VPN, Mullvad Browser quotidien, Tor Browser anonyme.
- Page « comment me joindre confidentiellement » publique.
- Routines complètes appliquées.

**Profil 3 : activiste, manifestation à risque**

- GrapheneOS sur Pixel d’occasion dédié manifestation.
- Aucune donnée personnelle, contacts limités à 3 numéros essentiels.
- Faraday bag.
- Numéros de hotline juridique et avocat sur papier.
- Procédure d’arrestation préparée (qui appeler, qui prévenir).
- Vrai téléphone perso laissé chez soi.

**Profil 4 : dirigeant PME exposé**

- MacBook avec ADP iCloud, FileVault, Lockdown Mode en voyage sensible.
- iPhone idem.
- 1Password famille (partage avec direction).
- Signal pour interne sensible, iMessage avec Contact Key Verification pour exec team.
- Compartimentation pro/perso strictes.
- Formation périodique des collaborateurs (BEC, phishing).
- Politique d’entreprise : MFA obligatoire, MDM Apple Business Manager / Intune.

**Profil 5 : opposant politique en exil (modèle Anya)**

- GrapheneOS dédié, profils stricts.
- Qubes OS pour travail public.
- Tor par défaut pour publications.
- Signal/SimpleX selon contacts.
- Liens hebdomadaires avec Citizen Lab / Access Now.
- Préparation à un éventuel ciblage spyware (MVT installé, iVerify).
- Documentation publique de la situation = stratégie protectrice.

**Profil 6 : RSSI ONG terrain (modèle Yann)**

- Qubes OS sur laptops équipe.
- Procédures écrites et formation continue.
- Cloud E2EE collectif (Proton Drive Business ou Tresorit).
- Stack messageries unifiée (Signal pour interne, Wire pour partenaires).
- Audit annuel par tiers de confiance.

**Profil 7 : particulier face à ex-conjoint abusif (cas D)**

- Changement complet de credentials après séparation.
- Nouveau téléphone, nouveau Apple ID / Google.
- Audit physique du domicile (caméras cachées, AirTags, stalkerware).
- Coalition Against Stalkerware ressources.
- Soutien : association locale, juriste, psychologue.
- Compartimentation totale avec l’ancien partenaire (canaux, comptes, lieux).

**Profil 8 : Personnel institutionnel, défense ou industrie sensible

Pour qui : militaires, policiers spécialisés, personnels de renseignement, protection rapprochée, agents pénitentiaires exposés, salariés de sites critiques, cadres de l’industrie de défense, sous-traitants sensibles.
Objectif : éviter qu’un téléphone personnel ou professionnel ne révèle des lieux sensibles, des routines, des domiciles, des proches ou des déplacements opérationnels.

- téléphone personnel interdit ou laissé hors zone sensible ;
- téléphone professionnel ou opérationnel dédié, géré par MDM/EMM ;
- liste blanche d’applications autorisées ;
- absence d’applications gratuites financées par la publicité ;
- localisation désactivée par défaut, activée seulement pour les usages strictement nécessaires ;
- identifiant publicitaire désactivé ou régulièrement réinitialisé ;
- séparation stricte entre usages personnels, professionnels et opérationnels ;
- formation régulière sur les risques AdTech, ADINT et data brokers ;
- procédures écrites : quels appareils sont autorisés dans quels lieux ;
- contrôles réguliers et sanctions internes en cas de non-respect des consignes.

Point clé : pour ces profils, le risque n’est pas seulement la compromission du téléphone. Le simple fonctionnement normal d’applications grand public peut suffire à exposer des données exploitables par un adversaire.

**Profil 9 : profil HVT extrême (combinaison)**

- Qubes OS + GrapheneOS combinés.
- Tor + VPN obfusqué.
- Multiples appareils air-gap pour secrets long terme.
- Procédures forensiques mensuelles (MVT auto-vérification).
- Réseau de soutien (avocats, ONG, contacts médias).
- Documentation publique stratégique.

#### 38.6 Quand simplifier

L’inverse de l’élévation de posture est aussi nécessaire à savoir gérer : quand l’enquête se termine, quand le threat ne s’applique plus, quand on quitte un poste à risque. Démantèlement contrôlé :

- Décommissioning des appareils dédiés.
- Fusion progressive des comptes si justifié.
- Effacement des secrets de l’enquête (en gardant copies légales et archives).
- Retour à un standard durci mais soutenable.

Le sur-durcissement permanent sans justification est aussi une faute opérationnelle.

-----

> 🟩 **À retenir de la Partie 7**
> 
> - L’humain est le principal vecteur d’attaque moderne. Le travail sur soi et son entourage compte autant que la technique.
> - L’IA générative a déplacé les seuils : phishing personnalisé indiscernable, deepfakes audio/vidéo accessibles.
> - Frontières : éteindre vraiment (BFU), burner devices pour pays sensibles.
> - Le droit protège, mais sa connaissance et son usage actif sont nécessaires. Pas d’OPSEC sans cadre légal éclairé.
> - La sécurité est un processus. Routines hebdo/mensuelle/trimestrielle/annuelle.
> - Architectures par profil : la posture suit le threat model, pas le mode.

-----


## Cas de synthèse finaux

> **Pourquoi ces cas** : les chapitres précédents ont introduit briques et concepts. Les cas montrent comment ces briques se combinent dans des scénarios réalistes complets. Chaque cas mobilise plusieurs parties du cours et fait l’objet de renvois croisés explicites. Le **Cas A** clôt le fil rouge de Léa. Les **Cas B, C, D** déploient les autres profils annoncés en avant-propos.

-----
