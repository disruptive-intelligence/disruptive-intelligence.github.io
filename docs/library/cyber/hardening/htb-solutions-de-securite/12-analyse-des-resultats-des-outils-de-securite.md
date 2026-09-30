---
title: Analyse des résultats des outils de sécurité
source: Cyber/04_Hardening/HTB_Solutions de sécurité.md
note: HTB — Solutions de sécurité
up:
- - HTB — Solutions de sécurité
  - index.md
---

- Diverses technologies de sécurité fournissent des résultats qui peuvent vous aider à identifier et à répondre aux incidents de sécurité potentiels.
### HIDS / HIPS

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

### Antivirus

- Fournit logs/notifications sur :
    - malware détecté ;
    - fichier concerné ;
    - résultat du scan ;
    - action effectuée : quarantaine, suppression

→ Surveiller les détections et vérifier que la menace a bien été traitée.
### Advanced Malware Removal Tools

- Donnent davantage de détails sur :
    - malware identifié ;
    - suppression/quarantaine ;
    - état du nettoyage.

→ Vérifier que le malware est réellement **contenu et supprimé**.
### Patch Management Tools

- Rapports sur :
    - patches nécessaires ;
    - état du déploiement ;
    - systèmes à jour/non à jour ;
    - échecs d’installation.

→ Prioriser les patches critiques et enquêter sur les systèmes où le déploiement échoue
### UTM — Unified Threat Management
Regroupe plusieurs fonctions de sécurité dans une même solution.
Output possible :

- trafic suspect ;
- virus/spam bloqués ;
- violations de content filtering.

→ Examiner les alertes et rapports réseau.
### DLP

- Génère une alerte lorsqu’un transfert sensible est détecté/bloqué.

Exemples :

```
Copie fichier confidentiel → USB
Email contenant données sensibles → externe
```

→ appliquer les politiques DLP et surveiller les violations.
### DEP — Data Execution Prevention

- Empêche l’exécution de code dans certaines zones mémoire normalement destinées aux **données**.
### WAF — Web Application Firewall

- Filtre le trafic destiné aux **applications Web**.
- Les logs indiquent notamment :
    - requêtes autorisées ;
    - trafic malveillant bloqué ;
    - tentatives d’attaque Web.

```
Client → WAF → Web Application
```

→ analyser les logs pour identifier et répondre aux attaques applicatives.


## Cloud vs On Prem

- Lors de la transition vers des environnements cloud, il est essentiel de traiter les vulnérabilités qui peuvent découler d'erreurs de configuration.
- Voici les principales considérations pour les vulnérabilités basées sur le cloud par rapport aux installations sur site (on-premises) :

### Ports ouverts
**On-Prem :**

- ne pas exposer de ports/services inutiles sur le LAN ou Internet.

**Cloud :**

- éviter les ports inutiles sur VM/services ;
- ne pas exposer directement RDP/SSH si une solution intermédiaire existe.

Exemple Azure :

```
Internet
   ↓
Azure Bastion
   ↓
VM

plutôt que

Internet → RDP 3389 → VM
```


### Authentication Methods
**On-Prem :**

- authentification souvent gérée localement ou via **Active Directory / Domain Controllers**.

**Cloud :**

- ressources potentiellement accessibles mondialement ;
- utiliser **MFA** pour réduire l’impact d’un password compromis.

```
Password
+
Second facteur
→ MFA
```


> Un facteur résistant au phishing est préférable quand disponible ; le SMS reste une forme de MFA mais est moins robuste.
### Conditional Access
**On-Prem :**

- contrôles souvent basés sur réseau, AD et GPO.

**Cloud :**

- **Conditional Access Policies** selon :
    - identité utilisateur ;
    - emplacement ;
    - état/conformité du device ;
    - niveau de risque.

Exemple :

```
Login admin
+
device non conforme
+
pays inhabituel
→ MFA renforcée / accès bloqué
```

### Privilege Management
**On-Prem :**

- permissions locales/AD ;
- contrôle via rôles et groupes.

**Cloud :**

- éviter les privilèges excessifs ;
- appliquer **RBAC + Least Privilege** ;
- limiter fortement les rôles à très hauts privilèges (`Global Administrator`, etc.).
