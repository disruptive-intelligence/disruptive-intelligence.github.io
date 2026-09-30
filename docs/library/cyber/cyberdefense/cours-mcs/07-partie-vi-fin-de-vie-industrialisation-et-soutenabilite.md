---
title: PARTIE VI — Fin de vie, industrialisation et soutenabilité
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
chapter: 7
chapters: 10
---

Cette partie traite ce qui fait tenir un programme de MCS dans la durée : retirer proprement ce qui ne sert plus, automatiser ce qui peut l'être, financer et rendre le travail soutenable, mesurer, et prouver.

---

## Chapitre 35 — Décommissionnement sécurisé

### 35.1 Le cycle de vie ne s'achève pas à « migration effectuée »

Un système remplacé mais non retiré cumule tous les défauts : il n'est plus maintenu puisqu'il n'est plus utilisé, il reste joignable puisque personne ne l'a débranché, et il conserve ses comptes, ses secrets et ses accès. C'est l'actif idéal pour un attaquant : privilégié, oublié, et surveillé par personne.

**Les cinq résidus typiques d'un décommissionnement incomplet** :

| Résidu | Conséquence |
|---|---|
| Enregistrement de nom toujours actif | Le service semble exister ; une réattribution d'adresse peut créer une confusion exploitable |
| Compte de service toujours valide | Accès conservé sur d'autres systèmes |
| Règle de filtrage toujours ouverte | Un chemin réseau subsiste vers ce qui remplace l'ancien système |
| Sauvegardes restaurables | Les données existent encore, sans propriétaire |
| Machine éteinte mais non supprimée | Rallumée un jour « pour vérifier quelque chose », dans un état d'il y a trois ans |

**Le décommissionnement est donc un acte de MCS à part entière**, au même titre que l'application d'un correctif — et il figure explicitement dans la définition du §1.1.

### 35.2 La décision de retrait

| Élément | Contenu |
|---|---|
| Déclencheur | Migration terminée, usage nul, fin de support, fin de contrat |
| **Mesure de l'usage réel** | Avant tout, comme au §32.7 : qui l'utilise, à quelle fréquence ? |
| Décideur | Propriétaire métier (§9.2) |
| Communication | Préavis proportionné, diffusé largement |
| Période d'observation | Extinction avant suppression, pour révéler les usages non déclarés |

✅ **BONNE PRATIQUE (P0) — l'extinction avant la suppression**
Éteignez avant de supprimer, et observez. Une à quatre semaines selon la criticité. C'est la méthode la plus fiable pour découvrir les dépendances non documentées — celles que §10.5 ne trouve pas, notamment les traitements mensuels ou annuels. Le préavis, lui, réveille les utilisateurs : dans le fil rouge du §5.5, il avait suffi à faire réapparaître onze propriétaires sur vingt-neuf.

### 35.3 Identifier les dépendances

| Type | Comment le trouver |
|---|---|
| Flux entrants | Analyse des connexions sur une période représentative (§10.5) |
| Flux sortants | Idem — souvent oubliés |
| Tâches planifiées ailleurs | Recherche du nom d'hôte dans les configurations et les scripts |
| Intégrations applicatives | Recherche dans les fichiers de configuration des applications |
| Comptes utilisés ailleurs | Le compte de service de cette machine sert-il sur d'autres systèmes ? |
| Certificats | Émis pour ce service, utilisés par un autre ? |
| Documentation et procédures | Références au système dans les procédures d'exploitation |

⚠️ **PIÈGE — la dépendance annuelle**
Une analyse de flux sur trois semaines manque le traitement de clôture annuelle. C'est la raison pour laquelle la période d'observation en extinction doit couvrir, pour un système ancien, au moins un cycle métier — ou être assortie d'une recherche documentaire explicite.

### 35.4 Traitement des données

| Étape | Exigence |
|---|---|
| Inventaire des données | Quelles données, quelle sensibilité, quelle durée de conservation légale ou contractuelle |
| Migration ou archivage | Vers où, sous quel format, avec quelle vérification d'intégrité |
| **Vérification de lisibilité** | Un archivage illisible dans cinq ans n'est pas un archivage |
| Effacement | Méthode adaptée au support et à la sensibilité |
| **Preuve d'effacement** | Attestation, journal, certificat de destruction |

**Le point souvent manqué** : l'effacement doit couvrir **toutes** les copies — instantanés, environnements de recette alimentés par une copie (§28.1), exports temporaires, et sauvegardes selon leur politique de rétention.

### 35.5 Retrait des points d'entrée

| Objet | Action |
|---|---|
| Enregistrements de résolution de noms | Suppression, y compris les alias et les entrées internes |
| Publications externes | Retrait de la publication, vérification depuis l'extérieur (ch. 11) |
| Règles de filtrage | Suppression, pas seulement désactivation |
| Entrées de répartiteur de charge | Retrait de la grappe |
| Certificats | Révocation, retrait des magasins où ils étaient déclarés |
| Références dans d'autres configurations | Recherche systématique du nom et de l'adresse |

### 35.6 Révocations

C'est la section la plus oubliée, et celle qui produit les résidus les plus dangereux.

| Objet | Action |
|---|---|
| Comptes utilisateurs locaux | Suppression |
| **Comptes de service** | Suppression, après vérification qu'ils ne servent nulle part ailleurs (§24.11) |
| Clés d'accès distant | Retrait des clés autorisées, sur ce système **et** sur ceux qu'il administrait |
| Clés d'API et jetons | Révocation côté fournisseur, pas seulement suppression locale |
| Secrets dans les coffres-forts | Suppression, avec vérification des consommateurs |
| **Autorisations déléguées** | Révocation côté service concerné (§31.6) |
| Certificats clients | Révocation |
| Appartenances à des groupes | Retrait |

⚠️ **La révocation côté fournisseur** est le point critique : supprimer une clé d'un fichier de configuration ne l'invalide pas. Tant qu'elle n'est pas révoquée à la source, elle reste utilisable par quiconque en détient une copie.

### 35.7 Retrait de l'outillage

| Outil | Action | Effet si oublié |
|---|---|---|
| Supervision | Retrait des sondes | Alertes permanentes que l'on finit par ignorer |
| Scanner de vulnérabilités | Retrait du périmètre | Constats sur un actif inexistant (§15.11, faux positif n° 10) |
| Protection des postes | Désinstallation de l'agent, retrait de la console | Licence consommée, machine fantôme dans les indicateurs |
| Sauvegarde | Arrêt des travaux, décision sur les sauvegardes existantes | Sauvegardes orphelines, coût de stockage |
| Gestion de configuration | Retrait du périmètre de convergence | Erreurs récurrentes |
| Outil de déploiement | Retrait | Actif compté dans le dénominateur, jamais joignable |
| **Inventaire** | Passage au statut « décommissionné », **sans suppression de l'historique** | Perte de la trace |

### 35.8 Sauvegardes existantes

Question à trancher explicitement : que fait-on des sauvegardes d'un système retiré ?

| Option | Quand |
|---|---|
| Conservation jusqu'à expiration de la rétention normale | Cas général |
| Conservation prolongée pour raison légale | Obligation de conservation identifiée |
| Suppression anticipée | Données sensibles sans obligation de conservation |

**Dans tous les cas** : la décision est documentée, une date de suppression effective est fixée, et un propriétaire en répond. Une sauvegarde restaurable d'un système décommissionné il y a quatre ans est un risque sans bénéfice.

### 35.9 Matériel et licences

Récupération des licences réaffectables, effacement des supports de stockage avec preuve, destruction ou restitution du matériel avec traçabilité, retrait du parc et de l'assurance. Pour le matériel loué ou repris par un tiers, l'effacement doit être vérifié **avant** la restitution, pas supposé.

### 35.10 Clôture contractuelle

Résiliation des contrats de support associés, arrêt des abonnements liés, retrait des accès du fournisseur (§13.5), récupération des données détenues par le fournisseur, et confirmation écrite de la suppression de son côté.

### 35.11 Vérification finale

**La règle** : un décommissionnement se **vérifie**, il ne se déclare pas.

| Contrôle | Méthode |
|---|---|
| Absence de réponse réseau | Test depuis plusieurs points du réseau |
| Absence dans les sources d'inventaire | Rejeu de la réconciliation (§10.3) |
| Absence d'exposition externe | Nouvelle passe de découverte externe (ch. 11) |
| Absence de comptes actifs | Recherche par nom dans l'annuaire |
| Absence de références résiduelles | Recherche du nom d'hôte dans les configurations |
| **Délai d'observation** | 30 à 90 jours, pour détecter les usages résiduels |

### 35.12 ✅ Livrable — Procès-verbal de décommissionnement

