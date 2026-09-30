---
title: PARTIE VII — GÉOPOLITIQUE, ATTRIBUTION ET PROSPECTIVE
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
chapter: 7
chapters: 8
---

> **Ce que cette partie apprend.** Maîtriser la méthodologie d’attribution (niveaux, évidences, pièges), cartographier l’écosystème cyber offensif mondial, comprendre les enjeux stratégiques de la dissuasion cyber et de la responsabilité étatique, identifier les tendances structurelles 2024-2026, et construire une défense adaptée aux APT.
> 
> **Ce qu’elle ne couvre pas.** Le détail réglementaire juridique par juridiction (Annexe G), la conduite opérationnelle d’un SOC (cours SOC dédié), les outils techniques d’investigation (Ch.3, cours IR et Forensics).
> 
> **Ce que vous saurez faire après cette partie.** Conduire une matrice ACH sur un incident, évaluer la solidité d’une attribution publique, anticiper les évolutions de la menace à 12-24 mois, et structurer une défense APT-ready pour une organisation.

-----

## Chapitre 24 — Attribution : méthodes, limites et enjeux

### 24.1 Les trois niveaux d’attribution

L’**attribution** d’une cyberopération signifie différentes choses selon le niveau d’analyse. La confusion entre ces niveaux est la première source d’erreur analytique.

**Niveau 1 — Attribution technique** : relier une activité observée à un **intrusion set** identifié (APT29, Sandworm, Volt Typhoon, etc.). Fondée sur les TTP, l’infrastructure, le malware, la victimologie. Seuil de preuve : cohérence du faisceau technique avec un profil documenté. C’est l’attribution la plus accessible et la plus couramment produite par les vendors CTI.

**Niveau 2 — Attribution opérationnelle** : relier l’intrusion set à un **service ou une unité spécifique** (SVR russe, MSS Tianjin chinois, Lazarus/RGB nord-coréen, MOIS iranien). Nécessite des évidences supplémentaires — renseignement sur l’organisation sponsor, patterns d’horaires, artefacts linguistiques. Seuil de preuve : lien démontré entre l’intrusion set et une organisation spécifique.

**Niveau 3 — Attribution stratégique** : relier l’opération à un **État et une intention politique**. Qui a commandité ? Dans quel but stratégique ? Quels objectifs géopolitiques servis ? Seuil de preuve : compréhension contextuelle et renseignement non-technique (HUMINT, SIGINT stratégique, contexte diplomatique).

Les trois niveaux ont des **seuils de preuve croissants** et des **implications différentes**. Une attribution technique (« c’est APT29 ») est différente d’une attribution stratégique (« opération du SVR commanditée dans le cadre de la collecte de renseignement sur les positions européennes vis-à-vis de l’Ukraine »).

Les attributions publiques gouvernementales (indictments DOJ, advisories Five Eyes) atteignent souvent les trois niveaux. Les rapports CTI privés s’arrêtent souvent au niveau 1-2, laissant les considérations stratégiques en termes plus prudents.

### 24.2 Les évidences d’attribution

Plusieurs catégories d’évidences construisent l’attribution. Leur **convergence** renforce la confiance, leur divergence l’affaiblit.

**TTP / tradecraft** : la manière dont l’attaquant opère. Patterns de reconnaissance, choix de vecteurs, outils utilisés, techniques de persistence, de mouvement latéral, d’exfiltration. Les TTP sont plus durables que les IoC (Pyramide de la Douleur), et un tradecraft mature est une signature forte.

**Infrastructure** : domaines, IP, certificats, serveurs C2, patterns d’enregistrement. Un même attaquant réutilise souvent des patterns d’infrastructure (même registrar, même hébergeur, même structure de sous-domaines) — erreur d’OPSEC fréquente même chez les acteurs sophistiqués.

**Malware** : familles de malware, signatures techniques du code, patterns de développement (commentaires, noms de variables, structure), artefacts de compilation (paths PDB, fuseau horaire de la machine de compilation, langue du système).

**Victimologie** : qui est ciblé ? Si une campagne cible exclusivement des entreprises de semiconducteurs dans l’UE et les US, le profil des cibles est un signal — la Chine a un intérêt documenté, la Russie moins, la DPRK encore moins. La victimologie aligne sur les priorités stratégiques connues.

**Timing géopolitique** : l’attaque coïncide-t-elle avec un événement politique ? Une tentative d’ingérence électorale avant un scrutin, une campagne contre des institutions ukrainiennes lors d’une escalade militaire, un ciblage énergétique en hiver — le timing renforce certaines hypothèses.

**Renseignement HUMINT / SIGINT** : accessible seulement aux services étatiques. Les attributions publiques gouvernementales peuvent s’appuyer sur ce renseignement (sans le révéler). Les vendors privés n’y ont pas accès, d’où la différence de nature entre attribution publique gouvernementale et rapport CTI privé.

**Erreurs opérationnelles** : artefacts qui trahissent l’origine. Langue maternelle dans les commentaires de code, fuseau horaire de la machine de compilation, réutilisation d’infrastructure déjà attribuée, horaires de travail compatibles avec un fuseau horaire donné.

**Lien avec des indictments antérieurs** : si des opérateurs nommément identifiés par un indictment antérieur réapparaissent (mêmes emails, mêmes identités), l’attribution devient extrêmement solide.

### 24.3 Les pièges classiques de l’attribution

Plusieurs pièges classiques doivent être systématiquement écartés.

**False flags** : un attaquant plante délibérément des indices qui pointent vers un autre acteur. **Olympic Destroyer (2018)** est le cas d’école : Sandworm a inclus des fragments de code Lazarus documenté (DPRK), des infrastructures évoquant les APT chinoises, et des artefacts linguistiques trompeurs. L’analyse minutieuse par Kaspersky a identifié les faux marqueurs et consolidé l’attribution Sandworm. Leçon : un faisceau d’évidences apparemment convergent peut être fabriqué.

**Piggybacking sur une autre APT** : **Turla** a utilisé l’infrastructure d’APT34 (OilRig, Iran) pour ses propres opérations. Une victime qui voit une intrusion en provenance d’infrastructure connue comme iranienne peut être trompée sur l’origine réelle.

**Outils partagés** : **Cobalt Strike** est utilisé par presque tous les acteurs offensifs (APT étatiques, red teams légitimes, groupes ransomware). La seule présence de Cobalt Strike ne discrimine rien. Les infrastructures Let’s Encrypt, les VPS génériques, les services cloud légitimes sont utilisés par tous.

**Infrastructure louée / partagée** : les VPS sont loués, les domaines enregistrés via des registrars communs. Une IP qui a hébergé une opération APT29 il y a deux ans peut héberger aujourd’hui un site e-commerce légitime ou une opération totalement distincte.

**Biais géopolitiques** : attribuer à la Russie « par défaut » parce que le contexte le rend plausible est une erreur méthodologique. La discipline ACH exige de tester **plusieurs hypothèses** contre les mêmes évidences.

**Biais de confirmation** : une fois une hypothèse formulée tôt, l’investigateur tend à chercher des preuves qui la confirment et à ignorer celles qui la contredisent. Parade : formuler explicitement l’hypothèse, puis **chercher activement** les évidences qui l’invalideraient.

**Effet de signature reconnue** : reconnaître un pattern connu produit une sensation de certitude (« c’est Volt Typhoon, je le sens »). Cette intuition est utile mais doit être formalisée et testée contre les alternatives.

### 24.4 Les niveaux de confiance et le vocabulaire calibré

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

### 24.5 L’attribution publique par les gouvernements

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

### 24.6 Les attributions privées : vendors CTI

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

### 24.7 Fil rouge — BLACKOUT Épisode 6

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

## Chapitre 25 — L’écosystème cyber offensif mondial

### 25.1 Panorama quantitatif

Plusieurs centaines de groupes APT sont suivis publiquement. Ordres de grandeur (2026) :

- **MITRE ATT&CK Groups** : ~160 groupes documentés publiquement.
- **Malpedia** (Fraunhofer FKIE) : plusieurs centaines de familles de malware attribuées.
- **CrowdStrike** : 230+ acteurs nommés suivis.
- **Mandiant** : 300+ intrusion sets dans son périmètre interne.
- **Microsoft Threat Intelligence** : 150+ threat actors nommés publiquement.

