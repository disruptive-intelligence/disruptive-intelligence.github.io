---
title: Chapitre 11 — Sock puppets, avatars et identités d'enquête
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE II — Cadre juridique, éthique et OPSEC
  - index.md
---

## 11.1 Définition et cadre

Un **sock puppet** (ou avatar, ou identité d'enquête) est un compte créé et opéré par l'analyste qui n'est pas son identité personnelle. Son usage est central dans l'OSINT moderne : sans avatar, l'accès à de nombreuses plateformes (LinkedIn, Telegram, X, Discord, forums) est impossible ou révèle immédiatement l'identité réelle de l'investigateur.

L'avatar est un outil **professionnel**, pas une fausse identité criminelle. Sa création et son usage respectent un cadre éthique et juridique strict. Mal manié, il bascule en infraction d'usurpation d'identité (art. 433-19 CP en France) ou en pratique HUMINT non-déclarée potentiellement frauduleuse.

## 11.2 Typologies d'avatars

**Avatar passif d'observation.** Compte qui n'interagit pas, n'écrit pas, ne contacte personne. Il sert uniquement à voir des contenus accessibles aux comptes connectés mais pas aux visiteurs non identifiés (groupes Facebook privés au sens « visible aux membres », posts LinkedIn nécessitant connexion). C'est l'usage le plus défensif et le moins juridiquement exposé.

**Avatar actif d'observation.** Compte qui interagit légèrement (likes, joindre des groupes ouverts, suivre des comptes publics) pour s'intégrer dans un écosystème observable. Plus exposé juridiquement, à manier avec rigueur.

**Avatar d'élicitation.** Compte qui contacte activement des sources pour les faire parler. **Sortie du périmètre OSINT pur**, bascule en HUMINT. Légitime dans certains cadres (LEA, journalisme avec déontologie stricte) mais exigeant : suppose mandat, suppose limites éthiques, suppose qu'on accepte la responsabilité de manipuler une personne.

**Avatar honeypot.** Compte qui attire des cibles (faux profil amoureux, faux profil candidat, faux profil journaliste). Très exposé juridiquement et éthiquement. À réserver à des cadres LEA strictement encadrés ou à des journalistes avec déontologie publiée.

Pour le présent cours, l'usage par défaut est l'avatar **passif** ou **actif léger**. Les autres usages sortent du cadre OSINT standard.

## 11.3 Légitimité juridique de l'avatar

L'usage d'un avatar reste légitime tant que :

- Il **n'usurpe pas une identité réelle existante** (pas de copie d'une personne réelle).
- Il **n'usurpe pas une qualité protégée** (pas de prétention à être avocat, médecin, policier, journaliste accrédité si on ne l'est pas).
- Il **ne sert pas à commettre une infraction** (escroquerie, harcèlement, atteinte à la vie privée caractérisée).
- Il **respecte les CGU** de la plateforme, ou les violations restent mineures et déontologiquement justifiées.

Sortir de ces limites, c'est entrer en zone pénale ou déontologique fragile. La jurisprudence française reste en évolution sur ces sujets.

## 11.4 Création d'un avatar : éléments constitutifs

Construire un avatar crédible est un travail. Six éléments doivent être cohérents.