| Section | Contenu |
|---|---|
| Identification | Actif, propriétaires, date de mise en service |
| Décision | Motif, décideur, date, préavis diffusé |
| Dépendances | Identifiées, traitées, avec preuve |
| Données | Migrées, archivées, effacées — avec attestation |
| Points d'entrée | Retirés, avec vérification |
| Révocations | Liste des comptes, clés, secrets, autorisations révoqués |
| Outillage | Retraits effectués |
| Sauvegardes | Décision, date de suppression prévue |
| Matériel et licences | Traitement, preuve de destruction ou de restitution |
| Contrats | Résiliations |
| **Vérification finale** | Contrôles réalisés, date, résultat |
| Signature | Propriétaire métier et propriétaire technique |

### 35.13 🔬 Mini-lab 8 — Décommissionner un serveur

**Objectif** — Repérer les oublis d'un décommissionnement déclaré terminé, et produire le PV manquant.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** §35.5 à §35.11, §24.5 · **Livrable** formulaire D.14 rempli + actions correctives.
**Compétences validées** — ✔ identifier les résidus d'un décommissionnement ✔ révoquer du bon côté ✔ décider d'une révocation de certificat selon le contexte ✔ mesurer le risque transféré par une réattribution d'adresse

**Dossier fourni**

*Pièce 1 — compte rendu de l'équipe*
> « Le serveur `SRV-APP-07` a été éteint le 12 mars. L'application a été migrée vers `SRV-APP-12` le 5 mars, les utilisateurs ont été informés, et les données ont été reprises. La machine virtuelle a été supprimée de l'hyperviseur le 20 mars. Le ticket est clos. »

*Pièce 2 — extrait de l'inventaire, `SRV-APP-07`*
```
mis_en_service      : 2016-09-14
statut_cycle_vie    : décommissionné
environnement       : production
certificats         : 2 (expiration 2029-04-30, 2028-11-12)
comptes_service     : svc-app07-batch, svc-app07-sql
cles_ssh_autorisees : 3 (dont 1 utilisée pour administrer SRV-BDD-01 et SRV-BDD-02)
sauvegardes         : politique 7 ans, dernière le 2027-03-11
```

*Pièce 3 — extrait DNS, 10 avril*
```
srv-app-07.interne.exemple      A      10.42.7.18
app-crm.interne.exemple         CNAME  srv-app-07.interne.exemple
crm-legacy.interne.exemple      CNAME  srv-app-07.interne.exemple
```

*Pièce 4 — règles de filtrage, extrait*
```
ALLOW  10.42.7.18 -> 10.42.9.0/24  tcp/1433   "SRV-APP-07 vers bases"
ALLOW  10.20.0.0/16 -> 10.42.7.18  tcp/443    "accès utilisateurs CRM"
```

*Pièce 5 — supervision*
```
srv-app-07 : 412 alertes "hôte injoignable" depuis le 12 mars — notification désactivée le 3 avril
```

**Questions**
(a) Identifiez les oublis et l'action manquante pour chacun.
(b) Lequel présente le risque le plus élevé, et pourquoi ?
(c) L'adresse `10.42.7.18` a été réattribuée le 2 avril à un poste de test. Quelles conséquences ?
(d) Faut-il révoquer les deux certificats ?
(e) Que manque-t-il au compte rendu, indépendamment de toute action technique ?

---

**Corrigé commenté**

**(a) Les neuf oublis**

| # | Oubli | Preuve dans le dossier | Action manquante |
|---|---|---|---|
| 1 | **Enregistrements de noms** | Pièce 3 : 1 entrée A + 2 alias actifs le 10 avril | Suppression des trois entrées |
| 2 | **Comptes de service** | Pièce 2 : 2 comptes | Vérifier leur usage ailleurs (§24.11), puis supprimer |
| 3 | **Clés SSH** | Pièce 2 : 1 clé administre `SRV-BDD-01` et `-02` | Retirer la clé **sur les deux bases** — l'accès subsiste dans l'autre sens |
| 4 | **Règles de filtrage** | Pièce 4 : 2 règles actives | Suppression, pas désactivation |
| 5 | **Certificats** | Pièce 2 : 2, dont un jusqu'en 2029 | Voir (d) |
| 6 | **Retrait des outils** | Pièce 5 : notification désactivée, sonde conservée | Retrait de la supervision, du scanner, de la sauvegarde, de la protection des postes |
| 7 | **Sauvegardes** | Pièce 2 : rétention 7 ans, aucune décision | Décision documentée, date de suppression, propriétaire |
| 8 | **Effacement et preuve** | Absent | Attestation d'effacement, **y compris instantanés et copies en recette** |
| 9 | **Vérification finale** | Absente | Contrôles du §35.11 après délai d'observation |

**(b) Le risque le plus élevé : la clé SSH (oubli n° 3)**

Les autres oublis laissent des traces exploitables ; celui-ci laisse un **accès actif vers deux serveurs de bases de données toujours en service**. La suppression de `SRV-APP-07` n'y change rien : la clé est déclarée du côté des bases, pas du côté du serveur retiré. C'est le mécanisme du §35.6 — la révocation se fait **là où l'accès est reconnu**, pas là où il était utilisé.

Le compte de service `svc-app07-sql` présente le même défaut, avec la même cause.

**(c) La réattribution d'adresse — deux conséquences**

1. **Confusion d'inventaire.** Le poste de test hérite d'une adresse portant trois entrées DNS pointant vers un serveur applicatif de production. Tout outil raisonnant sur l'adresse ou le nom l'identifiera comme `SRV-APP-07` (§15.11, faux positif n° 8).
2. **Exposition réelle.** La règle `ALLOW 10.20.0.0/16 -> 10.42.7.18 tcp/443` autorise désormais **l'ensemble du réseau bureautique** à joindre un poste de test sur le port 443. Ce n'était pas l'intention, et personne ne l'a décidé.

C'est l'illustration la plus concrète de ce que produit un décommissionnement incomplet : le risque n'est pas resté sur l'actif retiré, il a été **transféré** à un autre actif.

**(d) Les certificats — la réponse n'est pas automatique**

| Cas | Décision |
|---|---|
| Clé privée détruite avec la machine, aucune copie | Révocation **non nécessaire** : documenter la destruction de la clé et le retrait du service |
| Clé privée présente dans une sauvegarde, un instantané ou un coffre | **Révocation nécessaire** |
| Clé privée exportée à un moment quelconque, sans certitude | **Révocation** — le doute impose la prudence |
| Certificat déclaré dans un magasin de confiance tiers | Retrait de la déclaration, en plus de la révocation |

Ici, la pièce 2 indique une sauvegarde du 11/03/2027 avec rétention 7 ans : la clé privée est **probablement restaurable**. Décision retenue : révocation des deux certificats, et rattachement de la question au traitement des sauvegardes (oubli n° 7).

**(e) Ce qui manque au compte rendu, et qui n'est pas technique**

Aucun propriétaire nommé, aucune signature, aucune vérification. **Personne ne répond de ce décommissionnement.** Dans dix-huit mois, quand la clé SSH sera découverte lors d'un audit, aucun nom ne sera associé à la décision — et c'est exactement ce qui s'est produit dans le fil rouge du §35.14.

Le PV D.14 corrige cela par construction : quinze lignes de contrôle, une preuve par ligne, et **deux signatures**.

**Les deux erreurs attendues**
1. Considérer que la suppression de la machine virtuelle achève le processus. Elle supprime le système, pas ce qui gravite autour — et c'est ce qui gravite autour qui constitue le risque résiduel.
2. Traiter la révocation des certificats comme un réflexe automatique, sans se demander où se trouve la clé privée.

### 35.14 🔴 FIL ROUGE — août 2028 : les résidus de décembre 2026

Claire Nadeau fait vérifier les neuf serveurs décommissionnés en décembre 2026 (§1.9 et suivants), vingt mois plus tard, dans le cadre de la préparation du dossier de preuves.

**Le résultat.**

| Contrôle | Résultat |
|---|---|
| Machines supprimées de l'hyperviseur | 9 sur 9 |
| Enregistrements de noms supprimés | **6 sur 9** — 3 entrées subsistent |
| Comptes de service supprimés | **8 sur 9** — 1 compte actif, avec droits de lecture sur le serveur de fichiers |
| Règles de filtrage supprimées | 7 sur 9 |
| Certificats révoqués | **4 sur 9** — 5 certificats valides, dont 2 expirant en 2029 |
| Sauvegardes traitées | **0 sur 9** — aucune décision prise, sauvegardes conservées par défaut |
| Preuve d'effacement | Aucune |
| Procès-verbal signé | Aucun |

**Le compte de service survivant** est celui qui préoccupe le plus. Créé en 2017, il dispose de droits de lecture sur le serveur de fichiers, son mot de passe n'a jamais été modifié, et il n'apparaît dans aucun inventaire d'application — puisque l'application n'existe plus. Il figurait pourtant parmi les 94 comptes sans propriétaire identifiés en septembre 2027 (§24.11), et il avait alors été classé « à investiguer ».

**Ce que l'épisode démontre**, et c'est pourquoi il clôt cette partie : le décommissionnement de décembre 2026 avait été considéré comme fait. Il l'était à 70 %. Les 30 % restants ont produit, vingt mois plus tard, un compte privilégié orphelin, cinq certificats valides sans porteur, trois entrées de résolution de noms, et un volume de sauvegardes conservé sans décision.

