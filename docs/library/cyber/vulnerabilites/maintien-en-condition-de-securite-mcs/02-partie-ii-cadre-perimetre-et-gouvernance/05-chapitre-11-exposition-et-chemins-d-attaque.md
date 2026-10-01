---
title: Chapitre 11 — Exposition et chemins d'attaque
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE II — Cadre, périmètre et gouvernance
  - index.md
---

## 11.1 L'inventaire dit ce qui existe, l'exposition dit ce qui peut être atteint

Le chapitre 10 a produit une liste. Cette liste ne suffit pas, parce qu'elle traite comme équivalents deux actifs qui ne le sont pas du tout : un serveur portant une vulnérabilité critique mais joignable uniquement depuis un réseau d'administration restreint, et le même serveur publié sur Internet.

**La différence est d'un facteur considérable sur le risque réel, et elle n'apparaît dans aucun score de gravité** (§4.10). C'est vous, et personne d'autre, qui apportez cette information.

**Le modèle mental.** Une vulnérabilité est une porte fermée à clé. L'exposition détermine s'il y a un couloir qui mène jusqu'à cette porte, et qui peut l'emprunter. Une porte fragile au fond d'une pièce fermée n'est pas le même problème qu'une porte fragile sur la rue.

**Trois questions définissent l'exposition d'un actif :**

1. **Depuis où est-il joignable ?** Internet, réseau bureautique, réseau d'administration, réseau industriel, nulle part.
2. **Par qui ?** Anonyme, utilisateur authentifié quelconque, utilisateur privilégié, prestataire.
3. **Vers quoi mène-t-il ?** Un actif compromis donne accès à quoi d'autre — c'est la question des chemins d'attaque (§11.4).

Les deux premières questions relèvent de la surface d'exposition. La troisième change la nature de l'exercice : elle transforme une liste d'actifs en **graphe**.

## 11.2 Les familles d'approche, et ce qu'elles apportent réellement

| Approche | Point de vue | Ce qu'elle apporte | Ce qu'elle ne voit pas |
|---|---|---|---|
| **Découverte externe** | Depuis Internet, sans rien savoir de vous | Ce qui est réellement publié à votre nom, y compris ce que vous ignorez | Tout l'interne |
| **Consolidation de la vue des actifs** | Agrégation de vos propres sources | Une vue unifiée exploitable, avec les écarts (ch. 10) | Ce qu'aucune de vos sources ne connaît |
| **Analyse de chemins d'attaque** | Le point de vue de l'attaquant | Les enchaînements entre actifs, identités et droits | Ce qui n'est pas modélisé dans ses sources |
| **Test d'intrusion** | Un attaquant réel, sur un périmètre borné | La démonstration concrète, avec preuve | Le reste du périmètre, et l'instant d'après |

**Le principe fondateur de la découverte externe** mérite d'être compris, parce qu'il explique son rendement : elle part de ce que **l'extérieur** peut savoir de vous — noms de domaine, enregistrements publics, certificats émis à votre nom, blocs d'adresses, mentions publiques — et reconstruit votre surface. Elle trouve donc précisément ce que votre inventaire interne ne connaît pas : le site créé par une équipe marketing chez un hébergeur externe, l'environnement de démonstration monté pour un salon en 2023, la ressource cloud d'un projet abandonné.

⚠️ **PIÈGE — les certificats comme source de découverte**
Les certificats émis publiquement sont enregistrés dans des journaux consultables par tous. Quand vous publiez un service sous un nom, ce nom devient public — y compris pour un environnement de recette ou d'administration que vous pensiez discret. Ce n'est pas une faille, c'est le fonctionnement normal du dispositif, et c'est une des premières sources qu'utilise un attaquant. Nommer un service `admin-preprod.exemple.fr` n'a donc rien de discret.

## 11.3 L'exposition Internet : ce qu'il faut chercher en premier

Par ordre de gravité constatée, voici ce qui se trouve réellement lors d'un premier exercice de découverte externe.

