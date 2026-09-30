---
title: Chapitre 40 — Forces de l'ordre, disruption et coopération internationale
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VII — Cas d'usage, tendances et prospective
  - index.md
---

Ce chapitre couvre l'autre face — comment les autorités luttent contre l'écosystème dark web. Comprendre leurs capacités et leur coordination informe à la fois la défense organisationnelle et la prospective.

## 40.1 Les capacités étatiques

**FBI (US)**. Forces de l'ordre fédérales US, capacités cyber considérables. Opérations Bayonet, Cookie Monster, Cronos (lead côté US). Compétences techniques internes + coopération avec NSA pour SIGINT. Mandat large.

**Europol et EC3 (European Cybercrime Centre)**. Coordination des polices européennes, opérations multi-pays. Pas pouvoir de police directe mais coordination, intelligence sharing, soutien technique. Operations notables : Endgame (2024), Pacifier, Cookie Monster (côté EU), multiple ransomware.

**NCA (UK)**. National Crime Agency, lead Operation Cronos. Forte expertise cyber.

**BKA (Allemagne)**. Lead saisie Hydra (avril 2022), nombreuses opérations.

**ANSSI / SDLC / OFAC (France)**. ANSSI : agence cybersécurité, défensif principalement. **Sous-Direction de la Lutte contre la Cybercriminalité** (SDLC, gendarmerie). **OFAC français** (Office Anti-Cybercriminalité créé 2023). DGSI pour contre-espionnage cyber. DGSE pour renseignement extérieur. Coordination multi-agences en France.

**Interpol**. Coordination internationale globale, focal point pour pays moins équipés. Notable Operation Synergia (2024) contre infrastructure phishing.

**National CSIRTs**. CERT-FR (ANSSI), BSI (Allemagne), NCSC (UK), CISA (US), JPCERT (Japon), etc.

**Services de renseignement**. NSA (US), GCHQ (UK), DGSE (France), BND (Allemagne) — capacités SIGINT massives. Application sur dark web : surveillance d'infrastructures, déanonymisation par corrélation de trafic, infiltration par moyens classifiés.

## 40.2 La coopération internationale

**Interpol-Europol Cybercrime Conferences** annuelles. Coordination, partage d'intelligence.

**J-CAT (Joint Cybercrime Action Taskforce)**. Hébergé par Europol, regroupe spécialistes des principaux pays européens + US, UK, Australie, Canada. Coordination opérationnelle.

**Counter Ransomware Initiative (CRI)**. Lancée par US 2021, 60+ pays membres en 2025. Coordination contre ransomware, partage intel, déclarations conjointes anti-paiement.

**Pall Mall Process (2024)**. Régulation des PSO (Private Sector Offensive — NSO, Intellexa, etc.). 40+ États signataires. Cadre non-contraignant mais structurant.

**Convention de Budapest (2001)** + protocole additionnel (2022) sur cybercriminalité. Cadre juridique de coopération.

**Mutual Legal Assistance Treaties (MLATs)**. Bilatéraux. Permettent demandes de preuves entre pays.

**Limites** : la coopération marche avec **pays alignés** (démocraties occidentales, Five Eyes, UE+). Avec Russie, Chine, certaines autres juridictions, coopération minimale ou nulle. C'est la raison structurelle de la persistance de l'écosystème criminel — sanctuaires juridictionnels existent.

## 40.3 Les grandes opérations 2022-2026

**Operation Hydra (avril 2022)**. BKA + FBI. Saisie de Hydra Market (russophone, dominant). 25 M USD saisis en crypto. Fragmentation de l'écosystème russophone qui se poursuit.

**Operation Pacifier (2017+, multi-vagues)**. Suite de Playpen, contre CSAM globalement.

**Operation Lyrebird (2022)**. France+UK contre Glupteba botnet.

**Operation Cookie Monster (avril 2023)**. FBI + Europol + 17 pays. Saisie Genesis Market (marché de logs leader). 120+ arrestations.

**Operation Endgame (mai 2024)**. Europol-led. Démantèlement infrastructures multiples (IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee). 4 M USD saisis. Coordination avec FBI, BSI, Eurojust.

