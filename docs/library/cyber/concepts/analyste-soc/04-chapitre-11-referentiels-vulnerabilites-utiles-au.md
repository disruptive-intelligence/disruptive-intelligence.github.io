---
title: Chapitre 11 — Référentiels vulnérabilités utiles au SOC
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

CVE, CWE, CVSS, EPSS, KEV**

_Quand une alerte, un IOC ou un bulletin CTI mentionne une vulnérabilité, l’analyste SOC doit savoir exactement de quoi on parle. Ce chapitre pose les repères indispensables pour lire correctement une vulnérabilité, comprendre son niveau de risque réel, et l’intégrer dans la qualification d’incident sans confondre sévérité technique et gravité opérationnelle._

Ce chapitre s’intègre bien ici parce que ton cours passe, en Partie III, des **principes d’investigation** vers les **méthodes d’analyse et de qualification**. Il prépare naturellement le futur chapitre sur **CVSS v4 et le rescoring contextuel**, sans casser la logique des chapitres techniques d’investigation par domaine.

---


## **11.1 Pourquoi ce vocabulaire compte pour le SOC**


### Idée directrice

Avant même de parler de scoring, il faut éviter la confusion classique :

- une **CVE** n’est pas un score ;
- une **CWE** n’est pas une vulnérabilité exploitée ;
- un **CVSS** ne dit pas si l’incident est grave pour l’organisation ;
- un **EPSS** n’est pas une preuve d’exploitation ;
- une présence en **KEV** change fortement la lecture opérationnelle.


### Ce que tu peux développer

- En SOC, ces sigles apparaissent partout : alertes scanner, bulletins CERT, rapports CTI, tickets patching, rapports éditeurs, EDR, SIEM.
- Le problème n’est pas seulement de les connaître, mais de **savoir à quoi ils servent dans une décision opérationnelle**.
- Une mauvaise lecture peut conduire à deux erreurs :
    - sur-réagir à une vulnérabilité “critique” mais peu exploitable chez toi ;
    - sous-réagir à une vulnérabilité au score moyen mais activement exploitée.


### Message clé

**Le SOC ne lit pas une vulnérabilité pour faire de la théorie ; il la lit pour décider quoi investiguer, quoi escalader, et quoi prioriser.**

---


## **11.2 CVE — identifier précisément la vulnérabilité**


### Objectif

Expliquer la CVE comme **identifiant normalisé** d’une vulnérabilité.


### À couvrir

- Définition simple : une **CVE** est un identifiant unique attribué à une vulnérabilité connue.
- Exemple de format : `CVE-2025-XXXX`.
- Ce que permet une CVE :
    - parler tous de la même vulnérabilité ;
    - retrouver les bulletins éditeurs, NVD, CTI, règles de détection, IoC, PoC.
- Ce que **n’est pas** une CVE :
    - ce n’est pas un score ;
    - ce n’est pas une preuve d’exploitation ;
    - ce n’est pas une mesure de gravité.


### Angle SOC

Quand une alerte ou un bulletin mentionne une CVE, l’analyste doit pouvoir répondre :

- quel produit est concerné ;
- quelle version ;
- quel vecteur d’exploitation ;
- quels systèmes internes sont potentiellement exposés.


### Transition possible

> La CVE dit **de quelle vulnérabilité on parle**. Elle ne dit pas encore **pourquoi elle existe** ni **à quel point elle est dangereuse chez nous**.

---


## **11.3 CWE — comprendre la faiblesse sous-jacente**


### Objectif

Montrer que la CWE sert à comprendre la **nature du défaut** derrière la vulnérabilité.


### À couvrir

- Définition simple : une **CWE** décrit une **catégorie de faiblesse** logicielle ou de conception.
- Exemples : injection, contrôle d’accès défaillant, désérialisation, use-after-free, buffer overflow.
- Différence CVE / CWE :
    - **CVE** = instance précise d’une vulnérabilité ;
    - **CWE** = type de faiblesse plus général.


