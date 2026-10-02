---
title: MTTD, MTTC, MTTR
source: Cyber/12 Fiches notions/MTTD, MTTC, MTTR.md
format: fiche
revue: '2026-10-02'
terms:
  MTTD: Mean Time To Detect — délai moyen entre la compromission (ou l'événement malveillant) et sa détection.
  MTTC: Mean Time To Contain — délai moyen entre la détection et le confinement effectif.
  MTTR: Mean Time To Respond, Remediate ou Recover selon le contexte — toujours préciser lequel.
  MTTA: Mean Time To Acknowledge — délai moyen entre une alerte et sa prise en charge par un analyste.
  MTTI: Mean Time To Inventory — délai moyen pour qu'un actif nouveau ou modifié apparaisse dans l'inventaire.
  Dwell time: Temps de séjour de l'attaquant — durée entre la compromission initiale et la détection.
---

> Fiche notion assemblée à partir de mes notes (sources en fin de fiche), complétée là où mes cours sont muets.

## En bref

| Sigle | Mesure le délai entre… | … et | Question posée |
|---|---|---|---|
| **MTTI** | l'apparition d'un actif | son entrée dans l'inventaire | Sait-on ce qu'on doit protéger ? |
| **Dwell time** | la compromission initiale | la détection (un incident) | Combien de temps l'attaquant est-il resté ? |
| **MTTD** | la compromission / l'événement | la détection | Voit-on vite ? |
| **MTTA** | l'alerte | sa prise en charge | L'alerte attend-elle dans la file ? |
| **MTTC** | la détection | le confinement | Arrête-t-on vite la propagation ? |
| **MTTR** | la détection ou le confinement | la réponse, la remédiation ou la reprise | Selon le « R » choisi |

*Tableau de synthèse ; les définitions sourcées suivent.*

## Le cycle d'un incident : MTTD, MTTC, MTTR

Les métriques clés pour évaluer et améliorer la capacité IR. Le **MTTD** (Mean Time To Detect) : délai entre la compromission initiale et la détection. Pour BLACKTIDE : 35 jours (l'infostealer est resté non détecté pendant 5 semaines) — un chiffre élevé qui révèle les failles de détection. Le **MTTC** (Mean Time To Contain) : délai entre la détection et le confinement effectif. Pour BLACKTIDE : environ 3 heures (de l'alerte EDR à la décision de confinement des 3 sites) — un chiffre honorable. Le **MTTR** (Mean Time To Recover) : délai entre le confinement et la reprise complète. Pour BLACKTIDE : 12 jours — un chiffre dans la norme pour un incident de cette ampleur.[^1]

## Le même sigle, trois sens pour le « R »

Les métriques qui comptent : **MTTD** (Mean Time to Detect — temps entre l'événement malveillant et sa détection par le SOC ; cible : < 1h pour les critiques — dans FALCONWATCH, le MTTD est de ~23h car l'infection initiale samedi 08h12 n'a été détectée que lundi 07h42), **MTTR** (Mean Time to Respond — temps entre la détection et le confinement ; cible : < 4h — dans FALCONWATCH, le MTTR est de ~45 minutes entre la détection et l'isolation des postes), **taux de FP** (% d'alertes faussement positives ; cible : < 15 % — au-dessus de 30 %, le SOC est en surcharge), **backlog** (alertes en attente de triage ; cible : proche de 0 en fin de shift), **couverture ATT&CK** (% de techniques couvertes par des règles testées ; amélioration continue via le purple team), et **taux de détection SOC** (% d'incidents détectés par le SOC vs découverts par d'autres moyens — utilisateur, tiers, médias ; cible : > 80 %).[^2]

Le **MTTRemediate — Mean Time to Remediate** mesure le délai entre la détection d'une vulnérabilité chez vous (par scan, advisory, ou autre signal) et sa remédiation effective. C'est la métrique opérationnelle clé pour le programme VM.[^3]

> En réponse à incident, MTTR = *Recover* (du confinement à la reprise) ; au SOC, MTTR = *Respond* (de la détection au confinement, ce que la réponse à incident appelle MTTC) ; en gestion des vulnérabilités, MTTR = *Remediate*. Toujours écrire le mot entier dans un tableau de bord.

*Remarque de synthèse sur les trois passages ci-dessus.*

## Dwell time — le temps de séjour

Le dwell time — la durée entre la compromission initiale et la détection — est la métrique qui détermine la profondeur de l'investigation. Selon le M-Trends 2025 de Mandiant, la médiane mondiale est d'environ 10 à 13 jours, avec une amélioration progressive grâce à la généralisation des EDR. Mais cette médiane masque une distribution très dispersée : les ransomwares sont souvent détectés en quelques jours (l'attaquant accélère pour chiffrer), tandis que les opérations d'espionnage peuvent durer des mois, voire des années.[^4]

## Côté vulnérabilités : TTE et TTPatch

Le **TTPatch — Time to Patch** mesure le délai entre la disponibilité du patch (par le vendor) et son déploiement effectif sur les actifs concernés. Cette métrique est interne à chaque organisation et reflète sa maturité opérationnelle.[^3]

## Les remonter à la gouvernance

**Indicateurs opérationnels** (pour le RSSI et l'équipe sécurité, fréquence hebdomadaire) : nombre d'incidents par sévérité, MTTD (temps moyen de détection), MTTR (temps moyen de réponse), taux de patching par criticité (critique < 48h, élevé < 15 jours), nombre de vulnérabilités critiques ouvertes et tendance, couverture EDR (% des endpoints protégés), et backlog d'alertes SOC.[^5]

## Compléments (pas encore dans mes cours)

- **MTTI — Mean Time To Inventory** : délai moyen entre l'apparition d'un actif (nouveau serveur, instance cloud, application, compte de service) et son entrée dans l'inventaire. Un actif absent de l'inventaire n'est ni scanné, ni supervisé, ni sauvegardé : un MTTI élevé allonge mécaniquement le MTTD.
- **MTTA — Mean Time To Acknowledge** : délai moyen entre la levée d'une alerte et sa prise en charge par un analyste. Il isole l'attente dans la file du SOC, que le MTTD ou le MTTR masquent.
- **Pièges de lecture** : une moyenne est tirée par quelques incidents très longs (regarder aussi la médiane) ; un MTTD ne compte que les incidents détectés ; chaque délai n'a de sens qu'avec ses bornes écrites noir sur blanc (quel horodatage de début, quel horodatage de fin).

*Compléments rédigés pour cette fiche, à confronter à un cours quand j'en aurai un sur le sujet.*

## Pour approfondir

- [Réponse à incident](../detection/reponse-a-incident/index.md) — chapitre 11 (détection, dwell time) et métriques de fin de cours.
- [Analyste SOC](../detection/analyste-soc/index.md) — métriques et pilotage du SOC.
- [Vulnerability management & intelligence](../vulnerabilites/vulnerability-management-intelligence/index.md) — chapitre 25 (patch gap, TTE, TTPatch, MTTRemediate).

## Voir aussi

[CVE, CWE, CVSS, EPSS, KEV](cve-cwe-cvss-epss-kev.md) · [IOC, IOA, TTP](ioc-ioa-ttp.md)

## Sources

[^1]: [Réponse à incident](../detection/reponse-a-incident/index.md), chapitre sur les métriques IR.
[^2]: [Analyste SOC](../detection/analyste-soc/index.md), métriques du SOC.
[^3]: [Vulnerability management & intelligence](../vulnerabilites/vulnerability-management-intelligence/index.md), chapitre 25.
[^4]: [Réponse à incident](../detection/reponse-a-incident/index.md), chapitre 11.2.
[^5]: [GRC](../gouvernance/gouvernance-risques-et-conformite-grc/index.md), indicateurs opérationnels.
