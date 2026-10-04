---
title: Threat modeling
source: Cyber/12 Fiches notions/Threat modeling.md
format: fiche
resume: 'Repérer ce qui peut mal tourner dans un système avant de le construire : DFD, STRIDE, DREAD, PASTA, LINDDUN.'
revue: '2026-10-04'
terms:
  Threat modeling: 'Modélisation des menaces — démarche structurée pour identifier, dès la conception, ce qui peut mal tourner dans un système : actifs, attaquants, menaces et contre-mesures.'
  STRIDE: 'Taxonomie de menaces de Microsoft : Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege ; chaque lettre viole une propriété de sécurité.'
  DREAD: Grille de cotation des menaces (Damage, Reproducibility, Exploitability, Affected users, Discoverability), utile pour prioriser mais jugée subjective.
  PASTA: Process for Attack Simulation and Threat Analysis — méthode de threat modeling en sept étapes, centrée sur le risque métier.
  LINDDUN: 'Taxonomie de menaces pour la vie privée : Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Non-compliance.'
  DFD: Data Flow Diagram — schéma des entités, processus, stockages et flux d'un système, support habituel du threat modeling.
  Frontière de confiance: Trust boundary — limite entre deux zones de confiance différentes ; chaque flux qui la franchit doit être authentifié et validé.
---

> Fiche notion assemblée à partir de mes notes, complétée par les références publiques du sujet (sources en fin de fiche).

## En bref

**Définition.** La *modélisation des menaces* est une démarche structurée pour identifier, **en amont**, ce qui peut mal tourner dans un système : quels actifs protéger, face à quels attaquants, quelles menaces, et quelles contre-mesures.[^1] Elle déplace la découverte des failles du « après le piratage » vers « avant le code ».[^1]

**Quatre questions suffisent à la résumer**[^1][^8] :

1. *Que construit-on ?* — le système, ses actifs, ses flux.
2. *Qu'est-ce qui peut mal tourner ?* — les menaces.
3. *Que fait-on face à chacune ?* — les contre-mesures, ou l'acceptation explicite du risque.
4. *A-t-on bien fait ?* — vérifier, puis revoir le modèle à chaque évolution.