| Découverte | Pourquoi c'est grave | Fréquence constatée |
|---|---|---|
| **Interface d'administration publiée** | Conçue pour un réseau de confiance, souvent sans authentification forte | Très fréquente |
| **Service oublié** | Plus de propriétaire, donc plus de correctifs depuis des années | Très fréquente |
| Environnement de recette exposé | Données parfois réelles, durcissement moindre (ch. 28) | Fréquente |
| Stockage cloud ouvert | Fuite de données sans aucune intrusion | Fréquente |
| Accès distant secondaire | Mis en place en urgence, jamais retiré | Fréquente |
| Équipement réseau avec interface publiée | Cible de premier choix, très recherchée | Moins fréquente, très grave |

**La première tâche d'un programme de MCS**, avant même de corriger quoi que ce soit, consiste à établir cette liste. Elle est courte, elle se constitue en quelques jours, et elle produit presque toujours des fermetures immédiates — c'est-à-dire une réduction de risque sans correctif, sans fenêtre et sans négociation.

🖼 **SCHÉMA — Chemin d'attaque type en six étapes.** *Graphe orienté du poste bureautique jusqu'à la console de sauvegarde, chaque arête annotée par ce qui la rend praticable (mot de passe local partagé, session privilégiée, joignabilité réseau).*

## 11.4 Chemins d'attaque : de la liste au graphe

Une vulnérabilité isolée est rarement l'histoire complète. Une compromission réelle est un **enchaînement** : entrée par un actif exposé, récupération d'identifiants, déplacement vers un actif de plus grande valeur, élévation de privilèges, atteinte de l'objectif.

**Les trois dimensions à croiser** — et c'est le croisement qui fait l'information :

| Dimension | Question |
|---|---|
| **Réseau** | Depuis cet actif, qu'est-ce qui est joignable ? |
| **Identité** | Quels comptes existent ou peuvent être obtenus sur cet actif, et où sont-ils valables ailleurs ? |
| **Vulnérabilité** | Que permet techniquement chaque étape ? |

**L'exemple canonique**, qu'on retrouve dans une grande partie des compromissions documentées :

```
Poste bureautique compromis (hameçonnage — aucune vulnérabilité exploitée)
    → un compte d'administration local partage son mot de passe avec 400 autres postes
    → déplacement vers un serveur de fichiers
    → un compte de service à privilèges élevés y a laissé une session ouverte
    → récupération de ce compte
    → accès à la console de sauvegarde
    → accès à l'ensemble des données, y compris les sauvegardes
```


**Ce que cet exemple enseigne au MCS.** Aucune des étapes ne dépend d'une vulnérabilité au sens du chapitre 4, sauf éventuellement la première. Ce qui rend le chemin praticable, ce sont des **choix de configuration et d'identité** : mot de passe local partagé, compte de service surprivilégié, console de sauvegarde joignable depuis le réseau bureautique. C'est précisément le périmètre des chapitres 22 et 24 — et la démonstration que réduire le MCS aux correctifs laisse ce chemin entièrement ouvert.

## 11.5 Combinaisons toxiques

Une **combinaison toxique** est un ensemble d'éléments individuellement acceptables dont la conjonction crée un risque majeur.

| Élément 1 | Élément 2 | Élément 3 | Résultat |
|---|---|---|---|
| Vulnérabilité de gravité moyenne | Actif joignable depuis Internet | Compte à privilèges élevés présent sur l'actif | Compromission du domaine |
| Machine hors support | Aucune segmentation | Copie de données de production | Fuite de données par un actif « secondaire » |
| Compte de service | Mot de passe inchangé depuis 2019 | Droits d'administration sur 200 machines | Propagation immédiate |
| Recette exposée | Mêmes identifiants qu'en production | Journalisation absente | Compromission indétectable |

**Le point qui rend ces combinaisons dangereuses en pratique** : chaque élément pris isolément passe sous les seuils. La vulnérabilité moyenne n'est pas prioritaire, l'exposition seule paraît acceptable, le compte à privilèges est justifié par un besoin d'exploitation. Aucun outil raisonnant constat par constat ne les remontera. Il faut **croiser**, et le croisement est un travail d'analyse, pas d'outillage.

✅ **BONNE PRATIQUE (P1)** — Faites une revue trimestrielle des combinaisons, sur une liste courte et fixe de règles écrites : *actif exposé + compte à privilèges*, *hors support + non segmenté*, *recette + données de production*, *compte de service + droits étendus + mot de passe ancien*. Quatre requêtes sur votre inventaire enrichi suffisent, et elles trouvent ce qu'aucun scanner ne remonte.

## 11.6 Atteignabilité

