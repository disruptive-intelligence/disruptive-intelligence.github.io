---
title: Chapitre 40 — Construire une fonction de zéro à douze mois
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE VIII — Piloter et industrialiser
  - index.md
---

#### 40.1 Le diagnostic en dix jours : cinq questions

Avant tout plan, situez l'organisation. Cinq questions, et les réponses se trouvent en dix jours.

| # | Question | Ce que la réponse révèle |
|---|---|---|
| **1** | **Quelles décisions se prennent ici où il manque quelque chose ?** | L'existence ou non de besoins réels |
| **2** | **Qui prendrait ces décisions ?** | Les destinataires — sans eux, rien n'est possible |
| **3** | **Que recevons-nous déjà, et qui le lit ?** | Ce qui est couvert sans le savoir |
| **4** | **Qu'est-ce qui nous est arrivé ces dix-huit derniers mois ?** | Les angles morts réels, et la crédibilité de départ |
| **5** | **Que savons-nous de notre exposition ?** | Si l'étape 4 du chapitre 2 est possible |

**La lecture des réponses.** Si les questions 1 et 2 n'ont pas de réponse, ne souscrivez rien et ne collectez rien : construisez d'abord les besoins. Si la question 5 n'a pas de réponse, votre priorité n'est pas le CTI mais l'inventaire — sans lui, vous ne pourrez jamais vérifier l'applicabilité, donc jamais produire de renseignement.

#### 40.2 Jours 0-30 : les besoins et les destinataires

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Rencontrer chaque destinataire potentiel, avec les trois questions du §14.2 | Une liste de besoins bruts |
| **P0** | Formuler 3 à 6 besoins avec les cinq propriétés du §14.1 | Registre des besoins |
| **P0** | Inventorier ce qui est **déjà reçu** et jamais exploité | Matrice de couverture |
| **P0** | Relire les incidents des 18 derniers mois | Fiche de synthèse des angles morts |
| P1 | Identifier le référent juridique et protection des données | Contact établi |

**Ce qu'on ne fait pas ce mois-ci** : souscrire, installer un outil, produire un livrable périodique, suivre des sources.

⚠️ **L'erreur de séquencement la plus coûteuse** : commencer par les sources. Elle produit une fonction occupée qui, dix-huit mois plus tard, ne peut démontrer aucune décision modifiée.

#### 40.3 Jours 30-90 : le premier cycle mesuré

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Construire le plan de collecte, avec la colonne « déjà couvert » | Matrice besoins × sources |
| **P0** | Mettre en place la file à cinq états, avec archivage motivé | Processus |
| **P0** | Produire **un** premier produit, sur le besoin le plus actionnable | Fiche opérationnelle |
| **P0** | **Demander un retour** deux semaines après | Trois questions |
| P1 | Établir l'échelle de calibrage | Une page, validée |
| P1 | Organiser la relecture croisée | Grille en six points |

**Le premier produit doit porter sur le besoin le plus actionnable**, pas sur le plus intéressant. Dans la quasi-totalité des cas, c'est la priorisation de la remédiation : le destinataire est identifié, la décision est concrète, et le résultat est immédiatement visible.

#### 40.4 Jours 90-180 : le calibrage et les interfaces

| Prio | Action |
|---|---|
| **P0** | Appliquer l'échelle de calibrage à tous les produits |
| **P0** | Établir les interfaces avec la détection et la gestion des vulnérabilités |
| **P0** | Tenir le registre des décisions — deux lignes par produit |
| P1 | Adhérer à un dispositif sectoriel, avec le cadre juridique instruit |
| P1 | Produire la première fiche de renseignement post-incident |
| P2 | Évaluer, sans souscrire, ce qui manque réellement |

#### 40.5 Jours 180-365 : la mesure et le partage

| Prio | Action |
|---|---|
| **P0** | Premier tableau de bord, avec les trois familles d'indicateurs |
| **P0** | Premier retour d'expérience analytique — les dix dernières estimations |
| **P0** | Réviser les besoins : lesquels sont satisfaits, abandonnés, mal formulés ? |
| P1 | Premier partage sectoriel, même minimal |
| P1 | Audit d'empreinte informationnelle |
| P2 | Souscription commerciale, si et seulement si un besoin précis reste non couvert après les cinq tests |

#### 40.6 ⚠️ Les erreurs de séquencement

| Erreur | Conséquence |
|---|---|
| **Souscrire avant d'avoir des besoins** | Vous payez pour ce que vous ne lisez pas |
| **Installer une plateforme avant d'avoir du volume** | Vous maintenez un outil au lieu de produire |
| **Produire une lettre d'information** | §38.4 — l'anti-pattern, difficile à défaire ensuite |
| **Ne pas demander de retour dès le premier produit** | La boucle ne se ferme jamais |
| **Chercher la couverture avant l'utilité** | Vous suivez tout et ne servez personne |
| **Alerter tôt pour exister** | §27.6 — vous dépensez un crédit que vous n'avez pas encore |