**Les trois mesures.**

1. Le **procès-verbal de décommissionnement** (§35.12) devient obligatoire, avec double signature. Un décommissionnement sans procès-verbal n'est pas clos.
2. Une **vérification à J+90** est ajoutée systématiquement, avec les contrôles du §35.11.
3. Les neuf décommissionnements de 2026 et les quatre de 2027 sont **repris intégralement** — six jours de travail.

**Ce que Claire écrit au comité.** *Nous avons construit un dispositif capable de détecter une vulnérabilité sur un serveur en vingt-quatre heures. Il nous a fallu vingt mois pour découvrir qu'un compte privilégié survivait à un serveur que nous avions nous-mêmes éteint.*

→ La suite en 🔴 §36.8, sur ce qui peut réellement être automatisé.

→ **Chapitre 36 — Automatisation, orchestration et limites** : automatiser dans le bon ordre, et savoir où s'arrêter.

### Synthèse mentale du chapitre 35

Un système remplacé mais non retiré cumule tous les défauts : plus maintenu, toujours joignable, comptes et secrets intacts — c'est l'actif idéal pour un attaquant. Le décommissionnement est donc un acte de MCS à part entière. Il commence par la mesure de l'usage réel et par une extinction avant suppression, seule méthode fiable pour révéler les dépendances non documentées, notamment annuelles. La section la plus oubliée est celle des révocations, et le point critique y est la révocation **côté fournisseur** : supprimer une clé d'un fichier de configuration ne l'invalide pas. Un décommissionnement se vérifie après un délai d'observation, il ne se déclare pas, et il se clôt par un procès-verbal signé — faute de quoi personne ne répond des résidus découverts deux ans plus tard.

**Trois questions de vérification**

1. Une machine virtuelle a été supprimée de l'hyperviseur. Citez six objets qui peuvent lui survivre, et lequel présente le risque le plus élevé.
2. Pourquoi une analyse de flux de trois semaines est-elle insuffisante pour décider du retrait d'un système ancien ?
3. Que signifie exactement « révoquer » une clé d'API, et en quoi cela diffère-t-il de la supprimer de la configuration ?

---

## Chapitre 36 — Automatisation, orchestration et limites

### 36.1 Que faut-il automatiser en premier

L'ordre importe, et l'intuition conduit généralement au mauvais.

| Rang | Objet | Pourquoi cet ordre |
|---|---|---|
| **1** | **La collecte** — inventaire, versions, états | Sans donnée fiable, tout le reste est faux (§10.1) |
| **2** | **La corrélation** — rapprocher avis et inventaire | Supprime le travail manuel le plus ingrat, sans risque |
| **3** | **La vérification** — contrôler que l'état a changé | Automatiser la preuve libère du temps et améliore l'audit |
| **4** | **Le déploiement** — appliquer les correctifs | Efficace, mais requiert anneaux et critères d'arrêt |
| **5** | **La décision** — prioriser automatiquement | En dernier, et jamais totalement |

**Pourquoi la décision arrive en dernier.** La priorisation dépend de l'exposition et de la criticité métier (§16.2), c'est-à-dire d'informations contextuelles que l'automatisme n'établit pas seul. Un arbre de décision peut être outillé — il l'est utilement — mais ses entrées doivent être fiables, ce qui suppose que les rangs 1 et 2 soient déjà solides.

⚠️ **L'erreur de séquencement la plus fréquente** consiste à automatiser le déploiement en premier, parce que c'est le plus visible. On obtient alors un mécanisme efficace appliqué à un périmètre inconnu — les tableaux de bord verts du §1.4.

### 36.2 Automatiser la remédiation

| Élément | Exigence |
|---|---|
| **Condition de déclenchement** | Écrite, précise, testée : quel type de constat, sur quelle classe d'actif |
| **Périmètre** | Explicitement borné, avec liste d'exclusions |
| **Déploiement témoin** | Obligatoire, même en automatique |
| **Critères d'arrêt** | Chiffrés, évalués automatiquement (§18.4) |
| **Journal** | Chaque action automatique tracée comme une action humaine |
| **Interruption manuelle** | Un moyen d'arrêter immédiatement, connu de l'astreinte |

**Le principe directeur** : l'automatisation ne doit pas retirer de garde-fou. Elle exécute plus vite ce qu'un humain ferait, avec les mêmes protections — anneaux, critères d'arrêt, retour arrière, preuve.

### 36.3 Auto-remédiation : où c'est raisonnable, où c'est dangereux

| Périmètre | Automatisation | Raison |
|---|---|---|
| Postes de travail, correctifs courants | **Raisonnable** | Volume élevé, impact unitaire faible, retour arrière par redéploiement |
| Images et modèles | **Raisonnable** | Corrige la source, effet démultiplié (§28.5) |
| Serveurs C3 non critiques | Raisonnable avec anneaux | Impact limité |
| Serveurs C1 et actifs de niveau 0 | **Déconseillé** | Un incident affecte tout le reste |
| Bases de données | **Déconseillé** | Point de non-retour (§6.7) |
| Équipements réseau | **Déconseillé** | Une erreur coupe l'accès au moyen de la corriger |
| Systèmes industriels | **Proscrit** | Validation constructeur obligatoire (ch. 29) |

**Le critère unique qui résume ce tableau** : automatisez là où **le retour arrière est simple et testé**. Partout ailleurs, l'automatisation transfère un risque humain vers un risque systémique.

### 36.4 La chaîne outillée type

```
Inventaire (source d'autorité, §17.11)
   ↓ enrichi de criticité, exposition, propriétaires
Veille automatisée (§14.6)
   ↓ corrélation, archivage de ce qui est écarté
Constats candidats
   ↓ arbre de décision outillé (§16.3)
Tickets et campagnes (§17.6)
   ↓ affectation automatique par propriétaire d'actif
Déploiement (§18.4)
   ↓ anneaux, critères d'arrêt automatiques
Vérification (§18.9)
   ↓ contrôle de l'état constaté
Preuve archivée (§2.9)
   ↓
Indicateurs (ch. 38)
```

**Les deux points de rupture** les plus fréquents dans cette chaîne : entre l'inventaire et les outils, faute d'identifiant pivot commun (§15.7) ; et entre le déploiement et la vérification, quand la clôture se fait sur déclaration plutôt que sur preuve (§17.8).

### 36.5 L'assistance par intelligence artificielle

**Les usages réellement utiles aujourd'hui**, dans le périmètre de ce cours :

| Usage | Valeur | Précaution |
|---|---|---|
| Résumer un avis technique long | Gain de temps réel | Vérifier les versions affectées à la source |
| Reformuler un constat technique en termes métier | Utile pour les dérogations (§20.10) | Relecture obligatoire |
| Aider à rédiger une règle de détection ou un script | Accélération | Tester avant déploiement |
| Explorer un jeu de données de constats | Aide à l'analyse | Ne pas fonder une décision sur la seule sortie |
| Préparer une communication de crise | Gain de temps sous pression | Validation par le pilote |

**Le risque spécifique** : une sortie plausible mais fausse est plus dangereuse qu'une absence de réponse, parce qu'elle ne déclenche aucune vérification. Une version affectée inexacte, un identifiant inventé, une conclusion sur l'exploitabilité non fondée peuvent orienter une décision entière.

✅ **BONNE PRATIQUE (P0)** — Toute information issue d'une assistance automatisée et destinée à fonder une décision engageante doit être **vérifiée à la source**, et le statut du §14.7 s'applique : ce qui n'est pas vérifié reste une hypothèse.

### 36.6 ⏱ Tendance : volumétrie et vitesse

*Bloc daté, vérifié le 30/07/2026.*

La découverte de vulnérabilités s'accélère, notamment sous l'effet de méthodes de recherche assistées. Trois conséquences pour le dimensionnement des processus, sans dramatisation :

1. **La pression porte sur la vitesse de remédiation**, pas sur la qualité du triage. Une organisation capable de décider vite mais lente à déployer sera limitée par le déploiement.
2. **Le regroupement devient plus rentable que le traitement unitaire** (§16.7) : la montée de version et la reconstruction d'image absorbent le volume, le traitement constat par constat ne le peut pas.
3. **L'exposition redevient le levier principal** : réduire la surface protège indépendamment du volume de vulnérabilités publiées (§11.8).

**Ce qui ne change pas** : l'inventaire, la propriété, les fenêtres, la preuve et le financement. Une organisation qui n'a pas ces cinq bases ne sera pas sauvée par l'automatisation — elle produira simplement plus vite des chiffres faux.

### 36.7 ⚠️ Le risque systémique de l'automatisation

Une mise à jour défectueuse, déployée manuellement, touche quelques machines avant qu'on ne l'arrête. Déployée automatiquement sans garde-fou, elle touche l'ensemble du parc en quelques minutes.

