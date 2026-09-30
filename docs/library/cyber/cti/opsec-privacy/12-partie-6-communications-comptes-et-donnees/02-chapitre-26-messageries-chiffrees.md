---
title: Chapitre 26 — Messageries chiffrées
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 6 — Communications, comptes et données
  - index.md
---

> **Niveau de posture (cf. Ch 2.6)** : Signal pour tout + WhatsApp avec sauvegarde E2EE activée pour cercle qui ne migrera pas = **Niveau 1**. Signal avec username + iMessage avec Contact Key Verification pour cercle Apple + SimpleX pour quelques contacts particulièrement sensibles = **Niveau 2**. SimpleX comme canal primary + Signal sur GrapheneOS profil dédié + Briar pour offline / manifestations + vérification active des Safety Numbers en personne pour tous les contacts critiques = **Niveau 3**.

## 26.1 Anatomie d’une messagerie chiffrée

À évaluer pour chaque option :

- Protocole de chiffrement et ses propriétés (E2EE par défaut ou opt-in ? Forward secrecy ? Open source ?).
- Identifiant utilisateur requis (numéro, email, pseudonyme, rien).
- Métadonnées exposées au serveur.
- Juridiction du fournisseur.
- Audits indépendants.
- Maturité et adoption (réseau utile).

## 26.2 Signal

**Référence E2EE depuis 2014**. Signal Protocol open source, audité, déployé à 100+ millions d’utilisateurs. Propriétés :

- E2EE par défaut.
- Forward secrecy et PCS via double ratchet.
- Sealed sender : minimise l’information dont le serveur dispose (l’expéditeur d’un message ne lui est visible que sous certaines conditions).
- Numéros de téléphone historiquement requis ; depuis 2024, les **usernames** permettent de partager un identifiant de contact sans révéler le numéro. À comprendre précisément : **l’enregistrement initial du compte requiert toujours un numéro de téléphone** (lié à une SIM/eSIM, donc à un opérateur, donc en pratique à une identité civile dans la plupart des juridictions européennes). Ce que les usernames changent, c’est le partage de l’identifiant entre utilisateurs : tu peux donner ton @username à un nouveau contact sans lui dévoiler ton numéro. **Mais** les personnes qui ont déjà ton numéro dans leur carnet d’adresses continuent de te voir associé à ce numéro selon les réglages côté serveur Signal et le contexte. Pour réduire encore cette exposition, dans les paramètres Signal : « Téléphone » → « Qui peut me trouver par mon numéro » → *Personne*. Cela découple le numéro de la découverte sociale, mais l’enregistrement reste numérocentrique.
- **Disappearing messages** : expiration automatique configurable par conversation.
- **Safety Numbers** : vérification d’identité.

**Limites** :

- Service centralisé : Signal Foundation, basée aux États-Unis. Subpoena possible mais Signal a prouvé en justice ne posséder presque aucune donnée à fournir.
- L’enregistrement nécessite encore un numéro de téléphone (lié à un compte SIM, donc à un opérateur, donc à une identité).
- Apple/Google Play Store : la version officielle passe par eux ; alternative sur le site Signal pour Android.

**Pour qui** : tout le monde. C’est le minimum de l’hygiène 2025-2026.

## 26.3 SimpleX

**Modèle radicalement différent** : pas d’identifiant utilisateur global. Tu communiques via des liens de connexion ou QR codes que tu partages. Aucune base centrale ne sait que tu existes.

**Propriétés** :

- E2EE par défaut (double ratchet, similaire à Signal).
- **Pas de carnet d’adresses uploadé**.
- **Pas de numéro de téléphone** requis.
- Architecture en relais : tu choisis tes serveurs (incluant possibilité d’auto-hébergement).

**Contraintes** :

- UX moins fluide que Signal pour le grand public.
- Cercle social plus restreint (effet réseau plus faible).
- Découverte de nouveaux contacts par échange de lien (frottement à chaque nouvelle relation).

**Pour qui** : journalistes-sources, lanceurs d’alerte, profils où le numéro de téléphone est une corrélation à éviter absolument.

