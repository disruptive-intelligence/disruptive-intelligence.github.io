---
title: Chapitre 25 — L’écosystème cyber offensif mondial
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie VII — Géopolitique, attribution et prospective
  - index.md
---

## 25.1 Panorama quantitatif

Plusieurs centaines de groupes APT sont suivis publiquement. Ordres de grandeur (2026) :

- **MITRE ATT&CK Groups** : ~160 groupes documentés publiquement.
- **Malpedia** (Fraunhofer FKIE) : plusieurs centaines de familles de malware attribuées.
- **CrowdStrike** : 230+ acteurs nommés suivis.
- **Mandiant** : 300+ intrusion sets dans son périmètre interne.
- **Microsoft Threat Intelligence** : 150+ threat actors nommés publiquement.

Ces chiffres croissent chaque année. La concentration d’activité reste sur un noyau restreint d’acteurs de premier plan — la **loi de Pareto** s’applique largement : 20% des groupes produisent 80% de l’activité documentée.

## 25.2 La prolifération des capacités

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

## 25.3 Le modèle contractor comme industrie offensive

Le modèle des **contractors civils** mandatés pour des opérations cyber étatiques est une dimension structurelle de l’écosystème contemporain.

**Chine — i-Soon et ses pairs** : le leak i-Soon (Ch.8) a documenté un écosystème vaste. D’autres contractors chinois existent. Entreprise privée qui vend des services cyber (outils, opérations, surveillance) à des clients étatiques multiples (MSS, PLA, polices provinciales).

**Russie — écosystème flou entre services et prestataires** : moins formalisé qu’en Chine, mais plusieurs entités sont à la frontière (KillNet, NoName057(16) côté russe, avec niveaux de coordination variables avec les services).

**Israël — secteur commercial structurellement lié à l’appareil de défense** : pipeline Unité 8200 → startups → surveillance commerciale (Ch.18). NSO, Intellexa, Candiru, Paragon régulés par le ministère israélien de la Défense.

**Occident — contractors de défense classiques étendus au cyber** : Raytheon, Lockheed Martin, BAE Systems, Thales, Airbus et d’autres ont des divisions cyber. Opèrent généralement dans des cadres juridiques plus formalisés (marchés publics, supervision parlementaire).

**États émergents** : plusieurs pays développent des capacités via acquisition de services privés (achat de spywares commerciaux), recrutement d’opérateurs formés ailleurs, coopération avec des contractors étrangers. Le seuil d’entrée pour un État désireux d’acquérir des capacités cyber est plus bas qu’il y a 10 ans.

**Implications analytiques** : l’attribution devient plus difficile quand plusieurs contractors travaillent pour un même client ou qu’un contractor travaille pour plusieurs clients. Les frontières « opération étatique » / « opération commerciale au service de l’État » s’estompent.

## 25.4 Lecture comparative des doctrines par bloc

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

## 25.5 L’écosystème comme instrument diplomatique

Les cyberopérations sont **intégrées dans la diplomatie** des États.

**Le cyber comme signal** : une cyberopération peut signaler une position politique (Shamoon comme représailles iraniennes pour Stuxnet, Sandworm comme démonstration de capacité hybride russe, Volt Typhoon comme dissuasion chinoise liée à Taïwan). Comprendre le signal est aussi important que comprendre l’effet technique.

**Le cyber comme monnaie d’échange** : les attributions, sanctions, indictments peuvent être levés ou maintenus selon l’évolution des relations. L’accord Xi-Obama 2015 sur l’espionnage économique chinois a produit un effet temporaire observable dans la baisse des opérations APT chinoises contre les entreprises US pendant quelques années.

**Le cyber comme test de résolution** : les acteurs testent la volonté des défenseurs de répondre. Une escalade cyber qui ne provoque pas de réponse significative encourage de nouvelles escalades. Une réponse ferme peut décourager.

**Le cyber comme déstabilisation en deçà du seuil du conflit armé** : la zone grise permet des opérations qui, dans le monde physique, appelleraient une réponse militaire — mais qui restent « tolérées » au cyber. Cette asymétrie favorise les États agresseurs.

Pour l’analyste, ces dimensions diplomatiques et stratégiques sont indissociables du technique. Un rapport CTI qui se limite aux IoC et aux TTP, sans considération du contexte diplomatique, donne une vision incomplète.

-----
