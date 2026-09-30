---
title: OPSEC & privacy
source: Cyber/OPSEC_Privacy.md
format: cours
---

*Manuel de sécurité numérique défensive pour journalistes d’investigation, sources, activistes, dirigeants, professionnels exposés et particuliers exigeants (2025-2026)*

-----

## Avant-propos

### Pourquoi ce cours

La plupart des guides de sécurité numérique grand public oscillent entre deux postures stériles : la liste de courses (« installez Signal, prenez un VPN, mettez à jour vos appareils ») et la promesse fantasmatique (« devenez invisible en 30 jours »). Aucune ne forme à raisonner. La première oublie que sans modèle de menace, un outil mal employé est un faux sentiment de sécurité ; la seconde oublie que l’anonymat absolu n’existe pas, et que prétendre le contraire est non seulement faux mais dangereux pour ceux qui en dépendent réellement.

Ce cours prend une troisième voie. Il enseigne **à raisonner** : modéliser sa menace, identifier ses actifs, hiérarchiser les risques, choisir les outils adaptés à un contexte précis, comprendre leurs limites, construire une compartimentation soutenable, et accepter que la sécurité parfaite n’existe pas — mais que la sécurité *suffisante pour son threat model* est atteignable, et durable.

### Public visé

Le cours s’adresse à toute personne ayant des raisons sérieuses de réduire son exposition numérique :

- **Journalistes d’investigation** et **sources** : protection des communications, des documents, des contacts.
- **Lanceurs d’alerte** et **avocats** travaillant sur des sujets sensibles.
- **Activistes** et personnes engagées politiquement, particulièrement dans des contextes répressifs ou ciblés.
- **Personnalités publiques** (politiques, dirigeants, créateurs médiatisés) exposées au doxxing, au harcèlement coordonné ou à l’espionnage économique.
- **Professionnels cyber** (RSSI, analystes, chercheurs en sécurité, threat hunters) qui doivent compartimenter recherche, lab, veille et vie personnelle.
- **Agents** travaillant dans des environnements à contrainte de discrétion.
- **Particuliers exigeants** souhaitant atteindre un haut niveau d’hygiène numérique sans s’enchaîner à un activisme paranoïaque.
- **Victimes potentielles d’adversaires de proximité** (ex-partenaire abusif, harceleur, employeur intrusif) — un threat model souvent ignoré par les cours « cyber » trop orientés État ou APT.

### Ce que ce cours **n’est pas**

- Ce n’est pas un guide pour commettre des infractions ni pour échapper à des autorités judiciaires légitimes.
- Ce n’est pas un manuel d’anonymisation absolue.
- Ce n’est pas une suite de recettes prêtes à l’emploi : chaque chapitre force à réfléchir avant d’agir.
- Ce n’est pas un cours offensif (red team, OSINT investigatif, intrusion). Il est exclusivement défensif.

### Cadre légal et éthique (à lire dès maintenant)

La protection de la vie privée est un droit fondamental garanti par la Convention européenne des droits de l’homme (article 8), la Charte des droits fondamentaux de l’Union européenne (articles 7 et 8) et, en droit français, l’article 9 du Code civil. Le chiffrement est légal en France depuis la LCEN (article 30). Le secret des sources des journalistes est protégé par la loi du 4 janvier 2010 et renforcé par le règlement (UE) 2024/1083 dit *European Media Freedom Act* (EMFA), qui protège notamment les sources journalistiques contre l’usage abusif de spyware par les États membres.

Ces droits ne sont **pas absolus**. Ils s’inscrivent dans un cadre de proportionnalité : ordre public, enquête judiciaire, sécurité nationale peuvent fonder des restrictions, sous contrôle d’un juge. Ce cours respecte intégralement ce cadre. Il n’enseigne pas à dissimuler des activités illicites. Il enseigne à exercer un droit légitime : celui de la confidentialité, de la sécurité personnelle, et de la liberté d’enquête, d’information et d’expression.

Le cadre légal complet est traité au **chapitre 37**.

### Comment lire ce cours

Le cours est conçu pour être lu **dans l’ordre** : chaque partie installe les concepts utilisés par la suivante. Une lecture par picorage est possible mais réduit la valeur des renvois croisés et de la progression du fil rouge narratif.

