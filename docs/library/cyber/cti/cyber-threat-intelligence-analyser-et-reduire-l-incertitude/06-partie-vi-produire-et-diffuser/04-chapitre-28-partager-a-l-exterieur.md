---
title: Chapitre 28 — Partager à l'extérieur
source: Cyber/01 CTI & renseignement/Menace cyber/Cyber Threat Intelligence — analyser et réduire l'incertitude.md
note: Cyber Threat Intelligence — analyser et réduire l'incertitude
up:
- - Cyber Threat Intelligence — analyser et réduire l'incertitude
  - ../index.md
- - PARTIE VI — Produire et diffuser
  - index.md
---

## 28.1 Pourquoi partager, et ce qu'on y gagne réellement

**Les trois gains**, par ordre de valeur constatée :

| Gain | Mécanisme |
|---|---|
| **L'antériorité** | Savoir avant que ce ne soit public — §19.3, l'étape ③ plutôt que l'étape ⑥ |
| **Le contexte sectoriel** | Ce qui vise vos pairs vous concerne probablement |
| **La validation** | Un pair confirme ou infirme votre analyse |

**Le troisième est sous-estimé.** Un dispositif de partage est aussi un moyen de tester une hypothèse auprès de gens qui observent le même environnement — c'est l'analyse à plusieurs (§12.5) étendue hors de l'organisation.

**Ce qu'on n'y gagne pas** : une couverture exhaustive, une réactivité garantie, ou une information sur ce qui vous vise spécifiquement. Un dispositif sectoriel voit ce que ses membres partagent, ni plus ni moins.

## 28.2 Ce qui se partage et ce qui ne se partage pas

Reprise et approfondissement du §20.6.

| Catégorie | Se partage ? | Précaution |
|---|---|---|
| Indicateurs techniques anonymisés | **Oui, facilement** | Vérifier qu'ils ne révèlent pas votre architecture |
| Constats d'exploitation de vulnérabilités | **Oui** | Sans mention de vos actifs affectés |
| Modes opératoires observés | **Oui** | Sans détail permettant d'identifier la victime |
| Évaluations et analyses | Oui, avec le niveau de confiance | Ce qui protège juridiquement (§20.8) |
| Détails d'un incident propre | **Au cas par cas** | Décision de niveau direction |
| Éléments identifiant une victime tierce | **Non** | Y compris un client |
| Vos angles morts et vos lacunes | **Non** | C'est du renseignement sur vous (chapitre 34) |
| Ce qui est sous marquage restrictif reçu | **Non** | §20.5 |

⚠️ **Le point d'attention le plus fréquent** : un indicateur peut révéler votre architecture. Une adresse interne, un nom d'hôte, un format de compte, une plage horaire — ces éléments accompagnent parfois un partage sans que personne n'y prenne garde. **Relisez ce que vous transmettez comme si vous étiez le destinataire.**

## 28.3 Anonymisation et niveaux de diffusion

**Trois degrés d'anonymisation**, à choisir selon l'élément :

| Degré | Ce qui est retiré | Quand |
|---|---|---|
| **Aucun** | — | Indicateur purement externe : domaine adverse, adresse d'infrastructure |
| **Partiel** | Ce qui identifie l'actif touché, en conservant le contexte | Mode opératoire, séquence observée |
| **Complet** | Toute référence à l'organisation, y compris indirecte | Détail d'incident, statistique interne |

**Le piège de l'anonymisation partielle** : un ensemble d'éléments individuellement anonymes peut identifier l'organisation par recoupement — secteur, taille, technologie employée, date. Dans un dispositif sectoriel de vingt membres, la marge est mince.

**Le marquage de diffusion** (§20.5) accompagne systématiquement le partage, et il porte sur ce que le destinataire peut **retransmettre**, distinctement de ce qu'il peut **faire**.

## 28.4 Le fonctionnement réel d'un dispositif sectoriel

**Ce qu'on y trouve**, dans l'ordre de fréquence :

