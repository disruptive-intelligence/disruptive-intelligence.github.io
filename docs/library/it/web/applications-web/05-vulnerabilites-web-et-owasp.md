---
title: Vulnérabilités web et OWASP
source: IT/05 Web & applications/Applications web/Applications web.md
note: Applications web
up:
- - Applications web
  - index.md
---

## 24. Vulnérabilités web courantes

### À retenir
La plupart des failles web sont des **conséquences** de mauvaises décisions dans les couches précédentes (validation absente, contrôle d'accès oublié, requêtes concaténées).

### Comment ça fonctionne (vue d'ensemble)

| Vulnérabilité | Principe | Impact | Prévention (haut niveau) |
|---|---|---|---|
| **Broken Authentication** | Contourner l'authentification | Connexion sans identifiants valides | Auth robuste côté serveur |
| **Broken Access Control** | Accéder à ce qui est interdit | Accès admin, données d'autrui | Contrôle d'accès serveur sur chaque ressource |
| **Malicious File Upload** | Uploader un script exécutable | RCE sur le serveur | Valider type/contenu, stockage non exécutable |
| **File Inclusion** | Inclure un fichier non prévu | Lecture de code, RCE | Pas d'inclusion basée sur entrée utilisateur |
| **Command Injection** | Injecter une commande OS | Exécution sur le serveur | Ne pas passer d'entrée à des commandes système |
| **SQL Injection** | Injecter du SQL | Lecture/écriture base, RCE | Requêtes paramétrées |
| **IDOR / BOLA** | Manipuler un identifiant d'objet | Accès aux ressources d'autrui | Vérifier l'appartenance côté serveur |
| **Security Misconfiguration** | Réglage par défaut/erroné | Exposition variée | Durcissement, revue de config |
| **Vulnerable/Outdated Components** | Composant connu vulnérable | Exploit public | Mise à jour, inventaire des dépendances |

### Pourquoi c'est important en cyber
Comprendre **d'où vient** chaque faille (quelle couche, quelle décision) permet de la détecter, de l'expliquer au client et de proposer une remédiation structurelle.

### Point clé à mémoriser
Une vulnérabilité n'est pas un accident isolé : c'est le symptôme d'une couche mal conçue.

---

## 25. Broken Authentication vs Broken Access Control

### À retenir
Deux notions à ne **jamais confondre** :

- **Authentification** = « **Qui es-tu ?** » (prouver son identité).
- **Autorisation / contrôle d'accès** = « **As-tu le droit ?** » (vérifier les permissions).

### Comment ça fonctionne

- **Broken Authentication** : on contourne la vérification d'identité — login sans identifiants valides, devenir un autre utilisateur.
- **Broken Access Control** : on est authentifié, mais on accède à des ressources/fonctions interdites pour son rôle.

### Pourquoi c'est important en cyber
Ce sont parmi les failles **les plus fréquentes et les plus graves**. Le contrôle d'accès doit être vérifié **côté serveur sur chaque ressource**, pas déduit de l'interface affichée.

### Exemple concret

- Bypass de login via un champ email piégé.
- `roleid` modifiable à l'inscription (`roleid=3` → `roleid=0`) pour s'auto-attribuer un rôle admin.
- Accès direct à `/admin` sans en avoir le droit.
- Modifier `/user/701/edit-profile` en `/user/702/edit-profile` pour éditer le profil d'autrui (IDOR).

### Point clé à mémoriser
Authentification ≠ autorisation. Être connecté ne signifie pas avoir le droit.

---

## 26. File Upload, File Inclusion, Command Injection, SQL Injection

### À retenir
Quatre failles back-end critiques qui partagent une cause commune : **une entrée utilisateur traitée sans contrôle**.

### Comment ça fonctionne

- **Malicious File Upload** : l'application accepte un fichier sans valider type/contenu → upload d'un script (ex. `.php`) → exécution sur le serveur. Les contrôles faibles (extension seule) se contournent (ex. `shell.php.jpg`).
- **File Inclusion** : l'application inclut un fichier dont le chemin dépend de l'entrée utilisateur → lecture de code source, voire RCE.
- **Command Injection** : l'entrée est intégrée dans une commande OS → l'attaquant ajoute sa propre commande (ex. `| commande`) exécutée sur le serveur.
- **SQL Injection** : l'entrée est concaténée dans une requête SQL → l'attaquant modifie la logique de la requête (auth bypass, extraction de données, parfois RCE).

### Pourquoi c'est important en cyber
Ces failles mènent souvent **directement à l'exécution de code** ou à la **compromission de la base**, donc au contrôle du serveur. Ce sont des cibles prioritaires en pentest.

### Prévention (haut niveau)

- Upload : valider type **et** contenu, stocker hors zone exécutable.
- Inclusion : ne jamais baser un chemin d'inclusion sur l'entrée utilisateur.
- Command Injection : éviter d'appeler l'OS avec une entrée ; sinon, échappement strict / API dédiées.
- SQLi : **requêtes paramétrées** (préparées), jamais de concaténation.

> Objectif ici : **comprendre** le mécanisme et l'impact, pas exécuter une exploitation détaillée.

### Point clé à mémoriser
Entrée utilisateur + traitement non contrôlé (fichier, inclusion, commande, requête) = porte vers le serveur.

---

## 27. OWASP Top 10

### À retenir
Le classement de référence des risques web les plus critiques. À connaître comme grille de lecture.

### Liste (version moderne)

1. **Broken Access Control** — accès à des ressources interdites (ex. `/user/702`).
2. **Cryptographic Failures** — chiffrement absent/faible (ex. mots de passe en clair).
3. **Injection** — SQLi, command injection, etc. (entrée non filtrée).
4. **Insecure Design** — faille de conception, pas seulement de code (ex. pas de RBAC prévu).
5. **Security Misconfiguration** — réglages par défaut/erronés (ex. page d'admin exposée).
6. **Vulnerable and Outdated Components** — composant vulnérable connu (ex. plugin non patché).
7. **Identification and Authentication Failures** — authentification cassée (ex. bypass de login).
8. **Software and Data Integrity Failures** — mise à jour/dépendance non vérifiée (ex. pipeline compromis).
9. **Security Logging and Monitoring Failures** — pas de détection (ex. intrusion non journalisée).
10. **Server-Side Request Forgery (SSRF)** — forcer le serveur à émettre des requêtes (ex. accès à un service interne).

### Pourquoi c'est important en cyber
C'est le langage commun du pentest web : savoir classer une faille dans l'OWASP Top 10 structure le rapport et la priorisation.

### Point clé à mémoriser
L'OWASP Top 10 est une **grille de lecture**, pas un substitut à la compréhension de l'architecture.

---

## 28. Public vulnerabilities, CVE et CVSS

### À retenir
Les vulnérabilités publiques sont répertoriées par **CVE** et notées par **CVSS**. Identifier la **version** d'un composant est la première étape pour chercher un exploit.

### Comment ça fonctionne

- **CVE** (Common Vulnerabilities and Exposures) : identifiant unique d'une vulnérabilité connue.
- **NVD** (National Vulnerability Database) : fournit les scores CVSS de base.
- Sources d'exploits : **Exploit-DB**, **Rapid7 DB**, **GitHub advisories**.
- **CVSS** (Common Vulnerability Scoring System) : score de **0 à 10** basé sur des métriques **Base**, **Temporal**, **Environmental** (le NVD ne fournit que la Base).

Sévérité CVSS v3 :

| Sévérité | Score |
|---|---|
| None | 0.0 |
| Low | 0.1–3.9 |
| Medium | 4.0–6.9 |
| High | 7.0–8.9 |
| Critical | 9.0–10.0 |

### Pourquoi c'est important en cyber
Premier réflexe sur une application connue : **identifier le composant et sa version**, puis chercher un exploit public (priorité aux scores 8–10 ou menant à la RCE). À étendre aux composants externes (plugins, dépendances) et au serveur web lui-même (ex. Shellshock).

### Point clé à mémoriser
Pas de version identifiée = pas de recherche d'exploit efficace. Toujours commencer par l'empreinte (fingerprinting).

---
