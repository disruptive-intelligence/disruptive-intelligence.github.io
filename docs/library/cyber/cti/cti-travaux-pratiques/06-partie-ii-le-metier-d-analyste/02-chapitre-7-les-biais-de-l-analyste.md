---
title: Chapitre 7 — Les biais de l'analyste
source: Cyber/01_CTI/CTI_Work.md
note: CTI — travaux pratiques
up:
- - CTI — travaux pratiques
  - ../index.md
- - PARTIE II — Le métier d'analyste
  - index.md
---

## 7.1 Les biais ne sont pas un défaut de rigueur

Une mise au point préalable, parce qu'elle change complètement la façon d'aborder ce chapitre.

**Un biais n'est pas une erreur qu'on commet par manque d'attention.** C'est un mode de fonctionnement normal du raisonnement, qui produit d'excellents résultats dans la plupart des situations et des résultats faux dans un contexte précis : information incomplète, ambiguë, et pression temporelle. C'est-à-dire le contexte permanent du CTI.

**Trois conséquences pratiques :**

| Conséquence | Ce que ça implique |
|---|---|
| On ne se débarrasse pas d'un biais par la volonté | « Je vais faire attention » ne fonctionne pas. Il faut des dispositifs |
| L'expérience aggrave certains biais | Un analyste chevronné a des intuitions justes, ce qui le dispense de les tester |
| **On ne détecte pas ses propres biais** | On détecte ceux des autres. D'où la relecture croisée du chapitre 12 |

⚠️ Ce chapitre n'expose aucun mécanisme cognitif sous-jacent. Ce qui compte ici est : **comment ça se voit dans un livrable**, et **quel dispositif l'évite**. Les références académiques figurent en annexe.

## 7.2 Le biais de confirmation

**Ce que c'est** : chercher, retenir et pondérer plus fortement ce qui va dans le sens de l'hypothèse qu'on a déjà.

**Comment ça se voit dans un produit** :

> *« Plusieurs éléments confirment cette hypothèse : l'infrastructure utilisée correspond à celle décrite dans le rapport de mars, le mode opératoire est similaire, et le ciblage sectoriel est cohérent. »*

Trois éléments **compatibles**, présentés comme trois **confirmations**. Aucun n'est discriminant : ils sont tous également compatibles avec « un autre acteur utilise les mêmes techniques », hypothèse que le paragraphe n'envisage pas.

**La reformulation :**

> *« Trois éléments sont compatibles avec cette hypothèse : […]. Ils sont également compatibles avec l'hypothèse d'un acteur distinct employant des techniques largement diffusées. Aucun élément discriminant n'a été identifié à ce stade. »*

**Le dispositif qui fonctionne** : la matrice du §6.6. On ne remplit pas une colonne « éléments à l'appui », on remplit une ligne par élément et une colonne par hypothèse. La structure du tableau rend le biais visible.

## 7.3 L'ancrage

**Ce que c'est** : la première information reçue fixe le cadre, et tout ce qui suit est interprété par rapport à elle.

**Comment ça se voit** : dans la chronologie d'un dossier. La première hypothèse formulée survit à des éléments qui auraient dû la faire abandonner, parce qu'ils sont réinterprétés pour s'y loger.

> *Jour 1 : « probablement une compromission par hameçonnage »*
> *Jour 3 : découverte d'un accès par une passerelle exposée*
> *Jour 3, produit : « l'accès par la passerelle a probablement servi à consolider la compromission initiale »*

Le jour 3 aurait dû remettre en cause le jour 1. Il a été absorbé.

**Le dispositif** : dater les hypothèses et les relire. Concrètement, une ligne dans le dossier — *hypothèse formulée le [date] sur la base de [éléments]* — et une relecture explicite à chaque élément majeur : *cette hypothèse tiendrait-elle si je découvrais cet élément en premier ?*

⚠️ **L'ancrage par le titre.** Un rapport intitulé « Campagne du groupe X contre le secteur de la santé » ancre son lecteur avant la première ligne. Si vous lisez un tel document, notez votre hypothèse **avant** de l'ouvrir. Si vous en écrivez un, sachez que votre titre fait la moitié du travail de persuasion — et pesez-le.