| Contenu | Fréquence | Valeur |
|---|---|---|
| Indicateurs partagés par les membres | Élevée | Variable |
| Alertes reprises de sources publiques | Élevée | **Faible** — vous les avez déjà |
| Questions posées par des membres | Moyenne | **Élevée** — c'est là que se joue l'entraide |
| Retours d'expérience d'incidents | **Faible** | **Très élevée** |
| Analyses produites par le dispositif | Variable | Élevée quand elles existent |

**La ligne des questions est celle qui surprend.** Un membre qui demande *« quelqu'un a-t-il observé ceci ? »* obtient souvent une réponse en quelques heures — et c'est le mécanisme le plus rapide et le moins coûteux de tout le dispositif. C'est aussi celui qui exige le plus de confiance mutuelle, donc celui qui se construit en dernier.

**Ce qui fait la valeur d'un dispositif** : moins la quantité partagée que **la vitesse de réponse aux questions**. Un dispositif où l'on obtient une réponse en trois heures vaut mieux qu'un dispositif qui diffuse trois cents indicateurs par semaine.

## 28.5 ⚠️ Le partage à sens unique

**Le constat** : dans tout dispositif, une minorité produit la majorité. Ce n'est pas un dysfonctionnement (§20.6) — mais il existe un seuil au-delà duquel le déséquilibre devient un problème.

| Situation | Diagnostic |
|---|---|
| Vous recevez trois fois plus que vous ne donnez | **Normal**, surtout la première année |
| Vous n'avez rien partagé depuis six mois | **À corriger** — la réciprocité est la règle implicite |
| Vous partagez uniquement ce qui ne coûte rien | Acceptable, mais limité |
| Vous ne posez jamais de question | **Vous n'exploitez pas le dispositif** |

**Les trois choses qu'une organisation peut toujours partager**, même sans capacité d'analyse :

1. **Une confirmation** : *« nous avons observé la même chose »*. Coût : cinq minutes. Valeur : élevée pour l'émetteur.
2. **Une infirmation** : *« nous avons vérifié, nous ne le voyons pas chez nous »*. Coût identique, valeur souvent supérieure — elle aide à cerner un périmètre.
3. **Une question** : elle enrichit le dispositif en signalant un sujet.

⚠️ Une organisation qui pense n'avoir rien à partager se trompe presque toujours : elle confond « produire une analyse » et « contribuer ».

## 28.6 Ce que le partage révèle de vous

**Le versant que personne n'examine**, et qui prépare le chapitre 34.

| Ce que vous partagez | Ce que cela révèle |
|---|---|
| Un indicateur | Que vous l'avez observé — donc que vous êtes visé ou touché |
| Une question précise | Ce qui vous préoccupe, donc où vous vous sentez vulnérable |
| Une analyse détaillée | Votre niveau de capacité — utile et exploitable |
| Un silence prolongé | Que vous n'observez rien, ou que vous ne pouvez rien dire |
| **Le moment où vous partagez** | Quand vous avez découvert |

**Ce qu'il faut en faire** : pas renoncer au partage — la valeur reçue dépasse largement ce risque dans un dispositif de confiance. Mais **relire ce qu'on transmet** en se demandant ce qu'un observateur attentif en déduirait.

🎯 **ET MAINTENANT ?**
*Vous subissez un incident. Un membre du dispositif sectoriel demande si quelqu'un a observé une activité correspondant à des indicateurs qu'il diffuse — ce sont les vôtres. Que faites-vous ?*
**Réponse** : vous répondez, et vous décidez du degré. Le minimum utile et sans risque : *« observé, période cohérente avec la vôtre »*. Cela confirme, aide l'émetteur, et ne révèle ni l'ampleur, ni le vecteur, ni le résultat. Si votre organisation le permet et que la confiance est établie, ajouter le vecteur d'entrée a une valeur considérable pour les autres membres — et c'est une décision de niveau direction, pas une décision d'analyste. Ce qui n'est jamais acceptable, c'est de ne pas répondre : vous savez, et le silence a un coût pour la communauté que vous exploitez par ailleurs.

## 28.7 🔴 FIL ROUGE — mars 2030 : ce qu'HELIOMED partage de son incident

L'incident de février (§23.7) a produit quatorze indicateurs, dont neuf encore valides. La question se pose au comité du 12 mars : que partage-t-on ?

