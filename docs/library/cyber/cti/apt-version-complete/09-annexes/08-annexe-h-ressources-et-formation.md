---
title: Annexe H — Ressources et formation
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Annexes
  - index.md
---

Cette annexe consolide les ressources essentielles pour un analyste CTI/SOC travaillant sur les APT. Sélection non exhaustive — privilégie les sources de qualité établie.

#### H.1 Rapports annuels et périodiques de référence

**Rapports annuels vendors** (tous gratuits et téléchargeables) :

- **Mandiant M-Trends** : publication annuelle depuis 2011. Synthèse des incidents IR traités par Mandiant, tendances des APT, dwell time moyen. Référence centrale.
- **CrowdStrike Global Threat Report (GTR)** : publication annuelle, synthèse des acteurs et tendances.
- **Microsoft Digital Defense Report (DDR)** : publication annuelle depuis 2020. Volume massif, vision cloud (M365, Azure).
- **Verizon Data Breach Investigations Report (DBIR)** : publication annuelle depuis 2008. Données statistiques sur les breaches, vision plus large que les APT stricts.
- **ENISA Threat Landscape** : publication annuelle ENISA, vision européenne.
- **ANSSI Panorama de la cybermenace** : publication annuelle ANSSI, perspective française.
- **NCSC Annual Review** (UK) : publication annuelle NCSC.
- **CISA Year in Review** : publication annuelle CISA.
- **Kaspersky APT Reports** : rapports trimestriels et ad hoc.
- **ESET Threat Report** : publication biannuelle, forte visibilité Europe centrale/orientale.
- **Europol IOCTA** — Internet Organised Crime Threat Assessment, publication annuelle. Focus cybercrime mais avec zones de chevauchement APT.
- **Recorded Future Annual Report** : publication annuelle.
- **Unit 42 (Palo Alto) Incident Response Report** : publication annuelle, données IR.
- **Chainalysis Crypto Crime Report** : publication annuelle, centrale pour le volet crypto/Lazarus.
- **TRM Labs / Elliptic reports** : publications régulières sur les flux illicites crypto.

**Rapports sectoriels** :

- **Dragos Year in Review** : publication annuelle Dragos, focus OT/ICS.
- **Claroty Biannual ICS Risk & Vulnerability Report**.
- **FS-ISAC** : rapports sectoriels finance.
- **H-ISAC** : rapports sectoriels santé.

**Rapports thématiques majeurs** :

- **Pegasus Project** (2021) — Forbidden Stories + 17 médias — usage NSO Pegasus.
- **Leak i-Soon analyses** (2024) — multiple vendors (SentinelOne, Sekoia, Harfang Lab).
- **ContiLeaks analyses** (2022) — multiples chercheurs indépendants.
- **Citizen Lab reports** — University of Toronto — référence internationale sur spywares et surveillance.

#### H.2 Formations certifiantes

**SANS Institute** (gold standard) :

- **FOR578 — Cyber Threat Intelligence** : formation de référence CTI. Enseignants majeurs du domaine (Rebekah Brown, Scott Roberts, Ryan Fetterman). Certification **GCTI**.
- **FOR508 — Advanced Incident Response, Threat Hunting, and Digital Forensics**. Certification **GCFA**.
- **FOR572 — Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response**. Certification **GNFA**.
- **ICS515 — ICS Active Defense and Incident Response** : formation phare OT. Enseignants Dragos (Robert M. Lee). Certification **GRID**.
- **ICS456 — Essentials for NERC Critical Infrastructure Protection** : focus réglementaire NERC CIP (US électricité).
- **FOR528 — Ransomware and Cyber Extortion for Incident Responders**.
- **FOR608 — Enterprise-Class Incident Response & Threat Hunting**.
- **SEC599 — Defeating Advanced Adversaries**.
- **SEC504 — Hacker Tools, Techniques, and Incident Handling**.

**Offensive Security** :

- **OSCP** (Offensive Security Certified Professional) : certification offensive de référence, base du pentest.
- **OSEP** (Offensive Security Experienced Penetration Tester) : niveau plus avancé.
- **OSED** (Offensive Security Exploit Developer).

**EC-Council** :

- **CEH** (Certified Ethical Hacker) — largement reconnu mais considéré comme moins rigoureux que OSCP par les praticiens.
- **CTIA** (Certified Threat Intelligence Analyst).
- **CHFI** (Computer Hacking Forensic Investigator).

**ISC2** :

- **CISSP** (Certified Information Systems Security Professional) — management sécurité.
- **CCSP** (Certified Cloud Security Professional).
- **CCFP** (Certified Cyber Forensics Professional).

**ISACA** :

- **CISM** (Certified Information Security Manager) — management.
- **CISA** (Certified Information Systems Auditor) — audit.
- **CRISC** (Certified in Risk and Information Systems Control).

