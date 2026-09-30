---
title: 'Chapitre 3 — Incident technique, incident majeur, crise cyber : les seuils de bascule'
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie I — Fondations : comprendre la réponse à incident'
  - index.md
---

## 3.1 Pourquoi cette distinction est critique

En pratique, la confusion entre « incident gérable par l'équipe technique » et « crise nécessitant une gouvernance exécutive » est une source majeure de dysfonctionnement. Deux erreurs symétriques menacent.

La **sous-escalade** : traiter une crise comme un incident technique ordinaire. L'équipe IT essaie de « gérer en interne » un ransomware qui a chiffré 200 serveurs, sans informer la direction, sans mobiliser le juridique, sans notifier l'ANSSI. Les conséquences : perte de temps critique, non-respect des obligations légales, décisions techniques prises sans validation stratégique, et découverte tardive de l'ampleur réelle — souvent quand l'attaquant publie les données sur son leak site et que la presse appelle.

La **sur-escalade** : déclencher la cellule de crise pour un incident mineur. Un phishing bloqué par le filtre email, un malware isolé sur un poste sans données sensibles, une tentative de brute force bloquée par le WAF. La sur-escalade crée de la panique inutile, use la crédibilité de l'équipe sécurité auprès de la direction (« ils crient au loup tout le temps »), et gaspille des ressources qui seraient mieux employées ailleurs.

La capacité à calibrer correctement l'escalade — ni trop, ni trop peu — est une compétence clé de l'IR lead. Elle repose sur des critères objectifs, pas sur l'intuition.

## 3.2 Critères de bascule en incident majeur

Un incident technique standard bascule en **incident majeur** quand au moins un des critères suivants est vérifié : compromission de l'Active Directory (contrôleur de domaine, compte krbtgt, Golden Ticket — la perte de contrôle de l'AD signifie la perte de contrôle de l'ensemble du SI Windows), chiffrement ou destruction de données à grande échelle (le ransomware a touché plus de quelques postes isolés), exfiltration de données sensibles confirmée (propriété intellectuelle, données personnelles, secrets industriels), impact sur un site OIV ou une infrastructure critique (obligations légales spécifiques), atteinte au réseau OT/ICS (risque physique potentiel), compromission du système de sauvegarde (la dernière ligne de défense est tombée), ou indisponibilité d'un service critique métier (production, facturation, logistique).

L'incident majeur déclenche une mobilisation renforcée : le prestataire PRIS est appelé si pas encore mobilisé, le RSSI prend le relais de la coordination, et un point de situation régulier est établi avec la direction technique.

## 3.3 Critères de bascule en crise cyber

Un incident majeur bascule en **crise cyber** quand l'impact dépasse la sphère technique et touche le fonctionnement de l'organisation dans ses dimensions business, réputationnelle, réglementaire ou stratégique.

Les critères de bascule incluent un impact business significatif (production arrêtée, perte de chiffre d'affaires mesurable, clients impactés), une exposition médiatique (revendication sur un leak site, article de presse, tendance sur les réseaux sociaux), un impact réglementaire (notification CNIL obligatoire, notification ANSSI en tant qu'OIV/OSE, enquête réglementaire potentielle), une demande d'extorsion (la rançon est un élément de crise par nature — elle implique des décisions stratégiques, juridiques et éthiques), une atteinte à la sécurité physique (compromission de systèmes OT/SCADA dans un environnement industriel à risque), ou un dépassement de la capacité de réponse technique (l'équipe IR est submergée, l'incident évolue plus vite que la capacité d'analyse).

## 3.4 Gouvernance technique vs gouvernance exécutive

L'activation de la crise crée deux niveaux de gouvernance qui doivent fonctionner en parallèle sans se mélanger.

La **cellule technique** est pilotée par l'IR lead. Elle comprend les analystes forensic, les analystes logs/réseau, l'analyste CTI, les administrateurs systèmes et réseaux, et le prestataire PRIS. Elle gère l'investigation technique, les actions de confinement et d'éradication, la collecte de preuves, et la production des IoC. Elle travaille en heures et en minutes.

La **cellule de crise exécutive** est pilotée par le DG ou son représentant mandaté. Elle comprend le RSSI (interface entre les deux cellules), le directeur juridique, le directeur de la communication, le DRH, le DPO, le directeur des opérations/métiers, et le DSI. Elle gère les décisions stratégiques (couper ou ne pas couper la production, payer ou ne pas payer la rançon), la communication (interne et externe), le juridique (notifications réglementaires, dépôt de plainte), et l'allocation de ressources.

