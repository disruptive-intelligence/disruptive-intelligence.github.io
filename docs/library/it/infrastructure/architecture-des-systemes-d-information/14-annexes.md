---
title: ANNEXES
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - index.md
---

### Plan d'accès

| J'ai besoin de… | Annexe |
|---|---|
| Comprendre un terme | **A** — glossaire |
| Retrouver un composant et son rôle | **B** — fiches composants |
| Lire une architecture méthodiquement | **C** — la grille en sept passes |
| Comprendre une convention de dessin | **D** — conventions |
| Retrouver un schéma du cours | **E** — catalogue |
| Voir une architecture type commentée | **F** — dix architectures |
| Vérifier que je ne tombe pas dans un piège | **G** — pièges de lecture |
| Savoir ce qui n'est jamais dessiné | **H** — liste de contrôle |
| Placer un dispositif | **I** — les cinq actions |
| Concevoir et écrire mes compromis | **J** — grille de conception |
| Relier ce cours aux autres volumes | **K** — raccordement |
| Une liste à cocher | **L** — checklists |

---


## Annexe A — Glossaire

**Actif éphémère** — Composant dont la durée de vie est inférieure au cycle d'observation. §41
**Adresse** — Identifiant d'une machine sur le réseau. **Elle change, elle est réattribuée, et derrière une traduction elle n'identifie pas l'origine.** §P.2, §P.4
**Active Directory** — Implémentation de référence d'un service d'annuaire en entreprise. **Ce cours l'utilise pour rendre le concept concret ; ses propriétés ne sont pas celles de tous les services d'identité.** §16
**Double pile** — Coexistence des deux familles d'adressage sur une même machine. **Deux chemins possibles, deux jeux de règles.** §P.5
**Annuaire** — Composant détenant identités, groupes et règles. Répond à *qui es-tu* et *à quoi as-tu droit*. §16
**Arbitrage** — Choix entre deux contraintes contradictoires. **Toute architecture en est faite.** §1.4
**Bordure** — Zone de contact avec l'extérieur : pare-feu, accès distant. §5.2
**Chemin d'administration** — Voie par laquelle on pilote un système. **Plus puissante que ce qu'elle administre.** §27
**Compromis** — Arbitrage assumé et **écrit**. S'il n'est pas écrit, il est subi. §46.5
**Contrainte** — L'une des six forces qui produisent une architecture : disponibilité, performance, coût, sécurité, conformité, **histoire**. §1.4
**Dégradation** — État où le service fonctionne partiellement. À distinguer de l'arrêt et de la cécité. §35.4
**Flux de dépendance** — Ce sans quoi un service **ne peut pas s'établir**. Rarement dessiné. principe des trois flux
**Flux d'exploitation** — Ce qui permet de tenir, observer, restaurer. Sa rupture **rend aveugle sans arrêter**. principe des trois flux
**Flux métier** — Ce que le service transporte ou traite. Le seul généralement dessiné. principe des trois flux
**Frontière** — Ce qu'il faut traverser pour passer d'une zone à une autre. **Une frontière déclarative n'en est pas une.** §5.3
**Kerberos** — Protocole d'authentification employé dans un domaine Active Directory. **À ne pas confondre avec LDAP, qui interroge l'annuaire sans assurer l'authentification.** §16
**Mandataire inverse** — Reçoit de l'extérieur à la place des serveurs internes. **Voit le contenu si le chiffrement y est terminé — modes B et C du §12.**
**Masque de sous-réseau** — Ce qui définit jusqu'où s'étend « à côté ». §P.2
**Passerelle par défaut** — Où une machine envoie ce qui n'est pas dans son sous-réseau. **Sans elle, elle ne sort pas de son segment.** §P.2
**Mandataire sortant** — Concentre les accès internes vers l'extérieur. Fonction opposée du précédent. §11
**Point de rupture** — Ce qui, en tombant, arrête un service. **La notion la plus utile du cours.** §2.2
**Répartiteur de charge** — Distribue entre plusieurs exemplaires. **Crée un point de rupture en en résolvant un.** §13
**Résolution de noms** — Traduit un nom en adresse. **Sa panne est la plus déroutante d'un système d'information.** §14
**Réplication** — Copie continue vers un autre stockage. **Protège de la panne, pas de la suppression : celle-ci est répliquée aussi.** §23.4
**Sauvegarde** — Copie **indépendante**, sur un autre support. **La seule des trois qui protège de tout — si elle a été testée.** §23.4
**Instantané** — État figé à un instant, **sur le même stockage**. Protège d'une erreur récente, pas de la perte du stockage. §23.4
**Stockage bloc / fichier / objet** — Trois façons d'exposer du stockage : un disque · un dossier partagé · une adresse à appeler. §23.4
**RPO** — Objectif de perte de données, exprimé en temps. *Combien de minutes de données accepte-t-on de perdre ?* §46.3
**RTO** — Objectif de délai de reprise. *Sous combien de temps vise-t-on la restauration ?* **À ne pas confondre avec la tolérance métier maximale, qui est une contrainte, ni avec le délai réel, qui se mesure.** §46.3
**Courtier de messages** — Composant qui porte des messages entre un producteur et un consommateur. **Découple leur disponibilité, et devient le point dont tout dépend.** §42.4
**File d'échecs** — Où finissent les messages qu'un consommateur n'arrive jamais à traiter. **Personne ne la regarde.** §42.4
**Idempotence** — Propriété d'une opération qu'on peut rejouer sans changer le résultat. **Indispensable dès qu'un message peut être livré deux fois.** §42.4
**Overlay / underlay** — Réseau logique construit au-dessus d'un réseau physique IP. **Le schéma logique et le schéma physique divergent alors radicalement.** §24.3
**Passerelle d'interconnexion** — **L'ensemble des composants et fonctions** par lesquels deux zones de confiance distinctes sont autorisées à échanger. Ce n'est pas un équipement. §25.5
**Quorum** — Mécanisme par lequel un ensemble distribué décide **quelle partie a le droit de continuer** quand ses membres ne communiquent plus. §23.5
**Split-brain** — Situation où deux parties d'un même système, séparées, continuent chacune de leur côté avec des vérités divergentes. §23.5
**Sens d'établissement** — Qui a initié une connexion. **L'information la plus déterminante d'un flux, et la plus souvent absente des schémas.** §P.3
**Sédimentation** — Empilement de décisions prises à des époques différentes. **L'état normal de tout système en service.** Ch. 4
**Segment** — Ensemble de machines qui se joignent directement, sans traverser d'équipement de routage. **Les y placer ne crée pas entre elles la frontière de filtrage inter-segments visible sur le schéma ; leur isolation éventuelle est à chercher ailleurs.** §24.1
**Service** — Ce qui produit une valeur pour l'organisation. Ne correspond à aucun composant. §35.1
**Strate** — Couche historique d'une architecture, reconnaissable à ses conventions et ses technologies. §4.2
**Terminaison du chiffrement** — Point où un flux chiffré est ouvert. **Détermine qui voit le contenu en clair.** Trois modes, §12
**Traduction d'adresses** — Mécanisme qui remplace une adresse au passage. **L'adresse observée n'est alors pas celle de l'origine.** §P.4
**Vue** — Représentation partielle d'un système : physique, logique, flux, service. **Aucune ne ment.** §3.3
**Zone** — Regroupement de segments partageant un niveau de confiance. Six de référence. §5.2
**Zone démilitarisée** — Ce qui doit être joignable de l'extérieur, **en supposant que ce sera compromis**. Définie par sa **seconde** frontière. §25

