---
title: "Analyse — ENISA : rapport sur le panorama des menaces cyber, édition 2026"
date: 2026-10-08
kind: analysis
document_type: rapport
theme: cyber
slug: menaces-cyber-en-europe-le-bruit-des-ddos-le-poids-des-dependances
author: "ENISA"
organization: "Agence de l'Union européenne pour la cybersécurité (ENISA)"
tags:
  - panorama des menaces
  - DDoS
  - rançongiciel
  - cyberespionnage
  - chaîne d'approvisionnement
  - manipulation de l'information
source_file: inbox/ENISA Threat Landscape 2026_Final.pdf
source_url: https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Threat%20Landscape%202026_Final.pdf
---

# Analyse — ENISA : rapport sur le panorama des menaces cyber, édition 2026

## Métadonnées

- **Document :** *ENISA Threat Landscape 2026*, rapport institutionnel de 101 pages, marqué TLP:CLEAR. Le PDF original est conservé dans `inbox/ENISA Threat Landscape 2026_Final.pdf`.
- **Auteur et éditeur :** ENISA, Agence de l'Union européenne pour la cybersécurité, comme l'indiquent la couverture et la page de crédits (p. 1-2). Le fichier PDF porte aussi une métadonnée technique au nom de Jamila Boutemeur ; elle ne remplace pas le crédit d'auteur « ENISA » imprimé dans le rapport.
- **Date :** septembre 2026 sur la couverture ; le jour exact n'y est pas indiqué. ISBN 978-92-9204-807-5 ; DOI 10.2824/0806036 (p. 1, 3).
- **Périmètre :** incidents concernant les États membres et organisations établies dans l'UE entre le 1er janvier et le 31 décembre 2025 ; 8 257 incidents réunis principalement à partir de sources ouvertes et de contributions anonymisées (p. 9).
- **Méthode de cette analyse :** jusqu'aux « Cinq éléments essentiels », les constats proviennent uniquement du PDF et renvoient à sa pagination imprimée. La dernière section examine séparément des sources extérieures consultées le 8 octobre 2026.

## Repères pour comprendre le document

Ce rapport est un **panorama de signalements documentés**, pas un recensement exhaustif de toutes les intrusions dans l'UE. Il juxtapose des attaques techniquement différentes, des revendications parfois invérifiables et des observations publiées avec retard. Ses pourcentages changent de dénominateur selon le chapitre : ensemble des 8 257 incidents, incidents d'accès non autorisé, sous-ensemble dont le vecteur est connu, ou revendications d'une famille d'acteurs. Le lire correctement exige donc de demander à chaque chiffre « sur quels cas ? » avant d'en tirer une priorité de défense (p. 9-13).

- **Incident enregistré** — Cas retenu dans la base de l'ENISA à partir de sources publiques ou de contributions ; sa présence ne prouve ni la totalité de ses effets ni une fréquence réelle dans toute l'UE (p. 9-10).
- **DDoS** — Saturation d'un service en ligne par un grand volume de requêtes ou de trafic. Une revendication DDoS ne démontre pas à elle seule une indisponibilité effective (p. 83, 88).
- **Accès non autorisé** — Entrée dans un système ou compte sans autorisation ; cette catégorie couvre des objectifs et des conséquences différents, de l'espionnage au vol de données (p. 11-13).
- **Vecteur d'intrusion** — Première voie d'accès identifiée, par exemple une faille exploitable, un compte compromis ou une mauvaise configuration ; il demeure inconnu dans une large part des cas (p. 11, 60).
- **Faille *zero-day* / *N-day*** — Vulnérabilité exploitée avant sa divulgation ou sa correction pour la première ; faille déjà connue pour la seconde. Cette distinction pédagogique explicite les termes employés par le rapport (p. 7, 90).
- **Rançongiciel et extorsion** — Opération criminelle qui chiffre des systèmes, vole des données, ou combine les deux pour exiger un paiement ; une inscription sur un site de fuite ne prouve pas toujours un déploiement de logiciel malveillant (p. 46-51).
- **Dépendance numérique** — Prestataire, logiciel, bibliothèque, service cloud ou infrastructure dont la compromission peut atteindre plusieurs organisations clientes ou utilisatrices (p. 12, 18, 95).
- **Groupe lié à un État (*state-nexus*)** — Ensemble d'intrusion associé dans le rapport à un intérêt ou à un pays sur la base d'attributions publiques et d'analyses techniques citées ; cette imputation n'est pas identique à une décision judiciaire (p. 60-63).
- **FIMI** — Manipulation de l'information et ingérence étrangères : activité coordonnée visant des perceptions ou des débats publics, étudiée ici à partir des données du Service européen pour l'action extérieure (p. 74).
- **OT** — Technologie opérationnelle contrôlant des processus physiques ou industriels ; les revendications d'accès OT demandent une vérification spécifique des effets réels (p. 83-84).
- **NIS2** — Directive européenne distinguant notamment des entités essentielles et importantes et imposant des mesures de gestion du risque ainsi que la notification de certains incidents. Ses notifications et la veille en sources ouvertes n'ont pas le même périmètre (p. 18-19).
- **KEV** — Catalogue de vulnérabilités dont l'exploitation est connue, utilisé dans le chapitre sur les failles pour distinguer exploitation attestée et simple gravité théorique (p. 93-94).

