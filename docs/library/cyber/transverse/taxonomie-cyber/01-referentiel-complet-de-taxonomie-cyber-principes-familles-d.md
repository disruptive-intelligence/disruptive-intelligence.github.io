---
title: Référentiel complet de taxonomie cyber — principes, familles d'attaques, défenses et raisonnement SOC/IR
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
chapter: 1
chapters: 15
---

> **Référentiel de référence — Volume 1/8**
> Parties 1 à 3 : Fondations · Grands principes défensifs · Gouvernance, risque et conformité
>
> Ce cours est conçu comme un **cours-pivot** : son objectif n'est pas de cataloguer des attaques isolées, mais de bâtir une **carte mentale** de toute la cybersécurité. On apprend à *classer*, à *relier*, et à passer de l'attaque à la défense.

---

### Comment lire ce cours

Encadrés récurrents utilisés tout au long du cours :

- 🎯 **À retenir** — l'essentiel d'un chapitre, mémorisable en une phrase.
- ⚠️ **Erreur fréquente** — la confusion ou la faute classique à éviter.
- 🔧 **Exemple concret** — illustration conceptuelle, jamais un payload offensif.
- 🛡️ **Défense** — les contre-mesures associées.
- 🧭 **Taxonomie** — où ranger la notion, à quoi elle se relie.

**Cadres de référence** mobilisés (utilisés comme ossature, pas recopiés) : NIST Cybersecurity Framework 2.0 (Govern, Identify, Protect, Detect, Respond, Recover), MITRE ATT&CK (tactiques/techniques/sous-techniques), MITRE D3FEND (contre-mesures), MITRE CAPEC (patterns d'attaque), CWE (faiblesses logicielles), OWASP Top 10 / API Security Top 10 / ASVS.

**Posture du cours :** légal, défensif, pédagogique. On explique les *mécanismes*, les *familles*, les *impacts*, les *signaux de détection* et les *défenses*. On ne fournit ni payload exploitable, ni procédure offensive opérationnelle.

---


## Introduction — Pourquoi une taxonomie ?

### Pourquoi la cybersécurité est illisible sans classification

La cybersécurité souffre d'un problème de **volume** et de **vocabulaire**. Un débutant rencontre en quelques jours des centaines de termes — XSS, SSRF, Kerberoasting, EDR, BOLA, golden ticket, MFA fatigue — sans grille de lecture pour les organiser. Le résultat est une connaissance en « liste de courses » : on connaît des noms, mais on ne sait pas les *ranger*, donc on ne sait pas *raisonner*.

Une taxonomie résout ce problème. Elle transforme une liste plate en **arbre** : familles, sous-familles, types, sous-types. Quand une attaque inconnue apparaît, on n'a plus besoin de la connaître par cœur : il suffit de la rattacher à une famille connue, et on hérite immédiatement de tout ce qu'on sait sur cette famille (mécanisme général, impacts probables, défenses applicables).

### Apprendre des attaques isolées vs comprendre des familles

Apprendre « le reflected XSS » isolément, c'est mémoriser un cas. Comprendre « l'injection » comme famille — *mélange de données et de code, exécuté par un interpréteur qui ne distingue pas les deux* — c'est obtenir une clé qui ouvre XSS, SQLi, command injection, LDAP injection, SSTI, etc. La famille donne le **principe** ; les sous-types ne sont que des variations de contexte (un navigateur, une base SQL, un shell, un annuaire LDAP, un moteur de templates).

C'est la différence entre retenir 300 faits et comprendre 12 principes qui génèrent ces 300 faits.

### Le fil rouge du cours

Tout le cours suit une chaîne de raisonnement unique, déclinée encore et encore :

> **comprendre → classer → relier → défendre → répondre**

Et au niveau d'un objet de sécurité, la chaîne canonique est :

> **actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation**

Retenez cette chaîne : elle est le squelette de toute la discipline. Chaque chapitre du cours occupe une position précise sur cette chaîne.

🎯 **À retenir** — La cybersécurité ne se mémorise pas, elle se *classe*. Une bonne taxonomie est un multiplicateur : elle vous fait comprendre des attaques que vous n'avez jamais vues.

---