**Mandiant Academy** : formations spécifiques (CTI, IR, malware analysis).

**CrowdStrike University** : formations internes et ouvertes.

**SECO Institute** (Europe) : certifications cybersécurité européennes.

**Formations françaises** :

- **CNAM** : master cybersécurité.
- **Télécom Paris / Télécom SudParis / INSA** : masters spécialisés.
- **Centrale-Supélec** : formation continue et formations initiales.
- **ESIEA, EPITA, EPITECH** : formations ingénieur avec spécialisations cyber.
- **EC-Conseil** : formations ANSSI orientées.

#### H.3 Bases de données et plateformes techniques

**MITRE — référence absolue** :

- **MITRE ATT&CK** : attack.mitre.org — framework TTP. Sections Enterprise, Mobile, ICS (OT).
- **MITRE ATT&CK Groups** : attack.mitre.org/groups/ — page par groupe avec TTP associées et alias.
- **MITRE CTI GitHub** : github.com/mitre/cti — export STIX des données ATT&CK.
- **MITRE D3FEND** : d3fend.mitre.org — contre-framework défensif aligné sur ATT&CK.
- **MITRE Engage** : cadre pour deception.
- **MITRE Shield** (remplacé par Engage) : cadre historique de defensive cyber operations.
- **CTI Blueprints** : github.com/center-for-threat-informed-defense — méthodologies.

**Malware et samples** :

- **Malpedia** : malpedia.caad.fkie.fraunhofer.de — base consolidée par Fraunhofer FKIE, mapping famille/acteur.
- **VirusTotal** : virustotal.com — Google. Intelligence sur fichiers, URLs, domaines, IPs.
- **Hybrid Analysis** : hybrid-analysis.com — sandboxing public.
- **Any.run** : any.run — sandboxing interactif.
- **Joe Sandbox** : joesandbox.com — analyse dynamique.
- **Triage** : tria.ge — Hatching (Recorded Future).
- **VX-Underground** : vx-underground.org — archives malware historiques.

**Intelligence / reconnaissance** :

- **Shodan** : shodan.io — recherche appliances exposées Internet.
- **Censys** : censys.io — concurrent de Shodan.
- **ZoomEye** : zoomeye.org — équivalent chinois.
- **FOFA, Quake** : équivalents chinois.
- **GreyNoise** : greynoise.io — caractérisation du bruit Internet vs activité ciblée.
- **AlienVault OTX** : otx.alienvault.com — partage communautaire.
- **URLhaus** : urlhaus.abuse.ch — URLs malveillantes.
- **ThreatFox** : threatfox.abuse.ch — IoC partagés.
- **Feodo Tracker** : feodotracker.abuse.ch — botnets bancaires.
- **URLScan** : urlscan.io — scan URLs.

**Threat intelligence platforms** :

- **MISP** : misp-project.org — open source, standard de partage.
- **OpenCTI** : github.com/OpenCTI-Platform — open source.
- **Anomali ThreatStream**, **ThreatConnect**, **EclecticIQ**, **Recorded Future** : commerciaux.

**Vulnerability intelligence** :

- **CISA KEV** : cisa.gov/known-exploited-vulnerabilities-catalog.
- **NVD** : nvd.nist.gov — National Vulnerability Database US.
- **MITRE CVE** : cve.mitre.org.
- **First EPSS** : first.org/epss — scoring prédictif d’exploitation.
- **Patch Tuesday trackers** (divers) : consolidation des patches Microsoft.

#### H.4 Blogs, newsletters, podcasts

**Blogs vendors CTI** (publications techniques de haute qualité) :

- **Mandiant blog** : cloud.google.com/security/resources/threat-intelligence.
- **CrowdStrike blog** : crowdstrike.com/blog.
- **Microsoft Threat Intelligence blog** : microsoft.com/security/blog.
- **Kaspersky Securelist** : securelist.com.
- **ESET WeLiveSecurity** : welivesecurity.com.
- **Unit 42 (Palo Alto)** : unit42.paloaltonetworks.com.
- **Trend Micro Research** : trendmicro.com/research.
- **Proofpoint Threat Insight** : proofpoint.com/us/blog.
- **Check Point Research** : research.checkpoint.com.
- **Sekoia blog** : blog.sekoia.io.
- **Harfang Lab blog** : harfanglab.io/insidethelab.
- **Dragos blog** : dragos.com/blog (OT/ICS).
- **Claroty Team82** : claroty.com/team82/research (OT).
- **Recorded Future Insikt Group** : recordedfuture.com/research.

**Blogs indépendants et communautaires** :

