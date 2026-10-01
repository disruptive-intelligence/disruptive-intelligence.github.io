---
title: 'Annexe C — OPSEC analyste : checklists'
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Annexes
  - index.md
---

## C.1 Préparation environnement (avant première session)

- [ ] **Machine dédiée** : ordinateur séparé de l'usage personnel et professionnel courant.
- [ ] **OS dédié** : Whonix (Gateway + Workstation), Tails, ou Qubes OS. Pas Windows / macOS personnel.
- [ ] **Réseau isolé** : connexion Internet séparée si possible (clé 4G dédiée, ou réseau invité, pas réseau corporate principal).
- [ ] **Tor Browser configuré** : mode Safest activé par défaut, vérification version à jour.
- [ ] **VM de manipulation** : VM jetable pour ouvrir échantillons (Windows 10 sandbox, ou Linux jetable).
- [ ] **Outils installés** : Hunchly ou équivalent capture, exiftool, hash utilities, scripts custom.
- [ ] **Pas de comptes personnels** sur la machine (mail perso, RS, banque — interdit).

## C.2 Préparation persona

- [ ] **Pseudonyme unique** non lié à l'analyste ou ses identités antérieures.
- [ ] **Histoire crédible** : background fictif documenté (origine, métier, intérêts).
- [ ] **Style linguistique cohérent** avec l'origine prétendue.
- [ ] **Email jetable** sur service approprié (protonmail, autre).
- [ ] **Compte sur forum cible** : créé avec délai progressif d'activité, pas immédiat.
- [ ] **PGP key dédiée** à la persona, pas réutilisée d'ailleurs.
- [ ] **JID XMPP** dédié sur serveur approprié.
- [ ] **Maintenance** : posts occasionnels même hors investigation pour crédibilité.

## C.3 Pendant chaque session

- [ ] **Vérification Tor Browser à jour** avant lancement.
- [ ] **Mode Safest confirmé** (icône bouclier).
- [ ] **Capture systématique** activée (Hunchly).
- [ ] **Notes en temps réel** : URL visitées, observations, hypothèses.
- [ ] **Pas de comptes personnels** ouverts en parallèle.
- [ ] **Aucun téléchargement direct** sur OS hôte — toujours en VM isolée.
- [ ] **Vérification adresse .onion** sur 2 sources avant accès à un service inconnu.
- [ ] **Pas de JS activé sauf nécessité absolue** identifiée.
- [ ] **Logs OTR/OMEMO** des sessions XMPP archivés.

## C.4 Post-session

- [ ] **Capture finale** complète (Hunchly export, ou archives manuelles).
- [ ] **Hashing** des fichiers téléchargés (SHA-256 minimum).
- [ ] **Documentation chronologique** dans le journal d'investigation.
- [ ] **Pas de copie hors environnement sécurisé** des données collectées.
- [ ] **Snapshot VM** restauré si modifications.
- [ ] **Mise à jour du graphe d'investigation** (entités, relations).

## C.5 Communication équipe

- [ ] **Validation hiérarchie** pour actions sensibles (contact vendeur, paiement, téléchargement).
- [ ] **Briefing pair** sur évolutions importantes.
- [ ] **Coordination autorités** maintenue selon mandat.
- [ ] **Confidentialité** stricte — pas de partage avec tiers non habilités.
- [ ] **Debriefing psychologique** disponible si exposition à contenus difficiles.

## C.6 Signaux d'alerte (compromission persona)

- [ ] **Pseudo identifié** par cibles (contre-investigation, mention « cet acteur est suspect »).
- [ ] **Comportements de contact étranges** (over-cooperation soudaine, demandes inhabituelles).
- [ ] **Tentatives techniques** (envoi de fichiers piégés évidents, liens suspects).
- [ ] **Mentions du nom réel** ou organisation dans communications.
- [ ] **Patterns de surveillance** observés.

→ En cas de signal, **abandonner la persona immédiatement**, ne pas chercher à la « sauver », escalade hiérarchique, debriefing.

---
