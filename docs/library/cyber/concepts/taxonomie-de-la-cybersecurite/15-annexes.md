---
title: Annexes
source: Cyber/11 Concepts/Taxonomie de la cybersécurité.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

## Annexe A — Glossaire cyber essentiel

- **Actif** : ce qui a de la valeur et qu'on protège (donnée, service, système, identité).
- **Menace** : danger potentiel (acteur/événement) pouvant nuire.
- **Vulnérabilité** : faiblesse exploitable.
- **Risque** : combinaison vraisemblance × impact d'une menace exploitant une vulnérabilité.
- **Impact** : gravité des conséquences.
- **CIA/DIC** : Confidentialité, Intégrité, Disponibilité.
- **Authentification** : prouver son identité. **Autorisation** : déterminer ses droits.
- **Surface d'attaque** : ensemble des points exploitables.
- **Défense en profondeur** : empilement de couches indépendantes.
- **Moindre privilège** : droits strictement nécessaires.
- **Zero Trust** : ne jamais faire confiance par défaut, toujours vérifier.
- **Assume breach** : supposer la compromission pour mieux limiter/détecter/répondre.
- **Tiering** : cloisonnement des niveaux d'administration (Tier 0/1/2).
- **MFA** : authentification multi-facteur ; *résistant au phishing* = FIDO2/passkeys, number matching.
- **EDR/NDR/SIEM/SOAR** : détection/réponse hôte / réseau / corrélation centrale / automatisation.
- **IOC/IOA/TTP** : indicateur de compromission / d'attaque / tactiques-techniques-procédures.
- **CVE/CVSS/EPSS/KEV** : identifiant de vulnérabilité / score de gravité / probabilité d'exploitation / catalogue d'exploitation active.
- **SBOM** : inventaire des composants logiciels.
- **PRA/PCA** : reprise / continuité d'activité ; **RTO/RPO** : délai de reprise / perte de données acceptables.
- **Lateral movement** : déplacement interne de l'attaquant.
- **RCE** : exécution de code à distance.
- **Pentest / bug bounty / purple teaming** : test offensif ponctuel / continu communautaire / collaboration red-blue.


## Annexe B — Tableau de correspondance central (fiche réflexe)

> **Tableau-pivot du référentiel** (enrichi en V2). Pour chaque attaque majeure : famille, vulnérabilité-racine, surface, propriété CIA visée, **logs utiles** (où chercher), **défenses principales**. C'est l'outil pratique à garder sous la main pour relier *attaque ↔ vulnérabilité ↔ surface ↔ impact ↔ détection ↔ défense* en une ligne.

