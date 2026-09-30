---
title: Annexe B — Cheat sheets par plateforme
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - ANNEXES
  - index.md
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