Les **trois capstones intermédiaires** sont des exercices de mise en pratique. Les **quatre cas de synthèse** finaux mobilisent l’ensemble du cours dans des scénarios complets. Les **neuf annexes** sont des outils opérationnels (matrices, templates, architectures de référence, cadre juridique, cas d’échec OPSEC célèbres, ressources).

### Le fil rouge

Le cours est traversé par un récit. **Léa Martens**, journaliste d’investigation freelance basée à Bruxelles (34 ans), démarre une enquête sensible pour un consortium européen de journalistes : un dossier de corruption transeuropéen impliquant un commissaire européen, une société de surveillance privée et un oligarque proche du Kremlin. Léa commence le cours avec une hygiène numérique « grand public » : Gmail, iPhone non durci, WhatsApp, mots de passe réutilisés, présence active sur LinkedIn et X. Son durcissement progresse au fil des chapitres, avec des erreurs corrigées en cours de route.

Cinq personnages secondaires apparaissent quand un chapitre se prête mieux à un autre profil : **Karim B.**, lanceur d’alerte interne dans une autorité administrative française ; **Sophie R.**, activiste climatique exposée à une surveillance administrative ; **Olivier M.**, dirigeant d’une PME tech cible d’espionnage économique ; **Yann T.**, RSSI d’une ONG des droits humains basée à Genève ; **Anya V.**, opposante politique russe en exil à Berlin.

Le fil rouge n’est pas décoratif. Il illustre les concepts au moment où ils sont abordés.

> 🟨 **Avertissement** : Léa, Karim, Sophie, Olivier, Yann, Anya, Catherine et tous les autres personnages et scénarios du cours (y compris dans les cas de synthèse finaux) sont **fictifs**, même lorsqu’ils s’inspirent de situations réalistes documentées dans la presse et les rapports d’ONG. Toute ressemblance avec des personnes réelles serait fortuite. Les cas nommément cités (Ross Ulbricht, Eldo Kim, Reality Winner, John McAfee, etc.) en Annexe 8 sont, eux, des cas réels publics et judiciairement clos, traités à des fins pédagogiques sur la base de documentation publique.

-----

## Sommaire

- [Partie 1 — Fondations conceptuelles et threat modeling](01-partie-1-fondations-conceptuelles-et-threat-modeli/index.md)
    - [Chapitre 1 — Concepts fondamentaux et notions transverses](01-partie-1-fondations-conceptuelles-et-threat-modeli/01-chapitre-1-concepts-fondamentaux-et-notions-transv.md)
    - [Chapitre 2 — Threat modeling personnel](01-partie-1-fondations-conceptuelles-et-threat-modeli/02-chapitre-2-threat-modeling-personnel.md)
    - [Chapitre 3 — Taxonomie des adversaires](01-partie-1-fondations-conceptuelles-et-threat-modeli/03-chapitre-3-taxonomie-des-adversaires.md)
    - [Chapitre 4 — Cartographie de l’empreinte et grands modèles d’exposition](01-partie-1-fondations-conceptuelles-et-threat-modeli/04-chapitre-4-cartographie-de-lempreinte-et-grands-mo.md)
- [Partie 2 — Identité, compartimentation et hygiène comportementale](02-partie-2-identite-compartimentation-et-hygiene-com/index.md)
    - [Chapitre 5 — OSINT défensif : auditer son propre profil](02-partie-2-identite-compartimentation-et-hygiene-com/01-chapitre-5-osint-defensif-auditer-son-propre-profi.md)
    - [Chapitre 6 — Data brokers, courtiers de données et désinscription effective](02-partie-2-identite-compartimentation-et-hygiene-com/02-chapitre-6-data-brokers-courtiers-de-donnees-et-de.md)
    - [Chapitre 7 — Doxxing : mécanique, prévention et réponse](02-partie-2-identite-compartimentation-et-hygiene-com/03-chapitre-7-doxxing-mecanique-prevention-et-reponse.md)
    - [Chapitre 8 — Réseaux sociaux et exposition publique](02-partie-2-identite-compartimentation-et-hygiene-com/04-chapitre-8-reseaux-sociaux-et-exposition-publique.md)
    - [Chapitre 9 — Compartimentation et hygiène comportementale](02-partie-2-identite-compartimentation-et-hygiene-com/05-chapitre-9-compartimentation-et-hygiene-comporteme.md)