**Les quatre garde-fous non négociables** :

| Garde-fou | Rôle |
|---|---|
| **Déploiement progressif** | Un incident touche un anneau, pas le parc |
| **Critères d'arrêt automatiques** | La campagne s'interrompt sans attendre une décision humaine |
| **Retour arrière testé** | Chronométré, connu de l'astreinte (§18.8) |
| **Interruption manuelle** | Un moyen d'arrêter immédiatement, documenté et connu |

**La règle qui les résume** : *plus le déploiement est rapide, plus les garde-fous doivent être stricts.* L'automatisation sans anneaux n'est pas une accélération, c'est une amplification.

### 36.8 📌 Limites de l'automatisation

- **La dette d'outillage** : chaque automatisme est un actif à maintenir — scripts, connecteurs, règles. Une chaîne outillée non maintenue casse silencieusement.
- **La fragilité des connecteurs** : un changement d'interface côté fournisseur interrompt une intégration, souvent sans alerte.
- **L'effet « tableau de bord vert »** : un automatisme qui échoue silencieusement produit une absence de signal interprétée comme une absence de problème (§15.8).
- **L'automatisation ne crée pas de capacité de décision** : les arbitrages métier, les fenêtres et les dérogations restent humains.
- **Le coût d'intégration** est souvent supérieur au coût de la licence.

✅ **BONNE PRATIQUE (P1)** — Surveillez vos automatismes eux-mêmes : date de dernière exécution réussie, taux d'échec, volume traité. Un automatisme qui ne s'exécute plus est plus dangereux qu'un processus manuel qu'on sait manuel.

→ **Chapitre 37 — Économie du MCS, charge de travail et facteur humain** : financer le dispositif et le rendre soutenable.

### Synthèse mentale du chapitre 36

L'ordre d'automatisation compte, et l'intuition conduit au mauvais : collecte, corrélation, vérification, déploiement, décision — automatiser le déploiement en premier produit un mécanisme efficace appliqué à un périmètre inconnu. L'automatisation ne doit retirer aucun garde-fou : elle exécute plus vite ce qu'un humain ferait, avec les mêmes anneaux, critères d'arrêt et preuves. Le critère qui décide où automatiser est unique : là où le retour arrière est simple et testé. L'assistance automatisée est utile pour résumer, reformuler et explorer, mais une sortie plausible et fausse est plus dangereuse qu'une absence de réponse, car elle ne déclenche aucune vérification. Face à l'accélération de la volumétrie, le regroupement et la réduction d'exposition sont les seuls leviers qui passent à l'échelle. Enfin, un automatisme qui échoue silencieusement transforme une absence de signal en fausse assurance : surveillez vos automatismes comme vous surveillez vos actifs.

**Trois questions de vérification**

1. Votre direction veut automatiser le déploiement des correctifs avant tout le reste. Quel est le problème, et par quoi proposez-vous de commencer ?
2. Sur quel critère unique décidez-vous qu'un périmètre peut recevoir de l'auto-remédiation ?
3. Pourquoi une chaîne d'automatisation non surveillée est-elle plus dangereuse qu'un processus manuel équivalent ?

---

## Chapitre 37 — Économie du MCS, charge de travail et facteur humain

### 37.1 Chiffrer le MCS

Un programme non chiffré n'est pas arbitrable, et un programme non arbitré est financé par défaut — c'est-à-dire mal.

**Les six postes de coût**, dont trois sont presque toujours omis :

| Poste | Contenu | Souvent omis ? |
|---|---|---|
| Personnel | ETP consacrés à la veille, au triage, au déploiement, à la preuve | Non |
| Licences et outillage | Scan, déploiement, gestion, journalisation | Non |
| **Coût d'interruption** | Production perdue pendant les fenêtres | **Oui** |
| **Coût de test** | Environnements, jeux de données, temps métier de validation | **Oui** |
| Dette d'obsolescence | Support étendu, migrations à venir | Parfois |
| **Coût des compensations** | Charge récurrente des mesures compensatoires (§20.7, attribut 5) | **Oui** |

**Les trois postes omis sont ceux qui rendent visible le coût de ne pas faire.** Ils apparaissent ailleurs dans les budgets — production, projets, exploitation — et jamais dans la ligne « sécurité », ce qui fausse tous les arbitrages.

### 37.2 Construire un dossier d'investissement

**La structure qui fonctionne**, en quatre parties :

| Partie | Contenu |
|---|---|
| **1. Situation** | Où nous en sommes, avec les indicateurs de résultat et leur tendance |
| **2. Point de bascule** | À quelle date, sans décision, la situation se dégrade mécaniquement |
| **3. Trois options chiffrées** | Sur la durée complète, jamais sur la première année |
| **4. Recommandation** | Une option, avec son risque résiduel assumé |

**Les trois options doivent toujours inclure le statu quo**, chiffré (§12.5). Une direction n'arbitre pas ce qu'elle ne peut pas comparer, et l'absence de troisième option est la première cause de non-décision.

**Le calcul du coût de ne rien faire** comprend : le coût des compensations maintenues, le surcoût des interventions en urgence, le coût du support étendu, la charge d'astreinte, l'écart de prime d'assurance, et le risque résiduel exprimé en termes métier — jours d'arrêt possibles, données concernées, conséquences contractuelles.

### 37.3 L'assurance cyber

Pour de nombreuses organisations, les questionnaires d'assurance constituent l'un des leviers les plus efficaces pour obtenir un arbitrage sur le MCS (§7.5) — souvent devant l'argument du risque.

**Ce qu'ils exigent typiquement**, et ce que ce cours vous permet de démontrer :

| Exigence du questionnaire | Chapitre correspondant |
|---|---|
| Processus documenté de gestion des correctifs | 7 |
| Délais de correction par criticité, et leur respect mesuré | 7, 38 |
| Inventaire des actifs | 10 |
| Part du parc hors support | 12 |
| Authentification multifacteur sur les accès distants | 24 |
| Sauvegardes testées et immuables | 34 |
| Gestion des accès à privilèges | 24 |
| Délai de détection et de réaction | 21 |

⚠️ **PIÈGE — la déclaration inexacte**
Répondre par l'affirmative à une exigence non tenue peut, en cas de sinistre, fonder un refus de garantie. La réponse honnête assortie d'un plan daté est préférable à une réponse flatteuse — et, en pratique, mieux reçue par les assureurs qu'on ne le croit.

### 37.4 Dimensionner l'équipe

**La méthode par la capacité**, seule fiable, en quatre étapes (§16.5) :

```
1. Mesurer le volume mensuel réel par catégorie de traitement
2. Mesurer le temps réel par unité — pas le temps théorique
3. Calculer la charge, en incluant la preuve et le suivi
4. Confronter à la capacité disponible, en déduisant l'incompressible
```

**Les quatre postes de charge incompressible**, systématiquement sous-estimés : les réunions et le reporting, les urgences non planifiées, la relance des propriétaires, et le traitement de la traîne longue (§18.10).

**Les seuils de rupture à connaître** :

| Signal | Ce qu'il indique |
|---|---|
| Le *backlog* grossit malgré une activité constante | Capacité structurellement insuffisante (§17.10) |
| La part de changements d'urgence dépasse 15-20 % | Le processus normal ne fonctionne pas (§5.1) |
| Les vérifications post-déploiement sont abandonnées | Premier symptôme de surcharge — et le plus coûteux |
| La preuve n'est plus produite | Second symptôme : le pilotage devient impossible |

**Cet ordre s'observe fréquemment** : sous pression, une équipe abandonne souvent d'abord la vérification, puis la preuve, puis la qualification. Elle continue à déployer — l'activité visible — tout en perdant la capacité de démontrer quoi que ce soit. C'est le signal à surveiller.

### 37.5 Astreintes, nuits et week-ends

Le MCS consomme du temps hors horaires : fenêtres nocturnes, interventions de week-end, astreintes de crise.

| Point | Traitement |
|---|---|
| **Prévisibilité** | Fenêtres récurrentes plutôt qu'interventions négociées (§5.2) |
| **Rotation** | Jamais les mêmes personnes ; une astreinte concentrée sur deux personnes est une dépendance critique |
| **Compensation** | Récupération effective, pas théorique |
| **Réduction du besoin** | Redondance, correction à chaud, déploiement progressif (ch. 6) — c'est l'argument économique du §6.13 |

**Le point rarement fait explicitement** : investir dans l'architecture réduit le travail de nuit. C'est un argument qui parle aux équipes et à la direction des ressources humaines autant qu'à la direction financière.

### 37.6 La fatigue de la vulnérabilité

**Le mécanisme.** Une file qui ne se vide jamais, des constats en volume ininterrompu, et l'impression que l'effort ne produit aucun résultat visible. C'est une cause de démotivation documentée, et elle est **structurelle**, pas individuelle.

