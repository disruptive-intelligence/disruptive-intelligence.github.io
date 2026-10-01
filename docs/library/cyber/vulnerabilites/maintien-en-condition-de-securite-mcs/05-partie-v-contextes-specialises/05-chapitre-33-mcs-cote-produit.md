---
title: Chapitre 33 — MCS côté produit
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE V — Contextes spécialisés
  - index.md
---

PSIRT, divulgation coordonnée et obligations réglementaires

> 🎓 **MODULE AVANCÉ — fabricants et éditeurs de produits numériques.**
> Ce chapitre ne concerne pas le maintien de votre système d'information, mais celui d'un **produit que vous mettez sur le marché** et qui s'exécute chez vos clients. Il n'est pas requis pour un parcours d'exploitation. Il est en revanche indispensable si votre organisation vend un logiciel, un équipement connecté, une application ou une appliance — et il le devient réglementairement.

## 33.1 Une différence de nature, pas de degré

| | Maintenir son SI | Maintenir un produit chez ses clients |
|---|---|---|
| Périmètre | Vos actifs | Toutes les versions déployées, chez tous les clients |
| Décision de corriger | Vous | Vous produisez le correctif, **le client décide de l'appliquer** |
| Délai | Le vôtre | Le vôtre **plus** celui d'adoption par le client |
| Visibilité | Vous voyez votre parc | Vous ne savez souvent pas qui utilise quelle version |
| Information | Vous recevez des avis | **Vous devez en publier** |
| Conséquence d'un défaut | Votre risque | Le risque de tous vos clients, simultanément |

**La conséquence structurante** : votre produit devient un composant du MCS de vos clients. Tout ce que ce cours leur enseigne à exiger de leurs fournisseurs (§13.6), ils vous le demanderont.

## 33.2 Construire un PSIRT

Un PSIRT — l'équipe qui traite la sécurité des produits — n'est pas nécessairement une équipe dédiée. Dans une organisation de taille intermédiaire, c'est un **rôle attribué** à deux ou trois personnes, avec un processus écrit.

**Les six fonctions à couvrir** :

| Fonction | Contenu |
|---|---|
| **Réception** | Point de contact unique, joignable, surveillé — y compris hors heures ouvrées |
| **Qualification** | Reproduire, évaluer l'impact, déterminer les versions affectées |
| **Coordination** | Faire corriger par les équipes de développement, arbitrer les priorités |
| **Publication** | Rédiger et diffuser l'avis de sécurité |
| **Notification** | Informer clients et autorités selon les obligations applicables |
| **Suivi** | Mesurer l'adoption du correctif chez les clients |

**Les trois décisions à prendre au démarrage**, et à écrire :

1. **Qui décide** de publier un avis, et selon quels critères ?
2. **Quel délai** vous engagez-vous à tenir entre la réception d'un signalement et la première réponse ?
3. **Qui est joignable** un samedi d'août, et comment ?

⚠️ **PIÈGE — le point de contact qui n'existe pas**
Beaucoup d'organisations découvrent, au premier signalement, qu'un chercheur a tenté de les contacter pendant trois semaines via le formulaire commercial du site, sans réponse. Le signalement finit alors publié sans coordination. **La mesure élémentaire** : une adresse de contact sécurité publiée, surveillée, avec un accusé de réception automatique et un délai de réponse annoncé.

## 33.3 La politique de divulgation coordonnée

**Le principe** : organiser la relation avec les personnes qui découvrent des vulnérabilités dans votre produit, de façon à ce que la correction précède la publication.

**Ce qu'une politique publiée doit contenir** :

| Élément | Contenu |
|---|---|
| Point de contact | Adresse dédiée, et moyen de chiffrer si nécessaire |
| Périmètre | Quels produits, quelles versions, ce qui est hors périmètre |
| Engagements | Délai d'accusé de réception, de qualification, de correction |
| Délai de publication | Le temps que vous demandez avant divulgation publique |
| Engagement de non-poursuite | Pour les recherches menées de bonne foi dans le périmètre |
| Reconnaissance | Mention du chercheur dans l'avis, si souhaité |

**Le fichier de découverte automatique** — un fichier `security.txt` normalisé par la **RFC 9116**, placé sous `/.well-known/security.txt` — est le geste le moins coûteux et le plus efficace : il permet à un chercheur de trouver comment vous joindre en dix secondes. Il comporte au minimum un champ `Contact` et un champ `Expires` [S-19].

