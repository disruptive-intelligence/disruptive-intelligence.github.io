---
title: Chapitre 23 — Archivage et préservation web
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IV — Moteurs, recherche web et restrictions plateformes
  - index.md
---

## 23.1 L'archivage anticipé comme stratégie

Le web est **éphémère**. Une page peut être modifiée, retirée, censurée à tout moment. Un compte peut être supprimé. Une vidéo peut être démonétisée et masquée. En 2026, avec la fermeture progressive des plateformes, l'éphémérité est devenue **un risque opérationnel majeur**.

L'**archivage anticipé** est devenu une stratégie défensive et offensive : capturer dès que vous voyez, ne pas attendre que la page soit citée dans le rapport. Une page non archivée à la date de consultation est une page que vous pouvez perdre.

## 23.2 Wayback Machine (Internet Archive)

**Wayback Machine** (web.archive.org) est l'archive web la plus large du monde, opérée par Internet Archive (ONG).

**Usage.**

- **Consultation.** Voir les versions historiques d'une URL.
- **Sauvegarde manuelle.** Soumettre une URL pour archivage (`web.archive.org/save/[URL]`).
- **Sauvegarde via API.** Automatisable pour des batches.
- **CDX search.** Recherche sur les archives existantes (`web.archive.org/cdx/search/cdx`).

**Forces.**

- Gratuit, ouvert, large couverture.
- Historique parfois très profond (snapshots quotidiens des sites majeurs).
- Standard de fait pour citer des archives en investigation.

**Limites.**

- Pas tout est archivé (sites bloquant les crawlers, contenu derrière login).
- Snapshots irréguliers pour sites mineurs.
- Délais avant indexation.
- Risque de suppression sur demande (rare mais possible).

## 23.3 archive.today

**archive.today** (ou archive.ph, archive.is) est complémentaire à Wayback.

**Forces.**

- Archive sur demande (snapshot immédiat).
- Capture meilleure du JavaScript-rendered content.
- Captures les pages Twitter/X mieux que Wayback.
- Pas affecté par les protections anti-crawler de certains sites.
- Snapshots persistants.

**Limites.**

- Pas de recherche full-text.
- Modèle économique opaque.
- Disponibilité variable.

**Combinaison.** Pour chaque archive critique : sauvegarder sur **Wayback Machine** ET **archive.today**. Redondance défensive.

## 23.4 Conifer et Webrecorder

**Conifer** (conifer.rhizome.org) et **Webrecorder** offrent des solutions de capture web interactive : on enregistre une session de navigation complète (clics, scrolls, formulaires), pas juste une page.

**Cas d'usage OSINT.**

- Capturer une expérience utilisateur complète (formulaire interactif).
- Préserver une exploration de carte.
- Archiver une vidéo embarquée avec ses contrôles.

**Format.** WARC (Web ARChive), standard open archive.

## 23.5 SingleFile : capture HTML complète

**SingleFile** (extension navigateur, gratuit) capture une page web complète dans un fichier HTML unique (HTML + CSS + images + scripts inlinés).

**Avantages.**

- 100 % local.
- Pas de dépendance à un service tiers.
- Hash directement calculable.
- Lisible hors-ligne par n'importe quel navigateur.

Indispensable pour les pages très sensibles ou éphémères que vous voulez préserver souverainement.

## 23.6 Hunchly : la solution professionnelle

**Hunchly** est traité au Ch.15 pour son rôle de journal. Côté archivage, il capture **automatiquement chaque page consultée** pendant une session d'investigation, avec horodatage et hash. Génère un rapport complet exportable.

C'est la solution **professionnelle** de référence pour archivage couplé à investigation.

## 23.7 FAW (Forensic Acquisition of Websites)

**FAW** est un outil professionnel forensique pour acquisition web. Plus lourd que Hunchly, orienté procédure judiciaire stricte (hash légaux, certificats horodatés). Utilisé en LEA et en expertise judiciaire.

## 23.8 Captures vidéo

Pour les vidéos (YouTube, X, Telegram, TikTok, Twitch) :

**yt-dlp.** Successeur de youtube-dl. Multi-plateformes. Téléchargement direct, format original.

```bash
yt-dlp [URL]
yt-dlp --write-info-json [URL]   # avec métadonnées
yt-dlp -f bestvideo+bestaudio [URL]   # qualité max
yt-dlp --list-formats [URL]   # voir formats disponibles
```


**OBS** pour enregistrement live (streams Twitch, YouTube Live, X Spaces).

**Streamlink** pour téléchargement de streams.

**Combiné.** Téléchargement du média + capture de la page (Hunchly/SingleFile) + hash + métadonnées.

## 23.9 Archivage Telegram

**Telegram** pose un défi spécifique : volume massif, contenu éphémère, restrictions API.

**Méthodes.**

- **TGStat / Telemetr.io** : statistiques de canaux publics.
- **Telegram Desktop + export** : pour canaux où on est membre.
- **Scripts Python (Telethon, Pyrogram)** : automatisation conforme aux CGU et limites API.
- **Telegago** : moteur de recherche Telegram (canaux publics).

**Captures.** Screenshots horodatés + hash + export JSON du canal si possible.

## 23.10 Archivage Discord

**Discord** est encore plus restrictif. Pas d'API publique pour observation tiers, CGU strictes.

**Méthodes.**

- **DiscordChatExporter** (Tyrrrz, GitHub) : export des conversations dont vous êtes membre. Usage déontologique strict.
- Captures manuelles + horodatage + hash.
- Pour observation passive, accès limité à votre fenêtre membre.

## 23.11 Archivage de livestreams et événements éphémères

Pour les événements en direct (X Spaces, Twitter Spaces, YouTube Live, Twitch streams) :

- **Enregistrement en temps réel.** OBS, Streamlink. Lancer dès que vous identifiez l'événement.
- **Multi-flux.** Si critique, deux machines redondantes.
- **Métadonnées.** Date, heure, intervenants apparents, hash du fichier final.

**Cas d'usage OSINT.** Un dirigeant qui parle sur X Spaces une seule fois et le retire ensuite. Une diffusion live d'événement controversé. Une intervention politique non rediffusée.

## 23.12 Stratégie d'archivage par sensibilité

| Sensibilité du contenu | Stratégie d'archivage |
|---|---|
| Public stable | Wayback + lien dans journal |
| Public éphémère | Wayback + archive.today + capture locale |
| Critique pour enquête | Wayback + archive.today + Hunchly + SingleFile + hash |
| Judiciaire | Tout ci-dessus + horodatage qualifié + FAW si dispo |
| Vidéo importante | yt-dlp + capture page + hash + métadonnées EXIF |
| Live éphémère | OBS dual-stream + hash final |

## 23.13 Outils en évolution rapide

L'écosystème change. En 2026, surveiller :

- L'évolution de Wayback Machine (financement, politique de retrait).
- Les nouvelles solutions de capture mobile.
- Les outils dédiés au capture des contenus AI-generated (provenance C2PA).
- Les outils d'archivage de **dark web** spécifiques (Onionland, OnionScan).

-----