| Cause structurelle | Remède |
|---|---|
| File infinie | Priorisation qui **exclut** explicitement (§16.3), et campagnes plutôt que constats (§16.7) |
| Absence de résultat visible | Indicateurs de résultat, tendance sur plusieurs trimestres (§38.1) |
| Travail invisible des autres | Communication interne sur ce qui a été évité |
| Responsabilité sans autorité | Le RACI du §9.2 |
| Constats non traités qui s'accumulent | Qualification systématique : dérogation ou dépriorisation, jamais l'oubli (§17.10) |

**Le remède le plus efficace, et le moins coûteux** : mesurer et montrer les **actifs ramenés à un état de référence** plutôt que les vulnérabilités fermées (§16.7). La première mesure progresse et se voit ; la seconde donne l'impression de vider la mer.

### 37.7 Compétences et transmission

| Risque | Traitement |
|---|---|
| Dépendance à une personne clé | Suppléance nommée sur chaque rôle (§14.8) |
| Savoir non documenté | Procédures d'exploitation à jour, testées par une autre personne |
| Perte au départ | Passation formalisée, avec période de recouvrement |
| Outils maîtrisés par une seule personne | Formation croisée, documentation d'administration |

**Le test qui révèle la dépendance** : une personne est absente trois semaines. Que devient le processus ? Si la réponse est « il s'arrête », vous avez une dépendance critique, pas une équipe.

### 37.8 Communiquer vers les métiers

| Situation | Ce qui fonctionne |
|---|---|
| Annoncer une interruption | Préavis, créneau, durée, ce qui se passe si on ne le fait pas |
| Gérer un refus | Qualifier le motif (§20.1), proposer une alternative, formaliser si le refus persiste |
| Après un incident évité | Le dire — c'est la seule occasion où le travail devient visible |
| Demander un budget | Termes métier, options chiffrées, jamais le vocabulaire technique |

🏢 **VU EN RÉUNION** — Présentation d'un plan de sortie d'obsolescence au comité de direction. Le RSSI ouvre sur le nombre de vulnérabilités critiques. Au bout de quatre minutes, le directeur financier interrompt : « combien ça coûte, et qu'est-ce qui se passe si on ne le fait pas ? ». Ces deux questions figuraient en diapositive onze. Depuis, elles sont en diapositive deux.

⚠️ **PIÈGE — la communication par la peur**
Elle fonctionne une fois. À la deuxième, elle produit de la lassitude ; à la troisième, du discrédit. La communication qui tient dans la durée est factuelle, chiffrée, et propose des options.

### 37.9 🔴 FIL ROUGE — septembre 2028 : 62 heures par mois

Lors de l'entretien annuel, Malik Ferhaoui expose à Sonia Weber une mesure qu'il tient depuis six mois : **62 heures par mois** consacrées au MCS, sur un temps de travail théorique de 151 heures. Soit 41 % de son temps, pour une mission qui n'est pas dans sa fiche de poste.

**La décomposition qu'il présente.**

| Activité | Heures/mois |
|---|---|
| Qualification et triage des constats | 12 |
| Planification et coordination des campagnes | 14 |
| Exécution — dont 9 h hors horaires ouvrés | 18 |
| Vérification et production de preuve | 8 |
| Relance des propriétaires d'actifs | **7** |
| Comité, reporting, documentation | 3 |

**La ligne qui déclenche la discussion** est la cinquième : sept heures par mois passées à relancer des personnes qui ne répondent pas. Ce n'est pas du travail technique, c'est le symptôme d'un défaut de gouvernance — les propriétaires sont nommés (§5.5), mais l'affectation d'un ticket ne les engage à rien tant qu'aucun délai de contestation ni aucune escalade automatique n'existe (§17.4).

**Les quatre décisions, et leur effet mesuré trois mois plus tard.**

| Décision | Effet |
|---|---|
| Escalade automatique à J+5 sans réponse du propriétaire, vers son responsable | Relances : 7 h → **1 h** |
| Regroupement des campagnes de C3 en une seule fenêtre mensuelle | Planification : 14 h → 9 h |
| Automatisation de la vérification et de l'export de preuve (§36.1, rang 3) | Vérification : 8 h → 3 h |
| Recrutement d'un alternant en apprentissage sur le suivi et la preuve | Capacité ajoutée, et suppléance créée |

Total après trois mois : **62 h → 37 h**. Aucune de ces mesures n'a réduit le périmètre ni le niveau d'exigence.

**Ce que Sonia Weber retient**, et qu'elle porte au comité stratégique : le poste de charge le plus lourd n'était ni la technique ni le volume, c'était **l'absence de mécanisme d'engagement**. Sept heures mensuelles de relance représentaient, sur deux ans, l'équivalent de plus de vingt jours de travail consacrés à demander à des gens de répondre.

**Le point que Claire Nadeau ajoute.** Les 9 heures mensuelles hors horaires ouvrés ne diminuent pas : elles tiennent aux systèmes non interruptibles. Elles constituent la ligne d'argumentation du dossier d'investissement en redondance présenté au budget 2029 — l'application directe du §6.13, appuyée cette fois sur une mesure et non sur un principe.

**Livrable de l'épisode.** La mesure de charge par activité, reconduite trimestriellement, et l'escalade automatique intégrée au workflow de remédiation (Annexe J).

→ La suite en 🔴 §38.9, quand le directeur financier posera une question sur les indicateurs.

→ **Chapitre 38 — Indicateurs, tableaux de bord et maturité** : mesurer sans produire de chiffres faux.

### Synthèse mentale du chapitre 37

Trois postes de coût du MCS sont presque toujours omis — interruption, test, compensations — et ce sont précisément ceux qui rendent visible le coût de ne rien faire, parce qu'ils apparaissent dans d'autres budgets. Un dossier d'investissement présente toujours trois options chiffrées sur la durée complète, dont le statu quo : son absence est la première cause de non-décision. Les questionnaires d'assurance sont devenus le premier levier réel du MCS, et une réponse honnête assortie d'un plan daté vaut mieux qu'une réponse flatteuse qui peut fonder un refus de garantie. Sous surcharge, une équipe abandonne dans un ordre constant : d'abord la vérification, puis la preuve, puis la qualification — elle continue à déployer tout en perdant la capacité de démontrer quoi que ce soit. La fatigue de la vulnérabilité est structurelle, et son remède le moins coûteux consiste à mesurer les actifs ramenés à un état de référence plutôt que les vulnérabilités fermées. Enfin, le poste de charge le plus lourd est souvent l'absence de mécanisme d'engagement : la relance manuelle se remplace par une escalade automatique.

**Trois questions de vérification**

1. Votre direction estime que le MCS coûte cher. Quels trois postes de coût lui manquent probablement, et où apparaissent-ils actuellement ?
2. Votre équipe déploie toujours autant de correctifs mais ne produit plus de preuve. Que se passe-t-il, et quel symptôme l'a précédé ?
3. Une personne passe sept heures par mois à relancer des propriétaires d'actifs. Est-ce un problème de charge ou de gouvernance, et que corrigez-vous ?

---

## Chapitre 38 — Indicateurs, tableaux de bord et maturité

### 38.1 Ce qu'un indicateur doit permettre de décider

Un indicateur qui ne change aucune décision n'a pas d'utilité, quel que soit son intérêt apparent. Trois questions à poser avant d'en créer un :

1. **Quelle décision** cet indicateur permet-il de prendre, et par qui ?
2. **Quel seuil** déclenche une action ?
3. **Que fait-on** exactement quand ce seuil est franchi ?

Sans réponse aux trois, l'indicateur est décoratif — et il consommera du temps de production chaque mois.

### 38.2 Le dictionnaire d'indicateurs

C'est le livrable central du chapitre. **Chaque indicateur doit être défini par huit attributs**, faute de quoi deux personnes calculeront deux valeurs différentes.

| Attribut | Rôle |
|---|---|
| Formule | Le calcul exact |
| Numérateur | Ce qui est compté |
| **Dénominateur** | Sur quoi c'est rapporté — l'attribut le plus important |
| Périmètre | Quels actifs, quelles classes |
| Période | Sur quel intervalle |
| **Exclusions** | Ce qui est retiré, et pourquoi |
| Source | D'où viennent les données |
| Propriétaire | Qui le produit et en répond |

**Les dix indicateurs de référence** — la fiche complète de chacun figure en **Annexe K** :

| # | Indicateur | Formule | Ce qu'il mesure |
|---|---|---|---|
| 1 | **Couverture d'inventaire** | actifs identifiés / actifs estimés du périmètre | La fiabilité de tout le reste |
| 2 | **Couverture de scan** | actifs scannés avec succès / périmètre de référence | Ce que l'on voit réellement |
| 3 | **Conformité de correctifs** | actifs conformes / actifs éligibles | L'état du parc |
| 4 | **Respect des délais** | constats clos dans le délai / constats arrivés à échéance | La tenue des engagements |
| 5 | **Âge moyen du *backlog*** | moyenne des durées depuis la première détection | La vitesse réelle |
| 6 | **Dette critique échue** | constats critiques dont le délai est dépassé | Le retard qui compte |
| 7 | **Âge des dérogations** | ancienneté moyenne des dérogations ouvertes | La dette formellement acceptée |
| 8 | **Taux de récurrence** | constats réapparus / constats clos | Un problème de source (§17.9) |
| 9 | **Taux de retour arrière** | déploiements annulés / déploiements réalisés | La qualité de la validation |
| 10 | **Taux d'échec de déploiement** | actifs en échec / actifs ciblés | La santé de la chaîne |

