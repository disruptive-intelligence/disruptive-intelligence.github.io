---
title: 'Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs'
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

## 13.1 Ce qui est délégable, et ce qui ne l'est jamais

La délégation est la norme, pas l'exception : parc bureautique confié à un infogérant, applications hébergées chez un éditeur, systèmes industriels maintenus par un constructeur, infrastructure chez un fournisseur cloud. Un programme de MCS qui ne traite que ce que vous exploitez vous-même couvre souvent moins de la moitié du périmètre.

**La distinction fondatrice, à poser une fois pour toutes :**

| Délégable | Jamais délégable |
|---|---|
| L'**exécution** : appliquer les correctifs, tester, redémarrer | La **décision** d'accepter un risque |
| La **détection** : scanner, remonter les constats | La définition des **exigences** : délais, périmètre, criticité |
| La **production de preuve** : rapports, journaux | Le **contrôle** que ces exigences sont tenues |
| L'**expertise** technique sur une plateforme | La **responsabilité** vis-à-vis de vos clients et du régulateur |

**La conséquence pratique**, à énoncer clairement devant toute direction qui pense avoir transféré le sujet avec le contrat : vous pouvez déléguer le travail, vous ne pouvez pas déléguer d'en répondre. Un incident causé par un défaut de mise à jour chez votre prestataire reste votre incident vis-à-vis de vos clients, de vos utilisateurs et de l'autorité de contrôle. Le contrat organise le recours entre vous et lui ; il ne vous exonère pas devant les tiers.

## 13.2 Lire un contrat d'infogérance sous l'angle du MCS

La plupart des contrats d'infogérance sont construits autour de la **disponibilité**. C'est ce que le client demande et ce que le prestataire sait mesurer. La sécurité y figure souvent de manière générale, sans obligation vérifiable.

**Les quatre questions à poser à un contrat existant** — l'exercice prend deux heures et produit systématiquement des surprises :

| Question | Réponse fréquente | Ce qu'elle signifie |
|---|---|---|
| Quel **délai** de correction est engagé, par criticité ? | Aucun, ou « dans les meilleurs délais » | Aucune obligation opposable |
| Quel **périmètre** exact est couvert ? | Flou : « le parc bureautique » | Les exclusions apparaissent au moment du litige |
| Quelles **données** le prestataire doit-il restituer, à quelle fréquence ? | Un rapport de disponibilité mensuel | Vous ne pouvez pas mesurer votre propre conformité |
| Que se passe-t-il en cas de **manquement** ? | Rien de spécifique | L'obligation sans sanction est une intention |

🏢 **VU EN RÉUNION** — Point mensuel avec un infogérant. Le chargé de compte présente 99,94 % de disponibilité, félicitations générales. Le RSSI demande le taux d'application des correctifs. Réponse : « ce n'est pas un indicateur que nous produisons ». Ce n'était pas un refus : personne ne le lui avait jamais demandé, et le contrat ne le prévoyait pas.

⚠️ **PIÈGE — le taux de disponibilité comme indicateur de sécurité**
Un prestataire tenu à 99,9 % de disponibilité a une incitation **contraire** à l'application rapide des correctifs : chaque redémarrage consomme son budget d'indisponibilité, chaque correctif crée un risque de régression dont il porte la pénalité. Sans engagement de sécurité symétrique, le contrat pousse structurellement au report. Ce n'est pas de la mauvaise volonté, c'est le contrat qui produit ce comportement.

## 13.3 Les clauses à exiger

Voici le jeu minimal, formulé de manière directement réutilisable. Le modèle complet figure en **Annexe D**.