**Sur les délais** : un délai de 90 jours entre le signalement et la publication est l'usage le plus répandu. Le chercheur peut publier au-delà, que vous ayez corrigé ou non. Négocier une prolongation est possible **si vous communiquez** — le silence est ce qui déclenche les publications anticipées.

## 33.4 Attribuer des identifiants

Deux voies : devenir vous-même autorité d'attribution pour vos produits, ou passer par un tiers.

| | Devenir autorité | Passer par un tiers |
|---|---|---|
| Maîtrise du calendrier | Totale | Dépendante |
| Charge | Processus, formation, obligations de qualité | Faible |
| Crédibilité | Signal de maturité | Neutre |
| Pertinent si | Publication régulière d'avis | Quelques avis par an |

Dans les deux cas, l'important n'est pas l'identifiant mais **l'avis** : un identifiant sans avis exploitable ne sert à rien à vos clients.

## 33.5 ⚖️ ⏱ Les obligations de signalement

*Bloc périssable, vérifié le 30/07/2026.*

Le règlement européen sur la cyberrésilience impose aux fabricants de produits comportant des éléments numériques des obligations de signalement — **article 14 du règlement** — applicables **à compter du 11 septembre 2026**, soit, à la date de vérification de ce bloc, une échéance encore à venir.

**Deux déclencheurs seulement**, et il faut les connaître précisément car ils sont plus étroits qu'on ne le croit :

1. le fabricant **a connaissance** d'une vulnérabilité de son produit **activement exploitée** ;
2. un **incident grave** affecte la sécurité du produit.

Une vulnérabilité découverte et corrigée avant toute exploitation, un correctif de routine ou une mise à jour préventive **ne relèvent pas** de l'article 14.

| Échéance | Objet | Point de départ |
|---|---|---|
| **≤ 24 h** | Alerte précoce | Prise de connaissance |
| **≤ 72 h** | Notification, avec les éléments connus et les mesures correctives ou d'atténuation disponibles | Prise de connaissance |
| **≤ 14 jours** | Rapport final, pour une **vulnérabilité activement exploitée** | **La mise à disposition d'une mesure corrective ou d'atténuation** |
| **≤ 1 mois** | Rapport final, pour un **incident grave** affectant la sécurité du produit | La notification initiale |

Le signalement s'effectue simultanément auprès de l'ENISA et du CSIRT désigné coordinateur, via la **plateforme unique de déclaration prévue à l'article 16**.

**Une obligation complémentaire souvent manquée** : l'article 14 impose également d'**informer les utilisateurs impactés** de la vulnérabilité ou de l'incident, et le cas échéant des mesures d'atténuation qu'ils peuvent déployer — de préférence dans un format structuré lisible par machine. C'est ce qui relie l'article 14 aux avis de sécurité du §33.10.

⚠️ **Ce que l'article 14 n'impose pas au 11 septembre 2026** : ni la publication d'une politique de divulgation coordonnée, ni la tenue d'un inventaire de composants, ni un processus complet de gestion des vulnérabilités. Ces exigences relèvent de l'**article 13**, applicable au 11 décembre 2027. Confondre les deux conduit à sur-dimensionner l'échéance de 2026 — ou, plus grave, à croire que l'article 14 se prépare seul.

📎 **Sources** — [S-04], [S-05], [S-06].

## 33.6 ⏱ Ce que ces délais exigent réellement en amont

C'est le point le plus important de ce chapitre, et le plus sous-estimé : **un délai de 24 heures n'est pas une obligation de formulaire, c'est une exigence de capacité organisationnelle.**

**Ce qu'il faut avoir construit avant** :

| Capacité | Sans elle |
|---|---|
| **Détecter** qu'une vulnérabilité de votre produit est activement exploitée | Vous ne déclencherez jamais le compteur, et vous serez informé par un client ou par la presse |
| **Qualifier rapidement** le périmètre affecté : quelles versions, quels clients | Vous ne pourrez pas remplir la notification |
| **Décider sans chaîne d'approbation longue** | Vingt-quatre heures ne suffisent pas pour un circuit de validation classique |
| **Rédiger vite et correctement** | Modèles préparés à l'avance |
| **Joindre les bonnes personnes** un jour férié | Astreinte, suppléance, coordonnées à jour |

