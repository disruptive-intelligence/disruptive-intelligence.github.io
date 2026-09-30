---
title: Chapitre 13 — L'attribution
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

> 📌 **Périmètre de ce chapitre.** Il traite l'attribution du point de vue d'une organisation qui se défend. Le renseignement étatique, les équipes d'attribution spécialisées et les enjeux judiciaires relèvent d'autres métiers, avec d'autres moyens, d'autres accès et d'autres cadres juridiques. Quand ce chapitre écrit « vous ne pouvez pas », cela signifie *une organisation ordinaire ne le peut pas* — pas *personne ne le peut*.

## 13.1 Ce que l'attribution cherche à établir

**L'attribution consiste à relier une activité observée à son auteur.** Le mot recouvre en réalité quatre questions distinctes, de difficulté croissante, et la confusion entre elles explique une grande partie des malentendus.

| Niveau | Question | Difficulté | Utile à qui |
|---|---|---|---|
| **1 — Technique** | Quelle machine, quelle infrastructure ? | Accessible | Détection, blocage |
| **2 — Opérationnelle** | Quel ensemble d'activités forme un tout cohérent ? | Accessible avec du travail | **Vous** — c'est le regroupement en campagnes |
| **3 — Organisationnelle** | Quel groupe, quelle structure ? | Difficile | Rarement vous |
| **4 — Politique** | Quel commanditaire, quel État ? | **Très difficile, souvent impossible sans moyens régaliens** | Presque jamais vous |

**Le niveau 2 est celui qui vous concerne, et il est rarement appelé « attribution ».** Regrouper des activités en un ensemble cohérent — même infrastructure, mêmes outils, même séquence — permet de raisonner, de prévoir et de détecter. Cela ne nécessite aucun nom.

**Les niveaux 3 et 4 sont ceux dont on parle**, et ce sont ceux dont vous n'avez presque jamais besoin. Le §13.5 le démontre.

## 13.2 Les méthodes, et leurs faiblesses

| Méthode | Principe | Faiblesse |
|---|---|---|
| **Infrastructure** | Réutilisation d'adresses, de domaines, d'hébergeurs | Infrastructure partagée, louée, revendue, compromise chez un tiers |
| **Outillage** | Réutilisation de code, de configurations, d'outils | **Outils partagés, vendus, volés, publiés** — c'est la faiblesse majeure |
| **Modes opératoires** | Similarité des séquences d'actions | Les techniques efficaces se diffusent ; la ressemblance est attendue |
| **Artefacts linguistiques** | Langue, fuseau horaire, encodage, fautes | Falsifiables trivialement, et souvent falsifiés |
| **Horaires d'activité** | Rythme de travail, jours chômés | Falsifiable, et brouillé par les infrastructures intermédiaires |
| **Ciblage** | Cohérence des victimes avec un intérêt supposé | Raisonnement circulaire : on attribue à qui « aurait intérêt », ce qui suppose la conclusion |
| **Renseignement d'origine humaine ou technique étatique** | — | **Hors de portée d'une organisation privée** |

**Le point commun de toutes ces méthodes** : elles établissent des **ressemblances**, jamais des identités. Une ressemblance est un indice au sens du §6.2, et l'accumulation d'indices faibles ne produit pas une preuve (§6.2, piège).

⚠️ **PIÈGE — le raisonnement par le ciblage**
« Cette attaque bénéficie à X, donc X en est l'auteur » est la faiblesse la plus séduisante de la liste, parce qu'elle produit un récit satisfaisant. Elle suppose que l'auteur soit rationnel, informé, et seul à en tirer bénéfice — trois hypothèses rarement vérifiées. Elle est aussi trivialement exploitable par un adversaire qui souhaite être attribué à un autre.

## 13.3 Les opérations sous faux drapeau et la réutilisation d'outillage

**Deux phénomènes distincts, souvent confondus.**

**La réutilisation d'outillage** est le cas ordinaire, et il n'implique aucune intention de tromper. Les outils circulent : vendus, loués, publiés après une fuite, réimplémentés. Un outil associé à un groupe dans un rapport de 2027 peut être employé en 2030 par n'importe qui. **C'est le mécanisme qui invalide le plus d'attributions**, sans qu'aucun adversaire n'ait rien fait pour cela.

