---
title: Chapitre 2 — Cadre juridique et recevabilité de la preuve
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 2.1 La preuve numérique en droit français

La preuve numérique est admissible en droit français, tant en matière pénale (Code de procédure pénale) qu'en matière civile et commerciale (Code civil, Code de commerce). Mais son admissibilité est conditionnée par trois principes fondamentaux qui guident toute la méthodologie forensic.

La **loyauté** signifie que la preuve doit avoir été obtenue par des moyens légaux et éthiques. Une preuve obtenue par piratage, par intrusion non autorisée dans un système tiers, ou en violation du droit du travail est irrecevable, quel que soit son contenu. En matière pénale, la jurisprudence est stricte : les preuves obtenues de manière déloyale par les forces de l'ordre sont annulées (principe posé par la chambre criminelle de la Cour de cassation). En matière civile, la jurisprudence a évolué : l'assemblée plénière de la Cour de cassation a admis en 2023 que des preuves obtenues de manière déloyale pouvaient être recevables si leur production était indispensable à l'exercice du droit à la preuve et proportionnée aux intérêts en jeu. Mais cette ouverture ne dispense pas de la rigueur.

L'**intégrité** garantit que la preuve n'a pas été altérée entre le moment de la collecte et le moment de la présentation. C'est le fondement de la chaîne de custody et du hashing : prouver qu'un fichier analysé est identique au fichier collecté, bit pour bit. Sans preuve d'intégrité, la partie adverse peut contester que la preuve a été modifiée — intentionnellement ou accidentellement.

Le **contradictoire** impose que la partie adverse puisse examiner, contester et faire contre-expertiser la preuve. C'est pourquoi la documentation méthodologique est aussi importante que l'analyse elle-même : il faut pouvoir expliquer exactement comment on a procédé, avec quels outils (nom, version, paramètres), et pourquoi, pour qu'un expert adverse puisse reproduire ou contester les résultats. Un rapport forensic techniquement brillant mais méthodologiquement opaque sera attaqué au contradictoire.

## 2.2 Code de procédure pénale : perquisitions numériques

Les perquisitions numériques obéissent aux règles générales de la perquisition (autorisation judiciaire, présence de témoins, procès-verbal) adaptées au numérique. Les enquêteurs peuvent saisir les équipements informatiques ou, plus couramment dans la pratique actuelle, réaliser des copies forensic sur place (moins perturbant pour l'activité de l'entreprise). Les réquisitions (articles 60-1 et 77-1-1 du CPP) permettent d'obtenir des données auprès des fournisseurs de services (opérateurs télécom, hébergeurs, éditeurs SaaS, fournisseurs cloud) sans saisie physique. Les scellés numériques garantissent l'intégrité des supports saisis : le hash calculé au moment de la saisie est l'équivalent numérique du scellé physique apposé sur un sac de preuves.

L'accès aux données chiffrées est un enjeu croissant. L'article 434-15-2 du Code pénal punit le refus de remettre une convention de chiffrement (clé ou mot de passe) demandée par l'autorité judiciaire, mais en pratique, si le suspect ne coopère pas et que la clé n'est pas récupérable par ailleurs, les données restent inaccessibles. D'où l'importance du dump mémoire à chaud (la clé de chiffrement BitLocker ou FileVault est en mémoire tant que le volume est déverrouillé).

## 2.3 L'expert judiciaire

L'expert judiciaire en informatique est un technicien inscrit sur la liste d'une cour d'appel, mandaté par un magistrat (juge d'instruction, juge civil, ou tribunal de commerce) pour réaliser une expertise technique. Son statut est régi par la loi du 29 juin 1971 et le décret du 23 décembre 2004.

