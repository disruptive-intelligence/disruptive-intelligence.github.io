---
title: 'Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j'
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE III — Le cœur opérationnel
  - index.md
---

## 21.1 Ce qui distingue une crise vulnérabilité d'un incident

| | Crise vulnérabilité | Incident de sécurité |
|---|---|---|
| Point de départ | Une faille est publiée ou exploitée **ailleurs** | **Vous** êtes touché |
| Question centrale | Suis-je exposé, et depuis quand ? | Que s'est-il passé, et jusqu'où ? |
| Objectif | Réduire l'exposition avant d'être atteint | Contenir, éradiquer, reconstruire |
| Horloge | Course contre l'automatisation des attaques | Course contre la progression de l'attaquant |

**Le lien entre les deux, et il est essentiel** : une crise vulnérabilité sur un actif exposé depuis plusieurs jours **peut déjà être un incident** sans que vous le sachiez. C'est le §21.3, et c'est ce qui distingue une réaction professionnelle d'une réaction naïve.

## 21.2 L'échelle de qualification en cinq niveaux

Toutes les vulnérabilités graves ne déclenchent pas une crise. Cinq niveaux, avec une réponse propre à chacun.

| Niveau | Situation | Réponse |
|---|---|---|
| **1** | Vulnérabilité critique, aucune preuve d'exploitation | Processus normal, délai de la classe de service |
| **2** | Exploitation active observée dans le monde | Accélération : arbre de décision, feuille « urgence » (§16.3) |
| **3** | Exploitation observée **dans votre secteur** | Déclenchement de la cellule, hypothèse de ciblage |
| **4** | Indices de compromission **chez vous** | Bascule en gestion d'incident |
| **5** | **Journalisation insuffisante pour conclure** | **Traiter comme le niveau 4 jusqu'à preuve du contraire** |

Le niveau 5 est celui que les organisations traitent le plus mal, parce qu'il n'y a rien à voir — et l'absence de signal est confondue avec l'absence d'événement.

## 21.3 La règle qu'il faut enseigner explicitement

> **L'absence de preuve de compromission n'est pas la preuve de l'absence de compromission — a fortiori quand la journalisation est insuffisante.**

**Pourquoi c'est capital en pratique.** Après la publication d'un exploit sur un équipement exposé, la question n'est pas seulement « corrigeons-nous ? » mais « avons-nous déjà été atteints ? ». Corriger ferme la porte ; cela ne fait pas sortir celui qui serait entré avant. Sur les équipements de bordure en particulier, les compromissions **persistent au-delà du correctif** : implants dans le micrologiciel, comptes créés, configurations modifiées, sessions volées.

**Les trois questions à poser dès la première heure :**

1. Depuis combien de temps cet actif est-il exposé et vulnérable ?
2. De quels journaux disposons-nous sur cette période, et à quelle granularité ?
3. Ces journaux permettraient-ils de **détecter** ce type d'exploitation, ou seulement de constater une indisponibilité ?

Si la réponse à la troisième question est négative, vous êtes au niveau 5. Il faut le dire dans ces termes à la direction : *« nous ne pouvons pas établir que nous n'avons pas été compromis »*. C'est une formulation inconfortable, et c'est la seule honnête.

## 21.4 Critères de déclenchement

Écrits à l'avance, sans discussion possible au moment des faits :

```
DÉCLENCHEMENT DE LA CELLULE si TOUTES ces conditions sont réunies :
   · vulnérabilité activement exploitée (source vérifiée)
   · au moins un actif du périmètre est affecté
   · cet actif est exposé à Internet OU de niveau 0 OU critique métier

DÉCLENCHEMENT si l'une de ces conditions est réunie :
   · indices de compromission sur un actif affecté
   · impossibilité d'établir l'absence de compromission (niveau 5)
   · demande d'une autorité ou d'un client majeur
```


## 21.5 La cellule de crise vulnérabilité

**Composition minimale** : un pilote qui décide et arbitre, un responsable technique qui conduit les actions, un référent métier pour les décisions d'interruption, un référent communication, et un **greffier** dont le seul rôle est de tenir le journal.

**Le rythme** : points fixes toutes les deux heures les premières douze heures, puis toutes les quatre à six heures. Points courts — dix minutes — avec trois questions invariables : qu'a-t-on appris, que décide-t-on, qui fait quoi d'ici au prochain point.

