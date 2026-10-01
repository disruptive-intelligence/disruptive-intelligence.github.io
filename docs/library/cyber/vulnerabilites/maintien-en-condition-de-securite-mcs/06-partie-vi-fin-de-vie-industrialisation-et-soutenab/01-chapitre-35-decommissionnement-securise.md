---
title: Chapitre 35 — Décommissionnement sécurisé
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE VI — Fin de vie, industrialisation et soutenabilité
  - index.md
---

## 35.1 Le cycle de vie ne s'achève pas à « migration effectuée »

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

## 35.2 La décision de retrait

| Élément | Contenu |
|---|---|
| Déclencheur | Migration terminée, usage nul, fin de support, fin de contrat |
| **Mesure de l'usage réel** | Avant tout, comme au §32.7 : qui l'utilise, à quelle fréquence ? |
| Décideur | Propriétaire métier (§9.2) |
| Communication | Préavis proportionné, diffusé largement |
| Période d'observation | Extinction avant suppression, pour révéler les usages non déclarés |

✅ **BONNE PRATIQUE (P0) — l'extinction avant la suppression**
Éteignez avant de supprimer, et observez. Une à quatre semaines selon la criticité. C'est la méthode la plus fiable pour découvrir les dépendances non documentées — celles que §10.5 ne trouve pas, notamment les traitements mensuels ou annuels. Le préavis, lui, réveille les utilisateurs : dans le fil rouge du §5.5, il avait suffi à faire réapparaître onze propriétaires sur vingt-neuf.

## 35.3 Identifier les dépendances

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

## 35.4 Traitement des données

| Étape | Exigence |
|---|---|
| Inventaire des données | Quelles données, quelle sensibilité, quelle durée de conservation légale ou contractuelle |
| Migration ou archivage | Vers où, sous quel format, avec quelle vérification d'intégrité |
| **Vérification de lisibilité** | Un archivage illisible dans cinq ans n'est pas un archivage |
| Effacement | Méthode adaptée au support et à la sensibilité |
| **Preuve d'effacement** | Attestation, journal, certificat de destruction |

**Le point souvent manqué** : l'effacement doit couvrir **toutes** les copies — instantanés, environnements de recette alimentés par une copie (§28.1), exports temporaires, et sauvegardes selon leur politique de rétention.

## 35.5 Retrait des points d'entrée

| Objet | Action |
|---|---|
| Enregistrements de résolution de noms | Suppression, y compris les alias et les entrées internes |
| Publications externes | Retrait de la publication, vérification depuis l'extérieur (ch. 11) |
| Règles de filtrage | Suppression, pas seulement désactivation |
| Entrées de répartiteur de charge | Retrait de la grappe |
| Certificats | Révocation, retrait des magasins où ils étaient déclarés |
| Références dans d'autres configurations | Recherche systématique du nom et de l'adresse |

## 35.6 Révocations

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

## 35.7 Retrait de l'outillage

| Outil | Action | Effet si oublié |
|---|---|---|
| Supervision | Retrait des sondes | Alertes permanentes que l'on finit par ignorer |
| Scanner de vulnérabilités | Retrait du périmètre | Constats sur un actif inexistant (§15.11, faux positif n° 10) |
| Protection des postes | Désinstallation de l'agent, retrait de la console | Licence consommée, machine fantôme dans les indicateurs |
| Sauvegarde | Arrêt des travaux, décision sur les sauvegardes existantes | Sauvegardes orphelines, coût de stockage |
| Gestion de configuration | Retrait du périmètre de convergence | Erreurs récurrentes |
| Outil de déploiement | Retrait | Actif compté dans le dénominateur, jamais joignable |
| **Inventaire** | Passage au statut « décommissionné », **sans suppression de l'historique** | Perte de la trace |

## 35.8 Sauvegardes existantes

Question à trancher explicitement : que fait-on des sauvegardes d'un système retiré ?

| Option | Quand |
|---|---|
| Conservation jusqu'à expiration de la rétention normale | Cas général |
| Conservation prolongée pour raison légale | Obligation de conservation identifiée |
| Suppression anticipée | Données sensibles sans obligation de conservation |

**Dans tous les cas** : la décision est documentée, une date de suppression effective est fixée, et un propriétaire en répond. Une sauvegarde restaurable d'un système décommissionné il y a quatre ans est un risque sans bénéfice.

## 35.9 Matériel et licences

Récupération des licences réaffectables, effacement des supports de stockage avec preuve, destruction ou restitution du matériel avec traçabilité, retrait du parc et de l'assurance. Pour le matériel loué ou repris par un tiers, l'effacement doit être vérifié **avant** la restitution, pas supposé.

## 35.10 Clôture contractuelle

Résiliation des contrats de support associés, arrêt des abonnements liés, retrait des accès du fournisseur (§13.5), récupération des données détenues par le fournisseur, et confirmation écrite de la suppression de son côté.

## 35.11 Vérification finale

**La règle** : un décommissionnement se **vérifie**, il ne se déclare pas.

| Contrôle | Méthode |
|---|---|
| Absence de réponse réseau | Test depuis plusieurs points du réseau |
| Absence dans les sources d'inventaire | Rejeu de la réconciliation (§10.3) |
| Absence d'exposition externe | Nouvelle passe de découverte externe (ch. 11) |
| Absence de comptes actifs | Recherche par nom dans l'annuaire |
| Absence de références résiduelles | Recherche du nom d'hôte dans les configurations |
| **Délai d'observation** | 30 à 90 jours, pour détecter les usages résiduels |

## 35.12 ✅ Livrable — Procès-verbal de décommissionnement

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

## 35.13 🔬 Mini-lab 8 — Décommissionner un serveur

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

## 35.14 🔴 FIL ROUGE — août 2028 : les résidus de décembre 2026

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

## Synthèse mentale du chapitre 35

Un système remplacé mais non retiré cumule tous les défauts : plus maintenu, toujours joignable, comptes et secrets intacts — c'est l'actif idéal pour un attaquant. Le décommissionnement est donc un acte de MCS à part entière. Il commence par la mesure de l'usage réel et par une extinction avant suppression, seule méthode fiable pour révéler les dépendances non documentées, notamment annuelles. La section la plus oubliée est celle des révocations, et le point critique y est la révocation **côté fournisseur** : supprimer une clé d'un fichier de configuration ne l'invalide pas. Un décommissionnement se vérifie après un délai d'observation, il ne se déclare pas, et il se clôt par un procès-verbal signé — faute de quoi personne ne répond des résidus découverts deux ans plus tard.

**Trois questions de vérification**

1. Une machine virtuelle a été supprimée de l'hyperviseur. Citez six objets qui peuvent lui survivre, et lequel présente le risque le plus élevé.
2. Pourquoi une analyse de flux de trois semaines est-elle insuffisante pour décider du retrait d'un système ancien ?
3. Que signifie exactement « révoquer » une clé d'API, et en quoi cela diffère-t-il de la supprimer de la configuration ?

---
