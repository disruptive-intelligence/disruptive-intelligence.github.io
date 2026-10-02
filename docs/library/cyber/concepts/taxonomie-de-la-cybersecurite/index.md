---
title: Taxonomie de la cybersécurité
source: Cyber/11 Concepts/Cartes & familles/Taxonomie de la cybersécurité.md
format: cours
revue: '2026-06-10'
---

## Référentiel complet de taxonomie cyber — principes, familles d'attaques, défenses et raisonnement SOC/IR (index)

**Référentiel de référence — Principes, attaques, défenses et réponse à incident**

Un référentiel-pivot de culture cyber large : non pas un catalogue d'attaques isolées, mais une **carte mentale** complète permettant de *comprendre, classer, relier, défendre et répondre*. 14 parties, 319 chapitres, 9 annexes (dont une partie de cas filés d'investigation et des tableaux de correspondance utilisables comme fiches réflexes).

> **Nature de ce document.** C'est un *référentiel structurant* (une taxonomie), exhaustif **en largeur**. Il donne la carte du territoire et le raisonnement ; les cours spécialisés de la bibliothèque approfondissent ensuite chaque domaine (CTI, forensic, AD, cloud, web, malware…). Sa force est de *ranger, relier et raisonner*, pas de tout détailler en profondeur opérationnelle.

> **Fil rouge du cours :** `actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation`

> **Posture :** légal, défensif, pédagogique. Mécanismes, impacts, signaux de détection et défenses — sans payload offensif ni procédure d'exploitation.

---

### Les 8 volumes

**Volume 1 — Fondations, principes défensifs, GRC** *(`cours_cyber_vol1_fondations.md`)*
Introduction · Partie 1 (fondations : actif, menace, vulnérabilité, risque, CIA, AAA, surfaces, contrôles) · Partie 2 (principes : défense en profondeur, moindre privilège, Zero Trust, assume breach, tiering, hardening, secure by design, threat modeling, sauvegarde) · Partie 3 (GRC : PSSI, analyse de risque, homologation, gestion des vulnérabilités/actifs, classification, audit, sensibilisation, supply chain, crise). Chapitres 1–39.

**Volume 2 — Surfaces d'attaque & vulnérabilités** *(`cours_cyber_vol2_surfaces_vulnerabilites.md`)*
Partie 4 (22 surfaces : poste, serveur, réseau, AD/IAM, web, API, cloud, conteneurs, CI/CD, messagerie, navigateur, mobile, IoT, OT/ICS, Wi-Fi, VPN, SaaS, identité, données, humain, physique, firmware) · Partie 5 (20 familles de vulnérabilités, vocabulaire CWE). Chapitres 40–81.

**Volume 3 — Attaques web et applicatives** *(`cours_cyber_vol3_attaques_web.md`)*
Partie 6 : Broken Access Control, IDOR/BOLA, élévation de privilèges, famille XSS complète, famille SQLi complète, command/LDAP/XPath injection, SSTI, XXE, SSRF (+blind/métadonnées), file inclusion (LFI/RFI/traversal), upload, Zip Slip, désérialisation, CSRF, clickjacking, CORS, open redirect, host header, request smuggling, cache poisoning, web cache deception, prototype pollution, rate limit bypass, business logic, GraphQL. Chapitres 82–126.

**Volume 4 — Réseau et infrastructure** *(`cours_cyber_vol4_reseau_infra.md`)*
Partie 7 : reconnaissance/scan, énumération, sniffing, spoofing (ARP/DNS/DHCP), DNS tunneling, MITM, replay, downgrade, exploitation de services, SMB/RDP/VPN, pivoting, tunneling, lateral movement, DoS/DDoS, reflection/amplification, botnet, VLAN hopping, Wi-Fi evil twin, rogue AP, deauth, BGP hijacking. Chapitres 127–154.

**Volume 5 — Identité, Active Directory et privilèges** *(`cours_cyber_vol5_identite_ad.md`)*
Partie 8 : identité-périmètre, structure AD, Kerberos/NTLM/LDAP, comptes, tiering, Kerberoasting, AS-REP roasting, spraying/brute force/stuffing, pass-the-hash/ticket, overpass-the-hash, golden/silver ticket, DCSync/DCShadow, abus de délégation/RBCD, GPO/ACL abuse, shadow credentials, AD CS abuse, credential dumping, lateral movement Windows, PAM/bastion. Chapitres 155–183.

**Volume 6 — Malware, phishing et client-side** *(`cours_cyber_vol6_malware_phishing.md`)*
Partie 9 : classification des malwares (virus, ver, trojan, ransomware, wiper, spyware, infostealer, RAT, backdoor, loader/dropper/downloader, rootkit/bootkit, fileless, macro, LotL/LOLBins) ; ingénierie sociale (phishing, spear/whaling, smishing, vishing, quishing, BEC, malspam, drive-by, malvertising, SEO poisoning, watering hole, MFA fatigue, consent phishing). Chapitres 184–217.

**Volume 7 — Cloud, API, conteneurs et supply chain** *(`cours_cyber_vol7_cloud_api_supplychain.md`)*
Partie 10 : principes cloud/responsabilité partagée, IAM cloud, buckets/secrets/clés, métadonnées, élévation/lateral movement cloud, API (BOLA/BFLA/exposition/consommation), Kubernetes RBAC, container escape, images/registres, CI/CD, pipeline poisoning, dependency confusion, typosquatting, paquets/build compromis, signature/intégrité, SBOM, secrets management. Chapitres 218–244.

