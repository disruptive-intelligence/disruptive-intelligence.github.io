---
title: Partie III — Chine
source: Cyber/01_CTI/APT_Synthese.md
note: APT — synthèse
up:
- - APT — synthèse
  - index.md
---

*La Chine est l'acteur étatique le plus prolifique en volume d'espionnage et le plus stratégique dans son ciblage — avec une réorganisation majeure post-2015 qui a significativement augmenté sa sophistication.*

---


## Chapitre 8 — Chine : contexte, doctrine et appareil cyber

### 8.1 Priorités géopolitiques

Le cyber est un instrument de la stratégie de puissance globale chinoise. Les priorités : rattrapage technologique (Made in China 2025 — atteindre l'autosuffisance dans les technologies clés : semi-conducteurs, IA, aérospatiale, biotechnologie), unification (Taïwan — le scénario géopolitique le plus déterminant pour les cyberopérations chinoises), contrôle interne (surveillance des dissidents, du Tibet, du Xinjiang, de Hong Kong), puissance régionale Indo-Pacifique (projection de puissance en mer de Chine, Routes de la Soie), et accumulation de données (collecte massive via le cyber-espionnage, les JV, et les programmes académiques).

### 8.2 Structure

Le **MSS** (Ministère de la Sécurité d'État) est le service de renseignement civil — espionnage économique et technologique, avec des bureaux régionaux (le MSS Hainan est derrière APT40). Le **PLA** (Armée populaire de libération) a historiquement conduit le cyber-espionnage (Unit 61398 / APT1 exposé par Mandiant en 2013) mais a été réorganisé après 2015 (PLA Strategic Support Force — SSF). Les **contractors** et universités mandatés par le MSS ou le PLA conduisent des opérations pour le compte de l'État (le modèle chinois brouille la frontière public/privé).

La **réorganisation post-2015** est un tournant : après l'exposition publique d'APT1 (2013) et l'accord Obama-Xi de 2015 (engagement à ne plus mener d'espionnage économique — largement violé), la Chine a transféré la majorité des opérations du PLA vers le MSS, avec une montée en sophistication significative (meilleur OPSEC, tradecraft plus furtif, exploitation d'appliances edge plutôt que phishing basique).

---


## Chapitre 9 — Chine : les groupes APT en détail

**APT41 / Wicked Panda / Brass Typhoon (MSS)** — le groupe à double casquette : espionnage étatique (ciblage tech, santé, télécoms) + cybercrime personnel (gaming, ransomware). Les deux activités utilisent les mêmes outils et la même infrastructure. Indictments DOJ en 2020. TTP : supply chain (CCleaner), exploitation de vulnérabilités web, rootkits, backdoors sophistiquées.

**APT40 / Gingham Typhoon (MSS Hainan)** — espionnage maritime, défense, aérospatial, Asie-Pacifique. TTP signature : exploitation systématique et rapide des vulnérabilités sur les appliances réseau (VPN, firewalls) — souvent dans les 48h suivant la publication d'un advisory. Ciblage cohérent avec les intérêts maritimes chinois en mer de Chine.

**Volt Typhoon (PRC state-sponsored)** — le cas le plus inquiétant. Pré-positionnement dans les infrastructures critiques américaines (télécoms, énergie, eau, transport) avec LotL quasi exclusif. Pas d'exfiltration, pas de sabotage — un accès dormant maintenu pendant des mois/années. Signification stratégique : capacité de dissuasion/représailles en cas de conflit autour de Taïwan. Traité en profondeur au Ch.22 et Ch.31.

**Salt Typhoon (PRC state-sponsored)** — compromission d'opérateurs télécoms mondiaux (AT&T, Verizon, d'autres) pour accéder aux systèmes d'interception légale (wiretapping systems). Révélé fin 2024. Impact : accès potentiel aux communications ciblées par les autorités américaines elles-mêmes.

**APT10 / Stone Panda (MSS)** — ciblage des MSP (Managed Service Providers) via l'opération Cloud Hopper, donnant accès aux réseaux de centaines de clients dans des dizaines de pays. Indictments DOJ en 2018.

**APT31 / Zirconium (MSS)** — ciblage gouvernemental large (parlementaires, think tanks, dissidents). Indictments DOJ en 2024 ciblant 7 opérateurs MSS.

Acteurs associés : **Mustang Panda** (ciblage des ONG, think tanks, et gouvernements en Asie du Sud-Est), **Gallium** (télécoms), et le **Winnti umbrella** (écosystème de groupes utilisant des outils partagés, frontière floue entre espionnage étatique et cybercrime).

---


## Chapitre 10 — Chine : campagnes de référence et tendances

**Cloud Hopper (2016-2018)** : APT10 a compromis des MSP pour accéder aux réseaux de leurs clients — des centaines d'entreprises dans des dizaines de pays. L'attribution repose sur la victimologie (les données volées correspondent aux priorités stratégiques chinoises). Leçon : la supply chain de services (MSP, infogérants) est un vecteur de compromission massive.

**Microsoft Exchange / Hafnium (2021)** : exploitation de 4 vulnérabilités zero-day dans Exchange on-premise, touchant ~250 000 serveurs mondialement. L'exploitation a commencé de manière ciblée puis s'est massifiée — transition inhabituelle vers l'exploitation opportuniste.

**Volt Typhoon (2023-présent)** et **Salt Typhoon (2024)** sont traités respectivement au Ch.22/Ch.31 et dans ce chapitre. Salt Typhoon illustre une évolution : cibler non plus les données elles-mêmes mais les systèmes qui les collectent (les systèmes d'interception légale des opérateurs télécom).

**Tendances structurelles chinoises :** exploitation massive des appliances edge (Ivanti, Fortinet, Citrix, Barracuda — souvent dans les heures suivant la publication d'une CVE), LotL systématique (sophistication croissante de l'OPSEC post-réorganisation MSS), pré-positionnement stratégique dans les infras critiques, ciblage de la supply chain logicielle, et volume d'espionnage inchangé malgré les accords diplomatiques.

> **⚡ BLACKOUT — Épisode 4**
>
> L'exploitation Ivanti dans BLACKOUT est un TTP signature chinois (APT40, Volt Typhoon). Le LotL (pas de malware custom identifié, utilisation de certutil, PowerShell, et PsExec) est compatible avec le tradecraft Volt Typhoon. Le pré-positionnement OT sans action est compatible avec le modèle de « capacité dormante ». L'hypothèse chinoise (H2) est posée avec confiance faible à modérée — mais les patterns de beaconing ne correspondent pas aux profils chinois documentés.

---