---


## Annexe B — Fiches composants

*Format uniforme : rôle · s'il disparaît · effet sur la donnée · reconnaissance · contrainte et coût.*

| Composant | S'il disparaît | Délai | Compréhensible ? |
|---|---|---|---|
| **Commutateur** | Un segment entier | Immédiat | ✅ |
| **Routeur** | Les échanges entre segments | Immédiat | ⚠️ |
| **Pare-feu** | Tout ce qui traverse · **ou rien, s'il est contourné** | Immédiat | ⚠️ |
| **Mandataire sortant** | L'accès Internet des postes | Immédiat | ❌ |
| **Mandataire inverse** | Les accès externes seuls | Immédiat | ❌ |
| **Répartiteur** | **Tout le service**, malgré des serveurs sains | Immédiat | ❌ |
| **Résolution de noms** | Presque tout | **Différé — caches** | ❌ |
| **Attribution d'adresses** | Les machines une par une | **Différé, jours** | ❌ |
| **Annuaire** | Les authentifications, puis tout | Progressif | ⚠️ |
| **Infrastructure de clés** | Un service à chaque expiration | **Différé, mois** | ❌ |
| **Serveur web** | Rien si redondé | Immédiat | ✅ |
| **Applicatif** | Le service · le site s'affiche, rien ne marche | Immédiat | ⚠️ |
| **Base de données** | Tout ce qui en dépend · **perte possiblement définitive** | Immédiat | ⚠️ |
| **Serveur de fichiers** | Le travail, pas toujours le service | Immédiat | ✅ |
| **Messagerie** | Les courriels · **et la réinitialisation des mots de passe** | Immédiat puis différé | ⚠️ |
| **Hôte de virtualisation** | Ses machines | Immédiat | ⚠️ |
| **Stockage partagé** | **Toute la plateforme** | Immédiat | ⚠️ |
| **Stockage objet** | Ce qui l'appelle | Immédiat | ⚠️ — **joignable par clé, pas par le réseau** |
| **Plan de gestion** | Rien · **on ne peut plus rien administrer** | Immédiat | ❌ |