| Attaque | Famille | Vulnérabilité-racine | Surface | Impact CIA | Logs utiles | Défenses principales |
|---|---|---|---|---|---|---|
| Stored XSS | Injection | Encodage de sortie absent | Web | Confidentialité / Intégrité | Logs applicatifs, rapports CSP, WAF | Encodage contextuel, CSP, cookies HttpOnly |
| Reflected/DOM XSS | Injection | Sortie/sink non sécurisés | Web / navigateur | Confidentialité | Logs app, CSP, analyse JS client | Encodage, CSP, Trusted Types |
| SQLi | Injection | Requête concaténée | Web / base | Confidentialité / Intégrité | Erreurs SQL, logs base/app, WAF | Requêtes paramétrées, moindre privilège base |
| Command injection | Injection | Concaténation vers shell | Web / serveur | C/I/Disponibilité | EDR serveur (processus enfants), logs app | API sans shell, allowlist, moindre privilège |
| SSTI | Injection | Entrée dans la structure du template | Web / serveur | C/I/D (RCE) | Logs app, EDR, comportement d'évaluation | Données en variables (jamais en template), sandbox |
| XXE | Parsing | Entités externes XML activées | Web / API | Confidentialité (+SSRF) | Logs app, accès fichiers/réseau du parser | Désactiver entités externes & DOCTYPE |
| IDOR / BOLA | Contrôle d'accès | Défaut d'autorisation par objet | Web / API | Confidentialité / Intégrité | Logs API (accès hors périmètre), énumération d'IDs | Contrôle d'accès par objet côté serveur, deny by default |
| BFLA | Contrôle d'accès | Défaut d'autorisation par fonction | API | Intégrité / privilège | Logs API (appels privilégiés) | Contrôle d'autorisation par fonction, séparation des rôles |
| SSRF → métadonnées | Falsification requête | Validation/allowlist d'URL insuffisante | Web / cloud | Confidentialité (secrets) | Proxy/app, NDR, accès au point de métadonnées, audit cloud | Allowlist, egress filtering, métadonnées renforcées, moindre privilège du rôle |
| CSRF | Falsification requête | Pas de jeton anti-CSRF / SameSite | Web | Intégrité | Logs app (requêtes sans jeton/origine incohérente) | Jetons anti-CSRF, SameSite, vérification d'origine |
| Path traversal / LFI / Zip Slip | Accès fichiers | Chemin dérivé d'une entrée | Web / serveur | Confidentialité (+RCE) | Logs app (séquences de traversée), accès fichiers | Allowlist mappée, normaliser puis vérifier l'appartenance |
| Unrestricted upload | Accès fichiers | Type/emplacement non contrôlés | Web | C/I/D (RCE) | Logs upload, EDR, accès aux fichiers servis | Valider le contenu réel, stockage hors webroot, domaine isolé |
| Insecure deserialization | Intégrité logicielle | Désérialisation d'entrée non fiable | Web / serveur | C/I/D (RCE) | EDR (instanciation/processus), logs app | Ne pas désérialiser le non fiable, signer/typer strictement |
| Request smuggling | Parsing protocole | Désaccord de framing entre serveurs | Web / infra | Intégrité / Confidentialité | Logs frontal/back incohérents, outils dédiés | Normaliser au frontal, rejeter l'ambiguïté, HTTP cohérent |
| Cache poisoning / deception | Infra web | Clé de cache incomplète / cache de privé | Web / CDN | Intégrité / Confidentialité | Logs cache/CDN, réponses incohérentes | Clé de cache complète, ne jamais cacher le privé |
| Bucket public | Mauvaise configuration | Accès public par défaut | Cloud | Confidentialité | CSPM, audit cloud, accès anonymes | Blocage public par défaut, CSPM, chiffrement |
| Clé/secret exposé | Exposition de secrets | Secret hors coffre | Cloud / CI-CD | Confidentialité | Secrets scanning, audit cloud (usage de clé) | Coffre-fort, portée minimale, rotation, scanning |
| Privilege escalation cloud | Autorisation cloud | Permissions IAM dangereuses | Cloud | C/I/privilège | Audit IAM (modif. politiques/rôles) | Moindre privilège, suppression des chemins d'auto-élévation |
| Kubernetes RBAC abuse | Autorisation conteneurs | RBAC trop large | Conteneurs | C/I/privilège | Audit Kubernetes, API server | Moindre privilège RBAC, comptes de service minimaux |
| Container escape | Élévation conteneurs | Conteneur privilégié / montages | Conteneurs | C/I/D | Runtime security, EDR, audit | Conteneurs non privilégiés, capacités/montages minimaux |
| Dependency confusion / typosquat | Supply chain | Résolution de paquets | CI-CD / dépendances | C/I/D (RCE) | Logs build, résolution de sources | Dépôts internes prioritaires, lockfiles, SBOM/SCA |
| CI/CD / pipeline poisoning | Supply chain | Build/pipeline non protégé | CI-CD | C/I/D | Logs CI, intégrité des artefacts | Moindre privilège, isolation, provenance/signature (SLSA) |
| Password spraying | Authentification | Mots de passe faibles, pas de MFA | Identité | C/privilège | Auth logs (échecs multi-comptes), sign-in logs | MFA, bannissement de mots de passe courants, détection de spraying |
| Credential stuffing | Authentification | Réutilisation de mots de passe | Identité / SaaS | Confidentialité | Sign-in logs (taux d'échec élevé, sources distribuées) | MFA, détection d'identifiants fuités, rate limiting |
| Kerberoasting | Identité (AD) | Compte de service/SPN + mot de passe faible | Active Directory | Confidentialité / privilège | Kerberos 4769 (TGS-REQ + chiffrement faible), EDR | gMSA, mots de passe longs, tiering, détection comportementale |
| Pass-the-hash / ticket | Identité (AD) | Réutilisation de secrets + privilèges excessifs | Active Directory | Privilège / latéral | Auth NTLM/Kerberos anormales, EDR | Tiering, LAPS, Credential Guard, restriction NTLM |
| DCSync | Identité (AD) | Droits de réplication excessifs | Active Directory | Confidentialité (secrets domaine) | Réplication depuis hôte non-DC, audit droits | Restreindre/surveiller les droits de réplication (Tier 0) |
| Golden ticket | Identité (AD) | Secret krbtgt compromis | Active Directory | Privilège / persistance | Tickets aux propriétés anormales (durée/chiffrement) | Protéger krbtgt, double rotation post-incident, surveillance DC |
| AD CS abuse | Identité (AD) | Modèles de certificats permissifs | Active Directory | Privilège / persistance | Inscriptions de certificats anormales, audit CA | Durcir modèles & droits, CA en Tier 0 |
| Lateral movement | Mouvement latéral | Réutilisation d'identifiants + réseau plat | Réseau / AD | Latéral / privilège | Connexions inter-machines, EDR/NDR, SIEM | Segmentation, tiering, LAPS, MFA admin |
| Ransomware | Impact (multi) | Accès + propagation + privilèges | Multi | Disponibilité (+Confidentialité) | EDR (chiffrement, suppression clichés), auth, exfiltration | Sauvegardes immuables/testées, segmentation, MFA, tiering, détection précoce |
| Wiper | Impact (destruction) | Accès + sabotage | Multi | Disponibilité / Intégrité | EDR (destruction), comportements | Sauvegardes hors-ligne, segmentation, continuité |
| Infostealer | Malware (vol) | Malware sur poste + secrets accessibles | Poste / identité | Confidentialité | EDR (accès aux stockages de secrets), connexions par jeton | EDR, expiration de session, MFA anti-phishing |
| Phishing | Ingénierie sociale | Confiance humaine, pas de MFA fort | Messagerie / humain | Confidentialité | Sign-in logs, logs mail/proxy, création de règles de boîte | Sensibilisation, filtrage mail, SPF/DKIM/DMARC, MFA anti-phishing |
| BEC | Ingénierie sociale | Confiance + pas de double validation | Messagerie / humain | Intégrité (fraude) | Logs mail (expéditeur/domaine), règles de boîte | Double validation hors canal, séparation des tâches, DMARC |
| Consent phishing | Ingénierie sociale / OAuth | Octroi OAuth non gouverné | SaaS / identité | Confidentialité / persistance | Journaux d'octrois OAuth | Gouvernance des consentements OAuth, allowlist d'applications |
| MFA fatigue | Contournement MFA | Push simple (approuver/refuser) | Identité | Privilège / accès | Volume anormal de demandes MFA, approbation après rafale | MFA résistant au phishing (FIDO2, number matching) |
| ARP/DNS/DHCP spoofing → MITM | Usurpation réseau | Protocoles non authentifiés | Réseau | Confidentialité / Intégrité | NDR, anomalies d'association, alertes WIPS | DAI, DHCP snooping, chiffrement authentifié, DNSSEC |
| DNS tunneling | Exfiltration / C2 | DNS sortant non inspecté | Réseau | Confidentialité | Logs DNS (volume/entropie/fréquence), NDR | Inspection/filtrage DNS, détection d'anomalies |
| DDoS | Disponibilité | Capacité finie / spoofing | Réseau | Disponibilité | NetFlow, signatures DDoS, alertes amont | Anti-DDoS amont (scrubbing/CDN), anti-spoofing (BCP38) |
| BGP hijacking | Routage | Confiance BGP non validée | Infra Internet | Intégrité / Disponibilité | Monitoring BGP, anomalies de chemins | RPKI, filtrage de préfixes, MANRS |

🧭 **Mode d'emploi.** Lire une ligne de gauche à droite, c'est dérouler le fil rouge sur une attaque : *où elle frappe* (surface), *pourquoi elle marche* (vulnérabilité-racine), *ce qu'elle vise* (CIA), *où la voir* (logs), *comment l'arrêter* (défenses). Pour une attaque inconnue, appliquer d'abord la méthode du chapitre 306, puis l'inscrire dans ce format.


## Annexe C — Tableau surface → attaques typiques → logs utiles

| Surface | Attaques typiques | Sources de logs utiles |
|---|---|---|
| Poste utilisateur | Phishing, malware, infostealer | EDR, logs système, proxy/DNS |
| Active Directory | Kerberoasting, DCSync, pass-the-hash | Journaux AD/Kerberos, EDR, SIEM |
| Application web | XSS, SQLi, IDOR, SSRF | Logs applicatifs, WAF, accès HTTP |
| API | BOLA, BFLA, exposition de données | Logs API/passerelle |
| Cloud | Buckets publics, IAM, métadonnées | Journaux cloud (audit), CSPM |
| Réseau | Scan, MITM, lateral movement | NDR/IDS, flux (NetFlow), DNS |
| Messagerie | Phishing, BEC, malspam | Logs mail, DMARC reports |
| Conteneurs/K8s | RBAC abuse, container escape | Audit Kubernetes, runtime security |


## Annexe D — Tableau de correspondance des cadres

| Besoin | Cadre de référence |
|---|---|
| Fonctions de sécurité de haut niveau | NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) |
| Tactiques/techniques adverses | MITRE ATT&CK |
| Contre-mesures défensives | MITRE D3FEND |
| Patterns d'attaque | MITRE CAPEC |
| Faiblesses logicielles | CWE |
| Risques applicatifs web | OWASP Top 10 |
| Risques API | OWASP API Security Top 10 (2023) |
| Vérification applicative | OWASP ASVS |
| Intégrité de la supply chain | SLSA, SBOM |
| Analyse de risque | EBIOS RM, ISO 27005, FAIR |
| Gestion de la sécurité | ISO/IEC 27001 |

