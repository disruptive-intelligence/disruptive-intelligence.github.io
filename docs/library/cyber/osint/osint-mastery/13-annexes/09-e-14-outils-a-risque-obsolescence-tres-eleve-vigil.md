---
title: E.14 — Outils à risque obsolescence Très Élevé (vigilance)
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - Annexes
  - index.md
---

Liste des outils dont l'accès / l'existence est particulièrement volatile en 2026, à surveiller au moment de l'enquête :

| Outil | Usage typique | Statut mai 2026 | Alternative |
|---|---|---|---|
| **Nitter** | Miroir X/Twitter | Quasi tous instances down | yt-dlp pour vidéos, archive.today, X API payante |
| **Pushshift** | Reddit archive | Restreint à modérateurs/chercheurs | API Reddit officielle (payante), undelete.pullpush (mirror partiel) |
| **Holehe** | Comptes liés email | Fonctionne partiellement, plateformes bloquent | Combinaisons manuelles, Epieos |
| **GHunt** | Google account info | Restreint régulièrement par Google | Pivots indirects, recherche manuelle |
| **InstaLoader** | Instagram download | Risque CGU Meta, blocages fréquents | Compte invest + Hunchly |
| **Sherlock** | Username cross-plateformes | Mises à jour communauté nécessaires | WhatsMyName en complément |
| **Diverses instances Searx, Whoogle** | Privacy search | Instances ouvrent/ferment | Self-host, multi-instances |
| **CrowdTangle (Meta)** | Recherche réseau social | **Fermé août 2024** | Meta Content Library (chercheurs), Brandwatch |
| **Plus de 50 % des outils crypto on-chain gratuits 2021-2023** | Clustering, attribution | Payants ou abandonnés | Etherscan, Walletexplorer, services payants |

**Discipline.** Tester tout outil sensible **avant** d'en dépendre dans une enquête critique. Documenter l'état au moment de l'usage. Identifier au moins une alternative pour chaque outil critique du parc.


### E.15 — Politique de mise à jour

L'écosystème OSINT évolue **mensuellement**. L'analyste révise son catalogue d'outils **au minimum tous les trimestres** :

- Quels outils n'ont plus de support / sont obsolètes ?
- Quels nouveaux outils sont apparus ?
- Quels outils ont changé de modèle (gratuit → payant) ?
- Quelles modifications d'API ou de fonctionnalités ?

Sources de veille : Bellingcat resources, OSINT Framework, OSINT Combine, Trace Labs, communautés Discord et Reddit (/r/OSINT, /r/cybersecurity).

-----


## ANNEXE F — Checklist OPSEC

Checklist opérationnelle d'OPSEC à appliquer pour toute enquête OSINT. À adapter au niveau de menace (cible peu équipée vs cible étatique).


### F.1 — Avant l'enquête : préparation

**Matériel.**

- [ ] Machine d'investigation dédiée (physique ou VM cloisonnée).
- [ ] Disque dur chiffré (VeraCrypt ou équivalent).
- [ ] Sauvegarde chiffrée 3-2-1.
- [ ] Câble réseau ou Wi-Fi dédié (pas Wi-Fi personnel).

**Réseau.**

- [ ] VPN no-log auditésuite, payé via moyens non-traçants si menace élevée.
- [ ] Tor Browser installé sur VM dédiée.
- [ ] Killswitch VPN activé (déconnexion auto si VPN tombe).
- [ ] DNS over HTTPS / DNS chiffrés (NextDNS, Cloudflare 1.1.1.1).

**Navigateurs.**

- [ ] Profils navigateur séparés (Firefox profils, Brave profils).
- [ ] Extensions privacy (uBlock, Privacy Badger, Cookie AutoDelete).
- [ ] Mode privé activé par défaut.
- [ ] Pas d'extension non vérifiée (risque exfiltration).
- [ ] User-Agent réaliste (pas custom révélateur).

**Comptes d'investigation.**

- [ ] Comptes matures (créés 6-12 mois avant usage critique).
- [ ] Email burner dédié (ProtonMail / Tutanota).
- [ ] Numéros virtuels pour SMS confirmation (TextNow, etc.).
- [ ] Photos avatars cohérentes (pas IA détectable au premier coup).
- [ ] Cohérence biographique entre plateformes.


### F.2 — Pendant l'enquête : pratique

**Captures.**