⚠️ **Les six lignes marquées ❌ sont les six composants dont la panne est incompréhensible.** Cinq d'entre eux ne sont jamais dessinés.

---


## Annexe B bis — Index des notions à reconnaître

> **Les vingt-deux technologies que vous rencontrerez sans avoir à les maîtriser.** Chacune est traitée là où elle devient naturelle, jamais en catalogue.

| Notion | Ce qu'il faut en retenir en une ligne | Où |
|---|---|---|
| **BGP** | Les politiques comptent autant que la distance · le chemin dépend de ce que d'autres annoncent | §9.2 |
| **MPLS** | Un réseau privé d'opérateur **n'est pas un chiffrement** | §26.3 |
| **SD-WAN** | Pas un nouveau câble : une couche de pilotage · **le chemin devient dynamique** | §26.3 |
| **VXLAN / EVPN** | Réseau logique au-dessus du physique · **étendre un segment étend la propagation** | §24.3 |
| **WAF** | Le seul des trois qui juge **le contenu** d'une requête web | §12.3 |
| **CDN** | Le chiffrement est terminé chez un tiers · **une page personnalisée en cache est servie à un autre** | §12.3 |
| **Passerelle d'interfaces** | Une façade **avec une politique**, pas un mandataire moderne | §42.3 |
| **Maillage de services** | Tous les environnements de microservices n'en ont pas besoin | §41.4 |
| **HSM** | La clé peut être **utilisée sans être exportée** | §17.3 |
| **PAM** | Transforme un état permanent en **événement daté et motivé** · attention au compte de secours | §27.3 |
| **NAC** | Place le terminal **dans un segment selon ce qu'il est** · que fait-on s'il tombe ? | §24.4 |
| **SASE / SSE / CASB** | Des familles de capacités, **pas des implémentations identiques** | §39.4 |
| **VDI** | *Où s'exécute réellement l'application ?* · une panne réseau **arrête** le travail | §23.3 |
| **Hyperconvergence** | La simplification physique **déplace la complexité dans le logiciel** | §23.3 |
| **Réseau de stockage dédié** | Une infrastructure entière absente de tous les schémas logiques | §23.5 |
| **Immutabilité** | Protège une copie existante · **n'empêche pas de cesser d'en créer** | §23.5 |
| **Quorum** | Un membre sain peut devoir **s'arrêter faute de majorité** · deux nœuds ne suffisent pas | §23.5 |
| **Consensus distribué** | La forte cohérence se paie en disponibilité ou en performance | §42.3 |
| **Mainframe** | **Ancien ne veut dire ni inutile, ni non critique** | §4.2 |
| **Calcul intensif** | Une zone aux priorités inversées, comme l'industriel | §5.4 |

