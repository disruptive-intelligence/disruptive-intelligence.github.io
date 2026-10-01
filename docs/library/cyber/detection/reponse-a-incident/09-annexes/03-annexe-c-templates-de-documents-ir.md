---
title: Annexe C — Templates de documents IR
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Annexes
  - index.md
---

## Template SitRep

```
SITREP #[N] — [NOM OPÉRATION] — [DATE HEURE]
Classification : [INTERNE / CONFIDENTIEL]

1. CE QU'ON SAIT (faits confirmés)
   - ...

2. CE QU'ON NE SAIT PAS (inconnues explicites)
   - ...

3. CE QU'ON FAIT (actions en cours)
   - ...

4. CE QU'ON ENVISAGE (prochaines étapes, options)
   - ...

5. CE DONT ON A BESOIN (ressources, décisions, autorisations)
   - ...

6. PROCHAINE ÉCHÉANCE : [date/heure]

Rédigé par : [nom]    Validé par : [nom]
```


## Template journal d'incident

```
JOURNAL D'INCIDENT — [NOM OPÉRATION]
Ouvert le : [date heure]    IR Lead : [nom]

| Date/Heure | Auteur | Action / Observation / Décision | Source | Impact |
|-----------|--------|-------------------------------|--------|--------|
| JJ/MM HH:MM | [nom] | [description] | [source] | [impact] |
```


## Template notification CNIL (72h)

```
NOTIFICATION DE VIOLATION DE DONNÉES PERSONNELLES
(Article 33 du RGPD)

1. NATURE DE LA VIOLATION
   Type : [confidentialité / intégrité / disponibilité]
   Description : [description factuelle]
   Date de prise de connaissance : [date]

2. CATÉGORIES DE DONNÉES CONCERNÉES
   [données d'identification, données financières, données de santé, etc.]

3. CATÉGORIES ET NOMBRE DE PERSONNES CONCERNÉES
   [nombre estimé]    [catégories : employés, clients, partenaires]

4. CONSÉQUENCES PROBABLES
   [risque d'usurpation d'identité, risque financier, etc.]

5. MESURES PRISES OU PROPOSÉES
   [mesures de confinement, d'éradication, de notification aux personnes]

6. COORDONNÉES DU DPO
   [nom, email, téléphone]
```


---
