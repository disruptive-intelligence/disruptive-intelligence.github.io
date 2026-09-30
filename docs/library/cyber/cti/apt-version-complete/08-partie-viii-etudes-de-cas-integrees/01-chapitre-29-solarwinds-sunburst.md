---
title: Chapitre 29 — SolarWinds / SUNBURST
source: Cyber/01_CTI/APT_vFULL.md
note: APT — version complète
up:
- - APT — version complète
  - ../index.md
- - Partie VIII — Études DE cas intégrées
  - index.md
---

la supply chain comme vecteur d’espionnage

SolarWinds est le **cas d’école** de la compromission supply chain à très grande échelle menée par un acteur étatique sophistiqué. Il mérite un traitement détaillé — timeline, TTP, attribution, leçons.

## 29.1 Contexte : APT29, SVR, paradigme supply chain

**Acteur** : APT29 / Cozy Bear / Midnight Blizzard — service de renseignement extérieur russe (SVR).

**Paradigme** : la supply chain logicielle comme vecteur d’espionnage stratégique massif. SolarWinds n’était pas la première compromission supply chain étatique — CCleaner (APT17/APT41, 2017), M.E.Doc (Sandworm, 2017 pour NotPetya) l’ont précédée — mais c’est la plus ambitieuse et sophistiquée documentée publiquement.

**Cible SolarWinds** : éditeur de logiciel de supervision réseau basé au Texas. Son produit phare **Orion** est utilisé par **~33 000 organisations** dans le monde, dont une large part du gouvernement fédéral américain, des entreprises Fortune 500, et des infrastructures critiques. C’est précisément cette base installée privilégiée qui en fait une cible APT idéale.

## 29.2 Timeline détaillée

**Septembre-octobre 2019** : activité suspecte détectable rétrospectivement dans l’environnement de développement SolarWinds. Modifications de « test » dans le code Orion — vraisemblablement la phase de reconnaissance et de préparation de l’attaquant.

**Février 2020** : la backdoor **SUNBURST** est injectée pour la première fois dans un build opérationnel d’Orion. Le mécanisme d’injection ciblait spécifiquement le **processus de build** de SolarWinds — pas une compromission de développeur individuel, mais la compromission de l’infrastructure qui compile le code source en binaires signés.

**Mars 2020** : la mise à jour Orion trojanisée (versions 2019.4 HF5, 2020.2, 2020.2 HF1) est distribuée via les canaux officiels SolarWinds. Tous les clients qui mettent à jour (~18 000 organisations) reçoivent SUNBURST. Le malware est **signé avec le certificat légitime SolarWinds** — rien ne le distingue d’une mise à jour normale.

**Mars-juin 2020** : SUNBURST se propage lentement dans les environnements des victimes. Une fois exécuté, il **attend 12 à 14 jours** avant de s’activer — technique d’évasion pour échapper aux sandboxes automatisées qui analyseraient le fichier pendant quelques minutes seulement. Puis il contacte son serveur C2 (`avsvmcloud.com`, domaine au nom évocateur de services cloud/antivirus légitimes).

**Juillet-décembre 2020** : APT29 examine les signaux reçus des ~18 000 environnements infectés et sélectionne **environ 100 cibles de haute valeur** pour l’exploitation approfondie. Le ciblage sélectif est une signature de l’opération — APT29 n’a pas intérêt à être partout, seulement dans les cibles stratégiques. Sur les cibles sélectionnées, les opérateurs déploient des **outils de seconde étape** :

- **TEARDROP** : loader en mémoire.
- **RAINDROP** : variant de loader identifié ultérieurement.
- **GoldMax / SUNSHUTTLE** : backdoor Go cross-platform.
- **GoldFinder** : HTTP tracer pour reconnaissance d’infrastructure.
- **SIBOT** : backdoor VBScript.

Les cibles finales incluent : **Département du Trésor**, **Département du Commerce**, **Département de la Sécurité intérieure (DHS)**, **Département d’État**, **Département de l’Énergie** (y compris NNSA — National Nuclear Security Administration), **Pentagone** (partiellement), **Microsoft**, **FireEye/Mandiant**, et plusieurs autres grandes entreprises et agences.

**8 décembre 2020** : **FireEye** annonce publiquement avoir été compromis et avoir eu des outils Red Team volés.

**13 décembre 2020** : FireEye publie ses conclusions — l’intrusion chez FireEye provenait de SolarWinds Orion compromis. Publication simultanée d’un rapport technique détaillé sur SUNBURST. L’ensemble de l’écosystème CTI commence à enquêter.

