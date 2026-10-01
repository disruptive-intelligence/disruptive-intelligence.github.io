---
title: Chapitre 27 — Tendances 2024-2026 et signaux d’anticipation
source: Cyber/01 CTI & renseignement/Menace cyber/APT — menaces persistantes avancées.md
note: APT — menaces persistantes avancées
up:
- - APT — menaces persistantes avancées
  - ../index.md
- - Partie VII — Géopolitique, attribution et prospective
  - index.md
---

## 27.1 Exploitation massive des appliances edge

La tendance n°1 du paysage cyber contemporain : l’**exploitation des appliances edge exposées sur Internet**. VPN, firewalls, passerelles mail, appliances de sécurité elles-mêmes sont devenues le vecteur d’entrée privilégié des APT sophistiquées.

**Vagues notables 2023-2026** :

- **Ivanti Connect Secure** : CVE-2023-46805, CVE-2024-21887, CVE-2024-21888 exploitées par plusieurs acteurs (Volt Typhoon, APT40, APT31, clusters non identifiés). Vague massive début 2024.
- **Fortinet FortiOS** : multiples CVE 2022-2024 exploitées par APT40 et autres.
- **Citrix ADC/NetScaler** : CVE-2023-4966 (« Citrix Bleed »), CVE-2023-3519 exploitées par APT29, APT40, acteurs ransomware.
- **Barracuda Email Security Gateway** : CVE-2023-2868 exploitée par UNC4841 (Chine) pendant 8 mois avant découverte.
- **Palo Alto GlobalProtect** : CVE-2024-3400 exploitée mi-2024.
- **Cisco IOS XE** : CVE-2023-20198 exploitation massive fin 2023.

**Pourquoi cette concentration** :

- **Pas d’EDR sur les appliances** : les appliances réseau ne peuvent pas faire tourner d’agents de détection endpoint. La visibilité est limitée aux logs (parfois insuffisants).
- **Exposition Internet par construction** : une VPN gateway doit être accessible depuis Internet, donc exposée aux scans massifs des attaquants.
- **Credentials privilégiés en aval** : compromettre une appliance de sécurité donne souvent un accès privilégié au réseau interne (VPN → accès réseau, firewall → capacité de manipulation des flux, passerelle mail → accès aux communications).
- **Patching complexe** : les appliances sont souvent en production continue, leur patching est planifié et parfois retardé.
- **Vulnérabilités nombreuses** : les appliances de sécurité ont des vulnérabilités comme les autres logiciels — le paradoxe consiste à ce que les outils de défense deviennent des vecteurs d’attaque.

**Défense** : surveillance renforcée des appliances (logs exhaustifs, SIEM intégré), patching d’urgence (suivre KEV CISA), durcissement des configurations (désactiver les composants non-nécessaires), monitoring réseau entourant les appliances.

## 27.2 Ciblage de l’identité cloud

L’**identité cloud** est devenue le nouveau périmètre. Les APT ciblent massivement Azure AD/Entra ID, les tokens SAML/OAuth, les mécanismes MFA.

**Tactiques dominantes** :

- **Password spraying sur Azure AD** : volume massif, taux de succès faible par tentative mais cumul efficace. APT33 (Iran) et APT29 (Russie) en font un usage systématique.
- **Abus OAuth** : création d’applications OAuth malveillantes ou détournement d’applications existantes avec des permissions Graph API excessives. Accès persistant sans mot de passe, contourne la MFA. Signature APT29.
- **Vol de tokens (pass-the-cookie, pass-the-token)** : réutilisation de sessions authentifiées volées via infostealers ou AitM phishing. Contourne la MFA.
- **AitM phishing avec Evilginx et équivalents** : proxy malveillant qui intercepte les credentials ET les cookies de session. Contourne la MFA. Utilisé massivement par acteurs étatiques et cybercriminels.
- **GoldenSAML** : forgeage de tokens SAML via compromission d’ADFS. Technique pivot de SolarWinds, toujours utilisée.
- **MFA fatigue** : bombardement de notifications push pour inciter la victime à en accepter une par lassitude. Technique de base mais efficace.
- **Compromission de comptes de service** : les comptes de service (applications, systèmes) ont souvent des permissions larges et des mécanismes d’authentification plus faibles (clés API, secrets partagés).