⚠️ **Le contrat, rappelé** : ces vingt-deux notions relèvent du niveau 🔭. **On attend de vous que vous sachiez ce qu'elles impliquent, et quelle question poser — pas que vous sachiez les configurer.**

---


## Annexe C — La grille en sept passes

```
①  ZONES        Combien ? Qu'est-ce qui matérialise chaque frontière ?
                Y a-t-il une seconde frontière après la DMZ ?
                Un composant est-il à cheval ?

②  ENTRÉE       Utilisateur externe : par où ?
                Utilisateur interne : par où ? (souvent plus court)
                Administrateur : par où ? (jamais dessiné)

③  DONNÉES      Où sont-elles ? En combien d'endroits existent-elles ?
                Réplicas · sauvegardes · recette · exports · rapports

④  IDENTITÉ     Contre quoi s'authentifie-t-on ?
                Combien de fois sur un parcours ?
                Que se passe-t-il si ce composant tombe ?

⑤  FLUX         Quel chemin suit une requête, en douze étapes ?
                Quelle famille pour chaque flux ?

⑥  RUPTURES     Quels composants sont uniques ?
                Les exemplaires sont-ils sur des hôtes différents ?
                Le basculement a-t-il été testé ?
                Où sont les sessions ?

⑦  INVISIBLE    Les onze éléments de l'annexe H
```


**Rendu attendu** : une page, se terminant par **trois questions, pas un jugement**.
**Durée réelle** : 1 h pour une architecture simple, une demi-journée pour un système réel.

---


## Annexe D — Conventions de schéma

| Convention | Signification habituelle | Fiabilité |
|---|---|---|
| Position haute | Extérieur, Internet | Élevée |
| Position basse | Données | Élevée |
| Nuage | Ce qu'on ne maîtrise ou ne détaille pas | Élevée |
| Boîtes empilées | Plusieurs exemplaires | Moyenne |
| Trait pointillé | Flux logique, relation, lien non permanent | **Faible** |
| Double ligne | Redondance ou haut débit | **Faible** |
| Composant à cheval | Traverse une frontière — **toujours à interroger** | Élevée |

⚠️ **Aucune convention n'est normalisée.** Première question devant un schéma inconnu : *y a-t-il une légende ?*

**Ce qu'une boîte peut représenter** : machine · rôle · groupe · service · fournisseur externe. §3.1
**Ce qu'un trait peut représenter** : câble · flux · relation logique · adjacence · **rien de précis**. §3.2

---


## Annexe E — Catalogue des schémas

| # | Schéma | Chapitre |
|---|---|---|
| 1.1 | HELIOMED, vue d'ensemble | §1.1 |
| 1.2 | Les quatre questions du lecteur | §1.3 |
| 1.3 | Trois arbitrages, trois architectures | §1.4 |
| 3.1 | Le même système, quatre vues | §3.3 |
| 4.1 | Les strates d'un système d'information | §4.2 |
| 5.1 | Les six zones | §5.2 |
| 6.1 | Ce qu'un poste atteint | §6.2 |
| 6.2 | Les deux chemins d'un poste nomade | §6.3 |
| 10.1 | Ce que le suivi d'état change | §10.2 |
| P.1 | La décision que prend toute machine | §P.2 |
| P.2 | Les deux traductions d'adresses | §P.4 |
| 12.1 | Ce que le mandataire inverse change | §12 |
| 12.2 | Les trois modes de terminaison du chiffrement | §12 |
| 14.1 | La place réelle de la résolution de noms | §14 |
| 20.1 | Pourquoi la base est au fond | §20 |
| 23.1 | La redondance qui n'en est pas | §23.3 |
| 23.2 | Bloc, fichier, objet · quatre architectures de stockage | §23.4 |
| 25.1 | Les deux frontières d'une DMZ | §25.1 |
| 27.1 | Le chemin d'administration | §27.2 |
| 28.1 | Les trois modèles de frontière industrielle | §28.3 |
| 29.1 | Une requête, de bout en bout | §29.1 |
| 29.2 | Quatre chemins vers le même service | §29.3 |
| 30.1 | La cascade d'une panne d'annuaire | §30.2 |
| 31.1 | Où vit la session | §31.2 |
| 32.1 | Une donnée, de la saisie à l'oubli | §32.1 |
| 35.1 | L'arbre de dépendance d'un service | §35.2 |
| 35.2 | Dix flux superposés sur un même service | §35.3 |
| 36.1 | Les sept passes | §36.1 |
| 38.1 | Les trois façons de dessiner un tiers | §38.2 |
| 39.1 | Où passe la frontière de responsabilité | §39.2 |
| 40.1 | Les trois liens d'une architecture hybride | §40.2 |
| 41.1 | Deux façons de dessiner un cluster | §41.2 |
| 43.1 | Les cinq actions | §43.1 |
| 46.1 | Lire et concevoir | §46.1 |

