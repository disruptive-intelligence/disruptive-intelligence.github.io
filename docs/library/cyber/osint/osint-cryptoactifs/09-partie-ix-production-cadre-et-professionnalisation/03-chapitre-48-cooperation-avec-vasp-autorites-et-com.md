---
title: Chapitre 48 — Coopération avec VASP, autorités et compliance
source: Cyber/02_OSINT/OSINT_Crypto_vFULL.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IX — Production, cadre ET professionnalisation
  - index.md
---

L’enquête OSINT crypto produit son maximum de valeur **en coopération** avec autres acteurs. Ce chapitre couvre le cadre de coopération.

## 48.1 Coopération avec exchanges / VASP

**Pour quoi** :

- Réquisitions KYC sur dépôts identifiés.
- Gel de fonds.
- Information sur patterns / tentatives suspectes.

**Comment** :

- **Via autorités** : exchange ne coopère pas directement avec entité privée pour réquisition KYC. Doit passer par autorité (DGSI, FBI, équivalent juridiction).
- **Via signalement direct** : exchange peut recevoir signalement « possible activité frauduleuse » d’enquêteur privé, qui alimente leur propre AML monitoring.
- **Via partenariats sectoriels** : ISACs financiers, partage de threat intel.

**Délais** :

- Signalement → traitement : variable.
- Réquisition autorité → exchange : jours à semaines selon urgence.
- Gel de fonds : peut être rapide (heures) si coordination fluide.

**Limites** :

- Exchanges non-régulés : peu / pas de coopération.
- Juridictions hostiles : impasse.
- Confidentialité KYC : exchange ne peut pas divulguer KYC à entité privée, seulement à autorités.

## 48.2 Coopération avec émetteurs de stablecoins

**Tether (USDT)** :

- Coopère avec autorités sur réquisition.
- Gels documentés sur centaines de millions USDT cumulés.
- Délais variables.
- Plus réactif depuis 2023.

**Circle (USDC)** :

- Coopère activement.
- Gels rapides (heures-jours).
- Bien intégré aux processus US (OFAC).

**Pour l’enquêteur** : identifier dès qu’un fonds passe en stablecoin = opportunité de gel. Remontée via autorité.

## 48.3 Coopération avec autorités françaises

**TRACFIN** :

- Cellule de renseignement financier.
- Reçoit déclarations de soupçon des assujettis.
- Pour enquêteur privé, contact via mandant assujetti (banque, VASP français).
- Pour enquêteur travaillant avec entreprise victime, le mandant peut faire signalement TRACFIN.

**ANSSI** :

- Sécurité des SI.
- Intervient sur OIV et opérateurs de services essentiels.
- Pour ransomware sur OIV, coordination ANSSI obligatoire.

**DGSI** :

- Sécurité intérieure.
- Cyberterrorisme, atteintes à la nation.
- Coordination pour cas sensibles.

**Cybermalveillance.gouv.fr** :

- Service public d’aide aux victimes.
- Signalement individuel.
- Orientation vers services compétents.

**Pharos** :

- Plateforme de signalement de contenus illicites.
- Pour scams crypto repérés.

**Police / Gendarmerie cyber** :

- SDLC (Sous-direction de la lutte contre la cybercriminalité, gendarmerie).
- BL2C / OFCS (police).
- Plaintes formelles.

**Magistrats spécialisés** :

- JIRS / J3 (juridictions interrégionales spécialisées).
- Procureurs cyber.

## 48.4 Coopération internationale

**Europol EC3** :

- European Cybercrime Centre.
- Coordonne enquêtes EU.
- Operations Cronos (LockBit), autres.

**Interpol** :

- Coordination 195 pays.
- Notices rouges (mandats internationaux).
- Cyber Fusion Centre.

**FBI Cyber Division** (US) :

- Très actif sur ransomware et crypto crime.
- IC3 pour signalement individuel.

**NCA (UK)** :

- National Crime Agency.
- Cyber unit active.

**BKA (Allemagne)** :

- Bundeskriminalamt.
- Coopération étroite avec partenaires.

**FIOD (Pays-Bas)** :

- Service fiscal-pénal.
- Investigations Tornado Cash, autres.

**Autres** :

- Centres cyber au Japon, Corée du Sud, Singapour, Australie, Canada, Israël.
- Coopération variable selon dossiers et juridictions.

## 48.5 OFAC et sanctions

**OFAC** : Office of Foreign Assets Control, US Treasury.

- Maintient SDN list.
- Sanctionne entités, individus, et **adresses crypto** (depuis ~2018, plus actif depuis 2022).
- Interaction avec sanctioned = violation pour US persons et entités sous juridiction US.

**Pour enquêteur** :

- Cross-check systématique des adresses sur SDN list.
- Identifier flux vers ou depuis adresses sanctionnées = drapeau majeur.
- Informer autorités si enquête révèle interaction sanctioned.

**Sanctions UE** :

- Liste des sanctions financières UE.
- Coordination avec OFAC mais avec divergences.
- Implications pour entités EU.

**Sanctions UK, autres juridictions** : régimes spécifiques.

## 48.6 Cadre juridique français

**Article 40 CPP** : tout fonctionnaire ayant connaissance d’un crime ou délit doit le signaler au procureur. S’applique aux analystes en services publics.

**Pour enquêteurs privés** :

- **Pas d’obligation article 40**.
- Mais souvent : si découverte d’infraction grave dans le cadre de l’enquête, signalement opportun.
- Discussion avec mandant et juridique.

**RGPD** :

- Données personnelles (incluant celles de tiers identifiés dans l’enquête) doivent être traitées conformément.
- Bases légales : intérêt légitime, mission d’intérêt public (selon contexte), consentement.

**Secret professionnel** :

- L’enquêteur respecte la confidentialité du mandat.
- Sauf obligations légales contraires.

**Secret bancaire / secret des télécommunications** : limites externes au mandat OSINT.

## 48.7 ISAC et partage sectoriel

**ISAC** (Information Sharing and Analysis Centers) :

- Communautés sectorielles de partage de threat intel.
- FS-ISAC (financial sectors), H-ISAC (health), autres.
- Partage anonymisé selon TLP.

**Pour crypto-forensique** :

- **SEAL ISAC** : Security and Enforcement Analytics Lab, focus crypto.
- **Crypto ISAC** : initiative dédiée.
- **CTI-League** : volontariat communauté CTI.

**Bénéfices** :

- Patterns émergents partagés.
- Wallets / adresses connues distribuées.
- Coordination réponse à campagnes.

**Pour analyste / cabinet** : participation à ISAC pertinent enrichit base de connaissance et contribue à l’écosystème.

## 48.8 Limites de la coopération

**Lenteur** : procédures internationales prennent mois / années.

**Variability** : coopération fluide avec certaines juridictions, opaque avec d’autres.

**Scoping** : autorités ont priorités. Petits dossiers peuvent être négligés.

**Confidentialité** : informations transmises peuvent être moins suivies que désiré.

**Politique** : enjeux géopolitiques peuvent ralentir / dévier coopération.

## 48.9 Construire des relations

**Pour cabinet ou analyste** :

- Présence à conférences (FIRST, Cybersec Forum Europe, FIC, etc.).
- Participation à ISACs.
- Contributions publiques (blog, talks).
- Coopération sur dossiers concrets renforce confiance.

**Avec le temps** :

- Réseau de pairs construit.
- Contacts directs aux autorités (avec confiance).
- Partage facilité.

C’est un investissement sur années, mais structurant pour efficacité.

-----