Ces chiffres croissent chaque année. La concentration d’activité reste sur un noyau restreint d’acteurs de premier plan — la **loi de Pareto** s’applique largement : 20% des groupes produisent 80% de l’activité documentée.

### 25.2 La prolifération des capacités

La **prolifération des capacités cyber offensives** est la tendance structurelle la plus préoccupante. Plusieurs dynamiques y contribuent.

**Frameworks C2 accessibles** :

- **Cobalt Strike** : outil commercial de pentest, largement « cracké ». Utilisé par la grande majorité des APT et groupes ransomware depuis 2018-2020.
- **Brute Ratel C4** : concurrent commercial, également cracké.
- **Sliver** (BishopFox, open source) : framework C2 open source, massivement adopté.
- **Havoc** (open source) : framework récent en progression.
- **Mythic** (open source) : plateforme C2 modulaire.
- **Metasploit** : pentest framework classique.

Ces outils fournissent des capacités sophistiquées à des acteurs qui n’auraient pas les ressources pour les développer. Les TTP autrefois signature d’APT étatique deviennent accessibles à des acteurs moindres.

**Marché de la surveillance privée (PSO)** : NSO, Intellexa, Candiru, Paragon — traités au Ch.15 et Ch.18. Des **dizaines d’États** peuvent désormais **acheter** ces capacités auprès de fournisseurs commerciaux.

**Vulnerability brokers** : marchés légaux (Zerodium, Crowdfense) et gris. Prix d’un 0-day iOS full chain : plusieurs millions de dollars. Permettent à des acteurs de niveau intermédiaire d’acquérir des capacités.

**Leaks d’outils étatiques** :

- **Shadow Brokers** (2016-2017) : outils NSA (EternalBlue utilisé dans WannaCry/NotPetya, DoublePulsar).
- **Vault 7** (2017) : outils CIA via WikiLeaks.
- **Leak i-Soon** (février 2024) : écosystème contractor chinois.
- **ContiLeaks** (2022) : opérations internes d’un groupe ransomware majeur.

Ces leaks arment des acteurs moindres avec des capacités étatiques.

**Initial Access Brokers (IAB)** : vendent des accès obtenus sur des forums dark web. Un acteur qui ne sait pas compromettre peut acheter un accès pour quelques centaines ou milliers de dollars. Fragmentation de la chaîne d’attaque.

**IA offensive** : usage de LLM et d’IA générative pour améliorer le phishing, générer du code, détecter des vulnérabilités, amplifier les campagnes d’influence. Impact croissant (voir Ch.27).

### 25.3 Le modèle contractor comme industrie offensive

Le modèle des **contractors civils** mandatés pour des opérations cyber étatiques est une dimension structurelle de l’écosystème contemporain.

**Chine — i-Soon et ses pairs** : le leak i-Soon (Ch.8) a documenté un écosystème vaste. D’autres contractors chinois existent. Entreprise privée qui vend des services cyber (outils, opérations, surveillance) à des clients étatiques multiples (MSS, PLA, polices provinciales).

**Russie — écosystème flou entre services et prestataires** : moins formalisé qu’en Chine, mais plusieurs entités sont à la frontière (KillNet, NoName057(16) côté russe, avec niveaux de coordination variables avec les services).

**Israël — secteur commercial structurellement lié à l’appareil de défense** : pipeline Unité 8200 → startups → surveillance commerciale (Ch.18). NSO, Intellexa, Candiru, Paragon régulés par le ministère israélien de la Défense.

**Occident — contractors de défense classiques étendus au cyber** : Raytheon, Lockheed Martin, BAE Systems, Thales, Airbus et d’autres ont des divisions cyber. Opèrent généralement dans des cadres juridiques plus formalisés (marchés publics, supervision parlementaire).

**États émergents** : plusieurs pays développent des capacités via acquisition de services privés (achat de spywares commerciaux), recrutement d’opérateurs formés ailleurs, coopération avec des contractors étrangers. Le seuil d’entrée pour un État désireux d’acquérir des capacités cyber est plus bas qu’il y a 10 ans.

**Implications analytiques** : l’attribution devient plus difficile quand plusieurs contractors travaillent pour un même client ou qu’un contractor travaille pour plusieurs clients. Les frontières « opération étatique » / « opération commerciale au service de l’État » s’estompent.

### 25.4 Lecture comparative des doctrines par bloc

Synthèse doctrinale consolidée.

|Acteur                        |Doctrine centrale                |Tradecraft                            |Sophistication     |Tolérance au bruit|
|------------------------------|---------------------------------|--------------------------------------|-------------------|------------------|
|**Russie — SVR/APT29**        |Espionnage stratégique, furtivité|Supply chain, abus cloud, OAuth       |Très élevée        |Très faible       |
|**Russie — GRU/Sandworm**     |Sabotage, destructif ouvert      |Wipers, OT custom                     |Élevée             |Élevée            |
|**Russie — GRU/APT28**        |Espionnage militaire + influence |Spear-phishing, exploits              |Élevée             |Moyenne-élevée    |
|**Russie — FSB/Turla**        |Espionnage long terme            |Rootkits, piggybacking                |Exceptionnelle     |Très faible       |
|**Chine — MSS**               |Espionnage massif, patience      |Supply chain, LotL, volume            |Élevée, croissante |Faible            |
|**Chine — Volt Typhoon**      |Pré-positionnement               |LotL exclusif, SOHO botnet            |Très élevée        |Extrême-faible    |
|**DPRK — Lazarus/RGB**        |Financement régime               |Cybervol, social engineering          |Élevée, pragmatique|Moyenne           |
|**Iran — MOIS**               |Espionnage régional              |Webshells, DNS tunneling              |Moyenne-élevée     |Moyenne           |
|**Iran — IRGC (APT35)**       |Surveillance ciblée              |Social engineering extrême            |Élevée (SE)        |Faible            |
|**Iran — Agrius**             |Destructif représailles          |Wipers, fausses bannières             |Moyenne            |Moyenne-élevée    |
|**US — USCYBERCOM/NSA**       |Defend forward                   |Spectre large, capacités avancées     |Très élevée        |Variable          |
|**UK — NCF/GCHQ**             |Disruption by design             |Ciblage précis, coordination Five Eyes|Très élevée        |Faible            |
|**Israël — Unité 8200/Mossad**|Préemption                       |Ciblage précis, HUMINT intégré        |Très élevée        |Variable          |

### 25.5 L’écosystème comme instrument diplomatique

Les cyberopérations sont **intégrées dans la diplomatie** des États.

**Le cyber comme signal** : une cyberopération peut signaler une position politique (Shamoon comme représailles iraniennes pour Stuxnet, Sandworm comme démonstration de capacité hybride russe, Volt Typhoon comme dissuasion chinoise liée à Taïwan). Comprendre le signal est aussi important que comprendre l’effet technique.

**Le cyber comme monnaie d’échange** : les attributions, sanctions, indictments peuvent être levés ou maintenus selon l’évolution des relations. L’accord Xi-Obama 2015 sur l’espionnage économique chinois a produit un effet temporaire observable dans la baisse des opérations APT chinoises contre les entreprises US pendant quelques années.

**Le cyber comme test de résolution** : les acteurs testent la volonté des défenseurs de répondre. Une escalade cyber qui ne provoque pas de réponse significative encourage de nouvelles escalades. Une réponse ferme peut décourager.

**Le cyber comme déstabilisation en deçà du seuil du conflit armé** : la zone grise permet des opérations qui, dans le monde physique, appelleraient une réponse militaire — mais qui restent « tolérées » au cyber. Cette asymétrie favorise les États agresseurs.

Pour l’analyste, ces dimensions diplomatiques et stratégiques sont indissociables du technique. Un rapport CTI qui se limite aux IoC et aux TTP, sans considération du contexte diplomatique, donne une vision incomplète.

-----

## Chapitre 26 — Dissuasion, normes et responsabilité étatique

> **Note sur ce chapitre.** Ce chapitre traite les **enjeux stratégiques et analytiques** du droit international appliqué au cyber, des normes négociées, et de la responsabilité étatique. Le **détail réglementaire** (textes, articles, agences par juridiction) est consolidé dans l’**Annexe G**. L’objectif ici est de saisir les enjeux, pas de cataloguer les textes.

### 26.1 Peut-on dissuader dans le cyberespace ?