**Les positions initiales**, et elles sont toutes défendables :

| Personne | Position |
|---|---|
| Nour | Partager les indicateurs et le mode opératoire — c'est utile aux membres |
| Yann Prigent | Prudence — nos clients sont membres du même dispositif |
| Le juridique | Vérifier ce que la charte engage, et ce que révèle chaque élément |
| Claire | Partager, mais décider **quoi** élément par élément |

**La décision, prise élément par élément** :

| Élément | Partagé ? | Motif |
|---|---|---|
| 9 indicateurs valides | **Oui**, sans anonymisation | Purement externes : domaines et adresses adverses |
| Le mode opératoire — 6 techniques | **Oui**, anonymisation partielle | Sans mention de l'actif touché ni du service concerné |
| Le vecteur d'entrée — pièce jointe, macro | **Oui** | Générique, aucune information sur HELIOMED |
| **L'exclusion de politique** qui a permis l'exécution | **Non** | Révèle une faiblesse de configuration propre |
| Le délai de détection — 11 jours | **Non** | Révèle une capacité |
| Le fait que la victime soit HELIOMED | **Non** | Anonymisation complète |
| Ce qui a arrêté l'adversaire | **Oui**, formulé génériquement | *« détection par alerte sur accès inhabituel à un dépôt de code »* — utile aux autres, sans révéler notre dispositif |

**La ligne la plus discutée est la dernière.** Yann Prigent objecte qu'elle révèle une capacité de détection. Nour répond que la formulation générique ne dit ni quel outil, ni quelle règle, ni quel seuil — et qu'elle est précisément l'information la plus utile aux autres membres, parce qu'elle indique **où regarder**.

Claire tranche pour le partage, avec la formulation exacte validée en séance.

**L'effet, dans les trois semaines** :

| Retour | Délai |
|---|---|
| Deux membres signalent une activité correspondant aux indicateurs | 8 et 19 jours |
| Un membre demande des précisions sur le vecteur | 4 jours |
| **Un membre signale avoir la même exclusion de politique** | 11 jours |

**Le dernier retour est celui que personne n'attendait.** Un membre, en lisant le mode opératoire, a vérifié sa propre configuration et découvert une exclusion équivalente — non partagée par HELIOMED, mais déduite du fait que la macro s'était exécutée.

**Ce que Claire en tire**, et qui nuance sa propre décision :

> *« Nous n'avons pas partagé l'exclusion. Ils l'ont déduite. C'est une information à garder en tête : ce qu'on tait n'est pas toujours invisible. »*

**Le bilan du partage à douze mois** figure au §20.8 : 34 éléments transmis, 91 exploités, quatre alertes reçues avant publication publique. Le rapport de 1 pour 2,7 est présenté sans gêne.

**Livrable de l'épisode.** La grille de décision élément par élément, et la règle : *ce qu'on partage se décide par élément, jamais par document*.

→ **Fin de la Partie VI.** La suite en Partie VII, quand il faudra transformer tout cela en décisions — et savoir quand ne rien faire.

---

> ### 🎓 À ce stade de la Partie VI, vous savez…
>
> - **placer la conclusion en tête**, et écrire une première phrase en quatre éléments ;
> - **structurer un produit** avec trois titres explicites qui disciplinent l'auteur autant qu'ils orientent le lecteur ;
> - **adapter à cinq destinataires** sans jamais altérer la conclusion — et savoir que cela coûte moins de temps que l'analyse ;
> - **dire ce que vous attendez du destinataire**, faute de quoi l'inaction est le résultat par défaut ;
> - **alerter selon quatre conditions cumulatives**, et savoir que la capacité d'alerter est un crédit qui se dépense ;
> - **clore une alerte**, et revenir dessus deux semaines plus tard ;
> - **décider ce qui se partage élément par élément**, et relire ce que vous transmettez comme si vous étiez le destinataire.
>
> **Ce que vous ne savez pas encore** : comment tout cela se transforme en décisions — y compris la décision de ne rien faire, qui est la plus fréquente. C'est l'objet de la Partie VII.

---
