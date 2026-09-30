---
title: Chapitre 16 — Chaîne de conservation numérique
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 16.1 Du journal à la chain of custody

Le journal d'enquête trace les actions de l'analyste. La **chaîne de conservation** (chain of custody) trace les **éléments de preuve eux-mêmes** : leur origine, leur traitement, leur conservation, leur transmission. C'est un concept emprunté à la criminalistique judiciaire, adapté aux preuves numériques.

L'objectif : garantir qu'**un élément présenté en preuve est bien celui qui a été collecté à l'origine**, sans altération, sans substitution, sans contamination. Cette garantie est ce qui rend l'élément opposable.

## 16.2 Quatre piliers de la chaîne de conservation

**Intégrité.** L'élément n'a pas été modifié depuis sa collecte. Garantie par le hash cryptographique.

**Origine.** L'élément vient d'une source identifiée, traçable. Garantie par la documentation de la collecte (URL, date, méthode).

**Conservation.** L'élément est stocké de manière sécurisée, sans risque d'altération accidentelle ou malveillante. Garantie par chiffrement, sauvegarde, accès restreint.

**Transmission.** Si l'élément est transmis (à un client, un avocat, un magistrat), la transmission est tracée et l'intégrité préservée. Garantie par canal sécurisé et vérification du hash à réception.

## 16.3 Hash SHA-256 : la signature de l'intégrité

Le **hash cryptographique** est la signature mathématique d'un fichier. Un changement d'un seul bit produit un hash totalement différent. SHA-256 est le standard contemporain (SHA-1 et MD5 sont obsolètes pour usage forensique).

**Pratique.**

```bash
# Hash d'un fichier
sha256sum capture_delaunay_linkedin_20260520.pdf
# Sortie : a3f5b...e9c (64 caractères hex)

# Hash récursif d'un dossier (Linux)
find dossier_enquete/ -type f -exec sha256sum {} \; > hashes.txt

# Vérification ultérieure
sha256sum -c hashes.txt
```


Chaque capture importante a son hash, consigné dans le journal. Le hash est conservé séparément du fichier (idéalement signé numériquement ou conservé sur un media différent).

## 16.4 Horodatage et timestamp

L'horodatage prouve **quand** l'élément a été collecté.

**Niveaux d'horodatage.**

**Horodatage simple.** Date et heure consignées dans le journal. Suffisant pour l'enquête interne, mais auto-déclaratif (l'analyste peut, théoriquement, ré-écrire son journal).

**Horodatage matériel** (timestamping qualifié). Un tiers de confiance horodate la donnée. Services européens conformes eIDAS : Universign, DocuSign, certaines API gratuites. Le hash + horodatage est signé par le tiers de confiance et opposable.

**Horodatage blockchain.** Certaines solutions ancrent le hash dans une blockchain publique (OpenTimestamps via Bitcoin), créant un timestamp impossible à falsifier rétroactivement. Pour les enquêtes à fort enjeu judiciaire.

**Pour le journalisme et l'enquête privée.** Horodatage simple en général suffit. Pour les éléments destinés au judiciaire, **horodatage qualifié** recommandé.

## 16.5 Préservation au-delà du fichier

Une capture isolée préserve la donnée. La **chaîne de conservation complète** préserve aussi le contexte.

**Éléments contextuels à préserver.**

- URL exacte (avec paramètres).
- Date/heure UTC de la consultation.
- Statut HTTP (200, 301, etc.).
- Redirections (si A redirige vers B, garder trace).
- Headers HTTP pertinents.
- IP du serveur résolu.
- Capture en plusieurs formats (PDF, HTML brut, parfois screenshots).
- Version du navigateur (Hunchly le fait automatiquement).

Pour les contenus dynamiques (vidéos, lives, contenus JavaScript-rendered), capturer le rendu **et** le source si possible.

## 16.6 Cas particulier : les vidéos et streams

Les vidéos sont des éléments fragiles (peuvent être retirées rapidement).

**Outils.**

- **yt-dlp** (successeur de youtube-dl) : capture multi-plateformes (YouTube, X, Twitch, Telegram, TikTok).
- **OBS** pour enregistrement écran live.
- **Hunchly** capture les pages contenant la vidéo, mais pas toujours la vidéo elle-même.

**Pratique.**

