---
title: Chapitre 15 — Investigation réseau
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

Les logs réseau complètent l'investigation endpoint et identité.

**Analyse du beaconing C2 :** les logs proxy montrent les connexions HTTPS vers `185.xx.xx.xx` avec un pattern temporel régulier (intervalle de 45 secondes ± 3 secondes). Le user-agent est `Mozilla/5.0 (Windows NT 10.0; Win64; x64) NorexiaUpdate/1.0` — un user-agent custom qui imite un navigateur légitime mais avec un suffixe inhabituel.

**Recherche d'exfiltration :** les logs proxy montrent qu'à J+1 (dimanche), le poste WKS-IT-045 (le second poste compromis — poste d'un admin IT) a lancé `rclone.exe` qui a uploadé 12 Go de données vers un bucket S3 externe. Le SRUM (System Resource Usage Monitor) sur WKS-IT-045 confirme que `rclone.exe` a consommé 12.3 Go de bande passante réseau en 4 heures.

**Reconstruction de la timeline réseau :** corrélation firewall + proxy + DNS pour reconstituer les communications de l'attaquant heure par heure. Les résolutions DNS montrent que `update-norexia[.]xyz` a été résolu pour la première fois samedi à 08h12 UTC (le moment du phishing initial) — 23 heures avant la détection par l'EDR lundi à 07h42.

---
