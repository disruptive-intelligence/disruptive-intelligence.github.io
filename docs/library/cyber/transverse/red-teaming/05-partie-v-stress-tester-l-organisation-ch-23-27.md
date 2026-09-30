---
title: Partie V — Stress-tester L'organisation (ch.23-27)
source: Cyber/Red_Teaming.md
note: Red teaming
up:
- - Red teaming
  - index.md
---

*Troisième couche du triptyque : quoi tester. La Partie IV traitait du **comment exercer**. Cette partie traite des **objets du test** : les plans et stratégies existantes, démontés hypothèse par hypothèse.*

*La promesse du stress-test est distincte de celle de l'exercice : **démonter les hypothèses implicites d'un plan ou d'une stratégie, pour en révéler les fragilités avant qu'un incident réel ne les révèle.***

---


## Chapitre 23 — La logique du stress-test

### Synopsis

Distinction fondamentale avec l'exercice :

- **L'exercice** (Partie IV) met en scène un scénario et observe comment l'organisation réagit.
- **Le stress-test** prend un plan ou une stratégie existante, identifie ses hypothèses implicites, et les soumet au démontage systématique par les TAS de la Partie III.

Les deux sont complémentaires : un stress-test peut précéder un exercice (« quelles hypothèses de ce plan sont les plus fragiles ? → on va tester celles-là ») ou lui succéder (« l'exercice a révélé que X ne fonctionnait pas → stress-test systématique de X »).

**Méthodologie générale du stress-test :**

1. Identifier l'objet à stress-tester (document : stratégie, plan IR, PCA, plan de com)
2. Déconstruire en hypothèses explicites et implicites
3. Pour chaque hypothèse, appliquer les TAS pertinentes : Devil's Advocacy, pre-mortem, What-If, ACH
4. Classer les hypothèses par solidité : vérifiées, plausibles non vérifiées, fragiles
5. Produire un rapport de stress-test avec recommandations

**L'écueil à éviter :** le stress-test qui se contente de lister des risques génériques sans les ancrer dans des hypothèses spécifiques du document analysé. Un stress-test qui pourrait s'appliquer à n'importe quelle organisation est un stress-test qui ne sert à rien.

> **🪞 MIRRORGATE — Épisode 23 :** Diane explique le protocole à Thomas. « On prend le plan IR. On sort un stylo rouge. On ne cherche pas ce qui nous plaît. On cherche chaque phrase qui commence par un 'en cas de' ou un 'si', et on se demande : cette hypothèse est-elle vraie ? Si elle est fausse, qu'est-ce qui casse ? »

---


## Chapitre 24 — Stress-test de la stratégie de cybersécurité

### Synopsis

Application du protocole à la stratégie cyber.

**Hypothèses stratégiques les plus fréquemment fragiles :** « notre périmètre est défini et contrôlé » (shadow IT, IoT, OT non inventorié), « nos sous-traitants appliquent nos exigences » (pas de vérification réelle), « notre plan IR fonctionne » (jamais testé), « notre sensibilisation est efficace » (mesurée en taux de complétion de e-learning, pas en résistance réelle au phishing ciblé).

Livrable type : rapport de stress-test stratégique avec hypothèses vérifiées / plausibles / fragiles, et recommandations priorisées.

> **🪞 MIRRORGATE — Épisode 24 :** Stress-test de la stratégie 2025-2027 d'Hélio. 14 hypothèses implicites identifiées. 4 solides, 6 plausibles, 4 fragiles. La plus fragile : « notre architecture réseau empêche le pivot IT → OT ». Diane découvre 3 points de passage non documentés — dont un poste à double connexion, exactement le vecteur utilisé lors de l'incident passé. Non éliminé pendant la remédiation.

---


## Chapitre 25 — Stress-test du plan de réponse à incident

### Synopsis

Application du protocole au plan IR (lien cours IR).

Pour chaque phase (détection, qualification, confinement, éradication, recovery, communication, RETEX), trois questions :

1. **« Le plan suppose X — est-ce vérifié ? »** (ex : le plan suppose une détection SOC en moins de 24h — est-ce le cas pour les TTP de nos adversaires prioritaires ?)
2. **« Le plan prévoit que Y fait Z — Y le sait-il ? A-t-il les moyens ? L'a-t-il déjà fait ? »**
3. **« Le plan fonctionne en conditions normales — fonctionne-t-il en conditions dégradées ? »** (ex : le plan fonctionne si l'AD est disponible — fonctionne-t-il si l'AD est compromis ?)

Défaillances les plus fréquemment révélées : plan non à jour, non connu (les personnes nommées ignorent leur rôle), non réaliste (délais incompatibles avec les capacités), non résilient (ne fonctionne pas si l'infrastructure de communication elle-même est compromise).

> **🪞 MIRRORGATE — Épisode 25 :** Diane interroge chaque personne nommée dans le plan IR. 3 sur 8 ne savent pas qu'elles y figurent. 2 ont changé de poste. Le numéro d'urgence du prestataire IR est un ancien numéro. Et le plan suppose que les communications de crise passent par l'email — premier service coupé en cas de ransomware.

---


## Chapitre 26 — Stress-test des plans de continuité et de reprise (PCA/PRA)

### Synopsis

Spécificité du stress-test PCA/PRA dans un contexte cyber : ces plans sont souvent conçus pour des sinistres physiques (incendie, inondation) et ne couvrent pas les spécificités d'un incident cyber.

Hypothèses PCA/PRA à tester : sauvegardes intègres et restaurables (testé quand pour la dernière fois ?), site de repli opérationnel (avec quel délai, quelle capacité ?), processus métiers sans IT pendant X heures/jours (vérifié avec les métiers ?), reconstruction AD maîtrisée (avec quel processus, quels outils, quel personnel ?), reprise dans un environnement sain (comment s'assurer que l'attaquant n'est pas dans l'environnement restauré ?).

Le scénario **worst case réaliste** : ransomware + exfiltration + destruction des sauvegardes en ligne + compromission de l'AD + indisponibilité du prestataire habituel (mobilisé sur un autre incident).

> **🪞 MIRRORGATE — Épisode 26 :** « Combien de temps pour reconstruire l'AD de zéro ? » — « On n'a jamais fait l'exercice. Le PRA prévoit une restauration depuis la sauvegarde. » — « Et si la sauvegarde est chiffrée ? » Silence. « Vous avez un PRA qui fonctionne si les sauvegardes fonctionnent. Pas un PRA pour le cas où elles ne fonctionnent pas. »

---


## Chapitre 27 — Stress-test de la communication de crise et du dispositif réglementaire

### Synopsis

Stress-test des dimensions souvent parents pauvres de la préparation — et pourtant les plus visibles (et les plus destructrices) en cas de défaillance.

**La communication de crise cyber :** parties prenantes (employés, clients, partenaires, régulateurs, médias, actionnaires), messages (que dit-on, que ne dit-on pas), timing (trop tôt = incomplet, trop tard = dissimulation), porte-parole (qui, avec quel mandat, avec quelle préparation).

**Les obligations réglementaires :** ANSSI (OIV, OSE, NIS 2), CNIL (RGPD — 72h), notification sectorielle (DORA pour la finance, réglementation nucléaire pour l'énergie), notification contractuelle (clients, partenaires). Stress-test : les responsables savent-ils quelles notifications sont obligatoires ? Connaissent-ils les délais ? Ont-ils les templates ? Les contacts ?

**Le scénario de stress communicationnel :** la fuite médiatique avant la communication officielle, l'instrumentalisation par l'adversaire (le groupe ransomware tweete, contacte les clients, publie sur le leak site), la crise réputationnelle qui survit à l'incident technique.

> **🪞 MIRRORGATE — Épisode 27 :** Stress-test du dispositif com. Aucun Q&A préparé pour scénario cyber, aucun porte-parole identifié, aucun template de communiqué, le responsable com « n'a jamais géré de crise cyber ». Diane : « Dans un incident réel, vous aurez 2 à 6 heures entre la fuite publique et le moment où vous devez parler. Si vous n'êtes pas prêts, ce sont les autres qui parleront de vous. »

---
