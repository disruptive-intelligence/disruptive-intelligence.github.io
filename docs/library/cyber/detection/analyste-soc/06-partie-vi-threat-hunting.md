---
title: Partie VI — Threat hunting
source: Cyber/06 Détection & réponse/Détection & SOC/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

*La recherche proactive de menaces que les règles de détection n'ont pas vues — la compétence qui distingue l'analyste avancé.*

---


## Chapitre 30 — Fondamentaux du Threat Hunting

Le hunting est la recherche proactive de menaces non détectées. L'analyste formule une hypothèse (basée sur la CTI, un rapport, une intuition, ou une anomalie observée) et la teste dans les données. Le hunting ne remplace pas la détection automatisée — il la complète en couvrant les angles morts (les techniques non couvertes par des règles, les variantes non anticipées, les comportements trop subtils pour les seuils automatiques).

Les approches : **hypothesis-driven** (la CTI fournit une hypothèse — « l'acteur X utilise le DLL sideloading sur les applications de supervision » → le hunter cherche), **data-driven** (l'analyste explore les données à la recherche d'anomalies — outliers, distributions inhabituelles, nouveaux patterns), et **intelligence-driven** (les IoC et TTP d'un rapport CTI sont recherchés proactivement dans les logs historiques — rétro-hunt).

Le processus : hypothèse → requête → résultats → analyse → conclusion (compromission trouvée → escalade IR et enrichissement du profil ; rien trouvé → enrichissement de la baseline, documentation, nouvelle hypothèse). Un hunt qui ne trouve rien n'est PAS un échec — il enrichit la connaissance de l'environnement (les « normaux » découverts pendant le hunt réduisent les futurs FP) et renforce la confiance dans la posture.

---


## Chapitre 31 — Techniques de hunting concrètes

**Stacking :** agrégation et comptage pour identifier les outliers. « Quels sont les processus les plus rares exécutés sur les postes du parc cette semaine ? » → requête SPL :

```
index=sysmon EventCode=1 earliest=-7d 
| stats count by Image 
| sort count 
| head 20
```

Les processus avec 1-2 occurrences sur 500 postes méritent investigation — pourquoi un seul poste exécute-t-il ce binaire ?

**Frequency analysis pour le beaconing :** analyse des intervalles de connexion d'un processus vers une destination. Requête SPL :

```
index=proxy src_ip="10.0.5.112" dest="185.xx.xx.xx" 
| sort _time 
| streamstats current=f last(_time) as prev_time 
| eval interval=_time-prev_time 
| stats avg(interval) as avg_int stdev(interval) as std_int count by src_ip dest
| eval jitter_pct=(std_int/avg_int)*100
| where jitter_pct < 15 AND count > 50
```

Un intervalle moyen régulier (ex : 45 secondes) avec un jitter faible (< 15 %) est un indicateur fort de beaconing automatisé.

**Long tail analysis :** les événements rares dans les distributions — les domaines DNS avec 1-2 requêtes dans tout le parc, les user-agents avec 1-2 occurrences, les connexions vers des pays inhabituels. Ces outliers sont souvent du bruit légitime — mais occasionnellement, c'est un C2 discret qui n'a contacté qu'une seule machine.

**Hunt sur les LOLBins :** recherche d'utilisations suspectes de certutil, mshta, bitsadmin, regsvr32, rundll32 — en contexte. L'outil est légitime, c'est le contexte qui distingue l'usage malveillant : qui exécute (un utilisateur standard, pas un admin), depuis quel processus parent (winword.exe, pas cmd.exe lancé manuellement), avec quels arguments (certutil -urlcache -f, pas certutil -verify), et à quelle heure.

---


## Chapitre 32 — Purple teaming et validation de détection

Le purple team est la collaboration structurée entre l'offensive (red team) et la défensive (SOC) pour valider l'efficacité des détections. Le processus : le red team exécute une technique ATT&CK spécifique (par exemple T1059.001 PowerShell -EncodedCommand) → le SOC vérifie si l'alerte s'est déclenchée → si oui : la détection fonctionne, documenter → si non : gap identifié, la règle est créée ou corrigée → le test est rejoué pour valider.

**Atomic Red Team** (Red Canary, open source) est la bibliothèque de tests unitaires par technique ATT&CK — chaque test est un script exécutable en un clic qui simule une technique d'attaque spécifique (pas un exploit réel — une simulation safe qui génère les mêmes artefacts de détection). L'analyste SOC peut exécuter un test Atomic RT et vérifier dans son SIEM si l'alerte se déclenche — sans avoir besoin d'un red teamer.

Le cycle purple team comme processus d'amélioration continue : 2 techniques testées par semaine, documentées, avec le résultat (détecté / non détecté / partiellement détecté), les actions correctives (règle créée, règle modifiée, log source ajouté), et la re-validation. En 6 mois, un programme purple team régulier améliore dramatiquement la couverture ATT&CK du SOC.

---
