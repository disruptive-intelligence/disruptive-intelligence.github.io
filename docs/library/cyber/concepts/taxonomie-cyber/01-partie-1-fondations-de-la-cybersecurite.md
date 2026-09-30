---
title: Partie 1 — Fondations de la cybersécurité
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
up:
- - Taxonomie cyber
  - index.md
---

## Chapitre 1 — Cybersécurité, sécurité informatique, sécurité des SI

**Définition.** Trois termes voisins, souvent confondus, désignent des périmètres différents.

- **Sécurité informatique** : protection des composants techniques (postes, serveurs, réseaux, logiciels). Périmètre étroit, centré sur la machine.
- **Sécurité des systèmes d'information (SSI)** : protection de l'ensemble organisé qui traite l'information — incluant les processus, les procédures, les personnes, les données et la gouvernance, pas seulement la technique.
- **Cybersécurité** : terme le plus large, englobant la SSI mais ajoutant la dimension des **menaces externes actives** (cybercriminalité, espionnage, sabotage), le cyberespace, et souvent la défense des intérêts au-delà du seul SI (réputation, continuité d'activité, souveraineté).

**Pourquoi la distinction compte.** Un chiffrement parfait (sécurité informatique) ne protège pas contre un employé qui exfiltre des données par négligence (relève de la SSI : processus, sensibilisation) ni contre une campagne d'espionnage ciblée (relève de la cybersécurité : renseignement sur la menace).

🧭 **Taxonomie** — Pensez en cercles concentriques : sécurité informatique ⊂ SSI ⊂ cybersécurité.

⚠️ **Erreur fréquente** — Croire qu'« acheter un firewall » règle un problème de cybersécurité. Le firewall est de la sécurité informatique ; le risque, lui, est souvent organisationnel.

🎯 **À retenir** — La cybersécurité protège l'information *et* l'organisation, pas seulement les machines.


## Chapitre 2 — Actif, donnée, service, système, identité

**Définition.** Un **actif** (asset) est tout ce qui a de la valeur pour l'organisation et mérite donc d'être protégé. La sécurité commence toujours par *savoir ce qu'on protège*.

Cinq grandes catégories d'actifs structurants :

- **Donnée** : l'information elle-même (dossiers clients, secrets industriels, identifiants). Souvent l'actif de plus grande valeur.
- **Service** : une fonction rendue (messagerie, site marchand, paie). Sa valeur est sa *disponibilité* et son *intégrité*.
- **Système** : le support technique (serveur, application, base de données) qui héberge données et services.
- **Identité** : un compte et ses droits — l'actif devenu central, car compromettre une identité donne accès à tout ce que cette identité peut atteindre.
- **Actifs immatériels** : réputation, conformité, propriété intellectuelle.

🔧 **Exemple concret** — Dans une banque, la *donnée* « solde du compte » est l'actif ; le *service* « virement » la manipule ; le *système* « core banking » l'héberge ; l'*identité* « administrateur » peut tout modifier.

🧭 **Taxonomie** — Tout le reste du cours protège ces cinq familles d'actifs. Une attaque vise toujours, in fine, un actif.

🎯 **À retenir** — On ne peut pas protéger ce qu'on n'a pas inventorié. L'inventaire des actifs est le fondement de toute sécurité (NIST CSF : fonction *Identify*).


## Chapitre 3 — Menace, vulnérabilité, risque, impact, vraisemblance

**Définitions.** Ces cinq mots forment le cœur conceptuel de la gestion du risque. Les confondre rend tout raisonnement impossible.

- **Menace** (threat) : un *danger potentiel* — un acteur ou un événement capable de nuire (un attaquant, un malware, un incendie). La menace existe indépendamment de vous.
- **Vulnérabilité** : une *faiblesse* exploitable dans un actif (un mot de passe faible, un logiciel non patché, un employé non sensibilisé).
- **Risque** : la *combinaison* d'une menace exploitant une vulnérabilité, avec ses conséquences. C'est une grandeur, pas un objet.
- **Impact** : la *gravité des conséquences* si le risque se réalise (perte financière, arrêt d'activité, fuite de données).
- **Vraisemblance** (likelihood) : la *probabilité* que le risque se réalise.

**La formule mentale :**

> Risque ≈ Vraisemblance (menace × vulnérabilité × exposition) × Impact

🔧 **Exemple concret** — Menace : un cambrioleur. Vulnérabilité : une fenêtre sans verrou. Impact : vol des biens. Risque : élevé si le quartier est exposé (vraisemblance) et les biens précieux (impact). Poser un verrou réduit la *vulnérabilité*, donc le risque — sans supprimer la menace.

⚠️ **Erreur fréquente** — Dire « j'ai une vulnérabilité, donc j'ai un gros risque ». Faux : une vulnérabilité sans menace réaliste ni impact significatif est un risque faible. C'est la combinaison qui compte.

🧭 **Taxonomie** — Position sur le fil rouge : `menace` et `vulnérabilité` sont les *causes*, `risque` est l'*évaluation*, `impact` est la *conséquence*.

🎯 **À retenir** — Menace = qui/quoi peut nuire. Vulnérabilité = par où. Risque = combien ça compte. Ne jamais les confondre.


## Chapitre 4 — Attaque, incident, compromission, intrusion, fuite de données

**Définitions.** Termes proches qui décrivent des *étapes* ou des *états* différents d'un événement de sécurité.

- **Attaque** : une *action hostile délibérée* visant un actif. Une attaque peut échouer.
- **Intrusion** : un *accès non autorisé* obtenu dans un système. C'est une attaque qui a réussi à franchir le périmètre.
- **Compromission** : un système (ou une identité) est passé sous le contrôle, partiel ou total, d'un attaquant. État plus grave que la simple intrusion.
- **Incident (de sécurité)** : tout *événement* qui porte atteinte (ou menace de porter atteinte) à la confidentialité, l'intégrité ou la disponibilité. Terme générique du SOC. Une attaque réussie est un incident ; une panne accidentelle aussi.
- **Fuite de données** (data breach/leak) : une *catégorie d'impact* où des données confidentielles sortent du périmètre de contrôle, par attaque ou par erreur.

🔧 **Exemple concret** — Un attaquant envoie un mail piégé (**attaque**). Un employé clique et l'attaquant obtient un accès (**intrusion**). Il installe une porte dérobée et contrôle le poste (**compromission**). Le SOC ouvre un ticket (**incident**). L'attaquant exfiltre le fichier clients (**fuite de données**).

⚠️ **Erreur fréquente** — Utiliser « breach » pour toute attaque. Une attaque bloquée n'est pas une compromission ; une compromission sans sortie de données n'est pas une fuite.

🧭 **Taxonomie** — Ces termes décrivent une *progression* : attaque → (intrusion) → compromission → impact (dont fuite). L'incident est l'enveloppe qui englobe le tout côté défense.

🎯 **À retenir** — Distinguez l'*action* (attaque), l'*état* (intrusion, compromission) et la *conséquence* (fuite).


## Chapitre 5 — Confidentialité, intégrité, disponibilité (triptyque CIA)

**Définition.** Le triptyque **CIA** (Confidentiality, Integrity, Availability — en français DIC : Disponibilité, Intégrité, Confidentialité) est la boussole de la sécurité. Toute mesure de sécurité sert au moins l'une de ces trois propriétés.

- **Confidentialité** : l'information n'est accessible qu'aux personnes autorisées. Atteinte = fuite, espionnage.
- **Intégrité** : l'information n'est ni altérée ni falsifiée sans autorisation. Atteinte = sabotage, fraude, manipulation de données.
- **Disponibilité** : l'information et les services sont accessibles quand on en a besoin. Atteinte = déni de service, ransomware, panne.

**Extensions fréquentes** : on ajoute parfois la **traçabilité/imputabilité** (preuve de qui a fait quoi) et la **non-répudiation** (impossibilité de nier une action). Certains parlent du modèle étendu « Parkerian hexad ».

🔧 **Exemple concret** — Un ransomware chiffre les fichiers : il attaque surtout la **disponibilité** (et parfois la confidentialité par double extorsion). Une falsification de relevé bancaire attaque l'**intégrité**. Un vol de base de données attaque la **confidentialité**.

🧭 **Taxonomie** — Toute attaque peut être classée par la propriété CIA qu'elle vise. C'est une des grilles de classification les plus puissantes.

🎯 **À retenir** — Quand vous analysez une attaque, demandez : *quelle propriété CIA est visée ?* La réponse oriente immédiatement la défense.


## Chapitre 6 — Authentification, autorisation, traçabilité, imputabilité

**Définition.** Quatre piliers du contrôle d'accès, souvent regroupés sous **AAA** (Authentication, Authorization, Accounting) + imputabilité.

- **Authentification** : *prouver qui l'on est* (mot de passe, certificat, biométrie, MFA). Répond à « êtes-vous bien vous ? ».
- **Autorisation** : *déterminer ce que l'on a le droit de faire* une fois authentifié. Répond à « avez-vous le droit ? ».
- **Traçabilité** (accounting/auditing) : *enregistrer les actions* dans des journaux pour pouvoir les reconstituer.
- **Imputabilité** (accountability) : *pouvoir attribuer une action à un acteur précis* de manière fiable. Suppose authentification + traçabilité solides.

**Facteurs d'authentification** (à connaître) : ce que je *sais* (mot de passe), ce que je *possède* (téléphone, clé), ce que je *suis* (biométrie). Combiner au moins deux familles = MFA.

🔧 **Exemple concret** — Confondre les deux premiers est une faute classique : un système peut parfaitement *authentifier* un utilisateur (il est bien lui) tout en l'*autorisant* à trop de choses (droits excessifs). L'IDOR (chapitre 83) est précisément une faille d'**autorisation**, pas d'authentification.

⚠️ **Erreur fréquente** — « L'utilisateur est connecté donc il a le droit ». Authentification ≠ autorisation. Vérifier l'identité ne dit rien sur les permissions.

🧭 **Taxonomie** — Les attaques sur l'authentification (brute force, credential stuffing) et sur l'autorisation (IDOR, élévation de privilèges) forment deux familles distinctes — ne pas les mélanger.

🎯 **À retenir** — Authentification = *qui*. Autorisation = *quoi*. Traçabilité = *preuve*. Imputabilité = *attribution*.


## Chapitre 7 — Surface d'attaque, exposition, chemin d'attaque

**Définition.**

- **Surface d'attaque** : l'*ensemble des points* par lesquels un attaquant peut tenter d'entrer ou d'agir (ports ouverts, formulaires web, comptes, API, employés…). Plus elle est grande, plus il y a d'occasions d'attaque.
- **Exposition** : le *degré d'accessibilité* d'un actif depuis une zone dangereuse (Internet > réseau interne > réseau isolé). Un même actif est plus risqué s'il est exposé.
- **Chemin d'attaque** (attack path) : la *séquence d'étapes* reliant le point d'entrée de l'attaquant à son objectif final (souvent : Internet → phishing → poste → identité → serveur → données).

**Réduction de surface d'attaque** : principe défensif majeur (chapitre 22) — fermer les ports inutiles, désinstaller les logiciels superflus, limiter les comptes.

🔧 **Exemple concret** — Un serveur exposé sur Internet avec 30 ports ouverts a une grande surface d'attaque *et* une forte exposition. Le même serveur derrière un VPN, avec 2 ports, réduit les deux.

🧭 **Taxonomie** — La Partie 4 entière est une *taxonomie des surfaces d'attaque*. Le chemin d'attaque, lui, est l'objet d'étude de la modélisation de menace (chapitre 25) et du graphe d'attaque en Active Directory (Partie 8).

🎯 **À retenir** — On défend mieux en *réduisant la surface* qu'en empilant les contrôles sur une surface tentaculaire.


## Chapitre 8 — Contrôles préventifs, détectifs, correctifs et dissuasifs

**Définition.** Tout contrôle de sécurité se classe par sa *fonction temporelle* par rapport à l'incident.

- **Préventif** : empêche l'incident *avant* qu'il survienne (firewall, MFA, durcissement, chiffrement).
- **Détectif** : repère l'incident *pendant* ou *après* (SIEM, EDR, journaux, IDS, alarme).
- **Correctif** : *répare* après l'incident (restauration de sauvegarde, patch, reconstruction).
- **Dissuasif** : *décourage* l'attaquant (bannière légale, visibilité de la surveillance, réputation de robustesse).

On ajoute souvent **compensatoire** (mesure de substitution quand le contrôle idéal est impossible) et **récupératif/recovery**.

🔧 **Exemple concret** — Contre le vol : un verrou (préventif), une caméra (détectif), une assurance (correctif), un panneau « sous surveillance » (dissuasif). La sécurité combine les quatre car aucun n'est suffisant seul.

🧭 **Taxonomie** — Cette grille croise parfaitement le NIST CSF : *Protect* ≈ préventif, *Detect* ≈ détectif, *Respond/Recover* ≈ correctif. Toute défense de la Partie 12 peut être classée ici.

⚠️ **Erreur fréquente** — Tout miser sur le préventif (« assume breach » nous dira que la prévention échouera un jour). Sans détection ni correction, une seule faille devient catastrophique.

🎯 **À retenir** — Une bonne sécurité équilibre prévention, détection et correction. La prévention seule est une illusion.


## Chapitre 9 — Menace opportuniste vs menace ciblée

**Définition.** Classer la menace par son *intentionnalité envers vous*.

- **Menace opportuniste** : l'attaquant ne vous vise pas *vous*, il ratisse large et frappe qui est vulnérable (scans automatisés, ransomware de masse, phishing générique). Vous êtes une cible *parce que* vous étiez faible.
- **Menace ciblée** : l'attaquant vous a *choisi* et investit des efforts spécifiques (espionnage, APT — Advanced Persistent Threat, attaque de la supply chain visant un client précis). Vous êtes une cible *malgré* vos défenses.

**Conséquence défensive.** Contre l'opportuniste, l'hygiène de base suffit souvent (être « moins faible que le voisin »). Contre le ciblé, l'hygiène ne suffit pas : il faut détection avancée, threat hunting, renseignement (CTI).

🧭 **Taxonomie** — Cette distinction structure la *modélisation de menace* (qui m'attaque ?) et le niveau d'investissement défensif justifié.

🎯 **À retenir** — La question « suis-je une cible choisie ou de passage ? » change radicalement la stratégie de défense.


## Chapitre 10 — Risque technique vs risque métier

**Définition.** Un même fait technique a deux lectures.

- **Risque technique** : exprimé en termes de système (« cette vulnérabilité permet une exécution de code à distance », « ce port est exposé »).
- **Risque métier** : exprimé en termes d'*impact pour l'organisation* (« cette vulnérabilité peut interrompre la facturation pendant 3 jours et coûter X € »).

**Pourquoi la traduction est cruciale.** La direction ne décide pas sur des CVE, elle décide sur des conséquences métier. Le rôle de la GRC (Partie 3) est précisément de traduire le technique en métier pour permettre l'arbitrage et le financement.

🔧 **Exemple concret** — « Le serveur SAP n'est pas patché » (technique) devient « la paie de 2 000 salariés peut être bloquée » (métier). Seule la seconde formulation débloque un budget.

⚠️ **Erreur fréquente** — Présenter à la direction des risques uniquement techniques : ils ne seront ni compris ni priorisés.

🧭 **Taxonomie** — Le risque technique alimente le risque métier ; l'analyse de risque (chapitre 30) fait le pont.

🎯 **À retenir** — Un risque qu'on ne sait pas exprimer en langage métier ne sera jamais financé ni traité.

---
