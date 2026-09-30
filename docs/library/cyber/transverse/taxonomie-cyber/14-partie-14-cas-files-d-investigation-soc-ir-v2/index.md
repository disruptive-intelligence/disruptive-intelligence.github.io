---
title: Partie 14 — Cas filés d'investigation SOC/IR (V2)
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - ../index.md
---

> Cette partie répond à la principale limite du référentiel : le passage du *vocabulaire* au *raisonnement opérationnel*. Six cas filés déroulent le cycle complet **événement → alerte → hypothèse → qualification → investigation → confinement → éradication → rétablissement → REX**, en nommant à chaque étape les **sources de logs**, les **signaux faibles** et les **décisions défensives**.
>
> **Posture inchangée** : défensive et pédagogique. Les cas sont conceptuels — aucune procédure offensive, aucune commande d'exploitation. Les noms de journaux et d'identifiants d'événements sont donnés à titre indicatif (les versions exactes évoluent ; se reporter aux sources de l'Annexe I).


## Schéma de référence du cycle d'incident

```text
ÉVÉNEMENT ──► ALERTE ──► TRIAGE ──► QUALIFICATION ──► [INCIDENT ?]
                                                          │ oui
                                                          ▼
   INVESTIGATION ──► CONFINEMENT ──► ÉRADICATION ──► RÉTABLISSEMENT ──► REX
   (portée totale)   (stopper)       (tout retirer)  (restaurer sain)   (apprendre)
        ▲                                                                   │
        └───────────────── boucle d'amélioration continue ◄────────────────┘
```


🧭 **Comment lire un cas.** Chaque cas suit la même trame : *contexte → signal initial → classement taxonomique (renvois aux chapitres) → hypothèse → sources de logs → investigation/pivots → confinement → éradication → rétablissement → REX → erreurs à éviter*.

---

## Dans cette partie

- [Chapitre 314 — Cas 1 : Phishing avec vol d'identifiants](01-chapitre-314-cas-1-phishing-avec-vol-d-identifiant.md)
- [Chapitre 315 — Cas 2 : Suspicion de Kerberoasting](02-chapitre-315-cas-2-suspicion-de-kerberoasting.md)
- [Chapitre 316 — Cas 3 : Malware sur un poste de travail](03-chapitre-316-cas-3-malware-sur-un-poste-de-travail.md)
- [Chapitre 317 — Cas 4 : Exfiltration depuis le cloud](04-chapitre-317-cas-4-exfiltration-depuis-le-cloud.md)
- [Chapitre 318 — Cas 5 : Ransomware](05-chapitre-318-cas-5-ransomware.md)
- [Chapitre 319 — Cas 6 : SSRF vers les métadonnées cloud](06-chapitre-319-cas-6-ssrf-vers-les-metadonnees-cloud.md)