de la présence du composant à l'exécution du code vulnérable

Une nuance qui divise le volume de travail par un facteur important, et qui devient centrale au chapitre 25.

Un outil détecte la **présence** d'un composant vulnérable. Il ne détecte pas si le **code vulnérable est réellement atteignable** dans le contexte d'exécution. Trois niveaux :

| Niveau | Question | Effet sur la priorité |
|---|---|---|
| Présent | Le composant est installé | Signal faible |
| Chargé | Le composant est effectivement utilisé par l'application | Signal moyen |
| **Atteignable** | La fonction vulnérable peut être appelée par une entrée contrôlable par un attaquant | **Signal fort** |

**Deux applications concrètes :**

- Une bibliothèque vulnérable dont la fonction fautive n'est jamais appelée par l'application ne constitue pas un risque exploitable. Le fournisseur peut le déclarer formellement — c'est l'objet des déclarations d'exploitabilité du §4.8.
- Un service vulnérable installé mais **désactivé** n'est pas exposé. Vérifier l'état d'activation avant de traiter un constat évite une part significative du travail — et c'est une vérification de trente secondes.

📌 **LIMITES** — L'analyse d'atteignabilité est coûteuse et imparfaite : elle dépend de la qualité de l'analyse du code, elle traite mal les appels dynamiques, et elle peut donner une fausse assurance. Utilisez-la pour **déprioriser de façon documentée**, jamais pour clore définitivement un constat. La distinction entre déprioriser et clore est traitée au chapitre 17.

## 11.7 Actifs d'entrée et actifs de niveau 0

Deux catégories méritent un traitement distinct de tout le reste du parc.

**Les actifs d'entrée** — tout ce par quoi un attaquant peut arriver : passerelles d'accès distant, portails publiés, serveurs de messagerie, postes de travail, interfaces d'échange avec des partenaires. Leur particularité : ils sont exposés **par conception**, on ne peut pas fermer leur exposition sans supprimer leur fonction. Le seul levier disponible est donc la **vitesse de correction**. Ce sont eux qui justifient la classe C1 du §7.2.

**Les actifs de niveau 0** — ceux dont la compromission donne le contrôle d'un ensemble d'autres actifs : annuaire, autorité de certification, plan de gestion de virtualisation, console de sauvegarde, outil de déploiement de correctifs, coffre-fort de secrets, chaîne de construction logicielle, outillage d'administration.

⚠️ **PIÈGE — le paradoxe du niveau 0**
Ces actifs sont statistiquement parmi les plus en retard du parc, pour trois raisons convergentes : leur mise à jour « n'apporte rien aux métiers », elle interrompt l'outil que les administrateurs utilisent quotidiennement, et ils sont souvent considérés comme protégés parce qu'ils ne sont pas exposés à Internet. Or leur compromission ne nécessite pas d'exposition externe : elle se produit par un chemin interne (§11.4). **Le fait de ne pas être exposé à Internet ne rend pas un actif secondaire.**

✅ **BONNE PRATIQUE (P0)** — Établissez la liste nominative de vos actifs de niveau 0. Elle tient sur une page. Placez-les tous en classe C1, avec fenêtre récurrente et propriétaire nommé. C'est la mesure de MCS ayant le meilleur rapport effort/réduction de risque de tout ce cours.

## 11.8 Fermer l'exposition plutôt que corriger

Voici l'un des enseignements les plus rentables de ce cours, et l'un des moins appliqués.

Face à une vulnérabilité sur un actif exposé, deux actions sont possibles : corriger, ou **retirer l'exposition**. Comparons-les honnêtement.

| Critère | Corriger | Fermer l'exposition |
|---|---|---|
| Délai | Heures à semaines | **Minutes à heures** |
| Risque de régression | Réel | Faible, et immédiatement réversible |
| Fenêtre nécessaire | Souvent | Rarement |
| Effet sur les **futures** vulnérabilités du même actif | Aucun | **Protège aussi contre celles à venir** |
| Effet métier | Nul si tout va bien | Peut supprimer un usage légitime |

La quatrième ligne est décisive et rarement formulée : fermer une exposition inutile protège contre toutes les vulnérabilités futures du service concerné, y compris celles qui ne sont pas encore découvertes. C'est la seule action de ce cours qui produise un effet durable sans effort récurrent.