## 7.4 La disponibilité et la saillance

**Ce que c'est** : on surestime ce qui vient facilement à l'esprit — ce dont on a récemment parlé, ce qui est spectaculaire, ce qui raconte une histoire.

**C'est le biais le plus actif en CTI**, pour une raison structurelle : le domaine est saturé de récits. Les publications décrivent des acteurs, des campagnes, des noms de code. Ce qui est raconté devient disponible ; ce qui n'est raconté par personne devient invisible — y compris quand c'est plus probable.

**Comment ça se voit** :

| Ce qui est surestimé | Ce qui est sous-estimé |
|---|---|
| Les acteurs étatiques, très documentés | La criminalité opportuniste, banale |
| Les techniques sophistiquées | Le vol d'identifiants et l'erreur de configuration |
| Ce qui a fait l'objet d'un rapport récent | Ce qui n'intéresse personne parce que trop courant |
| Une menace nommée | Une menace sans nom |

**L'exemple du mini-lab 2** en est une illustration : la démission d'un salarié — élément ④, saillant, romanesque — a plus de poids intuitif que l'appartenance d'un poste — élément ⑤, factuel, ennuyeux. Le second est pourtant décisif et le premier ne l'est pas.

**Le dispositif** : la question de la fréquence de base. *Sur cent situations de ce type, combien relèvent de l'explication que j'envisage ?* Si votre hypothèse est un acteur étatique sophistiqué et que la réponse honnête est « une ou deux sur cent », il vous faut des éléments nettement plus forts que ceux dont vous disposez.

## 7.5 La récence

**Ce que c'est** : le dernier élément reçu pèse plus lourd que les précédents, indépendamment de sa qualité.

**Comment ça se voit** : dans les révisions successives d'une évaluation. À chaque nouvelle information, la conclusion bascule — non parce que la nouvelle information est décisive, mais parce qu'elle est fraîche.

**Le dispositif** : relire l'ensemble du dossier avant chaque révision, et exiger que le changement de conclusion soit justifié par le **caractère discriminant** de l'élément nouveau, pas par son existence. Une question suffit : *si j'avais reçu cet élément il y a trois semaines, aurait-il changé quelque chose ?*

## 7.6 La pensée de groupe et le récit dominant

**Ce que c'est** : dans un collectif, la convergence prématurée vers une conclusion partagée, et la difficulté croissante à exprimer un désaccord à mesure que le consensus se forme.

**Sa forme particulière en CTI** : le **récit dominant** du domaine à un moment donné. Il existe toujours une explication en vogue — une année ce sont les acteurs étatiques, une autre les chaînes d'approvisionnement, une autre l'automatisation par des modèles de langage. Ces sujets sont réels. Le biais consiste à les voir **partout**, y compris là où une explication banale suffirait.

**Comment ça se voit** : quand tous les produits d'une organisation, sur six mois, convergent vers le même type d'explication.

**Le dispositif** : la note dissidente, traitée au §12.4. Et pour l'analyste seul, un exercice simple — *si je devais défendre l'explication la plus banale possible, que dirais-je ?*

## 7.7 Le biais du client

**Ce que c'est** : produire, sans intention consciente, le renseignement que le destinataire attend.

**C'est le biais le plus spécifique au métier**, et le moins traité dans la littérature générale sur les biais. Il ne relève pas de la complaisance : il opère en amont, dans la sélection de ce qu'on retient et dans le choix des mots.

**Ses trois manifestations** :

| Manifestation | Exemple |
|---|---|
| **Le renforcement** | Le RSSI prépare un dossier d'investissement en détection ; les produits de la période mettent en avant les menaces que la détection traiterait |
| **L'atténuation** | Une conclusion embarrassante pour un projet en cours est formulée avec plus de prudence qu'elle ne le mériterait |
| **L'anticipation** | L'analyste ne creuse pas une piste dont il pressent qu'elle dérangera |

**La troisième est la plus grave**, parce qu'elle ne laisse aucune trace : ce qui n'a pas été cherché n'apparaît nulle part.

**Le dispositif** — deux mesures :