---


## Annexe F — Les dix architectures

| # | Architecture | Ce qu'elle enseigne | Où |
|---|---|---|---|
| 1 | Application interne, trois composants | Une architecture proportionnée · l'authentification non représentée | §37.1 |
| 2 | Site web public | Qui voit le contenu en clair · la frontière 2 | §37.2 |
| 3 | Trois niveaux, redondance partielle | **La rupture de symétrie est une information** | §37.3 |
| 4 | Système hérité mal documenté | Trois signes convergents d'une strate ancienne | §37.4 |
| 5 | Haute disponibilité complète | Le coût de la symétrie · ce qu'elle ne couvre pas | Cas B |
| 6 | Multi-sites | L'autonomie locale et ses trois dépendances | §26.2 |
| 7 | Hybride | Le lien d'identités, point de fragilité récurrent | §40 |
| 8 | Industrielle | L'inversion des priorités | §28 |
| 9 | **Réelle et désordonnée** | Vingt ans de sédimentation | Cas A |
| 10 | HELIOMED complet | La synthèse du fil rouge | §1.1 + ajouts §50.6 |

---


## Annexe G — Pièges de lecture

| # | Piège | Détection |
|---|---|---|
| 1 | Lire un **rôle** comme une machine | *Combien y en a-t-il réellement ?* |
| 2 | Croire qu'un **trait** signifie une autorisation | *Est-ce permis, ou seulement possible ?* |
| 3 | Confondre **mandataire sortant et inverse** | *Pour entrer, ou pour sortir ?* |
| 4 | Prendre une **frontière déclarative** pour une frontière | *Qu'est-ce qui empêche de passer ?* |
| 5 | Oublier la **seconde frontière** d'une DMZ | Elle n'est presque jamais dessinée |
| 6 | Croire une **redondance** dessinée | *Sur des hôtes différents ? Le basculement est-il testé ?* |
| 7 | Oublier que la **session** peut annuler la redondance | *Où vit la session ?* |
| 8 | Ne pas voir les composants **reliés à rien** | Annuaire, résolution : tout s'y connecte |
| 9 | Chercher une panne parmi les **composants dessinés** | Sept étapes sur douze sont invisibles |
| 10 | Juger une anomalie sans demander sa **date** | Chaque anomalie a une histoire |
| 11 | Déduire une architecture de la **taille** | *Principe de la contrainte* |
| 12 | Oublier le **poste utilisateur** | La majorité des flux et des incidents |
| 13 | Oublier le **prestataire** | Dessiné en nuage, présent au cœur de l'administration |
| 14 | Croire qu'un **service en ligne** se sécurise comme le reste | Les cinq actions ne s'appliquent pas à son infrastructure — elles se déplacent — §42.5 |
| 15 | Lire un **cluster** par ses instances | Quatre éléments : entrée, services, état, plan de contrôle |
| 16 | Placer un dispositif au **périmètre** en croyant tout couvrir | Il ne voit pas l'interne |
| 17 | Proposer **dix améliorations** | Une seule sera peut-être faite |
| 18 | Croire un schéma **à jour** | Datez-le |
| 19 | Prendre une **identification** pour une certitude | *Principe d'hypothèse* — port et position font un faisceau, pas une preuve |
| 20 | Conclure à une **redondance** parce qu'elle est dessinée | *Principe de preuve* — hôte, stockage, site, alimentation partagés ? |
| 21 | Croire qu'un mandataire inverse **voit toujours le contenu** | Trois modes de terminaison — §12 |
| 22 | Confondre **LDAP et authentification** | LDAP interroge · d'autres mécanismes authentifient — §16 |
| 23 | Croire qu'un **certificat chiffre** | Il lie une identité à une clé ; le protocole chiffre — §17 |
| 24 | Prendre une **adresse dans un journal** pour l'origine | Traduction d'adresses, mandataires — §P.4, §34.1 |
| 25 | Supposer que le modèle **IPv4 + traduction** est universel | §P.5 |
| 26 | Croire que **la base est la donnée** | Elle en porte une partie — §20, §32.2 |
| 27 | Croire qu'un **jeton autoporté ne peut pas être révoqué** | C'est un compromis de coût et de délai — §31.2 |
| 28 | Confondre **réplication et sauvegarde** | La réplication copie aussi les suppressions — §23.4 |
| 29 | Confondre **instantané et sauvegarde** | L'instantané vit sur le même stockage — §23.4 |
| 30 | Oublier le **stockage objet** parce qu'il n'a pas de lien réseau | Il est joignable par clé, depuis n'importe où — §23.4 |
| 31 | Croire que sur un service en ligne **on ne peut rien faire** | Les actions se déplacent vers la configuration et les identités — §42.6 |
| 32 | Croire que deux **réseaux sans fil annoncés** sont deux segments | Annoncé ≠ segmenté — §24.4 |
| 33 | Oublier que le **sans-fil contourne le périmètre physique** | Mode A : la clé donne l'accès interne — §24.4 |
| 34 | Croire qu'une **file asynchrone** protège de tout | Elle déplace la panne : accumulation silencieuse — §42.4 |
| 35 | Ne pas rendre un **consommateur idempotent** | Au moins une livraison ≠ exactement une — §42.4 |
| 36 | Confondre **tolérance métier, RTO visé et délai réel** | Trois choses différentes — §46.3 |
| 37 | Transposer un **ratio d'exploitation** d'un corrigé | Ce sont des données de scénario — §48.0 |

