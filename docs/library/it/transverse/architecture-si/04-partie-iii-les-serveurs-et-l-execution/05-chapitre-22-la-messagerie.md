---
title: Chapitre 22 — La messagerie
source: IT/Architecture_SI.md
note: Architecture SI
up:
- - Architecture SI
  - ../index.md
- - PARTIE III — Les serveurs et l'exécution
  - index.md
---

## 22.1 À quoi ça sert

Recevoir, stocker et distribuer les courriels, et servir de **moyen de récupération** pour de nombreux services.

## 22.2 Ce qu'il fait à la donnée

Il en conserve des années, souvent sans limite, et c'est **le plus grand entrepôt non structuré de l'organisation** — contrats, mots de passe échangés, pièces jointes sensibles, historique de décisions.

## 22.3 La dépendance croisée, et pourquoi elle est structurante

```
   Un service quelconque
        │
        └── « mot de passe oublié » ──► envoie un lien à l'adresse
                                          de messagerie
                                              │
                                              ▼
                                    Qui contrôle la messagerie
                                    contrôle la RÉINITIALISATION
                                    de ce service
```


⚠️ **La conséquence, souvent mal évaluée** : la messagerie est simultanément **une voie d'entrée majeure** et **le point de récupération de nombreux comptes**. Une compromission de messagerie est rarement une compromission de messagerie seule.

**Ce que cela impose en conception** : les comptes d'administration ne doivent pas dépendre de la messagerie pour leur récupération — sinon la chaîne est circulaire.

## 22.4 Deux architectures

```
  A — MESSAGERIE INTERNE
      Internet ──► [ relais ] ──► [ serveur de messagerie ]
      → maîtrise complète · données chez vous
      → un service critique à exploiter, corriger, sauvegarder
      → une exposition permanente sur Internet

  B — MESSAGERIE EN LIGNE
      Internet ──► [ service du fournisseur ]
                          │
                    identités synchronisées
                          ▼
                   [ annuaire interne ]
      → plus de serveur à exploiter
      → une dépendance de disponibilité hors de vos mains
      → ⚠️ le lien d'identités devient critique — §40.2
```


⚠️ **Ce que le passage de A à B ne supprime pas** : les données existent toujours, la voie d'entrée existe toujours, et la dépendance croisée du §22.3 existe toujours. **Ce qui change, c'est qui exploite** — et le fait que les cinq actions du chapitre 43 ne s'appliquent plus à l'infrastructure, mais seulement à la configuration, aux identités et aux données — §42.5.

## 22.5 S'il disparaît

| Effet | Portée |
|---|---|
| Plus de courriels | Immédiat, visible |
| **Plus de réinitialisation de mot de passe** | Différé, et bloquant |
| Plus de notifications applicatives | Différé — des processus métier s'arrêtent silencieusement |

🔥 **SCÉNARIO — la messagerie tombe, et un processus métier s'arrête sans que personne ne le voie**

| Question | Réponse |
|---|---|
| Symptôme | Trois jours plus tard : des commandes n'ont pas été validées |
| Hypothèse naïve | « Les commerciaux n'ont pas fait leur travail » |
| Dépendance réelle | **Le circuit de validation passe par des notifications par courriel** |
| Ce que le schéma aurait dû montrer | Que la messagerie est une **dépendance de processus**, pas seulement un outil |
| Concevoir différemment | Identifier les processus métier qui en dépendent — **presque personne ne l'a fait** |

## 22.6 Sur un schéma

Un relais en zone démilitarisée, et un serveur ou un service en ligne à l'intérieur. **Le relais est souvent le seul élément dessiné.**

⚠️ **Et il reste souvent dessiné après une migration** — c'est l'anomalie n° 1 du cas de synthèse A : un relais devenu inutile, toujours exposé, que plus personne ne surveille.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est passé sur le cloud » | La messagerie est externalisée | **Le relais interne existe-t-il encore ? Est-il encore exposé ?** |
| « Les mails ne partent pas » | Un blocage d'envoi | Relais · réputation · quota · trois causes distinctes |
| « Il a cliqué sur un lien » | Un poste est peut-être compromis | Ce qui compte n'est pas le clic, c'est **ce que ce poste atteint** — §6.2 |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Communiquer avec l'extérieur | **Une voie d'entrée majeure, et historiquement l'une des plus fréquentes** |
| Conserver l'historique des échanges | Un volume et une valeur qui croissent indéfiniment |
| Servir de secours d'authentification | **Une dépendance croisée** |
| Porter des notifications de processus | **Des processus métier qui s'arrêtent silencieusement** en cas de panne |

---