| # | Clause | Formulation |
|---|---|---|
| 1 | **Délais par criticité** | « Le prestataire applique les correctifs selon les délais suivants, décomptés à partir de la publication du correctif : [reprendre les classes de service du §7.2] » |
| 2 | **Périmètre nominatif** | « Le périmètre couvert est défini par la liste des actifs annexée, mise à jour trimestriellement et contradictoirement » |
| 3 | **Restitution de données** | « Le prestataire fournit mensuellement, dans un format exploitable, l'état de mise à jour de chaque actif du périmètre, **y compris la liste des actifs non joignables** » |
| 4 | **Notification de vulnérabilité** | « Le prestataire notifie sous 24 heures toute vulnérabilité activement exploitée affectant un actif du périmètre, ainsi que toute impossibilité de correction » |
| 5 | **Transparence des versions** | « Le prestataire communique sur demande les versions déployées et son propre calendrier d'obsolescence » |
| 6 | **Droit d'audit** | « Le client peut faire réaliser, à sa charge, un contrôle technique du périmètre, avec un préavis de X jours » |
| 7 | **Sous-traitance en cascade** | « Le prestataire déclare ses propres sous-traitants intervenant sur le périmètre et leur impose les mêmes obligations » |
| 8 | **Escalade des impossibilités** | « Toute impossibilité de correction est notifiée sous 5 jours ouvrés, avec sa cause et une proposition de mesure compensatoire » |
| 9 | **Réversibilité** | « En fin de contrat, le prestataire restitue l'inventaire complet, l'historique de mise à jour et la documentation d'exploitation » |
| 10 | **Sanction** | « Le non-respect des délais donne lieu à [pénalité / plan de retour à la conformité sous contrôle] » |

**Les trois clauses qui produisent le plus d'effet**, si vous ne pouvez en obtenir que trois : la **restitution de données** (3), sans laquelle vous ne pouvez rien mesurer ; l'**escalade des impossibilités** (8), qui transforme le silence en obligation ; et la **transparence sur le périmètre** (2), qui empêche le débat sur ce qui était inclus.

✅ **BONNE PRATIQUE (P0)** — La clause 3 est celle à obtenir en priorité, y compris en la négociant seule et en cours de contrat. Sans donnée restituée, votre indicateur affiche « non mesuré » (§10.11) — ce qui est honnête, mais ne réduit aucun risque. Avec la donnée, vous pouvez piloter, y compris sans les autres clauses.

## 13.4 Les référentiels de prestation d'administration et de maintenance

**Le besoin auquel ils répondent.** Un prestataire d'infogérance dispose des accès les plus privilégiés de votre système d'information : comptes d'administration, outils de déploiement, accès distants permanents. Il constitue à ce titre un actif de niveau 0 externalisé — et un chemin d'attaque de premier ordre. Plusieurs compromissions majeures documentées ont emprunté cette voie : compromettre un prestataire pour atteindre l'ensemble de ses clients.

**Ce que ces référentiels encadrent**, indépendamment du schéma considéré : la sécurisation des postes et des accès d'administration du prestataire, la gestion et la traçabilité des comptes à privilèges, le cloisonnement entre les clients, la journalisation des actions d'administration, et les compétences et l'organisation du prestataire.

⏱ **ÉTAT DE L'ART (à vérifier lors de chaque revue)** — En France, un référentiel dédié aux prestataires d'administration et de maintenance sécurisées a été élaboré par l'ANSSI. **Le statut exact du schéma de qualification et la liste des prestataires éventuellement qualifiés doivent être vérifiés directement sur le site de l'agence** : ce type de dispositif évolue, et une information périmée sur ce point peut orienter à tort un choix de prestataire. 📎 [S-15]

**Ce que vous pouvez en faire même sans qualification formelle.** Le référentiel constitue une **grille d'exigences réutilisable** dans un appel d'offres ou un questionnaire fournisseur, indépendamment de tout schéma de certification. Cinq questions en tirent l'essentiel :

1. Les postes utilisés pour administrer notre parc sont-ils dédiés à l'administration, ou servent-ils aussi à la messagerie et à la navigation ?
2. Comment sont gérés les comptes à privilèges utilisés chez nous, et sont-ils propres à notre organisation ?
3. Comment est assuré le cloisonnement entre vos clients ?
4. Les actions d'administration sont-elles journalisées, et pouvons-nous obtenir ces journaux ?
5. Quel est votre propre niveau de maintien en condition de sécurité, et comment le démontrez-vous ?