**Vulnérabilité structurelle** : une compromission cloud bien installée peut survivre à la réinstallation complète de tous les endpoints. La remédiation nécessite de révoquer les tokens, recréer les applications OAuth, auditer les permissions, changer les secrets — opérations complexes et souvent incomplètes.

**Défense** :

- **MFA résistant au phishing** : FIDO2 / WebAuthn / clés hardware (YubiKey). Ne tombe pas à l’AitM.
- **Conditional Access** : règles basées sur le contexte (device, location, risk signals).
- **Monitoring OAuth et consents** : détecter les applications OAuth avec consent admin, les permissions Graph API excessives, les anomalies d’authentification.
- **Privileged Identity Management (PIM)** : activation just-in-time des rôles privilégiés, pas de standing admin.
- **Identity threat detection** : outils dédiés (Microsoft Defender for Identity, CrowdStrike Identity Threat Protection, Okta ITDR).

## 27.3 Convergence crime-État

La **convergence entre cybercrime et action étatique** est une tendance structurelle déjà largement évoquée dans les parties précédentes.

**Manifestations principales** :

- **APT41** (Chine) : double mission espionnage/cybercrime personnel assumée.
- **Ransomware russophone sous tolérance tacite** : LockBit, BlackBasta, Play, Royal, ALPHV, Cl0p.
- **DPRK/Lazarus** : méthode criminelle (cybervol crypto), finalité étatique (financement régime).
- **Infostealers et IAB** : cybercriminels qui fournissent involontairement des accès aux APT étatiques via la revente sur marchés dark web.
- **Hacktivisme instrumentalisé** : KillNet, NoName057(16), IT Army of Ukraine.

**Implications** :

- **Attribution plus complexe** : face à une compromission, distinguer si l’acteur est purement criminel, purement étatique, ou entre les deux est souvent difficile.
- **Réponse adaptée** : les mesures qui fonctionnent contre le cybercrime (démantèlements d’infrastructure, sanctions économiques) sont moins efficaces contre les APT étatiques. Les mesures diplomatiques qui fonctionnent contre les APT sont sans effet sur les cybercriminels. La zone grise nécessite des approches mixtes.
- **Tendance à la professionnalisation** : le cybercrime devient plus sophistiqué sous l’influence des TTP étatiques ; les APT empruntent les techniques criminelles (infostealers, IAB) pour l’efficacité.

**Trajectoire 2024-2026** : la convergence va probablement s’approfondir. Les distinctions « pur crime » vs « pur État » deviendront de moins en moins nettes.

## 27.4 LotL comme standard

Le **Living off the Land** est passé d’une technique avancée à un **standard** des APT sophistiquées.

**Volt Typhoon** a démontré qu’une opération étatique sophistiquée de pré-positionnement peut être conduite **sans aucun malware custom**. Son modèle se diffuse : de plus en plus d’acteurs adoptent des approches LotL-heavy pour maximiser la furtivité.

**Implications pour la défense** :

- Les signatures EDR classiques (hash de fichiers, strings de malware) détectent moins.
- La détection doit être **comportementale** : patterns d’usage des LOLBins, contextes d’exécution, chaînes de processus.
- Les baselines comportementales deviennent cruciales — identifier qu’un `ntdsutil` exécuté par un compte admin depuis un serveur non-DC est anormal nécessite de savoir ce qui est normal.
- Le **threat hunting proactif** prend de l’importance sur la détection automatique passive.

**Outils défensifs adaptés** : EDR modernes qui surveillent les **chaînes de processus** et les **patterns comportementaux** (Microsoft Defender for Endpoint, CrowdStrike Falcon, SentinelOne, Carbon Black, Palo Alto Cortex XDR) plutôt que les signatures seules. SIEM avec règles de détection comportementales.

