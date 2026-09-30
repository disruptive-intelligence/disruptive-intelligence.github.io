---
title: Chapitre 23 — Dérive de configuration, IaC et immutabilité
source: Cyber/05_Cyberdefense/MCS_COURS_v1.6_2026-08-01.md
note: Cours MCS
up:
- - Cours MCS
  - ../index.md
- - PARTIE IV — Configuration, dépendances et couches oubliées
  - index.md
---

## 23.1 Les mécanismes de la dérive

Une configuration conforme le jour J ne le reste pas. Six mécanismes la dégradent, tous parfaitement légitimes pris isolément :

| Mécanisme | Illustration |
|---|---|
| **Intervention manuelle** | Un paramètre modifié pour résoudre un problème, jamais reversé |
| **Résolution d'urgence** | Un contrôle désactivé pendant un incident, jamais réactivé |
| **Intervention d'un prestataire** | Un tiers applique sa propre configuration de référence |
| **Mise à jour applicative** | L'installeur remet des valeurs par défaut |
| **Restauration** | Retour à un état antérieur à un durcissement |
| **Nouveau projet** | Une exigence projet contredit la *baseline*, sans arbitrage |

**Le point commun** : aucun de ces mécanismes n'est malveillant ni négligent. La dérive n'est pas un problème de discipline, c'est une propriété des systèmes vivants. Elle se traite par la détection et la convergence, pas par la réprimande.

## 23.2 Détecter la dérive

| Méthode | Principe | Signal / bruit |
|---|---|---|
| **Contrôle de conformité périodique** | Rejouer les points de la *baseline* (§22.4) | Bon, si la *baseline* est bien dérivée |
| **Empreinte de configuration** | Comparer un état complet à une référence | Bruit élevé : tout change tout le temps |
| **Détection de changement en temps réel** | Alerter sur modification de fichiers ou de paramètres sensibles | Excellent si le périmètre est **étroit** |
| **Comparaison code / réalité** | Écart entre la description et l'existant | Bon, limité au périmètre décrit |

⚠️ **PIÈGE — la détection de changement à périmètre trop large**
Surveiller « toutes les modifications de configuration » produit des milliers d'alertes quotidiennes légitimes, que personne ne traite. Ciblez : comptes à privilèges, règles de filtrage, paramètres d'authentification, tâches planifiées, points de démarrage. Vingt éléments bien choisis valent mieux que la surveillance exhaustive.

## 23.3 Corriger par convergence

Un outil de gestion de configuration applique un état désiré et le **réapplique périodiquement**. La dérive est corrigée automatiquement, sans intervention.

| Bénéfice | Effet pervers correspondant |
|---|---|
| La configuration revient toujours à la référence | Une correction manuelle légitime est écrasée sans prévenir |
| L'état désiré est documenté dans le code | Le code devient un actif critique à maintenir (§3.5) |
| Le déploiement est reproductible | Une erreur dans le code se propage à tout le parc en quelques minutes |
| L'écart est mesurable | Ce qui n'est pas décrit n'est pas surveillé — et donne une fausse assurance |

**Les deux règles qui évitent les effets pervers** : appliquer le code de configuration **par anneaux**, comme tout déploiement (§18.4) ; et prévoir un mécanisme d'exclusion explicite et tracé pour les actifs devant diverger temporairement.

## 23.4 L'approche immuable

Ne jamais modifier un système en fonctionnement : reconstruire et remplacer (§3.5, §6.10).

**Ce que cela change pour la dérive** : elle devient **impossible par construction** sur la durée de vie de l'instance, qui est courte. Une instance vit quelques jours ou semaines, puis est remplacée par une instance neuve issue d'une image à jour et conforme.

**Les trois conditions de faisabilité**, souvent sous-estimées : les données doivent être externalisées de l'instance ; la reconstruction doit être automatisée et rapide ; et l'application doit tolérer le remplacement de ses instances.

**Le déplacement du problème** : la conformité se joue entièrement dans la **construction de l'image**. C'est là que doivent porter les contrôles (§22.4), et c'est là qu'un défaut se propage à l'ensemble du parc.

## 23.5 Le MCS du code d'infrastructure

Le code qui décrit votre infrastructure est lui-même un actif :

| Objet | Ce qui se dégrade | Traitement |
|---|---|---|
| Modules réutilisés | Vulnérabilités, abandon du mainteneur | Versionnement, revue, mise à jour périodique (ch. 25) |
| Connecteurs vers les fournisseurs | Fins de support, changements d'interface | Suivi des versions supportées |
| Fichier d'état | Contient des secrets, décrit toute l'infrastructure | **Actif de niveau 0** : chiffrement, accès restreint, journalisation |
| Écart code / réalité | Ressources créées à la main | Détection périodique et réconciliation |