**Operation Cronos (février 2024)**. NCA, FBI, Europol, 10+ pays. LockBit. Infrastructure saisie, identification Khoroshev (LockBitSupp), publication clés de déchiffrement, sanctions.

**Operation Magnus (octobre 2024)**. Saisie d'infrastructure RedLine et MetaStealer (deux infostealers majeurs). Coordination globale.

**Operation Kaerb (septembre 2024)**. Démantèlement plateforme phishing iServer. Argentine + 10 pays.

**Kidflix (mars 2025)**. Plateforme CSAM, coordination internationale, arrestations.

**Saisies BreachForums multiples** (mars 2023, juillet 2024, autres). Pompompurin arrêté, Baphomet arrêté ensuite, ShinyHunters reprend opération, nouvelles actions.

**Pavel Durov (août 2024)**. Arrestation en France. Inculpation pour complicité dans diffusion de contenus illicites via Telegram. Impact massif sur Telegram (durcissement modération, coopération accrue avec autorités). Procédure ouverte, en cours.

## 40.4 Les techniques d'opération law enforcement

**Investigation prolongée**. Les grandes opérations sont préparées sur **mois ou années**. Operation Cronos a été préparée depuis 2022. Bayonet mois de préparation.

**Coopération multi-agences**. FBI + Europol + NCA + 10+ pays. Coordination juridique complexe, harmonisation des actions.

**Coordination temporelle**. Saisies simultanées dans multiples pays pour empêcher fuite. Précis à la minute parfois.

**Opérations de takeover** (modèle Hansa). Prise de contrôle de l'infrastructure criminelle, opération sous contrôle pendant période, puis annonce. Objectif : maximiser collecte de données utilisateurs, pas seulement saisir.

**Saisies de cryptoactifs**. Coordination avec exchanges, gel de fonds, identification d'opérateurs via flux. FBI a récupéré centaines de millions USD cumulés.

**Communication post-opération**. Stratégique. Les autorités publient parfois avec mise en scène (LockBit a vu son leak site « hijacké » avec messages NCA/FBI), parfois avec discrétion. Objectif : maximiser effet dissuasif tout en protégeant méthodes.

**Coopération avec secteur privé**. Vendors CTI (Mandiant, CrowdStrike, Microsoft, Recorded Future) fournissent intelligence. Exchanges crypto coopèrent. Hébergeurs cooperent (parfois sous contrainte légale).

## 40.5 Les limites et critiques

Malgré succès, limites structurelles.

**Sanctuaires juridictionnels**. Russie, Chine, certains pays — coopération minimale. Acteurs basés là-bas largement intouchables. Tant que le sanctuaire existe, l'écosystème persiste.

**Asymétrie coût-bénéfice**. Une opération comme Cronos mobilise des ressources énormes, pour un impact temporaire. LockBit reconstitue partiellement, affiliés migrent. Le ROI policier est questionné.

**Ressources limitées**. Le volume du cybercrime explose, les moyens policiers grandissent moins vite. Triage extreme — seules les opérations les plus impactantes sont menées.

**Frontières juridictionnelles**. Un acteur russe attaque une victime française via un serveur néerlandais avec paiement crypto à un wallet panaméen — qui poursuit ?

**Critiques sur méthodes**. Operation Playpen (FBI a opéré CSAM site pendant 2 semaines pour piéger). Multiple cas de NIT contestées. Question : où placer les limites éthiques ?

**Effet temporaire** : disrupter LockBit n'élimine pas le phénomène ransomware. Successeurs émergent.

**Underground innovation** : les acteurs s'adaptent. Plus de OPSEC, plus de fragmentation, plus de chiffrement, plus de cantonnement aux sanctuaires.

## 40.6 La stratégie « pressure permanente »

Plutôt que viser élimination (impossible), la doctrine occidentale émergente est **pressure permanente**.

**Augmentation des coûts opérationnels** : forces les acteurs à investir plus en OPSEC, infrastructure résiliente, fragmentation. Réduit ROI criminel.