La cinquième question est celle qui met le plus souvent mal à l'aise. C'est aussi la plus légitime.

## 13.5 Maîtriser le MCS de l'administrateur externe

Le prestataire, en tant que chemin d'accès, mérite un traitement à part — au même titre que les actifs de niveau 0 du §11.7.

**Les cinq points de contrôle :**

| Point | Ce qu'il faut obtenir | Pourquoi |
|---|---|---|
| **Postes d'administration** | Postes dédiés, durcis, à jour, sans usage bureautique | Un poste d'administration qui lit des courriels est un point d'entrée direct vers vos droits les plus élevés |
| **Comptes** | Comptes nominatifs, propres à votre organisation, avec authentification forte | Un compte partagé entre plusieurs clients propage une compromission |
| **Accès distant** | Accès à la demande, borné dans le temps, journalisé | Un accès permanent est une exposition permanente |
| **Journalisation** | Journaux d'actions d'administration accessibles **de votre côté** | Sans cela, vous ne pouvez rien reconstituer après incident |
| **Retrait** | Procédure de retrait des accès au départ d'un intervenant | Les comptes d'anciens intervenants sont un classique des audits |

⚠️ **PIÈGE — l'accès permanent hérité**
Beaucoup d'organisations découvrent, lors d'un premier inventaire des accès, des comptes de prestataires dont le contrat s'est terminé il y a plusieurs années. Le mécanisme est toujours le même : personne ne détient la procédure de retrait, parce qu'elle n'a jamais été écrite. C'est un sujet du chapitre 24, et c'est aussi un sujet de décommissionnement (chapitre 35).

## 13.6 Éditeurs et fournisseurs de services

La délégation ne s'arrête pas à l'infogérance. Chaque éditeur d'application métier, chaque fournisseur de service en ligne, chaque constructeur d'équipement porte une part de votre MCS.

**Les cinq questions à poser à tout fournisseur**, en évaluation comme en revue périodique :

1. **Quelle est votre politique de publication de correctifs de sécurité ?** Fréquence, canaux, délai entre découverte et publication.
2. **Combien de versions maintenez-vous simultanément, et pendant combien de temps ?** C'est ce qui détermine si vous serez contraint à des montées de version subies.
3. **Quel préavis donnez-vous avant une fin de support ?** Six mois est court pour une application métier critique.
4. **Comment nous notifiez-vous une vulnérabilité affectant votre produit ?** Un fournisseur qui ne notifie pas vous laisse découvrir par la presse.
5. **Quels composants tiers votre produit embarque-t-il ?** C'est la question de l'inventaire de composants (§4.8), et elle deviendra réglementaire pour de nombreux produits.

⚠️ **PIÈGE — le prérequis figé**
Certains éditeurs métier conditionnent leur support à une version précise du système d'exploitation, du moteur de base de données ou de l'environnement d'exécution. Vous héritez alors de **leur** calendrier, et vous ne pouvez plus corriger sans perdre le support. C'est l'exigence n° 2 du §6.2 — et elle se négocie avant la signature, jamais après. Une fois l'application déployée et le métier dépendant, votre pouvoir de négociation est nul.

## 13.7 Ce que la réglementation change dans les deux sens

Un effet notable des évolutions réglementaires est de faire circuler les exigences le long de la chaîne d'approvisionnement, dans les deux sens.

**Vers l'amont — ce que vous devez demander.** Si vous êtes soumis à des obligations de maîtrise de votre chaîne d'approvisionnement, vous devez pouvoir démontrer que vous imposez des exigences à vos fournisseurs et que vous les contrôlez. Les clauses du §13.3 ne sont plus seulement de bonne gestion : elles deviennent un élément de preuve.

