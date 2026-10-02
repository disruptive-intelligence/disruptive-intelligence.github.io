---
title: 'Chapitre 99 — Cas pratique : OPSEC défensive sur Telegram'
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 99.1 Présentation du cas

Un dirigeant d'organisation reçoit, via Telegram, des messages anonymes le menaçant et révélant des informations personnelles sur sa famille. L'analyste OSINT est mandaté pour :

- Identifier la source des messages.
- Évaluer la menace.
- Renforcer l'OPSEC de la cible.
- Documenter pour suite judiciaire.

## 99.2 Étape 1 — Préservation

**Captures.** Tous les messages reçus, profil du compte expéditeur, photos partagées, liens.

**Hashes**, horodatage.

## 99.3 Étape 2 — Profil du compte expéditeur

**Username.** `@MrAnonymous2026`.

**Photo profil.** Avatar générique.

**Bio.** Vide.

**Numéro.** Masqué (mode anonyme).

**Date de création.** 2 jours avant le premier message.

**Conclusion.** Compte burner créé pour l'opération.

## 99.4 Étape 3 — Pivots

**Username search.** Sherlock sur `MrAnonymous2026` : aucun résultat ailleurs.

**Photo profil reverse search.** Yandex : photo apparaît sur Unsplash (image stock). Non discriminante.

**Analyse stylométrique des messages.** Style soigné, vocabulaire fluent, références culturelles françaises (proverbes, expressions idiomatiques).

## 99.5 Étape 4 — Contenu des messages

**Informations révélées sur la famille de la cible.**

- Nom du conjoint (info publique LinkedIn).
- Nom des enfants (info publique via réseaux sociaux conjoint).
- Lieux fréquentés (école des enfants, club de sport).
- Détails sur l'emploi du temps.

**Conclusion.** L'expéditeur a accès à informations relatives à la famille — soit issues d'OSINT propre, soit issues d'observation physique, soit issues d'un proche.

## 99.6 Étape 5 — Cartographie de l'exposition de la famille

**Recherche.** Que voit-on publiquement sur la famille ?

- Conjoint : LinkedIn public, Instagram public avec photos famille.
- Enfants : tags sur photos Instagram du conjoint.
- École : identifiable via géolocalisation des photos.
- Emploi du temps : posts réguliers permettant déduction.

**Conclusion.** Toutes les informations révélées par l'expéditeur peuvent être obtenues via OSINT sans observation physique. La source est plausiblement un OSINT-savvy adversaire.

## 99.7 Étape 6 — Évaluation de la menace

**Tonalité.** Menaçante mais pas explicitement violente. Niveau intermediate.

**Demande.** Réclamations financières.

**Pattern.** Comparable à pattern d'extorsion classique.

**Conclusion.** Menace réelle mais probablement opérée par acteur isolé ou petit groupe. Pas signature crime organisé.

## 99.8 Étape 7 — Identification de la source

**Limites OSINT.**

- Telegram coopère pour LEA mais pas pour OSINT privé.
- Réquisition judiciaire nécessaire pour obtenir IP et numéro de téléphone derrière le compte burner.

**Action.** Dépôt de plainte (extorsion, harcèlement). Le PNAT ou parquet local peut requérir Telegram (depuis l'arrestation Durov 2024, coopération renforcée).

## 99.9 Étape 8 — Mesures défensives OPSEC

**Pour la cible.**

- Renforcement OPSEC familial : revue des comptes réseaux sociaux du conjoint et enfants, restrictions visibilité.
- Suppression des photos d'enfants identifiables.
- Géolocalisation strippée.
- Communication d'évitement avec l'expéditeur (pas répondre, conserver les messages).
- Plainte pénale.
- Vigilance physique renforcée si menaces persistent.

## 99.10 Étape 9 — Production

**Note au dirigeant.**

> **BLUF.** Les messages anonymes proviennent d'un compte Telegram burner créé pour l'opération. Les informations révélées sont compatibles avec une collecte OSINT exclusive (pas nécessairement observation physique). Le pattern correspond à une extorsion par individu / petit groupe, sans signature crime organisé. **Recommandations : plainte pénale immédiate (réquisitions Telegram), renforcement OPSEC familial, vigilance physique, accompagnement juridique.**

## 99.11 Pédagogie

Ce cas illustre :

- OSINT défensif (protection cible).
- Cartographie de la surface d'attaque personnelle.
- Évaluation de la menace.
- Recours nécessaire à la procédure judiciaire pour pivots techniques (réquisitions plateformes).
- Conseil OPSEC personnel.

-----