**14 décembre 2020** : SolarWinds confirme la compromission, publie des indicateurs.

**15-20 décembre 2020** : Microsoft et d’autres entités confirment des compromissions. **CISA** publie une Emergency Directive ordonnant aux agences fédérales US de déconnecter Orion ou de le mettre à jour vers une version saine.

**Janvier 2021** : **attribution officielle** par le gouvernement américain — ODNI, NSA, FBI, CISA attribuent à APT29 / SVR russe. L’attribution est renforcée ultérieurement avec le ralliement de Five Eyes + UE en avril 2021.

## 29.3 TTP détaillées — mapping ATT&CK

SolarWinds est un cas d’étude très documenté en ATT&CK. Techniques principales observées :

- **T1195.002 — Supply Chain Compromise: Compromise Software Supply Chain** : injection de SUNBURST dans le build pipeline SolarWinds.
- **T1218 — Signed Binary Proxy Execution** : SUNBURST est un composant légitime d’Orion, signé numériquement.
- **T1036 — Masquerading** : domaines C2 (avsvmcloud.com, etc.) au nom évocateur de services cloud légitimes. Sous-domaines construits pour ressembler à des requêtes normales.
- **T1071 — Application Layer Protocol: Web Protocols** : C2 HTTPS avec DNS queries de type DNS-over-HTTPS.
- **T1087 — Account Discovery** : énumération des comptes Active Directory.
- **T1550 — Use Alternate Authentication Material** : **GoldenSAML** — forgeage de tokens SAML via compromission d’ADFS, accès aux ressources Azure AD / O365 sans authentification classique.
- **T1528 — Steal Application Access Token** : vol de tokens OAuth Azure AD.
- **T1114 — Email Collection** : accès aux boîtes mail via Graph API en utilisant les tokens SAML forgés.
- **T1078 — Valid Accounts** : usage de comptes légitimes pour le mouvement latéral.
- **T1041 — Exfiltration Over C2 Channel**.

Le chaînage de ces techniques — supply chain → persistence furtive → forgeage d’identité cloud → accès données — est le paradigme que SolarWinds a établi pour les opérations APT cloud modernes.

## 29.4 GoldenSAML : l’innovation pivot

Le pivot **GoldenSAML** mérite une explication technique dédiée car il est devenu une référence.

**Principe ADFS** : Active Directory Federation Services (ADFS) est le composant Microsoft qui permet l’authentification fédérée. Quand un utilisateur se connecte à Azure AD / O365, ADFS (si configuré) génère un **token SAML** signé par la clé privée d’ADFS. Ce token est présenté à Azure AD comme preuve d’authentification — Azure AD fait confiance à la signature ADFS et autorise l’accès.

**L’attaque GoldenSAML** : l’attaquant qui compromet le serveur ADFS et vole la **clé privée de signature** peut **forger ses propres tokens SAML** pour n’importe quel utilisateur, avec n’importe quels attributs. Azure AD ne peut pas distinguer un token légitime d’un token forgé — la signature est valide.

**Conséquences** :

- L’attaquant peut **se faire passer pour n’importe quel utilisateur**, y compris des administrateurs globaux.
- Accès à **Exchange Online** (lecture de tous les emails), **SharePoint** (tous les documents), **Teams**, **OneDrive**.
- **Persistence sans malware** : tant que la clé n’est pas renouvelée, l’attaquant garde l’accès, sans aucun code malveillant déposé côté cloud.
- **Très difficile à détecter** : les logs Azure AD montrent des authentifications légitimes (tokens valides, signature correcte).

**Remédiation** : nécessite la **régénération des clés ADFS**, idéalement la **reconstruction complète d’ADFS**, et l’audit de tous les accès effectués depuis la compromission — opération lourde qui peut durer des mois.

GoldenSAML, déjà connu théoriquement avant 2020, est devenu **opérationnellement célèbre** avec SolarWinds. D’autres acteurs (notamment chinois) ont adopté la technique ensuite.

## 29.5 Découverte par FireEye/Mandiant

La découverte de SolarWinds est elle-même une histoire remarquable. FireEye enquêtait sur une intrusion dans son propre environnement — les attaquants avaient volé des outils Red Team. L’investigation interne a remonté jusqu’au vecteur : Orion compromis. FireEye a alors compris que tous ses clients utilisant Orion étaient potentiellement compromis, et au-delà — que l’ensemble du parc Orion dans le monde était compromis.