**Logique de lecture :** ATT&CK décrit *ce que fait l'attaquant* ; CWE/CAPEC, *par quelle faiblesse/pattern* ; D3FEND, *comment se défendre* ; NIST CSF, *comment organiser le tout* ; OWASP, *les risques applicatifs concrets*.


## Annexe E — Fiches réflexes

**XSS** — Encoder la sortie selon le contexte ; CSP ; cookies HttpOnly ; assainir le HTML riche. *Racine : injection côté navigateur.*

**SQLi** — Requêtes paramétrées partout (y compris données stockées) ; moindre privilège base ; erreurs génériques. *Racine : injection SQL.*

**SSRF** — Allowlist de destinations ; bloquer plages internes et service de métadonnées ; filtrage sortant ; durcir les rôles d'instance. *Racine : confiance dans une URL fournie.*

**Phishing** — Sensibilisation + culture du signalement ; filtrage mail ; SPF/DKIM/DMARC ; MFA résistant au phishing. *Racine : manipulation humaine.*

**Ransomware** — Sauvegardes immuables/testées ; segmentation ; MFA ; EDR ; patch ; tiering ; plan de crise/PRA. *Racine : multiple (accès + propagation).*

**Compromission AD** — Tiering (protéger le Tier 0/krbtgt) ; PAM/bastion ; LAPS ; Credential Guard ; audit ACL/délégations/GPO ; surveillance. *Racine : exposition/réutilisation de secrets privilégiés.*