✅ **BONNE PRATIQUE (P0) — l'exercice à blanc**
Réalisez au moins une fois par an un exercice : *une vulnérabilité de notre produit est signalée comme activement exploitée, un vendredi à 18 h*. Mesurez le temps réel nécessaire pour identifier les versions affectées, joindre le décideur, et produire un projet de notification. Le résultat du premier exercice est presque toujours très supérieur à 24 heures — et c'est précisément pourquoi il faut le faire avant, pas pendant.

## 33.7 ⏱ Les autres obligations structurantes

| Obligation | Contenu | Ce qu'elle implique |
|---|---|---|
| **Période de support** | Fournir des correctifs de sécurité pendant une durée déterminée après la mise sur le marché | Politique de versions (§25.7), et un modèle économique qui la finance |
| **Gestion des vulnérabilités du produit** | Processus documenté de traitement, y compris des composants tiers | Les chapitres 14 à 18, appliqués au produit |
| **Inventaire des composants** | Documenter les composants du produit | Le §25.11, automatisé à la construction |
| **Documentation et conformité** | Documentation technique, évaluation, marquage | Processus de conformité produit |
| **Application générale** | Échéance du **11 décembre 2027** pour l'essentiel des exigences | Le calendrier de mise en conformité se construit maintenant |

## 33.8 ⚖️ La méthode de qualification du périmètre

**Le principe** : certains produits sont exclus parce qu'ils relèvent d'un autre régime européen qui leur est propre — notamment les dispositifs médicaux couverts par la réglementation applicable, et plusieurs autres secteurs réglementés.

⚠️ **L'exclusion ne s'analyse jamais par gamme commerciale. Elle s'analyse produit par produit.**

**La grille de questions à instruire pour chaque objet de votre offre :**

| # | Question | Pourquoi elle compte |
|---|---|---|
| 1 | Comment le produit est-il commercialisé et **mis à disposition sur le marché** ? | Détermine l'applicabilité de principe |
| 2 | **Qui est juridiquement le fabricant** ? | Marque blanche, fabrication pour compte de tiers, sous-traitance de développement changent la réponse |
| 3 | Le **service distant** associé est-il nécessaire au fonctionnement du produit, ou constitue-t-il un service autonome ? | C'est la question la plus délicate, et celle qui décide pour les plateformes en ligne associées à un équipement |
| 4 | Ces composants forment-ils **un seul produit ou plusieurs produits distincts** ? | Un ensemble commercial peut relever de plusieurs régimes |
| 5 | Une partie relève-t-elle d'un **autre règlement qui s'applique effectivement** ? | L'exclusion suppose que l'autre régime s'applique réellement, pas qu'il pourrait s'appliquer |
| 6 | La conclusion est-elle **documentée et datée** ? | Elle est opposable, et devra être justifiée |

⚠️ **Point d'attention majeur.** Une solution en ligne n'entre pas dans le champ au seul motif qu'elle est **vendue avec** un équipement. Son rôle fonctionnel doit être analysé : un service dont dépend le fonctionnement du produit ne se traite pas comme un service autonome commercialisé séparément.

## 33.9 ⚠️ Les erreurs de qualification les plus fréquentes

| Erreur | Conséquence |
|---|---|
| Raisonner par gamme commerciale | Un produit exclu masque plusieurs produits inclus |
| **Confondre exclusion et absence d'exigences** | Le régime alternatif — notamment médical — impose ses propres exigences de cybersécurité |
| Traiter uniformément les produits **déjà mis sur le marché** | Distinction fixée par l'**article 69** : le paragraphe 2 prévoit que les produits mis sur le marché avant le 11/12/2027 ne relèvent des exigences générales qu'en cas de **modification substantielle** postérieure à cette date ; le paragraphe 3 y **déroge explicitement pour l'article 14**, dont les obligations de signalement s'appliquent à l'ensemble des produits déjà sur le marché. Un produit livré en 2020 et jamais modifié depuis doit donc disposer d'une capacité de signalement sous 24 h dès septembre 2026 [S-05] |
| Considérer la qualification comme définitive | Un changement de produit, d'usage ou de texte la remet en cause |
| Faire porter l'analyse par la seule équipe technique | C'est une analyse juridique et réglementaire, à conduire conjointement |

## 33.10 Les avis de sécurité produit

**Ce qu'un avis exploitable contient** — et c'est exactement ce que vos clients attendent pour alimenter les chapitres 14 et 16 :