#### 40.7 ✅ Feuille de route consolidée

**P0 — sans quoi rien ne fonctionne**

1. Trois à six besoins formulés, avec demandeur nommé et décision identifiée.
2. Un inventaire exploitable, permettant de vérifier l'applicabilité.
3. Une file à cinq états, avec **archivage motivé**.
4. Une échelle de calibrage, publiée en annexe de chaque produit.
5. Un premier produit sur le besoin le plus actionnable, avec **retour demandé**.
6. Un registre des décisions, tenu dès le premier jour.
7. Le cadre juridique de la collecte, instruit avec le référent.

**P1 — ce qui rend la fonction durable**

8. Une relecture croisée, avec la grille en six points.
9. Les interfaces avec la détection et la gestion des vulnérabilités.
10. L'exploitation du renseignement interne : incidents, tentatives bloquées, dérogations.
11. L'adhésion sectorielle, avec son cadre.
12. Le tableau de bord en six indicateurs.

**P2 — ce qui fait la différence dans la durée**

13. Le retour d'expérience analytique semestriel.
14. L'audit d'empreinte informationnelle annuel.
15. Une souscription commerciale, après les cinq tests et sur un besoin précis.
16. Un comité de priorisation, si les besoins viennent de plusieurs services.

#### 40.8 Ce qui fait un bon analyste

**Ce qui s'apprend** : les modèles, les formats, les techniques d'analyse structurée, le calibrage, l'écriture. Tout le contenu de ce cours s'apprend, et se pratique en quelques mois.

**Ce qui se pratique et ne s'enseigne pas** :

| Qualité | Comment elle se développe |
|---|---|
| **Tolérer l'incertitude** | En écrivant « nous ne savons pas » jusqu'à ce que ce soit confortable |
| **Sentir qu'un raisonnement est trop propre** | En s'étant trompé plusieurs fois de la même façon |
| **Savoir quand s'arrêter** | En ayant produit un graphe inutile (§24.8) |
| **Poser la question qui manque** | En ayant vu quelqu'un d'autre la poser |
| **Résister à la pression de conclure** | En ayant conclu trop vite une fois, et en l'ayant payé |

**Se tromper publiquement** est ce qui enseigne le plus, et le fil rouge est construit autour de cela : Nour se trompe en juillet 2029, et c'est cet épisode qui produit le calibrage, la clause de réfutation et le seuil de mobilisation. Une fonction qui ne s'est jamais trompée n'a probablement pas assez conclu.

> **Ce qui distingue un bon analyste n'est pas son taux d'exactitude. C'est l'alignement entre ce qu'il affirme et ce qu'il sait — et sa capacité à voir, avant les autres, quand cet alignement se dégrade.**

#### 40.9 La chaîne complète, en une page

🖼 **SCHÉMA — La boucle analytique complète.** *Poster récapitulatif pleine page, reprenant les six segments avec leurs chapitres. Destiné à l'impression séparée.*

```
  ┌─ ① QUESTION ───────────────────────────────────────────────┐
  │  Besoins prioritaires (14) ─► Plan de collecte (14)         │
  │  Trois niveaux (3) · Cinq objets (2) · Axiomes (4)          │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ② COLLECTE ───────────────────────────────────────────────┐
  │  Cadre juridique (20) ─► Sources ouvertes (21)              │
  │  Sources payantes (22) · Renseignement interne (23)         │
  │  Infrastructure adverse (24)                                │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ③ ANALYSE ────────────────────────────────────────────────┐
  │  Hypothèses concurrentes (6, 8) ─► Biais (7)                │
  │  Évaluation de source (10) · Acteurs (17) · Modèles (18)    │
  │  Économie de la menace (16) · Campagnes (19)                │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ④ JUGEMENT ───────────────────────────────────────────────┐
  │  Calibrer (9) ─► Produire un jugement (11) ─► Relire (12)   │
  │  Écrire (25) · Adapter (26) · Alerter (27) · Partager (28)  │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ⑤ DÉCISION ───────────────────────────────────────────────┐
  │  Cinq décisions (29) ─► Détection (30) · Vulnérabilités (31)│
  │  Réponse à incident (32) · Produit (33)                     │
  └──────────────────────────┬─────────────────────────────────┘
                             ▼
  ┌─ ⑥ RETOUR ─────────────────────────────────────────────────┐
  │  Mesurer (35) ─► Retour d'expérience analytique (35.6)      │
  │  Empreinte (34) · Économie (37) · Organisation (38)         │
  └──────────────────────────┬─────────────────────────────────┘
                             │
                    nouvelle incertitude
                             │
                             └──────────► retour en ①
```


**Les huit règles qui résument le cours**

