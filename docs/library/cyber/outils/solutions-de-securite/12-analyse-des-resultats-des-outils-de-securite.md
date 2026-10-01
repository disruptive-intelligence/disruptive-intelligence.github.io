---
title: Analyse des résultats des outils de sécurité
source: Cyber/10 Outils & solutions/Solutions de sécurité/Solutions de sécurité.md
note: Solutions de sécurité
up:
- - Solutions de sécurité
  - index.md
---

- Diverses technologies de sécurité fournissent des résultats qui peuvent vous aider à identifier et à répondre aux incidents de sécurité potentiels.
## HIDS / HIPS

- **Output** : alertes sur des activités suspectes détectées sur l’hôte.
- Examiner :
    - date/heure ;
    - source ;
    - compte impliqué ;
    - événement déclencheur.

```
HIDS → détecte
HIPS → détecte + peut bloquer
```

## Antivirus

- Fournit logs/notifications sur :
    - malware détecté ;
    - fichier concerné ;
    - résultat du scan ;
    - action effectuée : quarantaine, suppression

→ Surveiller les détections et vérifier que la menace a bien été traitée.
## Advanced Malware Removal Tools

- Donnent davantage de détails sur :
    - malware identifié ;
    - suppression/quarantaine ;
    - état du nettoyage.

→ Vérifier que le malware est réellement **contenu et supprimé**.
## Patch Management Tools

- Rapports sur :
    - patches nécessaires ;
    - état du déploiement ;
    - systèmes à jour/non à jour ;
    - échecs d’installation.

→ Prioriser les patches critiques et enquêter sur les systèmes où le déploiement échoue
## UTM — Unified Threat Management
Regroupe plusieurs fonctions de sécurité dans une même solution.
Output possible :

- trafic suspect ;
- virus/spam bloqués ;
- violations de content filtering.

→ Examiner les alertes et rapports réseau.
## DLP

- Génère une alerte lorsqu’un transfert sensible est détecté/bloqué.

Exemples :

```
Copie fichier confidentiel → USB
Email contenant données sensibles → externe
```

→ appliquer les politiques DLP et surveiller les violations.
## DEP — Data Execution Prevention

- Empêche l’exécution de code dans certaines zones mémoire normalement destinées aux **données**.
## WAF — Web Application Firewall

- Filtre le trafic destiné aux **applications Web**.
- Les logs indiquent notamment :
    - requêtes autorisées ;
    - trafic malveillant bloqué ;
    - tentatives d’attaque Web.

```
Client → WAF → Web Application
```

→ analyser les logs pour identifier et répondre aux attaques applicatives.