La **dissuasion** est un concept stratégique hérité du nucléaire : convaincre l’adversaire que les coûts d’une action dépasseraient les bénéfices. Son application au cyber fait l’objet de débats intenses.

**Difficultés structurelles de la dissuasion cyber**.

**L’attribution est lente et imparfaite** : la dissuasion nucléaire repose sur une certitude d’attribution (un missile vient de tel pays). En cyber, l’attribution prend des semaines à des années, avec des niveaux de confiance variables. Un adversaire peut agir sans savoir exactement si et quand il sera attribué.

**La gradation des représailles est difficile** : dans le nucléaire, la doctrine de la « mutuelle destruction assurée » était claire. En cyber, quels seuils déclenchent quelle réponse ? Une cyberattaque sur une centrale peut-elle justifier une riposte conventionnelle ? Une réponse cyber équivalente ? Une sanction économique ? Les doctrines varient et sont souvent volontairement ambiguës.

**Le déni plausible** : beaucoup de cyberopérations sont conduites de manière à offrir un déni plausible au sponsor. La tolérance tacite du cybercrime russophone, l’usage de contractors chinois, les fausses bannières iraniennes — autant de techniques qui diluent la responsabilité étatique.

**L’asymétrie** : un État comme la DPRK, sans infrastructure vulnérable équivalente, n’est pas dissuadable par la menace de représailles cyber — il n’a rien à perdre en cyber. Sa motivation (financer le régime) reste suffisante malgré sanctions diplomatiques.

**Le seuil bas** : contrairement au nucléaire où le coût initial est extrême, le cyber est quotidien. La dissuasion efficace suppose que chaque action soit individuellement coûteuse — difficile à calibrer quand le volume d’opérations est élevé.

**Éléments de dissuasion qui semblent fonctionner (au moins partiellement)** :

**Capacité démontrée de détection et d’attribution** : les advisories Five Eyes, les indictments DOJ, les rapports CTI publics démontrent que les opérations seront découvertes. Cette démonstration impose un coût réputationnel.

**Sanctions cumulées** : les sanctions OFAC et UE, accumulées dans le temps, produisent un coût financier réel sur les individus et entités ciblés.

**Démantèlements d’infrastructure** : les opérations Medusa (Snake), KV Botnet (Volt Typhoon), Raptor Train (Flax Typhoon), LockBit (Cronos) imposent un coût opérationnel — remplacer une infrastructure démantelée demande du temps et des ressources.

**Coordination alliée** : l’attribution coordonnée Five Eyes + alliés crée un coût diplomatique plus élevé qu’une attribution isolée.

**Bilan** : la dissuasion cyber est **partielle**. Elle n’empêche pas les opérations, mais elle en augmente le coût et peut modérer les ambitions les plus destructives. Les grandes puissances cyber n’ont jamais franchi publiquement certains seuils (pas de cyber-attaques destructives sur les infrastructures critiques US par la Chine, pas de cyber-attaques destructives sur les infrastructures critiques russes par les US) — ce qui suggère une forme de dissuasion fonctionnelle sur les seuils les plus élevés.

### 26.2 Droit international appliqué au cyber : débats fondamentaux

Le droit international n’a pas été conçu pour le cyberespace. Son application fait l’objet de débats qui reflètent des visions stratégiques divergentes.

**Principes applicables (consensus large)** :

- **Souveraineté** : un État ne peut pas mener d’opérations dans le territoire (y compris les réseaux) d’un autre État sans son consentement.
- **Non-intervention** : un État ne peut pas intervenir dans les affaires intérieures d’un autre État.
- **Proportionnalité** : les réponses doivent être proportionnées à l’agression.
- **Interdiction du recours à la force** (article 2.4 Charte ONU) : quelle est la frontière entre « cyberopération » et « recours à la force » ?

**Le processus de Tallinn** (Manuel 1.0 en 2013, 2.0 en 2017) : travail d’un groupe d’experts coordonné par le **CCDCOE OTAN** (Tallinn). Propose une interprétation du droit international appliqué au cyber. **Non contraignant juridiquement** mais référence académique majeure. Position dominante : le droit international s’applique au cyberespace, les États sont responsables des opérations qu’ils conduisent ou tolèrent.

**Négociations ONU — GGE et OEWG** : depuis 2004, l’ONU négocie des normes de comportement responsable. Le **GGE** (expert restreint) a produit des rapports consensuels (2013, 2015). L’**OEWG** (tous États membres) est plus divisif politiquement.

**Positions divergentes structurantes** :

- **Bloc occidental** (US, UE, Five Eyes, Japon, Corée du Sud) : les normes existantes s’appliquent au cyber sans nouveau traité. Focus sur l’**application** et les **comportements responsables**. Défense de la liberté d’Internet et du **multistakeholderisme** (gouvernements + secteur privé + société civile + communauté technique).
- **Bloc Russie-Chine** : un nouveau traité international est nécessaire. Concept de « **sécurité de l’information** » qui inclut non seulement la cybersécurité au sens technique mais aussi le **contrôle du contenu** — contrôle de l’Internet, restriction de l’information jugée déstabilisatrice. Défense du **multilatéralisme onusien** strict (gouvernements seuls).

Ces positions reflètent des **visions incompatibles** de la gouvernance numérique. Le conflit n’est pas purement technique ou juridique — il est fondamentalement politique. La perspective d’un traité universel contraignant sur le cyber reste éloignée.

### 26.3 Attributions publiques et sanctions : la logique stratégique

Les attributions publiques gouvernementales et les sanctions associées constituent l’instrument principal de réponse des démocraties occidentales aux cybermenaces étatiques. Leur logique stratégique mérite d’être analysée.

**La logique de naming and shaming** : rendre publique l’attribution impose un coût réputationnel à l’État commanditaire. Ce coût est d’autant plus élevé que l’attribution est coordonnée internationalement (Five Eyes + alliés) et argumentée techniquement.

**La logique de signalement** : une attribution publique signale la **capacité de détection** de la victime. Message implicite : « nous vous voyons, vos opérations ne sont pas invisibles ». Cet effet peut décourager certaines opérations futures par le simple fait de la démonstration.

**La logique du coût cumulé** : les sanctions OFAC, les Entity List, les indictments DOJ n’empêchent pas individuellement une opération, mais leur **accumulation dans le temps** produit un coût réel. Un opérateur nommément identifié par un indictment ne peut plus voyager dans la plupart des pays, ses avoirs peuvent être gelés, son identité est publique.

**La logique de l’alliance** : les attributions coordonnées entre alliés (Five Eyes, UE, OTAN) renforcent la cohérence des démocraties face aux menaces étatiques. Elles traduisent une solidarité stratégique au-delà de la simple déclaration.

**Les limites** :

- **Pas d’effet sur les agresseurs déterminés** : la DPRK continue de voler, la Russie continue ses opérations, la Chine maintient son pré-positionnement. Les sanctions imposent un coût sans changer fondamentalement les incitations.
- **Asymétrie démocratique** : les démocraties attribuent publiquement ; les autocraties rarement. Cette asymétrie favorise les démocraties dans le récit public mais n’équilibre pas nécessairement les rapports de force opérationnels.
- **Risque de dévaluation** : si les attributions publiques deviennent trop fréquentes, leur poids individuel diminue. La discipline consiste à attribuer publiquement avec parcimonie, pour les cas les plus significatifs.

### 26.4 Responsabilité étatique dans le cyberespace

La question de la **responsabilité étatique** — à quoi un État est-il tenu, pour quelles actions de quels acteurs ? — est centrale.

**Le standard classique du droit international** : un État est responsable des actions qu’il conduit lui-même **et** des actions de tiers qu’il contrôle effectivement (« effective control »). Appliqué au cyber, cela signifie qu’un État est responsable :

- Des cyberopérations conduites par ses services étatiques directs.
- Des cyberopérations conduites par des contractors sous son contrôle.
- Possiblement des cyberopérations conduites par des acteurs qu’il tolère ou soutient sans s’opposer.

**Le seuil de l’effective control** : souvent difficile à démontrer. Un contractor chinois qui conduit une opération pour le MSS est-il sous effective control de l’État ? Un groupe ransomware russophone toléré par le FSB est-il sous effective control ? Les opérations de pré-positionnement attribuées à la Chine correspondent-elles à une décision politique de haut niveau ou à une initiative d’un bureau régional MSS ?

