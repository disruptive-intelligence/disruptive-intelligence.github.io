---
title: Chapitre 27 — Pivots email, téléphone, username, photo
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 27.1 Le pivot comme opération centrale

Une fois une **identité** confirmée (Ch.26), l'enquête mobilise des **pivots** : opérations qui transforment un sélecteur en plusieurs autres.

**Exemple.** Email → comptes liés sur multiples plateformes → usernames → autres emails → numéros de téléphone → photos → réseaux sociaux secondaires. Chaque pivot ouvre des dimensions nouvelles.

L'analyste maître les pivots fait des progrès **exponentiels** sur une cible. L'analyste qui ne maîtrise que les recherches frontales reste limité.

## 27.2 Pivot email

**Validation de l'email.**

**Hunter.io.** Outil standard. Trouve les emails associés à un domaine. Vérifie la validité.

**Snov.io.** Alternative.

**Email Verifier services.** Vérification SMTP.

**Format guessing.** À partir du nom et du domaine, deviner le format probable (`prenom.nom@`, `pnom@`, `prenom@`, etc.).

**Pivots depuis un email confirmé.**

**Holehe** (open source, gratuit). Liste les comptes en ligne probablement associés à un email. Très large couverture (130+ services).

```bash
holehe marc.delaunay76@gmail.com
```


**Epieos** (epieos.com, freemium). Détection des comptes Google, autres comptes liés. Pivots automatisés.

**GHunt** (open source). Pour comptes Google. Reveal photo profil Google, ID Google, etc.

**HIBP, DeHashed, IntelX.** Recherche dans breaches (Ch.42).

**Hudson Rock.** Stealer logs (Ch.43).

**WHOIS historique.** Si email pre-2018, peut apparaître dans WHOIS de domaines.

**Forums et code public.** Recherche GitHub avec email, forums archivés.

**Cas MIRAGE.** L'email `marc.delaunay76@gmail.com` (déduit MIRAGE 4) ouvre énormément de pivots : Holehe → confirmation présence sur Twitter, Instagram, Pinterest, Spotify, Apple. HIBP → 6 breaches. Hudson Rock → stealer log avec credentials Binance. **Email = sélecteur pivot majeur.**

## 27.3 Pivot téléphone

**Validation du format.** Standards internationaux (E.164). Bibliothèques (libphonenumber Google).

**Outils.**

**Truecaller.** Identification d'un numéro inconnu. Crowdsourcé.

**WhatsApp Web / Telegram.** Vérification de présence (déontologie attentive).

**Numverify, NumValidate.** Validation et opérateur.

**Recherches presse.** Numéros parfois publiés par cible (signature email pro).

**Pivots.**

- Téléphone → WhatsApp profil (photo, statut).
- Téléphone → Telegram profil (si non masqué).
- Téléphone → identité (Truecaller).
- Téléphone → adresse (recherche inverse limitée FR).

**Limites France.** Recherche directe numéro → identité **strictement limitée légalement** hors LEA.

## 27.4 Pivot username

**Sherlock** (open source, GitHub). Standard pour recherche d'username cross-plateformes (300+ sites).

```bash
sherlock mdelaunay76
```


**WhatsMyName** (whatsmyname.app). Alternative web.

**NameCheckup, Knowem.** Alternatives commerciales.

**Méthode.**

1. Tester le username probable.
2. Examiner les hits : photo profil, bio, activité cohérente.
3. Cross-vérification par autres sélecteurs.
4. Cotation prudente (homonymie possible).

## 27.5 Pivot photo

Voir Ch.30 pour reconnaissance faciale détaillée.

**Méthode rapide.**

1. Recherche inversée Yandex / Google Lens.
2. Examen des occurrences.
3. PimEyes / FaceCheck.ID si justification légale (UE).

**Pivots photo.**

- Photo profil partagée entre comptes → indique opérateur commun.
- Photo lieu identifiable → géolocalisation (Ch.48).
- Photo avec EXIF → métadonnées (Ch.29).

## 27.6 Pivot document

Voir Ch.29 pour métadonnées documents.

**Pivots typiques.**

- Métadonnées Office / PDF révèlent auteur, modificateur, logiciel.
- Chemins absolus révèlent identité ou organisation.
- Co-auteurs révèlent réseau.

## 27.7 Méthodologie pivot itératif

**Cycle.**

1. **Sélecteur initial** (nom).
2. **Premier pivot** (LinkedIn → email pro probable).
3. **Validation** (Hunter.io confirme format).
4. **Pivot suivant** (email → Holehe → autres comptes).
5. **Validation** de chaque hit.
6. **Pivot suivant** (comptes → usernames).
7. **Sherlock sur usernames** → autres plateformes.
8. **Pivot suivant** (photos partagées → reverse search).
9. ...

L'enquête s'élargit en arbre, jusqu'à épuiser les pivots productifs ou atteindre la cible des IR.

## 27.8 Arrêt et discipline

**Discipline.** Ne pas se laisser **emporter** par la fascination des pivots. À chaque étape :

- Cet élément sert-il une IR ?
- Si non, est-il pertinent ?
- Si non, ne pas l'inclure.

L'enquête peut produire des centaines d'entités si l'analyste laisse les pivots aller sans contrôle. Discipline = focus sur IR.

## 27.9 Cotation des pivots

Chaque pivot produit des éléments à coter.

**Pivot par sélecteur fort + corroboration multi-sources.** Cotation A1-B2.

**Pivot par sélecteur faible.** Cotation D3-F6 par défaut.

**Pivot par déduction sans confirmation.** Hypothèse, F6 jusqu'à validation.

## 27.10 Outils synthèse

| Pivot | Outils principaux |
|---|---|
| Email validation | Hunter.io, Snov.io |
| Email → comptes | Holehe, Epieos, GHunt |
| Email → breaches | HIBP, DeHashed, IntelX |
| Email → stealer logs | Hudson Rock |
| Téléphone | Truecaller, WhatsApp Web (déontologie) |
| Username | Sherlock, WhatsMyName |
| Photo | Yandex, Google Lens, PimEyes |
| Document | ExifTool |

> **Principe.** Le pivot mature transforme une enquête. Mais le pivot non discipliné égare. Maîtriser les pivots = compétence d'analyste senior.

-----
