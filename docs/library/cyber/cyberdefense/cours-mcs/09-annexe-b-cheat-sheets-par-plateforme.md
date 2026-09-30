---
title: Annexe B — Cheat sheets par plateforme
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 9
chapters: 10
---

> ⏱ **Annexe versionnée — vérifiée le 1er août 2026.** Elle contient des commandes et des cadences susceptibles d'évoluer.
>
> **Format uniforme pour les douze fiches** : périmètre · contrôles · privilèges requis · lecture du résultat · preuve produite · limites · source de vérité · piège spécifique · cadence.

---

### B.1 Windows

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Postes et serveurs Windows, système et composants natifs |
| **Contrôles** | `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" \| Select ProductName, DisplayVersion, CurrentBuild, UBR` · `Get-HotFix \| Sort InstalledOn -Descending` · `Test-Path "HKLM:\...\Component Based Servicing\RebootPending"` · `Get-WinEvent -LogName Setup` |
| **Privilèges** | Lecture locale suffisante ; administrateur pour le journal Setup |
| **Lecture du résultat** | Le couple **build + UBR** identifie le niveau de mise à jour cumulative |
| **Preuve produite** | Relevé build+UBR horodaté, avec identifiant d'actif (§2.9) |
| **Limites** | Ne couvre ni les applications, ni les composants facultatifs, ni l'environnement de récupération, ni les pilotes, ni les micrologiciels. La clé `RebootPending` n'est **qu'un** des signaux de redémarrage |
| **Source de vérité** | Portail de sécurité de l'éditeur, pour les versions affectées et corrigées |
| **Piège** | La réversibilité d'un correctif cumulatif ne se présume jamais (§2.5) |
| **Cadence** | Mensuelle, hors cycle en urgence |

---

### B.2 Linux — famille Debian

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Distributions dérivées de Debian, paquets système |
| **Contrôles** | `apt-cache policy <paquet>` · `zcat /usr/share/doc/<paquet>/changelog.Debian.gz \| head -40` · `needrestart -r l` · `/var/log/dpkg.log`, `/var/log/apt/history.log` |
| **Privilèges** | Lecture pour la version ; root pour `needrestart` complet |
| **Lecture du résultat** | La **révision éditeur** (`+debXuY`, `~debXuY`) porte le correctif, pas le numéro amont |
| **Preuve produite** | Version complète du paquet + date, + confirmation de redémarrage du service |
| **Limites** | `apt list --upgradable` ne filtre **pas** sur la sécurité · le journal local est un indice, pas une preuve |
| **Source de vérité** | Avis de sécurité de la distribution et suivi officiel du paquet |
| **Piège** | La notion d'**époque** (`1:`) prend le pas sur le reste dans les comparaisons de version |
| **Cadence** | Quotidienne pour la veille, mensuelle pour les campagnes |

---

### B.3 Linux — famille RHEL

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Distributions dérivées de Red Hat |
| **Contrôles** | `dnf updateinfo list security` · `rpm -q --changelog <paquet> \| grep CVE` · `needs-restarting -s` (services) · `needs-restarting -r` (système) · `dnf history list` / `dnf history info <ID>` |
| **Privilèges** | Lecture pour l'inventaire ; root pour `needs-restarting -r` |
| **Lecture du résultat** | `dnf updateinfo` filtre réellement sur la sécurité, contrairement à l'équivalent Debian |
| **Preuve produite** | Transaction `dnf history` datée + relevé de version |
| **Limites** | Le changelog RPM ne mentionne pas systématiquement l'identifiant de la faille |
| **Source de vérité** | Avis de sécurité de la distribution |
| **Piège** | Correctif appliqué sans redémarrage de service : le code vulnérable reste chargé (§2.6) |
| **Cadence** | Idem Debian |

---

### B.4 macOS et mobiles

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Postes macOS, terminaux mobiles gérés |
| **Contrôles** | Version minimale exigée par la politique d'accès · délai de report autorisé à l'utilisateur · population non enrôlée |
| **Privilèges** | Console de gestion de flotte |
| **Lecture du résultat** | La conformité dépend en partie du **comportement de l'utilisateur**, pas seulement du déploiement |
| **Preuve produite** | État de conformité par appareil, avec date de dernier contact |
| **Limites** | Ne couvre que les appareils **enrôlés** — les autres n'apparaissent nulle part |
| **Source de vérité** | Notes de version de l'éditeur du système |
| **Piège** | On pilote ici par la **politique d'accès**, pas par le déploiement (§19.4) |
| **Cadence** | Mensuelle, avec contrôle à la reconnexion |

---

### B.5 Conteneurs et orchestration

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Images, registres, clusters d'orchestration |
| **Contrôles** | Âge de l'image en production · référence par empreinte immuable et non par étiquette · version du plan de contrôle · écart plan de contrôle / nœuds · inventaire des interfaces dépréciées utilisées |
| **Privilèges** | Lecture sur le registre et l'orchestrateur |
| **Lecture du résultat** | L'âge de l'image est un **indicateur préventif central**, à compléter par l'analyse de vulnérabilités |
| **Preuve produite** | Empreinte d'image déployée + date de construction |
| **Limites** | Ne voit pas ce qui est ajouté au conteneur à l'exécution · les actifs éphémères échappent à l'inventaire réseau |
| **Source de vérité** | Registre d'images et politique de support du projet |
| **Piège** | Une image reconstruite hier peut embarquer une dépendance vulnérable ; une image plus ancienne peut porter un rétroportage corrigé |
| **Cadence** | Reconstruction ≤ 30 j · montée de version du cluster 2 à 3 fois/an |

---

