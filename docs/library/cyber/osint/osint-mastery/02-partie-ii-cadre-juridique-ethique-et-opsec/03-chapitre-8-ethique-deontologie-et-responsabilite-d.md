---
title: Chapitre 8 — Éthique, déontologie et responsabilité de l'analyste
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE II — Cadre juridique, éthique et OPSEC
  - index.md
---

## 8.1 Pourquoi l'éthique au-delà du droit

Le droit pose un plancher, pas un plafond. Un comportement légal peut être profondément non-éthique. L'investigateur OSINT a une responsabilité **déontologique** qui dépasse la conformité juridique stricte.

Trois raisons concrètes.

**Premièrement, l'OSINT touche aux personnes.** Une note d'analyse mal calibrée, une diffusion non maîtrisée, un soupçon présenté comme preuve peuvent causer des dommages réels : licenciement injuste, divorce, atteinte à la réputation, suicide. L'analyste qui produit du renseignement engage une responsabilité morale qu'aucun mandat n'efface.

**Deuxièmement, la légitimité collective de la discipline.** L'OSINT est une discipline jeune. Sa crédibilité dépend de la rigueur éthique de ses praticiens. Un dérapage individuel (doxxing public, harcèlement) entache toute la profession. L'éthique est aussi une question de soutenabilité collective.

**Troisièmement, l'analyste lui-même.** L'OSINT expose à des contenus difficiles (violence, abus, harcèlement, désinformation). Une posture éthique structurée protège la santé mentale du praticien et la qualité de son travail dans la durée.

## 8.2 Les principes fondamentaux

**Proportionnalité.** L'intensité de l'investigation doit être proportionnée à l'enjeu. On n'utilise pas la reconnaissance faciale, le scrapping massif et l'analyse stylométrique pour vérifier une réservation de restaurant. La proportionnalité est aussi un principe juridique (RGPD) — c'est ici un principe éthique structurant.

**Minimisation.** Collecter le strict nécessaire à la finalité. Le RGPD l'impose ; l'éthique le renforce. Toute collecte excédentaire est une intrusion dans la vie privée sans justification.

**Nécessité.** L'investigation doit être nécessaire. Si l'objectif peut être atteint par une voie moins intrusive (entretien direct, consultation officielle), elle doit être privilégiée. L'OSINT n'est pas la première option par défaut.

**Finalité.** Toute collecte a une fin déterminée. La réutilisation des données pour une finalité autre est une trahison du commanditaire et de la personne ciblée.

**Loyauté.** Les méthodes doivent être loyales : pas d'usurpation agressive d'identité, pas de manipulation, pas de pièges techniques. La transparence par défaut, l'opacité par exception justifiée.

**Respect des personnes.** La personne ciblée a une dignité. Elle reste un sujet, pas un objet d'enquête. Le langage du rapport, la formulation des conclusions, le partage des données respectent cette dignité.

## 8.3 Ce qui est éthiquement interdit

Certaines pratiques sont **hors-jeu**, même si elles peuvent être techniquement réalisables et juridiquement ambiguës.

**Doxxing public.** La publication d'informations personnelles d'une personne dans le but de lui nuire, l'exposer à du harcèlement, ou orchestrer une vengeance est interdite. Les forums de doxxing (Kiwi Farms et successeurs) ne sont pas des sources OSINT légitimes — ce sont des dispositifs de harcèlement.

**Harcèlement et stalking.** L'utilisation des compétences OSINT pour suivre, harceler, intimider une personne (ex-conjoint, ex-collègue, manifestant, journaliste) est interdite. Si vous êtes sollicité pour une investigation qui ressemble à du stalking déguisé, vous refusez.

**Surveillance abusive.** Le monitoring permanent d'une personne sans base légale (ex-conjoint, voisin, manifestant) est interdit. Le RGPD l'interdit, l'éthique le renforce.

**Manipulation active de sources.** Créer une fausse situation pour faire parler quelqu'un (faux profil de recruteur pour faire candidater, faux profil amoureux pour faire confier, faux investisseur pour faire diligenter) bascule en HUMINT manipulé et sort du cadre OSINT légitime.

**Violations volontaires des CGU.** Le scraping massif en violation explicite des CGU peut, dans certains pays, exposer pénalement. L'éthique recommande la modération et le respect des CGU autant que possible.

**Diffusion non maîtrisée.** Le partage de données collectées hors du périmètre du mandat (commentaire sur Twitter, brief informel à un confrère, fuite à un journaliste) est une faute professionnelle.

## 8.4 Le doxxing : zone particulièrement sensible

Le **doxxing** mérite un traitement spécifique tant l'incidence est forte.

**Définition.** Publication d'informations personnelles d'une personne (adresse, téléphone, employeur, famille) dans le but de l'exposer, généralement à des fins d'intimidation, vengeance, ou mobilisation hostile.