L'expert reçoit une mission précise définie par le magistrat (par exemple : « déterminer si des données ont été exfiltrées du SI de la société X entre le 1er janvier et le 31 mars 2026, identifier les moyens utilisés, et chiffrer le préjudice »). Il est tenu par cette mission et ne peut pas la dépasser sans autorisation. Il doit respecter le contradictoire : les parties sont informées des opérations d'expertise, peuvent y assister (ou se faire représenter par un conseil technique, souvent appelé « sapiteur »), et peuvent soumettre des « dires » (observations écrites auxquelles l'expert doit répondre dans son rapport). Le rapport d'expertise est soumis au juge, qui reste libre de le suivre ou non (l'expertise est un avis technique, pas un jugement).

L'inscription sur la liste des experts exige une compétence technique reconnue et une formation à la procédure judiciaire. L'expert prête serment. Sa responsabilité professionnelle est engagée en cas de faute. Dans le contexte forensic, l'expert doit maîtriser à la fois la technique (acquisition, analyse, outils) et la procédure (chaîne de custody, documentation, rédaction pour le contradictoire).

## 2.4 Chaîne de custody

La chaîne de custody (chain of custody) retrace le parcours complet d'une pièce à conviction numérique, de sa collecte à sa présentation. Elle répond à une question simple : qui a eu accès à cette preuve, quand, et qu'en a-t-il fait ?

Chaque manipulation est documentée : qui a acquis le support (nom, qualité, organisme), à quelle date et heure (horodatage précis, fuseau horaire explicite), avec quel outil (nom, version, paramètres), quel est le hash d'intégrité (MD5 + SHA-256 calculés immédiatement après l'acquisition), où le support est-il stocké (lieu physique, conditions de sécurité), qui l'a transporté (nom, date, moyen de transport), et qui l'a analysé (nom, dates, outils utilisés).

Une rupture dans la chaîne de custody — un moment où la preuve n'était pas sous contrôle documenté — permet à la partie adverse de contester son intégrité. C'est la différence entre une preuve et un simple fichier. Le formulaire de chaîne de custody est en Annexe E.

> **Bonne pratique :** Même en investigation interne (sans perspective judiciaire immédiate), respecter les principes de la chaîne de custody dès le départ. La raison est pragmatique : de nombreuses investigations internes basculent en judiciaire quand l'ampleur des faits est révélée. Si les preuves ont été collectées sans rigueur au début, elles sont inexploitables devant un tribunal — et l'entreprise a perdu sa chance de judiciariser.

## 2.5 Recevabilité de la preuve numérique

Pour qu'une preuve numérique soit acceptée par un tribunal, plusieurs conditions cumulatives doivent être remplies : **authenticité** (la preuve est bien ce qu'elle prétend être — hash d'intégrité vérifié), **fiabilité** (la méthode de collecte et d'analyse est reconnue et reproductible — outils documentés, méthodologie explicite), **pertinence** (la preuve est en rapport avec les faits litigieux — hors sujet = irrecevable), **proportionnalité** (la collecte n'a pas été disproportionnée par rapport à l'enjeu — imager le disque du DG pour un conflit sur l'utilisation de la photocopieuse serait disproportionné), et **loyauté** (obtenue par des moyens légaux — ce critère a été assoupli en matière civile par la jurisprudence de 2023, mais reste strict en matière pénale).

Un rapport forensic parfaitement rédigé mais fondé sur une acquisition non documentée sera contesté. Un rapport fondé sur une acquisition impeccable mais dont les conclusions dépassent les constatations sera également contesté. La rigueur doit être de bout en bout.

## 2.6 Forensic judiciaire vs investigation interne : deux régimes

L'investigation interne (menée par l'entreprise elle-même ou un prestataire mandaté) et l'investigation judiciaire (menée sous mandat d'un magistrat) obéissent à des règles différentes. L'investigation interne n'a pas de pouvoir de réquisition (elle ne peut pas forcer un hébergeur AWS à communiquer les logs CloudTrail), elle est contrainte par le RGPD et le droit du travail (voir 2.7 et 2.8), mais elle bénéficie d'une flexibilité méthodologique plus grande (pas de scellés formels, pas de contradictoire obligatoire). L'investigation judiciaire dispose de pouvoirs étendus (perquisition, réquisition, scellés, mandat international) mais est soumise à un cadre procédural strict dont la violation entraîne la nullité des actes.