## 27.5 IA offensive : phishing, deepfakes, aide au développement

L’**IA générative** (LLM et génération multimédia) entre dans l’arsenal offensif. Impact croissant, encore émergent.

**Phishing amélioré par LLM** : les emails de phishing sont rédigés dans un langage natif et contextuel parfait, sans les erreurs linguistiques caractéristiques des campagnes non-natives. L’avantage historique des anglophones sur les campagnes de phishing ciblant les entreprises anglophones (vs attaquants non-anglophones avec erreurs) est en train de disparaître. APT iraniens, chinois, russes produisent désormais des emails de phishing indiscernables linguistiquement de correspondants légitimes.

**Deepfakes vocaux** : impersonation vocale de dirigeants pour des attaques BEC (Business Email Compromise) au téléphone. Cas documentés : un employé finance convaincu par téléphone que le CFO lui demande un virement urgent, pour découvrir plus tard qu’il s’agissait d’une voix synthétique. Les deepfakes audio sont techniquement plus accessibles que les deepfakes vidéo et leur utilisation criminelle s’industrialise.

**Deepfakes vidéo** : cas documentés en Asie (vidéoconférences truquées où plusieurs participants étaient des deepfakes d’employés légitimes, aboutissant à des transferts frauduleux de dizaines de millions). Technique coûteuse mais accessible aux acteurs sophistiqués.

**Aide au développement de malware** : les LLM peuvent aider à générer du code offensif — scripts d’exploitation, évasions EDR, obfuscations. Les garde-fous des LLM commerciaux (OpenAI, Anthropic, Google) filtrent beaucoup de demandes manifestement malveillantes, mais les LLM open source ou partiellement contournés offrent moins de résistance. Impact : accélération du développement par les acteurs sophistiqués, accessibilité accrue pour les acteurs moyens.

**Reconnaissance et profilage assistés** : LLM utilisés pour agréger des données OSINT sur des cibles, identifier des vulnérabilités humaines (points d’approche social engineering), générer des leurres personnalisés.

**État actuel (2026)** : l’IA offensive augmente la **productivité** des attaquants mais n’a pas encore produit de rupture capacitaire qualitative. Les opérations restent conduites par des humains avec outillage IA, pas entièrement automatisées. La trajectoire à moyen terme (2027-2030) est incertaine — l’automatisation croissante des attaques via agents IA est une menace anticipée mais pas encore massivement observée.

## 27.6 Pré-positionnement dans les infras critiques

la menace structurelle

Le **pré-positionnement** (Ch.22) est probablement **la menace structurelle qui définira la prochaine décennie**. Plusieurs dynamiques l’amplifient :

**Volt Typhoon comme modèle** : démontre qu’un pré-positionnement prolongé sans détection est possible. Ce modèle va être répliqué par d’autres acteurs.

**Extension géographique** : au-delà des US, l’Europe est désormais une cible crédible de pré-positionnement (par la Russie et la Chine). L’Asie-Pacifique également (par la Chine).

**Dilemmes de réponse non résolus** : éradiquer vs surveiller, communiquer publiquement vs rester discret — ces dilemmes restent non tranchés systématiquement. Chaque cas fait l’objet de décisions ad hoc.

**Manque de maturité défensive** : beaucoup d’opérateurs d’infrastructures critiques n’ont toujours pas les moyens (visibilité OT, threat hunting, collaboration) pour détecter un pré-positionnement sophistiqué. La maturité nécessite des années à construire.

**Tensions géopolitiques** : Taïwan, Ukraine, Moyen-Orient, rivalités économiques. Les tensions croissantes augmentent la probabilité d’**activations** potentielles de pré-positionnements existants — ce qui augmente la gravité du problème.

## 27.7 Ciblage des télécoms et interception

**Salt Typhoon** (2024) a démontré l’ampleur du ciblage télécom par des acteurs étatiques. Cette tendance va s’amplifier.

**Pourquoi les télécoms** :