### Angle SOC

- Pour l’analyste SOC, la CWE aide à :
    - comprendre la logique d’exploitation ;
    - anticiper les artefacts à rechercher ;
    - généraliser le raisonnement à d’autres cas similaires.
- Exemple pédagogique :
    - plusieurs CVE différentes peuvent renvoyer à une même famille de faiblesse ;
    - donc plusieurs incidents distincts peuvent laisser des traces comparables.


### Message clé

**La CVE nomme le cas ; la CWE aide à comprendre le mécanisme.**

---


## **11.4 CVSS — mesurer la sévérité technique**


### Objectif

Présenter CVSS comme un **score de sévérité**, pas comme un verdict opérationnel absolu.


### À couvrir

- Définition simple : le **CVSS** sert à estimer la sévérité technique d’une vulnérabilité.
- Rappeler que le score externe est souvent le point de départ d’une lecture plus contextuelle.
- Tu peux introduire brièvement les idées suivantes sans entrer encore dans tout le détail v4 :
    - facilité d’exploitation ;
    - privilèges requis ;
    - interaction utilisateur ;
    - impact sur confidentialité, intégrité, disponibilité.


### Angle SOC

- Le CVSS aide à prioriser, mais ne suffit pas à lui seul.
- En investigation, il éclaire l’analyste sur le **potentiel technique** d’une vulnérabilité.
- Mais il ne remplace ni :
    - l’état réel de compromission ;
    - la criticité de l’actif ;
    - l’impact métier ;
    - la propagation observée.


### Message clé

**CVSS répond à “à quel point cette vulnérabilité est sévère techniquement ?”, pas à “à quel point l’incident est grave pour nous ?”**

Cette distinction est d’ailleurs exactement la logique du texte d’ajout CVSS v4 : séparer la **gravité IR de l’incident** de la **sévérité de la vulnérabilité**, puis utiliser le rescoring contextuel pour éclairer la décision.

---


## **11.5 EPSS — estimer la probabilité d’exploitation**


### Objectif

Introduire EPSS comme complément très utile au CVSS.


### À couvrir

- Définition simple : **EPSS** estime la probabilité qu’une vulnérabilité soit exploitée dans un horizon proche.
- Expliquer l’intérêt pratique :
    - deux vulnérabilités peuvent avoir un CVSS proche ;
    - mais une seule peut avoir une forte probabilité d’exploitation réelle.
- EPSS apporte une lecture plus dynamique, plus orientée menace.


### Angle SOC

- Très utile pour :
    - prioriser le hunting ;
    - prioriser la surveillance ;
    - appuyer les décisions de traitement rapide ;
    - distinguer la vulnérabilité “grave sur le papier” de celle qui risque de générer un incident demain matin.
- Important à préciser :
    - EPSS n’est **pas** une preuve que la vulnérabilité est déjà exploitée dans ton SI ;
    - c’est un indicateur de **probabilité**, pas un constat.


### Message clé

**CVSS regarde surtout la sévérité technique ; EPSS aide à regarder la vraisemblance d’exploitation.**

---


## **11.6 KEV — savoir si la menace est déjà réelle**


### Objectif

Montrer pourquoi la KEV a une valeur opérationnelle très forte pour le SOC.


### À couvrir

- Définition simple : une vulnérabilité présente en **KEV** est une vulnérabilité **connue comme exploitée dans le monde réel**.
- Là, on n’est plus dans l’hypothèse théorique, mais dans la menace observée.


### Angle SOC

- Si une CVE apparaît en KEV :
    - la vigilance monte immédiatement ;
    - le hunting devient prioritaire ;
    - la remédiation prend une autre urgence ;
    - la qualification d’une alerte liée à cette CVE change de ton.
- Cela rejoint bien le futur chapitre sur le rescoring, où le texte d’ajout insiste justement sur la dimension **Threat / exploitation active / Attacked / KEV** dans la priorisation contextuelle.