**Les questions à poser systématiquement** devant un actif exposé :

1. Cette exposition est-elle **nécessaire** aujourd'hui, ou héritée d'un besoin passé ?
2. Peut-elle être **restreinte** — à des plages d'adresses connues, derrière une authentification, via un accès distant maîtrisé ?
3. L'interface d'administration a-t-elle besoin d'être publiée, ou seulement le service métier ?

En pratique, une part significative des expositions constatées lors d'un premier inventaire externe ne correspond plus à aucun besoin actif. Les fermer coûte une demi-journée et retire du périmètre à surveiller des actifs entiers.

## 11.9 Suivre l'exposition dans le temps

L'exposition n'est pas un état, c'est un flux : chaque projet en crée, chaque urgence en ajoute, chaque décommissionnement incomplet en laisse.

**Les trois indicateurs utiles**, définis rigoureusement au chapitre 38 :

- **nombre d'actifs exposés à Internet**, avec son évolution — la tendance importe plus que la valeur absolue ;
- **délai moyen entre l'apparition d'une exposition et sa détection** — mesure la réactivité de votre découverte externe ;
- **nombre de réapparitions** — une exposition fermée qui revient signale un problème de processus, pas de configuration : quelqu'un la recrée, et il faut comprendre pourquoi.

⚠️ **PIÈGE — l'exposition temporaire**
« On ouvre pour la migration, on referme après. » La règle qui fonctionne : **toute ouverture temporaire porte une date de fermeture dans la demande de changement**, et un contrôle automatique vérifie la fermeture à cette date. Sans cela, la statistique est constante : une part importante de ces ouvertures reste en place des années.

## 11.10 📌 Ce que chaque approche ne voit pas

| Approche | Angle mort |
|---|---|
| Inventaire interne | Ce que vous ne savez pas posséder — ressources hébergées ailleurs, environnements montés hors processus |
| Scanner de vulnérabilités | La joignabilité réelle depuis l'extérieur ; il scanne depuis là où il est placé |
| Découverte externe | L'interne ; et elle peut attribuer à tort un actif qui ne vous appartient pas |
| Analyse de chemins d'attaque | Ce qui n'est pas dans ses sources : systèmes industriels, environnements séparés, applications propriétaires |
| Test d'intrusion | Tout ce qui n'était pas dans le périmètre, et tout ce qui a changé depuis |

**La conséquence méthodologique** : ces approches ne se substituent pas, elles se croisent. Un actif remonté par la découverte externe et absent de l'inventaire interne est le constat le plus riche que produise ce chapitre — il signale à la fois une exposition et un trou d'inventaire.

## 11.11 ✅ Livrable — Carte des actifs exposés et matrice des chemins critiques

**Partie 1 — Carte des actifs exposés.** Une ligne par actif joignable depuis l'extérieur.

| Actif | Service publié | Depuis quand | Propriétaire | Nécessité confirmée | Restriction possible | Classe | Décision |
|---|---|---|---|---|---|---|---|

**Partie 2 — Matrice des chemins critiques.** Une ligne par enchaînement plausible, limité aux chemins menant à un actif de niveau 0.

| Point d'entrée | Étape intermédiaire | Cible finale | Élément qui rend le chemin praticable | Rupture la moins coûteuse | Prio |
|---|---|---|---|---|---|

**La colonne décisive est l'avant-dernière.** Pour chaque chemin, on ne cherche pas à tout corriger : on cherche **le maillon le moins cher à rompre**. Souvent, ce n'est pas un correctif — c'est une règle de filtrage, un mot de passe local unique par machine, un compte de service dont on retire des droits, ou une console qu'on retire du réseau bureautique.

**Priorisation recommandée** : **P0** pour tout chemin menant à un actif de niveau 0 en trois étapes ou moins ; **P1** au-delà de trois étapes ; **P2** pour les chemins nécessitant un accès physique ou un privilège initial élevé.

## 11.12 🔴 FIL ROUGE — septembre 2026 : l'interface publiée depuis 2022

Claire Nadeau fait réaliser un premier exercice de découverte externe sur les noms de domaine d'HELIOMED. Trois jours de travail, résultat en une page.

**Ce qui est trouvé.**