**Positions divergentes** :

- **Position occidentale** (tend à élargir la responsabilité) : un État est responsable non seulement de ce qu’il contrôle mais aussi de ce qu’il aurait pu et dû empêcher. La tolérance d’opérations depuis son territoire peut engager sa responsabilité.
- **Position russe/chinoise** (tend à restreindre) : seules les opérations prouvées comme directement conduites par l’État engagent sa responsabilité. Les acteurs non-étatiques, même tolérés, ne peuvent pas être imputés à l’État.

Ces divergences juridiques ont des implications pratiques : un ransomware russophone peut-il justifier une réponse étatique contre la Russie ? Un groupe cyber chinois sous forte présomption MSS peut-il justifier des sanctions contre des officiels chinois ?

**L’évolution des pratiques** : les attributions publiques occidentales récentes (indictments, sanctions) désignent de plus en plus les **institutions étatiques** et les **officiels nommément identifiés**, pas seulement les opérateurs techniques. Cette tendance élargit la responsabilité étatique dans la pratique, indépendamment des débats juridiques théoriques.

### 26.5 L’OTAN et le seuil de l’article 5

L’**OTAN** a reconnu le cyberespace comme **5ème domaine d’opérations** au sommet de Varsovie (2016). Cette reconnaissance a des implications majeures pour la dissuasion.

**Principe** : le **Treaty de Washington (1949), Article 5** stipule qu’une attaque armée contre un membre de l’OTAN est considérée comme une attaque contre tous. La reconnaissance du cyber comme 5ème domaine signifie qu’**une cyberattaque significative peut en théorie déclencher l’article 5**.

**En pratique, le seuil n’a jamais été formellement défini**. L’OTAN a annoncé que le cas serait évalué au cas par cas. Plusieurs conséquences :

**Ambiguïté stratégique** : le seuil non-défini est **délibéré**. L’ambiguïté maintient l’incertitude chez l’adversaire — il ne sait pas ce qui déclenchera l’article 5, ce qui l’incite à la prudence.

**Cas de test non-déclenchés** : NotPetya (2017), qui a causé des dommages massifs à des pays membres (Royaume-Uni notamment), n’a pas déclenché l’article 5. SolarWinds (2020) non plus. Le ciblage OT en Ukraine n’a pas impliqué l’article 5 (l’Ukraine n’est pas membre OTAN).

**Concept de « seuil d’attaque armée cyber »** : débattu dans les travaux OTAN et académiques. Éléments généralement considérés : **mort ou blessure humaine**, **destruction physique massive**, **impact économique à l’échelle d’une attaque cinétique**, **atteinte à la souveraineté**. Un blackout de plusieurs jours affectant des millions de personnes pourrait potentiellement atteindre ce seuil. Une exfiltration de documents classifiés, aussi significative soit-elle, ne l’atteindrait probablement pas.

**Pratique récente** : l’OTAN a développé des capacités de défense cyber collective (NATO Cyber Operations Centre, **CCDCOE** à Tallinn pour la doctrine, **exercices Locked Shields**). Une structure mature, sans pour autant s’engager mécaniquement dans la dissuasion automatique.

### 26.6 Le cadre français : doctrine LIO/LID/L2I

La France a publiquement formalisé sa **doctrine cyber** en 2019 via la revue stratégique de cyberdéfense, structurée autour de trois piliers.

**LID** — **Lutte Informatique Défensive** : la protection et la défense des systèmes d’information de l’État et des OIV. Conduite principalement par l’**ANSSI**.

**LIO** — **Lutte Informatique Offensive** : la conduite d’opérations cyber offensives pour le compte de l’État. Conduite principalement par le **COMCYBER** (Commandement de la cyberdéfense, ministère des Armées). La France s’est réservé le droit de mener des opérations offensives en réponse à une agression. La doctrine publique mentionne l’encadrement par l’autorité politique et le respect du droit international et humanitaire.

**L2I** — **Lutte Informatique d’Influence** : la contre-ingérence dans l’espace informationnel, face aux opérations de désinformation étatiques. Ce volet, plus récent, reflète la prise de conscience de la dimension informationnelle des conflits contemporains.

Le détail institutionnel (structures ANSSI, COMCYBER, DGSE, DGSI, C4) et réglementaire (OIV, NIS 2 en France) est consolidé dans l’**Annexe G**. Ce qui importe ici est la **cohérence doctrinale** : la France a explicitement assumé un spectre complet de capacités cyber (défensives, offensives, informationnelles), avec une articulation avec l’appareil de sécurité nationale globale.

### 26.7 Le cadre européen : NIS 2, Cyber Solidarity Act, ENISA

Au niveau européen, la cybersécurité s’est massivement structurée ces dernières années. Synthèse stratégique (détail en Annexe G).

**ENISA** (European Union Agency for Cybersecurity) : coordination cybersécurité entre États membres, publication de rapports (Threat Landscape annuel), exercices (Cyber Europe).

**NIS 2** (Directive 2022/2555, entrée en application 2024) : extension massive du périmètre par rapport à NIS 1. Environnement **essentiel/important** dans 18 secteurs. Obligations renforcées : mesures techniques et organisationnelles, notification d’incidents, gouvernance cybersécurité au niveau direction, évaluations de risques de la supply chain, sanctions administratives pouvant atteindre 10 M€ ou 2% du chiffre d’affaires mondial.

**EU Cyber Solidarity Act** (2024) : création d’un réseau européen de **SOC** (Security Operations Centers) pour partager la détection et la réponse, mécanisme de **réserve cyber** européenne activable en crise.

**Cyber Resilience Act** (adoption 2024) : obligations de cybersécurité pour les produits connectés (IoT, logiciels), responsabilité des fabricants.

**EU Cyber Sanctions Regime** (depuis 2019) : cadre permettant des sanctions ciblées (gel des avoirs, interdictions de voyager) contre des personnes et entités impliquées dans des cyberattaques.

### 26.8 Responsabilité des États sur les opérations de leurs alliés ou proxies

Une question émergente : la responsabilité des États pour les opérations conduites par leurs alliés ou proxies.

**Cas concrets** :

- **Volontaires internationaux IT Army of Ukraine** : conduits sous coordination étatique ukrainienne publique. Quelle responsabilité ukrainienne pour des actes illégaux commis par des volontaires depuis des pays tiers ? Question juridique ouverte.
- **Hacktivistes pro-russes (KillNet, NoName057)** : ciblés par des sanctions UE en 2023-2024. La Russie est-elle responsable des actes d’hacktivistes qu’elle tolère et probablement soutient ? Le débat rejoint celui de la responsabilité étatique classique.
- **Opérations offensives conduites avec l’aide d’alliés** : USCYBERCOM hunt forward en Ukraine. Les opérations américaines conduites sur le sol ukrainien engagent-elles la responsabilité américaine, ukrainienne, ou les deux ?

**Tendance émergente** : les démocraties occidentales cherchent à **formaliser** le cadre d’emploi des capacités cyber pour clarifier les responsabilités. L’ambiguïté stratégique a des avantages (flexibilité) mais aussi des coûts (imprévisibilité, risque d’escalade non désirée).

### 26.9 Pall Mall Process et régulation des PSO

Le **Pall Mall Process** est l’initiative internationale de régulation des capacités cyber offensives commerciales (spywares, outils offensifs). Lancé à Londres en février 2024, conjointement par le Royaume-Uni et la France.

**Objectif** : établir un cadre international pour la régulation du marché des **PSO** (Private Sector Offensive Actors) — NSO, Intellexa, Candiru, Paragon et leurs concurrents. Préoccupation centrale : l’usage abusif de ces outils contre des journalistes, dissidents, opposants politiques, défenseurs des droits humains.

**Signataires** : plus de 40 États à la déclaration initiale de Londres (février 2024), rejoints par d’autres lors des rounds ultérieurs. Entreprises cosignataires incluent Apple, Google, Meta, Microsoft. ONG de droits humains également partie prenante.

**Principes affirmés** :

- Usage des capacités cyber commerciales dans le respect du droit international et des droits humains.
- Responsabilité des États sur les usages de ces capacités qu’ils acquièrent.
- Transparence relative sur les acquisitions étatiques.
- Sanctions contre les entreprises documentées pour des usages abusifs.

