---
title: Chapitre 33 — Suivre un secret
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

## 33.1 Ce qu'on appelle un secret

Mot de passe de service, clé d'interface applicative, certificat client, jeton d'accès, chaîne de connexion à une base. **Ils ont une propriété commune** : celui qui les détient est authentifié **sans être un utilisateur**.

⚠️ **C'est cette propriété qui les rend dangereux** : un secret volé ne déclenche aucun second facteur, aucune alerte de connexion inhabituelle, aucune expiration de session. **Il fonctionne exactement comme il est censé fonctionner.**

## 33.2 Où ils vivent, et qui les voit en clair

| Emplacement | Fréquence | Qui le voit en clair |
|---|---|---|
| **Dans un fichier de configuration** | **Très fréquent** | Toute personne ayant accès au serveur · **et aux sauvegardes** |
| Dans le code source | Fréquent, et grave | Tous ceux qui ont accès au dépôt · **son historique le conserve** |
| Dans une variable d'environnement | Fréquent | Les processus, les journaux de démarrage, les outils de diagnostic |
| Dans un coffre à secrets | Le bon modèle | L'application, à l'exécution seulement |
| **Dans un ticket, un courriel, un tableur** | **Fréquent, jamais avoué** | Tous les destinataires, indéfiniment |

⚠️ **La deuxième ligne mérite d'être soulignée** : un secret retiré du code source reste dans l'historique du dépôt. **Le supprimer ne le supprime pas.** Seule sa rotation le rend inoffensif.

⚠️ **La première ligne aussi, et pour une raison qu'on oublie** : un secret dans un fichier de configuration se retrouve **dans toutes les sauvegardes** de ce serveur. Une sauvegarde de trois ans conserve un secret de trois ans — qui n'a peut-être jamais été changé.

## 33.3 Le chemin d'un secret

```
  ① CRÉATION      qui le génère, et avec quelle qualité
  ② STOCKAGE      fichier · coffre · code
  ③ DISTRIBUTION  comment il arrive sur le serveur
                  → souvent manuellement, par quelqu'un qui l'a vu
  ④ USAGE         chargé en mémoire, parfois écrit dans un journal
  ⑤ ROTATION      changé, ou jamais
  ⑥ RÉVOCATION    ce qui se passe s'il fuit
```


**Les étapes ⑤ et ⑥ sont celles qui manquent presque toujours.** Un secret non tournant reste valide indéfiniment, et sa révocation n'a jamais été testée.

⚠️ **L'étape ③ est la plus sous-estimée.** Un secret distribué manuellement a été vu par au moins une personne, et il figure probablement dans un échange écrit — courriel, ticket, message. **La chaîne de confidentialité est rompue dès la mise en service.**

## 33.4 Le coffre à secrets, et son paradoxe

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne plus stocker de secret en clair | Un composant de plus, **dont la panne empêche les applications de démarrer** |
| Tourner automatiquement | Une intégration applicative — pas toujours possible |
| Tracer qui accède à quoi | Une exploitation supplémentaire |

⚠️ **Le paradoxe, et il est réel** : un coffre indisponible peut empêcher le démarrage de tout ce qui en dépend. **Principe du coût en action** — et une nouvelle dépendance circulaire : le coffre a lui-même besoin d'un secret pour démarrer.

📌 **Comment on résout ce paradoxe en pratique** : les applications conservent le secret en mémoire après l'avoir obtenu. Une panne du coffre n'arrête donc pas ce qui tourne — **elle empêche seulement ce qui redémarre**. C'est une nuance importante : la panne est **différée jusqu'au prochain redémarrage**, comme celle de l'attribution d'adresses, §15.3.

🔥 **SCÉNARIO — l'application ne redémarre plus**

| Question | Réponse |
|---|---|
| Symptôme | L'application tourne. Après un redémarrage planifié, elle refuse de se lancer |
| Hypothèse naïve | « La mise à jour a cassé quelque chose » |
| Dépendance réelle | **Le coffre à secrets est injoignable** — ou le secret a expiré |
| Ce que le schéma aurait dû montrer | Que l'application dépend du coffre **au démarrage** |
| Comment le reconnaître | **Elle fonctionnait, elle ne redémarre plus, rien d'autre n'a changé** |

## 33.5 Sur un schéma

Jamais. Un secret n'est ni un composant, ni un flux dessinable — c'est un attribut d'un flux existant.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Le mot de passe est dans le fichier de conf » | Secret en clair sur le serveur | **Et dans toutes les sauvegardes** |
| « On l'a mis dans le vault » | Un coffre est utilisé | **Est-il un point de rupture au démarrage ?** |
| « On va le changer » | Rotation ponctuelle | **Combien d'endroits faut-il modifier ?** C'est ce qui empêche les rotations |
| « C'est un compte de service » | Une identité non humaine | **Depuis quand son secret n'a-t-il pas changé ?** |

---
