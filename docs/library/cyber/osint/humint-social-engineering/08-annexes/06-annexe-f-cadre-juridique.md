---
title: Annexe F — Cadre juridique
source: Cyber/02 OSINT/Facteur humain/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Annexes
  - index.md
---

## F.1 France

| Infraction | Article du Code pénal | Peine maximale | Application au SE |
|---|---|---|---|
| Escroquerie | Art. 313-1 | 5 ans + 375 000 € | Fraude au président, BEC, phishing |
| Usurpation d'identité | Art. 226-4-1 | 1 an + 15 000 € | Impersonation (y compris en ligne) |
| Accès frauduleux à un STAD | Art. 323-1 | 3 ans + 100 000 € | Intrusion informatique post-phishing |
| Atteinte au secret des correspondances | Art. 226-15 | 1 an + 45 000 € | Compromission de boîte mail |
| Fabrication/usage de faux | Art. 441-1 | 3 ans + 45 000 € | Faux documents, faux badges |
| Violation de domicile | Art. 226-4 | 1 an + 15 000 € | Intrusion physique non autorisée |
| Collecte frauduleuse de données personnelles | Art. 226-18 | 5 ans + 300 000 € | Credential harvesting |

**Le red team autorisé** : la lettre de mission signée par un représentant habilité constitue le fondement juridique de l'autorisation. Elle ne crée pas un « droit à commettre des infractions » mais établit le consentement de l'organisation — ce qui élimine l'un des éléments constitutifs de la plupart des infractions (le caractère frauduleux, non autorisé ou sans le consentement de la victime). La lettre de mission doit être juridiquement robuste (rédaction par un avocat recommandée) et couvrir explicitement chaque technique utilisée.

**RGPD.** Les données personnelles collectées pendant un test de SE (identifiants, informations personnelles, photos) sont soumises au RGPD. Le traitement doit avoir une base légale (l'intérêt légitime du responsable de traitement, avec l'analyse d'impact correspondante), les données doivent être minimisées, sécurisées et détruites après la fin de la mission.

## F.2 Comparatif international

| Aspect | France | Union européenne | États-Unis |
|---|---|---|---|
| Usurpation d'identité en ligne | Délit spécifique (art. 226-4-1) | Variable selon les États membres | Federal : 18 USC § 1028, variable selon les États |
| Enregistrement de conversations | Interdit sans consentement (art. 226-1) | Variable (certains pays autorisent avec une seule partie consentante) | Variable selon les États (one-party vs two-party consent) |
| Red team autorisé | Encadré par lettre de mission | Encadré par le droit national des États membres | Encadré par contrat, jurisprudence CFAA |
| Pretexting dans les enquêtes privées | Limité (pas de faux documents officiels) | Variable | Plus largement toléré (sauf pour obtenir des données financières — GLBA) |

---