- **Accès aux communications** : appels, SMS, métadonnées de millions d’utilisateurs.
- **Systèmes d’interception légale** : compromettre les systèmes CALEA permet de voir qui les autorités surveillent — contre-espionnage de haute valeur.
- **Position centrale** : les télécoms ont accès à tout le trafic de leurs clients — un point de collecte privilégié.
- **Compromission difficilement détectable** : les infrastructures télécoms sont complexes, avec beaucoup d’équipements hérités et de sous-traitance.

**Implications** :

- Les personnalités à haut risque (opposants politiques, journalistes, militants, dirigeants d’entreprise critique) doivent supposer que leurs communications **non chiffrées de bout en bout** peuvent être compromises.
- Le passage à Signal, WhatsApp, iMessage (messageries E2EE) est devenu une recommandation standard, y compris par les autorités US post-Salt Typhoon.
- La souveraineté télécom redevient un enjeu stratégique — dépendre d’opérateurs étrangers (notamment chinois dans certains pays) pose des questions sécuritaires nouvelles.

## 27.8 Supply chain continues et éditeurs logiciels

Les **compromissions supply chain** restent un vecteur APT majeur. Tendances 2024-2026 :

**Ciblage des éditeurs logiciels tier 1** : Microsoft, SolarWinds, Kaseya, JetBrains ont été compromis dans des opérations majeures. La tendance ne faiblit pas — les éditeurs restent des cibles à très fort effet de levier.

**Cascades supply chain** (modèle 3CX) : compromission d’un éditeur via un autre éditeur compromis. Niveau d’imbrication qui complique l’attribution et la remédiation.

**Compromission de dépendances open source** : packages npm, PyPI, GitHub compromis pour injecter du malware dans les chaînes de build de multiples projets. Cas récents documentés en quantité croissante.

**Contractors et MSP** : les prestataires IT sont des cibles indirectes. Compromettre un MSP donne accès à ses clients (modèle Cloud Hopper d’APT10, toujours réplicable).

**Défense** :

- Zero Trust appliqué à la supply chain (ne pas faire confiance aux fournisseurs par défaut).
- Software Bill of Materials (SBOM) : obligations émergentes aux États-Unis (EO 14028) et en Europe (Cyber Resilience Act).
- Monitoring des processes fournisseurs (intégrité du build pipeline, signatures, reproductibilité).
- Évaluation de risques de la supply chain (obligation NIS 2).

## 27.9 Signaux géopolitiques à surveiller

Les analystes cyber doivent suivre plusieurs signaux géopolitiques qui affectent le paysage de la menace.

**Tensions autour de Taïwan** : une escalade militaire dans le détroit de Taïwan activerait probablement des pré-positionnements chinois existants. Les indicateurs : augmentation des exercices militaires PLA, déclarations politiques, mouvements diplomatiques.

**Évolution de la guerre en Ukraine** : intensification ou désescalade affectera les opérations russes destructives et d’influence. Les cessations de conflit ne signifient pas la fin des opérations cyber — elles peuvent simplement changer de forme.

**Élections majeures** : élections présidentielles et législatives dans les grandes démocraties sont des cibles récurrentes d’ingérence étrangère. Les services CTI montent typiquement leur vigilance à l’approche des échéances électorales.

**Sanctions et escalade économique** : l’introduction de nouvelles sanctions peut déclencher des ripostes cyber (Iran contre l’Albanie en 2022 après hébergement du MEK — précédent).

**Crises énergétiques** : tensions sur l’approvisionnement énergétique (Europe post-2022, tensions Moyen-Orient) augmentent le ciblage des infrastructures énergétiques.

**Crises médicales ou sanitaires** : pandémies ou crises sanitaires majeures produisent des vagues de cyberattaques opportunistes + étatiques (ciblage santé COVID par APT russes et chinois en 2020).

Pour l’analyste, maintenir une **veille géopolitique** parallèle à la veille technique est essentiel. Les deux s’alimentent réciproquement.

-----