## 26.4 Briar

**Architecture P2P**, sans serveur central. Communications via Tor (par défaut) ou Bluetooth/Wi-Fi local (hors-ligne). Conçu pour environnements répressifs et coupures réseau.

**Cas d’usage** : manifestation, contexte sans internet, isolement réseau. Avec Briar, deux téléphones en proximité Bluetooth peuvent communiquer même sans aucun internet.

**Limites** : pas d’historique cloud, donc perte de téléphone = perte de tout. UX plus complexe. Pas d’appels (que des messages texte et forums).

## 26.5 Matrix / Element

**Décentralisé fédéré**. Chaque utilisateur a un compte sur un *homeserver* (hébergeur). Les homeservers fédèrent : tu peux échanger entre serveurs comme avec email.

**Propriétés** :

- E2EE possible (à activer par salon).
- Auto-hébergement possible (synapse, dendrite).
- Pas de numéro de téléphone requis.

**Limites** :

- E2EE non par défaut historiquement (en train de changer, mais à vérifier).
- Métadonnées : ton homeserver voit tout. Si tu utilises matrix.org, c’est l’organisation Matrix.
- Complexité opérationnelle de l’auto-hébergement.
- Historique des messages côté serveur (selon configuration).

**Pour qui** : communautés open source, ONG avec capacité d’auto-héberger, équipes techniques.

## 26.6 WhatsApp

**Le plus utilisé au monde (~3 milliards d’utilisateurs)**. Signal Protocol (E2EE) pour le contenu des messages. Mais :

- Métadonnées chez Meta (relations, fréquences, timings, statut en ligne).
- Carnet d’adresses uploadé sur les serveurs Meta (par défaut).
- Sauvegardes iCloud/Google Drive **non E2EE par défaut**. À activer manuellement (« Sauvegarde chiffrée de bout en bout ») depuis 2021.
- Intégration profonde aux services Meta.

**Pour qui** : usage avec contacts qui ne migreront jamais ailleurs. Ne pas y faire transiter du sensible. Activer la sauvegarde E2EE.

## 26.7 Telegram

**Confusion fréquente**. Telegram n’est PAS E2EE par défaut. Seuls les **« Secret Chats »** le sont, et :

- Disponibles uniquement en 1-à-1, pas en groupe.
- Pas de synchronisation multi-appareil pour les Secret Chats.
- Protocole maison (MTProto) critiqué par les cryptographes.

Tous les autres chats Telegram (groupes, channels) sont chiffrés en transit *vers les serveurs Telegram*, qui peuvent les lire. Telegram a coopéré sélectivement avec des forces de l’ordre.

**Pour qui** : ne pas y faire transiter du sensible. Telegram est un outil de diffusion (canaux publics, larges groupes), pas une messagerie privée.

## 26.8 iMessage

E2EE par défaut pour les iMessage (textos entre iPhones). SMS classiques (vers Android) : non E2EE.

**Contact Key Verification** (iOS 17.2+) : vérifie cryptographiquement les clés de tes contacts iMessage. Indispensable pour HVT.

**Limites** :

- Écosystème Apple uniquement (avec RCS support partiel en 2024-2025 mais pas E2EE).
- Sauvegardes iCloud : non-E2EE sans ADP activée (Ch 14).
- Pas d’audit indépendant du protocole côté Apple.

**Pour qui** : utilisateurs Apple-only, avec ADP activée et Contact Key Verification. Acceptable pour conversation modérément sensible entre Apple/Apple.

## 26.9 Session, Threema, Wire

- **Session** : fork de Signal sans numéro de téléphone, route via réseau Loki (similaire à Tor). Modèle intéressant, adoption modeste.
- **Threema** : commercial suisse, payant unique, pas de numéro requis. Bonne réputation, niche.
- **Wire** : suisse également, support entreprise. Plus orienté pro.

## 26.10 Choix par threat model

