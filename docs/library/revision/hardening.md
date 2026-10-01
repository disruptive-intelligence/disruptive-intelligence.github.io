---
title: Révision — Hardening
revision: cyber/hardening
domaine: Cyber
sources:
- Cyber/05 Hardening/Sécurité applicative (AppSec).md
---

*D'après le cours [Sécurité applicative (AppSec)](../cyber/hardening/securite-applicative-appsec/index.md)*

## Questions essentielles

- **Question :** Qu'est-ce qu'une injection SQL et comment la prévenir ?
  - **Réponse type :** L'injection SQL se produit quand des données utilisateur sont interprétées comme du code SQL — le développeur concatène l'input directement dans la requête. L'attaquant peut alors extraire des données, modifier la base, ou contourner l'authentification. La solution fondamentale c'est le prepared statement : on sépare la structure de la requête des données. Avec un ORM comme celui de Django ou Sequelize, les requêtes sont paramétrées par défaut. Il ne faut jamais construire une requête SQL par concaténation.

- **Question :** Qu'est-ce qu'un IDOR et pourquoi c'est si courant ?
  - **Réponse type :** Un IDOR, c'est quand l'utilisateur change un identifiant dans l'URL ou l'API — par exemple `/api/patients/1234` → `/api/patients/1235` — et accède aux données d'un autre utilisateur sans que le backend vérifie l'autorisation. C'est courant parce que les développeurs implémentent l'authentification mais oublient l'autorisation : ils vérifient *qui* est l'utilisateur mais pas s'il a le *droit* d'accéder à *cette* ressource. Le fix : vérifier côté serveur, sur chaque endpoint, que l'utilisateur connecté est bien autorisé à accéder à l'objet demandé.

- **Question :** Qu'est-ce que le XSS et quelles sont les protections ?
  - **Réponse type :** Le XSS (Cross-Site Scripting) permet à un attaquant d'injecter du JavaScript dans une page vue par d'autres utilisateurs. L'impact principal c'est le vol de cookies de session. Il y a trois types : Reflected (dans la réponse immédiate), Stored (enregistré en base et affiché à d'autres utilisateurs — le plus dangereux), et DOM-based (manipulation côté client). Les protections : l'output encoding systématique (les frameworks modernes le font par défaut), le cookie HttpOnly (empêche le vol par JS), et une CSP stricte avec des nonces.

- **Question :** C'est quoi un pipeline DevSecOps ?
  - **Réponse type :** C'est l'intégration des contrôles de sécurité directement dans le pipeline CI/CD. En pré-commit, on détecte les secrets avec gitleaks. Au build, on fait du SAST (analyse statique du code) avec Semgrep et du SCA (scan des dépendances) avec pip-audit ou npm audit. En staging, on lance un DAST (scan dynamique) avec ZAP. Au déploiement, on vérifie les politiques et on signe les artefacts. L'idée c'est le shift-left : trouver les vulnérabilités le plus tôt possible, car corriger en production coûte 30 à 100 fois plus cher qu'en développement.

- **Question :** Qu'est-ce que la supply chain security en AppSec ?
  - **Réponse type :** La majorité du code d'une application vient de dépendances tierces. Les attaques supply chain compromettent ces dépendances : typosquatting (un package malveillant avec un nom similaire), dependency confusion (package public qui écrase un package interne), ou compromission d'un maintainer. Les cas connus : SolarWinds, event-stream, XZ Utils. Les défenses : lockfiles avec hashes, registre privé, SCA en continu, SBOM pour inventorier les dépendances, et vérification de signature.

## Questions complémentaires

- **Question :** Qu'est-ce que le threat modeling et comment le pratiquez-vous ?
  - **Réponse type :** Le threat modeling identifie les risques de sécurité dès la conception. On utilise souvent STRIDE : pour chaque composant, on cherche les menaces de Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, et Elevation of Privilege. En pratique, c'est un atelier d'1-2h avec l'équipe de développement au début de chaque fonctionnalité significative. On dessine les flux de données, on identifie les trust boundaries, et on liste les menaces qui deviennent des tâches dans le backlog.

- **Question :** Quels risques spécifiques posent les applications intégrant un LLM ?
  - **Réponse type :** Le risque principal c'est le prompt injection — direct (l'utilisateur manipule le prompt) ou indirect (des données externes contiennent des instructions cachées). Il y a aussi le insecure output handling : si la sortie du LLM est insérée dans du HTML sans encodage, c'est du XSS. Et l'excessive agency : si le LLM peut exécuter des actions (modifier une base, envoyer un email), un prompt malveillant peut lui faire faire des choses non prévues. La règle de base : traiter la sortie du LLM comme une source non fiable, exactement comme une entrée utilisateur.

## Questions les plus probables en entretien

1. Injection SQL : principe et prévention ?
2. IDOR : c'est quoi, pourquoi c'est courant ?
3. XSS : types et protections ?
4. C'est quoi un pipeline DevSecOps ?
5. Supply chain security : risques et défenses ?
6. OWASP Top 10 : les catégories clés ?

## Réponses flash

- **Injection SQL** → Input interprété comme code. Fix = prepared statements / ORM. Jamais de concaténation.
- **IDOR** → Changement d'ID → accès non autorisé. Fix = vérification d'autorisation côté serveur sur chaque endpoint.
- **XSS** → JS injecté dans la page. Fix = output encoding, HttpOnly, CSP avec nonces.
- **DevSecOps** → Sécurité dans le CI/CD : SAST (code), SCA (dépendances), DAST (scan dynamique), secrets detection.
- **Supply chain** → Dépendances compromises. Fix = lockfiles, registre privé, SCA, SBOM, signature.
- **Threat modeling** → STRIDE, DFD, trust boundaries. Atelier en amont du développement.
- **LLM security** → Prompt injection, insecure output, excessive agency. Traiter la sortie LLM comme source non fiable.

---

> **Note de clôture**
>
> Ce cours a été conçu pour enseigner la sécurité applicative comme une discipline complète — du code à la production, de l'attaque à la défense, de la vulnérabilité individuelle au programme d'entreprise.
>
> SecureHealth illustre une transformation que toute organisation peut réaliser : en 12 mois, une équipe sans référent sécurité est passée de 3 vulnérabilités critiques à un score SAMM de 2.0/3, un pipeline DevSecOps complet, des Security Champions formés, un bug bounty actif, et la capacité de détecter et contenir un incident supply chain en 48 heures. Le coût : 50-150K€/an. Le coût de ne rien faire : 4-10M€ par breach.
>
> Le cours assume trois convictions. Première : l'AppSec ne s'arrête pas au secure coding — elle couvre la prévention, la vérification, la détection et la gouvernance. Un code parfaitement sécurisé déployé dans un environnement mal configuré, sans logging, et sans processus de gestion des vulnérabilités est un incident en attente. Deuxième : les surfaces d'attaque évoluent — la supply chain logicielle, les applications intégrant de l'IA, et les environnements cloud-native sont les terrains de 2025-2026, et ce cours les couvre. Troisième : la défense en profondeur fonctionne — chaque couche (code, tests, WAF, monitoring, IR) est contournable individuellement, mais les empiler force l'attaquant à dépenser plus de temps et à générer plus de signaux.
>
> *Comprendre la vulnérabilité • Écrire le code qui la prévient • Détecter l'attaque qui l'exploite • Construire le programme qui pérennise la sécurité.*