**Le doxxing est interdit éthiquement et souvent pénalement.**

**Distinction importante.** Un rapport OSINT remis à un commanditaire légitime n'est pas un doxxing — c'est un livrable confidentiel. Le doxxing commence à la **diffusion non maîtrisée à un public hostile**.

**Réflexes.**

- Toujours sécuriser la diffusion du livrable.
- Ne jamais publier d'éléments identifiants sans nécessité.
- En cas de communication publique (presse, conférence), anonymiser systématiquement les exemples.
- Refuser les demandes ambiguës qui ressemblent à de la commande de doxxing.

## 8.5 Cas particulier : les contenus sensibles

L'OSINT expose à des contenus difficiles : violence, abus, terrorisme, harcèlement. Trois cas méritent une attention particulière.

**CSAM (Child Sexual Abuse Material).** Le matériel pédopornographique est pénalement gravissime. Aucune justification (recherche, enquête, curiosité) n'autorise un analyste OSINT privé à le consulter ou le télécharger. **Si vous découvrez du CSAM** : ne pas télécharger, ne pas faire de capture, signaler immédiatement à **Pharos** (en France), **INHOPE** (international), **NCMEC** (US). Les services de police judiciaire ont les habilitations pour traiter, pas vous.

**Contenus terroristes / extrémistes.** Idem. Signalement Pharos. Pas de stockage local. Pas de partage.

**Contenus traumatiques (violence, accidents, morts).** Pour les besoins d'investigation, peut être nécessaire de visionner. Précautions : limiter le temps d'exposition, ne pas stocker plus que nécessaire, débriefer avec collègue, considérer suivi psychologique si exposition fréquente (cf. infra).

## 8.6 Hygiène mentale de l'analyste

L'OSINT prolongé expose à un **stress traumatique secondaire**. Les investigateurs spécialisés CSAM, conflit armé, désinformation politique vivent un coût psychologique réel.

**Réflexes recommandés.**

- Limiter le temps d'exposition aux contenus difficiles (séances cadrées, pauses).
- Ne pas travailler seul sur des sujets lourds — équipe, débrief, soutien.
- Hygiène de séparation pro/perso : VM dédiée, horaires, espace physique séparé.
- Reconnaître les signaux d'alerte (insomnie, ruminations, irritabilité, cynisme).
- Accepter le suivi psychologique si nécessaire — c'est une marque de professionnalisme, pas de faiblesse.

Les grandes organisations OSINT (Bellingcat, ICIJ) ont structuré un soutien psychologique pour leurs équipes. Le free-lance doit s'auto-organiser une équivalence.

## 8.7 Conflits d'intérêts

L'investigateur OSINT peut être confronté à des conflits d'intérêts.

**Cas typiques.**

- Investigation sur un acteur économique concurrent d'un autre client.
- Investigation sur un proche, un ami, un collègue.
- Investigation commanditée par un client dont la finalité réelle vous semble suspecte.

**Réflexes.**

- Déclarer le conflit dès qu'il apparaît.
- Refuser le mandat ou solliciter accord explicite du commanditaire.
- Tenir un registre interne des conflits potentiels.

## 8.8 Secret professionnel et confidentialité

Les données collectées et les livrables produits sont confidentiels. L'analyste est tenu au secret.

**Pratiques.**

- Stockage chiffré, accès restreint.
- Pas de partage non autorisé, même informel.
- Destruction sécurisée à l'expiration de la durée de conservation.
- Non-divulgation des clients (sauf cas où l'investigation est rendue publique par eux).
- Vigilance sur les conversations en lieu public, dans les transports.

## 8.9 Quand refuser une mission

Quelques signaux qui doivent conduire à refuser une mission.

- Mandat flou ou refusé par écrit.
- Finalité réelle suspecte (« je veux des éléments sur mon ex », « je veux faire pression »).
- Demande de doxxing déguisée.
- Demande d'accès à des données non publiques (paie pour un leak, accès à un compte).
- Cible vulnérable (mineur, lanceur d'alerte, opposant politique sous régime hostile).
- Délais ou budgets manifestement insuffisants pour une investigation sérieuse.
- Manque de transparence du commanditaire sur sa propre identité.

Refuser une mission est parfois la décision la plus professionnelle. La capacité à dire non protège le métier.

## 8.10 Vers une déontologie professionnelle structurée

L'OSINT n'a pas encore d'ordre professionnel équivalent au Barreau ou à l'Ordre des médecins. Plusieurs associations posent des chartes (OSMOSIS, AFCOSINT, Bellingcat Code of Conduct). Le mouvement vers une professionnalisation déontologique structurée est en cours en 2026. À titre individuel, adopter une charte éthique écrite, la publier le cas échéant, s'y conformer est un signal de sérieux.

-----