## Résumé exécutif

L'ENISA examine **8 257 incidents concernant l'UE en 2025**. Les DDoS constituent 51,3 % des cas enregistrés et les accès non autorisés 39,5 %. Mais le volume n'est pas l'impact : les DDoS, souvent revendiqués par des groupes militants, pèsent sur la visibilité statistique tandis que les rançongiciels menacent davantage la continuité immédiate et que l'espionnage peut produire des effets stratégiques différés. L'administration publique arrive en tête des secteurs recensés (31,8 %), principalement sous l'effet de ces campagnes DDoS (p. 7, 13, 18, 20).

Le rapport suit cinq fils : exposition sectorielle ; cybercriminalité et extorsion ; intrusions liées à des États ; manipulation de l'information ; hacktivisme, puis vulnérabilités. Il montre que le même chemin d'accès, notamment la faille exposée, le compte détourné ou le fournisseur compromis, sert des objectifs distincts. Les dépendances envers prestataires, bibliothèques logicielles et environnements cloud expliquent pourquoi un incident local peut se propager à plusieurs organisations (p. 9, 12, 43-46, 60, 95).

La **conclusion utile pour la veille** est double. D'une part, surveiller séparément la fréquence des revendications, les compromissions avérées et la gravité opérationnelle. D'autre part, cartographier les accès et dépendances partagés avant de hiérarchiser les correctifs et les mesures de continuité. Les données de l'ENISA donnent des tendances observées, mais ni un taux d'attaque de l'ensemble des organisations européennes ni une comparaison annuelle directe : la période et les catégories de collecte ont changé (p. 9-10, 18-19).

## Chronologie

La séquence sert ici à distinguer les faits de 2025, leur analyse publiée en 2026 et les évolutions que le rapport place lui-même hors de sa période statistique.

- **Janvier-décembre 2025 :** fenêtre de collecte des 8 257 incidents ; elle chevauche de six mois l'édition précédente, qui allait de juillet 2024 à juin 2025 (p. 9).
- **Premier semestre 2025 :** les campagnes de rançongiciels et plusieurs opérations de police modifient temporairement les marques et infrastructures criminelles ; la disparition d'un nom ne signifie pas celle de ses affiliés (p. 53, 59).
- **Troisième trimestre 2025 :** les revendications hacktivistes culminent, notamment après l'opération policière Eastwood contre NoName057(16) ; des revendications concernant l'OT se multiplient ensuite, sans preuve comparable d'effets physiques (p. 84, 86-87).
- **Septembre 2026 :** l'ENISA publie ce rapport et une version actualisée de sa méthodologie. Les exemples d'IA de 2026 qu'il cite sont explicitement extérieurs à sa fenêtre de collecte (p. 1, 9, 17).

## Thèse principale

Le rapport est une **synthèse de renseignement sur les menaces**, accompagnée d'évaluations prospectives, plutôt qu'une démonstration causale. L'ENISA soutient que des familles d'acteurs aux motivations différentes réutilisent des accès, outils et services semblables, tandis que l'interconnexion des environnements numériques élargit les effets d'une compromission. Cette convergence complique l'imputation ; elle ne rend pas équivalents les risques de disponibilité, d'extorsion et d'espionnage (p. 7-8, 14, 95-96).