- [ ] Hunchly activé (toutes pages d'enquête capturées).
- [ ] Hashes calculés sur chaque pièce critique.
- [ ] Horodatage qualifié (OpenTimestamps) sur pièces sensibles.
- [ ] Pas d'usage d'outils en SaaS pour pièces sensibles (préférer locaux).

**Requêtes.**

- [ ] Pas d'usage de Google / Bing direct pour cibles sensibles (privilégier Yandex, DuckDuckGo, ou via Tor).
- [ ] Pas d'usage de WHOIS via service sans VPN.
- [ ] Pas d'usage de Shodan / Censys directement depuis IP traçable à l'analyste.
- [ ] LLMs cloud (Claude, GPT) uniquement pour tâches non-sensibles ; sensibles → LLM local.

**Interactions.**

- [ ] Pas d'interaction directe avec cible (likes, comments, follows) — observation passive uniquement.
- [ ] Pas de message direct.
- [ ] Pas de demande d'amitié / connexion.

**Fichiers.**

- [ ] EXIF strippés sur tout fichier transmis hors workspace chiffré.
- [ ] Aucun fichier non chiffré sur cloud public.
- [ ] Hashage avant transmission, vérification à réception.


### F.3 — Communications

**Avec commanditaire.**

- [ ] Email chiffré (PGP/GPG ou S/MIME).
- [ ] Signal (chiffrement bout en bout).
- [ ] Plateforme dédiée (Tresorit Send, OnionShare).
- [ ] Pas de SMS pour information sensible.
- [ ] Confirmation à réception.

**Stockage des communications.**

- [ ] Chiffrement local.
- [ ] Durée de conservation documentée.
- [ ] Purge programmée.


### F.4 — Niveau de menace : adaptations

**Niveau 1 (cible peu équipée).** OPSEC standard suffisante.

**Niveau 2 (cible compétente).** Renforcer : LLMs locaux, VPN multi-saut, Tor pour requêtes sensibles, durcissement comptes invest.

**Niveau 3 (cible étatique).** OPSEC maximale : Tails sur USB, Whonix VM, jamais de cloud, communications PGP, devices air-gapped pour stockage, possibilité d'analyste itinérant.

**Niveau 4 (urgence vie).** Coopération avec services compétents (DGSI, gendarmerie). L'OSINT privée seule est inadéquate.


### F.5 — Après l'enquête : clôture

**Diffusion.**

- [ ] Rapport chiffré (PAdES, AES).
- [ ] Watermark destinataire si pertinent.
- [ ] TLP marqué.
- [ ] Confirmation à destinataire.

**Archivage.**

- [ ] Stockage chiffré 3-2-1.
- [ ] Durée de conservation documentée.
- [ ] Intégrité vérifiée périodiquement (re-hash).

**Purge.**

- [ ] Données personnelles purgées à fin de période (RGPD).
- [ ] Comptes d'investigation maintenus ou archivés selon usage.
- [ ] LLMs locaux : modèles téléchargés peuvent être conservés (pas de risque).
- [ ] Logs d'enquête conservés ou purgés selon mandat.


### F.6 — Erreurs OPSEC fréquentes à éviter

- Mélanger compte personnel et compte d'investigation.
- Liker / follower par erreur depuis compte invest.
- Oublier VPN sur certaines requêtes.
- Conserver fichiers non chiffrés sur disque pour « gagner du temps ».
- Cloud sync (Dropbox, OneDrive, iCloud) sur fichiers d'enquête.
- Mention du nom du commanditaire dans recherches Google.
- Photos perso accidentellement uploadées avec EXIF.
- Captures contenant URL de l'analyste dans la barre d'adresse.
- Métadonnées de fichiers (auteur Word, chemin) révélant identité analyste.


### F.7 — Audit OPSEC régulier

L'analyste / cabinet audite régulièrement (semestriellement) sa propre OPSEC :

- Test d'attaque hypothétique (que verrait un adversaire ?).
- Mise à jour des bonnes pratiques.
- Renouvellement des comptes d'investigation si compromis.
- Veille sur évolutions menaces et contre-mesures.

> **Principe.** L'OPSEC est une discipline continue, pas un état. Une enquête sans OPSEC, c'est une investigation qui se retournera tôt ou tard contre l'analyste ou son commanditaire.

-----


## ANNEXE G — Modèle de journal d'investigation

Le **journal d'investigation** est la mémoire écrite et structurée de l'enquête. Tout est inscrit, daté, sourcé, coté. Modèle de référence pour usage en vault Obsidian / fichier Markdown local chiffré.


### G.1 — Structure du journal

**Niveau 1 — Index du dossier.**

- Page d'index avec liens vers tous les éléments du dossier.

**Niveau 2 — Sections principales.**

- 0-mandat.md : Mandat reçu et cadrage.
- 1-methodologie.md : Méthodologie spécifique adoptée.
- 2-fiches/ : Dossier contenant les fiches entités.
- 3-journal/ : Dossier contenant les entrées chronologiques.
- 4-pieces/ : Dossier contenant les pièces archivées avec hashes.
- 5-analyse/ : Dossier contenant ACH, matrices, hypothèses.
- 6-livrables/ : Dossier contenant les versions du rapport.


### G.2 — Entrée type de journal

Chaque entrée de journal contient :

```markdown
# Entrée [YYYY-MM-DD-HHmm] [Action]

## Contexte
[Pourquoi cette entrée, dans quel cadre]

## Action conduite
[Quoi exactement : recherche, capture, vérification]

## Sources consultées
- [URL 1] — [date d'accès] — [hash si applicable]
- [URL 2] — ...

## Résultats
[Ce qui a été trouvé]

## Cotation préliminaire
- Source : [A-F]
- Information : [1-6]

## Pivots possibles identifiés
- [Pivot 1]
- [Pivot 2]

## Limites / questions ouvertes
[Ce qui reste à investiguer]

## Liens dossier
- Fiches mises à jour : [[Fiche P-001]]
- Pièces archivées : pieces/[ref]

## Notes méthodologiques
[Bonnes pratiques, leçons, biais détectés]

---
Hash de cette entrée (post-rédaction) : [SHA-256]
```