**Vers l'aval — ce qu'on va vous demander.** Symétriquement, vos clients vous adresseront les mêmes questionnaires. C'est déjà le cas, souvent avant toute obligation légale (§8.1).

✅ **BONNE PRATIQUE (P1) — le dossier fournisseur réutilisable**
Constituez **une fois** un dossier de réponse standard : votre politique MCS, vos classes de service et délais, votre couverture mesurée, votre traitement des exceptions, votre organisation de gestion des incidents. Vous répondrez à 80 % des questionnaires clients par extraction plutôt que par rédaction. C'est le même dossier de preuves que celui du §8.8 — d'où l'intérêt de le construire dans une structure unique.

## 13.8 📌 Limites : l'asymétrie de pouvoir

Tout ce chapitre suppose une capacité de négociation. Elle n'existe pas toujours, et le nier serait malhonnête.

| Situation | Ce qui est réellement possible |
|---|---|
| Fournisseur dominant, contrat d'adhésion non négociable | Aucune clause spécifique. Reste : documenter le risque accepté, exploiter ce que le fournisseur publie déjà, préparer une alternative |
| Petit client d'un grand infogérant | Peu de pouvoir individuel. Levier : le renouvellement, et le groupement avec d'autres clients |
| Éditeur métier en situation de monopole fonctionnel | Négociation faible. Levier : le contrat de maintenance annuel, et la trace écrite des demandes refusées |
| Prestataire en difficulté financière | Le rapport de force s'inverse contre vous : il faut anticiper la réversibilité |

**Ce qui reste toujours possible, quelle que soit l'asymétrie :**

1. **Écrire.** Une demande formalisée, refusée par écrit, change radicalement votre position juridique et votre position en audit.
2. **Mesurer par vous-même** ce que le prestataire ne restitue pas — un scan authentifié de votre côté, si le contrat le permet.
3. **Déclarer non couvert** ce que vous ne pouvez ni mesurer ni imposer (§7.7). C'est ce qui rend le sujet finançable.
4. **Préparer la réversibilité** : un fournisseur qu'on ne peut pas quitter est un fournisseur avec qui on ne négocie pas.

## 13.9 🔴 FIL ROUGE — novembre 2026 : la renégociation

Munie de la note établissant que 620 postes n'ont reçu aucun correctif de sécurité pendant douze mois (§12.8), Claire Nadeau conduit avec Sonia Weber la renégociation du contrat Numeria, dix mois avant son échéance.

**La position initiale du prestataire.** Le contrat de 2023 ne comporte aucun engagement de délai de correction. Le chargé de compte le rappelle : ce qui n'était pas au contrat n'était pas dû. Juridiquement, il n'a pas tort.

**Le levier qui déplace la discussion.** Claire ne conteste pas ce point. Elle expose deux faits : l'information transmise en juin sur l'éligibilité au programme de support étendu était **inexacte**, et cette inexactitude a fondé une décision de report chez HELIOMED. Le sujet cesse d'être « qui devait patcher » pour devenir « quelle information avons-nous reçue ». La négociation change de terrain.

**Ce qui est obtenu à l'avenant, et ce qui ne l'est pas.**

| Demande | Résultat |
|---|---|
| Restitution mensuelle de l'état de mise à jour, actifs non joignables inclus | **Obtenu**, format exploitable, à compter de janvier 2027 |
| Délais de correction par criticité, alignés sur les classes de service | **Obtenu partiellement** : 7 jours pour les vulnérabilités exploitées, 30 jours pour les critiques. Pas d'engagement sur le reste |
| Notification sous 24 h des vulnérabilités exploitées et des impossibilités | **Obtenu** |
| Périmètre nominatif annexé, révisé trimestriellement | **Obtenu** |
| Droit d'audit technique | **Obtenu**, avec préavis de 30 jours et à la charge d'HELIOMED |
| Pénalités financières | **Refusé.** Remplacé par un plan de retour à la conformité sous contrôle en cas de manquement constaté deux mois consécutifs |
| Déclaration des sous-traitants | **Obtenu** |