Sa proposition implicite pour l'action est de **prioriser par impact et dépendance**, en replaçant chaque pourcentage dans sa population observée. L'agence anticipe le maintien du cybercrime comme risque majeur de continuité, la persistance des opérations d'espionnage et des vagues de DDoS liées à l'actualité géopolitique. Elle juge l'IA susceptible d'accélérer plusieurs phases des opérations malveillantes, tout en reconnaissant que ses usages constatés en 2025 servent surtout à renforcer des pratiques existantes (p. 15-17, 95-96).

## Informations et arguments importants

Les nombres les plus cités dans ce rapport n'ont de sens qu'accompagnés de leur champ. La base associe plusieurs types d'événements et de revendications ; l'ENISA précise que les sources ouvertes et les contributions volontaires ne donnent qu'une vue partielle, que les dates de divulgation varient et que fraude, fuite de données et rançongiciel peuvent se recouper (p. 9-10).

### Une carte dominée par les DDoS, pas par les dommages

Sur l'ensemble des incidents retenus, **51,3 % concernent des DDoS** et **39,5 % des accès non autorisés**. Les objectifs évalués sont principalement idéologiques (57,3 %) puis financiers (29,2 % dans le chapitre de synthèse, 29,3 % dans le résumé). L'ENISA insiste : la première catégorie comprend beaucoup de perturbations limitées, tandis que les rançongiciels ont un effet plus fort à court terme et l'espionnage à moyen ou long terme. La proportion d'incidents ne mesure donc pas la perte économique ou stratégique (p. 7, 13-14).

Le **phishing représente 77,8 % des techniques d'ingénierie sociale identifiées**, et non 77,8 % de tous les incidents. Parmi les accès non autorisés, un vecteur initial n'est identifié que pour **5,2 %** des cas ; dans ce sous-ensemble restreint, l'exploitation de vulnérabilités représente **60,4 %**. Ce résultat souligne un chemin d'accès important, mais ne permet pas d'affirmer que six intrusions sur dix, toutes catégories confondues, commencent par une faille (p. 11).

### Des secteurs exposés selon des mécanismes différents

La répartition globale place l'**administration publique à 31,8 %**, devant les services aux entreprises (8,5 %), le transport (8 %), l'industrie manufacturière (6,9 %) et la finance ou banque (5,6 %). Pour l'administration, **81,8 % des incidents sectoriels** relèvent de DDoS à motivation idéologique. Dans l'industrie, au contraire, l'accès non autorisé domine (80,4 %) et, parmi les cas à motivation financière du secteur, le rançongiciel constitue 82,8 %. Ces deux profils appellent des lectures opérationnelles différentes malgré un même classement général (p. 18, 20, 31-32).

Le rapport compare sa veille avec **1 954 événements notifiés par les États membres au titre de NIS2 pour 2025**, comptés au 14 juillet 2026. Dans ce second ensemble, santé et infrastructure numérique entrent dans les cinq premiers secteurs, aux côtés de l'administration, de la banque et du transport. Les obligations, seuils et conditions de notification diffèrent de la collecte ouverte ; ce contraste évite de traiter le classement ENISA comme une photographie complète des incidents importants (p. 19, 37).

Les **dépendances partagées** traversent ces secteurs. L'ENISA cite des prestataires de services, des dépôts et paquets logiciels, ainsi que des environnements SaaS ou cloud dont la compromission ouvre l'accès à plusieurs clients. Elle évoque notamment la campagne Shai-Hulud contre des paquets npm et, dans les services aux entreprises, un fournisseur spécialisé français dont l'incident aurait perturbé des banques et conseillers patrimoniaux. Il s'agit d'exemples étayant le mécanisme, pas d'une mesure de la fréquence de toutes les attaques de chaîne d'approvisionnement (p. 12, 24, 43-46).

### La cybercriminalité : accès, données, pression

Les activités financières représentent **29,3 % des événements** selon le chapitre cybercrime. Dans cette sous-population, les revendications de rançongiciel forment **47,3 %**, les fuites de données **36 %**, les fraudes et usurpations **13,3 %**. Les fabricants concentrent 25,2 % des revendications de rançongiciel ; les services aux entreprises suivent à 18,7 %. Qilin, SafePay, Akira, INC Ransom et Hunters International figurent parmi les opérateurs les plus actifs dans la collecte (p. 38, 46-49).

