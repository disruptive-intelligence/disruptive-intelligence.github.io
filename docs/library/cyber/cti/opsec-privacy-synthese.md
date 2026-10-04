---
title: OPSEC & privacy — synthèse
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy — synthèse.md
format: synthese
resume: 'L''essentiel de l''OPSEC en une page : partir de l''observateur, casser les corrélations, choisir l''outil selon le besoin et ce qu''il ne résout pas.'
revue: '2026-10-04'
---

> Synthèse de mon cours [OPSEC & privacy](opsec-privacy/index.md), complétée par quelques références publiques (sources en fin de page). Chaque partie renvoie au chapitre du cours qui la détaille.

## L'idée centrale

L'OPSEC consiste à identifier, contrôler et protéger les **indicateurs** qui, une fois recoupés, permettraient à un adversaire de déduire ce qu'on veut garder pour soi.[^1] Trois convictions traversent tout le cours :

1. **On se protège contre quelqu'un.** Pas d'anonymat absolu ni d'outil magique : la protection est probabiliste et dépend de l'adversaire.[^1]
2. **Les métadonnées comptent plus que le contenu.** Le chiffrement protège ce qui est dit, presque jamais qui parle à qui, quand et d'où.[^1]
3. **La défense coupe la corrélation, pas l'identification.** Empêcher qu'on identifie un élément est souvent impossible ; empêcher qu'on le relie aux autres, non.[^1]

## Cinq mots qu'on confond

Choisir le mauvais mot, c'est choisir le mauvais outil.[^1][^7]

| Notion | Ce que c'est | Échec typique |
|---|---|---|
| **Vie privée** | Décider qui sait quoi à mon sujet, selon le contexte | Un service garde plus de données que prévu |
| **Sécurité** | Protéger la confidentialité, l'intégrité et la disponibilité de ses actifs | Un compte bien protégé mais à mon nom : sûr, pas anonyme |
| **Pseudonymat** | Un nom de substitution **stable** | Un e-mail de récupération, un paiement, une photo ou un style d'écriture le relie à moi |
| **Anonymat** | Un observateur ne peut attribuer l'action à personne, pas même à un pseudonyme | Une connexion, une empreinte de navigateur ou un horaire réduit le groupe à une personne |
| **Secret** | Une information cachée activement, par son **contenu** | Le contenu est chiffré, mais les métadonnées révèlent la relation |

**Non-associabilité** (*unlinkability*) : deux actions ne peuvent pas être attribuées à la même personne. C'est souvent le vrai objectif, et ce que la compartimentation recherche.[^7]

## Commencer par l'observateur