**Les indicateurs 1 et 2 conditionnent tous les autres**, et leur combinaison appelle une précaution de vocabulaire.

Le produit *conformité × couverture* — 95 % × 60 % = 57 % — est le **ratio conservateur d'actifs confirmés conformes sur le périmètre**. Il suppose implicitement que **tout actif non mesuré est non conforme**. C'est une hypothèse de prudence, pas une mesure : il ne décrit pas la conformité réelle, qui reste **inconnue** sur les 40 % non mesurés.

✅ **Publier quatre valeurs, jamais une seule** :

| Valeur | Exemple |
|---|---|
| Couverture | 60 % |
| Conformité **dans la population mesurée** | 95 % |
| **Ratio confirmé conforme sur périmètre** | 57 % |
| **Non mesuré** | 40 % |

La dernière ligne est celle qui appelle une décision. Les trois premières décrivent ce que vous savez ; la quatrième décrit ce que vous ignorez.

### 38.3 Les pièges de calcul

| Piège | Mécanisme | Contre-mesure |
|---|---|---|
| **Dénominateur mouvant** | Le périmètre change d'un mois à l'autre, la tendance devient illisible | Périmètre de référence figé, avec ses variations documentées |
| **Exclusions non déclarées** | Les actifs difficiles sortent silencieusement (§15.6) | Liste d'exclusions publiée avec l'indicateur |
| **Agrégation trompeuse** | Un taux global masque une population entière | Publication par population (§10.11) |
| **Moyenne qui masque la traîne** | L'âge moyen cache les constats très anciens | Publier aussi la médiane et le maximum |
| **Indicateur récompensant l'inaction** | Le nombre de vulnérabilités détectées baisse si l'on scanne moins | Toujours associer volume et couverture |
| **Remise à zéro d'historique** | Un actif recréé perd son ancienneté (§15.7) | Identifiant pivot stable |

### 38.4 ⚠️ La discontinuité de modèle comme piège de reporting

Un cas particulier qui mérite d'être isolé, car il produit des conclusions entièrement fausses.

Les modèles de score externes évoluent par versions, et **un changement de version déplace tous les scores simultanément** (§4.5). Conséquence : un indicateur fondé sur un seuil de score peut varier fortement sans qu'aucun correctif n'ait été appliqué et sans qu'aucune vulnérabilité n'ait changé.

**La règle** : toute série temporelle traversant un changement de modèle doit être **marquée comme discontinue** sur le graphique, et l'interprétation doit le mentionner. Avant de célébrer une amélioration soudaine, vérifiez d'abord ce qui a changé dans les données d'entrée.

### 38.5 Concevoir un tableau de bord par audience

| Audience | Nombre d'indicateurs | Contenu | Fréquence |
|---|---|---|---|
| **Exploitation** | 8 à 12 | Opérationnels : échecs, traîne, campagnes en cours, échéances proches | Hebdomadaire |
| **Comité MCS** | 5 à 8 | Résultat : conformité par population, respect des délais, dérogations, dette | Mensuelle |
| **Direction générale** | **3 à 5** | Risque : dette critique, actifs hors support, tendance sur 4 à 8 trimestres | Trimestrielle |
| **Auditeur** | Le dossier de preuves | Définitions, périmètres, exclusions, historique (ch. 39) | À la demande |

**La règle de la direction générale** : trois à cinq indicateurs, une tendance, et une décision demandée. Un comité de direction ne réagit pas à un niveau, il réagit à une **pente** — et il ne peut arbitrer que ce qui lui est présenté sous forme d'options (§12.6).

### 38.6 Le modèle de maturité

Un modèle de maturité sert à situer une organisation et à définir la prochaine étape. Il devient cosmétique dès qu'il sert à s'auto-évaluer favorablement.

| Niveau | Nom | Caractéristique |
|---|---|---|
| **0** | Inexistant | Aucun processus ; les correctifs s'appliquent au gré des incidents |
| **1** | Réactif | On corrige quand un problème survient ; pas d'inventaire fiable |
| **2** | Documenté | Politique écrite, inventaire constitué, propriétaires nommés |
| **3** | Piloté | Délais définis et mesurés, dérogations tracées, indicateurs suivis |
| **4** | Industrialisé | Automatisation, campagnes, preuve produite systématiquement |
| **5** | Adaptatif et fondé sur le risque | Priorisation par exposition et exploitation, boucle d'amélioration, MCS *by design* |

**L'usage utile** : identifier le niveau atteint **par domaine** — inventaire, veille, remédiation, configuration, identités, preuve — et non globalement. Une organisation est rarement au même niveau partout, et un domaine critique faible **plafonne** la maturité de tout ce qui en dépend. La grille par domaine figure en Annexe K.

### 38.7 Historisation et conservation

Sans historique, aucun progrès n'est démontrable — et la démonstration de progrès est ce qui pérennise un budget (§7.5).

| Exigence | Contenu |
|---|---|
| Conservation | Valeurs mensuelles conservées plusieurs années, indépendamment des outils |
| **Indépendance des outils** | Export périodique en format ouvert (§15.12) |
| Traçabilité des définitions | Un changement de formule est daté et documenté |
| Marquage des ruptures | Changement de périmètre, d'outil ou de modèle (§38.4) |

### 38.8 🔬 Mini-lab 9 — Construire un tableau de bord MCS

**Objectif** — Produire un tableau de bord exploitable et repérer les métriques trompeuses.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** §38.2, §38.3, annexes I.4 et K · **Livrable** deux tableaux de bord (comité, direction) + trois métriques trompeuses identifiées.
**Compétences validées** — ✔ définir un indicateur par ses huit attributs ✔ adapter le tableau de bord à son audience ✔ repérer une métrique trompeuse ✔ publier une population non mesurée sans la faire disparaître

**Données fournies.**

| Source | Contenu |
|---|---|
| Inventaire | Périmètre de référence : 340 actifs, dont 28 hors support, 12 sans propriétaire |
| Scans | 268 actifs scannés avec authentification, 31 en échec d'authentification, 41 non scannés (dont 14 exclus documentés) |
| Constats | 1 240 ouverts, dont 38 critiques échus ; âge moyen 74 jours, médiane 21 jours, maximum 610 jours |
| Tickets | 96 ouverts, 14 dépassant leur échéance, 9 sans propriétaire accepté |
| Dérogations | 17 ouvertes, âge moyen 8 mois, dont 4 renouvelées au moins une fois |
| Campagnes | 6 en cours, 2 en retard, taux d'échec moyen 4 % |
| Conformité | 241 actifs conformes sur les 268 scannés avec succès |

**Questions.** (a) Proposez 5 à 8 indicateurs avec leur formule et leur périmètre. (b) Produisez la version comité MCS et la version direction générale. (c) Identifiez trois métriques trompeuses que ces données invitent à produire.

**Corrigé commenté**

**(a) Les indicateurs retenus**

| Indicateur | Formule | Valeur | Commentaire |
|---|---|---|---|
| Couverture de scan | 268 / 340 | **79 %** | Le chiffre qui conditionne tous les autres |
| Conformité interne au scan | 241 / 268 | 90 % | À ne jamais publier seul |
| **Ratio confirmé conforme** | 241 / 340 | **71 %** | Conservateur : traite les 72 non mesurés comme non conformes |
| **Non mesuré** | 72 / 340 | **21 %** | La valeur qui appelle une décision |
| Actifs hors support | 28 / 340 | 8,2 % | Dette structurelle |
| Dette critique échue | 38 constats | 38 | En valeur absolue, pas en taux |
| Âge du *backlog* | médiane / maximum | 21 j / **610 j** | La médiane rassure, le maximum informe |
| Âge des dérogations | moyenne, dont renouvelées | 8 mois, 4 renouvelées | Dette acceptée |
| Actifs sans propriétaire | 12 | 12 | Blocage structurel |

**(b) Les deux versions**

*Comité MCS* — les huit ci-dessus, avec les 41 actifs non scannés détaillés (14 exclus documentés, 27 à traiter) et les 9 tickets sans propriétaire accepté.

*Direction générale* — quatre lignes seulement :
1. Ratio confirmé conforme : **71 %**, avec 21 % non mesuré — tendance sur quatre trimestres.
2. Actifs hors support : **28**, dont X exposés — avec le plan et son coût.
3. Constats critiques échus : **38** — avec la cause principale.
4. Dette acceptée : **17 dérogations**, dont 4 renouvelées — décision demandée sur celles-ci.