L'ENISA décrit une **chaîne de monétisation** : phishing et kits prêts à l'emploi, vol d'identifiants ou de sessions, vente d'accès, extraction de données, puis extorsion. ClickFix pousse une victime à exécuter elle-même une commande malveillante ; l'usurpation de personnels informatiques et l'emploi d'outils de gestion légitimes brouillent aussi les défenses. Les exemples de fuites tirés de forums sont explicitement des *revendications dont l'authenticité ou l'actualité n'a pas pu être vérifiée* ; les compter comme violations confirmées surévaluerait la preuve disponible (p. 40-46, 51-57).

L'agence infère un déplacement vers l'exfiltration et l'extorsion à partir des techniques publiquement documentées pour les principaux opérateurs. Son relevé fait apparaître T1041, exfiltration sur canal de commande, dans 73,3 % de ces techniques, contre 13,7 % pour T1486, chiffrement à effet. Ce sont des **fréquences de techniques rapportées**, dépendantes de la visibilité publique, et non la part de toutes les attaques de rançongiciel sans chiffrement (p. 51-52).

### Espionnage, ingérence et hacktivisme

Les ensembles d'intrusion liés à des États privilégient, selon les cas documentés, l'administration, la défense, les télécommunications, le transport et les outils de gestion. Parmi les incidents de cette catégorie, **81,7 %** sont des accès non autorisés et **12 %** des campagnes de phishing. Le vecteur initial n'est connu que pour **20 %** ; dans ce sous-ensemble, 70 % impliquent une vulnérabilité. Parmi les ensembles attribués à un pays dans le rapport, les liens russes représentent 47,6 %, chinois 15,5 %, nord-coréens 14,1 % et iraniens 9 % : ces parts ne sont pas celles de toutes les attaques en Europe (p. 60-63).

Le chapitre FIMI reprend directement une étude du **Service européen pour l'action extérieure (SEAE)** sur **540 incidents de manipulation de l'information en 2025**. Il s'agit d'un autre corpus que les 8 257 événements cyber. Sur ce corpus FIMI, 65 % restent sans attribution, 29 % sont attribués à la Russie et 6 % liés à la Chine ; 27 % des incidents détectés utilisent des techniques liées à l'IA. Le rapport note aussi qu'une production synthétique abondante peut susciter peu d'engagement authentique : volume et efficacité de l'influence ne se confondent pas (p. 74, 79).

Enfin, l'ENISA relève **4 709 revendications hacktivistes**, dont plus de 89 % portent sur des DDoS. Sur une analyse propre aux annonces de NoName057(16) et à DDoSia, seules **23,8 % des revendications examinées** ont été validées par des contrôles indépendants de disponibilité. Le reste n'est pas nécessairement fictif, mais ne constitue pas une preuve d'indisponibilité. Les annonces d'intrusion OT augmentent, alors que la vérification des victimes, des méthodes et de l'impact manque souvent (p. 83-84, 88).

### Vulnérabilités et IA : exposition constatée, scénarios anticipés

L'ENISA signale **plus de 48 000 nouvelles vulnérabilités avec identifiant CVE en 2025**, soit 22 % de plus qu'en 2024 ; 9 % sont classées critiques et 30 % élevées selon les scores disponibles. Le chapitre souligne l'intérêt de la base KEV pour distinguer les failles effectivement exploitées. Le nombre brut de CVE n'indique pas le nombre de systèmes européens vulnérables ni l'ordre des correctifs pour une organisation donnée (p. 90-94).

Pour l'IA, le rapport fait une distinction utile : en 2025, les acteurs observés emploient surtout des outils grand public pour accélérer l'hameçonnage, les scripts, la reconnaissance ou la manipulation de contenus ; la démonstration d'une capacité offensive entièrement nouvelle demeure plus limitée. Les exemples de 2026 figurent dans un encadré **hors période de collecte**. La perspective d'opérations avec moins de supervision humaine relève ainsi d'une évaluation prospective, pas d'une proportion mesurée dans les incidents de 2025 (p. 15-17, 95-96).