## Annexe F — Mini-cas d'analyse défensive

**Cas 1 — Alerte « connexion réussie après 200 échecs sur 200 comptes ».**
Classer : authentification, password spraying (chapitre 165). Réponse : confiner le compte réussi, vérifier MFA, chercher le mouvement latéral. Fond : MFA + détection de spraying.

**Cas 2 — Un serveur web initie des requêtes vers l'adresse interne de métadonnées.**
Classer : SSRF vers métadonnées cloud (chapitre 107). Réponse : couper, vérifier l'usage des identifiants de rôle, roter. Fond : allowlist SSRF + métadonnées renforcées + moindre privilège.

**Cas 3 — Chiffrement massif de fichiers + suppression de clichés sur plusieurs serveurs.**
Classer : ransomware (chapitre 188), avec lateral movement. Réponse : confiner/segmenter, déclencher la cellule de crise et le PRA, restaurer depuis l'immuable. Fond : sauvegardes immuables + segmentation + MFA + tiering.


## Annexe G — Cartographie des métiers cyber

- **SOC analyst (N1/N2/N3)** : détection, triage, qualification, réponse de premier niveau.
- **Incident responder / DFIR** : investigation, forensic, éradication, rétablissement.
- **Threat intelligence (CTI)** : connaissance des menaces, acteurs, TTP, alimentation de la détection.
- **Pentester / Red team** : test offensif autorisé, simulation d'adversaire.
- **Blue team / Detection engineer** : construction et réglage des détections.
- **Purple team** : pont red/blue pour améliorer la détection.
- **GRC / Risk manager** : gouvernance, analyse de risque, conformité, homologation.
- **Security architect** : conception sécurisée (secure by design, Zero Trust).
- **AppSec / Product security** : sécurité du développement (SAST/DAST, threat modeling).
- **Cloud security engineer** : sécurité des environnements cloud (IAM, configuration, CSPM).
- **IAM/PAM engineer** : identités, accès, comptes privilégiés.
- **RSSI / CISO** : pilotage stratégique de la sécurité.

