---
title: Chapitre 10 — Exercices et entraînement
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie II — Préparation : avant que l''incident n''arrive'
  - index.md
---

## 10.1 Types d'exercices

Les **exercices tabletop** sont des simulations sur papier : un scénario est présenté (« il est 22h, le SOC détecte une alerte EDR sur un DC, que faites-vous ? »), les participants discutent leurs décisions, les processus sont testés sans manipulation technique. Efficace pour tester l'IRP, la chaîne d'escalade, la communication, et la coordination entre équipes. Peu coûteux, rapide à organiser (2 à 4 heures), et adapté à la sensibilisation de la direction.

Les **exercices techniques** sont des simulations en environnement de lab ou en production contrôlée : un malware est déployé (avec l'accord de la direction), un mouvement latéral est simulé, les analystes doivent détecter, investiguer, et confiner. Efficace pour tester les compétences techniques, l'outillage, et les playbooks. Plus coûteux (nécessite un environnement de test et un red team ou purple team), mais irremplaçable pour valider la capacité opérationnelle réelle.

Les **exercices de crise complets** impliquent la direction, la communication, le juridique, et les métiers — en plus de l'équipe technique. Le scénario inclut des éléments de pression réalistes : appel d'un journaliste (simulé), publication sur un faux leak site, pression des « clients » (acteurs de l'exercice). Efficace pour tester la gouvernance, la communication de crise, et la prise de décision stratégique. Lourd à organiser (une journée complète, préparation de plusieurs semaines), mais le seul moyen de tester la chaîne complète de la détection au RETEX.

## 10.2 Fréquence et progression

Fréquence minimale recommandée : exercice tabletop trimestriel, exercice technique semestriel, exercice de crise complet annuel. Chaque exercice est suivi d'un retex structuré avec plan d'amélioration. La progression va du simple au complexe : d'abord un seul type d'incident avec l'équipe technique seule, puis des scénarios multi-vecteurs avec des parties prenantes multiples.

## 10.3 Le test le plus simple et le plus révélateur

Appeler les numéros de la chaîne d'escalade un dimanche matin à 7h pour vérifier que quelqu'un répond, que la personne connaît son rôle, et qu'elle sait qui mobiliser ensuite. Résultat habituel : 30 à 50 % d'échec au premier essai (numéro qui ne répond pas, personne qui ne sait pas qu'elle est d'astreinte, personne qui ne connaît pas la procédure). Ce test coûte 30 minutes et révèle plus de failles que n'importe quel audit de 3 semaines.

## 10.4 Fil rouge — BLACKTIDE : les exercices manqués

> **🔍 BLACKTIDE — Épisode 10**
>
> Arvantis avait prévu un exercice de crise cyber depuis 2 ans. Il a été reporté 4 fois (« pas le bon moment », « trop de projets en cours », « le budget est serré cette année », « on fera ça au prochain trimestre »). Le seul exercice réalisé est un tabletop basique il y a 18 mois, limité à l'équipe IT. La direction n'a jamais participé à un exercice de crise cyber.
>
> Conséquences : le CEO d'Arvantis découvre le fonctionnement d'une cellule de crise le samedi matin à 06h00, en situation réelle. Il ne comprend pas pourquoi « on ne peut pas simplement restaurer les sauvegardes et redémarrer ». Il ne connaît pas les obligations de notification ANSSI. Il est surpris par le coût du prestataire PRIS (« 2 500 € par jour et par consultant ?! »). Toutes ces surprises auraient été évitées par un exercice de crise incluant la direction.

---