**Le journal de décision** est le livrable central de la crise. Pour chaque entrée : horodatage, information reçue et sa source, décision prise, décideur, action engagée. Il sert pendant la crise à éviter les redites et les contradictions ; après, il constitue la preuve, la base du retour d'expérience, et l'élément qui vous protège si les décisions sont contestées.

⚠️ **PIÈGE — le greffier improvisé**
Sans rôle dédié, personne ne tient le journal : tout le monde agit. Trois jours plus tard, il est impossible de reconstituer qui a décidé quoi, quand, et sur quelle information. Le greffier est le rôle le plus facile à supprimer sous pression, et celui dont l'absence coûte le plus cher après.

## 21.6 Les six premières heures

| Heure | Action | Livrable |
|---|---|---|
| H+0 | Vérifier l'information à la source (avis éditeur, pas un article de presse) | Constat qualifié (§14.7) |
| H+0 à H+1 | **Mesurer l'exposition** : quels actifs, joignables d'où, depuis quand | Liste nominative |
| H+1 | Vérifier l'existence d'un correctif et d'un contournement officiel | Options disponibles |
| H+1 à H+2 | **Décider d'une mesure d'urgence** : fermeture d'exposition en priorité (§11.8) | Décision tracée |
| H+2 à H+4 | Engager la recherche de compromission préalable (§21.7) | Périmètre d'investigation |
| H+4 à H+6 | Informer la direction, préparer la communication | Note de situation |

**La décision la plus fréquente et la plus efficace à H+2** n'est pas d'appliquer le correctif — il n'est pas toujours disponible, testé ni déployable en deux heures. C'est de **fermer l'exposition** : couper la publication Internet, restreindre à des plages d'adresses connues, désactiver le service. Quelques minutes, réversible, et cela arrête l'horloge.

## 21.7 La recherche de compromission préalable

**L'hypothèse de travail par défaut**, pour tout équipement de bordure exposé et exploité : *considérer qu'une compromission a pu avoir lieu, jusqu'à preuve raisonnable du contraire.*

**Les cinq vérifications de premier niveau :**

| Vérification | Ce qu'on cherche |
|---|---|
| Comptes | Comptes créés, modifiés, réactivés depuis la date d'exposition |
| Configuration | Écarts par rapport à la référence (§22.3) : règles, redirections, accès |
| Persistance | Tâches planifiées, services, scripts de démarrage inconnus |
| Journaux d'accès | Connexions depuis des origines inhabituelles, horaires atypiques |
| Trafic sortant | Communications vers des destinations inhabituelles |

**Quand basculer en gestion d'incident** : dès qu'une de ces vérifications produit un résultat non explicable. La bascule est une décision du pilote de cellule, et elle change la nature des opérations — l'objectif devient la préservation des traces et la reconstruction, ce qui peut **contredire** l'urgence de correction. Ce point doit être compris à l'avance : sur un équipement compromis, appliquer le correctif peut détruire les preuves.

## 21.8 Le correctif d'urgence

**Le principe.** Contourner le processus normal sans détruire ce qui le rend fiable.

| Étape normale | En urgence |
|---|---|
| Délai d'observation | **Supprimé** — le calcul de risque s'inverse (§18.11) |
| Validation en recette | Réduite à un test fonctionnel minimal |
| Anneaux | Conservés, mais compressés : pilote de quelques heures |
| Critères d'arrêt | **Conservés intégralement** — c'est ce qui rend la compression acceptable |
| Plan de retour arrière | **Conservé intégralement** |
| Demande de changement | Émise **a posteriori**, sous 48 h, avec le journal de décision |
| Preuve | Conservée intégralement |

**Ce qu'on ne supprime jamais** : les critères d'arrêt, le retour arrière et la preuve. Ce sont les trois éléments qui permettent de se tromper sans catastrophe — précisément ce dont on a besoin quand on va vite.

## 21.9 Communication