**Limites** : initiative non-contraignante juridiquement. Plusieurs États majeurs (notamment des clients majeurs de NSO et ses pairs) ne sont pas signataires. Effet dépend de la mise en œuvre nationale et de la coordination internationale.

**Importance stratégique** : malgré ses limites, le Pall Mall Process est un premier jalon international sur un marché qui a opéré jusque-là sans régulation globale. Son développement dans les années à venir sera un indicateur de la capacité de la communauté internationale à gouverner cet espace.

-----

## Chapitre 27 — Tendances 2024-2026 et signaux d’anticipation

### 27.1 Exploitation massive des appliances edge

La tendance n°1 du paysage cyber contemporain : l’**exploitation des appliances edge exposées sur Internet**. VPN, firewalls, passerelles mail, appliances de sécurité elles-mêmes sont devenues le vecteur d’entrée privilégié des APT sophistiquées.

**Vagues notables 2023-2026** :

- **Ivanti Connect Secure** : CVE-2023-46805, CVE-2024-21887, CVE-2024-21888 exploitées par plusieurs acteurs (Volt Typhoon, APT40, APT31, clusters non identifiés). Vague massive début 2024.
- **Fortinet FortiOS** : multiples CVE 2022-2024 exploitées par APT40 et autres.
- **Citrix ADC/NetScaler** : CVE-2023-4966 (« Citrix Bleed »), CVE-2023-3519 exploitées par APT29, APT40, acteurs ransomware.
- **Barracuda Email Security Gateway** : CVE-2023-2868 exploitée par UNC4841 (Chine) pendant 8 mois avant découverte.
- **Palo Alto GlobalProtect** : CVE-2024-3400 exploitée mi-2024.
- **Cisco IOS XE** : CVE-2023-20198 exploitation massive fin 2023.

**Pourquoi cette concentration** :

- **Pas d’EDR sur les appliances** : les appliances réseau ne peuvent pas faire tourner d’agents de détection endpoint. La visibilité est limitée aux logs (parfois insuffisants).
- **Exposition Internet par construction** : une VPN gateway doit être accessible depuis Internet, donc exposée aux scans massifs des attaquants.
- **Credentials privilégiés en aval** : compromettre une appliance de sécurité donne souvent un accès privilégié au réseau interne (VPN → accès réseau, firewall → capacité de manipulation des flux, passerelle mail → accès aux communications).
- **Patching complexe** : les appliances sont souvent en production continue, leur patching est planifié et parfois retardé.
- **Vulnérabilités nombreuses** : les appliances de sécurité ont des vulnérabilités comme les autres logiciels — le paradoxe consiste à ce que les outils de défense deviennent des vecteurs d’attaque.

**Défense** : surveillance renforcée des appliances (logs exhaustifs, SIEM intégré), patching d’urgence (suivre KEV CISA), durcissement des configurations (désactiver les composants non-nécessaires), monitoring réseau entourant les appliances.

### 27.2 Ciblage de l’identité cloud

L’**identité cloud** est devenue le nouveau périmètre. Les APT ciblent massivement Azure AD/Entra ID, les tokens SAML/OAuth, les mécanismes MFA.

**Tactiques dominantes** :

- **Password spraying sur Azure AD** : volume massif, taux de succès faible par tentative mais cumul efficace. APT33 (Iran) et APT29 (Russie) en font un usage systématique.
- **Abus OAuth** : création d’applications OAuth malveillantes ou détournement d’applications existantes avec des permissions Graph API excessives. Accès persistant sans mot de passe, contourne la MFA. Signature APT29.
- **Vol de tokens (pass-the-cookie, pass-the-token)** : réutilisation de sessions authentifiées volées via infostealers ou AitM phishing. Contourne la MFA.
- **AitM phishing avec Evilginx et équivalents** : proxy malveillant qui intercepte les credentials ET les cookies de session. Contourne la MFA. Utilisé massivement par acteurs étatiques et cybercriminels.
- **GoldenSAML** : forgeage de tokens SAML via compromission d’ADFS. Technique pivot de SolarWinds, toujours utilisée.
- **MFA fatigue** : bombardement de notifications push pour inciter la victime à en accepter une par lassitude. Technique de base mais efficace.
- **Compromission de comptes de service** : les comptes de service (applications, systèmes) ont souvent des permissions larges et des mécanismes d’authentification plus faibles (clés API, secrets partagés).

**Vulnérabilité structurelle** : une compromission cloud bien installée peut survivre à la réinstallation complète de tous les endpoints. La remédiation nécessite de révoquer les tokens, recréer les applications OAuth, auditer les permissions, changer les secrets — opérations complexes et souvent incomplètes.

**Défense** :

- **MFA résistant au phishing** : FIDO2 / WebAuthn / clés hardware (YubiKey). Ne tombe pas à l’AitM.
- **Conditional Access** : règles basées sur le contexte (device, location, risk signals).
- **Monitoring OAuth et consents** : détecter les applications OAuth avec consent admin, les permissions Graph API excessives, les anomalies d’authentification.
- **Privileged Identity Management (PIM)** : activation just-in-time des rôles privilégiés, pas de standing admin.
- **Identity threat detection** : outils dédiés (Microsoft Defender for Identity, CrowdStrike Identity Threat Protection, Okta ITDR).

### 27.3 Convergence crime-État

La **convergence entre cybercrime et action étatique** est une tendance structurelle déjà largement évoquée dans les parties précédentes.

**Manifestations principales** :

- **APT41** (Chine) : double mission espionnage/cybercrime personnel assumée.
- **Ransomware russophone sous tolérance tacite** : LockBit, BlackBasta, Play, Royal, ALPHV, Cl0p.
- **DPRK/Lazarus** : méthode criminelle (cybervol crypto), finalité étatique (financement régime).
- **Infostealers et IAB** : cybercriminels qui fournissent involontairement des accès aux APT étatiques via la revente sur marchés dark web.
- **Hacktivisme instrumentalisé** : KillNet, NoName057(16), IT Army of Ukraine.

**Implications** :

- **Attribution plus complexe** : face à une compromission, distinguer si l’acteur est purement criminel, purement étatique, ou entre les deux est souvent difficile.
- **Réponse adaptée** : les mesures qui fonctionnent contre le cybercrime (démantèlements d’infrastructure, sanctions économiques) sont moins efficaces contre les APT étatiques. Les mesures diplomatiques qui fonctionnent contre les APT sont sans effet sur les cybercriminels. La zone grise nécessite des approches mixtes.
- **Tendance à la professionnalisation** : le cybercrime devient plus sophistiqué sous l’influence des TTP étatiques ; les APT empruntent les techniques criminelles (infostealers, IAB) pour l’efficacité.

**Trajectoire 2024-2026** : la convergence va probablement s’approfondir. Les distinctions « pur crime » vs « pur État » deviendront de moins en moins nettes.

### 27.4 LotL comme standard

Le **Living off the Land** est passé d’une technique avancée à un **standard** des APT sophistiquées.

**Volt Typhoon** a démontré qu’une opération étatique sophistiquée de pré-positionnement peut être conduite **sans aucun malware custom**. Son modèle se diffuse : de plus en plus d’acteurs adoptent des approches LotL-heavy pour maximiser la furtivité.

**Implications pour la défense** :

- Les signatures EDR classiques (hash de fichiers, strings de malware) détectent moins.
- La détection doit être **comportementale** : patterns d’usage des LOLBins, contextes d’exécution, chaînes de processus.
- Les baselines comportementales deviennent cruciales — identifier qu’un `ntdsutil` exécuté par un compte admin depuis un serveur non-DC est anormal nécessite de savoir ce qui est normal.
- Le **threat hunting proactif** prend de l’importance sur la détection automatique passive.

**Outils défensifs adaptés** : EDR modernes qui surveillent les **chaînes de processus** et les **patterns comportementaux** (Microsoft Defender for Endpoint, CrowdStrike Falcon, SentinelOne, Carbon Black, Palo Alto Cortex XDR) plutôt que les signatures seules. SIEM avec règles de détection comportementales.

### 27.5 IA offensive : phishing, deepfakes, aide au développement

L’**IA générative** (LLM et génération multimédia) entre dans l’arsenal offensif. Impact croissant, encore émergent.