| Élément | Pourquoi |
|---|---|
| Identifiant | Dédoublonnage (§4.2) |
| **Versions affectées et versions corrigées, précisément** | Sans cela, le client ne peut rien corréler (§14.6) |
| Description de la vulnérabilité et de son impact | Qualification |
| **Vecteur d'accès et conditions d'exploitation** | L'information la plus déterminante (§14.10) |
| Gravité, avec son mode de calcul | Priorisation |
| Exploitation observée, le cas échéant | Déclenche l'urgence |
| Mesures d'atténuation en attendant la mise à jour | Permet de compenser (ch. 20) |
| Date de publication et historique des révisions | Traçabilité |

**Publier un avis lisible par machine** (§4.8) démultiplie l'utilité de tout ce qui précède : vos clients peuvent l'intégrer automatiquement.

⚠️ **La cohérence entre ce que vous publiez et ce que vous corrigez** est un point de vigilance : corriger silencieusement une vulnérabilité sans publier d'avis prive vos clients de l'information dont ils ont besoin pour prioriser leur mise à jour. C'est un choix qui se retourne systématiquement contre le fournisseur au premier incident.

## 33.11 Maintenir les versions déployées chez les clients

| Sujet | Question |
|---|---|
| Matrice de support | Quelles versions recevront ce correctif ? |
| Rétroportage | Corrigez-vous les versions antérieures, et lesquelles (§25.5) ? |
| Mécanisme de mise à jour | Est-il sûr, atomique, réversible (§6.11) ? |
| Adoption | **Savez-vous combien de clients ont appliqué le correctif ?** |
| Clients refusant la mise à jour | Que faites-vous, et qu'avez-vous tracé ? |

**La question de l'adoption est celle que la plupart des éditeurs ne savent pas traiter.** Publier un correctif ne réduit le risque de personne tant qu'il n'est pas appliqué. Deux leviers : mesurer l'adoption quand le produit le permet, et **communiquer directement** aux clients concernés plutôt que de se contenter d'une publication passive.

**Le client qui refuse** relève du même raisonnement que le §32.6 : la trace écrite de votre notification, et de son refus, détermine la répartition des responsabilités le jour de l'incident.

## 33.12 📌 Limites

- **Marque blanche et fabrication pour compte de tiers** : qui publie l'avis, qui notifie ? À régler contractuellement, avant l'incident.
- **Composants intégrés fournis par des tiers** : vous dépendez de leur délai de correction, et vos clients dépendent du vôtre.
- **Sous-traitance de développement** : la responsabilité reste au fabricant, quel que soit l'auteur du code.
- **Produits anciens encore déployés** : la période de support engagée doit être tenue même si le produit n'est plus commercialisé.

## 33.13 🔴 FIL ROUGE — juin 2028 : la qualification produit par produit

Vingt et un mois après la mise en service du dispositif minimal de septembre 2026 (§8.10), HELIOMED conduit sa **revue de maturité produit**. Yann Prigent et le docteur Hélène Fabre reprennent la qualification réglementaire des quatre produits, cette fois avec un appui juridique externe et le temps de l'argumenter. Deux semaines de travail, une note de neuf pages.

**Ce que la revue confirme** : la qualification prudente de 2026 était correcte sur les trois cas tranchés. **Ce qu'elle corrige** : le statut d'HelioLink, traité par défaut comme inclus, méritait une analyse distinguant ses deux modes de commercialisation. **Ce qu'elle révèle** : le dispositif de 2026 n'aurait pas tenu un délai de 24 heures — c'est l'objet de l'exercice à blanc ci-dessous.

> ⚠️ **Les conclusions ci-dessous découlent des caractéristiques fictives décrites dans ce cas.** Elles illustrent une **méthode d'analyse**, non un résultat transposable : chaque produit réel doit faire l'objet de sa propre qualification.

**Les quatre produits, et leur traitement.**

| Produit | Description retenue dans le cas | Conclusion | Motif |
|---|---|---|---|
| **PX-40** — pompe à perfusion | Dispositif médical au sens de la réglementation applicable, marqué à ce titre | **Exclu du règlement cyberrésilience** | Le régime médical s'applique effectivement — question 5 de la grille |
| **HelioBox** — passerelle hospitalière | Équipement connecté générique, commercialisé séparément, non revendiqué comme dispositif médical | **Dans le périmètre** | Produit avec éléments numériques mis sur le marché — questions 1 et 4 |
| **HelioMove** — application mobile de bien-être | Application grand public, sans revendication médicale | **Dans le périmètre** | Logiciel mis sur le marché |
| **HelioLink** — plateforme de télésuivi | **Statut ouvert** | **À trancher** | Question 3 : le service est-il autonome, ou nécessaire au fonctionnement de HelioBox ? |