- [Partie 3 — Sécurité matérielle, racine de confiance et isolation](03-partie-3-securite-materielle-racine-de-confiance-e/index.md)
    - [Chapitre 10 — Sécurité matérielle](03-partie-3-securite-materielle-racine-de-confiance-e/01-chapitre-10-securite-materielle.md)
    - [Chapitre 11 — Firmware, UEFI, Secure Boot, TPM et chaîne de démarrage](03-partie-3-securite-materielle-racine-de-confiance-e/02-chapitre-11-firmware-uefi-secure-boot-tpm-et-chain.md)
    - [Chapitre 12 — Chiffrement complet du disque](03-partie-3-securite-materielle-racine-de-confiance-e/03-chapitre-12-chiffrement-complet-du-disque.md)
    - [Chapitre 13 — Air gap, appareils dédiés et environnements isolés](03-partie-3-securite-materielle-racine-de-confiance-e/04-chapitre-13-air-gap-appareils-dedies-et-environnem.md)
    - [Chapitre 14 — Durcissement Windows, macOS et Linux pour le quotidien](03-partie-3-securite-materielle-racine-de-confiance-e/05-chapitre-14-durcissement-windows-macos-et-linux-po.md)
    - [Chapitre 15 — Mobile : iOS durci, Android, GrapheneOS](03-partie-3-securite-materielle-racine-de-confiance-e/06-chapitre-15-mobile-ios-durci-android-grapheneos.md)
- [Partie 4 — Environnements de session sensible](04-partie-4-environnements-de-session-sensible/index.md)
    - [Chapitre 16 — Machines virtuelles, live USB et environnements jetables](04-partie-4-environnements-de-session-sensible/01-chapitre-16-machines-virtuelles-live-usb-et-enviro.md)
    - [Chapitre 17 — Tails, Whonix et Qubes OS](04-partie-4-environnements-de-session-sensible/02-chapitre-17-tails-whonix-et-qubes-os.md)
    - [Chapitre 18 — Qubes OS en pratique](04-partie-4-environnements-de-session-sensible/03-chapitre-18-qubes-os-en-pratique.md)
- [Partie 5 — Réseau, anonymat et navigation web](05-partie-5-reseau-anonymat-et-navigation-web/index.md)
    - [Chapitre 19 — Pile réseau : ce que voit chaque acteur](05-partie-5-reseau-anonymat-et-navigation-web/01-chapitre-19-pile-reseau-ce-que-voit-chaque-acteur.md)
    - [Chapitre 20 — VPN : utilité réelle, limites, choix](05-partie-5-reseau-anonymat-et-navigation-web/02-chapitre-20-vpn-utilite-reelle-limites-choix.md)
    - [Chapitre 21 — Tor : architecture, bridges, services onion, OPSEC](05-partie-5-reseau-anonymat-et-navigation-web/03-chapitre-21-tor-architecture-bridges-services-onio.md)
    - [Chapitre 22 — Wi-Fi, Bluetooth, cellulaire, MAC, IMSI](05-partie-5-reseau-anonymat-et-navigation-web/04-chapitre-22-wi-fi-bluetooth-cellulaire-mac-imsi.md)
    - [Chapitre 23 — AdTech, tracking web,  fingerprinting et ADINT](05-partie-5-reseau-anonymat-et-navigation-web/05-chapitre-23-adtech-tracking-web-fingerprinting-et.md)
    - [Chapitre 24 — Navigateurs, moteurs de recherche et stratégies anti-fingerprint](05-partie-5-reseau-anonymat-et-navigation-web/06-chapitre-24-navigateurs-moteurs-de-recherche-et-st.md)