### Message clé

**KEV répond à la question : “est-ce que cette vulnérabilité est déjà exploitée pour de vrai ?”**

---


## **11.7 Bien lire l’ensemble : ce que chaque référentiel apporte**


### Objectif

Faire une section de synthèse très pédagogique.


### Tableau conseillé

|Référentiel|Question à laquelle il répond|Utilité SOC|
|---|---|---|
|**CVE**|De quelle vulnérabilité parle-t-on ?|Corrélation, recherche, suivi|
|**CWE**|Quel type de faiblesse est en cause ?|Compréhension technique, généralisation|
|**CVSS**|À quel point c’est sévère techniquement ?|Priorisation initiale|
|**EPSS**|Quelle probabilité d’exploitation ?|Priorisation menace, hunting|
|**KEV**|Est-ce exploité dans le réel ?|Urgence opérationnelle|


### Message clé

Cette sous-partie doit vraiment ancrer le réflexe :

- **CVE = identifiant**
- **CWE = cause/faiblesse**
- **CVSS = sévérité**
- **EPSS = probabilité**
- **KEV = exploitation réelle**

---


## **11.8 Ce que le SOC doit en faire concrètement**


### Objectif

Ramener immédiatement le chapitre à l’usage analyste.


### À couvrir

Quand une vulnérabilité apparaît dans une alerte, un ticket ou un bulletin :

1. **Identifier la CVE** concernée.
2. **Comprendre le type de faiblesse** via la CWE si pertinent.
3. **Lire le score CVSS** comme un indicateur de sévérité technique, pas comme une conclusion finale.
4. **Consulter EPSS / KEV** pour estimer la pression de menace.
5. **Croiser avec le contexte interne** :
    - exposition Internet ou non ;
    - actif critique ou non ;
    - exploit observé ou seulement théorique ;
    - contrôles compensatoires ;
    - indices d’exploitation dans les logs.
6. **Qualifier l’incident** selon la grille IR de l’organisation.


### Message clé

**Le SOC ne doit jamais raisonner sur un seul indicateur isolé.**  
Il doit croiser **référentiel vulnérabilité**, **renseignement menace** et **contexte opérationnel interne**.

Cette articulation prépare parfaitement ton prochain chapitre autonome sur **gravité d’incident, CVSS v4 et rescoring contextuel**, qui approfondira justement cette logique.

---


## **11.9 Fil rouge / mise en situation SOC**

Je te conseille fortement une petite sous-partie narrative, comme ton cours utilise déjà un **fil rouge FALCONWATCH**. Le document principal montre bien que ton cours s’appuie sur cette logique narrative récurrente.


### Format possible

> **🛡️ FALCONWATCH — Référentiel vulnérabilités en pratique**  
> Une alerte remonte sur un serveur exposé avec mention d’une CVE critique. Karim identifie l’ID CVE, vérifie la nature de la faiblesse, consulte le score CVSS, puis regarde si la vulnérabilité apparaît dans les listes de vulnérabilités activement exploitées. Il constate que la sévérité technique est élevée, mais que la vraie priorité opérationnelle dépend surtout de trois questions : le système est-il exposé, observe-t-on des traces d’exploitation, et l’actif concerné est-il critique pour le métier ?

L’objectif est de faire sentir que ces référentiels servent à **raisonner**, pas à réciter des définitions.

---


## **11.10 Transition vers le chapitre suivant**

Très important pour garder la fluidité du cours.


### Phrase de transition possible

> Connaître les référentiels ne suffit cependant pas. En investigation SOC, le point décisif n’est pas seulement de savoir qu’une vulnérabilité existe, mais de comprendre ce qu’elle représente dans l’environnement réel de l’organisation. C’est tout l’enjeu du chapitre suivant : distinguer la sévérité d’une vulnérabilité, la probabilité de son exploitation, et la gravité opérationnelle de l’incident qu’elle peut provoquer.

---
