---
title: Protection de la navigation Internet
source: Cyber/99_Concepts/HTB_IT Security for Corporates.md
note: HTB — IT Security for Corporates
up:
- - HTB — IT Security for Corporates
  - index.md
---

- Objectif : empêcher l’accès à des :
    - sites non autorisés ;
    - domaines suspects ;
    - domaines connus comme malveillants.

```
User → DNS / Web Filtering → Allow / Block
```

## DNS Filtering

- Le **DNS Filtering** bloque la résolution de domaines classés comme :
    - malware ;
    - phishing ;
    - C2 ;
    - contenus interdits par la politique interne.
- Peut aussi bloquer certaines catégories non professionnelles.

```
User demande malicious-site.com
→ DNS Filter
→ domaine interdit
→ résolution bloquée
```


> Le filtrage DNS n’est pas forcément réalisé directement par le firewall : il peut être assuré par un **resolver DNS sécurisé**, une passerelle Web ou une solution dédiée.
## URL Shorteners

- Les **raccourcisseurs d’URL** masquent la destination finale d’un lien.
- Ils sont fréquemment utilisés dans :
    - phishing ;
    - redirections malveillantes ;
    - contournement de certains filtres.
- Exemple :

```
https://bit.ly/xxxx
→ destination réelle non visible immédiatement
```

- Selon la politique de l’entreprise :
	- bloquer certains services de shortening ;
	- ou les analyser/résoudre avant autorisation.
## Monitoring des blocages

- Après mise en place du filtrage, il faut examiner les tentatives d’accès bloquées.
- Informations utiles :
	- utilisateur ;
	- device ;
	- domaine demandé ;
	- catégorie ;
	- timestamp ;
	- fréquence des tentatives.

```
DNS Block Logs
→ domaine malveillant
→ quel utilisateur ?
→ quelle machine ?
→ incident isolé ou compromission ?
```

- Une tentative vers un domaine C2 ou phishing peut être un **signal d’investigation**, pas seulement un événement à bloquer.
## Gestion centralisée des navigateurs

- Appliquer une configuration homogène et sécurisée sur les navigateurs de l’entreprise.
- Objectif : réduire les possibilités d’exécution ou d’installation de contenu dangereux.
- Mesures possibles :
	- mises à jour automatiques ;
	- limiter/interdire les extensions non approuvées ;
	- désactiver certains contenus ou fonctions à risque ;
	- imposer les paramètres de sécurité ;
	- contrôler les téléchargements ;
	- appliquer des politiques de navigation.
- Outils possibles selon l’environnement :

```
GPO
Intune
Browser Enterprise Policies
```

## Extensions / Plug-ins

- Une extension navigateur peut disposer de permissions importantes :
    - lire les pages visitées ;
    - modifier leur contenu ;
    - accéder à certaines données utilisateur.

→ utiliser une **allowlist d’extensions approuvées** plutôt que laisser les utilisateurs installer librement n’importe quel plug-in.
