---
title: 'Chapitre 24 — Attribution : méthodes, limites et enjeux'
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie VII — Géopolitique, attribution et prospective
  - index.md
---

## 24.1 Les trois niveaux d’attribution

L’**attribution** d’une cyberopération signifie différentes choses selon le niveau d’analyse. La confusion entre ces niveaux est la première source d’erreur analytique.

**Niveau 1 — Attribution technique** : relier une activité observée à un **intrusion set** identifié (APT29, Sandworm, Volt Typhoon, etc.). Fondée sur les TTP, l’infrastructure, le malware, la victimologie. Seuil de preuve : cohérence du faisceau technique avec un profil documenté. C’est l’attribution la plus accessible et la plus couramment produite par les vendors CTI.

**Niveau 2 — Attribution opérationnelle** : relier l’intrusion set à un **service ou une unité spécifique** (SVR russe, MSS Tianjin chinois, Lazarus/RGB nord-coréen, MOIS iranien). Nécessite des évidences supplémentaires — renseignement sur l’organisation sponsor, patterns d’horaires, artefacts linguistiques. Seuil de preuve : lien démontré entre l’intrusion set et une organisation spécifique.

**Niveau 3 — Attribution stratégique** : relier l’opération à un **État et une intention politique**. Qui a commandité ? Dans quel but stratégique ? Quels objectifs géopolitiques servis ? Seuil de preuve : compréhension contextuelle et renseignement non-technique (HUMINT, SIGINT stratégique, contexte diplomatique).

Les trois niveaux ont des **seuils de preuve croissants** et des **implications différentes**. Une attribution technique (« c’est APT29 ») est différente d’une attribution stratégique (« opération du SVR commanditée dans le cadre de la collecte de renseignement sur les positions européennes vis-à-vis de l’Ukraine »).

Les attributions publiques gouvernementales (indictments DOJ, advisories Five Eyes) atteignent souvent les trois niveaux. Les rapports CTI privés s’arrêtent souvent au niveau 1-2, laissant les considérations stratégiques en termes plus prudents.

## 24.2 Les évidences d’attribution

Plusieurs catégories d’évidences construisent l’attribution. Leur **convergence** renforce la confiance, leur divergence l’affaiblit.

**TTP / tradecraft** : la manière dont l’attaquant opère. Patterns de reconnaissance, choix de vecteurs, outils utilisés, techniques de persistence, de mouvement latéral, d’exfiltration. Les TTP sont plus durables que les IoC (Pyramide de la Douleur), et un tradecraft mature est une signature forte.

**Infrastructure** : domaines, IP, certificats, serveurs C2, patterns d’enregistrement. Un même attaquant réutilise souvent des patterns d’infrastructure (même registrar, même hébergeur, même structure de sous-domaines) — erreur d’OPSEC fréquente même chez les acteurs sophistiqués.

**Malware** : familles de malware, signatures techniques du code, patterns de développement (commentaires, noms de variables, structure), artefacts de compilation (paths PDB, fuseau horaire de la machine de compilation, langue du système).

**Victimologie** : qui est ciblé ? Si une campagne cible exclusivement des entreprises de semiconducteurs dans l’UE et les US, le profil des cibles est un signal — la Chine a un intérêt documenté, la Russie moins, la DPRK encore moins. La victimologie aligne sur les priorités stratégiques connues.

**Timing géopolitique** : l’attaque coïncide-t-elle avec un événement politique ? Une tentative d’ingérence électorale avant un scrutin, une campagne contre des institutions ukrainiennes lors d’une escalade militaire, un ciblage énergétique en hiver — le timing renforce certaines hypothèses.

**Renseignement HUMINT / SIGINT** : accessible seulement aux services étatiques. Les attributions publiques gouvernementales peuvent s’appuyer sur ce renseignement (sans le révéler). Les vendors privés n’y ont pas accès, d’où la différence de nature entre attribution publique gouvernementale et rapport CTI privé.

**Erreurs opérationnelles** : artefacts qui trahissent l’origine. Langue maternelle dans les commentaires de code, fuseau horaire de la machine de compilation, réutilisation d’infrastructure déjà attribuée, horaires de travail compatibles avec un fuseau horaire donné.

**Lien avec des indictments antérieurs** : si des opérateurs nommément identifiés par un indictment antérieur réapparaissent (mêmes emails, mêmes identités), l’attribution devient extrêmement solide.

## 24.3 Les pièges classiques de l’attribution

Plusieurs pièges classiques doivent être systématiquement écartés.

**False flags** : un attaquant plante délibérément des indices qui pointent vers un autre acteur. **Olympic Destroyer (2018)** est le cas d’école : Sandworm a inclus des fragments de code Lazarus documenté (DPRK), des infrastructures évoquant les APT chinoises, et des artefacts linguistiques trompeurs. L’analyse minutieuse par Kaspersky a identifié les faux marqueurs et consolidé l’attribution Sandworm. Leçon : un faisceau d’évidences apparemment convergent peut être fabriqué.