**Phishing amélioré par LLM** : les emails de phishing sont rédigés dans un langage natif et contextuel parfait, sans les erreurs linguistiques caractéristiques des campagnes non-natives. L’avantage historique des anglophones sur les campagnes de phishing ciblant les entreprises anglophones (vs attaquants non-anglophones avec erreurs) est en train de disparaître. APT iraniens, chinois, russes produisent désormais des emails de phishing indiscernables linguistiquement de correspondants légitimes.

**Deepfakes vocaux** : impersonation vocale de dirigeants pour des attaques BEC (Business Email Compromise) au téléphone. Cas documentés : un employé finance convaincu par téléphone que le CFO lui demande un virement urgent, pour découvrir plus tard qu’il s’agissait d’une voix synthétique. Les deepfakes audio sont techniquement plus accessibles que les deepfakes vidéo et leur utilisation criminelle s’industrialise.

**Deepfakes vidéo** : cas documentés en Asie (vidéoconférences truquées où plusieurs participants étaient des deepfakes d’employés légitimes, aboutissant à des transferts frauduleux de dizaines de millions). Technique coûteuse mais accessible aux acteurs sophistiqués.

**Aide au développement de malware** : les LLM peuvent aider à générer du code offensif — scripts d’exploitation, évasions EDR, obfuscations. Les garde-fous des LLM commerciaux (OpenAI, Anthropic, Google) filtrent beaucoup de demandes manifestement malveillantes, mais les LLM open source ou partiellement contournés offrent moins de résistance. Impact : accélération du développement par les acteurs sophistiqués, accessibilité accrue pour les acteurs moyens.

**Reconnaissance et profilage assistés** : LLM utilisés pour agréger des données OSINT sur des cibles, identifier des vulnérabilités humaines (points d’approche social engineering), générer des leurres personnalisés.

**État actuel (2026)** : l’IA offensive augmente la **productivité** des attaquants mais n’a pas encore produit de rupture capacitaire qualitative. Les opérations restent conduites par des humains avec outillage IA, pas entièrement automatisées. La trajectoire à moyen terme (2027-2030) est incertaine — l’automatisation croissante des attaques via agents IA est une menace anticipée mais pas encore massivement observée.

### 27.6 Pré-positionnement dans les infras critiques : la menace structurelle

Le **pré-positionnement** (Ch.22) est probablement **la menace structurelle qui définira la prochaine décennie**. Plusieurs dynamiques l’amplifient :

**Volt Typhoon comme modèle** : démontre qu’un pré-positionnement prolongé sans détection est possible. Ce modèle va être répliqué par d’autres acteurs.

**Extension géographique** : au-delà des US, l’Europe est désormais une cible crédible de pré-positionnement (par la Russie et la Chine). L’Asie-Pacifique également (par la Chine).

**Dilemmes de réponse non résolus** : éradiquer vs surveiller, communiquer publiquement vs rester discret — ces dilemmes restent non tranchés systématiquement. Chaque cas fait l’objet de décisions ad hoc.

**Manque de maturité défensive** : beaucoup d’opérateurs d’infrastructures critiques n’ont toujours pas les moyens (visibilité OT, threat hunting, collaboration) pour détecter un pré-positionnement sophistiqué. La maturité nécessite des années à construire.

**Tensions géopolitiques** : Taïwan, Ukraine, Moyen-Orient, rivalités économiques. Les tensions croissantes augmentent la probabilité d’**activations** potentielles de pré-positionnements existants — ce qui augmente la gravité du problème.

### 27.7 Ciblage des télécoms et interception

**Salt Typhoon** (2024) a démontré l’ampleur du ciblage télécom par des acteurs étatiques. Cette tendance va s’amplifier.

**Pourquoi les télécoms** :

- **Accès aux communications** : appels, SMS, métadonnées de millions d’utilisateurs.
- **Systèmes d’interception légale** : compromettre les systèmes CALEA permet de voir qui les autorités surveillent — contre-espionnage de haute valeur.
- **Position centrale** : les télécoms ont accès à tout le trafic de leurs clients — un point de collecte privilégié.
- **Compromission difficilement détectable** : les infrastructures télécoms sont complexes, avec beaucoup d’équipements hérités et de sous-traitance.

**Implications** :

- Les personnalités à haut risque (opposants politiques, journalistes, militants, dirigeants d’entreprise critique) doivent supposer que leurs communications **non chiffrées de bout en bout** peuvent être compromises.
- Le passage à Signal, WhatsApp, iMessage (messageries E2EE) est devenu une recommandation standard, y compris par les autorités US post-Salt Typhoon.
- La souveraineté télécom redevient un enjeu stratégique — dépendre d’opérateurs étrangers (notamment chinois dans certains pays) pose des questions sécuritaires nouvelles.

### 27.8 Supply chain continues et éditeurs logiciels

Les **compromissions supply chain** restent un vecteur APT majeur. Tendances 2024-2026 :

**Ciblage des éditeurs logiciels tier 1** : Microsoft, SolarWinds, Kaseya, JetBrains ont été compromis dans des opérations majeures. La tendance ne faiblit pas — les éditeurs restent des cibles à très fort effet de levier.

**Cascades supply chain** (modèle 3CX) : compromission d’un éditeur via un autre éditeur compromis. Niveau d’imbrication qui complique l’attribution et la remédiation.

**Compromission de dépendances open source** : packages npm, PyPI, GitHub compromis pour injecter du malware dans les chaînes de build de multiples projets. Cas récents documentés en quantité croissante.

**Contractors et MSP** : les prestataires IT sont des cibles indirectes. Compromettre un MSP donne accès à ses clients (modèle Cloud Hopper d’APT10, toujours réplicable).

**Défense** :

- Zero Trust appliqué à la supply chain (ne pas faire confiance aux fournisseurs par défaut).
- Software Bill of Materials (SBOM) : obligations émergentes aux États-Unis (EO 14028) et en Europe (Cyber Resilience Act).
- Monitoring des processes fournisseurs (intégrité du build pipeline, signatures, reproductibilité).
- Évaluation de risques de la supply chain (obligation NIS 2).

### 27.9 Signaux géopolitiques à surveiller

Les analystes cyber doivent suivre plusieurs signaux géopolitiques qui affectent le paysage de la menace.

**Tensions autour de Taïwan** : une escalade militaire dans le détroit de Taïwan activerait probablement des pré-positionnements chinois existants. Les indicateurs : augmentation des exercices militaires PLA, déclarations politiques, mouvements diplomatiques.

**Évolution de la guerre en Ukraine** : intensification ou désescalade affectera les opérations russes destructives et d’influence. Les cessations de conflit ne signifient pas la fin des opérations cyber — elles peuvent simplement changer de forme.

**Élections majeures** : élections présidentielles et législatives dans les grandes démocraties sont des cibles récurrentes d’ingérence étrangère. Les services CTI montent typiquement leur vigilance à l’approche des échéances électorales.

**Sanctions et escalade économique** : l’introduction de nouvelles sanctions peut déclencher des ripostes cyber (Iran contre l’Albanie en 2022 après hébergement du MEK — précédent).

**Crises énergétiques** : tensions sur l’approvisionnement énergétique (Europe post-2022, tensions Moyen-Orient) augmentent le ciblage des infrastructures énergétiques.

**Crises médicales ou sanitaires** : pandémies ou crises sanitaires majeures produisent des vagues de cyberattaques opportunistes + étatiques (ciblage santé COVID par APT russes et chinois en 2020).

Pour l’analyste, maintenir une **veille géopolitique** parallèle à la veille technique est essentiel. Les deux s’alimentent réciproquement.

-----

## Chapitre 28 — Construire une défense APT-ready

> **Note sur ce chapitre.** Ce chapitre synthétise les principes de défense spécifiques aux APT. Il ne reproduit pas un cours de SOC ou d’Incident Response — il se concentre sur ce qui distingue la défense contre les APT étatiques de la défense générale.

### 28.1 Principes : assume breach, defense in depth, Zero Trust

La défense APT-ready repose sur trois principes structurants.

**Assume breach** : partir du principe que **l’adversaire est probablement déjà à l’intérieur**. Cette posture change tout — les efforts ne se limitent pas à empêcher l’entrée (prévention), mais s’étendent à la détection précoce, au containment rapide, à l’éradication efficace, et à la résilience.

