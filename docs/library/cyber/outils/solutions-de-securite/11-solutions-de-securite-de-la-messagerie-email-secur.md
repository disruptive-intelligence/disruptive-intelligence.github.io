---
title: Solutions de sécurité de la messagerie — Email Security
source: Cyber/10 Outils & solutions/Solutions de sécurité/Solutions de sécurité.md
note: Solutions de sécurité
up:
- - Solutions de sécurité
  - index.md
---

## Email Security Solution

- Solution matérielle ou logicielle destinée à **protéger contre les menaces véhiculées par email**.
- Son objectif principal est d’analyser les emails avant qu’ils n’atteignent l’utilisateur final.

```
Email entrant
→ Analyse
→ Allow / Quarantine / Block / Alert
```

## Fonctions principales

- analyser les **pièces jointes** ;
- analyser les **URLs** présentes dans les emails ;
- détecter et bloquer les emails usurpés (**spoofing**) ;
- bloquer les emails malveillants connus ;
- bloquer les expéditeurs identifiés comme malveillants ;
- générer des alertes / transmettre les informations aux outils ou équipes concernés.

Exemples de menaces ciblées :

```
Phishing
Malicious Attachment
Malicious URL
Email Spoofing
Spam
Malware Delivery
```

### Analyse des pièces jointes

- Les fichiers joints peuvent être analysés pour détecter :
    - signatures malveillantes ;
    - macros suspectes ;
    - malware connu ;
    - comportement anormal.
- Certaines solutions envoient aussi les pièces jointes dans une **sandbox** pour observer leur comportement avant livraison.

```
Attachment
→ AV / Sandbox
→ Malicious ?
→ Block / Quarantine
```

### Analyse des URLs

- Vérifie si les liens contenus dans l’email pointent vers :
    - domaine de phishing ;
    - site malveillant ;
    - malware ;
    - infrastructure connue comme dangereuse.
- Selon la solution, le lien peut être :
    - bloqué ;
    - réécrit ;
    - analysé au moment du clic.
### Email Spoofing

- Un attaquant peut falsifier l’identité apparente de l’expéditeur afin de rendre l’email crédible.
- Exemple :

```
From: ceo@company.com
→ semble légitime
→ réellement envoyé par attaquant
```

- Les solutions de sécurité peuvent utiliser des mécanismes d’authentification email comme :
    - **SPF** → quels serveurs sont autorisés à envoyer pour le domaine ;
    - **DKIM** → signature cryptographique du message ;
    - **DMARC** → politique basée sur SPF/DKIM + reporting.

```
SPF + DKIM + DMARC
→ réduisent l'usurpation de domaine
```

## Limites

- Une solution Email Security seule ne suffit pas.
- À combiner avec :

```
Email Security
+ User Awareness
+ MFA
+ EDR
+ Sandbox
+ SIEM
```

→ un email peut être techniquement propre mais socialement trompeur, d’où l’importance de la sensibilisation utilisateur.
## Logs / informations utiles

- Complément pertinent côté SOC :
    - sender / recipient ;
    - subject ;
    - timestamp ;
    - source IP ;
    - verdict ;
    - URL détectée ;
    - fichier joint ;
    - hash ;
    - action : `Delivered / Blocked / Quarantined` ;
    - résultats SPF / DKIM / DMARC.

```
Email Alert
→ sender
→ URL / attachment
→ verdict
→ action
→ analyste / SIEM
```
