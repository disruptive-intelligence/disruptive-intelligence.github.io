---
title: Chapitre 26 — Décider sous incertitude
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie V — Confinement, décision ET préservation de preuve
  - index.md
---

## 26.1 La réalité de la prise de décision en IR

L'IR n'est pas seulement collecter, analyser, contenir. C'est **décider** — et décider avec des informations incomplètes, des contraintes métiers contradictoires, des coûts immédiats, des conséquences juridiques potentielles, et un stress intense.

À aucun moment de l'incident l'équipe IR ne dispose de « toutes les informations ». Le scoping est toujours approximatif. L'étendue de la compromission est toujours sous-estimée dans les premières heures. Le volume de données exfiltrées n'est jamais connu avec précision tant que l'investigation n'est pas terminée — et l'investigation prend des jours.

La discipline de décision consiste à expliciter ce qu'on sait, ce qu'on ne sait pas, et ce qu'on suppose, puis à décider en connaissance de cause de cette incertitude — pas à attendre la certitude qui ne viendra pas.

## 26.2 Arbitrage sécurité vs production

La sécurité veut isoler le réseau (pour contenir). La production veut maintenir le réseau (pour ne pas arrêter les usines). Les deux ont raison dans leur logique. L'arbitrage est une décision de direction, pas une décision technique — mais la direction a besoin de données claires pour décider.

L'IR lead doit formuler des **options** (pas une recommandation unique), avec pour chaque option : l'impact sécurité (quel risque accepte-t-on ?), l'impact business (quel coût subit-on ?), les conséquences (que se passe-t-il si l'option se révèle insuffisante ?), et la réversibilité (peut-on revenir en arrière ?).

## 26.3 Erreurs réversibles vs irréversibles

Un principe directeur en situation d'incertitude : **privilégier les actions réversibles**. Isoler un serveur via EDR est réversible (on peut lever l'isolation en un clic). Éteindre un serveur sans collecte mémoire est irréversible (la RAM est perdue pour toujours). Restaurer un système depuis une sauvegarde est irréversible (les artefacts forensic sont écrasés). Communiquer publiquement est irréversible (on ne peut pas « dé-communiquer »). Payer une rançon est irréversible (l'argent est parti).

Quand deux options offrent un niveau de sécurité comparable, choisir la plus réversible.

## 26.4 Documentation des décisions

Chaque décision significative est documentée dans le journal d'incident : qui a décidé, quand, sur la base de quelles informations (y compris les incertitudes), quelles alternatives ont été considérées, et pourquoi cette option a été retenue. Cette documentation protège les décideurs (ils ont agi raisonnablement avec les informations disponibles), alimente le retex (quelles informations manquaient pour mieux décider ?), et sert de preuve de bonne foi en cas de contentieux.

## 26.5 Comment formuler des options à la direction

La direction ne veut pas un briefing technique de 30 minutes. Elle veut 3 options, chacune sur une ligne, avec : ce qu'on fait, ce que ça coûte en arrêt de production, ce que ça risque en termes de sécurité, et le délai de reprise estimé. Un tableau situation/options/risques/recommandation sur une page, avec un niveau de confiance explicite, est le format le plus efficace.

## 26.6 Fil rouge — BLACKTIDE : les arbitrages du COMEX

> **🔍 BLACKTIDE — Épisode 26**
>
> Samedi 10h00. Réunion de la cellule de crise exécutive. Le CEO, Pierre Gautier, pose la question directe : « On redémarre quand ? »
>
> Marc (RSSI) présente le tableau des options de reprise (voir Ch.3, épisode BLACKTIDE). Le CEO choisit l'option B (reprise contrôlée, J+5 à J+12). La décision est documentée dans le PV de la réunion de crise, avec les réserves du RSSI (« le risque résiduel de l'option B n'est pas nul — nous recommandons un threat hunting post-reprise de 4 semaines ») et la signature du CEO.
>
> Deuxième arbitrage : la demande de rançon de 4,2 M€ arrivée à 09h00 via le portail de négociation PhantomCrypt. Le RSSI recommande de ne pas payer (les sauvegardes offline sont intactes, la production peut reprendre sans les données chiffrées). Le directeur juridique confirme qu'il n'y a pas d'obligation de payer, et que le paiement pourrait exposer Arvantis à des risques si l'opérateur est sanctionné par l'OFAC. Le CEO valide : pas de paiement. Décision documentée.

---