| Destinataire | Quand | Contenu |
|---|---|---|
| Direction générale | H+4 à H+6 | Situation, exposition, décisions prises, ce qui n'est pas encore su |
| Métiers concernés | Avant toute interruption | Ce qui va être coupé, quand, pour combien de temps |
| Utilisateurs | Si effet visible | Fait, durée, contournement |
| Clients | Si leur service est affecté, ou si contractuellement prévu | Factuel, sans spéculation |
| Assureur | Selon contrat, souvent sous 48-72 h | Déclaration conservatoire |
| Autorités | Selon obligations applicables (ch. 8, ch. 33) | Délais réglementaires, à connaître **avant** |

⚠️ **PIÈGE — annoncer trop tôt une conclusion**
« Nous n'avons pas été compromis » prononcé à H+6 est presque toujours prématuré, et devient très difficile à corriger si l'investigation dit l'inverse. Formulation à privilégier : *« à ce stade, les vérifications réalisées n'ont pas mis en évidence de compromission ; l'investigation se poursuit »*.

## 21.10 Sortie de crise et retour d'expérience

**Les critères de sortie**, à énoncer explicitement : correctif appliqué et vérifié sur l'ensemble du périmètre affecté · recherche de compromission conclue · mesures d'urgence soit levées, soit converties en compensations formelles (§20.7) · communication close.

**Le retour d'expérience utile** tient en cinq questions, et il porte sur le processus, jamais sur les personnes :

1. Quel a été le **délai de détection** — entre la publication et notre prise de connaissance ?
2. Quel a été le **délai de mesure d'exposition** — et pourquoi ?
3. Quelle information nous a **manqué**, et comment l'obtenir la prochaine fois ?
4. Quelle décision a été **retardée**, et par quel manque de mandat ?
5. Que faut-il **pré-arbitrer** pour ne plus reprendre cette discussion à chaud (§9.4) ?

## 21.11 🔴 FIL ROUGE — juillet 2027 : ce que la passerelle avait vécu

Le 9 juillet 2027, un avis constructeur publie une vulnérabilité critique sur la passerelle d'accès distant d'HELIOMED. Exploitation active confirmée dans les heures qui suivent.

**H+0 — la qualification.** Malik Ferhaoui vérifie à la source. La version installée est affectée. Un correctif existe depuis six heures.

**H+1 — l'exposition.** L'interface d'administration a été fermée en septembre 2026 (§11.12). Le service d'accès distant lui-même, lui, reste nécessairement publié : c'est sa fonction. 210 collaborateurs l'utilisent quotidiennement.

**H+2 — la décision.** Fermer l'exposition signifierait couper l'accès distant de 210 personnes un mercredi matin. Claire Nadeau applique le pré-arbitrage du §9.4 : le seuil d'urgence autorise l'interruption sur décision du propriétaire technique. Elle ne coupe pas — elle **restreint** : accès limité aux plages d'adresses des sites HELIOMED et aux connexions déjà établies, le temps du correctif. Sept collaborateurs en déplacement sont impactés et prévenus individuellement.

**H+3 — la question qui change tout.** Le greffier note une remarque de Malik : *« depuis quand cette version est-elle installée ? »* Réponse : mars 2022. Et l'interface d'administration, celle qui porte la fonction vulnérable, a été publiée sur Internet de mars 2022 à septembre 2026 — **quatre ans et demi**.

La vulnérabilité publiée aujourd'hui existait dans le code depuis la version de 2021.

**H+4 — le niveau 5.** Claire pose les trois questions du §21.3. Les journaux de la passerelle sont conservés 30 jours. Il n'existe **aucune donnée** sur la période 2022-2026. La question « avons-nous été compromis pendant ces quatre ans et demi ? » n'a pas de réponse possible.

Elle informe Pierre Vasseur dans ces termes exacts : *nous ne pouvons pas établir que nous n'avons pas été compromis.* C'est la phrase la plus difficile de tout le fil rouge, et c'est la seule honnête.

**H+6 à J+3 — les opérations.** Correctif appliqué la nuit suivante, en urgence, avec critères d'arrêt et retour arrière conservés. Recherche de compromission sur les cinq axes du §21.7 : deux comptes locaux non documentés sont découverts sur la passerelle. Leur date de création n'est pas déterminable. Ils sont supprimés, et l'équipement est intégralement reconstruit à partir d'une configuration de référence plutôt que corrigé — décision prise en application du §21.7.