1. Le renseignement n'a de valeur que s'il modifie une décision.
2. Le besoin précède la collecte — toujours.
3. Une meilleure collecte ne compense jamais une mauvaise analyse.
4. Les faits sont observés ; les jugements sont argumentés.
5. La confiance s'exprime, et elle est indépendante de la gravité.
6. Une analyse qui ne dit pas ce qui l'invaliderait est une opinion.
7. Personne ne peut produire votre renseignement à votre place, parce que personne d'autre ne connaît votre contexte.
8. Ignorer est la décision la plus fréquente — et elle doit être tracée.

#### 40.10 La phrase fondatrice, reprise

Le chapitre 1 s'ouvrait sur elle. Elle clôt le cours :

> ### Le CTI n'est pas là pour prédire l'avenir. Il est là pour prendre de meilleures décisions malgré l'incertitude.

**Ce que quarante chapitres ont ajouté à cette phrase** : la certitude qu'elle est atteignable. Réduire l'incertitude ne demande ni moyens exceptionnels, ni sources rares, ni outillage coûteux. Cela demande de savoir ce qu'on cherche, de raisonner avec méthode, de dire ce qu'on ignore, et d'écrire pour quelqu'un.

Le reste — les référentiels, les formats, les plateformes — est du soutien.

#### 40.11 🔴 FIL ROUGE — décembre 2031 : ce que Nour écrit

Trente-deux mois après sa prise de poste, Nour rédige un document que Claire lui a demandé : un guide interne, destiné au second analyste qui arrivera en 2032.

**Le document fait onze pages.** Voici sa première.

> **Ce que j'aurais aimé savoir en arrivant**
>
> **1. Ne souscris rien pendant trois mois.** Tout ce dont tu as besoin est déjà là, et personne ne le lit. Ta première valeur, c'est de le lire.
>
> **2. Va voir les gens avant de lire quoi que ce soit.** Pose-leur deux questions : quelles décisions te manquent, et qu'est-ce qui t'a surpris cette année. Tu auras tes besoins en une semaine.
>
> **3. Le premier rapport que tu produiras ne sera pas lu.** Ce n'est pas grave, et ce n'est pas parce qu'il est mauvais. C'est parce que tu commenceras par le contexte. Mets la conclusion en premier.
>
> **4. Tu te tromperas, et probablement dans les six premiers mois.** Écris ce qui invaliderait tes analyses **avant** de te tromper. C'est la ligne qui t'aurait sauvée, et c'est celle qu'on oublie.
>
> **5. Quand quelqu'un te demandera qui nous attaque, ne réponds pas.** Explique-lui pourquoi la question ne change rien, et donne-lui ce qui change quelque chose.
>
> **6. La plupart de ton travail consistera à archiver des choses.** Écris toujours pourquoi. C'est ce qui distingue une décision d'un oubli, et tu ne t'en rendras compte que le jour où on te posera la question.
>
> **7. Fais-toi relire par quelqu'un qui n'y connaît rien.** Il verra ce que tu ne vois plus.
>
> **8. Mesure ce que tes produits ont changé, dès le premier.** Pas ce que tu as produit. Dans deux ans, on te le demandera, et ce sera trop tard pour reconstituer.
>
> **9. Une semaine sans décision d'agir n'est pas une semaine perdue.** C'est une semaine où trente-neuf fois, quelqu'un aurait pu s'inquiéter et n'a pas eu à le faire.
>
> **10. Tu ne prédiras jamais rien.** Ce n'est pas ton métier. Ton métier, c'est de faire en sorte que les gens décident mieux sans savoir tout.

**Ce que Claire ajoute en préface**, une phrase :

> *« Nour a mis trente-deux mois à écrire cette page. Lis-la en dix minutes, et reviens la relire dans un an — tu ne la comprendras vraiment qu'à ce moment-là. »*

---

> ### 🎓 À ce stade de la Partie VIII, vous savez…
>
> - **auditer ce que votre organisation révèle d'elle-même**, et distinguer les mesures utiles du repli ;
> - **mesurer une fonction** par ses décisions modifiées et non par sa production ;
> - **conduire un retour d'expérience analytique**, et juger l'alignement entre confiance et justesse ;
> - **placer les outils à leur place** : ils accélèrent, ils ne raisonnent pas ;
> - **chiffrer une fonction**, y compris le temps des destinataires ;
> - **organiser la fonction** selon l'origine des besoins, et reconnaître l'anti-pattern de la veille documentaire ;
> - **construire un dispositif minimal viable** à trois heures par semaine, avec des renoncements écrits ;
> - **séquencer les douze premiers mois** sans commettre les six erreurs classiques.

---


## Cas de synthèse

Les trois cas se travaillent en situation, annexes ouvertes. Chacun fournit un dossier de données, pose des questions dans l'ordre où elles se présentent, et propose un corrigé argumenté avec les erreurs volontairement insérées.

---