- **The DFIR Report** : thedfirreport.com — analyses d’intrusions détaillées, gratuit et de qualité exceptionnelle.
- **Krebs on Security** : krebsonsecurity.com — Brian Krebs, journalisme cyber.
- **SANS ISC (Internet Storm Center)** : isc.sans.edu — diary quotidien.
- **Bleeping Computer** : bleepingcomputer.com — actualité cyber accessible.
- **The Record** (Recorded Future) : therecord.media.
- **CyberScoop** : cyberscoop.com.
- **Ars Technica — Security** : arstechnica.com/information-technology.
- **The Hacker News** : thehackernews.com.

**Blogs techniques profonds** :

- **Harel Fortinet** / **Securelist** : analyses malware approfondies.
- **Didier Stevens** : didierstevens.com — outils et analyses malware.
- **Objective-See** (Patrick Wardle) : objective-see.org — sécurité macOS.
- **SpecterOps** : posts.specterops.io — red team/AD.
- **Google Project Zero** : googleprojectzero.blogspot.com — recherche vulnérabilités.

**Citizen Lab** : citizenlab.ca — référence sur spywares, surveillance, droits humains numériques.

**Newsletters** :

- **Risky.Biz** (Patrick Gray) : riskybiz.media — podcast et newsletter, référence industrie.
- **The CyberWire** : thecyberwire.com — newsletter quotidienne.
- **This Week in Security** : Matt Tait (@pwnallthethings).
- **TLDR Sec** (Clint Gibler) : tldrsec.com.
- **Return on Security** (Mike Privette) : returnonsecurity.com.

**Podcasts** :

- **Risky.Biz** — Patrick Gray.
- **Darknet Diaries** (Jack Rhysider) : darknetdiaries.com — histoires cyber racontées.
- **SANS Internet Stormcast**.
- **Cyber Weekly**.
- **Hacking Humans** (CyberWire).
- **NoLimitSecu** (français).
- **Le Comptoir Sécu** (français).

#### H.5 Conférences et événements

**Internationales** :

- **Black Hat USA** (Las Vegas, août) — conférence industrielle majeure, briefings techniques.
- **DEF CON** (Las Vegas, août) — conférence hacker historique.
- **RSA Conference** (San Francisco, avril-mai) — plus grande conférence cyber mondiale.
- **Black Hat Europe** (Londres, décembre).
- **Black Hat Asia** (Singapour).
- **FIRST Annual Conference** : conférence du Forum of Incident Response and Security Teams.
- **Virus Bulletin (VB)** : conférence AV/CTI.
- **CyCon** : conférence CCDCOE OTAN, Tallinn. Focus cyber et droit international.
- **REcon** (Montréal) : reverse engineering.
- **ShmooCon** (Washington).
- **Kaspersky SAS (Security Analyst Summit)** : conférence CTI annuelle.

**Européennes / francophones** :

- **SSTIC** (Rennes, juin) : Symposium sur la sécurité des technologies de l’information et des communications. Conférence francophone de référence.
- **FIC** (Lille, puis Marseille, janvier) : Forum International de la Cybersécurité. Dimension institutionnelle forte.
- **Botconf** (Strasbourg/autres, annuel) : focus botnets et malware.
- **NoLimitSecu Days**.
- **ECRIME** (Amsterdam).
- **Troopers** (Heidelberg, Allemagne).
- **hack.lu** (Luxembourg).
- **NDSS** (Network and Distributed System Security) : conférence académique USENIX.
- **USENIX Security** : conférence académique.
- **Hardwear.io** (La Haye) : hardware security.

**Conférences OT spécialisées** :

- **S4** (Miami, janvier) : conférence OT sécurité la plus prestigieuse.
- **SANS ICS Summit** (Orlando).
- **Dragos ICS Cybersecurity Conference**.

**Conférences étatiques / agences** :

- **CSS** (Cyber Security Summit) : événements ANSSI.
- **NCSC One** (UK).
- **RSA Conference Government Track** (US).

#### H.6 OSINT sur APT — sources à cultiver

**Comptes Twitter/X / Mastodon à suivre** (sélection) :

Vendors et chercheurs réputés :

- @TrailofBits, @juanandres_gs, @cyb3rops (Florian Roth), @malwrhunterteam, @vxunderground, @MalwareTechBlog, @bryankb, @wdormann, @gossithedog, @taosecurity (Richard Bejtlich), @jeffreycarr, @MalwareJake, @2sec4u.

Agences et officiels :

- @CISAgov, @NCSC, @ANSSI_FR, @BSI_Bund, @ENISA_EU, @FBI_CYBER, @ODNIgov, @CERT_UA, @WarOnTheRocks.

Journalistes :

- @briankrebs, @lorenzofb, @binaryflash (Kim Zetter), @patrickwardle, @bing_chris, @josephmenn.

Acteurs spécialisés :

- @DragosInc, @mandiant, @CrowdStrike, @Kaspersky, @ESETresearch, @Unit42_Intel, @MsftSecIntel, @citizenlab, @Telecomix, @Recorded_Future.

