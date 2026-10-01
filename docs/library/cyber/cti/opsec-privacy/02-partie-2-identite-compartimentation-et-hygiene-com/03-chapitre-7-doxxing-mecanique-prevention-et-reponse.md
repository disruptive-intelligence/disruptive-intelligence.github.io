---
title: 'Chapitre 7 — Doxxing : mécanique, prévention et réponse'
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 2 — Identité, compartimentation et hygiène comportementale
  - index.md
---

## 7.1 Définition et formes

Le **doxxing** (parfois orthographié *doxing*) consiste à révéler publiquement des informations personnelles identifiantes (nom réel, adresse, employeur, contacts familiaux, photos privées) sur une cible, dans une intention nuisible : harcèlement, intimidation, atteinte professionnelle, violences physiques par procuration.

Formes principales :

- **Doxxing classique** : publication d’une fiche identifiante.
- **Swatting** : appel des forces d’intervention à l’adresse de la cible sous prétexte fallacieux. Documenté avec des morts aux États-Unis. Risque croissant en Europe.
- **Harcèlement coordonné** : campagne organisée (raid sur un compte, signalements coordonnés, messages massifs).
- **Doxxing par deepfake** : association de la cible à des contenus fabriqués (cf. Ch 34).
- **Doxxing patrimonial** : révélation d’informations sur la famille, les enfants, l’école, le lieu de travail.

## 7.2 Anatomie d’une opération de doxxing

Une opération typique suit cinq phases :

1. **Trigger** : action de la cible (publication, prise de position, conflit en ligne) qui motive l’attaque.
1. **Reconnaissance** : OSINT sur la cible (cf. Ch 5 inversé).
1. **Compilation** : assemblage d’une fiche avec les informations agrégées.
1. **Publication** : sur un forum hostile, un site dédié, ou via des canaux de chat.
1. **Amplification** : appel à harcèlement de masse.

La défense efficace agit aux phases 2 et 3 : réduire ce qui est trouvable, casser les corrélations qui permettent l’assemblage.

## 7.3 Profils particulièrement ciblés

Les données disponibles (rapports PEN America, Online Harassment Field Manual, Coalition Against Online Violence) identifient comme cibles surreprésentées : femmes journalistes, journalistes traitant de l’extrême-droite ou des questions de genre, activistes LGBTQ+, chercheurs sur les mouvements extrémistes, victimes de gamergates et de raids ciblés, témoins dans des affaires sensibles.

## 7.4 Prévention structurelle

Sept axes prioritaires :

1. **Adresse postale alternative** : boîte postale, domiciliation commerciale (légale, ~15-30€/mois), ou adresse d’un proche consentant. À utiliser pour tout enregistrement public, livraisons sensibles.
1. **Téléphone séparé** : un numéro pro distinct du numéro principal — eSIM, MVNO, ou service comme MySudo (US), JMP.chat. Ce numéro filtre les contacts professionnels.
1. **Hygiène photo** : éviter les arrière-plans identifiants, les marquages industriels (entreprises locales), les vues par fenêtre permettant la géolocalisation visuelle (cf. Ch 35).
1. **Audit de l’entourage** : tes proches publient-ils ton nom, ton adresse, tes photos ? Conversation diplomatique recommandée.
1. **Compartimentation des plateformes** : ton compte professionnel n’a pas besoin de mentionner ton compte personnel, et inversement.
1. **Filtrage des questions de récupération** : pas de question dont la réponse est dans tes posts publics (« nom de ton chien »).
1. **Surveillance proactive** : Google Alerts sur ton nom, monitoring HaveIBeenPwned (notifications automatiques de nouvelles fuites).

## 7.5 Réponse à doxxing en cours

Si tu es la cible d’un doxxing actif :

1. **Documenter** : captures d’écran, URLs, horodatages. Préserver les preuves avant suppression éventuelle.
1. **Signaler aux plateformes** : la plupart ont des procédures spécifiques anti-doxxing (X, Reddit, GitHub, Discord, etc.).
1. **Contacter les hébergeurs** (si nécessaire) : un site dédié peut être signalé à son hébergeur, à son registrar, et à son CDN.
1. **Évaluer la menace physique** : si l’adresse est publiée et qu’il y a menace crédible, prévenir les autorités, envisager un changement temporaire de logement.
1. **Soutien psychologique et juridique** : pas un détail. Le doxxing est traumatisant. PEN America, GIJN, RSF, La Quadrature, Reporters Sans Frontières proposent des aides selon les profils.
1. **Plainte** : en France, le doxxing peut tomber sous plusieurs qualifications (atteinte à la vie privée, violation du secret des correspondances, mise en danger délibérée, harcèlement). PHAROS pour le signalement.

## 7.6 *Fil rouge* — Léa découvre son adresse sur un forum

Trois semaines après une publication intermédiaire sur son enquête, Léa reçoit une capture d’écran d’un canal Telegram : son adresse postale, son numéro de téléphone, et le nom de son père y sont publiés, avec « cette journaliste mérite une visite ». Application immédiate de la procédure ci-dessus. Mise en alerte de son entourage proche. Dépôt de plainte. Et surtout, leçon : son adresse était dans le registre du commerce belge (entreprise individuelle) — elle bascule en SCI avec domiciliation commerciale dans la semaine.

-----
