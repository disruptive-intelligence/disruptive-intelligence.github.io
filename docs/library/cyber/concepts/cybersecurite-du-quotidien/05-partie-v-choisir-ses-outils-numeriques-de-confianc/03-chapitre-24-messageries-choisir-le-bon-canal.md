---
title: 'Chapitre 24 — Messageries : choisir le bon canal'
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie V — Choisir ses outils numériques de confiance
  - index.md
---

*Toutes les messageries ne se valent pas. Le critère n'est pas seulement le chiffrement, c'est aussi le contexte d'usage et le destinataire.*

| Canal | Bon usage | Limites / vigilances |
|-------|-----------|---------------------|
| **SMS** | Notifications, messages banals | Non chiffré, expéditeur usurpable (spoofing), inadapté au sensible |
| **iMessage** | Conversations courantes entre Apple, chiffrement de bout en bout entre iPhone | Bascule en SMS non chiffré quand le destinataire n'est pas Apple |
| **WhatsApp** | Échanges quotidiens chiffrés de bout en bout, groupes familiaux/amicaux | Métadonnées collectées par Meta (qui parle à qui, quand, durée) ; sauvegardes cloud parfois non chiffrées par défaut |
| **Signal** | Conversations privées sensibles, référence grand public | Repose sur le numéro de téléphone (en évolution avec les noms d'utilisateur) ; dépend du bon usage et de la sécurité du téléphone des deux côtés |
| **Olvid** | Échanges **très sensibles**, personnalités exposées, contexte souverain, réduction forte des métadonnées | Solution française ; chiffre messages, pièces jointes et appels ; **n'utilise pas le numéro de téléphone** comme identifiant principal ; cherche aussi à protéger les métadonnées (« qui parle à qui ») ; certifications CSPN ANSSI sur des versions et périmètres précis |
| **Telegram** | Communautés, canaux publics, groupes thématiques, veille | Conversations normales **non chiffrées de bout en bout** par défaut — seuls les « chats secrets » 1-à-1 le sont ; pas adapté aux conversations confidentielles par défaut |
| **Tchap** | Messagerie souveraine du secteur public français, chiffrée de bout en bout, gérée par l'administration | À privilégier pour les agents publics dans le cadre d'échanges entre agents quand l'organisation l'a déployée |
| **Email** | Documents formels, communications administratives | Non chiffré par défaut, pièces jointes potentiellement risquées, métadonnées exposées |

**La règle** : le bon canal n'est pas seulement celui qui chiffre, c'est celui qui correspond au **contexte**, au **destinataire** et à la **donnée échangée**. Un RIB ou une photo de pièce d'identité ne s'envoient pas par SMS, par email non chiffré, ou par Telegram en mode normal. Si c'est nécessaire, utiliser un canal chiffré (Signal, Olvid) ou un partage de fichier sécurisé (cf. Ch.25).

**Recommandations selon le contexte** :

- *Conversations privées sensibles d'un particulier* : **Signal** ou **Olvid**.
- *Échanges très sensibles, ou nécessitant une réduction forte des métadonnées* (personnalités exposées, journalisme, sources, contextes à risque) : **Olvid**.
- *Échanges professionnels entre agents publics* : **Tchap** quand déployé par l'administration.
- *Échanges pro entreprise* : la messagerie de l'organisation (Teams, Slack, ou autre selon contrat) avec les conventions internes.

**Note sur Olvid** : Olvid est une solution française de messagerie sécurisée qui ne s'appuie pas sur le numéro de téléphone comme identifiant principal — un point différenciant par rapport à Signal et WhatsApp. La protection vise non seulement le contenu mais aussi les métadonnées (qui parle à qui, quand). Olvid a obtenu des certifications **CSPN** auprès de l'ANSSI ; comme pour toute certification, **elle porte sur une version, une configuration et un périmètre précis** — c'est un signal de sérieux, pas une garantie absolue ni une recommandation universelle.

**Côté agent public** : Tchap est conçu pour les échanges du secteur public avec chiffrement de bout en bout, et permet d'inviter des personnes externes sous certaines conditions. Pour des échanges plus sensibles ou hors du périmètre Tchap, Olvid peut être pertinent quand l'organisation l'a validé.

---

<a id="chapitre-25"></a>