- Télécharger la vidéo en format original (mp4 en général).
- Hash SHA-256 du fichier.
- Capture de la page contenant la vidéo.
- Pour les lives : enregistrement OBS du flux en temps réel.

## 16.7 Conservation et stockage

Le stockage de la chaîne de conservation respecte plusieurs principes.

**Sécurité.**

- Conteneur chiffré (VeraCrypt, LUKS).
- Accès restreint (mot de passe robuste, 2FA si solution le permet).
- Pas de stockage sur cloud grand public (Dropbox, Google Drive personnel).
- Cloud spécialisé chiffré côté client (Tresorit, Proton Drive, ou self-hosted Nextcloud) acceptable.

**Redondance.**

- Sauvegarde sur media physique séparé (disque chiffré offline).
- Géographiquement séparée si enjeu fort.
- Stratégie 3-2-1 : 3 copies, 2 supports différents, 1 hors site.

**Cycle de vie.**

- Durée de conservation alignée sur la finalité (RGPD).
- Destruction sécurisée à expiration (shred, wipe).
- Documentation de la destruction.

## 16.8 Transmission sécurisée

Quand un élément est transmis (au client, à un avocat, à un magistrat) :

**Canal.**

- Email chiffré PGP, ou ProtonMail.
- Service de transfert chiffré (Tresorit Send, Proton Drive partage avec lien).
- Remise physique sur support chiffré pour très sensible.
- **Pas** de WeTransfer / Google Drive partage public.

**Vérification.**

- Le hash est communiqué séparément (autre canal, ou en main propre).
- Le destinataire vérifie le hash à réception.
- Accusé de réception tracé.

## 16.9 Limites OSINT versus forensique judiciaire

La chaîne de conservation OSINT **n'équivaut pas** à la chaîne forensique judiciaire stricte (saisie pénale, scellés, hash devant huissier).

**OSINT.**

- Auto-collectée par l'analyste.
- Hash auto-déclaré (sauf horodatage qualifié).
- Intégrité technique, mais pas d'autorité judiciaire de saisie.
- **Valeur indicative et orientante**, pas évidence pénale autosuffisante.

**Forensique judiciaire.**

- Saisie sous procédure (perquisition, réquisition).
- Scellés, horodatage huissier, contre-signature.
- Hash certifié par expert judiciaire.
- **Valeur probante directe**.

**Implication.** L'OSINT produit du renseignement orienteur, qui peut justifier une enquête judiciaire. Lors de cette enquête, les éléments seront **re-collectés** sous procédure pour acquérir valeur probante. La chaîne de conservation OSINT facilite cette re-collecte (les magistrats savent où chercher), mais ne la remplace pas.

## 16.10 Admissibilité 2026 dans un monde post-deepfakes

L'arrivée des contenus synthétiques sophistiqués (Ch.53-59) complique l'admissibilité judiciaire des preuves numériques. Une vidéo, une photo, un audio peuvent désormais être falsifiés à un niveau qui résiste à l'œil nu.

**Tendance 2026.**

- Provenance chain (C2PA) émerge comme standard de preuve d'authenticité.
- Watermarking (SynthID) commence à se déployer.
- Les magistrats demandent de plus en plus une **expertise d'authenticité** pour les éléments numériques.

**Pour l'analyste OSINT.**

- Documenter la **provenance** de chaque élément (où, quand, comment collecté).
- Conserver les **métadonnées C2PA** si présentes.
- Capturer les éléments dès leur publication originale (pas après recopies multiples).
- Si la pièce est centrale, recommander expertise technique complémentaire.

## 16.11 Synthèse

| Élément | Action |
|---|---|
| Capture | PDF + HTML brut + screenshot, via Hunchly idéalement |
| Hash | SHA-256, consigné séparément |
| Horodatage | Journal + horodatage qualifié si judiciaire |
| Contexte | URL, statut HTTP, redirections, navigateur |
| Stockage | Conteneur chiffré, 3-2-1 backup |
| Transmission | PGP / Proton / Tresorit Send + hash sur autre canal |
| Cycle de vie | Durée alignée finalité, destruction sécurisée tracée |
| Limites | Renseignement orienteur, pas preuve pénale autonome |

La chaîne de conservation n'est pas un luxe — c'est ce qui transforme votre travail en livrable opposable. Sans elle, vous produisez du commentaire.

-----
