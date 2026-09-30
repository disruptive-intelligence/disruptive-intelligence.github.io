---
title: IOC, IOA, TTP
source: Cyber/00_Notions/Fiche_IOC_IOA_TTP.md
format: fiche
revue: '2026-10-01'
terms:
  IOC: Indicator of Compromise — trace technique d'une compromission (adresse, condensat de fichier, domaine malveillant), concrète mais éphémère.
  IOA: Indicator of Attack — signe d'un comportement d'attaque en cours, indépendant des artefacts précis.
  TTP: Tactics, Techniques, Procedures — les méthodes de l'attaquant, formalisées par MITRE ATT&CK ; le niveau le plus stable et le plus précieux.
---

> Fiche notion assemblée à partir de mes notes (sources sous chaque bloc).

## En bref

**Définition.** Trois niveaux d'indicateurs de menace, par ordre de valeur croissante.

- **IOC (Indicator of Compromise)** : trace technique d'une compromission (adresse, condensat de fichier, domaine malveillant). Concret mais *éphémère* (l'attaquant change facilement).
- **IOA (Indicator of Attack)** : signe d'un *comportement* d'attaque en cours (séquence d'actions), indépendant des artefacts précis.
- **TTP (Tactics, Techniques, Procedures)** : les *méthodes* de l'attaquant (le « comment » durable), formalisées par MITRE ATT&CK. Le plus stable et le plus précieux.

**Principe : la « pyramide de la douleur ».** Bloquer un IOC gêne peu l'attaquant (il le change) ; détecter ses TTP l'oblige à changer ses méthodes — bien plus coûteux pour lui.

*↳ [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md) (chapitre 247)*

## Comment l'expliquer

Un IOC (Indicator of Compromise) est un artefact observable qui indique qu'une compromission a eu lieu ou est en cours. Ça peut être un hash de fichier malveillant, une adresse IP ou un domaine C2, une clé de registre suspecte, un user-agent inhabituel. Les IOC sont utiles pour la détection immédiate mais ils sont fragiles — l'attaquant les change facilement entre chaque campagne. C'est pour ça que la détection basée sur les TTP (comportements) est plus durable.

*↳ [Questions d'entretien](../../it/culture/questions-d-entretien-cyber-sysadmin/index.md) (réponse type)*

## En pratique

**Blocage d'IoC :** ajout de domaines C2, d'IP, et de hash aux listes de blocage du proxy, du firewall, et de l'EDR. Procédure : vérifier que l'IoC est confirmé (ne pas bloquer une IP Google parce qu'elle apparaît dans une alerte de beaconing), documenter le blocage (qui, quand, pourquoi, IoC exact), et vérifier l'effet (le trafic vers l'IoC est-il effectivement bloqué ?).

*↳ [Analyste SOC](../cyberdefense/analyste-soc/index.md)*

La **corrélation TTP** est plus nuancée : les mêmes techniques ATT&CK sont observées dans deux incidents. C'est un indice de possible lien — mais les techniques ATT&CK sont partagées par de nombreux acteurs (T1059.001 PowerShell est utilisé par quasiment tout le monde). C'est la procédure (le « comment exactement ») qui discrimine, pas la technique générique.

*↳ [CTI](../cti/cyber-threat-intelligence-cti/index.md)*

**Métriques de maturité :** pourcentage des détections basées sur les TTP vs les IoC (plus le % TTP est élevé, plus la CTI est mature — un SOC qui ne détecte que les IoC est au bas de la Pyramid of Pain), […]

*↳ [CTI](../cti/cyber-threat-intelligence-cti/index.md)*

## À retenir

🎯 **À retenir** — Détecter au niveau TTP (comportements/méthodes) fait bien plus mal à l'attaquant que bloquer des IOC volatils.

*↳ [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md) (chapitre 247)*

## Voir aussi

[Frameworks de cyberdéfense (Pyramid of Pain)](../cyberdefense/frameworks-de-cyberdefense-kill-chain-pyramid-of-pain-ukc-diamant/index.md) · [MITRE ATT&CK](../cyberdefense/mitre-att-ck/index.md) · [Défense en profondeur](defense-en-profondeur.md)