### B.6 Réseau et sécurité

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Pare-feu, routeurs, commutateurs, passerelles d'accès distant |
| **Contrôles** | Version d'image active et de secours · **date de fin de support de sécurité** · interface d'administration non publiée (vérification **depuis l'extérieur**) · export des journaux hors équipement |
| **Privilèges** | Compte d'administration en lecture |
| **Lecture du résultat** | Relevé de version directement sur l'équipement, pas dans un tableur |
| **Preuve produite** | Sortie de commande de version, horodatée |
| **Limites** | Rarement couvert par un scan authentifié : suivi manuel assumé |
| **Source de vérité** | Portail de sécurité du constructeur |
| **Piège** | La fin de support **de sécurité** précède souvent de plusieurs années la fin de vie matérielle (§27.3) |
| **Cadence** | Trimestrielle, doctrine de version datée et revue |

---

### B.7 Hyperviseurs et plans de gestion

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Hôtes, plan de gestion, micrologiciel du matériel sous-jacent |
| **Contrôles** | Version de l'hôte · version du plan de gestion · **exposition réseau du plan de gestion** · version du micrologiciel serveur |
| **Privilèges** | Administration de la plateforme |
| **Lecture du résultat** | Quatre objets distincts à suivre séparément (§3.1) |
| **Preuve produite** | Inventaire de versions exporté depuis la console |
| **Limites** | Les appliances virtuelles fournisseur ne sont pas maintenues par vous |
| **Source de vérité** | Matrice de compatibilité et avis de l'éditeur |
| **Piège** | Le plan de gestion est un **actif de niveau 0** régulièrement laissé en retard |
| **Cadence** | Trimestrielle, avec fenêtre récurrente dédiée |

---

### B.8 Cloud

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Ressources, images, services managés, identités, configuration |
| **Contrôles** | Âge des images du catalogue · **versions de services managés et leurs dates de fin de support** · identités à droits étendus · garde-fous préventifs actifs · écart entre code d'infrastructure et réalité |
| **Privilèges** | Lecture sur les interfaces du fournisseur |
| **Lecture du résultat** | Sur les services managés, vous pilotez l'**anticipation**, pas la correction |
| **Preuve produite** | Export d'inventaire de ressources + versions, horodaté |
| **Limites** | Aucune preuve technique possible sur la couche du fournisseur |
| **Source de vérité** | Notes de service et calendriers de dépréciation du fournisseur |
| **Piège** | Les versions de services managés doivent entrer au référentiel d'obsolescence (§30.3) — l'oubli le plus fréquent |
| **Cadence** | Mensuelle pour les annonces, trimestrielle pour l'inventaire |

---

### B.9 Services en ligne

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Configuration du locataire, identités, extensions, intégrations |
| **Contrôles** | État de référence sur les huit familles de paramètres (§31.4) · inventaire des autorisations déléguées · consentement utilisateur restreint · rétention des journaux connue |
| **Privilèges** | Administration du service |
| **Lecture du résultat** | Comparaison à un état de référence documenté, pas à la mémoire |
| **Preuve produite** | Export de configuration daté + liste des applications autorisées |
| **Limites** | Aucun accès technique au socle · rapports d'audit du fournisseur insuffisants seuls |
| **Source de vérité** | Notes de version et annonces de dépréciation du fournisseur |
| **Piège** | Une fonctionnalité activée par défaut modifie votre exposition sans que votre configuration change |
| **Cadence** | Mensuelle sur les services sensibles, annuelle sur les autres |

---

### B.10 Industriel

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Automates, supervision, systèmes d'exécution de production |
| **Contrôles** | Écoute passive du trafic · extraction depuis les outils d'ingénierie · inventaire manuel avec l'équipe de maintenance |
| **Privilèges** | Accès aux outils d'ingénierie, avec accompagnement |
| **Lecture du résultat** | L'inventaire manuel est souvent le plus fiable sur les équipements anciens |
| **Preuve produite** | Relevé de version signé, journal de transfert (§29.5) |
| **Limites** | L'écoute passive ne voit que ce qui communique |
| **Source de vérité** | Avis du constructeur, avec validation écrite pour tout correctif |
| **Piège** | Doctrine : **passif par défaut, actif sous procédure** — un scan actif contrôlé reste possible, il ne s'improvise pas |
| **Cadence** | Alignée sur les arrêts de production |

---

### B.11 Bases de données, middlewares et *runtimes*

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Moteurs de bases, serveurs d'applications, environnements d'exécution, bibliothèques embarquées |
| **Contrôles** | Inventaire **par application** et non par machine · versions majeures et mineures suivies séparément · authentification activée sur brokers, caches et moteurs de recherche |
| **Privilèges** | Lecture applicative et système |
| **Lecture du résultat** | Le blocage vient presque toujours de l'application, pas du moteur |
| **Preuve produite** | Tableau composant / version / date de fin de support / source |
| **Limites** | Les bibliothèques natives embarquées n'apparaissent ni au scan système, ni à l'analyse de composition |
| **Source de vérité** | Pages de cycle de vie de chaque éditeur, et inventaire de composants fourni |
| **Piège** | Système parfaitement à jour, application sur un composant hors support depuis deux ans (§26.1) |
| **Cadence** | Trimestrielle pour l'inventaire, annuelle pour la trajectoire de version |

---

### B.12 Applications tierces du poste

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Navigateurs et extensions, lecteurs, environnements d'exécution, utilitaires métier |
| **Contrôles** | Inventaire sur un **échantillon** de postes avant tout achat d'outil · liste des applications hors support |
| **Privilèges** | Lecture locale ou console de gestion |
| **Lecture du résultat** | La liste est presque toujours plus longue et plus ancienne qu'attendu |
| **Preuve produite** | Inventaire applicatif par poste, daté |
| **Limites** | Non couvert par les mécanismes natifs du système |
| **Source de vérité** | Éditeur de chaque application |
| **Piège** | La mise à jour automatique native ne donne ni contrôle, ni visibilité, ni preuve (§19.5) |
| **Cadence** | Mensuelle, avec un inventaire complet semestriel |

---


## Annexe C — Matrices de priorisation et de délais

### C.1 Comparatif des signaux

| Signal | Répond à | Ne répond pas à | Volatilité |
|---|---|---|---|
| Gravité technique | Quels dégâts si exploitée ? | Est-ce exploité ? Suis-je atteignable ? | Nulle (base fixe) |
| Probabilité d'exploitation | Sera-t-elle exploitée dans le monde ? | Chez moi ? Sur cet actif ? | **Élevée** — et discontinue entre versions de modèle |
| Exploitation avérée | A-t-elle été observée ? | Suis-je concerné et exposé ? | Cumulative |
| Arbre de décision | **Que dois-je faire ?** | *(nécessite l'exposition en entrée)* | Stable |
| **Exposition** | Est-ce atteignable, par qui ? | — | Change à chaque projet |
| **Criticité métier** | Que vaut cet actif ? | — | Stable |

Les deux dernières lignes sont produites **par vous seul**.

### C.2 Arbre de décision de référence

```
① Exploitation active ?
   ├─ OUI → ② Joignable depuis Internet ?
   │         ├─ OUI → AGIR EN URGENCE (72 h, hors fenêtre autorisée)
   │         └─ NON → ③ Niveau 0 ou critique métier ?
   │                   ├─ OUI → TRAITER EN PRIORITÉ (7 j)
   │                   └─ NON → TRAITER (30 j)
   └─ NON → ④ Probabilité élevée OU gravité critique ?
             ├─ OUI → ⑤ Exposé ou critique ?
             │         ├─ OUI → TRAITER (30 j)
             │         └─ NON → PLANIFIER (campagne)
             └─ NON → ⑥ Corrigeable en campagne groupée ?
                       ├─ OUI → PLANIFIER (trimestrielle)
                       └─ NON → SURVEILLER (revue semestrielle)
```

### C.3 Matrice délais × classe

| | C1 exposé/critique | C2 important | C3 courant | C4 contraint |
|---|---|---|---|---|
| Exploitée | 72 h | 7 j | 30 j | **Compensation sous 72 h** |
| Critique non exploitée | 15 j | 30 j | 60 j | Compensation ou dérogation |
| Autres | 30 j | 90 j | 180 j | Selon fenêtre constructeur |
| Vérification | Hebdo | Mensuelle | Mensuelle | Trimestrielle |
| Test préalable | Recette + témoin | Témoin | Anneau pilote | Validation fournisseur |

*Valeurs de départ pour une organisation de taille intermédiaire. Calibrez sur votre capacité mesurée (§16.5).*

### C.4 Grille d'acceptation de risque

| Niveau de risque résiduel | Signataire |
|---|---|
| Actif C3, non exposé | Propriétaire technique |
| Actif C2 | Propriétaire métier |
| Actif C1 ou exposé | Directeur des systèmes d'information |
| Actif de niveau 0, ou données sensibles | **Direction générale** |
| Renouvellement d'une dérogation | **Niveau supérieur au précédent** (§7.4) |

---


## Annexe D — Templates opérationnels

> **Quatorze formulaires remplissables.** Chacun porte un identifiant, une version et une date. Les champs `[ ]` sont à compléter, les champs marqués **(O)** sont obligatoires, **(F)** facultatifs. Les règles de validation indiquent ce qui bloque l'acceptation du document.
>
> ⚠️ Les valeurs numériques proposées (délais, seuils, durées) constituent un **modèle de référence de ce cours**, à adapter et faire approuver par votre organisation. Elles ne sont ni une norme ni une exigence externe.

---

### D.1 — Politique MCS

**Identifiant** `POL-MCS-[nn]` · **Version** `[x.y]` · **Date** `[jj/mm/aaaa]` · **Approbateur** `[nom, fonction]` · **Revue** `[annuelle]`

| § | Section | Contenu attendu | Longueur |
|---|---|---|---|
| 1 | Objet et périmètre | Ce qui est couvert · **ce qui ne l'est pas, et pourquoi** | ½ p. |
| 2 | Définitions | Actif · propriétaire · couverture · conformité · population éligible · non mesuré | 1 p. |
| 3 | Rôles | Renvoi au RACI D.3, décideurs nommés par type de décision | 1 p. |
| 4 | Classes de service | Le formulaire D.2 intégré | 2-3 p. |
| 5 | Processus | Veille · détection · triage · remédiation · vérification · preuve | 2-3 p. |
| 6 | Dérogations | Renvoi à D.4, niveaux de signature, règle de renouvellement | 1 p. |
| 7 | Mesure et contrôle | Indicateurs publiés, fréquence, destinataires | 1 p. |
| Ann. | **Périmètres non couverts** | Tableau ci-dessous | 1 p. |

**Annexe obligatoire — périmètres déclarés non couverts**

| Périmètre | Motif de non-couverture | Propriétaire désigné | Échéance de première mesure | Compensation en place |
|---|---|---|---|---|
| `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Règles de validation** — La politique ne peut être approuvée si : un délai annoncé n'a pas été confronté à une mesure de capacité (§16.5) · la procédure de dérogation est absente · l'annexe des périmètres non couverts est vide sans justification écrite.

---

### D.2 — Table des classes de service

**Identifiant** `CLS-[nn]` · **Version** `[ ]` · **Approbateur** `[DSI]`

| Paramètre | C1 — critique/exposé | C2 — important | C3 — courant | C4 — contraint |
|---|---|---|---|---|
| **Définition** (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| **Exemples d'actifs** (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Délai — vulnérabilité exploitée (O) | `[72 h]` | `[7 j]` | `[30 j]` | `[compensation 72 h]` |
| Délai — critique non exploitée (O) | `[15 j]` | `[30 j]` | `[60 j]` | `[compensation/dérogation]` |
| Délai — autres (O) | `[30 j]` | `[90 j]` | `[180 j]` | `[fenêtre constructeur]` |
| Fréquence de vérification (O) | `[hebdo]` | `[mensuelle]` | `[mensuelle]` | `[trimestrielle]` |
| Niveau de test (O) | `[recette + témoin]` | `[témoin]` | `[anneau pilote]` | `[validation fournisseur]` |
| Fenêtre (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Délai d'observation (F) | `[0-3 j]` | `[5 j]` | `[5 j]` | `[n/a]` |

**Validation** — Chaque délai doit être accompagné de la mesure de capacité qui le justifie. Un délai non tenu trois mois consécutifs déclenche une révision de la classe ou de la capacité.

---

### D.3 — RACI du MCS

**Identifiant** `RACI-MCS-[nn]` · **Version** `[ ]` · **Périmètre** `[IT / OT / cloud / produit]`

**R** réalise · **A** approuve (un seul par ligne) · **C** consulté · **I** informé

| Activité | RSSI | Exploitation | Propr. métier | DSI | Prestataire |
|---|---|---|---|---|---|
| Définir la politique et les classes | `[R]` | `[C]` | `[C]` | `[A]` | `[I]` |
| Tenir l'inventaire | `[C]` | `[R/A]` | `[C]` | `[I]` | `[R]` |
| Veille et qualification | `[R/A]` | `[C]` | `[I]` | `[I]` | `[C]` |
| Prioriser et fixer les délais | `[R]` | `[C]` | `[C]` | `[A]` | `[I]` |
| Planifier et exécuter | `[I]` | `[R/A]` | `[C]` | `[I]` | `[R]` |
| **Décider d'une interruption** | `[C]` | `[C]` | `[A]` | `[I]` | `[I]` |
| **Accorder une dérogation** | `[R]` | `[C]` | `[A]` | `[C]` | `[I]` |
| Produire la preuve | `[C]` | `[R]` | `[I]` | `[I]` | `[R]` |
| Escalader une impossibilité | `[C]` | `[R]` | `[C]` | `[A]` | `[R]` |
| Contrôler l'application | `[R/A]` | `[C]` | `[I]` | `[I]` | `[I]` |

**Validation** — Un seul **A** par ligne. Toute case **A** doit correspondre à une personne nommée disposant du mandat correspondant, pas à une entité collective.

---

### D.4 — Fiche de dérogation

**Identifiant** `DER-[aaaa]-[nnn]` · **Version** `[ ]` · **Date d'émission** `[ ]`

| Champ | | Valeur |
|---|---|---|
| Objet précis | (O) | `[actif(s) · vulnérabilité ou écart · correctif concerné]` |
| Type d'impossibilité | (O) | `[ ] technique  [ ] contractuelle  [ ] métier  [ ] budgétaire  [ ] temporelle` |
| **Analyse de risque, en termes métier** | (O) | `[ce qui se passe si le risque se réalise : données, service, personnes, conséquences contractuelles]` |
| Exposition mesurée | (O) | `[ ] Internet  [ ] réseau bureautique  [ ] réseau d'administration  [ ] isolé` |
| Exploitation observée | (O) | `[ ] non  [ ] dans le monde  [ ] dans le secteur  [ ] indices chez nous` |
| Mesures compensatoires | (O) | `[1. ]  [2. ]  [3. ]` — hiérarchie du §20.2, en indiquant les rangs écartés et pourquoi |
| **Moyen de vérification** | (O) | `[test précis prouvant que la compensation est active]` |
| Fréquence du contrôle | (O) | `[mensuelle]` |
| Coût opérationnel | (O) | `[h/mois]` |
| Propriétaire de la compensation | (O) | `[nom]` |
| **Signataire** | (O) | `[nom, fonction — selon la grille C.4]` |
| Date de début | (O) | `[ ]` |
| **Date d'expiration** | (O) | `[date du calendrier, alignée sur un événement décisionnel réel]` |
| Conditions de sortie | (O) | `[correction réalisée]  [exploitation observée]  [changement d'exposition]` |
| **Conditions de révocation anticipée** | (O) | `[événements imposant de mettre fin immédiatement à la dérogation]` |
| Nombre de renouvellements | (O) | `[0]` — chaque renouvellement remonte d'un niveau de signature |
| Date de revue | (O) | `[trimestrielle]` |

**Règles de validation** — Rejet automatique si : pas de date d'expiration ou date exprimée en événement flou · compensation sans moyen de vérification · signataire non conforme à la grille C.4 · risque décrit en termes techniques uniquement.

**Quatre notions que le terrain confond, et qu'il faut séparer par écrit**

| Notion | Nature | Durée | Signataire | Ce qui la clôt |
|---|---|---|---|---|
| **Dérogation** | Exception temporaire à une règle existante | **Bornée** | Propriétaire métier, niveau selon C.4 | La correction, ou une condition de sortie |
| **Acceptation de risque** | Décision durable de porter un risque résiduel | **Non bornée**, mais revue | Niveau supérieur, selon C.4 | Une revue qui change la décision |
| **N/A** | La règle ne s'applique pas à cet actif | Permanente tant que le contexte tient | Propriétaire technique | Un changement de contexte |
| **Faux positif** | Le constat était erroné | Définitive | Analyste, **avec démonstration** | — |

⚠️ **Le mot « exception » recouvre les quatre dans le langage courant**, et il désigne en plus les exclusions d'outil (§15.6, §34.4). C'est la principale source d'ambiguïté d'un registre de dérogations. La règle interne : le mot « exception » ne figure dans aucun document formel de ce dispositif — on écrit toujours laquelle des cinq choses on désigne.

---

### D.5 — Demande de changement urgent

**Identifiant** `CHG-U-[aaaa]-[nnn]` · **Émission** `[date, heure]` · **Régularisation attendue sous** `[48 h]`

| Section | Contenu |
|---|---|
| Constat et qualification | `[identifiant · statut : fait vérifié / hypothèse / piste · source]` |
| Exposition mesurée | `[nombre d'actifs · joignables depuis · depuis quand]` |
| Chemin dans l'arbre de décision | `[reproduire les réponses aux questions ① à ⑥]` |
| Justification de l'urgence | `[critère de déclenchement satisfait]` |
| Périmètre de l'intervention | `[liste ou requête d'actifs]` |
| **Écart recette / production** | `[versions · volumétrie · intégrations · configuration — chacun qualifié]` |
| **Critères go/no-go** | Renvoi D.6, **joints obligatoirement** |
| **Plan de retour arrière** | Renvoi D.7, **joint obligatoirement** |
| Point de non-retour | `[instant précis]` ou `[aucun]` |
| Décideur nommé | `[nom]` |
| Décideur du retour arrière | `[nom]` — peut différer |
| Communication prévue | `[direction] [métiers] [utilisateurs] [clients] [assureur] [autorités]` |
| Preuve à produire | `[nature · échantillon · responsable]` |

**Validation** — Le changement ne peut être exécuté sans D.6 et D.7 joints, ni sans décideur nommé pour le retour arrière.

---

### D.6 — Critères go / no-go

**Identifiant** `GNG-[aaaa]-[nnn]` · **Rattaché à** `[CHG-...]` · **Écrit le** `[avant l'intervention]`

| Indicateur | Seuil d'arrêt | Mesuré par | Fenêtre d'observation |
|---|---|---|---|
| Taux d'échec d'installation | `[> 5 %]` | `[outil]` | `[continu]` |
| Incidents déclarés liés | `[≥ 3 sur l'anneau]` | `[support]` | `[24 h]` |
| **Indicateur fonctionnel métier** (O) | `[baisse > 10 % sur 30 min]` | `[supervision]` | `[continu]` |
| Redémarrages inattendus | `[≥ 2 machines]` | `[supervision]` | `[continu]` |
| Temps de réponse | `[+ 50 % sur 15 min]` | `[supervision]` | `[continu]` |

**Critère de passage à l'anneau suivant** : `[tous les seuils respectés pendant [n] jours ET aucun incident bloquant ouvert]`

**Validation** — Au moins un indicateur **fonctionnel** est obligatoire : un service peut répondre correctement tout en ayant cessé de faire son travail (§6.8). Un formulaire rempli après le début de l'intervention est irrecevable.

---

### D.7 — Plan de retour arrière

**Identifiant** `RB-[aaaa]-[nnn]` · **Rattaché à** `[CHG-...]`

| Champ | Valeur |
|---|---|
| Mécanisme retenu | `[ ] instantané  [ ] sauvegarde  [ ] redéploiement d'image  [ ] désinstallation vérifiée  [ ] double partition  [ ] bascule bleu/vert` |
| **Testé le** (O) | `[date]` — sur `[topologie représentative : oui/non, écarts]` |
| **Durée mesurée** (O) | `[hh:mm]` |
| Périmètre couvert | `[ ] binaires  [ ] configuration  [ ] schéma de données  [ ] caches  [ ] files de messages  [ ] effets externes` |
| **Point de non-retour** (O) | `[instant précis]` ou `[aucun]` |
| Ce que le retour arrière **ne restaure pas** | `[transactions depuis l'instantané · état des systèmes tiers · notifications déjà émises]` |
| Critère de déclenchement | `[renvoi D.6]` |
| Décideur | `[nom]` |
| Vérification post-retour | `[contrôles à réaliser pour confirmer l'état antérieur]` |

**Validation** — Un plan dont la durée n'a pas été chronométrée sur une topologie représentative n'est pas un plan : c'est une intention (§18.8).

---

### D.8 — Fiche d'obsolescence d'actif

**Identifiant** `OBS-[aaaa]-[nnn]`

| Champ | Valeur |
|---|---|
| Actif ou population | `[ ]` · Nombre `[ ]` |
| Composant concerné | `[système / base de données / runtime / matériel / micrologiciel]` |
| **Date de fin de support** | `[ ]` · Type : `[ ] fonctionnelle [ ] support [ ] support de sécurité [ ] support étendu` |
| **Source et date de vérification** | `[page officielle, consultée le ...]` |
| Criticité / exposition | `[C1-C4]` / `[ ]` |
| Éligibilité au support étendu | `[ ] vérifiée actif par actif — résultat : [ ]` |

**Trois options chiffrées, sur la durée complète** *(le statu quo est obligatoire)*

| Option | Coût total | Risque résiduel | Faisabilité |
|---|---|---|---|
| Support étendu `[n]` ans | `[ ]` | `[ ]` | `[ ]` |
| Migration / remplacement | `[ ]` | `[ ]` | `[ ]` |
| **Statu quo** | `[compensations + urgences + astreinte + risque]` | `[ ]` | `[ ]` ou `[indisponible : motif]` |
| Retrait du service | `[ ]` | `[ ]` | `[ ]` |

**Décision** `[option]` · **Décideur** `[nom]` · **Date** `[ ]` · **Financement** `[exercice, montant]` · **Jalons** `[ ]` · **Point de non-retour** `[ ]`

---

### D.9 — Clauses contractuelles MCS

**Identifiant** `CLA-MCS-[nn]` — à insérer en annexe technique du contrat.

| # | Clause | Texte type | Obtenue |
|---|---|---|---|
| 1 | Délais par criticité | « Le Prestataire applique les correctifs de sécurité selon les délais figurant en annexe [X], décomptés à partir de la publication du correctif par l'éditeur. » | `[ ]` |
| 2 | Périmètre nominatif | « Le périmètre couvert est défini par la liste d'actifs annexée, mise à jour trimestriellement et contradictoirement. » | `[ ]` |
| 3 | **Restitution de données** | « Le Prestataire fournit mensuellement, dans un format exploitable et exportable, l'état de mise à jour de chaque actif du périmètre, **y compris la liste des actifs non joignables et leur motif**. » | `[ ]` |
| 4 | Notification | « Le Prestataire notifie sous 24 heures toute vulnérabilité activement exploitée affectant un actif du périmètre. » | `[ ]` |
| 5 | Transparence des versions | « Le Prestataire communique sur demande les versions déployées et son propre calendrier d'obsolescence. » | `[ ]` |
| 6 | Droit d'audit et de test | « Le Client peut faire réaliser un contrôle technique du périmètre, avec un préavis de [30] jours. » | `[ ]` |
| 7 | Sous-traitance | « Le Prestataire déclare ses sous-traitants intervenant sur le périmètre et leur impose les mêmes obligations. » | `[ ]` |
| 8 | **Escalade des impossibilités** | « Toute impossibilité de correction est notifiée sous [5] jours ouvrés, avec sa cause et une proposition de mesure compensatoire. » | `[ ]` |
| 9 | Accès aux preuves | « Le Prestataire met à disposition les journaux d'administration et les preuves d'application relatifs au périmètre. » | `[ ]` |
| 10 | Réversibilité | « En fin de contrat, le Prestataire restitue l'inventaire complet, **l'historique de mise à jour** et la documentation d'exploitation, dans un format ouvert. » | `[ ]` |
| 11 | Assistance au décommissionnement | « Le Prestataire assiste au retrait des accès, comptes et secrets le concernant, et en fournit la preuve. » | `[ ]` |
| 12 | Conséquence d'un manquement | « Le non-respect constaté deux mois consécutifs déclenche un plan de retour à la conformité sous contrôle du Client. » | `[ ]` |

**Priorité si vous ne pouvez en obtenir que trois** : 3, 8, 2.
**En cas de refus** : consigner la demande et le refus **par écrit** (§13.8), documenter le risque accepté, préparer l'architecture de sortie.

---

### D.10 — Questionnaire fournisseur

**Identifiant** `QF-[aaaa]-[nnn]` · **Fournisseur** `[ ]` · **Produit/service** `[ ]` · **Date** `[ ]`

| # | Question | Réponse | Preuve fournie |
|---|---|---|---|
| 1 | Politique de publication des correctifs de sécurité : fréquence, canaux, délai entre découverte et publication | `[ ]` | `[ ]` |
| 2 | Combien de versions maintenez-vous en sécurité, et pendant combien de temps ? | `[ ]` | `[ ]` |
| 3 | Quel préavis donnez-vous avant une fin de support ? | `[ ]` | `[ ]` |
| 4 | Comment nous notifiez-vous une vulnérabilité affectant votre produit ? | `[ ]` | `[ ]` |
| 5 | Fournissez-vous un inventaire des composants du produit ? Sous quel format ? | `[ ]` | `[ ]` |
| 6 | Publiez-vous des déclarations d'exploitabilité ? | `[ ]` | `[ ]` |
| 7 | Les postes utilisés pour administrer notre périmètre sont-ils **dédiés** à l'administration ? | `[ ]` | `[ ]` |
| 8 | Les comptes utilisés chez nous nous sont-ils propres ? | `[ ]` | `[ ]` |
| 9 | Comment cloisonnez-vous vos clients ? | `[ ]` | `[ ]` |
| 10 | Les actions d'administration sont-elles journalisées, et pouvons-nous obtenir ces journaux ? | `[ ]` | `[ ]` |
| 11 | **Quel est votre propre niveau de MCS, et comment le démontrez-vous ?** | `[ ]` | `[ ]` |
| 12 | Quelles données conservez-vous, où, et comment les restituez-vous en fin de contrat ? | `[ ]` | `[ ]` |

**Cotation** : `[ ]` réponse documentée avec preuve · `[ ]` réponse déclarative · `[ ]` sans réponse. Toute question sans réponse devient une ligne de risque documentée.

---

### D.11 — Journal de crise vulnérabilité

**Identifiant** `CRI-[aaaa]-[nnn]` · **Pilote** `[nom]` · **Greffier** `[nom]` · **Ouverture** `[date, heure]`

| Heure | Information reçue | **Source** | Statut | Décision | Décideur | Action | Responsable | Échéance |
|---|---|---|---|---|---|---|---|---|
| `[hh:mm]` | `[ ]` | `[ ]` | `[fait/hypothèse/piste]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Encadré permanent — état de la connaissance**

| Question | Réponse à l'instant `[hh:mm]` |
|---|---|
| Depuis quand l'actif est-il exposé et vulnérable ? | `[ ]` |
| Quels journaux couvrent cette période ? | `[ ]` |
| Permettraient-ils de détecter ce type d'exploitation ? | `[ ]` |
| **Peut-on établir l'absence de compromission ?** | `[ ] oui  [ ] non — préciser` |

**Clôture** : critères de sortie atteints `[ ]` · mesures d'urgence levées ou converties en compensations `[ ]` · retour d'expérience planifié le `[ ]`

---

### D.12 — Matrice de responsabilité cloud

**Identifiant** `RESP-CLOUD-[nn]` · **Revue** `[semestrielle]`

| Service | Modèle | Le fournisseur maintient | Nous maintenons | Fenêtre imposée | Préavis | **Preuve disponible** | Propriétaire |
|---|---|---|---|---|---|---|---|
| `[ ]` | `[IaaS/PaaS/SaaS/fonctions]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ] oui [ ] non` | `[ ]` |

**Ligne obligatoire par service** : version actuellement utilisée `[ ]` · **date de fin de support de cette version** `[ ]` · source `[ ]`.

**Validation** — Toute ligne dont la colonne « preuve disponible » est vide alimente l'annexe des périmètres non couverts de D.1.

---

### D.13 — Dossier de preuves

**Identifiant** `PRV-[aaaa]` · **Constitué en continu** · **Responsable** `[nom]`

| # | Pièce | Présente | Date de la dernière mise à jour | Emplacement |
|---|---|---|---|---|
| 1 | Périmètre de référence daté, avec sources réconciliées et zones non couvertes | `[ ]` | `[ ]` | `[ ]` |
| 2 | Politique MCS approuvée (D.1) | `[ ]` | `[ ]` | `[ ]` |
| 3 | RACI et comitologie (D.3) | `[ ]` | `[ ]` | `[ ]` |
| 4 | Arbre de décision de triage, daté et validé | `[ ]` | `[ ]` | `[ ]` |
| 5 | Journaux de campagne, dont traîne longue qualifiée | `[ ]` | `[ ]` | `[ ]` |
| 6 | **Preuves d'état sur échantillon**, indépendantes des outils | `[ ]` | `[ ]` | `[ ]` |
| 7 | Registre des dérogations (D.4) | `[ ]` | `[ ]` | `[ ]` |
| 8 | Registre des exclusions (scan, protection des postes) | `[ ]` | `[ ]` | `[ ]` |
| 9 | Comptes rendus de comité, avec **décisions** | `[ ]` | `[ ]` | `[ ]` |
| 10 | Indicateurs historisés, avec définitions et ruptures marquées | `[ ]` | `[ ]` | `[ ]` |
| 11 | Procès-verbaux de décommissionnement (D.14) | `[ ]` | `[ ]` | `[ ]` |

**Contrôle de crédibilité** — Si les dates de production de plus de la moitié des pièces sont groupées sur moins d'un mois, le dossier a été reconstitué : cela se voit, et cela se retourne contre vous (§39.2).

---

### D.14 — Procès-verbal de décommissionnement

**Identifiant** `PVD-[aaaa]-[nnn]` · **Actif** `[ ]` · **Mis en service le** `[ ]`

| # | Étape | Fait | Date | Preuve | Responsable |
|---|---|---|---|---|---|
| 1 | Usage réel mesuré avant décision | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 2 | Décision de retrait et préavis diffusé | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 3 | **Extinction avant suppression**, observation ≥ 1 cycle métier | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 4 | Dépendances identifiées et traitées | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 5 | Données migrées / archivées / **effacées avec attestation** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 6 | Enregistrements de noms et alias supprimés | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 7 | Publications externes retirées, vérifiées depuis l'extérieur | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 8 | Règles de filtrage supprimées | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 9 | **Comptes, clés, secrets, jetons, autorisations déléguées révoqués côté fournisseur** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 10 | Certificats traités (révocation **ou** destruction de clé documentée) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 11 | Retrait des outils, **historiques préservés** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 12 | Décision sur les sauvegardes, avec date de suppression | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 13 | Matériel et licences traités | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 14 | Contrats résiliés | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 15 | **Vérification à J+[90]** — contrôles du §35.11 | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Signatures** — Propriétaire métier `[nom, date]` · Propriétaire technique `[nom, date]`

**Validation** — Le décommissionnement n'est pas clos tant que la ligne 15 n'est pas renseignée. Un PV sans double signature est irrecevable.

---


## Annexe E — Familles d'outils et exemples de référence

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** Péremption recommandée : **12 mois**.
> Organisée par **famille**, avec deux à trois exemples représentatifs. **Aucun tarif détaillé** : les prix sont négociés, dépendants des offres groupées, régionaux et rapidement obsolètes. Seuls les *modèles* de facturation figurent ici, car eux seuls sont structurants pour un budget. Aucun outil n'est une solution universelle.

### E.1 Comment lire les modèles de licence

| Modèle | Ce qu'il implique pour le budget |
|---|---|
| **Gratuit / open source** | Gratuit à l'acquisition ; l'exploitation, l'intégration et le maintien restent à financer — souvent le poste principal |
| **Par actif** | Le coût croît avec la découverte : mieux inventorier augmente la facture (incitation perverse, §19.9) |
| **Par volume analysé** | Coût lié au nombre d'analyses, d'images ou de charges de travail |
| **À la consommation** | Coût lié aux appels, aux données ou à la durée |
| **Sur devis** | Prix non public, fortement dépendant du périmètre et de la négociation |

### E.2 Les familles

| Famille | Exemples représentatifs | Modèle | Limites concrètes |
|---|---|---|---|
| **Scan de vulnérabilités** | Solutions commerciales de scan authentifié (Tenable, Qualys, Rapid7) · alternative libre : OpenVAS/Greenbone | Par actif · libre | Faux positifs de rétroportage · historique rarement portable · systèmes industriels et services en ligne hors champ |
| **Découverte externe** | Modules EASM des mêmes éditeurs · services spécialisés | Par domaine · sur devis | Peut attribuer à tort des actifs · ne voit rien de l'interne |
| **Déploiement Windows** | Configuration Manager · Intune · Windows Update for Business · WSUS (en fin de cycle) | Inclus dans des offres groupées · par poste | Applications tierces non couvertes nativement · reporting difficilement exportable |
| **Déploiement Linux** | Ansible · Red Hat Satellite · Landscape · SUSE Manager · dépôts internes | Libre · par nœud · abonnement | Orchestration des redémarrages à construire |
| **Applications tierces** | Gestionnaires de paquets Windows (winget, Chocolatey) · modules tiers des outils de déploiement | Libre · option payante | Couverture du catalogue variable sur les applications métier |
| **Gestion de flotte** | Intune · Jamf · solutions équivalentes | Par appareil | Ne couvre que les appareils enrôlés |
| **Analyse de composition** | Dependabot/Renovate · Snyk · OWASP Dependency-Check · Trivy | Libre · par développeur · par dépôt | Bruit élevé sans analyse d'atteignabilité |
| **Analyse d'images** | Trivy · Grype · modules de registres | Libre · inclus | Ne voit pas ce qui est ajouté à l'exécution |
| **Contrôle de configuration** | OpenSCAP · outils natifs de politique · Ansible | Libre · inclus | Référentiels génériques inadaptés aux applications métier |
| **Posture cloud** | Modules natifs des fournisseurs · solutions tierces | À la consommation · par ressource | Multi-cloud = dispositifs multiples à maintenir |
| **Gestion de secrets** | HashiCorp Vault · coffres natifs des fournisseurs | Libre · à la consommation | Devient un actif de niveau 0 · rotation à répercuter |
| **Inventaire / CMDB** | Modules ITSM · GLPI · solutions CAASM | Par actif · libre | Vaut ce que valent ses sources |
| **Ticketing / workflow** | Jira · GLPI · modules ITSM | Par utilisateur | Ne règle ni l'absence de propriétaire ni la capacité |
| **Journalisation** | Solutions SIEM · piles ouvertes (OpenSearch, Loki) | Par volume ingéré · libre | Le coût croît avec la rétention — arbitrage à faire tôt |
| **Découverte industrielle** | Solutions d'écoute passive OT | Sur devis | Ne voit que ce qui communique |

### E.3 Critères de sélection, par ordre d'importance

1. **Exportabilité des données brutes** et de l'historique en format ouvert — le critère décisif à cinq ans (§19.1).
2. Capacité à calculer la couverture sur **votre** périmètre de référence, pas sur le sien.
3. Granularité de ciblage : anneaux, exclusions documentées, populations.
4. Couverture réelle des applications tierces et des composants intermédiaires.
5. Fonctionnement hors réseau interne.
6. Coût total : licence **plus** intégration **plus** exploitation.

---


## Annexe F — Cadre réglementaire et normatif comparatif

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** Les statuts évoluent ; revérifier à chaque revue.

| Texte | Qui est concerné | Exigence MCS principale | Preuve attendue | Statut au 30/07/2026 |
|---|---|---|---|---|
| **NIS2** (directive UE) | Entités essentielles et importantes, par secteur et taille | Gestion des risques, dont vulnérabilités et correctifs | Politique, inventaire, mesure, incidents | Transposition française **non promulguée** ; dossier législatif ouvert |
| **ReCyF** (ANSSI) | Entités visées par la transposition | Une vingtaine d'objectifs, avec moyens acceptables de conformité et proportionnalité | Analyse d'écart, preuve par objectif | **Version de travail** du 17/03/2026 — non opposable |
| **Cyber Resilience Act** — règlement (UE) 2024/2847 | **Fabricants** de produits à éléments numériques (voir aussi importateurs, distributeurs, art. 19-20) | **Art. 13** : gestion des vulnérabilités, période de support, inventaire des composants · **Art. 14** : signalement · **Art. 16** : plateforme unique · **Art. 69** : régime transitoire | Documentation technique, avis publiés, notifications via la plateforme | En vigueur (10/12/2024) · chapitre relatif aux organismes d'évaluation depuis le 11/06/2026 · **art. 14 à compter du 11/09/2026** · application générale au 11/12/2027 [S-04] [S-05] [S-06] |
| **ISO/IEC 27001 / 27002** | Volontaire, souvent exigé par les clients | Gestion des vulnérabilités techniques, des configurations, des changements | Processus documenté + preuve d'application sur échantillon | Version 2022 en vigueur |
| **IEC 62443** | Systèmes industriels : exploitants, intégrateurs, fabricants | Gestion des correctifs adaptée au contexte industriel, zones et conduits | Plan de MCS industriel, répartition des rôles | Série en vigueur |
| **Hébergement de données de santé** | Hébergeurs, et clients par ricochet | Maintien et traçabilité, obligations contractuelles | Certification, rapports | En vigueur |
| **SecNumCloud** | Fournisseurs cloud pour usages sensibles | Exigences détaillées de MCS et de transparence client | Qualification, rapports | En vigueur — vérifier la version applicable |
| **PCI DSS** | Traitement de données de paiement | Le plus prescriptif : délais chiffrés, scans périodiques internes et externes | Rapports de scan, journaux de correction | Version 4.x en vigueur |
| **DORA** | Secteur financier européen | Gestion du risque informatique, tests, maîtrise des tiers critiques | Registre des prestataires, tests, incidents | En vigueur |
| **RGPD art. 32** | Tout responsable de traitement | Mesures appropriées à l'état de l'art | Traçabilité des décisions et des écarts | En vigueur |
| **BOD 26-04 (CISA)** | **Agences civiles fédérales américaines uniquement** | Priorisation par le risque, délais différenciés | — | Publiée le 10/06/2026. **Modèle méthodologique, aucune obligation en Europe** |

**Ce qui reste incertain au 30/07/2026** : le calendrier de promulgation du texte français de transposition · la version définitive du ReCyF et l'éventuelle évolution de ses objectifs · les modalités pratiques d'exercice des obligations de signalement produit.

---


## Annexe G — Catalogue des faux positifs, pièges et illusions

*Classé par domaine. Pour chacun : le mécanisme, et le contrôle qui le détecte.*

### G.1 Scan et détection

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 1 | Faux positif de rétroportage | Le numéro amont ne bouge pas | Comparer la révision éditeur + avis de la distribution |
| 2 | Service installé mais désactivé | Présence ≠ exécution | Vérifier l'état d'activation |
| 3 | Composant non chargé | Dépendance déclarée, jamais appelée | Atteignabilité, déclaration du fournisseur |
| 4 | Bannière modifiée | Version annoncée fausse | Scan authentifié |
| 5 | Correspondance produit erronée | Nomenclatures divergentes | Table de correspondance maintenue |
| 6 | Doublon agent / scan réseau | Deux sources, un actif | Identifiant pivot |
| 7 | Constat sur actif décommissionné | Nettoyage non fait | Réconciliation d'inventaire |
| 8 | Adresse réattribuée | L'actif détecté n'est pas le vôtre | Réconciliation |
| 9 | Constat sur image de base déjà corrigé | Analyse de la mauvaise couche | Analyser l'image finale |
| 10 | Base de détection périmée | L'outil ne sait pas chercher | Suivre l'âge du contenu |
| 11 | **« Non scanné » lu comme « non vulnérable »** | Trois états identiques dans un rapport | Les trois questions du §15.8 |
| 12 | Exclusion silencieuse | Actif retiré « temporairement » | Registre des exclusions revu en comité |

### G.2 Triage et pilotage

| # | Piège | Mécanisme |
|---|---|---|
| 13 | Seuil de gravité seul | Ignore exposition et exploitation |
| 14 | Score composite pondéré | Pondérations indéfendables ; bloque si une entrée manque |
| 15 | Discontinuité de modèle de score | Tous les scores bougent sans qu'aucun correctif ne soit appliqué |
| 16 | Dépriorisation sans date de revue | Devient un oubli |
| 17 | Faux positif déclaré sans preuve | Vide la file sans travailler |
| 18 | Constat ouvert depuis 6 mois | Dérogation non formalisée, décidée par personne |
| 19 | Compter les vulnérabilités fermées | Récompense l'agitation, pas le résultat |

### G.3 Déploiement

| # | Piège | Mécanisme |
|---|---|---|
| 20 | Correctif installé, service non redémarré | Code vulnérable toujours en mémoire |
| 21 | Correctif en mode observation jamais activé | Protection incomplète, croyance complète |
| 22 | Anneau pilote non représentatif | Valide l'installation, pas la non-régression |
| 23 | Critères d'arrêt discutés pendant l'incident | Toujours interprétés « on continue » |
| 24 | Retour arrière jamais testé | Une intention, pas un plan |
| 25 | Point de non-retour non identifié | Migration de schéma franchie sans le savoir |
| 26 | Traîne longue non qualifiée | Les 3 % les plus risqués |
| 27 | Recette non représentative | Fausse confiance, pire que pas de test |

### G.4 Configuration et identités

| # | Piège | Mécanisme |
|---|---|---|
| 28 | Référentiel appliqué sans dérivation | Contrôles désactivés un par un, baseline fictive |
| 29 | Contrôle désactivé pendant un incident | Jamais reversé |
| 30 | Rotation non répercutée | Ancien secret toujours valide |
| 31 | Autorisation déléguée | Survit au changement de mot de passe |
| 32 | Compte de service partagé | Une compromission se propage |
| 33 | Compte de secours non testé | Ne fonctionnera pas le jour venu |
| 34 | Certificat interne oublié | Expiration = panne difficile à diagnostiquer |

### G.5 Périmètre et couverture

| # | Piège | Mécanisme |
|---|---|---|
| 35 | Taux calculé sur les actifs connus | Biaisé **dans le sens favorable** |
| 36 | Actif déclaré, actif, hors outil de gestion | Tout le monde le croit géré |
| 37 | Machine éteinte non décommissionnée | Comptes et enregistrements survivants |
| 38 | Agent absent | La machine n'apparaît pas comme non conforme, elle n'apparaît plus |
| 39 | Additionner les rapports de plusieurs outils | Périmètres recouvrants, définitions divergentes |
| 40 | Actif éphémère | Absent des inventaires réseau |

### G.6 Contractuel et fournisseurs

| # | Piège | Mécanisme |
|---|---|---|
| 41 | SLA de disponibilité seul | Pousse structurellement au report des correctifs |
| 42 | Éligibilité au support étendu supposée | Programme grand public ≠ parc géré |
| 43 | Prérequis de version imposé par un éditeur | Vous héritez de son calendrier |
| 44 | Accès prestataire permanent | Exposition permanente |
| 45 | Déclaration fournisseur sans donnée | Confiance, pas preuve |

### G.7 Industriel, cloud, services en ligne, produit

| # | Piège | Mécanisme |
|---|---|---|
| 46 | Scan actif sur réseau industriel | Défaut d'automate, perte durable de confiance |
| 47 | Support amovible du prestataire | Vecteur d'entrée historique |
| 48 | Pièce de rechange non prépatchée | Remise en service en version ancienne |
| 49 | Version de service managé hors référentiel d'obsolescence | Migration subie |
| 50 | Fonctionnalité activée par défaut par le fournisseur | Exposition élargie sans décision |
| 51 | « C'est du SaaS, c'est maintenu » | Configuration, identités, intégrations restent à vous |
| 52 | Correctif produit publié sans mesure d'adoption | Le risque client ne diminue pas |
| 53 | Qualification réglementaire par gamme | Un produit exclu masque des produits inclus |

---


## Annexe H — Calendrier des échéances et ressources

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** C'est l'annexe la plus périssable du document.

### H.1 Échéances datées

| Date | Objet |
|---|---|
| 14/10/2025 | Fin de support de Windows 10 |
| 15/04/2026 | Priorisation de l'enrichissement des fiches du NVD par le NIST |
| 11/06/2026 | Applicabilité du chapitre du CRA relatif aux organismes d'évaluation de la conformité |
| 15/06/2026 | Début de publication des scores EPSS v5 — **rupture de série** |
| 24 et 27/06/2026 | Expiration des certificats de démarrage sécurisé émis en 2011 (KEK CA, UEFI CA) |
| 11/09/2026 | Applicabilité des obligations de signalement du CRA |
| 13/10/2026 | Fin de support de Windows 10 Entreprise / IoT LTSB 2016 |
| 19/10/2026 | Expiration du certificat Windows Production PCA 2011 |
| 12/01/2027 | Fin de support étendu de Windows Server 2016 |
| 12/10/2027 | Fin du programme de support étendu **grand public** de Windows 10 — **exclut les machines gérées** |
| 11/12/2027 | Application générale du CRA |

### H.2 Échéances récurrentes sans date fixe

*À intégrer au référentiel d'obsolescence (§12.2), avec vérification à la source.*

| Objet | Cycle typique |
|---|---|
| Distributions Linux à support long | 5 à 10 ans, prolongations par abonnement |
| Moteurs de bases de données | 5 à 8 ans (versions majeures) |
| **Environnements d'exécution applicatifs** | **2 à 4 ans** — principale source d'obsolescence invisible |
| Versions d'orchestrateur de conteneurs | ~14 mois (12 standard + 2 limités) |
| Services managés cloud | Variable, annoncé plusieurs mois à l'avance |
| Équipements réseau — fin de support **de sécurité** | Souvent antérieure de plusieurs années à la fin de vie matérielle |
| Micrologiciels serveurs | 5 à 7 ans après commercialisation |
| Certificats publics | Durées en réduction progressive |

### H.3 Sources de veille et cadence

| Source | Cadence | Usage |
|---|---|---|
| Avis des éditeurs de vos produits C1 | Quotidienne | **Source de vérité** sur les versions |
| Avis des distributions | Quotidienne | Révisions rétroportées |
| Bulletins des centres de réponse nationaux | Quotidienne | Point d'entrée principal |
| Centres de réponse et communautés sectoriels | Hebdomadaire | Ciblage de votre secteur |
| Catalogues d'exploitation avérée | Quotidienne | Déclencheur d'urgence |
| Bases agrégées | Quotidienne | Couverture |
| **Notes de version des services cloud et en ligne** | **Mensuelle** | La ligne la plus faible de la plupart des dispositifs |
| Pages de cycle de vie des éditeurs | Trimestrielle | Référentiel d'obsolescence |
| Publications des agences nationales | Mensuelle | Doctrine, guides, référentiels |

### H.4 Formations et certifications

*Aucune certification ne porte spécifiquement sur le MCS. Les plus utiles au regard de ce cours :*

| Domaine | Utilité réelle |
|---|---|
| Management de la sécurité de l'information | Utile pour la partie gouvernance, preuve et audit |
| Sécurité industrielle | Indispensable si votre périmètre comprend de l'OT |
| Administration système et cloud | Le socle technique des chapitres 2, 3, 30 |
| Gestion des vulnérabilités (certifications éditeurs) | Utile sur l'outil, peu transférable |
| Analyse de risque (méthodes reconnues) | Utile pour la criticité et l'acceptation de risque |

⚠️ Une certification atteste d'une connaissance, pas d'une pratique. Les compétences réellement déterminantes de ce cours — négocier une fenêtre, obtenir un propriétaire, écrire une dérogation défendable — ne s'enseignent pas en formation.

### H.5 Ressources et communautés

Publications des agences nationales de cybersécurité · centres de réponse aux incidents nationaux et sectoriels · groupements professionnels de RSSI · communautés d'utilisateurs de vos outils · conférences sécurité généralistes et sectorielles · publications des éditeurs sur les incidents et les retours d'expérience.

---


## Annexe I — Modèle de données MCS

> Modèle relationnel minimal. Types : `str` texte · `enum` valeur contrôlée · `date` · `bool` · `ref` référence · `int`. Cardinalité : `1` obligatoire unique · `0..1` optionnel · `0..n` multiple.

### I.1 Entité ACTIF

| Champ | Type | Card. | Valeurs contrôlées / format | Obligatoire à la création |
|---|---|---|---|---|
| `id_actif` | str | 1 | Identifiant interne stable, **jamais réutilisé** | Oui |
| `ids_sources` | str | 0..n | `{source}:{identifiant natif}` — un par outil | Non |
| `nom` | str | 1 | Nom d'usage | Oui |
| `type` | enum | 1 | serveur · poste · mobile · réseau · sécurité · hyperviseur · conteneur · industriel · périphérique · service_en_ligne · identité_applicative · certificat | Oui |
| `proprietaire_metier` | ref | 0..1 | Personne ou rôle géré | Non — un actif découvert s'enregistre **sans** propriétaire |
| `suppleant_metier` | ref | 0..1 | | Non |
| `proprietaire_technique` | ref | 0..1 | | Non |
| `suppleant_technique` | ref | 0..1 | | Non |
| `criticite` | enum | 0..1 | C1 · C2 · C3 · C4 | Non |
| `exposition` | enum | 0..1 | internet · bureautique · administration · industriel · isolé · inconnue | Non |
| `environnement` | enum | 1 | production · recette · développement · laboratoire · formation · secours | Oui |
| `classification_donnees` | enum | 0..1 | publique · interne · confidentielle · sensible | Non |
| `perimetre_reglementaire` | enum | 0..n | santé · paiement · industriel · produit · aucun | Non |
| `systeme` / `version` | str | 0..1 | | Non |
| `composants` | ref | 0..n | → COMPOSANT | Non |
| `statut_support` | enum | 0..1 | supporté · support_étendu · hors_support · inconnu | Non |
| `date_fin_support` | date | 0..1 | | Non |
| `source_fin_support` | str | 0..1 | Référence + date de consultation | Si `date_fin_support` renseignée |
| `fournisseur` / `contrat` | ref | 0..1 | | Non |
| `fenetre_maintenance` | str | 0..1 | Expression récurrente | Non |
| `outils_couverture` | ref | 0..n | → OUTIL, avec rôle (déploiement / scan / protection / sauvegarde) | Non |
| **`first_seen`** | date | 1 | Première observation, toutes sources | Oui (automatique) |
| **`last_seen`** | date | 1 | Dernière observation | Oui (automatique) |
| **`confiance`** | enum | 1 | confirmée · probable · à_vérifier | Oui |
| **`source_decouverte`** | enum | 1 | cmdb · annuaire · scan · agent · hyperviseur · api_cloud · orchestrateur · comptabilité · déclaration · manuel | Oui |
| **`statut_cycle_vie`** | enum | 1 | découvert · en_service · orphelin · en_extinction · décommissionné | Oui |
| `motif_disparition` | enum | 0..1 | décommissionné · renommé · migré · perdu_de_vue · doublon | Si statut = décommissionné |
| `derniere_tentative_scan` | date | 0..1 | | Non |
| `dernier_succes_scan` | date | 0..1 | **Distinct du précédent** | Non |
| `derniere_preuve_conformite` | ref | 0..1 | → PREUVE | Non |
| `derogations_en_cours` | ref | 0..n | → DEROGATION | Non |

⚠️ **Aucun champ de propriété n'est obligatoire à la création.** Un actif découvert sans propriétaire doit pouvoir être enregistré avec `statut_cycle_vie = orphelin` — le rejeter par contrainte de champ obligatoire revient à effacer précisément ce qu'on cherche à découvrir.

### I.2 Entités liées

| Entité | Champs clés |
|---|---|
| **COMPOSANT** | `id` · `actif` (ref) · `type` (base_de_données / runtime / serveur_applicatif / bibliothèque / micrologiciel / pilote) · `nom` · `version` · `statut_support` · `date_fin_support` · `proprietaire_couche` (ref) |
| **CONSTAT** | `id` · `origine` (scan / avis / pentest / audit / incident / bug_bounty / configuration / secret / architecture) · `identifiant_externe` (0..1) · `statut_qualification` · `actifs` (0..n) · `decision_triage` · `horloge_risque_debut` · `horloge_sla_debut` · `temps_suspendu` |
| **DEROGATION** | Les champs de D.4 · `actifs` (0..n) · `nb_renouvellements` · `signataire` · `date_expiration` |
| **PREUVE** | `id` · `type` (état_constaté / rapport_console / journal / attestation) · `date_collecte` · `perimetre` · `methode` · `actifs_non_joignables` · `empreinte` |
| **OUTIL** | `id` · `nom` · `role` · `perimetre_theorique` · `date_derniere_extraction` · `format_export` |
| **CONTRAT** | `id` · `fournisseur` · `perimetre` · `delais_engages` · `restitution_donnees` (bool) · `date_echeance` |

### I.3 Relations

| Relation | Cardinalité |
|---|---|
| ACTIF `dépend de` ACTIF | 0..n |
| ACTIF `est construit depuis` MODELE | 0..1 |
| ACTIF `est couvert par` OUTIL | 0..n, avec rôle |
| ACTIF `porte` COMPOSANT | 0..n |
| ACTIF `utilise` COMPTE | 0..n |
| CONSTAT `affecte` ACTIF | 1..n |
| DEROGATION `couvre` CONSTAT | 1..n |
| PREUVE `atteste` ACTIF `pour` CONSTAT | 1..n |

### I.4 Périmètre maître et populations éligibles

Le périmètre de référence est le **périmètre maître** : l'union de tout ce qui est connu.

```
Périmètre maître = ∪ (toutes les sources d'inventaire)
   incluant : actifs orphelins · actifs en extinction · actifs de service
   excluant : rien — les exclusions sont documentées, jamais retirées
```

⚠️ **Le périmètre maître n'est pas le dénominateur de tout indicateur.** Un service en ligne n'est pas éligible à un indicateur de correctif système ; un automate n'est pas éligible au scan actif ; un actif arrêté en cours de décommissionnement n'est pas éligible à la conformité aux correctifs ; un certificat ne s'évalue pas avec les contrôles d'un serveur. Utiliser le périmètre maître comme dénominateur universel produit des taux artificiellement bas et indéfendables.

| Notion | Définition | Champ correspondant |
|---|---|---|
| **Périmètre maître** | Tout ce qui est connu, sans exclusion silencieuse | tous les ACTIF |
| **Population éligible** | Sous-ensemble auquel le contrôle **s'applique** | filtre explicite par indicateur |
| **Population mesurée** | Actifs éligibles effectivement évalués | `dernier_succes_scan` renseigné |
| **N/A** | Hors population éligible, **avec motif** | `motif_na` |
| **Non mesuré** | Éligible mais non évalué. **Jamais conforme par défaut** | éligible ∧ `dernier_succes_scan` vide |

### I.5 Règles de qualité et contrôles

| # | Règle | Requête | Fréquence |
|---|---|---|---|
| 1 | Aucun actif en service sans deux propriétaires | `statut = en_service ∧ (prop_metier vide ∨ prop_tech vide)` | Mensuelle |
| 2 | Aucun actif en service sans criticité ni exposition | `statut = en_service ∧ (criticite vide ∨ exposition vide)` | Mensuelle |
| 3 | Date de fin de support renseignée ou motif | `date_fin_support vide ∧ motif vide` | Trimestrielle |
| 4 | Couverture ou exclusion documentée | `outils_couverture vide ∧ exclusion vide` | Mensuelle |
| 5 | Actif décommissionné avec PV | `statut = décommissionné ∧ pv vide` | Trimestrielle |
| 6 | Actif non revu depuis N jours | `last_seen < aujourd'hui - 90` | Mensuelle |
| 7 | Écart entre sources supérieur au seuil | Réconciliation (§10.3) | Mensuelle |
| 8 | Orphelin depuis plus de 30 jours | `statut = orphelin ∧ first_seen < -30 j` | Mensuelle |

### I.6 Exemple d'enregistrement

```yaml
id_actif: SRV-0142
ids_sources: [cmdb:CI00873, scan:asset-51190, hyperviseur:vm-2201]
nom: srv-app-crm-02
type: serveur
proprietaire_metier: directeur.commercial
proprietaire_technique: m.ferhaoui
criticite: C2
exposition: bureautique
environnement: production
classification_donnees: confidentielle
systeme: "Linux LTS 12"
version: "12.7"
composants:
  - {type: runtime, nom: "runtime applicatif A", version: "8.3", statut_support: hors_support,
     date_fin_support: 2023-03-31, proprietaire_couche: equipe.applicative}
statut_support: supporté
date_fin_support: 2028-06-30
source_fin_support: "page officielle éditeur, consultée le 30/07/2026"
first_seen: 2019-04-11
last_seen: 2026-07-29
confiance: confirmée
source_decouverte: cmdb
statut_cycle_vie: en_service
dernier_succes_scan: 2026-07-28
derogations_en_cours: [DER-2027-014]
```

---


## Annexe J — Workflow et modèle de ticket de remédiation

### J.1 États et transitions

```
NOUVEAU ──qualification──► QUALIFIÉ ──────► FAUX POSITIF (clos + démonstration)
                              │
                         triage (§16.3)
                              ▼
                          AFFECTÉ ◄──────► CONFLIT DE PROPRIÉTÉ (délai borné)
                              │                      │
                      acceptation propriétaire       └──► arbitrage comité
                              ▼
                          PLANIFIÉ ────────► DÉROGATION (ouvert, D.4)
                              │              RISQUE ACCEPTÉ (ouvert, durable)
                              ▼              N/A (clos, motif)
                       EN CORRECTION
                              ▼
                        À VÉRIFIER ────────► ÉCHEC ──► retour à PLANIFIÉ
                              ▼
                            CLOS ◄────────── NOUVELLE OCCURRENCE (ticket lié)
```

### J.2 Droits de transition

| Transition | Qui peut la déclencher |
|---|---|
| Nouveau → Qualifié | Analyste sécurité |
| Qualifié → Faux positif | Analyste sécurité, **avec démonstration jointe** |
| Qualifié → Affecté | Automatique, depuis le propriétaire d'actif |
| Affecté → Conflit de propriété | Propriétaire désigné, sous 5 j ouvrés |
| Conflit → Affecté | Comité MCS uniquement |
| Planifié → Dérogation | Propriétaire métier (signature D.4) |
| Planifié → Risque accepté | Selon grille C.4 |
| À vérifier → Clos | **Seulement avec preuve rattachée** |
| Clos → réouverture | Interdite : créer une **nouvelle occurrence liée** (J.6) |

### J.3 Champs obligatoires par état

| État | Exigences |
|---|---|
| Qualifié | Statut de qualification · actifs confirmés · vérification d'activation · **origine du constat** |
| Affecté | Propriétaire nominatif · échéance SLA · **chemin dans l'arbre reproduit** |
| Planifié | Fenêtre ou campagne · plan de retour arrière (D.7) |
| En correction | Date de début · intervenant |
| À vérifier | Date d'action · méthode de vérification prévue |
| Clos | **Preuve** conforme aux six champs du §2.9 |
| Dérogation | Les champs de D.4 |
| Risque accepté | Signataire selon C.4 · date de revue · **pas de date d'expiration** (c'est ce qui le distingue de la dérogation) |
| N/A | Motif documenté · population éligible d'origine |

### J.4 Les deux horloges

| Élément | Règle |
|---|---|
| **Horloge de risque** | Départ : connaissance pertinente ou disponibilité d'une correction. **Ne se suspend jamais.** Publiée à la direction |
| **Horloge de traitement (SLA)** | Même départ, suspensions limitativement définies. Pilote l'équipe |
| Compteur complémentaire | Depuis la **détection** → réactivité de la veille |
| Suspensions admises (SLA uniquement) | Attente de correctif éditeur · attente d'information demandée par écrit · gel de production |
| Condition d'une suspension > 5 j | **Mesure compensatoire engagée ou acceptation formelle** |
| Temps suspendu | **Mesuré et affiché séparément** |
| Écart entre les deux horloges | Indicateur de premier plan : sa croissance signale un problème structurel |

### J.5 Règles de déduplication et modèle parent / enfants

| Règle | Application |
|---|---|
| Même identifiant sur plusieurs actifs | **Un** ticket parent, une occurrence enfant par actif |
| Constats corrigés par le **même correctif** | Un ticket parent |
| Même constat remonté par deux outils | Un ticket, deux sources tracées |
| Actifs de propriétaires, fenêtres ou criticités différents | **Occurrences enfants distinctes**, avec leurs propres échéances |

⚠️ Le parent porte la décision de triage et la cause racine ; **les enfants portent l'échéance, le propriétaire et la preuve**. Un parent ne se clôt que lorsque toutes ses occurrences sont closes ou qualifiées.

### J.6 Réouverture ou nouvelle occurrence

| Situation | Traitement |
|---|---|
| Le constat n'avait jamais été réellement corrigé | **Réouverture** de l'occurrence : le délai continue de courir |
| Le constat réapparaît après une correction vérifiée | **Nouvelle occurrence**, liée au ticket parent et à l'occurrence précédente |

Le second cas préserve la justesse des indicateurs de délai tout en rendant la **récurrence visible** : trois occurrences liées sur le même parent signalent une cause racine non traitée (§17.9), presque toujours un modèle ou une image de référence.

### J.7 Escalade — paramétrable par classe

| Déclencheur | C1 | C2 | C3 | Destinataire |
|---|---|---|---|---|
| Pas de réponse du propriétaire | 2 j | 5 j | 10 j | Responsable hiérarchique |
| Conflit de propriété non résolu | 3 j | 5 j | 10 j | Comité MCS |
| Échéance SLA dépassée | Immédiat | 5 j | 15 j | Comité MCS |
| Suspension prolongée | 10 j | 20 j | 30 j | Comité MCS |
| Constat non qualifié depuis | 90 j | 180 j | 180 j | **DSI — requalification obligatoire** |

### J.8 Issues et preuve exigée

| Issue | Nature | Preuve |
|---|---|---|
| **Corrigé** | Définitive | État constaté postérieur à l'action |
| **Atténué** | Temporaire | Mesure décrite, vérifiée active, **date d'expiration** |
| **Dérogation** | Temporaire, bornée | Fiche D.4 signée |
| **Risque accepté** | Durable | Signature C.4, revue périodique, **horloge de risque toujours active** |
| **N/A** | Définitive | Motif et population éligible d'origine |
| **Faux positif** | Définitive | **Démonstration vérifiable par un tiers** |
| **Sans objet** | Définitive | PV de décommissionnement (D.14) |

---


## Annexe K — Dictionnaire d'indicateurs et modèle de maturité

### K.1 Fiches d'indicateurs

*Format complet : formule · numérateur · **population éligible** · dénominateur publié · période · exclusions et N/A · source · propriétaire · fréquence · seuils.*

⚠️ La population éligible se définit **par indicateur** (Annexe I.4). Le périmètre maître est le point de départ, jamais le dénominateur par défaut.

---

**K1 — Couverture d'inventaire**
Formule : `actifs identifiés / actifs estimés du périmètre × 100` · Numérateur : actifs enregistrés · Population éligible : tous types · Dénominateur : estimation argumentée du parc réel · Période : instantané mensuel · Exclusions : aucune · Source : réconciliation multi-sources · Propriétaire : exploitation · Seuils : `< 90 %` alerte, `< 80 %` blocage de tout autre indicateur.

**K2 — Couverture de scan**
Formule : `actifs scannés avec succès / actifs éligibles au scan × 100` · Numérateur : `dernier_succes_scan` dans la période · **Population éligible : actifs scannables** — exclut services en ligne, industriels non scannables, certificats · Dénominateur : population éligible, publié · Exclusions : documentées, listées avec l'indicateur · N/A : motif obligatoire · Fréquence : mensuelle · Seuils : `< 90 %` alerte.

**K3 — Conformité de correctifs**
Formule : `actifs conformes / actifs mesurés × 100` · **Population éligible** : actifs porteurs du composant concerné · Trois valeurs à publier ensemble : conformité dans la population mesurée · **ratio confirmé conforme sur périmètre** (K3 × K2) · **part non mesurée** · Fréquence : mensuelle.

**K4 — Respect des délais**
Formule : `constats clos dans le délai / constats arrivés à échéance × 100` · Population éligible : constats avec échéance SLA dans la période · Exclusions : suspendus — **mais leur horloge de risque reste publiée** · Publier : médiane, **P90**, maximum, volume · Seuils : `< 85 %` alerte.

**K5 — Âge du backlog**
Formule : distribution des durées depuis la première détection · Publier : **médiane · P90 · P95 · maximum · volume de population** · Population éligible : constats ouverts · Piège : la moyenne masque la traîne, le maximum peut être dominé par un cas aberrant.

**K6 — Dette critique échue**
Formule : nombre absolu de constats critiques dont le délai est dépassé · **Jamais en taux** · Population éligible : constats de gravité critique · Fréquence : hebdomadaire · Seuil : toute valeur `> 0` sur actif exposé déclenche une revue.

**K7 — Dérogations**
Trois valeurs : nombre ouvert · **âge moyen et P90** · **nombre renouvelées ≥ 1 fois** · Le nombre seul n'est pas interprétable (§38.9) · Fréquence : mensuelle · Seuil : toute dérogation renouvelée deux fois remonte en comité de direction.

**K8 — Taux de récurrence**
Formule : `occurrences réapparues / occurrences closes sur la période × 100` · Population éligible : occurrences closes il y a plus de 30 jours · Interprétation : signale une cause racine (modèle, image, restauration), pas une mauvaise exécution · Seuil : `> 10 %` déclenche une analyse de cause racine.

**K9 — Taux de retour arrière**
Formule : `déploiements annulés / déploiements réalisés × 100` · Piège : un taux **nul** peut signaler qu'on ne teste pas ou qu'on n'ose pas revenir en arrière · Seuils : `> 10 %` qualité de validation insuffisante ; `= 0 %` sur 12 mois, examiner.

**K10 — Taux d'échec de déploiement**
Formule : `actifs en échec / actifs ciblés × 100` · **Les non-joignables comptent au dénominateur** et sont publiés séparément · Fréquence : par campagne.

**Indicateurs complémentaires** : âge des images et modèles · temps sans redémarrage (P90) · part de changements d'urgence (seuil 15-20 %) · fraîcheur du contenu de détection · nombre d'actifs exposés et tendance · nombre d'orphelins · part des technologies couvertes par une source de veille · âge des exclusions · **écart entre horloge de risque et horloge SLA**.

### K.2 Règles de publication

1. Tout taux est publié **avec son dénominateur, sa population éligible et sa date**.
2. Les populations non mesurées apparaissent comme **« non mesuré »**, jamais comme conformes ni comme absentes.
3. Les exclusions et les N/A sont listés avec l'indicateur, avec leur motif.
4. Les ruptures — périmètre, outil, modèle de score — sont **marquées sur la série**. Lorsque c'est possible, recalculer la période de transition avec l'ancien et le nouveau modèle et publier les deux.
5. Les délais se publient en **médiane, P90 ou P95, maximum et volume**.
6. Le nombre d'indicateurs est **inversement proportionnel** au niveau hiérarchique.
7. Un produit *conformité × couverture* est un **ratio conservateur**, nommé comme tel.
8. Le temps suspendu au titre du SLA reste compté par **l'horloge de risque**.

### K.3 Modèle de maturité — critères de preuve par niveau

| Niveau | Nom | **Preuve exigée pour l'atteindre** |
|---|---|---|
| 0 | Inexistant | — |
| 1 | Réactif | Traces de corrections réalisées, sans processus documenté |
| 2 | Documenté | Politique approuvée · inventaire constitué et daté · propriétaires nommés sur ≥ 80 % du périmètre |
| 3 | Piloté | Délais définis **et mesurés** · registre de dérogations tenu · indicateurs publiés avec dénominateurs · comptes rendus de comité avec décisions |
| 4 | Industrialisé | Automatisation de la collecte, corrélation et vérification · campagnes tracées avec critères d'arrêt · **preuve d'état sur échantillon produite systématiquement** |
| 5 | Adaptatif | Priorisation par exposition et exploitation documentée · MCS *by design* en revue d'architecture · boucle d'amélioration démontrée sur ≥ 4 trimestres · audit interne par sondages |

### K.4 Grille d'auto-évaluation par domaine

| Domaine | Niveau | Preuve citée | Facteur limitant ? |
|---|---|---|---|
| Inventaire et périmètre | `[0-5]` | `[ ]` | `[ ]` |
| Exposition et chemins d'attaque | `[ ]` | `[ ]` | `[ ]` |
| Veille et sources de constats | `[ ]` | `[ ]` | `[ ]` |
| Triage et priorisation | `[ ]` | `[ ]` | `[ ]` |
| Remédiation et workflow | `[ ]` | `[ ]` | `[ ]` |
| Configuration et dérive | `[ ]` | `[ ]` | `[ ]` |
| Identités, secrets, certificats | `[ ]` | `[ ]` | `[ ]` |
| Applications et dépendances | `[ ]` | `[ ]` | `[ ]` |
| Obsolescence et décommissionnement | `[ ]` | `[ ]` | `[ ]` |
| Contextes spécialisés | `[ ]` | `[ ]` | `[ ]` |
| Mesure et preuve | `[ ]` | `[ ]` | `[ ]` |
| Gouvernance et financement | `[ ]` | `[ ]` | `[ ]` |

**Lecture** — Un niveau élevé dans dix domaines ne compense pas un niveau 1 sur l'inventaire : celui-ci **plafonne** la maturité de tout ce qui en dépend. Identifiez les domaines **critiques pour votre contexte** et traitez-les comme facteurs limitants ; la moyenne des douze notes n'a aucune valeur informative.

---


## Annexe L — Checklists de cycle de vie

### L.1 Mise en production
☐ Déclaré à l'inventaire · ☐ Deux propriétaires nommés · ☐ Criticité et exposition attribuées · ☐ Classe de service · ☐ Couvert par un outil de déploiement et de scan · ☐ Fenêtre définie · ☐ Journalisation activée et exportée · ☐ Sauvegarde configurée et testée · ☐ Grille de maintenabilité du §6.14 renseignée · ☐ Fin de support des composants connue.

### L.2 Campagne périodique
☐ Périmètre défini et rapproché du périmètre de référence · ☐ **Vérification préalable sur 3 actifs représentatifs** · ☐ Qualification du correctif en 6 questions · ☐ Écart recette/production mesuré · ☐ Anneaux définis · ☐ **Critères d'arrêt chiffrés, écrits** · ☐ Plan de retour arrière chronométré · ☐ Décideur nommé · ☐ Vérification post-déploiement · ☐ **Traîne longue qualifiée** · ☐ Preuve archivée.

### L.3 Correctif urgent
☐ Information vérifiée à la source · ☐ Exposition mesurée · ☐ **Réduction d'exposition envisagée en premier** · ☐ Cellule constituée avec greffier · ☐ Délai d'observation supprimé — **critères d'arrêt, retour arrière et preuve conservés** · ☐ Recherche de compromission préalable · ☐ Communication direction et métiers · ☐ Demande de changement régularisée sous 48 h · ☐ Retour d'expérience.

### L.4 Système non patchable
☐ Type d'impossibilité qualifié (5 types) · ☐ **Usage réel mesuré** · ☐ Hiérarchie des compensations parcourue de haut en bas · ☐ Compensation avec les 7 attributs · ☐ Dérogation signée par le propriétaire métier · ☐ Date d'expiration · ☐ Contrôle périodique inscrit au comité · ☐ Plan de fin de vie ou de remplacement.

### L.5 Mise à jour hors ligne (industriel)
☐ Source officielle, compte nominatif · ☐ Poste de téléchargement dédié et durci · ☐ **Vérification de signature ou d'empreinte** (double contrôle) · ☐ Analyse antimalware multi-moteurs (double contrôle) · ☐ Support dédié, effacé, identifié · ☐ Sas de transfert · ☐ Validation constructeur écrite · ☐ Matériel de secours prêt · ☐ Application selon procédure · ☐ Tests fonctionnels et de sûreté · ☐ **Preuve d'installation et journal de transfert**.

### L.6 Renouvellement de certificat
☐ Inventaire à jour · ☐ Alertes à 60/30/7 jours · ☐ Renouvellement automatisé si possible · ☐ Déploiement sur **tous** les points d'usage · ☐ Vérification du certificat effectivement présenté · ☐ Ancien certificat révoqué · ☐ Magasins de confiance mis à jour.

### L.7 Migration de version majeure
☐ Fin de support de la version source confirmée à la source · ☐ Compatibilité applicative validée par l'éditeur, **par écrit** · ☐ Recette représentative sur les 4 axes · ☐ Migration de schéma découpée en expansion/contraction · ☐ **Point de non-retour identifié et écrit** · ☐ Plan de retour arrière testé sur topologie représentative · ☐ Fenêtre et communication · ☐ Vérification fonctionnelle post-migration.

### L.8 Changement de fournisseur
☐ Clauses MCS du §13.3 dans le nouveau contrat · ☐ **Restitution de données obtenue** · ☐ Périmètre nominatif annexé · ☐ Inventaire et historique récupérés de l'ancien prestataire · ☐ Accès de l'ancien prestataire révoqués · ☐ Comptes et clés associés supprimés · ☐ Documentation d'exploitation transférée.

### L.9 Décommissionnement
☐ Usage réel mesuré · ☐ Décision et préavis · ☐ **Extinction avant suppression, observation ≥ 1 cycle métier** · ☐ Dépendances identifiées et traitées · ☐ Données migrées/archivées/effacées avec preuve · ☐ Enregistrements de noms supprimés · ☐ Règles de filtrage supprimées · ☐ **Comptes, clés, secrets, jetons, autorisations déléguées révoqués côté fournisseur** · ☐ Certificats révoqués · ☐ Retrait de tous les outils · ☐ Décision sur les sauvegardes, avec date · ☐ Matériel et licences traités · ☐ Contrats résiliés · ☐ **Vérification à J+90** · ☐ Procès-verbal signé par les deux propriétaires.

---


## Ce que vous savez faire

Un cours ne se juge pas à ce qu'il a exposé, mais à ce que son lecteur est capable de faire ensuite. Voici la liste, formulée en actes plutôt qu'en connaissances. Elle sert aussi de grille d'auto-évaluation avant une prise de poste ou un entretien.

### Vous savez établir un périmètre et le défendre

☐ Croiser quatre sources d'inventaire dont une non technique, et **interpréter les écarts** plutôt que choisir un chiffre
☐ Identifier les actifs orphelins et conduire une campagne de désignation de propriétaires
☐ Établir la carte des actifs réellement exposés, et fermer ce qui ne sert plus
☐ Nommer les actifs de niveau 0 de votre organisation — la liste tient sur une page
☐ Déclarer un périmètre non couvert **plutôt que de le laisser invisible**

### Vous savez décider

☐ Qualifier une information en fait vérifié, hypothèse probable ou piste exploratoire
☐ Écarter un faux positif de rétroportage avant de lancer une campagne de 42 serveurs
☐ Appliquer un arbre de décision, et **expliquer votre chemin** devant un comité qui conteste
☐ Défendre une dépriorisation, et savoir ce qui la distingue d'un oubli
☐ Reconnaître qu'un délai accordé par la politique est une ressource, et l'utiliser sans culpabilité

### Vous savez corriger sans casser

☐ Qualifier un correctif en six questions, en lisant les notes de version **en entier**
☐ Composer un anneau pilote qui teste l'usage réel, pas seulement l'installation
☐ Écrire des critères d'arrêt chiffrés **avant** l'intervention, avec un décideur nommé
☐ Identifier un point de non-retour et le déclarer dans la demande de changement
☐ Chronométrer un retour arrière sur une topologie représentative
☐ Qualifier une traîne longue au lieu de clore une campagne à 97 %

### Vous savez traiter ce qui ne se corrige pas

☐ Qualifier une impossibilité parmi ses cinq types, et identifier le bon interlocuteur
☐ Parcourir la hiérarchie des compensations de haut en bas, en écrivant pourquoi vous descendez
☐ Rédiger une dérogation avec ses sept champs, et la faire signer au bon niveau
☐ Vérifier, six mois plus tard, qu'une compensation est **encore active**

### Vous savez réagir

☐ Poser les trois questions qui déterminent si vous pouvez conclure quoi que ce soit
☐ Réduire une exposition en quinze minutes, avant même de parler de correctif
☐ Dire à une direction générale que vous ne pouvez pas établir l'absence de compromission
☐ Comprimer un processus en urgence sans supprimer les garde-fous qui permettent de se tromper
☐ Décider de reconstruire plutôt que corriger, sur un critère explicite

### Vous savez prouver et financer

☐ Publier un taux avec sa population éligible, son dénominateur et sa part non mesurée
☐ Distinguer une mesure d'un ratio conservateur, et nommer chacun correctement
☐ Constituer un dossier de preuves en continu, en onze pièces
☐ Répondre à six questions d'auditeur sans prétendre être conforme
☐ Construire un dossier d'investissement à trois options, dont le statu quo chiffré

### Vous savez ce que vous ne savez pas

C'est la compétence la plus difficile, et celle que ce cours travaille le plus.

☐ Reconnaître qu'un rapport à 100 % de conformité doit déclencher un examen, pas une satisfaction
☐ Identifier ce que votre journalisation ne vous permettra jamais d'établir
☐ Écrire « non mesuré » dans un tableau de bord plutôt que de laisser une case vide
☐ Nommer un risque non maîtrisé **avant** qu'il ne se réalise, dans une note à la direction

---

**Ce que ce cours ne vous a pas appris**, et qu'il faut aller chercher ailleurs : administrer un système, concevoir un réseau, développer une application, conduire une investigation numérique, plaider un dossier juridique. Le MCS s'appuie sur ces métiers ; il ne les remplace pas, et ce document ne prétend pas les enseigner (§2.10).

**Ce qui vous manquera encore après ce cours**, et que seule la pratique donne : le sens du moment où une négociation peut aboutir, la capacité à sentir qu'un chiffre est faux avant de savoir pourquoi, et la patience nécessaire pour obtenir en dix-huit mois ce qui paraissait évident dès le premier jour. Le fil rouge HELIOMED existe pour rendre cette durée sensible : trois ans, une centaine de décisions, et quatre écarts au dernier audit.

---