Les deux cellules communiquent via des SitRep (Situation Reports) réguliers — toutes les 4 à 6 heures en phase aiguë, 1 à 2 fois par jour en phase de stabilisation. Le RSSI est la charnière entre les deux : il traduit la situation technique en termes compréhensibles par la direction, et il répercute les décisions stratégiques vers la cellule technique. Quand cette articulation fonctionne, la réponse est fluide. Quand elle dysfonctionne (le DG veut comprendre les Event IDs, l'analyste forensic conteste la décision de communication), la réponse patine.

## 3.5 Temporalités divergentes et objectifs parfois contradictoires

La cellule technique et la cellule exécutive ne travaillent pas dans le même temps, et leurs objectifs peuvent temporairement diverger.

La technique veut **comprendre avant d'agir**. L'idéal technique serait de cartographier complètement la compromission, d'identifier tous les mécanismes de persistance, et de planifier une éradication chirurgicale — ce qui peut prendre des jours. Observer l'attaquant sans l'alerter (pour comprendre l'étendue complète) est parfois plus productif que le confiner immédiatement.

Le business veut **agir avant de comprendre**. La direction veut redémarrer la production, rassurer les clients, communiquer que « tout est sous contrôle ». Chaque jour d'arrêt coûte des centaines de milliers d'euros, les clients menacent de partir, et le conseil d'administration demande des comptes.

L'arbitrage entre ces temporalités n'est pas technique — il est stratégique. Il appartient à la direction, informée par l'équipe technique. Le rôle de l'IR lead est de formuler des options claires avec leurs risques respectifs (voir Ch.26 — Décider sous incertitude), pas de prendre seul la décision.

> **Bonne pratique :** Quand les objectifs divergent, la question arbitrale est : « Quelle décision serions-nous le plus en difficulté de défendre a posteriori si elle s'avérait mauvaise ? » Redémarrer trop vite et être réinfecté est plus difficile à défendre que mettre 2 jours de plus à reprendre la production. Cette asymétrie des regrets guide la prise de décision.

## 3.6 Fil rouge — BLACKTIDE : la bascule en crise

> **🔍 BLACKTIDE — Épisode 3**
>
> Samedi 15 mars, 02h00. L'investigation initiale progresse. En 3 heures, l'équipe a établi :
> - DC01, DC02 et DC03 montrent des traces de PsExec et de modification GPO.
> - Le ransomware PhantomCrypt est en cours de déploiement via GPO — les serveurs de fichiers de 3 sites commencent à chiffrer.
> - Le trafic sortant vers le domaine C2 `update-srv-infra[.]xyz` est identifié (corrélation avec le cours Cartographie des Écosystèmes — c'est le même domaine).
> - Le volume d'exfiltration est inconnu mais des flux suspects vers AWS S3 sont repérés dans les logs proxy.
>
> Nadia évalue : ce n'est plus un incident P2. C'est un incident P1 avec probable bascule en crise. Elle appelle Marc (RSSI) à 02h15 :
>
> « Marc, on a une compromission des 3 DC, un ransomware en cours de déploiement sur les serveurs de fichiers de Fos, Lyon et Cologne, et une exfiltration probable vers un serveur externe. Le site OIV est touché. Je recommande la bascule en crise. »
>
> Marc active la cellule de crise exécutive pour 06h00 le samedi matin. Les deux gouvernances — technique et exécutive — sont désormais actives en parallèle.
>
> À 02h30, Nadia produit le premier SitRep :
>
> **SITREP #1 — BLACKTIDE — 15/03/2026 02h30**
> - **Ce qu'on sait :** 3 DC compromis, ransomware en cours de déploiement (3 sites touchés dont OIV Fos), trafic C2 identifié.
> - **Ce qu'on ne sait pas :** Étendue complète de la compromission. Volume de données exfiltrées. Identité de l'attaquant. Durée de présence dans le réseau.
> - **Ce qu'on fait :** Investigation en cours. Surveillance renforcée. Préparation des options de confinement.
> - **Ce qu'on envisage :** Confinement réseau des 3 sites impactés. Mobilisation PRIS. Notification ANSSI.
> - **Ce dont on a besoin :** Décision de confinement (impact production). Autorisation de notification ANSSI. Confirmation de la mobilisation du prestataire PRIS.

---