🧭 Ces métiers se répartissent sur le fil rouge : *prévenir* (architecture, AppSec, GRC), *détecter/répondre* (SOC, DFIR, CTI), *évaluer* (pentest, purple), *gouverner* (RSSI, GRC).


## Annexe H — Apprendre les attaques sans apprendre à attaquer illégalement

Principes pour progresser de façon **légale et éthique** :

1. **Comprendre les mécanismes, pas les payloads** : ce cours privilégie le *pourquoi ça marche* et *comment s'en défendre*.
2. **S'entraîner uniquement dans des environnements autorisés** : laboratoires personnels isolés, plateformes d'entraînement légales et dédiées, machines virtuelles vous appartenant, environnements de CTF/lab conçus pour cela.
3. **N'attaquer que ce qu'on est explicitement autorisé à tester** : un test sur un système sans autorisation écrite est illégal, même « pour apprendre ».
4. **Privilégier la posture défensive (blue/purple)** : détecter, comprendre les TTP (ATT&CK), construire des détections — une voie d'apprentissage riche et sans risque légal.
5. **Pratiquer la divulgation responsable** : si l'on découvre une faille, la signaler par les canaux prévus (bug bounty, contact sécurité), jamais l'exploiter.
6. **Se former via les cadres** : ATT&CK, OWASP, CWE/CAPEC, D3FEND offrent une montée en compétence structurée et légale.

⚠️ La frontière est simple : la *connaissance* est libre ; l'*action* sur un système exige une *autorisation*. Ce cours vise la première et la défense.


## Annexe I — Bibliographie indicative et standards à surveiller

- **NIST Cybersecurity Framework 2.0** — organisation des fonctions de sécurité.
- **MITRE ATT&CK** — base de connaissances des TTP adverses (à suivre, mise à jour régulière).
- **MITRE D3FEND** — contre-mesures défensives.
- **MITRE CAPEC** — patterns d'attaque.
- **CWE** — faiblesses logicielles (Top 25 mis à jour périodiquement).
- **OWASP Top 10** (web) et **OWASP API Security Top 10** (API) — révisés régulièrement.
- **OWASP ASVS** — exigences de vérification applicative.
- **ISO/IEC 27001 / 27005** — management et risque.
- **EBIOS Risk Manager (ANSSI)** — méthode d'analyse de risque.
- **CIS Benchmarks / CIS Controls** — durcissement et contrôles prioritaires.
- **SLSA** et travaux SBOM (formats type CycloneDX/SPDX) — intégrité de la supply chain.
- **Catalogue KEV (CISA)** — vulnérabilités activement exploitées, pour prioriser.

