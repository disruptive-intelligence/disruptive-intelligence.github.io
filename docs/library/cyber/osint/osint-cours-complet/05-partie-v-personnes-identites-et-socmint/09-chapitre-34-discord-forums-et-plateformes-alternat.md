---
title: Chapitre 34 — Discord, forums et plateformes alternatives
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE V — Personnes, identités et SOCMINT
  - index.md
---

## 34.1 Discord : la plateforme dominante 2026

**Discord** (lancé 2015, orienté gaming initialement) est devenu en 2026 l'une des plateformes principales pour communautés thématiques, projets crypto, criminalité organisée, désinformation politique.

**Caractéristiques.**

- Serveurs (équivalents groupes Slack/Telegram, structure en channels).
- Channels (text, vocal, vidéo).
- Voix permanentes (audio chat continu).
- Rôles et hiérarchies internes.
- Bots programmables très puissants.
- Stages, événements live.

**Volume.** 200+ millions d'utilisateurs mensuels.

## 34.2 Restrictions et accès Discord

**Limites OSINT.**

- Pas d'API publique pour observation tiers (uniquement bots dans serveurs où on est admis).
- Recherche cross-serveur impossible.
- CGU strictes contre observation.
- Modération réactive (suppression de comptes suspects).

**Stratégie.**

- Compte d'investigation Discord mature.
- Adhésion aux serveurs publics ou via invitations.
- Observation passive, pas d'interaction sauf nécessité.
- Capture systématique.

## 34.3 Méthodes de capture Discord

**DiscordChatExporter** (Tyrrrz, GitHub) : outil open source qui exporte les channels d'un serveur dont vous êtes membre. Export en HTML, JSON, CSV, TXT.

**Usage.** Compte invest membre → export → archivage local. Respecter les CGU est tendu (export massif peut violer CGU).

**Captures manuelles.** Screenshots horodatés + hash. Méthode forensique stricte.

**Bots de logging.** Pour serveurs où on a droits admin (consentement explicite).

## 34.4 Pivots Discord

- **Username Discord** → pivot Sherlock multi-plateformes (souvent réutilisé).
- **Avatar** → recherche inversée.
- **Servers communs** révèlent intérêts, milieux.
- **Mentions** révèlent réseau.

## 34.5 4chan, 8kun et l'imageboard underground

**4chan** (créé 2003) et son fork **8kun** (anciennement 8chan) sont des imageboards anonymes, sources majeures de :

- Génération de mèmes politiques.
- Désinformation et harcèlement coordonné.
- Communautés extrémistes.
- Subcultures internet.

**Méthodologie.**

- Consultation prudente (contenu potentiellement traumatique, dont CSAM épisodique sur certaines boards — refus immédiat de consultation, signalement).
- Outils : **4plebs** (archive 4chan), **archive.4plebs.org**.
- Pas d'interaction.

**OPSEC.** Tor recommandé.

## 34.6 Forums clandestins de surface

Au-delà de 4chan, plusieurs forums hostent des activités borderline ou criminelles.

**Exemples (compréhension, pas accès).**

- **BreachForums** et ses successeurs (vente de leaks).
- **RaidForums** (historique, fermé par LEA 2022).
- **XSS, Exploit** (forums russophones cybercriminels).
- **Dread** (forum dark web, accessible via Tor).

**Approche OSINT.**

- Forums **de surface** : consultation possible, OPSEC stricte.
- Forums **dark web** : voir Ch.44 (panorama) et Dark Web vFULL pour profondeur.

## 34.7 VKontakte (VK)

**VK** (vk.com) est le « Facebook russe », dominant en CEI.

**Usage OSINT.**

- Investigation sur cibles russophones.
- Recherche d'identités, photos, groupes.
- API plus ouverte que Facebook (mais évolutive).

**Outils.** Search engines russes, scripts VK API, **220vk** (outil OSINT VK dédié).

**OPSEC.** Service russe, requêtes loguées potentiellement. VPN.

## 34.8 OK.ru (Odnoklassniki)

**OK.ru** : « Copains d'avant russe », orienté plus 30+ ans, fortement utilisé CEI.

**Usage OSINT.**

- Investigation cibles slaves, anciennes générations.
- Photos de famille, événements.
- Souvent moins protégé que VK ou Facebook.

## 34.9 Plateformes asiatiques

**Weibo** (Chine) : Twitter chinois. Très utilisé. Censure forte.

**Baidu Tieba** (Chine) : forums Baidu.

**KakaoTalk** (Corée).

**Line** (Japon, Asie du Sud-Est).

**Naver Cafe** (Corée) : forums.

Spécificités OSINT : langues locales (besoin traduction), restrictions politiques (Chine), faible présence outils OSINT internationaux.

## 34.10 Autres plateformes émergentes

**Session.** Successeur Signal anonyme. Pas de numéro de téléphone requis. Utilisé dans certaines communautés cybercriminelles.

**Signal usage public.** Channels et groupes Signal publics émergent. Limité par design.

**SimpleX.** Application chiffrée sans identifiant utilisateur. Émergente.

**Matrix / Element.** Federated. Pour communautés tech et activistes.

## 34.11 Synthèse — plateformes alternatives

| Plateforme | Région / usage | Accessibilité OSINT |
|---|---|---|
| Discord | Mondial, communautés | Compte invest, observation passive |
| 4chan / 8kun | Mondial anonyme | Consultation prudente, outils archive |
| Forums clandestins surface | Mondial | OPSEC stricte, observation |
| VK / OK.ru | CEI | Compte invest, VPN |
| Weibo / Tieba | Chine | Compte invest, traduction, VPN |
| Session / SimpleX | Anonymat fort | Limité |
| Matrix | Tech/activistes | API ouverte |

-----
