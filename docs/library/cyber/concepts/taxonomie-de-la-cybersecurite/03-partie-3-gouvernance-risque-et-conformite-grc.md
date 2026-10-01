---
title: Partie 3 — Gouvernance, risque et conformité (GRC)
source: Cyber/11 Concepts/Taxonomie de la cybersécurité.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

> La GRC répond à : *qui décide, sur quelles bases, et comment prouve-t-on qu'on maîtrise ?* C'est la fonction *Govern* placée au centre du NIST CSF 2.0. Sans gouvernance, la technique est aveugle.


### Chapitre 29 — PSSI, politiques, standards et procédures

**Définition.** La documentation de sécurité s'organise en *niveaux* allant du général au précis.

- **PSSI** (Politique de Sécurité des SI) : document fondateur exprimant les *objectifs* et la *volonté* de l'organisation. Le « pourquoi ».
- **Politiques** : règles de haut niveau par domaine (mots de passe, accès, sauvegarde).
- **Standards** : exigences concrètes et obligatoires (« longueur minimale 14 caractères », « TLS 1.2+ »). Le « quoi ».
- **Procédures** : étapes détaillées pour appliquer un standard. Le « comment ».
- **Guides/recommandations** : conseils non obligatoires.

🧭 **Taxonomie** — Pyramide documentaire : PSSI → politiques → standards → procédures. Plus on descend, plus c'est précis et opérationnel.

⚠️ **Erreur fréquente** — Écrire des politiques que personne n'applique ni ne contrôle (« sécurité-papier »). Un document non appliqué crée un faux sentiment de sécurité.

🎯 **À retenir** — La PSSI fixe le cap ; les standards et procédures le rendent applicable et vérifiable.


### Chapitre 30 — Analyse de risque

**Définition.** Démarche structurée pour *identifier, estimer et hiérarchiser* les risques, afin de décider lesquels traiter en priorité.

**Étapes type.** Identifier les actifs → identifier menaces et vulnérabilités → estimer vraisemblance et impact → évaluer le niveau de risque → décider du traitement. Méthodes connues : EBIOS Risk Manager (France/ANSSI), ISO 27005, FAIR (quantitatif, en valeur monétaire).

**Quatre traitements possibles du risque :**