Le moment de la bascule est critique : quand les premiers résultats de l'investigation interne révèlent une infraction pénale (accès frauduleux — art. 323-1 CP, vol de données, abus de confiance, extorsion), l'entreprise doit décider si elle judiciarise (dépôt de plainte). À ce moment, les preuves collectées en interne doivent être exploitables judiciairement — d'où l'importance de la rigueur dès le début.

## 2.7 RGPD et forensic

Le RGPD s'applique dès que l'investigation traite des données à caractère personnel — ce qui est presque toujours le cas (un dump de disque contient les fichiers personnels de l'utilisateur, un log contient des identifiants, un dump mémoire peut contenir des mots de passe en clair). La base légale la plus courante pour l'investigation forensic est l'intérêt légitime de l'entreprise à assurer la sécurité de son SI (article 6.1.f du RGPD). La proportionnalité est essentielle : ne collecter que ce qui est nécessaire à l'investigation, ne conserver les données que le temps de l'investigation et de l'éventuelle procédure, et documenter la justification. Le DPO doit être impliqué dès le début de l'investigation.

## 2.8 Droit du travail et forensic interne

L'investigation forensic sur le poste d'un salarié est encadrée par le droit du travail et la jurisprudence de la chambre sociale de la Cour de cassation. Les grands principes : l'employeur peut accéder aux fichiers professionnels du salarié (présomption de caractère professionnel des fichiers sur le poste de travail de l'entreprise), mais les fichiers explicitement marqués « personnel » ou « privé » ne peuvent être ouverts qu'en présence du salarié ou après information (sauf si un événement particulier le justifie — menace sur la sécurité du SI). La charte informatique de l'entreprise (si elle existe, a été communiquée, et est à jour) encadre l'utilisation des outils et les modalités de contrôle. En pratique, impliquer le juridique et le DPO avant toute investigation sur un poste de salarié est indispensable — une preuve obtenue en violation du droit du travail est irrecevable dans une procédure disciplinaire.

## 2.9 Normes internationales

Trois normes ISO encadrent les pratiques forensic. **ISO 27037** (2012) couvre l'identification, la collecte, l'acquisition et la préservation des preuves numériques — c'est la norme de référence pour la phase d'acquisition (comment manipuler un support, quand utiliser un write blocker, comment documenter). **ISO 27042** (2015) couvre l'analyse et l'interprétation des preuves — elle formalise les principes d'analyse objective et de documentation des résultats. **ISO 27043** (2015) définit le processus global d'investigation — de l'identification au rapport. Ces normes ne sont pas obligatoires mais constituent un cadre de bonnes pratiques reconnu internationalement. S'y conformer renforce la crédibilité de l'investigation et la recevabilité des preuves, tant en France qu'à l'international.

## 2.10 Fil rouge — MUSIC BOX : le cadrage juridique

> **🔬 MUSIC BOX — Épisode 2**
>
> Vendredi soir, 18h30. Claire appelle le directeur juridique de NovaPharma, Maître Antoine Renard, et le DPO, Sandrine Leclerc.
>
> Questions immédiates : peut-on investiguer le poste de Julien Mallet ? Réponse : oui, c'est une investigation de sécurité sur un poste professionnel, pas une surveillance du salarié. La charte informatique autorise les contrôles de sécurité. Le DPO valide la base légale (intérêt légitime). Faut-il déposer plainte maintenant ? Pas encore — il faut d'abord comprendre l'étendue. Mais on préserve les preuves comme si on allait judiciariser.
>
> Le directeur juridique recommande de mandater une experte judiciaire inscrite pour sécuriser la chaîne de custody dès le début. Maître Élise Fournier (experte judiciaire en informatique, cour d'appel de Paris) est contactée — elle sera sur site samedi 9h. Son rôle : superviser les acquisitions, garantir la chaîne de custody, et être en mesure de témoigner de la rigueur méthodologique si l'affaire est judiciarisée.

---