**Identité fictive.** Un nom plausible mais non-existant (vérifier qu'il ne correspond pas à une personne réelle identifiable). Générateurs comme **Fake Name Generator** peuvent aider mais il faut vérifier l'unicité. Idéalement, créer un nom plausible pour la juridiction de l'enquête.

**Email dédié.** Adresse créée sur un service privacy-friendly (ProtonMail, Tutanota) ou sur un domaine que vous contrôlez. **Jamais lié au téléphone personnel**.

**Téléphone d'investigation.** Pour les plateformes qui exigent SMS de confirmation. Voir Ch.9 sur la séparation physique.

**Photo de profil.** Trois options :

- **Photo générée par IA** (ThisPersonDoesNotExist et successeurs). Avantage : aucune personne réelle. Inconvénient : les outils de détection IA s'améliorent et certaines plateformes flaguent les photos GAN-classiques.
- **Photo achetée banque image** (Adobe Stock, modèles consentants). Légalité OK si licence respectée, mais risque qu'elle apparaisse ailleurs (recherche inversée par la cible).
- **Photo générée par IA récente** (Midjourney, Flux) avec personnage stylisé. Compromis raisonnable, attention à la détection.

**Bio et histoire.** Cohérence avec l'identité (ville, parcours, profession, intérêts). Pas de vérité personnelle dedans (pas de vraie école, pas de vrai employeur). Suffisamment générique pour ne pas alerter, suffisamment spécifique pour être crédible.

**Réseau social initial.** Quelques posts neutres (paysages, citations, articles partagés), quelques abonnements à des comptes publics neutres. Avatar nu = avatar suspect.

## 11.5 Maturation

Un avatar **fraîchement créé** est suspect. Les plateformes (LinkedIn particulièrement) flaguent les comptes neufs. La maturation consiste à laisser l'avatar **prendre de l'âge** avant utilisation opérationnelle.

**Cadence type.**

- **Mois 1** : créer, compléter profil, 5-10 abonnements neutres, 2-3 posts généraux.
- **Mois 2-3** : poursuivre l'activité légère, abonnements progressifs, quelques interactions (likes sur contenus généraux), pas d'interaction avec cibles potentielles.
- **Mois 4-6** : avatar utilisable pour observation passive. Activité maintenue régulièrement.
- **Mois 6+** : avatar mature, utilisable plus largement (toujours dans le cadre passif/actif léger).

**Implication.** Si vous avez besoin d'avatars opérationnels, vous devez les créer **bien avant** d'en avoir besoin. Un cabinet professionnel maintient un parc d'avatars matures à différents stades.

## 11.6 Cohérence sur la durée

Un avatar bien conçu est trahi par les erreurs de cohérence sur la durée.

**Pièges classiques.**

- **Fuseau horaire incohérent** : avatar « basé à Lyon » qui poste à 3h du matin systématiquement.
- **Lexique trahissant** : l'avatar prétendument anglophone qui utilise des tournures françaises (et inversement).
- **Photo profil unique** : avatar qui n'a jamais d'autre photo, jamais de selfie circonstancié.
- **Activité saisonnière incohérente** : vacances supposées au Pérou en décembre, post de neige à Toulouse le même jour.
- **Inactivité prolongée** : six mois sans activité, puis usage soudain pour l'enquête (signal fort).
- **Réseau corrélé** : tous les avatars d'investigation suivent les mêmes comptes (clustering détectable).

## 11.7 Journal interne des avatars

Pour les cabinets et investigateurs maintenant plusieurs avatars, un **journal interne** est indispensable.

**Champs minimaux.**

- Nom de l'avatar.
- Date de création.
- Plateformes opérées.
- Email associé.
- Téléphone associé.
- IP/VPN utilisés.
- Historique d'activité (cadence, posts, abonnements).
- Enquêtes pour lesquelles utilisé.
- État actuel (actif, dormant, brûlé).
- Date de prochaine action de maintien.

Ce journal est **lui-même hautement sensible** : il révèle l'écosystème complet d'investigation. Stockage chiffré, accès strictement restreint.

## 11.8 Risque d'usurpation et erreurs classiques

**Erreurs récurrentes à éviter.**

- Avatar avec photo de personne réelle (recherche inversée → usurpation).
- Avatar qui se prétend journaliste, avocat, ou policier sans l'être (usurpation de qualité).
- Avatar utilisé pour escroquerie, harcèlement, doxxing (sortie pénale).
- Avatar dont l'email récupère vers l'adresse personnelle.
- Avatar dont le téléphone est le téléphone personnel.
- Avatar dont le numéro de carte bancaire est lié à l'investigateur.
- Avatar accédé depuis le même IP que les autres avatars (clustering plateforme).
- Avatar qui contacte des personnes vulnérables (mineurs, victimes).
- Plusieurs avatars qui se suivent entre eux pour créer une illusion de réseau (détectable).

## 11.9 Durée de vie et renouvellement

Un avatar n'est pas éternel.

**Causes de fin de vie.**

- **Brûlage** : cible le détecte ou suspecte.
- **Suspension plateforme** : LinkedIn, X suspendent régulièrement les comptes flagués.
- **Compromission OPSEC** : l'email associé est leaké, le téléphone est doxxé.
- **Fin d'enquête** : avatar dédié à une affaire, fermé à la conclusion.
- **Obsolescence** : photo, bio devenue trop vintage.

**Cycle.** Maintenir un parc d'avatars en pipeline : 30 % en maturation, 50 % opérationnels, 20 % en fin de vie / archivage.

## 11.10 Avatars en équipe et partage

Si une équipe partage un avatar, l'OPSEC se complique.

**Pratiques.**

- Accès via VPN dédié partagé.
- Mot de passe centralisé chiffré.
- Journal de qui a utilisé quand.
- Pas d'usage simultané (sessions parallèles peuvent flaguer le compte).
- Cohérence comportementale : un membre type a-t-il une cadence ? Tous les utilisateurs doivent s'y conformer.

## 11.11 Avatar et IA : tendance 2026

Les outils de génération IA permettent désormais de créer des avatars avec :

- Photos cohérentes série complète (visage identique sous différents angles, à différents âges, dans différents contextes).
- Posts générés par LLM (à condition de garder une cohérence de style).
- Vidéos courtes deepfake (très risqué juridiquement et déontologiquement, à éviter pour OSINT pur).

**Mais simultanément**, les plateformes développent des détecteurs IA. La course est en cours. L'avatar « 100 % IA » est de plus en plus détectable. Le compromis raisonnable en 2026 : photo générée par IA + bio rédigée par humain (ou LLM avec révision humaine forte) + activité humaine réelle.

## 11.12 Synthèse

| Élément | Bonne pratique |
|---|---|
| Identité | Plausible, non-existante vérifiée, jamais usurpation |
| Email | ProtonMail/Tutanota dédié, jamais lié au personnel |
| Téléphone | Téléphone d'investigation séparé |
| Photo | Génération IA récente OU stock licencié, jamais personne réelle |
| Bio | Cohérente, générique, pas de vérité personnelle |
| Maturation | 3-6 mois avant usage opérationnel |
| Activité | Régulière, neutre, cohérente fuseau horaire/lexique |
| Cloisonnement | IP séparée des autres avatars, VPN dédié si possible |
| Journal | Interne, chiffré, accès restreint |
| Cycle | Pipeline maturation → opérationnel → fin de vie |

L'avatar mature est un actif. Le maintenir demande du temps et de la rigueur. Le compromettre, c'est griller un investissement et potentiellement une enquête.

-----