1. **Écrire la conclusion avant de connaître l'usage qui en sera fait**, quand c'est possible.
2. **La relecture croisée par quelqu'un qui ne connaît pas le contexte politique** de la demande. C'est l'un des arguments les plus solides en faveur du chapitre 12, y compris dans une petite structure : le relecteur n'a pas besoin d'être analyste, il a besoin d'être extérieur à l'enjeu.

🎯 **ET MAINTENANT ?**
*Votre RSSI vous demande une note sur les menaces visant les accès distants, trois semaines avant un arbitrage budgétaire sur un projet d'authentification renforcée. Comment vous protégez-vous du biais du client ?*
**Réponse** : vous écrivez la note en trois sections nettement séparées — *ce que nous observons* · *ce que nous en estimons* · *ce que cela implique* — et vous rédigez les deux premières **sans lire le dossier du projet**. Puis vous ajoutez une ligne : *« évaluation produite indépendamment du dossier d'investissement en cours, dont l'analyste a eu connaissance après rédaction »*. Cette mention paraît excessive ; elle vaut beaucoup le jour où quelqu'un contestera l'indépendance de l'analyse.

## 7.8 ⚠️ Les sept biais, et où les repérer dans un produit

Grille de relecture. Elle figure en annexe C, et se lit en cinq minutes sur n'importe quel produit.

| Biais | Signe dans le texte | Question de vérification |
|---|---|---|
| **Confirmation** | « Plusieurs éléments confirment » · aucune hypothèse alternative mentionnée | Ces éléments sont-ils compatibles avec autre chose ? |
| **Ancrage** | La conclusion du dossier est celle du premier jour | Cette hypothèse tiendrait-elle si l'ordre des découvertes était inversé ? |
| **Disponibilité** | Une explication sophistiquée là où une banale suffirait | Sur cent cas semblables, combien relèvent de cette explication ? |
| **Saillance** | Le détail romanesque occupe plus de place que le détail décisif | Quel élément discrimine réellement ? |
| **Récence** | La conclusion a changé à la dernière information | Cet élément était-il discriminant, ou seulement récent ? |
| **Groupe / récit dominant** | Tous les produits du semestre concluent dans le même sens | Que dirait l'explication la plus banale ? |
| **Client** | Le produit conforte une décision en préparation | La conclusion aurait-elle été écrite ainsi sans ce contexte ? |

## 7.9 🔴 FIL ROUGE — juillet 2029 : les trois biais de Nour

Le 11 juillet, un dispositif de partage sectoriel diffuse une alerte : une campagne de rançongiciel viserait les fournisseurs de dispositifs médicaux européens. Deux victimes sont mentionnées, sans être nommées.

Nour produit en deux jours une évaluation de quatre pages. Sa conclusion :

> *« Nous estimons très probable qu'HELIOMED figure parmi les cibles de cette campagne. Un renforcement immédiat de la surveillance et un report des travaux non critiques sont recommandés. »*

Claire fait appliquer la procédure : mobilisation de l'exploitation, surveillance renforcée, deux projets décalés. Coût estimé de la semaine : environ 9 000 € en temps mobilisé.

**Ce qui se passe ensuite.** Le 24 juillet, une seconde publication du même dispositif précise que les deux victimes étaient **des distributeurs**, non des fabricants, et que le vecteur d'entrée était un progiciel de gestion commerciale qu'HELIOMED n'utilise pas. La campagne existe. Elle ne concerne pas HELIOMED.

**L'analyse a posteriori**, conduite par Nour et Claire avec la grille du §7.8. Trois biais, cumulés.

| # | Biais | Comment il a opéré |
|---|---|---|
| **1** | **Saillance** | « Fournisseurs de dispositifs médicaux » a été lu comme « nous ». Le terme correspondait à l'identité d'HELIOMED, ce qui a court-circuité la vérification de ce qu'il recouvrait exactement dans l'alerte |
| **2** | **Confirmation** | Nour a listé quatre éléments « allant dans le sens » d'un ciblage. Les quatre étaient compatibles avec une campagne opportuniste sur un progiciel. Aucun n'était discriminant |
| **3** | **Client** | C'était sa première alerte depuis son recrutement, six semaines après un épisode où son travail n'avait produit aucune décision (§3.8). Elle avait besoin que celle-ci en produise une |