|Profil                |Stack recommandée                                                           |
|----------------------|----------------------------------------------------------------------------|
|Grand public durci    |Signal pour tout, WhatsApp si nécessaire avec sauvegarde E2EE               |
|Journaliste-source    |SimpleX pour canal source, Signal pour le reste                             |
|Activiste avant action|Signal avec disappearing messages, Briar pour offline                       |
|Dirigeant exposé      |Signal + iMessage avec ADP, vérification active des contacts                |
|HVT                   |SimpleX + Signal sur GrapheneOS, vérification systématique, reboot quotidien|

## 26.11 OPSEC messagerie : pratiques

- **Disappearing messages** : activer par défaut sur conversations sensibles. Durée selon contexte (24h, 7 jours, 1 mois).
- **View-once** : pour photos/vidéos. Signal et WhatsApp supportent. Note : capture d’écran possible, défense imparfaite.
- **Safety Numbers** : vérifier en première rencontre avec contact sensible.
- **Audit des contacts** : périodiquement, qui a accès à quoi. Suppression des contacts non utilisés.
- **Notification preview** : désactiver sur écran verrouillé, ou minimiser (nom de l’expéditeur seulement, pas le contenu).

## 26.12 Chat Control / CSAR UE : état du débat 2025-2026

La proposition de règlement « Chat Control » (CSAR — Child Sexual Abuse Regulation) circule en Europe depuis 2022, avec des versions successives. L’idée centrale : obliger les fournisseurs de messageries à scanner les contenus *avant* chiffrement E2EE pour détecter du CSAM (matériel pédopornographique).

**Position des cryptographes** : techniquement impossible sans casser l’E2EE. Le scanning côté client (« client-side scanning ») revient à insérer une backdoor, accessible à toute partie qui contrôlerait le mécanisme à terme. Signal a indiqué qu’il se retirerait de l’UE plutôt que d’introduire un tel scanning. ProtonMail, Threema et la plupart des fournisseurs E2EE européens ont des positions similaires.

**État au moment de la rédaction (2026)** : le dossier reste mouvant et hautement politique. Le Conseil de l’UE a adopté en novembre 2025 une orientation générale ouvrant la porte à un scanning « volontaire » étendu et discutant de plusieurs options sur le scanning obligatoire. En mars 2026, le Parlement européen a soutenu l’extension temporaire de la dérogation ePrivacy (qui autorise déjà certains scans volontaires de contenus non E2EE) jusqu’en août 2027, afin d’éviter un vide juridique pendant que les négociations se poursuivent. Les positions nationales restent contrastées — certains États (notamment l’Allemagne et l’Autriche pendant plusieurs phases) ont exprimé des réserves fortes sur l’atteinte à l’E2EE ; d’autres (France, Espagne, Italie sur certaines périodes) ont soutenu une version exigeante. La présidence tournante du Conseil influence fortement le calendrier.

**Implication pratique pour le lecteur** :

- Le risque que l’E2EE européenne soit affaiblie n’est pas conjuré.
- Le calendrier exact et la forme finale (scanning obligatoire, volontaire étendu, ciblé seulement) restent ouverts.
- Suivi recommandé via *European Digital Rights* (EDRi, https://edri.org), *La Quadrature du Net*, *Patrick Breyer* (eurodéputé qui suit le dossier de près sur https://patrick-breyer.de), et *Center for Democracy & Technology*.
- Pour profils sensibles : ne pas baser sa stack uniquement sur des fournisseurs européens E2EE sans plan B (SimpleX, Briar, hébergement en Suisse hors UE, etc.).

## 26.13 *Fil rouge* — Léa et Karim choisissent SimpleX

Léa reçoit, via une rédaction tierce, un signal que Karim B. veut entrer en contact. Premier échange via une boîte morte ProtonMail. Léa propose : SimpleX, parce que ni Karim ni elle n’ont besoin de révéler leur numéro de téléphone. Karim installe SimpleX sur un téléphone d’occasion qu’il a acheté cash. Première rencontre numérique : Léa envoie un lien d’invitation via le canal ProtonMail. Connexion établie. Vérification : ils s’appellent par appel SimpleX et se lisent les Safety Numbers. Puis, basculement en disappearing messages 24h pour toute la conversation.

-----