**J+3 à J+30.** Investigation étendue : recherche des mêmes indicateurs sur les actifs joignables depuis la passerelle, rotation complète des secrets susceptibles d'avoir transité, revue des accès distants. Aucune trace d'activité malveillante n'est établie — ce qui, comme le rappelle Claire au comité, ne prouve rien sur la période non journalisée.

**Les quatre décisions structurelles issues du retour d'expérience.**

1. **Journalisation** : conservation portée à 12 mois pour tous les actifs de bordure et de niveau 0, avec export vers un système indépendant de l'équipement.
2. **Doctrine de version** sur les équipements de bordure : au plus N-1, revue trimestrielle, avec date (§2.7).
3. **Reconstruction plutôt que correction** pour tout équipement de bordure ayant subi une exploitation potentielle.
4. **Pré-arbitrage complété** : le seuil d'urgence distingue désormais *restreindre* et *couper*, avec un décideur différent pour chacun.

**Ce que Claire écrit en conclusion du retour d'expérience**, et qui vaut pour tout le cours : *la crise de juillet 2027 n'a pas commencé le 9 juillet. Elle a commencé en mars 2022, le jour où une exposition temporaire n'a pas été refermée, et où personne n'a écrit de date de fin.*

→ Le scénario complet, avec ses données et ses décisions à prendre, constitue le **cas de synthèse A**.

→ **Chapitre 22 — Durcissement et référentiels de configuration** : la configuration, qui annule l'effet des correctifs quand elle est mauvaise.

## Synthèse mentale du chapitre 21

Une crise vulnérabilité se distingue d'un incident par son point de départ, mais l'une peut être l'autre sans que vous le sachiez : sur un actif exposé depuis plusieurs jours, la question n'est pas seulement « corrigeons-nous » mais « avons-nous déjà été atteints ». Cinq niveaux de qualification, dont le cinquième — journalisation insuffisante pour conclure — se traite comme une compromission probable. L'absence de preuve de compromission n'est pas la preuve de l'absence de compromission, et cette phrase doit pouvoir être prononcée devant une direction. La décision la plus efficace des deux premières heures n'est pas d'appliquer le correctif mais de fermer ou restreindre l'exposition : quelques minutes, réversible, et l'horloge s'arrête. En urgence, on comprime le délai d'observation et la validation, jamais les critères d'arrêt, le retour arrière et la preuve — ce sont eux qui permettent de se tromper sans catastrophe. Enfin, sur un équipement de bordure potentiellement compromis, corriger ne suffit pas : on reconstruit.

**Trois questions de vérification**

1. Un équipement exposé porte une vulnérabilité exploitée depuis trois semaines. Quelles trois questions posez-vous avant même de parler du correctif, et que faites-vous si la réponse à la troisième est négative ?
2. Quelles étapes du processus normal comprimez-vous en urgence, lesquelles conservez-vous intégralement, et pourquoi cette distinction précise ?
3. Votre direction vous demande à H+6 si vous avez été compromis. Formulez la réponse exacte que vous donnez, et expliquez pourquoi chaque mot compte.

---

---

> ### 🎓 À ce stade de la Partie III, vous savez…
>
> - **construire** une veille à partir de l'inventaire, et faire entrer tous les constats — pentest, audit, configuration, secret, obsolescence — dans une file unique ;
> - **interpréter** un rapport de scan, calculer une couverture honnête, et ne jamais confondre « non détecté », « non vulnérable » et « non scanné » ;
> - **prioriser** par arbre de décision plutôt que par seuil de gravité, et défendre une dépriorisation devant un comité ;
> - **piloter** un constat de bout en bout : parent et occurrences, deux horloges, escalade automatique, preuve par type d'issue ;
> - **conduire** une campagne : qualification en six questions, anneaux représentatifs, critères d'arrêt chiffrés, retour arrière chronométré, traîne longue qualifiée ;
> - **compenser** quand corriger est impossible, en parcourant la hiérarchie de haut en bas et en attachant les sept attributs ;
> - **conduire** une crise vulnérabilité, y compris quand la journalisation ne permet pas de conclure.
>
> **Ce que vous ne savez pas encore** : tout ce qui se dégrade en dehors des versions logicielles. C'est l'objet de la Partie IV.