La justification de l’« assume breach » : face à des acteurs comme Volt Typhoon (LotL exclusif, zéro malware), APT29 (abus cloud/identity sophistiqué), Turla (piggybacking, rootkits kernel), la prévention seule ne suffit pas. Les défenseurs doivent supposer que tôt ou tard, un acteur suffisamment motivé et ressourcé **entrera**. L’objectif devient alors de **limiter l’impact** et d’**écourter le dwell time**.

**Defense in depth** : multiples couches de défense indépendantes, de manière à ce qu’une défaillance à une couche soit compensée par les suivantes. Couches typiques : sécurité périmétrique, endpoint, identity, cloud/SaaS, réseau interne, applicatif, données, détection/réponse. Un attaquant qui franchit une couche doit en franchir d’autres avant d’atteindre les données critiques.

**Zero Trust** : ne pas faire confiance par défaut aux utilisateurs, appareils, ou applications, même à l’intérieur du périmètre. Chaque accès est authentifié, autorisé, et validé. Le concept a été formalisé par Forrester (John Kindervag, 2010) et adopté largement — **NIST SP 800-207** (Zero Trust Architecture, 2020) en donne un cadre de référence.

Application Zero Trust : MFA résistant au phishing pour tous les accès, conditional access basé sur le contexte, micro-segmentation réseau, verification continue plutôt que session persistante, principle of least privilege strict.

### 28.2 Contrôles minimum viables

La défense APT-ready repose sur un ensemble de **contrôles minimum viables** — pratiques sans lesquelles tout le reste est compromis. Priorisation proposée.

**Priorité 0 — Prérequis absolus** :

- **MFA résistant au phishing** sur tous les comptes (FIDO2 / WebAuthn). Exclure TOTP SMS/appel (contournables par AitM).
- **Privileged Access Management (PAM)** : rotation des credentials privilégiés, sessions auditées, just-in-time pour les accès critiques.
- **EDR déployé partout** : endpoints et serveurs (incluant les serveurs de production). Les serveurs sans EDR sont les pivots préférés des attaquants.
- **Patching des edge devices en moins de 48h** sur les CVE exploitées activement (référence CISA KEV).

**Priorité 1 — Base solide** :

- **Segmentation réseau** : IT/OT, zones sensibles isolées, segmentation micro-services si possible.
- **Durcissement Active Directory** : tiering strict des comptes, limitation des privilèges, monitoring des changements critiques (groupes admin, GPO, trusts), protection KRBTGT.
- **Monitoring cloud / identity** : visibilité sur Azure AD/Entra, applications OAuth, sign-ins anormaux, changements de configuration.
- **Backup hors ligne testé** : backup offline (non joignable depuis le réseau), testé régulièrement par restore réel, couvrant systèmes et données critiques.
- **Plan IR formalisé et exercé** : playbooks documentés, équipe identifiée, retainer IR externe si besoin, exercices réguliers.

**Priorité 2 — Maturité** :

- **Threat hunting proactif** : équipe ou prestataire dédié, cycles réguliers, guidé par la CTI des acteurs pertinents.
- **Purple team** : exercices réguliers combinant red team (simulation TTP APT) et blue team (détection).
- **Intégration CTI** : ingestion de renseignement actionnable, corrélation avec la télémétrie.
- **Visibilité OT** (si applicable) : passive monitoring sur les segments industriels.
- **Gestion de la supply chain** : évaluation des prestataires, SBOM, monitoring des intégrations.

### 28.3 Visibilité minimum viable

Sans visibilité, la détection est impossible. Les **sources de télémétrie** essentielles :

**Endpoints** :

- **Sysmon** : logs détaillés des process, connexions réseau, modifications de fichiers, chargements de DLL. Configuration de référence : Olaf Hartong Sysmon config (GitHub, open source, largement adopté).
- **PowerShell ScriptBlock logging** : tous les scripts PowerShell exécutés sont loggés.
- **EDR** : détections comportementales, télémétrie détaillée.
- **Windows Security events** : authentifications, changements de comptes, privilèges.

**Réseau** :

- **DNS** : résolutions sortantes, détection des domaines malveillants connus, détection des patterns (beaconing).
- **Firewall et proxy** : flux sortants, tentatives d’exfiltration, connexions vers infrastructure suspecte.
- **Flow data (NetFlow/IPFIX)** : vue agrégée des communications, détection d’anomalies volumétriques.
- **IDS/NDR** : détection d’intrusion réseau, analyse comportementale.

**Identity / Cloud** :

- **Azure AD / Entra sign-in logs** : qui se connecte, depuis où, avec quel contexte.
- **Audit logs** : changements de configuration, consents OAuth, rôles modifiés.
- **Application logs** : pour les SaaS critiques (M365, Google Workspace, Salesforce, etc.).

**Email** :

- **Email gateway logs** : messages reçus/envoyés, détections phishing, blocages.
- **Messagerie interne** : monitoring des messages à haut risque (pièces jointes, liens externes, thèmes sensibles).

**Sources OT** (si applicable) :

- **Passive monitoring OT** (Claroty, Dragos, Nozomi, Microsoft Defender for IoT).
- **Logs des engineering workstations**.
- **Logs des HMI, historian, SCADA applications**.

**Centralisation** : tout remonte vers un **SIEM** centralisé (Splunk, QRadar, Sentinel, Elastic, Chronicle, Exabeam) qui permet corrélation cross-sources. Sans SIEM, chaque source est un silo et les corrélations (signe d’une APT) sont invisibles.

### 28.4 Détection TTP-driven vs IoC-driven

La détection moderne doit être **TTP-driven**, pas seulement IoC-driven.

**Détection IoC-driven (limitée)** : liste de hashes, IP, domaines connus comme malveillants. Facile à implémenter, efficace contre les malwares connus, **inefficace contre les APT** qui adaptent leurs IoC.

**Détection TTP-driven (recommandée)** : règles qui détectent les **comportements** plutôt que les signatures statiques. Exemples :

- « Un processus PowerShell exécuté par MS Word est suspect » (détecte les macros malveillantes).
- « Une connexion RDP sortante depuis un serveur vers une IP externe est suspecte ».
- « Un compte admin qui se connecte à un système où il ne s’est jamais connecté avant est suspect ».
- « Une connexion Azure AD depuis un pays où l’utilisateur ne travaille pas est suspecte ».

**Outils** :

- **Sigma rules** : format ouvert pour les règles de détection SIEM. Bibliothèque open source disponible.
- **Elastic detections, Splunk ES, Microsoft Sentinel analytics** : règles natives des SIEM.
- **ATT&CK mapping** : mapper les détections aux techniques MITRE ATT&CK pour visualiser la couverture.

**Detection engineering** : discipline de construction et maintenance des règles de détection. Cycle : hypothèse de TTP, développement de règle, test, déploiement, tuning par feedback terrain. Les équipes SOC matures ont des detection engineers dédiés.

### 28.5 Le containment APT : scope avant contenir

Face à une APT détectée, la règle critique est : **scope avant de contenir**.

**Pourquoi** : une APT sophistiquée a des **accès redondants** (plusieurs mécanismes de persistence, comptes backdoor, plusieurs hosts compromis). Si on contient un seul accès (isoler une machine, désactiver un compte), l’attaquant **active immédiatement ses accès redondants** et disparaît — tout en étant alerté que la détection a eu lieu. Résultat : perte de visibilité, réinfection via TTP modifiées, dwell time rallongé.

**Méthode recommandée** :

1. **Détecter** une présence APT (un signe).
1. **Ne pas agir visiblement** — préserver l’invisibilité pour l’attaquant.
1. **Scope** : identifier tous les systèmes, comptes, et mécanismes compromis. Threat hunting actif guidé par les premières observations. Cette phase peut durer des jours à des semaines.
1. **Planifier le containment coordonné** : qui fait quoi, quand, dans quel ordre.
1. **Containment simultané** : désactivation de **tous** les accès en une fenêtre courte (idéalement quelques heures), **de manière coordonnée**. L’attaquant ne peut plus pivoter vers des accès redondants parce qu’ils sont tous coupés simultanément.
1. **Éradication** : nettoyage des mécanismes de persistence, reset des credentials, reconstruction des systèmes compromis.
1. **Monitoring renforcé post-éradication** : l’attaquant tentera probablement de revenir — détection des tentatives de réentrée.