---


## Annexe H — Ce qui n'est jamais dessiné

**Liste de contrôle. À passer sur tout schéma, systématiquement.**

☐ **Résolution de noms** — sa panne arrête presque tout, de façon différée
☐ **Annuaire** — dessiné parfois, relié jamais
☐ **Synchronisation d'horloge** — sa dérive produit des rejets d'authentification
☐ **Chemins d'administration** — le chemin le plus court vers la compromission totale
☐ **Postes de travail** — la majorité des flux et des incidents
☐ **Postes de prestataires** — hors inventaire, avec des droits d'administration
☐ **Sauvegardes et leur chemin** — le serveur est parfois dessiné, jamais son chemin
☐ **Services en ligne** — pas chez vous, donc absents
☐ **Liens partenaires** — anciens, oubliés
☐ **Certificats et leur autorité** — invisibles tant qu'ils fonctionnent
☐ **Environnements de recette** — données de production, protections moindres
☐ **Collecte de journaux** — flux d'exploitation
☐ **Versions** — impossible de raisonner l'obsolescence sans elles
☐ **Le temps** — un schéma est un instantané, sans histoire ni migration en cours

⚠️ **Dessinez-les tous sur votre schéma : la page devient illisible en quatre minutes.** C'est pourquoi ils n'y sont pas — et pourquoi il faut savoir qu'ils existent.

---


## Annexe I — Les cinq actions et leurs emplacements

| Action | Possible | **Impossible** |
|---|---|---|
| **Observer** | Pare-feu · mandataires · commutateurs · postes · serveurs | Flux chiffré non terminé · **chez un tiers** |
| **Filtrer** | Pare-feu · mandataires · entre segments | **Dans un segment** · chez un tiers |
| **Authentifier** | Mandataire inverse · applicatif · annuaire · accès distant | Entre serveurs se faisant confiance par adresse |
| **Segmenter** | Entre zones · entre segments · au poste | **Dans un segment**, sans mesure explicite |
| **Journaliser** | Tout composant traversé | Ce qui ne traverse aucun composant journalisant |