**À ne pas confondre.** Les [Modèles d'analyse de la menace](../cti/modeles-d-analyse-de-la-menace/index.md) (Kill Chain, Diamant, ATT&CK) décrivent **un attaquant** et ce qu'il fait ; le threat modeling analyse **un système** et ce qui peut y casser. Le premier sert la CTI et le SOC, le second la conception.

| | Ce qu'il dit | Ce qu'il ne dit pas |
|---|---|---|
| **Threat model** | Où un système peut être attaqué, et ce qu'on a prévu pour chaque menace | S'il y a des bugs d'implémentation : il ne remplace pas les tests[^2] |
| **Analyse de risques** | Quels risques l'organisation accepte, traite ou transfère | Comment un composant précis peut être attaqué |
| **Pentest** | Si les menaces prévues sont réellement exploitables | Ce qui n'a pas été imaginé au départ |

## Où on s'en sert

- **Développement logiciel** — dans le cycle de développement sécurisé (SSDLC), au début de chaque fonctionnalité significative : le *shift-left* ultime.[^2][^5]
- **Pentest** — le standard PTES en fait une étape à part entière : documenter les actifs métier, les processus, les communautés de menaces et leurs capacités.[^6]
- **IA** — une fonctionnalité LLM se modélise comme le reste : le modèle, le RAG et la base vectorielle deviennent des composants du DFD.[^4]
- **Protection personnelle** — la même logique, appliquée à soi : qui pourrait s'intéresser à moi, avec quels moyens (voir [OPSEC & privacy](../cti/opsec-privacy/index.md)).[^3]

## Le modèle en un coup d'œil : le DFD

Le support habituel est un **diagramme de flux de données** (DFD). Dans Microsoft Threat Modeling Tool, les frontières de confiance sont des lignes pointillées rouges.[^7]

| Élément | Ce que c'est | Exemple |
|---|---|---|
| **Entité externe** (acteur) | Ce qui interagit avec le système sans en faire partie | Utilisateur, médecin partenaire, API tierce |
| **Processus** | Ce qui traite la donnée | Serveur web, API `/share`, fonction serverless |
| **Stockage** | Là où la donnée se pose | Base PostgreSQL, bucket S3, fichiers de logs |
| **Flux** | Le trajet d'une donnée entre deux éléments | Requête HTTPS, message de file, e-mail |
| **Frontière de confiance** | La limite entre deux zones de confiance | Internet / DMZ, client / serveur, tenant A / tenant B |

🎯 **À retenir** — Chaque flux qui franchit une frontière de confiance est un point où l'authentification et la validation doivent être appliquées. C'est là qu'on cherche les menaces en premier.[^2]

## STRIDE : six familles de menaces

Pour chaque élément du DFD, et surtout pour chaque flux qui franchit une frontière, on passe les six lettres en revue. Chacune viole une propriété de sécurité.[^1][^2]

| Lettre | Menace | Propriété violée | Exemple (application web)[^2] | Contre-mesure type |
|---|---|---|---|---|
| **S** | *Spoofing* — usurpation d'identité | Authentification | Un attaquant forge un JWT | Signature vérifiée, MFA |
| **T** | *Tampering* — altération | Intégrité | Le prix est modifié dans la requête | Contrôle côté serveur, signature |
| **R** | *Repudiation* — déni d'une action | Non-répudiation | Aucune journalisation d'audit | Journaux horodatés et protégés |
| **I** | *Information disclosure* — fuite | Confidentialité | Une trace d'erreur s'affiche en production | Messages d'erreur génériques, chiffrement |
| **D** | *Denial of service* | Disponibilité | Une requête sans pagination épuise la base | Limites, quotas, pagination |
| **E** | *Elevation of privilege* | Autorisation | *Mass assignment* `role=admin` | Contrôle d'accès côté serveur, listes blanches |

**LINDDUN, le pendant « vie privée ».** Quand l'enjeu est la donnée personnelle plutôt que la sécurité, LINDDUN pose d'autres questions : peut-on **relier** deux activités (*Linkability*), **identifier** la personne derrière (*Identifiability*), **détecter** qu'une activité a eu lieu (*Detectability*), la personne **ignore**-t-elle ce que deviennent ses données (*Unawareness*) ?[^3][^11]

## Les méthodes, et quand les utiliser

| Méthode | Ce qu'elle apporte | Quand la choisir |
|---|---|---|
| **STRIDE** | Une grille pour ne rien oublier, élément par élément[^5] | Conception d'une application ou d'une fonctionnalité |
| **Arbres d'attaque** | Les chemins d'un attaquant vers un objectif, en arbre de sous-objectifs[^1] | Comprendre comment une menace se réalise concrètement |
| **DREAD** | Une note par menace : dommages, reproductibilité, exploitabilité, utilisateurs touchés, découvrabilité[^5] | Prioriser une liste de menaces — en gardant en tête que la note est subjective |
| **PASTA** | Sept étapes, des objectifs métier jusqu'à l'analyse de risque et d'impact[^9] | Quand le métier doit porter la décision |
| **LINDDUN** | Les menaces sur la vie privée[^11] | Traitement de données personnelles, RGPD |
| **OCTAVE** | Une évaluation stratégique du risque organisationnel, pas seulement technique[^10] | Démarche à l'échelle d'une organisation |
| **VAST** | Des modèles qui passent à l'échelle et s'intègrent au cycle agile et DevOps[^10] | Beaucoup d'équipes, beaucoup d'applications |

## En pratique : le déroulé

Un atelier collaboratif d'une à deux heures avec l'équipe, au début de chaque fonctionnalité significative.[^2]

1. **Décrire** — dessiner le DFD, placer les frontières de confiance, lister les actifs.
2. **Identifier** — passer STRIDE sur chaque élément et chaque flux qui franchit une frontière ; ajouter des *abuse cases* (« et si un médecin partage le dossier d'un autre patient ? »).[^2]
3. **Coter** — prioriser (DREAD, ou simplement vraisemblance × impact).
4. **Traiter** — pour chaque menace : réduire, supprimer, transférer ou accepter explicitement. Les mitigations entrent dans le backlog **avant** le code.[^2]
5. **Vérifier et faire vivre** — tester les mitigations, et revoir le modèle à chaque évolution : un threat model est un document vivant, pas un livrable figé.

## Exemple

🔧 **Exemple concret** — Partage d'un dossier patient avec un médecin externe. DFD : médecin → SPA → API `/share` → PostgreSQL → SendGrid, frontières de confiance identifiées. STRIDE pose trois questions critiques : l'identité du médecin est-elle vérifiée (*Spoofing*) ? le lien de partage est-il devinable (*Information disclosure*) ? peut-on atteindre d'autres dossiers (*Elevation of privilege*) ? Sept menaces relevées, trois critiques, mitigations intégrées au backlog avant le développement.[^2]

## Outils

Un tableur suffit pour commencer. Pour dessiner et suivre le modèle :

- **OWASP Threat Dragon** — libre et gratuit, web ou bureau : diagramme, suggestion de menaces, suivi des mitigations.[^12]
- **Microsoft Threat Modeling Tool** — gratuit : diagramme, menaces STRIDE générées, suivi de leur traitement.[^7]

## Erreurs fréquentes

⚠️ **Erreur fréquente** — **Un modèle trop complexe.** Empiler des menaces fantasmées et des mesures impossibles à tenir, en ignorant les attaques réelles. Le bon test : *« si l'adversaire que je redoute me ciblait demain, que ferait-il en premier ? »* — le plus souvent un phishing ou un mot de passe réutilisé, pas un zero-day.[^3]

⚠️ **Erreur fréquente** — **Croire qu'il remplace les tests.** Le threat modeling trouve les failles de *conception*, pas les bugs d'*implémentation*.[^2]

⚠️ **Erreur fréquente** — **Oublier le hors-périmètre.** Un modèle honnête dit aussi ce qu'il ne couvre pas, pour savoir où ne pas dépenser d'effort.[^3]

## À retenir

🎯 **À retenir** — Que construit-on, qu'est-ce qui peut mal tourner, que fait-on, a-t-on bien fait : le threat modeling relie systématiquement *menace → vulnérabilité potentielle → contre-mesure*, avant qu'une ligne de code n'existe.[^1]

## Voir aussi

[Triade CIA](triade-cia.md) · [Surface d'attaque](surface-d-attaque.md) · [Défense en profondeur](defense-en-profondeur.md) · [Modèles d'analyse de la menace](../cti/modeles-d-analyse-de-la-menace/index.md) · [Sécurité applicative (AppSec)](../hardening/securite-applicative-appsec/index.md) · [OPSEC & privacy](../cti/opsec-privacy/index.md)

## Sources

[^1]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 25 — Threat modeling.
[^2]: [Sécurité applicative (AppSec)](../hardening/securite-applicative-appsec/index.md), chapitre 5 — Modélisation des menaces.
[^3]: [OPSEC & privacy](../cti/opsec-privacy/index.md), chapitre 2 — Threat modeling personnel (2.7 à 2.9).
[^4]: [IA et sécurité](../ia/ia-et-securite/index.md), chapitre 32 — Cas complet : threat modeling d'une fonctionnalité LLM.
[^5]: OWASP — [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html).
[^6]: PTES — [Threat Modeling](http://www.pentest-standard.org/index.php/Threat_Modeling), The Penetration Testing Execution Standard.
[^7]: Microsoft — [Getting started with the Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started).
[^8]: Adam Shostack, *Threat Modeling: Designing for Security*, Wiley, 2014.
[^9]: VerSprite — [PASTA Threat Modeling](https://versprite.com/blog/what-is-pasta-threat-modeling/).
[^10]: Carnegie Mellon SEI — [Threat Modeling: A Summary of Available Methods](https://insights.sei.cmu.edu/library/threat-modeling-a-summary-of-available-methods/), 2018.
[^11]: [LINDDUN](https://linddun.org/) — privacy threat modeling.
[^12]: OWASP — [Threat Dragon](https://owasp.org/www-project-threat-dragon/).