> **Note de mise à jour.** La cybersécurité évolue vite : versions de référentiels, nouvelles techniques, nouveaux outils. La *taxonomie* de ce référentiel (les familles et les principes) reste stable ; les *détails* (versions, CVE, produits) doivent être réactualisés via les sources ci-dessus.


## Annexe J — Schémas mentaux (ASCII)

> Quelques cartes mentales minimalistes à mémoriser. En cybersécurité, un bon schéma vaut souvent un paragraphe.

**Le fil rouge du référentiel**

```text
ACTIF → MENACE → VULNÉRABILITÉ → RISQUE → ATTAQUE → IMPACT → DÉTECTION → RÉPONSE → REMÉDIATION
```


**Chaîne d'un chemin d'attaque typique (du clic au domaine)**

```text
Phishing/Exploit → Poste compromis → Vol d'identifiants → Mouvement latéral → Tier 0 → Domaine compromis
   (Initial Access)   (Execution)      (Credential Access)   (Lateral Mvt)     (PrivEsc)   (Impact)
```


**SSRF → cloud (deux surfaces)**

```text
Attaquant → Application vulnérable (URL fournie) → Service de métadonnées → Identifiants de rôle → Ressources cloud
            [allowlist + egress filtering]          [métadonnées renforcées]  [moindre privilège du rôle]
```


**Injection (principe unique, plusieurs interpréteurs)**

```text
Entrée non fiable ─┬─► Navigateur  → XSS
                   ├─► SQL         → SQLi
                   ├─► Shell       → Command injection
                   ├─► LDAP/XPath  → LDAP/XPath injection
                   └─► Template    → SSTI
   Parade commune : SÉPARER données et code (paramétrage + encodage de sortie)
```


**Cycle de réponse à incident**

```text
Événement → Alerte → Triage → Qualification → [Incident] → Investigation →
Confinement → Éradication → Rétablissement → REX ──(boucle d'amélioration)──► Préparation
```


**Tiering Active Directory (étanchéité)**

```text
Tier 0  [Contrôleurs de domaine, krbtgt, IAM, AD CS]   ◄── ne jamais exposer ses identifiants plus bas
   ▲ (jamais de contrôle depuis le bas)
Tier 1  [Serveurs & applications]
   ▲
Tier 2  [Postes de travail]
```


**Défense en profondeur (un mail malveillant face aux couches)**

```text
Mail → [Filtrage mail] → [Sensibilisation] → [EDR] → [Moindre privilège] → [Segmentation] → [Détection SOC]
        chaque couche peut faillir ; l'attaquant doit TOUTES les franchir
```


**Pyramide de la douleur (valeur de la détection)**

```text
        TTP        ◄── le plus douloureux pour l'attaquant (change ses méthodes)
      Outils
   Artefacts réseau/hôte
      Noms de domaine
        IOC (hash, IP)  ◄── le moins douloureux (changé en un instant)
```


🎯 **À retenir** — Ces schémas condensent les invariants du référentiel : un même principe (injection, défense en profondeur, tiering, cycle d'incident) se décline partout. Les mémoriser, c'est tenir la carte mentale en tête.

---

> **Fin du référentiel.**
>
> Vous disposez désormais d'une cartographie complète et structurée de la cybersécurité : **14 parties, 319 chapitres** (dont 6 cas filés d'investigation), des fondations au raisonnement SOC/IR, reliées par un fil rouge unique et outillées de tableaux de correspondance et de schémas mentaux. L'objectif n'était pas de tout mémoriser, mais d'acquérir la **carte mentale** qui permet de *classer, relier, défendre et répondre* — y compris face à des menaces jamais rencontrées.
>
> Ce document est un **référentiel-pivot** : la colonne vertébrale d'une bibliothèque cyber. Les cours spécialisés (CTI, forensic, AD, cloud, web, malware…) approfondissent ensuite chaque territoire que cette carte permet de situer.
>
> *« Comprendre les familles, c'est comprendre les attaques qu'on n'a jamais vues. »*