**Les deux points les plus riches** :

| Point | Ce qu'il apporte | Sa limite |
|---|---|---|
| **Mandataire inverse** | Voit tout le trafic externe **en clair** · filtre · authentifie · journalise | **Ne voit que l'externe** |
| **Applicatif** | Le seul qui connaisse **l'utilisateur réel et l'action métier** | Reçoit rarement les moyens |

**Face à un emplacement impossible** : on **déplace**, on **remplace**, ou on **déclare non couvert**. Jamais on ne fait semblant.

⚠️ **Sur un service en ligne** : les cinq actions ne s'appliquent pas à son infrastructure, **et elles se déplacent** vers la configuration, les identités, les données et les journaux exposés — §42.5. **« Impossible » y signifie « pas sur ses couches internes », pas « rien à faire ».**

---


## Annexe J — Grille de conception et registre des compromis


### J.1 Fiche de contraintes

```
SERVICE         .................................
UTILISATEURS    Combien : ......  Où : ......  Quand : ......
DONNÉES         Nature : ......  Sensibilité : ......
DISPONIBILITÉ   Interruption tolérable : ......
                Perte de données tolérable : ......
PERFORMANCE     Temps de réponse : ......  Volume : ......
COÛT            Investissement : ......  Récurrent : ......
                EXPLOITANTS DISPONIBLES : ......   ← la ligne décisive
SÉCURITÉ        Exposition nécessaire : ......
CONFORMITÉ      Obligations : ......  Preuve à produire : ......
HISTOIRE        Existant à intégrer : ......
                Ce qu'on ne peut pas changer : ......
```


⚠️ **La ligne « exploitants disponibles » est celle qui explique le plus d'échecs.** §47.3


### J.2 Registre des compromis

| # | Compromis | Contrainte privilégiée | Contrainte dégradée | Conséquence acceptée | Décideur | **Revoir si** |
|---|---|---|---|---|---|---|

**C'est le vrai livrable d'une conception.** Le schéma montre le résultat ; le registre montre **pourquoi**.


### J.3 Ce qui reste à vérifier

| # | À vérifier | Pourquoi | Qui | Avant quand |
|---|---|---|---|---|

**Une proposition sans cette section est un engagement déguisé.**


### J.4 Grille de critique en six points

```
① POINT FORT          Ce qui est bien pensé, et pourquoi     ← toujours en premier
② POINT FAIBLE        Ce qui est fragile, sous quelle condition
③ POINT DE RUPTURE    Ce qui n'a pas de doublure
④ DÉPENDANCE CACHÉE   Ce dont tout dépend et qui n'est pas dessiné
⑤ RISQUE PRINCIPAL    Scénario le plus probable et le plus coûteux
⑥ AMÉLIORATION        UNE SEULE, avec son coût et son effet
```


**Format en cinq lignes** : ce qui fonctionne · ce que j'ai observé · **ce que je n'ai pas su** · le risque · ce que je propose.

---


## Annexe K — Raccordement aux autres volumes

| Ce que l'architecture détermine | Volume concerné | Chapitre |
|---|---|---|
| **L'interruptibilité** — un composant qui ne peut s'arrêter ne sera pas corrigé | Maintien en condition de sécurité | §45.1 |
| **Les fenêtres de maintenance** | MCS | §45.1 |
| **Ce qui est découvrable** — un actif derrière un filtre est invisible au scanner | Asset Management | §45.2 |
| **Les actifs éphémères** | Asset Management | §41 |
| **Les points de passage** — les seuls endroits où observer | Détection et journalisation | §45.3 |
| **La perte d'identité en chemin** | Détection | §34.1 |
| **La rétention des journaux** | Détection · Réponse à incident | §34.2 |
| **Ce qu'on peut isoler** | Réponse à incident | §45.4 |
| **Si l'on peut encore administrer un système compromis** | Réponse à incident | §45.4 |
| **Les chemins d'administration** | Identités et accès | §27 |
| **La fédération et ses dépendances** | Identités et accès | §30.3 |
| **L'exposition d'un composant** | Industrialiser la remédiation | §45.1 |

