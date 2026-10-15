---
title: "Europol et UC3M : données chiffrées captées aujourd'hui, risque de déchiffrement demain"
date: 2026-10-11
kind: analysis
theme: "cyber"
slug: "europol-et-uc3m-donnees-chiffrees-captees-aujourd-hui-risque-de-dechiffrement-demain"
organization: "Europol et Universidad Carlos III de Madrid (UC3M)"
document_type: "rapport"
source_file: "inbox/tech/Harvest-now-decrypt-later.pdf"
source_url: "https://www.europol.europa.eu/publications-events/publications/harvest-now-decrypt-later"
rubriques:
  - "cyber-menaces-cti"
  - "tech-quantique"
  - "tech-infrastructures"
tags:
  - "cryptographie post-quantique"
  - "HNDL"
  - "TLS"
  - "SSH"
  - "OpenPGP"
---

# Europol et UC3M : données chiffrées captées aujourd'hui, risque de déchiffrement demain

## Métadonnées

- **Titre original :** *Harvest now, decrypt later*.
- **Auteurs et éditeurs :** rapport conjoint d'Europol et de l'Universidad Carlos III de Madrid (UC3M), dont les deux logos figurent sur la couverture ; il est présenté comme un travail du groupe consultatif de recherche et développement lié au centre européen de lutte contre la cybercriminalité d'Europol. Aucune liste d'auteurs individuels du rapport n'est fournie (p. 1, 3, 40).
- **Publication :** 2026 ; la [notice d'Europol](https://www.europol.europa.eu/publications-events/publications/harvest-now-decrypt-later) date la mise en ligne du **7 octobre 2026**. ISBN `978-92-9414-153-8`, DOI `10.2813/1882350` imprimés p. 40.
- **Source originale :** `inbox/tech/Harvest-now-decrypt-later.pdf`, 40 pages PDF. [Version publique sur le site d'Europol](https://www.europol.europa.eu/publications-events/publications/harvest-now-decrypt-later).
- **Périmètre :** scénario de collecte actuelle de contenus chiffrés en vue d'un déchiffrement ultérieur, faisabilité selon TLS, SSH et OpenPGP, profils de cibles et mesures de migration cryptographique (p. 2-5, 16-36).
- **Nature de la preuve :** analyse technique et scénarios prospectifs ; le rapport ne présente pas une campagne HNDL avérée à grande échelle (p. 14, 35).

## Repères pour comprendre le document

La question n'est pas de savoir si un ordinateur quantique déchiffre aujourd'hui les communications courantes. Le scénario **HNDL** suppose qu'un adversaire **copie et conserve** dès maintenant le message chiffré et, pour une connexion réseau, les éléments publics de sa négociation cryptographique. Une machine quantique suffisamment puissante pourrait plus tard résoudre certains problèmes mathématiques utilisés pour établir ou envelopper la clé de session. La donnée doit encore avoir de la valeur au moment du déchiffrement. Cette description reformule les étapes posées par le rapport (p. 7-12, 16, 20, 25).

- **HNDL** — *harvest now, decrypt later*, collecte d'un contenu chiffré aujourd'hui pour tenter de le déchiffrer dans le futur, avec une avancée quantique ou cryptanalytique (p. 11-12).
- **Chiffrement asymétrique** — mécanismes à clé publique et clé privée, employés notamment pour l'échange de clés ou les signatures ; RSA et certains schémas sur courbes elliptiques sont visés par la menace quantique décrite ici (p. 7-9, 37).
- **Chiffrement symétrique** — même secret utilisé pour protéger et retrouver le contenu ; AES sert à chiffrer les données après l'établissement d'une clé de session (p. 7-8, 16, 39).
- **Échange de clés / *handshake*** — messages initiaux par lesquels deux parties s'authentifient et établissent les secrets d'une connexion TLS ou SSH ; leur capture peut être nécessaire à une attaque HNDL sur ce trafic (p. 16-18, 20, 23).
- **Diffie–Hellman éphémère (DHE/ECDHE)** — accord de secret avec de nouvelles valeurs pour chaque négociation ; l'exposition ultérieure de la clé d'identité du serveur ne suffit pas à retrouver les anciennes clés de session (p. 16, 20, 23).
- **Confidentialité persistante / *forward secrecy*** — protection des anciennes sessions contre la compromission future d'une clé d'identité durable ; elle ne garantit pas la résistance au calcul quantique si l'échange éphémère classique est lui-même cassé (p. 20-24, 37-38).
- **TLS et SSH** — protocoles de protection de connexions web et de connexions d'administration ou de transfert de fichiers, respectivement ; ils ont des mécanismes de renégociation différents (p. 16-18, 22-24).
- **OpenPGP** — format et écosystème pour chiffrer notamment courriels et fichiers : une clé symétrique aléatoire chiffre le contenu, puis une clé publique protège cette clé de session pour chaque destinataire (p. 19, 25, 38).
- **KEM / ML-KEM** — mécanisme d'encapsulation permettant d'établir un secret partagé ; ML-KEM est la famille post-quantique citée comme solution de migration (p. 28-29, 33, 38).
- **Échange hybride** — combinaison d'un mécanisme classique et d'un mécanisme post-quantique pour dériver un secret ; sa sécurité visée subsiste si au moins une composante demeure sûre, sous réserve d'une construction correcte (p. 33).
- **Crypto-agilité** — capacité d'une organisation à repérer puis remplacer algorithmes, paramètres, clés et certificats sans refondre tous ses systèmes à chaque changement (p. 32).
- **Horizon de confidentialité** — durée pendant laquelle une information doit rester secrète ; c'est le facteur de priorité qui rend certaines archives beaucoup plus exposées que des données vite périmées (p. 11, 30, 32).

## Résumé exécutif

Europol et UC3M examinent un risque à **deux échéances** : un adversaire peut copier maintenant des communications ou fichiers chiffrés, puis tenter de les lire après une percée quantique ou cryptanalytique. Il n'a donc pas besoin d'un ordinateur quantique au moment de la collecte. Le risque dépend toutefois de trois conditions cumulées : **capture suffisante**, **capacité future de casser la protection pertinente** et **valeur persistante** des données au moment de la lecture (p. 3-4, 11-12, 35).

L'apport principal est de distinguer les protocoles. Une connexion **TLS 1.2 avec transport de clé RSA** peut exposer de nombreuses sessions enregistrées si une seule clé durable du serveur est ensuite compromise. **TLS 1.3 et SSH avec Diffie–Hellman éphémère** résistent à cette seule compromission, mais un adversaire quantique capable de résoudre les échanges enregistrés pourrait attaquer chaque session. Dans **OpenPGP**, le message archivé contient la clé symétrique de contenu enveloppée pour le destinataire ; casser ultérieurement la clé publique asymétrique du destinataire peut donc révéler le passé (p. 19-25).

Le rapport classe le risque de **faible à moyen** pour les particuliers, **moyen à élevé** pour les entreprises et **élevé** pour les décideurs publics. Ce sont des appréciations de risque, pas des fréquences d'attaques mesurées. Les auteurs préconisent d'identifier les données qui doivent rester secrètes longtemps, de supprimer les copies inutiles, d'abandonner les configurations obsolètes et de déployer progressivement la cryptographie post-quantique, si possible sous forme hybride (p. 4-5, 27-33, 35-36).

La nuance décisive est empirique : le rapport qualifie HNDL de **menace techniquement crédible**, mais indique **ne pas disposer de preuve claire d'une exploitation systématique à grande échelle**. Ses exemples d'espionnage et de rançongiciel montrent que la collecte et la conservation de données sont possibles, sans démontrer une intention de déchiffrement quantique ultérieur. Une migration débutée après la capture ne réparera pas les copies déjà détenues par un adversaire (p. 13-14, 27-28, 35 ; dernière phrase : inférence de l'analyse).

## Chronologie

Le décalage entre la durée de vie des secrets et celle d'une migration explique le calendrier du rapport.

1. **1994-1996 :** le document rappelle les algorithmes de Shor puis de Grover, pour distinguer la vulnérabilité de la cryptographie à clé publique de l'affaiblissement plus limité de la recherche de clés symétriques (p. 8).
2. **Avril 2022 :** il cite OpenSSH 9.0 comme jalon d'adoption d'un échange hybride dans un logiciel répandu (p. 33).
3. **Novembre 2024 :** il reprend le projet NIST IR 8547 pour situer des horizons de transition, notamment 2030 et 2035 ; il ne donne pas une date certaine d'arrivée d'un ordinateur quantique cryptographiquement pertinent (p. 9).
4. **Juin 2025 :** il renvoie à la feuille de route coordonnée de l'Union européenne sur la migration post-quantique (p. 9, 32).
5. **Mars 2026 :** le rapport fonde sa comparaison technique des protocoles sur l'étude *On the Practical Feasibility of Harvest-Now, Decrypt-Later Attacks* (p. 16, 21).
6. **Octobre 2026 :** publication du rapport selon la notice officielle d'Europol ; il recommande d'engager dès maintenant les inventaires et tests, avant que la capacité de déchiffrement hypothétique n'existe (p. 27, 32, 35-36).

## Thèse principale

Le texte est une **analyse de faisabilité assortie d'un appel à la préparation**. Son raisonnement n'exige ni de prédire la date d'un ordinateur quantique utile à l'attaque, ni de supposer que toutes les données intéressent un adversaire. Si une donnée doit rester secrète plus longtemps que le temps nécessaire à la migration et que l'horizon d'arrivée d'une capacité de rupture est incertain, reporter la transition peut déjà laisser une fenêtre de capture exploitable (p. 9, 11, 30, 32).

Europol et UC3M modulent ce risque selon les protocoles, les clés et le coût d'attaque. Ils ne soutiennent pas qu'AES serait directement cassé comme RSA, ni que l'usage de TLS 1.3 suffirait à rendre des archives « post-quantiques ». La thèse générale devient plus convaincante pour les secrets de longue durée et les cibles de haute valeur que pour tout trafic Internet indifférencié (p. 8, 20-25, 35).

## Informations et arguments importants

### La chaîne d'attaque et ce qui constitue une preuve

Le scénario comprend quatre étapes : **collecter** trafic ou fichiers chiffrés, **les stocker**, **attendre** une capacité de cryptanalyse, puis **déchiffrer et exploiter**. Pour TLS ou SSH, l'adversaire doit notamment avoir gardé les valeurs publiques de l'échange de clés avec le trafic chiffré ; pour OpenPGP, le fichier chiffré et le paquet contenant la clé de session enveloppée sont centraux. Le volume de collecte et le temps de stockage peuvent être importants, surtout si chaque session exige son propre calcul futur (p. 11-12, 20-25, 35).

Les auteurs évoquent des intérêts plausibles : secrets d'État, dossiers d'enquête et identités d'informateurs, dossiers médicaux, secrets industriels ou contrats. Leur matrice de risque par parties prenantes exprime une **priorisation qualitative**. Elle ne mesure ni le nombre d'adversaires en train d'archiver du trafic, ni la part des archives lisibles dans le futur (p. 4, 13, 35).

Le cas des rançongiciels requiert une lecture stricte. Le rapport décrit l'exfiltration, la conservation et la réutilisation de données dans certaines extorsions, puis indique que cette pratique **pourrait** inclure une composante HNDL. Il précise qu'aucun cas spécifique largement documenté ne permet de prouver cette intention, et conclut à l'absence de preuve claire d'un déploiement systématique à grande échelle (p. 13-14, 35).

### TLS : la configuration compte davantage que le seul numéro de version

Avec **TLS 1.2 et un échange sans confidentialité persistante**, notamment le transport de clé RSA examiné dans le texte, la compromission ultérieure d'une clé durable peut ouvrir les anciennes sessions captées avec cette clé. Avec **DHE/ECDHE**, la clé du certificat ne donne pas à elle seule le secret d'une session passée ; il faut s'attaquer séparément aux échanges éphémères. **TLS 1.3** retire le transport de clé RSA des négociations complètes. Dans le cas de l'échange complet (EC)DHE étudié par le rapport, cela limite le rendement d'une seule compromission de clé durable ; les reprises avec secret prépartagé doivent être évaluées séparément (p. 20-22, 27).

Cette amélioration est **classique, pas post-quantique**. Si les valeurs publiques DHE/ECDHE ont été enregistrées, une machine quantique suffisamment puissante pourrait en principe retrouver les secrets des sessions sélectionnées. Les reprises de session avec secret prépartagé, le mode **0-RTT** et les mises à jour de clés TLS 1.3 demandent une analyse distincte : dans le scénario décrit, certaines clés restent dérivées d'un échange initial compromis. Le rapport souligne également que 0-RTT ne procure pas la même confidentialité persistante aux données précoces (p. 21-22, 27).

Les versions **TLS 1.0 et 1.1** sont traitées comme obsolètes et porteuses de problèmes immédiats de sécurité. Leur retrait est une mesure de réduction du risque actuel ; il ne doit pas être présenté comme la solution définitive à HNDL pour TLS 1.2/1.3 avec échange classique (p. 21, 27, 35).

### SSH et OpenPGP : deux formes différentes d'exposition du passé

Dans **SSH moderne**, la clé d'hôte sert à authentifier le serveur mais ne chiffre pas elle-même le secret de session. Voler plus tard cette clé ne déchiffre donc pas directement des enregistrements antérieurs. En revanche, un futur calcul quantique appliqué à l'échange DH/ECDH archivé pourrait retrouver le secret. Une renégociation SSH réalise un **nouvel échange** ; un adversaire qui veut lire toute la session doit casser aussi les échanges enregistrés après chaque changement de clé. Le rapport oppose ce comportement à une simple mise à jour de clé TLS 1.3 dérivée d'un secret antérieur (p. 23-24).

Dans **OpenPGP**, une clé de contenu symétrique aléatoire protège le message et se trouve elle-même chiffrée pour chaque destinataire. Une copie du message inclut donc le matériel à attaquer plus tard. L'obtention future de la clé privée d'un destinataire, par vol ou par résolution quantique du problème lié à sa clé publique classique, peut révéler les messages archivés pour lui. La phrase de passe d'une clé privée volée est un obstacle supplémentaire au vol de ce fichier ; elle ne neutralise pas un calcul de clé privée à partir d'une clé publique vulnérable (p. 19, 25).

Cette vulnérabilité ne se généralise pas sans examen à **tout stockage AES**. Le cas démontré par le rapport est celui d'une clé symétrique enveloppée sous une clé publique vulnérable ou d'une clé privée compromise ; un fichier chiffré directement avec une clé symétrique indépendante présente un autre modèle de menace (p. 19, 25 ; inférence de l'analyse).

### Mesures immédiates et migration post-quantique

Le rapport distingue protection de court terme et protection de long terme. Il propose d'abord l'inventaire des usages cryptographiques, des certificats et des données dont la confidentialité doit durer ; ensuite, la suppression des données inutiles, le durcissement des clés, le retrait des protocoles obsolètes et les tests d'interopérabilité ; enfin, une migration progressive vers des échanges et enveloppements post-quantiques, éventuellement **hybrides**. Pour les cibles les plus sensibles, il recommande des pilotes sur les systèmes critiques avant généralisation (p. 4-5, 27-33, 35-36).

La règle d'urgence reprise par les auteurs est **X + Y > Z** : durée pendant laquelle les données doivent rester secrètes (**X**), délai de migration (**Y**), délai avant une machine quantique capable de casser la cryptographie pertinente (**Z**). Si les deux premières durées excèdent la troisième, attendre expose potentiellement les données déjà échangées. Cette règle structure les décisions malgré l'incertitude sur **Z** ; elle ne prédit pas une date précise (p. 30).

La confidentialité persistante classique et la rotation des clés **augmentent le coût** d'une attaque ou réduisent d'autres risques ; elles ne rendent pas intouchable une copie déjà captée. De même, rechiffrer un ancien fichier dans son propre dépôt protège sa copie actuelle, mais ne supprime pas l'ancienne version que l'adversaire aurait déjà archivée. Cette dernière conséquence découle directement du modèle de collecte du rapport et doit guider la priorisation des archives existantes (p. 11-12, 20-22, 27-28 ; inférence de l'analyse).

## Points particulièrement intéressants pour la veille

La veille utile porte autant sur les **conditions de déploiement** que sur les annonces de capacités quantiques.

- **Valeur durable des données.** Le rapport fait de la durée de confidentialité le premier critère de risque. *Inférence pour la veille :* suivre les secteurs qui conservent longtemps dossiers de santé, archives judiciaires, secrets industriels ou communications diplomatiques, plutôt que classer tout trafic chiffré au même niveau (p. 4, 11, 30, 32).
- **Inventaire des modes TLS.** Le même numéro de version TLS 1.2 couvre des échanges à exposition très différente. *Inférence pour la veille :* documenter les échanges de clés effectivement négociés, les reprises de session et les dépendances matérielles avant de fixer l'ordre de migration (p. 20-22, 27).
- **Confidentialité persistante insuffisante seule.** Elle réduit le rendement d'une clé durable compromise, mais les échanges éphémères classiques restent un objet d'attaque quantique future. *Inférence pour la veille :* éviter de présenter TLS 1.3 ou SSH2 comme « quantum-safe » sans mécanisme adapté (p. 21-24, 27).
- **Preuve de menace.** Les auteurs distinguent faisabilité et activité observée. *Inférence pour la veille :* demander, pour chaque cas invoqué, si le contenu capté était déjà lisible, s'il était chiffré sous clé publique vulnérable et si une intention de déchiffrement différé est établie (p. 13-14, 35).
- **Migration des archives.** Le stockage durable et les copies externes compliquent la remédiation après capture. *Inférence pour la veille :* suivre les capacités concrètes de rechiffrement, d'effacement et de limitation de conservation, ainsi que les essais hybrides interopérables (p. 25, 28, 32-33).

## Faits, opinions et interprétations

### Faits rapportés par la source

Le document décrit la structure des échanges TLS et SSH et celle des messages OpenPGP, avec des scénarios de capture et de reconstruction de clés. Il affirme que TLS 1.2 peut employer soit un mode sans confidentialité persistante, soit DHE/ECDHE ; il analyse les échanges éphémères de TLS 1.3 et SSH, ainsi que les reprises TLS avec secret prépartagé ; et il explique que le paquet OpenPGP contient une clé de session enveloppée pour chaque destinataire. Sa propre conclusion dit qu'**aucune preuve claire** d'exploitation systématique HNDL à grande échelle n'est disponible (p. 16-25, 35).

### Opinions ou positions de l'auteur

Europol et UC3M jugent la menace « réelle » et préconisent une transition engagée immédiatement pour les secrets durables. Ils qualifient les risques par catégories de parties prenantes et estiment que les coûts actuels concentrent la menace sur les cibles à forte valeur. Le calendrier de l'ordinateur quantique pertinent et la future économie des attaques demeurent incertains ; la matrice de risque est un jugement d'experts, non un résultat d'enquête sur la fréquence des collectes (p. 4-5, 9, 35-36).

### Interprétations et inférences

L'analyse retient que **l'étape de capture rend le risque irréversible pour la copie volée** : une migration ultérieure améliore les nouvelles communications mais ne restaure pas la confidentialité d'un trafic déjà conservé par un tiers. Elle retient aussi qu'il faut distinguer **l'établissement de clé**, **l'authentification** et **le chiffrement symétrique**. Casser une signature classique dans le futur n'implique pas automatiquement le déchiffrement d'une ancienne session bénéficiant de confidentialité persistante ; casser l'échange éphémère enregistré, en revanche, peut le permettre (p. 16-25, 27-28).

## Limites et points à vérifier

1. **Absence de cas attribué.** Les scénarios d'espionnage et de rançongiciel illustrent une capacité de collecte, mais les auteurs ne présentent pas de dossier prouvant une stratégie HNDL quantique effectivement conduite ; ils reconnaissent l'absence de preuve claire d'exploitation systématique (p. 13-14, 35).
2. **Calendrier incertain.** Aucun horizon de disponibilité d'une machine quantique capable de casser les clés concernées n'est établi. La règle X + Y > Z aide à planifier, mais **Z** est une hypothèse variable (p. 9, 30).
3. **Coût et ciblage.** Le rapport invoque de gros volumes de collecte, stockage et calcul sans donner, pour chaque configuration, un budget d'attaque ou une probabilité de ciblage vérifiable. La hiérarchie des parties prenantes reste qualitative (p. 4, 13, 35).
4. **Périmètre technique.** Les cas approfondis sont TLS, SSH et OpenPGP ; la sécurité de chaque VPN, base de données ou sauvegarde dépend de son enveloppement concret de clés, absent de cette démonstration (p. 16, 19, 31-32).
5. **Copies déjà captées.** La rotation et le rechiffrement proposés pour les fichiers réduisent l'exposition de copies contrôlées par l'organisation, mais ne protègent pas rétroactivement une ancienne copie détenue par un adversaire (p. 11-12, 25, 28 ; inférence de l'analyse).
6. **Confusion possible entre RSA et transport de clé RSA.** Le danger de déchiffrement rétrospectif de TLS 1.2 décrit p. 20-22 concerne en particulier le **transport de clé RSA sans confidentialité persistante**. Une clé RSA utilisée seulement pour authentifier un échange DHE/ECDHE n'a pas le même effet sur les anciens contenus ; la recommandation générale p. 27 de désactiver « RSA » doit être lue à la lumière de cette distinction.
7. **Statut des références normatives.** Le rapport reprend des échéances du **projet** NIST IR 8547 et renvoie, pour TLS hybride, à un brouillon IETF daté de mai 2026. Leur statut précis à la date de publication doit être vérifié avant de les présenter comme des normes finales ou comme le dernier état des travaux (p. 9, 33).

## Sources et références mentionnées

La bibliographie mêle le **préprint technique de Blanco-Romero et collègues** sur la faisabilité HNDL, les spécifications TLS et SSH de l'IETF, les standards et projets du **NIST**, la feuille de route de la **Commission européenne**, des notes d'**Europol** sur le quantique, et les logiciels ou bibliothèques d'implémentation cités pour la migration. Ces références étayent surtout la **possibilité technique** et les choix de transition. Le rapport ne cite pas une enquête publique documentant une campagne HNDL quantique observée (p. 3, 9, 16-18, 21, 31-33, 35).

## Cinq éléments essentiels à retenir

1. **HNDL commence avant l'ordinateur quantique** : l'adversaire doit d'abord conserver une copie exploitable du trafic ou du fichier chiffré (p. 11-12, 20, 25).
2. **TLS 1.2 avec transport RSA** expose plusieurs anciennes sessions à une clé durable compromise ; **TLS 1.3 et SSH avec échange éphémère** demandent en principe une attaque sur chaque échange enregistré (p. 20-24).
3. **La confidentialité persistante classique ne suffit pas contre Shor** appliqué plus tard aux échanges DH/ECDH capturés ; le chiffrement symétrique n'est pas visé de la même manière (p. 8, 21-24).
4. **OpenPGP** peut exposer d'anciens messages si la clé publique classique d'un destinataire permet un jour de retrouver la clé de contenu enveloppée (p. 19, 25).
5. **Faisabilité n'est pas observation** : le rapport juge le risque crédible mais ne documente pas d'exploitation systématique avérée ; la priorité opérationnelle dépend de la durée de vie des secrets et du temps de migration (p. 30, 35-36).

## État de l'art et regards extérieurs

Recherches effectuées le **2026-10-11**. Les informations ci-dessous viennent de sources publiques vérifiées et servent à situer ou corriger le rapport ; elles ne modifient pas les sections précédentes, fondées sur la seule source analysée.

### Travaux de référence

- **Étude technique sous-jacente.** [Blanco-Romero et collègues — « On the Practical Feasibility of Harvest-Now, Decrypt-Later Attacks »](https://arxiv.org/abs/2603.01091), prépublication du **1er mars 2026**, modélise les coûts de stockage et de calcul pour TLS, QUIC et SSH avec un banc de simulation ouvert. Elle éclaire le coût relatif des configurations, sans constituer une preuve d'une campagne HNDL observée.
- **Norme cryptographique.** [NIST — FIPS 203, ML-KEM](https://csrc.nist.gov/pubs/fips/203/final), finale le **13 août 2024**, définit un mécanisme d'encapsulation de clé post-quantique. [FIPS 204, ML-DSA](https://csrc.nist.gov/pubs/fips/204/final), publiée le même jour, concerne les **signatures** : son rôle n'est pas interchangeable avec celui de ML-KEM pour protéger la confidentialité des anciennes sessions.
- **Norme de protocole.** [IETF — RFC 9846, TLS 1.3](https://www.rfc-editor.org/info/rfc9846/), **juillet 2026**, remplace la RFC 8446 sans changer le numéro de version TLS. Elle distingue notamment les garanties du trafic normal et celles des données précoces **0-RTT**, qui n'ont pas la même confidentialité persistante.

### Compléments sur le sujet

La réponse au risque HNDL dépend autant de l'inventaire réel des systèmes que de la sélection d'un algorithme. Les sources suivantes précisent les horizons institutionnels, les constructions disponibles et les contraintes que la simple formule « passer à la PQC » ne résout pas.

- **Priorités européennes.** La [feuille de route coordonnée de l'UE](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography), **23 juin 2025**, est décrite par la [Commission](https://digital-strategy.ec.europa.eu/en/policies/post-quantum-cryptography) comme demandant aux États membres de **commencer la transition d'ici fin 2026** et de protéger les usages à haut risque **au plus tard fin 2030**. Ce sont des jalons de politique de migration, pas des dates prédites pour une rupture quantique.
- **Priorisation française.** [ANSSI — « Analyse de risque chiffrement et cryptographie »](https://cyber.gouv.fr/nous-connaitre/publications/analyse-de-risque-sectorielle-et-technique/analyse-de-risque-chiffrement-et-cryptographie/), **27 mai 2026**, propose un classement des risques et impacts métiers à destination d'organisations non spécialistes. Son intérêt est de lier criticité des données, durée de protection et usages cryptographiques au lieu de décider sur le seul nom d'un protocole.
- **Hybridation prudente.** Dans sa [FAQ PQC](https://cyber.gouv.fr/enjeux-technologiques/cryptographie-post-quantique/faq-pqc/), consultée le **11 octobre 2026**, l'ANSSI recommande l'hybridation lorsque la protection doit durer au-delà de 2030 ; elle indique aussi que ses préconisations PQC ne sont pas, en elles-mêmes, une obligation réglementaire générale. Le risque de régression et l'interopérabilité restent des points de validation.
- **TLS hybride devenu spécifié.** [IETF — RFC 9954](https://www.rfc-editor.org/info/rfc9954/), **juillet 2026**, formalise une construction pour combiner des secrets dans TLS 1.3. [RFC 10024](https://www.rfc-editor.org/info/rfc10024/), **août 2026**, définit trois groupes concrets combinant **ECDHE et ML-KEM**, dont X25519MLKEM768. Une spécification publiée ne prouve pas que tous les clients, serveurs, équipements intermédiaires et partenaires l'utilisent déjà.
- **Horizon scientifique.** Le [NIST — « What Is Post-Quantum Cryptography? »](https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography), consulté le **11 octobre 2026**, indique qu'aucun calendrier fiable ne permet de prédire l'arrivée d'une machine quantique cryptographiquement pertinente. La préparation aujourd'hui répond à la durée de vie des secrets et des migrations.
- **Des estimations de ressources qui baissent vite.** Le rapport ne mentionne pas les travaux qui ont le plus fait bouger le terme **Z** de sa règle. [Craig Gidney (Google Quantum AI), 21 mai 2025](https://arxiv.org/abs/2505.15917), estime qu'une clé **RSA-2048** pourrait être factorisée en moins d'une semaine avec **moins d'un million de qubits physiques** bruités, contre environ 20 millions dans son estimation de 2019. Le [livre blanc de Google Quantum AI du 30 mars 2026](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf) applique le même exercice aux courbes elliptiques de 256 bits : **moins de 500 000 qubits physiques** et quelques dizaines de minutes de calcul sur une architecture supraconductrice. Ce sont des **estimations pour des machines qui n'existent pas**, fondées sur des hypothèses matérielles explicites ; elles ne datent pas l'arrivée d'une telle machine. Elles montrent toutefois que le seuil à franchir recule à mesure que les algorithmes s'améliorent, ce qui renforce l'argument d'Europol pour les secrets à longue durée de vie.

### Vérification des affirmations de la source

| Affirmation ou point à contrôler | Verdict | Source de la vérification |
| --- | --- | --- |
| La menace HNDL est techniquement plausible mais son exploitation systématique à grande échelle n'est pas démontrée. | **Confirmé pour la plausibilité ; non établi pour l'activité réelle** | [Préprint de Blanco-Romero et collègues](https://arxiv.org/abs/2603.01091), **1er mars 2026**, simule l'attaque et ses coûts ; il ne documente pas une campagne opérationnelle attribuée. |
| Une clé TLS 1.3 durable compromise ne suffit pas à relire d'anciennes sessions à échange éphémère ; 0-RTT a des garanties plus faibles. | **Confirmé, sous conditions de configuration** | [IETF — RFC 9846](https://www.rfc-editor.org/info/rfc9846/), **juillet 2026**, distingue échange de clés, reprises de session et 0-RTT ; elle remplace la RFC 8446. |
| ML-KEM et ML-DSA sont des standards post-quantiques disponibles. | **Confirmé, rôles distincts** | [NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) et [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), **13 août 2024** : établissement de secret pour le premier, signature pour le second. |
| Les échéances 2030/2035 reprises du NIST IR 8547 relèvent-elles d'une norme définitive ? | **Non : projet** | [NIST — IR 8547](https://csrc.nist.gov/pubs/ir/8547/ipd), **12 novembre 2024**, est marqué **Initial Public Draft** à la date de vérification ; ses échéances doivent être attribuées à ce projet. |
| L'IETF développe encore seulement un brouillon de construction TLS hybride. | **Dépassé lors de la publication du rapport** | [RFC 9954](https://www.rfc-editor.org/info/rfc9954/) de **juillet 2026** et [RFC 10024](https://www.rfc-editor.org/info/rfc10024/) d'**août 2026** avaient déjà été publiées avant le 7 octobre 2026. |
| TLS 1.3 seul rend-il les anciennes communications sûres face à une attaque quantique future ? | **Non, et le rapport le reconnaît** | [Préprint technique](https://arxiv.org/abs/2603.01091), **1er mars 2026**, et [RFC 9954](https://www.rfc-editor.org/info/rfc9954/), **juillet 2026** : un échange ECDHE classique enregistré demeure le point d'exposition ; le rapport lui-même le reconnaît p. 21-22. |

### Contrepoints et critiques

- **Le préprint précise l'économie de l'attaque.** [Blanco-Romero et collègues](https://arxiv.org/abs/2603.01091), **1er mars 2026**, avancent que la conservation du trafic peut être économiquement plus simple que son déchiffrement futur et que les paramètres de renégociation déplacent le coût du côté du calcul quantique. Leur modèle apporte un cadre de comparaison, mais ses hypothèses sur les budgets et machines futurs ne sont pas des observations d'adversaires.
- **La protection hybride ne se résume pas au nom d'un algorithme.** [ANSSI — FAQ PQC](https://cyber.gouv.fr/enjeux-technologiques/cryptographie-post-quantique/faq-pqc/), consultée le **11 octobre 2026**, et [RFC 10024](https://www.rfc-editor.org/info/rfc10024/), **août 2026**, montrent que la construction, la robustesse des deux composantes, les tailles de messages, les certificats et l'interopérabilité comptent autant que l'annonce « ML-KEM activé ».
- **Une réponse prospective doit éviter une fausse certitude.** Le [NIST](https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography), consulté le **11 octobre 2026**, ne date pas l'arrivée d'une machine capable de casser les clés actuelles. La priorité d'un système résulte donc d'un horizon de confidentialité, d'un temps de migration et d'une exposition à la capture, pas d'une année prédite avec précision.

### Évolutions depuis la publication

La recherche menée **quatre jours après** la publication du 7 octobre 2026 n'a pas identifié de fait nouveau qui modifie le bilan d'Europol. Le décalage vérifiable est **antérieur à la publication** : le texte parle encore d'un brouillon IETF pour TLS hybride alors que les [RFC 9954](https://www.rfc-editor.org/info/rfc9954/) (**juillet 2026**) et [10024](https://www.rfc-editor.org/info/rfc10024/) (**août 2026**) étaient déjà publiées. La [RFC 9846](https://www.rfc-editor.org/info/rfc9846/), **juillet 2026**, avait également remplacé la spécification générale TLS 1.3 de 2018. Ces mises à jour du statut normatif ne prouvent pas une adoption opérationnelle généralisée.

### Cadre juridique et éthique

- **Union européenne.** La [recommandation (UE) 2024/1101](https://eur-lex.europa.eu/eli/reco/2024/1101/oj/eng), **11 avril 2024**, invite à une feuille de route coordonnée de migration post-quantique. Sa nature de **recommandation** et la [feuille de route publiée le 23 juin 2025](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) ne doivent pas être présentées comme une obligation uniforme de déployer partout ML-KEM dès aujourd'hui.
- **Protection des données et conservation.** La collecte massive de trafic par un attaquant serait une atteinte à la confidentialité ; l'analyse privilégie la minimisation, la maîtrise des durées de conservation et la protection des clés. Les recommandations techniques d'Europol ne dispensent pas chaque organisation d'évaluer les obligations applicables à ses propres données et services (p. 32 ; conséquence pratique, sans prétendre trancher un régime juridique particulier).

### Pour aller plus loin

- [Europol — rapport original « Harvest now, decrypt later »](https://www.europol.europa.eu/publications-events/publications/harvest-now-decrypt-later), **7 octobre 2026** : scénarios détaillés et figures de protocoles.
- [Blanco-Romero et collègues — étude de faisabilité HNDL](https://arxiv.org/abs/2603.01091), **1er mars 2026** : coûts et banc de simulation sous-jacents.
- [NIST — FIPS 203, ML-KEM](https://csrc.nist.gov/pubs/fips/203/final), **13 août 2024** : spécification du mécanisme d'établissement post-quantique.
- [IETF — RFC 10024](https://www.rfc-editor.org/info/rfc10024/), **août 2026** : trois groupes hybrides concrets pour TLS 1.3.
- [ANSSI — analyse de risque chiffrement et cryptographie](https://cyber.gouv.fr/nous-connaitre/publications/analyse-de-risque-sectorielle-et-technique/analyse-de-risque-chiffrement-et-cryptographie/), **27 mai 2026** : méthode de priorisation destinée aux organisations.