- [Partie 6 — Communications, comptes et données](06-partie-6-communications-comptes-et-donnees/index.md)
    - [Chapitre 25 — Cryptographie appliquée aux communications](06-partie-6-communications-comptes-et-donnees/01-chapitre-25-cryptographie-appliquee-aux-communicat.md)
    - [Chapitre 26 — Messageries chiffrées](06-partie-6-communications-comptes-et-donnees/02-chapitre-26-messageries-chiffrees.md)
    - [Chapitre 27 — Email, PGP et limites structurelles](06-partie-6-communications-comptes-et-donnees/03-chapitre-27-email-pgp-et-limites-structurelles.md)
    - [Chapitre 28 — Partage sécurisé de fichiers et documents](06-partie-6-communications-comptes-et-donnees/04-chapitre-28-partage-securise-de-fichiers-et-docume.md)
    - [Chapitre 29 — Comptes critiques, authentification et secrets](06-partie-6-communications-comptes-et-donnees/05-chapitre-29-comptes-critiques-authentification-et.md)
    - [Chapitre 30 — Cloud, sauvegardes et chiffrement côté client](06-partie-6-communications-comptes-et-donnees/06-chapitre-30-cloud-sauvegardes-et-chiffrement-cote.md)
    - [Chapitre 31 — Métadonnées et nettoyage de fichiers](06-partie-6-communications-comptes-et-donnees/07-chapitre-31-metadonnees-et-nettoyage-de-fichiers.md)
    - [Chapitre 32 — Paiements, traçabilité financière et cryptomonnaies](06-partie-6-communications-comptes-et-donnees/08-chapitre-32-paiements-tracabilite-financiere-et-cr.md)
- [Partie 7 — OPSEC humaine, opérationnelle et continuité](07-partie-7-opsec-humaine-operationnelle-et-continuit/index.md)
    - [Chapitre 33 — Social engineering, phishing ciblé et spyware mercenaire](07-partie-7-opsec-humaine-operationnelle-et-continuit/01-chapitre-33-social-engineering-phishing-cible-et-s.md)
    - [Chapitre 34 — IA générative, LLM, deepfakes et privacy](07-partie-7-opsec-humaine-operationnelle-et-continuit/02-chapitre-34-ia-generative-llm-deepfakes-et-privacy.md)
    - [Chapitre 35 — OPSEC humaine](07-partie-7-opsec-humaine-operationnelle-et-continuit/03-chapitre-35-opsec-humaine.md)
    - [Chapitre 36 — Voyage, frontières et appareils temporaires](07-partie-7-opsec-humaine-operationnelle-et-continuit/04-chapitre-36-voyage-frontieres-et-appareils-tempora.md)
    - [Chapitre 37 — Cadre juridique et éthique](07-partie-7-opsec-humaine-operationnelle-et-continuit/05-chapitre-37-cadre-juridique-et-ethique.md)
    - [Chapitre 38 — Maintenance opérationnelle, réponse à incident et architectures par profil](07-partie-7-opsec-humaine-operationnelle-et-continuit/06-chapitre-38-maintenance-operationnelle-reponse-a-i.md)
- [Cas A — Léa Martens](08-cas-a-lea-martens.md)
- [Cas B — Sophie Roussel : activiste climat avant manifestation](09-cas-b-sophie-roussel-activiste-climat-avant-manife.md)
- [Cas C — Olivier Mercier](10-cas-c-olivier-mercier.md)
- [Cas D — Particulier face à un ex-conjoint abusif](11-cas-d-particulier-face-a-un-ex-conjoint-abusif.md)
- [Annexes](12-annexes/index.md)
    - [Annexe 1 — Glossaire (120+ termes)](12-annexes/01-annexe-1-glossaire-120-termes.md)
    - [Annexe 2 — Cheat sheets opérationnels](12-annexes/02-annexe-2-cheat-sheets-operationnels.md)
    - [Annexe 3 — Matrice d’outils de référence (2025-2026)](12-annexes/03-annexe-3-matrice-doutils-de-reference-2025-2026.md)
    - [Annexe 4 — Matrices de décision](12-annexes/04-annexe-4-matrices-de-decision.md)
    - [Annexe 5 — Architectures de référence par profil](12-annexes/05-annexe-5-architectures-de-reference-par-profil.md)
    - [Annexe 6 — Templates opérationnels](12-annexes/06-annexe-6-templates-operationnels.md)
    - [Annexe 7 — Cadre juridique comparé (FR / UE / US / UK / CH)](12-annexes/07-annexe-7-cadre-juridique-compare-fr-ue-us-uk-ch.md)
    - [Annexe 8 — Cas célèbres d’échec OPSEC : leçons défensives](12-annexes/08-annexe-8-cas-celebres-dechec-opsec-lecons-defensiv.md)
    - [Annexe 9 — Ressources, formations, communautés](12-annexes/09-annexe-9-ressources-formations-communautes.md)