**Les huit volumes et leurs limites fondamentales** :

| Volume | Limite |
|---|---|
| **Architecture des SI** | **Toute architecture est un compromis sédimenté** |
| Asset Management | La représentation n'est jamais le système |
| Cyber Threat Intelligence | L'incertitude ne se supprime pas |
| Maintien en condition de sécurité | Le système change avec le temps |
| Détection et journalisation | On ne voit que là où l'on regarde |
| Industrialiser la remédiation | La capacité est finie, le flux ne l'est pas |
| Réponse à incident | On décide sans savoir |
| Identités et accès | Les droits s'accumulent, ils ne se réduisent jamais seuls |

---


## Annexe L — Checklists


### L.1 — Devant un schéma inconnu
☐ Y a-t-il une légende ? · ☐ De quand date-t-il ? · ☐ **Pour qui a-t-il été fait ?** · ☐ Quelle vue est-ce ? · ☐ Que représente une boîte ici ? · ☐ Que représente un trait ?


### L.5 — Avant de conclure à un point de rupture
☐ Est-ce un rôle ou une machine ? · ☐ Combien d'exemplaires réels ? · ☐ Sur des hôtes différents ? · ☐ **Même stockage, même site, même alimentation ?** · ☐ **Le basculement a-t-il été testé, et quand ?** · ☐ Où vivent les sessions ?


### L.2 — Avant de croire à une sauvegarde
☐ Est-ce une réplication, un instantané ou une sauvegarde ? · ☐ **Sur quel stockage vit-elle ?** · ☐ Un compte d'exploitation compromis peut-il la supprimer ? · ☐ **Quand a-t-elle été restaurée pour de vrai ?**


### L.3 — Avant de croire à une séparation sans fil
☐ Combien de réseaux annoncés ? · ☐ **Chacun aboutit-il dans un segment distinct ?** · ☐ Qu'est-ce qui filtre entre eux ? · ☐ Le réseau entreprise aboutit-il dans le segment interne ? · ☐ **Contre quoi authentifie-t-on, et que se passe-t-il si ce service tombe ?**


### L.4 — Avant de croire à un découplage asynchrone
☐ Que se passe-t-il si le consommateur est arrêté ? · ☐ **Qui supervise la taille de la file et l'âge du plus ancien message ?** · ☐ Le consommateur est-il idempotent ? · ☐ **Qui regarde la file d'échecs ?** · ☐ Les messages en attente sont-ils persistés ?


### L.6 — Avant d'affirmer le rôle d'un composant
☐ Sur quel faisceau — port, position, connexions ? · ☐ **Le port peut-il être non standard ?** · ☐ Le composant cumule-t-il deux rôles ? · ☐ **Qu'est-ce qui confirmerait ?** · ☐ Ai-je écrit « probablement » plutôt qu'une affirmation ?


### L.7 — Avant de critiquer
☐ Ai-je demandé la date ? · ☐ Ai-je demandé le motif ? · ☐ Ai-je commencé par un point fort ? · ☐ **Ai-je une seule recommandation ?** · ☐ Ai-je chiffré son coût ?


### L.8 — Avant de concevoir
☐ Le service est-il formulé côté métier ? · ☐ L'interruption tolérable est-elle **chiffrée** ? · ☐ La perte de données tolérable est-elle chiffrée ? · ☐ **Combien d'exploitants disponibles ?** · ☐ Qu'accepte-t-on de perdre ? · ☐ Ai-je envisagé de renoncer à une fonctionnalité ?


### L.9 — Avant de livrer une conception
☐ Registre des compromis écrit ? · ☐ Conditions de réexamen ? · ☐ Ce qui reste à vérifier ? · ☐ L'architecture est-elle exploitable par l'organisation telle qu'elle est ?


### L.10 — Avant de placer un dispositif
☐ Que voit-il depuis cet emplacement ? · ☐ **Que ne voit-il pas ?** · ☐ Quelle proportion des flux y passe ? · ☐ Est-ce le point le plus riche disponible ? · ☐ Que déclare-t-on non couvert ?

---
