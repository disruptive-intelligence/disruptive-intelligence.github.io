---
title: Chapitre 10 — Techniques analytiques structurées (TAS)
source: Cyber/01_CTI/CTI.md
note: Cyber Threat Intelligence (CTI)
up:
- - Cyber Threat Intelligence (CTI)
  - ../index.md
- - 'Partie III — L''analyse : le cœur du métier'
  - index.md
---

## 10.1 ACH — Analysis of Competing Hypotheses

L'ACH est la technique analytique structurée la plus importante pour l'analyste CTI. Développée par Richards Heuer (CIA, 1999), elle force l'analyste à formuler explicitement les hypothèses concurrentes et à évaluer chaque évidence contre chaque hypothèse — pas seulement contre l'hypothèse préférée.

**Le processus ACH en 7 étapes :**

**Étape 1 — Formuler les hypothèses :** lister toutes les hypothèses plausibles (minimum 3-4). Les hypothèses doivent être mutuellement exclusives (si H1 est vraie, les autres sont fausses) et collectivement exhaustives (l'une d'entre elles doit être vraie). Dans MERIDIAN : H1 (GRU/Sandworm), H2 (Chine/Volt Typhoon-like), H3 (mercenaire cyber), H4 (cybercriminel sophistiqué).

**Étape 2 — Lister les évidences :** toutes les données pertinentes, avec leur source et leur fiabilité. Les évidences incluent les faits observés (TTP, IoC, infrastructure, victimologie), les déductions, et les absences significatives (le fait que l'attaquant n'a PAS déployé de ransomware est une évidence — elle est incohérente avec H4).

**Étape 3 — Construire la matrice :** colonnes = hypothèses, lignes = évidences. Pour chaque cellule : l'évidence est-elle cohérente (C), incohérente (I), ou non applicable (N) avec l'hypothèse ?

**Étape 4 — Évaluer la matrice :** la clé de l'ACH n'est PAS de choisir l'hypothèse avec le plus de « C ». C'est d'éliminer les hypothèses avec le plus de « I ». La logique : une seule incohérence forte peut invalider une hypothèse, alors que la cohérence ne prouve rien (un acteur peut être cohérent avec une hypothèse sans que cette hypothèse soit correcte).

**Étape 5 — Identifier les évidences diagnostiques :** les évidences qui différencient le plus entre les hypothèses (cohérentes avec une hypothèse et incohérentes avec les autres) sont les plus précieuses. Les évidences cohérentes avec toutes les hypothèses ne sont pas diagnostiques — elles ne discriminent pas.

**Étape 6 — Conclure :** l'hypothèse la moins réfutée (avec le moins d'incohérences) est la conclusion, accompagnée d'un niveau de confiance. Si plusieurs hypothèses sont également non réfutées, la conclusion est « insuffisamment déterminé — données supplémentaires nécessaires ».

**Étape 7 — Identifier les milestones de révision :** quelles données nouvelles changeraient la conclusion ? Si un IoC de Sandworm est identifié dans l'infrastructure C2, H1 est renforcée. Si un tool custom chinois est trouvé dans les artefacts, H2 est renforcée. Ces milestones guident la collecte future.

## 10.2 Fil rouge — MERIDIAN : la matrice ACH

> **🔎 MERIDIAN — Épisode 6**
>
> Élise construit la matrice ACH pour les 4 hypothèses sur l'identité de UNC-VOLT.
>
> | Évidence | H1 GRU/Sandworm | H2 Chine/VoltTyphoon | H3 Mercenaire | H4 Cybercriminel |
> |----------|:---:|:---:|:---:|:---:|
> | Ciblage OIV énergie européen | C | C | C | I |
> | Pré-positionnement OT sans action | C | C | C | I |
> | Exploitation Ivanti (CVE-2024-21887) | C | C | C | C |
> | DLL sideloading (technique spécifique observée) | C | C | C | N |
> | Pas de ransomware, pas d'exfiltration financière | C | C | C | I |
> | Infrastructure C2 dans ASN Serverius (NL) | C | N | C | C |
> | Patterns de beaconing similaires à Sandworm/CaddyWiper | C | I | N | N |
> | Horaires d'activité UTC+3 | C | I | C | N |
> | Aucun outil custom chinois dans les artefacts | N | I | N | N |
> | Victimologie cohérente avec les objectifs GRU post-2022 | C | N | N | I |
>
> **Résultat :** H4 (cybercriminel) est éliminée (3 incohérences fortes). H2 (Chine) est affaiblie (3 incohérences — patterns de beaconing non chinois, horaires non chinois, pas d'outil chinois). H3 (mercenaire) reste possible mais peu étayée. H1 (GRU/Sandworm) est l'hypothèse la moins réfutée — conclusion avec **confiance modérée** (les TTP et la victimologie convergent, mais pas de preuve technique directe comme un outil Sandworm identifié ou un IoC partagé confirmé).

## 10.3 Autres TAS

**Key Assumptions Check :** identifier les hypothèses implicites qui sous-tendent l'analyse et les tester explicitement. Exemple dans MERIDIAN : « Nous supposons que l'attaquant est étatique parce que l'OT est ciblé et qu'il n'y a pas de rançon » — est-ce une hypothèse valide ? Les cybercriminels ne ciblent-ils jamais l'OT ? (réponse : ils le font parfois par erreur ou par opportunisme, mais l'absence de toute monétisation après 6 mois rend cette hypothèse faible).

**Red Hat Analysis :** se mettre dans la peau de l'adversaire. « Si j'étais UNC-VOLT (un acteur étatique cherchant à pré-positionner dans les infras critiques européennes), pourquoi aurais-je ciblé EDE ? Quelles seraient mes prochaines étapes ? » Cette perspective aide à anticiper les actions futures de l'acteur et à formuler les recommandations défensives.

**Méthode des cônes :** analyse prospective par scénarios. Le cône d'évolution (probable → plausible → possible → imaginable) appliqué à la question « UNC-VOLT va-t-il revenir cibler EDE dans les 12 prochains mois ? ». Scénario probable : oui, avec un vecteur d'accès différent (les vulnérabilités précédentes sont patchées). Scénario plausible : ciblage d'un sous-traitant d'EDE (supply chain). Scénario possible : passage à l'action destructive (sabotage OT). Scénario imaginable : utilisation des accès pour une opération d'influence (fuite de données internes pour déstabiliser).

---