**Outils** : EDR modernes permettent la réponse coordonnée (isolation réseau de multiple endpoints en une action, désactivation de comptes en masse). SOAR (Security Orchestration, Automation and Response) pour orchestrer les playbooks complexes.

**Retainer IR** : avoir un prestataire IR contractualisé en amont permet une réponse rapide sans négocier les termes pendant la crise. Retainers Mandiant, CrowdStrike, Kroll, Unit 42, Sophos, et équivalents européens sont la norme pour les grandes organisations.

### 28.6 Purple team orienté APT

Le **purple team** combine red team (simulation d’attaque) et blue team (détection/réponse) en exercices collaboratifs. Appliqué aux APT, il vise à **valider** les détections face aux TTP des acteurs pertinents.

**Approche** :

- Identifier les acteurs pertinents pour l’organisation (sectoriels, géographiques).
- Cataloguer leurs TTP documentées (ATT&CK Groups, rapports CTI).
- Reproduire ces TTP dans un environnement contrôlé.
- Vérifier si le SOC détecte chaque TTP avec quelle latence.
- Identifier les gaps et les corriger (nouvelles règles de détection, nouvelles sources de télémétrie).

**Frameworks d’émulation** :

- **Atomic Red Team** (Red Canary, open source) : bibliothèque de tests atomiques mappés sur ATT&CK.
- **CALDERA** (MITRE) : plateforme d’émulation adversaire automatisée.
- **Red Canary AtomicTestHarnesses** : tests paramétrés.
- **Vectr** : plateforme de gestion des exercices purple team.
- **APT Emulation Plans** (MITRE CTID) : plans d’émulation d’acteurs spécifiques (APT29, FIN6, menuPass/APT10, Sandworm, Carbanak, Turla).

**Cadence recommandée** : exercices réguliers (trimestriels pour les grandes organisations), chaque exercice ciblant un acteur ou un ensemble de TTP spécifique.

**Bénéfices** :

- Validation empirique des détections (vs théorique).
- Formation des équipes blue sur les TTP réelles.
- Priorisation des investissements de détection sur les gaps identifiés.
- Documentation des capacités de détection pour la direction et les auditeurs.

### 28.7 Exercices de simulation (tabletop et au-delà)

Les exercices testent la **réponse organisationnelle**, pas seulement les capacités techniques.

**Niveaux** :

- **Tabletop** : discussion autour d’un scénario. Durée 2-4h. Participants : CISO, SOC, IR, juridique, communication, direction. Teste la coordination, les décisions, les procédures.
- **Fonctionnel** : simulation plus approfondie avec actions techniques sur environnement de test.
- **Full-scale / live** : exercice sur systèmes réels (en environnement contrôlé) avec injection de scenarios réels.

**Scénarios APT recommandés** :

**Tabletop 1 — « APT29 a compromis votre Azure AD via phishing OAuth »**

- J0 : alerte sign-in suspect depuis un pays inhabituel sur un compte admin.
- J+1 : règle de forwarding inbox créée par le compte, redirigeant des emails vers externe.
- J+3 : exfiltration détectée de SharePoint via Graph API, ~500 Go de données.
- J+5 : découverte d’une application OAuth avec permissions admin et tokens SAML forgés via ADFS compromis.
- Questions clés : Quand escaladez-vous à la direction ? Qui informez-vous (clients, autorités, ANSSI) ? Contenez-vous immédiatement (risque perdre visibilité) ou scopez-vous d’abord ?

**Tabletop 2 — « Ransomware BlackBasta avec précurseur APT »**

- J0 : déploiement ransomware massif, des centaines d’endpoints chiffrés, note de rançon sur plusieurs serveurs.
- Investigation révèle que l’accès initial a été vendu par un Initial Access Broker qui l’avait obtenu 6 mois plus tôt via une compromission Citrix.
- L’IAB avait probablement aussi vendu l’accès à un acteur étatique qui l’a utilisé pour d’autres opérations (exfiltration de propriété intellectuelle) avant le déploiement ransomware.
- Questions clés : comment discriminer cybercrime vs APT dans la réponse ? Qui notifier (ANSSI pour les OIV, CNIL pour les données personnelles, parquet pour les infractions pénales) ? Comment gérer la communication externe ?

**Tabletop 3 — « Pré-positionnement OT détecté sans action destructive »**

- Le SOC détecte des TTP compatibles avec Volt Typhoon/Sandworm dans l’environnement OT.
- L’attaquant est présent depuis probablement 3+ mois, pas d’exfiltration visible, pas d’action destructive.
- Questions clés : éradiquez-vous immédiatement (risque de perdre le renseignement sur l’adversaire) ou surveillez-vous (risque de laisser une menace active) ? Qui prend cette décision ? Comment se coordonne-t-on avec l’ANSSI ? Comment communique-t-on (ou pas) publiquement ?

Ces tabletops révèlent régulièrement des gaps organisationnels : procédures d’escalade floues, absence de contacts établis avec les autorités, mauvais partage d’information interne, gaps de communication avec la direction.

### 28.8 Le partage d’information : ISAC, CSIRT, coordination européenne

Le **partage d’information** est un pilier de la défense collective contre les APT.

**Niveaux de partage** :

- **Intra-organisation** : entre équipes (SOC, IR, threat intel, IT, métiers).
- **Sectoriel** : ISAC (Ch.23) — partage des IoC, TTP, tendances avec les pairs du même secteur.
- **National** : CERT national (CERT-FR, CERT-DE, NCSC, etc.), autorités (ANSSI, BSI).
- **International** : FIRST (Forum of Incident Response and Security Teams), coordination Five Eyes, UE.

**Règles de partage — TLP (Traffic Light Protocol)** :

- **TLP:RED** : strictement limité aux destinataires nommés.
- **TLP:AMBER** : limité à l’organisation et partenaires directs.
- **TLP:GREEN** : partage dans la communauté pertinente.
- **TLP:CLEAR** : public sans restriction.

**Outils de partage** :

- **MISP** (Malware Information Sharing Platform) : plateforme open source de partage d’indicateurs structurés.
- **STIX / TAXII** : formats standards pour le partage de threat intelligence.
- **ISAC portals** : chaque ISAC a ses mécanismes de partage.

**Bénéfice collectif** : un IoC partagé par un membre protège potentiellement tous les autres. L’inverse : ne pas partager par crainte d’exposer l’incident laisse les pairs vulnérables.

**Obligations légales** : NIS 2 impose des notifications aux autorités sous 24h (early warning) et 72h (détaillée) pour les incidents significatifs. RGPD impose la notification CNIL sous 72h pour les violations de données personnelles.

### 28.9 Former les équipes : CTI-driven defense

La défense APT-ready n’existe pas sans équipes **formées et motivées**. Quelques principes.

**Recrutement et rétention** : les profils cyber sont rares et chers. La rétention dépend de facteurs non-salariaux (défis intéressants, formation continue, reconnaissance, culture d’équipe, flexibilité). Les RSSI qui traitent leurs équipes cyber comme un investissement stratégique retiennent mieux.

**Formation continue** : certifications (SANS, Offensive Security, ISC2, ISACA), conférences (Black Hat, DEF CON, SSTIC, FIC, Botconf, RSA), labs d’entraînement (Hack The Box, TryHackMe, RangeForce), lectures (rapports Mandiant, CrowdStrike, Microsoft, Dragos, blogs spécialisés).

**CTI-driven mindset** : comprendre les acteurs avant de défendre contre les acteurs. Les équipes qui lisent régulièrement la CTI (rapports publics, threat intel d’abonnement, partages ISAC) savent ce contre quoi elles défendent. Les équipes qui ne lisent que leur SIEM ne savent pas.

**Exercices et apprentissage continu** : les tabletops, purple teams, CTF internes entretiennent les compétences. Une équipe qui ne s’entraîne pas perd ses capacités.

**Culture d’apprentissage des incidents** : après chaque incident (réel ou simulé), **post-mortem blameless** — analyse des faits, identification des causes systémiques, actions correctives documentées. Les équipes qui cachent les erreurs apprennent moins que celles qui les exposent et corrigent.

**Relation avec la direction** : le CISO doit pouvoir parler métier, budget, et risque, pas seulement technique. La défense APT-ready exige des investissements que la direction doit comprendre et soutenir — d’où l’importance de traduire les menaces APT en langage d’impact business compréhensible par le non-technique.

-----