**Le cas HelioLink occupe l'essentiel de l'analyse.** La plateforme est commercialisée sous deux formes : un abonnement autonome souscrit par des établissements de santé, et une offre couplée où HelioBox ne fonctionne qu'avec elle. Selon la forme, le raisonnement diffère. La note conclut en distinguant explicitement les deux cas d'usage et retient l'hypothèse la plus contraignante pour la conception du dispositif — décision de prudence assumée et documentée.

**Ce que la qualification déclenche concrètement.**

1. **PSIRT** : le rôle minimal de 2026 est structuré — deux suppléants au lieu d'un, politique de divulgation coordonnée publiée avec un délai de 90 jours, fichier de découverte automatique conforme à la spécification en vigueur ajouté sur les sites.
2. **Capacité de notification** : modèles de notification préparés, chaîne de décision pré-autorisée — Yann peut déclencher une notification sans validation préalable de la direction générale, avec information immédiate.
3. **Exercice à blanc** : réalisé en juillet. Résultat du premier essai : **31 heures** pour produire un projet de notification exploitable, contre 24 exigées. Les deux points de blocage identifiés sont l'inventaire des versions déployées chez les clients, et la joignabilité du responsable juridique un dimanche. Corrigés en septembre ; le second exercice descend à 9 heures.
4. **Inventaire des versions déployées** : c'était le trou principal. HELIOMED ne savait pas quelle version de HelioBox tournait chez quel client. Un mécanisme de remontée de version est ajouté au produit — avec l'accord des clients, et avec une analyse d'impact sur les données personnelles conduite par Léa Cassin.
5. **Inventaire des composants** : généré automatiquement à la construction pour HelioLink et HelioBox (§25.11), conservé par version publiée.

**Le point le plus révélateur.** L'exercice à blanc montre que l'obstacle n'était ni juridique, ni technique : c'était l'**absence d'inventaire des versions déployées chez les clients**. HELIOMED savait maintenir son propre parc depuis deux ans ; elle ne savait pas ce qui tournait chez les siens.

**Ce que Yann Prigent écrit en conclusion de la note** : *nous avons appliqué à nos clients ce que nous reprochions à nos fournisseurs.*

→ La suite en 🔴 §34.12, quand la console de sauvegarde révélera son propre retard.

→ **Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes** : les outils de sécurité eux-mêmes, souvent les plus en retard.

## Synthèse mentale du chapitre 33

Maintenir un produit chez ses clients diffère en nature du maintien de son SI : vous produisez le correctif, le client décide de l'appliquer, et vous ignorez souvent quelle version tourne chez qui. Un PSIRT n'est pas nécessairement une équipe mais un rôle attribué couvrant six fonctions, dont la première — un point de contact réellement surveillé — manque à la plupart des organisations au moment du premier signalement. Les délais de notification réglementaires ne sont pas une obligation de formulaire mais une exigence de capacité organisationnelle : détecter l'exploitation, qualifier le périmètre, décider sans circuit long, et joindre les bonnes personnes un jour férié. L'exclusion du champ réglementaire s'analyse produit par produit, jamais par gamme, et exclusion ne signifie pas absence d'exigences. Enfin, publier un correctif ne réduit le risque de personne tant qu'il n'est pas appliqué : la mesure de l'adoption chez les clients est le sujet que la plupart des éditeurs ne traitent pas.

**Trois questions de vérification**

1. Une vulnérabilité de votre produit est signalée comme activement exploitée un vendredi à 18 h. Listez les cinq capacités que vous devez déjà posséder pour tenir un délai de 24 heures.
2. Votre gamme comprend un dispositif réglementé, un équipement générique et une application mobile. Pourquoi ne pouvez-vous pas conclure d'un seul examen, et quelles questions instruisez-vous pour chaque objet ?
3. Vous publiez un correctif de sécurité pour votre produit. Pourquoi le risque n'a-t-il pas encore diminué, et que faites-vous ?

---
