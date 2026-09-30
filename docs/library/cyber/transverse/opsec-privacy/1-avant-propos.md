---
title: Avant-propos
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 1
chapters: 8
---

## Pourquoi ce cours

La plupart des guides de sécurité numérique grand public oscillent entre deux postures stériles : la liste de courses (« installez Signal, prenez un VPN, mettez à jour vos appareils ») et la promesse fantasmatique (« devenez invisible en 30 jours »). Aucune ne forme à raisonner. La première oublie que sans modèle de menace, un outil mal employé est un faux sentiment de sécurité ; la seconde oublie que l’anonymat absolu n’existe pas, et que prétendre le contraire est non seulement faux mais dangereux pour ceux qui en dépendent réellement.

Ce cours prend une troisième voie. Il enseigne **à raisonner** : modéliser sa menace, identifier ses actifs, hiérarchiser les risques, choisir les outils adaptés à un contexte précis, comprendre leurs limites, construire une compartimentation soutenable, et accepter que la sécurité parfaite n’existe pas — mais que la sécurité *suffisante pour son threat model* est atteignable, et durable.

## Public visé

Le cours s’adresse à toute personne ayant des raisons sérieuses de réduire son exposition numérique :

- **Journalistes d’investigation** et **sources** : protection des communications, des documents, des contacts.
- **Lanceurs d’alerte** et **avocats** travaillant sur des sujets sensibles.
- **Activistes** et personnes engagées politiquement, particulièrement dans des contextes répressifs ou ciblés.
- **Personnalités publiques** (politiques, dirigeants, créateurs médiatisés) exposées au doxxing, au harcèlement coordonné ou à l’espionnage économique.
- **Professionnels cyber** (RSSI, analystes, chercheurs en sécurité, threat hunters) qui doivent compartimenter recherche, lab, veille et vie personnelle.
- **Agents** travaillant dans des environnements à contrainte de discrétion.
- **Particuliers exigeants** souhaitant atteindre un haut niveau d’hygiène numérique sans s’enchaîner à un activisme paranoïaque.
- **Victimes potentielles d’adversaires de proximité** (ex-partenaire abusif, harceleur, employeur intrusif) — un threat model souvent ignoré par les cours « cyber » trop orientés État ou APT.

## Ce que ce cours **n’est pas**

- Ce n’est pas un guide pour commettre des infractions ni pour échapper à des autorités judiciaires légitimes.
- Ce n’est pas un manuel d’anonymisation absolue.
- Ce n’est pas une suite de recettes prêtes à l’emploi : chaque chapitre force à réfléchir avant d’agir.
- Ce n’est pas un cours offensif (red team, OSINT investigatif, intrusion). Il est exclusivement défensif.

## Cadre légal et éthique (à lire dès maintenant)

La protection de la vie privée est un droit fondamental garanti par la Convention européenne des droits de l’homme (article 8), la Charte des droits fondamentaux de l’Union européenne (articles 7 et 8) et, en droit français, l’article 9 du Code civil. Le chiffrement est légal en France depuis la LCEN (article 30). Le secret des sources des journalistes est protégé par la loi du 4 janvier 2010 et renforcé par le règlement (UE) 2024/1083 dit *European Media Freedom Act* (EMFA), qui protège notamment les sources journalistiques contre l’usage abusif de spyware par les États membres.

Ces droits ne sont **pas absolus**. Ils s’inscrivent dans un cadre de proportionnalité : ordre public, enquête judiciaire, sécurité nationale peuvent fonder des restrictions, sous contrôle d’un juge. Ce cours respecte intégralement ce cadre. Il n’enseigne pas à dissimuler des activités illicites. Il enseigne à exercer un droit légitime : celui de la confidentialité, de la sécurité personnelle, et de la liberté d’enquête, d’information et d’expression.

Le cadre légal complet est traité au **chapitre 37**.

## Comment lire ce cours

Le cours est conçu pour être lu **dans l’ordre** : chaque partie installe les concepts utilisés par la suivante. Une lecture par picorage est possible mais réduit la valeur des renvois croisés et de la progression du fil rouge narratif.

Les **trois capstones intermédiaires** sont des exercices de mise en pratique. Les **quatre cas de synthèse** finaux mobilisent l’ensemble du cours dans des scénarios complets. Les **neuf annexes** sont des outils opérationnels (matrices, templates, architectures de référence, cadre juridique, cas d’échec OPSEC célèbres, ressources).

## Le fil rouge

Le cours est traversé par un récit. **Léa Martens**, journaliste d’investigation freelance basée à Bruxelles (34 ans), démarre une enquête sensible pour un consortium européen de journalistes : un dossier de corruption transeuropéen impliquant un commissaire européen, une société de surveillance privée et un oligarque proche du Kremlin. Léa commence le cours avec une hygiène numérique « grand public » : Gmail, iPhone non durci, WhatsApp, mots de passe réutilisés, présence active sur LinkedIn et X. Son durcissement progresse au fil des chapitres, avec des erreurs corrigées en cours de route.

Cinq personnages secondaires apparaissent quand un chapitre se prête mieux à un autre profil : **Karim B.**, lanceur d’alerte interne dans une autorité administrative française ; **Sophie R.**, activiste climatique exposée à une surveillance administrative ; **Olivier M.**, dirigeant d’une PME tech cible d’espionnage économique ; **Yann T.**, RSSI d’une ONG des droits humains basée à Genève ; **Anya V.**, opposante politique russe en exil à Berlin.

Le fil rouge n’est pas décoratif. Il illustre les concepts au moment où ils sont abordés.

> 🟨 **Avertissement** : Léa, Karim, Sophie, Olivier, Yann, Anya, Catherine et tous les autres personnages et scénarios du cours (y compris dans les cas de synthèse finaux) sont **fictifs**, même lorsqu’ils s’inspirent de situations réalistes documentées dans la presse et les rapports d’ONG. Toute ressemblance avec des personnes réelles serait fortuite. Les cas nommément cités (Ross Ulbricht, Eldo Kim, Reality Winner, John McAfee, etc.) en Annexe 8 sont, eux, des cas réels publics et judiciairement clos, traités à des fins pédagogiques sur la base de documentation publique.

-----
