---
title: Chapitre 15 — Journal d'enquête, preuve et traçabilité
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 15.1 Pourquoi tenir un journal

Le journal d'enquête est la **mémoire structurée** de l'investigation. Il n'est pas un journal au sens littéraire : c'est un registre opérationnel.

**Fonctions du journal.**

- **Reproductibilité** : un confrère doit pouvoir refaire votre cheminement.
- **Défense** : capacité à justifier chaque conclusion par les actions menées.
- **Auditabilité** : un magistrat, un contre-expert, un commanditaire peut vérifier la rigueur.
- **Mémoire personnelle** : 4 semaines après une enquête, vous ne vous souvenez plus du détail. Le journal sauve.
- **Cotation** : la cotation finale d'un fait dépend de la fiabilité de la source ET de la rigueur de la collecte. Le journal documente la seconde.

## 15.2 Champs minimaux d'une entrée de journal

Chaque action significative produit une entrée de journal avec :

- **Date et heure** précises (timezone explicite).
- **Action menée** (description courte mais claire).
- **Source consultée** (URL ou nom de plateforme, version, paramètres de requête).
- **Sélecteur utilisé**.
- **Résultat** (texte court, ou référence à capture).
- **Capture / hash si applicable** (chemin de fichier dans le dossier d'enquête).
- **Pertinence** (haute / moyenne / faible / aucune).
- **Hypothèse(s) éclairée(s)** (référence à l'IR / l'hypothèse concernée).
- **Cotation préliminaire de la source** (Admiralty A-F).
- **Actions suivantes envisagées** (prochain pivot).

## 15.3 Format pratique

Plusieurs formats sont possibles. Le choix dépend du volume et de la complexité.

**Format A — Markdown structuré (Obsidian).** Un fichier `journal.md` ou un fichier par jour. Tags Obsidian pour entités, IRs, hypothèses. Lié au vault d'enquête.

**Format B — Tableau (Google Sheets chiffré, ou Excel local).** Colonnes structurées. Idéal pour grosses enquêtes avec beaucoup d'actions. Filtrable.

**Format C — Outil dédié (Hunchly).** Hunchly capture automatiquement la navigation web avec horodatage et hash. Génère un rapport. Largement utilisé en OSINT professionnel.

**Format D — Notion (avec prudence OPSEC).** Pour les équipes. Attention au cloud — préférer self-hosted ou outil local pour les sujets sensibles.

## 15.4 Hunchly comme standard

**Hunchly** est devenu le standard de fait pour le journal d'enquête OSINT.

**Fonctionnalités.**

- Capture automatique de chaque page consultée (timestamped + hashed).
- Surlignage de sélecteurs (notations).
- Export en rapport PDF avec captures, hashes, métadonnées.
- Annotations personnelles.
- Compatible Chrome/Firefox via extension.
- Local-first (les données restent chez vous).

**Coût.** Abonnement payant, mais investissement rentable pour usage professionnel.

**Alternatives gratuites.** SingleFile (extension navigateur, capture HTML complet), Wayback Machine pour les pages publiques, captures manuelles + script de hashing.

## 15.5 Captures et préservation

Pour chaque page ou ressource d'intérêt :

**Capture.** PDF complet (Hunchly, ou impression PDF), HTML brut (SingleFile), capture image (Greenshot, ShareX, ou outils OS natifs). Le HTML brut permet une analyse ultérieure du code source ; le PDF est lisible directement.

**Horodatage.** Date et heure précises, en UTC ou avec timezone explicite.

**Hash.** SHA-256 du fichier de capture. Un hash garantit que le fichier n'a pas été modifié après collecte.

**Métadonnées contextuelles.** URL exacte, statut HTTP, redirections éventuelles, version du navigateur.

```bash
# Calcul SHA-256 sous Linux/Mac
sha256sum capture_001.pdf

# Sous Windows
certutil -hashfile capture_001.pdf SHA256
```


## 15.6 Versioning du dossier

Le dossier d'enquête évolue. Le **versioning** permet de tracer l'historique.

**Solutions.**

- **Git** : avec un repo local chiffré. Idéal pour markdown / fichiers texte.
- **Snapshots VeraCrypt** : un conteneur chiffré snapshotté à dates clés.
- **Hunchly export** : génère un rapport horodaté à chaque export.

## 15.7 Reproductibilité

L'enquête est **reproductible** quand un confrère, avec le même journal et les mêmes accès, aboutit aux mêmes conclusions.

**Conditions.**

- Sources documentées avec URL exacte.
- Requêtes documentées (mots-clés, opérateurs).
- Outils documentés avec version.
- Paramètres de configuration documentés.
- Cheminement de pivot reconstructible.

La reproductibilité est l'idéal. La réalité de l'OSINT en 2026 (plateformes qui ferment, archives qui disparaissent) la rend partiellement impossible. L'archivage anticipé (Ch.23) compense.

## 15.8 Pièges classiques du journal

- **Tenue rétroactive** : « je remplis le journal le soir ». Fragmentation, oublis, ré-écritures partielles.
- **Imprécision** : « j'ai cherché sur Google ». Quels mots-clés ? Quelle date ?
- **Pas d'horodatage** : journal sans timestamp est inutilisable.
- **Pas de capture** : URL seule = preuve fragile si la page disparaît.
- **Mélange enquête et notes perso** : journal d'enquête est strictement professionnel.
- **Stockage non chiffré** : journal contient des données sensibles, doit être chiffré.
- **Pas de cotation** : sources non cotées = analyse plus tard impossible.

## 15.9 Synthèse — le journal en cinq règles

1. **Toujours** tenir le journal en temps réel, pas rétroactivement.
2. **Toujours** horodater chaque entrée (avec timezone).
3. **Toujours** capturer (Hunchly, SingleFile, PDF) ce qui compte.
4. **Toujours** hasher les captures (SHA-256).
5. **Toujours** chiffrer le journal (VeraCrypt, LUKS, FileVault).

Un journal négligé est une enquête fragile. Un journal rigoureux est une enquête défendable.

-----