## Points particulièrement intéressants pour la veille

Les signaux suivants se prêtent à un suivi, à condition de mesurer les effets observables et non seulement la communication des groupes.

- **Écart entre revendication et service réellement touché.** La faible validation indépendante des annonces de DDoSia (23,8 % dans l'échantillon étudié) montre l'importance d'associer toute revendication à une mesure de disponibilité et à sa durée. *Inférence pour la veille :* suivre séparément annonce, preuve technique et effet utilisateur (p. 88).
- **Concentration du risque chez les intermédiaires.** Les incidents visant fournisseurs SaaS, plateformes de développement et prestataires peuvent exposer plusieurs clients par une relation de confiance commune. *Inférence pour la veille :* cartographier les dépendances et droits d'accès des fournisseurs, au-delà du seul nombre d'incidents reçus (p. 12, 43-46, 68).
- **Deux visages de l'administration publique.** Les DDoS dominent son volume enregistré, tandis que l'espionnage cible notamment les missions diplomatiques et ministères. *Inférence pour la veille :* ne pas laisser les pics de DDoS masquer des compromissions de comptes ou de messagerie plus discrètes (p. 20-23, 67).
- **L'identité comme porte d'entrée.** Phishing par code d'appareil, vol de jetons, usurpation du support et infostealers exploitent des flux légitimes d'authentification. *Inférence pour la veille :* considérer les sessions, consentements d'application et comptes de prestataires comme des actifs critiques (p. 46, 55-56, 64).
- **IA à la fois instrument et cible.** Le rapport documente l'assistance aux opérations et l'intérêt pour les systèmes d'IA connectés à des fichiers ou identifiants. *Inférence pour la veille :* distinguer preuve d'emploi offensif, exposition des intégrations internes et scénarios encore prospectifs (p. 15-17).

## Faits, opinions et interprétations

### Faits rapportés par la source

L'ENISA dit avoir analysé **8 257 incidents** pour l'année civile 2025, avec une forte part de DDoS (**51,3 %**) et d'accès non autorisés (**39,5 %**). L'administration publique représente **31,8 %** des incidents classés par secteur, et les revendications hacktivistes sont au nombre de **4 709**. Ces chiffres décrivent la base rassemblée par l'agence, pas un univers d'incidents exhaustivement connus. Le corpus FIMI de 540 cas provient quant à lui du SEAE (p. 7, 9, 18, 74, 83).

### Opinions ou positions de l'auteur

L'agence estime que les rançongiciels sont les plus perturbateurs à court terme et que l'espionnage constitue une menace stratégique plus longue, jugement qui ne découle pas d'un simple comptage. Elle évalue comme probable la persistance des vagues hacktivistes et comme hautement probable l'accélération de certaines opérations malveillantes par l'IA. La matrice de l'annexe associe notamment « highly likely » à une confiance supérieure à 90 % dans le langage du rapport ; il s'agit d'un degré d'estimation de l'analyste, pas d'une fréquence observée (p. 10, 13, 95-96, 100).

### Interprétations et inférences

L'interprétation centrale de cette analyse est que **le risque de propagation par les dépendances** mérite une priorité de veille que le classement brut des attaques ne révèle pas. Les cas de fournisseurs, de plateformes logicielles et de services d'identité soutiennent ce raisonnement, mais le PDF ne chiffre pas une probabilité universelle de propagation. De même, la différence entre la veille ouverte de l'ENISA et les notifications NIS2 suggère un biais de visibilité sectoriel ; elle ne permet pas, sans données supplémentaires, de recalculer un « vrai » palmarès des secteurs (p. 9, 12, 18-19, 43-46).

## Limites et points à vérifier

Les limites suivantes touchent la portée des conclusions, et non la présentation formelle du rapport.

1. **Échantillon incomplet et sélectif.** Les sources ouvertes favorisent les attaques visibles ou revendiquées ; les contributions des États et partenaires ne sont pas exhaustives. L'espionnage peut apparaître avec six mois à plus de quatre ans de retard, ce qui sous-représente potentiellement ses effets récents (p. 9-10).
2. **Comparaison d'une année à l'autre fragile.** La fenêtre 2025 chevauche de six mois l'édition précédente et la collecte de fraudes et de fuites a été élargie. Une hausse du nombre d'événements recueillis n'établit donc pas seule une hausse égale des attaques réelles (p. 9).
3. **Dénominateurs difficiles à suivre.** Le 60,4 % des intrusions par vulnérabilité repose sur seulement 5,2 % des accès non autorisés dont le vecteur est connu. De même, les proportions sectorielles, financières et étatiques portent sur des populations différentes et ne doivent pas être additionnées (p. 11, 18, 38, 60).
4. **Revendiquer n'est pas prouver.** Les annonces de fuite sur forums et de DDoS ou d'accès OT ne documentent pas systématiquement une compromission nouvelle ou une perturbation mesurée. Les contrôles de disponibilité de DDoSia montrent concrètement cet écart (p. 42, 83-84, 88).
5. **Attribution et impact distincts.** Les liens d'un groupe à un État, ainsi que les jugements d'intention, dépendent de sources publiques et d'imputations techniques. Le nombre d'opérations attribuées ne traduit ni leur gravité ni une responsabilité étatique juridiquement établie (p. 60-63).
6. **Données hétérogènes entre chapitres.** Le FIMI du SEAE, les notifications NIS2 et la veille cyber de l'ENISA ont chacun leur propre définition d'un cas. Leur juxtaposition éclaire les angles morts, mais n'autorise pas un total unique ni une comparaison directe des taux (p. 9, 19, 74).
7. **Chiffres internes à contrôler.** Le résumé donne 29,3 % d'activités financières, le panorama 29,2 % ; le résumé cite 5,9 % de cyberespionnage, le panorama 6,3 %. Ces petits écarts peuvent tenir au périmètre ou aux arrondis, sans explication explicite suffisante dans les passages concernés (p. 7, 13).
8. **Prospective IA encore peu quantifiée.** Les exemples de 2026 sont hors fenêtre et les scénarios d'automatisation accrue restent des évaluations. Le PDF ne mesure pas une part d'attaques 2025 autonomes de bout en bout (p. 15-17, 95-96).

## Sources et références mentionnées

Le rapport s'appuie sur sa méthodologie CTL actualisée, des signalements nationaux et du partenariat cyber de l'ENISA, puis sur une bibliographie abondante de CERT, agences publiques, éditeurs de sécurité, chercheurs et médias. Le chapitre FIMI reprend explicitement le quatrième rapport du SEAE ; les comparaisons sectorielles citent NIS360 et le bilan des notifications NIS2 ; les vulnérabilités mobilisent CVE, CWE, la base EUVD et le catalogue KEV de la CISA. Les études de cas et revendications issues de forums ou de sites de fuite ont un statut probatoire plus faible que des notifications officielles ou des observations techniques indépendantes (p. 9, 18-19, 42-46, 74, 90-94).

## Cinq éléments essentiels à retenir

1. **Le volume n'est pas l'impact :** les DDoS dominent les cas recueillis, tandis que rançongiciels et espionnage concentrent d'autres formes de dommage (p. 7, 13).
2. **Les chiffres ont des dénominateurs différents :** le 60,4 % d'exploitation de failles ne concerne qu'un sous-ensemble très restreint d'accès non autorisés (p. 11).
3. **L'administration cumule deux risques :** beaucoup de perturbations publiques et des intrusions discrètes visant les fonctions diplomatiques ou gouvernementales (p. 20-23, 67).
4. **Les prestataires et plateformes multiplient les effets :** leur accès partagé peut transformer une compromission en incident pour plusieurs organisations (p. 12, 43-46).
5. **Une revendication exige une preuve :** fuites, DDoS et intrusions OT doivent être vérifiés avant d'être traités comme des dommages confirmés (p. 42, 83-84, 88).

## État de l'art et regards extérieurs

Recherches effectuées le 2026-10-08. Cette section seule utilise des sources en ligne ; elle confronte les constats précédents à leurs origines et à des données publiées après ou autour du rapport, sans modifier l'analyse du PDF.

### Travaux de référence

- **Méthode de collecte.** [ENISA — *Cybersecurity Threat Landscape Methodology*](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology), publiée le 1er août 2025 et mise à jour en septembre 2026, explicite la production des panoramas horizontaux et sectoriels. Elle aide à comprendre que le rapport décrit un processus d'observation et d'évaluation, non une enquête de prévalence auprès de toutes les organisations européennes.
- **Résilience des secteurs.** [ENISA — *NIS360*](https://www.enisa.europa.eu/enisa-nis360-2026), publié le 28 mai 2026, évalue maturité et criticité de secteurs NIS2 selon un cadre différent du comptage d'incidents. Sa [présentation des résultats](https://www.enisa.europa.eu/news/nis360-the-bigger-picture-on-maturity-and-criticality-of-nis-critical-sectors) du même jour situe notamment la santé, le rail, le maritime et l'administration dans la zone où la criticité dépasse la maturité. Cette seconde grille explique pourquoi un secteur moins représenté dans les signalements ouverts peut rester prioritaire.

### Compléments sur le sujet

Les sources extérieures précisent surtout la différence entre visibilité, capacité technique et effet réel. Elles ne fournissent pas une base commune permettant de recalculer les parts du panorama ENISA.

- **Mesurer les DDoS.** [Cloudflare — *2025 Q4 DDoS threat report*](https://blog.cloudflare.com/ddos-threat-report-2025-q4/), 5 février 2026, annonce 47,1 millions d'attaques atténuées sur **son propre réseau** en 2025, dont 34,4 millions à la couche réseau. Cette mesure directe illustre la fréquence et la croissance des DDoS, mais son périmètre mondial, lié aux clients et infrastructures Cloudflare, ne peut être comparé au 51,3 % des incidents européens retenus par l'ENISA. La taille record de 31,4 Tb/s rapportée par l'entreprise n'est pas une mesure du dommage moyen subi par les victimes.
- **Notifier des incidents significatifs.** [Directive (UE) 2022/2555, articles 21 à 23](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng), publiée le 27 décembre 2022, établit des obligations de gestion des risques et de notification pour les entités dans son champ. Les notifications significatives, incidents, menaces et quasi-incidents agrégés par les États répondent à des règles différentes des mentions trouvées en sources ouvertes : c'est une explication institutionnelle possible du contraste sectoriel relevé p. 19, et non la preuve qu'un classement serait erroné.
- **Ingérence informationnelle.** [SEAE — *4th Report on FIMI Threats*](https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf), mars 2026, est la source primaire des **540 cas FIMI**, des 10 500 canaux et des quelque 43 000 contenus ou observables. Le SEAE précise que 65 % des cas restent non attribués et que l'accès aux données des plateformes varie. Le chiffre de 88 % sur X décrit les observables de son corpus, pas une répartition mondiale de toute la manipulation de l'information.
- **Hiérarchiser les failles.** [CISA — *Known Exploited Vulnerabilities Catalog*](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), catalogue consulté le 8 octobre 2026, recense des CVE avec preuve d'exploitation active. Il apporte un critère distinct du score CVSS utilisé par l'ENISA : pour une organisation, exploitation connue, exposition de ses propres actifs et rôle du produit dans sa chaîne de services doivent être croisés. Le catalogue est évolutif ; son contenu actuel n'est pas le même qu'au 31 décembre 2025.

### Vérification des affirmations de la source

Les confirmations ci-dessous sont circonscrites aux chiffres et périmètres que les sources primaires permettent réellement de contrôler.

| Affirmation du document | Verdict | Source de la vérification |
| --- | --- | --- |
| La publication couvre les événements du 1er janvier au 31 décembre 2025. | **Confirmé** | [ENISA — page officielle du rapport](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026), 22 septembre 2026. |
| L'administration publique est le premier secteur de la collecte, autour de 32 %. | **Confirmé** pour le corpus ENISA, pas pour tous les incidents européens. | [ENISA — communiqué de publication](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience), 22 septembre 2026. |
| Les attaques financières constituent 29,3 % des incidents et le rançongiciel 47,3 % de cette catégorie. | **Nuancé** : le communiqué et une communication ultérieure de la même agence donnent 36 % et 40 %, sans exposer clairement une réconciliation des dénominateurs. | [ENISA — communiqué](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience), 22 septembre 2026 ; [ENISA — communication du mois de la cybersécurité](https://www.enisa.europa.eu/news/cybersecurity-month-work-employees-skills-under-the-looking-glass), 30 septembre 2026. |
| Le chapitre FIMI reprend 540 cas suivis par le SEAE en 2025. | **Confirmé** pour ce corpus distinct. | [SEAE — quatrième rapport FIMI](https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf), mars 2026. |
| Les attaques DDoS ont fortement augmenté en 2025. | **Nuancé** : Cloudflare observe +121 % sur son réseau mondial ; cela ne vérifie pas une hausse de même ampleur dans toute l'UE. | [Cloudflare — bilan DDoS 2025](https://blog.cloudflare.com/ddos-threat-report-2025-q4/), 5 février 2026. |

### Contrepoints et critiques

- **Le communiqué ne reproduit pas tous les chiffres du PDF.** [ENISA — communiqué du 22 septembre 2026](https://www.enisa.europa.eu/news/exploring-the-evolution-of-the-cyber-threat-landscape-how-dependencies-weaken-our-digital-resilience) annonce **36 %** pour le cybercrime et **40 %** pour le rançongiciel au sein des activités financières, contre **29,3 %** et **47,3 %** dans le PDF examiné (p. 38). Sa [communication du 30 septembre](https://www.enisa.europa.eu/news/cybersecurity-month-work-employees-skills-under-the-looking-glass) reprend 36 % et 40 %. Un changement de définition ou de version est possible, mais non établi par ces pages. Pour toute reprise chiffrée, il faut citer explicitement le support et le dénominateur, voire demander une clarification à l'agence.
- **Le volume de la plateforme observatrice influence le résultat.** [Cloudflare — bilan du 5 février 2026](https://blog.cloudflare.com/ddos-threat-report-2025-q4/) documente les attaques mitigées sur sa propre infrastructure, tandis que le PDF ENISA agrège des signalements de plusieurs provenances. Ces séries ne valident pas mutuellement leur nombre absolu et ne doivent pas être fusionnées.

### Évolutions depuis la publication

La [communication ENISA du 30 septembre 2026](https://www.enisa.europa.eu/news/cybersecurity-month-work-employees-skills-under-the-looking-glass) prolonge la diffusion du rapport à l'occasion du mois européen de la cybersécurité. Elle réaffirme les risques d'ingénierie sociale et de rançongiciel, mais reprend aussi les proportions du communiqué qui divergent du PDF. À la date de cette recherche, les sources institutionnelles consultées n'établissent pas de correction officielle de ce décalage ; le point reste ouvert.

### Cadre juridique et éthique

- **Union européenne : NIS2.** La [directive (UE) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng), publiée le 27 décembre 2022, impose aux entités concernées des mesures de gestion du risque, incluant la sécurité de la chaîne d'approvisionnement, et des notifications d'incidents significatifs. Elle ne transforme ni une revendication de groupe en incident confirmé ni tous les événements du PDF en notifications obligatoires.
- **Attribution et vie privée.** Le [quatrième rapport FIMI du SEAE](https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf), mars 2026, signale ses nombreux cas non attribués. Une attribution publique prudente est d'autant plus nécessaire lorsque la menace concerne journalistes, ONG et victimes de logiciels espions ; les associations techniques exposées dans le PDF ne prouvent pas à elles seules une responsabilité juridique.

### Pour aller plus loin

- [ENISA — *ENISA Threat Landscape 2026*](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026), 22 septembre 2026 : page officielle donnant accès à la version publiée du rapport.
- [ENISA — *Cybersecurity Threat Landscape Methodology*](https://www.enisa.europa.eu/publications/enisa-cybersecurity-threat-landscape-methodology), mise à jour en septembre 2026 : cadre de collecte et d'analyse pour relire les statistiques.
- [ENISA — *NIS360*](https://www.enisa.europa.eu/enisa-nis360-2026), 28 mai 2026 : autre grille, centrée sur la criticité et la maturité sectorielles.
- [SEAE — *4th Report on FIMI Threats*](https://www.eeas.europa.eu/sites/default/files/2026/documents/EEAS%204th%20Threat%20Report_web.pdf), mars 2026 : corpus primaire du chapitre sur l'ingérence.
- [CISA — *Known Exploited Vulnerabilities Catalog*](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), consulté le 8 octobre 2026 : base évolutive pour prioriser les failles exploitées.
