---
title: Vue d'ensemble
source: IT/05 Web & applications/Applications web.md
note: Applications web
up:
- - Applications web
  - index.md
---

## 1. Vue d'ensemble : qu'est-ce qu'une application web ?

### À retenir
Une application web est une application **interactive** qui s'exécute dans un navigateur et repose sur un modèle **client/serveur**. Contrairement à un simple site, elle réagit aux actions de l'utilisateur et renvoie un contenu personnalisé.

### Comment ça fonctionne
On distingue deux moitiés :

- **Front-end (côté client)** : ce que le navigateur télécharge et exécute (HTML, CSS, JavaScript). C'est l'interface visible.
- **Back-end (côté serveur)** : la logique métier, les traitements et les données, exécutés sur un serveur distant.

Le dialogue entre les deux se fait via **HTTP/HTTPS**.

Déroulé typique d'une action :

```
Navigateur → requête HTTP → serveur web → logique applicative → base de données
           ← rendu navigateur ← réponse HTTP ←
```


### Pourquoi c'est important en cyber
Chaque flèche de ce schéma est un point d'interaction, donc une **surface d'attaque potentielle**. Comprendre où s'exécute le code (client vs serveur) détermine ce qu'un attaquant peut voir, modifier ou rejouer.

### Exemple concret
Gmail, Amazon, Google Docs, HTB Academy : toutes des applications web. Le navigateur affiche l'interface, mais l'envoi d'un mail ou le calcul d'un panier se fait côté serveur.

### Point clé à mémoriser
Le front-end **montre**, le back-end **décide**, la base de données **contient la valeur**.

---

## 2. Site web statique vs application web

### À retenir
Un **site statique (Web 1.0)** affiche le même contenu pour tout le monde et ne change qu'avec une modification manuelle du code. Une **application web dynamique (Web 2.0)** génère un contenu différent selon l'utilisateur et ses actions.

### Comment ça fonctionne
Le statique sert des fichiers fixes. Le dynamique exécute du code côté serveur (et parfois côté client) pour construire la page à la volée : session, panier, résultats de recherche, etc.

### Pourquoi c'est important en cyber

> Plus d'interactions = plus d'entrées utilisateur = plus de surface d'attaque.

Un site statique n'accepte presque aucune donnée utilisateur. Une application dynamique traite des formulaires, des paramètres et des fichiers — autant d'occasions d'injection ou de mauvaise validation.

### Point clé à mémoriser
La dynamique apporte la richesse fonctionnelle **et** le risque : chaque entrée utilisateur est une porte à tester.

---

## 3. Application web vs application native

### À retenir
Une application **web** tourne dans un navigateur, indépendamment de l'OS. Une application **native** est installée sur le système et exploite directement ses ressources.

### Comment ça fonctionne

| | Application web | Application native |
|---|---|---|
| Installation | Aucune | Requise par OS |
| Mise à jour | Centralisée (serveur) | Poussée à chaque client |
| Multi-plateforme | Oui (navigateur) | Build par plateforme |
| Performance / matériel | Limitée au navigateur | Accès complet, plus rapide |

Les applications **hybrides / PWA** mélangent les deux : code web tournant avec des capacités natives.

### Pourquoi c'est important en cyber
La mise à jour centralisée du web est un atout défensif : un correctif s'applique pour tous d'un coup. Mais l'exposition Internet permanente élargit la surface accessible à distance.

### Point clé à mémoriser
Web = accessible partout sans installation, donc attaquable partout.

---

## 4. Pourquoi les applications web sont critiques en sécurité

### À retenir
Les applications web sont **exposées sur Internet**, offrent une **large surface d'attaque** et sont souvent connectées à des **données sensibles**. Une seule faille peut servir de point d'entrée vers tout le système d'information.

### Comment ça fonctionne

- Accessibles depuis n'importe quel pays, par n'importe qui ayant un navigateur.
- Outillage automatisé d'attaque très répandu (scanners, exploits).
- Reliées à des bases de données et hébergées sur des serveurs portant d'autres ressources.
- Évoluent en permanence : un simple changement de code peut introduire une vulnérabilité critique.

### Pourquoi c'est important en cyber
Une faille web n'est presque jamais une fin en soi : c'est un **pivot**. Une SQLi exposant des emails → password spraying sur le VPN → foothold dans le réseau interne. C'est l'effet de **chaînage**.

### Exemple concret
Une SQLi sur un portail authentifié via Active Directory permet souvent d'extraire les emails (= identifiants AD), puis de tenter un password spray contre le webmail ou le VPN.

### Point clé à mémoriser
Une faille web compromet rarement *que* l'application : elle ouvre la route vers le reste du SI.

---

## 5. Logique générale d'un pentest web

### À retenir
Pentester une application web ne consiste pas à balancer des payloads au hasard, mais à **comprendre l'application** avant de l'attaquer.

### Comment ça fonctionne
Démarche type (inspirée de l'**OWASP Web Security Testing Guide**) :

1. Analyser le front-end (HTML, CSS, JS) à la recherche de données exposées et d'endpoints.
2. Observer le trafic HTTP entre navigateur et serveur.
3. Identifier la stack technique (serveur web, framework, versions).
4. Tester en **non authentifié**.
5. Tester en **authentifié**.
6. Comparer les **rôles** (user vs admin) pour repérer les défauts de contrôle d'accès.
7. Chercher les vulnérabilités sur chaque entrée.

### Pourquoi c'est important en cyber
La majorité des failles intéressantes (IDOR, broken access control, escalade de privilèges) ne se voient qu'en comparant les comportements selon le contexte d'authentification.

### Point clé à mémoriser
Comprendre l'application > envoyer des payloads. La compréhension dirige les payloads.

---