**Listes et agrégateurs** :

- **Twitter/X lists** sur CTI, APT, threat intelligence par des curateurs reconnus.
- **Mastodon instances** : infosec.exchange (plus focus technique), social.cyber.gay.
- **LinkedIn** : pour les publications plus institutionnelles et les annonces corporatives.

**Plateformes de partage structuré** :

- **CTI league** (formée en 2020) : volontaires COVID, a montré la puissance du partage.
- **InfoSec Handlers Diary** (SANS ISC).
- **Exploit-db.com** : exploits publiés.
- **0day.today** : marketplace (usage à considérer avec prudence).

**Rapports gouvernementaux publics** :

- **US CISA advisories** : cisa.gov/news-events/cybersecurity-advisories.
- **NSA Cybersecurity Advisories** : nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance.
- **UK NCSC advisories** : ncsc.gov.uk/section/advice-guidance/all-topics.
- **CERT-FR** : cert.ssi.gouv.fr.
- **BSI** : bsi.bund.de.
- **CCCS Canada** : cyber.gc.ca.
- **ACSC Australia** : cyber.gov.au.

**Ressources académiques** :

- **arXiv cs.CR** : publications académiques en sécurité.
- **Citizen Lab publications** : citizenlab.ca/category/research/.
- **Atlantic Council Cyber Statecraft Initiative**.
- **CSIS Cyber Policy** : csis.org/programs/strategic-technologies-program.
- **RAND Cyber Policy** : rand.org.

#### H.7 Livres de référence

**Cyber géopolitique et acteurs** :

- *Sandworm* — Andy Greenberg. Référence sur Sandworm/GRU, NotPetya, Ukraine.
- *Dark Territory: The Secret History of Cyber War* — Fred Kaplan.
- *Confront and Conceal* — David Sanger. Stuxnet et Iran.
- *The Perfect Weapon* — David Sanger.
- *This Is How They Tell Me the World Ends* — Nicole Perlroth. Marché 0-day.
- *Countdown to Zero Day* — Kim Zetter. Stuxnet.
- *Cult of the Dead Cow* — Joseph Menn. Histoire du hacking et des enjeux politiques.
- *Active Measures* — Thomas Rid. Histoire de la désinformation.

**CTI et analyse** :

- *Intelligence-Driven Incident Response* — Scott Roberts & Rebekah Brown.
- *The Cuckoo’s Egg* — Cliff Stoll. Premier cas d’APT documenté (1989), encore pertinent.
- *Practical Threat Intelligence and Data-Driven Threat Hunting* — Valentina Palacín.
- *Threat Intelligence and Me* — Robert M. Lee (accessible).
- *The Threat Intelligence Handbook* — Recorded Future.

**Analyse et méthodes** :

- *Psychology of Intelligence Analysis* — Richards Heuer (CIA, ancien mais classique).
- *Structured Analytic Techniques for Intelligence Analysis* — Richards Heuer & Randolph Pherson.

**Technique** :

- *Practical Malware Analysis* — Michael Sikorski & Andrew Honig.
- *The Practice of Network Security Monitoring* — Richard Bejtlich.
- *Applied Incident Response* — Steve Anson.
- *Blue Team Handbook* — Don Murdoch.
- *Red Team Field Manual* — Ben Clark.

**OT / ICS** :

- *Industrial Cybersecurity* — Pascal Ackerman.
- *Hacking Exposed: Industrial Control Systems* — Clint Bodungen et al.

**Ouvrages français** :

- *La cyberdéfense : politique de l’espace numérique* — Stéphane Taillat, Amaël Cattaruzza, Didier Danet.
- *Cyberattaque et cyberdéfense* — Daniel Ventre.
- *La guerre cognitive* — François-Bernard Huyghe.

-----


## CLÔTURE DU COURS


### Ce que ce cours a cherché à apprendre

Ce cours AU CŒUR DES APT s’est donné pour mission de **faire comprendre les acteurs cyber étatiques** — qui ils sont, comment ils opèrent, quelles sont leurs doctrines, leurs ambitions, leurs contraintes. Cette compréhension n’est pas académique : elle est **opérationnellement indispensable**.

Face à une intrusion sophistiquée, un analyste sans connaissance des acteurs peut détecter une compromission mais ne peut pas l’interpréter correctement. Il manipule des IoC sans comprendre les intentions. Il alerte sans calibrer l’urgence. Il répond sans anticiper les mouvements suivants de l’adversaire.

Un analyste qui connaît les acteurs voit différemment. Un beaconing HTTPS sur un poste OT dans un opérateur énergétique européen, pendant un conflit ukrainien actif, n’est pas un artefact technique isolé — c’est le signal possible d’un pré-positionnement stratégique dont les implications s’étendent de la détection technique à la coordination diplomatique internationale. Le cours a cherché à permettre cette lecture.