⚠️ **PIÈGE — l'illusion de maîtrise**
Un environnement décrit par du code **donne le sentiment** d'être maîtrisé. Mais si 30 % des ressources ont été créées manuellement en dehors du code, la description est fausse — et plus dangereusement fausse qu'une absence de description, parce qu'on lui fait confiance.

## 23.6 Gérer les exceptions et les actifs non convergeables

Certains actifs ne peuvent pas converger : systèmes industriels, appliances fermées, applications imposant une configuration propre, matériel spécialisé.

**Le traitement** : les identifier explicitement, les rattacher à la classe C4 (§7.2), leur appliquer un contrôle manuel périodique documenté, et **les compter séparément** dans les indicateurs. Ce qui n'est pas acceptable, c'est qu'ils disparaissent silencieusement du périmètre contrôlé — c'est le mécanisme de l'exclusion silencieuse du §15.6.

## 23.7 🔴 FIL ROUGE — août 2027 : le serveur d'impression de 2019

Le premier contrôle de conformité automatisé d'HELIOMED, déployé sur les 176 serveurs internes, remonte un résultat global de 87 % — et sept serveurs sous 40 %.

**Le cas le plus instructif** : SRV-PRINT-01, serveur d'impression, 31 % de conformité. L'analyse retrace son histoire.

En novembre 2019, un incident bloque les impressions du siège pendant une demi-journée. Pour rétablir le service, l'administrateur de l'époque — parti depuis — élargit les droits d'un compte de service, désactive deux contrôles d'authentification, et ouvre l'accès depuis l'ensemble du réseau. Le service repart. L'incident est clos.

Rien n'a été reversé. Huit ans plus tard, le compte de service dispose de droits d'administration sur 34 serveurs, l'authentification héritée est toujours active, et le serveur est joignable depuis n'importe quel poste du groupe.

**Ce que révèle le croisement avec le chapitre 11.** SRV-PRINT-01 apparaît dans la matrice des chemins d'attaque comme **étape intermédiaire de trois chemins distincts** menant à des actifs de niveau 0. Il n'avait jamais été identifié comme critique : c'est un serveur d'impression.

**Les décisions.**

1. **Traitement immédiat** des trois points critiques : réduction des droits du compte de service, désactivation de l'authentification héritée après mesure en mode observation (§22.6), restriction de l'accès réseau.
2. **Règle de processus** : toute modification de configuration réalisée pendant un incident est enregistrée dans le journal de l'incident et **fait l'objet d'un ticket de reversion** à la clôture. Sans reversion possible, elle devient un écart motivé et documenté.
3. **Convergence** : le serveur d'impression entre dans le périmètre de l'outil de gestion de configuration, qui n'y avait jamais été déployé.

**Ce que Claire Nadeau retient**, et qu'elle formule au comité : *nous cherchions les serveurs critiques dans la liste des applications métier. Le chemin le plus court vers nos données passait par l'imprimante.*

**Livrable de l'épisode.** La règle de reversion post-incident, intégrée à la procédure de gestion des incidents, et l'extension du périmètre de convergence.

→ La suite en 🔴 §24.11, quand la revue des comptes de service révélera l'ampleur du sujet.

→ **Chapitre 24 — Identités, secrets et cryptographie** : les identités, les secrets et la cryptographie — ce qu'aucun correctif ne réduit.

## Synthèse mentale du chapitre 23

La dérive n'est pas un problème de discipline mais une propriété des systèmes vivants : six mécanismes la produisent, tous légitimes pris isolément, et elle se traite par la détection et la convergence plutôt que par la réprimande. Surveiller toutes les modifications produit un bruit ingérable ; vingt éléments bien choisis — comptes à privilèges, règles de filtrage, authentification, tâches planifiées, points de démarrage — valent mieux que l'exhaustivité. La convergence automatique corrige la dérive mais écrase les corrections légitimes et propage les erreurs en quelques minutes : elle s'applique par anneaux. L'approche immuable rend la dérive impossible par construction, et déplace toute la conformité vers la construction de l'image. Enfin, une infrastructure décrite par du code donne un sentiment de maîtrise qui devient dangereux dès qu'une part significative des ressources a été créée manuellement — une description fausse à laquelle on fait confiance est pire qu'une absence de description.

**Trois questions de vérification**

1. Un contrôle a été désactivé pendant un incident il y a trois ans. Quel mécanisme de processus aurait empêché qu'il le reste, et à quel moment précis s'applique-t-il ?
2. Pourquoi la surveillance exhaustive des changements de configuration produit-elle moins de sécurité qu'une surveillance de vingt éléments ?
3. Votre infrastructure est décrite par du code à 70 %. En quoi cette situation est-elle plus risquée qu'une absence totale de description ?

---