**La décision de publication** : FireEye aurait pu traiter l’incident en privé. L’entreprise a choisi la **publication rapide et détaillée** (rapport SUNBURST publié dès le 13 décembre 2020). Cette décision, courageuse commercialement (révéler publiquement une compromission est coûteux en réputation), a permis à l’écosystème entier de réagir. C’est devenu un **cas emblématique de l’importance de la transparence** en cybersécurité.

**Kevin Mandia** (alors PDG de FireEye) a conduit les communications publiques. L’entreprise a été saluée pour son approche — le rapport technique est devenu une référence, et la transparence a renforcé (contre-intuitivement) la confiance des clients.

## 29.6 L’attribution et ses suites

**Attribution officielle** :

- **Janvier 2021** : ODNI, NSA, FBI, CISA attribuent à un acteur russe, probablement le SVR. Confiance : élevée.
- **Avril 2021** : attribution renforcée, mention explicite du SVR. **Sanctions** — l’administration Biden annonce des sanctions contre la Russie (incluant expulsions de diplomates, sanctions financières ciblées).
- **UE et Five Eyes** se coordonnent sur l’attribution.

**Pas d’indictment DOJ** pour SolarWinds (contrairement à certaines autres opérations russes) — probablement parce que les opérateurs individuels sont protégés par le contexte et que l’attribution au niveau étatique était jugée suffisante.

**Pas de représailles cyber déclarées** — les États-Unis ont choisi de répondre par sanctions et diplomatie, pas par action cyber offensive publique en représailles directes.

## 29.7 Impact et réponse structurelle

**Impact immédiat** :

- **Dwell time** : APT29 avait maintenu l’accès aux environnements les plus sensibles pendant **6 à 12 mois** (voire plus) avant détection.
- **Renseignement collecté** : quantité et nature classifiées, mais probablement massive — emails gouvernementaux US stratégiques, plans, communications diplomatiques.
- **Impact sur la confiance** : ébranlement de la confiance dans la supply chain logicielle. SolarWinds, grand éditeur respecté, était compromis — la question « qui d’autre ? » s’est imposée.

**Réponse structurelle** :

**Executive Order 14028 (mai 2021)** — « Improving the Nation’s Cybersecurity » : réponse américaine majeure à SolarWinds. Exigences :

- **SBOM** (Software Bill of Materials) obligatoire pour les fournisseurs du gouvernement fédéral.
- **Zero Trust** architecture dans les agences fédérales.
- **Amélioration du partage d’information** entre agences et avec CISA.
- **Critical software definition** et contrôles associés.
- **Endpoint Detection and Response** généralisé sur les endpoints fédéraux.

**Cyber Safety Review Board (CSRB)** : création en 2022 sur le modèle du NTSB (investigation d’accidents aériens). Le CSRB investigue les incidents cyber majeurs et publie des rapports. Son premier rapport (juillet 2022) portait sur Log4j ; d’autres ont suivi (Lapsus$, Storm-0558).

**Changements dans l’industrie** : durcissement des build pipelines (isolation, reproducibility, signatures multi-factorielles), Zero Trust sur les mises à jour, monitoring du plan de contrôle identity cloud.

## 29.8 Leçons opérationnelles

SolarWinds a produit un **corpus de leçons** qui structurent la pratique cyber contemporaine.

**La supply chain logicielle est un vecteur APT majeur** : tous les éditeurs sont des cibles potentielles. Les acheteurs doivent intégrer ce risque dans leurs évaluations.

**La confiance implicite dans un éditeur ne protège pas** : une mise à jour signée par un éditeur légitime peut contenir une backdoor. Le monitoring comportemental des processus, même légitimes, reste indispensable.

**Le monitoring identity cloud est critique** : GoldenSAML, abus OAuth, tokens SAML forgés — la détection d’anomalies dans le plan de contrôle identity est un domaine à part entière de la défense moderne.

**Zero Trust s’impose** : appliqué aux fournisseurs, aux mises à jour, aux authentifications — la confiance ne peut plus être implicite.

**L’intégrité du build pipeline est un enjeu stratégique** : les éditeurs logiciels doivent investir dans la sécurité de leur processus de build (isolation, signatures, audit, reproducibility).

**La transparence bénéficie à l’écosystème** : la décision FireEye de publier rapidement a permis à tous les défenseurs de réagir. Ce modèle de divulgation coordonnée est devenu une référence.

**L’attribution publique coordonnée impose un coût** : les sanctions et expulsions diplomatiques n’ont pas empêché APT29 de continuer, mais elles ont imposé un coût réel à la Russie. L’effet n’est pas nul.

-----
