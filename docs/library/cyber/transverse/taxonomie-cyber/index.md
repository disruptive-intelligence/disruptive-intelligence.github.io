---
title: Taxonomie cyber
source: Cyber/Taxonomie_Cyber.md
chapters: 15
---

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

## Sommaire

1. [Référentiel complet de taxonomie cyber — principes, familles d'attaques, défenses et raisonnement SOC/IR](01-referentiel-complet-de-taxonomie-cyber-principes-familles-d.md)
2. [Partie 1 — Fondations de la cybersécurité](02-partie-1-fondations-de-la-cybersecurite.md)
3. [Partie 2 — Grands principes défensifs](03-partie-2-grands-principes-defensifs.md)
4. [Partie 3 — Gouvernance, risque et conformité (GRC)](04-partie-3-gouvernance-risque-et-conformite-grc.md)
5. [Partie 4 — Taxonomie des surfaces d'attaque](05-partie-4-taxonomie-des-surfaces-d-attaque.md)
6. [Partie 5 — Taxonomie des vulnérabilités](06-partie-5-taxonomie-des-vulnerabilites.md)
7. [Partie 6 — Attaques web et applicatives](07-partie-6-attaques-web-et-applicatives.md)
8. [Partie 7 — Attaques réseau et infrastructure](08-partie-7-attaques-reseau-et-infrastructure.md)
9. [Partie 8 — Identité, Active Directory et privilèges](09-partie-8-identite-active-directory-et-privileges.md)
10. [Partie 9 — Malware, phishing et attaques client-side](10-partie-9-malware-phishing-et-attaques-client-side.md)
11. [Partie 10 — Cloud, API, conteneurs et supply chain](11-partie-10-cloud-api-conteneurs-et-supply-chain.md)
12. [Partie 11 — Détection, SOC et réponse à incident](12-partie-11-detection-soc-et-reponse-a-incident.md)
13. [Partie 12 — Taxonomie des défenses](13-partie-12-taxonomie-des-defenses.md)
14. [Partie 13 — Synthèse transversale](14-partie-13-synthese-transversale.md)
15. [Partie 14 — Cas filés d'investigation SOC/IR (V2)](15-partie-14-cas-files-d-investigation-soc-ir-v2.md)