**Le faux drapeau** est délibéré : l'adversaire imite les caractéristiques d'un autre pour orienter l'attribution. C'est plus rare, plus coûteux, et cela cible précisément les méthodes du §13.2 — artefacts linguistiques, réutilisation d'outils connus, horaires.

**Ce qu'il faut en retenir opérationnellement** : *l'ensemble des caractéristiques observables d'une intrusion est falsifiable par un adversaire qui en a la volonté et les moyens*. Toute attribution de niveau 3 ou 4 fondée uniquement sur des éléments techniques est donc réfutable — ce qui ne la rend pas fausse, mais interdit d'y accorder une confiance élevée.

## 13.4 ⚠️ Pourquoi un défenseur n'en a presque jamais besoin

Voici la démonstration, et c'est le cœur du chapitre.

**Le test** : prenez les mesures de défense que vous prendriez, et demandez lesquelles changent selon l'auteur.

| Mesure | Change selon l'auteur ? |
|---|---|
| Corriger la vulnérabilité exploitée | **Non** |
| Réinitialiser les identifiants compromis | **Non** |
| Rechercher les indicateurs dans les journaux | **Non** |
| Renforcer la détection sur les techniques observées | **Non** |
| Segmenter le périmètre atteint | **Non** |
| Notifier les personnes concernées | **Non** |
| Restaurer et reconstruire | **Non** |
| Alerter un partenaire exposé | **Non** |

**Aucune.** Les mesures de défense découlent de **ce qui a été fait**, pas de **qui l'a fait**. C'est le niveau 2 de l'attribution — le regroupement opérationnel — qui les informe, jamais le niveau 3 ou 4.

**La conséquence, formulée franchement** : le temps consacré à identifier un auteur est du temps qui n'est pas consacré à comprendre le mode opératoire — lequel, lui, change vos mesures.

📌 **Ce que l'attribution apporte malgré tout, indirectement** : connaître un acteur permet parfois d'**anticiper** ce qu'il fera ensuite, s'il a un comportement stable. C'est un apport réel, mais il est de nature prédictive et faible : les acteurs évoluent, se recomposent, et les rapports qui les décrivent ont dix-huit mois de retard.

## 13.5 Les rares cas où elle compte

Ils existent, et il faut les connaître pour ne pas être dogmatique.

| Cas | Pourquoi l'attribution compte | Qui la produit |
|---|---|---|
| **Assurance** | Certaines polices excluent les actes relevant d'un conflit armé ou d'un acteur étatique | L'assureur, pas vous — mais vous fournissez les éléments |
| **Contentieux** | Une action judiciaire suppose un auteur identifiable | Les autorités et les experts judiciaires |
| **Sanctions et conformité** | Verser une rançon à une entité sanctionnée expose à des poursuites | Le juridique, sur la base de listes officielles |
| **Décision politique ou diplomatique** | Hors du champ d'une organisation privée | Les États |
| **Communication de crise** | Un client ou un régulateur peut demander | **Vous — et c'est le §13.7** |

⚠️ Dans les trois premiers cas, remarquez que **ce n'est pas vous qui attribuez**. Votre rôle est de fournir des éléments factuels et de ne pas produire d'affirmation que vous ne pouvez pas soutenir. Une attribution hasardeuse figurant dans un document interne peut se retourner contre l'organisation dans une procédure.

## 13.6 Le coût d'une attribution erronée

Quatre coûts, dans l'ordre où ils se manifestent :

| Coût | Mécanisme |
|---|---|
| **Défense mal orientée** | On se prépare au comportement supposé de l'acteur nommé, pas à ce qui se passe réellement |
| **Crédibilité** | Une attribution démentie publiquement décrédibilise l'ensemble de la fonction, y compris ses analyses justes |
| **Juridique** | Une désignation d'un tiers, même interne, peut engager la responsabilité de l'organisation |
| **Diplomatique ou commercial** | Nommer un État ou une entité peut avoir des conséquences hors du champ de la sécurité |