**La contrepartie.** Numeria obtient une revalorisation d'environ 6 % du contrat, justifiée par la charge de production des rapports et l'engagement de délais. Karim Lebrun valide sans difficulté : le coût annuel supplémentaire représente une fraction de ce qu'aurait coûté le support étendu sur deux ans (§12.8).

**Ce que Claire retient de la négociation**, et qu'elle formalise en règle interne : *aucun périmètre délégué n'entre en service sans clause de restitution de données*. Sans mesure, il n'y a pas de pilotage — seulement de la confiance, ce qui n'est pas une méthode.

**Livrable de l'épisode.** L'avenant contractuel, et la grille de dix clauses du §13.3 versée au référentiel achats d'HELIOMED pour tout futur contrat d'infogérance ou d'hébergement.

→ La suite en 🔴 §14.11, quand la chaîne de veille devra couvrir un périmètre devenu beaucoup plus large que le parc interne.

→ **Chapitre 14 — Veille et sources de constats** : savoir qu'un problème existe — et distinguer les quinze origines de constats.

## Synthèse mentale du chapitre 13

On délègue l'exécution, la détection et la production de preuve ; on ne délègue jamais la décision d'accepter un risque, la définition des exigences, le contrôle, ni la responsabilité devant les tiers. Un contrat construit sur la seule disponibilité pousse structurellement au report des correctifs, puisque chaque redémarrage consomme le budget d'indisponibilité du prestataire — ce n'est pas de la mauvaise volonté, c'est le contrat qui produit ce comportement. Dix clauses couvrent le sujet, dont trois sont décisives : restitution de données, escalade des impossibilités, périmètre nominatif. Le prestataire d'administration est un actif de niveau 0 externalisé : postes dédiés, comptes propres à votre organisation, accès bornés, journaux accessibles de votre côté, procédure de retrait écrite. Un prérequis de version imposé par un éditeur métier se négocie avant la signature, jamais après. Enfin, quand l'asymétrie interdit toute négociation, quatre actions restent toujours possibles : écrire, mesurer soi-même, déclarer non couvert, et préparer la réversibilité.

**Trois questions de vérification**

1. Votre infogérant tient un engagement de disponibilité de 99,9 % et n'a aucun engagement de sécurité. Expliquez pourquoi cette configuration retarde mécaniquement les correctifs, sans mettre en cause sa bonne foi.
2. Vous ne pouvez obtenir qu'une seule clause supplémentaire à votre contrat. Laquelle demandez-vous, et pourquoi celle-là plutôt que des pénalités ?
3. Un fournisseur de service en ligne refuse toute modification contractuelle. Que faites-vous concrètement, en quatre actions ?

---

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> - **rédiger** une politique MCS décidable, finançable, et qui prévoit un chemin légitime pour les cas où corriger est impossible ;
> - **construire** des classes de service avec des délais calibrés sur une capacité mesurée, dont une classe explicite pour les actifs non corrigeables ;
> - **lire** un référentiel réglementaire selon la grille exigence / objectif / moyen, et distinguer ce qui oblige de ce qui inspire ;
> - **répartir** les rôles sans faire du RSSI le propriétaire de l'exécution, et pré-arbitrer les conflits récurrents plutôt que les trancher à chaque fois ;
> - **construire** un périmètre de référence en croisant plusieurs sources, et **lire les écarts** plutôt que choisir un chiffre ;
> - **distinguer** ce qui existe de ce qui est atteignable, et reconnaître qu'une fermeture d'exposition protège aussi contre les vulnérabilités futures ;
> - **bâtir** un plan de sortie d'obsolescence financé, et exiger d'un prestataire les trois clauses qui rendent la mesure possible.
>
> **Ce que vous ne savez pas encore** : comment faire tourner la chaîne au quotidien. C'est l'objet de la Partie III.