**Volume 8 — SOC/réponse, défenses, synthèse + annexes** *(`cours_cyber_vol8_soc_defenses_synthese.md`)*
Partie 11 (détection/SOC/IR : événement→alerte→incident, IOC/IOA/TTP, SIEM/EDR/NDR/SOAR, triage→qualification→escalade→investigation→confinement→éradication→rétablissement→REX, forensic, timeline, crise, PRA/PCA) · Partie 12 (taxonomie des défenses, reliées aux attaques) · Partie 13 (synthèse : classer/relier/prioriser, carte mentale, erreurs de raisonnement) · **Partie 14 (V2 — cas filés d'investigation SOC/IR : phishing, Kerberoasting, malware poste, exfiltration cloud, ransomware, SSRF métadonnées)** · Annexes A–J (glossaire, tableau de correspondance central multi-colonnes, tableaux surface/cadres, fiches réflexes, mini-cas, métiers, apprentissage légal, bibliographie, schémas ASCII). Chapitres 245–319.

> **Note V2.** Cette édition ajoute, suite à relecture : une **Partie 14** de six cas filés d'investigation (du signal brut au REX) pour passer de « je connais les mots » à « je sais raisonner sur un incident » ; un **grand tableau de correspondance multi-colonnes** (Annexe B) attaque → famille → vulnérabilité-racine → surface → impact CIA → logs utiles → défenses, utilisable comme fiche réflexe ; et des **schémas mentaux ASCII** (Annexe J).

---

### Cadres de référence mobilisés

NIST CSF 2.0 · MITRE ATT&CK · MITRE D3FEND · MITRE CAPEC · CWE · OWASP Top 10 · OWASP API Security Top 10 · OWASP ASVS · SLSA/SBOM · ISO 27001/27005 · EBIOS RM · CIS · KEV (CISA).

### Comment utiliser ce cours

1. **Lecture linéaire** (volumes 1→8) pour construire la carte mentale.
2. **Lecture par besoin** : consulter une surface (vol. 2), une famille d'attaque (vol. 3–10), ou une défense (vol. 8) à la demande.
3. **Référence rapide** : annexes du volume 8 (glossaire, tableaux, fiches réflexes).
4. **Méthode de raisonnement** : appliquer les chapitres 306–310 face à toute situation nouvelle.


---

## Référentiel complet de taxonomie cyber — principes, familles d'attaques, défenses et raisonnement SOC/IR

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

## Sommaire

- [Partie 1 — Fondations de la cybersécurité](01-partie-1-fondations-de-la-cybersecurite.md)
- [Partie 2 — Grands principes défensifs](02-partie-2-grands-principes-defensifs.md)
- [Partie 3 — Gouvernance, risque et conformité (GRC)](03-partie-3-gouvernance-risque-et-conformite-grc.md)
- [Partie 4 — Taxonomie des surfaces d'attaque](04-partie-4-taxonomie-des-surfaces-d-attaque.md)
- [Partie 5 — Taxonomie des vulnérabilités](05-partie-5-taxonomie-des-vulnerabilites.md)
- [Partie 6 — Attaques web et applicatives](06-partie-6-attaques-web-et-applicatives.md)
- [Partie 7 — Attaques réseau et infrastructure](07-partie-7-attaques-reseau-et-infrastructure.md)
- [Partie 8 — Identité, Active Directory et privilèges](08-partie-8-identite-active-directory-et-privileges.md)
- [Partie 9 — Malware, phishing et attaques client-side](09-partie-9-malware-phishing-et-attaques-client-side.md)
- [Partie 10 — Cloud, API, conteneurs et supply chain](10-partie-10-cloud-api-conteneurs-et-supply-chain.md)
- [Partie 11 — Détection, SOC et réponse à incident](11-partie-11-detection-soc-et-reponse-a-incident.md)
- [Partie 12 — Taxonomie des défenses](12-partie-12-taxonomie-des-defenses.md)
- [Partie 13 — Synthèse transversale](13-partie-13-synthese-transversale.md)
- [Partie 14 — Cas filés d'investigation SOC/IR (V2)](14-partie-14-cas-files-d-investigation-soc-ir-v2/index.md)
    - [Chapitre 314 — Cas 1 : Phishing avec vol d'identifiants](14-partie-14-cas-files-d-investigation-soc-ir-v2/01-chapitre-314-cas-1-phishing-avec-vol-d-identifiant.md)
    - [Chapitre 315 — Cas 2 : Suspicion de Kerberoasting](14-partie-14-cas-files-d-investigation-soc-ir-v2/02-chapitre-315-cas-2-suspicion-de-kerberoasting.md)
    - [Chapitre 316 — Cas 3 : Malware sur un poste de travail](14-partie-14-cas-files-d-investigation-soc-ir-v2/03-chapitre-316-cas-3-malware-sur-un-poste-de-travail.md)
    - [Chapitre 317 — Cas 4 : Exfiltration depuis le cloud](14-partie-14-cas-files-d-investigation-soc-ir-v2/04-chapitre-317-cas-4-exfiltration-depuis-le-cloud.md)
    - [Chapitre 318 — Cas 5 : Ransomware](14-partie-14-cas-files-d-investigation-soc-ir-v2/05-chapitre-318-cas-5-ransomware.md)
    - [Chapitre 319 — Cas 6 : SSRF vers les métadonnées cloud](14-partie-14-cas-files-d-investigation-soc-ir-v2/06-chapitre-319-cas-6-ssrf-vers-les-metadonnees-cloud.md)
- [Annexes](15-annexes.md)