**Le troisième est celui qui la marque le plus.** Il n'était ni conscient, ni malhonnête, et il est parfaitement compréhensible — ce qui ne le rend pas moins coûteux.

**Ce qui manquait dans son évaluation**, et qui aurait suffi :

| Élément absent | Ce qu'il aurait produit |
|---|---|
| Une hypothèse alternative | « Campagne opportuniste exploitant un composant commun » — celle qui était vraie |
| La question du vecteur | *Par où entrent-ils ?* — l'alerte ne le disait pas, et cela aurait dû être signalé comme une lacune majeure |
| Un niveau de confiance | « Très probable » sans confiance associée, sur une source unique et partielle |
| Ce qui l'invaliderait | Une seule ligne — *cette évaluation serait remise en cause si les victimes n'étaient pas des fabricants* — aurait déclenché la vérification |

**Ce que Claire ne fait pas.** Elle ne reproche rien, et elle le dit explicitement au comité : *l'erreur est dans le dispositif, pas dans la personne*. Aucune procédure n'exigeait alors une hypothèse alternative, un niveau de confiance ni une clause de réfutation.

**Les trois mesures.**

1. **La clause de réfutation devient obligatoire** sur toute évaluation destinée à déclencher une action — une ligne, non négociable.
2. **Le niveau de confiance devient obligatoire** sur toute affirmation d'évaluation (chapitre 9).
3. **Le seuil de déclenchement d'une mobilisation** est écrit : une source unique, non corroborée, ne déclenche pas de mobilisation — elle déclenche une **vérification**. C'est le chapitre 27.

**Ce que Nour écrit dans son carnet** :

> *J'ai eu raison sur l'existence de la campagne et tort sur tout le reste. Le pire est que si les victimes avaient été des fabricants, personne n'aurait jamais su que mon raisonnement était faux — j'aurais eu raison par accident, et j'aurais recommencé.*

**Livrable de l'épisode.** Trois lignes ajoutées au modèle de fiche opérationnelle : hypothèse alternative · niveau de confiance · ce qui invaliderait. Elles figurent en annexe D.

→ La suite en 🔴 §8.9, quand Nour appliquera pour la première fois une analyse d'hypothèses concurrentes complète.

## Synthèse mentale du chapitre 7

Un biais n'est pas un défaut de rigueur mais un mode de fonctionnement normal, efficace ailleurs et fautif ici : on ne s'en débarrasse pas par la volonté, il faut des dispositifs, et on ne détecte jamais les siens. Le biais de confirmation transforme des éléments compatibles en confirmations ; la matrice à hypothèses concurrentes le rend visible par sa structure même. L'ancrage fait survivre la première hypothèse à des éléments qui auraient dû l'abattre, et un titre ancre son lecteur avant la première ligne. La disponibilité et la saillance sont les biais les plus actifs en CTI, parce que le domaine est saturé de récits : ce qui est raconté devient disponible, ce qui n'intéresse personne devient invisible — y compris quand c'est plus probable. Le biais du client est le plus spécifique au métier et le plus difficile à corriger seul, surtout dans sa forme la plus grave : la piste qu'on ne creuse pas ne laisse aucune trace. Enfin, avoir raison par accident est plus dangereux qu'avoir tort, parce qu'on recommence.

**Trois questions de vérification**

1. « Plusieurs éléments confirment cette hypothèse. » Pourquoi cette phrase doit-elle systématiquement déclencher une vérification, et laquelle ?
2. Vous concluez à l'action d'un acteur sophistiqué. Quelle question de fréquence vous posez-vous, et que faites-vous si la réponse est défavorable ?
3. Pourquoi la forme la plus grave du biais du client est-elle celle qui ne laisse aucune trace, et quel dispositif la corrige ?

→ **Chapitre 8 — Les techniques d'analyse structurée** : les méthodes qui rendent ces dispositifs opérationnels, avec leur coût et les cas où il ne faut pas les employer.

---