**Piggybacking sur une autre APT** : **Turla** a utilisé l’infrastructure d’APT34 (OilRig, Iran) pour ses propres opérations. Une victime qui voit une intrusion en provenance d’infrastructure connue comme iranienne peut être trompée sur l’origine réelle.

**Outils partagés** : **Cobalt Strike** est utilisé par presque tous les acteurs offensifs (APT étatiques, red teams légitimes, groupes ransomware). La seule présence de Cobalt Strike ne discrimine rien. Les infrastructures Let’s Encrypt, les VPS génériques, les services cloud légitimes sont utilisés par tous.

**Infrastructure louée / partagée** : les VPS sont loués, les domaines enregistrés via des registrars communs. Une IP qui a hébergé une opération APT29 il y a deux ans peut héberger aujourd’hui un site e-commerce légitime ou une opération totalement distincte.

**Biais géopolitiques** : attribuer à la Russie « par défaut » parce que le contexte le rend plausible est une erreur méthodologique. La discipline ACH exige de tester **plusieurs hypothèses** contre les mêmes évidences.

**Biais de confirmation** : une fois une hypothèse formulée tôt, l’investigateur tend à chercher des preuves qui la confirment et à ignorer celles qui la contredisent. Parade : formuler explicitement l’hypothèse, puis **chercher activement** les évidences qui l’invalideraient.

**Effet de signature reconnue** : reconnaître un pattern connu produit une sensation de certitude (« c’est Volt Typhoon, je le sens »). Cette intuition est utile mais doit être formalisée et testée contre les alternatives.

## 24.4 Les niveaux de confiance et le vocabulaire calibré

L’attribution ne produit jamais de certitudes absolues. La communication analytique utilise un **vocabulaire calibré** — les **Words of Estimative Probability** (WEP), hérités de la tradition analytique CIA et adoptés par les services occidentaux et les vendors CTI sérieux.

|Expression                                   |Probabilité|
|---------------------------------------------|-----------|
|Almost certain / Quasi-certain               |>95 %      |
|Very likely / Très probable                  |80-95 %    |
|Likely / Probable                            |55-80 %    |
|Roughly even chance / Indéterminé            |45-55 %    |
|Unlikely / Improbable                        |20-45 %    |
|Very unlikely / Très improbable              |5-20 %     |
|Almost certainly not / Quasi-certainement non|<5 %       |

**Usage** : une attribution publique doit situer son niveau de confiance. « Attribution à APT29 avec haute confiance » signifie quelque chose de précis. « Attribution à APT29 » sans qualification laisse l’interprétation ouverte et est moins rigoureux.

**Évolution de la confiance** : la confiance peut évoluer avec de nouvelles évidences. Une attribution à confiance modérée au jour J peut devenir attribution à haute confiance au jour J+30, ou rester à confiance modérée indéfiniment.

**Règles de communication** :

- Jamais « certain » sans qualification.
- Préciser le **niveau** d’attribution (technique, opérationnelle, stratégique).
- Documenter les **évidences majeures**.
- Mentionner les **hypothèses alternatives considérées et écartées**.
- Identifier les **indicateurs de révision** — ce qui, si trouvé, remettrait en question l’attribution.

## 24.5 L’attribution publique par les gouvernements

Les attributions publiques gouvernementales ont un statut particulier. Elles conjuguent renseignement technique, SIGINT/HUMINT classifié, et considérations diplomatiques.

**Formats** :

- **Advisories conjoints** (NSA/CISA/FBI + Five Eyes + alliés) : ton technique, IoC partagés, TTP détaillées.
- **Indictments DOJ** : mise en accusation formelle avec détails opérationnels publiés. Effet de naming and shaming.
- **Sanctions (OFAC, UE, UK)** : désignation de personnes et entités, interdiction de transactions. Effet financier et symbolique.
- **Déclarations officielles** : communiqués diplomatiques, déclarations aux parlements, auditions publiques.
- **Rapports gouvernementaux** : rapports annuels des agences (ANSSI Panorama de la cybermenace, NCSC Annual Review, CISA reports).

**Pourquoi publier** : naming and shaming, coordination internationale, dissuasion, armement des défenseurs, appui aux sanctions.

**Pourquoi ne pas publier** : protection des sources et méthodes, considérations diplomatiques, incertitude insuffisante, valeur continue de la surveillance (révéler un pré-positionnement détecté peut compromettre la capacité de le surveiller).

L’attribution publique est un **acte politique** autant que technique.

## 24.6 Les attributions privées : vendors CTI

Les vendors CTI privés produisent massivement des attributions — avec forces et limites distinctes des attributions publiques gouvernementales.

**Forces** :

