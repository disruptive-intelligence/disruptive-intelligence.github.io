---
title: SPF, DKIM, DMARC
source: Cyber/12 Fiches notions/SPF, DKIM, DMARC.md
format: fiche
revue: '2026-10-02'
terms:
  SPF: Enregistrement TXT DNS qui liste les serveurs autorisés à envoyer des mails pour un domaine.
  DKIM: Signature cryptographique du mail par le serveur d'envoi ; le destinataire la vérifie avec la clé publique publiée dans le DNS.
  DMARC: Politique qui dit quoi faire si SPF ou DKIM échoue (none, quarantine, reject), avec du reporting.
---

> Fiche notion assemblée à partir de mes notes (sources en fin de fiche).

## En bref

Mécanismes d'*authentification de l'expéditeur* d'e-mail.

- **SPF** : déclare quels serveurs peuvent envoyer pour un domaine.
- **DKIM** : signe les messages (intégrité + origine).
- **DMARC** : politique combinant SPF/DKIM et reporting (que faire des messages non authentifiés).[^1]

## Comment ça fonctionne

- **DMARC — Domain-based Message Authentication, Reporting & Conformance** protège principalement contre l’**usurpation directe d’un domaine**.
- L'idée est de rejeter les e-mails qui "prétendent" provenir d'une organisation.
- Il s’appuie sur :
    - **SPF** ;
    - **DKIM** ;
    - leur alignement avec le domaine visible dans le champ `From:`.

```
SPF
+
DKIM
+
Domain Alignment
→ DMARC
```


### SPF

- Définit quels serveurs sont autorisés à envoyer des e-mails pour un domaine.

### DKIM

- Ajoute une **signature cryptographique** permettant de vérifier :
    - l’origine du message ;
    - son intégrité.

### DMARC

- Définit la politique à appliquer lorsque les contrôles échouent.

Politiques principales :[^2]

```
p=none
→ monitor

p=quarantine
→ considérer le message comme suspect

p=reject
→ refuser le message
```


Les trois sont complémentaires et indispensables : SPF seul ne suffit pas (contournable), DKIM seul ne suffit pas (pas de politique de rejet), DMARC orchestre les deux et fournit du reporting.[^3]

## Pourquoi c'est important en cyber

**Contre quoi.** Usurpation de domaine (spoofing), phishing/BEC par usurpation directe.[^1]

Le spoofing d'adresse exploite l'absence ou la mauvaise configuration de SPF/DKIM/DMARC pour envoyer un email qui affiche une adresse légitime dans le champ « From ».

En configuration stricte (DMARC p=reject), ces protocoles bloquent le spoofing direct du domaine. Mais ils ne protègent pas contre le typosquatting, les domaines lookalike, le compromission d'email légitime ou le display name spoofing. La protection email est une défense en profondeur, pas une solution unique.[^4]

> DMARC ne bloque pas **tout le phishing**. Il protège surtout contre le spoofing du domaine ; un attaquant peut toujours utiliser un domaine ressemblant au domaine légitime.[^5]

```
company.com
vs
cornpany.com
```


## Déployer

- Tester avant d’appliquer une politique stricte.
- Vérifier notamment :
    - services SaaS envoyant des e-mails ;
    - plateformes marketing ;
    - systèmes de ticketing ;
    - prestataires envoyant « au nom de » l’entreprise.

```
Monitor
→ Fix legitimate senders
→ Quarantine
→ Reject
```


-> Un mauvais déploiement peut bloquer des messages légitimes.[^5]

⚠️ **Erreur fréquente** — DMARC en mode permissif (« none ») jamais durci, donc sans effet.[^1]

## Vérifier

Contrôler les enregistrements publiés :[^6]

```bash
dig technovert.fr MX
dig _dmarc.technovert.fr TXT
```


- **Vérification du sender** : analyser les en-têtes complets (Received, Authentication-Results).[^7]

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
    - résultats SPF / DKIM / DMARC.[^8]

## À retenir

- **SPF/DKIM/DMARC** → SPF = serveurs autorisés. DKIM = signature. DMARC = politique. Les trois ensemble.[^3]

🎯 **À retenir** — SPF+DKIM+DMARC (en mode actif) empêchent l'usurpation directe du domaine : socle anti-phishing/BEC.[^1]

## Sources

[^1]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 294.
[^2]: [HTB — Réponse à incidents](../detection/reponse-a-incident-synthese/index.md), Protection des e-mails.
[^3]: [Infrastructure IT](../../it/infrastructure/infrastructure-it/index.md).
[^4]: [HUMINT & social engineering](../osint/humint-social-engineering/index.md).
[^5]: [HTB — Réponse à incidents](../detection/reponse-a-incident-synthese/index.md).
[^6]: [OSINT Mastery](../osint/osint-cours-complet/index.md), enregistrements DNS.
[^7]: [OPSEC & privacy](../cti/opsec-privacy/index.md).
[^8]: [HTB — Solutions de sécurité](../outils/solutions-de-securite/index.md).