**Le deuxième est le plus fréquent et le plus durable.** Une fonction CTI qui s'est trompée une fois sur une attribution voit ses évaluations ultérieures reçues avec réserve, y compris celles qui sont solides. Le gain d'une attribution juste est faible ; le coût d'une attribution fausse est élevé et prolongé. **L'asymétrie du pari est défavorable.**

## 13.7 Répondre à « qui nous attaque ? » sans mentir ni esquiver

La question sera posée. Par une direction, un client, un journaliste, un partenaire. Voici comment y répondre.

**Ce qui ne fonctionne pas** :

| Réponse | Pourquoi |
|---|---|
| « Nous ne faisons pas d'attribution. » | Reçu comme une dérobade, ou comme de l'incompétence |
| « C'est probablement [nom]. » | Vous engagez l'organisation sur ce que vous ne pouvez pas soutenir |
| « C'est trop complexe pour être expliqué. » | Condescendant, et faux |

**Ce qui fonctionne** — quatre temps, trente secondes :

```
1. Ce que nous savons du COMPORTEMENT
   « Nous avons identifié le vecteur d'entrée, les techniques employées
     et le périmètre atteint. »

2. Ce que cela nous permet de FAIRE
   « Cela nous a permis de fermer l'accès, de corriger la faille et de
     vérifier l'absence de persistance. »

3. Pourquoi le NOM ne change rien
   « L'identité de l'auteur ne modifierait aucune de ces mesures. »

4. Ce que nous pouvons dire, honnêtement
   « Le mode opératoire présente des similarités avec des activités
     décrites publiquement. Nous ne sommes pas en mesure d'attribuer
     avec un niveau de confiance suffisant pour l'affirmer. »
```


**Le troisième point est celui qui désamorce.** La question « qui nous attaque ? » exprime presque toujours un besoin de contrôle — comprendre pour maîtriser. Montrer que la maîtrise vient du comportement, pas du nom, y répond réellement.

🎯 **ET MAINTENANT ?**
*Un journaliste vous demande si l'attaque que vous avez subie provient d'un acteur étatique. Que répondez-vous ?*
**Réponse** : rien de plus que les quatre temps ci-dessus, et vous ne vous laissez pas entraîner sur le terrain de la spéculation — y compris quand la question est reformulée en « mais ce serait cohérent avec… ». La phrase utile : *« nous ne disposons pas d'éléments permettant d'attribuer cette activité avec un niveau de confiance qui justifierait une affirmation publique »*. Elle est vraie, elle n'est pas une esquive, et elle ne vous engage pas. Si votre organisation dispose d'une procédure de communication de crise, cette réponse y figure — écrite à froid, comme le veut le chapitre 32.

## 13.8 🔴 FIL ROUGE — février 2030 : Nour refuse de confirmer

Le 4 février, un article de presse spécialisée affirme qu'une campagne visant des fournisseurs du secteur de la santé européen est « attribuée au groupe TEMPEST-14 ». HELIOMED n'est pas citée.

Le 5 février, le directeur des systèmes d'information du centre hospitalier universitaire — celui-là même dont le courriel de mars 2029 a déclenché toute l'histoire (§1.10) — écrit à Yann Prigent :

> *« Nous lisons que le groupe TEMPEST-14 cible nos fournisseurs. Confirmez-vous que c'est bien cet acteur qui est à l'origine des incidents que vous nous avez signalés en septembre ? Notre comité de sécurité se réunit jeudi. »*

**La tentation est réelle.** Confirmer donnerait une réponse claire à un client important, avant son comité, et l'article dit ce que tout le monde pense.

**Ce que Nour vérifie**, en une demi-journée :

| Vérification | Résultat |
|---|---|
| Sur quoi l'article fonde-t-il l'attribution ? | Une publication d'éditeur du 28 janvier |
| Que dit cette publication exactement ? | *« présente des similarités avec l'outillage associé à TEMPEST-14 »* — une similarité d'outillage, avec confiance modérée |
| L'incident de septembre chez HELIOMED est-il lié ? | **Non** — il s'agissait de la compromission du prestataire (§8.9), avec un vecteur documenté et sans rapport |
| L'outillage cité a-t-il circulé ? | **Oui** — publié après une fuite en 2028, employé depuis par plusieurs acteurs distincts |