**(c) Les trois métriques trompeuses**

| Métrique | Pourquoi elle trompe |
|---|---|
| **« 90 % de conformité »** | C'est la conformité **dans la population mesurée**, sur 79 % de couverture. Le ratio confirmé conforme est de 71 %, et 21 % du périmètre reste **non mesuré** — c'est-à-dire ni conforme ni non conforme (Annexe K.2) |
| **« Âge moyen du *backlog* : 74 jours »** | La moyenne est tirée par un maximum à 610 jours. La médiane à 21 jours décrit le flux normal, le maximum décrit le problème. Publier la seule moyenne ne décrit ni l'un ni l'autre |
| **« 1 240 constats ouverts »** | Volume brut sans priorisation ni couverture. Il baisserait si l'on scannait moins, et il n'indique aucune décision (§5.7) |

**L'erreur attendue** : produire un tableau de bord de quinze indicateurs pour la direction générale. Le nombre d'indicateurs est inversement proportionnel au niveau hiérarchique.

### 38.9 🔴 FIL ROUGE — octobre 2028 : la question du directeur financier

Claire Nadeau présente au comité de direction le tableau de bord trimestriel. Quatre indicateurs, une tendance sur huit trimestres.

| Indicateur | T4 2026 | T4 2028 |
|---|---|---|
| Conformité globale, périmètre de référence | 72 % | **94 %** |
| Actifs hors support | 41 | **9** |
| Constats critiques échus | 61 | **7** |
| Dérogations ouvertes | 3 | **19** |

**La question de Karim Lebrun** porte sur la dernière ligne : *« Les trois premiers indicateurs s'améliorent nettement. Le quatrième a été multiplié par six. Comment interprétez-vous cela ? »*

**La réponse de Claire**, et c'est le point de cet épisode : les 3 dérogations de 2026 ne signifiaient pas que l'organisation n'avait que trois exceptions. Elles signifiaient qu'elle n'en formalisait que trois. Les autres existaient — sous forme de constats jamais traités, de systèmes ignorés, de compensations informelles. Les 19 dérogations de 2028 sont la **partie enfin visible** d'une dette qui a en réalité diminué.

Elle le démontre par un chiffre complémentaire : les constats ouverts depuis plus de 180 jours et non qualifiés — les dérogations non formalisées du §17.10 — sont passés de **47 à 2**.

**Ce que Karim Lebrun demande alors**, et qui devient la meilleure question de tout le fil rouge : *« Alors comment saurai-je, l'an prochain, si 19 dérogations est un bon ou un mauvais chiffre ? »*

**La réponse construite en séance**, qui donnera lieu à deux indicateurs supplémentaires : le nombre de dérogations n'est pas interprétable seul. Ce qui compte est leur **âge moyen** — une dette qui vieillit est une dette qui pourrit (§20.9) — et le **nombre de renouvellements**, qui mesure combien d'exceptions ont échoué à se résoudre.

**Les décisions du comité.**

1. Ajout de deux indicateurs au tableau de bord de direction : âge moyen des dérogations, et nombre de dérogations renouvelées au moins une fois.
2. Revue annuelle en comité de direction des dérogations renouvelées deux fois ou plus — application du §7.4.
3. La progression 72 % → 94 % est communiquée à l'assureur, avec le dossier de preuves associé. La surprime de 34 % d'octobre 2025 (§1.9) fait l'objet d'une renégociation.

**Ce que Claire note en conclusion.** *Le meilleur indicateur de maturité d'une organisation n'est pas son taux de conformité. C'est l'écart entre ce qu'elle sait de ses propres écarts et ce qu'elle en montre.*

→ La suite en 🔴 §39.8, avec la revue interne et la constitution du dossier de preuves.

→ **Chapitre 39 — Audit, contrôle et production de preuve** : prouver, c'est-à-dire résister à un contrôle.

### Synthèse mentale du chapitre 38

Un indicateur qui ne change aucune décision est décoratif, et il coûte du temps de production chaque mois. Huit attributs le définissent, dont le dénominateur, sans lequel deux personnes calculeront deux valeurs différentes. La couverture d'inventaire et la couverture de scan conditionnent tous les autres indicateurs : 95 % de conformité sur 60 % de couverture vaut 57 %. Les moyennes masquent la traîne — publiez médiane et maximum —, et un indicateur de volume brut récompense l'inaction puisqu'il baisse quand on scanne moins. Une série traversant un changement de modèle de score doit être marquée discontinue : vérifiez ce qui a changé dans les données avant de célébrer une amélioration soudaine. Le nombre d'indicateurs est inversement proportionnel au niveau hiérarchique : trois à cinq pour une direction générale, avec une tendance et une décision demandée. Enfin, une hausse du nombre de dérogations peut signaler une amélioration : ce qui compte est leur âge, leur distribution et leur nombre de renouvellements.

**Trois questions de vérification**

1. Votre tableau de bord affiche 90 % de conformité. Quelles deux valeurs devez-vous connaître pour savoir ce que ce chiffre décrit réellement ?
2. Votre indicateur de vulnérabilités à forte probabilité chute de 30 % en une semaine sans aucun déploiement. Que vérifiez-vous avant toute communication ?
3. Le nombre de dérogations de votre organisation a été multiplié par six en deux ans. Est-ce un bon ou un mauvais signe, et quels indicateurs complémentaires permettent de trancher ?

---

## Chapitre 39 — Audit, contrôle et production de preuve

### 39.1 Ce que « prouver son MCS » signifie

Prouver, ce n'est ni affirmer ni montrer un tableau de bord. C'est établir quatre choses, et l'ordre compte :

| # | Ce qu'il faut établir | Sans quoi |
|---|---|---|
| 1 | **Le périmètre** : sur quoi porte le dispositif, et ce qui en est exclu | Tout le reste est invérifiable |
| 2 | **La règle** : ce que l'organisation s'engage à faire, écrit et daté | On ne peut mesurer aucun écart |
| 3 | **L'application** : ce qui a effectivement été fait, avec des données datées | L'engagement reste théorique |
| 4 | **Le traitement des écarts** : ce qui n'a pas été fait, et pourquoi c'est décidé | La preuve devient une fiction |

**Le quatrième point est celui qui distingue un dossier crédible d'un dossier de façade.** Un dossier sans écart n'est pas un bon dossier, c'est un dossier incomplet — aucune organisation n'applique 100 % de sa politique sur 100 % de son parc. Ce que regarde un auditeur, c'est si les écarts sont **connus, décidés et suivis**.

### 39.2 Le dossier de preuves

Structuré une fois, projeté ensuite sur chaque référentiel (§8.8). Onze pièces.

| # | Pièce | Contenu | Chapitre |
|---|---|---|---|
| 1 | **Périmètre de référence daté** | Sources, réconciliation, écarts expliqués, zones déclarées non couvertes | 10 |
| 2 | Politique MCS | Version, date, approbation nominative, classes de service | 7 |
| 3 | RACI et comitologie | Rôles, décideurs, fréquence | 9 |
| 4 | Arbre de décision de triage | Daté, validé | 16 |
| 5 | **Journaux de campagne** | Périmètre, exécution, échecs, traîne longue qualifiée | 18 |
| 6 | **Preuves d'état** | Relevés horodatés sur échantillon, indépendants des outils | 2 |
| 7 | Registre des dérogations | Sept champs, signataires, revues | 7, 20 |
| 8 | Registre des exclusions | Scan, protection des postes, avec motif et compensation | 15, 34 |
| 9 | Comptes rendus de comité | **Décisions**, pas discussions | 9 |
| 10 | Indicateurs historisés | Définitions, séries, ruptures marquées | 38 |
| 11 | Procès-verbaux de décommissionnement | Signés, avec vérification | 35 |

✅ **BONNE PRATIQUE (P0)** — Constituez ce dossier **en continu**, pas à l'approche d'un contrôle. Un dossier reconstitué après coup se voit immédiatement : les dates de production sont groupées, les preuves d'état sont postérieures aux campagnes qu'elles documentent, et les comptes rendus manquent d'aspérités.

### 39.3 Se préparer à un contrôle

| Type de contrôle | Ce qui est regardé en priorité |
|---|---|
| **Certification** | Existence et fonctionnement du système de management ; échantillonnage |
| **Autorité** | Conformité aux obligations applicables, traitement des incidents |
| **Client** | Ce qui concerne **son** périmètre : sa donnée, son service, ses délais |
| **Assureur** | Les points du questionnaire, et leur cohérence avec la réalité (§37.3) |
| **Audit interne** | Écart entre la règle et la pratique |

**Les six constats les plus fréquents**, et le chapitre qui les traite :

| Constat | Origine | Traité au |
|---|---|---|
| Périmètre non défini ou incohérent entre documents | Inventaire absent ou non réconcilié | 10 |
| Indicateurs sans dénominateur | Reporting produit par l'outil | 38 |
| Exceptions non formalisées | Constats anciens jamais qualifiés | 17, 20 |
| Absence de preuve d'application | Clôture sur déclaration | 17, 18 |
| Exclusions non documentées | Actifs difficiles sortis silencieusement | 15, 34 |
| Prestataires non contrôlés | Contrat sans clause de restitution | 13 |