| Découverte | Origine | Décision |
|---|---|---|
| Interface d'administration de la passerelle d'accès distant, publiée sur Internet | Ouverture réalisée en mars 2022 pendant une période de télétravail massif, jamais refermée | **Fermeture immédiate**, restriction à deux plages d'adresses |
| Environnement de démonstration d'HelioLink, monté pour un salon en 2023 | Hébergé chez un fournisseur externe, facturé sur la carte du service commercial | Contient une copie de données de test réalistes. Extinction sous 15 jours |
| Deux sous-domaines pointant vers des ressources cloud désallouées | Reliquat d'un projet abandonné | Suppression des enregistrements de noms |
| Trois noms d'environnements internes découverts via les journaux de certificats publics | Nommage explicite : recette, administration, sauvegarde | Aucune exposition réelle, mais information offerte à un attaquant. Politique de nommage revue |

**Le chemin d'attaque qui change la priorisation.** L'interface d'administration de la passerelle porte la vulnérabilité de gravité 5,9 identifiée en février (§4.11) — celle que la méthode initiale, fondée sur la gravité, avait écartée. En croisant avec l'exposition, le constat change de nature : vulnérabilité **présente au catalogue d'exploitation avérée**, sur une interface **d'administration**, **publiée sur Internet**, sur un actif d'**entrée**. Trois des quatre critères de la classe C1 sont réunis.

La fermeture de l'exposition est réalisée le jour même, en quarante minutes, sans fenêtre et sans risque de régression pour les utilisateurs — l'accès métier n'était pas concerné. La correction, elle, est planifiée sous 72 heures.

**Ce que Claire présente au comité.** Non pas « nous avons corrigé une vulnérabilité », mais : *nous avons retiré du périmètre exposé quatre actifs, dont un portait une vulnérabilité activement exploitée, et cette fermeture nous protège également des vulnérabilités futures de ces mêmes services*. La distinction n'est pas rhétorique — c'est celle du §11.8, et c'est ce qui débloque le budget de l'exercice de découverte externe récurrent.

**Livrable de l'épisode.** La carte des actifs exposés, la première matrice de chemins d'attaque d'HELIOMED, et une règle de nommage interdisant les noms explicites sur les enregistrements publics.

**Ce qui se joue sans que personne le sache encore.** La passerelle a été exposée pendant quatre ans et demi. La question de savoir si quelqu'un en a profité pendant cette période n'est pas posée en septembre. Elle le sera brutalement au chapitre 21, et elle constitue le point de départ du cas de synthèse A.

→ La suite en 🔴 §12.8, quand il faudra financer la sortie d'obsolescence de ce que cet inventaire a révélé.

→ **Chapitre 12 — Cycle de vie, obsolescence et dette technique** : l'obsolescence, seule menace dont la date est annoncée à l'avance.

## Synthèse mentale du chapitre 11

L'inventaire dit ce qui existe, l'exposition dit ce qui peut être atteint — et cette information n'est produite par aucun score, elle vient de vous seul. Trois questions la définissent : depuis où, par qui, et vers quoi cet actif mène-t-il. La troisième transforme la liste en graphe, car une compromission réelle est un enchaînement dont la plupart des étapes ne reposent sur aucune vulnérabilité mais sur des choix de configuration et d'identité. Les combinaisons toxiques échappent à tout outil raisonnant constat par constat : quatre règles écrites et une revue trimestrielle les trouvent. Les actifs de niveau 0 sont statistiquement les plus en retard, précisément parce qu'on les croit protégés par leur absence d'exposition externe. Enfin, fermer une exposition inutile est la seule action qui protège aussi contre les vulnérabilités futures du service : elle coûte des minutes, ne nécessite pas de fenêtre, et une part significative des expositions constatées ne correspond plus à aucun besoin actif.

**Trois questions de vérification**

1. Deux serveurs portent la même vulnérabilité critique ; l'un est publié sur Internet, l'autre joignable uniquement depuis un réseau d'administration. Le score de gravité est identique. Qu'est-ce qui doit différencier votre traitement, et d'où vient cette information ?
2. Reconstruisez un chemin d'attaque en quatre étapes qui ne repose sur aucune vulnérabilité logicielle. Quel est le maillon le moins coûteux à rompre ?
3. Votre équipe demande l'ouverture temporaire d'un accès pour une migration de trois semaines. Quelle condition posez-vous, et pourquoi la formuler au moment de la demande plutôt qu'après ?

---