**Ce que Nour écrit à Yann**, pour transmission au client — quatre paragraphes :

> *Nous ne sommes pas en mesure de confirmer cette attribution, et nous ne pouvons pas l'infirmer.*
>
> *L'affirmation reprise par la presse provient d'une publication du 28 janvier, qui indique une similarité d'outillage avec un ensemble d'activités désigné TEMPEST-14, avec une confiance modérée. L'outillage concerné a été rendu public en 2028 et est employé depuis par plusieurs acteurs distincts ; sa présence ne permet donc pas d'identifier un auteur.*
>
> *Concernant les incidents que nous vous avons signalés en septembre 2029 : leur origine est documentée et sans rapport avec cette campagne. Il s'agissait de la compromission d'un prestataire d'infogérance, confirmée par ce dernier, avec un vecteur d'entrée identifié.*
>
> *Ce que nous pouvons affirmer : le vecteur employé en septembre est fermé, la mesure correspondante est en place et vérifiée, et nous n'avons observé aucune activité comparable depuis. Nous restons disponibles pour présenter ces éléments à votre comité.*

**La réaction du client** — et c'est ce que l'épisode enseigne. Le directeur répond le lendemain :

> *« C'est exactement ce dont j'avais besoin. Mon comité voulait un nom ; ce que je vais leur présenter est mieux : ce qui s'est passé, ce qui a été fait, et ce que vous savez ne pas savoir. »*

**Ce que Claire relève au comité de sécurité.** Refuser de confirmer aurait pu être perçu comme une faiblesse. Ce qui l'a évité, ce n'est pas le refus lui-même — c'est ce qui l'accompagnait : une explication du raisonnement, une réponse à la question sous-jacente, et une proposition d'aller plus loin.

> *« Dire "je ne sais pas" tout court, c'est une dérobade, note-t-elle. Dire "je ne sais pas, voici pourquoi, voici ce que je sais et voici ce que je peux faire", c'est du renseignement. »*

**L'épilogue, six semaines plus tard.** Le 19 mars, l'éditeur à l'origine de la publication du 28 janvier publie une mise à jour : l'attribution est retirée, la similarité d'outillage s'expliquant par la diffusion publique du code. Deux autres fournisseurs du secteur, qui avaient confirmé l'attribution à leurs clients, doivent se rétracter.

**Livrable de l'épisode.** La réponse type en quatre temps du §13.7, intégrée à la procédure de communication de crise d'HELIOMED — et validée par la direction juridique.

→ **Fin de la Partie II.** La suite en Partie III, quand il faudra transformer six questions posées en mai 2029 en un dispositif de collecte.

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> - **raisonner avec plusieurs hypothèses**, et chercher ce qui les discrimine plutôt que ce qui les confirme ;
> - **reconnaître les sept biais** dans un produit — le vôtre comme celui des autres — et savoir qu'aucun ne se corrige par la volonté seule ;
> - **structurer une analyse** avec une matrice d'hypothèses concurrentes, et **savoir quand ne pas le faire** ;
> - **calibrer** une affirmation sur trois axes indépendants, et écrire un niveau de confiance qui s'explique en une ligne ;
> - **évaluer une source**, remonter une chaîne de provenance, et détecter une circularité en quinze minutes ;
> - **produire un jugement** qui s'engage, dit ce qui l'invaliderait, et sépare l'évaluation de la recommandation ;
> - **faire relire** votre travail par un non-spécialiste avec une grille en six points ;
> - **répondre à « qui nous attaque ? »** sans mentir, sans esquiver, et sans engager votre organisation.
>
> **Ce que vous ne savez pas encore** : comment obtenir d'un décideur ce qu'il a réellement besoin de savoir, et comment organiser la collecte qui en découle. C'est l'objet de la Partie III.

---