Avant tout outil, cinq questions (cadre de l'EFF)[^2][^6] :

1. **Que veux-je protéger ?** — identité, comptes (l'e-mail principal concentre souvent les clés de tout le reste), données, appareils, relations, localisation, réputation.
2. **Contre qui ?** — sans inflation (« la NSA me vise ») ni déni (« je ne suis personne » : beaucoup d'attaques sont opportunistes ou viennent de proches).
3. **Avec quelle probabilité ?** — capacité × motivation.
4. **Quelles conséquences si j'échoue ?**
5. **Quelle difficulté suis-je prêt à accepter ?** — la plus oubliée, et la plus importante.

Puis, pour chaque **observateur** (opérateur, FAI, VPN, site, régie publicitaire, hébergeur, banque, employeur, État), noter ce qu'il voit et les **éléments qui permettent de recouper** : adresse IP, champs de récupération d'un compte, numéro de téléphone, identifiants d'appareil, cookies, empreinte du navigateur, fuseau horaire, moyen de paiement, adresse de livraison, style d'écriture, présence physique.[^7]

| | Capacité faible | Capacité moyenne | Capacité forte |
|---|---|---|---|
| **Motivation faible** | Négligeable | Faible | Modéré (opportuniste) |
| **Motivation moyenne** | Faible | Modéré | Élevé |
| **Motivation forte** | Modéré | Élevé | Critique |

On calibre les défenses sur les cases « modéré » et au-delà.[^2] Et on écrit ce que le modèle **ne couvre pas** : c'est là qu'on ne dépense pas d'effort. Voir la fiche [Threat modeling](../notions/threat-modeling.md).[^2]

## Trois surfaces, une chaîne

- **Surface d'attaque** — ce par quoi on peut m'atteindre techniquement (comptes, applications, services).
- **Surface d'exposition** — ce qu'on peut savoir de moi **sans m'attaquer** (publications, courtiers de données, fuites).
- **Surface de corrélation** — ce qui permet de **relier** deux identités ou deux activités.[^1]

L'adversaire procède en trois temps : **identification** (un pseudo, un numéro) → **corrélation** (ce pseudo utilise ce téléphone, qui se connecte depuis cette IP) → **attribution** (c'est cette personne).[^1] C'est au maillon *corrélation* qu'on coupe.

## Qui voit quoi sur le réseau

| Observateur | Voit | Ne voit pas |
|---|---|---|
| **FAI** (sans VPN) | IP, requêtes DNS (sauf DoH), nom du site via SNI (sauf ECH), volumes et horaires | Le contenu HTTPS |
| **VPN** | Mon IP réelle, les destinations, le SNI, les métadonnées | Le contenu HTTPS |
| **Site visité** | IP de sortie, navigateur, empreinte, cookies, tout ce que j'envoie | Mon identité, tant que je ne me connecte pas |
| **Wi-Fi public** | Comme le FAI, sur le trafic non chiffré | Le contenu HTTPS |

Un VPN **déplace** la confiance, il ne crée pas d'anonymat.[^3] Fuites classiques : WebRTC, IPv6 hors tunnel, portails captifs. À vérifier sur `browserleaks.com` ou `dnsleaktest.com`.[^3]

## Compartimenter

Cinq niveaux d'identité : **légale**, **professionnelle**, **pseudonyme stable**, **pseudonyme jetable**, **anonyme**. Ceux qui doivent rester séparés doivent l'être *complètement*.[^4]

| Dimension | Séparation faible | Séparation forte |
|---|---|---|
| **Appareil** | Profils distincts sur un même OS | Appareils physiquement distincts |
| **Compte** | Comptes séparés chez un même fournisseur | Fournisseurs différents selon l'usage |
| **Numéro** | Cartes SIM différentes | Réseaux différents (eSIM, SIM physique, service IP) |
| **Paiement** | Cartes virtuelles différentes | Cartes physiques, espèces, lieux distincts |
| **Lieu et horaire** | Maison et bureau séparés | Lieux et horaires totalement disjoints |

**Les corrélateurs silencieux** — même e-mail, même mot de passe, même pseudo (retrouvable sur des centaines de services), même numéro, même photo de profil, même biographie. Puis, plus fins : style d'écriture, horaires de connexion, contacts communs, empreinte du navigateur, adresse IP.[^4]

## Quel outil pour quel besoin

L'outil répond à un besoin précis ; la dernière colonne dit ce qu'il **ne** règle pas.[^5][^7]

| Besoin | Point de départ | Ce que ça ne résout pas |
|---|---|---|
| Cacher sa navigation au FAI ou au Wi-Fi public | VPN réputé (Mullvad, IVPN) | Le VPN voit tout ; comptes, cookies et empreinte restent |
| Naviguer anonymement | Tor Browser ; Tails pour une session sans trace | Les comptes qu'on ouvre, ce qu'on écrit, la corrélation de trafic à grande échelle |
| Mener une activité pseudonyme dans la durée | Whonix, ou Qubes OS + Whonix | Une compromission de l'hôte, les liens de comportement |
| Échanger avec une source | SimpleX, ou Signal avec nom d'utilisateur | L'appareil saisi déverrouillé, les métadonnées côté appareil |
| Manifester ou rester joignable sans réseau | Briar, téléphone dédié éteint (BFU) | Les caméras, la présence physique |
| Protéger ses comptes critiques | Clé FIDO2 matérielle sur l'e-mail principal | Une procédure de récupération faible, l'ingénierie sociale du support |
| Protéger ses appareils | FileVault, BitLocker + PIN, LUKS2 | Un appareil saisi allumé et déverrouillé (AFU) |
| Payer sans exposer sa carte | Carte virtuelle de sa banque | La banque sait tout ; l'adresse de livraison parle |
| Contourner la censure | Tor avec ponts obfs4 ou Snowflake | Le risque légal local |

## Architectures par profil

| Profil | Socle | Ce qui fait la différence |
|---|---|---|
| **Particulier durci** | Téléphone à jour, disque chiffré, gestionnaire de mots de passe, clé FIDO2 | Une routine mensuelle tenue dans la durée |
| **Journaliste** | Téléphone dédié aux sources, SimpleX + Signal, VPN permanent | Tails pour les sessions sensibles, deux clés FIDO2 |
| **Activiste en manifestation** | Téléphone de manifestation, Signal + Briar | Appareil éteint (BFU), contacts d'urgence sur papier |
| **Dirigeant** | Mode Isolement, appareils de voyage | Procédure anti-fraude au président, formation de l'équipe |
| **Victime de violences conjugales** | Téléphone neuf, nouvel e-mail chiffré | Recherche de logiciel espion, soutien associatif |

[^5]

## Les règles d'or

1. **Séparer avant d'agir.** Une compartimentation ajoutée après coup n'efface pas les liens déjà créés.[^7]
2. **Ne pas se rendre unique.** Trop personnaliser son navigateur rend son empreinte remarquable ; une configuration standard se fond dans la masse.[^7][^8]
3. **Protéger l'appareil.** L'anonymat réseau ne sauve pas un appareil compromis, déverrouillé ou saisi.[^7]
4. **Chiffrer le contenu, réduire les métadonnées.**[^1]
5. **Traiter chaque fournisseur comme un observateur** — VPN, messagerie, hébergeur, banque : chacun voit une partie.[^7]
6. **Préférer ce qui se vérifie** — documentation, audits publics, politique de conservation, plutôt que « chiffrement de niveau militaire ».[^7]
7. **La meilleure OPSEC est celle qu'on tient dans la durée.** Une mesure trop coûteuse finit abandonnée.[^2]
8. **Réévaluer régulièrement** — les services, les lois et les adversaires changent.[^7]

## Ce qui fait tomber

Dans les affaires célèbres, la technique tient presque toujours ; c'est l'humain qui cède, souvent sur un seul point.[^6]

| Affaire | L'erreur | La leçon |
|---|---|---|
| **Silk Road** (Ulbricht, 2013) | Le même pseudo sur un forum public, puis une question technique signée avec son Gmail réel ; un ordinateur saisi ouvert | Un pseudonyme ne croise **jamais** un identifiant civil ; pas d'appareil sensible déverrouillé en public |
| **Fausse alerte à Harvard** (Kim, 2013) | Tor utilisé depuis le Wi-Fi du campus : il était presque le seul à s'en servir à cette heure | Tor cache le contenu et la destination, pas le fait de l'utiliser depuis un réseau surveillé |
| **LulzSec** (« Sabu », 2011) | Une seule connexion sans anonymisation | Une seule erreur suffit, et elle est définitive |
| **Fuite NSA** (Winner, 2017) | Les micro-points jaunes d'une imprimante, et peu de personnes ayant accédé au document | Les documents portent des marques invisibles ; les journaux d'accès réduisent le cercle |
| **McAfee** (2012) | Une photo publiée avec ses coordonnées GPS dans les métadonnées | Nettoyer les métadonnées de tout fichier publié |

> ⚠️ **Cadre légal** — Comprendre une technique ne donne pas le droit de l'utiliser. La vie privée et
> l'anonymat sont légitimes ; s'en servir pour accéder sans droit à un système, contourner une sanction ou
> dissimuler un délit ne l'est pas. Le cours y consacre un chapitre entier.[^9]

## Aller plus loin dans le cours

| Pour… | Lire |
|---|---|
| Les concepts et le threat model personnel | Partie 1 — chapitres 1 à 4 |
| Auditer et réduire son exposition (OSINT défensif, courtiers de données, doxxing) | Partie 2 — chapitres 5 à 9 |
| Matériel, chiffrement de disque, durcissement des OS et du mobile | Partie 3 — chapitres 10 à 15 |
| Tails, Whonix, Qubes OS | Partie 4 — chapitres 16 à 18 |
| VPN, Tor, Wi-Fi, traçage publicitaire, empreinte de navigateur | Partie 5 — chapitres 19 à 24 |
| Messageries, e-mail, partage de fichiers, comptes, métadonnées, paiements | Partie 6 — chapitres 25 à 32 |
| Ingénierie sociale, IA, voyage, droit, maintenance | Partie 7 — chapitres 33 à 38 |
| Quatre profils déroulés de bout en bout | Cas A à D |
| Matrices de décision, modèles, cas d'échec | Annexes 4, 6 et 8 |

## Sources

[^1]: [OPSEC & privacy](opsec-privacy/index.md), chapitre 1 — Concepts fondamentaux et notions transverses.
[^2]: [OPSEC & privacy](opsec-privacy/index.md), chapitre 2 — Threat modeling personnel.
[^3]: [OPSEC & privacy](opsec-privacy/index.md), chapitres 19 et 20 — Pile réseau, VPN.
[^4]: [OPSEC & privacy](opsec-privacy/index.md), chapitre 9 — Compartimentation et hygiène comportementale.
[^5]: [OPSEC & privacy](opsec-privacy/index.md), annexes 4 et 5 — Matrices de décision, architectures par profil.
[^6]: [OPSEC & privacy](opsec-privacy/index.md), annexe 8 — Cas célèbres d'échec OPSEC ; EFF, [Surveillance Self-Defense — Your Security Plan](https://ssd.eff.org/module/your-security-plan).
[^7]: HackTricks, *Offensive Privacy, Attribution Evasion and OPSEC* (rubrique Generic Methodologies & Resources) : approche par l'observateur, règles de base, tableau de décision.
[^8]: W3C — [Mitigating Browser Fingerprinting in Web Specifications](https://www.w3.org/TR/fingerprinting-guidance/).
[^9]: [OPSEC & privacy](opsec-privacy/index.md), chapitre 37 — Cadre juridique et éthique.