**Réduction des espaces sûrs** : sanctions ciblées (Tornado Cash, Garantex, Bitzlato, Suex), coopération sur juridictions précédemment permissives.

**Dissuasion par publicité** : grandes opérations communiquées créent doute chez acteurs, démontrent capacités.

**Fragilisation des chaînes** : taper IAB, RaaS opérateurs, blanchisseurs simultanément. Casse confiance écosystémique.

**Coopération public-privé**. Vendors CTI, exchanges, hébergeurs comme partenaires actifs.

**Efficacité** : pas d'élimination du cybercrime, mais réduction de son taux de croissance, augmentation de sa difficulté opérationnelle, réduction d'impact macro. Mesure ambivalente.

## 40.7 Le rôle du privé

Pour les analystes CTI privés, plusieurs rôles dans l'écosystème law enforcement.

**Partenaires d'intelligence**. Vendors CTI fournissent indicateurs, attribution, contexte. Mandiant, CrowdStrike, Microsoft, Recorded Future, etc. — tous ont des liens fonctionnels avec FBI / NCA / Europol.

**Première ligne de détection**. Beaucoup d'incidents sont d'abord détectés par secteur privé (SOC), puis remontés aux autorités. La rapidité de détection privée conditionne l'impact des opérations publiques.

**Forensics et reconstitution**. Cabinets IR (Mandiant, Kroll, Stroz Friedberg, Wavestone, etc.) reconstituent attaques, alimentent enquêtes, témoignent en justice si besoin.

**Sensibilisation et formation**. Les analystes privés produisent rapports publics qui informent décideurs, journalistes, public. Sensibilisation de masse.

**Coopération sectorielle**. ISAC (FS-ISAC, H-ISAC, E-ISAC, etc.) facilitent partage rapide d'IoC entre pairs sectoriels.

**Limites du rôle privé** : pas de pouvoir coercitif, pas d'accès aux capacités SIGINT, contraintes commerciales (clients, conflits d'intérêt potentiels).

## 40.8 Fil rouge — DARKSTREAM : conclusion law enforcement

> **🌐 DARKSTREAM — Épisode 20 : transmission DGSI**
>
> Le rapport DARKSTREAM final est transmis à la DGSI le 15 mai 2026. La DGSI accuse réception, indique qu'elle exploitera les éléments selon ses canaux propres.
>
> Lucas n'aura pas de retour direct sur les suites — la DGSI ne communique pas sur ses opérations en cours. Cela peut signifier :
> - Investigation interne approfondie sur les acteurs identifiés (aero_source, magnit_ru).
> - Coopération avec partenaires internationaux (FBI, BKA, autres) pour traçage personnel, peut-être identification physique.
> - Inclusion dans intelligence stratégique sur menaces ciblant aerospace européen.
> - Rien — capacité non priorisée face à autres dossiers.
>
> Pour Vectris, l'investigation DARKSTREAM se conclut sur :
> - Confirmation et caractérisation de l'incident.
> - Recommandations défensives détaillées et applicables.
> - Cadre coopératif avec autorités établi.
> - Préparation à possible escalade (publication totale, revente à étatique).
>
> Pour Athéna et Lucas, l'investigation produit :
> - Cas documenté qui enrichit la doctrine interne.
> - Contacts opérationnels avec DGSI renforcés.
> - Compétences éprouvées par cas réel.
> - Référence anonymisée pour publications futures et formation.
>
> **6 mois plus tard** (extrapolation) : pas de publication totale du dump observée. aero_source toujours actif sur l'écosystème (sous ses 3 pseudonymes). Possible : un acheteur final a payé, le dump est passé en circulation privée. Possible : aero_source attend opportunité commerciale meilleure. Possible : la DGSI et partenaires suivent en temps réel sans communiquer.
>
> L'investigation DARKSTREAM aura été **un succès partiel** — pas d'identification personnelle, pas de récupération des données, pas d'arrestation. Mais : confirmation et caractérisation rapides, défense Vectris solide, cadre durable construit. C'est ce que l'investigation privée produit réalistement.

---