- **Réduire** (mettre des contrôles),
- **Transférer** (assurance, sous-traitance),
- **Éviter** (renoncer à l'activité risquée),
- **Accepter** (assumer le risque résiduel, formellement).

🧭 **Taxonomie** — Cœur de la GRC ; fait le pont entre risque technique et risque métier (chapitre 10). Alimente l'homologation (chapitre 31).

🎯 **À retenir** — On ne traite jamais tous les risques ; on les *priorise* en fonction de vraisemblance × impact, puis on choisit consciemment réduire/transférer/éviter/accepter.


### Chapitre 31 — Homologation et acceptation du risque

**Définition.**

- **Homologation** (accreditation/authorization to operate) : décision *formelle*, prise par une autorité responsable, autorisant un système à fonctionner *en connaissance des risques résiduels*.
- **Acceptation du risque** : reconnaissance explicite et tracée qu'un risque résiduel est assumé par un responsable identifié.

**Principe.** La sécurité parfaite n'existe pas ; il reste toujours un risque résiduel. L'homologation force une *décision consciente et responsable* plutôt qu'un risque subi par défaut. Elle a un propriétaire et une date de revue.

⚠️ **Erreur fréquente** — Laisser le risque résiduel « non décidé » : personne ne l'assume, donc personne ne le surveille. L'acceptation doit être nominative et datée.

🧭 **Taxonomie** — Aboutissement de l'analyse de risque ; relève de la gouvernance (qui *signe*).

🎯 **À retenir** — Accepter un risque est une décision légitime — à condition qu'elle soit explicite, tracée et portée par une autorité.


### Chapitre 32 — Gestion des vulnérabilités

**Définition.** Processus *continu* d'identification, d'évaluation, de priorisation et de correction des vulnérabilités du parc.

**Cycle.** Découverte (scanners, veille CVE, pentest) → évaluation (gravité via CVSS, exploitabilité via EPSS, exposition réelle) → priorisation → remédiation (patch, contournement) → vérification → reporting. Notions clés : **CVE** (identifiant de vulnérabilité), **CVSS** (score de gravité 0–10), **EPSS** (probabilité d'exploitation), **KEV** (catalogue des vulnérabilités activement exploitées de la CISA).

⚠️ **Erreur fréquente** — Prioriser uniquement par CVSS. Une vulnérabilité « critique » non exposée et non exploitée est moins urgente qu'une « moyenne » exposée sur Internet et activement exploitée (présente dans le KEV). Croiser gravité, exploitabilité et exposition.

🧭 **Taxonomie** — Processus GRC opérationnel relié à la gestion des actifs (chapitre 33) et à la supervision continue (chapitre 27).

🎯 **À retenir** — Patcher tout est impossible ; patcher *intelligemment* (gravité × exploitabilité × exposition) est la compétence clé.


### Chapitre 33 — Gestion des actifs

**Définition.** Inventorier et maintenir à jour la connaissance de *tout* ce qu'on possède : matériels, logiciels, services cloud, données, comptes.

**Principe.** « On ne protège que ce qu'on connaît. » Un actif inconnu (shadow IT, serveur oublié) n'est ni patché, ni surveillé, ni sauvegardé — donc une porte d'entrée idéale. La gestion d'actifs alimente toutes les autres fonctions (vulnérabilités, surveillance, sauvegarde).

🔧 **Exemple concret** — Un vieux serveur de test, oublié de l'inventaire, exposé sur Internet et non patché : porte d'entrée classique des intrusions réelles.

🧭 **Taxonomie** — Fonction *Identify* du NIST CSF, prérequis de presque tout le reste. Inclut le **CMDB** et de plus en plus le **CAASM** (gestion de la surface d'attaque).

🎯 **À retenir** — L'inventaire d'actifs n'est pas un sujet « ennuyeux » : c'est la fondation de toute la sécurité. L'inconnu est l'ennemi.


### Chapitre 34 — Classification de l'information

**Définition.** Attribuer à chaque donnée un *niveau de sensibilité* (par ex. public / interne / confidentiel / secret) qui détermine les protections requises.

**Principe.** Toutes les données ne se valent pas. La classification permet d'appliquer des contrôles *proportionnés* : chiffrement, restrictions d'accès (besoin d'en connaître), règles de conservation et de destruction, marquage. Elle est le préalable à la DLP (chapitre 285).

🧭 **Taxonomie** — Relie le besoin d'en connaître (chapitre 13), la confidentialité (chapitre 5) et la protection des données. Base de la gouvernance de la donnée.

🎯 **À retenir** — Sans classification, on protège tout pareil — donc on sur-protège l'inutile et on sous-protège l'essentiel.


### Chapitre 35 — Gestion des exceptions

**Définition.** Processus formel pour *autoriser temporairement* un écart à une règle de sécurité, quand l'application stricte est impossible, avec validation, justification, mesures compensatoires et date d'expiration.

**Principe.** Les exceptions existent toujours (système legacy inpatchable, contrainte métier). Le danger n'est pas l'exception elle-même, mais l'exception *non tracée, non limitée dans le temps, non compensée*. Une bonne gestion les recense, les justifie et les revoit.

⚠️ **Erreur fréquente** — L'exception « provisoire » qui dure des années sans revue. Toute exception doit avoir une échéance et un propriétaire.

🧭 **Taxonomie** — Soupape de la GRC ; étroitement liée à l'acceptation du risque (chapitre 31) et aux mesures compensatoires (chapitre 8).

🎯 **À retenir** — Une exception acceptable est une exception *connue, justifiée, compensée et datée*.


### Chapitre 36 — Audit et contrôle

**Définition.**

- **Contrôle interne** : vérifications *continues* intégrées aux processus (le « premier niveau »).
- **Audit** : évaluation *indépendante et périodique* de la conformité et de l'efficacité des contrôles (interne ou externe).

**Principe.** « Faire confiance, mais vérifier. » L'audit fournit une assurance objective que les politiques sont réellement appliquées et efficaces. Il produit des constats, des écarts (gaps) et des plans d'action. Les **trois lignes de défense** : opérationnels (1), fonctions risque/conformité (2), audit interne (3).

🧭 **Taxonomie** — Contrôle *détectif* au niveau organisationnel ; pilier de la conformité (ISO 27001, SOC 2…).

🎯 **À retenir** — Sans audit, on ne sait pas si la sécurité documentée existe vraiment. L'audit transforme la croyance en preuve.


### Chapitre 37 — Sensibilisation

**Définition.** Programme visant à élever le niveau de vigilance et de compétence des utilisateurs face aux menaces (phishing, mots de passe, ingénierie sociale, manipulation de données).

**Principe.** L'humain est à la fois la cible privilégiée (phishing, social engineering — Partie 9) et un capteur précieux (un employé formé *signale* une attaque). La sensibilisation transforme le « maillon faible » en première ligne de détection. Formes : formations, simulations de phishing, communication régulière, culture du signalement *sans punition*.

⚠️ **Erreur fréquente** — Punir l'utilisateur qui « clique » : il cessera de signaler, ce qui aggrave le risque. On cultive le signalement, on ne le réprime pas.

🧭 **Taxonomie** — Contrôle transversal, à la fois préventif et détectif ; indispensable contre toute la Partie 9.

🎯 **À retenir** — Un utilisateur formé est un capteur de sécurité supplémentaire. La sensibilisation est un investissement à très fort rendement.


### Chapitre 38 — Sécurité des tiers et supply chain

**Définition.** Gérer les risques introduits par les *fournisseurs, prestataires et dépendances* externes — qui ont souvent un accès ou une influence sur votre SI.

**Principe.** Votre sécurité ne vaut que celle de votre maillon le plus faible, y compris externe. Un fournisseur compromis (logiciel, infogérant, composant) devient un vecteur d'attaque (supply chain attack). Mesures : évaluation des fournisseurs, clauses contractuelles de sécurité, droit d'audit, limitation des accès, surveillance.

🔧 **Exemple concret** — Une mise à jour logicielle d'un éditeur de confiance, compromise à la source, distribue une porte dérobée à tous ses clients (cf. dependency confusion, build system compromise — Partie 10).

🧭 **Taxonomie** — Risque transverse relié à la supply chain logicielle (chapitre 81, Partie 10) et à la gestion des tiers. Sujet en forte croissance.

🎯 **À retenir** — Vous héritez du risque de vos fournisseurs. La confiance contractuelle ne remplace pas la vérification.


### Chapitre 39 — Gestion de crise cyber

**Définition.** Dispositif *organisationnel* (et pas seulement technique) pour piloter une crise majeure : décision, coordination, communication, continuité, sous forte pression et incertitude.

**Composants.** Cellule de crise (rôles définis à l'avance), procédures d'escalade, moyens de communication *de secours* (hors du SI potentiellement compromis), plan de communication interne/externe/réglementaire, articulation avec le PRA/PCA. Préparée *à froid* par des exercices (tabletop, chapitre 304).

⚠️ **Erreur fréquente** — Improviser la crise le jour J, communiquer via les outils compromis, ou découvrir que personne ne sait qui décide. La crise se prépare *avant*.

🧭 **Taxonomie** — Niveau de pilotage au-dessus de la réponse à incident technique (Partie 11) ; relié au PRA/PCA (chapitre 267) et à la communication de crise (chapitre 268).

🎯 **À retenir** — La crise cyber se gère avec une cellule, des rôles et des canaux préparés à l'avance — jamais en improvisation.

---

> **Fin du Volume 1/8.**
>
> **Suite prévue :**
> - Volume 2 — Parties 4 & 5 : Taxonomie des surfaces d'attaque & des vulnérabilités
> - Volume 3 — Partie 6 : Attaques web et applicatives
> - Volume 4 — Partie 7 : Attaques réseau et infrastructure
> - Volume 5 — Partie 8 : Identité, Active Directory et privilèges
> - Volume 6 — Partie 9 : Malware, phishing et attaques client-side
> - Volume 7 — Partie 10 : Cloud, API, conteneurs et supply chain
> - Volume 8 — Parties 11 à 13 + Annexes : Détection/SOC/IR, défenses, synthèse, glossaire


---


## Taxonomie de la cybersécurité — Volume 2/8

> Parties 4 & 5 : Taxonomie des surfaces d'attaque · Taxonomie des vulnérabilités
>
> Rappel du fil rouge : **actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation**. La Partie 4 répond à *« par où peut-on m'attaquer ? »* (les surfaces). La Partie 5 répond à *« quelle faiblesse est exploitée ? »* (les vulnérabilités). Les attaques elles-mêmes viendront dans les volumes suivants.

---