### 39.4 L'audit interne du MCS

Se contrôler soi-même avant qu'un tiers ne le fasse, avec une méthode d'échantillonnage plutôt qu'une revue exhaustive.

**Le plan de contrôle type**, six tests par sondage :

| Test | Méthode | Ce qu'il révèle |
|---|---|---|
| **Test de périmètre** | Prendre 20 actifs au hasard dans une source non utilisée pour le reporting, vérifier leur présence dans le périmètre | Trous d'inventaire |
| **Test d'état** | Vérifier directement sur 15 actifs l'état déclaré conforme | Écart entre déclaration et réalité |
| **Test de délai** | Prendre 10 constats clos, recalculer le délai réel | Fiabilité de l'indicateur |
| **Test de preuve** | Demander la preuve de 10 clôtures | Clôtures sur déclaration |
| **Test de dérogation** | Vérifier que les compensations de 5 dérogations sont **effectivement actives** | Compensations disparues (§20.7) |
| **Test de décommissionnement** | Vérifier les résidus de 5 décommissionnements anciens | Le §35.14 |

**Le cinquième test est le plus productif** : il vérifie une chose que personne ne vérifie jamais, et qui échoue souvent.

### 39.5 Homologation et réhomologation

Dans les contextes où une décision formelle d'autorisation d'usage est requise, le MCS conditionne le maintien de cette décision dans le temps.

| Élément | Ce que le MCS doit fournir |
|---|---|
| Dossier initial | État du système, dispositif de maintien prévu |
| **Maintien** | Preuve que le dispositif fonctionne — c'est le dossier du §39.2 |
| Changements significatifs | Ce qui déclenche un réexamen |
| Réhomologation | Bilan sur la période, écarts, plan |

**Le point pratique** : une homologation prononcée sur la base d'un dispositif de MCS qui n'a pas fonctionné devient contestable. C'est un argument utile en interne pour obtenir les moyens du maintien, et non seulement ceux de la mise en service.

### 39.6 ⚠️ Les preuves qui ne prouvent rien

| Preuve produite | Pourquoi elle ne vaut rien |
|---|---|
| Capture d'écran non datée | Ni date, ni périmètre, ni intégrité |
| Extraction d'outil sans périmètre | On ignore sur quoi elle porte (§15.8) |
| Chiffre agrégé sans dénominateur | Interprétation impossible |
| Politique non approuvée | Un projet n'engage personne |
| Compte rendu relatant des discussions | Aucune décision traçable |
| Déclaration d'un prestataire sans donnée | Confiance, pas preuve (§13.3) |
| Rapport présentant 100 % de conformité | Possible sur un petit périmètre maîtrisé, mais doit déclencher un examen du périmètre, des exclusions et des actifs non joignables |
| Dossier constitué en trois jours | Les métadonnées le montrent |

### 39.7 Conserver la preuve

| Exigence | Contenu |
|---|---|
| Durée | Alignée sur les obligations applicables et la durée de vie des actifs — souvent 3 à 5 ans |
| **Intégrité** | Horodatage, stockage non modifiable, ou signature |
| **Indépendance des outils** | Export en format ouvert : un changement d'outil ne doit pas effacer l'antériorité (§15.12) |
| Accessibilité | Retrouvable en heures, pas en jours |
| Continuité | Les changements de définition et de périmètre sont documentés (§38.7) |

### 39.8 🔴 FIL ROUGE — janvier 2029 : la revue interne

Trois ans après l'arrivée de Claire Nadeau, HELIOMED conduit sa première revue interne complète du dispositif de MCS, avec un auditeur externe mandaté par la direction générale — en préparation d'une exigence client et de la renégociation d'assurance.

**Le dossier présenté** : les onze pièces du §39.2, constituées en continu depuis 2026.

**Les quatre écarts constatés.**

| # | Écart | Origine |
|---|---|---|
| 1 | **12 actifs du périmètre de référence absents de tout outil de gestion** | Machines de laboratoire de Nantes, créées après la dernière réconciliation |
| 2 | **Compensations de 2 dérogations sur 5 testées non actives** | Une règle de filtrage supprimée lors d'une refonte réseau en juin 2028, sans que la dérogation ne soit alertée |
| 3 | **Preuve d'état manquante sur 3 campagnes de 2027** | Clôtures fondées sur le rapport de console seul, sans échantillon vérifié |
| 4 | **Registre des exclusions de la protection des postes incomplet** | 6 exclusions ajoutées après la revue de juillet 2028, non enregistrées |

**Ce que l'auditeur relève comme point fort**, et c'est ce que Claire retient : *« L'organisation connaît ses écarts. Les quatre constats de cet audit portent sur des dispositifs qui existent et qui ont partiellement failli, pas sur des dispositifs absents. Le point le plus favorable du dossier est l'annexe des périmètres déclarés non couverts, tenue depuis 2026. »*

C'est l'annexe d'une page ajoutée à la politique v1 en mai 2026 (§7.7) — celle qui ressemblait à un aveu de faiblesse.

**L'écart n° 2 est celui qui préoccupe le plus l'équipe.** Une compensation disparue signifie qu'un risque accepté sous condition était en réalité porté sans condition, pendant sept mois, sans que personne ne le sache. C'est très exactement le mécanisme du §20.7, attribut 4 — le moyen de vérification existait sur la fiche, mais le contrôle mensuel n'avait pas été réalisé depuis mars.

**Les corrections décidées.**

1. **Contrôle des compensations** inscrit comme point d'ordre du jour permanent du comité MCS, avec test effectif et non déclaratif — cinq minutes par mois (§20.7).
2. **Réconciliation d'inventaire** portée de trimestrielle à mensuelle, automatisée (§10.7).
3. **Échantillon de preuve d'état** rendu obligatoire pour toute campagne de plus de 20 actifs, avec le point de contrôle du §15.13.
4. **Registre des exclusions** rattaché au workflow : aucune exclusion ne peut être ajoutée sans ticket (§34.4).

**Le résultat externe.** L'assureur accepte de ramener la surprime de 34 % à 6 %, sur la base du dossier de preuves et de la trajectoire sur huit trimestres. Le gain annuel dépasse le coût cumulé de l'outillage acquis depuis 2026.

**Ce que Pierre Vasseur dit en clôture du comité**, et qui referme le fil rouge ouvert au §1.9 : *« En octobre 2025, on nous a reproché de ne pas pouvoir démontrer un processus qui existait. Aujourd'hui, on nous reproche quatre écarts dans un processus que nous démontrons. C'est exactement la différence que je voulais. »*

→ **Fin de la Partie VI.** La suite en Partie VII, avec la construction d'un programme complet et les trois cas de synthèse.

→ **Chapitre 40 — Construire un programme MCS de zéro à douze mois** : mettre tout cela en séquence sur douze mois.

### Synthèse mentale du chapitre 39

Prouver son MCS suppose d'établir quatre choses dans l'ordre : le périmètre, la règle, l'application, et le traitement des écarts. Le quatrième distingue un dossier crédible d'un dossier de façade — un dossier sans écart n'est pas bon, il est incomplet, car aucune organisation n'applique 100 % de sa politique sur 100 % de son parc. Onze pièces composent le dossier, à constituer en continu : reconstitué après coup, il se voit immédiatement. L'audit interne se conduit par sondages, et le test le plus productif est celui que personne ne fait jamais — vérifier que les compensations des dérogations sont effectivement actives. Enfin, un rapport annonçant 100 % de conformité est statistiquement invraisemblable : il signale que les actifs non joignables ont été omis.

**Trois questions de vérification**

1. Un auditeur vous demande de démontrer votre gestion des correctifs. Quelles quatre choses devez-vous établir, et dans quel ordre ?
2. Pourquoi un dossier de preuves ne comportant aucun écart est-il un mauvais signe plutôt qu'un bon ?
3. Parmi les six tests d'audit interne, lequel échoue le plus souvent, et pourquoi personne ne le réalise-t-il spontanément ?

---

---

> ### 🎓 À ce stade de la Partie VI, vous savez…
>
> - **retirer** un système proprement, et vérifier qu'il ne survit pas dans les comptes, les clés, les certificats et les sauvegardes ;
> - **automatiser** dans le bon ordre, et reconnaître le seul critère qui autorise l'auto-remédiation ;
> - **chiffrer** le MCS, construire un dossier d'investissement à trois options, et repérer les seuils de rupture d'une équipe ;
> - **définir** un indicateur avec sa population éligible et son dénominateur, et distinguer une mesure d'un ratio conservateur ;
> - **constituer** un dossier de preuves en continu, et conduire un audit interne par sondages.
>
> **Ce qu'il vous reste** : mettre tout cela en séquence, et l'éprouver sur des cas. C'est l'objet de la Partie VII.