- **Visibilité privée massive** : Microsoft voit les signaux sur des milliards d’endpoints et tenants O365, CrowdStrike sur des millions d’endpoints EDR, Mandiant sur des milliers d’incidents IR par an.
- **Agilité de publication** : rapports techniques en quelques semaines, vs plusieurs mois pour les attributions gouvernementales.
- **Détail technique** : IoC, TTP, samples de malware, timeline. Les attributions gouvernementales sont souvent plus synthétiques.

**Limites** :

- **Pas d’accès au renseignement classifié** : HUMINT, SIGINT non-cyber. L’attribution stratégique (niveau 3) est plus difficile.
- **Risques commerciaux** : un vendor qui attribue à un État peut subir des conséquences (perte de clients, contentieux). Incite à la prudence.
- **Qualité variable** : Mandiant, CrowdStrike, Microsoft, Kaspersky, ESET, Unit 42 (Palo Alto), Recorded Future, Sekoia ont une réputation établie. D’autres vendors produisent des rapports moins fiables.

**Règle pratique** : croiser les attributions privées de plusieurs vendors sérieux. Si Mandiant, CrowdStrike et Microsoft concordent, la fiabilité est élevée.

## 24.7 Fil rouge — BLACKOUT Épisode 6

> **⚡ BLACKOUT — Épisode 6 : la matrice ACH complète**
> 
> Le CERT consolide l’attribution via une matrice ACH formelle. Les quatre hypothèses testées :
> 
> - **H1** : Sandworm (GRU Unit 74455) — pré-positionnement dans le contexte du conflit ukrainien.
> - **H2** : cluster chinois (Volt Typhoon ou similaire) — pré-positionnement stratégique.
> - **H3** : nouveau cluster étatique non attribué — acteur émergent, intention indéterminée.
> - **H4** : acteur non-étatique sophistiqué — cybercriminel de haut niveau.
> 
> **Matrice ACH (extrait)** :
> 
> |Évidence                                 |H1 Sandworm|H2 Chine |H3 Nouveau|H4 Non-étatique|
> |-----------------------------------------|:---------:|:-------:|:--------:|:-------------:|
> |Exploitation Ivanti CVE-2024-21887       |C          |**C**    |C         |C              |
> |LotL dominant, peu de malware custom     |I partiel  |**C**    |C         |C              |
> |DLL sideloading sur app de supervision   |C          |**C**    |C         |N              |
> |Beaconing HTTPS régulier                 |C          |I        |C         |C              |
> |Pas de malware custom Sandworm identifié |**I**      |C        |C         |C              |
> |Ciblage OT énergie                       |**C**      |C        |C         |I              |
> |Patience opérationnelle (42j sans action)|C          |**C**    |C         |I              |
> |Contexte géopolitique (conflit ukrainien)|**C**      |I partiel|C         |N              |
> |Absence totale de monétisation           |C          |C        |C         |**I**          |
> |Pas d’exfiltration massive               |C          |C        |C         |I              |
> |Sophistication technique observée        |C          |C        |C         |I              |
> 
> **Lecture** : C = cohérent ; I = incohérent ; I partiel = partiellement incohérent ; N = non applicable.
> 
> **Comptage des incohérences** :
> 
> - H1 Sandworm : 1 incohérence forte (pas de malware custom), 1 partielle (LotL atypique).
> - H2 Chine : 1 incohérence (beaconing régulier atypique Volt Typhoon), 1 partielle (contexte géopolitique).
> - H3 Nouveau cluster : 0 incohérence — mais hypothèse peu contrainte par défaut.
> - H4 Non-étatique : 4 incohérences fortes — **éliminée**.
> 
> **Conclusion d’attribution** :
> 
> - **H4 éliminée** : caractéristiques incompatibles avec un acteur non-étatique.
> - **H1 plausible** : confiance modérée. TTP, contexte, ciblage énergie s’alignent. Point faible : absence de malware custom Sandworm.
> - **H2 plausible** : confiance faible à modérée. TTP LotL s’alignent fortement, mais contexte géopolitique et beaconing régulier sont des décalages.
> - **H3 plausible** : ne peut être écartée. Confiance faible.
> 
> **Attribution provisoire** : « Pré-positionnement OT par acteur étatique — très probable (>80%). Attribution la plus probable : **Sandworm/GRU avec confiance modérée**. Hypothèse alternative Chine avec confiance faible à modérée. Hypothèse alternative cluster non identifié non écartée. »
> 
> **Indicateurs de révision identifiés** :
> 
> - Si un outil custom Sandworm est identifié → H1 renforcée.
> - Si un pattern d’infrastructure chinois documenté (routeurs SOHO compromis, C2 via IP résidentielles) est trouvé → H2 renforcée.
> - Si 2+ opérateurs européens confirment des TTP identiques via ISAC → probabilité d’attribution accrue par victimologie élargie.
> 
> Le CERT transmet le dossier à l’ANSSI pour coordination nationale et aux partenaires européens.

-----
