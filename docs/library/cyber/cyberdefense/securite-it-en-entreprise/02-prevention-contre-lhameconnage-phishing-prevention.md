---
title: Prévention contre l’hameçonnage — Phishing Prevention
source: Cyber/04_Hardening/HTB_Sécurité IT en entreprise.md
note: Sécurité IT en entreprise
up:
- - Sécurité IT en entreprise
  - index.md
---

- Le **phishing** reste un vecteur majeur d’**Initial Access**, au même titre que l’exploitation de vulnérabilités sur des services exposés à Internet.
- La prévention repose sur plusieurs couches : filtrage technique + procédure d’analyse + sensibilisation utilisateur.
## Antispam & Email Security

- Tous les emails entrants doivent passer par un **filtre antispam / Email Security Gateway**.
- Les pièces jointes doivent être analysées par l’**AV**.
- La configuration doit être :
    - maintenue à jour ;
    - adaptée aux nouvelles menaces ;
    - régulièrement revue.

```
Email entrant
→ Antispam
→ AV / analyse pièce jointe
→ Allow / Quarantine / Block
```


- **Complément utile :**
	- analyser également les **URLs** contenues dans les emails ;
	- utiliser SPF / DKIM / DMARC contre certaines formes de spoofing ;
	- sandboxer les pièces jointes suspectes si disponible.
## Procédure d’analyse

- Un employé ayant un doute sur un email doit savoir **à qui le signaler**.
- L’organisation doit prévoir un canal simple :
    - bouton `Report Phishing` ;
    - adresse dédiée ;
    - ticket SOC / IT.

```
Email suspect
→ utilisateur signale
→ SOC / IT analyse
→ verdict + actions
```

- L’objectif est d’éviter que l’utilisateur doive décider seul si l’email est sûr.
## Exercices de phishing

- Réaliser des **phishing simulations** permet de vérifier si les employés savent :
    - reconnaître un email suspect ;
    - ne pas cliquer ;
    - signaler correctement l’événement.
- Ces exercices doivent surtout servir à **mesurer et améliorer la préparation**, pas simplement à piéger les utilisateurs.
- Indicateurs possibles :

```
Click Rate
Credential Submission Rate
Report Rate
```

→ le **Report Rate** est particulièrement intéressant pour mesurer la capacité des utilisateurs à remonter rapidement une menace.
